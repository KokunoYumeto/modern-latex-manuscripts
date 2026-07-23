#!/usr/bin/env python3
"""Build the Weber Volume I high-detail audit-crop metadata and ZIP payloads."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import sys
import zipfile
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import fitz
from PIL import Image


MAPPED_RE = re.compile(
    r"^vol1_p(?P<printed>\d{3})_crop_(?P<x0>\d+)_(?P<y0>\d+)\.png$",
    re.IGNORECASE,
)
PAGE_STRIP_RE = re.compile(
    r"^vol1_p\d{3}_(?:top|mid|bot|full)\.png$", re.IGNORECASE
)
PAGE_DERIVATIVE_RE = re.compile(
    r"^vol1_p\d{3}_(?:"
    r"offsetcheck|bot_ac|bot_mirror|bot_sharp|mid_ac|mid_mirror|"
    r"mid_sharp|bot_enh|mid_enh"
    r")\.png$",
    re.IGNORECASE,
)
PRIVATE_MARKERS = (
    "c:\\users\\",
    "floris",
    "chatnotes",
    "claude",
    "codex",
    "thread_id",
    "source_thread_id",
    "@gmail.",
    "@outlook.",
)
MAPPED_ZIP = "Weber_VolumeI_PageMapped_HighDetail_Audit_Crops_20260723.zip"
UNMAPPED_ZIP = "Weber_VolumeI_Recovered_Unmapped_Audit_Images_20260723.zip"
README_NAME = "Weber_VolumeI_HighDetail_Audit_Crops_README_20260723.md"
PARENT_NAME = "Weber_VolumeI_HighDetail_Audit_Crops_PARENT_SOURCE_20260723.json"
MAPPED_MANIFEST_NAME = (
    "Weber_VolumeI_PageMapped_HighDetail_Audit_Crops_Manifest_20260723.csv"
)
UNMAPPED_MANIFEST_NAME = (
    "Weber_VolumeI_Recovered_Unmapped_Audit_Images_Manifest_20260723.csv"
)
VALIDATION_NAME = "Weber_VolumeI_HighDetail_Audit_Crops_VALIDATION_20260723.json"
UPLOAD_MANIFEST_NAME = (
    "Weber_VolumeI_HighDetail_Audit_Crops_ZENODO_UPLOAD_MANIFEST_20260723.csv"
)
SHA_NAME = "Weber_VolumeI_HighDetail_Audit_Crops_SHA256SUMS_20260723.txt"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--parent-pdf", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--zip-dir", type=Path, required=True)
    return parser.parse_args()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def utc_mtime(path: Path) -> str:
    return datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).isoformat()


def png_metadata(path: Path) -> dict[str, object]:
    with Image.open(path) as image:
        image.verify()
    with Image.open(path) as image:
        info = {str(key): str(value) for key, value in image.info.items()}
        dpi = image.info.get("dpi")
        dpi_x = round(float(dpi[0]), 4) if dpi else ""
        dpi_y = round(float(dpi[1]), 4) if dpi else ""
        result = {
            "width_px": image.width,
            "height_px": image.height,
            "color_mode": image.mode,
            "embedded_dpi_x": dpi_x,
            "embedded_dpi_y": dpi_y,
            "metadata_text": json.dumps(info, ensure_ascii=True, sort_keys=True),
        }
    return result


def privacy_hits(values: list[str]) -> list[str]:
    joined = "\n".join(values).lower()
    return sorted(marker for marker in PRIVATE_MARKERS if marker in joined)


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_text_lf(path: Path, text: str) -> None:
    path.write_bytes(text.encode("utf-8"))


def make_row(
    path: Path,
    source_dir: Path,
    image: dict[str, object],
    digest: str,
    parent_sha: str,
    mapped: re.Match[str] | None,
) -> dict[str, object]:
    source_relative_path = path.relative_to(source_dir).as_posix()
    if mapped:
        printed_page = int(mapped.group("printed"))
        pdf_page = printed_page + 26
        origin_x = int(mapped.group("x0"))
        origin_y = int(mapped.group("y0"))
        archive_path = f"images/page_mapped/{source_relative_path}"
        locator_status = "printed_and_pdf_page_recorded"
        bbox_status = "origin_recorded_extent_not_recorded"
        generator = (
            "crop_src.py naming profile; tool documentation declares a 600-dpi "
            "source render and 3x display scale unless the caller overrides them"
        )
    else:
        printed_page = ""
        pdf_page = ""
        origin_x = ""
        origin_y = ""
        archive_path = f"images/unmapped/{source_relative_path}"
        locator_status = "volume_known_page_unresolved"
        bbox_status = "not_recorded"
        generator = "recovered current-audit image; per-file invocation not retained"
    return {
        "archive_path": archive_path,
        "source_relative_path": source_relative_path,
        "source_basename": path.name,
        "bytes": path.stat().st_size,
        "sha256": digest,
        "width_px": image["width_px"],
        "height_px": image["height_px"],
        "color_mode": image["color_mode"],
        "embedded_dpi_x": image["embedded_dpi_x"],
        "embedded_dpi_y": image["embedded_dpi_y"],
        "modified_utc": utc_mtime(path),
        "volume": 1,
        "printed_page": printed_page,
        "parent_pdf_page_1based": pdf_page,
        "crop_origin_x_percent": origin_x,
        "crop_origin_y_percent": origin_y,
        "crop_bbox_status": bbox_status,
        "generator_profile": generator,
        "locator_status": locator_status,
        "qa_disposition": "source_audit_witness_not_translation_certification",
        "linked_tex_object": "weber_v1_ge.tex",
        "parent_scan_sha256": parent_sha,
    }


def zip_payload(
    zip_path: Path,
    rows: list[dict[str, object]],
    source_dir: Path,
    metadata_paths: list[Path],
) -> dict[str, object]:
    fixed_zip_time = (2026, 7, 23, 0, 0, 0)

    def add_file(archive: zipfile.ZipFile, path: Path, member_name: str) -> None:
        info = zipfile.ZipInfo(member_name, date_time=fixed_zip_time)
        info.compress_type = zipfile.ZIP_STORED
        info.create_system = 3
        info.external_attr = 0o100644 << 16
        archive.writestr(info, path.read_bytes())

    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_STORED) as archive:
        for metadata_path in metadata_paths:
            add_file(archive, metadata_path, f"metadata/{metadata_path.name}")
        for row in rows:
            add_file(
                archive,
                source_dir / str(row["source_relative_path"]),
                str(row["archive_path"]),
            )

    expected = {
        **{
            f"metadata/{path.name}": (path.stat().st_size, sha256(path))
            for path in metadata_paths
        },
        **{
            str(row["archive_path"]): (int(row["bytes"]), str(row["sha256"]))
            for row in rows
        },
    }
    errors: list[str] = []
    member_rows: list[dict[str, object]] = []
    with zipfile.ZipFile(zip_path, "r") as archive:
        bad_member = archive.testzip()
        if bad_member:
            errors.append(f"CRC failure: {bad_member}")
        names = archive.namelist()
        if len(names) != len(set(names)):
            errors.append("duplicate ZIP member names")
        if set(names) != set(expected):
            missing = sorted(set(expected) - set(names))
            extra = sorted(set(names) - set(expected))
            errors.append(f"ZIP set mismatch missing={missing} extra={extra}")
        for member in archive.infolist():
            if member.filename.startswith("/") or ".." in Path(member.filename).parts:
                errors.append(f"unsafe ZIP member: {member.filename}")
            data = archive.read(member.filename)
            digest = hashlib.sha256(data).hexdigest().upper()
            size = len(data)
            expected_item = expected.get(member.filename)
            if expected_item and expected_item != (size, digest):
                errors.append(f"ZIP member identity mismatch: {member.filename}")
            member_rows.append(
                {
                    "path": member.filename,
                    "bytes": size,
                    "sha256": digest,
                }
            )
    return {
        "filename": zip_path.name,
        "bytes": zip_path.stat().st_size,
        "sha256": sha256(zip_path),
        "members": len(member_rows),
        "image_members": len(rows),
        "uncompressed_bytes": sum(int(row["bytes"]) for row in member_rows),
        "errors": errors,
    }


def main() -> int:
    args = parse_args()
    source_dir = args.source_dir.resolve()
    parent_pdf = args.parent_pdf.resolve()
    output_dir = args.output_dir.resolve()
    zip_dir = args.zip_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    zip_dir.mkdir(parents=True, exist_ok=True)

    files = sorted(
        source_dir.rglob("*.png"),
        key=lambda path: path.relative_to(source_dir).as_posix().lower(),
    )
    mapped_paths: list[tuple[Path, re.Match[str]]] = []
    unmapped_paths: list[Path] = []
    excluded_paths: list[Path] = []
    errors: list[str] = []
    for path in files:
        mapped = MAPPED_RE.fullmatch(path.name)
        if mapped:
            mapped_paths.append((path, mapped))
        elif PAGE_STRIP_RE.fullmatch(path.name) or PAGE_DERIVATIVE_RE.fullmatch(
            path.name
        ):
            excluded_paths.append(path)
        elif path.name.lower().startswith("vol1_p"):
            errors.append(f"unclassified page-labelled file: {path.name}")
        else:
            unmapped_paths.append(path)

    parent_sha = sha256(parent_pdf)
    parent_stat = parent_pdf.stat()
    with fitz.open(parent_pdf) as document:
        parent_pages = document.page_count
        parent_metadata = document.metadata

    mapped_rows: list[dict[str, object]] = []
    unmapped_rows: list[dict[str, object]] = []
    content_hash_paths: dict[str, list[str]] = defaultdict(list)
    png_privacy: dict[str, list[str]] = {}

    for path, mapped in mapped_paths:
        try:
            image = png_metadata(path)
        except Exception as exc:
            errors.append(f"invalid PNG {path.name}: {exc}")
            continue
        digest = sha256(path)
        row = make_row(path, source_dir, image, digest, parent_sha, mapped)
        mapped_rows.append(row)
        source_relative_path = path.relative_to(source_dir).as_posix()
        content_hash_paths[digest].append(source_relative_path)
        hits = privacy_hits([source_relative_path, str(image["metadata_text"])])
        if hits:
            png_privacy[source_relative_path] = hits

    for path in unmapped_paths:
        try:
            image = png_metadata(path)
        except Exception as exc:
            errors.append(f"invalid PNG {path.name}: {exc}")
            continue
        digest = sha256(path)
        row = make_row(path, source_dir, image, digest, parent_sha, None)
        unmapped_rows.append(row)
        source_relative_path = path.relative_to(source_dir).as_posix()
        content_hash_paths[digest].append(source_relative_path)
        hits = privacy_hits([source_relative_path, str(image["metadata_text"])])
        if hits:
            png_privacy[source_relative_path] = hits

    if png_privacy:
        errors.append(f"PNG metadata or filename privacy hits: {png_privacy}")

    manifest_fields = list(mapped_rows[0].keys()) if mapped_rows else []
    mapped_manifest = output_dir / MAPPED_MANIFEST_NAME
    unmapped_manifest = output_dir / UNMAPPED_MANIFEST_NAME
    write_csv(mapped_manifest, mapped_rows, manifest_fields)
    write_csv(unmapped_manifest, unmapped_rows, manifest_fields)

    parent_identity = {
        "title": "Heinrich Weber, Lehrbuch der Algebra, Erster Band",
        "author": "Heinrich Weber",
        "publication": "Braunschweig: Friedrich Vieweg und Sohn, 1895",
        "source_file_basename": parent_pdf.name,
        "bytes": parent_stat.st_size,
        "sha256": parent_sha,
        "pages": parent_pages,
        "printed_to_pdf_offset": 26,
        "pdf_page_formula": "pdf_page_1based = printed_page + 26",
        "pdf_metadata": parent_metadata,
        "rights_status": (
            "Public-domain historical work. No new copyright is asserted in "
            "the source text or mechanical crop pixels."
        ),
        "parent_scan_not_duplicated_in_this_release": True,
    }
    parent_path = output_dir / PARENT_NAME
    write_text_lf(
        parent_path,
        json.dumps(parent_identity, indent=2, ensure_ascii=True) + "\n",
    )

    duplicate_groups = {
        digest: sorted(paths)
        for digest, paths in content_hash_paths.items()
        if len(paths) > 1
    }
    readme = f"""# Weber Volume I High-Detail Audit Crops

