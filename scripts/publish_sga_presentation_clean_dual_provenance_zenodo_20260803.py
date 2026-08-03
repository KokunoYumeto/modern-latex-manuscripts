#!/usr/bin/env python3
"""Publish the SGA presentation-clean shelf and its dual-DOI provenance."""

from __future__ import annotations

import copy
import csv
import hashlib
import io
import json
import os
import time
import urllib.parse
import zipfile
from dataclasses import dataclass
from pathlib import Path, PurePosixPath

import publish_current_reader_bundles_zenodo_20260730 as base


API = base.API
MODERN = {"Accept": "application/vnd.inveniordm.v1+json"}
REPO = Path(__file__).resolve().parents[1]
HANDOFF_BASE = Path(os.environ["SGA_PRESENTATION_CLEAN_HANDOFF_BASE"]).resolve()
CONTROL_PATH = Path(os.environ["SGA_DUAL_DOI_CONTROL_PATH"]).resolve()
HANDOFF_TABLE = HANDOFF_BASE / (
    "SGA_English_1_7II_presentation_clean_checkpoint_20260803_r2_"
    "ARCHIVE_HANDOFF_FILES.csv"
)
STATE = REPO / "tmp/zenodo/sga-presentation-clean-complete-20260803-r2/state.json"
DERIVED = STATE.parent / "derived-provenance"
PUBLICATION_DATE = "2026-08-03"

PROVENANCE_ZIP = "SGA_1-7II_PRESENTATION_CLEAN_PROVENANCE_20260803.zip"
PROVENANCE_MANIFEST = (
    "SGA_1-7II_PRESENTATION_CLEAN_PROVENANCE_MANIFEST_20260803.csv"
)
OLD_PROVENANCE = {
    "SGA7__COMPLETE_PROVENANCE.zip",
    "SGA7__COMPLETE_PROVENANCE_MANIFEST.csv",
}
CONTROL_NAME = "PROJECT_LOGBOOK_METHODOLOGY_REPLICATION_DOI_REQUIREMENT_20260802.md"
CONTROL_BYTES = 2_296
CONTROL_SHA256 = "BFA1E3A3EDA94E8C3425BAE50C842610A47D508FB260BF761BA3206883012679"


@dataclass(frozen=True)
class Target:
    key: str
    predecessor: int
    concept_doi: str
    files: int
    total_bytes: int
    version: str


TARGETS = {
    "sga": Target(
        "sga",
        21_778_413,
        "10.5281/zenodo.20410947",
        100,
        783_208_002,
        "2026-08-03 presentation-clean complete SGA 1-7 II reader and source shelf",
    ),
    "methodology": Target(
        "methodology",
        21_765_963,
        "10.5281/zenodo.21124403",
        99,
        4_989_661_645,
        "2026-08-03 SGA 1-7 II presentation-clean methodology provenance",
    ),
    "replication": Target(
        "replication",
        21_765_983,
        "10.5281/zenodo.20461174",
        64,
        8_062_622,
        "2026-08-03 SGA 1-7 II presentation-clean replication provenance",
    ),
}


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def md5_path(path: Path) -> str:
    digest = hashlib.md5(usedforsecurity=False)
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().lower()


def identity(entry: dict) -> tuple[int, str]:
    return int(entry["size"]), base.normalized_md5(entry["checksum"])


def local_identity(row: dict) -> tuple[int, str]:
    return int(row["bytes"]), str(row["md5"])


def file_row(path: Path) -> dict[str, object]:
    return {
        "path": path,
        "bytes": path.stat().st_size,
        "sha256": sha256_path(path),
        "md5": md5_path(path),
    }


def safe_member(name: str) -> bool:
    pure = PurePosixPath(name)
    return (
        name == name.replace("\\", "/")
        and not pure.is_absolute()
        and ".." not in pure.parts
        and not (len(name) > 1 and name[1] == ":")
    )


