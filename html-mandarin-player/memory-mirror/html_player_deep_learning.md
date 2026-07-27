---
name: html_player_architecture
description: "Deep learning notes on HTML Player architecture, design decisions, and key code patterns for future modifications"
metadata: 
  node_type: memory
  type: project
  originSessionId: d38ba609-545e-4921-addc-02aedf6f4cee
---

# HTML Mandarin Player — Architecture & Design Deep Dive

**Level:** Advanced Technical Reference  
**Version:** v25_11_100 (baseline; this doc still has some v25_11_87-era sections not yet
fully refreshed — cross-check against [[html_player_v25_11_100_final]] for the locked baseline
and [[mp3_no_based_naming_migration_plan]] for the most recent MP3-matching changes)  
**Last Updated:** 2026-07-25  

---

## 🏗️ Core Architecture

### **Dual-Column System (Decision #1) — ⚠️ REVERTED 2026-07-25, see [[mp3_no_based_naming_migration_plan]]**

**Correction (2026-07-25):** this decision has been reverted. `getRowIndexFromTr()` now reads
"No" (cells[0]) again, not "Ref." (cells[1]) — "Ref." was only ever a stopgap added because MP3
Generator's old code couldn't parse letters in "No", and MP3 Generator was revised 2026-07-23 to
read "No" directly. "Ref." is now free for the user to repurpose for something unrelated to MP3
matching. Keeping the original decision text below for history — it explains why the split
existed in the first place, which is still useful context.

**Problem:** Need 2 different numbering systems
- **No column** = User-facing (8, 8a, 8b, 8c) for navigation
- **Ref column** = Backend (1, 2, 3, 4) for MP3 filenames

**Solution:** Keep both columns
- Minimal code changes
- Ref already existed (renamed from Note1)
- User already familiar with system

**Code Pattern:**
```javascript
const cells = tr.querySelectorAll('td.cn');
const refNum = parseInt(cells[1]?.textContent || '0');  // Ref column (for MP3)
const noNum = cells[0]?.textContent.trim();              // No column (for UI)

// MP3 lookup uses Ref
const mp3name = `${prefix}_r${refNum}_mandarin.mp3`;

// Navigation uses No
// User sees "8c" but MP3 is "004"
```

**Why Not Change?**
- Touching `getRowIndexFromTr()` affects 15+ functions:
  - playModeSequence, setPlayingRowHighlight, canGetMp3
  - Download CSV, Admin panel, Filtering logic
- Breaking change risk high
- Current system works well, future-proof for migration

---

### **Baca No (Row Announcement) - Decision #2**

**Pattern:**
```javascript
function getRowNumberGroup(rowNo) {
  const match = String(rowNo).match(/^(\d+)/);
  return match ? match[1] : null;
}
// "8c" → "8", "9a" → "9", "10" → "10"

// Skip-group logic: only announce when group changes
let lastAnnouncedGroup = null;
if (lastAnnouncedGroup !== currentGroup) {
  speakText(`Kalimat ${currentGroup}`);
  lastAnnouncedGroup = currentGroup;
}
```

**Why Read No (Not Ref)?**
- User primary question: "Di mana saya sekarang?" (position)
- Ref (1, 2, 3) meaningless for navigation
- No (8, 8c) directly maps to worksheet row numbers

---

### **canPlayMode Filter - Decision #5**

**Critical for Background Playback:**
```javascript
function canPlayMode(tr) {
  if (audioMode === 'mp3') {
    // MP3 mode: skip rows without MP3 (no TTS fallback)
    for (let mode of MODES) {
      if (!canGetMp3(tr, mode)) return false;
    }
    return true;
  }
  // TTS mode: play everything
  return hasPlayableText(tr);
}

// Usage in playAllSequence:
const playableRows = rows.filter(tr => canPlayMode(tr));
```

**Why No Fallback TTS in MP3 Mode?**
- Chrome throttles TTS 1000ms+ when screen off (unreliable)
- If user picks MP3 mode, they want MP3 reliability
- Clear UX: "choose mode → get that mode's behavior"
- Trade-off: rows without MP3 are skipped (acceptable)

**Impact on Vivo V9 Improvement:**
- By skipping rows without MP3, reduced setTimeout calls
- Fewer setTimeout = less aggressive throttling by OS
- May explain why Vivo V9 "audio tidak mati total seperti dulu"

