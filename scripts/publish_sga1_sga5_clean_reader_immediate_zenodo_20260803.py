#!/usr/bin/env python3
"""Publish the validated clean SGA1 and SGA5 readers immediately."""

from __future__ import annotations

import copy
import hashlib
import json
import time
import urllib.parse
from pathlib import Path

import build_sga1_sga5_clean_reader_immediate_archive_20260803 as builder
import publish_current_reader_bundles_zenodo_20260730 as base


API = base.API
REPO = Path(__file__).resolve().parents[1]
PAYLOAD = builder.OUTPUT
CURRENT_RECORD = 21778265
CONCEPT_DOI = "10.5281/zenodo.20410947"
CURRENT_FILES = 92
CURRENT_BYTES = 783_417_797
REPLACE = {"00a_SGA1_English_Reader.pdf", "00e_SGA5_English_Reader.pdf"}
DEFAULT_PREVIEW = "00a_SGA1_English_Reader.pdf"
PRIMARY_ZIP = "00_Current_SGA1-7II_English_Readers_and_Buildable_TeX_20260802.zip"
STATE = REPO / "tmp/zenodo/sga1-sga5-clean-reader-immediate-20260803-r1/state.json"
MODERN = {"Accept": "application/vnd.inveniordm.v1+json"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def md5(path: Path) -> str:
    digest = hashlib.md5(usedforsecurity=False)
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().lower()


def save_state(data: dict) -> None:
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def local_uploads() -> dict[str, dict[str, object]]:
    builder.main()
    files = sorted(
        (path for path in PAYLOAD.iterdir() if path.is_file() and path.name != ".gitattributes"),
        key=lambda path: path.name.casefold(),
    )
    if len(files) != 10 or set(path.name for path in files) & REPLACE != REPLACE:
        raise RuntimeError("Immediate clean-reader payload boundary changed")
    return {
        path.name: {
            "path": path,
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
            "md5": md5(path),
        }
        for path in files
    }


def modern_record(session, record_id: int, token: str | None = None) -> dict:
    headers = dict(MODERN)
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return base.check(
        session.get(f"{API}/records/{record_id}?expand=true", headers=headers, timeout=(30, 180)),
        {200},
    ).json()


def identity(entry: dict) -> tuple[int, str]:
    return int(entry["size"]), base.normalized_md5(entry["checksum"])


def upload_file(session, token: str, bucket: str, name: str, path: Path) -> None:
    with path.open("rb") as handle:
        base.check(
            session.put(
                f"{bucket.rstrip('/')}/{urllib.parse.quote(name, safe='')}",
                headers={"Authorization": f"Bearer {token}", "Content-Type": "application/octet-stream"},
                data=handle,
                timeout=(30, 1800),
            ),
            {200, 201},
        )


def desired_order(names: set[str]) -> list[str]:
    english_pdfs = sorted(
        (name for name in names if name.lower().endswith(".pdf") and "english" in name.lower()),
        key=str.casefold,
    )
    other_pdfs = sorted(
        (name for name in names if name.lower().endswith(".pdf") and name not in english_pdfs),
        key=str.casefold,
    )
    tex = sorted((name for name in names if name.lower().endswith(".tex")), key=str.casefold)
    preferred = [PRIMARY_ZIP, *english_pdfs, *other_pdfs, *tex]
    result = [name for name in preferred if name in names]
    result.extend(sorted(names - set(result), key=str.casefold))
    if result[0] != PRIMARY_ZIP:
        raise RuntimeError("Complete shelf ZIP is not first")
    return result


def create_or_resume(session, token: str, current: dict, current_entries: dict[str, dict]) -> int:
    if STATE.is_file():
        state = json.loads(STATE.read_text(encoding="utf-8"))
        return int(state["record_id"] if state.get("published") else state["draft_id"])
    auth_legacy = {"Authorization": f"Bearer {token}"}
    auth_modern = {**MODERN, "Authorization": f"Bearer {token}"}
    probe = session.get(
        f"{API}/records/{CURRENT_RECORD}/draft?expand=true", headers=auth_modern, timeout=(30, 180)
    )
    if probe.status_code != 404:
        raise RuntimeError("Active SGA draft exists; refusing parallel draft")
    deposition = base.check(
        session.get(f"{API}/deposit/depositions/{CURRENT_RECORD}", headers=auth_legacy, timeout=(30, 180)),
        {200},
    ).json()
    created = base.check(
        session.post(deposition["links"]["newversion"], headers=auth_legacy, timeout=(30, 300)),
        {201},
    ).json()
    draft_deposition = base.check(
        session.get(created["links"]["latest_draft"], headers=auth_legacy, timeout=(30, 180)),
        {200},
    ).json()
    inherited = base.legacy_entries(draft_deposition)
    if set(inherited) != set(current_entries):
        raise RuntimeError("Clean-reader draft inheritance boundary changed")
    for name, row in current_entries.items():
        observed = int(inherited[name]["filesize"]), base.normalized_md5(inherited[name]["checksum"])
        if observed != identity(row):
            raise RuntimeError(f"Inherited clean-reader draft identity changed: {name}")
    draft_id = int(draft_deposition["id"])
    save_state(
        {
            "status": "OPEN_TRACKED_DRAFT",
            "draft_id": draft_id,
            "predecessor_record": CURRENT_RECORD,
            "concept_doi": CONCEPT_DOI,
            "published": False,
        }
    )
    return draft_id


def stream_readback(session, url: str) -> tuple[int, str]:
    response = base.check(session.get(url, stream=True, timeout=(30, 900)), {200})
    digest = hashlib.sha256()
    total = 0
    with response:
        for block in response.iter_content(1024 * 1024):
            if block:
                digest.update(block)
                total += len(block)
    return total, digest.hexdigest().upper()


def main() -> None:
    uploads = local_uploads()
    session = base.make_session()
    token = base.find_token()
    auth_legacy = {"Authorization": f"Bearer {token}"}
    auth_modern = {**MODERN, "Authorization": f"Bearer {token}"}
    current = modern_record(session, CURRENT_RECORD)
    current_entries = base.modern_entries(current)
    if (
        current["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI
        or current.get("is_published") is not True
        or len(current_entries) != CURRENT_FILES
        or sum(int(row["size"]) for row in current_entries.values()) != CURRENT_BYTES
        or "Reader-presentation hold" in current["metadata"].get("description", "")
    ):
        raise RuntimeError("Restored SGA predecessor guard changed")
    latest = base.check(session.get(current["links"]["latest"], headers=MODERN, timeout=(30, 180)), {200}).json()
    state = json.loads(STATE.read_text(encoding="utf-8")) if STATE.is_file() else None
    if state and state.get("published"):
        record_id = int(state["record_id"])
    else:
        if int(latest["id"]) != CURRENT_RECORD:
            raise RuntimeError("SGA latest head changed before clean-reader publication")
        draft_id = create_or_resume(session, token, current, current_entries)
        deposition = base.check(
            session.get(f"{API}/deposit/depositions/{draft_id}", headers=auth_legacy, timeout=(30, 180)),
            {200},
        ).json()
        staged = base.legacy_entries(deposition)
        allowed = (set(current_entries) - REPLACE) | set(uploads)
        if not set(staged).issubset(set(current_entries) | set(uploads)):
            raise RuntimeError("Tracked clean-reader draft contains an untracked file")
        for name in sorted(REPLACE & set(staged)):
            base.check(
                session.delete(staged[name]["links"]["self"], headers=auth_legacy, timeout=(30, 300)),
                {204},
            )
        deposition = base.check(
            session.get(f"{API}/deposit/depositions/{draft_id}", headers=auth_legacy, timeout=(30, 180)),
            {200},
        ).json()
        staged = base.legacy_entries(deposition)
        bucket = deposition["links"]["bucket"]
        for name, row in uploads.items():
            if name in staged:
                observed = int(staged[name]["filesize"]), base.normalized_md5(staged[name]["checksum"])
                if observed != (int(row["bytes"]), str(row["md5"])):
                    raise RuntimeError(f"Staged clean-reader upload differs: {name}")
                continue
            upload_file(session, token, bucket, name, Path(row["path"]))

        draft = base.check(
            session.get(f"{API}/records/{draft_id}/draft?expand=true", headers=auth_modern, timeout=(30, 180)),
            {200},
        ).json()
        entries = base.modern_entries(draft)
        expected = (set(current_entries) - REPLACE) | set(uploads)
        if set(entries) != expected or len(entries) != 100:
            raise RuntimeError("Final clean-reader draft boundary changed")
        for name in set(current_entries) - REPLACE:
            if identity(entries[name]) != identity(current_entries[name]):
                raise RuntimeError(f"Retained predecessor identity changed: {name}")
        for name, row in uploads.items():
            if identity(entries[name]) != (int(row["bytes"]), str(row["md5"])):
                raise RuntimeError(f"Final clean-reader upload identity changed: {name}")

        metadata = copy.deepcopy(current["metadata"])
        metadata["publication_date"] = "2026-08-03"
        metadata["version"] = "2026-08-03 complete SGA 1-7 II reader shelf, clean reader revision"
        metadata["description"] = current["metadata"]["description"]
        metadata.pop("additional_descriptions", None)
        order = desired_order(set(entries))
        payload = {
            "access": current["access"],
            "files": {"enabled": True, "default_preview": DEFAULT_PREVIEW, "order": order},
            "metadata": metadata,
            "custom_fields": current.get("custom_fields", {}),
        }
        if draft.get("pids"):
            payload["pids"] = draft["pids"]
        patched = base.check(
            session.put(
                f"{API}/records/{draft_id}/draft",
                headers={**auth_modern, "Content-Type": "application/json"},
                json=payload,
                timeout=(30, 300),
            ),
            {200},
        ).json()
        if (
            set(base.modern_entries(patched)) != expected
            or patched["files"].get("default_preview") != DEFAULT_PREVIEW
            or patched["metadata"].get("description") != current["metadata"]["description"]
            or patched["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI
        ):
            raise RuntimeError("Patched clean-reader presentation changed")
        published = base.check(
            session.post(patched["links"]["publish"], headers=auth_modern, timeout=(30, 900)),
            {200, 202},
        ).json()
        record_id = int(published["id"])
        save_state(
            {
                "status": "PUBLISHED_READBACK_PENDING",
                "record_id": record_id,
                "doi": published["pids"]["doi"]["identifier"],
                "predecessor_record": CURRENT_RECORD,
                "concept_doi": CONCEPT_DOI,
                "published": True,
            }
        )

    record = None
    for attempt in range(60):
        response = session.get(f"{API}/records/{record_id}?expand=true", headers=MODERN, timeout=(30, 180))
        if response.status_code == 200 and response.json().get("is_published"):
            candidate = response.json()
            if len(base.modern_entries(candidate)) == 100:
                record = candidate
                break
        time.sleep(min(1 + attempt, 5))
    if record is None:
        raise RuntimeError("Clean-reader successor did not become public")
    entries = base.modern_entries(record)
    expected = (set(current_entries) - REPLACE) | set(uploads)
    if set(entries) != expected:
        raise RuntimeError("Public clean-reader file boundary changed")
    for name in set(current_entries) - REPLACE:
        if identity(entries[name]) != identity(current_entries[name]):
            raise RuntimeError(f"Public retained identity changed: {name}")
    readback: dict[str, dict[str, object]] = {}
    for name, row in uploads.items():
        observed = stream_readback(session, entries[name]["links"]["content"])
        wanted = int(row["bytes"]), str(row["sha256"])
        readback[name] = {"bytes": observed[0], "sha256": observed[1], "match": observed == wanted}
        if observed != wanted:
            raise RuntimeError(f"Public clean-reader byte readback changed: {name}")
    latest = base.check(session.get(record["links"]["latest"], headers=MODERN, timeout=(30, 180)), {200}).json()
    draft_probe = session.get(
        f"{API}/records/{record_id}/draft", headers=auth_modern, timeout=(30, 180)
    )
    if (
        int(latest["id"]) != record_id
        or record["files"].get("default_preview") != DEFAULT_PREVIEW
        or record["metadata"].get("description") != current["metadata"]["description"]
        or draft_probe.status_code != 404
    ):
        raise RuntimeError("Public clean-reader closeout changed")
    result = {
        "status": "PASS_PUBLISHED_CLEAN_READERS",
        "record_id": record_id,
        "doi": record["pids"]["doi"]["identifier"],
        "concept_doi": CONCEPT_DOI,
        "predecessor_record": CURRENT_RECORD,
        "files": len(entries),
        "bytes": sum(int(row["size"]) for row in entries.values()),
        "retained_predecessor_files": len(set(current_entries) - REPLACE),
        "replaced_reader_files": sorted(REPLACE),
        "added_external_provenance_files": sorted(set(uploads) - REPLACE),
        "default_preview": DEFAULT_PREVIEW,
        "landing_description_unchanged_whole_project": True,
        "raw_public_readback": readback,
        "active_draft": False,
        "duplicate_concept": False,
    }
    receipt = REPO / "manifests/published-zenodo" / f"20260803_sga1_sga5_clean_readers_record_{record_id}_public_readback.json"
    base.save_json(receipt, result)
    state = json.loads(STATE.read_text(encoding="utf-8"))
    state.update({"status": "CLOSED_PUBLIC_READBACK_PASS", "readback_complete": True})
    save_state(state)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
