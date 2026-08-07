from __future__ import annotations

import hashlib
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageStat


ROOT = Path(__file__).resolve().parent
IMAGE_DIR = ROOT / "img"
SHEET_DIR = ROOT / "sheet"
VISUAL_RECORD = ROOT / "vis.json"
PAGES_PER_SHEET = 16
COLS = 4
ROWS = 4
THUMB_W = 250
THUMB_H = 354
LABEL_H = 24
GAP = 8


def page_number(path: Path) -> int:
    return int(path.stem.split("-")[-1])


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def main() -> None:
    pages = sorted(IMAGE_DIR.glob("p-*.png"), key=page_number)
    if [page_number(path) for path in pages] != list(range(1, 425)):
        raise SystemExit("expected exactly page images 1 through 424")
    if VISUAL_RECORD.exists():
        raise SystemExit("refusing to overwrite vis.json")
    SHEET_DIR.mkdir(exist_ok=False)
    font = ImageFont.load_default()
    cell_w = THUMB_W + 2 * GAP
    cell_h = THUMB_H + LABEL_H + 2 * GAP
    records: list[dict[str, object]] = []
    dimensions: set[tuple[int, int]] = set()
    blank_suspects: list[int] = []
    edge_suspects: list[int] = []
    unexpected_dimensions: list[dict[str, object]] = []
    for offset in range(0, len(pages), PAGES_PER_SHEET):
        group = pages[offset : offset + PAGES_PER_SHEET]
        canvas = Image.new("RGB", (COLS * cell_w, ROWS * cell_h), "#d9d9d9")
        draw = ImageDraw.Draw(canvas)
        for local_index, path in enumerate(group):
            row, col = divmod(local_index, COLS)
            x = col * cell_w + GAP
            y = row * cell_h + GAP
            page = page_number(path)
            with Image.open(path) as source:
                source.load()
                image = source.convert("RGB")
                gray = image.convert("L")
                dimensions.add(image.size)
                expected_size = (1287, 910) if page in (41, 42) else (910, 1287)
                if image.size != expected_size:
                    unexpected_dimensions.append(
                        {"page": page, "actual": list(image.size), "expected": list(expected_size)}
                    )
                mask = gray.point(lambda value: 255 if value < 245 else 0)
                bbox = mask.getbbox()
                histogram = gray.histogram()
                ink_fraction = sum(histogram[:245]) / (image.width * image.height)
                mean_gray = float(ImageStat.Stat(gray).mean[0])
                blank = bbox is None or ink_fraction < 0.001
                edge = bool(
                    bbox
                    and (
                        bbox[0] <= 2
                        or bbox[1] <= 2
                        or bbox[2] >= image.width - 2
                        or bbox[3] >= image.height - 2
                    )
                )
                if blank:
                    blank_suspects.append(page)
                if edge:
                    edge_suspects.append(page)
                records.append(
                    {
                        "page": page,
                        "file": path.name,
                        "bytes": path.stat().st_size,
                        "sha256": sha256(path),
                        "width": image.width,
                        "height": image.height,
                        "ink_fraction": round(ink_fraction, 8),
                        "mean_gray": round(mean_gray, 5),
                        "bbox_lt245": list(bbox) if bbox else None,
                        "blank_suspect": blank,
                        "edge_suspect": edge,
                    }
                )
                image.thumbnail((THUMB_W, THUMB_H), Image.Resampling.LANCZOS)
            px = x + (THUMB_W - image.width) // 2
            py = y + LABEL_H + (THUMB_H - image.height) // 2
            canvas.paste(image, (px, py))
            draw.text((x, y + 3), f"page {page}", fill="black", font=font)
        first = page_number(group[0])
        last = page_number(group[-1])
        canvas.save(SHEET_DIR / f"s{first:03d}-{last:03d}.jpg", quality=92, subsampling=0)

    result = {
        "record_id": "ZHCHK-NOETHER-CUM-R5-VIS-MECHANICAL-001",
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
        "contact_sheets": sorted(path.name for path in SHEET_DIR.glob("*.jpg")),
        "pages": records,
    }
    VISUAL_RECORD.write_text(
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
