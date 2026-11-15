#!/usr/bin/env python3
"""Build the bounded Stage-0 marginal-intelligibility preregistration v002.

The builder is intentionally separate from the validator. It writes only the
explicit output directory supplied with --write and never mutates an input.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
from pathlib import Path
from typing import Any


RECORDED_AT = "2026-08-12T03:04:19+02:00"
DEFAULT_WORKSPACE = Path(r"C:\Users\user\Documents\interlanguage")
PACKAGE_REL = Path(
    "03_projects/language_management/slavic_interslavic/00_lane_control/"
    "marginal_intelligibility_20260811/preregistration_v002"
)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest().upper()


def strict_json(path: Path) -> Any:
    def reject(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        out: dict[str, Any] = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate JSON key {key!r} in {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=reject)


def file_pin(
    pin_id: str,
    role: str,
    rel: str,
    size: int,
    sha: str,
    acceptance_state: str,
    note: str = "",
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "pin_id": pin_id,
        "role": role,
        "pin_kind": "whole_file",
        "workspace_relative_path": rel,
        "expected_bytes": size,
        "expected_sha256": sha,
        "acceptance_state": acceptance_state,
    }
    if note:
        row["note"] = note
    return row


PINS: list[dict[str, Any]] = [
    file_pin("PIN-GOAL-001", "durable_goal_reconstruction", "03_projects/language_management/slavic_interslavic/00_lane_control/DURABLE_GOAL_RECONSTRUCTION_20260811.json", 7972, "B60EA4A7E6E729221292CECC080411B0AB4D92044886779957052A338B14845D", "governing_user_goal"),
    file_pin("PIN-GOAL-002", "active_goal_addendum", "03_projects/language_management/slavic_interslavic/00_lane_control/ACTIVE_GOAL_ADDENDUM_20260811.json", 4976, "BEAB7E2CB3D23BC2352EAD9A5AD992A86AB4A02CCD3ED8371EC1F90A4FF5F3B1", "governing_user_goal"),
    file_pin("PIN-PREREG1-001", "predecessor_preregistration", "03_projects/language_management/slavic_interslavic/00_lane_control/marginal_intelligibility_20260811/preregistration_v001/ISV_MI_PREREGISTRATION_V001.json", 28057, "17DDBA856C46A6B5840DF8D174B53EBF1B7BE5C67CF9B8A83EDA00DFB682934E", "superseded_design_input_not_launch_authority"),
    file_pin("PIN-PREREG1-002", "predecessor_preregistration_manifest", "03_projects/language_management/slavic_interslavic/00_lane_control/marginal_intelligibility_20260811/preregistration_v001/MANIFEST.json", 2406, "0BE79910DFF80253A2F4F478666C5DD589A2F521DF372FFB4F7C9A3CB061B8A2", "lineage_pin"),
    file_pin("PIN-OFFICIAL-001", "official_authority_snapshot_manifest", "03_projects/language_management/slavic_interslavic/00_lane_control/marginal_intelligibility_20260811/authority_snapshots/AUTHORITY_SNAPSHOT_MANIFEST.json", 107058, "CFF235A721386FB74CB5970C5F7114655EA791E5CC48777CCCC4CD3F83130B9A", "documentary_authority"),
    file_pin("PIN-OFFICIAL-002", "official_design_criteria_snapshot", "03_projects/language_management/slavic_interslavic/00_lane_control/marginal_intelligibility_20260811/authority_snapshots/snapshots/official_site/docs/learn/misc/design-criteria.md", 20238, "215184553FD9BDDE4A75632B82D9880D74ABEC3776732F182B55C576B0261CC3", "governance_comparator_only"),
    file_pin("PIN-DAG-001", "acyclic_typed_evidence_dag_successor", "03_projects/language_management/slavic_interslavic/00_lane_control/marginal_intelligibility_20260811/evidence_dag_successor_v001/TYPED_EVIDENCE_DAG_SUCCESSOR_V001.json", 85146, "873E00E3A62FEC63A2FDC278D72CAC2E00649D70BC0DAF2A6584BAB70DA75ED2", "accepted_mechanical_provenance_routing"),
    file_pin("PIN-DAG-002", "acyclic_typed_evidence_dag_manifest", "03_projects/language_management/slavic_interslavic/00_lane_control/marginal_intelligibility_20260811/evidence_dag_successor_v001/MANIFEST.json", 2827, "8E76D0A7F63F3DFBAB80449FCB652A69175C60EEDF297CE1CDDB4977C1C0512A", "lineage_pin"),
    file_pin("PIN-TREE-001", "symmetric_family_cohort_tree", "03_projects/language_management/slavic_interslavic/00_lane_control/marginal_intelligibility_20260811/ISV_SYMMETRIC_FAMILY_COHORT_TREE.json", 9015, "5A23D79C72889B7CC92E009FECDC90F5832834B4A12E28D3FA151E84B6685085", "declared_sampling_dependence_tree"),
    file_pin("PIN-TREE-002", "symmetric_family_cohort_tree_schema", "03_projects/language_management/slavic_interslavic/00_lane_control/marginal_intelligibility_20260811/ISV_SYMMETRIC_FAMILY_COHORT_TREE.schema.json", 1398, "F54C68E6A3E576C2DFF36A074D393FC1748F126FC7797C6FCE2EDB7D89504243", "schema_pin"),
    file_pin("PIN-DE-001", "current_german_authority_pointer", "03_projects/noether/07_german_canon_control/CURRENT_GERMAN_AUTHORITY_POINTER.json", 132270, "0053EA0B7E44DDE7EA7DC285ABC115DFC43F4A74B34C54DE8F39DE4E445D5BEA", "current_german_authority"),
    file_pin("PIN-DE-002", "immutable_german_pointer_v047", "03_projects/noether/07_german_canon_control/pointers/v047.json", 132270, "0053EA0B7E44DDE7EA7DC285ABC115DFC43F4A74B34C54DE8F39DE4E445D5BEA", "current_german_authority"),
    file_pin("PIN-DE-003", "resolved_german_authority_body_ED0011", "03_projects/noether/07_german_canon_control/candidates/ED0011/noether.tex", 2153594, "9E6BF2BC3155ECE3DF98CD8A408C23662BEFB047A1DDF200CA1DC8476A488BF3", "source_authority_not_mutated"),
    file_pin("PIN-LATIN3-001", "current_editable_latin_candidate_v003", "03_projects/language_management/slavic_interslavic/00_lane_control/isv_normalization_20260811/post_edit_latin_candidate_v003/ISV_POST_EDIT_LATIN_CANDIDATE_v003.json", 286591, "1234A20345E32908896BE0EF983B6DF5E3728EAA87EF722E7A303DC0B18BF497", "accepted_non_release_candidate"),
    file_pin("PIN-LATIN3-002", "current_editable_latin_candidate_v003_manifest", "03_projects/language_management/slavic_interslavic/00_lane_control/isv_normalization_20260811/post_edit_latin_candidate_v003/ISV_POST_EDIT_LATIN_CANDIDATE_PACKAGE_MANIFEST_v003.json", 8450, "E37B66EFC6E8B8B2AE332266A30691B1F41C740806F909CC18E60B4AE84ACF9A", "accepted_package_pin"),
    file_pin("PIN-INPUT4-001", "successor_input_ledger_v004", "03_projects/language_management/slavic_interslavic/00_lane_control/isv_normalization_20260811/successor_input_ledger_v004/ISV_SUCCESSOR_INPUT_LEDGER_v004.json", 2173148, "82557224A6C9150D8007C9CDB5CCCD7AF3D8E92EB1C17C7DE3933E59E2B40C2D", "accepted_input_control"),
    file_pin("PIN-INPUT4-002", "successor_input_ledger_v004_manifest", "03_projects/language_management/slavic_interslavic/00_lane_control/isv_normalization_20260811/successor_input_ledger_v004/ISV_SUCCESSOR_INPUT_LEDGER_PACKAGE_MANIFEST_v004.json", 17384, "1C162794126416069271BB56072393A2BBB1D6262F0EBD78EDAAAF91CEA339A6", "accepted_package_pin"),
    file_pin("PIN-ITEM-001", "marginal_intelligibility_item_binding", "03_projects/language_management/slavic_interslavic/00_lane_control/marginal_intelligibility_20260811/item_binding/ISV_MI_ITEM_BINDING.json", 145339, "8A9E733E7269ECB0DBAAC4FD7BBB5D9F7642AD11EB777D7F130773C39A8D37B7", "held_preregistration_input"),
    file_pin("PIN-MORPH2-001", "morphology_binding_v2", "03_projects/language_management/slavic_interslavic/00_lane_control/marginal_intelligibility_20260811/morphology_extension_v2/ISV_MI_MORPHOLOGY_BINDING_V2.json", 52159, "86A19C7AD035038A198739AF7BC507ED630BD91D09AACB3173D55E641A7BA1DD", "exact_source_binding_only_all_items_held"),
    file_pin("PIN-COMMUNITY-001", "community_review_packet_v001", "03_projects/language_management/slavic_interslavic/00_lane_control/marginal_intelligibility_20260811/community_review_packet_v001/ISV_MI_COMMUNITY_REVIEW_PACKET_v001.json", 250674, "4CC3721BB741F7205ACCA4DAF6F59351FA4B52F3C20F207BA8A0D4EAA5C5AC5A", "pre_review_no_outreach_no_approval"),
    file_pin("PIN-COMMUNITY-002", "community_review_packet_v001_manifest", "03_projects/language_management/slavic_interslavic/00_lane_control/marginal_intelligibility_20260811/community_review_packet_v001/ISV_MI_COMMUNITY_REVIEW_PACKET_v001.manifest.json", 11455, "2D4EA98FED5AADA5B292D8EF9FB5B8AE6C0B9DE5883C0A468A736867C91BCEDF", "lineage_pin"),
    file_pin("PIN-DECISION-067", "lj_nj_acceptance_withheld_decision", "03_projects/language_management/slavic_interslavic/00_lane_control/decision_records/SLISV-20260812-067.json", 7015, "7D9BFDC9D18EFEB4425D0BAB158655F43684F76384565DAA17B05AF24FCBABCA", "current_hold_authority_at_cutoff"),
    file_pin("PIN-DIFFICULTY-0092", "lj_nj_receipt_and_tree_custody_defect", "03_projects/language_management/slavic_interslavic/00_lane_control/difficulty_ledger/SLISV-DIFF-0092.json", 7458, "E13C1A4D3AF2FA82FA1E2031E932E87B91D43EAEBCF426D1E35993C05B627D49", "open_at_decision_cutoff"),
    file_pin("PIN-LJNJ-001", "lj_nj_semantic_candidate_data", "03_projects/language_management/slavic_interslavic/00_lane_control/isv_normalization_20260811/isv_lj_nj_morphology_triage_v001/ISV_LJ_NJ_MORPHOLOGY_TRIAGE_v001.json", 17670, "EE5ECDF9D9745BB8C4DF2E02532FAF50ED16B35534486CA5F07D06324F6DA7AC", "candidate_evidence_only_package_acceptance_withheld"),
    file_pin("PIN-DECISION-068", "priority_v004_parent_decision_pretty_json", "03_projects/language_management/slavic_interslavic/00_lane_control/decision_records/SLISV-20260812-068.json", 7675, "D450598D59F20AD5A526F6D7437DD1921BC24CFA4DE2D2C518BB59E02C345BB1", "exact_observed_pretty_json_serialization", "Decision 072 gives the correct hash but an inconsistent 10,216-byte assertion; observed exact bytes are 7,675."),
    file_pin("PIN-DECISION-070", "semantic_priority_v005_parent_acceptance", "03_projects/language_management/slavic_interslavic/00_lane_control/decision_records/SLISV-20260812-070.json", 8285, "0D89BD4CDCF9BE83EDFE3E81907ED0F08A8FCB0ACF0A8651BABE8A65C9028F37", "substantive_decision_cutoff_with_corrected_field"),
    file_pin("PIN-DECISION-072", "append_only_hash_serialization_correction", "03_projects/language_management/slavic_interslavic/00_lane_control/decision_records/SLISV-20260812-072.json", 4114, "413E48EFCD2C34846ABA30B2652F87E67494E53E436B092FF27AF8B3B4E68C81", "correction_consumed_with_byte_count_adverse_note"),
    file_pin("PIN-DIFFICULTY-0096", "decision_hash_serialization_failure_record", "03_projects/language_management/slavic_interslavic/00_lane_control/difficulty_ledger/SLISV-DIFF-0096.json", 4099, "038F679FE8F92D48440EA8425AAE01E926114EA2D46600CCCEA38299746D337B", "resolved_hash_error_but_byte_count_discrepancy_not_erased"),
    file_pin("PIN-DECISION-073", "append_only_decision_068_byte_count_correction", "03_projects/language_management/slavic_interslavic/00_lane_control/decision_records/SLISV-20260812-073.json", 3706, "164BD5177CA6273A5B3EF074ADC000EC9672449AE4D24E6221F1FF21455AED8A", "current_atomic_path_bytes_hash_correction"),
    file_pin("PIN-DIFFICULTY-0097", "decision_068_byte_count_failure_record", "03_projects/language_management/slavic_interslavic/00_lane_control/difficulty_ledger/SLISV-DIFF-0097.json", 3718, "38C8B3F2353B91EC7114E140627D3891D006395B94E5B88740D7C52379DDC5B4", "resolved_by_append_only_decision_073"),
    file_pin("PIN-COORD-001", "candidate_v003_coordinate_rebase_mechanical_evidence", "03_projects/language_management/slavic_interslavic/00_lane_control/isv_normalization_20260811/candidate_v003_coordinate_rebase_v001/ISV_CANDIDATE_V003_COORDINATE_REBASE_v001.json", 10358, "6285D8A8A070C40601FC21F5F082F8B8BBA1392001DF2C4E1DB3480A7316304E", "mechanical_only_not_semantic_or_projection_authority"),
    file_pin("PIN-COORD-002", "candidate_v003_coordinate_rebase_manifest", "03_projects/language_management/slavic_interslavic/00_lane_control/isv_normalization_20260811/candidate_v003_coordinate_rebase_v001/ISV_CANDIDATE_V003_COORDINATE_REBASE_PACKAGE_MANIFEST_v001.json", 7531, "0261F87BA0DE11BBB6ABEEB6D4F6A32EE8A1B1D056CA232B8FABFF700DE7845E", "accepted_package_pin"),
]

PRIORITY = [
    (1, 54, 50, 4, 1313955, "5253FF693D2AB501D6F3A5461BECA10A88E40737481F111378AE03740C2425D1", 7223, "65945D0A100E9C8822A1AEC0279678F8CCB1A9C0B38EE7DD8FAB2D51336571BD"),
    (2, 100, 59, 41, 2790863, "3BF6A6E6244DF23FCCFDB25531F24D044361A9829CF0E9BEB45E38DC1DA43649", 8131, "4FD907E541D445EE13A86CC149D133DE1E1B1A2B7AFA001519A324A5A0A11FB0"),
    (3, 100, 53, 47, 2944692, "FCE0C3A1691512BCBEADEC1127D5245628FE52CCA407133E498436CA60DF01FE", 9315, "BB548A88FB99E5FD193B93B0E1D93D213404254981E28AB97032A80F71AF3CDF"),
    (4, 100, 89, 11, 3220362, "A675D27E0A95DB156A57DB8D95A94BC651A5414A02B025BC35157DC0BC6A57BC", 10183, "1B5EC0176EF67388E1F7FF71031FE97B93B54A952B573CFF055F75872C521CCB"),
    (5, 100, 83, 17, 3142585, "E71BF2A6300D7C3477EF508EB82F1A9F76F197AD3D07F77120EAF4712D89505B", 11272, "F20DA684EA64EC926F34F4053D514DC77517B86474265214889D8A90138F39FF"),
]
for version, _, _, _, main_bytes, main_sha, manifest_bytes, manifest_sha in PRIORITY:
    tag = f"v{version:03d}"
    root = f"03_projects/language_management/slavic_interslavic/00_lane_control/isv_normalization_20260811/semantic_boundary_priority_review_{tag}"
    PINS.append(file_pin(f"PIN-PRIORITY-{tag.upper()}-MAIN", f"semantic_boundary_priority_review_{tag}", f"{root}/ISV_SEMANTIC_BOUNDARY_PRIORITY_REVIEW_{tag}.json", main_bytes, main_sha, "accepted_unapplied_candidate_v002_coordinate_review"))
    PINS.append(file_pin(f"PIN-PRIORITY-{tag.upper()}-MANIFEST", f"semantic_boundary_priority_review_{tag}_manifest", f"{root}/ISV_SEMANTIC_BOUNDARY_PRIORITY_REVIEW_PACKAGE_MANIFEST_{tag}.json", manifest_bytes, manifest_sha, "accepted_package_pin"))

PINS.extend(
    [
        {
            "pin_id": "PIN-DECISION-LOG-PREFIX-070",
            "role": "append_only_decision_log_prefix_through_070",
            "pin_kind": "jsonl_prefix_through_decision_id",
            "workspace_relative_path": "03_projects/language_management/slavic_interslavic/00_lane_control/SLAVIC_INTERSLAVIC_DECISION_LOG_v1.jsonl",
            "locator": {"decision_id": "SLISV-20260812-070", "line_number": 88, "terminal_eol": "LF"},
            "expected_bytes": 644825,
            "expected_sha256": "FF649F49610BA69474006BE5593B7A8D4A17AAFB33545574BD970EE62BB403FB",
            "acceptance_state": "substantive_authority_cutoff",
        },
        {
            "pin_id": "PIN-DECISION-068-ROW",
            "role": "decision_068_compact_log_row_utf8_without_eol",
            "pin_kind": "jsonl_row_utf8_no_eol",
            "workspace_relative_path": "03_projects/language_management/slavic_interslavic/00_lane_control/SLAVIC_INTERSLAVIC_DECISION_LOG_v1.jsonl",
            "locator": {"decision_id": "SLISV-20260812-068", "line_number": 86, "serialization": "UTF-8 exact compact row bytes excluding LF"},
            "expected_bytes": 7028,
            "expected_sha256": "6C02D0A582E50A99DE678FEA6AFF0A1555729925BE7EEE19EBC1BBF7442DE5FF",
            "acceptance_state": "exact_compact_row_serialization",
        },
    ]
)


def verify_input_pin(workspace: Path, pin: dict[str, Any]) -> None:
    path = workspace / Path(pin["workspace_relative_path"])
    if not path.is_file():
        raise FileNotFoundError(path)
    kind = pin["pin_kind"]
    if kind == "whole_file":
        size = path.stat().st_size
        digest = sha256_file(path)
    else:
        raw_lines = path.read_bytes().splitlines(keepends=True)
        loc = pin["locator"]
        idx = int(loc["line_number"]) - 1
        if idx < 0 or idx >= len(raw_lines):
            raise ValueError(f"line out of range for {pin['pin_id']}")
        row_raw = raw_lines[idx]
        row_no_eol = row_raw.rstrip(b"\r\n")
        row = json.loads(row_no_eol)
        if row.get("decision_id") != loc["decision_id"]:
            raise ValueError(f"decision locator mismatch for {pin['pin_id']}")
        if kind == "jsonl_prefix_through_decision_id":
            payload = b"".join(raw_lines[: idx + 1])
        elif kind == "jsonl_row_utf8_no_eol":
            payload = row_no_eol
        else:
            raise ValueError(f"unknown pin kind {kind}")
        size = len(payload)
        digest = hashlib.sha256(payload).hexdigest().upper()
    if size != pin["expected_bytes"] or digest != pin["expected_sha256"]:
        raise ValueError(
            f"pin drift {pin['pin_id']}: observed {size}/{digest}, "
            f"expected {pin['expected_bytes']}/{pin['expected_sha256']}"
        )


def make_protocol() -> dict[str, Any]:
    priority_rows = [
        {
            "version": f"v{v:03d}",
            "reviewed": reviewed,
            "accepted_preserve_candidates": accepted,
            "held_records_preserved": held,
            "coordinate_state": "candidate_v002_unapplied",
        }
        for v, reviewed, accepted, held, *_ in PRIORITY
    ]
    leaf_slots = [
        ("E1", "east_slavic", "official_group_russian", ["russian"]),
        ("E2", "east_slavic", "official_group_ukrainian_belarusian", ["ukrainian", "belarusian"]),
        ("W1", "west_slavic", "official_group_polish", ["polish"]),
        ("W2", "west_slavic", "official_group_czech_slovak", ["czech", "slovak"]),
        ("S1", "south_slavic", "official_group_slovene_bcs", ["slovene", "bosnian", "croatian", "serbian", "montenegrin"]),
        ("S2", "south_slavic", "official_group_bulgarian_macedonian", ["bulgarian", "macedonian"]),
    ]
    leaves = [
        {
            "slot_id": slot,
            "macrobranch": branch,
            "official_group_sampling_frame": group,
            "eligible_leaf_ids": eligible,
            "selected_leaf_id": None,
            "provisional_analyzable_readers": 12,
            "state": "leaf_selection_and_recruitment_unfrozen_launch_blocker",
            "pooling_rule": "preserve_each_selected_standard_as_a_separate_leaf",
        }
        for slot, branch, group, eligible in leaf_slots
    ]
    arms = [
        ("ARM-CURRENT-V018", "current_v018", "historical_current_reader_surface"),
        ("ARM-OFFICIAL-ISV", "official_isv", "official_standard_comparator"),
        ("ARM-DOMINANT-EAST", "dominant_east_baseline", "explicit_baseline_not_default_truth"),
        ("ARM-BRANCH-BALANCED", "branch_balanced_candidate", "candidate_under_test_not_claimed_optimum"),
        ("ARM-NATIVE-CONTROL", "native_language_control", "leaf_specific_instrument_calibration_only"),
    ]
    arm_rows = [
        {
            "arm_id": arm_id,
            "role": role,
            "interpretation": interpretation,
            "frozen_bytes": False,
            "sha256": None,
            "state": "not_constructed_or_not_frozen_launch_blocker",
        }
        for arm_id, role, interpretation in arms
    ]
    passage_types = [
        {
            "passage_type_id": "PT-DEFINITION",
            "role": "definition_and_terminology_dense",
            "required_features": ["controlled_definition", "formula_or_symbol_context", "running_prose_recurrence"],
            "frozen_passage_ids": [],
        },
        {
            "passage_type_id": "PT-PROOF",
            "role": "proof_connective_and_scope_dense",
            "required_features": ["inferential_connectives", "antecedent_scope", "proof_step_order"],
            "frozen_passage_ids": [],
        },
        {
            "passage_type_id": "PT-MIXED",
            "role": "mixed_expository_mathematical_prose",
            "required_features": ["definition_reuse", "morphosyntax", "technical_register", "integrated_inference"],
            "frozen_passage_ids": [],
        },
    ]
    gates = [
        ("PREREG2-G001", "all_declared_input_pins_match", "pass"),
        ("PREREG2-G002", "symmetric_East_West_South_tree_declared", "pass"),
        ("PREREG2-G003", "official_vote_system_is_governance_comparator_only", "pass"),
        ("PREREG2-G004", "acyclic_typed_evidence_DAG_successor_replayed", "pass"),
        ("PREREG2-G005", "German_v047_resolves_exact_ED0011", "pass"),
        ("PREREG2-G006", "decision_068_serialization_bytes_fully_reconciled", "pass"),
        ("PREREG2-G007", "six_exact_leaf_identities_frozen_two_per_macrobranch", "blocked"),
        ("PREREG2-G008", "simulation_justifies_analyzable_n_and_recruitment_oversample", "blocked"),
        ("PREREG2-G009", "ethics_consent_privacy_retention_withdrawal_frozen", "blocked"),
        ("PREREG2-G010", "five_arm_surfaces_frozen_and_byte_identical_roles_collapsed", "blocked"),
        ("PREREG2-G011", "coherent_same_information_passages_questions_and_answer_keys_frozen", "blocked"),
        ("PREREG2-G012", "qualified_West_and_South_surfaces_and_balanced_independent_review_complete", "blocked"),
        ("PREREG2-G013", "native_language_controls_authored_reviewed_and_frozen", "blocked"),
        ("PREREG2-G014", "randomization_seed_assignment_and_blinding_commitments_frozen", "blocked"),
        ("PREREG2-G015", "harm_false_friend_multiplicity_interval_and_exclusion_rules_frozen", "blocked"),
        ("PREREG2-G016", "lj_nj_package_receipt_and_tree_custody_hold_resolved_and_consumed", "blocked"),
        ("PREREG2-G017", "all_semantic_holds_and_unreviewed_gap_population_resolved_for_included_passages", "blocked"),
        ("PREREG2-G018", "Jan_or_community_approval", "not_a_launch_gate"),
    ]
    return {
        "$schema": "./ISV_MI_PREREGISTRATION_V002.schema.json",
        "schema_id": "slisv-isv-mi-preregistration-v002",
        "protocol_id": "SLISV-ISV-MI-PREREG-20260812-002",
        "version": "0.0.2-bounded-stage0-proposal",
        "recorded_at": RECORDED_AT,
        "timezone": "Europe/Berlin",
        "status": "fail_closed_not_launch_ready_no_human_validation",
        "purpose": "Define the smallest honest Stage-0 marginal-intelligibility design while repinning the current bounded Noether/Interslavic evidence state. This is a proposed commitment, not achieved validation, recruitment authorization, canonicality, or publication readiness.",
        "authority_cutoff": {
            "substantive_decision_prefix_through": "SLISV-20260812-070",
            "decision_log_prefix_pin_id": "PIN-DECISION-LOG-PREFIX-070",
            "post_cutoff_corrections_consumed": ["SLISV-20260812-072", "SLISV-20260812-073"],
            "post_cutoff_substantive_decisions_consumed": [],
            "decision_068_serializations": {
                "standalone_pretty_json": {"pin_id": "PIN-DECISION-068", "observed_bytes": 7675, "sha256": "D450598D59F20AD5A526F6D7437DD1921BC24CFA4DE2D2C518BB59E02C345BB1"},
                "compact_log_row_utf8_no_eol": {"pin_id": "PIN-DECISION-068-ROW", "observed_bytes": 7028, "sha256": "6C02D0A582E50A99DE678FEA6AFF0A1555729925BE7EEE19EBC1BBF7442DE5FF"},
                "superseded_invalid_hash": "6C02D0A5F48BFD8595EC01C6F9939EC561D6B3707A73336EEB48330CD18E1C11",
                "decision_072_claimed_standalone_bytes": 10216,
                "superseded_invalid_standalone_bytes": 10216,
                "current_atomic_tuple_correction": "SLISV-20260812-073",
                "byte_count_conflict": "resolved_append_only; exact standalone tuple is 7675 bytes and D450...; preserve and reject the superseded 10216-byte assertion",
            },
            "rule": "Name the exact serialization and EOL convention. The superseded hash may appear only as historical adverse evidence and can never satisfy a pin.",
        },
        "input_repin_audit": {
            "path": "INPUT_REPIN_AUDIT_V002.json",
            "pin_count": len(PINS),
            "all_pins_required": True,
            "upstream_mutation_allowed": False,
        },
        "official_authority": {
            "snapshot_manifest_pin_id": "PIN-OFFICIAL-001",
            "design_criteria_pin_id": "PIN-OFFICIAL-002",
            "role": "documentary_language_and_governance_authority_not_human_outcome",
            "six_group_vote_role": "separate_governance_comparator_only",
            "automatic_decision": False,
            "community_certification_inferred": False,
        },
        "evidence_model": {
            "object_type": "typed_evidence_DAG",
            "dag_pin_id": "PIN-DAG-001",
            "workspace_relative_path": next(p["workspace_relative_path"] for p in PINS if p["pin_id"] == "PIN-DAG-001"),
            "bytes": 85146,
            "sha256": "873E00E3A62FEC63A2FDC278D72CAC2E00649D70BC0DAF2A6584BAB70DA75ED2",
            "acyclic_required": True,
            "acyclic_replayed": True,
            "channels": ["support", "candidate", "competitor", "adverse", "absence", "veto"],
            "absence_is_not_adverse": True,
            "candidate_is_not_support": True,
            "positive_mass_offsets_adverse": False,
            "may_define_human_intelligibility": False,
            "may_auto_decide": False,
        },
        "family_tree": {
            "tree_pin_id": "PIN-TREE-001",
            "macrobranches": ["east_slavic", "west_slavic", "south_slavic"],
            "macrobranches_symmetric": True,
            "numeric_edge_lengths": None,
            "empirical_weights": None,
            "population_weights": None,
            "missing_leaf_rule": "unknown_not_zero_not_imputed",
            "cyrillic_interslavic_is_independent_leaf": False,
        },
        "current_state": {
            "german_authority": {
                "pointer_id": "NOETH-DE-AUTH-v047-20260808",
                "pointer_sha256": "0053EA0B7E44DDE7EA7DC285ABC115DFC43F4A74B34C54DE8F39DE4E445D5BEA",
                "resolved_authority_id": "NOETH-DE-ED-0011",
                "resolved_body_bytes": 2153594,
                "resolved_body_sha256": "9E6BF2BC3155ECE3DF98CD8A408C23662BEFB047A1DDF200CA1DC8476A488BF3",
                "canonical_claim": False,
            },
            "latin_candidate_v003": {
                "main_pin_id": "PIN-LATIN3-001",
                "manifest_pin_id": "PIN-LATIN3-002",
                "records": 81,
                "replace": 31,
                "preserve": 42,
                "holds": 8,
                "status": "accepted_non_release_editable_latin_candidate_not_reader_not_canonical",
            },
            "successor_input_v004": {
                "main_pin_id": "PIN-INPUT4-001",
                "manifest_pin_id": "PIN-INPUT4-002",
                "records": 81,
                "proposed_replace": 31,
                "proposed_preserve": 42,
                "holds": 8,
                "application_authority_records": 0,
            },
            "semantic_boundary_review": {
                "packages": priority_rows,
                "reviewed_total": 454,
                "accepted_preserve_candidates_total": 334,
                "raw_hold_records_preserved_total": 120,
                "decision_060_note": "Two of the four v001 hold loci later received bounded unapplied proposals; the original four hold records remain preserved as lineage and are not silently rewritten.",
                "unreviewed_semantic_gap_records": 2737,
                "ordinary_false_positives_in_purposive_priority_sample": 0,
                "precision_extrapolation_authorized": False,
                "next_cursor": {"rank": 451, "record_id": "SLISV-SBA-G001996", "score": 49},
            },
            "coordinate_rebase_v001": {
                "main_pin_id": "PIN-COORD-001",
                "manifest_pin_id": "PIN-COORD-002",
                "mappings": 4839,
                "intervals": 19356,
                "role": "mechanical_candidate_v002_to_v003_locator_evidence_only",
                "semantic_authority": False,
                "projection_authority": False,
            },
            "item_and_morphology": {
                "item_binding_pin_id": "PIN-ITEM-001",
                "item_families": 12,
                "item_arm_roles": 60,
                "morphology_v2_pin_id": "PIN-MORPH2-001",
                "morphology_loci": 5,
                "qualified_west_experimental_surfaces": 0,
                "qualified_south_experimental_surfaces": 0,
                "native_controls": 0,
                "lj_nj": {
                    "semantic_candidate_pin_id": "PIN-LJNJ-001",
                    "occurrences": 10536,
                    "provisional_A": 473,
                    "provisional_B": 363,
                    "held": 9700,
                    "package_state": "HOLD_acceptance_withheld_at_authority_cutoff",
                    "hold_decision": "SLISV-20260812-067",
                    "defect_record": "SLISV-DIFF-0092",
                    "reason": "unmanifested_receipt_tree_custody_and_uncaptured_parent_hostile_result_at_cutoff",
                },
            },
            "community_review": {
                "packet_pin_id": "PIN-COMMUNITY-001",
                "review_units": 19,
                "responses": 0,
                "approvals": 0,
                "west_authored_arms": 0,
                "south_authored_arms": 0,
                "Jan_or_community_returns": 0,
                "outreach_authorized": False,
                "outreach_performed": False,
            },
            "human_evidence": {
                "participants": 0,
                "analyzable_readers": 0,
                "qualified_native_controls": 0,
                "qualified_review_responses": 0,
                "human_intelligibility_estimates": 0,
            },
        },
        "stage0_design": {
            "design_state": "proposed_commitments_not_achieved_validation_launch_blocked",
            "study_unit": "coherent_information_matched_passage_arm_exposure_with_leaf_specific_reader",
            "leaf_sampling": {
                "slots": leaves,
                "required_slots_per_macrobranch": 2,
                "provisional_analyzable_readers_per_selected_leaf": 12,
                "provisional_total_analyzable_readers": 72,
                "actual_analyzable_readers": 0,
                "sample_size_status": "heuristic_placeholder_no_simulation_or_power_justification",
                "recruitment_oversample": None,
                "unsampled_leaf_rule": "remain_visible_as_unknown_not_imputed_not_claimed",
            },
            "arms": {
                "roles": arm_rows,
                "declared_role_count": 5,
                "byte_identical_collapse": {
                    "required": True,
                    "rule": "Any byte-identical arm roles collapse to one exposure and one observation; aliases and all original roles remain recorded.",
                    "maximum_unique_exposures_per_item": 5,
                    "observed_collapses": None,
                },
                "script_rule": "Latin and deterministic Cyrillic Interslavic are script conditions over identical language content, never independent language witnesses or votes.",
            },
            "assignment": {
                "design": "balanced_incomplete_block",
                "constraints": [
                    "balance by selected leaf, macrobranch, item, passage type, arm alias set, and competent script condition",
                    "one arm per decision family per participant",
                    "one coherent version per passage per participant",
                    "no participant sees byte-identical aliases twice",
                    "assignment generated only after frozen arm, question, answer-key, leaf, exclusion, and seed commitments",
                ],
                "randomization_seed_commitment": None,
                "assignment_table_sha256": None,
                "state": "not_generated_launch_blocker",
            },
            "passages": {
                "types": passage_types,
                "whole_passage_contract": {
                    "same_German_authority_units": True,
                    "same_information_units": True,
                    "same_mathematics_formulae_definitions_names_citations_examples": True,
                    "coherent_whole_passage_required": True,
                    "tokenwise_mosaic_forbidden": True,
                    "unilateral_gloss_or_doublet_forbidden": True,
                    "question_and_answer_key_semantics_identical": True,
                },
                "frozen_passage_count": 0,
                "state": "not_constructed_not_source_equivalence_certified_launch_blocker",
            },
            "outcome_vector": {
                "primary_scalar": None,
                "auto_choice_from_scalar": False,
                "baseline": "dominant_east_baseline",
                "marginal_effect_definition": "within_selected_leaf arm_minus_dominant_east_baseline contrast for the same frozen item or coherent passage and outcome domain",
                "domains": [
                    {"domain_id": "lexical", "observables": ["sense_accuracy", "false_friend_error", "confidence", "correct_response_time"]},
                    {"domain_id": "morphology_morphosyntax", "observables": ["grammatical_relation_accuracy", "scope_or_referent_accuracy", "confidence", "correct_response_time"]},
                    {"domain_id": "syntax_connectives_register", "observables": ["inferential_relation_accuracy", "proof_step_order", "register_misread", "confidence", "correct_response_time"]},
                    {"domain_id": "script", "observables": ["matched_content_accuracy_difference", "reading_time_difference", "script_specific_error"]},
                    {"domain_id": "integrated_passage_comprehension", "observables": ["concept_accuracy", "non_keyword_inference_accuracy", "proof_step_order", "terminology_consistency_error", "blinded_free_paraphrase_rubric"]},
                ],
            },
            "reporting": {
                "order": ["raw_anonymized_trials", "leaf_by_arm_by_domain", "macrobranch_by_domain_if_both_leaf_slots_estimable", "branch_equal_vector_if_all_three_macrobranches_estimable", "minimum_sampled_leaf_vector", "false_friend_and_harm_ledger", "unknown_and_not_estimable_cells", "governance_comparator_separately"],
                "branch_equal_rule": "Each estimable macrobranch contributes one third; within a macrobranch the two selected leaves contribute equally. If either selected leaf is not estimable, that macrobranch and the branch-equal summary are not estimable.",
                "minimum_cohort_rule": "Report the minimum selected-leaf effect for every arm and domain before any branch-equal summary.",
                "no_harm_rule": "No broad recommendation if any selected leaf crosses a preregistered adverse margin; the margin is currently null and launch-blocking.",
                "false_friend_rule": "Report count, rate, severity, exact item, leaf, sense, and confidence; high-severity false-friend evidence holds the affected arm regardless of grand mean.",
                "grand_mean_may_erase_harm": False,
            },
            "missing_data": {
                "missing_equals": "unknown",
                "impute_from_relative_language": False,
                "encode_unknown_as_zero": False,
                "treat_missing_as_pass": False,
                "not_estimable_rule": "Serialize not_estimable with exact reason whenever a frozen minimum, assignment, review, answer-key, or model gate fails.",
                "outcome_imputation": False,
            },
            "analysis_and_decision": {
                "model_specification": None,
                "harm_margin": None,
                "false_friend_margin": None,
                "multiplicity_rule": None,
                "interval_rule": None,
                "exclusion_rule": None,
                "answer_key_commitment": None,
                "no_scalar_auto_choice": True,
                "choice_rule": "Human-adjudicated vector and gate decision only after leaf-first results, minimum-cohort/no-harm and false-friend review; no algorithmic maximum or canonical auto-promotion.",
            },
        },
        "launch_gates": [{"gate_id": gid, "criterion": criterion, "state": state} for gid, criterion, state in gates],
        "claim_boundary": {
            "permitted": ["input_bytes_repinned", "acyclic_DAG_successor_bound", "symmetric_tree_bound", "Stage0_structure_proposed", "launch_blockers_explicit"],
            "prohibited": ["participant_ready", "recruitment_authorized", "human_intelligibility_measured", "canonical_Interslavic", "maximally_intelligible", "pan_Slavic_validated", "native_approved", "community_approved", "Jan_van_Steenbergen_approved", "release_ready", "publication_ready"],
            "reader_or_translation_bytes_mutated": False,
            "participant_launch_performed": False,
            "outreach_performed": False,
            "publication_handoff_ready": False,
        },
        "proof_boundary": {
            "proves": [
                "The declared exact input pins and bounded decision cutoff can be independently replayed.",
                "The pinned evidence graph is the acyclic successor, not the cyclic predecessor.",
                "The proposed Stage-0 structure preserves two leaf slots per macrobranch, byte-identical arm collapse, leaf-first reporting, and missing-as-unknown semantics.",
            ],
            "does_not_prove": [
                "No participant, reader, reviewer, native control, West or South experimental surface, community response, approval, human effect, or canonical result exists because of this package.",
                "The provisional 12 analyzable readers per leaf is not a justified sample size and cannot authorize launch.",
                "Validator success cannot establish source meaning, naturalness, human comprehension, or canonicality.",
            ],
        },
        "continuation_cursor": "Preserve decisions 072 and 073 as the append-only two-step provenance correction and reject both superseded hash/size values; preserve the lj/nj HOLD; select exactly two leaf standards per macrobranch without pooling false standards; obtain qualified West/South and native-control surfaces; freeze ethics, recruitment simulation and sample size, passages/arms/questions/answer keys, random seed/assignment, scoring, exclusions, margins, multiplicity and intervals; then issue a successor before outreach or participant launch.",
    }


def make_schema() -> dict[str, Any]:
    gate_schema = {
        "type": "object",
        "additionalProperties": False,
        "required": ["gate_id", "criterion", "state"],
        "properties": {
            "gate_id": {"type": "string", "pattern": "^PREREG2-G[0-9]{3}$"},
            "criterion": {"type": "string", "minLength": 1},
            "state": {"enum": ["pass", "blocked", "not_a_launch_gate"]},
        },
    }
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "slisv-isv-mi-preregistration-v002.schema.json",
        "title": "Fail-closed Interslavic marginal-intelligibility Stage-0 preregistration v002",
        "type": "object",
        "additionalProperties": False,
        "required": ["$schema", "schema_id", "protocol_id", "version", "recorded_at", "timezone", "status", "purpose", "authority_cutoff", "input_repin_audit", "official_authority", "evidence_model", "family_tree", "current_state", "stage0_design", "launch_gates", "claim_boundary", "proof_boundary", "continuation_cursor"],
        "properties": {
            "$schema": {"const": "./ISV_MI_PREREGISTRATION_V002.schema.json"},
            "schema_id": {"const": "slisv-isv-mi-preregistration-v002"},
            "protocol_id": {"const": "SLISV-ISV-MI-PREREG-20260812-002"},
            "version": {"const": "0.0.2-bounded-stage0-proposal"},
            "recorded_at": {"type": "string", "pattern": "\\+02:00$"},
            "timezone": {"const": "Europe/Berlin"},
            "status": {"const": "fail_closed_not_launch_ready_no_human_validation"},
            "purpose": {"type": "string", "minLength": 100},
            "authority_cutoff": {"type": "object", "required": ["substantive_decision_prefix_through", "post_cutoff_corrections_consumed", "decision_068_serializations", "rule"], "properties": {"substantive_decision_prefix_through": {"const": "SLISV-20260812-070"}, "decision_log_prefix_pin_id": {"const": "PIN-DECISION-LOG-PREFIX-070"}, "post_cutoff_corrections_consumed": {"const": ["SLISV-20260812-072", "SLISV-20260812-073"]}, "post_cutoff_substantive_decisions_consumed": {"const": []}, "decision_068_serializations": {"type": "object"}, "rule": {"type": "string"}}, "additionalProperties": False},
            "input_repin_audit": {"type": "object", "required": ["path", "pin_count", "all_pins_required", "upstream_mutation_allowed"], "properties": {"path": {"const": "INPUT_REPIN_AUDIT_V002.json"}, "pin_count": {"type": "integer", "minimum": 1}, "all_pins_required": {"const": True}, "upstream_mutation_allowed": {"const": False}}, "additionalProperties": False},
            "official_authority": {"type": "object"},
            "evidence_model": {"type": "object", "required": ["object_type", "dag_pin_id", "workspace_relative_path", "bytes", "sha256", "acyclic_required", "acyclic_replayed", "channels", "may_define_human_intelligibility", "may_auto_decide"], "properties": {"object_type": {"const": "typed_evidence_DAG"}, "dag_pin_id": {"const": "PIN-DAG-001"}, "workspace_relative_path": {"type": "string"}, "bytes": {"type": "integer"}, "sha256": {"type": "string", "pattern": "^[0-9A-F]{64}$"}, "acyclic_required": {"const": True}, "acyclic_replayed": {"const": True}, "channels": {"const": ["support", "candidate", "competitor", "adverse", "absence", "veto"]}, "absence_is_not_adverse": {"const": True}, "candidate_is_not_support": {"const": True}, "positive_mass_offsets_adverse": {"const": False}, "may_define_human_intelligibility": {"const": False}, "may_auto_decide": {"const": False}}, "additionalProperties": False},
            "family_tree": {"type": "object", "required": ["tree_pin_id", "macrobranches", "macrobranches_symmetric", "missing_leaf_rule", "cyrillic_interslavic_is_independent_leaf"], "properties": {"tree_pin_id": {"const": "PIN-TREE-001"}, "macrobranches": {"const": ["east_slavic", "west_slavic", "south_slavic"]}, "macrobranches_symmetric": {"const": True}, "numeric_edge_lengths": {"type": "null"}, "empirical_weights": {"type": "null"}, "population_weights": {"type": "null"}, "missing_leaf_rule": {"const": "unknown_not_zero_not_imputed"}, "cyrillic_interslavic_is_independent_leaf": {"const": False}}, "additionalProperties": False},
            "current_state": {"type": "object", "required": ["german_authority", "latin_candidate_v003", "successor_input_v004", "semantic_boundary_review", "coordinate_rebase_v001", "item_and_morphology", "community_review", "human_evidence"]},
            "stage0_design": {"type": "object", "required": ["design_state", "study_unit", "leaf_sampling", "arms", "assignment", "passages", "outcome_vector", "reporting", "missing_data", "analysis_and_decision"]},
            "launch_gates": {"type": "array", "minItems": 1, "uniqueItems": True, "items": gate_schema},
            "claim_boundary": {"type": "object", "required": ["permitted", "prohibited", "reader_or_translation_bytes_mutated", "participant_launch_performed", "outreach_performed", "publication_handoff_ready"], "properties": {"permitted": {"type": "array", "items": {"type": "string"}}, "prohibited": {"type": "array", "items": {"type": "string"}}, "reader_or_translation_bytes_mutated": {"const": False}, "participant_launch_performed": {"const": False}, "outreach_performed": {"const": False}, "publication_handoff_ready": {"const": False}}, "additionalProperties": False},
            "proof_boundary": {"type": "object", "required": ["proves", "does_not_prove"], "properties": {"proves": {"type": "array", "items": {"type": "string"}}, "does_not_prove": {"type": "array", "items": {"type": "string"}}}, "additionalProperties": False},
            "continuation_cursor": {"type": "string", "minLength": 100},
        },
    }


def make_audit() -> dict[str, Any]:
    return {
        "schema_id": "slisv-isv-mi-preregistration-v002-input-repin-audit",
        "audit_id": "SLISV-ISV-MI-PREREG2-REPIN-20260812-001",
        "recorded_at": RECORDED_AT,
        "timezone": "Europe/Berlin",
        "status": "exact_pins_replayed_with_append_only_hash_and_byte_count_corrections_consumed",
        "workspace_root": "C:/Users/user/Documents/interlanguage",
        "policy": "Every input is read-only. Whole-file, JSONL-prefix, and compact-row serializations are distinct. Hash or path drift fails closed; a corrected hash does not cure a false byte count.",
        "pins": PINS,
        "counts": {"pins": len(PINS), "whole_files": sum(p["pin_kind"] == "whole_file" for p in PINS), "jsonl_prefixes": 1, "jsonl_rows": 1},
        "adverse_provenance": [{"issue_id": "PREREG2-ADV-001", "state": "resolved_append_only_by_SLISV-20260812-073_and_SLISV-DIFF-0097", "symptom": "Decision 072 and difficulty 0096 assert 10,216 bytes for the standalone decision-068 pretty JSON, but exact ReadAllBytes/Get-Item replay observes 7,675 bytes at the accepted D450... hash.", "action": "Bind 7,675 observed bytes and D450...; preserve decisions 072/073; reject the superseded 10,216-byte assertion and 6C02D0A5F48B... hash."}],
        "proof_boundary": {"proves": "Exact byte identities at this package build; no upstream mutation.", "does_not_prove": "Semantic correctness, naturalness, human intelligibility, community approval, canonicality, or launch readiness."},
    }


def make_csv(protocol: dict[str, Any]) -> str:
    output = io.StringIO(newline="")
    fields = ["row_type", "stable_id", "macrobranch", "role_or_criterion", "state", "planned_analyzable_n", "value", "note"]
    writer = csv.DictWriter(output, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    for leaf in protocol["stage0_design"]["leaf_sampling"]["slots"]:
        writer.writerow({"row_type": "leaf_slot", "stable_id": leaf["slot_id"], "macrobranch": leaf["macrobranch"], "role_or_criterion": leaf["official_group_sampling_frame"], "state": leaf["state"], "planned_analyzable_n": leaf["provisional_analyzable_readers"], "value": "|".join(leaf["eligible_leaf_ids"]), "note": "selected_leaf_id=null; no pooling"})
    for arm in protocol["stage0_design"]["arms"]["roles"]:
        writer.writerow({"row_type": "arm_role", "stable_id": arm["arm_id"], "role_or_criterion": arm["role"], "state": arm["state"], "value": "sha256=null", "note": arm["interpretation"]})
    for passage in protocol["stage0_design"]["passages"]["types"]:
        writer.writerow({"row_type": "passage_type", "stable_id": passage["passage_type_id"], "role_or_criterion": passage["role"], "state": "no_frozen_passages", "value": "|".join(passage["required_features"]), "note": "same-information coherent passage required"})
    for gate in protocol["launch_gates"]:
        writer.writerow({"row_type": "launch_gate", "stable_id": gate["gate_id"], "role_or_criterion": gate["criterion"], "state": gate["state"], "note": "not a readiness claim"})
    return output.getvalue()


def make_protocol_md(protocol: dict[str, Any]) -> str:
    return """# Interslavic marginal-intelligibility Stage-0 preregistration v002

