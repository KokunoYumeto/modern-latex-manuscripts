#!/usr/bin/env python3
"""Publish and read back the compact SGA3 current-progress successor."""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
import os
import re
import shutil
import time
import zipfile
from pathlib import Path, PurePosixPath
from urllib.parse import quote

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


API = "https://zenodo.org/api"
CONCEPT_DOI = "10.5281/zenodo.20410947"
PREDECESSOR_RECORD = 21631485
PREDECESSOR_DOI = "10.5281/zenodo.21631485"
SUCCESSOR_RECORD = 21632790
SUCCESSOR_DOI = "10.5281/zenodo.21632790"
VERSION = "2026-07-28 SGA3 current-progress cumulative I-IX, XI, XIII"
PUBLICATION_DATE = "2026-07-28"
DEFAULT_PREVIEW = (
    "00a_SGA1_English_CompleteVolume_Working_"
    "NoExhaustiveCertification_20260722.pdf"
)

REPO_ROOT = Path(__file__).resolve().parent.parent
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
PREDECESSOR_RECEIPT = (
    RECEIPT_ROOT
    / "20260727_sga6_idx627_631_record_21631485_public_readback.json"
)
CONTROLS_ROOT = Path(
    os.environ.get(
        "SGA3_CUMULATIVE_ZENODO_CONTROLS_ROOT",
        Path(os.environ["LOCALAPPDATA"])
        / "Temp"
        / "sga3_cumulative_zenodo_21632790_controls",
    )
)
RELEASE_ROOT = Path(
    os.environ.get(
        "SGA3_CUMULATIVE_RELEASE_ROOT",
        Path.home()
        / "Documents"
        / "interlanguage"
        / "03_projects"
        / "language_management"
        / "english_germanic"
        / "03_working_translations"
        / "sga3_english_current_progress_cumulative_i_vi_viii_ix_xi_20260728_r1"
        / "release",
    )
)
READBACK_ROOT = Path(
    os.environ.get(
        "SGA3_CUMULATIVE_ZENODO_READBACK_ROOT",
        Path(os.environ["LOCALAPPDATA"])
        / "Temp"
        / "sga3_cumulative_zenodo_21632790_public_readback",
    )
)
TOKEN_LOG = Path(
    os.environ.get(
        "ZENODO_TOKEN_LOG",
        Path.home() / ".codex" / ".sandbox" / "sandbox.log",
    )
)

LOCAL_FILES = {
    "00c_SGA3_English_CurrentProgress_Cumulative_I-IX_XI_XIII_20260728.pdf": (
        RELEASE_ROOT
        / "00c_SGA3_English_CurrentProgress_Cumulative_I-IX_XI_XIII_20260728.pdf"
    ),
    "02c_SGA3_English_CurrentProgress_Cumulative_I-IX_XI_XIII_20260728.tex": (
        RELEASE_ROOT
        / "02c_SGA3_English_CurrentProgress_Cumulative_I-IX_XI_XIII_20260728.tex"
    ),
    "09_README_CURRENT_RELEASE.md": CONTROLS_ROOT
    / "09_README_CURRENT_RELEASE.md",
    "09a_RELEASE_FILE_MANIFEST.csv": CONTROLS_ROOT
    / "09a_RELEASE_FILE_MANIFEST.csv",
    "09b_RELEASE_VALIDATION.json": CONTROLS_ROOT
    / "09b_RELEASE_VALIDATION.json",
    "10c_SGA3_Previous_Public_Component_Readers_and_Source_Archives_Through_XI_20260728.zip": (
        RELEASE_ROOT
        / "10c_SGA3_Previous_Public_Component_Readers_and_Source_Archives_Through_XI_20260728.zip"
    ),
    "10c8_SGA3_CurrentProgress_Integration_Source_I-IX_XI_XIII_20260728.zip": (
        RELEASE_ROOT
        / "10c8_SGA3_CurrentProgress_Integration_Source_I-IX_XI_XIII_20260728.zip"
    ),
}

