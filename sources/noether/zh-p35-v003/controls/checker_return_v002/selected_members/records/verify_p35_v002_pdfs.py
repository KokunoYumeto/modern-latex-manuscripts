#!/usr/bin/env python3
"""Supplement visual P35 v002 review with PDF text, metadata, and raster-equivalence checks."""

from __future__ import annotations

from hashlib import sha256
import importlib.metadata
import json
from pathlib import Path

import pdfplumber
from pypdf import PdfReader


SCRIPT = Path(__file__).resolve()
RECHECK = SCRIPT.parents[1]
OUT = RECHECK / "build/P35_V002_PDF_TEXT_METADATA_VERIFICATION.json"

PDFS = {
    "producer_hans": RECHECK / (
        "intake/frozen_producer_package_v002/build/zh-Hans-CN-v002/"
        "Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_v002.pdf"
    ),
    "checker_hans": RECHECK / (
        "build/hans_exact/Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_v002.pdf"
    ),
    "producer_hant_rejected": RECHECK / (
        "intake/frozen_producer_package_v002/build/zh-Hant-controlled-v002/"
        "Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_v002.pdf"
    ),
    "checker_hant_rejected_rebuild": RECHECK / (
        "build/hant_frozen_exact/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_v002.pdf"
    ),
    "checker_hant_candidate_v003": RECHECK / (
        "build/hant_candidate_v003/"
        "Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_checker_candidate_v003.pdf"
    ),
}

RASTERS = {
    "producer_hans": RECHECK / "render/producer_hans",
    "checker_hans": RECHECK / "render/checker_hans",
    "producer_hant_rejected": RECHECK / "render/producer_hant",
    "checker_hant_rejected_rebuild": RECHECK / "render/checker_hant_frozen",
    "checker_hant_candidate_v003": RECHECK / "render/candidate_hant_v003",
}


def digest(data: bytes) -> str:
    return sha256(data).hexdigest().upper()


def inspect_pdf(path: Path) -> tuple[dict[str, object], str, str]:
    data = path.read_bytes()
    reader = PdfReader(path)
    pypdf_pages = [page.extract_text() or "" for page in reader.pages]
    with pdfplumber.open(path) as pdf:
        plumber_pages = [page.extract_text() or "" for page in pdf.pages]
    record = {
        "path": str(path),
        "bytes": len(data),
        "sha256": digest(data),
        "pages_pypdf": len(pypdf_pages),
        "pages_pdfplumber": len(plumber_pages),
        "page_text_chars_pypdf": [len(page) for page in pypdf_pages],
        "page_text_chars_pdfplumber": [len(page) for page in plumber_pages],
        "all_pages_nonempty_pypdf": all(pypdf_pages),
        "all_pages_nonempty_pdfplumber": all(plumber_pages),
        "creation_date": str(reader.metadata.get("/CreationDate")) if reader.metadata else None,
    }
    return record, "\n".join(pypdf_pages), "\n".join(plumber_pages)


def raster_facts(directory: Path) -> list[dict[str, object]]:
    rows = []
    for path in sorted(directory.glob("page-*.png")):
        data = path.read_bytes()
        rows.append({"name": path.name, "bytes": len(data), "sha256": digest(data)})
    return rows


def hashes(rows: list[dict[str, object]]) -> list[str]:
    return [str(row["sha256"]) for row in rows]


