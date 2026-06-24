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
import json
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
    "riemann",
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
    "frobenius",
    "poincare",
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
    "riemann": "Bernhard Riemann",
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
    "frobenius": "Ferdinand Georg Frobenius",
    "poincare": "Henri Poincare",
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
        "Dedicated Bianchi working-edition record. Volume I of `Lezioni di geometria differenziale` is represented as a full source-pdfpage 001-543 Italian transcription and English translation working edition, with top-level reader PDFs, a source-scan witness PDF, and `95 Luigi Bianchi - Volume I Complete TeX Source Witnesses and Auditfix Package.zip` carrying the TeX, ledgers, render checks, and the post-completion auditfix pass. The A2 branch is separate and now has compact/core Italian-English working coverage through source p0135, with the public `Bianchi_A2_core_p0001_0135_IT_EN_20260613.zip` as the latest cataloged A2 package and earlier large scan-heavy p0105/repair packages retained as provenance/backstop. A smaller same-name Edge re-export has been routed locally under a disambiguated filename and is pending review/upload; it is not yet a public catalog replacement. These are working manuscript witnesses: TeX builds and renders, but matrix dots, prime marks, summation superscripts, and handwritten-symbol details still need continuing source/glyph audit. OCR/image-analysis material remains witness/locator evidence only.",
    ],
    "cayley": [
        "Accuracy warning 2026-06-09/12: this record is not a completed or proofed edition. A source comparison found substantial symbol/text mismatches in current Cayley Volume I material. Existing PDFs, TeX, indexes, and ZIPs are retained as provenance, salvage, and repair material, not as source-faithful transcription, unless a future page-by-page glyph/source audit explicitly re-promotes a specific range. The narrow `Cayley_V1_critical_p001_045_v2_20260609.zip` packet is the current promoted restart tranche for Volume I printed pp.1-45 / Papers 1-9 as a source-inspected working packet, not as a critical edition; v2 corrects the Paper 6 low-comma subscript notation and removes forced source-page whitespace. Do not infer reliability from inherited filenames: several older reader PDFs and ZIPs still contain phrases such as `Source-Checked`, but those labels are obsolete for Cayley unless the specific package is named in the promoted restart note above or in a later source-audit note. A later source-quality audit found that several Cayley repair lanes had been working from low-DPI Internet Archive derivative PDFs; future source-faithful repair should prefer the IA `_jp2.zip` master image archives and verified scan-page maps where available.",
    ],
    "gordan_clebsch_gordan": [
        "Dedicated Gordan / Clebsch-Gordan working-edition split from the mixed additional-author shelf. The current published Abelsche continuation includes `Gordan_Abel27_p343_355_DE_EN_20260612.zip`, covering source pp.343-355 / printed pp.321-333 and cumulative German/English TeX/PDF through source p355. It completes sections 91-93 and the authorial text of `Theorie der Abelschen Functionen`; source pp.356-362 are retained as blank/end/cover scan witnesses only. Local staging 2026-06-13 has `Gordan_Abelsche_FinalAuditFix02_DE_EN_20260613.zip` queued for upload: package notes report a final recursive audit/fix for the same Abelsche ending and a section 91 notation-family correction from `n_k^{(h)}` to source-visible `w_k^{(h)}` in the composed-period family. Local staging also has `Gordan_de_linea_p025_047_final_LA_EN_scans_20260613.zip` queued for upload: package notes report `De linea geodetica` p001-p047 represented in cumulative Latin/English TeX/PDF, with the final p025-p047 tranche completing Capita V-IX, Vita, and Theses. The newest local staging package `Gordan_VB1_01_p001_009_DE_EN_20260613.zip` starts Gordan's `Vorlesungen ueber Invariantentheorie`, Bd. 1, `Determinanten`: title page, Hermite dedication, and full Vorwort are transcribed/translated from GDZ/SUB Goettingen 600ppi source witnesses 0001-0009; duplicate title, stamp, and blank pages remain scan-only witnesses. Scans and zoom crops control formula readings; OCR prose witnesses remain noncanonical gap detectors. These are package-audited, source-witnessed working drafts, not final critical editions.",
        "Local staging update 2026-06-13: `Gordan_VB1_02_p010_028_DE_EN_20260613.zip` is also queued for upload. It continues `Vorlesungen ueber Invariantentheorie` Bd. 1 from source TIFF witnesses 0010-0028, covering contents pages VIII-XI, one blank scan-only page, and printed pp.1-14 through section 1 paragraphs 1-12, with current/cumulative German/English TeX/PDF, GDZ 600ppi witnesses, render checks, and no reported red flags. It is not yet a public Zenodo file until upload succeeds.",
    ],
    "steinitz": [
        "Dedicated Steinitz working-edition split from the mixed additional-author shelf. This record includes current package-audited German/English packets for 1910 fields sections 1-24, 1913 Bedingt I complete, strict early works from 1894/1897/1906, 1914 Bedingt II complete, and the first 1916 Bedingt III tranche through pp.1-13. These are source-witnessed working drafts, not final critical editions; OCR layers are locator/check aids only.",
    ],
    "frobenius": [
        "Dedicated Frobenius split from the mixed additional-author shelf. The initial public package is `Frobenius_all_GE_EN_cum_scans_QA03_20260611.zip`, a German/English selected group-character cumulative with package status reporting completed items 10/10, tracked source-intake pages 221/221, German all-author cumulative 182 generated pages, English all-author cumulative 176 generated pages, and 241 cumulative source-scan pages merged. Local staging 2026-06-13 has `Frobenius_all_GE_EN_cum_scans_RA05_20260613.zip` queued for upload: package notes report English item 070 formula-punctuation fixes, directly compilable all-author cumulative TeX/PDF replacing previous source-archive concatenations, verified ZIP extraction, 221/221 aid source page images present, zero German/English structural flags, zero post-fix `\\fnum` skeleton mismatches, and zero fatal build/layout diagnostics. This is a source-witnessed working-draft package, not a certified critical edition; OCR/text extraction is a locator and comparison aid only.",
    ],
    "poincare": [
        "Dedicated Poincare split from the mixed additional-author shelf. The record publishes the currently available local `poincare_v1_*` working packages through `poincare_v1_26.zip`. The latest package covers source witnesses v1_0371-v1_0384 top and reaches the close of Section I of `Sur les equations lineaires`, before Section II `Equations aux differences finies`. This is not a seamless continuous Tome I edition: local artifacts currently include v1_01, v1_02, v1_08-v1_21, and v1_24-v1_26; v1_03-v1_07 and v1_22-v1_23 are not currently present as local package artifacts. Use package by package, not as blanket certification.",
    ],
    "riemann": [
        "Dedicated Riemann author record. The current surface has two reader PDFs, one selected-papers reader and one broader Gesammelte Werke complete-draft reader, plus matching artifact ZIPs with TeX/source/provenance material. These are machine-assisted working drafts for checking and continuation, not proofread critical editions.",
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
        "Current caveat from the 2026-06-24 SGA repair032 audit-support update: the latest published record is DOI `10.5281/zenodo.20821507`, which adds `SGA5_repair032_audit_support_20260624.zip`. SGA5 is explicitly not complete and should be assumed to contain many remaining errors unless a later, narrower source-audit packet promotes a specific locus. Repair032 is preservation/support evidence for ongoing SGA5 repair, not a certified edition, not English synchronization, and not closure of diagram/formula/notation/typography queues. The SGA record remains at the 100-file ceiling; this version removed obsolete `sga_repair019_public_summary.json` to add the bundle. Treat SGA6 and SGA7 as substantial working drafts with explicit compression caveats unless a specific packet declares source-checked coverage. Older filenames containing words such as `Complete`, `Source-Checked`, `Strict`, or `High-Fidelity` are legacy package names, not current global certification. Witness-aid ZIPs are source-witness/anchor aids, not authority by themselves.",
    ],
    "weber": [
        "Current Weber public surface: Volume I is represented as a repaired/source-scan-audited working edition; Volume II has current German/English cumulative reader material plus localized recursive repairs/ledgers. Batch132 is the latest public recursive gap-repair package, covering Volume II sections 120 and 128; its status reports the active 112-row repair ledger at 73 closed / 39 open and Tier-3 rows 11/11 closed. Local staging 2026-06-13 has Batch136 queued for Zenodo upload: Volume I sections 56, 63, 64, 68, 70, 73, 78, 89, 100, and 113 reviewed as scan-reviewed no-change source closures, with the working ledger estimate at 101/112 closed and 11/112 open. Batch136 is not yet in the public file catalog. Earlier pending Batch134 remains a previous no-change closure packet. Volume III remains the current repaired cumulative from the earlier baseline. OCR and display ledgers are omission guards and locator layers, not independent authority; continuation ranges remain working drafts unless the package declares source-checked coverage.",
    ],
    "noether": [
        'Current Noether public surface: latest published Zenodo version is record 20821592 / DOI 10.5281/zenodo.20821592. It carries forward the R120/R121/R122 curated reader/source-audit surface, the four targeted R122 source-audit candidate ZIPs published in record 20821409, and now adds `Noether_R122_20260623.zip` as the consolidated R122 German source-queue/cumulative working package. The consolidated package reports Papers 32-33 source-audit work closed in that branch and identifies Paper 34 as the next high-fidelity sequential target. These files are working/source-audit/provenance packages only, not promoted critical editions, not whole-corpus mathematical certification, and not multilingual propagation. Earlier targeted caveats still apply: Paper 13 pp.239-257 remain explicitly unchecked in the P16P13 drop; P16 uses best staged local witnesses with ambiguous DPI metadata; P20/P39 are targeted page ranges. Final Paper 02 tag/layout inventory, branch reconciliation, downstream language synchronization, and unresolved low-resolution/best-source queues remain open.',
        'Corrections, source comparisons, LaTeX fixes, and translation improvements can be suggested through GitHub issues or pull requests: <https://github.com/KokunoYumeto/modern-latex-manuscripts>. For citation-critical use, verify formulas, tables, theorem statements, diagrams, apparatus notes, and unusual notation against the included source witnesses and current audit ledgers.',
    ],
    "albattani_opus_astronomicum": [
        "Work-level al-Battani record. The 251-page trilingual text reader, catalogue data, geography gazetteer, chronology layer, source witnesses, and workflow notes are useful working materials. Legacy filenames such as `Complete Critical Edition` for the fixed-star catalogue are not maintainer-certified critical-edition claims; read them as inherited data/workflow labels. The text and tables should continue to be checked against Nallino and the source witnesses for citation-critical use.",
    ],
    "non_european_consolidated": [
        "Consolidated multilingual record. Some inherited al-Battani file names still contain `Complete Critical Edition`; those names are not current critical-edition certification. Treat OCR, reconstructed tables, translations, and source-intake readers as working material unless the relevant work-level record gives a narrower promoted status.",
    ],
    "additional_author_cluster": [
        "Mixed selected-author shelf. This remains a backstop/provenance shelf for authors not yet split into full standalone records and for older routed packets. Poincare and Frobenius now have preferred standalone records; earlier Poincare/Frobenius/Kneser packets here remain provenance/backstop where present. `Kneser_LVR_p0206_0219_DE_EN_20260612.zip` remains the current published Kneser source-witnessed continuation in this mixed shelf. Local staging 2026-06-13 has `Kneser_LVR_p0234_0248_DE_EN_20260613.zip` queued for upload, covering p0234 lower-p0248 / sections 53-55 and reporting 248/336 source pages done (73.8%), with next start p0249 / Seventh Section / section 56. Bianchi, Gordan, Steinitz, Sylvester, Gibbs, Maxwell, Poincare, and Frobenius now have preferred standalone records. Treat this shelf package by package, not as a blanket certification of every included author.",
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


def load_concept_urls(root: Path) -> dict[str, str]:
    map_path = root / "manifests" / "zenodo-record-concept-doi-map.json"
    if not map_path.exists():
        return {}

    try:
        records = json.loads(map_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}

    urls: dict[str, str] = {}
    for record in records:
        record_id = str(record.get("id", "")).strip()
        concept_url = str(record.get("concepturl", "")).strip()
        if record_id and concept_url:
            urls[record_id] = concept_url
    return urls


def write_record_page(label: str, rows: list[dict[str, str]], out_dir: Path, concept_urls: dict[str, str]) -> None:
    display = DISPLAY_NAMES.get(label, label.replace("_", " ").title())
    title = rows[0]["record_title"]
    record_id = rows[0]["record_id"]
    url = concept_urls.get(record_id, f"https://zenodo.org/records/{record_id}")
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
    record_notes = RECORD_NOTES.get(label, [])
    for note in record_notes:
        lines.extend([note, ""])
    if not any("GitHub issues or pull requests" in note for note in record_notes):
        lines.extend(
            [
                "Corrections, source comparisons, LaTeX fixes, and translation improvements can be suggested through GitHub issues or pull requests: <https://github.com/KokunoYumeto/modern-latex-manuscripts>.",
                "",
            ]
        )
    lines.extend(
        [
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


def write_index(grouped: dict[str, list[dict[str, str]]], out_dir: Path, concept_urls: dict[str, str]) -> None:
    lines = [
        "# Record Landing Pages",
        "",
        "These pages are generated from `manifests/public-file-catalog.csv` and group each public Zenodo record into reader PDFs, artifact ZIPs, and manifest/status files. This index uses compact browse labels; each linked record page gives the full public Zenodo title and current quality/status notes.",
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
        url = concept_urls.get(record_id, f"https://zenodo.org/records/{record_id}")
        lines.append(
            f"| {display} | {len(rows)} | {len(pdfs)} | {len(zips)} | {size_sum(rows):.1f} | [{page}]({page}) | [Zenodo]({url}) |"
        )
    lines.append("")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "README.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    root = Path.cwd()
    rows = read_rows(root / "manifests" / "public-file-catalog.csv")
    concept_urls = load_concept_urls(root)
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[row["record_label"]].append(row)

    out_dir = root / "docs" / "records"
    for label in RECORD_ORDER:
        if label in grouped:
            write_record_page(label, grouped[label], out_dir, concept_urls)
    write_index(grouped, out_dir, concept_urls)
    print(f"Wrote {len(grouped)} record landing pages to {out_dir}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
