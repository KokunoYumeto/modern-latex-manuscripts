#!/usr/bin/env python3
"""Compare a rebuilt SGA 1 reader to a controlling reader semantically."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import fitz
from pypdf import PdfReader


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def page_content(page: object) -> bytes:
    contents = page.get_contents()
    return b"" if contents is None else contents.get_data()


def destination_signature(reader: PdfReader, destination: object) -> tuple:
    return (
        reader.get_destination_page_number(destination),
        str(destination.typ),
        repr(destination.left),
        repr(destination.top),
        repr(destination.zoom),
    )


def actions(reader: PdfReader) -> list[tuple]:
    result: list[tuple] = []
    for page_number, page in enumerate(reader.pages, 1):
        for annotation_index, annotation_ref in enumerate(
            page.get("/Annots", [])
        ):
            annotation = annotation_ref.get_object()
            action_ref = annotation.get("/A")
            if action_ref is None:
                continue
            action = action_ref.get_object()
            if action.get("/S") != "/GoTo":
                continue
            result.append(
                (
                    page_number,
                    annotation_index,
                    tuple(round(float(value), 3) for value in annotation.get("/Rect", [])),
                    str(action.get("/D")),
                )
            )
    return result


def main() -> int:
    if len(sys.argv) != 4:
        raise SystemExit(
            "usage: validate_rebuilt_reader.py "
            "REFERENCE.pdf REBUILT.pdf OUTPUT.json"
        )
    reference_path = Path(sys.argv[1]).resolve()
    rebuilt_path = Path(sys.argv[2]).resolve()
    output_path = Path(sys.argv[3]).resolve()
    reference = PdfReader(str(reference_path))
    rebuilt = PdfReader(str(rebuilt_path))
    errors: list[str] = []
    if len(reference.pages) != len(rebuilt.pages):
        errors.append("page counts differ")
    page_count = min(len(reference.pages), len(rebuilt.pages))
    content_mismatches = [
        index + 1
        for index in range(page_count)
        if page_content(reference.pages[index])
        != page_content(rebuilt.pages[index])
    ]
    if content_mismatches:
        errors.append(f"decoded page content differs: {content_mismatches[:30]}")

    reference_fitz = fitz.open(reference_path)
    rebuilt_fitz = fitz.open(rebuilt_path)
    text_mismatches = [
        index + 1
        for index in range(page_count)
        if reference_fitz[index].get_text("text")
        != rebuilt_fitz[index].get_text("text")
    ]
    reference_fitz.close()
    rebuilt_fitz.close()
    if text_mismatches:
        errors.append(f"extracted page text differs: {text_mismatches[:30]}")

    reference_actions = actions(reference)
    rebuilt_actions = actions(rebuilt)
    if reference_actions != rebuilt_actions:
        errors.append("GoTo action targets or geometries differ")

    reference_names = reference.named_destinations
    rebuilt_names = rebuilt.named_destinations
    missing_names = sorted(set(reference_names) - set(rebuilt_names))
    extra_names = sorted(set(rebuilt_names) - set(reference_names))
    changed_destinations = [
        name
        for name in sorted(set(reference_names) & set(rebuilt_names))
        if destination_signature(reference, reference_names[name])
        != destination_signature(rebuilt, rebuilt_names[name])
    ]
    if missing_names:
        errors.append(f"named destinations missing: {missing_names[:20]}")
    if extra_names:
        errors.append(f"extra named destinations: {extra_names[:20]}")
    if changed_destinations:
        errors.append(
            f"named destination coordinates differ: {changed_destinations[:20]}"
        )

    validation = {
        "schema": "sga1-reference-reader-rebuild-comparison-1.0",
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "reference": {
            "path": str(reference_path),
            "bytes": reference_path.stat().st_size,
            "sha256": sha256(reference_path),
        },
        "rebuilt": {
            "path": str(rebuilt_path),
            "bytes": rebuilt_path.stat().st_size,
            "sha256": sha256(rebuilt_path),
        },
        "comparison": {
            "pages": page_count,
            "decoded_content_mismatch_pages": content_mismatches,
            "extracted_text_mismatch_pages": text_mismatches,
            "goto_actions_reference": len(reference_actions),
            "goto_actions_rebuilt": len(rebuilt_actions),
            "goto_actions_and_geometry_exact": reference_actions
            == rebuilt_actions,
            "named_destinations_reference": len(reference_names),
            "named_destinations_rebuilt": len(rebuilt_names),
            "missing_named_destinations": missing_names,
            "extra_named_destinations": extra_names,
            "changed_named_destination_coordinates": changed_destinations,
            "byte_identity_required": False,
            "note": "PDF container bytes may differ because TeX/PDF writers emit run-specific identifiers; decoded pages, text, actions, rectangles, and destination coordinates are the reproducibility contract.",
        },
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(validation, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(validation, indent=2, ensure_ascii=False))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
