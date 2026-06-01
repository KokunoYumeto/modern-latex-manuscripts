#!/usr/bin/env python3
"""Lightweight invariant checks for translated TeX modules."""
from __future__ import annotations
import re, sys, pathlib, json

PATTERNS = {
    'labels': re.compile(r'\\label\{[^}]+\}'),
    'refs': re.compile(r'\\(?:eqref|ref)\{[^}]+\}'),
    'cites': re.compile(r'\\cite[a-zA-Z]*\{[^}]+\}'),
    'checks': re.compile(r'\[\[CHECK:[^\]]+\]\]'),
    'bad_unicode': re.compile(r'�'),
}

def count(path: pathlib.Path):
    text = path.read_text(errors='replace')
    return {k: len(p.findall(text)) for k,p in PATTERNS.items()}

def main():
    if len(sys.argv) < 2:
        print('usage: tex_invariant_check.py file_or_dir [file_or_dir...]')
        raise SystemExit(2)
    files=[]
    for arg in sys.argv[1:]:
        p=pathlib.Path(arg)
        if p.is_dir():
            files.extend(p.rglob('*.tex'))
        elif p.suffix == '.tex':
            files.append(p)
    result={str(p): count(p) for p in files}
    print(json.dumps(result, ensure_ascii=False, indent=2))
if __name__ == '__main__':
    main()
