#!/usr/bin/env python3
"""Inventory ephemeral SGA7 source-image evidence without copying the pixels."""

from __future__ import annotations

import argparse
import ast
import csv
import hashlib
import json
import re
import warnings
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

import fitz
from PIL import Image


Image.MAX_IMAGE_PIXELS = None
warnings.filterwarnings("ignore", category=SyntaxWarning)

FOLIO_OFFSET = 11
PRIVATE_MARKERS = (
    "c:\\users\\",
    "c:/users/",
    "appdata",
    "papors",
    "chatnotes",
    ".claude",
    ".codex",
)


@dataclass(frozen=True)
class RootSpec:
    root_id: str
    path: Path
    cutoff: float | None
    priority: int


@dataclass
class Job:
    tag: str
    page_index: int | None
    bbox: tuple[float, float, float, float] | None
    render_parameter: int | None


@dataclass
class ScriptInfo:
    root_id: str
    path: Path
    modified: float
    sha256: str
    source_class: str
    generator_kind: str
    output_patterns: list[re.Pattern[str]]
    jobs: list[Job]
    page_candidates: set[int]
    render_candidates: set[int]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--parent-pdf", type=Path, required=True)
    parser.add_argument(
        "--root",
        action="append",
        required=True,
        help="ROOT_ID=absolute scratchpad path; repeat in preference order",
    )
    parser.add_argument(
        "--cutoff",
        action="append",
        default=[],
        help="ROOT_ID=local ISO timestamp, for example 2026-07-28T21:16:00",
    )
    parser.add_argument("--review-log", type=Path)
    parser.add_argument("--project-root", type=Path)
    parser.add_argument(
        "--session-log",
        action="append",
        default=[],
        help="PUBLIC_LABEL=absolute Claude JSONL session log; repeat as needed",
    )
    parser.add_argument("--provenance-override", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def parse_key_values(values: list[str]) -> dict[str, str]:
    parsed: dict[str, str] = {}
    for value in values:
        key, separator, item = value.partition("=")
        if not separator or not key or not item:
            raise ValueError(f"Expected KEY=VALUE, got {value!r}")
        if key in parsed:
            raise ValueError(f"Duplicate key: {key}")
        parsed[key] = item
    return parsed


def root_specs(args: argparse.Namespace) -> list[RootSpec]:
    roots = parse_key_values(args.root)
    cutoffs = parse_key_values(args.cutoff)
    unknown = set(cutoffs) - set(roots)
    if unknown:
        raise ValueError(f"Cutoff without root: {sorted(unknown)}")
    result: list[RootSpec] = []
    for priority, (root_id, value) in enumerate(roots.items()):
        path = Path(value).resolve()
        if not path.is_dir():
            raise FileNotFoundError(path)
        cutoff = None
        if root_id in cutoffs:
            cutoff = datetime.fromisoformat(cutoffs[root_id]).timestamp()
        result.append(RootSpec(root_id, path, cutoff, priority))
    return result


def selected(path: Path, cutoff: float | None) -> bool:
    return cutoff is None or path.stat().st_mtime >= cutoff


def generator_kind(path: Path) -> str:
    name = path.name.lower()
    if re.search(r"crop|zoom|clip|glyph|detail|tight|snip|slice", name):
        return "targeted_crop"
    if re.search(r"compare|mask|diff|contact|good|bad", name):
        return "comparison"
    if re.search(r"render|page|band", name):
        return "routine_render"
    return "other"


def joined_pattern(node: ast.JoinedStr) -> re.Pattern[str] | None:
    pieces: list[str] = []
    literal_signal = ""
    for value in node.values:
        if isinstance(value, ast.Constant) and isinstance(value.value, str):
            basename = value.value.replace("\\", "/").split("/")[-1]
            pieces.append(re.escape(basename))
            literal_signal += basename
        elif isinstance(value, ast.FormattedValue):
            pieces.append(r".+?")
    expression = "".join(pieces)
    signal = re.sub(r"(?i)\.png$", "", literal_signal)
    if ".png" not in expression.lower() or not re.search(r"[a-z0-9]", signal):
        return None
    return re.compile(r"^.*" + expression + r"$", re.IGNORECASE)


def literal_value(node: ast.AST) -> object | None:
    if isinstance(node, ast.Constant) and isinstance(
        node.value, (str, int, float)
    ):
        return node.value
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        value = literal_value(node.operand)
        if isinstance(value, (int, float)):
            return -value
    return None


def job_from_values(values: list[object]) -> Job | None:
    strings = [value for value in values if isinstance(value, str)]
    if not strings:
        return None
    tag_candidates: list[tuple[int, str]] = []
    for value in strings:
        normalized = value.replace("\\", "/")
        basename = normalized.split("/")[-1]
        if not 1 <= len(basename) <= 160 or ".pdf" in basename.lower():
            continue
        if basename.lower().endswith(".png"):
            tag_candidates.append((0, basename))
        elif "/" not in normalized and ":" not in normalized:
            tag_candidates.append((1, basename))
    tag = min(tag_candidates, default=(99, ""))[1]
    if not tag:
        return None
    if tag.lower().endswith(".png"):
        tag = tag[:-4]
    page_index = next(
        (
            value
            for value in values
            if isinstance(value, int) and 0 <= value < 540
        ),
        None,
    )
    fractions = [
        float(value)
        for value in values
        if isinstance(value, (int, float)) and 0 <= value <= 1
    ]
    bbox = None
    if len(fractions) >= 4:
        candidate = tuple(fractions[:4])
        if candidate[0] < candidate[2] and candidate[1] < candidate[3]:
            bbox = candidate
    render_parameter = next(
        (
            value
            for value in reversed(values)
            if isinstance(value, int) and 600 <= value <= 12000
        ),
        None,
    )
    return Job(tag, page_index, bbox, render_parameter)


def script_info(root: RootSpec, path: Path, parent_name: str) -> ScriptInfo:
    text = path.read_text(encoding="utf-8", errors="replace")
    lowered = text.lower()
    if parent_name.lower() in lowered:
        source_class = "controlling_540_page_scan"
    elif "sga7-1.pdf" in lowered:
        source_class = "superseded_low_resolution_scan"
    elif "fitz.open" in lowered or "image.open" in lowered:
        source_class = "source_or_derived_dynamic_input"
    else:
        source_class = "non_image_helper"

    output_patterns: list[re.Pattern[str]] = []
    jobs: list[Job] = []
    page_candidates: set[int] = set()
    render_candidates: set[int] = set()
    try:
        tree = ast.parse(text)
    except (SyntaxError, ValueError):
        tree = None
    if tree is not None:
        literal_names: set[str] = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, str):
                basename = node.value.replace("\\", "/").split("/")[-1]
                if basename.lower().endswith(".png"):
                    literal_names.add(basename)
            elif isinstance(node, ast.JoinedStr):
                pattern = joined_pattern(node)
                if pattern:
                    output_patterns.append(pattern)
            elif isinstance(node, (ast.Tuple, ast.List)):
                values = [literal_value(item) for item in node.elts]
                if all(value is not None for value in values):
                    job = job_from_values(values)
                    if job:
                        jobs.append(job)
            elif isinstance(node, ast.Call):
                values = [literal_value(item) for item in node.args]
                compact = [value for value in values if value is not None]
                job = job_from_values(compact)
                if job:
                    jobs.append(job)
            elif (
                isinstance(node, ast.Subscript)
                and isinstance(node.value, ast.Name)
                and node.value.id.lower() in {"d", "doc", "document", "pdf"}
            ):
                value = literal_value(node.slice)
                if isinstance(value, int) and 0 <= value < 540:
                    page_candidates.add(value)
        output_patterns.extend(
            re.compile("^" + re.escape(value) + "$", re.IGNORECASE)
            for value in literal_names
        )
    for job in jobs:
        if job.page_index is not None:
            page_candidates.add(job.page_index)
        if job.render_parameter is not None:
            render_candidates.add(job.render_parameter)
    render_candidates.update(
        int(value)
        for value in re.findall(
            r"(?<![\d.])(\d{3,5})(?:\.0)?\s*/\s*72(?:\.0)?", text
        )
        if 300 <= int(value) <= 12000
    )
    render_candidates.update(
        int(value)
        for value in re.findall(
            r"(?i)\b(?:dpi|zoom|target)\s*=\s*(\d{3,5})(?:\.0)?", text
        )
        if 600 <= int(value) <= 12000
    )
    return ScriptInfo(
        root.root_id,
        path,
        path.stat().st_mtime,
        sha256(path),
        source_class,
        generator_kind(path),
        output_patterns,
        jobs,
        page_candidates,
        render_candidates,
    )


