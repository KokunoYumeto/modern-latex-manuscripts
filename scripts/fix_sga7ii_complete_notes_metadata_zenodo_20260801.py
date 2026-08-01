#!/usr/bin/env python3
"""Remove the duplicated notes paragraph from SGA record 21747165 in place."""

from __future__ import annotations

import copy
import hashlib
import time
from pathlib import Path

import publish_current_reader_bundles_zenodo_20260730 as base


API = base.API
RECORD_ID = 21_747_165
DOI = "10.5281/zenodo.21747165"
CONCEPT_DOI = "10.5281/zenodo.20410947"
EXPECTED_FILES = 85
EXPECTED_BYTES = 684_224_664
DEFAULT_PREVIEW = "00a_SGA1_English_Reader.pdf"
DESCRIPTION_SHA256 = (
    "2E0152CAC9B6111A24FDA37C69A40EDB7A7869655502458E38B5DE72448910D6"
)
NOTE = (
    "<p>Reader PDFs contain mathematical text rather than project-status "
    "prefaces. Buildable source, provenance, and release controls are separate "
    "downloads.</p>"
)
DUPLICATED_NOTE_SHA256 = (
    "44035EB96AFD791144F6DD92B403396CC598429762EEED1F40B4C7F5AD35E684"
)
REPO_ROOT = Path(__file__).resolve().parents[1]
RECEIPT = (
    REPO_ROOT
    / "manifests/published-zenodo/"
    "20260801_sga_record_21747165_notes_deduplication.json"
)


def public_headers() -> dict[str, str]:
    return {"Accept": "application/vnd.inveniordm.v1+json"}


def auth_headers(token: str) -> dict[str, str]:
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.inveniordm.v1+json",
    }


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest().upper()


def snapshot(record: dict) -> dict[str, dict[str, object]]:
    return {
        name: {
            "bytes": int(entry["size"]),
            "md5": base.normalized_md5(entry["checksum"]),
        }
        for name, entry in sorted(
            base.modern_entries(record).items(), key=lambda row: row[0].casefold()
        )
    }


def fetch_public(session) -> dict:
    return base.check(
        session.get(
            f"{API}/records/{RECORD_ID}?expand=true",
            headers=public_headers(),
            timeout=(30, 180),
        ),
        {200},
    ).json()


