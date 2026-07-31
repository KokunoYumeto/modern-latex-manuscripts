#!/usr/bin/env python3
"""Package current SGA7 II source-image witnesses without copying other projects."""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import json
import re
import sys
import zipfile
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image


Image.MAX_IMAGE_PIXELS = None
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".webp"}
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
class ImageInstance:
    root_id: str
    root_priority: int
    path: Path
    relative_path: str
    generator: object | None
    generator_match: str
    selection_reason: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--parent-pdf", type=Path, required=True)
    parser.add_argument(
        "--root",
        action="append",
        required=True,
        help="PUBLIC_LABEL=absolute scratchpad path; repeat in preference order",
    )
    parser.add_argument(
        "--cutoff",
        action="append",
        required=True,
        help="PUBLIC_LABEL=local ISO timestamp",
    )
    parser.add_argument("--metadata-dir", type=Path, required=True)
    parser.add_argument("--zip-path", type=Path, required=True)
    return parser.parse_args()


def parse_key_values(values: list[str]) -> dict[str, str]:
    result: dict[str, str] = {}
    for value in values:
        key, separator, item = value.partition("=")
        if not separator or not key or not item:
            raise ValueError(f"Expected KEY=VALUE, got {value!r}")
        if key in result:
            raise ValueError(f"Duplicate key: {key}")
        result[key] = item
    return result


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def load_inventory_helpers() -> object:
    source = Path(__file__).with_name("build_sga7_visual_evidence_inventory.py")
    spec = importlib.util.spec_from_file_location("sga7_visual_helpers", source)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {source}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def csv_write(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def json_write(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=True, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def safe_name(name: str) -> str:
    value = re.sub(r"[^A-Za-z0-9._-]+", "_", name).strip("._")
    return value or "image.png"


def infer_page(name: str, generator: object | None, helpers: object) -> tuple[int | None, str]:
    stem = Path(name).stem
    patterns = (
        (r"(?i)(?:^|[_-])idx[_-]?(\d{1,3})(?:[_-]|$)", "explicit_idx_filename"),
        (r"(?i)(?:^|[_-])(?:page|pg|p|q|r|n|m|c|d|z|t|tc|zz)[_-]?(\d{1,3})(?:[_-]|$)", "explicit_page_filename"),
        (r"(?i)^crop[_-]?(\d{1,3})(?:[_-]|$)", "explicit_crop_page_filename"),
    )
    for pattern, method in patterns:
        match = re.search(pattern, stem)
        if match and 0 <= int(match.group(1)) < 446:
            return int(match.group(1)), method
    if generator is not None:
        job = helpers.match_job(name, generator)
        if job is not None and job.page_index is not None and job.page_index < 446:
            return job.page_index, "generator_job"
        candidates = sorted(value for value in generator.page_candidates if value < 446)
        if len(candidates) == 1:
            return candidates[0], "single_generator_page"
    numbers = [
        int(value)
        for value in re.findall(r"(?<!\d)(\d{1,3})(?!\d)", stem)
        if 8 <= int(value) < 446
    ]
    if numbers:
        return numbers[0], "numeric_filename_inference"
    return None, "unresolved"


def scope_for_page(page_index: int | None) -> str:
    if page_index is None:
        return "unresolved"
    scopes = (
        (8, 45, "X"),
        (46, 68, "XI"),
        (69, 89, "XII"),
        (90, 122, "XIII"),
        (123, 171, "XIV"),
        (172, 203, "XV"),
        (204, 218, "XVI"),
    )
    for first, last, label in scopes:
        if first <= page_index <= last:
            return label
    if 219 <= page_index < 348:
        return "XVII-XIX_boundary_unresolved"
    if 348 <= page_index < 370:
        return "XX"
    if 370 <= page_index < 446:
        return "XXI-XXII_boundary_unresolved"
    return "front_matter_or_unmapped"


def build_selection(args: argparse.Namespace, helpers: object) -> tuple[list[ImageInstance], list[object]]:
    roots = parse_key_values(args.root)
    cutoffs = parse_key_values(args.cutoff)
    if set(roots) != set(cutoffs):
        raise ValueError("Each root requires exactly one cutoff")
    specs = []
    for priority, (root_id, value) in enumerate(roots.items()):
        path = Path(value).resolve()
        if not path.is_dir():
            raise FileNotFoundError(path)
        cutoff = datetime.fromisoformat(cutoffs[root_id]).timestamp()
        specs.append(helpers.RootSpec(root_id, path, cutoff, priority))

    scripts = []
    for root in specs:
        scripts.extend(
            helpers.script_info(root, path, args.parent_pdf.name)
            for path in root.path.rglob("*.py")
            if helpers.selected(path, root.cutoff)
        )

    candidates: list[tuple[object, Path, object | None, str]] = []
    for root in specs:
        for path in root.path.rglob("*"):
            if (
                path.is_file()
                and path.suffix.lower() in IMAGE_SUFFIXES
                and helpers.selected(path, root.cutoff)
            ):
                generator, method = helpers.match_generator(
                    path.name, path.stat().st_mtime, scripts, root.root_id
                )
                candidates.append((root, path, generator, method))

    selected: set[tuple[str, str]] = set()
    reasons: dict[tuple[str, str], str] = {}
    for root, path, generator, _ in candidates:
        if generator is not None and generator.source_class == "controlling_540_page_scan":
            key = (root.root_id, path.relative_to(root.path).as_posix().casefold())
            selected.add(key)
            reasons[key] = "direct_Number12_generator"

    changed = True
    while changed:
        changed = False
        selected_names = {Path(relative).name for _, relative in selected}
        selected_scripts: set[tuple[str, str]] = set()
        for script in scripts:
            if script.source_class == "controlling_540_page_scan":
                selected_scripts.add((script.root_id, str(script.path)))
                continue
            text = script.path.read_text(encoding="utf-8", errors="replace").casefold()
            if any(name in text for name in selected_names):
                selected_scripts.add((script.root_id, str(script.path)))
        for root, path, generator, _ in candidates:
            relative = path.relative_to(root.path).as_posix()
            key = (root.root_id, relative.casefold())
            if key in selected or generator is None:
                continue
            if (generator.root_id, str(generator.path)) in selected_scripts:
                selected.add(key)
                reasons[key] = "downstream_crop_of_Number12_image"
                changed = True

    result = []
    for root, path, generator, method in candidates:
        relative = path.relative_to(root.path).as_posix()
        key = (root.root_id, relative.casefold())
        if key in selected:
            result.append(
                ImageInstance(
                    root.root_id,
                    root.priority,
                    path,
                    relative,
                    generator,
                    method,
                    reasons[key],
                )
            )
    return result, scripts


def main() -> None:
    args = parse_args()
    parent = args.parent_pdf.resolve()
    if not parent.is_file():
        raise FileNotFoundError(parent)
    helpers = load_inventory_helpers()
    instances, scripts = build_selection(args, helpers)
    if not instances:
        raise RuntimeError("No Number12-derived images selected")

    initial = {
        item.path: (item.path.stat().st_size, item.path.stat().st_mtime_ns)
        for item in instances
    }
    rows = []
    by_hash: dict[str, list[dict[str, object]]] = defaultdict(list)
    digest_paths: dict[str, Path] = {}
    for item in instances:
        stat = item.path.stat()
        digest = sha256(item.path)
        digest_paths.setdefault(digest, item.path)
        with Image.open(item.path) as image:
            width, height = image.size
            mode = image.mode
            image_format = image.format or item.path.suffix.lstrip(".").upper()
        page_index, page_method = infer_page(item.path.name, item.generator, helpers)
        generator_sha = item.generator.sha256 if item.generator is not None else ""
        generator_name = item.generator.path.name if item.generator is not None else ""
        row: dict[str, object] = {
            "root_label": item.root_id,
            "original_name": item.path.name,
            "relative_name": item.relative_path,
            "bytes": stat.st_size,
            "sha256": digest,
            "width_px": width,
            "height_px": height,
            "mode": mode,
            "format": image_format,
            "modified_local": datetime.fromtimestamp(stat.st_mtime).isoformat(timespec="seconds"),
            "source_pdf_index_0based": "" if page_index is None else page_index,
            "physical_pdf_page_1based": "" if page_index is None else page_index + 1,
            "book_folio": "" if page_index is None else page_index - 7,
            "expose_scope": scope_for_page(page_index),
            "page_inference": page_method,
            "selection_reason": item.selection_reason,
            "generator_name": generator_name,
            "generator_sha256": generator_sha,
            "generator_match": item.generator_match,
            "archive_member": "",
            "canonical": 0,
        }
        rows.append(row)
        by_hash[digest].append(row)

    canonical_rows = []
    alias_rows = []
    for digest, members in sorted(by_hash.items()):
        members.sort(
            key=lambda row: (
                str(row["root_label"]),
                str(row["relative_name"]).casefold(),
            )
        )
        canonical = members[0]
        canonical_rows.append(canonical)
        for alias in members[1:]:
            alias_rows.append(
                {
                    "sha256": digest,
                    "canonical_original_name": canonical["original_name"],
                    "alias_original_name": alias["original_name"],
                    "alias_root_label": alias["root_label"],
                    "alias_relative_name": alias["relative_name"],
                    "bytes": alias["bytes"],
                }
            )
    canonical_rows.sort(
        key=lambda row: (
            row["source_pdf_index_0based"] == "",
            int(row["source_pdf_index_0based"] or 9999),
            str(row["original_name"]).casefold(),
            str(row["sha256"]),
        )
    )
    for index, row in enumerate(canonical_rows, start=1):
        visual_id = f"SGA7II-VIS-{index:05d}"
        row["visual_id"] = visual_id
        row["canonical"] = 1
        row["archive_member"] = f"images/{visual_id}_{safe_name(str(row['original_name']))}"
    canonical_by_hash = {str(row["sha256"]): row for row in canonical_rows}
    for row in rows:
        canonical = canonical_by_hash[str(row["sha256"])]
        row["visual_id"] = canonical["visual_id"]
        row["archive_member"] = canonical["archive_member"]

    fields = [
        "visual_id",
        "root_label",
        "original_name",
        "relative_name",
        "bytes",
        "sha256",
        "width_px",
        "height_px",
        "mode",
        "format",
        "modified_local",
        "source_pdf_index_0based",
        "physical_pdf_page_1based",
        "book_folio",
        "expose_scope",
        "page_inference",
        "selection_reason",
        "generator_name",
        "generator_sha256",
        "generator_match",
        "archive_member",
        "canonical",
    ]
    metadata = args.metadata_dir.resolve()
    metadata.mkdir(parents=True, exist_ok=True)
    index_path = metadata / "SGA7II_SOURCE_IMAGE_WITNESS_INDEX.csv"
    aliases_path = metadata / "SGA7II_SOURCE_IMAGE_DUPLICATE_ALIASES.csv"
    csv_write(index_path, rows, fields)
    csv_write(
        aliases_path,
        alias_rows,
        [
            "sha256",
            "canonical_original_name",
            "alias_original_name",
            "alias_root_label",
            "alias_relative_name",
            "bytes",
        ],
    )

    parent_sha = sha256(parent)
    page_counts = Counter(str(row["source_pdf_index_0based"]) for row in canonical_rows)
    scope_counts = Counter(str(row["expose_scope"]) for row in canonical_rows)
    unresolved = sum(row["source_pdf_index_0based"] == "" for row in canonical_rows)
    readme = metadata / "README.md"
    readme.write_text(
        "# SGA 7 II source-image witnesses\n\n"
        "This archive contains the actual source-page renders and high-detail crops generated "
        "from the publicly available SGA 7 II scan during the current transcription pass. "
        "It does not contain screenshots of the reconstructed reader.\n\n"
        f"- parent scan: 446 pages / {parent.stat().st_size:,} bytes / SHA-256 `{parent_sha}`;\n"
        f"- selected image instances: {len(rows):,};\n"
        f"- deduplicated image members: {len(canonical_rows):,};\n"
        f"- duplicate aliases omitted from the ZIP: {len(alias_rows):,};\n"
        f"- page-resolved canonical images: {len(canonical_rows) - unresolved:,};\n"
        f"- unresolved-page canonical images: {unresolved:,}.\n\n"
        "The index records exact bytes, SHA-256, dimensions, source-PDF page and folio where "
        "recoverable, Expose scope, and generator identity. Page assignments marked inferred "
        "should be checked against the parent scan before citation. Generated images can exceed "
        "the parent scan's optical resolution; enlargement does not create new source detail.\n",
        encoding="utf-8",
        newline="\n",
    )

    zip_path = args.zip_path.resolve()
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    source_lookup = {str(row["sha256"]): digest_paths[str(row["sha256"])] for row in canonical_rows}
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        for path in (readme, index_path, aliases_path):
            archive.write(path, path.name)
        for row in canonical_rows:
            archive.write(source_lookup[str(row["sha256"])], str(row["archive_member"]))

    archive_errors = []
    with zipfile.ZipFile(zip_path) as archive:
        bad = archive.testzip()
        if bad:
            archive_errors.append(f"bad_crc:{bad}")
        names = archive.namelist()
        expected = 3 + len(canonical_rows)
        if len(names) != expected:
            archive_errors.append(f"member_count:{len(names)}!={expected}")
        if len(names) != len(set(names)):
            archive_errors.append("duplicate_member_names")
        for row in canonical_rows:
            data = archive.read(str(row["archive_member"]))
            digest = hashlib.sha256(data).hexdigest().upper()
            if digest != row["sha256"]:
                archive_errors.append(f"member_hash:{row['archive_member']}")

    metadata_text = "\n".join(
        path.read_text(encoding="utf-8", errors="replace")
        for path in (readme, index_path, aliases_path)
    ).casefold()
    privacy_hits = [marker for marker in PRIVATE_MARKERS if marker in metadata_text]
    post_mutations = []
    for path, identity in initial.items():
        stat = path.stat()
        if (stat.st_size, stat.st_mtime_ns) != identity:
            post_mutations.append(str(path.name))

    validation = {
        "status": "PASS" if not archive_errors and not privacy_hits and not post_mutations else "FAIL",
        "errors": archive_errors,
        "parent_pdf": {
            "pages": 446,
            "bytes": parent.stat().st_size,
            "sha256": parent_sha,
            "included": False,
        },
        "cutoff": parse_key_values(args.cutoff),
        "selected_instances": len(rows),
        "selected_instance_bytes": sum(int(row["bytes"]) for row in rows),
        "canonical_images": len(canonical_rows),
        "canonical_image_bytes": sum(int(row["bytes"]) for row in canonical_rows),
        "duplicate_aliases": len(alias_rows),
        "page_resolved_canonical_images": len(canonical_rows) - unresolved,
        "page_unresolved_canonical_images": unresolved,
        "scope_counts": dict(sorted(scope_counts.items())),
        "source_page_counts": dict(sorted(page_counts.items())),
        "generator_scripts_considered": len(scripts),
        "privacy_hits": privacy_hits,
        "source_mutations_during_build": post_mutations,
        "zip": {
            "path_name": zip_path.name,
            "bytes": zip_path.stat().st_size,
            "sha256": sha256(zip_path),
            "members": 3 + len(canonical_rows),
        },
        "generated_utc": datetime.now(timezone.utc).isoformat(),
    }
    validation_path = metadata / "SGA7II_SOURCE_IMAGE_WITNESS_VALIDATION.json"
    json_write(validation_path, validation)
    if validation["status"] != "PASS":
        raise RuntimeError(json.dumps(validation, indent=2))
    print(json.dumps(validation, indent=2))


if __name__ == "__main__":
    main()