def read_handoff() -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    if HANDOFF_TABLE.stat().st_size != 16_128:
        raise RuntimeError("SGA handoff table byte guard changed")
    if sha256_path(HANDOFF_TABLE) != (
        "2998A1B2B7E8B9D168C715DDB41B557816EB4775B7C1C59A72BF13B80CFF18E0"
    ):
        raise RuntimeError("SGA handoff table hash guard changed")
    with HANDOFF_TABLE.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 36:
        raise RuntimeError(f"Expected 36 handoff rows, found {len(rows)}")
    seen: set[str] = set()
    for row in rows:
        name = row["proposed_public_name"]
        path = Path(row["absolute_local_path"]).resolve()
        if name in seen or not path.is_relative_to(HANDOFF_BASE):
            raise RuntimeError(f"Unsafe or duplicate handoff row: {name}")
        seen.add(name)
        if (
            not path.is_file()
            or path.stat().st_size != int(row["bytes"])
            or sha256_path(path) != row["sha256"].upper()
        ):
            raise RuntimeError(f"Handoff byte identity changed: {name}")
        row["resolved_path"] = str(path)
    sga = [row for row in rows if row["archive_target"].startswith("SGA concept")]
    dual = [row for row in rows if row["archive_target"].startswith("methodology DOI")]
    if len(sga) != 33 or len(dual) != 3:
        raise RuntimeError("Handoff target partition changed")
    if sga[0]["proposed_public_name"] != (
        "00_Current_SGA1-7II_English_Presentation_Clean_Readers_and_"
        "Buildable_Source_20260803.zip"
    ):
        raise RuntimeError("Complete checkpoint ZIP is not first")
    if (
        sga[1]["proposed_public_name"] != "00_SGA_1-7II_English_Global_Reader.pdf"
        or sga[1]["default_preview"].lower() != "true"
    ):
        raise RuntimeError("Clean cumulative reader presentation guard changed")
    expected_dual = {"LOGBOOK_PRIVACY_CLEAN.md", "DECISION_LOG.csv", "REVISION_HISTORY.csv"}
    if {row["proposed_public_name"] for row in dual} != expected_dual:
        raise RuntimeError("Dual-DOI provenance boundary changed")
    return sga, dual


