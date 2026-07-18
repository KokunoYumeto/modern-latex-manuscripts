from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
TRANCHE = HERE.parents[1]
INDEX = HERE / "STRUCTURAL_INDEX.jsonl"
CSV_PROJECTION = HERE / "STRUCTURAL_INDEX.csv"
METADATA = HERE / "STRUCTURAL_INDEX_METADATA.json"

REQUIRED = {
    "schema_version", "structural_id", "work_id", "unit_type", "parent_id",
    "order_index", "source", "target", "relations", "completion_state",
    "review_state", "publication_state", "boundary_confidence", "boundary_note",
    "continuation_cursor", "supersedes",
}
SIDE_REQUIRED = {"artifact_path", "artifact_sha256", "authority_id", "language", "locator", "fragment_sha256"}
LOCATOR_REQUIRED = {"line_start", "line_end", "char_start", "char_end", "printed_page", "pdf_page"}
SHA = re.compile(r"^[0-9A-F]{64}$")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def extract_fragment(path: Path, locator: dict) -> str:
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    a, b = locator["line_start"], locator["line_end"]
    if not (1 <= a <= b <= len(lines)):
        raise ValueError(f"invalid line range {a}-{b} for {path}")
    char_start, char_end = locator["char_start"], locator["char_end"]
    if char_start is None and char_end is None:
        return "\n".join(lines[a - 1:b])
    if a != b or char_start is None or char_end is None:
        raise ValueError("character ranges require one line and two non-null endpoints")
    line = lines[a - 1]
    if not (1 <= char_start <= char_end <= len(line)):
        raise ValueError(f"invalid character range {char_start}-{char_end} for {path}:{a}")
    return line[char_start - 1:char_end]


def main() -> int:
    errors: list[str] = []
    records = []
    for line_no, line in enumerate(INDEX.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append(f"JSONL line {line_no}: {exc}")
            continue
        records.append(record)
        missing = REQUIRED - record.keys()
        extra = record.keys() - REQUIRED
        if missing or extra:
            errors.append(f"{record.get('structural_id', line_no)} fields missing={sorted(missing)} extra={sorted(extra)}")

    ids = [r.get("structural_id") for r in records]
    id_set = set(ids)
    if len(ids) != len(id_set):
        errors.append("duplicate structural IDs")

    for record in records:
        sid = record["structural_id"]
        parent = record["parent_id"]
        if parent is not None and parent not in id_set:
            errors.append(f"{sid}: unresolved parent {parent}")
        for rel_name in ("cross_references", "dependencies"):
            for target in record["relations"][rel_name]:
                if target not in id_set:
                    errors.append(f"{sid}: unresolved {rel_name} target {target}")
        if not record["boundary_note"].strip() or not record["continuation_cursor"].strip():
            errors.append(f"{sid}: empty boundary note or continuation cursor")
        for side_name in ("source", "target"):
            side = record[side_name]
            if set(side) != SIDE_REQUIRED:
                errors.append(f"{sid}/{side_name}: invalid side fields")
                continue
            if set(side["locator"]) != LOCATOR_REQUIRED:
                errors.append(f"{sid}/{side_name}: invalid locator fields")
                continue
            path = TRANCHE / side["artifact_path"]
            if not path.is_file():
                errors.append(f"{sid}/{side_name}: missing artifact {path}")
                continue
            if not SHA.fullmatch(side["artifact_sha256"]) or digest(path.read_bytes()) != side["artifact_sha256"]:
                errors.append(f"{sid}/{side_name}: artifact hash mismatch")
            try:
                fragment = extract_fragment(path, side["locator"])
            except ValueError as exc:
                errors.append(f"{sid}/{side_name}: {exc}")
                continue
            if not SHA.fullmatch(side["fragment_sha256"]) or digest(fragment.encode("utf-8")) != side["fragment_sha256"]:
                errors.append(f"{sid}/{side_name}: fragment hash mismatch")

    sibling_orders = Counter((r["parent_id"], r["order_index"]) for r in records)
    for key, count in sibling_orders.items():
        if count > 1:
            errors.append(f"duplicate sibling order {key}")

    metadata = json.loads(METADATA.read_text(encoding="utf-8"))
    if len(records) != metadata["expected_record_count"]:
        errors.append(f"record count {len(records)} != {metadata['expected_record_count']}")
    counts = Counter(r["unit_type"] for r in records)
    if dict(counts) != metadata["expected_type_counts"]:
        errors.append(f"type counts {dict(counts)} != {metadata['expected_type_counts']}")

    with CSV_PROJECTION.open(encoding="utf-8-sig", newline="") as handle:
        csv_rows = list(csv.DictReader(handle))
    csv_ids = [r["structural_id"] for r in csv_rows]
    if csv_ids != ids:
        errors.append("CSV projection ID/order mismatch")

    print(f"records={len(records)} types={dict(counts)} csv_rows={len(csv_rows)} errors={len(errors)}")
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
