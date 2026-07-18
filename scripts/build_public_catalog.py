#!/usr/bin/env python3
"""Build the public Zenodo file catalog for this repository.

This script uses only the public Zenodo records API. It does not need a token.
Run it from the repository root:

    python scripts/build_public_catalog.py

Outputs:
    manifests/public-file-catalog.csv
    docs/public-file-catalog.md
"""

from __future__ import annotations

import csv
import html
import json
import re
import sys
import urllib.request
from pathlib import Path
from typing import Any


RECORDS: list[tuple[str, str]] = [
    ("main", "20459634"),
    ("workflow", "21424987"),
    ("interlanguage_reflections", "21430885"),
    ("lean_formalization_sidecars", "21129946"),
    ("split_zero_research_sidecar", "21426216"),
    ("noether", "21431458"),
    ("weber", "21402223"),
    ("cayley", "20617845"),
    ("sga", "21431041"),
    ("deligne", "21212608"),
    ("ega", "20454552"),
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
    ("additional_author_cluster", "20672984"),
]

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
        "Current SGA public surface is record 21431041. It fronts the replacement 309-page SGA5 English source-synchronized working reader and compact 54-file scan-free support package; the exact scope is ten curated exposes through printed p.480 plus the index through p.484. Printed p.14 carries an editorial defect note and the p.43 ambiguity remains explicitly unresolved. The record retains the four-page English SGA1 Expose I opening/section I.1 checkpoint, corrected 381-page layered SGA6 English reader, 374-page French SGA6 idx684 checkpoint, and bounded Spanish SGA6 Expose X idx532-537 tranche. The privacy-defective historical SGA6 support ZIP remains withdrawn, and historical Spanish SGA5 checkpoints remain non-current. These are substantive working editions, translations, and source-audit checkpoints, not complete translations, independently human-certified critical editions, rights determinations, uniform whole-volume source certification, diagram-by-diagram certification, or whole-SGA completion.",
    ],
    "weber": [
        "Current Weber public surface is record 21402223. The active Volume I German p1-p99 direct content-fidelity pass reaches printed p88, with p89 next. Its p77-p88 evidence package contains the current TeX/PDF, exact diff, ledgers, twelve source pages, high-resolution crops, render checks, and checksums; it rebuilds the damaged section 23 and restores omitted displays, rows, proof text, labels, and notation. The Volume I English reader predates these German repairs and is explicitly unsynchronized. Volume II retains current German/English cumulative material through section 176 plus repair packets; Volume III remains the current repaired cumulative. This is source-witnessed working material, not whole-volume symbol-by-symbol certification, synchronized English, publication-grade proofreading, or a critical edition.",
    ],
    "noether": [
        "Current Noether update 2026-07-18: latest public surface is record 21431458. It retains the German R823 source-control corpus; directly exposes the English, 473-page Spanish, 494-page French, 527-page Latin-script Interslavic, and 551-page Cyrillic-script Interslavic readers; and carries bounded CJK/Korean, Slavic, Arabic/Persian, and Indonesian work. The English cumulative reader remains the default preview. This version adds a source-audited English Paper 3 checkpoint; Korean Paper 27; Paper 28 in Simplified Chinese, controlled generic Traditional Chinese, Japanese, and Korean; Paper 29 in Simplified Chinese and controlled generic Traditional Chinese; and a grouped editable-source/evidence package. File `17` preserves 3,024 unique French, Spanish, and Interslavic render/review images not already present by exact hash in prior evidence packages, with a complete machine-readable index. File `11` contains all 442 current Interslavic editable units and unit PDFs plus normalization Tranches 002A-007 and the final 221-unit Latin-corpus audit; 353 `važi*|važe*` mathematical sense-extension probes in 101 files remain an external-authority blocker. File `15` retains the bounded German Paper 30 hard-math source-control supplement, and file `14` retains the exact French TeX/evidence closure. These are source-control working editions, translations, and render witnesses, not native-language certification, peer review, proof checking, whole-corpus source certification, universal symbol accuracy, complete multilingual synchronization, or a critical edition.",
    ],
    "kneser": [
        "Dedicated Kneser working-edition split from the mixed additional-author shelf. Current public coverage fronts German-source and English working-translation reader PDF/TeX surfaces through p0011-p0248, a high-quality source witness through p0001-p0248, and the p0234 lower-p0248 slice/audit package. The included worklist reports 248/336 source pages done (73.8 percent), latest slice sections 53-55 completing the Sixth Section, and next continuation at p0249 / Seventh Section / section 56. This is a source-witnessed working draft and audit/progress record, not a certified critical edition.",
    ],
    "lean_formalization_sidecars": [
        "Small Lean 4 / Mathlib-style sidecar record for useful formalization/library-candidate material connected to the historical transcription and translation archive. These files are not source-fidelity evidence, not translation certification, not scanned-edition certification, and not critical-edition material.",
    ],
    "split_zero_research_sidecar": [
        "Separate exploratory mathematics sidecar, outside the manuscript-translation completion ranking. Version 21426216 retains the Project Atlas as its default preview, the bookmarked results compendium, Lean/Python checks and ledgers, editable working texts, replayable visualization/data packages, and the Part 8-C2B residual-Niemeier audit. It adds one bounded N16-N18 predatum/K4/Hopf working-note and executable-check supplement. Its four script groups reran at 12/12, 17/17, 10/10, and 12/12 encoded checks; external topos, bundle-classification, cited-topology, and referee-recorded numeric steps remain explicitly outside that machine rerun. This is a working research record, not peer review, a proof of a famous open problem, or certification of every broader claim.",
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
        "Methodology, source-body, provenance, corpus-control, and bounded-output sidecar for mathematical translation. Current version 21430885 fronts the v0.13 five-page archive map, retains the full numbered source-body, weighted-automata, terminology, manager-fleet, Romance v10, Interslavic, and Noether R823-gate layers, and adds organized Romance corpus/WordWeb/governance/T008 and Interslavic-through-Tranche-007 checkpoints. WordWeb records 60 concepts, 106 senses, 954 access rows, and 28 explicit gaps; controlled Romance continues at German R823 line 21309. These are model-built methodology, normalization, corpus, and bounded working-translation artifacts, not native validation, human intelligibility evidence, rights clearance, community certification, peer review, or critical editions.",
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
    "lean_formalization_sidecars": "Classical Mathematics Lean 4 Formalization Sidecars",
    "interlanguage_reflections": "Interlanguage and Mathematical Translation Methodology Sidecar",
    "split_zero_research_sidecar": "Split-Zero Geometry and Common Deformation Registers: Project Atlas, Exact Results, Formalization, and Visualizations",
}


