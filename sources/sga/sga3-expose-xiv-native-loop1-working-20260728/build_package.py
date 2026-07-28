#!/usr/bin/env python3
"""Build and validate the compact SGA3 Expose XIV working package."""

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
    "00c14_SGA3_Expose_XIV_English_"
    "NativeDiagram_Loop1_Working_20260728.pdf"
)
TEX_NAME = (
    "02c14_SGA3_Expose_XIV_English_"
    "NativeDiagram_Loop1_Working_20260728.tex"
)
ZIP_NAME = (
    "10c14_SGA3_Expose_XIV_"
    "NativeDiagram_Loop1_Source_20260728.zip"
)
EXPECTED_PRODUCER_PDF = (
    240_676,
    "6CD0B985FE2F4D0C69A52ACCD0E766F3029B3E8E6A40AEB31B9E511C40E72EA0",
)
EXPECTED_REBUILD_PDF = (
    240_682,
    "100F3D63F8C606E55A79B916096B69EAF5A02067C67CE82B9AC578934DD47CFA",
)
EXPECTED_LEAD_RECEIPT = (
    4_065,
    "D932026811FF0DA5E9C1C6FEEBF3CCFE785699DE24D5AD712071585AC59045F6",
)
EXPECTED_TEX_COUNT = 33
EXPECTED_TEX_AGGREGATE = (
    4_343,
    "DCA2048F665EF3D36A25EFACEA97AADF39B30D13F3DB43580782DBDDDBEBE00F",
)
EXPECTED_METRICS = {
    "pages": 37,
    "named_destinations": 236,
    "internal_goto_actions": 24,
    "linked_pages": 11,
    "invalid_actions": 0,
    "uri_actions": 0,
    "font_resources": 32,
    "type3_fonts": 0,
    "raster_xobjects": 0,
}
PUBLIC_DOCS = (
    "README.md",
    "PROVENANCE_AND_RIGHTS.md",
    "PUBLICATION_READINESS.md",
    "BUILD_SUMMARY_PUBLIC.md",
    "FINAL_VISUAL_QA.md",
    "INDEPENDENT_ARCHIVE_REBUILD_PASS.md",
)
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
FIXED_ZIP_TIME = (2026, 7, 28, 0, 0, 0)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--producer-root", type=Path, required=True)
    parser.add_argument("--rebuild-pdf", type=Path, required=True)
    parser.add_argument("--producer-render-dir", type=Path, required=True)
    parser.add_argument("--rebuild-render-dir", type=Path, required=True)
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


