#!/usr/bin/env python3
"""Read back the EGA IV p128-155 and p226-281 closeout commit."""

from __future__ import annotations

import readback_ega4_source_image_witness_p087_105_github_20260731 as base


base.COMMIT = "b6228eee74c1c43f3c439fc44363d8f79b3feda3"
base.RECEIPT_STEM = (
    "20260731_ega4_source_image_witness_p128_155_p226_281_"
    "closeout_commit_b6228eee_public_readback"
)
base.TITLE = "EGA IV printed pages 128-155 and 226-281 GitHub closeout readback"


if __name__ == "__main__":
    raise SystemExit(base.main())
