#!/usr/bin/env python3
import csv, hashlib, json, re
from pathlib import Path
import argparse

def sha256(p: Path) -> str:
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1<<20), b''):
            h.update(b)
    return h.hexdigest()

def title_guess(txt: str) -> str:
    m=re.search(r'\\title\s*\{(.{0,700})', txt, re.S)
    if not m: return ''
    s=m.group(1).split('\n')[0]
    s=re.sub(r'\\[a-zA-Z]+\*?(\[[^\]]*\])?(\{[^}]*\})?', '', s)
    return re.sub(r'[{}\\]+',' ',s).strip()[:200]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('source_root')
    ap.add_argument('quality_csv')
    ap.add_argument('out_csv')
    args=ap.parse_args()
    q={}
    with open(args.quality_csv, newline='', encoding='utf-8') as f:
        for r in csv.DictReader(f):
            q[r['rel_path']]=r
    root=Path(args.source_root)
    rows=[]
    for p in sorted(root.glob('*/*.tex')):
        rel=str(p.relative_to(root))
        txt=p.read_text(errors='ignore')
        comments=[]
        for line in txt.splitlines()[:12]:
            if line.strip().startswith('%'):
                comments.append(line.strip('% ').strip())
        qr=q.get(rel,{})
        rows.append({
            'rel_path': rel,
            'bytes': p.stat().st_size,
            'lines': len(txt.splitlines()),
            'sha256': sha256(p),
            'grade': qr.get('grade',''),
            'score': qr.get('score',''),
            'flags': qr.get('flags',''),
            'title_guess': title_guess(txt),
            'opening_comments': ' | '.join(comments)[:300]
        })
    with open(args.out_csv, 'w', newline='', encoding='utf-8') as f:
        w=csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    print(json.dumps({'files':len(rows),'out':args.out_csv}, indent=2))
if __name__=='__main__': main()
