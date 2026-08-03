#!/usr/bin/env python3
"""Bind the FAC blind-comparator payload to a guarded dual-DOI release spec.

The payload must already be committed and pushed at the supplied GitHub
commit.  This builder performs local verification and anonymous Zenodo reads
only.  It creates no draft and publishes nothing.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
from pathlib import Path
from typing import Any

import build_all_session_provenance_release_spec_20260802 as base


REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT = REPO_ROOT / (
    "manifests/zenodo-active-custody/"
    "fac-blind-comparator-dual-doi-20260803-r1"
)
FAC_ROOT = REPO_ROOT / (
    "manifests/methodology-evidence/"
    "20260803_fac-blind-comparator-r1"
)
FAC_PAYLOAD = FAC_ROOT / "payload"
RELEASE_ID = "fac-blind-comparator-dual-doi-20260803-r1"
PUBLICATION_DATE = "2026-08-03"
CONTROL_NAME = "PROJECT_LOGBOOK_METHODOLOGY_REPLICATION_DOI_REQUIREMENT_20260802.md"
SHARED_NAME = "ENGLISH_GERMANIC_DECISION_LOG_v1.jsonl"
INDEX_NAME = "ALL_SESSION_PROVENANCE_TRANCHE_INDEX.json"
ARCHIVE_MAPPING_NAME = "FAC_BLIND_COMPARATOR_ARCHIVE_MAPPING_20260803.zip"
RETENTION_ARCHIVE_NAME = (
    "24_Retained_Interlanguage_Companion_Manifests_Statuses_20260803.zip"
)
RETENTION_MANIFEST_NAME = (
    "24a_Retained_Interlanguage_Companion_Manifests_"
    "Statuses_20260803_MANIFEST.csv"
)
RETENTION_INNER_MANIFEST = "RETENTION_MANIFEST.csv"
SAFE_PUBLISH_ORDER = ("methodology", "replication")
TARGETS: dict[str, dict[str, Any]] = {
    "methodology": {
        "record_id": 21_764_482,
        "concept_id": 21_124_403,
        "concept_doi": "10.5281/zenodo.21124403",
        "version_doi": "10.5281/zenodo.21764482",
    },
    "replication": {
        "record_id": 21_764_484,
        "concept_id": 20_461_174,
        "concept_doi": "10.5281/zenodo.20461174",
        "version_doi": "10.5281/zenodo.21764484",
    },
}

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


def relative(path: Path) -> str:
    return os.path.relpath(path, OUTPUT).replace("\\", "/")


def role_for_fac(name: str) -> str:
    upper = name.upper()
    if name == "FAC_PROJECT_LOGBOOK_SNAPSHOT.md":
        return "privacy-clean chronological logbook continuation provenance"
    if name == "FAC_EDITORIAL_DECISION_LOGBOOK_SNAPSHOT.md":
        return "privacy-clean decision rationale revision provenance"
    if name == "FAC_EDITORIAL_SELF_CORRECTION_LEDGER_PRIVACY_CLEAN.csv":
        return "privacy-clean append-only revision reversal error provenance"
    if name == CONTROL_NAME:
        return "privacy-clean dual-DOI logbook control projection"
    if "MANIFEST" in upper or "INVENTORY" in upper or "IDENTIT" in upper:
        return "privacy-clean evidence identity manifest"
    if "RIGHTS" in upper:
        return "privacy-clean rights caveat and source provenance"
    if "VALIDATION" in upper or "READINESS" in upper:
        return "privacy-clean bounded operational validation"
    if "REPORT" in upper or "METHODOLOGY" in upper or name == "README.md":
        return "privacy-clean qualitative methodology evidence"
    return "privacy-clean FAC comparator evidence"


def upload_row(
    name: str,
    path: Path,
    role: str,
    *,
    dual: bool,
    supersession: str,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "name": name,
        "path": relative(path),
        "bytes": path.stat().st_size,
        "md5": base.md5_path(path),
        "sha256": base.sha256_path(path),
        "role": role,
        "dual_doi_provenance": dual,
        "privacy_clean": True,
        "supersession_state": supersession,
    }
    if dual:
        row["control_binding_sha256"] = base.CONTROL_SHA256
    if path.suffix.casefold() == ".zip":
        row.update(base.zip_inventory(path))
    return row


def load_fac_rows() -> list[dict[str, Any]]:
    mapping_path = FAC_ROOT / "PUBLIC_PROJECTION_IDENTITY_MANIFEST.csv"
    with mapping_path.open(encoding="utf-8-sig", newline="") as handle:
        mapping = [dict(row) for row in csv.DictReader(handle)]
    if len(mapping) != 19:
        raise RuntimeError("FAC source-to-public mapping must have 19 rows")
    rows: list[dict[str, Any]] = []
    for item in sorted(mapping, key=lambda row: row["relative_path"]):
        name = item["relative_path"]
        path = FAC_PAYLOAD / name
        row = upload_row(
            name,
            path,
            role_for_fac(name),
            dual=True,
            supersession=(
                "FIRST_IMMUTABLE_FINAL_FAC_1_79_BLIND_COMPARATOR_EVIDENCE_SNAPSHOT"
            ),
        )
        if (row["bytes"], row["sha256"]) != (
            int(item["public_bytes"]),
            item["public_sha256"],
        ):
            raise RuntimeError(f"FAC public payload changed: {name}")
        rows.append(row)
    return rows


def metadata_append(key: str, github_commit: str) -> dict[str, Any]:
    if key == "methodology":
        version = "2026-08-03 v0.22 FAC blind-comparator evidence"
        description = (
            "<p>Adds the chronology-bounded accidental held-out comparison evidence "
            "for FAC nos. 1-79: nineteen direct privacy-clean evidence files including "
            "the full chronological project logbook, editorial-decision logbook, and "
            "219-row append-only self-correction ledger. It also replaces the shared "
            "471-record decision-log projection and adds the exact archive privacy/"
            "transport mapping ZIP. To remain below Zenodo's 100-file ceiling, 22 "
            "legacy companion manifest/hash/status files are mechanically reorganized "
            "as exact bytes inside one indexed preservation ZIP with the identical "
            "manifest direct. No distinct content is dropped; immutable predecessor "
            "versions retain every former direct form.</p>"
        )
    else:
        version = "2026-08-03 FAC blind-comparator evidence"
        description = (
            "<p>Adds the exact same chronology-bounded FAC nos. 1-79 evidence, direct "
            "logbooks, append-only correction history, 471-record shared decision-log "
            "projection, and archive mapping deposited on the methodology DOI. The "
            "external Achinger-Krupa PDF/source remain absent because no explicit "
            "redistribution license was found. The comparison is qualitative only; "
            "nos. 80-81 are excluded from blind claims.</p>"
        )
    links = [
        {
            "identifier": (
                "https://github.com/KokunoYumeto/modern-latex-manuscripts/tree/"
                f"{github_commit}/manifests/methodology-evidence/"
                "20260803_fac-blind-comparator-r1"
            ),
            "scheme": "url",
            "relation_type": "issupplementedby",
        },
        {
            "identifier": (
                "https://github.com/KokunoYumeto/modern-latex-manuscripts/tree/"
                f"{github_commit}/manifests/zenodo-active-custody/"
                "fac-blind-comparator-dual-doi-20260803-r1"
            ),
            "scheme": "url",
            "relation_type": "issupplementedby",
        },
    ]
    return {
        "version_suffix": version,
        "description_html": description,
        "cross_links": links,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--github-commit", required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    base.verify_github_commit(args.github_commit)
    if not OUTPUT.is_dir():
        raise RuntimeError(f"Payload output is absent: {OUTPUT}")
    generated_names = (
        "methodology_upload_manifest.json",
        "replication_upload_manifest.json",
        "release_spec.json",
        "RELEASE_SPEC_BUILD_VALIDATION.json",
    )
    existing = [name for name in generated_names if (OUTPUT / name).exists()]
    if existing:
        raise RuntimeError(f"Release-spec outputs already exist: {existing}")
    payload_validation = json.loads(
        (OUTPUT / "PAYLOAD_BUILD_VALIDATION.json").read_text(encoding="utf-8")
    )
    if payload_validation.get("status") != "PASS_READ_ONLY_DUAL_DOI_PAYLOAD_BUILD":
        raise RuntimeError("Payload build validation is not PASS")

    dual_rows = load_fac_rows()
    dual_rows.extend(
        (
            upload_row(
                SHARED_NAME,
                OUTPUT / SHARED_NAME,
                "privacy-clean append-only shared decision revision reversal logbook",
                dual=True,
                supersession="APPEND_ONLY_471_RECORD_SNAPSHOT",
            ),
            upload_row(
                INDEX_NAME,
                OUTPUT / INDEX_NAME,
                "privacy-clean public provenance manifest and source-to-public binding",
                dual=True,
                supersession="SUPERSEDES_PRIOR_RELEASE_INDEX_WITHOUT_ERASING_IT",
            ),
            upload_row(
                ARCHIVE_MAPPING_NAME,
                OUTPUT / ARCHIVE_MAPPING_NAME,
                "privacy-clean archive provenance mapping decision revision error transport",
                dual=True,
                supersession="FIRST_FAC_BLIND_COMPARATOR_ARCHIVE_MAPPING",
            ),
        )
    )
    dual_rows.sort(key=lambda row: row["name"])
    methodology_rows = list(dual_rows)
    methodology_rows.extend(
        (
            upload_row(
                RETENTION_ARCHIVE_NAME,
                OUTPUT / RETENTION_ARCHIVE_NAME,
                "retained predecessor companion archive",
                dual=False,
                supersession=(
                    "ORGANIZES_EXACT_PREDECESSOR_BYTES_WITH_IMMUTABLE_VERSION_LINKAGE"
                ),
            ),
            upload_row(
                RETENTION_MANIFEST_NAME,
                OUTPUT / RETENTION_MANIFEST_NAME,
                "retained predecessor companion index",
                dual=False,
                supersession=(
                    "DIRECT_INDEX_FOR_EXACT_PREDECESSOR_BYTES_IN_COMPANION_ARCHIVE"
                ),
            ),
        )
    )
    methodology_rows.sort(key=lambda row: row["name"])
    target_rows = {
        "methodology": methodology_rows,
        "replication": dual_rows,
    }

    manifest_guards: dict[str, dict[str, Any]] = {}
    for key, rows in target_rows.items():
        manifest_guards[key] = base.write_manifest(
            OUTPUT / f"{key}_upload_manifest.json", rows
        )

    with base.make_session() as session:
        guards = {
            key: base.predecessor_guard(session, key, registry)
            for key, registry in TARGETS.items()
        }

    policies: dict[str, dict[str, Any]] = {}
    final_counts: dict[str, int] = {}
    for key, rows in target_rows.items():
        old_names = {row["name"] for row in guards[key]["files"]}
        new_names = {row["name"] for row in rows}
        collisions = sorted(old_names & new_names)
        if key == "methodology":
            removals = set(RETENTION_NAMES)
            if not removals.issubset(old_names - new_names):
                raise RuntimeError("Methodology retention set is not predecessor-only")
            policies[key] = {
                "mode": "add-replace-remove-named",
                "replace_names": collisions,
                "remove_names": sorted(removals),
                "preservation_transport": {
                    "archive_name": RETENTION_ARCHIVE_NAME,
                    "manifest_name": RETENTION_MANIFEST_NAME,
                    "inner_manifest_name": RETENTION_INNER_MANIFEST,
                },
            }
            final_counts[key] = len(old_names - removals - set(collisions)) + len(new_names)
        else:
            if not collisions:
                raise RuntimeError("Replication has no explicit replacement collisions")
            policies[key] = {
                "mode": "add-or-replace-named",
                "replace_names": collisions,
            }
            final_counts[key] = len(old_names - set(collisions)) + len(new_names)
    if final_counts != {"methodology": 99, "replication": 64}:
        raise RuntimeError(f"Successor file-count preview changed: {final_counts}")

    targets: dict[str, Any] = {}
    for key in TARGETS:
        targets[key] = {
            "predecessor_guard": guards[key],
            "manifest_path": f"{key}_upload_manifest.json",
            "manifest_guard": manifest_guards[key],
            "file_policy": policies[key],
            "metadata_append": metadata_append(key, args.github_commit),
        }
    spec = {
        "schema": base.SCHEMA,
        "release_id": RELEASE_ID,
        "publication_date": PUBLICATION_DATE,
        "github_commit": args.github_commit,
        "safe_publish_order": list(SAFE_PUBLISH_ORDER),
        "control": {
            "path": base.path_for_manifest(base.CONTROL_PATH, OUTPUT),
            "bytes": base.CONTROL_BYTES,
            "sha256": base.CONTROL_SHA256,
        },
        "targets": targets,
    }
    spec_path = OUTPUT / "release_spec.json"
    spec_path.write_text(
        json.dumps(spec, ensure_ascii=True, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    validation = {
        "status": "PASS_READ_ONLY_DUAL_DOI_RELEASE_SPEC",
        "errors": [],
        "release_id": RELEASE_ID,
        "github_commit": args.github_commit,
        "release_spec": {
            "path": spec_path.name,
            "bytes": spec_path.stat().st_size,
            "sha256": base.sha256_path(spec_path),
        },
        "targets": {
            key: {
                "concept_doi": TARGETS[key]["concept_doi"],
                "predecessor_record": TARGETS[key]["record_id"],
                "predecessor_files": guards[key]["file_count"],
                "upload_manifest_files": len(target_rows[key]),
                "replacement_files": len(policies[key]["replace_names"]),
                "removed_direct_files": len(policies[key].get("remove_names", [])),
                "successor_files": final_counts[key],
                "manifest_bytes": manifest_guards[key]["bytes"],
                "manifest_sha256": manifest_guards[key]["sha256"],
            }
            for key in TARGETS
        },
        "dual_doi_rows": len(dual_rows),
        "dual_payload_identical": True,
        "fac_direct_files_per_record": 19,
        "fac_direct_provenance_surfaces_per_record": 3,
        "zenodo_mutation_performed": False,
        "draft_created": False,
    }
    (OUTPUT / "RELEASE_SPEC_BUILD_VALIDATION.json").write_text(
        json.dumps(validation, ensure_ascii=True, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps(validation, ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
