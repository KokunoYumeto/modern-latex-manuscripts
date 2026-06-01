#!/usr/bin/env python3
"""Compare labels/refs/cites/begin/end command inventory between source and translation."""
from pathlib import Path
import argparse, re, collections
parser=argparse.ArgumentParser()
parser.add_argument('source')
parser.add_argument('translated')
args=parser.parse_args()
patterns = {
    'label': r'\\label\{[^}]+\}',
    'ref': r'\\(?:ref|eqref|autoref)\{[^}]+\}',
    'cite': r'\\cite[a-zA-Z]*\{[^}]+\}',
    'begin': r'\\begin\{[^}]+\}',
    'end': r'\\end\{[^}]+\}',
}
for name, pat in patterns.items():
    a=collections.Counter(re.findall(pat, Path(args.source).read_text(encoding='utf-8', errors='replace')))
    b=collections.Counter(re.findall(pat, Path(args.translated).read_text(encoding='utf-8', errors='replace')))
    missing=a-b; added=b-a
    print(f'## {name}')
    print('missing:', dict(missing))
    print('added:', dict(added))
