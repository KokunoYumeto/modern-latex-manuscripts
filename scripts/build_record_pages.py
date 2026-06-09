#!/usr/bin/env python3
"""Build per-record Markdown landing pages from the public file catalog.

Run from the repository root after `manifests/public-file-catalog.csv` exists:

    python scripts/build_record_pages.py

Outputs:
    docs/records/README.md
    docs/records/<record_label>.md
"""

from __future__ import annotations

import csv
import html
import re
from collections import defaultdict
from pathlib import Path


RECORD_ORDER = [
    "main",
    "workflow",
    "noether",
    "weber",
    "cayley",
    "ega",
    "sga",
    "deligne",
    "ukrainian_applied_math",
    "gauss",
    "albattani_opus_astronomicum",
    "non_european_consolidated",
    "chinese",
    "indian_sanskrit",
    "islamic_arabic",
    "historical_references",
    "classical_algebra_arithmetic",
    "sylvester",
    "dedekind",
    "dirichlet",
    "additional_author_cluster",
]


DISPLAY_NAMES = {
    "main": "Main Project Landing",
    "workflow": "Workflow / Replication Packet",
    "noether": "Emmy Noether",
    "weber": "Heinrich Weber",
    "cayley": "Arthur Cayley",
    "ega": "EGA",
    "sga": "SGA",
    "deligne": "Pierre Deligne",
    "ukrainian_applied_math": "Ukrainian Applied Mathematics",
    "gauss": "Gauss",
    "albattani_opus_astronomicum": "al-Battani Opus Astronomicum",
    "non_european_consolidated": "Non-European Mathematics, Consolidated",
    "chinese": "Chinese Mathematical Classics",
    "indian_sanskrit": "Indian and Sanskrit Mathematical Classics",
    "islamic_arabic": "Islamic and Arabic Mathematical Texts",
    "historical_references": "Historical Reference Witnesses",
    "classical_algebra_arithmetic": "Classical Algebra and Arithmetic",
    "sylvester": "James Joseph Sylvester",
    "dedekind": "Richard Dedekind",
    "dirichlet": "P. G. Lejeune Dirichlet",
    "additional_author_cluster": "Additional Author Cluster",
}

INDEX_DISPLAY_NAMES = {
    "cayley": "Arthur Cayley (suspect draft/provenance; not accuracy-certified)",
}

RECORD_NOTES = {
    "cayley": [
        "Accuracy warning 2026-06-09: this record is not a completed or proofed edition. A source comparison found substantial symbol/text mismatches in current Cayley Volume I material. Existing PDFs, TeX, indexes, and ZIPs are retained as provenance, salvage, and repair material, not as source-faithful transcription, unless a future page-by-page glyph/source audit explicitly re-promotes a specific range.",
    ],
    "classical_algebra_arithmetic": [
        "Accuracy warning 2026-06-09: Cayley files in this older mixed shelf are retained for provenance and repair only. A source comparison found substantial symbol/text mismatches in current Cayley Volume I material, so Cayley filenames containing `Source-Checked` should be read as obsolete package names rather than a current quality claim. Use the dedicated Cayley record for the latest warning/status.",
    ],
    "sga": [
        "Current caveat from the 2026-06-09 SGA audits: the SGA5 and SGA6 cumulative page-range chains are structurally represented, but they should be treated as substantial working drafts rather than scribe-grade complete editions. For SGA5, the accepted local repair lane repaired p378-p382, repair003 closed p194, p400, p419, p431, p432, p433, and p460, and repair004 closes p165, p188, and p459 while leaving English unsynchronized to the latest French repair state. SGA5 still needs a global diagram/exact-symbol inventory. For SGA6, the audit confirms localized compression/omission samples on source pages 014 and 625, with strong candidates on 431 and 679; the next repair targets are p014, then the clusters 423-454, 619-653, and 670-692. Later external visual-repair output is not promoted unless individual source-crop checks independently re-establish a patch.",
    ],
}


