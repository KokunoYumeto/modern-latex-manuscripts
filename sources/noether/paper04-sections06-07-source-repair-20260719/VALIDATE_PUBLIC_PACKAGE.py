from __future__ import annotations
import csv, hashlib, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PRIVATE = re.compile(r"(?i)(?:[A-Z]:[\\/]Users[\\/]|Users[\\/]Floris|C:[\\/]IL_GitHub|C:[\\/]tmp|/home/[^/\s]+|\bFloris\b|\bCodex\b|\bClaude\b|archive-maintenance|1\s+zenodo/github|019f[0-9a-f]{4}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12})")

def digest(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
    return h.hexdigest().upper()

errors=[]
with (ROOT/'PUBLIC_SHA256SUMS.csv').open(encoding='utf-8-sig',newline='') as f: rows=list(csv.DictReader(f))
for row in rows:
    p=ROOT/row['path']
    if not p.is_file(): errors.append('missing:'+row['path'])
    elif p.stat().st_size!=int(row['bytes']) or digest(p)!=row['sha256']: errors.append('mismatch:'+row['path'])
for p in ROOT.rglob('*'):
    if p.is_file() and p.suffix.lower() in {'.csv','.diff','.json','.jsonl','.md','.txt','.py'} and p.name!='VALIDATE_PUBLIC_PACKAGE.py':
        text=p.read_text(encoding='utf-8-sig',errors='replace')
        if PRIVATE.search(text): errors.append('private:'+p.relative_to(ROOT).as_posix())
        if p.suffix.lower()=='.json':
            try: json.loads(text)
            except Exception as exc: errors.append('json:'+p.relative_to(ROOT).as_posix()+':'+str(exc))
        if p.suffix.lower()=='.jsonl':
            for i,line in enumerate(text.splitlines(),1):
                if line.strip():
                    try: json.loads(line)
                    except Exception as exc: errors.append(f'jsonl:{p.relative_to(ROOT).as_posix()}:{i}:{exc}')
print({'rows':len(rows),'errors':errors})
sys.exit(1 if errors else 0)
