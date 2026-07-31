#!/usr/bin/env python3
"""Publish EGA IV printed 128-155 and 226-281 source-image ZIPs."""

from __future__ import annotations

import os
from pathlib import Path

import publish_ega4_source_image_witness_p087_105_zenodo_20260731 as base


base.PREDECESSOR_RECORD = 21_712_882
base.PREDECESSOR_DOI = "10.5281/zenodo.21712882"
base.EXPECTED_PREDECESSOR_FILES = 36
base.EXPECTED_PREDECESSOR_BYTES = 2_133_238_113
base.EXPECTED_FINAL_FILES = 38
base.EXPECTED_FINAL_BYTES = 2_946_206_542
base.EXPECTED_SOURCE_IMAGES = 169
base.EXPECTED_ZIP_MEMBERS = 177
base.VERSION = (
    "2026-07-31 EGA IV source-image witnesses for printed pages 128-155 "
    "and 226-281"
)
base.GITHUB_COMMIT = "37e81426edcfe46db309933b5848a9c696862c48"
base.GITHUB_PATH = "sources/ega/visual-evidence"
base.ZIP_ROOT = Path(os.environ["LOCALAPPDATA"]) / "Temp" / (
    "ega4_source_image_witness_p128_281_upload_20260731"
)
base.READBACK_ROOT = Path(os.environ["LOCALAPPDATA"]) / "Temp" / (
    "ega4_source_image_witness_p128_281_readback_20260731"
)
base.PREDECESSOR_RECEIPT = base.RECEIPT_ROOT / (
    "20260731_ega4_source_image_witness_p119_127_p185_225_"
    "record_21712882_public_readback.json"
)
base.RECEIPT_TAG = "20260731_ega4_source_image_witness_p128_155_p226_281"
base.DRAFT_STATE = base.RECEIPT_ROOT / f"{base.RECEIPT_TAG}_zenodo_draft_state.json"
base.NEW_FILES = {
    "89a EGA IV - Source Image Witnesses Printed 128-155 "
    "(600-1800dpi) 20260731.zip": {
        "bytes": 344_895_950,
        "sha256": (
            "646E08EA6AF6ED9B2DBFEAE45A2F7E3AEA04246C0E0B18E28C730CAEB4FB094C"
        ),
        "members": 116,
        "images": 112,
        "uncompressed_bytes": 344_862_242,
    },
    "89b EGA IV - Source Image Witnesses Printed 226-281 "
    "(1800dpi) 20260731.zip": {
        "bytes": 468_072_479,
        "sha256": (
            "257313297CDB9CEF30E07905DB6FFFA7585D3A84123C2661E19D6742C240809A"
        ),
        "members": 61,
        "images": 57,
        "uncompressed_bytes": 468_054_365,
    },
}
base.DESCRIPTION_ADDITION = (
    "<p><strong>EGA IV source-image witnesses for printed pages 128-155 and "
    "226-281:</strong> this successor adds two ZIPs containing 169 actual "
    "scan-derived PNG witnesses from the publicly available NUMDAM EGA IV Part "
    "4 scan already downloadable on this record. Archive 89a provides one "
    "600-dpi full page and three overlapping 1800-dpi bands for each printed "
    "page 128-155. Pages 128-149 are bound to producer checkpoint r36; pages "
    "150-155 are explicitly marked as prepared continuation witnesses. Archive "
    "89b provides one 1800-dpi full page for each printed page 226-281 plus a "
    "targeted formula crop. Pages 226-271 are bound to producer checkpoint r14; "
    "pages 272-281 are prepared continuation witnesses. Actual image coverage "
    "is now continuous on pages 5-155 and 185-281; the remaining page 156-184 "
    "gap is explicit. English-reader screenshots are excluded. Every member has "
    "page, dimensions, resolution, SHA-256, linked TeX, and QA-disposition "
    "metadata.</p>"
)
base.NOTES_ADDITION = (
    "<p>Archives 89a and 89b add actual EGA IV source-scan evidence for printed "
    "pages 128-155 and 226-281. They are not redundant screenshots of the "
    "downloadable English readers. EGA 0 remains the default browser "
    "preview.</p>"
)


if __name__ == "__main__":
    raise SystemExit(base.main())
