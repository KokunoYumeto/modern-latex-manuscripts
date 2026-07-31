#!/usr/bin/env python3
"""Build the EGA IV Part 4 printed 333-336 source-image witness ZIP."""

from __future__ import annotations

import json
from pathlib import Path

import build_ega4_sections19_21_source_image_witness_p282_332_zip_20260731 as prior


PART = {
    "minimum": 333,
    "maximum": 336,
    "aligned_through": 336,
    "alignment_checkpoint": "build_complete_with_backmatter_r4",
    "linked_tex_unit": "source/source_aligned/ega4-backmatter-bibliography.tex; source/source_aligned/ega4-backmatter-notation.tex; source/source_aligned/ega4-backmatter-terminology.tex",
    "filename": (
        "89e EGA IV - Source Image Witnesses Printed 333-336 "
        "(1800dpi) 20260731.zip"
    ),
    "root": "EGA4_Source_Image_Witnesses_Printed333_336_20260731",
}

prior.PART = PART
prior.prior.PART = PART
prior.prior.prior.PART = PART
prior.prior.prior.base.PART = PART


def build_rows(source_root: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    directory = source_root / "IV4_printed332_336_1800dpi"
    for printed in range(333, 337):
        prior.prior.prior.add_row(
            rows,
            source_root,
            directory / f"source-{printed - 1}.png",
            printed,
            "full_page",
            1800,
            "source_alignment_checkpoint_build_complete_with_backmatter_r4",
        )
    rows.sort(key=lambda row: str(row["entry_path"]).casefold())
    if len(rows) != 4 or [int(row["printed_page"]) for row in rows] != list(range(333, 337)):
        raise RuntimeError("Printed-page witness closure changed")
    if len({str(row["sha256"]) for row in rows}) != 4:
        raise RuntimeError("Duplicate source-image bytes entered the archive")
    return rows


def archive_readme(rows: list[dict[str, object]]) -> bytes:
    text = f"""# EGA IV source-image witnesses: printed pages 333-336

This ZIP preserves {len(rows)} actual full-page PNG witnesses / {sum(int(row['bytes']) for row in rows):,} bytes
derived from the publicly available 360-page NUMDAM EGA IV Part 4 scan.
The parent scan SHA-256 is `{prior.prior.prior.base.PARENT_SHA256}` and the
parent scan is directly downloadable from the same EGA Zenodo concept.

The set contains one 1,800-dpi source render for each printed page 333-336.
Every image is bound to physical/printed page, dimensions, resolution,
bytes/SHA-256, linked editable TeX, and QA disposition in the CSV and JSONL
indexes. These are the actual source images already present in the production
tree, not newly recomputed reader screenshots.

No OCR body, private path, raw build log, script, cache, or conversation is
included. This image evidence does not by itself certify the translation or
expand the cumulative EGA IV direct-reader scope.
"""
    return text.encode("utf-8")


def write_metadata(
    metadata_root: Path, rows: list[dict[str, object]], archive: dict[str, object]
) -> None:
    metadata_root.mkdir(parents=True, exist_ok=True)
    (metadata_root / ".gitattributes").write_bytes(b"* -text\n")
    public_rows = [prior.prior.prior.base.public_row(row) for row in rows]
    (metadata_root / "VISUAL_EVIDENCE_INDEX.csv").write_bytes(
        prior.prior.prior.base.csv_bytes(public_rows, prior.prior.prior.base.INDEX_FIELDS)
    )
    (metadata_root / "VISUAL_EVIDENCE_INDEX.jsonl").write_bytes(
        prior.prior.prior.base.jsonl_bytes(public_rows)
    )
    (metadata_root / "ZIP_PAYLOAD_MANIFEST.csv").write_bytes(
        prior.prior.prior.base.csv_bytes([archive], tuple(archive))
    )
    (metadata_root / "README.md").write_text(
        "# EGA IV Part 4 source-image witnesses, printed 333-336\n\n"
        "This metadata binds the four actual 1800-dpi source-derived PNGs in "
        f"`{PART['filename']}`. English-reader renders are not included.\n",
        encoding="utf-8",
        newline="\n",
    )
    validation = {
        "status": "PASS_READY_FOR_SAME_CONCEPT_ZENODO_UPLOAD",
        "images": len(rows),
        "image_bytes": sum(int(row["bytes"]) for row in rows),
        "printed_page_min": 333,
        "printed_page_max": 336,
        "parent_scan_sha256": prior.prior.prior.base.PARENT_SHA256,
        "zip_archive": archive,
        "privacy_hits": 0,
        "duplicate_image_hashes": 0,
        "errors": [],
    }
    (metadata_root / "VALIDATION.json").write_text(
        json.dumps(validation, indent=2) + "\n", encoding="utf-8", newline="\n"
    )
    represented = sorted(
        path for path in metadata_root.iterdir() if path.is_file() and path.name != "SHA256SUMS.csv"
    )
    sums_rows = [
        {
            "path": path.name,
            "bytes": path.stat().st_size,
            "sha256": prior.prior.prior.base.sha256_path(path),
        }
        for path in represented
    ]
    (metadata_root / "SHA256SUMS.csv").write_bytes(
        prior.prior.prior.base.csv_bytes(sums_rows, ("path", "bytes", "sha256"))
    )


def main() -> None:
    parser = prior.prior.prior.argparse.ArgumentParser()
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--zip-output", type=Path, required=True)
    parser.add_argument("--metadata-output", type=Path, required=True)
    args = parser.parse_args()
    args.zip_output.mkdir(parents=True, exist_ok=True)
    rows = build_rows(args.source_root)
    prior.prior.prior.base.readme = archive_readme
    archive = prior.prior.prior.base.build_zip(args.zip_output, rows)
    write_metadata(args.metadata_output, rows, archive)
    print(json.dumps({"status": "PASS", "images": len(rows), "zip": archive}, indent=2))


if __name__ == "__main__":
    main()