def fetch_record(record_id: str) -> dict[str, Any]:
    url = f"https://zenodo.org/api/records/{record_id}"
    with urllib.request.urlopen(url, timeout=60) as response:
        return json.loads(response.read().decode("utf-8"))


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


def build_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for label, record_id in RECORDS:
        record = fetch_record(record_id)
        actual_record_id = str(record.get("id", record_id))
        title = TITLE_OVERRIDES.get(label, record.get("metadata", {}).get("title", ""))
        for item in sorted(record.get("files", []), key=lambda value: value.get("key", "").lower()):
            filename = item.get("key", "")
            size_mb = float(item.get("size", 0)) / (1024 * 1024)
            rows.append(
                {
                    "record_label": label,
                    "record_id": actual_record_id,
                    "record_title": title,
                    "file_role": file_role(filename),
                    "filename": filename,
                    "size_mb": f"{size_mb:.4f}",
                    "url": file_url(actual_record_id, filename),
                }
            )
    return rows


def write_csv(rows: list[dict[str, str]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "record_label",
                "record_id",
                "record_title",
                "file_role",
                "filename",
                "size_mb",
                "url",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)


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


def write_markdown(rows: list[dict[str, str]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    grouped: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        grouped.setdefault(row["record_label"], []).append(row)

    root = path.parent.parent
    concept_urls = load_concept_urls(root)

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
    write_markdown(rows, root / "docs" / "public-file-catalog.md")
    print(f"Indexed {len(rows)} public files from {len(RECORDS)} records.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
