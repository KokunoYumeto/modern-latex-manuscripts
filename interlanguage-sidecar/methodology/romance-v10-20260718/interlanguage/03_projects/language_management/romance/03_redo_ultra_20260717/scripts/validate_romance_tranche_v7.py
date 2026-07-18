from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
ROMANCE = ROOT.parent
MANAGER = ROMANCE / "00_lane_control"
QA = ROOT / "qa"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def jread(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def graph_metrics(wordweb: dict) -> tuple[int, int, int, int]:
    valid_ids = (
        {core["term_id"] for core in wordweb["core_concepts"]}
        | {sense["sense_id"] for sense in wordweb["senses"]}
        | {node["concept_id"] for node in wordweb["c2_extension_nodes"]}
    )
    relations = [relation for core in wordweb["core_concepts"] for relation in core["relations"]]
    target_edges = sum(relation.get("target_id") in valid_ids for relation in relations)
    memberships = sum(len(core["sense_ids"]) for core in wordweb["core_concepts"])
    return len(relations), target_edges, memberships, target_edges + memberships


expected_cohort_ids = [
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

# Manager control plane: v2 is canonical everywhere; v1 is only preserved history.
tree_v2 = jread(MANAGER / "ROMANCE_FAMILY_COHORT_TREE_v2.json")
manager_readme = (MANAGER / "ROMANCE_MANAGER_README_20260717.md").read_text(encoding="utf-8")
manager_validation = jread(MANAGER / "ROMANCE_MANAGER_CONTROL_VALIDATION_20260717.json")
manager_manifest = read_csv(MANAGER / "ROMANCE_MANAGER_CONTROL_SHA256SUMS.csv")
tree_ids = [cohort["cohort_id"] for cohort in tree_v2["reader_cohorts"]]
root_leaf_ids = [leaf for branch in tree_v2["root"]["children"] for leaf in branch["children"]]
assert tree_v2["artifact"] == "ROMANCE_FAMILY_COHORT_TREE_v2"
assert tree_v2["supersedes"] == "ROMANCE_FAMILY_COHORT_TREE_v1"
assert tree_v2["root"]["id"] == "romance_manager"
assert tree_v2["cohort_count"] == len(tree_ids) == len(set(tree_ids)) == 9
assert tree_ids == expected_cohort_ids and set(root_leaf_ids) == set(expected_cohort_ids)
assert tree_v2["romansh_distinction"]["current_human_observations"] == 0
assert tree_v2["dependence_policy"]["MII_result_feeds_decisions"] is False
assert "canonical nine-reader-cohort" in manager_readme
assert "ROMANCE_FAMILY_COHORT_TREE_v1.json` is retained" in manager_readme
assert "zero human observations" in manager_readme
assert manager_validation["pass"] is True
assert manager_validation["canonical_family_tree"] == "ROMANCE_FAMILY_COHORT_TREE_v2.json"
assert manager_validation["cohort_count_actual"] == 9
assert manager_validation["cohort_ids_actual"] == expected_cohort_ids
assert manager_validation["current_human_observations"] == 0
assert all(manager_validation["semantic_checks"].values())
assert all(manager_validation["structural_checks"].values())
assert manager_validation["sha_manifest_design"]["self_hash_excluded"] is True
manager_paths = [row["path"] for row in manager_manifest]
assert manager_paths == manager_validation["sha_manifest_design"]["managed_artifacts"]
assert len(manager_manifest) == 9 and "ROMANCE_FAMILY_COHORT_TREE_v2.json" in manager_paths
assert "ROMANCE_MANAGER_CONTROL_SHA256SUMS.csv" not in manager_paths
for row in manager_manifest:
    path = MANAGER / row["path"]
    assert path.exists() and path.stat().st_size == int(row["bytes"])
    assert sha(path) == row["sha256"].upper()

# Current corpus tranche and branch routing.
manifest = read_csv(ROOT / "corpus" / "WIKIMEDIA_HTML_CORPUS_MANIFEST_v1.csv")
query = read_csv(ROOT / "corpus" / "WIKIMEDIA_HTML_QUERY_LOG_v1.csv")
rejected_html = read_csv(ROOT / "corpus" / "WIKIMEDIA_HTML_REJECTED_AUTOMATIC_SEARCH_v1.csv")
manifest_qa = jread(ROOT / "corpus" / "WIKIMEDIA_HTML_MANIFEST_QA_v1.json")
corpus = read_csv(ROOT / "corpus" / "ROMANCE_CONSOLIDATED_CORPUS_v2.csv")
coverage = read_csv(ROOT / "corpus" / "ROMANCE_CORPUS_LANGUAGE_DOMAIN_COVERAGE_v2.csv")
routes = read_csv(ROOT / "corpus" / "ROMANCE_BRANCH_ROUTING_LEDGER_v1.csv")
assert len(manifest) == 42 and not any(row["language_code"] == "rm" for row in manifest)
assert not any(not row["title"].strip() or int(row["page_id"]) == 0 or int(row["revision_id"]) == 0 for row in manifest)
assert manifest_qa["historical_pre_qa_rows"] == 48 and manifest_qa["active_rows"] == 42
assert manifest_qa["romansh_downloaded"] == manifest_qa["romansh_unique_pages"] == 0
assert Counter(row["title"] for row in rejected_html) == Counter(
    {"Biologia": 2, "Tirchia": 1, "Republica Populara da la China": 1}
)
query_status = Counter(row["status"].split(":", 1)[0] for row in query if row["language"] == "rm")
assert query_status == Counter({"rejected_nonmathematical_result": 4, "no_article_result_zero_page_or_revision": 2})
assert len(corpus) == 146 and len({row["record_id"] for row in corpus}) == 146
assert sum(row["dedupe_status"] == "primary_unique" for row in corpus) == 140
assert sum(row["counting_eligible"] == "true" for row in corpus) == 64
assert all(row["term_promotion_eligible"] == "false" for row in corpus)
for row in corpus:
    original = Path(row["absolute_path"])
    assert original.exists() and original.stat().st_size == int(row["bytes"])
    assert sha(original) == row["sha256"]
    if row["counting_eligible"] == "true":
        search = Path(row["search_text_path"])
        assert search.exists() and sha(search) == row["search_text_sha256"]
rm_rows = [row for row in corpus if row["language"] == "rm" and row["counting_eligible"] == "true"]
assert len(rm_rows) == 1 and rm_rows[0]["variety_code"] == "rm-rg"
assert rm_rows[0]["domain"] == "mathematics_education"
assert rm_rows[0]["license_status"] == "unresolved_no_explicit_reuse_grant"
rm_coverage = next(row for row in coverage if row["language"] == "rm")
assert rm_coverage["counting_eligible"] == "1" and rm_coverage["body_status"] == "substantive_body_present"
assert len(routes) == 61
assert sum(int(row["current_active_body_count"]) > 0 for row in routes) == 8
assert sum(int(row["current_active_body_count"]) == 0 for row in routes) == 53
assert all(row["dominant_standard_not_proxy"] == "true" for row in routes)
rm_route = next(row for row in routes if row["variety_code"] == "rm-rg")
assert rm_route["current_active_body_count"] == "1"
assert "general school-mathematics body" in rm_route["notes"] and "specialist algebra" in rm_route["notes"]
assert sha(ROOT / "corpus" / "ROMANCE_BRANCH_ROUTING_LEDGER_v1.csv") == "7440CE0E6D4FB4CFDC33C30E704F41E301853BFC2E81E6D26550A4A6438767CF"

# Contiguous T01-T30 evidence review and v7 semantic successor.
occurrence_summary = jread(ROOT / "wordweb" / "ROMANCE_TERM_OCCURRENCES_v1.json")
review_t01 = jread(ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_T01_T10_v1.json")
review_t11 = jread(ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_T11_T20_v1.json")
review_t21 = jread(ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_T21_T30_v1.json")
review_t21_rows = read_csv(ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_T21_T30_v1.csv")
review_rm = jread(ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_RM_RG_SOURCE_v1.json")
protocol = (ROOT / "wordweb" / "OCCURRENCE_REVIEW_PROTOCOL_v1.md").read_text(encoding="utf-8")
assert occurrence_summary["occurrence_count"] == 679 and occurrence_summary["terms_with_context"] == 54
assert occurrence_summary["languages"]["rm"] == 2 and occurrence_summary["promotion_eligible"] == 0
assert (review_t01["reviewed_rows"], review_t01["accepted_sense_matches"], review_t01["rejected_adverse_or_wrong_sense"]) == (117, 84, 33)
assert (review_t11["reviewed_rows"], review_t11["accepted_sense_matches"], review_t11["rejected_adverse_or_wrong_sense"], review_t11["held_rows"]) == (111, 90, 10, 11)
assert review_t11["explicit_zero_hit_terms"] == ["T11"]
assert review_t11["bridge_form_promotions"] == review_t11["human_observations"] == 0
assert len(review_t21_rows) == len({row["occurrence_id"] for row in review_t21_rows}) == review_t21["reviewed_rows"] == 131
assert (review_t21["accepted_sense_matches"], review_t21["rejected_adverse_or_wrong_sense"], review_t21["held_rows"]) == (64, 58, 9)
assert review_t21["zero_accepted_sense_gaps"] == ["T22-S2", "T25-S2", "T26-S1"]
assert review_t21["narrow_language_coverage"] == {"T27-S1": ["es", "fr"], "T28-S1": ["es"]}
assert review_t21["bridge_form_promotions"] == review_t21["human_observations"] == 0
assert review_t21["review_manifest_sha256"] == sha(ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_T21_T30_v1.csv")
assert review_rm["unique_occurrences"] == 2 and review_rm["sense_judgments"] == 3
assert (review_rm["accepted_sense_matches"], review_rm["rejected_adverse_or_wrong_sense"]) == (2, 1)
assert review_rm["core_form_promotions"] == review_rm["human_observations"] == 0
assert "T01–T30" in protocol and "next contiguous cursor is T31" in protocol
assert "Human-observation count is zero" in protocol

ww6 = jread(ROOT / "wordweb" / "PAN_ROMANCE_WORDWEB_v6.json")
ww7 = jread(ROOT / "wordweb" / "PAN_ROMANCE_WORDWEB_v7.json")
access7 = jread(ROOT / "access" / "PAN_ROMANCE_ACCESS_LEDGER_v7.json")
assert ww7["artifact"] == "PAN_ROMANCE_WORDWEB_v7" and ww7["supersedes_for_semantic_use"] == "PAN_ROMANCE_WORDWEB_v6"
assert ww7["core_concept_count"] == 60 and ww7["sense_count"] == 106 and len(ww7["decisions"]) == 106
assert ww7["evidence_record_count"] == len(ww7["evidence_records"]) == 481
assert graph_metrics(ww6) == graph_metrics(ww7) == (402, 27, 106, 133)
assert ww7["relation_count"] == ww7["relation_metrics"]["relation_records"] == 402
assert ww7["relation_metrics"]["valid_target_id_edges"] == 27
assert ww7["relation_metrics"]["concept_to_sense_membership_edges"] == 106
assert ww7["relation_metrics"]["total_id_resolved_references_including_memberships"] == 133
assert [core["forms"] for core in ww7["core_concepts"]] == [core["forms"] for core in ww6["core_concepts"]]
assert ww7["c2_extension_nodes"] == ww6["c2_extension_nodes"]
assert [decision["candidate_surfaces"] for decision in ww7["decisions"]] == [decision["candidate_surfaces"] for decision in ww6["decisions"]]
assert all(record["quote"] is None and record["acceptance"] == "unresolved_locator" and record["language"] in {"es", "fr"} for record in ww7["evidence_records"][:120])
boundary = ww7["core_evidence_boundary"]
assert boundary["inherited_es_fr_core_records"] == 120 and boundary["inherited_core_quotation_count"] == 0
assert (boundary["reviewed_occurrence_records"], boundary["reviewed_supporting_status_events"], boundary["reviewed_adverse_or_rejected_status_events"], boundary["reviewed_held_status_events"]) == (361, 240, 102, 20)
assert boundary["contiguous_reviewed_terms"] == "T01-T30" and boundary["explicit_zero_hit_terms"] == ["T11"]
assert boundary["zero_accepted_sense_gaps_T21_T30"] == ["T22-S2", "T25-S2", "T26-S1"]
assert boundary["narrow_accepted_language_coverage"] == {"T27-S1": ["es", "fr"], "T28-S1": ["es"]}
assert boundary["extension_context_to_core_promotions"] == boundary["core_form_promotions"] == boundary["human_observations"] == 0
assert ww7["occurrence_review_cursor"].endswith("next_contiguous_T31")
t57 = next(core for core in ww7["core_concepts"] if core["term_id"] == "T57")
t57_edges = [relation for relation in t57["relations"] if relation.get("target_label") == "straight_direction_not_algebraic_right_action"]
assert len(t57_edges) == 1 and t57_edges[0]["target_id"] == "T57-S1"
for term_id in ("T51", "T60"):
    senses = [sense for sense in ww7["senses"] if sense["term_id"] == term_id]
    decisions = [decision for decision in ww7["decisions"] if decision["term_id"] == term_id]
    assert len(senses) == len(decisions) == 4 and all(not decision["candidate_surfaces"] for decision in decisions)
for sense_id in ("T22-S2", "T25-S2"):
    assert not next(decision for decision in ww7["decisions"] if decision["sense_id"] == sense_id)["candidate_surfaces"]
t26s1 = next(decision for decision in ww7["decisions"] if decision["sense_id"] == "T26-S1")
assert t26s1["candidate_surfaces"] == ["Galois"] and "not_promoted" in t26s1["construction_status"]
assert t26s1["confidence_bridge_decision"] == "hypothesis_only"

# Canonical 106x9 access implementation, still with zero human observations.
ledger_ids = [cohort["cohort_id"] for cohort in access7["cohorts"]]
assert ledger_ids == tree_ids == expected_cohort_ids
assert access7["artifact"] == "PAN_ROMANCE_ACCESS_LEDGER_v7" and access7["method"] == "MII_METHOD_v7"
assert access7["sense_count"] == 106 and access7["row_count"] == len(access7["rows"]) == 954
assert access7["canonical_cohort_topology"]["cohort_ids"] == expected_cohort_ids
assert access7["human_observation_count"] == access7["pilot_eligible_count"] == 0
pairs = {(row["sense_id"], row["cohort_id"]) for row in access7["rows"]}
assert len(pairs) == 954
assert Counter(row["sense_id"] for row in access7["rows"]) == Counter({sense["sense_id"]: 9 for sense in ww7["senses"]})
human_fields = ["human_n", "human_correct", "human_incorrect", "human_abstain", "human_latency_ms", "human_confidence", "effect_interval"]
assert all(all(row[field] is None for field in human_fields) and row["pilot_eligible"] is False for row in access7["rows"])
method_text = (ROOT / "access" / "MII_METHOD_v7.md").read_text(encoding="utf-8")
assert "106 × 9 = 954" in method_text and "zero human observations" in method_text
assert "no numeric MII proxy may promote" in method_text and "next T31" in method_text

# Source-keyed controlled-language tranches. Embedded hashes are independently recomputed.
t001 = jread(ROOT / "R823_HG_T001" / "qa" / "R823_HG_T001_validation.json")
t002 = jread(ROOT / "R823_HG_T002" / "qa" / "R823_HG_T002_validation.json")
t003 = jread(ROOT / "R823_HG_T003" / "qa" / "R823_HG_T003_validation.json")
t001_paths = {
    "source_manifest_sha256": ROOT / "R823_HG_T001" / "source" / "R823_HG_T001_SOURCE_MANIFEST.json",
    "target_tex_sha256": ROOT / "R823_HG_T001" / "tex" / "R823_HG_T001_romance.tex",
    "pdf_sha256": ROOT / "R823_HG_T001" / "build" / "R823_HG_T001_romance.pdf",
    "clause_map_sha256": ROOT / "R823_HG_T001" / "semantic" / "R823_HG_T001_clause_map.csv",
    "terminology_sha256": ROOT / "R823_HG_T001" / "terminology" / "R823_HG_T001_TERMINOLOGY_v1.csv",
    "grammar_sha256": ROOT / "R823_HG_T001" / "grammar" / "CONTROLLED_ROMANCE_GRAMMAR_TEST_v1.csv",
    "validator_sha256": ROOT / "R823_HG_T001" / "scripts" / "validate_t001.py",
}
t002_paths = {
    "authority_slice_sha256": ROOT / "R823_HG_T002" / "source" / "R823_HG_T002_de_exact.tex",
    "source_manifest_sha256": ROOT / "R823_HG_T002" / "source" / "R823_HG_T002_SOURCE_MANIFEST.json",
    "target_tex_sha256": ROOT / "R823_HG_T002" / "tex" / "R823_HG_T002_romance.tex",
    "pdf_sha256": ROOT / "R823_HG_T002" / "build" / "R823_HG_T002_romance.pdf",
    "clause_map_sha256": ROOT / "R823_HG_T002" / "semantic" / "R823_HG_T002_clause_map.csv",
    "terminology_sha256": ROOT / "R823_HG_T002" / "terminology" / "R823_HG_T002_TERMINOLOGY_v1.csv",
    "extracted_text_sha256": ROOT / "R823_HG_T002" / "qa" / "R823_HG_T002_extracted.txt",
    "pdfinfo_sha256": ROOT / "R823_HG_T002" / "qa" / "R823_HG_T002_pdfinfo.txt",
    "validator_sha256": ROOT / "R823_HG_T002" / "scripts" / "validate_t002.py",
}
t003_paths = {
    "authority_slice_sha256": ROOT / "R823_HG_T003" / "source" / "R823_HG_T003_de_exact.tex",
    "source_manifest_sha256": ROOT / "R823_HG_T003" / "source" / "R823_HG_T003_SOURCE_MANIFEST.json",
    "target_tex_sha256": ROOT / "R823_HG_T003" / "tex" / "R823_HG_T003_romance.tex",
    "pdf_sha256": ROOT / "R823_HG_T003" / "build" / "R823_HG_T003_romance.pdf",
    "clause_map_sha256": ROOT / "R823_HG_T003" / "semantic" / "R823_HG_T003_clause_map.csv",
    "terminology_sha256": ROOT / "R823_HG_T003" / "terminology" / "R823_HG_T003_TERMINOLOGY_v1.csv",
    "grammar_delta_sha256": ROOT / "R823_HG_T003" / "grammar" / "CONTROLLED_ROMANCE_GRAMMAR_T003_DELTA_v1.csv",
    "extracted_text_sha256": ROOT / "R823_HG_T003" / "qa" / "R823_HG_T003_extracted.txt",
    "pdfinfo_sha256": ROOT / "R823_HG_T003" / "qa" / "R823_HG_T003_pdfinfo.txt",
    "validator_sha256": ROOT / "R823_HG_T003" / "scripts" / "validate_t003.py",
}
for validation, paths in ((t001, t001_paths), (t002, t002_paths), (t003, t003_paths)):
    assert validation["status"] == "PASS"
    for key, path in paths.items():
        assert validation[key] == sha(path), (validation["artifact"], key)
    assert validation["human_validation_rows"] == 0 and validation["pilot_claim"] is False
assert t001["authority_body_slice_sha256"] == "33E4D17FEC404CB5B5A7DF208EE1BC5855BB6B0F4091A04905B95B75C1D9AF64"
assert t001["authority_metadata_slice_sha256"] == "D424D5D19D8B8E153B1DF736933F71B83098A5C54135646561B9E3E2C8519559"
assert (t001["clause_rows"], t001["target_ids"], t001["terminology_rows"], t001["grammar_rows"]) == (27, 34, 35, 18)
assert t001["grammar_required_features_checked"] and t001["solidus_tokens_total"] == t001["date_ranges_exempted"] == 2
assert t001["lexical_alternative_bundles_in_running_prose"] == t001["unclassified_solidus_tokens"] == 0
t002_manifest = jread(t002_paths["source_manifest_sha256"])
assert t002_manifest["line_start"] == 21089 and t002_manifest["line_end"] == 21097 and t002_manifest["next_line"] == 21099
assert (t002["clause_rows"], t002["target_ids"], t002["terminology_rows"]) == (6, 8, 10)
assert all(t002[key] for key in ("all_source_segments_accounted", "c_and_C_case_distinction_retained", "exact_conjugation_formula_present", "historical_regular_matrix_sense_noted", "equivalent_isomorphic_distinction_noted"))
t002_tex = t002_paths["target_tex_sha256"].read_text(encoding="utf-8")
assert r"P^{-1}CP\subseteq P^{-1}\mathfrak D P" in t002_tex
assert "10mm" in t002_tex and "la elemento" not in t002_tex
t003_manifest = jread(t003_paths["source_manifest_sha256"])
assert t003_manifest["line_start"] == 21099 and t003_manifest["line_end"] == 21115 and t003_manifest["next_line"] == 21117
assert (t003["clause_rows"], t003["target_ids"], t003["terminology_rows"], t003["grammar_delta_rows"]) == (10, 11, 12, 4)
assert all(t003[key] for key in ("all_source_segments_accounted", "direct_action_order_present", "reciprocal_action_order_present", "zero_annihilator_conditions_present", "source_x_star_variation_preserved_and_noted", "source_einfach_sense_held"))
assert len(read_csv(t003_paths["grammar_delta_sha256"])) == 4
assert {row["status"] for row in read_csv(t003_paths["grammar_delta_sha256"])} == {"test_only"}
warning_pattern = re.compile(r"Overfull|Underfull|Missing character|LaTeX Warning|Package .* Warning", re.I)
for build_log in (
    ROOT / "R823_HG_T001" / "build" / "R823_HG_T001_lualatex_console.log",
    ROOT / "R823_HG_T002" / "build" / "R823_HG_T002_lualatex_console.log",
    ROOT / "R823_HG_T003" / "build" / "R823_HG_T003_lualatex_console.log",
):
    assert not warning_pattern.search(build_log.read_text(encoding="utf-8", errors="replace"))

# Reproducible render evidence for the corrected T002 page 2 and T003.
render = jread(QA / "PDF_RENDER_REPRODUCIBILITY_v7.json")
assert render["status"] == "PASS" and render["render_dpi"] == 150
assert render["t002_page2_top_spacing"] == {"first_nonwhite_row": 299, "minimum_allowed_row": 250, "cap_height_clipped": False}
for tranche in render["tranches"]:
    assert tranche["pdf_sha256"] == sha(ROOT / tranche["tranche"] / "build" / f"{tranche['tranche']}_romance.pdf")
    for page in tranche["pages"]:
        pinned = ROOT / tranche["tranche"] / "qa" / "rendered" / f"{tranche['tranche']}_page-{page['page']}.png"
        assert page["exact_match"] is True and page["pinned_render_sha256"] == page["fresh_render_sha256"] == sha(pinned)

# Predecessor v6 is preserved but explicitly not the current lane-wide gate.
v6_gate = jread(QA / "ROMANCE_ACCEPTANCE_GATE_v6.json")
assert sha(QA / "ROMANCE_ACCEPTANCE_GATE_v6.json") == "B1D67C308CDF6DE3C8AAD7F26CAB1708DC66962B6F93182614623F9E47C97467"
assert sha(QA / "SHA256SUMS_v6.csv") == "821E6E609877A2BF80E41A3F3CC857B3A05207EB69CAF5F30397B210006D954B"
assert v6_gate["goal_status"] == "ACTIVE_NOT_COMPLETE" and v6_gate["hash_target_count"] == 86
scope_note = (QA / "V6_SCOPE_CORRECTION_v7.md").read_text(encoding="utf-8")
assert "not the current lane-wide gate" in scope_note and "superseded eight-cohort v1 tree" in scope_note

# Build a complete successor dependency manifest. V6 labels are recomputed at
# current bytes, then all manager, semantic-review, v7, T003, and render controls
# are added. The gate and manifest do not self-hash.
v6_rows = read_csv(QA / "SHA256SUMS_v6.csv")
hash_targets: dict[str, Path] = {row["relative_path"]: ROOT / row["relative_path"] for row in v6_rows}
additions = {
    "../00_lane_control/ROMANCE_MANAGER_README_20260717.md": MANAGER / "ROMANCE_MANAGER_README_20260717.md",
    "../00_lane_control/ROMANCE_MANAGER_CONTROL_VALIDATION_20260717.json": MANAGER / "ROMANCE_MANAGER_CONTROL_VALIDATION_20260717.json",
    "../00_lane_control/ROMANCE_MANAGER_CONTROL_SHA256SUMS.csv": MANAGER / "ROMANCE_MANAGER_CONTROL_SHA256SUMS.csv",
    "../00_lane_control/validate_manager_control_v2.py": MANAGER / "validate_manager_control_v2.py",
    "../00_lane_control/ROMANCE_FAMILY_COHORT_TREE_v1.json": MANAGER / "ROMANCE_FAMILY_COHORT_TREE_v1.json",
    "../_agent_reports/manager_control_reconciliation_v2.md": ROMANCE / "_agent_reports" / "manager_control_reconciliation_v2.md",
    "../_agent_reports/romance_acceptance_reaudit_v6.md": ROMANCE / "_agent_reports" / "romance_acceptance_reaudit_v6.md",
    "../_agent_reports/review_t21_t25.md": ROMANCE / "_agent_reports" / "review_t21_t25.md",
    "../_agent_reports/review_t26_t30.md": ROMANCE / "_agent_reports" / "review_t26_t30.md",
    "wordweb/OCCURRENCE_REVIEW_PROTOCOL_v1.md": ROOT / "wordweb" / "OCCURRENCE_REVIEW_PROTOCOL_v1.md",
    "wordweb/ROMANCE_OCCURRENCE_REVIEW_T21_T30_v1.csv": ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_T21_T30_v1.csv",
    "wordweb/ROMANCE_OCCURRENCE_REVIEW_T21_T30_v1.json": ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_T21_T30_v1.json",
    "wordweb/PAN_ROMANCE_WORDWEB_v7.json": ROOT / "wordweb" / "PAN_ROMANCE_WORDWEB_v7.json",
    "access/MII_METHOD_v7.md": ROOT / "access" / "MII_METHOD_v7.md",
    "access/PAN_ROMANCE_ACCESS_LEDGER_v7.json": ROOT / "access" / "PAN_ROMANCE_ACCESS_LEDGER_v7.json",
    "access/PAN_ROMANCE_ACCESS_LEDGER_v7.csv": ROOT / "access" / "PAN_ROMANCE_ACCESS_LEDGER_v7.csv",
    "scripts/review_occurrences_t21_t30_v1.py": ROOT / "scripts" / "review_occurrences_t21_t30_v1.py",
    "scripts/build_wordweb_and_access_v7.py": ROOT / "scripts" / "build_wordweb_and_access_v7.py",
    "scripts/verify_pdf_renders_v7.py": ROOT / "scripts" / "verify_pdf_renders_v7.py",
    "scripts/validate_romance_tranche_v7.py": ROOT / "scripts" / "validate_romance_tranche_v7.py",
    "qa/OCCURRENCE_REVIEW_T21_T30_v1.log": ROOT / "qa" / "OCCURRENCE_REVIEW_T21_T30_v1.log",
    "qa/WORDWEB_ACCESS_BUILD_v7.log": ROOT / "qa" / "WORDWEB_ACCESS_BUILD_v7.log",
    "qa/PDF_RENDER_REPRODUCIBILITY_v7.json": ROOT / "qa" / "PDF_RENDER_REPRODUCIBILITY_v7.json",
    "qa/PDF_VISUAL_QA_v7.md": ROOT / "qa" / "PDF_VISUAL_QA_v7.md",
    "qa/ACCEPTANCE_MATRIX_v7.md": ROOT / "qa" / "ACCEPTANCE_MATRIX_v7.md",
    "qa/V6_SCOPE_CORRECTION_v7.md": ROOT / "qa" / "V6_SCOPE_CORRECTION_v7.md",
    "qa/ROMANCE_ACCEPTANCE_GATE_v6.json": ROOT / "qa" / "ROMANCE_ACCEPTANCE_GATE_v6.json",
    "qa/SHA256SUMS_v6.csv": ROOT / "qa" / "SHA256SUMS_v6.csv",
    "R823_HG_T002/qa/R823_HG_T002_extracted.txt": ROOT / "R823_HG_T002" / "qa" / "R823_HG_T002_extracted.txt",
    "R823_HG_T002/qa/R823_HG_T002_pdfinfo.txt": ROOT / "R823_HG_T002" / "qa" / "R823_HG_T002_pdfinfo.txt",
    "R823_HG_T003/CONTINUATION_CURSOR.md": ROOT / "R823_HG_T003" / "CONTINUATION_CURSOR.md",
    "R823_HG_T003/source/R823_HG_T003_de_exact.tex": ROOT / "R823_HG_T003" / "source" / "R823_HG_T003_de_exact.tex",
    "R823_HG_T003/source/R823_HG_T003_de_numbered.txt": ROOT / "R823_HG_T003" / "source" / "R823_HG_T003_de_numbered.txt",
    "R823_HG_T003/source/R823_HG_T003_SOURCE_MANIFEST.json": ROOT / "R823_HG_T003" / "source" / "R823_HG_T003_SOURCE_MANIFEST.json",
    "R823_HG_T003/semantic/R823_HG_T003_clause_map_seed.csv": ROOT / "R823_HG_T003" / "semantic" / "R823_HG_T003_clause_map_seed.csv",
    "R823_HG_T003/semantic/R823_HG_T003_clause_map.csv": ROOT / "R823_HG_T003" / "semantic" / "R823_HG_T003_clause_map.csv",
    "R823_HG_T003/terminology/R823_HG_T003_TERMINOLOGY_v1.csv": ROOT / "R823_HG_T003" / "terminology" / "R823_HG_T003_TERMINOLOGY_v1.csv",
    "R823_HG_T003/grammar/CONTROLLED_ROMANCE_GRAMMAR_T003_DELTA_v1.csv": ROOT / "R823_HG_T003" / "grammar" / "CONTROLLED_ROMANCE_GRAMMAR_T003_DELTA_v1.csv",
    "R823_HG_T003/scripts/prepare_source.py": ROOT / "R823_HG_T003" / "scripts" / "prepare_source.py",
    "R823_HG_T003/scripts/build_t003.ps1": ROOT / "R823_HG_T003" / "scripts" / "build_t003.ps1",
    "R823_HG_T003/scripts/validate_t003.py": ROOT / "R823_HG_T003" / "scripts" / "validate_t003.py",
    "R823_HG_T003/tex/R823_HG_T003_romance.tex": ROOT / "R823_HG_T003" / "tex" / "R823_HG_T003_romance.tex",
    "R823_HG_T003/build/R823_HG_T003_romance.pdf": ROOT / "R823_HG_T003" / "build" / "R823_HG_T003_romance.pdf",
    "R823_HG_T003/build/R823_HG_T003_lualatex_console.log": ROOT / "R823_HG_T003" / "build" / "R823_HG_T003_lualatex_console.log",
    "R823_HG_T003/qa/R823_HG_T003_extracted.txt": ROOT / "R823_HG_T003" / "qa" / "R823_HG_T003_extracted.txt",
    "R823_HG_T003/qa/R823_HG_T003_pdfinfo.txt": ROOT / "R823_HG_T003" / "qa" / "R823_HG_T003_pdfinfo.txt",
    "R823_HG_T003/qa/R823_HG_T003_validation.json": ROOT / "R823_HG_T003" / "qa" / "R823_HG_T003_validation.json",
    "R823_HG_T003/qa/R823_HG_T003_VISUAL_QA.md": ROOT / "R823_HG_T003" / "qa" / "R823_HG_T003_VISUAL_QA.md",
    "R823_HG_T003/qa/rendered/R823_HG_T003_page-1.png": ROOT / "R823_HG_T003" / "qa" / "rendered" / "R823_HG_T003_page-1.png",
    "R823_HG_T003/qa/rendered/R823_HG_T003_page-2.png": ROOT / "R823_HG_T003" / "qa" / "rendered" / "R823_HG_T003_page-2.png",
}
hash_targets.update(additions)
hash_rows = []
for label, path in hash_targets.items():
    assert path.exists(), path
    hash_rows.append({"relative_path": label, "bytes": path.stat().st_size, "sha256": sha(path)})
hash_manifest = QA / "SHA256SUMS_v7.csv"
with hash_manifest.open("w", encoding="utf-8-sig", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=["relative_path", "bytes", "sha256"])
    writer.writeheader()
    writer.writerows(hash_rows)

gate = {
    "artifact": "ROMANCE_ACCEPTANCE_GATE_v7",
    "machine_validation": "PASS",
    "goal_status": "ACTIVE_NOT_COMPLETE",
    "predecessor_v6": {
        "status": "PRESERVED_BOUNDED_SNAPSHOT_NOT_CURRENT_LANE_GATE",
        "gate_sha256": sha(QA / "ROMANCE_ACCEPTANCE_GATE_v6.json"),
        "manifest_sha256": sha(QA / "SHA256SUMS_v6.csv"),
        "scope_correction": "qa/V6_SCOPE_CORRECTION_v7.md",
    },
    "manager_control_plane": {
        "status": "PASS",
        "canonical_tree": "ROMANCE_FAMILY_COHORT_TREE_v2",
        "cohort_count": 9,
        "v1_status": "preserved_superseded",
        "human_observations": 0,
    },
    "stage_A": {
        "status": "NOT_COMPLETE",
        "production_evidence": "61 explicit routes; 8 active and 53 zero/gap; minimal bodies for all eight starting standards",
        "blocking_gap": "Rumantsch Grischun has one general school-math body but zero specialist-algebra bodies; five idioms and 48 other routes remain zero-source",
    },
    "stage_B": {
        "status": "CURRENT_CORPUS_TRANCHE_PASS",
        "records": 146,
        "primary_unique": 140,
        "counting_eligible": 64,
        "romansh_active": 1,
        "romansh_specialist_algebra": 0,
    },
    "stage_C": {
        "status": "PARTIAL",
        "core_concepts": 60,
        "senses": 106,
        "evidence_records": 481,
        "relation_records": 402,
        "valid_target_id_relation_edges": 27,
        "concept_to_sense_membership_edges": 106,
        "total_id_resolved_references_including_memberships": 133,
        "occurrence_review_cursor": "T01_T30_complete_plus_RM_RG_T45_T57_next_contiguous_T31",
        "human_observations": 0,
        "core_form_promotions": 0,
    },
    "stage_D": {
        "status": "T001_T003_PRODUCTION_TRANCHES_PASS_NOT_LANGUAGE_VALIDATED",
        "T001_body_lines": "21047-21087",
        "T001_metadata_lines": "20985-20990",
        "T002_body_lines": "21089-21097",
        "T003_body_lines": "21099-21115",
        "next_authority_line": 21117,
        "human_validation": 0,
    },
    "canonical_cohort_topology": {
        "artifact": "ROMANCE_FAMILY_COHORT_TREE_v2",
        "cohort_count": 9,
        "cohort_ids": expected_cohort_ids,
        "human_observations": 0,
        "MII_result_feeds_decisions": False,
    },
    "core_evidence_boundary": {
        "inherited_es_fr_records": 120,
        "inherited_core_quotations": 0,
        "extension_context_to_core_promotions": 0,
    },
    "T002_render": {"page_2_first_nonwhite_row": 299, "cap_height_clipped": False},
    "pilot_claim": False,
    "full_R823_romance_translation_claim": False,
    "hash_target_count": len(hash_rows),
    "hash_manifest_sha256": sha(hash_manifest),
    "key_hashes": {row["relative_path"]: row["sha256"] for row in hash_rows},
}
(QA / "ROMANCE_ACCEPTANCE_GATE_v7.json").write_text(json.dumps(gate, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
lines = [
    "PASS machine_validation",
    "goal_status=ACTIVE_NOT_COMPLETE",
    "predecessor_v6=PRESERVED_BOUNDED_SNAPSHOT_NOT_CURRENT_LANE_GATE",
    "manager_control=PASS canonical_v2_cohorts=9 human=0",
    "stage_A=NOT_COMPLETE active_routes=8 explicit_zero_routes=53 romansh_specialist_algebra=0",
    "stage_B=CURRENT_CORPUS_TRANCHE_PASS records=146 primary_unique=140 counting_eligible=64",
    "stage_C=PARTIAL concepts=60 senses=106 evidence=481 relation_records=402 valid_target_edges=27 memberships=106 total_resolved=133 reviewed_T01_T30 human=0 promotions=0",
    "stage_D=T001_T003_PRODUCTION_TRANCHES_PASS_NOT_LANGUAGE_VALIDATED next=21117",
    "T002_page2_first_nonwhite_row=299 cap_height_clipped=false",
    "cohorts=9 access_rows=954 human_observations=0 MII_result_feeds_decisions=false",
    "pilot_claim=false full_R823_romance_translation_claim=false",
    f"hash_targets={len(hash_rows)} sha256_manifest={sha(hash_manifest)}",
]
(QA / "ROMANCE_ACCEPTANCE_GATE_v7.log").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
