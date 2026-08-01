#!/usr/bin/env python3
"""Reduce the live Noether landing metadata to readers, coverage, and caveats."""

from __future__ import annotations

import copy
import hashlib
import json
import time
from pathlib import Path

import publish_current_reader_bundles_zenodo_20260730 as base


API = base.API
RECORD_ID = 21_699_405
DOI = "10.5281/zenodo.21699405"
CONCEPT_DOI = "10.5281/zenodo.20412587"
EXPECTED_FILES = 20
EXPECTED_BYTES = 583_142_749
DEFAULT_PREVIEW = "01j_Noether_R823_Full_Cumulative_English_20260722.pdf"
OLD_DESCRIPTION_SHA256 = (
    "934A7C961C5F95EC416E626375A49E45470CAB50B09883ADC7A820E0CE32A4BA"
)

DESCRIPTION = """<p><strong>Read Noether:</strong> open the 459-page full cumulative English reader directly, or download its adjacent English TeX/PDF ZIP for the complete buildable source. German, Spanish, French, Latin Interslavic, and Cyrillic Interslavic cumulative working readers are also direct downloads.</p>
<p><strong>Coverage:</strong> the English reader contains the inherited 43-paper corpus plus the complete translated German tail through line 24123. Editable TeX entry points and compact language, source-control, repair, and archive ZIPs follow the readers.</p>
<p>These are working editions and translations, not critical editions, peer review, mathematical or accessibility certification, rights clearance, or uniform recertification of every historical layer.</p>"""

REPO_ROOT = Path(__file__).resolve().parent.parent
RECEIPT_PATH = REPO_ROOT / "manifests" / "published-zenodo" / (
    "20260801_noether_record_21699405_readers_only_metadata_revision.json"
)


def public_headers() -> dict[str, str]:
    return {"Accept": "application/vnd.inveniordm.v1+json"}


def auth_headers(token: str) -> dict[str, str]:
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.inveniordm.v1+json",
    }


def description_sha256(value: str) -> str:
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
        raise RuntimeError("Live Noether record boundary changed")
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
        raise RuntimeError("Noether concept head moved")


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
    updated["additional_descriptions"] = []
    return updated


def validate_readers_only_metadata(metadata: dict) -> None:
    if metadata.get("description") != DESCRIPTION:
        raise RuntimeError("Noether readers-only description did not persist")
    if len(DESCRIPTION.encode("utf-8")) > 1_200:
        raise RuntimeError("Noether readers-only description grew beyond its boundary")
    if DESCRIPTION.count("<p>") != 3:
        raise RuntimeError("Noether readers-only description must have three paragraphs")
    lowered = DESCRIPTION.casefold()
    for forbidden in (
        "image",
        "raster",
        "dpi",
        "witness",
        "crop",
        "png",
        "visual evidence",
    ):
        if forbidden in lowered:
            raise RuntimeError(
                f"Noether description contains secondary-image prose: {forbidden}"
            )
    if metadata.get("additional_descriptions"):
        raise RuntimeError("Noether landing page still has an additional notes speech")


def save_receipt(
    before: dict,
    after: dict,
    before_files: dict[str, dict[str, object]],
    status: str,
) -> None:
    after_files = validate_boundary(after)
    if after_files != before_files:
        raise RuntimeError("Noether file identities changed during metadata revision")
    validate_readers_only_metadata(after["metadata"])
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
            "description_before_sha256": description_sha256(
                before["metadata"]["description"]
            ),
            "description_after_bytes": len(DESCRIPTION.encode("utf-8")),
            "description_after_sha256": description_sha256(DESCRIPTION),
            "description_paragraphs": DESCRIPTION.count("<p>"),
            "additional_description_rows": len(
                after["metadata"].get("additional_descriptions", [])
            ),
            "anonymous_metadata_readback": True,
            "official_api_method": "edit published record in place via record draft",
        },
    )


def main() -> None:
    session = base.make_session()
    token = base.find_token()
    before = fetch_public(session)
    before_files = validate_boundary(before)
    assert_latest(session)

    if before["metadata"].get("description") == DESCRIPTION:
        validate_readers_only_metadata(before["metadata"])
        if edit_draft_status(session, token) != 404:
            raise RuntimeError("Unexpected active Noether edit draft after applied revision")
        save_receipt(before, before, before_files, "PASS_ALREADY_APPLIED")
        print(json.dumps(json.loads(RECEIPT_PATH.read_text(encoding="utf-8"))))
        return

    observed_description_sha = description_sha256(
        before["metadata"].get("description", "")
    )
    if observed_description_sha != OLD_DESCRIPTION_SHA256:
        raise RuntimeError(
            "Noether description changed before edit: " + observed_description_sha
        )
    if edit_draft_status(session, token) != 404:
        raise RuntimeError("An active Noether edit draft already exists")

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
            raise RuntimeError("Noether in-place edit draft did not inherit exactly")

        metadata = replacement_metadata(draft["metadata"])
        validate_readers_only_metadata(metadata)
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
            raise RuntimeError("Noether file identities changed in staged edit")
        validate_readers_only_metadata(patched["metadata"])

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
        raise RuntimeError("Readers-only Noether metadata did not become public")
    assert_latest(session)
    if edit_draft_status(session, token) != 404:
        raise RuntimeError("Noether edit draft remained after publication")
    save_receipt(before, after, before_files, "PASS_PUBLIC_METADATA_READBACK")
    print(json.dumps(json.loads(RECEIPT_PATH.read_text(encoding="utf-8"))))


if __name__ == "__main__":
    main()
