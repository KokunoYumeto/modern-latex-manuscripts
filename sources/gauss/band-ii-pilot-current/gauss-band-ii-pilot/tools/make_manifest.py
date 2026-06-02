#!/usr/bin/env python3
import csv, hashlib, sys
from pathlib import Path
root=Path(sys.argv[1]) if len(sys.argv)>1 else Path('.')
out=Path(sys.argv[2]) if len(sys.argv)>2 else root/'manifest.csv'
rows=[]
for p in sorted(root.rglob('*')):
    if p.is_file() and p != out:
        h=hashlib.sha256(p.read_bytes()).hexdigest()
        rows.append({'path':str(p.relative_to(root)), 'bytes':p.stat().st_size, 'sha256':h})
with out.open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=['path','bytes','sha256']); w.writeheader(); w.writerows(rows)
print(f'wrote {out} with {len(rows)} files')
