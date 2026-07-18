from __future__ import annotations

import csv
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PRIVATE = re.compile(r"(?i)(?:[A-Z]:[\\/]Users[\\/]|Users[\\/]Floris|C:[\\/]IL_GitHub|/home/[^/\s]+|\bFloris\b|\bCodex\b|\bClaude\b|archive-maintenance|1\s+zenodo/github|019f[0-9a-f]{4}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12})")

def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest().upper()

errors = []
with (ROOT / "PUBLIC_SHA256SUMS.csv").open(encoding="utf-8-sig", newline="") as handle:
    rows = list(csv.DictReader(handle))
for row in rows:
    path = ROOT / row["path"]
    if not path.is_file():
        errors.append(f"missing:{row['path']}")
    elif path.stat().st_size != int(row["bytes"]) or digest(path) != row["sha256"]:
        errors.append(f"mismatch:{row['path']}")
for path in ROOT.rglob("*"):
    if path.is_file() and path.suffix.lower() in {".csv", ".json", ".jsonl", ".md", ".txt", ".py"}:
        if path.name == "VALIDATE_PUBLIC_PACKAGE.py":
            continue
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        if PRIVATE.search(text):
            errors.append(f"private:{path.relative_to(ROOT).as_posix()}")
print({"rows": len(rows), "errors": errors})
sys.exit(1 if errors else 0)
