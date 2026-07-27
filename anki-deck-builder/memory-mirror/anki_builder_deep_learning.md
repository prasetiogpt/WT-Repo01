---
name: anki_builder_architecture
description: "Consolidated learning notes on Anki Deck Builder v3 architecture, preset system, and APKG generation"
metadata: 
  node_type: memory
  type: project
  originSessionId: d38ba609-545e-4921-addc-02aedf6f4cee
---

# Anki Deck Builder — Architecture & Implementation

**Level:** Advanced Technical Reference  
**Version:** v3 (FIXED)  
**Last Updated:** 2026-07-12  

---

## 🏗️ Core Architecture

### **Application Purpose**

**Input:** CSV files with Mandarin learning data  
**Output:** APKG files for AnkiDroid  
**Key Feature:** Preset persistence (localStorage)  

**Data Flow:**
```
CSV Upload
  ↓
Parse → Detect columns
  ↓
Map columns to Front/Back
  ↓
Apply styles & audio tags
  ↓
Preview cards
  ↓
Export APKG (Anki format)
```

---

## 💾 Preset System (Fixed in v3)

### **4 Root Causes of Preset Persistence Bug (ALL FIXED)**

**Issue 1: Incomplete readStore() Initialization (Line 449)**
```javascript
// BEFORE: Missing activePreset field
return {presets:{}};

// AFTER: Complete structure
return {presets:{}, activePreset: null};
```
**Impact:** New presets created without proper initialization

**Issue 2: No Validation in writeStore() (Line 452)**
```javascript
// BEFORE: Silent save, no checks
localStorage.setItem(STORAGE_KEY, JSON.stringify(store));

// AFTER: Validation + error handling
if (!Array.isArray(preset.frontItems)) preset.frontItems = [];
// ... validate other fields
localStorage.setItem(STORAGE_KEY, JSON.stringify(validated));
```
**Impact:** Corrupt data could be saved undetected

**Issue 3: CRITICAL Data Loss in normalizeConfig() (Line 495-496)**
```javascript
// BEFORE: Filter removes null values (DATA LOSS!)
cfg.frontItems=(cfg.frontItems || []).map(resolveColumnName).filter(Boolean);

// AFTER: Preserve original if resolve fails
cfg.frontItems=(cfg.frontItems || []).filter(name => {
  const resolved=resolveColumnName(name);
  return resolved || name;  // Keep original name!
});
```
**Why Critical:**
- Session 1: Save "Eng KW", "Indo KW"
- Session 2: resolveColumnName returns null (CSV loaded differently)
- Old code: null filtered out → frontItems becomes []
- New code: preserves original name → frontItems stays ["Eng KW", "Indo KW"]

**Issue 4: Hardcoded Override (Line 498-502)**
```javascript
// BEFORE: Force-add Indo KW regardless of saved preset
if(presetName==='english'){
  const indoKw=pickCols([['Indo KW','Arti KW']]);
  if(fixed.length) cfg.frontItems=fixed;  // OVERRIDE SAVED PRESET!
}

// AFTER: Removed completely
// Let saved preset work without interference
```
**Impact:** User's carefully saved preset would get overridden on load

---

## 🎫 Preset JSON Structure

**Complete Schema:**
```json
{
  "version": 19,
  "presetName": "mandkw",
  "frontItems": ["Eng KW"],
  "backItems": ["Mand KW", "Pin Yin KW", "Indo KW", "Mandarin"],
  "styles": {
    "Eng KW": { "size": 48, "bold": true, "align": "center" }
  },
  "audio": {
    "Eng KW": { "enabled": true, "lang": "en-US" }
  },
  "deckMode": "master",
  "parentDeck": "Mandarin Master",
  "deckName": "Mandarin",
  "subdeckName": "Text 001",
  "noteType": "WT Basic",
  "onlyChecked": true,
  "skipEmptyCards": true,
  "showFrontOnBack": true,
  "nativeAnkiTts": true
}
```

**Built-in Presets:** mandkw, sentence, english, full

---

## 🔑 Key Functions

### **Storage Layer**