Status: **fail closed; not launch ready; no human validation**.

This successor repins the durable goal, official snapshot, acyclic evidence-DAG successor, symmetric East/West/South tree, German v047/ED0011 authority, Latin candidate v003, successor-input v004, item/morphology controls, community packet, semantic review through v005, and the mechanical coordinate rebase. It consumes substantive decisions only through `SLISV-20260812-070`, plus append-only corrections `SLISV-20260812-072` and `SLISV-20260812-073`.

The two-step correction is preserved: decision 072 corrects the serialization hashes, and decision 073 corrects its mistaken 10,216-byte assertion. The decision-068 standalone file is exactly 7,675 bytes at `D450598D...`; the compact log row is a different UTF-8/no-EOL serialization at `6C02D0A582E5...`. The values `6C02D0A5F48B...` and 10,216 bytes are superseded and cannot satisfy any pin.

## Proposed Stage 0

- Two sampled leaf slots per macrobranch, one from each official governance group sampling frame: six selected standards total.
- Provisional target: 12 analyzable readers per selected leaf, 72 total. This is a placeholder, not a power result; simulation, attrition allowance, recruitment window, and exact leaf identities remain launch-blocking.
- Five arm roles: current v018, official Interslavic, dominant-East baseline, branch-balanced candidate, and leaf-specific native-language control.
- Byte-identical roles collapse to one exposure and observation while retaining aliases.
- Balanced incomplete assignment; one arm per decision family and one coherent version per passage for each participant.
- Three coherent passage classes: definition/terminology dense, proof/connective dense, and mixed expository mathematical prose.
- Leaf-first outcome vectors for lexical, morphology/morphosyntax, syntax/connectives/register, script, and integrated passage comprehension.
- A branch-equal summary is estimable only when both selected leaves in all three macrobranches are estimable. Minimum-leaf, no-harm, and false-friend reporting precede any aggregate.
- Missing means unknown. No relative-language imputation, zero encoding, or scalar automatic choice.

