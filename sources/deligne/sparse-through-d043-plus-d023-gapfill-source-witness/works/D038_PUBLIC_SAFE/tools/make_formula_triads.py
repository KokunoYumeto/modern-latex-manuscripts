#!/usr/bin/env python3
"""Make authority/source/English triads for formula-dense D038 pages."""

from __future__ import annotations

import argparse
import json
import pathlib

from PIL import Image, ImageDraw, ImageFont


PAGES = (2, 5, 6, 7, 8, 11, 14, 20, 21, 22, 25, 31, 36, 39, 42, 44, 45, 46, 49, 53, 54, 55, 56, 57, 58)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True, type=pathlib.Path)
    args = parser.parse_args()
    root = args.root.resolve()
    freeze = json.loads((root / "manifests/FREEZE_RECEIPT.json").read_text(encoding="utf-8"))
    render = root / "rendered" / f"frozen_{freeze['candidate_aggregate_sha256'][:8]}"
    out_dir = render / "formula_triads"
    out_dir.mkdir(parents=True, exist_ok=True)
    font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 18)
    cell_w, cell_h, label_h = 450, 668, 28
    for group_index in range(0, len(PAGES), 2):
        pages = PAGES[group_index:group_index + 2]
        sheet = Image.new("RGB", (cell_w * 3, (cell_h + label_h) * 2), "white")
        draw = ImageDraw.Draw(sheet)
        for row, page in enumerate(pages):
            paths = (
                root / "candidate/assets/authority_pages" / f"p{page:03d}.png",
                render / "source" / f"page-{page:02d}.png",
                render / "english" / f"page-{page:02d}.png",
            )
            for col, (layer, path) in enumerate(zip(("AUTHORITY", "SOURCE", "ENGLISH"), paths)):
                with Image.open(path) as source:
                    image = source.convert("RGB")
                    image.thumbnail((cell_w - 8, cell_h - 8), Image.Resampling.LANCZOS)
                x = col * cell_w + (cell_w - image.width) // 2
                y0 = row * (cell_h + label_h)
                y = y0 + label_h + (cell_h - image.height) // 2
                sheet.paste(image, (x, y))
                draw.text((col * cell_w + 8, y0 + 4), f"{layer} p{page:02d} / {page + 79}", fill="black", font=font)
                draw.rectangle((col * cell_w, y0, (col + 1) * cell_w - 1, y0 + cell_h + label_h - 1), outline="#999999")
        label = f"{pages[0]:03d}_{pages[-1]:03d}"
        sheet.save(out_dir / f"TRIAD_{label}.png", optimize=True)
    print("PASS_TRIAD_RENDER", len(list(out_dir.glob("TRIAD_*.png"))))


if __name__ == "__main__":
    main()
