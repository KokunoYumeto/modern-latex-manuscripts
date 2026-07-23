#!/usr/bin/env python3
"""Build the incremental SGA6 high-detail source-audit crop release.

The source scratch directory is live and large. This builder reads it in
place, selects only files that can be associated with a generator script for
the controlling parent PDF inside one closed time interval, writes compact
public metadata, and creates temporary ZIPs without copying the source image
tree.
"""

from __future__ import annotations

import argparse
import ast
import bisect
import csv
import hashlib
import json
import re
import sys
import warnings
import zipfile
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import fitz
from PIL import Image


EXPLICIT_ZIP = (
    "10k_SGA6_SourceAudit_Explicit_Targeted_HighDetail_Crops_"
    "ColdReverify_idx315_321_20260723.zip"
)
RECOVERED_ZIP = (
    "10m_SGA6_SourceAudit_Recovered_Named_HighDetail_Crops_"
    "ColdReverify_idx315_321_20260723.zip"
)
METADATA_ZIP = (
    "10l_SGA6_SourceAudit_Crop_Provenance_RightsBlocked_Metadata_"
    "ColdReverify_idx315_321_20260723.zip"
)
README_NAME = "SGA6_HighDetail_SourceAudit_Crops_idx315_321_README_20260723.md"
PARENT_NAME = (
    "SGA6_HighDetail_SourceAudit_Crops_idx315_321_PARENT_SOURCE_20260723.json"
)
EXPLICIT_MANIFEST_NAME = (
    "SGA6_Explicit_Targeted_HighDetail_Crops_idx315_321_Manifest_20260723.csv"
)
RECOVERED_MANIFEST_NAME = (
    "SGA6_Recovered_Named_HighDetail_Crops_idx315_321_Manifest_20260723.csv"
)
BLOCKED_MANIFEST_NAME = (
    "SGA6_Routine_PageBands_idx315_321_RightsBlocked_Manifest_20260723.csv"
)
AUDIT_CONTEXT_NAME = "SGA6_HighDetail_Crops_idx315_321_Audit_Context_20260723.csv"
VALIDATION_NAME = (
    "SGA6_HighDetail_SourceAudit_Crops_idx315_321_VALIDATION_20260723.json"
)
UPLOAD_MANIFEST_NAME = (
    "SGA6_HighDetail_SourceAudit_Crops_idx315_321_"
    "ZENODO_UPLOAD_MANIFEST_20260723.csv"
)
SHA_NAME = "SGA6_HighDetail_SourceAudit_Crops_idx315_321_SHA256SUMS_20260723.txt"

