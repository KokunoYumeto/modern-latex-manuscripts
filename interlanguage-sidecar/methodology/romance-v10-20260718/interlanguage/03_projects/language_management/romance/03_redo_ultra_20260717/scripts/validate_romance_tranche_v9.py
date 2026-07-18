from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
ROMANCE = ROOT.parent
WORKSPACE = ROOT.parents[3]
QA = ROOT / "qa"
WORDWEB_DIR = ROOT / "wordweb"
ACCESS_DIR = ROOT / "access"

WORDWEB_V8 = WORDWEB_DIR / "PAN_ROMANCE_WORDWEB_v8.json"
ACCESS_V8_JSON = ACCESS_DIR / "PAN_ROMANCE_ACCESS_LEDGER_v8.json"
ACCESS_V8_CSV = ACCESS_DIR / "PAN_ROMANCE_ACCESS_LEDGER_v8.csv"
GATE_V8 = QA / "ROMANCE_ACCEPTANCE_GATE_v8.json"
MANIFEST_V8 = QA / "SHA256SUMS_v8.csv"

WORDWEB_V9 = WORDWEB_DIR / "PAN_ROMANCE_WORDWEB_v9.json"
ACCESS_V9_JSON = ACCESS_DIR / "PAN_ROMANCE_ACCESS_LEDGER_v9.json"
ACCESS_V9_CSV = ACCESS_DIR / "PAN_ROMANCE_ACCESS_LEDGER_v9.csv"
METHOD_V9 = ACCESS_DIR / "MII_METHOD_v9.md"
BUILDER_V9 = ROOT / "scripts" / "build_wordweb_and_access_v9.py"
BUILD_LOG_V9 = QA / "WORDWEB_ACCESS_BUILD_v9.log"
MANIFEST_V9 = QA / "SHA256SUMS_v9.csv"
GATE_V9 = QA / "ROMANCE_ACCEPTANCE_GATE_v9.json"
GATE_LOG_V9 = QA / "ROMANCE_ACCEPTANCE_GATE_v9.log"

OCCURRENCES_V1 = WORDWEB_DIR / "ROMANCE_TERM_OCCURRENCES_v1.csv"
OCCURRENCES_V2 = WORDWEB_DIR / "ROMANCE_TERM_OCCURRENCES_v2.csv"
REVIEW_FILES = [
    WORDWEB_DIR / "ROMANCE_OCCURRENCE_REVIEW_T01_T10_v1.csv",
    WORDWEB_DIR / "ROMANCE_OCCURRENCE_REVIEW_T11_T20_v1.csv",
    WORDWEB_DIR / "ROMANCE_OCCURRENCE_REVIEW_T21_T30_v1.csv",
    WORDWEB_DIR / "ROMANCE_OCCURRENCE_REVIEW_T31_T40_v1.csv",
    WORDWEB_DIR / "ROMANCE_OCCURRENCE_REVIEW_T41_T50_v1.csv",
    WORDWEB_DIR / "ROMANCE_OCCURRENCE_REVIEW_T51_T60_v1.csv",
]
REVIEW_JSON_FILES = [path.with_suffix(".json") for path in REVIEW_FILES]
RM_DELTA_REVIEW = WORDWEB_DIR / "ROMANCE_OCCURRENCE_REVIEW_RM_RG_2024_DELTA_v1.csv"
RM_DELTA_REVIEW_JSON = RM_DELTA_REVIEW.with_suffix(".json")
COHORT_TREE = ROMANCE / "00_lane_control" / "ROMANCE_FAMILY_COHORT_TREE_v2.json"
CORPUS = ROOT / "corpus" / "ROMANCE_CONSOLIDATED_CORPUS_v3.csv"
ROUTES = ROOT / "corpus" / "ROMANCE_BRANCH_ROUTING_LEDGER_v2.csv"
CORPUS_AUDIT = QA / "CORPUS_BRANCH_PACKAGE_AUDIT_v1.json"
RENDER_V10 = QA / "PDF_RENDER_REPRODUCIBILITY_v10.json"
README = ROOT / "README.md"
CURSOR = ROOT / "CONTINUATION_CURSOR.md"

