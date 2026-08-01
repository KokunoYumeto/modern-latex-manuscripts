#!/usr/bin/env python3
"""Publish Deligne D002 through one exact existing-concept successor."""

from __future__ import annotations

import csv
import io
import json
import zipfile
from pathlib import Path, PurePosixPath

import publish_deligne_d001_zenodo_20260801 as flow


flow.PREDECESSOR_RECORD = 21_744_184
flow.PREDECESSOR_DOI = "10.5281/zenodo.21744184"
flow.PREDECESSOR_FILES = 10
flow.PREDECESSOR_BYTES = 486_525_402
flow.FINAL_FILES = 14
flow.FINAL_BYTES = 488_199_164
flow.PUBLICATION_DATE = "2026-08-01"
flow.VERSION = "2026-08-01 D002 bilingual source-aligned checkpoint"
flow.GITHUB_COMMIT = "2f239cab5df057b99f776da5ffbe273af82cdf0c"
flow.CHECKPOINT_LABEL = "D002"
flow.RECEIPT_STEM = "deligne_d002"
flow.ZIP_ROOT = "Deligne_D002_Bilingual_SourceAligned_20260801"
flow.ZIP_EXPECTED_MEMBERS = 21
flow.INNER_MANIFEST_ROWS = 19
flow.CROP_PATH_PREFIX = "visual_evidence/source_crops/"
flow.CROP_COUNT = 4
flow.DESCRIPTION_PARAGRAPH = (
    "<p><strong>D002 source-aligned checkpoint:</strong> direct bilingual, "
    "English, and corrected-French readers are accompanied by one compact "
    "editable-source and decisive-source-evidence ZIP. The ZIP contains four "
    "tightly bounded source crops used for the page-411, page-413, and "
    "page-415 diagram/formula decisions; its ledger distinguishes the 1200-dpi "
    "source render from enlarged inspection presentation. Full scans, output "
    "screenshots, and raw logs are excluded. This is a complete working edition "
    "of D002 only, not a whole-corpus completion, critical edition, peer review, "
    "certification, or new license grant.</p>"
)

flow.PACKAGE_REL = Path("sources/deligne/d002-bilingual-source-aligned-20260801")
flow.PACKAGE_ROOT = flow.REPO_ROOT / flow.PACKAGE_REL
flow.PUBLIC_ROOT = flow.PACKAGE_ROOT / "public_files"
flow.UPLOAD_MANIFEST = flow.PACKAGE_ROOT / "ZENODO_UPLOAD_MANIFEST.csv"
flow.TEMP_ROOT = flow.REPO_ROOT / "tmp/zenodo/deligne-d002-20260801"
flow.STATE_PATH = flow.TEMP_ROOT / "draft_state.json"
flow.PREPARE_PATH = flow.TEMP_ROOT / "prepare_result.json"

flow.PREDECESSOR_ORDER = [
    flow.DEFAULT_PREVIEW,
    "01_Deligne_Sequential_Cumulative_Papers_001_016p080_French_WorkingDraft.pdf",
    "02_Deligne_English_Paper_and_Letter_PDFs_20260706.zip",
    "03_Deligne_French_Paper_and_Letter_PDFs_20260706.zip",
    "04_Deligne_TeX_Source_QA_and_Update_Packets_20260706.zip",
    "05_Deligne_D001_Bilingual_SourceAligned_Reader_20260801.pdf",
    "06_Deligne_D001_English_SourceAligned_20260801.pdf",
    "07_Deligne_D001_French_SourceAligned_20260801.pdf",
    "08_Deligne_D001_TeX_and_Decisive_Source_Crops_20260801.zip",
    "99_Deligne_Public_Status_NotCritical_20260706.md",
]
flow.NEW_ORDER = [
    "09_Deligne_D002_Bilingual_SourceAligned_Reader_20260801.pdf",
    "10_Deligne_D002_English_SourceAligned_20260801.pdf",
    "11_Deligne_D002_French_SourceAligned_20260801.pdf",
    "12_Deligne_D002_TeX_and_Decisive_Source_Crops_20260801.zip",
]
flow.FINAL_ORDER = flow.PREDECESSOR_ORDER[:9] + flow.NEW_ORDER + flow.PREDECESSOR_ORDER[9:]
flow.EXPECTED_UPLOADS = {
    "09_Deligne_D002_Bilingual_SourceAligned_Reader_20260801.pdf": (
        222_429,
        "F272A0CAEF2853469A4AAEE29C6FF6F066818772364CD1BE0D635B73DAAE5F37",
    ),
    "10_Deligne_D002_English_SourceAligned_20260801.pdf": (
        106_630,
        "BDE6B832859555994F889C0CFDA7642B8D6848A1D4907503B6A52B3A0C3E2C71",
    ),
    "11_Deligne_D002_French_SourceAligned_20260801.pdf": (
        106_349,
        "6DE66CDAD91E61756EA228D48AAD413C8287A8AC2A6B825D7E3B33B90325F345",
    ),
    "12_Deligne_D002_TeX_and_Decisive_Source_Crops_20260801.zip": (
        1_238_354,
        "9F8C04E8467C1008AA1BFF767FE0569CFC75D0426BEEFE06ADDB86EA084AFE0F",
    ),
}


def safe_member(name: str) -> bool:
    pure = PurePosixPath(name)
    return (
        name == name.replace("\\", "/")
        and not pure.is_absolute()
        and ".." not in pure.parts
        and not (len(name) > 1 and name[1] == ":")
    )


def replay_zip(data: bytes) -> dict[str, object]:
    wanted = flow.EXPECTED_UPLOADS[flow.NEW_ORDER[-1]]
    if (len(data), flow.sha256_bytes(data)) != wanted:
        raise RuntimeError("D002 ZIP outer identity changed")
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        infos = [row for row in archive.infolist() if not row.is_dir()]
        names = [row.filename for row in infos]
        if (
            archive.testzip() is not None
            or len(infos) != flow.ZIP_EXPECTED_MEMBERS
            or len(names) != len(set(names))
            or not all(safe_member(name) for name in names)
        ):
            raise RuntimeError("D002 ZIP member boundary changed")
        manifest_name = f"{flow.ZIP_ROOT}/SHA256SUMS.csv"
        rows = list(
            csv.DictReader(io.StringIO(archive.read(manifest_name).decode("utf-8-sig")))
        )
        if len(rows) != flow.INNER_MANIFEST_ROWS:
            raise RuntimeError("D002 inner manifest row boundary changed")
        prefix = f"{flow.ZIP_ROOT}/"
        identities = {}
        for row in rows:
            name = prefix + row["relative_path"]
            payload = archive.read(name)
            observed = (len(payload), flow.sha256_bytes(payload))
            expected = (int(row["bytes"]), row["sha256"].upper())
            if observed != expected:
                raise RuntimeError(f"D002 ZIP member changed: {name}")
            identities[row["relative_path"]] = {
                "bytes": observed[0],
                "sha256": observed[1],
            }
        crops = [name for name in identities if name.startswith(flow.CROP_PATH_PREFIX)]
        if len(crops) != flow.CROP_COUNT:
            raise RuntimeError("D002 decisive source-crop boundary changed")
        return {
            "status": "PASS",
            "members": len(infos),
            "uncompressed_bytes": sum(row.file_size for row in infos),
            "manifest_rows": len(rows),
            "decisive_source_crops": len(crops),
            "member_identities": identities,
        }


flow.replay_zip = replay_zip


if __name__ == "__main__":
    raise SystemExit(flow.main())
