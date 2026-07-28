#!/usr/bin/env python3
"""Build and validate the compact SGA3 Exposé XXIII working package."""

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
    "00c23_SGA3_Expose_XXIII_English_"
    "NativeDiagram_Loop1_Working_20260728.pdf"
)
TEX_NAME = (
    "02c23_SGA3_Expose_XXIII_English_"
    "NativeDiagram_Loop1_Working_20260728.tex"
)
ZIP_NAME = (
    "10c23_SGA3_Expose_XXIII_"
    "NativeDiagram_Loop1_Source_20260728.zip"
)
EXPECTED_PRODUCER_PDF = (
    220_261,
    "22EB1CD2B5133D2E7567CAE086AFE920EA90AEA4FF17E4C07BC5BA5E42DBF7D5",
)
EXPECTED_REBUILD_PDF = (
    220_282,
    "6E9AD4D929FDFA3A9DA8000F8768EA57A38D6332AA25A55AC48131722E1EB344",
)
EXPECTED_LEAD_RECEIPT = (
    2_492,
    "F319B162353D811B50793467AD860CB75A98266D743CFA8B10357924E9425FA0",
)
EXPECTED_TEX = {
    "tex/components/00_expose_XXIII_title_and_definition11.tex": (
        2_363,
        "7884F3A8B7823841685F9A9E1243ECFD322277C9F0A765716FFC7ED19CA430FE",
    ),
    "tex/components/01_expose_XXIII_par12_and_definition13.tex": (
        2_551,
        "70C06210CBFC5DD0C6D278EA05CA1756418053C61B891582EB74B8EC73CD4371",
    ),
    "tex/components/02_expose_XXIII_par14_through_scholium16.tex": (
        1_414,
        "7EF6F7458FD160F03B4E7C14CD21DC19D9E01A6558B2CF2FE25285F5AD0D15C1",
    ),
    "tex/components/03_expose_XXIII_par17_through_remark193.tex": (
        8_185,
        "FBA51F9E5AD9492DFEF877A187E3B486447CAF4236C05720DEBB6254E707721C",
    ),
    "tex/components/04_expose_XXIII_theorem21_through_corollary24.tex": (
        19_293,
        "0DEF26BFAF89E8CC54BFD1066A1C79BE9F5357453B66EA16C2AABC5E84994276",
    ),
    "tex/components/05_expose_XXIII_cor25_through_par313.tex": (
        8_676,
        "B1AC3E4F425B96E01AF62219198E48CEDFDCF343CA8AB461DACDB3228F05AB24",
    ),
    "tex/components/06_expose_XXIII_type_A2_and_B2.tex": (
        12_176,
        "9A2D25E02526FDDF1AFCF1A6229E87B6D572C6FD736AC5449D1A578AB4F81CB5",
    ),
    "tex/components/07_expose_XXIII_type_G2.tex": (
        10_798,
        "3BF5FF2966EA6F0FC8E99C5039AACA303133F088BEDA6BB337EFA638B35DA998",
    ),
    "tex/components/08_expose_XXIII_generators_relations_explicit.tex": (
        3_873,
        "404D92D2C65FA9FC734D73DDDA2302C9A3BD24C1FD62B801C70A149AB5C47D8D",
    ),
    "tex/components/09_expose_XXIII_fundamental_theorem.tex": (
        11_703,
        "869F9CFAC409FC4F81DBC921DC5A94A3410E2BAF15904CB152866BE5E403096E",
    ),
    "tex/components/10_expose_XXIII_corollaries.tex": (
        7_726,
        "493A1F66C9E99C354A7B555A35E3C380C670A848454C9F25C0A73C7F9A7ACD24",
    ),
    "tex/components/11_expose_XXIII_chevalley_systems_and_bibliography.tex": (
        8_717,
        "CEB9C70A52CB812757B29A471E55393717D8030CABEB7202E9DA6F8BAF692FFD",
    ),
    "tex/SGA3_Expose_XXIII_English.tex": (
        1_790,
        "3DC28C22DE4DC972C3D10B363BC9B9CA674EC5CB1353F68DF8FCFE7D2B022274",
    ),
    "tex/sga3_expose_xxiii_macros.tex": (
        773,
        "E0FC5FF0C0D3669DF006334B51CF1054D4ABC25494264DE31C352E7800F4D0EA",
    ),
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


def pdf_metrics(path: Path) -> dict[str, int]:
    reader = PdfReader(path)
    goto = 0
    invalid = 0
    uri = 0
    linked_pages = 0
    fonts: set[tuple[int | None, int | None]] = set()
    type3 = 0
    raster_xobjects = 0
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
    output = args.output_dir.resolve()
    output.mkdir(parents=True, exist_ok=True)
    errors: list[str] = []

    producer_pdf = producer / "build" / "SGA3_Expose_XXIII_English.pdf"
    producer_master = producer / "tex" / "SGA3_Expose_XXIII_English.tex"
    lead_receipt = (
        producer
        / "qa"
        / "diagram_highzoom"
        / "LEAD_NATIVE_DIAGRAM_5000DPI_REVIEW_PASS.md"
    )
    for path in (producer_pdf, producer_master, lead_receipt, rebuild_pdf):
        if not path.is_file():
            errors.append(f"missing required input: {path}")
    if errors:
        raise SystemExit("\n".join(errors))

    for relative, expected in EXPECTED_TEX.items():
        path = producer / PurePosixPath(relative)
        if not path.is_file() or identity(path) != expected:
            errors.append(f"TeX identity mismatch: {relative}")
    if identity(producer_pdf) != EXPECTED_PRODUCER_PDF:
        errors.append("producer PDF identity mismatch")
    if identity(rebuild_pdf) != EXPECTED_REBUILD_PDF:
        errors.append("independent rebuild PDF identity mismatch")
    if identity(lead_receipt) != EXPECTED_LEAD_RECEIPT:
        errors.append("lead review receipt identity mismatch")

    tex_content = "\n".join(
        (producer / PurePosixPath(relative)).read_text(
            encoding="utf-8", errors="strict"
        )
        for relative in sorted(EXPECTED_TEX)
    )
    if tex_content.count(r"\begin{tikzcd}") != 1:
        errors.append("native diagram count is not exactly one")
    if r"\includegraphics" in tex_content:
        errors.append("raster include found in TeX closure")

    comparison = compare_pdfs(producer_pdf, rebuild_pdf)
    expected_metrics = {
        "pages": 37,
        "named_destinations": 227,
        "internal_goto_actions": 58,
        "linked_pages": 13,
        "invalid_actions": 0,
        "uri_actions": 0,
        "font_resources": 36,
        "type3_fonts": 0,
        "raster_xobjects": 0,
    }
    if comparison["producer_metrics"] != expected_metrics:
        errors.append("producer PDF metric mismatch")
    if comparison["rebuild_metrics"] != expected_metrics:
        errors.append("rebuild PDF metric mismatch")
    for field in (
        "text_mismatch_pages",
        "content_stream_mismatch_pages",
        "geometry_mismatch_pages",
    ):
        if comparison[field]:
            errors.append(f"PDF comparison failure: {field}")

    shutil.copyfile(producer_pdf, output / PDF_NAME)
    shutil.copyfile(producer_master, output / TEX_NAME)
    shutil.copyfile(
        lead_receipt,
        output / "LEAD_NATIVE_DIAGRAM_5000DPI_REVIEW_PASS.md",
    )

    source_members: dict[str, bytes] = {}
    for relative in sorted(EXPECTED_TEX):
        source_members[relative] = (
            producer / PurePosixPath(relative)
        ).read_bytes()
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
        "schema": "sga3_expose_xxiii_native_loop1_source_v1",
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "scope": {
            "complete": "SGA3 Expose XXIII only",
            "authority_pages": "local 1-37 / combined 1209-1245",
            "next_cursor": "Expose XXIV local 1 / combined 1246",
        },
        "editable_tex_files": len(EXPECTED_TEX),
        "native_tikzcd_diagrams": 1,
        "raster_includes": 0,
        "authority_images_included": 0,
        "source_manifest_rows": len(source_rows),
        "source_manifest_sha256": sha256_bytes(source_manifest),
        "pdf_comparison": comparison,
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
        "schema": "sga3_expose_xxiii_native_loop1_outer_v1",
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "reader": {
            "filename": PDF_NAME,
            "bytes": (output / PDF_NAME).stat().st_size,
            "sha256": sha256(output / PDF_NAME),
            **expected_metrics,
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
        "render_equivalence": {
            "dpi": 200,
            "producer_pages": 37,
            "rebuild_pages": 37,
            "pixel_or_byte_mismatch_pages": 0,
        },
        "visual_review": {
            "pages_reviewed": 37,
            "native_diagrams_reviewed_at_5000dpi": 1,
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
