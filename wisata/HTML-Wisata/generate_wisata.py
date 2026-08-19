#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_wisata.py — regenerate the `destinations` data block inside a
trip's Wisata.html from its master Markdown itinerary files.

Shared across all trips/countries under wisata/ — nothing in this parser
is China-specific, it just walks generic Markdown structure. Each trip
still keeps its own Wisata.html (with the DESTINATIONS markers already
in it, seeded from an existing trip's file) and Itinerary/*.md files in
its own wisata/<country>/ subfolder.

USAGE
-----
    py generate_wisata.py <country>

    <country> is the subfolder name under wisata/, e.g.:
        py generate_wisata.py china

    This reads wisata/<country>/Itinerary/*.md and rewrites
    wisata/<country>/Wisata.html in place.

WORKFLOW
--------
1. Edit the itinerary Markdown files in wisata/<country>/Itinerary/,
   following the same structure as the existing files — tables, headings,
   blockquotes, "**Plan-B hari ini:**", the Lampiran section, etc.
2. Run this script with the country folder name as argument.
3. It rewrites the block between the `/* === DESTINATIONS:START === */`
   and `/* === DESTINATIONS:END === */` markers inside that country's
   Wisata.html.
4. Open Wisata.html locally to sanity-check, then commit+push (or tell
   Claude to do it).

WHAT IT PARSES
--------------
- "# Itinerary Perjalanan <Kota>" + subtitle line -> name / dates
- "## Informasi Penerbangan" / "## Informasi Transportasi" table + the
  prose/blockquotes that follow it, up to the first "## Hari" heading
  -> transportPergi (flight-style if the Rute row looks like
     "CGK City (T3) -> NKG City (T2)", otherwise a generic transit card)
- "## Informasi Transportasi Pulang" / "## Informasi Penerbangan Pulang"
  (optional, anywhere before "# Lampiran") -> transportPulang, same table
  format and same flight/transit auto-detection as the outbound leg.
  Rendered as a second collapsible transport card, placed after the
  "Catatan Penting Lainnya" notes card in the Itinerary tab.
- Each "## Hari N — Weekday, Date (Label)" section:
    - an optional blockquote right after the heading -> reserve/advisory
      (classified as "reserve" if it mentions "wajib reservasi" /
      "reservasi wajib", otherwise "advisory")
    - the | Jam | Kegiatan | Catatan | CNY | IDR | table -> day.items
    - the "TOTAL HARI" row -> day.total
    - "**Plan-B hari ini:** ..." paragraph -> day.planb
- "## Ringkasan Budget Total" -> destination.budget
- "## Catatan Penting Lainnya" bullet list -> destination.notes
- "# Lampiran — ..." section, grouped by "## Hari N — ..." and
  "## Cadangan" subheadings, each "### Place Name" entry -> lampiran[]
    - the title -> nameEn (text before the first "(") and nameHanzi (the
      last parenthesised group containing CJK characters, if any); these
      power the "Copy EN" / "Copy Hanzi" buttons in the Lampiran tab. A
      heading combining two places (e.g. "A (Hanzi-A) + B (Hanzi-B)")
      produces a WRONG nameHanzi (grabs B's hanzi for the whole row) —
      split such headings into two separate "###" entries instead.
    - "— Plan-B Hari X" suffix or a leading "\U0001F3F7\uFE0F"/emoji marker -> tag "planb"
    - inside the "## Cadangan" group -> tag "planc"
    - otherwise tag "main" (or "food" if the title contains "(kuliner)")
    - "**Cara reservasi:** ..." -> reserveInfo
    - "**Kenapa jadi Plan-B:** ..." / "**Kenapa tidak dimasukkan:** ..." -> context
    - "**Terkait:** Hari 3, Hari 4" (on a Cadangan/Plan C entry) -> relatedDays;
      the Itinerary tab shows these titles as a "tempat sekitar lain" hint
      under that day's Plan-B banner
    - "- Foto/info: URL" -> wiki
    - "- Video referensi: URL" -> yt
    - "- Rekomendasi tempat sekitar: a; b; c" -> nearby (split on ";")
    - "- Rekomendasi hotel (Trip.com): a; b; c" -> hotels (split on ";",
      each item linked to a Google search scoped to site:trip.com instead
      of Google Maps — used on the "Area Menginap yang Disarankan" entry)

This is a best-effort structural parser tuned to the current template.
If you restructure the Markdown headings/tables significantly, the
script may need small tweaks (it will usually fail loudly rather than
silently produce garbage — check the console output).
"""

import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

if len(sys.argv) != 2:
    sys.exit(
        "Usage: py generate_wisata.py <country>\n"
        "  <country> = subfolder name under wisata/, e.g. 'china'\n"
        "  (looks for wisata/<country>/Itinerary/*.md and\n"
        "   rewrites wisata/<country>/Wisata.html)"
    )
COUNTRY = sys.argv[1]
WISATA_DIR = Path(__file__).resolve().parent.parent  # .../wisata/
MD_DIR = WISATA_DIR / COUNTRY / "Itinerary"
HTML_PATH = WISATA_DIR / COUNTRY / "Wisata.html"
# All *.md files in MD_DIR are picked up automatically — no need to list
# them by hand. City tabs appear in alphabetical filename order; if you
# want a specific order (e.g. Nanjing before Suzhou before Wuxi), prefix
# the filenames with a number, e.g. "1 Nanjing Itinerary.md",
# "2 Suzhou Itinerary.md", "3 Wuxi Itinerary.md".

START_MARK = "/* === DESTINATIONS:START === */"
END_MARK = "/* === DESTINATIONS:END === */"


# --------------------------------------------------------------------------
# text helpers
# --------------------------------------------------------------------------
def htmlify(s):
    """Turn RAW markdown text into HTML: escape &/</>, convert **bold**
    to <b>, convert *italic-ish asides* by just dropping the asterisks
    (these are minor parenthetical notes in the source, not meant to
    render as styled italics on this page)."""
    if s is None:
        return ""
    s = s.strip()
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"\*(.+?)\*", r"\1", s)
    return s


def js_safe(s):
    """Escape text that is ALREADY final HTML so it can sit inside a JS
    template literal (backtick string) without breaking the script."""
    s = s.replace("\\", "\\\\").replace("`", "\\`")
    s = re.sub(r"\$\{", "\\${", s)
    return s


def jsval(raw_text):
    """RAW markdown/plain text -> htmlify -> JS template-literal string.
    Use this for any text pulled straight out of the Markdown that has
    not been processed yet. Never call htmlify()/esc() on the value
    beforehand — that would double-escape it."""
    e = js_safe(htmlify(raw_text))
    return "``" if not e else "`" + e + "`"


# Alias kept for readability at call sites (identical behaviour to jsval).
jsraw = jsval


def jsplain(raw_text):
    """RAW plain text (no htmlify/entity-escaping) -> JS template-literal
    string. Use for values meant to be copied verbatim (clipboard text),
    where "&" must stay "&" and not become "&amp;"."""
    if raw_text is None:
        return "``"
    e = js_safe(raw_text.strip())
    return "``" if not e else "`" + e + "`"


def jswrap(final_html_text):
    """Text that is ALREADY final HTML (built by hand with entities like
    &middot;, or assembled from pieces that were individually htmlify()'d
    already) -> JS template-literal string. Does NOT run htmlify() again."""
    if final_html_text is None:
        final_html_text = ""
    e = js_safe(final_html_text.strip())
    return "``" if not e else "`" + e + "`"


def strip_md_link(s):
    """'[text](url)' -> 'text', leave plain text untouched."""
    return re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)


def is_blank(line):
    return line.strip() == ""


def clean_cell(s):
    s = s.strip()
    s = strip_md_link(s)
    if s in ("—", "-", ""):
        return ""
    return s


def money_cny(s):
    s = s.strip()
    if s in ("—", "-", ""):
        return ""
    return "CNY " + s


def money_idr(s):
    s = s.strip()
    if s in ("—", "-", ""):
        return ""
    return s


# --------------------------------------------------------------------------
# markdown table parsing
# --------------------------------------------------------------------------
def parse_table(lines, start_idx):
    """Given lines and the index of a '| ... |' header row, parse the
    markdown table. Returns (rows, next_idx) where rows is a list of
    lists of cell strings (header row excluded), next_idx is the line
    index right after the table."""
    header = [c.strip() for c in lines[start_idx].strip().strip("|").split("|")]
    i = start_idx + 1
    if i < len(lines) and re.match(r"^\s*\|?[\s:|-]+\|?\s*$", lines[i]):
        i += 1  # separator row
    rows = []
    while i < len(lines) and lines[i].strip().startswith("|"):
        cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
        rows.append(cells)
        i += 1
    return header, rows, i


# --------------------------------------------------------------------------
# section splitting
# --------------------------------------------------------------------------
HEADING_RE = re.compile(r"^(#{1,3})\s+(.*)$")


def split_top_sections(lines):
    """Split the whole doc (before '# Lampiran') into a dict keyed by the
    heading text of each '##' section, preserving order, plus the H1
    title/subtitle at the top."""
    sections = []  # (level, title, [lines])
    cur = None
    for line in lines:
        m = HEADING_RE.match(line)
        if m and len(m.group(1)) <= 2:
            if cur:
                sections.append(cur)
            cur = [len(m.group(1)), m.group(2).strip(), []]
        else:
            if cur is None:
                cur = [0, "__preamble__", []]
            cur[2].append(line)
    if cur:
        sections.append(cur)
    return sections


# --------------------------------------------------------------------------
# transportPergi
# --------------------------------------------------------------------------
ROUTE_RE = re.compile(
    r"^([A-Z]{3})\s+(.+?)\s*\((.+?)\)\s*(?:→|->)\s*([A-Z]{3})\s+(.+?)\s*\((.+?)\)$"
)
FLIGHT_CODE_RE = re.compile(r"\b([A-Z]{2}\d{3,4})\b")
JADWAL_RE = re.compile(
    r"Berangkat\s+([\d:]+)\s*(?:→|->)\s*Tiba\s+([\d:]+)\s*\(([^,]+),\s*([^)]+)\)"
)


def parse_info_section(info_rows_dict, prose_lines, weekday_date_str,
                        field_key="transportPergi",
                        kicker_flight="Transport Pergi",
                        kicker_transit="Transport ke Tujuan"):
    """Build a transportPergi/transportPulang dict from the info table +
    trailing prose. field_key/kicker_* let this same parser produce either
    leg of the trip."""
    rute = info_rows_dict.get("Rute", "")
    m = ROUTE_RE.match(rute)

    # split trailing prose into warning-style paragraphs (blockquotes, or
    # plain paragraphs that open with a "**⚠️ ...**"/"**Perhatian...**"-style
    # bold warning marker) vs plain informational paragraphs
    warn_paras, note_paras = [], []
    buf, buf_is_quote = [], None

    def flush():
        if not buf:
            return
        text = " ".join(buf)
        if re.search(r"catatan biaya|sumber tempat", text, re.I):
            return  # dropped intentionally (shown elsewhere / not needed)
        looks_like_warning = bool(re.match(r"^\*\*(⚠️|■|Perhatian)", text))
        (warn_paras if (buf_is_quote or looks_like_warning) else note_paras).append(text)

    for line in prose_lines + [""]:
        stripped = line.strip()
        is_quote = stripped.startswith(">")
        content = stripped.lstrip(">").strip()
        if content == "":
            flush()
            buf, buf_is_quote = [], None
            continue
        if buf and is_quote != buf_is_quote:
            flush()
            buf = []
        buf_is_quote = is_quote
        buf.append(content)

    # each paragraph is raw markdown -> htmlify it ONCE here, then the
    # joined result is already-final HTML (wrap later with jswrap, not jsval)
    note = "<br><br>".join(htmlify(p) for p in note_paras)
    warn = "<br><br>".join(htmlify(p) for p in warn_paras)

    if m:
        code1, city1, term1, code2, city2, term2 = m.groups()
        maskapai = info_rows_dict.get("Maskapai", "")
        jadwal = info_rows_dict.get("Jadwal", "")
        fcode_m = FLIGHT_CODE_RE.search(maskapai)
        code = fcode_m.group(1) if fcode_m else ""
        jm = JADWAL_RE.search(jadwal)
        if jm:
            dep, arr, kind, dur = jm.groups()
            duration = f"{htmlify(dur.strip())} &middot; {htmlify(kind.strip())}"
            time_range = f"{dep}&ndash;{arr}"
        else:
            duration, time_range = "", ""

        meta = []
        for k, v in info_rows_dict.items():
            if k.lower() in ("rute", "tanggal"):
                continue
            meta.append(f'        [{jsval(k)},{jsval(v)}],')
        meta_js = "\n".join(meta)

        title = f"{code1} &rarr; {code2} &middot; {htmlify(weekday_date_str)} &middot; {time_range}"
        from_name = f"{htmlify(city1)} &middot; {htmlify(term1)}"
        to_name = f"{htmlify(city2)} &middot; {htmlify(term2)}"
        return f"""    {field_key}:{{
      mode:"flight", kicker:{jsval(kicker_flight)},
      title:{jswrap(title)},
      tag:"ok", openByDefault:true, code:{jsval(code)},
      from:{{code:{jsval(code1)}, name:{jswrap(from_name)}}},
      to:{{code:{jsval(code2)}, name:{jswrap(to_name)}}},
      duration:{jswrap(duration)},
      meta:[
{meta_js}
      ],
      note:{jswrap(note)},
      warn:{jswrap(warn)}
    }},"""
    else:
        items = []
        for k, v in info_rows_dict.items():
            if k.lower() == "rute":
                continue
            items.append(f'        [{jsval(k)},{jsval(v)}],')
        items_js = "\n".join(items)
        title = f"Rute belum ditentukan &middot; {htmlify(weekday_date_str)} (perkiraan)"
        return f"""    {field_key}:{{
      mode:"transit", kicker:{jsval(kicker_transit)},
      title:{jswrap(title)},
      tag:"tbd", openByDefault:true,
      items:[
{items_js}
      ],
      warn:{jswrap(warn if warn else note)}
    }},"""


# --------------------------------------------------------------------------
# day sections
# --------------------------------------------------------------------------
DAY_HEAD_RE = re.compile(r"^Hari\s+(\d+)\s*[—-]\s*([^(]+?)\s*(?:\(([^)]*)\))?\s*$")


def parse_day_section(title, body_lines):
    m = DAY_HEAD_RE.match(title)
    if not m:
        return None
    num = int(m.group(1))
    date = m.group(2).strip()
    label = (m.group(3) or "").strip()

    # advisory/reservation text right after the heading, before the table —
    # may be a blockquote ("> ...") or one-or-more plain paragraphs
    # (possibly starting with a "**⚠️/■/Perhatian**" bold marker). Collect
    # ALL such paragraphs (they may span multiple, blank-line-separated
    # paragraphs), htmlify each individually, then join as final HTML.
    reserve, advisory = "", ""
    paras, cur = [], []
    idx = 0
    while idx < len(body_lines) and not body_lines[idx].strip().startswith("|"):
        s = body_lines[idx].strip()
        if s == "":
            if cur:
                paras.append(" ".join(cur))
                cur = []
        else:
            cur.append(s.lstrip(">").strip())
        idx += 1
    if cur:
        paras.append(" ".join(cur))
    if paras:
        raw_joined = " ".join(paras)  # for keyword sniffing only
        final_html = "<br><br>".join(htmlify(p) for p in paras)
        if re.search(r"wajib reservasi|reservasi wajib", raw_joined, re.I):
            reserve = final_html
        else:
            advisory = final_html

    # find table
    items, total = [], None
    i = 0
    while i < len(body_lines):
        if body_lines[i].strip().startswith("|"):
            header, rows, i = parse_table(body_lines, i)
            for r in rows:
                if len(r) < 5:
                    r = r + [""] * (5 - len(r))
                jam, keg, cat, cny, idr = r[0], r[1], r[2], r[3], r[4]
                if "TOTAL" in jam.upper() or "TOTAL" in keg.upper():
                    total = (money_cny(cny) or money_cny(idr), idr)  # handled below
                    # figure out which columns actually hold the numbers
                    nums = [c for c in r if re.search(r"\d", c)]
                    if len(nums) >= 2:
                        total = (money_cny(nums[-2]), money_idr(nums[-1]))
                    continue
                jam_c = clean_cell(jam) or "—"
                dest_c = clean_cell(keg)
                ket_c = clean_cell(cat)
                items.append((jam_c, dest_c, ket_c, "", money_cny(cny), money_idr(idr)))
            continue
        i += 1

    # Plan-B paragraph anywhere in the section — stop at the first blank
    # line so a following "**Update penting:**"-style paragraph doesn't
    # get swallowed into the same field.
    planb = ""
    joined = "\n".join(body_lines)
    pm = re.search(r"\*\*Plan-B hari ini:\*\*\s*(.+?)(?:\n\s*\n|\Z)", joined, re.S)
    if pm:
        planb = re.sub(r"\s+", " ", pm.group(1)).strip()

    return {
        "num": num, "date": date, "label": label,
        "reserve": reserve, "advisory": advisory,
        "items": items, "total": total, "planb": planb,
    }


def render_day_js(d, day_id):
    lines = []
    lines.append("      {")
    lines.append(f'        id:"h{d["num"]}", num:{d["num"]}, date:{jsraw(d["date"])}, label:{jsraw(d["label"])},')
    if d["reserve"]:
        lines.append(f"        reserve:{jswrap(d['reserve'])},")
    if d["advisory"]:
        lines.append(f"        advisory:{jswrap(d['advisory'])},")
    lines.append("        items:[")
    for jam, dest, ket, cat, cny, idr in d["items"]:
        lines.append(
            f"          [{jsraw(jam)},{jsraw(dest)},{jsval(ket)},{jsraw(cat)},{jsraw(cny)},{jsraw(idr)}],"
        )
    lines.append("        ],")
    if d["total"]:
        cny, idr = d["total"]
        lines.append(f'        total:{{cny:{jsraw(cny)}, idr:{jsraw(idr)}}},')
    if d["planb"]:
        lines.append(f"        planb:{jsval(d['planb'])},")
    lines.append("      },")
    return "\n".join(lines)


# --------------------------------------------------------------------------
# budget section
# --------------------------------------------------------------------------
def parse_budget_section(body_lines):
    joined = "\n".join(body_lines)
    note_m = re.match(r"\s*(.+?)\n\n\|", joined, re.S)
    note = re.sub(r"\s+", " ", note_m.group(1)).strip() if note_m else ""

    tables = []
    i = 0
    while i < len(body_lines):
        if body_lines[i].strip().startswith("|"):
            header, rows, i = parse_table(body_lines, i)
            tables.append(rows)
            continue
        i += 1

    # NOTE: rows may have MORE than 3 columns (e.g. a "CNY skenario hemat"
    # column inserted before the real CNY/IDR pair) — always take the CNY
    # value from the second-to-last column and IDR from the last column,
    # never hardcode index [1]/[2], so extra columns don't shift things.
    by_day, by_cat, grand_day, cat_total = [], [], None, None
    if len(tables) >= 1:
        for r in tables[0]:
            label = clean_cell(r[0]).replace("**", "")
            cny = clean_cell(r[-2]).replace("**", "")
            idr = clean_cell(r[-1]).replace("**", "")
            if "GRAND TOTAL" in label.upper():
                grand_day = (label, cny, idr)
                continue
            by_day.append((label, cny, idr))
    if len(tables) >= 2:
        for r in tables[1]:
            label = clean_cell(r[0]).replace("**", "")
            cny = clean_cell(r[-2]).replace("**", "")
            idr = clean_cell(r[-1]).replace("**", "")
            if label.upper() == "TOTAL":
                cat_total = (label, cny, idr)
                continue
            by_cat.append((label, cny, idr))

    caveat_m = re.search(r"\*\*Catatan:\*\*\s*(.+)$", joined, re.S)
    caveat = re.sub(r"\s+", " ", caveat_m.group(1)).strip() if caveat_m else ""

    grand = grand_day or ("GRAND TOTAL", "", "")
    cat_total = cat_total or grand
    return note, by_day, by_cat, grand, cat_total, caveat


def render_budget_js(budget):
    note, by_day, by_cat, grand, cat_total, caveat = budget
    lines = ["    budget:{"]
    lines.append(f"      note:{jsval(note)},")
    lines.append("      byDay:[")
    for label, cny, idr in by_day:
        lines.append(f"        [{jsraw(label)},{jsraw(cny)},{jsraw(idr)}],")
    lines.append("      ],")
    lines.append("      byCategory:[")
    for label, cny, idr in by_cat:
        lines.append(f"        [{jsraw(label)},{jsraw(cny)},{jsraw(idr)}],")
    lines.append("      ],")
    lines.append(f'      grand:[{jsraw(grand[0])},{jsraw(grand[1])},{jsraw(grand[2])}],')
    lines.append(f'      catTotal:[{jsraw(cat_total[0])},{jsraw(cat_total[1])},{jsraw(cat_total[2])}],')
    lines.append(f"      caveat:{jsval(caveat)},")
    lines.append("    },")
    return "\n".join(lines)


# --------------------------------------------------------------------------
# notes (Catatan Penting Lainnya)
# --------------------------------------------------------------------------
def parse_bullet_list(body_lines):
    out = []
    for line in body_lines:
        s = line.strip()
        if s.startswith("- ") or s.startswith("* "):
            out.append(s[2:].strip())
    return out


# --------------------------------------------------------------------------
# lampiran
# --------------------------------------------------------------------------
ENTRY_HEAD_RE = re.compile(r"^(?:\S+\uFE0F\s+)?(.+?)(?:\s*—\s*(Plan-B[^(]*)(?:\(([^)]*)\))?)?$")


def parse_lampiran_place(title_line, body_lines, group_key, is_cadangan, is_intro=False):
    title_line = title_line.strip()
    # strip a leading emoji/badge like the "tag" glyphs
    title_line = re.sub(r"^[^\w\(]+\s*", "", title_line)

    planb_m = re.search(r"—\s*Plan-B\s+(Hari[\w\s&]+)", title_line)
    is_food = bool(re.search(r"\(kuliner\)", title_line, re.I))
    title = re.sub(r"\s*—\s*Plan-B.*$", "", title_line).strip()
    # drop a trailing verification badge (✅ verified / ⚠️ not yet verified)
    # — that's an authoring note about the hanzi, not something to show
    # travelers. The hanzi itself (in parentheses right before it) stays.
    title = re.sub(r"\s*[✅⚠️]+\s*$", "", title).strip()

    # Copy-to-clipboard names (for the Amap/Google Maps buttons in the
    # Lampiran tab): nameEn = everything before the first "(" (so trailing
    # qualifiers like "(kuliner)", "(Cultural Relics Area)", or the hanzi
    # itself never leak into the English name); nameHanzi = the LAST
    # parenthesised group that contains at least one CJK character (so an
    # English aside in earlier parens, e.g. "Huishan Temple (Cultural
    # Relics Area) (惠山寺)", doesn't get mistaken for the hanzi group).
    # NOTE: an entry whose heading combines two distinct places (e.g. an
    # old "A (汉字A) + B (汉字B)" title) will produce a WRONG/mismatched
    # nameHanzi here — such headings should be split into two separate
    # "###" entries instead (see SKILL.md), not patched around here.
    name_en = re.split(r"\s*\(", title, maxsplit=1)[0].strip()
    hanzi_m = re.search(r"\(([^()]*[一-鿿][^()]*)\)\s*$", title)
    name_hanzi = hanzi_m.group(1).strip() if hanzi_m else ""

    joined = "\n".join(body_lines)
    context = ""
    ctx_m = re.search(
        r"\*\*(Kenapa jadi Plan-B|Kenapa tidak dimasukkan)[:\uFF1A]?\*\*\s*(.+?)(?:\n\n|\Z)",
        joined, re.S,
    )
    reserve_info = ""
    res_m = re.search(r"\*\*Cara reservasi:\*\*\s*(.+?)(?:\n\n|\Z)", joined, re.S)
    if res_m:
        reserve_info = re.sub(r"\s+", " ", res_m.group(1)).strip()

    # "**Terkait:** Hari 3, Hari 4" on a Cadangan (Plan C) entry -> which
    # itinerary day(s) this place is geographically close to, so the
    # Itinerary tab can surface it under that day's Plan-B banner as a
    # "tempat sekitar lain" hint. Only meaningful on planc entries, but
    # parsed generically here.
    related_days = []
    rel_m = re.search(r"\*\*Terkait:\*\*\s*(.+?)(?:\n\n|\Z)", joined, re.S)
    if rel_m:
        related_days = [int(x) for x in re.findall(r"Hari\s+(\d+)", rel_m.group(1))]

    wiki = ""
    yt = ""
    nearby = []
    hotels = []
    for line in body_lines:
        s = line.strip().lstrip("-").strip()
        if s.lower().startswith("foto/info:"):
            wiki = s.split(":", 1)[1].strip()
        elif s.lower().startswith("video referensi:"):
            yt = s.split(":", 1)[1].strip()
        elif s.lower().startswith("rekomendasi tempat sekitar:"):
            raw = s.split(":", 1)[1].strip()
            nearby = [x.strip() for x in re.split(r";\s*", raw) if x.strip()]
        elif re.match(r"^rekomendasi hotel\b", s, re.I):
            raw = s.split(":", 1)[1].strip() if ":" in s else ""
            hotels = [x.strip() for x in re.split(r";\s*", raw) if x.strip()]

    # main paragraph text = everything before the first "**...**" special
    # line, "- Foto/info", or "- Video referensi". A standalone
    # "✅/⚠️ Nama Hanzi ..." verification line is an authoring note, not
    # traveler-facing content — skip it, but keep reading afterwards.
    text_paras = []
    for line in body_lines:
        s = line.strip()
        if not s:
            continue
        if s.startswith("**Cara reservasi") or s.startswith("**Kenapa") or s.startswith("**Terkait"):
            break
        s_lower = s.lower().lstrip("-").strip()
        if s_lower.startswith(("foto/info:", "video referensi:", "rekomendasi tempat sekitar:")) or re.match(r"^rekomendasi hotel\b", s_lower):
            break
        if re.match(r"^[✅⚠️]", s):
            continue
        text_paras.append(s)
    text = " ".join(text_paras)

    if is_cadangan:
        tag, label = "planc", "Plan C"
    elif planb_m:
        tag = "planb"
        label = "Plan-B " + planb_m.group(1).strip()
    elif is_food:
        tag, label = "food", "Kuliner"
    elif is_intro:
        tag, label = "info", "Sebelum Berangkat"
    else:
        tag, label = "main", "Itinerary utama"

    if ctx_m:
        raw_ctx = re.sub(r"\s+", " ", ctx_m.group(2)).strip()
        prefix = "Kenapa jadi Plan-B: " if ctx_m.group(1).lower().startswith("kenapa jadi") else "Kenapa tidak dimasukkan: "
        context = prefix + raw_ctx

    return {
        "group": group_key, "tag": tag, "label": label, "title": title,
        "nameEn": name_en, "nameHanzi": name_hanzi,
        "context": context, "text": text, "reserveInfo": reserve_info,
        "wiki": wiki, "yt": yt, "nearby": nearby, "hotels": hotels,
        "relatedDays": related_days,
    }


def render_lampiran_entry_js(p):
    lines = [f'      {{group:{jsraw(p["group"])}, tag:{jsraw(p["tag"])}, label:{jsraw(p["label"])}, title:{jsraw(p["title"])},']
    if p["nameEn"]:
        lines.append(f"       nameEn:{jsplain(p['nameEn'])},")
    if p["nameHanzi"]:
        lines.append(f"       nameHanzi:{jsplain(p['nameHanzi'])},")
    if p["context"]:
        lines.append(f"       context:{jsval(p['context'])},")
    lines.append(f"       text:{jsval(p['text'])},")
    if p["reserveInfo"]:
        lines.append(f"       reserveInfo:{jsval(p['reserveInfo'])},")
    if p["wiki"]:
        lines.append(f"       wiki:{jsraw(p['wiki'])},")
    if p["yt"]:
        lines.append(f"       yt:{jsraw(p['yt'])},")
    if p["nearby"]:
        nb = ",".join(jsval(x) for x in p["nearby"])
        lines.append(f"       nearby:[{nb}],")
    if p["hotels"]:
        ht = ",".join(jsval(x) for x in p["hotels"])
        lines.append(f"       hotels:[{ht}],")
    if p["relatedDays"]:
        rd = ",".join(str(n) for n in p["relatedDays"])
        lines.append(f"       relatedDays:[{rd}],")
    lines[-1] = lines[-1].rstrip(",") + "},"
    return "\n".join(lines)


# --------------------------------------------------------------------------
# main per-file parse
# --------------------------------------------------------------------------
def parse_destination(md_path):
    raw = md_path.read_text(encoding="utf-8")
    raw = raw.replace("\ufeff", "")
    lines = raw.split("\n")
    # drop markdown horizontal rules \u2014 pure dividers, never content
    lines = [l for l in lines if l.strip() not in ("---", "***", "___")]

    # split at the first H1 "# Lampiran" (top-level, not the doc's own H1 title)
    split_idx = None
    for i, line in enumerate(lines):
        if re.match(r"^#\s+Lampiran\b", line) and i > 0:
            split_idx = i
            break
    if split_idx is None:
        raise ValueError(f"tidak ketemu '# Lampiran' section")

    main_lines = lines[:split_idx]
    lampiran_lines = lines[split_idx:]

    title_m = re.match(r"^#\s+Itinerary Perjalanan\s+(.+)$", main_lines[0].strip())
    name = title_m.group(1).strip() if title_m else md_path.stem
    dates_line = main_lines[1].strip()
    dest_id = name.lower().replace(" ", "")

    sections = split_top_sections(main_lines[2:])

    info_rows = {}
    info_prose = []
    info_rows_pulang = {}
    info_prose_pulang = []
    has_pulang_section = False
    weekday_date_str = ""
    days = []
    budget = None
    notes = []

    for level, heading, body in sections:
        if heading == "__preamble__":
            continue
        if re.match(r"^Informasi (Penerbangan|Transportasi)$", heading):
            for j, l in enumerate(body):
                if l.strip().startswith("|"):
                    header, rows, nxt = parse_table(body, j)
                    for r in rows:
                        if len(r) >= 2:
                            info_rows[r[0].strip("* ")] = r[1].strip()
                    info_prose = body[nxt:]
                    break
        elif re.match(r"^Informasi (Penerbangan|Transportasi) Pulang$", heading):
            has_pulang_section = True
            for j, l in enumerate(body):
                if l.strip().startswith("|"):
                    header, rows, nxt = parse_table(body, j)
                    for r in rows:
                        if len(r) >= 2:
                            info_rows_pulang[r[0].strip("* ")] = r[1].strip()
                    info_prose_pulang = body[nxt:]
                    break
            else:
                info_prose_pulang = body
        elif DAY_HEAD_RE.match(heading):
            d = parse_day_section(heading, body)
            if d:
                days.append(d)
                if not weekday_date_str:
                    weekday_date_str = d["date"]
        elif heading.startswith("Ringkasan Budget Total"):
            budget = parse_budget_section(body)
        elif heading == "Catatan Penting Lainnya":
            notes = parse_bullet_list(body)

    if not weekday_date_str and days:
        weekday_date_str = days[0]["date"]

    transport_js = parse_info_section(info_rows, info_prose, weekday_date_str)
    transport_pulang_js = None
    if has_pulang_section:
        pulang_date_str = info_rows_pulang.get("Tanggal", "") or (days[-1]["date"] if days else weekday_date_str)
        transport_pulang_js = parse_info_section(
            info_rows_pulang, info_prose_pulang, pulang_date_str,
            field_key="transportPulang",
            kicker_flight="Transport Pulang",
            kicker_transit="Transport Pulang",
        )

    # --- lampiran ---
    # Groups appear in whatever order the Markdown has them (typically:
    # an intro "Sebelum Berangkat" section first, then "Hari N" groups,
    # then "Cadangan" last) — we preserve that document order rather than
    # hardcoding it, so a "Sebelum Berangkat" section always renders first
    # simply because it's written first in the file.
    lamp_sections = split_top_sections(lampiran_lines[1:])
    lampiran_entries = []
    lampiran_groups = []  # [(key, heading_text)] in first-seen order
    for level, heading, body in lamp_sections:
        if heading == "__preamble__":
            continue
        is_cadangan = heading.strip().lower() == "cadangan"
        is_intro = bool(re.search(r"sebelum\s+berangkat\s*$", heading, re.I))
        gm = re.match(r"^Hari\s+(\d+)", heading)
        om = re.match(r"^Opsional\s+(\S+)", heading, re.I)
        if is_cadangan:
            group_key = "cadangan"
        elif is_intro:
            group_key = "intro"
        elif gm:
            group_key = f"h{gm.group(1)}"
        elif om:
            group_key = f"opsional{om.group(1).lower()}"
        else:
            print(f"    [!] Heading Lampiran tidak dikenali, dilewati: '{heading}'")
            continue
        lampiran_groups.append((group_key, heading.strip()))

        # split this group's body into ### place entries
        place_sections = []
        cur_title, cur_body = None, []
        for line in body:
            hm = re.match(r"^###\s+(.*)$", line)
            if hm:
                if cur_title is not None:
                    place_sections.append((cur_title, cur_body))
                cur_title, cur_body = hm.group(1), []
            else:
                if cur_title is not None:
                    cur_body.append(line)
        if cur_title is not None:
            place_sections.append((cur_title, cur_body))

        for t, b in place_sections:
            entry = parse_lampiran_place(t, b, group_key, is_cadangan, is_intro)
            lampiran_entries.append(entry)

    return {
        "id": dest_id, "name": name, "dates_line": dates_line,
        "transport_js": transport_js, "transport_pulang_js": transport_pulang_js,
        "days": days, "budget": budget,
        "notes": notes, "lampiran": lampiran_entries, "lampiran_groups": lampiran_groups,
    }


def render_destination_js(dest):
    lines = []
    lines.append("  {")
    lines.append(f'    id:{jsraw(dest["id"])},')
    lines.append(f'    name:{jsraw(dest["name"])},')
    lines.append(f'    dates:{jsval(dest["dates_line"])},')
    lines.append("")
    lines.append(dest["transport_js"])
    lines.append("")
    lines.append("    days:[")
    for d in dest["days"]:
        lines.append(render_day_js(d, d["num"]))
    lines.append("    ],")
    lines.append("")
    if dest["budget"]:
        lines.append(render_budget_js(dest["budget"]))
        lines.append("")
    lines.append("    notes:[")
    for n in dest["notes"]:
        lines.append(f"      {jsval(n)},")
    lines.append("    ],")
    lines.append("")
    if dest["transport_pulang_js"]:
        lines.append(dest["transport_pulang_js"])
        lines.append("")
    lines.append("    lampiran:[")
    last_group = None
    for p in dest["lampiran"]:
        if p["group"] != last_group:
            lines.append(f"      // --- {p['group']} ---")
            last_group = p["group"]
        lines.append(render_lampiran_entry_js(p))
    lines.append("    ],")
    lines.append("    lampiranGroups:[")
    for key, heading in dest["lampiran_groups"]:
        lines.append(f"      {{key:{jsraw(key)}, heading:{jsval(heading)}}},")
    lines.append("    ],")
    lines.append("  },")
    return "\n".join(lines)


def main():
    if not HTML_PATH.exists():
        sys.exit(f"[!] Tidak ketemu {HTML_PATH}")
    if not MD_DIR.exists():
        sys.exit(f"[!] Folder tidak ketemu: {MD_DIR}")

    md_paths = sorted(MD_DIR.glob("*.md"), key=lambda p: p.name.lower())
    if not md_paths:
        sys.exit(f"[!] Tidak ada file .md di {MD_DIR}")

    dest_blocks = []
    for path in md_paths:
        print(f"[.] Parsing {path.name} ...")
        try:
            dest = parse_destination(path)
        except SystemExit:
            raise
        except Exception as e:
            print(f"[!] Gagal parse {path.name}, dilewati: {e}")
            continue
        print(f"    -> {len(dest['days'])} hari, {len(dest['lampiran'])} entri lampiran")
        dest_blocks.append(render_destination_js(dest))

    if not dest_blocks:
        sys.exit("[!] Tidak ada destinasi yang berhasil diparse, dibatalkan.")

    new_block = (
        START_MARK + "\n"
        "const destinations = [\n"
        + "\n".join(dest_blocks) + "\n"
        "];\n"
        + END_MARK
    )

    html = HTML_PATH.read_text(encoding="utf-8")
    if START_MARK not in html or END_MARK not in html:
        sys.exit("[!] Marker DESTINATIONS:START/END tidak ketemu di Wisata.html")

    pattern = re.compile(re.escape(START_MARK) + r".*?" + re.escape(END_MARK), re.S)
    new_html, n = pattern.subn(new_block, html, count=1)
    if n != 1:
        sys.exit("[!] Gagal mengganti blok data (marker rusak?)")

    HTML_PATH.write_text(new_html, encoding="utf-8", newline="\n")
    print(f"[OK] Wisata.html diperbarui ({len(dest_blocks)} destinasi).")


if __name__ == "__main__":
    main()
