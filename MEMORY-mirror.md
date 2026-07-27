# WTMandarin Memory Index

**Purpose:** Permanent reference for understanding and modifying 3 interdependent projects

**📍 Workspace Location:** `I:\My Drive\WS Fam\` (ONLY - do not use C:\ or other drives)  
**📁 Memory Folder:** `I:\My Drive\WS Fam\Memory\` (this folder — reorganized into per-project subfolders 2026-07-26, see below)  
**🛠 Skills Folder:** `I:\My Drive\WS Fam\Skills\` — only `artifacts\Preset_A2.json` remains (live Anki Deck Builder app data, NOT a stale skill file). Both custom skills (`wtmandarin-mp3-generator`, `anki-deck-builder`) are now account-level server-side skills, see [workspace/skills_moved_to_server.md](workspace/skills_moved_to_server.md)

**📂 Folder Map:**
- `html-player/` — HTML Mandarin Player memory
- `mp3-generator/` — MP3 Generator memory
- `anki-builder/` — Anki Deck Builder memory
- `financial/` — Summary Bisnis.xlsx project (unrelated to WTMandarin)
- `workspace/` — meta: workspace setup, collaboration style, staging/archiving rules
- root — misc notes that don't cleanly belong to one project (AnkiDroid personal notes, Top 2000 Hanzi)

**🧹 2026-07-27 cleanup pass:** duplication/verbosity/staleness review across the 3 apps' memory
files, requested to check for content that should live in a Skill instead. Several fully-redundant
or fully-superseded files were archived to
`Temp Claude/2026-07-27 Memory Cleanup - HTML Player, MP3 Gen, Anki Builder/` (see that folder's
`_KENAPA_DIPINDAH_KESINI.md` for exactly what and why — nothing deleted permanently, safe to
restore if a judgment call turns out wrong): `html-player/v25_11_100_changelog.md`,
`html-player/html_player_v25_11_100_development.md`, `html-player/session_2_handover.md`,
`html-player/html_player_status.md`, `html-player/screen_off_investigation.md`,
`html-player/screen_off_fix_plan.md`, `wtmandarin-shared/wtmandarin_projects_index.md` (whole
folder removed, now empty), root `session_3_final_summary.md`, root `session_4_multi_device_setup.md`.
Several remaining files were trimmed in place (session-log-style narration compressed to
pointer+summary, stale "PENDING"/"IMPLEMENTATION_READY" notes corrected to point at what actually
shipped) — see each project's deep-learning file for current state.

---

## 📚 Deep Learning Notes (Read These First)

- [HTML Player Architecture](html-player/html_player_deep_learning.md) — Design decisions, dual-column system, canPlayMode filter, why screen-off works
- [MP3 Generator Architecture](mp3-generator/mp3_generator_deep_learning.md) — TTS flow, speed control, concatenation, library naming, integration points
- [Anki Builder Architecture](anki-builder/anki_builder_deep_learning.md) — v3 preset bug fixes (4 root causes), storage system, APKG generation

---

## 📍 Project Status & Locations

Current versions/status/integration for all 3 apps live in the Quick Reference and Integration
Map sections below — that's the up-to-date source now (the old separate project-index file was
retired 2026-07-27 for being permanently out of date, see cleanup note above).

---

## 🔧 Solutions & Technical Fixes

- [Pull-to-Refresh Prevention (v25_11_88)](html-player/pull_to_refresh_solution.md) — CSS touch-action + JS capture phase, 100% success on Vivo V9/Redmi/Realme/Vivo V27E
- [MP3 Naming Migration: Ref. → No (1a/1b/1c)](mp3-generator/mp3_no_based_naming_migration_plan.md) — ✅ **DONE end-to-end as of 2026-07-25.** Both MP3 Generator and HTML Player now key MP3 filenames off the "No" column (e.g. `1a`) instead of "Ref." — verified with real generated MP3s played in-browser, including with "Ref." actually blank. "Ref." column is now free for the user to repurpose. Still TODO: renumber the rest of the old `Text File\` CSVs + regenerate their MP3s (only the `010 Break tes.csv` test file uses the new scheme so far). Supersedes the stale "PENDING 1a/1b naming" notes in the MP3 Generator / HTML Player deep-learning docs below. 🔒 Pre-migration rollback backup at `Backup Sebelum Migrasi No-Based 2026-07-23\` (HTML Player, MP3 Generator, Anki Builder, all Text File CSVs) — see file for exact contents.

---

## 🔒 PRODUCTION RELEASE

- [HTML Player v25_11_100 FINAL](html-player/html_player_v25_11_100_final.md) — **🔒 Feature-locked baseline (2026-07-14)**: Alt (Pre-Combine) mode, screen-off support via combined audio, status message repositioned. **No new features** without major requirement shift, but bug/perf fixes are in scope — see the 2026-07-22 combine patch documented in the same file (mono/24kHz output, batched decode, UI-freeze fix, Pre-Comb re-entrancy guard, cache-survives-mode-switch, wrong "Mode TTS aktif" message fix).

---

## 🔧 Development Context

- [Workspace Paths](workspace/workspace_paths.md) — **I: drive ONLY** → Workspace: I:\My Drive\WS Fam\ | Deliverable HTML: I:\My Drive\WS Fam\HTML+MP3 Player\HTML Versions\ (renamed 2026-07-16, was \versions\)
- [Multi-Device Workspace Setup](workspace/workspace_preference.md) — User works on multiple laptops with I: drive access
- [User Collaboration Style](workspace/user_collaboration_style.md) — Preferences, workflow, communication style, and lessons learned from past mistakes
- [Temp Claude Staging Rule](workspace/temp_claude_staging_rule.md) — never delete workspace files directly; stage in `Temp Claude\` first, dated + labeled for easy restore
- [Skills Moved to Server](workspace/skills_moved_to_server.md) — both MP3 Generator/HTML Player and Anki Deck Builder skills now server-side (2026-07-26); `Skills\`/`.claude\skills\` cleared except live `Preset_A2.json`
- [Diff Before Archiving "Duplicates"](workspace/file_dedup_diff_before_archive.md) — near-miss data loss 2026-07-26: always diff full content before archiving a same-named file as stale, don't assume by folder location

---

## 📌 Other Notes (not a WTMandarin project, kept here per the I:-drive-only rule)

- [AnkiDroid Scheduler Notes](ankidroid_scheduler_notes.md) — personal AnkiDroid app troubleshooting, unrelated to the 3 codebases above
- [Top 2000 Hanzi Project](top_2000_hanzi_project.md) — `Text File\000 Top Hanzi.csv`: frequency-ranked hanzi list + example sentences sourced from `000 Merge 001-010 Text.csv`; rows 1-500 done, 501-2000 pending sentences; sourcing/matching methodology + normalization gotcha

## 💰 Financial — Summary Bisnis.xlsx (separate project, unrelated to WTMandarin)

- [Bank Monthly Sheet Structure](financial/bank_monthly_sheet_structure.md) — layout of `Financial\Summary Bisnis.xlsx` sheet "Bank Monthly": banks tracked, row/formula layout, units (Rp miliar, truncated), which report line items to pull
- [Bank Report Sources](financial/bank_report_sources.md) — where/how to fetch each bank's (BBCA/BMRI/BBRI/BBNI/NISP) monthly published report
- [XLSX Recalc Windows Workaround](financial/xlsx_recalc_windows_workaround.md) — recalc.py fails here (no LibreOffice); use Excel COM via PowerShell instead
- [Bank Report Scheduled Task](financial/bank_report_scheduled_task.md) — status of the auto-check/auto-fill cron task, which laptop has it, pending on the other one until user asks

---

## 🎯 Quick Reference

### HTML Player (v25_11_100 - feature-locked baseline, patched 2026-07-22)
- **Key feature:** Alt (Pre-Combine) mode with intelligent caching + screen-off support
- **Screen-off:** Works via combined audio file (1 file = no JS callbacks needed)
- **Trade-off:** Row highlights/loop logic simplified; Baca No disabled in Alt mode
- **Status message:** Repositioned to bottom for better visibility
- **Locked:** No further feature additions without reconsidering screen-off architecture — bug/perf fixes ARE in scope (see 2026-07-22 combine patch)
- **2026-07-22 patch:** combine now mono/24kHz (was stereo/browser-rate), decode batched 8-at-a-time with per-file progress, UI-freeze during Pre-Comb fixed (was a real paint-starvation bug), Pre-Comb button now has a re-entrancy guard, cache now survives Audio Mode switching (was wiped every time), "Mode TTS aktif" no longer wrongly shown in Alt mode — full detail in [html_player_v25_11_100_final.md](html-player/html_player_v25_11_100_final.md)
- **2026-07-25 addition:** red "Ytube" button per sheet (after V4, before Loop) — opens the YouTube link from the source CSV's top-left cell if present. When absent, button stays the SAME size (text is always in the DOM, just color-matched to the background so it looks blank — an empty-string label was tried first but made the button visibly shrink, fixed same day). CSV download — both single-tab AND merge, standardized same day — always follows row1=URL (or literal `xxx` placeholder if none/merge), row2=blank, row3=header, row4+=data, matching the original source file layout exactly. See [html_player_deep_learning.md](html-player/html_player_deep_learning.md#-youtube-link-button-added-2026-07-25).
- **Legacy:** v25_11_88 (pull-to-refresh fix) still available for reference

### MP3 Generator (v3.7 - Stable)
- **Key concept:** Sequence + delay config, async TTS generation, ffmpeg MP3 merging
- **Integration:** Creates MP3s matching HTML Player's filename pattern — now `010_1a_mandarin.mp3` style, keyed off the CSV's "No" column (letters allowed), not row position. Done 2026-07-25, see [[mp3_no_based_naming_migration_plan]].
- **2026-07-25:** trailing silence on "per sheet" output shortened 12s → 10s (both `generate_one()` and `generate_merged()`)
- **2026-07-25:** rebuilt & deployed a fresh `.exe` from the updated source, replacing `MP3 Generator\MP3 GENERATOR 3.7.exe` (old one still safe in the pre-migration backup). Verified by actually launching it twice, not just checking the file exists. Version string unchanged (still "v3.7 ZIP SAFE").
- **Note:** PyInstaller does NOT bundle ffmpeg → requires PATH setup

### Anki Builder (v3 - Production Ready)
- **Key concept:** Preset persistence via localStorage (4 fixes in v3)
- **Critical fix:** normalizeConfig() preserves original column name if resolve fails
- **Architecture:** Per-column styles + audio, deck structure flexibility
- **Next:** Optional improvements if needed, otherwise stable as-is

---

## 🔗 Integration Map

```
CSV Data (source)
  ↓
