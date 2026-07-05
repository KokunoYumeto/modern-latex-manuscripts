# Build UNION_TERM_SPINE_v2_WITH_SLAVIC (json/md/csv) and STRATIFIED_CORE_SPINE_PROPOSAL (json/md).
# Boundary: evidence merge + stratum assignment only; no promotion, no new wording.
import argparse
import csv
import hashlib
import json
import re
from pathlib import Path
from collections import Counter

ap = argparse.ArgumentParser()
ap.add_argument("--outdir", default=r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")
args = ap.parse_args()
OUT = Path(args.outdir)

def sha256(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

V1 = OUT / "frozen" / "UNION_TERM_SPINE_v1_preSlavic.json"
SLAV = OUT / "slavic_term_dataset_20260704.json"
spine = json.loads(V1.read_text(encoding="utf-8"))
slav = json.loads(SLAV.read_text(encoding="utf-8"))

# --- add Slavic lane to matched concepts --------------------------------------
def get(rec, *keys):
    ex = rec.get("extra_fields") or {}
    for k in keys:
        v = rec.get(k) or ex.get(k)
        if isinstance(v, str) and v.strip():
            return v.strip()
    return None

# Slavic column is routed THROUGH the interlingual concept ledger (de -> concept_id -> en),
# NOT via gloss substring matching (retired 2026-07-04 after Ränderung/irreducible false links).
# Deflated counts are kept honest; no fuzzy recovery.
ledger = json.loads((OUT / "INTERLINGUAL_CONCEPT_LEDGER_20260704.json").read_text(encoding="utf-8"))
seed = json.loads((OUT / "data" / "concept_ledger_seed.json").read_text(encoding="utf-8"))
blocked = {c["en"].lower(): set(c.get("do_not_merge_with", [])) for c in seed["concepts"]}

matched, ledger_only = 0, 0
slavic_by_concept = {}
for c in ledger["concepts"]:
    en_key = c["en"].lower()
    if en_key not in spine["concepts"]:
        ledger_only += 1
        continue
    if en_key in blocked and blocked[en_key]:
        pass  # concept itself fine; blocks apply to merging INTO other concepts
    matched += c["term_rows"]
    slavic_by_concept[en_key] = {
        "spine_id": f"ISV-{c['concept_id']}",
        "via": "interlingual_concept_ledger (de->concept_id->en)",
        "linkage": {
            "linked_to_concept": True,
            "witnessed_for_branch": {"east": bool(c["uk"] or c["ru"]), "west": False, "south": False},
            "reviewed_for_bridge_use": False,
            "note": "ledger-routed; East-witnessed via uk/ru labels; W/S pending backfill; NOT review-cleared",
        },
        "forms": {"uk": (c["uk"] or [None])[0], "ru": (c["ru"] or [None])[0],
                  "isv": (c["isv"] or [None])[0], "isv_cyr": (c["isv_cyr"] or [None])[0]},
        "f10_flags": c["f10_flags"],
        "record_count": c["term_rows"],
    }
unmatched = ledger["retrofit_rows_unmapped"]

for k, e in slavic_by_concept.items():
    spine["concepts"][k]["lanes"]["interslavic"] = e
    spine["concepts"][k]["lane_count"] = len(spine["concepts"][k]["lanes"])

spine["artifact"] = "union_term_spine_v2_with_slavic"
spine["generated"] = "2026-07-04"
spine["v2_note"] = ("Slavic lane routed through the interlingual concept ledger (de->concept_id->en); "
                    f"{matched} term rows attached onto {len(slavic_by_concept)} spine concepts; "
                    f"{ledger_only} ledger concepts have no spine row yet (kept ledger-side); "
                    f"{unmatched} retrofit rows remain unmapped (phrase-level; retrofit-ledger scope). "
                    "All Slavic entries are linked_to_concept ONLY - branch witness and review statuses are explicit.")
spine["run_manifest"] = {"inputs": {V1.name: sha256(V1), SLAV.name: sha256(SLAV)}}
(OUT / "UNION_TERM_SPINE_v2_WITH_SLAVIC.json").write_text(
    json.dumps(spine, ensure_ascii=False, indent=1), encoding="utf-8")

LANES = ["pan_romance", "controlled_arabic", "arabic_farsi_persianate", "malay_indonesian", "interslavic"]
with (OUT / "UNION_TERM_SPINE_v2_WITH_SLAVIC.csv").open("w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["concept", "clusters", "lane_count"] + LANES)
    for k, u in sorted(spine["concepts"].items()):
        row = [k, ",".join(u.get("clusters", [])), u["lane_count"]]
        for ln in LANES:
            rec = u["lanes"].get(ln)
            if not rec:
                row.append("")
            else:
                forms = rec.get("forms") or {}
                main = forms.get("isv") or forms.get("my_id") or forms.get("es") or \
                       forms.get("ar_preferred") or forms.get("persianate_bridge") or \
                       next((v for v in forms.values() if v), "")
                row.append(main)
        w.writerow(row)

# --- stratified core spine proposal (C2) --------------------------------------
PROOF_GRAMMAR = {"definition", "theorem", "lemma", "corollary", "proof", "example", "exercise",
                 "problem", "notation", "proposition", "statement", "assumption", "formula",
                 "if and only if", "for all", "exists", "therefore", "conversely", "respectively",
                 "relation", "equation", "identity"}
NOETHER_KEYWORDS = r"invariant|form|transvection|resultant|modulus|reduction|reducent|folding|ground form|complete system|elementary divisor|covariant|contravariant|biquadratic|ternary"

def stratum_of(k, clusters):
    if k in PROOF_GRAMMAR or "proof_grammar" in clusters:
        return "proof_grammar"
    if re.search(NOETHER_KEYWORDS, k):
        return "noether_corpus"
    return "curriculum_algebra"

core_rows = []
for k, u in sorted(spine["concepts"].items()):
    present = sorted(u["lanes"].keys())
    lane_count_nonslav = len([l for l in present if l != "interslavic"])
    stratum = stratum_of(k, u.get("clusters", []))
    in_core = (u["lane_count"] >= 3) or stratum == "proof_grammar" or \
              (stratum == "noether_corpus" and lane_count_nonslav >= 1)
    if not in_core:
        continue
    missing = [l for l in LANES if l not in present]
    core_rows.append({
        "stratum": stratum,
        "concept_id": f"C2-{k[:32].replace(' ', '_')}",
        "concept_label": k,
        "present_lanes": present,
        "missing_lanes": missing,
        "required_fill_action": ("none" if not missing else
                                 "per missing lane: witnessed form | explicit gap | not-applicable"),
        "why_in_core": ("multi-lane overlap (>=3)" if u["lane_count"] >= 3 else
                        ("proof-grammar stratum (universal register need)" if stratum == "proof_grammar"
                         else "Noether-corpus stratum (shared source text)")),
    })

strata_counts = Counter(r["stratum"] for r in core_rows)
core = {
    "artifact": "stratified_core_spine_proposal_v1",
    "generated": "2026-07-04",
    "architecture": {
        "C0_intersection": "17 all-lane concepts - sanity/schema/display only",
        "C1_broad_shared": "32 concepts in >=3 lanes - first comparison set",
        "C2_stratified_core": "THIS artifact - balanced strata with fill-list semantics",
        "C3_outer_union": "138+ concept inventory - discovery surface, not a comparability core",
    },
    "fill_semantics": "each lane per row: witnessed | gap | not_applicable (never invented forms)",
    "strata_counts": dict(strata_counts),
    "row_count": len(core_rows),
    "rows": core_rows,
}
(OUT / "STRATIFIED_CORE_SPINE_PROPOSAL_20260704.json").write_text(
    json.dumps(core, ensure_ascii=False, indent=1), encoding="utf-8")

md = ["# Stratified Core Spine (C2) — proposal v1", "",
      "2026-07-04. Fill semantics: per lane, each row must become witnessed | gap | not-applicable. No invented forms.",
      "",
      f"- Rows: **{len(core_rows)}** — strata: " + ", ".join(f"{s} {n}" for s, n in strata_counts.items()),
      f"- Slavic column source: retrofit ledger ({matched} glossary records matched onto {len(slavic_by_concept)} spine concepts; German-keyed remainder pending concept normalization)",
      "", "| Stratum | Concept | Present | Missing |", "| --- | --- | --- | --- |"]
for r in core_rows:
    md.append(f"| {r['stratum']} | {r['concept_label']} | {', '.join(l[:12] for l in r['present_lanes'])} | {', '.join(l[:12] for l in r['missing_lanes']) or '—'} |")
(OUT / "STRATIFIED_CORE_SPINE_PROPOSAL_20260704.md").write_text("\n".join(md), encoding="utf-8")

print(f"v2: slavic matched {matched} records -> {len(slavic_by_concept)} concepts; unmatched {unmatched}")
print(f"core spine rows: {len(core_rows)} strata: {dict(strata_counts)}")
print("wrote UNION_TERM_SPINE_v2_WITH_SLAVIC.json/.csv + STRATIFIED_CORE_SPINE_PROPOSAL_20260704.json/.md")
