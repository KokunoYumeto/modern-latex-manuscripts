#!/usr/bin/env python3
"""Independently replay and verify the SGA6 idx653-665 crop release."""

from __future__ import annotations

import argparse
import csv
import gc
import hashlib
import io
import json
import re
import zipfile
from pathlib import Path
from typing import Any

import fitz
from PIL import Image, ImageChops, ImageEnhance, ImageOps, ImageStat


PARENT_SHA256 = "73FBBAD41340C12ECCDCFCF6C3A1656953FE3D712AA8E391678458CCD17B4BAA"
PARENT_BYTES = 26_833_956
PARENT_PAGES = 720
START_INDEX = 653
END_INDEX = 665
START_ENTRY = 1405
END_ENTRY = 1417
AUDIT_SHA256 = "53552F00132E2672D78C693FF78ACA8DF7E8A5ED1FD6D6621F9F585993340E3C"
TARGET_COUNT = 68
TARGET_BYTES = 3_148_724
EXCLUDED_COUNT = 13
ROUTINE_COUNT = 65
ROUTINE_BYTES = 14_631_063

PRIVATE_MARKERS = (
    "c:\\users\\",
    "c:/users/",
    "\\appdata\\",
    "/appdata/",
    "floris",
    "chatnotes",
    ".claude",
    "source_thread_id",
    "thread_id",
    "@gmail.",
    "@outlook.",
)
FORMULA_PREFIXES = ("=", "+", "-", "@")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--package-dir", type=Path, required=True)
    parser.add_argument("--zip-dir", type=Path, required=True)
    parser.add_argument("--scratch-dir", type=Path, required=True)
    parser.add_argument("--parent-pdf", type=Path, required=True)
    parser.add_argument("--cert-log", type=Path, required=True)
    return parser.parse_args()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest().upper()


def rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def formula_triggers(path: Path) -> list[str]:
    triggers: list[str] = []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        for row_number, row in enumerate(csv.reader(handle), start=1):
            for column_number, cell in enumerate(row, start=1):
                if cell.startswith(FORMULA_PREFIXES):
                    triggers.append(f"R{row_number}C{column_number}:{cell[:40]}")
    return triggers


def audit_headings(cert_log: Path) -> list[str]:
    selected: list[tuple[int, str]] = []
    pattern = re.compile(r"^### #(?P<entry>\d+)\b")
    for line in cert_log.read_text(encoding="utf-8", errors="replace").splitlines():
        match = pattern.match(line)
        if not match:
            continue
        entry = int(match.group("entry"))
        if START_ENTRY <= entry <= END_ENTRY:
            selected.append((entry, line))
    selected.sort(key=lambda item: item[0])
    return [line for _, line in selected]


def parse_profile(value: str) -> tuple[int, float, float]:
    match = re.fullmatch(
        r"grayscale;autocontrast_cutoff_(?P<cutoff>[0-9.]+);"
        r"contrast_(?P<contrast>[0-9.]+);"
        r"sharpness_(?P<sharpness>[0-9.]+)",
        value,
    )
    if not match:
        raise ValueError(f"unrecognized profile: {value}")
    return (
        int(float(match.group("cutoff"))),
        float(match.group("contrast")),
        float(match.group("sharpness")),
    )


def replay_png(document: fitz.Document, row: dict[str, str]) -> bytes:
    page = document[int(row["parent_pdf_index_0based"])]
    rect = page.rect
    clip = fitz.Rect(
        rect.x0 + rect.width * float(row["bbox_fx0"]),
        rect.y0 + rect.height * float(row["bbox_fy0"]),
        rect.x0 + rect.width * float(row["bbox_fx1"]),
        rect.y0 + rect.height * float(row["bbox_fy1"]),
    )
    dpi = int(row["render_dpi"])
    pixmap = page.get_pixmap(
        matrix=fitz.Matrix(dpi / 72.0, dpi / 72.0),
        clip=clip,
    )
    pixmap_png = pixmap.tobytes("png")
    del pixmap
    with Image.open(io.BytesIO(pixmap_png)) as rendered:
        image = rendered.convert("L")
    del pixmap_png
    cutoff, contrast, sharpness = parse_profile(row["processing_profile"])
    image = ImageOps.autocontrast(image, cutoff=cutoff)
    image = ImageEnhance.Contrast(image).enhance(contrast)
    image = ImageEnhance.Sharpness(image).enhance(sharpness)
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    image.close()
    return buffer.getvalue()


