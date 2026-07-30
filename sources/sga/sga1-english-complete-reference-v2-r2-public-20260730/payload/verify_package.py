#!/usr/bin/env python3
"""Read-only verifier for the complete SGA 1 reference-v2 package."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from pathlib import Path

from pypdf import PdfReader


EXCLUDED_FROM_MANIFEST = {
    "ZENODO_PAYLOAD_MANIFEST.csv",
    "PACKAGE_VALIDATION.json",
}
PRIVATE_PATTERNS = {
    "windows_user_path_backslash": re.compile(rb"[A-Za-z]:\\Users\\[^\\\r\n]+"),
    "windows_user_path_slash": re.compile(rb"[A-Za-z]:/Users/[^/\r\n]+"),
    "posix_home_path": re.compile(rb"/" + rb"home/" + rb"[^/\r\n]+"),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> int:
    root = Path(__file__).resolve().parent
    errors: list[str] = []
    manifest_path = root / "ZENODO_PAYLOAD_MANIFEST.csv"
    if not manifest_path.exists():
        raise SystemExit("ZENODO_PAYLOAD_MANIFEST.csv is missing")
    manifest = read_csv(manifest_path)
    manifest_by_path = {row["relative_path"]: row for row in manifest}
    if len(manifest_by_path) != len(manifest):
        errors.append("manifest has duplicate relative paths")
    actual_paths = {
        path.relative_to(root).as_posix()
        for path in root.rglob("*")
        if path.is_file()
        and path.relative_to(root).as_posix() not in EXCLUDED_FROM_MANIFEST
    }
    manifest_paths = set(manifest_by_path)
    if actual_paths != manifest_paths:
        errors.append(
            "manifest exact-set mismatch: "
            f"missing={sorted(actual_paths - manifest_paths)[:20]}, "
            f"extra={sorted(manifest_paths - actual_paths)[:20]}"
        )
    replay_errors: list[str] = []
    for relative_path, row in manifest_by_path.items():
        path = root / relative_path
        if not path.exists():
            replay_errors.append(f"missing:{relative_path}")
            continue
        if path.stat().st_size != int(row["bytes"]):
            replay_errors.append(f"size:{relative_path}")
        if sha256(path) != row["sha256"]:
            replay_errors.append(f"hash:{relative_path}")
    if replay_errors:
        errors.append(f"manifest replay errors: {replay_errors[:30]}")

    csv_errors: list[str] = []
    json_errors: list[str] = []
    for path in sorted(root.rglob("*.csv")):
        try:
            rows = read_csv(path)
            if rows:
                expected = set(rows[0])
                if any(set(row) != expected for row in rows):
                    csv_errors.append(f"nonrectangular:{path.relative_to(root)}")
            for row_number, row in enumerate(rows, 2):
                for column, value in row.items():
                    if value.startswith(("=", "+", "-", "@")):
                        csv_errors.append(
                            f"formula-unsafe:{path.relative_to(root)}:{row_number}:{column}"
                        )
        except Exception as exc:
            csv_errors.append(f"parse:{path.relative_to(root)}:{exc}")
    for path in sorted(root.rglob("*.json")):
        try:
            json.loads(path.read_text(encoding="utf-8-sig"))
        except Exception as exc:
            json_errors.append(f"parse:{path.relative_to(root)}:{exc}")
    if csv_errors:
        errors.append(f"CSV validation errors: {csv_errors[:30]}")
    if json_errors:
        errors.append(f"JSON validation errors: {json_errors[:30]}")

    targets = read_csv(root / "controls" / "REFERENCE_TARGETS.csv")
    edges = read_csv(root / "controls" / "REFERENCE_EDGES.csv")
    candidates = read_csv(root / "controls" / "REFERENCE_CANDIDATES.csv")
    applications = read_csv(root / "controls" / "REFERENCE_APPLICATIONS.csv")
    residuals = read_csv(root / "controls" / "REFERENCE_RESIDUALS.csv")
    target_ids = {row["target_id"] for row in targets}
    candidate_ids = {row["candidate_id"] for row in candidates}
    application_candidates = {row["candidate_id"] for row in applications}
    residual_candidates = {row["candidate_id"] for row in residuals}
    if len(target_ids) != 933 or len(targets) != 933:
        errors.append("target count/uniqueness is not 933")
    if len(edges) != 1600 or len({row["edge_id"] for row in edges}) != 1600:
        errors.append("edge count/uniqueness is not 1600")
    if {row["target_id"] for row in edges} - target_ids:
        errors.append("edge target closure failed")
    if len(applications) != 31 or len(residuals) != 189:
        errors.append("candidate partition counts are not 31/189")
    if application_candidates & residual_candidates:
        errors.append("candidate partition overlaps")
    if application_candidates | residual_candidates != candidate_ids:
        errors.append("candidate partition does not cover the candidate universe")

    pdf_path = root / "SGA1_English_complete_reference_reader.pdf"
    reader = PdfReader(str(pdf_path))
    named = reader.named_destinations
    goto_count = 0
    broken: list[tuple[int, str]] = []
    external_actions: list[tuple[int, str]] = []
    for page_number, page in enumerate(reader.pages, 1):
        for annotation_ref in page.get("/Annots", []):
            annotation = annotation_ref.get_object()
            action_ref = annotation.get("/A")
            if action_ref is None:
                continue
            action = action_ref.get_object()
            action_type = str(action.get("/S", ""))
            if action_type == "/GoTo":
                goto_count += 1
                destination = str(action.get("/D"))
                if destination not in named:
                    broken.append((page_number, destination))
            elif action_type:
                external_actions.append((page_number, action_type))
    if len(reader.pages) != 262:
        errors.append("PDF page count is not 262")
    if len(named) != 2151:
        errors.append("PDF named-destination count is not 2151")
    if goto_count != 1600 or broken:
        errors.append(f"PDF GoTo closure failed: count={goto_count}, broken={broken[:20]}")
    if external_actions:
        errors.append(f"external/active PDF actions remain: {external_actions[:20]}")

    privacy_hits: list[dict] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        data = path.read_bytes()
        for name, pattern in PRIVATE_PATTERNS.items():
            count = len(pattern.findall(data))
            if count:
                privacy_hits.append(
                    {
                        "path": path.relative_to(root).as_posix(),
                        "pattern": name,
                        "count": count,
                    }
                )
    if privacy_hits:
        errors.append(f"privacy hits remain: {privacy_hits[:20]}")

    result = {
        "schema": "sga1-complete-reference-package-validation-1.0",
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "package": {
            "manifest_rows": len(manifest),
            "manifest_sha256": sha256(manifest_path),
            "manifest_replay_errors": replay_errors,
            "excluded_controls": sorted(EXCLUDED_FROM_MANIFEST),
        },
        "reference_graph": {
            "targets": len(targets),
            "edges": len(edges),
            "candidates": len(candidates),
            "applications": len(applications),
            "residuals": len(residuals),
        },
        "reader": {
            "bytes": pdf_path.stat().st_size,
            "sha256": sha256(pdf_path),
            "pages": len(reader.pages),
            "named_destinations": len(named),
            "goto_actions": goto_count,
            "broken_goto_actions": len(broken),
            "external_or_active_actions": len(external_actions),
        },
        "csv_errors": csv_errors,
        "json_errors": json_errors,
        "privacy_hits": privacy_hits,
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
