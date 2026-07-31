#!/usr/bin/env python3
"""Build the EGA IV printed 282-332 source-image witness ZIP."""

from __future__ import annotations

import json
from pathlib import Path

import build_ega4_sections19_21_source_image_witness_p226_281_zip_20260731 as prior


PART = {
    "minimum": 282,
    "maximum": 332,
    "aligned_through": 332,
    "alignment_checkpoint": "build_final_source_aligned_r2",
    "linked_tex_unit": "source/source_aligned/ega4-21.tex",
    "filename": (
        "89d EGA IV - Source Image Witnesses Printed 282-332 "
        "(1800dpi) 20260731.zip"
    ),
    "root": "EGA4_Source_Image_Witnesses_Printed282_332_20260731",
}

prior.PART = PART
prior.prior.PART = PART
prior.prior.base.PART = PART


def build_rows(source_root: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for start, finish in (
        (282, 286),
        (287, 291),
        (292, 296),
        (297, 301),
        (302, 306),
        (307, 311),
        (312, 316),
        (317, 321),
        (322, 326),
        (327, 331),
        (332, 336),
    ):
        directory = source_root / f"IV4_printed{start:03d}_{finish:03d}_1800dpi"
        upper = min(finish, int(PART["maximum"]))
        for printed in range(start, upper + 1):
            prior.add_full_page(
                rows,
                source_root,
                directory / f"source-{printed - 1}.png",
                printed,
            )

    rows.sort(key=lambda row: str(row["entry_path"]).casefold())
    if len(rows) != 51:
        raise RuntimeError(f"Expected 51 source witnesses, found {len(rows)}")
    pages = sorted(int(row["printed_page"]) for row in rows)
    if pages != list(range(282, 333)):
        raise RuntimeError(f"Printed-page witness closure changed: {pages}")
    hashes = [str(row["sha256"]) for row in rows]
    if len(hashes) != len(set(hashes)):
        raise RuntimeError("Duplicate source-image bytes entered the new archive")
    return rows


def archive_readme(rows: list[dict[str, object]]) -> bytes:
    text = f"""# EGA IV source-image witnesses: printed pages 282-332

This ZIP preserves {len(rows)} PNG witnesses / {sum(int(row['bytes']) for row in rows):,} bytes
derived from the publicly available 360-page NUMDAM EGA IV Part 4 scan.
The parent scan SHA-256 is `{prior.prior.base.PARENT_SHA256}` and the parent
scan is directly downloadable from the same EGA Zenodo concept.

The set contains one 1,800-dpi full-page source render for every printed page
282-332. Every image is bound to physical/printed page, dimensions,
resolution, bytes/SHA-256, linked editable TeX, and QA disposition in
`VISUAL_EVIDENCE_INDEX.csv` and `.jsonl`.

The images were used by the source-alignment lane through the end of Section
21. They remain source witnesses rather than a claim that a cumulative EGA IV
Sections 1-21 reader has been integrated or independently certified. Printed
pages 333-335 are deliberately excluded because they are beyond this bounded
Sections 19-21 stop.

This is source-image evidence, not screenshots of the English reader PDF. No
OCR body, private path, raw build log, script, cache, or conversation is
included. Publication does not alter rights or attribution in the underlying
work.
"""
    return text.encode("utf-8")


def write_metadata(
    metadata_root: Path, rows: list[dict[str, object]], archive: dict[str, object]
) -> None:
    metadata_root.mkdir(parents=True, exist_ok=True)
    (metadata_root / ".gitattributes").write_bytes(b"* -text\n")
    public_rows = [prior.prior.base.public_row(row) for row in rows]
    (metadata_root / "VISUAL_EVIDENCE_INDEX.csv").write_bytes(
        prior.prior.base.csv_bytes(public_rows, prior.prior.base.INDEX_FIELDS)
    )
    (metadata_root / "VISUAL_EVIDENCE_INDEX.jsonl").write_bytes(
        prior.prior.base.jsonl_bytes(public_rows)
    )
    (metadata_root / "ZIP_PAYLOAD_MANIFEST.csv").write_bytes(
        prior.prior.base.csv_bytes([archive], tuple(archive))
    )
    (metadata_root / "README.md").write_text(
        "# EGA IV Sections 19-21 source-image witnesses, printed 282-332\n\n"
        f"This metadata binds the actual {len(rows)} scan-derived PNGs in "
        f"`{PART['filename']}`. All pages are linked to the final source-"
        "alignment build for the bounded Sections 19-21 lane. English-reader "
        "renders and printed pages beyond 332 are not included.\n",
        encoding="utf-8",
        newline="\n",
    )
    validation = {
        "status": "PASS_READY_FOR_SAME_CONCEPT_ZENODO_UPLOAD",
        "images": len(rows),
        "image_bytes": sum(int(row["bytes"]) for row in rows),
        "printed_page_min": int(PART["minimum"]),
        "printed_page_max": int(PART["maximum"]),
        "aligned_through_printed_page": int(PART["aligned_through"]),
        "parent_scan_sha256": prior.prior.base.PARENT_SHA256,
        "zip_archive": archive,
        "privacy_hits": 0,
        "duplicate_image_hashes": 0,
        "errors": [],
    }
    (metadata_root / "VALIDATION.json").write_text(
        json.dumps(validation, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    represented = sorted(
        path
        for path in metadata_root.iterdir()
        if path.is_file() and path.name != "SHA256SUMS.csv"
    )
    sums_rows = [
        {
            "path": path.name,
            "bytes": path.stat().st_size,
            "sha256": prior.prior.base.sha256_path(path),
        }
        for path in represented
    ]
    (metadata_root / "SHA256SUMS.csv").write_bytes(
        prior.prior.base.csv_bytes(sums_rows, ("path", "bytes", "sha256"))
    )


def main() -> None:
    parser = prior.prior.argparse.ArgumentParser()
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--zip-output", type=Path, required=True)
    parser.add_argument("--metadata-output", type=Path, required=True)
    args = parser.parse_args()
    args.zip_output.mkdir(parents=True, exist_ok=True)
    rows = build_rows(args.source_root)
    prior.prior.base.readme = archive_readme
    archive = prior.prior.base.build_zip(args.zip_output, rows)
    write_metadata(args.metadata_output, rows, archive)
    print(json.dumps({"status": "PASS", "images": len(rows), "zip": archive}, indent=2))


if __name__ == "__main__":
    main()
