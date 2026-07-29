#!/usr/bin/env python3
"""Build the compact, reader-clean SGA3 R18 native-update package."""

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


PDF_NAME = (
    "00c00_SGA3_English_Complete_Reader_"
    "Native_Update_R18_20260729.pdf"
)
TEX_NAME = (
    "02c00_SGA3_English_Complete_Reader_"
    "Native_Update_R18_20260729.tex"
)
SOURCE_ZIP_NAME = (
    "10c9_SGA3_English_Complete_Reader_"
    "Source_and_History_R18_20260729.zip"
)
BUNDLE_MASTER_NAME = (
    "SGA3_English_Complete_Reader_Native_Update_R18_20260729.tex"
)
PREDECESSOR_PDF_NAME = (
    "00c00_SGA3_English_Complete_Reader_Native_Update_R17_20260729.pdf"
)
PREDECESSOR_TEX_NAME = (
    "02c00_SGA3_English_Complete_Reader_Native_Update_R17_20260729.tex"
)

EXPECTED_PDF = (
    10_466_981,
    "1626FE58BCD43DEBBC63AB7144DE227ACA4109092E7A67CA0DE2609AF36F9F75",
)
EXPECTED_MASTER = (
    21_853,
    "9D5BA11B11E895156AB4D708A169E1BD51C19052B3A03A11A4E3BD30E0354396",
)
EXPECTED_PREDECESSOR_PDF = (
    10_668_964,
    "9761E6F89988E2CF5FDE78C5B398CD96846D28F7D364B1EF2D0EEB9BFD2662C8",
)
EXPECTED_PREDECESSOR_TEX = (
    21_853,
    "9D5BA11B11E895156AB4D708A169E1BD51C19052B3A03A11A4E3BD30E0354396",
)
EXPECTED_CLOSURE_FILES = 898
EXPECTED_CLOSURE_BYTES = 6_296_463
EXPECTED_CLOSURE_TEX = 795
EXPECTED_CLOSURE_PNG = 103
EXPECTED_CLOSURE_AGGREGATE = (
    "EBC582A2A3ADD91E31AB9011AC4CC1360D6E5EC716F11802F32888EB1C43F680"
)
EXPECTED_PDF_METRICS = {
    "pages": 1470,
    "named_destinations": 9485,
    "internal_goto_actions": 4591,
    "linked_pages": 1063,
    "invalid_actions": 0,
    "uri_actions": 0,
    "font_resources": 62,
    "type3_fonts": 0,
    "raster_xobjects": 103,
}

FIXED_ZIP_TIME = (2026, 7, 29, 0, 0, 0)
ALLOWED_SOURCE_SUFFIXES = {".bib", ".cls", ".png", ".sty", ".tex"}
PUBLIC_DOCS = (
    "README.md",
    "PROVENANCE_AND_RIGHTS.md",
    "PUBLICATION_READINESS.md",
    "BUILD_SUMMARY_PUBLIC.md",
    "FINAL_VISUAL_QA.md",
)
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
PROCESS_PATTERNS = (
    r"\bChatGPT\b",
    r"\bClaude\b",
    r"\bCodex\b",
    r"\bLLM\b",
    r"GPU\s+OCR",
    r"\bOCR\b",
    r"Reinhold",
    r"Loop[- ]?1",
    r"working[- ]state",
    r"current translation boundary",
    r"producing session",
    r"internal checkpoint",
    r"release readiness",
    r"comparison lineage",
    r"machine[- ]ledger",
    r"independent review",
    r"Temporary\s+(?:Loop[- ]?1\s+)?image",
    r"source locator",
    r"source status",
    r"production status",
    r"workflow status",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--integration-root", type=Path, required=True)
    parser.add_argument("--overlay-root", type=Path, required=True)
    parser.add_argument("--recorder-file", type=Path, required=True)
    parser.add_argument("--reader-pdf", type=Path, required=True)
    parser.add_argument("--master-tex", type=Path, required=True)
    parser.add_argument("--predecessor-pdf", type=Path, required=True)
    parser.add_argument("--predecessor-tex", type=Path, required=True)
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


def identity(path: Path) -> tuple[int, str]:
    return path.stat().st_size, sha256(path)


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


def scan_bytes(
    name: str, data: bytes, hits: list[dict[str, str]]
) -> None:
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


def pdf_metrics(path: Path) -> dict[str, int]:
    reader = PdfReader(path)
    goto = 0
    invalid = 0
    uri = 0
    linked_pages = 0
    text_pages = 0
    font_objects: set[tuple[int, int] | str] = set()
    type3_objects: set[tuple[int, int] | str] = set()
    raster_objects: set[tuple[int, int] | str] = set()
    for page in reader.pages:
        if (page.extract_text() or "").strip():
            text_pages += 1
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
                type3_objects.add(key)
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
        "text_pages": text_pages,
        "named_destinations": len(reader.named_destinations),
        "internal_goto_actions": goto,
        "linked_pages": linked_pages,
        "invalid_actions": invalid,
        "uri_actions": uri,
        "font_resources": len(font_objects),
        "type3_fonts": len(type3_objects),
        "raster_xobjects": len(raster_objects),
    }


