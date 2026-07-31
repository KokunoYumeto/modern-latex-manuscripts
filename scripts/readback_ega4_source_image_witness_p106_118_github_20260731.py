#!/usr/bin/env python3
"""Read back the EGA IV p106-118 publication closeout commit."""

from __future__ import annotations

import readback_ega4_source_image_witness_p087_105_github_20260731 as base


base.COMMIT = "c064f739b369fcfeb0ab831a93a328eb594c861d"
base.RECEIPT_STEM = (
    "20260731_ega4_source_image_witness_p106_118_"
    "closeout_commit_c064f739_public_readback"
)
base.TITLE = "EGA IV printed pages 106-118 GitHub closeout readback"


if __name__ == "__main__":
    raise SystemExit(base.main())
