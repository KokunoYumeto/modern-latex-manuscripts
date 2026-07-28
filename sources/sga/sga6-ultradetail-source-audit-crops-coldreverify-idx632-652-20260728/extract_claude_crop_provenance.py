#!/usr/bin/env python3
"""Extract SGA6 crop provenance from a Claude session log.

The source session can be several gigabytes. This tool streams it once and
retains only crop-generation Bash calls and image Read calls for the requested
index range. Its output is an internal build input, not a public artifact.
"""

from __future__ import annotations

import argparse
import ast
import base64
import hashlib
import io
import json
import os
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from PIL import Image, ImageChops, ImageStat


TIGHT_RE = re.compile(r"^(?:zoom|z)(\d{3})(?:[^\\/]*)\.png$", re.IGNORECASE)
ROUTINE_RE = re.compile(
    r"^cve(?:0p)?(\d{3})_(top|a|b|c|d)\.png$",
    re.IGNORECASE,
)
INDEX_IN_COMMAND_RE = re.compile(
    r"(?:(?:zoom|z)|cve(?:0p)?)(\d{3})",
    re.IGNORECASE,
)
HEREDOC_RE = re.compile(
    r"<<\s*['\"]?(?P<delimiter>[A-Za-z0-9_]+)['\"]?\r?\n"
    r"(?P<body>.*?)\r?\n(?P=delimiter)(?:\r?\n|$)",
    re.DOTALL,
)
Image.MAX_IMAGE_PIXELS = None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--session-log", type=Path, required=True)
    parser.add_argument("--scratch-dir", type=Path, required=True)
    parser.add_argument("--start-index", type=int, required=True)
    parser.add_argument("--end-index", type=int, required=True)
    parser.add_argument(
        "--min-mtime-utc",
        default="",
        help="Optional inclusive ISO-8601 UTC lower bound for selected PNGs.",
    )
    parser.add_argument(
        "--generator-script-dir",
        type=Path,
        help=(
            "Optional directory containing retained cve0p*.py page-band and "
            "zoom*.py tight-crop scripts. These supplement generators whose "
            "final edited bodies are absent from the session log."
        ),
    )
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def utc_mtime(path: Path) -> str:
    return datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).isoformat()


def basename(value: str) -> str:
    return value.replace("\\", "/").rsplit("/", 1)[-1]


def tool_uses(value: Any) -> list[dict[str, Any]]:
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


def read_attachment_results(value: Any) -> list[dict[str, Any]]:
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
        if isinstance(item, dict) and item.get("type") == "tool_result"
    ]


def simple_eval(node: ast.AST, values: dict[str, Any]) -> Any:
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.Name):
        if node.id in values:
            return values[node.id]
        raise KeyError(node.id)
    if isinstance(node, (ast.Tuple, ast.List)):
        return tuple(simple_eval(item, values) for item in node.elts)
    if isinstance(node, ast.UnaryOp):
        value = simple_eval(node.operand, values)
        if isinstance(node.op, ast.USub):
            return -value
        if isinstance(node.op, ast.UAdd):
            return +value
    if isinstance(node, ast.BinOp):
        left = simple_eval(node.left, values)
        right = simple_eval(node.right, values)
        if isinstance(node.op, ast.Add):
            return left + right
        if isinstance(node.op, ast.Sub):
            return left - right
        if isinstance(node.op, ast.Mult):
            return left * right
        if isinstance(node.op, ast.Div):
            return left / right
        if isinstance(node.op, ast.Mod):
            return left % right
    if isinstance(node, ast.JoinedStr):
        parts: list[str] = []
        for item in node.values:
            if isinstance(item, ast.FormattedValue):
                parts.append(str(simple_eval(item.value, values)))
            else:
                parts.append(str(item.value))
        return "".join(parts)
    if (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id in {"int", "float", "str"}
        and node.args
    ):
        converter = {"int": int, "float": float, "str": str}[node.func.id]
        return converter(simple_eval(node.args[0], values))
    raise ValueError(ast.dump(node)[:240])


def python_source(record: dict[str, Any]) -> tuple[str, str] | None:
    source_text = str(record.get("source_text") or "")
    source_path = str(record.get("source_path") or "")
    if record.get("tool_name") in {"Write", "retained_local_generator_script"}:
        return source_text, basename(source_path)
    if record.get("tool_name") != "Bash":
        return None
    match = HEREDOC_RE.search(source_text)
    if not match:
        return None
    script_match = re.search(
        r"cat\s*>\s*['\"]?(?P<path>[^'\"\s]+)",
        source_text,
        re.IGNORECASE,
    )
    script_name = basename(script_match.group("path")) if script_match else ""
    return match.group("body"), script_name


