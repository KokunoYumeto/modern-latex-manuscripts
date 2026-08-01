#!/usr/bin/env python3
"""Publish SGA7 II English through Expose XX Section 4.3."""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import io
import json
import shutil
import subprocess
import time
import urllib.parse
import zipfile
from pathlib import Path, PurePosixPath

import publish_sga7ii_expose_xviii_wip_source_zenodo_20260731 as template


base = template.base
prior = template.prior
API = template.API
PUBLICATION_DATE = "2026-08-02"
CONCEPT_DOI = "10.5281/zenodo.20410947"
PREDECESSOR_RECORD = 21_749_057
PREDECESSOR_DOI = "10.5281/zenodo.21749057"
PREDECESSOR_FILES = 85
PREDECESSOR_BYTES = 684_305_261
FINAL_FILES = 87
DEFAULT_PREVIEW = "00a_SGA1_English_Reader.pdf"
OLD_CONTROLS_NAME = "10z_SGA_Current_Release_Controls_20260801_r5.zip"
CONTROLS_NAME = "10z_SGA_Current_Release_Controls_20260802_r6.zip"
VERSION = "2026-08-02 SGA7 II English through Expose XX Section 4.3"

REPO_ROOT = Path(__file__).resolve().parents[1]
PACKAGE_REL = Path(
    "sources/sga/"
    "sga7ii-english-through-expose-xx-4-3-20260802"
)
PACKAGE_ROOT = REPO_ROOT / PACKAGE_REL
IMAGE_PACKAGE_REL = Path(
    "sources/sga/sga7ii-expose-xx-source-audit-images-20260802"
)
IMAGE_PACKAGE_ROOT = REPO_ROOT / IMAGE_PACKAGE_REL
TEMP_ROOT = REPO_ROOT / "tmp/zenodo/sga7ii-english-expose-xx-4-3-20260802"
CONTROLS_ROOT = TEMP_ROOT / "release-controls"
CONTROLS_ZIP = TEMP_ROOT / CONTROLS_NAME
READBACK_ROOT = TEMP_ROOT / "public-readback"
STATE_PATH = TEMP_ROOT / "draft_state.json"
RECEIPT_ROOT = REPO_ROOT / "manifests/published-zenodo"
RECEIPT_TAG = "20260802_sga7ii_english_through_expose_xx_4_3"
PREDECESSOR_RECEIPT = (
    RECEIPT_ROOT
    / "20260801_sga7ii_english_through_xix_complete_record_21749057_public_readback.json"
)
GITHUB_PACKAGE_COMMIT = "880358f6b7e5c93d5b76f8875af34234309fab8f"

PDF_NAME = (
    "00j_SGA7II_English_Through_Expose_XX_4_3_Working_20260802.pdf"
)
SOURCE_ZIP_NAME = (
    "10g3_SGA7II_English_Through_Expose_XX_4_3_"
    "Reader_and_TeX_20260802.zip"
)
OLD_PDF_NAME = (
    "00j_SGA7II_English_Through_Expose_XIX_Complete_Working_20260801.pdf"
)
OLD_SOURCE_ZIP_NAME = (
    "10g3_SGA7II_English_Through_Expose_XIX_Complete_"
    "Reader_and_TeX_20260801.zip"
)
TRANSLATED_IMAGES_NAME = (
    "10h5_SGA7II_ExposeXX_SourceAudit_Images_"
    "idx348_363_Through_4_3_20260802.zip"
)
PREPARATORY_IMAGES_NAME = (
    "10h6_SGA7II_ExposeXX_Preparatory_SourceAudit_Images_"
    "idx364_367_20260802.zip"
)
REPLACED_NAMES = {OLD_CONTROLS_NAME, OLD_PDF_NAME, OLD_SOURCE_ZIP_NAME}

EXPECTED_PACKAGE_FILES = 156
EXPECTED_PACKAGE_BYTES = 3_154_900
EXPECTED_PACKAGE_AGGREGATE = (
    "2DC939C4D544CCA25F325120A47CB4064FA2D8EF157B5D42A9EA79FED698D9F8"
)
EXPECTED_MANIFEST = (
    21_003,
    "235DFD7822529048574296E1559500A33CDC58EB0DAA1668C3F3F97A3948B648",
)
EXPECTED_VALIDATION = (
    2_205,
    "D9E1AC51993C695A6C9AE8DDC1AA4C69C0E00BB0C507434D86936301CA43DD0F",
)
EXPECTED_PDF = (
    1_108_748,
    "BE785D0E6E87122F08254B4E09BED82E16214C8C5E40BDB0B9F15583D7D7E4C8",
)
EXPECTED_SOURCE_ZIP = (
    1_372_720,
    "448D0E6FECE81C17849D6E8D36A41ABFE4D610FC39868DB3A4A9F6EBB2F9B494",
)
EXPECTED_ZIP_MEMBERS = 148
EXPECTED_ZIP_MANIFEST = (
    20_161,
    "C9800E2E2FD147D7AD8272018A4A8E62CF9168A8DF9784FDAC6CE9FD972BF781",
)
EXPECTED_IMAGE_PACKAGE = (
    7,
    43_705_648,
    "103D7343A2024001DB4FCCF113B7B5BB93F92FEBADFD7E628FFC961A2FEC37CF",
)
EXPECTED_IMAGE_MANIFEST = (
    714,
    "268D377BE09C98B903B786067BA27ACE7B083B1F2465F348ED91E83A5A96A672",
)
EXPECTED_IMAGE_VALIDATION = (
    1_807,
    "A04B58088C7D548E0E2BD86323A44CDD813C2A43480F7B9F77D320C492D194D0",
)
EXPECTED_TRANSLATED_IMAGES = (
    32_358_371,
    "40954D6F8C8B16001FAF30AD5F13E0B2EB76203316B967BE22E4B5CC51AA42CF",
    27,
)
EXPECTED_PREPARATORY_IMAGES = (
    11_322_928,
    "433500EA3685423EF1091A63EE6EE7C205B923A60C41B902C3BA3F286D3BEB2F",
    17,
)
EXPECTED_PREDECESSOR_RECEIPT = (
    41_052,
    "80186A4AA021B9D70F9D7727EDE4E9C8C4BCC962E8A9E75D97777AA7685A9CD7",
)
EXPECTED_OLD_CONTROLS = (
    20_254,
    "E1C6E2FA929F4322F0D7961C345EF0780BE9A039B7D8A8E8F558AC40E2889D43",
)

