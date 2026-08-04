from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
LEDGER = HERE / "DIFFICULTY_LEDGER.jsonl"
CSV_PROJECTION = HERE / "DIFFICULTY_LEDGER.csv"
REPORT = HERE / "DIFFICULTY_LEDGER_VALIDATION_REPORT.json"
STRUCTURAL_INDEX = HERE.parent / "structural_index" / "PRODUCER_STRUCTURAL_INDEX.jsonl"

REQUIRED = {
    "schema_version",
    "issue_id",
    "recorded_at",
    "occurrence_time",
    "work_unit",
    "structural_ids",
    "source_locator",
    "target_locator",
    "difficulty_class",
    "symptom",
    "severity",
    "discovery_channel",
    "cause",
    "attempted_approaches",
    "resolution_state",
    "resolution_or_workaround",
    "evidence_artifacts",
    "residual_risk",
    "recurrence_cues",
    "transferable_lesson",
    "future_check",
    "related_decision_ids",
    "changed_artifacts",
    "supersedes",
    "supersession_state",
    "continuation_or_revisit",
}


def load_jsonl(path: Path) -> list[dict]:
    records = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
        if not line.strip():
            continue
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path.name}:{line_no}: {exc}") from exc
    return records


def csv_safe(value: object) -> str:
    if value is None:
        return ""
    text = str(value)
    return "'" + text if text.startswith(("=", "+", "-", "@")) else text


def main() -> int:
    errors: list[str] = []
    try:
        records = load_jsonl(LEDGER)
        structural = load_jsonl(STRUCTURAL_INDEX)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 1
    structural_ids = {record["structural_id"] for record in structural}
    issue_ids = [record.get("issue_id") for record in records]
    issue_set = set(issue_ids)
    if len(issue_ids) != len(issue_set):
        errors.append("duplicate issue IDs")
    for record in records:
        issue_id = record.get("issue_id", "<missing>")
        if set(record) != REQUIRED:
            errors.append(
                f"{issue_id}: fields missing={sorted(REQUIRED - set(record))} extra={sorted(set(record) - REQUIRED)}"
            )
            continue
        unresolved = [sid for sid in record["structural_ids"] if sid not in structural_ids]
        if unresolved:
            errors.append(f"{issue_id}: unresolved structural IDs {unresolved}")
        for prior in record["supersedes"]:
            if prior not in issue_set:
                errors.append(f"{issue_id}: unresolved supersedes ID {prior}")
        if not record["attempted_approaches"] or not record["evidence_artifacts"]:
            errors.append(f"{issue_id}: attempts and evidence must be nonempty")
        if not record["related_decision_ids"] or not record["recurrence_cues"]:
            errors.append(f"{issue_id}: decision IDs and recurrence cues are required")
        if record["resolution_state"] in {"held", "unresolved"}:
            continuation = record["continuation_or_revisit"].lower()
            if "revisit" not in continuation and "retry" not in continuation:
                errors.append(f"{issue_id}: held item lacks explicit revisit or retry condition")
    fields = [
        "issue_id",
        "recorded_at",
        "work_unit",
        "structural_ids",
        "difficulty_class",
        "symptom",
        "severity",
        "resolution_state",
        "residual_risk",
        "related_decision_ids",
        "continuation_or_revisit",
        "supersession_state",
    ]
    with CSV_PROJECTION.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for record in records:
            row = {
                "issue_id": record["issue_id"],
                "recorded_at": record["recorded_at"],
                "work_unit": record["work_unit"],
                "structural_ids": "|".join(record["structural_ids"]),
                "difficulty_class": record["difficulty_class"],
                "symptom": record["symptom"],
                "severity": record["severity"],
                "resolution_state": record["resolution_state"],
                "residual_risk": record["residual_risk"],
                "related_decision_ids": "|".join(record["related_decision_ids"]),
                "continuation_or_revisit": record["continuation_or_revisit"],
                "supersession_state": record["supersession_state"],
            }
            writer.writerow({key: csv_safe(value) for key, value in row.items()})
    with CSV_PROJECTION.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if [row["issue_id"] for row in rows] != issue_ids:
        errors.append("CSV projection ID/order mismatch")
    states = Counter(record["resolution_state"] for record in records)
    report = {
        "schema_version": "1.0.0",
        "record_count": len(records),
        "state_counts": dict(sorted(states.items())),
        "latest_issue_id": records[-1]["issue_id"] if records else None,
        "errors": errors,
        "status": "pass" if not errors else "fail",
        "append_only_note": "resolved, rejected, failed, and held paths remain in the JSONL authority",
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
