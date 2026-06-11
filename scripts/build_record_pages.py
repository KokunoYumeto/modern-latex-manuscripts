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
    "gibbs_old_physics",
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
    "gibbs_old_physics": "J. Willard Gibbs / Old Physics",
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
        "Dedicated Bianchi working-edition record. Volume I of `Lezioni di geometria differenziale` remains complete as a package-audited Italian/English working edition through source pdfpages 001-543. The A2 branch, `Lezioni sulla teoria dei gruppi continui finiti di trasformazioni`, now has `Bianchi_A2_cont_p0001_0066_IT_EN_20260611.zip` as the preferred continuation package through source p0066: it restores the deferred section 10 opening on p0057 and continues through complete sections 10, 11, and 12. The older `Bianchi_A2_HQ_p0001_0066_IT_EN_20260610.zip` and `Bianchi_A2_auditcont_p0001_0057_IT_EN_20260611.zip` remain provenance/support layers. A2 is not complete; section 13 begins at the lower part of p0066 but is deliberately deferred to the next work unit. OCR/image-analysis material remains witness/locator evidence only.",
    ],
    "cayley": [
        "Accuracy warning 2026-06-09: this record is not a completed or proofed edition. A source comparison found substantial symbol/text mismatches in current Cayley Volume I material. Existing PDFs, TeX, indexes, and ZIPs are retained as provenance, salvage, and repair material, not as source-faithful transcription, unless a future page-by-page glyph/source audit explicitly re-promotes a specific range. The narrow `Cayley_V1_critical_p001_045_v2_20260609.zip` packet is the current promoted restart tranche for Volume I printed pp.1-45 / complete Papers 1-9; v2 corrects the Paper 6 low-comma subscript notation and removes forced source-page whitespace.",
    ],
    "gordan_clebsch_gordan": [
        "Dedicated Gordan / Clebsch-Gordan working-edition split from the mixed additional-author shelf. The current Abelsche continuation now includes `Gordan_Abel16_p218_227_DE_EN_20260611.zip`, extending `Theorie der Abelschen Functionen` through source PDF p227 / printed p205 with current and cumulative DE/EN TeX/PDF, source-scan witnesses, formula crops, ledgers, render checks, and clean build logs. Abel13 remains the p182-p193 promoted segment including the p190 continuation of equation (4), followed by Abel14 p194-p202 and Abel15 p203-p217. `Gordan_AllPrior_AuditFix01_20260610.zip` remains the consolidated checkpoint for De linea geodetica, theta, Formensystem, and Abelsche through p121; theta carries the FIX05 `c^8=1` display correction. OCR prose witnesses remain noncanonical gap detectors. These are package-audited, source-witnessed working drafts, not final critical editions.",
    ],
    "steinitz": [
        "Dedicated Steinitz working-edition split from the mixed additional-author shelf. This record includes current package-audited German/English packets for 1910 fields sections 1-24, 1913 Bedingt I complete, strict early works from 1894/1897/1906, 1914 Bedingt II complete, and the first 1916 Bedingt III tranche through pp.1-13. These are source-witnessed working drafts, not final critical editions; OCR layers are locator/check aids only.",
    ],
    "classical_algebra_arithmetic": [
        "Accuracy warning 2026-06-09: Cayley files in this older mixed shelf are retained for provenance and repair only. A source comparison found substantial symbol/text mismatches in current Cayley Volume I material, so Cayley filenames containing `Source-Checked` should be read as obsolete package names rather than a current quality claim. Use the dedicated Cayley record for the latest warning/status.",
    ],
    "sylvester": [
        "Dedicated Sylvester working-edition split. This record now has a top-level reader and source/index package for Volume I through book page 608. The newest tranche covers book pp.595-608 and completes Papers 59-60; the package audit reports no screenshot substitutions, no placeholders, no includegraphics in the new range, and TeX arrays for the Ferrers partition arrays and ternary-period table. Next continuation starts at book page 609, Paper 61. These are source-checked working editions, not final critical editions; OCR/math-OCR witnesses remain locator/check aids rather than source authority.",
    ],
    "gibbs_old_physics": [
        "Dedicated Gibbs / old-physics working-edition split. Current coverage is The Scientific Papers of J. Willard Gibbs, Volume I, printed pp.001-124: Graphical Methods in the Thermodynamics of Fluids, A Method of Geometrical Representation by Surfaces, and the opening continuation of On the Equilibrium of Heterogeneous Substances. Top-level PDF/TeX files are reader-facing cumulative surfaces; ZIP packets preserve source-scan slices, TeX, and method/audit notes. This is a source-scan-backed working tranche, not a complete Gibbs corpus or final critical edition. Continue after p.124.",
    ],
    "sga": [
        "Current caveat from the 2026-06-11 SGA repairs: SGA5 French is carried through repair016, but this is not a global every-symbol certification. English remains an unsynchronized carry-forward, not a synchronized branch. SGA6 repair003 restores Expose VI source pp.372-387 in French from source scans, replacing compressed/noncanonical material in the projective-bundle calculation and restoring proof material, formulas, statement numbering, and remarks 1.12-1.14. Remaining SGA6 repair lanes include dense clusters pp.388-460 and pp.571-680, diagram geometry, and English synchronization. Treat SGA6 and SGA7 as substantial working drafts with explicit compression caveats unless a specific packet declares source-checked coverage. Witness-aid ZIPs are source-witness/anchor aids, not authority by themselves.",
    ],
    "weber": [
        "Current Weber public surface: Volume I is complete as a repaired/source-scan-audited working edition; Volume II has current German/English cumulative reader PDFs through section 176, with Batch104-Batch106 covering sections 169-176 and localized Batch107-Batch119 recursive repairs/ledgers added for sections including Vol. I §§124, 151, 183 and Vol. II §§20, 21, 52, 57, 58, 60, 61, 77, 99, 101, 118, 126. Batch117 scan-reviewed Volume I §124 as a false-positive/no-change row; Batch119 repairs Volume II §§77 and 101 and reports 17 closed priority repair rows and 95 still open. Volume III remains the current repaired cumulative from the earlier baseline. OCR and display ledgers are omission guards and locator layers, not independent authority; continuation ranges remain working drafts unless the package declares source-checked coverage.",
    ],
    "noether": [
        "Current Noether public surface: the numbered German/English 43-paper corpus remains the canonical branch, while Spanish/Japanese are complete working branches and French/Simplified Chinese are active checkpoint streams. Latest Noether public-surface cleanup removes raw RA12/high-DPI witness material from the current reader-facing record. The numbered German/English corpus and Spanish/Japanese complete working branches remain exposed; French/Simplified Chinese remain checkpoint streams. OCR, high-DPI witnesses, and audit outputs should be distilled into corrected TeX/PDF or concise public status notes before publication.",
    ],
    "additional_author_cluster": [
        "Mixed selected-author shelf. The current routed Kneser package is `Kneser_LVR_p0158_0177_DE_EN_20260611.zip`, a German/English source-witnessed working tranche for Lehrbuch der Variationsrechnung source pp.158-177, covering sections 37-39 complete and carrying cumulative DE/EN TeX/PDF through p177. The same surface retains `poincare_v1_19.zip`, a French/English Poincare Tome I working tranche through Chapter XI, plus `Kneser_LVR_p0139_0158_DE_EN_20260611.zip`, `Frob070_p016_034_final_GE_EN_20260611.zip`, and `Frob071_crit_GE_EN_scans_20260611.zip`. Frob071 is a source-scan-backed German/English working draft for Frobenius item 071 with internal formula/display/alignment audits; it is not a final critical edition. The 2026-06-11 surface pruned clearly superseded Poincare/Picard/Klein-Fricke/Gordan duplicate files from the latest record to stay below Zenodo's 100-file record limit; older Zenodo versions retain those files as provenance. Bianchi, Gordan, Steinitz, Sylvester, and Gibbs now have preferred standalone records; their copies in mixed shelves remain backstop/provenance where present. Treat this shelf package by package, not as a blanket certification of every included author.",
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
