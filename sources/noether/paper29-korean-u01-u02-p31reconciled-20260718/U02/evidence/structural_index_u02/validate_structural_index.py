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
INDEX, CSV_PATH, SCHEMA, METADATA = (HERE / "STRUCTURAL_INDEX.jsonl", HERE / "STRUCTURAL_INDEX.csv", HERE / "STRUCTURAL_INDEX.schema.json", HERE / "STRUCTURAL_INDEX_METADATA.json")
EXPECTED_SOURCE_SHA = "B7EF88537BCD90D0408B3D1942DA410410FE45E79DD457B2DF6DFA2D4929DCAC"
EXPECTED_TARGET_SHA = "B694D05E57B58E1B0373D976356E6B3B3F4883D7CC9398081DB12111877B6A7C"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def load_jsonl(path: Path) -> tuple[list[dict], list[str]]:
    rows, errors = [], []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            errors.append(f"{path.name}:{number}: {exc}")
    return rows, errors


def fragment(path: Path, loc: dict) -> str:
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    a, b = loc["line_start"], loc["line_end"]
    if not 1 <= a <= b <= len(lines):
        raise ValueError(f"invalid lines {a}-{b} for {path}")
    cs, ce = loc["char_start"], loc["char_end"]
    if cs is None and ce is None:
        return "\n".join(lines[a - 1:b])
    if a != b or cs is None or ce is None or not 1 <= cs <= ce <= len(lines[a - 1]):
        raise ValueError(f"invalid characters {cs}-{ce} for {path}:{a}")
    return lines[a - 1][cs - 1:ce]


def projection(r: dict) -> dict[str, str]:
    s, t = r["source"], r["target"]
    return {
        "structural_id": r["structural_id"], "unit_type": r["unit_type"], "parent_id": r["parent_id"] or "", "order_index": str(r["order_index"]),
        "source_path": s["artifact_path"], "source_line_start": str(s["locator"]["line_start"]), "source_line_end": str(s["locator"]["line_end"]), "source_char_start": str(s["locator"]["char_start"] or ""), "source_char_end": str(s["locator"]["char_end"] or ""), "source_printed_page": s["locator"]["printed_page"] or "", "source_fragment_sha256": s["fragment_sha256"],
        "target_path": t["artifact_path"], "target_line_start": str(t["locator"]["line_start"]), "target_line_end": str(t["locator"]["line_end"]), "target_char_start": str(t["locator"]["char_start"] or ""), "target_char_end": str(t["locator"]["char_end"] or ""), "target_printed_page": t["locator"]["printed_page"] or "", "target_fragment_sha256": t["fragment_sha256"],
        "cross_references": ";".join(r["relations"]["cross_references"]), "dependencies": ";".join(r["relations"]["dependencies"]), "completion_state": r["completion_state"], "review_state": r["review_state"], "publication_state": r["publication_state"], "boundary_confidence": r["boundary_confidence"], "continuation_cursor": r["continuation_cursor"],
    }