**readStore() (Line 449)**
```javascript
function readStore(){
  try{
    const current=localStorage.getItem(STORAGE_KEY);
    if(current) return JSON.parse(current);
    
    // Backward compat: check old keys
    for(const key of PREVIOUS_STORAGE_KEYS){
      const previous=localStorage.getItem(key);
      if(previous){
        const parsed=JSON.parse(previous);
        localStorage.setItem(STORAGE_KEY, JSON.stringify(parsed));  // Migrate
        return parsed;
      }
    }
    
    return {presets:{}, activePreset: null};  // Default empty
  }catch(e){ 
    return {presets:{}, activePreset: null};  // Error fallback
  }
}
```

**Pattern:** Try current key → try old keys for migration → return default

**writeStore() (Line 455)**
```javascript
function writeStore(store){
  try{
    const validated = {
      presets: store.presets || {},
      activePreset: store.activePreset || null
    };
    // Validate each preset's structure
    Object.values(validated.presets).forEach(preset => {
      if (!Array.isArray(preset.frontItems)) preset.frontItems = [];
      // ... validate other fields
    });
    localStorage.setItem(STORAGE_KEY, JSON.stringify(validated));
  }catch(e){
    console.error('Failed to save preset:', e);
    // Show error to user
  }
}
```

**Pattern:** Validate before serialize, error handling + user feedback

---

### **Configuration Management**

**currentConfig() (Line 467)**
```javascript
function currentConfig(){
  return {
    version: APP_VERSION,
    presetName: state.activePreset,
    frontItems: [...state.frontItems],
    backItems: [...state.backItems],
    styles: clone(state.styles),
    audio: clone(state.audio),
    // ... all UI settings
  };
}
```

**normalizeConfig() (Line 493)**
```javascript
function normalizeConfig(config, presetName){
  const cfg=clone(config);
  
  // Try resolve column names, keep originals if not found
  cfg.frontItems=(cfg.frontItems || []).filter(name => {
    const resolved=resolveColumnName(name);
    if(!resolved) console.warn(`Column not found: "${name}", keeping original`);
    return resolved || name;  // KEY FIX: Keep original!
  });
  
  // Build-in preset: don't override user's saved preset
  const builtIn=builtinPreset(presetName);
  if(builtIn && !config.presetName){  // Only if no saved preset
    cfg.frontItems=builtIn.frontItems;
    cfg.backItems=builtIn.backItems;
  }
  
  return cfg;
}
```

**Pattern:** Defensive copying, graceful fallback for missing data

---

### **APKG Export**

**APKG Format:**
```
APKG File (Anki Package)
├── collection.anki2        (SQLite database)
├── media                    (Media files like MP3s)
└── [manifest required]      (ZIP structure)
```

**Export Flow:**
1. Read UI settings → currentConfig()
2. Build deck structure (parent/sub per deckMode)
3. Create note for each CSV row
4. Serialize to SQLite
5. Package as ZIP (APKG)

---

## 🎨 Styling System

**Per-Column Styles:**
```javascript
const BUILTIN_STYLES = {
  "Mand KW": {
    font: "Noto Sans SC, Microsoft YaHei",
    size: 42,
    bold: true,
    align: "center"
  },
  "English": {
    font: "Arial",
    size: 24,
    bold: false
  }
};
```

**Applied to:**
- Preview (HTML rendering)
- Export TSV (for Anki import)
- Not directly to APKG (Anki has its own card styling)

---

## 🎯 Deck Modes

**Mode: "master" (Parent + Sub)**
```
Mandarin Master (parent deck)
├── Text 001 (sub)
├── Text 002 (sub)
└── Text 003 (sub)
```

**Mode: "single" (One Deck + Tags)**
```
Mandarin (single deck)
All cards tagged by file: [001], [002], [003]
```

**Mode: "separate" (Independent)**
```
Text 001 (independent)
Text 002 (independent)
Text 003 (independent)
```

**Why 3 Modes?**
- master: organize by lesson
- single: study all together with file tags
- separate: complete independence

---

## 📋 Column Resolution

**Problem:** User might name columns differently
- "Mand KW" vs "Hanzi KW" vs "Chinese Keyword"
- "Pin Yin" vs "Pinyin" vs "py"

**Solution: Aliases**
```javascript
const ALIASES = {
  "Hanzi KW": "Mand KW",
  "Hanzi Keyword": "Mand KW",
  "English KW": "Eng KW",
  "Pinyin KW": "Pin Yin KW",
  // ... more aliases
};

function resolveColumnName(name){
  if(ALIASES[name]) return ALIASES[name];
  if(CSV_HEADERS.includes(name)) return name;
  return null;  // Not found
}
```

