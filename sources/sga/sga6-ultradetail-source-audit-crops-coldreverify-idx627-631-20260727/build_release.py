#!/usr/bin/env python3
"""Build the SGA6 idx627-631 rights-curated crop release.

Only tight crops that the source-audit session actually opened are included
as pixels. Generated-but-unread alternatives and routine page bands are
represented by exact metadata without redistributing their pixels.
"""

from __future__ import annotations

import argparse
import csv
import gc
import hashlib
import io
import json
import re
import zipfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import fitz
from PIL import Image, ImageChops, ImageEnhance, ImageOps, ImageStat


DATE_TAG = "20260727"
PACKAGE_TAG = "idx627_631"
TARGET_ZIP = (
    "10x_SGA6_SourceAudit_Targeted_UltraDetail_Crops_"
    f"{PACKAGE_TAG}_{DATE_TAG}.zip"
)
METADATA_ZIP = (
    "10y_SGA6_SourceAudit_Crop_Provenance_RightsBlocked_Metadata_"
    f"{PACKAGE_TAG}_{DATE_TAG}.zip"
)
README_NAME = f"SGA6_UltraDetail_Crops_{PACKAGE_TAG}_README_{DATE_TAG}.md"
PARENT_NAME = f"SGA6_UltraDetail_Crops_{PACKAGE_TAG}_PARENT_SOURCE_{DATE_TAG}.json"
TARGET_MANIFEST_NAME = (
    f"SGA6_Targeted_UltraDetail_Crops_{PACKAGE_TAG}_Manifest_{DATE_TAG}.csv"
)
EXCLUDED_MANIFEST_NAME = (
    f"SGA6_GeneratedUnread_Tight_Crops_{PACKAGE_TAG}_"
    f"Excluded_Manifest_{DATE_TAG}.csv"
)
BLOCKED_MANIFEST_NAME = (
    f"SGA6_PageBands_{PACKAGE_TAG}_RightsBlocked_Manifest_{DATE_TAG}.csv"
)
AUDIT_CONTEXT_NAME = (
    f"SGA6_Targeted_UltraDetail_Crops_{PACKAGE_TAG}_Audit_Context_{DATE_TAG}.csv"
)
VALIDATION_NAME = (
    f"SGA6_Targeted_UltraDetail_Crops_{PACKAGE_TAG}_VALIDATION_{DATE_TAG}.json"
)
UPLOAD_MANIFEST_NAME = (
    f"SGA6_Targeted_UltraDetail_Crops_{PACKAGE_TAG}_"
    f"ZENODO_UPLOAD_MANIFEST_{DATE_TAG}.csv"
)
SHA_NAME = (
    f"SGA6_Targeted_UltraDetail_Crops_{PACKAGE_TAG}_SHA256SUMS_{DATE_TAG}.txt"
)

PARENT_SHA256 = "73FBBAD41340C12ECCDCFCF6C3A1656953FE3D712AA8E391678458CCD17B4BAA"
PARENT_BYTES = 26_833_956
PARENT_PAGES = 720
START_INDEX = 627
END_INDEX = 631
START_ENTRY = 1379
END_ENTRY = 1383
SELECTED_AUDIT_ROWS = 5
SELECTED_AUDIT_SHA256 = (
    "3D56CA97C97CFFC52707BEB5D7E53F57AF47312C4F8A3AF98CF7B1ACBE084BE3"
)
EXPECTED_TIGHT_FILES = 2
EXPECTED_OPENED_TIGHT_FILES = 2
EXPECTED_OPENED_TIGHT_BYTES = 379_504
EXPECTED_UNREAD_TIGHT_FILES = 0
EXPECTED_ROUTINE_FILES = 25
EXPECTED_ROUTINE_BYTES = 7_402_000
LINKED_TEX_OBJECT = "sga6_fr_workpass.tex"

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
    parser.add_argument("--provenance-json", type=Path, required=True)
    parser.add_argument("--scratch-dir", type=Path, required=True)
    parser.add_argument("--parent-pdf", type=Path, required=True)
    parser.add_argument("--cert-log", type=Path, required=True)
    parser.add_argument("--prior-public-readback", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--zip-dir", type=Path, required=True)
    return parser.parse_args()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest().upper()


def utc_mtime(path: Path) -> str:
    return datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).isoformat()


def write_text(path: Path, value: str) -> None:
    path.write_bytes(value.encode("utf-8"))


def write_csv(
    path: Path,
    rows: list[dict[str, object]],
    fields: list[str],
) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def privacy_hits(values: list[str]) -> list[str]:
    joined = "\n".join(values).lower()
    return sorted(marker for marker in PRIVATE_MARKERS if marker in joined)


