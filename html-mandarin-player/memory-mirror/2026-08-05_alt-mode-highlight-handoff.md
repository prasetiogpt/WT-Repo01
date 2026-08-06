# Handoff: Alt/Combine mode — live row highlight + related fixes

**Written:** 2026-08-05, from a Claude Code Cloud (remote) session, for continuation in a local
Claude Code session (per user's decision — this work needs real-device audio/screen-lock testing,
which the remote sandbox can't do; local can iterate fast by copying straight to the Drive test
path instead of push→pull→download each time).

**Status: pure design discussion, ZERO code written for anything in this doc.** Everything below
was talked through and agreed with the user in the cloud session, but no implementation started.
Do not re-litigate the reasoning below unless new evidence contradicts it — it was already worked
through carefully. Do implement it fresh, reading current line numbers (they will drift).

## The problem the user is solving

In Alt/Pre-Combine mode, all selected rows' audio get merged into one WAV file before playback
starts, specifically so **zero JS needs to run between rows** while the phone screen is off
(Chrome throttles setTimeout/setInterval/onended etc. when backgrounded — this is the whole reason
Alt mode exists, see Rule 3 in the `html-mandarin-player` skill). The cost of that design: while
combined audio plays, there is no per-row highlight like MP3/TTS mode has. If the user turns the
screen back on mid-playback, they have no way to tell which sentence is currently being read
without manually searching — that's the pain point driving this work.

## Agreed solution (3 parts, meant to be built together since they share the same underlying data)

### Part 1 — Record per-row time offsets when building the combined blob

`combineAudioBlobs()` (search for this name; was ~line 897-943 as of this writing) already computes
a running `offset` per audio source while placing it into the `OfflineAudioContext` (was ~line
929-936) — it just doesn't currently save that number anywhere, it only returns the final rendered
WAV blob.

The outer pre-combine build loop (search `isCombining`/`combinedBlobCache =`; was ~line 2560-2620)
iterates `rows = rowCycle(tbl, modes)` and for each row pushes possibly multiple blobs (one per
mode) into a flat `audioBlobs` array. To get **row-level** offsets (not blob-level), that loop needs
to record, per row, the index into `audioBlobs` where that row's block starts. After
`combineAudioBlobs` returns per-blob offsets, map `rowStartBlobIndex[i]` → time-in-seconds to get a
`rowOffsets` array (row index → start time within the combined WAV).

Confirmed with the user: this adds negligible time — a few array pushes vs. the actual cost centers
(per-file `decodeAudioData`, `OfflineAudioContext` rendering), which dominate render time already
and are unaffected by this change.

### Part 2 — Live highlight while screen is ON, fully silent while screen is OFF

- A lightweight `setInterval` (~300-500ms) runs **only** while `document.visibilityState==='visible'`
  AND Alt-mode combine audio is actively playing. Each tick: read the combine `<audio>` element's
  `currentTime`, find the matching row via `rowOffsets` (linear scan is fine, row counts are small),
  call the existing `setPlayingRowHighlight(tr)` (was ~line 1282) and scroll it into view.
- On `visibilitychange` → `'hidden'`: `clearInterval` immediately. This is the load-bearing
  invariant — **zero JS runs while the screen is off**, so Rule 3 / screen-off reliability is fully
  preserved. Audio playback itself is native (`<audio>` element), completely independent of this
  timer, so it's never at risk regardless of what the timer does.
- On `visibilitychange` → `'visible'`: restart the interval; first tick immediately resyncs the
  highlight to wherever playback actually is (jumps straight to the right row, no searching).

Confirmed with the user: this can't cause Play All stutter. The interval's work (read currentTime,
scan a small array, toggle a class, scroll) is far below anything that competes with native audio
playback for resources; worst case is the highlight lagging by a fraction of a second, audio itself
never glitches. This is a different code path from the audio pipeline entirely.

**Do not implement this with `requestAnimationFrame`** — Rule 1 in the skill bans rAF for anything
load-bearing since it silently stops firing when backgrounded. Here that's arguably a *feature*
(auto-stops when hidden) but it's not deterministic/controllable the way `setInterval` +
`visibilitychange` is, so use the explicit interval approach for predictability, not rAF.

### Part 3 — Reuse rowOffsets for "continue from next row" in Alt Play All

