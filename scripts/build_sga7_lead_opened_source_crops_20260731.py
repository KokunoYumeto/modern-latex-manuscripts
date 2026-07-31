#!/usr/bin/env python3
"""Build the deduplicated SGA7 lead-opened source-crop package."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image


SGA7I_PARENT = {
    "title": "SGA 7 I public scan",
    "pages": 540,
    "sha256": "9CD40FF06EB1E488AF385A56899D4F492492A06A1E2E3C0ED6876B82E3E3603F",
}
SGA7II_PARENT = {
    "title": "SGA 7 II / LNM 340 public Number12 scan",
    "pages": 446,
    "sha256": "FA679DEBFC8ADA3232D7E752A1837FC6CE474488E20A44D7641CF296876E1297",
}

INDEX_BACKED_SGA7I = (
    "p12.png",
    "p15.png",
    "p165.png",
    "p166.png",
    "p170.png",
    "p241.png",
    "p352.png",
    "p52.png",
    "r112_full.png",
    "r172_full.png",
    "z329_all.png",
    "z329_lower.png",
    "z48_leftdiamond.png",
    "z48b_middlerow.png",
)

MANUAL = {
    "z52_seq.png": {
        "work": "SGA7I",
        "page0": 52,
        "physical": 53,
        "folio": 41,
        "expose": "VI",
        "linked_tex": "expose_VI_body.tex",
        "bbox": (0.10, 0.596, 0.95, 0.632),
        "dpi": 7000,
        "purpose": "surjective-map sequence and arrowhead adjudication",
    },
    "z52b_seq.png": {
        "work": "SGA7I",
        "page0": 52,
        "physical": 53,
        "folio": 41,
        "expose": "VI",
        "linked_tex": "expose_VI_body.tex",
        "bbox": (0.10, 0.575, 0.95, 0.612),
        "dpi": 7000,
        "purpose": "surjective-map sequence and final connector adjudication",
    },
    "z52b_alpha.png": {
        "work": "SGA7I",
        "page0": 52,
        "physical": 53,
        "folio": 41,
        "expose": "VI",
        "linked_tex": "expose_VI_body.tex",
        "bbox": (0.10, 0.628, 0.95, 0.665),
        "dpi": 7000,
        "purpose": "alpha and phi subscript adjudication",
    },
    "z52c_alpha.png": {
        "work": "SGA7I",
        "page0": 52,
        "physical": 53,
        "folio": 41,
        "expose": "VI",
        "linked_tex": "expose_VI_body.tex",
        "bbox": (0.03, 0.626, 0.55, 0.660),
        "dpi": 8000,
        "purpose": "alpha and phi subscript adjudication",
    },
    "z52c_ii.png": {
        "work": "SGA7I",
        "page0": 52,
        "physical": 53,
        "folio": 41,
        "expose": "VI",
        "linked_tex": "expose_VI_body.tex",
        "bbox": (0.03, 0.733, 0.55, 0.768),
        "dpi": 8000,
        "purpose": "part (ii) notation and A-hat styling adjudication",
    },
    "z52d_ii.png": {
        "work": "SGA7I",
        "page0": 52,
        "physical": 53,
        "folio": 41,
        "expose": "VI",
        "linked_tex": "expose_VI_body.tex",
        "bbox": (0.03, 0.706, 0.75, 0.742),
        "dpi": 8000,
        "purpose": "part (ii) notation and A-hat styling adjudication",
    },
    "z360_cas.png": {
        "work": "SGA7I",
        "page0": 360,
        "physical": 361,
        "folio": 349,
        "expose": "IX",
        "linked_tex": "expose_IX_body.tex",
        "bbox": (0.05, 0.735, 0.95, 0.775),
        "dpi": 8000,
        "purpose": "case distinction wording adjudication",
    },
    "z360b_cas.png": {
        "work": "SGA7I",
        "page0": 360,
        "physical": 361,
        "folio": 349,
        "expose": "IX",
        "linked_tex": "expose_IX_body.tex",
        "bbox": (0.05, 0.680, 0.95, 0.716),
        "dpi": 8000,
        "purpose": "case distinction wording adjudication",
    },
    "z360c_cas.png": {
        "work": "SGA7I",
        "page0": 360,
        "physical": 361,
        "folio": 349,
        "expose": "IX",
        "linked_tex": "expose_IX_body.tex",
        "bbox": (0.05, 0.648, 0.95, 0.692),
        "dpi": 8000,
        "purpose": "case-S-or wording adjudication",
    },
    "chk_faisceaux.png": {
        "work": "SGA7II",
        "page0": 9,
        "physical": 10,
        "folio": 2,
        "expose": "X",
        "linked_tex": "expose_X_body.tex",
        "bbox": (0.06, 0.300, 0.96, 0.345),
        "dpi": 7000,
        "purpose": "coherent-sheaf wording disagreement adjudication",
    },
    "chk_faisceaux2.png": {
        "work": "SGA7II",
        "page0": 9,
        "physical": 10,
        "folio": 2,
        "expose": "X",
        "linked_tex": "expose_X_body.tex",
        "bbox": (0.06, 0.330, 0.96, 0.395),
        "dpi": 7000,
        "purpose": "coherent-sheaf wording disagreement adjudication",
    },
    "chk_disjoint.png": {
        "work": "SGA7II",
        "page0": 11,
        "physical": 12,
        "folio": 4,
        "expose": "X",
        "linked_tex": "expose_X_body.tex",
        "bbox": (0.06, 0.150, 0.96, 0.205),
        "dpi": 7000,
        "purpose": "disjointness wording disagreement adjudication",
    },
    "sga7ii_idx120_500dpi_c0.25-0.62.png": {
        "work": "SGA7II",
        "page0": 120,
        "physical": 121,
        "folio": 113,
        "expose": "XIII",
        "linked_tex": "expose_XIII_body.tex",
        "bbox": (0.0, 0.25, 1.0, 0.62),
        "dpi": 500,
        "purpose": "lead-opened source region used during transcription",
    },
    "sga7ii_idx122_500dpi_c0.08-0.3.png": {
        "work": "SGA7II",
        "page0": 122,
        "physical": 123,
        "folio": 115,
        "expose": "XIII",
        "linked_tex": "expose_XIII_body.tex",
        "bbox": (0.0, 0.08, 1.0, 0.30),
        "dpi": 500,
        "purpose": "lead-opened source region used during transcription",
    },
    "idx158_300dpi_crop0.0-0.5.png": {
        "work": "SGA7II",
        "page0": 158,
        "physical": 159,
        "folio": 151,
        "expose": "XIV",
        "linked_tex": "expose_XIV_body.tex",
        "bbox": (0.0, 0.0, 1.0, 0.5),
        "dpi": 300,
        "purpose": "lead-opened half-page source context used during transcription",
    },
}

EXACT_PUBLIC_DUPLICATES = {
    "z112_overk.png": "10x_SGA7I_SourceAudit_Opened_Targeted_Crops_20260730.zip",
    "z112_overk2.png": "10x_SGA7I_SourceAudit_Opened_Targeted_Crops_20260730.zip",
    "z329_bottom.png": "10x_SGA7I_SourceAudit_Opened_Targeted_Crops_20260730.zip",
    "idx535_hard.png": "10h_SGA7II_SourceAudit_Number12_HighDetail_Crops_20260731.zip",
}

TARGET_RENDERS = ("mine_p22.png", "mine_p87.png")
FAC_IMAGES = (
    "fac_idx1_300dpi_c0.0-0.42.png",
    "fac_idx1_900dpi_c0.045-0.1.png",
    "fac_idx3_600dpi_c0.05-0.32.png",
    "fac_idx3_600dpi_c0.6-0.85.png",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def read_events(transcript: Path) -> dict[str, list[str]]:
    events: dict[str, list[str]] = defaultdict(list)
    with transcript.open("r", encoding="utf-8") as handle:
        for raw in handle:
            if '"name":"Read"' not in raw or '.png' not in raw:
                continue
            record = json.loads(raw)
            timestamp = record.get("timestamp", "")
            for item in record.get("message", {}).get("content", []):
                if item.get("type") != "tool_use" or item.get("name") != "Read":
                    continue
                name = Path(item.get("input", {}).get("file_path", "")).name
                if name.lower().endswith(".png"):
                    events[name].append(timestamp)
    return events


def load_index(path: Path) -> dict[str, dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return {row["sha256"].upper(): row for row in csv.DictReader(handle)}


def collect_public_hashes(paths: tuple[Path, ...]) -> set[str]:
    hashes: set[str] = set()

    def walk(value: object) -> None:
        if isinstance(value, dict):
            digest = value.get("sha256")
            if isinstance(digest, str) and len(digest) == 64:
                hashes.add(digest.upper())
            for child in value.values():
                walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)

    for path in paths:
        walk(json.loads(path.read_text(encoding="utf-8")))
    return hashes


def image_info(path: Path) -> tuple[int, int, str]:
    with Image.open(path) as image:
        return image.width, image.height, image.mode


def find_file(name: str, roots: tuple[Path, ...]) -> Path:
    matches = [root / name for root in roots if (root / name).is_file()]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one source for {name}, found {matches}")
    return matches[0]


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--historical-root", type=Path, required=True)
    parser.add_argument("--current-root", type=Path, required=True)
    parser.add_argument("--transcript", type=Path, required=True)
    parser.add_argument("--existing-index", type=Path, required=True)
    parser.add_argument("--public-readback", type=Path, action="append", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    output = args.output.resolve()
    if output.exists():
        shutil.rmtree(output)
    (output / "images").mkdir(parents=True)

    roots = (args.historical_root.resolve(), args.current_root.resolve())
    events = read_events(args.transcript.resolve())
    index_by_sha = load_index(args.existing_index.resolve())
    public_hashes = collect_public_hashes(
        tuple(path.resolve() for path in args.public_readback)
    )
    rows: list[dict[str, object]] = []

    for sequence, name in enumerate((*INDEX_BACKED_SGA7I, *MANUAL.keys()), start=1):
        source = find_file(name, roots)
        digest = sha256(source)
        if digest in public_hashes:
            raise RuntimeError(f"New package image is already public: {name} / {digest}")
        width, height, mode = image_info(source)

        if name in INDEX_BACKED_SGA7I:
            existing = index_by_sha.get(digest)
            if not existing:
                raise RuntimeError(f"No exact SGA7I index row for {name} / {digest}")
            metadata = {
                "work": "SGA7I",
                "page0": existing["parent_pdf_index_0based"],
                "physical": existing["parent_pdf_physical_page_1based"],
                "folio": existing["book_folio"],
                "expose": existing["expose"],
                "linked_tex": existing["linked_tex_file"],
                "bbox": (
                    existing["bbox_fx0"],
                    existing["bbox_fy0"],
                    existing["bbox_fx1"],
                    existing["bbox_fy1"],
                ),
                "dpi": existing["render_parameter"],
                "purpose": existing["qa_disposition"],
                "prior_visual_id": existing["visual_id"],
            }
        else:
            metadata = dict(MANUAL[name])
            metadata["prior_visual_id"] = ""

        parent = SGA7I_PARENT if metadata["work"] == "SGA7I" else SGA7II_PARENT
        member = f"images/{metadata['work']}_{name}"
        destination = output / member
        shutil.copy2(source, destination)
        if sha256(destination) != digest:
            raise RuntimeError(f"Copy mismatch for {name}")

        times = events.get(name, [])
        bbox = metadata["bbox"]
        rows.append(
            {
                "visual_id": f"SGA7-LEAD-{sequence:03d}",
                "work": metadata["work"],
                "expose": metadata["expose"],
                "parent_scan_title": parent["title"],
                "parent_pdf_sha256": parent["sha256"],
                "parent_pdf_pages": parent["pages"],
                "parent_pdf_index_0based": metadata["page0"],
                "physical_pdf_page_1based": metadata["physical"],
                "book_folio": metadata["folio"],
                "bbox_fx0": bbox[0],
                "bbox_fy0": bbox[1],
                "bbox_fx1": bbox[2],
                "bbox_fy1": bbox[3],
                "render_dpi": metadata["dpi"],
                "width_px": width,
                "height_px": height,
                "color_mode": mode,
                "bytes": source.stat().st_size,
                "sha256": digest,
                "original_filename": name,
                "archive_member": member,
                "linked_tex_file": metadata["linked_tex"],
                "qa_disposition": "lead_opened_source_evidence",
                "source_check_purpose": metadata["purpose"],
                "read_count": len(times),
                "first_read_timestamp_utc": min(times) if times else "",
                "last_read_timestamp_utc": max(times) if times else "",
                "prior_visual_id": metadata["prior_visual_id"],
                "publication_disposition": "public_actual_pixel_deduplicated",
            }
        )

    index_fields = list(rows[0].keys())
    write_csv(output / "SGA7_LEAD_OPENED_SOURCE_CROP_INDEX.csv", rows, index_fields)

    exclusions: list[dict[str, object]] = []
    for name, archive in EXACT_PUBLIC_DUPLICATES.items():
        source = find_file(name, roots)
        exclusions.append(
            {
                "filename": name,
                "bytes": source.stat().st_size,
                "sha256": sha256(source),
                "disposition": "excluded_exact_pixel_already_public",
                "reason": archive,
            }
        )
    for name in TARGET_RENDERS:
        source = find_file(name, roots)
        exclusions.append(
            {
                "filename": name,
                "bytes": source.stat().st_size,
                "sha256": sha256(source),
                "disposition": "excluded_target_reader_render",
                "reason": "not source-scan evidence",
            }
        )
    for name in FAC_IMAGES:
        source = find_file(name, roots)
        exclusions.append(
            {
                "filename": name,
                "bytes": source.stat().st_size,
                "sha256": sha256(source),
                "disposition": "routed_to_serre_fac_work",
                "reason": "different work and publication line",
            }
        )
    write_csv(
        output / "DEDUPLICATION_AND_ROUTING.csv",
        exclusions,
        ["filename", "bytes", "sha256", "disposition", "reason"],
    )

    readme = """# SGA7 lead-opened source-image crops

