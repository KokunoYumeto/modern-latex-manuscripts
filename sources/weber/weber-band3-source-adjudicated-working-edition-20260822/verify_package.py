#!/usr/bin/env python3
import csv
import hashlib
from pathlib import Path

root = Path(__file__).resolve().parent
rows = list(csv.DictReader((root / "SHA256SUMS.csv").open(encoding="utf-8", newline="")))
assert rows and len({row["path"] for row in rows}) == len(rows)
for row in rows:
    path = root / row["path"]
    assert path.is_file(), row["path"]
    assert path.stat().st_size == int(row["bytes"]), row["path"]
    assert hashlib.sha256(path.read_bytes()).hexdigest().upper() == row["sha256"], row["path"]
assert max(int(row["bytes"]) for row in rows) < 100_000_000
print(f"PASS: {len(rows)} checksummed files; every regular blob <100,000,000 bytes")
