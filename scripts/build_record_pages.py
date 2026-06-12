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
    "maxwell",
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
    "maxwell": "James Clerk Maxwell",
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
        "Latest workflow update 2026-06-12 adds source-audit/public-surface and object-level audit rules: reader-first latest records, source-image authority, derivative-PDF traps, OCR as locator rather than judge, page-map requirements, aid-package design, reliability labels, and the rule that diagram/table promotion needs a source object witness, output render witness, stable object ID, and explicit ledger verdict. The live workflow notes also record the SGA OCR lesson that Surya-style GPU OCR can be a stronger math/prose locator for French mathematical typescript than ordinary CPU OCR, while OCR from a mismatched source copy must not be used for page-precise claims without a source checksum and page map. Earlier workflow files document source/edition identity checks, structured repair worklists, high-DPI crop packets, local-to-web audit loops, Lean/Lake as a selective formal-checking companion, and GitHub/Zenodo publication hygiene.",
    ],
    "bianchi": [
        "Dedicated Bianchi working-edition record. Volume I of `Lezioni di geometria differenziale` remains represented as a package-audited Italian/English working edition through source pdfpages 001-543. The A2 branch now continues through source p0105 / about 14.36 percent of the 731-page source sequence, with `Bianchi_A2_cont_p0001_0105_IT_EN_20260612.zip` as the latest package. It adds source pp.0091-0105 after the p0001-p0090 summation repair, includes a notation logbook and machine-readable equation indices, and leaves the next continuation at source p0106, continuing section 27 after formula (17). The current package is a working manuscript witness: TeX builds and renders, but matrix dots, prime marks, summation superscripts, and handwritten-symbol details still need continuing source/glyph audit. OCR/image-analysis material remains witness/locator evidence only.",
    ],
    "cayley": [
        "Accuracy warning 2026-06-09/12: this record is not a completed or proofed edition. A source comparison found substantial symbol/text mismatches in current Cayley Volume I material. Existing PDFs, TeX, indexes, and ZIPs are retained as provenance, salvage, and repair material, not as source-faithful transcription, unless a future page-by-page glyph/source audit explicitly re-promotes a specific range. The narrow `Cayley_V1_critical_p001_045_v2_20260609.zip` packet is the current promoted restart tranche for Volume I printed pp.1-45 / Papers 1-9 as a source-inspected working packet, not as a critical edition; v2 corrects the Paper 6 low-comma subscript notation and removes forced source-page whitespace. Do not infer reliability from inherited filenames: several older reader PDFs and ZIPs still contain phrases such as `Source-Checked`, but those labels are obsolete for Cayley unless the specific package is named in the promoted restart note above or in a later source-audit note. A later source-quality audit found that several Cayley repair lanes had been working from low-DPI Internet Archive derivative PDFs; future source-faithful repair should prefer the IA `_jp2.zip` master image archives and verified scan-page maps where available.",
    ],
    "gordan_clebsch_gordan": [
        "Dedicated Gordan / Clebsch-Gordan working-edition split from the mixed additional-author shelf. The current Abelsche continuation now includes `Gordan_Abel25_p322_331_DE_EN_20260612.zip`, covering source pp.322-331 / printed pp.300-309 and cumulative German/English TeX/PDF through source p331. It completes sections 85 and 86 and begins section 87 through formula (5) plus the first normalization paragraph for third-kind integrals. The package audit reports no unresolved scan-quality blocker and checks determinant conditions, minor relations, row/column reductions I-IV, and period-transformation formulas. Earlier Abel tranches and `Gordan_AllPrior_AuditFix01_20260610.zip` remain support/provenance and correction layers. OCR prose witnesses remain noncanonical gap detectors. These are package-audited, source-witnessed working drafts, not final critical editions.",
    ],
    "steinitz": [
        "Dedicated Steinitz working-edition split from the mixed additional-author shelf. This record includes current package-audited German/English packets for 1910 fields sections 1-24, 1913 Bedingt I complete, strict early works from 1894/1897/1906, 1914 Bedingt II complete, and the first 1916 Bedingt III tranche through pp.1-13. These are source-witnessed working drafts, not final critical editions; OCR layers are locator/check aids only.",
    ],
    "classical_algebra_arithmetic": [
        "Accuracy warning 2026-06-09: Cayley files in this older mixed shelf are retained for provenance and repair only. A source comparison found substantial symbol/text mismatches in current Cayley Volume I material, so Cayley filenames containing `Source-Checked` should be read as obsolete package names rather than a current quality claim. Use the dedicated Cayley record for the latest warning/status.",
    ],
    "sylvester": [
        "Dedicated Sylvester working-edition split. This record now has a top-level reader and source/index package for Volume I through book page 608. The newest tranche covers book pp.595-608 and structurally covers Papers 59-60; the package audit reports no screenshot substitutions, no placeholders, no includegraphics in the new range, and TeX arrays for the Ferrers partition arrays and ternary-period table. Next continuation starts at book page 609, Paper 61. These are source-witnessed working drafts, not final critical editions; OCR/math-OCR witnesses remain locator/check aids rather than source authority.",
    ],
    "maxwell": [
        "Dedicated Maxwell working-tranche split. Current coverage is A Treatise on Electricity and Magnetism, Volume I: IA 1873 first-edition pp.001-059, with math/token registers currently refreshed through pp.001-058 and p.059 queued for the next register refresh, plus earlier ledger-backed source-witnessed working tranches for book pages 95-101, 103, 105, 109, and the main continuous run 111-267. The included broader batch TeX/PDF substrate is status-mixed; promoted range claims are governed by ledgers and source witness images. OCR/XML witnesses are locator/provenance aids, not textual authority. This is not a complete Maxwell Treatise or final critical edition. Printed p.060 is the next continuation point.",
    ],
    "gibbs_old_physics": [
        "Dedicated Gibbs / old-physics working-edition split. Current coverage is The Scientific Papers of J. Willard Gibbs, Volume I, printed pp.001-124: Graphical Methods in the Thermodynamics of Fluids, A Method of Geometrical Representation by Surfaces, and the opening continuation of On the Equilibrium of Heterogeneous Substances. Top-level PDF/TeX files are reader-facing cumulative surfaces; ZIP packets preserve source-scan slices, TeX, and method/audit notes. This is a source-scan-backed working tranche, not a complete Gibbs corpus or final critical edition. Continue after p.124.",
    ],
    "sga": [
        "Current caveat from the 2026-06-12 SGA repair025 update: repair025 carries forward cumulative SGA5/SGA6 French TeX/PDF, covers SGA5 French source pp.160, 171, 174-177, and 180, and includes a 484-page source-indexed SGA5 audit PDF plus source-to-current-French-page map. SGA6 French is unchanged; SGA5 English remains an unsynchronized carry-forward branch. SGA6 dense worklist material remains open and was not touched in repair025. Treat SGA6 and SGA7 as substantial working drafts with explicit compression caveats unless a specific packet declares source-checked coverage. Older filenames containing words such as `Complete` or `Source-Checked` should be read as legacy package names, not current global certification. Witness-aid ZIPs are source-witness/anchor aids, not authority by themselves. Due to Zenodo's 100-file ceiling, older aid-only witness package `SGA5_r007_diag_aid_20260609.zip` was removed from this latest file surface while prior versions preserve it.",
    ],
    "weber": [
        "Current Weber public surface: Volume I is represented as a repaired/source-scan-audited working edition; Volume II has current German/English cumulative reader PDFs through section 176, with Batch104-Batch129 covering sections 169-176 plus localized recursive repairs/ledgers. Batch129 repairs Volume II sections 33-34 from source scans pp.134-140, with p.141 / section 35 treated as the handoff boundary, replacing compressed/simple-group material in the cumulative Volume II branch, including Frobenius proof material, footnotes, and explicit permutation arrays for the simple group of degree 60. Batch129 reports an estimated 68/112 repair rows closed and 44/112 open. Volume III remains the current repaired cumulative from the earlier baseline. OCR and display ledgers are omission guards and locator layers, not independent authority; continuation ranges remain working drafts unless the package declares source-checked coverage.",
    ],
    "noether": [
        "Current Noether public surface: the latest version remains a curated reader-facing cleanup rather than a raw workbench dump. It contains cumulative reader PDFs, 43 standalone English paper PDFs, compact language/source ZIPs, the RA23 display-layout correction package, and the RA25-RA33 Paper 02 source-critical symbol/body/table audit packages. RA28 validates the Greek nu rebase for Paper 02 and protects genuine Latin-v contexts. RA29 closes the Paper 02 body pp.23-90 at the current page-level standard; RA30 adds the Paper 02 final-summary/table-plate audit package, fixing the p.90 final summary display, formula (31) tag placement, A4 landscape table plates, and selected Table II transvectant parentheses. RA31 source-checks Tabelle I on printed/source p.91 and corrects six cell-level issues. RA33 source-checks the top band of Tabelle II on printed/source p.92, rows 0-7. Tabelle II rows 8-23, final Paper 02 tag/layout inventory, and multilingual propagation remain open. This is not a certified critical edition; subtle formula, scan-reading, and cross-language synchronization errors may remain. Raw audit/witness bundles should be distilled into corrected TeX/PDF or concise public status notes before publication.",
    ],
    "albattani_opus_astronomicum": [
        "Work-level al-Battani record. The 251-page trilingual text reader, catalogue data, geography gazetteer, chronology layer, source witnesses, and workflow notes are useful working materials. Legacy filenames such as `Complete Critical Edition` for the fixed-star catalogue are not maintainer-certified critical-edition claims; read them as inherited data/workflow labels. The text and tables should continue to be checked against Nallino and the source witnesses for citation-critical use.",
    ],
    "non_european_consolidated": [
        "Consolidated multilingual record. Some inherited al-Battani file names still contain `Complete Critical Edition`; those names are not current critical-edition certification. Treat OCR, reconstructed tables, translations, and source-intake readers as working material unless the relevant work-level record gives a narrower promoted status.",
    ],
    "additional_author_cluster": [
        "Mixed selected-author shelf. Latest update adds `poincare_v1_25.zip`, a Poincare Tome I French/English working tranche for source witnesses v1_0345-v1_0370 / Chapter XIX, `Etude des courbes fermees`. This is explicitly not a continuous cumulative through v1_0370 because intervening v1_22/v1_23 artifacts were not locally available; the package includes a recovery branch built from the local cumulative base through v1_0284 plus v1_24 and v1_25. The next Poincare continuation is v1_0371, `Sur les series de polynomes`. `Kneser_LVR_p0206_0219_DE_EN_20260612.zip` remains the current Kneser source-witnessed continuation, and `Frobenius_all_GE_EN_cum_scans_QA03_20260611.zip` remains the selected Frobenius cumulative/QA package. Earlier Poincare/Frobenius/Kneser packets remain provenance/backstop where present. Bianchi, Gordan, Steinitz, Sylvester, Gibbs, and Maxwell now have preferred standalone records; their copies in mixed shelves remain backstop/provenance where present. Treat this shelf package by package, not as a blanket certification of every included author.",
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
        "**Quality warning:** This generated page lists public files and current record notes. It does not certify a critical edition. Legacy filenames can include terms such as `Complete`, `Strict`, `Source-Checked`, or `Critical`; use the status notes, source witnesses, and audit ledgers before relying on mathematical details.",
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