def slug(label: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", label.lower()).strip("-")


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def size_sum(rows: list[dict[str, str]]) -> float:
    return sum(float(row["size_mb"]) for row in rows)


def role_rows(rows: list[dict[str, str]], role: str) -> list[dict[str, str]]:
    return [row for row in rows if row["file_role"] == role]


def table_for(rows: list[dict[str, str]], include_role: bool = False) -> list[str]:
    if not rows:
        return ["No files in this group.", ""]

    if include_role:
        lines = ["| Role | Size MB | File |", "|---|---:|---|"]
    else:
        lines = ["| Size MB | File |", "|---:|---|"]

    for row in rows:
        filename = html.escape(row["filename"])
        url = row["url"]
        if include_role:
            lines.append(f"| {row['file_role']} | {row['size_mb']} | [{filename}]({url}) |")
        else:
            lines.append(f"| {row['size_mb']} | [{filename}]({url}) |")
    lines.append("")
    return lines


def write_record_page(label: str, rows: list[dict[str, str]], out_dir: Path) -> None:
    display = DISPLAY_NAMES.get(label, label.replace("_", " ").title())
    title = rows[0]["record_title"]
    record_id = rows[0]["record_id"]
    url = f"https://zenodo.org/records/{record_id}"
    pdfs = [row for row in rows if row["filename"].lower().endswith(".pdf")]
    zips = [row for row in rows if row["filename"].lower().endswith(".zip")]
    manifests = role_rows(rows, "manifest/status")
    reader_pdfs = role_rows(rows, "reader/reference PDF")
    other_pdfs = [row for row in pdfs if row not in reader_pdfs]

    lines = [
        f"# {display}",
        "",
        f"Zenodo record: [{record_id}]({url})",
        "",
        f"Public title: {html.escape(title)}",
        "",
        "| Files | PDFs | ZIPs | Total MB |",
        "|---:|---:|---:|---:|",
        f"| {len(rows)} | {len(pdfs)} | {len(zips)} | {size_sum(rows):.1f} |",
        "",
        "## How To Read This Record",
        "",
        "Open the reader/reference PDFs first. Use artifact ZIPs when you need TeX, source witnesses, OCR, page images, render checks, or provenance material.",
        "",
    ]
    for note in RECORD_NOTES.get(label, []):
        lines.extend([note, ""])
    lines.extend(
        [
            "Corrections, source comparisons, LaTeX fixes, and translation improvements can be suggested through GitHub issues or pull requests: <https://github.com/KokunoYumeto/modern-latex-manuscripts>.",
            "",
            "## Reader And Reference PDFs",
            "",
        ]
    )
    lines.extend(table_for(reader_pdfs))

    if other_pdfs:
        lines.extend(["## Additional PDFs", ""])
        lines.extend(table_for(other_pdfs))

    lines.extend(["## Artifact ZIPs", ""])
    lines.extend(table_for(zips))

    lines.extend(["## Manifest And Status Files", ""])
    lines.extend(table_for(manifests))

    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / f"{slug(label)}.md").write_text("\n".join(lines), encoding="utf-8")


def write_index(grouped: dict[str, list[dict[str, str]]], out_dir: Path) -> None:
    lines = [
        "# Record Landing Pages",
        "",
        "These pages are generated from `manifests/public-file-catalog.csv` and group each public Zenodo record into reader PDFs, artifact ZIPs, and manifest/status files.",
        "",
        "| Record | Files | PDFs | ZIPs | MB | Page | Zenodo |",
        "|---|---:|---:|---:|---:|---|---|",
    ]
    for label in RECORD_ORDER:
        rows = grouped.get(label)
        if not rows:
            continue
        display = INDEX_DISPLAY_NAMES.get(label, DISPLAY_NAMES.get(label, label.replace("_", " ").title()))
        record_id = rows[0]["record_id"]
        pdfs = [row for row in rows if row["filename"].lower().endswith(".pdf")]
        zips = [row for row in rows if row["filename"].lower().endswith(".zip")]
        page = f"{slug(label)}.md"
        lines.append(
            f"| {display} | {len(rows)} | {len(pdfs)} | {len(zips)} | {size_sum(rows):.1f} | [{page}]({page}) | [Zenodo](https://zenodo.org/records/{record_id}) |"
        )
    lines.append("")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "README.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    root = Path.cwd()
    rows = read_rows(root / "manifests" / "public-file-catalog.csv")
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[row["record_label"]].append(row)

    out_dir = root / "docs" / "records"
    for label in RECORD_ORDER:
        if label in grouped:
            write_record_page(label, grouped[label], out_dir)
    write_index(grouped, out_dir)
    print(f"Wrote {len(grouped)} record landing pages to {out_dir}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
