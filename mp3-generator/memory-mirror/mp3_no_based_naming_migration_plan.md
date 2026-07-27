---
name: mp3_no_based_naming_migration_plan
description: "MP3 filename matching migrated from the 'Ref.' column back to the 'No' column (with letter suffixes like 1a/1b/1c), across MP3 Generator and HTML Player"
metadata:
  node_type: memory
  type: project
---

# MP3 Filename Matching: "No" Column (1a/1b/1c) — Decision Record

**Status: DONE (2026-07-23 to 2026-07-25).** MP3 Generator and HTML Player both key MP3
filenames off the CSV's "No" column (raw string, letters allowed). "Ref." is no longer read for
MP3 matching and is free for the user to repurpose. Verified end-to-end with real generated MP3s
played in-browser, including with "Ref." blank.

## Final format

`{prefix}_{no}_{key}.mp3` — e.g. `010_1a_mandkw.mp3`. `no` is the raw "No" cell value passed
through a filename-safe sanitizer (strips `<>:"/\|?*` only — no lowercasing, no stripped dots, no
zero-padding, no `int()`/`parseInt()` parsing of any kind). Both tools must produce the identical
sanitized string or filenames won't match:
- **MP3 Generator** (`wt_mandarin_mp3_generator_gui.py`): `read_rows_numbered()` uses
  `safe_name(raw_no)`, falling back to physical row position only when "No" is blank.
  `library_filename()` = `f"{prefix}_{row_no}_{key}.mp3"`.
- **HTML Player** (`HTML_mandarin_v25_11_100.html`): `getRowIndexFromTr()` reads `cells[0]` ("No")
  raw, sanitizes the same way, same blank-row fallback. Matching is case-insensitive on this side.

## Why "Ref." existed, and why it was retired

"No" was always the intended long-term MP3-matching key — it's user-facing and can contain letter
suffixes (`1a`, `8c`). "Ref." was added earlier purely as a workaround: MP3 Generator's Python
code could only `int()`-parse a clean sequential number, so a separate pure-integer column was
needed until the Generator was revised to handle letter-suffixed "No" values directly. Once that
revision shipped (2026-07-23) and HTML Player was reverted to read "No" directly (2026-07-25),
"Ref." had no remaining role in MP3 matching and was freed up for the user's own use.

**Bug found along the way:** JS `parseInt("1a")` silently truncates to `1` (unlike Python's
`int()`, which raises) — this was collapsing every letter-suffixed row in the same numeric group
onto the same MP3 filename before HTML Player's matching code was rewritten to stop parsing "No"/
"Ref." as a number at all. Worth remembering for any future numeric-looking-string parsing in this
codebase.

## Rollback backup

**`I:\My Drive\WS Fam\Backup Sebelum Migrasi No-Based 2026-07-23\`** — full pre-migration copies of
HTML Player, MP3 Generator (source + built `.exe`), Anki Builder, and every CSV under `Text File\`
(the CSVs matter most here, since migration step 2 below rewrites "No" values in place). Not
re-taken after the migration — treat as a point-in-time snapshot, not a rolling backup.

## Still open

The rest of the old `Text File\` CSVs (everything except the one test file,
`Breakdown\010 Break tes.csv`) still use the old numbering scheme and haven't been renumbered to
the `1a`/`1b`/`1c` scheme or had their MP3s regenerated yet.
