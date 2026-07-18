from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
LEDGER, CSV_PATH, METADATA = HERE / "DIFFICULTY_LEDGER.jsonl", HERE / "DIFFICULTY_LEDGER.csv", HERE / "DIFFICULTY_LEDGER_METADATA.json"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def project(r: dict) -> dict[str, str]:
    return {"ledger_sequence": str(r["ledger_sequence"]), "issue_id": r["issue_id"], "difficulty_class": r["difficulty_class"], "severity": r["severity"], "resolution_state": r["resolution_state"], "structural_ids": ";".join(r["structural_ids"]), "related_decision_ids": ";".join(r["related_decision_ids"]), "recorded_at": r["recorded_at"], "occurrence_time": r["occurrence_time"]["value"], "occurrence_precision": r["occurrence_time"]["precision"], "source_locator": r["source_locator"], "target_locator": r["target_locator"], "record_sha256": r["record_sha256"], "previous_record_sha256": r["previous_record_sha256"] or "", "supersedes": ";".join(r["supersedes"]), "continuation_or_revisit": r["continuation_or_revisit"]}


def main() -> int:
    records = [json.loads(line) for line in LEDGER.read_text(encoding="utf-8").splitlines() if line.strip()]
    if not records:
        raise SystemExit("empty ledger")
    rows = [project(r) for r in records]
    with CSV_PATH.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader(); writer.writerows(rows)
    states = Counter(r["resolution_state"] for r in records)
    metadata = {"schema_version": "1.0.0", "ledger_id": "CJK-KO-P29-U02-DIFFICULTY-LEDGER-001", "work_id": "noether.paper29.ko.u02", "append_only": True, "append_rule": "Append a new chained JSONL line with a new issue ID; corrections cite supersedes; existing lines remain immutable.", "record_hash_algorithm": "SHA-256 over UTF-8 canonical JSON sort_keys=true excluding record_sha256", "record_count": len(records), "ordered_issue_ids": [r["issue_id"] for r in records], "first_issue_id": records[0]["issue_id"], "latest_issue_id": records[-1]["issue_id"], "chain_head_sha256": records[-1]["record_sha256"], "canonical_jsonl_sha256": digest(LEDGER.read_bytes()), "resolution_state_counts": dict(states), "continuation_cursor": "U03 begins at exact full-P29 line 41 after authority rehash; historical terminology debt remains held."}
    METADATA.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"projected={len(records)} states={dict(states)} head={records[-1]['record_sha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
