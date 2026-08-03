#!/usr/bin/env python3
"""Hold the status-bearing SGA readers without creating a new version.

This edits only the published record metadata/default preview.  It does not
create a concept or version and does not add, replace, reorder, or delete any
file.  The provisional cumulative reader remains preserved as historical
bytes while a no-overwrite reader-pure successor is prepared.
"""

from __future__ import annotations

import copy
import hashlib
import time
from pathlib import Path

import publish_current_reader_bundles_zenodo_20260730 as base


API = base.API
RECORD_ID = 21_775_746
DOI = "10.5281/zenodo.21775746"
CONCEPT_DOI = "10.5281/zenodo.20410947"
EXPECTED_FILES = 100
EXPECTED_BYTES = 851_729_584
OLD_DEFAULT_PREVIEW = "00a_SGA1_English_Reader.pdf"
NEW_DEFAULT_PREVIEW = "00b_SGA2_English_Reader.pdf"
NEW_PREVIEW_BYTES = 1_996_972
NEW_PREVIEW_MD5 = "49c10557f839e3de3888366ecb1bedf4"
HELD_GLOBAL = (
    "00z_SGA_1-7II_English_Global_Reader_navigation_r3_"
    "PROVISIONAL_20260803.pdf"
)
HELD_GLOBAL_BYTES = 33_402_752
HELD_GLOBAL_MD5 = "ff775da5d7584d91af07df511b57126e"

HOLD_PARAGRAPH = (
    "<p><strong>Reader-presentation hold (3 August 2026):</strong> "
    "the provisional cumulative SGA 1-7 II PDF and the then-current SGA1 "
    "preview inherit visible workflow/source-status prose. They are retained "
    "in this version only as explicitly provisional, superseded archival "
    "history and must not be treated as clean reader-facing editions. A "
    "no-overwrite clean cumulative successor is in preparation; production "
    "rationale remains in external logbooks rather than reader PDFs.</p>"
)
STALE_START_PARAGRAPH = (
    "<p><strong>Start here:</strong> the first ZIP collects the current "
    "English reader PDFs and buildable TeX closures for SGA 1 through SGA 7 "
    "II. The same readers and master TeX files remain direct; SGA1 remains "
    "the browser preview. This is not yet one cross-volume SGA 1-7.2 PDF.</p>"
)
HOLD_START_PARAGRAPH = (
    "<p><strong>Archive layout during the hold:</strong> the first ZIP "
    "preserves the predecessor standalone English reader PDFs and buildable "
    "TeX closures for SGA 1 through SGA 7 II. The same readers and master "
    "TeX files remain direct. The verified clean SGA2 reader is the interim "
    "browser preview; the provisional cumulative PDF remains directly "
    "downloadable only as held/superseded history. This is not a clean or "
    "terminal cross-volume SGA release.</p>"
)

REPO_ROOT = Path(__file__).resolve().parent.parent
RECEIPT_PATH = REPO_ROOT / "manifests" / "published-zenodo" / (
    "20260803_sga_record_21775746_reader_presentation_hold_revision.json"
)


def public_headers() -> dict[str, str]:
    return {"Accept": "application/vnd.inveniordm.v1+json"}


def auth_headers(token: str) -> dict[str, str]:
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.inveniordm.v1+json",
    }


