#!/usr/bin/env python3
"""Build the compact SGA3 current-progress package through Expose XXII."""

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
    "00c_SGA3_English_CurrentProgress_Cumulative_Through_XXII_"
    "Snapshot_20260728.pdf"
)
TEX_NAME = (
    "02c_SGA3_English_CurrentProgress_Cumulative_Through_XXII_"
    "Snapshot_20260728.tex"
)
SOURCE_ZIP_NAME = (
    "10c8_SGA3_CurrentProgress_Source_History_Through_XXII_"
    "Snapshot_20260728.zip"
)
MASTER_NAME = (
    "SGA3_English_Current_Progress_Cumulative_Through_XXII_Snapshot.tex"
)
EXPECTED_PDF_SHA256 = (
    "E401297F71F030C8EBD26F321B7F91B03799A628462A06EFF9DC4C5ADB47E739"
)
EXPECTED_PAGES = 1100
EXPECTED_DESTINATIONS = 6805
EXPECTED_GOTO_ACTIONS = 3917
FIXED_ZIP_TIME = (2026, 7, 28, 0, 0, 0)
PUBLIC_DOCS = (
    "README.md",
    "PUBLICATION_READINESS.md",
    "BUILD_SUMMARY_PUBLIC.md",
    "FINAL_VISUAL_QA.md",
)
TEXT_SUFFIXES = {
    ".bib",
    ".cls",
    ".csv",
    ".json",
    ".jsonl",
    ".md",
    ".sty",
    ".tex",
    ".txt",
}
PRIVATE_MARKERS = (
    "c:\\users\\",
    "c:/users/",
    "\\appdata\\",
    "/appdata/",
    "chatnotes",
    ".claude",
    "source_thread_id",
    "thread_id",
    "@gmail.",
    "@outlook.",
)
EXCLUDED_SUFFIXES = {
    ".aux",
    ".console.txt",
    ".log",
    ".out",
    ".toc",
}
EXCLUDED_FILENAMES = {
    "INDEPENDENT_SOURCE_ARCHIVE_REBUILD_PASS.md",
    "STATUS.md",
    "authority-page34.png",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--integration-root", type=Path, required=True)
    parser.add_argument("--predecessor-package-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--independent-receipt", type=Path)
    return parser.parse_args()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def safe_member(name: str) -> bool:
    parts = PurePosixPath(name).parts
    return (
        bool(name)
        and not name.startswith(("/", "\\"))
        and re.match(r"^[A-Za-z]:", name) is None
        and ".." not in parts
    )


def csv_bytes(rows: list[dict[str, object]], fields: list[str]) -> bytes:
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue().encode("utf-8")


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
    if suffix == ".pdf":
        return "bounded_predecessor_or_component_reader"
    if suffix == ".png":
        return "required_diagram_or_source_crop"
    if suffix in {".csv", ".json", ".jsonl"}:
        return "machine_control"
    if suffix == ".md":
        return "scope_provenance_or_readiness"
    return "supporting_source_dependency"


def excluded(relative: str) -> bool:
    path = PurePosixPath(relative)
    parts_lower = tuple(part.lower() for part in path.parts)
    name = path.name
    lower = relative.lower()
    if parts_lower and parts_lower[0] in {"build", "qa"}:
        return True
    if "qa" in parts_lower and "renders" in parts_lower:
        return True
    if "upstream_controls" in parts_lower and "reader" in parts_lower:
        return True
    if name in EXCLUDED_FILENAMES:
        return True
    if any(lower.endswith(suffix) for suffix in EXCLUDED_SUFFIXES):
        return True
    return False


def pdf_metrics(path: Path) -> dict[str, int]:
    reader = PdfReader(path)
    goto = 0
    invalid = 0
    uri = 0
    font_objects: set[tuple[int, int] | str] = set()
    type3 = 0
    linked_pages = 0
    for page in reader.pages:
        page_links = 0
        annotations = page.get("/Annots") or []
        for annotation_ref in annotations:
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
            if hasattr(font_ref, "idnum"):
                key: tuple[int, int] | str = (
                    int(font_ref.idnum),
                    int(font_ref.generation),
                )
            else:
                key = repr(font_ref)
            font_objects.add(key)
            font = font_ref.get_object()
            if font.get("/Subtype") == "/Type3":
                type3 += 1
    return {
        "pages": len(reader.pages),
        "named_destinations": len(reader.named_destinations),
        "internal_goto_actions": goto,
        "linked_pages": linked_pages,
        "invalid_actions": invalid,
        "uri_actions": uri,
        "font_resources": len(font_objects),
        "type3_fonts": type3,
    }


def add_member(
    members: dict[str, bytes],
    name: str,
    data: bytes,
    errors: list[str],
) -> None:
    normalized = PurePosixPath(name).as_posix()
    if not safe_member(normalized):
        errors.append(f"unsafe source member: {normalized}")
    elif normalized in members:
        errors.append(f"duplicate source member: {normalized}")
    else:
        members[normalized] = data


def scan_text(
    name: str,
    data: bytes,
    hits: list[dict[str, str]],
) -> None:
    text = data.decode("utf-8", errors="replace").lower()
    for marker in PRIVATE_MARKERS:
        if marker in text:
            hits.append({"path": name, "marker": marker})


def scan_pdf(
    name: str,
    data: bytes,
    hits: list[dict[str, str]],
) -> None:
    raw = data.decode("latin-1", errors="ignore").lower()
    for marker in PRIVATE_MARKERS:
        if marker in raw:
            hits.append({"path": name, "marker": marker, "surface": "raw"})
    try:
        reader = PdfReader(io.BytesIO(data))
        metadata = " ".join(str(value) for value in (reader.metadata or {}).values())
        extracted = "\n".join(page.extract_text() or "" for page in reader.pages)
        text = (metadata + "\n" + extracted).lower()
        for marker in PRIVATE_MARKERS:
            if marker in text:
                hits.append(
                    {"path": name, "marker": marker, "surface": "metadata_or_text"}
                )
    except Exception as exc:  # pragma: no cover - recorded as a gate failure
        hits.append({"path": name, "marker": f"pdf_parse_error:{exc}"})


def main() -> int:
    args = parse_args()
    root = args.integration_root.resolve()
    predecessor = args.predecessor_package_dir.resolve()
    output = args.output_dir.resolve()
    output.mkdir(parents=True, exist_ok=True)
    errors: list[str] = []

    master = root / MASTER_NAME
    reader = root / "build" / f"{master.stem}.pdf"
    for path in (root, predecessor, master, reader):
        if not path.exists():
            errors.append(f"missing input: {path}")
    if errors:
        raise SystemExit("\n".join(errors))

    pdf_path = output / PDF_NAME
    tex_path = output / TEX_NAME
    shutil.copyfile(reader, pdf_path)
    shutil.copyfile(master, tex_path)
    for name in PUBLIC_DOCS:
        shutil.copyfile(root / name, output / name)
    if args.independent_receipt:
        shutil.copyfile(
            args.independent_receipt,
            output / "INDEPENDENT_SOURCE_ARCHIVE_REBUILD_PASS.md",
        )

    if sha256(pdf_path) != EXPECTED_PDF_SHA256:
        errors.append("reader PDF identity mismatch")
    metrics = pdf_metrics(pdf_path)
    for field, expected in (
        ("pages", EXPECTED_PAGES),
        ("named_destinations", EXPECTED_DESTINATIONS),
        ("internal_goto_actions", EXPECTED_GOTO_ACTIONS),
        ("invalid_actions", 0),
        ("uri_actions", 0),
        ("type3_fonts", 0),
    ):
        if metrics[field] != expected:
            errors.append(
                f"PDF metric {field}={metrics[field]} expected {expected}"
            )

    members: dict[str, bytes] = {}
    for source in sorted(root.rglob("*")):
        if not source.is_file():
            continue
        relative = source.relative_to(root).as_posix()
        if excluded(relative):
            continue
        add_member(members, relative, source.read_bytes(), errors)

    predecessor_files = {
        "predecessor/cumulative-through-xviii/"
        "00c_SGA3_English_CurrentProgress_Cumulative_Through_XVIII_20260728.pdf":
            predecessor
            / "00c_SGA3_English_CurrentProgress_Cumulative_Through_XVIII_20260728.pdf",
        "predecessor/cumulative-through-xviii/"
        "02c_SGA3_English_CurrentProgress_Cumulative_Through_XVIII_20260728.tex":
            predecessor
            / "02c_SGA3_English_CurrentProgress_Cumulative_Through_XVIII_20260728.tex",
        "predecessor/cumulative-through-xviii/README.md":
            predecessor / "README.md",
    }
    for name, source in predecessor_files.items():
        if not source.is_file():
            errors.append(f"missing predecessor file: {source.name}")
            continue
        add_member(members, name, source.read_bytes(), errors)

    privacy_hits: list[dict[str, str]] = []
    for name, data in members.items():
        suffix = PurePosixPath(name).suffix.lower()
        if suffix in TEXT_SUFFIXES:
            scan_text(name, data, privacy_hits)
        elif suffix == ".pdf":
            scan_pdf(name, data, privacy_hits)
    scan_pdf(PDF_NAME, pdf_path.read_bytes(), privacy_hits)
    if privacy_hits:
        errors.append(f"privacy hits: {privacy_hits[:20]}")

    premanifest_rows = [
        {
            "relative_path": name,
            "bytes": len(data),
            "sha256": sha256_bytes(data),
            "role": role_for(name),
        }
        for name, data in sorted(members.items(), key=lambda item: item[0].lower())
    ]
    source_validation = {
        "schema": "sga3_current_progress_source_history_through_xxii_v1",
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "scope": {
            "complete": (
                "Editorial Notice, Introduction, Exposes I-XVI, and Expose XVIII"
            ),
            "partial": "Exposes XVII, XX, and XXII",
            "gaps": "Exposes XIX, XXI, and XXIII-XXVI",
            "claim": "working current-progress reader, not complete SGA3",
        },
        "reader": {
            "filename": PDF_NAME,
            "bytes": pdf_path.stat().st_size,
            "sha256": sha256(pdf_path),
            **metrics,
        },
        "source_selection": {
            "pre_manifest_members": len(premanifest_rows),
            "pdf_page_render_qa_included": 0,
            "authority_pdf_pages_included": 0,
            "required_diagram_and_source_crop_assets_retained": True,
            "predecessor_cumulative_pdf_tex_readme_retained": True,
        },
        "privacy": {"hits": privacy_hits},
    }
    validation_data = (
        json.dumps(source_validation, indent=2, ensure_ascii=True) + "\n"
    ).encode("utf-8")
    add_member(
        members,
        "SOURCE_BUNDLE_VALIDATION.json",
        validation_data,
        errors,
    )
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
    add_member(members, "SOURCE_BUNDLE_SHA256.csv", manifest_data, errors)

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

    package_validation = {
        "schema": "sga3_current_progress_outer_package_through_xxii_v1",
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
        "privacy": {"hits": privacy_hits},
        "visual_qa_pages": [
            1,
            9,
            11,
            772,
            962,
            963,
            1024,
            1025,
            1049,
            1057,
            1058,
            1078,
            1079,
            1080,
            1086,
            1087,
            1088,
            1097,
            1098,
            1099,
            1100,
        ],
        "independent_source_archive_rebuild_receipt_included": bool(
            args.independent_receipt
        ),
    }
    validation_path = output / "PACKAGE_VALIDATION.json"
    validation_path.write_text(
        json.dumps(package_validation, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )

    allowed_names = {
        PDF_NAME,
        TEX_NAME,
        SOURCE_ZIP_NAME,
        "build_package.py",
        "PACKAGE_VALIDATION.json",
        *PUBLIC_DOCS,
    }
    if args.independent_receipt:
        allowed_names.add("INDEPENDENT_SOURCE_ARCHIVE_REBUILD_PASS.md")
    stale = [
        path.name
        for path in output.iterdir()
        if path.is_file()
        and path.name not in allowed_names
        and path.name != "SHA256SUMS.csv"
    ]
    if stale:
        errors.append(f"unexpected outer files: {stale}")

    outer_paths = sorted(
        (
            output / name
            for name in allowed_names
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
