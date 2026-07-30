#!/usr/bin/env python3
"""Publish and read back the EGA IV Sections 1-10 working reader."""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import importlib.util
import io
import json
import os
import sys
import zipfile
from pathlib import Path, PurePosixPath
from urllib.parse import quote


SCRIPT_DIR = Path(__file__).resolve().parent
PREVIOUS_PATH = (
    SCRIPT_DIR / "publish_ega2_complete_source_aligned_zenodo_20260730.py"
)
SPEC = importlib.util.spec_from_file_location(
    "ega2_complete_publisher",
    PREVIOUS_PATH,
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load the established EGA publication workflow")
previous = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = previous
SPEC.loader.exec_module(previous)

base = previous.base
pipeline = previous.pipeline
API = previous.API
CONCEPT_DOI = "10.5281/zenodo.20414353"
PREDECESSOR_RECORD = 21_696_776
PREDECESSOR_DOI = "10.5281/zenodo.21696776"
PUBLICATION_DATE = "2026-07-30"
VERSION = "2026-07-30 EGA IV Sections 1-10 source-aligned working reader"
TITLE = previous.TITLE

GITHUB_COMMIT = "f96d11509e0eca414021ebae76fdde3205bb965a"
GITHUB_PACKAGE = (
    "sources/ega/checkpoints/"
    "ega4-sections1-10-source-aligned-working-20260730"
)

REPO_ROOT = SCRIPT_DIR.parent
PACKAGE_ROOT = REPO_ROOT / GITHUB_PACKAGE
ZENODO_CONTROL_ROOT = (
    REPO_ROOT / "tmp" / "ega4_sections1_10_zenodo_20260730"
)
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
TEMP_ROOT = Path(os.environ["LOCALAPPDATA"]) / "Temp"
READBACK_ROOT = TEMP_ROOT / "ega4_sections1_10_zenodo_readback"
RECEIPT_PREFIX = "20260730_ega4_sections1_10_source_aligned"
DRAFT_STATE = READBACK_ROOT / f"{RECEIPT_PREFIX}_zenodo_draft_state.json"
PREDECESSOR_RECEIPT = (
    RECEIPT_ROOT
    / "20260730_ega2_complete_source_aligned_record_21696776_public_readback.json"
)
PREDECESSOR_ZIP_RECEIPT = (
    RECEIPT_ROOT
    / "20260730_ega2_complete_source_aligned_record_21696776_zip_member_readback.json"
)

README_NAME = "90 EGA - README and Status.md"
SUMMARY_NAME = "91 EGA - Public Summary.json"
OLD_ZIPS = {
    "10d_EGA4_Sections1_2_SourceAligned_Inputs_20260729.zip",
    "10e_EGA4_Section3_SourceAligned_Inputs_20260729.zip",
    "10f_EGA4_Section4_1_4_4_SourceAligned_Inputs_20260730.zip",
}
NEW_PDF = "00d_EGA4_English_Sections1_10_Reader.pdf"
NEW_TEX = "02d_EGA4_English_Sections1_10_Master.tex"
NEW_ZIP = "10g_EGA4_English_Sections1_10_Source_20260730.zip"
ZIP_ROOT = "EGA4_English_Sections1_10_Source_20260730"
DEFAULT_PREVIEW = previous.DEFAULT_PREVIEW
REPLACED_PREDECESSOR_FILES = OLD_ZIPS | {README_NAME, SUMMARY_NAME}
EXPECTED_PREDECESSOR_FILES = 28
EXPECTED_RETAINED_FILES = 23
EXPECTED_LOCAL_FILES = 5
EXPECTED_FINAL_FILES = 28
EXPECTED_ZIP_ARCHIVES = 8

LOCAL_PATHS = {
    NEW_PDF: PACKAGE_ROOT / NEW_PDF,
    NEW_TEX: PACKAGE_ROOT / NEW_TEX,
    NEW_ZIP: PACKAGE_ROOT / NEW_ZIP,
    README_NAME: ZENODO_CONTROL_ROOT / README_NAME,
    SUMMARY_NAME: ZENODO_CONTROL_ROOT / SUMMARY_NAME,
}
LOCAL_EXPECTED = {
    NEW_PDF: (
        2_632_563,
        "773EFC15C9B815504D06A59F624C7EFC9A76B55BD5EC2F4FD17DAAEFEEB5AA6A",
    ),
    NEW_TEX: (
        765,
        "2209635F42A66B61001271D9791E03DD7988BF1FDBDE0DECF7A80CD47951B9FF",
    ),
    NEW_ZIP: (
        365_786,
        "08EDEA8FEF8B3233E8FA69072E981F26A60860C68A234363F580B8BB3E2C9677",
    ),
    README_NAME: (
        2_868,
        "7CA8323F41FF73EEDDBA362B4B9FBE5A25A19742F6EF4AFF579F6864A534E86D",
    ),
    SUMMARY_NAME: (
        4_267,
        "B4155FF8D036473A35AF9B1C2F549D3BFBB0FAC73708747AE498869112943837",
    ),
}
EXPECTED_ZIP_MEMBERS = 50
EXPECTED_ZIP_UNCOMPRESSED_BYTES = 1_468_047
EXPECTED_ZIP_MANIFEST_ROWS = 49

DESCRIPTION_PARAGRAPHS = [
    (
        "This same-concept successor adds a cumulative source-aligned EGA IV "
        "English working reader through Section 10, with Section 11 as the "
        "continuation."
    ),
    (
        "The reader is 268 pages. Its master TeX is directly visible. The "
        "compact source ZIP contains the exact sealed source closure, the "
        "reader-clean wrapper, concise build and scope notes, reference-limit "
        "evidence, and exact member checksums."
    ),
    (
        "The current landing surface replaces three bounded EGA IV custody "
        "ZIPs for Sections 1-2, Section 3, and Sections 4.1-4.4 with the one "
        "cumulative Sections 1-10 source ZIP. Immutable predecessor versions "
        "preserve those bounded packages."
    ),
    (
        "All 2,708 compiled internal GoTo actions are valid. Exhaustive "
        "cross-volume linking remains open: 1,041 printed locator occurrences "
        "across 500 unique names are not clickable. Printed locator text is "
        "preserved, and no convention-v2 completion claim is made."
    ),
    (
        "The broader older EGA IV Sections 1-21 PDF remains available as "
        "historical working coverage. For Sections 1-10, the new source-aligned "
        "reader is the preferred object."
    ),
    (
        "These are scholarly working and custody materials, not critical "
        "editions, peer-review certifications, rights determinations, "
        "whole-corpus completion claims, or tagged-PDF accessibility "
        "remediation. No new blanket license or transfer of underlying rights "
        "is asserted."
    ),
]
DESCRIPTION_HTML = "\n".join(
    f"<p>{paragraph}</p>" for paragraph in DESCRIPTION_PARAGRAPHS
)
NOTES_HTML = (
    "<p>Direct current readers remain ordered EGA 0/III, EGA II, EGA III, "
    "and EGA IV Sections 1-10, followed by directly visible master TeX files "
    "and grouped source archives. The preferred preview remains the EGA 0/III "
    "reader. The older EGA IV Sections 1-21 draft remains a broader historical "
    "working surface, while the new Sections 1-10 reader is preferred for its "
    "source-aligned scope.</p>"
)


def identity(path: Path) -> dict:
    return {
        "path": path,
        "bytes": path.stat().st_size,
        "sha256": base.sha256_file(path),
        "md5": base.md5_file(path),
    }


def safe_member_name(name: str) -> bool:
    normalized = name.replace("\\", "/")
    path = PurePosixPath(normalized)
    return (
        normalized == name
        and not path.is_absolute()
        and ".." not in path.parts
        and not (path.parts and ":" in path.parts[0])
    )


def inspect_new_zip(path: Path, *, include_members: bool) -> dict:
    members = {}
    with zipfile.ZipFile(path) as archive:
        if archive.testzip() is not None:
            raise RuntimeError("EGA IV source ZIP CRC validation failed")
        infos = archive.infolist()
        if any(info.is_dir() or not safe_member_name(info.filename) for info in infos):
            raise RuntimeError("EGA IV source ZIP contains an unsafe member")
        for info in infos:
            data = archive.read(info.filename)
            members[info.filename] = {
                "bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest().upper(),
                "crc32": f"{info.CRC:08X}",
            }

        manifest_name = f"{ZIP_ROOT}/SHA256SUMS.csv"
        rows = list(
            csv.DictReader(
                io.StringIO(archive.read(manifest_name).decode("utf-8-sig"))
            )
        )
        if len(rows) != EXPECTED_ZIP_MANIFEST_ROWS:
            raise RuntimeError("EGA IV source manifest row count changed")
        row_paths = {f"{ZIP_ROOT}/{row['relative_path']}" for row in rows}
        if (
            len(row_paths) != len(rows)
            or row_paths != set(members) - {manifest_name}
        ):
            raise RuntimeError("EGA IV source manifest boundary mismatch")
        for row in rows:
            name = f"{ZIP_ROOT}/{row['relative_path']}"
            observed = members[name]
            if (observed["bytes"], observed["sha256"]) != (
                int(row["bytes"]),
                row["sha256"].upper(),
            ):
                raise RuntimeError(
                    f"EGA IV source manifest mismatch: {row['relative_path']}"
                )

        packaged_master = members[
            f"{ZIP_ROOT}/build_harness/EGA4_English_Sections1_10.tex"
        ]
        if (
            packaged_master["bytes"] != LOCAL_EXPECTED[NEW_TEX][0]
            or packaged_master["sha256"] != LOCAL_EXPECTED[NEW_TEX][1]
            or b"Continuation: EGA IV Section 11."
            not in archive.read(f"{ZIP_ROOT}/SOURCE_ALIGNMENT_STATUS.md")
        ):
            raise RuntimeError("EGA IV packaged scope or master identity changed")

    summary = {
        "status": "PASS",
        "filename": NEW_ZIP,
        "bytes": path.stat().st_size,
        "sha256": base.sha256_file(path),
        "member_count": len(members),
        "uncompressed_bytes": sum(row["bytes"] for row in members.values()),
        "manifest_rows": len(rows),
        "scope": "EGA IV Sections 1-10",
        "continuation": "EGA IV Section 11",
        "sealed_source_files": 40,
        "reader_pages": 268,
    }
    if include_members:
        summary["members"] = members
    return summary


def assert_new_zip(summary: dict) -> None:
    if (
        summary["status"] != "PASS"
        or summary["bytes"] != LOCAL_EXPECTED[NEW_ZIP][0]
        or summary["sha256"] != LOCAL_EXPECTED[NEW_ZIP][1]
        or summary["member_count"] != EXPECTED_ZIP_MEMBERS
        or summary["uncompressed_bytes"] != EXPECTED_ZIP_UNCOMPRESSED_BYTES
        or summary["manifest_rows"] != EXPECTED_ZIP_MANIFEST_ROWS
    ):
        raise RuntimeError("EGA IV source ZIP identity boundary changed")


def github_package_readback() -> None:
    session = base.make_session()
    root = (
        "https://raw.githubusercontent.com/"
        f"KokunoYumeto/modern-latex-manuscripts/{GITHUB_COMMIT}/"
        f"{GITHUB_PACKAGE}/"
    )
    for path in sorted(PACKAGE_ROOT.iterdir(), key=lambda value: value.name.casefold()):
        if not path.is_file():
            continue
        response = base.check(
            session.get(root + quote(path.name), timeout=(30, 180)),
            {200},
        )
        data = response.content
        if (len(data), hashlib.sha256(data).hexdigest().upper()) != (
            path.stat().st_size,
            base.sha256_file(path),
        ):
            raise RuntimeError(f"GitHub EGA IV package mismatch: {path.name}")


def verify_local_files() -> dict[str, dict]:
    result = {}
    for name, path in LOCAL_PATHS.items():
        if not path.is_file():
            raise FileNotFoundError(path)
        row = identity(path)
        if (row["bytes"], row["sha256"]) != LOCAL_EXPECTED[name]:
            raise RuntimeError(f"Local EGA IV successor mismatch: {name}")
        result[name] = row
    package_validation = json.loads(
        (PACKAGE_ROOT / "PACKAGE_VALIDATION.json").read_text(encoding="utf-8")
    )
    if (
        not str(package_validation.get("status", "")).startswith("PASS")
        or package_validation.get("errors") != []
    ):
        raise RuntimeError("EGA IV package validation is not PASS")
    assert_new_zip(inspect_new_zip(LOCAL_PATHS[NEW_ZIP], include_members=False))
    json.loads(LOCAL_PATHS[SUMMARY_NAME].read_text(encoding="utf-8"))
    forbidden = ("chatgpt", "claude", "codex", "large language model")
    for name in (README_NAME, SUMMARY_NAME):
        text = LOCAL_PATHS[name].read_text(encoding="utf-8").casefold()
        hits = [term for term in forbidden if term in text]
        if hits:
            raise RuntimeError(f"Reader-facing EGA summary terms: {name}: {hits}")
    github_package_readback()
    return result


def expected_files(
    predecessor_receipt: dict,
    local: dict[str, dict],
) -> tuple[dict[str, dict], dict[str, dict]]:
    predecessor = pipeline.receipt_identities(predecessor_receipt)
    retained = {
        name: row
        for name, row in predecessor.items()
        if name not in REPLACED_PREDECESSOR_FILES
    }
    if len(predecessor) != EXPECTED_PREDECESSOR_FILES:
        raise RuntimeError("Unexpected EGA predecessor file boundary")
    if len(retained) != EXPECTED_RETAINED_FILES:
        raise RuntimeError("Unexpected retained EGA predecessor boundary")
    if set(retained) & set(local):
        raise RuntimeError("New EGA filenames collide with retained files")
    expected = {**retained, **local}
    if len(local) != EXPECTED_LOCAL_FILES or len(expected) != EXPECTED_FINAL_FILES:
        raise RuntimeError("Unexpected final EGA file boundary")
    return expected, retained


def ordered_names(expected: dict[str, dict]) -> list[str]:
    priority = [
        DEFAULT_PREVIEW,
        "00b_EGA2_English_Reader.pdf",
        "00c_EGA3_English_Working_Reader_Assigned_SourceFirst_Sections1_7_20260729.pdf",
        NEW_PDF,
        "00 EGA - English Translation Working Draft.pdf",
        "01 EGA IV - English Translation Working Draft (Sections 1-21).pdf",
        "02a_EGA0_English_Working_Master_Assigned_SourceFirst_Sections8_13_20260729.tex",
        "02b_EGA2_English_Master.tex",
        "02c_EGA3_English_Working_Master_Assigned_SourceFirst_Sections1_7_20260729.tex",
        NEW_TEX,
        "10a_EGA0_III_and_EGA3_Assigned_Lane_Source_20260729.zip",
        "10b_EGA2_English_Source_20260730.zip",
        NEW_ZIP,
    ]
    result = [name for name in priority if name in expected]
    result.extend(
        name for name in sorted(expected, key=str.casefold) if name not in result
    )
    if len(result) != len(expected):
        raise RuntimeError("EGA file-order construction failed")
    return result


def anonymous_readback(
    record_id: int,
    expected: dict[str, dict],
    retained: dict[str, dict],
    predecessor_zip_receipt: dict,
) -> tuple[dict, dict]:
    session = base.make_session()
    record = pipeline.wait_for_public(session, record_id)
    if int(record["id"]) != record_id or base.concept_doi(record) != CONCEPT_DOI:
        raise RuntimeError("Public EGA successor lineage mismatch")
    pipeline.assert_metadata(record["metadata"])
    if record["files"].get("default_preview") != DEFAULT_PREVIEW:
        raise RuntimeError("Public EGA default preview mismatch")
    public_order = record["files"].get("order", [])
    if public_order and public_order != ordered_names(expected):
        raise RuntimeError("Public EGA file order mismatch")
    entries = base.entries_map(record)
    if set(entries) != set(expected):
        raise RuntimeError("Public EGA outer-file set mismatch")
    for name, wanted in expected.items():
        if (
            int(entries[name]["size"]),
            base.normalize_checksum(entries[name]["checksum"]),
        ) != (wanted["bytes"], wanted["md5"]):
            raise RuntimeError(f"Public EGA API identity mismatch: {name}")

    latest = base.check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}/versions/latest?expand=true",
            headers={"Accept": "application/vnd.inveniordm.v1+json"},
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if int(latest["id"]) != record_id or base.concept_doi(latest) != CONCEPT_DOI:
        raise RuntimeError("Public EGA successor is not the concept head")

    pipeline.clean_temp(READBACK_ROOT)
    READBACK_ROOT.mkdir(parents=True)
    files = {}
    zip_summaries = copy.deepcopy(predecessor_zip_receipt["archives"])
    for old_zip in OLD_ZIPS:
        if zip_summaries.pop(old_zip, None) is None:
            raise RuntimeError(f"Predecessor EGA ZIP receipt is missing: {old_zip}")
    try:
        for index, name in enumerate(sorted(expected, key=str.casefold), start=1):
            wanted = expected[name]
            if name in retained:
                files[name] = {
                    "bytes": wanted["bytes"],
                    "sha256": wanted["sha256"],
                    "md5": wanted["md5"],
                    "url": entries[name]["links"]["content"],
                    "match": True,
                    "readback_mode": (
                        "public_api_size_md5_bound_to_predecessor_sha256"
                    ),
                }
                continue
            print(f"PUBLIC READBACK {index}/{len(expected)} {name}", flush=True)
            target = READBACK_ROOT / f"public-{index:02d}"
            size, sha, md5 = pipeline.download_file(
                session,
                entries[name]["links"]["content"],
                target,
            )
            if (size, sha, md5) != (
                wanted["bytes"],
                wanted["sha256"],
                wanted["md5"],
            ):
                raise RuntimeError(f"Public EGA readback mismatch: {name}")
            files[name] = {
                "bytes": size,
                "sha256": sha,
                "md5": md5,
                "url": entries[name]["links"]["content"],
                "match": True,
                "readback_mode": "anonymous_full_download_sha256",
            }
            if name == NEW_ZIP:
                summary = inspect_new_zip(target, include_members=True)
                assert_new_zip(summary)
                zip_summaries[name] = summary
            target.unlink()
    finally:
        pipeline.clean_temp(READBACK_ROOT)

    if (
        len(files) != EXPECTED_FINAL_FILES
        or len(retained) != EXPECTED_RETAINED_FILES
        or len(zip_summaries) != EXPECTED_ZIP_ARCHIVES
    ):
        raise RuntimeError("EGA public readback boundary did not close")

    public = {
        "status": "PASS",
        "errors": [],
        "record": record_id,
        "doi": base.version_doi(record),
        "conceptdoi": CONCEPT_DOI,
        "record_url": f"https://zenodo.org/records/{record_id}",
        "version": VERSION,
        "file_count": len(files),
        "bytes": sum(row["bytes"] for row in files.values()),
        "files": files,
        "latest_record": int(latest["id"]),
        "rdm_default_preview": record["files"].get("default_preview"),
        "rdm_file_order": public_order,
        "requested_file_order": ordered_names(expected),
        "github_commit": GITHUB_COMMIT,
        "github_package": GITHUB_PACKAGE,
        "retained_predecessor_files": EXPECTED_RETAINED_FILES,
        "replaced_predecessor_files": sorted(REPLACED_PREDECESSOR_FILES),
        "new_or_renamed_files": EXPECTED_LOCAL_FILES,
        "duplicate_concept_created": False,
        "second_draft_created": False,
    }
    zipped = {
        "status": "PASS",
        "errors": [],
        "record": record_id,
        "doi": base.version_doi(record),
        "zip_archive_count": len(zip_summaries),
        "archives": zip_summaries,
    }
    base.save_json(
        RECEIPT_ROOT / f"{RECEIPT_PREFIX}_record_{record_id}_public_readback.json",
        public,
    )
    base.save_json(
        RECEIPT_ROOT
        / f"{RECEIPT_PREFIX}_record_{record_id}_zip_member_readback.json",
        zipped,
    )
    return public, zipped


