#!/usr/bin/env python3
"""Publish the complete EGA II reference-v2 same-concept successor."""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import io
import json
import re
import shutil
import time
import zipfile
from pathlib import Path, PurePosixPath
from urllib.parse import quote

import publish_current_reader_bundles_zenodo_20260730 as base


API = base.API
PUBLICATION_DATE = "2026-07-30"
PREDECESSOR_RECORD = 21_702_700
PREDECESSOR_DOI = "10.5281/zenodo.21702700"
CONCEPT_DOI = "10.5281/zenodo.20414353"
EXPECTED_PREDECESSOR_FILES = 29
EXPECTED_PREDECESSOR_BYTES = 508_639_518
EXPECTED_RETAINED_FILES = 23
EXPECTED_FINAL_FILES = 29
EXPECTED_FINAL_BYTES = 513_253_980
EXPECTED_ZIP_ARCHIVES = 9
DEFAULT_PREVIEW = (
    "00a_EGA0_English_Working_Reader_Assigned_SourceFirst_"
    "Sections8_13_20260729.pdf"
)
TITLE = (
    "Elements de geometrie algebrique (EGA): French Originals, "
    "English Working Readers, and Source Archives"
)
VERSION = "2026-07-30 complete EGA II reference-v2 working reader"
GITHUB_COMMIT = "24f757158c6b10b7ef116b71434f59e0ab43d522"

REPO_ROOT = Path(__file__).resolve().parent.parent
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
TEMP_ROOT = Path(base.os.environ["LOCALAPPDATA"]) / "Temp" / (
    "ega2_reference_v2_zenodo_20260730"
)
READBACK_ROOT = TEMP_ROOT / "public_readback"
DRAFT_STATE = RECEIPT_ROOT / (
    "20260730_ega2_reference_v2_zenodo_draft_state.json"
)
PREDECESSOR_RECEIPT = RECEIPT_ROOT / (
    "20260730_ega_current_reader_bundle_record_21702700_"
    "public_readback.json"
)
SHA_BASELINE_RECEIPT = RECEIPT_ROOT / (
    "20260730_ega4_sections1_10_source_aligned_record_21697218_"
    "public_readback.json"
)
ZIP_BASELINE_RECEIPT = RECEIPT_ROOT / (
    "20260730_ega4_sections1_10_source_aligned_record_21697218_"
    "zip_member_readback.json"
)
GITHUB_RECEIPTS = (
    REPO_ROOT
    / "manifests/published-github/"
    "20260730_ega2_reference_v2_commit_24f757158_public_readback.json",
    REPO_ROOT
    / "manifests/published-github/"
    "20260730_ega2_reference_v2_commit_24f757158_zip_member_readback.json",
    REPO_ROOT
    / "manifests/published-github/"
    "20260730_ega_reader_bundle_reference_v2_commit_24f757158_"
    "zip_member_readback.json",
)

BUNDLE_NAME = "00 Current_EGA_English_Readers_and_Buildable_TeX_20260730.zip"
PDF_NAME = "00b_EGA2_English_Reader.pdf"
TEX_NAME = "02b_EGA2_English_Master.tex"
SOURCE_NAME = "10b_EGA2_English_Source_20260730.zip"
README_NAME = "90 EGA - README and Status.md"
SUMMARY_NAME = "91 EGA - Public Summary.json"
REPLACED_NAMES = {
    BUNDLE_NAME,
    PDF_NAME,
    TEX_NAME,
    SOURCE_NAME,
    README_NAME,
    SUMMARY_NAME,
}

