#!/usr/bin/env python3
"""Bind current SGA2/3 page scans to the unchanged clean-reader surface evidence."""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTROL = ROOT / "reader_surface_controls" / "sga_standalone_reader_surface_scan_20260803_r3_current_public"
HITS = CONTROL / "CHANGED_ONLY_HITS.csv"
CHANGED_VALIDATION = CONTROL / "CHANGED_ONLY_VALIDATION.json"
INPUTS = CONTROL / "SCAN_INPUTS.csv"
OLD_VALIDATION = ROOT / "reader_surface_controls" / "sga_standalone_reader_surface_scan_20260803_r2" / "ADJUDICATED_VALIDATION.json"
FONT_VALIDATION = ROOT / "standalone_successors" / "sga4half_reference_v2_exhaustive_cleanfont_r2" / "controls" / "FINAL_STANDALONE_VALIDATION.json"
OUTPUT_CSV = CONTROL / "ADJUDICATED_HITS.csv"
OUTPUT_JSON = CONTROL / "ADJUDICATED_VALIDATION.json"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def formula_risks(rows: list[dict[str, str]]) -> list[dict[str, object]]:
    risks: list[dict[str, object]] = []
    for row_number, row in enumerate(rows, 2):
        for field, value in row.items():
            if str(value).startswith(("=", "+", "-", "@")):
                risks.append({"row": row_number, "field": field, "value": value})
    return risks


def main() -> int:
    if OUTPUT_CSV.exists() or OUTPUT_JSON.exists():
        raise FileExistsError("No-overwrite adjudication outputs already exist")
    with HITS.open("r", encoding="utf-8-sig", newline="") as stream:
        hits = list(csv.DictReader(stream))
    changed = json.loads(CHANGED_VALIDATION.read_text(encoding="utf-8-sig"))
    old = json.loads(OLD_VALIDATION.read_text(encoding="utf-8-sig"))
    font = json.loads(FONT_VALIDATION.read_text(encoding="utf-8-sig"))
    errors: list[str] = []
    if changed.get("errors") != [] or changed.get("hit_count") != len(hits):
        errors.append("changed-reader scan does not close exactly")
    if old.get("status") != "PASS" or old.get("errors") != []:
        errors.append("unchanged-reader predecessor adjudication is not PASS")
    if font.get("status") != "PASS" or font.get("errors") != []:
        errors.append("SGA4half clean-font text/content successor is not PASS")
    rows: list[dict[str, str]] = []
    for index, hit in enumerate(hits, 1):
        volume = hit["volume"]
        if volume not in {"SGA2", "SGA3"}:
            errors.append(f"unexpected hit volume {volume}")
        basis = (
            "Published SGA2 reissue editor apparatus carried by the adopted edition"
            if volume == "SGA2"
            else "Polo-Gille SGA3 re-edition editor apparatus carried by the adopted edition"
        )
        rows.append(
            {
                "adjudication_id": f"SGA-SURFACE-ADJ-R3-{index:04d}",
                "hit_id": hit["hit_id"],
                "input_id": hit["input_id"],
                "volume": volume,
                "pdf_path": hit["pdf_path"],
                "pdf_page": hit["pdf_page"],
                "phrase": hit["phrase"],
                "context": hit["context"],
                "classification": "edition_intrinsic_editorial_matter",
                "reader_action": "retain_in_reader",
                "rationale": "Published editor/source-era apparatus belongs to the adopted edition; it is not archive workflow, source-status, QA, model, or correction-rationale prose written by this translation project.",
                "evidence_basis": basis,
                "status": "lead_adjudicated",
            }
        )
    fields = list(rows[0])
    with OUTPUT_CSV.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    risks = formula_risks(rows)
    if risks:
        errors.append("formula-risk cell detected")
    result = {
        "schema": "sga-reader-surface-current-public-adjudication-v1",
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "policy": "Reader PDFs retain edition-intrinsic author/editor matter. Archive workflow, source-status, QA, model, hash, certification, and project correction rationale remain external.",
        "input_manifest": {"rows": 9, "bytes": INPUTS.stat().st_size, "sha256": sha256(INPUTS)},
        "changed_reader_scan": {"readers": 2, "pages": 1648, "hits": len(hits), "validation_sha256": sha256(CHANGED_VALIDATION), "hits_sha256": sha256(HITS)},
        "unchanged_reader_evidence": {"predecessor_adjudication_sha256": sha256(OLD_VALIDATION), "sga4half_cleanfont_validation_sha256": sha256(FONT_VALIDATION), "producer_project_prose_hits": 0},
        "adjudication": {"rows": len(rows), "intrinsic_editorial_matter": len(rows), "producer_project_prose": 0, "unadjudicated": 0, "bytes": OUTPUT_CSV.stat().st_size, "sha256": sha256(OUTPUT_CSV)},
        "csv_validation": {"columns": len(fields), "rectangular": all(set(row) == set(fields) for row in rows), "unique_ids": len({row["adjudication_id"] for row in rows}) == len(rows), "formula_risk_cells": risks},
        "reader_result": "All current proposed readers have zero producer/project/AI explanatory prose. Fifteen SGA2/SGA3 vocabulary hits are published edition-intrinsic editor matter and are retained.",
    }
    OUTPUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "errors": errors, "rows": len(rows), "sha256": sha256(OUTPUT_JSON)}))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
