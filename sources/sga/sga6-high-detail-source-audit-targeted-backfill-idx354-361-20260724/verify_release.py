#!/usr/bin/env python3
"""Independently replay the SGA6 idx354-361 targeted-crop backfill."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path

import fitz
from PIL import Image, ImageChops, ImageEnhance, ImageOps


TARGET_ZIP = (
    "10t_SGA6_SourceAudit_Targeted_HighDetail_Crops_Backfill_"
    "idx354_361_20260724.zip"
)
METADATA_ZIP = (
    "10u_SGA6_SourceAudit_Crop_Provenance_RightsBlocked_Metadata_Backfill_"
    "idx354_361_20260724.zip"
)
PREFIX = "SGA6_Targeted_HighDetail_Crops_Backfill_idx354_361"
TARGET_MANIFEST = f"{PREFIX}_Manifest_20260724.csv"
BLOCKED_MANIFEST = (
    "SGA6_PageBands_idx354_361_RightsBlocked_Manifest_20260724.csv"
)
AUDIT_CONTEXT = f"{PREFIX}_Audit_Context_20260724.csv"
README = f"{PREFIX}_README_20260724.md"
PARENT = f"{PREFIX}_PARENT_SOURCE_20260724.json"
VALIDATION = f"{PREFIX}_VALIDATION_20260724.json"
UPLOAD = f"{PREFIX}_ZENODO_UPLOAD_MANIFEST_20260724.csv"
PARENT_SHA256 = "73FBBAD41340C12ECCDCFCF6C3A1656953FE3D712AA8E391678458CCD17B4BAA"
PGCROP_SHA256 = "553A9DEADEBA92AB2FE2E28C56BE76C9373B21F5F8887C3865FD0E03B058271C"
FORMULA_PREFIXES = ("=", "+", "-", "@")
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
EXPECTED_TARGETS = {
    "c354_552.png",
    "c356_561tag.png",
    "c356_binom.png",
    "c356_gk.png",
    "c357_grp2.png",
    "c358_612.png",
    "c358_612b.png",
    "c358_disp1.png",
    "c358_disp2.png",
    "c358_fonct.png",
    "c358_obc.png",
    "c358_obc2.png",
    "c359_disp1.png",
    "c359_disp2.png",
    "c359_disp2b.png",
    "c359_gp_top.png",
    "c359_surcg.png",
    "c359_surcg2.png",
    "c360_621.png",
    "c360_621end.png",
    "c360_obcg.png",
    "c361_adots.png",
    "c361_chXa.png",
    "c361_etadot.png",
    "c361_tensor.png",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--package-dir", type=Path, required=True)
    parser.add_argument("--zip-dir", type=Path, required=True)
    parser.add_argument("--scratch-dir", type=Path, required=True)
    parser.add_argument("--script-dir", type=Path, required=True)
    parser.add_argument("--parent-pdf", type=Path, required=True)
    parser.add_argument("--cert-log", type=Path, required=True)
    parser.add_argument(
        "--prior-package-dir",
        type=Path,
        action="append",
        required=True,
    )
    parser.add_argument("--report", type=Path, required=True)
    return parser.parse_args()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def formula_triggers(
    fields: list[str],
    rows: list[dict[str, str]],
) -> list[str]:
    result: list[str] = []
    for row_number, row in enumerate(rows, start=2):
        for field in fields:
            value = row.get(field, "")
            if value.startswith(FORMULA_PREFIXES):
                result.append(f"{row_number}:{field}:{value[:32]}")
    return result


def pixel_equal(left: Image.Image, right: Image.Image) -> bool:
    if left.mode != right.mode or left.size != right.size:
        return False
    return ImageChops.difference(left, right).getbbox() is None


def render_parent_page(page: fitz.Page) -> Image.Image:
    pixmap = page.get_pixmap(
        matrix=fitz.Matrix(500 / 72.0, 500 / 72.0),
        colorspace=fitz.csGRAY,
    )
    image = Image.frombytes(
        "L", [pixmap.width, pixmap.height], pixmap.samples
    )
    image = ImageOps.autocontrast(image, cutoff=1)
    image = ImageEnhance.Contrast(image).enhance(2.0)
    image = ImageEnhance.Sharpness(image).enhance(1.7)
    return image


def band_bounds(full_height: int, band_number: int) -> tuple[int, int]:
    overlap = int(full_height / 5 * 0.10)
    return (
        max(0, int(full_height * (band_number - 1) / 5) - overlap),
        min(full_height, int(full_height * band_number / 5) + overlap),
    )


def zip_replay(
    path: Path,
    expected: dict[str, tuple[int, str]],
) -> dict[str, object]:
    errors: list[str] = []
    members: list[dict[str, object]] = []
    with zipfile.ZipFile(path) as archive:
        bad = archive.testzip()
        if bad:
            errors.append(f"CRC failure: {bad}")
        infos = archive.infolist()
        names = [info.filename for info in infos]
        if len(names) != len(set(names)):
            errors.append("duplicate member")
        if set(names) != set(expected):
            errors.append(
                f"set mismatch: missing={sorted(set(expected)-set(names))}; "
                f"extra={sorted(set(names)-set(expected))}"
            )
        for info in infos:
            if info.filename.startswith("/") or ".." in Path(info.filename).parts:
                errors.append(f"unsafe member: {info.filename}")
            data = archive.read(info.filename)
            identity = (len(data), sha256_bytes(data))
            if info.filename in expected and identity != expected[info.filename]:
                errors.append(f"identity mismatch: {info.filename}")
            members.append(
                {
                    "path": info.filename,
                    "bytes": identity[0],
                    "sha256": identity[1],
                }
            )
    return {
        "filename": path.name,
        "bytes": path.stat().st_size,
        "sha256": sha256(path),
        "members": members,
        "errors": errors,
    }


def prior_target_hashes(paths: list[Path]) -> set[str]:
    result: set[str] = set()
    for root in paths:
        for path in root.glob("*Targeted*Manifest*.csv"):
            _fields, rows = read_csv(path)
            result.update(
                row["sha256"].upper()
                for row in rows
                if row.get("sha256")
            )
    return result


def main() -> int:
    args = parse_args()
    package_dir = args.package_dir.resolve()
    zip_dir = args.zip_dir.resolve()
    scratch_dir = args.scratch_dir.resolve()
    script_dir = args.script_dir.resolve()
    parent_pdf = args.parent_pdf.resolve()
    cert_log = args.cert_log.resolve()
    prior_dirs = [path.resolve() for path in args.prior_package_dir]
    report_path = args.report.resolve()
    errors: list[str] = []
    Image.MAX_IMAGE_PIXELS = None

    validation_path = package_dir / VALIDATION
    validation = json.loads(validation_path.read_text(encoding="utf-8"))
    if validation.get("status") != "PASS" or validation.get("errors") != []:
        errors.append("producer validation is not PASS/errors[]")

    target_fields, targets = read_csv(package_dir / TARGET_MANIFEST)
    blocked_fields, blocked = read_csv(package_dir / BLOCKED_MANIFEST)
    audit_fields, audits = read_csv(package_dir / AUDIT_CONTEXT)
    upload_fields, uploads = read_csv(package_dir / UPLOAD)
    if len(targets) != 25:
        errors.append(f"target count is {len(targets)}, expected 25")
    if len(blocked) != 80:
        errors.append(f"blocked count is {len(blocked)}, expected 80")
    if len(audits) != 16:
        errors.append(f"audit row count is {len(audits)}, expected 16")
    if len(uploads) != 2:
        errors.append(f"upload count is {len(uploads)}, expected 2")
    if {row["source_basename"] for row in targets} != EXPECTED_TARGETS:
        errors.append("target basename set mismatch")
    if {
        int(row["parent_pdf_index_0based"]) for row in targets + blocked
    } != set(range(354, 362)):
        errors.append("parent index set mismatch")
    if any(row["archive_path"] == "" for row in targets):
        errors.append("target manifest has blank archive path")
    if any(
        row["public_disposition"]
        != "public_targeted_source_audit_evidence_no_license_grant"
        for row in targets
    ):
        errors.append("target public disposition mismatch")
    if any(
        row["public_disposition"] != "rights_blocked_not_public"
        for row in blocked
    ):
        errors.append("blocked public disposition mismatch")

    source_errors: list[str] = []
    for row in targets + blocked:
        source = scratch_dir / row["source_basename"]
        if not source.is_file():
            source_errors.append(f"missing source: {row['source_basename']}")
            continue
        if (
            source.stat().st_size != int(row["bytes"])
            or sha256(source) != row["sha256"]
        ):
            source_errors.append(
                f"source identity mismatch: {row['source_basename']}"
            )
    errors.extend(source_errors)

    if sha256(parent_pdf) != PARENT_SHA256:
        errors.append("parent hash mismatch")
    pgcrop = script_dir / "pgcrop.py"
    if not pgcrop.is_file() or sha256(pgcrop) != PGCROP_SHA256:
        errors.append("pgcrop identity mismatch")

    replay_errors: list[str] = []
    target_by_band: dict[str, list[dict[str, str]]] = {}
    for row in targets:
        target_by_band.setdefault(row["source_band_basename"], []).append(row)
    replayed_bands = 0
    replayed_targets = 0
    with fitz.open(parent_pdf) as document:
        if document.page_count != 720:
            errors.append(f"parent has {document.page_count} pages, expected 720")
        for index in range(354, 362):
            full = render_parent_page(document[index])
            for band_number in range(1, 6):
                name = f"p{index}_b{band_number}.png"
                source = scratch_dir / name
                y0, y1 = band_bounds(full.height, band_number)
                expected = full.crop((0, y0, full.width, y1))
                with Image.open(source) as actual_source:
                    actual = actual_source.convert("L")
                    if not pixel_equal(expected, actual):
                        replay_errors.append(
                            f"parent-to-band pixel mismatch: {name}"
                        )
                replayed_bands += 1
                for row in target_by_band.get(name, []):
                    bbox = tuple(
                        int(value)
                        for value in row["bbox_in_source_band_px"].split(",")
                    )
                    scale = int(row["target_upsample_factor"])
                    with Image.open(source) as source_band:
                        generated = ImageOps.autocontrast(
                            source_band.convert("L").crop(bbox)
                        )
                        generated = generated.resize(
                            (
                                generated.width * scale,
                                generated.height * scale,
                            ),
                            Image.Resampling.LANCZOS,
                        )
                    with Image.open(
                        scratch_dir / row["source_basename"]
                    ) as target:
                        if not pixel_equal(generated, target.convert("L")):
                            replay_errors.append(
                                "band-to-target pixel mismatch: "
                                f"{row['source_basename']}"
                            )
                    replayed_targets += 1
    if replayed_bands != 40:
        replay_errors.append(f"replayed {replayed_bands} historical bands, expected 40")
    if replayed_targets != 25:
        replay_errors.append(f"replayed {replayed_targets} targets, expected 25")
    errors.extend(replay_errors)

    prior_hashes = prior_target_hashes(prior_dirs)
    target_hashes = {row["sha256"] for row in targets}
    duplicate_prior = sorted(target_hashes & prior_hashes)
    if duplicate_prior:
        errors.append(f"target hashes already in prior package: {duplicate_prior}")

    audit_by_id = {row["audit_entry_number"]: row for row in audits}
    cert_text = cert_log.read_text(encoding="utf-8", errors="replace")
    audit_errors: list[str] = []
    for row in targets + blocked:
        index = row["parent_pdf_index_0based"]
        for field in ("original_audit_entry", "cold_reverify_audit_entry"):
            entry = row[field]
            audit = audit_by_id.get(entry)
            if audit is None or audit["parent_pdf_index_0based"] != index:
                audit_errors.append(
                    f"{row['source_basename']} has invalid {field}={entry}"
                )
                continue
            pattern = re.compile(
                rf"^###\s+#{re.escape(entry)}\b.*\bidx{re.escape(index)}\b",
                re.MULTILINE,
            )
            if not pattern.search(cert_text):
                audit_errors.append(
                    f"live certification log lacks {entry}@idx{index}"
                )
    errors.extend(sorted(set(audit_errors)))

    metadata_names = [README, PARENT, TARGET_MANIFEST, AUDIT_CONTEXT]
    target_expected = {
        **{
            f"metadata/{name}": (
                (package_dir / name).stat().st_size,
                sha256(package_dir / name),
            )
            for name in metadata_names
        },
        **{
            row["archive_path"]: (int(row["bytes"]), row["sha256"])
            for row in targets
        },
    }
    metadata_names_full = [
        README,
        PARENT,
        TARGET_MANIFEST,
        BLOCKED_MANIFEST,
        AUDIT_CONTEXT,
    ]
    metadata_expected = {
        f"metadata/{name}": (
            (package_dir / name).stat().st_size,
            sha256(package_dir / name),
        )
        for name in metadata_names_full
    }
    upload_by_name = {row["filename"]: row for row in uploads}
    zip_results: dict[str, dict[str, object]] = {}
    for name, expected in (
        (TARGET_ZIP, target_expected),
        (METADATA_ZIP, metadata_expected),
    ):
        path = zip_dir / name
        row = upload_by_name.get(name)
        if row is None:
            errors.append(f"upload manifest lacks {name}")
            continue
        if (
            not path.is_file()
            or path.stat().st_size != int(row["bytes"])
            or sha256(path) != row["sha256"]
        ):
            errors.append(f"outer archive mismatch: {name}")
            continue
        result = zip_replay(path, expected)
        zip_results[name] = result
        errors.extend(f"{name}: {item}" for item in result["errors"])

    public_members = {
        member["path"]
        for result in zip_results.values()
        for member in result["members"]  # type: ignore[index]
    }
    leaked_bands = [
        row["source_basename"]
        for row in blocked
        if any(
            member.endswith("/" + row["source_basename"])
            or member == row["source_basename"]
            for member in public_members
        )
    ]
    if leaked_bands:
        errors.append(f"rights-blocked band pixels leaked: {leaked_bands}")

    csv_results: dict[str, object] = {}
    for path in sorted(package_dir.glob("*.csv")):
        fields, rows = read_csv(path)
        triggers = formula_triggers(fields, rows)
        if triggers:
            errors.append(f"formula-trigger cells in {path.name}: {triggers}")
        csv_results[path.name] = {
            "rows": len(rows),
            "columns": len(fields),
            "formula_triggers": triggers,
        }

    privacy: dict[str, list[str]] = {}
    public_text = [
        path
        for path in package_dir.iterdir()
        if path.is_file()
        and path.suffix.lower() in {".md", ".csv", ".json", ".txt"}
    ]
    for path in public_text:
        text = path.read_text(encoding="utf-8-sig", errors="replace").lower()
        hits = [marker for marker in PRIVATE_MARKERS if marker in text]
        if hits:
            privacy[path.name] = hits
    if privacy:
        errors.append(f"public metadata privacy hits: {privacy}")

    report = {
        "schema": "sga6_targeted_crop_backfill_idx354_361_independent_replay_v1",
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "selection": {
            "targeted_public_images": len(targets),
            "rights_blocked_page_bands": len(blocked),
            "parent_indices": sorted(
                {int(row["parent_pdf_index_0based"]) for row in targets}
            ),
        },
        "source_identity_replay": {
            "files": len(targets) + len(blocked),
            "errors": source_errors,
        },
        "pixel_replay": {
            "historical_parent_to_band_files": replayed_bands,
            "historical_band_to_target_files": replayed_targets,
            "errors": replay_errors,
        },
        "deduplication": {
            "prior_target_hashes": len(prior_hashes),
            "intersection": duplicate_prior,
        },
        "audit_reference_closure": {
            "rows": len(audits),
            "errors": sorted(set(audit_errors)),
        },
        "outer_archives": zip_results,
        "csv_validation": csv_results,
        "privacy": {
            "files_scanned": len(public_text),
            "hits": privacy,
        },
        "cert_log": {
            "live_bytes": cert_log.stat().st_size,
            "live_sha256": sha256(cert_log),
            "packaged_bytes": validation["parent_source"][
                "cert_log_bytes_at_packaging_snapshot"
            ],
            "packaged_sha256": validation["parent_source"][
                "cert_log_sha256_at_packaging_snapshot"
            ],
        },
    }
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(
        json.dumps(report, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps(report, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
