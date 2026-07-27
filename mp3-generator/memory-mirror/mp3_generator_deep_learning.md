---
name: mp3_generator_architecture
description: "Deep learning notes on MP3 Generator architecture, config system, and generation flow"
metadata: 
  node_type: memory
  type: project
  originSessionId: d38ba609-545e-4921-addc-02aedf6f4cee
---

# MP3 Mandarin Generator — Architecture & Code Flow

**Level:** Advanced Technical Reference  
**Version:** 3.7 (ZIP SAFE)  
**Last Updated:** 2026-07-25  

---

## 🏗️ Core Architecture

### **Application Structure**

**Stack:**
- Python 3.13 (PyInstaller bundled as .exe)
- edge-tts (Microsoft TTS service)
- ffmpeg 8.1.1 (audio processing)
- tkinter (GUI)
- Async/threading (concurrent generation)

**Files:**
- `MP3 GENERATOR 3.7.exe` — Standalone executable
- `config/config_gui.json` — Current settings
- `config/presets_gui.json` — Saved presets

**Key Limitation:** PyInstaller does NOT bundle ffmpeg
- ffmpeg must be in Windows PATH or local folder
- Current PATH setup: `C:\WT on C\Master\ffmpeg-8.1.1-essentials_build\bin`

---

### **Configuration System**

**DEFAULT_CONFIG (Line 63-90):**
```python
{
  "sequence": ["Mand KW", "Mandarin", "English", "Diam"],  # Which columns to read + delays
  "delay_after_ms": [2000, 2000, 1000, 0],                 # Wait after each item
  "rows": "all",                                            # Which rows to process
  "global_tts_speed": "1.0",                               # Speed multiplier
  "advanced_rate": False,                                  # Per-language rate control?
  "rates": {"zh": "+0%", "en": "+0%", "id": "+0%"},       # Rate adjustments
  "voices": {
    "zh": "zh-CN-XiaoxiaoNeural",                          # Mandarin voice
    "en": "en-US-JennyNeural",                             # English voice
    "id": "id-ID-GadisNeural",                             # Indonesian voice
  },
  "output_folder": "output_mp3",                           # Where MP3s go
  "skip_existing": True,                                  # Don't re-generate if exists
  "generate_mode": "long",                                 # "long" or "library"
  "zip_all": False,                                        # Create ZIP of all MP3s
}
```

**Presets (Line 92-126):**
- **Listening:** Mand KW → Mandarin → English (default speeds)
- **Shadowing:** Mandarin → Mandarin → English (0.9x slower for shadowing)
- **Vocabulary:** Mand KW → Indo KW → Eng KW (random order, great for testing)

**Why Nested Config + Presets?**
- `config_gui.json` = user's current settings (persistent)
- `presets_gui.json` = saved presets for quick reuse
- `deep_merge()` (line 149): new presets overwrite only their keys, keep defaults

---

### **Generation Modes**

**Mode 1: "long" (Per Sheet)**
```
Input: CSV with multiple rows
Process: Read sheet name → generate one long MP3
         All rows concatenated with delays
Output: One big MP3 file
         filename: [sheet_name].mp3
Use case: Full lesson playback
```

**Mode 2: "library" (Per Cell) — naming scheme changed 2026-07-23, see [[mp3_no_based_naming_migration_plan]] for full history**
```
Input: CSV with multiple rows, multiple columns
Process: For each (row, column) → generate individual MP3
         Named: [prefix]_[No]_[column].mp3, where "No" is the raw CSV "No" cell value
         (e.g. "1a", "1b", "10i") — NOT an int-parsed row index anymore.
         Matches HTML Player's naming convention (also reverted to "No" 2026-07-25).
Output: Many small MP3 files
         Ex: 010_1a_mandkw.mp3, 010_1d_mandarin.mp3, 010_2g_engkw.mp3, ...
Use case: HTML Player background playback (screen off needs fast loading)
```
- `read_rows_numbered()` (~line 261) no longer does `int(raw_no)` — it uses `safe_name(raw_no)`
  (the existing filesystem-safe-name helper) directly, so letter-suffixed "No" values survive
  as-is. Falls back to physical CSV row position only when "No" is blank.
