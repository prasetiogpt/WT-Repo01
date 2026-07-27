import csv
import asyncio
import subprocess
import tempfile
import threading
import queue
import json
import random
import re
import sys
import zipfile
import tkinter as tk
import tkinter.simpledialog
from pathlib import Path
from tkinter import ttk, filedialog, messagebox

try:
    import edge_tts
except ImportError:
    edge_tts = None

APP_TITLE = "WT Mandarin MP3 Generator v3.7 ZIP SAFE"
CONFIG_FILE = "config_gui.json"
PRESET_FILE = "presets_gui.json"

CHOICES = ["Diam", "Mand KW", "Indo KW", "Eng KW", "Mandarin", "Indonesia", "English", "Pin Yin KW", "Pin Yin"]

LANG_BY_COLUMN = {
    "Mand KW": "zh",
    "Mandarin": "zh",
    "Pin Yin KW": "zh",
    "Pin Yin": "zh",
    "English": "en",
    "Eng KW": "en",
    "Indonesia": "id",
    "Indo KW": "id",
}

ALIASES = {
    "Hanzi KW": "Mand KW",
    "Hanzi Keyword": "Mand KW",
    "English KW": "Eng KW",
    "English Keyword": "Eng KW",
    "Arti KW": "Indo KW",
    "Pinyin KW": "Pin Yin KW",
    "Pinyin": "Pin Yin",
}

# MP3 Library columns must match the HTML MP3 Folder player names.
LIBRARY_COLUMNS = [
    ("mandkw", "Mand KW", "Mand KW"),
    ("mandarin", "Mandarin", "Mandarin"),
    ("engkw", "Eng KW", "Eng KW"),
    ("english", "English", "English"),
    ("indokw", "Indo KW", "Indo KW"),
    ("indonesia", "Indonesia", "Indonesia"),
]
LIBRARY_COLUMN_LABELS = {key: label for key, label, _src in LIBRARY_COLUMNS}
LIBRARY_KEY_BY_SOURCE = {src: key for key, _label, src in LIBRARY_COLUMNS}

SYSTEM_PRESETS = {"Listening", "Shadowing", "Vocabulary"}

DEFAULT_CONFIG = {
    "sequence": ["Mand KW", "Mandarin", "English", "Diam"],
    "delay_after_ms": [2000, 2000, 1000, 0],
    "rows": "all",
    "random": False,  # compatibility with older config/presets
    "random_per_file": False,
    "random_merge_file": False,
    "global_tts_speed": "1.0",
    "advanced_rate": False,
    "rates": {"zh": "+0%", "en": "+0%", "id": "+0%"},
    "voices": {
        "zh": "zh-CN-XiaoxiaoNeural",
        "en": "en-US-JennyNeural",
        "id": "id-ID-GadisNeural",
    },
    "pitch": {"zh": "+0Hz", "en": "+0Hz", "id": "+0Hz"},
    "output_folder": "output_mp3",
    "last_input_folder": "",
    "last_active_preset": "Listening",
    "final_delay_ms": 10000,
    "auto_open_output": True,
    "skip_existing": True,
    "merge_files": False,
    "generate_mode": "long",
    "library_columns": {"mandkw": True, "mandarin": True, "engkw": True, "english": True, "indokw": True, "indonesia": True},
    "zip_per_text": False,
    "zip_all": False,
}

DEFAULT_PRESETS = {
    "Listening": {
        "sequence": ["Mand KW", "Mandarin", "English", "Diam"],
        "delay_after_ms": [2000, 2000, 1000, 0],
        "rows": "all",
        "global_tts_speed": "1.0",
        "random": False,
        "random_per_file": False,
        "random_merge_file": False,
        "advanced_rate": False,
        "rates": {"zh": "+0%", "en": "+0%", "id": "+0%"},
    },
    "Shadowing": {
        "sequence": ["Mandarin", "Mandarin", "English", "Diam"],
        "delay_after_ms": [1500, 2500, 1500, 0],
        "rows": "all",
        "global_tts_speed": "0.9",
        "random": False,
        "random_per_file": False,
        "random_merge_file": False,
        "advanced_rate": False,
        "rates": {"zh": "+0%", "en": "+0%", "id": "+0%"},
    },
    "Vocabulary": {
        "sequence": ["Mand KW", "Indo KW", "Eng KW", "Diam"],
        "delay_after_ms": [1500, 1500, 1500, 0],
        "rows": "all",
        "global_tts_speed": "1.0",
        "random": True,
        "random_per_file": True,
        "random_merge_file": False,
        "advanced_rate": False,
        "rates": {"zh": "+0%", "en": "+0%", "id": "+0%"},
    },
}


def app_dir() -> Path:
    # Important for PyInstaller --onefile:
    # store config/presets beside EXE, not temporary _MEI folder.
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent
    return Path(__file__).resolve().parent


def run_hidden(cmd, **kwargs):
    if "creationflags" not in kwargs and hasattr(subprocess, "CREATE_NO_WINDOW"):
        kwargs["creationflags"] = subprocess.CREATE_NO_WINDOW
    return subprocess.run(cmd, **kwargs)


def popen_hidden(cmd, **kwargs):
    if "creationflags" not in kwargs and hasattr(subprocess, "CREATE_NO_WINDOW"):
        kwargs["creationflags"] = subprocess.CREATE_NO_WINDOW
    return subprocess.Popen(cmd, **kwargs)


def deep_merge(base: dict, data: dict) -> dict:
    cfg = base.copy()
    for key, value in (data or {}).items():
        if isinstance(value, dict) and isinstance(cfg.get(key), dict):
            merged = cfg[key].copy()
            merged.update(value)
            cfg[key] = merged
        else:
            cfg[key] = value
    cfg["final_delay_ms"] = 10000
    return cfg


def normalize_preset(preset: dict) -> dict:
    raw = preset or {}
    p = deep_merge(DEFAULT_CONFIG, raw)
    # Older presets only had "random". Treat it as Random Per File.
    random_per_file = bool(raw.get("random_per_file", raw.get("random", p.get("random", False))))
    random_merge_file = bool(raw.get("random_merge_file", False))
    if random_merge_file:
        random_per_file = False
    return {
        "sequence": p["sequence"],
        "delay_after_ms": p["delay_after_ms"],
        "rows": p["rows"],
        "global_tts_speed": p["global_tts_speed"],
        "random": random_per_file,  # compatibility
        "random_per_file": random_per_file,
        "random_merge_file": random_merge_file,
        "advanced_rate": p["advanced_rate"],
        "rates": p["rates"],
    }


def load_config() -> dict:
    path = app_dir() / CONFIG_FILE
    if not path.exists():
        return DEFAULT_CONFIG.copy()
    try:
        return deep_merge(DEFAULT_CONFIG, json.loads(path.read_text(encoding="utf-8")))
    except Exception:
        return DEFAULT_CONFIG.copy()


def save_config(cfg: dict) -> None:
    (app_dir() / CONFIG_FILE).write_text(json.dumps(cfg, ensure_ascii=False, indent=2), encoding="utf-8")


def load_presets() -> dict:
    path = app_dir() / PRESET_FILE
    if not path.exists():
        path.write_text(json.dumps(DEFAULT_PRESETS, ensure_ascii=False, indent=2), encoding="utf-8")
        return DEFAULT_PRESETS.copy()
    try:
        loaded = json.loads(path.read_text(encoding="utf-8"))
        presets = DEFAULT_PRESETS.copy()
        presets.update(loaded)
        return {k: normalize_preset(v) for k, v in presets.items()}
    except Exception:
        return DEFAULT_PRESETS.copy()


def save_presets(presets: dict) -> None:
    clean = {k: normalize_preset(v) for k, v in presets.items()}
    (app_dir() / PRESET_FILE).write_text(json.dumps(clean, ensure_ascii=False, indent=2), encoding="utf-8")


def checked(value: str) -> bool:
    return str(value or "").strip().lower() in {"x", "1", "✓", "true", "yes", "y", "v"}


def silent(value) -> bool:
    return str(value or "").strip() in {"", "."}


def safe_name(name: str) -> str:
    return "".join("_" if c in '<>:"/\\|?*' else c for c in str(name)).strip() or "output"


def find_header_row(lines):
    for i, line in enumerate(lines):
        low = line.lower()
        if ("mand kw" in low or "hanzi" in low) and "mandarin" in low and "english" in low:
            return i
    return 0


def read_rows(path: Path, rows_mode: str):
    raw = Path(path).read_text(encoding="utf-8-sig", errors="replace").splitlines()
    if not raw:
        return []
    start = find_header_row(raw)
    sample = "\n".join(raw[start:start + 10])
    try:
        dialect = csv.Sniffer().sniff(sample, delimiters=",;\t")
    except Exception:
        dialect = csv.excel

    rows = []
    for row in csv.DictReader(raw[start:], dialect=dialect):
        if row is None:
            continue
        normalized = {str(k).strip(): v for k, v in row.items() if k is not None}
        for old, new in ALIASES.items():
            if old in normalized and new not in normalized:
                normalized[new] = normalized[old]
        if rows_mode == "checked" and not checked(normalized.get("Pilih", "")):
            continue
        rows.append(normalized)
    return rows


