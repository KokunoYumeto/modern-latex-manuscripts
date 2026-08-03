#!/usr/bin/env python3
"""Bounded page-by-page scan for producer prose on selected SGA readers."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from pathlib import Path

from pypdf import PdfReader


PHRASES = (
    "source and status note",
    "source note",
    "editorial note",
    "editorial status",
    "source status",
    "working reader",
    "working translation",
    "source-backed",
    "source checked",
    "source-checked",
    "source-first",
    "workpass",
    "not certified",
    "not a critical edition",
    "publication readiness",
    "quality assurance",
    "sha-256",
    "sha256",
    "provenance",
    "prepared for the interlanguage",
    "interlanguage mathematical translation",
    "translation and preservation project",
    "this reader provides",
    "authority is layered",
    "source scan pages",
    "underlying-source",
    "license questions",
    "correction ledger",
    "audit status",
    "producer note",
    "workflow",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def formula_risks(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    risks: list[dict[str, str]] = []
    for row_number, row in enumerate(rows, start=2):
        for field, value in row.items():
            if str(value).startswith(("=", "+", "-", "@")):
                risks.append({"row": str(row_number), "field": field, "value": str(value)})
    return risks


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", type=Path, required=True)
    parser.add_argument("--inputs", type=Path, required=True)
    parser.add_argument("--hits-output", type=Path, required=True)
    parser.add_argument("--validation-output", type=Path, required=True)
    args = parser.parse_args()

    if args.hits_output.exists() or args.validation_output.exists():
        raise SystemExit("Refusing to overwrite an existing scan output")
    with args.inputs.open(encoding="utf-8-sig", newline="") as stream:
        inputs = list(csv.DictReader(stream))
    errors: list[str] = []
    hits: list[dict[str, str]] = []
    readers: list[dict[str, object]] = []
    total_pages = 0
    for input_row in inputs:
        pdf_path = args.project_root / Path(input_row["pdf_path"])
        if not pdf_path.exists():
            errors.append(f"missing PDF: {input_row['pdf_path']}")
            continue
        actual_hash = sha256(pdf_path)
        if actual_hash != input_row["expected_sha256"]:
            errors.append(f"hash mismatch: {input_row['input_id']}")
        reader = PdfReader(str(pdf_path), strict=True)
        expected_pages = int(input_row["expected_pages"])
        if len(reader.pages) != expected_pages:
            errors.append(
                f"page mismatch: {input_row['input_id']} expected={expected_pages} actual={len(reader.pages)}"
            )
        total_pages += len(reader.pages)
        reader_hit_count = 0
        for page_number, page in enumerate(reader.pages, start=1):
            text = normalize(page.extract_text() or "")
            lowered = text.lower()
            for phrase in PHRASES:
                search_from = 0
                while True:
                    position = lowered.find(phrase, search_from)
                    if position < 0:
                        break
                    context_start = max(0, position - 120)
                    context_end = min(len(text), position + len(phrase) + 120)
                    hits.append(
                        {
                            "hit_id": f"SGA-SURFACE-HIT-{len(hits)+1:04d}",
                            "input_id": input_row["input_id"],
                            "volume": input_row["volume"],
                            "pdf_path": input_row["pdf_path"],
                            "pdf_page": str(page_number),
                            "phrase": phrase,
                            "context": text[context_start:context_end],
                            "scan_disposition": "requires_lead_adjudication",
                        }
                    )
                    reader_hit_count += 1
                    search_from = position + len(phrase)
        readers.append(
            {
                "input_id": input_row["input_id"],
                "volume": input_row["volume"],
                "pdf_path": input_row["pdf_path"],
                "pages": len(reader.pages),
                "bytes": pdf_path.stat().st_size,
                "sha256": actual_hash,
                "phrase_hits": reader_hit_count,
            }
        )

    fieldnames = [
        "hit_id",
        "input_id",
        "volume",
        "pdf_path",
        "pdf_page",
        "phrase",
        "context",
        "scan_disposition",
    ]
    args.hits_output.parent.mkdir(parents=True, exist_ok=True)
    with args.hits_output.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(hits)
    risks = formula_risks(hits)
    if risks:
        errors.append(f"formula-risk cells in hit ledger: {risks}")
    result = {
        "schema": "sga-reader-surface-producer-prose-scan-v1",
        "status": (
            "FAIL"
            if errors
            else "PASS_NO_HITS"
            if not hits
            else "HOLD_HITS_REQUIRE_LEAD_ADJUDICATION"
        ),
        "errors": errors,
        "input_manifest": {
            "path": str(args.inputs),
            "bytes": args.inputs.stat().st_size,
            "sha256": sha256(args.inputs),
            "rows": len(inputs),
        },
        "reader_count": len(readers),
        "total_pages": total_pages,
        "phrase_vocabulary": list(PHRASES),
        "hit_count": len(hits),
        "readers": readers,
        "hits_csv": {
            "path": str(args.hits_output),
            "bytes": args.hits_output.stat().st_size,
            "sha256": sha256(args.hits_output),
            "rows": len(hits),
            "columns": len(fieldnames),
            "rectangular": True,
            "formula_risk_cells": risks,
        },
    }
    args.validation_output.write_text(
        json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