## Current blockers

There are zero West/South experimental surfaces, native controls, participants, qualified review responses, Jan/community returns, or outreach authorization. The five arm surfaces, passage bytes, questions, answer keys, leaf selections, ethics/privacy rules, sample-size simulation, recruitment window, random seed, scoring, exclusions, harm margins, multiplicity, and interval rules are not frozen. The lj/nj package remains held at this authority cutoff. Semantic priority review covers 454 records: 334 raw accepted preserve candidates, 120 raw hold records preserved, and 2,737 gap records unreviewed.

Nothing here mutates German authority, Latin/Cyrillic readers, translation bytes, releases, or publication-owner custody. Validator PASS proves artifact consistency only.
"""


def make_readme() -> str:
    return r"""# `preregistration_v002`

Bounded, fail-closed successor for the proposed Noether/Interslavic marginal-intelligibility Stage-0 study. It is an internal design and provenance package, not recruitment authorization, human evidence, a canonical-language claim, or a publication payload.

Core files are deterministically generated by `build_isv_mi_preregistration_v002.py`. The independent validator imports no builder code. Hostile tests cover duplicate JSON keys, path escape, hash drift, authority substitution, false readiness, missing macrobranch leaf slots, cyclic-DAG substitution, unexpected files, and reparse points. Reproducibility uses a separate temporary output and exact byte comparison.

