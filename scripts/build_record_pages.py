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
    "kneser",
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
    "kneser": "Adolf Kneser",
    "additional_author_cluster": "Additional Author Cluster",
}

INDEX_DISPLAY_NAMES = {
    "cayley": "Arthur Cayley (suspect draft/provenance; not accuracy-certified)",
}

RECORD_NOTES = {
    "workflow": [
        "Latest workflow update 2026-06-24 adds the compact audit-harness snapshot for Noether, Weber, SGA6, and Steinitz, building on the 2026-06-12 source-audit/public-surface and object-level audit rules: reader-first latest records, source-image authority, derivative-PDF traps, OCR as locator rather than judge, page-map requirements, aid-package design, reliability labels, and the rule that diagram/table promotion needs a source object witness, output render witness, stable object ID, and explicit ledger verdict. The live workflow notes also record the SGA OCR lesson that Surya-style GPU OCR can be a stronger math/prose locator for French mathematical typescript than ordinary CPU OCR, while OCR from a mismatched source copy must not be used for page-precise claims without a source checksum and page map. Earlier workflow files document source/edition identity checks, structured repair worklists, high-DPI crop packets, local-to-web audit loops, Lean/Lake as a selective formal-checking companion, and GitHub/Zenodo publication hygiene.",
    ],
    "bianchi": [
        "Dedicated Bianchi working-edition record. Volume I of `Lezioni di geometria differenziale` is represented as a full source-pdfpage 001-543 Italian transcription and English translation working edition, with top-level reader PDFs, a source-scan witness PDF, and `95 Luigi Bianchi - Volume I Complete TeX Source Witnesses and Auditfix Package.zip` carrying the TeX, ledgers, render checks, and the post-completion auditfix pass. The A2 branch is separate and now has compact/core Italian-English working coverage through source p0135, with the public `Bianchi_A2_core_p0001_0135_IT_EN_20260613.zip` as the latest cataloged A2 package and earlier large scan-heavy p0105/repair packages retained as provenance/backstop. A smaller same-name Edge re-export has been routed locally under a disambiguated filename and is pending review/upload; it is not yet a public catalog replacement. These are working manuscript witnesses: TeX builds and renders, but matrix dots, prime marks, summation superscripts, and handwritten-symbol details still need continuing source/glyph audit. OCR/image-analysis material remains witness/locator evidence only.",
    ],
    "cayley": [
        "Accuracy warning 2026-06-09/12: this record is not a completed or proofed edition. A source comparison found substantial symbol/text mismatches in current Cayley Volume I material. Existing PDFs, TeX, indexes, and ZIPs are retained as provenance, salvage, and repair material, not as source-faithful transcription, unless a future page-by-page glyph/source audit explicitly re-promotes a specific range. The narrow `Cayley_V1_critical_p001_045_v2_20260609.zip` packet is the current promoted restart tranche for Volume I printed pp.1-58 / Papers 1-9 as a source-inspected working packet, not as a critical edition; v2 corrects the Paper 6 low-comma subscript notation and removes forced source-page whitespace. Do not infer reliability from inherited filenames: several older reader PDFs and ZIPs still contain phrases such as `Source-Checked`, but those labels are obsolete for Cayley unless the specific package is named in the promoted restart note above or in a later source-audit note. A later source-quality audit found that several Cayley repair lanes had been working from low-DPI Internet Archive derivative PDFs; future source-faithful repair should prefer the IA `_jp2.zip` master image archives and verified scan-page maps where available.",
    ],
    "gordan_clebsch_gordan": [
        "Current dedicated Gordan/Clebsch-Gordan record published as <https://doi.org/10.5281/zenodo.20822196> under concept DOI <https://doi.org/10.5281/zenodo.20616260>. The latest 2026-06-24 project-control update adds `Gordan_Project_Control_Status_20260624.zip`; the same public version also carries `Gordan_Theta_1863_FullAudit_fix06_20260623.zip`, `Gordan_Abelsche_FinalAuditFix02_DE_EN_20260613.zip`, `Gordan_de_linea_p025_047_final_LA_EN_scans_20260613.zip`, `Gordan_VB1_01_p001_009_DE_EN_20260613.zip`, and `Gordan_VB1_02_p010_028_DE_EN_20260613.zip`. This makes the FinalAuditFix02, De linea p001-p047, theta fix06, and Vorlesungen Bd.1 p001-p028 packets public. Earlier Abel tranches and AllPrior/AuditFix packets remain correction/provenance layers. These are source-witnessed working drafts and source-audit packets, not certified critical editions; OCR remains a locator/check layer and important formulas, diagrams, notation, and theorem statements must be checked against included source witnesses. The full Gordan article corpus register remains open, and Vorlesungen Bd.1 is only begun through source p28.",
    ],
    "steinitz": [
        "Dedicated Steinitz working-edition split from the mixed additional-author shelf. Latest public version <https://doi.org/10.5281/zenodo.20822189> adds `Steinitz_Project_Control_Status_20260624.zip`, a compact project-control/status package distilled from larger local project-upload bricks; it is a control/status update, not a new critical-edition certification. This record includes current package-audited German/English packets for 1910 fields sections 1-24, 1913 Bedingt I complete, strict early works from 1894/1897/1906, 1914 Bedingt II complete, and the first 1916 Bedingt III tranche through pp.1-13. These are source-witnessed working drafts, not final critical editions; OCR layers are locator/check aids only.",
    ],
    "frobenius": [
        'Dedicated Frobenius split from the mixed additional-author shelf. The current public surface includes the initial `Frobenius_all_GE_EN_cum_scans_QA03_20260611.zip` package and the 2026-06-24 RA05 refresh `Frobenius_all_GE_EN_cum_scans_RA05_20260613.zip`, plus top-level German/English cumulative PDF/TeX readers. The selected group-character sequence covers items 053, 054, 056, 057, 058, 059, 060, 061, 070, and 071, with 10/10 selected items, 221/221 tracked source-intake pages, 241 cumulative source-scan pages, German cumulative reader of 182 generated pages, and English cumulative reader of 176 generated pages. RA05 reports English item 070 formula-punctuation fixes, directly compilable all-author cumulative TeX/PDF replacing previous source-archive concatenations, verified ZIP extraction, zero German/English structural flags, zero post-fix formula-number skeleton mismatches, and zero fatal build/layout diagnostics. This is a source-witnessed working-draft package, not a certified critical edition; OCR/text extraction is a locator and comparison aid only.',
    ],
    "poincare": [
        "Dedicated Poincare split from the mixed additional-author shelf. The current public record publishes the available local `poincare_v1_*` working packages through `poincare_v1_26.zip`. The latest public package covers source witnesses v1_0371-v1_0384 top and reaches the close of Section I of `Sur les equations lineaires`, before Section II `Equations aux differences finies`. This is not a seamless continuous Tome I edition: the public record currently carries v1_01, v1_02, v1_08-v1_21, and v1_24-v1_26. A 2026-06-25 Edge-download sweep recovered local but not-yet-public `poincare_v1_03.zip`, `poincare_v1_04.zip`, `poincare_v1_05.zip`, and `poincare_v1_07.zip`; `poincare_v1_06.zip` and v1_22-v1_23 remain absent by this sweep. Use package by package, not as blanket certification.",
    ],
    "kneser": [
        "Dedicated Kneser working-edition split from the mixed additional-author shelf. Current public coverage fronts German-source and English working-translation reader PDF/TeX surfaces through p0011-p0248, a high-quality source witness through p0001-p0248, and the p0234 lower-p0248 slice/audit package. The included worklist reports 248/336 source pages done (73.8 percent), latest slice sections 53-55 completing the Sixth Section, and next continuation at p0249 / Seventh Section / section 56. This is a source-witnessed working draft and audit/progress record, not a certified critical edition.",
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
        "Dedicated Maxwell working-tranche split. Current coverage is A Treatise on Electricity and Magnetism, Volume I: IA 1873 first-edition source-witnessed working sequence pp.001-079, or 79/467 source-map pages (16.9 percent), plus earlier ledger-backed source-witnessed working tranches for book pages 95-101, 103, 105, 109, and the main continuous run 111-267. The included broader batch TeX/PDF substrate is status-mixed; promoted range claims are governed by ledgers and source witness images. OCR/XML witnesses are locator/provenance aids, not textual authority. This is not a complete Maxwell Treatise or final critical edition. Printed p.080 / IA leaf 118 is the next continuation point for the compact IA-first-edition sequence.",
    ],
    "gibbs_old_physics": [
        "Dedicated Gibbs / old-physics working-edition split. Current coverage is The Scientific Papers of J. Willard Gibbs, Volume I, printed pp.001-134: Graphical Methods in the Thermodynamics of Fluids, A Method of Geometrical Representation by Surfaces, and the opening continuation of On the Equilibrium of Heterogeneous Substances. Top-level PDF/TeX files are reader-facing cumulative surfaces, including the updated Paper 3 pp.055-134 reader; ZIP packets preserve source-scan slices, TeX, and method/audit notes. This is a source-scan-backed working tranche, not a complete Gibbs corpus or final critical edition. Continue after p.134.",
    ],
    "sga": [
        "Current caveat from the 2026-06-24 SGA audit-support updates: the latest published record is DOI `10.5281/zenodo.20822648`. SGA5 is explicitly not complete and should be assumed to contain many remaining errors unless a later, narrower source-audit packet promotes a specific locus. The public surface carries `SGA5_repair032_audit_support_20260624.zip` plus later local workpass evidence. The live SGA5 workpass reports 411 verified corrections, pdflatex exit 0, 0 errors, and a 307-page French workpass; the careful p375-p484 back-third pass is complete (Expose X/XII/XV plus index), and the front-grind now reaches printed p202 after manual p75-p101 and workflow p102-p202, with cursor at p203. Open areas still include p1-p74, p203-p374, remaining heavy-QA/uncertain/type-B items, and English synchronization. This is preservation/support evidence for ongoing repair, not a certified edition, not English synchronization, and not closure of diagram/formula/notation/typography queues. Treat SGA6 and SGA7 as substantial working drafts with explicit compression caveats unless a specific packet declares source-checked coverage. Older filenames containing words such as `Complete`, `Source-Checked`, `Strict`, or `High-Fidelity` are legacy package names, not current global certification. Witness-aid ZIPs are source-witness/anchor aids, not authority by themselves.",
    ],
    "weber": [
        "Current Weber public surface: latest public version is record 20837104 / DOI 10.5281/zenodo.20837104 under the permanent concept DOI 10.5281/zenodo.20412153. Volume I is represented as a repaired/source-scan-audited working edition; Volume II has current German/English cumulative reader material through section 176 plus localized recursive repairs/ledgers; Volume III remains the current repaired cumulative from the earlier baseline. Batch137 is now public and supersedes the public Batch132 ledger status: it reports scan-reviewed no-change closures for Volume I sections 120, 122, 128, 145, 148, 149, 150, 156, 158, 162, 163, 168, 169, 173, 174, 175, 176, 179, 180, 181, 182, and 183, with the active 112-row ledger at 112/112 closed. Batch138 is public as a focused Volume II section 6 control-character footnote fix. B139 is public as a focused Volume II English section 49 merged-tag repair and recursive range-tag scan rule. These are working/source-witnessed repair-ledger packages, not certified critical editions; Batch137's Volume II patch candidates remain candidate evidence unless later integrated. OCR and display ledgers are omission guards and locator layers, not independent authority.",
    ],
    "noether": [
        'Current Noether public surface: latest published Zenodo version is record 20836874 / DOI 10.5281/zenodo.20836874. It carries forward the curated reader/source-audit surface and adds file 119, `119 Noether - PostR124 Survival Rollup NoNewPatch Audit 2026-06-24.zip`, as a compact post-R124 survival/no-new-patch rollup. These files are working/source-audit/provenance packages only: not promoted critical editions, not whole-corpus mathematical certification, not downstream multilingual synchronization proof, and not final high-resolution certification. Earlier R124-plus repair packages, P34/P40 hotspot dispositions, source-audit addenda, and survival clusters remain provenance layers; they are not blanket certification. Ukrainian/Russian/Interslavic material remains work-so-far translation/linguistics apparatus. Record 20836874 supersedes 20836432 as the current public Noether version, and the record is now at the Zenodo 100-file ceiling.',
        'Corrections, source comparisons, LaTeX fixes, and translation improvements can be suggested through GitHub issues or pull requests: <https://github.com/KokunoYumeto/modern-latex-manuscripts>. For citation-critical use, verify formulas, tables, theorem statements, diagrams, apparatus notes, and unusual notation against the included source witnesses and current audit ledgers.',
    ],
    "albattani_opus_astronomicum": [
        "Work-level al-Battani record. The 251-page trilingual text reader, catalogue data, geography gazetteer, chronology layer, source witnesses, and workflow notes are useful working materials. Legacy filenames such as `Complete Critical Edition` for the fixed-star catalogue are not maintainer-certified critical-edition claims; read them as inherited data/workflow labels. The text and tables should continue to be checked against Nallino and the source witnesses for citation-critical use.",
    ],
    "non_european_consolidated": [
        "Consolidated multilingual record. Some inherited al-Battani file names still contain `Complete Critical Edition`; those names are not current critical-edition certification. Treat OCR, reconstructed tables, translations, and source-intake readers as working material unless the relevant work-level record gives a narrower promoted status.",
    ],
    "additional_author_cluster": [
        "Mixed selected-author shelf. This remains a backstop/provenance shelf for authors not yet split into full standalone records and for older routed packets. Kneser now has a preferred standalone record at concept DOI `10.5281/zenodo.20836971`; earlier Kneser packets here remain provenance/backstop where present. Bianchi, Gordan, Steinitz, Sylvester, Gibbs, Maxwell, Poincare, Frobenius, and Kneser now have preferred standalone records. Treat this shelf package by package, not as a blanket certification of every included author.",
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