def read_rows_numbered(path: Path, rows_mode: str):
    """Return (visible row identifier, normalized row). Identifier is the raw "No" column value
    (e.g. "1a", "1b", "10i"), not parsed as an int, so letter-suffixed identifiers survive as-is.
    This keeps generated names aligned with the HTML table, e.g. 010_1a_mandarin.mp3.
    Falls back to the physical CSV row position only when "No" is blank.
    """
    raw = Path(path).read_text(encoding="utf-8-sig", errors="replace").splitlines()
    if not raw:
        return []
    start = find_header_row(raw)
    sample = "\n".join(raw[start:start + 10])
    try:
        dialect = csv.Sniffer().sniff(sample, delimiters=",;\t")
    except Exception:
        dialect = csv.excel

    result = []
    for data_index, row in enumerate(csv.DictReader(raw[start:], dialect=dialect), start=1):
        if row is None:
            continue
        normalized = {str(k).strip(): v for k, v in row.items() if k is not None}
        for old, new in ALIASES.items():
            if old in normalized and new not in normalized:
                normalized[new] = normalized[old]
        if rows_mode == "checked" and not checked(normalized.get("Pilih", "")):
            continue
        raw_no = str(normalized.get("No", "")).strip()
        row_no = safe_name(raw_no) if raw_no else str(data_index)
        result.append((row_no, normalized))
    return result


def text_prefix_from_file(path: Path) -> str:
    m = re.match(r"^\D*(\d{3})", Path(path).stem)
    if m:
        return m.group(1)
    cleaned = re.sub(r"[^A-Za-z0-9]+", "_", Path(path).stem).strip("_")
    return cleaned[:20] or "text"


def library_output_dir_for(file_path: Path, cfg: dict) -> Path:
    out_dir = Path(cfg["output_folder"])
    if not out_dir.is_absolute():
        out_dir = app_dir() / out_dir
    # MP3 per cell output folder must match the HTML sheet name / text file name.
    # Parent output folder may be anything; subfolder is the text filename without .csv/.txt.
    # Sits under "Per Cell MP3" so it's a sibling of "Per Cell ZIP" (library_zip_output_dir),
    # not mixed in at the output_folder root.
    folder_name = safe_name(Path(file_path).stem)
    return out_dir / "Per Cell MP3" / folder_name

def cleanTitleForFolder(name: str) -> str:
    return safe_name(re.sub(r"^\D*\d{3}[_ -]*", "", str(name)).strip())[:40] or "Text"


def library_filename(file_path: Path, row_no: str, key: str) -> str:
    prefix = text_prefix_from_file(file_path)
    return f"{prefix}_{row_no}_{key}.mp3"


def selected_library_keys(cfg: dict):
    cols = cfg.get("library_columns") or {}
    keys = [key for key, _label, _src in LIBRARY_COLUMNS if cols.get(key, True)]
    return keys


def read_rows_with_ids(path: Path, rows_mode: str):
    """Return (stable row id, row) so one merged random order can be reused by every preset."""
    all_rows = read_rows(path, "all")
    result = []
    path_key = str(Path(path).resolve())
    for original_index, row in enumerate(all_rows):
        if rows_mode == "checked" and not checked(row.get("Pilih", "")):
            continue
        result.append(((path_key, original_index), row))
    return result


def active_rows(rows, cfg):
    active = []
    for row in rows:
        values = [row.get(label, "") for label in cfg["sequence"] if label != "Diam"]
        if values and not all(silent(v) for v in values):
            active.append(row)
    return active


def estimate_text_seconds(text, col, speed):
    if silent(text):
        return 0.0
    text = str(text).strip()
    speed = max(0.4, float(speed or 1.0))
    lang = LANG_BY_COLUMN.get(col, "zh")
    if lang == "zh":
        units = max(1, len(text.replace(" ", "")))
        return max(0.8, units / 3.2) / speed
    words = max(1, len(text.split()))
    return max(0.8, words / 2.4) / speed


def format_seconds(sec):
    sec = int(round(sec))
    h, rem = divmod(sec, 3600)
    m, s = divmod(rem, 60)
    if h:
        return f"{h} jam {m} menit {s} detik"
    if m:
        return f"{m} menit {s} detik"
    return f"{s} detik"


def output_path_for(file_path: Path, preset_name: str, cfg: dict) -> Path:
    out_dir = Path(cfg["output_folder"])
    if not out_dir.is_absolute():
        out_dir = app_dir() / out_dir
    return out_dir / f"{safe_name(file_path.stem)}_{safe_name(preset_name)}.mp3"


def merged_output_path(first_file: Path, last_file: Path, preset_name: str, cfg: dict) -> Path:
    out_dir = Path(cfg["output_folder"])
    if not out_dir.is_absolute():
        out_dir = app_dir() / out_dir

    first_stem = first_file.stem
    last_stem = last_file.stem
    first_match = re.match(r"^(\d{3})(.*)$", first_stem)
    last_match = re.match(r"^(\d{3})", last_stem)

    if first_match and last_match:
        first_number = first_match.group(1)
        last_number = last_match.group(1)
        first_suffix = first_match.group(2)
        merged_name = f"Merge {first_number}-{last_number}{first_suffix}+{preset_name}"
    else:
        merged_name = f"Merge {first_stem}-{last_stem}+{preset_name}"

    return out_dir / f"{safe_name(merged_name)}.mp3"


def collect_stats(files, preset_names, presets, global_cfg):
    total_seconds = 0.0
    skipped_existing = 0
    total_rows = 0
    active_rows_count = 0
    audio_by_lang = {"zh": 0, "en": 0, "id": 0}
    merge_files = bool(global_cfg.get("merge_files", False) and len(files) > 1)
    total_outputs = len(preset_names) if merge_files else len(preset_names) * len(files)

    for preset_name in preset_names:
        cfg = build_cfg_for_preset(preset_name, presets, global_cfg)
        preset_skipped = False
        if merge_files:
            out_file = merged_output_path(Path(files[0]), Path(files[-1]), preset_name, cfg)
            preset_skipped = bool(cfg.get("skip_existing", True) and out_file.exists())
            if preset_skipped:
                skipped_existing += 1

        for f in files:
            f = Path(f)
            if not merge_files:
                out_file = output_path_for(f, preset_name, cfg)
                if cfg.get("skip_existing", True) and out_file.exists():
                    skipped_existing += 1
                    continue
            elif preset_skipped:
                continue

            rows = read_rows(f, cfg["rows"])
            active = active_rows(rows, cfg)
            total_rows += len(rows)
            active_rows_count += len(active)

            for row in active:
                for i, label in enumerate(cfg["sequence"]):
                    if label == "Diam":
                        continue
                    value = row.get(label, "")
                    if not silent(value):
                        lang = LANG_BY_COLUMN.get(label, "zh")
                        audio_by_lang[lang] = audio_by_lang.get(lang, 0) + 1
                        total_seconds += estimate_text_seconds(value, label, cfg.get("global_tts_speed", "1.0"))
                    delay = int(cfg["delay_after_ms"][i]) if i < len(cfg["delay_after_ms"]) else 0
                    total_seconds += max(0, delay) / 1000

            if active and not merge_files:
                total_seconds += 12

        if merge_files and not preset_skipped:
            any_active = any(active_rows(read_rows(Path(f), cfg["rows"]), cfg) for f in files)
            if any_active:
                total_seconds += 12

    approx_mb = total_seconds * 0.015
    return {
        "seconds": total_seconds,
        "outputs": total_outputs,
        "skipped_existing": skipped_existing,
        "will_generate": total_outputs - skipped_existing,
        "total_rows": total_rows,
        "active_rows": active_rows_count,
        "audio_by_lang": audio_by_lang,
        "audio_total": sum(audio_by_lang.values()),
        "approx_mb": approx_mb,
        "merge_files": merge_files,
    }


def atempo_filter(speed):
    speed = max(0.25, min(float(speed), 4.0))
    parts = []
    while speed < 0.5:
        parts.append("atempo=0.5")
        speed /= 0.5
    while speed > 2.0:
        parts.append("atempo=2.0")
        speed /= 2.0
    parts.append(f"atempo={speed:.4f}")
    return ",".join(parts)


