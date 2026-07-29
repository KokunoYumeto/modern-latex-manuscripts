#!/usr/bin/env python3
"""Publish the compact EGA assigned-source-first same-concept successor."""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import importlib.util
import io
import json
import os
import shutil
import sys
import time
import zipfile
from pathlib import Path
from urllib.parse import quote


SCRIPT_DIR = Path(__file__).resolve().parent
BASE_PATH = (
    SCRIPT_DIR
    / "publish_ega0_iii_section11_source_first_zenodo_20260728.py"
)
SPEC = importlib.util.spec_from_file_location("ega_section11_20260728", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load the established EGA publication workflow")
base = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = base
SPEC.loader.exec_module(base)


API = base.API
CONCEPT_DOI = "10.5281/zenodo.20414353"
PREDECESSOR_RECORD = 21_652_720
PREDECESSOR_DOI = "10.5281/zenodo.21652720"
PUBLICATION_DATE = "2026-07-29"
VERSION = (
    "2026-07-29 EGA 0/III sections 8-13 and "
    "EGA III sections 1-7 source-first working checkpoints"
)
TITLE = (
    "Elements de geometrie algebrique (EGA): French Originals, "
    "English Working Readers, and Source Archives"
)

GITHUB_COMMIT = "35fce7afa8c495130947ecf1f9ad6535c3582c0e"
GITHUB_PACKAGE = (
    "sources/ega/checkpoints/"
    "ega0-iii-and-ega3-source-first-assigned-lane-complete-20260729"
)

EGA0_PDF = (
    "00a_EGA0_English_Working_Reader_"
    "Assigned_SourceFirst_Sections8_13_20260729.pdf"
)
EGA3_PDF = (
    "00b_EGA3_English_Working_Reader_"
    "Assigned_SourceFirst_Sections1_7_20260729.pdf"
)
EGA0_TEX = (
    "02a_EGA0_English_Working_Master_"
    "Assigned_SourceFirst_Sections8_13_20260729.tex"
)
EGA3_TEX = (
    "02b_EGA3_English_Working_Master_"
    "Assigned_SourceFirst_Sections1_7_20260729.tex"
)
SOURCE_ZIP = "10a_EGA0_III_and_EGA3_Assigned_Lane_Source_20260729.zip"
CONTROLS_ZIP = (
    "90a_EGA0_III_and_EGA3_"
    "Assigned_SourceFirst_Controls_20260729.zip"
)
DEFAULT_PREVIEW = EGA0_PDF

OLD_SECTION11_FILES = {
    (
        "00a_EGA0_English_Working_Reader_"
        "SourceFirst_11_5_1_to_11_10_3_20260728.pdf"
    ),
    (
        "02a_EGA0_III_Section11_English_"
        "SourceFirst_11_5_1_to_11_10_3_20260728.tex"
    ),
    (
        "10a_EGA0_English_Working_Source_"
        "with_Section11_SourceFirst_20260728.zip"
    ),
    "90a_EGA0_III_SourceFirst_11_5_1_to_11_10_3_Status_20260728.md",
    "91a_EGA0_III_SourceFirst_11_5_1_to_11_10_3_Validation_20260728.json",
}

EXPECTED_PREDECESSOR_FILES = 21
EXPECTED_RETAINED_FILES = 16
EXPECTED_NEW_FILES = 6
EXPECTED_FINAL_FILES = 22
EXPECTED_PACKAGE_FILES = 11
EXPECTED_SOURCE_ZIP_MEMBERS = 44
EXPECTED_SOURCE_ZIP_MANIFEST_ROWS = 43
EXPECTED_SOURCE_ZIP_UNCOMPRESSED_BYTES = 1_904_261
EXPECTED_SOURCE_ZIP_MANIFEST_BYTES = 4_484
EXPECTED_SOURCE_ZIP_MANIFEST_SHA256 = (
    "5985AA0BC2F8C36D2494B0325A032DA695719B1B4C058539E0916CD15EAA6020"
)
EXPECTED_CONTROL_ZIP_MEMBERS = 6

REPO_ROOT = SCRIPT_DIR.parent
PACKAGE_ROOT = REPO_ROOT / GITHUB_PACKAGE
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
TEMP_ROOT = Path(os.environ["LOCALAPPDATA"]) / "Temp"
CONTROLS_ROOT = TEMP_ROOT / "ega_assigned_source_first_compact_controls"
READBACK_ROOT = TEMP_ROOT / "ega_assigned_source_first_compact_readback"
DRAFT_STATE = (
    RECEIPT_ROOT
    / "20260729_ega_assigned_source_first_compact_zenodo_draft_state.json"
)
PREDECESSOR_RECEIPT = (
    RECEIPT_ROOT
    / "20260728_ega0_iii_section11_record_21652720_public_readback.json"
)
PREDECESSOR_ZIP_RECEIPT = (
    RECEIPT_ROOT
    / "20260728_ega0_iii_section11_record_21652720_zip_member_readback.json"
)
PUBLIC_PARTIAL = (
    RECEIPT_ROOT
    / "20260729_ega_assigned_source_first_compact_public_readback.partial.json"
)

PRIMARY_NAMES = {EGA0_PDF, EGA3_PDF, EGA0_TEX, EGA3_TEX, SOURCE_ZIP}
PRIMARY_PATHS = {name: PACKAGE_ROOT / name for name in PRIMARY_NAMES}
PRIMARY_EXPECTED = {
    EGA0_PDF: (
        1_190_098,
        "D0454AA8BB79653D9CC97C7973EB54B2038BF8038525022038A29E9628C978F4",
    ),
    EGA3_PDF: (
        1_284_316,
        "1C2A3F286A02EBBB521D0D4939B0604A7D8000023288F4599322EFC0FA21B886",
    ),
    EGA0_TEX: (
        787,
        "35991ACEB8C7467344198E5B09E725DDD96E692BA1F14DECAE7A55C059FEFEAF",
    ),
    EGA3_TEX: (
        3_294,
        "931DDCEBB043AC945AAA5C1D3556458E01ED547C55C02644E864918D48EA33E1",
    ),
    SOURCE_ZIP: (
        468_919,
        "B645E2F59F79F7F4DCD6A78922E0566C1DBF02590C0629358795EF49CA640BDF",
    ),
}

CONTROL_MEMBERS = (
    "README.md",
    "PROVENANCE_AND_RIGHTS.md",
    "PUBLICATION_READINESS.md",
    "BUILD_SUMMARY_PUBLIC.md",
    "PACKAGE_VALIDATION.json",
    "SHA256SUMS.csv",
)

DESCRIPTION_PARAGRAPHS = [
    (
        "This same-concept successor preserves 16 unrelated files from "
        "version 10.5281/zenodo.21652720 byte-identically. It replaces the "
        "five bounded section-11 live-surface objects with two current "
        "English working readers, two direct editable master TeX files, one "
        "grouped source ZIP, and one grouped controls ZIP."
    ),
    (
        "The 120-page EGA 0/III reader preserves the completed assigned "
        "source-first lane for Sections 8-13 in a layered working container. "
        "The 150-page EGA III reader contains the completed assigned English "
        "Sections 1-7 and ends at 7.9.14, followed by 'To be continued.'"
    ),
    (
        "The EGA 0/III reader has 392 named destinations and 846 valid "
        "internal GoTo actions. The EGA III reader has 488 named destinations "
        "and 1,037 valid internal GoTo actions. Their direct TeX masters are "
        "present for inspection; 43 recursive source files and an exact "
        "internal identity manifest are grouped in one 44-member source ZIP."
    ),
    (
        "The controlling authorities are the frozen NUMDAM EGA 0/III and "
        "EGA III PDFs already represented in this concept. They are not "
        "duplicated in this checkpoint. Existing user-supplied OCR and "
        "external English lineages were consulted read-only as locator or "
        "drafting controls; no OCR was generated or rerun."
    ),
    (
        "These are machine-assisted scholarly working checkpoints, not "
        "completion of EGA, critical editions, independent human "
        "certification, rights determinations, final exhaustive-reference "
        "certification, or tagged-PDF accessibility remediation. No new "
        "license grant or transfer of underlying rights is asserted."
    ),
]
DESCRIPTION_HTML = "\n".join(
    f"<p>{paragraph}</p>" for paragraph in DESCRIPTION_PARAGRAPHS
)
NOTES_HTML = (
    "<p>The preferred preview is the current EGA 0/III Sections 8-13 "
    "working reader. Current readers and editable master TeX files are "
    "directly visible; recursive source and release controls are grouped "
    "into compact ZIPs. Immutable predecessor versions preserve the bounded "
    "section-11 release history.</p>"
)


def identity(path: Path) -> dict:
    return {
        "path": path,
        "bytes": path.stat().st_size,
        "sha256": base.sha256_file(path),
        "md5": base.md5_file(path),
    }


def clean_temp(path: Path) -> None:
    if not path.exists():
        return
    resolved = path.resolve()
    if TEMP_ROOT.resolve() not in resolved.parents:
        raise RuntimeError(f"Refusing cleanup outside {TEMP_ROOT}")
    shutil.rmtree(path)


def github_readback() -> None:
    session = base.make_session()
    raw_root = (
        "https://raw.githubusercontent.com/"
        f"KokunoYumeto/modern-latex-manuscripts/{GITHUB_COMMIT}/"
        f"{GITHUB_PACKAGE}/"
    )
    local_files = sorted(
        (path for path in PACKAGE_ROOT.iterdir() if path.is_file()),
        key=lambda path: path.name.casefold(),
    )
    if len(local_files) != EXPECTED_PACKAGE_FILES:
        raise RuntimeError("GitHub EGA package file boundary mismatch")
    for index, path in enumerate(local_files, start=1):
        print(
            f"GITHUB READBACK {index}/{len(local_files)} {path.name}",
            flush=True,
        )
        response = base.check(
            session.get(raw_root + quote(path.name), timeout=(30, 180)),
            {200},
        )
        data = response.content
        if (len(data), hashlib.sha256(data).hexdigest().upper()) != (
            path.stat().st_size,
            base.sha256_file(path),
        ):
            raise RuntimeError(f"GitHub EGA readback mismatch: {path.name}")


def source_zip_summary(path: Path, *, include_members: bool) -> dict:
    summary = base.inspect_zip(path, include_members=include_members)
    with zipfile.ZipFile(path) as archive:
        names = {
            info.filename
            for info in archive.infolist()
            if not info.is_dir()
        }
        if "SOURCE_MANIFEST.csv" not in names:
            raise RuntimeError("EGA source ZIP lacks SOURCE_MANIFEST.csv")
        manifest_bytes = archive.read("SOURCE_MANIFEST.csv")
        rows = list(
            csv.DictReader(
                io.StringIO(manifest_bytes.decode("utf-8-sig"), newline="")
            )
        )
        errors = []
        for row in rows:
            member = row["path"]
            if member not in names:
                errors.append(f"missing:{member}")
                continue
            data = archive.read(member)
            if (
                len(data) != int(row["bytes"])
                or hashlib.sha256(data).hexdigest().upper()
                != row["sha256"].upper()
            ):
                errors.append(f"identity:{member}")
        summary["internal_manifest"] = {
            "rows": len(rows),
            "bytes": len(manifest_bytes),
            "sha256": hashlib.sha256(manifest_bytes).hexdigest().upper(),
            "errors": errors,
        }
    return summary


def assert_source_zip(summary: dict) -> None:
    manifest = summary["internal_manifest"]
    if (
        summary["file_members"] != EXPECTED_SOURCE_ZIP_MEMBERS
        or summary["directory_entries"] != 0
        or summary["all_entries"] != EXPECTED_SOURCE_ZIP_MEMBERS
        or summary["uncompressed_bytes"] != EXPECTED_SOURCE_ZIP_UNCOMPRESSED_BYTES
        or not summary["safe_paths"]
        or summary["crc_error"] is not None
        or manifest["rows"] != EXPECTED_SOURCE_ZIP_MANIFEST_ROWS
        or manifest["bytes"] != EXPECTED_SOURCE_ZIP_MANIFEST_BYTES
        or manifest["sha256"] != EXPECTED_SOURCE_ZIP_MANIFEST_SHA256
        or manifest["errors"]
    ):
        raise RuntimeError("EGA source ZIP closure mismatch")


def verify_primary_files() -> dict[str, dict]:
    result = {}
    for name, path in PRIMARY_PATHS.items():
        if not path.is_file():
            raise FileNotFoundError(path)
        actual = identity(path)
        if (actual["bytes"], actual["sha256"]) != PRIMARY_EXPECTED[name]:
            raise RuntimeError(f"EGA primary identity mismatch: {name}")
        result[name] = actual

    package_files = {
        path.name: path
        for path in PACKAGE_ROOT.iterdir()
        if path.is_file()
    }
    if len(package_files) != EXPECTED_PACKAGE_FILES:
        raise RuntimeError("EGA package set mismatch")
    manifest_path = PACKAGE_ROOT / "SHA256SUMS.csv"
    rows = list(
        csv.DictReader(
            io.StringIO(
                manifest_path.read_text(encoding="utf-8-sig"),
                newline="",
            )
        )
    )
    if len(rows) != EXPECTED_PACKAGE_FILES - 1:
        raise RuntimeError("EGA package manifest row mismatch")
    for row in rows:
        path = PACKAGE_ROOT / row["filename"]
        if not path.is_file():
            raise FileNotFoundError(path)
        if (path.stat().st_size, base.sha256_file(path)) != (
            int(row["bytes"]),
            row["sha256"].upper(),
        ):
            raise RuntimeError(f"EGA package manifest mismatch: {path.name}")

    validation = json.loads(
        (PACKAGE_ROOT / "PACKAGE_VALIDATION.json").read_text(encoding="utf-8")
    )
    if validation.get("status") != "PASS" or validation.get("errors") != []:
        raise RuntimeError("EGA package validation is not PASS")
    if validation.get("privacy_hits") != []:
        raise RuntimeError("EGA package privacy validation changed")
    expected_reader_metrics = {
        EGA0_PDF: (120, 392, 846),
        EGA3_PDF: (150, 488, 1_037),
    }
    for name, wanted in expected_reader_metrics.items():
        row = validation["reader_metrics"][name]
        actual = (
            row["pages"],
            row["named_destinations"],
            row["internal_goto_actions"],
        )
        if (
            actual != wanted
            or row["invalid_actions"] != 0
            or row["reader_process_hits"] != []
        ):
            raise RuntimeError(f"EGA reader validation mismatch: {name}")

    assert_source_zip(
        source_zip_summary(PRIMARY_PATHS[SOURCE_ZIP], include_members=False)
    )
    github_readback()
    return result


def build_controls_zip() -> dict:
    clean_temp(CONTROLS_ROOT)
    CONTROLS_ROOT.mkdir(parents=True)
    path = CONTROLS_ROOT / CONTROLS_ZIP
    expected_members = {}
    with zipfile.ZipFile(
        path,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as archive:
        for name in CONTROL_MEMBERS:
            source = PACKAGE_ROOT / name
            data = source.read_bytes()
            info = zipfile.ZipInfo(name, date_time=(2026, 7, 29, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED)
            expected_members[name] = {
                "bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest().upper(),
            }
    summary = base.inspect_zip(path, include_members=True)
    if (
        summary["file_members"] != EXPECTED_CONTROL_ZIP_MEMBERS
        or summary["directory_entries"] != 0
        or summary["all_entries"] != EXPECTED_CONTROL_ZIP_MEMBERS
        or summary["crc_error"] is not None
        or not summary["safe_paths"]
        or {
            row["relative_path"]: {
                "bytes": row["bytes"],
                "sha256": row["sha256"],
            }
            for row in summary["members"]
        }
        != expected_members
    ):
        raise RuntimeError("EGA controls ZIP closure mismatch")
    result = identity(path)
    result["zip_summary"] = summary
    return result


def load_predecessor_receipt() -> dict:
    if (
        not PREDECESSOR_RECEIPT.is_file()
        or not PREDECESSOR_ZIP_RECEIPT.is_file()
    ):
        raise RuntimeError("Missing current EGA predecessor receipt")
    receipt = json.loads(PREDECESSOR_RECEIPT.read_text(encoding="utf-8"))
    zip_receipt = json.loads(
        PREDECESSOR_ZIP_RECEIPT.read_text(encoding="utf-8")
    )
    if (
        receipt.get("status") != "PASS"
        or int(receipt.get("record", -1)) != PREDECESSOR_RECORD
        or receipt.get("doi") != PREDECESSOR_DOI
        or receipt.get("conceptdoi") != CONCEPT_DOI
        or len(receipt.get("files", {})) != EXPECTED_PREDECESSOR_FILES
        or not OLD_SECTION11_FILES.issubset(receipt["files"])
        or zip_receipt.get("status") != "PASS"
        or int(zip_receipt.get("record", -1)) != PREDECESSOR_RECORD
        or len(zip_receipt.get("archives", {})) != 5
    ):
        raise RuntimeError("EGA predecessor receipt is not controlling")
    receipt["zip_summaries"] = zip_receipt["archives"]
    return receipt


def receipt_identities(receipt: dict) -> dict[str, dict]:
    return {
        name: {
            "bytes": int(row["bytes"]),
            "sha256": row["sha256"].upper(),
            "md5": row["md5"].lower(),
        }
        for name, row in receipt["files"].items()
    }


def verify_live_predecessor(session, receipt: dict) -> dict:
    headers = {"Accept": "application/vnd.inveniordm.v1+json"}
    predecessor = base.check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}?expand=true",
            headers=headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    entries = base.entries_map(predecessor)
    if (
        int(predecessor["id"]) != PREDECESSOR_RECORD
        or base.concept_doi(predecessor) != CONCEPT_DOI
        or base.version_doi(predecessor) != PREDECESSOR_DOI
        or set(entries) != set(receipt["files"])
    ):
        raise RuntimeError("Live EGA predecessor identity changed")
    for name, row in receipt["files"].items():
        entry = entries[name]
        if (
            int(entry["size"]),
            base.normalize_checksum(entry["checksum"]),
        ) != (
            int(row["bytes"]),
            row["md5"].lower(),
        ):
            raise RuntimeError(f"Live EGA predecessor drift: {name}")
    latest = base.check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}/versions/latest?expand=true",
            headers=headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if (
        int(latest["id"]) != PREDECESSOR_RECORD
        or base.concept_doi(latest) != CONCEPT_DOI
    ):
        raise RuntimeError("EGA concept head moved; refusing parallel successor")
    return predecessor


def retained_identities(receipt: dict) -> dict[str, dict]:
    identities = receipt_identities(receipt)
    retained = {
        name: row
        for name, row in identities.items()
        if name not in OLD_SECTION11_FILES
    }
    if len(retained) != EXPECTED_RETAINED_FILES:
        raise RuntimeError("Unexpected retained EGA predecessor boundary")
    return retained


def create_or_resume_draft(session, token: str, predecessor: dict) -> int:
    auth = {"Authorization": f"Bearer {token}"}
    vendor = {
        **auth,
        "Accept": "application/vnd.inveniordm.v1+json",
    }
    existing = session.get(
        f"{API}/records/{PREDECESSOR_RECORD}/draft",
        headers=vendor,
        timeout=(30, 180),
    )
    if existing.status_code == 200:
        if not DRAFT_STATE.is_file():
            raise RuntimeError("Untracked EGA successor draft exists")
        state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
        draft = existing.json()
        draft_id = int(draft["id"])
        if (
            draft_id != int(state["draft_id"])
            or int(state["predecessor_record"]) != PREDECESSOR_RECORD
            or base.concept_doi(draft) != CONCEPT_DOI
        ):
            raise RuntimeError("Existing EGA draft is not the tracked draft")
        return draft_id
    base.check(existing, {404})

    if DRAFT_STATE.is_file():
        state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
        if state.get("published"):
            raise RuntimeError("Tracked EGA successor is published")
        draft_id = int(state["draft_id"])
        tracked = session.get(
            f"{API}/records/{draft_id}/draft",
            headers=vendor,
            timeout=(30, 180),
        )
        if tracked.status_code == 200:
            draft = tracked.json()
            if (
                int(draft["id"]) != draft_id
                or int(state["predecessor_record"]) != PREDECESSOR_RECORD
                or base.concept_doi(draft) != CONCEPT_DOI
            ):
                raise RuntimeError("Tracked EGA draft identity changed")
            return draft_id
        base.check(tracked, {404})
        raise RuntimeError("Tracked EGA draft state exists but draft is absent")

    legacy = base.check(
        session.get(
            f"{API}/deposit/depositions/{PREDECESSOR_RECORD}",
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
        raise RuntimeError("EGA predecessor is not a versioning base")
    created = base.check(
        session.post(
            legacy["links"]["newversion"],
            headers=auth,
            timeout=(30, 300),
        ),
        {201},
    ).json()
    draft = base.check(
        session.get(
            created["links"]["latest_draft"],
            headers=auth,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    draft_id = int(draft["id"])
    if (
        base.concept_doi(draft) != CONCEPT_DOI
        or set(base.legacy_file_map(draft))
        != set(base.entries_map(predecessor))
    ):
        raise RuntimeError("New EGA version did not inherit exact predecessor")
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


def final_expected(
    retained: dict[str, dict],
    primary: dict[str, dict],
    controls: dict,
) -> tuple[dict[str, dict], dict[str, dict]]:
    local = {**primary, CONTROLS_ZIP: controls}
    if set(retained) & set(local):
        raise RuntimeError("New EGA filenames collide with retained files")
    expected = {**retained, **local}
    if (
        len(local) != EXPECTED_NEW_FILES
        or len(expected) != EXPECTED_FINAL_FILES
    ):
        raise RuntimeError("Unexpected final EGA file boundary")
    return expected, local


def stage_draft(
    session,
    token: str,
    draft_id: int,
    expected: dict[str, dict],
    local: dict[str, dict],
) -> dict:
    auth = {"Authorization": f"Bearer {token}"}
    deposition = base.check(
        session.get(
            f"{API}/deposit/depositions/{draft_id}",
            headers=auth,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if deposition.get("state") != "unsubmitted" or deposition.get("submitted"):
        raise RuntimeError("Tracked EGA successor is not unpublished")
    files = base.legacy_file_map(deposition)
    extras = set(files) - set(expected)
    if not extras.issubset(OLD_SECTION11_FILES):
        raise RuntimeError(f"Unexpected inherited EGA draft files: {sorted(extras)}")

    actions = []
    for name in sorted(extras, key=str.casefold):
        base.check(
            session.delete(
                files[name]["links"]["self"],
                headers=auth,
                timeout=(30, 300),
            ),
            {204},
        )
        actions.append({"filename": name, "action": "removed_obsolete_live_surface"})

    deposition = base.check(
        session.get(
            f"{API}/deposit/depositions/{draft_id}",
            headers=auth,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    files = base.legacy_file_map(deposition)
    bucket = deposition["links"]["bucket"].rstrip("/")
    for name in sorted(local, key=str.casefold):
        wanted = local[name]
        existing = files.get(name)
        if existing is not None:
            observed = (
                int(existing["filesize"]),
                base.normalize_checksum(existing["checksum"]),
            )
            if observed == (wanted["bytes"], wanted["md5"]):
                actions.append({"filename": name, "action": "already_exact"})
                continue
            base.check(
                session.delete(
                    existing["links"]["self"],
                    headers=auth,
                    timeout=(30, 300),
                ),
                {204},
            )
        print(f"UPLOAD {name}", flush=True)
        with wanted["path"].open("rb") as handle:
            uploaded = base.check(
                session.put(
                    f"{bucket}/{quote(name, safe='')}",
                    headers={
                        **auth,
                        "Content-Type": "application/octet-stream",
                    },
                    data=handle,
                    timeout=(30, 1800),
                ),
                {200, 201},
            ).json()
        if (
            int(uploaded.get("size", uploaded.get("filesize", -1))),
            base.normalize_checksum(uploaded.get("checksum", "")),
        ) != (
            wanted["bytes"],
            wanted["md5"],
        ):
            raise RuntimeError(f"EGA upload response mismatch: {name}")
        actions.append({"filename": name, "action": "uploaded_exact"})

    final = base.check(
        session.get(
            f"{API}/deposit/depositions/{draft_id}",
            headers=auth,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    final_files = base.legacy_file_map(final)
    if set(final_files) != set(expected):
        raise RuntimeError("Staged EGA draft file set mismatch")
    for name, wanted in expected.items():
        observed = (
            int(final_files[name]["filesize"]),
            base.normalize_checksum(final_files[name]["checksum"]),
        )
        if observed != (wanted["bytes"], wanted["md5"]):
            raise RuntimeError(f"Staged EGA identity mismatch: {name}")

    receipt = {
        "status": "PASS_STAGED",
        "errors": [],
        "predecessor_record": PREDECESSOR_RECORD,
        "draft_id": draft_id,
        "concept_doi": CONCEPT_DOI,
        "file_count": len(final_files),
        "retained_predecessor_files": EXPECTED_RETAINED_FILES,
        "removed_obsolete_files": len(OLD_SECTION11_FILES),
        "new_files": EXPECTED_NEW_FILES,
        "actions": actions,
        "duplicate_concept_created": False,
        "second_draft_created": False,
    }
    base.save_json(
        RECEIPT_ROOT
        / f"20260729_ega_assigned_source_first_record_{draft_id}_draft_files.json",
        receipt,
    )
    return receipt


def patch_notes(metadata: dict) -> None:
    rows = [
        row
        for row in metadata.get("additional_descriptions", [])
        if row.get("type", {}).get("id") != "notes"
    ]
    rows.append(
        {
            "description": NOTES_HTML,
            "type": {"id": "notes", "title": {"en": "Notes"}},
        }
    )
    metadata["additional_descriptions"] = rows


def assert_metadata(metadata: dict) -> None:
    if (
        metadata.get("title") != TITLE
        or metadata.get("version") != VERSION
        or metadata.get("publication_date") != PUBLICATION_DATE
        or metadata.get("description") != DESCRIPTION_HTML
        or not any(
            row.get("description") == NOTES_HTML
            for row in metadata.get("additional_descriptions", [])
        )
    ):
        raise RuntimeError("EGA metadata mismatch")


def modern_draft(session, token: str, draft_id: int) -> dict:
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.inveniordm.v1+json",
    }
    draft = base.check(
        session.get(
            f"{API}/records/{draft_id}/draft",
            headers=headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if int(draft["id"]) != draft_id or base.concept_doi(draft) != CONCEPT_DOI:
        raise RuntimeError("EGA draft escaped the existing concept")
    files = base.check(
        session.get(
            draft["links"]["files"],
            headers=headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    entries = files.get("entries", {})
    if isinstance(entries, list):
        entries = {row["key"]: row for row in entries}
    files["entries"] = entries
    draft["files"] = files
    return draft


def ordered_names(expected: dict[str, dict]) -> list[str]:
    priority = [
        EGA0_PDF,
        EGA3_PDF,
        "00 EGA - English Translation Working Draft.pdf",
        "01 EGA IV - English Translation Working Draft (Sections 1-21).pdf",
        EGA0_TEX,
        EGA3_TEX,
        SOURCE_ZIP,
        CONTROLS_ZIP,
    ]
    result = [name for name in priority if name in expected]
    result.extend(
        name
        for name in sorted(expected, key=str.casefold)
        if name not in result
    )
    if len(result) != len(expected):
        raise RuntimeError("EGA file-order construction failed")
    return result


def publish_draft(
    session,
    token: str,
    draft_id: int,
    expected: dict[str, dict],
) -> dict:
    draft = modern_draft(session, token, draft_id)
    if set(draft["files"]["entries"]) != set(expected):
        raise RuntimeError("Cannot publish EGA draft: file set mismatch")
    metadata = copy.deepcopy(draft["metadata"])
    metadata["title"] = TITLE
    metadata["version"] = VERSION
    metadata["publication_date"] = PUBLICATION_DATE
    metadata["description"] = DESCRIPTION_HTML
    patch_notes(metadata)
    payload = {
        "access": draft["access"],
        "files": {
            "enabled": True,
            "default_preview": DEFAULT_PREVIEW,
            "order": ordered_names(expected),
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
            f"{API}/records/{draft_id}/draft",
            headers=headers,
            json=payload,
            timeout=(30, 300),
        ),
        {200},
    ).json()
    assert_metadata(patched["metadata"])
    reread = modern_draft(session, token, draft_id)
    assert_metadata(reread["metadata"])
    if (
        reread["files"].get("default_preview") != DEFAULT_PREVIEW
        or set(reread["files"]["entries"]) != set(expected)
    ):
        raise RuntimeError("EGA draft changed after metadata patch")
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
        raise RuntimeError("Published EGA response escaped the concept")
    state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
    state.update({"published": True, "doi": base.version_doi(published)})
    base.save_json(DRAFT_STATE, state)
    receipt = {
        "status": "PUBLISH_ACCEPTED",
        "errors": [],
        "record_id": draft_id,
        "doi": base.version_doi(published),
        "concept_doi": CONCEPT_DOI,
        "file_count": EXPECTED_FINAL_FILES,
        "default_preview": DEFAULT_PREVIEW,
        "duplicate_concept_created": False,
        "second_draft_created": False,
    }
    base.save_json(
        RECEIPT_ROOT
        / f"20260729_ega_assigned_source_first_record_{draft_id}_publish_response.json",
        receipt,
    )
    return receipt


def wait_for_public(session, record_id: int) -> dict:
    headers = {"Accept": "application/vnd.inveniordm.v1+json"}
    for _ in range(120):
        response = session.get(
            f"{API}/records/{record_id}?expand=true",
            headers=headers,
            timeout=(30, 180),
        )
        if response.status_code == 200:
            record = response.json()
            if len(base.entries_map(record)) == EXPECTED_FINAL_FILES:
                return record
        time.sleep(5)
    raise RuntimeError("Published EGA successor did not stabilize")


def download_file(session, url: str, destination: Path) -> tuple[int, str, str]:
    destination.parent.mkdir(parents=True, exist_ok=True)
    sha = hashlib.sha256()
    md5 = hashlib.md5(usedforsecurity=False)
    size = 0
    with session.get(url, stream=True, timeout=(30, 300)) as response:
        base.check(response, {200})
        with destination.open("wb") as handle:
            for block in response.iter_content(4 * 1024 * 1024):
                if not block:
                    continue
                handle.write(block)
                sha.update(block)
                md5.update(block)
                size += len(block)
    return size, sha.hexdigest().upper(), md5.hexdigest().lower()


def anonymous_readback(
    record_id: int,
    expected: dict[str, dict],
    predecessor_receipt: dict,
    controls_summary: dict,
) -> tuple[dict, dict]:
    session = base.make_session()
    record = wait_for_public(session, record_id)
    if int(record["id"]) != record_id or base.concept_doi(record) != CONCEPT_DOI:
        raise RuntimeError("Public EGA successor lineage mismatch")
    assert_metadata(record["metadata"])
    if record["files"].get("default_preview") != DEFAULT_PREVIEW:
        raise RuntimeError("Public EGA default preview mismatch")
    entries = base.entries_map(record)
    if set(entries) != set(expected):
        raise RuntimeError("Public EGA outer-file set mismatch")
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

    if PUBLIC_PARTIAL.is_file():
        partial = json.loads(PUBLIC_PARTIAL.read_text(encoding="utf-8"))
        if int(partial.get("record", -1)) != record_id:
            raise RuntimeError("Stale EGA public-readback partial receipt")
        file_receipt = partial.get("files", {})
        zip_receipt = partial.get("zip_summaries", {})
    else:
        file_receipt = {}
        zip_receipt = {}

    clean_temp(READBACK_ROOT)
    READBACK_ROOT.mkdir(parents=True)
    try:
        for index, name in enumerate(
            sorted(entries, key=str.casefold), start=1
        ):
            existing = file_receipt.get(name)
            wanted = expected[name]
            if existing is not None:
                if (
                    int(existing["bytes"]),
                    existing["sha256"].upper(),
                    existing["md5"].lower(),
                ) != (
                    wanted["bytes"],
                    wanted["sha256"],
                    wanted["md5"],
                ):
                    raise RuntimeError(f"Partial EGA readback drift: {name}")
                print(
                    f"PUBLIC READBACK {index}/{len(entries)} {name} "
                    "(resume exact)",
                    flush=True,
                )
                continue
            print(
                f"PUBLIC READBACK {index}/{len(entries)} {name}",
                flush=True,
            )
            target = READBACK_ROOT / f"public-{index:02d}"
            size, sha, md5 = download_file(
                session, entries[name]["links"]["content"], target
            )
            if (size, sha, md5) != (
                wanted["bytes"],
                wanted["sha256"],
                wanted["md5"],
            ):
                raise RuntimeError(f"Public EGA readback mismatch: {name}")
            file_receipt[name] = {
                "bytes": size,
                "sha256": sha,
                "md5": md5,
                "url": entries[name]["links"]["content"],
                "match": True,
            }
            if name.lower().endswith(".zip"):
                if name == SOURCE_ZIP:
                    summary = source_zip_summary(target, include_members=True)
                    assert_source_zip(summary)
                else:
                    summary = base.inspect_zip(target, include_members=True)
                if name == CONTROLS_ZIP:
                    if (
                        summary["file_members"] != EXPECTED_CONTROL_ZIP_MEMBERS
                        or {
                            row["relative_path"]: {
                                "bytes": row["bytes"],
                                "sha256": row["sha256"],
                            }
                            for row in summary["members"]
                        }
                        != {
                            row["relative_path"]: {
                                "bytes": row["bytes"],
                                "sha256": row["sha256"],
                            }
                            for row in controls_summary["members"]
                        }
                    ):
                        raise RuntimeError("Public EGA controls ZIP mismatch")
                elif name != SOURCE_ZIP:
                    prior = predecessor_receipt["zip_summaries"].get(name)
                    if prior is None:
                        raise RuntimeError(
                            f"Retained ZIP lacks predecessor control: {name}"
                        )
                    core = {
                        key: summary[key]
                        for key in (
                            "file_members",
                            "directory_entries",
                            "all_entries",
                            "uncompressed_bytes",
                            "canonical_member_identity_sha256",
                            "crc_error",
                            "safe_paths",
                        )
                    }
                    prior_core = {
                        key: prior[key]
                        for key in (
                            "file_members",
                            "directory_entries",
                            "all_entries",
                            "uncompressed_bytes",
                            "canonical_member_identity_sha256",
                            "crc_error",
                            "safe_paths",
                        )
                    }
                    if core != prior_core:
                        raise RuntimeError(
                            f"Retained ZIP member readback changed: {name}"
                        )
                zip_receipt[name] = summary
            target.unlink()
            base.save_json(
                PUBLIC_PARTIAL,
                {
                    "status": "PARTIAL",
                    "record": record_id,
                    "files": file_receipt,
                    "zip_summaries": zip_receipt,
                },
            )
    finally:
        clean_temp(READBACK_ROOT)

    retained = set(predecessor_receipt["files"]) - OLD_SECTION11_FILES
    if (
        len(file_receipt) != EXPECTED_FINAL_FILES
        or len(retained) != EXPECTED_RETAINED_FILES
        or any(not file_receipt[name]["match"] for name in retained)
    ):
        raise RuntimeError("EGA retained-file readback did not close")
    public_receipt = {
        "status": "PASS",
        "errors": [],
        "record": record_id,
        "doi": base.version_doi(record),
        "conceptdoi": CONCEPT_DOI,
        "record_url": f"https://zenodo.org/records/{record_id}",
        "version": VERSION,
        "file_count": len(file_receipt),
        "bytes": sum(row["bytes"] for row in file_receipt.values()),
        "files": file_receipt,
        "latest_record": int(latest["id"]),
        "rdm_default_preview": record["files"].get("default_preview"),
        "rdm_file_order": record["files"].get("order", []),
        "github_commit": GITHUB_COMMIT,
        "github_package": GITHUB_PACKAGE,
        "retained_predecessor_files": EXPECTED_RETAINED_FILES,
        "removed_obsolete_files": sorted(OLD_SECTION11_FILES),
        "new_files": EXPECTED_NEW_FILES,
        "duplicate_concept_created": False,
        "second_draft_created": False,
    }
    zipped = {
        "status": "PASS",
        "errors": [],
        "record": record_id,
        "doi": base.version_doi(record),
        "zip_archive_count": len(zip_receipt),
        "archives": zip_receipt,
    }
    base.save_json(
        RECEIPT_ROOT
        / f"20260729_ega_assigned_source_first_record_{record_id}_public_readback.json",
        public_receipt,
    )
    base.save_json(
        RECEIPT_ROOT
        / f"20260729_ega_assigned_source_first_record_{record_id}_zip_member_readback.json",
        zipped,
    )
    PUBLIC_PARTIAL.unlink(missing_ok=True)
    return public_receipt, zipped


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--preflight", action="store_true")
    parser.add_argument("--readback-only", action="store_true")
    args = parser.parse_args()

    primary = verify_primary_files()
    controls = build_controls_zip()
    predecessor_receipt = load_predecessor_receipt()
    retained = retained_identities(predecessor_receipt)
    expected, local = final_expected(retained, primary, controls)
    session = base.make_session()

    if args.preflight:
        verify_live_predecessor(session, predecessor_receipt)
        print(
            json.dumps(
                {
                    "status": "PASS_PREFLIGHT",
                    "concept_doi": CONCEPT_DOI,
                    "predecessor_record": PREDECESSOR_RECORD,
                    "retained_files": len(retained),
                    "removed_obsolete_files": len(OLD_SECTION11_FILES),
                    "new_files": len(local),
                    "final_files": len(expected),
                    "default_preview": DEFAULT_PREVIEW,
                    "source_zip_members": EXPECTED_SOURCE_ZIP_MEMBERS,
                    "controls_zip_members": EXPECTED_CONTROL_ZIP_MEMBERS,
                },
                indent=2,
            ),
            flush=True,
        )
        clean_temp(CONTROLS_ROOT)
        return

    if args.readback_only:
        state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
        if not state.get("published"):
            raise RuntimeError("Tracked EGA successor is not published")
        public, zipped = anonymous_readback(
            int(state["draft_id"]),
            expected,
            predecessor_receipt,
            controls["zip_summary"],
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
        clean_temp(CONTROLS_ROOT)
        return

    predecessor = verify_live_predecessor(session, predecessor_receipt)
    token = base.find_token()
    draft_id = create_or_resume_draft(session, token, predecessor)
    stage = stage_draft(session, token, draft_id, expected, local)
    published = publish_draft(session, token, draft_id, expected)
    public, zipped = anonymous_readback(
        draft_id,
        expected,
        predecessor_receipt,
        controls["zip_summary"],
    )
    print(
        json.dumps(
            {
                "stage": stage,
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
    clean_temp(CONTROLS_ROOT)


if __name__ == "__main__":
    main()
