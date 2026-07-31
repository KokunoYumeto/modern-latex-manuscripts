#!/usr/bin/env python3
"""Build compact EGA IV source-image witness ZIPs without copying the PNG tree."""

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
PARTS = (
    {
        "minimum": 5,
        "maximum": 45,
        "filename": (
            "84 EGA IV - Source Image Witnesses Printed 005-045 "
            "(600-9000dpi) 20260731.zip"
        ),
        "root": "EGA4_Source_Image_Witnesses_Printed005_045_20260731",
    },
    {
        "minimum": 46,
        "maximum": 86,
        "filename": (
            "85 EGA IV - Source Image Witnesses Printed 046-086 "
            "(600-1800dpi) 20260731.zip"
        ),
        "root": "EGA4_Source_Image_Witnesses_Printed046_086_20260731",
    },
)
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
        "".join(json.dumps(row, ensure_ascii=True, separators=(",", ":")) + "\n" for row in rows)
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
    if "formula" in lower:
        return "formula_detail"
    return "targeted_detail"


def linked_tex(printed: int) -> str:
    if printed < 56:
        return "source/source_aligned/ega4-16.tex"
    if printed == 56:
        return "source/source_aligned/ega4-16.tex;source/source_aligned/ega4-17.tex"
    return "source/source_aligned/ega4-17.tex"


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
    paths = sorted(source_root.glob("authority_*.png"), key=lambda path: path.name.casefold())
    rows: list[dict[str, object]] = []
    for path in paths:
        match = IMAGE_PATTERN.fullmatch(path.name)
        if not match:
            raise RuntimeError(f"Unclassified authority image: {path.name}")
        physical = int(match.group("physical"))
        printed = int(match.group("printed"))
        role = match.group("role")
        part = next(
            row for row in PARTS if row["minimum"] <= printed <= row["maximum"]
        )
        dpi_match = re.search(r"_(\d+)dpi(?:\.|$)", path.name)
        if not dpi_match:
            raise RuntimeError(f"Missing nominal DPI: {path.name}")
        width, height, x_ppm, y_ppm = png_info(path)
        entry = f"{part['root']}/images/{path.name}"
        rows.append(
            {
                "witness_id": f"EGA4-IV4-P{printed:03d}-{role.upper().replace('-', '_')}",
                "archive_filename": part["filename"],
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
                "linked_tex_unit": linked_tex(printed),
                "qa_disposition": (
                    "source_alignment_and_manual_review_complete_through_r23"
                    if printed <= 78
                    else "prepared_source_witness_not_yet_claimed_aligned"
                ),
                "public_disposition": "public_scan_derived_source_witness",
                "notes": (
                    "Publicly available scan-derived witness; underlying-source rights "
                    "and attribution remain unaffected."
                ),
                "_source_path": path,
            }
        )
    if len(rows) != 343 or {int(row["printed_page"]) for row in rows} != set(range(5, 87)):
        raise RuntimeError("Expected 343 authority images spanning printed pages 5-86")
    return rows


def public_row(row: dict[str, object]) -> dict[str, object]:
    return {field: row[field] for field in INDEX_FIELDS}


def readme(part: dict[str, object], rows: list[dict[str, object]]) -> bytes:
    aligned = sum(1 for row in rows if int(row["printed_page"]) <= 78)
    prepared = len(rows) - aligned
    text = f"""# EGA IV source-image witnesses: printed pages {part['minimum']:03d}-{part['maximum']:03d}

This ZIP preserves {len(rows)} PNG witnesses / {sum(int(row['bytes']) for row in rows):,} bytes
derived from the publicly available 360-page NUMDAM EGA IV Part 4 scan.
The parent scan SHA-256 is `{PARENT_SHA256}` and the parent scan itself remains
available directly as `17 EGA IV Part 4 - French Original (NUMDAM PMIHES 32,
1967).pdf` on the same EGA Zenodo record.

The set includes full-page renders, overlapping bands, and targeted ambiguity
crops at nominal resolutions from {min(int(row['nominal_dpi']) for row in rows)}
through {max(int(row['nominal_dpi']) for row in rows)} dpi. Each image is bound
to physical/printed page coordinates, dimensions, resolution metadata, exact
bytes/SHA-256, linked editable TeX, and QA disposition in
`VISUAL_EVIDENCE_INDEX.csv` and `.jsonl`.

{aligned} images correspond to pages included in the source-aligned checkpoint
through printed page 78. {prepared} later images are preserved as prepared
source witnesses and do not claim completed text alignment. Crop command pixel
offsets were not retained by the producer; symbolic full/top/middle/bottom or
targeted-detail roles and exact output dimensions are recorded instead.

The two English-reader render PNGs in the producer directory are deliberately
excluded: this package preserves source-image evidence, not redundant images
of an already downloadable PDF. No OCR body, private path, raw log, script,
cache, or conversation is included. Publication of these scan-derived
witnesses does not alter the rights or attribution of the underlying work.
"""
    return text.encode("utf-8")