PRIVATE_MARKERS = (
    "c:\\users\\",
    "floris",
    "chatnotes",
    "claude",
    "codex",
    "thread_id",
    "source_thread_id",
    "@gmail.",
    "@outlook.",
)
EXPLICIT_RE = re.compile(r"^(?:zoom|zoomp|peek|recheck)", re.IGNORECASE)
GENERIC_IMAGE_PATTERNS = (
    re.compile(r"^cve0p\d+_(?:top|a|b|c|d)\.png$", re.IGNORECASE),
    re.compile(r"^[pb]\d+_b[1-5]\.png$", re.IGNORECASE),
    re.compile(r"^cvi\d+_(?:top|a|b|c|d)\.png$", re.IGNORECASE),
    re.compile(r"^cvpref_[ab]\.png$", re.IGNORECASE),
    re.compile(r"^cvtitle_(?:top|bot)\.png$", re.IGNORECASE),
    re.compile(r"^cvtdm_\d+\.png$", re.IGNORECASE),
)
ROUTINE_SCRIPT_FAMILIES = {
    "bands",
    "pgcrop",
    "cvintro",
    "cvpreface",
    "cvtitle",
    "cvtdm",
    "cvcodex",
    "coldverify",
    "render",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scratch-dir", type=Path, required=True)
    parser.add_argument("--script-dir", type=Path, required=True)
    parser.add_argument("--parent-pdf", type=Path, required=True)
    parser.add_argument("--cert-log", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--zip-dir", type=Path, required=True)
    parser.add_argument("--start-after-utc", required=True)
    parser.add_argument("--cutoff-utc", required=True)
    parser.add_argument("--start-index", type=int, required=True)
    parser.add_argument("--end-index", type=int, required=True)
    parser.add_argument("--association-window-seconds", type=float, default=900.0)
    return parser.parse_args()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def utc_mtime(path: Path) -> str:
    return datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).isoformat()


def parse_utc(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def write_text_lf(path: Path, text: str) -> None:
    path.write_bytes(text.encode("utf-8"))


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def privacy_hits(values: list[str]) -> list[str]:
    joined = "\n".join(values).lower()
    return sorted(marker for marker in PRIVATE_MARKERS if marker in joined)


def sanitize_public_text(value: str) -> str:
    sanitized = re.sub(r"(?i)\bfloris\b", "[archive owner]", value)
    sanitized = re.sub(r"(?i)\b(?:claude|codex)\b", "[agent]", sanitized)
    sanitized = re.sub(
        r"(?i)\b[a-z]:\\(?:[^\\\s,;)\]]+\\)*[^,\r\n;)\]]*",
        "[private path]",
        sanitized,
    )
    return sanitized


def public_generator_basename(path: Path) -> str:
    if privacy_hits([path.name]):
        return f"generator_{sha256(path)[:12].lower()}.py"
    return path.name


def png_metadata(path: Path) -> dict[str, object]:
    # These are intentionally enormous audit crops.
    Image.MAX_IMAGE_PIXELS = None
    with Image.open(path) as image:
        image.verify()
    with Image.open(path) as image:
        info = {str(key): str(value) for key, value in image.info.items()}
        dpi = image.info.get("dpi")
        return {
            "width_px": image.width,
            "height_px": image.height,
            "color_mode": image.mode,
            "embedded_dpi_x": round(float(dpi[0]), 4) if dpi else "",
            "embedded_dpi_y": round(float(dpi[1]), 4) if dpi else "",
            "metadata_text": json.dumps(info, ensure_ascii=True, sort_keys=True),
        }


def safe_eval(node: ast.AST, env: dict[str, object]) -> object | None:
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.Name):
        return env.get(node.id)
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        value = safe_eval(node.operand, env)
        return -value if isinstance(value, (int, float)) else None
    if isinstance(node, ast.BinOp):
        left = safe_eval(node.left, env)
        right = safe_eval(node.right, env)
        try:
            if isinstance(node.op, ast.Add):
                return left + right  # type: ignore[operator]
            if isinstance(node.op, ast.Sub):
                return left - right  # type: ignore[operator]
            if isinstance(node.op, ast.Mult):
                return left * right  # type: ignore[operator]
            if isinstance(node.op, ast.Div):
                return left / right  # type: ignore[operator]
            if isinstance(node.op, ast.Mod):
                return left % right  # type: ignore[operator]
        except (TypeError, ValueError, ZeroDivisionError):
            return None
    if isinstance(node, ast.JoinedStr):
        parts: list[str] = []
        for value in node.values:
            if isinstance(value, ast.Constant):
                parts.append(str(value.value))
            elif isinstance(value, ast.FormattedValue):
                evaluated = safe_eval(value.value, env)
                if evaluated is None:
                    return None
                parts.append(str(evaluated))
        return "".join(parts)
    if isinstance(node, ast.List):
        return [safe_eval(item, env) for item in node.elts]
    if isinstance(node, ast.Tuple):
        return tuple(safe_eval(item, env) for item in node.elts)
    if (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id in {"str", "int", "float"}
        and node.args
    ):
        value = safe_eval(node.args[0], env)
        try:
            return {"str": str, "int": int, "float": float}[node.func.id](value)
        except (TypeError, ValueError):
            return None
    return None


def script_page_index(text: str) -> int | None:
    patterns = (
        r"\bidx\s*=\s*(\d+)",
        r"\bpg\s*=\s*d\[(\d+)\]",
        r"\bpg\s*=\s*doc\[(\d+)\]",
        r"\bpage\s*=\s*d\[(\d+)\]",
        r"\bpage\s*=\s*doc\[(\d+)\]",
        r"\bP\s*=\s*d\[(\d+)\]",
        r"\bp\s*=\s*d\[(\d+)\]",
    )
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return int(match.group(1))
    return None


def script_output_parameters(text: str) -> dict[str, dict[str, object]]:
    """Recover output filename and common crop parameters without executing code."""
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", SyntaxWarning)
            tree = ast.parse(text)
    except SyntaxError:
        return {}

    global_env: dict[str, object] = {"OUT": ""}
    for node in tree.body:
        if (
            isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
        ):
            value = safe_eval(node.value, global_env)
            if value is not None:
                global_env[node.targets[0].id] = value

    definitions = {
        node.name: node for node in tree.body if isinstance(node, ast.FunctionDef)
    }
    outputs: dict[str, dict[str, object]] = {}
    for node in tree.body:
        if not (
            isinstance(node, ast.Expr)
            and isinstance(node.value, ast.Call)
            and isinstance(node.value.func, ast.Name)
            and node.value.func.id in definitions
        ):
            continue
        call = node.value
        function = definitions[call.func.id]
        env = dict(global_env)
        for argument, value_node in zip(function.args.args, call.args):
            env[argument.arg] = safe_eval(value_node, global_env)
        for keyword in call.keywords:
            if keyword.arg:
                env[keyword.arg] = safe_eval(keyword.value, global_env)

        for statement in function.body:
            if (
                isinstance(statement, ast.Assign)
                and len(statement.targets) == 1
                and isinstance(statement.targets[0], ast.Name)
            ):
                value = safe_eval(statement.value, env)
                if value is not None:
                    env[statement.targets[0].id] = value

        for statement in ast.walk(function):
            if not (
                isinstance(statement, ast.Call)
                and isinstance(statement.func, ast.Attribute)
                and statement.func.attr == "save"
                and statement.args
            ):
                continue
            output_value = safe_eval(statement.args[0], env)
            if not isinstance(output_value, str):
                continue
            basename = Path(output_value.replace("\\", "/")).name
            if not basename.lower().endswith(".png"):
                continue
            fields = {
                key: env.get(key, "")
                for key in (
                    "fx0",
                    "fx1",
                    "fy0",
                    "fy1",
                    "x0",
                    "x1",
                    "y0",
                    "y1",
                    "dpi",
                    "contrast",
                    "sharp",
                    "cut",
                )
            }
            outputs[basename] = fields
    return outputs


def script_family(path: Path) -> str:
    match = re.match(r"^[A-Za-z]+", path.stem)
    return match.group(0).lower() if match else path.stem.lower()


def classify(image: Path, generator: Path) -> str:
    if EXPLICIT_RE.match(image.name) or EXPLICIT_RE.match(generator.stem):
        return "explicit_targeted"
    if any(pattern.fullmatch(image.name) for pattern in GENERIC_IMAGE_PATTERNS):
        return "routine_page_derivative"
    if script_family(generator) in ROUTINE_SCRIPT_FAMILIES:
        return "routine_page_derivative"
    return "recovered_named_targeted"


def parse_audit_context(cert_bytes: bytes) -> tuple[list[dict[str, object]], dict[int, dict[str, object]]]:
    text = cert_bytes.decode("utf-8", errors="replace")
    rows: list[dict[str, object]] = []
    by_index: dict[int, dict[str, object]] = {}
    heading_pattern = re.compile(r"^###\s+#(?P<number>\d+).*?\bidx(?P<idx>\d+)\b(?P<tail>.*)$")
    footer_pattern = re.compile(r"footer\s+[«\"](?P<printed>\d+)[»\"]", re.IGNORECASE)
    for line in text.splitlines():
        match = heading_pattern.match(line)
        if not match:
            continue
        index = int(match.group("idx"))
        footer = footer_pattern.search(line)
        normalized = sanitize_public_text(re.sub(r"\s+", " ", line).strip())
        if len(normalized) > 1200:
            normalized = normalized[:1197] + "..."
        row = {
            "audit_entry_number": int(match.group("number")),
            "parent_pdf_index_0based": index,
            "parent_pdf_page_1based": index + 1,
            "printed_page_from_audit": int(footer.group("printed")) if footer else "",
            "audit_heading": normalized,
        }
        rows.append(row)
        by_index[index] = row
    rows.sort(key=lambda row: (int(row["parent_pdf_index_0based"]), int(row["audit_entry_number"])))
    return rows, by_index


def build_manifest_row(
    image: Path,
    generator: Path,
    script_text: str,
    association_seconds: float,
    category: str,
    image_meta: dict[str, object],
    digest: str,
    parent_sha: str,
    output_parameters: dict[str, dict[str, object]],
    audit_by_index: dict[int, dict[str, object]],
) -> dict[str, object]:
    index = script_page_index(script_text)
    audit = audit_by_index.get(index if index is not None else -1, {})
    parameters = output_parameters.get(image.name, {})
    if all(parameters.get(key, "") != "" for key in ("fx0", "fx1", "fy0", "fy1")):
        bbox_coordinate_system = "fraction_of_parent_page"
    elif all(parameters.get(key, "") != "" for key in ("x0", "x1", "y0", "y1")):
        bbox_coordinate_system = "parent_pdf_points"
    else:
        bbox_coordinate_system = "not_recovered"
    if image.name in output_parameters:
        provenance_status = "exact_generator_output_recovered"
    else:
        provenance_status = "nearest_preceding_parent_script_within_900_seconds"
    processing = []
    if "csGRAY" in script_text:
        processing.append("grayscale")
    if "autocontrast" in script_text:
        processing.append("autocontrast")
    if "ImageEnhance.Contrast" in script_text:
        processing.append("contrast_enhancement")
    if "ImageEnhance.Sharpness" in script_text:
        processing.append("sharpness_enhancement")
    return {
        "archive_path": (
            f"images/{'explicit_targeted' if category == 'explicit_targeted' else 'recovered_named'}/"
            f"{image.name}"
            if category != "routine_page_derivative"
            else ""
        ),
        "source_basename": image.name,
        "bytes": image.stat().st_size,
        "sha256": digest,
        "width_px": image_meta["width_px"],
        "height_px": image_meta["height_px"],
        "color_mode": image_meta["color_mode"],
        "embedded_dpi_x": image_meta["embedded_dpi_x"],
        "embedded_dpi_y": image_meta["embedded_dpi_y"],
        "modified_utc": utc_mtime(image),
        "category": category,
        "public_disposition": (
            "public_targeted_source_audit_evidence_no_license_grant"
            if category != "routine_page_derivative"
            else "rights_blocked_not_public"
        ),
        "parent_pdf_index_0based": index if index is not None else "",
        "parent_pdf_page_1based": index + 1 if index is not None else "",
        "printed_page_from_audit": audit.get("printed_page_from_audit", ""),
        "linked_tex_object": "sga6_fr_workpass.tex",
        "linked_audit_entry": audit.get("audit_entry_number", ""),
        "generator_script_basename": public_generator_basename(generator),
        "generator_script_sha256": sha256(generator),
        "generator_script_modified_utc": utc_mtime(generator),
        "association_seconds": round(association_seconds, 6),
        "provenance_status": provenance_status,
        "bbox_coordinate_system": bbox_coordinate_system,
        "bbox_x0": parameters.get("fx0", parameters.get("x0", "")),
        "bbox_y0": parameters.get("fy0", parameters.get("y0", "")),
        "bbox_x1": parameters.get("fx1", parameters.get("x1", "")),
        "bbox_y1": parameters.get("fy1", parameters.get("y1", "")),
        "render_dpi": parameters.get("dpi", ""),
        "processing_profile": ";".join(processing) if processing else "not_recovered",
        "qa_disposition": "used_in_sga6_source_audit_not_translation_certification",
        "parent_scan_sha256": parent_sha,
    }


def zip_payload(
    zip_path: Path,
    rows: list[dict[str, object]],
    scratch_dir: Path,
    metadata_paths: list[Path],
) -> dict[str, object]:
    fixed_zip_time = (2026, 7, 23, 0, 0, 0)

    def add_file(archive: zipfile.ZipFile, path: Path, member_name: str) -> None:
        info = zipfile.ZipInfo(member_name, date_time=fixed_zip_time)
        info.compress_type = zipfile.ZIP_STORED
        info.create_system = 3
        info.external_attr = 0o100644 << 16
        archive.writestr(info, path.read_bytes())

    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_STORED) as archive:
        for metadata_path in metadata_paths:
            add_file(archive, metadata_path, f"metadata/{metadata_path.name}")
        for row in rows:
            add_file(
                archive,
                scratch_dir / str(row["source_basename"]),
                str(row["archive_path"]),
            )

    expected = {
        **{
            f"metadata/{path.name}": (path.stat().st_size, sha256(path))
            for path in metadata_paths
        },
        **{
            str(row["archive_path"]): (int(row["bytes"]), str(row["sha256"]))
            for row in rows
        },
    }
    errors: list[str] = []
    member_rows: list[dict[str, object]] = []
    with zipfile.ZipFile(zip_path, "r") as archive:
        bad_member = archive.testzip()
        if bad_member:
            errors.append(f"CRC failure: {bad_member}")
        names = archive.namelist()
        if len(names) != len(set(names)):
            errors.append("duplicate ZIP member names")
        if set(names) != set(expected):
            errors.append(
                "ZIP set mismatch "
                f"missing={sorted(set(expected) - set(names))} "
                f"extra={sorted(set(names) - set(expected))}"
            )
        for member in archive.infolist():
            if member.filename.startswith("/") or ".." in Path(member.filename).parts:
                errors.append(f"unsafe ZIP member: {member.filename}")
            data = archive.read(member.filename)
            digest = sha256_bytes(data)
            size = len(data)
            expected_item = expected.get(member.filename)
            if expected_item and expected_item != (size, digest):
                errors.append(f"ZIP member identity mismatch: {member.filename}")
            member_rows.append(
                {"path": member.filename, "bytes": size, "sha256": digest}
            )
    return {
        "filename": zip_path.name,
        "bytes": zip_path.stat().st_size,
        "sha256": sha256(zip_path),
        "members": len(member_rows),
        "image_members": len(rows),
        "uncompressed_bytes": sum(int(row["bytes"]) for row in member_rows),
        "errors": errors,
    }


