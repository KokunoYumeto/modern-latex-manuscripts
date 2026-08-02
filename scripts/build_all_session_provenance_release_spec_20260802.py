#!/usr/bin/env python3
"""Build a read-only six-concept Zenodo provenance release specification.

The input is the frozen, privacy-clean 34-object all-session tranche already
bound to an exact GitHub commit.  The same complete set is assigned to the
methodology and replication concepts.  Each corpus concept receives its own
complete provenance ZIP and manifest plus its loose core logbooks.  The builder
performs local reads and anonymous Zenodo reads only; it never creates a draft.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import zipfile
from pathlib import Path, PurePosixPath
from typing import Any, Iterable

import requests


REPO_ROOT = Path(__file__).resolve().parents[1]
API = "https://zenodo.org/api"
PUBLICATION_DATE = "2026-08-02"
SCHEMA = "zenodo-active-custody-release-spec-v1"
MANIFEST_SCHEMA = "zenodo-upload-manifest-v1"
RELEASE_ID = "all-session-mathematical-provenance-20260802-v3"
MAX_ZENODO_FILES = 100
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
TRANCHE_RELATIVE = Path(
    "manifests/provenance-tranches/20260802T204119CEST_all-session-v3"
)
DEFAULT_OUTPUT = REPO_ROOT / (
    "manifests/zenodo-active-custody/all-session-provenance-20260802"
)

TARGETS: dict[str, dict[str, Any]] = {
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
    "deligne": {
        "record_id": 21_745_061,
        "concept_id": 20_410_853,
        "concept_doi": "10.5281/zenodo.20410853",
        "version_doi": "10.5281/zenodo.21745061",
    },
    "sga7": {
        "record_id": 21_756_931,
        "concept_id": 20_410_947,
        "concept_doi": "10.5281/zenodo.20410947",
        "version_doi": "10.5281/zenodo.21756931",
    },
}
SAFE_PUBLISH_ORDER = (
    "methodology",
    "replication",
    "fac_gaga",
    "ega",
    "deligne",
    "sga7",
)

CORPUS_NAMES = {
    "fac_gaga": {
        "FAC__COMPLETE_PROVENANCE.zip",
        "FAC__COMPLETE_PROVENANCE_MANIFEST.csv",
        "FAC__EDITORIAL_DECISION_LOGBOOK.md",
        "FAC__LOGBOOK.md",
        "FAC__STATUS.md",
    },
    "ega": {
        "EGA__COMPLETE_PROVENANCE.zip",
        "EGA__COMPLETE_PROVENANCE_MANIFEST.csv",
        "EGA_EN__LOGBOOK.md",
        "EGA_EN__STATUS.md",
        "EGA_FR__CONTINUATION_HANDOFF.md",
        "EGA_FR__LOGBOOK.md",
        "EGA_FR__STATUS.md",
    },
    "deligne": {
        "DELIGNE__COMPLETE_PROVENANCE.zip",
        "DELIGNE__COMPLETE_PROVENANCE_MANIFEST.csv",
        "D001__LOGBOOK.md",
        "D002__LOGBOOK.md",
        "D003__LOGBOOK.md",
        "D004__LOGBOOK.md",
        "D005_R1__LOGBOOK.md",
        "D005_R2__LOGBOOK.md",
        "D006__LOGBOOK.md",
        "D006__LOGBOOK_RECOVERED_FROM_THREAD_HISTORY_20260802.md",
        "D006__controls__LOGBOOK_STATUS_NUL_CORRUPTION_AND_RECOVERY_20260802.md",
        "D007__LOGBOOK.md",
    },
    "sga7": {
        "SGA7__COMPLETE_PROVENANCE.zip",
        "SGA7__COMPLETE_PROVENANCE_MANIFEST.csv",
        "SGA7I__FRENCH_SOURCE_CORRECTION_LOGBOOK.md",
        "SGA7II__LOGBOOK.md",
    },
}


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value, ensure_ascii=True, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


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
        if archive.testzip() is not None:
            raise RuntimeError(f"ZIP CRC replay failed: {path}")
        infos = [entry for entry in archive.infolist() if not entry.is_dir()]
        names = [entry.filename for entry in infos]
        if len(names) != len(set(names)) or not all(safe_zip_name(n) for n in names):
            raise RuntimeError(f"Unsafe or duplicate ZIP member: {path}")
        for entry in infos:
            digest = hashlib.sha256()
            total = 0
            with archive.open(entry) as handle:
                for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
                    total += len(block)
                    digest.update(block)
            if total != entry.file_size:
                raise RuntimeError(f"ZIP member length changed: {path}/{entry.filename}")
            rows.append(
                {
                    "name": entry.filename,
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


def make_session() -> requests.Session:
    session = requests.Session()
    session.headers.update(
        {
            "Accept": "application/vnd.inveniordm.v1+json",
            "User-Agent": "modern-latex-manuscripts-provenance-spec/1.0",
            "Connection": "close",
        }
    )
    return session


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
    record_id = int(registry["record_id"])
    response = session.get(f"{API}/records/{record_id}?expand=true", timeout=(30, 180))
    if response.status_code != 200:
        raise RuntimeError(f"Zenodo predecessor read failed for {key}: HTTP {response.status_code}")
    record = response.json()
    latest_response = session.get(
        f"{API}/records/{record_id}/versions/latest?expand=true", timeout=(30, 180)
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
        record_id,
        registry["version_doi"],
        registry["concept_doi"],
        True,
        record_id,
    )
    if boundary != expected:
        raise RuntimeError(f"Zenodo predecessor boundary moved for {key}: {boundary}")
    entries = record.get("files", {}).get("entries")
    if not isinstance(entries, dict) or not entries:
        raise RuntimeError(f"Zenodo predecessor files absent for {key}")
    rows: list[dict[str, Any]] = []
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
        "record_id": record_id,
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


def verify_github_commit(commit: str) -> None:
    if not re.fullmatch(r"[0-9a-f]{40}", commit):
        raise RuntimeError("GitHub commit must be a full lowercase SHA-1")
    result = subprocess.run(
        ["git", "cat-file", "-e", f"{commit}^{{commit}}"],
        cwd=REPO_ROOT,
        capture_output=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"Git commit is not locally available: {commit}")
    remote = subprocess.run(
        ["git", "ls-remote", "origin", "refs/heads/agent/fac-ega-active-custody-20260802"],
        cwd=REPO_ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    if not remote or remote.split()[0] != commit:
        raise RuntimeError("The exact GitHub branch head is not the requested commit")


def load_tranche(tranche: Path) -> list[dict[str, Any]]:
    manifest_path = tranche / "UPLOAD_MANIFEST.json"
    document = json.loads(manifest_path.read_text(encoding="utf-8"))
    if document.get("schema") != MANIFEST_SCHEMA:
        raise RuntimeError("Unexpected tranche upload-manifest schema")
    rows = document.get("files")
    if not isinstance(rows, list) or len(rows) != 34:
        raise RuntimeError("The all-session dual-DOI tranche must contain exactly 34 files")
    result: list[dict[str, Any]] = []
    for raw in rows:
        name = str(raw.get("name") or "")
        if not name or Path(name).name != name:
            raise RuntimeError(f"Unsafe upload name: {name!r}")
        path = (tranche / str(raw.get("path") or "")).resolve()
        if path.parent != tranche.resolve() or not path.is_file():
            raise RuntimeError(f"Upload path escaped the frozen tranche: {path}")
        row = dict(raw)
        expected = (
            int(row["bytes"]),
            str(row["sha256"]).upper(),
            str(row["md5"]).lower(),
        )
        observed = (path.stat().st_size, sha256_path(path), md5_path(path))
        if observed != expected:
            raise RuntimeError(f"Frozen tranche object changed: {name}")
        if row.get("privacy_clean") is not True or row.get("dual_doi_provenance") is not True:
            raise RuntimeError(f"Tranche object is not dual-DOI privacy-clean: {name}")
        if name.lower().endswith(".zip"):
            observed_zip = zip_inventory(path)
            supplied_zip = {
                key: row.get(key)
                for key in (
                    "zip_member_count",
                    "zip_uncompressed_bytes",
                    "zip_inventory_sha256",
                )
            }
            if observed_zip != supplied_zip:
                raise RuntimeError(f"Frozen ZIP inventory changed: {name}")
        row["_path"] = path
        result.append(row)
    names = [row["name"] for row in result]
    if len(names) != len(set(names)) or len(names) != len({name.casefold() for name in names}):
        raise RuntimeError("Duplicate or case-colliding tranche filename")

    control_path = tranche / CONTROL_PATH.name
    if (control_path.stat().st_size, sha256_path(control_path)) != (
        CONTROL_PUBLIC_BYTES,
        CONTROL_PUBLIC_SHA256,
    ):
        raise RuntimeError("Privacy-clean controlling file identity changed")
    index = json.loads(
        (tranche / "ALL_SESSION_PROVENANCE_TRANCHE_INDEX.json").read_text(
            encoding="utf-8"
        )
    )
    binding = index.get("control_binding") or {}
    if (
        int(binding.get("original_bytes", -1)),
        binding.get("original_sha256"),
        int(binding.get("public_bytes", -1)),
        binding.get("public_sha256"),
        binding.get("status"),
    ) != (
        CONTROL_BYTES,
        CONTROL_SHA256,
        CONTROL_PUBLIC_BYTES,
        CONTROL_PUBLIC_SHA256,
        "BOUND_EXACT_ORIGINAL_IDENTITY_WITH_PRIVACY_CLEAN_PUBLIC_PROJECTION",
    ):
        raise RuntimeError("All-session index does not bind the controlling identity")
    return sorted(result, key=lambda row: row["name"])


def release_row(row: dict[str, Any], output: Path, *, dual: bool) -> dict[str, Any]:
    result = {
        key: row[key]
        for key in (
            "name",
            "bytes",
            "sha256",
            "md5",
            "role",
            "privacy_clean",
            "supersession_state",
            "zip_member_count",
            "zip_uncompressed_bytes",
            "zip_inventory_sha256",
        )
        if key in row
    }
    result.update(
        {
            "path": path_for_manifest(row["_path"], output),
            "dual_doi_provenance": dual,
        }
    )
    if dual:
        result["control_binding_sha256"] = CONTROL_SHA256
    return result


def write_manifest(path: Path, rows: list[dict[str, Any]]) -> dict[str, Any]:
    payload = json.dumps(
        {"schema": MANIFEST_SCHEMA, "files": rows},
        ensure_ascii=True,
        sort_keys=True,
        indent=2,
    ) + "\n"
    path.write_text(payload, encoding="utf-8", newline="\n")
    return {"bytes": path.stat().st_size, "sha256": sha256_path(path)}


def metadata_append(key: str, github_commit: str) -> dict[str, Any]:
    descriptions = {
        "methodology": (
            "<p>Adds the complete privacy-clean all-session reasoning tranche: 325 "
            "captured FAC, EGA, Deligne D001-D007, and SGA7 provenance files represented "
            "by four complete path/hash-bound ZIPs, their manifests, loose core logbooks, "
            "archive controls, and the append-only shared decision log. The exact same 34 "
            "objects are deposited on the replication DOI.</p>"
        ),
        "replication": (
            "<p>Adds the same complete 34-object privacy-clean all-session provenance "
            "tranche deposited on the methodology DOI, including corpus ZIPs, manifests, "
            "loose logbooks, error/reversal histories, continuation state, and the shared "
            "decision log needed to audit the AI-assisted workflow.</p>"
        ),
        "fac_gaga": (
            "<p>Adds the complete FAC provenance ZIP and manifest plus loose status, "
            "chronological logbook, and editorial decision logbook from the bounded "
            "2026-08-02 custody snapshot.</p>"
        ),
        "ega": (
            "<p>Adds the complete active EGA English-correction and French-canon provenance "
            "ZIP and manifest plus loose English/French logbooks, status records, and the "
            "French continuation handoff. Distinct decisions, errors, reversals, and "
            "superseded generations remain preserved.</p>"
        ),
        "deligne": (
            "<p>Adds the complete Deligne D001-D007 provenance ZIP and manifest plus every "
            "current loose project logbook, including the D006 recovered history and NUL "
            "corruption/recovery record.</p>"
        ),
        "sga7": (
            "<p>Adds the complete SGA7 I/II provenance ZIP and manifest plus the SGA7 I "
            "French-source correction logbook and the SGA7 II chronological logbook.</p>"
        ),
    }
    versions = {
        "methodology": "2026-08-02 v0.20 all-session provenance tranche",
        "replication": "2026-08-02 all-session provenance tranche",
        "fac_gaga": "2026-08-02 FAC provenance tranche",
        "ega": "2026-08-02 active EGA provenance tranche",
        "deligne": "2026-08-02 D001-D007 provenance tranche",
        "sga7": "2026-08-02 SGA7 provenance tranche",
    }
    github_url = (
        "https://github.com/KokunoYumeto/modern-latex-manuscripts/tree/"
        f"{github_commit}/{TRANCHE_RELATIVE.as_posix()}"
    )
    return {
        "version_suffix": versions[key],
        "description_html": descriptions[key],
        "cross_links": [
            {
                "identifier": github_url,
                "scheme": "url",
                "relation_type": "issupplementedby",
            }
        ],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--github-commit", required=True)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    verify_github_commit(args.github_commit)
    output = args.output_dir.resolve()
    allowed = (REPO_ROOT / "manifests/zenodo-active-custody").resolve()
    if output == allowed or allowed not in output.parents:
        raise RuntimeError(f"Output escaped guarded manifest root: {output}")
    if output.exists():
        raise RuntimeError(f"Output already exists: {output}")
    output.mkdir(parents=True)

    tranche = (REPO_ROOT / TRANCHE_RELATIVE).resolve()
    rows = load_tranche(tranche)
    dual_rows = [release_row(row, output, dual=True) for row in rows]
    target_rows: dict[str, list[dict[str, Any]]] = {
        "methodology": dual_rows,
        "replication": dual_rows,
    }
    for key, names in CORPUS_NAMES.items():
        selected = [row for row in rows if row["name"] in names]
        if {row["name"] for row in selected} != names:
            raise RuntimeError(f"Incomplete {key} corpus provenance selection")
        target_rows[key] = [release_row(row, output, dual=False) for row in selected]

    manifest_paths: dict[str, Path] = {}
    manifest_guards: dict[str, dict[str, Any]] = {}
    for key in TARGETS:
        path = output / f"{key}_upload_manifest.json"
        manifest_paths[key] = path
        manifest_guards[key] = write_manifest(path, target_rows[key])

    with make_session() as session:
        guards = {
            key: predecessor_guard(session, key, registry)
            for key, registry in TARGETS.items()
        }
    for key, guard in guards.items():
        new_names = {row["name"] for row in target_rows[key]}
        old_names = {row["name"] for row in guard["files"]}
        if new_names & old_names:
            raise RuntimeError(f"Add-only filename collision for {key}: {sorted(new_names & old_names)}")
        if int(guard["file_count"]) + len(target_rows[key]) > MAX_ZENODO_FILES:
            raise RuntimeError(f"Zenodo file limit exceeded for {key}")
    if guards["methodology"]["file_count"] + len(dual_rows) != MAX_ZENODO_FILES:
        raise RuntimeError("Methodology successor must exactly fill the 100-file boundary")

    targets: dict[str, Any] = {}
    for key in TARGETS:
        targets[key] = {
            "predecessor_guard": guards[key],
            "manifest_path": manifest_paths[key].name,
            "manifest_guard": manifest_guards[key],
            "file_policy": {"mode": "add-only", "replace_names": []},
            "metadata_append": metadata_append(key, args.github_commit),
        }
    spec = {
        "schema": SCHEMA,
        "release_id": RELEASE_ID,
        "publication_date": PUBLICATION_DATE,
        "github_commit": args.github_commit,
        "safe_publish_order": list(SAFE_PUBLISH_ORDER),
        "control": {
            "path": path_for_manifest(CONTROL_PATH, output),
            "bytes": CONTROL_BYTES,
            "sha256": CONTROL_SHA256,
        },
        "targets": targets,
    }
    spec_path = output / "release_spec.json"
    spec_path.write_text(
        json.dumps(spec, ensure_ascii=True, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    summary = {
        "status": "PASS_READ_ONLY_SIX_CONCEPT_RELEASE_SPEC",
        "release_id": RELEASE_ID,
        "github_commit": args.github_commit,
        "release_spec": {
            "path": str(spec_path),
            "bytes": spec_path.stat().st_size,
            "sha256": sha256_path(spec_path),
        },
        "targets": {
            key: {
                "concept_doi": TARGETS[key]["concept_doi"],
                "predecessor_record": TARGETS[key]["record_id"],
                "predecessor_files": guards[key]["file_count"],
                "upload_files": len(target_rows[key]),
                "successor_files": guards[key]["file_count"] + len(target_rows[key]),
                "upload_bytes": sum(int(row["bytes"]) for row in target_rows[key]),
                "manifest_bytes": manifest_guards[key]["bytes"],
                "manifest_sha256": manifest_guards[key]["sha256"],
            }
            for key in TARGETS
        },
        "dual_payload_identical": target_rows["methodology"] == target_rows["replication"],
        "draft_created": False,
        "zenodo_mutation_performed": False,
    }
    (output / "BUILD_VALIDATION.json").write_text(
        json.dumps(summary, ensure_ascii=True, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps(summary, ensure_ascii=True, indent=2))


if __name__ == "__main__":
    main()
