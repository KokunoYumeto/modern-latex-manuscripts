#!/usr/bin/env python3
"""Build the EGA IV printed 106-118 source-image witness ZIP."""

from __future__ import annotations

import build_ega4_sections16_18_source_image_witness_p087_105_zip_20260731 as base


base.PART = {
    "minimum": 106,
    "maximum": 118,
    "aligned_through": 111,
    "alignment_checkpoint": "checkpoint_printed111_r31",
    "linked_tex_unit": "source/source_aligned/ega4-18.tex",
    "filename": (
        "87 EGA IV - Source Image Witnesses Printed 106-118 "
        "(600-1800dpi) 20260731.zip"
    ),
    "root": "EGA4_Source_Image_Witnesses_Printed106_118_20260731",
}


if __name__ == "__main__":
    base.main()
