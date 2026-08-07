from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
PRE = HERE / "p1"
OUT = HERE / "cmp.json"


def digest(path: Path) -> tuple[int, str]:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            h.update(chunk)
    return path.stat().st_size, h.hexdigest().upper()


def main() -> None:
    if OUT.exists():
        raise RuntimeError("refusing to overwrite raster-comparison record")

    old_tex = (PRE / "reader.tex").read_bytes()
    new_tex = (HERE / "reader.tex").read_bytes()
    differing_offsets = [
        index for index, (old, new) in enumerate(zip(old_tex, new_tex)) if old != new
    ]
    if len(old_tex) != len(new_tex):
        raise RuntimeError("metadata-only rebuild changed TeX byte length")

    old_text_identity = digest(PRE / "reader.txt")
    new_text_identity = digest(HERE / "reader.txt")

    old_pages = sorted((PRE / "img").glob("p-*.png"))
    new_pages = sorted((HERE / "img").glob("p-*.png"))
    expected_names = [f"p-{page:03d}.png" for page in range(1, 425)]
    if [path.name for path in old_pages] != expected_names:
        raise RuntimeError("accepted comparison render is not exactly pages 1--424")
    if [path.name for path in new_pages] != expected_names:
        raise RuntimeError("final render is not exactly pages 1--424")

    raster_mismatches: list[dict[str, object]] = []
    for old, new in zip(old_pages, new_pages):
        old_identity = digest(old)
        new_identity = digest(new)
        if old_identity != new_identity:
            raster_mismatches.append(
                {
                    "page": int(old.stem.split("-")[1]),
                    "accepted": {"bytes": old_identity[0], "sha256": old_identity[1]},
                    "final": {"bytes": new_identity[0], "sha256": new_identity[1]},
                }
            )

    record = {
        "record_id": "ZHCHK-NOETHER-CUM-R4-RASTER-COMPARE-001",
        "purpose": "prove that the r1-to-r4 PDF metadata correction changed no rendered page content",
        "accepted_pre_metadata_build": {
            "tex": dict(zip(("bytes", "sha256"), digest(PRE / "reader.tex"))),
            "pdf": dict(zip(("bytes", "sha256"), digest(PRE / "reader.pdf"))),
            "text": dict(zip(("bytes", "sha256"), old_text_identity)),
        },
        "final_build": {
            "tex": dict(zip(("bytes", "sha256"), digest(HERE / "reader.tex"))),
            "pdf": dict(zip(("bytes", "sha256"), digest(HERE / "reader.pdf"))),
            "text": dict(zip(("bytes", "sha256"), new_text_identity)),
        },
        "tex_byte_diff": {
            "count": len(differing_offsets),
            "offsets_0_based": differing_offsets,
            "accepted_bytes": [old_tex[index] for index in differing_offsets],
            "final_bytes": [new_tex[index] for index in differing_offsets],
            "expected": "one ASCII byte: r1 -> r4 in pdftitle metadata",
        },
        "text_extraction_byte_identical": old_text_identity == new_text_identity,
        "render": {
            "dpi": 110,
            "page_count": len(new_pages),
            "raster_mismatches": raster_mismatches,
            "all_424_page_rasters_byte_identical": not raster_mismatches,
        },
    }
    record["all_pass"] = bool(
        record["tex_byte_diff"]["count"] == 1
        and record["tex_byte_diff"]["accepted_bytes"] == [49]
        and record["tex_byte_diff"]["final_bytes"] == [52]
        and record["text_extraction_byte_identical"]
        and record["render"]["all_424_page_rasters_byte_identical"]
    )
    if not record["all_pass"]:
        raise RuntimeError(json.dumps(record, ensure_ascii=False))

    OUT.write_text(
        json.dumps(record, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps({"all_pass": True, "raster_pages": len(new_pages)}))


if __name__ == "__main__":
    main()
