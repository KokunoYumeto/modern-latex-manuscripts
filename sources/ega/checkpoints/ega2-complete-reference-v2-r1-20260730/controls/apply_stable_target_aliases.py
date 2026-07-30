#!/usr/bin/env python3
"""Add stable EGA II named-destination aliases to a compiled reader.

Each stable name is an exact alias of a destination already emitted by
Hyperref.  Page content streams and link rectangles are not edited.
"""

from __future__ import annotations

import csv
import sys
from collections import defaultdict
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf.generic import (
    ArrayObject,
    DictionaryObject,
    NameObject,
    TextStringObject,
)


def destination_signature(reader: PdfReader, destination: object) -> tuple[object, ...]:
    """Return the page and view coordinates that define a destination."""

    return (
        reader.get_destination_page_number(destination),
        str(destination.typ),
        repr(destination.left),
        repr(destination.top),
        repr(destination.zoom),
    )


KIND_PRIORITY = {
    "chapter": 0,
    "sec": 1,
    "prop": 2,
    "thm": 3,
    "cor": 4,
    "lem": 5,
    "def": 6,
    "statement": 7,
    "rem": 8,
    "ex": 9,
    "eq": 10,
    "bib": 11,
    "note": 12,
    "footnote": 13,
    "page": 14,
    "index": 15,
    "anchor": 16,
    "generated": 17,
}