async def make_tts(text, voice, rate, pitch, speed, out_file):
    if silent(text):
        return False
    speed = float(speed or 1.0)

    if abs(speed - 1.0) < 0.001:
        await edge_tts.Communicate(text=str(text), voice=voice, rate=rate, pitch=pitch).save(str(out_file))
        return True

    raw_file = out_file.with_suffix(".raw.mp3")
    await edge_tts.Communicate(text=str(text), voice=voice, rate=rate, pitch=pitch).save(str(raw_file))
    run_hidden(
        ["ffmpeg", "-y", "-i", str(raw_file), "-filter:a", atempo_filter(speed), "-vn", str(out_file)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=True,
    )
    try:
        raw_file.unlink()
    except Exception:
        pass
    return True


def make_silence(ms, out_file):
    if int(ms or 0) <= 0:
        return False
    run_hidden(
        [
            "ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono",
            "-t", str(int(ms) / 1000), "-q:a", "9", "-acodec", "libmp3lame", str(out_file)
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=True,
    )
    return True


def concat_mp3(parts, out_file):
    out_file.parent.mkdir(parents=True, exist_ok=True)
    list_file = out_file.parent / "_concat_list.txt"
    with list_file.open("w", encoding="utf-8") as f:
        for part in parts:
            f.write(f"file '{part.resolve().as_posix()}'\n")
    run_hidden(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(list_file), "-c", "copy", str(out_file)], check=True)
    try:
        list_file.unlink()
    except Exception:
        pass


def build_cfg_for_preset(preset_name, presets, global_cfg):
    preset = normalize_preset(presets[preset_name])
    cfg = deep_merge(DEFAULT_CONFIG, preset)
    cfg["output_folder"] = global_cfg["output_folder"]
    cfg["last_input_folder"] = global_cfg.get("last_input_folder", "")
    cfg["auto_open_output"] = global_cfg.get("auto_open_output", True)
    cfg["skip_existing"] = global_cfg.get("skip_existing", True)
    cfg["merge_files"] = global_cfg.get("merge_files", False)
    cfg["random_per_file"] = bool(preset.get("random_per_file", preset.get("random", False)))
    cfg["random_merge_file"] = bool(preset.get("random_merge_file", False))
    cfg["random"] = cfg["random_per_file"]
    cfg["voices"] = DEFAULT_CONFIG["voices"].copy()
    cfg["pitch"] = DEFAULT_CONFIG["pitch"].copy()
    cfg["final_delay_ms"] = 10000
    cfg["last_active_preset"] = preset_name
    return cfg


async def generate_one(file_path, preset_name, cfg, log, progress, stop_event, preset_index, preset_count, file_index, file_count, base_done, total_units):
    file_path = Path(file_path)
    out_file = output_path_for(file_path, preset_name, cfg)

    rows = active_rows(read_rows(file_path, cfg["rows"]), cfg)
    if cfg.get("random_per_file", cfg.get("random", False)):
        random.shuffle(rows)

    if cfg.get("skip_existing", True) and out_file.exists():
        log(f"SKIP EXISTING: {out_file.name}\n")
        progress(base_done + len(rows), total_units, f"Preset {preset_index}/{preset_count} | File {file_index}/{file_count} | skipped existing")
        return None, len(rows)

    if not rows:
        log(f"SKIP {file_path.name} / {preset_name}: tidak ada baris aktif\n")
        return None, 0

    rates = cfg["rates"] if cfg.get("advanced_rate") else {"zh": "+0%", "en": "+0%", "id": "+0%"}
    parts = []
    counter = 0
    processed_rows = 0

    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        for row_index, row in enumerate(rows, start=1):
            if stop_event.is_set():
                break

            for seq_index, col in [(i, v) for i, v in enumerate(cfg["sequence"]) if v != "Diam"]:
                if stop_event.is_set():
                    break
                value = row.get(col, "")
                lang = LANG_BY_COLUMN.get(col, "zh")

                if not silent(value):
                    counter += 1
                    audio_file = tmp / f"{counter:06d}_{row_index:04d}_{safe_name(col)}.mp3"
                    log(f"[Preset {preset_index}/{preset_count}] [{preset_name}] [File {file_index}/{file_count}] [{file_path.name}] Row {row_index}/{len(rows)} | {col}: {value}\n")
                    ok = await make_tts(
                        value,
                        cfg["voices"].get(lang, cfg["voices"]["zh"]),
                        rates.get(lang, "+0%"),
                        cfg["pitch"].get(lang, "+0Hz"),
                        cfg["global_tts_speed"],
                        audio_file,
                    )
                    if ok:
                        parts.append(audio_file)
                else:
                    log(f"[{preset_name}] [{file_path.name}] Row {row_index}/{len(rows)} | {col}: silent\n")

                delay = int(cfg["delay_after_ms"][seq_index]) if seq_index < len(cfg["delay_after_ms"]) else 0
                if delay > 0:
                    counter += 1
                    silent_file = tmp / f"{counter:06d}_silence_{delay}.mp3"
                    if make_silence(delay, silent_file):
                        parts.append(silent_file)

            processed_rows += 1
            progress(base_done + processed_rows, total_units, f"Preset {preset_index}/{preset_count} | File {file_index}/{file_count} | Row {row_index}/{len(rows)}")

        if parts and not stop_event.is_set():
            counter += 1
            final_silence = tmp / f"{counter:06d}_final_10000.mp3"
            make_silence(10000, final_silence)
            parts.append(final_silence)

        if not parts or stop_event.is_set():
            log(f"Generate dihentikan / tidak ada audio: {file_path.name} / {preset_name}\n")
            return None, processed_rows

        log(f"Menggabungkan: {out_file.name}\n")
        concat_mp3(parts, out_file)

    log(f"SELESAI: {out_file}\n\n")
    return out_file, processed_rows


async def generate_merged(files, preset_name, cfg, log, progress, stop_event, preset_index, preset_count, base_done, total_units, merged_random_rank=None):
    first_file = Path(files[0])
    last_file = Path(files[-1])
    out_file = merged_output_path(first_file, last_file, preset_name, cfg)

    rows_by_file = []
    total_rows = 0
    tagged_all = []
    for f in files:
        tagged = [(row_id, row) for row_id, row in read_rows_with_ids(Path(f), cfg["rows"]) if row in active_rows([row], cfg)]
        if cfg.get("random_per_file", cfg.get("random", False)):
            random.shuffle(tagged)
        rows_by_file.append((Path(f), tagged))
        tagged_all.extend((Path(f), row_id, row) for row_id, row in tagged)
        total_rows += len(tagged)

    if cfg.get("random_merge_file", False):
        # Randomize the complete merged pool once, without replacement.
        # Then remove duplicate spoken rows (including duplicates caused by
        # adding the same CSV more than once or identical rows across files).
        if merged_random_rank is None:
            random.shuffle(tagged_all)
        else:
            tagged_all.sort(key=lambda item: merged_random_rank.get(item[1], 10**12))

        unique_tagged = []
        seen_spoken_rows = set()
        spoken_columns = [col for col in cfg["sequence"] if col != "Diam"]
        for item in tagged_all:
            row = item[2]
            signature = tuple(
                " ".join(str(row.get(col, "")).strip().split()).casefold()
                for col in spoken_columns
            )
            if signature in seen_spoken_rows:
                continue
            seen_spoken_rows.add(signature)
            unique_tagged.append(item)

        removed_duplicates = len(tagged_all) - len(unique_tagged)
        if removed_duplicates:
            log(f"Random Merge: {removed_duplicates} baris duplikat dilewati agar tidak berulang.\n")
        tagged_all = unique_tagged
        total_rows = len(tagged_all)
        rows_by_file = [(None, tagged_all)]

    if cfg.get("skip_existing", True) and out_file.exists():
        log(f"SKIP EXISTING: {out_file.name}\n")
        progress(base_done + total_rows, total_units, f"Preset {preset_index}/{preset_count} | merged | skipped existing")
        return None, total_rows

    if total_rows == 0:
        log(f"SKIP MERGE / {preset_name}: tidak ada baris aktif\n")
        return None, 0

    rates = cfg["rates"] if cfg.get("advanced_rate") else {"zh": "+0%", "en": "+0%", "id": "+0%"}
    parts = []
    counter = 0
    processed_rows = 0

    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        for file_index, (file_path, rows) in enumerate(rows_by_file, start=1):
            for row_index, item in enumerate(rows, start=1):
                if cfg.get("random_merge_file", False):
                    source_path, _row_id, row = item
                else:
                    _row_id, row = item
                    source_path = file_path
                if stop_event.is_set():
                    break

                for seq_index, col in [(i, v) for i, v in enumerate(cfg["sequence"]) if v != "Diam"]:
                    if stop_event.is_set():
                        break
                    value = row.get(col, "")
                    lang = LANG_BY_COLUMN.get(col, "zh")

                    if not silent(value):
                        counter += 1
                        audio_file = tmp / f"{counter:06d}_{file_index:03d}_{row_index:04d}_{safe_name(col)}.mp3"
                        log(f"[Preset {preset_index}/{preset_count}] [{preset_name}] [Merge] [{source_path.name}] Row {processed_rows + 1}/{total_rows} | {col}: {value}\n")
                        ok = await make_tts(
                            value,
                            cfg["voices"].get(lang, cfg["voices"]["zh"]),
                            rates.get(lang, "+0%"),
                            cfg["pitch"].get(lang, "+0Hz"),
                            cfg["global_tts_speed"],
                            audio_file,
                        )
                        if ok:
                            parts.append(audio_file)
                    else:
                        log(f"[{preset_name}] [{source_path.name}] Row {processed_rows + 1}/{total_rows} | {col}: silent\n")

                    delay = int(cfg["delay_after_ms"][seq_index]) if seq_index < len(cfg["delay_after_ms"]) else 0
                    if delay > 0:
                        counter += 1
                        silent_file = tmp / f"{counter:06d}_silence_{delay}.mp3"
                        if make_silence(delay, silent_file):
                            parts.append(silent_file)

                processed_rows += 1
                progress(base_done + processed_rows, total_units, f"Preset {preset_index}/{preset_count} | Merge | Row {processed_rows}/{total_rows}")

            if stop_event.is_set():
                break

        if parts and not stop_event.is_set():
            counter += 1
            final_silence = tmp / f"{counter:06d}_final_10000.mp3"
            make_silence(10000, final_silence)
            parts.append(final_silence)

        if not parts or stop_event.is_set():
            log(f"Generate merge dihentikan / tidak ada audio: {preset_name}\n")
            return None, processed_rows

        log(f"Menggabungkan semua CSV: {out_file.name}\n")
        concat_mp3(parts, out_file)

    log(f"SELESAI MERGE: {out_file}\n\n")
    return out_file, processed_rows


async def generate_all(files, preset_names, presets, global_cfg, log, progress, stop_event):
    total_units = 0
    active_counts = {}
    merge_files = bool(global_cfg.get("merge_files", False) and len(files) > 1)

    for preset_name in preset_names:
        cfg = build_cfg_for_preset(preset_name, presets, global_cfg)
        for f in files:
            rows_count = len(active_rows(read_rows(Path(f), cfg["rows"]), cfg))
            active_counts[(preset_name, f)] = rows_count
            total_units += rows_count
    total_units = max(1, total_units)

    done_before = 0
    outputs = []
    preset_count = len(preset_names)
    file_count = len(files)

    # Build one random order once and reuse it for all selected presets.
    merged_random_rank = None
    if merge_files and any(normalize_preset(presets[name]).get("random_merge_file", False) for name in preset_names):
        all_row_ids = []
        for f in files:
            all_row_ids.extend(row_id for row_id, _row in read_rows_with_ids(Path(f), "all"))
        random.shuffle(all_row_ids)
        merged_random_rank = {row_id: index for index, row_id in enumerate(all_row_ids)}

    for p_index, preset_name in enumerate(preset_names, start=1):
        cfg = build_cfg_for_preset(preset_name, presets, global_cfg)
        if merge_files:
            out, processed = await generate_merged(
                files, preset_name, cfg, log, progress, stop_event,
                p_index, preset_count, done_before, total_units, merged_random_rank
            )
            done_before += sum(active_counts[(preset_name, f)] for f in files)
            if out:
                outputs.append(out)
        else:
            for f_index, f in enumerate(files, start=1):
                if stop_event.is_set():
                    break
                out, processed = await generate_one(
                    f, preset_name, cfg, log, progress, stop_event,
                    p_index, preset_count, f_index, file_count, done_before, total_units
                )
                done_before += active_counts[(preset_name, f)]
                if out:
                    outputs.append(out)
        if stop_event.is_set():
            break

    log("=== RINGKASAN ===\n")
    for out in outputs:
        log(str(out) + "\n")
    log(f"Total MP3 dibuat: {len(outputs)}\n")
    return outputs



def collect_library_stats(files, cfg):
    keys = selected_library_keys(cfg)
    total_rows = 0
    audio_total = 0
    skipped = 0
    empty = 0
    seconds = 0.0
    for f in files:
        f = Path(f)
        out_dir = library_output_dir_for(f, cfg)
        numbered = read_rows_numbered(f, cfg.get("rows", "all"))
        total_rows += len(numbered)
        for row_no, row in numbered:
            for key, _label, src in LIBRARY_COLUMNS:
                if key not in keys:
                    continue
                text = row.get(src, "")
                if silent(text):
                    empty += 1
                    continue
                audio_total += 1
                out_file = out_dir / library_filename(f, row_no, key)
                if cfg.get("skip_existing", True) and out_file.exists() and out_file.stat().st_size > 0:
                    skipped += 1
                    continue
                seconds += estimate_text_seconds(text, src, cfg.get("global_tts_speed", "1.0"))
    return {
        "files": len(files),
        "rows": total_rows,
        "columns": len(keys),
        "audio_total": audio_total,
        "skipped_existing": skipped,
        "will_generate": max(0, audio_total - skipped),
        "empty": empty,
        "seconds": seconds,
        "approx_mb": seconds * 0.015,
    }


async def generate_library_all(files, cfg, log, progress, stop_event):
    keys = selected_library_keys(cfg)
    if not keys:
        log("Tidak ada kolom MP3 per cell yang dipilih.\n")
        return []

    total_units = 0
    for f in files:
        for _row_no, row in read_rows_numbered(Path(f), cfg.get("rows", "all")):
            for key, _label, src in LIBRARY_COLUMNS:
                if key in keys and not silent(row.get(src, "")):
                    total_units += 1
    total_units = max(1, total_units)

    done = 0
    made = []
    rates = cfg["rates"] if cfg.get("advanced_rate") else {"zh": "+0%", "en": "+0%", "id": "+0%"}

    for file_index, f in enumerate(files, start=1):
        if stop_event.is_set():
            break
        f = Path(f)
        prefix = text_prefix_from_file(f)
        out_dir = library_output_dir_for(f, cfg)
        out_dir.mkdir(parents=True, exist_ok=True)
        manifest_rows = []
        numbered = read_rows_numbered(f, cfg.get("rows", "all"))
        log(f"[MP3 per cell] File {file_index}/{len(files)}: {f.name} -> folder {out_dir.name}\n")

        for row_pos, (row_no, row) in enumerate(numbered, start=1):
            if stop_event.is_set():
                break
            for key, label, src in LIBRARY_COLUMNS:
                if key not in keys:
                    continue
                text = row.get(src, "")
                filename = library_filename(f, row_no, key)
                out_file = out_dir / filename
                manifest_rows.append([row_no, key, filename, text])
                if silent(text):
                    log(f"[MP3 per cell] {filename}: cell kosong, dilewati\n")
                    continue
                if cfg.get("skip_existing", True) and out_file.exists() and out_file.stat().st_size > 0:
                    done += 1
                    progress(done, total_units, f"MP3 per cell {file_index}/{len(files)} | {filename} | skipped")
                    continue
                lang = LANG_BY_COLUMN.get(src, "zh")
                log(f"[MP3 per cell] {filename} | {label}: {text}\n")
                await make_tts(
                    text,
                    cfg["voices"].get(lang, cfg["voices"]["zh"]),
                    rates.get(lang, "+0%"),
                    cfg["pitch"].get(lang, "+0Hz"),
                    cfg.get("global_tts_speed", "1.0"),
                    out_file,
                )
                made.append(out_file)
                done += 1
                progress(done, total_units, f"MP3 per cell {file_index}/{len(files)} | Row {row_no} | {label}")

        manifest_path = out_dir / f"{prefix}_manifest.csv"
        with manifest_path.open("w", encoding="utf-8-sig", newline="") as mf:
            writer = csv.writer(mf, delimiter=";")
            writer.writerow(["row", "column", "filename", "text"])
            writer.writerows(manifest_rows)
        log(f"[MP3 per cell] Manifest: {manifest_path}\n\n")

    log("=== RINGKASAN MP3 PER CELL ===\n")
    log(f"Total MP3 dibuat: {len(made)}\n")
    return made


def library_zip_output_dir(cfg: dict) -> Path:
    out_dir = Path(cfg["output_folder"])
    if not out_dir.is_absolute():
        out_dir = app_dir() / out_dir
    return out_dir / "Per Cell ZIP"


def mp3_files_for_text_folder(folder: Path):
    if not folder.exists():
        return []
    return sorted([p for p in folder.glob("*.mp3") if p.is_file()])


def zip_name_for_all(files):
    if not files:
        return "MP3_Cell_All.zip"
    first = text_prefix_from_file(Path(files[0]))
    last = text_prefix_from_file(Path(files[-1]))
    if first == last:
        return f"MP3_Cell_{first}.zip"
    return f"MP3_Cell_{first}-{last}.zip"


def create_library_zips(files, cfg, log):
    """Create ZIP files for HTML ZIP mode.

    Safe behavior v3.7:
    - ZIP dibuat dari MP3 yang sudah ada di folder output.
    - Jadi kalau MP3 sudah selesai/skip existing, ZIP tetap bisa dibuat.
    - Log dibuat lebih jelas agar terlihat proses ZIP benar-benar berjalan.
    """
    log("\nMulai membuat ZIP dari folder MP3 yang sudah ada...\n")
    """Create ZIP files for HTML ZIP mode.

    ZIP entries keep the internal structure:
      001 Text/001_r001_mandkw.mp3
      002 Text/002_r001_mandarin.mp3

    MP3 is already compressed, so ZIP_STORED is used. This is faster, avoids
    unnecessary recompression, and is easier for browser-side ZIP readers.
    """
    outputs = []
    if not (cfg.get("zip_per_text") or cfg.get("zip_all")):
        return outputs

    zip_dir = library_zip_output_dir(cfg)
    zip_dir.mkdir(parents=True, exist_ok=True)

    text_folders = []
    for f in files:
        f = Path(f)
        folder = library_output_dir_for(f, cfg)
        sheet_name = safe_name(f.stem)
        mp3s = mp3_files_for_text_folder(folder)
        text_folders.append((sheet_name, folder, mp3s))

    if cfg.get("zip_per_text"):
        log("\n=== ZIP PER TEXT ===\n")
        for sheet_name, folder, mp3s in text_folders:
            if not mp3s:
                log(f"[ZIP per Text] {sheet_name}: tidak ada MP3, dilewati\n")
                continue
            zip_path = zip_dir / f"{safe_name(sheet_name)}.zip"
            with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_STORED) as zf:
                for mp3 in mp3s:
                    zf.write(mp3, arcname=f"{sheet_name}/{mp3.name}")
            outputs.append(zip_path)
            log(f"[ZIP per Text] {zip_path.name}: {len(mp3s)} MP3\n")

    if cfg.get("zip_all"):
        log("\n=== ZIP ALL / MERGE SELECTED ===\n")
        zip_path = zip_dir / zip_name_for_all(files)
        total = 0
        with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_STORED) as zf:
            for sheet_name, folder, mp3s in text_folders:
                for mp3 in mp3s:
                    zf.write(mp3, arcname=f"{sheet_name}/{mp3.name}")
                    total += 1
        if total:
            outputs.append(zip_path)
            log(f"[ZIP All] {zip_path.name}: {total} MP3\n")
        else:
            try:
                zip_path.unlink(missing_ok=True)
            except Exception:
                pass
            log("[ZIP All] tidak ada MP3, ZIP tidak dibuat\n")

    return outputs



