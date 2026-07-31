#!/usr/bin/env python3
"""Build the EGA IV printed 185-225 high-detail source-image ZIP."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import build_ega4_sections16_18_source_image_witness_p087_105_zip_20260731 as base


PART = {
    "minimum": 185,
    "maximum": 225,
    "aligned_through": 225,
    "alignment_checkpoint": "build_p185_225_r12",
    "linked_tex_unit": "source/source_aligned/ega4-19.tex",
    "filename": (
        "89 EGA IV - Source Image Witnesses Printed 185-225 "
        "(600-5000dpi) 20260731.zip"
    ),
    "root": "EGA4_Source_Image_Witnesses_Printed185_225_20260731",
}

base.PART = PART


def natural_key(path: Path) -> tuple[object, ...]:
    return tuple(
        int(token) if token.isdigit() else token.casefold()
        for token in re.split(r"(\d+)", path.name)
    )


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.casefold()).strip("_")


def add_row(
    rows: list[dict[str, object]],
    source_root: Path,
    path: Path,
    printed: int,
    role: str,
    dpi: int,
    qa_disposition: str = "source_alignment_checkpoint_build_p185_225_r12",
) -> None:
    width, height, x_ppm, y_ppm = base.png_info(path)
    entry_name = (
        f"authority_physical{printed - 1:03d}_printed{printed:03d}_"
        f"{slug(role)}_{dpi}dpi.png"
    )
    entry = f"{PART['root']}/images/{entry_name}"
    rows.append(
        {
            "witness_id": f"EGA4-IV4-P{printed:03d}-{slug(role).upper()}",
            "archive_filename": PART["filename"],
            "entry_path": entry,
            "source_filename": path.relative_to(source_root).as_posix(),
            "physical_pdf_page": printed - 1,
            "printed_page": printed,
            "crop_region": (
                "full_page"
                if "full" in role or "navigation" in role
                else "high_detail_tiled_crop"
            ),
            "crop_bbox_parent_pixels": "not_preserved_by_producer_command",
            "nominal_dpi": dpi,
            "width_pixels": width,
            "height_pixels": height,
            "png_x_pixels_per_meter": x_ppm if x_ppm is not None else "",
            "png_y_pixels_per_meter": y_ppm if y_ppm is not None else "",
            "rotation_degrees": 0,
            "bytes": path.stat().st_size,
            "sha256": base.sha256_path(path),
            "parent_scan_sha256": base.PARENT_SHA256,
            "linked_tex_unit": PART["linked_tex_unit"],
            "qa_disposition": qa_disposition,
            "public_disposition": "public_scan_derived_source_witness",
            "notes": (
                "Publicly available scan-derived witness; underlying-source rights "
                "and attribution remain unaffected."
            ),
            "_source_path": path,
        }
    )


def build_rows(source_root: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []

    navigation = sorted(
        source_root.glob("IV4_printed185_navigation_600dpi*.png"),
        key=natural_key,
    )
    if [path.name for path in navigation] != [
        "IV4_printed185_navigation_600dpi.png",
        "IV4_printed185_navigation_600dpi_r2.png",
    ]:
        raise RuntimeError("Printed-page 185 navigation witness set changed")
    for path in navigation:
        current = path.stem.endswith("_r2")
        add_row(
            rows,
            source_root,
            path,
            185,
            "navigation_full_r2" if current else "navigation_full_r1",
            600,
            (
                "source_alignment_checkpoint_build_p185_225_r12"
                if current
                else "superseded_navigation_r1_retained_as_visual_history"
            ),
        )

    for printed in range(185, 196):
        directory = source_root / f"IV4_printed{printed:03d}_5000dpi"
        files = sorted(directory.glob("*.png"), key=natural_key)
        if len(files) != 10:
            raise RuntimeError(f"Expected ten 5000-dpi tiles for printed {printed}")
        for path in files:
            match = re.fullmatch(rf"p{printed}_(.+)\.png", path.name)
            if not match:
                raise RuntimeError(f"Unclassified 5000-dpi tile: {path.name}")
            add_row(rows, source_root, path, printed, f"tile_{match.group(1)}", 5000)

    full_page_directories = [
        source_root / "IV4_printed196_200_1800dpi",
        source_root / "IV4_printed201_205_1800dpi",
        source_root / "IV4_printed206_210_1800dpi",
        source_root / "IV4_printed211_215_1800dpi",
        source_root / "IV4_printed216_220_1800dpi",
        source_root / "IV4_printed221_223_1800dpi",
        source_root / "IV4_printed224_226_1800dpi",
    ]
    for directory in full_page_directories:
        match = re.fullmatch(r"IV4_printed(\d{3})_(\d{3})_1800dpi", directory.name)
        if not match:
            raise RuntimeError(f"Unclassified full-page directory: {directory.name}")
        start = int(match.group(1))
        finish = int(match.group(2))
        files = sorted(
            (path for path in directory.glob("*.png") if "detail" not in path.stem),
            key=natural_key,
        )
        required_finish = min(finish, int(PART["maximum"]))
        required = max(0, required_finish - start + 1)
        if len(files) < required:
            raise RuntimeError(f"Missing full-page images in {directory.name}")
        for offset, printed in enumerate(range(start, required_finish + 1)):
            add_row(rows, source_root, files[offset], printed, "full_page", 1800)

    if len(rows) != 142:
        raise RuntimeError(f"Expected 142 source witnesses, found {len(rows)}")
    pages = {int(row["printed_page"]) for row in rows}
    if pages != set(range(int(PART["minimum"]), int(PART["maximum"]) + 1)):
        raise RuntimeError("Printed-page coverage changed")
    entries = [str(row["entry_path"]) for row in rows]
    if len(entries) != len(set(entries)):
        raise RuntimeError("Canonical archive entry collision")
    return rows


def archive_readme(rows: list[dict[str, object]]) -> bytes:
    text = f"""# EGA IV source-image witnesses: printed pages 185-225