EXPECTED_V8_HASHES = {
    WORDWEB_V8: "A332A8EDD7C0D33E018F0DB5AF7963701A2C8A716C94F83329C6AD24DE8EF0AD",
    ACCESS_V8_JSON: "8155351FF40F57EF8627C22C377164A846AE7BA90F3AAF64B5BC6099639A28C0",
    ACCESS_V8_CSV: "5A33FE4E4173457553D78449B20495036077054F72F546C287690F77D91E9EEC",
    GATE_V8: "8CB731AED9A245240F55925B75407A1253C9FCEB59D39AB85442F9EC34DE0B1A",
    MANIFEST_V8: "044A864A64C7A3BE703838F6122EAB6832A86094FCAA8E1D0250B0CCFCD5952D",
}
EXPECTED_ROW_CLASSES = {"accepted": 510, "rejected": 127, "held": 45}
EXPECTED_ZERO_SUPPORT = {
    "T09-S1", "T10-S1", "T10-S2", "T11-S1", "T11-S2", "T14-S2",
    "T15-S3", "T17-S2", "T17-S3", "T22-S2", "T25-S2", "T26-S1",
    "T31-S2", "T31-S3", "T33-S1", "T33-S3", "T34-S1", "T35-S1",
    "T35-S3", "T37-S2", "T44-S2", "T51-S4", "T52-S1", "T52-S2",
    "T52-S3", "T53-S1", "T53-S2", "T53-S3", "T54-S1", "T55-S1",
    "T55-S2", "T56-S1", "T56-S2",
}
EXPECTED_ZERO_HIT_TERMS = {"T11", "T34", "T52", "T53", "T54", "T56"}
HUMAN_FIELDS = [
    "human_n", "human_correct", "human_incorrect", "human_abstain",
    "human_latency_ms", "human_confidence", "effect_interval",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def jread(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def split_ids(value: str | None) -> list[str]:
    return [item.strip() for item in (value or "").replace("|", ";").split(";") if item.strip()]


def csv_scalar(value) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)


def semantic_signature(sense: dict):
    return (
        sense["sense_id"], sense["term_id"], sense["sense_label"], sense["definition"],
        tuple(sense.get("domain_clusters", [])), tuple(sense.get("inclusions", [])),
        tuple(sense.get("exclusions", [])),
    )


def review_projection(row: dict[str, str], source: str, sense_ids: set[str]) -> dict:
    if source == "T01_T10":
        raw = row["semantic_review_status"]
        row_class = "accepted" if raw == "accepted_sense_match" else "rejected"
        support = split_ids(row["sense_ids"]) if row_class == "accepted" else []
        adverse_all = split_ids(row["sense_ids"]) if row_class == "rejected" else []
        held = []
    elif source in {"T11_T20", "T21_T30"}:
        raw = row["semantic_review_status"]
        row_class = "accepted" if raw == "accepted_sense_match" else "held" if raw.startswith("held_") else "rejected"
        support = split_ids(row["reviewed_sense_ids"])
        adverse_all = split_ids(row["adverse_to_sense_ids"])
        held = split_ids(row["held_for_sense_ids"])
    elif source in {"T31_T40", "T41_T50"}:
        raw = row["review_decision"]
        row_class = "accepted" if raw == "accepted_sense_match" else "held" if raw == "held" else "rejected"
        support = split_ids(row["accepted_sense_id"])
        adverse_all = split_ids(row["adverse_target"])
        held = split_ids(row["candidate_sense_ids"])
    elif source == "T51_T60":
        raw = row["row_review_decision"]
        row_class = "accepted" if raw == "accepted_sense_match" else "held" if raw == "held" else "rejected"
        support = split_ids(row["support_sense_ids"])
        adverse_all = split_ids(row["adverse_targets"])
        held = split_ids(row["held_candidate_sense_ids"])
        events = json.loads(row["review_events_json"])
        require(
            len(events) == int(row["support_event_count"]) + int(row["adverse_event_count"]) + int(row["hold_event_count"]),
            f"event count mismatch {row['occurrence_id']}",
        )
    else:
        raw = row["review_decision"]
        row_class = "accepted" if raw == "accepted" else "held" if raw == "held" else "rejected"
        support = split_ids(row["supporting_sense_ids"])
        adverse_all = split_ids(row["adverse_target_sense_id"])
        held = split_ids(row["held_sense_ids"])
    adverse_senses = [item for item in adverse_all if item in sense_ids]
    require(set(support + adverse_senses + held) <= sense_ids, f"unknown sense in {row['occurrence_id']}")
    require(
        hashlib.sha256(row["quote"].encode("utf-8")).hexdigest().upper() == row["quote_sha256"],
        f"quote hash mismatch {row['occurrence_id']}",
    )
    return {
        "occurrence_id": row["occurrence_id"],
        "evidence_id": "E-" + row["occurrence_id"],
        "term_id": row["term_id"],
        "row_class": row_class,
        "support": support,
        "adverse_senses": adverse_senses,
        "adverse_all": adverse_all,
        "held": held,
    }


def verify_predecessor_manifest(core_only: bool) -> tuple[int, list[str]]:
    for path, expected in EXPECTED_V8_HASHES.items():
        require(sha(path) == expected, f"v8 artifact changed: {path.name}")
    rows = read_csv(MANIFEST_V8)
    require(len(rows) == len({row["relative_path"] for row in rows}) == 223, "v8 manifest shape changed")
    mismatches = []
    for row in rows:
        path = (ROOT / row["relative_path"]).resolve()
        if not path.exists() or path.stat().st_size != int(row["bytes"]) or sha(path) != row["sha256"]:
            mismatches.append(row["relative_path"])
    if core_only:
        require(not mismatches, f"v8 manifest mismatch before successor docs: {mismatches}")
    else:
        require(
            set(mismatches) <= {"README.md", "CONTINUATION_CURSOR.md"},
            f"unexpected v8 predecessor drift: {mismatches}",
        )
    return len(rows), mismatches


def validate_stage_d() -> dict:
    expected_next = {"R823_HG_T005": 21209, "R823_HG_T006": 21256}
    validation_hashes = {}
    for tranche, next_line in expected_next.items():
        path = ROOT / tranche / "qa" / f"{tranche}_validation.json"
        data = jread(path)
        require(data["status"] == "PASS", f"{tranche} local validation failed")
        require(data["next_source_line"] == next_line, f"{tranche} cursor mismatch")
        require(data["human_validation_rows"] == 0 and data["native_validation"] is False and data["pilot_claim"] is False, f"{tranche} human claim leak")
        require(data["all_source_segments_accounted"] is True, f"{tranche} source accounting incomplete")
        build_pdf = ROOT / tranche / "build" / f"{tranche}_romance.pdf"
        output_pdf = WORKSPACE / "output" / "pdf" / f"{tranche}_controlled_romance.pdf"
        require(build_pdf.read_bytes() == output_pdf.read_bytes(), f"{tranche} output PDF mismatch")
        require(data["pdf_sha256"] == sha(build_pdf) == data["output_pdf_sha256"], f"{tranche} PDF hash mismatch")
        validation_hashes[tranche] = sha(path)
    render = jread(RENDER_V10)
    require(render["artifact"] == "PDF_RENDER_REPRODUCIBILITY_v10" and render["status"] == "PASS", "render v10 not PASS")
    require([item["tranche"] for item in render["tranches"]] == [f"R823_HG_T00{i}" for i in range(1, 7)], "render tranche topology mismatch")
    require(render["totals"]["tranches"] == 6 and render["totals"]["pinned_pages"] == 15, "render totals mismatch")
    require(render["totals"]["all_build_output_pdfs_byte_identical"] is True and render["totals"]["all_fresh_pinned_pngs_byte_identical"] is True, "render reproducibility failed")
    return {
        "status": "T001_T006_PRODUCTION_TRANCHES_PASS_NOT_LANGUAGE_VALIDATED",
        "source_lines": {
            "T001": "21047-21087", "T002": "21089-21097", "T003": "21099-21115",
            "T004": "21117-21146", "T005": "21148-21202", "T006": "21209-21254",
        },
        "next_authority_line": 21256,
        "output_copy_exact_matches": 6,
        "render_reproducibility": "T001_T006_PASS_15_OF_15_PAGES",
        "T005_T006_validation_hashes": validation_hashes,
        "human_validation": 0,
    }


def validate_core(core_only: bool) -> dict:
    predecessor_rows, predecessor_mismatches = verify_predecessor_manifest(core_only)
    wordweb_v8 = jread(WORDWEB_V8)
    wordweb = jread(WORDWEB_V9)
    access_v8 = jread(ACCESS_V8_JSON)
    access = jread(ACCESS_V9_JSON)
    access_csv = read_csv(ACCESS_V9_CSV)
    cohort_tree = jread(COHORT_TREE)

    require(wordweb["artifact"] == "PAN_ROMANCE_WORDWEB_v9", "wrong WordWeb artifact")
    require(wordweb["core_concept_count"] == len(wordweb["core_concepts"]) == 60, "concept count mismatch")
    require(wordweb["sense_count"] == len(wordweb["senses"]) == 106, "sense count mismatch")
    require(len(wordweb["c2_extension_nodes"]) == 39 and len(wordweb["decisions"]) == 106, "C2/decision count mismatch")
    require(wordweb["evidence_record_count"] == len(wordweb["evidence_records"]) == 802, "evidence count mismatch")
    require(wordweb["evidence_records"][:564] == wordweb_v8["evidence_records"], "v8 evidence prefix changed")
    evidence_ids = [record["evidence_id"] for record in wordweb["evidence_records"]]
    require(len(evidence_ids) == len(set(evidence_ids)) == 802, "evidence IDs not unique")
    occurrence_records = [record for record in wordweb["evidence_records"] if record.get("occurrence_id")]
    require(len(occurrence_records) == len({record["occurrence_id"] for record in occurrence_records}) == 682, "reviewed occurrence count mismatch")

    sense_ids = {sense["sense_id"] for sense in wordweb["senses"]}
    projections = []
    for path, source in zip(REVIEW_FILES, ["T01_T10", "T11_T20", "T21_T30", "T31_T40", "T41_T50", "T51_T60"], strict=True):
        projections.extend(review_projection(row, source, sense_ids) for row in read_csv(path))
    projections.extend(review_projection(row, "RM_DELTA", sense_ids) for row in read_csv(RM_DELTA_REVIEW))
    require(len(projections) == len({row["occurrence_id"] for row in projections}) == 682, "review projection count mismatch")
    occurrence_v1_ids = {row["occurrence_id"] for row in read_csv(OCCURRENCES_V1)}
    occurrence_v2_ids = {row["occurrence_id"] for row in read_csv(OCCURRENCES_V2)}
    require(len(occurrence_v1_ids) == 679 and len(occurrence_v2_ids) == 682, "occurrence table count mismatch")
    require({row["occurrence_id"] for row in projections} == occurrence_v2_ids, "review coverage does not equal occurrence v2")
    require(Counter(row["row_class"] for row in projections) == Counter(EXPECTED_ROW_CLASSES), "row class counts mismatch")

    support_by_sense = defaultdict(list)
    adverse_by_sense = defaultdict(list)
    held_by_sense = defaultdict(list)
    support_by_term = defaultdict(list)
    adverse_by_term = defaultdict(list)
    held_by_term = defaultdict(list)
    hit_terms = set()
    for row in projections:
        hit_terms.add(row["term_id"])
        for sense_id in row["support"]:
            support_by_sense[sense_id].append(row["evidence_id"])
        for sense_id in row["adverse_senses"]:
            adverse_by_sense[sense_id].append(row["evidence_id"])
        for sense_id in row["held"]:
            held_by_sense[sense_id].append(row["evidence_id"])
        if row["support"]:
            support_by_term[row["term_id"]].append(row["evidence_id"])
        if row["row_class"] == "rejected" or row["adverse_all"]:
            adverse_by_term[row["term_id"]].append(row["evidence_id"])
        if row["row_class"] == "held" or row["held"]:
            held_by_term[row["term_id"]].append(row["evidence_id"])
    require(
        (
            sum(len(row["support"]) for row in projections),
            sum(len(row["adverse_senses"]) for row in projections),
            sum(len(row["held"]) for row in projections),
            sum(target.endswith("-form-admission") for row in projections for target in row["adverse_all"]),
        ) == (515, 129, 50, 20),
        "review event-link totals mismatch",
    )
    require(sense_ids - set(support_by_sense) == EXPECTED_ZERO_SUPPORT, "zero-support sense set mismatch")
    require(len(set(support_by_sense)) == 73, "support coverage mismatch")
    require({core["term_id"] for core in wordweb["core_concepts"]} - hit_terms == EXPECTED_ZERO_HIT_TERMS, "zero-hit term set mismatch")

    for sense in wordweb["senses"]:
        sense_id = sense["sense_id"]
        require(sense["reviewed_supporting_occurrence_evidence_ids"] == list(dict.fromkeys(support_by_sense[sense_id])), f"support links mismatch {sense_id}")
        require(sense["reviewed_adverse_occurrence_evidence_ids"] == list(dict.fromkeys(adverse_by_sense[sense_id])), f"adverse links mismatch {sense_id}")
        require(sense["reviewed_held_occurrence_evidence_ids"] == list(dict.fromkeys(held_by_sense[sense_id])), f"held links mismatch {sense_id}")
    for core in wordweb["core_concepts"]:
        term_id = core["term_id"]
        block = core["reviewed_occurrence_evidence"]
        require(block["supporting_ids"] == list(dict.fromkeys(support_by_term[term_id])), f"core support mismatch {term_id}")
        require(block["adverse_ids"] == list(dict.fromkeys(adverse_by_term[term_id])), f"core adverse mismatch {term_id}")
        require(block["held_ids"] == list(dict.fromkeys(held_by_term[term_id])), f"core held mismatch {term_id}")
        require(block["form_promotions"] == block["human_observations"] == 0, f"core claim leak {term_id}")
    decision_by_sense = {decision["sense_id"]: decision for decision in wordweb["decisions"]}
    for sense_id in sense_ids:
        decision = decision_by_sense[sense_id]
        require(decision["reviewed_supporting_occurrence_evidence_ids"] == list(dict.fromkeys(support_by_sense[sense_id])), f"decision support mismatch {sense_id}")

    require([core["forms"] for core in wordweb["core_concepts"]] == [core["forms"] for core in wordweb_v8["core_concepts"]], "forms drifted")
    require([core["relations"] for core in wordweb["core_concepts"]] == [core["relations"] for core in wordweb_v8["core_concepts"]], "relations drifted")
    require(wordweb["c2_extension_nodes"] == wordweb_v8["c2_extension_nodes"], "C2 nodes drifted")
    require([semantic_signature(sense) for sense in wordweb["senses"]] == [semantic_signature(sense) for sense in wordweb_v8["senses"]], "sense semantics drifted")
    require([decision["candidate_surfaces"] for decision in wordweb["decisions"]] == [decision["candidate_surfaces"] for decision in wordweb_v8["decisions"]], "candidate surfaces drifted")
    relation_count = sum(len(core["relations"]) for core in wordweb["core_concepts"])
    targeted = sum(bool(relation.get("target_id")) for core in wordweb["core_concepts"] for relation in core["relations"])
    require((relation_count, targeted) == (402, 27), "relation metrics changed")
    require(wordweb["core_evidence_boundary"]["core_form_promotions"] == wordweb["core_evidence_boundary"]["human_observations"] == 0, "WordWeb claim leak")

    cohort_ids = [cohort["cohort_id"] for cohort in cohort_tree["reader_cohorts"]]
    require(access["artifact"] == "PAN_ROMANCE_ACCESS_LEDGER_v9" and access["method"] == "MII_METHOD_v9", "wrong access artifact/method")
    require(access["sense_count"] == 106 and access["row_count"] == len(access["rows"]) == len(access_csv) == 954, "access row count mismatch")
    require([cohort["cohort_id"] for cohort in access["cohorts"]] == cohort_ids and len(cohort_ids) == 9, "cohort topology mismatch")
    require(len({(row["sense_id"], row["cohort_id"]) for row in access["rows"]}) == 954, "duplicate access pair")
    require(Counter(row["sense_id"] for row in access["rows"]) == Counter({sense_id: 9 for sense_id in sense_ids}), "access sense multiplicity mismatch")
    require(Counter(row["cohort_id"] for row in access["rows"]) == Counter({cohort_id: 106 for cohort_id in cohort_ids}), "access cohort multiplicity mismatch")
    require(access["human_observation_count"] == access["pilot_eligible_count"] == access["form_promotion_count"] == 0, "access aggregate claim leak")
    require(all(all(row[field] is None for field in HUMAN_FIELDS) and row["pilot_eligible"] is False for row in access["rows"]), "access human field leak")
    require(list(access["rows"][0]) == list(access_csv[0]), "access CSV field order mismatch")
    for json_row, csv_row in zip(access["rows"], access_csv, strict=True):
        require({key: csv_scalar(value) for key, value in json_row.items()} == csv_row, "access JSON/CSV mismatch")
        sense_id = json_row["sense_id"]
        require(split_ids(json_row["reviewed_occurrence_support_ids"]) == list(dict.fromkeys(support_by_sense[sense_id])), f"access support mismatch {sense_id}")
        require(split_ids(json_row["reviewed_occurrence_adverse_ids"]) == list(dict.fromkeys(adverse_by_sense[sense_id])), f"access adverse mismatch {sense_id}")
        require(split_ids(json_row["reviewed_occurrence_held_ids"]) == list(dict.fromkeys(held_by_sense[sense_id])), f"access held mismatch {sense_id}")

    diagnostic_fields = [
        "candidate_surfaces", "cohort_id", "cohort_name", "cohort_standard",
        "dominant_standard_forms", "candidate_to_cohort_orthographic_proxy",
        "Spanish_to_cohort_orthographic_proxy", "French_to_cohort_orthographic_proxy",
        "proxy_delta_over_Spanish", "proxy_delta_over_French",
        "beats_both_dominant_forms_by_0_05", "proxy_interpretation", "penalties",
    ]
    for old, new in zip(access_v8["rows"], access["rows"], strict=True):
        require({field: new[field] for field in diagnostic_fields} == {field: old[field] for field in diagnostic_fields}, "orthographic diagnostic drift")
    require(sum(row["candidate_to_cohort_orthographic_proxy"] is not None for row in access["rows"]) == 358, "candidate proxy count mismatch")
    require(sum(row["Spanish_to_cohort_orthographic_proxy"] is not None for row in access["rows"]) == 699, "Spanish proxy count mismatch")
    require(sum(row["French_to_cohort_orthographic_proxy"] is not None for row in access["rows"]) == 699, "French proxy count mismatch")
    rm_id_rows = [row for row in access["rows"] if row["cohort_id"] == "C-RM-ID"]
    require(all(row["candidate_to_cohort_orthographic_proxy"] is None for row in rm_id_rows), "regional Romansh proxy must remain absent")

    corpus_audit = jread(CORPUS_AUDIT)
    require(corpus_audit["status"] == "PASS", "corpus audit not PASS")
    require(corpus_audit["counts"] == {
        "records": 148, "primary_unique": 142, "representation_aliases": 6,
        "counting_eligible": 66, "excluded": 5, "coverage_rows": 9,
        "routes": 61, "active_routes": 8, "zero_routes": 53,
        "rm_counting_eligible": 3, "rm_general_school_math": 3,
        "rm_specialist_algebra": 0, "rm_inherited_form_attestation": 0,
        "rm_regional_idiom_active_bodies": 0,
    }, "corpus audit counts changed")
    routes = read_csv(ROUTES)
    require(len(routes) == 61 and sum(int(row["current_active_body_count"]) > 0 for row in routes) == 8, "route count mismatch")
    rm_route = next(row for row in routes if row["variety_code"] == "rm-rg")
    require((rm_route["current_active_body_count"], rm_route["current_general_school_math_body_count"], rm_route["current_specialist_algebra_body_count"]) == ("3", "3", "0"), "RM-RG route mismatch")
    idioms = [row for row in routes if row["variety_code"] in {"rm-sursilvan", "rm-sutsilvan", "rm-surmiran", "rm-puter", "rm-vallader"}]
    require(len(idioms) == 5 and all(row["current_active_body_count"] == "0" for row in idioms), "Romansh idiom gap changed")

    stage_d = validate_stage_d()
    return {
        "predecessor_manifest_rows": predecessor_rows,
        "predecessor_manifest_live_mismatches": predecessor_mismatches,
        "stage_d": stage_d,
        "wordweb_sha256": sha(WORDWEB_V9),
        "access_json_sha256": sha(ACCESS_V9_JSON),
        "access_csv_sha256": sha(ACCESS_V9_CSV),
    }


def validate_docs() -> None:
    readme = README.read_text(encoding="utf-8")
    cursor = CURSOR.read_text(encoding="utf-8")
    method = METHOD_V9.read_text(encoding="utf-8")
    for text, label in ((readme, "README"), (cursor, "cursor")):
        for required in ("v9", "682", "802", "73/106", "954", "zero human", "T005", "T006", "21256"):
            require(required.lower() in text.lower(), f"{label} missing {required}")
    for required in (
        "PAN_ROMANCE_WORDWEB_v9", "PAN_ROMANCE_ACCESS_LEDGER_v9",
        "zero human observations", "954", "diagnostics", "do not measure intelligibility",
    ):
        require(required.lower() in method.lower(), f"MII method missing {required}")


def build_manifest() -> list[dict[str, str | int]]:
    targets: dict[str, Path] = {}
    for row in read_csv(MANIFEST_V8):
        targets[row["relative_path"]] = (ROOT / row["relative_path"]).resolve()
    additions = {
        "qa/ROMANCE_ACCEPTANCE_GATE_v8.json": GATE_V8,
        "qa/SHA256SUMS_v8.csv": MANIFEST_V8,
        "README.md": README,
        "CONTINUATION_CURSOR.md": CURSOR,
        "wordweb/PAN_ROMANCE_WORDWEB_v9.json": WORDWEB_V9,
        "access/PAN_ROMANCE_ACCESS_LEDGER_v9.json": ACCESS_V9_JSON,
        "access/PAN_ROMANCE_ACCESS_LEDGER_v9.csv": ACCESS_V9_CSV,
        "access/MII_METHOD_v9.md": METHOD_V9,
        "scripts/build_wordweb_and_access_v9.py": BUILDER_V9,
        "scripts/validate_romance_tranche_v9.py": Path(__file__).resolve(),
        "qa/WORDWEB_ACCESS_BUILD_v9.log": BUILD_LOG_V9,
        "wordweb/OCCURRENCE_REVIEW_PROTOCOL_v2.md": WORDWEB_DIR / "OCCURRENCE_REVIEW_PROTOCOL_v2.md",
        "wordweb/ROMANCE_TERM_OCCURRENCES_v2.csv": OCCURRENCES_V2,
        "wordweb/ROMANCE_TERM_OCCURRENCES_v2.json": WORDWEB_DIR / "ROMANCE_TERM_OCCURRENCES_v2.json",
        "wordweb/ROMANCE_TERM_OCCURRENCE_COVERAGE_v2.csv": WORDWEB_DIR / "ROMANCE_TERM_OCCURRENCE_COVERAGE_v2.csv",
        "wordweb/ROMANCE_OCCURRENCE_REVIEW_RM_RG_2024_DELTA_v1.csv": RM_DELTA_REVIEW,
        "wordweb/ROMANCE_OCCURRENCE_REVIEW_RM_RG_2024_DELTA_v1.json": RM_DELTA_REVIEW_JSON,
        "scripts/verify_pdf_renders_v10.py": ROOT / "scripts" / "verify_pdf_renders_v10.py",
        "qa/PDF_RENDER_REPRODUCIBILITY_v10.json": RENDER_V10,
        "qa/PDF_VISUAL_QA_v10.md": QA / "PDF_VISUAL_QA_v10.md",
    }
    for path in REVIEW_FILES + REVIEW_JSON_FILES:
        additions[path.relative_to(ROOT).as_posix()] = path
    for tranche in ("R823_HG_T005", "R823_HG_T006"):
        directory = ROOT / tranche
        for path in sorted(directory.rglob("*")):
            if not path.is_file():
                continue
            if path.suffix in {".aux", ".out"} or path.name == f"{tranche}_romance.log":
                continue
            additions[path.relative_to(ROOT).as_posix()] = path
        additions[f"../../../../output/pdf/{tranche}_controlled_romance.pdf"] = WORKSPACE / "output" / "pdf" / f"{tranche}_controlled_romance.pdf"
    targets.update(additions)
    rows = []
    for label, path in targets.items():
        require(path.exists(), f"manifest target missing: {label}")
        rows.append({"relative_path": label, "bytes": path.stat().st_size, "sha256": sha(path)})
    require(len(rows) == len({row["relative_path"] for row in rows}), "manifest labels not unique")
    with MANIFEST_V9.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["relative_path", "bytes", "sha256"], lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--core-only", action="store_true", help="validate data/tranches before updating successor documentation")
    args = parser.parse_args()
    core = validate_core(args.core_only)
    if args.core_only:
        print("PASS ROMANCE_V9_CORE_GATE")
        print("wordweb=60/106/39 evidence=802 reviewed=682 support_coverage=73/106")
        print("access=954 human_observations=0 pilot_eligible=0 promotions=0")
        print("stage_D=T001_T006_PASS next_authority_line=21256")
        return

    validate_docs()
    manifest_rows = build_manifest()
    gate = {
        "artifact": "ROMANCE_ACCEPTANCE_GATE_v9",
        "machine_validation": "PASS",
        "goal_status": "ACTIVE_NOT_COMPLETE",
        "predecessor_v8": {
            "status": "PRESERVED_IMMUTABLE_VERSIONED_PREDECESSOR",
            "wordweb_sha256": sha(WORDWEB_V8),
            "access_json_sha256": sha(ACCESS_V8_JSON),
            "access_csv_sha256": sha(ACCESS_V8_CSV),
            "gate_sha256": sha(GATE_V8),
            "manifest_sha256": sha(MANIFEST_V8),
            "manifest_rows": core["predecessor_manifest_rows"],
            "mutable_successor_pointer_paths": core["predecessor_manifest_live_mismatches"],
        },
        "stage_A": {
            "status": "NOT_COMPLETE", "explicit_routes": 61, "active_routes": 8,
            "zero_body_routes": 53, "romansh_general_school_math_bodies": 3,
            "romansh_specialist_algebra_bodies": 0, "romansh_regional_idiom_bodies": 0,
        },
        "stage_B": {
            "status": "CURRENT_CORPUS_TRANCHE_PASS", "records": 148,
            "primary_unique": 142, "representation_aliases": 6,
            "counting_eligible": 66, "excluded": 5,
        },
        "stage_C": {
            "status": "STRUCTURALLY_COMPLETE_REVIEW_LAYER_NOT_HUMAN_VALIDATED",
            "core_concepts": 60, "senses": 106, "c2_nodes": 39,
            "evidence_records": 802, "inherited_unresolved_claims": 120,
            "reviewed_occurrences": 682, "row_classifications": EXPECTED_ROW_CLASSES,
            "support_sense_links": 515, "adverse_sense_links": 129,
            "held_sense_links": 50, "form_admission_adverse_events": 20,
            "senses_with_accepted_support": 73, "senses_without_accepted_support": 33,
            "relation_records": 402, "valid_target_id_relation_edges": 27,
            "concept_to_sense_membership_edges": 106,
            "total_id_resolved_references_including_memberships": 133,
            "human_observations": 0, "core_form_promotions": 0,
        },
        "stage_D": core["stage_d"],
        "access_and_MII": {
            "sense_count": 106, "cohort_count": 9, "rows": 954,
            "human_result_fields_nonnull": 0, "human_observations": 0,
            "pilot_eligible_rows": 0, "form_promotions": 0,
            "empirical_MII_status": "ZERO_OBSERVATIONS_NOT_IMPLEMENTED",
            "diagnostic_boundary": "Orthographic proxy values are design diagnostics and do not measure intelligibility.",
        },
        "documentation_status": "CURRENT_V9",
        "pilot_claim": False,
        "full_R823_romance_translation_claim": False,
        "hash_target_count": len(manifest_rows),
        "hash_manifest_sha256": sha(MANIFEST_V9),
        "key_hashes": {row["relative_path"]: row["sha256"] for row in manifest_rows},
    }
    GATE_V9.write_text(json.dumps(gate, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "PASS machine_validation goal_status=ACTIVE_NOT_COMPLETE",
        "stage_A=NOT_COMPLETE routes=61 active=8 zero=53 rm_general_math=3 rm_specialist_algebra=0 rm_idioms=0",
        "stage_B=PASS records=148 primary_unique=142 counting_eligible=66 excluded=5",
        "stage_C=PASS_STRUCTURAL concepts=60 senses=106 c2=39 evidence=802 reviewed=682 accepted=510 rejected=127 held=45 supported_senses=73/106",
        "access=PASS rows=954 cohorts=9 human_observations=0 pilot_eligible=0 promotions=0 empirical_MII=ZERO_OBSERVATIONS",
        "stage_D=T001_T006_PASS outputs=6 render_pages=15/15 next=21256 human_validation=0",
        f"wordweb_v9_sha256={sha(WORDWEB_V9)}",
        f"access_v9_json_sha256={sha(ACCESS_V9_JSON)}",
        f"access_v9_csv_sha256={sha(ACCESS_V9_CSV)}",
        f"hash_targets={len(manifest_rows)} sha256_manifest={sha(MANIFEST_V9)}",
        f"gate_v9_sha256={sha(GATE_V9)}",
    ]
    GATE_LOG_V9.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
