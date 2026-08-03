#!/usr/bin/env python3
"""Publish current SGA producer/archive log closure on both audit concepts."""

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
from pathlib import Path

import publish_current_reader_bundles_zenodo_20260730 as base


API = base.API
MODERN = {"Accept": "application/vnd.inveniordm.v1+json"}
REPO = Path(__file__).resolve().parents[1]
SOURCE_ROOT = Path(os.environ["SGA_PRESENTATION_CLEAN_SOURCE_ROOT"]).resolve()
CONTROL_ROOT = Path(os.environ["ENGLISH_GERMANIC_CONTROL_ROOT"]).resolve()
TEMP = REPO / "tmp/zenodo/sga-archive-log-closure-dual-doi-20260803"
STATE = TEMP / "state.json"
ZIP_NAME = "SGA_1-7II_PRESENTATION_CLEAN_PROVENANCE_20260803.zip"
MANIFEST_NAME = "SGA_1-7II_PRESENTATION_CLEAN_PROVENANCE_MANIFEST_20260803.csv"
SHARED_LOG_NAME = "ENGLISH_GERMANIC_DECISION_LOG_v1.jsonl"
CONTROL_NAME = "PROJECT_LOGBOOK_METHODOLOGY_REPLICATION_DOI_REQUIREMENT_20260802.md"
CONTROL_SHA256 = "BFA1E3A3EDA94E8C3425BAE50C842610A47D508FB260BF761BA3206883012679"
DECISION_FILES = (
    "ARCHIVE_DECISION_RECORD_SGA_GITHUB_PR257_MERGED_20260803_2025.json",
    "ARCHIVE_DECISION_RECORD_SGA_PRESENTATION_CLEAN_DUAL_DOI_PUBLISHED_20260803_2025.json",
    "ARCHIVE_DECISION_RECORD_SGA_PRIVACY_REMEDIATION_PUBLISHED_20260803_2025.json",
)


@dataclass(frozen=True)
class Target:
    key: str
    predecessor: int
    concept_doi: str
    files: int
    total_bytes: int
    version: str


TARGETS = (
    Target(
        "methodology", 21_778_658, "10.5281/zenodo.21124403", 99, 4_989_453_171,
        "2026-08-03 SGA presentation-clean producer and archive decision-log closure",
    ),
    Target(
        "replication", 21_778_661, "10.5281/zenodo.20461174", 64, 7_854_148,
        "2026-08-03 SGA presentation-clean replication and archive decision-log closure",
    ),
)


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


def file_row(path: Path) -> dict[str, object]:
    return {
        "path": path,
        "bytes": path.stat().st_size,
        "sha256": sha256_path(path),
        "md5": md5_path(path),
    }


