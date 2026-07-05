# THE central artifact: interlingual marker table — all concepts x all language markers,
# with evidence tags and weights. Consolidates spine v2, concept ledger, W/S backfill,
# scores v3, core-spine strata. Cells honest: empty = no data; tags: [S] branch supports
# ISV-cognate family, [C] branch attests competitor lexeme, [d] draft-origin, [?] unpinned.
import csv
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
OUT = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")
DROP = OUT / "user made flr with chat web stuff"

spine = json.loads((OUT / "UNION_TERM_SPINE_v2_WITH_SLAVIC.json").read_text(encoding="utf-8"))
ledger = json.loads((OUT / "INTERLINGUAL_CONCEPT_LEDGER_20260704.json").read_text(encoding="utf-8"))
core = json.loads((OUT / "STRATIFIED_CORE_SPINE_PROPOSAL_20260704.json").read_text(encoding="utf-8"))
bf = json.loads((OUT / "WS_WITNESS_BACKFILL_v1_20260704.json").read_text(encoding="utf-8"))
v3 = json.loads((DROP / "WEIGHTED_INTELLIGIBILITY_SCORES_v3_20260704.json").read_text(encoding="utf-8"))

core_by_label = {r["concept_label"]: r for r in core["rows"]}
v3_by_concept = {r["concept"]: r for r in v3["rows"]}
ledger_by_en = {c["en"].lower(): c for c in ledger["concepts"]}

BF_ALIAS = {"division ring / body": "division ring", "algebra (structure)": "algebra",
            "extension (field)": "extension of the ground field"}

# W/S cell derivation from backfill: competitor lemma from candidate note; support = cognate.
LANG_OF_NOTE = [("cs", r"\bcs\b|czech"), ("sk", r"\bsk\b|slovak"), ("pl", r"\bpl\b|polish"),
                ("sl", r"\bsl\b|slovenian"), ("hr_sr", r"\bhr\b|\bsr\b|croat|serb"), ("bg", r"\bbg\b|bulgar")]

def ws_cells(cname, isv):
    cells = {k: "" for k, _ in LANG_OF_NOTE}
    spec = bf["concepts"].get(cname)
    if not spec:
        return cells
    for h in spec["hits"]:
        lg = h["lang"]
        col = "hr_sr" if lg in ("hr", "sr") else lg
        if col not in cells:
            continue
        if h["kind"] == "support":
            if not cells[col]:
                cells[col] = f"≈{isv} [S]"
        else:
            lemma = h["note"].split(None, 1)[-1] if h["note"] else h["stem"]
            lemma = re.sub(r"^(cs|sk|pl|sl|hr|sr|bg)[ /]*", "", lemma).strip()
            tag = f"{lemma} [C]"
            if "[C]" not in cells[col]:
                cells[col] = tag if not cells[col] else cells[col] + "; " + tag
            elif lemma not in cells[col]:
                cells[col] = cells[col].replace(" [C]", f"/{lemma} [C]", 1)
    return cells

LANES = spine["concepts"]
rows_out = []
for key in sorted(LANES):
    u = LANES[key]
    lanes = u["lanes"]
    led = ledger_by_en.get(key)
    isv = (lanes.get("interslavic", {}).get("forms", {}) or {}).get("isv") or \
          ((led["isv"][0] if led and led["isv"] else None))
    bf_key = next((c for c, a in BF_ALIAS.items() if a == key), key if key in bf["concepts"] else None)
    ws = ws_cells(bf_key, isv or "?") if bf_key else {k: "" for k, _ in LANG_OF_NOTE}
    rom = lanes.get("pan_romance", {}).get("forms", {}) or {}
    ar_c = (lanes.get("controlled_arabic", {}).get("forms", {}) or {})
    afp = (lanes.get("arabic_farsi_persianate", {}).get("forms", {}) or {})
    mi = (lanes.get("malay_indonesian", {}).get("forms", {}) or {})
    sl_lane = lanes.get("interslavic", {}).get("forms", {}) or {}
    v3r = v3_by_concept.get(key) or v3_by_concept.get(bf_key or "")
    cr = core_by_label.get(key)
    branch_cov = 0
    if sl_lane.get("uk") or sl_lane.get("ru") or (led and (led["uk"] or led["ru"])):
        branch_cov += 1
    if any("[S]" in ws[c] or "[C]" in ws[c] for c in ("cs", "sk", "pl")):
        branch_cov += 1
    if any("[S]" in ws[c] or "[C]" in ws[c] for c in ("sl", "hr_sr", "bg")):
        branch_cov += 1
    rows_out.append({
        "concept": key,
        "stratum": (cr["stratum"] if cr else (",".join(u.get("clusters", []))[:24] or "")),
        "C2": "yes" if cr else "",
        "de": "; ".join((led or {}).get("de", [])[:2]) if led else "",
        "en": key,
        "uk": (led["uk"][0] if led and led["uk"] else (sl_lane.get("uk") or "")),
        "ru": (led["ru"][0] if led and led["ru"] else (sl_lane.get("ru") or "")),
        "isv": isv or "",
        "isv_cyr": (led["isv_cyr"][0] if led and led["isv_cyr"] else (sl_lane.get("isv_cyr") or "")),
        **ws,
        "es": rom.get("es") or "", "fr": rom.get("fr") or "",
        "pt": rom.get("pt") or "", "gl": rom.get("gl") or "", "ca": rom.get("ca") or "",
        "it": rom.get("it") or "", "ro": rom.get("ro") or "", "rm": rom.get("rm") or "",
        "ar": ar_c.get("ar_preferred") or afp.get("ar") or "",
        "fa": afp.get("fa") or "",
        "my_id": mi.get("my_id") or "",
        "branch_coverage_slavic": branch_cov,
        "action_class": (v3r or {}).get("action_class", ""),
        "sensitivity": (v3r or {}).get("sensitivity", ""),
        "best_alt_mean_MAG": round((v3r or {}).get("best_noncurrent_mean_mag", 0), 3) if v3r else "",
        "lane_count": u["lane_count"],
    })

