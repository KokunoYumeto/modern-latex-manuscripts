#!/usr/bin/env python3
"""Exhaustive PDF and rendered-layout QA for the SGA 1 reference reader."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

import fitz
from pypdf import PdfReader


EXPECTED_METADATA = {
    "/Title": "SGA 1: Étale Coverings and the Fundamental Group — English Translation",
    "/Author": "English translation from the official French arXiv/SMF TeX",
    "/Subject": "Complete English translation of SGA 1",
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


def object_key(obj: object) -> tuple:
    indirect = getattr(obj, "indirect_reference", None)
    if indirect is not None:
        return ("indirect", indirect.idnum, indirect.generation)
    return ("direct", id(obj))


def dereference(value: object) -> object:
    getter = getattr(value, "get_object", None)
    return getter() if getter is not None else value


def font_descriptor(font: object) -> object | None:
    font = font.get_object()
    subtype = str(font.get("/Subtype", ""))
    if subtype == "/Type0":
        descendants = font.get("/DescendantFonts", [])
        if not descendants:
            return None
        descendant = descendants[0].get_object()
        descriptor = descendant.get("/FontDescriptor")
        return None if descriptor is None else descriptor.get_object()
    descriptor = font.get("/FontDescriptor")
    return None if descriptor is None else descriptor.get_object()


def inspect_resources(reader: PdfReader) -> dict:
    fonts: dict[tuple, object] = {}
    images: dict[tuple, object] = {}
    forms_seen: set[tuple] = set()

    def walk_resources(resources_ref: object | None) -> None:
        if resources_ref is None:
            return
        resources = dereference(resources_ref)
        for font_ref in dereference(resources.get("/Font", {})).values():
            font = font_ref.get_object()
            fonts[object_key(font)] = font
        for xobject_ref in dereference(resources.get("/XObject", {})).values():
            xobject = xobject_ref.get_object()
            key = object_key(xobject)
            subtype = str(xobject.get("/Subtype", ""))
            if subtype == "/Image":
                images[key] = xobject
            elif subtype == "/Form" and key not in forms_seen:
                forms_seen.add(key)
                walk_resources(xobject.get("/Resources"))

    for page in reader.pages:
        walk_resources(page.get("/Resources"))

    type3 = 0
    unembedded: list[str] = []
    subtype_counts: Counter[str] = Counter()
    for font in fonts.values():
        subtype = str(font.get("/Subtype", ""))
        subtype_counts[subtype] += 1
        if subtype == "/Type3":
            type3 += 1
        descriptor = font_descriptor(font)
        embedded = False
        if descriptor is not None:
            embedded = any(
                descriptor.get(key) is not None
                for key in ("/FontFile", "/FontFile2", "/FontFile3")
            )
        if not embedded:
            unembedded.append(str(font.get("/BaseFont", "<unnamed>")))
    return {
        "font_objects": len(fonts),
        "font_subtypes": dict(sorted(subtype_counts.items())),
        "type3_fonts": type3,
        "unembedded_fonts": sorted(unembedded),
        "image_xobjects": len(images),
        "form_xobjects": len(forms_seen),
    }


def inspect_actions(reader: PdfReader) -> dict:
    named = reader.named_destinations
    counts: Counter[str] = Counter()
    broken: list[dict] = []
    external: list[dict] = []
    for page_number, page in enumerate(reader.pages, 1):
        for annotation_index, annotation_ref in enumerate(
            page.get("/Annots", [])
        ):
            annotation = annotation_ref.get_object()
            action_ref = annotation.get("/A")
            if action_ref is None:
                continue
            action = action_ref.get_object()
            action_type = str(action.get("/S", ""))
            counts[action_type] += 1
            if action_type == "/GoTo":
                destination = str(action.get("/D"))
                if destination not in named:
                    broken.append(
                        {
                            "page": page_number,
                            "annotation_index": annotation_index,
                            "destination": destination,
                        }
                    )
            elif action_type in {"/URI", "/GoToR", "/Launch", "/JavaScript"}:
                external.append(
                    {
                        "page": page_number,
                        "annotation_index": annotation_index,
                        "action_type": action_type,
                    }
                )
    return {
        "action_counts": dict(sorted(counts.items())),
        "broken_goto_actions": broken,
        "external_or_active_actions": external,
    }


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit("usage: validate_complete_reference_reader.py ROOT")
    root = Path(sys.argv[1]).resolve()
    controls = root / "controls"
    baseline_pdf = (
        root
        / "build_hypertexnames_false"
        / "SGA1_English_source_sync_workpass.pdf"
    )
    source_build_pdf = (
        root
        / "build_raw_links_r2_source_footnote_anchors"
        / "SGA1_English_source_sync_workpass.pdf"
    )
    final_pdf = (
        root
        / "build_stable_alias_overlay_r6_source_complete"
        / "SGA1_English_complete_reference_reader.pdf"
    )
    graph_validation_path = controls / "REFERENCE_GRAPH_VALIDATION.json"
    graph_validation = json.loads(
        graph_validation_path.read_text(encoding="utf-8")
    )
    source_closure = read_csv(controls / "SOURCE_CLOSURE.csv")

    errors: list[str] = []
    baseline_reader = PdfReader(str(baseline_pdf))
    source_reader = PdfReader(str(source_build_pdf))
    final_reader = PdfReader(str(final_pdf))
    if not (
        len(baseline_reader.pages)
        == len(source_reader.pages)
        == len(final_reader.pages)
        == 262
    ):
        errors.append("page-count invariant failed")
    if graph_validation.get("status") != "PASS":
        errors.append("reference graph validation is not PASS")

    metadata = {key: str(value) for key, value in (final_reader.metadata or {}).items()}
    for key, expected in EXPECTED_METADATA.items():
        if metadata.get(key) != expected:
            errors.append(
                f"metadata {key} differs: {metadata.get(key)!r} != {expected!r}"
            )

    resource_audit = inspect_resources(final_reader)
    if resource_audit["type3_fonts"]:
        errors.append("Type3 fonts remain")
    if resource_audit["unembedded_fonts"]:
        errors.append(
            f"unembedded fonts remain: {resource_audit['unembedded_fonts']}"
        )
    if resource_audit["image_xobjects"]:
        errors.append("raster image XObjects remain")

    action_audit = inspect_actions(final_reader)
    if action_audit["broken_goto_actions"]:
        errors.append("broken GoTo actions remain")
    if action_audit["external_or_active_actions"]:
        errors.append("external or active PDF actions remain")
    if action_audit["action_counts"].get("/GoTo") != 1600:
        errors.append("final GoTo action count is not 1600")
    if len(final_reader.named_destinations) != 2151:
        errors.append("final named-destination count is not 2151")

    # Full-page visual equivalence at 180 dpi.  Link annotations and named
    # destinations are nonvisual; every page must rasterize identically to the
    # pre-reference baseline.
    baseline_document = fitz.open(baseline_pdf)
    final_document = fitz.open(final_pdf)
    matrix = fitz.Matrix(2.5, 2.5)
    render_rows: list[dict[str, object]] = []
    render_mismatches: list[int] = []
    accepted_subpixel_pages: list[int] = []
    material_render_mismatches: list[int] = []
    for index in range(len(final_document)):
        baseline_pixmap = baseline_document[index].get_pixmap(
            matrix=matrix, colorspace=fitz.csRGB, alpha=False, annots=False
        )
        final_pixmap = final_document[index].get_pixmap(
            matrix=matrix, colorspace=fitz.csRGB, alpha=False, annots=False
        )
        baseline_hash = hashlib.sha256(baseline_pixmap.samples).hexdigest().upper()
        final_hash = hashlib.sha256(final_pixmap.samples).hexdigest().upper()
        equal = (
            baseline_pixmap.width == final_pixmap.width
            and baseline_pixmap.height == final_pixmap.height
            and baseline_hash == final_hash
        )
        if not equal:
            render_mismatches.append(index + 1)
        baseline_words = baseline_document[index].get_text("words")
        final_words = final_document[index].get_text("words")
        word_text_equal = [row[4] for row in baseline_words] == [
            row[4] for row in final_words
        ]
        maximum_word_coordinate_delta = 0.0
        changed_word_boxes = 0
        if word_text_equal:
            for baseline_word, final_word in zip(
                baseline_words, final_words
            ):
                delta = max(
                    abs(float(baseline_word[position]) - float(final_word[position]))
                    for position in range(4)
                )
                maximum_word_coordinate_delta = max(
                    maximum_word_coordinate_delta, delta
                )
                if delta:
                    changed_word_boxes += 1
        subpixel_equivalent = (
            not equal
            and word_text_equal
            and maximum_word_coordinate_delta <= 0.02
        )
        if subpixel_equivalent:
            accepted_subpixel_pages.append(index + 1)
        elif not equal:
            material_render_mismatches.append(index + 1)
        render_rows.append(
            {
                "pdf_page": index + 1,
                "dpi": 180,
                "width_px": final_pixmap.width,
                "height_px": final_pixmap.height,
                "baseline_pixel_sha256": baseline_hash,
                "final_pixel_sha256": final_hash,
                "pixel_exact": str(equal).lower(),
                "word_text_equal": str(word_text_equal).lower(),
                "changed_word_boxes": changed_word_boxes,
                "maximum_word_coordinate_delta_points": (
                    f"{maximum_word_coordinate_delta:.9f}"
                ),
                "status": (
                    "PASS_PIXEL_EXACT"
                    if equal
                    else (
                        "PASS_SUBPIXEL_TEXT_GEOMETRY"
                        if subpixel_equivalent
                        else "FAIL"
                    )
                ),
            }
        )
    baseline_document.close()
    final_document.close()
    if material_render_mismatches:
        errors.append(
            f"material render mismatches: {material_render_mismatches[:30]}"
        )

    render_qa_path = controls / "RENDER_QA_180DPI.csv"
    with render_qa_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(render_rows[0]),
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(render_rows)

    # Privacy scan exactly the active TeX closure, final PDF, and co-current
    # machine ledgers.  Historical build logs are intentionally outside this
    # delivery surface.
    delivery_files = [
        root / row["relative_path"] for row in source_closure
    ] + [
        final_pdf,
        controls / "REFERENCE_TARGETS.csv",
        controls / "REFERENCE_EDGES.csv",
        controls / "REFERENCE_CANDIDATES.csv",
        controls / "REFERENCE_APPLICATIONS.csv",
        controls / "REFERENCE_RESIDUALS.csv",
        controls / "REFERENCE_GRAPH_VALIDATION.json",
        render_qa_path,
    ]
    privacy_hits: list[dict[str, object]] = []
    for path in delivery_files:
        data = path.read_bytes()
        for pattern_name, pattern in PRIVATE_PATTERNS.items():
            matches = list(pattern.finditer(data))
            if matches:
                privacy_hits.append(
                    {
                        "path": str(path.relative_to(root)).replace("\\", "/")
                        if path.is_relative_to(root)
                        else path.name,
                        "pattern": pattern_name,
                        "count": len(matches),
                    }
                )
    if privacy_hits:
        errors.append(f"privacy hits remain: {privacy_hits[:20]}")

    validation = {
        "schema": "sga1-complete-reference-reader-pdf-qa-1.0",
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "reader": {
            "path": final_pdf.name,
            "bytes": final_pdf.stat().st_size,
            "sha256": sha256(final_pdf),
            "pages": len(final_reader.pages),
            "metadata": metadata,
        },
        "source_build": {
            "path": source_build_pdf.name,
            "bytes": source_build_pdf.stat().st_size,
            "sha256": sha256(source_build_pdf),
            "pass3_console_sha256": sha256(
                source_build_pdf.parent / "pass3_console.txt"
            ),
            "pass4_console_sha256": sha256(
                source_build_pdf.parent / "pass4_console.txt"
            ),
            "pass3_pass4_console_byte_identical": (
                sha256(source_build_pdf.parent / "pass3_console.txt")
                == sha256(source_build_pdf.parent / "pass4_console.txt")
            ),
        },
        "reference_graph": {
            "validation_path": graph_validation_path.name,
            "validation_sha256": sha256(graph_validation_path),
            "status": graph_validation.get("status"),
            "counts": graph_validation.get("counts"),
        },
        "resources": resource_audit,
        "actions": action_audit,
        "render_qa": {
            "dpi": 180,
            "pages_checked": len(render_rows),
            "pixel_exact_pages": len(render_rows) - len(render_mismatches),
            "subpixel_text_geometry_equivalent_pages": accepted_subpixel_pages,
            "material_mismatch_pages": material_render_mismatches,
            "pixel_nonidentical_pages": render_mismatches,
            "ledger": render_qa_path.name,
            "ledger_sha256": sha256(render_qa_path),
        },
        "privacy": {
            "files_scanned": len(delivery_files),
            "hits": privacy_hits,
        },
        "source_closure": {
            "files": len(source_closure),
            "bytes": sum(int(row["bytes"]) for row in source_closure),
            "ledger": "SOURCE_CLOSURE.csv",
            "ledger_sha256": sha256(controls / "SOURCE_CLOSURE.csv"),
        },
    }
    validation_path = controls / "FINAL_PDF_QA_VALIDATION.json"
    validation_path.write_text(
        json.dumps(validation, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "status": validation["status"],
                "errors": errors,
                "reader_sha256": validation["reader"]["sha256"],
                "render_qa": validation["render_qa"],
                "resources": resource_audit,
                "privacy": validation["privacy"],
                "validation": str(validation_path),
                "validation_sha256": sha256(validation_path),
            },
            indent=2,
        )
    )
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
