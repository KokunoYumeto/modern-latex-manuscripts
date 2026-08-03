#!/usr/bin/env python3
"""Build the bounded FAC blind-comparator dual-DOI successor payload.

This is a read-only Zenodo operation.  It captures the locked shared decision
log into exact private custody, creates a separate minimally redacted public
projection, downloads a mechanically defined set of small legacy methodology
companion files, and preserves those exact public predecessor bytes in an
indexed deterministic ZIP.  It also builds a dual-DOI archive-mapping ZIP and
a direct release index.  It creates no Zenodo draft and publishes nothing.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import shutil
import time
import zipfile
from collections import Counter
from pathlib import Path, PurePosixPath
from typing import Any, Iterable

import requests

from build_fac_blind_comparator_transport_20260803 import (
    project_text,
    residual_findings,
    sha256_bytes,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
API = "https://zenodo.org/api"
OUTPUT = REPO_ROOT / (
    "manifests/zenodo-active-custody/"
    "fac-blind-comparator-dual-doi-20260803-r1"
)
PRIVATE_ROOT = Path(
    "C:/Users/Floris/Documents/Codex/archive-private-custody/"
    "20260803T040000CEST_fac-blind-comparator-dual-doi-release-r1"
)
LANE_CONTROL = Path(
    "C:/Users/Floris/Documents/interlanguage/03_projects/language_management/"
    "english_germanic/00_lane_control"
)
SHARED_LOG = LANE_CONTROL / "ENGLISH_GERMANIC_DECISION_LOG_v1.jsonl"
TRANSPORT_DECISION = LANE_CONTROL / (
    "ARCHIVE_DECISION_RECORD_FAC_BLIND_COMPARATOR_TRANSPORT_"
    "ACCEPTED_20260803_0349.json"
)
TRANSPORT_ROOT = REPO_ROOT / (
    "manifests/methodology-evidence/"
    "20260803_fac-blind-comparator-r1"
)
FAC_PAYLOAD = TRANSPORT_ROOT / "payload"
GITHUB_RECEIPT_ROOT = REPO_ROOT / "manifests/published-github"

HANDOFF_ID = "FAC-METHODOLOGY-BLIND-COMPARATOR-DUAL-DOI-HANDOFF-20260803-R1"
RELEASE_ID = "fac-blind-comparator-dual-doi-20260803-r1"
METHODOLOGY_CONCEPT = "10.5281/zenodo.21124403"
REPLICATION_CONCEPT = "10.5281/zenodo.20461174"
METHODOLOGY_RECORD = 21_764_482
REPLICATION_RECORD = 21_764_484
EXPECTED_SHARED_BYTES = 3_139_044
EXPECTED_SHARED_SHA256 = (
    "E7E76CA4F2F1E425BCD26AD7B504B160C92B5DE14C61370C7D5241E03C180D90"
)
EXPECTED_SHARED_RECORDS = 471
EXPECTED_SHARED_LATEST = (
    "EG-ARCHIVE-FAC-BLIND-COMPARATOR-TRANSPORT-ACCEPTED-20260803-0001"
)
EXPECTED_FAC_FILES = 19
EXPECTED_FAC_BYTES = 734_806
EXPECTED_FAC_TREE_SHA256 = (
    "5CEF1E35818D8A1D75EF397809A7F7831E6ABE06E4513D04AD2EC189E3ED65B8"
)
CONTROL_NAME = "PROJECT_LOGBOOK_METHODOLOGY_REPLICATION_DOI_REQUIREMENT_20260802.md"
CONTROL_ORIGINAL_BYTES = 2_296
CONTROL_ORIGINAL_SHA256 = (
    "BFA1E3A3EDA94E8C3425BAE50C842610A47D508FB260BF761BA3206883012679"
)
CONTROL_PUBLIC_BYTES = 2_242
CONTROL_PUBLIC_SHA256 = (
    "864DC6B0183161DFA289D6A25DDE268D09E5187C3C4102C854F05422B86DF2AA"
)
FIXED_ZIP_TIME = (2026, 8, 3, 0, 0, 0)

RETENTION_ARCHIVE_NAME = (
    "24_Retained_Interlanguage_Companion_Manifests_Statuses_20260803.zip"
)
RETENTION_MANIFEST_NAME = (
    "24a_Retained_Interlanguage_Companion_Manifests_"
    "Statuses_20260803_MANIFEST.csv"
)
RETENTION_INNER_MANIFEST = "RETENTION_MANIFEST.csv"
ARCHIVE_MAPPING_NAME = "FAC_BLIND_COMPARATOR_ARCHIVE_MAPPING_20260803.zip"

RETENTION_NAMES = (
    "09_Interlanguage_SourceBody_SideBranch_Inventory_20260707.csv",
    "09_Interlanguage_SourceBody_SideBranch_Inventory_20260707.md",
    "09_Interlanguage_SourceBody_SideBranch_Public_Manifest_20260707.csv",
    "09_Interlanguage_SourceBody_SideBranch_Public_SHA256_20260707.csv",
    "10_Interlanguage_Post2DE_RouteContext_Returns_sha256_20260707.csv",
    "11_Interlanguage_v04_public_manifest_20260710.csv",
    "11_Interlanguage_v04_public_sha256_20260710.csv",
    "13_Interlanguage_v06_public_manifest_20260718.csv",
    "13_Interlanguage_v06_public_sha256_20260718.txt",
    "14_Interlanguage_Romance_v10_public_manifest_20260718.csv",
    "14_Interlanguage_Romance_v10_public_sha256_20260718.txt",
    "15_Interlanguage_v11_public_manifest_20260718.csv",
    "15_Interlanguage_v11_public_sha256_20260718.txt",
    "16_Interlanguage_v12_public_manifest_20260718.csv",
    "16_Interlanguage_v12_public_sha256_20260718.txt",
    "17_Interlanguage_v13_public_manifest_20260718.csv",
    "17_Interlanguage_v13_public_sha256_20260718.txt",
    "18_CJK_Visual_Evidence_v14_public_manifest_20260722.csv",
    "18_CJK_Visual_Evidence_v14_public_sha256_20260722.txt",
    "99_Interlanguage_Public_Status_v13_20260718.md",
    "99_Interlanguage_Public_Status_v14_20260722.md",
    "99_Interlanguage_SourceBody_SideBranch_Public_Status_20260707.md",
)

DIRECT_PROVENANCE = (
    "FAC_PROJECT_LOGBOOK_SNAPSHOT.md",
    "FAC_EDITORIAL_DECISION_LOGBOOK_SNAPSHOT.md",
    "FAC_EDITORIAL_SELF_CORRECTION_LEDGER_PRIVACY_CLEAN.csv",
)

REQUIRED_DECISION_FIELDS = {
    "decision_id",
    "recorded_at",
    "decision_time",
    "work_unit",
    "authority_and_cursor",
    "choice",
    "alternatives",
    "evidence",
    "motivation",
    "uncertainty_and_adverse_evidence",
    "consequences",
    "changed_artifacts",
    "supersession",
    "review_state",
    "next_cursor_or_revisit_condition",
}


def json_bytes(value: Any) -> bytes:
    return (
        json.dumps(value, ensure_ascii=True, sort_keys=True, indent=2) + "\n"
    ).encode("utf-8")


def csv_bytes(header: Iterable[str], rows: Iterable[Iterable[Any]]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.writer(stream, lineterminator="\n")
    writer.writerow(list(header))
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def md5_bytes(data: bytes) -> str:
    return hashlib.md5(data, usedforsecurity=False).hexdigest().lower()


def md5_path(path: Path) -> str:
    digest = hashlib.md5(usedforsecurity=False)
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().lower()


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def safe_member(name: str) -> bool:
    pure = PurePosixPath(name)
    return (
        bool(name)
        and name == name.replace("\\", "/")
        and not pure.is_absolute()
        and ".." not in pure.parts
        and re.match(r"^[A-Za-z]:", name) is None
    )


def write_zip(path: Path, members: list[tuple[str, bytes]]) -> None:
    names = [name for name, _ in members]
    if len(names) != len(set(names)) or not all(safe_member(name) for name in names):
        raise RuntimeError(f"Unsafe or duplicate ZIP members: {path.name}")
    with zipfile.ZipFile(
        path,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
        allowZip64=True,
    ) as archive:
        for name, data in sorted(members, key=lambda item: item[0]):
            info = zipfile.ZipInfo(name, FIXED_ZIP_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            info.create_system = 3
            archive.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


def zip_inventory(path: Path, include_members: bool = False) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    with zipfile.ZipFile(path) as archive:
        bad = archive.testzip()
        if bad is not None:
            raise RuntimeError(f"ZIP CRC replay failed: {path.name}/{bad}")
        infos = [entry for entry in archive.infolist() if not entry.is_dir()]
        names = [entry.filename for entry in infos]
        if len(names) != len(set(names)) or not all(safe_member(name) for name in names):
            raise RuntimeError(f"Unsafe ZIP inventory: {path.name}")
        for entry in infos:
            digest = hashlib.sha256()
            total = 0
            with archive.open(entry) as handle:
                for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
                    total += len(block)
                    digest.update(block)
            rows.append(
                {
                    "name": entry.filename,
                    "bytes": total,
                    "sha256": digest.hexdigest().upper(),
                }
            )
    rows.sort(key=lambda row: row["name"])
    canonical = json.dumps(
        rows, ensure_ascii=True, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    result: dict[str, Any] = {
        "member_count": len(rows),
        "uncompressed_bytes": sum(int(row["bytes"]) for row in rows),
        "inventory_sha256": sha256_bytes(canonical),
    }
    if include_members:
        result["members"] = rows
    return result


def identity_rows(root: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in sorted((item for item in root.iterdir() if item.is_file()), key=lambda item: item.name):
        data = path.read_bytes()
        rows.append(
            {"relative_path": path.name, "bytes": len(data), "sha256": sha256_bytes(data)}
        )
    return rows


def tree_sha256(rows: list[dict[str, Any]]) -> str:
    canonical = "".join(
        f"{row['relative_path']}|{row['bytes']}|{row['sha256']}\n" for row in rows
    ).encode("utf-8")
    return sha256_bytes(canonical)


def jsonl_identity(data: bytes) -> dict[str, Any]:
    lines = data.decode("utf-8").splitlines()
    records: list[dict[str, Any]] = []
    for ordinal, line in enumerate(lines, 1):
        if not line.strip():
            raise RuntimeError(f"Blank shared decision-log row: {ordinal}")
        row = json.loads(line)
        if not isinstance(row, dict) or not REQUIRED_DECISION_FIELDS.issubset(row):
            raise RuntimeError(f"Invalid shared decision-log record: {ordinal}")
        records.append(row)
    ids = [str(row["decision_id"]) for row in records]
    if len(ids) != len(set(ids)):
        raise RuntimeError("Shared decision-log IDs are not unique")
    return {
        "records": len(records),
        "latest_id": ids[-1] if ids else None,
        "unique_ids": True,
    }


def request_json(session: requests.Session, url: str) -> dict[str, Any]:
    response = session.get(url, timeout=(30, 300))
    if response.status_code != 200:
        raise RuntimeError(f"Zenodo read failed HTTP {response.status_code}: {url}")
    return response.json()


def concept_doi(record: dict[str, Any]) -> str | None:
    return (
        record.get("parent", {}).get("pids", {}).get("doi", {}).get("identifier")
        or record.get("conceptdoi")
    )


def version_doi(record: dict[str, Any]) -> str | None:
    return record.get("pids", {}).get("doi", {}).get("identifier") or record.get("doi")


def verify_head(
    session: requests.Session,
    record_id: int,
    expected_concept: str,
    expected_files: int,
) -> dict[str, Any]:
    record = request_json(session, f"{API}/records/{record_id}?expand=true")
    latest = request_json(
        session, f"{API}/records/{record_id}/versions/latest?expand=true"
    )
    entries = record.get("files", {}).get("entries") or {}
    observed = (
        int(record["id"]),
        version_doi(record),
        concept_doi(record),
        bool(record.get("is_published")),
        int(latest["id"]),
        len(entries),
    )
    expected = (
        record_id,
        f"10.5281/zenodo.{record_id}",
        expected_concept,
        True,
        record_id,
        expected_files,
    )
    if observed != expected:
        raise RuntimeError(f"Zenodo predecessor boundary moved: {observed}")
    return record


def normalize_md5(value: Any) -> str:
    digest = str(value).lower().removeprefix("md5:")
    if re.fullmatch(r"[0-9a-f]{32}", digest) is None:
        raise RuntimeError(f"Invalid MD5: {value!r}")
    return digest


def download_retained_predecessor(
    session: requests.Session,
    record: dict[str, Any],
) -> tuple[bytes, list[dict[str, Any]], dict[str, Any]]:
    entries = record["files"]["entries"]
    if set(RETENTION_NAMES) - set(entries):
        raise RuntimeError(
            f"Retention names absent: {sorted(set(RETENTION_NAMES) - set(entries))}"
        )
    rows: list[dict[str, Any]] = []
    members: list[tuple[str, bytes]] = []
    for name in sorted(RETENTION_NAMES):
        entry = entries[name]
        response = session.get(
            entry["links"]["content"],
            headers={"Accept": "*/*"},
            timeout=(30, 300),
        )
        if response.status_code != 200:
            raise RuntimeError(f"Retention download failed HTTP {response.status_code}: {name}")
        data = response.content
        file_id = str(entry.get("id") or "").lower()
        observed = (len(data), md5_bytes(data))
        expected = (int(entry["size"]), normalize_md5(entry["checksum"]))
        if observed != expected or re.fullmatch(r"[0-9a-f-]{36}", file_id) is None:
            raise RuntimeError(f"Retained predecessor identity changed: {name}")
        member_path = f"retained_predecessor/{name}"
        rows.append(
            {
                "predecessor_name": name,
                "source_record_id": METHODOLOGY_RECORD,
                "source_version_doi": f"10.5281/zenodo.{METHODOLOGY_RECORD}",
                "bytes": len(data),
                "md5": observed[1],
                "sha256": sha256_bytes(data),
                "zenodo_file_id": file_id,
                "zip_member_path": member_path,
                "role": "legacy_companion_manifest_hash_or_status",
                "preservation_status": (
                    "EXACT_PREDECESSOR_BYTES_RETAINED_IN_INDEXED_ARCHIVE"
                ),
                "direct_predecessor_version_preserved": True,
            }
        )
        members.append((member_path, data))
    header = (
        "predecessor_name",
        "source_record_id",
        "source_version_doi",
        "bytes",
        "md5",
        "sha256",
        "zenodo_file_id",
        "zip_member_path",
        "role",
        "preservation_status",
        "direct_predecessor_version_preserved",
    )
    manifest = csv_bytes(header, ([row[field] for field in header] for row in rows))
    members.append((RETENTION_INNER_MANIFEST, manifest))
    archive_path = OUTPUT / RETENTION_ARCHIVE_NAME
    write_zip(archive_path, members)
    (OUTPUT / RETENTION_MANIFEST_NAME).write_bytes(manifest)
    return manifest, rows, zip_inventory(archive_path, include_members=True)


def action_rows_bytes(actions: list[dict[str, object]]) -> bytes:
    header = (
        "relative_path",
        "rule",
        "ordinal",
        "line",
        "matched_utf8_bytes",
        "matched_sha256",
        "replacement",
    )
    ordered = sorted(
        actions,
        key=lambda item: (
            str(item["relative_path"]),
            str(item["rule"]),
            int(item["ordinal"]),
        ),
    )
    return csv_bytes(header, ([item[field] for field in header] for item in ordered))


def project_member(
    source_locator: str,
    member_path: str,
    source_data: bytes,
) -> tuple[bytes, dict[str, Any], list[dict[str, object]]]:
    public_data, actions = project_text(source_data, member_path)
    residual = residual_findings(public_data.decode("utf-8"))
    if residual:
        raise RuntimeError(f"Archive-mapping privacy residual: {member_path}: {residual}")
    row = {
        "member_path": member_path,
        "source_locator": source_locator,
        "source_bytes": len(source_data),
        "source_sha256": sha256_bytes(source_data),
        "public_bytes": len(public_data),
        "public_sha256": sha256_bytes(public_data),
        "privacy_action_count": len(actions),
        "privacy_rules": ";".join(sorted({str(item["rule"]) for item in actions})),
        "privacy_result": "PASS_PRIVACY_CLEAN_PUBLIC_PROJECTION",
        "supersession_state": "APPEND_ONLY_SOURCE_TO_PUBLIC_MAPPING_PRESERVED",
    }
    return public_data, row, actions


def build_archive_mapping(
    shared_source: bytes,
    shared_public: bytes,
    shared_actions: list[dict[str, object]],
    shared_source_identity: dict[str, Any],
    shared_public_identity: dict[str, Any],
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    sources = (
        (
            "methodology-evidence/ARCHIVE_TRANSPORT_ACCEPTANCE.json",
            "transport/ARCHIVE_TRANSPORT_ACCEPTANCE.json",
            TRANSPORT_ROOT / "ARCHIVE_TRANSPORT_ACCEPTANCE.json",
        ),
        (
            "methodology-evidence/PRIVATE_ORIGINAL_IDENTITY_MANIFEST.csv",
            "transport/PRIVATE_ORIGINAL_IDENTITY_MANIFEST.csv",
            TRANSPORT_ROOT / "PRIVATE_ORIGINAL_IDENTITY_MANIFEST.csv",
        ),
        (
            "methodology-evidence/PUBLIC_PROJECTION_IDENTITY_MANIFEST.csv",
            "transport/PUBLIC_PROJECTION_IDENTITY_MANIFEST.csv",
            TRANSPORT_ROOT / "PUBLIC_PROJECTION_IDENTITY_MANIFEST.csv",
        ),
        (
            "methodology-evidence/PRIVACY_TRANSFORMATIONS.csv",
            "transport/PRIVACY_TRANSFORMATIONS.csv",
            TRANSPORT_ROOT / "PRIVACY_TRANSFORMATIONS.csv",
        ),
        (
            "methodology-evidence/PUBLIC_PROJECTION_VALIDATION.json",
            "transport/PUBLIC_PROJECTION_VALIDATION.json",
            TRANSPORT_ROOT / "PUBLIC_PROJECTION_VALIDATION.json",
        ),
        (
            "methodology-evidence/README.md",
            "transport/ARCHIVE_TRANSPORT_README.md",
            TRANSPORT_ROOT / "README.md",
        ),
        (
            "methodology-evidence/TRANSPORT_GIT_LINE_ENDING_ERROR_AND_CORRECTION.md",
            "transport/TRANSPORT_GIT_LINE_ENDING_ERROR_AND_CORRECTION.md",
            TRANSPORT_ROOT / "TRANSPORT_GIT_LINE_ENDING_ERROR_AND_CORRECTION.md",
        ),
        (
            "published-github/FAC payload readback receipt",
            "github/20260803_fac_blind_comparator_payload_public_readback.json",
            GITHUB_RECEIPT_ROOT
            / "20260803_fac_blind_comparator_payload_commit_3c9489183_19_file_public_readback.json",
        ),
        (
            "published-github/FAC transport correction readback receipt",
            "github/20260803_fac_blind_comparator_transport_public_readback.json",
            GITHUB_RECEIPT_ROOT
            / "20260803_fac_blind_comparator_transport_commit_3c9489183_public_readback.json",
        ),
        (
            "lane-control/FAC transport acceptance decision",
            "decision/ARCHIVE_DECISION_RECORD_FAC_BLIND_COMPARATOR_TRANSPORT_ACCEPTED_20260803.json",
            TRANSPORT_DECISION,
        ),
    )
    members: list[tuple[str, bytes]] = []
    rows: list[dict[str, Any]] = []
    mapping_actions: list[dict[str, object]] = []
    for source_locator, member_path, path in sources:
        if not path.is_file():
            raise RuntimeError(f"Archive-mapping source missing: {path}")
        public_data, row, actions = project_member(
            source_locator, member_path, path.read_bytes()
        )
        members.append((member_path, public_data))
        rows.append(row)
        mapping_actions.extend(actions)

    shared_identity_document = {
        "schema": "shared-decision-log-public-projection-identity-v1",
        "source": {
            **shared_source_identity,
            "bytes": len(shared_source),
            "sha256": sha256_bytes(shared_source),
            "private_custody_id": PRIVATE_ROOT.name,
            "public_disclosure": False,
        },
        "public": {
            **shared_public_identity,
            "bytes": len(shared_public),
            "sha256": sha256_bytes(shared_public),
            "privacy_action_count": len(shared_actions),
            "privacy_actions_by_rule": dict(
                sorted(Counter(str(item["rule"]) for item in shared_actions).items())
            ),
            "privacy_residual_count": 0,
        },
        "source_preserved_unchanged": True,
        "public_projection_minimal_operational_privacy_only": True,
        "errors": [],
    }
    generated = (
        (
            "payload-builder adverse transport history",
            "transport/PAYLOAD_BUILD_ERROR_AND_CORRECTION.md",
            (
                "# FAC dual-DOI payload build error and correction\n\n"
                "The first read-only payload-build attempt on 2026-08-03 "
                "stopped on the first retained-predecessor download with HTTP "
                "406. The session-level records-API `Accept` media type had been "
                "inherited by the file-content request. A second read-only attempt "
                "set `Accept: application/octet-stream`, which this Zenodo endpoint "
                "also rejected with HTTP 406. Anonymous probes established that the "
                "endpoint accepts `*/*` and returns its declared text media type. No "
                "Zenodo draft, upload, metadata edit, or publication occurred in "
                "either attempt; the builder removed each partial public output and "
                "private staging. The correction sets `Accept: */*` only on content "
                "downloads, then replays size, MD5, SHA-256, file UUID, ZIP "
                "membership, and predecessor-record identity before accepting any "
                "retained byte.\n"
            ).encode("utf-8"),
        ),
        (
            "shared-decision-log projection identity",
            "shared/SHARED_DECISION_LOG_PUBLIC_PROJECTION_IDENTITY.json",
            json_bytes(shared_identity_document),
        ),
        (
            "shared-decision-log privacy transformation ledger",
            "shared/SHARED_DECISION_LOG_PRIVACY_TRANSFORMATIONS.csv",
            action_rows_bytes(shared_actions),
        ),
        (
            "archive-mapping member privacy transformation ledger",
            "transport/ARCHIVE_MAPPING_MEMBER_PRIVACY_TRANSFORMATIONS.csv",
            action_rows_bytes(mapping_actions),
        ),
    )
    for locator, member_path, data in generated:
        members.append((member_path, data))
        rows.append(
            {
                "member_path": member_path,
                "source_locator": locator,
                "source_bytes": len(data),
                "source_sha256": sha256_bytes(data),
                "public_bytes": len(data),
                "public_sha256": sha256_bytes(data),
                "privacy_action_count": 0,
                "privacy_rules": "",
                "privacy_result": "PASS_PRIVACY_CLEAN_ARCHIVE_GENERATED_CONTROL",
                "supersession_state": "APPEND_ONLY_RELEASE_CONTROL",
            }
        )

    header = (
        "member_path",
        "source_locator",
        "source_bytes",
        "source_sha256",
        "public_bytes",
        "public_sha256",
        "privacy_action_count",
        "privacy_rules",
        "privacy_result",
        "supersession_state",
    )
    rows.sort(key=lambda row: row["member_path"])
    manifest = csv_bytes(header, ([row[field] for field in header] for row in rows))
    members.append(("ARCHIVE_MAPPING_MANIFEST.csv", manifest))
    archive_path = OUTPUT / ARCHIVE_MAPPING_NAME
    write_zip(archive_path, members)
    return zip_inventory(archive_path, include_members=True), rows


def load_fac_mapping() -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    mapping_path = TRANSPORT_ROOT / "PUBLIC_PROJECTION_IDENTITY_MANIFEST.csv"
    actions_path = TRANSPORT_ROOT / "PRIVACY_TRANSFORMATIONS.csv"
    with mapping_path.open(encoding="utf-8-sig", newline="") as handle:
        mapping = [dict(row) for row in csv.DictReader(handle)]
    with actions_path.open(encoding="utf-8-sig", newline="") as handle:
        actions = [dict(row) for row in csv.DictReader(handle)]
    if len(mapping) != EXPECTED_FAC_FILES or len(actions) != 13:
        raise RuntimeError("FAC public mapping/action counts changed")
    for row in mapping:
        path = FAC_PAYLOAD / row["relative_path"]
        if not path.is_file():
            raise RuntimeError(f"FAC public payload missing: {row['relative_path']}")
        data = path.read_bytes()
        if (len(data), sha256_bytes(data)) != (
            int(row["public_bytes"]),
            row["public_sha256"],
        ):
            raise RuntimeError(f"FAC public mapping changed: {row['relative_path']}")
    rows = identity_rows(FAC_PAYLOAD)
    if (
        len(rows),
        sum(int(row["bytes"]) for row in rows),
        tree_sha256(rows),
    ) != (EXPECTED_FAC_FILES, EXPECTED_FAC_BYTES, EXPECTED_FAC_TREE_SHA256):
        raise RuntimeError("FAC public payload tree changed")
    return mapping, actions


def write_private_custody(shared_source: bytes, decision_source: bytes) -> dict[str, Any]:
    if PRIVATE_ROOT.exists():
        raise RuntimeError(f"Private custody already exists: {PRIVATE_ROOT}")
    temporary = PRIVATE_ROOT.with_name(PRIVATE_ROOT.name + ".tmp")
    if temporary.exists():
        raise RuntimeError(f"Private custody staging already exists: {temporary}")
    raw = temporary / "raw"
    raw.mkdir(parents=True)
    source_rows = (
        ("ENGLISH_GERMANIC_DECISION_LOG_v1.jsonl", shared_source),
        (TRANSPORT_DECISION.name, decision_source),
    )
    for name, data in source_rows:
        (raw / name).write_bytes(data)
    manifest = csv_bytes(
        ("relative_path", "bytes", "sha256", "custody_status"),
        (
            (f"raw/{name}", len(data), sha256_bytes(data), "EXACT_PRIVATE_ORIGINAL")
            for name, data in source_rows
        ),
    )
    (temporary / "PRIVATE_ORIGINAL_IDENTITY_MANIFEST.csv").write_bytes(manifest)
    temporary.rename(PRIVATE_ROOT)
    return {
        "custody_id": PRIVATE_ROOT.name,
        "files": len(source_rows),
        "bytes": sum(len(data) for _, data in source_rows),
        "manifest_bytes": len(manifest),
        "manifest_sha256": sha256_bytes(manifest),
        "source_files_preserved_unchanged": True,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=OUTPUT)
    parser.add_argument("--private-custody-dir", type=Path, default=PRIVATE_ROOT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output = args.output_dir.resolve()
    private = args.private_custody_dir.resolve()
    if output != OUTPUT.resolve() or private != PRIVATE_ROOT.resolve():
        raise RuntimeError("This exact release builder does not permit alternate targets")
    if output.exists():
        raise RuntimeError(f"Output already exists: {output}")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.mkdir()
    try:
        shared_source = SHARED_LOG.read_bytes()
        decision_source = TRANSPORT_DECISION.read_bytes()
        if (len(shared_source), sha256_bytes(shared_source)) != (
            EXPECTED_SHARED_BYTES,
            EXPECTED_SHARED_SHA256,
        ):
            raise RuntimeError("Locked shared decision-log identity moved")
        shared_source_identity = jsonl_identity(shared_source)
        if (
            shared_source_identity["records"],
            shared_source_identity["latest_id"],
        ) != (EXPECTED_SHARED_RECORDS, EXPECTED_SHARED_LATEST):
            raise RuntimeError("Locked shared decision-log cursor moved")

        shared_public, shared_actions = project_text(
            shared_source, "ENGLISH_GERMANIC_DECISION_LOG_v1.jsonl"
        )
        residual = residual_findings(shared_public.decode("utf-8"))
        if residual:
            raise RuntimeError(f"Shared decision-log privacy residual: {residual}")
        shared_public_identity = jsonl_identity(shared_public)
        if shared_public_identity != shared_source_identity:
            raise RuntimeError("Shared decision-log structure changed in projection")
        (output / SHARED_LOG.name).write_bytes(shared_public)

        private_receipt = write_private_custody(shared_source, decision_source)

        session = requests.Session()
        session.headers.update(
            {
                "Accept": "application/vnd.inveniordm.v1+json",
                "User-Agent": "fac-blind-comparator-dual-doi-payload/1.0",
                "Connection": "close",
            }
        )
        methodology = verify_head(
            session, METHODOLOGY_RECORD, METHODOLOGY_CONCEPT, 100
        )
        replication = verify_head(
            session, REPLICATION_RECORD, REPLICATION_CONCEPT, 45
        )
        _, retained_rows, retention_inventory = download_retained_predecessor(
            session, methodology
        )
        archive_mapping_inventory, archive_mapping_rows = build_archive_mapping(
            shared_source,
            shared_public,
            shared_actions,
            shared_source_identity,
            shared_public_identity,
        )
        fac_mapping, fac_actions = load_fac_mapping()
        by_fac_name = {row["relative_path"]: row for row in fac_mapping}
        direct = [
            {
                "relative_path": name,
                "source_bytes": int(by_fac_name[name]["source_bytes"]),
                "source_sha256": by_fac_name[name]["source_sha256"],
                "public_bytes": int(by_fac_name[name]["public_bytes"]),
                "public_sha256": by_fac_name[name]["public_sha256"],
                "privacy_result": "PASS_PRIVACY_CLEAN_PUBLIC_PROJECTION",
                "supersession_state": "FIRST_IMMUTABLE_FINAL_79_OF_79_SNAPSHOT",
                "direct_file_on_methodology": True,
                "direct_file_on_replication": True,
            }
            for name in DIRECT_PROVENANCE
        ]
        control = by_fac_name[CONTROL_NAME]
        if (
            int(control["source_bytes"]),
            control["source_sha256"],
            int(control["public_bytes"]),
            control["public_sha256"],
        ) != (
            CONTROL_ORIGINAL_BYTES,
            CONTROL_ORIGINAL_SHA256,
            CONTROL_PUBLIC_BYTES,
            CONTROL_PUBLIC_SHA256,
        ):
            raise RuntimeError("Dual-DOI control mapping changed")

        index = {
            "schema": "fac-blind-comparator-dual-doi-successor-index-v1",
            "release_id": RELEASE_ID,
            "handoff_id": HANDOFF_ID,
            "built_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "methodology_concept_doi": METHODOLOGY_CONCEPT,
            "replication_concept_doi": REPLICATION_CONCEPT,
            "predecessors": {
                "methodology": {
                    "record_id": METHODOLOGY_RECORD,
                    "version_doi": f"10.5281/zenodo.{METHODOLOGY_RECORD}",
                    "file_count": len(methodology["files"]["entries"]),
                    "latest": True,
                    "published": True,
                },
                "replication": {
                    "record_id": REPLICATION_RECORD,
                    "version_doi": f"10.5281/zenodo.{REPLICATION_RECORD}",
                    "file_count": len(replication["files"]["entries"]),
                    "latest": True,
                    "published": True,
                },
            },
            "control_binding": {
                "relative_path": CONTROL_NAME,
                "original_bytes": CONTROL_ORIGINAL_BYTES,
                "original_sha256": CONTROL_ORIGINAL_SHA256,
                "public_bytes": CONTROL_PUBLIC_BYTES,
                "public_sha256": CONTROL_PUBLIC_SHA256,
                "privacy_result": "PASS_PRIVACY_CLEAN_PUBLIC_PROJECTION",
                "status": (
                    "BOUND_EXACT_ORIGINAL_IDENTITY_WITH_PRIVACY_CLEAN_PUBLIC_PROJECTION"
                ),
                "public_disclosure_of_original": False,
            },
            "fac_source": {
                "files": 19,
                "bytes": 734_768,
                "tree_sha256": (
                    "FD7414EDC70BB86B9968AD2328FA2C1B3F619788E6665F11C97EDADB0FBEF1B8"
                ),
                "private_custody_id": (
                    "20260803T033607CEST_fac-blind-comparator-methodology-r1"
                ),
                "preserved_unchanged": True,
                "public_disclosure": False,
            },
            "fac_public_projection": {
                "files": EXPECTED_FAC_FILES,
                "bytes": EXPECTED_FAC_BYTES,
                "tree_sha256": EXPECTED_FAC_TREE_SHA256,
                "source_to_public": fac_mapping,
                "privacy_transformations": fac_actions,
                "privacy_action_count": len(fac_actions),
                "privacy_residual_count": 0,
                "direct_provenance_surfaces": direct,
            },
            "archive_mapping_zip": {
                "name": ARCHIVE_MAPPING_NAME,
                "bytes": (output / ARCHIVE_MAPPING_NAME).stat().st_size,
                "sha256": sha256_path(output / ARCHIVE_MAPPING_NAME),
                "md5": md5_path(output / ARCHIVE_MAPPING_NAME),
                **archive_mapping_inventory,
                "member_source_to_public": archive_mapping_rows,
                "on_methodology": True,
                "on_replication": True,
            },
            "shared_decision_log": {
                "name": SHARED_LOG.name,
                "source_bytes": len(shared_source),
                "source_sha256": sha256_bytes(shared_source),
                "public_bytes": len(shared_public),
                "public_sha256": sha256_bytes(shared_public),
                "records": shared_source_identity["records"],
                "latest_id": shared_source_identity["latest_id"],
                "privacy_action_count": len(shared_actions),
                "privacy_actions_by_rule": dict(
                    sorted(
                        Counter(str(item["rule"]) for item in shared_actions).items()
                    )
                ),
                "privacy_residual_count": 0,
                "source_private_custody": private_receipt,
                "on_methodology": True,
                "on_replication": True,
            },
            "methodology_file_limit_organization": {
                "mode": "MECHANICAL_EXACT_BYTE_COMPANION_FILE_CONSOLIDATION",
                "editorial_selection": False,
                "distinct_content_omitted": False,
                "removed_direct_predecessor_names": list(sorted(RETENTION_NAMES)),
                "removed_direct_count": len(RETENTION_NAMES),
                "removed_direct_bytes": sum(int(row["bytes"]) for row in retained_rows),
                "retention_archive": {
                    "name": RETENTION_ARCHIVE_NAME,
                    "bytes": (output / RETENTION_ARCHIVE_NAME).stat().st_size,
                    "sha256": sha256_path(output / RETENTION_ARCHIVE_NAME),
                    "md5": md5_path(output / RETENTION_ARCHIVE_NAME),
                    **retention_inventory,
                },
                "direct_retention_manifest": {
                    "name": RETENTION_MANIFEST_NAME,
                    "bytes": (output / RETENTION_MANIFEST_NAME).stat().st_size,
                    "sha256": sha256_path(output / RETENTION_MANIFEST_NAME),
                    "md5": md5_path(output / RETENTION_MANIFEST_NAME),
                },
                "immutable_predecessor_preserved": True,
                "successor_file_count_preview": 99,
            },
            "replication_successor_file_count_preview": 64,
            "scope": {
                "fac_blind_numbers": "1-79",
                "personally_adjudicated": "79/79",
                "numbers_80_81_excluded_from_blind_claim": True,
                "qualitative_only": True,
                "scalar_score_or_ranking": False,
                "whole_fac_gaga_completion_claim": False,
                "continuation_cursor": None,
            },
            "rights": {
                "external_comparator_full_pdf_or_source_files": 0,
                "external_redistribution_license_found": False,
                "authorship_urls_sizes_hashes_and_locator_findings_only": True,
            },
            "github_transport": {
                "branch": "agent/fac-ega-active-custody-20260802",
                "exact_payload_commit": (
                    "3c9489183c9dc46e5fc318b5fecd665b1dfdf4ea"
                ),
                "transport_receipt_head": (
                    "0a341fa5c4c2d96ffa1b487b3194f3c681b2c53c"
                ),
                "payload_raw_readback": "19/19",
                "payload_raw_readback_bytes": 734_806,
                "pull_request": None,
                "merged": False,
            },
            "completion_claimed": False,
            "mathematical_certification_claimed": False,
            "editorial_certification_claimed": False,
            "duplicate_concept_authorized": False,
            "errors": [],
        }
        (output / "ALL_SESSION_PROVENANCE_TRANCHE_INDEX.json").write_bytes(
            json_bytes(index)
        )

        # Re-read the mutable lane controls after every derived object is closed.
        if SHARED_LOG.read_bytes() != shared_source or TRANSPORT_DECISION.read_bytes() != decision_source:
            raise RuntimeError("Lane-control source bytes moved during coherent snapshot")

        validation = {
            "status": "PASS_READ_ONLY_DUAL_DOI_PAYLOAD_BUILD",
            "errors": [],
            "release_id": RELEASE_ID,
            "handoff_id": HANDOFF_ID,
            "zenodo_mutation_performed": False,
            "draft_created": False,
            "predecessors": {
                "methodology_record": METHODOLOGY_RECORD,
                "methodology_files": 100,
                "replication_record": REPLICATION_RECORD,
                "replication_files": 45,
            },
            "fac_public_payload": {
                "files": EXPECTED_FAC_FILES,
                "bytes": EXPECTED_FAC_BYTES,
                "tree_sha256": EXPECTED_FAC_TREE_SHA256,
            },
            "shared_decision_log": {
                "source_records": shared_source_identity["records"],
                "source_bytes": len(shared_source),
                "source_sha256": sha256_bytes(shared_source),
                "public_records": shared_public_identity["records"],
                "public_bytes": len(shared_public),
                "public_sha256": sha256_bytes(shared_public),
                "privacy_actions": len(shared_actions),
                "privacy_residuals": 0,
            },
            "retained_predecessor": {
                "direct_files_organized": len(retained_rows),
                "all_exact": True,
                "archive": RETENTION_ARCHIVE_NAME,
                "manifest": RETENTION_MANIFEST_NAME,
                "zip_member_count": retention_inventory["member_count"],
            },
            "archive_mapping": {
                "archive": ARCHIVE_MAPPING_NAME,
                "zip_member_count": archive_mapping_inventory["member_count"],
                "privacy_residuals": 0,
            },
            "successor_file_count_preview": {
                "methodology": 99,
                "replication": 64,
            },
            "private_custody": private_receipt,
        }
        (output / "PAYLOAD_BUILD_VALIDATION.json").write_bytes(json_bytes(validation))
        print(json.dumps(validation, ensure_ascii=True, indent=2))
        return 0
    except Exception:
        if output.exists():
            shutil.rmtree(output)
        if private.exists():
            shutil.rmtree(private)
        raise


if __name__ == "__main__":
    raise SystemExit(main())
