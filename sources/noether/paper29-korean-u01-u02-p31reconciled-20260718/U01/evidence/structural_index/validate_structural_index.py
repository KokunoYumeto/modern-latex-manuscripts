from __future__ import annotations

import csv
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

from jsonschema import Draft202012Validator


HERE = Path(__file__).resolve().parent
TRANCHE = HERE.parents[1]
INDEX = HERE / "STRUCTURAL_INDEX.jsonl"
CSV_PROJECTION = HERE / "STRUCTURAL_INDEX.csv"
SCHEMA = HERE / "STRUCTURAL_INDEX.schema.json"
METADATA = HERE / "STRUCTURAL_INDEX_METADATA.json"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def load_jsonl(path: Path) -> tuple[list[dict], list[str]]:
    records: list[dict] = []
    errors: list[str] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError as exc:
            errors.append(f"{path.name}:{line_number}: invalid JSON: {exc}")
    return records, errors


def extract_fragment(path: Path, locator: dict) -> str:
    content = path.read_text(encoding="utf-8-sig").splitlines()
    line_start = locator["line_start"]
    line_end = locator["line_end"]
    if not 1 <= line_start <= line_end <= len(content):
        raise ValueError(f"invalid line range {line_start}-{line_end} for {path}")
    char_start = locator["char_start"]
    char_end = locator["char_end"]
    if char_start is None and char_end is None:
        return "\n".join(content[line_start - 1:line_end])
    if line_start != line_end or char_start is None or char_end is None:
        raise ValueError("character ranges require one line and two non-null endpoints")
    selected = content[line_start - 1]
    if not 1 <= char_start <= char_end <= len(selected):
        raise ValueError(
            f"invalid character range {char_start}-{char_end} for {path}:{line_start}"
        )
    return selected[char_start - 1:char_end]


def project(record: dict) -> dict[str, str]:
    source = record["source"]
    target = record["target"]
    return {
        "structural_id": record["structural_id"],
        "unit_type": record["unit_type"],
        "parent_id": record["parent_id"] or "",
        "order_index": str(record["order_index"]),
        "source_path": source["artifact_path"],
        "source_line_start": str(source["locator"]["line_start"]),
        "source_line_end": str(source["locator"]["line_end"]),
        "source_char_start": str(source["locator"]["char_start"] or ""),
        "source_char_end": str(source["locator"]["char_end"] or ""),
        "source_printed_page": source["locator"]["printed_page"] or "",
        "source_fragment_sha256": source["fragment_sha256"],
        "target_path": target["artifact_path"],
        "target_line_start": str(target["locator"]["line_start"]),
        "target_line_end": str(target["locator"]["line_end"]),
        "target_char_start": str(target["locator"]["char_start"] or ""),
        "target_char_end": str(target["locator"]["char_end"] or ""),
        "target_printed_page": target["locator"]["printed_page"] or "",
        "target_fragment_sha256": target["fragment_sha256"],
        "cross_references": ";".join(record["relations"]["cross_references"]),
        "dependencies": ";".join(record["relations"]["dependencies"]),
        "completion_state": record["completion_state"],
        "review_state": record["review_state"],
        "publication_state": record["publication_state"],
        "boundary_confidence": record["boundary_confidence"],
        "continuation_cursor": record["continuation_cursor"],
    }