def configure_pipeline() -> None:
    previous.CONCEPT_DOI = CONCEPT_DOI
    previous.PREDECESSOR_RECORD = PREDECESSOR_RECORD
    previous.PREDECESSOR_DOI = PREDECESSOR_DOI
    previous.PUBLICATION_DATE = PUBLICATION_DATE
    previous.VERSION = VERSION
    previous.TITLE = TITLE
    previous.GITHUB_COMMIT = GITHUB_COMMIT
    previous.GITHUB_PACKAGE = GITHUB_PACKAGE
    previous.DRAFT_STATE = DRAFT_STATE
    previous.RECEIPT_PREFIX = RECEIPT_PREFIX
    previous.PREDECESSOR_RECEIPT = PREDECESSOR_RECEIPT
    previous.PREDECESSOR_ZIP_RECEIPT = PREDECESSOR_ZIP_RECEIPT
    previous.REPLACED_PREDECESSOR_FILES = REPLACED_PREDECESSOR_FILES
    previous.EXPECTED_PREDECESSOR_FILES = EXPECTED_PREDECESSOR_FILES
    previous.EXPECTED_RETAINED_FILES = EXPECTED_RETAINED_FILES
    previous.EXPECTED_LOCAL_FILES = EXPECTED_LOCAL_FILES
    previous.EXPECTED_FINAL_FILES = EXPECTED_FINAL_FILES
    previous.DEFAULT_PREVIEW = DEFAULT_PREVIEW
    previous.DESCRIPTION_HTML = DESCRIPTION_HTML
    previous.NOTES_HTML = NOTES_HTML
    previous.ordered_names = ordered_names
    previous.configure_pipeline()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--preflight", action="store_true")
    parser.add_argument("--readback-only", action="store_true")
    args = parser.parse_args()

    configure_pipeline()
    local = verify_local_files()
    predecessor_receipt, predecessor_zip_receipt = pipeline.load_predecessor()
    expected, retained = expected_files(predecessor_receipt, local)
    session = base.make_session()

    if args.preflight:
        pipeline.verify_live_predecessor(session, predecessor_receipt)
        print(
            json.dumps(
                {
                    "status": "PASS_PREFLIGHT",
                    "concept_doi": CONCEPT_DOI,
                    "predecessor_record": PREDECESSOR_RECORD,
                    "retained_files": len(retained),
                    "replaced_files": len(REPLACED_PREDECESSOR_FILES),
                    "new_or_renamed_files": len(local),
                    "final_files": len(expected),
                    "default_preview": DEFAULT_PREVIEW,
                    "ega4_source_zip_members": EXPECTED_ZIP_MEMBERS,
                    "final_zip_archives": EXPECTED_ZIP_ARCHIVES,
                },
                indent=2,
            ),
            flush=True,
        )
        return

    if args.readback_only:
        state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
        if not state.get("published"):
            raise RuntimeError("Tracked EGA successor is not published")
        public, zipped = anonymous_readback(
            int(state["draft_id"]),
            expected,
            retained,
            predecessor_zip_receipt,
        )
        print(
            json.dumps(
                {
                    "status": public["status"],
                    "record": public["record"],
                    "doi": public["doi"],
                    "files": public["file_count"],
                    "bytes": public["bytes"],
                    "zip_archives": zipped["zip_archive_count"],
                },
                indent=2,
            ),
            flush=True,
        )
        return

    predecessor = pipeline.verify_live_predecessor(session, predecessor_receipt)
    token = base.find_token()
    draft_id = pipeline.create_or_resume_draft(session, token, predecessor)
    staged = pipeline.stage_draft(session, token, draft_id, expected, local)
    published = pipeline.publish_draft(session, token, draft_id, expected)
    public, zipped = anonymous_readback(
        draft_id,
        expected,
        retained,
        predecessor_zip_receipt,
    )
    print(
        json.dumps(
            {
                "stage": staged,
                "publish": published,
                "readback": {
                    "status": public["status"],
                    "record": public["record"],
                    "doi": public["doi"],
                    "files": public["file_count"],
                    "bytes": public["bytes"],
                    "zip_archives": zipped["zip_archive_count"],
                },
            },
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