def reader_process_hits(path: Path) -> list[dict[str, object]]:
    reader = PdfReader(path)
    hits: list[dict[str, object]] = []
    for page_number, page in enumerate(reader.pages, 1):
        text = " ".join((page.extract_text() or "").split())
        for pattern in PROCESS_PATTERNS:
            if re.search(pattern, text, flags=re.IGNORECASE):
                hits.append({"page": page_number, "pattern": pattern})
    return hits


def path_member(
    path: Path,
    integration_root: Path,
    overlay_root: Path,
    master: Path,
) -> str | None:
    if path == master:
        return BUNDLE_MASTER_NAME
    try:
        return path.relative_to(overlay_root).as_posix()
    except ValueError:
        pass
    try:
        return path.relative_to(integration_root).as_posix()
    except ValueError:
        return None


def recorder_closure(
    integration_root: Path,
    overlay_root: Path,
    recorder: Path,
    master: Path,
) -> dict[str, bytes]:
    members: dict[str, bytes] = {}
    for line in recorder.read_text(
        encoding="utf-8", errors="replace"
    ).splitlines():
        if not line.startswith("INPUT "):
            continue
        raw = Path(line[6:])
        source = (
            raw.resolve()
            if raw.is_absolute()
            else (recorder.parent / raw).resolve()
        )
        if (
            not source.is_file()
            or source.suffix.lower() not in ALLOWED_SOURCE_SUFFIXES
        ):
            continue
        name = path_member(source, integration_root, overlay_root, master)
        if name is None:
            continue
        if not safe_member(name):
            raise ValueError(f"unsafe source member: {name}")
        data = source.read_bytes()
        if name in members and members[name] != data:
            raise ValueError(f"conflicting source member: {name}")
        members[name] = data
    return members


def member_aggregate(members: dict[str, bytes]) -> str:
    digest = hashlib.sha256()
    for name, data in sorted(
        members.items(), key=lambda item: item[0].casefold()
    ):
        digest.update(
            f"{name}\t{len(data)}\t{sha256_bytes(data)}\n".encode("utf-8")
        )
    return digest.hexdigest().upper()


def role_for(name: str) -> str:
    if name.startswith("predecessor_public_reader/"):
        return "superseded_public_reader_preserved_as_history"
    if name.startswith("release/"):
        return "release_metadata"
    suffix = PurePosixPath(name).suffix.lower()
    if suffix == ".tex":
        return "editable_source"
    if suffix == ".png":
        return "current_diagram_dependency_not_diagram_final"
    if suffix == ".json":
        return "machine_validation"
    if suffix == ".csv":
        return "machine_manifest"
    return "build_dependency"


def copy_if_needed(source: Path, target: Path) -> None:
    if source.resolve() != target.resolve():
        shutil.copyfile(source, target)


