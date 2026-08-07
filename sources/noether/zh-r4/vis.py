from __future__ import annotations

import hashlib
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageStat


HERE = Path(__file__).resolve().parent
IMG = HERE / "img"
SHEETS = HERE / "sheet"
OUT = HERE / "vis.json"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def main() -> None:
    if OUT.exists() or SHEETS.exists():
        raise RuntimeError("refusing to overwrite visual QA output")

    pages = sorted(IMG.glob("p-*.png"))
    expected_names = [f"p-{page:03d}.png" for page in range(1, 425)]
    if [path.name for path in pages] != expected_names:
        raise RuntimeError("rendered-page sequence is not exactly 1--424")

    SHEETS.mkdir()
    font = ImageFont.load_default()
    records: list[dict[str, object]] = []
    dimensions: set[tuple[int, int]] = set()
    blank_suspects: list[int] = []
    edge_suspects: list[int] = []
    unexpected_dimensions: list[dict[str, object]] = []

    cols, rows = 4, 4
    cell_w, cell_h = 260, 375
    sheet: Image.Image | None = None
    draw: ImageDraw.ImageDraw | None = None

    for index, path in enumerate(pages):
        page_number = index + 1
        with Image.open(path) as source:
            source.load()
            rgb = source.convert("RGB")
            gray = rgb.convert("L")
            dimensions.add(rgb.size)
            expected_size = (1287, 910) if page_number in (41, 42) else (910, 1287)
            if rgb.size != expected_size:
                unexpected_dimensions.append(
                    {
                        "page": page_number,
                        "actual": list(rgb.size),
                        "expected": list(expected_size),
                    }
                )

            # Pixels darker than 245 are treated as visible content.
            mask = gray.point(lambda value: 255 if value < 245 else 0)
            bbox = mask.getbbox()
            hist = gray.histogram()
            ink = sum(hist[:245])
            total = rgb.width * rgb.height
            ink_fraction = ink / total
            stat = ImageStat.Stat(gray)
            blank = bbox is None or ink_fraction < 0.001
            edge = bool(
                bbox
                and (
                    bbox[0] <= 2
                    or bbox[1] <= 2
                    or bbox[2] >= rgb.width - 2
                    or bbox[3] >= rgb.height - 2
                )
            )
            if blank:
                blank_suspects.append(page_number)
            if edge:
                edge_suspects.append(page_number)

            records.append(
                {
                    "page": page_number,
                    "file": path.name,
                    "bytes": path.stat().st_size,
                    "sha256": sha256(path),
                    "width": rgb.width,
                    "height": rgb.height,
                    "ink_fraction": round(ink_fraction, 8),
                    "mean_gray": round(float(stat.mean[0]), 5),
                    "bbox_lt245": list(bbox) if bbox else None,
                    "blank_suspect": blank,
                    "edge_suspect": edge,
                }
            )

            sheet_offset = index % (cols * rows)
            if sheet_offset == 0:
                sheet = Image.new("RGB", (cols * cell_w, rows * cell_h), "white")
                draw = ImageDraw.Draw(sheet)
            assert sheet is not None and draw is not None
            thumb = rgb.copy()
            thumb.thumbnail((240, 340), Image.Resampling.LANCZOS)
            col = sheet_offset % cols
            row = sheet_offset // cols
            x = col * cell_w + (cell_w - thumb.width) // 2
            y = row * cell_h + 22
            sheet.paste(thumb, (x, y))
            draw.text((col * cell_w + 8, row * cell_h + 5), f"p.{page_number}", fill="black", font=font)

            if sheet_offset == cols * rows - 1 or index == len(pages) - 1:
                first = index - sheet_offset + 1
                last = page_number
                sheet.save(SHEETS / f"s{first:03d}-{last:03d}.jpg", quality=90, optimize=True)
                sheet.close()
                sheet = None
                draw = None

    result = {
        "record_id": "ZHCHK-NOETHER-CUM-R4-VIS-MECHANICAL-001",
        "render": {
            "engine": "Poppler pdftoppm",
            "dpi": 110,
            "page_count": len(pages),
            "dimensions": [list(item) for item in sorted(dimensions)],
        },
        "mechanical_screen": {
            "blank_suspects": blank_suspects,
            "edge_suspects": edge_suspects,
            "unexpected_dimensions": unexpected_dimensions,
            "allowed_landscape_pages": [41, 42],
            "all_pass": not blank_suspects and not edge_suspects and not unexpected_dimensions,
        },
        "contact_sheets": sorted(path.name for path in SHEETS.glob("*.jpg")),
        "pages": records,
    }
    OUT.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(
        json.dumps(
            {
                "pages": len(pages),
                "dimensions": result["render"]["dimensions"],
                "blank_suspects": blank_suspects,
                "edge_suspects": edge_suspects,
                "unexpected_dimensions": unexpected_dimensions,
                "sheets": len(result["contact_sheets"]),
            }
        )
    )


if __name__ == "__main__":
    main()
