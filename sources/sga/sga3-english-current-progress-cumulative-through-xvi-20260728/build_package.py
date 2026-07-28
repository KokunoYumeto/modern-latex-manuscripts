#!/usr/bin/env python3
"""Build and verify the compact SGA3 cumulative-through-XVI package."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
import zipfile
from pathlib import Path, PurePosixPath

from pypdf import PdfReader


PDF_NAME = "00c_SGA3_English_CurrentProgress_Cumulative_Through_XVI_20260728.pdf"
TEX_NAME = "02c_SGA3_English_CurrentProgress_Cumulative_Through_XVI_20260728.tex"
SOURCE_ZIP_NAME = (
    "10c8_SGA3_CurrentProgress_Integration_Source_Through_XVI_20260728.zip"
)
SOURCE_MASTER_NAME = "SGA3_English_Current_Progress_Cumulative_Through_XVI.tex"
EXPECTED_PDF_SHA256 = (
    "8D1DC78CDE64F22B76AD89150BEE73C48A1934EAECE0738B50AA413670CDDEAA"
)
EXPECTED_PAGES = 950
EXPECTED_DESTINATIONS = 5923
EXPECTED_GOTO_ACTIONS = 3792
FIXED_ZIP_TIME = (2026, 7, 28, 0, 0, 0)
REPLACED_SOURCE_MEMBERS = {
    "BUILD_SUMMARY_PUBLIC.md",
    "PUBLICATION_READINESS.md",
    "README.md",
    "SGA3_English_Current_Progress_Cumulative.tex",
    "SOURCE_BUNDLE_SHA256.csv",
    "SOURCE_BUNDLE_VALIDATION.json",
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
TEXT_SUFFIXES = {".csv", ".json", ".md", ".tex", ".txt"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prior-source-zip", type=Path, required=True)
    parser.add_argument("--master-tex", type=Path, required=True)
    parser.add_argument("--reader-pdf", type=Path, required=True)
    parser.add_argument("--xii-root", type=Path, required=True)
    parser.add_argument("--xvi-root", type=Path, required=True)
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


def safe_member(name: str) -> bool:
    parts = PurePosixPath(name).parts
    return (
        bool(name)
        and not name.startswith(("/", "\\"))
        and re.match(r"^[A-Za-z]:", name) is None
        and ".." not in parts
    )


def role_for(name: str) -> str:
    suffix = PurePosixPath(name).suffix.lower()
    if suffix == ".tex":
        return "editable_source"
    if suffix == ".png":
        return "required_diagram_asset"
    if suffix in {".csv", ".json", ".jsonl"}:
        return "machine_control"
    if suffix == ".md":
        return "scope_or_readiness_documentation"
    return "supporting_source_dependency"


def csv_bytes(rows: list[dict[str, object]], fields: list[str]) -> bytes:
    import io

    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue().encode("utf-8")


def add_tree(
    members: dict[str, bytes],
    root: Path,
    relative_root: str,
    pattern: str,
) -> None:
    for source in sorted(root.glob(pattern)):
        if not source.is_file():
            continue
        relative = source.relative_to(root).as_posix()
        members[f"{relative_root}/{relative}"] = source.read_bytes()


def zip_info(name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, date_time=FIXED_ZIP_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.create_system = 3
    info.external_attr = 0o100644 << 16
    return info


def pdf_metrics(path: Path) -> dict[str, int]:
    reader = PdfReader(path)
    goto = 0
    invalid = 0
    font_objects: set[tuple[int, int] | str] = set()
    type3 = 0
    for page in reader.pages:
        annotations = page.get("/Annots") or []
        for annotation_ref in annotations:
            annotation = annotation_ref.get_object()
            action = annotation.get("/A")
            destination = annotation.get("/Dest")
            if action and action.get("/S") == "/GoTo":
                goto += 1
                if action.get("/D") is None:
                    invalid += 1
            elif destination is not None:
                goto += 1
            elif action is not None:
                invalid += 1
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
        "invalid_actions": invalid,
        "font_resources": len(font_objects),
        "type3_fonts": type3,
    }


def main() -> int:
    args = parse_args()
    output = args.output_dir.resolve()
    output.mkdir(parents=True, exist_ok=True)
    errors: list[str] = []

    for path in (
        args.prior_source_zip,
        args.master_tex,
        args.reader_pdf,
        args.xii_root,
        args.xvi_root,
    ):
        if not path.exists():
            errors.append(f"missing input: {path.name}")
    if errors:
        raise SystemExit("\n".join(errors))

    pdf_path = output / PDF_NAME
    tex_path = output / TEX_NAME
    shutil.copyfile(args.reader_pdf, pdf_path)
    shutil.copyfile(args.master_tex, tex_path)
    if sha256(pdf_path) != EXPECTED_PDF_SHA256:
        errors.append("reader PDF identity mismatch")

    metrics = pdf_metrics(pdf_path)
    for field, expected in (
        ("pages", EXPECTED_PAGES),
        ("named_destinations", EXPECTED_DESTINATIONS),
        ("internal_goto_actions", EXPECTED_GOTO_ACTIONS),
        ("invalid_actions", 0),
        ("type3_fonts", 0),
    ):
        if metrics[field] != expected:
            errors.append(
                f"PDF metric {field}={metrics[field]} expected {expected}"
            )

    members: dict[str, bytes] = {}
    with zipfile.ZipFile(args.prior_source_zip) as archive:
        bad = archive.testzip()
        if bad:
            errors.append(f"prior source ZIP CRC failure: {bad}")
        for info in archive.infolist():
            name = info.filename
            if name in REPLACED_SOURCE_MEMBERS:
                continue
            if not safe_member(name):
                errors.append(f"unsafe inherited member: {name}")
                continue
            if name in members:
                errors.append(f"duplicate inherited member: {name}")
                continue
            members[name] = archive.read(name)

    members[SOURCE_MASTER_NAME] = args.master_tex.read_bytes()
    add_tree(
        members,
        args.xii_root / "tex" / "components",
        "xii/tex/components",
        "*.tex",
    )
    add_tree(
        members,
        args.xvi_root / "tex" / "components",
        "xvi/tex/components",
        "*.tex",
    )
    add_tree(members, args.xvi_root / "figures", "xvi/figures", "*.png")
    for name in (
        "README.md",
        "PUBLICATION_READINESS.md",
        "BUILD_SUMMARY_PUBLIC.md",
    ):
        members[name] = (output / name).read_bytes()

    validation = {
        "schema": "sga3_current_progress_source_bundle_through_xvi_v1",
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "scope": {
            "included": "Editorial Notice, Introduction, Exposes I-XIII and XVI",
            "absent": "Exposes XIV-XV and XVII-XXVI",
            "claim": "working current-progress reader, not complete SGA3",
        },
        "reader": {
            "filename": PDF_NAME,
            "bytes": pdf_path.stat().st_size,
            "sha256": sha256(pdf_path),
            **metrics,
        },
        "additive_sources": {
            "expose_xii_component_tex": len(
                list((args.xii_root / "tex" / "components").glob("*.tex"))
            ),
            "expose_xvi_component_tex": len(
                list((args.xvi_root / "tex" / "components").glob("*.tex"))
            ),
            "expose_xvi_raster_placeholders": len(
                list((args.xvi_root / "figures").glob("*.png"))
            ),
        },
        "authority_exclusions": {
            "source_pdfs_included": 0,
            "ocr_corpora_included": 0,
        },
    }
    members["SOURCE_BUNDLE_VALIDATION.json"] = (
        json.dumps(validation, indent=2, ensure_ascii=True) + "\n"
    ).encode("utf-8")

    manifest_rows = [
        {
            "relative_path": name,
            "bytes": len(data),
            "sha256": sha256_bytes(data),
            "role": role_for(name),
        }
        for name, data in sorted(members.items(), key=lambda item: item[0].lower())
    ]
    members["SOURCE_BUNDLE_SHA256.csv"] = csv_bytes(
        manifest_rows,
        ["relative_path", "bytes", "sha256", "role"],
    )

    privacy_hits: list[dict[str, str]] = []
    for name, data in members.items():
        if PurePosixPath(name).suffix.lower() not in TEXT_SUFFIXES:
            continue
        text = data.decode("utf-8", errors="replace").lower()
        for marker in PRIVATE_MARKERS:
            if marker in text:
                privacy_hits.append({"path": name, "marker": marker})
    if privacy_hits:
        errors.append(f"source bundle privacy hits: {privacy_hits[:20]}")

    source_zip = output / SOURCE_ZIP_NAME
    with zipfile.ZipFile(
        source_zip,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
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
            zip_errors.append("duplicate member")
        if set(names) != set(members):
            zip_errors.append("exact member set mismatch")
        for name in names:
            data = archive.read(name)
            if data != members[name]:
                zip_errors.append(f"member identity mismatch: {name}")
    errors.extend(zip_errors)

    validation.update(
        {
            "status": "PASS" if not errors else "FAIL",
            "errors": errors,
            "source_archive": {
                "filename": SOURCE_ZIP_NAME,
                "bytes": source_zip.stat().st_size,
                "sha256": sha256(source_zip),
                "members": len(members),
                "uncompressed_bytes": sum(len(data) for data in members.values()),
                "crc_errors": len(zip_errors),
                "manifest_rows": len(manifest_rows),
            },
            "privacy": {"hits": privacy_hits},
            "visual_qa_pages": [
                846,
                847,
                848,
                894,
                895,
                896,
                924,
                925,
                926,
                927,
                937,
                939,
                949,
                950,
            ],
        }
    )
    validation_path = output / "PACKAGE_VALIDATION.json"
    validation_path.write_text(
        json.dumps(validation, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )

    outer_paths = sorted(
        (
            path
            for path in output.iterdir()
            if path.is_file() and path.name != "SHA256SUMS.csv"
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

    for row in outer_rows:
        path = output / str(row["filename"])
        if (
            path.stat().st_size != int(row["bytes"])
            or sha256(path) != row["sha256"]
        ):
            errors.append(f"outer identity mismatch: {path.name}")

    result = {
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
        "source_archive": validation["source_archive"],
        "outer_manifest_rows": len(outer_rows),
        "outer_manifest_sha256": sha256(sums_path),
    }
    print(json.dumps(result, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
