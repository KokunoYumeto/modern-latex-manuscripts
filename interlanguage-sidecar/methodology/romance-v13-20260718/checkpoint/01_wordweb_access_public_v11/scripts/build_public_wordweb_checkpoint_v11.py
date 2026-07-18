#!/usr/bin/env python3
"""Build a public-safe, rights-conservative projection of WordWeb/access v11.

The internal WordWeb remains the provenance authority.  This projection removes
source quotations, source locators, host paths, and raw source bodies while
retaining semantic structure, evidence metadata, design diagnostics, adverse
evidence classifications, and the zero-human-data claim boundary.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
from pathlib import Path


ARTIFACT = "ROMANCE_WORDWEB_ACCESS_PUBLIC_CHECKPOINT_v11"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest().upper()


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def selected(source: dict, keys: list[str]) -> dict:
    return {key: source[key] for key in keys if key in source}


FORM_KEYS = [
    "form_id",
    "language",
    "language_name",
    "surface_as_inherited",
    "lemma_candidate",
    "native_orthography_status",
    "morphology_status",
    "evidence_state",
]

RELATION_KEYS = [
    "type",
    "target_id",
    "target_label",
    "status",
    "form_languages",
    "sense_ids",
    "evidence_ids",
]

CONCEPT_KEYS = [
    "term_id",
    "concept",
    "definition",
    "sense_notes",
    "derivations",
    "proof_phrase",
    "false_friend",
    "register",
    "decision_policy",
    "domain_clusters",
    "inherited_retrieval_status",
    "status_interpretation",
    "fallback_search_candidates",
    "source_evidence_ids",
    "branch_coverage",
    "competing_forms",
    "unresolved_gaps",
    "status",
    "sense_ids",
    "reviewed_occurrence_evidence",
]

SENSE_KEYS = [
    "sense_id",
    "term_id",
    "sense_label",
    "definition",
    "domain_clusters",
    "inclusions",
    "exclusions",
    "status",
    "source_evidence_ids",
    "reviewed_supporting_occurrence_evidence_ids",
    "reviewed_adverse_occurrence_evidence_ids",
    "reviewed_held_occurrence_evidence_ids",
    "reviewed_lexical_navigation_occurrence_evidence_ids",
    "reviewed_running_body_occurrence_evidence_ids",
    "occurrence_review_status",
]

EVIDENCE_KEYS = [
    "evidence_id",
    "occurrence_id",
    "term_id",
    "language",
    "variety_code",
    "source_type",
    "origin_layer",
    "logical_source_id",
    "record_id",
    "source_sha256",
    "license_status",
    "source_candidate_sense_ids",
    "reviewed_supporting_sense_ids",
    "reviewed_adverse_to_sense_ids",
    "reviewed_held_for_sense_ids",
    "reviewed_excluded_other_sense_ids",
    "adverse_targets_all",
    "row_classification",
    "review_status_raw",
    "acceptance",
    "review_reason_code",
    "review_note",
    "review_tier",
    "evidence_context_class",
    "body_attestation_status",
    "core_form_promotion",
    "bridge_form_promotion_eligible",
    "human_observation",
    "pilot_claim",
    "quote_sha256",
    "macro_quote_sha256",
]

DECISION_KEYS = [
    "decision_id",
    "term_id",
    "sense_id",
    "sense_label",
    "policy",
    "candidate_surfaces",
    "construction_status",
    "predecessor_construction_status_v10",
    "algorithm",
    "branch_weighted_candidate_scores",
    "unadjusted_branch_scores",
    "anti_dominance_adjustments",
    "dominance_control",
    "confidence_source_occurrence",
    "confidence_sense_link",
    "confidence_bridge_decision",
    "human_validation_required",
    "pilot_eligible",
    "reviewed_supporting_occurrence_evidence_ids",
    "reviewed_adverse_occurrence_evidence_ids",
    "reviewed_held_occurrence_evidence_ids",
    "T31_T40_lexical_navigation_evidence_ids",
    "T31_T40_running_body_evidence_ids",
    "occurrence_review_status",
    "source_audit_v11_support_evidence_ids",
    "source_audit_v11_adverse_evidence_ids",
    "source_audit_v11_excluded_nearby_evidence_ids",
    "source_audit_v11_status",
]


def public_concepts(wordweb: dict) -> list[dict]:
    result = []
    for raw in wordweb["core_concepts"]:
        item = selected(raw, CONCEPT_KEYS)
        item["forms"] = [selected(form, FORM_KEYS) for form in raw.get("forms", [])]
        item["relations"] = [
            selected(relation, RELATION_KEYS) for relation in raw.get("relations", [])
        ]
        result.append(item)
    return result


def public_extensions(wordweb: dict) -> list[dict]:
    keys = [
        "concept_id",
        "concept",
        "stratum",
        "status",
        "note",
        "evidence_summary",
        "relation_to_core",
        "protected_from_general_shelf_fill",
        "forms_es",
        "forms_fr",
        "definition_status",
    ]
    result = []
    for raw in wordweb["c2_extension_nodes"]:
        item = selected(raw, keys)
        item["internal_context_evidence_count"] = len(raw.get("context_evidence", []))
        item["public_context_policy"] = (
            "counts_only; source locators and quotations excluded from this projection"
        )
        result.append(item)
    return result


def public_evidence(wordweb: dict) -> list[dict]:
    result = []
    for raw in wordweb["evidence_records"]:
        item = selected(raw, EVIDENCE_KEYS)
        item["internal_locator_available"] = bool(raw.get("locator"))
        item["internal_quote_available"] = bool(raw.get("quote"))
        result.append(item)
    return result


def build_method(cohorts: list[dict]) -> str:
    cohort_lines = "\n".join(
        f"- `{row['cohort_id']}` — {row['name']} ({row['standard']})."
        for row in cohorts
    )
    return f"""# Public marginal-access method v11

