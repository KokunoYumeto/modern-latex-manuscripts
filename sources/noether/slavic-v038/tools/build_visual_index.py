#!/usr/bin/env python3
"""Build the schema-documented visual-evidence index and CSV projection."""

from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "release" / "evidence"
RENDER_MANIFEST = EVIDENCE / "visual_render_manifest.json"
REVIEW = EVIDENCE / "visual_review.json"
STRUCTURAL = EVIDENCE / "structural_index.jsonl"
OUTPUT = EVIDENCE / "visual_evidence_index.jsonl"
CSV_OUTPUT = EVIDENCE / "visual_evidence_index.csv"
REPORT = EVIDENCE / "visual_evidence_build_report.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def stable_id(image_hash: str) -> str:
    return f"SLISV-VIS-{image_hash[:12]}"


def structural_maps() -> tuple[dict, dict]:
    records = [json.loads(line) for line in STRUCTURAL.read_text(encoding="utf-8").splitlines() if line.strip()]
    unit_map = {}
    tex_map = {}
    for record in records:
        if record["structure_type"] != "work_unit":
            continue
        key = (record["language"], record["work_unit_id"])
        unit_map[key] = record["structural_id"]
        tex_map[key] = record["target_locator"]["path"]
    return unit_map, tex_map


def target_language(target: str) -> str:
    return {"ru": "ru-Cyrl", "uk": "uk-Cyrl", "isv": "isv-Latn", "isv-cy": "isv-Cyrl"}[target]