Separate but related ask from earlier in the conversation: in MP3/TTS mode, if you manually play a
single row (▶ button) then hit Play All, it continues from the *next* row instead of restarting
(`getStartIndex()`, was ~line 1358-1363, using the module-level `lastPlayedTr` set in
`playRowSequence()` at ~line 1585). `playAllCombineMode()` (was ~line 1466-1490) currently has no
such logic — it always starts the combined blob from time 0, because until Part 1 exists there's no
way to know where "row N" begins inside the flat WAV.

Once `rowOffsets` exists (Part 1), `playAllCombineMode` can resolve `lastPlayedTr` to a row index,
look up its offset, and `audio.currentTime = rowOffsets[idx]` before calling `play()` — a one-time
seek before playback starts, not a mid-sequence callback, so this doesn't touch the screen-off
constraint either.

## Separate, smaller agreed change — per-row ▶ button MP3/TTS fallback behavior

Not related to highlighting, but discussed in the same conversation and agreed:

- **Mode MP3, manual per-row ▶ click** (`playRowSequence()` → `speakMode()`/`canPlayMode()`, was
  ~line 1024-1046): currently if no MP3 file matches, the row silently does nothing (no fallback —
  this is Rule 6 in the skill, "MP3 mode never falls back to TTS"). Agreed: **add a TTS fallback
  specifically for the manual per-row button**, since Rule 6's reasoning (Chrome throttles TTS after
  screen-off) doesn't apply to a manual click — the screen is necessarily on when the user taps a
  button. **Play All in MP3 mode must keep skipping with no fallback, unchanged** — Rule 6 stays
  fully intact for the automated sequence. This is a scope-narrowing of Rule 6, not a reversal of
  it — update the skill's Rule 6 wording to say explicitly "applies to the automated Play All
  sequence; the manual per-row button may fall back to TTS."
- **Mode Alt/Combine, manual per-row ▶ click**: currently always uses TTS (because
  `canPlayMode`/`speakMode` only branch to MP3 lookup when `getAudioMode()==='mp3'`, combine falls
  through to TTS same as plain TTS mode). Agreed: extend that condition to also try MP3 lookup
  (`findMp3For`, was ~line 684) when mode is `'combine'`, sourcing from the same MP3
  folder/zip already loaded for MP3 mode — **not** from `combinedBlobCache` (that's one flat file,
  can't be sliced to a single row without Part 1's offsets, and even with them, playing a slice of
  a WAV read as a Blob is unnecessary complexity when the original per-row MP3 file is right there).
  If no MP3 found for that row, fall back to TTS (same reasoning as MP3 mode above — manual click,
  screen is on, Rule 6's throttling concern doesn't apply).
- **Play All in Alt mode is unaffected by this — unchanged, still plays `combinedBlobCache` as one
  file from the (possibly seeked, per Part 3) offset.**

## Already-confirmed, do-not-re-derive facts from this discussion

- `playableRows()`/`rowCycle()` (was ~1251-1368) already filters to `!hidden && isRowChecked` before
  modes-filtering — Pre-Combine already only combines rows that are both visibly filtered-in AND
  checked (Pilih=X). This was a separate question the user asked and it's already correct, no
  change needed there.
- `combineSignature()` (was ~1462-1464) hashes rows+modes+delay, so changing the visible filter
  after a combine was built correctly invalidates the cached combine (forces rebuild) rather than
  silently playing a stale/mismatched combine.

## Unrelated but done in the same session — already shipped, don't redo

Separate task, already committed and pushed to branch `claude/html-player-mp3-generator-pi3eoa`
(commit `7201d5c`): rows with no digit in the "No" column, or with every other data column empty,
are now silently skipped in both TXT/CSV upload (`parseDelimitedText`) and CSV download
(`panelToCSV`) in `HTML_mandarin_player.html`. This did not touch the MP3 Generator Python code —
that was explicitly out of scope per the user (MP3 Generator's default "rows" preset is `"all"`, not
`"checked"`, so old un-reprocessed source files could still have junk rows reach the generator —
flagged to the user as a known gap, but deferred, not part of this task).

## Two more items discussed after this note was first written (not yet in the numbered plan above)

### Download the combined WAV as a file