MP3 Generator → MP3 files (010_1a_mandarin.mp3, 010_1a_mandkw.mp3, ...)
  ↓
HTML Player → playback + UI (reads MP3 files, provides CSV export)
  ↓
Anki Builder → APKG deck (reads CSV, creates Anki cards)
```

**Key Sync Point:** MP3 naming convention — both tools key off the CSV's "No" column value
directly (done 2026-07-25, see [[mp3_no_based_naming_migration_plan]])

---

## 📋 Release Notes

- [v25_11_100 Final](html-player/html_player_v25_11_100_final.md) — Released 2026-07-14, patched 2026-07-22. Alt mode, screen-off support, status message repositioned. The single authoritative doc for this release — earlier development-stage notes and the near-duplicate changelog were archived 2026-07-27 (see cleanup note above), their content is either superseded or already folded into this file and [html_player_deep_learning.md](html-player/html_player_deep_learning.md).

---

## 📝 Recent Sessions

- **2026-07-27:** Memory cleanup pass across the 3 apps (duplication/verbosity/staleness review,
  requested check for skill-worthy content) — see cleanup note near the top of this file.

- **2026-07-26 (Session 9):** Skill consolidation + Memory reorganization. `wtmandarin-mp3-generator`
  and `anki-deck-builder` migrated to account-level server-side Claude Skills; `Skills\`/
  `.claude\skills\` cleared (except live `Preset_A2.json`). `Memory\` reorganized into per-project
  subfolders. Near-miss caught mid-session: a file archived as a "stale duplicate" actually had
  unique content — restored, lesson captured in
  [workspace/file_dedup_diff_before_archive.md](workspace/file_dedup_diff_before_archive.md). Full
  detail: [workspace/skills_moved_to_server.md](workspace/skills_moved_to_server.md).

- **2026-07-23 to 2026-07-25 (Session 8):** MP3 filename matching migrated from "Ref." to "No"
  (letters allowed, e.g. `1a`/`1b`/`1c`) across both MP3 Generator and HTML Player, end-to-end
  verified with real generated MP3s. Also: trailing silence shortened 12s→10s, MP3 Generator "per
  cell" output folders renamed/reorganized, HTML Player gained a per-sheet "Ytube" button. Full
  detail: [mp3_no_based_naming_migration_plan.md](mp3-generator/mp3_no_based_naming_migration_plan.md),
  [html_player_deep_learning.md](html-player/html_player_deep_learning.md#-youtube-link-button-added-2026-07-25).

- **2026-07-22 (Session 7):** HTML Player combine performance & reliability patch (7 fixes: mono/
  24kHz combine output, batched decode, UI-freeze fix, rAF→setTimeout yield-point fix, Pre-Comb
  re-entrancy guard, cache-survives-mode-switch, status message fix). Full detail:
  [html_player_v25_11_100_final.md](html-player/html_player_v25_11_100_final.md#html_player_combine_patch_2026_07_22).

- **2026-07-21 (Session 6):** Top 2000 Hanzi project recovery + data fix (not a WTMandarin app —
  see [top_2000_hanzi_project.md](top_2000_hanzi_project.md)).

- **2026-07-16 (Session 5):** Anki Deck Builder feature work — audio auto-force manual override,
  repeat-question-voice option, output filename split, IndexedDB folder persistence, sticky
  sidebar/tabs, `No`/`Nomor`+`__Source` inline rendering, cosmetic renames. Full detail:
  [anki_builder_deep_learning.md](anki-builder/anki_builder_deep_learning.md) (2026-07-16 section).

- **2026-07-15 (Session 4) / 2026-07-14 (Session 3):** Workspace consolidated to I: drive only;
  v25_11_100 locked & approved as final HTML Player version. (Session summary files for these two
  were archived 2026-07-27 — fully superseded by [workspace/workspace_paths.md](workspace/workspace_paths.md)
  and [html_player_v25_11_100_final.md](html-player/html_player_v25_11_100_final.md).)

- **2026-07-12:** v25_11_88 shipped (pull-to-refresh fix, all 4 test devices) — see
  [pull_to_refresh_solution.md](html-player/pull_to_refresh_solution.md). Earlier the same day:
  v25_11_87 with MediaSession API + debounce + auto-gen sentences.
