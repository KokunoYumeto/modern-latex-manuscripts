#!/usr/bin/env python3
"""Simple local helper: split a TeX file at section/subsection anchors.
It does not translate. It creates batch text files plus a CSV manifest.
"""
from pathlib import Path
import argparse, re, csv

parser = argparse.ArgumentParser()
parser.add_argument('tex_file')
parser.add_argument('--out', default='spark_batches')
parser.add_argument('--prefix', default='batch')
args = parser.parse_args()

src = Path(args.tex_file)
out = Path(args.out)
out.mkdir(parents=True, exist_ok=True)
text = src.read_text(encoding='utf-8', errors='replace')
anchors = list(re.finditer(r'(?m)^\\(section|subsection|subsubsection)\*?\{([^}]*)\}', text))
if not anchors:
    anchors = [re.match(r'', text)]
rows = []
for i, m in enumerate(anchors):
    start = m.start()
    end = anchors[i+1].start() if i+1 < len(anchors) else len(text)
    title = m.group(2) if hasattr(m, 'group') and m.lastindex and m.lastindex >= 2 else f'chunk {i+1}'
    chunk = text[start:end]
    bid = f'{args.prefix}_{i+1:03d}'
    fname = out / f'{bid}.tex'
    fname.write_text(chunk, encoding='utf-8')
    rows.append({'batch_id': bid, 'source_file': str(src), 'section_title': title, 'output_file': str(fname), 'chars': len(chunk)})
with (out / 'manifest.csv').open('w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=['batch_id','source_file','section_title','output_file','chars'])
    w.writeheader(); w.writerows(rows)
print(f'wrote {len(rows)} batches to {out}')
