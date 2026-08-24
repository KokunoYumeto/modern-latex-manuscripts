#!/usr/bin/env python3
"""Render the frozen D038 PDFs and prepare all-page visual audit sheets."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import pathlib
import subprocess

from PIL import Image, ImageDraw, ImageFont


PDFS = {
    "source": "D038_SOURCE_LANGUAGE_CANONICAL.pdf",
    "english": "D038_ENGLISH_CANONICAL.pdf",
    "apparatus": "D038_RESTRAINED_APPARATUS.pdf",
}
GROUPS = ((1, 16), (17, 32), (33, 48), (49, 58))


def sha256(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def contact_sheet(paths: list[pathlib.Path], labels: list[str], output: pathlib.Path) -> None:
    cell_w, cell_h, label_h = 320, 476, 28
    sheet = Image.new("RGB", (cell_w * 4, (cell_h + label_h) * 4), "white")
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 18)
    for index, (path, label) in enumerate(zip(paths, labels)):
        image = Image.open(path).convert("RGB")
        image.thumbnail((cell_w - 8, cell_h - 8), Image.Resampling.LANCZOS)
        col, row = index % 4, index // 4
        x = col * cell_w + (cell_w - image.width) // 2
        y = row * (cell_h + label_h) + label_h
        sheet.paste(image, (x, y))
        draw.text((col * cell_w + 8, row * (cell_h + label_h) + 4), label, fill="black", font=font)
        draw.rectangle((col * cell_w, row * (cell_h + label_h), (col + 1) * cell_w - 1, (row + 1) * (cell_h + label_h) - 1), outline="#a0a0a0")
    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output, optimize=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True, type=pathlib.Path)
    args = parser.parse_args()
    root = args.root.resolve()
    freeze = json.loads((root / "manifests/FREEZE_RECEIPT.json").read_text(encoding="utf-8"))
    require(freeze["status"] == "FROZEN", "candidate has no valid freeze receipt")
    tag = freeze["candidate_aggregate_sha256"][:8]
    render_root = root / "rendered" / f"frozen_{tag}"
    render_root.mkdir(parents=True, exist_ok=True)
    metrics: list[dict[str, object]] = []

    for layer, name in PDFS.items():
        out_dir = render_root / layer
        out_dir.mkdir(parents=True, exist_ok=True)
        prefix = out_dir / "page"
        result = subprocess.run(
            ["pdftoppm", "-png", "-r", "144", str(root / "candidate" / name), str(prefix)],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
        require(result.returncode == 0, f"pdftoppm failed for {name}: {result.stdout}")
        pages = sorted(out_dir.glob("page-*.png"))
        require(len(pages) == 58, f"render count mismatch for {layer}: {len(pages)}")
        for page, path in enumerate(pages, 1):
            with Image.open(path) as image:
                require(image.size == (922, 1368), f"render geometry mismatch {layer} p{page}: {image.size}")
                gray = image.convert("L")
                mask = gray.point(lambda value: 255 if value < 245 else 0)
                bbox = mask.getbbox()
                require(bbox is not None, f"blank render {layer} p{page}")
                histogram = gray.histogram()
                dark = sum(histogram[:245])
                ratio = dark / (image.width * image.height)
                require(0.002 < ratio < 0.40, f"implausible ink ratio {layer} p{page}: {ratio}")
                require(bbox[0] >= 20 and bbox[1] >= 20 and bbox[2] <= image.width - 20 and bbox[3] <= image.height - 20,
                        f"content touches safety margin {layer} p{page}: {bbox}")
                metrics.append({
                    "layer": layer,
                    "physical_page": page,
                    "render_path": path.relative_to(root).as_posix(),
                    "width_px": image.width,
                    "height_px": image.height,
                    "ink_ratio": f"{ratio:.8f}",
                    "ink_bbox": ",".join(map(str, bbox)),
                    "sha256": sha256(path),
                    "programmatic_visual_status": "PASS",
                })

    contact_rows = []
    for layer in (*PDFS.keys(), "authority"):
        if layer == "authority":
            pages = [root / "candidate/assets/authority_pages" / f"p{page:03d}.png" for page in range(1, 59)]
        else:
            pages = sorted((render_root / layer).glob("page-*.png"))
        for first, last in GROUPS:
            selected = pages[first - 1:last]
            labels = [f"{layer.upper()} physical {page:02d} / printed {page + 79}" for page in range(first, last + 1)]
            output = render_root / "contacts" / f"{layer.upper()}_{first:03d}_{last:03d}.png"
            contact_sheet(selected, labels, output)
            contact_rows.append({
                "layer": layer,
                "physical_pages": f"{first:03d}-{last:03d}",
                "path": output.relative_to(root).as_posix(),
                "bytes": output.stat().st_size,
                "sha256": sha256(output),
            })

    audit = root / "audit"
    audit.mkdir(parents=True, exist_ok=True)
    metrics_path = audit / "RENDER_PAGE_METRICS.tsv"
    with metrics_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=tuple(metrics[0]), delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(metrics)
    contacts_path = audit / "CONTACT_SHEET_INVENTORY.tsv"
    with contacts_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=tuple(contact_rows[0]), delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(contact_rows)
    receipt = {
        "schema": "d038-render-qa-v1",
        "status": "PASS_PROGRAMMATIC_PENDING_INDEPENDENT_VISUAL_INSPECTION",
        "frozen_candidate_aggregate_sha256": freeze["candidate_aggregate_sha256"],
        "render_engine": "pdftoppm",
        "render_dpi": 144,
        "reader_pages_rendered": len(metrics),
        "authority_fallback_pages_in_contacts": 58,
        "contact_sheets": len(contact_rows),
        "page_metrics": {"path": metrics_path.relative_to(root).as_posix(), "sha256": sha256(metrics_path)},
        "contact_inventory": {"path": contacts_path.relative_to(root).as_posix(), "sha256": sha256(contacts_path)},
    }
    receipt_path = audit / "RENDER_QA_PROGRAMMATIC.json"
    receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print("PASS_RENDER_PROGRAMMATIC", render_root)


if __name__ == "__main__":
    main()
