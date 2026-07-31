#!/usr/bin/env python3
"""Build the compact SGA7 II X-XIV release controls and source ZIP."""

from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import zipfile
from collections import Counter
from pathlib import Path, PurePosixPath


REPO_ROOT = Path(__file__).resolve().parents[1]
PACKAGE_ROOT = (
    REPO_ROOT
    / "sources/sga/sga7ii-french-source-transcription-working-x-xiv-20260731"
)
TEMP_ROOT = Path(os.environ.get("TEMP", r"C:\Users\Floris\AppData\Local\Temp"))

PDF_NAME = "00h_SGA7II_French_Source_Transcription_Working_X-XIV_20260731.pdf"
TEX_NAME = "02h_SGA7II_French_Source_Transcription_Working_X-XIV_20260731.tex"
SOURCE_ZIP_NAME = (
    "10g2_SGA7II_French_Source_Transcription_Working_X-XIV_"
    "Reader_Source_and_WIP_20260731.zip"
)
IMAGE_ZIP_NAME = "10h_SGA7II_SourceAudit_Number12_HighDetail_Crops_20260731.zip"

PDF_PATH = PACKAGE_ROOT / "reader/SGA7II_French_Source_Transcription_Working_X-XIV_20260731.pdf"
TEX_PATH = PACKAGE_ROOT / "source/SGA7II_French_Source_Transcription_Working_X-XIV_20260731.tex"
SOURCE_ZIP_PATH = TEMP_ROOT / SOURCE_ZIP_NAME
IMAGE_ZIP_PATH = TEMP_ROOT / IMAGE_ZIP_NAME

EXPECTED_PDF = (
    735_900,
    "67D81C7EF432A29493ADCFEFC8BA517C65A0CBE3B7731FF507BA2DD4CD30EB47",
)
EXPECTED_IMAGE_ZIP = (
    150_312_768,
    "A59B1BD449C1DF5074002D128B2F638A17509E32D6345F06561C5C7189F0D14B",
    5_036,
)

SOURCE_MEMBERS = (
    "README.md",
    "PUBLICATION_READINESS.md",
    "RIGHTS_AND_PROVENANCE.md",
    "BUILD_SUMMARY_PUBLIC.md",
    "reader/SGA7II_French_Source_Transcription_Working_X-XIV_20260731.pdf",
    "source/SGA7II_French_Source_Transcription_Working_X-XIV_20260731.tex",
    "source/expose_X_body.tex",
    "source/expose_XI_body.tex",
    "source/expose_XII_body.tex",
    "source/expose_XIII_body.tex",
    "source/expose_XIV_body.tex",
    "evidence/SOURCE_NOTES.md",
    "evidence/DOUBLE_TRANSCRIPTION_CHECK.md",
    "work-in-progress/README.md",
    "work-in-progress/expose_XV_partial.tex",
)

