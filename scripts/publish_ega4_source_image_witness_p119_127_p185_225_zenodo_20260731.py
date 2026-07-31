#!/usr/bin/env python3
"""Publish the EGA IV printed 119-127 and 185-225 source-image ZIPs."""

from __future__ import annotations

import os
from pathlib import Path

import publish_ega4_source_image_witness_p087_105_zenodo_20260731 as base


base.PREDECESSOR_RECORD = 21_712_610
base.PREDECESSOR_DOI = "10.5281/zenodo.21712610"
base.EXPECTED_PREDECESSOR_FILES = 34
base.EXPECTED_PREDECESSOR_BYTES = 1_783_031_328
base.EXPECTED_FINAL_FILES = 36
base.EXPECTED_FINAL_BYTES = 2_133_238_113
base.EXPECTED_SOURCE_IMAGES = 178
base.EXPECTED_ZIP_MEMBERS = 186
base.VERSION = (
    "2026-07-31 EGA IV source-image witnesses for printed pages 119-127 "
    "and 185-225"
)
base.GITHUB_COMMIT = "8a2b16ab069225a3f1b0645c231a3a0ed534f5be"
base.GITHUB_PATH = "sources/ega/visual-evidence"
base.ZIP_ROOT = Path(os.environ["LOCALAPPDATA"]) / "Temp" / (
    "ega4_source_image_witness_p119_225_upload_20260731"
)
base.READBACK_ROOT = Path(os.environ["LOCALAPPDATA"]) / "Temp" / (
    "ega4_source_image_witness_p119_225_readback_20260731"
)
base.PREDECESSOR_RECEIPT = base.RECEIPT_ROOT / (
    "20260731_ega4_source_image_witness_p106_118_"
    "record_21712610_public_readback.json"
)
base.RECEIPT_TAG = "20260731_ega4_source_image_witness_p119_127_p185_225"
base.DRAFT_STATE = base.RECEIPT_ROOT / f"{base.RECEIPT_TAG}_zenodo_draft_state.json"
base.NEW_FILES = {
    "88 EGA IV - Source Image Witnesses Printed 119-127 "
    "(600-1800dpi) 20260731.zip": {
        "bytes": 115_118_349,
        "sha256": (
            "931F3A7154EBDA5FE77279D66EBB81942C74C9E7CEC2A4E4E28B6D1B116F1332"
        ),
        "members": 40,
        "images": 36,
        "uncompressed_bytes": 115_106_909,
    },
    "89 EGA IV - Source Image Witnesses Printed 185-225 "
    "(600-5000dpi) 20260731.zip": {
        "bytes": 235_088_436,
        "sha256": (
            "E27FBE24F2C6E85F46D9B8034E5AD96C175B33D5C2AE0EA58026C881D174FF16"
        ),
        "members": 146,
        "images": 142,
        "uncompressed_bytes": 235_044_078,
    },
}
base.DESCRIPTION_ADDITION = (
    "<p><strong>EGA IV source-image witnesses for printed pages 119-127 and "
    "185-225:</strong> this successor adds two ZIPs containing 178 actual "
    "scan-derived PNG witnesses from the publicly available NUMDAM EGA IV Part "
    "4 scan already downloadable on this record. Archive 88 provides one "
    "600-dpi full page and three overlapping 1800-dpi bands for each printed "
    "page 119-127, bound to producer checkpoint r33. Archive 89 provides "
    "5000-dpi tiled source crops for pages 185-195 and 1800-dpi full-page "
    "renders for pages 196-225, bound to producer checkpoint r12. The gap at "
    "printed pages 128-184 remains explicit. English-reader screenshots are "
    "excluded. Every member has page, dimensions, resolution, SHA-256, linked "
    "TeX, and QA-disposition metadata.</p>"
)
base.NOTES_ADDITION = (
    "<p>Archives 88 and 89 add actual EGA IV source-scan evidence for printed "
    "pages 119-127 and 185-225. They are not redundant screenshots of the "
    "downloadable English readers. EGA 0 remains the default browser preview.</p>"
)


if __name__ == "__main__":
    raise SystemExit(base.main())
