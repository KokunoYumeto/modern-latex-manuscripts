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
    "bianchi",
    "gordan_clebsch_gordan",
    "steinitz",
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
    "bianchi": "Luigi Bianchi",
    "gordan_clebsch_gordan": "Paul Gordan and Clebsch-Gordan",
    "steinitz": "Ernst Steinitz",
    "additional_author_cluster": "Additional Author Cluster",
}

INDEX_DISPLAY_NAMES = {
    "cayley": "Arthur Cayley (suspect draft/provenance; not accuracy-certified)",
}

RECORD_NOTES = {
    "workflow": [
        "Latest workflow update 2026-06-11 adds distilled lessons from the source-audit sweep: source scans as authority, OCR/Markdown as witnesses rather than canonical text, high-DPI crop packets for diagram/formula audit, explicit artifact quality labels, Zenodo file-limit bundling, GitHub as the public correction surface, and local operational logging for long-running multi-session work.",
    ],
    "bianchi": [
        "Dedicated Bianchi working-edition record. Volume I of `Lezioni di geometria differenziale` remains complete as a package-audited Italian/English working edition through source pdfpages 001-543. The A2 branch, `Lezioni sulla teoria dei gruppi continui finiti di trasformazioni`, now has a promoted high-quality Italian/English start through source p0001-p0066, about 9 percent of the 731-page source. It includes sections 1-12; section 13 begins at the lower part of p0066 and continues on p0067, so p0066 lower-page material is deliberately deferred to the next range. A2 is not complete, and OCR/image-analysis material remains witness/locator evidence only.",
    ],
    "cayley": [
        "Accuracy warning 2026-06-09: this record is not a completed or proofed edition. A source comparison found substantial symbol/text mismatches in current Cayley Volume I material. Existing PDFs, TeX, indexes, and ZIPs are retained as provenance, salvage, and repair material, not as source-faithful transcription, unless a future page-by-page glyph/source audit explicitly re-promotes a specific range. The narrow `Cayley_V1_critical_p001_045_v2_20260609.zip` packet is the current promoted restart tranche for Volume I printed pp.1-45 / complete Papers 1-9; v2 corrects the Paper 6 low-comma subscript notation and removes forced source-page whitespace.",
    ],
    "gordan_clebsch_gordan": [
        "Dedicated Gordan / Clebsch-Gordan working-edition split from the mixed additional-author shelf. The current Abelsche continuation packages are `Gordan_Abel11_p162_173_DE_EN_20260611.zip`, `Gordan_Abel12_p174_181_DE_EN_20260611.zip`, and `Gordan_Abel13_p182_189_DE_EN_20260611.zip`, extending `Theorie der Abelschen Functionen` through source PDF p189 / printed p167. Abel13 deliberately stops at p189, where equation (4) continues onto p190, so the next continuation must start by resolving that display continuation. `Gordan_AllPrior_AuditFix01_20260610.zip` remains the consolidated checkpoint for De linea geodetica, theta, Formensystem, and Abelsche through p121; theta carries the FIX05 `c^8=1` display correction. OCR prose witnesses remain noncanonical gap detectors. These are package-audited, source-witnessed working drafts, not final critical editions.",
    ],
    "steinitz": [
        "Dedicated Steinitz working-edition split from the mixed additional-author shelf. This record includes current package-audited German/English packets for 1910 fields sections 1-24, 1913 Bedingt I complete, strict early works from 1894/1897/1906, 1914 Bedingt II complete, and the first 1916 Bedingt III tranche through pp.1-13. These are source-witnessed working drafts, not final critical editions; OCR layers are locator/check aids only.",
    ],
    "classical_algebra_arithmetic": [
        "Accuracy warning 2026-06-09: Cayley files in this older mixed shelf are retained for provenance and repair only. A source comparison found substantial symbol/text mismatches in current Cayley Volume I material, so Cayley filenames containing `Source-Checked` should be read as obsolete package names rather than a current quality claim. Use the dedicated Cayley record for the latest warning/status.",
    ],
    "sga": [
        "Current caveat from the 2026-06-10 SGA audits: the SGA5 and SGA6 cumulative page-range chains are structurally represented, but they should be treated as substantial working drafts rather than scribe-grade complete editions. For SGA5, the latest promoted repair package is `sga5_repair014_sga6_repair001_20260610.zip`; repair014 closes the current known concrete French phrase-gap locator queue, including the source-page-339 direct-proof sentences, while earlier repair packets remain part of the patch trail. English remains an unsynchronized carry-forward, not a synchronized branch. None of these packages is a final certification of all SGA5 symbols or diagrams; diagram microgeometry, exact-symbol inventory, underlined operator typography outside the patched lane, and English synchronization remain open. The SGA5 witness-aid ZIPs are source-witness/anchor aids, not promoted replacement text or authority in themselves. For SGA6, repair001 restores Expose V §§5.5-5.6 around source pp.348-350, but displayed-label flags and queued repair clusters remain; SGA7 material remains especially provisional unless a specific packet declares source-checked coverage.",
    ],
    "weber": [
        "Current Weber public surface: Volume I is complete as a repaired/source-scan-audited working edition; Volume II now has current German/English cumulative reader PDFs through section 176, with Batch104-Batch106 covering sections 169-176 and localized Batch107-Batch113 recursive repairs/ledgers added for sections including Vol. I §§151, 183 and Vol. II §§20, 58, 61, 118. Batch113 reports 8 closed gap rows and 104 still open, so the recursive gap-audit lane remains active. Volume III remains the current repaired cumulative from the earlier baseline. OCR and display ledgers are omission guards and locator layers, not independent authority; continuation ranges remain working drafts unless the package declares source-checked coverage.",
    ],
    "noether": [
        "Current Noether public surface: the numbered German/English 43-paper corpus remains the canonical branch, while Spanish/Japanese are complete working branches and French/Simplified Chinese are active checkpoint streams. Latest Noether public-surface cleanup removes raw RA12/high-DPI witness material from the current reader-facing record. The numbered German/English corpus and Spanish/Japanese complete working branches remain exposed; French/Simplified Chinese remain checkpoint streams. OCR, high-DPI witnesses, and audit outputs should be distilled into corrected TeX/PDF or concise public status notes before publication.",
    ],
    "additional_author_cluster": [
        "Mixed selected-author shelf. The current routed Poincare package is `poincare_v1_14.zip`, a Tome I French/English cumulative working tranche through Chapter V, including figures 6-15 as source-crop witnesses, with Chapter VI as the next continuation point. Older Poincare ZIPs remain provenance/backstop material rather than the current tranche. Bianchi, Gordan, and Steinitz now have preferred standalone records; their copies here remain backstop/provenance. Loose Bianchi A2 pp.76-90 material is not promoted here until the missing pp.67-75 bridge/context is resolved. Treat this shelf package by package, not as a blanket certification of every included author.",
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

    if reader_pdfs:
        how_to_read = "Open the reader/reference PDFs first. Use artifact ZIPs when you need TeX, source witnesses, OCR, page images, render checks, or provenance material."
    else:
        how_to_read = "This record has no top-level reader PDFs in the current file surface. Open the artifact ZIPs for TeX, component PDFs, source witnesses, OCR, page images, render checks, and provenance material."

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
        how_to_read,
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