---

### **Global vs Per-Panel Architecture - Decision #6**

**Per-Panel (Local State):**
- Loop ON/OFF — each panel independent
- Random ON/OFF — each panel preference
- V1-V4 selection — each panel can mix differently
- Baca No — visible per-panel, syncs to global

**Global (Shared State):**
- Ak.Clip accumulator (3 separate: han, eng, all)
- Speed slider (affects all panels)
- Audio Mode (MP3 or TTS for all)
- Play All / Stop buttons

**Why This Split?**
- User workflow: open panel A → set preferences → switch to panel B → different settings
- Natural mental model: local = this panel's settings, global = affects everything
- Single speed slider simpler than duplicating per-panel

---

### **Ak.Clip Architecture - Decision #4**

**Three Separate Accumulators (Not One):**
```javascript
let hanAccum = [];  // Mandarin clipboard
let engAccum = [];  // English clipboard
let allAccum = [];  // All fields clipboard

// Each accumulator independent, can clear separately
// User can paste Han to app A, Eng to app B
```

**User Workflows Enabled:**
1. Copy Mandarin → app for flashcard
2. Copy English → app for reference
3. Copy all → spreadsheet for spreadsheet

**Why Not Single?**
- Single accumulator doesn't support multi-target workflow
- Would force choose: save Han OR Eng OR All, not all 3

---

## 📊 Key Functions & Patterns

### **MP3 Matching: mp3CandidateNames() — updated 2026-07-25, see [[mp3_no_based_naming_migration_plan]]**

Current actual implementation (`HTML_mandarin_v25_11_100.html:641-670`), not the old parseInt/
zero-padded version this doc previously showed:

```javascript
function getRowIndexFromTr(tr){
  // Raw "No" cell value as-is (e.g. "1a") — NOT parseInt()'d. JS parseInt("1a") silently
  // truncates to 1 (unlike Python's int(), which raises), which used to collapse every
  // letter-suffixed row in the same numeric group onto the same MP3 filename — found and fixed
  // 2026-07-23. Falls back to physical row position only when "No" is blank.
  const cells = tr?.querySelectorAll('td.cn');
  const noText = cells && cells[0] ? String(cells[0].textContent||'').trim() : '';
  if(noText) return noText.replace(/[<>:"/\\|?*]/g, '_');
  const table=tr?.closest('table');
  return String(qa('tbody tr', table).indexOf(tr)+1);
}
function mp3CandidateNames(table, tr, mode) {
  const key = modeToMp3Key(mode);
  const sheetPrefix = getSheetPrefixFromTable(table);
  const row = getRowIndexFromTr(tr);  // e.g. "1a" — no padding, no parseInt
  const aliases = { mandarin: [...], mandkw: [...], /* ...more aliases */ };
  const candidates = [];
  (aliases[key] || [key]).forEach(k => {
    candidates.push(`${sheetPrefix}_r${row}_${k}.mp3`);  // legacy "_r" variant, kept for old files
    candidates.push(`${sheetPrefix}_${row}_${k}.mp3`);   // matches MP3 Generator's current output exactly
  });
  return [...new Set(candidates)];
}
```

**Pattern:** Try multiple filename conventions, use first that exists. The plain (non-`_r`)
variant is what MP3 Generator's `library_filename()` produces since 2026-07-23 — the two tools
are meant to agree on that exact string.

---

### **Playback Flow: playModeSequence()**

**Flow:**
1. Get filtered rows via `canPlayMode()` ← Critical for screen-off
2. For each row: play V1-V4 modes based on checkbox selection
3. Between rows: delay(s) from preset config
4. Handle Baca No announcements (skip if group same)
5. Update playing highlight
6. Handle global speed multiplier

**Screen-Off Throttling Workaround:**
- Skip rows without playable content → fewer setTimeout calls
- Chrome throttles setTimeout to 1000ms+ when screen off
- By reducing setTimeout count, delay is less noticeable

---

## 🧩 Alt Mode / Pre-Combine Pipeline (added after v25_11_87, current as of 2026-07-22 patch)

Not present when this doc was first written (v25_11_87) — Alt mode/Pre-Combine shipped in
v25_11_100 (see [[html_player_v25_11_100_final]] for the full feature and its 2026-07-22 patch).
Documented here because the deep-learning doc is the "read first" reference and previously had
zero coverage of what is now a core playback path.