def main() -> int:
    if len(sys.argv) not in {4, 5}:
        raise SystemExit(
            "usage: apply_stable_target_aliases.py "
            "INPUT.pdf REFERENCE_TARGETS.csv OUTPUT.pdf "
            "[REFERENCE_ACTION_OVERRIDES.csv]"
        )
    input_pdf = Path(sys.argv[1]).resolve()
    ledger = Path(sys.argv[2]).resolve()
    output_pdf = Path(sys.argv[3]).resolve()
    override_ledger = (
        Path(sys.argv[4]).resolve() if len(sys.argv) == 5 else None
    )
    if output_pdf.exists():
        raise FileExistsError(f"Refusing to overwrite {output_pdf}")

    reader = PdfReader(str(input_pdf))
    destinations = reader.named_destinations
    with ledger.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))

    target_ids = [row["target_id"] for row in rows]
    if len(target_ids) != len(set(target_ids)):
        raise RuntimeError("REFERENCE_TARGETS.csv has duplicate target IDs")
    collisions = sorted(set(target_ids).intersection(destinations))
    if collisions:
        raise RuntimeError(f"Stable target already exists: {collisions[:10]}")

    missing = sorted(
        {
            row["baseline_pdf_destination"]
            for row in rows
            if row["baseline_pdf_destination"] not in destinations
        }
    )
    if missing:
        raise RuntimeError(f"Missing baseline destinations: {missing[:20]}")

    rows_by_baseline: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        rows_by_baseline[row["baseline_pdf_destination"]].append(row)
    canonical_target = {
        baseline: min(
            candidates,
            key=lambda row: (
                KIND_PRIORITY.get(row["kind"], 99),
                row["target_id"],
            ),
        )["target_id"]
        for baseline, candidates in rows_by_baseline.items()
    }

    action_overrides: dict[tuple[int, int], dict[str, str]] = {}
    if override_ledger is not None:
        with override_ledger.open(
            "r", encoding="utf-8-sig", newline=""
        ) as handle:
            override_rows = list(csv.DictReader(handle))
        for row in override_rows:
            key = (int(row["pdf_page"]), int(row["annotation_index"]))
            if key in action_overrides:
                raise RuntimeError(f"Duplicate action override selector: {key}")
            if row["target_id"] not in target_ids:
                raise RuntimeError(
                    "Action override names an unknown stable target: "
                    f"{row['target_id']}"
                )
            action_overrides[key] = row

    writer = PdfWriter()
    writer.clone_document_from_reader(reader)

    # Hyperref emitted a multi-branch name tree.  PdfWriter's convenience
    # helper only handles a flat /Names array and, on this input, creates an
    # unattached array under the existing /Kids root.  Rebuild /Dests as one
    # standards-compliant sorted flat name tree instead.  The destination
    # arrays still point to the same cloned page objects and coordinates.
    output_destinations: dict[str, object] = {
        name: destination.dest_array
        for name, destination in destinations.items()
    }
    for row in rows:
        source_destination = destinations[row["baseline_pdf_destination"]]
        output_destinations[row["target_id"]] = source_destination.dest_array

    flattened_names = ArrayObject()
    for name in sorted(output_destinations):
        flattened_names.append(TextStringObject(name))
        flattened_names.append(output_destinations[name].clone(writer))

    rebuilt_dests = DictionaryObject(
        {
            NameObject("/Names"): flattened_names,
            NameObject("/Limits"): ArrayObject(
                [
                    TextStringObject(min(output_destinations)),
                    TextStringObject(max(output_destinations)),
                ]
            ),
        }
    )
    root_names = writer.root_object[NameObject("/Names")]
    root_names[NameObject("/Dests")] = writer._add_object(rebuilt_dests)

    rewritten_actions = 0
    input_goto_actions = 0
    input_unmapped_actions: list[tuple[int, str]] = []
    applied_overrides: set[tuple[int, int]] = set()
    for page_number, page in enumerate(writer.pages, 1):
        for annotation_index, annotation_ref in enumerate(
            page.get("/Annots", [])
        ):
            annotation = annotation_ref.get_object()
            if annotation.get("/Subtype") != "/Link":
                continue
            action_ref = annotation.get("/A")
            if action_ref is None:
                continue
            action = action_ref.get_object()
            if action.get("/S") != "/GoTo":
                continue
            input_goto_actions += 1
            baseline_destination = str(action.get("/D"))
            override_key = (page_number, annotation_index)
            override = action_overrides.get(override_key)
            if override is not None:
                if baseline_destination != override["input_destination"]:
                    raise RuntimeError(
                        "Action override input destination changed at "
                        f"{override_key}: expected "
                        f"{override['input_destination']}, found "
                        f"{baseline_destination}"
                    )
                target_id = override["target_id"]
                applied_overrides.add(override_key)
            else:
                target_id = canonical_target.get(baseline_destination)
            if target_id is None:
                input_unmapped_actions.append(
                    (page_number, baseline_destination)
                )
                continue
            action[NameObject("/D")] = TextStringObject(target_id)
            rewritten_actions += 1
    if input_unmapped_actions:
        raise RuntimeError(
            "GoTo actions lack a stable target: "
            f"{input_unmapped_actions[:20]}"
        )
    unapplied_overrides = sorted(set(action_overrides) - applied_overrides)
    if unapplied_overrides:
        raise RuntimeError(
            f"Action overrides were not applied: {unapplied_overrides[:20]}"
        )

    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    with output_pdf.open("wb") as handle:
        writer.write(handle)

    output_reader = PdfReader(str(output_pdf))
    output_named = output_reader.named_destinations
    expected_count = len(destinations) + len(rows)
    if len(output_named) != expected_count:
        raise RuntimeError(
            f"Output has {len(output_named)} named destinations; "
            f"expected {expected_count}"
        )
    missing_output = sorted(set(output_destinations).difference(output_named))
    if missing_output:
        raise RuntimeError(f"Output omitted destinations: {missing_output[:20]}")

    changed_existing = [
        name
        for name, destination in destinations.items()
        if destination_signature(reader, destination)
        != destination_signature(output_reader, output_named[name])
    ]
    if changed_existing:
        raise RuntimeError(
            f"Existing destination coordinates changed: {changed_existing[:20]}"
        )

    mismatched_aliases = [
        row["target_id"]
        for row in rows
        if destination_signature(
            output_reader, output_named[row["target_id"]]
        )
        != destination_signature(
            output_reader,
            output_named[row["baseline_pdf_destination"]],
        )
    ]
    if mismatched_aliases:
        raise RuntimeError(
            f"Stable aliases differ from baselines: {mismatched_aliases[:20]}"
        )

    unresolved_output_actions: list[tuple[int, str]] = []
    output_goto_actions = 0
    stable_output_actions = 0
    for page_number, page in enumerate(output_reader.pages, 1):
        for annotation_ref in page.get("/Annots", []):
            annotation = annotation_ref.get_object()
            if annotation.get("/Subtype") != "/Link":
                continue
            action_ref = annotation.get("/A")
            if action_ref is None:
                continue
            action = action_ref.get_object()
            if action.get("/S") != "/GoTo":
                continue
            output_goto_actions += 1
            destination = str(action.get("/D"))
            if destination in target_ids:
                stable_output_actions += 1
            if destination not in output_named:
                unresolved_output_actions.append((page_number, destination))
    if unresolved_output_actions:
        raise RuntimeError(
            "Output GoTo actions do not resolve: "
            f"{unresolved_output_actions[:20]}"
        )
    if output_goto_actions != input_goto_actions:
        raise RuntimeError(
            f"GoTo action count changed from {input_goto_actions} "
            f"to {output_goto_actions}"
        )
    if stable_output_actions != output_goto_actions:
        raise RuntimeError(
            f"Only {stable_output_actions}/{output_goto_actions} GoTo "
            "actions use stable targets"
        )

    print(
        {
            "input_named_destinations": len(destinations),
            "stable_aliases_added": len(rows),
            "output_named_destinations": len(output_named),
            "existing_coordinates_changed": len(changed_existing),
            "alias_coordinate_mismatches": len(mismatched_aliases),
            "goto_actions_rewritten": rewritten_actions,
            "action_overrides_applied": len(applied_overrides),
            "output_goto_actions": output_goto_actions,
            "stable_output_goto_actions": stable_output_actions,
            "unresolved_output_goto_actions": len(unresolved_output_actions),
            "output": str(output_pdf),
        }
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
