from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest().upper()


errors = []
manifest = ROOT / "ZENODO_PAYLOAD_MANIFEST.csv"
with manifest.open("r", encoding="utf-8-sig", newline="") as handle:
    rows = list(csv.DictReader(handle))

for row in rows:
    path = ROOT / row["relative_path"]
    if not path.is_file():
        errors.append({"code": "missing_file", "path": row["relative_path"]})
        continue
    if path.stat().st_size != int(row["bytes"]):
        errors.append({"code": "byte_mismatch", "path": row["relative_path"]})
    if digest(path) != row["sha256"]:
        errors.append({"code": "sha256_mismatch", "path": row["relative_path"]})

actual = {
    path.relative_to(ROOT).as_posix()
    for path in ROOT.rglob("*")
    if path.is_file() and path != manifest
}
listed = {row["relative_path"] for row in rows}
if actual != listed:
    errors.append(
        {
            "code": "manifest_set_mismatch",
            "missing_from_manifest": sorted(actual - listed),
            "missing_from_tree": sorted(listed - actual),
        }
    )

privacy_patterns = (
    b"C:" + b"\\Users\\",
    b"C:" + b"/" + b"Users/",
    b"/" + b"Users/",
    b"/" + b"home/",
    b"03_" + b"working_translations",
    b"C:" + b"\\tmp\\",
    b"C:" + b"/tmp/",
)
privacy = []
for rel in sorted(actual):
    data = (ROOT / rel).read_bytes()
    for pattern in privacy_patterns:
        count = data.count(pattern)
        if count:
            privacy.append(
                {"relative_path": rel, "pattern": pattern.decode("ascii"), "occurrences": count}
            )
if privacy:
    errors.append({"code": "privacy_hits", "hits": privacy})

print(json.dumps({"status": "PASS" if not errors else "FAIL", "rows": len(rows), "errors": errors}, indent=2))
raise SystemExit(0 if not errors else 1)