def sanitize_public_text(value: str) -> str:
    value = re.sub(r"(?i)\bfloris\b", "[archive owner]", value)
    value = re.sub(r"(?i)\b(?:claude|codex)\b", "[agent]", value)
    value = re.sub(
        r"(?i)\b[a-z]:\\(?:[^\\\s,;)\]]+\\)*[^,\r\n;)\]]*",
        "[private path]",
        value,
    )
    value = value.replace("\x00", "")
    return re.sub(r"\s+", " ", value).strip()


def formula_triggers(path: Path) -> list[str]:
    triggers: list[str] = []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        for row_number, row in enumerate(csv.reader(handle), start=1):
            for column_number, cell in enumerate(row, start=1):
                if cell.startswith(FORMULA_PREFIXES):
                    triggers.append(f"R{row_number}C{column_number}:{cell[:40]}")
    return triggers


def png_metadata(path: Path) -> dict[str, object]:
    Image.MAX_IMAGE_PIXELS = None
    with Image.open(path) as image:
        image.verify()
    with Image.open(path) as image:
        dpi = image.info.get("dpi")
        return {
            "width_px": image.width,
            "height_px": image.height,
            "color_mode": image.mode,
            "embedded_dpi_x": round(float(dpi[0]), 4) if dpi else "",
            "embedded_dpi_y": round(float(dpi[1]), 4) if dpi else "",
            "metadata_text": json.dumps(
                {str(key): str(value) for key, value in image.info.items()},
                sort_keys=True,
                ensure_ascii=True,
            ),
        }


def expose_for_index(index: int) -> str:
    if index <= 428:
        return "VI"
    if index <= 478:
        return "VII"
    if index <= 510:
        return "VIII"
    if index <= 531:
        return "IX"
    if index <= 571:
        return "X"
    if index <= 607:
        return "X Appendix"
    if index <= 628:
        return "XII"
    return "XIII"


def audit_headings(cert_bytes: bytes) -> list[str]:
    headings: list[tuple[int, str]] = []
    pattern = re.compile(r"^### #(?P<entry>\d+)\b")
    for line in cert_bytes.decode("utf-8", errors="replace").splitlines():
        match = pattern.match(line)
        if not match:
            continue
        entry = int(match.group("entry"))
        if START_ENTRY <= entry <= END_ENTRY:
            headings.append((entry, line))
    headings.sort(key=lambda item: item[0])
    return [line for _, line in headings]


