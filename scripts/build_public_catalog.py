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

import csv
import html
import json
import re
import sys
import time
import urllib.request
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError


RECORDS: list[tuple[str, str]] = [
    ("main", "20459634"),
    ("workflow", "21707334"),
    ("interlanguage_reflections", "21485338"),
    ("lean_formalization_sidecars", "21129946"),
    ("split_zero_research_sidecar", "21443852"),
    ("noether", "21699405"),
    ("weber", "21513712"),
    ("cayley", "20617845"),
    ("sga", "21720340"),
    ("deligne", "21212608"),
    ("ega", "21717450"),
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
    ("serre", "21720997"),
    ("additional_author_cluster", "20672984"),
]

EXPECTED_SELECTED_PREVIEWS = {
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
        "Current compact SGA record 21720340 starts with one 1,394-member ZIP containing all six cumulative English reader PDFs and complete buildable TeX closures. The same readers and masters remain direct in SGA1-6 order; SGA1 remains the default preview. The 1,470-page SGA3 R29 cumulative covers the Introduction, Exposes I-XXVI, Tome-I subject index, Tome-III mathematical guide, and terminal index, with 13,119 named destinations and 12,337 valid internal GoTo actions. SGA7 I is a complete working source transcription of its six written exposes in a 267-page PDF. Direct SGA7 II files provide a working French source transcription of Exposes X-XVII. Its compact source archive preserves 48 continuous Expose-XVIII markers, scan indices 261-308, including the exact 400-dpi index-261 title/contents crop with parent hash, page, bbox, dimensions, linked source, and crop hash; indices 309-334 remain absent, so Expose XVIII is explicitly incomplete and outside the direct reader. Existing image archives retain 5,033 Number12-derived high-detail images, ten recovered-page images, 29 lead-opened SGA7 I/II PNGs, and 260 post-cutoff SGA7 I crop pixels. These are actual source pixels, not reader screenshots or metadata-only substitutes. Anonymous readback passed all 80 outer files / 671,216,941 bytes, all 78 retained predecessor identities, and all 22 members of the replacement source archive. SGA3 remains a useful heterogeneous integration rather than final whole-reader diagram-fidelity closure; SGA4half remains rights-held; SGA6 remains layered rather than uniformly source-certified. Historical versions remain immutable. These are working editions, translations, transcriptions, and source-image evidence, not critical editions, rights determinations, mathematical certifications, accessibility certifications, uniform whole-series source certification, or final whole-SGA certification. Record rights metadata remains License Not Specified.",
    ],
    "ega": [
        "Current EGA surface is compact record 21717450 under the established EGA concept DOI 10.5281/zenodo.20414353. It starts with one 125-member ZIP containing all five current cumulative English reader PDFs and their complete buildable TeX closures; the same readers and masters remain direct downloads. EGA 0 through Section 13, EGA I through authority EOF, EGA II through authority EOF, and the complete published EGA III text through 7.9.14 are reference-v2 working readers. The direct cumulative EGA IV reader remains source-aligned through Sections 1-10. Archive 02e separately preserves complete bounded Sections 16-18, while direct reader 00f and source archive 02f preserve the corrected 133-page source-aligned r6 Sections 19-21 plus Part 4 backmatter reader; neither is a cumulative Sections 1-21 integration. Eleven image ZIPs preserve 989 actual high-detail source-image witnesses from the publicly available NUMDAM EGA IV Part 4 scan, continuously covering printed pages 5-336. The images include 600/1800-dpi page and band evidence, targeted 5000/9000-dpi ambiguity crops, and full 1800-dpi pages through 336. They are public scan-derived pixels, not ledger-only placeholders or English-reader screenshots. Anonymous readback passed all 44 outer files / 3,745,046,266 bytes and all 19 members of the replacement source ZIP; 42 unrelated predecessor files remained byte-identical and two reader/source artifacts were replaced. EGA 0 remains the default preview. Sections 11-15 remain the principal cumulative integration gap. Superseded loose readers remain available in immutable predecessor versions. Record rights metadata is License Not Specified. EGA remains separate from SGA because it has its own established concept and authority history. These are working translations and source controls, not a complete whole-EGA translation, critical edition, rights clearance, peer review, accessibility certification, or whole-reader source certification.",
    ],
    "workflow": [
        "Current workflow version 21707334 publishes a compact eleven-file methodology surface. The corrected seven-page A4 workflow PDF remains the default preview, with the exact Markdown, Claude high-resolution source method, resource-efficiency incident note, controlling SGA3 diagram-fidelity correction, seven-member source packet, and retained July 6 addenda. It adds one exact ChatGPT export of dated July 11-27 research-methodology briefings, explicitly labeled generated and unverified; claims and citations require primary-source checking. User-supplied OCR remains read-only locator/drafting evidence and must not be regenerated. Existing 600/1200-dpi evidence remains valid history and context; only 300-dpi-only approvals and independently found material defects are reopened. New final SGA3 diagram successors use native editable TeX, 300-dpi page context, about 5000-dpi default comparison, targeted 9000-dpi ambiguity crops, disjoint ownership, and lead-signed evidence. Raster authority witnesses remain private. The emissions discussion is scenario analysis, not metered OpenAI telemetry. These are methodology, accountability, and research-note materials, not edition or translation certification.",
    ],
    "weber": [
        "Current Weber public surface is record 21513712 under concept DOI 10.5281/zenodo.20412153. It retains the readable modernized and summarized reader surface and adds two deterministic Volume I high-detail audit-crop archives: 248 page-mapped tight crops and 846 recovered formula-, glyph-, and detail-level images whose page locator was not recovered. All three volumes remain incomplete. Volume I's direct German content-fidelity pass reaches printed p88 with p89 next; its English reader predates those repairs and is unsynchronized. Volume II reaches section 176; Volume III is an incomplete repaired cumulative, not a finished v3. The images are visual/provenance evidence rather than source, translation, mathematics, or critical-edition certification.",
    ],
    "noether": [
        "Current Noether public surface is compact record 21699405. Its 20 files directly expose the 459-page full cumulative English working reader and editable master TeX, covering the inherited 43-paper corpus plus the translated German tail through R823 line 24123. The full English PDF is the default preview. German, Spanish, French, and paired Interslavic readers remain direct downloads; bounded CJK and other-language work, source audits, repair evidence, visual evidence, and predecessor maps are grouped into nine coherent ZIPs. The latest same-concept successor retains 19 predecessor files byte-identically and replaces grouped source-audit archive 61 with a 132-member survivor package for bounded Paper 4 and Paper 37 repairs across Latin and Cyrillic Interslavic, Russian, and Ukrainian. Anonymous readback passed all 20 outer files and all 132 replacement-ZIP members. Immutable predecessor 21499492 retains the prior 100-file surface. These are working translations, source controls, repairs, and render witnesses, not peer review, proof checking, complete multilingual synchronization, native-language certification, whole-corpus source certification, rights clearance, accessibility certification, or a critical edition.",
    ],
    "kneser": [
        "Dedicated Kneser working-edition split from the mixed additional-author shelf. Current public coverage fronts German-source and English working-translation reader PDF/TeX surfaces through p0011-p0248, a high-quality source witness through p0001-p0248, and the p0234 lower-p0248 slice/audit package. The included worklist reports 248/336 source pages done (73.8 percent), latest slice sections 53-55 completing the Sixth Section, and next continuation at p0249 / Seventh Section / section 56. This is a source-witnessed working draft and audit/progress record, not a certified critical edition.",
    ],
    "serre": [
        "Dedicated Serre working-transcription record. FAC is directly readable as a 54-page French working reader covering 70 of 82 printed source pages; the twelve exact gaps remain disclosed. The direct master and body TeX accompany one compact 14-member FAC source/evidence ZIP containing four actual scan-derived crops with exact page, rasterization, bounding-box, dimension, and hash provenance. A separate eight-member ZIP preserves the complete first-pass GAGA TeX source; its earlier PDF remains held because visible join sentinels are still present. License metadata is License Not Specified. This is partial/first-pass scholarly custody, not complete Serre works, a critical edition, mathematical certification, accessibility certification, or blanket rights clearance.",
    ],
    "lean_formalization_sidecars": [
        "Small Lean 4 / Mathlib-style sidecar record for useful formalization/library-candidate material connected to the historical transcription and translation archive. These files are not source-fidelity evidence, not translation certification, not scanned-edition certification, and not critical-edition material.",
    ],
    "split_zero_research_sidecar": [
        "Separate exploratory mathematics sidecar, outside the manuscript-translation completion ranking. Current version 21443852 fronts the concise Project Atlas and retains the bookmarked results compendium, Lean/Python checks and ledgers, editable working texts, replayable visualization/data packages, and the bounded N16-N18 predatum/K4/Hopf supplement from predecessor 21426216. It adds the coherent Part 8-C2A through C2F2 finite-glue, shell, triality, and Fricke proof chain. The seven source-free Python replays pass 16/16, 19/19, 16/16, 18/18, 20/20, 11/11, and 19/19 checks; the stated marking, topology, classification, and Niemeier/Fricke boundaries remain explicit. This is a working research record, not peer review, a proof of a famous open problem, or certification of every broader claim.",
    ],
    "deligne": [
        "Current reader-first surface is version 21212608. It directly exposes the sequential English and French working readers through Papers 001-016p080 and groups individual paper/letter PDFs and the TeX/source/QA material into four archives. These are uneven working drafts and repair material, not a critical edition or blanket source-faithfulness claim; diagram-heavy and equation-dense pieces still require direct source comparison.",
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
        "Methodology, source-body, provenance, corpus-control, and bounded-output sidecar for mathematical translation. Current version 21485338 retains the full numbered v0.13 archive and adds the CJK visual-evidence checkpoint: 290 open project-generated or project-recovered images, six public-safe controls, and metadata-only representation of 14 rights-blocked images. The index also records 1,716 excluded non-project images, 49 metadata-incomplete records, and one inherited undecodable PNG. Parent and structural links remain candidates unless explicitly confirmed. These are model-built methodology, normalization, corpus, bounded working-translation, provenance, and visual-QA artifacts, not native validation, translation or source-fidelity certification, rights clearance, community certification, peer review, or critical editions.",
    ],
    "additional_author_cluster": [
        "Mixed selected-author shelf. This remains a backstop/provenance shelf for authors not yet split into full standalone records and for older routed packets. Kneser now has a preferred standalone record at concept DOI `10.5281/zenodo.20836971`; earlier Kneser packets in this shelf remain provenance/backstop. Poincare and Frobenius also have preferred standalone records. Treat this shelf package by package, not as a blanket certification of every included author.",
    ],
}

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
    "serre": "Jean-Pierre Serre: FAC Partial French Working Transcription and GAGA TeX Source Custody",
    "lean_formalization_sidecars": "Classical Mathematics Lean 4 Formalization Sidecars",
    "interlanguage_reflections": "Interlanguage and Mathematical Translation Methodology Sidecar",
    "split_zero_research_sidecar": "Split-Zero Geometry and Common Deformation Registers: Project Atlas, Exact Results, Formalization, and Visualizations",
}


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
        except (HTTPError, URLError, TimeoutError):
            if attempt == 7:
                raise
            print(
                f"Retrying Zenodo record {record_id} after API failure "
                f"({attempt + 1}/8)",
                file=sys.stderr,
            )
            time.sleep(2 ** attempt)
    raise AssertionError("unreachable")


def fetch_selected_preview(record_id: str) -> str:
    url = f"https://zenodo.org/records/{record_id}"
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "modern-latex-manuscripts-catalog/1.0"},
    )
    for attempt in range(8):
        try:
            with urllib.request.urlopen(request, timeout=120) as response:
                page = response.read().decode("utf-8", errors="replace")
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


def build_rows() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for label, record_id in RECORDS:
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
        for row in group:
            filename = row["filename"]
            lines.append(
                f"| {row['file_role']} | {row['size_mb']} | [{html.escape(filename)}]({row['url']}) |"
            )
        lines.append("")

    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    root = Path.cwd()
    rows = build_rows()
    write_csv(rows, root / "manifests" / "public-file-catalog.csv")
    write_current_records(rows, root / "manifests" / "zenodo-records-current.json")
    write_markdown(rows, root / "docs" / "public-file-catalog.md")
    print(f"Indexed {len(rows)} public files from {len(RECORDS)} records.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
