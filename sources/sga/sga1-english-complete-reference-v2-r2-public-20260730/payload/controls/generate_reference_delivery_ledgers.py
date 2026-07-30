#!/usr/bin/env python3
"""Generate the complete SGA 1 reference-v2 delivery ledgers.

The source-candidate universe is deliberately separate from the PDF edge
universe:

* candidates = 31 source applications + 189 justified residuals;
* edges = every internal GoTo action in the delivered PDF, inherited or new.

This script never edits TeX or PDF.  It derives ledgers from the reviewed
source, the pre-application candidate history, and the final stable-alias PDF.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable

import fitz
from pypdf import PdfReader


LINK_RE = re.compile(
    r"\\hyperref\[([^\]]+)\]\{([^{}]*)\}"
    r"|\\hyperlink\{([^{}]+)\}\{([^{}]*)\}"
)
INPUT_RE = re.compile(r"\\input\{([^{}]+)\}")
UNSAFE_CSV_PREFIXES = ("=", "+", "-", "@")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def row_safe(value: object) -> str:
    text = "" if value is None else str(value)
    if text.startswith(UNSAFE_CSV_PREFIXES):
        return "'" + text
    return text


def write_csv(path: Path, fieldnames: list[str], rows: Iterable[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=fieldnames, lineterminator="\n"
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {field: row_safe(row.get(field, "")) for field in fieldnames}
            )


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def rect_tuple(annotation: object) -> tuple[float, ...]:
    return tuple(round(float(value), 3) for value in annotation.get("/Rect", []))


def page_content(page: object) -> bytes:
    contents = page.get_contents()
    return b"" if contents is None else contents.get_data()


def goto_actions(reader: PdfReader) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for page_number, page in enumerate(reader.pages, 1):
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
            rows.append(
                {
                    "pdf_page": page_number,
                    "annotation_index": annotation_index,
                    "rect": rect_tuple(annotation),
                    "destination": str(action.get("/D")),
                }
            )
    return rows


def resolve_input(root: Path, current: Path, raw: str) -> Path:
    candidate = (current.parent / raw).resolve()
    if candidate.exists():
        return candidate
    candidate = (root / raw).resolve()
    if candidate.exists():
        return candidate
    if not Path(raw).suffix:
        for suffix in (".tex", ".texfrag"):
            candidate = (current.parent / f"{raw}{suffix}").resolve()
            if candidate.exists():
                return candidate
            candidate = (root / f"{raw}{suffix}").resolve()
            if candidate.exists():
                return candidate
    raise FileNotFoundError(f"Cannot resolve input {raw!r} from {current}")


def active_link_occurrences(root: Path) -> list[dict[str, object]]:
    master = root / "SGA1_English_source_sync_workpass.tex"
    occurrences: list[dict[str, object]] = []
    active_stack: list[Path] = []

    def walk(path: Path) -> None:
        resolved = path.resolve()
        if resolved in active_stack:
            raise RuntimeError(f"Recursive TeX input cycle at {resolved}")
        active_stack.append(resolved)
        text = resolved.read_text(encoding="utf-8")
        relpath = resolved.relative_to(root).as_posix()
        for line_number, raw_line in enumerate(text.splitlines(), 1):
            line = re.split(r"(?<!\\)%", raw_line, maxsplit=1)[0]
            events: list[tuple[int, str, object]] = []
            for match in INPUT_RE.finditer(line):
                events.append((match.start(), "input", match))
            for match in LINK_RE.finditer(line):
                events.append((match.start(), "link", match))
            for _, event_kind, match in sorted(events, key=lambda item: item[0]):
                if event_kind == "input":
                    walk(resolve_input(root, resolved, match.group(1)))
                    continue
                if match.group(1) is not None:
                    target_label = match.group(1)
                    visible_text = match.group(2)
                    command_kind = "hyperref"
                else:
                    hyperlink_target = match.group(3)
                    target_label = (
                        "bib:VI.1"
                        if hyperlink_target == "cite.VI.1"
                        else hyperlink_target
                    )
                    visible_text = match.group(4)
                    command_kind = "hyperlink"
                occurrences.append(
                    {
                        "document_order": len(occurrences) + 1,
                        "source_relpath": relpath,
                        "current_source_line": line_number,
                        "current_source_column": match.start() + 1,
                        "target_label": target_label,
                        "visible_text": visible_text,
                        "command_kind": command_kind,
                        "link_command": match.group(0),
                        "current_source_sha256": sha256(resolved),
                    }
                )
        active_stack.pop()

    walk(master)
    return occurrences


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit("usage: generate_reference_delivery_ledgers.py ROOT")
    root = Path(sys.argv[1]).resolve()
    controls = root / "controls"
    baseline_pdf = (
        root
        / "build_hypertexnames_false"
        / "SGA1_English_source_sync_workpass.pdf"
    )
    raw_pdf = (
        root
        / "build_raw_links_r2_source_footnote_anchors"
        / "SGA1_English_source_sync_workpass.pdf"
    )
    final_pdf = (
        root
        / "build_stable_alias_overlay_r6_source_complete"
        / "SGA1_English_complete_reference_reader.pdf"
    )

    candidates_path = controls / "REFERENCE_CANDIDATES.csv"
    targets_path = controls / "REFERENCE_TARGETS.csv"
    overrides_path = controls / "REFERENCE_ACTION_OVERRIDES.csv"
    candidates = read_csv(candidates_path)
    targets = read_csv(targets_path)
    override_history = read_csv(overrides_path)
    overrides = [
        row for row in override_history if row["status"] == "active"
    ]
    target_by_id = {row["target_id"]: row for row in targets}
    target_ids = set(target_by_id)

    application_candidates = [
        row for row in candidates if row["disposition"] == "insert_link"
    ]
    residual_candidates = [
        row for row in candidates if row["disposition"] == "positive_residual"
    ]
    unexpected_dispositions = sorted(
        {
            row["disposition"]
            for row in candidates
            if row["disposition"] not in {"insert_link", "positive_residual"}
        }
    )

    occurrences = active_link_occurrences(root)
    occurrences_by_key: dict[tuple[str, str, str], list[dict]] = defaultdict(list)
    for occurrence in occurrences:
        key = (
            str(occurrence["source_relpath"]),
            str(occurrence["target_label"]),
            str(occurrence["visible_text"]),
        )
        occurrences_by_key[key].append(occurrence)
    candidates_by_key: dict[tuple[str, str, str], list[dict]] = defaultdict(list)
    for candidate in application_candidates:
        key = (
            candidate["source_relpath"],
            candidate["target_label"],
            candidate["visible_text"],
        )
        candidates_by_key[key].append(candidate)

    applications: list[dict[str, object]] = []
    application_errors: list[str] = []
    for key in sorted(set(occurrences_by_key) | set(candidates_by_key)):
        source_occurrences = sorted(
            occurrences_by_key.get(key, []),
            key=lambda row: (
                int(row["current_source_line"]),
                int(row["current_source_column"]),
            ),
        )
        source_candidates = sorted(
            candidates_by_key.get(key, []),
            key=lambda row: (
                int(row["source_line"]),
                int(row["source_column"]),
                row["candidate_id"],
            ),
        )
        if len(source_occurrences) != len(source_candidates):
            application_errors.append(
                f"application occurrence mismatch {key}: "
                f"{len(source_occurrences)} source commands vs "
                f"{len(source_candidates)} candidates"
            )
            continue
        for occurrence, candidate in zip(source_occurrences, source_candidates):
            applications.append(
                {
                    "application_id": candidate["candidate_id"].replace(
                        ".candidate.", ".application.", 1
                    ),
                    "candidate_id": candidate["candidate_id"],
                    "document_order": occurrence["document_order"],
                    "source_relpath": occurrence["source_relpath"],
                    "preapplication_source_line": candidate["source_line"],
                    "current_source_line": occurrence["current_source_line"],
                    "current_source_column": occurrence["current_source_column"],
                    "visible_text": candidate["visible_text"],
                    "target_label": candidate["target_label"],
                    "target_id": candidate["target_id"],
                    "command_kind": occurrence["command_kind"],
                    "link_command": occurrence["link_command"],
                    "classification": candidate["classification"],
                    "reason": candidate["reason"],
                    "current_source_sha256": occurrence[
                        "current_source_sha256"
                    ],
                    "status": "applied_and_compiled",
                }
            )
    applications.sort(key=lambda row: int(row["document_order"]))

    residuals: list[dict[str, object]] = []
    for candidate in residual_candidates:
        residuals.append(
            {
                "residual_id": candidate["candidate_id"].replace(
                    ".candidate.", ".residual.", 1
                ),
                "candidate_id": candidate["candidate_id"],
                "source_relpath": candidate["source_relpath"],
                "source_line": candidate["source_line"],
                "source_column": candidate["source_column"],
                "visible_text": candidate["visible_text"],
                "normalized_locator": candidate["normalized_locator"],
                "classification": candidate["classification"],
                "target_label": candidate["target_label"],
                "target_id": candidate["target_id"],
                "reason": candidate["reason"],
                "context": candidate["context"],
                "context_sha256": candidate["context_sha256"],
                "source_sha256_at_adjudication": candidate["source_sha256"],
                "status": "reviewed_positive_residual",
            }
        )

    baseline_reader = PdfReader(str(baseline_pdf))
    raw_reader = PdfReader(str(raw_pdf))
    final_reader = PdfReader(str(final_pdf))
    baseline_actions = goto_actions(baseline_reader)
    raw_actions = goto_actions(raw_reader)
    final_actions = goto_actions(final_reader)
    if len(raw_actions) != len(final_actions):
        raise RuntimeError("Raw/final GoTo action counts differ")
    baseline_rects = Counter(
        (row["pdf_page"], row["rect"]) for row in baseline_actions
    )
    new_action_flags: list[bool] = []
    for row in raw_actions:
        key = (row["pdf_page"], row["rect"])
        if baseline_rects[key]:
            baseline_rects[key] -= 1
            new_action_flags.append(False)
        else:
            new_action_flags.append(True)

    override_by_selector = {
        (int(row["pdf_page"]), int(row["annotation_index"])): row
        for row in overrides
    }
    applications_by_target: dict[str, list[dict]] = defaultdict(list)
    for application in applications:
        applications_by_target[str(application["target_id"])].append(application)
    for target_rows in applications_by_target.values():
        target_rows.sort(key=lambda row: int(row["document_order"]))
    new_edges_by_target: dict[str, list[int]] = defaultdict(list)
    for index, (is_new, final_action) in enumerate(
        zip(new_action_flags, final_actions)
    ):
        if is_new:
            new_edges_by_target[str(final_action["destination"])].append(index)
    application_for_edge: dict[int, str] = {}
    edge_application_errors: list[str] = []
    for target_id in sorted(
        set(applications_by_target) | set(new_edges_by_target)
    ):
        application_rows = applications_by_target.get(target_id, [])
        edge_indexes = new_edges_by_target.get(target_id, [])
        if len(application_rows) != len(edge_indexes):
            edge_application_errors.append(
                f"new-edge/application mismatch for {target_id}: "
                f"{len(edge_indexes)} edges vs {len(application_rows)} "
                "applications"
            )
            continue
        for edge_index, application in zip(edge_indexes, application_rows):
            application_for_edge[edge_index] = str(
                application["application_id"]
            )

    fitz_document = fitz.open(final_pdf)
    named_destinations = final_reader.named_destinations
    edges: list[dict[str, object]] = []
    for index, (raw_action, final_action, is_new) in enumerate(
        zip(raw_actions, final_actions, new_action_flags)
    ):
        if (
            raw_action["pdf_page"] != final_action["pdf_page"]
            or raw_action["annotation_index"]
            != final_action["annotation_index"]
            or raw_action["rect"] != final_action["rect"]
        ):
            raise RuntimeError(f"Raw/final annotation geometry changed at {index}")
        target_id = str(final_action["destination"])
        destination = named_destinations[target_id]
        target_page = final_reader.get_destination_page_number(destination) + 1
        rect = final_action["rect"]
        page = fitz_document[int(final_action["pdf_page"]) - 1]
        x0, y0, x1, y1 = rect
        crop = fitz.Rect(
            max(0, x0 - 1),
            max(0, page.rect.height - y1 - 1),
            min(page.rect.width, x1 + 1),
            min(page.rect.height, page.rect.height - y0 + 1),
        )
        visible_text = " ".join(page.get_textbox(crop).split())
        selector = (
            int(final_action["pdf_page"]),
            int(final_action["annotation_index"]),
        )
        override = override_by_selector.get(selector)
        if is_new:
            origin_class = "reviewed_source_application"
        elif override is not None:
            origin_class = "inherited_link_semantic_override"
        else:
            origin_class = "inherited_internal_link"
        identity_material = "|".join(
            [
                str(final_action["pdf_page"]),
                str(final_action["annotation_index"]),
                ",".join(f"{value:.3f}" for value in rect),
                target_id,
            ]
        )
        edge_id = "sga1.edge.sha256." + hashlib.sha256(
            identity_material.encode("utf-8")
        ).hexdigest()
        target = target_by_id.get(target_id, {})
        edges.append(
            {
                "edge_id": edge_id,
                "pdf_page": final_action["pdf_page"],
                "annotation_index": final_action["annotation_index"],
                "rect_x0": f"{x0:.3f}",
                "rect_y0": f"{y0:.3f}",
                "rect_x1": f"{x1:.3f}",
                "rect_y1": f"{y1:.3f}",
                "visible_text_from_rect": visible_text,
                "input_destination": raw_action["destination"],
                "target_id": target_id,
                "target_pdf_page": target_page,
                "target_view": str(destination.typ),
                "target_left": destination.left,
                "target_top": destination.top,
                "target_kind": target.get("kind", ""),
                "target_expose": target.get("expose", ""),
                "target_title": target.get("title", ""),
                "origin_class": origin_class,
                "application_id": application_for_edge.get(index, ""),
                "override_id": "" if override is None else override["override_id"],
                "status": "resolved_stable_goto",
            }
        )
    fitz_document.close()

    applications_path = controls / "REFERENCE_APPLICATIONS.csv"
    residuals_path = controls / "REFERENCE_RESIDUALS.csv"
    edges_path = controls / "REFERENCE_EDGES.csv"
    write_csv(
        applications_path,
        [
            "application_id",
            "candidate_id",
            "document_order",
            "source_relpath",
            "preapplication_source_line",
            "current_source_line",
            "current_source_column",
            "visible_text",
            "target_label",
            "target_id",
            "command_kind",
            "link_command",
            "classification",
            "reason",
            "current_source_sha256",
            "status",
        ],
        applications,
    )
    write_csv(
        residuals_path,
        [
            "residual_id",
            "candidate_id",
            "source_relpath",
            "source_line",
            "source_column",
            "visible_text",
            "normalized_locator",
            "classification",
            "target_label",
            "target_id",
            "reason",
            "context",
            "context_sha256",
            "source_sha256_at_adjudication",
            "status",
        ],
        residuals,
    )
    write_csv(
        edges_path,
        [
            "edge_id",
            "pdf_page",
            "annotation_index",
            "rect_x0",
            "rect_y0",
            "rect_x1",
            "rect_y1",
            "visible_text_from_rect",
            "input_destination",
            "target_id",
            "target_pdf_page",
            "target_view",
            "target_left",
            "target_top",
            "target_kind",
            "target_expose",
            "target_title",
            "origin_class",
            "application_id",
            "override_id",
            "status",
        ],
        edges,
    )

    errors: list[str] = []
    errors.extend(application_errors)
    errors.extend(edge_application_errors)
    if unexpected_dispositions:
        errors.append(
            f"unexpected candidate dispositions: {unexpected_dispositions}"
        )
    candidate_ids = {row["candidate_id"] for row in candidates}
    application_candidate_ids = {
        str(row["candidate_id"]) for row in applications
    }
    residual_candidate_ids = {str(row["candidate_id"]) for row in residuals}
    if application_candidate_ids & residual_candidate_ids:
        errors.append("application/residual candidate partition overlaps")
    if application_candidate_ids | residual_candidate_ids != candidate_ids:
        errors.append("application/residual partition does not cover candidates")
    if len(target_ids) != len(targets):
        errors.append("duplicate target IDs")
    if len({row["edge_id"] for row in edges}) != len(edges):
        errors.append("duplicate edge IDs")
    if len({row["application_id"] for row in applications}) != len(
        applications
    ):
        errors.append("duplicate application IDs")
    if len({row["residual_id"] for row in residuals}) != len(residuals):
        errors.append("duplicate residual IDs")
    unknown_edge_targets = sorted(
        {str(row["target_id"]) for row in edges} - target_ids
    )
    if unknown_edge_targets:
        errors.append(f"edge targets missing: {unknown_edge_targets[:20]}")
    if set(application_for_edge.values()) != {
        str(row["application_id"]) for row in applications
    }:
        errors.append("not every application maps to exactly one new PDF edge")
    if len([row for row in edges if row["origin_class"] == "reviewed_source_application"]) != len(
        applications
    ):
        errors.append("new edge count differs from application count")
    if {
        str(row["override_id"])
        for row in edges
        if row["override_id"]
    } != {row["override_id"] for row in overrides}:
        errors.append("action override coverage is not exact")

    raw_content_equal = sum(
        page_content(raw_reader.pages[index])
        == page_content(final_reader.pages[index])
        for index in range(len(raw_reader.pages))
    )
    raw_text_equal = sum(
        (raw_reader.pages[index].extract_text() or "")
        == (final_reader.pages[index].extract_text() or "")
        for index in range(len(raw_reader.pages))
    )
    baseline_text_equal = sum(
        (baseline_reader.pages[index].extract_text() or "")
        == (raw_reader.pages[index].extract_text() or "")
        for index in range(len(raw_reader.pages))
    )
    baseline_content_mismatches = [
        index + 1
        for index in range(len(raw_reader.pages))
        if page_content(baseline_reader.pages[index])
        != page_content(raw_reader.pages[index])
    ]
    raw_geometry = [
        (row["pdf_page"], row["annotation_index"], row["rect"])
        for row in raw_actions
    ]
    final_geometry = [
        (row["pdf_page"], row["annotation_index"], row["rect"])
        for row in final_actions
    ]
    if raw_content_equal != len(raw_reader.pages):
        errors.append("stable overlay changed decoded page content")
    if raw_text_equal != len(raw_reader.pages):
        errors.append("stable overlay changed extracted text")
    if raw_geometry != final_geometry:
        errors.append("stable overlay changed link geometry")
    if baseline_text_equal != len(raw_reader.pages):
        errors.append("reviewed source applications changed visible text")

    unsafe_cells: list[str] = []
    for csv_path in (applications_path, residuals_path, edges_path):
        for row_number, row in enumerate(read_csv(csv_path), 2):
            for column, value in row.items():
                if value.startswith(UNSAFE_CSV_PREFIXES):
                    unsafe_cells.append(f"{csv_path.name}:{row_number}:{column}")
    if unsafe_cells:
        errors.append(f"formula-unsafe CSV cells: {unsafe_cells[:20]}")

    validation = {
        "schema": "sga1-reference-v2-delivery-validation-1.0",
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "set_relation": {
            "candidate_universe": len(candidates),
            "applications": len(applications),
            "residuals": len(residuals),
            "formula": "REFERENCE_CANDIDATES = REFERENCE_APPLICATIONS disjoint-union REFERENCE_RESIDUALS",
            "partition_overlap": len(
                application_candidate_ids & residual_candidate_ids
            ),
            "partition_missing": len(
                candidate_ids
                - (application_candidate_ids | residual_candidate_ids)
            ),
            "pdf_edge_universe": len(edges),
            "edge_explanation": "REFERENCE_EDGES is the complete delivered-PDF GoTo graph; it includes inherited links and is not a partition member of the source-candidate universe.",
        },
        "counts": {
            "targets": len(targets),
            "edges": len(edges),
            "applications": len(applications),
            "residuals": len(residuals),
            "reviewed_source_application_edges": len(
                [
                    row
                    for row in edges
                    if row["origin_class"] == "reviewed_source_application"
                ]
            ),
            "semantic_override_edges": len(
                [
                    row
                    for row in edges
                    if row["origin_class"]
                    == "inherited_link_semantic_override"
                ]
            ),
            "inherited_internal_edges": len(
                [
                    row
                    for row in edges
                    if row["origin_class"] == "inherited_internal_link"
                ]
            ),
            "stable_named_destinations": len(final_reader.named_destinations),
            "final_pdf_pages": len(final_reader.pages),
        },
        "pdf_invariants": {
            "baseline_goto_actions": len(baseline_actions),
            "reviewed_source_build_goto_actions": len(raw_actions),
            "final_goto_actions": len(final_actions),
            "raw_to_final_content_pages_equal": raw_content_equal,
            "raw_to_final_text_pages_equal": raw_text_equal,
            "raw_to_final_link_geometry_equal": raw_geometry == final_geometry,
            "baseline_to_raw_text_pages_equal": baseline_text_equal,
            "baseline_to_raw_decoded_content_mismatch_pages": baseline_content_mismatches,
            "action_overrides": [
                {
                    "override_id": row["override_id"],
                    "pdf_page": int(row["pdf_page"]),
                    "annotation_index": int(row["annotation_index"]),
                    "input_destination": row["input_destination"],
                    "target_id": row["target_id"],
                }
                for row in overrides
            ],
        },
        "files": {
            path.name: {
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
            for path in (
                candidates_path,
                targets_path,
                overrides_path,
                applications_path,
                residuals_path,
                edges_path,
                baseline_pdf,
                raw_pdf,
                final_pdf,
            )
        },
    }
    validation_path = controls / "REFERENCE_GRAPH_VALIDATION.json"
    validation_path.write_text(
        json.dumps(validation, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "status": validation["status"],
                "errors": errors,
                "counts": validation["counts"],
                "validation": str(validation_path),
                "validation_sha256": sha256(validation_path),
            },
            indent=2,
        )
    )
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