- `library_filename()` (~line 314): `f"{prefix}_{row_no}_{key}.mp3"` — no more `_r` prefix, no
  more zero-padding (didn't make sense for alphanumeric IDs).
- **Output folder layout changed 2026-07-25:** `library_output_dir_for()` now returns
  `{output_folder}/Per Cell MP3/{sheet_name}/` (was `{output_folder}/{sheet_name}/` directly) and
  `library_zip_output_dir()` now returns `{output_folder}/Per Cell ZIP/` (was
  `{output_folder}/ZIP/`) — both are now explicit, clearly-named siblings directly under the
  output folder, instead of per-sheet MP3 folders sitting unlabeled at the output root next to a
  generically-named "ZIP" folder. UI label near the ZIP checkboxes updated to match. Verified with
  a real generated file: `output/Per Cell MP3/<sheet>/<file>.mp3`.
- This was previously "PENDING" — now done and verified end-to-end (real MP3s generated + played
  in HTML Player). See the migration plan file for full verification detail and history of why
  this changed (a "Ref." column briefly existed as a stopgap, since removed from the matching
  logic on both sides).

---

### **Generation Pipeline**

**High-Level Flow:**

```
User clicks Generate
  ↓
load_config() + load_presets()
  ↓
start_generate() (threaded, non-blocking UI)
  ↓
If mode=="long": generate_long(files, config)
If mode=="library": generate_library_all(files, config)
  ↓
For each input file:
  Parse CSV (detect delimiter)
  ↓
  For each row:
    Extract columns per sequence
    ↓
    make_tts_and_silence(text, lang, speed)
      ├─→ edge_tts.Communicate().save()  [Get raw MP3]
      ├─→ If speed != 1.0:
      │     ffmpeg -filter:a atempo      [Adjust speed]
      └─→ Return adjusted MP3
    ↓
    If column == "Diam":
      make_silence(duration)              [Generate silence]
    ↓
    Collect MP3 segments
  ↓
  concat_mp3(segments, output_file)       [Merge all segments]
    └─→ ffmpeg -f concat                  [Chain MP3s together]
  ↓
  If zip_mode: Add to ZIP
  ↓
Output: MP3 files ready to use
```

---

## 🔑 Key Functions

### **TTS + Speed Control: make_tts_and_silence() (Line 480+)**

```python
async def make_tts_and_silence(text, lang, speed=1.0, voice=None):
    """Generate TTS MP3 with optional speed adjustment."""
    
    # 1. Generate raw TTS via edge-tts
    raw_mp3 = await edge_tts.Communicate(text=text, voice=voice).save(...)
    
    # 2. If speed != 1.0, adjust via ffmpeg
    if speed != 1.0:
        # ffmpeg -filter:a atempo=[speed] raw.mp3 output.mp3
        # atempo = preserve pitch, change speed (not transpose)
        return adjusted_mp3
    
    return raw_mp3
```

**Why atempo (not speed)?**
- atempo: changes speed, preserves pitch (naturel)
- speed: changes playback speed, lowers pitch (sounds like chipmunk at 2x)
- User preference: preserve pitch, adjust tempo only

---

### **Silence Generation: make_silence() (Line 504+)**

```python
def make_silence(duration_ms):
    """Generate silence MP3 using ffmpeg anullsrc."""
    # ffmpeg -f lavfi -i anullsrc=r=44100:cl=mono -t [duration_sec] silence.mp3
    # Uses ffmpeg null audio source (no external audio file needed)
    return mp3_bytes
```

**Why anullsrc?**
- No need for template silence file
- Generated on-the-fly, exact duration
- Works for "Diam" (silence) in sequence

---

### **MP3 Concatenation: concat_mp3() (Line 519+)**

```python
def concat_mp3(parts, out_file):
    """Merge multiple MP3 parts into single file."""
    # 1. Create concat demux file
    concat_list = "file 'part1.mp3'\nfile 'part2.mp3'\n..."
    
    # 2. ffmpeg -f concat -safe 0 -i concat.txt -c copy output.mp3
    # -f concat: use concat demux format
    # -c copy: copy streams (no re-encoding, fast)
    #          (re-encoding would be slow + quality loss)
    return output_file
```

**Why -c copy (not re-encode)?**
- All input MP3s already encoded (edge-tts + ffmpeg)
- Re-encoding = slowest step
- Copy = just join segments (fast)
- Quality: no degradation (already compressed)

---

### **Generation Entry Point: start_generate() (Line 1636+)**

```python
def start_generate(self):
    """Main entry point for generation (threaded)."""
    # 1. Load current config/presets
    # 2. Get input CSV files
    # 3. Get mode (long vs library)
    # 4. Spawn thread with generate_long() or generate_library()
    # 5. Update progress UI real-time
    # 6. Handle errors (show messagebox)
```

**Thread Model:**
- UI runs on main thread (tkinter)
- Generation runs on worker thread
- Queue for progress updates → UI thread
- Result: UI stays responsive while generating

---

## 🔄 Integration with HTML Player

**Naming Convention (current, since 2026-07-23/25 — see [[mp3_no_based_naming_migration_plan]] for full history):**
```
Row "No"=1a:
  010_1a_mandkw.mp3     ← "Mand KW" column
  010_1a_mandarin.mp3   ← "Mandarin" column
  010_1a_english.mp3    ← "English" column

Row "No"=1b:
  010_1b_mandkw.mp3
  010_1b_mandarin.mp3
  010_1b_english.mp3
```

**Matching Logic:**
- HTML Player: `mp3CandidateNames(tr)` reads the row's "No" cell (`getRowIndexFromTr()`,
  `HTML_mandarin_v25_11_100.html:641`) → `["010_1a_mandkw.mp3", ...]`