def parse_iso_timestamp(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def build_audit_rows(cert_bytes: bytes) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    pattern = re.compile(
        r"^### #(?P<entry>\d+).*?\bidx(?P<index>\d+)\b",
        re.IGNORECASE,
    )
    for line in audit_headings(cert_bytes):
        match = pattern.match(line)
        if not match:
            continue
        entry = int(match.group("entry"))
        index = int(match.group("index"))
        normalized = sanitize_public_text(line)
        if len(normalized) > 1800:
            normalized = normalized[:1797] + "..."
        raw = line.encode("utf-8")
        rows.append(
            {
                "audit_entry_number": entry,
                "parent_pdf_index_0based": index,
                "parent_pdf_page_1based": index + 1,
                "printed_page": index - 13,
                "expose": expose_for_index(index),
                "raw_heading_bytes": len(raw),
                "raw_heading_sha256": sha256_bytes(raw),
                "sanitized_audit_heading": normalized,
            }
        )
    return rows


def processing_profile(row: dict[str, Any]) -> str:
    return (
        "grayscale;"
        f"autocontrast_cutoff_{row['autocontrast_cutoff']};"
        f"contrast_{row['contrast']};"
        f"sharpness_{row['sharpness']}"
    )


def public_crop_row(
    source: dict[str, Any],
    *,
    category: str,
    disposition: str,
    archive_path: str,
    audit_entry: int,
    qa_disposition: str,
    replay_disposition: str,
) -> dict[str, object]:
    description = sanitize_public_text(str(source.get("description") or ""))
    attachments = list(source.get("read_attachment_events") or [])
    return {
        "archive_path": archive_path,
        "source_basename": source["basename"],
        "bytes": source["bytes"],
        "sha256": source["sha256"],
        "width_px": source["width_px"],
        "height_px": source["height_px"],
        "color_mode": source["mode"],
        "embedded_dpi_x": (
            source["embedded_dpi"][0] if source.get("embedded_dpi") else ""
        ),
        "embedded_dpi_y": (
            source["embedded_dpi"][1] if source.get("embedded_dpi") else ""
        ),
        "modified_utc": source["mtime_utc"],
        "category": category,
        "public_disposition": disposition,
        "parent_pdf_index_0based": source["index"],
        "parent_pdf_page_1based": int(source["index"]) + 1,
        "printed_page": int(source["index"]) - 13,
        "expose": expose_for_index(int(source["index"])),
        "linked_tex_object": LINKED_TEX_OBJECT,
        "linked_audit_entry": audit_entry,
        "generator_script_basename": source["generator_script_basename"],
        "generator_source_sha256": source["generator_source_sha256"],
        "generator_timestamp": source["generator_timestamp"],
        "generator_tool_class": source["generator_tool_name"],
        "generator_candidate_count": source["generator_candidate_count"],
        "bbox_coordinate_system": "fraction_of_parent_page",
        "bbox_fx0": source["bbox_fx0"],
        "bbox_fy0": source["bbox_fy0"],
        "bbox_fx1": source["bbox_fx1"],
        "bbox_fy1": source["bbox_fy1"],
        "render_dpi": source["render_dpi"],
        "processing_profile": processing_profile(source),
        "description": description,
        "session_read_count": source["read_count"],
        "first_read_timestamp": source["first_read_timestamp"],
        "last_read_timestamp": source["last_read_timestamp"],
        "viewer_attachment_count": len(attachments),
        "viewer_attachment_sha256": ";".join(
            str(item["attachment_sha256"]) for item in attachments
        ),
        "viewer_attachment_dimensions": ";".join(
            f"{item['attachment_width_px']}x{item['attachment_height_px']}"
            for item in attachments
        ),
        "viewer_source_lanczos_max_mean_absolute_error": (
            max(
                float(item["source_lanczos_mean_absolute_error"])
                for item in attachments
            )
            if attachments
            else ""
        ),
        "viewer_source_lanczos_max_changed_fraction": (
            max(
                float(item["source_lanczos_changed_fraction"])
                for item in attachments
            )
            if attachments
            else ""
        ),
        "viewer_attachment_correlation": (
            "PASS"
            if attachments
            and all(
                bool(item["source_attachment_correlation_pass"])
                for item in attachments
            )
            else ""
        ),
        "replay_disposition": replay_disposition,
        "qa_disposition": qa_disposition,
        "parent_scan_sha256": PARENT_SHA256,
    }


def render_crop_bytes(
    document: fitz.Document,
    row: dict[str, Any],
) -> tuple[tuple[int, int], bytes]:
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
    image = ImageOps.autocontrast(
        image,
        cutoff=row["autocontrast_cutoff"],
    )
    image = ImageEnhance.Contrast(image).enhance(float(row["contrast"]))
    image = ImageEnhance.Sharpness(image).enhance(float(row["sharpness"]))
    dimensions = image.size
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    image.close()
    return dimensions, buffer.getvalue()


def pixel_difference_stats(left_bytes: bytes, right_path: Path) -> dict[str, object]:
    Image.MAX_IMAGE_PIXELS = None
    with Image.open(io.BytesIO(left_bytes)) as left:
        with Image.open(right_path) as right:
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
            mean_error = float(ImageStat.Stat(difference).mean[0])
            max_error = max(
                (value for value, count in enumerate(histogram) if count),
                default=0,
            )
            result = {
                "dimensions_exact": True,
                "pixel_exact": changed == 0,
                "changed_pixels": changed,
                "total_pixels": total,
                "changed_fraction": round(changed / total, 12),
                "mean_absolute_error": round(mean_error, 12),
                "max_absolute_error": max_error,
            }
            difference.close()
            left_l.close()
            right_l.close()
            return result


def readback_hashes(path: Path | None) -> set[str]:
    if not path or not path.is_file():
        return set()
    text = path.read_text(encoding="utf-8", errors="replace").upper()
    return set(re.findall(r"\b[0-9A-F]{64}\b", text))


def add_zip_file(
    archive: zipfile.ZipFile,
    source: Path,
    member: str,
) -> None:
    info = zipfile.ZipInfo(member, date_time=(2026, 7, 27, 0, 0, 0))
    info.compress_type = zipfile.ZIP_STORED
    info.create_system = 3
    info.external_attr = 0o100644 << 16
    archive.writestr(info, source.read_bytes())


def build_zip(
    path: Path,
    image_rows: list[dict[str, object]],
    scratch_dir: Path,
    metadata_paths: list[Path],
) -> dict[str, object]:
    expected: dict[str, tuple[int, str]] = {}
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_STORED) as archive:
        for row in image_rows:
            source = scratch_dir / str(row["source_basename"])
            member = str(row["archive_path"])
            add_zip_file(archive, source, member)
            expected[member] = (source.stat().st_size, sha256(source))
        for source in metadata_paths:
            member = f"metadata/{source.name}"
            add_zip_file(archive, source, member)
            expected[member] = (source.stat().st_size, sha256(source))

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
                "ZIP exact-set mismatch: "
                f"missing={sorted(set(expected)-set(names))}; "
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
                errors.append(f"unsafe ZIP member: {name}")
                continue
            data = archive.read(name)
            observed = (len(data), sha256_bytes(data))
            if name in expected and observed != expected[name]:
                errors.append(f"ZIP member identity mismatch: {name}")
            members.append(
                {
                    "path": name,
                    "bytes": len(data),
                    "sha256": sha256_bytes(data),
                }
            )
    members.sort(key=lambda row: str(row["path"]).lower())
    aggregate = sha256_bytes(
        "".join(
            f"{row['path']}\t{row['bytes']}\t{row['sha256']}\n"
            for row in members
        ).encode("utf-8")
    )
    return {
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "members": len(members),
        "member_bytes": sum(int(row["bytes"]) for row in members),
        "member_identity_aggregate_sha256": aggregate,
    }


