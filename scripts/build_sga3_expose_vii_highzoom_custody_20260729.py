#!/usr/bin/env python3
"""Build the compact GitHub custody package for the SGA3 Expose VII input."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
import zipfile
from pathlib import Path, PurePosixPath


REPO = Path(__file__).resolve().parents[1]
SOURCE: Path
OUTPUT = (
    REPO
    / "sources"
    / "sga"
    / "sga3-expose-vii-highzoom-native-integration-input-20260729"
)
ZIP_NAME = "10c_SGA3_Expose_VII_HighZoom_Native_Integration_Input_20260729.zip"
ZIP_TIME = (2026, 7, 29, 0, 0, 0)
TEXT_EXTENSIONS = {
    ".bib",
    ".cls",
    ".csv",
    ".json",
    ".jsonl",
    ".log",
    ".md",
    ".sty",
    ".tex",
    ".txt",
}
PRIVATE_PATTERNS = {
    "private_home": re.compile(rb"C:\\Users\\Floris", re.IGNORECASE),
    "private_github": re.compile(rb"C:\\IL_GitHub", re.IGNORECASE),
    "papors": re.compile(rb"Papors", re.IGNORECASE),
    "chatnotes": re.compile(rb"Chatnotes", re.IGNORECASE),
    "codex_thread": re.compile(
        rb"\b019[0-9a-f]{5}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b",
        re.IGNORECASE,
    ),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source",
        required=True,
        type=Path,
        help="Exact local SGA3 Expose VII public-projection root.",
    )
    return parser.parse_args()


def source_files() -> list[Path]:
    return sorted(
        (path for path in SOURCE.rglob("*") if path.is_file()),
        key=lambda path: path.relative_to(SOURCE).as_posix(),
    )


def validate_source_manifest(files: list[Path]) -> dict[str, object]:
    manifest_path = SOURCE / "SHA256SUMS.csv"
    with manifest_path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))

    expected = {
        path.relative_to(SOURCE).as_posix(): path
        for path in files
        if path != manifest_path
    }
    errors: list[str] = []
    seen: set[str] = set()
    for row in rows:
        relative = row["relative_path"]
        if relative in seen:
            errors.append(f"duplicate manifest path: {relative}")
            continue
        seen.add(relative)
        path = expected.get(relative)
        if path is None:
            errors.append(f"manifest path missing from tree: {relative}")
            continue
        if int(row["bytes"]) != path.stat().st_size:
            errors.append(f"byte mismatch: {relative}")
        if row["sha256"].upper() != sha256(path):
            errors.append(f"SHA-256 mismatch: {relative}")

    missing = sorted(set(expected) - seen)
    errors.extend(f"tree path missing from manifest: {relative}" for relative in missing)
    if errors:
        raise RuntimeError("\n".join(errors))

    return {
        "rows": len(rows),
        "manifest_bytes": manifest_path.stat().st_size,
        "manifest_sha256": sha256(manifest_path),
    }


def privacy_scan(files: list[Path]) -> dict[str, object]:
    hits: list[dict[str, str]] = []
    scanned = 0
    for path in files:
        if path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        scanned += 1
        data = path.read_bytes()
        for name, pattern in PRIVATE_PATTERNS.items():
            if pattern.search(data):
                hits.append(
                    {
                        "relative_path": path.relative_to(SOURCE).as_posix(),
                        "pattern": name,
                    }
                )
    if hits:
        raise RuntimeError(f"privacy scan failed: {hits}")
    return {"text_files_scanned": scanned, "hits": hits, "hit_count": len(hits)}


def zip_info(name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, date_time=ZIP_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    return info


def build_zip(files: list[Path], destination: Path) -> dict[str, object]:
    with zipfile.ZipFile(destination, "w", allowZip64=True) as archive:
        for path in files:
            name = path.relative_to(SOURCE).as_posix()
            archive.writestr(
                zip_info(name),
                path.read_bytes(),
                compress_type=zipfile.ZIP_DEFLATED,
                compresslevel=9,
            )

    errors: list[str] = []
    expected = {path.relative_to(SOURCE).as_posix(): path for path in files}
    with zipfile.ZipFile(destination) as archive:
        bad = archive.testzip()
        if bad:
            errors.append(f"CRC failure: {bad}")
        names = archive.namelist()
        if len(names) != len(set(names)):
            errors.append("duplicate ZIP member names")
        if set(names) != set(expected):
            errors.append("ZIP member set differs from source tree")
        for name in names:
            pure = PurePosixPath(name)
            if pure.is_absolute() or ".." in pure.parts or "\\" in name:
                errors.append(f"unsafe ZIP member name: {name}")
                continue
            data = archive.read(name)
            if hashlib.sha256(data).hexdigest().upper() != sha256(expected[name]):
                errors.append(f"ZIP member hash mismatch: {name}")
        uncompressed = sum(info.file_size for info in archive.infolist())

    if errors:
        raise RuntimeError("\n".join(errors))
    return {
        "filename": destination.name,
        "bytes": destination.stat().st_size,
        "sha256": sha256(destination),
        "members": len(files),
        "uncompressed_bytes": uncompressed,
        "crc_test": "PASS",
        "safe_member_names": True,
        "member_hash_readback": "PASS",
    }


def write_readme(zip_result: dict[str, object]) -> None:
    text = f"""# SGA 3 Expose VII native-diagram integration input