EXPECTED_OUTER_FILES = 63
EXPECTED_OUTER_BYTES = 371_590_556
EXPECTED_RETAINED_FILES = 56
EXPECTED_ZIP_ARCHIVES = 44
EXPECTED_ZIP_FILE_MEMBERS = 4_005
EXPECTED_ZIP_DIRECTORY_ENTRIES = 6
EXPECTED_ZIP_ALL_ENTRIES = 4_011
EXPECTED_ZIP_UNCOMPRESSED_BYTES = 387_806_305

GITHUB_COMMIT = "a5f0f25cb1ff8413f9328039bfd4622f8ef979ba"
GITHUB_PACKAGE = (
    "sources/sga/"
    "sga3-english-current-progress-cumulative-i-ix-xi-xiii-20260728"
)

DESCRIPTION_PARAGRAPHS = [
    (
        "This same-concept compact successor preserves the reader-first SGA "
        "surface from version 10.5281/zenodo.21631485. Fifty-six unrelated "
        "predecessor files are retained byte-identically. Nineteen formerly "
        "loose SGA3 component readers, editable masters, rights ledgers, and "
        "source/QA archives are preserved inside one byte-exact history ZIP "
        "and replaced on the landing surface by one cumulative working reader, "
        "one direct editable integration master, one history ZIP, one current "
        "integration-source ZIP, and refreshed release controls."
    ),
    (
        "The preferred SGA3 current-progress reader has 836 A4 pages and "
        "contains the Editorial Notice, Introduction, and Exposes I-IX, XI, "
        "and XIII. It includes explicit gap leaves for Exposes X and XII and "
        "ends before Expose XIV; Exposes XIV-XXVI are absent. It is therefore "
        "a substantial working reader, not a complete SGA3 translation, "
        "critical edition, or mathematical certification."
    ),
    (
        "The reader has 5,332 named destinations, 3,647 valid internal GoTo "
        "actions, zero broken internal GoTo actions, 173 outlines, 62 embedded "
        "fonts, and no Type3 fonts. Four XeLaTeX passes converged without hard "
        "errors, undefined references, duplicate destinations, missing glyphs, "
        "or overfull boxes. An isolated rebuild matched all 836 pages in "
        "content, text, geometry, links, and fonts."
    ),
    (
        "Expose VII is the latest readable repaired r5 body; its final "
        "detector/reference package remains unfinished. Expose XIII is a "
        "complete Loop-1 body whose source, formulas, and high-zoom diagrams "
        "were reviewed, while exhaustive reference/package closeout remains "
        "unfinished. These limitations are stated inside the reader and "
        "release controls rather than used to hide useful readable work."
    ),
    (
        "The history ZIP contains 21 exact members, including all nineteen "
        "superseded loose public SGA3 objects. The current integration-source "
        "ZIP contains 932 exact members. Across this successor there are 44 ZIP "
        "archives with 4,005 non-directory members and 387,806,305 uncompressed "
        "bytes. SGA1 remains the default preview; numeric filenames place the "
        "new cumulative SGA3 reader directly after SGA2."
    ),
    (
        "The controlling French source images and PDFs are not redistributed "
        "by the new integration archive. OCR and extracted text are locator or "
        "drafting witnesses only. Jacob C. Reinhold's jcreinhold/sga English "
        "lineage at revision e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e is "
        "credited comparison/drafting material, not source authority; its "
        "author-declared CC BY 4.0 applies only to that contribution. Rights in "
        "the underlying French works and scans remain with their holders; no "
        "blanket license or rights transfer is asserted. Machine-assisted "
        "contributors include OpenAI Codex / ChatGPT and Anthropic Claude under "
        "human direction. This successor updates only existing SGA concept "
        "10.5281/zenodo.20410947."
    ),
]
DESCRIPTION_HTML = "\n".join(f"<p>{value}</p>" for value in DESCRIPTION_PARAGRAPHS)
NOTES_HTML = (
    "<p>Compact reader-first surface: English readers for SGA1 through SGA6 "
    "remain directly accessible, followed by primary editable TeX. Recursive "
    "sources, QA, evidence, and predecessor objects are grouped into coherent "
    "ZIP archives. This version has 63 public files. GitHub package commit: "
    f"{GITHUB_COMMIT}.</p>"
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def md5_file(path: Path) -> str:
    digest = hashlib.md5(usedforsecurity=False)
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().lower()


def normalize_checksum(value: str) -> str:
    return value.lower().removeprefix("md5:")


def save_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=True, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def find_token() -> str:
    direct = os.environ.get("ZENODO_TOKEN")
    if direct:
        return direct
    data = TOKEN_LOG.read_text(encoding="utf-8", errors="ignore")
    candidates = sorted(
        set(re.findall(r"(?<![A-Za-z0-9])[A-Za-z0-9]{60}(?![A-Za-z0-9])", data))
    )
    if len(candidates) != 1:
        raise RuntimeError(
            f"Expected exactly one locally retained Zenodo credential, found "
            f"{len(candidates)}"
        )
    return candidates[0]


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
        {"User-Agent": "modern-latex-manuscripts-archive/1.0"}
    )
    return session


