#!/usr/bin/env python3
"""Join verified source/target manifests into a conservative parity ledger.

Rows are never promoted automatically.  Existing review state is retained only
when both exact unit hashes and the whole expanded target-document hash are
unchanged; otherwise the row returns to pending.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

from noether_r823_completion_gate import HEX64, REQUIRED_UNITS, normalized_status


FIELDS = (
    "unit_id",
    "source_start_line",
    "source_end_line",
    "source_chars",
    "source_sha256",
    "target_start_line",
    "target_end_line",
    "target_chars",
    "target_sha256",
    "target_document_sha256",
    "status",
    "review_evidence",
    "notes",
)


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def by_unit(rows: list[dict[str, str]], label: str) -> dict[str, dict[str, str]]:
    result: dict[str, dict[str, str]] = {}
    for row in rows:
        unit = row.get("unit_id", "").strip()
        if not unit:
            raise ValueError(f"{label} contains a row without unit_id")
        if unit in result:
            raise ValueError(f"{label} contains duplicate unit_id {unit}")
        result[unit] = row
    missing = [unit for unit in REQUIRED_UNITS if unit not in result]
    extra = sorted(set(result) - set(REQUIRED_UNITS))
    if missing or extra:
        raise ValueError(f"{label} unit mismatch: missing={missing}; extra={extra}")
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-manifest", type=Path, required=True)
    parser.add_argument("--target-manifest", type=Path, required=True)
    parser.add_argument("--existing-ledger", type=Path)
    parser.add_argument("--output-csv", type=Path, required=True)
    args = parser.parse_args()

    source = by_unit(read_rows(args.source_manifest), "source manifest")
    target = by_unit(read_rows(args.target_manifest), "target manifest")
    target_document_hashes = {
        row.get("target_document_sha256", "").upper()
        for row in target.values()
    }
    if (
        len(target_document_hashes) != 1
        or not HEX64.fullmatch(next(iter(target_document_hashes), ""))
    ):
        raise ValueError(
            "target manifest must carry one valid whole-document SHA-256 across all rows: "
            f"{sorted(target_document_hashes)}"
        )
    existing: dict[str, dict[str, str]] = {}
    if args.existing_ledger and args.existing_ledger.is_file():
        existing = by_unit(read_rows(args.existing_ledger), "existing ledger")

    rows: list[dict[str, str]] = []
    retained = reset = 0
    for unit in REQUIRED_UNITS:
        source_row = source[unit]
        target_row = target[unit]
        old = existing.get(unit)
        hashes_unchanged = bool(
            old
            and old.get("source_sha256", "").upper() == source_row["source_sha256"].upper()
            and old.get("target_sha256", "").upper() == target_row["target_sha256"].upper()
            and old.get("target_document_sha256", "").upper()
            == target_row.get("target_document_sha256", "").upper()
            and bool(target_row.get("target_document_sha256", "").strip())
        )
        if hashes_unchanged:
            status = old.get("status", "pending-source-reconciliation")
            review_evidence = old.get("review_evidence", "")
            notes = old.get("notes", "")
            retained += 1
        else:
            status = "pending-source-reconciliation"
            review_evidence = ""
            old_status = normalized_status(old.get("status", "")) if old else ""
            notes = (
                f"hash changed; prior status {old_status or 'absent'} invalidated"
                if old
                else ""
            )
            reset += 1

        rows.append(
            {
                "unit_id": unit,
                "source_start_line": source_row["start_line"],
                "source_end_line": source_row["end_line"],
                "source_chars": source_row["chars"],
                "source_sha256": source_row["source_sha256"].upper(),
                "target_start_line": target_row["target_start_line"],
                "target_end_line": target_row["target_end_line"],
                "target_chars": target_row["target_chars"],
                "target_sha256": target_row["target_sha256"].upper(),
                "target_document_sha256": target_row["target_document_sha256"].upper(),
                "status": status,
                "review_evidence": review_evidence,
                "notes": notes,
            }
        )

    args.output_csv.parent.mkdir(parents=True, exist_ok=True)
    with args.output_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {len(rows)} rows to {args.output_csv}")
    print(f"retained_exact_hash_review_state={retained}")
    print(f"pending_or_reset={reset}")


if __name__ == "__main__":
    main()
