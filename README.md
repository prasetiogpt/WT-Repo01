# WT-Repo01 — WTMandarin Apps (source code + memory mirror)

Private repo for 3 interdependent Mandarin-learning apps built by/for prasetiogpt:
`html-mandarin-player/`, `mp3-generator/`, `anki-deck-builder/`.

Also holds `wisata/` — a separate, unrelated umbrella folder for personal trip itineraries
(one subfolder per trip/country, e.g. `wisata/china/`), migrated here from the laptop so this
repo is the full source of truth (code AND data) for them. See `wisata/README.md` for the
general convention and each subfolder's own README for its workflow — this does NOT follow the
Drive-is-primary / memory-mirror convention described below, which applies only to the 3
Mandarin apps.

## What lives here vs. what lives on Google Drive

**Primary working environment is Google Drive (`I:\My Drive\WS Fam\`), not this repo.**
This repo holds two things:

1. **Source code** (the actual source of truth for code — see each app folder). Edited here,
   committed, then the latest build is copied back to the Drive folder for testing/use.
2. **`<app>/memory-mirror/`** — a periodic backup/mirror of that app's memory docs, which
   normally live at `I:\My Drive\WS Fam\Memory\<app>\`. **This mirror is NOT the primary memory
   source — it exists purely as a fallback for disaster recovery.**

## Memory: primary vs. fallback (read this if you're picking up work with no Drive access)

- **Default, every normal session:** read and write memory at
  `I:\My Drive\WS Fam\Memory\<app>\`. Only touch `<app>/memory-mirror/` here if that path is
  genuinely unreachable (e.g. Claude Desktop/Code is running in a cloud/remote environment with
  no access to this user's local Google Drive mount — this has happened before after repeated
  Desktop app crashes).
- **If you're reading this because the Drive path IS unreachable:** use
  `<app>/memory-mirror/` as your memory for this session. It won't be perfectly current (only
  synced when the user asks for a checkpoint), but it's the best available context.
- **Once Drive access is confirmed working again:** copy anything written to `memory-mirror/`
  during the fallback period back to `I:\My Drive\WS Fam\Memory\<app>\`, reconciling with
  whatever changed there in the meantime, then resume treating Drive as primary. Don't just
  silently switch back without syncing — that would lose whatever was learned/decided during
  the fallback period.

Each `<app>/memory-mirror/` also has its own short README noting when it was last synced.

## Version history convention

Each app's source file has a **fixed filename** (no version number in the name) — `git log` is
the version history now, replacing the old "one file per version number" convention. See each
skill (`html-mandarin-player`, `wtmandarin-mp3-generator`, `anki-deck-builder`) for full operating
rules.