def numeric_from_expression(
    source: str,
    pattern: str,
    values: dict[str, Any],
    fallback: float | int | None,
) -> float | int | None:
    match = re.search(pattern, source)
    if not match:
        return fallback
    try:
        expression = ast.parse(match.group("value"), mode="eval").body
        return simple_eval(expression, values)
    except (SyntaxError, KeyError, TypeError, ValueError):
        return fallback


def dimension_fraction(
    node: ast.AST,
    dimension_name: str,
    values: dict[str, Any],
) -> float:
    """Evaluate a normalized coordinate such as 0.03*W or fy0*H."""
    if isinstance(node, ast.Name) and node.id in values:
        return float(values[node.id])
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mult):
        if isinstance(node.left, ast.Name) and node.left.id == dimension_name:
            return float(simple_eval(node.right, values))
        if isinstance(node.right, ast.Name) and node.right.id == dimension_name:
            return float(simple_eval(node.left, values))
    raise ValueError(ast.dump(node)[:240])


def loop_generator_specs(
    tree: ast.Module,
    source: str,
    script_name: str,
    record: dict[str, Any],
    globals_: dict[str, Any],
    page_index: int | None,
) -> list[dict[str, Any]]:
    """Parse retained page-band generators that emit crops from a bands loop."""
    results: list[dict[str, Any]] = []
    for node in tree.body:
        if not (
            isinstance(node, ast.For)
            and isinstance(node.target, (ast.Tuple, ast.List))
            and all(isinstance(item, ast.Name) for item in node.target.elts)
        ):
            continue
        try:
            rows = simple_eval(node.iter, globals_)
        except (KeyError, TypeError, ValueError):
            continue
        target_names = [item.id for item in node.target.elts]

        rect_call: ast.Call | None = None
        save_call: ast.Call | None = None
        matrix_call: ast.Call | None = None
        for child in ast.walk(node):
            if isinstance(child, ast.Call):
                if (
                    isinstance(child.func, ast.Attribute)
                    and child.func.attr == "Rect"
                    and len(child.args) == 4
                ):
                    rect_call = child
                if (
                    isinstance(child.func, ast.Attribute)
                    and child.func.attr == "save"
                    and child.args
                ):
                    save_call = child
                if (
                    isinstance(child.func, ast.Attribute)
                    and child.func.attr == "Matrix"
                    and child.args
                ):
                    matrix_call = child
        if rect_call is None or save_call is None:
            continue

        for row in rows:
            if not isinstance(row, (tuple, list)) or len(row) != len(target_names):
                continue
            values = dict(globals_)
            values.update(dict(zip(target_names, row)))
            local_values = dict(values)
            for statement in node.body:
                if (
                    isinstance(statement, ast.Assign)
                    and len(statement.targets) == 1
                    and isinstance(statement.targets[0], ast.Name)
                ):
                    try:
                        local_values[statement.targets[0].id] = simple_eval(
                            statement.value,
                            local_values,
                        )
                    except (KeyError, TypeError, ValueError):
                        pass

            try:
                bbox = (
                    dimension_fraction(rect_call.args[0], "W", local_values),
                    dimension_fraction(rect_call.args[1], "H", local_values),
                    dimension_fraction(rect_call.args[2], "W", local_values),
                    dimension_fraction(rect_call.args[3], "H", local_values),
                )
                output_path = str(simple_eval(save_call.args[0], local_values))
            except (KeyError, TypeError, ValueError):
                continue

            dpi_value = local_values.get("dpi") or local_values.get("DPI")
            if dpi_value is None and matrix_call is not None:
                try:
                    dpi_value = 72.0 * float(
                        simple_eval(matrix_call.args[0], local_values)
                    )
                except (KeyError, TypeError, ValueError):
                    pass
            if dpi_value is None and local_values.get("zoom") is not None:
                dpi_value = float(local_values["zoom"]) * 72.0
            if dpi_value is None or page_index is None:
                continue

            cutoff = numeric_from_expression(
                source,
                r"autocontrast\(\s*img?\s*,\s*cutoff\s*=\s*(?P<value>[^,)]+)",
                local_values,
                0,
            )
            contrast = numeric_from_expression(
                source,
                r"Contrast\(\s*img?\s*\)\.enhance\(\s*(?P<value>[^)]+)",
                local_values,
                1.0,
            )
            sharpness = numeric_from_expression(
                source,
                r"Sharpness\(\s*img?\s*\)\.enhance\(\s*(?P<value>[^)]+)",
                local_values,
                1.0,
            )
            results.append(
                {
                    "basename": basename(output_path),
                    "parent_pdf_index_0based": page_index,
                    "bbox_fx0": bbox[0],
                    "bbox_fy0": bbox[1],
                    "bbox_fx1": bbox[2],
                    "bbox_fy1": bbox[3],
                    "render_dpi": int(round(float(dpi_value))),
                    "autocontrast_cutoff": cutoff,
                    "contrast": contrast,
                    "sharpness": sharpness,
                    "description": "",
                    "generator_script_basename": script_name,
                    "generator_source_sha256": record["source_sha256"],
                    "generator_timestamp": record["timestamp"],
                    "generator_tool_name": record["tool_name"],
                }
            )
    return results