## Purpose and topology

This checkpoint implements a **design ledger**, not an intelligibility result. It contains one row for every combination of 106 semantic senses and nine declared reader cohorts: **106 × 9 = 954 rows**. There are **zero human observations**. Sense splitting is mandatory; in particular, `domain` has four senses (`T51-S1`–`T51-S4`) and `identity` has four senses (`T60-S1`–`T60-S4`).

The canonical cohort topology is:

{cohort_lines}

The regional-Romansh cohort must later name Sursilvan, Sutsilvan, Surmiran, Putèr, or Vallader. It is separate from Rumantsch Grischun; neither cohort proxies the other.

## Stored design diagnostic

The populated numeric values are deterministic orthographic comparisons. For strings `a` and `b`, normalized similarity is `1 - Levenshtein(a,b) / max(len(a),len(b))`, with the empty/empty case defined as 1. Candidate surfaces are compared with inherited cohort forms and with Spanish and French dominance carriers. Stored deltas are candidate proxy minus the corresponding dominant-standard proxy.

These values are **not** comprehension, pronunciation, semantic transparency, acceptability, processing time, or marginal intelligibility. The Boolean comparison field merely reports whether the stored orthographic proxy exceeds both dominance-carrier proxies by 0.05; it is not a successful test result.

Candidate construction uses equal total weight across five branch zones. Spanish and French receive no population bonus, and a form carried only by Spanish or only by French receives the recorded single-zone dominance penalty. Candidate scores remain hypotheses; no score promotes a controlled form.

## Evidence and adverse evidence

Every ledger row names its sense, cohort, candidates, dominant-standard comparator forms, penalties, supporting evidence IDs, adverse evidence, confidence state, and review status. Accepted sense support, wrong-sense/adverse evidence, held evidence, lexical-navigation evidence, and running-body evidence remain distinct. Evidence IDs in the public WordWeb resolve to metadata-only evidence records. Underlying quotations, locators, host paths, and raw source bodies remain internal because reuse rights are unresolved or not publication-cleared.

