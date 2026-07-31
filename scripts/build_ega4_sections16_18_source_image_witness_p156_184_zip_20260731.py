#!/usr/bin/env python3
"""Build the EGA IV printed 156-184 source-image witness ZIP."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import build_ega4_sections16_18_source_image_witness_p087_105_zip_20260731 as base


base.PART = {
    "minimum": 156,
    "maximum": 184,
    "aligned_through": 184,
    "alignment_checkpoint": "complete_sections16_18_source_aligned_r42",
    "linked_tex_unit": "source/source_aligned/ega4-18.tex",
    "filename": (
        "89c EGA IV - Source Image Witnesses Printed 156-184 "
        "(600-1800dpi) 20260731.zip"
    ),
    "root": "EGA4_Source_Image_Witnesses_Printed156_184_20260731",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--zip-output", type=Path, required=True)
    parser.add_argument("--metadata-output", type=Path, required=True)
    args = parser.parse_args()
    args.zip_output.mkdir(parents=True, exist_ok=True)
    args.metadata_output.mkdir(parents=True, exist_ok=True)
    (args.metadata_output / ".gitattributes").write_bytes(b"* -text\n")
    rows = base.build_rows(args.source_root)
    archive = base.build_zip(args.zip_output, rows)
    base.write_metadata(args.metadata_output, rows, archive)
    print(json.dumps({"status": "PASS", "images": len(rows), "zip": archive}, indent=2))


if __name__ == "__main__":
    main()