def direct_generator_specs(
    tree: ast.Module,
    source: str,
    script_name: str,
    record: dict[str, Any],
    globals_: dict[str, Any],
    page_index: int | None,
) -> list[dict[str, Any]]:
    """Parse top-level one-off crop scripts without a helper function."""
    if page_index is None:
        return []

    values = dict(globals_)
    clips: dict[str, tuple[float, float, float, float]] = {}
    pixmaps: dict[str, tuple[str, int]] = {}
    image_pixmaps: dict[str, str] = {}
    clip_lines: dict[str, int] = {}
    lines = source.splitlines()
    results: list[dict[str, Any]] = []

    def referenced_name(node: ast.AST, candidates: set[str]) -> str | None:
        for child in ast.walk(node):
            if isinstance(child, ast.Name) and child.id in candidates:
                return child.id
        return None

    def comments_before(line_number: int) -> str:
        comments: list[str] = []
        cursor = line_number - 2
        while cursor >= 0 and (
            not lines[cursor].strip() or lines[cursor].lstrip().startswith("#")
        ):
            if lines[cursor].lstrip().startswith("#"):
                comments.append(lines[cursor].lstrip()[1:].strip())
            cursor -= 1
        return " ".join(reversed(comments))

    for statement in tree.body:
        target_name: str | None = None
        if (
            isinstance(statement, ast.Assign)
            and len(statement.targets) == 1
            and isinstance(statement.targets[0], ast.Name)
        ):
            target_name = statement.targets[0].id
            try:
                values[target_name] = simple_eval(statement.value, values)
            except (KeyError, TypeError, ValueError):
                pass

            value = statement.value
            if (
                isinstance(value, ast.Call)
                and isinstance(value.func, ast.Attribute)
                and value.func.attr == "Rect"
                and len(value.args) == 4
            ):
                try:
                    clips[target_name] = (
                        dimension_fraction(value.args[0], "W", values),
                        dimension_fraction(value.args[1], "H", values),
                        dimension_fraction(value.args[2], "W", values),
                        dimension_fraction(value.args[3], "H", values),
                    )
                    clip_lines[target_name] = statement.lineno
                except (KeyError, TypeError, ValueError):
                    pass

            get_pixmap: ast.Call | None = None
            for child in ast.walk(value):
                if (
                    isinstance(child, ast.Call)
                    and isinstance(child.func, ast.Attribute)
                    and child.func.attr == "get_pixmap"
                ):
                    get_pixmap = child
                    break
            if get_pixmap is not None:
                keywords = {
                    keyword.arg: keyword.value
                    for keyword in get_pixmap.keywords
                    if keyword.arg
                }
                clip_node = keywords.get("clip")
                clip_name = (
                    clip_node.id if isinstance(clip_node, ast.Name) else None
                )
                dpi_value: float | int | None = None
                dpi_node = keywords.get("dpi")
                if dpi_node is not None:
                    try:
                        dpi_value = simple_eval(dpi_node, values)
                    except (KeyError, TypeError, ValueError):
                        pass
                matrix_node = keywords.get("matrix")
                if (
                    dpi_value is None
                    and isinstance(matrix_node, ast.Call)
                    and isinstance(matrix_node.func, ast.Attribute)
                    and matrix_node.func.attr == "Matrix"
                    and matrix_node.args
                ):
                    try:
                        dpi_value = 72.0 * float(
                            simple_eval(matrix_node.args[0], values)
                        )
                    except (KeyError, TypeError, ValueError):
                        pass
                if clip_name in clips and dpi_value is not None:
                    pixmaps[target_name] = (
                        clip_name,
                        int(round(float(dpi_value))),
                    )

            pixmap_name = referenced_name(value, set(pixmaps))
            image_name = referenced_name(value, set(image_pixmaps))
            if pixmap_name is not None:
                image_pixmaps[target_name] = pixmap_name
            elif image_name is not None:
                image_pixmaps[target_name] = image_pixmaps[image_name]

        for child in ast.walk(statement):
            if not (
                isinstance(child, ast.Call)
                and isinstance(child.func, ast.Attribute)
                and child.func.attr == "save"
                and child.args
                and isinstance(child.func.value, ast.Name)
            ):
                continue
            image_name = child.func.value.id
            pixmap_name = image_pixmaps.get(image_name)
            if pixmap_name not in pixmaps:
                continue
            clip_name, render_dpi = pixmaps[pixmap_name]
            try:
                output_path = str(simple_eval(child.args[0], values))
            except (KeyError, TypeError, ValueError):
                continue
            bbox = clips[clip_name]
            cutoff = numeric_from_expression(
                source,
                r"autocontrast\(\s*img\d?\s*,\s*cutoff\s*=\s*(?P<value>[^,)]+)",
                values,
                0,
            )
            contrast = numeric_from_expression(
                source,
                r"Contrast\(\s*img\d?\s*\)\.enhance\(\s*(?P<value>[^)]+)",
                values,
                1.0,
            )
            sharpness = numeric_from_expression(
                source,
                r"Sharpness\(\s*img\d?\s*\)\.enhance\(\s*(?P<value>[^)]+)",
                values,
                1.0,
            )
            results.append(
                {
                    "basename": basename(output_path),
                    "parent_pdf_index_0based": page_index,
                    "bbox_fx0": bbox[0],
                    "bbox_fy0": bbox[1],
                    "bbox_fx1": bbox[2],
                    "bbox_fy1": bbox[3],
                    "render_dpi": render_dpi,
                    "autocontrast_cutoff": cutoff,
                    "contrast": contrast,
                    "sharpness": sharpness,
                    "description": comments_before(clip_lines[clip_name]),
                    "generator_script_basename": script_name,
                    "generator_source_sha256": record["source_sha256"],
                    "generator_timestamp": record["timestamp"],
                    "generator_tool_name": record["tool_name"],
                }
            )
    return results


