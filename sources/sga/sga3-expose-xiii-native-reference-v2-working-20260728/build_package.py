#!/usr/bin/env python3
"""Build the compact public package for the exact SGA3 Expose XIII handoff."""

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
    "00c13_SGA3_Expose_XIII_English_"
    "NativeDiagram_ReferenceV2_Working_20260728.pdf"
)
TEX_NAME = (
    "02c13_SGA3_Expose_XIII_English_"
    "NativeDiagram_ReferenceV2_Working_20260728.tex"
)
ZIP_NAME = (
    "10c13_SGA3_Expose_XIII_"
    "NativeDiagram_ReferenceV2_Source_QA_20260728.zip"
)
EXPECTED_TREE = (
    85,
    17_762_764,
    "4200EA722A2659F21EE886456751CFBD88AA274262CA322BA12BD32B846D68F0",
)
EXPECTED_MANIFEST = (
    83,
    9_032,
    "9723E97AF581C6FAE2D11C3B8C75F8DEA9DF4FFDF8DEF154D77457B8E81F4072",
)
EXPECTED_PACKAGE_VALIDATION = (
    2_931,
    "D2E6629C278FDE16878198E86FA05FEB70FE9DE0876A2D314080BD001AECB24F",
)
EXPECTED_ARCHIVE_VALIDATION = (
    2_931,
    "8F5F81220F40E23122669669E6FD7ED96A3588A62D9F45E4704C91DC1BBE72D9",
)
EXPECTED_PDF = (
    245_982,
    "69810FAAF7FF1A502E26B2488D57F95421F4786409D03DD1842E7DFD9ED92BD9",
)
EXPECTED_TEX = (
    1_286,
    "FD0FD9EEEB719A801518CF1D3BC7126CB4E686972F06ACDD35F456118F73CF80",
)
EXPECTED_METRICS = {
    "pages": 32,
    "named_destinations": 274,
    "internal_goto_actions": 494,
    "invalid_actions": 0,
    "uri_actions": 0,
    "font_resources": 32,
    "type3_fonts": 0,
    "raster_xobjects": 0,
}
PUBLIC_DOCS = (
    "README.md",
    "PUBLICATION_READINESS.md",
    "BUILD_SUMMARY_PUBLIC.md",
    "INDEPENDENT_ARCHIVE_REBUILD_PASS.md",
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
)
FIXED_ZIP_TIME = (2026, 7, 28, 0, 0, 0)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--payload-root", type=Path, required=True)
    parser.add_argument("--archive-validation", type=Path, required=True)
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


