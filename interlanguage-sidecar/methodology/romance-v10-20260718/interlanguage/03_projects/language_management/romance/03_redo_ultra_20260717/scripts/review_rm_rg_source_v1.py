from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "wordweb" / "ROMANCE_TERM_OCCURRENCES_v1.csv"
OUT = ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_RM_RG_SOURCE_v1.csv"
SUMMARY = ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_RM_RG_SOURCE_v1.json"
LOG = ROOT / "qa" / "OCCURRENCE_REVIEW_RM_RG_SOURCE_v1.log"


def sha(path: Path):
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


with SOURCE.open(encoding="utf-8-sig", newline="") as handle:
    rows = list(csv.DictReader(handle))
source_rows = {r["occurrence_id"]: r for r in rows if r["logical_source_id"] == "CURATED-RM-RG-GRCH-AP1G-2021-M1"}
assert set(source_rows) == {"OCC-8A2E8CACFACD2104", "OCC-278E8BA674E87D7A"}

judgment_specs = [
    (
        "RMJ-001", "OCC-8A2E8CACFACD2104", "T45-S1", "accepted_sense_match",
        "consequence_connective_in_mathematics_word_problem",
        "The sentence uses damai to mark the consequence that the neighbour's cat is also fed from day four.",
    ),
    (
        "RMJ-002", "OCC-278E8BA674E87D7A", "T57-S1", "rejected_adverse_or_wrong_sense",
        "straight_direction_not_algebraic_right_action",
        "The phrase a dretg ora means straight ahead in a route description; it is adverse evidence for the algebraic right-action sense.",
    ),
    (
        "RMJ-003", "OCC-278E8BA674E87D7A", "T57-S2", "accepted_sense_match",
        "ordinary_directional_right_sense_matches",
        "The same a dretg ora occurrence supports the explicitly separated ordinary directional sense.",
    ),
]

out = []
for judgment_id, occurrence_id, sense_id, status, reason, note in judgment_specs:
    source = source_rows[occurrence_id]
    out.append({
        "judgment_id": judgment_id,
        "occurrence_id": occurrence_id,
        "term_id": source["term_id"],
        "sense_id": sense_id,
        "language": "rm",
        "variety_code": "rm-rg",
        "logical_source_id": source["logical_source_id"],
        "record_id": source["record_id"],
        "source_sha256": source["source_sha256"],
        "license_status": source["license_status"],
        "locator_path": source["locator_path"],
        "line_number": source["line_number"],
        "quote": source["quote"],
        "quote_sha256": source["quote_sha256"],
        "semantic_review_status": status,
        "review_reason_code": reason,
        "review_note": note,
        "review_tier": "codex_internal_manual_context_review_20260717",
        "bridge_form_promotion_eligible": "false",
        "human_observation": "false",
    })

fields = list(out[0])
with OUT.open("w", encoding="utf-8-sig", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=fields)
    writer.writeheader()
    writer.writerows(out)

summary = {
    "artifact": "ROMANCE_OCCURRENCE_REVIEW_RM_RG_SOURCE_v1",
    "source_occurrence_manifest_sha256": sha(SOURCE),
    "unique_occurrences": 2,
    "sense_judgments": 3,
    "accepted_sense_matches": 2,
    "rejected_adverse_or_wrong_sense": 1,
    "core_form_promotions": 0,
    "human_observations": 0,
    "review_manifest_sha256": sha(OUT),
    "boundary": "One official bilingual school-mathematics body supports a consequence connective and an ordinary directional sense. It supplies no specialist algebra attestation.",
}
SUMMARY.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
assert all(r["bridge_form_promotion_eligible"] == r["human_observation"] == "false" for r in out)

lines = [
    "PASS unique_occurrences=2 sense_judgments=3",
    "accepted_sense_matches=2 adverse=1",
    "core_form_promotions=0 human_observations=0",
    f"review_manifest_sha256={summary['review_manifest_sha256']}",
]
LOG.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