The 120 inherited Spanish/French core records remain unresolved locator claims with **zero quotations** and are not promoted by contextual extension-node snippets. The internal v11 layer contains 811 evidence records. Seventy-eight of 106 senses have accepted internal support; 28 remain explicit gaps. This is source-evidence coverage, not reader validation.

## Human protocol and hard gate

All seven human-result fields are null on all 954 rows, the human observation count is zero, every row and every decision has `pilot_eligible=false`, and no controlled bridge form is promoted. Therefore no MII result feeds a vocabulary or grammar decision in this checkpoint.

A future human study must record the exact cohort (and Romansh idiom where applicable), mathematical-literacy band, other Romance exposure, randomized and blinded item order, task instructions, correct/incorrect/abstain outcomes, latency, confidence, uncertainty, consent, exclusions, and review state. Only cohort-level observations with an approved analysis plan may support a marginal-gain or intelligibility statement.

## Graph boundary

The WordWeb has 406 descriptive relation records. Exactly 27 are target-ID graph edges. Adding 106 concept-to-sense memberships yields 133 ID-resolved references. It is incorrect to report all 406 relation records as graph edges.

## Publication boundary

This public projection deliberately excludes raw sources, quotations, locators, and host paths. It does not declare a license for the underlying source bodies and does not certify the controlled Romance language, a pilot, or the four-stage lane as complete.
"""


def build(project_root: Path, output: Path) -> dict:
    wordweb_path = project_root / "wordweb" / "PAN_ROMANCE_WORDWEB_v11.json"
    access_json_path = project_root / "access" / "PAN_ROMANCE_ACCESS_LEDGER_v11.json"
    access_csv_path = project_root / "access" / "PAN_ROMANCE_ACCESS_LEDGER_v11.csv"
    method_path = project_root / "access" / "MII_METHOD_v11.md"
    input_paths = {
        "PAN_ROMANCE_WORDWEB_v11": wordweb_path,
        "PAN_ROMANCE_ACCESS_LEDGER_v11_json": access_json_path,
        "PAN_ROMANCE_ACCESS_LEDGER_v11_csv": access_csv_path,
        "MII_METHOD_v11": method_path,
    }
    missing = [name for name, path in input_paths.items() if not path.is_file()]
    if missing:
        raise FileNotFoundError(f"missing inputs: {missing}")

    wordweb = json.loads(wordweb_path.read_text(encoding="utf-8"))
    access = json.loads(access_json_path.read_text(encoding="utf-8"))
    new_support = set(
        wordweb["semantic_evidence_batch_v11"]["newly_supported_senses"]
    )
    unsupported = [
        sense_id
        for sense_id in wordweb["core_evidence_boundary"][
            "zero_accepted_support_sense_ids"
        ]
        if sense_id not in new_support
    ]
    if len(unsupported) != 28:
        raise ValueError(f"expected 28 final gaps, got {len(unsupported)}")

    concepts = public_concepts(wordweb)
    senses = [selected(sense, SENSE_KEYS) for sense in wordweb["senses"]]
    extensions = public_extensions(wordweb)
    evidence = public_evidence(wordweb)
    decisions = [selected(decision, DECISION_KEYS) for decision in wordweb["decisions"]]

    projection = {
        "artifact": "PAN_ROMANCE_WORDWEB_PUBLIC_v11",
        "checkpoint": ARTIFACT,
        "derived_from": {
            "artifact": wordweb["artifact"],
            "sha256": sha256(wordweb_path),
        },
        "projection_policy": (
            "semantic structure and evidence metadata retained; quotations, source locators, "
            "host paths, raw bodies, and C2 context snippets excluded"
        ),
        "claim_boundary": (
            "Internal source evidence and orthographic diagnostics only. Zero human observations, "
            "zero pilot eligibility, zero controlled-form promotions, and no intelligibility or "
            "completion claim."
        ),
        "counts": {
            "core_concepts": len(concepts),
            "senses": len(senses),
            "extension_nodes": len(extensions),
            "evidence_metadata_records": len(evidence),
            "decisions": len(decisions),
            "supported_senses_internal": wordweb["semantic_evidence_batch_v11"][
                "supported_senses_total"
            ],
            "unsupported_senses": len(unsupported),
            "human_observations": 0,
            "controlled_form_promotions": 0,
        },
        "relation_metrics": wordweb["relation_metrics"],
        "core_evidence_boundary": {
            "inherited_es_fr_core_records": wordweb["core_evidence_boundary"][
                "inherited_es_fr_core_records"
            ],
            "inherited_core_quotation_count": wordweb["core_evidence_boundary"][
                "inherited_core_quotation_count"
            ],
            "extension_context_to_core_promotions": wordweb[
                "core_evidence_boundary"
            ]["extension_context_to_core_promotions"],
            "core_form_promotions": 0,
            "human_observations": 0,
            "pilot_or_intelligibility_claims": 0,
            "final_unsupported_sense_ids": unsupported,
        },
        "exact_sense_label_contract_T51_T60": wordweb[
            "exact_sense_label_contract_T51_T60"
        ],
        "occurrence_review_cursor": wordweb["occurrence_review_cursor"],
        "core_concepts": concepts,
        "senses": senses,
        "c2_extension_nodes": extensions,
        "evidence_metadata": evidence,
        "decisions": decisions,
    }
    write_json(output / "data" / "PAN_ROMANCE_WORDWEB_PUBLIC_v11.json", projection)

    public_access = {
        "artifact": "PAN_ROMANCE_ACCESS_LEDGER_PUBLIC_v11",
        "checkpoint": ARTIFACT,
        "derived_from": {
            "artifact": access["artifact"],
            "sha256_json": sha256(access_json_path),
            "sha256_csv": sha256(access_csv_path),
        },
        "status": access["status"],
        "claim_boundary": access["claim_boundary"],
        "method": "MII_METHOD_PUBLIC_v11",
        "canonical_cohort_topology": access["canonical_cohort_topology"],
        "cohorts": access["cohorts"],
        "sense_count": access["sense_count"],
        "row_count": access["row_count"],
        "human_observation_count": access["human_observation_count"],
        "pilot_eligible_count": access["pilot_eligible_count"],
        "form_promotion_count": access["form_promotion_count"],
        "exact_sense_label_contract_T51_T60": access[
            "exact_sense_label_contract_T51_T60"
        ],
        "source_evidence_batch_v11": access["source_evidence_batch_v11"],
        "rows": access["rows"],
    }
    write_json(
        output / "data" / "PAN_ROMANCE_ACCESS_LEDGER_PUBLIC_v11.json",
        public_access,
    )
    row_fields = list(access["rows"][0].keys())
    write_csv(
        output / "data" / "PAN_ROMANCE_ACCESS_LEDGER_PUBLIC_v11.csv",
        row_fields,
        access["rows"],
    )

    sense_by_id = {sense["sense_id"]: sense for sense in senses}
    gap_rows = [
        {
            "term_id": sense_by_id[sense_id]["term_id"],
            "sense_id": sense_id,
            "sense_label": sense_by_id[sense_id]["sense_label"],
            "definition": sense_by_id[sense_id]["definition"],
            "review_status": sense_by_id[sense_id]["occurrence_review_status"],
            "gap_interpretation": (
                "zero accepted support in the internal v11 evidence boundary; not evidence of "
                "absence from the language and not a human-access result"
            ),
        }
        for sense_id in unsupported
    ]
    write_csv(
        output / "data" / "WORDWEB_UNRESOLVED_SENSE_GAPS_v11.csv",
        list(gap_rows[0].keys()),
        gap_rows,
    )

    cohort_fields = [
        "cohort_id",
        "name",
        "languages",
        "standard",
        "math_literacy",
        "other_romance_exposure",
    ]
    cohort_rows = []
    for cohort in access["cohorts"]:
        item = selected(cohort, cohort_fields)
        item["languages"] = " | ".join(item["languages"])
        cohort_rows.append(item)
    write_csv(
        output / "data" / "ROMANCE_READER_COHORTS_v2.csv",
        cohort_fields,
        cohort_rows,
    )

    (output / "method").mkdir(parents=True, exist_ok=True)
    (output / "method" / "MII_METHOD_PUBLIC_v11.md").write_text(
        build_method(access["cohorts"]), encoding="utf-8", newline="\n"
    )

    provenance = {
        "artifact": "ROMANCE_WORDWEB_ACCESS_PUBLIC_INPUT_BINDING_v11",
        "checkpoint": ARTIFACT,
        "input_hashes": {name: sha256(path) for name, path in input_paths.items()},
        "source_rights_boundary": (
            "Underlying bodies remain internal and are not included. This hash binding does not "
            "grant or imply redistribution rights."
        ),
    }
    write_json(output / "PROVENANCE_INPUT_HASHES.json", provenance)

    readme = f"""# Romance WordWeb and marginal-access checkpoint v11

