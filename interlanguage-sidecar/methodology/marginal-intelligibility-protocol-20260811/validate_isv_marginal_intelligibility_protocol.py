#!/usr/bin/env python3
"""Strict, no-write-by-default validator for the Interslavic MI pilot design."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

HERE = Path(__file__).resolve().parent
TREE = HERE / "ISV_SYMMETRIC_FAMILY_COHORT_TREE.json"
TREE_SCHEMA = HERE / "ISV_SYMMETRIC_FAMILY_COHORT_TREE.schema.json"
PROTOCOL = HERE / "ISV_MARGINAL_INTELLIGIBILITY_PILOT_PROTOCOL.json"
PROTOCOL_SCHEMA = HERE / "ISV_MARGINAL_INTELLIGIBILITY_PILOT_PROTOCOL.schema.json"
RECEIPT = HERE / "ISV_MARGINAL_INTELLIGIBILITY_PILOT_PROTOCOL.validation.json"

EXPECTED_BRANCHES = ["east_slavic", "west_slavic", "south_slavic"]
EXPECTED_OFFICIAL_GROUPS_BY_BRANCH = {
    "east_slavic": ["official_group_russian", "official_group_ukrainian_belarusian"],
    "west_slavic": ["official_group_polish", "official_group_czech_slovak"],
    "south_slavic": ["official_group_slovene_bcs", "official_group_bulgarian_macedonian"],
}
EXPECTED_OFFICIAL_VOTE_GROUPS = [
    "Russian",
    "Ukrainian_and_Belarusian",
    "Polish",
    "Czech_and_Slovak",
    "Slovene_and_Serbian_Croatian_Bosnian",
    "Bulgarian_and_Macedonian",
]
EXPECTED_SENTINELS = {"rusyn", "kashubian", "upper_sorbian", "lower_sorbian"}
EXPECTED_ARMS = {
    "current_v018",
    "official_isv",
    "dominant_east_baseline",
    "branch_balanced_candidate",
    "native_language_control",
}
EXPECTED_TASK_LEVELS = {
    "lexeme_sense_morphology",
    "sentence_proof_function",
    "passage_global_integration",
}
EXPECTED_OUTCOMES = {
    "lexeme_accuracy",
    "sentence_comprehension_accuracy",
    "passage_comprehension_score",
    "false_friend_error",
    "correct_trial_response_time",
    "confidence",
    "proof_step_order",
    "terminology_consistency_error",
    "blinded_free_paraphrase",
}
PROHIBITED_CURRENT_CLAIMS = {
    "canonical",
    "certified",
    "community_approved",
    "maximally_intelligible",
    "pan_Slavic_validated",
    "source_faithful_successor_complete",
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key {key!r}")
        result[key] = value
    return result


def load_unique(path: Path):
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)


def schema_errors(instance, schema, label: str) -> list[str]:
    Draft202012Validator.check_schema(schema)
    errors = []
    for error in sorted(Draft202012Validator(schema).iter_errors(instance), key=lambda item: list(item.path)):
        path = "/".join(str(part) for part in error.path) or "$"
        errors.append(f"{label} schema {path}: {error.message}")
    return errors


def file_record(path: Path) -> dict:
    data = path.read_bytes()
    return {"path": path.as_posix(), "bytes": len(data), "sha256": sha256(data)}


def validate(tree: dict, protocol: dict, check_paths: bool = True) -> list[str]:
    errors: list[str] = []

    branches = tree.get("macrobranches", [])
    branch_ids = [branch.get("id") for branch in branches]
    if branch_ids != EXPECTED_BRANCHES:
        errors.append(f"tree macrobranch order/identity mismatch: {branch_ids}")
    if tree.get("tree_contract", {}).get("macrobranches_symmetric") is not True:
        errors.append("tree must declare symmetric macrobranches")
    if tree.get("tree_contract", {}).get("official_groups_per_macrobranch") != 2:
        errors.append("tree must declare exactly two official groups per macrobranch")
    if tree.get("tree_contract", {}).get("numeric_edge_lengths") is not None:
        errors.append("numeric edge lengths must remain null until separately justified")
    if tree.get("tree_contract", {}).get("empirical_outcome_weights") is not None:
        errors.append("empirical outcome weights must remain null before data/design freeze")
    if tree.get("tree_contract", {}).get("population_weights") is not None:
        errors.append("tree population weights must remain null")
    if tree.get("tree_contract", {}).get("cyrillic_interslavic_is_independent_leaf") is not False:
        errors.append("Cyrillic Interslavic must not be an independent leaf")

    leaf_ids = []
    sentinel_ids = set()
    for branch in branches:
        group_ids = [group.get("id") for group in branch.get("official_groups", [])]
        expected = EXPECTED_OFFICIAL_GROUPS_BY_BRANCH.get(branch.get("id"), [])
        if group_ids != expected:
            errors.append(f"official groups mismatch for {branch.get('id')}: {group_ids}")
        for group in branch.get("official_groups", []):
            for language in group.get("languages", []):
                leaf_ids.append(language.get("id"))
        for leaf in branch.get("protected_sentinel_leaves", []):
            leaf_ids.append(leaf.get("id"))
            sentinel_ids.add(leaf.get("id"))
    if len(leaf_ids) != len(set(leaf_ids)):
        errors.append("tree contains duplicate language/sentinel leaf IDs")
    if sentinel_ids != EXPECTED_SENTINELS:
        errors.append(f"protected sentinel set mismatch: {sorted(sentinel_ids)}")
    if "montenegrin" not in leaf_ids:
        errors.append("Montenegrin participant leaf must remain separately recorded")

    object_separation = protocol.get("object_separation", {})
    for object_id in ["typed_evidence_dag", "declared_family_cohort_tree", "governance_comparators"]:
        if object_separation.get(object_id, {}).get("may_define_human_intelligibility") is not False:
            errors.append(f"{object_id} must be prohibited from defining human intelligibility")
    empirical = object_separation.get("empirical_comprehension_outcomes", {})
    if empirical.get("current_state") != "not_collected":
        errors.append("empirical outcome state must remain not_collected")
    if "only permitted basis" not in empirical.get("role", ""):
        errors.append("empirical outcomes must remain the only permitted intelligibility basis")
    if object_separation.get("editorial_decision_ledger", {}).get("may_auto_promote_from_one_scalar") is not False:
        errors.append("editorial ledger must prohibit scalar auto-promotion")

    current = protocol.get("current_work_state", {})
    if current.get("human_response_records") != 0:
        errors.append("pre-recruitment protocol must report zero human responses")
    if current.get("accepted_external_or_community_reviews") != 0:
        errors.append("pre-recruitment protocol must report zero accepted external reviews")
    if current.get("canonical_marginal_intelligibility_successor") != "not built":
        errors.append("canonical successor state must remain not built")
    if current.get("german_canonical_claim") is not False:
        errors.append("German pointer canonical_claim must remain false")

    tree_ref = protocol.get("cohort_tree", {})
    if tree_ref.get("tree_id") != tree.get("record_id"):
        errors.append("protocol/tree stable ID mismatch")
    if check_paths:
        tree_path = Path(tree_ref.get("path", ""))
        if not tree_path.is_file():
            errors.append("protocol cohort-tree path is missing")
        else:
            observed = file_record(tree_path)
            if observed["bytes"] != tree_ref.get("bytes") or observed["sha256"] != tree_ref.get("sha256"):
                errors.append("protocol cohort-tree bytes/hash mismatch")

    comparators = {item.get("id"): item for item in protocol.get("governance_comparators", [])}
    required_comparators = {
        "official_six_vote_rule",
        "macrobranch_equal",
        "population_sensitivity",
        "minimum_leaf_and_macrobranch_vector",
    }
    if set(comparators) != required_comparators:
        errors.append(f"governance comparator set mismatch: {sorted(comparators)}")
    official = comparators.get("official_six_vote_rule", {})
    if official.get("groups") != EXPECTED_OFFICIAL_VOTE_GROUPS:
        errors.append("official six-vote group list was altered")
    if "no automatic promotion" not in official.get("decision_role", ""):
        errors.append("official voting comparator must prohibit automatic promotion")
    population = comparators.get("population_sensitivity", {})
    if population.get("type") != "sensitivity_only" or "never primary" not in population.get("decision_role", ""):
        errors.append("population comparator must remain non-primary sensitivity only")
    minimum = comparators.get("minimum_leaf_and_macrobranch_vector", {})
    if minimum.get("aggregation") != "none" or "cannot erase harm" not in minimum.get("decision_role", ""):
        errors.append("minimum-cohort vector must remain unaggregated and no-harm preserving")

    families = protocol.get("decision_family_plan", {}).get("families", [])
    if protocol.get("decision_family_plan", {}).get("family_count") != 12 or len(families) != 12:
        errors.append("decision-family frame must contain exactly 12 families")
    if [item.get("id") for item in families] != [f"MI-FAM-{i:02d}" for i in range(1, 13)]:
        errors.append("decision-family IDs/order mismatch")

    arm_ids = {arm.get("id") for arm in protocol.get("arms", [])}
    if arm_ids != EXPECTED_ARMS:
        errors.append(f"arm set mismatch or inadmissible arm present: {sorted(arm_ids)}")
    if "token_mosaic" in arm_ids:
        errors.append("token mosaic is not an admissible participant arm")
    task_ids = {task.get("id") for task in protocol.get("task_levels", [])}
    if task_ids != EXPECTED_TASK_LEVELS:
        errors.append(f"task-level set mismatch: {sorted(task_ids)}")
    passage = next((task for task in protocol.get("task_levels", []) if task.get("id") == "passage_global_integration"), {})
    if "No tokenwise best-word mosaic" not in passage.get("constraint", ""):
        errors.append("passage design must reject tokenwise mosaic arms")

    outcome_ids = {outcome.get("id") for outcome in protocol.get("outcomes", [])}
    if outcome_ids != EXPECTED_OUTCOMES:
        errors.append(f"outcome set mismatch: {sorted(outcome_ids)}")
    sampling = protocol.get("sampling_plan", {})
    if "not_started" not in sampling.get("ethics_and_privacy_state", ""):
        errors.append("ethics/privacy gate must remain visibly not started")
    if "at least two independently sampled leaf standards" not in sampling.get("macrobranch_launch_floor", ""):
        errors.append("macrobranch comparison floor is missing")
    if "never impute" not in sampling.get("small_cohort_rule", ""):
        errors.append("small-cohort no-imputation rule is missing")
    if sampling.get("optional_stopping")[:10] != "prohibited":
        errors.append("effect-based optional stopping must be prohibited")

    analysis = protocol.get("analysis_plan", {})
    if analysis.get("harm_margin") is not None or analysis.get("false_friend_margin") is not None:
        errors.append("unratified harm margins must remain null before calibration")
    if analysis.get("analysis_freeze_state") != "not_ready_for_recruitment":
        errors.append("analysis must remain not ready for recruitment")
    if "may not turn an unsampled leaf into observed evidence" not in analysis.get("partial_pooling_limit", ""):
        errors.append("partial-pooling missing-leaf prohibition is missing")

    claims = protocol.get("claim_scope", {})
    current_labels = set(claims.get("current_permitted_labels", []))
    if current_labels & PROHIBITED_CURRENT_CLAIMS:
        errors.append("a prohibited canonical/community claim appears in current permitted labels")
    if set(claims.get("prohibited_without_later_evidence", [])) != PROHIBITED_CURRENT_CLAIMS:
        errors.append("prohibited-claim set mismatch")
    if claims.get("external_validation_state") != "none":
        errors.append("external validation state must remain none")
    if claims.get("human_intelligibility_index_state") != "does_not_exist_yet":
        errors.append("human intelligibility index must remain nonexistent")

    gate_map = {gate.get("id"): gate for gate in protocol.get("hard_gates", [])}
    if set(gate_map) != {f"MI-GATE-{i:03d}" for i in range(1, 15)}:
        errors.append("hard-gate IDs must be exactly MI-GATE-001..014")
    if gate_map.get("MI-GATE-013", {}).get("state") != "open":
        errors.append("external/community-review gate must remain open")
    if gate_map.get("MI-GATE-014", {}).get("state") != "design_pass":
        errors.append("no-scalar-auto-promotion design gate must pass")

    if check_paths:
        for pin in protocol.get("authority_pins", []):
            path_text = pin.get("path")
            if not path_text:
                continue
            path = Path(path_text)
            if not path.is_file():
                errors.append(f"authority path missing: {path_text}")
                continue
            observed = file_record(path)
            if pin.get("bytes") != observed["bytes"] or pin.get("sha256") != observed["sha256"]:
                errors.append(f"authority pin mismatch: {pin.get('authority_id')}")
    live_web_pins = [pin for pin in protocol.get("authority_pins", []) if pin.get("url")]
    if len(live_web_pins) != 2 or any(pin.get("exact_saved_bytes") is not None for pin in live_web_pins):
        errors.append("live official web authorities must remain exactly two, visibly unsnapshotted at this stage")
    return errors


def run_adversarial(tree: dict, protocol: dict) -> list[dict]:
    cases = []

    def case(name, mutate):
        t = copy.deepcopy(tree)
        p = copy.deepcopy(protocol)
        mutate(t, p)
        failures = validate(t, p, check_paths=False)
        cases.append({"fixture": name, "expected": "reject", "observed": "reject" if failures else "accept", "failure_count": len(failures), "first_failure": failures[0] if failures else None})

    case("drop_west_official_group", lambda t, p: t["macrobranches"][1]["official_groups"].pop())
    case("invent_numeric_edge_lengths", lambda t, p: t["tree_contract"].__setitem__("numeric_edge_lengths", {"all": 1}))
    case("promote_cyrillic_to_language_leaf", lambda t, p: t["tree_contract"].__setitem__("cyrillic_interslavic_is_independent_leaf", True))
    case("erase_rusyn_sentinel", lambda t, p: t["macrobranches"][0].__setitem__("protected_sentinel_leaves", []))
    case("claim_human_responses_without_status_change", lambda t, p: p["current_work_state"].__setitem__("human_response_records", 1))
    case("make_D1_human_basis", lambda t, p: p["object_separation"]["empirical_comprehension_outcomes"].__setitem__("role", "D1 is the human intelligibility basis"))
    case("promote_population_to_primary", lambda t, p: p["governance_comparators"][2].__setitem__("decision_role", "primary result"))
    case("add_token_mosaic_arm", lambda t, p: p["arms"].append({"id": "token_mosaic"}))
    case("rewrite_official_vote_with_montenegrin", lambda t, p: p["governance_comparators"][0]["groups"].append("Montenegrin"))
    case("permit_canonical_claim_now", lambda t, p: p["claim_scope"]["current_permitted_labels"].append("canonical"))
    case("erase_no_imputation_rule", lambda t, p: p["sampling_plan"].__setitem__("small_cohort_rule", "pool with relatives"))
    case("mark_external_review_complete", lambda t, p: p["claim_scope"].__setitem__("external_validation_state", "complete"))
    return cases


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--write-receipt", action="store_true")
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args()

    tree_schema = load_unique(TREE_SCHEMA)
    protocol_schema = load_unique(PROTOCOL_SCHEMA)
    tree = load_unique(TREE)
    protocol = load_unique(PROTOCOL)
    failures = []
    failures.extend(schema_errors(tree, tree_schema, "tree"))
    failures.extend(schema_errors(protocol, protocol_schema, "protocol"))
    failures.extend(validate(tree, protocol, check_paths=True))
    adversarial = run_adversarial(tree, protocol) if args.self_test or args.write_receipt else []
    adversarial_failures = [item for item in adversarial if item["observed"] != item["expected"]]
    if adversarial_failures:
        failures.append(f"adversarial suite false accepts: {[item['fixture'] for item in adversarial_failures]}")

    receipt = {
        "schema": "slisv-isv-marginal-intelligibility-pilot-protocol-validation-v1",
        "status": "pass" if not failures else "fail",
        "classification": "protocol/control validation only; no human data, native certification, canonicalization, reader mutation, build, render, or publication claim",
        "files": {
            "tree": file_record(TREE),
            "tree_schema": file_record(TREE_SCHEMA),
            "protocol": file_record(PROTOCOL),
            "protocol_schema": file_record(PROTOCOL_SCHEMA),
            "validator": file_record(Path(__file__)),
        },
        "checks": {
            "duplicate_key_rejection_active": True,
            "draft_2020_12_executed": True,
            "authority_path_hashes_checked": True,
            "symmetric_three_branch_two_group_tree_checked": True,
            "small_and_transitional_sentinels_checked": True,
            "official_governance_empirical_outcome_separation_checked": True,
            "zero_human_and_zero_external_review_state_checked": True,
            "coherent_three_level_task_design_checked": True,
            "no_token_mosaic_arm_checked": True,
            "no_scalar_auto_promotion_checked": True,
            "adversarial_fixture_count": len(adversarial),
            "adversarial_false_accept_count": len(adversarial_failures),
        },
        "failure_count": len(failures),
        "failures": failures,
        "adversarial_results": adversarial,
        "writes_performed": [RECEIPT.as_posix()] if args.write_receipt else [],
        "human_response_records": 0,
        "external_review_returns": 0,
        "reader_or_release_files_modified": False,
        "continuation_cursor": protocol.get("continuation_cursor"),
    }
    archival_encoded = (json.dumps(receipt, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    stdout_encoded = (
        (json.dumps(receipt, ensure_ascii=False, separators=(",", ":")) + "\n").encode("utf-8")
        if args.compact
        else archival_encoded
    )
    if args.write_receipt:
        RECEIPT.write_bytes(archival_encoded)
    print(stdout_encoded.decode("utf-8"), end="")
    return 0 if not failures else 5


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(json.dumps({"status": "failure", "error_type": type(exc).__name__, "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        raise SystemExit(4)
