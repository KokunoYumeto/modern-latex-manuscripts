#!/usr/bin/env python3
"""Replace tombstoned FAC cross-links on three current Zenodo records.

This is an in-place metadata-only correction.  It creates no record, version,
concept, or file and verifies that file identities, configured order, default
preview, title, access, and lineage remain unchanged.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import sys
import time
from dataclasses import dataclass
from pathlib import Path

import publish_current_reader_bundles_zenodo_20260730 as base


API = base.API
MODERN = {"Accept": "application/vnd.inveniordm.v1+json"}
OLD_CONCEPT = "10.5281/zenodo.21779392"
OLD_VERSION = "10.5281/zenodo.21779393"
NEW_CONCEPT = "10.5281/zenodo.21720996"
NEW_VERSION = "10.5281/zenodo.21781714"
CONFIRMATION = "21782511,21782515,21781323"
REPO_ROOT = Path(__file__).resolve().parent.parent


@dataclass(frozen=True)
class Surface:
    key: str
    record_id: int
    doi: str
    concept_doi: str
    files: int
    bytes: int
    preview: str


SURFACES = (
    Surface(
        "methodology",
        21782511,
        "10.5281/zenodo.21782511",
        "10.5281/zenodo.21124403",
        100,
        5_004_414_281,
        "00_Interlanguage_Methodology_Current_v13_20260718.pdf",
    ),
    Surface(
        "replication",
        21782515,
        "10.5281/zenodo.21782515",
        "10.5281/zenodo.20461174",
        77,
        22_843_758,
        "00_AI_Run_Modern_LaTeX_Manuscript_Workflow_Current_20260728.pdf",
    ),
    Surface(
        "gaga",
        21781323,
        "10.5281/zenodo.21781323",
        "10.5281/zenodo.21781322",
        62,
        1_455_665,
        "01_GAGA_English_reference_v2.pdf",
    ),
)


def auth(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}", **MODERN}


def entries(record: dict) -> dict[str, dict]:
    return record.get("files", {}).get("entries", {})


def snapshot(record: dict) -> dict[str, tuple[str, int, str]]:
    return {
        name: (
            str(row["id"]),
            int(row["size"]),
            base.normalized_md5(row["checksum"]),
        )
        for name, row in entries(record).items()
    }


def snapshot_sha256(value: dict[str, tuple[str, int, str]]) -> str:
    digest = hashlib.sha256()
    for name in sorted(value, key=str.casefold):
        row = value[name]
        digest.update(f"{name}\t{row[0]}\t{row[1]}\t{row[2]}\n".encode())
    return digest.hexdigest().upper()


def text_sha256(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest().upper()


def fetch_public(session, surface: Surface) -> dict:
    record = base.check(
        session.get(
            f"{API}/records/{surface.record_id}",
            headers=MODERN,
            timeout=(30, 300),
        ),
        {200},
    ).json()
    observed = (
        int(record["id"]),
        record.get("pids", {}).get("doi", {}).get("identifier"),
        record.get("parent", {}).get("pids", {}).get("doi", {}).get("identifier"),
        len(entries(record)),
        sum(int(row["size"]) for row in entries(record).values()),
        record.get("files", {}).get("default_preview"),
        record.get("status"),
        record.get("versions", {}).get("is_latest"),
    )
    expected = (
        surface.record_id,
        surface.doi,
        surface.concept_doi,
        surface.files,
        surface.bytes,
        surface.preview,
        "published",
        True,
    )
    if observed != expected:
        raise RuntimeError(f"{surface.key} public boundary changed: {observed!r}")
    return record


def desired_description(value: str) -> str:
    return value.replace(OLD_CONCEPT, NEW_CONCEPT).replace(OLD_VERSION, NEW_VERSION)


def probe_draft(session, token: str, surface: Surface) -> int:
    response = session.get(
        f"{API}/records/{surface.record_id}/draft",
        headers=auth(token),
        timeout=(30, 180),
    )
    if response.status_code == 404:
        return 404
    base.check(response, {200})
    return 200


def validate_description(surface: Surface, before: str, after: str) -> None:
    if OLD_CONCEPT not in before or OLD_VERSION not in before:
        if OLD_CONCEPT not in after and OLD_VERSION not in after and NEW_VERSION in after:
            return
        raise RuntimeError(f"{surface.key} did not contain the expected stale FAC links")
    if (
        OLD_CONCEPT in after
        or OLD_VERSION in after
        or NEW_CONCEPT not in after
        or NEW_VERSION not in after
    ):
        raise RuntimeError(f"{surface.key} FAC cross-link replacement is incomplete")


def preflight(session, token: str) -> dict[str, object]:
    results = []
    for surface in SURFACES:
        record = fetch_public(session, surface)
        description = record["metadata"].get("description", "")
        wanted = desired_description(description)
        validate_description(surface, description, wanted)
        if probe_draft(session, token, surface) != 404:
            raise RuntimeError(f"{surface.key} already has an active edit draft")
        results.append(
            {
                "surface": surface.key,
                "record_id": surface.record_id,
                "doi": surface.doi,
                "concept_doi": surface.concept_doi,
                "files": surface.files,
                "bytes": surface.bytes,
                "default_preview": surface.preview,
                "stale_concept_occurrences": description.count(OLD_CONCEPT),
                "stale_version_occurrences": description.count(OLD_VERSION),
                "mutation_required": wanted != description,
                "active_edit_draft": False,
            }
        )
    return {
        "status": "PASS_READY_FOR_METADATA_ONLY_FAC_CROSSLINK_REPAIR",
        "old_fac_concept": OLD_CONCEPT,
        "old_fac_version": OLD_VERSION,
        "new_fac_concept": NEW_CONCEPT,
        "new_fac_version": NEW_VERSION,
        "surfaces": results,
        "new_record_created": False,
        "new_version_created": False,
        "files_changed": 0,
    }


def apply_one(session, token: str, surface: Surface) -> dict[str, object]:
    before = fetch_public(session, surface)
    before_files = snapshot(before)
    before_description = before["metadata"].get("description", "")
    wanted = desired_description(before_description)
    validate_description(surface, before_description, wanted)
    if wanted == before_description:
        return {
            "status": "PASS_ALREADY_APPLIED",
            "surface": surface.key,
            "record_id": surface.record_id,
        }
    if probe_draft(session, token, surface) != 404:
        raise RuntimeError(f"{surface.key} already has an edit draft")

    draft = base.check(
        session.post(
            f"{API}/records/{surface.record_id}/draft",
            headers=auth(token),
            timeout=(30, 300),
        ),
        {201},
    ).json()
    if int(draft["id"]) != surface.record_id or snapshot(draft) != before_files:
        raise RuntimeError(f"{surface.key} edit draft did not inherit exactly")
    metadata = copy.deepcopy(draft["metadata"])
    metadata["description"] = wanted
    payload = {
        "access": draft["access"],
        "files": {
            "enabled": True,
            "default_preview": before["files"].get("default_preview"),
            "order": before["files"].get("order") or [],
        },
        "metadata": metadata,
        "custom_fields": draft.get("custom_fields", {}),
    }
    if draft.get("pids"):
        payload["pids"] = draft["pids"]
    staged = base.check(
        session.put(
            f"{API}/records/{surface.record_id}/draft",
            headers={**auth(token), "Content-Type": "application/json"},
            json=payload,
            timeout=(30, 600),
        ),
        {200},
    ).json()
    if (
        snapshot(staged) != before_files
        or staged["metadata"].get("description") != wanted
        or staged["metadata"].get("title") != before["metadata"].get("title")
        or staged["files"].get("default_preview")
        != before["files"].get("default_preview")
    ):
        raise RuntimeError(f"{surface.key} staged metadata-only boundary changed")
    base.check(
        session.post(
            f"{API}/records/{surface.record_id}/draft/actions/publish",
            headers=auth(token),
            timeout=(30, 600),
        ),
        {200, 202},
    )

    anonymous = base.make_session()
    after = None
    for _ in range(60):
        candidate = fetch_public(anonymous, surface)
        description = candidate["metadata"].get("description", "")
        if description == wanted:
            after = candidate
            break
        time.sleep(2)
    if after is None:
        raise RuntimeError(f"{surface.key} corrected description did not become public")
    after_files = snapshot(after)
    validate_description(surface, before_description, after["metadata"]["description"])
    if (
        after_files != before_files
        or after["files"].get("order") != before["files"].get("order")
        or after["files"].get("default_preview")
        != before["files"].get("default_preview")
        or after["metadata"].get("title") != before["metadata"].get("title")
        or probe_draft(session, token, surface) != 404
    ):
        raise RuntimeError(f"{surface.key} public metadata-only closeout changed")

    result = {
        "status": "PASS_METADATA_ONLY_FAC_CROSSLINK_REPAIR",
        "surface": surface.key,
        "record_id": surface.record_id,
        "record_url": after["links"]["self_html"],
        "doi": surface.doi,
        "concept_doi": surface.concept_doi,
        "old_fac_concept_absent": OLD_CONCEPT not in after["metadata"]["description"],
        "old_fac_version_absent": OLD_VERSION not in after["metadata"]["description"],
        "new_fac_concept_present": NEW_CONCEPT in after["metadata"]["description"],
        "new_fac_version_present": NEW_VERSION in after["metadata"]["description"],
        "files": len(after_files),
        "bytes": sum(row[1] for row in after_files.values()),
        "file_surface_sha256": snapshot_sha256(after_files),
        "file_identities_unchanged": True,
        "file_order_unchanged": True,
        "default_preview": after["files"].get("default_preview"),
        "default_preview_unchanged": True,
        "title_unchanged": True,
        "description_before_sha256": text_sha256(before_description),
        "description_after_sha256": text_sha256(after["metadata"]["description"]),
        "active_edit_draft": False,
        "new_record_created": False,
        "new_version_created": False,
        "duplicate_concept_created": False,
    }
    receipt = (
        REPO_ROOT
        / "manifests/published-zenodo"
        / f"20260804_fac_crosslink_repair_{surface.key}_record_{surface.record_id}_metadata_readback.json"
    )
    base.save_json(receipt, result)
    return result


def apply(session, token: str) -> dict[str, object]:
    results = [apply_one(session, token, surface) for surface in SURFACES]
    combined = {
        "status": "PASS_CURRENT_FAC_CROSSLINK_REPAIR_ALL_SURFACES",
        "old_fac_concept": OLD_CONCEPT,
        "old_fac_version": OLD_VERSION,
        "new_fac_concept": NEW_CONCEPT,
        "new_fac_version": NEW_VERSION,
        "surfaces": results,
        "files_changed": 0,
        "new_record_created": False,
        "new_version_created": False,
        "duplicate_concept_created": False,
    }
    base.save_json(
        REPO_ROOT
        / "manifests/published-zenodo/20260804_fac_crosslink_repair_combined_receipt.json",
        combined,
    )
    return combined


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=("preflight", "apply"))
    parser.add_argument("--confirm-apply")
    args = parser.parse_args()
    session = base.make_session()
    token = base.find_token()
    if args.action == "preflight":
        result = preflight(session, token)
    else:
        if args.confirm_apply != CONFIRMATION:
            raise RuntimeError(f"Applying requires --confirm-apply {CONFIRMATION}")
        result = apply(session, token)
    print(json.dumps(result, ensure_ascii=True, indent=2), flush=True)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr, flush=True)
        raise
