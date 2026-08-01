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
        "Reusable source-audit image worksets",
        [
            "visual_evidence",
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
            "ega",
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
            "serre",
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
            "cayley",
        ],
    ),
]

RECORD_ORDER = [label for _, labels in RECORD_TIERS for label in labels]


DISPLAY_NAMES = {
    "main": "Main Project Landing",
    "workflow": "Workflow / Replication Packet",
    "visual_evidence": "SGA / EGA Source-Audit Image Worksets",
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
    "serre": "Jean-Pierre Serre",
    "additional_author_cluster": "Additional Author Cluster",
}

INDEX_DISPLAY_NAMES = {
    "cayley": "Arthur Cayley (suspect draft/provenance; not accuracy-certified)",
    "ega": "EGA (current complete-scope working readers)",
    "sga": "SGA (current working readers; SGA7 II partial)",
}

RECORD_NOTES = {
    "workflow": [
        "Current workflow version 21707334 publishes a compact eleven-file methodology surface. The corrected seven-page A4 workflow PDF remains the default preview, with the exact Markdown, Claude high-resolution source method, resource-efficiency incident note, controlling SGA3 diagram-fidelity correction, seven-member source packet, and retained July 6 addenda. It adds one exact ChatGPT export of dated July 11-27 research-methodology briefings, explicitly labeled generated and unverified; claims and citations require primary-source checking. User-supplied OCR remains read-only locator/drafting evidence and must not be regenerated. Existing 600/1200-dpi evidence remains valid history and context; only 300-dpi-only approvals and independently found material defects are reopened. New final SGA3 diagram successors use native editable TeX, 300-dpi page context, about 5000-dpi default comparison, targeted 9000-dpi ambiguity crops, disjoint ownership, and lead-signed evidence. Raster authority witnesses remain private. The emissions discussion is scenario analysis, not metered OpenAI telemetry. These are methodology, accountability, and research-note materials, not edition or translation certification.",
    ],
    "visual_evidence": [
        "Dedicated compute-reuse dataset for provenance-bound high-detail source crops used during SGA and EGA transcription checks. The initial version contains 5,855 recovered SGA7 I targeted crops in two image archives plus one metadata archive. It is source-audit evidence, not a reader, translation, critical edition, mathematical certification, or blanket rights determination. Reader landing pages remain separate and reader-first.",
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
    "serre": [
        "Dedicated Serre working-transcription record. FAC is directly readable as a complete 63-page French working transcription covering all 82 source pages / printed pp.197-278. The direct master and body TeX accompany one compact 27-member FAC source/evidence ZIP containing the complete editable closure, exact ledgers, and four actual scan-derived crops with page, rasterization, bounding-box, dimension, and hash provenance. A separate eight-member ZIP preserves the complete first-pass GAGA TeX source for printed pp.1-42; its earlier PDF remains held because visible join sentinels are still present. License metadata is License Not Specified. This is working-transcription custody, not a complete Serre corpus, critical edition, mathematical certification, accessibility certification, or blanket rights clearance.",
    ],
    "lean_formalization_sidecars": [
        "Small Lean 4 / Mathlib-style sidecar package for useful formal mathematics connected to Noether, Steinitz, Weber, and Jordan. This is library-candidate/formalization material with build logs and toolchain metadata. It is not proof that any scanned edition or translation is source-faithful, not source-fidelity evidence, not translation certification, and not critical-edition material.",
    ],
    "interlanguage_reflections": [
        "Methodology, source-body, provenance, corpus-control, and bounded-output sidecar for mathematical translation. Current version 21743417 retains the complete numbered archive, the Interslavic dictionary anchor, the Fable Tranche 001 acknowledgement, and the direct Gate 15 source anchor, then adds one compact commit-pinned Persian Noether-topic XeLaTeX source ZIP. The Persian packet closes a Noether-topic editable-source row only, not Persian invariant theory; GitHub reported no repository license. Paper 06 semantic reconciliation, linguistic review, global-ledger completeness, Persian invariant theory, Arabic invariant theory, Dari editable mathematics, and Tajik abstract-algebra/native-TeX source remain open. These are methodology, normalization, corpus, source-custody, bounded working-translation, provenance, and QA artifacts, not native validation, translation or source-fidelity certification, rights clearance, community certification, peer review, or critical editions.",
    ],
    "split_zero_research_sidecar": [
        "Separate exploratory mathematics record, not part of the manuscript-translation completion ranking. Current version 21443852 fronts the concise Project Atlas and retains the bookmarked results compendium, Lean/Python checks and ledgers, editable working texts, replayable visualization/data packages, and the bounded N16-N18 predatum/K4/Hopf supplement from predecessor 21426216. It adds the coherent Part 8-C2A through C2F2 finite-glue, shell, triality, and Fricke proof chain. The seven source-free Python replays pass 16/16, 19/19, 16/16, 18/18, 20/20, 11/11, and 19/19 checks; the stated marking, topology, classification, and Niemeier/Fricke boundaries remain explicit. This is a working research record, not peer review, a proof of a famous open problem, or certification of every broader claim.",
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
        "Current compact SGA record 21750586 leads with the SGA1-7 I English reader-and-TeX bundle, followed by direct readers and masters; SGA1 remains the default preview. The bundle contains current standalone readers and buildable TeX, not yet one cross-volume SGA 1-7.2 PDF. The clean 1,470-page SGA3 R29 cumulative covers the Introduction, Exposes I-XXVI, Tome-I subject index, Tome-III mathematical guide, and terminal index. SGA7 I has a complete 287-page English working reader for all written Exposes I, II, VI, VII, VIII, and IX. A direct 212-page SGA7 II English current-progress reader contains complete Exposes X-XIX and Expose XX through Section 4.3, with a 148-member reader/source ZIP. Two compact source-image ZIPs preserve 26 translated-scope images and 16 preparatory images; the latter make no translation claim. Expose XX Section 4.4 is next and Exposes XXI-XXII are absent. French working transcriptions remain separately available. Anonymous readback passed all 87 outer files, all 82 retained predecessor identities, all 148 reader/source members, both image-ZIP inventories (27 and 17 members), and all 18 release-control members. Historical versions remain immutable. These are working editions, translations, and transcriptions, not critical editions, rights determinations, mathematical certifications, exhaustive reference certifications, accessibility certifications, uniform whole-series source certification, or final whole-SGA certification. Record rights metadata remains License Not Specified.",
    ],
    "ega": [
        "Open the fronted 1,356-page linked EGA 0-IV reader for one continuous reading surface, or use the five direct standalone English readers. The leading bundle contains the global reader, all five standalone readers, and their complete buildable TeX closures. EGA 0 is complete through Section 13; EGA I and II through their authority EOFs; the published EGA III text through 7.9.14; and EGA IV through Sections 1-21 and EOF. Anonymous readback passed all 42 outer files and all 265 leading-bundle members. These are working translations, not critical editions, rights clearance, mathematical certification, accessibility certification, or a claim of uniform whole-corpus source certification.",
    ],
    "deligne": [
        "Current reader-first public surface is record 21212608. It exposes the sequential English and French working readers through Papers 001-016p080, groups individual paper and letter PDFs by language, and groups TeX/source-check/QA/update material separately. These are useful but uneven working drafts and source/QA packets, not a critical edition or blanket source-faithfulness claim; commutative diagrams, dense formulas, references, and theorem statements still require source comparison.",
    ],
    "chinese": [
        "Current public surface is record 20543246. English, modern-Chinese, Chinese-original, and Arabic working readers are directly available, with TeX/source artifacts grouped in ZIPs. The Arabic readers passed build/openability checks but remain working translation drafts without native-language or source-accuracy certification.",
    ],
    "indian_sanskrit": [
        "Current public surface is record 20435677. It exposes reader/index PDFs and a filtered TeX/source archive for the represented Indian and Sanskrit works. These are working original-language and English translation drafts, not proofed critical editions.",
    ],
    "islamic_arabic": [
        "Current public surface is record 20435687. It exposes reader/index PDFs, original/reference surfaces, English working translations, and a filtered TeX/source archive. These are working drafts and reference witnesses, not proofed critical editions.",
    ],
    "historical_references": [
        "Current public surface is record 20435690. It is a focused historical-reference shelf with reader PDFs and filtered TeX/source material for terminology and historical comparison, not a blanket source-certified or critical-edition corpus.",
    ],
    "weber": [
        "Current Weber public surface: latest public version is record 21728241 / DOI 10.5281/zenodo.21728241 under the permanent concept DOI 10.5281/zenodo.20412153. It fronts the complete 420-page German Volume I working reader, exposes its editable TeX directly, and groups the reader/source/QA closure in one compact ZIP. Volume I covers the body through Section 188 and the printed errata; the full content map, damaged-section retranscription, four global consistency sweeps, and broad visual spot checks are complete, while the stricter cold page-by-page pass reaches printed p124 with p125 next. The Volume I English reader predates the current German repairs and is unsynchronized. Volume II reaches Section 176; Volume III remains an incomplete repaired cumulative. These are working readers, not critical editions, synchronized translations, full symbol-by-symbol recertification, peer review, mathematical certification, rights determinations, or accessibility remediation.",
    ],
    "noether": [
        "Current Noether public surface is compact record 21699405 under concept DOI 10.5281/zenodo.20412587. Its 20 files directly expose the 459-page full cumulative English working reader and editable master TeX, covering the inherited 43-paper corpus plus the translated German tail through R823 line 24123. The full English PDF is the default preview. German, Spanish, French, and paired Interslavic readers remain direct downloads; bounded CJK and other-language work, source audits, repair evidence, visual evidence, and predecessor maps are grouped into nine coherent ZIPs. The latest same-concept successor retains 19 predecessor files byte-identically and replaces grouped source-audit archive 61 with a 132-member survivor package for bounded Paper 4 and Paper 37 repairs across Latin and Cyrillic Interslavic, Russian, and Ukrainian. Anonymous readback passed all 20 outer files and all 132 replacement-ZIP members. Immutable predecessor 21499492 retains the prior 100-file surface. These are working translations, source controls, repairs, and render witnesses, not peer review, proof checking, complete multilingual synchronization, native-language certification, whole-corpus source certification, rights clearance, accessibility certification, or a critical edition.",
        "Corrections, source comparisons, LaTeX fixes, and translation improvements can be suggested through GitHub issues or pull requests: <https://github.com/KokunoYumeto/modern-latex-manuscripts>. For citation-critical use, verify formulas, tables, theorem statements, diagrams, apparatus notes, and unusual notation against the included source witnesses and current audit ledgers.",
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
        raise FileNotFoundError(f"Missing concept DOI map: {map_path}")

    try:
        records = json.loads(map_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise RuntimeError(f"Cannot read concept DOI map {map_path}: {error}") from error

    urls: dict[str, str] = {}
    for record in records:
        record_id = str(record.get("id", "")).strip()
        concept_url = str(record.get("concepturl", "")).strip()
        if record_id and concept_url:
            if record_id in urls:
                raise RuntimeError(f"Duplicate record ID in concept DOI map: {record_id}")
            urls[record_id] = concept_url
    return urls


def validate_preserved_record_page(
    label: str, rows: list[dict[str, str]], target: Path
) -> None:
    text = target.read_text(encoding="utf-8")
    match = re.search(r"Zenodo record: \[([0-9]+)\]", text)
    expected_record_id = rows[0]["record_id"]
    actual_record_id = match.group(1) if match else None
    if actual_record_id != expected_record_id:
        raise RuntimeError(
            f"Preserved record page for {label!r} is stale: "
            f"{actual_record_id or 'missing'} -> {expected_record_id}. "
            f"Rebuild with --overwrite-record-pages --record-label {label}."
        )

    missing_notes = [
        note for note in RECORD_NOTES.get(label, []) if note not in text
    ]
    if missing_notes:
        raise RuntimeError(
            f"Preserved record page for {label!r} is missing "
            f"{len(missing_notes)} current status note(s). Rebuild with "
            f"--overwrite-record-pages --record-label {label}."
        )


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
    editable_tex = role_rows(rows, "editable TeX")
    other_pdfs = [row for row in pdfs if row not in reader_pdfs]

    if label == "ega":
        reader_pdfs = [
            row for row in rows if row["filename"].startswith("00") and row["filename"].lower().endswith(".pdf")
        ]
        editable_tex = [
            row for row in rows if row["filename"].startswith("01") and row["filename"].lower().endswith(".tex")
        ]
        preferred_zip_names = {
            "00 Current_EGA_English_Readers_and_Buildable_TeX_20260801.zip",
            "02d_EGAIV_English_Complete_Reference_v2_TeX_PDF_QA_20260801.zip",
        }
        zips = [row for row in rows if row["filename"] in preferred_zip_names]
        manifests = []
        other_pdfs = []

    if label in {"ega", "sga"}:
        how_to_read = "Start with the leading current-reader bundle or open a direct reader PDF. Direct master TeX files follow; provenance and QA archives are secondary downloads."
    elif reader_pdfs:
        how_to_read = "Open the reader/reference PDFs first. When editable TeX is listed below, it is a direct download; use artifact ZIPs for additional source witnesses, OCR, page images, render checks, or provenance material."
    else:
        how_to_read = "This record has no top-level reader PDFs in the current file surface. Open the artifact ZIPs for TeX, component PDFs, source witnesses, OCR, page images, render checks, and provenance material."

    quality_warning = "**Quality warning:** This generated page lists public files and current record notes. It does not certify a critical edition. Legacy filenames can include terms such as `Complete`, `Strict`, `Source-Checked`, or `Critical`; use the status notes, source witnesses, and audit ledgers before relying on mathematical details."
    if label == "ega":
        how_to_read = "Open the fronted global EGA 0-IV PDF for one continuous linked reader. The five standalone readers and their master TeX files remain direct downloads; the leading ZIP contains all six readers and their complete buildable TeX closures."
        quality_warning = "**Status:** These are current working readers for the stated scopes, not critical editions, rights clearance, mathematical certification, or uniform whole-corpus certification."

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
        quality_warning,
        "",
        "| Files | PDFs | TeX | ZIPs | Total MB |",
        "|---:|---:|---:|---:|---:|",
        f"| {len(rows) if label != 'ega' else len(reader_pdfs) + len(editable_tex) + len(zips)} | {len(pdfs) if label != 'ega' else len(reader_pdfs)} | {len(editable_tex)} | {len(zips)} | {size_sum(rows) if label != 'ega' else size_sum(reader_pdfs + editable_tex + zips):.1f} |",
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

    if editable_tex:
        lines.extend(["## Editable TeX", ""])
        lines.extend(table_for(editable_tex))

    if other_pdfs:
        lines.extend(["## Additional PDFs", ""])
        lines.extend(table_for(other_pdfs))

    lines.extend(["## Artifact ZIPs", ""])
    lines.extend(table_for(zips))

    if label == "ega":
        hidden_count = len(rows) - len(reader_pdfs) - len(editable_tex) - len(zips)
        lines.extend(
            [
                "## Full Archive",
                "",
                f"The remaining {hidden_count} preserved support files are available in the [full Zenodo file list]({record_url}#files). They are deliberately not expanded on this reading page.",
                "",
            ]
        )

    if manifests:
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
        "| Record | Files | PDFs | TeX | ZIPs | MB | Page | Zenodo |",
        "|---|---:|---:|---:|---:|---:|---|---|",
    ]
    for tier, labels in RECORD_TIERS:
        present = [label for label in labels if grouped.get(label)]
        if not present:
            continue
        lines.append(f"| **{tier}** |  |  |  |  |  |  |  |")
        for label in present:
            rows = grouped[label]
            display = INDEX_DISPLAY_NAMES.get(label, DISPLAY_NAMES.get(label, label.replace("_", " ").title()))
            record_id = rows[0]["record_id"]
            pdfs = [row for row in rows if row["filename"].lower().endswith(".pdf")]
            tex = [row for row in rows if row["filename"].lower().endswith(".tex")]
            zips = [row for row in rows if row["filename"].lower().endswith(".zip")]
            page = f"{slug(label)}.md"
            url = concept_urls.get(record_id, f"https://zenodo.org/records/{record_id}")
            lines.append(
                f"| {display} | {len(rows)} | {len(pdfs)} | {len(tex)} | {len(zips)} | {size_sum(rows):.1f} | [{page}]({page}) | [Zenodo]({url}) |"
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
    parser.add_argument(
        "--record-label",
        help="Rewrite only one record label while still refreshing the index.",
    )
    args = parser.parse_args()

    root = Path.cwd()
    rows = read_rows(root / "manifests" / "public-file-catalog.csv")
    concept_urls = load_concept_urls(root)
    record_ids = {row["record_id"] for row in rows}
    missing_concepts = sorted(record_ids - concept_urls.keys())
    if missing_concepts:
        raise RuntimeError(
            "Current Zenodo records missing from concept DOI map: "
            + ", ".join(missing_concepts)
        )
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[row["record_label"]].append(row)

    out_dir = root / "docs" / "records"
    for label in RECORD_ORDER:
        if label in grouped:
            if args.record_label and label != args.record_label:
                continue
            target = out_dir / f"{slug(label)}.md"
            if args.overwrite_record_pages or not target.exists():
                write_record_page(label, grouped[label], out_dir, concept_urls)
            else:
                validate_preserved_record_page(label, grouped[label], target)
    write_index(grouped, out_dir, concept_urls)
    print(f"Wrote {len(grouped)} record landing pages to {out_dir}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
