#!/usr/bin/env python3
"""Project the append-only U03 difficulty JSONL into CSV and metadata."""

from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
LEDGER = HERE / "DIFFICULTY_LEDGER.jsonl"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


records = [json.loads(line) for line in LEDGER.read_text(encoding="utf-8").splitlines() if line.strip()]
fields = [
    "difficulty_id", "recorded_at", "time_precision", "source_locator", "target_locator", "symptom",
    "state", "resolution_or_hold", "residual_risk", "transferable_lesson", "revisit_condition",
    "previous_hash", "record_hash"
]
csv_path = HERE / "DIFFICULTY_LEDGER.csv"
with csv_path.open("w", encoding="utf-8", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=fields)
    writer.writeheader()
    for record in records:
        writer.writerow({field: record[field] for field in fields})

metadata = {
    "schema_version": "1.0.0",
    "ledger_id": "CJK-KO-P29-U03-DIFFICULTY-LEDGER-001",
    "append_only": True,
    "record_count": len(records),
    "state_counts": dict(sorted(Counter(record["state"] for record in records).items())),
    "latest_id": records[-1]["difficulty_id"],
    "chain_head": records[-1]["record_hash"],
    "jsonl_sha256": sha(LEDGER),
    "csv_sha256": sha(csv_path),
    "continuation_cursor": "Append a new chained record; never edit or delete this prefix."
}
(HERE / "DIFFICULTY_LEDGER_METADATA.json").write_text(
    json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n"
)
print(json.dumps(metadata, ensure_ascii=False))
