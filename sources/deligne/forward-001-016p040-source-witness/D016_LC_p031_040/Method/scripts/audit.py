#!/usr/bin/env python3
"""Basic hygiene audit for a clean Deligne paper package root."""
from __future__ import annotations
import argparse
from pathlib import Path
import re
import fitz

FORBIDDEN_EXT = {".aux", ".log", ".out", ".toc", ".png", ".jpg", ".jpeg", ".csv", ".md", ".txt"}
FORBIDDEN_WORDS = [
    "source checked", "verified package", "working draft", "audit report", "screenshot",
    "render_check", "TODO", "FIXME"
]

def pdf_pages(path: Path) -> int:
    doc = fitz.open(str(path))
    n = len(doc)
    doc.close()
    return n

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("root", type=Path)
    args = ap.parse_args()
    root = args.root
    errors: list[str] = []

    if not root.exists():
        raise SystemExit(f"Missing root: {root}")

    for p in root.rglob("*"):
        if p.is_file():
            if p.suffix.lower() in FORBIDDEN_EXT:
                errors.append(f"Forbidden file extension in clean package: {p}")
            low_name = p.name.lower()
            for word in FORBIDDEN_WORDS:
                if word.lower() in low_name:
                    errors.append(f"Forbidden process word in filename: {p}")
            if p.suffix.lower() == ".tex":
                text = p.read_text(encoding="utf-8", errors="ignore").lower()
                for word in FORBIDDEN_WORDS:
                    if word.lower() in text:
                        errors.append(f"Forbidden process word in TeX text: {p}: {word}")
            if p.suffix.lower() == ".pdf":
                try:
                    n = pdf_pages(p)
                    if n <= 0:
                        errors.append(f"Zero-page PDF: {p}")
                except Exception as e:
                    errors.append(f"Could not open PDF {p}: {e}")

    # Ensure every Installment/Cumulative folder has TEX/PDF/SCAN.
    for branch in [p for p in root.iterdir() if p.is_dir()]:
        for sub in ("TEX", "PDF", "SCAN"):
            if not (branch / sub).is_dir():
                errors.append(f"Missing {sub}/ in {branch}")

    if errors:
        for e in errors:
            print("ERROR:", e)
        raise SystemExit(1)
    print("OK")

if __name__ == "__main__":
    main()