def main() -> int:
    errors: list[str] = []
    for path in (INDEX, CSV_PATH, SCHEMA, METADATA):
        if not path.is_file():
            errors.append(f"missing {path}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    records, parse_errors = load_jsonl(INDEX)
    errors.extend(parse_errors)
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    metadata = json.loads(METADATA.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    schema_errors = 0
    for number, record in enumerate(records, 1):
        for problem in validator.iter_errors(record):
            schema_errors += 1
            where = "/".join(str(x) for x in problem.absolute_path) or "<record>"
            errors.append(f"line {number} {record.get('structural_id')} schema {where}: {problem.message}")

    ids = [r.get("structural_id") for r in records]
    id_set = set(ids)
    if len(ids) != len(id_set):
        errors.append("duplicate structural IDs")
    if ids != metadata.get("expected_structural_ids"):
        errors.append("ID/order mismatch against metadata")
    roots = [r for r in records if r.get("parent_id") is None]
    if len(roots) != 1 or (roots and roots[0].get("unit_type") != "work"):
        errors.append(f"expected one work root; got {len(roots)}")

    sibling_keys: set[tuple[str | None, int]] = set()
    by_id = {r["structural_id"]: r for r in records if "structural_id" in r}
    for r in records:
        sid, parent = r["structural_id"], r["parent_id"]
        if parent is not None and parent not in id_set:
            errors.append(f"{sid}: unresolved parent {parent}")
        key = (parent, r["order_index"])
        if key in sibling_keys:
            errors.append(f"{sid}: duplicate sibling order {key}")
        sibling_keys.add(key)
        for rel in ("cross_references", "dependencies"):
            for target in r["relations"][rel]:
                if target not in id_set:
                    errors.append(f"{sid}: unresolved {rel} {target}")
                if target == sid:
                    errors.append(f"{sid}: self-reference in {rel}")
        for side_name in ("source", "target"):
            side = r[side_name]
            path = TRANCHE / side["artifact_path"]
            if not path.is_file():
                errors.append(f"{sid}/{side_name}: missing {path}")
                continue
            if digest(path.read_bytes()) != side["artifact_sha256"]:
                errors.append(f"{sid}/{side_name}: artifact hash mismatch")
            try:
                text = fragment(path, side["locator"])
            except ValueError as exc:
                errors.append(f"{sid}/{side_name}: {exc}")
                continue
            if not text.strip() or digest(text.encode("utf-8")) != side["fragment_sha256"]:
                errors.append(f"{sid}/{side_name}: empty or hash-mismatched fragment")
            if r["unit_type"] == "note" and (not text.startswith(r"\footnote{") or not text.endswith("}")):
                errors.append(f"{sid}/{side_name}: note is not an exact balanced footnote command")
            if r["unit_type"] == "display" and side_name == "target" and (not text.startswith(r"\[") or not text.endswith(r"\]")):
                errors.append(f"{sid}/target: display locator lacks exact display delimiters")

    for sid in by_id:
        seen: set[str] = set()
        cursor: str | None = sid
        while cursor is not None and cursor in by_id:
            if cursor in seen:
                errors.append(f"{sid}: parent cycle at {cursor}")
                break
            seen.add(cursor)
            cursor = by_id[cursor]["parent_id"]

    counts = Counter(r.get("unit_type") for r in records)
    if len(records) != metadata.get("expected_record_count"):
        errors.append("record count mismatch")
    if dict(counts) != metadata.get("expected_type_counts"):
        errors.append(f"type counts {dict(counts)} != {metadata.get('expected_type_counts')}")
    if counts.get("display") != 3:
        errors.append(f"expected exactly three target display records, got {counts.get('display', 0)}")

    authority = metadata.get("authority", {})
    for path_key, hash_key in (("full_p29_slice_path", "full_p29_slice_sha256"), ("u02_source_path", "u02_source_sha256"), ("target_tex_path", "target_tex_sha256")):
        path = TRANCHE / authority.get(path_key, "")
        if not path.is_file() or digest(path.read_bytes()) != authority.get(hash_key):
            errors.append(f"metadata authority mismatch for {path_key}")
    if authority.get("u02_source_sha256") != EXPECTED_SOURCE_SHA:
        errors.append("U02 source differs from assigned authority hash")
    if authority.get("target_tex_sha256") != EXPECTED_TARGET_SHA:
        errors.append("U02 target differs from assigned final hash")
    sealed = Path(authority.get("sealed_cumulative_path", ""))
    if not sealed.is_file() or digest(sealed.read_bytes()) != authority.get("sealed_cumulative_sha256"):
        errors.append("sealed P31 authority hash/path mismatch")

    full = (TRANCHE / authority["full_p29_slice_path"]).read_text(encoding="utf-8-sig").splitlines()
    u02 = (TRANCHE / authority["u02_source_path"]).read_text(encoding="utf-8-sig").splitlines()
    if len(u02) != 15 or full[24:39] != u02:
        errors.append("U02 normalized full-source lines 25-39 mismatch")
    if len(full) < 41 or full[39] != "" or not full[40].startswith(r"2. \srcspaced{Beweis des Endlichkeitskriteriums.}"):
        errors.append("exact full-source line-41 continuation mismatch")

    with CSV_PATH.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        header = reader.fieldnames
    expected = [projection(r) for r in records]
    if header != (list(expected[0]) if expected else []):
        errors.append("CSV header mismatch")
    if len(rows) != len(expected):
        errors.append("CSV row count mismatch")
    else:
        for number, (actual, wanted) in enumerate(zip(rows, expected), 2):
            if actual != wanted:
                errors.append(f"CSV row {number} mismatch: {[k for k in wanted if actual.get(k) != wanted[k]]}")

    print(f"records={len(records)} types={dict(counts)} csv_rows={len(rows)} schema_errors={schema_errors} total_errors={len(errors)}")
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