def file_snapshot(record: dict) -> dict[str, dict[str, object]]:
    return {
        name: {
            "uuid": str(entry["id"]),
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
            (
                f"{name}\t{row['uuid']}\t{int(row['bytes'])}\t"
                f"{row['md5']}\n"
            ).encode("utf-8")
        )
    return digest.hexdigest().upper()


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest().upper()


def fetch_public(session) -> dict:
    return base.check(
        session.get(
            f"{API}/records/{RECORD_ID}?expand=true",
            headers=public_headers(),
            timeout=(30, 180),
        ),
        {200},
    ).json()


def fetch_edit_draft(session, token: str) -> tuple[int, dict | None]:
    response = session.get(
        f"{API}/records/{RECORD_ID}/draft?expand=true",
        headers=auth_headers(token),
        timeout=(30, 90),
    )
    if response.status_code == 404:
        return 404, None
    return 200, base.check(response, {200}).json()


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


def validate_boundary(
    record: dict, allowed_previews: set[str]
) -> dict[str, dict[str, object]]:
    files = file_snapshot(record)
    if (
        int(record["id"]) != RECORD_ID
        or record["pids"]["doi"]["identifier"] != DOI
        or record["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI
        or not record.get("is_published")
        or not record["versions"].get("is_latest")
        or len(files) != EXPECTED_FILES
        or sum(int(row["bytes"]) for row in files.values()) != EXPECTED_BYTES
        or record["files"].get("default_preview") not in allowed_previews
    ):
        raise RuntimeError("Live SGA hold boundary changed")
    if (
        files[NEW_DEFAULT_PREVIEW]["bytes"],
        files[NEW_DEFAULT_PREVIEW]["md5"],
    ) != (NEW_PREVIEW_BYTES, NEW_PREVIEW_MD5):
        raise RuntimeError("Clean interim preview identity changed")
    if (files[HELD_GLOBAL]["bytes"], files[HELD_GLOBAL]["md5"]) != (
        HELD_GLOBAL_BYTES,
        HELD_GLOBAL_MD5,
    ):
        raise RuntimeError("Held cumulative reader identity changed")
    return files


def description_with_hold(description: str) -> str:
    updated = description.replace(STALE_START_PARAGRAPH, HOLD_START_PARAGRAPH)
    if STALE_START_PARAGRAPH in updated:
        raise RuntimeError("Stale SGA1 preview paragraph survived replacement")
    if not updated.startswith(HOLD_PARAGRAPH):
        updated = HOLD_PARAGRAPH + "\n" + updated
    return updated


def save_receipt(
    before: dict,
    after: dict,
    before_files: dict[str, dict[str, object]],
    status: str,
) -> None:
    after_files = validate_boundary(after, {NEW_DEFAULT_PREVIEW})
    if after_files != before_files:
        raise RuntimeError("File identities changed during presentation hold")
    if not after["metadata"].get("description", "").startswith(HOLD_PARAGRAPH):
        raise RuntimeError("Public hold paragraph did not persist")
    if HOLD_START_PARAGRAPH not in after["metadata"].get("description", ""):
        raise RuntimeError("Public interim-preview paragraph did not persist")
    if STALE_START_PARAGRAPH in after["metadata"].get("description", ""):
        raise RuntimeError("Public description still claims SGA1 is the preview")
    if after["files"].get("order", []) != before["files"].get("order", []):
        raise RuntimeError("File order changed during presentation hold")
    base.save_json(
        RECEIPT_PATH,
        {
            "status": status,
            "errors": [],
            "action": "in_place_reader_presentation_hold_only",
            "record": RECORD_ID,
            "doi": DOI,
            "conceptdoi": CONCEPT_DOI,
            "public_url": f"https://zenodo.org/records/{RECORD_ID}",
            "new_record_created": False,
            "new_version_created": False,
            "duplicate_concept_created": False,
            "file_count": len(after_files),
            "bytes": sum(int(row["bytes"]) for row in after_files.values()),
            "file_surface_sha256": file_surface_sha256(after_files),
            "file_identities_unchanged": True,
            "file_order_unchanged": True,
            "revision_before": before.get("revision_id"),
            "revision_after": after.get("revision_id"),
            "default_preview_before": before["files"].get("default_preview"),
            "default_preview_after": after["files"].get("default_preview"),
            "held_global_reader": HELD_GLOBAL,
            "held_global_reader_bytes": HELD_GLOBAL_BYTES,
            "held_global_reader_md5": HELD_GLOBAL_MD5,
            "interim_clean_preview": NEW_DEFAULT_PREVIEW,
            "interim_clean_preview_bytes": NEW_PREVIEW_BYTES,
            "interim_clean_preview_md5": NEW_PREVIEW_MD5,
            "description_before_sha256": sha256_text(
                before["metadata"].get("description", "")
            ),
            "description_after_sha256": sha256_text(
                after["metadata"].get("description", "")
            ),
            "anonymous_metadata_readback": True,
            "active_edit_draft_after": False,
            "permanent_successor_order": [
                "complete reader/source ZIP",
                "clean cumulative reader PDF and default preview",
                "individual reader PDFs",
                "cumulative and individual TeX/source",
                "validation, manifests, logbooks, and history",
            ],
            "claim_boundary": (
                "Metadata/default-preview hold only. No file, version, concept, "
                "translation, source, mathematical, or navigation bytes changed."
            ),
        },
    )


def main() -> None:
    session = base.make_session()
    token = base.find_token()
    before = fetch_public(session)
    before_files = validate_boundary(
        before, {OLD_DEFAULT_PREVIEW, NEW_DEFAULT_PREVIEW}
    )
    assert_latest(session)
    draft_status, _ = fetch_edit_draft(session, token)
    if draft_status != 404:
        raise RuntimeError("An active SGA edit draft already exists")

    desired_description = description_with_hold(
        before["metadata"].get("description", "")
    )
    if (
        before["files"].get("default_preview") == NEW_DEFAULT_PREVIEW
        and before["metadata"].get("description") == desired_description
    ):
        save_receipt(before, before, before_files, "PASS_ALREADY_APPLIED")
        print(RECEIPT_PATH.read_text(encoding="utf-8"))
        return

    created = False
    publish_sent = False
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

        metadata = copy.deepcopy(draft["metadata"])
        metadata["description"] = desired_description
        payload = {
            "access": draft["access"],
            "files": {
                "enabled": True,
                "default_preview": NEW_DEFAULT_PREVIEW,
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
            raise RuntimeError("File identities changed in staged presentation hold")
        if patched["files"].get("default_preview") != NEW_DEFAULT_PREVIEW:
            raise RuntimeError("Staged clean interim preview did not persist")
        if patched["metadata"].get("description") != desired_description:
            raise RuntimeError("Staged presentation-hold paragraph did not persist")

        publish_sent = True
        response = session.post(
            f"{API}/records/{RECORD_ID}/draft/actions/publish",
            headers=auth_headers(token),
            timeout=(30, 300),
        )
        base.check(response, {200, 202})
        created = False
    except Exception:
        if created and not publish_sent:
            session.delete(
                f"{API}/records/{RECORD_ID}/draft",
                headers=auth_headers(token),
                timeout=(30, 180),
            )
        if not publish_sent:
            raise

    after = None
    for _ in range(90):
        try:
            candidate = fetch_public(session)
            if (
                candidate["files"].get("default_preview") == NEW_DEFAULT_PREVIEW
                and candidate["metadata"].get("description", "").startswith(
                    HOLD_PARAGRAPH
                )
            ):
                after = candidate
                break
        except Exception:
            pass
        time.sleep(2)
    if after is None:
        raise RuntimeError("Presentation hold did not become anonymously public")
    assert_latest(session)
    draft_status, _ = fetch_edit_draft(session, token)
    if draft_status != 404:
        raise RuntimeError("SGA edit draft remained after presentation hold")
    save_receipt(before, after, before_files, "PASS_PUBLIC_METADATA_READBACK")
    print(RECEIPT_PATH.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