PRIVACY_PATTERNS = (
    re.compile(r"[A-Za-z]:\\(?:Users|IL_GitHub)\\", re.IGNORECASE),
    re.compile(r"(?:/home/|/Users/)[^\s/]+/", re.IGNORECASE),
    re.compile(r"Floris", re.IGNORECASE),
    re.compile(r"(?:Claude|ChatGPT|OpenAI|Codex)", re.IGNORECASE),
    re.compile(r"(?:thread|task)[-_ ]?id", re.IGNORECASE),
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def identity(path: Path) -> tuple[int, str]:
    return path.stat().st_size, sha256_path(path)


def safe_member(name: str) -> bool:
    pure = PurePosixPath(name)
    return (
        name == name.replace("\\", "/")
        and not pure.is_absolute()
        and ".." not in pure.parts
        and not re.match(r"^[A-Za-z]:", name)
    )


def media_type(path: str) -> str:
    suffix = Path(path).suffix.lower()
    return {
        ".csv": "text/csv",
        ".json": "application/json",
        ".md": "text/markdown",
        ".pdf": "application/pdf",
        ".tex": "application/x-tex",
        ".zip": "application/zip",
    }.get(suffix, "application/octet-stream")


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, value: object) -> None:
    path.write_text(
        json.dumps(value, ensure_ascii=True, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def source_scope_replay() -> dict[str, object]:
    expected = {
        "expose_X_body.tex": (8, 45),
        "expose_XI_body.tex": (46, 68),
        "expose_XII_body.tex": (69, 89),
        "expose_XIII_body.tex": (90, 122),
        "expose_XIV_body.tex": (123, 171),
    }
    observed: dict[str, dict[str, object]] = {}
    all_indices: list[int] = []
    for name, (start, end) in expected.items():
        text = (PACKAGE_ROOT / "source" / name).read_text(
            encoding="utf-8", errors="strict"
        )
        indices = [int(value) for value in re.findall(r"scan idx\s+(\d+)", text)]
        wanted = list(range(start, end + 1))
        if indices != wanted:
            raise RuntimeError(f"Source-page marker mismatch: {name}")
        observed[name] = {
            "first": start,
            "last": end,
            "markers": len(indices),
        }
        all_indices.extend(indices)
    if all_indices != list(range(8, 172)):
        raise RuntimeError("X-XIV source-page continuity changed")
    partial = (PACKAGE_ROOT / "work-in-progress/expose_XV_partial.tex").read_text(
        encoding="utf-8", errors="strict"
    )
    partial_indices = [
        int(value) for value in re.findall(r"scan idx\s+(\d+)", partial)
    ]
    if partial_indices != list(range(172, 204)):
        raise RuntimeError("Expose XV partial source-page boundary changed")
    return {
        "reader_scope": observed,
        "reader_source_pages": len(all_indices),
        "reader_first_index": all_indices[0],
        "reader_last_index": all_indices[-1],
        "partial_xv_first_index": partial_indices[0],
        "partial_xv_last_index": partial_indices[-1],
        "partial_xv_source_pages": len(partial_indices),
    }


def build_source_zip() -> dict[str, object]:
    manifest_path = PACKAGE_ROOT / "SOURCE_PACKAGE_MANIFEST.csv"
    rows: list[dict[str, object]] = []
    for relative in SOURCE_MEMBERS:
        path = PACKAGE_ROOT / relative
        if not path.is_file():
            raise RuntimeError(f"Missing source package member: {relative}")
        rows.append(
            {
                "relative_path": relative,
                "bytes": path.stat().st_size,
                "sha256": sha256_path(path),
                "media_type": media_type(relative),
                "release_role": (
                    "working_partial_continuation"
                    if relative.startswith("work-in-progress/")
                    else "reader_and_buildable_source"
                ),
            }
        )
    write_csv(
        manifest_path,
        rows,
        ["relative_path", "bytes", "sha256", "media_type", "release_role"],
    )
    zip_members = (*SOURCE_MEMBERS, "SOURCE_PACKAGE_MANIFEST.csv")
    SOURCE_ZIP_PATH.unlink(missing_ok=True)
    with zipfile.ZipFile(
        SOURCE_ZIP_PATH,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
        allowZip64=True,
    ) as archive:
        for relative in zip_members:
            data = (PACKAGE_ROOT / relative).read_bytes()
            info = zipfile.ZipInfo(relative, date_time=(2026, 7, 31, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            info.create_system = 3
            archive.writestr(info, data, compresslevel=9)
    with zipfile.ZipFile(SOURCE_ZIP_PATH) as archive:
        infos = [item for item in archive.infolist() if not item.is_dir()]
        names = [item.filename for item in infos]
        if (
            archive.testzip() is not None
            or names != list(zip_members)
            or len(names) != len(set(names))
            or not all(safe_member(name) for name in names)
        ):
            raise RuntimeError("Source ZIP boundary or CRC failure")
        replay = {
            item.filename: {
                "bytes": item.file_size,
                "sha256": sha256_bytes(archive.read(item.filename)),
            }
            for item in infos
        }
    return {
        "path_name": SOURCE_ZIP_PATH.name,
        "bytes": SOURCE_ZIP_PATH.stat().st_size,
        "sha256": sha256_path(SOURCE_ZIP_PATH),
        "members": len(replay),
        "uncompressed_bytes": sum(
            int(value["bytes"]) for value in replay.values()
        ),
        "member_identities": replay,
    }


def validate_image_zip() -> dict[str, object]:
    if identity(IMAGE_ZIP_PATH) != EXPECTED_IMAGE_ZIP[:2]:
        raise RuntimeError("Image ZIP outer identity changed")
    with zipfile.ZipFile(IMAGE_ZIP_PATH) as archive:
        infos = [item for item in archive.infolist() if not item.is_dir()]
        names = [item.filename for item in infos]
        if (
            archive.testzip() is not None
            or len(names) != EXPECTED_IMAGE_ZIP[2]
            or len(names) != len(set(names))
            or not all(safe_member(name) for name in names)
        ):
            raise RuntimeError("Image ZIP member boundary or CRC changed")
        image_members = [
            item for item in infos if item.filename.lower().endswith(".png")
        ]
        if len(image_members) != 5_033:
            raise RuntimeError("Image ZIP pixel-member count changed")
        uncompressed = sum(item.file_size for item in infos)
    return {
        "path_name": IMAGE_ZIP_PATH.name,
        "bytes": EXPECTED_IMAGE_ZIP[0],
        "sha256": EXPECTED_IMAGE_ZIP[1],
        "members": EXPECTED_IMAGE_ZIP[2],
        "image_members": len(image_members),
        "uncompressed_bytes": uncompressed,
    }


def privacy_replay() -> list[dict[str, str]]:
    hits: list[dict[str, str]] = []
    for path in sorted(PACKAGE_ROOT.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in {
            ".csv",
            ".json",
            ".md",
            ".tex",
        }:
            continue
        if path.name == "PACKAGE_VALIDATION.json":
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in PRIVACY_PATTERNS:
            if pattern.search(text):
                hits.append(
                    {
                        "path": path.relative_to(PACKAGE_ROOT).as_posix(),
                        "pattern": pattern.pattern,
                    }
                )
    return hits


def main() -> None:
    if identity(PDF_PATH) != EXPECTED_PDF:
        raise RuntimeError("Reader PDF identity changed")
    scope = source_scope_replay()
    source_zip = build_source_zip()
    image_zip = validate_image_zip()

    uploads = [
        (PDF_NAME, PDF_PATH, "direct_working_reader"),
        (TEX_NAME, TEX_PATH, "direct_editable_master"),
        (SOURCE_ZIP_NAME, SOURCE_ZIP_PATH, "portable_reader_source_and_wip"),
        (IMAGE_ZIP_NAME, IMAGE_ZIP_PATH, "actual_source_image_witnesses"),
    ]
    upload_rows = [
        {
            "upload_name": name,
            "bytes": path.stat().st_size,
            "sha256": sha256_path(path),
            "media_type": media_type(name),
            "release_role": role,
        }
        for name, path, role in uploads
    ]
    write_csv(
        PACKAGE_ROOT / "ZENODO_UPLOAD_MANIFEST.csv",
        upload_rows,
        ["upload_name", "bytes", "sha256", "media_type", "release_role"],
    )

    excluded = {"SHA256SUMS.csv", "PACKAGE_VALIDATION.json"}
    sha_rows: list[dict[str, object]] = []
    for path in sorted(PACKAGE_ROOT.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(PACKAGE_ROOT).as_posix()
        if relative in excluded:
            continue
        sha_rows.append(
            {
                "relative_path": relative,
                "bytes": path.stat().st_size,
                "sha256": sha256_path(path),
            }
        )
    write_csv(
        PACKAGE_ROOT / "SHA256SUMS.csv",
        sha_rows,
        ["relative_path", "bytes", "sha256"],
    )

    privacy_hits = privacy_replay()
    image_validation = json.loads(
        (
            PACKAGE_ROOT
            / "visual-evidence/SGA7II_SOURCE_IMAGE_WITNESS_VALIDATION.json"
        ).read_text(encoding="utf-8")
    )
    errors: list[str] = []
    if privacy_hits:
        errors.append("privacy_hits")
    if image_validation.get("status") != "PASS" or image_validation.get("errors"):
        errors.append("image_validation_not_pass")
    if image_validation.get("zip", {}).get("sha256") != EXPECTED_IMAGE_ZIP[1]:
        errors.append("image_validation_zip_identity_mismatch")
    validation = {
        "status": "PASS_ARCHIVE_HANDOFF_READY" if not errors else "FAIL",
        "errors": errors,
        "claim_boundary": {
            "reader": "working French source transcription, Exposes X-XIV",
            "partial_source": "Expose XV indices 172-203, stops mid-sentence",
            "complete_sga7ii_claim": False,
            "critical_edition_claim": False,
            "diagram_fidelity_certification": False,
            "accessibility_certification": False,
        },
        "scope": scope,
        "reader": {
            "pages": 87,
            "bytes": EXPECTED_PDF[0],
            "sha256": EXPECTED_PDF[1],
        },
        "source_zip": source_zip,
        "image_zip": image_zip,
        "upload_manifest": {
            "rows": len(upload_rows),
            "bytes": (PACKAGE_ROOT / "ZENODO_UPLOAD_MANIFEST.csv").stat().st_size,
            "sha256": sha256_path(PACKAGE_ROOT / "ZENODO_UPLOAD_MANIFEST.csv"),
        },
        "package_manifest": {
            "rows": len(sha_rows),
            "bytes": (PACKAGE_ROOT / "SHA256SUMS.csv").stat().st_size,
            "sha256": sha256_path(PACKAGE_ROOT / "SHA256SUMS.csv"),
        },
        "privacy_hits": privacy_hits,
        "source_images_are_actual_pixels": True,
        "source_image_archive_scope_extends_beyond_reader": True,
        "source_image_archive_does_not_claim_later_text_completion": True,
    }
    write_json(PACKAGE_ROOT / "PACKAGE_VALIDATION.json", validation)
    if errors:
        raise RuntimeError("Release projection validation failed: " + ", ".join(errors))
    print(json.dumps(validation, ensure_ascii=True, indent=2))


if __name__ == "__main__":
    main()
