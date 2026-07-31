#!/usr/bin/env python3
"""Publish the EGA IV printed 282-332 source-image witness ZIP."""

from __future__ import annotations

import os
from pathlib import Path

import publish_ega4_sections16_18_complete_source_images_zenodo_20260731 as prior


base = prior.base
base.PREDECESSOR_RECORD = 21_714_514
base.PREDECESSOR_DOI = "10.5281/zenodo.21714514"
base.EXPECTED_PREDECESSOR_FILES = 40
base.EXPECTED_PREDECESSOR_BYTES = 3_328_546_146
base.EXPECTED_FINAL_FILES = 41
base.EXPECTED_FINAL_BYTES = 3_729_694_469
base.EXPECTED_SOURCE_IMAGES = 51
base.EXPECTED_ZIP_MEMBERS = 55
base.VERSION = "2026-07-31 EGA IV source-image witnesses through printed page 332"
base.GITHUB_COMMIT = "b7aa17387596ecf5b99b7cf0ac13e95d246106f5"
base.GITHUB_PATH = (
    "sources/ega/visual-evidence/"
    "ega4-sections19-21-source-image-witnesses-printed282-332-20260731"
)
base.ZIP_ROOT = Path(os.environ["LOCALAPPDATA"]) / "Temp" / (
    "ega4_source_image_witness_p282_332_upload_20260731"
)
base.READBACK_ROOT = Path(os.environ["LOCALAPPDATA"]) / "Temp" / (
    "ega4_source_image_witness_p282_332_readback_20260731"
)
base.PREDECESSOR_RECEIPT = base.RECEIPT_ROOT / (
    "20260731_ega4_sections16_18_complete_source_images_p156_184_"
    "record_21714514_public_readback.json"
)
base.RECEIPT_TAG = "20260731_ega4_source_image_witness_p282_332"
base.DRAFT_STATE = base.RECEIPT_ROOT / f"{base.RECEIPT_TAG}_zenodo_draft_state.json"
base.NEW_FILES = {
    "89d EGA IV - Source Image Witnesses Printed 282-332 "
    "(1800dpi) 20260731.zip": {
        "bytes": 401_148_323,
        "sha256": (
            "EA60A76DD4D2B5C50588DCC395EC37E67E5FD387BA82C144D2817BA73B936CFD"
        ),
        "members": 55,
        "images": 51,
        "uncompressed_bytes": 401_132_029,
    }
}
base.DESCRIPTION_ADDITION = (
    "<p><strong>EGA IV source-image witnesses through printed page 332:</strong> "
    "this successor adds one ZIP containing 51 actual scan-derived full-page "
    "PNG witnesses for printed pages 282-332 from the publicly available "
    "NUMDAM EGA IV Part 4 scan already downloadable on this record. Each page "
    "is rendered at 1800 dpi and bound to physical/printed page, dimensions, "
    "SHA-256, linked editable TeX, and QA disposition. The images are source "
    "evidence, not screenshots of an English reader. Together with archives "
    "84-89c, the public source-image surface contains 985 actual images and "
    "covers printed pages 5-332 continuously.</p>"
    "<p>The image archive does not claim that a cumulative EGA IV Sections "
    "1-21 reader has been integrated or independently certified. The direct "
    "cumulative EGA IV reader remains Sections 1-10; archive 02e remains the "
    "separate bounded Sections 16-18 reader.</p>"
)
base.NOTES_ADDITION = (
    "<p>Archive 89d extends the actual high-detail source-scan witness surface "
    "through printed page 332. EGA 0 remains the default browser preview.</p>"
)


if __name__ == "__main__":
    raise SystemExit(base.main())
