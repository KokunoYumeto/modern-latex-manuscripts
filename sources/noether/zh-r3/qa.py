from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

from PIL import Image, ImageChops
from pypdf import PdfReader


HERE = Path(__file__).resolve().parent
OLD = HERE.parent / "cum_r2"
WITNESS = (
    HERE.parents[2]
    / "03_working_translations"
    / "P09_zh_v2"
    / "src"
    / "zh_wit.tex"
)
CANDIDATE = HERE.parent / "paper09" / "rb1" / "p09.tex"
OLD_HASH = "E03B84F2C56D0FA839A5FC03A1B04532550A38A84E9B4F1146B03547816643F5"
WITNESS_HASH = "3BF1EA83C5AD18BC388DCDCAEF38B608693A66088D4C7377B641A4231E2DDDBF"
CANDIDATE_HASH = "1199FC266E910F61AFE6A7BAFB9E390595B8DD7DE848EAE3BC939D8626CEEE94"
NEW_HASH = "50B212EA04061921607E13CB7B367DEBF4AAF2449CF5614F931E74AA1B5A5338"
OFFSET = 379_451
EXPECTED_CHANGED = [
    92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106,
    108, 109, 110, 111, 112, 113, 114, 116, 118, 119, 120, 121, 123, 124,
    125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138,
    139, 140, 141, 142, 144, 146, 147, 149, 151, 152, 153, 155, 156, 157,
    158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 171, 172, 173,
    175, 176, 177, 178, 179, 181, 182, 183, 184, 185, 186,
]


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


old = (OLD / "reader.tex").read_bytes()
witness = WITNESS.read_bytes()
candidate = CANDIDATE.read_bytes()
new = (HERE / "reader.tex").read_bytes()
if (len(old), digest(old)) != (1_810_851, OLD_HASH):
    raise SystemExit("predecessor identity mismatch")
if (len(witness), digest(witness)) != (66_683, WITNESS_HASH):
    raise SystemExit("witness identity mismatch")
if (len(candidate), digest(candidate)) != (66_861, CANDIDATE_HASH):
    raise SystemExit("P09 candidate identity mismatch")
if (len(new), digest(new)) != (1_811_029, NEW_HASH):
    raise SystemExit("successor identity mismatch")
expected = old[:OFFSET] + candidate + old[OFFSET + len(witness) :]
if old[OFFSET : OFFSET + len(witness)] != witness or new != expected:
    raise SystemExit("exact splice gate failed")

old_pages = sorted((OLD / "viz").glob("p-*.png"))
new_pages = sorted((HERE / "viz").glob("p-*.png"))
if len(old_pages) != 413 or len(new_pages) != 413:
    raise SystemExit("render count mismatch")

changed: list[dict[str, object]] = []
blank: list[int] = []
edge: list[int] = []
dimensions: set[tuple[int, int]] = set()
for number, (old_path, new_path) in enumerate(zip(old_pages, new_pages), 1):
    if old_path.name != new_path.name:
        raise SystemExit("render name mismatch")
    with Image.open(old_path) as old_image, Image.open(new_path) as new_image:
        old_rgb = old_image.convert("RGB")
        new_rgb = new_image.convert("RGB")
        if old_rgb.size != new_rgb.size:
            raise SystemExit(f"dimension mismatch on page {number}")
        dimensions.add(new_rgb.size)
        bbox = ImageChops.difference(old_rgb, new_rgb).getbbox()
        if bbox is not None:
            changed.append({"page": number, "bbox": list(bbox)})
        gray = new_rgb.convert("L")
        if gray.getextrema()[0] >= 245:
            blank.append(number)
        width, height = gray.size
        bands = (
            gray.crop((0, 0, width, 2)),
            gray.crop((0, height - 2, width, height)),
            gray.crop((0, 0, 2, height)),
            gray.crop((width - 2, 0, width, height)),
        )
        if any(band.getextrema()[0] < 245 for band in bands):
            edge.append(number)

log = (HERE / "pass2.log").read_text(encoding="utf-8", errors="replace")
diagnostics = {
    "latex_warning": len(re.findall(r"LaTeX Warning", log)),
    "package_warning": len(re.findall(r"Package .* Warning", log)),
    "overfull": len(re.findall(r"Overfull \\hbox|Overfull \\vbox", log)),
    "underfull": len(re.findall(r"Underfull \\hbox|Underfull \\vbox", log)),
    "undefined_control": len(re.findall(r"Undefined control sequence", log)),
    "missing_character": len(re.findall(r"Missing character", log)),
    "fatal": len(re.findall(r"Fatal error|Emergency stop", log)),
}
changed_numbers = [int(entry["page"]) for entry in changed]
old_pdf_pages = len(PdfReader(str(OLD / "reader.pdf")).pages)
new_pdf_pages = len(PdfReader(str(HERE / "reader.pdf")).pages)
result = {
    "qa_id": "ZHCHK-CUM-R3-QA-001",
    "exact_splice": {
        "offset": OFFSET,
        "removed_bytes": len(witness),
        "inserted_bytes": len(candidate),
        "prefix_bytes": OFFSET,
        "suffix_bytes": len(old) - OFFSET - len(witness),
        "outside_bytes_unchanged": True,
    },
    "pdf": {
        "bytes": (HERE / "reader.pdf").stat().st_size,
        "sha256": digest((HERE / "reader.pdf").read_bytes()),
        "pages": new_pdf_pages,
        "predecessor_pages": old_pdf_pages,
    },
    "render": {
        "dpi": 144,
        "pages": len(new_pages),
        "dimensions": [list(value) for value in sorted(dimensions)],
        "changed": changed,
        "changed_pages": len(changed),
        "unchanged_pages": 413 - len(changed),
        "blank_pages": blank,
        "outer_two_pixel_ink_pages": edge,
    },
    "pass2_diagnostics": diagnostics,
}
result["all_mechanical_gates_pass"] = (
    old_pdf_pages == new_pdf_pages == 413
    and changed_numbers == EXPECTED_CHANGED
    and not blank
    and not edge
    and all(value == 0 for value in diagnostics.values())
)
if not result["all_mechanical_gates_pass"]:
    raise SystemExit(json.dumps(result, ensure_ascii=False, indent=2))
print(json.dumps(result, ensure_ascii=False, indent=2))