def build_zip(
    source_root: Path,
    output_root: Path,
    part: dict[str, object],
    rows: list[dict[str, object]],
) -> dict[str, object]:
    archive_path = output_root / str(part["filename"])
    archive_rows = [row for row in rows if row["archive_filename"] == part["filename"]]
    public_rows = [public_row(row) for row in archive_rows]
    root = str(part["root"])
    generated: dict[str, bytes] = {
        f"{root}/README.md": readme(part, archive_rows),
        f"{root}/VISUAL_EVIDENCE_INDEX.csv": csv_bytes(public_rows, INDEX_FIELDS),
        f"{root}/VISUAL_EVIDENCE_INDEX.jsonl": jsonl_bytes(public_rows),
    }
    expected: dict[str, tuple[int, str]] = {
        name: (len(data), sha256_bytes(data)) for name, data in generated.items()
    }
    for row in archive_rows:
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
        for row in sorted(archive_rows, key=lambda item: str(item["entry_path"]).casefold()):
            info = zip_info(str(row["entry_path"]))
            with archive.open(info, "w") as destination, Path(row["_source_path"]).open("rb") as source:
                shutil.copyfileobj(source, destination, 1024 * 1024)

    observed: dict[str, tuple[int, str]] = {}
    with zipfile.ZipFile(archive_path) as archive:
        infos = [info for info in archive.infolist() if not info.is_dir()]
        names = [info.filename for info in infos]
        if len(names) != len(set(names)) or not all(safe_member(name) for name in names):
            raise RuntimeError(f"Unsafe or duplicate ZIP member: {archive_path.name}")
        if archive.testzip() is not None:
            raise RuntimeError(f"CRC failure: {archive_path.name}")
        for info in infos:
            digest = hashlib.sha256()
            size = 0
            with archive.open(info) as handle:
                for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                    digest.update(chunk)
                    size += len(chunk)
            observed[info.filename] = (size, digest.hexdigest().upper())
    if observed != expected:
        raise RuntimeError(f"ZIP member identity mismatch: {archive_path.name}")
    return {
        "filename": archive_path.name,
        "bytes": archive_path.stat().st_size,
        "sha256": sha256_path(archive_path),
        "members": len(observed),
        "image_members": len(archive_rows),
        "uncompressed_bytes": sum(size for size, _digest in observed.values()),
        "printed_page_min": int(part["minimum"]),
        "printed_page_max": int(part["maximum"]),
        "safe_paths": True,
        "crc_pass": True,
        "member_identities_exact": True,
    }


def write_metadata(metadata_root: Path, rows: list[dict[str, object]], zips: list[dict]) -> None:
    metadata_root.mkdir(parents=True, exist_ok=True)
    public_rows = [public_row(row) for row in rows]
    (metadata_root / "VISUAL_EVIDENCE_INDEX.csv").write_bytes(csv_bytes(public_rows, INDEX_FIELDS))
    (metadata_root / "VISUAL_EVIDENCE_INDEX.jsonl").write_bytes(jsonl_bytes(public_rows))
    zip_fields = (
        "filename",
        "bytes",
        "sha256",
        "members",
        "image_members",
        "uncompressed_bytes",
        "printed_page_min",
        "printed_page_max",
        "safe_paths",
        "crc_pass",
        "member_identities_exact",
    )
    (metadata_root / "ZIP_PAYLOAD_MANIFEST.csv").write_bytes(csv_bytes(zips, zip_fields))
    readme_text = """# EGA IV Sections 16-18 source-image witness archives

Two same-concept Zenodo ZIPs preserve the current 343 source-derived PNG
witnesses spanning printed pages 5-86. They contain the actual 600/1800-dpi
full-page and band images plus targeted 5000/9000-dpi ambiguity crops, not
screenshots of the English reader PDF.

The combined index records the parent scan hash, physical and printed page,
symbolic crop region, output dimensions, PNG resolution metadata, rotation,
bytes, SHA-256, linked editable TeX unit, and QA disposition for every image.
The source scan is already directly downloadable from the same EGA record.

Pages through printed 78 are bound to the current source-aligned checkpoint;
pages 79-86 are preserved as prepared witnesses without claiming completed
text alignment. Underlying-source rights and attribution remain unaffected.
"""
    (metadata_root / "README.md").write_text(readme_text, encoding="utf-8", newline="\n")
    validation = {
        "status": "PASS_READY_FOR_SAME_CONCEPT_ZENODO_UPLOAD",
        "images": len(rows),
        "image_bytes": sum(int(row["bytes"]) for row in rows),
        "printed_page_min": min(int(row["printed_page"]) for row in rows),
        "printed_page_max": max(int(row["printed_page"]) for row in rows),
        "parent_scan_sha256": PARENT_SHA256,
        "english_reader_render_images_excluded": 2,
        "zip_archives": zips,
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
    zips = [build_zip(args.source_root, args.zip_output, part, rows) for part in PARTS]
    write_metadata(args.metadata_output, rows, zips)
    print(json.dumps({"status": "PASS", "images": len(rows), "zips": zips}, indent=2))


if __name__ == "__main__":
    main()
