#!/usr/bin/env python3
"""Publish the privacy-clean SGA1 R2 corrective Zenodo successor."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import time
import zipfile
from pathlib import Path, PurePosixPath
from urllib.parse import quote

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


API = "https://zenodo.org/api"
PUBLICATION_DATE = "2026-07-30"
PREDECESSOR_RECORD = 21_703_448
PREDECESSOR_DOI = "10.5281/zenodo.21703448"
CONCEPT_DOI = "10.5281/zenodo.20410947"
EXPECTED_PREDECESSOR_FILES = 67
EXPECTED_PREDECESSOR_BYTES = 449_692_338
EXPECTED_FINAL_FILES = 67
EXPECTED_RETAINED_FILES = 65
DEFAULT_PREVIEW = "00a_SGA1_English_Reader.pdf"
TITLE = "SGA 1-6: English Readers, French Texts, and TeX Archives"
VERSION = "2026-07-30 privacy-clean SGA1 reference-v2 R2 source correction"
GITHUB_COMMIT = "02b1f4ffa7348ab09c49e17fb572193700fded1c"
GITHUB_REPOSITORY = "KokunoYumeto/modern-latex-manuscripts"

REPO_ROOT = Path(__file__).resolve().parent.parent
PACKAGE_ROOT = (
    REPO_ROOT
    / "sources/sga/sga1-english-complete-reference-v2-r2-public-20260730/payload"
)
BUNDLE_PATH = (
    REPO_ROOT
    / "sources/sga/sga1-6-current-readers-and-buildable-tex-bundle-20260730"
    / "00_Current_SGA1-6_English_Readers_and_Buildable_TeX_20260730.zip"
)
PDF_PATH = PACKAGE_ROOT / "SGA1_English_complete_reference_reader.pdf"
TEX_PATH = PACKAGE_ROOT / "SGA1_English_source_sync_workpass.tex"
REPLAY_PATH = PACKAGE_ROOT.parent / "INDEPENDENT_ARCHIVE_REPLAY.json"
RELEASE_BUILD_PATH = PACKAGE_ROOT.parent / "RELEASE_BUILD.json"

BUNDLE_NAME = "00_Current_SGA1-6_English_Readers_and_Buildable_TeX_20260730.zip"
PDF_NAME = "00a_SGA1_English_Reader.pdf"
TEX_NAME = "02a_SGA1_English_Master.tex"
OLD_SOURCE_NAME = "10a_SGA1_English_Source_and_History_R3_20260730.zip"
SOURCE_NAME = "10a_SGA1_English_Source_and_History_R4_20260730.zip"
CONTROLS_NAME = "10z_SGA_Current_Release_Controls_20260730.zip"

EXPECTED_LOCAL = {
    BUNDLE_NAME: (
        23_636_706,
        "56C49D60DAAE7DA8C0F1236EC38A1876C3D3DD36A7D6C365438ABA7E9F9E2660",
    ),
    PDF_NAME: (
        2_763_471,
        "46406925C8EBBF4309A67CF4D84B493952EF99C067E1971F885F0F3AF326BA1E",
    ),
    TEX_NAME: (
        29_494,
        "AF811E732138E82FE9C7A7D0B8C12D0C3A4D2A10C85A9C0757143E6FA2078D26",
    ),
    SOURCE_NAME: (
        5_186_998,
        "D3E3E401822557E538EF0443569666AE7B1939F16EBB2E21C2F30D8FB5FFC4BF",
    ),
}

REPLACED_NAMES = {
    OLD_SOURCE_NAME,
    CONTROLS_NAME,
}
CURRENT_READERS = tuple(
    f"00{chr(96 + index)}_SGA{index}_English_Reader.pdf"
    for index in range(1, 7)
)
CURRENT_TEX = tuple(
    f"02{chr(96 + index)}_SGA{index}_English_Master.tex"
    for index in range(1, 7)
)

TEMP_ROOT = (
    Path(os.environ["LOCALAPPDATA"])
    / "Temp/sga1_reference_v2_zenodo_20260730"
)
SOURCE_PATH = TEMP_ROOT / SOURCE_NAME
CONTROLS_PATH = TEMP_ROOT / CONTROLS_NAME
READBACK_ROOT = TEMP_ROOT / "public_readback"
RECEIPT_ROOT = REPO_ROOT / "manifests/published-zenodo"
DRAFT_STATE = (
    RECEIPT_ROOT
    / "20260730_sga1_reference_v2_r2_privacy_correction_draft_state.json"
)
FIXED_ZIP_TIME = (2026, 7, 30, 12, 0, 0)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def md5_path(path: Path) -> str:
    digest = hashlib.md5(usedforsecurity=False)
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().lower()


def normalized_md5(value: str) -> str:
    return value.lower().removeprefix("md5:")


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=True, indent=2) + "\n").encode(
        "utf-8"
    )


def save_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(json_bytes(value))


def csv_bytes(rows: list[dict[str, object]], fields: list[str]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def read_csv_bytes(data: bytes) -> list[dict[str, str]]:
    return list(
        csv.DictReader(io.StringIO(data.decode("utf-8-sig"), newline=""))
    )


def safe_member(name: str) -> bool:
    pure = PurePosixPath(name)
    return (
        name == name.replace("\\", "/")
        and not pure.is_absolute()
        and ".." not in pure.parts
        and not re.match(r"^[A-Za-z]:", name)
    )


def zip_info(name: str) -> zipfile.ZipInfo:
    if not safe_member(name):
        raise RuntimeError(f"Unsafe ZIP member: {name}")
    info = zipfile.ZipInfo(name, FIXED_ZIP_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    info.create_system = 3
    return info


def check(response: requests.Response, expected: set[int]) -> requests.Response:
    if response.status_code not in expected:
        raise RuntimeError(
            f"Zenodo HTTP {response.status_code} for "
            f"{response.request.method} {response.url}: "
            f"{response.text[:2000]}"
        )
    return response


def make_session() -> requests.Session:
    session = requests.Session()
    retry = Retry(
        total=8,
        connect=8,
        read=8,
        status=8,
        backoff_factor=1.5,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=frozenset({"GET", "HEAD", "PUT"}),
        raise_on_status=False,
    )
    session.mount("https://", HTTPAdapter(max_retries=retry))
    session.headers.update(
        {
            "User-Agent": "modern-latex-manuscripts-archive/1.0",
            "Connection": "close",
        }
    )
    return session


def find_token() -> str:
    direct = os.environ.get("ZENODO_TOKEN")
    if direct:
        return direct
    raise RuntimeError("Set ZENODO_TOKEN before authenticated publication")


def modern_entries(record: dict) -> dict[str, dict]:
    return record["files"]["entries"]


def legacy_entries(record: dict) -> dict[str, dict]:
    return {row["filename"]: row for row in record["files"]}


def public_headers() -> dict[str, str]:
    return {"Accept": "application/vnd.inveniordm.v1+json"}


def auth_headers(token: str) -> dict[str, str]:
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.inveniordm.v1+json",
    }


def verify_identity(path: Path, expected: tuple[int, str]) -> None:
    observed = (path.stat().st_size, sha256_path(path))
    if observed != expected:
        raise RuntimeError(f"Local identity mismatch: {path.name}: {observed}")


def validate_candidate() -> dict:
    manifest_path = PACKAGE_ROOT / "ZENODO_PAYLOAD_MANIFEST.csv"
    validation_path = PACKAGE_ROOT / "PACKAGE_VALIDATION.json"
    rows = read_csv_bytes(manifest_path.read_bytes())
    actual = {
        path.relative_to(PACKAGE_ROOT).as_posix(): path
        for path in PACKAGE_ROOT.rglob("*")
        if path.is_file()
        and path.name not in {"ZENODO_PAYLOAD_MANIFEST.csv", "PACKAGE_VALIDATION.json"}
    }
    indexed = {row["relative_path"]: row for row in rows}
    if len(rows) != 178 or len(indexed) != 178 or set(indexed) != set(actual):
        raise RuntimeError("SGA1 package manifest exact-set closure changed")
    for name, path in actual.items():
        row = indexed[name]
        if (path.stat().st_size, sha256_path(path)) != (
            int(row["bytes"]),
            row["sha256"].upper(),
        ):
            raise RuntimeError(f"SGA1 package member mismatch: {name}")
    validation = json.loads(validation_path.read_text(encoding="utf-8-sig"))
    if validation.get("status") != "PASS" or validation.get("errors"):
        raise RuntimeError("SGA1 packaged validation is not PASS")
    files = sorted(
        (path for path in PACKAGE_ROOT.rglob("*") if path.is_file()),
        key=lambda path: path.relative_to(PACKAGE_ROOT).as_posix(),
    )
    canonical = hashlib.sha256()
    for path in files:
        relative = path.relative_to(PACKAGE_ROOT).as_posix()
        canonical.update(
            (
                f"{relative}\t{path.stat().st_size}\t{sha256_path(path)}\n"
            ).encode("utf-8")
        )
    result = {
        "files": len(files),
        "bytes": sum(path.stat().st_size for path in files),
        "canonical_identity_sha256": canonical.hexdigest().upper(),
        "manifest_rows": len(rows),
        "manifest_sha256": sha256_path(manifest_path),
        "validation_sha256": sha256_path(validation_path),
    }
    if result != {
        "files": 180,
        "bytes": 7_596_171,
        "canonical_identity_sha256": (
            "B203C46448BA5E9CFAE89F368186196CE8A0DF0A2933CF0F82B21D6BF250F385"
        ),
        "manifest_rows": 178,
        "manifest_sha256": (
            "68D412C5270C08D114882E068997ECC14B6B5C069BF0A48A01BE2072BDD846BB"
        ),
        "validation_sha256": (
            "6D355C1F1E599F530E7BE84C3BD89C5E9DDA63F915630FBB49F0E7021D5F9E33"
        ),
    }:
        raise RuntimeError(f"SGA1 package boundary changed: {result!r}")
    return result


def build_source_zip() -> dict:
    TEMP_ROOT.mkdir(parents=True, exist_ok=True)
    temporary = SOURCE_PATH.with_suffix(".zip.tmp")
    temporary.unlink(missing_ok=True)
    files = sorted(
        (path for path in PACKAGE_ROOT.rglob("*") if path.is_file()),
        key=lambda path: path.relative_to(PACKAGE_ROOT).as_posix(),
    )
    root = "SGA1_English_Complete_ReferenceV2_R2_Public_20260730"
    with zipfile.ZipFile(temporary, "w", allowZip64=True) as archive:
        for path in files:
            name = f"{root}/{path.relative_to(PACKAGE_ROOT).as_posix()}"
            archive.writestr(
                zip_info(name), path.read_bytes(), compresslevel=9
            )
    temporary.replace(SOURCE_PATH)
    verify_identity(SOURCE_PATH, EXPECTED_LOCAL[SOURCE_NAME])
    return replay_source_zip(SOURCE_PATH)


def replay_source_zip(path: Path) -> dict:
    expected = {
        f"SGA1_English_Complete_ReferenceV2_R2_Public_20260730/"
        f"{member.relative_to(PACKAGE_ROOT).as_posix()}": member
        for member in PACKAGE_ROOT.rglob("*")
        if member.is_file()
    }
    observed = {}
    with zipfile.ZipFile(path) as archive:
        infos = [row for row in archive.infolist() if not row.is_dir()]
        names = [row.filename for row in infos]
        if (
            len(infos) != 180
            or len(set(names)) != 180
            or set(names) != set(expected)
            or not all(map(safe_member, names))
            or archive.testzip() is not None
        ):
            raise RuntimeError("SGA1 source ZIP boundary changed")
        for name, source in expected.items():
            data = archive.read(name)
            identity = {"bytes": len(data), "sha256": sha256_bytes(data)}
            if (identity["bytes"], identity["sha256"]) != (
                source.stat().st_size,
                sha256_path(source),
            ):
                raise RuntimeError(f"SGA1 source ZIP mismatch: {name}")
            observed[name] = identity
    return {
        "status": "PASS",
        "members": 180,
        "uncompressed_bytes": 7_596_171,
        "member_identities": observed,
    }


def replay_bundle(path: Path) -> dict:
    root = "SGA_Current_English_Readers_and_TeX_20260730"
    manifest_name = f"{root}/SHA256SUMS.csv"
    required = {
        f"{root}/SGA{index}/reader/SGA{index}_English_Reader.pdf"
        for index in range(1, 7)
    }
    observed = {}
    with zipfile.ZipFile(path) as archive:
        infos = [row for row in archive.infolist() if not row.is_dir()]
        names = [row.filename for row in infos]
        if (
            len(infos) != 1_394
            or len(set(names)) != 1_394
            or manifest_name not in names
            or not required.issubset(names)
            or not all(map(safe_member, names))
            or archive.testzip() is not None
        ):
            raise RuntimeError("Current SGA1-6 ZIP boundary changed")
        rows = read_csv_bytes(archive.read(manifest_name))
        if len(rows) != 1_393:
            raise RuntimeError("Current SGA1-6 ZIP manifest rows changed")
        for row in rows:
            name = f"{root}/{row['relative_path']}"
            data = archive.read(name)
            identity = {"bytes": len(data), "sha256": sha256_bytes(data)}
            if (identity["bytes"], identity["sha256"]) != (
                int(row["bytes"]),
                row["sha256"].upper(),
            ):
                raise RuntimeError(f"Current SGA ZIP mismatch: {name}")
            observed[name] = identity
        manifest_data = archive.read(manifest_name)
        observed[manifest_name] = {
            "bytes": len(manifest_data),
            "sha256": sha256_bytes(manifest_data),
        }
        if set(observed) != set(names):
            raise RuntimeError("Current SGA ZIP manifest closure changed")
    return {
        "status": "PASS",
        "members": 1_394,
        "manifest_rows": 1_393,
        "uncompressed_bytes": 39_594_468,
        "required_cumulative_readers": sorted(required),
        "member_identities": observed,
    }


def verify_github_public() -> dict:
    public_main = subprocess.check_output(
        [
            "git",
            "ls-remote",
            f"https://github.com/{GITHUB_REPOSITORY}.git",
            "refs/heads/main",
        ],
        cwd=REPO_ROOT,
        text=True,
    ).split("\t", 1)[0]
    if public_main != GITHUB_COMMIT:
        raise RuntimeError(f"GitHub main changed: {public_main}")
    session = make_session()
    root = (
        "https://raw.githubusercontent.com/"
        f"{GITHUB_REPOSITORY}/{GITHUB_COMMIT}/"
        "sources/sga/sga1-english-complete-reference-v2-r2-public-20260730/payload/"
    )
    checked = {}
    for path in sorted(
        (member for member in PACKAGE_ROOT.rglob("*") if member.is_file()),
        key=lambda member: member.relative_to(PACKAGE_ROOT).as_posix(),
    ):
        relative = path.relative_to(PACKAGE_ROOT).as_posix()
        response = session.get(root + relative, timeout=(30, 600))
        if response.status_code != 200:
            raise RuntimeError(
                f"GitHub raw HTTP {response.status_code}: {relative}"
            )
        data = response.content
        identity = {"bytes": len(data), "sha256": sha256_bytes(data)}
        if (identity["bytes"], identity["sha256"]) != (
            path.stat().st_size,
            sha256_path(path),
        ):
            raise RuntimeError(f"GitHub raw mismatch: {relative}")
        checked[relative] = identity
    bundle_url = (
        "https://raw.githubusercontent.com/"
        f"{GITHUB_REPOSITORY}/{GITHUB_COMMIT}/"
        "sources/sga/sga1-6-current-readers-and-buildable-tex-bundle-20260730/"
        f"{BUNDLE_NAME}"
    )
    response = session.get(bundle_url, timeout=(30, 900))
    if response.status_code != 200 or (
        len(response.content), sha256_bytes(response.content)
    ) != EXPECTED_LOCAL[BUNDLE_NAME]:
        raise RuntimeError("GitHub raw cumulative-reader ZIP mismatch")
    return {
        "status": "PASS_PUBLIC_GITHUB_READBACK",
        "commit": GITHUB_COMMIT,
        "payload_files": len(checked),
        "payload_file_identities": checked,
        "bundle": {
            "bytes": len(response.content),
            "sha256": sha256_bytes(response.content),
        },
    }


def fetch_live(session: requests.Session) -> dict:
    live = check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}/versions/latest",
            headers=public_headers(),
            timeout=(30, 180),
        ),
        {200},
    ).json()
    entries = modern_entries(live)
    observed = (
        int(live["id"]),
        live["pids"]["doi"]["identifier"],
        live["parent"]["pids"]["doi"]["identifier"],
        len(entries),
        sum(int(row["size"]) for row in entries.values()),
        live["files"].get("default_preview"),
    )
    expected = (
        PREDECESSOR_RECORD,
        PREDECESSOR_DOI,
        CONCEPT_DOI,
        EXPECTED_PREDECESSOR_FILES,
        EXPECTED_PREDECESSOR_BYTES,
        DEFAULT_PREVIEW,
    )
    if observed != expected:
        raise RuntimeError(f"Live predecessor boundary changed: {observed!r}")
    if set(CURRENT_READERS + CURRENT_TEX) - set(entries):
        raise RuntimeError("Live direct cumulative readers/TeX are incomplete")
    return live


def fetch_predecessor_manifest(
    session: requests.Session, live: dict
) -> list[dict[str, str]]:
    entry = modern_entries(live)[CONTROLS_NAME]
    response = check(
        session.get(entry["links"]["content"], timeout=(30, 300)), {200}
    )
    if normalized_md5(entry["checksum"]) != hashlib.md5(
        response.content, usedforsecurity=False
    ).hexdigest().lower():
        raise RuntimeError("Predecessor controls ZIP MD5 mismatch")
    with zipfile.ZipFile(io.BytesIO(response.content)) as archive:
        if archive.testzip() is not None:
            raise RuntimeError("Predecessor controls ZIP CRC mismatch")
        accepted_basenames = {
            "09_RELEASE_FILE_MANIFEST.csv",
            "09a_RELEASE_FILE_MANIFEST.csv",
        }
        manifest_names = [
            name
            for name in archive.namelist()
            if PurePosixPath(name).name in accepted_basenames
        ]
        if len(manifest_names) != 1:
            raise RuntimeError(
                "Predecessor controls contain no unique release manifest"
            )
        rows = read_csv_bytes(archive.read(manifest_names[0]))
    if len(rows) != 66 or len({row.get("filename") for row in rows}) != 66:
        raise RuntimeError("Predecessor release manifest boundary changed")
    entries = modern_entries(live)
    expected_names = set(entries) - {CONTROLS_NAME}
    if {row["filename"] for row in rows} != expected_names:
        raise RuntimeError("Predecessor release manifest set changed")
    normalized = []
    for row in rows:
        name = row["filename"]
        try:
            size = int(row["bytes"])
        except (KeyError, TypeError, ValueError) as exc:
            raise RuntimeError(
                f"Predecessor release size is invalid: {name}"
            ) from exc
        digest = row.get("sha256", "").upper()
        if not re.fullmatch(r"[0-9A-F]{64}", digest):
            raise RuntimeError(
                f"Predecessor release SHA-256 is invalid: {name}"
            )
        if size != int(entries[name]["size"]):
            raise RuntimeError(
                f"Predecessor release size disagrees with live record: {name}"
            )
        normalized.append(
            {
                "filename": name,
                "bytes": str(size),
                "sha256": digest,
                "role": row.get("role") or "retained_release_file",
                "provenance": row.get("provenance")
                or f"retained byte-identically from Zenodo record {PREDECESSOR_RECORD}",
                "status": row.get("status")
                or row.get("disposition")
                or "current",
            }
        )
    return normalized


def assert_no_untracked_draft(
    session: requests.Session, token: str
) -> None:
    headers = auth_headers(token)
    if DRAFT_STATE.is_file():
        state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
        if state.get("published"):
            raise RuntimeError("Tracked SGA1 successor is already published")
        response = session.get(
            f"{API}/records/{int(state['draft_id'])}/draft",
            headers=headers,
            timeout=(30, 60),
        )
        check(response, {200})
        return
    response = session.get(
        f"{API}/records/{PREDECESSOR_RECORD}/draft",
        headers=headers,
        timeout=(30, 60),
    )
    if response.status_code == 200:
        raise RuntimeError("Untracked active SGA successor draft exists")
    check(response, {404})


def create_or_resume_draft(
    session: requests.Session, token: str, live: dict
) -> int:
    headers = auth_headers(token)
    if DRAFT_STATE.is_file():
        state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
        draft_id = int(state["draft_id"])
        check(
            session.get(
                f"{API}/records/{draft_id}/draft",
                headers=headers,
                timeout=(30, 60),
            ),
            {200},
        )
        return draft_id
    predecessor = check(
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
        raise RuntimeError("Live predecessor is not a valid version base")
    created = check(
        session.post(
            predecessor["links"]["newversion"],
            headers={"Authorization": f"Bearer {token}"},
            timeout=(30, 300),
        ),
        {201},
    ).json()
    deposition = check(
        session.get(
            created["links"]["latest_draft"],
            headers={"Authorization": f"Bearer {token}"},
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if set(legacy_entries(deposition)) != set(modern_entries(live)):
        raise RuntimeError("Successor did not inherit predecessor exactly")
    draft_id = int(deposition["id"])
    save_json(
        DRAFT_STATE,
        {
            "status": "OPEN_TRACKED_DRAFT",
            "predecessor_record": PREDECESSOR_RECORD,
            "draft_id": draft_id,
            "published": False,
        },
    )
    return draft_id


def build_controls(
    draft_id: int,
    live: dict,
    predecessor_rows: list[dict[str, str]],
) -> dict:
    previous = {row["filename"]: row for row in predecessor_rows}
    entries = modern_entries(live)
    retained_names = set(entries) - REPLACED_NAMES
    if len(retained_names) != EXPECTED_RETAINED_FILES:
        raise RuntimeError("Retained predecessor boundary changed")
    rows = []
    for name in sorted(retained_names, key=str.casefold):
        prior = previous.get(name)
        if prior is None:
            raise RuntimeError(f"Retained release row missing: {name}")
        rows.append(dict(prior))
    new_rows = {
        SOURCE_NAME: {
            "role": "source_archive",
            "provenance": (
                "privacy-clean 180-member SGA1 R2 source, graph, and QA archive; "
                f"GitHub commit {GITHUB_COMMIT}"
            ),
        },
    }
    local_paths = {
        SOURCE_NAME: SOURCE_PATH,
    }
    for name, detail in new_rows.items():
        path = local_paths[name]
        rows.append(
            {
                "filename": name,
                "bytes": path.stat().st_size,
                "sha256": sha256_path(path),
                "role": detail["role"],
                "provenance": detail["provenance"],
                "status": "current",
            }
        )
    rows.sort(key=lambda row: row["filename"].casefold())
    if len(rows) != 66 or len({row["filename"] for row in rows}) != 66:
        raise RuntimeError("Prospective release manifest boundary changed")

    readme = f"""# Current compact SGA release

