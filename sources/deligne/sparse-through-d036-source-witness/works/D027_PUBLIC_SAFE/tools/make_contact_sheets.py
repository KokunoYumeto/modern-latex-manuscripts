#!/usr/bin/env python3
"""Create labelled contact sheets from rendered D027 page PNGs."""

from __future__ import annotations

import argparse
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def natural_key(path: Path) -> tuple:
    stem = path.stem
    digits = ""
    for char in reversed(stem):
        if char.isdigit():
            digits = char + digits
        elif digits:
            break
    return (stem[: -len(digits)] if digits else stem, int(digits or 0))


def build_sheets(render_dir: Path, output_dir: Path, label: str, per_sheet: int = 12) -> list[Path]:
    pages = sorted(render_dir.glob("*.png"), key=natural_key)
    if not pages:
        raise ValueError(f"no PNG pages in {render_dir}")

    output_dir.mkdir(parents=True, exist_ok=True)
    font = ImageFont.load_default()
    columns = 4
    rows = math.ceil(per_sheet / columns)
    thumb_width = 300
    thumb_height = 424
    label_height = 24
    gutter = 12
    sheet_width = columns * (thumb_width + gutter) + gutter
    sheet_height = rows * (thumb_height + label_height + gutter) + gutter
    outputs: list[Path] = []

    for sheet_index, start in enumerate(range(0, len(pages), per_sheet), start=1):
        subset = pages[start : start + per_sheet]
        canvas = Image.new("RGB", (sheet_width, sheet_height), "#d8d8d8")
        draw = ImageDraw.Draw(canvas)
        for slot, page in enumerate(subset):
            row, column = divmod(slot, columns)
            x = gutter + column * (thumb_width + gutter)
            y = gutter + row * (thumb_height + label_height + gutter)
            with Image.open(page) as source:
                image = source.convert("RGB")
                image.thumbnail((thumb_width, thumb_height), Image.Resampling.LANCZOS)
                cell = Image.new("RGB", (thumb_width, thumb_height), "white")
                px = (thumb_width - image.width) // 2
                py = (thumb_height - image.height) // 2
                cell.paste(image, (px, py))
                canvas.paste(cell, (x, y))
            page_number = start + slot + 1
            draw.text((x + 4, y + thumb_height + 5), f"{label} PDF page {page_number}: {page.name}", fill="black", font=font)

        output = output_dir / f"{label.lower()}_contact_{sheet_index:02d}.png"
        canvas.save(output, format="PNG", optimize=True)
        outputs.append(output)
    return outputs


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--render-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--label", required=True)
    parser.add_argument("--per-sheet", type=int, default=12)
    args = parser.parse_args()
    outputs = build_sheets(args.render_dir, args.output_dir, args.label, args.per_sheet)
    for output in outputs:
        print(output)


if __name__ == "__main__":
    main()
