#!/usr/bin/env python3
"""Read-only exact-set verifier for the EGA II reference-v2 package."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

from pypdf import PdfReader


EXCLUDED_FROM_MANIFEST = {"ZENODO_PAYLOAD_MANIFEST.csv", "PACKAGE_VALIDATION.json"}
PRIVATE_PATTERNS = {
    "windows_user_path_backslash": re.compile(rb"[A-Za-z]:\\Users\\[^\\\r\n]+"),
    "windows_user_path_slash": re.compile(rb"[A-Za-z]:/Users/[^/\r\n]+"),
    "posix_home_path": re.compile(rb"/" + rb"home/" + rb"[^/\r\n]+"),
}
CORE_IDS = {
    "REFERENCE_TARGETS.csv": ("target_id", 1028),
    "REFERENCE_EDGES.csv": ("edge_id", 2078),
    "REFERENCE_CANDIDATES.csv": ("candidate_id", 921),
    "REFERENCE_APPLICATIONS.csv": ("application_id", 264),
    "REFERENCE_RESIDUALS.csv": ("residual_id", 657),
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


def inspect_pdf(path: Path) -> dict[str, object]:
    reader = PdfReader(str(path))
    named = reader.named_destinations
    goto = 0
    broken: list[tuple[int, str]] = []
    non_goto: list[tuple[int, str]] = []
    direct_destinations = 0
    subtype_counts: Counter[str] = Counter()
    fonts: dict[tuple[int, int], object] = {}
    images: set[tuple[int, int]] = set()
    forms_seen: set[tuple[int, int]] = set()

    def key(obj: object) -> tuple[int, int]:
        ref = getattr(obj, "indirect_reference", None)
        return (ref.idnum, ref.generation) if ref is not None else (id(obj), 0)

    def dereference(value: object) -> object:
        getter = getattr(value, "get_object", None)
        return getter() if getter is not None else value

    def walk_resources(resources_ref: object | None) -> None:
        if resources_ref is None:
            return
        resources = dereference(resources_ref)
        for font_ref in dereference(resources.get("/Font", {})).values():
            font = dereference(font_ref)
            fonts[key(font)] = font
        for xobject_ref in dereference(resources.get("/XObject", {})).values():
            xobject = dereference(xobject_ref)
            object_key = key(xobject)
            subtype = str(xobject.get("/Subtype", ""))
            if subtype == "/Image":
                images.add(object_key)
            elif subtype == "/Form" and object_key not in forms_seen:
                forms_seen.add(object_key)
                walk_resources(xobject.get("/Resources"))

    for page_number, page in enumerate(reader.pages, 1):
        walk_resources(page.get("/Resources"))
        for annotation_ref in page.get("/Annots", []):
            annotation = dereference(annotation_ref)
            subtype_counts[str(annotation.get("/Subtype", ""))] += 1
            if annotation.get("/Dest") is not None:
                direct_destinations += 1
            action_ref = annotation.get("/A")
            if action_ref is None:
                continue
            action = dereference(action_ref)
            action_type = str(action.get("/S", ""))
            if action_type == "/GoTo":
                goto += 1
                destination = str(action.get("/D"))
                if destination not in named:
                    broken.append((page_number, destination))
            else:
                non_goto.append((page_number, action_type))

    type3 = 0
    unembedded: list[str] = []
    subset = 0
    to_unicode = 0
    for font in fonts.values():
        subtype = str(font.get("/Subtype", ""))
        base_name = str(font.get("/BaseFont", "<unnamed>"))
        if subtype == "/Type3":
            type3 += 1
        if re.search(r"/[A-Z]{6}\+", base_name):
            subset += 1
        if font.get("/ToUnicode") is not None:
            to_unicode += 1
        if subtype == "/Type0":
            descendants = dereference(font.get("/DescendantFonts", []))
            descriptor = (
                dereference(descendants[0]).get("/FontDescriptor")
                if descendants
                else None
            )
        else:
            descriptor = font.get("/FontDescriptor")
        descriptor = None if descriptor is None else dereference(descriptor)
        embedded = descriptor is not None and any(
            descriptor.get(name) is not None
            for name in ("/FontFile", "/FontFile2", "/FontFile3")
        )
        if not embedded:
            unembedded.append(base_name)

    return {
        "pages": len(reader.pages),
        "metadata": {
            key: str(value) for key, value in (reader.metadata or {}).items()
        },
        "named_destinations": len(named),
        "goto_actions": goto,
        "broken_goto_actions": broken,
        "non_goto_actions": non_goto,
        "direct_destinations": direct_destinations,
        "annotation_subtypes": dict(sorted(subtype_counts.items())),
        "font_objects": len(fonts),
        "subset_fonts": subset,
        "fonts_with_to_unicode": to_unicode,
        "type3_fonts": type3,
        "unembedded_fonts": sorted(unembedded),
        "image_xobjects": len(images),
        "form_xobjects": len(forms_seen),
    }


def main() -> int:
    root = Path(__file__).resolve().parent
    output = (
        Path(sys.argv[1]).resolve()
        if len(sys.argv) > 1
        else root / "PACKAGE_VALIDATION.json"
    )
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
    for path in sorted(root.rglob("*.csv")):
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            raw_rows = list(csv.reader(handle))
        if not raw_rows:
            csv_errors.append(f"empty:{path.relative_to(root)}")
            continue
        width = len(raw_rows[0])
        if any(len(row) != width for row in raw_rows):
            csv_errors.append(f"nonrectangular:{path.relative_to(root)}")
        for row_number, row in enumerate(raw_rows[1:], 2):
            for column_number, value in enumerate(row, 1):
                if value.startswith(("=", "+", "-", "@")):
                    csv_errors.append(
                        f"formula-unsafe:{path.relative_to(root)}:"
                        f"{row_number}:{column_number}"
                    )
    if csv_errors:
        errors.append(f"CSV errors: {csv_errors[:30]}")

    ledgers: dict[str, list[dict[str, str]]] = {}
    for name, (id_field, expected_count) in CORE_IDS.items():
        rows = read_csv(root / "controls" / name)
        ledgers[name] = rows
        ids = [row[id_field] for row in rows]
        if len(rows) != expected_count or len(set(ids)) != expected_count:
            errors.append(f"{name} count/ID uniqueness differs")
    targets = {row["target_id"] for row in ledgers["REFERENCE_TARGETS.csv"]}
    edges = ledgers["REFERENCE_EDGES.csv"]
    candidates = {
        row["candidate_id"] for row in ledgers["REFERENCE_CANDIDATES.csv"]
    }
    applications = {
        row["candidate_id"] for row in ledgers["REFERENCE_APPLICATIONS.csv"]
    }
    residuals = {
        row["candidate_id"] for row in ledgers["REFERENCE_RESIDUALS.csv"]
    }
    if {row["target_id"] for row in edges} - targets:
        errors.append("edge target closure failed")
    if applications & residuals or applications | residuals != candidates:
        errors.append("candidate partition failed")

    source_closure = read_csv(root / "controls" / "SOURCE_CLOSURE.csv")
    source_errors: list[str] = []
    for row in source_closure:
        path = root / "source" / row["relative_path"]
        if not path.exists():
            source_errors.append(f"missing:{row['relative_path']}")
            continue
        if path.stat().st_size != int(row["bytes"]):
            source_errors.append(f"size:{row['relative_path']}")
        if sha256(path) != row["sha256"]:
            source_errors.append(f"hash:{row['relative_path']}")
    if source_errors:
        errors.append(f"source closure failed: {source_errors[:20]}")

    json_errors: list[str] = []
    required_pass_json = [
        "controls/FINAL_READER_VALIDATION.json",
        "controls/REFERENCE_CANDIDATE_PARTITION_VALIDATION.json",
        "controls/REFERENCE_GRAPH_VALIDATION.json",
        "controls/SOURCE_PRESERVATION_VALIDATION.json",
        "controls/VISUAL_QA_VALIDATION.json",
    ]
    for relative_path in required_pass_json:
        value = json.loads((root / relative_path).read_text(encoding="utf-8-sig"))
        if value.get("status") != "PASS" or value.get("errors"):
            json_errors.append(f"not-clean-PASS:{relative_path}")
    if json_errors:
        errors.append(f"JSON control errors: {json_errors}")

    pdf_path = root / "EGA2_English_complete_reference_reader.pdf"
    pdf = inspect_pdf(pdf_path)
    expected_metadata = {
        "/Title": (
            "EGA II: Elementary Global Study of Some Classes of Morphisms "
            "– English Translation"
        ),
        "/Author": "Alexander Grothendieck and Jean Dieudonne; English translation",
        "/Subject": "Complete source-aligned English reader of EGA II",
    }
    for key, value in expected_metadata.items():
        if pdf["metadata"].get(key) != value:
            errors.append(f"PDF metadata mismatch: {key}")
    if pdf["pages"] != 165:
        errors.append("PDF page count differs")
    if pdf["named_destinations"] != 2538:
        errors.append("PDF named-destination count differs")
    if pdf["goto_actions"] != 2078 or pdf["broken_goto_actions"]:
        errors.append("PDF GoTo closure failed")
    if pdf["non_goto_actions"] or pdf["direct_destinations"]:
        errors.append("non-stable PDF actions remain")
    if pdf["annotation_subtypes"] != {"/Link": 2078}:
        errors.append("PDF annotations are not exactly 2078 Link annotations")
    if pdf["type3_fonts"] or pdf["unembedded_fonts"]:
        errors.append("PDF font embedding failed")
    if pdf["image_xobjects"]:
        errors.append("PDF raster image XObjects remain")

    privacy_hits: list[dict[str, object]] = []
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

    forbidden_payloads = [
        path.relative_to(root).as_posix()
        for path in root.rglob("*")
        if path.is_file()
        and (
            path.name.lower() == "the.bib"
            or "authority" in path.name.lower()
            or "ocr" in path.name.lower()
            or "scan" in path.name.lower()
        )
    ]
    if forbidden_payloads:
        errors.append(f"forbidden source-witness payloads: {forbidden_payloads}")

    result = {
        "schema": "ega2-complete-reference-package-validation-1.0",
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
        "source_closure": {
            "files": len(source_closure),
            "bytes": sum(int(row["bytes"]) for row in source_closure),
            "replay_errors": source_errors,
        },
        "reader": {
            "bytes": pdf_path.stat().st_size,
            "sha256": sha256(pdf_path),
            **pdf,
        },
        "csv_errors": csv_errors,
        "json_errors": json_errors,
        "privacy_hits": privacy_hits,
        "forbidden_payloads": forbidden_payloads,
    }
    output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