LOCAL_PATHS = {
    BUNDLE_NAME: REPO_ROOT
    / "sources/ega/"
    "ega-current-readers-and-buildable-tex-bundle-reference-v2-20260730/"
    / BUNDLE_NAME,
    PDF_NAME: REPO_ROOT
    / "sources/ega/ega2-complete-reference-v2-release-20260730"
    / PDF_NAME,
    TEX_NAME: REPO_ROOT
    / "sources/ega/ega2-complete-reference-v2-release-20260730"
    / TEX_NAME,
    SOURCE_NAME: REPO_ROOT
    / "sources/ega/ega2-complete-reference-v2-release-20260730"
    / SOURCE_NAME,
    README_NAME: REPO_ROOT / "manifests" / README_NAME,
    SUMMARY_NAME: REPO_ROOT / "manifests" / SUMMARY_NAME,
}
LOCAL_EXPECTED = {
    BUNDLE_NAME: (
        5_866_777,
        "6E1796CD3356CEAC4CD91CCB4ECE8358F722E59DD7FF3AA434E71FF5C05EE455",
    ),
    PDF_NAME: (
        1_905_144,
        "16487005C6257BDA2FC8B2C872C153538DE73A8950CD9B26D772B6BE354FA78F",
    ),
    TEX_NAME: (
        2_205,
        "D42280B6ECD1E0ECCB4812A5F902510E9DBF1BBCFB6965EEA7CED06E0199A525",
    ),
    SOURCE_NAME: (
        4_950_763,
        "415324691FFFD387F35862E29115184B14AE4A6D0C8703A0BB2B057211D8F2BD",
    ),
    README_NAME: (
        3_536,
        "D46D17C30FC18090ACAFB92CA89008BF17B76D912CF71EE1FB87E386F9B89E8F",
    ),
    SUMMARY_NAME: (
        4_717,
        "C1B81D6E33716E16E435F872B6B27E8B4A057FB56D1BF6BEC5D2710E9546CCD3",
    ),
}

DESCRIPTION_HTML = "\n".join(
    f"<p>{paragraph}</p>"
    for paragraph in (
        (
            "<strong>Start here:</strong> the first file is one clean ZIP "
            "containing one cumulative English reader PDF for every current "
            "EGA scope in this record together with its complete buildable "
            "TeX closure. The same readers and master TeX files remain "
            "directly accessible immediately afterward."
        ),
        (
            "This same-concept successor replaces EGA II with its complete "
            "165-page source-aligned reference-v2 working reader through "
            "authority EOF, including the bibliography, notation and "
            "terminology indexes, contents, and Errata and Addenda (List 1)."
        ),
        (
            "The EGA II reader contains 1,028 stable targets, 2,078 resolved "
            "internal GoTo actions, and 2,538 named destinations, with no "
            "broken or external actions. Its master TeX is directly visible; "
            "the grouped source ZIP contains the exact 51-file public package."
        ),
        (
            "The current EGA 0/III, EGA III, and EGA IV scopes are retained "
            "byte-for-byte. EGA 0/III remains the preferred preview. Earlier "
            "versions remain immutable release history."
        ),
        (
            "These are scholarly working and custody materials, not critical "
            "editions, peer-review or mathematical certifications, rights "
            "determinations, whole-EGA completion claims, or tagged-PDF "
            "accessibility remediation. No blanket license or transfer of "
            "underlying rights is asserted."
        ),
    )
)
NOTES_HTML = (
    "<p>Direct current readers remain ordered EGA 0/III, EGA II, EGA III, "
    "and EGA IV Sections 1-10, followed by directly visible master TeX files "
    "and grouped source archives. The older EGA IV Sections 1-21 draft "
    "remains broader historical working coverage.</p>"
)


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
        and not re.match(r"^[A-Za-z]:", name)
    )


def zip_inventory(path: Path) -> dict[str, object]:
    members: dict[str, dict[str, object]] = {}
    with zipfile.ZipFile(path) as archive:
        if archive.testzip() is not None:
            raise RuntimeError(f"ZIP CRC failure: {path.name}")
        infos = [row for row in archive.infolist() if not row.is_dir()]
        names = [row.filename for row in infos]
        if len(names) != len(set(names)) or not all(map(safe_member, names)):
            raise RuntimeError(f"Unsafe or duplicate ZIP member: {path.name}")
        for info in sorted(infos, key=lambda row: row.filename.casefold()):
            data = archive.read(info.filename)
            members[info.filename] = {
                "bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest().upper(),
                "crc32": f"{info.CRC:08X}",
            }
    return {
        "status": "PASS",
        "filename": path.name,
        "bytes": path.stat().st_size,
        "sha256": sha256_path(path),
        "members": len(members),
        "uncompressed_bytes": sum(
            int(row["bytes"]) for row in members.values()
        ),
        "member_identities": members,
    }


def compact_member_map(value: object) -> dict[str, tuple[int, str]]:
    if isinstance(value, dict):
        return {
            name: (int(row["bytes"]), str(row["sha256"]).upper())
            for name, row in value.items()
        }
    if isinstance(value, list):
        return {
            str(row["relative_path"]): (
                int(row["bytes"]),
                str(row["sha256"]).upper(),
            )
            for row in value
        }
    raise RuntimeError("Unsupported predecessor ZIP-member receipt schema")


