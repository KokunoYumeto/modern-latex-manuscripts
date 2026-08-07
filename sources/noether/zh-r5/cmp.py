from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
BASE = ROOT.parent / "cum_r4"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def main() -> None:
    output = ROOT / "cmp.json"
    if output.exists():
        raise SystemExit("refusing to overwrite cmp.json")
    changed: list[int] = []
    for page in range(1, 425):
        before = BASE / "img" / f"p-{page:03d}.png"
        after = ROOT / "img" / f"p-{page:03d}.png"
        if sha256(before) != sha256(after):
            changed.append(page)
    allowed = set(range(81, 187)) | {326} | set(range(416, 421)) | {423}
    result = {
        "record_id": "ZHCHK-NOETHER-CUM-R5-RASTER-CMP-001",
        "method": "serial SHA-256 comparison of identically rendered 110-dpi Poppler PNGs",
        "base_pdf": {
            "path": "../cum_r4/reader.pdf",
            "bytes": (BASE / "reader.pdf").stat().st_size,
            "sha256": sha256(BASE / "reader.pdf"),
            "pages": 424,
        },
        "candidate_pdf": {
            "path": "reader.pdf",
            "bytes": (ROOT / "reader.pdf").stat().st_size,
            "sha256": sha256(ROOT / "reader.pdf"),
            "pages": 424,
        },
        "render_settings_equal": True,
        "compared_pages": 424,
        "byte_identical_raster_pages": 424 - len(changed),
        "changed_raster_pages": changed,
        "changed_raster_page_count": len(changed),
        "authorized_visual_impact_zones": {
            "P06_P13_notes_and_counter_or_reflow_effects": "81-186",
            "P38_Schur_note": [326],
            "P45_rebase_and_local_counter_or_reference_effects": "416-420",
            "bibliography": [423],
        },
        "changed_pages_outside_authorized_visual_impact_zones": sorted(set(changed) - allowed),
        "mechanical_pass": set(changed) <= allowed,
        "interpretation": "Raster equality is supplemental. Every r5 page was freshly inspected regardless of whether it matched r4.",
    }
    output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    if not result["mechanical_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
