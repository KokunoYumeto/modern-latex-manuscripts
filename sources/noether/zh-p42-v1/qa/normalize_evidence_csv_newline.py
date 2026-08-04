#!/usr/bin/env python3
"""Remove one extra terminal blank record from the three Paper 42 CSVs."""

from pathlib import Path
import hashlib
import json


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "evidence"
EXPECTED = {
    "PRODUCER_TERMINOLOGY_LEDGER.csv": "DF06053174D7E1DD165F8A592C00B52E8D73E33463A149A05C865F66C1A6EC36",
    "ADVERSE_SENSE_LEDGER.csv": "2062DB2DD4BFE404B4CE5770982C4D820E62BCB4590853ABBA885CA7548093DE",
    "CJKV_CROSSWALK_P42_ZH.csv": "33A7A62430A13D63854E25EDDD5481A1358AB6CF6BB947324FD9A188A1B80D72",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


report = {}
for name, expected_hash in EXPECTED.items():
    path = EVIDENCE / name
    input_hash = sha(path)
    if input_hash != expected_hash:
        raise RuntimeError(f"{name} changed: expected {expected_hash}, found {input_hash}")
    text = path.read_text(encoding="utf-8")
    normalized = text.rstrip("\r\n") + "\n"
    path.write_text(normalized, encoding="utf-8", newline="\n")
    report[name] = {
        "input_sha256": input_hash,
        "output_sha256": sha(path),
        "operation": "terminal blank-record removal only",
    }

record = {
    "work_id": "NOETHER-P42",
    "claim_class": "mechanical_csv_transport_formatting",
    "files": report,
    "claim_limit": "No terminology, source, semantic, or review judgment performed.",
}
(ROOT / "qa/EVIDENCE_CSV_NEWLINE_RECORD.json").write_text(
    json.dumps(record, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(record, indent=2))
