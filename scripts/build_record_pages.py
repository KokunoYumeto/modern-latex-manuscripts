#!/usr/bin/env python3
"""Build per-record Markdown landing pages from the public file catalog.

Run from the repository root after `manifests/public-file-catalog.csv` exists:

    python scripts/build_record_pages.py

Outputs:
    docs/records/README.md
    docs/records/<record_label>.md, when missing

Existing individual record pages can contain hand-maintained status notes that
are richer than the generator's compact notes. By default this script preserves
those pages and only refreshes the index plus missing pages. Use
`--overwrite-record-pages` only when a full regeneration is intentional.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import re
from collections import defaultdict
from pathlib import Path


RECORD_TIERS = [
    (
        "Project infrastructure and public entry points",
        [
            "main",
            "workflow",
            "interlanguage_reflections",
            "lean_formalization_sidecars",
        ],
    ),
    (
        "Separate mathematics research sidecar",
        [
            "split_zero_research_sidecar",
        ],
    ),
    (
        "Best current reader/translation surfaces",
        [
            "noether",
            "weber",
            "frobenius",
            "kneser",
            "sylvester",
            "albattani_opus_astronomicum",
        ],
    ),
    (
        "Serious source-aware work, with caveats",
        [
            "sga",
            "deligne",
            "bianchi",
            "gordan_clebsch_gordan",
            "steinitz",
            "maxwell",
            "gibbs_old_physics",
            "ukrainian_applied_math",
            "non_european_consolidated",
            "chinese",
            "indian_sanskrit",
            "islamic_arabic",
            "historical_references",
        ],
    ),
    (
        "Partial or non-continuous author workstreams",
        [
            "dedekind",
            "dirichlet",
            "gauss",
            "riemann",
            "poincare",
            "classical_algebra_arithmetic",
            "additional_author_cluster",
        ],
    ),
    (
        "OCR/support/provenance or currently unsafe draft lanes",
        [
            "ega",
            "cayley",
        ],
    ),
]

RECORD_ORDER = [label for _, labels in RECORD_TIERS for label in labels]


DISPLAY_NAMES = {
    "main": "Main Project Landing",
    "workflow": "Workflow / Replication Packet",
    "interlanguage_reflections": "Interlanguage Methodology",
    "lean_formalization_sidecars": "Lean Formalization Sidecars",
    "split_zero_research_sidecar": "Split-Zero Geometry and Common Deformation Registers",
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
    "ega": "EGA (French originals + OCR/support + partial translation draft)",
    "sga": "SGA (serious active work; not complete)",
}

RECORD_NOTES = {
    "workflow": [
        "Current workflow version 21300795 describes the actual AI-run pipeline: source identity and page maps, local GPU OCR/VLM as witness layers, page-unit TeX reconstruction, local-to-web review handoffs, deterministic repair, compile/render gates, conservative public labels, and reader-first GitHub/Zenodo publication. The July 10 SGA6 lesson is explicit: compile-clean scaffolds can contain whole-page compression, omitted proofs, invented statements, wrong relations, notation drift, and unsupported equation tags. Mathematical objects and tags must be verified individually against source witnesses; OCR, VLM, agent output, and compile logs do not certify an edition.",
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
    "lean_formalization_sidecars": [
        "Small Lean 4 / Mathlib-style sidecar package for useful formal mathematics connected to Noether, Steinitz, Weber, and Jordan. This is library-candidate/formalization material with build logs and toolchain metadata. It is not proof that any scanned edition or translation is source-faithful, not source-fidelity evidence, not translation certification, and not critical-edition material.",
    ],
    "interlanguage_reflections": [
        "Methodology, source-body, and provenance sidecar for interlanguage and constructed-language mathematical translation. Current public version 21422899 fronts the v0.11 methodology map, retains the Romance v10, Interslavic v0.6, source-body, automata, and provenance layers, and adds the Noether R823 completion gate v4. The Spanish replay passes all 35 declared checks against the exact 473-page candidate, with 81 source-reconciled units, 68 independent hash-pinned native Spanish TeX witnesses, a readable final audit, and a candidate-derived pixel-bound render baseline. This gate certifies declared artifact/evidence/build/render bindings; it is not native-language approval, semantic perfection, mathematical proof checking, peer review, or a critical edition. French remains active. The actual Noether reader remains on record 21422620.",
    ],
    "split_zero_research_sidecar": [
        "Separate exploratory mathematics record, not part of the manuscript-translation completion ranking. Version 21421058 fronts a human-readable Project Atlas and a 195-page bookmarked results compendium, with exact Lean/Python checks and ledgers, editable working texts, visualizations, scene data, and replay/QA material. A release-level reference-closure gate includes every generated result named by the public atlas, including the restored Packet 076 dependency and Packets 198-202. The record is not peer review, not a proof of a famous open problem, and not certification of every broader claim.",
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
        "Current public SGA surface is corrective record 21422245. It fronts the 309-page source-aware English SGA5 working translation and directly exposes the corrected 381-page SGA6 full-range layered English working reader covering the full extant source scan. This version restores Lemma 5.8.2 footnote 14, absent from historical version 21421931. The SGA6 reader has three declared authority layers: source-PDF 001-525 is inherited and partially synchronized; idx532-662 is synchronized against the directly checked French workpass; and idx663-702 plus terminal back matter is scan-checked English draft material pending later French reconciliation. Its grouped package contains editable TeX, authority/formula/terminology/page ledgers, build evidence, all-page renders, contact sheets, prefix-repair and correction evidence, hashes, and validation. The record also retains the French SGA5 and French SGA6 idx662 workpasses and the bounded four-page Spanish SGA6 Expose X idx532-537 tranche. These are substantive machine-assisted source-aware working translations and repairs, not independently human-certified critical editions, uniform whole-volume source certification, or whole-SGA completion.",
    ],
    "weber": [
        "Current Weber public surface: latest public version is record 21402223 / DOI 10.5281/zenodo.21402223 under the permanent concept DOI 10.5281/zenodo.20412153. The active Volume I German p1-p99 direct content-fidelity pass reaches printed p88, with p89 next; the p77-p88 package includes the current TeX/PDF, exact diff, ledgers, twelve source pages, high-resolution crops, render checks, and checksums. It rebuilds the damaged section 23 and restores omitted displays, rows, proof text, labels, and notation. The Volume I English reader predates these German repairs and is explicitly unsynchronized. Volume II retains current German/English cumulative material through section 176 plus localized recursive repairs/ledgers; Volume III remains the current repaired cumulative. Historical Batch137/B138/B139 packets remain provenance and repair evidence. These are working/source-witnessed drafts and repair-ledger packages, not whole-volume symbol-by-symbol certification or critical editions; OCR and display ledgers are omission guards and locator layers, not independent authority.",
    ],
    "noether": [
        'Current Noether public surface: latest published Zenodo version is record 21422620 / DOI 10.5281/zenodo.21422620 under concept DOI 10.5281/zenodo.20412587. It retains the 466-page v26/R823 German source-control reader as default preview; directly exposes the 473-page Spanish and 529-page Latin / 552-page Cyrillic Interslavic working readers; fronts a complete-work Indonesian Paper 36 working translation; and directly exposes complete Papers 26 and 36 in Simplified Chinese, generic Traditional Chinese, Japanese, and Korean. File `12_Noether_Arabic_Persian_Indonesian_WorkingComponents_20260718.zip` carries Indonesian TeX/evidence plus bounded Arabic and Iranian-Persian Paper 06 openings. File `11` retains all 442 Interslavic TeX bodies and individual PDFs; file `10` retains Spanish TeX/evidence; file `09` retains twelve bounded R823-synchronized English components plus exact CJK TeX/audit evidence and Slavic components. Paper 06 remains partial in Arabic/Persian; the eight CJK PDFs passed technical gates but lack external native review. These are working translations and source-control evidence: not a critical edition, universal mathematical source certification, complete multilingual synchronization, or final linguistic approval.',
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
    record_url = f"https://zenodo.org/records/{record_id}"
    concept_url = concept_urls.get(record_id)
    pdfs = [row for row in rows if row["filename"].lower().endswith(".pdf")]
    zips = [row for row in rows if row["filename"].lower().endswith(".zip")]
    manifests = role_rows(rows, "manifest/status")
    reader_pdfs = role_rows(rows, "reader/reference PDF")
    other_pdfs = [row for row in pdfs if row not in reader_pdfs]

    if reader_pdfs:
        how_to_read = "Open the reader/reference PDFs first. Use artifact ZIPs when you need TeX, source witnesses, OCR, page images, render checks, or provenance material."
    else:
        how_to_read = "This record has no top-level reader PDFs in the current file surface. Open the artifact ZIPs for TeX, component PDFs, source witnesses, OCR, page images, render checks, and provenance material."

    zenodo_line = f"Zenodo record: [{record_id}]({record_url})"
    if concept_url:
        zenodo_line += f"; concept DOI: [{concept_url}]({concept_url})"

    lines = [
        f"# {display}",
        "",
        zenodo_line,
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
        "These pages are generated from `manifests/public-file-catalog.csv` and group each public Zenodo record into reader PDFs, artifact ZIPs, and manifest/status files. This index is ordered by current reader usefulness and source-audit confidence, not by file count, storage size, or aspirational project importance. Each linked record page gives the full public Zenodo title and current quality/status notes.",
        "",
        "| Record | Files | PDFs | ZIPs | MB | Page | Zenodo |",
        "|---|---:|---:|---:|---:|---|---|",
    ]
    for tier, labels in RECORD_TIERS:
        present = [label for label in labels if grouped.get(label)]
        if not present:
            continue
        lines.append(f"| **{tier}** |  |  |  |  |  |  |")
        for label in present:
            rows = grouped[label]
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
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--overwrite-record-pages",
        action="store_true",
        help="Rewrite existing docs/records/<record>.md pages. Default preserves them.",
    )
    args = parser.parse_args()

    root = Path.cwd()
    rows = read_rows(root / "manifests" / "public-file-catalog.csv")
    concept_urls = load_concept_urls(root)
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[row["record_label"]].append(row)

    out_dir = root / "docs" / "records"
    for label in RECORD_ORDER:
        if label in grouped:
            target = out_dir / f"{slug(label)}.md"
            if args.overwrite_record_pages or not target.exists():
                write_record_page(label, grouped[label], out_dir, concept_urls)
    write_index(grouped, out_dir, concept_urls)
    print(f"Wrote {len(grouped)} record landing pages to {out_dir}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
