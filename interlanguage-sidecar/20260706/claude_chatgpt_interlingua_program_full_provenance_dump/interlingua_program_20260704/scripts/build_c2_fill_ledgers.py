# Task E: lane-specific C2 fill ledgers — one codex-consumable file per lane.
# Each missing row becomes a fillable record: witnessed | gap | not_applicable.
# No forms invented; existing lane evidence pointers included where the spine has them.
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
OUT = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")
DISP = OUT / "dispatch"
DISP.mkdir(exist_ok=True)

core = json.loads((OUT / "STRATIFIED_CORE_SPINE_PROPOSAL_20260704.json").read_text(encoding="utf-8"))
spine = json.loads((OUT / "UNION_TERM_SPINE_v2_WITH_SLAVIC.json").read_text(encoding="utf-8"))

LANE_HEADERS = {
    "pan_romance": ("Pan-Romance lane (R1)",
        "Witness sources: family source matrix + fallback shelves (es/fr tier-0; pt/gl/ca/it/ro/rm). "
        "Fill via access-ledger fields per PAN_ROMANCE_ACCESS_LEDGER_HANDOFF_20260704.md. "
        "Comparators (Interlingua/Esperanto/...) are evidence floor, never authority."),
    "controlled_arabic": ("Controlled Arabic lane (R3)",
        "Witness sources: native math register shelf (+ targeted fallback PDFs, marked). "
        "Status vocabulary as in the 60-term spine (source_backed_promotable_seed / attested_needs_review / "
        "fallback_attested_needs_review / open_*)."),
    "arabic_farsi_persianate": ("Arabic/Farsi/Persianate ledger (R3)",
        "Paired ar/fa evidence; bridge candidates carry rejection_lanes (no Dari/Tajik inheritance). "
        "Persianate rows are comparison-register entries, not living-language claims."),
    "malay_indonesian": ("Malay-Indonesian lane (R7)",
        "Dual-standard evidence (id + my); variant_pair_required where standards diverge; "
        "access-gain fields per the lane's reviewer-route plan."),
    "interslavic": ("Interslavic lane (Slavic)",
        "Rows arrive via the interlingual concept ledger (de->concept). Statuses stay honest: "
        "linked_to_concept vs witnessed_for_branch (E/W/S separately; W/S from the 20-source shelf) "
        "vs reviewed_for_bridge_use. Draft translations are NOT witnesses (SOURCE_USE_POLICY)."),
}

counts = {}
for lane, (title, note) in LANE_HEADERS.items():
    rows = []
    for r in core["rows"]:
        if lane not in r["missing_lanes"]:
            continue
        rows.append(r)
    counts[lane] = len(rows)
    md = [f"# C2 Fill Ledger — {title}", "",
          f"2026-07-04. {len(rows)} core-spine rows missing in this lane. For each: provide a WITNESSED form "
          "(source-pinned, native evidence per SOURCE_USE_POLICY category 2), or mark GAP (searched, absent), "
          "or NOT_APPLICABLE (with reason). Never invent forms. Return this file filled; it feeds "
          "UNION_TERM_SPINE_v3 and the lane's own spine.", "",
          f"_{note}_", ""]
    ledger_rows = []
    for r in sorted(rows, key=lambda x: (x["stratum"], x["concept_label"])):
        present = ", ".join(l for l in r["present_lanes"])
        md += [f"## {r['concept_label']}  ({r['stratum']})",
               f"- concept_id: `{r['concept_id']}` · present in: {present}",
               "- fill_status: [ ] witnessed / [ ] gap / [ ] not_applicable",
               "- form(s): ", "- witness_source (file/URL + locator): ", "- status_note: ", ""]
        ledger_rows.append({"concept_id": r["concept_id"], "concept_label": r["concept_label"],
                            "stratum": r["stratum"], "fill_status": None, "forms": [],
                            "witness_sources": [], "status_note": None})
    (DISP / f"C2_FILL_{lane.upper()}_20260704.md").write_text("\n".join(md), encoding="utf-8")
    (DISP / f"C2_FILL_{lane.upper()}_20260704.json").write_text(json.dumps({
        "artifact": f"c2_fill_ledger_{lane}", "generated": "2026-07-04",
        "lane": lane, "row_count": len(rows), "rows": ledger_rows,
        "boundary": "fill with witnessed|gap|not_applicable; native witnesses only; no invented forms",
    }, ensure_ascii=False, indent=1), encoding="utf-8")

print("fill ledgers written:", counts)
