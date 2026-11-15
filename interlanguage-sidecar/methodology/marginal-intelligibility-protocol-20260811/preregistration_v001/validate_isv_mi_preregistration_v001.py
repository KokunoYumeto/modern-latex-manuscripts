#!/usr/bin/env python3
"""Independent, read-only validator for the bounded ISV MI preregistration."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker


BASE = Path(__file__).resolve().parent
PROTOCOL = BASE / "ISV_MI_PREREGISTRATION_V001.json"
PROTOCOL_SCHEMA = BASE / "ISV_MI_PREREGISTRATION_V001.schema.json"
AUDIT = BASE / "INPUT_REPIN_AUDIT.json"
AUDIT_SCHEMA = BASE / "INPUT_REPIN_AUDIT.schema.json"
FIXTURES = BASE / "ISV_MI_PREREGISTRATION_V001.hostile_fixtures.json"
MANIFEST = BASE / "MANIFEST.json"
SUMS = BASE / "SHA256SUMS.sha256"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest().upper()


def schema_errors(instance: Any, schema: dict[str, Any], prefix: str) -> list[dict[str, str]]:
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = []
    for err in sorted(validator.iter_errors(instance), key=lambda e: list(e.absolute_path)):
        loc = "/" + "/".join(str(x) for x in err.absolute_path)
        errors.append({"code": prefix, "detail": f"{loc}: {err.message}"})
    return errors


def add(errors: list[dict[str, str]], condition: bool, code: str, detail: str) -> None:
    if not condition:
        errors.append({"code": code, "detail": detail})


def semantic_errors(p: dict[str, Any]) -> list[dict[str, str]]:
    e: list[dict[str, str]] = []
    scope = p.get("scope", {})
    add(e, p.get("status") == "fail_closed_not_recruitment_ready", "LAUNCH_STATE", "Protocol status must remain fail-closed.")
    add(e, all(scope.get(k) == 0 for k in ["human_response_records", "participant_records", "speaker_records", "qualified_review_records", "jan_or_community_review_records"]), "SCOPE_NONCLAIM", "No people, responses, or reviews may be invented.")
    add(e, scope.get("reader_release_or_translation_mutation") is False and scope.get("external_message_sent") is False, "SCOPE_NONCLAIM", "This package may not mutate releases or send messages.")

    tree = p.get("declared_family_tree", {})
    add(e, tree.get("initially_symmetric") is True and tree.get("macrobranches") == ["east_slavic", "west_slavic", "south_slavic"], "TREE_SYMMETRY", "Tree must declare symmetric East/West/South macrobranches in frozen order.")
    add(e, tree.get("numeric_edge_lengths") is None and tree.get("empirical_outcome_weights") is None and tree.get("population_weights") is None, "TREE_SYMMETRY", "No tree weights may be invented.")

    gov = p.get("governance_comparator", {})
    required_groups = ["Russian", "Ukrainian_and_Belarusian", "Polish", "Czech_and_Slovak", "Slovene_and_Serbian_Croatian_Bosnian", "Bulgarian_and_Macedonian"]
    add(e, gov.get("groups") == required_groups, "GOVERNANCE_GROUPS", "Official comparator must contain exactly the six pinned groups.")
    add(e, gov.get("group_vote") == "one_vote_each" and gov.get("within_group_disagreement") == "one_half_vote_per_alternative", "GOVERNANCE_VOTE", "One-vote groups and half-votes on within-group disagreement are mandatory.")
    add(e, "population" in str(gov.get("tie_break", "")).lower(), "GOVERNANCE_TIE", "Pinned population tie-break missing.")
    add(e, "common_sense" in str(gov.get("common_sense_override", "")).lower(), "GOVERNANCE_COMMON_SENSE", "Pinned common-sense override missing.")
    add(e, gov.get("role") == "governance_comparison_only" and gov.get("empirical_outcome_weight") is False and gov.get("automatic_decision") is False, "GOVERNANCE_ROLE", "Governance comparator cannot weight empirical outcomes or decide automatically.")
    add(e, gov.get("observed_votes") is None and gov.get("observed_override") is None and gov.get("approval_inference") is False, "GOVERNANCE_ROLE", "No votes, overrides, or approval may be invented.")

    model = p.get("evidence_model", {})
    add(e, model.get("object_type") == "typed_evidence_DAG" and model.get("acyclic_required") is True, "DAG_REQUIRED", "Evidence object must remain a typed DAG.")
    add(e, model.get("predecessor_acyclic") is False and model.get("predecessor_cycle_edge_pair") == ["old_post44_witness->old_post44_scope_gap", "old_post44_scope_gap->old_post44_witness"] and model.get("construction_state") == "blocked_until_cycle_is_reconciled_in_an_append_only_successor_DAG", "DAG_REQUIRED", "Known predecessor cycle must remain explicit and held.")
    add(e, model.get("required_channels") == ["support", "candidate", "competitor", "adverse", "absence", "veto"] and model.get("channel_separation_required") is True, "EVIDENCE_CHANNELS", "Evidence channels must remain separate and complete.")
    add(e, model.get("adverse_evidence_policy", {}).get("offsettable_by_positive_mass") is False, "ADVERSE_OFFSET", "Positive mass cannot offset adverse evidence.")
    add(e, model.get("generated_text_may_witness_native_use") is False and model.get("may_define_human_intelligibility") is False and model.get("may_auto_decide") is False, "DAG_REQUIRED", "Evidence DAG cannot become native witness, human outcome, or auto-decision.")

    w0 = p.get("w0_projection", {})
    add(e, w0.get("id") == "W0" and w0.get("type") == "projection" and all(w0.get(k) is False for k in ["current_measurement", "accepted_writeback", "participant_arm", "human_outcome", "may_overwrite_state_c"]), "W0_PROJECTION", "W0 must remain an unapplied projection only.")
    add(e, w0.get("may_auto_decide") is False, "W0_DECISION", "W0 cannot decide automatically.")

    diag = p.get("concentration_diagnostics", {})
    add(e, diag.get("objects") == ["Hill_D1", "KL_to_declared_target"] and diag.get("separate_from_human_intelligibility") is True and diag.get("measures_intelligibility") is False and diag.get("measures_correctness") is False, "DIAGNOSTIC_SEPARATION", "D1/KL must remain concentration diagnostics only.")

    outcome = p.get("outcome_vector", {})
    domain_ids = [x.get("id") for x in outcome.get("domains", []) if isinstance(x, dict)]
    add(e, domain_ids == ["lexical", "morphology_morphosyntax", "syntax_connectives_register", "script", "integrated_passage_comprehension"], "OUTCOME_VECTOR", "Exactly five separately ordered outcome domains are required.")
    add(e, outcome.get("scalar_primary_outcome") is None and outcome.get("auto_decision_from_any_scalar") is False and outcome.get("grand_mean_may_erase_harm") is False, "SCALAR_DECISION", "No scalar or grand mean may decide or erase harm.")

    arm = p.get("arm_design", {})
    native = arm.get("native_language_control", {})
    passage = arm.get("whole_passage_contract", {})
    add(e, native.get("required") is True and native.get("bridge_candidate") is False and "same_frozen_source_information_units" in str(native.get("information_matching", "")), "NATIVE_CONTROL", "Native-language control must be required, information-matched, and non-candidate.")
    add(e, all(passage.get(k) is True for k in ["identical_information_required", "same_source_passage_id_required", "same_information_unit_set_required", "same_mathematical_propositions_required", "same_definitions_formulae_names_citations_and_examples_required", "same_question_answer_key_semantics_required"]), "PASSAGE_INFORMATION", "All whole-passage arms must carry identical frozen information.")
    add(e, passage.get("coherent_whole_passage_required") is True and passage.get("tokenwise_mosaic_forbidden") is True and passage.get("unilateral_gloss_definition_or_doublet_forbidden") is True, "PASSAGE_COHERENCE", "Coherent passages are mandatory and mosaics/unilateral aids forbidden.")

    people = p.get("participants_and_speakers", {})
    participant_fields = set(people.get("participant_metadata_required", []))
    add(e, {"pseudonymous_participant_id", "consent_state", "self_identified_native_standard_or_standards", "home_variety_or_dialect", "mathematical_training_band", "other_Slavic_language_exposure_matrix", "Russian_exposure_separately", "prior_Interslavic_exposure", "Latin_script_reading_proficiency", "Cyrillic_script_reading_proficiency", "script_preference"}.issubset(participant_fields), "PARTICIPANT_METADATA", "Participant language, exposure, script, and proficiency fields are incomplete.")
    speaker_fields = set(people.get("speaker_metadata_if_audio_is_added", []))
    add(e, {"pseudonymous_speaker_id", "self_identified_native_standard_or_standards", "home_variety_or_dialect", "Interslavic_speaking_proficiency", "other_Slavic_language_exposure_matrix", "independent_pronunciation_review_ids", "audio_file_sha256"}.issubset(speaker_fields), "SPEAKER_METADATA", "Conditional speaker provenance/proficiency fields are incomplete.")

    review = p.get("review_plan", {})
    add(e, review.get("required_macrobranches") == ["east_slavic", "west_slavic", "south_slavic"] and review.get("balanced_counts_required") is True and review.get("nonzero_each_macrobranch_required") is True, "REVIEW_BALANCE", "Competent review must be balanced and nonzero across East/West/South.")
    add(e, review.get("reviewer_count_per_macrobranch") is None and review.get("current_state") == "no_reviewers_or_approvals_recorded", "REVIEW_BALANCE", "No actual reviewer count or approval may be invented.")

    community = p.get("jan_and_community_review", {})
    jan = community.get("jan_van_steenbergen", {})
    comm = community.get("community_review", {})
    add(e, jan.get("response_state") == "none" and jan.get("approval_state") == "not_requested_not_inferred" and jan.get("silence_means_approval") is False, "JAN_APPROVAL", "Jan review cannot be inferred or invented.")
    add(e, comm.get("response_state") == "none" and comm.get("approval_state") == "not_requested_not_inferred" and comm.get("silence_or_participation_means_approval") is False, "JAN_APPROVAL", "Community review cannot be inferred or invented.")

    missing = p.get("missing_data_and_fail_closed", {})
    add(e, all(missing.get(k) is True for k in ["preregistered", "never_impute_from_related_language_or_macrobranch", "never_encode_unknown_as_zero", "never_treat_missing_as_pass", "participant_exclusion_before_arm_unblinding_only"]), "MISSING_FAIL_CLOSED", "Missing data must fail closed without imputation, zeroing, or post-unblinding exclusions.")

    sampling = p.get("sampling_and_assignment", {})
    add(e, sampling.get("actual_participants_declared") == [] and sampling.get("actual_speakers_declared") == [] and sampling.get("actual_reviewers_declared") == [] and sampling.get("participant_n") is None, "SCOPE_NONCLAIM", "No people or sample size may be invented.")
    add(e, sampling.get("optional_stopping") is False and sampling.get("outcome_blind_recruitment_only") is True, "OPTIONAL_STOPPING", "Recruitment cannot stop on outcome effects.")

    upstream = p.get("upstream_item_state", {})
    add(e, upstream.get("participant_ready") is False and upstream.get("direct_morphology_contrast_count") == 0 and upstream.get("west_surfaces_present") is False and upstream.get("south_surfaces_present") is False and upstream.get("native_authorship_records") == 0 and upstream.get("native_review_records") == 0 and upstream.get("direct_morphology_contrast_established") is False, "UPSTREAM_STATE", "Held upstream state must not be promoted.")

    stopping = p.get("stopping_and_revisit", {})
    add(e, stopping.get("effect_based_optional_stopping") is False and stopping.get("outcome_viewing_may_trigger_sample_stop") is False, "OPTIONAL_STOPPING", "Effect-based stopping is forbidden.")

    analysis = p.get("analysis_contract", {})
    add(e, analysis.get("state") == "blocked_not_analysis_ready" and all(analysis.get(k) is None for k in ["coefficients", "harm_margin", "false_friend_margin", "multiplicity_rule", "interval_rule"]), "ANALYSIS_UNFROZEN", "Analysis remains blocked until parameters and rules are honestly frozen.")
    add(e, analysis.get("single_scalar_decision_forbidden") is True and analysis.get("governance_projection_separate") is True and analysis.get("concentration_diagnostics_separate") is True, "SCALAR_DECISION", "Analysis objects must remain separate and non-scalar.")

    gates = {g.get("gate_id"): g.get("state") for g in p.get("launch_gates", []) if isinstance(g, dict)}
    add(e, all(gates.get(f"PREREG-G{i:03d}") == "pass" for i in [1, 2, 3, 5, 6]), "GATE_CONSISTENCY", "Completed structural gates G001-G003 and G005-G006 must pass.")
    add(e, gates.get("PREREG-G004") == "blocked" and all(gates.get(f"PREREG-G{i:03d}") == "blocked" for i in range(7, 13)) and gates.get("PREREG-G013") == "not_a_launch_gate", "GATE_CONSISTENCY", "DAG and empirical launch gates must remain blocked and community approval is not a launch gate.")
    return e


def pointer_parent(doc: Any, pointer: str) -> tuple[Any, str]:
    parts = [x.replace("~1", "/").replace("~0", "~") for x in pointer.split("/")[1:]]
    if not parts:
        raise ValueError("root mutation is prohibited")
    obj = doc
    for part in parts[:-1]:
        obj = obj[int(part)] if isinstance(obj, list) else obj[part]
    return obj, parts[-1]


def mutate(doc: dict[str, Any], mutation: dict[str, Any]) -> None:
    parent, key = pointer_parent(doc, mutation["path"])
    if mutation["op"] == "replace":
        if isinstance(parent, list):
            parent[int(key)] = mutation["value"]
        else:
            parent[key] = mutation["value"]
    elif mutation["op"] == "delete":
        if isinstance(parent, list):
            del parent[int(key)]
        else:
            del parent[key]
    else:
        raise ValueError(f"unsupported mutation op: {mutation['op']}")


def dag_errors(graph: dict[str, Any]) -> list[dict[str, str]]:
    errors: list[dict[str, str]] = []
    nodes = graph.get("nodes", [])
    ids = [n.get("id") for n in nodes]
    add(errors, len(ids) == len(set(ids)) and None not in ids, "UPSTREAM_DAG", "DAG node IDs must be unique and non-null.")
    idset = set(ids)
    adjacency = {x: [] for x in idset}
    indegree = {x: 0 for x in idset}
    known_cycle_edges = {
        ("old_post44_witness", "old_post44_scope_gap"),
        ("old_post44_scope_gap", "old_post44_witness"),
    }
    observed_pairs = {(x.get("from"), x.get("to")) for x in graph.get("edges", [])}
    add(errors, known_cycle_edges.issubset(observed_pairs), "UPSTREAM_DAG", "Expected preserved predecessor cycle edge-pair is missing.")
    for edge in graph.get("edges", []):
        source, target = edge.get("from"), edge.get("to")
        if source not in idset or target not in idset or not edge.get("type"):
            errors.append({"code": "UPSTREAM_DAG", "detail": "DAG edge has missing/unknown endpoint or type."})
            continue
        # Preserve the known defect as adverse evidence; remove one reverse
        # edge only for the residual-graph acyclicity test.
        if (source, target) != ("old_post44_scope_gap", "old_post44_witness"):
            adjacency[source].append(target)
            indegree[target] += 1
    queue = [x for x, degree in indegree.items() if degree == 0]
    visited = 0
    while queue:
        node = queue.pop()
        visited += 1
        for target in adjacency[node]:
            indegree[target] -= 1
            if indegree[target] == 0:
                queue.append(target)
    add(errors, visited == len(idset), "UPSTREAM_DAG", "Pinned evidence graph contains an additional or unrecorded cycle.")
    return errors


def upstream_errors(protocol: dict[str, Any], audit: dict[str, Any]) -> list[dict[str, str]]:
    errors: list[dict[str, str]] = []
    entries = audit.get("inputs", [])
    add(errors, len(entries) == 18 and len({x.get("input_id") for x in entries}) == 18, "REPIN_AUDIT", "Expected 18 distinct repinned inputs.")
    add(errors, audit.get("upstream_files_modified") == [], "REPIN_AUDIT", "Upstream mutation list must be empty.")
    by_role: dict[str, dict[str, Any]] = {}
    for item in entries:
        by_role[item.get("role", "")] = item
        path = (BASE / item.get("path", "")).resolve()
        if not path.is_file():
            errors.append({"code": "UPSTREAM_FILE", "detail": f"Missing input {item.get('input_id')}: {path}"})
            continue
        if path.stat().st_size != item.get("bytes") or digest(path) != item.get("sha256"):
            errors.append({"code": "UPSTREAM_HASH", "detail": f"Byte/hash drift for {item.get('input_id')}: {path}"})

    tree_entry = by_role.get("declared_symmetric_family_tree", {})
    if tree_entry:
        tree = load_json((BASE / tree_entry["path"]).resolve())
        add(errors, tree.get("tree_contract", {}).get("macrobranches_symmetric") is True and tree.get("tree_contract", {}).get("macrobranch_ids") == ["east_slavic", "west_slavic", "south_slavic"], "UPSTREAM_TREE", "Pinned tree no longer declares symmetric East/West/South.")

    item_entry = by_role.get("item_binding", {})
    if item_entry:
        item = load_json((BASE / item_entry["path"]).resolve())
        arm_count = sum(len(f.get("arms", [])) for f in item.get("families", []))
        channels = {x.get("edge_type") for x in item.get("evidence_registry", [])}
        add(errors, len(item.get("families", [])) == 12 and arm_count == 60 and item.get("claims", {}).get("participant_ready") is False, "UPSTREAM_ITEM", "Pinned item binding counts/state drifted.")
        add(errors, channels == {"support", "competitor", "adverse", "absence", "veto"}, "UPSTREAM_ITEM", "Pinned item evidence channel set drifted.")
        audit_state = item.get("morphology_scope_audit", {})
        add(errors, audit_state.get("direct_morphology_or_morphosyntax_contrast_count") == 0 and audit_state.get("lexically_overconcentrated") is True, "UPSTREAM_ITEM", "Pinned lexical-overconcentration state drifted.")

    morph_entry = by_role.get("morphology_binding_v2", {})
    if morph_entry:
        morph = load_json((BASE / morph_entry["path"]).resolve())
        loci = morph.get("loci", [])
        held = all(x.get("coverage", {}).get("west") == "missing_zero_surfaces" and x.get("coverage", {}).get("south") == "missing_zero_surfaces" and x.get("review_state", {}).get("native_authorship_records") == 0 and x.get("review_state", {}).get("native_review_records") == 0 and str(x.get("experimental_item_state", "")).startswith("held_") for x in loci)
        add(errors, len(loci) == 5 and held and morph.get("claims", {}).get("participant_ready") is False and morph.get("claims", {}).get("direct_morphology_contrast_established") is False, "UPSTREAM_MORPH", "Pinned held morphology state drifted or was silently promoted.")

    dag_entry = by_role.get("typed_evidence_graph_predecessor", {})
    if dag_entry:
        errors.extend(dag_errors(load_json((BASE / dag_entry["path"]).resolve())))

    official_entry = by_role.get("official_design_criteria_exact_capture", {})
    if official_entry:
        text = (BASE / official_entry["path"]).resolve().read_text(encoding="utf-8")
        for needle in ["six subgroups", "½ vote", "population decides", "common sense should always prevail"]:
            add(errors, needle in text, "UPSTREAM_AUTHORITY", f"Official design-criteria phrase missing: {needle}")

    return errors


def fixture_errors(protocol: dict[str, Any], schema: dict[str, Any], fixture_set: dict[str, Any]) -> tuple[list[dict[str, str]], list[dict[str, Any]]]:
    errors: list[dict[str, str]] = []
    results = []
    fixtures = fixture_set.get("fixtures", [])
    ids = [x.get("fixture_id") for x in fixtures]
    add(errors, len(fixtures) >= 24 and len(ids) == len(set(ids)), "FIXTURE_SET", "Hostile fixtures must be numerous and uniquely identified.")
    for fixture in fixtures:
        candidate = copy.deepcopy(protocol)
        mutate(candidate, fixture["mutation"])
        observed = semantic_errors(candidate)
        observed.extend(schema_errors(candidate, schema, "SCHEMA_PROTOCOL"))
        codes = sorted({x["code"] for x in observed})
        expected = fixture["expected_error_code"]
        rejected = expected in codes
        results.append({"fixture_id": fixture["fixture_id"], "expected_error_code": expected, "observed_error_codes": codes, "rejected": rejected})
        if not rejected:
            errors.append({"code": "FIXTURE_ACCEPTED", "detail": f"{fixture['fixture_id']} did not produce {expected}; observed {codes}"})
    return errors, results


def manifest_errors() -> list[dict[str, str]]:
    errors: list[dict[str, str]] = []
    if not MANIFEST.exists():
        return [{"code": "MANIFEST_MISSING", "detail": "MANIFEST.json not present."}]
    manifest = load_json(MANIFEST)
    for item in manifest.get("files", []):
        path = BASE / item.get("path", "")
        if not path.is_file() or path.stat().st_size != item.get("bytes") or digest(path) != item.get("sha256"):
            errors.append({"code": "MANIFEST_HASH", "detail": f"Manifest drift: {item.get('path')}"})
    if SUMS.exists():
        lines = [x for x in SUMS.read_text(encoding="ascii").splitlines() if x.strip()]
        for line in lines:
            expected, name = line.split("  ", 1)
            path = BASE / name
            if not path.is_file() or digest(path) != expected.upper():
                errors.append({"code": "CHECKSUM_FILE", "detail": f"Checksum drift: {name}"})
    return errors


def validate(include_manifest: bool) -> dict[str, Any]:
    protocol = load_json(PROTOCOL)
    protocol_schema = load_json(PROTOCOL_SCHEMA)
    audit = load_json(AUDIT)
    audit_schema = load_json(AUDIT_SCHEMA)
    fixture_set = load_json(FIXTURES)
    errors: list[dict[str, str]] = []
    errors.extend(schema_errors(protocol, protocol_schema, "SCHEMA_PROTOCOL"))
    errors.extend(schema_errors(audit, audit_schema, "SCHEMA_REPIN"))
    errors.extend(semantic_errors(protocol))
    errors.extend(upstream_errors(protocol, audit))
    fixture_problem, fixture_results = fixture_errors(protocol, protocol_schema, fixture_set)
    errors.extend(fixture_problem)
    if include_manifest:
        errors.extend(manifest_errors())
    return {
        "schema_id": "slisv-isv-mi-preregistration-validation-v1",
        "protocol_id": protocol.get("protocol_id"),
        "status": "PASS" if not errors else "FAIL",
        "validator_mode": "read_only_serial_memory_bounded",
        "manifest_checked": include_manifest,
        "checks": {
            "protocol_schema": not any(x["code"] == "SCHEMA_PROTOCOL" for x in errors),
            "repin_schema": not any(x["code"] == "SCHEMA_REPIN" for x in errors),
            "semantic_invariants": not any(x["code"] not in {"SCHEMA_PROTOCOL", "SCHEMA_REPIN", "UPSTREAM_FILE", "UPSTREAM_HASH", "UPSTREAM_TREE", "UPSTREAM_ITEM", "UPSTREAM_MORPH", "UPSTREAM_DAG", "UPSTREAM_AUTHORITY", "REPIN_AUDIT", "FIXTURE_SET", "FIXTURE_ACCEPTED", "MANIFEST_MISSING", "MANIFEST_HASH", "CHECKSUM_FILE"} for x in errors),
            "upstream_hashes_and_states": not any(x["code"].startswith("UPSTREAM_") or x["code"] == "REPIN_AUDIT" for x in errors),
            "hostile_fixtures_rejected": sum(1 for x in fixture_results if x["rejected"]),
            "hostile_fixture_count": len(fixture_results),
            "manifest_and_checksums": None if not include_manifest else not any(x["code"] in {"MANIFEST_MISSING", "MANIFEST_HASH", "CHECKSUM_FILE"} for x in errors)
        },
        "fixture_results": fixture_results,
        "errors": errors,
        "claim_boundary": "PASS proves schema, pinned-byte, DAG, semantic, fixture, and optional package-manifest integrity only. It does not prove participant readiness, source meaning, mathematical equivalence, grammar, naturalness, intelligibility, canonical status, approval, endorsement, or release readiness.",
        "next_cursor": protocol.get("next_cursor")
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", help="Emit indented JSON.")
    parser.add_argument("--compact", action="store_true", help="Emit compact JSON.")
    parser.add_argument("--include-manifest", action="store_true", help="Also verify MANIFEST.json and SHA256SUMS.sha256 when present.")
    args = parser.parse_args()
    result = validate(args.include_manifest)
    if args.json or args.compact:
        print(json.dumps(result, ensure_ascii=False, indent=None if args.compact else 2, sort_keys=True))
    else:
        print(f"{result['status']}: {result['checks']['hostile_fixtures_rejected']}/{result['checks']['hostile_fixture_count']} hostile fixtures rejected; errors={len(result['errors'])}")
        for error in result["errors"]:
            print(f"- {error['code']}: {error['detail']}")
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
