#!/usr/bin/env python3
"""Make the published EGA landing metadata describe the reader shelf only."""

from __future__ import annotations

import copy
import hashlib
import json
import time
from pathlib import Path

import publish_current_reader_bundles_zenodo_20260730 as base


API = base.API
RECORD_ID = 21_717_450
DOI = "10.5281/zenodo.21717450"
CONCEPT_DOI = "10.5281/zenodo.20414353"
EXPECTED_FILES = 44
EXPECTED_BYTES = 3_745_046_266
DEFAULT_PREVIEW = "00a_EGA0_English_Complete_Through_Section13_Reference_v2_20260730.pdf"
OLD_TITLE = "Elements de geometrie algebrique (EGA): French Originals, English Working Readers, and Source Archives"
NEW_TITLE = "Elements de geometrie algebrique (EGA): English Working Readers and Buildable TeX"
OLD_DESCRIPTION_SHA256 = "777EE61397F3884BA0782B2B5617F44F9DDA3E1166C70CD24C0ADABE32B1B39E"
NEW_VERSION = "2026-08-01 current English reader shelf"

DESCRIPTION = """<p><strong>Read EGA:</strong> begin with <code>00 Current_EGA_English_Readers_and_Buildable_TeX_20260730.zip</code>, or open any of the English reader PDFs directly. The complete buildable TeX is in the bundle, and the master TeX files are also direct downloads. EGA 0 is the default preview.</p>
<p><strong>Coverage:</strong> EGA 0 is complete through Section 13; EGA I and II are complete through their source endpoints; published EGA III is complete through 7.9.14; EGA IV is cumulative through Sections 1-10, with separate bounded readers for Sections 16-18 and Sections 19-21 plus Part 4 backmatter. Sections 11-15 remain to be integrated.</p>
<p>These are working translations, not a claim that all of EGA is complete or a critical edition.</p>"""

REPO_ROOT = Path(__file__).resolve().parent.parent
RECEIPT_PATH = REPO_ROOT / "manifests" / "published-zenodo" / "20260801_ega_record_21717450_reader_shelf_metadata_revision.json"


def headers(token: str | None = None) -> dict[str, str]:
    result = {"Accept": "application/vnd.inveniordm.v1+json"}
    if token:
        result["Authorization"] = f"Bearer {token}"
    return result


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest().upper()


def file_snapshot(record: dict) -> dict[str, tuple[int, str]]:
    return {
        name: (int(entry["size"]), base.normalized_md5(entry["checksum"]))
        for name, entry in sorted(base.modern_entries(record).items())
    }


def fetch_public(session) -> dict:
    return base.check(
        session.get(f"{API}/records/{RECORD_ID}?expand=true", headers=headers(), timeout=(30, 180)),
        {200},
    ).json()