def main() -> int:
    errors: list[str] = []
    for required_file in (INDEX, CSV_PROJECTION, SCHEMA, METADATA):
        if not required_file.is_file():
            errors.append(f"missing required file: {required_file}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    records, parse_errors = load_jsonl(INDEX)
    errors.extend(parse_errors)
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    metadata = json.loads(METADATA.read_text(encoding="utf-8"))
    schema_validator = Draft202012Validator(schema)

    for line_number, record in enumerate(records, 1):
        for problem in schema_validator.iter_errors(record):
            location = "/".join(str(part) for part in problem.absolute_path) or "<record>"
            errors.append(
                f"JSONL line {line_number} {record.get('structural_id', '<missing>')} schema {location}: {problem.message}"
            )

    ids = [record.get("structural_id") for record in records]
    id_set = set(ids)
    if len(ids) != len(id_set):
        errors.append("duplicate structural IDs")
    if ids != metadata.get("expected_structural_ids"):
        errors.append("JSONL ID/order differs from metadata expected_structural_ids")

    roots = [record for record in records if record.get("parent_id") is None]
    if len(roots) != 1 or (roots and roots[0].get("unit_type") != "work"):
        errors.append(f"expected exactly one work root; found {len(roots)}")

    sibling_keys: set[tuple[str | None, int]] = set()
    for record in records:
        sid = record.get("structural_id", "<missing>")
        if not isinstance(record, dict) or "source" not in record or "target" not in record:
            continue
        parent = record["parent_id"]
        if parent is not None and parent not in id_set:
            errors.append(f"{sid}: unresolved parent {parent}")
        sibling_key = (parent, record["order_index"])
        if sibling_key in sibling_keys:
            errors.append(f"{sid}: duplicate sibling order {sibling_key}")
        sibling_keys.add(sibling_key)
        for relation_name in ("cross_references", "dependencies"):
            for target_id in record["relations"][relation_name]:
                if target_id not in id_set:
                    errors.append(f"{sid}: unresolved {relation_name} target {target_id}")
                if target_id == sid:
                    errors.append(f"{sid}: self-reference in {relation_name}")

        for side_name in ("source", "target"):
            side = record[side_name]
            artifact = TRANCHE / side["artifact_path"]
            if not artifact.is_file():
                errors.append(f"{sid}/{side_name}: missing artifact {artifact}")
                continue
            actual_artifact_hash = digest(artifact.read_bytes())
            if actual_artifact_hash != side["artifact_sha256"]:
                errors.append(
                    f"{sid}/{side_name}: artifact hash mismatch {actual_artifact_hash} != {side['artifact_sha256']}"
                )
            try:
                fragment = extract_fragment(artifact, side["locator"])
            except ValueError as exc:
                errors.append(f"{sid}/{side_name}: {exc}")
                continue
            if not fragment.strip():
                errors.append(f"{sid}/{side_name}: selected fragment is empty")
            actual_fragment_hash = digest(fragment.encode("utf-8"))
            if actual_fragment_hash != side["fragment_sha256"]:
                errors.append(
                    f"{sid}/{side_name}: fragment hash mismatch {actual_fragment_hash} != {side['fragment_sha256']}"
                )
            if record["unit_type"] == "note":
                if not fragment.startswith(r"\footnote{") or not fragment.endswith("}"):
                    errors.append(f"{sid}/{side_name}: note locator is not an exact balanced footnote command")

    # Parent links must terminate at the unique root; this also detects cycles.
    by_id = {record["structural_id"]: record for record in records if "structural_id" in record}
    for sid in by_id:
        seen: set[str] = set()
        cursor: str | None = sid
        while cursor is not None and cursor in by_id:
            if cursor in seen:
                errors.append(f"{sid}: parent cycle through {cursor}")
                break
            seen.add(cursor)
            cursor = by_id[cursor]["parent_id"]

    counts = Counter(record.get("unit_type") for record in records)
    if len(records) != metadata.get("expected_record_count"):
        errors.append(
            f"record count {len(records)} != metadata {metadata.get('expected_record_count')}"
        )
    if dict(counts) != metadata.get("expected_type_counts"):
        errors.append(
            f"type counts {dict(counts)} != metadata {metadata.get('expected_type_counts')}"
        )

    authority = metadata.get("authority", {})
    for key in ("full_p29_slice_path", "u01_source_path", "target_tex_path"):
        relative = authority.get(key)
        if not relative or not (TRANCHE / relative).is_file():
            errors.append(f"metadata authority path missing or invalid: {key}={relative}")
    hash_pairs = (
        ("full_p29_slice_path", "full_p29_slice_sha256"),
        ("u01_source_path", "u01_source_sha256"),
        ("target_tex_path", "target_tex_sha256"),
    )
    for path_key, hash_key in hash_pairs:
        if authority.get(path_key) and (TRANCHE / authority[path_key]).is_file():
            actual = digest((TRANCHE / authority[path_key]).read_bytes())
            if actual != authority.get(hash_key):
                errors.append(f"metadata {hash_key} mismatch: {actual} != {authority.get(hash_key)}")
    sealed_path = Path(authority.get("sealed_cumulative_path", ""))
    if not sealed_path.is_file():
        errors.append(f"sealed cumulative authority path missing: {sealed_path}")
    elif digest(sealed_path.read_bytes()) != authority.get("sealed_cumulative_sha256"):
        errors.append("sealed cumulative authority hash no longer matches metadata")

    full_path = TRANCHE / authority.get("full_p29_slice_path", "")
    u01_path = TRANCHE / authority.get("u01_source_path", "")
    if full_path.is_file() and u01_path.is_file():
        full_lines = full_path.read_text(encoding="utf-8-sig").splitlines()
        u01_lines = u01_path.read_text(encoding="utf-8-sig").splitlines()
        if full_lines[:24] != u01_lines or len(u01_lines) != 24:
            errors.append("U01 is not the exact normalized first 24 lines of the full P29 slice")
        if len(full_lines) < 25 or not full_lines[24].startswith(
            r"\subsection*{§ 1. Das Endlichkeitskriterium}"
        ):
            errors.append("continuation cursor is not exact full-P29 line 25")

    with CSV_PROJECTION.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        csv_rows = list(reader)
        csv_header = reader.fieldnames
    expected_rows = [project(record) for record in records]
    expected_header = list(expected_rows[0]) if expected_rows else []
    if csv_header != expected_header:
        errors.append(f"CSV header mismatch: {csv_header} != {expected_header}")
    if len(csv_rows) != len(expected_rows):
        errors.append(f"CSV row count {len(csv_rows)} != JSONL record count {len(expected_rows)}")
    else:
        for row_number, (actual, expected) in enumerate(zip(csv_rows, expected_rows), 2):
            if actual != expected:
                mismatches = [key for key in expected if actual.get(key) != expected[key]]
                errors.append(f"CSV row {row_number} projection mismatch fields={mismatches}")

    print(
        "records={} types={} csv_rows={} schema_errors={} total_errors={}".format(
            len(records),
            dict(counts),
            len(csv_rows),
            sum(" schema " in error for error in errors),
            len(errors),
        )
    )
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