def generator_specs(record: dict[str, Any]) -> list[dict[str, Any]]:
    extracted = python_source(record)
    if not extracted:
        return []
    source, script_name = extracted
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return []

    # Treat page width and height as one while evaluating crop-spec tables.
    # This preserves normalized fractions for generators that assign the
    # coordinates to loop variables before calling fitz.Rect.
    globals_: dict[str, Any] = {"OUT": "", "W": 1.0, "H": 1.0}
    for node in tree.body:
        if (
            isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
        ):
            try:
                globals_[node.targets[0].id] = simple_eval(node.value, globals_)
            except (KeyError, TypeError, ValueError):
                pass

    page_index: int | None = None
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign) or not isinstance(node.value, ast.Subscript):
            continue
        if not any(
            isinstance(target, ast.Name) and target.id in {"pg", "page"}
            for target in node.targets
        ):
            continue
        try:
            page_index = int(simple_eval(node.value.slice, globals_))
        except (KeyError, TypeError, ValueError):
            continue

    functions = {
        node.name: node for node in tree.body if isinstance(node, ast.FunctionDef)
    }
    lines = source.splitlines()
    results: list[dict[str, Any]] = []
    for node in tree.body:
        if not (
            isinstance(node, ast.Expr)
            and isinstance(node.value, ast.Call)
            and isinstance(node.value.func, ast.Name)
            and node.value.func.id in functions
        ):
            continue
        call = node.value
        function = functions[call.func.id]
        parameters = [argument.arg for argument in function.args.args]
        values = dict(globals_)
        for parameter, argument in zip(parameters, call.args):
            try:
                values[parameter] = simple_eval(argument, globals_)
            except (KeyError, TypeError, ValueError):
                pass
        defaults: list[ast.AST | None] = [None] * (
            len(parameters) - len(function.args.defaults)
        ) + list(function.args.defaults)
        for parameter, default in zip(parameters, defaults):
            if parameter in values or default is None:
                continue
            try:
                values[parameter] = simple_eval(default, globals_)
            except (KeyError, TypeError, ValueError):
                pass
        for keyword in call.keywords:
            if not keyword.arg:
                continue
            try:
                values[keyword.arg] = simple_eval(keyword.value, globals_)
            except (KeyError, TypeError, ValueError):
                pass

        local_values = dict(values)
        output_path: str | None = None
        for statement in function.body:
            if (
                isinstance(statement, ast.Assign)
                and len(statement.targets) == 1
                and isinstance(statement.targets[0], ast.Name)
            ):
                try:
                    local_values[statement.targets[0].id] = simple_eval(
                        statement.value,
                        local_values,
                    )
                except (KeyError, TypeError, ValueError):
                    pass
            for child in ast.walk(statement):
                if not (
                    isinstance(child, ast.Call)
                    and isinstance(child.func, ast.Attribute)
                    and child.func.attr == "save"
                    and child.args
                ):
                    continue
                try:
                    output_path = str(simple_eval(child.args[0], local_values))
                except (KeyError, TypeError, ValueError):
                    pass

        bbox: tuple[float, float, float, float] | None = None
        render_dpi: int | None = None
        if all(key in values for key in ("fx0", "fx1", "fy0", "fy1")):
            bbox = (
                float(values["fx0"]),
                float(values["fy0"]),
                float(values["fx1"]),
                float(values["fy1"]),
            )
            render_dpi = int(values["dpi"])
        elif all(key in values for key in ("x0f", "y0f", "x1f", "y1f")):
            bbox = (
                float(values["x0f"]),
                float(values["y0f"]),
                float(values["x1f"]),
                float(values["y1f"]),
            )
            render_dpi = int(values["dpi"])
        elif "fr" in values:
            fractions = tuple(float(value) for value in values["fr"][:4])
            bbox = (fractions[0], fractions[1], fractions[2], fractions[3])
            dpi_value = values.get("dpi") or globals_.get("dpi") or globals_.get("DPI")
            render_dpi = int(dpi_value) if dpi_value is not None else None
        if function.name == "shot":
            page_value = values.get("pgno", values.get("pgidx"))
            if page_value is not None:
                page_index = int(page_value)

        comment_lines: list[str] = []
        cursor = node.lineno - 2
        while cursor >= 0 and (
            not lines[cursor].strip() or lines[cursor].lstrip().startswith("#")
        ):
            if lines[cursor].lstrip().startswith("#"):
                comment_lines.append(lines[cursor].lstrip()[1:].strip())
            cursor -= 1

        cutoff = values.get("cutoff")
        if cutoff is None:
            cutoff = numeric_from_expression(
                source,
                r"autocontrast\(\s*img?\s*,\s*cutoff\s*=\s*(?P<value>[^,)]+)",
                values,
                0,
            )
        contrast = values.get("contrast", values.get("cont"))
        if contrast is None:
            contrast = numeric_from_expression(
                source,
                r"Contrast\(\s*img?\s*\)\.enhance\(\s*(?P<value>[^)]+)",
                values,
                1.0,
            )
        sharpness = values.get("sharpness", values.get("sharp"))
        if sharpness is None:
            sharpness = numeric_from_expression(
                source,
                r"Sharpness\(\s*img?\s*\)\.enhance\(\s*(?P<value>[^)]+)",
                values,
                1.0,
            )

        if not output_path or page_index is None or bbox is None or render_dpi is None:
            continue
        results.append(
            {
                "basename": basename(output_path),
                "parent_pdf_index_0based": page_index,
                "bbox_fx0": bbox[0],
                "bbox_fy0": bbox[1],
                "bbox_fx1": bbox[2],
                "bbox_fy1": bbox[3],
                "render_dpi": render_dpi,
                "autocontrast_cutoff": cutoff,
                "contrast": contrast,
                "sharpness": sharpness,
                "description": " ".join(reversed(comment_lines)),
                "generator_script_basename": script_name,
                "generator_source_sha256": record["source_sha256"],
                "generator_timestamp": record["timestamp"],
                "generator_tool_name": record["tool_name"],
            }
        )
    results.extend(
        direct_generator_specs(
            tree,
            source,
            script_name,
            record,
            globals_,
            page_index,
        )
    )
    results.extend(
        loop_generator_specs(
            tree,
            source,
            script_name,
            record,
            globals_,
            page_index,
        )
    )
    return results