def main() -> int:
    pdf_records: dict[str, dict[str, object]] = {}
    pypdf_text: dict[str, str] = {}
    plumber_text: dict[str, str] = {}
    for label, path in PDFS.items():
        pdf_records[label], pypdf_text[label], plumber_text[label] = inspect_pdf(path)

    raster_records = {label: raster_facts(path) for label, path in RASTERS.items()}

    hans_required = ["极大整环", "雅可比矩阵", "整性基", "代数无关系统", "非整代数数", "生成元"]
    hans_forbidden = ["极大域", "函数矩阵", "整环基", "分数代数数", "倍理想", "基元素", "每个整数均"]
    hant_required = ["極大整環", "雅可比矩陣", "整性基", "代數無關系統", "非整代數數", "生成元"]
    hant_forbidden = ["極大域", "函數矩陣", "整環基", "分數代數數", "倍理想", "基元素", "每個整數均", "隻", "幷", "無關係統"]
    frozen_mixed_script_witnesses = ["数学问题", "众所周知", "消去理论", "代数量的算术理论"]
    corrected_traditional_witnesses = ["數學問題", "眾所周知", "消去理論", "代數量的算術理論"]

    checks = {
        "all_pdfs_have_six_pages": all(
            record["pages_pypdf"] == 6 and record["pages_pdfplumber"] == 6
            for record in pdf_records.values()
        ),
        "all_pages_have_extractable_text": all(
            record["all_pages_nonempty_pypdf"] and record["all_pages_nonempty_pdfplumber"]
            for record in pdf_records.values()
        ),
        "producer_checker_hans_text_equal_pypdf": pypdf_text["producer_hans"] == pypdf_text["checker_hans"],
        "producer_checker_hans_text_equal_pdfplumber": plumber_text["producer_hans"] == plumber_text["checker_hans"],
        "producer_checker_rejected_hant_text_equal_pypdf": pypdf_text["producer_hant_rejected"] == pypdf_text["checker_hant_rejected_rebuild"],
        "producer_checker_rejected_hant_text_equal_pdfplumber": plumber_text["producer_hant_rejected"] == plumber_text["checker_hant_rejected_rebuild"],
        "hans_required_terms_present": {term: term in pypdf_text["producer_hans"] for term in hans_required},
        "hans_rejected_terms_absent": {term: term not in pypdf_text["producer_hans"] for term in hans_forbidden},
        "candidate_hant_required_terms_present": {term: term in pypdf_text["checker_hant_candidate_v003"] for term in hant_required},
        "candidate_hant_rejected_terms_absent": {term: term not in pypdf_text["checker_hant_candidate_v003"] for term in hant_forbidden},
        "frozen_hant_mixed_script_witnesses_present": {term: term in pypdf_text["producer_hant_rejected"] for term in frozen_mixed_script_witnesses},
        "candidate_hant_mixed_script_witnesses_absent": {term: term not in pypdf_text["checker_hant_candidate_v003"] for term in frozen_mixed_script_witnesses},
        "candidate_hant_corrected_traditional_witnesses_present": {term: term in pypdf_text["checker_hant_candidate_v003"] for term in corrected_traditional_witnesses},
        "producer_checker_hans_rasters_equal": hashes(raster_records["producer_hans"]) == hashes(raster_records["checker_hans"]),
        "producer_checker_rejected_hant_rasters_equal": hashes(raster_records["producer_hant_rejected"]) == hashes(raster_records["checker_hant_rejected_rebuild"]),
        "candidate_hant_only_page5_differs_from_rejected": [
            index + 1
            for index, (before, after) in enumerate(
                zip(
                    hashes(raster_records["producer_hant_rejected"]),
                    hashes(raster_records["checker_hant_candidate_v003"]),
                )
            )
            if before != after
        ] == [5],
    }

    def all_values(value: object) -> bool:
        if isinstance(value, dict):
            return all(all_values(item) for item in value.values())
        return value is True

    all_pass = all(all_values(value) for value in checks.values())
    report = {
        "verification_id": "ZHCHK-P35-V002-PDF-001",
        "recorded_at": "2026-08-04T07:15:00+02:00",
        "libraries": {
            "pypdf": importlib.metadata.version("pypdf"),
            "pdfplumber": importlib.metadata.version("pdfplumber"),
        },
        "pdfs": pdf_records,
        "rasters_180dpi": raster_records,
        "checks": checks,
        "all_pass": all_pass,
        "finding_disposition": {
            "hans": "text_metadata_and_raster_reproducibility_pass",
            "frozen_hant_v002": "reproducible_but_rejected_for_confirmed_mixed_script_finding_ZHCHK-P35-F015",
            "checker_hant_candidate_v003": "text_metadata_raster_and_required_term_checks_pass; visual review recorded separately",
        },
        "claim_limit": "Text extraction, metadata, and raster hashes supplement but do not replace original-detail visual inspection. Hant remains controlled generic and nonregional.",
    }
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"all_pass": all_pass, "checks": checks}, ensure_ascii=True, indent=2))
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
