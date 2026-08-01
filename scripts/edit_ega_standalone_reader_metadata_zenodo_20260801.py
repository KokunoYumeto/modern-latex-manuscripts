#!/usr/bin/env python3
"""Describe the current EGA ZIP as standalone readers, not a global PDF."""

from __future__ import annotations

import copy
import hashlib
import json
import time
from pathlib import Path

import publish_current_reader_bundles_zenodo_20260730 as base


API = base.API
RECORD_ID = 21_740_145
DOI = "10.5281/zenodo.21740145"
CONCEPT_DOI = "10.5281/zenodo.20414353"
EXPECTED_FILES = 40
EXPECTED_BYTES = 3_752_670_964
DEFAULT_PREVIEW = (
    "00a_EGA0_English_Complete_Through_Section13_Reference_v2_20260730.pdf"
)
OLD_DESCRIPTION_SHA256 = (
    "A4A6B672080B9C985C2D8A20636D8835DCF37C8700034DF2DB5E1278757AA202"
)

DESCRIPTION = """<p><strong>Read EGA:</strong> open any English reader PDF directly, or download <code>00 Current_EGA_English_Readers_and_Buildable_TeX_20260801.zip</code> for the current standalone readers and their buildable TeX. EGA 0 remains the default preview.</p>
<p><strong>Coverage:</strong> EGA 0 is complete through Section 13; EGA I and II are complete through their source endpoints; published EGA III is complete through 7.9.14; EGA IV is complete through Sections 1-21 and EOF, with 5,911 destinations and 7,374 resolved local links. Cross-volume references remain visible nonlinks.</p>
<p>These are working translations, not critical editions.</p>"""

REPO_ROOT = Path(__file__).resolve().parent.parent
RECEIPT_PATH = REPO_ROOT / "manifests" / "published-zenodo" / (
    "20260801_ega_record_21740145_standalone_reader_metadata_revision.json"
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


def file_snapshot(record: dict) -> dict[str, dict[str, object]]:
    return {
        name: {
            "bytes": int(entry["size"]),
            "md5": base.normalized_md5(entry["checksum"]),
        }
        for name, entry in sorted(
            base.modern_entries(record).items(), key=lambda row: row[0].casefold()
        )
    }


def file_surface_sha256(files: dict[str, dict[str, object]]) -> str:
    digest = hashlib.sha256()
    for name, row in files.items():
        digest.update(
            f"{name}\t{int(row['bytes'])}\t{row['md5']}\n".encode("utf-8")
        )
    return digest.hexdigest().upper()


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
    files = file_snapshot(record)
    if (
        int(record["id"]) != RECORD_ID
        or record["pids"]["doi"]["identifier"] != DOI
        or record["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI
        or not record.get("is_published")
        or not record["versions"].get("is_latest")
        or len(files) != EXPECTED_FILES
        or sum(int(row["bytes"]) for row in files.values()) != EXPECTED_BYTES
        or record["files"].get("default_preview") != DEFAULT_PREVIEW
    ):
        raise RuntimeError("Live EGA record boundary changed")
    return files


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
        raise RuntimeError("EGA concept head moved")


def edit_draft_status(session, token: str) -> int:
    response = session.get(
        f"{API}/records/{RECORD_ID}/draft",
        headers=auth_headers(token),
        timeout=(30, 60),
    )
    if response.status_code == 404:
        return 404
    base.check(response, {200})
    return 200


def replacement_metadata(metadata: dict) -> dict:
    updated = copy.deepcopy(metadata)
    updated["description"] = DESCRIPTION
    return updated


def validate_metadata(metadata: dict) -> None:
    if metadata.get("description") != DESCRIPTION:
        raise RuntimeError("Standalone-reader description did not persist")
    if len(DESCRIPTION.encode("utf-8")) != 646 or DESCRIPTION.count("<p>") != 3:
        raise RuntimeError("Standalone-reader description boundary changed")
    if "current cumulative readers" in DESCRIPTION:
        raise RuntimeError("Stale cumulative-reader wording remains")


def save_receipt(
    before: dict,
    after: dict,
    before_files: dict[str, dict[str, object]],
    status: str,
) -> None:
    after_files = validate_boundary(after)
    if after_files != before_files:
        raise RuntimeError("EGA file identities changed during metadata revision")
    validate_metadata(after["metadata"])
    base.save_json(
        RECEIPT_PATH,
        {
            "status": status,
            "errors": [],
            "action": "in_place_metadata_revision_only",
            "record": RECORD_ID,
            "doi": DOI,
            "conceptdoi": CONCEPT_DOI,
            "public_url": f"https://zenodo.org/records/{RECORD_ID}",
            "new_record_created": False,
            "new_version_created": False,
            "duplicate_concept_created": False,
            "file_count": len(after_files),
            "bytes": sum(int(row["bytes"]) for row in after_files.values()),
            "default_preview": after["files"]["default_preview"],
            "file_surface_sha256": file_surface_sha256(after_files),
            "file_identities_unchanged": True,
            "revision_before": before.get("revision_id"),
            "revision_after": after.get("revision_id"),
            "description_before_bytes": len(
                before["metadata"]["description"].encode("utf-8")
            ),
            "description_before_sha256": sha256_text(
                before["metadata"]["description"]
            ),
            "description_after_bytes": len(DESCRIPTION.encode("utf-8")),
            "description_after_sha256": sha256_text(DESCRIPTION),
            "description_paragraphs": DESCRIPTION.count("<p>"),
            "anonymous_metadata_readback": True,
            "official_api_method": "edit published record in place via record draft",
            "claim_boundary": (
                "Reader-surface wording only; no file, preview, version, "
                "reference, translation, or quality claim changed."
            ),
        },
    )


def main() -> None:
    session = base.make_session()
    token = base.find_token()
    before = fetch_public(session)
    before_files = validate_boundary(before)
    assert_latest(session)

    if before["metadata"].get("description") == DESCRIPTION:
        validate_metadata(before["metadata"])
        if edit_draft_status(session, token) != 404:
            raise RuntimeError("Unexpected active EGA edit draft")
        save_receipt(before, before, before_files, "PASS_ALREADY_APPLIED")
        print(RECEIPT_PATH.read_text(encoding="utf-8"))
        return

    observed = sha256_text(before["metadata"].get("description", ""))
    if observed != OLD_DESCRIPTION_SHA256:
        raise RuntimeError("EGA description changed before edit: " + observed)
    if edit_draft_status(session, token) != 404:
        raise RuntimeError("An active EGA edit draft already exists")

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
        if int(draft["id"]) != RECORD_ID or file_snapshot(draft) != before_files:
            raise RuntimeError("EGA edit draft did not inherit exactly")

        metadata = replacement_metadata(draft["metadata"])
        validate_metadata(metadata)
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
        patched = base.check(
            session.put(
                f"{API}/records/{RECORD_ID}/draft",
                headers={**auth_headers(token), "Content-Type": "application/json"},
                json=payload,
                timeout=(30, 300),
            ),
            {200},
        ).json()
        if file_snapshot(patched) != before_files:
            raise RuntimeError("EGA file identities changed in staged edit")
        validate_metadata(patched["metadata"])

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
        if candidate["metadata"].get("description") == DESCRIPTION:
            after = candidate
            break
        time.sleep(2)
    if after is None:
        raise RuntimeError("Standalone-reader EGA metadata did not become public")
    assert_latest(session)
    if edit_draft_status(session, token) != 404:
        raise RuntimeError("EGA edit draft remained after publication")
    save_receipt(before, after, before_files, "PASS_PUBLIC_METADATA_READBACK")
    print(RECEIPT_PATH.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