OLD_DESCRIPTION = (
    "<p><strong>Start here:</strong> the first ZIP collects the current complete "
    "English reader PDFs and buildable TeX for SGA 1 through SGA 7 I. The same "
    "PDFs and master TeX files remain direct; SGA1 remains the browser preview. "
    "This is not yet one cross-volume SGA 1-7.2 PDF.</p>"
    "<p><strong>SGA3:</strong> the current cumulative English reader is the clean "
    "1,470-page R29 reader covering the Introduction, Exposes I-XXVI, indexes, "
    "and guide.</p>"
    "<p><strong>SGA7:</strong> SGA7 I has a complete 287-page English working "
    "reader for all written Exposes I, II, VI, VII, VIII, and IX. SGA7 II now "
    "has a direct 203-page English current-progress reader containing complete "
    "Exposes X-XIX through the Expose XIX bibliography, with its exact "
    "buildable TeX in one compact ZIP. The next cursor is the opening of Expose "
    "XX; Exposes XX-XXII are absent. French working "
    "transcriptions remain separately available.</p>"
    "<p>These are working scholarly translations, editions, or transcriptions, "
    "not critical editions, peer review, exhaustive reference certification, "
    "accessibility certification, rights determinations, or mathematical "
    "certification.</p>"
)
DESCRIPTION = (
    "<p><strong>Start here:</strong> the first ZIP collects the current complete "
    "English reader PDFs and buildable TeX for SGA 1 through SGA 7 I. The same "
    "PDFs and master TeX files remain direct; SGA1 remains the browser preview. "
    "This is not yet one cross-volume SGA 1-7.2 PDF.</p>"
    "<p><strong>SGA3:</strong> the current cumulative English reader is the clean "
    "1,470-page R29 reader covering the Introduction, Exposes I-XXVI, indexes, "
    "and guide.</p>"
    "<p><strong>SGA7:</strong> SGA7 I has a complete 287-page English working "
    "reader for all written Exposes I, II, VI, VII, VIII, and IX. SGA7 II now "
    "has a direct 212-page English current-progress reader containing complete "
    "Exposes X-XIX and Expose XX through Section 4.3, with its exact buildable "
    "TeX in one compact ZIP. The next cursor is Expose XX Section 4.4; the "
    "remainder of XX and Exposes XXI-XXII are absent. Two compact source-image "
    "ZIPs preserve the high-resolution pages and targeted crops used for this "
    "checkpoint and prepared for the next unit. French working transcriptions "
    "remain separately available.</p>"
    "<p>These are working scholarly translations, editions, or transcriptions, "
    "not critical editions, peer review, exhaustive reference certification, "
    "accessibility certification, rights determinations, or mathematical "
    "certification.</p>"
)
NOTES = (
    "<p>Reader PDFs contain mathematical text rather than project-status "
    "prefaces. Buildable source, provenance, and release controls are separate "
    "downloads.</p>"
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256_path(path: Path) -> str:
    return base.sha256_path(path)


def md5_path(path: Path) -> str:
    return base.md5_path(path)


def safe_member(name: str) -> bool:
    pure = PurePosixPath(name)
    return (
        name == name.replace("\\", "/")
        and not pure.is_absolute()
        and ".." not in pure.parts
        and not (len(name) > 1 and name[1] == ":")
    )


def package_files() -> list[Path]:
    return sorted(
        (path for path in PACKAGE_ROOT.rglob("*") if path.is_file()),
        key=lambda path: path.relative_to(PACKAGE_ROOT).as_posix().casefold(),
    )


def image_package_files() -> list[Path]:
    return sorted(
        (path for path in IMAGE_PACKAGE_ROOT.rglob("*") if path.is_file()),
        key=lambda path: path.relative_to(IMAGE_PACKAGE_ROOT).as_posix().casefold(),
    )


def package_snapshot(files: list[Path], root: Path = PACKAGE_ROOT) -> tuple[int, int, str]:
    digest = hashlib.sha256()
    for path in files:
        relative = path.relative_to(root).as_posix()
        digest.update(
            f"{relative}\t{path.stat().st_size}\t{sha256_path(path)}\n".encode()
        )
    return (
        len(files),
        sum(path.stat().st_size for path in files),
        digest.hexdigest().upper(),
    )


def replay_image_zip(path: Path, expected_members: int) -> dict[str, object]:
    inventory = prior.zip_inventory(path)
    if int(inventory["members"]) != expected_members:
        raise RuntimeError(f"Source-image ZIP boundary changed: {path.name}")
    return inventory


def replay_source_zip(path: Path) -> dict[str, object]:
    with zipfile.ZipFile(path) as archive:
        infos = [row for row in archive.infolist() if not row.is_dir()]
        names = [row.filename for row in infos]
        if (
            archive.testzip() is not None
            or len(infos) != EXPECTED_ZIP_MEMBERS
            or len(names) != len(set(names))
            or not all(safe_member(name) for name in names)
        ):
            raise RuntimeError("SGA7 II reader/source ZIP boundary changed")
        manifest_data = archive.read("ZIP_MEMBER_SHA256SUMS.csv")
        if (len(manifest_data), sha256_bytes(manifest_data)) != EXPECTED_ZIP_MANIFEST:
            raise RuntimeError("SGA7 II ZIP manifest changed")
        rows = list(
            csv.DictReader(io.StringIO(manifest_data.decode("utf-8-sig")))
        )
        if len(rows) != EXPECTED_ZIP_MEMBERS - 1:
            raise RuntimeError("SGA7 II ZIP manifest row boundary changed")
        info_by_name = {row.filename: row for row in infos}
        identities: dict[str, dict[str, object]] = {}
        for row in rows:
            data = archive.read(row["path"])
            observed = (len(data), sha256_bytes(data))
            wanted = (int(row["bytes"]), row["sha256"].upper())
            if observed != wanted:
                raise RuntimeError(f"SGA7 II ZIP member changed: {row['path']}")
            identities[row["path"]] = {
                "bytes": observed[0],
                "sha256": observed[1],
                "crc32": f"{info_by_name[row['path']].CRC:08X}",
            }
        identities["ZIP_MEMBER_SHA256SUMS.csv"] = {
            "bytes": len(manifest_data),
            "sha256": sha256_bytes(manifest_data),
            "crc32": f"{info_by_name['ZIP_MEMBER_SHA256SUMS.csv'].CRC:08X}",
        }
        return {
            "members": len(infos),
            "uncompressed_bytes": sum(row.file_size for row in infos),
            "member_identities": identities,
            "manifest_rows": len(rows),
            "safe_names": True,
            "crc_errors": 0,
        }


def verify_package() -> dict[str, object]:
    files = package_files()
    if package_snapshot(files) != (
        EXPECTED_PACKAGE_FILES,
        EXPECTED_PACKAGE_BYTES,
        EXPECTED_PACKAGE_AGGREGATE,
    ):
        raise RuntimeError("SGA7 II package boundary changed")
    manifest = PACKAGE_ROOT / "SHA256SUMS.csv"
    validation_path = PACKAGE_ROOT / "PACKAGE_VALIDATION.json"
    if (manifest.stat().st_size, sha256_path(manifest)) != EXPECTED_MANIFEST:
        raise RuntimeError("SGA7 II outer manifest changed")
    if (
        validation_path.stat().st_size,
        sha256_path(validation_path),
    ) != EXPECTED_VALIDATION:
        raise RuntimeError("SGA7 II package validation changed")
    validation = json.loads(validation_path.read_text(encoding="utf-8"))
    if (
        validation.get("status") != "PASS_PUBLIC_WORKING_CHECKPOINT"
        or validation.get("errors")
        or int(validation["reader"]["pages"]) != 212
        or int(validation["source"]["components"]) != 144
        or int(validation["privacy"]["occurrences"]) != 0
    ):
        raise RuntimeError("SGA7 II validation boundary changed")
    rows = list(csv.DictReader(manifest.open("r", encoding="utf-8", newline="")))
    represented = {
        path.relative_to(PACKAGE_ROOT).as_posix(): path
        for path in files
        if path.name != "SHA256SUMS.csv"
    }
    if len(rows) != 155 or {row["path"] for row in rows} != set(represented):
        raise RuntimeError("SGA7 II outer manifest closure changed")
    for row in rows:
        path = represented[row["path"]]
        if (path.stat().st_size, sha256_path(path)) != (
            int(row["bytes"]),
            row["sha256"].upper(),
        ):
            raise RuntimeError(f"SGA7 II package identity changed: {row['path']}")
    pdf = PACKAGE_ROOT / (
        "reader/SGA7II_English_Through_Expose_XX_4_3_20260802.pdf"
    )
    source_zip = PACKAGE_ROOT / (
        "SGA7II_English_Through_Expose_XX_4_3_"
        "Reader_and_TeX_20260802.zip"
    )
    if (pdf.stat().st_size, sha256_path(pdf)) != EXPECTED_PDF:
        raise RuntimeError("SGA7 II reader identity changed")
    if (source_zip.stat().st_size, sha256_path(source_zip)) != EXPECTED_SOURCE_ZIP:
        raise RuntimeError("SGA7 II source ZIP identity changed")
    return {
        "pdf": pdf,
        "source_zip": source_zip,
        "source_zip_inventory": replay_source_zip(source_zip),
    }


def verify_image_package() -> dict[str, object]:
    files = image_package_files()
    if package_snapshot(files, IMAGE_PACKAGE_ROOT) != EXPECTED_IMAGE_PACKAGE:
        raise RuntimeError("SGA7 II source-image package boundary changed")
    manifest = IMAGE_PACKAGE_ROOT / "SHA256SUMS.csv"
    validation_path = IMAGE_PACKAGE_ROOT / "PACKAGE_VALIDATION.json"
    if (manifest.stat().st_size, sha256_path(manifest)) != EXPECTED_IMAGE_MANIFEST:
        raise RuntimeError("SGA7 II source-image manifest changed")
    if (
        validation_path.stat().st_size,
        sha256_path(validation_path),
    ) != EXPECTED_IMAGE_VALIDATION:
        raise RuntimeError("SGA7 II source-image validation changed")
    validation = json.loads(validation_path.read_text(encoding="utf-8"))
    if (
        validation.get("status") != "PASS_PUBLIC_SOURCE_IMAGE_ARCHIVES"
        or validation.get("errors")
        or int(validation.get("images", -1)) != 42
        or int(validation.get("translated_checkpoint_images", -1)) != 26
        or int(validation.get("preparatory_images", -1)) != 16
        or int(validation.get("privacy_hits", -1)) != 0
        or int(validation.get("loose_images", -1)) != 0
    ):
        raise RuntimeError("SGA7 II source-image validation boundary changed")
    rows = list(csv.DictReader(manifest.open("r", encoding="utf-8", newline="")))
    represented = {
        path.relative_to(IMAGE_PACKAGE_ROOT).as_posix(): path
        for path in files
        if path.name != "SHA256SUMS.csv"
    }
    if len(rows) != 6 or {row["path"] for row in rows} != set(represented):
        raise RuntimeError("SGA7 II source-image manifest closure changed")
    for row in rows:
        path = represented[row["path"]]
        if (path.stat().st_size, sha256_path(path)) != (
            int(row["bytes"]),
            row["sha256"].upper(),
        ):
            raise RuntimeError(f"Source-image package identity changed: {row['path']}")
    translated = IMAGE_PACKAGE_ROOT / (
        "SGA7II_ExposeXX_SourceAudit_Images_"
        "idx348_363_Through_4_3_20260802.zip"
    )
    preparatory = IMAGE_PACKAGE_ROOT / (
        "SGA7II_ExposeXX_Preparatory_SourceAudit_Images_"
        "idx364_367_20260802.zip"
    )
    if (translated.stat().st_size, sha256_path(translated)) != EXPECTED_TRANSLATED_IMAGES[:2]:
        raise RuntimeError("Translated-scope source-image ZIP changed")
    if (preparatory.stat().st_size, sha256_path(preparatory)) != EXPECTED_PREPARATORY_IMAGES[:2]:
        raise RuntimeError("Preparatory source-image ZIP changed")
    return {
        "translated": translated,
        "translated_inventory": replay_image_zip(
            translated, EXPECTED_TRANSLATED_IMAGES[2]
        ),
        "preparatory": preparatory,
        "preparatory_inventory": replay_image_zip(
            preparatory, EXPECTED_PREPARATORY_IMAGES[2]
        ),
    }


def local_uploads() -> dict[str, dict[str, object]]:
    verified = verify_package()
    images = verify_image_package()
    paths = {
        PDF_NAME: verified["pdf"],
        SOURCE_ZIP_NAME: verified["source_zip"],
        TRANSLATED_IMAGES_NAME: images["translated"],
        PREPARATORY_IMAGES_NAME: images["preparatory"],
    }
    expected = {
        PDF_NAME: EXPECTED_PDF,
        SOURCE_ZIP_NAME: EXPECTED_SOURCE_ZIP,
        TRANSLATED_IMAGES_NAME: EXPECTED_TRANSLATED_IMAGES[:2],
        PREPARATORY_IMAGES_NAME: EXPECTED_PREPARATORY_IMAGES[:2],
    }
    result: dict[str, dict[str, object]] = {}
    for name, path in paths.items():
        if (path.stat().st_size, sha256_path(path)) != expected[name]:
            raise RuntimeError(f"SGA7 II public object changed: {name}")
        result[name] = {
            "path": path,
            "bytes": path.stat().st_size,
            "sha256": sha256_path(path),
            "md5": md5_path(path),
        }
    result[SOURCE_ZIP_NAME]["inventory"] = verified["source_zip_inventory"]
    result[TRANSLATED_IMAGES_NAME]["inventory"] = images["translated_inventory"]
    result[PREPARATORY_IMAGES_NAME]["inventory"] = images["preparatory_inventory"]
    return result


def load_predecessor(latest_record: int = PREDECESSOR_RECORD) -> dict[str, object]:
    if (
        PREDECESSOR_RECEIPT.stat().st_size,
        sha256_path(PREDECESSOR_RECEIPT),
    ) != EXPECTED_PREDECESSOR_RECEIPT:
        raise RuntimeError("SGA predecessor compact receipt changed")
    compact = json.loads(PREDECESSOR_RECEIPT.read_text(encoding="utf-8"))
    if (
        compact.get("status") != "PASS_PUBLIC_READBACK"
        or compact.get("errors")
        or int(compact.get("record_id", -1)) != PREDECESSOR_RECORD
        or compact.get("doi") != PREDECESSOR_DOI
        or compact.get("concept_doi") != CONCEPT_DOI
        or int(compact.get("outer_files", -1)) != PREDECESSOR_FILES
        or int(compact.get("outer_bytes", -1)) != PREDECESSOR_BYTES
        or compact.get("default_preview") != DEFAULT_PREVIEW
        or compact.get("duplicate_concept_created") is not False
        or compact.get("active_draft_remaining") is not False
    ):
        raise RuntimeError("SGA predecessor public receipt boundary changed")

    session = base.make_session()
    latest = base.check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}/versions/latest?expand=true",
            headers=prior.public_headers(),
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if int(latest["id"]) != latest_record:
        raise RuntimeError("SGA concept head moved before successor preparation")
    record = base.check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}?expand=true",
            headers=prior.public_headers(),
            timeout=(30, 180),
        ),
        {200},
    ).json()
    entries = base.modern_entries(record)
    notes = [
        row.get("description", "")
        for row in record["metadata"].get("additional_descriptions", [])
        if row.get("type", {}).get("id") == "notes"
    ]
    if (
        not record.get("is_published")
        or record["pids"]["doi"]["identifier"] != PREDECESSOR_DOI
        or record["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI
        or len(entries) != PREDECESSOR_FILES
        or sum(int(row["size"]) for row in entries.values()) != PREDECESSOR_BYTES
        or record["files"].get("default_preview") != DEFAULT_PREVIEW
        or record["metadata"].get("version") != compact.get("version")
        or record["metadata"].get("description", "").strip() != OLD_DESCRIPTION
        or notes != [NOTES]
    ):
        raise RuntimeError("Live SGA predecessor boundary changed")

    receipt_files = compact.get("outer_file_readback", {})
    if set(receipt_files) != set(entries):
        raise RuntimeError("SGA predecessor public receipt does not close")
    files: dict[str, dict[str, object]] = {}
    for name, entry in entries.items():
        row = receipt_files[name]
        observed = (
            int(entry["size"]),
            base.normalized_md5(entry["checksum"]),
        )
        wanted = (int(row["bytes"]), str(row["md5"]).lower())
        if observed != wanted or row.get("match") is not True:
            raise RuntimeError(f"SGA predecessor identity changed: {name}")
        files[name] = {
            "bytes": int(row["bytes"]),
            "sha256": str(row["sha256"]).upper(),
            "md5": observed[1],
            "content_url": entry["links"]["content"],
            "match": True,
        }

    controls_data = base.check(
        session.get(entries[OLD_CONTROLS_NAME]["links"]["content"], timeout=(30, 300)),
        {200},
    ).content
    if (len(controls_data), sha256_bytes(controls_data)) != EXPECTED_OLD_CONTROLS:
        raise RuntimeError("Current SGA release controls changed")
    with zipfile.ZipFile(io.BytesIO(controls_data)) as archive:
        if archive.testzip() is not None:
            raise RuntimeError("Current SGA release controls failed CRC")
        rows = list(
            csv.DictReader(
                io.StringIO(
                    archive.read("09a_RELEASE_FILE_MANIFEST.csv").decode("utf-8")
                )
            )
        )
    controls_manifest = {
        row["filename"]: (int(row["bytes"]), row["sha256"].upper())
        for row in rows
    }
    expected_control_names = set(entries) - {OLD_CONTROLS_NAME}
    if len(rows) != 84 or set(controls_manifest) != expected_control_names:
        raise RuntimeError("Current SGA release manifest boundary changed")
    for name in expected_control_names:
        row = files[name]
        if controls_manifest[name] != (int(row["bytes"]), str(row["sha256"]).upper()):
            raise RuntimeError(f"Current SGA control identity changed: {name}")
    return {
        "status": "PASS_PUBLIC_READBACK",
        "errors": [],
        "record_id": PREDECESSOR_RECORD,
        "doi": PREDECESSOR_DOI,
        "concept_doi": CONCEPT_DOI,
        "outer_files": len(files),
        "outer_bytes": sum(int(row["bytes"]) for row in files.values()),
        "outer_file_readback": files,
        "default_preview": DEFAULT_PREVIEW,
        "version": record["metadata"]["version"],
        "active_draft_remaining": False,
    }


def expected_retained(predecessor: dict[str, object]) -> dict[str, dict[str, object]]:
    return {
        name: row
        for name, row in predecessor["outer_file_readback"].items()
        if name not in REPLACED_NAMES
    }


def verify_github() -> dict[str, object]:
    subprocess.check_call(
        ["git", "fetch", "--no-tags", "github-write", "main"],
        cwd=REPO_ROOT,
    )
    remote = subprocess.check_output(
        ["git", "ls-remote", "github-write", "refs/heads/main"],
        cwd=REPO_ROOT,
        text=True,
    ).split()[0]
    subprocess.check_call(
        ["git", "merge-base", "--is-ancestor", GITHUB_PACKAGE_COMMIT, remote],
        cwd=REPO_ROOT,
    )
    session = base.make_session()
    readback: dict[str, dict[str, object]] = {}
    for package_root, package_rel, files in (
        (PACKAGE_ROOT, PACKAGE_REL, package_files()),
        (IMAGE_PACKAGE_ROOT, IMAGE_PACKAGE_REL, image_package_files()),
    ):
        root = (
            "https://raw.githubusercontent.com/KokunoYumeto/"
            f"modern-latex-manuscripts/{GITHUB_PACKAGE_COMMIT}/"
            f"{package_rel.as_posix()}"
        )
        for path in files:
            relative = path.relative_to(package_root).as_posix()
            public_path = f"{package_rel.as_posix()}/{relative}"
            url = f"{root}/{urllib.parse.quote(relative, safe='/')}"
            data = base.check(session.get(url, timeout=(30, 300)), {200}).content
            observed = (len(data), sha256_bytes(data))
            wanted = (path.stat().st_size, sha256_path(path))
            if observed != wanted:
                raise RuntimeError(f"GitHub SGA7 II readback changed: {public_path}")
            readback[public_path] = {
                "bytes": observed[0],
                "sha256": observed[1],
                "url": url,
                "match": True,
            }
    return {
        "status": "PASS_GITHUB_PUBLIC_READBACK",
        "errors": [],
        "commit": GITHUB_PACKAGE_COMMIT,
        "public_main": remote,
        "package_path": PACKAGE_REL.as_posix(),
        "package_paths": [PACKAGE_REL.as_posix(), IMAGE_PACKAGE_REL.as_posix()],
        "files_read_back": len(readback),
        "bytes_read_back": sum(int(row["bytes"]) for row in readback.values()),
        "file_readback": readback,
    }


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def build_controls(
    local: dict[str, dict[str, object]],
    predecessor: dict[str, object],
    github: dict[str, object],
) -> dict[str, object]:
    resolved = TEMP_ROOT.resolve()
    if not resolved.is_relative_to((REPO_ROOT / "tmp").resolve()):
        raise RuntimeError("Refusing release controls outside repository tmp")
    shutil.rmtree(CONTROLS_ROOT, ignore_errors=True)
    CONTROLS_ROOT.mkdir(parents=True)
    retained = expected_retained(predecessor)
    (CONTROLS_ROOT / "09_README_CURRENT_RELEASE.md").write_text(
        """# Current SGA release controls

The leading complete-reader bundle and SGA1 browser preview remain unchanged.
This successor adds a direct 212-page SGA7 II English current-progress reader
and one compact ZIP containing that reader plus its exact 144-component
buildable TeX closure. Two additional compact ZIPs preserve the high-detail
source pages and targeted crops used through Section 4.3 and prepared for the
next Section 4.4 unit.

The 212-page reader contains complete Exposes X-XIX and Expose XX through
Section 4.3. The next cursor is Expose XX Section 4.4; the remainder of Expose
XX and Exposes XXI-XXII are absent. The preparatory image archive makes no
translation claim. The reader is not represented as complete SGA7 II
or as exhaustively cross-referenced.
""",
        encoding="utf-8",
        newline="\n",
    )
    roles = {
        PDF_NAME: "direct_current_progress_english_reader",
        SOURCE_ZIP_NAME: "compact_reader_and_buildable_tex_archive",
        TRANSLATED_IMAGES_NAME: "translated_scope_high_resolution_source_images",
        PREPARATORY_IMAGES_NAME: "preparatory_high_resolution_source_images",
    }
    rows = [
        {
            "filename": name,
            "bytes": int(row["bytes"]),
            "sha256": str(row["sha256"]).upper(),
            "release_role": "retained_predecessor_file",
            "source": f"zenodo_record_{PREDECESSOR_RECORD}",
        }
        for name, row in retained.items()
    ]
    for name, row in local.items():
        rows.append(
            {
                "filename": name,
                "bytes": int(row["bytes"]),
                "sha256": str(row["sha256"]).upper(),
                "release_role": roles[name],
                "source": (
                    IMAGE_PACKAGE_REL.as_posix()
                    if name in {TRANSLATED_IMAGES_NAME, PREPARATORY_IMAGES_NAME}
                    else PACKAGE_REL.as_posix()
                ),
            }
        )
    rows.sort(key=lambda row: str(row["filename"]).casefold())
    write_csv(
        CONTROLS_ROOT / "09a_RELEASE_FILE_MANIFEST.csv",
        rows,
        ["filename", "bytes", "sha256", "release_role", "source"],
    )
    base.save_json(
        CONTROLS_ROOT / "09b_RELEASE_VALIDATION.json",
        {
            "status": "PASS_PREPARED_RELEASE_CONTROLS",
            "errors": [],
            "concept_doi": CONCEPT_DOI,
            "predecessor_record": PREDECESSOR_RECORD,
            "retained_predecessor_files": len(retained),
            "added_files": len(local),
            "replaced_files": sorted(REPLACED_NAMES),
            "expected_outer_files_including_controls": FINAL_FILES,
            "default_preview": DEFAULT_PREVIEW,
            "github": {
                "commit": github["commit"],
                "package_path": github["package_path"],
                "files_read_back": github["files_read_back"],
                "bytes_read_back": github["bytes_read_back"],
            },
            "reader_pages": 212,
            "reader_sha256": EXPECTED_PDF[1],
            "editable_tex_files": 145,
            "component_files": 144,
            "source_zip_members": EXPECTED_ZIP_MEMBERS,
            "translated_source_images": 26,
            "preparatory_source_images": 16,
            "complete_sga7ii_claim": False,
            "exhaustive_reference_claim": False,
            "reader_process_preface_pages": 0,
        },
    )
    copies = {
        "09c_SGA7II_PACKAGE_VALIDATION.json": PACKAGE_ROOT
        / "PACKAGE_VALIDATION.json",
        "09d_SGA7II_PACKAGE_SHA256SUMS.csv": PACKAGE_ROOT / "SHA256SUMS.csv",
        "09e_SGA7II_ZENODO_UPLOAD_MANIFEST.csv": PACKAGE_ROOT
        / "ZENODO_UPLOAD_MANIFEST.csv",
        "09f_SGA7II_BUILD_AND_QA_SUMMARY.md": PACKAGE_ROOT
        / "BUILD_AND_QA_SUMMARY.md",
        "09g_SGA7II_FINAL_VISUAL_QA.md": PACKAGE_ROOT / "FINAL_VISUAL_QA.md",
        "09h_SGA7II_RIGHTS_AND_PROVENANCE.md": PACKAGE_ROOT
        / "RIGHTS_AND_PROVENANCE.md",
        "09k_SGA7II_SOURCE_IMAGE_PACKAGE_VALIDATION.json": IMAGE_PACKAGE_ROOT
        / "PACKAGE_VALIDATION.json",
        "09l_SGA7II_SOURCE_IMAGE_INDEX.csv": IMAGE_PACKAGE_ROOT
        / "VISUAL_EVIDENCE_INDEX.csv",
        "09m_SGA7II_SOURCE_IMAGE_SHA256SUMS.csv": IMAGE_PACKAGE_ROOT
        / "SHA256SUMS.csv",
        "09n_SGA7II_SOURCE_IMAGE_RIGHTS_AND_PROVENANCE.md": IMAGE_PACKAGE_ROOT
        / "RIGHTS_AND_PROVENANCE.md",
    }
    for name, source in copies.items():
        shutil.copyfile(source, CONTROLS_ROOT / name)
    base.save_json(
        CONTROLS_ROOT / "09i_SGA7II_GITHUB_PUBLIC_READBACK_SUMMARY.json",
        {
            "status": github["status"],
            "errors": github["errors"],
            "commit": github["commit"],
            "public_main": github["public_main"],
            "package_path": github["package_path"],
            "files_read_back": github["files_read_back"],
            "bytes_read_back": github["bytes_read_back"],
        },
    )
    inventory = local[SOURCE_ZIP_NAME]["inventory"]
    base.save_json(
        CONTROLS_ROOT / "09j_SGA7II_SOURCE_ZIP_VALIDATION.json",
        {
            "status": "PASS",
            "errors": [],
            "filename": SOURCE_ZIP_NAME,
            "bytes": local[SOURCE_ZIP_NAME]["bytes"],
            "sha256": local[SOURCE_ZIP_NAME]["sha256"],
            "members": inventory["members"],
            "uncompressed_bytes": inventory["uncompressed_bytes"],
            "member_readback": "148/148 exact",
        },
    )
    for control_name, upload_name in (
        ("09o_SGA7II_TRANSLATED_SOURCE_IMAGES_VALIDATION.json", TRANSLATED_IMAGES_NAME),
        ("09p_SGA7II_PREPARATORY_SOURCE_IMAGES_VALIDATION.json", PREPARATORY_IMAGES_NAME),
    ):
        image_inventory = local[upload_name]["inventory"]
        base.save_json(
            CONTROLS_ROOT / control_name,
            {
                "status": "PASS",
                "errors": [],
                "filename": upload_name,
                "bytes": local[upload_name]["bytes"],
                "sha256": local[upload_name]["sha256"],
                "members": image_inventory["members"],
                "uncompressed_bytes": image_inventory["uncompressed_bytes"],
                "member_readback": f"{image_inventory['members']}/{image_inventory['members']} exact",
            },
        )
    packed = [
        {
            "filename": path.name,
            "bytes": path.stat().st_size,
            "sha256": sha256_path(path),
        }
        for path in sorted(CONTROLS_ROOT.iterdir(), key=lambda path: path.name.casefold())
    ]
    write_csv(
        CONTROLS_ROOT / "PACKED_CONTROL_SHA256.csv",
        packed,
        ["filename", "bytes", "sha256"],
    )
    CONTROLS_ZIP.parent.mkdir(parents=True, exist_ok=True)
    CONTROLS_ZIP.unlink(missing_ok=True)
    with zipfile.ZipFile(
        CONTROLS_ZIP,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
        allowZip64=True,
    ) as archive:
        for path in sorted(CONTROLS_ROOT.iterdir(), key=lambda path: path.name.casefold()):
            info = zipfile.ZipInfo(path.name, date_time=(2026, 8, 2, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            info.create_system = 3
            archive.writestr(info, path.read_bytes(), compresslevel=9)
    controls_inventory = prior.zip_inventory(CONTROLS_ZIP)
    return {
        "path": CONTROLS_ZIP,
        "bytes": CONTROLS_ZIP.stat().st_size,
        "sha256": sha256_path(CONTROLS_ZIP),
        "md5": md5_path(CONTROLS_ZIP),
        "inventory": controls_inventory,
    }


def ordered_names(names: set[str]) -> list[str]:
    bundle = "00_Current_SGA1-7_English_Readers_and_Buildable_TeX_20260801.zip"
    english = [
        "00a_SGA1_English_Reader.pdf",
        "00b_SGA2_English_Reader.pdf",
        "00c_SGA3_English_Reader.pdf",
        "00d_SGA4_English_Reader.pdf",
        "00e_SGA5_English_Reader.pdf",
        "00f_SGA6_English_Reader.pdf",
        "00i_SGA7I_English_Complete_Working_Reader_20260801.pdf",
        PDF_NAME,
    ]
    french = [
        "00g_SGA7I_Fresh_Source_Transcription_Complete_Working.pdf",
        "00h_SGA7II_French_Source_Transcription_Working_X-XXI_Partial_20260731.pdf",
        "01e_SGA5_French_Reader.pdf",
        "01f_SGA6_French_Reader.pdf",
    ]
    english_tex = [
        "02a_SGA1_English_Master.tex",
        "02b_SGA2_English_Master.tex",
        "02c_SGA3_English_Master.tex",
        "02d_SGA4_English_Master.tex",
        "02e_SGA5_English_Master.tex",
        "02f_SGA6_English_Master.tex",
        "02i_SGA7I_English_Complete_Working_Master_20260801.tex",
    ]
    french_tex = [
        "02g_SGA7I_Fresh_Source_Transcription_Complete_Working.tex",
        "02h_SGA7II_French_Source_Transcription_Working_X-XXI_Partial_20260731.tex",
        "03e_SGA5_French_Master.tex",
        "03f_SGA6_French_Master.tex",
    ]
    preferred = [bundle, *english, *french, *english_tex, *french_tex]
    if not set(preferred).issubset(names):
        raise RuntimeError(
            f"Direct SGA shelf changed: {sorted(set(preferred) - names)}"
        )
    remainder = names - set(preferred)
    other_pdfs = sorted(
        (name for name in remainder if name.lower().endswith(".pdf")),
        key=str.casefold,
    )
    other_tex = sorted(
        (name for name in remainder if name.lower().endswith(".tex")),
        key=str.casefold,
    )
    archives = sorted(remainder - set(other_pdfs) - set(other_tex), key=str.casefold)
    return [*preferred, *other_pdfs, *other_tex, *archives]


def configure_prior() -> None:
    prior.PUBLICATION_DATE = PUBLICATION_DATE
    prior.CONCEPT_DOI = CONCEPT_DOI
    prior.PREDECESSOR_RECORD = PREDECESSOR_RECORD
    prior.PREDECESSOR_DOI = PREDECESSOR_DOI
    prior.PREDECESSOR_FILES = PREDECESSOR_FILES
    prior.PREDECESSOR_BYTES = PREDECESSOR_BYTES
    prior.FINAL_FILES = FINAL_FILES
    prior.DEFAULT_PREVIEW = DEFAULT_PREVIEW
    prior.CONTROLS_NAME = CONTROLS_NAME
    prior.VERSION = VERSION
    prior.TEMP_ROOT = TEMP_ROOT
    prior.CONTROLS_ROOT = CONTROLS_ROOT
    prior.CONTROLS_ZIP = CONTROLS_ZIP
    prior.READBACK_ROOT = READBACK_ROOT
    prior.STATE_PATH = STATE_PATH
    prior.RECEIPT_ROOT = RECEIPT_ROOT
    prior.RECEIPT_TAG = RECEIPT_TAG
    prior.PREDECESSOR_RECEIPT = PREDECESSOR_RECEIPT
    prior.REPLACED_NAMES = REPLACED_NAMES
    prior.OLD_DESCRIPTION_ADDITION = OLD_DESCRIPTION
    prior.OLD_NOTES_ADDITION = NOTES
    prior.DESCRIPTION_ADDITION = DESCRIPTION
    prior.NOTES_ADDITION = NOTES
    prior.PDF_NAME = PDF_NAME
    prior.TEX_NAME = "02j_SGA7II_English_Master_Not_Directly_Released.tex"
    prior.SOURCE_ZIP_NAME = SOURCE_ZIP_NAME
    prior.expected_retained = expected_retained
    prior.ordered_names = ordered_names


def ensure_subject(session, token: str, draft_id: int) -> None:
    headers = prior.auth_headers(token)
    draft = base.check(
        session.get(
            f"{API}/records/{draft_id}/draft?expand=true",
            headers=headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    metadata = copy.deepcopy(draft["metadata"])
    subjects = metadata.setdefault("subjects", [])
    existing = {row.get("subject") for row in subjects}
    if "SGA7 II English translation" not in existing:
        subjects.append({"subject": "SGA7 II English translation"})
    payload = {
        "access": draft["access"],
        "files": {
            "enabled": True,
            "default_preview": draft["files"].get("default_preview"),
            "order": draft["files"].get("order", []),
        },
        "metadata": metadata,
        "custom_fields": draft.get("custom_fields", {}),
    }
    if draft.get("pids"):
        payload["pids"] = draft["pids"]
    base.check(
        session.put(
            f"{API}/records/{draft_id}/draft",
            headers={**headers, "Content-Type": "application/json"},
            json=payload,
            timeout=(30, 300),
        ),
        {200},
    )


def resumable_predecessor(
    session,
    token: str,
    draft_id: int,
    predecessor: dict[str, object],
    local: dict[str, dict[str, object]],
    controls: dict[str, object],
) -> dict[str, object]:
    """Adapt the inherited-file boundary after an interrupted staged upload."""
    deposition = base.check(
        session.get(
            f"{API}/deposit/depositions/{draft_id}",
            headers={"Authorization": f"Bearer {token}"},
            timeout=(30, 180),
        ),
        {200},
    ).json()
    files = base.legacy_entries(deposition)
    predecessor_files = predecessor["outer_file_readback"]
    full_names = set(predecessor_files)
    retained = expected_retained(predecessor)
    allowed = full_names | set(local) | {CONTROLS_NAME}
    current_names = set(files)

    if not set(retained).issubset(current_names):
        raise RuntimeError("Interrupted SGA draft lost a retained predecessor file")
    if not current_names.issubset(allowed):
        raise RuntimeError("Interrupted SGA draft contains an unexpected file")
    if not (full_names - current_names).issubset(REPLACED_NAMES):
        raise RuntimeError("Interrupted SGA draft lost an unreplaced predecessor file")

    staged_uploads = {**local, CONTROLS_NAME: controls}
    for name in current_names & set(staged_uploads):
        observed = (
            int(files[name]["filesize"]),
            base.normalized_md5(files[name]["checksum"]),
        )
        wanted = (
            int(staged_uploads[name]["bytes"]),
            str(staged_uploads[name]["md5"]).lower(),
        )
        if observed != wanted:
            raise RuntimeError(f"Interrupted SGA staged identity changed: {name}")

    if full_names.issubset(current_names):
        return predecessor
    if CONTROLS_NAME in current_names:
        raise RuntimeError(
            "Interrupted SGA draft already staged controls; manual replay required"
        )

    resumed = copy.deepcopy(predecessor)
    resumed["outer_file_readback"] = {
        name: predecessor_files[name] for name in retained
    }
    return resumed


def public_readback(
    session,
    token: str,
    record_id: int,
    local: dict[str, dict[str, object]],
    controls: dict[str, object],
    predecessor: dict[str, object],
    github: dict[str, object],
) -> dict[str, object]:
    record = None
    for _ in range(120):
        response = session.get(
            f"{API}/records/{record_id}?expand=true",
            headers=prior.public_headers(),
            timeout=(30, 180),
        )
        if response.status_code == 200 and response.json().get("is_published"):
            record = response.json()
            break
        time.sleep(2)
    if record is None:
        raise RuntimeError("Published SGA successor did not become public")
    retained = expected_retained(predecessor)
    expected = {**retained, **local, CONTROLS_NAME: controls}
    entries = base.modern_entries(record)
    latest = base.check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}/versions/latest?expand=true",
            headers=prior.public_headers(),
            timeout=(30, 180),
        ),
        {200},
    ).json()
    notes = [
        row.get("description", "")
        for row in record["metadata"].get("additional_descriptions", [])
        if row.get("type", {}).get("id") == "notes"
    ]
    if (
        set(entries) != set(expected)
        or len(entries) != FINAL_FILES
        or record["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI
        or record["files"].get("default_preview") != DEFAULT_PREVIEW
        or record["metadata"].get("version") != VERSION
        or record["metadata"].get("description", "").strip() != DESCRIPTION
        or notes != [NOTES]
        or int(latest["id"]) != record_id
    ):
        raise RuntimeError("Public SGA successor boundary changed")

    resolved = READBACK_ROOT.resolve()
    if not resolved.is_relative_to((REPO_ROOT / "tmp").resolve()):
        raise RuntimeError("Refusing public readback outside repository tmp")
    shutil.rmtree(READBACK_ROOT, ignore_errors=True)
    READBACK_ROOT.mkdir(parents=True)
    files: dict[str, dict[str, object]] = {}
    archives: dict[str, dict[str, object]] = {}
    try:
        for index, name in enumerate(sorted(entries, key=str.casefold), start=1):
            print(f"PUBLIC READBACK {index}/{len(entries)} {name}", flush=True)
            destination = (
                READBACK_ROOT / f"archive-{index:03d}.zip"
                if name
                in {
                    SOURCE_ZIP_NAME,
                    TRANSLATED_IMAGES_NAME,
                    PREPARATORY_IMAGES_NAME,
                    CONTROLS_NAME,
                }
                else None
            )
            observed = prior.stream_download(
                session, entries[name]["links"]["content"], destination
            )
            wanted = (
                int(expected[name]["bytes"]),
                str(expected[name]["sha256"]).upper(),
                str(expected[name]["md5"]).lower(),
            )
            if observed != wanted:
                raise RuntimeError(f"Public SGA mismatch: {name}")
            files[name] = {
                "bytes": observed[0],
                "sha256": observed[1],
                "md5": observed[2],
                "content_url": entries[name]["links"]["content"],
                "match": True,
                "readback_mode": "anonymous_full_download_exact_sha256",
            }
            if destination is not None:
                inventory = prior.zip_inventory(destination)
                if (
                    inventory["member_identities"]
                    != expected[name]["inventory"]["member_identities"]
                ):
                    raise RuntimeError(f"Public ZIP member drift: {name}")
                inventory["match"] = True
                archives[name] = inventory
    finally:
        shutil.rmtree(READBACK_ROOT, ignore_errors=True)
    retained_errors = [
        name
        for name in retained
        if files[name]["sha256"] != str(retained[name]["sha256"]).upper()
    ]
    if (
        len(files) != FINAL_FILES
        or retained_errors
        or int(archives[SOURCE_ZIP_NAME]["members"]) != EXPECTED_ZIP_MEMBERS
        or int(archives[TRANSLATED_IMAGES_NAME]["members"])
        != EXPECTED_TRANSLATED_IMAGES[2]
        or int(archives[PREPARATORY_IMAGES_NAME]["members"])
        != EXPECTED_PREPARATORY_IMAGES[2]
    ):
        raise RuntimeError("SGA public readback did not close")
    prior.assert_no_open_draft(session, token, record_id)
    result = {
        "status": "PASS_PUBLIC_READBACK",
        "errors": [],
        "record_id": record_id,
        "record_url": record["links"]["self_html"],
        "doi": record["pids"]["doi"]["identifier"],
        "concept_doi": CONCEPT_DOI,
        "predecessor_record": PREDECESSOR_RECORD,
        "version": VERSION,
        "outer_files": len(files),
        "outer_bytes": sum(int(row["bytes"]) for row in files.values()),
        "outer_file_readback": files,
        "retained_predecessor_files": len(retained),
        "retained_predecessor_identity_errors": retained_errors,
        "replaced_files": sorted(REPLACED_NAMES),
        "added_files": sorted(local),
        "default_preview": record["files"].get("default_preview"),
        "latest_record": int(latest["id"]),
        "github": {
            "commit": github["commit"],
            "package_path": github["package_path"],
            "files_read_back": github["files_read_back"],
            "bytes_read_back": github["bytes_read_back"],
        },
        "reader_pages": 212,
        "reader_sha256": EXPECTED_PDF[1],
        "source_zip_members": EXPECTED_ZIP_MEMBERS,
        "translated_source_image_zip_members": EXPECTED_TRANSLATED_IMAGES[2],
        "preparatory_source_image_zip_members": EXPECTED_PREPARATORY_IMAGES[2],
        "scope": (
            "SGA7 II Exposes X-XIX complete and Expose XX through Section 4.3"
        ),
        "complete_sga7ii_claim": False,
        "exhaustive_reference_claim": False,
        "duplicate_concept_created": False,
        "active_draft_remaining": False,
    }
    zip_result = {
        "status": "PASS",
        "errors": [],
        "record_id": record_id,
        "doi": result["doi"],
        "zip_archive_count": len(archives),
        "zip_member_count": sum(int(row["members"]) for row in archives.values()),
        "archives": archives,
    }
    base.save_json(
        RECEIPT_ROOT / f"{RECEIPT_TAG}_record_{record_id}_public_readback.json",
        result,
    )
    base.save_json(
        RECEIPT_ROOT / f"{RECEIPT_TAG}_record_{record_id}_zip_member_readback.json",
        zip_result,
    )
    (RECEIPT_ROOT / f"{RECEIPT_TAG}_record_{record_id}.md").write_text(
        "\n".join(
            [
                "# SGA7 II English current-progress publication receipt",
                "",
                f"- Record: <https://zenodo.org/records/{record_id}>",
                f"- DOI: `{result['doi']}`",
                f"- Concept DOI: `{CONCEPT_DOI}`",
                f"- GitHub package commit: `{GITHUB_PACKAGE_COMMIT}`",
                f"- Public files: {len(files)} / {result['outer_bytes']:,} bytes",
                f"- Retained predecessor files: {len(retained)} / identity errors 0",
                f"- Reader: 212 pages / SHA-256 `{EXPECTED_PDF[1]}`",
                f"- Reader/source ZIP: 148 members / SHA-256 `{EXPECTED_SOURCE_ZIP[1]}`",
                f"- Translated-scope source images: 27 ZIP members / SHA-256 `{EXPECTED_TRANSLATED_IMAGES[1]}`",
                f"- Preparatory source images: 17 ZIP members / SHA-256 `{EXPECTED_PREPARATORY_IMAGES[1]}`",
                "- Scope: Exposes X-XIX complete and Expose XX through Section 4.3",
                "- Next cursor Expose XX Section 4.4; no exhaustive-reference claim",
                f"- Default preview: `{DEFAULT_PREVIEW}`",
                "- Duplicate concept created: no",
                "- Active draft remaining: no",
                "",
            ]
        ),
        encoding="utf-8",
        newline="\n",
    )
    return result


def prepare(latest_record: int = PREDECESSOR_RECORD) -> tuple[
    dict[str, dict[str, object]],
    dict[str, object],
    dict[str, object],
    dict[str, object],
]:
    configure_prior()
    local = local_uploads()
    predecessor = load_predecessor(latest_record)
    github = verify_github()
    controls = build_controls(local, predecessor, github)
    return local, predecessor, github, controls


def preflight() -> dict[str, object]:
    local, predecessor, github, controls = prepare()
    token = base.find_token()
    session = base.make_session()
    prior.fetch_live(session, predecessor)
    prior.assert_no_untracked_draft(session, token)
    return {
        "status": "PASS_PREFLIGHT",
        "predecessor_record": PREDECESSOR_RECORD,
        "concept_doi": CONCEPT_DOI,
        "retained_files": len(expected_retained(predecessor)),
        "replaced_files": sorted(REPLACED_NAMES),
        "added_files": sorted(local),
        "final_files": FINAL_FILES,
        "default_preview": DEFAULT_PREVIEW,
        "github_commit": github["commit"],
        "uploads": {
            name: {"bytes": row["bytes"], "sha256": row["sha256"]}
            for name, row in local.items()
        },
        "controls_zip": {
            "bytes": controls["bytes"],
            "sha256": controls["sha256"],
            "members": controls["inventory"]["members"],
        },
        "duplicate_concept_created": False,
    }


def publish() -> dict[str, object]:
    local, predecessor, github, controls = prepare()
    token = base.find_token()
    session = base.make_session()
    live = prior.fetch_live(session, predecessor)
    prior.assert_no_untracked_draft(session, token)
    draft_id = prior.create_or_resume_draft(session, token, live)
    ensure_subject(session, token, draft_id)
    staged_predecessor = resumable_predecessor(
        session,
        token,
        draft_id,
        predecessor,
        local,
        controls,
    )
    published = prior.stage_and_publish(
        session,
        token,
        live,
        draft_id,
        local,
        controls,
        staged_predecessor,
    )
    return public_readback(
        session,
        token,
        int(published["id"]),
        local,
        controls,
        predecessor,
        github,
    )


def readback(record_id: int) -> dict[str, object]:
    local, predecessor, github, controls = prepare(record_id)
    token = base.find_token()
    session = base.make_session()
    return public_readback(
        session,
        token,
        record_id,
        local,
        controls,
        predecessor,
        github,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--preflight", action="store_true")
    parser.add_argument("--readback-record", type=int)
    args = parser.parse_args()
    if args.preflight and args.readback_record is not None:
        parser.error("--preflight and --readback-record are mutually exclusive")
    if args.preflight:
        result = preflight()
    elif args.readback_record is not None:
        result = readback(args.readback_record)
    else:
        result = publish()
    print(json.dumps(result, indent=2, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