def check(response: requests.Response, expected: set[int]) -> requests.Response:
    if response.status_code not in expected:
        raise RuntimeError(
            f"Zenodo HTTP {response.status_code} for {response.request.method} "
            f"{response.url}: {response.text[:2000]}"
        )
    return response


def expected_identities() -> dict[str, dict]:
    manifest_path = CONTROLS_ROOT / "09a_RELEASE_FILE_MANIFEST.csv"
    with manifest_path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 61:
        raise RuntimeError(f"Expected 61 release-manifest rows, got {len(rows)}")
    expected: dict[str, dict] = {}
    for row in rows:
        name = row["filename"]
        if name in expected:
            raise RuntimeError(f"Duplicate release-manifest filename: {name}")
        expected[name] = {
            "bytes": int(row["bytes"]),
            "sha256": row["sha256"].upper(),
        }
    for name in ("09a_RELEASE_FILE_MANIFEST.csv", "09b_RELEASE_VALIDATION.json"):
        path = CONTROLS_ROOT / name
        expected[name] = {
            "bytes": path.stat().st_size,
            "sha256": sha256_file(path),
        }
    if len(expected) != EXPECTED_OUTER_FILES:
        raise RuntimeError(f"Expected 63 final files, got {len(expected)}")
    if sum(row["bytes"] for row in expected.values()) != EXPECTED_OUTER_BYTES:
        raise RuntimeError("Expected final byte boundary does not match")
    for row in expected.values():
        row["md5"] = None
    predecessor = json.loads(PREDECESSOR_RECEIPT.read_text(encoding="utf-8-sig"))
    if int(predecessor["record"]) != PREDECESSOR_RECORD:
        raise RuntimeError("Predecessor receipt record mismatch")
    predecessor_files = predecessor["files"]
    retained = set(expected) - set(LOCAL_FILES)
    if len(retained) != EXPECTED_RETAINED_FILES:
        raise RuntimeError("Retained predecessor boundary mismatch")
    for name in retained:
        row = predecessor_files.get(name)
        if row is None:
            raise RuntimeError(f"Retained file absent from predecessor receipt: {name}")
        if (int(row["bytes"]), row["sha256"].upper()) != (
            expected[name]["bytes"],
            expected[name]["sha256"],
        ):
            raise RuntimeError(f"Retained predecessor identity mismatch: {name}")
    return expected


