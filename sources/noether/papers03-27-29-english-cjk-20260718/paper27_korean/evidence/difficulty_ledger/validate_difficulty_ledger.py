from __future__ import annotations

import csv
import json
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
LEDGER = HERE / "DIFFICULTY_LEDGER.jsonl"
CSV_PROJECTION = HERE / "DIFFICULTY_LEDGER.csv"
STRUCTURAL_INDEX = HERE.parent / "structural_index" / "STRUCTURAL_INDEX.jsonl"

REQUIRED = {
    "schema_version", "issue_id", "recorded_at", "occurrence_time", "work_unit",
    "structural_ids", "source_locator", "target_locator", "difficulty_class", "symptom",
    "severity", "discovery_channel", "cause", "attempted_approaches", "resolution_state",
    "resolution_or_workaround", "evidence_artifacts", "residual_risk", "recurrence_cues",
    "transferable_lesson", "future_check", "related_decision_ids", "changed_artifacts",
    "supersedes", "supersession_state", "continuation_or_revisit",
}


def load_jsonl(path: Path) -> list[dict]:
    rows = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path.name}:{line_no}: {exc}") from exc
    return rows


def main() -> int:
    errors: list[str] = []
    try:
        records = load_jsonl(LEDGER)
        structural = load_jsonl(STRUCTURAL_INDEX)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 1

    structural_ids = {r["structural_id"] for r in structural}
    issue_ids = [r.get("issue_id") for r in records]
    issue_set = set(issue_ids)
    if len(issue_ids) != len(issue_set):
        errors.append("duplicate issue IDs")

    for record in records:
        issue_id = record.get("issue_id", "<missing>")
        missing = REQUIRED - record.keys()
        extra = record.keys() - REQUIRED
        if missing or extra:
            errors.append(f"{issue_id}: fields missing={sorted(missing)} extra={sorted(extra)}")
            continue
        if not record["attempted_approaches"] or not record["evidence_artifacts"]:
            errors.append(f"{issue_id}: attempts/evidence must be nonempty")
        for sid in record["structural_ids"]:
            if sid not in structural_ids:
                errors.append(f"{issue_id}: unresolved structural ID {sid}")
        for prior in record["supersedes"]:
            if prior not in issue_set:
                errors.append(f"{issue_id}: unresolved supersedes ID {prior}")
        if not record["related_decision_ids"] or not record["recurrence_cues"]:
            errors.append(f"{issue_id}: decision IDs and recurrence cues are required")
        if record["resolution_state"] in {"held", "unresolved"} and "retry" not in record["continuation_or_revisit"].lower() and "revisit" not in record["continuation_or_revisit"].lower():
            errors.append(f"{issue_id}: held/unresolved item lacks explicit retry or revisit condition")

    with CSV_PROJECTION.open(encoding="utf-8-sig", newline="") as handle:
        csv_rows = list(csv.DictReader(handle))
    if [r["issue_id"] for r in csv_rows] != issue_ids:
        errors.append("CSV projection ID/order mismatch")

    states = {}
    for record in records:
        states[record["resolution_state"]] = states.get(record["resolution_state"], 0) + 1
    print(f"issues={len(records)} states={states} csv_rows={len(csv_rows)} errors={len(errors)}")
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
