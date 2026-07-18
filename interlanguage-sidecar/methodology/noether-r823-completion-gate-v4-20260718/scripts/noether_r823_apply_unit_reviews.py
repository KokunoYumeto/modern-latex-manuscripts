#!/usr/bin/env python3
"""Bind explicit unit-review records to an R823 parity-ledger seed.

This helper never infers review from structural metrics.  A unit is promoted only
when a supplied review record is explicitly source-reconciled, has substantive
method/findings fields, and its exact source and target unit hashes match the
document-bound seed.
"""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


HEX64 = re.compile(r"[0-9A-Fa-f]{64}")
REQUIRED_REVIEW_COLUMNS = {
    "unit_id",
    "source_sha256",
    "target_sha256",
    "status",
    "review_method",
    "review_findings",
}


def read_rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def normalized(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.strip().lower()).strip("-")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed-ledger", type=Path, required=True)
    parser.add_argument("--review-csv", type=Path, action="append", required=True)
    parser.add_argument("--output-csv", type=Path, required=True)
    args = parser.parse_args()

    seed_fields, seed_rows = read_rows(args.seed_ledger)
    required_seed = {
        "unit_id",
        "source_sha256",
        "target_sha256",
        "target_document_sha256",
        "status",
        "review_evidence",
        "notes",
    }
    missing_seed = required_seed - set(seed_fields)
    if missing_seed:
        raise ValueError(f"seed ledger missing columns: {sorted(missing_seed)}")

    seed_by_unit: dict[str, dict[str, str]] = {}
    for row in seed_rows:
        unit = row["unit_id"].strip()
        if not unit or unit in seed_by_unit:
            raise ValueError(f"blank or duplicate seed unit: {unit!r}")
        if not HEX64.fullmatch(row["target_document_sha256"].strip()):
            raise ValueError(f"seed unit {unit} lacks a document-bound target hash")
        seed_by_unit[unit] = row

    reviews: dict[str, tuple[Path, dict[str, str]]] = {}
    for review_path in args.review_csv:
        review_fields, review_rows = read_rows(review_path)
        missing = REQUIRED_REVIEW_COLUMNS - set(review_fields)
        if missing:
            raise ValueError(f"{review_path} missing review columns: {sorted(missing)}")
        for row in review_rows:
            unit = row["unit_id"].strip()
            if not unit:
                raise ValueError(f"{review_path} contains a blank unit_id")
            if unit in reviews:
                raise ValueError(f"duplicate review record for {unit}")
            reviews[unit] = (review_path, row)

    promoted: list[str] = []
    rejected: list[str] = []
    for unit, row in seed_by_unit.items():
        record = reviews.get(unit)
        if not record:
            continue
        review_path, review = record
        exact_hashes = (
            HEX64.fullmatch(review["source_sha256"].strip())
            and HEX64.fullmatch(review["target_sha256"].strip())
            and review["source_sha256"].upper() == row["source_sha256"].upper()
            and review["target_sha256"].upper() == row["target_sha256"].upper()
        )
        substantive = (
            normalized(review["status"]) == "source-reconciled"
            and len(review["review_method"].strip()) >= 12
            and len(review["review_findings"].strip()) >= 12
        )
        if not exact_hashes or not substantive:
            rejected.append(unit)
            continue
        row["status"] = "source-reconciled"
        row["review_evidence"] = (
            f"{review_path.resolve()}#unit_id={unit}; "
            f"method={review['review_method'].strip()}; "
            f"finding={review['review_findings'].strip()}"
        )
        row["notes"] = review.get("notes", "").strip() or review["review_findings"].strip()
        promoted.append(unit)

    unknown_reviews = sorted(set(reviews) - set(seed_by_unit))
    if unknown_reviews:
        raise ValueError(f"review records not present in seed: {unknown_reviews}")
    if rejected:
        raise ValueError(f"review records failed exact-hash/substance checks: {rejected}")

    args.output_csv.parent.mkdir(parents=True, exist_ok=True)
    with args.output_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=seed_fields)
        writer.writeheader()
        writer.writerows(seed_rows)
    pending = [row["unit_id"] for row in seed_rows if normalized(row["status"]) != "source-reconciled"]
    print(f"wrote {len(seed_rows)} rows to {args.output_csv}")
    print(f"exact_hash_reviews_applied={len(promoted)}")
    print(f"pending={len(pending)}:{','.join(pending)}")


if __name__ == "__main__":
    main()
