#!/usr/bin/env python3
"""Correct the SGA6 page count in the canonical SGA reader controls."""

from __future__ import annotations

import copy
import csv
import importlib.util
import io
import json
import os
import shutil
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
BASE_PATH = (
    SCRIPT_DIR
    / "publish_sga_canonical_reader_surface_r20_zenodo_20260729.py"
)
SPEC = importlib.util.spec_from_file_location("sga_canonical_r20", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load the canonical SGA publication workflow")
previous = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = previous
SPEC.loader.exec_module(previous)
base = previous.base


PREDECESSOR_RECORD = 21683020
PREDECESSOR_DOI = "10.5281/zenodo.21683020"
CONCEPT_DOI = previous.CONCEPT_DOI
PUBLICATION_DATE = previous.PUBLICATION_DATE
VERSION = "2026-07-29 canonical SGA1-6 reader surface"
TITLE = previous.TITLE
DEFAULT_PREVIEW = previous.DEFAULT_PREVIEW
GITHUB_COMMIT = previous.GITHUB_COMMIT
GITHUB_PACKAGE = previous.GITHUB_PACKAGE

README_NAME = previous.README_NAME
MANIFEST_NAME = previous.MANIFEST_NAME
VALIDATION_NAME = previous.VALIDATION_NAME
REPLACED_NAMES = {README_NAME, MANIFEST_NAME, VALIDATION_NAME}

EXPECTED_PREDECESSOR_FILES = 68
EXPECTED_FINAL_FILES = 68
EXPECTED_RETAINED_PREDECESSOR_FILES = 65
EXPECTED_UNRELATED_RETAINED_FILES = 65
EXPECTED_MANIFEST_ROWS = 66
EXPECTED_ZIP_ARCHIVES = previous.EXPECTED_ZIP_ARCHIVES
EXPECTED_ZIP_FILE_MEMBERS = previous.EXPECTED_ZIP_FILE_MEMBERS
EXPECTED_ZIP_DIRECTORY_ENTRIES = previous.EXPECTED_ZIP_DIRECTORY_ENTRIES
EXPECTED_ZIP_ALL_ENTRIES = previous.EXPECTED_ZIP_ALL_ENTRIES
EXPECTED_ZIP_UNCOMPRESSED_BYTES = previous.EXPECTED_ZIP_UNCOMPRESSED_BYTES
EXPECTED_GITHUB_READBACK_FILES = previous.EXPECTED_GITHUB_READBACK_FILES

REPO_ROOT = SCRIPT_DIR.parent
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
PREDECESSOR_RECEIPT = (
    RECEIPT_ROOT
    / "20260728_sga3_cumulative_with_x_record_21683020_public_readback.json"
)
TEMP_ROOT = Path(os.environ["LOCALAPPDATA"]) / "Temp"
CONTROLS_ROOT = TEMP_ROOT / "sga_canonical_reader_surface_control_correction"
READBACK_ROOT = TEMP_ROOT / "sga_canonical_reader_surface_correction_readback"
DRAFT_STATE = (
    RECEIPT_ROOT
    / "20260729_sga_canonical_reader_surface_correction_zenodo_draft_state.json"
)

PRIMARY_LOCAL_PATHS: dict[str, Path] = {}
NEW_MANIFEST_ROWS = {
    README_NAME: {
        "role": "reader_index",
        "provenance": "plain index to the direct readers and source archives",
        "status": "current",
    }
}
DESCRIPTION_HTML = previous.DESCRIPTION_HTML
NOTES_HTML = previous.NOTES_HTML

DIRECT_EXPECTED = {
    "00a_SGA1_English_Reader.pdf": (
        2_490_530,
        "D424E4A3E98E8C80C642BE5E5B8AAD813FF3F12D946BF53E237F6508387AC53B",
    ),
    "00b_SGA2_English_Reader.pdf": (
        2_001_862,
        "AA8663D393CAE37D0D917E16E911F12D64AD90B90829CFCE601557AD759DEDFA",
    ),
    "00c_SGA3_English_Reader.pdf": (
        6_811_667,
        "22A61E1C018EB0722635CADDAD71981EFE7BA0B01AD06ACBD7F8D0A9366FF8DB",
    ),
    "00d_SGA4_English_Reader.pdf": (
        4_420_366,
        "982DB88559FE4239CF3381D664792C2262658D511FA0A8A06FE99A1A68512BA5",
    ),
    "00e_SGA5_English_Reader.pdf": (
        2_431_050,
        "9BB41B09624BFEB566503EAADD3276B709F9E1AC03E2F71188E0CE7E80A00A38",
    ),
    "00f_SGA6_English_Reader.pdf": (
        3_189_902,
        "E14FF6F4F2AD65BBCAA8410B9DF7DBD480D193A6CA97AF5F4428E7AB6B60B2FE",
    ),
}
READER_PAGES = {
    "SGA1": 259,
    "SGA2": 178,
    "SGA3": 1_459,
    "SGA4": 864,
    "SGA5": 309,
    "SGA6": 376,
}


def guarded_remove(path: Path) -> None:
    if not path.exists():
        return
    resolved = path.resolve()
    if TEMP_ROOT.resolve() not in resolved.parents:
        raise RuntimeError(f"Refusing to remove a non-temporary path: {path}")
    shutil.rmtree(path)


def verify_primary_local_files() -> dict[str, dict]:
    receipt = json.loads(PREDECESSOR_RECEIPT.read_text(encoding="utf-8-sig"))
    if (
        receipt.get("status") != "PASS"
        or int(receipt.get("record", -1)) != PREDECESSOR_RECORD
        or receipt.get("conceptdoi") != CONCEPT_DOI
        or len(receipt.get("files", {})) != EXPECTED_PREDECESSOR_FILES
    ):
        raise RuntimeError("Canonical predecessor receipt is not controlling")
    for name, expected in DIRECT_EXPECTED.items():
        row = receipt["files"].get(name)
        if row is None or not row.get("match"):
            raise RuntimeError(f"Canonical predecessor file is missing: {name}")
        if (int(row["bytes"]), row["sha256"].upper()) != expected:
            raise RuntimeError(f"Canonical predecessor identity mismatch: {name}")
    old_direct = {
        name
        for name in receipt["files"]
        if (
            name.startswith(("00a_", "00b_", "00c00_", "00d_", "00e_", "00f_"))
            and name not in DIRECT_EXPECTED
        )
    }
    if old_direct:
        raise RuntimeError(f"Status-heavy direct names remain: {sorted(old_direct)}")
    return {}


def fetch_predecessor_manifest(
    session, predecessor: dict, receipt: dict
) -> list[dict[str, str]]:
    entry = base.entries_map(predecessor)[MANIFEST_NAME]
    response = base.check(
        session.get(entry["links"]["content"], timeout=(30, 180)),
        {200},
    )
    content = response.content
    wanted = receipt["files"][MANIFEST_NAME]
    if (
        len(content),
        base.hashlib.sha256(content).hexdigest().upper(),
    ) != (
        int(wanted["bytes"]),
        wanted["sha256"].upper(),
    ):
        raise RuntimeError("Canonical predecessor manifest mismatch")
    rows = list(
        csv.DictReader(
            io.StringIO(content.decode("utf-8-sig"), newline="")
        )
    )
    if len(rows) != EXPECTED_MANIFEST_ROWS:
        raise RuntimeError("Canonical predecessor manifest row mismatch")
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
        raise RuntimeError("Correction draft did not inherit the predecessor")
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


def readme_text(draft_id: int) -> str:
    return previous.readme_text(draft_id)


def generate_controls(
    draft_id: int,
    predecessor_rows: list[dict[str, str]],
    predecessor_identities: dict[str, dict],
    primary_local: dict[str, dict],
) -> dict[str, dict]:
    if primary_local:
        raise RuntimeError("Control correction must not add primary files")
    guarded_remove(CONTROLS_ROOT)
    CONTROLS_ROOT.mkdir(parents=True)

    readme_path = CONTROLS_ROOT / README_NAME
    readme_path.write_text(readme_text(draft_id), encoding="utf-8")
    readme_identity = {
        "path": readme_path,
        "bytes": readme_path.stat().st_size,
        "sha256": base.sha256_file(readme_path),
        "md5": base.md5_file(readme_path),
    }

    rows: list[dict[str, str]] = []
    for row in predecessor_rows:
        name = row["filename"]
        if name in REPLACED_NAMES:
            continue
        identity = predecessor_identities[name]
        if (int(row["bytes"]), row["sha256"].upper()) != (
            identity["bytes"],
            identity["sha256"],
        ):
            raise RuntimeError(f"Retained manifest mismatch: {name}")
        rows.append(dict(row))
    rows.append(
        {
            "filename": README_NAME,
            "bytes": str(readme_identity["bytes"]),
            "sha256": readme_identity["sha256"],
            **NEW_MANIFEST_ROWS[README_NAME],
        }
    )
    rows.sort(key=lambda row: row["filename"].casefold())
    if len(rows) != EXPECTED_MANIFEST_ROWS:
        raise RuntimeError("Corrected manifest row boundary mismatch")

    manifest_path = CONTROLS_ROOT / MANIFEST_NAME
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=(
                "filename",
                "bytes",
                "sha256",
                "role",
                "provenance",
                "status",
            ),
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)
    manifest_identity = {
        "path": manifest_path,
        "bytes": manifest_path.stat().st_size,
        "sha256": base.sha256_file(manifest_path),
        "md5": base.md5_file(manifest_path),
    }

    validation = {
        "schema": "sga_canonical_reader_surface_control_correction_v1",
        "status": "PASS",
        "errors": [],
        "concept_doi": CONCEPT_DOI,
        "predecessor_record": PREDECESSOR_RECORD,
        "reserved_successor_record": draft_id,
        "correction": {
            "field": "SGA6 page count",
            "old_value": 377,
            "correct_value": 376,
            "reader_bytes_changed": False,
        },
        "retained_files": EXPECTED_RETAINED_PREDECESSOR_FILES,
        "final_files": EXPECTED_FINAL_FILES,
        "manifest_rows": EXPECTED_MANIFEST_ROWS,
        "default_preview": DEFAULT_PREVIEW,
        "readers": {
            sga: {
                "filename": name,
                "pages": READER_PAGES[sga],
                "bytes": predecessor_identities[name]["bytes"],
                "sha256": predecessor_identities[name]["sha256"],
            }
            for sga, name in (
                ("SGA1", "00a_SGA1_English_Reader.pdf"),
                ("SGA2", "00b_SGA2_English_Reader.pdf"),
                ("SGA3", "00c_SGA3_English_Reader.pdf"),
                ("SGA4", "00d_SGA4_English_Reader.pdf"),
                ("SGA5", "00e_SGA5_English_Reader.pdf"),
                ("SGA6", "00f_SGA6_English_Reader.pdf"),
            )
        },
        "zip_surface_expected": {
            "archives": EXPECTED_ZIP_ARCHIVES,
            "file_members": EXPECTED_ZIP_FILE_MEMBERS,
            "directory_entries": EXPECTED_ZIP_DIRECTORY_ENTRIES,
            "all_entries": EXPECTED_ZIP_ALL_ENTRIES,
            "uncompressed_bytes": EXPECTED_ZIP_UNCOMPRESSED_BYTES,
        },
        "duplicate_concept_created": False,
        "second_draft_created": False,
        "new_license_grant": False,
    }
    validation_path = CONTROLS_ROOT / VALIDATION_NAME
    base.save_json(validation_path, validation)
    validation_identity = {
        "path": validation_path,
        "bytes": validation_path.stat().st_size,
        "sha256": base.sha256_file(validation_path),
        "md5": base.md5_file(validation_path),
    }
    return {
        README_NAME: readme_identity,
        MANIFEST_NAME: manifest_identity,
        VALIDATION_NAME: validation_identity,
    }


def assert_metadata(metadata: dict) -> None:
    if metadata.get("title") != TITLE:
        raise RuntimeError("Title metadata mismatch")
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
        raise RuntimeError("Notes metadata mismatch")


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
    base.patch_notes(metadata)
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
    if (
        reread["files"].get("default_preview") != DEFAULT_PREVIEW
        or set(reread["files"]["entries"]) != set(expected)
    ):
        raise RuntimeError("Corrected draft reread mismatch")
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
        raise RuntimeError("Published correction escaped the existing concept")
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
        "duplicate_concept_created": False,
        "second_draft_created": False,
    }
    base.save_json(
        RECEIPT_ROOT
        / (
            "20260729_sga_canonical_reader_surface_correction_record_"
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
    "NOTES_HTML": NOTES_HTML,
    "DEFAULT_PREVIEW": DEFAULT_PREVIEW,
}.items():
    setattr(base, name, value)

base.verify_primary_local_files = verify_primary_local_files
base.fetch_predecessor_manifest = fetch_predecessor_manifest
base.create_or_resume_draft = create_or_resume_draft
base.readme_text = readme_text
base.generate_controls = generate_controls
base.assert_metadata = assert_metadata
base.publish_draft = publish_draft


if __name__ == "__main__":
    base.main()