def validate_source_zip(summary: dict[str, object]) -> None:
    if (
        summary["members"] != 51
        or summary["uncompressed_bytes"] != 8_173_871
        or (summary["bytes"], summary["sha256"])
        != LOCAL_EXPECTED[SOURCE_NAME]
    ):
        raise RuntimeError("EGA II source ZIP boundary changed")
    members = summary["member_identities"]
    manifest = members.get("ZENODO_PAYLOAD_MANIFEST.csv")
    validation = members.get("PACKAGE_VALIDATION.json")
    if (
        manifest is None
        or validation is None
        or manifest["sha256"]
        != "5A173FD9FDA7DDE4B3427FC55857ACC9D48878ABC2A1D955C1E42D7E8457E0AC"
        or validation["sha256"]
        != "98BF4A241A264503DF9AB0A7FE1924067D00AAD8E4174AA164ACC6CF4F616B4D"
    ):
        raise RuntimeError("EGA II source ZIP control identity changed")
    with zipfile.ZipFile(LOCAL_PATHS[SOURCE_NAME]) as archive:
        rows = list(
            csv.DictReader(
                io.StringIO(
                    archive.read("ZENODO_PAYLOAD_MANIFEST.csv").decode(
                        "utf-8-sig"
                    )
                )
            )
        )
        if len(rows) != 49:
            raise RuntimeError("EGA II source manifest row count changed")
        for row in rows:
            observed = members.get(row["relative_path"])
            if observed is None or (
                int(observed["bytes"]), observed["sha256"]
            ) != (int(row["bytes"]), row["sha256"].upper()):
                raise RuntimeError(
                    f"EGA II source manifest mismatch: {row['relative_path']}"
                )


def validate_bundle(summary: dict[str, object]) -> None:
    if (
        summary["members"] != 99
        or summary["uncompressed_bytes"] != 10_411_777
        or (summary["bytes"], summary["sha256"])
        != LOCAL_EXPECTED[BUNDLE_NAME]
    ):
        raise RuntimeError("EGA current-reader bundle boundary changed")
    required = {
        "EGA_Current_English_Readers_and_TeX_20260730/EGA0/reader/"
        "EGA0_English_Working_Reader.pdf",
        "EGA_Current_English_Readers_and_TeX_20260730/EGA2/reader/"
        "EGA2_English_Reader.pdf",
        "EGA_Current_English_Readers_and_TeX_20260730/EGA3/reader/"
        "EGA3_English_Working_Reader_Sections1_7.pdf",
        "EGA_Current_English_Readers_and_TeX_20260730/EGA4/reader/"
        "EGA4_English_Working_Reader_Sections1_10.pdf",
    }
    if not required.issubset(summary["member_identities"]):
        raise RuntimeError("EGA current-reader bundle is missing a reader")


def load_receipts() -> tuple[dict, dict, dict]:
    predecessor = json.loads(PREDECESSOR_RECEIPT.read_text(encoding="utf-8"))
    baseline = json.loads(SHA_BASELINE_RECEIPT.read_text(encoding="utf-8"))
    zip_baseline = json.loads(ZIP_BASELINE_RECEIPT.read_text(encoding="utf-8"))
    if (
        predecessor.get("status") != "PASS_PUBLIC_READBACK"
        or int(predecessor.get("record_id", -1)) != PREDECESSOR_RECORD
        or predecessor.get("concept_doi") != CONCEPT_DOI
        or len(predecessor.get("outer_file_identities", {}))
        != EXPECTED_PREDECESSOR_FILES
        or baseline.get("status") != "PASS"
        or len(baseline.get("files", {})) != 28
        or zip_baseline.get("status") != "PASS"
        or len(zip_baseline.get("archives", {})) != 8
    ):
        raise RuntimeError("Controlling EGA predecessor receipts changed")
    return predecessor, baseline, zip_baseline


def verify_local() -> dict[str, dict[str, object]]:
    result: dict[str, dict[str, object]] = {}
    for name, path in LOCAL_PATHS.items():
        if not path.is_file():
            raise FileNotFoundError(path)
        observed = (path.stat().st_size, sha256_path(path))
        if observed != LOCAL_EXPECTED[name]:
            raise RuntimeError(f"Local replacement changed: {name}")
        result[name] = {
            "path": path,
            "bytes": observed[0],
            "sha256": observed[1],
            "md5": md5_path(path),
        }
    validate_source_zip(zip_inventory(LOCAL_PATHS[SOURCE_NAME]))
    validate_bundle(zip_inventory(LOCAL_PATHS[BUNDLE_NAME]))
    json.loads(LOCAL_PATHS[SUMMARY_NAME].read_text(encoding="utf-8"))
    for receipt in GITHUB_RECEIPTS:
        row = json.loads(receipt.read_text(encoding="utf-8"))
        if row.get("status") != "PASS" or row.get("commit") != GITHUB_COMMIT:
            raise RuntimeError(f"GitHub readback receipt changed: {receipt.name}")
    return result