def validate_boundary(record: dict) -> dict[str, tuple[int, str]]:
    files = file_snapshot(record)
    if (
        int(record["id"]) != RECORD_ID
        or record["pids"]["doi"]["identifier"] != DOI
        or record["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI
        or not record.get("is_published")
        or not record["versions"].get("is_latest")
        or len(files) != EXPECTED_FILES
        or sum(row[0] for row in files.values()) != EXPECTED_BYTES
        or record["files"].get("default_preview") != DEFAULT_PREVIEW
    ):
        raise RuntimeError("Live EGA record boundary changed")
    return files


def validate_metadata(metadata: dict) -> None:
    if metadata.get("title") != NEW_TITLE:
        raise RuntimeError("Reader-shelf title did not persist")
    if metadata.get("description") != DESCRIPTION:
        raise RuntimeError("Reader-shelf description did not persist")
    if metadata.get("version") != NEW_VERSION:
        raise RuntimeError("Reader-shelf version did not persist")
    lowered = (NEW_TITLE + " " + DESCRIPTION).casefold()
    for forbidden in ("image", "crop", "raster", "dpi", "witness", "scan"):
        if forbidden in lowered:
            raise RuntimeError(f"Reader-shelf metadata remains image-led: {forbidden}")


def replacement_metadata(metadata: dict) -> dict:
    updated = copy.deepcopy(metadata)
    updated["title"] = NEW_TITLE
    updated["description"] = DESCRIPTION
    updated["version"] = NEW_VERSION
    updated["subjects"] = [
        row for row in updated.get("subjects", [])
        if row.get("subject") != "French originals"
    ]
    existing = {row.get("subject") for row in updated.get("subjects", [])}
    for subject in ("English working readers", "buildable TeX"):
        if subject not in existing:
            updated.setdefault("subjects", []).append({"subject": subject})
    updated.pop("additional_descriptions", None)
    return updated


def main() -> None:
    session = base.make_session()
    token = base.find_token()
    before = fetch_public(session)
    before_files = validate_boundary(before)

    if before["metadata"].get("title") == NEW_TITLE:
        validate_metadata(before["metadata"])
        status = "PASS_ALREADY_APPLIED"
        after = before
    else:
        if before["metadata"].get("title") != OLD_TITLE:
            raise RuntimeError("EGA title changed before reader-shelf edit")
        observed = sha256_text(before["metadata"].get("description", ""))
        if observed != OLD_DESCRIPTION_SHA256:
            raise RuntimeError(f"EGA description changed before edit: {observed}")
        draft_status = session.get(f"{API}/records/{RECORD_ID}/draft", headers=headers(token), timeout=(30, 60))
        if draft_status.status_code != 404:
            raise RuntimeError("An EGA edit draft already exists")

        created = False
        try:
            draft = base.check(
                session.post(f"{API}/records/{RECORD_ID}/draft", headers=headers(token), timeout=(30, 180)),
                {201},
            ).json()
            created = True
            if file_snapshot(draft) != before_files:
                raise RuntimeError("EGA in-place draft did not inherit the exact file surface")

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
                "pids": draft["pids"],
            }
            patched = base.check(
                session.put(
                    f"{API}/records/{RECORD_ID}/draft",
                    headers={**headers(token), "Content-Type": "application/json"},
                    json=payload,
                    timeout=(30, 300),
                ),
                {200},
            ).json()
            if file_snapshot(patched) != before_files:
                raise RuntimeError("EGA files changed in the metadata draft")
            validate_metadata(patched["metadata"])
            base.check(
                session.post(
                    f"{API}/records/{RECORD_ID}/draft/actions/publish",
                    headers=headers(token),
                    timeout=(30, 300),
                ),
                {200, 202},
            )
            created = False
        except Exception:
            if created:
                session.delete(f"{API}/records/{RECORD_ID}/draft", headers=headers(token), timeout=(30, 180))
            raise

        after = None
        for _ in range(90):
            candidate = fetch_public(session)
            if candidate["metadata"].get("title") == NEW_TITLE:
                after = candidate
                break
            time.sleep(2)
        if after is None:
            raise RuntimeError("Reader-shelf metadata did not become public")
        status = "PASS_PUBLIC_METADATA_READBACK"

    after_files = validate_boundary(after)
    validate_metadata(after["metadata"])
    if after_files != before_files:
        raise RuntimeError("EGA file identities changed during metadata revision")
    receipt = {
        "status": status,
        "errors": [],
        "action": "in_place_reader_shelf_metadata_revision_only",
        "record": RECORD_ID,
        "doi": DOI,
        "concept_doi": CONCEPT_DOI,
        "public_url": f"https://zenodo.org/records/{RECORD_ID}",
        "new_record_created": False,
        "new_version_created": False,
        "file_count": len(after_files),
        "bytes": sum(row[0] for row in after_files.values()),
        "file_identities_unchanged": True,
        "default_preview": after["files"]["default_preview"],
        "revision_before": before.get("revision_id"),
        "revision_after": after.get("revision_id"),
        "title": NEW_TITLE,
        "description_bytes": len(DESCRIPTION.encode("utf-8")),
        "description_sha256": sha256_text(DESCRIPTION),
        "anonymous_public_readback": True,
    }
    base.save_json(RECEIPT_PATH, receipt)
    print(json.dumps(receipt))


if __name__ == "__main__":
    main()