class App:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_TITLE)
        self.root.geometry("1180x720")
        self.root.minsize(980, 650)

        self.cfg = load_config()
        self.presets = load_presets()
        self.files = []
        self.preset_vars = {}
        self.active_preset_name = self.cfg.get("last_active_preset", "Listening")
        self.q = queue.Queue()
        self.stop_event = threading.Event()
        self.running = False
        self.advanced_visible = False

        self.build_ui()
        self.refresh_preset_list()
        self.apply_preset_to_ui(self.active_preset_name)
        self.apply_global_config()
        self.update_rate_state()
        self.toggle_advanced(force_hide=True)
        self.poll_queue()

    def build_ui(self):
        # v3.2 UI FIX:
        # Left side redesigned so preset buttons are compact, Action always visible,
        # Advanced Rate stays attached to its toggle, and laptop screens can use the app comfortably.
        header = ttk.Frame(self.root)
        header.pack(fill="x", padx=10, pady=(6, 3))
        ttk.Label(header, text=APP_TITLE, font=("Segoe UI", 14, "bold")).pack(side="left")

        main = ttk.PanedWindow(self.root, orient="horizontal")
        main.pack(fill="both", expand=True, padx=8, pady=(0, 8))

        left_outer = ttk.Frame(main)
        right = ttk.Frame(main)
        main.add(left_outer, weight=1)
        main.add(right, weight=2)

        # Action fixed at bottom, always visible.
        self.left_action_bar = ttk.LabelFrame(left_outer, text="Action")
        self.left_action_bar.pack(side="bottom", fill="x", pady=(6, 0))

        # Scrollable settings above Action.
        left_canvas = tk.Canvas(left_outer, highlightthickness=0)
        left_scrollbar = ttk.Scrollbar(left_outer, orient="vertical", command=left_canvas.yview)
        left = ttk.Frame(left_canvas)
        left_window = left_canvas.create_window((0, 0), window=left, anchor="nw")
        left.bind("<Configure>", lambda e: left_canvas.configure(scrollregion=left_canvas.bbox("all")))
        left_canvas.bind("<Configure>", lambda e: left_canvas.itemconfigure(left_window, width=e.width))
        left_canvas.configure(yscrollcommand=left_scrollbar.set)
        left_canvas.pack(side="left", fill="both", expand=True)
        left_scrollbar.pack(side="right", fill="y")

        # Preset area: list on left, small preset action buttons on right.
        preset_frame = ttk.LabelFrame(left, text="Preset")
        preset_frame.pack(fill="x", pady=(0, 6))

        preset_body = ttk.Frame(preset_frame)
        preset_body.pack(fill="x", padx=5, pady=5)

        # Keep the preset controls visible even when the left pane is narrowed:
        # the preset list stays on top and all action buttons sit below it.
        preset_list_box = ttk.Frame(preset_body)
        preset_list_box.pack(fill="both", expand=True)

        preset_canvas = tk.Canvas(preset_list_box, height=115, highlightthickness=0)
        preset_scroll = ttk.Scrollbar(preset_list_box, orient="vertical", command=preset_canvas.yview)
        self.preset_inner = ttk.Frame(preset_canvas)
        preset_window = preset_canvas.create_window((0, 0), window=self.preset_inner, anchor="nw")
        self.preset_inner.bind("<Configure>", lambda e: preset_canvas.configure(scrollregion=preset_canvas.bbox("all")))
        preset_canvas.bind("<Configure>", lambda e: preset_canvas.itemconfigure(preset_window, width=e.width))
        preset_canvas.configure(yscrollcommand=preset_scroll.set)
        preset_canvas.pack(side="left", fill="both", expand=True)
        preset_scroll.pack(side="right", fill="y")

        preset_btns = ttk.Frame(preset_body)
        preset_btns.pack(fill="x", pady=(5, 0))
        for col in range(3):
            preset_btns.columnconfigure(col, weight=1, uniform="preset_actions")
        ttk.Button(preset_btns, text="Save As", command=self.save_as_preset).grid(row=0, column=0, sticky="ew", padx=2, pady=2)
        ttk.Button(preset_btns, text="Update", command=self.update_preset).grid(row=0, column=1, sticky="ew", padx=2, pady=2)
        ttk.Button(preset_btns, text="Rename", command=self.rename_preset).grid(row=0, column=2, sticky="ew", padx=2, pady=2)
        ttk.Button(preset_btns, text="Delete", command=self.delete_preset).grid(row=1, column=0, sticky="ew", padx=2, pady=2)
        ttk.Button(preset_btns, text="Import", command=self.import_presets).grid(row=1, column=1, sticky="ew", padx=2, pady=2)
        ttk.Button(preset_btns, text="Export", command=self.export_presets).grid(row=1, column=2, sticky="ew", padx=2, pady=2)

        settings_frame = ttk.LabelFrame(left, text="Basic Settings")
        settings_frame.pack(fill="x", pady=5)

        self.v_vars, self.delay_vars = [], []
        for i in range(4):
            ttk.Label(settings_frame, text=f"V{i+1}").grid(row=i, column=0, sticky="w", padx=6, pady=2)
            v = tk.StringVar()
            ttk.Combobox(settings_frame, textvariable=v, values=CHOICES, width=15, state="readonly").grid(row=i, column=1, sticky="ew", padx=4, pady=2)
            self.v_vars.append(v)

            delay_labels = ["Delay V2", "Delay V3", "Delay V4", "Delay Baris"]
            ttk.Label(settings_frame, text=delay_labels[i]).grid(row=i, column=2, sticky="w", padx=(8, 2), pady=2)
            d = tk.StringVar()
            ttk.Entry(settings_frame, textvariable=d, width=7).grid(row=i, column=3, sticky="w", padx=4, pady=2)
            self.delay_vars.append(d)

        self.rows_var = tk.StringVar()
        self.random_per_file_var = tk.BooleanVar()
        self.random_merge_file_var = tk.BooleanVar()
        ttk.Radiobutton(settings_frame, text="Semua", variable=self.rows_var, value="all").grid(row=4, column=0, sticky="w", padx=6, pady=3)
        ttk.Radiobutton(settings_frame, text="Centang", variable=self.rows_var, value="checked").grid(row=4, column=1, sticky="w", padx=4, pady=3)
        random_frame = ttk.Frame(settings_frame)
        random_frame.grid(row=4, column=2, columnspan=2, sticky="w", padx=4, pady=3)
        ttk.Checkbutton(random_frame, text="Random Per File", variable=self.random_per_file_var, command=self.on_random_per_file).pack(side="left")
        self.random_merge_check = ttk.Checkbutton(random_frame, text="Random Merge File", variable=self.random_merge_file_var, command=self.on_random_merge_file)
        self.random_merge_check.pack(side="left", padx=(10, 0))

        ttk.Label(settings_frame, text="Global Speed").grid(row=5, column=0, sticky="w", padx=6, pady=3)
        self.speed_var = tk.StringVar()
        ttk.Combobox(
            settings_frame,
            textvariable=self.speed_var,
            values=["0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0", "1.1", "1.2", "1.3", "1.4", "1.5", "1.6"],
            width=8,
            state="readonly",
        ).grid(row=5, column=1, sticky="w", padx=4, pady=3)
        settings_frame.columnconfigure(1, weight=1)

        # Advanced Rate: toggle and content kept together in one frame.
        self.advanced_container = ttk.LabelFrame(left, text="Advanced")
        self.advanced_container.pack(fill="x", pady=5)
        self.adv_toggle_btn = ttk.Button(self.advanced_container, text="▶ Advanced Rate", command=self.toggle_advanced)
        self.adv_toggle_btn.pack(fill="x", padx=5, pady=5)

        self.advanced_frame = ttk.Frame(self.advanced_container)
        self.advanced_rate_var = tk.BooleanVar()
        ttk.Checkbutton(self.advanced_frame, text="Enable Advanced Rate", variable=self.advanced_rate_var, command=self.update_rate_state).grid(row=0, column=0, columnspan=2, sticky="w", padx=6, pady=3)

        self.rate_zh, self.rate_en, self.rate_id = tk.StringVar(), tk.StringVar(), tk.StringVar()
        self.rate_widgets = []
        rate_values = ["-40%", "-30%", "-20%", "-10%", "+0%", "+10%", "+20%", "+30%", "+40%"]
        for idx, (label, var) in enumerate([("Mandarin", self.rate_zh), ("English", self.rate_en), ("Indonesia", self.rate_id)], start=1):
            ttk.Label(self.advanced_frame, text=label).grid(row=idx, column=0, sticky="w", padx=6, pady=2)
            cb = ttk.Combobox(self.advanced_frame, textvariable=var, values=rate_values, width=8, state="readonly")
            cb.grid(row=idx, column=1, sticky="w", padx=4, pady=2)
            self.rate_widgets.append(cb)

        output_frame = ttk.LabelFrame(left, text="Output")
        output_frame.pack(fill="x", pady=5)

        self.output_var = tk.StringVar()
        ttk.Entry(output_frame, textvariable=self.output_var).pack(fill="x", padx=6, pady=(5, 2))
        out_btns = ttk.Frame(output_frame)
        out_btns.pack(fill="x", padx=4, pady=(0, 5))
        ttk.Button(out_btns, text="Browse", width=9, command=self.choose_output).pack(side="left", padx=2)
        ttk.Button(out_btns, text="Open", width=9, command=self.open_output).pack(side="left", padx=2)
        self.auto_open_var = tk.BooleanVar()
        ttk.Checkbutton(out_btns, text="Auto open", variable=self.auto_open_var).pack(side="left", padx=6)
        self.skip_existing_var = tk.BooleanVar()
        ttk.Checkbutton(out_btns, text="Skip existing", variable=self.skip_existing_var).pack(side="left", padx=6)

        library_frame = ttk.LabelFrame(left, text="Generate Mode")
        library_frame.pack(fill="x", pady=5)
        self.generate_mode_var = tk.StringVar(value="long")
        ttk.Radiobutton(library_frame, text="MP3 per sheet", variable=self.generate_mode_var, value="long").grid(row=0, column=0, sticky="w", padx=6, pady=2)
        ttk.Radiobutton(library_frame, text="MP3 per cell", variable=self.generate_mode_var, value="library").grid(row=0, column=1, sticky="w", padx=6, pady=2)
        self.library_column_vars = {}
        self.library_column_widgets = []
        for idx, (key, label, _src) in enumerate(LIBRARY_COLUMNS):
            var = tk.BooleanVar(value=True)
            self.library_column_vars[key] = var
            cb = ttk.Checkbutton(library_frame, text=label, variable=var)
            cb.grid(row=1 + idx//3, column=idx%3, sticky="w", padx=6, pady=2)
            self.library_column_widgets.append(cb)
        self.zip_per_text_var = tk.BooleanVar()
        self.zip_all_var = tk.BooleanVar()
        self.zip_option_widgets = []
        self.zip_option_widgets.append(ttk.Checkbutton(library_frame, text="ZIP per Text", variable=self.zip_per_text_var))
        self.zip_option_widgets[-1].grid(row=3, column=0, sticky="w", padx=6, pady=(2,2))
        self.zip_option_widgets.append(ttk.Checkbutton(library_frame, text="ZIP All / Merge Selected", variable=self.zip_all_var))
        self.zip_option_widgets[-1].grid(row=3, column=1, columnspan=2, sticky="w", padx=6, pady=(2,2))
        ttk.Label(library_frame, text="MP3 per cell: output/Per Cell MP3/<nama sheet>. ZIP dibuat di output/Per Cell ZIP.").grid(row=4, column=0, columnspan=3, sticky="w", padx=6, pady=(2,5))
        self.generate_mode_var.trace_add("write", lambda *_: self.update_library_column_state())

        action_frame = self.left_action_bar
        ttk.Button(action_frame, text="Preview", command=self.preview_detail).pack(side="left", fill="x", expand=True, padx=4, pady=6)
        self.generate_button = ttk.Button(action_frame, text="GENERATE", command=self.start_generate)
        self.generate_button.pack(side="left", fill="x", expand=True, padx=4, pady=6)
        self.stop_button = ttk.Button(action_frame, text="STOP", command=self.stop_generate, state="disabled")
        self.stop_button.pack(side="left", fill="x", expand=True, padx=4, pady=6)
        ttk.Button(action_frame, text="Save", command=self.save_settings).pack(side="left", fill="x", expand=True, padx=4, pady=6)

        files_frame = ttk.LabelFrame(right, text="CSV Files")
        files_frame.pack(fill="both", expand=False, pady=(0, 6))

        file_btns = ttk.Frame(files_frame)
        file_btns.pack(fill="x", padx=6, pady=5)
        ttk.Button(file_btns, text="Tambah CSV", command=self.add_csv).pack(side="left", padx=3)
        ttk.Button(file_btns, text="Tambah Folder", command=self.add_folder).pack(side="left", padx=3)
        ttk.Button(file_btns, text="Remove Selected", command=self.remove_selected_file).pack(side="left", padx=3)
        ttk.Button(file_btns, text="Clear", command=self.clear_files).pack(side="left", padx=3)
        self.merge_files_var = tk.BooleanVar()
        ttk.Checkbutton(file_btns, text="Merge", variable=self.merge_files_var, command=self.on_merge_files_changed).pack(side="left", padx=(10, 3))

        file_list_frame = ttk.Frame(files_frame)
        file_list_frame.pack(fill="both", expand=True, padx=6, pady=(0, 6))
        self.file_list = tk.Listbox(file_list_frame, height=6)
        self.file_list.pack(side="left", fill="both", expand=True)
        file_scroll = ttk.Scrollbar(file_list_frame, orient="vertical", command=self.file_list.yview)
        file_scroll.pack(side="right", fill="y")
        self.file_list.config(yscrollcommand=file_scroll.set)

        progress_frame = ttk.LabelFrame(right, text="Progress")
        progress_frame.pack(fill="x", pady=5)

        self.progress = ttk.Progressbar(progress_frame, maximum=100)
        self.progress.pack(fill="x", padx=6, pady=(5, 2))
        row = ttk.Frame(progress_frame)
        row.pack(fill="x", padx=6, pady=(0, 5))
        self.progress_label = ttk.Label(row, text="0%")
        self.progress_label.pack(side="left")
        self.detail_label = ttk.Label(row, text="Ready")
        self.detail_label.pack(side="left", padx=12)

        log_frame = ttk.LabelFrame(right, text="Log")
        log_frame.pack(fill="both", expand=True, pady=(5, 0))

        log_btns = ttk.Frame(log_frame)
        log_btns.pack(fill="x", padx=6, pady=4)
        ttk.Button(log_btns, text="Clear Log", command=self.clear_log).pack(side="left", padx=3)
        ttk.Button(log_btns, text="Copy Log", command=self.copy_log).pack(side="left", padx=3)

        log_text_frame = ttk.Frame(log_frame)
        log_text_frame.pack(fill="both", expand=True, padx=6, pady=(0, 6))
        self.log_text = tk.Text(log_text_frame, height=28, wrap="word")
        self.log_text.pack(side="left", fill="both", expand=True)
        log_scroll = ttk.Scrollbar(log_text_frame, orient="vertical", command=self.log_text.yview)
        log_scroll.pack(side="right", fill="y")
        self.log_text.config(yscrollcommand=log_scroll.set)

    def on_random_per_file(self):
        if self.random_per_file_var.get():
            self.random_merge_file_var.set(False)

    def on_random_merge_file(self):
        if self.random_merge_file_var.get():
            self.random_per_file_var.set(False)

    def on_merge_files_changed(self):
        merge_enabled = bool(self.merge_files_var.get())
        self.random_merge_check.configure(state="normal" if merge_enabled else "disabled")
        if not merge_enabled:
            self.random_merge_file_var.set(False)

    def toggle_advanced(self, force_hide=False):
        if force_hide:
            self.advanced_visible = False
        else:
            self.advanced_visible = not self.advanced_visible
        if self.advanced_visible:
            self.advanced_frame.pack(fill="x", padx=5, pady=(0, 5))
            self.adv_toggle_btn.configure(text="▼ Advanced Rate")
        else:
            self.advanced_frame.pack_forget()
            self.adv_toggle_btn.configure(text="▶ Advanced Rate")

    def update_rate_state(self):
        state = "readonly" if self.advanced_rate_var.get() else "disabled"
        for widget in self.rate_widgets:
            widget.configure(state=state)

    def update_library_column_state(self):
        state = "normal" if getattr(self, "generate_mode_var", tk.StringVar(value="long")).get() == "library" else "disabled"
        for widget in getattr(self, "library_column_widgets", []):
            widget.configure(state=state)
        for widget in getattr(self, "zip_option_widgets", []):
            widget.configure(state=state)

    def selected_preset_names(self):
        return [name for name, var in self.preset_vars.items() if var.get()]

    def refresh_preset_list(self):
        for child in self.preset_inner.winfo_children():
            child.destroy()
        self.preset_vars = {}
        names = sorted(self.presets.keys())
        last = self.cfg.get("last_active_preset", "Listening")
        for row, name in enumerate(names):
            var = tk.BooleanVar(value=(name == last))
            self.preset_vars[name] = var
            cb = ttk.Checkbutton(self.preset_inner, variable=var)
            cb.grid(row=row, column=0, sticky="w", padx=(2, 0), pady=1)
            btn = ttk.Button(self.preset_inner, text=name, command=lambda n=name: self.activate_preset(n))
            btn.grid(row=row, column=1, sticky="ew", padx=2, pady=1)
        self.preset_inner.columnconfigure(1, weight=1)

    def activate_preset(self, name):
        if name not in self.presets:
            return
        self.active_preset_name = name
        self.preset_vars.setdefault(name, tk.BooleanVar()).set(True)
        self.apply_preset_to_ui(name)
        self.log(f"Preset loaded: {name}\n")

    def current_preset_payload(self):
        return {
            "sequence": [v.get() for v in self.v_vars],
            "delay_after_ms": [int(d.get() or 0) for d in self.delay_vars],
            "rows": self.rows_var.get(),
            "global_tts_speed": self.speed_var.get(),
            "random": bool(self.random_per_file_var.get()),  # compatibility
            "random_per_file": bool(self.random_per_file_var.get()),
            "random_merge_file": bool(self.random_merge_file_var.get()),
            "advanced_rate": bool(self.advanced_rate_var.get()),
            "rates": {"zh": self.rate_zh.get(), "en": self.rate_en.get(), "id": self.rate_id.get()},
        }

    def apply_preset_to_ui(self, name):
        preset = normalize_preset(self.presets.get(name, DEFAULT_PRESETS["Listening"]))
        for i in range(4):
            self.v_vars[i].set(preset["sequence"][i])
            self.delay_vars[i].set(str(preset["delay_after_ms"][i]))
        self.rows_var.set(preset.get("rows", "all"))
        self.random_per_file_var.set(bool(preset.get("random_per_file", preset.get("random", False))))
        self.random_merge_file_var.set(bool(preset.get("random_merge_file", False)))
        self.speed_var.set(str(preset.get("global_tts_speed", "1.0")))
        self.advanced_rate_var.set(bool(preset.get("advanced_rate", False)))
        rates = preset.get("rates", {"zh": "+0%", "en": "+0%", "id": "+0%"})
        self.rate_zh.set(rates.get("zh", "+0%"))
        self.rate_en.set(rates.get("en", "+0%"))
        self.rate_id.set(rates.get("id", "+0%"))
        self.update_rate_state()
        if hasattr(self, "random_merge_check"):
            self.on_merge_files_changed()

    def apply_global_config(self):
        out = self.cfg.get("output_folder", "output_mp3")
        if not Path(out).is_absolute():
            out = str(app_dir() / out)
        self.output_var.set(out)
        self.auto_open_var.set(bool(self.cfg.get("auto_open_output", True)))
        self.skip_existing_var.set(bool(self.cfg.get("skip_existing", True)))
        self.merge_files_var.set(bool(self.cfg.get("merge_files", False)))
        if hasattr(self, "generate_mode_var"):
            self.generate_mode_var.set(self.cfg.get("generate_mode", "long"))
        if hasattr(self, "library_column_vars"):
            cols = self.cfg.get("library_columns", DEFAULT_CONFIG.get("library_columns", {}))
            for key, var in self.library_column_vars.items():
                var.set(bool(cols.get(key, True)))
        if hasattr(self, "zip_per_text_var"):
            self.zip_per_text_var.set(bool(self.cfg.get("zip_per_text", False)))
        if hasattr(self, "zip_all_var"):
            self.zip_all_var.set(bool(self.cfg.get("zip_all", False)))
        self.on_merge_files_changed()
        if hasattr(self, "update_library_column_state"):
            self.update_library_column_state()

    def global_config(self):
        return {
            "output_folder": self.output_var.get(),
            "last_input_folder": str(Path(self.files[0]).parent) if self.files else self.cfg.get("last_input_folder", ""),
            "last_active_preset": self.active_preset_name,
            "auto_open_output": bool(self.auto_open_var.get()),
            "skip_existing": bool(self.skip_existing_var.get()),
            "merge_files": bool(self.merge_files_var.get()),
            "generate_mode": self.generate_mode_var.get() if hasattr(self, "generate_mode_var") else "long",
            "library_columns": {key: bool(var.get()) for key, var in getattr(self, "library_column_vars", {}).items()},
            "zip_per_text": bool(getattr(self, "zip_per_text_var", tk.BooleanVar(value=False)).get()),
            "zip_all": bool(getattr(self, "zip_all_var", tk.BooleanVar(value=False)).get()),
        }

    def full_config_for_save(self):
        cfg = deep_merge(DEFAULT_CONFIG, self.current_preset_payload())
        cfg.update(self.global_config())
        return cfg

    def save_settings(self):
        if self.active_preset_name in self.presets:
            self.presets[self.active_preset_name] = self.current_preset_payload()
            save_presets(self.presets)
        save_config(self.full_config_for_save())
        self.log("Setting + active preset tersimpan.\n")

    def save_as_preset(self):
        name = tkinter.simpledialog.askstring("Save Preset", "Nama preset baru:")
        if not name:
            return
        self.presets[name] = self.current_preset_payload()
        save_presets(self.presets)
        self.active_preset_name = name
        self.refresh_preset_list()
        self.preset_vars[name].set(True)
        self.log(f"Preset disimpan: {name}\n")

    def update_preset(self):
        name = self.active_preset_name
        if not name:
            return
        self.presets[name] = self.current_preset_payload()
        save_presets(self.presets)
        self.log(f"Preset diupdate: {name}\n")

    def rename_preset(self):
        old = self.active_preset_name
        if not old:
            return
        if old in SYSTEM_PRESETS:
            messagebox.showwarning("Preset sistem", "Preset bawaan tidak bisa di-rename. Gunakan Save As.")
            return
        new = tkinter.simpledialog.askstring("Rename Preset", "Nama baru:", initialvalue=old)
        if not new or new == old:
            return
        if new in self.presets:
            messagebox.showerror("Nama sudah ada", "Preset dengan nama itu sudah ada.")
            return
        self.presets[new] = self.presets.pop(old)
        save_presets(self.presets)
        self.active_preset_name = new
        self.refresh_preset_list()
        self.preset_vars[new].set(True)
        self.apply_preset_to_ui(new)
        self.log(f"Preset renamed: {old} -> {new}\n")

    def delete_preset(self):
        name = self.active_preset_name
        if not name:
            return
        if name in SYSTEM_PRESETS:
            messagebox.showwarning("Preset sistem", "Preset bawaan tidak bisa dihapus.")
            return
        if messagebox.askyesno("Delete Preset", f'Hapus preset "{name}"?'):
            self.presets.pop(name, None)
            save_presets(self.presets)
            self.active_preset_name = "Listening"
            self.refresh_preset_list()
            self.apply_preset_to_ui(self.active_preset_name)
            self.log(f"Preset deleted: {name}\n")

    def export_presets(self):
        path = filedialog.asksaveasfilename(
            title="Export Presets",
            defaultextension=".json",
            filetypes=[("JSON", "*.json")],
            initialfile="WTMandarin_presets.json",
        )
        if not path:
            return
        Path(path).write_text(json.dumps(self.presets, ensure_ascii=False, indent=2), encoding="utf-8")
        self.log(f"Presets exported: {path}\n")

    def import_presets(self):
        path = filedialog.askopenfilename(title="Import Presets", filetypes=[("JSON", "*.json")])
        if not path:
            return
        try:
            imported = json.loads(Path(path).read_text(encoding="utf-8"))
            for name, preset in imported.items():
                if isinstance(preset, dict):
                    self.presets[name] = normalize_preset(preset)
            save_presets(self.presets)
            self.refresh_preset_list()
            self.log(f"Presets imported: {path}\n")
        except Exception as e:
            messagebox.showerror("Import gagal", str(e))

    def add_file_path(self, path):
        path = str(Path(path).resolve())
        existing = {str(Path(p).resolve()) for p in self.files}
        if path not in existing:
            self.files.append(path)
            return True
        return False

    def add_csv(self):
        initial = self.cfg.get("last_input_folder", "")
        paths = filedialog.askopenfilenames(
            title="Pilih CSV / TXT",
            initialdir=initial if initial and Path(initial).exists() else None,
            filetypes=[("All Files", "*.*"), ("CSV/TXT", "*.csv *.txt"), ("CSV", "*.csv")],
        )
        added = 0
        for p in paths:
            if self.add_file_path(p):
                added += 1
        self.refresh_file_list()
        if paths:
            self.cfg["last_input_folder"] = str(Path(paths[0]).parent)
        if added < len(paths):
            self.log(f"Duplicate skipped: {len(paths) - added}\n")

    def add_folder(self):
        initial = self.cfg.get("last_input_folder", "")
        folder = filedialog.askdirectory(title="Pilih folder berisi CSV/TXT", initialdir=initial if initial and Path(initial).exists() else None)
        if not folder:
            return
        added = 0
        csvs = sorted(list(Path(folder).glob("*.csv")) + list(Path(folder).glob("*.txt")))
        for p in csvs:
            if self.add_file_path(p):
                added += 1
        self.cfg["last_input_folder"] = folder
        self.refresh_file_list()
        if added < len(csvs):
            self.log(f"Duplicate skipped: {len(csvs) - added}\n")

    def refresh_file_list(self):
        self.file_list.delete(0, "end")
        for p in self.files:
            self.file_list.insert("end", Path(p).name)

    def remove_selected_file(self):
        selected = list(self.file_list.curselection())
        for index in reversed(selected):
            self.files.pop(index)
        self.refresh_file_list()

    def clear_files(self):
        self.files = []
        self.refresh_file_list()

    def choose_output(self):
        path = filedialog.askdirectory(title="Pilih folder output", initialdir=self.output_var.get() if Path(self.output_var.get()).exists() else None)
        if path:
            self.output_var.set(path)

    def open_output(self):
        path = Path(self.output_var.get())
        path.mkdir(parents=True, exist_ok=True)
        popen_hidden(f'explorer "{path}"')

    def log(self, msg):
        self.q.put(("log", msg))

    def clear_log(self):
        self.log_text.delete("1.0", "end")

    def copy_log(self):
        text = self.log_text.get("1.0", "end")
        self.root.clipboard_clear()
        self.root.clipboard_append(text)
        self.log("Log copied.\n")

    def set_progress(self, done, total, detail):
        pct = max(0, min(100, int(done * 100 / max(1, total))))
        self.q.put(("progress", (pct, detail)))

    def poll_queue(self):
        try:
            while True:
                msg_type, value = self.q.get_nowait()
                if msg_type == "log":
                    self.log_text.insert("end", value)
                    self.log_text.see("end")
                elif msg_type == "progress":
                    pct, detail = value
                    self.progress["value"] = pct
                    self.progress_label.config(text=f"{pct}%")
                    self.detail_label.config(text=detail)
        except queue.Empty:
            pass
        self.root.after(150, self.poll_queue)

    def preview_detail(self):
        if not self.files:
            messagebox.showwarning("Belum ada CSV", "Tambahkan CSV dulu.")
            return
        selected = self.selected_preset_names()
        current_cfg = self.full_config_for_save()
        if current_cfg.get("generate_mode") != "library" and not selected:
            messagebox.showwarning("Belum ada preset", "Centang minimal 1 preset.")
            return
        try:
            if current_cfg.get("generate_mode") == "library":
                stats = collect_library_stats(self.files, current_cfg)
                cols = ", ".join(LIBRARY_COLUMN_LABELS.get(k, k) for k in selected_library_keys(current_cfg)) or "-"
                message = (
                    f"Mode: MP3 per cell\n"
                    f"CSV: {len(self.files)}\n"
                    f"Kolom: {cols}\n"
                    f"Rows: {'Centang saja' if current_cfg.get('rows') == 'checked' else 'Semua'}\n"
                    f"Total row: {stats['rows']}\n"
                    f"Total audio cell: {stats['audio_total']}\n"
                    f"Skip existing: {stats['skipped_existing']}\n"
                    f"Akan dibuat: {stats['will_generate']}\n"
                    f"Cell kosong dilewati: {stats['empty']}\n"
                    f"ZIP per Text: {'Ya' if current_cfg.get('zip_per_text') else 'Tidak'}\n"
                    f"ZIP All / Merge Selected: {'Ya' if current_cfg.get('zip_all') else 'Tidak'}\n\n"
                    f"Estimasi durasi audio baru: {format_seconds(stats['seconds'])}\n"
                    f"Estimasi ukuran MP3 baru: ± {stats['approx_mb']:.1f} MB\n\n"
                    "Nama file contoh: 001_r001_mandkw.mp3"
                )
                self.log(message.replace("\n", " | ") + "\n")
                messagebox.showinfo("Preview MP3 per cell", message)
                return

            stats = collect_stats(self.files, selected, self.presets, current_cfg)
            message = (
                f"CSV: {len(self.files)}\n"
                f"Preset dipilih: {len(selected)}\n"
                f"Mode: {'Merge menjadi 1 MP3 per preset' if stats.get('merge_files') else 'MP3 terpisah per CSV'}\n"
                f"Random: {'Merge semua file (1 urutan untuk semua preset)' if any(normalize_preset(self.presets[n]).get('random_merge_file', False) for n in selected) else ('Per file' if any(normalize_preset(self.presets[n]).get('random_per_file', False) for n in selected) else 'Tidak')}\n"
                f"Total output MP3: {stats['outputs']}\n"
                f"Skip existing: {stats['skipped_existing']}\n"
                f"Akan dibuat: {stats['will_generate']}\n\n"
                f"Total row: {stats['total_rows']}\n"
                f"Baris aktif: {stats['active_rows']}\n\n"
                f"TTS Mandarin: {stats['audio_by_lang'].get('zh', 0)}\n"
                f"TTS English: {stats['audio_by_lang'].get('en', 0)}\n"
                f"TTS Indonesia: {stats['audio_by_lang'].get('id', 0)}\n\n"
                f"Estimasi durasi: {format_seconds(stats['seconds'])}\n"
                f"Estimasi ukuran MP3: ± {stats['approx_mb']:.1f} MB\n\n"
                "Catatan: durasi dan ukuran adalah estimasi."
            )
            self.log(message.replace("\n", " | ") + "\n")
            messagebox.showinfo("Preview Detail", message)
        except Exception as e:
            messagebox.showerror("Preview error", str(e))

    def stop_generate(self):
        self.stop_event.set()
        self.log("Stop diminta. Generator akan berhenti setelah audio saat ini selesai.\n")

    def start_generate(self):
        if self.running:
            return
        if edge_tts is None:
            messagebox.showerror("edge-tts belum ada", "Jalankan: py -m pip install edge-tts")
            return
        if not self.files:
            messagebox.showwarning("Belum ada CSV", "Tambahkan CSV dulu.")
            return
        global_cfg_preview = self.full_config_for_save()
        library_mode = global_cfg_preview.get("generate_mode") == "library"
        selected = self.selected_preset_names()
        if not library_mode and not selected:
            messagebox.showwarning("Belum ada preset", "Centang minimal 1 preset.")
            return
        if library_mode and not selected_library_keys(global_cfg_preview):
            messagebox.showwarning("Belum ada kolom", "Pilih minimal 1 kolom MP3 per cell.")
            return

        # Apply the controls currently visible in the UI to the active preset
        # before generating. Previously, Generate used the last saved preset,
        # so a newly selected Random Merge File option could be ignored unless
        # the user clicked Update first.
        if self.active_preset_name in self.presets:
            self.presets[self.active_preset_name] = self.current_preset_payload()

        global_cfg = self.full_config_for_save()
        save_config(global_cfg)
        save_presets(self.presets)

        self.running = True
        self.stop_event.clear()
        self.generate_button.config(state="disabled")
        self.stop_button.config(state="normal")
        self.progress["value"] = 0
        self.progress_label.config(text="0%")
        self.detail_label.config(text="Starting...")
        self.log_text.delete("1.0", "end")
        self.log("Mulai generate MP3...\n")
        if global_cfg.get("generate_mode") == "library":
            self.log("Mode: MP3 per cell\n")
            self.log("Kolom: " + ", ".join(LIBRARY_COLUMN_LABELS.get(k, k) for k in selected_library_keys(global_cfg)) + "\n")
            self.log(f"ZIP per Text: {'ON' if global_cfg.get('zip_per_text') else 'OFF'} | ZIP All: {'ON' if global_cfg.get('zip_all') else 'OFF'}\n")
        else:
            self.log(f"Preset: {', '.join(selected)}\n")
            self.log(f"Mode: {'Merge' if global_cfg.get('merge_files') and len(self.files) > 1 else 'Terpisah'}\n")
        self.log(f"CSV: {len(self.files)} file\n\n")

        def worker():
            try:
                if global_cfg.get("generate_mode") == "library":
                    outputs = asyncio.run(generate_library_all(self.files, global_cfg, self.log, self.set_progress, self.stop_event))
                    # v3.7: ZIP dibuat dari MP3 yang sudah ada, jadi tetap boleh jalan
                    # setelah MP3 generation selesai/skip existing. Sebelumnya ZIP hanya
                    # dibuat pada akhir proses dan tampak seperti tidak terbentuk bila user
                    # menunggu di folder yang salah atau proses berhenti sebelum tahap ZIP.
                    if global_cfg.get("zip_per_text") or global_cfg.get("zip_all"):
                        self.log("\nMembuat ZIP... tunggu sampai muncul DONE.\n")
                        outputs = list(outputs) + create_library_zips(self.files, global_cfg, self.log)
                else:
                    outputs = asyncio.run(generate_all(self.files, selected, self.presets, global_cfg, self.log, self.set_progress, self.stop_event))
                if self.stop_event.is_set():
                    self.log("\nSTOPPED.\n")
                else:
                    self.set_progress(100, 100, "Done")
                    self.log("\nDONE.\n")
                    if global_cfg.get("auto_open_output", True) and outputs:
                        self.root.after(0, self.open_output)
            except Exception as e:
                self.log(f"\nERROR: {e}\n")
            finally:
                self.running = False
                self.root.after(0, lambda: self.generate_button.config(state="normal"))
                self.root.after(0, lambda: self.stop_button.config(state="disabled"))

        threading.Thread(target=worker, daemon=True).start()


root = tk.Tk()
try:
    ttk.Style().theme_use("clam")
except Exception:
    pass
App(root)
root.mainloop()
