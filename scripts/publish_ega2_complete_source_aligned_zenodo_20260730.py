#!/usr/bin/env python3
"""Publish and read back the complete source-aligned EGA II reader."""

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
    SCRIPT_DIR / "publish_ega4_sections1_2_custody_zenodo_20260729.py"
)
SPEC = importlib.util.spec_from_file_location(
    "ega_sections12_custody_publisher",
    PREVIOUS_PATH,
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load the established EGA custody workflow")
previous = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = previous
SPEC.loader.exec_module(previous)

base = previous.base
pipeline = previous.previous
API = previous.API
CONCEPT_DOI = "10.5281/zenodo.20414353"
PREDECESSOR_RECORD = 21_694_219
PREDECESSOR_DOI = "10.5281/zenodo.21694219"
PUBLICATION_DATE = "2026-07-30"
VERSION = "2026-07-30 complete source-aligned EGA II working reader"
TITLE = previous.TITLE

GITHUB_COMMIT = "c22f175492f0cbf51d05e3410e55ae168ca8f966"
GITHUB_PACKAGE = (
    "sources/ega/checkpoints/"
    "ega2-complete-source-aligned-working-20260730"
)

REPO_ROOT = SCRIPT_DIR.parent
PACKAGE_ROOT = REPO_ROOT / GITHUB_PACKAGE
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
TEMP_ROOT = Path(os.environ["LOCALAPPDATA"]) / "Temp"
READBACK_ROOT = TEMP_ROOT / "ega2_complete_source_aligned_zenodo_readback"
RECEIPT_PREFIX = "20260730_ega2_complete_source_aligned"
DRAFT_STATE = RECEIPT_ROOT / f"{RECEIPT_PREFIX}_zenodo_draft_state.json"
PREDECESSOR_RECEIPT = (
    RECEIPT_ROOT
    / "20260730_ega4_section4_1_4_4_custody_record_21694219_public_readback.json"
)
PREDECESSOR_ZIP_RECEIPT = (
    RECEIPT_ROOT
    / "20260730_ega4_section4_1_4_4_custody_record_21694219_zip_member_readback.json"
)

README_NAME = "90 EGA - README and Status.md"
SUMMARY_NAME = "91 EGA - Public Summary.json"
OLD_PDF = "00b_EGA2_English_Layered_Working_Reader_Through_4_4_5_20260729.pdf"
OLD_TEX = "02b_EGA2_English_Layered_Working_Master_Through_4_4_5_20260729.tex"
OLD_ZIP = "10b_EGA2_English_Layered_Working_Source_Through_4_4_5_20260729.zip"
NEW_PDF = "00b_EGA2_English_Reader.pdf"
NEW_TEX = "02b_EGA2_English_Master.tex"
NEW_ZIP = "10b_EGA2_English_Source_20260730.zip"
DEFAULT_PREVIEW = previous.DEFAULT_PREVIEW
REPLACED_PREDECESSOR_FILES = {
    OLD_PDF,
    OLD_TEX,
    OLD_ZIP,
    README_NAME,
    SUMMARY_NAME,
}
EXPECTED_PREDECESSOR_FILES = 28
EXPECTED_RETAINED_FILES = 23
EXPECTED_LOCAL_FILES = 5
EXPECTED_FINAL_FILES = 28
EXPECTED_ZIP_ARCHIVES = 10

LOCAL_PATHS = {
    NEW_PDF: PACKAGE_ROOT / NEW_PDF,
    NEW_TEX: PACKAGE_ROOT / NEW_TEX,
    NEW_ZIP: PACKAGE_ROOT / NEW_ZIP,
    README_NAME: REPO_ROOT / "manifests" / README_NAME,
    SUMMARY_NAME: REPO_ROOT / "manifests" / SUMMARY_NAME,
}
LOCAL_EXPECTED = {
    NEW_PDF: (
        1_060_715,
        "6CEB2FFBF3F364B8CCFE64698751C3DEAD7A8E3B3823680ECF4CBB5E8B5241BD",
    ),
    NEW_TEX: (
        1_799,
        "F4624484EE2C0A855952DC0B3D917085AEBC10F8B71E7F373D2B2574AA8D69C1",
    ),
    NEW_ZIP: (
        1_246_946,
        "6BB198A629A73AAB21BC68A8959FCA4CB232A2A07FDF2BA0E9B0D460F93415A4",
    ),
    README_NAME: (
        3_315,
        "5AEAEEB6C08D88BF41DD0965C740B4F8F7C138208572DC9B63335A38067278DA",
    ),
    SUMMARY_NAME: (
        4_167,
        "A3A906D839408C17EBB7F11DE57729FAB746DE32115A3EA3776E21B3C467C76D",
    ),
}
EXPECTED_ZIP_MEMBERS = 20
EXPECTED_ZIP_UNCOMPRESSED_BYTES = 1_838_698
EXPECTED_ZIP_MANIFEST_ROWS = 19

DESCRIPTION_PARAGRAPHS = [
    (
        "This same-concept successor replaces the bounded EGA II reader "
        "through Corollary 4.4.5 with a complete source-aligned EGA II "
        "English working reader through authority EOF."
    ),
    (
        "The 165-page reader is continuous from the chapter opening through "
        "Section 8.14, the bibliography, index of notation, terminological "
        "index, original table of contents, and Errata and Addenda (List 1). "
        "There is no remaining EGA II translation cursor."
    ),
    (
        "The master TeX is directly visible. The compact source ZIP contains "
        "20 exact members: the complete fourteen-file editable closure, the "
        "same reader, concise public build and visual-QA summaries, and a "
        "nineteen-row self-excluding checksum manifest."
    ),
    (
        "The public successor also removes duplicate backmatter registrations "
        "and repairs the original-contents table layout without changing the "
        "mathematical body. Project, model, workflow, source-status, and "
        "private-path text is absent from the reader."
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
    "<p>Direct readers remain ordered EGA 0/III, EGA II, and EGA III, "
    "followed by directly visible master TeX files and grouped source "
    "archives. EGA II is complete as a source-aligned working reader; the "
    "other direct readers remain bounded. The preferred preview remains the "
    "EGA 0/III reader. Immutable predecessor versions preserve the earlier "
    "partial EGA II release.</p>"
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
            raise RuntimeError("EGA II source ZIP CRC validation failed")
        infos = archive.infolist()
        if any(info.is_dir() or not safe_member_name(info.filename) for info in infos):
            raise RuntimeError(
                "EGA II source ZIP contains an unsafe member"
            )
        for info in infos:
            data = archive.read(info.filename)
            members[info.filename] = {
                "bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest().upper(),
                "crc32": f"{info.CRC:08X}",
            }

        rows = list(
            csv.DictReader(
                io.StringIO(archive.read("SHA256SUMS.csv").decode("utf-8-sig"))
            )
        )
        if len(rows) != EXPECTED_ZIP_MANIFEST_ROWS:
            raise RuntimeError("EGA II source manifest row count changed")
        row_paths = {row["relative_path"] for row in rows}
        if (
            len(row_paths) != len(rows)
            or row_paths != set(members) - {"SHA256SUMS.csv"}
        ):
            raise RuntimeError("EGA II source manifest boundary mismatch")
        for row in rows:
            observed = members[row["relative_path"]]
            if (observed["bytes"], observed["sha256"]) != (
                int(row["bytes"]),
                row["sha256"].upper(),
            ):
                raise RuntimeError(
                    "EGA II source manifest mismatch: "
                    f"{row['relative_path']}"
                )

        packaged_reader = members[f"reader/{NEW_PDF}"]
        if (
            packaged_reader["bytes"] != LOCAL_EXPECTED[NEW_PDF][0]
            or packaged_reader["sha256"] != LOCAL_EXPECTED[NEW_PDF][1]
            or len(
                [
                    name
                    for name in members
                    if name.startswith("source/") and name.endswith(".tex")
                ]
            )
            != 14
            or b"Remaining EGA II translation cursor: none."
            not in archive.read("SOURCE_ALIGNMENT_STATUS.md")
        ):
            raise RuntimeError("EGA II packaged scope or reader identity changed")

    summary = {
        "status": "PASS",
        "filename": NEW_ZIP,
        "bytes": path.stat().st_size,
        "sha256": base.sha256_file(path),
        "member_count": len(members),
        "uncompressed_bytes": sum(row["bytes"] for row in members.values()),
        "manifest_rows": len(rows),
        "scope": "Complete source-aligned EGA II",
        "continuation": "Authority EOF",
        "editable_source_files": 14,
        "reader_pages": 165,
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
        raise RuntimeError("EGA II source ZIP identity boundary changed")


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
                raise RuntimeError(
                f"GitHub EGA II package mismatch: {path.name}"
            )


def verify_local_files() -> dict[str, dict]:
    result = {}
    for name, path in LOCAL_PATHS.items():
        if not path.is_file():
            raise FileNotFoundError(path)
        row = identity(path)
        if (row["bytes"], row["sha256"]) != LOCAL_EXPECTED[name]:
            raise RuntimeError(f"Local EGA II successor mismatch: {name}")
        result[name] = row
    package_validation = json.loads(
        (PACKAGE_ROOT / "PACKAGE_VALIDATION.json").read_text(encoding="utf-8")
    )
    if (
        package_validation.get("status") != "PASS"
        or package_validation.get("errors") != []
    ):
        raise RuntimeError("EGA II package validation is not PASS")
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
        NEW_PDF,
        "00c_EGA3_English_Working_Reader_Assigned_SourceFirst_Sections1_7_20260729.pdf",
        "00 EGA - English Translation Working Draft.pdf",
        "01 EGA IV - English Translation Working Draft (Sections 1-21).pdf",
        (
            "02a_EGA0_English_Working_Master_"
            "Assigned_SourceFirst_Sections8_13_20260729.tex"
        ),
        NEW_TEX,
        "02c_EGA3_English_Working_Master_Assigned_SourceFirst_Sections1_7_20260729.tex",
        "10a_EGA0_III_and_EGA3_Assigned_Lane_Source_20260729.zip",
        NEW_ZIP,
        previous.NEW_ZIP,
        "10e_EGA4_Section3_SourceAligned_Inputs_20260729.zip",
        "10f_EGA4_Section4_1_4_4_SourceAligned_Inputs_20260730.zip",
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
    removed_zip = zip_summaries.pop(OLD_ZIP, None)
    if removed_zip is None:
        raise RuntimeError("Predecessor EGA II source ZIP receipt is missing")
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
    previous.configure_previous()


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
                    "ega2_source_zip_members": EXPECTED_ZIP_MEMBERS,
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