def build_provenance() -> tuple[dict[str, dict[str, object]], list[dict[str, object]]]:
    TEMP.mkdir(parents=True, exist_ok=True)
    inputs = [
        ("controls/LOGBOOK_PRIVACY_CLEAN.md", SOURCE_ROOT / "controls/LOGBOOK_PRIVACY_CLEAN.md", "privacy-clean producer logbook", "current R2 producer decision surface"),
        ("controls/DECISION_LOG.csv", SOURCE_ROOT / "controls/DECISION_LOG.csv", "producer decision ledger", "current R2 producer decision surface"),
        ("controls/REVISION_HISTORY.csv", SOURCE_ROOT / "controls/REVISION_HISTORY.csv", "producer revision/reversal history", "current R2 producer decision surface"),
        (f"controls/{CONTROL_NAME}", CONTROL_ROOT / CONTROL_NAME, "controlling dual-DOI provenance requirement", "authoritative exact public control"),
        (f"archive/{SHARED_LOG_NAME}", CONTROL_ROOT / SHARED_LOG_NAME, "shared append-only English/Germanic decision log", "current through record 477"),
    ]
    for name in DECISION_FILES:
        inputs.append((f"archive/{name}", CONTROL_ROOT / name, "archive decision/error/reversal record", "bound in shared log through record 477"))
    if inputs[3][1].stat().st_size != 2_296 or sha256_path(inputs[3][1]) != CONTROL_SHA256:
        raise RuntimeError("Authoritative control identity changed")
    if inputs[4][1].stat().st_size != 3_191_133 or sha256_path(inputs[4][1]) != (
        "067EA74FD007F45207E7E8504648FDC4683DB3CCA2ECD9A205299988B545974C"
    ):
        raise RuntimeError("Shared decision-log cursor changed")
    rows = []
    for member, path, role, state in inputs:
        if not path.is_file():
            raise RuntimeError(f"Missing provenance input: {member}")
        rows.append(
            {
                "member_path": member,
                "bytes": path.stat().st_size,
                "sha256": sha256_path(path),
                "role": role,
                "privacy_result": "PASS exact approved public provenance surface",
                "supersession_state": state,
                "source_path": path,
            }
        )
    manifest_path = TEMP / MANIFEST_NAME
    fields = [
        "member_path", "bytes", "sha256", "role", "privacy_result", "supersession_state",
        "methodology_concept_doi", "replication_concept_doi"
    ]
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {key: row[key] for key in fields if key in row}
                | {
                    "methodology_concept_doi": TARGETS[0].concept_doi,
                    "replication_concept_doi": TARGETS[1].concept_doi,
                }
            )
    zip_path = TEMP / ZIP_NAME
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for row in rows:
            info = zipfile.ZipInfo(str(row["member_path"]), date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, Path(row["source_path"]).read_bytes(), compresslevel=9)
        info = zipfile.ZipInfo("MANIFEST.csv", date_time=(1980, 1, 1, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o100644 << 16
        archive.writestr(info, manifest_path.read_bytes(), compresslevel=9)
    with zipfile.ZipFile(zip_path) as archive:
        wanted = [str(row["member_path"]) for row in rows] + ["MANIFEST.csv"]
        if archive.namelist() != wanted:
            raise RuntimeError("Archive-log provenance ZIP boundary changed")
        for row in rows:
            payload = archive.read(str(row["member_path"]))
            observed = len(payload), hashlib.sha256(payload).hexdigest().upper()
            if observed != (int(row["bytes"]), str(row["sha256"])):
                raise RuntimeError(f"Archive-log provenance member changed: {row['member_path']}")
        if archive.read("MANIFEST.csv") != manifest_path.read_bytes():
            raise RuntimeError("Archive-log provenance manifest member changed")
    uploads = {
        ZIP_NAME: file_row(zip_path),
        MANIFEST_NAME: file_row(manifest_path),
        SHARED_LOG_NAME: file_row(CONTROL_ROOT / SHARED_LOG_NAME),
    }
    public_rows = [{key: value for key, value in row.items() if key != "source_path"} for row in rows]
    public_rows.append(
        {
            "member_path": "MANIFEST.csv",
            "bytes": manifest_path.stat().st_size,
            "sha256": sha256_path(manifest_path),
            "role": "self-excluding direct member manifest",
            "privacy_result": "PASS",
            "supersession_state": "current archive-log closure manifest",
        }
    )
    return uploads, public_rows


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


def load_state() -> dict:
    return json.loads(STATE.read_text(encoding="utf-8")) if STATE.is_file() else {"targets": {}}


def save_state(value: dict) -> None:
    base.save_json(STATE, value)


def publish_target(session, token: str, target: Target, uploads: dict, zip_rows: list, state: dict) -> dict:
    auth_legacy = {"Authorization": f"Bearer {token}"}
    auth_modern = {**MODERN, "Authorization": f"Bearer {token}"}
    current = base.check(
        session.get(f"{API}/records/{target.predecessor}?expand=true", headers=MODERN, timeout=(30, 300)), {200}
    ).json()
    current_entries = base.modern_entries(current)
    latest = base.check(session.get(current["links"]["latest"], headers=MODERN, timeout=(30, 300)), {200}).json()
    target_state = state["targets"].get(target.key, {})
    expected_latest = int(target_state.get("published_record", target.predecessor))
    if (
        current.get("is_published") is not True
        or current["parent"]["pids"]["doi"]["identifier"] != target.concept_doi
        or len(current_entries) != target.files
        or sum(int(row["size"]) for row in current_entries.values()) != target.total_bytes
        or int(latest["id"]) != expected_latest
    ):
        raise RuntimeError(f"{target.key} archive-log predecessor guard changed")
    desired = set(current_entries)
    if target_state.get("published_record"):
        record_id = int(target_state["published_record"])
    else:
        probe = session.get(
            f"{API}/records/{target.predecessor}/draft?expand=true", headers=auth_modern, timeout=(30, 300)
        )
        if target_state.get("draft_id"):
            if probe.status_code != 200 or int(probe.json()["id"]) != int(target_state["draft_id"]):
                raise RuntimeError(f"Tracked {target.key} archive-log draft is not active")
            draft_id = int(target_state["draft_id"])
        else:
            if probe.status_code != 404:
                raise RuntimeError(f"Untracked active {target.key} draft exists")
            deposition = base.check(
                session.get(f"{API}/deposit/depositions/{target.predecessor}", headers=auth_legacy, timeout=(30, 300)), {200}
            ).json()
            created = base.check(
                session.post(deposition["links"]["newversion"], headers=auth_legacy, timeout=(30, 600)), {201}
            ).json()
            draft = base.check(
                session.get(created["links"]["latest_draft"], headers=auth_legacy, timeout=(30, 300)), {200}
            ).json()
            draft_id = int(draft["id"])
            state["targets"][target.key] = {
                "status": "OPEN_TRACKED_DRAFT", "draft_id": draft_id, "predecessor": target.predecessor
            }
            save_state(state)
            print(f"created tracked {target.key} archive-log draft {draft_id}", flush=True)
        deposition = base.check(
            session.get(f"{API}/deposit/depositions/{draft_id}", headers=auth_legacy, timeout=(30, 300)), {200}
        ).json()
        staged = base.legacy_entries(deposition)
        for name, row in uploads.items():
            if name in staged:
                observed = int(staged[name]["filesize"]), base.normalized_md5(staged[name]["checksum"])
                wanted = int(row["bytes"]), str(row["md5"])
                if observed == wanted:
                    continue
                base.check(session.delete(staged[name]["links"]["self"], headers=auth_legacy, timeout=(30, 300)), {204})
            upload_file(session, token, deposition["links"]["bucket"], name, Path(row["path"]))
        draft = base.check(
            session.get(f"{API}/records/{draft_id}/draft?expand=true", headers=auth_modern, timeout=(30, 300)), {200}
        ).json()
        entries = base.modern_entries(draft)
        if set(entries) != desired:
            raise RuntimeError(f"{target.key} archive-log staged boundary changed")
        for name, row in uploads.items():
            if identity(entries[name]) != (int(row["bytes"]), str(row["md5"])):
                raise RuntimeError(f"{target.key} archive-log staged upload changed: {name}")
        for name in desired - set(uploads):
            if identity(entries[name]) != identity(current_entries[name]):
                raise RuntimeError(f"{target.key} archive-log retained object changed: {name}")
        metadata = copy.deepcopy(current["metadata"])
        metadata["publication_date"] = "2026-08-03"
        metadata["version"] = target.version
        metadata["description"] = current["metadata"]["description"]
        metadata.pop("additional_descriptions", None)
        predecessor_order = current["files"].get("order") or sorted(current_entries, key=str.casefold)
        payload = {
            "access": current["access"],
            "files": {
                "enabled": True,
                "default_preview": current["files"].get("default_preview"),
                "order": predecessor_order,
            },
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
            or patched["files"].get("default_preview") != current["files"].get("default_preview")
        ):
            raise RuntimeError(f"{target.key} archive-log presentation patch changed")
        published = base.check(
            session.post(patched["links"]["publish"], headers=auth_modern, timeout=(30, 1200)), {200, 202}
        ).json()
        record_id = int(published["id"])
        state["targets"][target.key].update(
            {"status": "PUBLISHED_READBACK_PENDING", "published_record": record_id}
        )
        save_state(state)
        print(f"published {target.key} archive-log record {record_id}", flush=True)
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
        raise RuntimeError(f"{target.key} archive-log successor did not become public")
    entries = base.modern_entries(record)
    readback = {}
    for name, row in uploads.items():
        observed = stream_readback(session, entries[name]["links"]["content"])
        wanted = int(row["bytes"]), str(row["sha256"])
        readback[name] = {
            "bytes": observed[0], "sha256": observed[1], "match": observed == wanted,
            "content_url": entries[name]["links"]["content"],
        }
        if observed != wanted:
            raise RuntimeError(f"{target.key} archive-log readback changed: {name}")
    response = base.check(session.get(entries[ZIP_NAME]["links"]["content"], timeout=(30, 600)), {200})
    with zipfile.ZipFile(io.BytesIO(response.content)) as archive:
        observed_rows = []
        for name in archive.namelist():
            data = archive.read(name)
            observed_rows.append(
                {"member_path": name, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest().upper()}
            )
    if observed_rows != [
        {"member_path": row["member_path"], "bytes": int(row["bytes"]), "sha256": row["sha256"]}
        for row in zip_rows
    ]:
        raise RuntimeError(f"{target.key} archive-log ZIP member readback changed")
    latest = base.check(session.get(record["links"]["latest"], headers=MODERN, timeout=(30, 300)), {200}).json()
    draft_probe = session.get(f"{API}/records/{record_id}/draft", headers=auth_modern, timeout=(30, 300))
    if int(latest["id"]) != record_id or draft_probe.status_code != 404:
        raise RuntimeError(f"{target.key} archive-log closeout changed")
    result = {
        "status": "PASS_ARCHIVE_LOG_CLOSURE_PUBLISHED_AND_READBACK",
        "target": target.key,
        "record_id": record_id,
        "doi": record["pids"]["doi"]["identifier"],
        "concept_doi": target.concept_doi,
        "predecessor_record": target.predecessor,
        "files": len(entries),
        "bytes": sum(int(row["size"]) for row in entries.values()),
        "landing_description_unchanged": True,
        "raw_public_readback": readback,
        "zip_member_readback": observed_rows,
        "active_draft": False,
        "duplicate_concept": False,
    }
    receipt = REPO / "manifests/published-zenodo" / (
        f"20260803_sga_archive_log_closure_{target.key}_record_{record_id}_public_readback.json"
    )
    base.save_json(receipt, result)
    state["targets"][target.key].update(
        {"status": "CLOSED_PUBLIC_READBACK_PASS", "receipt": receipt.relative_to(REPO).as_posix()}
    )
    save_state(state)
    return result


def main() -> None:
    uploads, zip_rows = build_provenance()
    session = base.make_session()
    token = base.find_token()
    state = load_state()
    results = [publish_target(session, token, target, uploads, zip_rows, state) for target in TARGETS]
    state["status"] = "CLOSED_BOTH_PUBLIC_READBACK_PASS"
    save_state(state)
    print(json.dumps({"status": state["status"], "results": results}, indent=2), flush=True)


if __name__ == "__main__":
    main()