This is a public-safe projection of the internal v11 Romance semantic and access artifacts. It contains 60 concepts, 106 explicit senses, 39 extension nodes, 811 metadata-only evidence records, 106 provisional construction decisions, nine named reader cohorts, and the complete 954-row sense-by-cohort access grid.

It deliberately excludes source quotations, source locators, host paths, raw source bodies, and extension-node context snippets. Those materials remain internal because source-body reuse rights are unresolved or not publication-cleared. Evidence IDs, source hashes where available, classifications, and review notes are retained so that the semantic audit surface does not collapse into an unsupported vocabulary list.

The acceptance boundary is strict: 78 senses have accepted internal source support; 28 are explicit gaps. The 120 inherited Spanish/French core records still have zero quotations and remain unresolved. The grid has zero human observations, zero pilot-eligible rows, and zero form promotions. Orthographic values are design diagnostics only; they are not marginal-intelligibility or comprehension measurements.

The graph boundary is equally strict: 406 relation records are present, but only 27 have valid target IDs. With 106 concept-to-sense memberships, there are 133 ID-resolved references—not 406 graph edges.

## Contents

- `data/PAN_ROMANCE_WORDWEB_PUBLIC_v11.json`: semantic structure, evidence metadata, relations, and provisional decisions.
- `data/PAN_ROMANCE_ACCESS_LEDGER_PUBLIC_v11.json` and `.csv`: the complete 106 × 9 design grid.
- `data/ROMANCE_READER_COHORTS_v2.csv`: the canonical nine-cohort topology.
- `data/WORDWEB_UNRESOLVED_SENSE_GAPS_v11.csv`: the 28-sense open-evidence cursor.
- `method/MII_METHOD_PUBLIC_v11.md`: formula, cohort, evidence, and human-study gates.
- `PROVENANCE_INPUT_HASHES.json`: exact binding to the four internal v11 inputs without exposing them.
- `qa/`: deterministic validation and build evidence, added by the reproduction runner.
- `scripts/`: builder, validator, and reproduction runner.

This checkpoint is active evidence, not a complete Romance interlanguage, not an empirical MII result, and not a declaration of license for any underlying source body. Package licensing and public repository placement remain decisions for the archive maintainer.
"""
    output.mkdir(parents=True, exist_ok=True)
    (output / "README.md").write_text(readme, encoding="utf-8", newline="\n")

    script_dir = Path(__file__).resolve().parent
    (output / "scripts").mkdir(parents=True, exist_ok=True)
    for name in [
        "build_public_wordweb_checkpoint_v11.py",
        "validate_public_wordweb_checkpoint_v11.py",
        "reproduce_public_wordweb_checkpoint_v11.py",
    ]:
        source = script_dir / name
        if not source.is_file():
            raise FileNotFoundError(source)
        shutil.copyfile(source, output / "scripts" / name)

    return {
        "artifact": ARTIFACT,
        "concepts": len(concepts),
        "senses": len(senses),
        "evidence_metadata": len(evidence),
        "decisions": len(decisions),
        "access_rows": len(access["rows"]),
        "cohorts": len(access["cohorts"]),
        "unsupported_senses": len(unsupported),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = build(args.project_root.resolve(), args.output.resolve())
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
