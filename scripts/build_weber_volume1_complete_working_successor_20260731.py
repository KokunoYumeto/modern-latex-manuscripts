#!/usr/bin/env python3
"""Build and validate the compact Weber Volume I public package."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import zipfile
from pathlib import Path, PurePosixPath

from PIL import Image
from pypdf import PdfReader


REPO_ROOT = Path(__file__).resolve().parents[1]
PACKAGE_REL = Path(
    "sources/weber/weber-volume1-german-complete-working-source-repair-20260731"
)
PACKAGE_ROOT = REPO_ROOT / PACKAGE_REL
TEMP_ROOT = REPO_ROOT / "tmp/zenodo/weber-volume1-complete-working-20260731"
ZIP_PATH = TEMP_ROOT / (
    "80_Weber_VolumeI_German_Complete_Working_Reader_TeX_QA_20260731.zip"
)
PDF_REL = Path(
    "reader/Weber_VolumeI_German_Complete_Working_SourceRepair_20260731.pdf"
)
TEX_REL = Path(
    "source/Weber_VolumeI_German_Complete_Working_SourceRepair_20260731.tex"
)
VISUAL_MANIFEST_REL = Path("visual_witnesses/VISUAL_WITNESS_MANIFEST.csv")
CHECKSUMS_REL = Path("SHA256SUMS.csv")
VALIDATION_REL = Path("PACKAGE_VALIDATION.json")

EXPECTED_PDF = (
    2_275_193,
    "11000F9FA3F65C7C40ADB859A6A89689805012B3DF5D5DC4547E483778E1791A",
)
PARENT_SCAN = {
    "pages": 686,
    "bytes": 51_955_203,
    "sha256": "50BA482A39C9918AC81B31D631B65B11C37C5E67BEC42C559F6D504A28196DEB",
}
EXPECTED_VISUALS = {
    "vol1_p121_crop_4_24.png",
    "vol1_p121_crop_4_28.png",
    "vol1_p123_crop_4_27.png",
    "vol1_p123_crop_4_61.png",
    "vol1_p123_crop_4_81.png",
    "vol1_p124_top.png",
    "vol1_p124_mid.png",
    "vol1_p124_bot.png",
    "vol1_p124_crop_4_21.png",
    "vol1_p124_crop_4_70.png",
    "vol1_p124_crop_4_77.png",
    "vol1_p125_top.png",
    "vol1_p125_mid.png",
    "vol1_p125_bot.png",
}
TEXT_SUFFIXES = {".csv", ".json", ".md", ".tex", ".txt"}
FORBIDDEN_TEXT = (
    re.compile(r"C:\\Users", re.I),
    re.compile(r"\\Papors\\", re.I),
    re.compile(r"\\Chatnotes\\", re.I),
    re.compile(r"\.codex", re.I),
    re.compile(r"\bFloris\b", re.I),
    re.compile(r"\b(?:GPT|ChatGPT|Claude|Codex|Fable)\b", re.I),
    re.compile(r"\b(?:AI|language model)[ -]generated\b", re.I),
    re.compile(r"019f[0-9a-f-]{20,}", re.I),
)


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def save_json(path: Path, value: object) -> None:
    path.write_text(
        json.dumps(value, ensure_ascii=True, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def role_for(relative: str) -> str:
    if relative == PDF_REL.as_posix():
        return "current_reader_pdf"
    if relative == TEX_REL.as_posix():
        return "editable_master_tex"
    if relative.startswith("visual_witnesses/") and relative.endswith(".png"):
        return "source_check_visual_witness"
    if relative.startswith("visual_witnesses/"):
        return "visual_witness_control"
    if relative.startswith("evidence/"):
        return "public_qa_summary"
    return "reader_scope_control"


def make_visual_manifest() -> list[dict[str, object]]:
    root = PACKAGE_ROOT / "visual_witnesses"
    names = {path.name for path in root.glob("*.png")}
    if names != EXPECTED_VISUALS:
        raise RuntimeError(
            f"Visual set mismatch: missing={sorted(EXPECTED_VISUALS - names)}, "
            f"extra={sorted(names - EXPECTED_VISUALS)}"
        )
    rows: list[dict[str, object]] = []
    for path in sorted(root.glob("*.png"), key=lambda item: item.name):
        match = re.search(r"_p(\d+)_", path.name)
        if match is None:
            raise RuntimeError(f"No printed-page locator in {path.name}")
        printed_page = int(match.group(1))
        with Image.open(path) as image:
            image.verify()
        with Image.open(path) as image:
            width, height, mode = image.width, image.height, image.mode
        rows.append(
            {
                "id": f"WEBER-V1-P{printed_page:03d}-{path.stem.upper()}",
                "path": f"visual_witnesses/{path.name}",
                "bytes": path.stat().st_size,
                "sha256": sha256_path(path),
                "parent_scan_sha256": PARENT_SCAN["sha256"],
                "printed_page": printed_page,
                "source_pdf_physical_page_1based": printed_page + 26,
                "locator_basis": "physical_page=printed_page+26",
                "width_px": width,
                "height_px": height,
                "mode": mode,
                "witness_kind": (
                    "tight_high_detail_crop"
                    if "_crop_" in path.name
                    else "overlapping_source_page_band"
                ),
                "linked_source": TEX_REL.as_posix(),
                "qa_disposition": (
                    "reviewed_cold_reverify_support"
                    if printed_page <= 124
                    else "pending_next_cursor_source_band"
                ),
            }
        )
    write_csv(
        PACKAGE_ROOT / VISUAL_MANIFEST_REL,
        [
            "id",
            "path",
            "bytes",
            "sha256",
            "parent_scan_sha256",
            "printed_page",
            "source_pdf_physical_page_1based",
            "locator_basis",
            "width_px",
            "height_px",
            "mode",
            "witness_kind",
            "linked_source",
            "qa_disposition",
        ],
        rows,
    )
    return rows


def validate_pdf(path: Path) -> dict[str, object]:
    if (path.stat().st_size, sha256_path(path)) != EXPECTED_PDF:
        raise RuntimeError("Reader PDF identity changed")
    reader = PdfReader(str(path))
    if len(reader.pages) != 420:
        raise RuntimeError(f"Expected 420 PDF pages, found {len(reader.pages)}")
    empty: list[int] = []
    image_pages: list[int] = []
    type3: list[str] = []
    sizes: set[tuple[float, float]] = set()
    font_resources: set[tuple[str, str]] = set()
    for page_number, page in enumerate(reader.pages, 1):
        if not (page.extract_text() or "").strip():
            empty.append(page_number)
        sizes.add(
            (
                round(float(page.mediabox.width), 3),
                round(float(page.mediabox.height), 3),
            )
        )
        resources = page.get("/Resources") or {}
        for reference in (resources.get("/XObject") or {}).values():
            obj = reference.get_object()
            if obj.get("/Subtype") == "/Image":
                image_pages.append(page_number)
        for reference in (resources.get("/Font") or {}).values():
            obj = reference.get_object()
            subtype = str(obj.get("/Subtype") or "")
            name = str(obj.get("/BaseFont") or "")
            font_resources.add((name, subtype))
            if subtype == "/Type3":
                type3.append(name)
    if empty or image_pages or type3:
        raise RuntimeError(
            f"PDF gate failed: empty={empty}, images={image_pages}, type3={type3}"
        )
    return {
        "pages": len(reader.pages),
        "page_sizes_points": [list(item) for item in sorted(sizes)],
        "empty_text_pages": empty,
        "image_xobject_pages": image_pages,
        "font_resources": len(font_resources),
        "type3_fonts": type3,
    }


def scan_text_privacy() -> list[dict[str, str]]:
    hits: list[dict[str, str]] = []
    for path in sorted(PACKAGE_ROOT.rglob("*")):
        if not path.is_file() or path.suffix.casefold() not in TEXT_SUFFIXES:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for pattern in FORBIDDEN_TEXT:
            if pattern.search(text):
                hits.append(
                    {
                        "path": path.relative_to(PACKAGE_ROOT).as_posix(),
                        "pattern": pattern.pattern,
                    }
                )
    return hits


def make_checksums() -> list[dict[str, object]]:
    excluded = {CHECKSUMS_REL.as_posix(), VALIDATION_REL.as_posix()}
    rows: list[dict[str, object]] = []
    for path in sorted(PACKAGE_ROOT.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(PACKAGE_ROOT).as_posix()
        if relative in excluded:
            continue
        rows.append(
            {
                "path": relative,
                "bytes": path.stat().st_size,
                "sha256": sha256_path(path),
                "role": role_for(relative),
            }
        )
    write_csv(
        PACKAGE_ROOT / CHECKSUMS_REL,
        ["path", "bytes", "sha256", "role"],
        rows,
    )
    return rows


def canonical_aggregate(rows: list[dict[str, object]]) -> str:
    data = "".join(
        f"{row['path']}\t{row['bytes']}\t{row['sha256']}\n" for row in rows
    ).encode("utf-8")
    return sha256_bytes(data)


def build_zip() -> dict[str, object]:
    TEMP_ROOT.mkdir(parents=True, exist_ok=True)
    if ZIP_PATH.exists():
        ZIP_PATH.unlink()
    files = [path for path in sorted(PACKAGE_ROOT.rglob("*")) if path.is_file()]
    with zipfile.ZipFile(
        ZIP_PATH,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
        strict_timestamps=True,
    ) as archive:
        for path in files:
            relative = path.relative_to(PACKAGE_ROOT).as_posix()
            pure = PurePosixPath(relative)
            if pure.is_absolute() or ".." in pure.parts or "\\" in relative:
                raise RuntimeError(f"Unsafe ZIP member: {relative}")
            info = zipfile.ZipInfo(relative, date_time=(2026, 7, 31, 12, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes(), compresslevel=9)
    with zipfile.ZipFile(ZIP_PATH) as archive:
        if archive.testzip() is not None:
            raise RuntimeError("ZIP CRC validation failed")
        member_rows = [
            {
                "path": info.filename,
                "bytes": info.file_size,
                "sha256": sha256_bytes(archive.read(info.filename)),
            }
            for info in archive.infolist()
            if not info.is_dir()
        ]
    return {
        "path": str(ZIP_PATH),
        "bytes": ZIP_PATH.stat().st_size,
        "sha256": sha256_path(ZIP_PATH),
        "members": len(member_rows),
        "uncompressed_bytes": sum(int(row["bytes"]) for row in member_rows),
        "member_aggregate_sha256": canonical_aggregate(member_rows),
    }


def main() -> None:
    visual_rows = make_visual_manifest()
    pdf = validate_pdf(PACKAGE_ROOT / PDF_REL)
    privacy_hits = scan_text_privacy()
    if privacy_hits:
        raise RuntimeError(f"Privacy/process-name hits: {privacy_hits}")
    checksum_rows = make_checksums()
    represented_paths = {str(row["path"]) for row in checksum_rows}
    actual_represented = {
        path.relative_to(PACKAGE_ROOT).as_posix()
        for path in PACKAGE_ROOT.rglob("*")
        if path.is_file()
        and path.relative_to(PACKAGE_ROOT).as_posix()
        not in {CHECKSUMS_REL.as_posix(), VALIDATION_REL.as_posix()}
    }
    if represented_paths != actual_represented:
        raise RuntimeError("Checksum manifest does not close the represented tree")
    validation = {
        "status": "PASS_READY_FOR_GITHUB_AND_SAME_CONCEPT_ZENODO_SUCCESSOR",
        "errors": [],
        "scope": "Weber Volume I German complete working reader through Section 188 and errata",
        "strict_cold_reverify_cursor": {
            "complete_through_printed_page": 124,
            "next_printed_page": 125,
        },
        "parent_scan": PARENT_SCAN,
        "reader": {
            "path": PDF_REL.as_posix(),
            "bytes": EXPECTED_PDF[0],
            "sha256": EXPECTED_PDF[1],
            **pdf,
        },
        "editable_source": {
            "path": TEX_REL.as_posix(),
            "bytes": (PACKAGE_ROOT / TEX_REL).stat().st_size,
            "sha256": sha256_path(PACKAGE_ROOT / TEX_REL),
        },
        "isolated_rebuild": {
            "passes": 3,
            "pages": 420,
            "bytes": 2_275_193,
            "sha256": "1C43B8A48415ECA5A85169C2033AD48F75240EFCFA2D80F6ACE9BF082B6819A6",
            "extracted_text_page_differences": [],
            "decoded_page_content_stream_differences": [],
            "page_geometry_differences": [],
            "difference_disposition": "pdfTeX creation and modification timestamps only",
        },
        "visual_witnesses": {
            "files": len(visual_rows),
            "bytes": sum(int(row["bytes"]) for row in visual_rows),
            "reviewed_files": sum(
                row["qa_disposition"] == "reviewed_cold_reverify_support"
                for row in visual_rows
            ),
            "pending_cursor_files": sum(
                row["qa_disposition"] == "pending_next_cursor_source_band"
                for row in visual_rows
            ),
        },
        "represented_files": len(checksum_rows),
        "represented_bytes": sum(int(row["bytes"]) for row in checksum_rows),
        "represented_aggregate_sha256": canonical_aggregate(checksum_rows),
        "privacy_or_agent_process_hits": privacy_hits,
        "claim_limits": [
            "working reader, not a critical edition",
            "strict page-by-page cold re-verification complete only through printed p.124",
            "not mathematical, peer-review, rights-clearance, or accessibility certification",
        ],
    }
    save_json(PACKAGE_ROOT / VALIDATION_REL, validation)
    final_files = [path for path in PACKAGE_ROOT.rglob("*") if path.is_file()]
    zip_identity = build_zip()
    result = {
        "package_root": str(PACKAGE_ROOT),
        "package_files": len(final_files),
        "package_bytes": sum(path.stat().st_size for path in final_files),
        "checksums": {
            "rows": len(checksum_rows),
            "bytes": (PACKAGE_ROOT / CHECKSUMS_REL).stat().st_size,
            "sha256": sha256_path(PACKAGE_ROOT / CHECKSUMS_REL),
        },
        "validation": {
            "bytes": (PACKAGE_ROOT / VALIDATION_REL).stat().st_size,
            "sha256": sha256_path(PACKAGE_ROOT / VALIDATION_REL),
        },
        "zip": zip_identity,
    }
    save_json(TEMP_ROOT / "BUILD_RESULT.json", result)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
