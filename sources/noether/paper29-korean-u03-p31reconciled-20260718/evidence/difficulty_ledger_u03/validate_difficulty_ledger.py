#!/usr/bin/env python3
"""Validate U03 difficulty schema, hash chain, IDs, projections, and relations."""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

import jsonschema


HERE = Path(__file__).resolve().parent
REPORT = HERE / "DIFFICULTY_LEDGER_VALIDATION_REPORT.json"
ZERO = "0" * 64


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def payload_hash(record: dict) -> str:
    payload = {key: value for key, value in record.items() if key != "record_hash"}
    encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest().upper()


def main() -> int:
    errors: list[str] = []
    schema = json.loads((HERE / "DIFFICULTY_LEDGER.schema.json").read_text(encoding="utf-8"))
    records = [
        json.loads(line)
        for line in (HERE / "DIFFICULTY_LEDGER.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    rows = list(csv.DictReader((HERE / "DIFFICULTY_LEDGER.csv").open(encoding="utf-8", newline="")))
    expected_previous = ZERO
    ids: set[str] = set()
    for index, record in enumerate(records, start=1):
        try:
            jsonschema.validate(record, schema)
        except jsonschema.ValidationError as exc:
            errors.append(f"{record.get('difficulty_id', index)} schema: {exc.message}")
        if record["difficulty_id"] in ids:
            errors.append(f"duplicate ID {record['difficulty_id']}")
        ids.add(record["difficulty_id"])
        if record["previous_hash"] != expected_previous:
            errors.append(f"{record['difficulty_id']}: previous_hash mismatch")
        actual = payload_hash(record)
        if record["record_hash"] != actual:
            errors.append(f"{record['difficulty_id']}: record_hash mismatch")
        expected_previous = record["record_hash"]
    if len(rows) != len(records):
        errors.append("CSV/JSONL count mismatch")
    metadata = json.loads((HERE / "DIFFICULTY_LEDGER_METADATA.json").read_text(encoding="utf-8"))
    if metadata["chain_head"] != expected_previous:
        errors.append("metadata chain_head mismatch")
    report = {
        "schema_version": "1.0.0",
        "work_unit": "P29-KO-U03",
        "record_count": len(records),
        "csv_row_count": len(rows),
        "latest_id": records[-1]["difficulty_id"] if records else None,
        "chain_head": expected_previous,
        "jsonl_sha256": sha(HERE / "DIFFICULTY_LEDGER.jsonl"),
        "schema_sha256": sha(HERE / "DIFFICULTY_LEDGER.schema.json"),
        "validator_sha256": sha(Path(__file__)),
        "errors": errors,
        "external_human_review": "absent_do_not_claim"
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(report, ensure_ascii=False))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
