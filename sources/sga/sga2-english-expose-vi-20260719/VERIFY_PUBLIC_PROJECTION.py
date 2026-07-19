from __future__ import annotations
import csv, hashlib, json, re
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def sha(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda:f.read(1024*1024),b""): h.update(block)
    return h.hexdigest().upper()
errors=[]
with (ROOT/"SHA256SUMS.csv").open("r",encoding="utf-8-sig",newline="") as f: rows=list(csv.DictReader(f))
for row in rows:
    p=ROOT/row["relative_path"]
    if not p.is_file() or p.stat().st_size!=int(row["bytes"]) or sha(p)!=row["sha256"]: errors.append(row["relative_path"])
private=re.compile(r"(?i)(?:[A-Z]:[\\/]Users[\\/]|C:[\\/]IL_GitHub|archive[- ]maintenance|archive[- ]owner|task[- ]owned|1\s+zenodo/github|019f[0-9a-f]{4}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12})")
for p in ROOT.rglob("*"):
    if p.is_file() and p.suffix.lower() in {".csv",".json",".jsonl",".log",".md",".py",".tex",".txt"}:
        text=p.read_text(encoding="utf-8",errors="strict")
        if private.search(text): errors.append(str(p.relative_to(ROOT)))
print(json.dumps({"status":"pass" if not errors else "fail","checksum_rows":len(rows),"errors":errors},indent=2))
raise SystemExit(1 if errors else 0)