def pixel_difference_stats(data: bytes, source: Path) -> dict[str, object]:
    Image.MAX_IMAGE_PIXELS = None
    with Image.open(io.BytesIO(data)) as left:
        with Image.open(source) as right:
            left_l = left.convert("L")
            right_l = right.convert("L")
            if left_l.size != right_l.size:
                result = {
                    "dimensions_exact": False,
                    "pixel_exact": False,
                    "changed_pixels": "",
                    "total_pixels": "",
                    "changed_fraction": "",
                    "mean_absolute_error": "",
                    "max_absolute_error": "",
                }
                left_l.close()
                right_l.close()
                return result
            difference = ImageChops.difference(left_l, right_l)
            histogram = difference.histogram()
            changed = sum(histogram[1:])
            total = left_l.width * left_l.height
            result = {
                "dimensions_exact": True,
                "pixel_exact": changed == 0,
                "changed_pixels": changed,
                "total_pixels": total,
                "changed_fraction": round(changed / total, 12),
                "mean_absolute_error": round(
                    float(ImageStat.Stat(difference).mean[0]),
                    12,
                ),
                "max_absolute_error": max(
                    (value for value, count in enumerate(histogram) if count),
                    default=0,
                ),
            }
            difference.close()
            left_l.close()
            right_l.close()
            return result


def check_png(path: Path, row: dict[str, str]) -> list[str]:
    errors: list[str] = []
    Image.MAX_IMAGE_PIXELS = None
    try:
        with Image.open(path) as image:
            image.verify()
        with Image.open(path) as image:
            if image.width != int(row["width_px"]):
                errors.append(f"width mismatch: {path.name}")
            if image.height != int(row["height_px"]):
                errors.append(f"height mismatch: {path.name}")
            if image.mode != row["color_mode"]:
                errors.append(f"mode mismatch: {path.name}")
    except Exception as exc:  # noqa: BLE001
        errors.append(f"PNG decode failed {path.name}: {exc}")
    return errors


def verify_zip(
    path: Path,
    expected: dict[str, tuple[int, str]],
) -> dict[str, Any]:
    errors: list[str] = []
    members: list[dict[str, object]] = []
    with zipfile.ZipFile(path) as archive:
        bad = archive.testzip()
        if bad:
            errors.append(f"bad CRC member: {bad}")
        names = archive.namelist()
        if len(names) != len(set(names)):
            errors.append("duplicate ZIP member")
        if set(names) != set(expected):
            errors.append(
                "exact-set mismatch: "
                f"missing={sorted(set(expected)-set(names))};"
                f"extra={sorted(set(names)-set(expected))}"
            )
        for info in archive.infolist():
            name = info.filename
            unsafe = (
                name.startswith("/")
                or name.startswith("\\")
                or re.match(r"^[A-Za-z]:", name) is not None
                or ".." in Path(name).parts
            )
            if unsafe:
                errors.append(f"unsafe member: {name}")
                continue
            data = archive.read(name)
            identity = (len(data), sha256_bytes(data))
            if name in expected and identity != expected[name]:
                errors.append(f"member identity mismatch: {name}")
            members.append(
                {
                    "path": name,
                    "bytes": len(data),
                    "sha256": sha256_bytes(data),
                }
            )
    members.sort(key=lambda item: str(item["path"]).lower())
    return {
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "members": len(members),
        "member_bytes": sum(int(item["bytes"]) for item in members),
        "member_identity_aggregate_sha256": sha256_bytes(
            "".join(
                f"{item['path']}\t{item['bytes']}\t{item['sha256']}\n"
                for item in members
            ).encode("utf-8")
        ),
    }


