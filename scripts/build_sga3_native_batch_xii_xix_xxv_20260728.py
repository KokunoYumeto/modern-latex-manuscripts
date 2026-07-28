#!/usr/bin/env python3
"""Build compact SGA3 native-diagram working packages for XII, XIX, and XXV."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import shutil
import zipfile
from dataclasses import dataclass
from pathlib import Path, PurePosixPath

from pypdf import PdfReader


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


@dataclass(frozen=True)
class Unit:
    key: str
    producer_dir: str
    producer_pdf: str
    rebuild_pdf: str
    master: str
    output_dir: str
    pdf_name: str
    tex_name: str
    zip_name: str
    receipt_name: str
    receipt_source: str | None
    expected_receipt: tuple[int, str] | None
    expected_producer_pdf: tuple[int, str]
    expected_rebuild_pdf: tuple[int, str]
    expected_tex_count: int
    expected_tex_aggregate: tuple[int, str]
    expected_metrics: dict[str, int]
    expected_tikzcd: int
    scope: str
    authority_pages: str
    next_cursor: str
    authority_file: str
    authority_bytes: int
    authority_sha256: str
    visual_pages: tuple[int, ...]


UNITS = (
    Unit(
        key="xii",
        producer_dir="sga3_exposeXII_native_diagram_loop2_successor_r1_20260728",
        producer_pdf="build/SGA3_Expose_XII_English.pdf",
        rebuild_pdf="xii/build/SGA3_Expose_XII_English.pdf",
        master="tex/SGA3_Expose_XII_English.tex",
        output_dir="sources/sga/sga3-expose-xii-native-loop1-working-20260728",
        pdf_name=(
            "00c12_SGA3_Expose_XII_English_"
            "NativeDiagram_Loop1_Working_20260728.pdf"
        ),
        tex_name=(
            "02c12_SGA3_Expose_XII_English_"
            "NativeDiagram_Loop1_Working_20260728.tex"
        ),
        zip_name=(
            "10c12_SGA3_Expose_XII_"
            "NativeDiagram_Loop1_Source_20260728.zip"
        ),
        receipt_name="LEAD_NATIVE_DIAGRAM_5000_9000DPI_REVIEW_PASS.md",
        receipt_source=(
            "qa/native_redo_20260728/"
            "LEAD_NATIVE_DIAGRAM_5000_9000DPI_REVIEW_PASS.md"
        ),
        expected_receipt=(
            5_178,
            "8B436D4F8966DBD596B582F662B681166156C347C5FBB39EF5F8BADD402674A8",
        ),
        expected_producer_pdf=(
            282_869,
            "17D3646EF85FB1C1D7831B646755C199C862E912935EC4B01DAA0DF0BF48ADDC",
        ),
        expected_rebuild_pdf=(
            282_864,
            "678902C0BF78341B6950467D3DEE7F8EFF7EE78BCDD67FE4115D26D137326E82",
        ),
        expected_tex_count=5,
        expected_tex_aggregate=(
            572,
            "B5A3A7D7A5831E59E027FD6BD40DB04043C97AE75F17EB27AA372E4CA1A2ADE5",
        ),
        expected_metrics={
            "pages": 51,
            "named_destinations": 287,
            "internal_goto_actions": 28,
            "linked_pages": 14,
            "invalid_actions": 0,
            "uri_actions": 0,
            "font_resources": 27,
            "type3_fonts": 0,
            "raster_xobjects": 0,
        },
        expected_tikzcd=2,
        scope="complete SGA3 Expose XII only",
        authority_pages="local 1-48 / combined 757-804",
        next_cursor="Expose XIII local 1 / combined 805",
        authority_file="Expo12.pdf",
        authority_bytes=490_790,
        authority_sha256=(
            "4DAE85A06B7C1D6CD98D6332DE144AED80A96D19267D0603CC9CBEF06757C15E"
        ),
        visual_pages=(1, 12, 30, 51),
    ),
    Unit(
        key="xix",
        producer_dir="sga3_exposeXIX_english_loop1_reconstruction_20260728",
        producer_pdf=(
            "build_loop1_complete_r13/SGA3_Expose_XIX_English.pdf"
        ),
        rebuild_pdf="xix/build/SGA3_Expose_XIX_English.pdf",
        master="tex/SGA3_Expose_XIX_English.tex",
        output_dir="sources/sga/sga3-expose-xix-native-loop1-working-20260728",
        pdf_name=(
            "00c19_SGA3_Expose_XIX_English_"
            "NativeDiagram_Loop1_Working_20260728.pdf"
        ),
        tex_name=(
            "02c19_SGA3_Expose_XIX_English_"
            "NativeDiagram_Loop1_Working_20260728.tex"
        ),
        zip_name=(
            "10c19_SGA3_Expose_XIX_"
            "NativeDiagram_Loop1_Source_20260728.zip"
        ),
        receipt_name="ARCHIVE_NATIVE_DIAGRAM_5000DPI_REPLAY_PASS.md",
        receipt_source=None,
        expected_receipt=None,
        expected_producer_pdf=(
            659_293,
            "6C57558E58C3D27BF453C094121495F4EC66CF7CEC66E8790D783317BDD1DE39",
        ),
        expected_rebuild_pdf=(
            659_293,
            "23DB984412E4A4B619F4B10E281AE1AEA9E7C788A6AA240DD0924A63D88F557F",
        ),
        expected_tex_count=28,
        expected_tex_aggregate=(
            3_959,
            "E7747A48F21083B4D14AFA6585CED338EC8036D818DC37CB66F69EC77C8F4FC0",
        ),
        expected_metrics={
            "pages": 27,
            "named_destinations": 174,
            "internal_goto_actions": 55,
            "linked_pages": 22,
            "invalid_actions": 0,
            "uri_actions": 0,
            "font_resources": 35,
            "type3_fonts": 0,
            "raster_xobjects": 0,
        },
        expected_tikzcd=1,
        scope="complete SGA3 Expose XIX only",
        authority_pages="local 1-25 / combined 1035-1059",
        next_cursor="Expose XX local 1 / combined 1060",
        authority_file="Exp19-13oct24.pdf",
        authority_bytes=294_510,
        authority_sha256=(
            "B257B4D5D9003E966096E77E33D0131318F6B0266A144DEF71559A9C98F4BF9F"
        ),
        visual_pages=(1, 17, 27),
    ),
    Unit(
        key="xxv",
        producer_dir="sga3_exposeXXV_english_loop1_reconstruction_20260728",
        producer_pdf=(
            "build_loop1_complete_r2/SGA3_Expose_XXV_English.pdf"
        ),
        rebuild_pdf="xxv/build/SGA3_Expose_XXV_English.pdf",
        master="tex/SGA3_Expose_XXV_English.tex",
        output_dir="sources/sga/sga3-expose-xxv-native-loop1-working-20260728",
        pdf_name=(
            "00c25_SGA3_Expose_XXV_English_"
            "NativeDiagram_Loop1_Working_20260728.pdf"
        ),
        tex_name=(
            "02c25_SGA3_Expose_XXV_English_"
            "NativeDiagram_Loop1_Working_20260728.tex"
        ),
        zip_name=(
            "10c25_SGA3_Expose_XXV_"
            "NativeDiagram_Loop1_Source_20260728.zip"
        ),
        receipt_name="LEAD_NATIVE_DIAGRAM_5000DPI_REVIEW_PASS.md",
        receipt_source=(
            "qa/authority_highzoom/"
            "LEAD_NATIVE_DIAGRAM_5000DPI_REVIEW_PASS.md"
        ),
        expected_receipt=(
            1_028,
            "A460D03FA1308A12046252AA2DF8319DFF6BB2E1AC66EE7B424BB75492B349BD",
        ),
        expected_producer_pdf=(
            498_082,
            "8F2FC8434D352354F1AA16A8A36913988768F2261F74072A5F7CF4D796BE04D9",
        ),
        expected_rebuild_pdf=(
            498_082,
            "A30CB135A5EC26467E112178ACA685E3EBA59C1FD28C3747E70878016B0E400B",
        ),
        expected_tex_count=7,
        expected_tex_aggregate=(
            791,
            "45EFBA3B11AB5454F525476EBCB11D055F1123B8B62E144B9100060ACA0A512C",
        ),
        expected_metrics={
            "pages": 14,
            "named_destinations": 85,
            "internal_goto_actions": 29,
            "linked_pages": 6,
            "invalid_actions": 0,
            "uri_actions": 0,
            "font_resources": 29,
            "type3_fonts": 0,
            "raster_xobjects": 0,
        },
        expected_tikzcd=2,
        scope="complete SGA3 Expose XXV only",
        authority_pages="local 1-11 / combined 1300-1310",
        next_cursor="Expose XXVI local 1 / combined 1311",
        authority_file="Exp25-13oct24.pdf",
        authority_bytes=180_943,
        authority_sha256=(
            "DCC3D12ECEF709FB23DE2304B82F82AF25DEC4217AA2CDB85858FC1586FE5255"
        ),
        visual_pages=(1, 7, 11, 14),
    ),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--working-root", type=Path, required=True)
    parser.add_argument("--rebuild-root", type=Path, required=True)
    parser.add_argument("--render-root", type=Path, required=True)
    parser.add_argument("--repo-root", type=Path, required=True)
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
    path = PurePosixPath(name)
    return (
        bool(name)
        and not path.is_absolute()
        and ".." not in path.parts
        and "\\" not in name
        and re.match(r"^[A-Za-z]:", name) is None
    )


def zip_info(name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, date_time=FIXED_ZIP_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.create_system = 3
    info.external_attr = 0o100644 << 16
    return info


def tex_rows(producer: Path) -> list[dict[str, object]]:
    return [
        {
            "relative_path": path.relative_to(producer).as_posix(),
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        }
        for path in sorted((producer / "tex").rglob("*.tex"))
    ]


def tex_aggregate(rows: list[dict[str, object]]) -> tuple[int, str]:
    data = "".join(
        f"{row['relative_path']}\t{row['bytes']}\t{row['sha256']}\n"
        for row in rows
    ).encode("utf-8")
    return len(data), sha256_bytes(data)


def pdf_metrics(path: Path) -> dict[str, int]:
    reader = PdfReader(path)
    goto = invalid = uri = linked_pages = type3 = raster = 0
    fonts: set[tuple[int | None, int | None]] = set()
    for page in reader.pages:
        page_links = 0
        for annotation_ref in page.get("/Annots") or []:
            annotation = annotation_ref.get_object()
            if str(annotation.get("/Subtype")) != "/Link":
                continue
            action = annotation.get("/A")
            destination = annotation.get("/Dest")
            if destination is not None:
                goto += 1
                page_links += 1
            elif action and str(action.get_object().get("/S")) == "/GoTo":
                goto += 1
                page_links += 1
                invalid += action.get_object().get("/D") is None
            elif action and str(action.get_object().get("/S")) == "/URI":
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
            if str(font_ref.get_object().get("/Subtype")) == "/Type3":
                type3 += 1
        xobjects = resources.get("/XObject") or {}
        if hasattr(xobjects, "get_object"):
            xobjects = xobjects.get_object()
        for xobject_ref in xobjects.values():
            if str(xobject_ref.get_object().get("/Subtype")) == "/Image":
                raster += 1
    return {
        "pages": len(reader.pages),
        "named_destinations": len(reader.named_destinations),
        "internal_goto_actions": goto,
        "linked_pages": linked_pages,
        "invalid_actions": invalid,
        "uri_actions": uri,
        "font_resources": len(fonts),
        "type3_fonts": type3,
        "raster_xobjects": raster,
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
        left_contents = left.get_contents()
        right_contents = right.get_contents()
        left_data = left_contents.get_data() if left_contents else b""
        right_data = right_contents.get_data() if right_contents else b""
        if left_data != right_data:
            content_mismatch.append(page_number)
        if (
            tuple(left.mediabox),
            tuple(left.cropbox),
            int(left.get("/Rotate", 0) or 0),
        ) != (
            tuple(right.mediabox),
            tuple(right.cropbox),
            int(right.get("/Rotate", 0) or 0),
        ):
            geometry_mismatch.append(page_number)
    return {
        "producer_metrics": pdf_metrics(producer),
        "rebuild_metrics": pdf_metrics(rebuild),
        "text_mismatch_pages": text_mismatch,
        "content_stream_mismatch_pages": content_mismatch,
        "geometry_mismatch_pages": geometry_mismatch,
    }


def compare_renders(render_dir: Path, pages: int) -> dict[str, object]:
    producer = sorted(render_dir.glob("producer-*.png"))
    rebuild = sorted(render_dir.glob("rebuild-*.png"))
    mismatches = []
    if len(producer) == len(rebuild):
        for page_number, (left, right) in enumerate(
            zip(producer, rebuild), start=1
        ):
            if identity(left) != identity(right):
                mismatches.append(page_number)
    return {
        "dpi": 150,
        "producer_pages": len(producer),
        "rebuild_pages": len(rebuild),
        "expected_pages": pages,
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


def build_unit(
    unit: Unit,
    working_root: Path,
    rebuild_root: Path,
    render_root: Path,
    repo_root: Path,
) -> dict[str, object]:
    producer = (working_root / unit.producer_dir).resolve()
    producer_pdf = producer / unit.producer_pdf
    rebuild_pdf = (rebuild_root / unit.rebuild_pdf).resolve()
    producer_master = producer / unit.master
    output = (repo_root / unit.output_dir).resolve()
    output.mkdir(parents=True, exist_ok=True)
    errors: list[str] = []

    required = [producer_pdf, rebuild_pdf, producer_master, producer / "tex"]
    for name in PUBLIC_DOCS:
        required.append(output / name)
    if unit.receipt_source:
        required.append(producer / unit.receipt_source)
    else:
        required.append(output / unit.receipt_name)
    for path in required:
        if not path.exists():
            errors.append(f"missing required input: {path}")
    if errors:
        return {"unit": unit.key, "status": "FAIL", "errors": errors}

    rows = tex_rows(producer)
    if len(rows) != unit.expected_tex_count:
        errors.append("TeX file count mismatch")
    if tex_aggregate(rows) != unit.expected_tex_aggregate:
        errors.append("TeX aggregate mismatch")
    if identity(producer_pdf) != unit.expected_producer_pdf:
        errors.append("producer PDF identity mismatch")
    if identity(rebuild_pdf) != unit.expected_rebuild_pdf:
        errors.append("independent rebuild PDF identity mismatch")

    receipt_source = (
        producer / unit.receipt_source
        if unit.receipt_source
        else output / unit.receipt_name
    )
    if (
        unit.expected_receipt is not None
        and identity(receipt_source) != unit.expected_receipt
    ):
        errors.append("diagram review receipt identity mismatch")

    tex_content = "\n".join(
        (producer / str(row["relative_path"])).read_text(encoding="utf-8")
        for row in rows
    )
    if tex_content.count(r"\begin{tikzcd}") != unit.expected_tikzcd:
        errors.append("native tikz-cd count mismatch")
    if r"\includegraphics" in tex_content:
        errors.append("raster include found in TeX closure")

    comparison = compare_pdfs(producer_pdf, rebuild_pdf)
    if comparison["producer_metrics"] != unit.expected_metrics:
        errors.append("producer PDF metric mismatch")
    if comparison["rebuild_metrics"] != unit.expected_metrics:
        errors.append("rebuild PDF metric mismatch")
    for field in (
        "text_mismatch_pages",
        "content_stream_mismatch_pages",
        "geometry_mismatch_pages",
    ):
        if comparison[field]:
            errors.append(f"PDF comparison failure: {field}")

    render_comparison = compare_renders(
        render_root / unit.key, unit.expected_metrics["pages"]
    )
    if (
        render_comparison["producer_pages"]
        != unit.expected_metrics["pages"]
        or render_comparison["rebuild_pages"]
        != unit.expected_metrics["pages"]
        or render_comparison["pixel_or_byte_mismatch_pages"]
    ):
        errors.append("render comparison failure")

    shutil.copyfile(producer_pdf, output / unit.pdf_name)
    shutil.copyfile(producer_master, output / unit.tex_name)
    if receipt_source.resolve() != (output / unit.receipt_name).resolve():
        shutil.copyfile(receipt_source, output / unit.receipt_name)

    source_members: dict[str, bytes] = {
        str(row["relative_path"]): (
            producer / str(row["relative_path"])
        ).read_bytes()
        for row in rows
    }
    for name in (*PUBLIC_DOCS, unit.receipt_name):
        source_members[name] = (output / name).read_bytes()
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
        "schema": "sga3_native_loop1_source_v1",
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "scope": {
            "complete": unit.scope,
            "authority_pages": unit.authority_pages,
            "next_cursor": unit.next_cursor,
        },
        "authority": {
            "filename": unit.authority_file,
            "bytes": unit.authority_bytes,
            "sha256": unit.authority_sha256,
            "included": False,
        },
        "editable_tex_files": len(rows),
        "native_tikzcd_diagrams": unit.expected_tikzcd,
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

    source_zip = output / unit.zip_name
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
            scan_text(f"{unit.zip_name}:{name}", data, privacy_hits)
    if privacy_hits:
        errors.append(f"privacy hits: {privacy_hits}")

    package_validation = {
        "schema": "sga3_native_loop1_outer_v1",
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "scope": unit.scope,
        "reader": {
            "filename": unit.pdf_name,
            "bytes": (output / unit.pdf_name).stat().st_size,
            "sha256": sha256(output / unit.pdf_name),
            **unit.expected_metrics,
        },
        "direct_master_tex": {
            "filename": unit.tex_name,
            "bytes": (output / unit.tex_name).stat().st_size,
            "sha256": sha256(output / unit.tex_name),
        },
        "source_zip": {
            "filename": unit.zip_name,
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
            "archive_pages_reviewed": unit.visual_pages,
            "native_diagrams": unit.expected_tikzcd,
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
        unit.pdf_name,
        unit.tex_name,
        unit.zip_name,
        "PACKAGE_VALIDATION.json",
        unit.receipt_name,
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

    return {
        "unit": unit.key,
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


def main() -> int:
    args = parse_args()
    results = [
        build_unit(
            unit,
            args.working_root.resolve(),
            args.rebuild_root.resolve(),
            args.render_root.resolve(),
            args.repo_root.resolve(),
        )
        for unit in UNITS
    ]
    status = "PASS" if all(row["status"] == "PASS" for row in results) else "FAIL"
    print(json.dumps({"status": status, "units": results}, indent=2))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
