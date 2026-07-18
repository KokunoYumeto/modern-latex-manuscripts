from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
LEDGER = HERE / "DIFFICULTY_LEDGER.jsonl"
CSV_PROJECTION = HERE / "DIFFICULTY_LEDGER.csv"
METADATA = HERE / "DIFFICULTY_LEDGER_METADATA.json"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def load_jsonl(path: Path) -> list[dict]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


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
    if not LEDGER.is_file():
        raise SystemExit(f"missing canonical ledger: {LEDGER}")
    records = load_jsonl(LEDGER)
    rows = [project(record) for record in records]
    if not rows:
        raise SystemExit("canonical ledger is empty")

    with CSV_PROJECTION.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    states = Counter(record["resolution_state"] for record in records)
    metadata = {
        "schema_version": "1.0.0",
        "ledger_id": "CJK-KO-P29-U01-DIFFICULTY-LEDGER-001",
        "work_id": "noether.paper29.ko.u01",
        "append_only": True,
        "append_rule": "Append one new JSON object line with a new issue ID, next integer sequence, previous head in previous_record_sha256, and a recomputed record_sha256. Corrections cite supersedes. Existing lines are immutable.",
        "record_hash_algorithm": "SHA-256 over UTF-8 canonical JSON with sort_keys=true, separators=(',', ':'), ensure_ascii=false, excluding record_sha256",
        "record_count": len(records),
        "ordered_issue_ids": [record["issue_id"] for record in records],
        "first_issue_id": records[0]["issue_id"],
        "latest_issue_id": records[-1]["issue_id"],
        "chain_head_sha256": records[-1]["record_sha256"],
        "canonical_jsonl_sha256": digest(LEDGER.read_bytes()),
        "resolution_state_counts": dict(states),
        "continuation_cursor": "P29 U02 begins at exact full-source line 25 after sealed-authority rehash; held terminology and rights items remain open.",
    }
    METADATA.write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(
        f"projected={len(records)} states={dict(states)} "
        f"head={records[-1]['record_sha256']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
