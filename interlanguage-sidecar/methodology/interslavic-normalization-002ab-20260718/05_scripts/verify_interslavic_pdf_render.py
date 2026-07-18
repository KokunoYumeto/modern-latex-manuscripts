#!/usr/bin/env python3
"""Render and visually index an Interslavic tranche without parallelism."""

from __future__ import annotations

import argparse
import json
import math
import os
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path

from PIL import Image, ImageDraw, ImageOps, ImageStat


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = (
    ROOT
    / "03_projects"
    / "language_management"
    / "slavic_interslavic"
    / "normalization_20260718"
    / "tranche_002a_orthography"
)
EVIDENCE = WORKSPACE / "evidence"
BUILD_REPORT = EVIDENCE / "BUILD_REPORT.json"
OUTPUT = WORKSPACE / "visual_qa"
THUMBS = OUTPUT / "thumbnails"
SAMPLES = OUTPUT / "samples_96dpi"
CONTACTS = OUTPUT / "contact_sheets"
MASTERS = OUTPUT / "master_sheets"
REPORT = EVIDENCE / "RENDER_QA_REPORT.json"
TEMP_PARENT = ROOT / "tmp" / "pdfs"

def renderer_command(renderer: str, arguments: list[str]) -> list[str]:
    if os.name == "nt" and Path(renderer).suffix.lower() in {".cmd", ".bat"}:
        return [os.environ.get("COMSPEC", "cmd.exe"), "/d", "/c", renderer, *arguments]
    return [renderer, *arguments]


def page_number(path: Path) -> int:
    return int(path.stem.rsplit("-", 1)[1])


def analyze_page(path: Path) -> dict[str, object]:
    with Image.open(path) as image:
        image.load()
        width, height = image.size
        grayscale = ImageOps.grayscale(image)
        histogram = grayscale.histogram()
        pixels = width * height
        nonwhite = sum(histogram[:245])
        nonwhite_fraction = nonwhite / pixels
        mean_grayscale = ImageStat.Stat(grayscale).mean[0]
        ink_mask = grayscale.point(lambda value: 255 if value < 245 else 0)
        bbox = ink_mask.getbbox()
        edge_touch = bool(
            bbox
            and (bbox[0] <= 0 or bbox[1] <= 0 or bbox[2] >= width or bbox[3] >= height)
        )
        return {
            "width": width,
            "height": height,
            "nonwhite_fraction": round(nonwhite_fraction, 6),
            "mean_grayscale": round(mean_grayscale, 3),
            "ink_bbox": list(bbox) if bbox else None,
            "blank_flag": bbox is None or nonwhite_fraction < 0.001,
            "dark_page_flag": mean_grayscale < 150,
            "edge_touch_flag": edge_touch,
        }


def make_thumbnail(page_png: Path, destination: Path, label: str, width: int = 220) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(page_png) as image:
        image = image.convert("RGB")
        height = round(image.height * width / image.width)
        image.thumbnail((width, height), Image.Resampling.LANCZOS)
        canvas = Image.new("RGB", (width, height + 26), "white")
        canvas.paste(image, (0, 26))
        ImageDraw.Draw(canvas).text((4, 6), label[:52], fill="black")
        canvas.save(destination, "PNG", optimize=True)


