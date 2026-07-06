# C2 fill-list dispatch: per-lane work orders from the stratified core spine.
# Codex-consumable; fill semantics witnessed | gap | not_applicable; no invented forms.
import json
import sys
from pathlib import Path
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
OUT = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")
core = json.loads((OUT / "STRATIFIED_CORE_SPINE_PROPOSAL_20260704.json").read_text(encoding="utf-8"))

LANE_NOTES = {
    "pan_romance": "fill from family source matrix + fallback shelves; cite es/fr tier-0 and pt/gl/ca/it/ro/rm rows; access-ledger fields per PAN_ROMANCE_ACCESS_LEDGER_HANDOFF",
    "controlled_arabic": "fill from native math register shelf; status vocabulary as in CONTROLLED_ARABIC_60_TERM_SPINE (seed/attested/fallback/open)",
    "arabic_farsi_persianate": "fill via paired fa/ar evidence; rejection_lanes discipline stays (no Dari/Tajik inheritance)",
    "malay_indonesian": "fill from id/my dual-standard evidence; variant_pair where standards diverge",
    "interslavic": "rows arrive via concept ledger (de→concept); mark linked_to_concept vs witnessed_for_branch honestly; W/S witnesses from 20-source shelf where present",
}

per_lane = defaultdict(list)
for r in core["rows"]:
    for lane in r["missing_lanes"]:
        per_lane[lane].append(r)

md = ["# C2 Fill-List Dispatch — per-lane work orders", "",
      "2026-07-04. From STRATIFIED_CORE_SPINE_PROPOSAL (67 rows: proof-grammar 22 / curriculum 28 / Noether 17).",
      "Rule per row per lane: provide a WITNESSED form (source-pinned), or mark GAP (searched, absent), or NOT_APPLICABLE (with reason). Never invent forms. Rows already present in a lane are not listed.",
      ""]
for lane, rows in sorted(per_lane.items(), key=lambda kv: -len(kv[1])):
    md.append(f"## {lane} — {len(rows)} rows to fill")
    md.append(f"_{LANE_NOTES.get(lane, '')}_")
    md.append("")
    by_stratum = defaultdict(list)
    for r in rows:
        by_stratum[r["stratum"]].append(r["concept_label"])
    for st, labels in sorted(by_stratum.items()):
        md.append(f"- **{st}** ({len(labels)}): " + ", ".join(sorted(labels)))
    md.append("")
(OUT / "C2_FILL_DISPATCH_20260704.md").write_text("\n".join(md), encoding="utf-8")

counts = {lane: len(rows) for lane, rows in per_lane.items()}
(OUT / "C2_FILL_DISPATCH_20260704.json").write_text(json.dumps({
    "artifact": "c2_fill_dispatch_v1", "generated": "2026-07-04",
    "per_lane_missing_counts": counts,
    "rows": {lane: [r["concept_id"] for r in rows] for lane, rows in per_lane.items()},
}, ensure_ascii=False, indent=1), encoding="utf-8")
print("per-lane missing rows:", counts)
