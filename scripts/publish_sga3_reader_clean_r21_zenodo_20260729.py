#!/usr/bin/env python3
"""Publish the SGA3 R21 reader-clean successor on the existing SGA concept."""

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
BASE_PATH = SCRIPT_DIR / "publish_sga_compact_release_controls_zenodo_20260729.py"
SPEC = importlib.util.spec_from_file_location(
    "sga_compact_release_controls_20260729",
    BASE_PATH,
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load the established SGA publication workflow")
previous = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = previous
SPEC.loader.exec_module(previous)
base = previous.base


PREDECESSOR_RECORD = 21686789
PREDECESSOR_DOI = "10.5281/zenodo.21686789"
CONCEPT_DOI = "10.5281/zenodo.20410947"
PUBLICATION_DATE = "2026-07-29"
VERSION = "2026-07-29 compact SGA1-6 reader surface (SGA3 R21)"
TITLE = previous.TITLE
DEFAULT_PREVIEW = previous.DEFAULT_PREVIEW

DESCRIPTION_HTML = "\n".join(
    (
        "<p>English readers for SGA 1 through SGA 6 are listed first in "
        "numerical order. Available French texts and editable TeX masters "
        "follow; supplementary source and historical files are grouped in "
        "ZIP archives.</p>",
        "<p>The SGA3 reader has 1,459 A4 pages and contains the Editorial "
        "Notice, Introduction, Exposes I-XXVI, the Tome-I index, the Tome-III "
        "mathematical guide, and the terminal index. Exposes V and VI use "
        "native TeX diagrams.</p>",
        "<p>The direct PDFs contain the mathematical text, diagrams, "
        "references, and original historical editorial apparatus. Project "
        "production, source-reading, and workflow records are kept outside "
        "the reader pages and grouped with the supporting archives.</p>",
        "<p>These editions do not transfer rights in the underlying French "
        "works. Historical Zenodo versions remain immutable.</p>",
    )
)

GITHUB_COMMIT = "efc17fed71b0869fa60f11afd866084f4ab5a9d8"
GITHUB_PACKAGE = (
    "sources/sga/sga3-english-reader-clean-r21-no-project-notes-20260729"
)
GITHUB_CONTROLS_PACKAGE = (
    "sources/sga/sga-reader-clean-r21-release-controls-20260729"
)
REPO_ROOT = SCRIPT_DIR.parent
PACKAGE_ROOT = REPO_ROOT / GITHUB_PACKAGE
CONTROLS_PACKAGE_ROOT = REPO_ROOT / GITHUB_CONTROLS_PACKAGE

SGA3_PDF = "00c_SGA3_English_Reader.pdf"
OLD_SGA3_ZIP = "10c_SGA3_English_Source_and_History_R20_20260729.zip"
SGA3_ZIP = "10c_SGA3_English_Source_and_History_R21_20260729.zip"
CONTROLS_ZIP = "10z_SGA_Current_Release_Controls_20260729.zip"

README_NAME = previous.README_NAME
MANIFEST_NAME = previous.MANIFEST_NAME
VALIDATION_NAME = previous.VALIDATION_NAME
REPLACED_NAMES = {SGA3_PDF, OLD_SGA3_ZIP, CONTROLS_ZIP}

PRIMARY_LOCAL_PATHS = {
    SGA3_PDF: PACKAGE_ROOT / SGA3_PDF,
    SGA3_ZIP: PACKAGE_ROOT / SGA3_ZIP,
    CONTROLS_ZIP: CONTROLS_PACKAGE_ROOT / CONTROLS_ZIP,
}
PRIMARY_EXPECTED = {
    SGA3_PDF: (
        6_808_676,
        "62BB18E8646A57147F83D20DE6DEEF18B1E421D9EE821E16DDF10A6591128744",
    ),
    SGA3_ZIP: (
        9_102_765,
        "8DCF0B135F06DE88EF91929508D4B77F5F0A8377BB98CE918911B272940EC18A",
    ),
    CONTROLS_ZIP: (
        6_010,
        "ADD778480B5052053AC7C0180C466AD0055C4314899E559D2E205CAF3D2BA2C2",
    ),
}

R21_PACKAGE_MANIFEST = (
    1_094,
    "8E896BAD6E099F6DD9E5B94C8F5458E2D73EBCEA3CFDB6A45B65851F80233925",
)
R21_PACKAGE_VALIDATION = (
    3_003,
    "DEA8F56AC8DB91D44D9589110826758CFA84FB019B88E9F0035D1CC95C72CB22",
)
CONTROLS_PACKAGE_MANIFEST = (
    310,
    "AC9FEF6EC62F5630630C611220E79FD1E07A8281580474770386BE6AEEEA171C",
)
CONTROLS_PACKAGE_VALIDATION = (
    457,
    "0E7BE0378C5AD5101630B18A999648ACA2E7BEA0884AD69F080ED5516C4C959A",
)

R21_SOURCE_MEMBERS = 902
R21_SOURCE_MANIFEST_ROWS = 901
R21_SOURCE_UNCOMPRESSED_BYTES = 12_551_472
R21_SOURCE_MANIFEST_SHA256 = (
    "0F7EC0F6D41EF3868800A5ED6AF6FC674D900E1743197B5C2C705C0856A929A4"
)
CONTROL_MEMBER_EXPECTED = {
    README_NAME: (
        1_164,
        "426CAEDA30F56397958DF231C85DBAD1AC0ECFEE37BC893873A8C6FFA7BE6C2A",
    ),
    MANIFEST_NAME: (
        14_058,
        "1BB041D5B99FAEE4CA5A915FDB873D6317FA7A6E8F4E9BA4FA6F09DD26754F38",
    ),
    VALIDATION_NAME: (
        1_100,
        "54645F8354E4EFC087506F4EB8F95A0DE2F2C69CE780C58997F093B049198A37",
    ),
    "PACKED_CONTROL_SHA256.csv": (
        320,
        "E3D2B0776B87D856D4565EADC95F6D50C8450235A68BA1F2B7B501D73F41D49F",
    ),
}

EXPECTED_PREDECESSOR_FILES = 66
EXPECTED_FINAL_FILES = 66
EXPECTED_RETAINED_PREDECESSOR_FILES = 63
EXPECTED_UNRELATED_RETAINED_FILES = 63
EXPECTED_MANIFEST_ROWS = 65
EXPECTED_ZIP_ARCHIVES = 50
EXPECTED_ZIP_FILE_MEMBERS = 4_234
EXPECTED_ZIP_DIRECTORY_ENTRIES = 6
EXPECTED_ZIP_ALL_ENTRIES = 4_240
EXPECTED_ZIP_UNCOMPRESSED_BYTES = 441_061_146
EXPECTED_GITHUB_READBACK_FILES = 16

RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
PREDECESSOR_RECEIPT = (
    RECEIPT_ROOT
    / "20260728_sga3_cumulative_with_x_record_21686789_public_readback.json"
)
PREDECESSOR_ZIP_RECEIPT = (
    RECEIPT_ROOT
    / "20260728_sga3_cumulative_with_x_record_21686789_zip_member_readback.json"
)
TEMP_ROOT = Path(os.environ["LOCALAPPDATA"]) / "Temp"
CONTROLS_ROOT = TEMP_ROOT / "sga3_reader_clean_r21_zenodo_controls"
READBACK_ROOT = TEMP_ROOT / "sga3_reader_clean_r21_zenodo_readback"
DRAFT_STATE = (
    RECEIPT_ROOT
    / "20260729_sga3_reader_clean_r21_zenodo_draft_state.json"
)
NEW_MANIFEST_ROWS: dict[str, dict] = {}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def identity(path: Path) -> tuple[int, str]:
    return path.stat().st_size, base.sha256_file(path)


def read_csv_bytes(data: bytes) -> list[dict[str, str]]:
    return list(
        csv.DictReader(
            io.StringIO(data.decode("utf-8-sig"), newline="")
        )
    )


def verify_github_directory(
    package: str,
    root: Path,
    expected_files: int,
) -> None:
    files = sorted(
        (path for path in root.iterdir() if path.is_file()),
        key=lambda path: path.name.casefold(),
    )
    if len(files) != expected_files:
        raise RuntimeError(f"GitHub package boundary mismatch: {package}")
    raw_root = (
        "https://raw.githubusercontent.com/"
        f"KokunoYumeto/modern-latex-manuscripts/{GITHUB_COMMIT}/{package}/"
    )
    for path in files:
        request = urllib.request.Request(
            raw_root + path.name,
            headers={"User-Agent": "modern-latex-manuscripts-readback"},
        )
        with urllib.request.urlopen(request, timeout=600) as response:
            data = response.read()
        if (len(data), sha256_bytes(data)) != identity(path):
            raise RuntimeError(f"GitHub readback mismatch: {package}/{path.name}")


def verify_outer_manifest(
    root: Path,
    expected_identity: tuple[int, str],
    expected_rows: int,
) -> None:
    path = root / "SHA256SUMS.csv"
    if identity(path) != expected_identity:
        raise RuntimeError(f"Outer manifest identity mismatch: {root.name}")
    rows = read_csv_bytes(path.read_bytes())
    if len(rows) != expected_rows:
        raise RuntimeError(f"Outer manifest row mismatch: {root.name}")
    for row in rows:
        member = root / row["filename"]
        if identity(member) != (
            int(row["bytes"]),
            row["sha256"].upper(),
        ):
            raise RuntimeError(
                f"Outer manifest member mismatch: {root.name}/{member.name}"
            )


def verify_primary_local_files() -> dict[str, dict]:
    verify_github_directory(GITHUB_PACKAGE, PACKAGE_ROOT, 12)
    verify_github_directory(
        GITHUB_CONTROLS_PACKAGE,
        CONTROLS_PACKAGE_ROOT,
        4,
    )
    verify_outer_manifest(PACKAGE_ROOT, R21_PACKAGE_MANIFEST, 11)
    verify_outer_manifest(
        CONTROLS_PACKAGE_ROOT,
        CONTROLS_PACKAGE_MANIFEST,
        3,
    )

    if identity(PACKAGE_ROOT / "PACKAGE_VALIDATION.json") != (
        R21_PACKAGE_VALIDATION
    ):
        raise RuntimeError("R21 package validation identity mismatch")
    validation = json.loads(
        (PACKAGE_ROOT / "PACKAGE_VALIDATION.json").read_text(
            encoding="utf-8"
        )
    )
    reader = validation.get("reader", {})
    source = validation.get("source_archive", {})
    if (
        validation.get("status") != "PASS"
        or validation.get("errors") != []
        or reader.get("pages") != 1_459
        or reader.get("named_destinations") != 9_345
        or reader.get("internal_goto_actions") != 4_461
        or reader.get("invalid_actions") != 0
        or reader.get("uri_actions") != 0
        or reader.get("reader_process_term_hits") != []
        or validation.get("reader_apparatus_removals", {}).get("total") != 8
        or source.get("members") != R21_SOURCE_MEMBERS
        or source.get("manifest_rows") != R21_SOURCE_MANIFEST_ROWS
        or source.get("errors") != []
    ):
        raise RuntimeError("R21 package validation content mismatch")

    if identity(CONTROLS_PACKAGE_ROOT / "PACKAGE_VALIDATION.json") != (
        CONTROLS_PACKAGE_VALIDATION
    ):
        raise RuntimeError("R21 controls validation identity mismatch")
    control_validation = json.loads(
        (CONTROLS_PACKAGE_ROOT / "PACKAGE_VALIDATION.json").read_text(
            encoding="utf-8"
        )
    )
    if (
        control_validation.get("status") != "PASS"
        or control_validation.get("errors") != []
        or control_validation.get("source_record") != PREDECESSOR_RECORD
        or control_validation.get("prospective_zenodo_files")
        != EXPECTED_FINAL_FILES
        or control_validation.get("manifest_rows") != EXPECTED_MANIFEST_ROWS
    ):
        raise RuntimeError("R21 controls package validation mismatch")

    source_zip = PACKAGE_ROOT / SGA3_ZIP
    with zipfile.ZipFile(source_zip, "r") as archive:
        if archive.testzip() is not None:
            raise RuntimeError("R21 source ZIP failed CRC validation")
        infos = archive.infolist()
        if any(info.is_dir() for info in infos):
            raise RuntimeError("R21 source ZIP has directory entries")
        if (
            len(infos),
            sum(info.file_size for info in infos),
        ) != (
            R21_SOURCE_MEMBERS,
            R21_SOURCE_UNCOMPRESSED_BYTES,
        ):
            raise RuntimeError("R21 source ZIP boundary mismatch")
        rows = read_csv_bytes(archive.read("SOURCE_BUNDLE_SHA256.csv"))
        if len(rows) != R21_SOURCE_MANIFEST_ROWS:
            raise RuntimeError("R21 source ZIP manifest row mismatch")
        if (
            sha256_bytes(archive.read("SOURCE_BUNDLE_SHA256.csv"))
            != R21_SOURCE_MANIFEST_SHA256
        ):
            raise RuntimeError("R21 source ZIP manifest identity mismatch")
        for row in rows:
            data = archive.read(row["relative_path"])
            if (len(data), sha256_bytes(data)) != (
                int(row["bytes"]),
                row["sha256"].upper(),
            ):
                raise RuntimeError(
                    f"R21 source ZIP member mismatch: {row['relative_path']}"
                )

    controls_zip = CONTROLS_PACKAGE_ROOT / CONTROLS_ZIP
    with zipfile.ZipFile(controls_zip, "r") as archive:
        if archive.testzip() is not None:
            raise RuntimeError("R21 controls ZIP failed CRC validation")
        seen = {}
        for info in archive.infolist():
            base.safe_zip_name(info.filename)
            if info.is_dir():
                raise RuntimeError("R21 controls ZIP has a directory entry")
            data = archive.read(info)
            seen[info.filename] = (len(data), sha256_bytes(data))
        packed_rows = read_csv_bytes(
            archive.read("PACKED_CONTROL_SHA256.csv")
        )
    if seen != CONTROL_MEMBER_EXPECTED or len(packed_rows) != 3:
        raise RuntimeError("R21 controls ZIP member mismatch")
    for row in packed_rows:
        name = row["filename"]
        if (
            name not in {README_NAME, MANIFEST_NAME, VALIDATION_NAME}
            or (int(row["bytes"]), row["sha256"].upper())
            != CONTROL_MEMBER_EXPECTED[name]
        ):
            raise RuntimeError(f"R21 packed-control mismatch: {name}")

    result = {}
    for name, path in PRIMARY_LOCAL_PATHS.items():
        observed = identity(path)
        if observed != PRIMARY_EXPECTED[name]:
            raise RuntimeError(f"Primary local identity mismatch: {name}")
        result[name] = {
            "path": path,
            "bytes": observed[0],
            "sha256": observed[1],
            "md5": base.md5_file(path),
        }
    return result


def fetch_predecessor_manifest(
    session,
    predecessor: dict,
    receipt: dict,
) -> list[dict[str, str]]:
    entry = base.entries_map(predecessor)[CONTROLS_ZIP]
    response = base.check(
        session.get(entry["links"]["content"], timeout=(30, 180)),
        {200},
    )
    data = response.content
    wanted = receipt["files"][CONTROLS_ZIP]
    if (len(data), sha256_bytes(data)) != (
        int(wanted["bytes"]),
        wanted["sha256"].upper(),
    ):
        raise RuntimeError("Predecessor controls ZIP readback mismatch")
    with zipfile.ZipFile(io.BytesIO(data), "r") as archive:
        if archive.testzip() is not None:
            raise RuntimeError("Predecessor controls ZIP CRC mismatch")
        rows = read_csv_bytes(archive.read(MANIFEST_NAME))
    if len(rows) != 66:
        raise RuntimeError("Predecessor packed manifest boundary mismatch")
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
    if (
        legacy.get("state") != "done"
        or not legacy.get("submitted")
        or not legacy.get("links", {}).get("newversion")
    ):
        raise RuntimeError("Predecessor is not a submitted versioning base")
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
        raise RuntimeError("Successor draft did not inherit predecessor set")
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
    if len(predecessor_rows) != 66:
        raise RuntimeError("Predecessor packed control rows changed")
    if len(predecessor_identities) != EXPECTED_PREDECESSOR_FILES:
        raise RuntimeError("Predecessor identity boundary changed")
    if set(primary_local) != set(PRIMARY_LOCAL_PATHS):
        raise RuntimeError("R21 primary file set changed")

    expected_without_controls = {
        name: row
        for name, row in predecessor_identities.items()
        if name not in REPLACED_NAMES
    }
    expected_without_controls[SGA3_PDF] = primary_local[SGA3_PDF]
    expected_without_controls[SGA3_ZIP] = primary_local[SGA3_ZIP]
    if len(expected_without_controls) != EXPECTED_MANIFEST_ROWS:
        raise RuntimeError("Prospective release-manifest boundary mismatch")

    with zipfile.ZipFile(
        primary_local[CONTROLS_ZIP]["path"],
        "r",
    ) as archive:
        rows = read_csv_bytes(archive.read(MANIFEST_NAME))
        validation = json.loads(
            archive.read(VALIDATION_NAME).decode("utf-8")
        )
    row_map = {row["filename"]: row for row in rows}
    if len(row_map) != len(rows) or set(row_map) != set(
        expected_without_controls
    ):
        raise RuntimeError("R21 prospective release-manifest set mismatch")
    for name, wanted in expected_without_controls.items():
        row = row_map[name]
        if (int(row["bytes"]), row["sha256"].upper()) != (
            wanted["bytes"],
            wanted["sha256"],
        ):
            raise RuntimeError(
                f"R21 prospective release-manifest identity mismatch: {name}"
            )
    if (
        validation.get("status") != "PASS"
        or validation.get("errors") != []
        or validation.get("source_record") != PREDECESSOR_RECORD
        or validation.get("prospective_files") != EXPECTED_FINAL_FILES
        or validation.get("retained_files")
        != EXPECTED_RETAINED_PREDECESSOR_FILES
        or validation.get("default_preview") != DEFAULT_PREVIEW
    ):
        raise RuntimeError("R21 packed release validation mismatch")
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
            "20260729_sga3_reader_clean_r21_record_"
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