This package publishes 29 actual source-scan-derived PNGs that were opened by
the lead during SGA7 I and SGA7 II transcription checks and were not already
public by exact SHA-256. It contains 23 SGA7 I images and six SGA7 II images.

The images preserve useful page, formula, arrow, symbol, and wording evidence.
They are not screenshots of the English readers. Four exact pixels already in
the current SGA visual archives are excluded, as are two target-reader renders.
Four Serre FAC source crops are routed separately because they belong to a
different work.

`SGA7_LEAD_OPENED_SOURCE_CROP_INDEX.csv` records the parent-scan hash, scan
page, physical page, folio, Expose, fractional crop box where recovered,
render DPI, dimensions, image hash, linked TeX unit, read timestamps, and QA
purpose. Empty crop or DPI fields mean that the earlier generator parameters
were not recovered; the exact pixel and parent-page identity remain recorded.

These are transcription/source-adjudication witnesses. They do not certify a
complete SGA7 transcription, translation, proof, critical edition, or every
possible source reading.
"""
    rights = """# Rights and provenance

The two parent scans are publicly available scholarly scans. This successor
publishes the actual derived crop pixels used in transcription checks rather
than replacing them with a metadata-only rights-blocked ledger.

Parent identities:

- SGA7 I public scan: 540 pages, SHA-256
  `9CD40FF06EB1E488AF385A56899D4F492492A06A1E2E3C0ED6876B82E3E3603F`.