def main() -> int:
    args = parse_args()
    provenance_path = args.provenance_json.resolve()
    scratch_dir = args.scratch_dir.resolve()
    parent_pdf = args.parent_pdf.resolve()
    cert_log = args.cert_log.resolve()
    output_dir = args.output_dir.resolve()
    zip_dir = args.zip_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    zip_dir.mkdir(parents=True, exist_ok=True)

    errors: list[str] = []
    Image.MAX_IMAGE_PIXELS = None

    provenance = json.loads(provenance_path.read_text(encoding="utf-8"))
    if provenance.get("tight_provenance_mapping_errors"):
        errors.append(
            "tight provenance mapping errors: "
            f"{provenance['tight_provenance_mapping_errors']}"
        )
    if provenance.get("routine_provenance_mapping_warnings"):
        errors.append(
            "routine provenance mapping warnings: "
            f"{provenance['routine_provenance_mapping_warnings']}"
        )
    tight = list(provenance["files"])
    routine = list(provenance["routine_files"])
    opened = [row for row in tight if int(row["read_count"]) > 0]
    unread = [row for row in tight if int(row["read_count"]) == 0]
    if len(tight) != EXPECTED_TIGHT_FILES:
        errors.append(f"tight count {len(tight)} != {EXPECTED_TIGHT_FILES}")
    if len(opened) != EXPECTED_OPENED_TIGHT_FILES:
        errors.append(
            f"opened tight count {len(opened)} != {EXPECTED_OPENED_TIGHT_FILES}"
        )
    if sum(int(row["bytes"]) for row in opened) != EXPECTED_OPENED_TIGHT_BYTES:
        errors.append("opened tight byte count mismatch")
    if len(unread) != EXPECTED_UNREAD_TIGHT_FILES:
        errors.append(
            f"unread tight count {len(unread)} != {EXPECTED_UNREAD_TIGHT_FILES}"
        )
    if len(routine) != EXPECTED_ROUTINE_FILES:
        errors.append(f"routine count {len(routine)} != {EXPECTED_ROUTINE_FILES}")
    if sum(int(row["bytes"]) for row in routine) != EXPECTED_ROUTINE_BYTES:
        errors.append("routine byte count mismatch")
    attachment_events = [
        event
        for row in opened
        for event in row.get("read_attachment_events", [])
    ]
    if len(attachment_events) != sum(int(row["read_count"]) for row in opened):
        errors.append("viewer attachment count does not match selected read events")
    if not all(
        bool(event["source_attachment_correlation_pass"])
        for event in attachment_events
    ):
        errors.append("one or more selected viewer attachments do not correlate")
    for row in opened:
        if parse_iso_timestamp(str(row["first_read_timestamp"])) < parse_iso_timestamp(
            str(row["mtime_utc"])
        ):
            errors.append(f"read event predates selected source file: {row['basename']}")

    if (
        not parent_pdf.is_file()
        or parent_pdf.stat().st_size != PARENT_BYTES
        or sha256(parent_pdf) != PARENT_SHA256
    ):
        errors.append("parent PDF identity mismatch")
    document = fitz.open(parent_pdf)
    if document.page_count != PARENT_PAGES:
        errors.append(
            f"parent page count is {document.page_count}, expected {PARENT_PAGES}"
        )

    cert_bytes = cert_log.read_bytes()
    headings = audit_headings(cert_bytes)
    selected_audit_bytes = "\n".join(headings).encode("utf-8")
    selected_audit_sha = sha256_bytes(selected_audit_bytes)
    if len(headings) != SELECTED_AUDIT_ROWS:
        errors.append(
            f"selected audit rows {len(headings)} != {SELECTED_AUDIT_ROWS}"
        )
    if selected_audit_sha != SELECTED_AUDIT_SHA256:
        errors.append(
            "selected audit digest mismatch: "
            f"{selected_audit_sha} != {SELECTED_AUDIT_SHA256}"
        )
    audit_rows = build_audit_rows(cert_bytes)
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
        errors.append(
            "audit entry/index mapping mismatch: "
            f"missing={sorted(expected_pairs-observed_pairs)}; "
            f"extra={sorted(observed_pairs-expected_pairs)}"
        )
    audit_by_index = {
        int(row["parent_pdf_index_0based"]): int(row["audit_entry_number"])
        for row in audit_rows
    }

    source_rows = tight + routine
    initial_identities: dict[str, tuple[int, int, str]] = {}
    for row in source_rows:
        path = scratch_dir / str(row["basename"])
        if not path.is_file():
            errors.append(f"missing source image: {row['basename']}")
            continue
        stat = path.stat()
        digest = sha256(path)
        initial_identities[str(row["basename"])] = (
            stat.st_size,
            stat.st_mtime_ns,
            digest,
        )
        if stat.st_size != int(row["bytes"]) or digest != row["sha256"]:
            errors.append(f"source identity mismatch: {row['basename']}")
        meta = png_metadata(path)
        if (
            int(meta["width_px"]) != int(row["width_px"])
            or int(meta["height_px"]) != int(row["height_px"])
            or str(meta["color_mode"]) != str(row["mode"])
        ):
            errors.append(f"source PNG metadata mismatch: {row['basename']}")
        hits = privacy_hits([str(row["basename"]), str(meta["metadata_text"])])
        if hits:
            errors.append(f"source PNG privacy hit {row['basename']}: {hits}")

    public_hashes = readback_hashes(args.prior_public_readback)
    target_hashes = {str(row["sha256"]) for row in opened}
    prior_intersection = sorted(target_hashes & public_hashes)
    if prior_intersection:
        errors.append(
            f"target image hashes already public: {prior_intersection}"
        )

    target_rows: list[dict[str, object]] = []
    excluded_rows: list[dict[str, object]] = []
    blocked_rows: list[dict[str, object]] = []
    replay: dict[str, dict[str, object]] = {}

    for count, source in enumerate(
        sorted(opened, key=lambda row: (int(row["index"]), row["basename"])),
        start=1,
    ):
        name = str(source["basename"])
        image_path = scratch_dir / name
        dimensions, replay_bytes = render_crop_bytes(document, source)
        byte_exact = replay_bytes == image_path.read_bytes()
        difference = pixel_difference_stats(replay_bytes, image_path)
        pixel_exact = bool(difference["pixel_exact"])
        dimensions_exact = dimensions == (
            int(source["width_px"]),
            int(source["height_px"]),
        )
        if not dimensions_exact or not bool(difference["dimensions_exact"]):
            errors.append(f"target replay dimension mismatch: {name}")
        index = int(source["index"])
        replay_disposition = (
            "pixel_exact_and_png_byte_exact"
            if pixel_exact and byte_exact
            else (
                "dimensions_exact_renderer_version_pixel_drift_disclosed_"
                "source_identity_and_viewer_attachment_correlation_pass"
            )
        )
        target_rows.append(
            public_crop_row(
                source,
                category="targeted_symbol_formula_ultradetail_crop",
                disposition=(
                    "public_targeted_source_audit_evidence_no_license_grant"
                ),
                archive_path=f"images/targeted_ultradetail/{name}",
                audit_entry=audit_by_index[index],
                qa_disposition=(
                    "opened_in_cold_source_reverification_not_translation_"
                    "certification"
                ),
                replay_disposition=replay_disposition,
            )
        )
        replay[name] = {
            "pixel_exact": pixel_exact,
            "png_byte_exact": byte_exact,
            "dimensions_exact": dimensions_exact,
            "replay_sha256": sha256_bytes(replay_bytes),
            "difference": difference,
        }
        del replay_bytes
        if count % 10 == 0 or count == len(opened):
            print(f"replayed targeted crops: {count}/{len(opened)}", flush=True)
        gc.collect()

    for source in sorted(
        unread,
        key=lambda row: (int(row["index"]), row["basename"]),
    ):
        index = int(source["index"])
        excluded_rows.append(
            public_crop_row(
                source,
                category="generated_unread_tight_crop",
                disposition="metadata_only_not_selected_no_read_event",
                archive_path="",
                audit_entry=audit_by_index[index],
                qa_disposition=(
                    "generated_but_not_opened_excluded_from_target_archive"
                ),
                replay_disposition="not_replayed_not_public",
            )
        )

    for source in sorted(
        routine,
        key=lambda row: (int(row["index"]), row["basename"]),
    ):
        index = int(source["index"])
        blocked_rows.append(
            public_crop_row(
                source,
                category="routine_full_width_page_band_derivative",
                disposition="rights_blocked_not_public",
                archive_path="",
                audit_entry=audit_by_index[index],
                qa_disposition=(
                    "routine_page_band_metadata_only_pixels_withheld_for_rights"
                ),
                replay_disposition=(
                    "source_identity_and_png_decode_verified_no_pixel_replay"
                ),
            )
        )

    target_manifest = output_dir / TARGET_MANIFEST_NAME
    excluded_manifest = output_dir / EXCLUDED_MANIFEST_NAME
    blocked_manifest = output_dir / BLOCKED_MANIFEST_NAME
    audit_context = output_dir / AUDIT_CONTEXT_NAME
    crop_fieldnames = list(target_rows[0])
    write_csv(target_manifest, target_rows, crop_fieldnames)
    write_csv(excluded_manifest, excluded_rows, crop_fieldnames)
    write_csv(blocked_manifest, blocked_rows, crop_fieldnames)
    write_csv(audit_context, audit_rows, list(audit_rows[0]))

    parent_identity = {
        "title": "Theorie des intersections et theoreme de Riemann-Roch",
        "series_context": "SGA 6 source-audit parent reader",
        "source_file_basename": parent_pdf.name,
        "bytes": parent_pdf.stat().st_size,
        "sha256": PARENT_SHA256,
        "pages": document.page_count,
        "pdf_metadata": document.metadata,
        "rotation": 0,
        "parent_scan_not_duplicated_in_this_release": True,
        "rights_status": (
            "Underlying French work and scan rights remain with their holders. "
            "No blanket license or rights transfer is asserted."
        ),
        "crop_publication_policy": {
            "included_tight_crops_opened_during_audit": len(target_rows),
            "generated_unread_tight_crops_metadata_only": len(excluded_rows),
            "routine_page_bands_rights_blocked_metadata_only": len(blocked_rows),
        },
        "render_resolution_caveat": (
            "Render DPI describes computational rasterization and enlargement, "
            "not new optical detail beyond the parent scan."
        ),
        "audit_boundary": {
            "first_entry": START_ENTRY,
            "last_entry": END_ENTRY,
            "entries": len(audit_rows),
            "first_parent_pdf_index_0based": START_INDEX,
            "last_parent_pdf_index_0based": END_INDEX,
            "raw_heading_aggregate_sha256_no_terminal_lf": selected_audit_sha,
        },
        "session_evidence": {
            "raw_session_not_bundled": True,
            "source_session_bytes_at_extraction": provenance[
                "source_session_bytes"
            ],
            "source_session_mtime_utc_at_extraction": provenance[
                "source_session_mtime_utc"
            ],
            "selected_open_events": provenance["total_selected_read_events"],
            "selected_files_with_open_events": provenance[
                "files_with_read_events"
            ],
            "selected_viewer_attachment_events": provenance[
                "selected_read_attachment_events"
            ],
            "selected_viewer_attachment_correlations_pass": provenance[
                "selected_read_attachment_correlations_pass"
            ],
            "generator_sources_recovered": provenance[
                "generation_source_count"
            ],
            "retained_page_band_scripts_parsed": provenance[
                "retained_generator_script_count"
            ],
            "malformed_candidate_lines": provenance["session_scan"][
                "malformed_candidate_lines"
            ],
        },
        "claim_boundary": (
            "Sparse visual provenance and QA evidence through idx631 only; "
            "not continuous scan republication, transcription certification, "
            "translation certification, mathematical certification, or a "
            "critical edition."
        ),
    }
    parent_path = output_dir / PARENT_NAME
    write_text(
        parent_path,
        json.dumps(parent_identity, indent=2, ensure_ascii=True) + "\n",
    )

    counts = Counter(int(row["parent_pdf_index_0based"]) for row in target_rows)
    ranges = Counter(str(row["expose"]) for row in audit_rows)
    exact_replay_count = sum(
        bool(item["pixel_exact"]) and bool(item["png_byte_exact"])
        for item in replay.values()
    )
    drift_replay_count = len(replay) - exact_replay_count
    readme = f"""# SGA6 targeted ultra-detail source-audit crops, indices 627-631

This no-overwrite release preserves the tight symbol, formula, punctuation,
prime-mark, overline, diagram-label, and emphasis crops that were actually
opened during the current SGA6 cold source re-verification after the prior
idx612-617 tranche.

## Public image archive

- `{TARGET_ZIP}` contains {len(target_rows)} targeted images /
  {sum(int(row['bytes']) for row in target_rows):,} image bytes.
- The {len(target_rows)} images record
  {sum(int(row['session_read_count']) for row in target_rows)} explicit
  inspection events across
  {len(counts)} distinct parent pages.
- Computational render resolutions range from
  {min(int(row['render_dpi']) for row in target_rows):,} to
  {max(int(row['render_dpi']) for row in target_rows):,} DPI.
- Every included full-resolution PNG is frozen by exact identity and correlated
  to the downsampled viewer attachment returned to the source-audit viewer for its recorded
  `Read` event. All {len(target_rows)} attachment correlations pass.
- A fresh local replay reproduced dimensions for all {len(target_rows)} crops.
  {exact_replay_count} also matched pixel-for-pixel and PNG-byte-for-PNG-byte;
  {drift_replay_count} show disclosed renderer-version pixel drift while the
  source PNG and viewer attachment remain exact.

{len(excluded_rows)} additional tight crop(s) were generated but never opened in
the audit session. It is not included as pixels; `{EXCLUDED_MANIFEST_NAME}`
records its exact identity and provenance without treating it as used evidence.

## Rights-blocked routine bands

`{BLOCKED_MANIFEST_NAME}` records {len(blocked_rows):,} routine full-width
page bands / {sum(int(row['bytes']) for row in blocked_rows):,} bytes. Their
hashes, dimensions, page mappings, fractional boxes, render profiles, and
inspection-event counts are public, but their pixels are withheld. They are
redundant enlargements of the parent scan, not the high-value symbol-level
evidence selected for this release.

## Boundary and claims

The selected audit boundary is entries #{START_ENTRY}-#{END_ENTRY}, mapping
one-to-one to parent PDF indices {START_INDEX}-{END_INDEX}. The boundary spans
the close of Expose XII and the opening of Expose XIII through Proposition 1.4
and its diagram chase at idx631. The next live page, idx632, is excluded.

Audit entries by section label: {dict(sorted(ranges.items()))}.

This package is sparse provenance and QA evidence. It does not certify the
French transcription, English translation, mathematics, completeness, or
critical-edition status. The parent is the {PARENT_PAGES}-page reader
`{parent_pdf.name}`, {PARENT_BYTES:,} bytes, SHA-256 `{PARENT_SHA256}`. The
parent PDF is not bundled. Underlying French work and scan rights remain with
their holders; no blanket license or rights transfer is asserted.
"""
    readme_path = output_dir / README_NAME
    write_text(readme_path, readme)

    metadata_paths = [
        readme_path,
        parent_path,
        target_manifest,
        excluded_manifest,
        blocked_manifest,
        audit_context,
    ]
    metadata_privacy: dict[str, list[str]] = {}
    for path in metadata_paths:
        hits = privacy_hits(
            [path.read_text(encoding="utf-8", errors="replace")]
        )
        if hits:
            metadata_privacy[path.name] = hits
    if metadata_privacy:
        errors.append(f"generated metadata privacy hits: {metadata_privacy}")

    csv_paths = [
        target_manifest,
        excluded_manifest,
        blocked_manifest,
        audit_context,
    ]
    formula_errors = {path.name: formula_triggers(path) for path in csv_paths}
    for name, triggers in formula_errors.items():
        if triggers:
            errors.append(f"formula-trigger cells in {name}: {triggers}")

    target_zip_path = zip_dir / TARGET_ZIP
    metadata_zip_path = zip_dir / METADATA_ZIP
    target_zip_result = build_zip(
        target_zip_path,
        target_rows,
        scratch_dir,
        [
            readme_path,
            parent_path,
            target_manifest,
            excluded_manifest,
            audit_context,
        ],
    )
    metadata_zip_result = build_zip(
        metadata_zip_path,
        [],
        scratch_dir,
        metadata_paths,
    )
    errors.extend(str(error) for error in target_zip_result["errors"])
    errors.extend(str(error) for error in metadata_zip_result["errors"])

    race_errors: list[str] = []
    for name, initial in initial_identities.items():
        path = scratch_dir / name
        if not path.is_file():
            race_errors.append(f"source image disappeared: {name}")
            continue
        stat = path.stat()
        current = (stat.st_size, stat.st_mtime_ns, sha256(path))
        if current != initial:
            race_errors.append(f"source image changed: {name}")
    final_headings = "\n".join(audit_headings(cert_log.read_bytes())).encode(
        "utf-8"
    )
    if sha256_bytes(final_headings) != SELECTED_AUDIT_SHA256:
        race_errors.append("selected audit boundary changed during packaging")
    errors.extend(race_errors)

    validation = {
        "schema": "sga6_targeted_ultradetail_idx627_631_validation_v1",
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "selection": {
            "tight_candidates": len(tight),
            "targeted_public_images_opened_during_audit": len(target_rows),
            "targeted_public_image_bytes": sum(
                int(row["bytes"]) for row in target_rows
            ),
            "explicit_open_events": sum(
                int(row["session_read_count"]) for row in target_rows
            ),
            "generated_unread_tight_crops_metadata_only": len(excluded_rows),
            "rights_blocked_page_bands": len(blocked_rows),
            "rights_blocked_page_band_bytes": sum(
                int(row["bytes"]) for row in blocked_rows
            ),
            "distinct_target_parent_indices": len(counts),
        },
        "authority": {
            "parent_pdf_bytes": parent_pdf.stat().st_size,
            "parent_pdf_sha256": sha256(parent_pdf),
            "parent_pdf_pages": document.page_count,
            "selected_audit_heading_rows": len(audit_rows),
            "selected_audit_heading_bytes": len(selected_audit_bytes),
            "selected_audit_heading_aggregate_sha256": selected_audit_sha,
        },
        "provenance_extract": {
            "tight_mapping_errors": provenance[
                "tight_provenance_mapping_errors"
            ],
            "routine_mapping_warnings": provenance[
                "routine_provenance_mapping_warnings"
            ],
            "generation_source_count": provenance["generation_source_count"],
            "retained_generator_script_count": provenance[
                "retained_generator_script_count"
            ],
            "malformed_candidate_lines": provenance["session_scan"][
                "malformed_candidate_lines"
            ],
        },
        "target_replay": {
            "files": len(replay),
            "dimensions_exact": sum(
                bool(item["dimensions_exact"]) for item in replay.values()
            ),
            "pixel_exact": sum(
                bool(item["pixel_exact"]) for item in replay.values()
            ),
            "png_byte_exact": sum(
                bool(item["png_byte_exact"]) for item in replay.values()
            ),
            "details": replay,
        },
        "viewer_attachment_validation": {
            "selected_read_events": sum(
                int(row["read_count"]) for row in opened
            ),
            "attachment_events": len(attachment_events),
            "attachment_correlations_pass": sum(
                bool(event["source_attachment_correlation_pass"])
                for event in attachment_events
            ),
            "all_source_mtimes_precede_selected_read_events": not any(
                "read event predates selected source file" in error
                for error in errors
            ),
        },
        "routine_band_validation": {
            "source_identity_exact": len(blocked_rows),
            "png_decode_and_dimensions_exact": len(blocked_rows),
            "pixel_replay": (
                "not_performed_for_metadata_only_rights_blocked_derivatives"
            ),
        },
        "prior_public_hash_check": {
            "prior_sha256_values_loaded": len(public_hashes),
            "target_hash_intersection": prior_intersection,
        },
        "privacy": {"generated_metadata_hits": metadata_privacy},
        "csv_formula_safety": formula_errors,
        "source_freeze": {
            "input_images": len(initial_identities),
            "race_errors": race_errors,
        },
        "zip_validation": {
            TARGET_ZIP: target_zip_result,
            METADATA_ZIP: metadata_zip_result,
        },
    }
    validation_path = output_dir / VALIDATION_NAME
    write_text(
        validation_path,
        json.dumps(validation, indent=2, ensure_ascii=True) + "\n",
    )

    upload_rows = [
        {
            "filename": target_zip_path.name,
            "bytes": target_zip_path.stat().st_size,
            "sha256": sha256(target_zip_path),
            "role": "targeted_ultradetail_image_archive",
            "status": "proposed_public",
        },
        {
            "filename": metadata_zip_path.name,
            "bytes": metadata_zip_path.stat().st_size,
            "sha256": sha256(metadata_zip_path),
            "role": "provenance_and_rights_blocked_metadata_archive",
            "status": "proposed_public",
        },
    ]
    upload_manifest = output_dir / UPLOAD_MANIFEST_NAME
    write_csv(
        upload_manifest,
        upload_rows,
        ["filename", "bytes", "sha256", "role", "status"],
    )

    checksum_paths = metadata_paths + [validation_path, upload_manifest]
    checksum_path = output_dir / SHA_NAME
    write_text(
        checksum_path,
        "\n".join(
            f"{sha256(path)}  {path.name}" for path in checksum_paths
        )
        + "\n",
    )

    summary = {
        "status": validation["status"],
        "errors": errors,
        "targeted_images": len(target_rows),
        "generated_unread_tight_crops": len(excluded_rows),
        "rights_blocked_bands": len(blocked_rows),
        "target_zip": {
            "path": target_zip_path.name,
            "bytes": target_zip_path.stat().st_size,
            "sha256": sha256(target_zip_path),
            **target_zip_result,
        },
        "metadata_zip": {
            "path": metadata_zip_path.name,
            "bytes": metadata_zip_path.stat().st_size,
            "sha256": sha256(metadata_zip_path),
            **metadata_zip_result,
        },
        "validation": {
            "path": validation_path.name,
            "bytes": validation_path.stat().st_size,
            "sha256": sha256(validation_path),
        },
        "upload_manifest": {
            "path": upload_manifest.name,
            "bytes": upload_manifest.stat().st_size,
            "sha256": sha256(upload_manifest),
        },
    }
    print(json.dumps(summary, indent=2))
    document.close()
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
