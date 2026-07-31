#!/usr/bin/env python3
"""Replace the current EGA record's accumulated image notes with reader-first metadata."""

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
DEFAULT_PREVIEW = (
    "00a_EGA0_English_Complete_Through_Section13_Reference_v2_20260730.pdf"
)
OLD_DESCRIPTION_SHA256 = (
    "68D6795A1F1FEE8B8306CC0D6470AB6767BC53A58D85B9DCF8CE24D97DBB6B44"
)
IMAGE_ONLY_SUBJECTS = {
    "EGA IV source-image witnesses",
    "high-detail mathematical source crops",
}

DESCRIPTION = """<p><strong>Start here:</strong> download <code>00 Current_EGA_English_Readers_and_Buildable_TeX_20260730.zip</code> for one bundle containing all five current cumulative English readers and their complete buildable TeX. The same reader PDFs and master TeX files are also available as direct downloads. EGA 0 is the default preview.</p>
<p><strong>Current English readers:</strong> EGA 0 is complete through Section 13; EGA I and EGA II are complete through their authority EOFs; EGA III contains the complete published text through Section 7.9.14; and the cumulative EGA IV reader covers Sections 1-10. Separate bounded packages cover EGA IV Sections 16-18 and Sections 19-21 with Part 4 backmatter. Sections 11-15 remain the cumulative EGA IV integration gap.</p>
<p>The NUMDAM French originals, source and QA archives, and optional high-resolution EGA IV source-witness archives follow the reader files. Older presentation states and superseded readers remain available in immutable predecessor versions.</p>
<p>These are scholarly working translations and source materials, not critical editions, peer-review or mathematical certifications, rights determinations, whole-EGA completion claims, or tagged-PDF accessibility remediation. No blanket license or transfer of underlying rights is asserted.</p>"""

NOTES = (
    "<p>File order is reader-first: the one-click current-reader bundle, direct "
    "PDF readers, direct master TeX, source packages, French originals, and "
    "supporting provenance archives. EGA 0 remains the default preview.</p>"
)

REPO_ROOT = Path(__file__).resolve().parent.parent
RECEIPT_PATH = REPO_ROOT / "manifests" / "published-zenodo" / (
    "20260731_ega_record_21717450_reader_first_metadata_revision.json"
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
    updated["subjects"] = [
        row
        for row in updated.get("subjects", [])
        if row.get("subject") not in IMAGE_ONLY_SUBJECTS
    ]
    updated["additional_descriptions"] = [
        {
            "description": NOTES,
            "type": {"id": "notes", "title": {"en": "Notes"}},
        }
    ]
    return updated


def validate_reader_first_metadata(metadata: dict) -> None:
    if metadata.get("description") != DESCRIPTION:
        raise RuntimeError("EGA reader-first description did not persist")
    if len(DESCRIPTION.encode("utf-8")) > 2_000 or DESCRIPTION.count("<p>") != 4:
        raise RuntimeError("EGA reader-first description boundary changed")
    lowered = DESCRIPTION.casefold()
    for forbidden in ("dpi", "printed page", "every member", "actual image"):
        if forbidden in lowered:
            raise RuntimeError(f"EGA description remains image-led: {forbidden}")
    subjects = {row.get("subject") for row in metadata.get("subjects", [])}
    if subjects & IMAGE_ONLY_SUBJECTS:
        raise RuntimeError("EGA image-only subjects remain")
    additions = metadata.get("additional_descriptions", [])
    if len(additions) != 1 or additions[0].get("description") != NOTES:
        raise RuntimeError("EGA Notes field did not collapse to one reader-first note")


def save_receipt(
    before: dict,
    after: dict,
    before_files: dict[str, dict[str, object]],
    status: str,
) -> None:
    after_files = validate_boundary(after)
    if after_files != before_files:
        raise RuntimeError("EGA file identities changed during metadata revision")
    validate_reader_first_metadata(after["metadata"])
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
            "notes_rows": len(after["metadata"].get("additional_descriptions", [])),
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
        validate_reader_first_metadata(before["metadata"])
        if edit_draft_status(session, token) != 404:
            raise RuntimeError("Unexpected active EGA edit draft after applied revision")
        save_receipt(before, before, before_files, "PASS_ALREADY_APPLIED")
        print(json.dumps(json.loads(RECEIPT_PATH.read_text(encoding="utf-8"))))
        return

    observed_description_sha = description_sha256(
        before["metadata"].get("description", "")
    )
    if observed_description_sha != OLD_DESCRIPTION_SHA256:
        raise RuntimeError(
            "EGA description changed before edit: " + observed_description_sha
        )
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
            raise RuntimeError("EGA in-place edit draft did not inherit exactly")

        metadata = replacement_metadata(draft["metadata"])
        validate_reader_first_metadata(metadata)
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
        validate_reader_first_metadata(patched["metadata"])

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
        raise RuntimeError("Reader-first EGA metadata did not become public")
    assert_latest(session)
    if edit_draft_status(session, token) != 404:
        raise RuntimeError("EGA edit draft remained after publication")
    save_receipt(before, after, before_files, "PASS_PUBLIC_METADATA_READBACK")
    print(json.dumps(json.loads(RECEIPT_PATH.read_text(encoding="utf-8"))))


if __name__ == "__main__":
    main()