- Generator: `library_filename()` creates files matching this exact pattern from the same "No"
  cell value in the source CSV
- **Both tools now key off the CSV's "No" column value directly — not row position, not a
  separate "Ref." column.** A "Ref." column briefly existed as a stopgap (because Generator's old
  code could only parse pure integers) — it's no longer read by either tool as of 2026-07-25 and
  is free for the user to repurpose.
- Verified end-to-end 2026-07-23/25: real MP3s generated from `Text File\Breakdown\010 Break
  tes.csv`, uploaded into HTML Player along with the generated ZIP, played successfully.

---

## ⚙️ Configuration Deep Dive

### **Sequence + Delay**

```python
"sequence": ["Mand KW", "Mandarin", "English", "Diam"],
"delay_after_ms": [2000, 2000, 1000, 0],

# Playback flow:
# 1. Read "Mand KW" column → generate MP3 → play
# 2. Wait 2000ms (2 sec)
# 3. Read "Mandarin" column → generate MP3 → play
# 4. Wait 2000ms (2 sec)
# 5. Read "English" column → generate MP3 → play
# 6. Wait 1000ms (1 sec)
# 7. Read "Diam" (silence marker) → generate silence → play
# 8. Wait 0ms (no wait)
# 9. Next row starts
```

**Why Delay Array?**
- Different content needs different pause
- Keyword learning: longer pause for thinking
- Sentence: less pause (context helps)
- Silence: no pause after (already silent)

---

### **Trailing Silence on "long" mode (per-sheet) outputs**

Both `generate_one()` (single file per sheet, ~line 549) and `generate_merged()` (multiple CSVs
merged into one sheet, ~line 627) append one final silence segment after all rows, so playback
doesn't cut off abruptly at end-of-file. **Changed 2026-07-25: 12 seconds → 10 seconds**
(`make_silence(10000, final_silence)` in both functions; filename segment `_final_10000` too).
`DEFAULT_CONFIG["final_delay_ms"]` and the two places that force it back to a fixed value on
config load (~line 158, ~line 544) were updated to `10000` for consistency, though note this
config key isn't actually read anywhere else in the code — the real trailing-silence duration is
the hardcoded `10000` literal in the two `make_silence()` calls above; if changing this again,
update both call sites (and this config key, for consistency) together. "library" mode (per cell)
has no trailing silence — this only applies to "per sheet" output.

