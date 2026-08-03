#!/usr/bin/env python3
"""Guarded same-concept Zenodo publisher for the provisional SGA global reader."""

from __future__ import annotations

import argparse
import copy
import datetime as dt
import hashlib
import json
import shutil
import time
import urllib.parse
import zipfile
from pathlib import Path

import build_sga_global_reader_provisional_archive_20260803 as package_builder
import publish_current_reader_bundles_zenodo_20260730 as base


API = base.API
REPO_ROOT = Path(__file__).resolve().parents[1]
SPEC_PATH = (
    REPO_ROOT
    / "manifests/zenodo-active-custody/"
    "sga-global-reader-provisional-20260803-r1/release_spec.json"
)
STATE_PATH = (
    REPO_ROOT
    / "tmp/zenodo/sga-global-reader-provisional-20260803-r1/draft_state.json"
)
READBACK_ROOT = (
    REPO_ROOT
    / "tmp/zenodo/sga-global-reader-provisional-20260803-r1/public-readback"
)
RECEIPT_ROOT = REPO_ROOT / "manifests/published-zenodo"
RECEIPT_TAG = "20260803_sga_global_reader_provisional_r3"
MODERN_HEADERS = {"Accept": "application/vnd.inveniordm.v1+json"}


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace(
        "+00:00", "Z"
    )


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest().upper()


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def md5_path(path: Path) -> str:
    digest = hashlib.md5(usedforsecurity=False)
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().lower()


def normalized_inventory(entries: dict[str, dict]) -> list[dict[str, object]]:
    rows = [
        {
            "name": name,
            "bytes": int(entry["size"]),
            "md5": base.normalized_md5(entry["checksum"]),
            "zenodo_file_id": str(entry["id"]),
        }
        for name, entry in entries.items()
    ]
    return sorted(rows, key=lambda row: str(row["name"]).casefold())


