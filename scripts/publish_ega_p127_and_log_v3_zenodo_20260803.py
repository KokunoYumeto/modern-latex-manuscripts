#!/usr/bin/env python3
"""Publish the bounded EGA I p.127 custody checkpoint and decision-log v3.

The operation creates one successor under each of three existing concepts only:
EGA, methodology, and replication.  It never creates a concept.  The EGA
reader/source front remains intact; EGA p.127 provenance is added behind it.
Methodology's 100-file ceiling is handled mechanically by placing fourteen
small, exact legacy companion files in an indexed deterministic ZIP while every
predecessor and every distinct byte remains preserved.

Run ``preflight`` before any Git/Zenodo mutation, ``prepare`` only after the
source checkpoint is commit-pinned, and ``publish`` to stage, validate, publish,
and anonymously read back all newly uploaded bytes.
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
import time
import urllib.parse
import zipfile
from dataclasses import dataclass
from pathlib import Path

import publish_current_reader_bundles_zenodo_20260730 as base


API = base.API
MODERN = {"Accept": "application/vnd.inveniordm.v1+json"}
REPO = Path(__file__).resolve().parents[1]
TEMP = REPO / "tmp/zenodo/ega-p127-and-decision-log-v3-20260803"
STATE = TEMP / "state.json"
EGA_ROOT = REPO / "sources/ega/checkpoints/ega1-p127-diplomatic-prestacks-r1-20260803"
V3_ROOT = REPO / "interlanguage-sidecar/20260803/english-germanic-decision-log-privacy-v3"
RECEIPT_ROOT = REPO / "manifests/published-zenodo"
PUBLICATION_DATE = "2026-08-03"
GITHUB_REPO = "https://github.com/KokunoYumeto/modern-latex-manuscripts"
FAC_CONCEPT_DOI = "10.5281/zenodo.21779392"
FAC_VERSION_DOI = "10.5281/zenodo.21779393"

V2_NAMES = {
    "00_ENGLISH_GERMANIC_DECISION_LOG_1_PUBLIC_PRIVACY_CLEAN_v2.jsonl",
    "00_ENGLISH_GERMANIC_DECISION_LOG_2_PRIVACY_TRANSFORMATIONS_v2_20260803.csv",
    "SGA_1-7II_PRESENTATION_CLEAN_PROVENANCE_MANIFEST_v2_20260803.csv",
    "SGA_1-7II_PRESENTATION_CLEAN_PROVENANCE_v2_20260803.zip",
}

EGA_SELECTED = (
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
EGA_REMOTE_PREFIX = "30_EGA_P127__"
EGA_EXTRA_IDENTITIES = {
    # The package validation intentionally self-excludes from its upload manifest.
    "12_PACKAGE_VALIDATION.json": (
        71_492,
        "28DBFB167F60B4D2FCC4759CD1624A997ABD1517C8E7C1C7DBBF01C159F7459E",
    ),
}

V3_SELECTED = (
    "00_ENGLISH_GERMANIC_DECISION_LOG_PUBLIC_PRIVACY_CLEAN_v3.jsonl",
    "01_ENGLISH_GERMANIC_DECISION_LOG_PRIVACY_TRANSFORMATIONS_v3.csv",
    "02_ENGLISH_GERMANIC_DECISION_LOG_PRIVACY_VALIDATION_v3.json",
    "03_ENGLISH_GERMANIC_DECISION_LOG_PRIVACY_README_v3.md",
    "04_PACKAGE_PAYLOAD_MANIFEST.csv",
    "05_ENGLISH_GERMANIC_DECISION_LOG_PUBLIC_PROVENANCE_v3.zip",
)

COMPACT_NAMES = (
    "12_Interlanguage_Research_Department_and_Automata_v05_20260717_manifest.csv",
    "12_Interlanguage_Research_Department_and_Automata_v05_20260717_sha256.csv",
    "18_CJK_Visual_Evidence_Rights_Blocked_Metadata_20260722.jsonl",
    "18_CJK_Visual_Evidence_Schema_20260722.md",
    "18_CJK_Visual_Evidence_Scope_Caveats_20260722.md",
    "19a_Interslavic_Vaziti_Relevant_Dictionary_Rows_20260801.csv",
    "19b_Interslavic_Vaziti_Source_Snapshot_Metadata_20260801.json",
    "19c_Interslavic_Vaziti_Source_Anchor_SHA256SUMS_20260801.csv",
    "20a_Fable_Tranche001_Requirements_Acknowledgement_Validation_20260801.json",
    "20b_Fable_Tranche001_Requirements_Acknowledgement_SHA256SUMS_20260801.csv",
    "21a_Fable_G15_Source_Anchor_Readme_20260801.md",
    "21b_Fable_G15_Source_Anchor_Metadata_20260801.json",
    "21c_Fable_G15_Source_Anchor_Validation_20260801.json",
    "21d_Fable_G15_Source_Anchor_SHA256SUMS_20260801.csv",
)
COMPACT_ZIP_NAME = "25_Retained_Legacy_Companion_Metadata_20260803.zip"
COMPACT_MANIFEST_NAME = (
    "25a_Retained_Legacy_Companion_Metadata_20260803_MANIFEST.csv"
)


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
    file_surface_sha256: str
    version: str
    default_preview: str
    include_ega: bool
    include_v3: bool
    compact_methodology: bool


TARGETS = (
    Target(
        key="ega",
        predecessor=21_764_491,
        doi="10.5281/zenodo.21764491",
        concept_doi="10.5281/zenodo.20414353",
        title="Elements de geometrie algebrique (EGA): English Working Readers and Buildable TeX",
        files=49,
        total_bytes=3_773_174_458,
        revision=3,
        file_surface_sha256="8EB93180A90EEA73242E1967B62BE27F973AC9BFE7782EF9086D389E21DE291F",
        version="2026-08-03 EGA I diplomatic French and paired English through p.127",
        default_preview="00_GLOBAL_EGA_0_IV_English_Complete_Linked_Reader_20260801.pdf",
        include_ega=True,
        include_v3=False,
        compact_methodology=False,
    ),
    Target(
        key="methodology",
        predecessor=21_780_213,
        doi="10.5281/zenodo.21780213",
        concept_doi="10.5281/zenodo.21124403",
        title="Interlanguage and Mathematical Translation Methodology Sidecar",
        files=100,
        total_bytes=4_990_626_114,
        revision=3,
        file_surface_sha256="00CA9AB075415B5C8530BAC2228E60581FFCF711F0E702E5F81AC7F45A89163F",
        version="2026-08-03 EGA p.127 and 482-record audit successor",
        default_preview="00_Interlanguage_Methodology_Current_v13_20260718.pdf",
        include_ega=True,
        include_v3=True,
        compact_methodology=True,
    ),
    Target(
        key="replication",
        predecessor=21_780_218,
        doi="10.5281/zenodo.21780218",
        concept_doi="10.5281/zenodo.20461174",
        title="AI-Run Modern LaTeX Manuscript Workflow and Replication Packet",
        files=65,
        total_bytes=9_027_091,
        revision=3,
        file_surface_sha256="7C2A7356A00E89F74FE865AF2993F671E903A92A397B3618A2539807D3762011",
        version="2026-08-03 EGA p.127 and 482-record audit successor",
        default_preview="00_AI_Run_Modern_LaTeX_Manuscript_Workflow_Current_20260728.pdf",
        include_ega=True,
        include_v3=True,
        compact_methodology=False,
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


def file_surface_sha256(entries: dict[str, dict]) -> str:
    lines = [
        f"{name}\t{int(entries[name]['size'])}\t{base.normalized_md5(entries[name]['checksum'])}"
        for name in sorted(entries, key=str.casefold)
    ]
    return sha256_bytes("\n".join(lines).encode("utf-8"))


def load_state() -> dict:
    if STATE.is_file():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {"targets": {}}


def save_state(value: dict) -> None:
    TEMP.mkdir(parents=True, exist_ok=True)
    base.save_json(STATE, value)


def auth_modern(token: str) -> dict[str, str]:
    return {**MODERN, "Authorization": f"Bearer {token}"}


def fetch_public(session, record_id: int) -> dict:
    return base.check(
        session.get(
            f"{API}/records/{record_id}?expand=true",
            headers=MODERN,
            timeout=(30, 300),
        ),
        {200},
    ).json()


def fetch_predecessor(session, target: Target, require_latest: bool) -> tuple[dict, dict[str, dict]]:
    record = fetch_public(session, target.predecessor)
    entries = base.modern_entries(record)
    if (
        int(record["id"]) != target.predecessor
        or record["pids"]["doi"]["identifier"] != target.doi
        or record["parent"]["pids"]["doi"]["identifier"] != target.concept_doi
        or record["metadata"]["title"] != target.title
        or record.get("is_published") is not True
        or len(entries) != target.files
        or sum(int(row["size"]) for row in entries.values()) != target.total_bytes
        or int(record.get("revision_id", 0)) != target.revision
        or file_surface_sha256(entries) != target.file_surface_sha256
    ):
        raise RuntimeError(f"{target.key} predecessor boundary changed")
    if require_latest:
        latest = base.check(
            session.get(record["links"]["latest"], headers=MODERN, timeout=(30, 300)),
            {200},
        ).json()
        if int(latest["id"]) != target.predecessor:
            raise RuntimeError(f"{target.key} concept head moved")
    return record, entries


def assert_no_duplicate_concept(session, token: str, target: Target) -> None:
    response = base.check(
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
        for row in response.get("hits", {}).get("hits", [])
        if row.get("metadata", {}).get("title") == target.title
    ]
    concepts = {
        row.get("parent", {}).get("pids", {}).get("doi", {}).get("identifier")
        for row in exact
    }
    concepts.discard(None)
    if concepts != {target.concept_doi}:
        raise RuntimeError(f"{target.key} duplicate-concept guard changed: {sorted(concepts)}")


def assert_no_active_draft(session, token: str, target: Target) -> None:
    response = session.get(
        f"{API}/records/{target.predecessor}/draft?expand=true",
        headers=auth_modern(token),
        timeout=(30, 180),
    )
    if response.status_code != 404:
        raise RuntimeError(f"{target.key} has an active untracked draft")


def load_manifest(root: Path, name: str) -> dict[str, dict[str, str]]:
    with (root / name).open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    return {row["relative_path"]: row for row in rows}


def validate_local_packages() -> None:
    ega_manifest = load_manifest(EGA_ROOT, "11_ZENODO_UPLOAD_MANIFEST.csv")
    v3_manifest = load_manifest(V3_ROOT, "06_ZENODO_UPLOAD_MANIFEST.csv")
    for root, manifest, names, extras in (
        (EGA_ROOT, ega_manifest, EGA_SELECTED, EGA_EXTRA_IDENTITIES),
        (V3_ROOT, v3_manifest, V3_SELECTED, {}),
    ):
        for name in names:
            if name in manifest:
                wanted = int(manifest[name]["bytes"]), manifest[name]["sha256"].upper()
            elif name in extras:
                wanted = extras[name]
            else:
                raise RuntimeError(f"Upload manifest does not bind {name}")
            path = root / name
            observed = path.stat().st_size, sha256_path(path)
            if observed != wanted:
                raise RuntimeError(f"Local package identity changed: {path}")
    for path in (EGA_ROOT / "12_PACKAGE_VALIDATION.json", V3_ROOT / "07_PACKAGE_VALIDATION.json"):
        value = json.loads(path.read_text(encoding="utf-8"))
        if value.get("errors") != [] or not str(value.get("status", "")).startswith("PASS"):
            raise RuntimeError(f"Package validation is not PASS: {path}")
    v3_validation = json.loads(
        (V3_ROOT / "07_PACKAGE_VALIDATION.json").read_text(encoding="utf-8")
    )
    if v3_validation.get("records") != 482:
        raise RuntimeError("Decision-log v3 record count changed")


def download_exact(session, entry: dict, destination: Path) -> None:
    wanted = identity(entry)
    if destination.is_file() and (
        destination.stat().st_size,
        md5_path(destination),
    ) == wanted:
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
        raise RuntimeError(f"Downloaded predecessor byte mismatch: {destination.name}")
    os.replace(partial, destination)


def deterministic_member(archive: zipfile.ZipFile, name: str, payload: bytes) -> None:
    info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    archive.writestr(info, payload, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


def build_methodology_compaction(
    session, predecessor_entries: dict[str, dict]
) -> tuple[dict[str, dict[str, object]], list[dict[str, object]]]:
    missing = set(COMPACT_NAMES) - set(predecessor_entries)
    if missing:
        raise RuntimeError(f"Methodology compaction members missing: {sorted(missing)}")
    source_dir = TEMP / "methodology-legacy-companion-source"
    rows: list[dict[str, object]] = []
    for name in COMPACT_NAMES:
        path = source_dir / name
        download_exact(session, predecessor_entries[name], path)
        entry = predecessor_entries[name]
        rows.append(
            {
                "member_path": name,
                "bytes": path.stat().st_size,
                "md5": md5_path(path),
                "sha256": sha256_path(path),
                "source_record": TARGETS[1].predecessor,
                "source_doi": TARGETS[1].doi,
                "source_content_url": entry["links"]["content"],
                "disposition": (
                    "exact predecessor byte preserved in indexed ZIP; predecessor retains direct form"
                ),
            }
        )
    manifest = TEMP / COMPACT_MANIFEST_NAME
    fields = list(rows[0])
    with manifest.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    zip_path = TEMP / COMPACT_ZIP_NAME
    with zipfile.ZipFile(zip_path, "w") as archive:
        for row in rows:
            deterministic_member(
                archive,
                str(row["member_path"]),
                (source_dir / str(row["member_path"])).read_bytes(),
            )
        deterministic_member(archive, "MANIFEST.csv", manifest.read_bytes())
    with zipfile.ZipFile(zip_path) as archive:
        expected_names = list(COMPACT_NAMES) + ["MANIFEST.csv"]
        if archive.namelist() != expected_names:
            raise RuntimeError("Legacy companion ZIP member order changed")
        for row in rows:
            payload = archive.read(str(row["member_path"]))
            if (len(payload), sha256_bytes(payload)) != (
                int(row["bytes"]),
                str(row["sha256"]),
            ):
                raise RuntimeError(f"Legacy companion ZIP member changed: {row['member_path']}")
        manifest_payload = archive.read("MANIFEST.csv")
        if manifest_payload != manifest.read_bytes():
            raise RuntimeError("Legacy companion embedded manifest changed")
    return {
        COMPACT_ZIP_NAME: file_row(zip_path),
        COMPACT_MANIFEST_NAME: file_row(manifest),
    }, rows


def local_uploads(
    target: Target, compaction: dict[str, dict[str, object]]
) -> dict[str, dict[str, object]]:
    uploads: dict[str, dict[str, object]] = {}
    if target.include_ega:
        for name in EGA_SELECTED:
            uploads[EGA_REMOTE_PREFIX + name] = file_row(EGA_ROOT / name)
    if target.include_v3:
        for name in V3_SELECTED:
            uploads[name] = file_row(V3_ROOT / name)
    if target.compact_methodology:
        uploads.update(compaction)
    if len(uploads) != len(set(uploads)):
        raise RuntimeError(f"{target.key} upload-name collision")
    return uploads


def remove_names(target: Target) -> set[str]:
    names: set[str] = set()
    if target.include_v3:
        names |= V2_NAMES
    if target.compact_methodology:
        names |= set(COMPACT_NAMES)
    return names


def preflight(session, token: str, state: dict, source_commit: str | None) -> dict:
    validate_local_packages()
    snapshots: dict[str, object] = {}
    methodology_entries: dict[str, dict] | None = None
    for target in TARGETS:
        record, entries = fetch_predecessor(session, target, require_latest=True)
        assert_no_duplicate_concept(session, token, target)
        tracked = state.get("targets", {}).get(target.key, {})
        if not tracked.get("draft_id"):
            assert_no_active_draft(session, token, target)
        snapshots[target.key] = {
            "predecessor": target.predecessor,
            "doi": target.doi,
            "concept_doi": target.concept_doi,
            "files": len(entries),
            "bytes": sum(int(row["size"]) for row in entries.values()),
            "file_surface_sha256": file_surface_sha256(entries),
            "default_preview": record["files"].get("default_preview"),
            "active_draft": bool(tracked.get("draft_id")),
            "duplicate_concept": False,
        }
        if target.key == "methodology":
            methodology_entries = entries
    if methodology_entries is None:
        raise RuntimeError("Methodology surface was not loaded")
    compaction, compact_rows = build_methodology_compaction(session, methodology_entries)
    upload_summary: dict[str, object] = {}
    for target in TARGETS:
        uploads = local_uploads(target, compaction)
        desired_count = target.files - len(remove_names(target)) + len(uploads)
        wanted_count = {"ega": 58, "methodology": 99, "replication": 76}[target.key]
        if desired_count != wanted_count or desired_count > 100:
            raise RuntimeError(f"{target.key} successor file-count calculation changed")
        upload_summary[target.key] = {
            "remove_files": sorted(remove_names(target), key=str.casefold),
            "add_files": {
                name: {key: row[key] for key in ("bytes", "sha256", "md5")}
                for name, row in sorted(uploads.items(), key=lambda item: item[0].casefold())
            },
            "successor_files": desired_count,
        }
    if source_commit is not None:
        if not re.fullmatch(r"[0-9a-f]{40}", source_commit):
            raise RuntimeError("source commit must be a lowercase 40-character Git SHA")
        state["source_commit"] = source_commit
    state["status"] = "PREFLIGHT_PASS_NO_ZENODO_MUTATION"
    state["preflight"] = {
        "targets": snapshots,
        "uploads": upload_summary,
        "methodology_compaction": {
            "members": len(compact_rows) + 1,
            "represented_predecessor_files": len(compact_rows),
            "zip": {key: compaction[COMPACT_ZIP_NAME][key] for key in ("bytes", "sha256", "md5")},
            "manifest": {
                key: compaction[COMPACT_MANIFEST_NAME][key]
                for key in ("bytes", "sha256", "md5")
            },
        },
    }
    save_state(state)
    return state


def create_tracked_drafts(session, token: str, state: dict) -> dict:
    source_commit = state.get("source_commit")
    if not isinstance(source_commit, str) or not re.fullmatch(r"[0-9a-f]{40}", source_commit):
        raise RuntimeError("Run preflight with the exact source commit before prepare")
    auth_legacy = {"Authorization": f"Bearer {token}"}
    for target in TARGETS:
        tracked = state.setdefault("targets", {}).setdefault(target.key, {})
        if tracked.get("draft_id"):
            probe = session.get(
                f"{API}/records/{int(tracked['draft_id'])}/draft?expand=true",
                headers=auth_modern(token),
                timeout=(30, 300),
            )
            if probe.status_code != 200:
                raise RuntimeError(f"Tracked {target.key} draft is no longer active")
            continue
        record, entries = fetch_predecessor(session, target, require_latest=True)
        assert_no_duplicate_concept(session, token, target)
        assert_no_active_draft(session, token, target)
        deposition = base.check(
            session.get(
                f"{API}/deposit/depositions/{target.predecessor}",
                headers=auth_legacy,
                timeout=(30, 300),
            ),
            {200},
        ).json()
        created = base.check(
            session.post(
                deposition["links"]["newversion"],
                headers=auth_legacy,
                timeout=(30, 600),
            ),
            {201},
        ).json()
        draft = base.check(
            session.get(created["links"]["latest_draft"], headers=auth_legacy, timeout=(30, 300)),
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
        save_state(state)
        print(f"created tracked {target.key} draft {draft['id']}", flush=True)
    state["status"] = "PREPARED_THREE_TRACKED_DRAFTS"
    save_state(state)
    return state


def upload_file(session, token: str, bucket: str, name: str, path: Path) -> None:
    print(f"upload {name} ({path.stat().st_size} bytes)", flush=True)
    with path.open("rb") as handle:
        base.check(
            session.put(
                f"{bucket.rstrip('/')}/{urllib.parse.quote(name, safe='')}",
                headers={
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/octet-stream",
                },
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


def description(target: Target, source_commit: str) -> str:
    ega_url = (
        f"{GITHUB_REPO}/tree/{source_commit}/sources/ega/checkpoints/"
        "ega1-p127-diplomatic-prestacks-r1-20260803"
    )
    v3_url = (
        f"{GITHUB_REPO}/tree/{source_commit}/interlanguage-sidecar/20260803/"
        "english-germanic-decision-log-privacy-v3"
    )
    fac = (
        '<p><strong>Dedicated FAC quality assessment:</strong> use '
        f'<a href="https://doi.org/{FAC_CONCEPT_DOI}">{FAC_CONCEPT_DOI}</a> '
        f'(published version <a href="https://doi.org/{FAC_VERSION_DOI}">{FAC_VERSION_DOI}</a>) '
        "for the coherent FAC evidence package. It records that the orchestrator did not know "
        "the Achinger-Krupa translation existed when Codex translated and froze FAC nos. 1-79; "
        "the comparator was discovered afterward, and all 79 units were then adjudicated against "
        "the French authority. Nos. 80-81 are outside the blind claim. The evidence is qualitative, "
        "not a scalar score, ranking, certification, or general superiority claim. Its payload is "
        "not duplicated here; earlier broad FAC projections remain immutable adverse history, and "
        "GAGA remains a separate publication line.</p>"
    )
    if target.key == "ega":
        return (
            '<p><strong>Read EGA:</strong> open <code>00_GLOBAL_EGA_0_IV_English_Complete_Linked_Reader_20260801.pdf</code> '
            "for the continuous EGA 0-IV working reader; it is the default preview.</p>"
            '<p><strong>Download the current reader/source package:</strong> <code>00 Current_EGA_English_Readers_and_Buildable_TeX_20260801.zip</code> '
            "contains the global reader, five standalone readers, and buildable TeX for all six reader surfaces.</p>"
            "<p><strong>Reader coverage:</strong> EGA 0 through Section 13; EGA I and II through EOF; "
            "the published EGA III text through 7.9.14; and EGA IV Sections 1-21 through EOF. "
            "The 1,356-page global reader has 15,383 destinations and 17,808 resolved internal links.</p>"
            "<p><strong>Canonical French and pre-Stacks work:</strong> this same concept also preserves "
            "a bounded, coherent EGA I checkpoint through printed p.127: diplomatic French R50, "
            "paired English through R59, 127 exact English source identities, and the French-rooted "
            "pre-Stacks indexing scaffold. The full EGA French canon and semantic graph remain "
            "incomplete; p.128 is the next production cursor.</p>"
            '<p><strong>Audit and provenance:</strong> the p.127 source ZIP, machine-readable scaffold, '
            "privacy-clean project logbook, continuation handoff, status, French/English/error "
            "append-only ledgers, and package validation are direct files. Exact private custody "
            "retains unchanged source bytes; the public projection records each minimal privacy "
            f'transformation. Commit-pinned source: <a href="{ega_url}">{source_commit}</a>. '
            'Methodology: <a href="https://doi.org/10.5281/zenodo.21124403">10.5281/zenodo.21124403</a>; '
            'replication: <a href="https://doi.org/10.5281/zenodo.20461174">10.5281/zenodo.20461174</a>.</p>'
            "<p><strong>Status and rights:</strong> these are working readers and preservation checkpoints, "
            "not critical editions, source-fidelity or mathematical certifications, new rights grants, "
            "or claims that the whole French corpus or pre-Stacks graph is complete. French and third-party "
            "rights remain with their rightsholders.</p>"
        )
    if target.key == "methodology":
        return (
            '<p><strong>Open first:</strong> <code>00_Interlanguage_Methodology_Current_v13_20260718.pdf</code> '
            "is the default preview and maps the stable manuscript, reader, methodology, and provenance homes.</p>"
            "<p><strong>Purpose:</strong> this concept is the methodology, provenance, corpus-control, "
            "decision-rationale, and programme-state sidecar for the mathematical transcription and "
            "translation archive. It preserves source-body baselines, workflow controls, weighted-automaton "
            "and terminology work, correction and reversal histories, continuation state, reproducible "
            "checks, and bounded interlanguage experiments; full mathematical readers remain on their "
            "author or series concepts.</p>"
            "<p><strong>Current audit surface:</strong> the privacy-clean English/Germanic decision log has "
            "482 append-only records in exact order, with 2,427 event-level privacy transformations and "
            "no omitted decisions. The direct log, transformation ledger, validator, explanatory note, "
            "manifest, and deterministic provenance ZIP make the projection independently replayable. "
            f'Commit-pinned audit projection: <a href="{v3_url}">{source_commit}</a>.</p>'
            "<p><strong>EGA canonical-French checkpoint:</strong> direct files preserve the coherent EGA I "
            "p.127 diplomatic-French/paired-English checkpoint, the French-rooted pre-Stacks indexing "
            "scaffold, privacy-clean project logbook, decision/error/reversal ledgers, status, continuation "
            "handoff, and validation. This is a bounded checkpoint, not completion of EGA 0-IV. "
            f'Commit-pinned checkpoint: <a href="{ega_url}">{source_commit}</a>.</p>'
            + fac
            + "<p><strong>Archive organization:</strong> the numbered interlanguage, CJK, Noether, Fable, "
            "Persian, Tajik, Deligne, SGA, EGA, and historical FAC surfaces remain preserved. Fourteen small "
            "legacy companion metadata files are retained byte-for-byte in an indexed deterministic ZIP to "
            "stay below Zenodo's 100-file ceiling; predecessor versions retain their direct forms. No distinct "
            "content is selected away.</p>"
            "<p><strong>Limits:</strong> these model-built methodology, corpus, normalization, translation, "
            "provenance, and visual-QA artifacts do not claim native-language validation, translation or "
            "source-fidelity certification, mathematical correctness, rights clearance, critical-edition "
            "status, peer review, or completion of any author corpus.</p>"
        )
    return (
        '<p><strong>Open first:</strong> <code>00_AI_Run_Modern_LaTeX_Manuscript_Workflow_Current_20260728.pdf</code> '
        "is the default preview for the current workflow and replication packet.</p>"
        "<p><strong>Purpose:</strong> this concept preserves the reproducible workflow, source-control and "
        "visual-QA methods, decision and correction trails, exact manifests, research-methodology briefings, "
        "and public-safe replication surfaces used across the manuscript archive. Production tasks remain "
        "responsible for translation, transcription, source adjudication, mathematics, diagrams, and visual QA.</p>"
        "<p><strong>Current audit surface:</strong> the privacy-clean English/Germanic decision log contains "
        "482 append-only records in exact order, with 2,427 event-level transformations and no omitted "
        "decisions. The direct log, ledger, validator, note, manifest, and deterministic provenance ZIP are "
        f'byte-identical counterparts of the methodology surface. Commit-pinned projection: <a href="{v3_url}">{source_commit}</a>.</p>'
        "<p><strong>EGA replication checkpoint:</strong> direct files expose the EGA I p.127 source ZIP, "
        "French-rooted pre-Stacks scaffold, privacy-clean project logbook, continuation and status records, "
        "French/English/error append-only ledgers, and package validation. The checkpoint is coherent but "
        "does not claim completion of the French EGA corpus or semantic graph. "
        f'Commit-pinned source: <a href="{ega_url}">{source_commit}</a>.</p>'
        + fac
        + "<p><strong>Method boundary:</strong> source images and authoritative texts decide genuine ambiguities; "
        "OCR and generated research notes remain locators or evidence, not source authority. Native editable "
        "mathematical diagrams and exact references belong in reader/source successors, while workflow/status "
        "commentary remains in external provenance surfaces rather than reader PDFs.</p>"
        "<p><strong>Limits:</strong> this packet supports audit and replication but does not certify a translation, "
        "transcription, edition, mathematical claim, software system, rights status, or whole-project completion.</p>"
    )


def desired_order(target: Target, names: set[str]) -> list[str]:
    if target.key == "ega":
        front = [
            "00 Current_EGA_English_Readers_and_Buildable_TeX_20260801.zip",
            "00_GLOBAL_EGA_0_IV_English_Complete_Linked_Reader_20260801.pdf",
        ]
    elif target.key == "methodology":
        front = [
            target.default_preview,
            "00_Interlanguage_Methodology_Current_v13_20260718.md",
            *V3_SELECTED,
            *(EGA_REMOTE_PREFIX + name for name in EGA_SELECTED),
        ]
    else:
        front = [
            target.default_preview,
            "00_AI_Run_Modern_LaTeX_Manuscript_Workflow_Current_20260728.md",
            *V3_SELECTED,
            *(EGA_REMOTE_PREFIX + name for name in EGA_SELECTED),
        ]
    missing = [name for name in front if name not in names]
    if missing:
        raise RuntimeError(f"{target.key} front-order file missing: {missing}")
    seen: set[str] = set()
    order: list[str] = []
    for name in front + sorted(names, key=str.casefold):
        if name not in seen:
            seen.add(name)
            order.append(name)
    if set(order) != names:
        raise RuntimeError(f"{target.key} file order does not cover the whole surface")
    return order


def staged_metadata(target: Target, predecessor: dict, draft: dict, source_commit: str) -> dict:
    metadata = copy.deepcopy(predecessor["metadata"])
    metadata["publication_date"] = PUBLICATION_DATE
    metadata["version"] = target.version
    metadata["description"] = description(target, source_commit)
    metadata.pop("additional_descriptions", None)
    ega_url = (
        f"{GITHUB_REPO}/tree/{source_commit}/sources/ega/checkpoints/"
        "ega1-p127-diplomatic-prestacks-r1-20260803"
    )
    add_related(metadata, ega_url, "url", "issupplementedby")
    if target.include_v3:
        v3_url = (
            f"{GITHUB_REPO}/tree/{source_commit}/interlanguage-sidecar/20260803/"
            "english-germanic-decision-log-privacy-v3"
        )
        add_related(metadata, v3_url, "url", "issupplementedby")
        add_related(metadata, FAC_CONCEPT_DOI, "doi", "references")
        add_related(metadata, FAC_VERSION_DOI, "doi", "references")
    return metadata


def stage_target(
    session,
    token: str,
    target: Target,
    uploads: dict[str, dict[str, object]],
    state: dict,
) -> None:
    tracked = state["targets"][target.key]
    if tracked.get("status") in {
        "STAGED_VALIDATED",
        "PUBLISHED_READBACK_PENDING",
        "CLOSED_PUBLIC_READBACK_PASS",
    }:
        return
    predecessor, predecessor_entries = fetch_predecessor(session, target, require_latest=True)
    draft_id = int(tracked["draft_id"])
    auth_legacy = {"Authorization": f"Bearer {token}"}
    deposition = base.check(
        session.get(
            f"{API}/deposit/depositions/{draft_id}",
            headers=auth_legacy,
            timeout=(30, 300),
        ),
        {200},
    ).json()
    staged = base.legacy_entries(deposition)
    removals = remove_names(target)
    for name in sorted(removals | set(uploads), key=str.casefold):
        if name not in staged:
            continue
        wanted = uploads.get(name)
        observed = (
            int(staged[name]["filesize"]),
            base.normalized_md5(staged[name]["checksum"]),
        )
        if wanted and observed == (int(wanted["bytes"]), str(wanted["md5"])):
            continue
        base.check(
            session.delete(
                staged[name]["links"]["self"],
                headers=auth_legacy,
                timeout=(30, 300),
            ),
            {204},
        )
    deposition = base.check(
        session.get(
            f"{API}/deposit/depositions/{draft_id}",
            headers=auth_legacy,
            timeout=(30, 300),
        ),
        {200},
    ).json()
    staged = base.legacy_entries(deposition)
    for name, row in uploads.items():
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
    desired = (set(predecessor_entries) - removals) | set(uploads)
    if set(entries) != desired or len(entries) > 100:
        raise RuntimeError(f"{target.key} staged file boundary changed")
    for name, row in uploads.items():
        if identity(entries[name]) != (int(row["bytes"]), str(row["md5"])):
            raise RuntimeError(f"{target.key} staged upload changed: {name}")
    for name in desired - set(uploads):
        if identity(entries[name]) != identity(predecessor_entries[name]):
            raise RuntimeError(f"{target.key} retained predecessor file changed: {name}")
    order = desired_order(target, desired)
    payload = {
        "access": predecessor["access"],
        "files": {
            "enabled": True,
            "default_preview": target.default_preview,
            "order": order,
        },
        "metadata": staged_metadata(
            target, predecessor, draft, str(state["source_commit"])
        ),
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
    if (
        set(base.modern_entries(patched)) != desired
        or patched["files"].get("default_preview") != target.default_preview
        or patched["files"].get("order") != order
        or patched["metadata"].get("description") != payload["metadata"]["description"]
    ):
        raise RuntimeError(f"{target.key} staged metadata/presentation changed")
    tracked.update(
        {
            "status": "STAGED_VALIDATED",
            "staged_files": len(entries),
            "staged_bytes": sum(int(row["size"]) for row in entries.values()),
            "staged_file_surface_sha256": file_surface_sha256(entries),
            "removed_predecessor_files": sorted(removals, key=str.casefold),
            "new_upload_files": sorted(uploads, key=str.casefold),
        }
    )
    save_state(state)
    print(f"staged and validated {target.key} draft {draft_id}", flush=True)


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
    raise RuntimeError(f"Published record {record_id} did not become publicly readable")


def readback_compaction(session, entry: dict, compact_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    response = base.check(session.get(entry["links"]["content"], timeout=(30, 600)), {200})
    observed: list[dict[str, object]] = []
    with zipfile.ZipFile(io.BytesIO(response.content)) as archive:
        for name in archive.namelist():
            payload = archive.read(name)
            observed.append(
                {"member_path": name, "bytes": len(payload), "sha256": sha256_bytes(payload)}
            )
    expected = [
        {
            "member_path": str(row["member_path"]),
            "bytes": int(row["bytes"]),
            "sha256": str(row["sha256"]),
        }
        for row in compact_rows
    ]
    manifest = TEMP / COMPACT_MANIFEST_NAME
    expected.append(
        {
            "member_path": "MANIFEST.csv",
            "bytes": manifest.stat().st_size,
            "sha256": sha256_path(manifest),
        }
    )
    if observed != expected:
        raise RuntimeError("Methodology public compaction ZIP member readback changed")
    return observed


def publish_and_readback(
    session,
    token: str,
    target: Target,
    uploads: dict[str, dict[str, object]],
    compact_rows: list[dict[str, object]],
    state: dict,
) -> dict:
    tracked = state["targets"][target.key]
    draft_id = int(tracked["draft_id"])
    predecessor, predecessor_entries = fetch_predecessor(
        session, target, require_latest=not bool(tracked.get("published_record"))
    )
    removals = remove_names(target)
    desired = (set(predecessor_entries) - removals) | set(uploads)
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
            raise RuntimeError(f"{target.key} draft is not staged/validated")
        published = base.check(
            session.post(
                draft["links"]["publish"],
                headers=auth_modern(token),
                timeout=(30, 1200),
            ),
            {200, 202},
        ).json()
        if int(published["id"]) != draft_id:
            raise RuntimeError(f"{target.key} published record differs from tracked draft")
        tracked.update(
            {"status": "PUBLISHED_READBACK_PENDING", "published_record": draft_id}
        )
        save_state(state)
        print(f"published {target.key} record {draft_id}", flush=True)
    record_id = int(tracked["published_record"])
    record = wait_public(session, record_id, desired)
    entries = base.modern_entries(record)
    readback: dict[str, dict[str, object]] = {}
    for name, row in sorted(uploads.items(), key=lambda item: item[0].casefold()):
        observed = stream_readback(session, entries[name]["links"]["content"])
        wanted = int(row["bytes"]), str(row["sha256"])
        if observed != wanted:
            raise RuntimeError(f"{target.key} public upload readback changed: {name}")
        readback[name] = {
            "bytes": observed[0],
            "sha256": observed[1],
            "match": True,
            "content_url": entries[name]["links"]["content"],
        }
    compact_readback: list[dict[str, object]] = []
    if target.compact_methodology:
        compact_readback = readback_compaction(
            session, entries[COMPACT_ZIP_NAME], compact_rows
        )
    retained = desired - set(uploads)
    retained_mismatches = [
        name
        for name in retained
        if identity(entries[name]) != identity(predecessor_entries[name])
    ]
    if retained_mismatches or removals & set(entries):
        raise RuntimeError(f"{target.key} retained/superseded public boundary changed")
    if record["files"].get("default_preview") != target.default_preview:
        raise RuntimeError(f"{target.key} public default preview changed")
    if record["metadata"].get("description") != description(
        target, str(state["source_commit"])
    ):
        raise RuntimeError(f"{target.key} public landing description changed")
    versions = base.check(
        session.get(
            record["links"]["versions"],
            params={"size": 100},
            headers=auth_modern(token),
            timeout=(30, 300),
        ),
        {200},
    ).json()
    by_index = {
        int(row["versions"]["index"]): int(row["id"])
        for row in versions.get("hits", {}).get("hits", [])
    }
    predecessor_index = int(predecessor["versions"]["index"])
    latest = base.check(
        session.get(record["links"]["latest"], headers=MODERN, timeout=(30, 300)),
        {200},
    ).json()
    draft_probe = session.get(
        f"{API}/records/{record_id}/draft",
        headers=auth_modern(token),
        timeout=(30, 180),
    )
    assert_no_duplicate_concept(session, token, target)
    if (
        int(record["versions"]["index"]) != predecessor_index + 1
        or by_index.get(predecessor_index) != target.predecessor
        or int(latest["id"]) != record_id
        or draft_probe.status_code != 404
    ):
        raise RuntimeError(f"{target.key} predecessor/latest/draft closeout changed")
    result = {
        "status": "PASS_PUBLISHED_AND_ANONYMOUS_RAW_READBACK",
        "errors": [],
        "target": target.key,
        "record_id": record_id,
        "doi": record["pids"]["doi"]["identifier"],
        "concept_doi": target.concept_doi,
        "public_url": f"https://zenodo.org/records/{record_id}",
        "predecessor_record": target.predecessor,
        "predecessor_doi": target.doi,
        "source_commit": state["source_commit"],
        "files": len(entries),
        "bytes": sum(int(row["size"]) for row in entries.values()),
        "file_surface_sha256": file_surface_sha256(entries),
        "default_preview": target.default_preview,
        "file_order": record["files"].get("order", []),
        "landing_description_sha256": sha256_bytes(
            record["metadata"]["description"].encode("utf-8")
        ),
        "removed_from_successor_direct_surface": sorted(removals, key=str.casefold),
        "removed_bytes_preserved_in_predecessor": True,
        "retained_predecessor_files": len(retained),
        "retained_identity_mismatches": retained_mismatches,
        "new_uploads": readback,
        "new_upload_readback_matches": len(readback),
        "new_upload_readback_mismatches": 0,
        "compaction_zip_member_readback": compact_readback,
        "active_draft": False,
        "duplicate_concept": False,
        "new_concept_created": False,
        "fac_concept_mutated": False,
        "fac_payload_files_added": 0,
        "gaga_payload_files_added": 0,
    }
    receipt = RECEIPT_ROOT / (
        f"20260803_ega_p127_decision_log_v3_{target.key}_record_{record_id}_public_readback.json"
    )
    base.save_json(receipt, result)
    tracked.update(
        {
            "status": "CLOSED_PUBLIC_READBACK_PASS",
            "receipt": receipt.relative_to(REPO).as_posix(),
            "doi": result["doi"],
        }
    )
    save_state(state)
    return result


def publish_all(session, token: str, state: dict) -> list[dict]:
    if state.get("status") not in {
        "PREPARED_THREE_TRACKED_DRAFTS",
        "STAGED_ALL_THREE_VALIDATED",
        "PUBLICATION_IN_PROGRESS",
    }:
        raise RuntimeError("Run preflight and prepare before publish")
    validate_local_packages()
    methodology, methodology_entries = fetch_predecessor(
        session, TARGETS[1], require_latest=not bool(
            state.get("targets", {}).get("methodology", {}).get("published_record")
        )
    )
    del methodology
    compaction, compact_rows = build_methodology_compaction(session, methodology_entries)
    uploads_by_target = {
        target.key: local_uploads(target, compaction) for target in TARGETS
    }
    for target in TARGETS:
        stage_target(session, token, target, uploads_by_target[target.key], state)
    state["status"] = "STAGED_ALL_THREE_VALIDATED"
    save_state(state)
    results: list[dict] = []
    state["status"] = "PUBLICATION_IN_PROGRESS"
    save_state(state)
    for target in TARGETS:
        if state["targets"][target.key].get("status") == "CLOSED_PUBLIC_READBACK_PASS":
            receipt = REPO / state["targets"][target.key]["receipt"]
            results.append(json.loads(receipt.read_text(encoding="utf-8")))
            continue
        results.append(
            publish_and_readback(
                session,
                token,
                target,
                uploads_by_target[target.key],
                compact_rows,
                state,
            )
        )
    state["status"] = "CLOSED_THREE_CONCEPT_SUCCESSORS_PUBLIC_READBACK_PASS"
    save_state(state)
    base.save_json(
        RECEIPT_ROOT / "20260803_ega_p127_decision_log_v3_three_concept_closeout.json",
        {
            "status": state["status"],
            "errors": [],
            "source_commit": state["source_commit"],
            "results": results,
            "fac_dedicated_concept_unchanged": FAC_CONCEPT_DOI,
            "gaga_separate": True,
        },
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
            save_state(state)
        result = create_tracked_drafts(session, token, state)
    else:
        result = {
            "status": "CLOSED_THREE_CONCEPT_SUCCESSORS_PUBLIC_READBACK_PASS",
            "results": publish_all(session, token, state),
        }
    print(json.dumps(result, indent=2), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