---

### **Language Mapping**

```python
LANG_BY_COLUMN = {
    "Mand KW": "zh",          # Mandarin TTS
    "Mandarin": "zh",         # Mandarin TTS
    "Pin Yin KW": "zh",       # Mandarin TTS (pinyin)
    "Pin Yin": "zh",          # Mandarin TTS (pinyin)
    "English": "en",          # English TTS
    "Eng KW": "en",           # English TTS
    "Indonesia": "id",        # Indonesian TTS
    "Indo KW": "id",          # Indonesian TTS
}
```

**Alias Support (Line 39-47):**
- User can use different column names
- Aliases automatically resolved
- Ex: "Hanzi KW" → "Mand KW", "English KW" → "Eng KW"

---

## 🚀 Known Limitations

| Issue | Cause | Workaround |
|-------|-------|-----------|
| Network dependency | edge-tts needs internet | Check connection before generate |
| No offline mode | TTS cloud-based | Consider Pico TTS alternative (future) |
| Speed adjustment slow | ffmpeg re-encode | Skip speed adjustment if possible |
| FFmpeg PATH required | PyInstaller doesn't bundle | Ensure PATH setup or copy ffmpeg.exe locally |

---

## 💡 Modification Guidelines

**Safe Modifications:**
- Add new presets (copy Listening, modify sequence/delays)
- Adjust default voices
- Add new languages (if TTS service supports)
- Change output folder or naming

**Risky Modifications:**
- Changing `make_tts_and_silence()` → breaks speed control
- Changing `concat_mp3()` → may create corrupted MP3s
- Changing `read_rows_numbered()` / `library_filename()` row-identifier logic → MUST stay in sync
  with HTML Player's `getRowIndexFromTr()` (reads the same "No" column) or MP3 filenames stop
  matching between the two tools — see [[mp3_no_based_naming_migration_plan]]
- Threading model → race conditions risk
- Changing the trailing-silence duration in only ONE of `generate_one()` /`generate_merged()` →
  inconsistent behavior between single-file and merged-file "per sheet" output (see above, both
  must be changed together)

**Rebuilt & deployed 2026-07-25:** clean PyInstaller build (`--onefile --windowed`, standard spec,
no custom hooks) from the source above, after all the No-based naming / final-delay / Per Cell
folder changes. Build succeeded (~13.3MB, same ballpark as before). Verified twice by actually
launching the exe (not just checking it exists) — first the freshly built one in `dist\`, then
again after copying it over the production one — both times it opened, ran, and generated its own
fresh `presets_gui.json`/`config_gui.json` next to itself, confirming no crash-on-launch. Note:
first launch of a freshly-built unsigned exe took noticeably long (Windows Defender scanning it),
not a bug — expect this on future rebuilds too, don't assume a hang means it crashed.
**Deployed to `MP3 Generator\MP3 GENERATOR 3.7.exe`, overwriting the pre-migration build** — the
old one is still safe in `Backup Sebelum Migrasi No-Based 2026-07-23\MP3 Generator\` if a rollback
is ever needed. App title / version string was NOT bumped (still "v3.7 ZIP SAFE") since the user
didn't ask for a version change, just a rebuild reflecting the code changes.

**GUI restructuring (2026-07-25 decision):** user asked about splitting "MP3 per sheet" / "MP3
per cell" into separate GUI tabs (`ttk.Notebook`). Declined for now — the Tkinter app is a single
flat window (no Notebook anywhere), mode is currently just a Radiobutton that enables/disables
shared controls, and there's no way to visually verify a Tkinter layout change in this
environment (unlike the HTML Player, which can be tested in-browser). Revisit only if the user
raises it again, and prefer a lighter-touch option (labeled frames grouping mode-specific
controls) over a full Notebook restructure.

---

**This is the foundation for future MP3 Generator modifications and HTML Player integration.**
