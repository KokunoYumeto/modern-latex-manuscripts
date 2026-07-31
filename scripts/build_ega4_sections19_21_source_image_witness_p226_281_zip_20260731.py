#!/usr/bin/env python3
"""Build the EGA IV printed 226-281 source-image witness ZIP."""

from __future__ import annotations

import json
import re
from pathlib import Path

import build_ega4_sections19_21_source_image_witness_p185_225_zip_20260731 as prior


PART = {
    "minimum": 226,
    "maximum": 281,
    "aligned_through": 271,
    "alignment_checkpoint": "build_p185_271_r14",
    "linked_tex_unit": "source/source_aligned/ega4-21.tex",
    "filename": (
        "89b EGA IV - Source Image Witnesses Printed 226-281 "
        "(1800dpi) 20260731.zip"
    ),
    "root": "EGA4_Source_Image_Witnesses_Printed226_281_20260731",
}

prior.PART = PART
prior.base.PART = PART


def add_full_page(
    rows: list[dict[str, object]], source_root: Path, path: Path, printed: int
) -> None:
    prior.add_row(
        rows,
        source_root,
        path,
        printed,
        "full_page",
        1800,
        (
            "source_alignment_checkpoint_build_p185_271_r14"
            if printed <= int(PART["aligned_through"])
            else "prepared_source_witness_active_continuation_not_yet_ledger_closed"
        ),
    )


