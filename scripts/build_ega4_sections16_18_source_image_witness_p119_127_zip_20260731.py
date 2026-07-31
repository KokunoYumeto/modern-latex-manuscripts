#!/usr/bin/env python3
"""Build the EGA IV printed 119-127 source-image witness ZIP."""

from __future__ import annotations

import build_ega4_sections16_18_source_image_witness_p087_105_zip_20260731 as base


base.PART = {
    "minimum": 119,
    "maximum": 127,
    "aligned_through": 127,
    "alignment_checkpoint": "checkpoint_printed127_r33",
    "linked_tex_unit": "source/source_aligned/ega4-18.tex",
    "filename": (
        "88 EGA IV - Source Image Witnesses Printed 119-127 "
        "(600-1800dpi) 20260731.zip"
    ),
    "root": "EGA4_Source_Image_Witnesses_Printed119_127_20260731",
}


if __name__ == "__main__":
    base.main()