Safe validation (no writes):

```powershell
python validate_isv_mi_preregistration_v002.py --workspace-root C:\Users\user\Documents\interlanguage
```

The package remains launch-blocked even when technical validation passes. See `PROTOCOL_V002.md` and the machine-readable launch gates.
"""


def make_hostile_metadata() -> dict[str, Any]:
    cases = [
        ("HOSTILE-001", "duplicate_key", "strict JSON duplicate-key rejection"),
        ("HOSTILE-002", "path_escape", "workspace-relative path confinement"),
        ("HOSTILE-003", "hash_drift", "exact SHA-256 repin"),
        ("HOSTILE-004", "authority_substitution", "v047/ED0011 authority binding"),
        ("HOSTILE-005", "false_readiness", "launch-ready and human-evidence falsehood rejection"),
        ("HOSTILE-006", "missing_macrobranch_leaf", "exact two slots per macrobranch"),
        ("HOSTILE-007", "cyclic_DAG_substitution", "independent graph cycle detection"),
        ("HOSTILE-008", "unexpected_file", "exact package-tree closure after seal"),
        ("HOSTILE-009", "reparse_point", "reparse/symlink package-member rejection"),
    ]
    return {"schema_id": "slisv-isv-mi-preregistration-v002-hostile-fixtures", "recorded_at": RECORDED_AT, "canonical_artifacts_mutated": False, "cases": [{"case_id": cid, "mutation": mutation, "expected": "reject", "contract": contract} for cid, mutation, contract in cases]}


def write_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def core_outputs() -> dict[str, bytes]:
    protocol = make_protocol()
    values: dict[str, str] = {
        "ISV_MI_PREREGISTRATION_V002.json": json.dumps(protocol, ensure_ascii=False, indent=2) + "\n",
        "ISV_MI_PREREGISTRATION_V002.schema.json": json.dumps(make_schema(), ensure_ascii=False, indent=2) + "\n",
        "INPUT_REPIN_AUDIT_V002.json": json.dumps(make_audit(), ensure_ascii=False, indent=2) + "\n",
        "STAGE0_DESIGN_V002.csv": make_csv(protocol),
        "PROTOCOL_V002.md": make_protocol_md(protocol),
        "README.md": make_readme(),
        "HOSTILE_FIXTURES_V002.json": json.dumps(make_hostile_metadata(), ensure_ascii=False, indent=2) + "\n",
    }
    return {name: text.encode("utf-8") for name, text in values.items()}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace-root", type=Path, default=DEFAULT_WORKSPACE)
    parser.add_argument("--output-root", type=Path, default=DEFAULT_WORKSPACE / PACKAGE_REL)
    parser.add_argument("--write", action="store_true", help="write deterministic core outputs; without this flag perform no writes")
    args = parser.parse_args()
    workspace = args.workspace_root.resolve()
    for pin in PINS:
        verify_input_pin(workspace, pin)
    outputs = core_outputs()
    root = args.output_root.resolve()
    if args.write:
        root.mkdir(parents=True, exist_ok=True)
        for name, payload in outputs.items():
            (root / name).write_bytes(payload)
    else:
        missing = [name for name in outputs if not (root / name).is_file()]
        if missing:
            raise SystemExit(f"no-write check found missing outputs: {missing}")
        drift = [name for name, payload in outputs.items() if (root / name).read_bytes() != payload]
        if drift:
            raise SystemExit(f"no-write check found byte drift: {drift}")
    summary = {"status": "PASS", "write_performed": bool(args.write), "input_pins": len(PINS), "core_outputs": len(outputs), "output_root": root.as_posix()}
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
