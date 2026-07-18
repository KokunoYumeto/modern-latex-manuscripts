#!/usr/bin/env python3
"""Validate and hash the Romance manager control plane.

The SHA manifest intentionally excludes itself: a file cannot contain a stable
hash of its own final bytes. The preserved v1 tree remains in the manifest,
while v2 is the only canonical cohort topology.
"""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
README = HERE / "ROMANCE_MANAGER_README_20260717.md"
LOCATION_REGISTER = HERE / "WORK_CORPUS_LOCATION_REGISTER_v1.csv"
ROOT_INVENTORY = HERE / "DISK_WORK_ROOT_INVENTORY_v1.csv"
TREE_V1 = HERE / "ROMANCE_FAMILY_COHORT_TREE_v1.json"
TREE_V2 = HERE / "ROMANCE_FAMILY_COHORT_TREE_v2.json"
EVIDENCE_GRAPH = HERE / "ROMANCE_MANAGER_EVIDENCE_GRAPH_v1.json"
VALIDATION = HERE / "ROMANCE_MANAGER_CONTROL_VALIDATION_20260717.json"
SHA_MANIFEST = HERE / "ROMANCE_MANAGER_CONTROL_SHA256SUMS.csv"

EXPECTED_COHORT_IDS = [
    "C-ES-STD",
    "C-FR-STD",
    "C-PT-STD",
    "C-GL-STD",
    "C-CA-STD",
    "C-IT-STD",
    "C-RO-STD",
    "C-RM-RG",
    "C-RM-ID",
]

EXPECTED_INVENTORY_COUNTS = {
    "public_source_work": 15,
    "public_reader_work": 15,
    "papors_project_root": 55,
    "other_pc_language_body_package": 20,
}

# This is an evidence snapshot, not a monitor. A runtime wall-clock value made
# the validation JSON and the manifest row that hashes it change on every
# replay. Keep the declared control-snapshot timestamp deterministic; a later
# control revision must change this constant explicitly.
CONTROL_SNAPSHOT_TIMESTAMP = "2026-07-17T00:00:00+02:00"

