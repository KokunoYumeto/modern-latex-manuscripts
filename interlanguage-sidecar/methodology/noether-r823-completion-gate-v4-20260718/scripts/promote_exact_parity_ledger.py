#!/usr/bin/env python3
"""Promote an exact R823 parity seed only through current keyed evidence.

The v3 seed owns all source, target, and whole-document hashes.  This helper
does not calculate or alter them.  For every unit, the routed UTF-8 evidence
must explicitly contain the unit id, its exact source and target hashes, and
the exact whole expanded-target hash.  Merely creating a mapped file therefore
cannot manufacture ``source-reconciled`` status.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
from pathlib import Path


MAP_FIELDS = (
    "unit_id",
    "evidence_path",
    "evidence_record",
    "review_scope",
    "notes",
)
SEED_HASH_FIELDS = (
    "source_sha256",
    "target_sha256",
    "target_document_sha256",
)
HEX64 = re.compile(r"^[0-9A-F]{64}$")
LINE_RANGE = re.compile(
    r"(?i)(?:lines?\s*|L\s*)[:.]?\s*(\d+)\s*(?:--|[-–—])\s*(?:L\s*)?(\d+)"
)
REQUIRED_UNITS = (
    tuple(f"P{number:02d}" for number in range(1, 44))
    + ("BOOK_TITLE_INTRO",)
    + tuple(f"BOOK_S{number:02d}" for number in range(1, 32))
    + (
        "POST45_MAIN",
        "POST45_NOETHER_SUPPLEMENT",
        "BIBLIOGRAPHY",
        "SHORT_NOTICES",
        "BOOK_REVIEWS",
        "BOOKS_WITH_NOETHER",
    )
)
UNIT_EVIDENCE_FIELDS = (
    "unit_id",
    "source_sha256",
    "target_sha256",
    "target_document_sha256",
    "source_locator",
    "target_locator",
    "method",
    "reviewed_structures",
    "reviewed_formulas",
    "reviewed_notes",
    "findings",
    "reviewer_provenance",
    "supporting_artifacts",
    "supporting_artifact_sha256",
    "status",
)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def keyed(rows: list[dict[str, str]], label: str) -> dict[str, dict[str, str]]:
    result: dict[str, dict[str, str]] = {}
    for row in rows:
        unit = row.get("unit_id", "").strip()
        if not unit:
            raise ValueError(f"{label}: blank unit_id")
        if unit in result:
            raise ValueError(f"{label}: duplicate unit_id {unit}")
        result[unit] = row
    return result


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def require_line_range(value: str, *, label: str) -> None:
    match = LINE_RANGE.search(value)
    if match is None:
        raise ValueError(f"{label}: no explicit numeric line range in {value!r}")
    start, end = (int(part) for part in match.groups())
    if start < 1 or end < start:
        raise ValueError(f"{label}: invalid line range {start}--{end}")


def require_current_keyed_markdown_evidence(
    *,
    unit: str,
    seed_row: dict[str, str],
    evidence_path: Path,
) -> None:
    try:
        evidence_text = evidence_path.read_text(encoding="utf-8", errors="strict")
    except UnicodeError as exc:
        raise ValueError(f"{unit}: review evidence is not strict UTF-8: {evidence_path}") from exc
    if len(evidence_text.strip()) < 256:
        raise ValueError(f"{unit}: review evidence is not substantive: {evidence_path}")

    unit_pattern = re.compile(
        rf"(?<![A-Z0-9_]){re.escape(unit)}(?![A-Z0-9_])",
        re.IGNORECASE,
    )
    if unit_pattern.search(evidence_text) is None:
        raise ValueError(f"{unit}: unit id is absent from review evidence {evidence_path}")

    evidence_upper = evidence_text.upper()
    for field in SEED_HASH_FIELDS:
        value = seed_row.get(field, "").strip().upper()
        if HEX64.fullmatch(value) is None:
            raise ValueError(f"{unit}: seed has invalid {field}: {value!r}")
        if value not in evidence_upper:
            raise ValueError(
                f"{unit}: current {field} {value} is absent from review evidence "
                f"{evidence_path}"
            )


def require_current_keyed_csv_evidence(
    *,
    unit: str,
    record_id: str,
    seed_row: dict[str, str],
    evidence_path: Path,
) -> str:
    evidence_rows = read_csv(evidence_path)
    evidence_by_unit = keyed(evidence_rows, f"unit evidence {evidence_path}")
    actual_columns = set(evidence_rows[0]) if evidence_rows else set()
    missing_columns = set(UNIT_EVIDENCE_FIELDS) - actual_columns
    if missing_columns:
        raise ValueError(
            f"{unit}: unit-evidence CSV is missing columns {sorted(missing_columns)}"
        )
    if record_id != unit:
        raise ValueError(
            f"{unit}: evidence_record must be the exact unit id, got {record_id!r}"
        )
    if record_id not in evidence_by_unit:
        raise ValueError(
            f"{unit}: no direct record {record_id!r} in unit evidence {evidence_path}"
        )
    evidence_row = evidence_by_unit[record_id]

    for field in SEED_HASH_FIELDS:
        expected = seed_row.get(field, "").strip().upper()
        found = evidence_row.get(field, "").strip().upper()
        if HEX64.fullmatch(expected) is None:
            raise ValueError(f"{unit}: seed has invalid {field}: {expected!r}")
        if found != expected:
            raise ValueError(
                f"{unit}: evidence {field} is stale: found {found!r}; expected {expected}"
            )

    narrative_fields = (
        "source_locator",
        "target_locator",
        "method",
        "reviewed_structures",
        "reviewed_formulas",
        "reviewed_notes",
        "findings",
        "reviewer_provenance",
    )
    blank_fields = [
        field for field in narrative_fields if not evidence_row.get(field, "").strip()
    ]
    if blank_fields:
        raise ValueError(f"{unit}: blank substantive evidence fields {blank_fields}")
    minimum_field_lengths = {
        "source_locator": 18,
        "target_locator": 18,
        "method": 45,
        "reviewed_structures": 55,
        "reviewed_formulas": 55,
        "reviewed_notes": 45,
        "findings": 55,
        "reviewer_provenance": 35,
    }
    thin_fields = [
        field
        for field, minimum in minimum_field_lengths.items()
        if len(evidence_row.get(field, "").strip()) < minimum
    ]
    if thin_fields:
        raise ValueError(f"{unit}: thin substantive evidence fields {thin_fields}")
    for locator_field in ("source_locator", "target_locator"):
        locator = evidence_row.get(locator_field, "").strip()
        require_line_range(locator, label=f"{unit} {locator_field}")
    narrative_size = sum(
        len(evidence_row.get(field, "").strip()) for field in narrative_fields
    )
    if narrative_size < 320:
        raise ValueError(
            f"{unit}: unit review is too thin ({narrative_size} narrative characters)"
        )
    if re.sub(r"[^a-z0-9]+", "-", evidence_row.get("status", "").casefold()).strip("-") != "source-reconciled":
        raise ValueError(
            f"{unit}: unit-evidence status is not source-reconciled: "
            f"{evidence_row.get('status', '')!r}"
        )

    artifact_values = [
        value.strip()
        for value in evidence_row.get("supporting_artifacts", "").split(";")
        if value.strip()
    ]
    artifact_hashes = [
        value.strip().upper()
        for value in evidence_row.get("supporting_artifact_sha256", "").split(";")
        if value.strip()
    ]
    if not artifact_values or len(artifact_values) != len(artifact_hashes):
        raise ValueError(
            f"{unit}: supporting artifact paths/hashes are absent or count-mismatched"
        )
    for raw_artifact, expected_hash in zip(artifact_values, artifact_hashes):
        artifact_path = Path(raw_artifact)
        if not artifact_path.is_absolute():
            artifact_path = evidence_path.parent / artifact_path
        artifact_path = artifact_path.resolve()
        if not artifact_path.is_file():
            raise ValueError(f"{unit}: missing supporting artifact {artifact_path}")
        if HEX64.fullmatch(expected_hash) is None:
            raise ValueError(
                f"{unit}: invalid supporting artifact hash {expected_hash!r}"
            )
        live_hash = sha256(artifact_path)
        if live_hash != expected_hash:
            raise ValueError(
                f"{unit}: supporting artifact hash mismatch for {artifact_path}: "
                f"found {live_hash}; expected {expected_hash}"
            )

    substance_fields = (
        "method",
        "reviewed_structures",
        "reviewed_formulas",
        "reviewed_notes",
        "findings",
    )
    return "|".join(
        re.sub(r"\s+", " ", evidence_row.get(field, "").strip()).casefold()
        for field in substance_fields
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed-ledger", type=Path, required=True)
    parser.add_argument("--evidence-map", type=Path, required=True)
    parser.add_argument("--output-csv", type=Path, required=True)
    args = parser.parse_args()

    seed_rows = read_csv(args.seed_ledger)
    map_rows = read_csv(args.evidence_map)
    seed = keyed(seed_rows, "seed ledger")
    evidence = keyed(map_rows, "evidence map")
    if len(seed_rows) != 81:
        raise ValueError(f"seed ledger must contain exactly 81 rows, got {len(seed_rows)}")
    required_units = set(REQUIRED_UNITS)
    if set(seed) != required_units:
        raise ValueError(
            "seed ledger must contain the canonical 81 R823 unit IDs; "
            f"missing={sorted(required_units - set(seed))}; "
            f"extra={sorted(set(seed) - required_units)}"
        )
    if set(seed) != set(evidence):
        raise ValueError(
            "unit mismatch: "
            f"missing_from_map={sorted(set(seed) - set(evidence))}; "
            f"extra_in_map={sorted(set(evidence) - set(seed))}"
        )
    whole_hashes = {
        row.get("target_document_sha256", "").strip().upper()
        for row in seed_rows
    }
    if len(whole_hashes) != 1 or HEX64.fullmatch(next(iter(whole_hashes), "")) is None:
        raise ValueError(
            "seed ledger must carry one valid target_document_sha256 "
            f"across all 81 rows; found {sorted(whole_hashes)}"
        )

    evidence_root = args.evidence_map.parent
    csv_corpora: dict[Path, dict[str, dict[str, str]]] = {}
    for mapping in map_rows:
        raw_path = mapping.get("evidence_path", "").strip()
        if not raw_path:
            continue
        candidate = Path(raw_path)
        resolved = candidate if candidate.is_absolute() else evidence_root / candidate
        resolved = resolved.resolve()
        if resolved.suffix.casefold() != ".csv" or not resolved.is_file():
            continue
        if resolved not in csv_corpora:
            rows = read_csv(resolved)
            corpus = keyed(rows, f"unit evidence {resolved}")
            if len(rows) != 81 or set(corpus) != required_units:
                raise ValueError(
                    f"direct unit-evidence corpus {resolved} must contain exactly "
                    f"the 81 seed units; rows={len(rows)}, "
                    f"missing={sorted(required_units - set(corpus))}, "
                    f"extra={sorted(set(corpus) - required_units)}"
                )
            csv_corpora[resolved] = corpus

    required_map_columns = set(MAP_FIELDS)
    actual_map_columns = set(map_rows[0]) if map_rows else set()
    if not required_map_columns <= actual_map_columns:
        raise ValueError(
            f"evidence map missing columns {sorted(required_map_columns - actual_map_columns)}"
        )

    promoted: list[dict[str, str]] = []
    narrative_signatures: dict[str, str] = {}
    for row in seed_rows:
        unit = row["unit_id"].strip()
        mapping = evidence[unit]
        raw_path = mapping.get("evidence_path", "").strip()
        evidence_record = mapping.get("evidence_record", "").strip()
        review_scope = mapping.get("review_scope", "").strip()
        if not raw_path or not evidence_record or not review_scope:
            raise ValueError(
                f"{unit}: blank evidence_path, evidence_record, or review_scope"
            )
        candidate = Path(raw_path)
        resolved = candidate if candidate.is_absolute() else evidence_root / candidate
        resolved = resolved.resolve()
        if not resolved.is_file() or resolved.stat().st_size == 0:
            raise ValueError(f"{unit}: missing or empty review evidence {resolved}")
        if resolved.suffix.casefold() != ".csv":
            raise ValueError(
                f"{unit}: direct unit evidence must be a keyed CSV, not {resolved.suffix!r}"
            )
        narrative_signature = require_current_keyed_csv_evidence(
            unit=unit,
            record_id=evidence_record,
            seed_row=row,
            evidence_path=resolved,
        )
        if narrative_signature in narrative_signatures:
            raise ValueError(
                f"{unit}: substantive review duplicates unit "
                f"{narrative_signatures[narrative_signature]} exactly"
            )
        narrative_signatures[narrative_signature] = unit
        evidence_hash = sha256(resolved)
        updated = dict(row)
        updated["status"] = "source-reconciled"
        updated["review_evidence"] = (
            f"{raw_path}#{evidence_record} "
            f"[SHA-256 {evidence_hash}; {review_scope}]"
        )
        updated["notes"] = mapping.get("notes", "").strip()
        promoted.append(updated)

    fieldnames = list(seed_rows[0])
    args.output_csv.parent.mkdir(parents=True, exist_ok=True)
    with args.output_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(promoted)
    print(f"promoted {len(promoted)} exact-hash rows to {args.output_csv}")


if __name__ == "__main__":
    main()
