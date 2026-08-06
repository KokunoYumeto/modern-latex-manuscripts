#!/usr/bin/env python3
"""Validate the v038 visual-evidence JSONL and indexed file hashes."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime
from pathlib import Path

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "release" / "evidence"
SCHEMA = EVIDENCE / "visual_evidence_schema.json"
INDEX = EVIDENCE / "visual_evidence_index.jsonl"
OUTPUT = EVIDENCE / "visual_evidence_validation.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def main() -> int:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    records = [json.loads(line) for line in INDEX.read_text(encoding="utf-8").splitlines() if line.strip()]
    errors = []
    seen = set()
    ids = {record.get("visual_id") for record in records}
    for line_number, record in enumerate(records, 1):
        visual_id = record.get("visual_id")
        if visual_id in seen:
            errors.append(f"line {line_number}: duplicate visual_id {visual_id}")
        seen.add(visual_id)
        for error in validator.iter_errors(record):
            errors.append(f"line {line_number}: {'/'.join(str(item) for item in error.path)}: {error.message}")
        image = record.get("image", {})
        image_path = Path(image.get("path", ""))
        if not image_path.exists():
            errors.append(f"line {line_number}: missing image {image_path}")
        elif sha256(image_path) != image.get("sha256"):
            errors.append(f"line {line_number}: image hash mismatch {image_path}")
        cursor = record.get("continuation_cursor")
        if cursor is not None and cursor not in ids:
            errors.append(f"line {line_number}: missing cursor {cursor}")
    result = {
        "schema": "noether-slavic-v038-visual-evidence-validation/1.0",
        "generated_at": datetime.now().astimezone().isoformat(),
        "pass": not errors,
        "record_count": len(records),
        "reviewed_pass_count": sum(record.get("qa_state") == "visually_reopened_pass" for record in records),
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
