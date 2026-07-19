from __future__ import annotations
import csv, hashlib, json
from pathlib import Path
root = Path(__file__).resolve().parent
errors = []
with (root / "SHA256SUMS.csv").open("r", encoding="utf-8-sig", newline="") as handle:
    rows = list(csv.DictReader(handle))
for row in rows:
    path = root / row["relative_path"]
    if not path.is_file() or path.stat().st_size != int(row["bytes"]):
        errors.append("size:" + row["relative_path"]); continue
    if hashlib.sha256(path.read_bytes()).hexdigest().upper() != row["sha256"].upper():
        errors.append("hash:" + row["relative_path"])
ids = set()
for path in sorted(root.rglob("*.jsonl")):
    for line in path.read_text(encoding="utf-8").splitlines():
        item = json.loads(line)
        rid = item.get("record_id") or item.get("id")
        if not rid or rid in ids: errors.append("jsonl-id:" + str(rid))
        ids.add(rid)
print(json.dumps({"status":"pass" if not errors else "fail","checksum_rows":len(rows),"jsonl_ids":len(ids),"errors":errors},indent=2))
raise SystemExit(1 if errors else 0)