def validate_boundary(record: dict) -> dict[str, dict[str, object]]:
    files = snapshot(record)
    if (
        int(record["id"]) != RECORD_ID
        or record["pids"]["doi"]["identifier"] != DOI
        or record["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI
        or not record.get("is_published")
        or not record["versions"].get("is_latest")
        or len(files) != EXPECTED_FILES
        or sum(int(row["bytes"]) for row in files.values()) != EXPECTED_BYTES
        or record["files"].get("default_preview") != DEFAULT_PREVIEW
        or sha256_text(record["metadata"].get("description", ""))
        != DESCRIPTION_SHA256
    ):
        raise RuntimeError("Live SGA record boundary changed")
    return files


def notes(metadata: dict) -> list[dict]:
    return [
        row
        for row in metadata.get("additional_descriptions", [])
        if row.get("type", {}).get("id") == "notes"
    ]


def validate_fixed(metadata: dict) -> None:
    rows = notes(metadata)
    if len(rows) != 1 or rows[0].get("description") != NOTE:
        raise RuntimeError("SGA notes deduplication did not persist")


def draft_status(session, token: str) -> int:
    response = session.get(
        f"{API}/records/{RECORD_ID}/draft",
        headers=auth_headers(token),
        timeout=(30, 60),
    )
    if response.status_code == 404:
        return 404
    base.check(response, {200})
    return 200


def assert_latest(session) -> None:
    latest = base.check(
        session.get(
            f"{API}/records/{RECORD_ID}/versions/latest?expand=true",
            headers=public_headers(),
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if int(latest["id"]) != RECORD_ID:
        raise RuntimeError("SGA concept head moved")


def save_receipt(before: dict, after: dict, status: str) -> None:
    before_files = validate_boundary(before)
    after_files = validate_boundary(after)
    validate_fixed(after["metadata"])
    if before_files != after_files:
        raise RuntimeError("SGA file identities changed during notes edit")
    base.save_json(
        RECEIPT,
        {
            "status": status,
            "errors": [],
            "action": "in_place_notes_deduplication_only",
            "record": RECORD_ID,
            "doi": DOI,
            "concept_doi": CONCEPT_DOI,
            "public_url": f"https://zenodo.org/records/{RECORD_ID}",
            "new_record_created": False,
            "new_version_created": False,
            "duplicate_concept_created": False,
            "file_count": len(after_files),
            "bytes": sum(int(row["bytes"]) for row in after_files.values()),
            "default_preview": after["files"]["default_preview"],
            "file_identities_unchanged": True,
            "revision_before": before.get("revision_id"),
            "revision_after": after.get("revision_id"),
            "description_unchanged": True,
            "notes_before_sha256": sha256_text(notes(before["metadata"])[0]["description"]),
            "notes_after_sha256": sha256_text(NOTE),
            "notes_rows_after": 1,
            "anonymous_metadata_readback": True,
            "active_edit_draft_remaining": False,
        },
    )


def main() -> None:
    session = base.make_session()
    token = base.find_token()
    before = fetch_public(session)
    before_files = validate_boundary(before)
    assert_latest(session)
    current = notes(before["metadata"])
    if len(current) == 1 and current[0].get("description") == NOTE:
        if draft_status(session, token) != 404:
            raise RuntimeError("Unexpected active SGA edit draft")
        save_receipt(before, before, "PASS_ALREADY_APPLIED")
        print(RECEIPT.read_text(encoding="utf-8"))
        return
    if (
        len(current) != 1
        or sha256_text(current[0].get("description", ""))
        != DUPLICATED_NOTE_SHA256
    ):
        raise RuntimeError("Unexpected SGA notes boundary before edit")
    if draft_status(session, token) != 404:
        raise RuntimeError("An active SGA edit draft already exists")

    created = False
    try:
        draft = base.check(
            session.post(
                f"{API}/records/{RECORD_ID}/draft",
                headers=auth_headers(token),
                timeout=(30, 180),
            ),
            {201},
        ).json()
        created = True
        if int(draft["id"]) != RECORD_ID or snapshot(draft) != before_files:
            raise RuntimeError("SGA edit draft did not inherit exactly")
        metadata = copy.deepcopy(draft["metadata"])
        row = copy.deepcopy(notes(metadata)[0])
        row["description"] = NOTE
        metadata["additional_descriptions"] = [row]
        validate_fixed(metadata)
        payload = {
            "access": draft["access"],
            "files": {
                "enabled": True,
                "default_preview": DEFAULT_PREVIEW,
                "order": draft["files"].get("order", []),
            },
            "metadata": metadata,
            "custom_fields": draft.get("custom_fields", {}),
        }
        if draft.get("pids"):
            payload["pids"] = draft["pids"]
        staged = base.check(
            session.put(
                f"{API}/records/{RECORD_ID}/draft",
                headers={**auth_headers(token), "Content-Type": "application/json"},
                json=payload,
                timeout=(30, 300),
            ),
            {200},
        ).json()
        if snapshot(staged) != before_files:
            raise RuntimeError("SGA file identities changed in staged edit")
        validate_fixed(staged["metadata"])
        base.check(
            session.post(
                f"{API}/records/{RECORD_ID}/draft/actions/publish",
                headers=auth_headers(token),
                timeout=(30, 300),
            ),
            {200, 202},
        )
        created = False
    except Exception:
        if created:
            session.delete(
                f"{API}/records/{RECORD_ID}/draft",
                headers=auth_headers(token),
                timeout=(30, 180),
            )
        raise

    after = None
    for _ in range(90):
        candidate = fetch_public(session)
        try:
            validate_fixed(candidate["metadata"])
        except RuntimeError:
            time.sleep(2)
            continue
        after = candidate
        break
    if after is None:
        raise RuntimeError("SGA notes edit did not become public")
    assert_latest(session)
    if draft_status(session, token) != 404:
        raise RuntimeError("SGA edit draft remained after publication")
    save_receipt(before, after, "PASS_PUBLIC_METADATA_READBACK")
    print(RECEIPT.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
