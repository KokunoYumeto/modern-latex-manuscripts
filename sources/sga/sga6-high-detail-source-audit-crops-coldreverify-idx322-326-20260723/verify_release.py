#!/usr/bin/env python3
"""Independently replay the SGA6 idx322-326 crop release boundary."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
import zipfile
from pathlib import Path


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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--package-dir", type=Path, required=True)
    parser.add_argument("--zip-dir", type=Path, required=True)
    parser.add_argument("--scratch-dir", type=Path, required=True)
    parser.add_argument("--cert-log", type=Path, required=True)
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


def formula_cells(fields: list[str], rows: list[dict[str, str]]) -> list[str]:
    errors: list[str] = []
    for row_number, row in enumerate(rows, start=2):
        for field in fields:
            value = row.get(field, "")
            if value.startswith(FORMULA_PREFIXES):
                errors.append(f"{row_number}:{field}:{value[:32]}")
    return errors


def zip_replay(
    path: Path,
    expected: dict[str, tuple[int, str]],
) -> dict[str, object]:
    errors: list[str] = []
    members: list[dict[str, object]] = []
    with zipfile.ZipFile(path) as archive:
        bad_member = archive.testzip()
        if bad_member:
            errors.append(f"CRC failure: {bad_member}")
        infos = archive.infolist()
        names = [info.filename for info in infos]
        if len(names) != len(set(names)):
            errors.append("duplicate member name")
        if set(names) != set(expected):
            errors.append(
                "set mismatch: "
                f"missing={sorted(set(expected) - set(names))}; "
                f"extra={sorted(set(names) - set(expected))}"
            )
        for info in infos:
            if info.filename.startswith("/") or ".." in Path(info.filename).parts:
                errors.append(f"unsafe member name: {info.filename}")
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


def main() -> int:
    args = parse_args()
    package_dir = args.package_dir.resolve()
    zip_dir = args.zip_dir.resolve()
    scratch_dir = args.scratch_dir.resolve()
    cert_log = args.cert_log.resolve()
    report_path = args.report.resolve()
    errors: list[str] = []

    validation_path = (
        package_dir
        / "SGA6_HighDetail_SourceAudit_Crops_idx322_326_VALIDATION_20260723.json"
    )
    validation = json.loads(validation_path.read_text(encoding="utf-8"))
    if validation.get("status") != "PASS" or validation.get("errors") != []:
        errors.append("producer validation is not PASS/errors[]")

    explicit_path = (
        package_dir
        / "SGA6_Explicit_Targeted_HighDetail_Crops_idx322_326_Manifest_20260723.csv"
    )
    recovered_path = (
        package_dir
        / "SGA6_Recovered_Named_HighDetail_Crops_idx322_326_Manifest_20260723.csv"
    )
    blocked_path = (
        package_dir
        / "SGA6_Routine_PageBands_idx322_326_RightsBlocked_Manifest_20260723.csv"
    )
    upload_path = (
        package_dir
        / "SGA6_HighDetail_SourceAudit_Crops_idx322_326_"
        "ZENODO_UPLOAD_MANIFEST_20260723.csv"
    )
    explicit_fields, explicit_rows = read_csv(explicit_path)
    recovered_fields, recovered_rows = read_csv(recovered_path)
    blocked_fields, blocked_rows = read_csv(blocked_path)
    upload_fields, upload_rows = read_csv(upload_path)

    if len(explicit_rows) != 1:
        errors.append(f"explicit crop count is {len(explicit_rows)}, expected 1")
    if recovered_rows:
        errors.append(f"recovered crop count is {len(recovered_rows)}, expected 0")
    if len(blocked_rows) != 25:
        errors.append(f"blocked band count is {len(blocked_rows)}, expected 25")
    if len(upload_rows) != 2:
        errors.append(f"upload count is {len(upload_rows)}, expected 2")

    all_rows = explicit_rows + recovered_rows + blocked_rows
    indices = {int(row["parent_pdf_index_0based"]) for row in all_rows}
    if indices != set(range(322, 327)):
        errors.append(f"parent index set is {sorted(indices)}, expected 322-326")
    if any(row["category"] != "routine_page_derivative" for row in blocked_rows):
        errors.append("blocked manifest contains a non-routine row")
    if any(
        row["public_disposition"] != "rights_blocked_not_public"
        for row in blocked_rows
    ):
        errors.append("blocked manifest contains a public pixel disposition")

    source_errors: list[str] = []
    for row in explicit_rows + blocked_rows:
        source = scratch_dir / row["source_basename"]
        if not source.is_file():
            source_errors.append(f"missing source image: {row['source_basename']}")
            continue
        if source.stat().st_size != int(row["bytes"]) or sha256(source) != row["sha256"]:
            source_errors.append(f"source identity mismatch: {row['source_basename']}")
    errors.extend(source_errors)

    if sha256(cert_log) != validation["parent_source"]["cert_log_sha256_at_packaging_snapshot"]:
        errors.append("certification-log snapshot identity changed before replay")

    metadata_names = [
        "SGA6_HighDetail_SourceAudit_Crops_idx322_326_README_20260723.md",
        "SGA6_HighDetail_SourceAudit_Crops_idx322_326_PARENT_SOURCE_20260723.json",
        "SGA6_Explicit_Targeted_HighDetail_Crops_idx322_326_Manifest_20260723.csv",
        "SGA6_Recovered_Named_HighDetail_Crops_idx322_326_Manifest_20260723.csv",
        "SGA6_Routine_PageBands_idx322_326_RightsBlocked_Manifest_20260723.csv",
        "SGA6_HighDetail_Crops_idx322_326_Audit_Context_20260723.csv",
    ]
    common_metadata = {
        f"metadata/{name}": (
            (package_dir / name).stat().st_size,
            sha256(package_dir / name),
        )
        for name in metadata_names
    }
    explicit_expected = {
        **{
            f"metadata/{name}": common_metadata[f"metadata/{name}"]
            for name in metadata_names
            if name
            in {
                metadata_names[0],
                metadata_names[1],
                metadata_names[2],
                metadata_names[5],
            }
        },
        **{
            row["archive_path"]: (int(row["bytes"]), row["sha256"])
            for row in explicit_rows
        },
    }
    metadata_expected = common_metadata

    zip_results: dict[str, dict[str, object]] = {}
    for row in upload_rows:
        archive_path = zip_dir / row["filename"]
        if not archive_path.is_file():
            errors.append(f"missing proposed archive: {row['filename']}")
            continue
        if archive_path.stat().st_size != int(row["bytes"]) or sha256(archive_path) != row["sha256"]:
            errors.append(f"outer archive identity mismatch: {row['filename']}")
        expected = (
            explicit_expected
            if row["filename"].startswith("10m_")
            else metadata_expected
        )
        result = zip_replay(archive_path, expected)
        zip_results[row["filename"]] = result
        errors.extend(
            f"{row['filename']}: {error}" for error in result["errors"]  # type: ignore[index]
        )

    public_archive_members = {
        member["path"]
        for result in zip_results.values()
        for member in result["members"]  # type: ignore[index]
    }
    leaked_blocked = [
        row["archive_path"]
        for row in blocked_rows
        if row["archive_path"] in public_archive_members
    ]
    if leaked_blocked:
        errors.append(f"rights-blocked pixel members leaked: {leaked_blocked}")

    csv_results: dict[str, object] = {}
    for csv_path in sorted(package_dir.glob("*.csv")):
        fields, rows = read_csv(csv_path)
        triggers = formula_cells(fields, rows)
        if triggers:
            errors.append(f"formula-trigger cells in {csv_path.name}: {triggers}")
        csv_results[csv_path.name] = {
            "rows": len(rows),
            "columns": len(fields),
            "formula_triggers": triggers,
        }

    privacy_hits: dict[str, list[str]] = {}
    public_text_paths = [
        path
        for path in package_dir.iterdir()
        if path.is_file() and path.suffix.lower() in {".md", ".csv", ".json", ".txt"}
    ]
    for path in public_text_paths:
        text = path.read_text(encoding="utf-8-sig", errors="replace").lower()
        hits = [marker for marker in PRIVATE_MARKERS if marker in text]
        if hits:
            privacy_hits[path.name] = hits
    if privacy_hits:
        errors.append(f"public metadata privacy hits: {privacy_hits}")

    report = {
        "schema": "sga6_idx322_326_crop_release_independent_replay_v1",
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "outer_archives": zip_results,
        "source_replay": {
            "files": len(explicit_rows) + len(blocked_rows),
            "errors": source_errors,
        },
        "selection": {
            "explicit_targeted": len(explicit_rows),
            "recovered_named_targeted": len(recovered_rows),
            "routine_page_bands_rights_blocked": len(blocked_rows),
            "parent_indices": sorted(indices),
        },
        "csv_validation": csv_results,
        "privacy": {
            "files_scanned": len(public_text_paths),
            "hits": privacy_hits,
        },
        "cert_log_sha256": sha256(cert_log),
    }
    report_path.write_text(
        json.dumps(report, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps(report, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
