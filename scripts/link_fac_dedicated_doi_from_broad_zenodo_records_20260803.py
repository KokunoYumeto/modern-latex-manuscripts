#!/usr/bin/env python3
"""Add the dedicated FAC DOI link to the two broad provenance descriptions.

This is an in-place metadata-only revision of the already-published methodology
and replication heads. It creates no new version or concept and changes no file,
file order, or default preview.
"""

from __future__ import annotations

import copy
import hashlib
import time
from dataclasses import dataclass
from pathlib import Path

import publish_current_reader_bundles_zenodo_20260730 as base


API = base.API
FAC_CONCEPT_DOI = "10.5281/zenodo.21779392"
FAC_VERSION_DOI = "10.5281/zenodo.21779393"
FAC_URL = "https://doi.org/10.5281/zenodo.21779392"
FAC_VERSION_URL = "https://doi.org/10.5281/zenodo.21779393"
FAC_PARAGRAPH = (
    '<p><strong>Dedicated FAC quality-assessment record:</strong> '
    'the controlling coherent FAC translation-quality evidence is '
    f'<a href="{FAC_URL}">{FAC_CONCEPT_DOI}</a> '
    f'(current version <a href="{FAC_VERSION_URL}">{FAC_VERSION_DOI}</a>). '
    'It documents the accidental pre-discovery translation chronology for FAC '
    'nos. 1-79, both project English readers, authority-adjudicated findings, '
    'exact model/process provenance, and append-only decisions, corrections, '
    'errors, and reversals. Earlier FAC projections retained in this broad '
    'deposit are immutable adverse history; use the dedicated record for the '
    'coherent evidence package. No FAC payload is duplicated here, and GAGA '
    'remains a separate publication line.</p>'
)
REPO_ROOT = Path(__file__).resolve().parent.parent
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"


@dataclass(frozen=True)
class Surface:
    key: str
    record_id: int
    doi: str
    concept_doi: str
    files: int
    bytes: int