def public_headers() -> dict[str, str]:
    return {"Accept": "application/vnd.inveniordm.v1+json"}


def auth_headers(token: str) -> dict[str, str]:
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.inveniordm.v1+json",
    }


def fetch_live(session, predecessor: dict) -> dict:
    live = base.check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}?expand=true",
            headers=public_headers(),
            timeout=(30, 180),
        ),
        {200},
    ).json()
    entries = base.modern_entries(live)
    expected = predecessor["outer_file_identities"]
    if (
        int(live["id"]) != PREDECESSOR_RECORD
        or live["pids"]["doi"]["identifier"] != PREDECESSOR_DOI
        or live["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI
        or len(entries) != EXPECTED_PREDECESSOR_FILES
        or sum(int(row["size"]) for row in entries.values())
        != EXPECTED_PREDECESSOR_BYTES
        or live["files"].get("default_preview") != DEFAULT_PREVIEW
        or set(entries) != set(expected)
    ):
        raise RuntimeError("Live EGA predecessor boundary changed")
    for name, row in expected.items():
        if (
            int(entries[name]["size"]),
            base.normalized_md5(entries[name]["checksum"]),
        ) != (int(row["bytes"]), row["md5"].lower()):
            raise RuntimeError(f"Live EGA predecessor drift: {name}")
    latest = base.check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}/versions/latest?expand=true",
            headers=public_headers(),
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if int(latest["id"]) != PREDECESSOR_RECORD:
        raise RuntimeError("EGA concept head moved; refusing parallel successor")
    return live


def assert_no_untracked_draft(session, token: str) -> None:
    headers = auth_headers(token)
    if DRAFT_STATE.is_file():
        state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
        if state.get("published"):
            return
        response = session.get(
            f"{API}/records/{int(state['draft_id'])}/draft",
            headers=headers,
            timeout=(30, 60),
        )
        base.check(response, {200})
        return
    response = session.get(
        f"{API}/records/{PREDECESSOR_RECORD}/draft",
        headers=headers,
        timeout=(30, 60),
    )
    if response.status_code == 200:
        raise RuntimeError("Untracked active EGA successor draft exists")
    base.check(response, {404})