This directory preserves the exact source-only Expose VII successor used for
the next cumulative SGA 3 reader. The compact ZIP contains the English master,
97 components, 135 native TikZ/TikZ-cd diagrams, the 208-page reader, and the
package's validation and checksum controls.

## Scope and quality

- Scope: complete SGA 3 Expose VII only.
- Reader: 208 A4 pages.
- Native diagrams: 135/135.
- Direct authority/native comparison: 135/135 at 5,000 dpi.
- Corrected after high-zoom review: 019, 028, 040, 046, 049, 107, 108,
  126, 127, and 128.
- Reader-layout review: 22 changed or adjacent pages at 600 dpi.
- Raster delivery: none; active `includegraphics` calls and PDF image objects
  are both zero.
- Internal PDF actions: 312, with zero broken actions.

The authority PDFs are identified by hash inside the archive but are not
redistributed. OCR, authority crops, temporary comparison renders, raw logs,
private paths, and superseded builds are excluded.

## Archive identity

- ZIP: `{ZIP_NAME}`
- ZIP bytes: {zip_result["bytes"]}
- ZIP SHA-256: `{zip_result["sha256"]}`
- Members: {zip_result["members"]}
- Uncompressed member bytes: {zip_result["uncompressed_bytes"]}

This is a bounded integration input, not a separate current public reader and
not a claim that the cumulative SGA 3 reference graph is closed. The current
direct SGA 3 reader remains the first reader-facing object on the established
SGA Zenodo concept. This package is intended to be absorbed by its next
no-overwrite cumulative successor.

Jacob Reinhold's SGA Markdown at revision
`e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e` is credited inside the archive as
comparison and drafting lineage under his stated CC BY 4.0 terms. It is not
the source authority. No blanket license over the underlying French work or
the reconstructed package is asserted.
"""
    (OUTPUT / "README.md").write_text(text, encoding="utf-8", newline="\n")


def write_validation(
    files: list[Path],
    source_manifest: dict[str, object],
    privacy: dict[str, object],
    zip_result: dict[str, object],
) -> None:
    validation = {
        "status": "PASS",
        "errors": [],
        "scope": "SGA 3 Expose VII source-only native-diagram integration input",
        "source_tree": {
            "files": len(files),
            "bytes": sum(path.stat().st_size for path in files),
            "self_excluding_manifest": source_manifest,
        },
        "zip": zip_result,
        "privacy": privacy,
        "reader": {
            "pages": 208,
            "pdf_sha256": (
                "FF96CE59AC0068F520F29C5AAD370ADE637D81C2AC6B2C747C5CE9E80E95AE6B"
            ),
            "native_diagrams": 135,
            "lead_5000dpi_rows": 135,
            "repaired_diagrams": [19, 28, 40, 46, 49, 107, 108, 126, 127, 128],
            "includegraphics_invocations": 0,
            "pdf_image_objects": 0,
            "broken_internal_actions": 0,
        },
        "disposition": {
            "github_custody": "READY",
            "zenodo_reader_surface": "DEFER_TO_CUMULATIVE_SUCCESSOR",
            "current_direct_reader_replaced": False,
        },
    }
    (OUTPUT / "PACKAGE_VALIDATION.json").write_text(
        json.dumps(validation, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def write_outer_manifest() -> None:
    represented = [
        OUTPUT / ZIP_NAME,
        OUTPUT / "PACKAGE_VALIDATION.json",
        OUTPUT / "README.md",
    ]
    rows = [
        {
            "relative_path": path.name,
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        }
        for path in represented
    ]
    with (OUTPUT / "SHA256SUMS.csv").open(
        "w", encoding="utf-8", newline=""
    ) as handle:
        writer = csv.DictWriter(
            handle, fieldnames=["relative_path", "bytes", "sha256"], lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    global SOURCE
    SOURCE = parse_args().source.resolve()
    if not SOURCE.is_dir():
        raise SystemExit(f"source package does not exist: {SOURCE}")
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir(parents=True)

    files = source_files()
    source_manifest = validate_source_manifest(files)
    privacy = privacy_scan(files)
    zip_result = build_zip(files, OUTPUT / ZIP_NAME)
    write_readme(zip_result)
    write_validation(files, source_manifest, privacy, zip_result)
    write_outer_manifest()

    result = {
        "output": str(OUTPUT),
        "outer_files": len([path for path in OUTPUT.iterdir() if path.is_file()]),
        "outer_bytes": sum(path.stat().st_size for path in OUTPUT.iterdir() if path.is_file()),
        "zip": zip_result,
        "outer_manifest_sha256": sha256(OUTPUT / "SHA256SUMS.csv"),
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
