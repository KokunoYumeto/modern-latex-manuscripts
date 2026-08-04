#!/usr/bin/env python3
"""Correct one FAC landing-page attribution without changing record files.

The current record's own public ``05_READ_ME_FIRST.md`` names Piotr Achinger
and Łukasz Krupa.  The landing description accidentally says Marcin Krupa.
This tool opens an edit draft for the already-published record, changes only
that exact description token, republishes the same record/revision lineage,
and anonymously replays every public file against the prior SHA-256 receipt.
It cannot create a concept or a new version.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import time
from pathlib import Path

import publish_fac_reference_v2_r4_zenodo_20260804 as fac


base = fac.base
API = fac.API
RECORD_ID = 21783868
VERSION_DOI = "10.5281/zenodo.21783868"
CONCEPT_ID = "21720996"
CONCEPT_DOI = "10.5281/zenodo.21720996"
VERSION_INDEX = 6
EXPECTED_FILES = 50
EXPECTED_BYTES = 14_827_551
DEFAULT_PREVIEW = "00_FAC_Blind_Comparison_Readable_Report.pdf"
WRONG_ATTRIBUTION = "Piotr Achinger and Marcin Krupa"
RIGHT_ATTRIBUTION = "Piotr Achinger and Łukasz Krupa"
AUTHORITY_FILENAME = "05_READ_ME_FIRST.md"

REPO_ROOT = Path(__file__).resolve().parents[1]
PRIOR_RECEIPT = (
    REPO_ROOT
    / "manifests"
    / "published-zenodo"
    / "20260804_fac_reference_v2_r4_record_21783868_public_readback.json"
)
STATE_PATH = (
    REPO_ROOT
    / "manifests"
    / "zenodo-active-custody"
    / "fac-21783868-attribution-correction-20260804"
    / "state.json"
)
RECEIPT_PATH = (
    REPO_ROOT
    / "manifests"
    / "published-zenodo"
    / "20260804_fac_record_21783868_attribution_metadata_correction.json"
)


def canonical_sha256(value: object) -> str:
    data = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(data).hexdigest().upper()


def save(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    temporary.replace(path)


def state() -> dict | None:
    if not STATE_PATH.is_file():
        return None
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))


def public_record(session) -> dict:
    return base.check(
        session.get(
            f"{API}/records/{RECORD_ID}",
            headers=fac.MODERN,
            timeout=(30, 300),
        ),
        {200},
    ).json()


def record_boundary(record: dict) -> None:
    entries = fac.modern_entries(record)
    if (
        int(record.get("id", 0)) != RECORD_ID
        or record.get("pids", {}).get("doi", {}).get("identifier") != VERSION_DOI
        or record.get("parent", {}).get("id") != CONCEPT_ID
        or record.get("parent", {}).get("pids", {}).get("doi", {}).get("identifier")
        != CONCEPT_DOI
        or int(record.get("versions", {}).get("index", 0)) != VERSION_INDEX
        or len(entries) != EXPECTED_FILES
        or sum(int(row["size"]) for row in entries.values()) != EXPECTED_BYTES
        or record.get("files", {}).get("default_preview") != DEFAULT_PREVIEW
    ):
        raise RuntimeError("FAC record/concept/version/file boundary changed")


def file_api_identities(record: dict) -> dict[str, dict]:
    return {
        name: {
            "bytes": int(row["size"]),
            "md5": fac.normalized_md5(row["checksum"]),
        }
        for name, row in fac.modern_entries(record).items()
    }


def prior_readback() -> tuple[dict, dict[str, dict]]:
    receipt = json.loads(PRIOR_RECEIPT.read_text(encoding="utf-8"))
    rows = {
        row["filename"]: {
            "bytes": int(row["bytes"]),
            "sha256": row["sha256"].upper(),
        }
        for row in receipt.get("readback", [])
        if row.get("match") is True
    }
    if (
        receipt.get("status")
        != "PASS_PUBLISHED_FAC_R4_SAME_CONCEPT_AND_ANONYMOUS_RAW_READBACK"
        or int(receipt.get("record_id", 0)) != RECORD_ID
        or receipt.get("version_doi") != VERSION_DOI
        or receipt.get("concept_doi") != CONCEPT_DOI
        or int(receipt.get("files", 0)) != EXPECTED_FILES
        or int(receipt.get("bytes", 0)) != EXPECTED_BYTES
        or int(receipt.get("raw_readback_mismatches", -1)) != 0
        or len(rows) != EXPECTED_FILES
    ):
        raise RuntimeError("Prior FAC publication/readback receipt boundary changed")
    return receipt, rows


def authority_surface(session, record: dict) -> dict:
    entry = fac.modern_entries(record)[AUTHORITY_FILENAME]
    response = base.check(
        session.get(entry["links"]["content"], timeout=(30, 300)),
        {200},
    )
    data = response.content
    text = data.decode("utf-8")
    if text.count(RIGHT_ATTRIBUTION) != 1 or WRONG_ATTRIBUTION in text:
        raise RuntimeError("FAC public authority surface does not prove the correction")
    return {
        "filename": AUTHORITY_FILENAME,
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest().upper(),
        "right_attribution_occurrences": 1,
        "wrong_attribution_occurrences": 0,
        "content_url": entry["links"]["content"],
    }


def draft_probe(session, token: str):
    return session.get(
        f"{API}/records/{RECORD_ID}/draft",
        headers=fac.auth_modern(token),
        timeout=(30, 300),
    )


def preflight(session, token: str) -> dict:
    record = public_record(session)
    record_boundary(record)
    receipt, rows = prior_readback()
    authority = authority_surface(session, record)
    description = record["metadata"]["description"]
    probe = draft_probe(session, token)
    active_draft = probe.status_code == 200
    if probe.status_code not in {200, 404, 410}:
        base.check(probe, {200, 404, 410})
    tracked = state()
    if active_draft and (
        tracked is None
        or tracked.get("published") is True
        or int(tracked.get("record_id", 0)) != RECORD_ID
    ):
        raise RuntimeError("Untracked FAC edit draft exists")
    if (
        description.count(WRONG_ATTRIBUTION) != 1
        or RIGHT_ATTRIBUTION in description
    ):
        if (
            description.count(RIGHT_ATTRIBUTION) == 1
            and WRONG_ATTRIBUTION not in description
            and not active_draft
        ):
            return {
                "status": "ALREADY_CORRECT_ON_SAME_RECORD",
                "record_id": RECORD_ID,
                "version_doi": VERSION_DOI,
                "concept_doi": CONCEPT_DOI,
                "files": len(rows),
                "authority_surface": authority,
                "prior_receipt_sha256": fac.sha256(PRIOR_RECEIPT),
            }
        raise RuntimeError("FAC public description attribution boundary changed")
    return {
        "status": "PASS_READY_FOR_SAME_RECORD_METADATA_CORRECTION",
        "record_id": RECORD_ID,
        "version_doi": VERSION_DOI,
        "concept_doi": CONCEPT_DOI,
        "version_index": VERSION_INDEX,
        "files": EXPECTED_FILES,
        "bytes": EXPECTED_BYTES,
        "active_tracked_edit_draft": active_draft,
        "authority_surface": authority,
        "prior_receipt_sha256": fac.sha256(PRIOR_RECEIPT),
        "prior_zip_replays": {
            name: {
                "members": value["members"],
                "match": value["match"],
            }
            for name, value in receipt.get("zip_replays", {}).items()
        },
    }


def create_or_resume_edit(session, token: str, record: dict) -> dict:
    tracked = state()
    probe = draft_probe(session, token)
    if probe.status_code == 200:
        if (
            tracked is None
            or tracked.get("published") is True
            or int(tracked.get("record_id", 0)) != RECORD_ID
        ):
            raise RuntimeError("Untracked FAC edit draft exists")
        return probe.json()
    base.check(probe, {404, 410})
    if tracked is not None and tracked.get("published") is not True:
        raise RuntimeError("Tracked FAC edit state exists but the draft disappeared")
    created = base.check(
        session.post(
            f"{API}/records/{RECORD_ID}/draft",
            headers=fac.auth_modern(token),
            timeout=(30, 300),
        ),
        {201},
    ).json()
    save(
        STATE_PATH,
        {
            "schema": "fac_same_record_attribution_correction_state_v1",
            "status": "EDIT_DRAFT_CREATED",
            "record_id": RECORD_ID,
            "version_doi": VERSION_DOI,
            "concept_id": CONCEPT_ID,
            "concept_doi": CONCEPT_DOI,
            "version_index": VERSION_INDEX,
            "published": False,
            "before_revision_id": int(record["revision_id"]),
            "before_metadata_sha256": canonical_sha256(record["metadata"]),
            "created_at_epoch": int(time.time()),
        },
    )
    return created


def verify_edit_draft(draft: dict, before_files: dict[str, dict]) -> None:
    if (
        int(draft.get("id", 0)) != RECORD_ID
        or draft.get("is_published") is not True
        or draft.get("parent", {}).get("id") != CONCEPT_ID
        or int(draft.get("versions", {}).get("index", 0)) != VERSION_INDEX
        or draft.get("versions", {}).get("is_latest_draft") is not True
        or file_api_identities(draft) != before_files
        or draft.get("files", {}).get("default_preview") != DEFAULT_PREVIEW
    ):
        raise RuntimeError("FAC edit draft changed lineage, files, or preview")


def apply_correction(session, token: str, confirmation: str) -> dict:
    if confirmation != str(RECORD_ID):
        raise RuntimeError(f"Correction requires --confirm-record {RECORD_ID}")
    pre = preflight(session, token)
    if pre["status"] == "ALREADY_CORRECT_ON_SAME_RECORD":
        if RECEIPT_PATH.is_file():
            return json.loads(RECEIPT_PATH.read_text(encoding="utf-8"))
        return pre
    before = public_record(session)
    record_boundary(before)
    before_files = file_api_identities(before)
    draft = create_or_resume_edit(session, token, before)
    verify_edit_draft(draft, before_files)

    metadata = copy.deepcopy(draft["metadata"])
    old_description = metadata["description"]
    if old_description.count(WRONG_ATTRIBUTION) != 1 or RIGHT_ATTRIBUTION in old_description:
        raise RuntimeError("FAC edit draft description boundary changed")
    metadata["description"] = old_description.replace(
        WRONG_ATTRIBUTION,
        RIGHT_ATTRIBUTION,
        1,
    )
    payload = {
        "access": draft["access"],
        "files": {
            "enabled": True,
            "default_preview": DEFAULT_PREVIEW,
            "order": draft.get("files", {}).get("order") or [],
        },
        "metadata": metadata,
        "custom_fields": draft.get("custom_fields", {}),
    }
    if draft.get("pids"):
        payload["pids"] = draft["pids"]
    patched = base.check(
        session.put(
            f"{API}/records/{RECORD_ID}/draft",
            headers={
                **fac.auth_modern(token),
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=(30, 300),
        ),
        {200},
    ).json()
    verify_edit_draft(patched, before_files)
    if (
        patched["metadata"]["description"] != metadata["description"]
        or patched["metadata"]["description"].count(RIGHT_ATTRIBUTION) != 1
        or WRONG_ATTRIBUTION in patched["metadata"]["description"]
    ):
        raise RuntimeError("FAC edit draft did not stage the exact attribution correction")
    tracked = state()
    if tracked is None or int(tracked.get("record_id", 0)) != RECORD_ID:
        raise RuntimeError("FAC edit-draft custody state disappeared")
    tracked.update(
        {
            "status": "STAGED_EXACT_METADATA_ONLY_CORRECTION",
            "staged": True,
            "staged_at_epoch": int(time.time()),
            "staged_metadata_sha256": canonical_sha256(patched["metadata"]),
            "files_unchanged": len(before_files),
        }
    )
    save(STATE_PATH, tracked)

    published = base.check(
        session.post(
            patched["links"]["publish"],
            headers=fac.auth_modern(token),
            timeout=(30, 600),
        ),
        {200, 202},
    ).json()
    if int(published.get("id", 0)) != RECORD_ID:
        raise RuntimeError("FAC metadata edit unexpectedly changed the record identity")

    deadline = time.time() + 180
    after = None
    while time.time() < deadline:
        candidate = public_record(session)
        if (
            candidate["metadata"]["description"].count(RIGHT_ATTRIBUTION) == 1
            and WRONG_ATTRIBUTION not in candidate["metadata"]["description"]
        ):
            after = candidate
            break
        time.sleep(2)
    if after is None:
        raise RuntimeError("FAC corrected public metadata did not become readable")
    record_boundary(after)
    if file_api_identities(after) != before_files:
        raise RuntimeError("FAC file identities changed during metadata-only correction")
    active = draft_probe(session, token)
    if active.status_code not in {404, 410}:
        raise RuntimeError("FAC edit draft remains after publication")

    _, expected_readback = prior_readback()
    anonymous = base.make_session()
    readback = []
    errors = []
    for index, (name, row) in enumerate(fac.modern_entries(after).items(), start=1):
        print(f"READBACK {index}/{EXPECTED_FILES} {name}", flush=True)
        observed = fac.stream_identity(anonymous, row["links"]["content"])
        expected = expected_readback[name]
        match = observed == (expected["bytes"], expected["sha256"])
        if not match:
            errors.append(name)
        readback.append(
            {
                "filename": name,
                "bytes": observed[0],
                "sha256": observed[1],
                "match": match,
                "content_url": row["links"]["content"],
            }
        )
    if errors:
        raise RuntimeError(f"FAC metadata-correction raw readback mismatches: {errors}")

    receipt, _ = prior_readback()
    result = {
        "schema": "fac_same_record_attribution_metadata_correction_receipt_v1",
        "status": "PASS_CORRECTED_SAME_RECORD_METADATA_AND_ANONYMOUS_RAW_READBACK",
        "errors": [],
        "record_id": RECORD_ID,
        "record_url": after["links"]["self_html"],
        "version_doi": VERSION_DOI,
        "concept_id": CONCEPT_ID,
        "concept_doi": CONCEPT_DOI,
        "version_index": VERSION_INDEX,
        "before_revision_id": int(before["revision_id"]),
        "after_revision_id": int(after["revision_id"]),
        "before_metadata_sha256": canonical_sha256(before["metadata"]),
        "after_metadata_sha256": canonical_sha256(after["metadata"]),
        "metadata_field_changed": "description",
        "wrong_attribution": WRONG_ATTRIBUTION,
        "corrected_attribution": RIGHT_ATTRIBUTION,
        "wrong_attribution_public_occurrences_after": 0,
        "corrected_attribution_public_occurrences_after": 1,
        "authority_surface": pre["authority_surface"],
        "files": EXPECTED_FILES,
        "bytes": EXPECTED_BYTES,
        "default_preview": DEFAULT_PREVIEW,
        "file_api_identity_matches": EXPECTED_FILES,
        "file_api_identity_mismatches": 0,
        "anonymous_raw_readback_matches": EXPECTED_FILES,
        "anonymous_raw_readback_mismatches": 0,
        "readback": readback,
        "zip_member_replay_inherited_by_byte_identity": {
            name: {
                "members": value["members"],
                "match": value["match"],
            }
            for name, value in receipt.get("zip_replays", {}).items()
        },
        "prior_publication_receipt": {
            "relative_path": PRIOR_RECEIPT.relative_to(REPO_ROOT).as_posix(),
            "bytes": PRIOR_RECEIPT.stat().st_size,
            "sha256": fac.sha256(PRIOR_RECEIPT),
        },
        "active_draft": False,
        "same_record": True,
        "new_version_created": False,
        "duplicate_concept_created": False,
        "fac_files_mutated": False,
        "gaga_mutated": False,
    }
    save(RECEIPT_PATH, result)
    tracked.update(
        {
            "status": "PASS_PUBLISHED_SAME_RECORD_AND_READ_BACK",
            "published": True,
            "completed_at_epoch": int(time.time()),
            "after_revision_id": int(after["revision_id"]),
            "receipt_relative_path": RECEIPT_PATH.relative_to(REPO_ROOT).as_posix(),
            "receipt_bytes": RECEIPT_PATH.stat().st_size,
            "receipt_sha256": fac.sha256(RECEIPT_PATH),
        }
    )
    save(STATE_PATH, tracked)
    result["receipt_relative_path"] = RECEIPT_PATH.relative_to(REPO_ROOT).as_posix()
    result["receipt_bytes"] = RECEIPT_PATH.stat().st_size
    result["receipt_sha256"] = fac.sha256(RECEIPT_PATH)
    result["state_relative_path"] = STATE_PATH.relative_to(REPO_ROOT).as_posix()
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=("preflight", "apply"))
    parser.add_argument("--confirm-record")
    args = parser.parse_args()
    session = base.make_session()
    token = base.find_token()
    if args.action == "preflight":
        result = preflight(session, token)
    else:
        result = apply_correction(session, token, args.confirm_record or "")
    summary = {
        key: value
        for key, value in result.items()
        if key not in {"readback", "zip_member_replay_inherited_by_byte_identity"}
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
