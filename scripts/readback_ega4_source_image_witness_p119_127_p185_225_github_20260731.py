#!/usr/bin/env python3
"""Read back the EGA IV p119-127 and p185-225 closeout commit."""

from __future__ import annotations

import readback_ega4_source_image_witness_p087_105_github_20260731 as base


base.COMMIT = "7beecf53e4c20040bb04e614ee39768b14cc9403"
base.RECEIPT_STEM = (
    "20260731_ega4_source_image_witness_p119_127_p185_225_"
    "closeout_commit_7beecf53_public_readback"
)
base.TITLE = "EGA IV printed pages 119-127 and 185-225 GitHub closeout readback"


if __name__ == "__main__":
    raise SystemExit(base.main())