Not yet built at all — `combinedBlobCache` (was ~line 496, set ~line 2617) is already a proper
`Blob` with `type:'audio/wav'` (built by `audioBufferToWav()`, was ~line 945-982, returns
`new Blob([arrayBuffer], {type:'audio/wav'})`), so a download button is a small addition, same
pattern as the existing `downloadCSVFile()` (was ~line 2243) — create an `<a download>` with
`URL.createObjectURL(combinedBlobCache)`. Purely additive, doesn't touch playback/combine logic, no
interaction with Rule 3 (it's a manual one-shot click, not something running during screen-off
playback).

Discussed but undecided: WAV output is uncompressed (much larger than MP3 for the same audio). To
offer MP3 instead would require bundling an MP3 encoder (no browser-native MP3 encoding exists,
Web Audio only gives raw PCM) — e.g. `lamejs`, inlined to keep the single-file-HTML property. That
adds roughly 100-150KB (minified) to the source file (current size: ~221KB / 4315 lines, so this
would meaningfully grow it). User has not decided yet whether this is worth it — leave as WAV-only
unless they ask for MP3 encoding specifically.

### Pre-Combine build is slow for large sheets (several minutes for hundreds of rows)

User's real-world complaint: sheets with hundreds of checked+visible rows take multiple minutes to
Pre-Combine. Diagnosed three stages in the build handler (`preCombRefreshBtn` click listener, was
~line 2538-2627):

1. **Reading MP3s out of the zip** (was ~line 2574-2589): the `for(const tr of rows){ for(const
   mode of modes){ await readZipEntry(...) } }` loop is fully **sequential** — one file at a time,
   no batching. Actual decompression uses the browser-native `DecompressionStream` (was ~line
   823-825 `inflateZipRaw`), which is fast per-call, but doing hundreds of them one-by-one adds up.
2. **`decodeAudioData` batching** inside `combineAudioBlobs()` (was ~line 908-922): already batched
   at `BATCH_SIZE=8` concurrent, deliberately capped per an existing code comment ("bounded so
   weak/older phones don't get hit with 100s of decode jobs simultaneously"). This is likely the
   single biggest cost center — audio decode is CPU-heavy, and even at 8-way concurrency, hundreds
   of files means many sequential batches.
3. **`OfflineAudioContext` render** (was ~line 928-937): single render pass at the end, probably
   not the bottleneck (offline rendering is normally faster than real-time).

Three optimization ideas discussed, not yet prioritized/decided by the user — ask them before
picking:
- **(A) Cache decoded buffers per MP3 file within the session**, keyed by row+mode+filename (or
  the resolved zip entry), so re-running Pre-Combine after just tweaking the row filter/checkboxes
  doesn't re-decode files it already decoded earlier in the same session. Pure win, no tradeoff,
  but only helps repeat/re-combine, not a first-time build.
- **(B) Parallelize the zip-read stage** (item 1 above) with the same chunked-`Promise.all` pattern
  already used for decoding, instead of one-file-at-a-time. Low risk since each `readZipEntry` call
  is already lightweight.
- **(C) Make `BATCH_SIZE` for `decodeAudioData` adaptive** based on `navigator.hardwareConcurrency`
  — bigger batches on capable devices, keep the safe default (8) on weak/old ones. Likely the
  biggest potential win, but **needs real-device testing** (exactly the kind of testing that's the
  whole reason this work moved to a local session) since going too aggressive could make Pre-Combine
  janky/crash on older phones — the opposite of the reliability this whole feature exists for.

Recommended order if the user wants to tackle this: B + C together give the most speedup for a
*first-time* combine (not just repeats); A is a smaller, safer add for the repeat-combine case.
Confirm with the user which of A/B/C (or all three) they actually want before starting — this was
raised as a diagnosis, not yet greenlit as a task.

## Suggested build order for the local session

1. Part 1 (row offsets) — foundation for both highlight and continue-from-next-row.
2. Part 2 (live highlight) — the user's actual stated pain point, do this right after Part 1.
3. Part 3 (continue-from-next-row) — cheap once Part 1 exists, lower priority than Part 2.
4. Per-row ▶ MP3/TTS fallback — independent of 1-3, can be done anytime, simplest change of the four.

After implementing, update the `html-mandarin-player` skill (Rule 6 wording per above) and this
app's primary memory doc at `I:\My Drive\WS Fam\Memory\html-player\` (not just this mirror) once
Drive is reachable from the local session — per the skill's normal recovery procedure, reconcile
this mirror note into the primary doc rather than leaving it stranded here.
