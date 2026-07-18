from __future__ import annotations

import copy
import csv
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
ROMANCE = ROOT.parent

WORDWEB_V8 = ROOT / "wordweb" / "PAN_ROMANCE_WORDWEB_v8.json"
ACCESS_V8 = ROOT / "access" / "PAN_ROMANCE_ACCESS_LEDGER_v8.json"
OCCURRENCES_V1 = ROOT / "wordweb" / "ROMANCE_TERM_OCCURRENCES_v1.csv"
OCCURRENCES_V2 = ROOT / "wordweb" / "ROMANCE_TERM_OCCURRENCES_v2.csv"
COHORT_TREE = ROMANCE / "00_lane_control" / "ROMANCE_FAMILY_COHORT_TREE_v2.json"

REVIEW_FILES = [
    ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_T01_T10_v1.csv",
    ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_T11_T20_v1.csv",
    ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_T21_T30_v1.csv",
    ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_T31_T40_v1.csv",
    ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_T41_T50_v1.csv",
    ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_T51_T60_v1.csv",
]
RM_DELTA_REVIEW = (
    ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_RM_RG_2024_DELTA_v1.csv"
)

WORDWEB_V9 = ROOT / "wordweb" / "PAN_ROMANCE_WORDWEB_v9.json"
ACCESS_V9_JSON = ROOT / "access" / "PAN_ROMANCE_ACCESS_LEDGER_v9.json"
ACCESS_V9_CSV = ROOT / "access" / "PAN_ROMANCE_ACCESS_LEDGER_v9.csv"
LOG = ROOT / "qa" / "WORDWEB_ACCESS_BUILD_v9.log"

EXPECTED_HASHES = {
    "wordweb_v8": "A332A8EDD7C0D33E018F0DB5AF7963701A2C8A716C94F83329C6AD24DE8EF0AD",
    "access_v8": "8155351FF40F57EF8627C22C377164A846AE7BA90F3AAF64B5BC6099639A28C0",
    "occurrences_v1": "6DF8FAD570D48369CA0A8FE06CD5A0EBC3C21275677E35BEDCF077208865DEE8",
    "occurrences_v2": "22212ED9DBC3406FFDFD1081FF7F7FCF64F964F905DBA3AAE94BB8A5F2CCB9B2",
    "cohort_tree_v2": "9EBDEF5BE13B9BDBB0F1F2B718C2EE6583CF59F723C200E78668FC9CD9AD332C",
    "review_T01_T10": "B8B70742B8F9BAE3FA37E5E6C62AB630A421852969EBAFF8744D2F220FC9D35A",
    "review_T11_T20": "FDC8374345DA4F1B6FC26DAE1C8415F2A24EBE8F57DEF9298F0C48DD1DC89CBA",
    "review_T21_T30": "E40638A96D609FFDA89739D42F5AF77111A394353B6FF94754D42955BCA8F845",
    "review_T31_T40": "8F98D501A79E5902AF5A54BD563F069B899E7CFDED587A9D7192EFA8F4B99D25",
    "review_T41_T50": "572E29B23C66A9E3F8A35D38A882A3681EC3767B690A41DEA18B124834D909E2",
    "review_T51_T60": "573A4CB70EEB0A49B1E5AFCDD91EA4D8DAA545081B72B6D965FC96698A5A7176",
    "review_RM_2024_delta": "7384BDA2A51E5749398EC89CDF87302BEBD989D12C490D9F8A5B306664E547C5",
}

