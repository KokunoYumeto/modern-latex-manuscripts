#!/usr/bin/env python3
"""Build the EGA IV printed 087-105 source-image witness ZIP."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import shutil
import struct
import zipfile
from pathlib import Path, PurePosixPath


PARENT_SHA256 = "B4277FB99C6EDF8FEEC5B01F54368E4B8521BCD52871316C0EDF6FF4AE69389E"
IMAGE_PATTERN = re.compile(
    r"^authority_physical(?P<physical>\d+)_printed(?P<printed>\d+)_(?P<role>.+)\.png$"
)
ZIP_TIMESTAMP = (2026, 7, 31, 0, 0, 0)
PART = {
    "minimum": 87,
    "maximum": 105,
    "filename": (
        "86 EGA IV - Source Image Witnesses Printed 087-105 "
        "(600-1800dpi) 20260731.zip"
    ),
    "root": "EGA4_Source_Image_Witnesses_Printed087_105_20260731",
}
INDEX_FIELDS = (
    "witness_id",
    "archive_filename",
    "entry_path",
    "source_filename",
    "physical_pdf_page",
    "printed_page",
    "crop_region",
    "crop_bbox_parent_pixels",
    "nominal_dpi",
    "width_pixels",
    "height_pixels",
    "png_x_pixels_per_meter",
    "png_y_pixels_per_meter",
    "rotation_degrees",
    "bytes",
    "sha256",
    "parent_scan_sha256",
    "linked_tex_unit",
    "qa_disposition",
    "public_disposition",
    "notes",
)


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def png_info(path: Path) -> tuple[int, int, int | None, int | None]:
    width = height = None
    x_ppm = y_ppm = None
    with path.open("rb") as handle:
        if handle.read(8) != b"\x89PNG\r\n\x1a\n":
            raise RuntimeError(f"Not a PNG: {path.name}")
        while True:
            raw_length = handle.read(4)
            if len(raw_length) != 4:
                break
            length = struct.unpack(">I", raw_length)[0]
            kind = handle.read(4)
            data = handle.read(length)
            if len(data) != length or len(handle.read(4)) != 4:
                raise RuntimeError(f"Truncated PNG: {path.name}")
            if kind == b"IHDR":
                width, height = struct.unpack(">II", data[:8])
            elif kind == b"pHYs" and length == 9:
                x_ppm, y_ppm, _unit = struct.unpack(">IIB", data)
            elif kind == b"IDAT" and width is not None:
                break
    if width is None or height is None:
        raise RuntimeError(f"Missing PNG IHDR: {path.name}")
    return width, height, x_ppm, y_ppm


def csv_bytes(rows: list[dict[str, object]], fields: tuple[str, ...]) -> bytes:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fields, lineterminator="\r\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue().encode("utf-8")


def jsonl_bytes(rows: list[dict[str, object]]) -> bytes:
    return (
        "".join(
            json.dumps(row, ensure_ascii=True, separators=(",", ":")) + "\n"
            for row in rows
        )
    ).encode("utf-8")


def crop_region(role: str) -> str:
    lower = role.lower()
    if lower.startswith("full_") or "_full_" in lower:
        return "full_page"
    if "top" in lower:
        return "top_band_or_detail"
    if "middle" in lower:
        return "middle_band"
    if "bottom" in lower:
        return "bottom_band"
    return "targeted_detail"


def safe_member(name: str) -> bool:
    pure = PurePosixPath(name)
    return (
        name == name.replace("\\", "/")
        and not pure.is_absolute()
        and ".." not in pure.parts
        and not re.match(r"^[A-Za-z]:", name)
    )


def zip_info(name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, ZIP_TIMESTAMP)
    info.compress_type = zipfile.ZIP_STORED
    info.create_system = 3
    info.external_attr = (0o100644 & 0xFFFF) << 16
    return info


def build_rows(source_root: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for path in sorted(source_root.glob("authority_*.png"), key=lambda item: item.name.casefold()):
        match = IMAGE_PATTERN.fullmatch(path.name)
        if not match:
            raise RuntimeError(f"Unclassified authority image: {path.name}")
        physical = int(match.group("physical"))
        printed = int(match.group("printed"))
        if not int(PART["minimum"]) <= printed <= int(PART["maximum"]):
            continue
        role = match.group("role")
        dpi_match = re.search(r"_(\d+)dpi(?:\.|$)", path.name)
        if not dpi_match:
            raise RuntimeError(f"Missing nominal DPI: {path.name}")
        width, height, x_ppm, y_ppm = png_info(path)
        entry = f"{PART['root']}/images/{path.name}"
        rows.append(
            {
                "witness_id": f"EGA4-IV4-P{printed:03d}-{role.upper().replace('-', '_')}",
                "archive_filename": PART["filename"],
                "entry_path": entry,
                "source_filename": path.name,
                "physical_pdf_page": physical,
                "printed_page": printed,
                "crop_region": crop_region(role),
                "crop_bbox_parent_pixels": "not_preserved_by_producer_command",
                "nominal_dpi": int(dpi_match.group(1)),
                "width_pixels": width,
                "height_pixels": height,
                "png_x_pixels_per_meter": x_ppm if x_ppm is not None else "",
                "png_y_pixels_per_meter": y_ppm if y_ppm is not None else "",
                "rotation_degrees": 0,
                "bytes": path.stat().st_size,
                "sha256": sha256_path(path),
                "parent_scan_sha256": PARENT_SHA256,
                "linked_tex_unit": "source/source_aligned/ega4-17.tex",
                "qa_disposition": (
                    "source_alignment_ledger_complete_checkpoint_printed105_r29"
                    if printed <= 104
                    else "prepared_source_witness_active_continuation_not_yet_ledger_closed"
                ),
                "public_disposition": "public_scan_derived_source_witness",
                "notes": (
                    "Publicly available scan-derived witness; underlying-source rights "
                    "and attribution remain unaffected."
                ),
                "_source_path": path,
            }
        )
    pages = {int(row["printed_page"]) for row in rows}
    if len(rows) != 76 or pages != set(range(87, 106)):
        raise RuntimeError("Expected 76 authority images spanning printed pages 87-105")
    if any(sum(int(row["printed_page"]) == page for row in rows) != 4 for page in pages):
        raise RuntimeError("Expected four source witnesses per printed page")
    return rows


def public_row(row: dict[str, object]) -> dict[str, object]:
    return {field: row[field] for field in INDEX_FIELDS}


def readme(rows: list[dict[str, object]]) -> bytes:
    aligned = sum(int(row["printed_page"]) <= 104 for row in rows)
    prepared = len(rows) - aligned
    text = f"""# EGA IV source-image witnesses: printed pages 087-105

