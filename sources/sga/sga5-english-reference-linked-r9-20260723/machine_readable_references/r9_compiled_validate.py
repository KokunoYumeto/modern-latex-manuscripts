#!/usr/bin/env python3
"""Compiled-state validation for the SGA5 exhaustive-reference R9 successor."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
import subprocess
from collections import Counter, defaultdict
from pathlib import Path

from pypdf import PdfReader


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def formula_prefix_hits(rows: list[dict[str, str]]) -> int:
    return sum(
        1
        for row in rows
        for value in row.values()
        if isinstance(value, str) and value.startswith(("=", "+", "-", "@"))
    )


def csv_rectangular(path: Path) -> tuple[bool, int]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.reader(handle))
    if not rows:
        return False, 0
    width = len(rows[0])
    return all(len(row) == width for row in rows), width


def content_stream_digest(reader: PdfReader) -> tuple[int, str]:
    digest = hashlib.sha256()
    total = 0
    for page in reader.pages:
        stream = page.get_contents()
        data = stream.get_data() if stream is not None else b""
        digest.update(data)
        total += len(data)
    return total, digest.hexdigest().upper()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True, type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    evidence = root / "machine_readable_references"
    build = evidence / "build_internal_r9"
    tex_path = root / "SGA5_English_sync_workpass.tex"
    pdf_path = root / "SGA5_English_sync_workpass.pdf"
    aux_path = root / "SGA5_English_sync_workpass.aux"
    log_path = root / "SGA5_English_sync_workpass.log"

    errors: list[str] = []
    tex = tex_path.read_text(encoding="utf-8")
    tex_lines = tex.splitlines()
    aux = aux_path.read_text(encoding="utf-8", errors="replace")
    log = log_path.read_text(encoding="utf-8", errors="replace")

    targets = read_csv(evidence / "REFERENCE_TARGETS.csv")
    edges = read_csv(evidence / "REFERENCE_EDGES.csv")
    candidates = read_csv(evidence / "REFERENCE_CANDIDATES.csv")
    residual = read_csv(evidence / "R9_EXHAUSTIVE_RESIDUAL_CLASSIFICATION.csv")
    postlink = read_csv(evidence / "R9_POSTLINK_RESIDUAL_RESCAN.csv")

    csv_sets = {
        "REFERENCE_TARGETS.csv": targets,
        "REFERENCE_EDGES.csv": edges,
        "REFERENCE_CANDIDATES.csv": candidates,
        "R9_EXHAUSTIVE_RESIDUAL_CLASSIFICATION.csv": residual,
        "R9_POSTLINK_RESIDUAL_RESCAN.csv": postlink,
    }
    csv_formula_hits = {name: formula_prefix_hits(rows) for name, rows in csv_sets.items()}
    csv_rectangularity = {
        name: {
            "rectangular": csv_rectangular(evidence / name)[0],
            "columns": csv_rectangular(evidence / name)[1],
        }
        for name in csv_sets
    }
    if not all(value["rectangular"] for value in csv_rectangularity.values()):
        errors.append(f"nonrectangular CSV: {csv_rectangularity}")
    if any(csv_formula_hits.values()):
        errors.append(f"CSV formula-prefix hits: {csv_formula_hits}")
    prohibited_disposition_re = re.compile(r"unadjudicated|ambiguous|unresolved", re.IGNORECASE)
    prohibited_disposition_rows = {
        name: sum(
            1
            for row in rows
            if prohibited_disposition_re.search(" | ".join(str(value) for value in row.values()))
        )
        for name, rows in csv_sets.items()
    }
    if any(prohibited_disposition_rows.values()):
        errors.append(f"prohibited candidate/residual dispositions: {prohibited_disposition_rows}")

    target_labels = [row["latex_label"] for row in targets]
    target_ids = [row["stable_id"] for row in targets]
    edge_ids = [row["edge_id"] for row in edges]
    candidate_ids = [row["candidate_id"] for row in candidates]
    for label, values in (
        ("target labels", target_labels),
        ("target IDs", target_ids),
        ("edge IDs", edge_ids),
        ("candidate IDs", candidate_ids),
    ):
        if len(values) != len(set(values)):
            errors.append(f"nonunique {label}")

    if tex.count("\\hyperref[") != len(edges):
        errors.append("TeX hyperref count does not equal edge count")
    if tex.count("\\label{sga5:") != len(targets):
        errors.append("TeX SGA5 label count does not equal target count")

    reader = PdfReader(str(pdf_path))
    named_destinations = reader.named_destinations
    named_names = set(named_destinations)

    aux_label_to_destination: dict[str, str] = {}
    target_page_mismatches: list[dict[str, object]] = []
    for row in targets:
        label = row["latex_label"]
        tex_token = f"\\label{{{label}}}"
        aux_token = f"\\newlabel{{{label}}}"
        if tex.count(tex_token) != 1:
            errors.append(f"target label TeX multiplicity is not one: {label}")
        aux_lines = [line for line in aux.splitlines() if line.startswith(aux_token)]
        if len(aux_lines) != 1:
            errors.append(f"target label AUX multiplicity is not one: {label}")
            continue
        destination_match = re.search(r"\{([^{}]+)\}\{\}\}\s*$", aux_lines[0])
        if not destination_match:
            errors.append(f"could not parse AUX destination for {label}")
            continue
        destination = destination_match.group(1)
        aux_label_to_destination[label] = destination
        if destination not in named_names:
            errors.append(f"compiled named destination missing: {label} -> {destination}")
            continue
        expected_page = row.get("pdf_page", "")
        if expected_page:
            actual_page = reader.get_destination_page_number(named_destinations[destination]) + 1
            if actual_page != int(expected_page):
                target_page_mismatches.append(
                    {"label": label, "expected": int(expected_page), "actual": actual_page}
                )
    if target_page_mismatches:
        errors.append(f"target page mismatches: {len(target_page_mismatches)}")

    target_by_label = {row["latex_label"]: row for row in targets}
    source_wrapper_failures: list[str] = []
    for row in edges:
        destination_label = row["destination_label"]
        target = target_by_label.get(destination_label)
        if target is None:
            errors.append(f"edge destination label absent from targets: {row['edge_id']}")
            continue
        if target["stable_id"] != row["destination_stable_id"]:
            errors.append(f"edge stable-ID mismatch: {row['edge_id']}")
        line_number = int(row["source_line"])
        wrapper = f"\\hyperref[{destination_label}]{{{row['visible_text']}}}"
        if line_number < 1 or line_number > len(tex_lines) or wrapper not in tex_lines[line_number - 1]:
            source_wrapper_failures.append(row["edge_id"])
    if source_wrapper_failures:
        errors.append(f"edge wrappers missing at source coordinates: {len(source_wrapper_failures)}")

    # Reverse only the 720 R9 wrappers at their frozen R8 coordinates.  This
    # is independent of the forward writer and proves exact R8 reconstruction,
    # including the extra grouping required inside tikz-cd arrow labels.
    r8_root = root.parent / "sga5_full_reader_reference_retrofit_r8"
    r8_tex_path = r8_root / "SGA5_English_sync_workpass.tex"
    baseline_bytes = r8_tex_path.read_bytes()
    baseline_lines = baseline_bytes.decode("utf-8").splitlines(keepends=True)
    reconstructed_lines = tex_path.read_bytes().decode("utf-8").splitlines(keepends=True)
    r9_edges_by_line: dict[int, list[dict[str, str]]] = defaultdict(list)
    for row in edges:
        if row["revision"] == "R9":
            r9_edges_by_line[int(row["source_line"])].append(row)
    reconstruction_wrapper_failures: list[str] = []
    for line_number, line_edges in sorted(r9_edges_by_line.items()):
        baseline_line = baseline_lines[line_number - 1]
        current_line = reconstructed_lines[line_number - 1]
        for row in sorted(line_edges, key=lambda item: int(item["source_column_1based"])):
            start = int(row["source_column_1based"]) - 1
            visible = row["visible_text"]
            wrapper = f"\\hyperref[{row['destination_label']}]{{{visible}}}"
            if "\\arrow" in baseline_line:
                wrapper = "{" + wrapper + "}"
            if current_line[start : start + len(wrapper)] != wrapper:
                reconstruction_wrapper_failures.append(row["edge_id"])
                continue
            current_line = current_line[:start] + visible + current_line[start + len(wrapper) :]
        reconstructed_lines[line_number - 1] = current_line
    reconstructed_bytes = "".join(reconstructed_lines).encode("utf-8")
    reconstructed_sha = hashlib.sha256(reconstructed_bytes).hexdigest().upper()
    baseline_sha = hashlib.sha256(baseline_bytes).hexdigest().upper()
    if reconstruction_wrapper_failures or reconstructed_bytes != baseline_bytes:
        errors.append(
            "removing only R9 markup did not reconstruct the exact R8 TeX "
            f"({len(reconstruction_wrapper_failures)} wrapper-coordinate failures)"
        )

    annotation_destinations: Counter[str] = Counter()
    link_annotations = 0
    goto_annotations = 0
    for page in reader.pages:
        for annotation_ref in page.get("/Annots", []):
            annotation = annotation_ref.get_object()
            if annotation.get("/Subtype") != "/Link":
                continue
            link_annotations += 1
            action_ref = annotation.get("/A")
            if action_ref is not None:
                action = action_ref.get_object()
                if action.get("/S") == "/GoTo":
                    goto_annotations += 1
                    annotation_destinations[str(action.get("/D"))] += 1
            elif annotation.get("/Dest") is not None:
                goto_annotations += 1
                annotation_destinations[str(annotation.get("/Dest"))] += 1

    expected_destination_counts: Counter[str] = Counter()
    for edge in edges:
        destination = aux_label_to_destination.get(edge["destination_label"])
        if destination:
            expected_destination_counts[destination] += 1
    short_destinations = {
        destination: {
            "expected_minimum": count,
            "compiled_annotations": annotation_destinations[destination],
        }
        for destination, count in expected_destination_counts.items()
        if annotation_destinations[destination] < count
    }
    if short_destinations:
        errors.append(f"compiled annotation counts below edge counts: {len(short_destinations)}")

    r8_reader = PdfReader(str(r8_root / "SGA5_English_sync_workpass.pdf"))
    r8_named_names = set(r8_reader.named_destinations)
    r8_link_annotations = 0
    r8_goto_annotations = 0
    for page in r8_reader.pages:
        for annotation_ref in page.get("/Annots", []):
            annotation = annotation_ref.get_object()
            if annotation.get("/Subtype") != "/Link":
                continue
            r8_link_annotations += 1
            action_ref = annotation.get("/A")
            if action_ref is not None and action_ref.get_object().get("/S") == "/GoTo":
                r8_goto_annotations += 1
            elif annotation.get("/Dest") is not None:
                r8_goto_annotations += 1
    missing_r8_named_destinations = sorted(r8_named_names - named_names)
    if missing_r8_named_destinations:
        errors.append(f"R8 named destinations lost: {len(missing_r8_named_destinations)}")
    if link_annotations < r8_link_annotations or goto_annotations < r8_goto_annotations:
        errors.append("R8 compiled link annotations were not preserved")
    if len(reader.pages) != len(r8_reader.pages):
        errors.append("R8/R9 page count differs")

    final_log_prohibited = re.compile(
        r"undefined references?|citation.+undefined|multiply defined|fatal error|"
        r"emergency stop|no output pdf|rerun to get cross-references right",
        re.IGNORECASE,
    )
    prohibited_log_lines = [
        line for line in log.splitlines() if final_log_prohibited.search(line)
    ]
    if prohibited_log_lines:
        errors.append(f"prohibited final-log diagnostics: {len(prohibited_log_lines)}")

    pass_aux_hashes = [sha256(build / f"R9_PASS{number}.aux") for number in (1, 2, 3)]
    pass_out_hashes = [sha256(build / f"R9_PASS{number}.out") for number in (1, 2, 3)]
    pass_pdf_hashes = [sha256(build / f"R9_PASS{number}.pdf") for number in (1, 2, 3)]
    pass_content = []
    pass_metadata = []
    for number in (1, 2, 3):
        pass_reader = PdfReader(str(build / f"R9_PASS{number}.pdf"))
        pass_content.append(content_stream_digest(pass_reader))
        pass_metadata.append(dict(pass_reader.metadata or {}))
    if len(set(pass_aux_hashes)) != 1 or len(set(pass_out_hashes)) != 1:
        errors.append("AUX/OUT did not converge across three passes")
    if len(set(pass_content)) != 1:
        errors.append("PDF decoded page-content streams did not converge")
    metadata_keys = sorted({key for metadata in pass_metadata for key in metadata})
    metadata_differing_keys = [
        key for key in metadata_keys if len({metadata.get(key) for metadata in pass_metadata}) > 1
    ]
    if set(metadata_differing_keys) - {"/CreationDate", "/ModDate"}:
        errors.append(f"non-time PDF metadata varied: {metadata_differing_keys}")

    layout_paths = [build / "R8_LAYOUT.txt", build / "R9_LAYOUT.txt"]
    flow_paths = [build / "R8_FLOW.txt", build / "R9_FLOW.txt"]
    layout_hashes = [sha256(path) for path in layout_paths]
    flow_hashes = [sha256(path) for path in flow_paths]
    if len(set(layout_hashes)) != 1 or len(set(flow_hashes)) != 1:
        errors.append("R8/R9 extracted visible text differs")

    pdffonts = shutil.which("pdffonts")
    if not pdffonts:
        errors.append("pdffonts executable unavailable")
        font_rows: list[list[str]] = []
    else:
        completed = subprocess.run(
            [pdffonts, str(pdf_path)], check=True, capture_output=True, text=True
        )
        font_rows = [line.split() for line in completed.stdout.splitlines()[2:] if line.strip()]
        if not font_rows or any(row[-5:-2] != ["yes", "yes", "yes"] for row in font_rows):
            errors.append("one or more fonts lack embedded/subset/Unicode status")

    postlink_summary = json.loads(
        (evidence / "R9_POSTLINK_RESIDUAL_RESCAN_SUMMARY.json").read_text(encoding="utf-8")
    )
    if (
        postlink_summary.get("status") != "PASS"
        or postlink_summary.get("unwrapped_internally_resolvable_occurrences") != 0
        or postlink_summary.get("unadjudicated_occurrences") != 0
    ):
        errors.append("postlink residual replay is not closed")

    classification_counts = Counter(row["classification"] for row in residual)
    final_nonedge_counts = Counter(row["classification"] for row in postlink)
    expected_classification_counts = {
        "linked_internal_edge": 720,
        "structural_declaration_tag": 945,
        "external_work_citation": 268,
        "typography_layout_geometry_value": 179,
        "unavailable_source_target": 6,
    }
    if dict(classification_counts) != expected_classification_counts:
        errors.append("prelink exhaustive classification counts changed")

    result = {
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "root": str(root),
        "r9_tex": {
            "bytes": tex_path.stat().st_size,
            "sha256": sha256(tex_path),
            "hyperref_wrappers": tex.count("\\hyperref["),
            "target_labels": tex.count("\\label{sga5:"),
        },
        "r9_pdf": {
            "bytes": pdf_path.stat().st_size,
            "sha256": sha256(pdf_path),
            "pages": len(reader.pages),
            "named_destinations": len(named_destinations),
            "link_annotations": link_annotations,
            "goto_annotations": goto_annotations,
            "fonts": len(font_rows),
            "fonts_embedded_subset_unicode": bool(font_rows)
            and all(row[-5:-2] == ["yes", "yes", "yes"] for row in font_rows),
        },
        "machine_graph": {
            "targets": len(targets),
            "edges": len(edges),
            "candidates": len(candidates),
            "source_wrapper_failures": len(source_wrapper_failures),
            "edge_destinations_below_expected_annotation_count": len(short_destinations),
            "target_page_mismatches": len(target_page_mismatches),
        },
        "source_reconstruction": {
            "baseline_r8_tex_bytes": len(baseline_bytes),
            "baseline_r8_tex_sha256": baseline_sha,
            "reconstructed_tex_bytes": len(reconstructed_bytes),
            "reconstructed_tex_sha256": reconstructed_sha,
            "r9_wrappers_removed": sum(len(rows) for rows in r9_edges_by_line.values()),
            "wrapper_coordinate_failures": len(reconstruction_wrapper_failures),
            "exact": reconstructed_bytes == baseline_bytes,
        },
        "r8_link_preservation": {
            "r8_pages": len(r8_reader.pages),
            "r9_pages": len(reader.pages),
            "r8_named_destinations": len(r8_named_names),
            "r9_named_destinations": len(named_names),
            "missing_r8_named_destinations": len(missing_r8_named_destinations),
            "r8_link_annotations": r8_link_annotations,
            "r9_link_annotations": link_annotations,
            "r8_goto_annotations": r8_goto_annotations,
            "r9_goto_annotations": goto_annotations,
        },
        "exhaustive_prelink_occurrences": len(residual),
        "exhaustive_prelink_classification_counts": dict(classification_counts),
        "postlink_unwrapped_occurrences": len(postlink),
        "postlink_final_classification_counts": dict(final_nonedge_counts),
        "csv_rows": {name: len(rows) for name, rows in csv_sets.items()},
        "csv_formula_prefix_hits": csv_formula_hits,
        "csv_rectangularity": csv_rectangularity,
        "csv_prohibited_disposition_rows": prohibited_disposition_rows,
        "build": {
            "passes": 3,
            "aux_sha256": pass_aux_hashes,
            "out_sha256": pass_out_hashes,
            "pdf_sha256": pass_pdf_hashes,
            "decoded_page_content_bytes_sha256": [
                {"bytes": size, "sha256": digest} for size, digest in pass_content
            ],
            "metadata_differing_keys": metadata_differing_keys,
            "pdf_byte_variance": (
                "CreationDate/ModDate and dependent trailer identity only; "
                "decoded page content and all non-time metadata exact"
            ),
            "prohibited_final_log_diagnostics": prohibited_log_lines,
        },
        "visible_text_preservation": {
            "r8_r9_layout_exact": len(set(layout_hashes)) == 1,
            "layout_sha256": layout_hashes,
            "r8_r9_flow_exact": len(set(flow_hashes)) == 1,
            "flow_sha256": flow_hashes,
        },
        "convention": {
            "path": str(evidence / "MACHINE_READABLE_INTERNAL_REFERENCES_CONVENTION_v2_EXHAUSTIVE.md"),
            "sha256": sha256(
                evidence / "MACHINE_READABLE_INTERNAL_REFERENCES_CONVENTION_v2_EXHAUSTIVE.md"
            ),
        },
    }
    output = evidence / "R9_COMPILED_REFERENCE_VALIDATION.json"
    output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