def main() -> int:
    render_manifest = json.loads(RENDER_MANIFEST.read_text(encoding="utf-8"))
    review = json.loads(REVIEW.read_text(encoding="utf-8")) if REVIEW.exists() else {"records": []}
    reviews = {record["image_sha256"]: record for record in review.get("records", [])}
    unit_map, tex_map = structural_maps()
    records = []
    for item in render_manifest["render_records"]:
        target = item["target"]
        image_hash = item["image"]["sha256"]
        review_record = reviews.get(image_hash)
        pdf_path = Path(item["parent_pdf"]["path"])
        page = item["page"]
        reader_page = PdfReader(str(pdf_path)).pages[page - 1]
        width_points = float(reader_page.mediabox.width)
        height_points = float(reader_page.mediabox.height)
        work_units = item["linked_work_unit"].split("|")
        language = target_language(target)
        linked_ids = [unit_map[(language, unit)] for unit in work_units if (language, unit) in unit_map]
        linked_tex = sorted({tex_map[(language, unit)] for unit in work_units if (language, unit) in tex_map})
        records.append(
            {
                "schema_version": "noether-slavic-v038-visual-evidence/1.0",
                "visual_id": stable_id(image_hash),
                "visual_type": "target_page_render",
                "target": target,
                "image": item["image"],
                "parent_pdf": item["parent_pdf"],
                "parent_image_hashes": [],
                "page_number": page,
                "page_coordinates_points": [0.0, 0.0, width_points, height_points],
                "bounding_box_pixels": [0, 0, item["render"]["width_px"], item["render"]["height_px"]],
                "dimensions": {"width_px": item["render"]["width_px"], "height_px": item["render"]["height_px"]},
                "dpi": item["render"]["dpi"],
                "rotation_degrees": item["render"]["rotation_degrees"],
                "linked_work_units": work_units,
                "linked_structural_ids": linked_ids,
                "linked_tex_paths": linked_tex,
                "qa_state": review_record["qa_state"] if review_record else item["qa_state"],
                "review_evidence": review_record,
                "rights_basis": item["rights_basis"],
                "publication_disposition": item["publication_disposition"],
                "continuation_cursor": None,
            }
        )
    for item in render_manifest["contact_records"]:
        target = item["target"]
        image_hash = item["image"]["sha256"]
        review_record = reviews.get(image_hash)
        records.append(
            {
                "schema_version": "noether-slavic-v038-visual-evidence/1.0",
                "visual_id": stable_id(image_hash),
                "visual_type": "contact_sheet",
                "target": target,
                "image": item["image"],
                "parent_pdf": None,
                "parent_image_hashes": item["child_images"],
                "page_number": None,
                "page_coordinates_points": None,
                "bounding_box_pixels": [0, 0, item["render"]["width_px"], item["render"]["height_px"]],
                "dimensions": {"width_px": item["render"]["width_px"], "height_px": item["render"]["height_px"]},
                "dpi": item["render"]["dpi"],
                "rotation_degrees": item["render"]["rotation_degrees"],
                "linked_work_units": [],
                "linked_structural_ids": [],
                "linked_tex_paths": [],
                "qa_state": review_record["qa_state"] if review_record else item["qa_state"],
                "review_evidence": review_record,
                "rights_basis": item["rights_basis"],
                "publication_disposition": item["publication_disposition"],
                "continuation_cursor": None,
            }
        )
    for item in render_manifest.get("source_records", []):
        image_hash = item["image"]["sha256"]
        review_record = reviews.get(image_hash)
        pdf_path = Path(item["parent_pdf"]["path"])
        page = item["page"]
        reader_page = PdfReader(str(pdf_path)).pages[page - 1]
        width_points = float(reader_page.mediabox.width)
        height_points = float(reader_page.mediabox.height)
        work_units = item["linked_work_unit"].split("|")
        records.append(
            {
                "schema_version": "noether-slavic-v038-visual-evidence/1.0",
                "visual_id": stable_id(image_hash),
                "visual_type": "source_page_render",
                "target": "de-source",
                "image": item["image"],
                "parent_pdf": item["parent_pdf"],
                "parent_image_hashes": [],
                "page_number": page,
                "page_coordinates_points": [0.0, 0.0, width_points, height_points],
                "bounding_box_pixels": [0, 0, item["render"]["width_px"], item["render"]["height_px"]],
                "dimensions": {
                    "width_px": item["render"]["width_px"],
                    "height_px": item["render"]["height_px"],
                },
                "dpi": item["render"]["dpi"],
                "rotation_degrees": item["render"]["rotation_degrees"],
                "linked_work_units": work_units,
                "linked_structural_ids": [],
                "linked_tex_paths": [],
                "qa_state": review_record["qa_state"] if review_record else item["qa_state"],
                "review_evidence": review_record,
                "rights_basis": item["rights_basis"],
                "publication_disposition": item["publication_disposition"],
                "continuation_cursor": None,
            }
        )
    records.sort(key=lambda record: (record["target"], record["visual_type"], record["page_number"] or 0))
    for index, record in enumerate(records):
        record["continuation_cursor"] = records[index + 1]["visual_id"] if index + 1 < len(records) else None
    with OUTPUT.open("w", encoding="utf-8", newline="\n") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")

    fields = [
        "visual_id", "visual_type", "target", "image_path", "image_bytes", "image_sha256",
        "parent_pdf_path", "parent_pdf_sha256", "page_number", "width_px", "height_px", "dpi",
        "rotation_degrees", "linked_work_units", "linked_structural_ids", "qa_state", "rights_basis",
        "publication_disposition", "continuation_cursor",
    ]
    with CSV_OUTPUT.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for record in records:
            parent = record["parent_pdf"] or {}
            writer.writerow(
                {
                    "visual_id": record["visual_id"],
                    "visual_type": record["visual_type"],
                    "target": record["target"],
                    "image_path": record["image"]["path"],
                    "image_bytes": record["image"]["bytes"],
                    "image_sha256": record["image"]["sha256"],
                    "parent_pdf_path": parent.get("path", ""),
                    "parent_pdf_sha256": parent.get("sha256", ""),
                    "page_number": record["page_number"] or "",
                    "width_px": record["dimensions"]["width_px"],
                    "height_px": record["dimensions"]["height_px"],
                    "dpi": record["dpi"],
                    "rotation_degrees": record["rotation_degrees"],
                    "linked_work_units": "|".join(record["linked_work_units"]),
                    "linked_structural_ids": "|".join(record["linked_structural_ids"]),
                    "qa_state": record["qa_state"],
                    "rights_basis": record["rights_basis"],
                    "publication_disposition": record["publication_disposition"],
                    "continuation_cursor": record["continuation_cursor"] or "",
                }
            )
    report = {
        "schema": "noether-slavic-v038-visual-evidence-build-report/1.0",
        "generated_at": datetime.now().astimezone().isoformat(),
        "record_count": len(records),
        "page_render_count": sum(record["visual_type"] == "target_page_render" for record in records),
        "contact_sheet_count": sum(record["visual_type"] == "contact_sheet" for record in records),
        "source_page_render_count": sum(
            record["visual_type"] == "source_page_render" for record in records
        ),
        "reviewed_pass_count": sum(record["qa_state"] == "visually_reopened_pass" for record in records),
        "rights_disposition": (
            "target renders/contact sheets are project-generated with underlying-text publication left to the owner; "
            "the source-page render is preserved rights-blocked and only its public-safe metadata/hash/coordinate layer is proposed"
        ),
        "outputs": {
            "jsonl": {"path": OUTPUT.resolve().as_posix(), "bytes": OUTPUT.stat().st_size, "sha256": sha256(OUTPUT)},
            "csv": {"path": CSV_OUTPUT.resolve().as_posix(), "bytes": CSV_OUTPUT.stat().st_size, "sha256": sha256(CSV_OUTPUT)},
        },
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({**report, "report_sha256": sha256(REPORT)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
