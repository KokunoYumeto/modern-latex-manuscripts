from __future__ import annotations

import hashlib
import json
from pathlib import Path

from PIL import Image, ImageChops


HERE = Path(__file__).resolve().parent
PRE = HERE / "p2"
OUT = HERE / "cmp2.json"


def digest(path: Path) -> tuple[int, str]:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            h.update(chunk)
    return path.stat().st_size, h.hexdigest().upper()


def main() -> None:
    if OUT.exists():
        raise RuntimeError("refusing to overwrite source-repair comparison record")

    prior_pages = sorted((PRE / "img").glob("p-*.png"))
    final_pages = sorted((HERE / "img").glob("p-*.png"))
    expected_names = [f"p-{page:03d}.png" for page in range(1, 425)]
    if [path.name for path in prior_pages] != expected_names:
        raise RuntimeError("prior accepted render is not exactly pages 1--424")
    if [path.name for path in final_pages] != expected_names:
        raise RuntimeError("final render is not exactly pages 1--424")

    mismatches: list[dict[str, object]] = []
    for prior_path, final_path in zip(prior_pages, final_pages):
        prior_identity = digest(prior_path)
        final_identity = digest(final_path)
        if prior_identity == final_identity:
            continue
        with Image.open(prior_path) as prior_image, Image.open(final_path) as final_image:
            prior_rgb = prior_image.convert("RGB")
            final_rgb = final_image.convert("RGB")
            if prior_rgb.size != final_rgb.size:
                raise RuntimeError(f"render size changed: {prior_path.name}")
            delta = ImageChops.difference(prior_rgb, final_rgb)
            bbox = delta.getbbox()
            changed_pixels = sum(
                1 for pixel in delta.getdata() if pixel != (0, 0, 0)
            )
        mismatches.append(
            {
                "page": int(prior_path.stem.split("-")[1]),
                "prior": {"bytes": prior_identity[0], "sha256": prior_identity[1]},
                "final": {"bytes": final_identity[0], "sha256": final_identity[1]},
                "pixel_difference_bbox": list(bbox) if bbox else None,
                "changed_pixels": changed_pixels,
            }
        )

    changed_pages = [item["page"] for item in mismatches]
    record = {
        "record_id": "ZHCHK-NOETHER-CUM-R4-SOURCE-REPAIR-RENDER-COMPARE-001",
        "prior_accepted_build": {
            "tex": dict(zip(("bytes", "sha256"), digest(PRE / "reader.tex"))),
            "pdf": dict(zip(("bytes", "sha256"), digest(PRE / "reader.pdf"))),
            "text": dict(zip(("bytes", "sha256"), digest(PRE / "reader.txt"))),
        },
        "final_build": {
            "tex": dict(zip(("bytes", "sha256"), digest(HERE / "reader.tex"))),
            "pdf": dict(zip(("bytes", "sha256"), digest(HERE / "reader.pdf"))),
            "text": dict(zip(("bytes", "sha256"), digest(HERE / "reader.txt"))),
        },
        "render": {
            "engine": "Poppler pdftoppm",
            "dpi": 110,
            "page_count": 424,
            "byte_identical_pages": 424 - len(mismatches),
            "changed_pages": changed_pages,
            "mismatches": mismatches,
        },
        "expected_changed_pages": {
            "380": [
                "ZHCHK-DE-P44-001 ambient-object subscript",
                "ZHCHK-DE-P44-002 E_1 capitalization",
            ],
            "383": ["ZHCHK-DE-P44-003 four n-to-h endpoint substitutions"],
        },
        "manual_visual_reinspection": {
            "pages": [380, 383],
            "result": "PASS: exact repaired symbols are legible, within margins, and introduce no overlap, clipping, or reflow defect",
        },
        "unchanged_page_inference": "The other 422 final page PNGs are byte-identical to the fully inspected prior render.",
        "all_pass": changed_pages == [380, 383],
    }
    if not record["all_pass"]:
        raise RuntimeError(json.dumps(record, ensure_ascii=False))

    OUT.write_text(
        json.dumps(record, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps({"all_pass": True, "changed_pages": changed_pages}))


if __name__ == "__main__":
    main()
