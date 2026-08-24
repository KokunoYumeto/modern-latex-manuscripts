#!/usr/bin/env python3
"""Make labeled D035 contact sheets and deterministic per-page image metrics."""

from __future__ import annotations

import json
import pathlib

from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageStat


ROOT = pathlib.Path(__file__).resolve().parents[2]
RENDERED = ROOT / "audit" / "rendered"


def page_metrics(path: pathlib.Path) -> dict:
    image = Image.open(path).convert("L")
    width, height = image.size
    histogram = image.histogram()
    pixels = width * height
    nonwhite = sum(histogram[:250]) / pixels
    dark = sum(histogram[:96]) / pixels
    edge = max(5, round(min(width, height) * 0.012))
    edges = [
        image.crop((0, 0, width, edge)),
        image.crop((0, height - edge, width, height)),
        image.crop((0, 0, edge, height)),
        image.crop((width - edge, 0, width, height)),
    ]
    edge_pixels = sum(e.width * e.height for e in edges)
    edge_dark = sum(sum(e.histogram()[:96]) for e in edges) / edge_pixels
    inverted = ImageChops.invert(image)
    bbox = inverted.point(lambda x: 255 if x > 10 else 0).getbbox()
    return {
        "path": str(path.relative_to(ROOT)).replace("\\", "/"),
        "width": width,
        "height": height,
        "nonwhite_fraction": round(nonwhite, 9),
        "dark_fraction": round(dark, 9),
        "edge_dark_fraction": round(edge_dark, 9),
        "content_bbox": list(bbox) if bbox else None,
    }


def contact_sheet(paths: list[pathlib.Path], target: pathlib.Path, label: str) -> None:
    columns = 3
    thumb_width = 360
    label_height = 28
    margin = 15
    sample = Image.open(paths[0])
    thumb_height = round(sample.height * thumb_width / sample.width)
    rows = (len(paths) + columns - 1) // columns
    sheet = Image.new(
        "RGB",
        (
            margin * (columns + 1) + thumb_width * columns,
            52 + margin * (rows + 1) + (thumb_height + label_height) * rows,
        ),
        "white",
    )
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default(size=18)
    draw.text((margin, 12), label, fill="black", font=font)
    for index, path in enumerate(paths):
        row, col = divmod(index, columns)
        x = margin + col * (thumb_width + margin)
        y = 52 + margin + row * (thumb_height + label_height + margin)
        image = Image.open(path).convert("RGB")
        image.thumbnail((thumb_width, thumb_height), Image.Resampling.LANCZOS)
        sheet.paste(image, (x, y))
        draw.rectangle((x, y, x + image.width - 1, y + image.height - 1), outline="#777777")
        draw.text((x, y + thumb_height + 3), path.stem, fill="black", font=font)
    target.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(target, format="PNG", optimize=False)


def main() -> None:
    all_metrics: dict[str, list[dict]] = {}
    for edition in ("fr", "en", "apparatus"):
        paths = sorted((RENDERED / edition).glob("page-*.png"))
        if len(paths) != 34:
            raise SystemExit(f"{edition}: expected 34 rendered pages, got {len(paths)}")
        all_metrics[edition] = [page_metrics(path) for path in paths]
        contact_sheet(paths[:17], RENDERED / f"CONTACT_{edition.upper()}_P001_P017.png", f"D035 {edition}: pages 1--17")
        contact_sheet(paths[17:], RENDERED / f"CONTACT_{edition.upper()}_P018_P034.png", f"D035 {edition}: pages 18--34")
    (ROOT / "audit" / "VISUAL_METRICS.json").write_text(
        json.dumps(all_metrics, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n"
    )
    for edition, rows in all_metrics.items():
        print(
            edition,
            len(rows),
            min(row["nonwhite_fraction"] for row in rows),
            max(row["nonwhite_fraction"] for row in rows),
            max(row["edge_dark_fraction"] for row in rows),
        )


if __name__ == "__main__":
    main()
