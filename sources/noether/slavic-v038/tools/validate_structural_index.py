#!/usr/bin/env python3
"""Validate the v038 structural JSONL against its schema and invariants."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from datetime import datetime
from pathlib import Path

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "release" / "evidence"
SCHEMA = EVIDENCE / "structural_index_schema.json"
INDEX = EVIDENCE / "structural_index.jsonl"
OUTPUT = EVIDENCE / "structural_index_validation.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def main() -> int:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    records = [json.loads(line) for line in INDEX.read_text(encoding="utf-8").splitlines() if line.strip()]
    errors = []
    seen = set()
    record_ids = {record.get("structural_id") for record in records}
    for line_number, record in enumerate(records, 1):
        if record.get("structural_id") in seen:
            errors.append(f"line {line_number}: duplicate structural_id {record.get('structural_id')}")
        seen.add(record.get("structural_id"))
        for error in validator.iter_errors(record):
            errors.append(f"line {line_number}: {'/'.join(str(item) for item in error.path)}: {error.message}")
        parent = record.get("parent_id")
        if parent is not None and parent not in record_ids:
            errors.append(f"line {line_number}: missing parent_id {parent}")
        cursor = record.get("continuation_cursor")
        if cursor is not None and cursor not in record_ids:
            errors.append(f"line {line_number}: missing continuation_cursor {cursor}")
        locator = record.get("target_locator", {})
        if locator.get("start_line", 0) > locator.get("end_line", -1):
            errors.append(f"line {line_number}: inverted target locator")

    work_units = Counter(
        record["language"] for record in records if record.get("structure_type") == "work_unit"
    )
    for language in ("ru-Cyrl", "uk-Cyrl", "isv-Latn", "isv-Cyrl"):
        if work_units[language] != 36:
            errors.append(
                f"{language}: expected 36 work_unit records "
                f"(inherited base, touched P06 locus, and 34 post-P43 units), observed {work_units[language]}"
            )

    result = {
        "schema": "noether-slavic-v038-structural-index-validation/1.0",
        "generated_at": datetime.now().astimezone().isoformat(),
        "pass": not errors,
        "record_count": len(records),
        "work_unit_counts": dict(work_units),
        "errors": errors,
        "inputs": {
            "schema": {"path": SCHEMA.resolve().as_posix(), "sha256": sha256(SCHEMA)},
            "index": {"path": INDEX.resolve().as_posix(), "sha256": sha256(INDEX)},
        },
    }
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({**result, "output_sha256": sha256(OUTPUT)}, ensure_ascii=False))
    return 0 if result["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