def inventory_sha256(rows: list[dict[str, object]]) -> str:
    raw = json.dumps(
        rows, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("utf-8")
    return sha256_bytes(raw)


def inventory_map(entries: dict[str, dict]) -> dict[str, dict[str, object]]:
    return {str(row["name"]): row for row in normalized_inventory(entries)}


def modern_record(session, record_id: int) -> dict:
    return base.check(
        session.get(
            f"{API}/records/{record_id}?expand=true",
            headers=MODERN_HEADERS,
            timeout=(30, 180),
        ),
        {200},
    ).json()


def load_spec() -> tuple[dict, dict[str, dict[str, object]]]:
    spec = json.loads(SPEC_PATH.read_text(encoding="utf-8"))
    if spec.get("schema") != "zenodo-sga-single-concept-release-spec-v1":
        raise RuntimeError("Unexpected SGA release-spec schema")
    if spec.get("publication_date") != "2026-08-03":
        raise RuntimeError("Unexpected publication date")
    target = spec["target"]
    if (
        int(target["concept_id"]),
        str(target["concept_doi"]),
        int(target["predecessor_record"]),
        str(target["predecessor_doi"]),
        str(target["file_policy"]),
    ) != (
        20_410_947,
        "10.5281/zenodo.20410947",
        21_762_813,
        "10.5281/zenodo.21762813",
        "ADD_ONLY_PRESERVE_ALL_PREDECESSOR_OBJECTS",
    ):
        raise RuntimeError("SGA target identity or file policy changed")
    if spec.get("duplicate_concept_authorized") is not False or spec.get(
        "target_parallel_draft_authorized"
    ) is not False:
        raise RuntimeError("Release specification authorizes an unsafe target")

    manifest_guard = spec["upload_manifest"]
    manifest_path = (SPEC_PATH.parent / manifest_guard["path"]).resolve()
    if (manifest_path.stat().st_size, sha256_path(manifest_path)) != (
        int(manifest_guard["bytes"]),
        str(manifest_guard["sha256"]),
    ):
        raise RuntimeError("Upload-manifest identity changed")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("target_concept_doi") != target["concept_doi"]:
        raise RuntimeError("Upload manifest escaped the target concept")
    rows = manifest.get("files") or []
    names = [str(row["name"]) for row in rows]
    if len(rows) != 8 or len(names) != len(set(names)):
        raise RuntimeError("Upload manifest must contain eight unique files")
    uploads: dict[str, dict[str, object]] = {}
    for row in rows:
        name = str(row["name"])
        if Path(name).name != name or row.get("privacy_clean") is not True:
            raise RuntimeError(f"Unsafe upload row: {name}")
        path = (manifest_path.parent / str(row["path"])).resolve()
        try:
            path.relative_to(REPO_ROOT)
        except ValueError as exc:
            raise RuntimeError(f"Upload path escaped the repository: {name}") from exc
        observed = (path.stat().st_size, sha256_path(path), md5_path(path))
        expected = (
            int(row["bytes"]),
            str(row["sha256"]),
            str(row["md5"]).lower(),
        )
        if observed != expected:
            raise RuntimeError(f"Local upload identity changed: {name}")
        uploads[name] = {**row, "path": path}
    if (
        len(uploads),
        sum(int(row["bytes"]) for row in uploads.values()),
    ) != (
        int(manifest_guard["file_count"]),
        int(manifest_guard["total_bytes"]),
    ):
        raise RuntimeError("Upload-manifest aggregate changed")

    github_guard = spec["github_readback"]
    github_path = (SPEC_PATH.parent / github_guard["path"]).resolve()
    if (github_path.stat().st_size, sha256_path(github_path)) != (
        int(github_guard["bytes"]),
        str(github_guard["sha256"]),
    ):
        raise RuntimeError("GitHub-readback receipt identity changed")
    github = json.loads(github_path.read_text(encoding="utf-8"))
    if (
        github.get("status"),
        github.get("commit"),
        int(github.get("changed_file_count", -1)),
    ) != (
        github_guard["status"],
        spec["github_package_commit"],
        int(github_guard["changed_files"]),
    ):
        raise RuntimeError("GitHub commit readback is not closed")
    package_prefix = (
        "sources/sga/sga1-7ii-global-reader-provisional-20260803-r1/"
    )
    for name, row in uploads.items():
        readback = github["files"].get(package_prefix + name)
        if (
            readback is None
            or readback.get("match") is not True
            or (int(readback["bytes"]), str(readback["sha256"]))
            != (int(row["bytes"]), str(row["sha256"]))
        ):
            raise RuntimeError(f"GitHub upload identity is not exact: {name}")

    zip_result = package_builder.verify_zip(package_builder.load_manifest())
    zip_row = uploads[package_builder.ZIP_NAME]
    if (
        zip_result["zip"]["bytes"],
        zip_result["zip"]["sha256"],
        zip_result["zip"]["members"],
        zip_result["zip"]["uncompressed_bytes"],
        zip_result["zip"]["inventory_sha256"],
    ) != (
        int(zip_row["bytes"]),
        str(zip_row["sha256"]),
        int(zip_row["zip_member_count"]),
        int(zip_row["zip_uncompressed_bytes"]),
        str(zip_row["zip_inventory_sha256"]),
    ):
        raise RuntimeError("Local transport-ZIP boundary changed")
    return spec, uploads


def fetch_predecessor(session, spec: dict) -> tuple[dict, dict[str, dict]]:
    target = spec["target"]
    record_id = int(target["predecessor_record"])
    latest = base.check(
        session.get(
            f"{API}/records/{record_id}/versions/latest", timeout=(30, 180)
        ),
        {200},
    ).json()
    tracked_state = load_state(spec)
    allowed_latest_ids = {record_id}
    if tracked_state:
        for field in ("draft_id", "record_id"):
            if tracked_state.get(field) is not None:
                allowed_latest_ids.add(int(tracked_state[field]))
    if int(latest["id"]) not in allowed_latest_ids:
        raise RuntimeError(
            f"SGA live head changed to {latest['id']}; rebuild the release guard"
        )
    record = modern_record(session, record_id)
    if (
        record.get("is_published") is not True
        or record["parent"]["pids"]["doi"]["identifier"]
        != target["concept_doi"]
        or record["pids"]["doi"]["identifier"] != target["predecessor_doi"]
        or record["metadata"].get("title") != target["predecessor_title"]
        or record["metadata"].get("version") != target["predecessor_version"]
    ):
        raise RuntimeError("Published SGA predecessor metadata guard changed")
    entries = base.modern_entries(record)
    rows = normalized_inventory(entries)
    if (
        len(rows),
        sum(int(row["bytes"]) for row in rows),
        inventory_sha256(rows),
    ) != (
        int(target["predecessor_file_count"]),
        int(target["predecessor_total_bytes"]),
        target["predecessor_inventory_sha256"],
    ):
        raise RuntimeError("Published SGA predecessor file guard changed")
    return record, entries


def auth_headers(token: str) -> dict[str, str]:
    return {**MODERN_HEADERS, "Authorization": f"Bearer {token}"}


def load_state(spec: dict) -> dict | None:
    if not STATE_PATH.is_file():
        return None
    state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    if (
        state.get("release_id") != spec["release_id"]
        or state.get("release_spec_sha256") != sha256_path(SPEC_PATH)
        or int(state.get("predecessor_record", -1))
        != int(spec["target"]["predecessor_record"])
    ):
        raise RuntimeError("Tracked SGA draft state belongs to another release")
    return state


def target_draft_probe(session, token: str, spec: dict) -> dict[str, object]:
    predecessor = int(spec["target"]["predecessor_record"])
    response = session.get(
        f"{API}/records/{predecessor}/draft",
        headers=auth_headers(token),
        timeout=(30, 180),
    )
    state = load_state(spec)
    if response.status_code == 404:
        if state and not state.get("published"):
            raise RuntimeError("Tracked SGA draft disappeared")
        return {"http_status": 404, "active": False, "tracked": False}
    base.check(response, {200})
    draft = response.json()
    if not state or state.get("published") or int(draft["id"]) != int(
        state["draft_id"]
    ):
        raise RuntimeError("Untracked active SGA target draft exists")
    return {
        "http_status": 200,
        "active": True,
        "tracked": True,
        "draft_id": int(draft["id"]),
    }


def preflight(write_receipt: bool = True) -> dict[str, object]:
    spec, uploads = load_spec()
    session = base.make_session()
    predecessor, entries = fetch_predecessor(session, spec)
    collisions = set(entries) & set(uploads)
    if collisions:
        raise RuntimeError(f"Add-only upload names collide: {sorted(collisions)}")
    target = spec["target"]
    if (
        len(entries) + len(uploads),
        sum(int(entry["size"]) for entry in entries.values())
        + sum(int(row["bytes"]) for row in uploads.values()),
    ) != (int(target["final_file_count"]), int(target["final_total_bytes"])):
        raise RuntimeError("Final SGA file/byte boundary changed")
    token = base.find_token()
    draft = target_draft_probe(session, token, spec)
    result = {
        "status": "PASS_PREFLIGHT",
        "checked_utc": utc_now(),
        "release_id": spec["release_id"],
        "release_spec_bytes": SPEC_PATH.stat().st_size,
        "release_spec_sha256": sha256_path(SPEC_PATH),
        "github_package_commit": spec["github_package_commit"],
        "github_readback": "12/12 exact",
        "concept_doi": target["concept_doi"],
        "predecessor_record": int(target["predecessor_record"]),
        "predecessor_doi": target["predecessor_doi"],
        "predecessor_files": len(entries),
        "predecessor_bytes": sum(int(row["size"]) for row in entries.values()),
        "upload_files": len(uploads),
        "upload_bytes": sum(int(row["bytes"]) for row in uploads.values()),
        "final_files": int(target["final_file_count"]),
        "final_bytes": int(target["final_total_bytes"]),
        "name_collisions": [],
        "file_policy": target["file_policy"],
        "default_preview": target["default_preview"],
        "target_draft": draft,
        "same_concept_only": True,
        "duplicate_concept_created": False,
        "predecessor_title": predecessor["metadata"]["title"],
    }
    if write_receipt:
        base.save_json(SPEC_PATH.parent / "PREPUBLICATION_PREFLIGHT.json", result)
    return result


def verify_inherited(
    current: dict[str, dict], predecessor: dict[str, dict], context: str
) -> None:
    predecessor_map = inventory_map(predecessor)
    for name, wanted in predecessor_map.items():
        entry = current.get(name)
        if entry is None:
            raise RuntimeError(f"{context} lost predecessor file: {name}")
        observed = {
            "name": name,
            "bytes": int(entry.get("size", entry.get("filesize", -1))),
            "md5": base.normalized_md5(entry["checksum"]),
            "zenodo_file_id": str(entry["id"]),
        }
        if observed != wanted:
            raise RuntimeError(f"{context} changed predecessor identity: {name}")


def create_or_resume_draft(
    session, token: str, spec: dict, predecessor_entries: dict[str, dict]
) -> int:
    state = load_state(spec)
    if state:
        if state.get("published"):
            return int(state["record_id"])
        return int(state["draft_id"])
    probe = target_draft_probe(session, token, spec)
    if probe["active"]:
        raise RuntimeError("Refusing to create a parallel SGA draft")
    record_id = int(spec["target"]["predecessor_record"])
    legacy_headers = {"Authorization": f"Bearer {token}"}
    predecessor = base.check(
        session.get(
            f"{API}/deposit/depositions/{record_id}",
            headers=legacy_headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if (
        predecessor.get("state") != "done"
        or not predecessor.get("submitted")
        or not predecessor.get("links", {}).get("newversion")
    ):
        raise RuntimeError("SGA predecessor is not a same-concept versioning base")
    created = base.check(
        session.post(
            predecessor["links"]["newversion"],
            headers=legacy_headers,
            timeout=(30, 300),
        ),
        {201},
    ).json()
    deposition = base.check(
        session.get(
            created["links"]["latest_draft"],
            headers=legacy_headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    inherited = base.legacy_entries(deposition)
    if set(inherited) != set(predecessor_entries):
        raise RuntimeError("New SGA draft did not inherit the predecessor boundary")
    verify_inherited(inherited, predecessor_entries, "new SGA draft")
    draft_id = int(deposition["id"])
    base.save_json(
        STATE_PATH,
        {
            "status": "OPEN_TRACKED_DRAFT",
            "release_id": spec["release_id"],
            "release_spec_sha256": sha256_path(SPEC_PATH),
            "predecessor_record": record_id,
            "draft_id": draft_id,
            "concept_doi": spec["target"]["concept_doi"],
            "github_package_commit": spec["github_package_commit"],
            "published": False,
            "created_utc": utc_now(),
        },
    )
    return draft_id


def upload_file(session, token: str, bucket: str, name: str, path: Path) -> None:
    with path.open("rb") as handle:
        base.check(
            session.put(
                f"{bucket.rstrip('/')}/{urllib.parse.quote(name, safe='')}",
                headers={
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/octet-stream",
                },
                data=handle,
                timeout=(30, 3600),
            ),
            {200, 201},
        )


def desired_metadata(draft: dict, spec: dict) -> dict:
    metadata = copy.deepcopy(draft["metadata"])
    wanted = spec["metadata"]
    metadata["publication_date"] = spec["publication_date"]
    metadata["version"] = wanted["version"]
    addition = wanted["description_append_html"]
    description = str(metadata.get("description") or "").rstrip()
    if addition not in description:
        metadata["description"] = description + "\n" + addition

    subjects = metadata.setdefault("subjects", [])
    existing_subjects = {str(row.get("subject", "")) for row in subjects}
    for subject in wanted["subjects_add"]:
        if subject not in existing_subjects:
            subjects.append({"subject": subject})

    links = metadata.setdefault("related_identifiers", [])
    wanted_link = wanted["related_identifier"]
    if not any(row.get("identifier") == wanted_link["identifier"] for row in links):
        links.append(
            {
                "identifier": wanted_link["identifier"],
                "scheme": wanted_link["scheme"],
                "relation_type": {"id": wanted_link["relation_type"]},
            }
        )

    notes_append = wanted["notes_append_html"]
    descriptions = metadata.setdefault("additional_descriptions", [])
    note_rows = [
        row
        for row in descriptions
        if (row.get("type") or {}).get("id") == "notes"
    ]
    if note_rows:
        if notes_append not in str(note_rows[0].get("description") or ""):
            note_rows[0]["description"] = (
                str(note_rows[0].get("description") or "").rstrip()
                + "\n"
                + notes_append
            )
    else:
        descriptions.append(
            {"description": notes_append, "type": {"id": "notes"}}
        )
    return metadata


def stage_and_publish(
    session,
    token: str,
    spec: dict,
    uploads: dict[str, dict[str, object]],
    predecessor_entries: dict[str, dict],
    draft_id: int,
) -> dict:
    state = load_state(spec)
    if state and state.get("published"):
        return modern_record(session, int(state["record_id"]))
    legacy_headers = {"Authorization": f"Bearer {token}"}
    deposition = base.check(
        session.get(
            f"{API}/deposit/depositions/{draft_id}",
            headers=legacy_headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    staged = base.legacy_entries(deposition)
    if not set(predecessor_entries).issubset(staged) or not set(staged).issubset(
        set(predecessor_entries) | set(uploads)
    ):
        raise RuntimeError("Tracked SGA draft boundary changed")
    verify_inherited(staged, predecessor_entries, "tracked SGA draft")
    for name in set(staged) & set(uploads):
        observed = (
            int(staged[name]["filesize"]),
            base.normalized_md5(staged[name]["checksum"]),
        )
        wanted = (int(uploads[name]["bytes"]), str(uploads[name]["md5"]))
        if observed != wanted:
            raise RuntimeError(f"Tracked SGA staged identity changed: {name}")
    bucket = deposition["links"]["bucket"]
    missing = [name for name in uploads if name not in staged]
    for index, name in enumerate(missing, start=1):
        print(f"UPLOAD {index}/{len(missing)} {name}", flush=True)
        upload_file(
            session, token, bucket, name, Path(uploads[name]["path"])
        )

    headers = auth_headers(token)
    draft = base.check(
        session.get(
            f"{API}/records/{draft_id}/draft?expand=true",
            headers=headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    entries = base.modern_entries(draft)
    expected_names = set(predecessor_entries) | set(uploads)
    if set(entries) != expected_names or len(entries) != int(
        spec["target"]["final_file_count"]
    ):
        raise RuntimeError("Staged SGA final file boundary changed")
    verify_inherited(entries, predecessor_entries, "staged SGA final draft")
    for name, row in uploads.items():
        observed = (
            int(entries[name]["size"]),
            base.normalized_md5(entries[name]["checksum"]),
        )
        if observed != (int(row["bytes"]), str(row["md5"])):
            raise RuntimeError(f"Staged SGA upload identity changed: {name}")

    current_order = [
        name for name in draft["files"].get("order", []) if name in expected_names
    ]
    order = list(dict.fromkeys(current_order))
    for name in sorted(expected_names - set(order), key=str.casefold):
        order.append(name)
    payload = {
        "access": draft["access"],
        "files": {
            "enabled": True,
            "default_preview": spec["target"]["default_preview"],
            "order": order,
        },
        "metadata": desired_metadata(draft, spec),
        "custom_fields": draft.get("custom_fields", {}),
    }
    if draft.get("pids"):
        payload["pids"] = draft["pids"]
    patched = base.check(
        session.put(
            f"{API}/records/{draft_id}/draft",
            headers={**headers, "Content-Type": "application/json"},
            json=payload,
            timeout=(30, 300),
        ),
        {200},
    ).json()
    if (
        set(base.modern_entries(patched)) != expected_names
        or patched["files"].get("default_preview")
        != spec["target"]["default_preview"]
        or patched["metadata"].get("version") != spec["metadata"]["version"]
        or patched["parent"]["pids"]["doi"]["identifier"]
        != spec["target"]["concept_doi"]
    ):
        raise RuntimeError("Patched SGA draft controls changed")
    base.save_json(
        RECEIPT_ROOT / f"{RECEIPT_TAG}_record_{draft_id}_draft_files.json",
        {
            "status": "PASS_STAGED",
            "checked_utc": utc_now(),
            "release_id": spec["release_id"],
            "predecessor_record": spec["target"]["predecessor_record"],
            "draft_id": draft_id,
            "concept_doi": spec["target"]["concept_doi"],
            "files": len(entries),
            "retained_files": len(predecessor_entries),
            "added_files": len(uploads),
            "replaced_files": [],
            "default_preview": spec["target"]["default_preview"],
            "duplicate_concept_created": False,
            "uploads": {
                name: {
                    "bytes": int(row["bytes"]),
                    "sha256": row["sha256"],
                    "md5": row["md5"],
                }
                for name, row in uploads.items()
            },
        },
    )
    published = base.check(
        session.post(
            patched["links"]["publish"], headers=headers, timeout=(30, 900)
        ),
        {200, 202},
    ).json()
    if (
        int(published["id"]) != draft_id
        or published["parent"]["pids"]["doi"]["identifier"]
        != spec["target"]["concept_doi"]
    ):
        raise RuntimeError("Published SGA successor escaped the concept")
    state = load_state(spec) or {}
    state.update(
        {
            "status": "PUBLISHED_READBACK_PENDING",
            "published": True,
            "record_id": draft_id,
            "record_doi": published["pids"]["doi"]["identifier"],
            "published_utc": utc_now(),
        }
    )
    base.save_json(STATE_PATH, state)
    base.save_json(
        RECEIPT_ROOT / f"{RECEIPT_TAG}_record_{draft_id}_publish_response.json",
        {
            "status": "PUBLISHED_READBACK_PENDING",
            "record_id": draft_id,
            "doi": published["pids"]["doi"]["identifier"],
            "concept_doi": published["parent"]["pids"]["doi"]["identifier"],
            "published_utc": state["published_utc"],
        },
    )
    return published


def stream_readback(session, url: str, target: Path) -> tuple[int, str]:
    response = base.check(
        session.get(url, stream=True, timeout=(30, 900)),
        {200},
    )
    target.parent.mkdir(parents=True, exist_ok=True)
    digest = hashlib.sha256()
    size = 0
    with target.open("wb") as handle:
        for chunk in response.iter_content(1024 * 1024):
            if not chunk:
                continue
            handle.write(chunk)
            digest.update(chunk)
            size += len(chunk)
    return size, digest.hexdigest().upper()


def verify_zip_readback(path: Path, upload_row: dict[str, object]) -> dict:
    expected_names = package_builder.ordered_members(package_builder.load_manifest())
    rows: list[dict[str, object]] = []
    with zipfile.ZipFile(path) as archive:
        if archive.namelist() != expected_names:
            raise RuntimeError("Public ZIP member boundary changed")
        for name in expected_names:
            digest = hashlib.sha256()
            size = 0
            with archive.open(name) as handle:
                for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                    size += len(chunk)
                    digest.update(chunk)
            direct = package_builder.PACKAGE_ROOT / name
            expected = (direct.stat().st_size, sha256_path(direct))
            observed = (size, digest.hexdigest().upper())
            if observed != expected:
                raise RuntimeError(f"Public ZIP member changed: {name}")
            rows.append({"name": name, "bytes": size, "sha256": observed[1]})
    canonical = json.dumps(
        rows, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("utf-8")
    result = {
        "status": "PASS",
        "members": len(rows),
        "uncompressed_bytes": sum(int(row["bytes"]) for row in rows),
        "inventory_sha256": sha256_bytes(canonical),
        "member_readback": rows,
    }
    if (
        result["members"],
        result["uncompressed_bytes"],
        result["inventory_sha256"],
    ) != (
        int(upload_row["zip_member_count"]),
        int(upload_row["zip_uncompressed_bytes"]),
        str(upload_row["zip_inventory_sha256"]),
    ):
        raise RuntimeError("Public ZIP aggregate changed")
    return result


def public_readback(
    session,
    token: str,
    spec: dict,
    uploads: dict[str, dict[str, object]],
    predecessor_entries: dict[str, dict],
    record_id: int,
) -> dict[str, object]:
    record = None
    for attempt in range(12):
        response = session.get(
            f"{API}/records/{record_id}?expand=true",
            headers=MODERN_HEADERS,
            timeout=(30, 180),
        )
        if response.status_code == 200 and response.json().get("is_published"):
            record = response.json()
            break
        if attempt == 11:
            base.check(response, {200})
        time.sleep(min(2 + attempt, 10))
    if record is None:
        raise RuntimeError("Published SGA record did not become anonymously visible")
    entries = base.modern_entries(record)
    expected_names = set(predecessor_entries) | set(uploads)
    if set(entries) != expected_names or len(entries) != int(
        spec["target"]["final_file_count"]
    ):
        raise RuntimeError("Public SGA record file boundary changed")
    verify_inherited(entries, predecessor_entries, "public SGA successor")
    if (
        record["parent"]["pids"]["doi"]["identifier"]
        != spec["target"]["concept_doi"]
        or record["metadata"].get("version") != spec["metadata"]["version"]
        or record["files"].get("default_preview")
        != spec["target"]["default_preview"]
    ):
        raise RuntimeError("Public SGA record metadata boundary changed")

    if READBACK_ROOT.exists():
        resolved = READBACK_ROOT.resolve()
        expected_parent = (REPO_ROOT / "tmp/zenodo").resolve()
        try:
            resolved.relative_to(expected_parent)
        except ValueError as exc:
            raise RuntimeError("Refusing readback cleanup outside repository tmp") from exc
        shutil.rmtree(READBACK_ROOT)
    READBACK_ROOT.mkdir(parents=True)
    file_receipts: dict[str, dict[str, object]] = {}
    for index, (name, row) in enumerate(uploads.items(), start=1):
        print(f"READBACK {index}/{len(uploads)} {name}", flush=True)
        url = entries[name]["links"]["content"]
        target = READBACK_ROOT / name
        observed = stream_readback(session, url, target)
        expected = (int(row["bytes"]), str(row["sha256"]))
        if observed != expected:
            raise RuntimeError(f"Public SGA readback changed: {name}")
        file_receipts[name] = {
            "bytes": observed[0],
            "sha256": observed[1],
            "url": url,
            "match": True,
            "readback_mode": "anonymous_full_download_exact_sha256",
        }

    zip_result = verify_zip_readback(
        READBACK_ROOT / package_builder.ZIP_NAME,
        uploads[package_builder.ZIP_NAME],
    )
    latest = base.check(
        session.get(
            f"{API}/records/{spec['target']['predecessor_record']}/versions/latest",
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if int(latest["id"]) != record_id:
        raise RuntimeError("Published SGA successor is not the concept's latest head")
    draft_response = session.get(
        f"{API}/records/{record_id}/draft",
        headers=auth_headers(token),
        timeout=(30, 180),
    )
    if draft_response.status_code != 404:
        raise RuntimeError("Published SGA successor retains an active draft")

    retained_rows = normalized_inventory(predecessor_entries)
    result = {
        "status": "PASS_PUBLIC_READBACK",
        "checked_utc": utc_now(),
        "release_id": spec["release_id"],
        "record_id": record_id,
        "record_url": f"https://zenodo.org/records/{record_id}",
        "doi": record["pids"]["doi"]["identifier"],
        "concept_doi": record["parent"]["pids"]["doi"]["identifier"],
        "predecessor_record": spec["target"]["predecessor_record"],
        "same_concept_newversion": True,
        "duplicate_concept_created": False,
        "public_files": len(entries),
        "public_bytes": sum(int(entry["size"]) for entry in entries.values()),
        "retained_predecessor_files": len(retained_rows),
        "retained_predecessor_inventory_sha256": inventory_sha256(retained_rows),
        "new_files_read_back": len(file_receipts),
        "new_bytes_read_back": sum(
            int(row["bytes"]) for row in file_receipts.values()
        ),
        "new_file_readback": file_receipts,
        "zip_member_readback": {
            key: value for key, value in zip_result.items() if key != "member_readback"
        },
        "default_preview": record["files"].get("default_preview"),
        "version": record["metadata"].get("version"),
        "latest_head": record_id,
        "active_target_draft_remaining": False,
    }
    base.save_json(
        RECEIPT_ROOT / f"{RECEIPT_TAG}_record_{record_id}_public_readback.json",
        result,
    )
    base.save_json(
        RECEIPT_ROOT
        / f"{RECEIPT_TAG}_record_{record_id}_zip_member_readback.json",
        {**zip_result, "record_id": record_id, "doi": result["doi"]},
    )
    markdown = "\n".join(
        [
            "# Provisional SGA 1--7 II global-reader publication receipt",
            "",
            f"- Record: <https://zenodo.org/records/{record_id}>",
            f"- DOI: `{result['doi']}`",
            f"- Concept DOI: `{result['concept_doi']}`",
            f"- GitHub package commit: `{spec['github_package_commit']}`",
            f"- Predecessor: `{spec['target']['predecessor_doi']}`",
            f"- Public files: {result['public_files']} / {result['public_bytes']:,} bytes",
            f"- Retained predecessor files: {result['retained_predecessor_files']} / identity errors 0",
            f"- New files: {result['new_files_read_back']}/{result['new_files_read_back']} exact anonymous readback / {result['new_bytes_read_back']:,} bytes",
            f"- Reader: 4,185 pages / SHA-256 `{uploads['00z_SGA_1-7II_English_Global_Reader_navigation_r3_PROVISIONAL_20260803.pdf']['sha256']}`",
            f"- Privacy-clean direct logbook: {uploads['10z4_SGA_1-7II_Global_Reader_LOGBOOK_PRIVACY_CLEAN_20260803.md']['bytes']:,} bytes / SHA-256 `{uploads['10z4_SGA_1-7II_Global_Reader_LOGBOOK_PRIVACY_CLEAN_20260803.md']['sha256']}`",
            f"- Transport ZIP: {zip_result['members']} members / SHA-256 `{uploads[package_builder.ZIP_NAME]['sha256']}`",
            "- Scope: PROVISIONAL working checkpoint; not terminal reference-v2 or project completion",
            "- Default preview retained: `00a_SGA1_English_Reader.pdf`",
            "- Duplicate concept created: no",
            "- Active target draft remaining: no",
            "",
        ]
    )
    (RECEIPT_ROOT / f"{RECEIPT_TAG}_record_{record_id}.md").write_text(
        markdown, encoding="utf-8", newline="\n"
    )
    state = load_state(spec) or {}
    state.update(
        {
            "status": "CLOSED_PUBLIC_READBACK_PASS",
            "published": True,
            "record_id": record_id,
            "record_doi": result["doi"],
            "readback_complete": True,
            "closed_utc": result["checked_utc"],
        }
    )
    base.save_json(STATE_PATH, state)
    return result


def publish() -> dict[str, object]:
    preflight(write_receipt=True)
    spec, uploads = load_spec()
    session = base.make_session()
    predecessor, predecessor_entries = fetch_predecessor(session, spec)
    del predecessor
    token = base.find_token()
    draft_id = create_or_resume_draft(
        session, token, spec, predecessor_entries
    )
    published = stage_and_publish(
        session,
        token,
        spec,
        uploads,
        predecessor_entries,
        draft_id,
    )
    return public_readback(
        session,
        token,
        spec,
        uploads,
        predecessor_entries,
        int(published["id"]),
    )


def readback_only(record_id: int) -> dict[str, object]:
    spec, uploads = load_spec()
    session = base.make_session()
    _, predecessor_entries = fetch_predecessor(session, spec)
    token = base.find_token()
    return public_readback(
        session, token, spec, uploads, predecessor_entries, record_id
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--preflight", action="store_true")
    modes.add_argument("--publish", action="store_true")
    modes.add_argument("--readback-only", type=int, metavar="RECORD_ID")
    args = parser.parse_args()
    if args.publish:
        result = publish()
    elif args.readback_only is not None:
        result = readback_only(args.readback_only)
    else:
        result = preflight(write_receipt=True)
    print(
        json.dumps(
            {
                "status": result["status"],
                "release_id": result.get("release_id"),
                "concept_doi": result.get("concept_doi"),
                "predecessor_record": result.get("predecessor_record"),
                "record_id": result.get("record_id"),
                "doi": result.get("doi"),
                "files": result.get("public_files", result.get("final_files")),
                "bytes": result.get("public_bytes", result.get("final_bytes")),
            },
            indent=2,
            ensure_ascii=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
