"""Validate a PDF produced by build_prefixed_pdf.py.

The build JSON is treated as the expected namespace/page map.  Validation
checks exact page and destination counts, destination page offsets, link
counts, and resolvability of every internal GoTo action.  It emits one JSON
object and exits nonzero on any failure.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any

from pypdf import PdfReader


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def destination_name(value: Any) -> str | None:
    if isinstance(value, str):
        raw = str(value)
        return raw[1:] if raw.startswith("/") else raw
    return None


def main() -> int:
    if len(sys.argv) != 4:
        print(
            "usage: validate_prefixed_pdf.py BUILD.json OUTPUT.pdf VALIDATION.json",
            file=sys.stderr,
        )
        return 2

    build_path = Path(sys.argv[1])
    pdf_path = Path(sys.argv[2])
    validation_path = Path(sys.argv[3])
    build = json.loads(build_path.read_text(encoding="utf-8"))
    reader = PdfReader(pdf_path)
    destinations = reader.named_destinations

    errors: list[dict[str, Any]] = []
    expected_pages = int(build["pages"])
    expected_destinations = sum(
        int(record["named_destinations"]) for record in build["inputs"]
    )
    expected_links = sum(int(record["link_annotations"]) for record in build["inputs"])

    if len(reader.pages) != expected_pages:
        errors.append(
            {"kind": "page_count", "expected": expected_pages, "actual": len(reader.pages)}
        )
    if len(destinations) != expected_destinations:
        errors.append(
            {
                "kind": "destination_count",
                "expected": expected_destinations,
                "actual": len(destinations),
            }
        )

    missing_destinations: list[str] = []
    route_mismatches: list[dict[str, Any]] = []
    for record in build["inputs"]:
        offset = int(record["page_offset"])
        for name, local_page in record["expected_local_pages"].items():
            destination = destinations.get(name)
            if destination is None:
                missing_destinations.append(name)
                continue
            actual_page = reader.get_destination_page_number(destination)
            expected_page = offset + int(local_page)
            if actual_page != expected_page:
                route_mismatches.append(
                    {
                        "name": name,
                        "expected_page_zero_based": expected_page,
                        "actual_page_zero_based": actual_page,
                    }
                )

    link_annotations = 0
    goto_actions = 0
    external_actions = 0
    malformed_internal_actions: list[dict[str, Any]] = []
    broken_named_actions: list[dict[str, Any]] = []
    page_ids = {page.indirect_reference.idnum for page in reader.pages}

    for page_number, page in enumerate(reader.pages, start=1):
        for annot_ref in page.get("/Annots") or []:
            annot = annot_ref.get_object()
            if annot.get("/Subtype") != "/Link":
                continue
            link_annotations += 1

            action = annot.get("/A")
            value = None
            if action and action.get("/S") == "/GoTo":
                goto_actions += 1
                value = action.get("/D")
            elif annot.get("/Dest") is not None:
                goto_actions += 1
                value = annot.get("/Dest")
            else:
                external_actions += 1
                continue

            name = destination_name(value)
            if name is not None:
                if name not in destinations:
                    broken_named_actions.append({"page": page_number, "target": name})
                continue

            if isinstance(value, list) and value:
                target = value[0]
                if hasattr(target, "idnum") and target.idnum not in page_ids:
                    malformed_internal_actions.append(
                        {"page": page_number, "reason": "target_page_not_in_reader"}
                    )
                continue

            malformed_internal_actions.append(
                {"page": page_number, "reason": "unrecognized_destination"}
            )

    if link_annotations != expected_links:
        errors.append(
            {"kind": "link_count", "expected": expected_links, "actual": link_annotations}
        )
    if missing_destinations:
        errors.append(
            {
                "kind": "missing_destinations",
                "count": len(missing_destinations),
                "sample": missing_destinations[:20],
            }
        )
    if route_mismatches:
        errors.append(
            {
                "kind": "destination_route_mismatches",
                "count": len(route_mismatches),
                "sample": route_mismatches[:20],
            }
        )
    if broken_named_actions:
        errors.append(
            {
                "kind": "broken_named_actions",
                "count": len(broken_named_actions),
                "sample": broken_named_actions[:20],
            }
        )
    if malformed_internal_actions:
        errors.append(
            {
                "kind": "malformed_internal_actions",
                "count": len(malformed_internal_actions),
                "sample": malformed_internal_actions[:20],
            }
        )

    outline_items = 0
    invalid_outline_destinations: list[dict[str, Any]] = []
    outline_titles: list[str] = []

    def inspect_outline(items: list[Any]) -> None:
        nonlocal outline_items
        for item in items:
            if isinstance(item, list):
                inspect_outline(item)
                continue
            outline_items += 1
            title = getattr(item, "title", None)
            if title is not None:
                outline_titles.append(str(title))
            try:
                page_number = reader.get_destination_page_number(item)
            except Exception as exc:  # fail closed on malformed imported outlines
                invalid_outline_destinations.append(
                    {"title": str(title), "reason": type(exc).__name__}
                )
                continue
            if page_number < 0 or page_number >= len(reader.pages):
                invalid_outline_destinations.append(
                    {"title": str(title), "page_zero_based": page_number}
                )

    inspect_outline(reader.outline)
    missing_volume_outline_titles = [
        str(record["title"])
        for record in build["inputs"]
        if str(record["title"]) not in outline_titles
    ]
    expected_outline_items = len(build["inputs"]) + sum(
        int(record.get("imported_outline_items", 0)) for record in build["inputs"]
    )
    if outline_items != expected_outline_items:
        errors.append(
            {
                "kind": "outline_item_count",
                "expected": expected_outline_items,
                "actual": outline_items,
            }
        )
    if invalid_outline_destinations:
        errors.append(
            {
                "kind": "invalid_outline_destinations",
                "count": len(invalid_outline_destinations),
                "sample": invalid_outline_destinations[:20],
            }
        )
    if missing_volume_outline_titles:
        errors.append(
            {
                "kind": "missing_volume_outline_titles",
                "titles": missing_volume_outline_titles,
            }
        )

    result = {
        "schema": "sga-global-prefixed-pdf-validation-v1",
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "build_evidence": str(build_path),
        "pdf": str(pdf_path),
        "pdf_bytes": pdf_path.stat().st_size,
        "pdf_sha256": sha256(pdf_path),
        "pages": len(reader.pages),
        "named_destinations": len(destinations),
        "link_annotations": link_annotations,
        "goto_actions": goto_actions,
        "external_or_non_goto_actions": external_actions,
        "missing_destinations": len(missing_destinations),
        "destination_route_mismatches": len(route_mismatches),
        "broken_named_actions": len(broken_named_actions),
        "malformed_internal_actions": len(malformed_internal_actions),
        "outline_items": outline_items,
        "expected_outline_items": expected_outline_items,
        "invalid_outline_destinations": len(invalid_outline_destinations),
        "missing_volume_outline_titles": missing_volume_outline_titles,
    }
    validation_path.parent.mkdir(parents=True, exist_ok=True)
    validation_path.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
