from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
LEDGER = ROOT / "ROMANCE_DECISION_LEDGER_v1.jsonl"
RULE = ROOT / "ROMANCE_DECISION_LOGGING_RULE_v1.md"
REPORT = ROOT / "ROMANCE_DECISION_LEDGER_VALIDATION_v1.json"

REQUIRED = {
    "decision_id",
    "record_kind",
    "recorded_at",
    "decision_at",
    "decision_time_precision",
    "stage",
    "decision",
    "selected_option",
    "alternatives_considered",
    "evidence_used",
    "motivation",
    "uncertainty_and_adverse_evidence",
    "consequences",
    "review_status",
    "reflection",
    "revisit_when",
    "related_artifacts",
    "public_claim_boundary",
}
ALLOWED_KINDS = {"live", "backfill", "correction"}
ALLOWED_REVIEW = {
    "accepted_current",
    "in_production",
    "pending_validation",
    "held",
    "rejected",
    "superseded",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def nonempty(value: object) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, list):
        return bool(value) and all(nonempty(item) for item in value)
    return True


def main() -> None:
    checks: dict[str, bool] = {}
    errors: list[str] = []
    rows: list[dict[str, object]] = []

    checks["rule_exists_nonempty"] = RULE.is_file() and RULE.stat().st_size > 500
    checks["ledger_exists_nonempty"] = LEDGER.is_file() and LEDGER.stat().st_size > 500

    for line_number, raw in enumerate(LEDGER.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            row = json.loads(raw)
        except json.JSONDecodeError as exc:
            errors.append(f"line {line_number}: invalid JSON: {exc}")
            continue
        if not isinstance(row, dict):
            errors.append(f"line {line_number}: row is not an object")
            continue
        row["_line"] = line_number
        rows.append(row)

    ids = [str(row.get("decision_id", "")) for row in rows]
    checks["json_rows_present"] = len(rows) >= 16
    checks["unique_decision_ids"] = len(ids) == len(set(ids))
    checks["ordered_decision_ids"] = ids == [f"RDL-{index:04d}" for index in range(1, len(ids) + 1)]

    for row in rows:
        line = row.pop("_line")
        missing = sorted(REQUIRED - set(row))
        if missing:
            errors.append(f"line {line}: missing fields {missing}")
        empty = sorted(field for field in REQUIRED & set(row) if not nonempty(row[field]))
        if empty:
            errors.append(f"line {line}: empty fields {empty}")
        if row.get("record_kind") not in ALLOWED_KINDS:
            errors.append(f"line {line}: invalid record_kind {row.get('record_kind')!r}")
        if row.get("review_status") not in ALLOWED_REVIEW:
            errors.append(f"line {line}: invalid review_status {row.get('review_status')!r}")
        alternatives = row.get("alternatives_considered")
        evidence = row.get("evidence_used")
        artifacts = row.get("related_artifacts")
        if not isinstance(alternatives, list) or len(alternatives) < 2:
            errors.append(f"line {line}: at least two alternatives are required")
        if not isinstance(evidence, list) or len(evidence) < 2:
            errors.append(f"line {line}: at least two evidence statements are required")
        if not isinstance(artifacts, list) or not artifacts:
            errors.append(f"line {line}: related_artifacts must be a nonempty list")
        reflection = str(row.get("reflection", "")).lower()
        if not any(marker in reflection for marker in ("did not", "does not", "still", "cannot")):
            errors.append(f"line {line}: reflection lacks an explicit unresolved boundary")
        boundary = str(row.get("public_claim_boundary", "")).lower()
        if not any(marker in boundary for marker in ("not ", "never", "do not", "cannot")):
            errors.append(f"line {line}: public claim boundary is not explicit")

    checks["all_required_fields_valid"] = not errors
    checks["backfills_marked"] = all(
        row["decision_time_precision"] == "day"
        for row in rows
        if row["record_kind"] == "backfill"
    )
    checks["rule_requires_motivation_reflection"] = (
        "motivation/rationale" in RULE.read_text(encoding="utf-8")
        and "reflection" in RULE.read_text(encoding="utf-8")
        and "never silently rewritten or deleted" in RULE.read_text(encoding="utf-8")
    )

    status = "PASS" if all(checks.values()) else "FAIL"
    report = {
        "artifact": "ROMANCE_DECISION_LEDGER_VALIDATION_v1",
        "status": status,
        "decision_count": len(rows),
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "checks": checks,
        "errors": errors,
        "hashes": {
            "rule": sha256(RULE),
            "ledger": sha256(LEDGER),
            "validator": sha256(Path(__file__).resolve()),
        },
        "claim_boundary": "Decision-process integrity only; this report does not certify linguistic correctness, source completeness, human validation, or lane completion.",
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"{status} ROMANCE_DECISION_LEDGER decisions={len(rows)} "
        f"checks={report['checks_passed']}/{report['checks_total']} errors={len(errors)}"
    )
    if status != "PASS":
        for error in errors:
            print(error)
        raise SystemExit(1)


if __name__ == "__main__":
    main()

