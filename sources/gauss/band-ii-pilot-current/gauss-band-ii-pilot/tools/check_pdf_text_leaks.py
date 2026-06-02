#!/usr/bin/env python3
"""Check PDFs for obvious raw-TeX leakage in extracted text."""
import subprocess, sys, re, json
from pathlib import Path
PATTERNS = [r'\\\\frac', r'\\\\partial', r'\\\\begin', r'\\\\end', r'\\\\delta', r'\\\\psi', r'\\\\text', r'\\\\section', r'\\\\left', r'\\\\right']

def extract(pdf: Path) -> str:
    try:
        return subprocess.check_output(['pdftotext', str(pdf), '-'], text=True, stderr=subprocess.DEVNULL)
    except Exception as e:
        return f"__PDFTOTEXT_ERROR__ {e}"

def check(pdf: Path):
    txt = extract(pdf)
    hits = {}
    for pat in PATTERNS:
        m = re.findall(pat, txt)
        if m:
            hits[pat] = len(m)
    return {'pdf': str(pdf), 'text_chars': len(txt), 'hits': hits, 'ok': not hits}

if __name__ == '__main__':
    paths = [Path(p) for p in sys.argv[1:]]
    if not paths:
        paths = list(Path('.').rglob('*.pdf'))
    results = [check(p) for p in paths]
    print(json.dumps(results, indent=2, ensure_ascii=False))
    sys.exit(0 if all(r['ok'] for r in results) else 1)
