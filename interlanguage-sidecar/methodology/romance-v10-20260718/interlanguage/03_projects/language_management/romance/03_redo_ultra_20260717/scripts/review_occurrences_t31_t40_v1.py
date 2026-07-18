#!/usr/bin/env python3
"""Build the frozen internal semantic review artifact for T31–T40.

The two reviewed Markdown reports are authoritative inputs. This generator
parses only their occurrence decision tables, joins those decisions to the
frozen occurrence manifest, validates every ID and sense, and emits a
deterministic CSV, JSON, and QA log. It performs no form promotion and records
no human observation, pilot result, or intelligibility claim.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


BASE = Path(__file__).resolve().parents[1]
ROMANCE_ROOT = BASE.parent
REPORT_DIR = ROMANCE_ROOT / "_agent_reports"

OCCURRENCE_MANIFEST = BASE / "wordweb" / "ROMANCE_TERM_OCCURRENCES_v1.csv"
WORDWEB = BASE / "wordweb" / "PAN_ROMANCE_WORDWEB_v7.json"
REPORT_31_35 = REPORT_DIR / "review_t31_t35.md"
REPORT_36_40 = REPORT_DIR / "review_t36_t40.md"

OUTPUT_CSV = BASE / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_T31_T40_v1.csv"
OUTPUT_JSON = BASE / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_T31_T40_v1.json"
OUTPUT_LOG = BASE / "qa" / "OCCURRENCE_REVIEW_T31_T40_v1.log"

EXPECTED_HASHES = {
    OCCURRENCE_MANIFEST: "6DF8FAD570D48369CA0A8FE06CD5A0EBC3C21275677E35BEDCF077208865DEE8",
    WORDWEB: "A48BF8C89F252A0274D2FDE2FE8A2E6E6E3077AD81A4B60BFA0B5FFF44A1A366",
    REPORT_31_35: "F9CA9A4D39633E15807537A5580A6538C3FB3E6D6FABDA64AD16E5E8FBF63C05",
    REPORT_36_40: "E49904C818014D4BB1E7CFD0D2501842706688A97436C247BC86AF5CD875D9F7",
}

EXPECTED_COUNTS = {
    "source_rows": 83,
    "accepted": 63,
    "rejected": 8,
    "held": 12,
    "accepted_navigation_lexical": 4,
    "accepted_running_body_context": 59,
}

EXPECTED_BY_TERM = {
    "T31": {"raw": 5, "accepted": 1, "rejected": 4, "held": 0},
    "T32": {"raw": 3, "accepted": 3, "rejected": 0, "held": 0},
    "T33": {"raw": 4, "accepted": 2, "rejected": 2, "held": 0},
    "T34": {"raw": 0, "accepted": 0, "rejected": 0, "held": 0},
    "T35": {"raw": 1, "accepted": 1, "rejected": 0, "held": 0},
    "T36": {"raw": 6, "accepted": 3, "rejected": 0, "held": 3},
    "T37": {"raw": 12, "accepted": 7, "rejected": 2, "held": 3},
    "T38": {"raw": 12, "accepted": 8, "rejected": 0, "held": 4},
    "T39": {"raw": 21, "accepted": 19, "rejected": 0, "held": 2},
    "T40": {"raw": 19, "accepted": 19, "rejected": 0, "held": 0},
}

EXPECTED_ZERO_RAW_TERMS = ["T34"]
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

REASON_CODES_31_35 = {
    "OCC-C19FB1EB927EFB35": "REDUCED_RING_DEFINITION_IDEMPOTENT_ERROR",
    "OCC-27EA2D245FC98E5A": "ORDINARY_VERB_REDUCES_PROBLEM",
    "OCC-B0A4B253AF8E3FBD": "ORDINARY_REDUCED_TO_MINIMUM",
    "OCC-E1E3164538F997B7": "RING_CLASS_NAVIGATION_LEXICAL",
    "OCC-6C6FE57D6F455878": "ORDINARY_GENERALITY_REDUCED",
    "OCC-025AEC5228CF20A3": "ASSOCIATED_PRIME_NAVIGATION_LEXICAL",
    "OCC-4E98383B66B7E594": "ASSOCIATED_PRIME_NAVIGATION_LEXICAL",
    "OCC-38A244D91A019BB8": "ASSOCIATED_PRIME_NAVIGATION_LEXICAL",
    "OCC-B1A727E2131F8229": "SET_COMPLEMENT_MONOID_FACE",
    "OCC-CAF8B9176750BBC1": "SET_COMPLEMENT_PRIME_IDEAL_PAIR",
    "OCC-945F069751ED6784": "MATRIX_COFACTOR_UNMODELED",
    "OCC-3B2790D9171F7137": "GROUP_COMPLEMENT_UNMODELED",
    "OCC-1351B5D65CB3CD74": "MONOID_CONGRUENCE_RELATION_DEFINITION",
}

ADVERSE_TARGETS_31_35 = {
    "OCC-C19FB1EB927EFB35": "T31-S1",
    "OCC-27EA2D245FC98E5A": "T31-form-admission",
    "OCC-B0A4B253AF8E3FBD": "T31-form-admission",
    "OCC-6C6FE57D6F455878": "T31-form-admission",
    "OCC-945F069751ED6784": "T33-form-admission",
    "OCC-3B2790D9171F7137": "T33-S1",
}

ACCEPTED_NAVIGATION_IDS = {
    "OCC-E1E3164538F997B7",
    "OCC-025AEC5228CF20A3",
    "OCC-4E98383B66B7E594",
    "OCC-38A244D91A019BB8",
}

HELD_IDS = {
    "OCC-4319C50EC2EE8199",
    "OCC-9503AD323D4B9512",
    "OCC-CD5BC44BDA9E07D3",
    "OCC-2EACDF8D40BD2232",
    "OCC-2C40AFE31C10C8AE",
    "OCC-4D8A78A5A6AB0050",
    "OCC-4B0BE8D09019A5AF",
    "OCC-294DFB7F51C36D81",
    "OCC-F52BB4F6D1E2A13F",
    "OCC-77D0BE7622072E31",
    "OCC-07552FD5F9AB9323",
    "OCC-52A474006C2DEF83",
}

# family_id, family_role, cross_occurrence_id
FAMILY_METADATA = {
    "OCC-E1E3164538F997B7": (
        "FAM-T31-FR-ANNEAU-REDUIT-NAV",
        "single_lexical_navigation_location",
        "",
    ),
    "OCC-025AEC5228CF20A3": (
        "FAM-T32-IT-PRIMO-ASSOCIATO-NAV",
        "template_primary_location",
        "",
    ),
    "OCC-4E98383B66B7E594": (
        "FAM-T32-IT-PRIMO-ASSOCIATO-NAV",
        "template_duplicate_location",
        "",
    ),
    "OCC-38A244D91A019BB8": (
        "FAM-T32-IT-PRIMO-ASSOCIATO-NAV",
        "template_duplicate_location",
        "",
    ),
    "OCC-4319C50EC2EE8199": (
        "HOLD-T36-CA-IDEAL-DIVISIBILITY-AMBIGUITY",
        "single_semantic_ambiguity",
        "",
    ),
    "OCC-9503AD323D4B9512": (
        "FAM-T36-IT-DIVISIBILITY-NAV",
        "template_primary_location",
        "",
    ),
    "OCC-CD5BC44BDA9E07D3": (
        "FAM-T36-IT-DIVISIBILITY-NAV",
        "template_duplicate_location",
        "",
    ),
    "OCC-2EACDF8D40BD2232": (
        "FAM-T37-IT-POWER-NAV",
        "template_primary_location",
        "",
    ),
    "OCC-2C40AFE31C10C8AE": (
        "FAM-T37-IT-POWER-NAV",
        "template_duplicate_location",
        "",
    ),
    "OCC-4D8A78A5A6AB0050": (
        "FAM-T37-IT-POWER-NAV",
        "template_duplicate_location",
        "",
    ),
    "OCC-4B0BE8D09019A5AF": (
        "HOLD-T38-FR-CODE-MACRO-COMMENT",
        "single_code_comment",
        "",
    ),
    "OCC-294DFB7F51C36D81": (
        "FAM-T38-IT-MATRIX-NAV",
        "template_primary_location",
        "",
    ),
    "OCC-F52BB4F6D1E2A13F": (
        "FAM-T38-IT-MATRIX-NAV",
        "template_duplicate_location",
        "",
    ),
    "OCC-77D0BE7622072E31": (
        "HOLD-T38-RO-TOC-COMPOUND",
        "single_toc_compound",
        "",
    ),
    "OCC-07552FD5F9AB9323": (
        "FAM-T39-T40-FR-SOUS-GROUPE-OVERLAP",
        "substring_held_for_T39",
        "OCC-0796F59803BE313C",
    ),
    "OCC-0796F59803BE313C": (
        "FAM-T39-T40-FR-SOUS-GROUPE-OVERLAP",
        "full_term_accepted_for_T40",
        "OCC-07552FD5F9AB9323",
    ),
    "OCC-52A474006C2DEF83": (
        "HOLD-T39-GL-TOC-COMPOUND",
        "single_toc_compound",
        "",
    ),
}

CSV_FIELDS = [
    "review_sequence",
    "occurrence_id",
    "term_id",
    "concept",
    "language",
    "source_candidate_sense_ids",
    "surface_query",
    "normalization_group",
    "logical_source_id",
    "record_id",
    "source_sha256",
    "license_status",
    "locator_path",
    "line_number",
    "quote",
    "quote_sha256",
    "source_domain",
    "source_evidence_tier",
    "review_decision",
    "accepted_sense_id",
    "candidate_sense_ids",
    "adverse_target",
    "reason_code",
    "review_note",
    "evidence_context_class",
    "evidence_family_id",
    "family_role",
    "cross_occurrence_id",
    "review_report",
    "review_report_sha256",
    "review_authority",
    "promotion_status",
    "human_observation_count",
    "pilot_claim",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def verify_inputs() -> None:
    mismatches = []
    for path, expected in EXPECTED_HASHES.items():
        actual = sha256(path)
        if actual != expected:
            mismatches.append(f"{path}: expected {expected}, got {actual}")
    if mismatches:
        raise SystemExit("input hash mismatch:\n" + "\n".join(mismatches))


def table_rows(path: Path) -> list[list[str]]:
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| OCC-"):
            continue
        rows.append([part.strip() for part in line.strip().strip("|").split("|")])
    return rows


def sense_token(value: str) -> str:
    match = re.search(r"T\d{2}-S\d+", value)
    return match.group(0) if match else ""


def clean_reason(value: str) -> str:
    return value.strip().strip(chr(96))


def parse_report_31_35() -> dict[str, dict]:
    decisions = {}
    for parts in table_rows(REPORT_31_35):
        if len(parts) != 4:
            raise SystemExit(f"unexpected T31–T35 table row: {parts!r}")
        occurrence_id, classification, sense_or_target, note = parts
        if classification == "accepted":
            decision = "accepted_sense_match"
            accepted_sense = sense_token(sense_or_target)
        elif classification == "rejected_adverse":
            decision = "rejected_adverse"
            accepted_sense = ""
        elif classification == "rejected_wrong_sense":
            decision = "rejected_wrong_sense"
            accepted_sense = ""
        else:
            raise SystemExit(
                f"unexpected T31–T35 classification for {occurrence_id}: "
                f"{classification}"
            )
        decisions[occurrence_id] = {
            "review_decision": decision,
            "accepted_sense_id": accepted_sense,
            "candidate_sense_ids": "",
            "adverse_target": ADVERSE_TARGETS_31_35.get(occurrence_id, ""),
            "reason_code": REASON_CODES_31_35[occurrence_id],
            "review_note": note,
            "review_report": REPORT_31_35.name,
            "review_report_sha256": EXPECTED_HASHES[REPORT_31_35],
            "report_language": "",
        }
    if len(decisions) != 13:
        raise SystemExit(f"expected 13 T31–T35 report rows, got {len(decisions)}")
    return decisions


def parse_report_36_40() -> dict[str, dict]:
    decisions = {}
    for parts in table_rows(REPORT_36_40):
        if len(parts) != 7:
            raise SystemExit(f"unexpected T36–T40 table row: {parts!r}")
        (
            occurrence_id,
            language,
            classification,
            sense_or_candidate,
            adverse_target,
            reason_code,
            note,
        ) = parts
        token = sense_token(sense_or_candidate)
        if classification == "accepted":
            decision = "accepted_sense_match"
            accepted_sense = token
            candidates = ""
        elif classification == "held":
            decision = "held"
            accepted_sense = ""
            candidates = token
        elif classification == "rejected/wrong sense":
            decision = "rejected_wrong_sense"
            accepted_sense = ""
            candidates = ""
        else:
            raise SystemExit(
                f"unexpected T36–T40 classification for {occurrence_id}: "
                f"{classification}"
            )
        decisions[occurrence_id] = {
            "review_decision": decision,
            "accepted_sense_id": accepted_sense,
            "candidate_sense_ids": candidates,
            "adverse_target": "" if adverse_target == "none" else adverse_target,
            "reason_code": clean_reason(reason_code),
            "review_note": note,
            "review_report": REPORT_36_40.name,
            "review_report_sha256": EXPECTED_HASHES[REPORT_36_40],
            "report_language": language,
        }
    if len(decisions) != 70:
        raise SystemExit(f"expected 70 T36–T40 report rows, got {len(decisions)}")
    return decisions


def evidence_context(decision: dict, occurrence_id: str) -> str:
    status = decision["review_decision"]
    reason = decision["reason_code"]
    if status == "accepted_sense_match":
        if occurrence_id in ACCEPTED_NAVIGATION_IDS:
            return "navigation_lexical_match_internal"
        return "running_body_semantic_match_internal"
    if status == "rejected_adverse":
        return "adverse_source_context"
    if status == "rejected_wrong_sense":
        return "wrong_sense_source_context"
    if reason == "IDEAL_DIVISIBILITY_DEFINITION_UNSTATED":
        return "held_semantic_ambiguity"
    if reason == "CODE_MACRO_COMMENT_ONLY":
        return "held_code_comment"
    if reason == "TOC_COMPOUND_ONLY":
        return "held_toc_compound"
    if reason == "SUBGROUP_DERIVATIONAL_SUBSTRING_LEAK":
        return "held_derivational_substring_overlap"
    return "held_navigation_or_template"


def load_source_rows() -> list[dict[str, str]]:
    with OCCURRENCE_MANIFEST.open(
        encoding="utf-8-sig", newline=""
    ) as handle:
        all_rows = list(csv.DictReader(handle))
    return [
        row
        for row in all_rows
        if 31 <= int(row["term_id"][1:]) <= 40
    ]


def load_senses() -> tuple[dict[str, str], list[str]]:
    data = json.loads(WORDWEB.read_text(encoding="utf-8"))
    sense_to_term = {
        sense["sense_id"]: sense["term_id"] for sense in data["senses"]
    }
    in_scope = sorted(
        sense_id
        for sense_id, term_id in sense_to_term.items()
        if 31 <= int(term_id[1:]) <= 40
    )
    return sense_to_term, in_scope


def category(status: str) -> str:
    if status == "accepted_sense_match":
        return "accepted"
    if status == "held":
        return "held"
    if status.startswith("rejected_"):
        return "rejected"
    raise ValueError(status)


def build_records() -> tuple[list[dict], dict]:
    decisions = parse_report_31_35()
    overlap = set(decisions) & set(parse_report_36_40())
    if overlap:
        raise SystemExit(f"duplicate report decision IDs: {sorted(overlap)}")
    decisions.update(parse_report_36_40())

    source_rows = load_source_rows()
    source_ids = [row["occurrence_id"] for row in source_rows]
    if len(source_ids) != len(set(source_ids)):
        raise SystemExit("source occurrence IDs are not unique")
    if len(source_ids) != EXPECTED_COUNTS["source_rows"]:
        raise SystemExit(
            f"expected {EXPECTED_COUNTS['source_rows']} source rows, "
            f"got {len(source_ids)}"
        )
    if set(source_ids) != set(decisions):
        raise SystemExit(
            "decision/source ID mismatch: "
            f"missing={sorted(set(source_ids) - set(decisions))}; "
            f"extra={sorted(set(decisions) - set(source_ids))}"
        )

    sense_to_term, in_scope_senses = load_senses()
    records = []
    for sequence, source in enumerate(source_rows, 1):
        occurrence_id = source["occurrence_id"]
        review = decisions[occurrence_id]
        if review["report_language"] and (
            review["report_language"] != source["language"]
        ):
            raise SystemExit(
                f"report/source language mismatch for {occurrence_id}"
            )
        accepted_sense = review["accepted_sense_id"]
        candidate_sense = review["candidate_sense_ids"]
        for reviewed_sense in [accepted_sense, candidate_sense]:
            if not reviewed_sense:
                continue
            if sense_to_term.get(reviewed_sense) != source["term_id"]:
                raise SystemExit(
                    f"sense/term mismatch for {occurrence_id}: "
                    f"{reviewed_sense} vs {source['term_id']}"
                )

        family_id, family_role, cross_id = FAMILY_METADATA.get(
            occurrence_id, ("", "", "")
        )
        record = {
            "review_sequence": sequence,
            "occurrence_id": occurrence_id,
            "term_id": source["term_id"],
            "concept": source["concept"],
            "language": source["language"],
            "source_candidate_sense_ids": source["sense_ids"],
            "surface_query": source["surface_query"],
            "normalization_group": source["normalization_group"],
            "logical_source_id": source["logical_source_id"],
            "record_id": source["record_id"],
            "source_sha256": source["source_sha256"],
            "license_status": source["license_status"],
            "locator_path": source["locator_path"],
            "line_number": int(source["line_number"]),
            "quote": source["quote"],
            "quote_sha256": source["quote_sha256"],
            "source_domain": source["source_domain"],
            "source_evidence_tier": source["evidence_tier"],
            "review_decision": review["review_decision"],
            "accepted_sense_id": accepted_sense,
            "candidate_sense_ids": candidate_sense,
            "adverse_target": review["adverse_target"],
            "reason_code": review["reason_code"],
            "review_note": review["review_note"],
            "evidence_context_class": evidence_context(
                review, occurrence_id
            ),
            "evidence_family_id": family_id,
            "family_role": family_role,
            "cross_occurrence_id": cross_id,
            "review_report": review["review_report"],
            "review_report_sha256": review["review_report_sha256"],
            "review_authority": (
                "codex_internal_semantic_review_not_human"
            ),
            "promotion_status": "not_promoted",
            "human_observation_count": 0,
            "pilot_claim": False,
        }
        records.append(record)

    if {
        record["occurrence_id"]
        for record in records
        if record["review_decision"] == "held"
    } != HELD_IDS:
        raise SystemExit("held ID set does not match the reviewed hold set")
    if any(
        not record["evidence_family_id"]
        for record in records
        if record["review_decision"] == "held"
    ):
        raise SystemExit("every held row must preserve a hold/family identity")

    # Validate the physical overlap behind the T39 substring hold.
    record_by_id = {record["occurrence_id"]: record for record in records}
    overlap_a = record_by_id["OCC-07552FD5F9AB9323"]
    overlap_b = record_by_id["OCC-0796F59803BE313C"]
    for field in (
        "logical_source_id",
        "record_id",
        "line_number",
        "quote_sha256",
    ):
        if overlap_a[field] != overlap_b[field]:
            raise SystemExit(f"T39/T40 overlap mismatch in {field}")

    status_counts = Counter(category(r["review_decision"]) for r in records)
    context_counts = Counter(r["evidence_context_class"] for r in records)
    by_term = {}
    for term_number in range(31, 41):
        term_id = f"T{term_number:02d}"
        term_records = [r for r in records if r["term_id"] == term_id]
        term_counts = Counter(
            category(r["review_decision"]) for r in term_records
        )
        by_term[term_id] = {
            "raw": len(term_records),
            "accepted": term_counts["accepted"],
            "rejected": term_counts["rejected"],
            "held": term_counts["held"],
        }

    accepted_by_sense = Counter(
        r["accepted_sense_id"]
        for r in records
        if r["review_decision"] == "accepted_sense_match"
    )
    zero_raw_terms = [
        term_id for term_id, counts in by_term.items() if counts["raw"] == 0
    ]
    zero_accepted_senses = sorted(
        set(in_scope_senses) - set(accepted_by_sense)
    )

    actual_counts = {
        "source_rows": len(records),
        "accepted": status_counts["accepted"],
        "rejected": status_counts["rejected"],
        "held": status_counts["held"],
        "accepted_navigation_lexical": context_counts[
            "navigation_lexical_match_internal"
        ],
        "accepted_running_body_context": context_counts[
            "running_body_semantic_match_internal"
        ],
    }
    if actual_counts != EXPECTED_COUNTS:
        raise SystemExit(
            f"aggregate count mismatch: {actual_counts} != {EXPECTED_COUNTS}"
        )
    if by_term != EXPECTED_BY_TERM:
        raise SystemExit(f"term count mismatch: {by_term}")
    if zero_raw_terms != EXPECTED_ZERO_RAW_TERMS:
        raise SystemExit(f"zero-raw mismatch: {zero_raw_terms}")
    if zero_accepted_senses != EXPECTED_ZERO_ACCEPTED_SENSES:
        raise SystemExit(
            f"zero-accepted-sense mismatch: {zero_accepted_senses}"
        )
    if any(r["promotion_status"] != "not_promoted" for r in records):
        raise SystemExit("promotion status leak")
    if sum(r["human_observation_count"] for r in records) != 0:
        raise SystemExit("human observation leak")
    if any(r["pilot_claim"] for r in records):
        raise SystemExit("pilot claim leak")

    family_groups = defaultdict(list)
    for record in records:
        if record["evidence_family_id"]:
            family_groups[record["evidence_family_id"]].append(record)
    families = []
    for family_id in sorted(family_groups):
        members = family_groups[family_id]
        families.append(
            {
                "evidence_family_id": family_id,
                "occurrence_ids": [r["occurrence_id"] for r in members],
                "family_roles": {
                    r["occurrence_id"]: r["family_role"] for r in members
                },
                "decisions": {
                    r["occurrence_id"]: r["review_decision"] for r in members
                },
                "cross_occurrence_ids": {
                    r["occurrence_id"]: r["cross_occurrence_id"]
                    for r in members
                    if r["cross_occurrence_id"]
                },
            }
        )

    summary = {
        "counts": actual_counts,
        "by_term": by_term,
        "accepted_by_sense": dict(sorted(accepted_by_sense.items())),
        "zero_raw_hit_terms": zero_raw_terms,
        "zero_accepted_senses": zero_accepted_senses,
        "evidence_context_counts": dict(sorted(context_counts.items())),
        "evidence_families": families,
    }
    return records, summary


def write_csv(records: list[dict]) -> None:
    with OUTPUT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=CSV_FIELDS, lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(records)


def write_json(records: list[dict], summary: dict) -> None:
    payload = {
        "artifact": "ROMANCE_OCCURRENCE_REVIEW_T31_T40_v1",
        "schema_version": "1.0",
        "review_date": "2026-07-17",
        "generated_by": Path(__file__).name,
        "generator_sha256": sha256(Path(__file__).resolve()),
        "input_hashes": {
            path.name: expected for path, expected in EXPECTED_HASHES.items()
        },
        "scope": {
            "term_ids": [f"T{number:02d}" for number in range(31, 41)],
            "source_occurrence_id_count": 83,
            "source_occurrence_ids_exactly_once": True,
            "T34_zero_raw_hit": True,
        },
        "boundary": {
            "review_authority": (
                "codex_internal_semantic_review_not_human"
            ),
            "accepted_navigation_is_lexical_not_body_attestation": True,
            "form_promotion_count": 0,
            "human_observation_count": 0,
            "pilot_or_intelligibility_claim_count": 0,
        },
        **summary,
        "records": records,
    }
    OUTPUT_JSON.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def write_log(summary: dict) -> None:
    counts = summary["counts"]
    lines = [
        "ROMANCE OCCURRENCE REVIEW T31-T40 v1",
        "status=PASS",
        f"generator_sha256={sha256(Path(__file__).resolve())}",
        (
            "occurrence_manifest_sha256="
            f"{EXPECTED_HASHES[OCCURRENCE_MANIFEST]}"
        ),
        f"wordweb_v7_sha256={EXPECTED_HASHES[WORDWEB]}",
        f"review_t31_t35_sha256={EXPECTED_HASHES[REPORT_31_35]}",
        f"review_t36_t40_sha256={EXPECTED_HASHES[REPORT_36_40]}",
        f"source_ids={counts['source_rows']}",
        "source_ids_exactly_once=true",
        f"accepted_sense_matches={counts['accepted']}",
        f"rejected_wrong_or_adverse={counts['rejected']}",
        f"held={counts['held']}",
        (
            "accepted_navigation_lexical_not_body="
            f"{counts['accepted_navigation_lexical']}"
        ),
        (
            "accepted_running_body_context_matches="
            f"{counts['accepted_running_body_context']}"
        ),
        "T34_raw_hits=0",
        "zero_accepted_senses="
        + "|".join(summary["zero_accepted_senses"]),
        "held_rows_all_have_family_or_hold_identity=true",
        "T32_repeated_navigation_family_preserved=true",
        "T39_T40_subgroup_substring_overlap_preserved=true",
        "form_promotions=0",
        "human_observations=0",
        "pilot_or_intelligibility_claims=0",
        f"output_csv_sha256={sha256(OUTPUT_CSV)}",
        f"output_json_sha256={sha256(OUTPUT_JSON)}",
    ]
    OUTPUT_LOG.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    verify_inputs()
    records, summary = build_records()
    write_csv(records)
    write_json(records, summary)
    write_log(summary)


if __name__ == "__main__":
    main()
