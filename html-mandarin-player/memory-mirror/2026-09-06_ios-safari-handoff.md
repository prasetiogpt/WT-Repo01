# Handoff: iOS Safari access + file-picker fixes (2026-09-06)

Written as a git-mirror fallback (this session had no local Drive mount). Not yet copied to
`I:\My Drive\WS Fam\Memory\html-player\` — do that once Drive is reachable again, per CLAUDE.md's
fallback-recovery rule.

## What triggered this session

User's iPhone couldn't:
1. Select a `.zip` (MP3s) from Google Drive inside the app's "⬆ MP3" picker.
2. Open `HTML_mandarin_player.html` itself in Safari at all — tapping the file (from Google Drive
   "Open with" or from local Files app) always launched **WPS Office** or **Koder** instead; Safari
   and Chrome never appear as options.

## Root causes found (code-verified + well-known iOS/WebKit behavior)

- **Zip/CSV picker greyout:** `accept=".zip,application/zip,..."` (and the same pattern on the
  CSV/TXT inputs) can make iOS's Files "Browse" sheet show Google-Drive-sourced files as
  grey/unselectable, because the MIME/UTI the Drive provider reports doesn't always match the
  `accept` list. Confirmed safe to loosen: `handleMp3ZipFiles()` already filters by `.zip` filename
  itself (doesn't trust `accept`), and `handleTextUpload`/`handleVocabUpload` don't validate
  extension at all.
- **Can't open the file at all in Safari:** this is normal iOS behavior, not a bug — Safari/Chrome
  are never listed in "Open With" for local files, only apps that register as document handlers
  (WPS, Koder, etc.). No accept-attribute or code fix can change this; the file has to be reached
  as a URL instead of a local file.

## What's fixed and pushed (not yet merged to `main`)

Branch: `claude/html-mandarin-player-iphone-xsosol`
- `193696e` — `#mp3ZipInput` accept loosened to `*/*`
- `d3febba` — `#txtUpload` / `#vocabUpload` accept loosened to `*/*`

**Not yet tested on a real iPhone.** Ask user to confirm the zip/CSV picker greyout is actually
gone before treating this as closed.

## Chosen fix for "open in Safari at all": GitHub Pages, on WT-Repo01 itself

Decision (confirmed with user): don't create a separate mirror repo — make `WT-Repo01` itself
public and serve it directly via GitHub Pages (`main` branch, `/` root). Rationale:
- I (this session) have no GitHub API access to create new repos or toggle
  visibility/Pages settings — access was scoped to `prasetiogpt/WT-Repo01` only, and repo creation
  was tried and got a 403. Those are strictly-manual, web-UI-only steps for the user.
- Repo-wide scan for personal data before agreeing to public: **no passport numbers, phone
  numbers, emails, credentials, or large personal media found.** One flagged pattern match
  (`sha256` hex output) was a false positive, not a real phone number.
- ⚠️ One inconsistency worth remembering: `wisata/README.md` line 45 explicitly says *"Repo ini
  private — hindari commit data sangat sensitif kalau ada"* — i.e. the wisata/ folder's own docs
  assume the repo stays private. Content-wise nothing sensitive was found there, but this
  assumption is now stale once the repo goes public — worth a quick second look at `wisata/`
  before/after flipping visibility, and consider updating that README line to stop assuming private.
- Also noted, unrelated to this task: branch `claude/combine-download-and-speed-optimization` has
  ~28 commits (UI renames, MP3 status, speed opt for Pre-Combine) never merged to `main`, dating
  back to around Aug 2026. Confirmed via a UI marker check that the user's daily-use version is
  still `main` (button reads "⬆ MP3", not "MP3:"), so this doesn't affect the fixes above — but it's
  a separate pile of unmerged work someone should decide on eventually.

## Remaining steps — all manual, GitHub web UI only (no tool/API access for these)

1. Merge (or open a PR for) `claude/html-mandarin-player-iphone-xsosol` → `main`. Not created yet —
   user hadn't confirmed before this handoff was written.
2. Settings → General → Danger Zone → Change visibility → **Public**.
3. Settings → Pages → Build and deployment → Source: **Deploy from a branch** → Branch **main**,
   folder **/ (root)** → Save.
4. Bookmark in Safari once live:
   `https://prasetiogpt.github.io/WT-Repo01/html-mandarin-player/HTML_mandarin_player.html`

## Known unverified risk — flag before relying on it

Alt/Combine mode's whole screen-off design (combining rows into one audio file so zero JS runs
mid-sequence) was engineered and tested **only against Android Chrome's throttling behavior**
(devices tested: Vivo, Redmi, Realme — see `html_player_deep_learning.md`,
`pull_to_refresh_solution.md`). Nothing in project history documents it being tested on iOS
Safari. Safari has a different background-tab lifecycle (can suspend/discard a backgrounded tab's
JS context entirely under memory pressure, not just throttle timers) — the app does use
`navigator.mediaSession`, which is a genuine point in its favor for iOS specifically, but this is
inference, not a verified result. **Recommend the user actually test:** upload CSV+ZIP, pick Alt
mode, Play All, turn screen off, wait a few minutes, confirm audio keeps going to the end.