def infer_filename_page(name: str) -> tuple[int | None, str]:
    stem = Path(name).stem
    match = re.search(
        r"(?i)(?:^|[_-])idx[_-]?(\d{1,3})(?:[_-]|$)", stem
    )
    if match and 12 <= int(match.group(1)) <= 539:
        return int(match.group(1)), "explicit_idx_filename"
    match = re.search(
        r"(?i)(?:^|[_-])(?:page|pg|p)[_-]?(\d{1,3})(?:[_-]|$)", stem
    )
    if match and 12 <= int(match.group(1)) <= 539:
        return int(match.group(1)), "explicit_page_filename"
    numbers = [
        int(value)
        for value in re.findall(r"(?<!\d)(\d{1,4})(?!\d)", stem)
        if 12 <= int(value) <= 539
    ]
    if numbers:
        return numbers[0], "numeric_filename_inference"
    return None, "unresolved"


def match_job(name: str, script: ScriptInfo) -> Job | None:
    stem = Path(name).stem.lower()
    candidates = [
        job
        for job in script.jobs
        if job.tag.lower() == stem
        or job.tag.lower() in stem
        or stem in job.tag.lower()
    ]
    if not candidates:
        return None
    candidates.sort(
        key=lambda job: (
            job.tag.lower() != stem,
            -len(job.tag),
        )
    )
    return candidates[0]


def match_generator(
    name: str,
    modified: float,
    scripts: list[ScriptInfo],
    image_root_id: str,
) -> tuple[ScriptInfo | None, str]:
    patterned = [
        script
        for script in scripts
        if script.modified <= modified + 5
        and any(pattern.match(name) for pattern in script.output_patterns)
    ]
    if patterned:
        return max(
            patterned,
            key=lambda item: (
                match_job(name, item) is not None,
                item.root_id == image_root_id,
                item.modified,
                item.sha256,
            ),
        ), "output_pattern"
    nearby = [
        script
        for script in scripts
        if script.modified <= modified + 1
        and modified - script.modified <= 90
    ]
    if nearby:
        return max(
            nearby,
            key=lambda item: (
                item.root_id == image_root_id,
                item.modified,
                item.sha256,
            ),
        ), "nearest_preceding_90s"
    return None, "unresolved"


