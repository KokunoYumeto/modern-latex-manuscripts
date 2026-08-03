"""Build a cumulative PDF while namespacing each input's named destinations.

Usage:
  python tools/build_prefixed_pdf.py OUTPUT.pdf PREFIX TITLE INPUT.pdf [...]

Each input is appended whole.  Page content, page annotations, and outlines are
cloned by pypdf.  Named destinations and named GoTo actions are prefixed before
cloning so identical names in different volumes cannot silently misroute.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, TextStringObject


def _named_key(value: Any, known: set[str]) -> str | None:
    if not isinstance(value, str):
        return None
    raw = str(value)
    if raw in known:
        return raw
    if raw.startswith("/") and raw[1:] in known:
        return raw[1:]
    return None


def namespace_reader(reader: PdfReader, prefix: str) -> dict[str, Any]:
    original = reader.named_destinations
    known = set(original)
    renamed: dict[str, Any] = {}
    expected_local_pages: dict[str, int] = {}

    for old_name, destination in original.items():
        new_name = f"{prefix}::{old_name}"
        expected_local_pages[new_name] = reader.get_destination_page_number(destination)
        destination[NameObject("/Title")] = TextStringObject(new_name)
        renamed[new_name] = destination

    # PdfWriter.append asks the reader for this property immediately before
    # importing destinations.  An instance function is intentional here: it
    # returns the already resolved, uniquely renamed destination set.
    reader._get_named_destinations = lambda *args, **kwargs: renamed  # type: ignore[method-assign]

    renamed_actions = 0
    unresolved_named_actions: list[str] = []
    link_annotations = 0

    for page in reader.pages:
        for annot_ref in page.get("/Annots") or []:
            annot = annot_ref.get_object()
            if annot.get("/Subtype") != "/Link":
                continue
            link_annotations += 1

            action = annot.get("/A")
            container = None
            key = None
            value = None
            if action and action.get("/S") == "/GoTo":
                container, key, value = action, NameObject("/D"), action.get("/D")
            elif annot.get("/Dest") is not None:
                container, key, value = annot, NameObject("/Dest"), annot.get("/Dest")

            old_name = _named_key(value, known)
            if old_name is not None and container is not None and key is not None:
                container[key] = TextStringObject(f"{prefix}::{old_name}")
                renamed_actions += 1
            elif isinstance(value, str):
                unresolved_named_actions.append(str(value))

    return {
        "prefix": prefix,
        "pages": len(reader.pages),
        "named_destinations": len(renamed),
        "link_annotations": link_annotations,
        "renamed_named_actions": renamed_actions,
        "unresolved_named_actions": sorted(set(unresolved_named_actions)),
        "expected_local_pages": expected_local_pages,
    }


def extract_outline(reader: PdfReader) -> list[dict[str, Any]]:
    """Convert pypdf's alternating item/list outline form to a plain tree."""

    def walk(items: list[Any]) -> list[dict[str, Any]]:
        result: list[dict[str, Any]] = []
        previous: dict[str, Any] | None = None
        for item in items:
            if isinstance(item, list):
                if previous is not None:
                    previous["children"] = walk(item)
                continue
            title = str(getattr(item, "title", ""))
            try:
                page = reader.get_destination_page_number(item)
            except Exception:
                page = -1
            previous = {"title": title, "page": page, "children": []}
            result.append(previous)
        return result

    return walk(reader.outline)


def count_outline(items: list[dict[str, Any]]) -> int:
    return sum(1 + count_outline(item["children"]) for item in items)


def add_outline_tree(
    writer: PdfWriter,
    items: list[dict[str, Any]],
    page_offset: int,
    parent: Any,
) -> int:
    added = 0
    for item in items:
        local_page = int(item["page"])
        if local_page < 0:
            continue
        node = writer.add_outline_item(
            str(item["title"]), page_offset + local_page, parent=parent
        )
        added += 1
        added += add_outline_tree(
            writer, item["children"], page_offset=page_offset, parent=node
        )
    return added


def main() -> int:
    if len(sys.argv) < 6 or (len(sys.argv) - 2) % 3:
        print(
            "usage: build_prefixed_pdf.py OUTPUT.pdf PREFIX TITLE INPUT.pdf [...]",
            file=sys.stderr,
        )
        return 2

    output = Path(sys.argv[1])
    triples = [sys.argv[i : i + 3] for i in range(2, len(sys.argv), 3)]
    writer = PdfWriter()
    writer.add_metadata(
        {
            "/Title": "SGA 1–7.2 — English Reader",
            "/Author": "SGA authors and redactors",
            "/Subject": "English translations of SGA 1 through SGA 7 II",
            "/Keywords": "SGA, algebraic geometry, English translation",
        }
    )
    records: list[dict[str, Any]] = []
    page_offset = 0

    for prefix, title, input_name in triples:
        reader = PdfReader(input_name)
        outline = extract_outline(reader)
        record = namespace_reader(reader, prefix)
        record["title"] = title
        record["input"] = str(Path(input_name))
        record["page_offset"] = page_offset
        record["source_outline_items"] = count_outline(outline)
        writer.append(reader, import_outline=False)
        volume_node = writer.add_outline_item(title, page_offset)
        record["imported_outline_items"] = add_outline_tree(
            writer, outline, page_offset=page_offset, parent=volume_node
        )
        page_offset += record["pages"]
        records.append(record)

    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("wb") as stream:
        writer.write(stream)

    result = {
        "schema": "sga-global-prefixed-pdf-build-v1",
        "output": str(output),
        "pages": page_offset,
        "inputs": records,
    }
    evidence_path = output.with_name(f"{output.stem}_build.json")
    evidence_path.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "output": str(output),
                "build_evidence": str(evidence_path),
                "pages": page_offset,
                "inputs": len(records),
                "named_destinations": sum(r["named_destinations"] for r in records),
                "link_annotations": sum(r["link_annotations"] for r in records),
                "outline_items": len(records)
                + sum(r["imported_outline_items"] for r in records),
                "unresolved_named_actions": sum(
                    len(r["unresolved_named_actions"]) for r in records
                ),
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