EXPECTED_REVIEW_ROWS = [117, 111, 131, 83, 161, 76]
EXPECTED_ROW_CLASS_COUNTS = {"accepted": 510, "rejected": 127, "held": 45}
EXPECTED_ZERO_SUPPORT_SENSES = [
    "T09-S1",
    "T10-S1",
    "T10-S2",
    "T11-S1",
    "T11-S2",
    "T14-S2",
    "T15-S3",
    "T17-S2",
    "T17-S3",
    "T22-S2",
    "T25-S2",
    "T26-S1",
    "T31-S2",
    "T31-S3",
    "T33-S1",
    "T33-S3",
    "T34-S1",
    "T35-S1",
    "T35-S3",
    "T37-S2",
    "T44-S2",
    "T51-S4",
    "T52-S1",
    "T52-S2",
    "T52-S3",
    "T53-S1",
    "T53-S2",
    "T53-S3",
    "T54-S1",
    "T55-S1",
    "T55-S2",
    "T56-S1",
    "T56-S2",
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
HUMAN_FIELDS = [
    "human_n",
    "human_correct",
    "human_incorrect",
    "human_abstain",
    "human_latency_ms",
    "human_confidence",
    "effect_interval",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def split_ids(value: str | None) -> list[str]:
    return [
        item.strip()
        for item in (value or "").replace("|", ";").split(";")
        if item.strip()
    ]


def unique(values) -> list[str]:
    return list(dict.fromkeys(value for value in values if value))


def csv_scalar(value) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)


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


def relation_metrics(wordweb: dict) -> dict:
    valid_ids = (
        {core["term_id"] for core in wordweb["core_concepts"]}
        | {sense["sense_id"] for sense in wordweb["senses"]}
        | {node["concept_id"] for node in wordweb["c2_extension_nodes"]}
    )
    relations = [
        relation
        for core in wordweb["core_concepts"]
        for relation in core["relations"]
    ]
    invalid = [
        relation.get("target_id")
        for relation in relations
        if relation.get("target_id")
        and relation.get("target_id") not in valid_ids
    ]
    require(not invalid, f"invalid relation targets: {invalid}")
    targeted = sum(bool(relation.get("target_id")) for relation in relations)
    memberships = sum(len(core["sense_ids"]) for core in wordweb["core_concepts"])
    return {
        "relation_records": len(relations),
        "valid_target_id_edges": targeted,
        "invalid_target_id_edges": 0,
        "relation_records_without_target_id": len(relations) - targeted,
        "concept_to_sense_membership_edges": memberships,
        "total_id_resolved_references_including_memberships": targeted + memberships,
        "reporting_boundary": (
            "Relation records include descriptive/label relations without target IDs; "
            "they are not all graph edges. Any nonempty invalid target ID is a build error."
        ),
    }


def normalize_review_row(
    row: dict[str, str], source_name: str, sense_ids: set[str]
) -> dict:
    if source_name == "T01_T10":
        raw_status = row["semantic_review_status"]
        row_class = "accepted" if raw_status == "accepted_sense_match" else "rejected"
        support = split_ids(row["sense_ids"]) if row_class == "accepted" else []
        adverse_all = split_ids(row["sense_ids"]) if row_class == "rejected" else []
        held = []
        candidate_senses = split_ids(row["sense_ids"])
        context_class = row.get("evidence_role", "")
        review_tier = row["review_tier"]
        report = ""
        report_sha = ""
    elif source_name in {"T11_T20", "T21_T30"}:
        raw_status = row["semantic_review_status"]
        row_class = (
            "accepted"
            if raw_status == "accepted_sense_match"
            else "held"
            if raw_status.startswith("held_")
            else "rejected"
        )
        support = split_ids(row["reviewed_sense_ids"])
        adverse_all = split_ids(row["adverse_to_sense_ids"])
        held = split_ids(row["held_for_sense_ids"])
        candidate_senses = split_ids(row["sense_ids"])
        context_class = row.get("evidence_role", "")
        review_tier = row["review_tier"]
        report = ""
        report_sha = ""
    elif source_name in {"T31_T40", "T41_T50"}:
        raw_status = row["review_decision"]
        row_class = (
            "accepted"
            if raw_status == "accepted_sense_match"
            else "held"
            if raw_status == "held"
            else "rejected"
        )
        support = split_ids(row["accepted_sense_id"])
        adverse_all = split_ids(row["adverse_target"])
        held = split_ids(row["candidate_sense_ids"])
        candidate_senses = split_ids(row["source_candidate_sense_ids"])
        context_class = row["evidence_context_class"]
        review_tier = row["review_authority"]
        report = row["review_report"]
        report_sha = row["review_report_sha256"]
    elif source_name == "T51_T60":
        raw_status = row["row_review_decision"]
        row_class = (
            "accepted"
            if raw_status == "accepted_sense_match"
            else "held"
            if raw_status == "held"
            else "rejected"
        )
        support = split_ids(row["support_sense_ids"])
        adverse_all = split_ids(row["adverse_targets"])
        held = split_ids(row["held_candidate_sense_ids"])
        candidate_senses = split_ids(row["source_candidate_sense_ids"])
        context_class = row["evidence_context_class"]
        review_tier = row["review_authority"]
        report = row["review_report"]
        report_sha = row["review_report_sha256"]
        events = json.loads(row["review_events_json"])
        require(
            len(events)
            == int(row["support_event_count"])
            + int(row["adverse_event_count"])
            + int(row["hold_event_count"]),
            f"review event count mismatch for {row['occurrence_id']}",
        )
    elif source_name == "RM_2024_DELTA":
        raw_status = row["review_decision"]
        row_class = (
            "accepted"
            if raw_status == "accepted"
            else "held"
            if raw_status == "held"
            else "rejected"
        )
        support = split_ids(row["supporting_sense_ids"])
        adverse_all = split_ids(row["adverse_target_sense_id"])
        held = split_ids(row["held_sense_ids"])
        candidate_senses = [row["modeled_sense_id"]]
        context_class = row["source_context_class"]
        review_tier = row["review_tier"]
        report = row["review_report"]
        report_sha = row["review_report_sha256"]
    else:
        raise RuntimeError(f"unknown review source {source_name}")

    adverse_senses = [item for item in adverse_all if item in sense_ids]
    require(set(support + adverse_senses + held) <= sense_ids, "unknown modeled sense")
    require(
        all(item.startswith(row["term_id"] + "-") for item in support + adverse_senses + held),
        f"cross-term modeled sense on {row['occurrence_id']}",
    )
    require(
        hashlib.sha256(row["quote"].encode("utf-8")).hexdigest().upper()
        == row["quote_sha256"],
        f"quote hash mismatch for {row['occurrence_id']}",
    )

    if source_name in {"T01_T10", "T11_T20", "T21_T30"}:
        require(row["bridge_form_promotion_eligible"].lower() == "false", "promotion leak")
        require(row["human_observation"].lower() == "false", "human data leak")
        pilot_claim = False
    else:
        promotion = row.get("promotion_status", "not_promoted")
        if source_name == "RM_2024_DELTA":
            require(row["bridge_form_promotion_eligible"].lower() == "false", "promotion leak")
            require(row["core_form_promotion"].lower() == "false", "promotion leak")
        else:
            require(promotion == "not_promoted", "promotion leak")
        require(int(row["human_observation_count"]) == 0, "human data leak")
        require(row["pilot_claim"].lower() == "false", "pilot claim leak")
        pilot_claim = False

    evidence_id = "E-" + row["occurrence_id"]
    is_delta = source_name == "RM_2024_DELTA"
    body_status = row.get("body_attestation_status", "")
    if not body_status:
        body_status = (
            "internally_reviewed_context_match_not_human_attestation"
            if row_class == "accepted"
            else "held_not_attestation"
            if row_class == "held"
            else "wrong_or_adverse_context_not_target_attestation"
        )
    return {
        "evidence_id": evidence_id,
        "occurrence_id": row["occurrence_id"],
        "term_id": row["term_id"],
        "source_candidate_sense_ids": candidate_senses,
        "reviewed_supporting_sense_ids": unique(support),
        "reviewed_adverse_to_sense_ids": unique(adverse_senses),
        "reviewed_held_for_sense_ids": unique(held),
        "adverse_targets_all": unique(adverse_all),
        "row_classification": row_class,
        "review_status_raw": raw_status,
        "language": row["language"],
        "variety_code": row.get("variety_code") or None,
        "source_type": (
            "reviewed_corpus_v3_RM_2024_delta_occurrence"
            if is_delta
            else "reviewed_frozen_v1_occurrence"
        ),
        "origin_layer": (
            "corpus_v3_RM_2024_delta"
            if is_delta
            else "frozen_v1_complete_T01_T60_partition"
        ),
        "logical_source_id": row["logical_source_id"],
        "record_id": row["record_id"],
        "source_sha256": row["source_sha256"],
        "license_status": row["license_status"],
        "locator": f"{row['locator_path']}:{row['line_number']}",
        "quote": row["quote"],
        "quote_sha256": row["quote_sha256"],
        "acceptance": row_class,
        "review_reason_code": row.get("reason_code") or row.get("review_reason_code") or "",
        "review_note": row["review_note"],
        "review_tier": review_tier,
        "evidence_context_class": context_class,
        "body_attestation_status": body_status,
        "evidence_family_ids": split_ids(
            row.get("evidence_family_ids") or row.get("evidence_family_id")
        ),
        "family_roles": split_ids(row.get("family_roles") or row.get("family_role")),
        "review_report": report or None,
        "review_report_sha256": report_sha or None,
        "core_form_promotion": False,
        "bridge_form_promotion_eligible": False,
        "human_observation": False,
        "pilot_claim": pilot_claim,
    }


for label, path in {
    "wordweb_v8": WORDWEB_V8,
    "access_v8": ACCESS_V8,
    "occurrences_v1": OCCURRENCES_V1,
    "occurrences_v2": OCCURRENCES_V2,
    "cohort_tree_v2": COHORT_TREE,
    "review_T01_T10": REVIEW_FILES[0],
    "review_T11_T20": REVIEW_FILES[1],
    "review_T21_T30": REVIEW_FILES[2],
    "review_T31_T40": REVIEW_FILES[3],
    "review_T41_T50": REVIEW_FILES[4],
    "review_T51_T60": REVIEW_FILES[5],
    "review_RM_2024_delta": RM_DELTA_REVIEW,
}.items():
    require(sha(path) == EXPECTED_HASHES[label], f"input hash mismatch: {label}")

wordweb_v8 = json.loads(WORDWEB_V8.read_text(encoding="utf-8"))
access_v8 = json.loads(ACCESS_V8.read_text(encoding="utf-8"))
cohort_tree = json.loads(COHORT_TREE.read_text(encoding="utf-8"))
occurrences_v1 = read_csv(OCCURRENCES_V1)
occurrences_v2 = read_csv(OCCURRENCES_V2)
sense_ids = {sense["sense_id"] for sense in wordweb_v8["senses"]}

require(len(occurrences_v1) == len({row["occurrence_id"] for row in occurrences_v1}) == 679, "v1 occurrence count mismatch")
require(len(occurrences_v2) == len({row["occurrence_id"] for row in occurrences_v2}) == 682, "v2 occurrence count mismatch")
v1_ids = {row["occurrence_id"] for row in occurrences_v1}
v2_ids = {row["occurrence_id"] for row in occurrences_v2}
delta_ids = v2_ids - v1_ids
require(len(delta_ids) == 3 and not (v1_ids - v2_ids), "v2 delta must add exactly three IDs")

review_rows = []
source_names = ["T01_T10", "T11_T20", "T21_T30", "T31_T40", "T41_T50", "T51_T60"]
for path, source_name, expected_count in zip(REVIEW_FILES, source_names, EXPECTED_REVIEW_ROWS, strict=True):
    rows = read_csv(path)
    require(len(rows) == expected_count, f"row count mismatch in {path.name}")
    review_rows.extend((source_name, row) for row in rows)
delta_rows = read_csv(RM_DELTA_REVIEW)
require(len(delta_rows) == 3, "RM-2024 review delta must contain three rows")

frozen_review_ids = [row["occurrence_id"] for _, row in review_rows]
require(len(frozen_review_ids) == len(set(frozen_review_ids)) == 679, "frozen review IDs must be unique")
require(set(frozen_review_ids) == v1_ids, "T01-T60 reviews must exactly partition occurrence v1")
require({row["occurrence_id"] for row in delta_rows} == delta_ids, "RM delta review IDs must exactly equal v2-v1")

occurrence_by_id = {row["occurrence_id"]: row for row in occurrences_v2}
normalized = [normalize_review_row(row, source, sense_ids) for source, row in review_rows]
normalized.extend(normalize_review_row(row, "RM_2024_DELTA", sense_ids) for row in delta_rows)
require(len(normalized) == len({row["occurrence_id"] for row in normalized}) == 682, "normalized evidence IDs must be unique")
require({row["occurrence_id"] for row in normalized} == v2_ids, "normalized reviews must cover occurrence v2 exactly")

for record in normalized:
    source = occurrence_by_id[record["occurrence_id"]]
    for key in ("term_id", "language", "record_id", "source_sha256", "quote_sha256"):
        require(record[key] == source[key], f"occurrence identity mismatch {record['occurrence_id']} {key}")

row_class_counts = Counter(record["row_classification"] for record in normalized)
require(dict(row_class_counts) == EXPECTED_ROW_CLASS_COUNTS, f"row classification mismatch: {dict(row_class_counts)}")

support_by_sense = defaultdict(list)
adverse_by_sense = defaultdict(list)
held_by_sense = defaultdict(list)
support_by_term = defaultdict(list)
adverse_by_term = defaultdict(list)
held_by_term = defaultdict(list)
lexical_by_sense = defaultdict(list)
body_by_sense = defaultdict(list)
lexical_by_term = defaultdict(list)
body_by_term = defaultdict(list)
records_by_term = defaultdict(list)

for record in normalized:
    evidence_id = record["evidence_id"]
    term_id = record["term_id"]
    records_by_term[term_id].append(evidence_id)
    for sense_id in record["reviewed_supporting_sense_ids"]:
        support_by_sense[sense_id].append(evidence_id)
    for sense_id in record["reviewed_adverse_to_sense_ids"]:
        adverse_by_sense[sense_id].append(evidence_id)
    for sense_id in record["reviewed_held_for_sense_ids"]:
        held_by_sense[sense_id].append(evidence_id)
    if record["reviewed_supporting_sense_ids"]:
        support_by_term[term_id].append(evidence_id)
        if "navigation" in (record["evidence_context_class"] or "").lower():
            lexical_by_term[term_id].append(evidence_id)
            for sense_id in record["reviewed_supporting_sense_ids"]:
                lexical_by_sense[sense_id].append(evidence_id)
        else:
            body_by_term[term_id].append(evidence_id)
            for sense_id in record["reviewed_supporting_sense_ids"]:
                body_by_sense[sense_id].append(evidence_id)
    if record["row_classification"] == "rejected" or record["adverse_targets_all"]:
        adverse_by_term[term_id].append(evidence_id)
    if record["row_classification"] == "held" or record["reviewed_held_for_sense_ids"]:
        held_by_term[term_id].append(evidence_id)

supported_senses = {sense_id for sense_id, evidence in support_by_sense.items() if evidence}
zero_support_senses = sorted(sense_ids - supported_senses)
require(len(supported_senses) == 73, "accepted-support coverage must be 73/106")
require(zero_support_senses == EXPECTED_ZERO_SUPPORT_SENSES, "zero-support sense set changed")
support_sense_links = sum(
    len(record["reviewed_supporting_sense_ids"]) for record in normalized
)
adverse_sense_links = sum(
    len(record["reviewed_adverse_to_sense_ids"]) for record in normalized
)
held_sense_links = sum(
    len(record["reviewed_held_for_sense_ids"]) for record in normalized
)
form_admission_adverse_events = sum(
    target.endswith("-form-admission")
    for record in normalized
    for target in record["adverse_targets_all"]
)
require(
    (support_sense_links, adverse_sense_links, held_sense_links, form_admission_adverse_events)
    == (515, 129, 50, 20),
    "full review event-link counts changed",
)

wordweb = copy.deepcopy(wordweb_v8)
inherited = copy.deepcopy(wordweb_v8["evidence_records"][:120])
require(
    len(inherited) == 120
    and all(record["quote"] is None and record["acceptance"] == "unresolved_locator" for record in inherited),
    "v8 inherited evidence boundary changed",
)
v8_evidence = copy.deepcopy(wordweb_v8["evidence_records"])
v8_occurrence_ids = {
    record["occurrence_id"]
    for record in v8_evidence
    if record.get("occurrence_id")
}
require(len(v8_evidence) == 564, "v8 evidence count changed")
require(len(v8_occurrence_ids) == 444, "v8 reviewed occurrence count changed")
require(
    v8_occurrence_ids
    == set(frozen_review_ids[:442])
    | {"OCC-8A2E8CACFACD2104", "OCC-278E8BA674E87D7A"},
    "v8 reviewed evidence is not the expected T01-T40 plus two RM rows",
)
new_evidence = [
    record for record in normalized if record["occurrence_id"] not in v8_occurrence_ids
]
require(
    len(new_evidence)
    == len({record["evidence_id"] for record in new_evidence})
    == 238,
    "v9 must append exactly 238 post-v8 evidence records",
)
require(
    (
        sum(len(record["reviewed_supporting_sense_ids"]) for record in new_evidence),
        sum(len(record["reviewed_adverse_to_sense_ids"]) for record in new_evidence),
        sum(len(record["reviewed_held_for_sense_ids"]) for record in new_evidence),
        sum(
            target.endswith("-form-admission")
            for record in new_evidence
            for target in record["adverse_targets_all"]
        ),
    )
    == (209, 64, 19, 16),
    "post-v8 event-link counts changed",
)

for sense in wordweb["senses"]:
    sense_id = sense["sense_id"]
    term_id = sense["term_id"]
    sense["reviewed_supporting_occurrence_evidence_ids"] = unique(support_by_sense[sense_id])
    sense["reviewed_adverse_occurrence_evidence_ids"] = unique(adverse_by_sense[sense_id])
    sense["reviewed_held_occurrence_evidence_ids"] = unique(held_by_sense[sense_id])
    sense["reviewed_lexical_navigation_occurrence_evidence_ids"] = unique(lexical_by_sense[sense_id])
    sense["reviewed_running_body_occurrence_evidence_ids"] = unique(body_by_sense[sense_id])
    if not records_by_term[term_id]:
        sense["occurrence_review_status"] = "contiguous_T01_T60_review_complete_zero_raw_hit"
    elif sense_id in zero_support_senses:
        sense["occurrence_review_status"] = "contiguous_T01_T60_review_complete_zero_accepted_support"
    else:
        sense["occurrence_review_status"] = "contiguous_T01_T60_current_corpus_context_review_complete"

for core in wordweb["core_concepts"]:
    term_id = core["term_id"]
    block = core["reviewed_occurrence_evidence"]
    block["supporting_ids"] = unique(support_by_term[term_id])
    block["adverse_ids"] = unique(adverse_by_term[term_id])
    block["held_ids"] = unique(held_by_term[term_id])
    block["lexical_navigation_support_ids"] = unique(lexical_by_term[term_id])
    block["running_body_support_ids"] = unique(body_by_term[term_id])
    block["supporting_count"] = len(block["supporting_ids"])
    block["adverse_count"] = len(block["adverse_ids"])
    block["held_count"] = len(block["held_ids"])
    block["lexical_navigation_support_count"] = len(block["lexical_navigation_support_ids"])
    block["running_body_support_count"] = len(block["running_body_support_ids"])
    block["zero_hit_current_corpus"] = not bool(records_by_term[term_id])
    block["zero_accepted_sense_ids"] = [sense_id for sense_id in core["sense_ids"] if sense_id in zero_support_senses]
    block["scope"] = "contiguous_T01_T60_occurrence_v1_plus_reviewed_RM_RG_2024_delta"
    block["form_promotions"] = 0
    block["human_observations"] = 0
    core["status"] = "semantic_v9_contiguous_review_no_form_or_human_promotion"

sense_label_by_id = {sense["sense_id"]: sense["sense_label"] for sense in wordweb["senses"]}
for decision in wordweb["decisions"]:
    sense_id = decision["sense_id"]
    term_id = decision["term_id"]
    decision["reviewed_supporting_occurrence_evidence_ids"] = unique(support_by_sense[sense_id])
    decision["reviewed_adverse_occurrence_evidence_ids"] = unique(adverse_by_sense[sense_id])
    decision["reviewed_held_occurrence_evidence_ids"] = unique(held_by_sense[sense_id])
    decision["sense_label"] = sense_label_by_id[sense_id]
    if not records_by_term[term_id]:
        decision["occurrence_review_status"] = "T01_T60_context_reviewed_zero_raw_hit"
    elif sense_id in zero_support_senses:
        decision["occurrence_review_status"] = "T01_T60_context_reviewed_zero_accepted_support"
    else:
        decision["occurrence_review_status"] = "T01_T60_context_review_complete_support_adverse_hold_separated"
    decision["confidence_source_occurrence"] = "internal_context_review_only_not_human_attestation"

wordweb["artifact"] = "PAN_ROMANCE_WORDWEB_v9"
wordweb["supersedes_for_semantic_use"] = "PAN_ROMANCE_WORDWEB_v8"
wordweb["v8_retained_as"] = "immutable last machine-gated predecessor; not rewritten"
wordweb["input_hashes"] = {
    "wordweb_v8_preserved": sha(WORDWEB_V8),
    "access_v8_preserved": sha(ACCESS_V8),
    "occurrence_table_v1": sha(OCCURRENCES_V1),
    "occurrence_table_v2": sha(OCCURRENCES_V2),
    "review_T01_T10": sha(REVIEW_FILES[0]),
    "review_T11_T20": sha(REVIEW_FILES[1]),
    "review_T21_T30": sha(REVIEW_FILES[2]),
    "review_T31_T40": sha(REVIEW_FILES[3]),
    "review_T41_T50": sha(REVIEW_FILES[4]),
    "review_T51_T60": sha(REVIEW_FILES[5]),
    "review_RM_2024_delta": sha(RM_DELTA_REVIEW),
    "canonical_cohort_topology_v2": sha(COHORT_TREE),
    "builder_v9": sha(Path(__file__).resolve()),
}
wordweb["boundary"] = (
    "The 120 inherited Spanish/French core records remain unresolved locator claims with zero quotations. "
    "All 679 frozen occurrence-v1 IDs and the three occurrence-v2 RM-2024 delta IDs have internal semantic review, "
    "but no reviewed context promotes a form, supplies human data, or authorizes a pilot or intelligibility claim."
)
wordweb["occurrence_table_boundary"] = {
    "artifact": "ROMANCE_TERM_OCCURRENCES_v2.csv",
    "sha256": sha(OCCURRENCES_V2),
    "occurrence_count": 682,
    "frozen_v1_occurrence_count": 679,
    "reviewed_RM_2024_delta_count": 3,
    "review_coverage": "all_occurrence_ids_reviewed_exactly_once",
    "fabricated_or_backfilled_occurrence_rows": 0,
}
wordweb["core_evidence_boundary"] = {
    "inherited_es_fr_core_records": 120,
    "inherited_core_quotation_count": 0,
    "inherited_core_acceptance": "unresolved_locator",
    "reviewed_occurrence_records": 682,
    "reviewed_row_classifications": EXPECTED_ROW_CLASS_COUNTS,
    "reviewed_supporting_occurrence_ids": len({eid for values in support_by_term.values() for eid in values}),
    "reviewed_adverse_or_rejected_occurrence_ids": len({eid for values in adverse_by_term.values() for eid in values}),
    "reviewed_held_occurrence_ids": len({eid for values in held_by_term.values() for eid in values}),
    "reviewed_support_sense_links": support_sense_links,
    "reviewed_adverse_sense_links": adverse_sense_links,
    "reviewed_held_sense_links": held_sense_links,
    "form_admission_adverse_events": form_admission_adverse_events,
    "senses_with_accepted_support": 73,
    "senses_without_accepted_support": 33,
    "zero_accepted_support_sense_ids": zero_support_senses,
    "contiguous_reviewed_terms": "T01-T60",
    "explicit_zero_hit_terms": sorted(term_id for term_id in records_by_term if not records_by_term[term_id]),
    "reviewed_RM_2024_delta_records": 3,
    "extension_context_to_core_promotions": 0,
    "core_form_promotions": 0,
    "human_observations": 0,
    "pilot_or_intelligibility_claims": 0,
}
wordweb["occurrence_review_cursor"] = "T01_T60_complete_on_occurrence_v1_plus_reviewed_RM_2024_delta; all_682_occurrence_v2_ids_integrated"
wordweb["exact_sense_label_contract_T51_T60"] = EXPECTED_LABEL_CONTRACT
wordweb["evidence_records"] = v8_evidence + new_evidence
wordweb["evidence_record_count"] = len(wordweb["evidence_records"])
wordweb["relation_count"] = sum(len(core["relations"]) for core in wordweb["core_concepts"])
wordweb["relation_metrics"] = relation_metrics(wordweb)

require(wordweb["core_concept_count"] == len(wordweb["core_concepts"]) == 60, "concept count changed")
require(wordweb["sense_count"] == len(wordweb["senses"]) == 106, "sense count changed")
require(len(wordweb["c2_extension_nodes"]) == 39, "C2 node count changed")
require(len(wordweb["decisions"]) == 106, "decision count changed")
require(wordweb["evidence_record_count"] == 802, "evidence count must be 802")
require(len({record["evidence_id"] for record in wordweb["evidence_records"]}) == 802, "evidence IDs not unique")
require(wordweb["relation_metrics"]["relation_records"] == 402, "relation count changed")
require(wordweb["relation_metrics"]["valid_target_id_edges"] == 27, "targeted relation count changed")
require([core["forms"] for core in wordweb["core_concepts"]] == [core["forms"] for core in wordweb_v8["core_concepts"]], "forms changed")
require([core["relations"] for core in wordweb["core_concepts"]] == [core["relations"] for core in wordweb_v8["core_concepts"]], "relations changed")
require(wordweb["c2_extension_nodes"] == wordweb_v8["c2_extension_nodes"], "C2 nodes changed")
require([semantic_signature(sense) for sense in wordweb["senses"]] == [semantic_signature(sense) for sense in wordweb_v8["senses"]], "sense semantics changed")
require([decision["candidate_surfaces"] for decision in wordweb["decisions"]] == [decision["candidate_surfaces"] for decision in wordweb_v8["decisions"]], "candidate surfaces changed")
require(wordweb["core_evidence_boundary"]["core_form_promotions"] == 0, "form promotion leak")

WORDWEB_V9.write_text(json.dumps(wordweb, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

access = copy.deepcopy(access_v8)
tree_cohort_ids = [cohort["cohort_id"] for cohort in cohort_tree["reader_cohorts"]]
access["artifact"] = "PAN_ROMANCE_ACCESS_LEDGER_v9"
access["supersedes"] = "PAN_ROMANCE_ACCESS_LEDGER_v8"
access["status"] = "complete_106_by_9_design_grid_all_682_occurrences_reviewed_zero_human_data"
access["method"] = "MII_METHOD_v9"
access["input_hashes"] = {
    "access_v8_preserved": sha(ACCESS_V8),
    "wordweb_v9": sha(WORDWEB_V9),
    "occurrence_table_v2": sha(OCCURRENCES_V2),
    "canonical_cohort_topology_v2": sha(COHORT_TREE),
    "builder_v9": sha(Path(__file__).resolve()),
}
access["canonical_cohort_topology"] = {
    "artifact": cohort_tree["artifact"],
    "sha256": sha(COHORT_TREE),
    "cohort_ids": tree_cohort_ids,
    "cohort_count": 9,
}
access["claim_boundary"] = (
    "Empirical MII remains zero observations. Numeric orthographic proxies are deterministic design diagnostics only; "
    "they do not measure intelligibility and cannot promote a form, feed a vocabulary or grammar decision, or authorize a pilot."
)
access["occurrence_table_boundary"] = copy.deepcopy(wordweb["occurrence_table_boundary"])
access["exact_sense_label_contract_T51_T60"] = EXPECTED_LABEL_CONTRACT
access["human_observation_count"] = 0
access["pilot_eligible_count"] = 0
access["form_promotion_count"] = 0

for row in access["rows"]:
    sense_id = row["sense_id"]
    term_id = row["term_id"]
    supports = unique(support_by_sense[sense_id])
    adverse = unique(adverse_by_sense[sense_id])
    held = unique(held_by_sense[sense_id])
    inherited_support = [
        item
        for item in split_ids(row.get("supporting_evidence_ids", ""))
        if not item.startswith("E-OCC-")
    ]
    row["supporting_evidence_ids"] = ";".join(unique(inherited_support + supports))
    row["reviewed_occurrence_support_ids"] = ";".join(supports)
    row["reviewed_occurrence_adverse_ids"] = ";".join(adverse)
    row["reviewed_occurrence_held_ids"] = ";".join(held)
    adverse_text = row.get("adverse_evidence") or ""
    for marker in (
        " | reviewed adverse occurrence:",
        " | reviewed adverse occurrences:",
        " | reviewed RM-RG adverse occurrence:",
    ):
        adverse_text = adverse_text.split(marker, 1)[0]
    if adverse:
        adverse_text += " | reviewed adverse occurrences: " + ";".join(adverse)
    row["adverse_evidence"] = adverse_text
    if not records_by_term[term_id]:
        row["occurrence_review_status"] = "T01_T60_context_reviewed_zero_raw_hit"
    elif sense_id in zero_support_senses:
        row["occurrence_review_status"] = "T01_T60_context_reviewed_zero_accepted_support"
    else:
        row["occurrence_review_status"] = "T01_T60_context_review_complete_support_adverse_hold_separated"
    row["review_status"] = "sense_scoped_design_diagnostic_human_protocol_not_run"
    row["method_version"] = "MII_METHOD_v9"
    for field in HUMAN_FIELDS:
        row[field] = None
    row["pilot_eligible"] = False
    row["sense_label"] = sense_label_by_id[sense_id]

access["sense_count"] = 106
access["row_count"] = len(access["rows"])
require(access["row_count"] == 106 * 9 == 954, "access row count mismatch")
require(tree_cohort_ids == [cohort["cohort_id"] for cohort in access["cohorts"]], "cohort order mismatch")
require(len({(row["sense_id"], row["cohort_id"]) for row in access["rows"]}) == 954, "duplicate sense/cohort pair")
require(Counter(row["sense_id"] for row in access["rows"]) == Counter({sense_id: 9 for sense_id in sense_ids}), "sense multiplicity mismatch")
require(all(all(row[field] is None for field in HUMAN_FIELDS) for row in access["rows"]), "human data leak")
require(not any(row["pilot_eligible"] for row in access["rows"]), "pilot eligibility leak")
require(access["form_promotion_count"] == 0, "access form promotion leak")

ACCESS_V9_JSON.write_text(json.dumps(access, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
fields = list(access["rows"][0])
require(all(list(row) == fields for row in access["rows"]), "access row field order mismatch")
with ACCESS_V9_CSV.open("w", encoding="utf-8-sig", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    for row in access["rows"]:
        writer.writerow({key: csv_scalar(value) for key, value in row.items()})

csv_rows = read_csv(ACCESS_V9_CSV)
require(len(csv_rows) == 954 and list(csv_rows[0]) == fields, "access CSV schema mismatch")
for json_row, csv_row in zip(access["rows"], csv_rows, strict=True):
    require({key: csv_scalar(value) for key, value in json_row.items()} == csv_row, "access JSON/CSV mirror mismatch")

lines = [
    "PASS wordweb_v9 core_concepts=60 senses=106 c2_nodes=39 evidence_records=802 relations=402",
    "review_partition frozen_v1=679 rm_2024_delta=3 total=682 unique=682",
    "row_classifications accepted=510 rejected=127 held=45",
    "event_links support_sense=515 adverse_sense=129 held_sense=50 form_admission_adverse=20",
    "post_v8_appended_records=238 support_links=209 adverse_links=64 held_links=19 form_admission_adverse=16",
    "accepted_support_coverage=73/106 zero_support=33",
    "inherited_claims=120 quotations=0 unresolved=120",
    "access_rows=954 sense_cohort_pairs=954 cohorts=9 human_observations=0 pilot_eligible=0 form_promotions=0",
    "empirical_MII=0 diagnostics_are_not_measured_intelligibility",
    f"wordweb_v9_sha256={sha(WORDWEB_V9)}",
    f"access_v9_json_sha256={sha(ACCESS_V9_JSON)}",
    f"access_v9_csv_sha256={sha(ACCESS_V9_CSV)}",
]
LOG.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
