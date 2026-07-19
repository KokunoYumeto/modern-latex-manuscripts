from __future__ import annotations
import csv, hashlib, json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parent
def sha(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda:f.read(1024*1024),b""): h.update(block)
    return h.hexdigest().upper()
errors=[]
with (ROOT/"SHA256SUMS.csv").open("r",encoding="utf-8-sig",newline="") as f:
    rows=list(csv.DictReader(f))
for row in rows:
    p=ROOT/row["relative_path"]
    if not p.is_file() or p.stat().st_size!=int(row["bytes"]) or sha(p)!=row["sha256"]: errors.append(row["relative_path"])
ids=set()
for p in ROOT.rglob("*.jsonl"):
    for line in p.read_text(encoding="utf-8").splitlines():
        if line.strip():
            obj=json.loads(line); rid=obj.get("record_id")
            if not isinstance(rid,str) or rid in ids: errors.append(str(p))
            ids.add(rid)
terms=["archive"+"-maintenance","archive"+" maintenance","archive"+"-owner","task"+"-owned","1 zenodo"+"/github"]
path_re=re.compile(r"(?i)[A-Z]:[\\/]Users[\\/]")
for p in ROOT.rglob("*"):
    if p.is_file() and p.suffix.lower() in {".csv",".json",".jsonl",".log",".md",".py",".tex",".texfrag",".txt"}:
        text=p.read_text(encoding="utf-8",errors="ignore")
        if path_re.search(text) or any(term.lower() in text.lower() for term in terms): errors.append(str(p))
print(json.dumps({"status":"pass" if not errors else "fail","checksum_rows":len(rows),"jsonl_ids":len(ids),"errors":errors},indent=2))
raise SystemExit(1 if errors else 0)
