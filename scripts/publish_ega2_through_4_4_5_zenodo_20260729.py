#!/usr/bin/env python3
"""Publish and read back the compact EGA II same-concept successor."""

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
BASE_PATH = SCRIPT_DIR / "publish_ega0_iii_section11_source_first_zenodo_20260728.py"
SPEC = importlib.util.spec_from_file_location("ega_zenodo_base", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load the established EGA publication workflow")
base = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = base
SPEC.loader.exec_module(base)


API = base.API
CONCEPT_DOI = "10.5281/zenodo.20414353"
PREDECESSOR_RECORD = 21_677_876
PREDECESSOR_DOI = "10.5281/zenodo.21677876"
PUBLICATION_DATE = "2026-07-29"
VERSION = "2026-07-29 EGA 0, II, and III current working readers"
TITLE = (
    "Elements de geometrie algebrique (EGA): French Originals, "
    "English Working Readers, and Source Archives"
)

GITHUB_COMMIT = "2871320c39fff23e064114222f4734fa47ab6db7"
GITHUB_PACKAGE = (
    "sources/ega/checkpoints/"
    "ega2-source-aligned-through-4-4-5-working-20260729"
)

REPO_ROOT = SCRIPT_DIR.parent
EGA2_ROOT = REPO_ROOT / GITHUB_PACKAGE
EGA03_ROOT = (
    REPO_ROOT
    / "sources/ega/checkpoints/"
    "ega0-iii-and-ega3-source-first-assigned-lane-complete-20260729"
)
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
TEMP_ROOT = Path(os.environ["LOCALAPPDATA"]) / "Temp"
READBACK_ROOT = TEMP_ROOT / "ega2_through_4_4_5_zenodo_readback"
DRAFT_STATE = (
    RECEIPT_ROOT / "20260729_ega2_through_4_4_5_zenodo_draft_state.json"
)
PREDECESSOR_RECEIPT = (
    RECEIPT_ROOT
    / "20260729_ega_assigned_source_first_record_21677876_public_readback.json"
)
PREDECESSOR_ZIP_RECEIPT = (
    RECEIPT_ROOT
    / "20260729_ega_assigned_source_first_record_21677876_zip_member_readback.json"
)

OLD_EGA3_PDF = (
    "00b_EGA3_English_Working_Reader_"
    "Assigned_SourceFirst_Sections1_7_20260729.pdf"
)
OLD_EGA3_TEX = (
    "02b_EGA3_English_Working_Master_"
    "Assigned_SourceFirst_Sections1_7_20260729.tex"
)
EGA3_PDF = (
    "00c_EGA3_English_Working_Reader_"
    "Assigned_SourceFirst_Sections1_7_20260729.pdf"
)
EGA3_TEX = (
    "02c_EGA3_English_Working_Master_"
    "Assigned_SourceFirst_Sections1_7_20260729.tex"
)
EGA2_PDF = (
    "00b_EGA2_English_Layered_Working_Reader_"
    "Through_4_4_5_20260729.pdf"
)
EGA2_TEX = (
    "02b_EGA2_English_Layered_Working_Master_"
    "Through_4_4_5_20260729.tex"
)
EGA2_ZIP = (
    "10b_EGA2_English_Layered_Working_Source_"
    "Through_4_4_5_20260729.zip"
)
README_NAME = "90 EGA - README and Status.md"
SUMMARY_NAME = "91 EGA - Public Summary.json"
DEFAULT_PREVIEW = (
    "00a_EGA0_English_Working_Reader_"
    "Assigned_SourceFirst_Sections8_13_20260729.pdf"
)

REPLACED_PREDECESSOR_FILES = {
    OLD_EGA3_PDF,
    OLD_EGA3_TEX,
    README_NAME,
    SUMMARY_NAME,
}
EXPECTED_PREDECESSOR_FILES = 22
EXPECTED_RETAINED_FILES = 18
EXPECTED_LOCAL_FILES = 7
EXPECTED_FINAL_FILES = 25

LOCAL_PATHS = {
    EGA2_PDF: (
        EGA2_ROOT
        / "00a_EGA2_English_Layered_Working_Reader_"
        "Through_4_4_5_20260729.pdf"
    ),
    EGA2_TEX: (
        EGA2_ROOT
        / "02a_EGA2_English_Layered_Working_Master_"
        "Through_4_4_5_20260729.tex"
    ),
    EGA2_ZIP: (
        EGA2_ROOT
        / "10a_EGA2_English_Layered_Working_Source_"
        "Through_4_4_5_20260729.zip"
    ),
    EGA3_PDF: EGA03_ROOT / OLD_EGA3_PDF,
    EGA3_TEX: EGA03_ROOT / OLD_EGA3_TEX,
    README_NAME: REPO_ROOT / "manifests" / README_NAME,
    SUMMARY_NAME: REPO_ROOT / "manifests" / SUMMARY_NAME,
}
LOCAL_EXPECTED = {
    EGA2_PDF: (
        1_011_761,
        "C34EE831E694422ADA8824CA738B1DB7F71A3EBE07620D406853F826BC7B418C",
    ),
    EGA2_TEX: (
        1_744,
        "DCE888E004721F39C63C37A239441A7E3143CEEFB437C438E24D6ABC39EB4FAB",
    ),
    EGA2_ZIP: (
        1_188_929,
        "37E25CA7B3553FCE483E84137D683A1AB04002C4D538A7FF00271CDE6DAAC37A",
    ),
    EGA3_PDF: (
        1_284_316,
        "1C2A3F286A02EBBB521D0D4939B0604A7D8000023288F4599322EFC0FA21B886",
    ),
    EGA3_TEX: (
        3_294,
        "931DDCEBB043AC945AAA5C1D3556458E01ED547C55C02644E864918D48EA33E1",
    ),
    README_NAME: (
        1_704,
        "812D70E4CA4E3AA843B8542F8B71DB66ECB8ABBB7A95445AFFF8F9E849EB4C7A",
    ),
    SUMMARY_NAME: (
        2_871,
        "DE01E1F89D92865FA09E505361785E380D8841FA1FA67B757FEF091511FA87F5",
    ),
}

EXPECTED_EGA2_ZIP_MEMBERS = 17
EXPECTED_EGA2_ZIP_UNCOMPRESSED_BYTES = 1_756_631
EXPECTED_EGA2_ZIP_MANIFEST_ROWS = 16
EXPECTED_EGA2_ZIP_MANIFEST_SHA256 = (
    "2AC7A62C0850CE300230C6615B046E3E95B372BD921D1DADE755034D735144B9"
)

DESCRIPTION_PARAGRAPHS = [
    (
        "This same-concept successor adds the current EGA II layered English "
        "working reader, its directly visible master TeX, and one compact "
        "source ZIP. The current bounded English readers are presented in "
        "volume order: EGA 0/III, EGA II, and EGA III."
    ),
    (
        "The 151-page EGA II reader is admitted as source-aligned from its "
        "opening through Corollary 4.4.5. Its exact continuation is "
        "Proposition 4.4.6, at NUMDAM physical page 77 and printed page 80. "
        "Inherited English after that cursor remains in the layered reader "
        "for continuity, but is not admitted as source-aligned by this "
        "checkpoint."
    ),
    (
        "The EGA II reader has 528 named destinations and 1,753 valid "
        "internal GoTo actions. The 17-member source ZIP contains the master, "
        "preambles, bibliography, eight chapter components, reader PDF, and "
        "an exact internal identity manifest."
    ),
    (
        "The NUMDAM French reference volumes remain available on this record. "
        "The English source lineage includes the public ryankeleti/ega "
        "project and later source-aligned continuation work. This record "
        "remains on the separate EGA concept DOI while belonging to the same "
        "broader archive framework as the SGA materials."
    ),
    (
        "These are scholarly working readers, not critical editions, "
        "peer-review certifications, rights determinations, whole-corpus "
        "completion claims, or tagged-PDF accessibility remediation. No new "
        "blanket license or transfer of underlying rights is asserted."
    ),
]
DESCRIPTION_HTML = "\n".join(
    f"<p>{paragraph}</p>" for paragraph in DESCRIPTION_PARAGRAPHS
)
NOTES_HTML = (
    "<p>Direct readers are ordered EGA 0/III, EGA II, and EGA III, followed "
    "by directly visible master TeX files and grouped source archives. The "
    "preferred preview remains the EGA 0/III reader. Immutable predecessor "
    "versions preserve earlier bounded releases.</p>"
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


def inspect_ega2_zip(path: Path, *, include_members: bool) -> dict:
    summary = base.inspect_zip(path, include_members=include_members)
    with zipfile.ZipFile(path) as archive:
        names = {
            item.filename for item in archive.infolist() if not item.is_dir()
        }
        if "SHA256SUMS.csv" not in names:
            raise RuntimeError("EGA II source ZIP lacks SHA256SUMS.csv")
        manifest_data = archive.read("SHA256SUMS.csv")
        rows = list(
            csv.DictReader(
                io.StringIO(manifest_data.decode("utf-8-sig"), newline="")
            )
        )
        errors = []
        for row in rows:
            member = row["relative_path"]
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
            "bytes": len(manifest_data),
            "sha256": hashlib.sha256(manifest_data).hexdigest().upper(),
            "errors": errors,
        }
    return summary


def assert_ega2_zip(summary: dict) -> None:
    manifest = summary["internal_manifest"]
    if (
        summary["file_members"] != EXPECTED_EGA2_ZIP_MEMBERS
        or summary["directory_entries"] != 0
        or summary["all_entries"] != EXPECTED_EGA2_ZIP_MEMBERS
        or summary["uncompressed_bytes"] != EXPECTED_EGA2_ZIP_UNCOMPRESSED_BYTES
        or not summary["safe_paths"]
        or summary["crc_error"] is not None
        or manifest["rows"] != EXPECTED_EGA2_ZIP_MANIFEST_ROWS
        or manifest["sha256"] != EXPECTED_EGA2_ZIP_MANIFEST_SHA256
        or manifest["errors"]
    ):
        raise RuntimeError("EGA II source ZIP closure mismatch")


def github_readback() -> None:
    session = base.make_session()
    root = (
        "https://raw.githubusercontent.com/"
        f"KokunoYumeto/modern-latex-manuscripts/{GITHUB_COMMIT}/"
        f"{GITHUB_PACKAGE}/"
    )
    for path in sorted(EGA2_ROOT.iterdir(), key=lambda value: value.name.casefold()):
        if not path.is_file():
            continue
        response = base.check(
            session.get(root + quote(path.name), timeout=(30, 180)),
            {200},
        )
        data = response.content
        if (
            len(data),
            hashlib.sha256(data).hexdigest().upper(),
        ) != (
            path.stat().st_size,
            base.sha256_file(path),
        ):
            raise RuntimeError(f"GitHub EGA II readback mismatch: {path.name}")


def verify_local_files() -> dict[str, dict]:
    result = {}
    for name, path in LOCAL_PATHS.items():
        if not path.is_file():
            raise FileNotFoundError(path)
        row = identity(path)
        if (row["bytes"], row["sha256"]) != LOCAL_EXPECTED[name]:
            raise RuntimeError(f"Local EGA successor identity mismatch: {name}")
        result[name] = row

    validation = json.loads(
        (EGA2_ROOT / "PACKAGE_VALIDATION.json").read_text(encoding="utf-8")
    )
    if (
        validation.get("status") != "PASS"
        or validation.get("errors") != []
        or validation.get("source_zip", {}).get("member_readback") != "PASS"
    ):
        raise RuntimeError("EGA II package validation is not PASS")
    assert_ega2_zip(inspect_ega2_zip(LOCAL_PATHS[EGA2_ZIP], include_members=False))

    forbidden = (
        "machine-assisted",
        "chatgpt",
        "claude",
        "codex",
        "large language model",
    )
    for name in (README_NAME, SUMMARY_NAME):
        text = LOCAL_PATHS[name].read_text(encoding="utf-8").casefold()
        hits = [term for term in forbidden if term in text]
        if hits:
            raise RuntimeError(f"Reader-facing EGA summary terms: {name}: {hits}")
    github_readback()
    return result


def load_predecessor() -> tuple[dict, dict]:
    if not PREDECESSOR_RECEIPT.is_file() or not PREDECESSOR_ZIP_RECEIPT.is_file():
        raise RuntimeError("Missing controlling EGA predecessor receipts")
    receipt = json.loads(PREDECESSOR_RECEIPT.read_text(encoding="utf-8"))
    zipped = json.loads(PREDECESSOR_ZIP_RECEIPT.read_text(encoding="utf-8"))
    if (
        receipt.get("status") != "PASS"
        or int(receipt.get("record", -1)) != PREDECESSOR_RECORD
        or receipt.get("doi") != PREDECESSOR_DOI
        or receipt.get("conceptdoi") != CONCEPT_DOI
        or len(receipt.get("files", {})) != EXPECTED_PREDECESSOR_FILES
        or zipped.get("status") != "PASS"
        or int(zipped.get("record", -1)) != PREDECESSOR_RECORD
    ):
        raise RuntimeError("EGA predecessor receipt is not controlling")
    return receipt, zipped


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
    record = base.check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}?expand=true",
            headers=headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    entries = base.entries_map(record)
    if (
        int(record["id"]) != PREDECESSOR_RECORD
        or base.concept_doi(record) != CONCEPT_DOI
        or base.version_doi(record) != PREDECESSOR_DOI
        or set(entries) != set(receipt["files"])
    ):
        raise RuntimeError("Live EGA predecessor identity changed")
    for name, row in receipt["files"].items():
        if (
            int(entries[name]["size"]),
            base.normalize_checksum(entries[name]["checksum"]),
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
    if int(latest["id"]) != PREDECESSOR_RECORD:
        raise RuntimeError("EGA concept head moved; refusing parallel successor")
    return record


def expected_files(
    predecessor_receipt: dict,
    local: dict[str, dict],
) -> tuple[dict[str, dict], dict[str, dict]]:
    predecessor = receipt_identities(predecessor_receipt)
    retained = {
        name: row
        for name, row in predecessor.items()
        if name not in REPLACED_PREDECESSOR_FILES
    }
    if len(retained) != EXPECTED_RETAINED_FILES:
        raise RuntimeError("Unexpected retained EGA predecessor boundary")
    if (
        predecessor[OLD_EGA3_PDF]["sha256"] != local[EGA3_PDF]["sha256"]
        or predecessor[OLD_EGA3_TEX]["sha256"] != local[EGA3_TEX]["sha256"]
    ):
        raise RuntimeError("Renamed EGA III files are not byte-identical")
    if set(retained) & set(local):
        raise RuntimeError("New EGA filenames collide with retained files")
    expected = {**retained, **local}
    if len(local) != EXPECTED_LOCAL_FILES or len(expected) != EXPECTED_FINAL_FILES:
        raise RuntimeError("Unexpected final EGA file boundary")
    return expected, retained


def create_or_resume_draft(session, token: str, predecessor: dict) -> int:
    auth = {"Authorization": f"Bearer {token}"}
    vendor = {**auth, "Accept": "application/vnd.inveniordm.v1+json"}
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
        if (
            int(draft["id"]) != int(state["draft_id"])
            or int(state["predecessor_record"]) != PREDECESSOR_RECORD
            or base.concept_doi(draft) != CONCEPT_DOI
        ):
            raise RuntimeError("Existing EGA draft is not the tracked draft")
        return int(draft["id"])
    base.check(existing, {404})

    if DRAFT_STATE.is_file():
        state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
        if state.get("published"):
            raise RuntimeError("Tracked EGA successor is already published")
        tracked = session.get(
            f"{API}/records/{int(state['draft_id'])}/draft",
            headers=vendor,
            timeout=(30, 180),
        )
        if tracked.status_code == 200:
            return int(state["draft_id"])
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
        or set(base.legacy_file_map(draft)) != set(base.entries_map(predecessor))
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
    if not extras.issubset(REPLACED_PREDECESSOR_FILES):
        raise RuntimeError(f"Unexpected inherited EGA files: {sorted(extras)}")
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
        actions.append({"filename": name, "action": "removed_replaced_surface"})

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
        current = files.get(name)
        if current is not None:
            observed = (
                int(current["filesize"]),
                base.normalize_checksum(current["checksum"]),
            )
            if observed == (wanted["bytes"], wanted["md5"]):
                actions.append({"filename": name, "action": "already_exact"})
                continue
            base.check(
                session.delete(
                    current["links"]["self"],
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
        if (
            int(final_files[name]["filesize"]),
            base.normalize_checksum(final_files[name]["checksum"]),
        ) != (
            wanted["bytes"],
            wanted["md5"],
        ):
            raise RuntimeError(f"Staged EGA identity mismatch: {name}")
    receipt = {
        "status": "PASS_STAGED",
        "errors": [],
        "predecessor_record": PREDECESSOR_RECORD,
        "draft_id": draft_id,
        "concept_doi": CONCEPT_DOI,
        "file_count": len(final_files),
        "retained_predecessor_files": EXPECTED_RETAINED_FILES,
        "replaced_predecessor_files": sorted(REPLACED_PREDECESSOR_FILES),
        "new_or_renamed_files": EXPECTED_LOCAL_FILES,
        "actions": actions,
        "duplicate_concept_created": False,
        "second_draft_created": False,
    }
    base.save_json(
        RECEIPT_ROOT
        / f"20260729_ega2_through_4_4_5_record_{draft_id}_draft_files.json",
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
    text = json.dumps(metadata, ensure_ascii=True).casefold()
    for term in ("machine-assisted", "chatgpt", "claude", "codex"):
        if term in text:
            raise RuntimeError(f"Reader-facing EGA metadata contains {term}")


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
    files = base.check(
        session.get(draft["links"]["files"], headers=headers, timeout=(30, 180)),
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
        DEFAULT_PREVIEW,
        EGA2_PDF,
        EGA3_PDF,
        "00 EGA - English Translation Working Draft.pdf",
        "01 EGA IV - English Translation Working Draft (Sections 1-21).pdf",
        (
            "02a_EGA0_English_Working_Master_"
            "Assigned_SourceFirst_Sections8_13_20260729.tex"
        ),
        EGA2_TEX,
        EGA3_TEX,
        "10a_EGA0_III_and_EGA3_Assigned_Lane_Source_20260729.zip",
        EGA2_ZIP,
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
    if int(published["id"]) != draft_id or base.concept_doi(published) != CONCEPT_DOI:
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
        / f"20260729_ega2_through_4_4_5_record_{draft_id}_publish_response.json",
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
    with session.get(url, stream=True, timeout=(30, 600)) as response:
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
    retained: dict[str, dict],
    predecessor_zip_receipt: dict,
) -> tuple[dict, dict]:
    session = base.make_session()
    record = wait_for_public(session, record_id)
    if int(record["id"]) != record_id or base.concept_doi(record) != CONCEPT_DOI:
        raise RuntimeError("Public EGA successor lineage mismatch")
    assert_metadata(record["metadata"])
    if record["files"].get("default_preview") != DEFAULT_PREVIEW:
        raise RuntimeError("Public EGA default preview mismatch")
    if record["files"].get("order", []) != ordered_names(expected):
        raise RuntimeError("Public EGA file order mismatch")
    entries = base.entries_map(record)
    if set(entries) != set(expected):
        raise RuntimeError("Public EGA outer-file set mismatch")
    for name, wanted in expected.items():
        if (
            int(entries[name]["size"]),
            base.normalize_checksum(entries[name]["checksum"]),
        ) != (
            wanted["bytes"],
            wanted["md5"],
        ):
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

    clean_temp(READBACK_ROOT)
    READBACK_ROOT.mkdir(parents=True)
    files = {}
    zip_summaries = copy.deepcopy(predecessor_zip_receipt["archives"])
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
            size, sha, md5 = download_file(
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
            if name == EGA2_ZIP:
                summary = inspect_ega2_zip(target, include_members=True)
                assert_ega2_zip(summary)
                zip_summaries[name] = summary
            target.unlink()
    finally:
        clean_temp(READBACK_ROOT)

    if (
        len(files) != EXPECTED_FINAL_FILES
        or len(retained) != EXPECTED_RETAINED_FILES
        or len(zip_summaries) != predecessor_zip_receipt["zip_archive_count"] + 1
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
        "rdm_file_order": record["files"].get("order", []),
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
        RECEIPT_ROOT
        / f"20260729_ega2_through_4_4_5_record_{record_id}_public_readback.json",
        public,
    )
    base.save_json(
        RECEIPT_ROOT
        / f"20260729_ega2_through_4_4_5_record_{record_id}_zip_member_readback.json",
        zipped,
    )
    return public, zipped


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--preflight", action="store_true")
    parser.add_argument("--readback-only", action="store_true")
    args = parser.parse_args()

    local = verify_local_files()
    predecessor_receipt, predecessor_zip_receipt = load_predecessor()
    expected, retained = expected_files(predecessor_receipt, local)
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
                    "replaced_files": len(REPLACED_PREDECESSOR_FILES),
                    "new_or_renamed_files": len(local),
                    "final_files": len(expected),
                    "default_preview": DEFAULT_PREVIEW,
                    "ega2_zip_members": EXPECTED_EGA2_ZIP_MEMBERS,
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

    predecessor = verify_live_predecessor(session, predecessor_receipt)
    token = base.find_token()
    draft_id = create_or_resume_draft(session, token, predecessor)
    staged = stage_draft(session, token, draft_id, expected, local)
    published = publish_draft(session, token, draft_id, expected)
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