COLS = ["concept", "stratum", "C2", "de", "en", "uk", "ru", "isv", "isv_cyr",
        "cs", "sk", "pl", "sl", "hr_sr", "bg",
        "es", "fr", "pt", "gl", "ca", "it", "ro", "rm", "ar", "fa", "my_id",
        "branch_coverage_slavic", "action_class", "sensitivity", "best_alt_mean_MAG", "lane_count"]
with (OUT / "INTERLINGUAL_MARKER_TABLE_v1.csv").open("w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=COLS)
    w.writeheader()
    for r in rows_out:
        w.writerow(r)
(OUT / "INTERLINGUAL_MARKER_TABLE_v1.json").write_text(json.dumps({
    "artifact": "interlingual_marker_table_v1", "generated": "2026-07-04",
    "boundary": "consolidation of existing artifacts; [S]=branch supports ISV-cognate family, [C]=branch attests competitor lexeme (both concept-shelf level); Romance/ar/fa/my forms carry their lane statuses; empty=no data; weights from scores v3 where present",
    "concept_count": len(rows_out),
    "columns": COLS, "rows": rows_out}, ensure_ascii=False, indent=1), encoding="utf-8")

filled = {c: sum(1 for r in rows_out if r.get(c)) for c in COLS if c not in ("concept", "en", "lane_count")}
c2n = sum(1 for r in rows_out if r["C2"])
scored = sum(1 for r in rows_out if r["action_class"])
md = ["# Interlingual Marker Table — v1", "",
      "2026-07-04. THE central artifact: every concept x every language marker, evidence-tagged, weighted where scores exist. Full data: [csv](INTERLINGUAL_MARKER_TABLE_v1.csv) / [json](INTERLINGUAL_MARKER_TABLE_v1.json).",
      "",
      f"- Concepts: **{len(rows_out)}** (C2 core: {c2n}); scored rows (v3 weights): {scored}",
      f"- Column fill (of {len(rows_out)}): " + ", ".join(f"{c} {n}" for c, n in filled.items() if n),
      "",
      "Legend: [S] branch attests a cognate of the current Interslavic form · [C] branch attests a competitor lexeme · both concept-shelf level, row verification pending · empty = no data yet (honest gap).",
      "",
      "## Weighted review rows (from scores v3)",
      "", "| Concept | ISV | cs | pl | hr/sr | sl | bg | action | sensitivity |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for r in rows_out:
    if r["action_class"] in ("review_priority", "variant_or_doublet_note"):
        md.append(f"| {r['concept']} | {r['isv']} | {r['cs']} | {r['pl']} | {r['hr_sr']} | {r['sl']} | {r['bg']} | {r['action_class'][:14]} | {r['sensitivity'][:16]} |")
(OUT / "INTERLINGUAL_MARKER_TABLE_v1.md").write_text("\n".join(md), encoding="utf-8")

print(f"concepts {len(rows_out)} | C2 {c2n} | scored {scored}")
print("fill:", {k: v for k, v in filled.items() if v})
