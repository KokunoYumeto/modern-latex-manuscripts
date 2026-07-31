#!/usr/bin/env python3
"""Publish EGA IV Sections 16-18 and printed 156-184 source images."""

from __future__ import annotations

import csv
import io
import os
import zipfile
from pathlib import Path

import publish_ega4_source_image_witness_p087_105_zenodo_20260731 as base


base.PREDECESSOR_RECORD = 21_713_359
base.PREDECESSOR_DOI = "10.5281/zenodo.21713359"
base.EXPECTED_PREDECESSOR_FILES = 38
base.EXPECTED_PREDECESSOR_BYTES = 2_946_206_542
base.EXPECTED_FINAL_FILES = 40
base.EXPECTED_FINAL_BYTES = 3_328_546_146
base.EXPECTED_SOURCE_IMAGES = 116
base.EXPECTED_ZIP_MEMBERS = 133
base.VERSION = (
    "2026-07-31 EGA IV Sections 16-18 source-aligned reader and "
    "source-image witnesses through printed page 184"
)
base.GITHUB_COMMIT = "0e6fc5ca7ad4f07a725f25aebdc2978e1beea50c"
base.GITHUB_PATH = "sources/ega"
base.ZIP_ROOT = Path(os.environ["LOCALAPPDATA"]) / "Temp" / (
    "ega4_sections16_18_complete_upload_20260731"
)
base.READBACK_ROOT = Path(os.environ["LOCALAPPDATA"]) / "Temp" / (
    "ega4_sections16_18_complete_readback_20260731"
)
base.PREDECESSOR_RECEIPT = base.RECEIPT_ROOT / (
    "20260731_ega4_source_image_witness_p128_155_p226_281_"
    "record_21713359_public_readback.json"
)
base.RECEIPT_TAG = "20260731_ega4_sections16_18_complete_source_images_p156_184"
base.DRAFT_STATE = base.RECEIPT_ROOT / f"{base.RECEIPT_TAG}_zenodo_draft_state.json"
base.NEW_FILES = {
    "02e_EGAIV_English_Sections16_18_SourceAligned_TeX_PDF_20260731.zip": {
        "bytes": 1_076_881,
        "sha256": (
            "1542D004DE4F7A78D69ABE9046A580F2BC1DE67FAEB46AF05829E00E898DDD48"
        ),
        "members": 13,
        "images": 0,
        "uncompressed_bytes": 1_635_498,
    },
    "89c EGA IV - Source Image Witnesses Printed 156-184 "
    "(600-1800dpi) 20260731.zip": {
        "bytes": 381_262_723,
        "sha256": (
            "7E41AB4239AD4489EE66883D07E25509E71D9126A1261B4E2F7B9F08042CBA48"
        ),
        "members": 120,
        "images": 116,
        "uncompressed_bytes": 381_227_843,
    },
}
base.DESCRIPTION_ADDITION = (
    "<p><strong>EGA IV Sections 16-18 and source-image witnesses through "
    "printed page 184:</strong> this successor adds a self-contained ZIP "
    "with the complete bounded 136-page source-aligned English working reader "
    "for Sections 16-18 and its editable TeX closure. It also adds a separate "
    "ZIP containing 116 actual scan-derived PNG witnesses for printed pages "
    "156-184 from the publicly available NUMDAM EGA IV Part 4 scan already "
    "downloadable on this record: one 600-dpi full page and three overlapping "
    "1800-dpi bands per page. The images are source evidence, not screenshots "
    "of the English reader. Every image has page, dimensions, resolution, "
    "SHA-256, linked TeX, and QA-disposition metadata. Together with the "
    "predecessor archives, actual source-image coverage is continuous from "
    "printed page 5 through page 281.</p>"
    "<p>The Sections 16-18 reader stops before Section 19. It does not claim a "
    "complete cumulative EGA IV reader: Sections 11-15 are not yet integrated "
    "into this source-aligned line, and Sections 19-21 remain active work.</p>"
)
base.NOTES_ADDITION = (
    "<p>Archive 02e provides the bounded Sections 16-18 reader and buildable "
    "TeX. Archive 89c publishes the actual high-detail source-scan evidence for "
    "printed pages 156-184. EGA 0 remains the default browser preview.</p>"
)


def validate_internal_manifest(path: Path, inventory: dict[str, object]) -> None:
    """Verify manifests that use either archive-rooted or root-relative paths."""
    members = inventory["member_identities"]
    manifest_names = [name for name in members if name.endswith("/SHA256SUMS.csv")]
    if len(manifest_names) != 1:
        raise RuntimeError(f"ZIP manifest count changed: {path.name}")
    manifest_name = manifest_names[0]
    root = manifest_name.rsplit("/", 1)[0]
    with zipfile.ZipFile(path) as archive:
        rows = list(
            csv.DictReader(
                io.StringIO(archive.read(manifest_name).decode("utf-8-sig"))
            )
        )
    expected_names = set(members) - {manifest_name}
    observed_names: set[str] = set()
    for row in rows:
        name = row["path"]
        resolved = name if name in expected_names else f"{root}/{name}"
        if resolved not in expected_names:
            raise RuntimeError(f"ZIP manifest path changed: {name}")
        observed = members[resolved]
        expected = (int(row["bytes"]), row["sha256"].upper())
        if (int(observed["bytes"]), str(observed["sha256"])) != expected:
            raise RuntimeError(f"ZIP manifest identity mismatch: {name}")
        observed_names.add(resolved)
    if observed_names != expected_names:
        raise RuntimeError(f"ZIP manifest closure changed: {path.name}")


base.validate_internal_manifest = validate_internal_manifest


if __name__ == "__main__":
    raise SystemExit(base.main())
