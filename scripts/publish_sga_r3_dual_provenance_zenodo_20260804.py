#!/usr/bin/env python3
"""Publish SGA R3 provenance on the existing methodology/replication concepts.

The standing BFA1E3A3... control requires directly readable logbooks,
decision/reversal history, and continuation surfaces on both DOI lineages.
This script builds one deterministic controls ZIP from the already-validated
SGA R3 package, stages exactly one tracked successor on each existing concept,
and requires both draft ids before publishing.

Zenodo caps records at 100 files.  Six machine-only direct duplicates are
therefore removed from the new broad heads only after proving their exact bytes
are already members of retained GAGA/FAC provenance ZIPs.  Human-readable
logbooks and ledgers remain direct, and immutable predecessors retain every
former direct surface.
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import io
import json
import os
import sys
import time
import zipfile
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote

import publish_current_reader_bundles_zenodo_20260730 as base
import publish_sga_global_reference_r3_zenodo_20260804 as sga


API = base.API
MODERN = {"Accept": "application/vnd.inveniordm.v1+json"}
REPO_ROOT = Path(__file__).resolve().parent.parent
PUBLICATION_DATE = "2026-08-04"
SGA_RECORD_ID = 21782424
SGA_RECORD_DOI = "10.5281/zenodo.21782424"
SGA_CONCEPT_DOI = "10.5281/zenodo.20410947"

CONTROL_SHA256 = (
    "BFA1E3A3EDA94E8C3425BAE50C842610A47D508FB260BF761BA3206883012679"
)
PROVENANCE_ZIP = "07_SGA_R3__00_COMPLETE_PROVENANCE_CONTROLS_20260804.zip"
ZIP_PREFIX = "SGA_R3_PROVENANCE_CONTROLS_20260804"
MEMBER_MANIFEST_NAME = "MEMBER_MANIFEST.csv"
EXPECTED_SOURCE_MEMBERS = 112
EXPECTED_ZIP_MEMBERS = 113

DIRECT_PATHS = {
    "07_SGA_R3__01_PACKAGE_LOGBOOK.md": "controls/PACKAGE_LOGBOOK.md",
    "07_SGA_R3__02_CROSS_VOLUME_LOGBOOK.md": (
        "controls/current_global_r3/R3_CROSS_VOLUME_LOGBOOK.md"
    ),
    "07_SGA_R3__03_CONTINUATION.md": (
        "controls/current_global_r3/R3_CONTINUATION.md"
    ),
    "07_SGA_R3__04_SUPERSESSION_AND_ORDER.csv": (
        "controls/CURRENT_SUPERSESSION_AND_ORDER.csv"
    ),
    "07_SGA_R3__05_PREDECESSOR_DECISION_LOG.csv": (
        "controls/history/presentation_clean_r2/DECISION_LOG.csv"
    ),
    "07_SGA_R3__06_PREDECESSOR_REVISION_HISTORY.csv": (
        "controls/history/presentation_clean_r2/REVISION_HISTORY.csv"
    ),
}

COMPACTED_DIRECT_FILES = {
    "06_GAGA__10_ARCHIVE_PRIVACY_TRANSFORMATIONS.csv",
    "06_GAGA__11_ARCHIVE_PRIVACY_VALIDATION.json",
    "06_GAGA__13_PROVENANCE.csv",
    "06_GAGA__14_ZENODO_PAYLOAD_MANIFEST.csv",
    "06_GAGA__15_COMPLETE_PROVENANCE_CONTROLS_MANIFEST.csv",
    "27a_FAC_BROAD_PROJECTION_ADVERSE_HISTORY_20260803_MANIFEST.csv",
}
GAGA_RECEIPT = (
    REPO_ROOT
    / "manifests/published-zenodo/20260803_gaga_dual_doi_publication_receipt.json"
)

LANDING_BLOCK = """<h2>Current SGA 1-7 II R3 provenance</h2>
<p>The current SGA working-reader successor is <a href="https://doi.org/10.5281/zenodo.21782424">version 10.5281/zenodo.21782424</a> on the existing <a href="https://doi.org/10.5281/zenodo.20410947">SGA concept</a>. It fronts the complete 152-member reader/source ZIP and the 4,179-page global cross-volume reader.</p>
<p>This record directly exposes the exact SGA R3 package logbook, cross-volume decision logbook, continuation record, supersession/rationale ledger, and the preserved presentation-clean decision and revision histories. The accompanying deterministic provenance ZIP retains all 106 package control files plus the six top-level package manifests and validations. These surfaces make the workflow, corrections, reversals, residual references, privacy decisions, and continuation state auditable; they do not certify the translation, mathematics, rights, or accessibility.</p>"""


@dataclass(frozen=True)
class Target:
    key: str
    predecessor_id: int
    predecessor_doi: str
    concept_id: str
    concept_doi: str
    files: int
    bytes: int
    preview: str
    version: str


TARGETS = {
    "methodology": Target(
        key="methodology",
        predecessor_id=21781388,
        predecessor_doi="10.5281/zenodo.21781388",
        concept_id="21124403",
        concept_doi="10.5281/zenodo.21124403",
        files=99,
        bytes=4_993_297_296,
        preview="00_Interlanguage_Methodology_Current_v13_20260718.pdf",
        version="2026-08-04 SGA R3 provenance and global-reference controls",
    ),
    "replication": Target(
        key="replication",
        predecessor_id=21781392,
        predecessor_doi="10.5281/zenodo.21781392",
        concept_id="20461174",
        concept_doi="10.5281/zenodo.20461174",
        files=76,
        bytes=11_726_773,
        preview="00_AI_Run_Modern_LaTeX_Manuscript_Workflow_Current_20260728.pdf",
        version="2026-08-04 SGA R3 provenance and replication controls",
    ),
}

TEMP_ROOT = (
    Path(os.environ.get("LOCALAPPDATA", os.environ.get("TEMP", ".")))
    / "Temp"
    / "sga_r3_dual_provenance_20260804"
)
STATE_PATH = TEMP_ROOT / "state.json"
DERIVED_ROOT = TEMP_ROOT / "derived"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def md5(path: Path) -> str:
    digest = hashlib.md5(usedforsecurity=False)
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().lower()


def normalized_md5(value: str) -> str:
    return str(value).lower().removeprefix("md5:")


def modern_entries(record: dict) -> dict[str, dict]:
    return record.get("files", {}).get("entries", {})


def legacy_entries(record: dict) -> dict[str, dict]:
    return {row["filename"]: row for row in record.get("files", [])}


def identity(entry: dict) -> tuple[int, str]:
    return int(entry["size"]), normalized_md5(entry["checksum"])


def legacy_identity(entry: dict) -> tuple[int, str]:
    return int(entry["filesize"]), normalized_md5(entry["checksum"])


def local_identity(row: dict[str, object]) -> tuple[int, str]:
    return int(row["bytes"]), str(row["md5"])


def auth(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def auth_modern(token: str) -> dict[str, str]:
    return {**auth(token), **MODERN}


def save_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(value, ensure_ascii=True, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    temporary.replace(path)


def load_state() -> dict:
    if not STATE_PATH.is_file():
        return {"schema": "sga-r3-dual-provenance-state-v1", "targets": {}}
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))


def csv_bytes(rows: list[dict[str, object]]) -> bytes:
    output = io.StringIO(newline="")
    writer = csv.DictWriter(
        output,
        fieldnames=("relative_path", "bytes", "sha256"),
        lineterminator="\n",
    )
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue().encode("utf-8")


def deterministic_zipinfo(name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
    info.compress_type = zipfile.ZIP_DEFLATED
    info.create_system = 3
    info.external_attr = 0o100644 << 16
    return info


def file_row(path: Path, relative_path: str | None = None) -> dict[str, object]:
    return {
        "path": path,
        "relative_path": relative_path or path.name,
        "bytes": path.stat().st_size,
        "sha256": sha256(path),
        "md5": md5(path),
    }


def build_provenance_surface(package_root: Path) -> dict[str, object]:
    # Reuse the exact root/manifest guards from the SGA publisher.  The outer
    # 152-member transport was already independently replayed before publish;
    # this projection needs only the source-file identities.
    sga.local_surface(package_root, replay_complete_zip=False)
    control_paths = sorted(
        (path for path in (package_root / "controls").rglob("*") if path.is_file()),
        key=lambda path: path.relative_to(package_root).as_posix().casefold(),
    )
    top_controls = [
        package_root / name
        for name in (
            "README.md",
            "PACKAGE_CONTENT_MANIFEST.csv",
            "PACKAGE_CONTENT_VALIDATION.json",
            "PACKAGE_VALIDATION.json",
            sga.PAYLOAD_MANIFEST,
            sga.PAYLOAD_VALIDATION,
        )
    ]
    selected = sorted(
        [*control_paths, *top_controls],
        key=lambda path: path.relative_to(package_root).as_posix().casefold(),
    )
    if len(control_paths) != 106 or len(selected) != EXPECTED_SOURCE_MEMBERS:
        raise RuntimeError("SGA R3 provenance source-member count changed")

    private_patterns = (
        b"c:\\users\\floris",
        b"c:/users/floris",
        b"/users/floris",
        b".codex/",
        b".codex\\",
    )
    manifest_rows = []
    payloads: list[tuple[str, bytes]] = []
    for path in selected:
        relative = path.relative_to(package_root).as_posix()
        data = path.read_bytes()
        lowered = data.lower()
        hits = [pattern.decode("ascii") for pattern in private_patterns if pattern in lowered]
        if hits:
            raise RuntimeError(f"Private-path hit in SGA R3 control {relative}: {hits}")
        manifest_rows.append(
            {
                "relative_path": relative,
                "bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest().upper(),
            }
        )
        payloads.append((relative, data))
    manifest = csv_bytes(manifest_rows)
    DERIVED_ROOT.mkdir(parents=True, exist_ok=True)
    manifest_path = DERIVED_ROOT / "SGA_R3_PROVENANCE_CONTROLS_20260804_MEMBER_MANIFEST.csv"
    manifest_path.write_bytes(manifest)
    zip_path = DERIVED_ROOT / PROVENANCE_ZIP
    temporary = zip_path.with_suffix(".zip.tmp")
    with zipfile.ZipFile(
        temporary,
        mode="w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
        allowZip64=True,
    ) as archive:
        for relative, data in payloads:
            archive.writestr(
                deterministic_zipinfo(f"{ZIP_PREFIX}/{relative}"), data
            )
        archive.writestr(
            deterministic_zipinfo(f"{ZIP_PREFIX}/{MEMBER_MANIFEST_NAME}"),
            manifest,
        )
    temporary.replace(zip_path)

    with zipfile.ZipFile(zip_path) as archive:
        infos = [info for info in archive.infolist() if not info.is_dir()]
        if len(infos) != EXPECTED_ZIP_MEMBERS or archive.testzip() is not None:
            raise RuntimeError("Derived SGA provenance ZIP count or CRC changed")
        names = [info.filename for info in infos]
        expected_names = {
            f"{ZIP_PREFIX}/{relative}" for relative, _ in payloads
        } | {f"{ZIP_PREFIX}/{MEMBER_MANIFEST_NAME}"}
        if set(names) != expected_names or len(names) != len(set(names)):
            raise RuntimeError("Derived SGA provenance ZIP member boundary changed")
        for info in infos:
            parts = Path(info.filename.replace("\\", "/")).parts
            if info.filename.startswith(("/", "\\")) or ".." in parts:
                raise RuntimeError(f"Unsafe derived SGA ZIP member: {info.filename}")

    surface = {PROVENANCE_ZIP: file_row(zip_path)}
    for remote_name, relative in DIRECT_PATHS.items():
        path = package_root / Path(relative)
        surface[remote_name] = file_row(path, relative)
    if len(surface) != 7:
        raise RuntimeError("SGA R3 dual-DOI direct surface count changed")
    return {
        "surface": surface,
        "zip_path": zip_path,
        "zip_members": EXPECTED_ZIP_MEMBERS,
        "member_manifest": {
            "path": manifest_path,
            "bytes": len(manifest),
            "sha256": hashlib.sha256(manifest).hexdigest().upper(),
            "rows": len(manifest_rows),
        },
        "member_rows": manifest_rows,
    }


def compaction_proof() -> dict[str, dict[str, object]]:
    receipt = json.loads(GAGA_RECEIPT.read_text(encoding="utf-8"))
    surface = receipt["surfaces"][0]
    direct = surface["new_file_identities"]
    pools = []
    for key in ("gaga_provenance_zip_member_replay", "fac_adverse_zip_member_replay"):
        for member, row in surface[key]["member_identities"].items():
            pools.append((key, member, row))
    proof = {}
    for name in sorted(COMPACTED_DIRECT_FILES, key=str.casefold):
        if name not in direct:
            raise RuntimeError(f"Compacted predecessor proof is missing {name}")
        wanted = direct[name]
        matches = [
            (key, member, row)
            for key, member, row in pools
            if int(row["bytes"]) == int(wanted["bytes"])
            and row["sha256"] == wanted["sha256"]
        ]
        if len(matches) != 1:
            raise RuntimeError(f"Compacted byte has no unique retained ZIP member: {name}")
        key, member, row = matches[0]
        proof[name] = {
            "bytes": int(wanted["bytes"]),
            "sha256": wanted["sha256"],
            "retained_zip_proof": key,
            "retained_member_path": member,
        }
    return proof


def fetch_predecessor(session, target: Target, require_latest: bool = True) -> dict:
    record = base.check(
        session.get(
            f"{API}/records/{target.predecessor_id}",
            headers=MODERN,
            timeout=(30, 300),
        ),
        {200},
    ).json()
    entries = modern_entries(record)
    observed = (
        int(record["id"]),
        record.get("pids", {}).get("doi", {}).get("identifier"),
        str(record.get("parent", {}).get("id")),
        record.get("parent", {}).get("pids", {}).get("doi", {}).get("identifier"),
        len(entries),
        sum(int(row["size"]) for row in entries.values()),
        record.get("files", {}).get("default_preview"),
        record.get("status"),
    )
    expected = (
        target.predecessor_id,
        target.predecessor_doi,
        target.concept_id,
        target.concept_doi,
        target.files,
        target.bytes,
        target.preview,
        "published",
    )
    if observed != expected:
        raise RuntimeError(f"{target.key} predecessor boundary changed: {observed!r}")
    if not COMPACTED_DIRECT_FILES.issubset(entries):
        raise RuntimeError(f"{target.key} compacted direct-file boundary changed")
    if require_latest:
        latest = base.check(
            session.get(record["links"]["latest"], headers=MODERN, timeout=(30, 300)),
            {200},
        ).json()
        if int(latest["id"]) != target.predecessor_id:
            raise RuntimeError(f"{target.key} live head changed")
    return record


def verify_compaction_remote(
    session,
    records: dict[str, dict],
    proof: dict[str, dict[str, object]],
) -> None:
    anonymous = base.make_session()
    reference = None
    for key, record in records.items():
        entries = modern_entries(record)
        current = {}
        for name in COMPACTED_DIRECT_FILES:
            row = entries[name]
            current[name] = identity(row)
            expected = proof[name]
            if current[name][0] != int(expected["bytes"]):
                raise RuntimeError(f"{key} compacted file byte count changed: {name}")
        if reference is None:
            reference = current
        elif current != reference:
            raise RuntimeError("Methodology/replication compacted identities diverged")

    # Raw-read these six tiny predecessor bytes once and bind them to the
    # already verified retained ZIP-member identities before any deletion.
    entries = modern_entries(records["methodology"])
    for name in sorted(COMPACTED_DIRECT_FILES, key=str.casefold):
        response = base.check(
            anonymous.get(entries[name]["links"]["content"], timeout=(30, 300)),
            {200},
        )
        data = response.content
        expected = proof[name]
        if (
            len(data) != int(expected["bytes"])
            or hashlib.sha256(data).hexdigest().upper() != expected["sha256"]
        ):
            raise RuntimeError(f"Predecessor compaction raw-readback changed: {name}")


def target_state(state: dict, key: str) -> dict:
    return state.setdefault("targets", {}).setdefault(key, {})


def check_draft_boundary(session, token: str, target: Target, state: dict) -> None:
    tracked = target_state(state, target.key)
    draft_id = tracked.get("draft_id")
    predecessor_probe = session.get(
        f"{API}/records/{target.predecessor_id}/draft",
        headers=auth_modern(token),
        timeout=(30, 180),
    )
    if tracked.get("published_record"):
        if predecessor_probe.status_code not in {404, 410}:
            raise RuntimeError(f"{target.key} published state conflicts with a draft")
        return
    if not draft_id:
        if predecessor_probe.status_code == 200:
            raise RuntimeError(f"Untracked {target.key} successor draft exists")
        base.check(predecessor_probe, {404})
        return
    if predecessor_probe.status_code == 200:
        if int(predecessor_probe.json()["id"]) != int(draft_id):
            raise RuntimeError(f"{target.key} predecessor-scoped draft changed")
    else:
        base.check(predecessor_probe, {404})
    draft = base.check(
        session.get(
            f"{API}/records/{int(draft_id)}/draft",
            headers=auth_modern(token),
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if (
        int(draft["id"]) != int(draft_id)
        or str(draft.get("parent", {}).get("id")) != target.concept_id
        or draft.get("is_published") is not False
    ):
        raise RuntimeError(f"Tracked {target.key} draft identity changed")


def create_or_resume_draft(session, token: str, target: Target, state: dict) -> tuple[int, bool]:
    tracked = target_state(state, target.key)
    if tracked.get("draft_id"):
        return int(tracked["draft_id"]), False
    deposition = base.check(
        session.get(
            f"{API}/deposit/depositions/{target.predecessor_id}",
            headers=auth(token),
            timeout=(30, 300),
        ),
        {200},
    ).json()
    if (
        deposition.get("state") != "done"
        or not deposition.get("submitted")
        or str(deposition.get("conceptrecid")) != target.concept_id
        or not deposition.get("links", {}).get("newversion")
    ):
        raise RuntimeError(f"{target.key} is not a safe same-concept versioning base")
    created = base.check(
        session.post(
            deposition["links"]["newversion"],
            headers=auth(token),
            timeout=(30, 600),
        ),
        {201},
    ).json()
    draft = base.check(
        session.get(
            created["links"]["latest_draft"],
            headers=auth(token),
            timeout=(30, 300),
        ),
        {200},
    ).json()
    draft_id = int(draft["id"])
    tracked.update(
        {
            "status": "OPEN_TRACKED_DRAFT",
            "draft_id": draft_id,
            "predecessor_id": target.predecessor_id,
            "concept_id": target.concept_id,
            "concept_doi": target.concept_doi,
            "published": False,
        }
    )
    save_json(STATE_PATH, state)
    return draft_id, True


def desired_order(record: dict, desired: set[str], uploads: set[str]) -> list[str]:
    predecessor_order = record.get("files", {}).get("order") or sorted(
        modern_entries(record), key=str.casefold
    )
    retained_order = [name for name in predecessor_order if name in desired and name not in uploads]
    new_order = [PROVENANCE_ZIP, *DIRECT_PATHS]
    insertion = max(
        (index + 1 for index, name in enumerate(retained_order) if name.startswith("06_GAGA__")),
        default=min(6, len(retained_order)),
    )
    order = retained_order[:insertion] + new_order + retained_order[insertion:]
    if len(order) != len(desired) or set(order) != desired:
        raise RuntimeError("Dual-DOI file order is not an exact permutation")
    return order


def staged_description(current: str) -> str:
    if LANDING_BLOCK in current:
        return current
    return LANDING_BLOCK + "\n" + current


def verify_staged(
    draft: dict,
    target: Target,
    predecessor: dict,
    surface: dict[str, dict[str, object]],
    order: list[str],
) -> None:
    predecessor_entries = modern_entries(predecessor)
    desired = (set(predecessor_entries) - COMPACTED_DIRECT_FILES) | set(surface)
    entries = modern_entries(draft)
    if set(entries) != desired:
        raise RuntimeError(f"{target.key} staged file boundary changed")
    for name, row in surface.items():
        if identity(entries[name]) != local_identity(row):
            raise RuntimeError(f"{target.key} staged upload identity changed: {name}")
    for name in desired - set(surface):
        if identity(entries[name]) != identity(predecessor_entries[name]):
            raise RuntimeError(f"{target.key} retained predecessor changed: {name}")
    metadata = draft.get("metadata", {})
    if (
        metadata.get("publication_date") != PUBLICATION_DATE
        or metadata.get("version") != target.version
        or not metadata.get("description", "").startswith(LANDING_BLOCK)
        or SGA_RECORD_DOI not in metadata.get("description", "")
        or draft.get("files", {}).get("default_preview") != target.preview
    ):
        raise RuntimeError(f"{target.key} staged metadata or preview changed")
    observed_order = draft.get("files", {}).get("order") or []
    if observed_order not in (order, []):
        raise RuntimeError(f"{target.key} staged file order changed")


def preflight(session, token: str, package_root: Path) -> dict[str, object]:
    built = build_provenance_surface(package_root)
    proof = compaction_proof()
    state = load_state()
    records = {}
    for key, target in TARGETS.items():
        published = bool(target_state(state, key).get("published_record"))
        records[key] = fetch_predecessor(session, target, require_latest=not published)
        check_draft_boundary(session, token, target, state)
    verify_compaction_remote(session, records, proof)
    surface = built["surface"]
    return {
        "status": "PASS_READY_FOR_TRACKED_DUAL_DOI_SUCCESSORS",
        "sga_record": SGA_RECORD_ID,
        "sga_doi": SGA_RECORD_DOI,
        "sga_concept_doi": SGA_CONCEPT_DOI,
        "new_direct_files_per_target": len(surface),
        "new_direct_bytes_per_target": sum(int(row["bytes"]) for row in surface.values()),
        "provenance_zip": {
            "filename": PROVENANCE_ZIP,
            "bytes": int(surface[PROVENANCE_ZIP]["bytes"]),
            "sha256": surface[PROVENANCE_ZIP]["sha256"],
            "members": built["zip_members"],
            "source_member_manifest_rows": built["member_manifest"]["rows"],
            "source_member_manifest_sha256": built["member_manifest"]["sha256"],
        },
        "compacted_direct_files": proof,
        "targets": {
            key: {
                "predecessor": target.predecessor_id,
                "concept_doi": target.concept_doi,
                "predecessor_files": len(modern_entries(records[key])),
                "expected_successor_files": (
                    len(modern_entries(records[key]))
                    - len(COMPACTED_DIRECT_FILES)
                    + len(surface)
                ),
                "tracked_draft_id": target_state(state, key).get("draft_id"),
                "published_record": target_state(state, key).get("published_record"),
            }
            for key, target in TARGETS.items()
        },
        "duplicate_concept_created": False,
    }


def upload_file(session, token: str, bucket: str, name: str, path: Path) -> None:
    print(f"UPLOAD {name} ({path.stat().st_size} bytes)", flush=True)
    with path.open("rb") as handle:
        base.check(
            session.put(
                f"{bucket.rstrip('/')}/{quote(name, safe='')}",
                headers={**auth(token), "Content-Type": "application/octet-stream"},
                data=handle,
                timeout=(30, 3600),
            ),
            {200, 201},
        )


def stage_one(
    session,
    token: str,
    target: Target,
    predecessor: dict,
    surface: dict[str, dict[str, object]],
    state: dict,
) -> dict[str, object]:
    draft_id, created = create_or_resume_draft(session, token, target, state)
    deposition = base.check(
        session.get(
            f"{API}/deposit/depositions/{draft_id}",
            headers=auth(token),
            timeout=(30, 300),
        ),
        {200},
    ).json()
    remote = legacy_entries(deposition)
    expected_inherited = set(modern_entries(predecessor))
    if not set(remote).issubset(expected_inherited | set(surface)):
        raise RuntimeError(f"{target.key} draft contains an unexpected filename")
    deleted = []
    for name in sorted(COMPACTED_DIRECT_FILES & set(remote), key=str.casefold):
        print(f"DELETE NESTED MACHINE DUPLICATE {target.key} {name}", flush=True)
        base.check(
            session.delete(
                remote[name]["links"]["self"],
                headers=auth(token),
                timeout=(30, 600),
            ),
            {204},
        )
        deleted.append(name)

    deposition = base.check(
        session.get(
            f"{API}/deposit/depositions/{draft_id}",
            headers=auth(token),
            timeout=(30, 300),
        ),
        {200},
    ).json()
    remote = legacy_entries(deposition)
    uploaded = []
    for name in [PROVENANCE_ZIP, *DIRECT_PATHS]:
        row = surface[name]
        if name in remote:
            if legacy_identity(remote[name]) != local_identity(row):
                raise RuntimeError(f"{target.key} tracked upload changed: {name}")
            continue
        upload_file(session, token, deposition["links"]["bucket"], name, Path(row["path"]))
        uploaded.append(name)

    draft = base.check(
        session.get(
            f"{API}/records/{draft_id}/draft",
            headers=auth_modern(token),
            timeout=(30, 600),
        ),
        {200},
    ).json()
    desired = (set(modern_entries(predecessor)) - COMPACTED_DIRECT_FILES) | set(surface)
    order = desired_order(predecessor, desired, set(surface))
    metadata = copy.deepcopy(predecessor["metadata"])
    metadata["publication_date"] = PUBLICATION_DATE
    metadata["version"] = target.version
    metadata["description"] = staged_description(metadata.get("description", ""))
    payload = {
        "access": predecessor["access"],
        "files": {"enabled": True, "default_preview": target.preview, "order": order},
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
    verify_staged(patched, target, predecessor, surface, order)
    tracked = target_state(state, target.key)
    tracked.update(
        {
            "status": "STAGED_EXACT_READY_FOR_EXPLICIT_PUBLISH",
            "staged": True,
            "staged_files": len(modern_entries(patched)),
            "staged_bytes": sum(
                int(row["size"]) for row in modern_entries(patched).values()
            ),
        }
    )
    save_json(STATE_PATH, state)
    return {
        "target": target.key,
        "draft_id": draft_id,
        "draft_url": patched.get("links", {}).get("self_html"),
        "created_new_same_concept_draft": created,
        "concept_doi": target.concept_doi,
        "predecessor": target.predecessor_id,
        "deleted_nested_machine_duplicates": deleted,
        "uploaded_now": uploaded,
        "files": len(modern_entries(patched)),
        "bytes": sum(int(row["size"]) for row in modern_entries(patched).values()),
        "default_preview": patched["files"]["default_preview"],
    }


def stage(session, token: str, package_root: Path) -> dict[str, object]:
    built = build_provenance_surface(package_root)
    surface = built["surface"]
    proof = compaction_proof()
    state = load_state()
    records = {
        key: fetch_predecessor(session, target)
        for key, target in TARGETS.items()
    }
    for target in TARGETS.values():
        check_draft_boundary(session, token, target, state)
    verify_compaction_remote(session, records, proof)
    results = []
    for key, target in TARGETS.items():
        results.append(
            stage_one(session, token, target, records[key], surface, state)
        )
    return {
        "status": "STAGED_BOTH_EXACT_READY_FOR_EXPLICIT_PUBLISH",
        "sga_record": SGA_RECORD_ID,
        "provenance_zip": {
            "filename": PROVENANCE_ZIP,
            "bytes": surface[PROVENANCE_ZIP]["bytes"],
            "sha256": surface[PROVENANCE_ZIP]["sha256"],
            "members": built["zip_members"],
        },
        "targets": results,
        "duplicate_concept_created": False,
    }


def stream_identity(session, url: str, destination: Path | None = None) -> tuple[int, str]:
    digest = hashlib.sha256()
    total = 0
    response = base.check(session.get(url, stream=True, timeout=(30, 3600)), {200})
    try:
        handle = None if destination is None else destination.open("wb")
        try:
            for block in response.iter_content(4 * 1024 * 1024):
                if not block:
                    continue
                if handle is not None:
                    handle.write(block)
                digest.update(block)
                total += len(block)
        finally:
            if handle is not None:
                handle.close()
    finally:
        response.close()
    return total, digest.hexdigest().upper()


def replay_public_zip(path: Path, built: dict[str, object]) -> dict[str, object]:
    expected = {
        f"{ZIP_PREFIX}/{row['relative_path']}": (
            int(row["bytes"]),
            str(row["sha256"]),
        )
        for row in built["member_rows"]
    }
    manifest = built["member_manifest"]
    expected[f"{ZIP_PREFIX}/{MEMBER_MANIFEST_NAME}"] = (
        int(manifest["bytes"]),
        str(manifest["sha256"]),
    )
    errors = []
    members = []
    with zipfile.ZipFile(path) as archive:
        infos = [info for info in archive.infolist() if not info.is_dir()]
        if len(infos) != EXPECTED_ZIP_MEMBERS or set(info.filename for info in infos) != set(expected):
            errors.append("member_boundary")
        for info in infos:
            digest = hashlib.sha256()
            with archive.open(info) as handle:
                for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
                    digest.update(block)
            observed = (info.file_size, digest.hexdigest().upper())
            match = observed == expected.get(info.filename)
            if not match:
                errors.append(info.filename)
            members.append(
                {
                    "member_path": info.filename,
                    "bytes": observed[0],
                    "sha256": observed[1],
                    "match": match,
                }
            )
    return {
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "members": len(members),
        "matches": sum(1 for row in members if row["match"]),
        "mismatches": sum(1 for row in members if not row["match"]),
        "member_identities": members,
    }


def publish_one(
    session,
    token: str,
    target: Target,
    predecessor: dict,
    built: dict[str, object],
    state: dict,
    confirm: str,
) -> dict[str, object]:
    surface = built["surface"]
    tracked = target_state(state, target.key)
    if tracked.get("published_record"):
        record_id = int(tracked["published_record"])
    else:
        if not tracked.get("staged"):
            raise RuntimeError(f"{target.key} has no exact staged draft")
        draft_id = int(tracked["draft_id"])
        if confirm != str(draft_id):
            raise RuntimeError(
                f"Publishing {target.key} requires its exact confirmed draft id {draft_id}"
            )
        draft = base.check(
            session.get(
                f"{API}/records/{draft_id}/draft",
                headers=auth_modern(token),
                timeout=(30, 600),
            ),
            {200},
        ).json()
        desired = (set(modern_entries(predecessor)) - COMPACTED_DIRECT_FILES) | set(surface)
        order = desired_order(predecessor, desired, set(surface))
        verify_staged(draft, target, predecessor, surface, order)
        published = base.check(
            session.post(
                draft["links"]["publish"],
                headers=auth_modern(token),
                timeout=(30, 1200),
            ),
            {200, 202},
        )
        try:
            record_id = int(published.json().get("id", draft_id))
        except Exception:
            record_id = draft_id
        if record_id != draft_id:
            raise RuntimeError(f"{target.key} publication returned an unexpected record id")
        tracked.update(
            {
                "status": "PUBLISHED_READBACK_PENDING",
                "published": True,
                "published_record": record_id,
            }
        )
        save_json(STATE_PATH, state)

    anonymous = base.make_session()
    record = None
    for _ in range(60):
        probe = anonymous.get(
            f"{API}/records/{record_id}", headers=MODERN, timeout=(30, 300)
        )
        if probe.status_code == 200 and probe.json().get("status") == "published":
            record = probe.json()
            break
        time.sleep(2)
    if record is None:
        raise RuntimeError(f"{target.key} successor did not become public")
    desired = (set(modern_entries(predecessor)) - COMPACTED_DIRECT_FILES) | set(surface)
    order = desired_order(predecessor, desired, set(surface))
    verify_staged(record, target, predecessor, surface, order)
    if (
        str(record.get("parent", {}).get("id")) != target.concept_id
        or record.get("parent", {}).get("pids", {}).get("doi", {}).get("identifier")
        != target.concept_doi
        or record.get("versions", {}).get("is_latest") is not True
    ):
        raise RuntimeError(f"{target.key} published concept/latest identity changed")

    entries = modern_entries(record)
    readback = []
    zip_path = TEMP_ROOT / f"record_{record_id}_{PROVENANCE_ZIP}"
    for index, name in enumerate([PROVENANCE_ZIP, *DIRECT_PATHS], start=1):
        print(f"READBACK {target.key} {index}/7 {name}", flush=True)
        destination = zip_path if name == PROVENANCE_ZIP else None
        observed = stream_identity(anonymous, entries[name]["links"]["content"], destination)
        expected = (int(surface[name]["bytes"]), str(surface[name]["sha256"]))
        match = observed == expected
        if not match:
            raise RuntimeError(f"{target.key} raw readback changed: {name}")
        readback.append(
            {
                "filename": name,
                "source_relative_path": surface[name]["relative_path"],
                "bytes": observed[0],
                "sha256": observed[1],
                "match": match,
                "content_url": entries[name]["links"]["content"],
            }
        )
    zip_replay = replay_public_zip(zip_path, built)
    if zip_replay["status"] != "PASS" or zip_replay["matches"] != EXPECTED_ZIP_MEMBERS:
        raise RuntimeError(f"{target.key} provenance ZIP member replay failed")
    zip_path.unlink()

    retained_errors = []
    predecessor_entries = modern_entries(predecessor)
    for name in desired - set(surface):
        if identity(entries[name]) != identity(predecessor_entries[name]):
            retained_errors.append(name)
    if retained_errors:
        raise RuntimeError(f"{target.key} retained predecessor identities changed")
    draft_probe = session.get(
        f"{API}/records/{record_id}/draft",
        headers=auth_modern(token),
        timeout=(30, 180),
    )
    if draft_probe.status_code not in {404, 410}:
        raise RuntimeError(f"{target.key} active draft remains after publication")

    result = {
        "status": "PASS_PUBLISHED_AND_ANONYMOUS_RAW_READBACK",
        "target": target.key,
        "record_id": record_id,
        "record_url": record["links"]["self_html"],
        "doi": record["pids"]["doi"]["identifier"],
        "concept_id": target.concept_id,
        "concept_doi": target.concept_doi,
        "predecessor_record": target.predecessor_id,
        "predecessor_doi": target.predecessor_doi,
        "files": len(entries),
        "bytes": sum(int(row["size"]) for row in entries.values()),
        "default_preview": record["files"]["default_preview"],
        "new_direct_files": len(readback),
        "new_direct_raw_readback_matches": len(readback),
        "new_direct_raw_readback_mismatches": 0,
        "retained_predecessor_files": len(desired - set(surface)),
        "retained_predecessor_identity_mismatches": 0,
        "compacted_direct_files": sorted(COMPACTED_DIRECT_FILES),
        "compacted_bytes_preserved_in_retained_zips_and_predecessors": True,
        "provenance_zip_member_replay": zip_replay,
        "raw_public_readback": readback,
        "active_draft": False,
        "duplicate_concept_created": False,
    }
    tracked.update(
        {
            "status": "PASS_PUBLISHED_AND_ANONYMOUS_READBACK",
            "doi": result["doi"],
            "receipt_ready": True,
        }
    )
    save_json(STATE_PATH, state)
    receipt = (
        REPO_ROOT
        / "manifests/published-zenodo"
        / f"20260804_sga_r3_{target.key}_record_{record_id}_public_readback.json"
    )
    save_json(receipt, result)
    return result


def publish(
    session,
    token: str,
    package_root: Path,
    methodology_confirm: str,
    replication_confirm: str,
) -> dict[str, object]:
    built = build_provenance_surface(package_root)
    proof = compaction_proof()
    state = load_state()
    records = {
        key: fetch_predecessor(
            session,
            target,
            require_latest=not bool(target_state(state, key).get("published_record")),
        )
        for key, target in TARGETS.items()
    }
    verify_compaction_remote(session, records, proof)
    confirms = {
        "methodology": methodology_confirm,
        "replication": replication_confirm,
    }
    results = []
    for key, target in TARGETS.items():
        results.append(
            publish_one(
                session,
                token,
                target,
                records[key],
                built,
                state,
                confirms[key],
            )
        )
    identities = [
        {
            row["filename"]: (row["bytes"], row["sha256"])
            for row in result["raw_public_readback"]
        }
        for result in results
    ]
    if identities[0] != identities[1]:
        raise RuntimeError("Methodology and replication SGA R3 bytes diverged")
    combined = {
        "status": "PASS_SGA_R3_DUAL_DOI_PUBLICATION_AND_READBACK",
        "sga_record": SGA_RECORD_ID,
        "sga_doi": SGA_RECORD_DOI,
        "sga_concept_doi": SGA_CONCEPT_DOI,
        "surfaces": results,
        "identical_new_direct_files": True,
        "identical_new_direct_file_names": sorted(identities[0], key=str.casefold),
        "compaction_proof": proof,
        "provenance_zip": {
            "filename": PROVENANCE_ZIP,
            "bytes": built["surface"][PROVENANCE_ZIP]["bytes"],
            "sha256": built["surface"][PROVENANCE_ZIP]["sha256"],
            "members": EXPECTED_ZIP_MEMBERS,
            "member_manifest_rows": built["member_manifest"]["rows"],
            "member_manifest_sha256": built["member_manifest"]["sha256"],
        },
        "duplicate_concept_created": False,
    }
    save_json(
        REPO_ROOT
        / "manifests/published-zenodo/20260804_sga_r3_dual_doi_publication_receipt.json",
        combined,
    )
    return combined


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=("preflight", "stage", "publish"))
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--confirm-methodology")
    parser.add_argument("--confirm-replication")
    args = parser.parse_args()
    package_root = args.root.resolve()
    session = base.make_session()
    token = base.find_token()
    if args.action == "preflight":
        result = preflight(session, token, package_root)
    elif args.action == "stage":
        result = stage(session, token, package_root)
    else:
        if not args.confirm_methodology or not args.confirm_replication:
            raise RuntimeError(
                "Publishing requires both --confirm-methodology and --confirm-replication draft ids"
            )
        result = publish(
            session,
            token,
            package_root,
            args.confirm_methodology,
            args.confirm_replication,
        )
    summary = copy.deepcopy(result)
    for surface in summary.get("surfaces", []):
        surface.pop("raw_public_readback", None)
        surface.pop("provenance_zip_member_replay", None)
    if "compaction_proof" in summary:
        summary["compacted_direct_file_count"] = len(summary.pop("compaction_proof"))
    print(json.dumps(summary, ensure_ascii=True, indent=2), flush=True)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr, flush=True)
        raise