def combine_images(
    images: list[Path], destination: Path, columns: int, cell_width: int, cell_height: int
) -> None:
    rows = math.ceil(len(images) / columns)
    canvas = Image.new("RGB", (columns * cell_width, rows * cell_height), "white")
    for index, path in enumerate(images):
        with Image.open(path) as image:
            image = image.convert("RGB")
            image.thumbnail((cell_width, cell_height), Image.Resampling.LANCZOS)
            x = (index % columns) * cell_width + (cell_width - image.width) // 2
            y = (index // columns) * cell_height + (cell_height - image.height) // 2
            canvas.paste(image, (x, y))
    destination.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(destination, "PNG", optimize=True)


def sample_page_numbers(pages: int, all_pages: bool) -> set[int]:
    if all_pages:
        return set(range(1, pages + 1))
    return {1, max(1, math.ceil(pages / 2)), pages}


def result_source_path(result: dict[str, object]) -> str:
    return str(result.get("path") or result.get("source") or "").replace("\\", "/").lower()


def stratified_sample_indices(results: list[dict[str, object]]) -> set[int]:
    """Choose bounded coverage across the ordered tranche without fixed-size assumptions."""
    count = len(results)
    if not count:
        return set()
    target = min(15, count)
    if target == 1:
        chosen = {1}
    else:
        chosen = {
            1 + round(position * (count - 1) / (target - 1))
            for position in range(target)
        }
    for index, result in enumerate(results, start=1):
        source = result_source_path(result)
        if "paper35/source_fidelity/interslavic-cyrillic" in source:
            chosen.add(index)
    return chosen


def main() -> int:
    global WORKSPACE, EVIDENCE, BUILD_REPORT, OUTPUT, THUMBS, SAMPLES
    global CONTACTS, MASTERS, REPORT, TEMP_PARENT

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--workspace",
        type=Path,
        default=WORKSPACE,
        help="Tranche workspace containing evidence/BUILD_REPORT.json",
    )
    args = parser.parse_args()
    WORKSPACE = args.workspace.resolve()
    EVIDENCE = WORKSPACE / "evidence"
    BUILD_REPORT = EVIDENCE / "BUILD_REPORT.json"
    OUTPUT = WORKSPACE / "visual_qa"
    THUMBS = OUTPUT / "thumbnails"
    SAMPLES = OUTPUT / "samples_96dpi"
    CONTACTS = OUTPUT / "contact_sheets"
    MASTERS = OUTPUT / "master_sheets"
    REPORT = EVIDENCE / "RENDER_QA_REPORT.json"
    TEMP_PARENT = ROOT / "tmp" / "pdfs"

    bundled_renderer = (
        Path.home()
        / ".cache"
        / "codex-runtimes"
        / "codex-primary-runtime"
        / "dependencies"
        / "native"
        / "poppler"
        / "Library"
        / "bin"
        / "pdftoppm.exe"
    )
    renderer = str(bundled_renderer) if bundled_renderer.is_file() else shutil.which("pdftoppm")
    if not renderer:
        raise RuntimeError("pdftoppm is required for visual verification")
    build = json.loads(BUILD_REPORT.read_text(encoding="utf-8"))
    results = build["results"]
    expected_count = len(results)
    if build["successful_files"] != expected_count or build["failed_files"]:
        raise RuntimeError(
            f"Build report is not at its mandatory {expected_count}/{expected_count} pass gate"
        )
    sample_indices = stratified_sample_indices(results)

    for directory in (THUMBS, SAMPLES, CONTACTS, MASTERS, TEMP_PARENT):
        directory.mkdir(parents=True, exist_ok=True)

    page_rows: list[dict[str, object]] = []
    thumbnail_paths: list[Path] = []
    sample_paths: list[Path] = []
    with tempfile.TemporaryDirectory(prefix="interslavic-render-", dir=TEMP_PARENT) as temp_name:
        temp_root = Path(temp_name)
        for pdf_index, result in enumerate(results, start=1):
            pdf = Path(str(result["pdf"]))
            unit_temp = temp_root / f"u{pdf_index:03d}"
            unit_temp.mkdir()
            # Poppler on Windows still fails to open some deeply nested paths.
            # Render an exact temporary copy from a deliberately short name.
            short_pdf = unit_temp / "input.pdf"
            shutil.copy2(pdf, short_pdf)
            prefix = unit_temp / "page"
            command = renderer_command(
                renderer,
                ["-png", "-r", "96", str(short_pdf), str(prefix)],
            )
            completed = subprocess.run(
                command,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=180,
                check=False,
            )
            if completed.returncode:
                raise RuntimeError(
                    f"pdftoppm failed for {pdf}: {completed.stderr[-1000:]}"
                )
            rendered = sorted(unit_temp.glob("page-*.png"), key=page_number)
            expected_pages = int(result["pages"])
            if len(rendered) != expected_pages:
                raise RuntimeError(
                    f"Rendered page mismatch for {pdf}: expected {expected_pages}, found {len(rendered)}"
                )

            source = result_source_path(result)
            is_paper35_cyrillic = "paper35/source_fidelity/interslavic-cyrillic" in source
            chosen = sample_page_numbers(expected_pages, is_paper35_cyrillic)
            for page_png in rendered:
                number = page_number(page_png)
                metrics = analyze_page(page_png)
                label = f"{pdf_index:03d} p{number:02d} {result['script'][0]} {pdf.stem}"
                thumb = THUMBS / f"u{pdf_index:03d}_p{number:02d}.png"
                make_thumbnail(page_png, thumb, label)
                thumbnail_paths.append(thumb)
                sample = None
                if pdf_index in sample_indices and number in chosen:
                    sample = SAMPLES / f"u{pdf_index:03d}_p{number:02d}_{pdf.stem}.png"
                    shutil.copy2(page_png, sample)
                    sample_paths.append(sample)
                page_rows.append(
                    {
                        "unit_index": pdf_index,
                        "page": number,
                        "script": result["script"],
                        "pdf": str(pdf),
                        "thumbnail": str(thumb),
                        "sample": str(sample) if sample else None,
                        **metrics,
                    }
                )
            print(
                f"[{pdf_index:03d}/{expected_count:03d}] RENDER-PASS {result['script']} "
                f"pages={expected_pages} {pdf.name}",
                flush=True,
            )

    contact_paths: list[Path] = []
    for start in range(0, len(thumbnail_paths), 24):
        group = thumbnail_paths[start : start + 24]
        contact = CONTACTS / f"contact_{start // 24 + 1:02d}.png"
        combine_images(group, contact, columns=4, cell_width=220, cell_height=338)
        contact_paths.append(contact)

    master_paths: list[Path] = []
    for start in range(0, len(contact_paths), 4):
        group = contact_paths[start : start + 4]
        master = MASTERS / f"master_{start // 4 + 1:02d}.png"
        combine_images(group, master, columns=2, cell_width=880, cell_height=2028)
        master_paths.append(master)

    sample_contact_paths: list[Path] = []
    for start in range(0, len(sample_paths), 6):
        group = sample_paths[start : start + 6]
        contact = CONTACTS / f"samples_{start // 6 + 1:02d}.png"
        combine_images(group, contact, columns=2, cell_width=520, cell_height=736)
        sample_contact_paths.append(contact)

    flags = [
        row
        for row in page_rows
        if row["blank_flag"] or row["dark_page_flag"] or row["edge_touch_flag"]
    ]
    report = {
        "schema": "interslavic-render-qa-v1",
        "generated_at": datetime.now().astimezone().isoformat(),
        "renderer": renderer,
        "policy": {
            "dpi": 96,
            "parallel_renderers": 1,
            "temporary_render_scope": "one PDF at a time; automatically removed",
            "visual_index": "all rendered pages represented in master sheets",
            "high_resolution_sample": "stratified first/middle/last pages plus all repaired Paper 35 Cyrillic pages",
        },
        "pdfs_rendered": len(results),
        "pages_rendered": len(page_rows),
        "expected_pages": build["total_pages"],
        "thumbnails": len(thumbnail_paths),
        "contact_sheets": [str(path) for path in contact_paths],
        "master_sheets": [str(path) for path in master_paths],
        "sample_images": [str(path) for path in sample_paths],
        "sample_contact_sheets": [str(path) for path in sample_contact_paths],
        "machine_flags": flags,
        "machine_pass": not flags and len(page_rows) == build["total_pages"],
        "page_metrics": page_rows,
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "pdfs_rendered": report["pdfs_rendered"],
                "pages_rendered": report["pages_rendered"],
                "machine_flags": len(flags),
                "machine_pass": report["machine_pass"],
                "master_sheets": len(master_paths),
                "sample_contact_sheets": len(sample_contact_paths),
            },
            indent=2,
        ),
        flush=True,
    )
    print(f"wrote {REPORT}", flush=True)
    return 0 if report["machine_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