SURFACES = (
    Surface(
        key="methodology",
        record_id=21778949,
        doi="10.5281/zenodo.21778949",
        concept_doi="10.5281/zenodo.21124403",
        files=99,
        bytes=4_990_185_641,
    ),
    Surface(
        key="replication",
        record_id=21778962,
        doi="10.5281/zenodo.21778962",
        concept_doi="10.5281/zenodo.20461174",
        files=64,
        bytes=8_586_618,
    ),
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


def fetch_public(session, surface: Surface) -> dict:
    return base.check(
        session.get(
            f"{API}/records/{surface.record_id}?expand=true",
            headers=public_headers(),
            timeout=(30, 180),
        ),
        {200},
    ).json()


def validate_boundary(record: dict, surface: Surface) -> dict[str, dict[str, object]]:
    files = file_snapshot(record)
    if (
        int(record["id"]) != surface.record_id
        or record["pids"]["doi"]["identifier"] != surface.doi
        or record["parent"]["pids"]["doi"]["identifier"] != surface.concept_doi
        or not record.get("is_published")
        or not record["versions"].get("is_latest")
        or len(files) != surface.files
        or sum(int(row["bytes"]) for row in files.values()) != surface.bytes
    ):
        raise RuntimeError(f"{surface.key} live boundary changed")
    return files


def assert_latest(session, surface: Surface) -> None:
    latest = base.check(
        session.get(
            f"{API}/records/{surface.record_id}/versions/latest?expand=true",
            headers=public_headers(),
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if int(latest["id"]) != surface.record_id:
        raise RuntimeError(f"{surface.key} concept head moved")


def fetch_edit_draft(session, token: str, surface: Surface) -> tuple[int, dict | None]:
    response = session.get(
        f"{API}/records/{surface.record_id}/draft?expand=true",
        headers=auth_headers(token),
        timeout=(30, 90),
    )
    if response.status_code == 404:
        return 404, None
    return 200, base.check(response, {200}).json()


def desired_description(description: str) -> str:
    if FAC_CONCEPT_DOI in description and FAC_VERSION_DOI in description:
        return description
    return FAC_PARAGRAPH + "\n" + description


def save_receipt(
    surface: Surface,
    before: dict,
    after: dict,
    before_files: dict[str, dict[str, object]],
    status: str,
) -> None:
    after_files = validate_boundary(after, surface)
    if after_files != before_files:
        raise RuntimeError(f"{surface.key} file identities changed")
    description = after["metadata"].get("description", "")
    if not description.startswith(FAC_PARAGRAPH):
        raise RuntimeError(f"{surface.key} public FAC paragraph missing")
    if after["files"].get("order", []) != before["files"].get("order", []):
        raise RuntimeError(f"{surface.key} file order changed")
    if after["files"].get("default_preview") != before["files"].get(
        "default_preview"
    ):
        raise RuntimeError(f"{surface.key} default preview changed")

    receipt_path = RECEIPT_ROOT / (
        f"20260803_fac_dedicated_link_{surface.key}_record_"
        f"{surface.record_id}_metadata_readback.json"
    )
    base.save_json(
        receipt_path,
        {
            "status": status,
            "errors": [],
            "action": "in_place_fac_dedicated_doi_description_link_only",
            "record_id": surface.record_id,
            "doi": surface.doi,
            "concept_doi": surface.concept_doi,
            "public_url": f"https://zenodo.org/records/{surface.record_id}",
            "dedicated_fac_concept_doi": FAC_CONCEPT_DOI,
            "dedicated_fac_version_doi": FAC_VERSION_DOI,
            "new_record_created": False,
            "new_version_created": False,
            "duplicate_concept_created": False,
            "fac_payload_files_added": 0,
            "file_count": len(after_files),
            "bytes": sum(int(row["bytes"]) for row in after_files.values()),
            "file_surface_sha256": file_surface_sha256(after_files),
            "file_identities_unchanged": True,
            "file_order_unchanged": True,
            "default_preview_unchanged": True,
            "revision_before": before.get("revision_id"),
            "revision_after": after.get("revision_id"),
            "description_before_sha256": sha256_text(
                before["metadata"].get("description", "")
            ),
            "description_after_sha256": sha256_text(description),
            "fac_concept_link_present": FAC_CONCEPT_DOI in description,
            "fac_version_link_present": FAC_VERSION_DOI in description,
            "anonymous_metadata_readback": True,
            "active_edit_draft_after": False,
            "claim_boundary": (
                "Metadata description cross-link only. No file, file order, "
                "preview, version, concept, production, or rights bytes changed."
            ),
        },
    )


def revise_surface(session, token: str, surface: Surface) -> None:
    before = fetch_public(session, surface)
    before_files = validate_boundary(before, surface)
    assert_latest(session, surface)
    draft_status, _ = fetch_edit_draft(session, token, surface)
    if draft_status != 404:
        raise RuntimeError(f"{surface.key} already has an active edit draft")

    wanted = desired_description(before["metadata"].get("description", ""))
    if wanted == before["metadata"].get("description", ""):
        save_receipt(surface, before, before, before_files, "PASS_ALREADY_APPLIED")
        return

    created = False
    publish_sent = False
    try:
        draft = base.check(
            session.post(
                f"{API}/records/{surface.record_id}/draft",
                headers=auth_headers(token),
                timeout=(30, 180),
            ),
            {201},
        ).json()
        created = True
        if int(draft["id"]) != surface.record_id or file_snapshot(draft) != before_files:
            raise RuntimeError(f"{surface.key} edit draft did not inherit exactly")

        metadata = copy.deepcopy(draft["metadata"])
        metadata["description"] = wanted
        payload = {
            "access": draft["access"],
            "files": {
                "enabled": True,
                "default_preview": draft["files"].get("default_preview"),
                "order": draft["files"].get("order", []),
            },
            "metadata": metadata,
            "custom_fields": draft.get("custom_fields", {}),
        }
        if draft.get("pids"):
            payload["pids"] = draft["pids"]
        staged = base.check(
            session.put(
                f"{API}/records/{surface.record_id}/draft",
                headers={**auth_headers(token), "Content-Type": "application/json"},
                json=payload,
                timeout=(30, 300),
            ),
            {200},
        ).json()
        if file_snapshot(staged) != before_files:
            raise RuntimeError(f"{surface.key} staged files changed")
        if staged["metadata"].get("description") != wanted:
            raise RuntimeError(f"{surface.key} staged description changed")

        publish_sent = True
        response = session.post(
            f"{API}/records/{surface.record_id}/draft/actions/publish",
            headers=auth_headers(token),
            timeout=(30, 300),
        )
        base.check(response, {200, 202})
        created = False
    except Exception:
        if created and not publish_sent:
            session.delete(
                f"{API}/records/{surface.record_id}/draft",
                headers=auth_headers(token),
                timeout=(30, 180),
            )
        raise

    after = None
    for _ in range(90):
        try:
            candidate = fetch_public(session, surface)
            description = candidate["metadata"].get("description", "")
            if description.startswith(FAC_PARAGRAPH):
                after = candidate
                break
        except Exception:
            pass
        time.sleep(2)
    if after is None:
        raise RuntimeError(f"{surface.key} FAC link did not become public")
    assert_latest(session, surface)
    draft_status, _ = fetch_edit_draft(session, token, surface)
    if draft_status != 404:
        raise RuntimeError(f"{surface.key} edit draft remained after publish")
    save_receipt(
        surface,
        before,
        after,
        before_files,
        "PASS_PUBLIC_METADATA_READBACK",
    )


def main() -> int:
    token = base.find_token()
    session = base.make_session()
    for surface in SURFACES:
        revise_surface(session, token, surface)
        print(f"{surface.key}: PASS {surface.record_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