def tree_rows(root: Path) -> list[dict[str, object]]:
    rows = []
    for path in sorted(
        (path for path in root.rglob("*") if path.is_file()),
        key=lambda path: path.relative_to(root).as_posix(),
    ):
        rows.append(
            {
                "relative_path": path.relative_to(root).as_posix(),
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
        )
    return rows


def tree_aggregate(rows: list[dict[str, object]]) -> str:
    data = "".join(
        f"{row['relative_path']}\t{row['bytes']}\t{row['sha256']}\n"
        for row in rows
    ).encode("utf-8")
    return sha256_bytes(data)


def scan_bytes(name: str, data: bytes, hits: list[dict[str, str]]) -> None:
    lowered = data.lower()
    for marker in PRIVATE_MARKERS:
        if marker in lowered:
            hits.append(
                {
                    "path": name,
                    "marker": marker.decode("ascii", errors="replace"),
                }
            )


def pdf_metrics(path: Path) -> dict[str, int]:
    reader = PdfReader(str(path))
    goto = invalid = uri = type3 = 0
    fonts: set[tuple[int, int] | str] = set()
    images: set[tuple[int, int] | str] = set()
    for page in reader.pages:
        for annotation_ref in page.get("/Annots") or []:
            annotation = annotation_ref.get_object()
            if annotation.get("/Subtype") != "/Link":
                continue
            action = annotation.get("/A")
            destination = annotation.get("/Dest")
            if action and action.get("/S") == "/GoTo":
                goto += 1
                if action.get("/D") is None:
                    invalid += 1
            elif destination is not None:
                goto += 1
            elif action and action.get("/S") == "/URI":
                uri += 1
            else:
                invalid += 1
        resources = page.get("/Resources") or {}
        font_map = resources.get("/Font") or {}
        if hasattr(font_map, "get_object"):
            font_map = font_map.get_object()
        for font_ref in font_map.values():
            key = (
                (int(font_ref.idnum), int(font_ref.generation))
                if hasattr(font_ref, "idnum")
                else repr(font_ref)
            )
            fonts.add(key)
            if font_ref.get_object().get("/Subtype") == "/Type3":
                type3 += 1
        xobjects = resources.get("/XObject") or {}
        if hasattr(xobjects, "get_object"):
            xobjects = xobjects.get_object()
        for object_ref in xobjects.values():
            if object_ref.get_object().get("/Subtype") != "/Image":
                continue
            key = (
                (int(object_ref.idnum), int(object_ref.generation))
                if hasattr(object_ref, "idnum")
                else repr(object_ref)
            )
            images.add(key)
    return {
        "pages": len(reader.pages),
        "named_destinations": len(reader.named_destinations),
        "internal_goto_actions": goto,
        "invalid_actions": invalid,
        "uri_actions": uri,
        "font_resources": len(fonts),
        "type3_fonts": type3,
        "raster_xobjects": len(images),
    }


def main() -> int:
    args = parse_args()
    payload = args.payload_root.resolve()
    archive_validation = args.archive_validation.resolve()
    output = args.output_dir.resolve()
    output.mkdir(parents=True, exist_ok=True)
    errors: list[str] = []

    rows = tree_rows(payload)
    tree_identity = (
        len(rows),
        sum(int(row["bytes"]) for row in rows),
        tree_aggregate(rows),
    )
    if tree_identity != EXPECTED_TREE:
        errors.append(f"payload tree identity mismatch: {tree_identity}")

    manifest = payload / "SHA256SUMS.csv"
    producer_validation = payload / "FINAL_PACKAGE_VALIDATION.json"
    reader = payload / "reader/SGA3_Expose_XIII_English.pdf"
    master = payload / "source/tex/SGA3_Expose_XIII_English.tex"
    for path in (manifest, producer_validation, reader, master, archive_validation):
        if not path.is_file():
            errors.append(f"required file missing: {path}")
    if identity(manifest) != EXPECTED_MANIFEST[1:]:
        errors.append("producer manifest identity mismatch")
    if identity(producer_validation) != EXPECTED_PACKAGE_VALIDATION:
        errors.append("producer validation identity mismatch")
    if identity(archive_validation) != EXPECTED_ARCHIVE_VALIDATION:
        errors.append("archive validation identity mismatch")
    if identity(reader) != EXPECTED_PDF:
        errors.append("reader identity mismatch")
    if identity(master) != EXPECTED_TEX:
        errors.append("master TeX identity mismatch")

    manifest_rows = list(csv.DictReader(manifest.open(encoding="utf-8-sig")))
    expected_manifest_paths = {
        str(row["relative_path"]): (
            int(row["bytes"]),
            str(row["sha256"]).upper(),
        )
        for row in manifest_rows
    }
    actual_paths = {
        str(row["relative_path"]): (
            int(row["bytes"]),
            str(row["sha256"]).upper(),
        )
        for row in rows
        if row["relative_path"]
        not in {"SHA256SUMS.csv", "FINAL_PACKAGE_VALIDATION.json"}
    }
    if len(manifest_rows) != EXPECTED_MANIFEST[0]:
        errors.append("producer manifest row count mismatch")
    if expected_manifest_paths != actual_paths:
        errors.append("producer manifest exact replay mismatch")

    producer_result = json.loads(producer_validation.read_text(encoding="utf-8"))
    archive_result = json.loads(archive_validation.read_text(encoding="utf-8"))
    if producer_result.get("status") != "PASS" or producer_result.get("errors"):
        errors.append("producer validation is not PASS/errors[]")
    if archive_result.get("status") != "PASS" or archive_result.get("errors"):
        errors.append("archive validation is not PASS/errors[]")

    metrics = pdf_metrics(reader)
    for field, expected in EXPECTED_METRICS.items():
        if metrics[field] != expected:
            errors.append(
                f"PDF metric {field}={metrics[field]} expected {expected}"
            )

    text = "\n".join(
        path.read_text(encoding="utf-8", errors="replace")
        for path in sorted((payload / "source/tex").rglob("*.tex"))
    )
    if text.count(r"\begin{tikzcd}") != 7:
        errors.append("native diagram count is not 7")
    if r"\includegraphics" in text:
        errors.append("raster includegraphics found")

    privacy_hits: list[dict[str, str]] = []
    for path in payload.rglob("*"):
        if path.is_file():
            scan_bytes(path.relative_to(payload).as_posix(), path.read_bytes(), privacy_hits)
    pdf_path = output / PDF_NAME
    tex_path = output / TEX_NAME
    shutil.copyfile(reader, pdf_path)
    shutil.copyfile(master, tex_path)
    archive_validation_path = output / "ARCHIVE_INDEPENDENT_VALIDATION_PASS.json"
    shutil.copyfile(archive_validation, archive_validation_path)

    zip_path = output / ZIP_NAME
    with zipfile.ZipFile(
        zip_path,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
        allowZip64=True,
    ) as archive:
        for row in rows:
            name = str(row["relative_path"])
            if not safe_member(name):
                errors.append(f"unsafe member: {name}")
                continue
            archive.writestr(zip_info(name), (payload / name).read_bytes())

    zip_errors: list[str] = []
    with zipfile.ZipFile(zip_path) as archive:
        names = archive.namelist()
        if archive.testzip() is not None:
            zip_errors.append("CRC failure")
        if len(names) != len(set(names)):
            zip_errors.append("duplicate ZIP member")
        if set(names) != {str(row["relative_path"]) for row in rows}:
            zip_errors.append("ZIP exact member set mismatch")
        for row in rows:
            name = str(row["relative_path"])
            if archive.read(name) != (payload / name).read_bytes():
                zip_errors.append(f"ZIP identity mismatch: {name}")
    errors.extend(zip_errors)

    for name in PUBLIC_DOCS:
        path = output / name
        if not path.is_file():
            errors.append(f"missing public document: {name}")
        else:
            scan_bytes(name, path.read_bytes(), privacy_hits)
    if privacy_hits:
        errors.append(f"privacy hits: {privacy_hits[:20]}")

    package_validation = {
        "schema": "sga3_expose_xiii_compact_public_package_v1",
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "payload_tree": {
            "files": tree_identity[0],
            "bytes": tree_identity[1],
            "ordered_aggregate_sha256": tree_identity[2],
        },
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
            "filename": ZIP_NAME,
            "bytes": zip_path.stat().st_size,
            "sha256": sha256(zip_path),
            "members": len(rows),
            "uncompressed_bytes": sum(int(row["bytes"]) for row in rows),
            "crc_or_identity_errors": zip_errors,
        },
        "producer_validation": {
            "status": producer_result.get("status"),
            "errors": producer_result.get("errors"),
            "bytes": producer_validation.stat().st_size,
            "sha256": sha256(producer_validation),
        },
        "archive_validation": {
            "status": archive_result.get("status"),
            "errors": archive_result.get("errors"),
            "bytes": archive_validation.stat().st_size,
            "sha256": sha256(archive_validation),
        },
        "privacy": {"hits": privacy_hits},
    }
    validation_path = output / "PACKAGE_VALIDATION.json"
    validation_path.write_text(
        json.dumps(package_validation, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
        newline="\n",
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
    sums = output / "SHA256SUMS.csv"
    sums.write_bytes(csv_bytes(outer_rows, ["filename", "bytes", "sha256"]))

    print(
        json.dumps(
            {
                "status": package_validation["status"],
                "errors": errors,
                "reader": package_validation["reader"],
                "master_tex": package_validation["master_tex"],
                "source_archive": package_validation["source_archive"],
                "outer_manifest_rows": len(outer_rows),
                "outer_manifest_sha256": sha256(sums),
            },
            indent=2,
        )
    )
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
