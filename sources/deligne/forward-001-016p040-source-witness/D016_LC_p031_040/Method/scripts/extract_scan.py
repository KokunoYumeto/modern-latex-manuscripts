#!/usr/bin/env python3
"""Extract a page range from a source PDF as a scan sidecar PDF.

Pages are 1-indexed at the command line.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import fitz

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("source_pdf", type=Path)
    ap.add_argument("out_pdf", type=Path)
    ap.add_argument("--from-page", type=int, required=True)
    ap.add_argument("--to-page", type=int, required=True)
    args = ap.parse_args()

    src = fitz.open(str(args.source_pdf))
    if args.from_page < 1 or args.to_page > len(src) or args.to_page < args.from_page:
        raise SystemExit(f"Invalid page range for PDF with {len(src)} pages.")
    out = fitz.open()
    out.insert_pdf(src, from_page=args.from_page - 1, to_page=args.to_page - 1)
    args.out_pdf.parent.mkdir(parents=True, exist_ok=True)
    out.save(str(args.out_pdf))
    out.close()
    src.close()

if __name__ == "__main__":
    main()
