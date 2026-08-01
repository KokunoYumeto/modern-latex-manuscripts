#!/usr/bin/env python3
"""Describe the current SGA ZIP as reader PDFs, not one global SGA PDF."""

from __future__ import annotations

import copy
import hashlib
import time
from pathlib import Path

import publish_current_reader_bundles_zenodo_20260730 as base


API = base.API
RECORD_ID = 21_738_682
DOI = "10.5281/zenodo.21738682"
CONCEPT_DOI = "10.5281/zenodo.20410947"
EXPECTED_FILES = 83
EXPECTED_BYTES = 681_903_307
DEFAULT_PREVIEW = "00a_SGA1_English_Reader.pdf"
OLD_DESCRIPTION_SHA256 = (
    "85939C8E8AF6CABF76924B2E48CB7958155A719CCCFC214935643DDEE6001C84"
)
OLD_NOTE = (
    "<p>Reader PDFs contain mathematical text only. Build sources, provenance, "
    "and release controls are separate downloadable files.</p>"
)

DESCRIPTION = """<p><strong>Start here:</strong> the first ZIP collects the current English reader PDFs and buildable TeX for SGA 1 through SGA 7 I. The same PDFs and master TeX files remain direct; SGA1 remains the browser preview. This is not yet one cross-volume SGA 1-7.2 PDF.</p><p><strong>SGA3:</strong> the current cumulative English reader is the clean 1,470-page R29 reader covering the Introduction, Exposes I-XXVI, indexes, and guide.</p><p><strong>SGA7:</strong> SGA7 I has a complete 287-page English working reader for all written Exposes I, II, VI, VII, VIII, and IX. The record also retains the complete SGA7 I French working transcription and the current partial SGA7 II French transcription.</p><p>These are working scholarly translations, editions, or transcriptions, not critical editions, peer review, exhaustive reference certification, accessibility certification, rights determinations, or mathematical certification.</p>"""

REPO_ROOT = Path(__file__).resolve().parent.parent
RECEIPT_PATH = REPO_ROOT / "manifests" / "published-zenodo" / (
    "20260801_sga_record_21738682_standalone_reader_metadata_revision.json"
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
        raise RuntimeError("Live SGA record boundary changed")
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
        raise RuntimeError("SGA concept head moved")


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


def validate_metadata(metadata: dict) -> None:
    if metadata.get("description") != DESCRIPTION:
        raise RuntimeError("SGA standalone-reader description did not persist")
    if len(DESCRIPTION.encode("utf-8")) != 928 or DESCRIPTION.count("<p>") != 4:
        raise RuntimeError("SGA standalone-reader description boundary changed")
    if "current cumulative English reader PDF and buildable TeX for SGA" in DESCRIPTION:
        raise RuntimeError("Stale global cumulative-reader wording remains")
    if metadata.get("additional_descriptions"):
        raise RuntimeError("Redundant SGA Notes block remains")


def validate_old_notes(metadata: dict) -> None:
    rows = metadata.get("additional_descriptions", [])
    if (
        len(rows) != 1
        or rows[0].get("description") != OLD_NOTE
        or rows[0].get("type", {}).get("id") != "notes"
    ):
        raise RuntimeError("SGA additional-description boundary changed")


def save_receipt(
    before: dict,
    after: dict,
    before_files: dict[str, dict[str, object]],
    status: str,
) -> None:
    after_files = validate_boundary(after)
    if after_files != before_files:
        raise RuntimeError("SGA file identities changed during metadata revision")
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
            "additional_descriptions_before": len(
                before["metadata"].get("additional_descriptions", [])
            ),
            "additional_descriptions_after": len(
                after["metadata"].get("additional_descriptions", [])
            ),
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
            raise RuntimeError("Unexpected active SGA edit draft")
        save_receipt(before, before, before_files, "PASS_ALREADY_APPLIED")
        print(RECEIPT_PATH.read_text(encoding="utf-8"))
        return

    observed = sha256_text(before["metadata"].get("description", ""))
    if observed != OLD_DESCRIPTION_SHA256:
        raise RuntimeError("SGA description changed before edit: " + observed)
    validate_old_notes(before["metadata"])
    if edit_draft_status(session, token) != 404:
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
        if int(draft["id"]) != RECORD_ID or file_snapshot(draft) != before_files:
            raise RuntimeError("SGA edit draft did not inherit exactly")

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
            raise RuntimeError("SGA file identities changed in staged edit")
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
        raise RuntimeError("Standalone-reader SGA metadata did not become public")
    assert_latest(session)
    if edit_draft_status(session, token) != 404:
        raise RuntimeError("SGA edit draft remained after publication")
    save_receipt(before, after, before_files, "PASS_PUBLIC_METADATA_READBACK")
    print(RECEIPT_PATH.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