def zip_info(name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, date_time=FIXED_ZIP_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.create_system = 3
    info.external_attr = 0o100644 << 16
    return info


def safe_member(name: str) -> bool:
    path = PurePosixPath(name)
    return (
        bool(name)
        and not path.is_absolute()
        and ".." not in path.parts
        and "\\" not in name
        and re.match(r"^[A-Za-z]:", name) is None
    )


def tex_identity_rows(producer: Path) -> list[dict[str, object]]:
    rows = []
    for path in sorted((producer / "tex").rglob("*.tex")):
        rows.append(
            {
                "relative_path": path.relative_to(producer).as_posix(),
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
        )
    return rows


def tex_aggregate(rows: list[dict[str, object]]) -> tuple[int, str]:
    data = "".join(
        f"{row['relative_path']}\t{row['bytes']}\t{row['sha256']}\n"
        for row in rows
    ).encode("utf-8")
    return len(data), sha256_bytes(data)


def pdf_metrics(path: Path) -> dict[str, int]:
    reader = PdfReader(path)
    goto = invalid = uri = linked_pages = type3 = raster_xobjects = 0
    fonts: set[tuple[int | None, int | None]] = set()
    for page in reader.pages:
        page_links = 0
        for annotation_ref in page.get("/Annots") or []:
            annotation = annotation_ref.get_object()
            action = annotation.get("/A")
            destination = annotation.get("/Dest")
            if action and action.get("/S") == "/GoTo":
                goto += 1
                page_links += 1
                invalid += action.get("/D") is None
            elif destination is not None:
                goto += 1
                page_links += 1
            elif action and action.get("/S") == "/URI":
                uri += 1
            elif action is not None:
                invalid += 1
        linked_pages += bool(page_links)
        resources = page.get("/Resources") or {}
        page_fonts = resources.get("/Font") or {}
        if hasattr(page_fonts, "get_object"):
            page_fonts = page_fonts.get_object()
        for font_ref in page_fonts.values():
            fonts.add(
                (
                    getattr(font_ref, "idnum", None),
                    getattr(font_ref, "generation", None),
                )
            )
            if font_ref.get_object().get("/Subtype") == "/Type3":
                type3 += 1
        xobjects = resources.get("/XObject") or {}
        if hasattr(xobjects, "get_object"):
            xobjects = xobjects.get_object()
        for xobject_ref in xobjects.values():
            if xobject_ref.get_object().get("/Subtype") == "/Image":
                raster_xobjects += 1
    return {
        "pages": len(reader.pages),
        "named_destinations": len(reader.named_destinations),
        "internal_goto_actions": goto,
        "linked_pages": linked_pages,
        "invalid_actions": invalid,
        "uri_actions": uri,
        "font_resources": len(fonts),
        "type3_fonts": type3,
        "raster_xobjects": raster_xobjects,
    }


def compare_pdfs(producer: Path, rebuild: Path) -> dict[str, object]:
    first = PdfReader(producer)
    second = PdfReader(rebuild)
    text_mismatch = []
    content_mismatch = []
    geometry_mismatch = []
    for page_number, (left, right) in enumerate(
        zip(first.pages, second.pages), start=1
    ):
        if (left.extract_text() or "") != (right.extract_text() or ""):
            text_mismatch.append(page_number)
        left_data = (
            left.get_contents().get_data() if left.get_contents() else b""
        )
        right_data = (
            right.get_contents().get_data() if right.get_contents() else b""
        )
        if left_data != right_data:
            content_mismatch.append(page_number)
        if tuple(left.mediabox) != tuple(right.mediabox):
            geometry_mismatch.append(page_number)
    return {
        "producer_metrics": pdf_metrics(producer),
        "rebuild_metrics": pdf_metrics(rebuild),
        "text_mismatch_pages": text_mismatch,
        "content_stream_mismatch_pages": content_mismatch,
        "geometry_mismatch_pages": geometry_mismatch,
    }


def compare_render_dirs(first: Path, second: Path) -> dict[str, object]:
    left = sorted(path for path in first.iterdir() if path.is_file())
    right = sorted(path for path in second.iterdir() if path.is_file())
    mismatches = []
    if len(left) == len(right):
        for index, (left_path, right_path) in enumerate(
            zip(left, right), start=1
        ):
            if sha256(left_path) != sha256(right_path):
                mismatches.append(index)
    return {
        "dpi": 180,
        "producer_pages": len(left),
        "rebuild_pages": len(right),
        "pixel_or_byte_mismatch_pages": mismatches,
    }


def scan_text(name: str, data: bytes, hits: list[dict[str, str]]) -> None:
    text = data.decode("utf-8", errors="replace").lower()
    for marker in PRIVATE_MARKERS:
        if marker in text:
            hits.append({"path": name, "marker": marker})


def scan_pdf(name: str, data: bytes, hits: list[dict[str, str]]) -> None:
    raw = data.decode("latin-1", errors="ignore").lower()
    for marker in PRIVATE_MARKERS:
        if marker in raw:
            hits.append({"path": name, "marker": marker, "surface": "raw"})
    reader = PdfReader(io.BytesIO(data))
    text = "\n".join(page.extract_text() or "" for page in reader.pages)
    metadata = " ".join(str(value) for value in (reader.metadata or {}).values())
    combined = (metadata + "\n" + text).lower()
    for marker in PRIVATE_MARKERS:
        if marker in combined:
            hits.append(
                {
                    "path": name,
                    "marker": marker,
                    "surface": "metadata_or_text",
                }
            )


def main() -> int:
    args = parse_args()
    producer = args.producer_root.resolve()
    rebuild_pdf = args.rebuild_pdf.resolve()
    producer_render_dir = args.producer_render_dir.resolve()
    rebuild_render_dir = args.rebuild_render_dir.resolve()
    output = args.output_dir.resolve()
    output.mkdir(parents=True, exist_ok=True)
    errors: list[str] = []

    producer_pdf = (
        producer
        / "build_native_diagram_r1"
        / "SGA3_Expose_XIV_English.pdf"
    )
    producer_master = producer / "tex" / "SGA3_Expose_XIV_English.tex"
    lead_receipt = (
        producer
        / "qa"
        / "native_redo_20260728"
        / "LEAD_NATIVE_DIAGRAM_5000DPI_REVIEW_PASS.md"
    )
    for path in (
        producer_pdf,
        producer_master,
        lead_receipt,
        rebuild_pdf,
        producer_render_dir,
        rebuild_render_dir,
    ):
        if not path.exists():
            errors.append(f"missing required input: {path}")
    if errors:
        raise SystemExit("\n".join(errors))

    tex_rows = tex_identity_rows(producer)
    if len(tex_rows) != EXPECTED_TEX_COUNT:
        errors.append("TeX file count mismatch")
    if tex_aggregate(tex_rows) != EXPECTED_TEX_AGGREGATE:
        errors.append("TeX aggregate mismatch")
    if identity(producer_pdf) != EXPECTED_PRODUCER_PDF:
        errors.append("producer PDF identity mismatch")
    if identity(rebuild_pdf) != EXPECTED_REBUILD_PDF:
        errors.append("independent rebuild PDF identity mismatch")
    if identity(lead_receipt) != EXPECTED_LEAD_RECEIPT:
        errors.append("lead review receipt identity mismatch")

    tex_content = "\n".join(
        (producer / str(row["relative_path"])).read_text(
            encoding="utf-8", errors="strict"
        )
        for row in tex_rows
    )
    native_tikzcd = tex_content.count(r"\begin{tikzcd}")
    native_tikzpicture = tex_content.count(r"\begin{tikzpicture}")
    native_diagrams = native_tikzcd + native_tikzpicture
    if native_tikzcd != 0 or native_tikzpicture != 1:
        errors.append("native diagram environment count mismatch")
    if r"\includegraphics" in tex_content:
        errors.append("raster include found in TeX closure")

    comparison = compare_pdfs(producer_pdf, rebuild_pdf)
    if comparison["producer_metrics"] != EXPECTED_METRICS:
        errors.append("producer PDF metric mismatch")
    if comparison["rebuild_metrics"] != EXPECTED_METRICS:
        errors.append("rebuild PDF metric mismatch")
    for field in (
        "text_mismatch_pages",
        "content_stream_mismatch_pages",
        "geometry_mismatch_pages",
    ):
        if comparison[field]:
            errors.append(f"PDF comparison failure: {field}")

    render_comparison = compare_render_dirs(
        producer_render_dir, rebuild_render_dir
    )
    if (
        render_comparison["producer_pages"] != 37
        or render_comparison["rebuild_pages"] != 37
        or render_comparison["pixel_or_byte_mismatch_pages"]
    ):
        errors.append("render comparison failure")

    shutil.copyfile(producer_pdf, output / PDF_NAME)
    shutil.copyfile(producer_master, output / TEX_NAME)
    shutil.copyfile(
        lead_receipt,
        output / "LEAD_NATIVE_DIAGRAM_5000DPI_REVIEW_PASS.md",
    )

    source_members: dict[str, bytes] = {}
    for row in tex_rows:
        relative = str(row["relative_path"])
        source_members[relative] = (producer / relative).read_bytes()
    for name in PUBLIC_DOCS:
        source_members[name] = (output / name).read_bytes()
    source_members["LEAD_NATIVE_DIAGRAM_5000DPI_REVIEW_PASS.md"] = (
        output / "LEAD_NATIVE_DIAGRAM_5000DPI_REVIEW_PASS.md"
    ).read_bytes()

    source_rows = [
        {
            "relative_path": name,
            "bytes": len(data),
            "sha256": sha256_bytes(data),
        }
        for name, data in sorted(source_members.items())
    ]
    source_manifest = csv_bytes(
        source_rows, ["relative_path", "bytes", "sha256"]
    )
    source_members["SOURCE_SHA256SUMS.csv"] = source_manifest
    source_validation = {
        "schema": "sga3_expose_xiv_native_loop1_source_v1",
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "scope": {
            "complete": "SGA3 Expose XIV only",
            "authority_pages": "local 1-36 / combined 835-870",
            "next_cursor": "Expose XV local 1 / combined 871",
        },
        "editable_tex_files": len(tex_rows),
        "native_tikzcd_diagrams": native_diagrams,
        "replacement_diagram_rows_reviewed_at_5000dpi": 4,
        "raster_includes": 0,
        "authority_images_included": 0,
        "source_manifest_rows": len(source_rows),
        "source_manifest_sha256": sha256_bytes(source_manifest),
        "pdf_comparison": comparison,
        "render_comparison": render_comparison,
    }
    source_members["SOURCE_PACKAGE_VALIDATION.json"] = (
        json.dumps(source_validation, indent=2, ensure_ascii=True) + "\n"
    ).encode("utf-8")

    source_zip = output / ZIP_NAME
    with zipfile.ZipFile(
        source_zip,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
        allowZip64=True,
    ) as archive:
        for name, data in sorted(source_members.items()):
            if not safe_member(name):
                errors.append(f"unsafe ZIP member: {name}")
                continue
            archive.writestr(zip_info(name), data)

    zip_errors: list[str] = []
    with zipfile.ZipFile(source_zip) as archive:
        bad = archive.testzip()
        names = archive.namelist()
        if bad:
            zip_errors.append(f"CRC failure: {bad}")
        if len(names) != len(set(names)):
            zip_errors.append("duplicate ZIP member")
        if set(names) != set(source_members):
            zip_errors.append("ZIP exact-set mismatch")
        for name in names:
            if not safe_member(name):
                zip_errors.append(f"unsafe ZIP member: {name}")
            if archive.read(name) != source_members[name]:
                zip_errors.append(f"ZIP identity mismatch: {name}")
    errors.extend(zip_errors)

    privacy_hits: list[dict[str, str]] = []
    for path in output.iterdir():
        if not path.is_file():
            continue
        if path.suffix.lower() in {".md", ".tex", ".csv", ".json"}:
            scan_text(path.name, path.read_bytes(), privacy_hits)
        elif path.suffix.lower() == ".pdf":
            scan_pdf(path.name, path.read_bytes(), privacy_hits)
    for name, data in source_members.items():
        if PurePosixPath(name).suffix.lower() in {
            ".md",
            ".tex",
            ".csv",
            ".json",
        }:
            scan_text(f"{ZIP_NAME}:{name}", data, privacy_hits)
    if privacy_hits:
        errors.append(f"privacy hits: {privacy_hits}")

    package_validation = {
        "schema": "sga3_expose_xiv_native_loop1_outer_v1",
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "reader": {
            "filename": PDF_NAME,
            "bytes": (output / PDF_NAME).stat().st_size,
            "sha256": sha256(output / PDF_NAME),
            **EXPECTED_METRICS,
        },
        "direct_master_tex": {
            "filename": TEX_NAME,
            "bytes": (output / TEX_NAME).stat().st_size,
            "sha256": sha256(output / TEX_NAME),
        },
        "source_zip": {
            "filename": ZIP_NAME,
            "bytes": source_zip.stat().st_size,
            "sha256": sha256(source_zip),
            "members": len(source_members),
            "uncompressed_bytes": sum(
                len(data) for data in source_members.values()
            ),
            "errors": zip_errors,
        },
        "pdf_comparison": comparison,
        "render_equivalence": render_comparison,
        "visual_review": {
            "archive_pages_reviewed": [1, 18, 37],
            "replacement_diagram_rows_reviewed_at_5000dpi": 4,
            "observed_defects": 0,
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
        ZIP_NAME,
        "build_package.py",
        "PACKAGE_VALIDATION.json",
        "LEAD_NATIVE_DIAGRAM_5000DPI_REVIEW_PASS.md",
        *PUBLIC_DOCS,
    }
    actual_names = {
        path.name
        for path in output.iterdir()
        if path.is_file() and path.name != "SHA256SUMS.csv"
    }
    if actual_names != outer_names:
        errors.append(
            "outer exact-set mismatch: "
            f"missing={sorted(outer_names - actual_names)}, "
            f"extra={sorted(actual_names - outer_names)}"
        )

    outer_rows = [
        {
            "filename": name,
            "bytes": (output / name).stat().st_size,
            "sha256": sha256(output / name),
        }
        for name in sorted(outer_names)
    ]
    sums_path = output / "SHA256SUMS.csv"
    sums_path.write_bytes(
        csv_bytes(outer_rows, ["filename", "bytes", "sha256"])
    )

    if errors:
        package_validation["status"] = "FAIL"
        package_validation["errors"] = errors
        validation_path.write_text(
            json.dumps(package_validation, indent=2, ensure_ascii=True) + "\n",
            encoding="utf-8",
            newline="\n",
        )

    result = {
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "outer_files": len(outer_names) + 1,
        "outer_bytes": sum(
            path.stat().st_size
            for path in output.iterdir()
            if path.is_file()
        ),
        "outer_manifest_rows": len(outer_rows),
        "outer_manifest_sha256": sha256(sums_path),
        "reader": package_validation["reader"],
        "source_zip": package_validation["source_zip"],
    }
    print(json.dumps(result, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
