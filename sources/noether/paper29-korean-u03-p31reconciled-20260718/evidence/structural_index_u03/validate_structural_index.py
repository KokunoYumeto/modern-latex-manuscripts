#!/usr/bin/env python3
"""Validate U03 structural schema, hierarchy, relations, projection, and current hashes."""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

import jsonschema


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
REPORT = HERE / "STRUCTURAL_INDEX_VALIDATION_REPORT.json"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def main() -> int:
    errors: list[str] = []
    schema = json.loads((HERE / "STRUCTURAL_INDEX.schema.json").read_text(encoding="utf-8"))
    records = [
        json.loads(line)
        for line in (HERE / "STRUCTURAL_INDEX.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    rows = list(csv.DictReader((HERE / "STRUCTURAL_INDEX.csv").open(encoding="utf-8", newline="")))
    ids = [item["structural_id"] for item in records]
    if len(ids) != len(set(ids)):
        errors.append("duplicate structural_id")
    if len(rows) != len(records):
        errors.append(f"CSV rows {len(rows)} != JSONL records {len(records)}")
    for index, item in enumerate(records, start=1):
        try:
            jsonschema.validate(item, schema)
        except jsonschema.ValidationError as exc:
            errors.append(f"{item.get('structural_id', index)} schema: {exc.message}")
        if item["order"] != index:
            errors.append(f"{item['structural_id']}: order {item['order']} != {index}")
        parent = item["parent_id"]
        if parent is not None and parent not in ids:
            errors.append(f"{item['structural_id']}: missing parent {parent}")
        for relation in item["relations"]:
            target = relation["target_id"]
            if target.startswith("NOE-P29-KO-U03-") and target not in ids:
                errors.append(f"{item['structural_id']}: unresolved relation {target}")
    metadata = json.loads((HERE / "STRUCTURAL_INDEX_METADATA.json").read_text(encoding="utf-8"))
    source = ROOT / "source" / "Noether_Paper29_German_P31_U03_FinitenessCriterionProofSetup_exact_lf.tex"
    target = ROOT / "ko" / "Noether_Paper29_Korean_U03_v001.tex"
    if metadata["record_count"] != len(records):
        errors.append("metadata record_count mismatch")
    if metadata["source_sha256"] != sha(source):
        errors.append("metadata source hash mismatch")
    if metadata["target_sha256"] != sha(target):
        errors.append("metadata target hash mismatch")
    report = {
        "schema_version": "1.0.0",
        "work_unit": "P29-KO-U03",
        "record_count": len(records),
        "csv_row_count": len(rows),
        "latest_id": records[-1]["structural_id"] if records else None,
        "jsonl_sha256": sha(HERE / "STRUCTURAL_INDEX.jsonl"),
        "schema_sha256": sha(HERE / "STRUCTURAL_INDEX.schema.json"),
        "validator_sha256": sha(Path(__file__)),
        "errors": errors,
        "external_human_review": "absent_do_not_claim"
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(report, ensure_ascii=False))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