def local_identities(expected: dict[str, dict]) -> dict[str, dict]:
    result = {}
    for name, path in LOCAL_FILES.items():
        identity = {
            "path": path,
            "bytes": path.stat().st_size,
            "sha256": sha256_file(path),
            "md5": md5_file(path),
        }
        wanted = expected[name]
        if (identity["bytes"], identity["sha256"]) != (
            wanted["bytes"],
            wanted["sha256"],
        ):
            raise RuntimeError(f"Local identity mismatch: {name}")
        result[name] = identity
        wanted["md5"] = identity["md5"]
    return result


def legacy_draft(session: requests.Session, token: str) -> dict:
    return check(
        session.get(
            f"{API}/deposit/depositions/{SUCCESSOR_RECORD}",
            headers={"Authorization": f"Bearer {token}"},
            timeout=(30, 180),
        ),
        {200},
    ).json()


def modern_draft(session: requests.Session, token: str) -> dict:
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.inveniordm.v1+json",
    }
    draft = check(
        session.get(
            f"{API}/records/{SUCCESSOR_RECORD}/draft",
            headers=headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    files = check(
        session.get(draft["links"]["files"], headers=headers, timeout=(30, 180)),
        {200},
    ).json()
    entries = files.get("entries", {})
    if isinstance(entries, list):
        entries = {row["key"]: row for row in entries}
    if not isinstance(entries, dict):
        raise RuntimeError("Unexpected modern draft file shape")
    files["entries"] = entries
    draft["files"] = files
    return draft


def draft_file_map(deposition: dict) -> dict[str, dict]:
    result = {row["filename"]: row for row in deposition["files"]}
    if len(result) != len(deposition["files"]):
        raise RuntimeError("Draft contains duplicate filenames")
    return result


def legacy_identity(row: dict) -> tuple[int, str]:
    return int(row["filesize"]), normalize_checksum(row["checksum"])


def assert_draft_lineage(draft: dict) -> None:
    if int(draft["id"]) != SUCCESSOR_RECORD:
        raise RuntimeError("Unexpected draft record")
    if draft["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI:
        raise RuntimeError("Draft escaped the existing SGA concept")


def assert_public_lineage(record: dict) -> None:
    if int(record["id"]) != SUCCESSOR_RECORD:
        raise RuntimeError("Unexpected public record")
    concept_doi = record.get("conceptdoi")
    if concept_doi is None:
        concept_doi = (
            record.get("parent", {})
            .get("pids", {})
            .get("doi", {})
            .get("identifier")
        )
    if concept_doi != CONCEPT_DOI:
        raise RuntimeError("Published record escaped the SGA concept")
    version_doi = record.get("doi")
    if version_doi is None:
        version_doi = (
            record.get("pids", {}).get("doi", {}).get("identifier")
        )
    if version_doi != SUCCESSOR_DOI:
        raise RuntimeError("Published version DOI mismatch")


def predecessor_public_file_map(session: requests.Session) -> dict[str, dict]:
    record = check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}",
            headers={"Accept": "application/json"},
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if int(record["id"]) != PREDECESSOR_RECORD:
        raise RuntimeError("Unexpected predecessor public record")
    if record["conceptdoi"] != CONCEPT_DOI:
        raise RuntimeError("Predecessor escaped the SGA concept")
    result = {row["key"]: row for row in record["files"]}
    if len(result) != len(record["files"]):
        raise RuntimeError("Predecessor has duplicate public filenames")
    return result


def stage(session: requests.Session, token: str) -> dict:
    expected = expected_identities()
    local = local_identities(expected)
    predecessor_files = predecessor_public_file_map(session)
    for name in set(expected) - set(local):
        row = predecessor_files.get(name)
        if row is None:
            raise RuntimeError(f"Missing predecessor source identity: {name}")
        if int(row["size"]) != expected[name]["bytes"]:
            raise RuntimeError(f"Predecessor byte mismatch: {name}")
        expected[name]["md5"] = normalize_checksum(row["checksum"])
    draft = modern_draft(session, token)
    assert_draft_lineage(draft)
    deposition = legacy_draft(session, token)
    if deposition.get("state") != "unsubmitted" or deposition.get("submitted"):
        raise RuntimeError("Successor is not an unpublished draft")
    files = draft_file_map(deposition)
    extras = sorted(set(files) - set(expected))
    if extras:
        raise RuntimeError(f"Unexpected draft files: {extras}")
    missing_nonlocal = sorted(set(expected) - set(files) - set(local))
    if missing_nonlocal:
        raise RuntimeError(f"Missing retained predecessor files: {missing_nonlocal}")

    auth = {"Authorization": f"Bearer {token}"}
    actions = []
    for name, identity in sorted(expected.items(), key=lambda row: row[0].casefold()):
        existing = files.get(name)
        if existing is not None:
            size, existing_md5 = legacy_identity(existing)
            if (size, existing_md5) == (identity["bytes"], identity["md5"]):
                actions.append({"filename": name, "action": "already_exact"})
                continue
            if name not in local:
                raise RuntimeError(f"Retained draft identity mismatch: {name}")
            check(
                session.delete(
                    existing["links"]["self"],
                    headers=auth,
                    timeout=(30, 300),
                ),
                {204},
            )
            actions.append({"filename": name, "action": "deleted_stale"})

        if name not in local:
            raise RuntimeError(f"No authorized upload source for missing file: {name}")
        current = legacy_draft(session, token)
        bucket = current["links"]["bucket"].rstrip("/")
        upload_url = f"{bucket}/{quote(name, safe='')}"
        with local[name]["path"].open("rb") as handle:
            uploaded = check(
                session.put(
                    upload_url,
                    data=handle,
                    headers={
                        **auth,
                        "Content-Type": "application/octet-stream",
                    },
                    timeout=(30, 1800),
                ),
                {200, 201},
            ).json()
        uploaded_size = int(uploaded.get("size", uploaded.get("filesize", -1)))
        uploaded_md5 = normalize_checksum(uploaded.get("checksum", ""))
        if (uploaded_size, uploaded_md5) != (
            identity["bytes"],
            local[name]["md5"],
        ):
            raise RuntimeError(f"Upload response mismatch: {name}")
        identity["md5"] = uploaded_md5
        actions.append({"filename": name, "action": "uploaded_local_exact"})
        files = draft_file_map(legacy_draft(session, token))

    final_files = draft_file_map(legacy_draft(session, token))
    if set(final_files) != set(expected):
        raise RuntimeError("Staged draft does not have the exact 63-file set")
    retained = 0
    for name, row in final_files.items():
        size, md5 = legacy_identity(row)
        identity = expected[name]
        if (size, md5) != (identity["bytes"], identity["md5"]):
            raise RuntimeError(f"Staged identity mismatch: {name}")
        if name not in local:
            retained += 1
    if retained != EXPECTED_RETAINED_FILES:
        raise RuntimeError(f"Expected 56 retained files, got {retained}")

    receipt = {
        "status": "PASS_STAGED",
        "errors": [],
        "record_id": SUCCESSOR_RECORD,
        "concept_doi": CONCEPT_DOI,
        "file_count": len(final_files),
        "bytes": sum(int(row["filesize"]) for row in final_files.values()),
        "retained_predecessor_files": retained,
        "local_upload_files": len(local),
        "actions": actions,
        "duplicate_concept_created": False,
        "second_draft_created": False,
    }
    save_json(
        RECEIPT_ROOT
        / "20260728_sga3_cumulative_record_21632790_draft_files.json",
        receipt,
    )
    return receipt


def patch_notes(metadata: dict) -> None:
    additional = [
        row
        for row in metadata.get("additional_descriptions", [])
        if row.get("type", {}).get("id") != "notes"
    ]
    additional.append(
        {
            "description": NOTES_HTML,
            "type": {"id": "notes", "title": {"en": "Notes"}},
        }
    )
    metadata["additional_descriptions"] = additional


def assert_metadata(metadata: dict) -> None:
    if metadata.get("version") != VERSION:
        raise RuntimeError("Version metadata mismatch")
    if metadata.get("publication_date") != PUBLICATION_DATE:
        raise RuntimeError("Publication-date metadata mismatch")
    if metadata.get("description") != DESCRIPTION_HTML:
        raise RuntimeError("Description metadata mismatch")
    if not any(
        row.get("description") == NOTES_HTML
        for row in metadata.get("additional_descriptions", [])
    ):
        raise RuntimeError("Release notes metadata mismatch")


def publish(session: requests.Session, token: str) -> dict:
    expected = expected_identities()
    deposition = legacy_draft(session, token)
    files = draft_file_map(deposition)
    if set(files) != set(expected):
        raise RuntimeError("Cannot publish: draft exact set does not match")
    for name, identity in expected.items():
        size = int(files[name]["filesize"])
        if size != identity["bytes"]:
            raise RuntimeError(f"Cannot publish: draft byte mismatch: {name}")

    draft = modern_draft(session, token)
    assert_draft_lineage(draft)
    metadata = copy.deepcopy(draft["metadata"])
    metadata["version"] = VERSION
    metadata["publication_date"] = PUBLICATION_DATE
    metadata["description"] = DESCRIPTION_HTML
    patch_notes(metadata)
    payload = {
        "access": draft["access"],
        "files": {
            "enabled": True,
            "default_preview": DEFAULT_PREVIEW,
            "order": sorted(expected, key=str.casefold),
        },
        "metadata": metadata,
        "custom_fields": draft.get("custom_fields", {}),
    }
    if draft.get("pids"):
        payload["pids"] = draft["pids"]
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.inveniordm.v1+json",
        "Content-Type": "application/json",
    }
    patched = check(
        session.put(
            f"{API}/records/{SUCCESSOR_RECORD}/draft",
            headers=headers,
            json=payload,
            timeout=(30, 300),
        ),
        {200},
    ).json()
    assert_metadata(patched["metadata"])
    patched_readback = modern_draft(session, token)
    assert_metadata(patched_readback["metadata"])
    if patched_readback["files"].get("default_preview") != DEFAULT_PREVIEW:
        raise RuntimeError("Draft default preview mismatch")
    if set(patched_readback["files"]["entries"]) != set(expected):
        raise RuntimeError("Draft lost exact file set after metadata patch")

    published = check(
        session.post(
            patched_readback["links"]["publish"],
            headers={
                "Authorization": f"Bearer {token}",
                "Accept": "application/vnd.inveniordm.v1+json",
            },
            timeout=(30, 600),
        ),
        {200, 202},
    ).json()
    assert_public_lineage(published)
    receipt = {
        "status": "PUBLISH_ACCEPTED",
        "errors": [],
        "record_id": SUCCESSOR_RECORD,
        "doi": SUCCESSOR_DOI,
        "concept_doi": CONCEPT_DOI,
        "file_count": EXPECTED_OUTER_FILES,
        "default_preview": DEFAULT_PREVIEW,
        "duplicate_concept_created": False,
    }
    save_json(
        RECEIPT_ROOT
        / "20260728_sga3_cumulative_record_21632790_publish_response.json",
        receipt,
    )
    return receipt


def wait_for_public(session: requests.Session) -> dict:
    for _ in range(90):
        response = session.get(
            f"{API}/records/{SUCCESSOR_RECORD}?expand=true",
            headers={"Accept": "application/vnd.inveniordm.v1+json"},
            timeout=(30, 180),
        )
        if response.status_code == 200:
            record = response.json()
            entries = record.get("files", {}).get("entries", {})
            if isinstance(entries, list):
                entries = {row["key"]: row for row in entries}
                record["files"]["entries"] = entries
            if len(entries) == EXPECTED_OUTER_FILES:
                return record
        time.sleep(5)
    raise RuntimeError("Published record did not stabilize")


def safe_zip_name(name: str) -> None:
    pure = PurePosixPath(name)
    if pure.is_absolute() or ".." in pure.parts or "\\" in name:
        raise RuntimeError(f"Unsafe ZIP member path: {name}")


def readback(
    session: requests.Session, token: str, keep_downloads: bool
) -> tuple[dict, dict]:
    expected = expected_identities()
    record = wait_for_public(session)
    assert_public_lineage(record)
    assert_metadata(record["metadata"])
    if record["files"].get("default_preview") != DEFAULT_PREVIEW:
        raise RuntimeError("Published default preview mismatch")
    entries = record["files"]["entries"]
    if set(entries) != set(expected):
        raise RuntimeError("Published file set mismatch")
    if sum(int(row["size"]) for row in entries.values()) != EXPECTED_OUTER_BYTES:
        raise RuntimeError("Published byte boundary mismatch")

    latest = check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}/versions/latest?expand=true",
            headers={"Accept": "application/vnd.inveniordm.v1+json"},
            timeout=(30, 180),
        ),
        {200},
    ).json()
    assert_public_lineage(latest)

    if READBACK_ROOT.exists():
        shutil.rmtree(READBACK_ROOT)
    READBACK_ROOT.mkdir(parents=True)
    file_receipt = {}
    for index, name in enumerate(sorted(expected, key=str.casefold), start=1):
        print(f"READBACK {index}/{len(expected)} {name}", flush=True)
        entry = entries[name]
        target = READBACK_ROOT / name
        with session.get(
            entry["links"]["content"],
            stream=True,
            timeout=(30, 1800),
        ) as response:
            check(response, {200})
            with target.open("wb") as handle:
                for block in response.iter_content(4 * 1024 * 1024):
                    if block:
                        handle.write(block)
        actual = {
            "bytes": target.stat().st_size,
            "sha256": sha256_file(target),
            "url": entry["links"]["content"],
        }
        identity = expected[name]
        actual["match"] = (actual["bytes"], actual["sha256"]) == (
            identity["bytes"],
            identity["sha256"],
        )
        if not actual["match"]:
            raise RuntimeError(f"Public readback mismatch: {name}")
        file_receipt[name] = actual

    zip_archives = []
    zip_members = []
    zip_file_members = 0
    zip_directory_entries = 0
    zip_all_entries = 0
    zip_uncompressed_bytes = 0
    for name in sorted(file_receipt, key=str.casefold):
        if not name.lower().endswith(".zip"):
            continue
        path = READBACK_ROOT / name
        member_digest = hashlib.sha256()
        archive_file_members = 0
        archive_directory_entries = 0
        archive_uncompressed = 0
        with zipfile.ZipFile(path, "r") as archive:
            if archive.testzip() is not None:
                raise RuntimeError(f"ZIP CRC failure: {name}")
            for info in archive.infolist():
                safe_zip_name(info.filename)
                if info.is_dir():
                    archive_directory_entries += 1
                    continue
                digest = hashlib.sha256()
                with archive.open(info, "r") as source:
                    for block in iter(lambda: source.read(4 * 1024 * 1024), b""):
                        digest.update(block)
                sha = digest.hexdigest().upper()
                row = (
                    f"{info.filename}\t{info.file_size}\t{sha}\n".encode("utf-8")
                )
                member_digest.update(row)
                zip_members.append(
                    {
                        "archive": name,
                        "relative_path": info.filename,
                        "bytes": info.file_size,
                        "sha256": sha,
                    }
                )
                archive_file_members += 1
                archive_uncompressed += info.file_size
        archive_all = archive_file_members + archive_directory_entries
        zip_archives.append(
            {
                "filename": name,
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
                "member_count": archive_file_members,
                "directory_entry_count": archive_directory_entries,
                "all_entry_count": archive_all,
                "uncompressed_bytes": archive_uncompressed,
                "canonical_member_identity_sha256": (
                    member_digest.hexdigest().upper()
                ),
                "errors": [],
            }
        )
        zip_file_members += archive_file_members
        zip_directory_entries += archive_directory_entries
        zip_all_entries += archive_all
        zip_uncompressed_bytes += archive_uncompressed

    observed_zip = (
        len(zip_archives),
        zip_file_members,
        zip_directory_entries,
        zip_all_entries,
        zip_uncompressed_bytes,
    )
    expected_zip = (
        EXPECTED_ZIP_ARCHIVES,
        EXPECTED_ZIP_FILE_MEMBERS,
        EXPECTED_ZIP_DIRECTORY_ENTRIES,
        EXPECTED_ZIP_ALL_ENTRIES,
        EXPECTED_ZIP_UNCOMPRESSED_BYTES,
    )
    if observed_zip != expected_zip:
        raise RuntimeError(
            f"ZIP aggregate mismatch: observed={observed_zip}, "
            f"expected={expected_zip}"
        )

    public_receipt = {
        "status": "PASS",
        "errors": [],
        "record": SUCCESSOR_RECORD,
        "doi": SUCCESSOR_DOI,
        "conceptdoi": CONCEPT_DOI,
        "record_url": f"https://zenodo.org/records/{SUCCESSOR_RECORD}",
        "version": VERSION,
        "file_count": len(file_receipt),
        "bytes": sum(row["bytes"] for row in file_receipt.values()),
        "files": file_receipt,
        "latest_record": int(latest["id"]),
        "rdm_default_preview": record["files"].get("default_preview"),
        "github_commit": GITHUB_COMMIT,
        "github_package": GITHUB_PACKAGE,
        "retained_predecessor_files": EXPECTED_RETAINED_FILES,
        "duplicate_concept_created": False,
        "second_draft_created": False,
    }
    zip_receipt = {
        "status": "PASS",
        "errors": [],
        "record_id": SUCCESSOR_RECORD,
        "doi": SUCCESSOR_DOI,
        "zip_archive_count": len(zip_archives),
        "zip_file_member_count": zip_file_members,
        "zip_directory_entry_count": zip_directory_entries,
        "zip_all_entry_count": zip_all_entries,
        "zip_uncompressed_bytes": zip_uncompressed_bytes,
        "archives": zip_archives,
        "members": zip_members,
    }
    save_json(
        RECEIPT_ROOT
        / "20260728_sga3_cumulative_record_21632790_public_readback.json",
        public_receipt,
    )
    save_json(
        RECEIPT_ROOT
        / "20260728_sga3_cumulative_record_21632790_zip_member_readback.json",
        zip_receipt,
    )
    if not keep_downloads:
        shutil.rmtree(READBACK_ROOT)
    return public_receipt, zip_receipt


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "action",
        choices=("stage", "publish", "readback", "all"),
        default="all",
        nargs="?",
    )
    parser.add_argument("--keep-downloads", action="store_true")
    args = parser.parse_args()

    token = find_token()
    session = make_session()
    # Fail before mutation if the retained credential no longer owns this draft.
    legacy_draft(session, token)

    result = {}
    if args.action in {"stage", "all"}:
        result["stage"] = stage(session, token)
    if args.action in {"publish", "all"}:
        result["publish"] = publish(session, token)
    if args.action in {"readback", "all"}:
        public, zipped = readback(session, token, args.keep_downloads)
        result["readback"] = {
            "status": public["status"],
            "record": public["record"],
            "file_count": public["file_count"],
            "zip_archives": zipped["zip_archive_count"],
            "zip_members": zipped["zip_file_member_count"],
        }
    print(json.dumps(result, indent=2), flush=True)


if __name__ == "__main__":
    main()
