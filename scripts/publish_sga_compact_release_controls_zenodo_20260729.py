#!/usr/bin/env python3
"""Pack loose SGA release controls into one same-concept Zenodo ZIP."""

from __future__ import annotations

import copy
import csv
import hashlib
import importlib.util
import io
import json
import os
import sys
import urllib.request
import zipfile
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
BASE_PATH = (
    SCRIPT_DIR
    / "publish_sga_canonical_reader_surface_r20_zenodo_20260729.py"
)
SPEC = importlib.util.spec_from_file_location(
    "sga_canonical_reader_surface_r20",
    BASE_PATH,
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load the canonical SGA publication workflow")
previous = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = previous
SPEC.loader.exec_module(previous)
base = previous.base


PREDECESSOR_RECORD = 21683140
PREDECESSOR_DOI = "10.5281/zenodo.21683140"
CONCEPT_DOI = "10.5281/zenodo.20410947"
PUBLICATION_DATE = "2026-07-29"
VERSION = "2026-07-29 compact SGA1-6 reader surface"
TITLE = previous.TITLE
DESCRIPTION_HTML = previous.DESCRIPTION_HTML
DEFAULT_PREVIEW = previous.DEFAULT_PREVIEW

GITHUB_COMMIT = "285d6f0c153ce672685e372bbfa88b39d47fbfde"
GITHUB_PACKAGE = (
    "sources/sga/sga-canonical-release-controls-compact-20260729"
)
PACKAGE_ROOT = SCRIPT_DIR.parent / GITHUB_PACKAGE

README_NAME = previous.README_NAME
MANIFEST_NAME = previous.MANIFEST_NAME
VALIDATION_NAME = previous.VALIDATION_NAME
REPLACED_NAMES = {README_NAME, MANIFEST_NAME, VALIDATION_NAME}

ZIP_NAME = "10z_SGA_Current_Release_Controls_20260729.zip"
ZIP_EXPECTED = (
    6_424,
    "2F0D4D8247BEEB37A1A9C993F5A8AD18638EC0CCDB2B6EE0DDFD418C67256A39",
)
OUTER_EXPECTED = {
    ZIP_NAME: ZIP_EXPECTED,
    "PACKAGE_VALIDATION.json": (
        1_006,
        "8F5D46FEF0EA76161CAB65C18837CDE4E0973F658217014167EC1366C0543BD2",
    ),
    "README.md": (
        742,
        "234B926F19441046BA8C19F0F84FA607A12D5F46E54B4E6AD8074CB92ABA017E",
    ),
    "SHA256SUMS.csv": (
        316,
        "0EA6542B33961B7EF00BC1EA9D63C55398C8C22A646FFB8D38D537E68C45E686",
    ),
}
PACKED_MEMBER_EXPECTED = {
    README_NAME: (
        1_162,
        "F29777968A96534331357D67B4ACEF7F1B1A8BC24F1F306D650A9B2FA9C6E5CD",
    ),
    MANIFEST_NAME: (
        14_208,
        "E552C0D7A05F2E4FADFEAF198772854220464509CEC685521BFBCC2167178C38",
    ),
    VALIDATION_NAME: (
        1_952,
        "33283DBA919B606A0C62EB556110000457B694DA2A881ECCD2F7D891867D0CE7",
    ),
    "PACKED_CONTROL_SHA256.csv": (
        453,
        "7B187FEB5E1E2CF0999B4267E217AC2C4FBCB23301F01D553DB71FB27C37308D",
    ),
}

EXPECTED_PREDECESSOR_FILES = 68
EXPECTED_FINAL_FILES = 66
EXPECTED_RETAINED_PREDECESSOR_FILES = 65
EXPECTED_UNRELATED_RETAINED_FILES = 65
EXPECTED_MANIFEST_ROWS = 66
EXPECTED_ZIP_ARCHIVES = 50
EXPECTED_ZIP_FILE_MEMBERS = 4_254
EXPECTED_ZIP_DIRECTORY_ENTRIES = 6
EXPECTED_ZIP_ALL_ENTRIES = 4_260
EXPECTED_ZIP_UNCOMPRESSED_BYTES = 441_165_964
EXPECTED_GITHUB_READBACK_FILES = 4

REPO_ROOT = SCRIPT_DIR.parent
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
PREDECESSOR_RECEIPT = (
    RECEIPT_ROOT
    / "20260728_sga3_cumulative_with_x_record_21683140_public_readback.json"
)
TEMP_ROOT = Path(os.environ["LOCALAPPDATA"]) / "Temp"
CONTROLS_ROOT = TEMP_ROOT / "sga_compact_release_controls"
READBACK_ROOT = TEMP_ROOT / "sga_compact_release_controls_readback"
DRAFT_STATE = (
    RECEIPT_ROOT
    / "20260729_sga_compact_release_controls_zenodo_draft_state.json"
)

PRIMARY_LOCAL_PATHS = {ZIP_NAME: PACKAGE_ROOT / ZIP_NAME}
NEW_MANIFEST_ROWS: dict[str, dict] = {}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def verify_github_readback() -> None:
    local_files = sorted(
        (path for path in PACKAGE_ROOT.iterdir() if path.is_file()),
        key=lambda path: path.name.casefold(),
    )
    if len(local_files) != EXPECTED_GITHUB_READBACK_FILES:
        raise RuntimeError("Compact-control GitHub boundary mismatch")
    raw_root = (
        "https://raw.githubusercontent.com/"
        f"KokunoYumeto/modern-latex-manuscripts/{GITHUB_COMMIT}/"
        f"{GITHUB_PACKAGE}/"
    )
    for path in local_files:
        expected = OUTER_EXPECTED.get(path.name)
        actual = (path.stat().st_size, base.sha256_file(path))
        if expected is None or actual != expected:
            raise RuntimeError(f"Local compact-control mismatch: {path.name}")
        request = urllib.request.Request(
            raw_root + path.name,
            headers={"User-Agent": "modern-latex-manuscripts-readback"},
        )
        with urllib.request.urlopen(request, timeout=300) as response:
            data = response.read()
        if (len(data), sha256_bytes(data)) != expected:
            raise RuntimeError(f"GitHub compact-control mismatch: {path.name}")


def verify_primary_local_files() -> dict[str, dict]:
    verify_github_readback()

    outer_manifest = PACKAGE_ROOT / "SHA256SUMS.csv"
    rows = list(
        csv.DictReader(
            io.StringIO(
                outer_manifest.read_text(encoding="utf-8-sig"),
                newline="",
            )
        )
    )
    if len(rows) != 3:
        raise RuntimeError("Compact-control outer manifest row mismatch")
    for row in rows:
        path = PACKAGE_ROOT / row["relative_path"]
        wanted = (int(row["bytes"]), row["sha256"].upper())
        if (path.stat().st_size, base.sha256_file(path)) != wanted:
            raise RuntimeError(
                f"Compact-control outer manifest mismatch: {path.name}"
            )

    validation = json.loads(
        (PACKAGE_ROOT / "PACKAGE_VALIDATION.json").read_text(
            encoding="utf-8"
        )
    )
    if (
        validation.get("status") != "PASS"
        or validation.get("errors") != []
        or validation.get("source_record") != PREDECESSOR_RECORD
        or validation.get("expected_successor", {}).get("final_files")
        != EXPECTED_FINAL_FILES
    ):
        raise RuntimeError("Compact-control package validation mismatch")

    zip_path = PACKAGE_ROOT / ZIP_NAME
    seen: dict[str, tuple[int, str]] = {}
    with zipfile.ZipFile(zip_path, "r") as archive:
        if archive.testzip() is not None:
            raise RuntimeError("Compact-control ZIP failed CRC validation")
        for info in archive.infolist():
            base.safe_zip_name(info.filename)
            if info.is_dir():
                raise RuntimeError("Compact-control ZIP has a directory entry")
            data = archive.read(info)
            seen[info.filename] = (len(data), sha256_bytes(data))
        packed_rows = list(
            csv.DictReader(
                io.StringIO(
                    archive.read("PACKED_CONTROL_SHA256.csv").decode(
                        "utf-8-sig"
                    ),
                    newline="",
                )
            )
        )
    if seen != PACKED_MEMBER_EXPECTED:
        raise RuntimeError("Compact-control ZIP member set mismatch")
    if len(packed_rows) != 3:
        raise RuntimeError("Packed-control manifest row mismatch")
    for row in packed_rows:
        name = row["relative_path"]
        if name not in REPLACED_NAMES:
            raise RuntimeError(f"Unexpected packed control: {name}")
        if (
            int(row["bytes"]),
            row["sha256"].upper(),
            int(row["source_record"]),
        ) != (
            *PACKED_MEMBER_EXPECTED[name],
            PREDECESSOR_RECORD,
        ):
            raise RuntimeError(f"Packed-control identity mismatch: {name}")

    predecessor = json.loads(
        PREDECESSOR_RECEIPT.read_text(encoding="utf-8-sig")
    )
    for name in REPLACED_NAMES:
        row = predecessor["files"][name]
        if (
            int(row["bytes"]),
            row["sha256"].upper(),
            bool(row["match"]),
        ) != (*PACKED_MEMBER_EXPECTED[name], True):
            raise RuntimeError(f"Packed predecessor mismatch: {name}")

    return {
        ZIP_NAME: {
            "path": zip_path,
            "bytes": zip_path.stat().st_size,
            "sha256": base.sha256_file(zip_path),
            "md5": base.md5_file(zip_path),
        }
    }


def fetch_predecessor_manifest(
    session,
    predecessor: dict,
    receipt: dict,
) -> list[dict[str, str]]:
    entry = base.entries_map(predecessor)[MANIFEST_NAME]
    response = base.check(
        session.get(entry["links"]["content"], timeout=(30, 180)),
        {200},
    )
    content = response.content
    wanted = receipt["files"][MANIFEST_NAME]
    if (len(content), sha256_bytes(content)) != (
        int(wanted["bytes"]),
        wanted["sha256"].upper(),
    ):
        raise RuntimeError("Predecessor release manifest mismatch")
    rows = list(
        csv.DictReader(
            io.StringIO(content.decode("utf-8-sig"), newline="")
        )
    )
    if len(rows) != EXPECTED_MANIFEST_ROWS:
        raise RuntimeError("Predecessor release manifest boundary mismatch")
    return rows


def create_or_resume_draft(session, token: str, predecessor: dict) -> int:
    auth = {"Authorization": f"Bearer {token}"}
    vendor = {
        **auth,
        "Accept": "application/vnd.inveniordm.v1+json",
    }
    existing = session.get(
        f"{base.API}/records/{PREDECESSOR_RECORD}/draft",
        headers=vendor,
        timeout=(30, 180),
    )
    if existing.status_code == 200:
        if not DRAFT_STATE.is_file():
            raise RuntimeError("An untracked successor draft already exists")
        state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
        draft = existing.json()
        draft_id = int(draft["id"])
        if (
            draft_id != int(state["draft_id"])
            or base.concept_doi(draft) != CONCEPT_DOI
            or int(state["predecessor_record"]) != PREDECESSOR_RECORD
        ):
            raise RuntimeError("Existing successor is not the tracked draft")
        return draft_id
    base.check(existing, {404})
    if DRAFT_STATE.is_file():
        state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
        if state.get("published"):
            raise RuntimeError("Tracked successor is already published")
        raise RuntimeError("Tracked state exists but its draft is absent")

    legacy = base.check(
        session.get(
            f"{base.API}/deposit/depositions/{PREDECESSOR_RECORD}",
            headers=auth,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    created = base.check(
        session.post(
            legacy["links"]["newversion"],
            headers=auth,
            timeout=(30, 300),
        ),
        {201},
    ).json()
    deposit = base.check(
        session.get(
            created["links"]["latest_draft"],
            headers=auth,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    draft_id = int(deposit["id"])
    if set(base.legacy_file_map(deposit)) != set(
        base.entries_map(predecessor)
    ):
        raise RuntimeError("Successor draft did not inherit the predecessor")
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


def generate_controls(
    draft_id: int,
    predecessor_rows: list[dict[str, str]],
    predecessor_identities: dict[str, dict],
    primary_local: dict[str, dict],
) -> dict[str, dict]:
    if draft_id <= PREDECESSOR_RECORD:
        raise RuntimeError("Reserved successor record is not newer")
    if len(predecessor_rows) != EXPECTED_MANIFEST_ROWS:
        raise RuntimeError("Predecessor control rows changed")
    if len(predecessor_identities) != EXPECTED_PREDECESSOR_FILES:
        raise RuntimeError("Predecessor identity boundary changed")
    if set(primary_local) != {ZIP_NAME}:
        raise RuntimeError("Compact-control local file set changed")
    return primary_local


def assert_metadata(metadata: dict) -> None:
    if metadata.get("title") != TITLE:
        raise RuntimeError("Title metadata mismatch")
    if metadata.get("version") != VERSION:
        raise RuntimeError("Version metadata mismatch")
    if metadata.get("publication_date") != PUBLICATION_DATE:
        raise RuntimeError("Publication-date metadata mismatch")
    if metadata.get("description") != DESCRIPTION_HTML:
        raise RuntimeError("Description metadata mismatch")
    if metadata.get("contributors"):
        raise RuntimeError("Reader-facing contributor badges are forbidden")
    if any(
        row.get("type", {}).get("id") == "notes"
        for row in (metadata.get("additional_descriptions") or [])
    ):
        raise RuntimeError("Reader-facing release notes are forbidden")


def publish_draft(
    session,
    token: str,
    draft_id: int,
    expected: dict[str, dict],
) -> dict:
    draft = base.modern_draft(session, token, draft_id)
    if set(draft["files"]["entries"]) != set(expected):
        raise RuntimeError("Cannot publish: modern draft set mismatch")

    metadata = copy.deepcopy(draft["metadata"])
    metadata["title"] = TITLE
    metadata["version"] = VERSION
    metadata["publication_date"] = PUBLICATION_DATE
    metadata["description"] = DESCRIPTION_HTML
    metadata["contributors"] = []
    metadata["additional_descriptions"] = [
        row
        for row in (metadata.get("additional_descriptions") or [])
        if row.get("type", {}).get("id") != "notes"
    ]
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
    patched = base.check(
        session.put(
            f"{base.API}/records/{draft_id}/draft",
            headers=headers,
            json=payload,
            timeout=(30, 300),
        ),
        {200},
    ).json()
    assert_metadata(patched["metadata"])
    reread = base.modern_draft(session, token, draft_id)
    assert_metadata(reread["metadata"])
    if reread["files"].get("default_preview") != DEFAULT_PREVIEW:
        raise RuntimeError("Draft default preview mismatch")
    if set(reread["files"]["entries"]) != set(expected):
        raise RuntimeError("Draft lost exact file set after metadata patch")

    published = base.check(
        session.post(
            reread["links"]["publish"],
            headers={
                "Authorization": f"Bearer {token}",
                "Accept": "application/vnd.inveniordm.v1+json",
            },
            timeout=(30, 600),
        ),
        {200, 202},
    ).json()
    if (
        int(published["id"]) != draft_id
        or base.concept_doi(published) != CONCEPT_DOI
    ):
        raise RuntimeError("Published response escaped the existing concept")
    doi = base.version_doi(published)
    state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
    state.update({"published": True, "doi": doi})
    base.save_json(DRAFT_STATE, state)
    receipt = {
        "status": "PUBLISH_ACCEPTED",
        "errors": [],
        "record_id": draft_id,
        "doi": doi,
        "concept_doi": CONCEPT_DOI,
        "file_count": EXPECTED_FINAL_FILES,
        "default_preview": DEFAULT_PREVIEW,
        "contributors": [],
        "notes_present": False,
        "duplicate_concept_created": False,
        "second_draft_created": False,
    }
    base.save_json(
        RECEIPT_ROOT
        / (
            "20260729_sga_compact_release_controls_record_"
            f"{draft_id}_publish_response.json"
        ),
        receipt,
    )
    return receipt


for name, value in {
    "CONCEPT_DOI": CONCEPT_DOI,
    "PREDECESSOR_RECORD": PREDECESSOR_RECORD,
    "PREDECESSOR_DOI": PREDECESSOR_DOI,
    "PUBLICATION_DATE": PUBLICATION_DATE,
    "VERSION": VERSION,
    "GITHUB_COMMIT": GITHUB_COMMIT,
    "GITHUB_PACKAGE": GITHUB_PACKAGE,
    "README_NAME": README_NAME,
    "MANIFEST_NAME": MANIFEST_NAME,
    "VALIDATION_NAME": VALIDATION_NAME,
    "REPLACED_NAMES": REPLACED_NAMES,
    "EXPECTED_PREDECESSOR_FILES": EXPECTED_PREDECESSOR_FILES,
    "EXPECTED_FINAL_FILES": EXPECTED_FINAL_FILES,
    "EXPECTED_RETAINED_PREDECESSOR_FILES": (
        EXPECTED_RETAINED_PREDECESSOR_FILES
    ),
    "EXPECTED_UNRELATED_RETAINED_FILES": EXPECTED_UNRELATED_RETAINED_FILES,
    "EXPECTED_MANIFEST_ROWS": EXPECTED_MANIFEST_ROWS,
    "EXPECTED_ZIP_ARCHIVES": EXPECTED_ZIP_ARCHIVES,
    "EXPECTED_ZIP_FILE_MEMBERS": EXPECTED_ZIP_FILE_MEMBERS,
    "EXPECTED_ZIP_DIRECTORY_ENTRIES": EXPECTED_ZIP_DIRECTORY_ENTRIES,
    "EXPECTED_ZIP_ALL_ENTRIES": EXPECTED_ZIP_ALL_ENTRIES,
    "EXPECTED_ZIP_UNCOMPRESSED_BYTES": EXPECTED_ZIP_UNCOMPRESSED_BYTES,
    "EXPECTED_GITHUB_READBACK_FILES": EXPECTED_GITHUB_READBACK_FILES,
    "RECEIPT_ROOT": RECEIPT_ROOT,
    "PREDECESSOR_RECEIPT": PREDECESSOR_RECEIPT,
    "CONTROLS_ROOT": CONTROLS_ROOT,
    "READBACK_ROOT": READBACK_ROOT,
    "DRAFT_STATE": DRAFT_STATE,
    "PRIMARY_LOCAL_PATHS": PRIMARY_LOCAL_PATHS,
    "NEW_MANIFEST_ROWS": NEW_MANIFEST_ROWS,
    "DESCRIPTION_HTML": DESCRIPTION_HTML,
    "DEFAULT_PREVIEW": DEFAULT_PREVIEW,
}.items():
    setattr(base, name, value)

base.verify_primary_local_files = verify_primary_local_files
base.fetch_predecessor_manifest = fetch_predecessor_manifest
base.create_or_resume_draft = create_or_resume_draft
base.generate_controls = generate_controls
base.assert_metadata = assert_metadata
base.publish_draft = publish_draft


if __name__ == "__main__":
    base.main()