- SGA7 II / LNM 340 public Number12 scan: 446 pages, SHA-256
  `FA679DEBFC8ADA3232D7E752A1837FC6CE474488E20A44D7641CF296876E1297`.

Publication of these derived working crops does not assert ownership of the
underlying French work or invent a blanket license for the scans. Attribution
and any applicable underlying rights remain with their respective holders.
The parent PDFs are not duplicated in this package.
"""
    readiness = """# Publication readiness

Status: ready for public archival release as deduplicated source-image
evidence.

- actual source-derived PNGs: 29
- exact already-public pixels excluded: 4
- target-reader renders excluded: 2
- unrelated Serre FAC crops routed separately: 4
- private absolute paths in public text: 0

The package is source evidence, not completion or mathematical certification.
"""
    (output / "README.md").write_text(readme, encoding="utf-8", newline="\n")
    (output / "RIGHTS_AND_PROVENANCE.md").write_text(
        rights, encoding="utf-8", newline="\n"
    )
    (output / "PUBLICATION_READINESS.md").write_text(
        readiness, encoding="utf-8", newline="\n"
    )
    (output / ".gitattributes").write_text(
        "*.png binary\n*.csv text eol=lf\n*.md text eol=lf\n*.json text eol=lf\n",
        encoding="ascii",
        newline="\n",
    )

    checksum_files = sorted(
        path for path in output.rglob("*") if path.is_file() and path.name != "SHA256SUMS.csv"
    )
    checksum_rows = [
        {
            "relative_path": path.relative_to(output).as_posix(),
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        }
        for path in checksum_files
    ]
    write_csv(
        output / "SHA256SUMS.csv",
        checksum_rows,
        ["relative_path", "bytes", "sha256"],
    )

    text_blob = "\n".join(
        path.read_text(encoding="utf-8", errors="replace")
        for path in output.rglob("*")
        if path.is_file() and path.suffix.lower() in {".md", ".csv", ".json", ""}
    )
    forbidden = ("C:\\Users\\", "AppData\\Local\\Temp", "a6fe6ef4-", "9d1d4bc3-")
    privacy_hits = [pattern for pattern in forbidden if pattern in text_blob]
    image_bytes = sum((output / row["archive_member"]).stat().st_size for row in rows)
    validation = {
        "status": "PASS",
        "errors": [],
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "package_files_excluding_validation": len(checksum_rows) + 1,
        "image_files": len(rows),
        "image_bytes": image_bytes,
        "work_counts": {
            "SGA7I": sum(row["work"] == "SGA7I" for row in rows),
            "SGA7II": sum(row["work"] == "SGA7II" for row in rows),
        },
        "deduplication": {
            "public_baseline_hashes_compared": len(public_hashes),
            "new_image_hash_overlaps": 0,
            "exact_already_public_excluded": len(EXACT_PUBLIC_DUPLICATES),
            "target_reader_renders_excluded": len(TARGET_RENDERS),
            "serre_fac_images_routed_separately": len(FAC_IMAGES),
        },
        "read_event_rows": sum(bool(row["read_count"]) for row in rows),
        "manifest_rows": len(checksum_rows),
        "privacy_hits": privacy_hits,
        "parent_scans": [SGA7I_PARENT, SGA7II_PARENT],
    }
    if privacy_hits or len(rows) != 29 or validation["read_event_rows"] != 29:
        validation["status"] = "FAIL"
        validation["errors"].append("count_or_privacy_gate_failed")
    (output / "PACKAGE_VALIDATION.json").write_text(
        json.dumps(validation, indent=2) + "\n", encoding="utf-8", newline="\n"
    )
    if validation["status"] != "PASS":
        raise RuntimeError(validation)


if __name__ == "__main__":
    main()
