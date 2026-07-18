from __future__ import annotations

import csv
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
ROMANCE = ROOT.parent
MANAGER = ROMANCE / "00_lane_control"
REPORTS = ROMANCE / "_agent_reports"
QA = ROOT / "qa"
WORKSPACE = ROOT.parents[3]

COHORT_IDS = [
    "C-ES-STD", "C-FR-STD", "C-PT-STD", "C-GL-STD", "C-CA-STD",
    "C-IT-STD", "C-RO-STD", "C-RM-RG", "C-RM-ID",
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def jread(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def run_python(path: Path) -> None:
    completed = subprocess.run(
        [sys.executable, "-W", "error", str(path)],
        cwd=path.parent,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    assert completed.returncode == 0, (
        path,
        completed.stdout[-4000:],
        completed.stderr[-4000:],
    )


def graph_metrics(wordweb: dict) -> tuple[int, int, int, int]:
    valid_ids = (
        {core["term_id"] for core in wordweb["core_concepts"]}
        | {sense["sense_id"] for sense in wordweb["senses"]}
        | {node["concept_id"] for node in wordweb["c2_extension_nodes"]}
    )
    relations = [relation for core in wordweb["core_concepts"] for relation in core["relations"]]
    assert all(not relation.get("target_id") or relation["target_id"] in valid_ids for relation in relations)
    target_edges = sum(bool(relation.get("target_id")) for relation in relations)
    memberships = sum(len(core["sense_ids"]) for core in wordweb["core_concepts"])
    return len(relations), target_edges, memberships, target_edges + memberships


def csv_scalar(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)


# Re-run every current deterministic producer/validator that feeds the gate.
for script in (
    MANAGER / "validate_manager_control_v2.py",
    ROOT / "scripts" / "build_consolidated_corpus_v3.py",
    ROOT / "scripts" / "build_branch_routing_ledger_v2.py",
    ROOT / "scripts" / "validate_corpus_branch_package_v1.py",
    ROOT / "scripts" / "review_occurrences_t31_t40_v1.py",
    ROOT / "scripts" / "build_wordweb_and_access_v8.py",
    ROOT / "scripts" / "extract_wordweb_occurrences_v2.py",
    ROOT / "R823_HG_T001" / "scripts" / "validate_t001.py",
    ROOT / "R823_HG_T002" / "scripts" / "validate_t002.py",
    ROOT / "R823_HG_T003" / "scripts" / "validate_t003.py",
    ROOT / "R823_HG_T004" / "scripts" / "validate_t004.py",
    ROOT / "scripts" / "verify_pdf_renders_v8.py",
):
    run_python(script)

# Canonical manager control: exactly nine cohorts, with v1 retained as history.
tree = jread(MANAGER / "ROMANCE_FAMILY_COHORT_TREE_v2.json")
manager_validation = jread(MANAGER / "ROMANCE_MANAGER_CONTROL_VALIDATION_20260717.json")
manager_manifest = read_csv(MANAGER / "ROMANCE_MANAGER_CONTROL_SHA256SUMS.csv")
manager_readme = (MANAGER / "ROMANCE_MANAGER_README_20260717.md").read_text(encoding="utf-8")
tree_ids = [cohort["cohort_id"] for cohort in tree["reader_cohorts"]]
root_ids = [leaf for branch in tree["root"]["children"] for leaf in branch["children"]]
assert tree["artifact"] == "ROMANCE_FAMILY_COHORT_TREE_v2"
assert tree["supersedes"] == "ROMANCE_FAMILY_COHORT_TREE_v1"
assert tree["cohort_count"] == len(tree_ids) == len(set(tree_ids)) == 9
assert tree_ids == COHORT_IDS and set(root_ids) == set(COHORT_IDS)
assert tree["romansh_distinction"]["current_human_observations"] == 0
assert tree["dependence_policy"]["MII_result_feeds_decisions"] is False
assert "canonical nine-reader-cohort" in manager_readme
assert "zero human observations" in manager_readme
assert manager_validation["pass"] is True
assert manager_validation["canonical_family_tree"] == "ROMANCE_FAMILY_COHORT_TREE_v2.json"
assert manager_validation["cohort_ids_actual"] == COHORT_IDS
assert manager_validation["current_human_observations"] == 0
assert all(manager_validation["semantic_checks"].values())
assert all(manager_validation["structural_checks"].values())
assert [row["path"] for row in manager_manifest] == manager_validation["sha_manifest_design"]["managed_artifacts"]
assert len(manager_manifest) == 9
for row in manager_manifest:
    path = MANAGER / row["path"]
    assert path.exists() and path.stat().st_size == int(row["bytes"]) and sha(path) == row["sha256"].upper()

# Corpus v3 and explicit branch routing v2.
corpus_path = ROOT / "corpus" / "ROMANCE_CONSOLIDATED_CORPUS_v3.csv"
corpus = read_csv(corpus_path)
corpus_summary = jread(ROOT / "corpus" / "ROMANCE_CONSOLIDATED_CORPUS_v3.json")
coverage = read_csv(ROOT / "corpus" / "ROMANCE_CORPUS_LANGUAGE_DOMAIN_COVERAGE_v3.csv")
excluded = read_csv(ROOT / "corpus" / "ROMANCE_CORPUS_REJECTED_OR_EXCLUDED_v3.csv")
routes = read_csv(ROOT / "corpus" / "ROMANCE_BRANCH_ROUTING_LEDGER_v2.csv")
assert len(corpus) == len({row["record_id"] for row in corpus}) == 148
assert sum(row["dedupe_status"] == "primary_unique" for row in corpus) == 142
assert sum(row["counting_eligible"] == "true" for row in corpus) == 66
assert len(excluded) == corpus_summary["excluded_count"] == 5
assert len(coverage) == 9 and corpus_summary["record_count"] == 148
assert corpus_summary["primary_unique_count"] == 142
assert corpus_summary["manifest_sha256"] == sha(corpus_path)
assert all(row["term_promotion_eligible"] == "false" for row in corpus)
for row in corpus:
    original = Path(row["absolute_path"])
    assert original.exists() and original.stat().st_size == int(row["bytes"])
    assert sha(original) == row["sha256"].upper()
    if row["counting_eligible"] == "true":
        search = Path(row["search_text_path"])
        assert search.exists() and sha(search) == row["search_text_sha256"].upper()
rm_rows = [row for row in corpus if row["language"] == "rm" and row["counting_eligible"] == "true"]
assert len(rm_rows) == 3 and {row["variety_code"] for row in rm_rows} == {"rm-rg"}
assert {row["record_id"] for row in rm_rows} == {
    "CURATED-RM-RG-GRCH-AP1G-2021-M1",
    "CURATED-RM-RG-GRCH-AP1G-2024-M1",
    "CURATED-RM-RG-GRCH-AP1G-2024-M2",
}
assert all(row["license_status"] == "unresolved_no_explicit_reuse_grant" for row in rm_rows)
assert all(not re.search(r"algebra|ring|field|module|group", row["domain"], re.I) for row in rm_rows)
rm_coverage = next(row for row in coverage if row["language"] == "rm")
assert rm_coverage["counting_eligible"] == "3" and rm_coverage["body_status"] == "substantive_body_present"
assert len(routes) == 61 and len({row["route_id"] for row in routes}) == 61
assert sum(int(row["current_active_body_count"]) > 0 for row in routes) == 8
assert sum(int(row["current_active_body_count"]) == 0 for row in routes) == 53
assert all(row["dominant_standard_not_proxy"] == "true" for row in routes)
rm_route = next(row for row in routes if row["variety_code"] == "rm-rg")
assert rm_route["current_active_body_count"] == rm_route["current_general_school_math_body_count"] == "3"
assert rm_route["current_specialist_algebra_body_count"] == "0"
assert rm_route["inherited_form_attestation_count"] == "0"
assert rm_route["inherited_forms_are_corpus_attestation"] == "false"
assert "specialist algebra remains a zero-body gap" in rm_route["notes"]
assert rm_route["corpus_manifest_sha256"] == sha(corpus_path)
rm_idiom_routes = [row for row in routes if row["subbranch"] == "Romansh" and row["variety_code"] != "rm-rg"]
assert len(rm_idiom_routes) == 5 and all(row["current_active_body_count"] == "0" for row in rm_idiom_routes)
corpus_audit = jread(QA / "CORPUS_BRANCH_PACKAGE_AUDIT_v1.json")
assert corpus_audit["status"] == "PASS"
assert corpus_audit["counts"] == {
    "records": 148, "primary_unique": 142, "representation_aliases": 6,
    "counting_eligible": 66, "excluded": 5, "coverage_rows": 9,
    "routes": 61, "active_routes": 8, "zero_routes": 53,
    "rm_counting_eligible": 3, "rm_general_school_math": 3,
    "rm_specialist_algebra": 0, "rm_inherited_form_attestation": 0,
    "rm_regional_idiom_active_bodies": 0,
}
assert all(check["pass"] for check in corpus_audit["checks"])

# Review event math is derived from row-level judgments, not copied from summaries.
review_specs = (
    ("T01_T10", 117, Counter({"accepted_sense_match": 84, "rejected_adverse_or_wrong_sense": 33})),
    ("T11_T20", 111, Counter({"accepted_sense_match": 90, "rejected_adverse_or_wrong_sense": 10, "held_insufficient_context_or_unmodeled_sense": 11})),
    ("T21_T30", 131, Counter({"accepted_sense_match": 64, "rejected_adverse_or_wrong_sense": 58, "held_insufficient_context_or_unmodeled_sense": 9})),
)
reviewed_ids: set[str] = set()
derived_support = derived_adverse = derived_held = 0
for label, expected_rows, expected_counts in review_specs:
    rows = read_csv(ROOT / "wordweb" / f"ROMANCE_OCCURRENCE_REVIEW_{label}_v1.csv")
    counts = Counter(row["semantic_review_status"] for row in rows)
    assert len(rows) == expected_rows and len({row["occurrence_id"] for row in rows}) == expected_rows
    assert counts == expected_counts and not (reviewed_ids & {row["occurrence_id"] for row in rows})
    reviewed_ids.update(row["occurrence_id"] for row in rows)
    derived_support += counts["accepted_sense_match"]
    derived_adverse += counts["rejected_adverse_or_wrong_sense"]
    derived_held += counts["held_insufficient_context_or_unmodeled_sense"]
review_31_rows = read_csv(ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_T31_T40_v1.csv")
review_31 = jread(ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_T31_T40_v1.json")
review_31_counts = Counter(row["review_decision"] for row in review_31_rows)
assert len(review_31_rows) == len({row["occurrence_id"] for row in review_31_rows}) == 83
assert not (reviewed_ids & {row["occurrence_id"] for row in review_31_rows})
assert review_31_counts == Counter({"accepted_sense_match": 63, "rejected_adverse": 4, "rejected_wrong_sense": 4, "held": 12})
assert review_31["scope"]["T34_zero_raw_hit"] is True
assert review_31["zero_accepted_senses"] == [
    "T31-S2", "T31-S3", "T33-S1", "T33-S3", "T34-S1", "T35-S1", "T35-S3", "T37-S2"
]
assert all(row["promotion_status"] == "not_promoted" and row["human_observation_count"] == "0" and row["pilot_claim"] == "False" for row in review_31_rows)
reviewed_ids.update(row["occurrence_id"] for row in review_31_rows)
derived_support += review_31_counts["accepted_sense_match"]
derived_adverse += review_31_counts["rejected_adverse"] + review_31_counts["rejected_wrong_sense"]
derived_held += review_31_counts["held"]
rm_review = jread(ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_RM_RG_SOURCE_v1.json")
assert rm_review["unique_occurrences"] == 2 and rm_review["sense_judgments"] == 3
assert (rm_review["accepted_sense_matches"], rm_review["rejected_adverse_or_wrong_sense"]) == (2, 1)
assert rm_review["core_form_promotions"] == rm_review["human_observations"] == 0
derived_reviewed = len(reviewed_ids) + rm_review["unique_occurrences"]
derived_support += rm_review["accepted_sense_matches"]
derived_adverse += rm_review["rejected_adverse_or_wrong_sense"]
assert (derived_reviewed, derived_support, derived_adverse, derived_held) == (444, 303, 110, 32)
protocol = (ROOT / "wordweb" / "OCCURRENCE_REVIEW_PROTOCOL_v1.md").read_text(encoding="utf-8")
assert "T01–T40" in protocol and "next contiguous cursor is T41" in protocol
assert "Human-observation count" in protocol and "count are all zero" in protocol

# WordWeb v8: semantic successor, still hypotheses rather than a human result.
ww7 = jread(ROOT / "wordweb" / "PAN_ROMANCE_WORDWEB_v7.json")
ww8 = jread(ROOT / "wordweb" / "PAN_ROMANCE_WORDWEB_v8.json")
assert ww8["artifact"] == "PAN_ROMANCE_WORDWEB_v8"
assert ww8["supersedes_for_semantic_use"] == "PAN_ROMANCE_WORDWEB_v7"
assert ww8["core_concept_count"] == 60 and ww8["sense_count"] == 106
assert len(ww8["decisions"]) == 106 and ww8["evidence_record_count"] == len(ww8["evidence_records"]) == 564
assert graph_metrics(ww7) == graph_metrics(ww8) == (402, 27, 106, 133)
assert ww8["relation_metrics"]["relation_records"] == 402
assert ww8["relation_metrics"]["valid_target_id_edges"] == 27
assert ww8["relation_metrics"]["concept_to_sense_membership_edges"] == 106
assert ww8["relation_metrics"]["total_id_resolved_references_including_memberships"] == 133
assert [core["forms"] for core in ww8["core_concepts"]] == [core["forms"] for core in ww7["core_concepts"]]
assert ww8["c2_extension_nodes"] == ww7["c2_extension_nodes"]
assert [decision["candidate_surfaces"] for decision in ww8["decisions"]] == [decision["candidate_surfaces"] for decision in ww7["decisions"]]
assert all(record["quote"] is None and record["acceptance"] == "unresolved_locator" for record in ww8["evidence_records"][:120])
labels = {sense["sense_id"]: sense["sense_label"] for sense in ww8["senses"]}
assert {key: labels[key] for key in ("T51-S1", "T51-S2", "T51-S3", "T51-S4")} == {
    "T51-S1": "function_domain", "T51-S2": "integral_domain",
    "T51-S3": "generic_domain_or_region", "T51-S4": "coefficient_domain_linkage",
}
assert {key: labels[key] for key in ("T60-S1", "T60-S2", "T60-S3", "T60-S4")} == {
    "T60-S1": "neutral_or_identity_element", "T60-S2": "identity_map",
    "T60-S3": "algebraic_identity", "T60-S4": "unit_or_invertible_element",
}
boundary = ww8["core_evidence_boundary"]
assert boundary["inherited_es_fr_core_records"] == 120 and boundary["inherited_core_quotation_count"] == 0
assert (boundary["reviewed_occurrence_records"], boundary["reviewed_supporting_status_events"], boundary["reviewed_adverse_or_rejected_status_events"], boundary["reviewed_held_status_events"]) == (444, 303, 110, 32)
assert boundary["contiguous_reviewed_terms"] == "T01-T40"
assert boundary["explicit_zero_hit_terms"] == ["T11", "T34"]
assert boundary["extension_context_to_core_promotions"] == boundary["core_form_promotions"] == boundary["human_observations"] == 0
assert "next_contiguous_T41" in ww8["occurrence_review_cursor"]

# Access v8 is the exact 106-by-9 ledger and the CSV is a semantic mirror.
access = jread(ROOT / "access" / "PAN_ROMANCE_ACCESS_LEDGER_v8.json")
access_csv = read_csv(ROOT / "access" / "PAN_ROMANCE_ACCESS_LEDGER_v8.csv")
assert access["artifact"] == "PAN_ROMANCE_ACCESS_LEDGER_v8" and access["method"] == "MII_METHOD_v8"
assert [cohort["cohort_id"] for cohort in access["cohorts"]] == COHORT_IDS
assert access["sense_count"] == 106 and access["row_count"] == len(access["rows"]) == len(access_csv) == 954
assert access["human_observation_count"] == access["pilot_eligible_count"] == 0
assert len({(row["sense_id"], row["cohort_id"]) for row in access["rows"]}) == 954
human_fields = ["human_n", "human_correct", "human_incorrect", "human_abstain", "human_latency_ms", "human_confidence", "effect_interval"]
assert all(all(row[field] is None for field in human_fields) and row["pilot_eligible"] is False for row in access["rows"])
assert list(access["rows"][0]) == list(access_csv[0])
for json_row, csv_row in zip(access["rows"], access_csv, strict=True):
    assert {key: csv_scalar(value) for key, value in json_row.items()} == csv_row
method = (ROOT / "access" / "MII_METHOD_v8.md").read_text(encoding="utf-8")
method_flat = re.sub(r"\s+", " ", method)
assert "106 × 9 = 954" in method_flat and "zero human observations" in method_flat
assert "no numeric MII proxy may promote" in method_flat and "next T41" in method_flat
assert "frozen" in method_flat and "2024" in method_flat and "does not cover" in method_flat

# Corpus-v3 successor extraction is a separate unpromoted candidate layer.
occurrence_v2 = jread(ROOT / "wordweb" / "ROMANCE_TERM_OCCURRENCES_v2.json")
occurrence_v2_rows = read_csv(ROOT / "wordweb" / "ROMANCE_TERM_OCCURRENCES_v2.csv")
assert occurrence_v2["artifact"] == "ROMANCE_TERM_OCCURRENCES_v2"
assert occurrence_v2["occurrence_count"] == len(occurrence_v2_rows) == 682
assert occurrence_v2["new_vs_v1_count"] == 3 and occurrence_v2["removed_vs_v1_count"] == 0
assert occurrence_v2["languages"]["rm"] == 5
assert set(occurrence_v2["new_vs_v1_record_ids"]) == {
    "CURATED-RM-RG-GRCH-AP1G-2024-M1", "CURATED-RM-RG-GRCH-AP1G-2024-M2"
}
new_occurrence_rows = [row for row in occurrence_v2_rows if row["occurrence_id"] in occurrence_v2["new_vs_v1_occurrence_ids"]]
assert len(new_occurrence_rows) == 3 and {row["term_id"] for row in new_occurrence_rows} == {"T39", "T45"}
assert all(row["sense_review_status"] == "unreviewed_context_window" and row["acceptance"] == "candidate_not_promoted" for row in new_occurrence_rows)
assert all(row["human_observation_count"] == "0" and row["pilot_claim"] == "False" for row in occurrence_v2_rows)
assert occurrence_v2["sense_reviewed"] == occurrence_v2["promotion_eligible"] == occurrence_v2["human_observation_count"] == 0
assert occurrence_v2["pilot_claim"] is False

# T001–T004 local validators must bind every source/control/render input they claim.
validation_paths = {
    "R823_HG_T001": {
        "authority_body_slice_sha256": "source/R823_HG_T001_de_exact.tex",
        "authority_metadata_slice_sha256": "source/R823_HG_T001_de_metadata_exact.tex",
        "source_manifest_sha256": "source/R823_HG_T001_SOURCE_MANIFEST.json",
        "target_tex_sha256": "tex/R823_HG_T001_romance.tex",
        "pdf_sha256": "build/R823_HG_T001_romance.pdf",
        "clause_map_sha256": "semantic/R823_HG_T001_clause_map.csv",
        "terminology_sha256": "terminology/R823_HG_T001_TERMINOLOGY_v1.csv",
        "grammar_sha256": "grammar/CONTROLLED_ROMANCE_GRAMMAR_TEST_v1.csv",
        "extracted_text_sha256": "qa/R823_HG_T001_extracted.txt",
        "pdfinfo_sha256": "qa/R823_HG_T001_pdfinfo.txt",
        "validator_sha256": "scripts/validate_t001.py",
    },
    "R823_HG_T002": {
        "authority_slice_sha256": "source/R823_HG_T002_de_exact.tex",
        "source_manifest_sha256": "source/R823_HG_T002_SOURCE_MANIFEST.json",
        "target_tex_sha256": "tex/R823_HG_T002_romance.tex",
        "pdf_sha256": "build/R823_HG_T002_romance.pdf",
        "clause_map_sha256": "semantic/R823_HG_T002_clause_map.csv",
        "terminology_sha256": "terminology/R823_HG_T002_TERMINOLOGY_v1.csv",
        "extracted_text_sha256": "qa/R823_HG_T002_extracted.txt",
        "pdfinfo_sha256": "qa/R823_HG_T002_pdfinfo.txt",
        "validator_sha256": "scripts/validate_t002.py",
    },
    "R823_HG_T003": {
        "authority_slice_sha256": "source/R823_HG_T003_de_exact.tex",
        "source_manifest_sha256": "source/R823_HG_T003_SOURCE_MANIFEST.json",
        "target_tex_sha256": "tex/R823_HG_T003_romance.tex",
        "pdf_sha256": "build/R823_HG_T003_romance.pdf",
        "clause_map_sha256": "semantic/R823_HG_T003_clause_map.csv",
        "terminology_sha256": "terminology/R823_HG_T003_TERMINOLOGY_v1.csv",
        "grammar_delta_sha256": "grammar/CONTROLLED_ROMANCE_GRAMMAR_T003_DELTA_v1.csv",
        "extracted_text_sha256": "qa/R823_HG_T003_extracted.txt",
        "pdfinfo_sha256": "qa/R823_HG_T003_pdfinfo.txt",
        "validator_sha256": "scripts/validate_t003.py",
    },
    "R823_HG_T004": {
        "authority_slice_sha256": "source/R823_HG_T004_de_exact.tex",
        "source_manifest_sha256": "source/R823_HG_T004_SOURCE_MANIFEST.json",
        "target_tex_sha256": "tex/R823_HG_T004_romance.tex",
        "pdf_sha256": "build/R823_HG_T004_romance.pdf",
        "clause_seed_sha256": "semantic/R823_HG_T004_clause_map_seed.csv",
        "clause_map_sha256": "semantic/R823_HG_T004_clause_map.csv",
        "terminology_sha256": "terminology/R823_HG_T004_TERMINOLOGY_v1.csv",
        "grammar_delta_sha256": "grammar/CONTROLLED_ROMANCE_GRAMMAR_T004_DELTA_v1.csv",
        "extracted_text_sha256": "qa/R823_HG_T004_extracted.txt",
        "pdfinfo_sha256": "qa/R823_HG_T004_pdfinfo.txt",
        "validator_sha256": "scripts/validate_t004.py",
    },
}
validations: dict[str, dict] = {}
for tranche, mapping in validation_paths.items():
    validation = jread(ROOT / tranche / "qa" / f"{tranche}_validation.json")
    validations[tranche] = validation
    assert validation["status"] == "PASS"
    for key, relative in mapping.items():
        assert validation[key] == sha(ROOT / tranche / relative), (tranche, key)
    assert validation["human_validation_rows"] == 0 and validation["pilot_claim"] is False
    build_pdf = ROOT / tranche / "build" / f"{tranche}_romance.pdf"
    output_pdf = WORKSPACE / "output" / "pdf" / f"{tranche}_controlled_romance.pdf"
    assert build_pdf.read_bytes() == output_pdf.read_bytes()
assert validations["R823_HG_T001"]["solidus_tokens_total"] == validations["R823_HG_T001"]["date_ranges_exempted"] == 2
assert validations["R823_HG_T001"]["lexical_alternative_bundles_in_running_prose"] == 0
assert all(validations["R823_HG_T002"][key] for key in ("all_source_segments_accounted", "c_and_C_case_distinction_retained", "exact_conjugation_formula_present"))
assert all(validations["R823_HG_T003"][key] for key in ("all_source_segments_accounted", "direct_action_order_present", "reciprocal_action_order_present", "zero_annihilator_conditions_present"))
assert all(validations["R823_HG_T004"][key] for key in ("all_source_segments_accounted", "uniqueness_scope_locked_to_representation_class", "self_map_without_surjectivity_claim", "composition_order_c1c2_present", "ring_image_map_distinction_present", "basis_matrix_bijection_present"))
assert [validations[key]["next_source_line"] for key in ("R823_HG_T002", "R823_HG_T003", "R823_HG_T004")] == [21099, 21117, 21148]
warning_pattern = re.compile(r"Overfull|Underfull|Missing character|LaTeX Warning|Package .* Warning", re.I)
for tranche in validation_paths:
    log = ROOT / tranche / "build" / f"{tranche}_lualatex_console.log"
    assert not warning_pattern.search(log.read_text(encoding="utf-8", errors="replace"))

# Official render verifier now spans T001 through current and output-copy equality.
render = jread(QA / "PDF_RENDER_REPRODUCIBILITY_v8.json")
assert render["status"] == "PASS" and render["renderer"]["render_dpi"] == 150
assert [item["tranche"] for item in render["tranches"]] == ["R823_HG_T001", "R823_HG_T002", "R823_HG_T003", "R823_HG_T004"]
assert [item["expected_page_count"] for item in render["tranches"]] == [3, 2, 2, 2]
assert render["totals"]["all_build_output_pdfs_byte_identical"] is True
assert render["totals"]["all_fresh_pinned_pngs_byte_identical"] is True
t002_render = next(item for item in render["tranches"] if item["tranche"] == "R823_HG_T002")
assert t002_render["pages"][1]["first_nonwhite_row"] == 299
for item in render["tranches"]:
    tranche = item["tranche"]
    build_pdf = ROOT / tranche / "build" / f"{tranche}_romance.pdf"
    output_pdf = WORKSPACE / "output" / "pdf" / f"{tranche}_controlled_romance.pdf"
    assert item["build_pdf"]["sha256"] == sha(build_pdf)
    assert item["final_output_pdf"]["sha256"] == sha(output_pdf) == item["build_pdf"]["sha256"]
    assert item["build_output_binding"]["sha256_match"] is True
    assert item["build_output_binding"]["byte_identical"] is True
    for page in item["pages"]:
        pinned = ROOT / tranche / "qa" / "rendered" / f"{tranche}_page-{page['page']}.png"
        assert page["hash_match"] is True and page["byte_identical"] is True
        assert page["pinned_render"]["sha256"] == page["fresh_render_sha256"] == sha(pinned)

# V7 remains an immutable predecessor, never silently amended into the current gate.
assert sha(QA / "ROMANCE_ACCEPTANCE_GATE_v7.json") == "8DC965DE36B05EDE77A9BFD3166C09D8D1CA7BB7635930067B4A658426300724"
assert sha(QA / "SHA256SUMS_v7.csv") == "5DE7FA537695265AC6B3D0CF88C9F1B803A196E4F9E85BE37E5062DD5E565A16"
assert sha(REPORTS / "romance_acceptance_reaudit_v7.md") == "F4E22B2DA983A83705009D995DEFF6FD3D2072FBEC52F9894B9C75A05913030A"

# Recompute every predecessor dependency at current bytes, then add all v8 inputs.
hash_targets: dict[str, Path] = {}
for row in read_csv(QA / "SHA256SUMS_v7.csv"):
    hash_targets[row["relative_path"]] = (ROOT / row["relative_path"]).resolve()
additions = {
    "qa/ROMANCE_ACCEPTANCE_GATE_v7.json": QA / "ROMANCE_ACCEPTANCE_GATE_v7.json",
    "qa/SHA256SUMS_v7.csv": QA / "SHA256SUMS_v7.csv",
    "qa/ROMANCE_ACCEPTANCE_GATE_v7.log": QA / "ROMANCE_ACCEPTANCE_GATE_v7.log",
    "../_agent_reports/romance_acceptance_reaudit_v7.md": REPORTS / "romance_acceptance_reaudit_v7.md",
    "../_agent_reports/review_t31_t35.md": REPORTS / "review_t31_t35.md",
    "../_agent_reports/review_t36_t40.md": REPORTS / "review_t36_t40.md",
    "../_agent_reports/t004_source_semantic_visual_audit.md": REPORTS / "t004_source_semantic_visual_audit.md",
    "_agent_reports/corpus_v3_branch_v2_audit.md": ROOT / "_agent_reports" / "corpus_v3_branch_v2_audit.md",
    "corpus/CURATED_EXTERNAL_SOURCE_MANIFEST_v2.csv": ROOT / "corpus" / "CURATED_EXTERNAL_SOURCE_MANIFEST_v2.csv",
    "corpus/ROMANCE_CONSOLIDATED_CORPUS_v3.csv": corpus_path,
    "corpus/ROMANCE_CONSOLIDATED_CORPUS_v3.json": ROOT / "corpus" / "ROMANCE_CONSOLIDATED_CORPUS_v3.json",
    "corpus/ROMANCE_CORPUS_LANGUAGE_DOMAIN_COVERAGE_v3.csv": ROOT / "corpus" / "ROMANCE_CORPUS_LANGUAGE_DOMAIN_COVERAGE_v3.csv",
    "corpus/ROMANCE_CORPUS_REJECTED_OR_EXCLUDED_v3.csv": ROOT / "corpus" / "ROMANCE_CORPUS_REJECTED_OR_EXCLUDED_v3.csv",
    "corpus/ROMANCE_BRANCH_ROUTING_LEDGER_v2.csv": ROOT / "corpus" / "ROMANCE_BRANCH_ROUTING_LEDGER_v2.csv",
    "corpus/ROMANCE_BRANCH_ROUTING_LEDGER_v2.json": ROOT / "corpus" / "ROMANCE_BRANCH_ROUTING_LEDGER_v2.json",
    "corpus/CORPUS_PROVENANCE_AND_BRANCH_ROUTING_v6.md": ROOT / "corpus" / "CORPUS_PROVENANCE_AND_BRANCH_ROUTING_v6.md",
    "scripts/build_consolidated_corpus_v3.py": ROOT / "scripts" / "build_consolidated_corpus_v3.py",
    "scripts/build_branch_routing_ledger_v2.py": ROOT / "scripts" / "build_branch_routing_ledger_v2.py",
    "scripts/validate_corpus_branch_package_v1.py": ROOT / "scripts" / "validate_corpus_branch_package_v1.py",
    "qa/CORPUS_BUILD_v3.log": QA / "CORPUS_BUILD_v3.log",
    "qa/BRANCH_ROUTING_BUILD_v2.log": QA / "BRANCH_ROUTING_BUILD_v2.log",
    "qa/CORPUS_BRANCH_PACKAGE_AUDIT_v1.json": QA / "CORPUS_BRANCH_PACKAGE_AUDIT_v1.json",
    "qa/CORPUS_BRANCH_PACKAGE_AUDIT_v1.log": QA / "CORPUS_BRANCH_PACKAGE_AUDIT_v1.log",
    "qa/CORPUS_BRANCH_TABULAR_QA_v1.json": QA / "CORPUS_BRANCH_TABULAR_QA_v1.json",
    "qa/CORPUS_BRANCH_TABULAR_QA_v1.png": QA / "CORPUS_BRANCH_TABULAR_QA_v1.png",
    "qa/RM_RG_SOURCE_VISUAL_QA_v2.md": QA / "RM_RG_SOURCE_VISUAL_QA_v2.md",
    "wordweb/ROMANCE_OCCURRENCE_REVIEW_T31_T40_v1.csv": ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_T31_T40_v1.csv",
    "wordweb/ROMANCE_OCCURRENCE_REVIEW_T31_T40_v1.json": ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_T31_T40_v1.json",
    "scripts/review_occurrences_t31_t40_v1.py": ROOT / "scripts" / "review_occurrences_t31_t40_v1.py",
    "qa/OCCURRENCE_REVIEW_T31_T40_v1.log": QA / "OCCURRENCE_REVIEW_T31_T40_v1.log",
    "wordweb/PAN_ROMANCE_WORDWEB_v8.json": ROOT / "wordweb" / "PAN_ROMANCE_WORDWEB_v8.json",
    "access/PAN_ROMANCE_ACCESS_LEDGER_v8.json": ROOT / "access" / "PAN_ROMANCE_ACCESS_LEDGER_v8.json",
    "access/PAN_ROMANCE_ACCESS_LEDGER_v8.csv": ROOT / "access" / "PAN_ROMANCE_ACCESS_LEDGER_v8.csv",
    "access/MII_METHOD_v8.md": ROOT / "access" / "MII_METHOD_v8.md",
    "scripts/build_wordweb_and_access_v8.py": ROOT / "scripts" / "build_wordweb_and_access_v8.py",
    "qa/WORDWEB_ACCESS_BUILD_v8.log": QA / "WORDWEB_ACCESS_BUILD_v8.log",
    "scripts/extract_wordweb_occurrences_v2.py": ROOT / "scripts" / "extract_wordweb_occurrences_v2.py",
    "wordweb/ROMANCE_TERM_OCCURRENCES_v2.csv": ROOT / "wordweb" / "ROMANCE_TERM_OCCURRENCES_v2.csv",
    "wordweb/ROMANCE_TERM_OCCURRENCE_COVERAGE_v2.csv": ROOT / "wordweb" / "ROMANCE_TERM_OCCURRENCE_COVERAGE_v2.csv",
    "wordweb/ROMANCE_TERM_OCCURRENCES_v2.json": ROOT / "wordweb" / "ROMANCE_TERM_OCCURRENCES_v2.json",
    "qa/TERM_OCCURRENCE_EXTRACTION_v2.log": QA / "TERM_OCCURRENCE_EXTRACTION_v2.log",
    "R823_HG_T001/qa/R823_HG_T001_extracted.txt": ROOT / "R823_HG_T001" / "qa" / "R823_HG_T001_extracted.txt",
    "R823_HG_T001/qa/R823_HG_T001_pdfinfo.txt": ROOT / "R823_HG_T001" / "qa" / "R823_HG_T001_pdfinfo.txt",
    "R823_HG_T001/qa/R823_HG_T001_validation_run_v8.log": ROOT / "R823_HG_T001" / "qa" / "R823_HG_T001_validation_run_v8.log",
    "scripts/verify_pdf_renders_v8.py": ROOT / "scripts" / "verify_pdf_renders_v8.py",
    "qa/PDF_RENDER_REPRODUCIBILITY_v8.json": QA / "PDF_RENDER_REPRODUCIBILITY_v8.json",
    "qa/PDF_VISUAL_QA_v8.md": QA / "PDF_VISUAL_QA_v8.md",
    "qa/ACCEPTANCE_MATRIX_v8.md": QA / "ACCEPTANCE_MATRIX_v8.md",
    "scripts/validate_romance_tranche_v8.py": ROOT / "scripts" / "validate_romance_tranche_v8.py",
}
for tranche in validation_paths:
    additions[f"../../../../output/pdf/{tranche}_controlled_romance.pdf"] = WORKSPACE / "output" / "pdf" / f"{tranche}_controlled_romance.pdf"
for path in sorted((ROOT / "R823_HG_T004").rglob("*")):
    if path.is_file() and path.suffix not in {".aux", ".out"} and path.name != "R823_HG_T004_romance.log":
        additions[path.relative_to(ROOT).as_posix()] = path
for directory in (
    ROOT / "corpus" / "downloaded_curated" / "rm-rg" / "gr_ch_AP1G_2024",
    QA / "rm_source_render_2024",
):
    for path in sorted(directory.rglob("*")):
        if path.is_file():
            additions[path.relative_to(ROOT).as_posix()] = path
hash_targets.update(additions)
hash_rows = []
for label, path in hash_targets.items():
    assert path.exists(), path
    hash_rows.append({"relative_path": label, "bytes": path.stat().st_size, "sha256": sha(path)})
manifest_path = QA / "SHA256SUMS_v8.csv"
with manifest_path.open("w", encoding="utf-8-sig", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=["relative_path", "bytes", "sha256"])
    writer.writeheader()
    writer.writerows(hash_rows)

gate = {
    "artifact": "ROMANCE_ACCEPTANCE_GATE_v8",
    "machine_validation": "PASS",
    "goal_status": "ACTIVE_NOT_COMPLETE",
    "predecessor_v7": {
        "status": "PRESERVED_IMMUTABLE_PREDECESSOR_ASSURANCE_SURFACE_INCOMPLETE",
        "gate_sha256": sha(QA / "ROMANCE_ACCEPTANCE_GATE_v7.json"),
        "manifest_sha256": sha(QA / "SHA256SUMS_v7.csv"),
        "independent_audit_sha256": sha(REPORTS / "romance_acceptance_reaudit_v7.md"),
    },
    "manager_control_plane": {"status": "PASS", "canonical_tree": "ROMANCE_FAMILY_COHORT_TREE_v2", "cohort_count": 9, "human_observations": 0},
    "stage_A": {
        "status": "NOT_COMPLETE",
        "explicit_routes": 61,
        "active_routes": 8,
        "zero_body_routes": 53,
        "romansh_general_school_math_bodies": 3,
        "romansh_specialist_algebra_bodies": 0,
        "romansh_regional_idiom_bodies": 0,
    },
    "stage_B": {"status": "CURRENT_CORPUS_TRANCHE_PASS", "records": 148, "primary_unique": 142, "counting_eligible": 66, "excluded": 5},
    "stage_C": {
        "status": "PARTIAL",
        "core_concepts": 60,
        "senses": 106,
        "evidence_records": 564,
        "relation_records": 402,
        "valid_target_id_relation_edges": 27,
        "concept_to_sense_membership_edges": 106,
        "total_id_resolved_references_including_memberships": 133,
        "reviewed_occurrences": 444,
        "support_events": 303,
        "adverse_or_rejected_events": 110,
        "held_events": 32,
        "occurrence_review_cursor": "T01_T40_complete_plus_RM_RG_T45_T57_next_contiguous_T41",
        "successor_occurrence_v2_candidates": 682,
        "new_2024_rm_rg_candidate_rows_pending_semantic_integration": 3,
        "human_observations": 0,
        "core_form_promotions": 0,
    },
    "stage_D": {
        "status": "T001_T004_PRODUCTION_TRANCHES_PASS_NOT_LANGUAGE_VALIDATED",
        "source_lines": {"T001": "21047-21087", "T002": "21089-21097", "T003": "21099-21115", "T004": "21117-21146"},
        "next_authority_line": 21148,
        "output_copy_exact_matches": 4,
        "render_reproducibility": "T001_T004_PASS",
        "human_validation": 0,
    },
    "canonical_cohort_topology": {"artifact": "ROMANCE_FAMILY_COHORT_TREE_v2", "cohort_count": 9, "cohort_ids": COHORT_IDS, "human_observations": 0, "MII_result_feeds_decisions": False},
    "core_evidence_boundary": {"inherited_es_fr_records": 120, "inherited_core_quotations": 0, "extension_context_to_core_promotions": 0},
    "T002_render": {"page_2_first_nonwhite_row": 299, "cap_height_clipped": False},
    "pilot_claim": False,
    "full_R823_romance_translation_claim": False,
    "hash_target_count": len(hash_rows),
    "hash_manifest_sha256": sha(manifest_path),
    "key_hashes": {row["relative_path"]: row["sha256"] for row in hash_rows},
}
(QA / "ROMANCE_ACCEPTANCE_GATE_v8.json").write_text(json.dumps(gate, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
log_lines = [
    "PASS machine_validation",
    "goal_status=ACTIVE_NOT_COMPLETE",
    "predecessor_v7=PRESERVED_IMMUTABLE_ASSURANCE_SURFACE_INCOMPLETE",
    "manager_control=PASS canonical_v2_cohorts=9 human=0",
    "stage_A=NOT_COMPLETE active_routes=8 zero_routes=53 rm_general_math=3 rm_specialist_algebra=0 rm_idioms=0",
    "stage_B=CURRENT_CORPUS_TRANCHE_PASS records=148 primary_unique=142 counting_eligible=66 excluded=5",
    "stage_C=PARTIAL concepts=60 senses=106 evidence=564 relations=402 valid_target_edges=27 memberships=106 reviewed=444 support=303 adverse=110 held=32 next=T41 human=0 promotions=0",
    "stage_D=T001_T004_PRODUCTION_TRANCHES_PASS_NOT_LANGUAGE_VALIDATED next=21148 output_copies=4 renders=9/9",
    "cohorts=9 access_rows=954 human_observations=0 MII_result_feeds_decisions=false",
    "pilot_claim=false full_R823_romance_translation_claim=false",
    f"hash_targets={len(hash_rows)} sha256_manifest={sha(manifest_path)}",
]
(QA / "ROMANCE_ACCEPTANCE_GATE_v8.log").write_text("\n".join(log_lines) + "\n", encoding="utf-8")
print("\n".join(log_lines))
