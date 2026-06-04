#!/usr/bin/env python3
"""Render a PDF page range to PNG files with PyMuPDF.

Pages are 1-indexed at the command line.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import fitz

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf", type=Path)
    ap.add_argument("out_dir", type=Path)
    ap.add_argument("--from-page", type=int, required=True)
    ap.add_argument("--to-page", type=int, required=True)
    ap.add_argument("--dpi", type=int, default=220)
    args = ap.parse_args()

    if args.from_page < 1 or args.to_page < args.from_page:
        raise SystemExit("Invalid page range.")
    args.out_dir.mkdir(parents=True, exist_ok=True)

    doc = fitz.open(str(args.pdf))
    if args.to_page > len(doc):
        raise SystemExit(f"Range exceeds PDF page count {len(doc)}.")
    zoom = args.dpi / 72.0
    matrix = fitz.Matrix(zoom, zoom)
    for pno in range(args.from_page - 1, args.to_page):
        pix = doc[pno].get_pixmap(matrix=matrix, alpha=False)
        pix.save(args.out_dir / f"page-{pno+1:04d}.png")
    doc.close()

if __name__ == "__main__":
    main()