def main() -> int:
    args = parse_args()
    integration = args.integration_root.resolve()
    overlay = args.overlay_root.resolve()
    recorder = args.recorder_file.resolve()
    reader = args.reader_pdf.resolve()
    master = args.master_tex.resolve()
    predecessor_pdf = args.predecessor_pdf.resolve()
    predecessor_tex = args.predecessor_tex.resolve()
    output = args.output_dir.resolve()
    output.mkdir(parents=True, exist_ok=True)
    errors: list[str] = []

    required = (
        integration,
        overlay,
        recorder,
        reader,
        master,
        predecessor_pdf,
        predecessor_tex,
    )
    for path in required:
        if not path.exists():
            errors.append(f"missing input: {path.name}")
    if errors:
        raise SystemExit("\n".join(errors))

    pdf_path = output / PDF_NAME
    tex_path = output / TEX_NAME
    copy_if_needed(reader, pdf_path)
    copy_if_needed(master, tex_path)

    if identity(pdf_path) != EXPECTED_PDF:
        errors.append("reader PDF identity mismatch")
    if identity(tex_path) != EXPECTED_MASTER:
        errors.append("master TeX identity mismatch")
    if identity(predecessor_pdf) != EXPECTED_PREDECESSOR_PDF:
        errors.append("predecessor PDF identity mismatch")
    if identity(predecessor_tex) != EXPECTED_PREDECESSOR_TEX:
        errors.append("predecessor TeX identity mismatch")

    metrics = pdf_metrics(pdf_path)
    for field, expected in EXPECTED_PDF_METRICS.items():
        if metrics[field] != expected:
            errors.append(
                f"PDF metric {field}={metrics[field]} expected {expected}"
            )
    process_hits = reader_process_hits(pdf_path)
    if process_hits:
        errors.append(f"reader process-term hits: {process_hits[:20]}")

    closure = recorder_closure(integration, overlay, recorder, master)
    closure_bytes = sum(len(data) for data in closure.values())
    closure_tex = sum(Path(name).suffix.lower() == ".tex" for name in closure)
    closure_png = sum(Path(name).suffix.lower() == ".png" for name in closure)
    closure_aggregate = member_aggregate(closure)
    expected_closure = (
        EXPECTED_CLOSURE_FILES,
        EXPECTED_CLOSURE_BYTES,
        EXPECTED_CLOSURE_TEX,
        EXPECTED_CLOSURE_PNG,
        EXPECTED_CLOSURE_AGGREGATE,
    )
    actual_closure = (
        len(closure),
        closure_bytes,
        closure_tex,
        closure_png,
        closure_aggregate,
    )
    if actual_closure != expected_closure:
        errors.append(
            f"recorder closure mismatch: {actual_closure} != "
            f"{expected_closure}"
        )

    privacy_hits: list[dict[str, str]] = []
    for name, data in closure.items():
        scan_bytes(name, data, privacy_hits)
    scan_bytes(PDF_NAME, pdf_path.read_bytes(), privacy_hits)
    scan_bytes(TEX_NAME, tex_path.read_bytes(), privacy_hits)

    members = dict(closure)
    for name in PUBLIC_DOCS:
        path = output / name
        if not path.is_file():
            errors.append(f"missing public document: {name}")
            continue
        data = path.read_bytes()
        members[f"release/{name}"] = data
        scan_bytes(name, data, privacy_hits)

    members[
        f"predecessor_public_reader/{PREDECESSOR_PDF_NAME}"
    ] = predecessor_pdf.read_bytes()
    members[
        f"predecessor_public_reader/{PREDECESSOR_TEX_NAME}"
    ] = predecessor_tex.read_bytes()

    if privacy_hits:
        errors.append(f"privacy hits: {privacy_hits[:20]}")

    source_validation = {
        "schema": "sga3_complete_reader_native_update_r18_source_bundle_v1",
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "scope": (
            "Editorial Notice, Introduction, Exposes I-XXVI, "
            "Tome I subject index, Tome III guide, and terminal index"
        ),
        "claim": (
            "continuous English reader; not a critical edition, "
            "rights clearance, or final diagram certification"
        ),
        "recorder_closure": {
            "files": len(closure),
            "bytes": closure_bytes,
            "tex_files": closure_tex,
            "png_files": closure_png,
            "ordered_aggregate_sha256": closure_aggregate,
        },
        "reader": {
            "filename": PDF_NAME,
            "bytes": pdf_path.stat().st_size,
            "sha256": sha256(pdf_path),
            **metrics,
            "reader_process_term_hits": process_hits,
        },
        "predecessor_reader": {
            "pdf": {
                "filename": PREDECESSOR_PDF_NAME,
                "bytes": predecessor_pdf.stat().st_size,
                "sha256": sha256(predecessor_pdf),
            },
            "tex": {
                "filename": PREDECESSOR_TEX_NAME,
                "bytes": predecessor_tex.stat().st_size,
                "sha256": sha256(predecessor_tex),
            },
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
        for name, data in sorted(
            members.items(), key=lambda item: item[0].casefold()
        )
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
        for name, data in sorted(
            members.items(), key=lambda item: item[0].casefold()
        ):
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

    package_validation = {
        "schema": "sga3_complete_reader_native_update_r18_outer_package_v1",
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "reader": {
            "filename": PDF_NAME,
            "bytes": pdf_path.stat().st_size,
            "sha256": sha256(pdf_path),
            **metrics,
            "reader_process_term_hits": process_hits,
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
            "contains_predecessor_reader": True,
        },
        "visual_qa": {
            "pages_reviewed": list(range(18, 68)),
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
        (output / name for name in outer_names if (output / name).is_file()),
        key=lambda path: path.name.casefold(),
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