This ZIP preserves {len(rows)} PNG witnesses / {sum(int(row['bytes']) for row in rows):,} bytes
derived from the publicly available 360-page NUMDAM EGA IV Part 4 scan.
The parent scan SHA-256 is `{base.PARENT_SHA256}` and the parent scan is directly
downloadable from the same EGA Zenodo concept.

Printed pages 185-195 are preserved as tiled 5,000-dpi source crops, with the
page-185 600-dpi navigation renders retained as versioned context. Printed
pages 196-225 are preserved as 1,800-dpi full-page source renders. Every image
is bound to physical/printed page, crop role, output dimensions, resolution,
bytes/SHA-256, linked editable TeX, and QA disposition in
`VISUAL_EVIDENCE_INDEX.csv` and `.jsonl`.

The set is bound to producer checkpoint `{PART['alignment_checkpoint']}` and
the Section 19 editable unit. Crop-command pixel offsets were not retained;
the index records honest symbolic regions and exact dimensions rather than
inventing numeric bounding boxes.

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
    public_rows = [base.public_row(row) for row in rows]
    (metadata_root / "VISUAL_EVIDENCE_INDEX.csv").write_bytes(
        base.csv_bytes(public_rows, base.INDEX_FIELDS)
    )
    (metadata_root / "VISUAL_EVIDENCE_INDEX.jsonl").write_bytes(
        base.jsonl_bytes(public_rows)
    )
    (metadata_root / "ZIP_PAYLOAD_MANIFEST.csv").write_bytes(
        base.csv_bytes([archive], tuple(archive))
    )
    (metadata_root / "README.md").write_text(
        "# EGA IV Section 19 high-detail source-image witnesses\n\n"
        f"This metadata binds the actual {len(rows)} scan-derived PNGs in "
        f"`{PART['filename']}`. The images cover printed pages 185-225 and are "
        f"bound to `{PART['alignment_checkpoint']}`. English-reader renders are "
        "not included.\n",
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
        "parent_scan_sha256": base.PARENT_SHA256,
        "zip_archive": archive,
        "privacy_hits": 0,
        "errors": [],
    }
    (metadata_root / "VALIDATION.json").write_text(
        json.dumps(validation, indent=2) + "\n", encoding="utf-8", newline="\n"
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
            "sha256": base.sha256_path(path),
        }
        for path in represented
    ]
    (metadata_root / "SHA256SUMS.csv").write_bytes(
        base.csv_bytes(sums_rows, ("path", "bytes", "sha256"))
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--zip-output", type=Path, required=True)
    parser.add_argument("--metadata-output", type=Path, required=True)
    args = parser.parse_args()
    args.zip_output.mkdir(parents=True, exist_ok=True)
    rows = build_rows(args.source_root)
    base.readme = archive_readme
    archive = base.build_zip(args.zip_output, rows)
    write_metadata(args.metadata_output, rows, archive)
    print(json.dumps({"status": "PASS", "images": len(rows), "zip": archive}, indent=2))


if __name__ == "__main__":
    main()
