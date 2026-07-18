from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker


HERE = Path(__file__).resolve().parent
TRANCHE = HERE.parents[1]
LEDGER = HERE / "DIFFICULTY_LEDGER.jsonl"
CSV_PROJECTION = HERE / "DIFFICULTY_LEDGER.csv"
SCHEMA = HERE / "DIFFICULTY_LEDGER.schema.json"
METADATA = HERE / "DIFFICULTY_LEDGER_METADATA.json"
STRUCTURAL_INDEX = HERE.parent / "structural_index" / "STRUCTURAL_INDEX.jsonl"
STRUCTURAL_METADATA = HERE.parent / "structural_index" / "STRUCTURAL_INDEX_METADATA.json"
FILE_HASH = re.compile(r"^SHA-256:([0-9A-F]{64})(?:;bytes=([0-9]+))?$")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def canonical_record_hash(record: dict) -> str:
    without_hash = {key: value for key, value in record.items() if key != "record_sha256"}
    encoded = json.dumps(
        without_hash, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return digest(encoded)


def load_jsonl(path: Path) -> tuple[list[dict], list[str]]:
    rows: list[dict] = []
    errors: list[str] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            errors.append(f"{path.name}:{line_number}: invalid JSON: {exc}")
    return rows, errors


def resolve_file(reference: str) -> Path:
    path = Path(reference)
    return path if path.is_absolute() else TRANCHE / path


def project(record: dict) -> dict[str, str]:
    return {
        "ledger_sequence": str(record["ledger_sequence"]),
        "issue_id": record["issue_id"],
        "difficulty_class": record["difficulty_class"],
        "severity": record["severity"],
        "resolution_state": record["resolution_state"],
        "structural_ids": ";".join(record["structural_ids"]),
        "related_decision_ids": ";".join(record["related_decision_ids"]),
        "recorded_at": record["recorded_at"],
        "occurrence_time": record["occurrence_time"]["value"],
        "occurrence_precision": record["occurrence_time"]["precision"],
        "source_locator": record["source_locator"],
        "target_locator": record["target_locator"],
        "record_sha256": record["record_sha256"],
        "previous_record_sha256": record["previous_record_sha256"] or "",
        "supersedes": ";".join(record["supersedes"]),
        "continuation_or_revisit": record["continuation_or_revisit"],
    }


def main() -> int:
    errors: list[str] = []
    for required in (
        LEDGER,
        CSV_PROJECTION,
        SCHEMA,
        METADATA,
        STRUCTURAL_INDEX,
        STRUCTURAL_METADATA,
    ):
        if not required.is_file():
            errors.append(f"missing required file: {required}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    records, parse_errors = load_jsonl(LEDGER)
    structural, structural_parse_errors = load_jsonl(STRUCTURAL_INDEX)
    errors.extend(parse_errors)
    errors.extend(structural_parse_errors)
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    metadata = json.loads(METADATA.read_text(encoding="utf-8"))
    structural_metadata = json.loads(STRUCTURAL_METADATA.read_text(encoding="utf-8"))
    schema_validator = Draft202012Validator(schema, format_checker=FormatChecker())
    schema_error_count = 0
    for line_number, record in enumerate(records, 1):
        for problem in schema_validator.iter_errors(record):
            schema_error_count += 1
            location = "/".join(str(part) for part in problem.absolute_path) or "<record>"
            errors.append(
                f"JSONL line {line_number} {record.get('issue_id', '<missing>')} schema {location}: {problem.message}"
            )

    issue_ids = [record.get("issue_id") for record in records]
    issue_set = set(issue_ids)
    if len(issue_ids) != len(issue_set):
        errors.append("duplicate issue IDs")
    if issue_ids != metadata.get("ordered_issue_ids"):
        errors.append("JSONL ID/order differs from metadata ordered_issue_ids")

    structural_ids = {record["structural_id"] for record in structural}
    previous_hash: str | None = None
    earlier_ids: set[str] = set()
    for expected_sequence, record in enumerate(records, 1):
        issue_id = record.get("issue_id", "<missing>")
        if record.get("ledger_sequence") != expected_sequence:
            errors.append(
                f"{issue_id}: sequence {record.get('ledger_sequence')} != {expected_sequence}"
            )
        if record.get("previous_record_sha256") != previous_hash:
            errors.append(
                f"{issue_id}: previous hash {record.get('previous_record_sha256')} != {previous_hash}"
            )
        actual_record_hash = canonical_record_hash(record)
        if record.get("record_sha256") != actual_record_hash:
            errors.append(
                f"{issue_id}: record hash mismatch {actual_record_hash} != {record.get('record_sha256')}"
            )
        previous_hash = record.get("record_sha256")

        for structural_id in record.get("structural_ids", []):
            if structural_id not in structural_ids:
                errors.append(f"{issue_id}: unresolved structural ID {structural_id}")
        for superseded_id in record.get("supersedes", []):
            if superseded_id not in earlier_ids:
                errors.append(
                    f"{issue_id}: supersedes must reference an earlier issue, got {superseded_id}"
                )
        earlier_ids.add(issue_id)

        if record.get("resolution_state") in {"held", "unresolved"}:
            continuation = record.get("continuation_or_revisit", "").lower()
            if not any(word in continuation for word in ("revisit", "retry", "clearance")):
                errors.append(f"{issue_id}: held/unresolved item lacks an explicit revisit condition")
        if not record.get("related_decision_ids"):
            errors.append(f"{issue_id}: related_decision_ids is empty")

        for artifact in record.get("evidence_artifacts", []):
            kind = artifact.get("evidence_kind")
            reference = artifact.get("path_or_reference", "")
            hash_or_test = artifact.get("hash_or_test", "")
            if kind in {"current_file", "source_scan"}:
                match = FILE_HASH.fullmatch(hash_or_test)
                if not match:
                    errors.append(f"{issue_id}: malformed file hash evidence for {reference}")
                    continue
                path = resolve_file(reference)
                if not path.is_file():
                    errors.append(f"{issue_id}: missing evidence file {path}")
                    continue
                actual_hash = digest(path.read_bytes())
                if actual_hash != match.group(1):
                    errors.append(
                        f"{issue_id}: evidence file hash mismatch {reference}: {actual_hash} != {match.group(1)}"
                    )
                if match.group(2) is not None and path.stat().st_size != int(match.group(2)):
                    errors.append(
                        f"{issue_id}: evidence byte count mismatch {reference}: {path.stat().st_size} != {match.group(2)}"
                    )
            elif kind == "historical_hash":
                if not FILE_HASH.fullmatch(hash_or_test):
                    errors.append(f"{issue_id}: malformed historical hash for {reference}")
            elif kind == "external_url":
                if not reference.startswith(("https://", "http://")):
                    errors.append(f"{issue_id}: external_url is not HTTP(S): {reference}")

    states = Counter(record.get("resolution_state") for record in records)
    if metadata.get("append_only") is not True:
        errors.append("metadata append_only is not true")
    if metadata.get("record_count") != len(records):
        errors.append(f"metadata record_count {metadata.get('record_count')} != {len(records)}")
    if metadata.get("latest_issue_id") != (issue_ids[-1] if issue_ids else None):
        errors.append("metadata latest_issue_id mismatch")
    if metadata.get("chain_head_sha256") != previous_hash:
        errors.append("metadata chain head mismatch")
    if metadata.get("canonical_jsonl_sha256") != digest(LEDGER.read_bytes()):
        errors.append("metadata canonical JSONL hash mismatch")
    if metadata.get("resolution_state_counts") != dict(states):
        errors.append(
            f"metadata state counts {metadata.get('resolution_state_counts')} != {dict(states)}"
        )

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
                mismatch = [key for key in expected if actual.get(key) != expected[key]]
                errors.append(f"CSV row {row_number} projection mismatch fields={mismatch}")

    # Reproduce the source-prefix resolution in HARD-001.
    full_source = TRANCHE / "source/Noether_Paper29_German_P31_Sealed_exact_slice.tex"
    u01_source = TRANCHE / "source/Noether_Paper29_German_P31_U01_Introduction_exact_lf.tex"
    full_lines = full_source.read_text(encoding="utf-8-sig").splitlines()
    u01_lines = u01_source.read_text(encoding="utf-8-sig").splitlines()
    if len(u01_lines) != 24 or full_lines[:24] != u01_lines:
        errors.append("HARD-001 normalized first-24-line source-prefix check failed")
    if len(full_lines) < 25 or not full_lines[24].startswith(
        r"\subsection*{§ 1. Das Endlichkeitskriterium}"
    ):
        errors.append("HARD-001 line-25 continuation check failed")

    # Preserve all three superseded draft hashes after the in-place semantic repair.
    expected_rejected_hashes = {
        "242B3DF47606609F3E2962753782028F5325BD84646FD145AFA30CA2A899CCAD",
        "AA390A2FBB8F3C79650127C4C725C58A6F0C66E01439DEE2DE13F34142E47B5C",
        "7E0E5A0250BB9CC70EAFA79CDF22695254042D9CB20513B7226C6C1ED8B1919E",
    }
    hard_002 = next(
        (record for record in records if record.get("issue_id") == "CJK-KO-P29-HARD-002"),
        None,
    )
    recorded_rejected_hashes: set[str] = set()
    if hard_002:
        for artifact in hard_002.get("evidence_artifacts", []):
            if artifact.get("evidence_kind") == "historical_hash":
                match = FILE_HASH.fullmatch(artifact.get("hash_or_test", ""))
                if match:
                    recorded_rejected_hashes.add(match.group(1))
    if recorded_rejected_hashes != expected_rejected_hashes:
        errors.append(
            f"HARD-002 rejected hash set {recorded_rejected_hashes} != {expected_rejected_hashes}"
        )

    # Current target hash must agree across the structural metadata and filesystem.
    target_tex = TRANCHE / "ko/Noether_Paper29_Korean_U01_v001.tex"
    target_hash = digest(target_tex.read_bytes())
    if target_hash != structural_metadata.get("authority", {}).get("target_tex_sha256"):
        errors.append("current target hash differs from structural metadata")

    target_log = TRANCHE / "ko/Noether_Paper29_Korean_U01_v001.log"
    log_text = target_log.read_text(encoding="utf-8", errors="replace")
    for warning in (
        r"Underfull \hbox (badness 1603) in paragraph at lines 28--29",
        r"Underfull \hbox (badness 2050) in paragraph at lines 30--31",
    ):
        if warning not in log_text:
            errors.append(f"HARD-005 expected retained warning missing: {warning}")

    print(
        "issues={} states={} csv_rows={} chain_head={} schema_errors={} total_errors={}".format(
            len(records),
            dict(states),
            len(csv_rows),
            previous_hash,
            schema_error_count,
            len(errors),
        )
    )
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