# The manifest hashes every manager-control input/output that the earlier
# design covered, plus the canonical v2 tree and this reproducible validator.
# SHA_MANIFEST itself is necessarily excluded.
MANAGED_ARTIFACTS = [
    "ROMANCE_MANAGER_README_20260717.md",
    "WORK_CORPUS_LOCATION_REGISTER_v1.csv",
    "DISK_WORK_ROOT_INVENTORY_v1.csv",
    "ROMANCE_FAMILY_COHORT_TREE_v1.json",
    "ROMANCE_FAMILY_COHORT_TREE_v2.json",
    "ROMANCE_MANAGER_EVIDENCE_GRAPH_v1.json",
    "validate_manager_control_v2.py",
    "ROMANCE_MANAGER_CONTROL_VALIDATION_20260717.json",
    "NOETHER_FR_ES_RECOVERY_AUDIT_20260717.md",
]


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def root_leaf_ids(tree: dict) -> list[str]:
    leaves: list[str] = []
    for branch in tree["root"]["children"]:
        for child in branch.get("children", []):
            if isinstance(child, str):
                leaves.append(child)
    return leaves


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    readme = README.read_text(encoding="utf-8")
    readme_normalized = " ".join(readme.split())
    locations = load_csv(LOCATION_REGISTER)
    inventory = load_csv(ROOT_INVENTORY)
    v1 = load_json(TREE_V1)
    v2 = load_json(TREE_V2)
    evidence = load_json(EVIDENCE_GRAPH)

    inventory_counts: dict[str, int] = {}
    for row in inventory:
        kind = row["kind"]
        inventory_counts[kind] = inventory_counts.get(kind, 0) + 1

    actual_ids = [row["cohort_id"] for row in v2["reader_cohorts"]]
    leaf_ids = root_leaf_ids(v2)
    actual_id_set = set(actual_ids)
    expected_id_set = set(EXPECTED_COHORT_IDS)

    cohort_by_id = {row["cohort_id"]: row for row in v2["reader_cohorts"]}
    semantic_checks = {
        "v2_schema_version_is_2_0": v2.get("schema_version") == "2.0",
        "v2_artifact_identity": v2.get("artifact")
        == "ROMANCE_FAMILY_COHORT_TREE_v2",
        "v2_declared_cohort_count_is_9": v2.get("cohort_count") == 9,
        "v2_declared_count_matches_rows": v2.get("cohort_count")
        == len(actual_ids),
        "v2_cohort_ids_unique": len(actual_ids) == len(actual_id_set),
        "v2_cohort_ids_exact": actual_id_set == expected_id_set,
        "v2_root_leaf_ids_unique": len(leaf_ids) == len(set(leaf_ids)),
        "v2_root_leaf_ids_match_cohorts": set(leaf_ids) == actual_id_set,
        "v2_manager_root_is_romance_manager": v2["root"].get("id")
        == "romance_manager",
        "romansh_cohort_split_exact": {
            "C-RM-RG",
            "C-RM-ID",
        }.issubset(actual_id_set)
        and cohort_by_id["C-RM-RG"].get("languages") == ["rm"]
        and cohort_by_id["C-RM-ID"].get("languages") == [],
        "v2_current_human_observations_zero": v2.get(
            "romansh_distinction", {}
        ).get("current_human_observations")
        == 0,
        "v2_scalar_readiness_disallowed": v2.get("dependence_policy", {}).get(
            "scalar_readiness_allowed"
        )
        is False,
        "v2_MII_result_does_not_feed_decisions": v2.get(
            "dependence_policy", {}
        ).get("MII_result_feeds_decisions")
        is False,
        "v2_supersedes_v1": v2.get("supersedes")
        == "ROMANCE_FAMILY_COHORT_TREE_v1",
        "v1_preserved_and_parseable": TREE_V1.is_file()
        and v1.get("schema_version") == "1.0",
        "readme_declares_v2_canonical": (
            "ROMANCE_FAMILY_COHORT_TREE_v2.json" in readme_normalized
            and "canonical nine-reader-cohort topology" in readme_normalized
        ),
        "readme_links_manager_id": "manager identifier is" in readme_normalized
        and "romance_manager" in readme_normalized,
        "readme_retains_v1_as_superseded": (
            "ROMANCE_FAMILY_COHORT_TREE_v1.json" in readme_normalized
            and "retained as superseded" in readme_normalized
        ),
        "readme_declares_zero_human_observations": (
            "This topology has zero human observations." in readme_normalized
        ),
    }

    missing_locations = [
        row["path"] for row in locations if not Path(row["path"]).exists()
    ]
    structural_checks = {
        "location_register_rows_are_29": len(locations) == 29,
        "location_register_paths_exist": not missing_locations,
        "disk_root_inventory_rows_are_105": len(inventory) == 105,
        "disk_root_inventory_counts_exact": inventory_counts
        == EXPECTED_INVENTORY_COUNTS,
        "evidence_graph_automatic_scalar_decision_false": evidence.get(
            "automatic_scalar_decision"
        )
        is False,
        "evidence_graph_community_certification_claim_false": evidence.get(
            "community_certification_claim"
        )
        is False,
    }

    passed = all(semantic_checks.values()) and all(structural_checks.values())
    result = {
        "schema_version": "2.0",
        "checked_at": CONTROL_SNAPSHOT_TIMESTAMP,
        "checked_at_semantics": "deterministic control-snapshot timestamp; not runtime wall clock",
        "pass": passed,
        "manager_identifier": "romance_manager",
        "canonical_family_tree": "ROMANCE_FAMILY_COHORT_TREE_v2.json",
        "superseded_family_tree_preserved": (
            "ROMANCE_FAMILY_COHORT_TREE_v1.json"
        ),
        "cohort_count_declared": v2.get("cohort_count"),
        "cohort_count_actual": len(actual_ids),
        "cohort_ids_expected": EXPECTED_COHORT_IDS,
        "cohort_ids_actual": actual_ids,
        "root_leaf_cohort_ids": leaf_ids,
        "current_human_observations": v2.get("romansh_distinction", {}).get(
            "current_human_observations"
        ),
        "semantic_checks": semantic_checks,
        "location_register_rows": len(locations),
        "location_register_missing_paths": len(missing_locations),
        "disk_root_inventory_rows": len(inventory),
        "disk_root_inventory_counts": inventory_counts,
        "structural_checks": structural_checks,
        "automatic_scalar_decision": evidence.get(
            "automatic_scalar_decision"
        ),
        "community_certification_claim": evidence.get(
            "community_certification_claim"
        ),
        "sha_manifest_design": {
            "self_hash_excluded": True,
            "managed_artifact_count": len(MANAGED_ARTIFACTS),
            "managed_artifacts": MANAGED_ARTIFACTS,
        },
    }

    VALIDATION.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    with SHA_MANIFEST.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["path", "sha256", "bytes"])
        writer.writeheader()
        for relative in MANAGED_ARTIFACTS:
            path = HERE / relative
            writer.writerow(
                {
                    "path": relative,
                    "sha256": sha256(path),
                    "bytes": path.stat().st_size,
                }
            )

    if not passed:
        failed = [
            name
            for checks in (semantic_checks, structural_checks)
            for name, value in checks.items()
            if not value
        ]
        raise SystemExit("manager control validation failed: " + ", ".join(failed))


if __name__ == "__main__":
    main()
