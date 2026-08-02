#!/usr/bin/env python3
"""Build the guarded four-record FAC/EGA active-custody release specification.

This builder performs only local reads plus anonymous Zenodo metadata reads.  It
does not create or modify a Zenodo draft.  Existing predecessor objects are
guarded by record/concept identity, exact file UUID, byte count, and Zenodo MD5.
Every new upload is guarded locally by MD5, SHA-256, and (for ZIPs) a complete
member-level SHA-256 inventory.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import shutil
import subprocess
import time
import zipfile
from pathlib import Path, PurePosixPath
from typing import Any, Iterable

import requests


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = (
    REPO_ROOT / "manifests/zenodo-active-custody/fac-ega-live-20260802"
)
CONTROL_PATH = Path(
    "C:/Users/Floris/Documents/interlanguage/03_projects/language_management/"
    "english_germanic/00_lane_control/"
    "PROJECT_LOGBOOK_METHODOLOGY_REPLICATION_DOI_REQUIREMENT_20260802.md"
)
CONTROL_BYTES = 2_296
CONTROL_SHA256 = (
    "BFA1E3A3EDA94E8C3425BAE50C842610A47D508FB260BF761BA3206883012679"
)
CONTROL_PUBLIC_BYTES = 2_242
CONTROL_PUBLIC_SHA256 = (
    "864DC6B0183161DFA289D6A25DDE268D09E5187C3C4102C854F05422B86DF2AA"
)
PUBLICATION_DATE = "2026-08-02"
RELEASE_ID = "fac-ega-active-custody-20260802-r1"
API = "https://zenodo.org/api"
MAX_ZENODO_FILES = 100

FAC_ROOT = REPO_ROOT / "sources/serre/serre-fac-live-custody-20260802"
EGA_ROOT = REPO_ROOT / "sources/ega/ega-global-french-recheck-live-custody-20260802"

TARGETS: dict[str, dict[str, Any]] = {
    "fac_gaga": {
        "record_id": 21_721_854,
        "concept_id": 21_720_996,
        "concept_doi": "10.5281/zenodo.21720996",
        "version_doi": "10.5281/zenodo.21721854",
    },
    "ega": {
        "record_id": 21_744_406,
        "concept_id": 20_414_353,
        "concept_doi": "10.5281/zenodo.20414353",
        "version_doi": "10.5281/zenodo.21744406",
    },
    "methodology": {
        "record_id": 21_744_853,
        "concept_id": 21_124_403,
        "concept_doi": "10.5281/zenodo.21124403",
        "version_doi": "10.5281/zenodo.21744853",
    },
    "replication": {
        "record_id": 21_707_334,
        "concept_id": 20_461_174,
        "concept_doi": "10.5281/zenodo.20461174",
        "version_doi": "10.5281/zenodo.21707334",
    },
}

CORPUS_TOP_LEVEL = (
    "ARCHIVE_CONTROL_IDENTITIES.json",
    "ARCHIVE_SNAPSHOT_STATUS.md",
    "BINARY_PRIVACY_SCAN.csv",
    "DUAL_DOI_PROVENANCE_MANIFEST.csv",
    "ORIGINAL_PUBLIC_MANIFEST.csv",
    "PDF_EXTRACTED_TEXT_PRIVACY_SCAN.csv",
    "PRIVACY_ACTION_LEDGER.csv",
    "PRIVACY_VALIDATION.json",
    "PUBLIC_ARCHIVE_PARTS.csv",
    "README.md",
    "SHA256SUMS.csv",
    "SNAPSHOT_VALIDATION.json",
    "archive_controls/ARCHIVE_PROACTIVE_PRIVACY_AND_SUBSTANTIVE_UPDATE_REQUIREMENT_20260802.md",
    "archive_controls/PROJECT_LOGBOOK_METHODOLOGY_REPLICATION_DOI_REQUIREMENT_20260802.md",
)

FAC_DUAL_LOOSE = (
    "provenance/LOGBOOK.md",
    "provenance/EDITORIAL_DECISION_LOGBOOK.md",
    "provenance/STATUS.md",
    "provenance/controls/EDITORIAL_SELF_CORRECTION_LEDGER.csv",
)

EGA_DUAL_LOOSE = (
    "provenance/french_canon/LOGBOOK.md",
    "provenance/french_canon/CONTINUATION_HANDOFF.md",
    "provenance/french_canon/STATUS.md",
    "provenance/successor/LOGBOOK.md",
    "provenance/successor/STATUS.md",
    "provenance/french_canon/controls/ENGLISH_NORMALIZATION_DECISION_AND_REVISION_POLICY_20260802.md",
    "provenance/french_canon/controls/ENGLISH_CORRECTION_RECHECK_APPEND_20260802.jsonl",
    "provenance/french_canon/controls/ENGLISH_CORRECTION_RECHECK_APPEND_P70_20260802.jsonl",
    "provenance/french_canon/controls/ENGLISH_CORRECTION_RECHECK_APPEND_P71_20260802.jsonl",
    "provenance/french_canon/controls/ENGLISH_CORRECTION_RECHECK_APPEND_P71_P72_20260802.jsonl",
    "provenance/french_canon/controls/ENGLISH_CORRECTION_RECHECK_APPEND_P73_20260802.jsonl",
    "provenance/french_canon/controls/ENGLISH_CORRECTION_RECHECK_APPEND_P74_20260802.jsonl",
    "provenance/french_canon/controls/ENGLISH_CORRECTION_RECHECK_APPEND_P75_20260802.jsonl",
    "provenance/french_canon/controls/ENGLISH_CORRECTION_REPAIR_APPLICATION_20260802.jsonl",
    "provenance/french_canon/controls/ENGLISH_CORRECTION_REPAIR_APPLICATION_P70_20260802.jsonl",
    "provenance/french_canon/controls/ENGLISH_CORRECTION_REPAIR_APPLICATION_P71_20260802.jsonl",
    "provenance/french_canon/controls/ENGLISH_CORRECTION_REPAIR_APPLICATION_P71_P72_20260802.jsonl",
    "provenance/french_canon/controls/ENGLISH_CORRECTION_REPAIR_APPLICATION_P73_20260802.jsonl",
    "provenance/french_canon/controls/ENGLISH_CORRECTION_REPAIR_APPLICATION_P74_20260802.jsonl",
    "provenance/french_canon/controls/ENGLISH_CORRECTION_REPAIR_APPLICATION_P75_20260802.jsonl",
    "provenance/french_canon/controls/ENGLISH_REPAIR_VALIDATION_SUPERSESSION_P70_20260802.jsonl",
    "provenance/french_canon/controls/ENGLISH_REPAIR_VALIDATION_SUPERSESSION_P71_20260802.jsonl",
    "provenance/french_canon/controls/WORKFLOW_ERROR_APPEND_20260802.jsonl",
)

SHARED_CONTROL_PATHS = (
    "ARCHIVE_CONTROL_IDENTITIES.json",
    "archive_controls/ARCHIVE_PROACTIVE_PRIVACY_AND_SUBSTANTIVE_UPDATE_REQUIREMENT_20260802.md",
    "archive_controls/PROJECT_LOGBOOK_METHODOLOGY_REPLICATION_DOI_REQUIREMENT_20260802.md",
)


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value, ensure_ascii=True, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def hash_path(path: Path, algorithm: str) -> str:
    digest = (
        hashlib.md5(usedforsecurity=False)
        if algorithm == "md5"
        else hashlib.sha256()
    )
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    value = digest.hexdigest()
    return value.lower() if algorithm == "md5" else value.upper()


def sha256_path(path: Path) -> str:
    return hash_path(path, "sha256")


def md5_path(path: Path) -> str:
    return hash_path(path, "md5")


def safe_zip_name(name: str) -> bool:
    pure = PurePosixPath(name)
    return (
        bool(name)
        and name == name.replace("\\", "/")
        and not pure.is_absolute()
        and ".." not in pure.parts
        and not re.match(r"^[A-Za-z]:", name)
    )


def zip_inventory(path: Path) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    with zipfile.ZipFile(path) as archive:
        infos = [info for info in archive.infolist() if not info.is_dir()]
        names = [info.filename for info in infos]
        if len(names) != len(set(names)) or not all(safe_zip_name(name) for name in names):
            raise RuntimeError(f"Unsafe or duplicate ZIP member: {path}")
        for info in infos:
            digest = hashlib.sha256()
            total = 0
            with archive.open(info) as handle:
                for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
                    total += len(block)
                    digest.update(block)
            if total != info.file_size:
                raise RuntimeError(f"ZIP member length changed: {info.filename}")
            rows.append(
                {
                    "name": info.filename,
                    "bytes": total,
                    "sha256": digest.hexdigest().upper(),
                }
            )
    rows.sort(key=lambda row: row["name"])
    return {
        "zip_member_count": len(rows),
        "zip_uncompressed_bytes": sum(int(row["bytes"]) for row in rows),
        "zip_inventory_sha256": sha256_bytes(canonical_bytes(rows)),
    }


def path_for_manifest(path: Path, manifest_dir: Path) -> str:
    return os.path.relpath(path, manifest_dir).replace("\\", "/")


def remote_name(prefix: str, relative: str) -> str:
    value = f"{prefix}__{relative.replace('/', '__')}"
    if len(value.encode("utf-8")) > 240 or Path(value).name != value:
        raise RuntimeError(f"Unsafe or long Zenodo filename: {value}")
    return value


def role_for(relative: str, *, corpus_transport: bool = False) -> str:
    lower = relative.casefold()
    if corpus_transport:
        if lower.endswith(".zip"):
            return "privacy-clean public custody transport archive"
        if "manifest" in lower or "sha256sums" in lower or "archive_parts" in lower:
            return "public custody manifest"
        if "privacy" in lower or "scan" in lower:
            return "privacy validation and transformation evidence"
        if "status" in lower or "readme" in lower:
            return "public custody status and continuation guide"
        return "public custody control"
    if "dual_doi_provenance_manifest" in lower:
        return "public provenance manifest"
    if lower.endswith(".zip"):
        return "dual DOI complete provenance archive"
    if "logbook" in lower:
        return "privacy-clean chronological logbook decision revision provenance"
    if "continuation" in lower or "status" in lower:
        return "privacy-clean continuation provenance record"
    if "supersession" in lower:
        return "privacy-clean append-only revision reversal provenance"
    if "workflow_error" in lower:
        return "privacy-clean append-only error history provenance"
    if "decision" in lower or "recheck" in lower or "repair_application" in lower:
        return "privacy-clean decision rationale and revision provenance"
    if "manifest" in lower or "identities" in lower:
        return "public provenance manifest and identity binding"
    return "privacy-clean archive provenance control"


def upload_row(
    name: str,
    path: Path,
    role: str,
    manifest_dir: Path,
    *,
    dual: bool,
) -> dict[str, Any]:
    if not path.is_file():
        raise RuntimeError(f"Missing upload object: {path}")
    row: dict[str, Any] = {
        "name": name,
        "path": path_for_manifest(path, manifest_dir),
        "bytes": path.stat().st_size,
        "md5": md5_path(path),
        "sha256": sha256_path(path),
        "role": role,
        "dual_doi_provenance": dual,
        "privacy_clean": True,
        "control_binding_sha256": CONTROL_SHA256,
    }
    if path.suffix.casefold() == ".zip":
        row.update(zip_inventory(path))
    return row


def load_dual_manifest(root: Path) -> dict[str, dict[str, str]]:
    path = root / "DUAL_DOI_PROVENANCE_MANIFEST.csv"
    with path.open(encoding="utf-8-sig", newline="") as handle:
        rows = {row["relative_path"]: row for row in csv.DictReader(handle)}
    if not rows:
        raise RuntimeError(f"Empty dual DOI manifest: {path}")
    return rows


def validate_manifest_member(
    root: Path, manifest: dict[str, dict[str, str]], relative: str
) -> Path:
    row = manifest.get(relative)
    if row is None:
        raise RuntimeError(f"Dual DOI manifest omits {relative}")
    path = root / PurePosixPath(relative)
    observed = (path.stat().st_size, sha256_path(path))
    expected = (int(row["bytes"]), row["sha256"].upper())
    if observed != expected:
        raise RuntimeError(f"Dual DOI member identity changed: {relative}")
    if row.get("methodology_doi") != TARGETS["methodology"]["concept_doi"]:
        raise RuntimeError(f"Methodology DOI binding changed: {relative}")
    if row.get("replication_doi") != TARGETS["replication"]["concept_doi"]:
        raise RuntimeError(f"Replication DOI binding changed: {relative}")
    return path


def make_session() -> requests.Session:
    session = requests.Session()
    session.headers.update(
        {
            "Accept": "application/vnd.inveniordm.v1+json",
            "User-Agent": "modern-latex-manuscripts-release-spec/1.0",
            "Connection": "close",
        }
    )
    return session


def load_record(session: requests.Session, record_id: int) -> dict[str, Any]:
    response = session.get(
        f"{API}/records/{record_id}?expand=true", timeout=(30, 180)
    )
    if response.status_code != 200:
        raise RuntimeError(f"Zenodo record {record_id}: HTTP {response.status_code}")
    return response.json()


def concept_doi(record: dict[str, Any]) -> str | None:
    return (
        record.get("parent", {})
        .get("pids", {})
        .get("doi", {})
        .get("identifier")
        or record.get("conceptdoi")
    )


def version_doi(record: dict[str, Any]) -> str | None:
    return record.get("pids", {}).get("doi", {}).get("identifier") or record.get(
        "doi"
    )


def predecessor_guard(
    session: requests.Session, key: str, registry: dict[str, Any]
) -> dict[str, Any]:
    record = load_record(session, int(registry["record_id"]))
    latest_response = session.get(
        f"{API}/records/{registry['record_id']}/versions/latest?expand=true",
        timeout=(30, 180),
    )
    if latest_response.status_code != 200:
        raise RuntimeError(f"Zenodo latest probe failed for {key}")
    latest = latest_response.json()
    boundary = (
        int(record["id"]),
        version_doi(record),
        concept_doi(record),
        bool(record.get("is_published")),
        int(latest["id"]),
    )
    expected = (
        int(registry["record_id"]),
        registry["version_doi"],
        registry["concept_doi"],
        True,
        int(registry["record_id"]),
    )
    if boundary != expected:
        raise RuntimeError(f"Zenodo predecessor boundary moved for {key}: {boundary}")
    entries = record.get("files", {}).get("entries")
    if not isinstance(entries, dict) or not entries:
        raise RuntimeError(f"Zenodo predecessor file entries absent for {key}")
    rows = []
    for name, entry in entries.items():
        checksum = str(entry["checksum"]).lower().removeprefix("md5:")
        file_id = str(entry.get("id") or "").lower()
        if not re.fullmatch(r"[0-9a-f]{32}", checksum):
            raise RuntimeError(f"Invalid Zenodo MD5 for {key}/{name}")
        if not re.fullmatch(r"[0-9a-f-]{36}", file_id):
            raise RuntimeError(f"Invalid Zenodo file UUID for {key}/{name}")
        rows.append(
            {
                "name": name,
                "bytes": int(entry["size"]),
                "md5": checksum,
                "zenodo_file_id": file_id,
            }
        )
    rows.sort(key=lambda row: row["name"])
    return {
        "record_id": int(registry["record_id"]),
        "concept_id": int(registry["concept_id"]),
        "concept_doi": registry["concept_doi"],
        "version_doi": registry["version_doi"],
        "title": record["metadata"]["title"],
        "file_count": len(rows),
        "total_bytes": sum(int(row["bytes"]) for row in rows),
        "inventory_sha256": sha256_bytes(canonical_bytes(rows)),
        "identity_method": "zenodo_inherited_object_uuid_size_md5",
        "files": rows,
    }


def corpus_manifest(
    root: Path, prefix: str, manifest_dir: Path
) -> list[dict[str, Any]]:
    paths = [root / PurePosixPath(relative) for relative in CORPUS_TOP_LEVEL]
    paths.extend(sorted((root / "public_zip_parts").glob("*.zip")))
    rows = [
        upload_row(
            remote_name(prefix, path.relative_to(root).as_posix()),
            path,
            role_for(path.relative_to(root).as_posix(), corpus_transport=True),
            manifest_dir,
            dual=False,
        )
        for path in paths
    ]
    names = [row["name"] for row in rows]
    if len(names) != len(set(names)):
        raise RuntimeError(f"Duplicate corpus upload name for {prefix}")
    return sorted(rows, key=lambda row: row["name"])


def dual_manifest(manifest_dir: Path) -> list[dict[str, Any]]:
    fac_manifest = load_dual_manifest(FAC_ROOT)
    ega_manifest = load_dual_manifest(EGA_ROOT)
    rows: list[dict[str, Any]] = []
    by_name: dict[str, dict[str, Any]] = {}

    def add(name: str, path: Path, role: str) -> None:
        row = upload_row(name, path, role, manifest_dir, dual=True)
        previous = by_name.get(name)
        if previous is not None:
            identity = (row["bytes"], row["sha256"])
            previous_identity = (previous["bytes"], previous["sha256"])
            if identity != previous_identity:
                raise RuntimeError(f"Dual DOI filename collision: {name}")
            return
        by_name[name] = row
        rows.append(row)

    shared_remote_names = {
        "ARCHIVE_CONTROL_IDENTITIES.json": "ARCHIVE_CONTROL_IDENTITIES.json",
        "archive_controls/ARCHIVE_PROACTIVE_PRIVACY_AND_SUBSTANTIVE_UPDATE_REQUIREMENT_20260802.md": "ARCHIVE_PROACTIVE_PRIVACY_AND_SUBSTANTIVE_UPDATE_REQUIREMENT_20260802.md",
        "archive_controls/PROJECT_LOGBOOK_METHODOLOGY_REPLICATION_DOI_REQUIREMENT_20260802.md": "PROJECT_LOGBOOK_METHODOLOGY_REPLICATION_DOI_REQUIREMENT_20260802.md",
    }
    for relative in SHARED_CONTROL_PATHS:
        fac_path = validate_manifest_member(FAC_ROOT, fac_manifest, relative)
        ega_path = validate_manifest_member(EGA_ROOT, ega_manifest, relative)
        if (fac_path.stat().st_size, sha256_path(fac_path)) != (
            ega_path.stat().st_size,
            sha256_path(ega_path),
        ):
            raise RuntimeError(f"Shared archive control diverged: {relative}")
        add(shared_remote_names[relative], fac_path, role_for(relative))

    for relative in FAC_DUAL_LOOSE:
        path = validate_manifest_member(FAC_ROOT, fac_manifest, relative)
        add(remote_name("FAC_20260802", relative), path, role_for(relative))
    for relative in EGA_DUAL_LOOSE:
        path = validate_manifest_member(EGA_ROOT, ega_manifest, relative)
        add(remote_name("EGA_20260802", relative), path, role_for(relative))

    add(
        "FAC_20260802__DUAL_DOI_PROVENANCE_MANIFEST.csv",
        FAC_ROOT / "DUAL_DOI_PROVENANCE_MANIFEST.csv",
        "public provenance manifest",
    )
    add(
        "EGA_20260802__DUAL_DOI_PROVENANCE_MANIFEST.csv",
        EGA_ROOT / "DUAL_DOI_PROVENANCE_MANIFEST.csv",
        "public provenance manifest",
    )
    fac_archives = sorted((FAC_ROOT / "dual_doi").glob("*.zip"))
    ega_archives = sorted((EGA_ROOT / "dual_doi").glob("*.zip"))
    if len(fac_archives) != 1 or len(ega_archives) != 1:
        raise RuntimeError(
            "Expected exactly one complete dual-DOI provenance ZIP per corpus; "
            f"got FAC={len(fac_archives)}, EGA={len(ega_archives)}"
        )
    add(
        "FAC_20260802__Methodology_Replication_Provenance.zip",
        fac_archives[0],
        "dual DOI complete provenance archive",
    )
    add(
        "EGA_20260802__Methodology_Replication_Provenance.zip",
        ega_archives[0],
        "dual DOI complete provenance archive",
    )
    if len(rows) != 34:
        raise RuntimeError(f"Expected exactly 34 dual DOI upload objects; got {len(rows)}")
    return sorted(rows, key=lambda row: row["name"])


def write_json(path: Path, value: Any) -> None:
    path.write_text(
        json.dumps(value, ensure_ascii=True, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def write_manifest(path: Path, rows: list[dict[str, Any]]) -> dict[str, Any]:
    document = {"schema": "zenodo-upload-manifest-v1", "files": rows}
    write_json(path, document)
    return {"bytes": path.stat().st_size, "sha256": sha256_path(path)}


def metadata_append(key: str, github_commit: str) -> dict[str, Any]:
    base = "https://github.com/KokunoYumeto/modern-latex-manuscripts/tree"
    fac_link = f"{base}/{github_commit}/sources/serre/serre-fac-live-custody-20260802"
    ega_link = f"{base}/{github_commit}/sources/ega/ega-global-french-recheck-live-custody-20260802"
    descriptions = {
        "fac_gaga": (
            "<p>Adds an archive-owned privacy-clean projection of a sequential "
            "live FAC capture. The 851-file private custody is exact; 795 files "
            "are publicly projected and 56 rights-uncleared authority files "
            "remain private-only with exact manifest identities. U0041 content "
            "and the U0036-bound validator are preserved as disagreeing evidence.</p>"
        ),
        "ega": (
            "<p>Adds an archive-owned privacy-clean projection of the live EGA "
            "successor and French-canon custody trees. The 1,472-file private "
            "custody is exact; 257 files are publicly projected and 1,215 "
            "rights-uncleared authority objects remain private-only with exact "
            "manifest identities. The captured source/R9 identity disagreement "
            "is preserved and no coherent-R9 or completion claim is made.</p>"
        ),
        "methodology": (
            "<p>Adds the privacy-clean FAC/EGA logbooks, decision rationales, "
            "append-only revision, reversal and error histories, and continuation "
            "records. The 100-file record limit is met by two complete provenance "
            "ZIPs, two loose exact manifests, and first-class loose control and "
            "history surfaces; every ZIP member remains path/bytes/SHA-bound.</p>"
        ),
        "replication": (
            "<p>Adds the exact same privacy-clean FAC/EGA provenance payload as "
            "the methodology DOI: complete provenance ZIPs and manifests plus "
            "first-class loose logbook, decision, revision, reversal, error, and "
            "continuation surfaces.</p>"
        ),
    }
    suffixes = {
        "fac_gaga": "2026-08-02 active FAC custody snapshot",
        "ega": "2026-08-02 active EGA French-recheck custody snapshot",
        "methodology": "2026-08-02 FAC/EGA dual-DOI provenance",
        "replication": "2026-08-02 FAC/EGA dual-DOI provenance",
    }
    links = [fac_link] if key == "fac_gaga" else [ega_link]
    if key in {"methodology", "replication"}:
        links = [fac_link, ega_link]
    return {
        "version_suffix": suffixes[key],
        "description_html": descriptions[key],
        "cross_links": [
            {
                "identifier": link,
                "scheme": "url",
                "relation_type": "issupplementedby",
            }
            for link in links
        ],
    }


def verify_github_commit(commit: str) -> None:
    if not re.fullmatch(r"[0-9a-f]{40}", commit):
        raise RuntimeError("--github-commit must be a lowercase 40-hex commit")
    check = subprocess.run(
        ["git", "cat-file", "-e", f"{commit}^{{commit}}"],
        cwd=REPO_ROOT,
        check=False,
    )
    if check.returncode != 0:
        raise RuntimeError(f"Git commit is not locally available: {commit}")
    for relative in (
        "sources/serre/serre-fac-live-custody-20260802/README.md",
        "sources/ega/ega-global-french-recheck-live-custody-20260802/README.md",
    ):
        probe = subprocess.run(
            ["git", "cat-file", "-e", f"{commit}:{relative}"],
            cwd=REPO_ROOT,
            check=False,
        )
        if probe.returncode != 0:
            raise RuntimeError(f"Git commit omits custody path: {relative}")


def prepare_output(path: Path, replace: bool) -> None:
    allowed_root = (REPO_ROOT / "manifests/zenodo-active-custody").resolve()
    resolved = path.resolve()
    if resolved == allowed_root or allowed_root not in resolved.parents:
        raise RuntimeError(f"Output must be below {allowed_root}")
    if resolved.exists():
        if not replace:
            raise RuntimeError(f"Output exists; use --replace-output: {resolved}")
        shutil.rmtree(resolved)
    resolved.mkdir(parents=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--github-commit", required=True)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--replace-output", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    verify_github_commit(args.github_commit)
    if (CONTROL_PATH.stat().st_size, sha256_path(CONTROL_PATH)) != (
        CONTROL_BYTES,
        CONTROL_SHA256,
    ):
        raise RuntimeError("Controlling dual-DOI requirement identity changed")
    output = args.output_dir.resolve()
    prepare_output(output, args.replace_output)

    fac_rows = corpus_manifest(FAC_ROOT, "FAC_20260802", output)
    ega_rows = corpus_manifest(EGA_ROOT, "EGA_20260802", output)
    dual_rows = dual_manifest(output)
    public_controls = [
        row
        for row in dual_rows
        if row["name"]
        == "PROJECT_LOGBOOK_METHODOLOGY_REPLICATION_DOI_REQUIREMENT_20260802.md"
    ]
    if len(public_controls) != 1 or (
        public_controls[0]["bytes"], public_controls[0]["sha256"]
    ) != (CONTROL_PUBLIC_BYTES, CONTROL_PUBLIC_SHA256):
        raise RuntimeError("Privacy-clean public control identity changed")

    manifest_paths = {
        "fac_gaga": output / "fac_gaga_upload_manifest.json",
        "ega": output / "ega_upload_manifest.json",
        "dual": output / "methodology_replication_upload_manifest.json",
    }
    manifest_guards = {
        "fac_gaga": write_manifest(manifest_paths["fac_gaga"], fac_rows),
        "ega": write_manifest(manifest_paths["ega"], ega_rows),
        "dual": write_manifest(manifest_paths["dual"], dual_rows),
    }

    session = make_session()
    guards = {
        key: predecessor_guard(session, key, registry)
        for key, registry in TARGETS.items()
    }
    if guards["methodology"]["file_count"] + len(dual_rows) != MAX_ZENODO_FILES:
        raise RuntimeError("Methodology successor must resolve to exactly 100 files")
    for key, rows in (("fac_gaga", fac_rows), ("ega", ega_rows)):
        if guards[key]["file_count"] + len(rows) > MAX_ZENODO_FILES:
            raise RuntimeError(f"{key} successor exceeds Zenodo file limit")
    if guards["replication"]["file_count"] + len(dual_rows) > MAX_ZENODO_FILES:
        raise RuntimeError("Replication successor exceeds Zenodo file limit")

    spec_targets: dict[str, Any] = {}
    for key in ("fac_gaga", "ega", "methodology", "replication"):
        manifest_key = key if key in {"fac_gaga", "ega"} else "dual"
        spec_targets[key] = {
            "predecessor_guard": guards[key],
            "manifest_path": manifest_paths[manifest_key].name,
            "manifest_guard": manifest_guards[manifest_key],
            "file_policy": {"mode": "add-only"},
            "metadata_append": metadata_append(key, args.github_commit),
        }
    spec = {
        "schema": "zenodo-active-custody-release-spec-v1",
        "release_id": RELEASE_ID,
        "publication_date": PUBLICATION_DATE,
        "safe_publish_order": ["methodology", "replication", "fac_gaga", "ega"],
        "control": {
            "path": path_for_manifest(CONTROL_PATH, output),
            "bytes": CONTROL_BYTES,
            "sha256": CONTROL_SHA256,
        },
        "github_commit": args.github_commit,
        "targets": spec_targets,
    }
    spec_path = output / "release_spec.json"
    write_json(spec_path, spec)
    validation = {
        "schema": "fac-ega-active-custody-release-spec-build-v1",
        "status": "PASS_READ_ONLY_RELEASE_SPEC_BUILD",
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "zenodo_mutation_performed": False,
        "github_commit": args.github_commit,
        "release_spec": {
            "path": spec_path.name,
            "bytes": spec_path.stat().st_size,
            "sha256": sha256_path(spec_path),
        },
        "upload_manifests": {
            key: {
                **manifest_guards[key],
                "file_count": len(
                    fac_rows if key == "fac_gaga" else ega_rows if key == "ega" else dual_rows
                ),
            }
            for key in ("fac_gaga", "ega", "dual")
        },
        "successor_file_counts": {
            "fac_gaga": guards["fac_gaga"]["file_count"] + len(fac_rows),
            "ega": guards["ega"]["file_count"] + len(ega_rows),
            "methodology": guards["methodology"]["file_count"] + len(dual_rows),
            "replication": guards["replication"]["file_count"] + len(dual_rows),
        },
        "dual_doi_payload_identical": True,
        "dual_doi_new_file_count": len(dual_rows),
        "zenodo_file_limit": MAX_ZENODO_FILES,
        "predecessor_identity_method": "zenodo_inherited_object_uuid_size_md5",
        "new_payload_identity_method": "local_md5_sha256_and_zip_member_sha256",
        "errors": [],
    }
    validation_path = output / "BUILD_VALIDATION.json"
    write_json(validation_path, validation)
    print(json.dumps(validation, ensure_ascii=True, indent=2))


if __name__ == "__main__":
    main()