**Pipeline (Pre-Comb button click → ready-to-play):**
```
1. Extract: for each visible+checked row × selected V1-V4 mode → read/inflate MP3 from ZIP
   (sequential loop, yields every 15 rows so status message actually paints)
2. Decode: MP3 blobs → PCM AudioBuffers, in batches of 8 concurrent decodeAudioData() calls
   (not all-at-once — risks CPU/memory contention on weak phones; not fully sequential either)
3. Render: OfflineAudioContext(1 channel, 24000Hz) assembles all buffers on one timeline
   → audioBufferToWav() → single WAV Blob (combine NEVER just concatenates the source MP3s,
   it always fully decodes to PCM and re-encodes as WAV)
4. Cache: combinedBlobCache + combineSignature(rows+modes+delay) stored
5. Play: playAllCombineMode() plays the ONE WAV blob — audio.onended fires once, screen-off safe
```

**Why mono/24kHz, not stereo/browser-default:** source MP3s are edge-tts, confirmed mono 24kHz
(`MP3 Generator\...\wt_mandarin_mp3_generator_gui.py:509`, `anullsrc=r=24000:cl=mono`). Rendering
at the browser's default AudioContext rate (44.1/48kHz stereo) was pure waste — no quality gain,
~3-4x larger output, slower render. This does NOT speed up steps 1-2 (extraction/decode), which
dominate wall-clock time for large sheets (430+ rows) — only step 3.

**Cache validity:** `combineSignature()` = rows + modes + delay, checked at *play* time
(`playAllCombineMode`), not wiped reactively when Audio Mode changes. Switching Alt→MP3→Alt with
nothing else touched keeps the cache; changing V1-V4 selection or delay while cached correctly
invalidates it.

---

## ▶️ YouTube Link Button (added 2026-07-25)

**Source convention:** the original Text File CSVs sometimes carry a YouTube URL as the first
cell of a line *before* the header row (e.g. `https://www.youtube.com/watch?v=XD80CAchuFA;;;;;;;;;;;`
— see `Text File\008 Text.csv`/`009 Text.csv`/`010 Text.csv` for real examples). Not every sheet
has one.

**Parsing:** `parseDelimitedText()` (~line 1751) scans the lines before the detected header row
for a cell matching `^https?:\/\/(www\.)?(youtube\.com|youtu\.be)\/`, and attaches it as
`rows.youtubeUrl` (a non-array property tacked onto the returned array — kept the return type
array-shaped for back-compat with the exposed `window.parseDelimitedText`). `handleTextUpload()`
captures this into a local var *before* any `.filter()` reassigns `rows` (filter drops custom
properties), then passes it through to `addOrReplaceTextTab(title, rows, youtubeUrl)`, which
stores it as `panel.dataset.youtubeUrl` (a real DOM attribute — survives being saved into a new
standalone HTML via the existing "Download HTML Baru" feature).

