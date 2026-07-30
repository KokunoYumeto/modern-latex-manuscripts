#!/usr/bin/env python3
"""Build deterministic SGA7 visual-evidence ZIPs without copying source PNGs."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import zipfile
from pathlib import Path


FIXED_TIME = (2026, 7, 30, 0, 0, 0)
IMAGE_ZIP_NAME = "10x_SGA7I_SourceAudit_Opened_Targeted_Crops_20260730.zip"
METADATA_ZIP_NAME = (
    "10y_SGA7I_SourceAudit_Visual_Provenance_"
    "RightsBlocked_Metadata_20260730.zip"
)
PRIVATE_MARKERS = (
    b"c:\\users\\",
    b"c:/users/",
    b"appdata",
    b"papors",
    b"chatnotes",
    b".claude",
    b".codex",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--metadata-dir", type=Path, required=True)
    parser.add_argument(
        "--root",
        action="append",
        required=True,
        help="ROOT_ID=absolute scratchpad path",
    )
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args()


def key_values(values: list[str]) -> dict[str, Path]:
    result: dict[str, Path] = {}
    for value in values:
        key, separator, raw_path = value.partition("=")
        if not separator or not key or not raw_path:
            raise ValueError(f"Expected ROOT_ID=PATH, got {value!r}")
        if key in result:
            raise ValueError(f"Duplicate root: {key}")
        path = Path(raw_path).resolve()
        if not path.is_dir():
            raise FileNotFoundError(path)
        result[key] = path
    return result


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def zip_info(name: str, compress_type: int) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, FIXED_TIME)
    info.compress_type = compress_type
    info.create_system = 3
    info.external_attr = 0o100644 << 16
    return info


def csv_bytes(rows: list[dict[str, object]], fields: list[str]) -> bytes:
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue().encode("utf-8")


def member_manifest_bytes(members: list[dict[str, object]]) -> bytes:
    return csv_bytes(
        members,
        ["archive_member_path", "bytes", "sha256", "role"],
    )


def write_member(
    archive: zipfile.ZipFile,
    name: str,
    data: bytes,
    role: str,
    members: list[dict[str, object]],
    compress_type: int,
) -> None:
    archive.writestr(zip_info(name, compress_type), data)
    members.append(
        {
            "archive_member_path": name,
            "bytes": len(data),
            "sha256": sha256_bytes(data),
            "role": role,
        }
    )


def verify_zip(path: Path) -> dict[str, object]:
    with zipfile.ZipFile(path) as archive:
        bad_crc = archive.testzip()
        names = archive.namelist()
        if len(names) != len(set(names)):
            raise ValueError(f"Duplicate ZIP member: {path.name}")
        unsafe = [
            name
            for name in names
            if name.startswith(("/", "\\"))
            or re.match(r"^[A-Za-z]:", name)
            or ".." in Path(name).parts
        ]
        if unsafe:
            raise ValueError(f"Unsafe ZIP members in {path.name}: {unsafe}")
        manifest = list(
            csv.DictReader(
                io.TextIOWrapper(
                    archive.open("ARCHIVE_MEMBER_SHA256.csv"),
                    encoding="utf-8",
                )
            )
        )
        errors: list[str] = []
        for row in manifest:
            data = archive.read(row["archive_member_path"])
            if len(data) != int(row["bytes"]):
                errors.append(f"bytes:{row['archive_member_path']}")
            if sha256_bytes(data) != row["sha256"]:
                errors.append(f"sha256:{row['archive_member_path']}")
        if bad_crc or errors:
            raise ValueError(
                f"ZIP verification failed for {path.name}: crc={bad_crc}, {errors}"
            )
        return {
            "filename": path.name,
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
            "members": len(names),
            "manifested_members": len(manifest),
            "uncompressed_bytes": sum(item.file_size for item in archive.infolist()),
            "bad_crc": bad_crc,
            "unsafe_members": unsafe,
            "manifest_errors": errors,
        }


def main() -> None:
    args = parse_args()
    metadata = args.metadata_dir.resolve()
    if not metadata.is_dir():
        raise FileNotFoundError(metadata)
    roots = key_values(args.root)
    output = args.output_dir.resolve()
    output.mkdir(parents=True, exist_ok=True)

    validation_path = metadata / "SGA7I_VISUAL_EVIDENCE_VALIDATION.json"
    validation = json.loads(validation_path.read_text(encoding="utf-8"))
    if validation.get("status") != "PASS_METADATA_CUSTODY_READY":
        raise ValueError("Metadata inventory is not PASS")

    crop_manifest_path = metadata / "SGA7I_PUBLIC_TARGETED_CROP_MANIFEST.csv"
    with crop_manifest_path.open("r", encoding="utf-8", newline="") as handle:
        crop_rows = list(csv.DictReader(handle))
    if len(crop_rows) != 12:
        raise ValueError(f"Expected 12 public crops, got {len(crop_rows)}")

    image_zip = output / IMAGE_ZIP_NAME
    image_members: list[dict[str, object]] = []
    with zipfile.ZipFile(image_zip, "w", allowZip64=True) as archive:
        for row in sorted(crop_rows, key=lambda item: item["archive_member_path"]):
            root = roots.get(row["root_id"])
            if root is None:
                raise ValueError(f"Unknown root: {row['root_id']}")
            source = root / Path(row["relative_path"])
            if not source.is_file():
                raise FileNotFoundError(source)
            if source.stat().st_size != int(row["bytes"]):
                raise ValueError(f"Source byte mismatch: {row['visual_id']}")
            if sha256(source) != row["sha256"]:
                raise ValueError(f"Source hash mismatch: {row['visual_id']}")
            write_member(
                archive,
                row["archive_member_path"],
                source.read_bytes(),
                "opened_targeted_source_audit_crop",
                image_members,
                zipfile.ZIP_STORED,
            )
        for name in (
            "README.md",
            "RIGHTS_AND_PROVENANCE.md",
            "PUBLICATION_READINESS.md",
            "SGA7I_PUBLIC_TARGETED_CROP_MANIFEST.csv",
        ):
            path = metadata / name
            write_member(
                archive,
                name,
                path.read_bytes(),
                "scope_rights_or_provenance_control",
                image_members,
                zipfile.ZIP_DEFLATED,
            )
        archive.writestr(
            zip_info("ARCHIVE_MEMBER_SHA256.csv", zipfile.ZIP_DEFLATED),
            member_manifest_bytes(image_members),
        )

    metadata_names = (
        "README.md",
        "RIGHTS_AND_PROVENANCE.md",
        "PUBLICATION_READINESS.md",
        "SGA7I_TARGETED_CROP_PROVENANCE_OVERRIDES.csv",
        "SGA7I_GENERATOR_SCRIPT_IDENTITY.csv",
        "SGA7I_IMAGE_READ_EVENTS.csv",
        "SGA7I_PUBLIC_TARGETED_CROP_MANIFEST.csv",
        "SGA7I_VISUAL_EVIDENCE_DUPLICATE_ALIASES.csv",
        "SGA7I_VISUAL_EVIDENCE_INDEX.csv",
        "SGA7I_VISUAL_EVIDENCE_VALIDATION.json",
    )
    metadata_zip = output / METADATA_ZIP_NAME
    metadata_members: list[dict[str, object]] = []
    with zipfile.ZipFile(metadata_zip, "w", allowZip64=True) as archive:
        for name in metadata_names:
            path = metadata / name
            write_member(
                archive,
                name,
                path.read_bytes(),
                "visual_provenance_or_rights_blocked_metadata",
                metadata_members,
                zipfile.ZIP_DEFLATED,
            )
        archive.writestr(
            zip_info("ARCHIVE_MEMBER_SHA256.csv", zipfile.ZIP_DEFLATED),
            member_manifest_bytes(metadata_members),
        )

    results = [verify_zip(image_zip), verify_zip(metadata_zip)]
    for path in (image_zip, metadata_zip):
        with zipfile.ZipFile(path) as archive:
            for name in archive.namelist():
                if name.lower().endswith((".md", ".csv", ".json")):
                    lowered = archive.read(name).lower()
                    for marker in PRIVATE_MARKERS:
                        if marker in lowered:
                            raise ValueError(f"Private marker in {path.name}:{name}")

    upload_rows = [
        {
            "filename": item["filename"],
            "bytes": item["bytes"],
            "sha256": item["sha256"],
            "members": item["members"],
            "uncompressed_bytes": item["uncompressed_bytes"],
            "role": (
                "opened_targeted_source_audit_crops"
                if item["filename"] == IMAGE_ZIP_NAME
                else "visual_provenance_and_rights_blocked_metadata"
            ),
            "status": "proposed_public_existing_sga_concept_only",
        }
        for item in results
    ]
    upload_manifest = metadata / "SGA7I_ZENODO_UPLOAD_MANIFEST.csv"
    upload_manifest.write_bytes(
        csv_bytes(
            upload_rows,
            [
                "filename",
                "bytes",
                "sha256",
                "members",
                "uncompressed_bytes",
                "role",
                "status",
            ],
        )
    )
    build_validation = {
        "status": "PASS_READY_FOR_EXISTING_CONCEPT_UPLOAD",
        "errors": [],
        "archives": results,
        "upload_manifest": {
            "bytes": upload_manifest.stat().st_size,
            "sha256": sha256(upload_manifest),
            "rows": len(upload_rows),
        },
        "source_pixels_copied_outside_zip": 0,
    }
    build_validation_path = metadata / "SGA7I_ARCHIVE_BUILD_VALIDATION.json"
    build_validation_path.write_text(
        json.dumps(build_validation, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )

    checksum_rows = []
    for path in sorted(metadata.iterdir(), key=lambda item: item.name.casefold()):
        if not path.is_file() or path.name == "SHA256SUMS.csv":
            continue
        checksum_rows.append(
            {
                "relative_path": path.name,
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
        )
    (metadata / "SHA256SUMS.csv").write_bytes(
        csv_bytes(checksum_rows, ["relative_path", "bytes", "sha256"])
    )
    print(json.dumps(build_validation, indent=2, ensure_ascii=True))


if __name__ == "__main__":
    main()
