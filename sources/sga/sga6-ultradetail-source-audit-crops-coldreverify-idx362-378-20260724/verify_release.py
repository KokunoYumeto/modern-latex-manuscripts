#!/usr/bin/env python3
"""Independent replay validator for the SGA6 idx362-378 crop release."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import zipfile
from datetime import datetime, timezone
from pathlib import Path

import fitz
from PIL import Image, ImageChops, ImageEnhance, ImageOps


PARENT_SHA256 = "73FBBAD41340C12ECCDCFCF6C3A1656953FE3D712AA8E391678458CCD17B4BAA"
SELECTED_RAW_AUDIT_SHA256 = (
    "F36AE17F28CE851B61F58C9FDE856D406F341AE079859BD3CED74E003DCE8364"
)
START_ENTRY = 1114
END_ENTRY = 1130
PRIVATE_MARKERS = (
    "c:\\users\\",
    "c:/users/",
    "floris",
    "chatnotes",
    "source_thread_id",
    "thread_id",
    "@gmail.",
    "@outlook.",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scratch-dir", type=Path, required=True)
    parser.add_argument("--script-dir", type=Path, required=True)
    parser.add_argument("--parent-pdf", type=Path, required=True)
    parser.add_argument("--cert-log", type=Path, required=True)
    parser.add_argument("--prior-package-root", type=Path, required=True)
    parser.add_argument("--package-dir", type=Path, required=True)
    parser.add_argument("--zip-dir", type=Path, required=True)
    parser.add_argument("--report-path", type=Path, required=True)
    parser.add_argument("--validation-path", type=Path, required=True)
    return parser.parse_args()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest().upper()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def render(
    document: fitz.Document,
    row: dict[str, str],
) -> tuple[Image.Image, bytes]:
    index = int(row["parent_pdf_index_0based"])
    page = document[index]
    rect = page.rect
    fx0 = float(row["bbox_fx0"])
    fy0 = float(row["bbox_fy0"])
    fx1 = float(row["bbox_fx1"])
    fy1 = float(row["bbox_fy1"])
    clip = fitz.Rect(
        rect.x0 + rect.width * fx0,
        rect.y0 + rect.height * fy0,
        rect.x0 + rect.width * fx1,
        rect.y0 + rect.height * fy1,
    )
    dpi = int(row["render_dpi"])
    pixmap = page.get_pixmap(
        matrix=fitz.Matrix(dpi / 72.0, dpi / 72.0),
        clip=clip,
        colorspace=fitz.csGRAY,
    )
    image = Image.frombytes(
        "L",
        [pixmap.width, pixmap.height],
        pixmap.samples,
    )
    profile = row["processing_profile"]
    image = ImageOps.autocontrast(image, cutoff=1)
    contrast_match = re.search(r"contrast_([0-9.]+)", profile)
    sharpness_match = re.search(r"sharpness_([0-9.]+)", profile)
    if not contrast_match or not sharpness_match:
        raise RuntimeError(f"invalid processing profile: {profile}")
    image = ImageEnhance.Contrast(image).enhance(
        float(contrast_match.group(1))
    )
    image = ImageEnhance.Sharpness(image).enhance(
        float(sharpness_match.group(1))
    )
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    return image, buffer.getvalue()


def pixels_equal(left: Image.Image, right: Image.Image) -> bool:
    return (
        left.mode == right.mode
        and left.size == right.size
        and ImageChops.difference(left, right).getbbox() is None
    )


def selected_audit_bytes(path: Path) -> bytes:
    pattern = re.compile(r"^### #(?P<entry>\d+)\b")
    selected: list[str] = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        match = pattern.match(line)
        if match and START_ENTRY <= int(match.group("entry")) <= END_ENTRY:
            selected.append(line)
    return "\n".join(selected).encode("utf-8")


def prior_hashes(root: Path, excluded_dir: Path) -> set[str]:
    values: set[str] = set()
    for path in root.rglob("*.csv"):
        try:
            path.resolve().relative_to(excluded_dir.resolve())
            continue
        except ValueError:
            pass
        try:
            for row in read_csv(path):
                for key, value in row.items():
                    if key and "sha256" in key.lower():
                        normalized = value.strip().upper()
                        if re.fullmatch(r"[0-9A-F]{64}", normalized):
                            values.add(normalized)
        except (OSError, UnicodeError, csv.Error):
            continue
    return values


def verify_zip(
    path: Path,
    image_rows: list[dict[str, str]],
    metadata_paths: list[Path],
    scratch_dir: Path,
) -> dict[str, object]:
    expected: dict[str, tuple[int, str]] = {}
    for row in image_rows:
        source = scratch_dir / row["source_basename"]
        expected[row["archive_path"]] = (source.stat().st_size, sha256(source))
    for source in metadata_paths:
        expected[f"metadata/{source.name}"] = (
            source.stat().st_size,
            sha256(source),
        )
    errors: list[str] = []
    members: list[dict[str, object]] = []
    with zipfile.ZipFile(path) as archive:
        bad = archive.testzip()
        if bad:
            errors.append(f"bad CRC member: {bad}")
        names = archive.namelist()
        if len(names) != len(set(names)):
            errors.append("duplicate member")
        if set(names) != set(expected):
            errors.append(
                "exact-set mismatch: "
                f"missing={sorted(set(expected)-set(names))}; "
                f"extra={sorted(set(names)-set(expected))}"
            )
        for info in archive.infolist():
            name = info.filename
            if (
                name.startswith("/")
                or name.startswith("\\")
                or re.match(r"^[A-Za-z]:", name)
                or ".." in Path(name).parts
            ):
                errors.append(f"unsafe member: {name}")
                continue
            data = archive.read(name)
            observed = (len(data), sha256_bytes(data))
            if name in expected and observed != expected[name]:
                errors.append(f"identity mismatch: {name}")
            members.append(
                {
                    "path": name,
                    "bytes": len(data),
                    "sha256": sha256_bytes(data),
                }
            )
    members.sort(key=lambda row: str(row["path"]).lower())
    return {
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "members": len(members),
        "member_bytes": sum(int(row["bytes"]) for row in members),
        "member_identity_aggregate_sha256": sha256_bytes(
            "".join(
                f"{row['path']}\t{row['bytes']}\t{row['sha256']}\n"
                for row in members
            ).encode("utf-8")
        ),
    }


def main() -> int:
    args = parse_args()
    scratch_dir = args.scratch_dir.resolve()
    script_dir = args.script_dir.resolve()
    parent_pdf = args.parent_pdf.resolve()
    cert_log = args.cert_log.resolve()
    prior_root = args.prior_package_root.resolve()
    package_dir = args.package_dir.resolve()
    zip_dir = args.zip_dir.resolve()
    report_path = args.report_path.resolve()
    validation_path = args.validation_path.resolve()
    Image.MAX_IMAGE_PIXELS = None

    errors: list[str] = []
    package_validation_paths = list(
        package_dir.glob(
            "SGA6_Targeted_UltraDetail_Crops_*_VALIDATION_20260724.json"
        )
    )
    if len(package_validation_paths) != 1:
        errors.append("expected one producer validation")
        package_validation: dict[str, object] = {}
    else:
        package_validation = json.loads(
            package_validation_paths[0].read_text(encoding="utf-8")
        )
        if (
            package_validation.get("status") != "PASS"
            or package_validation.get("errors") != []
        ):
            errors.append("producer validation is not a clean PASS")

    target_manifest_paths = [
        path
        for path in package_dir.glob(
            "SGA6_Targeted_UltraDetail_Crops_*_Manifest_20260724.csv"
        )
        if "ZENODO_UPLOAD" not in path.name
    ]
    blocked_manifest_paths = list(
        package_dir.glob("*PageBands*RightsBlocked*Manifest*.csv")
    )
    audit_paths = list(package_dir.glob("*Audit_Context*.csv"))
    upload_paths = list(package_dir.glob("*ZENODO_UPLOAD_MANIFEST*.csv"))
    readme_paths = list(package_dir.glob("*README*.md"))
    parent_paths = list(package_dir.glob("*PARENT_SOURCE*.json"))
    if not all(
        len(paths) == 1
        for paths in (
            target_manifest_paths,
            blocked_manifest_paths,
            audit_paths,
            upload_paths,
            readme_paths,
            parent_paths,
        )
    ):
        errors.append("package control exact-set mismatch")
        target_rows: list[dict[str, str]] = []
        blocked_rows: list[dict[str, str]] = []
        upload_rows: list[dict[str, str]] = []
    else:
        target_rows = read_csv(target_manifest_paths[0])
        blocked_rows = read_csv(blocked_manifest_paths[0])
        upload_rows = read_csv(upload_paths[0])

    if len(target_rows) != 15:
        errors.append(f"target rows are {len(target_rows)}, expected 15")
    if len(blocked_rows) != 85:
        errors.append(f"blocked rows are {len(blocked_rows)}, expected 85")
    if len(upload_rows) != 2:
        errors.append(f"upload rows are {len(upload_rows)}, expected 2")

    if sha256(parent_pdf) != PARENT_SHA256:
        errors.append("parent identity mismatch")
    document = fitz.open(parent_pdf)
    if document.page_count != 720:
        errors.append("parent page count mismatch")

    audit_bytes = selected_audit_bytes(cert_log)
    if sha256_bytes(audit_bytes) != SELECTED_RAW_AUDIT_SHA256:
        errors.append("selected audit boundary mismatch")

    replay_rows = target_rows + blocked_rows
    pixel_exact = 0
    byte_exact = 0
    source_identity_exact = 0
    generator_identity_exact = 0
    for row in replay_rows:
        source = scratch_dir / row["source_basename"]
        if not source.is_file():
            errors.append(f"missing source image: {source.name}")
            continue
        if (
            source.stat().st_size == int(row["bytes"])
            and sha256(source) == row["sha256"]
        ):
            source_identity_exact += 1
        else:
            errors.append(f"source image identity mismatch: {source.name}")
        generator = script_dir / row["generator_script_basename"]
        if (
            generator.is_file()
            and generator.stat().st_size
            == int(row["generator_script_bytes"])
            and sha256(generator) == row["generator_script_sha256"]
        ):
            generator_identity_exact += 1
        else:
            errors.append(
                f"generator identity mismatch: "
                f"{row['generator_script_basename']}"
            )
        replay_image, replay_bytes = render(document, row)
        with Image.open(source) as source_image_handle:
            source_image = source_image_handle.convert("L")
            if pixels_equal(replay_image, source_image):
                pixel_exact += 1
            else:
                errors.append(f"pixel replay mismatch: {source.name}")
        if replay_bytes == source.read_bytes():
            byte_exact += 1
        else:
            errors.append(f"PNG byte replay mismatch: {source.name}")

    prior = prior_hashes(prior_root, package_dir)
    target_hashes = {row["sha256"] for row in target_rows}
    intersection = sorted(target_hashes & prior)
    if intersection:
        errors.append(f"prior target hash intersection: {intersection}")

    metadata_paths = [
        readme_paths[0],
        parent_paths[0],
        target_manifest_paths[0],
        blocked_manifest_paths[0],
        audit_paths[0],
    ]
    privacy: dict[str, list[str]] = {}
    for path in metadata_paths:
        text = path.read_text(encoding="utf-8", errors="replace").lower()
        hits = sorted(marker for marker in PRIVATE_MARKERS if marker in text)
        if hits:
            privacy[path.name] = hits
    if privacy:
        errors.append(f"metadata privacy hits: {privacy}")

    zip_results: dict[str, dict[str, object]] = {}
    if len(upload_rows) == 2:
        for row in upload_rows:
            path = zip_dir / row["filename"]
            if (
                not path.is_file()
                or path.stat().st_size != int(row["bytes"])
                or sha256(path) != row["sha256"]
            ):
                errors.append(f"outer ZIP identity mismatch: {path.name}")
                continue
            if "Targeted_UltraDetail" in path.name:
                image_rows = target_rows
                zip_metadata = [
                    readme_paths[0],
                    parent_paths[0],
                    target_manifest_paths[0],
                    audit_paths[0],
                ]
            else:
                image_rows = []
                zip_metadata = metadata_paths
            result = verify_zip(
                path,
                image_rows,
                zip_metadata,
                scratch_dir,
            )
            zip_results[path.name] = result
            errors.extend(
                f"{path.name}: {error}" for error in result["errors"]
            )

    validation = {
        "schema": "sga6_targeted_ultradetail_idx362_378_independent_replay_v1",
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "completed_utc": datetime.now(timezone.utc).isoformat(),
        "producer_validation": {
            "status": package_validation.get("status"),
            "errors": package_validation.get("errors"),
        },
        "counts": {
            "targeted_images": len(target_rows),
            "rights_blocked_bands": len(blocked_rows),
            "source_identity_exact": source_identity_exact,
            "generator_identity_exact": generator_identity_exact,
            "pixel_exact": pixel_exact,
            "png_byte_exact": byte_exact,
        },
        "authority": {
            "parent_pdf_sha256": sha256(parent_pdf),
            "parent_pdf_pages": document.page_count,
            "selected_audit_heading_sha256": sha256_bytes(audit_bytes),
        },
        "prior_public_hash_check": {
            "prior_sha256_values_loaded": len(prior),
            "target_hash_intersection": intersection,
        },
        "privacy_hits": privacy,
        "zip_validation": zip_results,
    }
    validation_path.parent.mkdir(parents=True, exist_ok=True)
    validation_path.write_text(
        json.dumps(validation, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )

    report = f"""# Independent replay: SGA6 idx362-378 ultra-detail crops

