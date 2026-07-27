---
name: html_player_v25_11_100_final
description: "v25_11_100 - Alt mode with Pre-Combine, screen-off support; received a combine performance/reliability patch 2026-07-22"
metadata:
  type: project
  status: PATCHED
  version: 25.11.100
  lastPatched: 2026-07-22
---

# HTML Mandarin MP3 Player - v25_11_100 (baseline locked 2026-07-14, patched 2026-07-22)

**Status:** 🔒 Baseline feature-locked (2026-07-14); bug fixes/perf patches applied on top, see [[html_player_combine_patch_2026_07_22]] below
**File:** `I:\My Drive\WS Fam\HTML+MP3 Player\HTML Versions\HTML_mandarin_v25_11_100.html` (same filename — edited in place, not a new version file; folder renamed `versions\` → `HTML Versions\` on 2026-07-16, see [[workspace_paths]])
**Approved By:** User (2026-07-14, baseline); combine patch approved incrementally across a 2026-07-22 session
**Lock scope:** No new *features* without re-evaluating screen-off trade-offs. Bug fixes to existing features (like the combine patch below) are in scope and expected — "locked" means feature-frozen, not bug-frozen.

---

## Features Implemented ✅

### 1. Alt Mode (Pre-Combine)
- **Combine button:** Separate combining step from playback
- **Intelligent caching:** Hash-based detection, re-combine only when selection/modes/delay actually changes — **note:** the hash (`lastCombineRowsHash`) was written on every combine but never actually *compared* anywhere until the 2026-07-22 patch, so this bullet describes the *intended* design, not what shipped on 2026-07-14. See [[html_player_combine_patch_2026_07_22]] for the real fix.
- **Cache persists across Audio Mode switches** (Alt → MP3 → Alt etc., since 2026-07-22) — validity is checked via `combineSignature()` at play time, not wiped reactively on mode change
- **Fast playback:** Play from cache is instant (<1s after initial combine)

### 2. Screen-Off Support ✅
- **Solution:** Combine all MP3s into 1 audio file
- **Why:** Eliminates callback chain - audio.onended only fires when audio ends (continues in background)
- **No JS callbacks saat screen off** = playback continues indefinitely
- **Trade-off:** Row highlights, loop logic, speed changes fixed to combined file

### 3. Status Message Repositioning ✅
- **Location:** Global toolbar, sebelah Download button
- **Styling:** 
  - Font size: .85rem (lebih besar dari original .78rem)
  - Color: var(--green)
  - Weight: 500 (bold)
  - Spacing: margin-left 12px
- **Why:** Global location ensures `setUploadMsg()` can find & update reliably
- **Visibility:** Always visible in upload toolbar area, not per-table

### 4. Known Limitations (By Design)

#### Announce Numbers (Baca No)
- **Status:** DISABLED in Alt mode
- **Reason:** Per-row announce requires callbacks → breaks screen-off solution
- **Option:** Works in MP3 mode (non-Alt) with original row-by-row playback
- **Current:** All-nomor-at-once in Alt mode (not per-row)

#### Loop Playback
- **Status:** Functional but simplified
- **Behavior:** Loop checkbox controls restart of combined audio
- **Note:** No per-row loop logic (all in 1 combined file)

#### Speed Control
- **Status:** Fixed to selected speed at combine time
- **Change:** Requires re-combine with new speed setting

---

## Architecture Summary

```
playAllCombineMode(tid, modes, btn, token)
  ├─ Check combineReadyFlag + cache
  ├─ Get rows from selection
  └─ doCombinePlay() [recursive]
      ├─ announceAllRowNumbers() [skipped in final]
      ├─ playAudioBlob(combinedBlobCache)
      │  └─ audio.onended → check isLoopOn()
      │     ├─ false → finishPlay()
      │     └─ true → doCombinePlay() [restart]
```

---

## Key Global Variables

```javascript
let combinedBlobCache = null;        // Cached combined audio
let lastCombineRowsHash = null;      // combineSignature() of the rows/modes/delay it was built from (since 2026-07-22; before that, an unused hash)
let combineReadyFlag = false;        // Ready-to-play flag
let playToken = 0;                   // Token for concurrent request prevention
let isCombining = false;             // (since 2026-07-22) re-entrancy guard, see patch notes
```

---

## CSS Changes

### New: `#statusMessageBar`
```css
#statusMessageBar {
  background: #fef3e2;
  border: 1px solid var(--border);
  padding: 10px 12px;
  text-align: center;
  display: none;  /* hidden by default */
}
#statusMessageBar.active {
  display: block;  /* shown when setUploadMsg() called with text */
}
```

---

## What NOT to Change (Screen-Off Safe Zone)

❌ **DO NOT add per-row callbacks** in Alt mode:
- `announceRowNumber()` per-row
- Individual MP3 playback per-row
- Per-row loop tracking
- Per-row highlight updates

All above would re-introduce callback chain → break screen-off support.

---

## Testing Checklist

✅ Alt mode + Combine button works
✅ Cache resets on selection change
✅ Play from cache is fast
✅ Loop checkbox toggles restart
✅ Status message appears/disappears (repositioned)
✅ No regressions in MP3/TTS modes

---

## Amendment 2026-07-22: Combine Performance & Reliability Patch {#html_player_combine_patch_2026_07_22}

User reported real-world pain with Pre-Comb on a sheet with **430 rows**: combine felt slow
(worse on older phones), the status message looked frozen, a second click while "frozen"
silently doubled the work, and the cache was lost every time Audio Mode was toggled away from
Alt and back. All of it was investigated and fixed in the same file (no new version number —
edited `HTML_mandarin_v25_11_100.html` in place). Every change below was verified in-browser
(console + direct function calls), not just read/reasoned about — see conversation for exact
test snippets if reproducing.

### 1. Combine output: mono 24kHz instead of stereo/browser-default-rate
`combineAudioBlobs()` (`audioBufferToWav()` builds a **WAV**, not MP3 — combine always decodes
every source MP3 to PCM and re-encodes as WAV; it never just concatenates the compressed files).
It was rendering as **stereo** at the **browser's default AudioContext sample rate** (44.1/48kHz)
regardless of source. The actual source (edge-tts, confirmed in
`MP3 Generator\...\wt_mandarin_mp3_generator_gui.py:509`, `anullsrc=r=24000:cl=mono`) is **mono
24kHz** — so every combine was paying for ~3-4x more audio data than the content contained.
Fixed: `OfflineAudioContext(1, ...)` (mono) at a fixed `TARGET_SAMPLE_RATE = 24000` (with a
try/catch fallback to the browser default if the browser rejects that constructor rate). Verified
by reading back the WAV header (`numChannels`, `sampleRate` fields) after combine.
**This mainly shrinks file size and speeds up the *render* step — it does NOT speed up ZIP
extraction or MP3 decode**, which for hundreds of rows are the actual bottleneck (see #2).

### 2. Decode: bounded-concurrency batches, not sequential and not all-at-once
Original: decode MP3s one at a time. First attempted fix: `Promise.all()` all N files at once —
**rejected after more thought**, because firing e.g. 430 concurrent `decodeAudioData()` calls
risks CPU/memory contention on exactly the older/weaker phones the user was complaining about
(could make things worse, not better). Landed on: `BATCH_SIZE = 8` — decode 8 concurrently, wait,
next 8, etc. Gets some parallelism without saturating weak devices. Progress callback fires
**per-file** (not per-batch) so the counter feels smooth even though decode happens in chunks of 8.

### 3. UI freeze during extraction/decode — was a real bug, not just perception
`setUploadMsg('⏳ Pre-Combining audio...')` was called before the ~430-iteration extraction loop,
but the message never got painted to screen before the loop finished, because the loop's
`await readZipEntry(...)` chain resolved fast enough, back-to-back, that the browser's rendering
step never got a slot — a classic "long microtask chain starves paint" issue. User correctly
identified this as "seolah belum terpencet", not a misperception.
**Fix:** added `nextPaint()` — `await`ed right after `setUploadMsg()` and periodically inside the
extraction loop (every 15 rows) and inside the decode batch loop (every batch) — plus live
progress text (`Membaca MP3... X/Y baris`, `Decoding X/Y files...`).
**⚠️ Important implementation detail:** `nextPaint()` was first written using double
`requestAnimationFrame`. **This is wrong for this codebase and was caught by testing, not
review** — `requestAnimationFrame` can stop firing entirely when the page isn't actively
compositing (backgrounded tab; plausibly also screen-off, given this whole app's screen-off
architecture is built around exactly that kind of rendering-pipeline pause). Using it as a yield
point risked hanging the *entire combine step* forever under the same conditions the app is
designed to survive. **Fixed to `setTimeout(r, 0)`** instead, which still yields but doesn't
depend on active compositing. **Lesson for any future work in this file: never use
`requestAnimationFrame` for a yield/delay point — always `setTimeout`.** This app's whole reason
for existing (background/screen-off playback) makes rAF-based timing a landmine.
A separate small "render in progress" spinner (`>`, `>>`, `>>>` cycling every 400ms via
`setInterval`, cleared in a `finally`) covers the one phase that has no numeric progress at all:
`OfflineAudioContext.startRendering()` is a single atomic promise with no progress events.

### 4. Pre-Comb button had no re-entrancy guard — root cause of "combine batal, harus diulang"
The actual async combine computation was **never** cancelled by clicking other buttons (Play/Stop
don't touch `combineAudioBlobs`'s local state). What actually happened: the Pre-Comb button itself
had no disabled/busy state, so a second click (the natural reaction to a UI that looks frozen)
started a **second, fully independent combine run** concurrently — both writing to the same
`setUploadMsg()` and the same cache variables, which visually looked like a restart and wasted
double the CPU/memory. **Fix:** `isCombining` guard flag + `btn.disabled = true` for the whole
run, reset in a `finally` block so it can't get stuck disabled on an error path. Verified: firing
`.click()` twice back-to-back now only runs the process once.

### 5. Cache wiped on every Audio Mode change, even switching back to the same state
`audioModeSelect`'s `change` handler unconditionally nulled `combinedBlobCache` /
`combineReadyFlag` / `lastCombineRowsHash` on *every* change — including MP3 → Alt with nothing
else touched, forcing a needless re-combine. Root fix: stopped wiping on mode change (only toggles
the Pre-Comb button's visibility now); instead added `combineSignature(tbl, modes)` = row
selection hash + chosen V1-V4 modes + delay-between-rows, computed both when Pre-Comb succeeds and
compared again in `playAllCombineMode()` right before playback. Cache now survives mode-switching
and only actually invalidates when something that would change the resulting audio really changed.
Verified both directions: toggling Alt→MP3→Alt with no other change preserves the cache and plays
immediately; changing a V1-V4 dropdown while cached correctly forces "Click Pre-Comb dulu" again.

### 6. "Mode TTS aktif" message wrongly shown in Alt mode, then message wording refined twice more
A separate, older status-message handler (`audioMode.onchange = ...`, unrelated to the Pre-Comb
button's own logic) only branched on `mp3` vs "everything else", so selecting Alt fell into the
"else" branch and showed "Mode TTS aktif." — misleading, since Alt requires the very different
Pre-Comb workflow. First fix added a third branch that checked `combineSignature()` and said
either "...Klik Pre-Comb dulu sebelum Play All." or "...Audio combine masih tersimpan — langsung
Play All." — the cache-aware *logic* was right, but the user asked to simplify the wording twice
after seeing it in practice. **Current final text** (all four Audio Mode messages, same session):
- TTS → `Mode TTS`
- MP3 → `Mode MP3. Pilih MP3 ZIP yang sesuai nama sheet.`
- Alt, cache still valid → `Mode Alt. Audio Combine sudah ada.`
- Alt, cache not ready (both the mode-switch message AND `playAllCombineMode()`'s own message when
  Play All is pressed without a valid cache) → `Mode Alt. Audio Combine belum ada.`

The cache-validity *check* behind the Alt-mode branch is unchanged from the original fix
(`combineSignature()` compared against `lastCombineRowsHash`) — only the displayed text changed.

### 7. Save Clip (Ak.Clip) — sheet separator made more visible when scrolling fast
`saveAllToClip()`'s Ak.Clip-on path (`allAccum`, combined via `entries.map(...).join(...)`)
previously separated different sheets' saved text with a bare title and 1 blank line. Changed to:
- Sheet title wrapped: `002 Text` → `_ _ _          002 Text          _ _ _` (applies to every
  sheet, including the first)
- Separator between sheets: 1 blank line → 3 blank lines (`.join('\n\n')` → `.join('\n\n\n\n')`)
- Scope: only the *between-sheets* separator/title — the existing *within-sheet*
  blank-line-per-No-group logic (`lines.push('')` when the row number changes) is untouched

### What did NOT change (screen-off safety preserved throughout)
All fixes above operate *before* playback starts (extraction/decode/render), in UI chrome (button
state, messages), or in the unrelated Save Clip text-formatting feature. The actual playback
mechanism — one combined WAV blob, one `audio.onended` — is untouched throughout this whole
amendment. Verified after each change: build a combined blob, play it with `audio.onended`,
confirm it fires exactly once at the end.

---

## Final Notes

- **Feature-locked, not bug-frozen:** v25_11_100 is still the baseline — no new *features*
  without re-evaluating screen-off trade-offs — but real bugs (like the combine patch above) are
  fair game and should be fixed when found, tested in-browser, and logged here.
- **Memory consolidated** in v25_11_100_final.md (this file)
- **Next session:** read the Amendment section above before touching combine/Pre-Comb code again
  — several of the "obvious" quick fixes here (parallel decode, requestAnimationFrame) turned out
  to be wrong on first instinct and were only caught by actually testing in-browser.