This is the same-concept corrective successor to Zenodo record
{PREDECESSOR_RECORD}, reserved as record {draft_id}. It retains
{EXPECTED_RETAINED_FILES} files byte-for-byte and replaces only the SGA1
source/history ZIP and this controls ZIP.

The leading bundle contains one cumulative English reader PDF for each of SGA
1 through SGA 6 together with every reader's complete buildable TeX closure.
The same six reader PDFs and master TeX files remain direct downloads, and the
SGA1 reader remains the default preview.

The retained SGA1 reader is the complete 262-page working English reading
edition with 2,151 named destinations and 1,600 resolved internal GoTo actions.
Its R2 public source archive has 180 exact members; five machine-local evidence
paths were sanitized without changing the reader, master, components, graph,
or mathematical text. The 1,394-member current-reader bundle is retained
byte-for-byte. Earlier Zenodo versions remain immutable history.

These are scholarly working translations and TeX editions, not critical
editions, peer review, accessibility certification, or rights determinations.
"""
    validation = {
        "status": "PASS_READY_FOR_SAME_CONCEPT_PUBLICATION",
        "errors": [],
        "source_record": PREDECESSOR_RECORD,
        "reserved_successor_record": draft_id,
        "concept_doi": CONCEPT_DOI,
        "prospective_files": EXPECTED_FINAL_FILES,
        "release_manifest_rows": len(rows),
        "retained_files": EXPECTED_RETAINED_FILES,
        "replaced_files": sorted(REPLACED_NAMES, key=str.casefold),
        "new_files": sorted([SOURCE_NAME, CONTROLS_NAME], key=str.casefold),
        "default_preview": DEFAULT_PREVIEW,
        "sga1_reader": {
            "pages": 262,
            "bytes": EXPECTED_LOCAL[PDF_NAME][0],
            "sha256": EXPECTED_LOCAL[PDF_NAME][1],
            "named_destinations": 2_151,
            "goto_actions": 1_600,
            "broken_or_external_actions": 0,
            "reader_project_ai_workflow_status_hits": 0,
        },
        "current_reader_bundle": {
            "members": 1_394,
            "cumulative_reader_pdfs": 6,
            "bytes": EXPECTED_LOCAL[BUNDLE_NAME][0],
            "sha256": EXPECTED_LOCAL[BUNDLE_NAME][1],
        },
        "sga1_source_zip": {
            "members": 180,
            "uncompressed_bytes": 7_596_171,
            "bytes": EXPECTED_LOCAL[SOURCE_NAME][0],
            "sha256": EXPECTED_LOCAL[SOURCE_NAME][1],
        },
        "privacy_hits": [],
        "new_license_grant": False,
        "duplicate_concept_created": False,
        "second_draft_created": False,
    }
    files = {
        "09_README_CURRENT_RELEASE.md": readme.encode("utf-8"),
        "09a_RELEASE_FILE_MANIFEST.csv": csv_bytes(
            rows,
            [
                "filename",
                "bytes",
                "sha256",
                "role",
                "provenance",
                "status",
            ],
        ),
        "09b_RELEASE_VALIDATION.json": json_bytes(validation),
        "09c_SGA1_INDEPENDENT_ARCHIVE_REPLAY.json": REPLAY_PATH.read_bytes(),
        "09d_SGA1_PACKAGE_SHA256SUMS.csv": (
            PACKAGE_ROOT / "ZENODO_PAYLOAD_MANIFEST.csv"
        ).read_bytes(),
        "09e_SGA1_RELEASE_BUILD.json": RELEASE_BUILD_PATH.read_bytes(),
    }
    packed_rows = [
        {
            "filename": name,
            "bytes": len(data),
            "sha256": sha256_bytes(data),
        }
        for name, data in sorted(files.items(), key=lambda item: item[0].casefold())
    ]
    files["PACKED_CONTROL_SHA256.csv"] = csv_bytes(
        packed_rows, ["filename", "bytes", "sha256"]
    )
    CONTROLS_PATH.unlink(missing_ok=True)
    with zipfile.ZipFile(
        CONTROLS_PATH, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9
    ) as archive:
        for name, data in sorted(files.items(), key=lambda item: item[0].casefold()):
            archive.writestr(zip_info(name), data, compresslevel=9)
    replay_controls(CONTROLS_PATH)
    return {
        "files": files,
        "identity": {
            "bytes": CONTROLS_PATH.stat().st_size,
            "sha256": sha256_path(CONTROLS_PATH),
        },
    }


def replay_controls(path: Path) -> dict:
    observed = {}
    with zipfile.ZipFile(path) as archive:
        infos = [row for row in archive.infolist() if not row.is_dir()]
        names = [row.filename for row in infos]
        if (
            len(infos) != 7
            or len(set(names)) != 7
            or "PACKED_CONTROL_SHA256.csv" not in names
            or archive.testzip() is not None
            or not all(map(safe_member, names))
        ):
            raise RuntimeError("Release controls ZIP boundary changed")
        rows = read_csv_bytes(archive.read("PACKED_CONTROL_SHA256.csv"))
        if len(rows) != 6:
            raise RuntimeError("Release controls packed manifest changed")
        for row in rows:
            data = archive.read(row["filename"])
            identity = {"bytes": len(data), "sha256": sha256_bytes(data)}
            if (identity["bytes"], identity["sha256"]) != (
                int(row["bytes"]),
                row["sha256"].upper(),
            ):
                raise RuntimeError(
                    f"Release controls member mismatch: {row['filename']}"
                )
            observed[row["filename"]] = identity
        packed = archive.read("PACKED_CONTROL_SHA256.csv")
        observed["PACKED_CONTROL_SHA256.csv"] = {
            "bytes": len(packed),
            "sha256": sha256_bytes(packed),
        }
        if set(observed) != set(names):
            raise RuntimeError("Release controls manifest closure changed")
    return {
        "status": "PASS",
        "members": 7,
        "member_identities": observed,
    }


def upload_file(
    session: requests.Session,
    token: str,
    bucket: str,
    name: str,
    path: Path,
) -> None:
    with path.open("rb") as handle:
        check(
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


def ordered_names(names: set[str]) -> list[str]:
    direct = set(CURRENT_READERS) | set(CURRENT_TEX)
    if not direct.issubset(names):
        raise RuntimeError("Direct current reader/TeX set changed")
    remainder = names - direct - {BUNDLE_NAME}
    other_pdfs = sorted(
        (name for name in remainder if name.lower().endswith(".pdf")),
        key=str.casefold,
    )
    other_tex = sorted(
        (name for name in remainder if name.lower().endswith(".tex")),
        key=str.casefold,
    )
    archives = sorted(
        remainder - set(other_pdfs) - set(other_tex), key=str.casefold
    )
    order = (
        [BUNDLE_NAME]
        + list(CURRENT_READERS)
        + list(CURRENT_TEX)
        + other_pdfs
        + other_tex
        + archives
    )
    if len(order) != len(names) or set(order) != names:
        raise RuntimeError("Final file order is not a permutation")
    return order


def stage_and_publish(
    session: requests.Session,
    token: str,
    live: dict,
    draft_id: int,
) -> dict:
    legacy_headers = {"Authorization": f"Bearer {token}"}
    deposition = check(
        session.get(
            f"{API}/deposit/depositions/{draft_id}",
            headers=legacy_headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    inherited = set(modern_entries(live))
    files = legacy_entries(deposition)
    uploads = {
        SOURCE_NAME: SOURCE_PATH,
        CONTROLS_NAME: CONTROLS_PATH,
    }
    allowed_names = (
        inherited
        | set(uploads)
        | {OLD_SOURCE_NAME}
    )
    if not set(files).issubset(allowed_names):
        raise RuntimeError("Tracked draft contains an unexpected file")
    for name in REPLACED_NAMES:
        existing = files.get(name)
        if existing is None:
            continue
        wanted = uploads.get(name)
        if wanted is not None and (
            int(existing["filesize"]),
            normalized_md5(existing["checksum"]),
        ) == (wanted.stat().st_size, md5_path(wanted)):
            continue
        check(
            session.delete(
                existing["links"]["self"],
                headers=legacy_headers,
                timeout=(30, 300),
            ),
            {204},
        )
    deposition = check(
        session.get(
            f"{API}/deposit/depositions/{draft_id}",
            headers=legacy_headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    files = legacy_entries(deposition)
    bucket = deposition["links"]["bucket"]
    for name, path in uploads.items():
        existing = files.get(name)
        if existing is not None:
            if (
                int(existing["filesize"]),
                normalized_md5(existing["checksum"]),
            ) != (path.stat().st_size, md5_path(path)):
                raise RuntimeError(f"Staged upload identity changed: {name}")
            continue
        upload_file(session, token, bucket, name, path)

    headers = auth_headers(token)
    draft = check(
        session.get(
            f"{API}/records/{draft_id}/draft",
            headers=headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    entries = modern_entries(draft)
    expected_names = inherited - {OLD_SOURCE_NAME} | {SOURCE_NAME}
    if set(entries) != expected_names or len(entries) != EXPECTED_FINAL_FILES:
        raise RuntimeError("Staged successor file set changed")
    retained = inherited - REPLACED_NAMES
    for name in retained:
        old = modern_entries(live)[name]
        new = entries[name]
        if (
            int(new["size"]),
            normalized_md5(new["checksum"]),
        ) != (
            int(old["size"]),
            normalized_md5(old["checksum"]),
        ):
            raise RuntimeError(f"Retained staged file changed: {name}")
    for name, path in uploads.items():
        entry = entries[name]
        if (
            int(entry["size"]),
            normalized_md5(entry["checksum"]),
        ) != (path.stat().st_size, md5_path(path)):
            raise RuntimeError(f"Staged upload identity changed: {name}")

    metadata = dict(draft["metadata"])
    description = metadata.get("description", "")
    start = (
        "<p><strong>SGA1 R2 source correction:</strong> the complete "
        "262-page reader, direct master TeX, and leading SGA1-6 cumulative "
        "PDF/buildable-TeX bundle are retained byte-for-byte. The grouped "
        "SGA1 source/history archive is replaced by its privacy-clean R2 "
        "projection; five machine-local paths were sanitized without "
        "changing the mathematical reader or source.</p>"
    )
    metadata["title"] = TITLE
    metadata["version"] = VERSION
    metadata["publication_date"] = PUBLICATION_DATE
    metadata["description"] = start + "\n" + description
    metadata["contributors"] = []
    metadata["additional_descriptions"] = [
        row
        for row in (metadata.get("additional_descriptions") or [])
        if row.get("type", {}).get("id") != "notes"
    ]
    order = ordered_names(expected_names)
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
    patched = check(
        session.put(
            f"{API}/records/{draft_id}/draft",
            headers={**headers, "Content-Type": "application/json"},
            json=payload,
            timeout=(30, 300),
        ),
        {200},
    ).json()
    if (
        set(modern_entries(patched)) != expected_names
        or patched["files"].get("default_preview") != DEFAULT_PREVIEW
        or patched["metadata"].get("contributors")
        or patched["metadata"].get("version") != VERSION
    ):
        raise RuntimeError("Patched draft controls changed")
    api_order = patched["files"].get("order") or []
    if api_order and api_order != order:
        raise RuntimeError("Zenodo returned a conflicting file order")
    published = check(
        session.post(
            patched["links"]["publish"], headers=headers, timeout=(30, 600)
        ),
        {200, 202},
    ).json()
    if (
        int(published["id"]) != draft_id
        or published["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI
    ):
        raise RuntimeError("Published response escaped the existing concept")
    state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
    state.update(
        {
            "published": True,
            "record_id": draft_id,
            "doi": published["pids"]["doi"]["identifier"],
        }
    )
    save_json(DRAFT_STATE, state)
    return published


def stream_download(
    session: requests.Session, url: str, path: Path
) -> tuple[int, str]:
    path.parent.mkdir(parents=True, exist_ok=True)
    digest = hashlib.sha256()
    total = 0
    with check(session.get(url, stream=True, timeout=(30, 1800)), {200}) as response:
        with path.open("wb") as handle:
            for block in response.iter_content(4 * 1024 * 1024):
                if block:
                    handle.write(block)
                    digest.update(block)
                    total += len(block)
    return total, digest.hexdigest().upper()


def public_readback(
    session: requests.Session,
    live: dict,
    record_id: int,
    github: dict,
) -> dict:
    record = None
    for _ in range(45):
        response = session.get(
            f"{API}/records/{record_id}",
            headers=public_headers(),
            timeout=(30, 180),
        )
        if response.status_code == 200 and response.json().get("is_published"):
            record = response.json()
            break
        time.sleep(2)
    if record is None:
        raise RuntimeError("Published successor did not become public")
    entries = modern_entries(record)
    predecessor_entries = modern_entries(live)
    expected_names = set(predecessor_entries) - {OLD_SOURCE_NAME} | {SOURCE_NAME}
    if (
        set(entries) != expected_names
        or len(entries) != EXPECTED_FINAL_FILES
        or record["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI
        or record["files"].get("default_preview") != DEFAULT_PREVIEW
        or record["metadata"].get("version") != VERSION
        or record["metadata"].get("contributors")
    ):
        raise RuntimeError("Public successor boundary changed")
    expected_order = ordered_names(expected_names)
    api_order = record["files"].get("order") or []
    if api_order and api_order != expected_order:
        raise RuntimeError("Public file order changed")
    retained_names = set(predecessor_entries) - REPLACED_NAMES
    retained = {}
    for name in retained_names:
        old = predecessor_entries[name]
        new = entries[name]
        identity = {
            "bytes": int(new["size"]),
            "md5": normalized_md5(new["checksum"]),
        }
        if (identity["bytes"], identity["md5"]) != (
            int(old["size"]),
            normalized_md5(old["checksum"]),
        ):
            raise RuntimeError(f"Public retained file changed: {name}")
        retained[name] = identity

    wanted = {
        BUNDLE_NAME: EXPECTED_LOCAL[BUNDLE_NAME],
        PDF_NAME: EXPECTED_LOCAL[PDF_NAME],
        TEX_NAME: EXPECTED_LOCAL[TEX_NAME],
        SOURCE_NAME: EXPECTED_LOCAL[SOURCE_NAME],
        CONTROLS_NAME: (CONTROLS_PATH.stat().st_size, sha256_path(CONTROLS_PATH)),
    }
    readback = {}
    for name, expected in wanted.items():
        destination = READBACK_ROOT / name
        observed = stream_download(
            session, entries[name]["links"]["content"], destination
        )
        if observed != expected:
            raise RuntimeError(f"Public SHA-256 readback mismatch: {name}")
        readback[name] = {
            "bytes": observed[0],
            "sha256": observed[1],
            "content_url": entries[name]["links"]["content"],
        }
    bundle_receipt = replay_bundle(READBACK_ROOT / BUNDLE_NAME)
    source_receipt = replay_source_zip(READBACK_ROOT / SOURCE_NAME)
    controls_receipt = replay_controls(READBACK_ROOT / CONTROLS_NAME)
    outer = {
        name: {
            "bytes": int(entry["size"]),
            "md5": normalized_md5(entry["checksum"]),
        }
        for name, entry in entries.items()
    }
    result = {
        "status": "PASS_PUBLIC_READBACK",
        "record_id": int(record["id"]),
        "record_url": record["links"]["self_html"],
        "doi": record["pids"]["doi"]["identifier"],
        "concept_doi": record["parent"]["pids"]["doi"]["identifier"],
        "predecessor_record": PREDECESSOR_RECORD,
        "github": github,
        "outer_files": len(entries),
        "outer_bytes": sum(int(entry["size"]) for entry in entries.values()),
        "retained_predecessor_files": len(retained),
        "default_preview": record["files"].get("default_preview"),
        "configured_file_order": expected_order,
        "api_file_order": api_order,
        "new_file_readback": readback,
        "outer_file_identities": outer,
        "retained_file_identities": retained,
        "bundle_readback": bundle_receipt,
        "source_zip_readback": source_receipt,
        "controls_zip_readback": controls_receipt,
        "duplicate_concept_created": False,
        "second_draft_created": False,
    }
    prefix = f"20260730_sga1_reference_v2_record_{record_id}"
    save_json(RECEIPT_ROOT / f"{prefix}_public_readback.json", result)
    save_json(
        RECEIPT_ROOT / f"{prefix}_bundle_member_readback.json",
        bundle_receipt,
    )
    save_json(
        RECEIPT_ROOT / f"{prefix}_source_zip_member_readback.json",
        source_receipt,
    )
    save_json(
        RECEIPT_ROOT / f"{prefix}_controls_zip_member_readback.json",
        controls_receipt,
    )
    return result


def preflight() -> dict:
    verify_identity(BUNDLE_PATH, EXPECTED_LOCAL[BUNDLE_NAME])
    verify_identity(PDF_PATH, EXPECTED_LOCAL[PDF_NAME])
    verify_identity(TEX_PATH, EXPECTED_LOCAL[TEX_NAME])
    candidate = validate_candidate()
    source = build_source_zip()
    bundle = replay_bundle(BUNDLE_PATH)
    github = verify_github_public()
    token = find_token()
    session = make_session()
    live = fetch_live(session)
    fetch_predecessor_manifest(session, live)
    assert_no_untracked_draft(session, token)
    return {
        "status": "PASS_PREFLIGHT",
        "candidate": candidate,
        "source_zip": source,
        "bundle": {
            key: value for key, value in bundle.items() if key != "member_identities"
        },
        "github": {
            key: value
            for key, value in github.items()
            if key != "payload_file_identities"
        },
        "live_record": int(live["id"]),
        "live_doi": live["pids"]["doi"]["identifier"],
        "concept_doi": live["parent"]["pids"]["doi"]["identifier"],
        "live_files": len(modern_entries(live)),
        "default_preview": live["files"].get("default_preview"),
    }


def publish() -> dict:
    verify_identity(BUNDLE_PATH, EXPECTED_LOCAL[BUNDLE_NAME])
    verify_identity(PDF_PATH, EXPECTED_LOCAL[PDF_NAME])
    verify_identity(TEX_PATH, EXPECTED_LOCAL[TEX_NAME])
    validate_candidate()
    build_source_zip()
    replay_bundle(BUNDLE_PATH)
    github = verify_github_public()
    token = find_token()
    session = make_session()
    live = fetch_live(session)
    predecessor_rows = fetch_predecessor_manifest(session, live)
    assert_no_untracked_draft(session, token)
    draft_id = create_or_resume_draft(session, token, live)
    build_controls(draft_id, live, predecessor_rows)
    published = stage_and_publish(session, token, live, draft_id)
    result = public_readback(session, live, int(published["id"]), github)
    save_json(TEMP_ROOT / "publication_summary.json", result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--preflight-only", action="store_true")
    args = parser.parse_args()
    result = preflight() if args.preflight_only else publish()
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