Status: **{validation['status']}**

- Targeted public crops: {len(target_rows)}
- Rights-blocked full-width page bands: {len(blocked_rows)}
- Source identities exact: {source_identity_exact}/{len(replay_rows)}
- Generator identities exact: {generator_identity_exact}/{len(replay_rows)}
- Parent-to-crop pixel replay exact: {pixel_exact}/{len(replay_rows)}
- Parent-to-crop PNG-byte replay exact: {byte_exact}/{len(replay_rows)}
- Selected audit boundary: entries #1114-#1130, SHA-256
  `{sha256_bytes(audit_bytes)}`
- Prior public target-hash intersection: {len(intersection)}
- Metadata privacy hits: {sum(len(value) for value in privacy.values())}
- ZIPs: {len(zip_results)}; all exact-set/member/CRC/safe-path gates
  {'PASS' if zip_results and all(item['status'] == 'PASS' for item in zip_results.values()) else 'FAIL'}.

This independent pass re-rendered all 100 represented images from the pinned
720-page parent. It confirms that only the 15 targeted crops are bundled as
pixels; all 85 full-width page bands remain manifest-only and rights-blocked.
The package is source-audit provenance, not translation or mathematical
certification.
"""
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report, encoding="utf-8", newline="\n")
    document.close()
    print(
        json.dumps(
            {
                "status": validation["status"],
                "errors": errors,
                "report": {
                    "path": report_path.name,
                    "bytes": report_path.stat().st_size,
                    "sha256": sha256(report_path),
                },
                "validation": {
                    "path": validation_path.name,
                    "bytes": validation_path.stat().st_size,
                    "sha256": sha256(validation_path),
                },
            },
            indent=2,
        )
    )
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