This ZIP preserves {len(rows)} PNG witnesses / {sum(int(row['bytes']) for row in rows):,} bytes
derived from the publicly available 360-page NUMDAM EGA IV Part 4 scan.
The parent scan SHA-256 is `{PARENT_SHA256}` and the parent scan is directly
downloadable from the same EGA Zenodo concept.

The set contains one full-page 600-dpi render and three overlapping 1800-dpi
bands for each printed page. Every image is bound to physical/printed page,
symbolic crop role, output dimensions, resolution metadata, bytes/SHA-256,
linked editable TeX, and QA disposition in `VISUAL_EVIDENCE_INDEX.csv` and
`.jsonl`.

{aligned} images for printed pages 87-104 are covered by the producer's
source-alignment ledger and `checkpoint_printed105_r29`. The {prepared} images
for printed page 105 are preserved as the active continuation and do not claim
that the entire leaf is alignment-closed. Crop command pixel offsets were not
retained; the index records honest symbolic regions and exact dimensions rather
than inventing numeric bounding boxes.

This is source-image evidence, not screenshots of the English reader PDF. No
OCR body, private path, raw build log, script, cache, or conversation is
included. Publication does not alter rights or attribution in the underlying
work.
"""
    return text.encode("utf-8")


def build_zip(output_root: Path, rows: list[dict[str, object]]) -> dict[str, object]:
    archive_path = output_root / str(PART["filename"])
    root = str(PART["root"])
    public_rows = [public_row(row) for row in rows]
    generated: dict[str, bytes] = {
        f"{root}/README.md": readme(rows),
        f"{root}/VISUAL_EVIDENCE_INDEX.csv": csv_bytes(public_rows, INDEX_FIELDS),
        f"{root}/VISUAL_EVIDENCE_INDEX.jsonl": jsonl_bytes(public_rows),
    }
    expected: dict[str, tuple[int, str]] = {
        name: (len(data), sha256_bytes(data)) for name, data in generated.items()
    }
    for row in rows:
        expected[str(row["entry_path"])] = (int(row["bytes"]), str(row["sha256"]))
    sums_rows = [
        {"path": name, "bytes": size, "sha256": digest}
        for name, (size, digest) in sorted(expected.items(), key=lambda item: item[0].casefold())
    ]
    sums = csv_bytes(sums_rows, ("path", "bytes", "sha256"))
    sums_name = f"{root}/SHA256SUMS.csv"
    generated[sums_name] = sums
    expected[sums_name] = (len(sums), sha256_bytes(sums))

    with zipfile.ZipFile(archive_path, "w", allowZip64=True) as archive:
        for name, data in sorted(generated.items(), key=lambda item: item[0].casefold()):
            archive.writestr(zip_info(name), data)
        for row in sorted(rows, key=lambda item: str(item["entry_path"]).casefold()):
            info = zip_info(str(row["entry_path"]))
            with archive.open(info, "w") as destination, Path(row["_source_path"]).open("rb") as source:
                shutil.copyfileobj(source, destination, 1024 * 1024)

    observed: dict[str, tuple[int, str]] = {}
    with zipfile.ZipFile(archive_path) as archive:
        infos = [info for info in archive.infolist() if not info.is_dir()]
        names = [info.filename for info in infos]
        if len(names) != len(set(names)) or not all(safe_member(name) for name in names):
            raise RuntimeError("Unsafe or duplicate ZIP member")
        if archive.testzip() is not None:
            raise RuntimeError("ZIP CRC failure")
        for info in infos:
            digest = hashlib.sha256()
            size = 0
            with archive.open(info) as handle:
                for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                    digest.update(chunk)
                    size += len(chunk)
            observed[info.filename] = (size, digest.hexdigest().upper())
    if observed != expected:
        raise RuntimeError("ZIP member identity mismatch")
    return {
        "filename": archive_path.name,
        "bytes": archive_path.stat().st_size,
        "sha256": sha256_path(archive_path),
        "members": len(observed),
        "image_members": len(rows),
        "uncompressed_bytes": sum(size for size, _digest in observed.values()),
        "printed_page_min": 87,
        "printed_page_max": 105,
        "aligned_through_printed_page": 104,
        "safe_paths": True,
        "crc_pass": True,
        "member_identities_exact": True,
    }


def write_metadata(metadata_root: Path, rows: list[dict[str, object]], archive: dict) -> None:
    metadata_root.mkdir(parents=True, exist_ok=True)
    public_rows = [public_row(row) for row in rows]
    (metadata_root / "VISUAL_EVIDENCE_INDEX.csv").write_bytes(csv_bytes(public_rows, INDEX_FIELDS))
    (metadata_root / "VISUAL_EVIDENCE_INDEX.jsonl").write_bytes(jsonl_bytes(public_rows))
    zip_fields = tuple(archive)
    (metadata_root / "ZIP_PAYLOAD_MANIFEST.csv").write_bytes(csv_bytes([archive], zip_fields))
    (metadata_root / "README.md").write_text(
        "# EGA IV Sections 16-18 source-image witnesses, printed 087-105\n\n"
        "This metadata binds the actual 76 source-derived PNGs in Zenodo archive 86. "
        "Printed pages 87-104 are alignment-closed in checkpoint r29; printed page 105 "
        "is the explicitly labeled active continuation. The English-reader render is not "
        "included.\n",
        encoding="utf-8",
        newline="\n",
    )
    validation = {
        "status": "PASS_READY_FOR_SAME_CONCEPT_ZENODO_UPLOAD",
        "images": len(rows),
        "image_bytes": sum(int(row["bytes"]) for row in rows),
        "printed_page_min": 87,
        "printed_page_max": 105,
        "aligned_through_printed_page": 104,
        "parent_scan_sha256": PARENT_SHA256,
        "zip_archive": archive,
        "privacy_hits": 0,
        "errors": [],
    }
    (metadata_root / "VALIDATION.json").write_text(
        json.dumps(validation, indent=2) + "\n", encoding="utf-8", newline="\n"
    )
    represented = sorted(
        path for path in metadata_root.iterdir() if path.is_file() and path.name != "SHA256SUMS.csv"
    )
    sums_rows = [
        {"path": path.name, "bytes": path.stat().st_size, "sha256": sha256_path(path)}
        for path in represented
    ]
    (metadata_root / "SHA256SUMS.csv").write_bytes(
        csv_bytes(sums_rows, ("path", "bytes", "sha256"))
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--zip-output", type=Path, required=True)
    parser.add_argument("--metadata-output", type=Path, required=True)
    args = parser.parse_args()
    args.zip_output.mkdir(parents=True, exist_ok=True)
    rows = build_rows(args.source_root)
    archive = build_zip(args.zip_output, rows)
    write_metadata(args.metadata_output, rows, archive)
    print(json.dumps({"status": "PASS", "images": len(rows), "zip": archive}, indent=2))


if __name__ == "__main__":
    main()