This package preserves the source-image derivatives actually used in the
current Weber Volume I transcription and fidelity audit. It does not repackage
ordinary PDF page renders as a substitute for the source PDF.

## Public image dumps

- `{MAPPED_ZIP}`: {len(mapped_rows)} tight high-detail crops,
  {sum(int(row['bytes']) for row in mapped_rows):,} uncompressed image bytes.
  Every image has an exact Weber printed-page and source-PDF-page locator in
  `{MAPPED_MANIFEST_NAME}`. The crop filename records the upper-left origin as
  a percentage of the source page; the opposite corner was not retained and is
  therefore not invented.
- `{UNMAPPED_ZIP}`: {len(unmapped_rows)} additional recovered audit images,
  {sum(int(row['bytes']) for row in unmapped_rows):,} uncompressed image bytes.
  These are preserved because they are real working zooms or derivatives from
  the same current Volume I audit, but their filenames do not retain a reliable
  page locator. Their manifest says `volume_known_page_unresolved`.

## Deliberate exclusions

The source directory contains {len(files)} PNG files / {sum(path.stat().st_size for path in files):,}
bytes. This release excludes {len(excluded_paths)} routine whole-page,
top/middle/bottom strip, offset-check, and enhancement renders /
{sum(path.stat().st_size for path in excluded_paths):,} bytes. Those files are
computationally cheap derivatives of the already available zoomable source PDF
and are not the high-value crop corpus requested for archive preservation.

