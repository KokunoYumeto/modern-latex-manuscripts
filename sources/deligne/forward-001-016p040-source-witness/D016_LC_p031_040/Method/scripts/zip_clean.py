#!/usr/bin/env python3
"""Zip a clean one-root-folder tree, refusing common build byproducts."""
from __future__ import annotations
import argparse
from pathlib import Path
import zipfile

FORBIDDEN_EXT = {".aux", ".log", ".out", ".toc", ".png", ".jpg", ".jpeg", ".csv", ".md", ".txt"}

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("root", type=Path)
    ap.add_argument("zip_path", type=Path)
    args = ap.parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        raise SystemExit(f"Not a directory: {root}")
    for p in root.rglob("*"):
        if p.is_file() and p.suffix.lower() in FORBIDDEN_EXT:
            raise SystemExit(f"Refusing forbidden build/process file: {p}")

    with zipfile.ZipFile(args.zip_path, "w", compression=zipfile.ZIP_DEFLATED) as z:
        for p in sorted(root.rglob("*")):
            z.write(p, p.relative_to(root.parent))
    print(args.zip_path)

if __name__ == "__main__":
    main()
