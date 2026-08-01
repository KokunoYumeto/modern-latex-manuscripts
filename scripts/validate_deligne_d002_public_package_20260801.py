#!/usr/bin/env python3
"""Independently replay the Deligne D002 public package from copied bytes."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import subprocess
import zipfile
from pathlib import Path, PurePosixPath

from pypdf import PdfReader

import build_deligne_d001_public_package_20260801 as base
import build_deligne_d002_public_package_20260801 as package


PDF_EXPECTATIONS = {
    "09_Deligne_D002_Bilingual_SourceAligned_Reader_20260801.pdf": (
        "build/bilingual_source_aligned_eof_r1/D002_ProperSupport_Bilingual_Reader.pdf",
        24,
    ),
    "10_Deligne_D002_English_SourceAligned_20260801.pdf": (
        "build/en_final/D002_ProperSupport_EN_source_aligned.pdf",
        12,
    ),
    "11_Deligne_D002_French_SourceAligned_20260801.pdf": (
        "build/fr_final/D002_ProperSupport_FR_source_aligned.pdf",
        12,
    ),
}


def safe_member(name: str) -> bool:
    pure = PurePosixPath(name)
    return (
        name == name.replace("\\", "/")
        and not pure.is_absolute()
        and ".." not in pure.parts
        and not (len(name) > 1 and name[1] == ":")
    )


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def verify_manifest(
    root: Path,
    manifest_path: Path,
    excluded_names: set[str],
) -> dict[str, object]:
    fields, rows = read_csv(manifest_path)
    if fields != ["relative_path", "bytes", "sha256"]:
        raise RuntimeError(f"Unexpected manifest fields in {manifest_path}: {fields}")
    row_paths = [row["relative_path"] for row in rows]
    if len(row_paths) != len(set(row_paths)):
        raise RuntimeError(f"Duplicate manifest paths in {manifest_path}")
    actual = sorted(
        path.relative_to(root).as_posix()
        for path in root.rglob("*")
        if path.is_file() and path.name not in excluded_names
    )
    if sorted(row_paths) != actual:
        missing = sorted(set(actual) - set(row_paths))
        extra = sorted(set(row_paths) - set(actual))
        raise RuntimeError(f"Manifest closure failed: missing={missing}, extra={extra}")
    for row in rows:
        path = root / row["relative_path"]
        wanted = (int(row["bytes"]), row["sha256"].upper())
        base.require_identity(path, wanted)
    return {
        "rows": len(rows),
        "bytes": manifest_path.stat().st_size,
        "sha256": base.sha256_path(manifest_path),
        "closure": "exact",
    }


def verify_csvs(root: Path) -> dict[str, object]:
    formula_errors: list[dict[str, object]] = []
    reports: list[dict[str, object]] = []
    for path in sorted(root.rglob("*.csv")):
        fields, rows = read_csv(path)
        if not fields or len(fields) != len(set(fields)):
            raise RuntimeError(f"Invalid CSV header: {path}")
        for row_number, row in enumerate(rows, start=2):
            if None in row:
                raise RuntimeError(f"Non-rectangular CSV row: {path}:{row_number}")
            for field, value in row.items():
                if value and value[0] in "=+-@":
                    formula_errors.append(
                        {
                            "path": path.relative_to(root).as_posix(),
                            "row": row_number,
                            "field": field,
                            "value": value[:80],
                        }
                    )
        reports.append(
            {
                "path": path.relative_to(root).as_posix(),
                "columns": len(fields),
                "rows": len(rows),
            }
        )
    if formula_errors:
        raise RuntimeError(f"Formula-unsafe CSV cells: {formula_errors[:3]}")
    return {"files": len(reports), "formula_errors": [], "reports": reports}


def verify_json(root: Path) -> dict[str, object]:
    json_files = 0
    jsonl_files = 0
    jsonl_records = 0
    for path in sorted(root.rglob("*.json")):
        json.loads(path.read_text(encoding="utf-8-sig"))
        json_files += 1
    for path in sorted(root.rglob("*.jsonl")):
        for line_number, line in enumerate(
            path.read_text(encoding="utf-8-sig").splitlines(), start=1
        ):
            if not line.strip():
                raise RuntimeError(f"Blank JSONL record: {path}:{line_number}")
            json.loads(line)
            jsonl_records += 1
        jsonl_files += 1
    return {
        "json_files": json_files,
        "jsonl_files": jsonl_files,
        "jsonl_records": jsonl_records,
        "errors": [],
    }


def verify_visual_ledger(inner: Path) -> dict[str, object]:
    csv_path = inner / "visual_evidence/VISUAL_EVIDENCE_INDEX.csv"
    jsonl_path = inner / "visual_evidence/VISUAL_EVIDENCE_INDEX.jsonl"
    _fields, csv_rows = read_csv(csv_path)
    json_rows = [
        json.loads(line)
        for line in jsonl_path.read_text(encoding="utf-8-sig").splitlines()
        if line.strip()
    ]
    if csv_rows != [{key: str(value) for key, value in row.items()} for row in json_rows]:
        raise RuntimeError("Visual-evidence CSV/JSONL mismatch")
    if len(csv_rows) != 4:
        raise RuntimeError(f"Visual-evidence row count changed: {len(csv_rows)}")
    witness_ids = [row["witness_id"] for row in csv_rows]
    if len(witness_ids) != len(set(witness_ids)):
        raise RuntimeError("Duplicate visual witness IDs")
    for row in csv_rows:
        if row["parent_source_sha256"] != package.AUTHORITY_SHA256:
            raise RuntimeError("Visual parent hash changed")
        path = inner / row["relative_path"]
        base.require_identity(path, (int(row["crop_bytes"]), row["crop_sha256"]))
        if base.png_dimensions(path) != (int(row["width_pixels"]), int(row["height_pixels"])):
            raise RuntimeError(f"Visual dimensions changed: {path}")
        box = json.loads(row["bbox_source_render_pixels"])
        if not (
            len(box) == 4
            and 0 <= box[0] < box[2] <= 9600
            and 0 <= box[1] < box[3] <= 13084
        ):
            raise RuntimeError(f"Invalid visual bbox: {row}")
    return {
        "rows": len(csv_rows),
        "unique_ids": True,
        "parent_hash_exact": True,
        "crop_hashes_exact": True,
        "dimensions_exact": True,
        "coordinates_bounded": True,
        "csv_jsonl_equal": True,
    }


def run_command(command: list[str], cwd: Path, log_path: Path) -> None:
    result = subprocess.run(
        command,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text(result.stdout, encoding="utf-8", newline="\n")
    if result.returncode != 0:
        raise RuntimeError(f"Command failed ({result.returncode}): {' '.join(command)}")


def build_tex(
    xelatex: str,
    cwd: Path,
    source_name: str,
    output_dir: Path,
    passes: int,
) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    for number in range(1, passes + 1):
        run_command(
            [
                xelatex,
                "-interaction=nonstopmode",
                "-halt-on-error",
                f"-output-directory={output_dir}",
                source_name,
            ],
            cwd,
            output_dir / f"pass-{number}.console.txt",
        )
    return output_dir / f"{Path(source_name).stem}.pdf"


def page_stream(page: object) -> bytes:
    contents = page.get_contents()
    return b"" if contents is None else contents.get_data()


def pdf_semantic_compare(expected: Path, observed: Path) -> dict[str, object]:
    left = PdfReader(expected)
    right = PdfReader(observed)
    if len(left.pages) != len(right.pages):
        raise RuntimeError(f"PDF page count mismatch: {expected} vs {observed}")
    text_equal = 0
    stream_equal = 0
    geometry_equal = 0
    for index, (left_page, right_page) in enumerate(zip(left.pages, right.pages), start=1):
        if (left_page.extract_text() or "") != (right_page.extract_text() or ""):
            raise RuntimeError(f"PDF text mismatch on page {index}: {expected.name}")
        text_equal += 1
        if page_stream(left_page) != page_stream(right_page):
            raise RuntimeError(f"PDF content-stream mismatch on page {index}: {expected.name}")
        stream_equal += 1
        left_geometry = (tuple(left_page.mediabox), tuple(left_page.cropbox))
        right_geometry = (tuple(right_page.mediabox), tuple(right_page.cropbox))
        if left_geometry != right_geometry:
            raise RuntimeError(f"PDF geometry mismatch on page {index}: {expected.name}")
        geometry_equal += 1
    return {
        "pages": len(left.pages),
        "text_pages_exact": text_equal,
        "content_stream_pages_exact": stream_equal,
        "geometry_pages_exact": geometry_equal,
        "expected_sha256": base.sha256_path(expected),
        "rebuilt_sha256": base.sha256_path(observed),
    }


def render_pdf(pdftoppm: str, pdf: Path, output_dir: Path) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    prefix = output_dir / "page"
    run_command(
        [pdftoppm, "-r", "180", "-png", str(pdf), str(prefix)],
        output_dir,
        output_dir / "render.console.txt",
    )
    return sorted(output_dir.glob("page-*.png"))


def raster_compare(
    pdftoppm: str,
    expected: Path,
    observed: Path,
    raster_root: Path,
) -> dict[str, object]:
    expected_pngs = render_pdf(pdftoppm, expected, raster_root / "expected")
    observed_pngs = render_pdf(pdftoppm, observed, raster_root / "observed")
    if len(expected_pngs) != len(observed_pngs):
        raise RuntimeError(f"Raster page count mismatch: {expected.name}")
    mismatches = []
    for index, (left, right) in enumerate(zip(expected_pngs, observed_pngs), start=1):
        if base.sha256_path(left) != base.sha256_path(right):
            mismatches.append(index)
    if mismatches:
        raise RuntimeError(f"Raster mismatches for {expected.name}: {mismatches}")
    return {
        "dpi": 180,
        "pages": len(expected_pngs),
        "pixel_exact_pages": len(expected_pngs),
        "mismatches": [],
    }


def validate(args: argparse.Namespace) -> dict[str, object]:
    source_root = args.package_root.resolve()
    work_root = args.work_root.resolve()
    if work_root.exists():
        raise RuntimeError(f"Replay work root already exists: {work_root}")
    copied_root = work_root / "copied_package"
    shutil.copytree(source_root, copied_root)
    before_tree = [
        (path.relative_to(source_root).as_posix(), path.stat().st_size, base.sha256_path(path))
        for path in sorted(source_root.rglob("*"))
        if path.is_file()
    ]
    copied_tree = [
        (path.relative_to(copied_root).as_posix(), path.stat().st_size, base.sha256_path(path))
        for path in sorted(copied_root.rglob("*"))
        if path.is_file()
    ]
    if before_tree != copied_tree:
        raise RuntimeError("Copied package changed")

    outer_manifest = verify_manifest(
        copied_root,
        copied_root / "SHA256SUMS.csv",
        {"SHA256SUMS.csv", "PACKAGE_VALIDATION.json"},
    )
    outer_privacy = base.scan_privacy(copied_root)
    if outer_privacy:
        raise RuntimeError(f"Outer privacy scan failed: {outer_privacy[:3]}")
    outer_csv = verify_csvs(copied_root)
    outer_json = verify_json(copied_root)

    upload_fields, upload_rows = read_csv(copied_root / "ZENODO_UPLOAD_MANIFEST.csv")
    if upload_fields != ["filename", "bytes", "sha256", "role", "scope", "pages", "zenodo_action"]:
        raise RuntimeError("Upload manifest fields changed")
    upload_names = [row["filename"] for row in upload_rows]
    actual_upload_names = sorted(path.name for path in (copied_root / "public_files").iterdir() if path.is_file())
    if sorted(upload_names) != actual_upload_names or len(upload_rows) != 4:
        raise RuntimeError("Upload manifest closure failed")
    for row in upload_rows:
        base.require_identity(
            copied_root / "public_files" / row["filename"],
            (int(row["bytes"]), row["sha256"]),
        )

    zip_path = copied_root / "public_files/12_Deligne_D002_TeX_and_Decisive_Source_Crops_20260801.zip"
    extract_root = work_root / "extracted"
    with zipfile.ZipFile(zip_path) as archive:
        infos = [item for item in archive.infolist() if not item.is_dir()]
        names = [item.filename for item in infos]
        if (
            archive.testzip() is not None
            or len(names) != len(set(names))
            or not all(safe_member(name) for name in names)
        ):
            raise RuntimeError("ZIP safety/read gate failed")
        archive.extractall(extract_root)
    inner = extract_root / package.ZIP_ROOT
    inner_manifest = verify_manifest(
        inner,
        inner / "SHA256SUMS.csv",
        {"SHA256SUMS.csv", "PACKAGE_VALIDATION.json"},
    )
    inner_privacy = base.scan_privacy(inner)
    if inner_privacy:
        raise RuntimeError(f"Inner privacy scan failed: {inner_privacy[:3]}")
    inner_csv = verify_csvs(inner)
    inner_json = verify_json(inner)
    visual = verify_visual_ledger(inner)

    for public_name, (inner_relative, expected_pages) in PDF_EXPECTATIONS.items():
        outer_pdf = copied_root / "public_files" / public_name
        inner_pdf = inner / inner_relative
        if base.identity(outer_pdf) != base.identity(inner_pdf):
            raise RuntimeError(f"Outer/inner PDF identity mismatch: {public_name}")
        if len(PdfReader(outer_pdf).pages) != expected_pages:
            raise RuntimeError(f"PDF page count changed: {public_name}")

    rebuild = work_root / "rebuild"
    shutil.copytree(inner / "tex", rebuild / "tex")
    fr_pdf = build_tex(
        args.xelatex,
        rebuild / "tex",
        "D002_ProperSupport_FR_source_aligned.tex",
        rebuild / "build/fr_final",
        3,
    )
    en_pdf = build_tex(
        args.xelatex,
        rebuild / "tex",
        "D002_ProperSupport_EN_source_aligned.tex",
        rebuild / "build/en_final",
        3,
    )
    bilingual_pdf = build_tex(
        args.xelatex,
        rebuild / "tex",
        "D002_ProperSupport_Bilingual_Reader.tex",
        rebuild / "build/bilingual_source_aligned_eof_r1",
        4,
    )
    rebuilt = {
        "09_Deligne_D002_Bilingual_SourceAligned_Reader_20260801.pdf": bilingual_pdf,
        "10_Deligne_D002_English_SourceAligned_20260801.pdf": en_pdf,
        "11_Deligne_D002_French_SourceAligned_20260801.pdf": fr_pdf,
    }
    semantic_reports = {}
    raster_reports = {}
    for public_name, fresh_pdf in rebuilt.items():
        expected = copied_root / "public_files" / public_name
        semantic_reports[public_name] = pdf_semantic_compare(expected, fresh_pdf)
        raster_reports[public_name] = raster_compare(
            args.pdftoppm,
            expected,
            fresh_pdf,
            work_root / "rasters" / Path(public_name).stem,
        )

    after_tree = [
        (path.relative_to(source_root).as_posix(), path.stat().st_size, base.sha256_path(path))
        for path in sorted(source_root.rglob("*"))
        if path.is_file()
    ]
    if before_tree != after_tree:
        raise RuntimeError("Source package changed during replay")
    aggregate = hashlib.sha256()
    for relative, size, digest in before_tree:
        aggregate.update(f"{relative}\t{size}\t{digest}\n".encode("utf-8"))
    result = {
        "status": "PASS_MACHINE_EXACT_REPLAY__MANUAL_CONTACT_SHEET_REVIEW_PENDING",
        "scope": "Deligne D002 complete bilingual source-aligned working edition through EOF",
        "package_tree": {
            "files": len(before_tree),
            "bytes": sum(row[1] for row in before_tree),
            "ordinal_tab_aggregate_sha256": aggregate.hexdigest().upper(),
            "copied_exact": True,
            "pre_post_exact": True,
        },
        "outer_manifest": outer_manifest,
        "inner_manifest": inner_manifest,
        "zip": {
            "members": len(infos),
            "uncompressed_bytes": sum(item.file_size for item in infos),
            "safe_paths": True,
            "crc_read": "pass",
        },
        "upload_files": {
            "rows": len(upload_rows),
            "files_exact": len(upload_rows),
        },
        "csv": {"outer": outer_csv, "inner": inner_csv},
        "json": {"outer": outer_json, "inner": inner_json},
        "visual_evidence": visual,
        "fresh_builds": {"french_passes": 3, "english_passes": 3, "bilingual_passes": 4},
        "semantic_pdf_replay": semantic_reports,
        "raster_replay": raster_reports,
        "privacy_hits": [],
        "errors": [],
    }
    receipt = work_root / "MACHINE_REPLAY.json"
    base.write_json(receipt, result)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--package-root", type=Path, required=True)
    parser.add_argument("--work-root", type=Path, required=True)
    parser.add_argument("--xelatex", required=True)
    parser.add_argument("--pdftoppm", required=True)
    args = parser.parse_args()
    validate(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