def main() -> int:
    args = parse_args()
    scratch_dir = args.scratch_dir.resolve()
    script_dir = args.script_dir.resolve()
    parent_pdf = args.parent_pdf.resolve()
    cert_log = args.cert_log.resolve()
    output_dir = args.output_dir.resolve()
    zip_dir = args.zip_dir.resolve()
    start_after = parse_utc(args.start_after_utc)
    cutoff = parse_utc(args.cutoff_utc)
    if start_after >= cutoff:
        raise ValueError("--start-after-utc must precede --cutoff-utc")
    start_after_timestamp = start_after.timestamp()
    cutoff_timestamp = cutoff.timestamp()
    output_dir.mkdir(parents=True, exist_ok=True)
    zip_dir.mkdir(parents=True, exist_ok=True)

    errors: list[str] = []
    parent_sha = sha256(parent_pdf)
    parent_stat = parent_pdf.stat()
    with fitz.open(parent_pdf) as document:
        parent_pages = document.page_count
        parent_metadata = document.metadata

    cert_bytes = cert_log.read_bytes()
    cert_sha = sha256_bytes(cert_bytes)
    all_audit_rows, audit_by_index = parse_audit_context(cert_bytes)

    all_scripts: list[dict[str, Any]] = []
    for path in script_dir.glob("*.py"):
        if path.stat().st_mtime > cutoff_timestamp:
            continue
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        all_scripts.append(
            {
                "mtime": path.stat().st_mtime,
                "path": path,
                "text": text,
                "is_parent": parent_pdf.name in text,
                "outputs": script_output_parameters(text),
            }
        )
    all_scripts.sort(key=lambda row: (float(row["mtime"]), str(row["path"]).lower()))
    script_times = [float(row["mtime"]) for row in all_scripts]

    associations: list[dict[str, Any]] = []
    for image in sorted(scratch_dir.glob("*.png"), key=lambda path: path.name.lower()):
        stat = image.stat()
        if stat.st_mtime <= start_after_timestamp or stat.st_mtime > cutoff_timestamp:
            continue
        position = bisect.bisect_right(script_times, stat.st_mtime) - 1
        if position < 0:
            continue
        script = all_scripts[position]
        delta = stat.st_mtime - float(script["mtime"])
        if (
            delta < 0
            or delta > args.association_window_seconds
            or not bool(script["is_parent"])
        ):
            continue
        associations.append(
            {
                "image": image,
                "script": script["path"],
                "script_text": script["text"],
                "script_outputs": script["outputs"],
                "delta": delta,
                "category": classify(image, script["path"]),
                "initial_size": stat.st_size,
                "initial_mtime_ns": stat.st_mtime_ns,
            }
        )

    manifest_rows: list[dict[str, object]] = []
    content_hash_paths: dict[str, list[str]] = defaultdict(list)
    png_privacy: dict[str, list[str]] = {}
    for association in associations:
        image = association["image"]
        try:
            metadata = png_metadata(image)
        except Exception as exc:
            errors.append(f"invalid PNG {image.name}: {exc}")
            continue
        digest = sha256(image)
        row = build_manifest_row(
            image=image,
            generator=association["script"],
            script_text=association["script_text"],
            association_seconds=float(association["delta"]),
            category=str(association["category"]),
            image_meta=metadata,
            digest=digest,
            parent_sha=parent_sha,
            output_parameters=association["script_outputs"],
            audit_by_index=audit_by_index,
        )
        manifest_rows.append(row)
        content_hash_paths[digest].append(image.name)
        hits = privacy_hits([image.name, str(metadata["metadata_text"])])
        if hits:
            png_privacy[image.name] = hits

    if png_privacy:
        errors.append(f"PNG filename or metadata privacy hits: {png_privacy}")

    explicit_rows = [
        row for row in manifest_rows if row["category"] == "explicit_targeted"
    ]
    recovered_rows = [
        row
        for row in manifest_rows
        if row["category"] == "recovered_named_targeted"
    ]
    blocked_rows = [
        row
        for row in manifest_rows
        if row["category"] == "routine_page_derivative"
    ]
    explicit_rows.sort(key=lambda row: str(row["source_basename"]).lower())
    recovered_rows.sort(key=lambda row: str(row["source_basename"]).lower())
    blocked_rows.sort(key=lambda row: str(row["source_basename"]).lower())
    represented_indices = sorted(
        {
            int(row["parent_pdf_index_0based"])
            for row in manifest_rows
            if row["parent_pdf_index_0based"] != ""
        }
    )
    represented_index_set = set(represented_indices)
    unexpected_indices = [
        index
        for index in represented_indices
        if index < args.start_index or index > args.end_index
    ]
    if unexpected_indices:
        errors.append(
            "represented parent indices fall outside declared interval: "
            f"{unexpected_indices}"
        )
    audit_rows = [
        row
        for row in all_audit_rows
        if int(row["parent_pdf_index_0based"]) in represented_index_set
    ]

    if len(manifest_rows) != len(associations):
        errors.append("manifest rows do not close over associated image set")
    if len(explicit_rows) + len(recovered_rows) + len(blocked_rows) != len(
        manifest_rows
    ):
        errors.append("classification counts do not close over manifest rows")

    fields = list(manifest_rows[0].keys()) if manifest_rows else []
    explicit_manifest = output_dir / EXPLICIT_MANIFEST_NAME
    recovered_manifest = output_dir / RECOVERED_MANIFEST_NAME
    blocked_manifest = output_dir / BLOCKED_MANIFEST_NAME
    audit_context = output_dir / AUDIT_CONTEXT_NAME
    write_csv(explicit_manifest, explicit_rows, fields)
    write_csv(recovered_manifest, recovered_rows, fields)
    write_csv(blocked_manifest, blocked_rows, fields)
    write_csv(
        audit_context,
        audit_rows,
        [
            "audit_entry_number",
            "parent_pdf_index_0based",
            "parent_pdf_page_1based",
            "printed_page_from_audit",
            "audit_heading",
        ],
    )

    parent_identity = {
        "title": "Theorie des intersections et theoreme de Riemann-Roch",
        "series_context": "SGA 6 source-audit parent reader",
        "source_file_basename": parent_pdf.name,
        "bytes": parent_stat.st_size,
        "sha256": parent_sha,
        "pages": parent_pages,
        "pdf_metadata": parent_metadata,
        "rotation": 0,
        "parent_scan_not_duplicated_in_this_release": True,
        "rights_status": (
            "Underlying French work and scan rights remain with their holders. "
            "No blanket license or rights transfer is asserted."
        ),
        "crop_publication_policy": (
            "Only targeted scholarly verification crops are included. Routine "
            "page-band derivatives are hash-manifested as rights-blocked and "
            "their pixels are not redistributed."
        ),
        "render_resolution_caveat": (
            "Generator render DPI records output rasterization resolution, not "
            "new optical detail beyond the parent scan."
        ),
        "cert_log_basename": cert_log.name,
        "cert_log_bytes_at_packaging_snapshot": len(cert_bytes),
        "cert_log_sha256_at_packaging_snapshot": cert_sha,
        "image_snapshot_start_after_utc": start_after.isoformat(),
        "image_snapshot_cutoff_utc": cutoff.isoformat(),
        "represented_parent_pdf_indices": {
            "distinct_indices": len(represented_indices),
            "minimum_index_0based": min(represented_indices)
            if represented_indices
            else None,
            "maximum_index_0based": max(represented_indices)
            if represented_indices
            else None,
            "continuous_coverage_claimed": False,
        },
    }
    parent_path = output_dir / PARENT_NAME
    write_text_lf(
        parent_path,
        json.dumps(parent_identity, indent=2, ensure_ascii=True) + "\n",
    )

    duplicate_groups = {
        digest: sorted(paths)
        for digest, paths in content_hash_paths.items()
        if len(paths) > 1
    }
    recovered_archive_text = (
        f"""- `{RECOVERED_ZIP}` contains {len(recovered_rows)} additional named
  formula, glyph, punctuation, diagram, and prose-detail crops /
  {sum(int(row['bytes']) for row in recovered_rows):,} image bytes.
"""
        if recovered_rows
        else (
            "- No additional recovered named crop archive was emitted for this "
            "interval because every selected high-detail image was explicitly "
            "named as a targeted zoom or recheck.\n"
        )
    )
    readme = f"""# SGA6 high-detail source-audit crops, cold re-verification indices {args.start_index}-{args.end_index}

This no-overwrite incremental release preserves the high-value source crops
actually generated and read after the prior index-314 snapshot. It does not
turn ordinary reader-page renders into a second copy of the parent PDF.

## Image archives

- `{EXPLICIT_ZIP}` contains {len(explicit_rows)} explicit `zoom`, `zoomp`,
  `peek`, or `recheck` crops / {sum(int(row['bytes']) for row in explicit_rows):,}
  image bytes.
{recovered_archive_text}

Each ZIP includes its exact image manifest plus this README, the parent-source
identity, and the audit-context table. The manifests record image hashes,
dimensions, parent PDF index where recoverable, printed-page evidence from the
audit log where available, generator-script identity, recovered crop
coordinates, render DPI, processing profile, and QA disposition.

`{METADATA_ZIP}` groups the complete public provenance surface, including both
targeted-image manifests and the rights-blocked routine-page manifest. Detailed
files remain individually browsable in the public GitHub package; Zenodo keeps
them compact.

## Deliberate non-image surface

`{BLOCKED_MANIFEST_NAME}` records {len(blocked_rows)} routine whole-page or
page-band derivatives / {sum(int(row['bytes']) for row in blocked_rows):,}
bytes. Their exact hashes and provenance remain public, but their pixels are
not redistributed. These are computationally cheap near-page reconstructions,
carry higher source-redistribution risk, and are not the symbol-level evidence
requested for durable preservation.

## Parent and snapshot

The parent is the 720-page Internet Archive-derived SGA6 reader
`{parent_pdf.name}`, {parent_stat.st_size:,} bytes, SHA-256 `{parent_sha}`.
The parent PDF itself is not bundled. This temporal, no-overwrite image
increment covers files modified after `{start_after.isoformat()}` and closes
at `{cutoff.isoformat()}`, after the cold-reverification pass reached parent
index {args.end_index} and before it began index {args.end_index + 1}. The
recoverable indices span {min(represented_indices) if represented_indices else "unknown"} through
{max(represented_indices) if represented_indices else "unknown"} across
{len(represented_indices)} distinct indices; this is not a claim of continuous
index coverage.

The generator scripts survive only as local operational files and contain
private paths. They are not published. Their SHA-256 identities and recoverable
page/bounding-box/DPI parameters are projected into the manifests.

## Claim and rights boundary

These images are visual/provenance evidence used in source checking. They do
not certify the French transcription, English translation, mathematics,
completeness, or critical-edition status. Underlying French work and scan
rights remain with their holders. No blanket license or rights transfer is
asserted. Reported DPI is output rasterization resolution, not a claim of new
optical detail beyond the parent scan.
"""
    readme_path = output_dir / README_NAME
    write_text_lf(readme_path, readme)

    metadata_paths = [
        readme_path,
        parent_path,
        explicit_manifest,
        recovered_manifest,
        blocked_manifest,
        audit_context,
    ]
    metadata_privacy: dict[str, list[str]] = {}
    for path in metadata_paths:
        hits = privacy_hits([path.read_text(encoding="utf-8", errors="replace")])
        if hits:
            metadata_privacy[path.name] = hits
    if metadata_privacy:
        errors.append(f"generated public metadata privacy hits: {metadata_privacy}")

    explicit_zip_path = zip_dir / EXPLICIT_ZIP
    recovered_zip_path = zip_dir / RECOVERED_ZIP
    metadata_zip_path = zip_dir / METADATA_ZIP
    explicit_zip_result = zip_payload(
        explicit_zip_path,
        explicit_rows,
        scratch_dir,
        [readme_path, parent_path, explicit_manifest, audit_context],
    )
    recovered_zip_result = None
    if recovered_rows:
        recovered_zip_result = zip_payload(
            recovered_zip_path,
            recovered_rows,
            scratch_dir,
            [readme_path, parent_path, recovered_manifest, audit_context],
        )
    metadata_zip_result = zip_payload(
        metadata_zip_path,
        [],
        scratch_dir,
        metadata_paths,
    )
    errors.extend(str(error) for error in explicit_zip_result["errors"])
    if recovered_zip_result:
        errors.extend(str(error) for error in recovered_zip_result["errors"])
    errors.extend(str(error) for error in metadata_zip_result["errors"])

    race_errors: list[str] = []
    manifest_by_source = {
        str(row["source_basename"]): row for row in manifest_rows
    }
    for association in associations:
        image = association["image"]
        row = manifest_by_source.get(image.name)
        if row is None:
            race_errors.append(f"missing manifest row during race recheck: {image.name}")
            continue
        stat = image.stat()
        if stat.st_size != association["initial_size"]:
            race_errors.append(f"size changed during freeze: {image.name}")
            continue
        if stat.st_mtime_ns != association["initial_mtime_ns"]:
            race_errors.append(f"mtime changed during freeze: {image.name}")
            continue
        if sha256(image) != row["sha256"]:
            race_errors.append(f"hash changed during freeze: {image.name}")
    errors.extend(race_errors)

    validation = {
        "schema": "sga6_high_detail_source_audit_crop_release_validation_v3",
        "image_snapshot_start_after_utc": start_after.isoformat(),
        "image_snapshot_cutoff_utc": cutoff.isoformat(),
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "source_selection": {
            "associated_parent_images": len(manifest_rows),
            "associated_parent_bytes": sum(
                int(row["bytes"]) for row in manifest_rows
            ),
            "association_window_seconds": args.association_window_seconds,
            "target_generator_scripts": len(
                {
                    str(row["generator_script_basename"])
                    for row in manifest_rows
                }
            ),
            "explicit_targeted": {
                "files": len(explicit_rows),
                "bytes": sum(int(row["bytes"]) for row in explicit_rows),
                "manifest_sha256": sha256(explicit_manifest),
            },
            "recovered_named_targeted": {
                "files": len(recovered_rows),
                "bytes": sum(int(row["bytes"]) for row in recovered_rows),
                "manifest_sha256": sha256(recovered_manifest),
            },
            "routine_page_derivatives_rights_blocked": {
                "files": len(blocked_rows),
                "bytes": sum(int(row["bytes"]) for row in blocked_rows),
                "manifest_sha256": sha256(blocked_manifest),
            },
        },
        "parent_source": parent_identity,
        "audit_context": {
            "rows": len(audit_rows),
            "represented_parent_indices": len(represented_indices),
            "sha256": sha256(audit_context),
            "cert_log_sha256_at_packaging_snapshot": cert_sha,
        },
        "png_validation": {
            "validated_files": len(manifest_rows),
            "invalid_files": sum(
                1 for error in errors if error.startswith("invalid PNG")
            ),
            "privacy_hits": png_privacy,
            "duplicate_content_groups": duplicate_groups,
        },
        "generated_metadata_privacy": {
            "files_scanned": len(metadata_paths),
            "hits": metadata_privacy,
        },
        "freeze_race_recheck": {
            "files": len(manifest_rows),
            "errors": race_errors,
        },
        "zip_validation": {
            EXPLICIT_ZIP: explicit_zip_result,
            METADATA_ZIP: metadata_zip_result,
            **(
                {RECOVERED_ZIP: recovered_zip_result}
                if recovered_zip_result
                else {}
            ),
        },
    }
    validation_path = output_dir / VALIDATION_NAME
    write_text_lf(
        validation_path,
        json.dumps(validation, indent=2, ensure_ascii=True) + "\n",
    )

    upload_paths = [
        explicit_zip_path,
        metadata_zip_path,
    ]
    if recovered_zip_result:
        upload_paths.insert(1, recovered_zip_path)
    upload_rows = []
    for path in upload_paths:
        upload_rows.append(
            {
                "filename": path.name,
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
                "role": (
                    "targeted_image_archive"
                    if path.suffix.lower() == ".zip"
                    else "public_metadata"
                ),
                "status": "proposed_public",
            }
        )
    upload_manifest = output_dir / UPLOAD_MANIFEST_NAME
    write_csv(
        upload_manifest,
        upload_rows,
        ["filename", "bytes", "sha256", "role", "status"],
    )
    checksum_paths = upload_paths + [upload_manifest]
    checksum_path = output_dir / SHA_NAME
    write_text_lf(
        checksum_path,
        "\n".join(
            f"{sha256(path)}  {path.name}"
            for path in sorted(checksum_paths, key=lambda item: item.name)
        )
        + "\n",
    )

    summary = {
        "status": validation["status"],
        "associated_images": len(manifest_rows),
        "explicit_targeted": len(explicit_rows),
        "recovered_named_targeted": len(recovered_rows),
        "rights_blocked_page_derivatives": len(blocked_rows),
        "explicit_zip": explicit_zip_result,
        "recovered_zip": recovered_zip_result,
        "metadata_zip": metadata_zip_result,
        "upload_manifest_sha256": sha256(upload_manifest),
        "sha256sums_sha256": sha256(checksum_path),
        "validation_sha256": sha256(validation_path),
    }
    print(json.dumps(summary, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
