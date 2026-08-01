#!/usr/bin/env python3
"""Independently replay the SGA7 I recovered targeted-crop dataset."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import sys
import zipfile
from pathlib import Path, PurePosixPath

from PIL import Image


PRIVATE_PATTERNS = (
    re.compile(r"(?i)[A-Z]:[\\/]+Users[\\/]+Floris"),
    re.compile(r"(?i)AppData[\\/]+Local[\\/]+Temp"),
    re.compile(r"(?i)C--Users-Floris"),
    re.compile(r"(?i)[A-Z]:[\\/]+w[\\/]"),
)
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".jpx", ".pnm"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive-dir", type=Path, required=True)
    parser.add_argument("--controls-dir", type=Path, required=True)
    return parser.parse_args()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def safe_member(name: str) -> bool:
    pure = PurePosixPath(name)
    return (
        name == name.replace("\\", "/")
        and not pure.is_absolute()
        and ".." not in pure.parts
        and not re.match(r"^[A-Za-z]:", name)
    )


def rows(data: bytes) -> list[dict[str, str]]:
    return list(csv.DictReader(io.StringIO(data.decode("utf-8-sig"))))


def main() -> int:
    args = parse_args()
    errors: list[str] = []
    outer = rows((args.controls_dir / "ZENODO_UPLOAD_MANIFEST.csv").read_bytes())
    if len(outer) != 3:
        errors.append(f"outer manifest rows: {len(outer)}")
    image_rows: list[dict[str, str]] = []
    decoded_images = 0
    archive_results = []
    for outer_row in outer:
        path = args.archive_dir / outer_row["filename"]
        if not path.is_file():
            errors.append(f"missing outer file: {path.name}")
            continue
        if path.stat().st_size != int(outer_row["bytes"]):
            errors.append(f"outer byte mismatch: {path.name}")
        if sha256_path(path) != outer_row["sha256"].upper():
            errors.append(f"outer hash mismatch: {path.name}")
        with zipfile.ZipFile(path) as bundle:
            bad = bundle.testzip()
            if bad:
                errors.append(f"CRC failure {path.name}: {bad}")
            entries = [entry for entry in bundle.infolist() if not entry.is_dir()]
            names = [entry.filename for entry in entries]
            if len(names) != len(set(names)):
                errors.append(f"duplicate member name: {path.name}")
            if not all(safe_member(name) for name in names):
                errors.append(f"unsafe member name: {path.name}")
            if len(entries) != int(outer_row["members"]):
                errors.append(f"member count mismatch: {path.name}")
            if sum(entry.file_size for entry in entries) != int(
                outer_row["uncompressed_bytes"]
            ):
                errors.append(f"uncompressed byte mismatch: {path.name}")
            sums = rows(bundle.read("SHA256SUMS.csv"))
            expected_names = {row["path"] for row in sums} | {"SHA256SUMS.csv"}
            if set(names) != expected_names:
                errors.append(f"checksum member closure: {path.name}")
            for checksum in sums:
                payload = bundle.read(checksum["path"])
                if len(payload) != int(checksum["bytes"]):
                    errors.append(
                        f"member byte mismatch: {path.name}/{checksum['path']}"
                    )
                if sha256_bytes(payload) != checksum["sha256"].upper():
                    errors.append(
                        f"member hash mismatch: {path.name}/{checksum['path']}"
                    )
                if PurePosixPath(checksum["path"]).suffix.lower() in IMAGE_SUFFIXES:
                    try:
                        with Image.open(io.BytesIO(payload)) as image:
                            image.verify()
                        decoded_images += 1
                    except Exception as exc:
                        errors.append(
                            f"image decode failure: {path.name}/{checksum['path']}: {exc}"
                        )
            if "IMAGE_MANIFEST.csv" in names:
                local_image_rows = rows(bundle.read("IMAGE_MANIFEST.csv"))
                image_members = {
                    name
                    for name in names
                    if PurePosixPath(name).suffix.lower() in IMAGE_SUFFIXES
                }
                if {row["archive_member"] for row in local_image_rows} != image_members:
                    errors.append(f"image manifest member closure: {path.name}")
                for row in local_image_rows:
                    payload = bundle.read(row["archive_member"])
                    if len(payload) != int(row["bytes"]):
                        errors.append(
                            f"image manifest byte mismatch: {row['visual_id']}"
                        )
                    if sha256_bytes(payload) != row["sha256"].upper():
                        errors.append(
                            f"image manifest hash mismatch: {row['visual_id']}"
                        )
                    if row["evidence_class"] != "targeted_crop":
                        errors.append(f"non-targeted image row: {row['visual_id']}")
                    if row["parent_pdf_sha256"].upper() != (
                        "9CD40FF06EB1E488AF385A56899D4F492492A06A1E2E3C0ED6876B82E3E3603F"
                    ):
                        errors.append(f"parent scan mismatch: {row['visual_id']}")
                image_rows.extend(local_image_rows)
            archive_results.append(
                {
                    "filename": path.name,
                    "bytes": path.stat().st_size,
                    "sha256": sha256_path(path),
                    "members": len(entries),
                }
            )
    metadata_name = "90_SGA7I_Targeted_Source_Crops_Metadata_20260801.zip"
    with zipfile.ZipFile(args.archive_dir / metadata_name) as bundle:
        metadata_included = rows(bundle.read("INCLUDED_IMAGE_MANIFEST.csv"))
        unavailable = rows(bundle.read("UNAVAILABLE_TARGETED_CROP_LEDGER.csv"))
        duplicates = rows(bundle.read("ALREADY_PUBLIC_DUPLICATES.csv"))
        summary = json.loads(bundle.read("DATASET_SUMMARY.json"))
    image_ids = [row["visual_id"] for row in image_rows]
    image_hashes = [row["sha256"].upper() for row in image_rows]
    if len(image_ids) != len(set(image_ids)) or len(image_hashes) != len(set(image_hashes)):
        errors.append("included image IDs or hashes are not unique")
    if sorted(image_ids) != sorted(row["visual_id"] for row in metadata_included):
        errors.append("metadata included-manifest ID closure")
    if len(image_rows) != 5_855 or decoded_images != 5_855:
        errors.append(
            f"included/decode boundary: image_rows={len(image_rows)} decoded={decoded_images}"
        )
    if len(unavailable) != 5_902 or len(duplicates) != 9:
        errors.append(
            f"disposition boundary: unavailable={len(unavailable)} duplicates={len(duplicates)}"
        )
    all_ids = image_ids + [row["visual_id"] for row in unavailable + duplicates]
    if len(all_ids) != 11_766 or len(all_ids) != len(set(all_ids)):
        errors.append("selected-row partition is not exact")
    if summary.get("included_rows") != 5_855 or summary.get("unavailable_rows") != 5_902:
        errors.append("summary boundary mismatch")
    privacy_hits = []
    for path in args.controls_dir.iterdir():
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in PRIVATE_PATTERNS:
            if pattern.search(text):
                privacy_hits.append(f"{path.name}:{pattern.pattern}")
    if privacy_hits:
        errors.extend(f"privacy hit: {value}" for value in privacy_hits)
    receipt = {
        "schema": "sga7i-targeted-high-detail-source-crops-independent-replay-v1",
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "outer_files": len(outer),
        "archives": archive_results,
        "included_images": len(image_rows),
        "decoded_images": decoded_images,
        "unavailable_ledger_rows": len(unavailable),
        "already_public_duplicate_rows": len(duplicates),
        "selected_partition_rows": len(all_ids),
        "privacy_hits": privacy_hits,
    }
    output = args.controls_dir / "INDEPENDENT_ARCHIVE_REPLAY.json"
    output.write_text(
        json.dumps(receipt, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps(receipt, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
