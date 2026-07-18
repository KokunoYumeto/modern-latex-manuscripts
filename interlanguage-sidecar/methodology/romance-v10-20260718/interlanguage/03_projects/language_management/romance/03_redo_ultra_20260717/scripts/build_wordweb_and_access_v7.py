from __future__ import annotations

import copy
import csv
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
ROMANCE = ROOT.parent
WW6 = ROOT / "wordweb" / "PAN_ROMANCE_WORDWEB_v6.json"
ACCESS6 = ROOT / "access" / "PAN_ROMANCE_ACCESS_LEDGER_v6.json"
REVIEW = ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_T21_T30_v1.csv"
REVIEW_SUMMARY = ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_T21_T30_v1.json"
REVIEW_PROTOCOL = ROOT / "wordweb" / "OCCURRENCE_REVIEW_PROTOCOL_v1.md"
COHORT_TREE = ROMANCE / "00_lane_control" / "ROMANCE_FAMILY_COHORT_TREE_v2.json"
METHOD = ROOT / "access" / "MII_METHOD_v7.md"
WW7 = ROOT / "wordweb" / "PAN_ROMANCE_WORDWEB_v7.json"
ACCESS7_JSON = ROOT / "access" / "PAN_ROMANCE_ACCESS_LEDGER_v7.json"
ACCESS7_CSV = ROOT / "access" / "PAN_ROMANCE_ACCESS_LEDGER_v7.csv"
LOG = ROOT / "qa" / "WORDWEB_ACCESS_BUILD_v7.log"