def main() -> int:
    args = parse_args()
    package = args.package_dir.resolve()
    zip_dir = args.zip_dir.resolve()
    scratch = args.scratch_dir.resolve()
    parent = args.parent_pdf.resolve()
    cert_log = args.cert_log.resolve()
    errors: list[str] = []
    Image.MAX_IMAGE_PIXELS = None

    files = {path.name: path for path in package.iterdir() if path.is_file()}
    target_manifest = files[
        "SGA6_Targeted_UltraDetail_Crops_idx653_665_Manifest_20260728.csv"
    ]
    excluded_manifest = files[
        "SGA6_GeneratedUnread_Tight_Crops_idx653_665_"
        "Excluded_Manifest_20260728.csv"
    ]
    blocked_manifest = files[
        "SGA6_PageBands_idx653_665_RightsBlocked_Manifest_20260728.csv"
    ]
    audit_manifest = files[
        "SGA6_Targeted_UltraDetail_Crops_idx653_665_"
        "Audit_Context_20260728.csv"
    ]
    validation_path = files[
        "SGA6_Targeted_UltraDetail_Crops_idx653_665_"
        "VALIDATION_20260728.json"
    ]
    upload_manifest = files[
        "SGA6_Targeted_UltraDetail_Crops_idx653_665_"
        "ZENODO_UPLOAD_MANIFEST_20260728.csv"
    ]
    readme = files[
        "SGA6_UltraDetail_Crops_idx653_665_README_20260728.md"
    ]
    parent_json = files[
        "SGA6_UltraDetail_Crops_idx653_665_PARENT_SOURCE_20260728.json"
    ]

    target_rows = rows(target_manifest)
    excluded_rows = rows(excluded_manifest)
    blocked_rows = rows(blocked_manifest)
    audit_rows = rows(audit_manifest)
    upload_rows = rows(upload_manifest)

    if len(target_rows) != TARGET_COUNT:
        errors.append(f"target rows {len(target_rows)} != {TARGET_COUNT}")
    if sum(int(row["bytes"]) for row in target_rows) != TARGET_BYTES:
        errors.append("target bytes mismatch")
    if len(excluded_rows) != EXCLUDED_COUNT:
        errors.append(f"excluded rows {len(excluded_rows)} != {EXCLUDED_COUNT}")
    if len(blocked_rows) != ROUTINE_COUNT:
        errors.append(f"routine rows {len(blocked_rows)} != {ROUTINE_COUNT}")
    if sum(int(row["bytes"]) for row in blocked_rows) != ROUTINE_BYTES:
        errors.append("routine bytes mismatch")
    if len(audit_rows) != END_ENTRY - START_ENTRY + 1:
        errors.append("audit row count mismatch")
    for row in target_rows:
        if int(row["viewer_attachment_count"]) != int(row["session_read_count"]):
            errors.append(
                f"viewer attachment/read count mismatch: {row['source_basename']}"
            )
        if row["viewer_attachment_correlation"] != "PASS":
            errors.append(
                f"viewer attachment correlation is not PASS: "
                f"{row['source_basename']}"
            )
        attachment_hashes = row["viewer_attachment_sha256"].split(";")
        if len(attachment_hashes) != int(row["viewer_attachment_count"]) or any(
            re.fullmatch(r"[0-9A-F]{64}", value) is None
            for value in attachment_hashes
        ):
            errors.append(
                f"viewer attachment hash set invalid: {row['source_basename']}"
            )

    for label, data, key in (
        ("target", target_rows, "archive_path"),
        ("excluded", excluded_rows, "source_basename"),
        ("blocked", blocked_rows, "source_basename"),
    ):
        values = [row[key] for row in data]
        if len(values) != len(set(values)):
            errors.append(f"duplicate {label} {key}")
        hashes = [row["sha256"] for row in data]
        if len(hashes) != len(set(hashes)):
            errors.append(f"duplicate {label} content hash")

    expected_pairs = {
        (entry, START_INDEX + entry - START_ENTRY)
        for entry in range(START_ENTRY, END_ENTRY + 1)
    }
    observed_pairs = {
        (
            int(row["audit_entry_number"]),
            int(row["parent_pdf_index_0based"]),
        )
        for row in audit_rows
    }
    if observed_pairs != expected_pairs:
        errors.append("audit entry/index mapping mismatch")
    headings = audit_headings(cert_log)
    heading_bytes = "\n".join(headings).encode("utf-8")
    if len(headings) != len(audit_rows):
        errors.append("live selected heading count mismatch")
    if sha256_bytes(heading_bytes) != AUDIT_SHA256:
        errors.append("live selected heading aggregate mismatch")

    for path in (
        target_manifest,
        excluded_manifest,
        blocked_manifest,
        audit_manifest,
        upload_manifest,
    ):
        triggers = formula_triggers(path)
        if triggers:
            errors.append(f"formula triggers in {path.name}: {triggers}")

    privacy_paths = (
        target_manifest,
        excluded_manifest,
        blocked_manifest,
        audit_manifest,
        validation_path,
        upload_manifest,
        readme,
        parent_json,
        files[
            "SGA6_Targeted_UltraDetail_Crops_idx653_665_"
            "SHA256SUMS_20260728.txt"
        ],
    )
    public_text = "\n".join(
        path.read_text(encoding="utf-8", errors="replace")
        for path in privacy_paths
    ).lower()
    privacy = [marker for marker in PRIVATE_MARKERS if marker in public_text]
    if privacy:
        errors.append(f"public package privacy hits: {privacy}")

    if (
        not parent.is_file()
        or parent.stat().st_size != PARENT_BYTES
        or sha256(parent) != PARENT_SHA256
    ):
        errors.append("parent identity mismatch")
    document = fitz.open(parent)
    if document.page_count != PARENT_PAGES:
        errors.append("parent page count mismatch")

    replay_details: dict[str, dict[str, object]] = {}
    for index, row in enumerate(target_rows, start=1):
        source = scratch / row["source_basename"]
        if not source.is_file():
            errors.append(f"missing target source: {source.name}")
            continue
        if source.stat().st_size != int(row["bytes"]) or sha256(source) != row[
            "sha256"
        ]:
            errors.append(f"target source identity mismatch: {source.name}")
        errors.extend(check_png(source, row))
        data = replay_png(document, row)
        byte_exact = data == source.read_bytes()
        difference = pixel_difference_stats(data, source)
        pixel_exact = bool(difference["pixel_exact"])
        expected_disposition = (
            "pixel_exact_and_png_byte_exact"
            if pixel_exact and byte_exact
            else (
                (
                    "dimensions_exact_renderer_version_pixel_drift_disclosed_"
                    "source_identity_and_viewer_attachment_correlation_pass"
                )
                if bool(difference["dimensions_exact"])
                else (
                    "renderer_version_geometry_and_pixel_drift_disclosed_"
                    "source_identity_and_viewer_attachment_correlation_pass"
                )
            )
        )
        if row["replay_disposition"] != expected_disposition:
            errors.append(f"target replay disposition mismatch: {source.name}")
        replay_details[source.name] = {
            "pixel_exact": pixel_exact,
            "png_byte_exact": byte_exact,
            "dimensions_exact": bool(difference["dimensions_exact"]),
            "replay_sha256": sha256_bytes(data),
            "difference": difference,
        }
        del data
        if index % 10 == 0 or index == len(target_rows):
            print(f"independent target replay: {index}/{len(target_rows)}", flush=True)
        gc.collect()

    metadata_only_rows = excluded_rows + blocked_rows
    for row in metadata_only_rows:
        source = scratch / row["source_basename"]
        if not source.is_file():
            errors.append(f"missing metadata-only source: {source.name}")
            continue
        if source.stat().st_size != int(row["bytes"]) or sha256(source) != row[
            "sha256"
        ]:
            errors.append(f"metadata-only identity mismatch: {source.name}")
        errors.extend(check_png(source, row))

    target_zip_row = next(
        row
        for row in upload_rows
        if row["role"] == "targeted_ultradetail_image_archive"
    )
    metadata_zip_row = next(
        row
        for row in upload_rows
        if row["role"] == "provenance_and_rights_blocked_metadata_archive"
    )
    target_zip = zip_dir / target_zip_row["filename"]
    metadata_zip = zip_dir / metadata_zip_row["filename"]
    for path, row in (
        (target_zip, target_zip_row),
        (metadata_zip, metadata_zip_row),
    ):
        if not path.is_file():
            errors.append(f"missing outer ZIP: {path.name}")
        elif (
            path.stat().st_size != int(row["bytes"])
            or sha256(path) != row["sha256"]
        ):
            errors.append(f"outer ZIP identity mismatch: {path.name}")

    target_expected = {
        row["archive_path"]: (int(row["bytes"]), row["sha256"])
        for row in target_rows
    }
    for path in (
        readme,
        parent_json,
        target_manifest,
        excluded_manifest,
        audit_manifest,
    ):
        target_expected[f"metadata/{path.name}"] = (
            path.stat().st_size,
            sha256(path),
        )
    metadata_expected = {
        f"metadata/{path.name}": (path.stat().st_size, sha256(path))
        for path in (
            readme,
            parent_json,
            target_manifest,
            excluded_manifest,
            blocked_manifest,
            audit_manifest,
        )
    }
    target_zip_result = verify_zip(target_zip, target_expected)
    metadata_zip_result = verify_zip(metadata_zip, metadata_expected)
    errors.extend(target_zip_result["errors"])
    errors.extend(metadata_zip_result["errors"])

    producer_validation = json.loads(validation_path.read_text(encoding="utf-8"))
    if producer_validation.get("status") != "PASS":
        errors.append("producer validation is not PASS")
    if producer_validation.get("errors") != []:
        errors.append("producer validation has errors")
    producer_replay = producer_validation.get("target_replay", {})
    for field, observed in (
        (
            "dimensions_exact",
            sum(bool(item["dimensions_exact"]) for item in replay_details.values()),
        ),
        (
            "pixel_exact",
            sum(bool(item["pixel_exact"]) for item in replay_details.values()),
        ),
        (
            "png_byte_exact",
            sum(bool(item["png_byte_exact"]) for item in replay_details.values()),
        ),
    ):
        if int(producer_replay.get(field, -1)) != observed:
            errors.append(f"producer/independent replay count mismatch: {field}")

    result = {
        "schema": "sga6_targeted_ultradetail_idx653_665_independent_replay_v1",
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "targeted_images": len(target_rows),
        "targeted_image_bytes": sum(int(row["bytes"]) for row in target_rows),
        "target_replay_dimensions_exact": sum(
            bool(item["dimensions_exact"]) for item in replay_details.values()
        ),
        "target_replay_pixel_exact": sum(
            bool(item["pixel_exact"]) for item in replay_details.values()
        ),
        "target_replay_png_byte_exact": sum(
            bool(item["png_byte_exact"]) for item in replay_details.values()
        ),
        "generated_unread_tight_metadata_rows": len(excluded_rows),
        "viewer_attachment_events": sum(
            int(row["viewer_attachment_count"]) for row in target_rows
        ),
        "viewer_attachment_correlations_pass": sum(
            row["viewer_attachment_correlation"] == "PASS"
            for row in target_rows
        ),
        "routine_rights_blocked_metadata_rows": len(blocked_rows),
        "metadata_only_source_identities_and_png_decode_exact": len(
            metadata_only_rows
        ),
        "audit_rows": len(audit_rows),
        "audit_heading_aggregate_sha256": sha256_bytes(heading_bytes),
        "privacy_hits": privacy,
        "target_zip": {
            "filename": target_zip.name,
            "bytes": target_zip.stat().st_size,
            "sha256": sha256(target_zip),
            **target_zip_result,
        },
        "metadata_zip": {
            "filename": metadata_zip.name,
            "bytes": metadata_zip.stat().st_size,
            "sha256": sha256(metadata_zip),
            **metadata_zip_result,
        },
    }
    output_json = package / "INDEPENDENT_REPLAY_VALIDATION_20260728.json"
    output_json.write_text(
        json.dumps(result, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    report = package / "INDEPENDENT_REPLAY_PASS_20260728.md"
    report.write_text(
        "# Independent replay: SGA6 idx653-665 ultra-detail crops\n\n"
        f"Status: **{result['status']}**\n\n"
        f"- Targeted source PNGs: {len(target_rows)}/{TARGET_COUNT} exact "
        "identities, all with PASS viewer-attachment correlation.\n"
        f"- Fresh replay dimensions: "
        f"{result['target_replay_dimensions_exact']}/{TARGET_COUNT} exact; "
        f"pixel/PNG exact: {result['target_replay_pixel_exact']}/"
        f"{TARGET_COUNT}.\n"
        f"- Generated-but-unread tight crops: {len(excluded_rows)} exact "
        "metadata-only identities.\n"
        f"- Routine rights-blocked page bands: {len(blocked_rows)} exact "
        "metadata-only identities and valid PNG decodes.\n"
        f"- Audit boundary: entries {START_ENTRY}-{END_ENTRY}, "
        f"idx{START_INDEX}-idx{END_INDEX}, {len(audit_rows)} rows.\n"
        f"- Target ZIP: `{target_zip.name}`, {target_zip.stat().st_size:,} "
        f"bytes, SHA-256 `{sha256(target_zip)}`.\n"
        f"- Metadata ZIP: `{metadata_zip.name}`, "
        f"{metadata_zip.stat().st_size:,} bytes, SHA-256 "
        f"`{sha256(metadata_zip)}`.\n"
        f"- Errors: `{errors}`.\n\n"
        "This verifies sparse provenance and QA evidence only. It does not "
        "certify transcription, translation, mathematics, completeness, "
        "rights clearance, or critical-edition status.\n",
        encoding="utf-8",
    )
    document.close()
    print(json.dumps(result, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