def review_pages(path: Path | None) -> set[int]:
    if path is None:
        return set()
    text = path.read_text(encoding="utf-8", errors="replace")
    pages = {
        int(value)
        for value in re.findall(r"(?i)\bidx\s*[= ]\s*(\d{1,3})\b", text)
        if 0 <= int(value) < 540
    }
    for first, last in re.findall(
        r"(?i)\bidx\s+(\d{1,3})\s*[\u2013-]\s*(\d{1,3})", text
    ):
        pages.update(range(int(first), int(last) + 1))
    return pages


def scope_for_page(page_index: int | None) -> tuple[str, str]:
    scopes = (
        (12, 35, "I", "expose_I_body.tex"),
        (36, 42, "II", "expose_II_body.tex"),
        (43, 143, "VI", "expose_VI_body.tex"),
        (144, 228, "VII", "expose_VII_body.tex"),
        (229, 323, "VIII", "expose_VIII_body.tex"),
        (324, 539, "IX", "expose_IX_body.tex"),
    )
    if page_index is not None:
        for first, last, expose, tex_name in scopes:
            if first <= page_index <= last:
                return expose, tex_name
    return "unmapped_front_matter_or_unresolved", ""


def page_confidence(method: str) -> str:
    if method in {
        "explicit_idx_filename",
        "explicit_page_filename",
        "generator_job",
        "single_generator_page",
    }:
        return "high"
    if method == "numeric_filename_inference":
        return "medium_filename_inference"
    return "unresolved"


def pixel_scope(name: str) -> str:
    lowered = name.lower()
    if re.fullmatch(r"(?:p|page|pg|mine_p)\d+\.png", lowered):
        return "routine_full_page_or_near_full_page"
    if re.search(r"(?:^|_)full(?:_|\.|$)", lowered):
        return "routine_full_page_or_near_full_page"
    return "targeted_region_or_detail"


def archive_member_path(visual_id: str, relative_path: str) -> str:
    basename = Path(relative_path).name
    safe = re.sub(r"[^A-Za-z0-9._-]+", "_", basename).strip("._")
    if not safe.lower().endswith(".png"):
        safe += ".png"
    return f"images/{visual_id}_{safe}"


def csv_write(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def csv_gate(path: Path) -> list[str]:
    errors: list[str] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.reader(handle))
    if not rows:
        return [f"empty_csv:{path.name}"]
    width = len(rows[0])
    for row_number, row in enumerate(rows, start=1):
        if len(row) != width:
            errors.append(
                f"nonrectangular_csv:{path.name}:row{row_number}:"
                f"{len(row)}!={width}"
            )
        for column_number, value in enumerate(row, start=1):
            if value.startswith(("=", "+", "-", "@")):
                errors.append(
                    f"formula_unsafe:{path.name}:row{row_number}:"
                    f"column{column_number}"
                )
    return errors