## Parent and method

The parent is Heinrich Weber, *Lehrbuch der Algebra*, Volume I (1895), exact
scan SHA-256 `{parent_sha}`. The PDF has {parent_pages} pages and the audit
mapping is `source PDF page = printed page + 26`.

The page-mapped tight-crop filenames were emitted by the audit's `crop_src.py`
profile. Its documentation declares a 600-dpi source render and a 3x display
upscale by default, but callers could override those values; the PNG manifests
therefore report embedded DPI when present and do not turn the tool default
into false per-file certainty.

## Claim boundary

These images are visual/provenance evidence. They do not certify the German
transcription, English translation, mathematics, completeness, or critical
edition status. The second ZIP is intentionally retained with unresolved page
locators rather than given fabricated coordinates.

The 1895 source work is public domain. This release asserts no new copyright in
the historical source text or mechanically derived crop pixels.
"""
    readme_path = output_dir / README_NAME
    write_text_lf(readme_path, readme)

    mapped_zip_path = zip_dir / MAPPED_ZIP
    unmapped_zip_path = zip_dir / UNMAPPED_ZIP
    mapped_zip_result = zip_payload(
        mapped_zip_path,
        mapped_rows,
        source_dir,
        [readme_path, parent_path, mapped_manifest],
    )
    unmapped_zip_result = zip_payload(
        unmapped_zip_path,
        unmapped_rows,
        source_dir,
        [readme_path, parent_path, unmapped_manifest],
    )
    errors.extend(str(error) for error in mapped_zip_result["errors"])
    errors.extend(str(error) for error in unmapped_zip_result["errors"])

    selection_counts = Counter(
        {
            "source_pngs": len(files),
            "page_mapped_tight_crops": len(mapped_rows),
            "recovered_unmapped_images": len(unmapped_rows),
            "excluded_page_render_derivatives": len(excluded_paths),
        }
    )
    if sum(
        selection_counts[key]
        for key in (
            "page_mapped_tight_crops",
            "recovered_unmapped_images",
            "excluded_page_render_derivatives",
        )
    ) != selection_counts["source_pngs"]:
        errors.append("selection counts do not close over source PNG set")

    snapshot_utc = datetime.fromtimestamp(
        max(path.stat().st_mtime for path in files), timezone.utc
    ).isoformat()
    validation = {
        "schema": "weber_visual_crop_release_validation_v1",
        "snapshot_utc": snapshot_utc,
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "source": {
            "files": len(files),
            "bytes": sum(path.stat().st_size for path in files),
        },
        "selection": {
            "page_mapped_tight_crops": {
                "files": len(mapped_rows),
                "bytes": sum(int(row["bytes"]) for row in mapped_rows),
                "manifest_sha256": sha256(mapped_manifest),
            },
            "recovered_unmapped_images": {
                "files": len(unmapped_rows),
                "bytes": sum(int(row["bytes"]) for row in unmapped_rows),
                "manifest_sha256": sha256(unmapped_manifest),
            },
            "excluded_render_derivatives": {
                "files": len(excluded_paths),
                "bytes": sum(path.stat().st_size for path in excluded_paths),
            },
        },
        "parent_source": parent_identity,
        "png_validation": {
            "validated_files": len(mapped_rows) + len(unmapped_rows),
            "invalid_files": sum(1 for error in errors if error.startswith("invalid PNG")),
            "privacy_hits": png_privacy,
            "duplicate_content_groups": duplicate_groups,
        },
        "zip_validation": {
            MAPPED_ZIP: mapped_zip_result,
            UNMAPPED_ZIP: unmapped_zip_result,
        },
    }
    validation_path = output_dir / VALIDATION_NAME
    write_text_lf(
        validation_path,
        json.dumps(validation, indent=2, ensure_ascii=True) + "\n",
    )

    upload_paths = [
        mapped_zip_path,
        unmapped_zip_path,
        readme_path,
        parent_path,
        mapped_manifest,
        unmapped_manifest,
        validation_path,
    ]
    upload_rows = []
    for path in upload_paths:
        upload_rows.append(
            {
                "filename": path.name,
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
                "role": (
                    "image_archive"
                    if path.suffix.lower() == ".zip"
                    else "public_metadata"
                ),
                "status": "proposed_public",
            }
        )
    upload_manifest = output_dir / UPLOAD_MANIFEST_NAME
    write_csv(
        upload_manifest,
        upload_rows,
        ["filename", "bytes", "sha256", "role", "status"],
    )

    checksum_paths = upload_paths + [upload_manifest]
    checksum_lines = [
        f"{sha256(path)}  {path.name}" for path in sorted(checksum_paths, key=lambda p: p.name)
    ]
    checksum_path = output_dir / SHA_NAME
    write_text_lf(checksum_path, "\n".join(checksum_lines) + "\n")

    summary = {
        "status": validation["status"],
        "mapped_files": len(mapped_rows),
        "unmapped_files": len(unmapped_rows),
        "excluded_files": len(excluded_paths),
        "mapped_zip": mapped_zip_result,
        "unmapped_zip": unmapped_zip_result,
        "upload_manifest_sha256": sha256(upload_manifest),
        "sha256sums_sha256": sha256(checksum_path),
        "validation_sha256": sha256(validation_path),
    }
    print(json.dumps(summary, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
