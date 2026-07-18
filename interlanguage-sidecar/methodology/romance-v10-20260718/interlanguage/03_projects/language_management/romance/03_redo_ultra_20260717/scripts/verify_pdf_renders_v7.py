from __future__ import annotations

import hashlib
import json
import subprocess
import tempfile
from pathlib import Path

from PIL import Image, ImageChops


ROOT = Path(__file__).resolve().parent.parent
POPLER = Path(
    r"C:\Users\Floris\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe"
)
OUT = ROOT / "qa" / "PDF_RENDER_REPRODUCIBILITY_v7.json"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def first_nonwhite_row(path: Path) -> int | None:
    with Image.open(path).convert("RGB") as image:
        white = Image.new("RGB", image.size, "white")
        bbox = ImageChops.difference(image, white).getbbox()
        return None if bbox is None else bbox[1]


def render_and_check(tranche: str, page_count: int) -> dict:
    base = ROOT / tranche
    pdf = base / "build" / f"{tranche}_romance.pdf"
    pinned_dir = base / "qa" / "rendered"
    with tempfile.TemporaryDirectory(prefix=f"{tranche}_", dir=ROOT / "tmp" / "pdfs") as temp_name:
        prefix = Path(temp_name) / f"{tranche}_page"
        subprocess.run(
            [str(POPLER), "-png", "-r", "150", str(pdf), str(prefix)],
            check=True,
            capture_output=True,
        )
        rendered = sorted(Path(temp_name).glob(f"{tranche}_page-*.png"))
        assert len(rendered) == page_count, (tranche, len(rendered), page_count)
        pages = []
        for index, fresh in enumerate(rendered, start=1):
            pinned = pinned_dir / f"{tranche}_page-{index}.png"
            assert pinned.exists(), pinned
            fresh_hash = sha(fresh)
            pinned_hash = sha(pinned)
            assert fresh_hash == pinned_hash, (tranche, index, fresh_hash, pinned_hash)
            with Image.open(fresh) as image:
                size = list(image.size)
            pages.append(
                {
                    "page": index,
                    "fresh_render_sha256": fresh_hash,
                    "pinned_render_sha256": pinned_hash,
                    "exact_match": True,
                    "pixel_size": size,
                    "first_nonwhite_row": first_nonwhite_row(fresh),
                }
            )
    return {
        "tranche": tranche,
        "pdf_sha256": sha(pdf),
        "page_count": page_count,
        "pages": pages,
    }


def main() -> None:
    (ROOT / "tmp" / "pdfs").mkdir(parents=True, exist_ok=True)
    assert POPLER.exists(), POPLER
    results = [render_and_check("R823_HG_T002", 2), render_and_check("R823_HG_T003", 2)]
    t002_page2 = results[0]["pages"][1]
    assert t002_page2["first_nonwhite_row"] == 299
    assert t002_page2["first_nonwhite_row"] >= 250
    report = {
        "artifact": "PDF_RENDER_REPRODUCIBILITY_v7",
        "status": "PASS",
        "renderer": str(POPLER),
        "render_dpi": 150,
        "tranches": results,
        "t002_page2_top_spacing": {
            "first_nonwhite_row": t002_page2["first_nonwhite_row"],
            "minimum_allowed_row": 250,
            "cap_height_clipped": False,
        },
        "claim_boundary": "Exact renderer reproduction and pixel-boundary checks only; linguistic and intelligibility validation remain zero.",
    }
    OUT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
