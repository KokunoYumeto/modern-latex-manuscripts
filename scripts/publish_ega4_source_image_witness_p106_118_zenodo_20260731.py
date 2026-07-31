#!/usr/bin/env python3
"""Publish the EGA IV printed 106-118 source-image witness ZIP."""

from __future__ import annotations

import os
from pathlib import Path

import publish_ega4_source_image_witness_p087_105_zenodo_20260731 as base


base.PREDECESSOR_RECORD = 21_712_381
base.PREDECESSOR_DOI = "10.5281/zenodo.21712381"
base.EXPECTED_PREDECESSOR_FILES = 33
base.EXPECTED_PREDECESSOR_BYTES = 1_622_065_440
base.EXPECTED_FINAL_FILES = 34
base.EXPECTED_FINAL_BYTES = 1_783_031_328
base.EXPECTED_SOURCE_IMAGES = 52
base.EXPECTED_ZIP_MEMBERS = 56
base.VERSION = "2026-07-31 EGA IV source-image witnesses through printed page 118"
base.GITHUB_COMMIT = "5e85c6ba819e4509226d72167e26f675ff9b6d75"
base.GITHUB_PATH = (
    "sources/ega/visual-evidence/"
    "ega4-sections16-18-source-image-witnesses-printed106-118-20260731"
)
base.ZIP_ROOT = Path(os.environ["LOCALAPPDATA"]) / "Temp" / (
    "ega4_source_image_witness_p106_118_upload_20260731"
)
base.READBACK_ROOT = Path(os.environ["LOCALAPPDATA"]) / "Temp" / (
    "ega4_source_image_witness_p106_118_readback_20260731"
)
base.PREDECESSOR_RECEIPT = base.RECEIPT_ROOT / (
    "20260731_ega4_source_image_witness_p087_105_"
    "record_21712381_public_readback.json"
)
base.RECEIPT_TAG = "20260731_ega4_source_image_witness_p106_118"
base.DRAFT_STATE = base.RECEIPT_ROOT / f"{base.RECEIPT_TAG}_zenodo_draft_state.json"
base.NEW_FILES = {
    "87 EGA IV - Source Image Witnesses Printed 106-118 "
    "(600-1800dpi) 20260731.zip": {
        "bytes": 160_965_888,
        "sha256": (
            "76027378EA97BD51D33B1D7E406E20C48FDF8FF6D6921D2CA79B9689632BD5E1"
        ),
        "members": 56,
        "images": 52,
        "uncompressed_bytes": 160_949_760,
    }
}
base.DESCRIPTION_ADDITION = (
    "<p><strong>EGA IV source-image witnesses through printed page 118:</strong> "
    "this successor adds one ZIP containing 52 actual scan-derived PNG witnesses "
    "from the publicly available NUMDAM EGA IV Part 4 scan already downloadable "
    "on this record. It preserves one 600-dpi full page and three overlapping "
    "1800-dpi bands for each printed page 106-118. Pages 106-111 are bound to "
    "producer checkpoint r31; pages 112-118 are explicitly marked active-"
    "continuation witnesses rather than alignment-closed text. English-reader "
    "screenshots are excluded. Every member has page, dimensions, resolution, "
    "SHA-256, linked TeX, and QA-disposition metadata.</p>"
)
base.NOTES_ADDITION = (
    "<p>Archive 87 extends the actual EGA IV source-image witness set through "
    "printed page 118. It contains source-scan evidence, not redundant screenshots "
    "of the downloadable English readers. EGA 0 remains the default browser "
    "preview.</p>"
)


if __name__ == "__main__":
    raise SystemExit(base.main())
