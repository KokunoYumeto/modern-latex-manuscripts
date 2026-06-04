#!/usr/bin/env python3
"""Compile a TeX file twice with pdflatex and fail on errors."""
from __future__ import annotations
import argparse
from pathlib import Path
import subprocess
import sys

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("tex", type=Path)
    args = ap.parse_args()
    tex = args.tex.resolve()
    if not tex.exists():
        raise SystemExit(f"Missing TeX file: {tex}")
    cmd = ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", tex.name]
    for run in range(2):
        proc = subprocess.run(cmd, cwd=str(tex.parent), text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        if proc.returncode != 0:
            sys.stderr.write(proc.stdout[-5000:])
            raise SystemExit(proc.returncode)
    print(tex.with_suffix(".pdf"))

if __name__ == "__main__":
    main()