def build_provenance(dual: list[dict[str, str]]) -> dict[str, dict[str, object]]:
    if CONTROL_PATH.name != CONTROL_NAME:
        raise RuntimeError("Dual-DOI control filename changed")
    if CONTROL_PATH.stat().st_size != CONTROL_BYTES or sha256_path(CONTROL_PATH) != CONTROL_SHA256:
        raise RuntimeError("Authoritative dual-DOI control identity changed")
    DERIVED.mkdir(parents=True, exist_ok=True)
    manifest_path = DERIVED / PROVENANCE_MANIFEST
    zip_path = DERIVED / PROVENANCE_ZIP
    members: list[dict[str, object]] = []
    for row in sorted(dual, key=lambda item: int(item["order"])):
        path = Path(row["resolved_path"])
        members.append(
            {
                "member_path": f"controls/{row['proposed_public_name']}",
                "source_path": path,
                "bytes": path.stat().st_size,
                "sha256": sha256_path(path),
                "role": row["role"],
                "privacy_result": "PASS producer privacy-clean; archive exact byte replay",
                "supersession_state": "current immutable SGA presentation-clean checkpoint R2",
            }
        )
    members.append(
        {
            "member_path": f"controls/{CONTROL_NAME}",
            "source_path": CONTROL_PATH,
            "bytes": CONTROL_BYTES,
            "sha256": CONTROL_SHA256,
            "role": "controlling dual-DOI provenance requirement",
            "privacy_result": "PASS authoritative public control identity",
            "supersession_state": "supersedes stale 2242-byte predecessor copy",
        }
    )
    fieldnames = [
        "member_path",
        "bytes",
        "sha256",
        "role",
        "privacy_result",
        "supersession_state",
        "methodology_concept_doi",
        "replication_concept_doi",
    ]
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for row in members:
            writer.writerow(
                {
                    key: row[key] for key in fieldnames if key in row
                }
                | {
                    "methodology_concept_doi": TARGETS["methodology"].concept_doi,
                    "replication_concept_doi": TARGETS["replication"].concept_doi,
                }
            )
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for row in members:
            member_name = str(row["member_path"])
            info = zipfile.ZipInfo(member_name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, Path(row["source_path"]).read_bytes(), compresslevel=9)
        info = zipfile.ZipInfo("MANIFEST.csv", date_time=(1980, 1, 1, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o100644 << 16
        archive.writestr(info, manifest_path.read_bytes(), compresslevel=9)
    with zipfile.ZipFile(zip_path) as archive:
        names = archive.namelist()
        wanted = [str(row["member_path"]) for row in members] + ["MANIFEST.csv"]
        if names != wanted or any(not safe_member(name) for name in names):
            raise RuntimeError("Derived provenance ZIP member boundary changed")
        for row in members:
            payload = archive.read(str(row["member_path"]))
            observed = len(payload), hashlib.sha256(payload).hexdigest().upper()
            if observed != (int(row["bytes"]), str(row["sha256"])):
                raise RuntimeError(f"Derived provenance member changed: {row['member_path']}")
        if archive.read("MANIFEST.csv") != manifest_path.read_bytes():
            raise RuntimeError("Derived provenance manifest member changed")
    return {
        PROVENANCE_ZIP: file_row(zip_path),
        PROVENANCE_MANIFEST: file_row(manifest_path),
        CONTROL_NAME: file_row(CONTROL_PATH),
    }


def load_state() -> dict:
    if not STATE.is_file():
        return {"schema": "sga-presentation-clean-dual-provenance-state-v1", "targets": {}}
    return json.loads(STATE.read_text(encoding="utf-8"))


def save_state(state: dict) -> None:
    base.save_json(STATE, state)


def modern_record(session, record_id: int, token: str | None = None) -> dict:
    headers = dict(MODERN)
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return base.check(
        session.get(f"{API}/records/{record_id}?expand=true", headers=headers, timeout=(30, 300)),
        {200},
    ).json()


def upload_file(session, token: str, bucket: str, name: str, path: Path) -> None:
    print(f"upload {name} ({path.stat().st_size} bytes)", flush=True)
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


def stream_readback(session, url: str) -> tuple[int, str]:
    response = base.check(session.get(url, stream=True, timeout=(30, 1800)), {200})
    digest = hashlib.sha256()
    total = 0
    with response:
        for block in response.iter_content(4 * 1024 * 1024):
            if block:
                digest.update(block)
                total += len(block)
    return total, digest.hexdigest().upper()


def current_guard(session, target: Target) -> tuple[dict, dict[str, dict]]:
    record = modern_record(session, target.predecessor)
    entries = base.modern_entries(record)
    if (
        record.get("is_published") is not True
        or record["parent"]["pids"]["doi"]["identifier"] != target.concept_doi
        or len(entries) != target.files
        or sum(int(row["size"]) for row in entries.values()) != target.total_bytes
    ):
        raise RuntimeError(f"{target.key} predecessor guard changed")
    latest = base.check(
        session.get(record["links"]["latest"], headers=MODERN, timeout=(30, 300)), {200}
    ).json()
    if int(latest["id"]) != target.predecessor:
        raise RuntimeError(f"{target.key} latest head changed")
    return record, entries


def preflight(session, token: str, target: Target, state: dict) -> tuple[dict, dict[str, dict]]:
    record, entries = current_guard(session, target)
    target_state = state["targets"].get(target.key, {})
    if target_state.get("published_record"):
        return record, entries
    probe = session.get(
        f"{API}/records/{target.predecessor}/draft?expand=true",
        headers={**MODERN, "Authorization": f"Bearer {token}"},
        timeout=(30, 300),
    )
    tracked = target_state.get("draft_id")
    if tracked:
        if probe.status_code != 200 or int(probe.json()["id"]) != int(tracked):
            raise RuntimeError(f"Tracked {target.key} draft is not the active draft")
    elif probe.status_code != 404:
        raise RuntimeError(f"Untracked active {target.key} draft exists")
    return record, entries


def create_or_resume_draft(session, token: str, target: Target, state: dict) -> int:
    target_state = state["targets"].get(target.key, {})
    if target_state.get("draft_id"):
        return int(target_state["draft_id"])
    auth = {"Authorization": f"Bearer {token}"}
    deposition = base.check(
        session.get(f"{API}/deposit/depositions/{target.predecessor}", headers=auth, timeout=(30, 300)),
        {200},
    ).json()
    created = base.check(
        session.post(deposition["links"]["newversion"], headers=auth, timeout=(30, 600)),
        {201},
    ).json()
    draft = base.check(
        session.get(created["links"]["latest_draft"], headers=auth, timeout=(30, 300)),
        {200},
    ).json()
    draft_id = int(draft["id"])
    state["targets"][target.key] = {
        "status": "OPEN_TRACKED_DRAFT",
        "draft_id": draft_id,
        "predecessor": target.predecessor,
        "concept_doi": target.concept_doi,
    }
    save_state(state)
    print(f"created tracked {target.key} draft {draft_id}", flush=True)
    return draft_id


def prepare_target(
    target: Target,
    current: dict,
    current_entries: dict[str, dict],
    sga_rows: list[dict[str, str]],
    provenance_uploads: dict[str, dict[str, object]],
) -> tuple[dict[str, dict[str, object]], set[str], list[str], str | None]:
    if target.key == "sga":
        uploads = {
            row["proposed_public_name"]: file_row(Path(row["resolved_path"])) for row in sga_rows
        }
        desired = set(uploads)
        order = [row["proposed_public_name"] for row in sorted(sga_rows, key=lambda item: int(item["order"]))]
        return uploads, desired, order, "00_SGA_1-7II_English_Global_Reader.pdf"
    uploads = provenance_uploads
    desired = (set(current_entries) - OLD_PROVENANCE) | set(uploads)
    predecessor_order = current["files"].get("order") or sorted(current_entries, key=str.casefold)
    order = [name for name in predecessor_order if name in desired and name not in uploads]
    order.extend([PROVENANCE_ZIP, PROVENANCE_MANIFEST, CONTROL_NAME])
    if len(order) != len(desired) or len(set(order)) != len(order):
        raise RuntimeError(f"{target.key} file order does not cover desired set")
    return uploads, desired, order, current["files"].get("default_preview")


def publish_target(
    session,
    token: str,
    target: Target,
    current: dict,
    current_entries: dict[str, dict],
    sga_rows: list[dict[str, str]],
    provenance_uploads: dict[str, dict[str, object]],
    state: dict,
) -> dict:
    target_state = state["targets"].get(target.key, {})
    uploads, desired, order, default_preview = prepare_target(
        target, current, current_entries, sga_rows, provenance_uploads
    )
    if target_state.get("published_record"):
        record_id = int(target_state["published_record"])
    else:
        draft_id = create_or_resume_draft(session, token, target, state)
        auth_legacy = {"Authorization": f"Bearer {token}"}
        auth_modern = {**MODERN, "Authorization": f"Bearer {token}"}
        deposition = base.check(
            session.get(f"{API}/deposit/depositions/{draft_id}", headers=auth_legacy, timeout=(30, 300)),
            {200},
        ).json()
        staged = base.legacy_entries(deposition)
        for name in sorted(set(staged) - desired):
            base.check(
                session.delete(staged[name]["links"]["self"], headers=auth_legacy, timeout=(30, 300)),
                {204},
            )
        deposition = base.check(
            session.get(f"{API}/deposit/depositions/{draft_id}", headers=auth_legacy, timeout=(30, 300)),
            {200},
        ).json()
        staged = base.legacy_entries(deposition)
        for name, row in uploads.items():
            if name in staged:
                observed = int(staged[name]["filesize"]), base.normalized_md5(staged[name]["checksum"])
                if observed == local_identity(row):
                    continue
                base.check(
                    session.delete(staged[name]["links"]["self"], headers=auth_legacy, timeout=(30, 300)),
                    {204},
                )
                staged.pop(name)
            upload_file(session, token, deposition["links"]["bucket"], name, Path(row["path"]))
        draft = base.check(
            session.get(f"{API}/records/{draft_id}/draft?expand=true", headers=auth_modern, timeout=(30, 300)),
            {200},
        ).json()
        draft_entries = base.modern_entries(draft)
        if set(draft_entries) != desired:
            raise RuntimeError(f"{target.key} staged file boundary changed")
        for name, row in uploads.items():
            if identity(draft_entries[name]) != local_identity(row):
                raise RuntimeError(f"{target.key} staged upload identity changed: {name}")
        for name in desired - set(uploads):
            if identity(draft_entries[name]) != identity(current_entries[name]):
                raise RuntimeError(f"{target.key} retained predecessor changed: {name}")
        metadata = copy.deepcopy(current["metadata"])
        metadata["publication_date"] = PUBLICATION_DATE
        metadata["version"] = target.version
        metadata["description"] = current["metadata"]["description"]
        metadata.pop("additional_descriptions", None)
        payload = {
            "access": current["access"],
            "files": {"enabled": True, "default_preview": default_preview, "order": order},
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
                timeout=(30, 600),
            ),
            {200},
        ).json()
        if (
            set(base.modern_entries(patched)) != desired
            or patched["metadata"]["description"] != current["metadata"]["description"]
            or patched["parent"]["pids"]["doi"]["identifier"] != target.concept_doi
            or patched["files"].get("default_preview") != default_preview
        ):
            raise RuntimeError(f"{target.key} patched presentation changed")
        published = base.check(
            session.post(patched["links"]["publish"], headers=auth_modern, timeout=(30, 1200)),
            {200, 202},
        ).json()
        record_id = int(published["id"])
        state["targets"][target.key].update(
            {"status": "PUBLISHED_READBACK_PENDING", "published_record": record_id}
        )
        save_state(state)
        print(f"published {target.key} record {record_id}", flush=True)
    record = None
    for attempt in range(90):
        response = session.get(f"{API}/records/{record_id}?expand=true", headers=MODERN, timeout=(30, 300))
        if response.status_code == 200 and response.json().get("is_published"):
            candidate = response.json()
            if set(base.modern_entries(candidate)) == desired:
                record = candidate
                break
        time.sleep(min(attempt + 1, 5))
    if record is None:
        raise RuntimeError(f"{target.key} successor did not become publicly stable")
    entries = base.modern_entries(record)
    readback: dict[str, dict[str, object]] = {}
    for name, row in uploads.items():
        print(f"readback {target.key} {name}", flush=True)
        observed = stream_readback(session, entries[name]["links"]["content"])
        wanted = int(row["bytes"]), str(row["sha256"])
        readback[name] = {
            "bytes": observed[0],
            "sha256": observed[1],
            "match": observed == wanted,
            "content_url": entries[name]["links"]["content"],
        }
        if observed != wanted:
            raise RuntimeError(f"{target.key} public byte readback changed: {name}")
    for name in desired - set(uploads):
        if identity(entries[name]) != identity(current_entries[name]):
            raise RuntimeError(f"{target.key} public retained identity changed: {name}")
    zip_members = None
    if target.key != "sga":
        response = base.check(session.get(entries[PROVENANCE_ZIP]["links"]["content"], timeout=(30, 300)), {200})
        zip_members = []
        with zipfile.ZipFile(io.BytesIO(response.content)) as archive:
            for name in archive.namelist():
                payload = archive.read(name)
                zip_members.append(
                    {"member_path": name, "bytes": len(payload), "sha256": hashlib.sha256(payload).hexdigest().upper()}
                )
        if len(zip_members) != 5:
            raise RuntimeError(f"{target.key} public provenance ZIP member count changed")
    latest = base.check(
        session.get(record["links"]["latest"], headers=MODERN, timeout=(30, 300)), {200}
    ).json()
    draft_probe = session.get(
        f"{API}/records/{record_id}/draft",
        headers={**MODERN, "Authorization": f"Bearer {token}"},
        timeout=(30, 300),
    )
    if (
        int(latest["id"]) != record_id
        or draft_probe.status_code != 404
        or record["metadata"]["description"] != current["metadata"]["description"]
        or record["files"].get("default_preview") != default_preview
    ):
        raise RuntimeError(f"{target.key} public closeout changed")
    result = {
        "status": "PASS_PUBLISHED_AND_PUBLIC_READBACK",
        "target": target.key,
        "record_id": record_id,
        "doi": record["pids"]["doi"]["identifier"],
        "concept_doi": target.concept_doi,
        "predecessor_record": target.predecessor,
        "files": len(entries),
        "bytes": sum(int(row["size"]) for row in entries.values()),
        "default_preview": default_preview,
        "landing_description_unchanged_whole_project": True,
        "uploaded_files": len(uploads),
        "retained_predecessor_files": len(desired - set(uploads)),
        "predecessor_only_files_preserved_in_version_history": sorted(set(current_entries) - desired),
        "raw_public_readback": readback,
        "provenance_zip_members": zip_members,
        "active_draft": False,
        "duplicate_concept": False,
    }
    receipt = REPO / "manifests/published-zenodo" / (
        f"20260803_sga_presentation_clean_{target.key}_record_{record_id}_public_readback.json"
    )
    base.save_json(receipt, result)
    state["targets"][target.key].update(
        {"status": "CLOSED_PUBLIC_READBACK_PASS", "receipt": receipt.relative_to(REPO).as_posix()}
    )
    save_state(state)
    return result


def main() -> None:
    sga_rows, dual_rows = read_handoff()
    provenance_uploads = build_provenance(dual_rows)
    state = load_state()
    session = base.make_session()
    token = base.find_token()
    contexts: dict[str, tuple[dict, dict[str, dict]]] = {}
    for key, target in TARGETS.items():
        contexts[key] = preflight(session, token, target, state)
    results = []
    for key, target in TARGETS.items():
        current, entries = contexts[key]
        results.append(
            publish_target(
                session,
                token,
                target,
                current,
                entries,
                sga_rows,
                provenance_uploads,
                state,
            )
        )
    state["status"] = "CLOSED_ALL_THREE_PUBLIC_READBACK_PASS"
    save_state(state)
    print(json.dumps({"status": state["status"], "results": results}, indent=2), flush=True)


if __name__ == "__main__":
    main()
