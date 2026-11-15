#!/usr/bin/env python3
"""Independent fail-closed validator for preregistration v002.

This file deliberately does not import the builder. It validates one file at a
time and streams large authority files to stay within the lane memory guard.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import stat
import sys
from pathlib import Path, PurePosixPath
from typing import Any

import jsonschema


DEFAULT_WORKSPACE = Path(r"C:\Users\user\Documents\interlanguage")
PACKAGE_REL = Path(
    "03_projects/language_management/slavic_interslavic/00_lane_control/"
    "marginal_intelligibility_20260811/preregistration_v002"
)
CORE_FILES = {
    "ISV_MI_PREREGISTRATION_V002.json",
    "ISV_MI_PREREGISTRATION_V002.schema.json",
    "INPUT_REPIN_AUDIT_V002.json",
    "STAGE0_DESIGN_V002.csv",
    "PROTOCOL_V002.md",
    "README.md",
    "HOSTILE_FIXTURES_V002.json",
}
SEALED_FILES = CORE_FILES | {
    "build_isv_mi_preregistration_v002.py",
    "validate_isv_mi_preregistration_v002.py",
    "test_isv_mi_preregistration_v002_hostile.py",
    "verify_isv_mi_preregistration_v002_reproducibility.py",
    "CONSTRUCTION_HISTORY_V002.jsonl",
    "VALIDATION_RECEIPT_V002.json",
    "HOSTILE_RECEIPT_V002.json",
    "REPRODUCIBILITY_RECEIPT_V002.json",
    "PACKAGE_MANIFEST_V002.json",
}
SHA_RE = re.compile(r"^[0-9A-F]{64}$")


class ValidationError(RuntimeError):
    pass


def strict_load_bytes(raw: bytes, label: str) -> Any:
    def reject(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        out: dict[str, Any] = {}
        for key, value in pairs:
            if key in out:
                raise ValidationError(f"duplicate JSON key {key!r} in {label}")
            out[key] = value
        return out

    try:
        return json.loads(raw.decode("utf-8"), object_pairs_hook=reject)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValidationError(f"invalid UTF-8 JSON in {label}: {exc}") from exc


def strict_load(path: Path) -> Any:
    return strict_load_bytes(path.read_bytes(), str(path))


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest().upper()


def ensure_inside(workspace: Path, rel: str) -> Path:
    pp = PurePosixPath(rel)
    if pp.is_absolute() or ".." in pp.parts or not pp.parts:
        raise ValidationError(f"unsafe workspace-relative path: {rel!r}")
    candidate = workspace.joinpath(*pp.parts)
    resolved = candidate.resolve(strict=True)
    try:
        resolved.relative_to(workspace.resolve(strict=True))
    except ValueError as exc:
        raise ValidationError(f"path escapes workspace: {rel}") from exc
    return resolved


def is_reparse(path: Path) -> bool:
    if path.is_symlink():
        return True
    try:
        attrs = path.stat(follow_symlinks=False).st_file_attributes
    except (AttributeError, OSError):
        return False
    return bool(attrs & stat.FILE_ATTRIBUTE_REPARSE_POINT)


def reject_reparse_chain(workspace: Path, path: Path) -> None:
    ws = workspace.resolve(strict=True)
    current = path
    while True:
        if is_reparse(current):
            raise ValidationError(f"reparse/symlink path rejected: {current}")
        if current.resolve(strict=True) == ws:
            break
        parent = current.parent
        if parent == current:
            raise ValidationError(f"could not reach workspace root from {path}")
        current = parent


def verify_pin(workspace: Path, pin: dict[str, Any]) -> int:
    required = {"pin_id", "role", "pin_kind", "workspace_relative_path", "expected_bytes", "expected_sha256", "acceptance_state"}
    if not required.issubset(pin):
        raise ValidationError(f"pin missing required keys: {pin.get('pin_id')}")
    if not SHA_RE.fullmatch(pin["expected_sha256"]):
        raise ValidationError(f"bad SHA format {pin['pin_id']}")
    path = ensure_inside(workspace, pin["workspace_relative_path"])
    if not path.is_file():
        raise ValidationError(f"pin is not a file: {path}")
    reject_reparse_chain(workspace, path)
    kind = pin["pin_kind"]
    if kind == "whole_file":
        observed_bytes = path.stat().st_size
        observed_sha = sha256_file(path)
    elif kind in {"jsonl_prefix_through_decision_id", "jsonl_row_utf8_no_eol"}:
        loc = pin.get("locator")
        if not isinstance(loc, dict):
            raise ValidationError(f"missing locator for {pin['pin_id']}")
        raw_lines = path.read_bytes().splitlines(keepends=True)
        idx = int(loc["line_number"]) - 1
        if idx < 0 or idx >= len(raw_lines):
            raise ValidationError(f"line locator out of range for {pin['pin_id']}")
        line_no_eol = raw_lines[idx].rstrip(b"\r\n")
        obj = strict_load_bytes(line_no_eol, f"{path}:line{idx + 1}")
        if obj.get("decision_id") != loc["decision_id"]:
            raise ValidationError(f"decision ID locator mismatch for {pin['pin_id']}")
        payload = b"".join(raw_lines[: idx + 1]) if kind.startswith("jsonl_prefix") else line_no_eol
        observed_bytes = len(payload)
        observed_sha = hashlib.sha256(payload).hexdigest().upper()
    else:
        raise ValidationError(f"unknown pin kind {kind}")
    if observed_bytes != pin["expected_bytes"] or observed_sha != pin["expected_sha256"]:
        raise ValidationError(
            f"pin mismatch {pin['pin_id']}: observed {observed_bytes}/{observed_sha}; "
            f"expected {pin['expected_bytes']}/{pin['expected_sha256']}"
        )
    return 4


def validate_dag(workspace: Path, protocol: dict[str, Any]) -> int:
    model = protocol["evidence_model"]
    path = ensure_inside(workspace, model["workspace_relative_path"])
    dag = strict_load(path)
    nodes = dag.get("nodes")
    edges = dag.get("edges")
    if not isinstance(nodes, list) or not isinstance(edges, list):
        raise ValidationError("DAG lacks nodes/edges lists")
    node_ids = [row.get("id") for row in nodes]
    if any(not isinstance(value, str) for value in node_ids) or len(node_ids) != len(set(node_ids)):
        raise ValidationError("DAG node IDs missing or duplicated")
    adj = {node: [] for node in node_ids}
    indegree = {node: 0 for node in node_ids}
    edge_ids: set[str] = set()
    for edge in edges:
        edge_id = edge.get("id")
        src, dst = edge.get("from"), edge.get("to")
        if not isinstance(edge_id, str) or edge_id in edge_ids:
            raise ValidationError("DAG edge ID missing or duplicated")
        edge_ids.add(edge_id)
        if src not in adj or dst not in adj:
            raise ValidationError(f"DAG edge endpoint missing: {edge_id}")
        adj[src].append(dst)
        indegree[dst] += 1
    queue = sorted(node for node, degree in indegree.items() if degree == 0)
    visited = 0
    while queue:
        node = queue.pop(0)
        visited += 1
        for dst in sorted(adj[node]):
            indegree[dst] -= 1
            if indegree[dst] == 0:
                queue.append(dst)
                queue.sort()
    if visited != len(node_ids):
        raise ValidationError("cyclic evidence DAG rejected")
    declared_order = dag.get("topological_order")
    if not isinstance(declared_order, list) or set(declared_order) != set(node_ids) or len(declared_order) != len(node_ids):
        raise ValidationError("declared topological order is not a full node permutation")
    positions = {node: i for i, node in enumerate(declared_order)}
    for edge in edges:
        if positions[edge["from"]] >= positions[edge["to"]]:
            raise ValidationError(f"declared topological order violates {edge['id']}")
    return len(nodes) + len(edges) + 2


def validate_tree(workspace: Path, protocol: dict[str, Any]) -> int:
    audit = strict_load(workspace / PACKAGE_REL / "INPUT_REPIN_AUDIT_V002.json")
    pin = next(row for row in audit["pins"] if row["pin_id"] == protocol["family_tree"]["tree_pin_id"])
    tree = strict_load(ensure_inside(workspace, pin["workspace_relative_path"]))
    branches = tree.get("macrobranches")
    ids = [row.get("id") for row in branches]
    expected = ["east_slavic", "west_slavic", "south_slavic"]
    if ids != expected:
        raise ValidationError(f"family-tree macrobranch mismatch: {ids}")
    if not tree.get("tree_contract", {}).get("macrobranches_symmetric"):
        raise ValidationError("family tree is not declared symmetric")
    if any(len(row.get("official_groups", [])) != 2 for row in branches):
        raise ValidationError("each macrobranch must expose two official group frames")
    return 6


def validate_protocol_semantics(protocol: dict[str, Any], audit: dict[str, Any]) -> int:
    checks = 0
    if protocol["status"] != "fail_closed_not_launch_ready_no_human_validation":
        raise ValidationError("false readiness status")
    checks += 1
    if protocol["authority_cutoff"]["substantive_decision_prefix_through"] != "SLISV-20260812-070":
        raise ValidationError("decision cutoff drift")
    if protocol["authority_cutoff"]["post_cutoff_corrections_consumed"] != ["SLISV-20260812-072", "SLISV-20260812-073"]:
        raise ValidationError("append-only correction chain missing")
    checks += 2
    serial = protocol["authority_cutoff"]["decision_068_serializations"]
    if serial["standalone_pretty_json"] != {"pin_id": "PIN-DECISION-068", "observed_bytes": 7675, "sha256": "D450598D59F20AD5A526F6D7437DD1921BC24CFA4DE2D2C518BB59E02C345BB1"}:
        raise ValidationError("decision-068 standalone serialization mismatch")
    if serial["compact_log_row_utf8_no_eol"] != {"pin_id": "PIN-DECISION-068-ROW", "observed_bytes": 7028, "sha256": "6C02D0A582E50A99DE678FEA6AFF0A1555729925BE7EEE19EBC1BBF7442DE5FF"}:
        raise ValidationError("decision-068 compact-row serialization mismatch")
    if serial["superseded_invalid_hash"] != "6C02D0A5F48BFD8595EC01C6F9939EC561D6B3707A73336EEB48330CD18E1C11" or serial["superseded_invalid_standalone_bytes"] != 10216:
        raise ValidationError("superseded provenance values not retained")
    checks += 3
    german = protocol["current_state"]["german_authority"]
    if german["pointer_id"] != "NOETH-DE-AUTH-v047-20260808" or german["resolved_authority_id"] != "NOETH-DE-ED-0011" or german["canonical_claim"] is not False:
        raise ValidationError("German authority identity/claim boundary drift")
    checks += 1
    sem = protocol["current_state"]["semantic_boundary_review"]
    packages = sem["packages"]
    if [row["reviewed"] for row in packages] != [54, 100, 100, 100, 100]:
        raise ValidationError("semantic review package coverage drift")
    if [row["accepted_preserve_candidates"] for row in packages] != [50, 59, 53, 89, 83]:
        raise ValidationError("semantic review acceptance counts drift")
    if [row["held_records_preserved"] for row in packages] != [4, 41, 47, 11, 17]:
        raise ValidationError("semantic review hold counts drift")
    if (sem["reviewed_total"], sem["accepted_preserve_candidates_total"], sem["raw_hold_records_preserved_total"], sem["unreviewed_semantic_gap_records"]) != (454, 334, 120, 2737):
        raise ValidationError("semantic cumulative counts drift")
    if sem["precision_extrapolation_authorized"] is not False:
        raise ValidationError("precision extrapolation falsely authorized")
    checks += 5
    lj = protocol["current_state"]["item_and_morphology"]["lj_nj"]
    if lj["package_state"] != "HOLD_acceptance_withheld_at_authority_cutoff" or lj["held"] != 9700:
        raise ValidationError("lj/nj hold lost")
    human = protocol["current_state"]["human_evidence"]
    if any(value != 0 for value in human.values()):
        raise ValidationError("fabricated human evidence")
    community = protocol["current_state"]["community_review"]
    for key in ("responses", "approvals", "west_authored_arms", "south_authored_arms", "Jan_or_community_returns"):
        if community[key] != 0:
            raise ValidationError(f"fabricated community state: {key}")
    if community["outreach_authorized"] or community["outreach_performed"]:
        raise ValidationError("outreach falsely authorized or performed")
    checks += 8
    slots = protocol["stage0_design"]["leaf_sampling"]["slots"]
    if len(slots) != 6:
        raise ValidationError("Stage-0 must have six leaf slots")
    branch_counts = {branch: 0 for branch in ("east_slavic", "west_slavic", "south_slavic")}
    for slot in slots:
        branch_counts[slot["macrobranch"]] += 1
        if slot["selected_leaf_id"] is not None or slot["provisional_analyzable_readers"] != 12:
            raise ValidationError("leaf selection or provisional target drift")
    if branch_counts != {"east_slavic": 2, "west_slavic": 2, "south_slavic": 2}:
        raise ValidationError(f"missing cohort branch: {branch_counts}")
    if protocol["stage0_design"]["leaf_sampling"]["provisional_total_analyzable_readers"] != 72:
        raise ValidationError("provisional total must be 72")
    if protocol["stage0_design"]["leaf_sampling"]["actual_analyzable_readers"] != 0:
        raise ValidationError("actual participant count must be zero")
    checks += 10
    arms = protocol["stage0_design"]["arms"]
    if arms["declared_role_count"] != 5 or len(arms["roles"]) != 5:
        raise ValidationError("five arm roles required")
    if not arms["byte_identical_collapse"]["required"] or arms["byte_identical_collapse"]["observed_collapses"] is not None:
        raise ValidationError("byte-identical collapse contract drift")
    if any(row["frozen_bytes"] or row["sha256"] is not None for row in arms["roles"]):
        raise ValidationError("unfrozen arm falsely materialized")
    checks += 4
    passage = protocol["stage0_design"]["passages"]
    if len(passage["types"]) != 3 or passage["frozen_passage_count"] != 0 or not passage["whole_passage_contract"]["tokenwise_mosaic_forbidden"]:
        raise ValidationError("passage contract drift")
    outcomes = protocol["stage0_design"]["outcome_vector"]
    if outcomes["primary_scalar"] is not None or outcomes["auto_choice_from_scalar"] is not False or len(outcomes["domains"]) != 5:
        raise ValidationError("outcome vector/scalar boundary drift")
    missing = protocol["stage0_design"]["missing_data"]
    if missing != {"missing_equals": "unknown", "impute_from_relative_language": False, "encode_unknown_as_zero": False, "treat_missing_as_pass": False, "not_estimable_rule": "Serialize not_estimable with exact reason whenever a frozen minimum, assignment, review, answer-key, or model gate fails.", "outcome_imputation": False}:
        raise ValidationError("missing-data policy drift")
    checks += 7
    gates = protocol["launch_gates"]
    gate_ids = [row["gate_id"] for row in gates]
    if len(gate_ids) != len(set(gate_ids)):
        raise ValidationError("duplicate launch gate")
    blocked = {row["criterion"] for row in gates if row["state"] == "blocked"}
    required_blocked = {
        "six_exact_leaf_identities_frozen_two_per_macrobranch",
        "simulation_justifies_analyzable_n_and_recruitment_oversample",
        "ethics_consent_privacy_retention_withdrawal_frozen",
        "five_arm_surfaces_frozen_and_byte_identical_roles_collapsed",
        "coherent_same_information_passages_questions_and_answer_keys_frozen",
        "qualified_West_and_South_surfaces_and_balanced_independent_review_complete",
        "native_language_controls_authored_reviewed_and_frozen",
        "randomization_seed_assignment_and_blinding_commitments_frozen",
        "harm_false_friend_multiplicity_interval_and_exclusion_rules_frozen",
        "lj_nj_package_receipt_and_tree_custody_hold_resolved_and_consumed",
        "all_semantic_holds_and_unreviewed_gap_population_resolved_for_included_passages",
    }
    if not required_blocked.issubset(blocked):
        raise ValidationError(f"launch blockers missing: {sorted(required_blocked - blocked)}")
    if next(row for row in gates if row["criterion"] == "Jan_or_community_approval")["state"] != "not_a_launch_gate":
        raise ValidationError("Jan/community approval incorrectly made launch gate")
    checks += len(gates) + len(required_blocked)
    claim = protocol["claim_boundary"]
    if any(claim[key] for key in ("reader_or_translation_bytes_mutated", "participant_launch_performed", "outreach_performed", "publication_handoff_ready")):
        raise ValidationError("false action/readiness claim")
    prohibited = set(claim["prohibited"])
    for term in ("participant_ready", "canonical_Interslavic", "maximally_intelligible", "community_approved", "Jan_van_Steenbergen_approved"):
        if term not in prohibited:
            raise ValidationError(f"missing prohibited claim {term}")
    checks += 9
    if audit["status"] != "exact_pins_replayed_with_append_only_hash_and_byte_count_corrections_consumed":
        raise ValidationError("repin audit correction state drift")
    if audit["counts"]["pins"] != len(audit["pins"]) or audit["counts"]["pins"] != protocol["input_repin_audit"]["pin_count"]:
        raise ValidationError("repin count mismatch")
    if len({row["pin_id"] for row in audit["pins"]}) != len(audit["pins"]):
        raise ValidationError("duplicate pin IDs")
    if audit["adverse_provenance"][0]["state"] != "resolved_append_only_by_SLISV-20260812-073_and_SLISV-DIFF-0097":
        raise ValidationError("append-only provenance correction missing")
    return checks + 4


def validate_csv(root: Path, protocol: dict[str, Any]) -> int:
    with (root / "STAGE0_DESIGN_V002.csv").open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    expected = 6 + 5 + 3 + len(protocol["launch_gates"])
    if len(rows) != expected:
        raise ValidationError(f"CSV row count mismatch: {len(rows)} != {expected}")
    if len({(row["row_type"], row["stable_id"]) for row in rows}) != len(rows):
        raise ValidationError("duplicate CSV row identity")
    return expected + 1


def validate_manifest(root: Path, require_manifest: bool, exact_tree: bool) -> int:
    path = root / "PACKAGE_MANIFEST_V002.json"
    if not path.exists():
        if require_manifest:
            raise ValidationError("manifest required but missing")
        return 0
    manifest = strict_load(path)
    if manifest.get("status") != "sealed_internal_fail_closed_not_launch_ready":
        raise ValidationError("manifest status drift")
    entries = manifest.get("files")
    if not isinstance(entries, list):
        raise ValidationError("manifest files missing")
    names = [row.get("path") for row in entries]
    if len(names) != len(set(names)):
        raise ValidationError("duplicate manifest path")
    expected_names = sorted(SEALED_FILES - {"PACKAGE_MANIFEST_V002.json"})
    if sorted(names) != expected_names:
        raise ValidationError(f"manifest declared tree mismatch: {sorted(set(names) ^ set(expected_names))}")
    for row in entries:
        member = root / row["path"]
        if not member.is_file() or is_reparse(member):
            raise ValidationError(f"manifest member missing/reparse: {row['path']}")
        if member.stat().st_size != row["bytes"] or sha256_file(member) != row["sha256"]:
            raise ValidationError(f"manifest member drift: {row['path']}")
    if exact_tree:
        physical: set[str] = set()
        for item in root.iterdir():
            if item.name == "__pycache__":
                raise ValidationError("__pycache__ rejected")
            if is_reparse(item):
                raise ValidationError(f"reparse package member rejected: {item.name}")
            if not item.is_file():
                raise ValidationError(f"unexpected non-file package member: {item.name}")
            physical.add(item.name)
        if physical != SEALED_FILES:
            raise ValidationError(f"exact tree mismatch: {sorted(physical ^ SEALED_FILES)}")
    return len(entries) * 3 + (1 if exact_tree else 0)


def validate(
    workspace: Path,
    root: Path,
    require_manifest: bool = False,
    exact_tree: bool = False,
) -> dict[str, Any]:
    workspace = workspace.resolve(strict=True)
    root = root.resolve(strict=True)
    try:
        root.relative_to(workspace)
    except ValueError as exc:
        raise ValidationError("package root outside workspace") from exc
    reject_reparse_chain(workspace, root)
    for name in CORE_FILES:
        member = root / name
        if not member.is_file() or is_reparse(member):
            raise ValidationError(f"missing/reparse core member: {name}")
    protocol = strict_load(root / "ISV_MI_PREREGISTRATION_V002.json")
    schema = strict_load(root / "ISV_MI_PREREGISTRATION_V002.schema.json")
    audit = strict_load(root / "INPUT_REPIN_AUDIT_V002.json")
    hostile_meta = strict_load(root / "HOSTILE_FIXTURES_V002.json")
    jsonschema.Draft202012Validator.check_schema(schema)
    errors = sorted(jsonschema.Draft202012Validator(schema).iter_errors(protocol), key=lambda err: list(err.path))
    if errors:
        raise ValidationError("schema failure: " + "; ".join(error.message for error in errors[:5]))
    checks = 4
    if hostile_meta.get("canonical_artifacts_mutated") is not False or len(hostile_meta.get("cases", [])) != 9:
        raise ValidationError("hostile fixture declaration drift")
    checks += 2
    for pin in audit.get("pins", []):
        checks += verify_pin(workspace, pin)
    checks += validate_protocol_semantics(protocol, audit)
    checks += validate_dag(workspace, protocol)
    checks += validate_tree(workspace, protocol)
    checks += validate_csv(root, protocol)
    checks += validate_manifest(root, require_manifest=require_manifest, exact_tree=exact_tree)
    return {
        "status": "PASS",
        "checks": checks,
        "input_pins": len(audit["pins"]),
        "launch_gate_counts": {state: sum(row["state"] == state for row in protocol["launch_gates"]) for state in ("pass", "blocked", "not_a_launch_gate")},
        "decision_cutoff": "SLISV-20260812-070",
        "corrections_consumed": ["SLISV-20260812-072", "SLISV-20260812-073"],
        "reviewed_semantic_records": 454,
        "accepted_preserve_candidates": 334,
        "raw_hold_records_preserved": 120,
        "unreviewed_semantic_gap_records": 2737,
        "participants": 0,
        "west_experimental_surfaces": 0,
        "south_experimental_surfaces": 0,
        "native_controls": 0,
        "outreach_authorized": False,
        "package_root": root.as_posix(),
        "manifest_checked": (root / "PACKAGE_MANIFEST_V002.json").exists(),
        "exact_tree_checked": exact_tree,
        "writes_performed": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace-root", type=Path, default=DEFAULT_WORKSPACE)
    parser.add_argument("--package-root", type=Path)
    parser.add_argument("--require-manifest", action="store_true")
    parser.add_argument("--exact-tree", action="store_true")
    args = parser.parse_args()
    root = args.package_root or args.workspace_root / PACKAGE_REL
    try:
        result = validate(args.workspace_root, root, args.require_manifest, args.exact_tree)
    except Exception as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False, sort_keys=True))
        return 1
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