**Button:** rendered by `dropdownPlayControlsHTML(tid, youtubeUrl)`, positioned right after the V4
dropdown and before the Loop checkbox (per user's explicit placement request). Class `.btn-ytube`
(red `var(--red)` background, white text). **Always rendered, even with no link** — user's explicit
choice: blank-looking button (not clickable) rather than hiding it, so the toolbar layout doesn't
shift between sheets. Click handled via the existing delegated-click pattern (`data-ytube-open`
attribute added to the same selector list as `data-final-pause` etc., ~line 2438) →
`window.open(url, '_blank', 'noopener')`.

**Fixed 2026-07-25 (same-day follow-up):** the "Ytube" text label is now ALWAYS rendered in the
button (never an empty string) — the first version set `textContent=''` when there was no link,
which made the button visibly shrink (no content = just padding). Now the text stays, and when
there's no link the button gets an extra class `.btn-ytube-empty` that sets `color:var(--red)`
(same as the background) — text is present in the DOM (button keeps full width) but invisible.
`cursor:default` + a neutralized `:hover` on that class too, since it's non-interactive.

**CSV export — standardized 2026-07-25 to always match the original source-file row layout,**
for BOTH single-tab and merge download (user's explicit request, revising the initial
"single-tab only" version): row1=URL (or literal `xxx` placeholder if no link), row2=blank,
row3=header, row4+=data — always, regardless of whether a link exists. Helper
`topUrlLine(youtubeUrl, numCols)` builds row 1 (`numCols` must match that export's header width —
12 for single-tab, 13 for merge which adds "Sumber File").
- `downloadActiveTabCSV()`: `[topUrlLine(panel.dataset.youtubeUrl, 12), '', panelToCSV(...)].join('\n')`
- `downloadMergeCSV()`: same shape, but row 1 is ALWAYS `xxx` — a merge combines multiple sheets
  (each with its own URL or none), so there's no single link that could go on row 1. Data across
  all merged sheets still starts at row 4, exactly like a single-sheet export.

**Verified live in-browser 2026-07-25:** uploaded one CSV with a YouTube link line and one
without, via `handleTextUpload()` (had to click through the real "Upload Semua Baris" modal, which
always blocks — confirmed it's not skippable). Confirmed: button shows "Ytube" + correct
`data-ytube-url` for the linked sheet, shows blank + doesn't call `window.open` for the unlinked
sheet, background color resolves to `rgb(192, 57, 43)` (`--red`), and `downloadActiveTabCSV()`
produces a CSV whose first line is exactly the YouTube URL + 11 empty fields, matching the
original file convention. Re-verified after the same-day button-shrink fix using the actual
`Text File\001 Text.csv` (real file, real link with query params `&list=...&index=2`) — button
width identical with/without a link (~59px both), and the downloaded CSV's first line is the full
URL intact. Re-verified again after standardizing the row1/row2/row3/row4 layout: captured all
three download paths in one pass (linked single-tab, unlinked single-tab, merge) and confirmed
each one's first 4 lines match the required shape exactly, including `xxx` showing up correctly
for both the no-link single sheet and the merge (which always uses `xxx`).

**Important distinction (surfaced by a user report that turned out not to be a bug):** only the
plain numbered "Text" files (`001-010 Text.csv` etc.) carry this top-left YouTube link convention.
The "Breakdown" files (`Text File\Breakdown\*.csv`, e.g. `011 Break.csv`) do NOT — they aggregate
keywords pulled from MULTIPLE different source texts (see their `Note2` column referencing
different source numbers like `001_10`, `009_02`), so there's no single YouTube video to
attribute to the whole sheet. A missing link/button-text on a Breakdown-type sheet is correct
behavior, not a bug — confirmed with the user 2026-07-25 after checking which file matched a
screenshot they sent.

---

## 🔌 Integration Points with MP3 Generator

**Naming (current, since 2026-07-25 — see [[mp3_no_based_naming_migration_plan]] for full history):**
- Generator creates: `010_1a_mandarin.mp3`, `010_1b_mandarin.mp3`
- HTML Player looks for: `${prefix}_1a_mandarin.mp3` (built from the row's "No" cell)
- Match via: the CSV's "No" column value, identical string on both sides — not row position, and
  not a separate "Ref." column anymore (that briefly existed 2026-07-23 to 2026-07-25 as a
  stopgap, see the migration plan file for why).

**Why this instead of row-position-based naming?**
- Row-position-based naming was fragile: inserting/reordering rows shifted every filename after
  the insertion point.
- Keying off "No" (which the user assigns per row and can include letter suffixes like `1a`,
  `1b`) is stable across reordering, and was always the intended long-term design — verified
  working end-to-end 2026-07-23/25 with real generated MP3s played back in the browser.

---

## ⚠️ Known Limitations & Workarounds

| Issue | Cause | Workaround | Status |
|-------|-------|-----------|--------|
| Screen-off delay (pre-v25_11_100) | Chrome throttles setTimeout/setInterval — and even `audio.onended`/`ontimeupdate` — when the page is backgrounded | ✅ **SHIPPED (v25_11_100, Alt mode):** combine every row into ONE audio file so zero mid-sequence JS callback is ever needed — see [[html_player_v25_11_100_final]] | ✅ RESOLVED |
| Play Row stop button | Event handling race condition | Use toolbar stop button | ✅ KNOWN |
| TTS unreliable screen off | Chrome throttles | Switch to MP3 mode | ✅ DOCUMENTED |
| Lock screen widget missing | Browser/OS limitation | MediaSession registered anyway | ✅ KNOWN |
| `requestAnimationFrame` as a yield/delay point | Can stop firing entirely when the page isn't actively compositing (backgrounded, plausibly screen-off) | Use `setTimeout(fn, 0)` for ANY "yield to let the browser paint" point, never rAF | ✅ FIXED 2026-07-22 (was introduced and caught same session, see [[html_player_v25_11_100_final]]) |
| Long button handler with no busy-state | Re-clicking a frozen-looking button starts a second concurrent run of the same async work (no cancellation exists for it) | Disable the triggering button + a re-entrancy flag for the whole duration of any multi-second async button handler | ✅ FIXED 2026-07-22 (Pre-Comb button) |

**Screen-off investigation history (2026-07-12 to 07-14, condensed):** MP3 Generator playing MP3s
successfully screen-off (via Android's native player, not Chrome) first proved the *devices* could
do it — the real culprit turned out to be Chrome throttling **all** JS callbacks once backgrounded,
not just `setTimeout`: `setInterval` and even `audio.onended`/`ontimeupdate` were tested and also
failed to fire. An event-driven per-row rewrite (swap `setTimeout` for `audio.onended`) was the
first plan, but testing showed it wouldn't have worked — no JS callback of any kind survives
backgrounding, only audio *playback itself* continues. Several other approaches were tried and
abandoned along the way (queued per-row playback, visibilitychange-triggered catch-up, per-row
combining with time-based highlight tracking). The only approach that actually worked: combine
every row into a single audio file so zero mid-sequence JS execution is needed at all — that's
what shipped as Alt/Pre-Combine mode in v25_11_100 (see [[html_player_v25_11_100_final]]), at the
cost of per-row highlights/announce/loop granularity (see table above). Full blow-by-blow of the
abandoned attempts archived in `Temp Claude/2026-07-27 Memory Cleanup - HTML Player, MP3 Gen, Anki Builder/html-player/` if ever needed again.

---

## 🎯 Future Improvements (From Technical Debt)

**HIGH Priority:**
1. MediaSession lock screen widget (may not be achievable on all devices)
2. ~~Implement 1a, 1b, 2a, 2b MP3 naming strategy~~ — ✅ DONE 2026-07-25, see [[mp3_no_based_naming_migration_plan]]

**MEDIUM Priority:**
1. Group-aware V1-V2 playback (V2 plays last row per group)
2. Auto-generate missing sentences from keywords
3. Debounce filter (DONE in v25_11_87 with 1s delay)

**LOW Priority:**
1. Consolidate scattered state into single state object
2. Refactor playModeSequence into separate functions per mode
3. Virtual scrolling for 500+ rows

---

## 💡 Modification Guidelines

**Before Modifying:**
1. MP3 matching now keys off "No" alone (not a dual No/Ref split — that was reverted 2026-07-25,
   see [[mp3_no_based_naming_migration_plan]]). "Ref." column may contain anything; don't assume
   it's still involved in MP3 lookup.
2. Respect the per-panel vs global architecture split
3. Remember: screen-off playback is primary use case for MP3 mode
4. canPlayMode filter is critical for Vivo V9 & similar devices

**Safe Modifications:**
- Add new buttons/controls (use global or per-panel as appropriate)
- Adjust delays in presets
- Add audio modes (keep current MP3 + TTS logic)
- Improve UI without changing playback logic

**Risky Modifications:**
- Changing `getRowIndexFromTr()` → only 4 call sites as of the live v25_11_100 file (verified
  2026-07-23, not the "15+ functions" this doc used to claim for an older version), but still the
  single point both HTML Player and MP3 Generator must agree on — any change here needs a
  matching change in MP3 Generator's `read_rows_numbered()`/`library_filename()`, see
  [[mp3_no_based_naming_migration_plan]]
- Removing canPlayMode filter → breaks screen-off playback
- Changing MP3 naming → needs Generator + HTML Player sync (now both keyed on "No" — done
  2026-07-25)
- ~~Consolidating No vs Ref columns~~ — done 2026-07-25, "Ref." no longer read for MP3 matching
- Using `requestAnimationFrame` anywhere for timing/yielding → can hang indefinitely under the
  same backgrounded/screen-off conditions this whole app is built to survive. Use `setTimeout`.
- Adding a long-running async button handler without a busy/disabled state + re-entrancy guard →
  a second click silently starts a duplicate concurrent run (this bit the Pre-Comb button, fixed
  2026-07-22 — see [[html_player_v25_11_100_final]])

---

**This is the brain dump from v25_11_85 → v25_11_87. Reference for all future modifications.**
