#!/usr/bin/env python3
"""Build the compact SGA3 current-progress full-volume integration package."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import shutil
import zipfile
from pathlib import Path, PurePosixPath

from pypdf import PdfReader


PDF_NAME = "00c_SGA3_English_CurrentProgress_Cumulative_Latest_20260728.pdf"
TEX_NAME = "02c_SGA3_English_CurrentProgress_Cumulative_Latest_20260728.tex"
SOURCE_ZIP_NAME = (
    "10c9_SGA3_CurrentProgress_FullVolume_Integration_Source_20260728.zip"
)
MASTER_NAME = "SGA3_English_Loop1_Full_Volume_Integration.tex"
EXPECTED_PDF_SHA256 = (
    "481EEDECAA8635AEAC5CCA91492797AF651D426A80B6A2F2510BDF05EB3DD36D"
)
EXPECTED_SOURCE_AGGREGATE = (
    "9696700CD20A12778AA060C970EB4B54C071C76C0CCDA8A9BA97DBB5643124B7"
)
EXPECTED_PAGES = 1434
EXPECTED_DESTINATIONS = 9246
EXPECTED_GOTO_ACTIONS = 4541
EXPECTED_FONT_RESOURCES = 64
EXPECTED_RASTER_XOBJECTS = 142
EXPECTED_CLOSURE_FILES = 865
EXPECTED_CLOSURE_BYTES = 7459146
FIXED_ZIP_TIME = (2026, 7, 28, 0, 0, 0)
PUBLIC_DOCS = (
    "README.md",
    "PUBLICATION_READINESS.md",
    "BUILD_SUMMARY_PUBLIC.md",
    "FINAL_VISUAL_QA.md",
    "INDEPENDENT_SOURCE_ARCHIVE_REBUILD_PASS.md",
)
TEXT_SUFFIXES = {
    ".bib",
    ".cls",
    ".csv",
    ".json",
    ".jsonl",
    ".md",
    ".ndjson",
    ".sty",
    ".tex",
    ".txt",
    ".yaml",
    ".yml",
}
PRIVATE_MARKERS = (
    b"c:\\users\\",
    b"c:/users/",
    b"\\appdata\\",
    b"/appdata/",
    b"papors",
    b"chatnotes",
    b".claude",
    b".codex",
    b"source_thread_id",
    b"thread_id",
    b"claude-please",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--integration-root", type=Path, required=True)
    parser.add_argument("--recorder-file", type=Path, required=True)
    parser.add_argument("--reader-pdf", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def csv_bytes(rows: list[dict[str, object]], fields: list[str]) -> bytes:
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue().encode("utf-8")


def safe_member(name: str) -> bool:
    parts = PurePosixPath(name).parts
    return (
        bool(name)
        and not name.startswith(("/", "\\"))
        and re.match(r"^[A-Za-z]:", name) is None
        and ".." not in parts
    )


def zip_info(name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, date_time=FIXED_ZIP_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.create_system = 3
    info.external_attr = 0o100644 << 16
    return info


def role_for(name: str) -> str:
    suffix = PurePosixPath(name).suffix.lower()
    if suffix == ".tex":
        return "editable_source"
    if suffix == ".png":
        return "loop1_diagram_asset_provisional_not_diagram_final"
    if suffix == ".csv":
        return "machine_manifest"
    if suffix == ".json":
        return "machine_validation"
    return "build_dependency"


def normalized_aggregate(root: Path) -> str:
    digest = hashlib.sha256()
    files = sorted(
        (
            path
            for path in root.rglob("*")
            if path.is_file()
            and "archive_build" not in path.parts
            and "$build" not in path.parts
        ),
        key=lambda path: path.relative_to(root).as_posix(),
    )
    for path in files:
        relative = path.relative_to(root).as_posix()
        row = f"{relative}\t{path.stat().st_size}\t{sha256(path)}\n"
        digest.update(row.encode("utf-8"))
    return digest.hexdigest().upper()


def parse_recorder_closure(root: Path, recorder: Path) -> list[Path]:
    closure: set[Path] = set()
    for line in recorder.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.startswith("INPUT "):
            continue
        raw = line[6:]
        candidate = Path(raw)
        if not candidate.is_absolute():
            candidate = root / candidate
        try:
            candidate = candidate.resolve()
            relative = candidate.relative_to(root)
        except (OSError, ValueError):
            continue
        if (
            candidate.is_file()
            and relative.parts
            and relative.parts[0] not in {"archive_build", "$build"}
        ):
            closure.add(candidate)
    return sorted(
        closure,
        key=lambda path: path.relative_to(root).as_posix().lower(),
    )


def scan_bytes(name: str, data: bytes, hits: list[dict[str, str]]) -> None:
    lowered = data.lower()
    for marker in PRIVATE_MARKERS:
        if marker in lowered:
            hits.append(
                {
                    "path": name,
                    "marker": marker.decode("ascii", errors="replace"),
                    "surface": "raw_bytes",
                }
            )


def scan_pdf(name: str, data: bytes, hits: list[dict[str, str]]) -> None:
    scan_bytes(name, data, hits)
    reader = PdfReader(io.BytesIO(data))
    metadata = " ".join(str(value) for value in (reader.metadata or {}).values())
    extracted = "\n".join(page.extract_text() or "" for page in reader.pages)
    scan_bytes(
        name,
        (metadata + "\n" + extracted).encode("utf-8", errors="replace"),
        hits,
    )


def pdf_metrics(path: Path) -> dict[str, int]:
    reader = PdfReader(path)
    goto = 0
    invalid = 0
    uri = 0
    linked_pages = 0
    font_objects: set[tuple[int, int] | str] = set()
    raster_objects: set[tuple[int, int] | str] = set()
    type3 = 0
    for page in reader.pages:
        page_links = 0
        for annotation_ref in page.get("/Annots") or []:
            annotation = annotation_ref.get_object()
            action = annotation.get("/A")
            destination = annotation.get("/Dest")
            if action and action.get("/S") == "/GoTo":
                goto += 1
                page_links += 1
                if action.get("/D") is None:
                    invalid += 1
            elif destination is not None:
                goto += 1
                page_links += 1
            elif action and action.get("/S") == "/URI":
                uri += 1
            elif action is not None:
                invalid += 1
        if page_links:
            linked_pages += 1
        resources = page.get("/Resources") or {}
        fonts = resources.get("/Font") or {}
        if hasattr(fonts, "get_object"):
            fonts = fonts.get_object()
        for font_ref in fonts.values():
            key = (
                (int(font_ref.idnum), int(font_ref.generation))
                if hasattr(font_ref, "idnum")
                else repr(font_ref)
            )
            font_objects.add(key)
            if font_ref.get_object().get("/Subtype") == "/Type3":
                type3 += 1
        xobjects = resources.get("/XObject") or {}
        if hasattr(xobjects, "get_object"):
            xobjects = xobjects.get_object()
        for object_ref in xobjects.values():
            object_value = object_ref.get_object()
            if object_value.get("/Subtype") != "/Image":
                continue
            key = (
                (int(object_ref.idnum), int(object_ref.generation))
                if hasattr(object_ref, "idnum")
                else repr(object_ref)
            )
            raster_objects.add(key)
    return {
        "pages": len(reader.pages),
        "named_destinations": len(reader.named_destinations),
        "internal_goto_actions": goto,
        "linked_pages": linked_pages,
        "invalid_actions": invalid,
        "uri_actions": uri,
        "font_resources": len(font_objects),
        "type3_fonts": type3,
        "raster_xobjects": len(raster_objects),
    }


def main() -> int:
    args = parse_args()
    root = args.integration_root.resolve()
    recorder = args.recorder_file.resolve()
    reader = args.reader_pdf.resolve()
    output = args.output_dir.resolve()
    output.mkdir(parents=True, exist_ok=True)
    errors: list[str] = []

    master = root / MASTER_NAME
    for path in (root, recorder, reader, master):
        if not path.exists():
            errors.append(f"missing input: {path}")
    if errors:
        raise SystemExit("\n".join(errors))

    if normalized_aggregate(root) != EXPECTED_SOURCE_AGGREGATE:
        errors.append("immutable source snapshot aggregate mismatch")

    pdf_path = output / PDF_NAME
    tex_path = output / TEX_NAME
    shutil.copyfile(reader, pdf_path)
    shutil.copyfile(master, tex_path)

    if sha256(pdf_path) != EXPECTED_PDF_SHA256:
        errors.append("reader PDF identity mismatch")
    metrics = pdf_metrics(pdf_path)
    for field, expected in (
        ("pages", EXPECTED_PAGES),
        ("named_destinations", EXPECTED_DESTINATIONS),
        ("internal_goto_actions", EXPECTED_GOTO_ACTIONS),
        ("invalid_actions", 0),
        ("uri_actions", 0),
        ("font_resources", EXPECTED_FONT_RESOURCES),
        ("type3_fonts", 0),
        ("raster_xobjects", EXPECTED_RASTER_XOBJECTS),
    ):
        if metrics[field] != expected:
            errors.append(
                f"PDF metric {field}={metrics[field]} expected {expected}"
            )

    closure = parse_recorder_closure(root, recorder)
    closure_bytes = sum(path.stat().st_size for path in closure)
    if len(closure) != EXPECTED_CLOSURE_FILES:
        errors.append(
            f"closure files={len(closure)} expected {EXPECTED_CLOSURE_FILES}"
        )
    if closure_bytes != EXPECTED_CLOSURE_BYTES:
        errors.append(
            f"closure bytes={closure_bytes} expected {EXPECTED_CLOSURE_BYTES}"
        )

    members: dict[str, bytes] = {}
    privacy_hits: list[dict[str, str]] = []
    for source in closure:
        relative = source.relative_to(root).as_posix()
        if not safe_member(relative):
            errors.append(f"unsafe source member: {relative}")
            continue
        if relative in members:
            errors.append(f"duplicate source member: {relative}")
            continue
        data = source.read_bytes()
        members[relative] = data
        scan_bytes(relative, data, privacy_hits)
    scan_pdf(PDF_NAME, pdf_path.read_bytes(), privacy_hits)
    scan_bytes(TEX_NAME, tex_path.read_bytes(), privacy_hits)
    if privacy_hits:
        errors.append(f"privacy hits: {privacy_hits[:20]}")

    source_validation = {
        "schema": "sga3_full_volume_working_source_bundle_v1",
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "scope": {
            "included": (
                "Editorial Notice, Introduction, Exposes I-XXIII and XXV-XXVI, "
                "terminal bibliography and Tome III index"
            ),
            "explicit_gaps": "four-page Tome III guide and Expose XXIV",
            "claim": (
                "current-progress Loop-1 working reader; incomplete and not "
                "diagram-final"
            ),
        },
        "source_snapshot": {
            "files": 1220,
            "bytes": 20733477,
            "ordered_aggregate_sha256": EXPECTED_SOURCE_AGGREGATE,
        },
        "recorder_closure": {
            "files": len(closure),
            "bytes": closure_bytes,
            "tex_files": sum(path.suffix.lower() == ".tex" for path in closure),
            "png_files": sum(path.suffix.lower() == ".png" for path in closure),
        },
        "reader": {
            "filename": PDF_NAME,
            "bytes": pdf_path.stat().st_size,
            "sha256": sha256(pdf_path),
            **metrics,
        },
        "privacy": {"hits": privacy_hits},
    }
    validation_data = (
        json.dumps(source_validation, indent=2, ensure_ascii=True) + "\n"
    ).encode("utf-8")
    members["SOURCE_BUNDLE_VALIDATION.json"] = validation_data

    manifest_rows = [
        {
            "relative_path": name,
            "bytes": len(data),
            "sha256": sha256_bytes(data),
            "role": role_for(name),
        }
        for name, data in sorted(members.items(), key=lambda item: item[0].lower())
    ]
    manifest_data = csv_bytes(
        manifest_rows,
        ["relative_path", "bytes", "sha256", "role"],
    )
    members["SOURCE_BUNDLE_SHA256.csv"] = manifest_data

    source_zip = output / SOURCE_ZIP_NAME
    with zipfile.ZipFile(
        source_zip,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
        allowZip64=True,
    ) as archive:
        for name, data in sorted(members.items(), key=lambda item: item[0].lower()):
            archive.writestr(zip_info(name), data)

    zip_errors: list[str] = []
    with zipfile.ZipFile(source_zip) as archive:
        bad = archive.testzip()
        if bad:
            zip_errors.append(f"CRC failure: {bad}")
        names = archive.namelist()
        if len(names) != len(set(names)):
            zip_errors.append("duplicate ZIP member")
        if set(names) != set(members):
            zip_errors.append("exact ZIP member set mismatch")
        for name in names:
            if not safe_member(name):
                zip_errors.append(f"unsafe ZIP member: {name}")
            if archive.read(name) != members[name]:
                zip_errors.append(f"ZIP member identity mismatch: {name}")
    errors.extend(zip_errors)

    for name in PUBLIC_DOCS:
        path = output / name
        if not path.is_file():
            errors.append(f"missing public document: {name}")
        else:
            scan_bytes(name, path.read_bytes(), privacy_hits)
    if privacy_hits and not any(error.startswith("privacy hits:") for error in errors):
        errors.append(f"privacy hits: {privacy_hits[:20]}")

    package_validation = {
        "schema": "sga3_full_volume_working_outer_package_v1",
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "reader": {
            "filename": PDF_NAME,
            "bytes": pdf_path.stat().st_size,
            "sha256": sha256(pdf_path),
            **metrics,
        },
        "master_tex": {
            "filename": TEX_NAME,
            "bytes": tex_path.stat().st_size,
            "sha256": sha256(tex_path),
        },
        "source_archive": {
            "filename": SOURCE_ZIP_NAME,
            "bytes": source_zip.stat().st_size,
            "sha256": sha256(source_zip),
            "members": len(members),
            "uncompressed_bytes": sum(len(data) for data in members.values()),
            "manifest_rows": len(manifest_rows),
            "manifest_sha256": sha256_bytes(manifest_data),
            "crc_or_identity_errors": zip_errors,
        },
        "visual_qa": {
            "pages_reviewed": [
                1,
                2,
                14,
                16,
                20,
                72,
                129,
                213,
                276,
                324,
                366,
                506,
                507,
                711,
                740,
                774,
                775,
                816,
                852,
                900,
                930,
                965,
                1028,
                1029,
                1053,
                1107,
                1108,
                1128,
                1130,
                1155,
                1194,
                1248,
                1326,
                1361,
                1363,
                1375,
                1431,
                1434,
            ],
            "result": "PASS",
        },
        "privacy": {"hits": privacy_hits},
    }
    validation_path = output / "PACKAGE_VALIDATION.json"
    validation_path.write_text(
        json.dumps(package_validation, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )

    outer_names = {
        PDF_NAME,
        TEX_NAME,
        SOURCE_ZIP_NAME,
        "build_package.py",
        "PACKAGE_VALIDATION.json",
        *PUBLIC_DOCS,
    }
    outer_paths = sorted(
        (
            output / name
            for name in outer_names
            if (output / name).is_file()
        ),
        key=lambda path: path.name.lower(),
    )
    outer_rows = [
        {
            "filename": path.name,
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        }
        for path in outer_paths
    ]
    sums_path = output / "SHA256SUMS.csv"
    sums_path.write_bytes(
        csv_bytes(outer_rows, ["filename", "bytes", "sha256"])
    )

    result = {
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "reader": package_validation["reader"],
        "master_tex": package_validation["master_tex"],
        "source_archive": package_validation["source_archive"],
        "outer_manifest_rows": len(outer_rows),
        "outer_manifest_sha256": sha256(sums_path),
    }
    print(json.dumps(result, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