**Pattern:** Try aliases, then exact match, then null

---

## ⚠️ Limitations & Edge Cases

**No Server Sync:**
- localStorage only, no cloud backup
- Lost if browser data cleared
- Per-browser storage (not cross-device)

**No Version Migration:**
- If v3 adds new fields, old v2 presets might break
- Handled gracefully: missing fields get defaults

**Column Name Sensitivity:**
- Aliases help but exact match preferred
- Always validate CSV headers on load

---

## 🚀 14 Potential Improvements (From Review)

**HIGH Priority (Robustness):**
1. Modularize PresetStore class
2. Validate CSV parsing (warn on empty)
3. Add DEBUG logging system

**MEDIUM Priority (Reliability):**
4. Define PRESET_SCHEMA constant
5. Add type checks before JSON operations
6. Add preset version warning
7. Export preset as text (not just JSON)

**LOW Priority (Polish):**
8. Undo/redo support
9. Lazy-load external libraries
10. Add validation report UI
11. API fallback for old browsers
12. Local library bundling
13-14. Code refactoring (low value)

---

## 💡 Modification Guidelines

**Safe Modifications:**
- Add new preset (copy existing, modify)
- Add new note type
- Adjust default styles
- Improve validation messages

**Risky Modifications:**
- Changing preset JSON structure → migration needed
- Modifying normalizeConfig() → data loss risk
- Changing column resolution → breaks existing presets
- APKG export format → format compatibility risk

**Before Large Changes:**
1. Understand the 4 root causes of v3 fixes
2. Add comprehensive error handling
3. Test with existing presets from users
4. Plan migration for any schema changes

---

## 🆕 2026-07-16 Updates (unrelated to the v3 preset-persistence fixes above)

Current active file: `Anki Deck Builder/Anki Versions/Anki_Deck_Builder_Master_14.html` (this is
the same file previously tracked as `Anki_Deck_Builder_Master_14_FIXED_v3.html` — it got
renamed at some point via Drive sync, dropping the `_FIXED_v3` suffix; the v3 fixes above are
still present in it, confirmed via the `// NOTE: Removed hardcoded override for 'english' preset`
comment still in the code).

**1. Audio auto-force now respects an explicit manual override.** `autoNativeTtsColumn()` force-
enables native Anki TTS for columns matching english/english-kw/mandarin/hanzi-kw patterns,
regardless of the manual "enabled" checkbox — intentional safety net so key columns never end up
silent (comment references a past "APKG 007" export). Problem: this meant the checkbox couldn't
actually turn OFF audio for those columns. Fix: added `a.userSet` flag on `state.audio[column]`,
set when the user touches the "enabled" checkbox in the Audio tab; `enabledAudioColumns()` now
lets an explicit uncheck (`userSet && !enabled`) override the auto-force. Untouched columns keep
the old default-on safety-net behavior.

**2. New option: repeat the question's voice on the Answer page, independent of the Question page.**
New checkbox `repeatQuestionVoiceOnBack`. Previously the Answer page (`afmt`) reused the magic
`{{FrontSide}}` field, which always carried over whatever audio the Question page had (tied to
`voiceOnFront`) — no way to have the question read only on the Answer page or vice versa.
`{{FrontSide}}` was replaced with explicit `{{Front}}` + an independently-gated audio block. Only
takes effect when `showFrontOnBack` is also on (user's explicit choice — not made independent of
it). Applies to Card 2 Reverse too. The browser preview (`renderPreview`/`renderCardSide`) was
also fixed to simulate this — previously the preview's Front and Back panels were fully
independent and never showed this combined-page behavior at all.

**3. Output filename (Explorer) now separate from in-Anki deck name.** `outputRootName()`
controls only the saved `.apkg` filename; `fullDeckNameForRow()` (deck name inside Anki) untouched.
For deckMode "master": single subdeck → `Parent (token).apkg`; multiple files/group → 
`Parent (firstToken-lastToken).apkg` (token = first word of subdeck/file name, via new
`deckNumberToken()` helper, `state.selectedFileNames` order).

