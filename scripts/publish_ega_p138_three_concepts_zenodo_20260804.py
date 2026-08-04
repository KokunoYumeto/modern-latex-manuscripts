#!/usr/bin/env python3
"""Publish the exact EGA I p.138 successor on three existing DOI lineages.

The operation is deliberately constrained to the existing EGA, methodology,
and replication concepts.  It cannot mint a concept.  ``preflight`` is
read-only on Zenodo; ``prepare`` creates one tracked successor draft per
concept; ``publish`` stages, validates, publishes, and anonymously reads back
every new direct byte and all 172 members of the p.138 source ZIP.

The methodology head is already at Zenodo's 100-file ceiling.  Ten machine-
only companion files therefore move from direct presentation into one indexed
deterministic ZIP.  Their exact predecessor bytes remain available in the new
ZIP and in immutable predecessor record 21782511.  No human logbook, decision
or reversal history, continuation record, rights note, or reader is compacted.
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time
import urllib.parse
import zipfile
from dataclasses import dataclass
from pathlib import Path, PurePosixPath

import publish_current_reader_bundles_zenodo_20260730 as base


API = base.API
MODERN = {"Accept": "application/vnd.inveniordm.v1+json"}
REPO = Path(__file__).resolve().parents[1]
PACKAGE_ROOT = REPO / "sources/ega/checkpoints/ega1-p138-diplomatic-prestacks-r1-20260804"
UPLOAD_MANIFEST = PACKAGE_ROOT / "14_ZENODO_UPLOAD_MANIFEST.csv"
PACKAGE_VALIDATION = PACKAGE_ROOT / "15_PACKAGE_VALIDATION.json"
INDEPENDENT_REPLAY = (
    REPO
    / "manifests/pending-zenodo-uploads/20260804_ega_p138_independent_exact_package_replay.json"
)
STATE = (
    REPO
    / "manifests/zenodo-active-custody/ega-p138-three-concept-20260804/state.json"
)
TEMP = REPO / "tmp/zenodo/ega-p138-three-concept-20260804"
RECEIPT_ROOT = REPO / "manifests/published-zenodo"
GITHUB_REPO = "https://github.com/KokunoYumeto/modern-latex-manuscripts"

PUBLICATION_DATE = "2026-08-04"
REMOTE_PREFIX = "08_EGA_P138__"
P138_ZIP_LOCAL_NAME = "00_EGA_I_P138_Diplomatic_French_Paired_English_PreStacks_Source.zip"
P138_ZIP_REMOTE_NAME = REMOTE_PREFIX + P138_ZIP_LOCAL_NAME
P138_ZIP_MEMBERS = 172
P138_EXTRA = {
    "15_PACKAGE_VALIDATION.json": (
        79_354,
        "E010E33952912E300DC24293BB807B3DE1B5A2ED4602A8435A132C8F27AC10E6",
    )
}
INDEPENDENT_REPLAY_IDENTITY = (
    2_876,
    "B69F36E082F9A624FE89F097D333836AA88F23BDAAFB19BECD85803FC16F6EFF",
)

P127_LOCAL_NAMES = (
    "00_EGA_I_P127_Diplomatic_French_Paired_English_PreStacks_Source.zip",
    "02_EGA_PRESTACKS_MACHINE_READABLE_INDEXING_SCAFFOLD_P127.md",
    "03_EGA_PROJECT_LOGBOOK_P127_PUBLIC_PRIVACY_CLEAN.md",
    "04_EGA_CONTINUATION_HANDOFF_P127_PUBLIC_PRIVACY_CLEAN.md",
    "05_EGA_STATUS_P127_PUBLIC_PRIVACY_CLEAN.md",
    "06a_FRENCH_DIPLOMATIC_TRANSCRIPTION_APPEND_P127_20260803.jsonl",
    "06b_ENGLISH_CORRECTION_RECHECK_APPEND_P127_20260803.jsonl",
    "06c_WORKFLOW_ERROR_APPEND_P127_20260803.jsonl",
    "12_PACKAGE_VALIDATION.json",
)
P127_REMOTE_NAMES = {"30_EGA_P127__" + name for name in P127_LOCAL_NAMES}

METHOD_MACHINE_COMPACTION_NAMES = (
    "02_ENGLISH_GERMANIC_DECISION_LOG_PRIVACY_VALIDATION_v3.json",
    "04_PACKAGE_PAYLOAD_MANIFEST.csv",
    "18_CJK_Visual_Evidence_Public_Safe_Index_20260722.jsonl",
    "24a_Retained_Interlanguage_Companion_Manifests_Statuses_20260803_MANIFEST.csv",
    "25a_Retained_Legacy_Companion_Metadata_20260803_MANIFEST.csv",
    "ALL_SESSION_PROVENANCE_TRANCHE_INDEX.json",
    "ALL_SESSION_PROVENANCE_TRANCHE_SHA256SUMS.csv",
    "DELIGNE__COMPLETE_PROVENANCE_MANIFEST.csv",
    "EGA__COMPLETE_PROVENANCE_MANIFEST.csv",
    "FAC__COMPLETE_PROVENANCE_MANIFEST.csv",
)
METHOD_COMPACTION_NAME = "07z_Retained_Machine_Companion_Metadata_20260804.zip"
METHOD_COMPACTION_PREFIX = "RETAINED_MACHINE_COMPANION_METADATA_20260804"
METHOD_COMPACTION_MEMBER_MANIFEST = "MEMBER_MANIFEST.csv"
METHOD_COMPACTION_README = "README.md"

FAC_CONCEPT_DOI = "10.5281/zenodo.21720996"
FAC_VERSION_DOI = "10.5281/zenodo.21781714"
TOMBSTONED_FAC_IDENTIFIERS = {
    "10.5281/zenodo.21779392",
    "10.5281/zenodo.21779393",
}
GAGA_CONCEPT_DOI = "10.5281/zenodo.21781322"
GAGA_VERSION_DOI = "10.5281/zenodo.21781323"
SGA_CONCEPT_DOI = "10.5281/zenodo.20410947"
SGA_VERSION_DOI = "10.5281/zenodo.21782424"

SGA_LANDING_BLOCK = """<h2>Current SGA 1-7 II R3 provenance</h2>
<p>The current SGA working-reader successor is <a href="https://doi.org/10.5281/zenodo.21782424">version 10.5281/zenodo.21782424</a> on the existing <a href="https://doi.org/10.5281/zenodo.20410947">SGA concept</a>. It fronts the complete 152-member reader/source ZIP and the 4,179-page global cross-volume reader.</p>
<p>This record directly exposes the exact SGA R3 package logbook, cross-volume decision logbook, continuation record, supersession/rationale ledger, and the preserved presentation-clean decision and revision histories. The accompanying deterministic provenance ZIP retains all 106 package control files plus the six top-level package manifests and validations. These surfaces make the workflow, corrections, reversals, residual references, privacy decisions, and continuation state auditable; they do not certify the translation, mathematics, rights, or accessibility.</p>
"""


@dataclass(frozen=True)
class Target:
    key: str
    predecessor: int
    doi: str
    concept_doi: str
    title: str
    files: int
    total_bytes: int
    revision: int
    version_index: int
    file_surface_sha256: str
    default_preview: str
    version: str
    expected_successor_files: int


TARGETS = (
    Target(
        key="ega",
        predecessor=21780931,
        doi="10.5281/zenodo.21780931",
        concept_doi="10.5281/zenodo.20414353",
        title="Elements de geometrie algebrique (EGA): English Working Readers and Buildable TeX",
        files=58,
        total_bytes=3_776_100_143,
        revision=3,
        version_index=62,
        file_surface_sha256="89500E3EA8BF7664E0C4194607A309CE46E96081AFBB2AC3FE0D683E9EF4A02D",
        default_preview="00_GLOBAL_EGA_0_IV_English_Complete_Linked_Reader_20260801.pdf",
        version="2026-08-04 EGA I diplomatic French and paired English through p.138",
        expected_successor_files=67,
    ),
    Target(
        key="methodology",
        predecessor=21782511,
        doi="10.5281/zenodo.21782511",
        concept_doi="10.5281/zenodo.21124403",
        title="Interlanguage and Mathematical Translation Methodology Sidecar",
        files=100,
        total_bytes=5_004_414_281,
        revision=4,
        version_index=29,
        file_surface_sha256="EA1113F6F8E9C4D65510A3CE012669C93AE5EEF75327F9E7D67A1341BA268591",
        default_preview="00_Interlanguage_Methodology_Current_v13_20260718.pdf",
        version="2026-08-04 EGA p.138 source, provenance, and pre-Stacks controls",
        expected_successor_files=100,
    ),
    Target(
        key="replication",
        predecessor=21782515,
        doi="10.5281/zenodo.21782515",
        concept_doi="10.5281/zenodo.20461174",
        title="AI-Run Modern LaTeX Manuscript Workflow and Replication Packet",
        files=77,
        total_bytes=22_843_758,
        revision=4,
        version_index=36,
        file_surface_sha256="372F6B05C1D9274CAE56B9E190AC3682794FA8E7803E917F27D7CA5ABE51A977",
        default_preview="00_AI_Run_Modern_LaTeX_Manuscript_Workflow_Current_20260728.pdf",
        version="2026-08-04 EGA p.138 replication and pre-Stacks controls",
        expected_successor_files=86,
    ),
)


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest().upper()


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


def file_row(path: Path) -> dict[str, object]:
    return {
        "path": str(path),
        "bytes": path.stat().st_size,
        "sha256": sha256_path(path),
        "md5": md5_path(path),
    }


def identity(entry: dict) -> tuple[int, str]:
    return int(entry["size"]), base.normalized_md5(entry["checksum"])


def legacy_identity(entry: dict) -> tuple[int, str]:
    return int(entry["filesize"]), base.normalized_md5(entry["checksum"])


def file_surface_sha256(entries: dict[str, dict]) -> str:
    lines = [
        f"{name}\t{int(entries[name]['size'])}\t{base.normalized_md5(entries[name]['checksum'])}"
        for name in sorted(entries, key=str.casefold)
    ]
    return sha256_bytes("\n".join(lines).encode("utf-8"))


def auth(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def auth_modern(token: str) -> dict[str, str]:
    return {**MODERN, "Authorization": f"Bearer {token}"}


def save_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    os.replace(temporary, path)


def load_state() -> dict:
    if STATE.is_file():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {"targets": {}}


def git_output(*args: str) -> str:
    return subprocess.run(
        ["git", *args],
        cwd=REPO,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    ).stdout.strip()


def validate_source_commit(source_commit: str) -> None:
    if not re.fullmatch(r"[0-9a-f]{40}", source_commit):
        raise RuntimeError("source commit must be an exact lowercase 40-hex commit")
    resolved = git_output("rev-parse", f"{source_commit}^{{commit}}")
    if resolved != source_commit:
        raise RuntimeError("source commit does not resolve exactly")
    head = git_output("rev-parse", "HEAD")
    if head != source_commit:
        raise RuntimeError(f"worktree HEAD {head} differs from source commit {source_commit}")


def load_upload_rows() -> dict[str, dict[str, str]]:
    with UPLOAD_MANIFEST.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 17 or len({row["relative_path"] for row in rows}) != 17:
        raise RuntimeError("p.138 direct-upload manifest must contain 17 unique rows")
    return {row["relative_path"]: row for row in rows}


def validate_local_package() -> dict[str, object]:
    rows = load_upload_rows()
    errors: list[str] = []
    for name, row in rows.items():
        path = PACKAGE_ROOT / name
        if not path.is_file() or (
            path.stat().st_size,
            sha256_path(path),
        ) != (int(row["bytes"]), row["sha256"].upper()):
            errors.append(name)
        for field, concept in (
            ("ega_concept", TARGETS[0].concept_doi),
            ("methodology_concept", TARGETS[1].concept_doi),
            ("replication_concept", TARGETS[2].concept_doi),
        ):
            if row.get(field) != concept:
                errors.append(f"{name}:{field}")
    for name, wanted in P138_EXTRA.items():
        path = PACKAGE_ROOT / name
        if not path.is_file() or (path.stat().st_size, sha256_path(path)) != wanted:
            errors.append(name)
    validation = json.loads(PACKAGE_VALIDATION.read_text(encoding="utf-8"))
    if (
        validation.get("status")
        != "PASS_READY_FOR_EXACT_ARCHIVE_CUSTODY_AND_THREE_CONCEPT_PUBLICATION"
        or validation.get("errors") != []
        or validation.get("public_projection", {}).get("direct_upload_objects") != 17
        or validation.get("public_projection", {}).get("zip", {}).get("members") != P138_ZIP_MEMBERS
    ):
        errors.append("package_validation_semantics")
    if (
        not INDEPENDENT_REPLAY.is_file()
        or (INDEPENDENT_REPLAY.stat().st_size, sha256_path(INDEPENDENT_REPLAY))
        != INDEPENDENT_REPLAY_IDENTITY
    ):
        errors.append("independent_replay_identity")
    else:
        replay = json.loads(INDEPENDENT_REPLAY.read_text(encoding="utf-8"))
        if replay.get("status") != "PASS_INDEPENDENT_EXACT_PACKAGE_REPLAY" or replay.get("errors") != []:
            errors.append("independent_replay_semantics")
    if errors:
        raise RuntimeError(f"local p.138 package boundary failed: {errors}")
    return {
        "manifest_rows": len(rows),
        "direct_objects_with_package_validation": 18,
        "direct_bytes_with_package_validation": sum(int(row["bytes"]) for row in rows.values())
        + P138_EXTRA["15_PACKAGE_VALIDATION.json"][0],
        "zip_members": P138_ZIP_MEMBERS,
        "independent_replay": {
            "bytes": INDEPENDENT_REPLAY_IDENTITY[0],
            "sha256": INDEPENDENT_REPLAY_IDENTITY[1],
        },
    }


def fetch_public(session, record_id: int) -> dict:
    return base.check(
        session.get(
            f"{API}/records/{record_id}?expand=true",
            headers=MODERN,
            timeout=(30, 300),
        ),
        {200},
    ).json()


def fetch_predecessor(session, target: Target, require_latest: bool = True) -> tuple[dict, dict[str, dict]]:
    record = fetch_public(session, target.predecessor)
    entries = base.modern_entries(record)
    observed = {
        "id": int(record["id"]),
        "doi": record["pids"]["doi"]["identifier"],
        "concept_doi": record["parent"]["pids"]["doi"]["identifier"],
        "title": record["metadata"]["title"],
        "is_published": record.get("is_published"),
        "files": len(entries),
        "bytes": sum(int(row["size"]) for row in entries.values()),
        "revision": int(record.get("revision_id", 0)),
        "version_index": int(record["versions"]["index"]),
        "surface": file_surface_sha256(entries),
        "preview": record.get("files", {}).get("default_preview"),
    }
    wanted = {
        "id": target.predecessor,
        "doi": target.doi,
        "concept_doi": target.concept_doi,
        "title": target.title,
        "is_published": True,
        "files": target.files,
        "bytes": target.total_bytes,
        "revision": target.revision,
        "version_index": target.version_index,
        "surface": target.file_surface_sha256,
        "preview": target.default_preview,
    }
    if observed != wanted:
        raise RuntimeError(f"{target.key} predecessor boundary changed: {observed}")
    if not P127_REMOTE_NAMES.issubset(entries):
        raise RuntimeError(f"{target.key} no longer contains the exact p.127 predecessor surface")
    if require_latest:
        latest = base.check(
            session.get(record["links"]["latest"], headers=MODERN, timeout=(30, 300)),
            {200},
        ).json()
        if int(latest["id"]) != target.predecessor:
            raise RuntimeError(f"{target.key} concept head moved to {latest['id']}")
    return record, entries


def assert_no_duplicate_concept(session, token: str, target: Target) -> None:
    result = base.check(
        session.get(
            f"{API}/records",
            params={"q": f'metadata.title:"{target.title}"', "size": 100},
            headers=auth_modern(token),
            timeout=(30, 300),
        ),
        {200},
    ).json()
    exact = [
        row
        for row in result.get("hits", {}).get("hits", [])
        if row.get("metadata", {}).get("title") == target.title
    ]
    concepts = {
        row.get("parent", {}).get("pids", {}).get("doi", {}).get("identifier")
        for row in exact
    }
    concepts.discard(None)
    if concepts != {target.concept_doi}:
        raise RuntimeError(f"{target.key} duplicate-concept guard changed: {sorted(concepts)}")


def check_draft_boundary(session, token: str, target: Target, state: dict) -> None:
    tracked = state.get("targets", {}).get(target.key, {})
    draft_id = tracked.get("draft_id")
    if draft_id:
        response = session.get(
            f"{API}/records/{int(draft_id)}/draft?expand=true",
            headers=auth_modern(token),
            timeout=(30, 300),
        )
        if tracked.get("published_record"):
            if response.status_code != 404:
                raise RuntimeError(f"{target.key} published tracked draft unexpectedly remains active")
            return
        if response.status_code != 200:
            raise RuntimeError(f"tracked {target.key} draft {draft_id} is not active")
        draft = response.json()
        if (
            draft.get("parent", {}).get("pids", {}).get("doi", {}).get("identifier")
            != target.concept_doi
            or int(draft.get("versions", {}).get("index", 0)) != target.version_index + 1
        ):
            raise RuntimeError(f"tracked {target.key} draft boundary changed")
        return
    response = session.get(
        f"{API}/records/{target.predecessor}/draft?expand=true",
        headers=auth_modern(token),
        timeout=(30, 180),
    )
    if response.status_code != 404:
        raise RuntimeError(f"{target.key} has an untracked active draft")


def download_exact(session, entry: dict, destination: Path) -> None:
    wanted = identity(entry)
    if destination.is_file() and (destination.stat().st_size, md5_path(destination)) == wanted:
        return
    destination.parent.mkdir(parents=True, exist_ok=True)
    partial = destination.with_suffix(destination.suffix + ".part")
    response = base.check(
        session.get(entry["links"]["content"], stream=True, timeout=(30, 600)),
        {200},
    )
    digest = hashlib.md5(usedforsecurity=False)
    total = 0
    with response, partial.open("wb") as handle:
        for block in response.iter_content(4 * 1024 * 1024):
            if block:
                handle.write(block)
                digest.update(block)
                total += len(block)
    if (total, digest.hexdigest().lower()) != wanted:
        raise RuntimeError(f"predecessor download identity mismatch: {destination.name}")
    os.replace(partial, destination)


def deterministic_zipinfo(name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    return info


def build_methodology_compaction(session, entries: dict[str, dict]) -> tuple[dict[str, object], list[dict[str, object]]]:
    missing = set(METHOD_MACHINE_COMPACTION_NAMES) - set(entries)
    if missing:
        raise RuntimeError(f"methodology compaction source files missing: {sorted(missing)}")
    source_root = TEMP / "methodology-compaction-source"
    rows: list[dict[str, object]] = []
    for name in METHOD_MACHINE_COMPACTION_NAMES:
        path = source_root / name
        download_exact(session, entries[name], path)
        rows.append(
            {
                "member_path": f"{METHOD_COMPACTION_PREFIX}/{name}",
                "original_direct_filename": name,
                "bytes": path.stat().st_size,
                "md5": md5_path(path),
                "sha256": sha256_path(path),
                "source_record": TARGETS[1].predecessor,
                "source_doi": TARGETS[1].doi,
                "source_content_url": entries[name]["links"]["content"],
                "disposition": "exact predecessor byte retained in indexed ZIP; predecessor retains direct presentation",
            }
        )
    fields = tuple(rows[0])
    manifest_buffer = io.StringIO(newline="")
    writer = csv.DictWriter(manifest_buffer, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    manifest_bytes = manifest_buffer.getvalue().encode("utf-8")
    readme_bytes = (
        "# Retained machine companion metadata\n\n"
        "This deterministic ZIP preserves ten exact machine-only files that were direct on methodology predecessor record 21782511. They are compacted solely because the successor must remain within Zenodo's 100-file ceiling while adding the full EGA p.138 provenance surface. No human logbook, decision/reversal history, continuation record, rights note, or reader is compacted. `MEMBER_MANIFEST.csv` binds every source URL, byte count, MD5, and SHA-256; record 21782511 preserves the direct predecessor presentation.\n"
    ).encode("utf-8")
    zip_path = TEMP / METHOD_COMPACTION_NAME
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for row in rows:
            source = source_root / str(row["original_direct_filename"])
            archive.writestr(deterministic_zipinfo(str(row["member_path"])), source.read_bytes())
        archive.writestr(
            deterministic_zipinfo(f"{METHOD_COMPACTION_PREFIX}/{METHOD_COMPACTION_MEMBER_MANIFEST}"),
            manifest_bytes,
        )
        archive.writestr(
            deterministic_zipinfo(f"{METHOD_COMPACTION_PREFIX}/{METHOD_COMPACTION_README}"),
            readme_bytes,
        )
    expected_names = [str(row["member_path"]) for row in rows] + [
        f"{METHOD_COMPACTION_PREFIX}/{METHOD_COMPACTION_MEMBER_MANIFEST}",
        f"{METHOD_COMPACTION_PREFIX}/{METHOD_COMPACTION_README}",
    ]
    with zipfile.ZipFile(zip_path) as archive:
        if archive.namelist() != expected_names or archive.testzip() is not None:
            raise RuntimeError("methodology compaction ZIP order/CRC changed")
        for row in rows:
            payload = archive.read(str(row["member_path"]))
            if (len(payload), sha256_bytes(payload)) != (int(row["bytes"]), str(row["sha256"])):
                raise RuntimeError(f"methodology compaction member changed: {row['member_path']}")
        if archive.read(expected_names[-2]) != manifest_bytes or archive.read(expected_names[-1]) != readme_bytes:
            raise RuntimeError("methodology compaction controls changed")
    result = file_row(zip_path)
    result.update(
        {
            "members": len(expected_names),
            "represented_predecessor_files": len(rows),
            "member_manifest_bytes": len(manifest_bytes),
            "member_manifest_sha256": sha256_bytes(manifest_bytes),
            "readme_bytes": len(readme_bytes),
            "readme_sha256": sha256_bytes(readme_bytes),
        }
    )
    return result, rows


def p138_uploads() -> dict[str, dict[str, object]]:
    rows = load_upload_rows()
    uploads: dict[str, dict[str, object]] = {}
    for name, row in rows.items():
        path = PACKAGE_ROOT / name
        uploads[REMOTE_PREFIX + name] = file_row(path)
    for name in P138_EXTRA:
        uploads[REMOTE_PREFIX + name] = file_row(PACKAGE_ROOT / name)
    if len(uploads) != 18:
        raise RuntimeError("p.138 upload map changed")
    return uploads


def removals(target: Target) -> set[str]:
    result = set(P127_REMOTE_NAMES)
    if target.key == "methodology":
        result.update(METHOD_MACHINE_COMPACTION_NAMES)
    return result


def uploads_for(target: Target, compaction: dict[str, object]) -> dict[str, dict[str, object]]:
    uploads = p138_uploads()
    if target.key == "methodology":
        uploads[METHOD_COMPACTION_NAME] = compaction
    if len(uploads) != (19 if target.key == "methodology" else 18):
        raise RuntimeError(f"{target.key} upload count changed")
    return uploads


def preflight(session, token: str, state: dict, source_commit: str | None) -> dict:
    local = validate_local_package()
    snapshots: dict[str, object] = {}
    records: dict[str, tuple[dict, dict[str, dict]]] = {}
    for target in TARGETS:
        record, entries = fetch_predecessor(
            session,
            target,
            require_latest=not bool(state.get("targets", {}).get(target.key, {}).get("published_record")),
        )
        assert_no_duplicate_concept(session, token, target)
        check_draft_boundary(session, token, target, state)
        records[target.key] = (record, entries)
        snapshots[target.key] = {
            "predecessor_record": target.predecessor,
            "predecessor_doi": target.doi,
            "concept_doi": target.concept_doi,
            "files": len(entries),
            "bytes": sum(int(row["size"]) for row in entries.values()),
            "file_surface_sha256": file_surface_sha256(entries),
            "default_preview": record["files"].get("default_preview"),
            "active_draft": bool(state.get("targets", {}).get(target.key, {}).get("draft_id")),
            "duplicate_concept": False,
        }
    compaction, compact_rows = build_methodology_compaction(session, records["methodology"][1])
    upload_summary: dict[str, object] = {}
    for target in TARGETS:
        uploads = uploads_for(target, compaction)
        desired_count = target.files - len(removals(target)) + len(uploads)
        if desired_count != target.expected_successor_files or desired_count > 100:
            raise RuntimeError(f"{target.key} successor count changed: {desired_count}")
        upload_summary[target.key] = {
            "remove_files": sorted(removals(target), key=str.casefold),
            "add_files": {
                name: {key: row[key] for key in ("bytes", "sha256", "md5")}
                for name, row in sorted(uploads.items(), key=lambda item: item[0].casefold())
            },
            "successor_files": desired_count,
        }
    if source_commit is not None:
        validate_source_commit(source_commit)
        state["source_commit"] = source_commit
    state.update(
        {
            "status": "PREFLIGHT_PASS_NO_ZENODO_MUTATION",
            "local_package": local,
            "preflight": {
                "targets": snapshots,
                "uploads": upload_summary,
                "methodology_compaction": {
                    key: compaction[key]
                    for key in (
                        "bytes",
                        "sha256",
                        "md5",
                        "members",
                        "represented_predecessor_files",
                        "member_manifest_bytes",
                        "member_manifest_sha256",
                        "readme_bytes",
                        "readme_sha256",
                    )
                },
                "methodology_compaction_source_rows": compact_rows,
                "new_concept_created": False,
            },
        }
    )
    save_json(STATE, state)
    return state


def create_tracked_drafts(session, token: str, state: dict) -> dict:
    source_commit = state.get("source_commit")
    if not isinstance(source_commit, str):
        raise RuntimeError("run preflight with --source-commit before prepare")
    validate_source_commit(source_commit)
    for target in TARGETS:
        tracked = state.setdefault("targets", {}).setdefault(target.key, {})
        if tracked.get("draft_id"):
            check_draft_boundary(session, token, target, state)
            continue
        record, entries = fetch_predecessor(session, target, require_latest=True)
        assert_no_duplicate_concept(session, token, target)
        check_draft_boundary(session, token, target, state)
        deposition = base.check(
            session.get(
                f"{API}/deposit/depositions/{target.predecessor}",
                headers=auth(token),
                timeout=(30, 300),
            ),
            {200},
        ).json()
        created = base.check(
            session.post(
                deposition["links"]["newversion"],
                headers=auth(token),
                timeout=(30, 600),
            ),
            {201},
        ).json()
        draft = base.check(
            session.get(created["links"]["latest_draft"], headers=auth(token), timeout=(30, 300)),
            {200},
        ).json()
        tracked.update(
            {
                "status": "OPEN_TRACKED_SUCCESSOR_DRAFT",
                "predecessor": target.predecessor,
                "predecessor_file_surface_sha256": file_surface_sha256(entries),
                "predecessor_revision": record.get("revision_id"),
                "draft_id": int(draft["id"]),
            }
        )
        save_json(STATE, state)
        print(f"created tracked {target.key} draft {draft['id']}", flush=True)
    state["status"] = "PREPARED_THREE_TRACKED_DRAFTS"
    save_json(STATE, state)
    return state


def upload_file(session, token: str, bucket: str, name: str, path: Path) -> None:
    print(f"upload {name} ({path.stat().st_size} bytes)", flush=True)
    with path.open("rb") as handle:
        base.check(
            session.put(
                f"{bucket.rstrip('/')}/{urllib.parse.quote(name, safe='')}",
                headers={**auth(token), "Content-Type": "application/octet-stream"},
                data=handle,
                timeout=(30, 1800),
            ),
            {200, 201},
        )


def add_related(metadata: dict, identifier: str, scheme: str, relation: str) -> None:
    rows = metadata.setdefault("related_identifiers", [])
    if any(row.get("identifier") == identifier for row in rows):
        return
    rows.append(
        {
            "identifier": identifier,
            "scheme": scheme,
            "relation_type": {"id": relation},
        }
    )


def fac_block() -> str:
    return (
        '<p><strong>Dedicated FAC publication:</strong> use '
        f'<a href="https://doi.org/{FAC_CONCEPT_DOI}">{FAC_CONCEPT_DOI}</a> '
        f'(current version <a href="https://doi.org/{FAC_VERSION_DOI}">{FAC_VERSION_DOI}</a>). '
        "It coherently preserves the French transcription, complete English reader, pre-discovery English through nos. 1-79, readable comparison report, 79 unit reviews, 138 findings, 219 self-corrections, and source/evidence projection. The orchestrator did not know the Achinger-Krupa translation existed when Codex translated and froze nos. 1-79; the comparator was discovered afterward, and all 79 blind-scope units were then adjudicated against the French authority. Nos. 80-81 are outside the blind claim. The comparison is qualitative, not a scalar score, ranking, certification, or general superiority claim. Earlier broad FAC projections remain immutable adverse history; GAGA remains separate.</p>"
    )


def gaga_block() -> str:
    return (
        '<p><strong>Dedicated GAGA working edition:</strong> the pure-GAGA concept is '
        f'<a href="https://doi.org/{GAGA_CONCEPT_DOI}">{GAGA_CONCEPT_DOI}</a> '
        f'(current version <a href="https://doi.org/{GAGA_VERSION_DOI}">{GAGA_VERSION_DOI}</a>). '
        "It covers Serre's printed pages 1-42 through bibliography and EOF as a linked 26-page English reader, buildable English TeX, and separate diplomatic and corrected French TeX layers. GAGA remains separate from FAC, and workflow/status prose is kept outside the mathematical reader.</p>"
    )


def description(target: Target, source_commit: str) -> str:
    ega_url = (
        f"{GITHUB_REPO}/tree/{source_commit}/sources/ega/checkpoints/"
        "ega1-p138-diplomatic-prestacks-r1-20260804"
    )
    if target.key == "ega":
        return (
            '<p><strong>Read EGA:</strong> open <code>00_GLOBAL_EGA_0_IV_English_Complete_Linked_Reader_20260801.pdf</code> for the continuous EGA 0-IV working reader; it remains the default preview.</p>'
            '<p><strong>Download the reader/source corpus:</strong> <code>00 Current_EGA_English_Readers_and_Buildable_TeX_20260801.zip</code> contains the global reader, five standalone readers, and buildable TeX for all six reader surfaces.</p>'
            "<p><strong>Reader coverage:</strong> EGA 0 through Section 13; EGA I and II through EOF; the published EGA III text through 7.9.14; and EGA IV Sections 1-21 through EOF. The 1,356-page global reader has 15,383 destinations and 17,808 resolved internal links.</p>"
            "<p><strong>Canonical French and pre-Stacks work:</strong> this concept now preserves the coherent EGA I checkpoint through printed p.138: terminal diplomatic French R61, paired English R82 with 127 exact source identities, the French-rooted pre-Stacks indexing scaffold, and four separately reasoned English fidelity repairs. The full eight-publication French EGA canon and semantic graph remain in progress; the next cursor is printed p.139, continuation of Proposition 5.5.10.</p>"
            "<p><strong>Audit and provenance:</strong> the p.138 source ZIP, machine-readable scaffold, French and English human logbooks, continuation handoff, both status surfaces, French/English/workflow append-only ledgers, privacy transformation/validation evidence, rights note, payload manifest, and package validation are direct files. Exact private custody retains source bytes unchanged; every minimal public privacy transformation is ledgered. "
            f'Commit-pinned checkpoint: <a href="{ega_url}">{source_commit}</a>. Methodology: <a href="https://doi.org/10.5281/zenodo.21124403">10.5281/zenodo.21124403</a>; replication: <a href="https://doi.org/10.5281/zenodo.20461174">10.5281/zenodo.20461174</a>.</p>'
            "<p><strong>Status and rights:</strong> these are working readers and preservation checkpoints, not critical editions, source-fidelity or mathematical certifications, new rights grants, or claims that the whole French corpus or pre-Stacks graph is complete. NUMDAM authority PDFs and page images are not redistributed; French and third-party rights remain with their rightsholders.</p>"
        )
    ega = (
        "<p><strong>EGA canonical-French / paired-English checkpoint:</strong> direct files preserve the coherent EGA I p.138 terminal French R61 / English R82 generation, the complete 127-file English source tree, French-rooted pre-Stacks scaffold, both privacy-clean human logbooks and status surfaces, continuation, French/English/workflow append-only decision-reversal-error ledgers, privacy evidence, rights note, manifests, and package validation. The next cursor is printed p.139; this does not claim completion of EGA I, the eight-publication French corpus, or the semantic graph. "
        f'Commit-pinned checkpoint: <a href="{ega_url}">{source_commit}</a>.</p>'
    )
    if target.key == "methodology":
        return (
            SGA_LANDING_BLOCK
            + '<p><strong>Open first:</strong> <code>00_Interlanguage_Methodology_Current_v13_20260718.pdf</code> is the default preview and maps the stable manuscript, reader, methodology, and provenance homes.</p>'
            "<p><strong>Purpose:</strong> this concept is the methodology, provenance, corpus-control, decision-rationale, and programme-state sidecar for the mathematical transcription and translation archive. It preserves source-body baselines, workflow controls, correction and reversal histories, continuation state, reproducible checks, and bounded interlanguage experiments; mathematical readers remain on their author or series concepts.</p>"
            "<p><strong>Current audit surface:</strong> the directly embedded privacy-clean English/Germanic v3 decision-log snapshot has 482 append-only records in exact order, 2,427 event-level privacy transformations, and no omitted decisions in that snapshot. The direct log, transformation ledger, validator, explanatory note, manifest, and deterministic provenance ZIP remain independently replayable.</p>"
            + ega
            + fac_block()
            + gaga_block()
            + "<p><strong>Archive organization:</strong> every human logbook, decision/reversal history, continuation record, rights note, reader, and new EGA p.138 surface remains direct. Ten older machine-only manifests/validators are retained byte-for-byte in <code>07z_Retained_Machine_Companion_Metadata_20260804.zip</code> solely to respect Zenodo's 100-file ceiling; its embedded manifest binds source URLs, bytes, MD5, and SHA-256, and predecessor record 21782511 retains their direct presentation. No distinct content is selected away.</p>"
            "<p><strong>Limits:</strong> these model-built methodology, corpus, translation, provenance, and visual-QA artifacts do not claim native-language validation, source-fidelity certification, mathematical correctness, rights clearance, critical-edition status, peer review, or completion of any author corpus.</p>"
        )
    return (
        SGA_LANDING_BLOCK
        + '<p><strong>Open first:</strong> <code>00_AI_Run_Modern_LaTeX_Manuscript_Workflow_Current_20260728.pdf</code> is the default preview for the current workflow and replication packet.</p>'
        "<p><strong>Purpose:</strong> this concept preserves reproducible workflow, source-control and visual-QA methods, decision and correction trails, exact manifests, methodology briefings, and public-safe replication surfaces used across the manuscript archive. Production tasks remain responsible for translation, transcription, source adjudication, mathematics, diagrams, and visual QA.</p>"
        "<p><strong>Current audit surface:</strong> the directly embedded privacy-clean English/Germanic v3 decision-log snapshot contains 482 append-only records in exact order, with 2,427 event-level transformations and no omitted decisions in that snapshot. The direct log and deterministic provenance ZIP remain byte-identical counterparts of the methodology surface.</p>"
        + ega
        + fac_block()
        + gaga_block()
        + "<p><strong>Method boundary:</strong> source images and authoritative texts decide genuine ambiguities; OCR and generated research notes remain locators or evidence, not source authority. Native editable mathematical diagrams and exact references belong in reader/source successors, while workflow/status commentary remains in external provenance surfaces rather than reader PDFs.</p>"
        "<p><strong>Limits:</strong> this packet supports audit and replication but does not certify a translation, transcription, edition, mathematical claim, software system, rights status, or whole-project completion.</p>"
    )


def staged_metadata(target: Target, predecessor: dict, source_commit: str) -> dict:
    metadata = copy.deepcopy(predecessor["metadata"])
    metadata["publication_date"] = PUBLICATION_DATE
    metadata["version"] = target.version
    metadata["description"] = description(target, source_commit)
    metadata.pop("additional_descriptions", None)
    related = []
    for row in metadata.get("related_identifiers", []):
        identifier = row.get("identifier")
        if identifier in TOMBSTONED_FAC_IDENTIFIERS:
            continue
        if isinstance(identifier, str) and "ega1-p127-diplomatic-prestacks-r1-20260803" in identifier:
            continue
        related.append(row)
    metadata["related_identifiers"] = related
    ega_url = (
        f"{GITHUB_REPO}/tree/{source_commit}/sources/ega/checkpoints/"
        "ega1-p138-diplomatic-prestacks-r1-20260804"
    )
    add_related(metadata, ega_url, "url", "issupplementedby")
    add_related(metadata, FAC_CONCEPT_DOI, "doi", "references")
    add_related(metadata, FAC_VERSION_DOI, "doi", "references")
    if target.key != "ega":
        add_related(metadata, GAGA_CONCEPT_DOI, "doi", "references")
        add_related(metadata, GAGA_VERSION_DOI, "doi", "references")
        add_related(metadata, SGA_CONCEPT_DOI, "doi", "references")
        add_related(metadata, SGA_VERSION_DOI, "doi", "references")
    return metadata


def desired_order(target: Target, names: set[str], uploads: set[str]) -> list[str]:
    p138 = [
        REMOTE_PREFIX + name
        for name in (
            P138_ZIP_LOCAL_NAME,
            "01_READ_ME_FIRST.md",
            "02_EGA_PRESTACKS_MACHINE_READABLE_INDEXING_SCAFFOLD_P138.md",
            "03_EGA_FRENCH_PROJECT_LOGBOOK_P138_PUBLIC_PRIVACY_CLEAN.md",
            "04_EGA_ENGLISH_RECHECK_LOGBOOK_P138_PUBLIC_PRIVACY_CLEAN.md",
            "05_EGA_CONTINUATION_HANDOFF_P138_PUBLIC_PRIVACY_CLEAN.md",
            "06_EGA_FRENCH_STATUS_P138_PUBLIC_PRIVACY_CLEAN.md",
            "07_EGA_ENGLISH_STATUS_P138_PUBLIC_PRIVACY_CLEAN.md",
            "09a_FRENCH_DIPLOMATIC_TRANSCRIPTION_APPEND_P138_20260804.jsonl",
            "09b_ENGLISH_CORRECTION_RECHECK_APPEND_P138_20260804.jsonl",
            "09c_WORKFLOW_ERROR_APPEND_P138_20260804.jsonl",
            "10_RIGHTS_AND_PROVENANCE.md",
            "08a_EGA1_CHAPTER1_P138_VALIDATION_R61.json",
            "08b_EGA_ENGLISH_SOURCE_DIFF_VALIDATION_R82.json",
            "11_PRIVACY_TRANSFORMATIONS.csv",
            "12_PRIVACY_VALIDATION.json",
            "13_PACKAGE_PAYLOAD_MANIFEST.csv",
            "15_PACKAGE_VALIDATION.json",
        )
    ]
    if target.key == "ega":
        front = [
            "00 Current_EGA_English_Readers_and_Buildable_TeX_20260801.zip",
            target.default_preview,
            *p138,
        ]
    elif target.key == "methodology":
        front = [
            target.default_preview,
            "00_Interlanguage_Methodology_Current_v13_20260718.md",
            "07_SGA_R3__00_COMPLETE_PROVENANCE_CONTROLS_20260804.zip",
            "07_SGA_R3__01_PACKAGE_LOGBOOK.md",
            "07_SGA_R3__02_CROSS_VOLUME_LOGBOOK.md",
            "07_SGA_R3__03_CONTINUATION.md",
            "07_SGA_R3__04_SUPERSESSION_AND_ORDER.csv",
            "07_SGA_R3__05_PREDECESSOR_DECISION_LOG.csv",
            "07_SGA_R3__06_PREDECESSOR_REVISION_HISTORY.csv",
            *p138,
            METHOD_COMPACTION_NAME,
        ]
    else:
        front = [
            target.default_preview,
            "00_AI_Run_Modern_LaTeX_Manuscript_Workflow_Current_20260728.md",
            "07_SGA_R3__00_COMPLETE_PROVENANCE_CONTROLS_20260804.zip",
            "07_SGA_R3__01_PACKAGE_LOGBOOK.md",
            "07_SGA_R3__02_CROSS_VOLUME_LOGBOOK.md",
            "07_SGA_R3__03_CONTINUATION.md",
            "07_SGA_R3__04_SUPERSESSION_AND_ORDER.csv",
            "07_SGA_R3__05_PREDECESSOR_DECISION_LOG.csv",
            "07_SGA_R3__06_PREDECESSOR_REVISION_HISTORY.csv",
            *p138,
        ]
    missing = [name for name in front if name not in names]
    if missing:
        raise RuntimeError(f"{target.key} front-order files missing: {missing}")
    order: list[str] = []
    seen: set[str] = set()
    for name in front + sorted(names, key=str.casefold):
        if name not in seen:
            seen.add(name)
            order.append(name)
    if set(order) != names or not uploads.issubset(names):
        raise RuntimeError(f"{target.key} order does not cover desired surface")
    return order


def stage_target(
    session,
    token: str,
    target: Target,
    uploads: dict[str, dict[str, object]],
    state: dict,
) -> None:
    tracked = state["targets"][target.key]
    if tracked.get("status") in {"STAGED_VALIDATED", "PUBLISHED_READBACK_PENDING", "CLOSED_PUBLIC_READBACK_PASS"}:
        return
    predecessor, predecessor_entries = fetch_predecessor(session, target, require_latest=True)
    draft_id = int(tracked["draft_id"])
    deposition = base.check(
        session.get(
            f"{API}/deposit/depositions/{draft_id}",
            headers=auth(token),
            timeout=(30, 300),
        ),
        {200},
    ).json()
    staged = base.legacy_entries(deposition)
    remove = removals(target)
    for name in sorted(remove | set(uploads), key=str.casefold):
        if name not in staged:
            continue
        wanted = uploads.get(name)
        if wanted and legacy_identity(staged[name]) == (int(wanted["bytes"]), str(wanted["md5"])):
            continue
        base.check(
            session.delete(staged[name]["links"]["self"], headers=auth(token), timeout=(30, 300)),
            {204},
        )
    deposition = base.check(
        session.get(
            f"{API}/deposit/depositions/{draft_id}",
            headers=auth(token),
            timeout=(30, 300),
        ),
        {200},
    ).json()
    staged = base.legacy_entries(deposition)
    for name, row in sorted(uploads.items(), key=lambda item: item[0].casefold()):
        if name not in staged:
            upload_file(session, token, deposition["links"]["bucket"], name, Path(str(row["path"])))
    draft = base.check(
        session.get(
            f"{API}/records/{draft_id}/draft?expand=true",
            headers=auth_modern(token),
            timeout=(30, 300),
        ),
        {200},
    ).json()
    entries = base.modern_entries(draft)
    desired = (set(predecessor_entries) - remove) | set(uploads)
    if set(entries) != desired or len(entries) != target.expected_successor_files:
        raise RuntimeError(f"{target.key} staged file set/count changed")
    for name, row in uploads.items():
        if identity(entries[name]) != (int(row["bytes"]), str(row["md5"])):
            raise RuntimeError(f"{target.key} staged upload identity changed: {name}")
    for name in desired - set(uploads):
        if identity(entries[name]) != identity(predecessor_entries[name]):
            raise RuntimeError(f"{target.key} retained predecessor changed: {name}")
    order = desired_order(target, desired, set(uploads))
    metadata = staged_metadata(target, predecessor, str(state["source_commit"]))
    payload = {
        "access": predecessor["access"],
        "files": {"enabled": True, "default_preview": target.default_preview, "order": order},
        "metadata": metadata,
        "custom_fields": predecessor.get("custom_fields", {}),
    }
    if draft.get("pids"):
        payload["pids"] = draft["pids"]
    patched = base.check(
        session.put(
            f"{API}/records/{draft_id}/draft",
            headers={**auth_modern(token), "Content-Type": "application/json"},
            json=payload,
            timeout=(30, 600),
        ),
        {200},
    ).json()
    related = {row.get("identifier") for row in patched.get("metadata", {}).get("related_identifiers", [])}
    if (
        set(base.modern_entries(patched)) != desired
        or patched.get("files", {}).get("default_preview") != target.default_preview
        or (patched.get("files", {}).get("order") or []) not in (order, [])
        or patched.get("metadata", {}).get("description") != metadata["description"]
        or related & TOMBSTONED_FAC_IDENTIFIERS
        or FAC_CONCEPT_DOI not in related
        or FAC_VERSION_DOI not in related
    ):
        raise RuntimeError(f"{target.key} staged metadata/presentation changed")
    tracked.update(
        {
            "status": "STAGED_VALIDATED",
            "staged_files": len(entries),
            "staged_bytes": sum(int(row["size"]) for row in entries.values()),
            "staged_file_surface_sha256": file_surface_sha256(entries),
            "removed_predecessor_files": sorted(remove, key=str.casefold),
            "new_upload_files": sorted(uploads, key=str.casefold),
        }
    )
    save_json(STATE, state)
    print(f"staged and validated {target.key} draft {draft_id}", flush=True)


def stream_readback(session, url: str, destination: Path | None = None) -> tuple[int, str]:
    response = base.check(session.get(url, stream=True, timeout=(30, 1800)), {200})
    digest = hashlib.sha256()
    total = 0
    handle = None
    partial = None
    if destination is not None:
        destination.parent.mkdir(parents=True, exist_ok=True)
        partial = destination.with_suffix(destination.suffix + ".part")
        handle = partial.open("wb")
    try:
        with response:
            for block in response.iter_content(4 * 1024 * 1024):
                if block:
                    digest.update(block)
                    total += len(block)
                    if handle is not None:
                        handle.write(block)
    finally:
        if handle is not None:
            handle.close()
    if destination is not None and partial is not None:
        os.replace(partial, destination)
    return total, digest.hexdigest().upper()


def wait_public(session, record_id: int, desired: set[str]) -> dict:
    for attempt in range(120):
        response = session.get(
            f"{API}/records/{record_id}?expand=true",
            headers=MODERN,
            timeout=(30, 300),
        )
        if response.status_code == 200:
            record = response.json()
            if record.get("is_published") and set(base.modern_entries(record)) == desired:
                return record
        time.sleep(min(attempt + 1, 5))
    raise RuntimeError(f"published record {record_id} did not become anonymously readable")


def replay_p138_zip(downloaded: Path) -> dict[str, object]:
    manifest_rows = load_upload_rows()
    del manifest_rows
    payload_manifest = PACKAGE_ROOT / "13_PACKAGE_PAYLOAD_MANIFEST.csv"
    with payload_manifest.open("r", encoding="utf-8-sig", newline="") as handle:
        payload_rows = list(csv.DictReader(handle))
    expected = {row["relative_path"]: row for row in payload_rows}
    expected["13_PACKAGE_PAYLOAD_MANIFEST.csv"] = {
        "bytes": str(payload_manifest.stat().st_size),
        "sha256": sha256_path(payload_manifest),
    }
    results: list[dict[str, object]] = []
    with zipfile.ZipFile(downloaded) as archive:
        names = archive.namelist()
        if names != sorted(expected) or len(names) != P138_ZIP_MEMBERS or archive.testzip() is not None:
            raise RuntimeError("public p.138 ZIP member order/set/CRC changed")
        for name in names:
            pure = PurePosixPath(name)
            if (
                pure.is_absolute()
                or ".." in pure.parts
                or "\\" in name
                or re.match(r"^[A-Za-z]:", name)
            ):
                raise RuntimeError(f"unsafe public p.138 ZIP member: {name}")
            payload = archive.read(name)
            row = expected[name]
            observed = len(payload), sha256_bytes(payload)
            wanted = int(row["bytes"]), str(row["sha256"]).upper()
            if observed != wanted:
                raise RuntimeError(f"public p.138 ZIP member changed: {name}")
            results.append(
                {
                    "member_path": name,
                    "bytes": observed[0],
                    "sha256": observed[1],
                    "match": True,
                }
            )
    return {"status": "PASS", "errors": [], "members": len(results), "matches": len(results), "mismatches": 0, "member_identities": results}


def replay_compaction(downloaded: Path, rows: list[dict[str, object]], compaction: dict[str, object]) -> dict[str, object]:
    results: list[dict[str, object]] = []
    with zipfile.ZipFile(downloaded) as archive:
        if archive.testzip() is not None or len(archive.namelist()) != int(compaction["members"]):
            raise RuntimeError("public methodology compaction ZIP changed")
        expected = {str(row["member_path"]): row for row in rows}
        for name in archive.namelist():
            payload = archive.read(name)
            if name in expected:
                row = expected[name]
                wanted = int(row["bytes"]), str(row["sha256"])
            elif name.endswith("/MEMBER_MANIFEST.csv"):
                wanted = int(compaction["member_manifest_bytes"]), str(compaction["member_manifest_sha256"])
            elif name.endswith("/README.md"):
                wanted = int(compaction["readme_bytes"]), str(compaction["readme_sha256"])
            else:
                raise RuntimeError(f"unexpected public compaction member: {name}")
            observed = len(payload), sha256_bytes(payload)
            if observed != wanted:
                raise RuntimeError(f"public compaction member changed: {name}")
            results.append({"member_path": name, "bytes": observed[0], "sha256": observed[1], "match": True})
    return {"status": "PASS", "errors": [], "members": len(results), "matches": len(results), "mismatches": 0, "member_identities": results}


def publish_and_readback(
    session,
    token: str,
    target: Target,
    uploads: dict[str, dict[str, object]],
    compaction: dict[str, object],
    compact_rows: list[dict[str, object]],
    state: dict,
) -> dict:
    tracked = state["targets"][target.key]
    draft_id = int(tracked["draft_id"])
    predecessor, predecessor_entries = fetch_predecessor(
        session,
        target,
        require_latest=not bool(tracked.get("published_record")),
    )
    remove = removals(target)
    desired = (set(predecessor_entries) - remove) | set(uploads)
    if not tracked.get("published_record"):
        draft = base.check(
            session.get(
                f"{API}/records/{draft_id}/draft?expand=true",
                headers=auth_modern(token),
                timeout=(30, 300),
            ),
            {200},
        ).json()
        if tracked.get("status") != "STAGED_VALIDATED" or set(base.modern_entries(draft)) != desired:
            raise RuntimeError(f"{target.key} draft is not staged and validated")
        published = base.check(
            session.post(draft["links"]["publish"], headers=auth_modern(token), timeout=(30, 1200)),
            {200, 202},
        ).json()
        if int(published["id"]) != draft_id:
            raise RuntimeError(f"{target.key} published record differs from tracked draft")
        tracked.update({"status": "PUBLISHED_READBACK_PENDING", "published_record": draft_id})
        save_json(STATE, state)
        print(f"published {target.key} record {draft_id}", flush=True)
    record_id = int(tracked["published_record"])
    record = wait_public(session, record_id, desired)
    entries = base.modern_entries(record)
    readback: dict[str, dict[str, object]] = {}
    p138_zip_download: Path | None = None
    compaction_download: Path | None = None
    for name, row in sorted(uploads.items(), key=lambda item: item[0].casefold()):
        destination = None
        if name == P138_ZIP_REMOTE_NAME:
            destination = TEMP / "public-readback" / str(record_id) / P138_ZIP_LOCAL_NAME
            p138_zip_download = destination
        elif name == METHOD_COMPACTION_NAME:
            destination = TEMP / "public-readback" / str(record_id) / METHOD_COMPACTION_NAME
            compaction_download = destination
        observed = stream_readback(session, entries[name]["links"]["content"], destination)
        wanted = int(row["bytes"]), str(row["sha256"])
        if observed != wanted:
            raise RuntimeError(f"{target.key} public direct readback changed: {name}")
        readback[name] = {
            "bytes": observed[0],
            "sha256": observed[1],
            "match": True,
            "content_url": entries[name]["links"]["content"],
        }
    if p138_zip_download is None:
        raise RuntimeError("p.138 ZIP was not captured for member replay")
    p138_zip_replay = replay_p138_zip(p138_zip_download)
    compaction_replay = None
    if target.key == "methodology":
        if compaction_download is None:
            raise RuntimeError("methodology compaction ZIP was not captured")
        compaction_replay = replay_compaction(compaction_download, compact_rows, compaction)
    retained = desired - set(uploads)
    retained_mismatches = [
        name for name in retained if identity(entries[name]) != identity(predecessor_entries[name])
    ]
    if retained_mismatches or remove & set(entries):
        raise RuntimeError(f"{target.key} retained/superseded public boundary changed")
    expected_metadata = staged_metadata(target, predecessor, str(state["source_commit"]))
    related = {row.get("identifier") for row in record.get("metadata", {}).get("related_identifiers", [])}
    if (
        record.get("files", {}).get("default_preview") != target.default_preview
        or record.get("metadata", {}).get("description") != expected_metadata["description"]
        or related & TOMBSTONED_FAC_IDENTIFIERS
        or FAC_CONCEPT_DOI not in related
        or FAC_VERSION_DOI not in related
    ):
        raise RuntimeError(f"{target.key} public metadata/preview changed")
    versions = base.check(
        # This is deliberately anonymous public-surface validation.  Zenodo
        # caps anonymous version pages at 25; the new record and its immediate
        # predecessor are both on the first page.
        session.get(record["links"]["versions"], params={"size": 25}, headers=MODERN, timeout=(30, 300)),
        {200},
    ).json()
    by_index = {
        int(row["versions"]["index"]): int(row["id"])
        for row in versions.get("hits", {}).get("hits", [])
    }
    latest = base.check(
        session.get(record["links"]["latest"], headers=MODERN, timeout=(30, 300)),
        {200},
    ).json()
    draft_probe = session.get(
        f"{API}/records/{record_id}/draft?expand=true",
        headers=auth_modern(token),
        timeout=(30, 180),
    )
    assert_no_duplicate_concept(session, token, target)
    if (
        int(record["versions"]["index"]) != target.version_index + 1
        or by_index.get(target.version_index) != target.predecessor
        or int(latest["id"]) != record_id
        or draft_probe.status_code != 404
    ):
        raise RuntimeError(f"{target.key} version/latest/draft closeout changed")
    result = {
        "status": "PASS_PUBLISHED_AND_ANONYMOUS_RAW_READBACK",
        "errors": [],
        "target": target.key,
        "record_id": record_id,
        "record_url": f"https://zenodo.org/records/{record_id}",
        "doi": record["pids"]["doi"]["identifier"],
        "concept_doi": target.concept_doi,
        "predecessor_record": target.predecessor,
        "predecessor_doi": target.doi,
        "version_index": int(record["versions"]["index"]),
        "source_commit": state["source_commit"],
        "files": len(entries),
        "bytes": sum(int(row["size"]) for row in entries.values()),
        "file_surface_sha256": file_surface_sha256(entries),
        "default_preview": target.default_preview,
        "landing_description_sha256": sha256_bytes(record["metadata"]["description"].encode("utf-8")),
        "removed_from_direct_successor_surface": sorted(remove, key=str.casefold),
        "removed_bytes_preserved_in_predecessor": True,
        "retained_predecessor_files": len(retained),
        "retained_identity_mismatches": retained_mismatches,
        "new_direct_files": len(readback),
        "new_direct_raw_readback_matches": len(readback),
        "new_direct_raw_readback_mismatches": 0,
        "raw_public_readback": readback,
        "p138_zip_member_replay": p138_zip_replay,
        "methodology_compaction_member_replay": compaction_replay,
        "tombstoned_fac_relations_present": False,
        "active_draft": False,
        "duplicate_concept": False,
        "new_concept_created": False,
        "fac_concept_mutated": False,
        "gaga_concept_mutated": False,
    }
    receipt = RECEIPT_ROOT / f"20260804_ega_p138_{target.key}_record_{record_id}_public_readback.json"
    save_json(receipt, result)
    tracked.update(
        {
            "status": "CLOSED_PUBLIC_READBACK_PASS",
            "receipt": receipt.relative_to(REPO).as_posix(),
            "doi": result["doi"],
        }
    )
    save_json(STATE, state)
    return result


def publish_all(session, token: str, state: dict) -> list[dict]:
    if state.get("status") not in {
        "PREPARED_THREE_TRACKED_DRAFTS",
        "STAGED_ALL_THREE_VALIDATED",
        "PUBLICATION_IN_PROGRESS",
    }:
        raise RuntimeError("run preflight and prepare before publish")
    validate_local_package()
    methodology, methodology_entries = fetch_predecessor(
        session,
        TARGETS[1],
        require_latest=not bool(state.get("targets", {}).get("methodology", {}).get("published_record")),
    )
    del methodology
    compaction, compact_rows = build_methodology_compaction(session, methodology_entries)
    uploads = {target.key: uploads_for(target, compaction) for target in TARGETS}
    for target in TARGETS:
        stage_target(session, token, target, uploads[target.key], state)
    state["status"] = "STAGED_ALL_THREE_VALIDATED"
    save_json(STATE, state)
    state["status"] = "PUBLICATION_IN_PROGRESS"
    save_json(STATE, state)
    results: list[dict] = []
    for target in TARGETS:
        tracked = state["targets"][target.key]
        if tracked.get("status") == "CLOSED_PUBLIC_READBACK_PASS":
            results.append(json.loads((REPO / tracked["receipt"]).read_text(encoding="utf-8")))
            continue
        results.append(
            publish_and_readback(
                session,
                token,
                target,
                uploads[target.key],
                compaction,
                compact_rows,
                state,
            )
        )
    state["status"] = "CLOSED_THREE_CONCEPT_SUCCESSORS_PUBLIC_READBACK_PASS"
    save_json(STATE, state)
    closeout = {
        "status": state["status"],
        "errors": [],
        "source_commit": state["source_commit"],
        "results": results,
        "fac_surviving_concept_unchanged": FAC_CONCEPT_DOI,
        "fac_surviving_version_unchanged": FAC_VERSION_DOI,
        "tombstoned_fac_concept_not_referenced_by_successors": True,
        "gaga_separate_unchanged": GAGA_CONCEPT_DOI,
        "new_concepts_created": 0,
    }
    save_json(
        RECEIPT_ROOT / "20260804_ega_p138_three_concept_publication_closeout.json",
        closeout,
    )
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("preflight", "prepare", "publish"))
    parser.add_argument("--source-commit")
    args = parser.parse_args()
    session = base.make_session()
    token = base.find_token()
    state = load_state()
    if args.action == "preflight":
        result = preflight(session, token, state, args.source_commit)
    elif args.action == "prepare":
        if args.source_commit:
            state["source_commit"] = args.source_commit
            save_json(STATE, state)
        result = create_tracked_drafts(session, token, state)
    else:
        result = {
            "status": "CLOSED_THREE_CONCEPT_SUCCESSORS_PUBLIC_READBACK_PASS",
            "results": publish_all(session, token, state),
        }
    summary = copy.deepcopy(result)
    for row in summary.get("results", []):
        row.pop("raw_public_readback", None)
        row.pop("p138_zip_member_replay", None)
        row.pop("methodology_compaction_member_replay", None)
    if "preflight" in summary:
        summary["preflight"].pop("methodology_compaction_source_rows", None)
    print(json.dumps(summary, indent=2, ensure_ascii=True), flush=True)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr, flush=True)
        raise
