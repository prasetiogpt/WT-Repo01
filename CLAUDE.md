# WT-Repo01 — Orientation

Private repo, 3 Mandarin-learning apps: `html-mandarin-player/`, `mp3-generator/`,
`anki-deck-builder/`. Full policy detail is in root `README.md` — this file is just the fast
orientation so a new session doesn't have to explore first.

## Source of truth — different per thing

| What | Primary | This repo's role |
|---|---|---|
| **Source code** (`.html`, `.py`) | This repo (Git) | Source of truth. Fixed filename per app, no version-number-in-filename anymore — `git log` is the version history. |
| **Memory / docs** | Google Drive (`I:\My Drive\WS Fam\Memory\<app>\`) | Fallback mirror only, in `<app>/memory-mirror/`. Only treat it as primary if Drive is genuinely unreachable this session (e.g. cloud/remote environment with no local Drive mount) — see root `README.md` for the full fallback procedure. |

## Before touching an app's code

Each app has an account-level Skill that should auto-trigger on relevant topics — let it load
rather than re-deriving context from scratch:
- `html-mandarin-player`
- `wtmandarin-mp3-generator`
- `anki-deck-builder`

If you need deep architecture/history detail beyond what the skill gives you, the index is
`MEMORY-mirror.md` (root) — it's a pointer/map to the right doc, not something to read end to end.

## Data safety

No personal data (personal vocab, personal progress files, anything not code/docs) goes into this
repo, especially since it may be made public per-app later for GitHub Pages testing. Check file
contents/sizes before committing anything that wasn't clearly source code or docs.