**4. Output folder can now be "remembered" across sessions via IndexedDB** (not the preset JSON —
a `showDirectoryPicker()` handle isn't JSON-serializable). New `saveFolderHandle()` /
`loadFolderHandle()` / `tryRestoreFolderHandle()`; the last one runs automatically on page load.
If the browser's permission grant is still valid, the folder activates silently; otherwise a
one-click "Aktifkan lagi" button appears instead of the full folder-picker dialog. Chrome/Edge
only (File System Access API).

**5. Cosmetic renames (2026-07-16):** "Download APKG" button → "Generate APKG"; quick-preset
labels shortened ("Mandarin Keyword"→"Mand KW" etc., internal keys `mandkw`/`sentence`/`english`/
`full` unchanged); several Card Display checkbox labels shortened; the explanatory paragraph under
the repeat-question checkbox removed per user request (behavior unchanged, just no longer spelled
out in the UI — see fact #4 above for the underlying logic if asked).

**6. Follow-up fix same day: the Audio tab checkbox was lying about what would actually happen.**
The `userSet` override (point 1) only suppressed auto-force for columns the user had *actively
toggled* in the current session. But the checkbox's displayed checked/unchecked state was driven
purely by the raw stored `a.enabled` value — for any column whose saved data already had
`enabled:false` (e.g. saved before this fix existed, or simply never touched), the checkbox showed
**unchecked**, while the invisible auto-force silently still added `{{tts}}` for it in the actual
APKG. User confirmed this exact symptom: "Eng KW" and "English" unticked in the Audio tab and
absent from the browser preview, but audible in AnkiDroid. Root cause: checkbox display and real
behavior were two different computations. Fix: added `columnWillHaveVoice(column)` — a single
shared function returning `{willHaveVoice, viaAutoForce}` — used by BOTH `enabledAudioColumns()`
(what actually goes in the export) AND `renderAudio()`'s checkbox `checked` attribute (what the
user sees), so the two can never disagree again. Also added a small inline hint ("Otomatis aktif
... uncheck untuk matikan") under any checkbox that's checked only because of auto-force, so the
user understands why before deciding whether to turn it off.

**7. ~~Found and fixed: `Skills/artifacts/Anki_Deck_Builder_Master_14.html` was a STALE COPY~~ —
⚠️ MOOT as of 2026-07-26.** The underlying incident (a `Skills/artifacts/` mirror of the live
Anki Versions file drifting 177 lines out of sync, causing a "fixed" audio bug to reappear from
the stale copy) is real history, but its "always sync Skills/artifacts/" lesson no longer applies:
the whole `Skills/` folder mechanism was retired in favor of the account-level server-side skill
(see [[skills_moved_to_server]]), and `Skills/artifacts/Anki_Deck_Builder_Master_14.html` doesn't
exist anymore. The general underlying caution — diff full content before assuming a same-named
file elsewhere is stale — lives on in [[file_dedup_diff_before_archive]].

**8. `__Source` and a "No"/"Nomor" column can render on one line instead of stacked.** New helper
`inlineCombineColumns(itemList, row)` detects when a side's item list contains BOTH `__Source`
and a column matching `/^no\.?$|^nomor$/i` (so "No", "No.", or "Nomor" — the user's actual column
was literally named "No", not "Nomor"; the regex was fixed 2026-07-16 after first shipping it too
narrow) with non-empty text for that row; when both are present, `sideParts()` (real APKG output)
and `renderCardSide()` (tool's own preview) emit them as two `<span class="anki-field-inline">`
inside one flexbox `<div>` instead of two separate stacked `<div class="anki-field">` blocks.
Falls back to normal stacked rendering if only one of the two has text for a given row. Scoped
specifically to these two columns — other columns are unaffected and still get their own line
each.

**9. Sticky sidebar + sticky tab bar (desktop, >980px)** so working in a tab or scrolled deep into
a tall panel doesn't require scrolling back up to reach config controls; falls back to normal
static stacking under the 980px mobile breakpoint.

**10. Folder renamed: `versions/` → `Anki Versions/`** — per-project distinct version-folder names
across all 3 WTMandarin projects instead of every project having an identically-named `versions/`
(HTML+MP3 Player's got renamed to `HTML Versions/` the same way; MP3 Generator has none yet).

**11. "Data Source" card made collapsible + Generate APKG button relocated below "Pilih Folder".**
**Found and fixed a pre-existing CSS bug while doing this, worth remembering as a landmine:** any
`<details>` block on this page failed to actually hide its content when collapsed — only the
disclosure triangle changed — because feature-specific `display:flex|grid` rules on the content
elements out-specificity the browser's native collapse behavior. Fixed globally with
`details:not([open])>*:not(summary){display:none!important}`, which applies to every `<details>`
on the page, not just the new one. **Anyone adding a new `<details>` block to this codebase should
know this rule exists** so they don't reintroduce the bug.

**12. Layout changed from 2-column to responsive 3-column** (`.wrap` max-width raised to `1680px`,
a `@media(min-width:1300px)` breakpoint upgrades the grid to `340px 1fr 340px`) to use unused
space on wide laptop screens; content reshuffled by purpose across the two sidebars. Falls back to
2-column at medium widths and single-column under 980px, unchanged from before.

**13. New feature: auto-fill empty sentence cells within a "No." group.** Source data pattern
(from user's actual CSV, `000 Data Testing.csv`): each "No." group has several keyword-only rows,
and only ONE row per group (usually the last) has the full-sentence columns (Pin Yin, Indonesia,
Mandarin, English) filled in — the rest are blank in those 4 columns. New checkbox
`fillSentenceByNo` ("Isi otomatis kalimat kosong berdasarkan kolom No"), default **checked**, in
the Data Source card.

Implementation: `state.rowsRaw` now holds the pristine, never-mutated merged rows (set in
`loadFiles()` right after `mergeParsedFiles`); `state.rows` (used everywhere else — Data tab,
Preview, APKG build) is derived from it via `applySentenceFillIfEnabled(rows, columns)`, which:
1. Finds the grouping column via the SAME `/^no\.?$|^nomor$/i` pattern used by `inlineCombineColumns` (fact #8) — reused for consistency, not duplicated logic.
2. Finds target columns via new `isSentenceColumn(column)` — matches Mandarin/Hanzi Kalimat,
   Pin Yin/Pinyin, Indonesia/Arti Indonesia, English by exact name, explicitly EXCLUDING anything
   with "kw"/"keyword" in it (so "Eng KW"/"Mand KW" etc. are never touched, only the full-sentence
   columns).
3. `fillSentenceColumnsByGroup(rows, groupColumn, targetColumns)` does the actual fill: for each
   group value, finds the first non-empty value per target column anywhere in that group, then
   fills any empty cell in that group/column with it.

Toggling the checkbox re-derives `state.rows` from `state.rowsRaw` live (no re-upload needed) via
a dedicated `onchange` handler. Persisted in presets via `currentConfig()`/`applyConfig()`
(`fillSentenceByNo` field) — but note `applyConfig()` runs partway through `loadFiles()`, so the
fill-recompute call was deliberately placed AFTER `applyConfig()` in `loadFiles()`, not before —
otherwise a saved preset that restores a different checkbox value wouldn't be reflected in the
freshly-loaded rows. `btnReset` also clears `state.rowsRaw`.

Verified in-browser end-to-end using the user's actual CSV pattern (real `<input type=file>`
`change` event, not just calling `loadFiles()` directly — an earlier test that called both
produced a confusing double-invocation artifact, not a real bug, since the file input already had
a `change` listener wired): empty sentence cells fill correctly from the group's non-empty row,
KW columns stay untouched, unchecking reverts to blank, rechecking re-fills, `rowsRaw` never
mutates.

**Process note (⚠️ superseded 2026-07-26):** a Claude Code skill was set up for this project on
2026-07-16, initially in the wrong (machine-local, C:\ drive) location before being corrected to
`.claude/skills/anki-deck-builder/` inside the Drive-synced project folder. That project-scoped
skill location was itself retired 2026-07-26 in favor of the current account-level server-side
skill (see [[skills_moved_to_server]]) — neither location is where the skill lives anymore. The
general lesson survives independent of the specific path: read `Memory/MEMORY.md` and
`workspace_preference.md` at the start of a session on this project before creating any new file,
rather than defaulting to the assistant's own built-in memory/skill locations.

---

**This is the foundation for all future Anki Builder maintenance and enhancement.**