def json_write(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=True, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def tool_uses(value: object) -> list[dict[str, object]]:
    if not isinstance(value, dict):
        return []
    message = value.get("message")
    if not isinstance(message, dict):
        return []
    content = message.get("content")
    if not isinstance(content, list):
        return []
    return [
        item
        for item in content
        if isinstance(item, dict) and item.get("type") == "tool_use"
    ]


def normalized_windows_path(value: str) -> str:
    return value.replace("/", "\\").casefold()


def scan_read_events(
    session_logs: dict[str, str],
    image_path_lookup: dict[str, tuple[str, str]],
) -> tuple[
    list[dict[str, str]],
    list[dict[str, object]],
    set[str],
]:
    events: list[dict[str, str]] = []
    summaries: list[dict[str, object]] = []
    tool_source_sha256s: set[str] = set()
    for session_label, value in session_logs.items():
        path = Path(value).resolve()
        if not path.is_file():
            raise FileNotFoundError(path)
        initial = (path.stat().st_size, path.stat().st_mtime_ns)
        digest = hashlib.sha256()
        line_count = 0
        candidate_lines = 0
        malformed_lines = 0
        read_tool_uses = 0
        selected_image_reads = 0
        unmatched_image_reads = 0
        with path.open("rb") as handle:
            for raw in handle:
                digest.update(raw)
                line_count += 1
                if b'"tool_use"' not in raw:
                    continue
                candidate_lines += 1
                try:
                    record = json.loads(raw)
                except (UnicodeDecodeError, json.JSONDecodeError):
                    malformed_lines += 1
                    continue
                timestamp = str(record.get("timestamp") or "")
                for tool in tool_uses(record):
                    inputs = tool.get("input")
                    if not isinstance(inputs, dict):
                        continue
                    tool_name = tool.get("name")
                    if tool_name in {"Bash", "PowerShell"}:
                        source = inputs.get("command")
                    elif tool_name == "Write":
                        source = inputs.get("content")
                    else:
                        source = None
                    if isinstance(source, str):
                        tool_source_sha256s.add(
                            hashlib.sha256(source.encode("utf-8")).hexdigest().upper()
                        )
                    if tool.get("name") != "Read":
                        continue
                    file_path = inputs.get("file_path")
                    if not isinstance(file_path, str) or not file_path.lower().endswith(
                        ".png"
                    ):
                        continue
                    read_tool_uses += 1
                    key = normalized_windows_path(file_path)
                    image_key = image_path_lookup.get(key)
                    if image_key is None:
                        unmatched_image_reads += 1
                        continue
                    selected_image_reads += 1
                    events.append(
                        {
                            "session_label": session_label,
                            "root_id": image_key[0],
                            "relative_path": image_key[1],
                            "timestamp": timestamp,
                        }
                    )
        final = (path.stat().st_size, path.stat().st_mtime_ns)
        if initial != final:
            raise RuntimeError(f"session_log_mutated_during_scan:{session_label}")
        summaries.append(
            {
                "session_label": session_label,
                "bytes": initial[0],
                "sha256": digest.hexdigest().upper(),
                "mtime_ns": initial[1],
                "line_count": line_count,
                "candidate_lines": candidate_lines,
                "malformed_candidate_lines": malformed_lines,
                "read_tool_uses_for_png": read_tool_uses,
                "selected_image_reads": selected_image_reads,
                "unmatched_image_reads_outside_selection": unmatched_image_reads,
                "included": False,
            }
        )
    return events, summaries, tool_source_sha256s


def read_provenance_overrides(path: Path | None) -> list[dict[str, str]]:
    if path is None:
        return []
    if not path.is_file():
        raise FileNotFoundError(path)
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    required = {
        "root_id",
        "relative_path",
        "parent_pdf_index_0based",
        "bbox_fx0",
        "bbox_fy0",
        "bbox_fx1",
        "bbox_fy1",
        "render_parameter",
        "generator_timestamp_utc",
        "generator_tool",
        "generator_label",
        "generator_definition_sha256",
        "generator_execution_sha256",
        "description",
    }
    missing = required - set(rows[0] if rows else [])
    if missing:
        raise ValueError(f"Missing override fields: {sorted(missing)}")
    return rows


def main() -> None:
    args = parse_args()
    roots = root_specs(args)
    parent = args.parent_pdf.resolve()
    if not parent.is_file():
        raise FileNotFoundError(parent)
    parent_sha = sha256(parent)
    parent_bytes = parent.stat().st_size
    parent_page_geometry: dict[int, dict[str, object]] = {}
    with fitz.open(parent) as document:
        parent_pages = document.page_count
        for page_index in range(document.page_count):
            page = document[page_index]
            images = page.get_images(full=True)
            largest = max(images, key=lambda item: item[2] * item[3]) if images else None
            width_px = largest[2] if largest else None
            height_px = largest[3] if largest else None
            width_inches = page.rect.width / 72
            height_inches = page.rect.height / 72
            parent_page_geometry[page_index] = {
                "rotation_deg": page.rotation,
                "scan_width_px": width_px,
                "scan_height_px": height_px,
                "effective_dpi_x": (
                    round(width_px / width_inches, 3) if width_px else None
                ),
                "effective_dpi_y": (
                    round(height_px / height_inches, 3) if height_px else None
                ),
            }
    if parent_pages != 540:
        raise ValueError(f"Unexpected parent page count: {parent_pages}")

    project_root = args.project_root.resolve() if args.project_root else None
    linked_tex_hashes: dict[str, str] = {}
    if project_root:
        if not project_root.is_dir():
            raise FileNotFoundError(project_root)
        for tex_name in (
            "expose_I_body.tex",
            "expose_II_body.tex",
            "expose_VI_body.tex",
            "expose_VII_body.tex",
            "expose_VIII_body.tex",
            "expose_IX_body.tex",
        ):
            tex_path = project_root / tex_name
            if tex_path.is_file():
                linked_tex_hashes[tex_name] = sha256(tex_path)

    session_logs = parse_key_values(args.session_log)
    provenance_override_path = (
        args.provenance_override.resolve() if args.provenance_override else None
    )
    provenance_overrides = read_provenance_overrides(provenance_override_path)

    scripts: list[ScriptInfo] = []
    for root in roots:
        scripts.extend(
            script_info(root, path, parent.name)
            for path in root.path.rglob("*.py")
            if selected(path, root.cutoff)
        )
    scripts.sort(
        key=lambda item: (
            item.root_id,
            item.path.name.casefold(),
            item.sha256,
        )
    )

    reviewed = review_pages(args.review_log)
    instances: list[dict[str, object]] = []
    source_paths: dict[tuple[str, str], Path] = {}
    initial_identity: dict[Path, tuple[int, int]] = {}
    for root in roots:
        for path in root.path.rglob("*.png"):
            if not selected(path, root.cutoff):
                continue
            stat = path.stat()
            initial_identity[path] = (stat.st_size, stat.st_mtime_ns)
            with Image.open(path) as image:
                width, height = image.size
                mode = image.mode
                image_format = image.format
            digest = sha256(path)
            relative = path.relative_to(root.path).as_posix()
            source_paths[(root.root_id, relative)] = path
            generator, match_method = match_generator(
                path.name,
                stat.st_mtime,
                scripts,
                root.root_id,
            )
            page_index, page_method = infer_filename_page(path.name)
            job = match_job(path.name, generator) if generator else None
            if page_index is None and job and job.page_index is not None:
                page_index = job.page_index
                page_method = "generator_job"
            if (
                page_index is None
                and generator
                and len(generator.page_candidates) == 1
            ):
                page_index = next(iter(generator.page_candidates))
                page_method = "single_generator_page"
            kind = generator.generator_kind if generator else "unknown"
            if kind == "other":
                lowered = path.name.lower()
                if re.search(
                    r"crop|zoom|clip|tight|glyph|diag|symbol|label|arrow|"
                    r"prime|dot|comma|eq",
                    lowered,
                ):
                    kind = "targeted_crop"
                elif re.search(
                    r"(^|_)(render|page|raw|full|top|bot|band)", lowered
                ):
                    kind = "routine_render"
            bbox = job.bbox if job else None
            render_parameter = job.render_parameter if job else None
            if render_parameter is None and generator and len(
                generator.render_candidates
            ) == 1:
                render_parameter = next(iter(generator.render_candidates))
            folio = (
                page_index - FOLIO_OFFSET
                if page_index is not None and page_index >= 12
                else None
            )
            expose, linked_tex = scope_for_page(page_index)
            geometry = (
                parent_page_geometry[page_index]
                if page_index is not None and page_index in parent_page_geometry
                else {}
            )
            instances.append(
                {
                    "root_id": root.root_id,
                    "root_priority": root.priority,
                    "relative_path": relative,
                    "bytes": stat.st_size,
                    "sha256": digest,
                    "width_px": width,
                    "height_px": height,
                    "color_mode": mode,
                    "image_format": image_format,
                    "pixel_scope": pixel_scope(path.name),
                    "modified_local": datetime.fromtimestamp(
                        stat.st_mtime
                    ).isoformat(timespec="seconds"),
                    "_modified_epoch": stat.st_mtime,
                    "parent_pdf_sha256": parent_sha,
                    "parent_pdf_index_0based": page_index,
                    "parent_pdf_physical_page_1based": (
                        page_index + 1 if page_index is not None else None
                    ),
                    "book_folio": folio,
                    "page_resolution_method": page_method,
                    "page_resolution_confidence": page_confidence(page_method),
                    "expose": expose,
                    "linked_tex_file": linked_tex,
                    "linked_tex_sha256": linked_tex_hashes.get(linked_tex, ""),
                    "parent_page_rotation_deg": geometry.get("rotation_deg", ""),
                    "parent_scan_width_px": geometry.get("scan_width_px", ""),
                    "parent_scan_height_px": geometry.get("scan_height_px", ""),
                    "parent_scan_effective_dpi_x": geometry.get(
                        "effective_dpi_x", ""
                    ),
                    "parent_scan_effective_dpi_y": geometry.get(
                        "effective_dpi_y", ""
                    ),
                    "generator_root_id": generator.root_id if generator else "",
                    "generator_script": generator.path.name if generator else "",
                    "generator_script_sha256": generator.sha256 if generator else "",
                    "generator_match_method": match_method,
                    "generator_source_class": (
                        generator.source_class if generator else "unresolved"
                    ),
                    "evidence_class": kind,
                    "bbox_fx0": bbox[0] if bbox else "",
                    "bbox_fy0": bbox[1] if bbox else "",
                    "bbox_fx1": bbox[2] if bbox else "",
                    "bbox_fy1": bbox[3] if bbox else "",
                    "render_parameter": render_parameter or "",
                    "manual_review_link": (
                        "review_log_page_link"
                        if page_index in reviewed
                        else "no_individual_review_link_recovered"
                    ),
                }
            )

    image_path_lookup = {
        normalized_windows_path(str(source_paths[(str(row["root_id"]), str(row["relative_path"]))])): (
            str(row["root_id"]),
            str(row["relative_path"]),
        )
        for row in instances
    }
    raw_read_events, session_summaries, tool_source_sha256s = scan_read_events(
        session_logs,
        image_path_lookup,
    )
    instance_by_key = {
        (str(row["root_id"]), str(row["relative_path"])): row
        for row in instances
    }
    read_event_groups: dict[
        tuple[str, str, str], list[dict[str, str]]
    ] = defaultdict(list)
    stale_pre_generation_read_events = 0
    for event in raw_read_events:
        instance = instance_by_key[(event["root_id"], event["relative_path"])]
        try:
            read_epoch = datetime.fromisoformat(
                event["timestamp"].replace("Z", "+00:00")
            ).timestamp()
        except ValueError:
            stale_pre_generation_read_events += 1
            continue
        if read_epoch + 10 < float(instance["_modified_epoch"]):
            stale_pre_generation_read_events += 1
            continue
        read_event_groups[
            (event["root_id"], event["relative_path"], event["timestamp"])
        ].append(event)
    read_events: list[dict[str, str]] = []
    for (root_id, relative_path, timestamp), group in sorted(
        read_event_groups.items()
    ):
        read_events.append(
            {
                "source_session_labels": ";".join(
                    sorted({event["session_label"] for event in group})
                ),
                "root_id": root_id,
                "relative_path": relative_path,
                "timestamp": timestamp,
            }
        )
    duplicate_branched_read_events_collapsed = (
        len(raw_read_events)
        - stale_pre_generation_read_events
        - len(read_events)
    )
    read_events_by_image: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for event in read_events:
        read_events_by_image[(event["root_id"], event["relative_path"])].append(event)
    for instance in instances:
        events = read_events_by_image.get(
            (str(instance["root_id"]), str(instance["relative_path"])),
            [],
        )
        instance["_read_events"] = events
        instance["read_count"] = len(events)
        instance["first_read_timestamp"] = (
            min(event["timestamp"] for event in events) if events else ""
        )
        instance["last_read_timestamp"] = (
            max(event["timestamp"] for event in events) if events else ""
        )
        instance["read_session_labels"] = ";".join(
            sorted(
                {
                    label
                    for event in events
                    for label in event["source_session_labels"].split(";")
                    if label
                }
            )
        )

    override_errors: list[str] = []
    seen_override_keys: set[tuple[str, str]] = set()
    for override in provenance_overrides:
        key = (override["root_id"], override["relative_path"])
        if key in seen_override_keys:
            override_errors.append(f"duplicate_provenance_override:{key}")
            continue
        seen_override_keys.add(key)
        instance = instance_by_key.get(key)
        if instance is None:
            override_errors.append(f"provenance_override_missing_image:{key}")
            continue
        definition_sha = override["generator_definition_sha256"].upper()
        execution_sha = override["generator_execution_sha256"].upper()
        if definition_sha not in tool_source_sha256s:
            override_errors.append(
                f"provenance_definition_not_in_session:{key}:{definition_sha}"
            )
        if execution_sha not in tool_source_sha256s:
            override_errors.append(
                f"provenance_execution_not_in_session:{key}:{execution_sha}"
            )
        page_index = int(override["parent_pdf_index_0based"])
        if not 0 <= page_index < parent_pages:
            override_errors.append(f"provenance_page_out_of_range:{key}:{page_index}")
            continue
        bbox = tuple(
            float(override[field])
            for field in ("bbox_fx0", "bbox_fy0", "bbox_fx1", "bbox_fy1")
        )
        if not (
            0 <= bbox[0] < bbox[2] <= 1
            and 0 <= bbox[1] < bbox[3] <= 1
        ):
            override_errors.append(f"provenance_bbox_invalid:{key}:{bbox}")
            continue
        expose, linked_tex = scope_for_page(page_index)
        geometry = parent_page_geometry[page_index]
        instance.update(
            {
                "parent_pdf_index_0based": page_index,
                "parent_pdf_physical_page_1based": page_index + 1,
                "book_folio": page_index - FOLIO_OFFSET if page_index >= 12 else None,
                "page_resolution_method": "exact_session_generator_command",
                "page_resolution_confidence": "high",
                "expose": expose,
                "linked_tex_file": linked_tex,
                "linked_tex_sha256": linked_tex_hashes.get(linked_tex, ""),
                "parent_page_rotation_deg": geometry.get("rotation_deg", ""),
                "parent_scan_width_px": geometry.get("scan_width_px", ""),
                "parent_scan_height_px": geometry.get("scan_height_px", ""),
                "parent_scan_effective_dpi_x": geometry.get(
                    "effective_dpi_x", ""
                ),
                "parent_scan_effective_dpi_y": geometry.get(
                    "effective_dpi_y", ""
                ),
                "generator_root_id": "session_log_exact",
                "generator_script": override["generator_label"],
                "generator_script_sha256": definition_sha,
                "generator_match_method": "exact_session_generator_command",
                "generator_source_class": "controlling_540_page_scan",
                "evidence_class": "targeted_crop",
                "bbox_fx0": bbox[0],
                "bbox_fy0": bbox[1],
                "bbox_fx1": bbox[2],
                "bbox_fy1": bbox[3],
                "render_parameter": int(override["render_parameter"]),
                "provenance_description": override["description"],
                "generator_timestamp_utc": override["generator_timestamp_utc"],
                "generator_tool": override["generator_tool"],
                "generator_execution_sha256": execution_sha,
            }
        )

    by_hash: dict[str, list[dict[str, object]]] = defaultdict(list)
    for instance in instances:
        by_hash[str(instance["sha256"])].append(instance)

    canonical: list[dict[str, object]] = []
    aliases: list[dict[str, object]] = []
    public_read_events: list[dict[str, object]] = []
    for digest in sorted(by_hash):
        group = by_hash[digest]
        group.sort(
            key=lambda row: (
                int(row["root_priority"]),
                row["evidence_class"] != "targeted_crop",
                str(row["relative_path"]).casefold(),
            )
        )
        current = dict(group[0])
        group_read_events = [
            event
            for row in group
            for event in row.get("_read_events", [])
        ]
        current["read_count"] = len(group_read_events)
        current["first_read_timestamp"] = (
            min(event["timestamp"] for event in group_read_events)
            if group_read_events
            else ""
        )
        current["last_read_timestamp"] = (
            max(event["timestamp"] for event in group_read_events)
            if group_read_events
            else ""
        )
        current["read_session_labels"] = ";".join(
            sorted(
                {
                    label
                    for event in group_read_events
                    for label in event["source_session_labels"].split(";")
                    if label
                }
            )
        )
        current["visual_id"] = f"SGA7I-VIS-{len(canonical) + 1:05d}"
        current["duplicate_instance_count"] = len(group)
        public_candidate = (
            current["evidence_class"] == "targeted_crop"
            and current["generator_source_class"]
            == "controlling_540_page_scan"
            and current["parent_pdf_index_0based"] is not None
            and current["read_count"] > 0
            and current["pixel_scope"] == "targeted_region_or_detail"
        )
        current["publication_disposition"] = (
            "candidate_targeted_excerpt_pending_rights_review"
            if public_candidate
            else "rights_blocked_not_public"
        )
        if current["read_count"] and current["manual_review_link"] == "review_log_page_link":
            current["qa_disposition"] = "opened_in_session_and_page_named_in_review_log"
        elif current["read_count"]:
            current["qa_disposition"] = "opened_in_source_audit_session"
        else:
            current["qa_disposition"] = (
                "generated_working_evidence_not_individually_claimed_reviewed"
            )
        canonical.append(current)
        for event in sorted(
            group_read_events,
            key=lambda row: (
                row["timestamp"],
                row["source_session_labels"],
                row["root_id"],
                row["relative_path"].casefold(),
            ),
        ):
            public_read_events.append(
                {
                    "visual_id": current["visual_id"],
                    "source_session_labels": event["source_session_labels"],
                    "root_id": event["root_id"],
                    "relative_path": event["relative_path"],
                    "timestamp": event["timestamp"],
                }
            )
        for alias in group[1:]:
            aliases.append(
                {
                    "visual_id": current["visual_id"],
                    "sha256": digest,
                    "canonical_root_id": current["root_id"],
                    "canonical_relative_path": current["relative_path"],
                    "alias_root_id": alias["root_id"],
                    "alias_relative_path": alias["relative_path"],
                    "bytes": alias["bytes"],
                }
            )

    fields = [
        "visual_id",
        "root_id",
        "relative_path",
        "bytes",
        "sha256",
        "width_px",
        "height_px",
        "color_mode",
        "image_format",
        "pixel_scope",
        "modified_local",
        "parent_pdf_sha256",
        "parent_pdf_index_0based",
        "parent_pdf_physical_page_1based",
        "book_folio",
        "page_resolution_method",
        "page_resolution_confidence",
        "expose",
        "linked_tex_file",
        "linked_tex_sha256",
        "parent_page_rotation_deg",
        "parent_scan_width_px",
        "parent_scan_height_px",
        "parent_scan_effective_dpi_x",
        "parent_scan_effective_dpi_y",
        "generator_root_id",
        "generator_script",
        "generator_script_sha256",
        "generator_match_method",
        "generator_source_class",
        "generator_timestamp_utc",
        "generator_tool",
        "generator_execution_sha256",
        "evidence_class",
        "bbox_fx0",
        "bbox_fy0",
        "bbox_fx1",
        "bbox_fy1",
        "render_parameter",
        "provenance_description",
        "manual_review_link",
        "qa_disposition",
        "read_count",
        "first_read_timestamp",
        "last_read_timestamp",
        "read_session_labels",
        "duplicate_instance_count",
        "publication_disposition",
    ]
    for row in canonical:
        row.pop("root_priority", None)
        row.pop("_read_events", None)
        row.pop("_modified_epoch", None)

    public_crop_rows = [
        {
            "archive_member_path": archive_member_path(
                str(row["visual_id"]), str(row["relative_path"])
            ),
            **row,
        }
        for row in canonical
        if row["publication_disposition"]
        == "candidate_targeted_excerpt_pending_rights_review"
    ]

    output = args.output_dir.resolve()
    output.mkdir(parents=True, exist_ok=True)
    index_path = output / "SGA7I_VISUAL_EVIDENCE_INDEX.csv"
    aliases_path = output / "SGA7I_VISUAL_EVIDENCE_DUPLICATE_ALIASES.csv"
    scripts_path = output / "SGA7I_GENERATOR_SCRIPT_IDENTITY.csv"
    read_events_path = output / "SGA7I_IMAGE_READ_EVENTS.csv"
    public_crops_path = output / "SGA7I_PUBLIC_TARGETED_CROP_MANIFEST.csv"
    csv_write(index_path, canonical, fields)
    csv_write(
        aliases_path,
        aliases,
        [
            "visual_id",
            "sha256",
            "canonical_root_id",
            "canonical_relative_path",
            "alias_root_id",
            "alias_relative_path",
            "bytes",
        ],
    )
    csv_write(
        read_events_path,
        public_read_events,
        [
            "visual_id",
            "source_session_labels",
            "root_id",
            "relative_path",
            "timestamp",
        ],
    )
    csv_write(
        public_crops_path,
        public_crop_rows,
        ["archive_member_path", *fields],
    )
    script_rows = [
        {
            "root_id": script.root_id,
            "script_basename": script.path.name,
            "bytes": script.path.stat().st_size,
            "sha256": script.sha256,
            "modified_local": datetime.fromtimestamp(
                script.modified
            ).isoformat(timespec="seconds"),
            "source_class": script.source_class,
            "generator_kind": script.generator_kind,
            "page_candidates": ";".join(
                str(value) for value in sorted(script.page_candidates)
            ),
            "render_candidates": ";".join(
                str(value) for value in sorted(script.render_candidates)
            ),
        }
        for script in sorted(
            scripts,
            key=lambda item: (item.root_id, item.path.name.casefold()),
        )
    ]
    csv_write(
        scripts_path,
        script_rows,
        [
            "root_id",
            "script_basename",
            "bytes",
            "sha256",
            "modified_local",
            "source_class",
            "generator_kind",
            "page_candidates",
            "render_candidates",
        ],
    )

    csv_errors = [
        error
        for path in (
            index_path,
            aliases_path,
            scripts_path,
            read_events_path,
            public_crops_path,
        )
        for error in csv_gate(path)
    ]

    after = {
        path: (path.stat().st_size, path.stat().st_mtime_ns)
        for path in initial_identity
    }
    mutated = [str(path) for path in initial_identity if initial_identity[path] != after[path]]
    output_text = "\n".join(
        path.read_text(encoding="utf-8", errors="replace").lower()
        for path in (
            index_path,
            aliases_path,
            scripts_path,
            read_events_path,
            public_crops_path,
        )
    )
    privacy_hits = [marker for marker in PRIVATE_MARKERS if marker in output_text]
    superseded_source_pixels = sum(
        row["generator_source_class"] == "superseded_low_resolution_scan"
        for row in canonical
    )
    errors = [
        *(f"source_mutated:{value}" for value in mutated),
        *(f"privacy_marker:{value}" for value in privacy_hits),
        *csv_errors,
        *override_errors,
    ]
    if superseded_source_pixels:
        errors.append(
            f"superseded_low_resolution_scan_pixels:{superseded_source_pixels}"
        )
    summary = {
        "status": "PASS_METADATA_CUSTODY_READY"
        if not errors
        else "FAIL",
        "errors": errors,
        "parent_pdf": {
            "basename": parent.name,
            "bytes": parent_bytes,
            "sha256": parent_sha,
            "pages": parent_pages,
            "included": False,
        },
        "selection": [
            {
                "root_id": root.root_id,
                "cutoff_local": (
                    datetime.fromtimestamp(root.cutoff).isoformat(timespec="seconds")
                    if root.cutoff is not None
                    else None
                ),
            }
            for root in roots
        ],
        "linked_tex": {
            name: {"sha256": digest, "included": False}
            for name, digest in sorted(linked_tex_hashes.items())
        },
        "session_logs": session_summaries,
        "provenance_overrides": {
            "rows": len(provenance_overrides),
            "errors": override_errors,
            "file": (
                {
                    "basename": provenance_override_path.name,
                    "bytes": provenance_override_path.stat().st_size,
                    "sha256": sha256(provenance_override_path),
                }
                if provenance_override_path
                else None
            ),
        },
        "image_instances": len(instances),
        "image_instance_bytes": sum(int(row["bytes"]) for row in instances),
        "unique_images": len(canonical),
        "unique_image_bytes": sum(int(row["bytes"]) for row in canonical),
        "duplicate_aliases": len(aliases),
        "duplicate_bytes_avoidable": sum(
            sum(int(row["bytes"]) for row in group[1:])
            for group in by_hash.values()
        ),
        "page_resolved": sum(
            row["parent_pdf_index_0based"] != ""
            and row["parent_pdf_index_0based"] is not None
            for row in canonical
        ),
        "generator_resolved": sum(bool(row["generator_script"]) for row in canonical),
        "generator_source_classes": Counter(
            str(row["generator_source_class"]) for row in canonical
        ),
        "superseded_low_resolution_scan_pixels": superseded_source_pixels,
        "evidence_classes": Counter(
            str(row["evidence_class"]) for row in canonical
        ),
        "publication_dispositions": Counter(
            str(row["publication_disposition"]) for row in canonical
        ),
        "manual_review_linked": sum(
            row["manual_review_link"] == "review_log_page_link"
            for row in canonical
        ),
        "read_events": len(public_read_events),
        "stale_pre_generation_read_events_excluded": (
            stale_pre_generation_read_events
        ),
        "duplicate_branched_read_events_collapsed": (
            duplicate_branched_read_events_collapsed
        ),
        "unique_images_opened": sum(bool(row["read_count"]) for row in canonical),
        "opened_targeted_crop_candidates": sum(
            row["publication_disposition"]
            == "candidate_targeted_excerpt_pending_rights_review"
            for row in canonical
        ),
        "opened_targeted_crop_candidate_bytes": sum(
            int(row["bytes"])
            for row in canonical
            if row["publication_disposition"]
            == "candidate_targeted_excerpt_pending_rights_review"
        ),
        "opened_full_page_pixels_withheld": sum(
            bool(row["read_count"])
            and row["pixel_scope"] == "routine_full_page_or_near_full_page"
            for row in canonical
        ),
        "generator_scripts": len(script_rows),
        "csv_gate": {
            "files": 5,
            "errors": csv_errors,
        },
        "metadata_files": {
            path.name: {"bytes": path.stat().st_size, "sha256": sha256(path)}
            for path in (
                index_path,
                aliases_path,
                scripts_path,
                read_events_path,
                public_crops_path,
            )
        },
    }
    json_write(output / "SGA7I_VISUAL_EVIDENCE_VALIDATION.json", summary)
    if summary["status"] != "PASS_METADATA_CUSTODY_READY":
        raise RuntimeError(summary["errors"])
    print(json.dumps(summary, ensure_ascii=True, indent=2))


if __name__ == "__main__":
    main()