def build_rows(source_root: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []

    # The producer filenames use physical-page numbering (printed page minus one).
    # Printed page 226 is the third page retained in the 224-226 batch.
    add_full_page(
        rows,
        source_root,
        source_root / "IV4_printed224_226_1800dpi" / "source-225.png",
        226,
    )

    for start, finish in (
        (227, 231),
        (237, 241),
        (242, 246),
        (247, 251),
        (252, 256),
        (257, 261),
        (262, 266),
        (267, 271),
        (272, 276),
        (277, 281),
    ):
        directory = source_root / f"IV4_printed{start:03d}_{finish:03d}_1800dpi"
        for printed in range(start, finish + 1):
            physical = printed - 1
            add_full_page(rows, source_root, directory / f"source-{physical}.png", printed)

    # The 232-236 batch contains a corrected explicitly named page-232 render,
    # followed by physical-page-numbered files for printed pages 233-236.
    directory = source_root / "IV4_printed232_236_1800dpi"
    add_full_page(rows, source_root, directory / "source-printed232.png", 232)
    for printed in range(233, 237):
        add_full_page(
            rows,
            source_root,
            directory / f"source-{printed - 1}.png",
            printed,
        )

    detail = (
        source_root
        / "IV4_printed227_231_1800dpi"
        / "source-228_detail_20.1.8.png"
    )
    prior.add_row(
        rows,
        source_root,
        detail,
        229,
        "detail_20_1_8",
        1800,
        "source_alignment_checkpoint_build_p185_271_r14",
    )

    rows.sort(key=lambda row: str(row["entry_path"]).casefold())
    if len(rows) != 57:
        raise RuntimeError(f"Expected 57 source witnesses, found {len(rows)}")
    page_counts = {
        page: sum(int(row["printed_page"]) == page for row in rows)
        for page in range(int(PART["minimum"]), int(PART["maximum"]) + 1)
    }
    if any(count != (2 if page == 229 else 1) for page, count in page_counts.items()):
        raise RuntimeError(f"Printed-page witness closure changed: {page_counts}")
    hashes = [str(row["sha256"]) for row in rows]
    if len(hashes) != len(set(hashes)):
        raise RuntimeError("Duplicate source-image bytes entered the new archive")
    return rows


def archive_readme(rows: list[dict[str, object]]) -> bytes:
    text = f"""# EGA IV source-image witnesses: printed pages 226-281

This ZIP preserves {len(rows)} PNG witnesses / {sum(int(row['bytes']) for row in rows):,} bytes
derived from the publicly available 360-page NUMDAM EGA IV Part 4 scan.
The parent scan SHA-256 is `{prior.base.PARENT_SHA256}` and the parent scan is
directly downloadable from the same EGA Zenodo concept.

The set contains one 1,800-dpi full-page source render for every printed page
226-281 and one additional 1,800-dpi detail crop for formula 20.1.8 on printed
page 229. Every image is bound to physical/printed page, crop role, dimensions,
resolution, bytes/SHA-256, linked editable TeX, and QA disposition in
`VISUAL_EVIDENCE_INDEX.csv` and `.jsonl`.

Printed pages 226-271 are covered by producer checkpoint
`{PART['alignment_checkpoint']}`. Printed pages 272-281 are retained as the
prepared active continuation and do not claim alignment closure. Filename
offsets and the corrected page-232 image are resolved explicitly by this
archive's build script; duplicate boundary renders are excluded.

This is source-image evidence, not screenshots of the English reader PDF. No
OCR body, private path, raw build log, script, cache, or conversation is
included. Publication does not alter rights or attribution in the underlying
work.
"""
    return text.encode("utf-8")


def write_metadata(
    metadata_root: Path, rows: list[dict[str, object]], archive: dict[str, object]
) -> None:
    metadata_root.mkdir(parents=True, exist_ok=True)
    public_rows = [prior.base.public_row(row) for row in rows]
    (metadata_root / "VISUAL_EVIDENCE_INDEX.csv").write_bytes(
        prior.base.csv_bytes(public_rows, prior.base.INDEX_FIELDS)
    )
    (metadata_root / "VISUAL_EVIDENCE_INDEX.jsonl").write_bytes(
        prior.base.jsonl_bytes(public_rows)
    )
    (metadata_root / "ZIP_PAYLOAD_MANIFEST.csv").write_bytes(
        prior.base.csv_bytes([archive], tuple(archive))
    )
    (metadata_root / "README.md").write_text(
        "# EGA IV Sections 19-21 source-image witnesses, printed 226-281\n\n"
        f"This metadata binds the actual {len(rows)} scan-derived PNGs in "
        f"`{PART['filename']}`. Printed pages through {PART['aligned_through']} "
        f"are alignment-closed in `{PART['alignment_checkpoint']}`; later pages "
        "are explicitly labeled active continuation. English-reader renders "
        "are not included.\n",
        encoding="utf-8",
        newline="\n",
    )
    validation = {
        "status": "PASS_READY_FOR_SAME_CONCEPT_ZENODO_UPLOAD",
        "images": len(rows),
        "image_bytes": sum(int(row["bytes"]) for row in rows),
        "printed_page_min": int(PART["minimum"]),
        "printed_page_max": int(PART["maximum"]),
        "aligned_through_printed_page": int(PART["aligned_through"]),
        "parent_scan_sha256": prior.base.PARENT_SHA256,
        "zip_archive": archive,
        "privacy_hits": 0,
        "duplicate_image_hashes": 0,
        "errors": [],
    }
    (metadata_root / "VALIDATION.json").write_text(
        json.dumps(validation, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    represented = sorted(
        path
        for path in metadata_root.iterdir()
        if path.is_file() and path.name != "SHA256SUMS.csv"
    )
    sums_rows = [
        {
            "path": path.name,
            "bytes": path.stat().st_size,
            "sha256": prior.base.sha256_path(path),
        }
        for path in represented
    ]
    (metadata_root / "SHA256SUMS.csv").write_bytes(
        prior.base.csv_bytes(sums_rows, ("path", "bytes", "sha256"))
    )


def main() -> None:
    parser = prior.argparse.ArgumentParser()
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--zip-output", type=Path, required=True)
    parser.add_argument("--metadata-output", type=Path, required=True)
    args = parser.parse_args()
    args.zip_output.mkdir(parents=True, exist_ok=True)
    rows = build_rows(args.source_root)
    prior.base.readme = archive_readme
    archive = prior.base.build_zip(args.zip_output, rows)
    write_metadata(args.metadata_output, rows, archive)
    print(json.dumps({"status": "PASS", "images": len(rows), "zip": archive}, indent=2))


if __name__ == "__main__":
    main()