EXPECTED_HASHES = {
    "wordweb_v6": "0D4B581A2CE3F6664B1A97A44AAD023ED1FDC6C023FED5ADE42677E445751AD4",
    "access_v6": "E16E57953B3F8825554AB89E0B6A59E757C4BF40F2CE8B025AC384110E4D93E4",
    "review_T21_T30": "E40638A96D609FFDA89739D42F5AF77111A394353B6FF94754D42955BCA8F845",
    "review_T21_T30_summary": "84E6DAA9CD311D9D0B38D86D3CBA0B33415B464FE613D5A4CA9CC26B0FD6A2A6",
    "review_protocol_v1": "FE2433D34E77D04D5B74A009794FF2DDFD484C7A65DC667E4703EED8864F1D0D",
    "cohort_tree_v2": "9EBDEF5BE13B9BDBB0F1F2B718C2EE6583CF59F723C200E78668FC9CD9AD332C",
    "method_v7": "9AD6DCB1665EED04D5F081EC0581AB6AC7773545E3978E39516CECA6CF3DFEDF",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def read_csv(path: Path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def split_ids(value: str):
    return [item.strip() for item in (value or "").split(";") if item.strip()]


def append_unique(existing, additions):
    return list(dict.fromkeys(list(existing or []) + list(additions)))


def append_string_ids(existing: str, additions):
    return ";".join(append_unique(split_ids(existing or ""), additions))


def relation_metrics(wordweb):
    valid_ids = (
        {core["term_id"] for core in wordweb["core_concepts"]}
        | {sense["sense_id"] for sense in wordweb["senses"]}
        | {node["concept_id"] for node in wordweb["c2_extension_nodes"]}
    )
    relations = [relation for core in wordweb["core_concepts"] for relation in core["relations"]]
    valid_target_edges = sum(relation.get("target_id") in valid_ids for relation in relations)
    memberships = sum(len(core["sense_ids"]) for core in wordweb["core_concepts"])
    return {
        "relation_records": len(relations),
        "valid_target_id_edges": valid_target_edges,
        "relation_records_without_target_id": sum(not relation.get("target_id") for relation in relations),
        "concept_to_sense_membership_edges": memberships,
        "total_id_resolved_references_including_memberships": valid_target_edges + memberships,
        "reporting_boundary": "Relation records include descriptive/label relations without target IDs; they are not all graph edges.",
    }


for label, path in {
    "wordweb_v6": WW6,
    "access_v6": ACCESS6,
    "review_T21_T30": REVIEW,
    "review_T21_T30_summary": REVIEW_SUMMARY,
    "review_protocol_v1": REVIEW_PROTOCOL,
    "cohort_tree_v2": COHORT_TREE,
    "method_v7": METHOD,
}.items():
    assert sha(path) == EXPECTED_HASHES[label], (label, sha(path), EXPECTED_HASHES[label])

wordweb_v6 = json.loads(WW6.read_text(encoding="utf-8"))
access_v6 = json.loads(ACCESS6.read_text(encoding="utf-8"))
review = read_csv(REVIEW)
review_summary = json.loads(REVIEW_SUMMARY.read_text(encoding="utf-8"))
cohort_tree = json.loads(COHORT_TREE.read_text(encoding="utf-8"))

assert review_summary["review_manifest_sha256"] == sha(REVIEW)
assert review_summary["reviewed_against_wordweb_sha256"] == sha(WW6)
assert review_summary["reviewed_rows"] == len(review) == 131
assert review_summary["accepted_sense_matches"] == 64
assert review_summary["rejected_adverse_or_wrong_sense"] == 58
assert review_summary["held_rows"] == 9
assert review_summary["zero_accepted_sense_gaps"] == ["T22-S2", "T25-S2", "T26-S1"]
assert review_summary["narrow_language_coverage"] == {"T27-S1": ["es", "fr"], "T28-S1": ["es"]}
assert review_summary["bridge_form_promotions"] == review_summary["human_observations"] == 0
assert Counter(row["term_id"] for row in review) == Counter(
    {"T21": 6, "T22": 19, "T23": 12, "T24": 7, "T25": 14, "T26": 15, "T27": 14, "T28": 10, "T29": 18, "T30": 16}
)

expected_metrics = {
    "relation_records": 402,
    "valid_target_id_edges": 27,
    "relation_records_without_target_id": 375,
    "concept_to_sense_membership_edges": 106,
    "total_id_resolved_references_including_memberships": 133,
    "reporting_boundary": "Relation records include descriptive/label relations without target IDs; they are not all graph edges.",
}
assert relation_metrics(wordweb_v6) == expected_metrics
assert wordweb_v6["core_concept_count"] == 60
assert wordweb_v6["sense_count"] == len(wordweb_v6["senses"]) == 106
assert len(wordweb_v6["decisions"]) == 106
assert wordweb_v6["evidence_record_count"] == len(wordweb_v6["evidence_records"]) == 350
assert wordweb_v6["core_evidence_boundary"]["reviewed_occurrence_records"] == 230
assert wordweb_v6["core_evidence_boundary"]["reviewed_supporting_status_events"] == 176
assert wordweb_v6["core_evidence_boundary"]["reviewed_adverse_or_rejected_status_events"] == 44
assert wordweb_v6["core_evidence_boundary"]["reviewed_held_status_events"] == 11

tree_cohort_ids = [cohort["cohort_id"] for cohort in cohort_tree["reader_cohorts"]]
ledger_cohort_ids = [cohort["cohort_id"] for cohort in access_v6["cohorts"]]
assert cohort_tree["cohort_count"] == len(tree_cohort_ids) == len(set(tree_cohort_ids)) == 9
assert tree_cohort_ids == ledger_cohort_ids

t57 = next(core for core in wordweb_v6["core_concepts"] if core["term_id"] == "T57")
t57_edges = [
    relation
    for relation in t57["relations"]
    if relation["type"] == "corpus_adverse_evidence"
    and relation.get("target_label") == "straight_direction_not_algebraic_right_action"
]
assert len(t57_edges) == 1 and t57_edges[0]["target_id"] == "T57-S1"

wordweb = copy.deepcopy(wordweb_v6)
access = copy.deepcopy(access_v6)
sense_ids = {sense["sense_id"] for sense in wordweb["senses"]}
existing_evidence_ids = {record["evidence_id"] for record in wordweb["evidence_records"]}

support_by_sense = defaultdict(list)
adverse_by_sense = defaultdict(list)
held_by_sense = defaultdict(list)
support_by_term = defaultdict(list)
rejected_by_term = defaultdict(list)
held_by_term = defaultdict(list)
new_evidence = []

for row in review:
    term_number = int(row["term_id"][1:])
    assert 21 <= term_number <= 30
    evidence_id = "E-" + row["occurrence_id"]
    assert evidence_id not in existing_evidence_ids
    status = row["semantic_review_status"]
    support_senses = split_ids(row["reviewed_sense_ids"])
    adverse_senses = split_ids(row["adverse_to_sense_ids"])
    held_senses = split_ids(row["held_for_sense_ids"])
    assert set(support_senses + adverse_senses + held_senses) <= sense_ids

    if status == "accepted_sense_match":
        assert len(support_senses) == 1 and not adverse_senses and not held_senses
        support_by_sense[support_senses[0]].append(evidence_id)
        support_by_term[row["term_id"]].append(evidence_id)
    elif status == "rejected_adverse_or_wrong_sense":
        assert not support_senses and not held_senses
        for sense_id in adverse_senses:
            adverse_by_sense[sense_id].append(evidence_id)
        rejected_by_term[row["term_id"]].append(evidence_id)
    else:
        assert status == "held_insufficient_context_or_unmodeled_sense"
        assert not support_senses and not adverse_senses and held_senses
        for sense_id in held_senses:
            held_by_sense[sense_id].append(evidence_id)
        held_by_term[row["term_id"]].append(evidence_id)

    assert row["bridge_form_promotion_eligible"].lower() == "false"
    assert row["human_observation"].lower() == "false"
    new_evidence.append(
        {
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
        }
    )

assert len(new_evidence) == len({record["evidence_id"] for record in new_evidence}) == 131

gap_senses = set(review_summary["zero_accepted_sense_gaps"])
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
    if 21 <= term_number <= 30:
        sense["occurrence_review_status"] = (
            "contiguous_T21_T30_review_complete_zero_accepted_support"
            if sense_id in gap_senses
            else "contiguous_T21_T30_current_corpus_context_review_complete"
        )

for core in wordweb["core_concepts"]:
    term_id = core["term_id"]
    term_number = int(term_id[1:])
    if not 21 <= term_number <= 30:
        continue
    block = core["reviewed_occurrence_evidence"]
    block["supporting_ids"] = append_unique(block.get("supporting_ids", []), support_by_term[term_id])
    block["adverse_ids"] = append_unique(block.get("adverse_ids", []), rejected_by_term[term_id])
    block["held_ids"] = append_unique(block.get("held_ids", []), held_by_term[term_id])
    block["supporting_count"] = len(block["supporting_ids"])
    block["adverse_count"] = len(block["adverse_ids"])
    block["held_count"] = len(block["held_ids"])
    block["zero_hit_current_corpus"] = False
    block["zero_accepted_sense_ids"] = [sense_id for sense_id in core["sense_ids"] if sense_id in gap_senses]
    block["scope"] = "contiguous_T01_T30_current_corpus_plus_opportunistic_RM_RG_T45_T57"
    block["form_promotions"] = 0
    block["human_observations"] = 0
    core["status"] = "semantic_v7_contiguous_review_no_form_promotion"

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
    if 21 <= term_number <= 30:
        decision["occurrence_review_status"] = (
            "T21_T30_context_reviewed_zero_accepted_support"
            if sense_id in gap_senses
            else "T21_T30_context_reviewed_support_adverse_and_hold_separated"
        )
        decision["confidence_source_occurrence"] = "internal_context_review_only_not_human_attestation"

wordweb["artifact"] = "PAN_ROMANCE_WORDWEB_v7"
wordweb["supersedes_for_semantic_use"] = "PAN_ROMANCE_WORDWEB_v6"
wordweb["v6_retained_as"] = "preserved predecessor with contiguous T01-T20 review; not rewritten"
wordweb["input_hashes"] = {
    "wordweb_v6_preserved": sha(WW6),
    "access_v6_preserved": sha(ACCESS6),
    "occurrence_review_T21_T30_v1": sha(REVIEW),
    "occurrence_review_T21_T30_summary_v1": sha(REVIEW_SUMMARY),
    "occurrence_review_protocol_v1": sha(REVIEW_PROTOCOL),
    "canonical_cohort_topology_v2": sha(COHORT_TREE),
    "MII_method_v7": sha(METHOD),
}
wordweb["boundary"] = (
    "The 120 inherited Spanish/French core records remain unresolved locator claims with zero quotations. "
    "The separate reviewed occurrence layer now covers contiguous T01-T30 plus opportunistic RM-RG T45/T57. "
    "No reviewed context promotes a form or supplies human data; rejected/adverse and held evidence remains explicit."
)
wordweb["core_evidence_boundary"] = {
    "inherited_es_fr_core_records": 120,
    "inherited_core_quotation_count": 0,
    "inherited_core_acceptance": "unresolved_locator",
    "reviewed_occurrence_records": 361,
    "reviewed_supporting_status_events": 240,
    "reviewed_adverse_or_rejected_status_events": 102,
    "reviewed_held_status_events": 20,
    "status_event_counts_nonexclusive": True,
    "nonexclusive_reason": "One RM-RG occurrence supports ordinary-direction T57-S2 and is adverse to algebraic right-action T57-S1.",
    "contiguous_reviewed_terms": "T01-T30",
    "explicit_zero_hit_terms": ["T11"],
    "zero_accepted_sense_gaps_T21_T30": ["T22-S2", "T25-S2", "T26-S1"],
    "narrow_accepted_language_coverage": {"T27-S1": ["es", "fr"], "T28-S1": ["es"]},
    "rm_rg_reviewed_occurrence_records": 2,
    "rm_rg_specialist_algebra_attestations": 0,
    "extension_context_to_core_promotions": 0,
    "core_form_promotions": 0,
    "human_observations": 0,
}
wordweb["occurrence_review_cursor"] = "T01_T30_complete; opportunistic_RM_RG_T45_T57_complete; next_contiguous_T31"
wordweb["evidence_records"].extend(new_evidence)
wordweb["evidence_record_count"] = len(wordweb["evidence_records"])
wordweb["relation_count"] = sum(len(core["relations"]) for core in wordweb["core_concepts"])
wordweb["relation_metrics"] = relation_metrics(wordweb)
wordweb["predecessor_v6_relation_metrics"] = {
    "relation_records": 402,
    "valid_target_id_edges": 27,
    "concept_to_sense_membership_edges": 106,
    "total_id_resolved_references_including_memberships": 133,
    "note": "The relation inventory is unchanged; descriptive records without target IDs are not graph edges.",
}

assert wordweb["core_concept_count"] == 60 and wordweb["sense_count"] == 106
assert len(wordweb["decisions"]) == 106 and wordweb["evidence_record_count"] == 481
assert wordweb["relation_metrics"] == expected_metrics
assert wordweb["relation_count"] == 402
assert [core["forms"] for core in wordweb["core_concepts"]] == [core["forms"] for core in wordweb_v6["core_concepts"]]
assert wordweb["c2_extension_nodes"] == wordweb_v6["c2_extension_nodes"]
assert [decision["candidate_surfaces"] for decision in wordweb["decisions"]] == [
    decision["candidate_surfaces"] for decision in wordweb_v6["decisions"]
]
assert wordweb["core_evidence_boundary"]["core_form_promotions"] == 0
assert wordweb["core_evidence_boundary"]["human_observations"] == 0
assert all(record["quote"] is None and record["acceptance"] == "unresolved_locator" for record in wordweb["evidence_records"][:120])
assert sum(core["reviewed_occurrence_evidence"].get("supporting_count", 0) for core in wordweb["core_concepts"]) == 240
assert sum(core["reviewed_occurrence_evidence"].get("adverse_count", 0) for core in wordweb["core_concepts"]) == 102
assert sum(core["reviewed_occurrence_evidence"].get("held_count", 0) for core in wordweb["core_concepts"]) == 20
assert t57_edges[0]["target_id"] == "T57-S1"
assert all(
    not next(decision for decision in wordweb["decisions"] if decision["sense_id"] == sense_id)["candidate_surfaces"]
    for sense_id in ["T22-S2", "T25-S2"]
)
t26_s1_decision = next(decision for decision in wordweb["decisions"] if decision["sense_id"] == "T26-S1")
assert t26_s1_decision["candidate_surfaces"] == ["Galois"]
assert "not_promoted" in t26_s1_decision["construction_status"]
assert t26_s1_decision["confidence_bridge_decision"] == "hypothesis_only"
WW7.write_text(json.dumps(wordweb, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

access["artifact"] = "PAN_ROMANCE_ACCESS_LEDGER_v7"
access["supersedes"] = "PAN_ROMANCE_ACCESS_LEDGER_v6"
access["status"] = "sense_scoped_design_proxy_T01_T30_context_reviewed_zero_human_data"
access["method"] = "MII_METHOD_v7"
access["canonical_cohort_topology"] = {
    "artifact": cohort_tree["artifact"],
    "sha256": sha(COHORT_TREE),
    "cohort_ids": tree_cohort_ids,
    "cohort_count": 9,
}
access["input_hashes"] = {
    "access_v6_preserved": sha(ACCESS6),
    "wordweb_v7": sha(WW7),
    "occurrence_review_T21_T30_v1": sha(REVIEW),
    "occurrence_review_T21_T30_summary_v1": sha(REVIEW_SUMMARY),
    "occurrence_review_protocol_v1": sha(REVIEW_PROTOCOL),
    "canonical_cohort_topology_v2": sha(COHORT_TREE),
    "MII_method_v7": sha(METHOD),
}
access["claim_boundary"] = (
    "All numeric proxies are design diagnostics only. The canonical nine-cohort topology has zero human observations; "
    "no MII result promotes a form or feeds decisions and every row remains pilot-ineligible."
)
access["human_observation_count"] = 0
access["pilot_eligible_count"] = 0

for row in access["rows"]:
    sense_id = row["sense_id"]
    supports = support_by_sense[sense_id]
    adverse = adverse_by_sense[sense_id]
    held = held_by_sense[sense_id]
    row["supporting_evidence_ids"] = append_string_ids(row.get("supporting_evidence_ids", ""), supports)
    row["reviewed_occurrence_support_ids"] = append_string_ids(row.get("reviewed_occurrence_support_ids", ""), supports)
    row["reviewed_occurrence_adverse_ids"] = append_string_ids(row.get("reviewed_occurrence_adverse_ids", ""), adverse)
    row["reviewed_occurrence_held_ids"] = append_string_ids(row.get("reviewed_occurrence_held_ids", ""), held)
    if adverse:
        row["adverse_evidence"] = (row.get("adverse_evidence") or "") + " | reviewed adverse occurrence: " + ";".join(adverse)
    term_number = int(row["term_id"][1:])
    if 21 <= term_number <= 30:
        row["occurrence_review_status"] = (
            "T21_T30_context_reviewed_zero_accepted_support"
            if sense_id in gap_senses
            else "T21_T30_context_reviewed_support_adverse_and_hold_separated"
        )
        row["review_status"] = "sense_scoped_design_proxy_context_reviewed_human_protocol_not_run"
    row["method_version"] = "MII_METHOD_v7"
    row["human_n"] = None
    row["human_correct"] = None
    row["human_incorrect"] = None
    row["human_abstain"] = None
    row["human_latency_ms"] = None
    row["human_confidence"] = None
    row["effect_interval"] = None
    row["pilot_eligible"] = False

access["sense_count"] = 106
access["row_count"] = len(access["rows"])
assert access["row_count"] == 106 * 9 == 954
assert [cohort["cohort_id"] for cohort in access["cohorts"]] == tree_cohort_ids
assert Counter(row["sense_id"] for row in access["rows"]) == Counter({sense_id: 9 for sense_id in sense_ids})
assert not any(
    row["human_n"] is not None
    or row["human_correct"] is not None
    or row["human_incorrect"] is not None
    or row["human_abstain"] is not None
    or row["human_latency_ms"] is not None
    or row["human_confidence"] is not None
    or row["effect_interval"] is not None
    or row["pilot_eligible"]
    for row in access["rows"]
)
assert all(row["method_version"] == "MII_METHOD_v7" for row in access["rows"])
ACCESS7_JSON.write_text(json.dumps(access, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

fields = list(access["rows"][0])
assert all(list(row) == fields for row in access["rows"])
with ACCESS7_CSV.open("w", encoding="utf-8-sig", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=fields)
    writer.writeheader()
    for row in access["rows"]:
        writer.writerow(
            {
                key: "" if value is None else str(value).lower() if isinstance(value, bool) else value
                for key, value in row.items()
            }
        )

lines = [
    "PASS core_concepts=60 senses=106 evidence_records=481",
    "relation_records=402 valid_target_id_edges=27 concept_sense_memberships=106 total_resolved_references=133",
    "T57_adverse_target=T57-S1",
    "reviewed_occurrence_records=361 accepted_support_events=240 rejected_adverse_events=102 held_events=20",
    "contiguous_review=T01-T30 next=T31",
    "zero_accepted_sense_gaps=T22-S2,T25-S2,T26-S1 narrow_T27=es,fr narrow_T28=es",
    "access_rows=954 canonical_cohorts=9 human_observations=0 pilot_eligible=0 form_promotions=0",
    f"review_protocol_v1_sha256={sha(REVIEW_PROTOCOL)}",
    f"wordweb_v7_sha256={sha(WW7)}",
    f"access_v7_json_sha256={sha(ACCESS7_JSON)}",
    f"access_v7_csv_sha256={sha(ACCESS7_CSV)}",
]
LOG.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
