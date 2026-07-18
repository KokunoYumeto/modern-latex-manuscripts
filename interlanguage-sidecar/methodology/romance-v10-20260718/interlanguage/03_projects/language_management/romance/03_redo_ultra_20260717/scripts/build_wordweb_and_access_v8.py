from __future__ import annotations

import copy
import csv
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
ROMANCE = ROOT.parent

WW7 = ROOT / "wordweb" / "PAN_ROMANCE_WORDWEB_v7.json"
ACCESS7 = ROOT / "access" / "PAN_ROMANCE_ACCESS_LEDGER_v7.json"
REVIEW = ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_T31_T40_v1.csv"
REVIEW_SUMMARY = ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_T31_T40_v1.json"
REVIEW_BUILDER = ROOT / "scripts" / "review_occurrences_t31_t40_v1.py"
REVIEW_PROTOCOL = ROOT / "wordweb" / "OCCURRENCE_REVIEW_PROTOCOL_v1.md"
FROZEN_OCCURRENCES = ROOT / "wordweb" / "ROMANCE_TERM_OCCURRENCES_v1.csv"
CURATED_MANIFEST = ROOT / "corpus" / "CURATED_EXTERNAL_SOURCE_MANIFEST_v2.csv"
COHORT_TREE = ROMANCE / "00_lane_control" / "ROMANCE_FAMILY_COHORT_TREE_v2.json"
METHOD = ROOT / "access" / "MII_METHOD_v8.md"

WW8 = ROOT / "wordweb" / "PAN_ROMANCE_WORDWEB_v8.json"
ACCESS8_JSON = ROOT / "access" / "PAN_ROMANCE_ACCESS_LEDGER_v8.json"
ACCESS8_CSV = ROOT / "access" / "PAN_ROMANCE_ACCESS_LEDGER_v8.csv"
LOG = ROOT / "qa" / "WORDWEB_ACCESS_BUILD_v8.log"

EXPECTED_HASHES = {
    "wordweb_v7": "A48BF8C89F252A0274D2FDE2FE8A2E6E6E3077AD81A4B60BFA0B5FFF44A1A366",
    "access_v7": "881034D4E707D89C55DCB1B4E4871DD3F2F317776463AF2A19108153B2CBD8FF",
    "review_T31_T40": "8F98D501A79E5902AF5A54BD563F069B899E7CFDED587A9D7192EFA8F4B99D25",
    "review_T31_T40_summary": "35DF1CCBE700DEF3D00298DD04D5DD48BD6E0886AAA74035BF923FB35B6C1074",
    "review_T31_T40_builder": "822D3C9EEDEE4176BA923CA804BC4AEDD3074681EC320F27869CF516C3AC6CFA",
    "review_protocol_v1": "2F41284AEF9C950E39384ED245DC9BA274507D90DE59B4C0F030119C7776C450",
    "frozen_occurrence_table_v1": "6DF8FAD570D48369CA0A8FE06CD5A0EBC3C21275677E35BEDCF077208865DEE8",
    "curated_external_source_manifest_v2": "3870079115BC397FC765D05A41B49920FF786B795096B64912F6371F12B7C62F",
    "cohort_tree_v2": "9EBDEF5BE13B9BDBB0F1F2B718C2EE6583CF59F723C200E78668FC9CD9AD332C",
    "method_v8": "C384D0E7EA12577A7BB2D232C5B1870579AC3EB7F2E2B69692C187B8395193A4",
}

INPUT_PATHS = {
    "wordweb_v7": WW7,
    "access_v7": ACCESS7,
    "review_T31_T40": REVIEW,
    "review_T31_T40_summary": REVIEW_SUMMARY,
    "review_T31_T40_builder": REVIEW_BUILDER,
    "review_protocol_v1": REVIEW_PROTOCOL,
    "frozen_occurrence_table_v1": FROZEN_OCCURRENCES,
    "curated_external_source_manifest_v2": CURATED_MANIFEST,
    "cohort_tree_v2": COHORT_TREE,
    "method_v8": METHOD,
}

EXPECTED_NEW_COUNTS = {"accepted": 63, "rejected": 8, "held": 12}
EXPECTED_CUMULATIVE_COUNTS = {
    "reviewed_occurrence_records": 444,
    "accepted": 303,
    "rejected": 110,
    "held": 32,
}
EXPECTED_ZERO_ACCEPTED_SENSES = [
    "T31-S2",
    "T31-S3",
    "T33-S1",
    "T33-S3",
    "T34-S1",
    "T35-S1",
    "T35-S3",
    "T37-S2",
]
NEW_RM_2024_SOURCE_IDS = [
    "CURATED-RM-RG-GRCH-AP1G-2024-M1",
    "CURATED-RM-RG-GRCH-AP1G-2024-M2",
]
EXPECTED_LABEL_CONTRACT = {
    "T51-S1": "function_domain",
    "T51-S2": "integral_domain",
    "T51-S3": "generic_domain_or_region",
    "T51-S4": "coefficient_domain_linkage",
    "T60-S1": "neutral_or_identity_element",
    "T60-S2": "identity_map",
    "T60-S3": "algebraic_identity",
    "T60-S4": "unit_or_invertible_element",
}


