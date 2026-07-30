#!/usr/bin/env python3
"""Compare a rebuilt EGA I reader with the packaged canonical reader."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

from pypdf import PdfReader


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def dereference(value: object) -> object:
    getter = getattr(value, "get_object", None)
    return getter() if getter is not None else value


def content(page: object) -> bytes:
    stream = page.get_contents()
    return b"" if stream is None else stream.get_data()


def destination_signature(reader: PdfReader, destination: object) -> tuple[object, ...]:
    return (
        reader.get_destination_page_number(destination),
        str(destination.typ),
        repr(destination.left),
        repr(destination.top),
        repr(destination.zoom),
    )


def action_signature(reader: PdfReader) -> list[tuple[object, ...]]:
    rows = []
    for page_number, page in enumerate(reader.pages, 1):
        for annotation_index, annotation_ref in enumerate(page.get("/Annots", [])):
            annotation = dereference(annotation_ref)
            rect = tuple(round(float(value), 5) for value in annotation.get("/Rect", []))
            action_ref = annotation.get("/A")
            action = None if action_ref is None else dereference(action_ref)
            rows.append(
                (
                    page_number,
                    annotation_index,
                    str(annotation.get("/Subtype", "")),
                    rect,
                    "" if action is None else str(action.get("/S", "")),
                    "" if action is None else str(action.get("/D", "")),
                    "" if annotation.get("/Dest") is None else str(annotation.get("/Dest")),
                )
            )
    return rows


def main() -> int:
    if len(sys.argv) != 4:
        raise SystemExit("usage: validate_rebuilt_reader.py EXPECTED.pdf REBUILT.pdf OUTPUT.json")
    expected_path = Path(sys.argv[1]).resolve()
    rebuilt_path = Path(sys.argv[2]).resolve()
    output = Path(sys.argv[3]).resolve()
    expected = PdfReader(str(expected_path))
    rebuilt = PdfReader(str(rebuilt_path))
    errors: list[str] = []
    if len(expected.pages) != len(rebuilt.pages):
        errors.append("page count differs")
    content_equal = len(expected.pages) == len(rebuilt.pages) and all(
        content(before) == content(after)
        for before, after in zip(expected.pages, rebuilt.pages)
    )
    text_equal = len(expected.pages) == len(rebuilt.pages) and all(
        before.extract_text() == after.extract_text()
        for before, after in zip(expected.pages, rebuilt.pages)
    )
    if not content_equal:
        errors.append("decoded page content streams differ")
    if not text_equal:
        errors.append("extracted page text differs")
    expected_destinations = expected.named_destinations
    rebuilt_destinations = rebuilt.named_destinations
    destination_keys_equal = set(expected_destinations) == set(rebuilt_destinations)
    if not destination_keys_equal:
        errors.append("named-destination key set differs")
    destination_signatures_equal = destination_keys_equal and all(
        destination_signature(expected, expected_destinations[name])
        == destination_signature(rebuilt, rebuilt_destinations[name])
        for name in expected_destinations
    )
    if not destination_signatures_equal:
        errors.append("named-destination coordinates differ")
    expected_actions = action_signature(expected)
    rebuilt_actions = action_signature(rebuilt)
    actions_equal = expected_actions == rebuilt_actions
    if not actions_equal:
        errors.append("annotation/action geometry or targets differ")
    metadata_equal = dict(expected.metadata or {}) == dict(rebuilt.metadata or {})
    if not metadata_equal:
        errors.append("metadata differs")

    result = {
        "schema": "ega1-clean-rebuild-semantic-equivalence-1.0",
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "expected": {
            "file": expected_path.name,
            "bytes": expected_path.stat().st_size,
            "sha256": sha(expected_path),
        },
        "rebuilt": {
            "file": rebuilt_path.name,
            "bytes": rebuilt_path.stat().st_size,
            "sha256": sha(rebuilt_path),
        },
        "pages": len(expected.pages),
        "decoded_content_streams_equal": content_equal,
        "extracted_text_equal": text_equal,
        "named_destinations": len(expected_destinations),
        "destination_keys_equal": destination_keys_equal,
        "destination_signatures_equal": destination_signatures_equal,
        "annotations": len(expected_actions),
        "annotation_action_signatures_equal": actions_equal,
        "metadata_equal": metadata_equal,
        "note": "Byte hashes may differ because the PDF trailer/document identifier is build-path-sensitive; all delivered semantic objects are required to match exactly.",
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
