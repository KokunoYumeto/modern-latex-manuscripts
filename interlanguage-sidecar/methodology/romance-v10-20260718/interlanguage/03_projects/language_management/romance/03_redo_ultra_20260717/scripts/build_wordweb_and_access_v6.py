from __future__ import annotations

import copy
import csv
import hashlib
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ROMANCE = ROOT.parent
WW5 = ROOT / "wordweb" / "PAN_ROMANCE_WORDWEB_v5.json"
ACCESS5 = ROOT / "access" / "PAN_ROMANCE_ACCESS_LEDGER_v5.json"
REVIEW = ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_T11_T20_v1.csv"
REVIEW_SUMMARY = ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_T11_T20_v1.json"
COHORT_TREE = ROMANCE / "00_lane_control" / "ROMANCE_FAMILY_COHORT_TREE_v2.json"
METHOD = ROOT / "access" / "MII_METHOD_v6.md"
WW6 = ROOT / "wordweb" / "PAN_ROMANCE_WORDWEB_v6.json"
ACCESS6_JSON = ROOT / "access" / "PAN_ROMANCE_ACCESS_LEDGER_v6.json"
ACCESS6_CSV = ROOT / "access" / "PAN_ROMANCE_ACCESS_LEDGER_v6.csv"
LOG = ROOT / "qa" / "WORDWEB_ACCESS_BUILD_v6.log"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def read_csv(path: Path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def split_ids(value: str):
    return [item.strip() for item in value.split(";") if item.strip()]


def append_unique(existing, additions):
    return list(dict.fromkeys(list(existing) + list(additions)))


def append_string_ids(existing: str, additions):
    return ";".join(append_unique(split_ids(existing or ""), additions))


def relation_metrics(wordweb):
    valid_ids = (
        {core["term_id"] for core in wordweb["core_concepts"]}
        | {sense["sense_id"] for sense in wordweb["senses"]}
        | {node["concept_id"] for node in wordweb["c2_extension_nodes"]}
    )
    relation_records = [relation for core in wordweb["core_concepts"] for relation in core["relations"]]
    valid_target_edges = sum(relation.get("target_id") in valid_ids for relation in relation_records)
    memberships = sum(len(core["sense_ids"]) for core in wordweb["core_concepts"])
    return {
        "relation_records": len(relation_records),
        "valid_target_id_edges": valid_target_edges,
        "relation_records_without_target_id": sum(not relation.get("target_id") for relation in relation_records),
        "concept_to_sense_membership_edges": memberships,
        "total_id_resolved_references_including_memberships": valid_target_edges + memberships,
        "reporting_boundary": "Relation records include descriptive/label relations without target IDs; they are not all graph edges.",
    }


wordweb = json.loads(WW5.read_text(encoding="utf-8"))
access = json.loads(ACCESS5.read_text(encoding="utf-8"))
review = read_csv(REVIEW)
review_summary = json.loads(REVIEW_SUMMARY.read_text(encoding="utf-8"))
cohort_tree = json.loads(COHORT_TREE.read_text(encoding="utf-8"))

assert sha(WW5) == "4B2B92D18F2823B1173AF6A9AD7F06FD990813452451F553F7623C300DDFFC5B"
assert review_summary["review_manifest_sha256"] == sha(REVIEW)
assert review_summary["reviewed_rows"] == len(review) == 111
assert review_summary["accepted_sense_matches"] == 90
assert review_summary["rejected_adverse_or_wrong_sense"] == 10
assert review_summary["held_rows"] == 11
assert relation_metrics(wordweb) == {
    "relation_records": 402,
    "valid_target_id_edges": 27,
    "relation_records_without_target_id": 375,
    "concept_to_sense_membership_edges": 106,
    "total_id_resolved_references_including_memberships": 133,
    "reporting_boundary": "Relation records include descriptive/label relations without target IDs; they are not all graph edges.",
}

tree_cohort_ids = [cohort["cohort_id"] for cohort in cohort_tree["reader_cohorts"]]
ledger_cohort_ids = [cohort["cohort_id"] for cohort in access["cohorts"]]
assert cohort_tree["cohort_count"] == len(tree_cohort_ids) == len(set(tree_cohort_ids)) == 9
assert tree_cohort_ids == ledger_cohort_ids

# Correct the preserved v5 semantic defect in the successor only.
t57 = next(core for core in wordweb["core_concepts"] if core["term_id"] == "T57")
t57_edges = [
    relation
    for relation in t57["relations"]
    if relation["type"] == "corpus_adverse_evidence"
    and relation.get("target_label") == "straight_direction_not_algebraic_right_action"
]
assert len(t57_edges) == 1 and t57_edges[0]["target_id"] == "T57-S2"
t57_edges[0]["target_id"] = "T57-S1"
t57_edges[0]["status"] = "adverse for algebraic right-action T57-S1; the same occurrence supports ordinary-direction T57-S2"

support_by_sense = defaultdict(list)
adverse_by_sense = defaultdict(list)
held_by_sense = defaultdict(list)
support_by_term = defaultdict(list)
rejected_by_term = defaultdict(list)
held_by_term = defaultdict(list)
new_evidence = []

for row in review:
    evidence_id = "E-" + row["occurrence_id"]
    status = row["semantic_review_status"]
    support_senses = split_ids(row["reviewed_sense_ids"])
    adverse_senses = split_ids(row["adverse_to_sense_ids"])
    held_senses = split_ids(row["held_for_sense_ids"])
    if status == "accepted_sense_match":
        assert support_senses and not adverse_senses and not held_senses
        for sense_id in support_senses:
            support_by_sense[sense_id].append(evidence_id)
        support_by_term[row["term_id"]].append(evidence_id)
    elif status == "rejected_adverse_or_wrong_sense":
        assert not support_senses and not held_senses
        for sense_id in adverse_senses:
            adverse_by_sense[sense_id].append(evidence_id)
        rejected_by_term[row["term_id"]].append(evidence_id)
    else:
        assert status == "held_insufficient_context_or_unmodeled_sense"
        assert not support_senses and not adverse_senses
        for sense_id in held_senses:
            held_by_sense[sense_id].append(evidence_id)
        held_by_term[row["term_id"]].append(evidence_id)

    new_evidence.append({
        "evidence_id": evidence_id,
        "occurrence_id": row["occurrence_id"],
        "term_id": row["term_id"],
        "reviewed_supporting_sense_ids": support_senses,
        "reviewed_adverse_to_sense_ids": adverse_senses,
        "reviewed_held_for_sense_ids": held_senses,
        "language": row["language"],
        "source_type": "reviewed_consolidated_corpus_context_window",
        "origin_layer": "consolidated_corpus_occurrence_not_inherited_core_and_not_c2_extension",
        "logical_source_id": row["logical_source_id"],
        "record_id": row["record_id"],
        "source_sha256": row["source_sha256"],
        "license_status": row["license_status"],
        "locator": f"{row['locator_path']}:{row['line_number']}",
        "quote": row["quote"],
        "quote_sha256": row["quote_sha256"],
        "acceptance": status,
        "review_reason_code": row["review_reason_code"],
        "review_note": row["review_note"],
        "review_tier": row["review_tier"],
        "evidence_role": row["evidence_role"],
        "core_form_promotion": False,
        "bridge_form_promotion_eligible": False,
        "human_observation": False,
    })

existing_evidence_ids = {record["evidence_id"] for record in wordweb["evidence_records"]}
assert not existing_evidence_ids & {record["evidence_id"] for record in new_evidence}

for sense in wordweb["senses"]:
    sense_id = sense["sense_id"]
    sense["reviewed_supporting_occurrence_evidence_ids"] = append_unique(
        sense.get("reviewed_supporting_occurrence_evidence_ids", []), support_by_sense[sense_id]
    )
    sense["reviewed_adverse_occurrence_evidence_ids"] = append_unique(
        sense.get("reviewed_adverse_occurrence_evidence_ids", []), adverse_by_sense[sense_id]
    )
    sense["reviewed_held_occurrence_evidence_ids"] = append_unique(
        sense.get("reviewed_held_occurrence_evidence_ids", []), held_by_sense[sense_id]
    )
    term_number = int(sense["term_id"][1:])
    if 11 <= term_number <= 20:
        if sense["term_id"] == "T11":
            sense["occurrence_review_status"] = "contiguous_T11_T20_review_complete_explicit_zero_hit"
        else:
            sense["occurrence_review_status"] = "contiguous_T11_T20_current_corpus_context_review_complete"

for core in wordweb["core_concepts"]:
    term_id = core["term_id"]
    term_number = int(term_id[1:])
    if not 11 <= term_number <= 20:
        continue
    block = core["reviewed_occurrence_evidence"]
    block["supporting_ids"] = append_unique(block.get("supporting_ids", []), support_by_term[term_id])
    block["adverse_ids"] = append_unique(block.get("adverse_ids", []), rejected_by_term[term_id])
    block["held_ids"] = append_unique(block.get("held_ids", []), held_by_term[term_id])
    block["supporting_count"] = len(block["supporting_ids"])
    block["adverse_count"] = len(block["adverse_ids"])
    block["held_count"] = len(block["held_ids"])
    block["zero_hit_current_corpus"] = term_id == "T11"
    block["scope"] = "contiguous_T01_T20_current_corpus_plus_opportunistic_RM_RG_T45_T57"
    block["form_promotions"] = 0
    block["human_observations"] = 0
    core["status"] = (
        "semantic_v6_contiguous_review_explicit_zero_hit_no_form_promotion"
        if term_id == "T11"
        else "semantic_v6_contiguous_review_no_form_promotion"
    )

for decision in wordweb["decisions"]:
    sense_id = decision["sense_id"]
    decision["reviewed_supporting_occurrence_evidence_ids"] = append_unique(
        decision.get("reviewed_supporting_occurrence_evidence_ids", []), support_by_sense[sense_id]
    )
    decision["reviewed_adverse_occurrence_evidence_ids"] = append_unique(
        decision.get("reviewed_adverse_occurrence_evidence_ids", []), adverse_by_sense[sense_id]
    )
    decision["reviewed_held_occurrence_evidence_ids"] = append_unique(
        decision.get("reviewed_held_occurrence_evidence_ids", []), held_by_sense[sense_id]
    )
    term_number = int(decision["term_id"][1:])
    if 11 <= term_number <= 20:
        decision["occurrence_review_status"] = (
            "explicit_zero_hit_current_corpus"
            if decision["term_id"] == "T11"
            else "T11_T20_context_reviewed_no_form_promotion"
        )
        decision["confidence_source_occurrence"] = "internal_context_review_only_not_human_attestation"

wordweb["artifact"] = "PAN_ROMANCE_WORDWEB_v6"
wordweb["supersedes_for_semantic_use"] = "PAN_ROMANCE_WORDWEB_v5"
wordweb["v5_retained_as"] = "preserved predecessor with audited T57 target and route-hash consistency defects; not rewritten"
wordweb["input_hashes"] = {
    "wordweb_v5_preserved": sha(WW5),
    "access_v5_preserved": sha(ACCESS5),
    "occurrence_review_T11_T20_v1": sha(REVIEW),
    "occurrence_review_T11_T20_summary_v1": sha(REVIEW_SUMMARY),
    "canonical_cohort_topology_v2": sha(COHORT_TREE),
    "MII_method_v6": sha(METHOD),
}
wordweb["boundary"] = (
    "The 120 inherited Spanish/French core records remain unresolved locator claims with zero quotations. "
    "Reviewed T01-T20 and RM-RG context records are a separate evidence layer; none promotes a form or supplies human data. "
    "V6 corrects the T57 adverse edge to algebraic right-action sense T57-S1."
)
wordweb["core_evidence_boundary"] = {
    "inherited_es_fr_core_records": 120,
    "inherited_core_quotation_count": 0,
    "inherited_core_acceptance": "unresolved_locator",
    "reviewed_occurrence_records": 230,
    "reviewed_supporting_status_events": 176,
    "reviewed_adverse_or_rejected_status_events": 44,
    "reviewed_held_status_events": 11,
    "status_event_counts_nonexclusive": True,
    "nonexclusive_reason": "One RM-RG occurrence supports ordinary-direction T57-S2 and is adverse to algebraic right-action T57-S1.",
    "contiguous_reviewed_terms": "T01-T20",
    "explicit_zero_hit_terms": ["T11"],
    "rm_rg_reviewed_occurrence_records": 2,
    "rm_rg_specialist_algebra_attestations": 0,
    "extension_context_to_core_promotions": 0,
    "core_form_promotions": 0,
    "human_observations": 0,
}
wordweb["occurrence_review_cursor"] = "T01_T20_complete; opportunistic_RM_RG_T45_T57_complete; next_contiguous_T21"
wordweb["evidence_records"].extend(new_evidence)
wordweb["evidence_record_count"] = len(wordweb["evidence_records"])
wordweb["relation_count"] = sum(len(core["relations"]) for core in wordweb["core_concepts"])
wordweb["relation_metrics"] = relation_metrics(wordweb)
wordweb["predecessor_v5_relation_metrics"] = {
    "relation_records": 402,
    "valid_target_id_edges": 27,
    "concept_to_sense_membership_edges": 106,
    "total_id_resolved_references_including_memberships": 133,
    "note": "These are the accurate v5 structural counts; 402 must not be described as 402 graph edges.",
}
wordweb["predecessor_v5_audit"] = {
    "status": "FAIL_semantic_and_hash_consistency",
    "report": "../_agent_reports/corpus_acceptance_reaudit_v5.md",
    "report_sha256": "3A611023472959D2AB2688D5B85D339FE3285CFD16A67682E66828779820A779",
    "resolved_in_v6": ["T57 adverse edge now targets T57-S1", "successor hash manifest will pin regenerated route ledger"],
}

assert wordweb["core_concept_count"] == 60 and wordweb["sense_count"] == 106
assert len(wordweb["decisions"]) == 106 and wordweb["evidence_record_count"] == 350
assert wordweb["relation_metrics"]["relation_records"] == wordweb["relation_count"] == 402
assert wordweb["relation_metrics"]["valid_target_id_edges"] == 27
assert wordweb["relation_metrics"]["total_id_resolved_references_including_memberships"] == 133
assert [core["forms"] for core in wordweb["core_concepts"]] == [core["forms"] for core in json.loads(WW5.read_text(encoding="utf-8"))["core_concepts"]]
assert wordweb["c2_extension_nodes"] == json.loads(WW5.read_text(encoding="utf-8"))["c2_extension_nodes"]
assert [decision["candidate_surfaces"] for decision in wordweb["decisions"]] == [decision["candidate_surfaces"] for decision in json.loads(WW5.read_text(encoding="utf-8"))["decisions"]]
assert wordweb["core_evidence_boundary"]["core_form_promotions"] == 0
assert wordweb["core_evidence_boundary"]["human_observations"] == 0
assert all(record["quote"] is None and record["acceptance"] == "unresolved_locator" for record in wordweb["evidence_records"][:120])
assert t57_edges[0]["target_id"] == "T57-S1"
WW6.write_text(json.dumps(wordweb, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

access6 = copy.deepcopy(access)
access6["artifact"] = "PAN_ROMANCE_ACCESS_LEDGER_v6"
access6["supersedes"] = "PAN_ROMANCE_ACCESS_LEDGER_v5"
access6["status"] = "sense_scoped_design_proxy_T01_T20_context_reviewed_zero_human_data"
access6["method"] = "MII_METHOD_v6"
access6["canonical_cohort_topology"] = {
    "artifact": cohort_tree["artifact"],
    "sha256": sha(COHORT_TREE),
    "cohort_ids": tree_cohort_ids,
    "cohort_count": 9,
}
access6["input_hashes"] = {
    "access_v5_preserved": sha(ACCESS5),
    "wordweb_v6": sha(WW6),
    "occurrence_review_T11_T20_v1": sha(REVIEW),
    "canonical_cohort_topology_v2": sha(COHORT_TREE),
    "MII_method_v6": sha(METHOD),
}
access6["claim_boundary"] = (
    "All numeric proxies are design diagnostics only. The canonical nine-cohort topology has zero human observations; "
    "no MII result feeds decisions and every row remains pilot-ineligible."
)
access6["human_observation_count"] = 0
access6["pilot_eligible_count"] = 0

for row in access6["rows"]:
    sense_id = row["sense_id"]
    supports = support_by_sense[sense_id]
    adverse = adverse_by_sense[sense_id]
    held = held_by_sense[sense_id]
    row["supporting_evidence_ids"] = append_string_ids(row.get("supporting_evidence_ids", ""), supports)
    row["reviewed_occurrence_support_ids"] = append_string_ids(row.get("reviewed_occurrence_support_ids", ""), supports)
    row["reviewed_occurrence_adverse_ids"] = append_string_ids(row.get("reviewed_occurrence_adverse_ids", ""), adverse)
    row["reviewed_occurrence_held_ids"] = append_string_ids(row.get("reviewed_occurrence_held_ids", ""), held)
    if adverse:
        row["adverse_evidence"] += " | reviewed adverse occurrence: " + ";".join(adverse)
    term_number = int(row["term_id"][1:])
    if 11 <= term_number <= 20:
        row["occurrence_review_status"] = (
            "T11_explicit_zero_hit_current_corpus"
            if row["term_id"] == "T11"
            else "T11_T20_context_reviewed_support_adverse_and_hold_separated"
        )
        row["review_status"] = "sense_scoped_design_proxy_context_reviewed_human_protocol_not_run"
    row["method_version"] = "MII_METHOD_v6"
    row["human_n"] = None
    row["human_correct"] = None
    row["human_incorrect"] = None
    row["human_abstain"] = None
    row["human_latency_ms"] = None
    row["human_confidence"] = None
    row["effect_interval"] = None
    row["pilot_eligible"] = False

access6["sense_count"] = 106
access6["row_count"] = len(access6["rows"])
assert access6["row_count"] == 106 * 9 == 954
assert [cohort["cohort_id"] for cohort in access6["cohorts"]] == tree_cohort_ids
assert not any(row["human_n"] is not None or row["pilot_eligible"] for row in access6["rows"])
assert all(not decision["candidate_surfaces"] for decision in wordweb["decisions"] if decision["term_id"] in {"T51", "T60"})
assert all(not decision["candidate_surfaces"] for decision in wordweb["decisions"] if decision["sense_id"] in {"T09-S1", "T10-S1", "T10-S2"})
ACCESS6_JSON.write_text(json.dumps(access6, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

fields = list(access6["rows"][0])
assert all(list(row) == fields for row in access6["rows"])
with ACCESS6_CSV.open("w", encoding="utf-8-sig", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=fields)
    writer.writeheader()
    for row in access6["rows"]:
        writer.writerow({
            key: "" if value is None else str(value).lower() if isinstance(value, bool) else value
            for key, value in row.items()
        })

lines = [
    "PASS core_concepts=60 senses=106 evidence_records=350",
    "relation_records=402 valid_target_id_edges=27 concept_sense_memberships=106 total_resolved_references=133",
    "T57_adverse_target=T57-S1",
    "T11_T20_reviewed_rows=111 accepted=90 rejected=10 held=11 explicit_zero_hit_T11=true",
    "access_rows=954 canonical_cohorts=9 human_observations=0 pilot_eligible=0",
    f"wordweb_v6_sha256={sha(WW6)}",
    f"access_v6_sha256={sha(ACCESS6_JSON)}",
]
LOG.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