class InvalidRelationTargetError(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def split_ids(value: str) -> list[str]:
    return [
        item.strip()
        for item in (value or "").replace("|", ";").split(";")
        if item.strip()
    ]


def append_unique(existing, additions):
    return list(dict.fromkeys(list(existing or []) + list(additions)))


def append_string_ids(existing: str, additions) -> str:
    return ";".join(append_unique(split_ids(existing or ""), additions))


def valid_graph_ids(wordweb: dict) -> set[str]:
    return (
        {core["term_id"] for core in wordweb["core_concepts"]}
        | {sense["sense_id"] for sense in wordweb["senses"]}
        | {node["concept_id"] for node in wordweb["c2_extension_nodes"]}
    )


def relation_metrics(wordweb: dict) -> dict:
    valid_ids = valid_graph_ids(wordweb)
    relation_records = []
    invalid = []
    for core in wordweb["core_concepts"]:
        for index, relation in enumerate(core["relations"]):
            relation_records.append(relation)
            target_id = relation.get("target_id")
            if target_id and target_id not in valid_ids:
                invalid.append(
                    {
                        "term_id": core["term_id"],
                        "relation_index": index,
                        "relation_type": relation.get("type"),
                        "target_id": target_id,
                    }
                )
    if invalid:
        raise InvalidRelationTargetError(
            "invalid nonempty relation target IDs: "
            + json.dumps(invalid, ensure_ascii=False, sort_keys=True)
        )
    valid_target_edges = sum(
        bool(relation.get("target_id")) for relation in relation_records
    )
    memberships = sum(
        len(core["sense_ids"]) for core in wordweb["core_concepts"]
    )
    return {
        "relation_records": len(relation_records),
        "valid_target_id_edges": valid_target_edges,
        "invalid_target_id_edges": 0,
        "relation_records_without_target_id": sum(
            not relation.get("target_id") for relation in relation_records
        ),
        "concept_to_sense_membership_edges": memberships,
        "total_id_resolved_references_including_memberships": (
            valid_target_edges + memberships
        ),
        "reporting_boundary": (
            "Relation records include descriptive/label relations without "
            "target IDs; they are not all graph edges. Any nonempty invalid "
            "target ID is a build error."
        ),
    }


def negative_relation_target_test(wordweb: dict) -> bool:
    probe = copy.deepcopy(wordweb)
    injected = False
    for core in probe["core_concepts"]:
        for relation in core["relations"]:
            if not relation.get("target_id"):
                relation["target_id"] = "__INVALID_RELATION_TARGET_PROBE__"
                injected = True
                break
        if injected:
            break
    require(injected, "could not construct invalid-target negative test")
    try:
        relation_metrics(probe)
    except InvalidRelationTargetError:
        return True
    return False


def semantic_signature(sense: dict):
    return (
        sense["sense_id"],
        sense["term_id"],
        sense["sense_label"],
        sense["definition"],
        tuple(sense.get("domain_clusters", [])),
        tuple(sense.get("inclusions", [])),
        tuple(sense.get("exclusions", [])),
    )


for label, path in INPUT_PATHS.items():
    actual = sha(path)
    require(
        actual == EXPECTED_HASHES[label],
        f"input hash mismatch for {label}: {actual} != "
        f"{EXPECTED_HASHES[label]}",
    )

wordweb_v7 = json.loads(WW7.read_text(encoding="utf-8"))
access_v7 = json.loads(ACCESS7.read_text(encoding="utf-8"))
review = read_csv(REVIEW)
review_summary = json.loads(REVIEW_SUMMARY.read_text(encoding="utf-8"))
frozen_occurrences = read_csv(FROZEN_OCCURRENCES)
curated_manifest = read_csv(CURATED_MANIFEST)
cohort_tree = json.loads(COHORT_TREE.read_text(encoding="utf-8"))
review_protocol = REVIEW_PROTOCOL.read_text(encoding="utf-8")

for required_protocol_text in (
    "contiguously through T01–T40",
    "the next contiguous cursor is T41",
    "Human-observation count, form-promotion count, and pilot-claim",
    "count are all zero",
    EXPECTED_HASHES["frozen_occurrence_table_v1"],
):
    require(
        required_protocol_text in review_protocol,
        f"review protocol is missing required v8 boundary: "
        f"{required_protocol_text}",
    )

require(
    review_summary["artifact"] == "ROMANCE_OCCURRENCE_REVIEW_T31_T40_v1",
    "wrong review summary artifact",
)
require(
    review_summary["counts"]
    == {
        "source_rows": 83,
        "accepted": 63,
        "rejected": 8,
        "held": 12,
        "accepted_navigation_lexical": 4,
        "accepted_running_body_context": 59,
    },
    "unexpected review summary counts",
)
require(len(review) == 83, "review CSV must contain exactly 83 rows")
require(
    len({row["occurrence_id"] for row in review}) == 83,
    "review CSV occurrence IDs must be unique",
)
require(
    review_summary["zero_accepted_senses"]
    == EXPECTED_ZERO_ACCEPTED_SENSES,
    "unexpected T31-T40 zero-accepted-sense list",
)
require(
    review_summary["boundary"]["form_promotion_count"] == 0
    and review_summary["boundary"]["human_observation_count"] == 0
    and review_summary["boundary"]["pilot_or_intelligibility_claim_count"]
    == 0,
    "review summary boundary leak",
)
require(
    review_summary["input_hashes"]["ROMANCE_TERM_OCCURRENCES_v1.csv"]
    == sha(FROZEN_OCCURRENCES),
    "review summary does not pin frozen occurrence table",
)
require(
    review_summary["input_hashes"]["PAN_ROMANCE_WORDWEB_v7.json"]
    == sha(WW7),
    "review summary does not pin v7",
)

frozen_scope = [
    row
    for row in frozen_occurrences
    if 31 <= int(row["term_id"][1:]) <= 40
]
require(len(frozen_scope) == 83, "frozen T31-T40 occurrence count changed")
require(
    {row["occurrence_id"] for row in frozen_scope}
    == {row["occurrence_id"] for row in review},
    "review IDs do not exactly equal frozen T31-T40 source IDs",
)
frozen_text = FROZEN_OCCURRENCES.read_text(encoding="utf-8-sig")
for source_id in NEW_RM_2024_SOURCE_IDS:
    require(
        source_id not in frozen_text,
        f"frozen occurrence table unexpectedly contains {source_id}",
    )
curated_by_id = {row["source_id"]: row for row in curated_manifest}
for source_id in NEW_RM_2024_SOURCE_IDS:
    require(source_id in curated_by_id, f"missing curated source {source_id}")
    require(
        curated_by_id[source_id]["publication_date"] == "2024"
        and curated_by_id[source_id]["language"] == "rm",
        f"curated source boundary mismatch for {source_id}",
    )

expected_predecessor_metrics = {
    "relation_records": 402,
    "valid_target_id_edges": 27,
    "invalid_target_id_edges": 0,
    "relation_records_without_target_id": 375,
    "concept_to_sense_membership_edges": 106,
    "total_id_resolved_references_including_memberships": 133,
    "reporting_boundary": (
        "Relation records include descriptive/label relations without "
        "target IDs; they are not all graph edges. Any nonempty invalid "
        "target ID is a build error."
    ),
}
require(
    relation_metrics(wordweb_v7) == expected_predecessor_metrics,
    "v7 relation inventory mismatch",
)
relation_negative_test_passed = negative_relation_target_test(wordweb_v7)
require(relation_negative_test_passed, "invalid target negative test failed")

require(
    wordweb_v7["core_concept_count"] == 60
    and len(wordweb_v7["core_concepts"]) == 60,
    "v7 core-concept count mismatch",
)
require(
    wordweb_v7["sense_count"] == len(wordweb_v7["senses"]) == 106,
    "v7 sense count mismatch",
)
require(len(wordweb_v7["decisions"]) == 106, "v7 decision count mismatch")
require(
    wordweb_v7["evidence_record_count"]
    == len(wordweb_v7["evidence_records"])
    == 481,
    "v7 evidence count mismatch",
)
require(
    wordweb_v7["core_evidence_boundary"]["reviewed_occurrence_records"]
    == 361,
    "v7 reviewed occurrence count mismatch",
)
require(
    wordweb_v7["core_evidence_boundary"][
        "reviewed_supporting_status_events"
    ]
    == 240
    and wordweb_v7["core_evidence_boundary"][
        "reviewed_adverse_or_rejected_status_events"
    ]
    == 102
    and wordweb_v7["core_evidence_boundary"][
        "reviewed_held_status_events"
    ]
    == 20,
    "v7 cumulative status counts mismatch",
)

tree_cohort_ids = [
    cohort["cohort_id"] for cohort in cohort_tree["reader_cohorts"]
]
ledger_cohort_ids = [
    cohort["cohort_id"] for cohort in access_v7["cohorts"]
]
require(
    cohort_tree["cohort_count"]
    == len(tree_cohort_ids)
    == len(set(tree_cohort_ids))
    == 9,
    "canonical cohort topology mismatch",
)
require(
    tree_cohort_ids == ledger_cohort_ids,
    "v7 ledger cohort IDs do not match canonical topology",
)

sense_label_by_id = {
    sense["sense_id"]: sense["sense_label"] for sense in wordweb_v7["senses"]
}
require(
    {
        sense_id: sense_label_by_id[sense_id]
        for sense_id in EXPECTED_LABEL_CONTRACT
    }
    == EXPECTED_LABEL_CONTRACT,
    "T51/T60 exact sense-label contract mismatch",
)

t57 = next(
    core for core in wordweb_v7["core_concepts"] if core["term_id"] == "T57"
)
t57_edges = [
    relation
    for relation in t57["relations"]
    if relation["type"] == "corpus_adverse_evidence"
    and relation.get("target_label")
    == "straight_direction_not_algebraic_right_action"
]
require(
    len(t57_edges) == 1 and t57_edges[0]["target_id"] == "T57-S1",
    "T57 adverse relation target mismatch",
)

wordweb = copy.deepcopy(wordweb_v7)
access = copy.deepcopy(access_v7)
sense_ids = {sense["sense_id"] for sense in wordweb["senses"]}
existing_evidence_ids = {
    record["evidence_id"] for record in wordweb["evidence_records"]
}

support_by_sense = defaultdict(list)
adverse_by_sense = defaultdict(list)
held_by_sense = defaultdict(list)
lexical_by_sense = defaultdict(list)
body_by_sense = defaultdict(list)
support_by_term = defaultdict(list)
rejected_by_term = defaultdict(list)
held_by_term = defaultdict(list)
lexical_by_term = defaultdict(list)
body_by_term = defaultdict(list)
new_evidence = []

new_category_counts = Counter()
for row in review:
    term_number = int(row["term_id"][1:])
    require(31 <= term_number <= 40, "review row outside T31-T40")
    evidence_id = "E-" + row["occurrence_id"]
    require(
        evidence_id not in existing_evidence_ids,
        f"evidence ID collision: {evidence_id}",
    )
    status = row["review_decision"]
    support_senses = split_ids(row["accepted_sense_id"])
    held_senses = split_ids(row["candidate_sense_ids"])
    adverse_target = row["adverse_target"].strip()
    adverse_senses = [adverse_target] if adverse_target in sense_ids else []
    require(
        set(support_senses + adverse_senses + held_senses) <= sense_ids,
        f"unknown reviewed sense in {row['occurrence_id']}",
    )

    if status == "accepted_sense_match":
        new_category_counts["accepted"] += 1
        require(
            len(support_senses) == 1
            and not adverse_senses
            and not held_senses,
            f"invalid accepted row {row['occurrence_id']}",
        )
        support_by_sense[support_senses[0]].append(evidence_id)
        support_by_term[row["term_id"]].append(evidence_id)
        if (
            row["evidence_context_class"]
            == "navigation_lexical_match_internal"
        ):
            lexical_by_sense[support_senses[0]].append(evidence_id)
            lexical_by_term[row["term_id"]].append(evidence_id)
        else:
            require(
                row["evidence_context_class"]
                == "running_body_semantic_match_internal",
                f"unexpected accepted context class {row['occurrence_id']}",
            )
            body_by_sense[support_senses[0]].append(evidence_id)
            body_by_term[row["term_id"]].append(evidence_id)
    elif status.startswith("rejected_"):
        new_category_counts["rejected"] += 1
        require(
            not support_senses and not held_senses,
            f"invalid rejected row {row['occurrence_id']}",
        )
        for sense_id in adverse_senses:
            adverse_by_sense[sense_id].append(evidence_id)
        rejected_by_term[row["term_id"]].append(evidence_id)
    else:
        require(status == "held", f"unknown review status {status}")
        new_category_counts["held"] += 1
        require(
            not support_senses
            and not adverse_senses
            and len(held_senses) == 1,
            f"invalid held row {row['occurrence_id']}",
        )
        for sense_id in held_senses:
            held_by_sense[sense_id].append(evidence_id)
        held_by_term[row["term_id"]].append(evidence_id)
        require(
            bool(row["evidence_family_id"]),
            f"held family identity missing {row['occurrence_id']}",
        )

    require(
        row["promotion_status"] == "not_promoted",
        f"promotion leak {row['occurrence_id']}",
    )
    require(
        int(row["human_observation_count"]) == 0,
        f"human observation leak {row['occurrence_id']}",
    )
    require(
        row["pilot_claim"].lower() == "false",
        f"pilot claim leak {row['occurrence_id']}",
    )
    require(
        hashlib.sha256(row["quote"].encode("utf-8")).hexdigest().upper()
        == row["quote_sha256"],
        f"quote hash mismatch {row['occurrence_id']}",
    )
    body_status = (
        "lexical_navigation_only_not_body_attestation"
        if row["evidence_context_class"]
        == "navigation_lexical_match_internal"
        else (
            "internally_reviewed_running_body_context_not_human_attestation"
            if row["evidence_context_class"]
            == "running_body_semantic_match_internal"
            else "not_accepted_body_attestation"
        )
    )
    new_evidence.append(
        {
            "evidence_id": evidence_id,
            "occurrence_id": row["occurrence_id"],
            "term_id": row["term_id"],
            "reviewed_supporting_sense_ids": support_senses,
            "reviewed_adverse_to_sense_ids": adverse_senses,
            "reviewed_held_for_sense_ids": held_senses,
            "adverse_target": adverse_target or None,
            "language": row["language"],
            "source_type": (
                "reviewed_frozen_v1_occurrence_context_or_lexical_label"
            ),
            "origin_layer": (
                "frozen_v1_consolidated_corpus_occurrence_not_inherited_core"
                "_and_not_new_2024_RM_sources"
            ),
            "logical_source_id": row["logical_source_id"],
            "record_id": row["record_id"],
            "source_sha256": row["source_sha256"],
            "license_status": row["license_status"],
            "locator": f"{row['locator_path']}:{row['line_number']}",
            "quote": row["quote"],
            "quote_sha256": row["quote_sha256"],
            "acceptance": status,
            "review_reason_code": row["reason_code"],
            "review_note": row["review_note"],
            "review_tier": row["review_authority"],
            "evidence_context_class": row["evidence_context_class"],
            "body_attestation_status": body_status,
            "evidence_family_id": row["evidence_family_id"] or None,
            "family_role": row["family_role"] or None,
            "cross_occurrence_id": row["cross_occurrence_id"] or None,
            "review_report": row["review_report"],
            "review_report_sha256": row["review_report_sha256"],
            "core_form_promotion": False,
            "bridge_form_promotion_eligible": False,
            "human_observation": False,
            "pilot_claim": False,
        }
    )

require(
    dict(new_category_counts) == EXPECTED_NEW_COUNTS,
    f"new review count mismatch: {dict(new_category_counts)}",
)
require(
    len(new_evidence)
    == len({record["evidence_id"] for record in new_evidence})
    == 83,
    "new evidence IDs must be 83 and unique",
)
require(
    not (
        {record["logical_source_id"] for record in new_evidence}
        & set(NEW_RM_2024_SOURCE_IDS)
    ),
    "new 2024 Romansh sources leaked into frozen review evidence",
)

gap_senses = set(EXPECTED_ZERO_ACCEPTED_SENSES)
for sense in wordweb["senses"]:
    sense_id = sense["sense_id"]
    sense["reviewed_supporting_occurrence_evidence_ids"] = append_unique(
        sense.get("reviewed_supporting_occurrence_evidence_ids", []),
        support_by_sense[sense_id],
    )
    sense["reviewed_adverse_occurrence_evidence_ids"] = append_unique(
        sense.get("reviewed_adverse_occurrence_evidence_ids", []),
        adverse_by_sense[sense_id],
    )
    sense["reviewed_held_occurrence_evidence_ids"] = append_unique(
        sense.get("reviewed_held_occurrence_evidence_ids", []),
        held_by_sense[sense_id],
    )
    sense["reviewed_lexical_navigation_occurrence_evidence_ids"] = (
        append_unique(
            sense.get(
                "reviewed_lexical_navigation_occurrence_evidence_ids", []
            ),
            lexical_by_sense[sense_id],
        )
    )
    sense["reviewed_running_body_occurrence_evidence_ids"] = append_unique(
        sense.get("reviewed_running_body_occurrence_evidence_ids", []),
        body_by_sense[sense_id],
    )
    term_number = int(sense["term_id"][1:])
    if 31 <= term_number <= 40:
        if sense["term_id"] == "T34":
            sense["occurrence_review_status"] = (
                "contiguous_T31_T40_review_complete_zero_raw_hit"
            )
        elif sense_id in gap_senses:
            sense["occurrence_review_status"] = (
                "contiguous_T31_T40_review_complete_zero_accepted_support"
            )
        else:
            sense["occurrence_review_status"] = (
                "contiguous_T31_T40_current_corpus_context_review_complete"
            )

for core in wordweb["core_concepts"]:
    term_id = core["term_id"]
    term_number = int(term_id[1:])
    if not 31 <= term_number <= 40:
        continue
    block = core["reviewed_occurrence_evidence"]
    block["supporting_ids"] = append_unique(
        block.get("supporting_ids", []), support_by_term[term_id]
    )
    block["adverse_ids"] = append_unique(
        block.get("adverse_ids", []), rejected_by_term[term_id]
    )
    block["held_ids"] = append_unique(
        block.get("held_ids", []), held_by_term[term_id]
    )
    block["lexical_navigation_support_ids"] = append_unique(
        block.get("lexical_navigation_support_ids", []),
        lexical_by_term[term_id],
    )
    block["running_body_support_ids"] = append_unique(
        block.get("running_body_support_ids", []), body_by_term[term_id]
    )
    block["supporting_count"] = len(block["supporting_ids"])
    block["adverse_count"] = len(block["adverse_ids"])
    block["held_count"] = len(block["held_ids"])
    block["lexical_navigation_support_count"] = len(
        block["lexical_navigation_support_ids"]
    )
    block["running_body_support_count"] = len(
        block["running_body_support_ids"]
    )
    block["zero_hit_current_corpus"] = term_id == "T34"
    block["zero_accepted_sense_ids"] = [
        sense_id for sense_id in core["sense_ids"] if sense_id in gap_senses
    ]
    block["scope"] = (
        "contiguous_T01_T40_frozen_occurrence_v1_plus_opportunistic_"
        "RM_RG_2021_T45_T57"
    )
    block["frozen_occurrence_table_excludes_new_2024_RM_sources"] = True
    block["form_promotions"] = 0
    block["human_observations"] = 0
    core["status"] = (
        "semantic_v8_contiguous_review_no_form_or_human_promotion"
    )

for decision in wordweb["decisions"]:
    sense_id = decision["sense_id"]
    decision["reviewed_supporting_occurrence_evidence_ids"] = append_unique(
        decision.get("reviewed_supporting_occurrence_evidence_ids", []),
        support_by_sense[sense_id],
    )
    decision["reviewed_adverse_occurrence_evidence_ids"] = append_unique(
        decision.get("reviewed_adverse_occurrence_evidence_ids", []),
        adverse_by_sense[sense_id],
    )
    decision["reviewed_held_occurrence_evidence_ids"] = append_unique(
        decision.get("reviewed_held_occurrence_evidence_ids", []),
        held_by_sense[sense_id],
    )
    decision["T31_T40_lexical_navigation_evidence_ids"] = list(
        lexical_by_sense[sense_id]
    )
    decision["T31_T40_running_body_evidence_ids"] = list(
        body_by_sense[sense_id]
    )
    decision["sense_label"] = sense_label_by_id[sense_id]
    term_number = int(decision["term_id"][1:])
    if 31 <= term_number <= 40:
        if decision["term_id"] == "T34":
            decision["occurrence_review_status"] = (
                "T31_T40_context_reviewed_zero_raw_hit"
            )
        elif sense_id in gap_senses:
            decision["occurrence_review_status"] = (
                "T31_T40_context_reviewed_zero_accepted_support"
            )
        else:
            decision["occurrence_review_status"] = (
                "T31_T40_context_reviewed_support_adverse_and_hold_separated"
            )
        decision["confidence_source_occurrence"] = (
            "internal_context_review_only_not_human_attestation"
        )

wordweb["artifact"] = "PAN_ROMANCE_WORDWEB_v8"
wordweb["supersedes_for_semantic_use"] = "PAN_ROMANCE_WORDWEB_v7"
wordweb["v7_retained_as"] = (
    "immutable predecessor with contiguous T01-T30 review; not rewritten"
)
wordweb["input_hashes"] = {
    "wordweb_v7_preserved": sha(WW7),
    "access_v7_preserved": sha(ACCESS7),
    "occurrence_review_T31_T40_v1": sha(REVIEW),
    "occurrence_review_T31_T40_summary_v1": sha(REVIEW_SUMMARY),
    "occurrence_review_T31_T40_builder_v1": sha(REVIEW_BUILDER),
    "occurrence_review_protocol_v1": sha(REVIEW_PROTOCOL),
    "frozen_occurrence_table_v1": sha(FROZEN_OCCURRENCES),
    "curated_external_source_manifest_v2_boundary_only": sha(
        CURATED_MANIFEST
    ),
    "canonical_cohort_topology_v2": sha(COHORT_TREE),
    "MII_method_v8": sha(METHOD),
    "builder_v8": sha(Path(__file__).resolve()),
}
wordweb["boundary"] = (
    "The 120 inherited Spanish/French core records remain unresolved locator "
    "claims with zero quotations. The reviewed layer covers contiguous "
    "T01-T40 plus opportunistic 2021 RM-RG T45/T57. The frozen v1 occurrence "
    "table predates and excludes the newly acquired 2024 RM sources. No "
    "reviewed context promotes a form, supplies human data, or licenses a "
    "pilot/intelligibility claim."
)
wordweb["occurrence_table_boundary"] = {
    "artifact": "ROMANCE_TERM_OCCURRENCES_v1.csv",
    "sha256": sha(FROZEN_OCCURRENCES),
    "status": "frozen_pre_2024_RM_acquisition_occurrence_table",
    "excluded_newly_acquired_source_ids": NEW_RM_2024_SOURCE_IDS,
    "excluded_sources_present_in_curated_manifest_v2": True,
    "fabricated_or_backfilled_occurrence_rows": 0,
    "next_required_action": (
        "later extraction and sense review against the curated 2024 RM "
        "sources; do not fold into v8"
    ),
}
wordweb["core_evidence_boundary"] = {
    "inherited_es_fr_core_records": 120,
    "inherited_core_quotation_count": 0,
    "inherited_core_acceptance": "unresolved_locator",
    "reviewed_occurrence_records": 444,
    "reviewed_supporting_status_events": 303,
    "reviewed_adverse_or_rejected_status_events": 110,
    "reviewed_held_status_events": 32,
    "status_event_counts_nonexclusive": True,
    "nonexclusive_reason": (
        "One preserved RM-RG occurrence supports ordinary-direction T57-S2 "
        "and is adverse to algebraic right-action T57-S1."
    ),
    "contiguous_reviewed_terms": "T01-T40",
    "explicit_zero_hit_terms": ["T11", "T34"],
    "zero_accepted_sense_gaps_T21_T30": [
        "T22-S2",
        "T25-S2",
        "T26-S1",
    ],
    "zero_accepted_sense_gaps_T31_T40": EXPECTED_ZERO_ACCEPTED_SENSES,
    "narrow_accepted_language_coverage_preserved": {
        "T27-S1": ["es", "fr"],
        "T28-S1": ["es"],
    },
    "T31_T40_reviewed_occurrence_records": 83,
    "T31_T40_accepted_status_events": 63,
    "T31_T40_rejected_status_events": 8,
    "T31_T40_held_status_events": 12,
    "T31_T40_accepted_lexical_navigation_records": 4,
    "T31_T40_accepted_running_body_context_records": 59,
    "rm_rg_reviewed_occurrence_records": 2,
    "rm_rg_specialist_algebra_attestations": 0,
    "new_2024_rm_sources_integrated_occurrence_records": 0,
    "extension_context_to_core_promotions": 0,
    "core_form_promotions": 0,
    "human_observations": 0,
    "pilot_or_intelligibility_claims": 0,
}
wordweb["occurrence_review_cursor"] = (
    "T01_T40_complete_on_frozen_occurrence_v1; "
    "opportunistic_2021_RM_RG_T45_T57_complete; next_contiguous_T41; "
    "new_2024_RM_sources_pending_later_extraction"
)
wordweb["exact_sense_label_contract_T51_T60"] = EXPECTED_LABEL_CONTRACT
wordweb["evidence_records"].extend(new_evidence)
wordweb["evidence_record_count"] = len(wordweb["evidence_records"])
wordweb["relation_count"] = sum(
    len(core["relations"]) for core in wordweb["core_concepts"]
)
wordweb["relation_metrics"] = relation_metrics(wordweb)
wordweb["predecessor_v7_relation_metrics"] = {
    "relation_records": 402,
    "valid_target_id_edges": 27,
    "invalid_target_id_edges": 0,
    "concept_to_sense_membership_edges": 106,
    "total_id_resolved_references_including_memberships": 133,
    "note": (
        "Relation records and semantic targets are unchanged; v8 rejects "
        "invalid nonempty targets."
    ),
}
wordweb["invalid_relation_target_negative_test_passed"] = (
    relation_negative_test_passed
)

require(
    wordweb["core_concept_count"] == 60
    and wordweb["sense_count"] == 106
    and len(wordweb["decisions"]) == 106,
    "v8 structural counts changed",
)
require(
    wordweb["evidence_record_count"] == 564,
    "v8 evidence count must equal 564",
)
require(
    wordweb["relation_metrics"] == expected_predecessor_metrics,
    "v8 relation metrics changed",
)
require(wordweb["relation_count"] == 402, "v8 relation count changed")
require(
    [core["forms"] for core in wordweb["core_concepts"]]
    == [core["forms"] for core in wordweb_v7["core_concepts"]],
    "core forms changed",
)
require(
    [core["relations"] for core in wordweb["core_concepts"]]
    == [core["relations"] for core in wordweb_v7["core_concepts"]],
    "relations changed",
)
require(
    wordweb["c2_extension_nodes"] == wordweb_v7["c2_extension_nodes"],
    "C2 extension nodes changed",
)
require(
    [semantic_signature(sense) for sense in wordweb["senses"]]
    == [semantic_signature(sense) for sense in wordweb_v7["senses"]],
    "sense semantics changed",
)
require(
    [decision["candidate_surfaces"] for decision in wordweb["decisions"]]
    == [
        decision["candidate_surfaces"]
        for decision in wordweb_v7["decisions"]
    ],
    "candidate surfaces changed",
)
require(
    {
        decision["sense_id"]: decision["sense_label"]
        for decision in wordweb["decisions"]
        if decision["sense_id"] in EXPECTED_LABEL_CONTRACT
    }
    == EXPECTED_LABEL_CONTRACT,
    "decision label contract mismatch",
)
require(
    all(
        record["quote"] is None
        and record["acceptance"] == "unresolved_locator"
        for record in wordweb["evidence_records"][:120]
    ),
    "inherited core quotation boundary changed",
)
occurrence_records = [
    record
    for record in wordweb["evidence_records"]
    if record.get("occurrence_id")
]
require(
    len(occurrence_records)
    == len({record["occurrence_id"] for record in occurrence_records})
    == 444,
    "v8 must contain 444 distinct reviewed occurrences",
)
require(
    len({record["evidence_id"] for record in wordweb["evidence_records"]})
    == 564,
    "v8 evidence IDs must be unique",
)
support_total = sum(
    core["reviewed_occurrence_evidence"].get("supporting_count", 0)
    for core in wordweb["core_concepts"]
)
rejected_total = sum(
    core["reviewed_occurrence_evidence"].get("adverse_count", 0)
    for core in wordweb["core_concepts"]
)
held_total = sum(
    core["reviewed_occurrence_evidence"].get("held_count", 0)
    for core in wordweb["core_concepts"]
)
require(
    {
        "reviewed_occurrence_records": len(occurrence_records),
        "accepted": support_total,
        "rejected": rejected_total,
        "held": held_total,
    }
    == EXPECTED_CUMULATIVE_COUNTS,
    "v8 cumulative status math mismatch",
)
require(
    support_total + rejected_total + held_total == 445,
    "nonexclusive status-event sum must be 445",
)
require(
    next(
        core
        for core in wordweb["core_concepts"]
        if core["term_id"] == "T34"
    )["reviewed_occurrence_evidence"]["zero_hit_current_corpus"]
    is True,
    "T34 zero-hit status missing",
)
require(
    t57_edges[0]["target_id"] == "T57-S1",
    "T57 adverse target changed",
)
require(
    wordweb["core_evidence_boundary"]["core_form_promotions"] == 0
    and wordweb["core_evidence_boundary"]["human_observations"] == 0
    and wordweb["core_evidence_boundary"][
        "pilot_or_intelligibility_claims"
    ]
    == 0,
    "v8 claim boundary leak",
)

WW8.write_text(
    json.dumps(wordweb, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
)

access["artifact"] = "PAN_ROMANCE_ACCESS_LEDGER_v8"
access["supersedes"] = "PAN_ROMANCE_ACCESS_LEDGER_v7"
access["status"] = (
    "sense_scoped_design_proxy_T01_T40_context_reviewed_zero_human_data"
)
access["method"] = "MII_METHOD_v8"
access["canonical_cohort_topology"] = {
    "artifact": cohort_tree["artifact"],
    "sha256": sha(COHORT_TREE),
    "cohort_ids": tree_cohort_ids,
    "cohort_count": 9,
}
access["input_hashes"] = {
    "access_v7_preserved": sha(ACCESS7),
    "wordweb_v8": sha(WW8),
    "occurrence_review_T31_T40_v1": sha(REVIEW),
    "occurrence_review_T31_T40_summary_v1": sha(REVIEW_SUMMARY),
    "occurrence_review_protocol_v1": sha(REVIEW_PROTOCOL),
    "frozen_occurrence_table_v1": sha(FROZEN_OCCURRENCES),
    "canonical_cohort_topology_v2": sha(COHORT_TREE),
    "MII_method_v8": sha(METHOD),
    "builder_v8": sha(Path(__file__).resolve()),
}
access["claim_boundary"] = (
    "All numeric proxies are design diagnostics only. The canonical "
    "nine-cohort topology has zero human observations; no MII result "
    "promotes a form or feeds decisions and every row remains "
    "pilot-ineligible. The frozen occurrence-v1 table excludes the newly "
    "acquired 2024 Rumantsch Grischun sources."
)
access["occurrence_table_boundary"] = (
    wordweb["occurrence_table_boundary"]
)
access["exact_sense_label_contract_T51_T60"] = EXPECTED_LABEL_CONTRACT
access["human_observation_count"] = 0
access["pilot_eligible_count"] = 0
access["form_promotion_count"] = 0

for row in access["rows"]:
    sense_id = row["sense_id"]
    supports = support_by_sense[sense_id]
    adverse = adverse_by_sense[sense_id]
    held = held_by_sense[sense_id]
    row["supporting_evidence_ids"] = append_string_ids(
        row.get("supporting_evidence_ids", ""), supports
    )
    row["reviewed_occurrence_support_ids"] = append_string_ids(
        row.get("reviewed_occurrence_support_ids", ""), supports
    )
    row["reviewed_occurrence_adverse_ids"] = append_string_ids(
        row.get("reviewed_occurrence_adverse_ids", ""), adverse
    )
    row["reviewed_occurrence_held_ids"] = append_string_ids(
        row.get("reviewed_occurrence_held_ids", ""), held
    )
    row["T31_T40_lexical_navigation_support_ids"] = ";".join(
        lexical_by_sense[sense_id]
    )
    row["T31_T40_running_body_support_ids"] = ";".join(
        body_by_sense[sense_id]
    )
    if adverse:
        row["adverse_evidence"] = (
            (row.get("adverse_evidence") or "")
            + " | reviewed adverse occurrence: "
            + ";".join(adverse)
        )
    term_number = int(row["term_id"][1:])
    if 31 <= term_number <= 40:
        if row["term_id"] == "T34":
            row["occurrence_review_status"] = (
                "T31_T40_context_reviewed_zero_raw_hit"
            )
        elif sense_id in gap_senses:
            row["occurrence_review_status"] = (
                "T31_T40_context_reviewed_zero_accepted_support"
            )
        else:
            row["occurrence_review_status"] = (
                "T31_T40_context_reviewed_support_adverse_and_hold_separated"
            )
        row["review_status"] = (
            "sense_scoped_design_proxy_context_reviewed_"
            "human_protocol_not_run"
        )
    row["method_version"] = "MII_METHOD_v8"
    row["human_n"] = None
    row["human_correct"] = None
    row["human_incorrect"] = None
    row["human_abstain"] = None
    row["human_latency_ms"] = None
    row["human_confidence"] = None
    row["effect_interval"] = None
    row["pilot_eligible"] = False
    row["sense_label"] = sense_label_by_id[sense_id]

access["sense_count"] = 106
access["row_count"] = len(access["rows"])
require(access["row_count"] == 106 * 9 == 954, "access row count mismatch")
require(
    [cohort["cohort_id"] for cohort in access["cohorts"]]
    == tree_cohort_ids,
    "access cohort ordering mismatch",
)
require(
    Counter(row["sense_id"] for row in access["rows"])
    == Counter({sense_id: 9 for sense_id in sense_ids}),
    "access sense/cohort multiplicity mismatch",
)
require(
    not any(
        row["human_n"] is not None
        or row["human_correct"] is not None
        or row["human_incorrect"] is not None
        or row["human_abstain"] is not None
        or row["human_latency_ms"] is not None
        or row["human_confidence"] is not None
        or row["effect_interval"] is not None
        or row["pilot_eligible"]
        for row in access["rows"]
    ),
    "human/pilot data leak in access rows",
)
require(
    all(row["method_version"] == "MII_METHOD_v8" for row in access["rows"]),
    "access method version mismatch",
)
for sense_id, expected_label in EXPECTED_LABEL_CONTRACT.items():
    matching_rows = [
        row for row in access["rows"] if row["sense_id"] == sense_id
    ]
    require(
        len(matching_rows) == 9
        and {row["sense_label"] for row in matching_rows}
        == {expected_label},
        f"access label mismatch for {sense_id}",
    )

ACCESS8_JSON.write_text(
    json.dumps(access, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
)

fields = list(access["rows"][0])
require(
    all(list(row) == fields for row in access["rows"]),
    "access row field order mismatch",
)
with ACCESS8_CSV.open("w", encoding="utf-8-sig", newline="") as handle:
    writer = csv.DictWriter(
        handle, fieldnames=fields, lineterminator="\n"
    )
    writer.writeheader()
    for row in access["rows"]:
        writer.writerow(
            {
                key: (
                    ""
                    if value is None
                    else str(value).lower()
                    if isinstance(value, bool)
                    else value
                )
                for key, value in row.items()
            }
        )

lines = [
    "PASS core_concepts=60 senses=106 evidence_records=564",
    (
        "relation_records=402 valid_target_id_edges=27 "
        "invalid_target_id_edges=0 concept_sense_memberships=106 "
        "total_resolved_references=133"
    ),
    "invalid_relation_target_negative_test=PASS",
    "T51_T60_exact_sense_label_contract=PASS",
    "T57_adverse_target=T57-S1",
    (
        "reviewed_occurrence_records=444 accepted_support_events=303 "
        "rejected_adverse_events=110 held_events=32 "
        "status_event_sum_nonexclusive=445"
    ),
    (
        "T31_T40_source_ids=83 accepted=63 rejected=8 held=12 "
        "lexical_navigation_accepted=4 running_body_context_accepted=59"
    ),
    "contiguous_review=T01-T40 next=T41",
    "explicit_zero_hit_terms=T11,T34",
    (
        "zero_accepted_sense_gaps_T31_T40="
        + ",".join(EXPECTED_ZERO_ACCEPTED_SENSES)
    ),
    (
        "frozen_occurrence_table_v1_sha256="
        + sha(FROZEN_OCCURRENCES)
    ),
    (
        "frozen_occurrence_table_excludes_2024_RM_sources="
        + ",".join(NEW_RM_2024_SOURCE_IDS)
    ),
    (
        "access_rows=954 canonical_cohorts=9 human_observations=0 "
        "pilot_eligible=0 form_promotions=0"
    ),
    f"MII_method_v8_sha256={sha(METHOD)}",
    f"occurrence_review_protocol_v1_sha256={sha(REVIEW_PROTOCOL)}",
    f"wordweb_v8_sha256={sha(WW8)}",
    f"access_v8_json_sha256={sha(ACCESS8_JSON)}",
    f"access_v8_csv_sha256={sha(ACCESS8_CSV)}",
]
LOG.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