def create_or_resume_draft(session, token: str, live: dict) -> int:
    headers = auth_headers(token)
    if DRAFT_STATE.is_file():
        state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
        if state.get("published"):
            raise RuntimeError("Tracked EGA successor is already published")
        draft_id = int(state["draft_id"])
        base.check(
            session.get(
                f"{API}/records/{draft_id}/draft",
                headers=headers,
                timeout=(30, 60),
            ),
            {200},
        )
        return draft_id
    predecessor = base.check(
        session.get(
            f"{API}/deposit/depositions/{PREDECESSOR_RECORD}",
            headers={"Authorization": f"Bearer {token}"},
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if (
        predecessor.get("state") != "done"
        or not predecessor.get("submitted")
        or not predecessor.get("links", {}).get("newversion")
    ):
        raise RuntimeError("Live EGA predecessor is not a versioning base")
    created = base.check(
        session.post(
            predecessor["links"]["newversion"],
            headers={"Authorization": f"Bearer {token}"},
            timeout=(30, 300),
        ),
        {201},
    ).json()
    deposition = base.check(
        session.get(
            created["links"]["latest_draft"],
            headers={"Authorization": f"Bearer {token}"},
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if set(base.legacy_entries(deposition)) != set(base.modern_entries(live)):
        raise RuntimeError("EGA successor did not inherit predecessor exactly")
    draft_id = int(deposition["id"])
    base.save_json(
        DRAFT_STATE,
        {
            "status": "OPEN_TRACKED_DRAFT",
            "predecessor_record": PREDECESSOR_RECORD,
            "draft_id": draft_id,
            "concept_doi": CONCEPT_DOI,
            "published": False,
        },
    )
    return draft_id


def ordered_names(names: set[str]) -> list[str]:
    order = [
        BUNDLE_NAME,
        DEFAULT_PREVIEW,
        PDF_NAME,
        "00c_EGA3_English_Working_Reader_Assigned_SourceFirst_Sections1_7_20260729.pdf",
        "00d_EGA4_English_Sections1_10_Reader.pdf",
        "02a_EGA0_English_Working_Master_Assigned_SourceFirst_Sections8_13_20260729.tex",
        TEX_NAME,
        "02c_EGA3_English_Working_Master_Assigned_SourceFirst_Sections1_7_20260729.tex",
        "02d_EGA4_English_Sections1_10_Master.tex",
        "00 EGA - English Translation Working Draft.pdf",
        "01 EGA IV - English Translation Working Draft (Sections 1-21).pdf",
        "10 EGA I - French Original (NUMDAM PMIHES 4, 1960).pdf",
        "11 EGA II - French Original (NUMDAM PMIHES 8, 1961).pdf",
        "12 EGA III Part 1 - French Original (NUMDAM PMIHES 11, 1961).pdf",
        "13 EGA III Part 2 - French Original (NUMDAM PMIHES 17, 1963).pdf",
        "14 EGA IV Part 1 - French Original (NUMDAM PMIHES 20, 1964).pdf",
        "15 EGA IV Part 2 - French Original (NUMDAM PMIHES 24, 1965).pdf",
        "16 EGA IV Part 3 - French Original (NUMDAM PMIHES 28, 1966).pdf",
        "17 EGA IV Part 4 - French Original (NUMDAM PMIHES 32, 1967).pdf",
        "10a_EGA0_III_and_EGA3_Assigned_Lane_Source_20260729.zip",
        SOURCE_NAME,
        "10g_EGA4_English_Sections1_10_Source_20260730.zip",
        "80 EGA - EGA 0 IV Translation TeX Supplement.zip",
        "81 EGA - Full TeX Source, French Originals, and Build Artifacts.zip",
        "82 EGA - EGA IV Main Text Translation TeX Supplement.zip",
        "83 EGA IV - Standalone Sections 1-21 TeX and PDF.zip",
        README_NAME,
        "90a_EGA0_III_and_EGA3_Assigned_SourceFirst_Controls_20260729.zip",
        SUMMARY_NAME,
    ]
    if len(order) != len(names) or set(order) != names:
        raise RuntimeError("EGA file order is not an exact permutation")
    return order


def upload_file(session, token: str, bucket: str, name: str, path: Path) -> None:
    with path.open("rb") as handle:
        base.check(
            session.put(
                f"{bucket.rstrip('/')}/{quote(name, safe='')}",
                headers={
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/octet-stream",
                },
                data=handle,
                timeout=(30, 1800),
            ),
            {200, 201},
        )


def stage_and_publish(
    session, token: str, live: dict, draft_id: int, local: dict
) -> dict:
    legacy_headers = {"Authorization": f"Bearer {token}"}
    deposition = base.check(
        session.get(
            f"{API}/deposit/depositions/{draft_id}",
            headers=legacy_headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    files = base.legacy_entries(deposition)
    if set(files) != set(base.modern_entries(live)):
        raise RuntimeError("Tracked EGA draft file set changed")
    for name in sorted(REPLACED_NAMES, key=str.casefold):
        existing = files.get(name)
        wanted = local[name]
        if existing is not None and (
            int(existing["filesize"]),
            base.normalized_md5(existing["checksum"]),
        ) == (wanted["bytes"], wanted["md5"]):
            continue
        if existing is not None:
            base.check(
                session.delete(
                    existing["links"]["self"],
                    headers=legacy_headers,
                    timeout=(30, 300),
                ),
                {204},
            )
    deposition = base.check(
        session.get(
            f"{API}/deposit/depositions/{draft_id}",
            headers=legacy_headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    files = base.legacy_entries(deposition)
    bucket = deposition["links"]["bucket"]
    for name in sorted(REPLACED_NAMES, key=str.casefold):
        wanted = local[name]
        existing = files.get(name)
        if existing is not None:
            if (
                int(existing["filesize"]),
                base.normalized_md5(existing["checksum"]),
            ) != (wanted["bytes"], wanted["md5"]):
                raise RuntimeError(f"Staged EGA replacement changed: {name}")
            continue
        print(f"UPLOAD {name}", flush=True)
        upload_file(session, token, bucket, name, wanted["path"])

    headers = auth_headers(token)
    draft = base.check(
        session.get(
            f"{API}/records/{draft_id}/draft?expand=true",
            headers=headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    entries = base.modern_entries(draft)
    inherited = base.modern_entries(live)
    if set(entries) != set(inherited) or len(entries) != EXPECTED_FINAL_FILES:
        raise RuntimeError("Staged EGA successor file set changed")
    for name, entry in entries.items():
        if name in local:
            wanted = local[name]
            expected = (wanted["bytes"], wanted["md5"])
        else:
            old = inherited[name]
            expected = (
                int(old["size"]),
                base.normalized_md5(old["checksum"]),
            )
        observed = (
            int(entry["size"]),
            base.normalized_md5(entry["checksum"]),
        )
        if observed != expected:
            raise RuntimeError(f"Staged EGA identity changed: {name}")

    metadata = copy.deepcopy(draft["metadata"])
    metadata["title"] = TITLE
    metadata["version"] = VERSION
    metadata["publication_date"] = PUBLICATION_DATE
    metadata["description"] = DESCRIPTION_HTML
    metadata["rights"] = [{"id": "notspecified"}]
    metadata["subjects"] = [
        row
        for row in metadata.get("subjects", [])
        if row.get("subject") not in {"public domain", "CC0", "OCR support"}
    ]
    existing_subjects = {row.get("subject") for row in metadata["subjects"]}
    for subject in (
        "source-aligned working reader",
        "reference-v2",
        "complete EGA II",
    ):
        if subject not in existing_subjects:
            metadata["subjects"].append({"subject": subject})
    metadata["additional_descriptions"] = [
        row
        for row in metadata.get("additional_descriptions", [])
        if row.get("type", {}).get("id") != "notes"
    ] + [
        {
            "description": NOTES_HTML,
            "type": {"id": "notes", "title": {"en": "Notes"}},
        }
    ]
    order = ordered_names(set(entries))
    payload = {
        "access": draft["access"],
        "files": {
            "enabled": True,
            "default_preview": DEFAULT_PREVIEW,
            "order": order,
        },
        "metadata": metadata,
        "custom_fields": draft.get("custom_fields", {}),
    }
    if draft.get("pids"):
        payload["pids"] = draft["pids"]
    patched = base.check(
        session.put(
            f"{API}/records/{draft_id}/draft",
            headers={**headers, "Content-Type": "application/json"},
            json=payload,
            timeout=(30, 300),
        ),
        {200},
    ).json()
    rights = patched["metadata"].get("rights", [])
    if (
        set(base.modern_entries(patched)) != set(entries)
        or patched["files"].get("default_preview") != DEFAULT_PREVIEW
        or patched["metadata"].get("version") != VERSION
        or [row.get("id") for row in rights] != ["notspecified"]
    ):
        raise RuntimeError("Patched EGA draft controls changed")
    api_order = patched["files"].get("order") or []
    if api_order and api_order != order:
        raise RuntimeError("Zenodo returned a conflicting EGA file order")
    staged_receipt = {
        "status": "PASS_STAGED",
        "errors": [],
        "predecessor_record": PREDECESSOR_RECORD,
        "draft_id": draft_id,
        "concept_doi": CONCEPT_DOI,
        "files": len(entries),
        "retained_files": EXPECTED_RETAINED_FILES,
        "replaced_files": sorted(REPLACED_NAMES, key=str.casefold),
        "default_preview": DEFAULT_PREVIEW,
        "license": "notspecified",
        "duplicate_concept_created": False,
        "second_draft_created": False,
    }
    base.save_json(
        RECEIPT_ROOT
        / f"20260730_ega2_reference_v2_record_{draft_id}_draft_files.json",
        staged_receipt,
    )
    published = base.check(
        session.post(
            patched["links"]["publish"],
            headers=headers,
            timeout=(30, 600),
        ),
        {200, 202},
    ).json()
    if (
        int(published["id"]) != draft_id
        or published["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI
    ):
        raise RuntimeError("Published EGA response escaped the concept")
    state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
    state.update(
        {
            "published": True,
            "record_id": draft_id,
            "doi": published["pids"]["doi"]["identifier"],
        }
    )
    base.save_json(DRAFT_STATE, state)
    base.save_json(
        RECEIPT_ROOT
        / f"20260730_ega2_reference_v2_record_{draft_id}_publish_response.json",
        {
            "status": "PUBLISH_ACCEPTED",
            "errors": [],
            "record_id": draft_id,
            "doi": published["pids"]["doi"]["identifier"],
            "concept_doi": CONCEPT_DOI,
        },
    )
    return published


def stream_download(session, url: str, destination: Path) -> tuple[int, str, str]:
    destination.parent.mkdir(parents=True, exist_ok=True)
    sha = hashlib.sha256()
    md5 = hashlib.md5(usedforsecurity=False)
    size = 0
    with base.check(
        session.get(url, stream=True, timeout=(30, 1800)), {200}
    ) as response:
        with destination.open("wb") as handle:
            for block in response.iter_content(4 * 1024 * 1024):
                if not block:
                    continue
                handle.write(block)
                sha.update(block)
                md5.update(block)
                size += len(block)
    return size, sha.hexdigest().upper(), md5.hexdigest().lower()


def public_readback(
    session,
    live: dict,
    record_id: int,
    local: dict,
    baseline: dict,
    zip_baseline: dict,
) -> dict:
    record = None
    for _ in range(90):
        response = session.get(
            f"{API}/records/{record_id}?expand=true",
            headers=public_headers(),
            timeout=(30, 180),
        )
        if response.status_code == 200 and response.json().get("is_published"):
            candidate = response.json()
            if len(base.modern_entries(candidate)) == EXPECTED_FINAL_FILES:
                record = candidate
                break
        time.sleep(2)
    if record is None:
        raise RuntimeError("Published EGA successor did not become public")
    entries = base.modern_entries(record)
    predecessor_entries = base.modern_entries(live)
    rights = record["metadata"].get("rights", [])
    if (
        set(entries) != set(predecessor_entries)
        or record["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI
        or record["files"].get("default_preview") != DEFAULT_PREVIEW
        or record["metadata"].get("version") != VERSION
        or [row.get("id") for row in rights] != ["notspecified"]
    ):
        raise RuntimeError("Public EGA successor boundary changed")
    expected_order = ordered_names(set(entries))
    api_order = record["files"].get("order") or []
    if api_order and api_order != expected_order:
        raise RuntimeError("Public EGA file order changed")
    latest = base.check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}/versions/latest?expand=true",
            headers=public_headers(),
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if int(latest["id"]) != record_id:
        raise RuntimeError("Published EGA successor is not the concept head")

    baseline_files = baseline["files"]
    retained_names = set(entries) - REPLACED_NAMES
    if len(retained_names) != EXPECTED_RETAINED_FILES:
        raise RuntimeError("Public EGA retained boundary changed")
    shutil.rmtree(READBACK_ROOT, ignore_errors=True)
    READBACK_ROOT.mkdir(parents=True)
    files: dict[str, dict[str, object]] = {}
    archives: dict[str, dict[str, object]] = {}
    try:
        for index, name in enumerate(expected_order, start=1):
            print(f"PUBLIC READBACK {index}/{len(expected_order)} {name}", flush=True)
            destination = READBACK_ROOT / f"{index:02d}-{Path(name).name}"
            observed = stream_download(
                session, entries[name]["links"]["content"], destination
            )
            if name in local:
                expected = (
                    local[name]["bytes"],
                    local[name]["sha256"],
                    local[name]["md5"],
                )
                mode = "anonymous_full_download_exact_local_sha256"
            else:
                prior = baseline_files.get(name)
                if prior is None:
                    raise RuntimeError(f"Missing retained SHA baseline: {name}")
                expected = (
                    int(prior["bytes"]),
                    prior["sha256"].upper(),
                    prior["md5"].lower(),
                )
                mode = "anonymous_full_download_exact_predecessor_sha256"
            if observed != expected:
                raise RuntimeError(f"Public EGA SHA-256 mismatch: {name}")
            files[name] = {
                "bytes": observed[0],
                "sha256": observed[1],
                "md5": observed[2],
                "url": entries[name]["links"]["content"],
                "match": True,
                "readback_mode": mode,
            }
            if name.lower().endswith(".zip"):
                summary = zip_inventory(destination)
                if name == SOURCE_NAME:
                    validate_source_zip(summary)
                elif name == BUNDLE_NAME:
                    validate_bundle(summary)
                else:
                    prior_zip = zip_baseline["archives"].get(name)
                    if prior_zip is None:
                        raise RuntimeError(f"Missing retained ZIP receipt: {name}")
                    expected_members = compact_member_map(
                        prior_zip.get("member_identities", prior_zip.get("members"))
                    )
                    observed_members = compact_member_map(
                        summary["member_identities"]
                    )
                    if observed_members != expected_members:
                        raise RuntimeError(f"Retained ZIP member drift: {name}")
                archives[name] = summary
            destination.unlink()
    finally:
        shutil.rmtree(READBACK_ROOT, ignore_errors=True)

    if (
        len(files) != EXPECTED_FINAL_FILES
        or sum(int(row["bytes"]) for row in files.values())
        != EXPECTED_FINAL_BYTES
        or len(archives) != EXPECTED_ZIP_ARCHIVES
    ):
        raise RuntimeError("EGA public readback did not close")
    result = {
        "status": "PASS_PUBLIC_READBACK",
        "errors": [],
        "record": record_id,
        "record_url": record["links"]["self_html"],
        "doi": record["pids"]["doi"]["identifier"],
        "conceptdoi": CONCEPT_DOI,
        "predecessor_record": PREDECESSOR_RECORD,
        "version": VERSION,
        "file_count": len(files),
        "bytes": sum(int(row["bytes"]) for row in files.values()),
        "files": files,
        "latest_record": int(latest["id"]),
        "rdm_default_preview": record["files"].get("default_preview"),
        "rdm_file_order": api_order,
        "requested_file_order": expected_order,
        "github_commit": GITHUB_COMMIT,
        "retained_predecessor_files": len(retained_names),
        "replaced_files": sorted(REPLACED_NAMES, key=str.casefold),
        "license": "notspecified",
        "zip_archive_count": len(archives),
        "duplicate_concept_created": False,
        "second_draft_created": False,
    }
    zipped = {
        "status": "PASS",
        "errors": [],
        "record": record_id,
        "doi": record["pids"]["doi"]["identifier"],
        "zip_archive_count": len(archives),
        "archives": archives,
    }
    base.save_json(
        RECEIPT_ROOT
        / f"20260730_ega2_reference_v2_record_{record_id}_public_readback.json",
        result,
    )
    base.save_json(
        RECEIPT_ROOT
        / f"20260730_ega2_reference_v2_record_{record_id}_zip_member_readback.json",
        zipped,
    )
    return result


def preflight() -> dict:
    local = verify_local()
    predecessor, baseline, zip_baseline = load_receipts()
    token = base.find_token()
    session = base.make_session()
    live = fetch_live(session, predecessor)
    assert_no_untracked_draft(session, token)
    retained_names = set(base.modern_entries(live)) - REPLACED_NAMES
    if (
        len(retained_names) != EXPECTED_RETAINED_FILES
        or not retained_names.issubset(baseline["files"])
        or len(zip_baseline["archives"]) != 8
    ):
        raise RuntimeError("EGA predecessor replay boundary changed")
    return {
        "status": "PASS_PREFLIGHT",
        "predecessor_record": PREDECESSOR_RECORD,
        "concept_doi": CONCEPT_DOI,
        "retained_files": len(retained_names),
        "replaced_files": len(local),
        "final_files": EXPECTED_FINAL_FILES,
        "final_bytes": EXPECTED_FINAL_BYTES,
        "source_zip_members": 51,
        "reader_bundle_members": 99,
        "final_zip_archives": EXPECTED_ZIP_ARCHIVES,
        "github_commit": GITHUB_COMMIT,
        "default_preview": DEFAULT_PREVIEW,
        "license": "notspecified",
    }


def publish() -> dict:
    local = verify_local()
    predecessor, baseline, zip_baseline = load_receipts()
    token = base.find_token()
    session = base.make_session()
    live = fetch_live(session, predecessor)
    assert_no_untracked_draft(session, token)
    draft_id = create_or_resume_draft(session, token, live)
    published = stage_and_publish(session, token, live, draft_id, local)
    return public_readback(
        session,
        live,
        int(published["id"]),
        local,
        baseline,
        zip_baseline,
    )


def readback_only() -> dict:
    local = verify_local()
    predecessor, baseline, zip_baseline = load_receipts()
    state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
    if not state.get("published"):
        raise RuntimeError("Tracked EGA successor is not published")
    session = base.make_session()
    live = base.check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}?expand=true",
            headers=public_headers(),
            timeout=(30, 180),
        ),
        {200},
    ).json()
    return public_readback(
        session,
        live,
        int(state["record_id"]),
        local,
        baseline,
        zip_baseline,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--preflight", action="store_true")
    parser.add_argument("--readback-only", action="store_true")
    args = parser.parse_args()
    if args.preflight:
        result = preflight()
    elif args.readback_only:
        result = readback_only()
    else:
        result = publish()
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
