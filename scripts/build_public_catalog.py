#!/usr/bin/env python3
"""Build the public Zenodo file catalog for this repository.

This script uses only the public Zenodo records API. It does not need a token.
Run it from the repository root:

    python scripts/build_public_catalog.py

Outputs:
    manifests/public-file-catalog.csv
    manifests/zenodo-records-current.json
    docs/public-file-catalog.md
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import re
import sys
import time
import urllib.request
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError


RECORDS: list[tuple[str, str]] = [
    ("main", "20459634"),
    ("workflow", "21780936"),
    ("visual_evidence", "21730032"),
    ("noether_cjk_visual_evidence", "21499951"),
    ("interlanguage_reflections", "21780933"),
    ("fac_quality_assessment", "21779393"),
    ("lean_formalization_sidecars", "21129946"),
    ("split_zero_research_sidecar", "21443852"),
    ("noether", "21699405"),
    ("weber", "21728241"),
    ("cayley", "20617845"),
    ("sga", "21778810"),
    ("deligne", "21745061"),
    ("ega", "21780931"),
    ("ukrainian_applied_math", "20520721"),
    ("gauss", "20674086"),
    ("riemann", "20434317"),
    ("albattani_opus_astronomicum", "20584850"),
    ("non_european_consolidated", "20586401"),
    ("chinese", "20543246"),
    ("indian_sanskrit", "20435677"),
    ("islamic_arabic", "20435687"),
    ("historical_references", "20435690"),
    ("classical_algebra_arithmetic", "20583048"),
    ("sylvester", "20649689"),
    ("maxwell", "20821947"),
    ("gibbs_old_physics", "20821820"),
    ("dedekind", "20586067"),
    ("dirichlet", "20586064"),
    ("bianchi", "20673932"),
    ("gordan_clebsch_gordan", "20822196"),
    ("steinitz", "20822189"),
    ("frobenius", "20821858"),
    ("poincare", "20673462"),
    ("kneser", "20836972"),
    ("serre", "21721854"),
    ("additional_author_cluster", "20672984"),
]

EXPECTED_SELECTED_PREVIEWS = {
    "ega": "00_GLOBAL_EGA_0_IV_English_Complete_Linked_Reader_20260801.pdf",
    "fac_quality_assessment": "00_READ_ME_FIRST.md",
    "sga": "00_SGA_1-7II_English_Global_Reader.pdf",
    "split_zero_research_sidecar": "00_PROJECT_ATLAS_20260717.pdf",
}

RECORD_NOTES = {
    "main": [
        "Current main-landing version 20459634 retains the preservation/workflow surface and adds two bounded source-aligned English SGA 2 checkpoints for Expose I sections 1 and 2. The six-page and five-page PDFs are directly readable, while one privacy-clean grouped ZIP carries editable TeX, public ledgers, target renders, provenance/attribution notes, cursors, and hashes. Coverage continues at Expose II / French line 505. These are working checkpoints, not complete SGA 2, peer review, a critical edition, or full-volume certification.",
    ],
    "cayley": [
        "Accuracy warning 2026-06-09/12: Cayley files listed here are retained for provenance and repair. Current Cayley PDFs/TeX are not accuracy-certified; package names containing `Source-Checked` are obsolete labels until a future per-page glyph/source audit re-promotes specific ranges. The narrow `Cayley_V1_critical_p001_045_v2_20260609.zip` packet is the current promoted restart tranche for Volume I printed pp.1-58 / Papers 1-9 as a source-inspected working packet, not as a critical edition; v2 corrects the Paper 6 low-comma subscript notation and removes forced source-page whitespace. A later source-quality audit found that several Cayley repair lanes had been working from low-DPI Internet Archive derivative PDFs; future source-faithful repair should prefer the IA `_jp2.zip` master image archives and verified scan-page maps where available.",
    ],
    "classical_algebra_arithmetic": [
        "Accuracy warning 2026-06-09: Cayley files in this older mixed shelf are retained for provenance and repair only; do not treat the Cayley slice readers as faithful editions without a new page-by-page audit.",
    ],
    "maxwell": [
        "Dedicated Maxwell working-tranche record. Current public coverage is A Treatise on Electricity and Magnetism, Volume I: IA 1873 first-edition source-witnessed working sequence pp.001-079, or 79/467 source-map pages (16.9 percent), plus earlier ledger-backed source-witnessed working tranches for book pages 95-101, 103, 105, 109, and continuous pp.111-267. The pp.001-079 sequence is governed by the closeout and continuation ledgers in the public ZIPs; it is not a complete Treatise edition or final critical edition. Source-check ledgers and witness images govern promoted range claims, while OCR/XML material is only a locator/provenance layer. The next continuation point for the compact IA-first-edition sequence is printed p.080 / IA leaf 118.",
    ],
    "albattani_opus_astronomicum": [
        "Legacy filename warning: the fixed-star catalogue PDF name contains `Complete Critical Edition`, but the current project status does not certify it as a final critical edition. Read it as a working data/catalogue layer with source witnesses, not as maintainer-certified critical finality.",
    ],
    "non_european_consolidated": [
        "Legacy filename warning: inherited al-Battani files in this consolidated shelf can contain `Complete Critical Edition`. The consolidated shelf is a working multilingual/source-intake record; work-level status notes override legacy filenames.",
    ],
    "sga": [
        "Current compact SGA record 21756931 starts with one ZIP containing the current standalone English reader PDFs and buildable TeX closures for SGA 1 through SGA 7 II. The same readers and masters remain direct; SGA1 is the default preview. This is not yet one cross-volume SGA 1-7.2 PDF. The clean 1,470-page SGA3 R29 cumulative is directly readable. SGA7 I has a complete 287-page English working reader for all written Exposes I, II, VI, VII, VIII, and IX. SGA7 II now has a complete 264-page English working reader containing Exposes X-XXII through volume EOF, with its master TeX direct and its 183-component buildable source in a 187-member ZIP. The separately available French SGA7 II working transcription remains partial. Anonymous readback passed all 88 outer files, all 83 retained predecessor identities, all 187 reader/source ZIP members, all 1,770 all-current-reader bundle members, and all 13 release-control members. Historical versions are immutable. These are working editions, translations, and transcriptions, not critical editions, rights determinations, mathematical certifications, exhaustive reference certifications, accessibility certifications, or final whole-SGA certification.",
    ],
    "ega": [
        "Open the fronted 1,356-page linked EGA 0-IV English reader for one continuous reading surface, or use the five direct standalone readers. The leading bundle contains the global reader, all five standalone readers, and their complete buildable TeX closures. Current same-concept record 21780931 retains those reader-facing bytes and adds a coherent EGA I printed-p.127 custody checkpoint: diplomatic French through p.127, the paired English state, a French-rooted pre-Stacks indexing scaffold, exact manifests/validation, and privacy-clean project logbook, continuation, status, correction, and workflow-error histories. The record has 58 files / 3,776,100,143 bytes; all nine new files and all 49 retained predecessor files passed anonymous byte/SHA-256 readback. Canonical diplomatic French EGA 0-IV, French-authority rechecking, and the cumulative pre-Stacks graph remain active; production has continued beyond this bounded p.127 snapshot. These are working translations and audit materials, not critical editions, rights clearance, mathematical certification, accessibility certification, or a claim of uniform whole-corpus source certification.",
    ],
    "workflow": [
        "Current workflow version 21707334 publishes a compact eleven-file methodology surface. The corrected seven-page A4 workflow PDF remains the default preview, with the exact Markdown, Claude high-resolution source method, resource-efficiency incident note, controlling SGA3 diagram-fidelity correction, seven-member source packet, and retained July 6 addenda. It adds one exact ChatGPT export of dated July 11-27 research-methodology briefings, explicitly labeled generated and unverified; claims and citations require primary-source checking. User-supplied OCR remains read-only locator/drafting evidence and must not be regenerated. Existing 600/1200-dpi evidence remains valid history and context; only 300-dpi-only approvals and independently found material defects are reopened. New final SGA3 diagram successors use native editable TeX, 300-dpi page context, about 5000-dpi default comparison, targeted 9000-dpi ambiguity crops, disjoint ownership, and lead-signed evidence. Raster authority witnesses remain private. The emissions discussion is scenario analysis, not metered OpenAI telemetry. These are methodology, accountability, and research-note materials, not edition or translation certification.",
    ],
    "visual_evidence": [
        "Dedicated compute-reuse dataset for provenance-bound high-detail source crops used during SGA and EGA transcription checks. The initial version contains 5,855 recovered SGA7 I targeted crops in two image archives plus one metadata archive. It is source-audit evidence, not a reader, translation, critical edition, mathematical certification, or blanket rights determination. Reader landing pages remain separate and reader-first.",
    ],
    "noether_cjk_visual_evidence": [
        "Dedicated compute-reuse supplement for 290 public-safe Noether/CJK visual-evidence and render-QA images, with a complete 2,020-row inventory and metadata-only accounting for 14 rights-blocked images. The archive retains one explicitly malformed inherited contact-sheet PNG as adverse evidence. It supplements the Noether and interlanguage-methodology concepts; it is not a reader, translation, source-fidelity or mathematical certification, native-language review, or blanket rights determination.",
    ],
    "weber": [
        "Current Weber public surface is record 21728241 under concept DOI 10.5281/zenodo.20412153. It fronts the complete 420-page German Volume I working reader, exposes its editable TeX directly, and groups the reader/source/QA closure in one compact ZIP. Volume I covers the body through Section 188 and the printed errata; the full content map, damaged-section retranscription, four global consistency sweeps, and broad visual spot checks are complete, while the stricter cold page-by-page pass reaches printed p124 with p125 next. The Volume I English reader predates the current German repairs and is unsynchronized. Volume II reaches Section 176; Volume III remains an incomplete repaired cumulative. These are working readers, not critical editions, synchronized translations, full symbol-by-symbol recertification, peer review, mathematical certification, rights determinations, or accessibility remediation.",
    ],
    "noether": [
        "Current Noether public surface is compact record 21699405. Its 20 files directly expose the 459-page full cumulative English working reader and editable master TeX, covering the inherited 43-paper corpus plus the translated German tail through R823 line 24123. The full English PDF is the default preview. German, Spanish, French, and paired Interslavic readers remain direct downloads; bounded CJK and other-language work, source audits, repair evidence, visual evidence, and predecessor maps are grouped into nine coherent ZIPs. The latest same-concept successor retains 19 predecessor files byte-identically and replaces grouped source-audit archive 61 with a 132-member survivor package for bounded Paper 4 and Paper 37 repairs across Latin and Cyrillic Interslavic, Russian, and Ukrainian. Anonymous readback passed all 20 outer files and all 132 replacement-ZIP members. Immutable predecessor 21499492 retains the prior 100-file surface. These are working translations, source controls, repairs, and render witnesses, not peer review, proof checking, complete multilingual synchronization, native-language certification, whole-corpus source certification, rights clearance, accessibility certification, or a critical edition.",
    ],
    "kneser": [
        "Dedicated Kneser working-edition split from the mixed additional-author shelf. Current public coverage fronts German-source and English working-translation reader PDF/TeX surfaces through p0011-p0248, a high-quality source witness through p0001-p0248, and the p0234 lower-p0248 slice/audit package. The included worklist reports 248/336 source pages done (73.8 percent), latest slice sections 53-55 completing the Sixth Section, and next continuation at p0249 / Seventh Section / section 56. This is a source-witnessed working draft and audit/progress record, not a certified critical edition.",
    ],
    "serre": [
        "Dedicated Serre working-transcription record. FAC is directly readable as a complete 63-page French working transcription covering all 82 source pages / printed pp.197-278. The direct master and body TeX accompany one compact 27-member FAC source/evidence ZIP containing the complete editable closure, exact ledgers, and four actual scan-derived crops with page, rasterization, bounding-box, dimension, and hash provenance. A separate eight-member ZIP preserves the complete first-pass GAGA TeX source for printed pp.1-42; its earlier PDF remains held because visible join sentinels are still present. License metadata is License Not Specified. This is working-transcription custody, not a complete Serre corpus, critical edition, mathematical certification, accessibility certification, or blanket rights clearance.",
    ],
    "lean_formalization_sidecars": [
        "Small Lean 4 / Mathlib-style sidecar record for useful formalization/library-candidate material connected to the historical transcription and translation archive. These files are not source-fidelity evidence, not translation certification, not scanned-edition certification, and not critical-edition material.",
    ],
    "split_zero_research_sidecar": [
        "Separate exploratory mathematics sidecar, outside the manuscript-translation completion ranking. Current version 21443852 fronts the concise Project Atlas and retains the bookmarked results compendium, Lean/Python checks and ledgers, editable working texts, replayable visualization/data packages, and the bounded N16-N18 predatum/K4/Hopf supplement from predecessor 21426216. It adds the coherent Part 8-C2A through C2F2 finite-glue, shell, triality, and Fricke proof chain. The seven source-free Python replays pass 16/16, 19/19, 16/16, 18/18, 20/20, 11/11, and 19/19 checks; the stated marking, topology, classification, and Niemeier/Fricke boundaries remain explicit. This is a working research record, not peer review, a proof of a famous open problem, or certification of every broader claim.",
    ],
    "deligne": [
        "Current reader-first surface is version 21745061. It retains the sequential English and French working readers through Papers 001-016p080, the grouped paper/letter PDF and TeX/source/QA archives, and the D001 source-aligned readers/source package, then adds direct bilingual, English, and French source-aligned working readers plus a 21-member TeX/source-crop package for D002. The cumulative English reader remains the default preview. D001 and D002 are complete source-aligned working editions for those papers only; the wider corpus remains uneven working-draft and repair material, not a critical edition, peer review, mathematical certification, or blanket source-faithfulness claim.",
    ],
    "chinese": [
        "Current version 20543246 provides direct English, modern-Chinese, Chinese-original, and Arabic working-reader surfaces plus filtered TeX/source archives. The Arabic files are working translation drafts whose local checks establish build/openability, not native-language or source-accuracy certification.",
    ],
    "indian_sanskrit": [
        "Current version 20435677 provides reader/index PDFs and a filtered TeX/source archive for the represented Indian and Sanskrit works. These are working original-language and English translation drafts, not proofed critical editions.",
    ],
    "islamic_arabic": [
        "Current version 20435687 provides reader/index PDFs, original/reference surfaces, English working translations, and a filtered TeX/source archive. These are working drafts and reference witnesses, not proofed critical editions.",
    ],
    "historical_references": [
        "Current version 20435690 is a focused historical-reference shelf with reader PDFs and filtered TeX/source material. It supports terminology and historical comparison; it is not a blanket source-certified or critical-edition corpus.",
    ],
    "interlanguage_reflections": [
        "Methodology, source-body, provenance, corpus-control, and bounded-output sidecar for mathematical translation. Current version 21744853 retains all 65 predecessor files from 21743417 and adds one compact six-member Tajik algebra source-anchor ZIP containing two public university mathematics PDFs plus exact scope, metadata, manifest, and checksum controls. This closes the Tajik abstract-algebra source row, not Tajik native TeX, native review, terminology approval, or rights clearance. The retained Persian packet closes a Noether-topic editable-source row only, not Persian invariant theory; GitHub reported no repository license. Paper 06 semantic reconciliation, linguistic review, global-ledger completeness, Persian invariant theory, Arabic invariant theory, Dari editable mathematics, and Tajik native-TeX source remain open. These are methodology, normalization, corpus, source-custody, bounded working-translation, provenance, and QA artifacts, not native validation, translation or source-fidelity certification, community certification, peer review, or critical editions.",
    ],
    "additional_author_cluster": [
        "Mixed selected-author shelf. This remains a backstop/provenance shelf for authors not yet split into full standalone records and for older routed packets. Kneser now has a preferred standalone record at concept DOI `10.5281/zenodo.20836971`; earlier Kneser packets in this shelf remain provenance/backstop. Poincare and Frobenius also have preferred standalone records. Treat this shelf package by package, not as a blanket certification of every included author.",
    ],
}

RECORD_NOTES.update(
    {
        "sga": [
            "Current same-concept SGA record 21778810 fronts the complete 126-member privacy-clean reader/source ZIP, then selects the clean 4,177-page cumulative English reader as the default preview, followed by nine standalone English readers, nine master TeX files, nine buildable source ZIPs, and exact validation/privacy controls. The record has 34 files / 182,736,901 bytes. The cumulative graph has 39,690 named destinations and 30,649 internal GoTo actions with no broken or misrouted link; all 4,177 pages match the admitted standalone inputs, Type3 and unembedded fonts are zero, PDF image objects are zero, and reader scans found no archive workflow/source-status prose or AI explanatory footnotes. The archive-derived projection made 45 minimal privacy replacements across 16 non-reader files while leaving all ten reader PDFs byte-identical; predecessor 21778605 remains immutable adverse history. The exact SGA logbook, decision ledger, revision/reversal history, controlling dual-DOI requirement, and current 482-record privacy-clean English/Germanic archive log are publicly hash-read back on methodology record 21780933 and replication record 21780936. These are working editions and translations, not critical editions, rights determinations, peer review, mathematical certification, accessibility certification, or uniform whole-series source certification. Record rights metadata remains License Not Specified."
        ],
        "interlanguage_reflections": [
            "Current methodology head 21780933 preserves the broad interlanguage, source-body, corpus-control, normalization, and bounded-output sidecar and exposes the complete 482-record v3 privacy-clean English/Germanic decision log with its 2,427-event transformation ledger. It adds the EGA I printed-p.127 privacy-clean project logbook, continuation, status, append-only correction/error histories, and French-rooted pre-Stacks scaffold as direct trust surfaces. Its 99 files / 4,993,523,160 bytes passed anonymous readback for all 17 new uploads, every member of the deterministic 15-member retained-legacy companion ZIP, and all 82 retained predecessor files. The 14 compacted legacy companions remain direct on predecessor 21780213 and exact inside the successor ZIP; nothing distinct was curated away. Earlier adverse-history predecessors remain immutable. Existing corpus-specific caveats, rights boundaries, open language-review work, and immutable predecessors remain in force."
        ],
        "workflow": [
            "Current replication head 21780936 preserves the workflow and replication packet and exposes the complete 482-record v3 privacy-clean English/Germanic decision log with its 2,427-event transformation ledger. It adds the EGA I printed-p.127 privacy-clean project logbook, continuation, status, append-only correction/error histories, and French-rooted pre-Stacks scaffold as direct replication surfaces. Its 76 files / 11,952,637 bytes passed anonymous readback for all 15 new uploads and all 61 retained predecessor files. Earlier adverse-history predecessors remain immutable. These materials permit inspection of decisions, reversals, errors, continuation state, archive custody, and the bounded p.127 scaffold; they do not certify the editions, translations, mathematics, rights, or accessibility."
        ],
        "fac_quality_assessment": [
            "Dedicated producer-owned FAC quality-assessment record 21779393 documents an accidental held-out comparison: Codex translated and source-checked FAC nos. 1-79 from Serre's French authority before the project discovered the independent Achinger-Krupa English translation. The record fronts a human-readable chronology, a 74-page blind reader through no. 79, a 78-page complete project reader through no. 81, 79 unit reviews, 138 locator-bound findings, 95 frozen input identities, 219 self-correction rows, decision/project/process logbooks, exact validation, and a 111-entry English/French project TeX source ZIP. All 22 files / 2,077,104 bytes passed public UI MD5 replay and anonymous raw byte/SHA-256 readback. The comparator PDF/source and French authority scan are not redistributed; authorship, URLs, hashes, rights limits, and source authority are explicit. This is inspectable bounded quality evidence, not peer review, mathematical certification, canonicity, a scalar score, general model superiority, or blanket rights clearance. Nos. 80-81 postdate discovery and are excluded from blind claims. Concept DOI 10.5281/zenodo.21779392 is authoritative for this FAC evidence; do not duplicate it into GAGA or mint another FAC concept."
        ],
    }
)

FAC_BROAD_CROSSLINK_NOTE = (
    "Open the dedicated producer-owned FAC quality-assessment concept "
    "10.5281/zenodo.21779392 (current version 10.5281/zenodo.21779393) for the "
    "controlling coherent accidental blind-comparison package. Earlier FAC "
    "projections on this broad record remain immutable adverse history; the "
    "dedicated FAC files are not duplicated here, and GAGA remains separate."
)
for broad_label in ("interlanguage_reflections", "workflow"):
    RECORD_NOTES[broad_label].insert(0, FAC_BROAD_CROSSLINK_NOTE)

TITLE_OVERRIDES = {
    "albattani_opus_astronomicum": "al-Battani: Opus Astronomicum / Kitab al-Zij, Text Working Edition and Audited Table Data",
    "sylvester": "James Joseph Sylvester: Collected Mathematical Papers, Source-Witnessed Modern LaTeX Working Drafts",
    "maxwell": "James Clerk Maxwell: A Treatise on Electricity and Magnetism, Volume I Source-Witnessed LaTeX Working Tranches",
    "dedekind": "Richard Dedekind: Source-Witnessed Working Drafts and English Translations",
    "dirichlet": "P. G. Lejeune Dirichlet: Werke Band II Source-Witnessed Working Drafts and English Translations",
    "gordan_clebsch_gordan": "Paul Gordan and Clebsch-Gordan: Source-Witnessed LaTeX and Translation Working Drafts",
    "frobenius": "Ferdinand Georg Frobenius: Group Character Papers, German Source and English Translation Working Drafts",
    "poincare": "Henri Poincare: Oeuvres, Tome I Source-Witnessed French/English Working Drafts",
    "kneser": "Adolf Kneser: Lehrbuch der Variationsrechnung, German Source and English Translation Working Drafts",
    "serre": "Jean-Pierre Serre: FAC Complete French Working Transcription and GAGA TeX Source Custody",
    "lean_formalization_sidecars": "Classical Mathematics Lean 4 Formalization Sidecars",
    "interlanguage_reflections": "Interlanguage and Mathematical Translation Methodology Sidecar",
    "split_zero_research_sidecar": "Split-Zero Geometry and Common Deformation Registers: Project Atlas, Exact Results, Formalization, and Visualizations",
    "visual_evidence": "SGA and EGA High-Detail Source-Audit Image Worksets: Compute-Reuse Dataset",
    "noether_cjk_visual_evidence": "Noether CJK Visual Evidence and Render-QA Images: Compute-Reuse Dataset",
}


class _RecordDataParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.record_data: str | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id") == "recordVersions" and values.get("data-record"):
            self.record_data = values["data-record"]


def fetch_public_record_page(record_id: str) -> tuple[dict[str, Any], str]:
    url = f"https://zenodo.org/records/{record_id}"
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "modern-latex-manuscripts-catalog/1.0"},
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        page = response.read().decode("utf-8", errors="replace")

    parser = _RecordDataParser()
    parser.feed(page)
    if not parser.record_data:
        raise RuntimeError(f"Cannot identify embedded data for Zenodo record {record_id}")
    record = json.loads(parser.record_data)
    file_data = record.get("files", {})
    if isinstance(file_data, dict) and isinstance(file_data.get("entries"), dict):
        record["files"] = [
            {"key": key, **value}
            for key, value in file_data["entries"].items()
        ]
        record["default_preview"] = file_data.get("default_preview", "")
    return record, page


def fetch_record(record_id: str) -> dict[str, Any]:
    url = f"https://zenodo.org/api/records/{record_id}/versions/latest"
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "modern-latex-manuscripts-catalog/1.0"},
    )
    for attempt in range(8):
        try:
            with urllib.request.urlopen(request, timeout=120) as response:
                return json.loads(response.read().decode("utf-8"))
        except HTTPError as error:
            if error.code == 403:
                break
            if attempt == 7:
                break
            print(
                f"Retrying Zenodo record {record_id} after API failure "
                f"({attempt + 1}/8)",
                file=sys.stderr,
            )
            time.sleep(2 ** attempt)
        except (URLError, TimeoutError):
            if attempt == 7:
                break
            print(
                f"Retrying Zenodo record {record_id} after API failure "
                f"({attempt + 1}/8)",
                file=sys.stderr,
            )
            time.sleep(2 ** attempt)
    print(
        f"Using Zenodo public HTML fallback for record {record_id}",
        file=sys.stderr,
    )
    record, _ = fetch_public_record_page(record_id)
    return record


def fetch_selected_preview(record_id: str) -> str:
    for attempt in range(8):
        try:
            record, page = fetch_public_record_page(record_id)
            embedded_preview = record.get("default_preview", "")
            if embedded_preview:
                return str(embedded_preview)
            match = re.search(
                r'id=["\']preview-file-title["\'][^>]*>([^<]+)', page
            )
            if not match:
                raise RuntimeError(
                    f"Cannot identify the selected preview for Zenodo record {record_id}"
                )
            return html.unescape(match.group(1)).strip()
        except (HTTPError, URLError, TimeoutError):
            if attempt == 7:
                raise
            print(
                f"Retrying Zenodo preview {record_id} after request failure "
                f"({attempt + 1}/8)",
                file=sys.stderr,
            )
            time.sleep(2 ** attempt)
    raise AssertionError("unreachable")


def file_role(filename: str) -> str:
    lower = filename.lower()
    if lower.endswith(".zip"):
        return "artifact/source ZIP"
    if lower.endswith((".json", ".md", ".csv", ".txt")):
        return "manifest/status"
    if lower.endswith(".tex"):
        return "editable TeX"
    if lower.endswith(".pdf"):
        return "reader/reference PDF"
    return "other"


def file_url(record_id: str, filename: str) -> str:
    from urllib.parse import quote

    return f"https://zenodo.org/records/{record_id}/files/{quote(filename)}"


def reader_facing_rows(label: str, rows: list[dict[str, str]]) -> list[dict[str, str]]:
    """Keep the EGA catalog page focused on material a reader opens directly."""
    if label != "ega":
        return rows

    direct_prefixes = (
        "00_GLOBAL_",
        "00a_",
        "00b_",
        "00c_",
        "00d_",
        "00e_",
        "00f_",
        "01_GLOBAL_",
        "01a_",
        "01b_",
        "01c_",
        "01d_",
        "01e_",
        "02d_",
    )
    bundle = "00 Current_EGA_English_Readers_and_Buildable_TeX_20260801.zip"
    return [
        row
        for row in rows
        if row["filename"] == bundle
        or row["filename"].startswith(direct_prefixes)
    ]


def build_rows(selected_labels: set[str] | None = None) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for label, record_id in RECORDS:
        if selected_labels is not None and label not in selected_labels:
            continue
        record = fetch_record(record_id)
        actual_record_id = str(record.get("id", record_id))
        if actual_record_id != record_id:
            raise RuntimeError(
                f"Configured Zenodo head for {label!r} is stale: "
                f"{record_id} -> {actual_record_id}. Review the successor, then "
                "update RECORDS and its public status notes before rebuilding."
            )
        expected_preview = EXPECTED_SELECTED_PREVIEWS.get(label)
        if expected_preview:
            actual_preview = fetch_selected_preview(record_id)
            if actual_preview != expected_preview:
                raise RuntimeError(
                    f"Selected preview for {label!r} changed: "
                    f"{expected_preview!r} -> {actual_preview!r}. Review the "
                    "live record and update its public status notes before rebuilding."
                )
        title = TITLE_OVERRIDES.get(label, record.get("metadata", {}).get("title", ""))
        for item in sorted(record.get("files", []), key=lambda value: value.get("key", "").lower()):
            filename = item.get("key", "")
            size_bytes = int(item.get("size", 0))
            size_mb = size_bytes / (1024 * 1024)
            rows.append(
                {
                    "record_label": label,
                    "record_id": actual_record_id,
                    "record_title": title,
                    "file_role": file_role(filename),
                    "filename": filename,
                    "size_mb": f"{size_mb:.4f}",
                    "_size_bytes": size_bytes,
                    "url": file_url(actual_record_id, filename),
                }
            )
    return rows


def read_existing_rows(path: Path) -> list[dict[str, Any]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def update_current_record(
    rows: list[dict[str, Any]], path: Path, selected_label: str
) -> None:
    records = json.loads(path.read_text(encoding="utf-8"))
    group = [row for row in rows if row["record_label"] == selected_label]
    if not group:
        raise RuntimeError(f"No catalog rows generated for {selected_label!r}")
    role_counts: dict[str, int] = {}
    for row in group:
        role = str(row["file_role"])
        role_counts[role] = role_counts.get(role, 0) + 1
    replacement = {
        "label": selected_label,
        "record_id": group[0]["record_id"],
        "title": group[0]["record_title"],
        "url": f"https://zenodo.org/records/{group[0]['record_id']}",
        "file_count": len(group),
        "total_mb": round(
            sum(int(row["_size_bytes"]) for row in group) / (1024 * 1024), 4
        ),
        "role_counts": dict(sorted(role_counts.items())),
    }
    updated = False
    for index, record in enumerate(records):
        if record.get("label") == selected_label:
            records[index] = replacement
            updated = True
            break
    if not updated:
        records.append(replacement)
        records.sort(key=lambda row: str(row["label"]))
    path.write_text(json.dumps(records, indent=2) + "\n", encoding="utf-8")


def write_csv(rows: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        fieldnames = [
            "record_label",
            "record_id",
            "record_title",
            "file_role",
            "filename",
            "size_mb",
            "url",
        ]
        writer = csv.DictWriter(
            handle,
            fieldnames=fieldnames,
        )
        writer.writeheader()
        writer.writerows({field: row[field] for field in fieldnames} for row in rows)


def write_current_records(rows: list[dict[str, Any]], path: Path) -> None:
    grouped: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        grouped.setdefault(row["record_label"], []).append(row)

    records: list[dict[str, Any]] = []
    for label in sorted(grouped):
        group = grouped[label]
        role_counts: dict[str, int] = {}
        for row in group:
            role = row["file_role"]
            role_counts[role] = role_counts.get(role, 0) + 1
        records.append(
            {
                "label": label,
                "record_id": group[0]["record_id"],
                "title": group[0]["record_title"],
                "url": f"https://zenodo.org/records/{group[0]['record_id']}",
                "file_count": len(group),
                "total_mb": round(sum(int(row["_size_bytes"]) for row in group) / (1024 * 1024), 4),
                "role_counts": dict(sorted(role_counts.items())),
            }
        )

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(records, indent=2) + "\n", encoding="utf-8")


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


def write_markdown(rows: list[dict[str, str]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    grouped: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        grouped.setdefault(row["record_label"], []).append(row)

    root = path.parent.parent
    concept_urls = load_concept_urls(root)
    record_ids = {row["record_id"] for row in rows}
    missing_concepts = sorted(record_ids - concept_urls.keys())
    if missing_concepts:
        raise RuntimeError(
            "Current Zenodo records missing from concept DOI map: "
            + ", ".join(missing_concepts)
        )

    lines: list[str] = [
        "# Public File Catalog",
        "",
        "Generated from the public Zenodo records API.",
        "",
        "**Quality warning:** this catalog mirrors public Zenodo filenames and record titles. It does not certify critical-edition status. Terms such as `Complete`, `Strict`, `Source-Checked`, or `Critical` can be legacy filenames or scoped working labels; use the current record notes, source witnesses, and audit ledgers before relying on mathematical details.",
        "",
        "## How To Read This Catalog",
        "",
        "| Signal | What It Usually Means | Caution |",
        "|---|---|---|",
        "| `reader/reference PDF` | A front-facing reader PDF, source scan, or reference witness. | The record notes decide whether it is a readable draft or only a witness/reference scan. |",
        "| `artifact/source ZIP` | TeX, source witnesses, page images, OCR, render checks, logs, ledgers, or provenance. | ZIPs can contain current work, superseded repair material, or raw witness layers; read the status files inside. |",
        "| `manifest/status` | JSON, Markdown, CSV, or text status files. | These are often the quickest way to learn what is current, partial, superseded, or suspect. |",
        "| `OCR`, `formula_witness`, `crop_witness`, `locator`, `aid` in a filename | Machine extraction or local aid material. | Use as evidence for repair/checking, not as a mathematical edition. |",
        "| `reader`, `working`, `cumulative`, `translation` in a filename | A compiled draft meant to be read or continued. | Still verify serious formulas, tables, diagrams, and theorem statements against source witnesses. |",
        "| `complete`, `strict`, `source_checked`, `critical`, `audit`, `repair` in a filename | A package's local or inherited scope label. | These terms do not override the current record notes; many are scoped, legacy, or repair labels rather than global certification. |",
        "",
        f"Total files indexed: {len(rows)}",
        "",
    ]

    for label, _record_id in RECORDS:
        group = grouped.get(label, [])
        if not group:
            continue
        displayed_group = reader_facing_rows(label, group)
        title = group[0]["record_title"]
        record_id = group[0]["record_id"]
        record_url = concept_urls.get(record_id, f"https://zenodo.org/records/{record_id}")
        lines.extend(
            [
                f"## {html.escape(title)}",
                "",
                f"Record: <{record_url}>",
                "",
            ]
        )
        for note in RECORD_NOTES.get(label, []):
            lines.extend([note, ""])
        lines.extend(
            [
                "| Role | Size MB | File |",
                "|---|---:|---|",
            ]
        )
        for row in displayed_group:
            filename = row["filename"]
            lines.append(
                f"| {row['file_role']} | {row['size_mb']} | [{html.escape(filename)}]({row['url']}) |"
            )
        if label == "ega":
            hidden_count = len(group) - len(displayed_group)
            lines.extend(
                [
                    "",
                    f"The remaining {hidden_count} preserved support files stay available in the "
                    f"[full Zenodo file list](https://zenodo.org/records/{record_id}#files); "
                    "they are intentionally omitted from this reader-facing catalog.",
                ]
            )
        lines.append("")

    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--record-label",
        choices=[label for label, _record_id in RECORDS],
        help="Refresh only one verified record while preserving other catalog rows.",
    )
    args = parser.parse_args()
    root = Path.cwd()
    catalog_path = root / "manifests" / "public-file-catalog.csv"
    current_path = root / "manifests" / "zenodo-records-current.json"
    selected = {args.record_label} if args.record_label else None
    fresh_rows = build_rows(selected)
    if args.record_label:
        existing = read_existing_rows(catalog_path)
        rows = [
            row for row in existing if row["record_label"] != args.record_label
        ] + fresh_rows
        order = {label: index for index, (label, _record_id) in enumerate(RECORDS)}
        rows.sort(
            key=lambda row: (
                order.get(str(row["record_label"]), len(order)),
                str(row["filename"]).casefold(),
            )
        )
        update_current_record(fresh_rows, current_path, args.record_label)
    else:
        rows = fresh_rows
        write_current_records(rows, current_path)
    write_csv(rows, catalog_path)
    write_markdown(rows, root / "docs" / "public-file-catalog.md")
    print(
        f"Indexed {len(rows)} public files; refreshed "
        f"{args.record_label or f'{len(RECORDS)} records'}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