def parse_timestamp(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def main() -> int:
    args = parse_args()
    min_mtime = args.min_mtime_utc.replace("Z", "+00:00")
    selected: dict[str, dict[str, Any]] = {}
    tight_keys: set[str] = set()
    routine_keys: set[str] = set()
    for path in sorted(args.scratch_dir.glob("*.png"), key=lambda item: item.name.lower()):
        tight_match = TIGHT_RE.fullmatch(path.name)
        routine_match = ROUTINE_RE.fullmatch(path.name)
        match = tight_match or routine_match
        if not match:
            continue
        index = int(match.group(1))
        if not args.start_index <= index <= args.end_index:
            continue
        mtime = utc_mtime(path)
        if min_mtime and mtime < min_mtime:
            continue
        with Image.open(path) as image:
            width, height = image.size
            mode = image.mode
            dpi = image.info.get("dpi")
        key = path.name.lower()
        selected[key] = {
            "basename": path.name,
            "evidence_class": (
                "tight_symbol_or_formula_crop"
                if tight_match
                else "routine_full_width_page_band"
            ),
            "index": index,
            "band_tag": routine_match.group(2).lower() if routine_match else "",
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
            "width_px": width,
            "height_px": height,
            "mode": mode,
            "embedded_dpi": list(dpi) if dpi else None,
            "mtime_utc": mtime,
        }
        if tight_match:
            tight_keys.add(key)
        else:
            routine_keys.add(key)

    reads: dict[str, list[dict[str, str]]] = defaultdict(list)
    read_tool_keys: dict[str, str] = {}
    read_attachments: dict[str, list[dict[str, Any]]] = defaultdict(list)
    generation_sources: dict[str, dict[str, Any]] = {}
    line_count = 0
    parsed_tool_lines = 0
    malformed_candidate_lines = 0
    read_tool_count = 0
    tool_counts: Counter[str] = Counter()
    candidate_bytes = 0

    with args.session_log.open("rb") as handle:
        for raw in handle:
            line_count += 1
            if b'"tool_use"' not in raw and b'"tool_use_id"' not in raw:
                continue
            candidate_bytes += len(raw)
            try:
                record = json.loads(raw)
            except (UnicodeDecodeError, json.JSONDecodeError):
                malformed_candidate_lines += 1
                continue
            parsed_tool_lines += 1
            timestamp = str(record.get("timestamp") or "")
            for tool in tool_uses(record):
                name = tool.get("name")
                tool_counts[str(name or "")] += 1
                tool_id = str(tool.get("id") or "")
                inputs = tool.get("input")
                if not isinstance(inputs, dict):
                    continue
                if name == "Read":
                    read_tool_count += 1
                    file_path = inputs.get("file_path")
                    if not isinstance(file_path, str):
                        continue
                    key = basename(file_path).lower()
                    if key in selected:
                        read_tool_keys[tool_id] = key
                        reads[key].append(
                            {
                                "timestamp": timestamp,
                                "tool_use_id": tool_id,
                            }
                        )
                elif name in {"Bash", "PowerShell", "Write", "Edit"}:
                    if name in {"Bash", "PowerShell"}:
                        source_text = inputs.get("command")
                        source_path = ""
                    elif name == "Write":
                        source_text = inputs.get("content")
                        source_path = str(inputs.get("file_path") or "")
                    else:
                        source_text = "\n".join(
                            str(inputs.get(field) or "")
                            for field in ("old_string", "new_string")
                        )
                        source_path = str(inputs.get("file_path") or "")
                    if not isinstance(source_text, str):
                        continue
                    searchable = f"{source_path}\n{source_text}"
                    if "png" not in searchable.lower():
                        continue
                    indexes = sorted(
                        {
                            int(value)
                            for value in INDEX_IN_COMMAND_RE.findall(searchable)
                            if args.start_index <= int(value) <= args.end_index
                        }
                    )
                    if not indexes:
                        continue
                    source_sha = hashlib.sha256(
                        source_text.encode("utf-8")
                    ).hexdigest().upper()
                    identity = f"{name}:{source_path}:{source_sha}"
                    generation_sources.setdefault(
                        identity,
                        {
                            "tool_name": name,
                            "source_path": source_path,
                            "source_sha256": source_sha,
                            "timestamp": timestamp,
                            "tool_use_id": tool_id,
                            "indexes": indexes,
                            "source_text": source_text,
                        },
                    )
            for result in read_attachment_results(record):
                tool_id = str(result.get("tool_use_id") or "")
                key = read_tool_keys.get(tool_id)
                if key not in tight_keys:
                    continue
                content = result.get("content")
                if not isinstance(content, list):
                    continue
                for item in content:
                    if not isinstance(item, dict) or item.get("type") != "image":
                        continue
                    source = item.get("source")
                    if not isinstance(source, dict) or source.get("type") != "base64":
                        continue
                    try:
                        attachment_bytes = base64.b64decode(source["data"], validate=True)
                        with Image.open(io.BytesIO(attachment_bytes)) as attachment:
                            attachment_image = attachment.convert("L")
                            attachment_size = attachment_image.size
                            attachment_mode = attachment.mode
                        with Image.open(args.scratch_dir / selected[key]["basename"]) as image:
                            resized = image.convert("L").resize(
                                attachment_size,
                                Image.Resampling.LANCZOS,
                            )
                        difference = ImageChops.difference(resized, attachment_image)
                        histogram = difference.histogram()
                        changed = sum(histogram[1:])
                        total = attachment_size[0] * attachment_size[1]
                        mean_error = float(ImageStat.Stat(difference).mean[0])
                        max_error = max(
                            (value for value, count in enumerate(histogram) if count),
                            default=0,
                        )
                        correlated = (
                            mean_error <= 0.25
                            and max_error <= 64
                            and changed / total <= 0.08
                        )
                    except (
                        KeyError,
                        TypeError,
                        ValueError,
                        OSError,
                        base64.binascii.Error,
                    ):
                        continue
                    read_attachments[key].append(
                        {
                            "tool_use_id": tool_id,
                            "attachment_bytes": len(attachment_bytes),
                            "attachment_sha256": hashlib.sha256(
                                attachment_bytes
                            ).hexdigest().upper(),
                            "attachment_width_px": attachment_size[0],
                            "attachment_height_px": attachment_size[1],
                            "attachment_mode": attachment_mode,
                            "source_lanczos_changed_pixels": changed,
                            "source_lanczos_total_pixels": total,
                            "source_lanczos_changed_fraction": round(
                                changed / total,
                                12,
                            ),
                            "source_lanczos_mean_absolute_error": round(
                                mean_error,
                                12,
                            ),
                            "source_lanczos_max_absolute_error": max_error,
                            "source_attachment_correlation_pass": correlated,
                        }
                    )

    spec_candidates: dict[str, list[dict[str, Any]]] = defaultdict(list)
    parsed_spec_count = 0
    for record in generation_sources.values():
        if "Théorie des Intersections" not in str(record.get("source_text") or ""):
            continue
        for spec in generator_specs(record):
            spec_candidates[spec["basename"].lower()].append(spec)
            parsed_spec_count += 1

    retained_script_count = 0
    if args.generator_script_dir:
        retained_paths = {
            path
            for pattern in ("cve0p*.py", "zoom*.py")
            for path in args.generator_script_dir.glob(pattern)
        }
        for script_path in sorted(retained_paths):
            source = script_path.read_text(encoding="utf-8", errors="replace")
            indexes = {
                int(value)
                for value in INDEX_IN_COMMAND_RE.findall(
                    f"{script_path.name}\n{source}"
                )
                if args.start_index <= int(value) <= args.end_index
            }
            if not indexes or "Théorie des Intersections" not in source:
                continue
            retained_script_count += 1
            record = {
                "tool_name": "retained_local_generator_script",
                "source_path": str(script_path),
                "source_sha256": hashlib.sha256(
                    source.encode("utf-8")
                ).hexdigest().upper(),
                "timestamp": utc_mtime(script_path),
                "tool_use_id": "",
                "indexes": sorted(indexes),
                "source_text": source,
            }
            generation_sources.setdefault(
                (
                    "retained_local_generator_script:"
                    f"{script_path.name}:{record['source_sha256']}"
                ),
                record,
            )
            for spec in generator_specs(record):
                spec_candidates[spec["basename"].lower()].append(spec)
                parsed_spec_count += 1

    files = []
    tight_mapping_errors: list[str] = []
    routine_mapping_warnings: list[str] = []
    for key in sorted(selected, key=lambda item: (selected[item]["index"], item)):
        row = dict(selected[key])
        file_timestamp = parse_timestamp(row["mtime_utc"])
        events = [
            event
            for event in reads.get(key, [])
            if parse_timestamp(event["timestamp"]) >= file_timestamp
        ]
        event_ids = {event["tool_use_id"] for event in events}
        row["read_count"] = len(events)
        row["first_read_timestamp"] = events[0]["timestamp"] if events else ""
        row["last_read_timestamp"] = events[-1]["timestamp"] if events else ""
        row["read_events"] = events
        row["read_attachment_events"] = [
            event
            for event in read_attachments.get(key, [])
            if event["tool_use_id"] in event_ids
        ]
        candidates = spec_candidates.get(key, [])
        if not candidates:
            message = f"no generator spec for {row['basename']}"
            if key in tight_keys:
                tight_mapping_errors.append(message)
            else:
                routine_mapping_warnings.append(message)
        else:
            chosen = min(
                candidates,
                key=lambda item: abs(
                    (
                        file_timestamp - parse_timestamp(item["generator_timestamp"])
                    ).total_seconds()
                ),
            )
            row.update(chosen)
            row["generator_candidate_count"] = len(candidates)
            row["generator_to_file_mtime_seconds"] = round(
                (
                    file_timestamp - parse_timestamp(chosen["generator_timestamp"])
                ).total_seconds(),
                6,
            )
            if int(chosen["parent_pdf_index_0based"]) != int(row["index"]):
                message = (
                    "generator page mismatch for "
                    f"{row['basename']}: {chosen['parent_pdf_index_0based']}"
                )
                if key in tight_keys:
                    tight_mapping_errors.append(message)
                else:
                    routine_mapping_warnings.append(message)
        files.append(row)

    tight_files = [row for row in files if row["evidence_class"].startswith("tight")]
    routine_files = [row for row in files if row["evidence_class"].startswith("routine")]
    payload = {
        "schema": "sga6-claude-crop-provenance-extract-v1",
        "source_session_bytes": args.session_log.stat().st_size,
        "source_session_mtime_utc": utc_mtime(args.session_log),
        "start_index": args.start_index,
        "end_index": args.end_index,
        "selected_file_count": len(tight_files),
        "selected_total_bytes": sum(row["bytes"] for row in tight_files),
        "selected_index_counts": dict(
            sorted(Counter(row["index"] for row in tight_files).items())
        ),
        "files_with_read_events": sum(bool(row["read_count"]) for row in tight_files),
        "total_selected_read_events": sum(row["read_count"] for row in tight_files),
        "selected_read_attachment_events": sum(
            len(row["read_attachment_events"]) for row in tight_files
        ),
        "selected_read_attachment_correlations_pass": sum(
            bool(event["source_attachment_correlation_pass"])
            for row in tight_files
            for event in row["read_attachment_events"]
        ),
        "routine_file_count": len(routine_files),
        "routine_total_bytes": sum(row["bytes"] for row in routine_files),
        "routine_files_with_read_events": sum(
            bool(row["read_count"]) for row in routine_files
        ),
        "total_routine_read_events": sum(row["read_count"] for row in routine_files),
        "generation_source_count": len(generation_sources),
        "retained_generator_script_count": retained_script_count,
        "parsed_generator_spec_count": parsed_spec_count,
        "tight_provenance_mapping_errors": tight_mapping_errors,
        "routine_provenance_mapping_warnings": routine_mapping_warnings,
        "session_scan": {
            "line_count": line_count,
            "parsed_tool_lines": parsed_tool_lines,
            "malformed_candidate_lines": malformed_candidate_lines,
            "candidate_bytes": candidate_bytes,
            "read_tool_count": read_tool_count,
            "tool_counts": dict(sorted(tool_counts.items())),
        },
        "files": tight_files,
        "routine_files": routine_files,
        "generation_sources": sorted(
            generation_sources.values(),
            key=lambda row: (
                row["indexes"][0],
                row["timestamp"],
                row["tool_name"],
                row["source_sha256"],
            ),
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print(
        json.dumps(
            {
                "selected_file_count": payload["selected_file_count"],
                "selected_total_bytes": payload["selected_total_bytes"],
                "files_with_read_events": payload["files_with_read_events"],
                "total_selected_read_events": payload["total_selected_read_events"],
                "generation_source_count": payload["generation_source_count"],
                "retained_generator_script_count": (
                    payload["retained_generator_script_count"]
                ),
                "parsed_generator_spec_count": payload["parsed_generator_spec_count"],
                "tight_provenance_mapping_errors": (
                    payload["tight_provenance_mapping_errors"]
                ),
                "routine_provenance_mapping_warnings": (
                    payload["routine_provenance_mapping_warnings"]
                ),
                "routine_file_count": payload["routine_file_count"],
                "routine_total_bytes": payload["routine_total_bytes"],
                "routine_files_with_read_events": (
                    payload["routine_files_with_read_events"]
                ),
                "session_scan": payload["session_scan"],
                "output": str(args.output),
            },
            indent=2,
        )
    )
    return 1 if tight_mapping_errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
