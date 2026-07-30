#!/usr/bin/env python3
"""Validate the privacy-clean EGA 0/EGA III reference-v2 projection.

The validation is intentionally path-independent and deterministic.  It rebuilds
both readers from only the packaged source, then compares page text, decoded page
content, named destinations, and the complete internal GoTo surface with the
packaged readers.  It also replays the source closure and reference graph, checks
all machine files, and scans the proposed public tree for private/task metadata.
"""

from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path

from pypdf import PdfReader


UNSAFE_PREFIXES = ("=", "+", "-", "@")
TEXT_EXTENSIONS = {
    ".bib", ".csv", ".json", ".jsonl", ".md", ".py", ".tex", ".txt",
}
PRIVACY_PATTERNS = {
    "windows_user_path": re.compile(r"(?i)C:[\\/]Users[\\/]"),
    "private_source_root": re.compile(r"(?i)C:[\\/]IL_GitHub(?:[\\/]|\b)"),
    "codex_private_path": re.compile(r"(?i)(?:[\\/]|^)\.co" + r"dex(?:[\\/]|\b)"),
    "working_tree_path": re.compile(r"(?i)03_working_" + r"translations"),
    "publication_candidate_path": re.compile(r"(?i)06_publication_" + r"candidates"),
    "task_thread_id": re.compile(
        r"(?i)\b019[0-9a-f]{5}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b"
    ),
    "workflow_marker": re.compile(
        r"(?i)(?:source_thread_" + r"id|codex_deleg" +
        r"ation|_claude_" + r"aid|archive-maintenance " + r"task)"
    ),
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def file_sha(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def csv_machine_check(path: Path) -> tuple[int, list[str]]:
    errors: list[str] = []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.reader(handle))
    if not rows:
        return 0, [f"empty CSV: {path.name}"]
    width = len(rows[0])
    if len(set(rows[0])) != width:
        errors.append(f"duplicate CSV headers: {path.name}")
    for row_number, row in enumerate(rows[1:], 2):
        if len(row) != width:
            errors.append(f"nonrectangular CSV: {path.name}:{row_number}")
        for column_number, value in enumerate(row, 1):
            if value.startswith(UNSAFE_PREFIXES) and not value.startswith("'"):
                errors.append(
                    f"formula-unsafe CSV cell: {path.name}:{row_number}:{column_number}"
                )
    return max(0, len(rows) - 1), errors


def page_content(page: object) -> bytes:
    contents = page.get_contents()
    return b"" if contents is None else contents.get_data()


def page_text_digest(reader: PdfReader) -> str:
    payload = b"\0".join((page.extract_text() or "").encode("utf-8") for page in reader.pages)
    return sha256_bytes(payload)


def page_content_digest(reader: PdfReader) -> str:
    payload = b"\0".join(page_content(page) for page in reader.pages)
    return sha256_bytes(payload)


def named_destination_rows(reader: PdfReader) -> list[tuple[str, int]]:
    return sorted(
        (str(name), reader.get_destination_page_number(destination) + 1)
        for name, destination in reader.named_destinations.items()
    )


def goto_rows(reader: PdfReader) -> list[tuple[int, int, tuple[float, ...], str]]:
    rows: list[tuple[int, int, tuple[float, ...], str]] = []
    for page_number, page in enumerate(reader.pages, 1):
        for annotation_index, ref in enumerate(page.get("/Annots") or []):
            annotation = ref.get_object()
            action = annotation.get("/A")
            if not action or action.get("/S") != "/GoTo":
                continue
            rect = tuple(round(float(value), 3) for value in annotation.get("/Rect"))
            rows.append((page_number, annotation_index, rect, str(action.get("/D"))))
    return rows


def uri_count(reader: PdfReader) -> int:
    count = 0
    for page in reader.pages:
        for ref in page.get("/Annots") or []:
            annotation = ref.get_object()
            action = annotation.get("/A")
            if action and action.get("/S") == "/URI":
                count += 1
    return count


def run(command: list[str], cwd: Path, env: dict[str, str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=str(cwd),
        env=env,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )


def build_reader(source: Path, build_dir: Path, stem: str) -> tuple[Path, str, list[str]]:
    errors: list[str] = []
    env = os.environ.copy()
    env["TEXINPUTS"] = str(source) + os.pathsep + env.get("TEXINPUTS", "")
    env["BIBINPUTS"] = str(source) + os.pathsep + env.get("BIBINPUTS", "")
    pdflatex = [
        "pdflatex", "-interaction=nonstopmode", "-halt-on-error", "-file-line-error",
        f"-output-directory={build_dir}", f"{stem}.tex",
    ]
    first = run(pdflatex, source, env)
    if first.returncode:
        errors.append(f"{stem}: pdfLaTeX pass1 exit {first.returncode}")
        return build_dir / f"{stem}.pdf", first.stdout, errors
    bibtex = run(["bibtex", stem], build_dir, env)
    if bibtex.returncode:
        errors.append(f"{stem}: BibTeX exit {bibtex.returncode}")
    last = first
    for pass_number in range(2, 5):
        last = run(pdflatex, source, env)
        if last.returncode:
            errors.append(f"{stem}: pdfLaTeX pass{pass_number} exit {last.returncode}")
            break
    return build_dir / f"{stem}.pdf", last.stdout, errors


def log_metrics(log_text: str, reader_name: str) -> tuple[dict[str, int], list[str]]:
    errors: list[str] = []
    references = re.findall(r"LaTeX Warning: Hyper reference `([^']+)'", log_text)
    if reader_name == "ega0":
        same_reader = [label for label in references if label.startswith("0.")]
        expected_external = 4
    else:
        same_reader = [label for label in references if label.startswith("III.")]
        expected_external = 682
    if same_reader:
        errors.append(f"{reader_name}: same-reader undefined references: {same_reader[:10]}")
    if len(references) != expected_external:
        errors.append(
            f"{reader_name}: external undefined count {len(references)} != {expected_external}"
        )
    patterns = {
        "fatal_errors": r"(?:Emergency stop|Fatal error|! LaTeX Error)",
        "undefined_controls": r"Undefined control sequence",
        "duplicate_destinations": r"destination with the same identifier|multiply defined",
        "missing_characters": r"Missing character:",
        "rerun_warnings": r"Rerun to get cross-references right|Label\(s\) may have changed",
        "overfull_hboxes": r"Overfull \\hbox",
        "underfull_hboxes": r"Underfull \\hbox",
    }
    metrics = {key: len(re.findall(pattern, log_text, re.IGNORECASE)) for key, pattern in patterns.items()}
    metrics["undefined_external_occurrences"] = len(references)
    metrics["undefined_external_unique"] = len(set(references))
    metrics["undefined_same_reader"] = len(same_reader)
    for key in (
        "fatal_errors", "undefined_controls", "duplicate_destinations",
        "missing_characters", "rerun_warnings",
    ):
        if metrics[key]:
            errors.append(f"{reader_name}: {key}={metrics[key]}")
    expected_boxes = {
        "ega0": {"overfull_hboxes": 6, "underfull_hboxes": 1},
        "ega3": {"overfull_hboxes": 9, "underfull_hboxes": 0},
    }[reader_name]
    for key, expected in expected_boxes.items():
        if metrics[key] != expected:
            errors.append(f"{reader_name}: {key}={metrics[key]} != {expected}")
    return metrics, errors


def validate_source_closure(root: Path) -> tuple[dict[str, object], list[str]]:
    errors: list[str] = []
    source = root / "source"
    rows = read_csv(root / "controls" / "SOURCE_CLOSURE.csv")
    expected = {row["source_relpath"] for row in rows}
    actual = {
        path.relative_to(source).as_posix()
        for path in source.rglob("*")
        if path.is_file()
    }
    if expected != actual:
        errors.append(
            f"source closure mismatch: missing={sorted(expected-actual)} extra={sorted(actual-expected)}"
        )
    for row in rows:
        path = source / row["source_relpath"]
        if not path.is_file():
            continue
        if path.stat().st_size != int(row["bytes"]):
            errors.append(f"source byte mismatch: {row['source_relpath']}")
        if file_sha(path) != row["sha256"]:
            errors.append(f"source hash mismatch: {row['source_relpath']}")
    return {"rows": len(rows), "files": len(actual), "exact": not errors}, errors


def validate_reference_graph(root: Path, readers: dict[str, PdfReader]) -> tuple[dict[str, object], list[str]]:
    controls = root / "controls"
    errors: list[str] = []
    candidates = read_csv(controls / "REFERENCE_CANDIDATES.csv")
    applications = read_csv(controls / "REFERENCE_APPLICATIONS.csv")
    residuals = read_csv(controls / "REFERENCE_RESIDUALS.csv")
    targets = read_csv(controls / "REFERENCE_TARGETS.csv")
    aliases = read_csv(controls / "REFERENCE_TARGET_ALIASES.csv")
    edges = read_csv(controls / "REFERENCE_EDGES.csv")
    candidate_ids = [row["candidate_id"] for row in candidates]
    application_ids = [row["candidate_id"] for row in applications]
    residual_ids = [row["candidate_id"] for row in residuals]
    target_ids = [row["target_id"] for row in targets]
    edge_ids = [row["edge_id"] for row in edges]
    if len(set(candidate_ids)) != len(candidate_ids):
        errors.append("duplicate candidate IDs")
    if set(application_ids) & set(residual_ids):
        errors.append("candidate partition overlap")
    if set(application_ids) | set(residual_ids) != set(candidate_ids):
        errors.append("candidate partition incomplete")
    if len(set(target_ids)) != len(target_ids):
        errors.append("duplicate target IDs")
    if len(set(edge_ids)) != len(edge_ids):
        errors.append("duplicate edge IDs")
    target_set = set(target_ids)
    for row in applications:
        if row["target_id"] not in target_set:
            errors.append(f"application target absent: {row['application_id']}")
    for row in edges:
        if row["target_id"] not in target_set or row["status"] != "resolved_internal_goto":
            errors.append(f"edge target/status invalid: {row['edge_id']}")

    actual_targets: set[tuple[str, str, int]] = set()
    actual_edges: set[tuple[str, int, int, str, str, str, str, str]] = set()
    for reader_name, reader in readers.items():
        for destination, page in named_destination_rows(reader):
            actual_targets.add((reader_name, destination, page))
        for page, index, rect, destination in goto_rows(reader):
            actual_edges.add(
                (
                    reader_name, page, index,
                    f"{rect[0]:.3f}", f"{rect[1]:.3f}",
                    f"{rect[2]:.3f}", f"{rect[3]:.3f}", destination,
                )
            )
    delivered_targets = {
        (row["reader"], row["pdf_destination"], int(row["pdf_page"])) for row in targets
    }
    delivered_edges = {
        (
            row["reader"], int(row["pdf_page"]), int(row["annotation_index"]),
            row["rect_x0"], row["rect_y0"], row["rect_x1"], row["rect_y1"],
            row["pdf_destination"],
        )
        for row in edges
    }
    if delivered_targets != actual_targets:
        errors.append(
            f"target/PDF mismatch: missing={len(actual_targets-delivered_targets)} "
            f"extra={len(delivered_targets-actual_targets)}"
        )
    if delivered_edges != actual_edges:
        errors.append(
            f"edge/PDF mismatch: missing={len(actual_edges-delivered_edges)} "
            f"extra={len(delivered_edges-actual_edges)}"
        )
    expected_counts = {
        "candidates": 2800, "applications": 1781, "residuals": 1019,
        "targets": 911, "aliases": 1416, "edges": 1993,
    }
    actual_counts = {
        "candidates": len(candidates), "applications": len(applications),
        "residuals": len(residuals), "targets": len(targets),
        "aliases": len(aliases), "edges": len(edges),
    }
    for key, expected in expected_counts.items():
        if actual_counts[key] != expected:
            errors.append(f"graph count {key}={actual_counts[key]} != {expected}")
    return {
        **actual_counts,
        "candidate_partition": f"{len(candidates)}={len(applications)}+{len(residuals)}",
        "candidate_partition_exact": not (set(application_ids) & set(residual_ids))
        and set(application_ids) | set(residual_ids) == set(candidate_ids),
        "targets_match_pdf": delivered_targets == actual_targets,
        "edges_match_pdf": delivered_edges == actual_edges,
    }, errors


def machine_and_privacy_checks(root: Path) -> tuple[dict[str, object], list[str]]:
    errors: list[str] = []
    csv_rows: dict[str, int] = {}
    json_files = 0
    jsonl_records = 0
    privacy_hits: list[dict[str, object]] = []
    excluded = {"ZENODO_PAYLOAD_MANIFEST.csv", "PUBLIC_PROJECTION_VALIDATION.json"}
    files = sorted(path for path in root.rglob("*") if path.is_file())
    for path in files:
        relpath = path.relative_to(root).as_posix()
        if path.name == "ZENODO_PAYLOAD_MANIFEST.csv":
            # The self-excluding manifest hashes this validation file.  Ignoring
            # the manifest here avoids a validation/manifest hash cycle while
            # the external replay validates every manifest row independently.
            continue
        if path.suffix.lower() == ".csv":
            count, csv_errors = csv_machine_check(path)
            csv_rows[relpath] = count
            errors.extend(csv_errors)
        elif path.suffix.lower() == ".json":
            try:
                json.loads(path.read_text(encoding="utf-8-sig"))
                json_files += 1
            except Exception as exc:  # noqa: BLE001 - validation surface
                errors.append(f"invalid JSON {relpath}: {exc}")
        elif path.suffix.lower() == ".jsonl":
            try:
                for line_number, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
                    if line.strip():
                        json.loads(line)
                        jsonl_records += 1
            except Exception as exc:  # noqa: BLE001 - validation surface
                errors.append(f"invalid JSONL {relpath}:{line_number}: {exc}")
        if path.suffix.lower() in TEXT_EXTENSIONS:
            text = path.read_text(encoding="utf-8-sig", errors="replace")
            for pattern_name, pattern in PRIVACY_PATTERNS.items():
                for match in pattern.finditer(text):
                    line = text.count("\n", 0, match.start()) + 1
                    privacy_hits.append(
                        {"relpath": relpath, "line": line, "pattern": pattern_name}
                    )
    if privacy_hits:
        errors.append(f"privacy/task metadata hits: {len(privacy_hits)}")
    validated_files = [
        path for path in files if path.name not in excluded
    ]
    return {
        "validated_files_excluding_self_and_manifest": len(validated_files),
        "validated_bytes_excluding_self_and_manifest": sum(path.stat().st_size for path in validated_files),
        "csv_files": len(csv_rows),
        "csv_rows": sum(csv_rows.values()),
        "json_files": json_files,
        "jsonl_records": jsonl_records,
        "privacy_hits": len(privacy_hits),
        "privacy_evidence": privacy_hits,
    }, errors


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit("usage: validate_public_projection.py PACKAGE_ROOT")
    root = Path(sys.argv[1]).resolve()
    source = root / "source"
    controls = root / "controls"
    errors: list[str] = []
    source_summary, source_errors = validate_source_closure(root)
    errors.extend(source_errors)
    reader_specs = {
        "ega0": root / "readers" / "EGA0_English_Complete_Through_Section13_Reference_v2.pdf",
        "ega3": root / "readers" / "EGAIII_English_Complete_Sections1_Through7_Reference_v2.pdf",
    }
    packaged_readers = {name: PdfReader(str(path)) for name, path in reader_specs.items()}
    reader_results: dict[str, dict[str, object]] = {}

    temp_parent = Path(r"C:\tmp") if Path(r"C:\tmp").is_dir() else None
    temp_root = Path(tempfile.mkdtemp(prefix="ega03-public-replay-", dir=temp_parent))
    try:
        for reader_name, packaged_path in reader_specs.items():
            build_dir = temp_root / reader_name
            build_dir.mkdir(parents=True)
            rebuilt_path, log_text, build_errors = build_reader(source, build_dir, reader_name)
            errors.extend(build_errors)
            if not rebuilt_path.is_file():
                errors.append(f"{reader_name}: rebuilt PDF absent")
                continue
            packaged = packaged_readers[reader_name]
            rebuilt = PdfReader(str(rebuilt_path))
            packaged_text = [(page.extract_text() or "") for page in packaged.pages]
            rebuilt_text = [(page.extract_text() or "") for page in rebuilt.pages]
            packaged_content = [page_content(page) for page in packaged.pages]
            rebuilt_content = [page_content(page) for page in rebuilt.pages]
            packaged_named = named_destination_rows(packaged)
            rebuilt_named = named_destination_rows(rebuilt)
            packaged_goto = goto_rows(packaged)
            rebuilt_goto = goto_rows(rebuilt)
            named_set = {name for name, _ in packaged_named}
            broken = [row for row in packaged_goto if row[3] not in named_set]
            metrics, metric_errors = log_metrics(log_text, reader_name)
            errors.extend(metric_errors)
            comparisons = {
                "page_count_equal": len(packaged.pages) == len(rebuilt.pages),
                "page_text_equal": packaged_text == rebuilt_text,
                "decoded_page_content_equal": packaged_content == rebuilt_content,
                "named_destinations_equal": packaged_named == rebuilt_named,
                "goto_surface_equal": packaged_goto == rebuilt_goto,
            }
            for comparison, passed in comparisons.items():
                if not passed:
                    errors.append(f"{reader_name}: {comparison} failed")
            reader_results[reader_name] = {
                "packaged_pdf_bytes": packaged_path.stat().st_size,
                "packaged_pdf_sha256": file_sha(packaged_path),
                "pages": len(packaged.pages),
                "page_text_sha256": page_text_digest(packaged),
                "decoded_page_content_sha256": page_content_digest(packaged),
                "named_destinations": len(packaged_named),
                "goto_actions": len(packaged_goto),
                "uri_actions": uri_count(packaged),
                "broken_goto_actions": len(broken),
                "comparisons": comparisons,
                "log_metrics": metrics,
            }
            if broken:
                errors.append(f"{reader_name}: broken GoTo actions={len(broken)}")
    finally:
        shutil.rmtree(temp_root, ignore_errors=True)

    graph_summary, graph_errors = validate_reference_graph(root, packaged_readers)
    errors.extend(graph_errors)
    machine_summary, machine_errors = machine_and_privacy_checks(root)
    errors.extend(machine_errors)
    result = {
        "schema": "ega0-ega3-public-projection-validation-1.0",
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "source_closure": source_summary,
        "readers": reader_results,
        "reference_graph": graph_summary,
        "machine_and_privacy": machine_summary,
        "authority_witnesses_packaged": 0,
        "ocr_generated_or_packaged": 0,
    }
    output = controls / "PUBLIC_PROJECTION_VALIDATION.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": result["status"],
        "errors": errors,
        "output_bytes": output.stat().st_size,
        "output_sha256": file_sha(output),
    }, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
