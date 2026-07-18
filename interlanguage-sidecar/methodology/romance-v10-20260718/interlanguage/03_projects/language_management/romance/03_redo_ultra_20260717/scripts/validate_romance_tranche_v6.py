from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ROMANCE = ROOT.parent
QA = ROOT / "qa"


def read_csv(path: Path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def jread(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def graph_metrics(wordweb):
    valid_ids = (
        {core["term_id"] for core in wordweb["core_concepts"]}
        | {sense["sense_id"] for sense in wordweb["senses"]}
        | {node["concept_id"] for node in wordweb["c2_extension_nodes"]}
    )
    relations = [relation for core in wordweb["core_concepts"] for relation in core["relations"]]
    target_edges = sum(relation.get("target_id") in valid_ids for relation in relations)
    memberships = sum(len(core["sense_ids"]) for core in wordweb["core_concepts"])
    return len(relations), target_edges, memberships, target_edges + memberships


manifest = read_csv(ROOT / "corpus" / "WIKIMEDIA_HTML_CORPUS_MANIFEST_v1.csv")
query = read_csv(ROOT / "corpus" / "WIKIMEDIA_HTML_QUERY_LOG_v1.csv")
rejected_html = read_csv(ROOT / "corpus" / "WIKIMEDIA_HTML_REJECTED_AUTOMATIC_SEARCH_v1.csv")
manifest_qa = jread(ROOT / "corpus" / "WIKIMEDIA_HTML_MANIFEST_QA_v1.json")
corpus = read_csv(ROOT / "corpus" / "ROMANCE_CONSOLIDATED_CORPUS_v2.csv")
coverage = read_csv(ROOT / "corpus" / "ROMANCE_CORPUS_LANGUAGE_DOMAIN_COVERAGE_v2.csv")
routes = read_csv(ROOT / "corpus" / "ROMANCE_BRANCH_ROUTING_LEDGER_v1.csv")
occurrence_summary = jread(ROOT / "wordweb" / "ROMANCE_TERM_OCCURRENCES_v1.json")
review_t01 = jread(ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_T01_T10_v1.json")
review_t11 = jread(ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_T11_T20_v1.json")
review_rm = jread(ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_RM_RG_SOURCE_v1.json")
ww5 = jread(ROOT / "wordweb" / "PAN_ROMANCE_WORDWEB_v5.json")
ww6 = jread(ROOT / "wordweb" / "PAN_ROMANCE_WORDWEB_v6.json")
access6 = jread(ROOT / "access" / "PAN_ROMANCE_ACCESS_LEDGER_v6.json")
cohort_tree = jread(ROMANCE / "00_lane_control" / "ROMANCE_FAMILY_COHORT_TREE_v2.json")
t001 = jread(ROOT / "R823_HG_T001" / "qa" / "R823_HG_T001_validation.json")
t001_source = jread(ROOT / "R823_HG_T001" / "source" / "R823_HG_T001_SOURCE_MANIFEST.json")
t002 = jread(ROOT / "R823_HG_T002" / "qa" / "R823_HG_T002_validation.json")
t002_source = jread(ROOT / "R823_HG_T002" / "source" / "R823_HG_T002_SOURCE_MANIFEST.json")

# Wikimedia correction gate: no placeholders or false Romansh pages in active coverage.
assert len(manifest) == 42
assert not any(row["language_code"] == "rm" for row in manifest)
assert not any(not row["title"].strip() or int(row["page_id"]) == 0 or int(row["revision_id"]) == 0 for row in manifest)
assert manifest_qa["historical_pre_qa_rows"] == 48 and manifest_qa["active_rows"] == 42
assert manifest_qa["romansh_downloaded"] == 0 and manifest_qa["romansh_unique_pages"] == 0
assert len(rejected_html) == 4
assert Counter(row["title"] for row in rejected_html) == Counter({"Biologia": 2, "Tirchia": 1, "Republica Populara da la China": 1})
query_status = Counter(row["status"].split(":", 1)[0] for row in query if row["language"] == "rm")
assert query_status == Counter({"rejected_nonmathematical_result": 4, "no_article_result_zero_page_or_revision": 2})

# Consolidated corpus and explicit branch routing.
assert len(corpus) == 146
assert len({row["record_id"] for row in corpus}) == 146
assert sum(row["dedupe_status"] == "primary_unique" for row in corpus) == 140
assert sum(row["counting_eligible"] == "true" for row in corpus) == 64
assert all(row["term_promotion_eligible"] == "false" for row in corpus)
for row in corpus:
    original = Path(row["absolute_path"])
    assert original.exists() and original.stat().st_size == int(row["bytes"]) and sha(original) == row["sha256"]
    if row["counting_eligible"] == "true":
        search = Path(row["search_text_path"])
        assert search.exists() and sha(search) == row["search_text_sha256"]
rm_rows = [row for row in corpus if row["language"] == "rm" and row["counting_eligible"] == "true"]
assert len(rm_rows) == 1 and rm_rows[0]["variety_code"] == "rm-rg"
assert rm_rows[0]["domain"] == "mathematics_education" and rm_rows[0]["license_status"] == "unresolved_no_explicit_reuse_grant"
rm_coverage = next(row for row in coverage if row["language"] == "rm")
assert rm_coverage["records"] == rm_coverage["primary_unique_records"] == rm_coverage["counting_eligible"] == "1"
assert rm_coverage["body_status"] == "substantive_body_present"

assert len(routes) == 61
assert sum(int(row["current_active_body_count"]) > 0 for row in routes) == 8
assert sum(int(row["current_active_body_count"]) == 0 for row in routes) == 53
assert all(row["dominant_standard_not_proxy"] == "true" for row in routes)
assert {row["variety_name"] for row in routes if row["subbranch"] == "Gallo-Italic"} >= {"Piedmontese", "Lombard", "Ligurian", "Emilian-Romagnol"}
assert any(row["variety_code"] == "ist" for row in routes)
rm_route = next(row for row in routes if row["variety_code"] == "rm-rg")
assert rm_route["current_active_body_count"] == "1"
assert "general school-mathematics body" in rm_route["notes"] and "specialist algebra" in rm_route["notes"]
assert sha(ROOT / "corpus" / "ROMANCE_BRANCH_ROUTING_LEDGER_v1.csv") == "7440CE0E6D4FB4CFDC33C30E704F41E301853BFC2E81E6D26550A4A6438767CF"

# Contiguous context review and semantic successor.
assert occurrence_summary["occurrence_count"] == 679 and occurrence_summary["terms_with_context"] == 54
assert occurrence_summary["languages"]["rm"] == 2 and occurrence_summary["promotion_eligible"] == 0
assert review_t01["reviewed_rows"] == 117 and review_t01["accepted_sense_matches"] == 84 and review_t01["rejected_adverse_or_wrong_sense"] == 33
assert review_t11["reviewed_rows"] == 111 and review_t11["accepted_sense_matches"] == 90
assert review_t11["rejected_adverse_or_wrong_sense"] == 10 and review_t11["held_rows"] == 11
assert review_t11["explicit_zero_hit_terms"] == ["T11"] and review_t11["bridge_form_promotions"] == review_t11["human_observations"] == 0
assert review_rm["unique_occurrences"] == 2 and review_rm["sense_judgments"] == 3
assert review_rm["accepted_sense_matches"] == 2 and review_rm["rejected_adverse_or_wrong_sense"] == 1
assert review_rm["core_form_promotions"] == review_rm["human_observations"] == 0

assert sha(ROOT / "wordweb" / "PAN_ROMANCE_WORDWEB_v5.json") == "4B2B92D18F2823B1173AF6A9AD7F06FD990813452451F553F7623C300DDFFC5B"
assert ww6["artifact"] == "PAN_ROMANCE_WORDWEB_v6" and ww6["supersedes_for_semantic_use"] == "PAN_ROMANCE_WORDWEB_v5"
assert ww6["core_concept_count"] == 60 and ww6["sense_count"] == 106 and len(ww6["decisions"]) == 106
assert ww6["evidence_record_count"] == len(ww6["evidence_records"]) == 350
assert graph_metrics(ww5) == (402, 27, 106, 133)
assert graph_metrics(ww6) == (402, 27, 106, 133)
assert ww6["relation_count"] == ww6["relation_metrics"]["relation_records"] == 402
assert ww6["relation_metrics"]["valid_target_id_edges"] == 27
assert ww6["relation_metrics"]["concept_to_sense_membership_edges"] == 106
assert ww6["relation_metrics"]["total_id_resolved_references_including_memberships"] == 133
assert ww6["predecessor_v5_relation_metrics"]["relation_records"] == 402
assert ww6["predecessor_v5_relation_metrics"]["valid_target_id_edges"] == 27
t57 = next(core for core in ww6["core_concepts"] if core["term_id"] == "T57")
t57_edges = [relation for relation in t57["relations"] if relation.get("target_label") == "straight_direction_not_algebraic_right_action"]
assert len(t57_edges) == 1 and t57_edges[0]["target_id"] == "T57-S1"
assert [core["forms"] for core in ww6["core_concepts"]] == [core["forms"] for core in ww5["core_concepts"]]
assert ww6["c2_extension_nodes"] == ww5["c2_extension_nodes"]
assert all(record["quote"] is None and record["acceptance"] == "unresolved_locator" and record["language"] in {"es", "fr"} for record in ww6["evidence_records"][:120])
boundary = ww6["core_evidence_boundary"]
assert boundary["inherited_es_fr_core_records"] == 120 and boundary["inherited_core_quotation_count"] == 0
assert boundary["reviewed_occurrence_records"] == 230 and boundary["explicit_zero_hit_terms"] == ["T11"]
assert boundary["extension_context_to_core_promotions"] == boundary["core_form_promotions"] == boundary["human_observations"] == 0
for term_id in ("T51", "T60"):
    senses = [sense for sense in ww6["senses"] if sense["term_id"] == term_id]
    decisions = [decision for decision in ww6["decisions"] if decision["term_id"] == term_id]
    assert len(senses) == len(decisions) == 4 and all(not decision["candidate_surfaces"] for decision in decisions)
assert all(not decision["candidate_surfaces"] for decision in ww6["decisions"] if decision["sense_id"] in {"T09-S1", "T10-S1", "T10-S2"})
assert sha(ROMANCE / "_agent_reports" / "corpus_acceptance_reaudit_v5.md") == "3A611023472959D2AB2688D5B85D339FE3285CFD16A67682E66828779820A779"

# One canonical nine-cohort topology; still zero human observations.
tree_ids = [cohort["cohort_id"] for cohort in cohort_tree["reader_cohorts"]]
ledger_ids = [cohort["cohort_id"] for cohort in access6["cohorts"]]
assert cohort_tree["artifact"] == "ROMANCE_FAMILY_COHORT_TREE_v2" and cohort_tree["cohort_count"] == 9
assert tree_ids == ledger_ids and len(set(tree_ids)) == 9
assert {"C-RM-RG", "C-RM-ID"} <= set(tree_ids)
assert access6["sense_count"] == 106 and access6["row_count"] == len(access6["rows"]) == 954
assert access6["canonical_cohort_topology"]["cohort_ids"] == tree_ids
assert access6["human_observation_count"] == 0 and access6["pilot_eligible_count"] == 0
assert all(row["human_n"] is None and row["human_correct"] is None and row["human_incorrect"] is None and row["human_abstain"] is None for row in access6["rows"])
assert all(not row["pilot_eligible"] for row in access6["rows"])
method_text = (ROOT / "access" / "MII_METHOD_v6.md").read_text(encoding="utf-8")
assert "106 × 9 = 954" in method_text and "zero human observations" in method_text and "no MII result may feed" in method_text

# T001 now binds metadata separately and truly validates grammar; T002 advances to §3.
t001_manifest_path = ROOT / "R823_HG_T001" / "source" / "R823_HG_T001_SOURCE_MANIFEST.json"
t001_clause_path = ROOT / "R823_HG_T001" / "semantic" / "R823_HG_T001_clause_map.csv"
t001_terms_path = ROOT / "R823_HG_T001" / "terminology" / "R823_HG_T001_TERMINOLOGY_v1.csv"
t001_grammar_path = ROOT / "R823_HG_T001" / "grammar" / "CONTROLLED_ROMANCE_GRAMMAR_TEST_v1.csv"
t001_validator_path = ROOT / "R823_HG_T001" / "scripts" / "validate_t001.py"
grammar_rows = read_csv(t001_grammar_path)
assert len(grammar_rows) == 18 and {row["status"] for row in grammar_rows} == {"test_only", "held"}
assert t001["status"] == "PASS" and t001["clause_rows"] == 27 and t001["target_ids"] == 34
assert t001["terminology_rows"] == 35 and t001["grammar_rows"] == 18 and t001["grammar_required_features_checked"]
assert t001["authority_body_slice_sha256"] == "33E4D17FEC404CB5B5A7DF208EE1BC5855BB6B0F4091A04905B95B75C1D9AF64"
assert t001["authority_metadata_slice_sha256"] == "D424D5D19D8B8E153B1DF736933F71B83098A5C54135646561B9E3E2C8519559"
assert t001_source["body_source_lines"] == [21047, 21087] and t001_source["metadata_source_lines"] == [20985, 20990]
assert t001["source_manifest_sha256"] == sha(t001_manifest_path)
assert t001["clause_map_sha256"] == sha(t001_clause_path)
assert t001["terminology_sha256"] == sha(t001_terms_path)
assert t001["grammar_sha256"] == sha(t001_grammar_path)
assert t001["validator_sha256"] == sha(t001_validator_path)
assert t001["solidus_tokens_total"] == t001["date_ranges_exempted"] == 2
assert t001["lexical_alternative_bundles_in_running_prose"] == t001["unclassified_solidus_tokens"] == 0
assert t001["human_validation_rows"] == 0 and not t001["pilot_claim"]

assert t002["status"] == "PASS" and t002["clause_rows"] == 6 and t002["target_ids"] == 8 and t002["terminology_rows"] == 10
assert t002["authority_slice_sha256"] == t002_source["exact_slice_sha256"] == "5F58DDE60BB8C34421D81E7A418BF712C3F2860DBF8E4F0C16007A1A2689E235"
assert t002["c_and_C_case_distinction_retained"] and t002["exact_conjugation_formula_present"]
assert t002["historical_regular_matrix_sense_noted"] and t002["equivalent_isomorphic_distinction_noted"]
assert t002["next_source_line"] == t002_source["next_line"] == 21099
assert t002["human_validation_rows"] == 0 and not t002["pilot_claim"]

warning_pattern = re.compile(r"Overfull|Underfull|Missing character|LaTeX Warning|Package .* Warning", re.I)
for build_log in (
    ROOT / "R823_HG_T001" / "build" / "R823_HG_T001_lualatex_console.log",
    ROOT / "R823_HG_T002" / "build" / "R823_HG_T002_lualatex_console.log",
):
    assert not warning_pattern.search(build_log.read_text(encoding="utf-8", errors="replace"))

# Complete dependency hash set. In particular, all five requested T001 control files are first-class dependencies.
hash_targets = [
    ("README.md", ROOT / "README.md"),
    ("CONTINUATION_CURSOR.md", ROOT / "CONTINUATION_CURSOR.md"),
    ("../00_lane_control/ROMANCE_FAMILY_COHORT_TREE_v2.json", ROMANCE / "00_lane_control" / "ROMANCE_FAMILY_COHORT_TREE_v2.json"),
    ("../_agent_reports/corpus_acceptance_reaudit_v5.md", ROMANCE / "_agent_reports" / "corpus_acceptance_reaudit_v5.md"),
    ("../_agent_reports/review_t11_t15.md", ROMANCE / "_agent_reports" / "review_t11_t15.md"),
    ("../_agent_reports/review_t16_t20.md", ROMANCE / "_agent_reports" / "review_t16_t20.md"),
    ("corpus/WIKIMEDIA_HTML_CORPUS_MANIFEST_v1.csv", ROOT / "corpus" / "WIKIMEDIA_HTML_CORPUS_MANIFEST_v1.csv"),
    ("corpus/WIKIMEDIA_HTML_COVERAGE_v1.csv", ROOT / "corpus" / "WIKIMEDIA_HTML_COVERAGE_v1.csv"),
    ("corpus/WIKIMEDIA_HTML_QUERY_LOG_v1.csv", ROOT / "corpus" / "WIKIMEDIA_HTML_QUERY_LOG_v1.csv"),
    ("corpus/WIKIMEDIA_HTML_REJECTED_AUTOMATIC_SEARCH_v1.csv", ROOT / "corpus" / "WIKIMEDIA_HTML_REJECTED_AUTOMATIC_SEARCH_v1.csv"),
    ("corpus/WIKIMEDIA_HTML_MANIFEST_QA_v1.json", ROOT / "corpus" / "WIKIMEDIA_HTML_MANIFEST_QA_v1.json"),
    ("curation/WIKIMEDIA_HTML_TOPIC_REVIEW_v1.csv", ROOT / "curation" / "WIKIMEDIA_HTML_TOPIC_REVIEW_v1.csv"),
    ("curation/ROMANCE_BRANCH_ROUTE_SEED_v1.csv", ROOT / "curation" / "ROMANCE_BRANCH_ROUTE_SEED_v1.csv"),
    ("corpus/CURATED_EXTERNAL_SOURCE_MANIFEST_v1.csv", ROOT / "corpus" / "CURATED_EXTERNAL_SOURCE_MANIFEST_v1.csv"),
    ("corpus/ROMANCE_CONSOLIDATED_CORPUS_v2.csv", ROOT / "corpus" / "ROMANCE_CONSOLIDATED_CORPUS_v2.csv"),
    ("corpus/ROMANCE_CORPUS_LANGUAGE_DOMAIN_COVERAGE_v2.csv", ROOT / "corpus" / "ROMANCE_CORPUS_LANGUAGE_DOMAIN_COVERAGE_v2.csv"),
    ("corpus/ROMANCE_BRANCH_ROUTING_LEDGER_v1.csv", ROOT / "corpus" / "ROMANCE_BRANCH_ROUTING_LEDGER_v1.csv"),
    ("corpus/CORPUS_PROVENANCE_AND_BRANCH_ROUTING_v5.md", ROOT / "corpus" / "CORPUS_PROVENANCE_AND_BRANCH_ROUTING_v5.md"),
    ("corpus/downloaded_curated/rm-rg/gr_ch_AP1G_2021/AP21_1G_M1_RG.pdf", ROOT / "corpus" / "downloaded_curated" / "rm-rg" / "gr_ch_AP1G_2021" / "AP21_1G_M1_RG.pdf"),
    ("corpus/downloaded_curated/rm-rg/gr_ch_AP1G_2021/AP21_1G_M1_RG.txt", ROOT / "corpus" / "downloaded_curated" / "rm-rg" / "gr_ch_AP1G_2021" / "AP21_1G_M1_RG.txt"),
    ("wordweb/ROMANCE_TERM_OCCURRENCES_v1.csv", ROOT / "wordweb" / "ROMANCE_TERM_OCCURRENCES_v1.csv"),
    ("wordweb/ROMANCE_TERM_OCCURRENCES_v1.json", ROOT / "wordweb" / "ROMANCE_TERM_OCCURRENCES_v1.json"),
    ("wordweb/ROMANCE_OCCURRENCE_REVIEW_T01_T10_v1.csv", ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_T01_T10_v1.csv"),
    ("wordweb/ROMANCE_OCCURRENCE_REVIEW_T01_T10_v1.json", ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_T01_T10_v1.json"),
    ("wordweb/ROMANCE_OCCURRENCE_REVIEW_RM_RG_SOURCE_v1.csv", ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_RM_RG_SOURCE_v1.csv"),
    ("wordweb/ROMANCE_OCCURRENCE_REVIEW_RM_RG_SOURCE_v1.json", ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_RM_RG_SOURCE_v1.json"),
    ("wordweb/ROMANCE_OCCURRENCE_REVIEW_T11_T20_v1.csv", ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_T11_T20_v1.csv"),
    ("wordweb/ROMANCE_OCCURRENCE_REVIEW_T11_T20_v1.json", ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_T11_T20_v1.json"),
    ("wordweb/PAN_ROMANCE_WORDWEB_v5.json", ROOT / "wordweb" / "PAN_ROMANCE_WORDWEB_v5.json"),
    ("wordweb/PAN_ROMANCE_WORDWEB_v6.json", ROOT / "wordweb" / "PAN_ROMANCE_WORDWEB_v6.json"),
    ("access/MII_METHOD_v6.md", ROOT / "access" / "MII_METHOD_v6.md"),
    ("access/PAN_ROMANCE_ACCESS_LEDGER_v6.json", ROOT / "access" / "PAN_ROMANCE_ACCESS_LEDGER_v6.json"),
    ("access/PAN_ROMANCE_ACCESS_LEDGER_v6.csv", ROOT / "access" / "PAN_ROMANCE_ACCESS_LEDGER_v6.csv"),
    ("scripts/normalize_wikimedia_html_manifest.ps1", ROOT / "scripts" / "normalize_wikimedia_html_manifest.ps1"),
    ("scripts/build_consolidated_corpus_v2.py", ROOT / "scripts" / "build_consolidated_corpus_v2.py"),
    ("scripts/build_branch_routing_ledger_v1.py", ROOT / "scripts" / "build_branch_routing_ledger_v1.py"),
    ("scripts/extract_wordweb_occurrences_v1.py", ROOT / "scripts" / "extract_wordweb_occurrences_v1.py"),
    ("scripts/review_occurrences_t01_t10_v1.py", ROOT / "scripts" / "review_occurrences_t01_t10_v1.py"),
    ("scripts/review_rm_rg_source_v1.py", ROOT / "scripts" / "review_rm_rg_source_v1.py"),
    ("scripts/review_occurrences_t11_t20_v1.py", ROOT / "scripts" / "review_occurrences_t11_t20_v1.py"),
    ("scripts/build_wordweb_and_access_v6.py", ROOT / "scripts" / "build_wordweb_and_access_v6.py"),
    ("scripts/validate_romance_tranche_v6.py", ROOT / "scripts" / "validate_romance_tranche_v6.py"),
    ("qa/CORPUS_BUILD_v2.log", ROOT / "qa" / "CORPUS_BUILD_v2.log"),
    ("qa/BRANCH_ROUTING_BUILD_v1.log", ROOT / "qa" / "BRANCH_ROUTING_BUILD_v1.log"),
    ("qa/TERM_OCCURRENCE_EXTRACTION_v1.log", ROOT / "qa" / "TERM_OCCURRENCE_EXTRACTION_v1.log"),
    ("qa/OCCURRENCE_REVIEW_T01_T10_v1.log", ROOT / "qa" / "OCCURRENCE_REVIEW_T01_T10_v1.log"),
    ("qa/OCCURRENCE_REVIEW_RM_RG_SOURCE_v1.log", ROOT / "qa" / "OCCURRENCE_REVIEW_RM_RG_SOURCE_v1.log"),
    ("qa/OCCURRENCE_REVIEW_T11_T20_v1.log", ROOT / "qa" / "OCCURRENCE_REVIEW_T11_T20_v1.log"),
    ("qa/WORDWEB_ACCESS_BUILD_v6.log", ROOT / "qa" / "WORDWEB_ACCESS_BUILD_v6.log"),
    ("qa/ACCEPTANCE_MATRIX_v6.md", ROOT / "qa" / "ACCEPTANCE_MATRIX_v6.md"),
    ("qa/RM_RG_SOURCE_VISUAL_QA_v1.md", ROOT / "qa" / "RM_RG_SOURCE_VISUAL_QA_v1.md"),
    ("qa/rm_source_render/AP21_1G_M1_RG_page_01.png", ROOT / "qa" / "rm_source_render" / "AP21_1G_M1_RG_page_01.png"),
    ("qa/rm_source_render/AP21_1G_M1_RG_page_04.png", ROOT / "qa" / "rm_source_render" / "AP21_1G_M1_RG_page_04.png"),
    ("qa/rm_source_render/AP21_1G_M1_RG_page_08.png", ROOT / "qa" / "rm_source_render" / "AP21_1G_M1_RG_page_08.png"),
    ("qa/rm_source_render/AP21_1G_M1_RG_page_13.png", ROOT / "qa" / "rm_source_render" / "AP21_1G_M1_RG_page_13.png"),
    ("R823_HG_T001/source/R823_HG_T001_de_exact.tex", ROOT / "R823_HG_T001" / "source" / "R823_HG_T001_de_exact.tex"),
    ("R823_HG_T001/source/R823_HG_T001_de_metadata_exact.tex", ROOT / "R823_HG_T001" / "source" / "R823_HG_T001_de_metadata_exact.tex"),
    ("R823_HG_T001/source/R823_HG_T001_SOURCE_MANIFEST.json", t001_manifest_path),
    ("R823_HG_T001/semantic/R823_HG_T001_clause_map.csv", t001_clause_path),
    ("R823_HG_T001/terminology/R823_HG_T001_TERMINOLOGY_v1.csv", t001_terms_path),
    ("R823_HG_T001/grammar/CONTROLLED_ROMANCE_GRAMMAR_TEST_v1.csv", t001_grammar_path),
    ("R823_HG_T001/scripts/prepare_source.py", ROOT / "R823_HG_T001" / "scripts" / "prepare_source.py"),
    ("R823_HG_T001/scripts/build_t001.ps1", ROOT / "R823_HG_T001" / "scripts" / "build_t001.ps1"),
    ("R823_HG_T001/scripts/validate_t001.py", t001_validator_path),
    ("R823_HG_T001/tex/R823_HG_T001_romance.tex", ROOT / "R823_HG_T001" / "tex" / "R823_HG_T001_romance.tex"),
    ("R823_HG_T001/build/R823_HG_T001_romance.pdf", ROOT / "R823_HG_T001" / "build" / "R823_HG_T001_romance.pdf"),
    ("R823_HG_T001/build/R823_HG_T001_lualatex_console.log", ROOT / "R823_HG_T001" / "build" / "R823_HG_T001_lualatex_console.log"),
    ("R823_HG_T001/qa/R823_HG_T001_validation.json", ROOT / "R823_HG_T001" / "qa" / "R823_HG_T001_validation.json"),
    ("R823_HG_T001/qa/R823_HG_T001_VISUAL_QA.md", ROOT / "R823_HG_T001" / "qa" / "R823_HG_T001_VISUAL_QA.md"),
    ("R823_HG_T001/qa/rendered/R823_HG_T001_page-1.png", ROOT / "R823_HG_T001" / "qa" / "rendered" / "R823_HG_T001_page-1.png"),
    ("R823_HG_T001/qa/rendered/R823_HG_T001_page-2.png", ROOT / "R823_HG_T001" / "qa" / "rendered" / "R823_HG_T001_page-2.png"),
    ("R823_HG_T001/qa/rendered/R823_HG_T001_page-3.png", ROOT / "R823_HG_T001" / "qa" / "rendered" / "R823_HG_T001_page-3.png"),
    ("R823_HG_T002/source/R823_HG_T002_de_exact.tex", ROOT / "R823_HG_T002" / "source" / "R823_HG_T002_de_exact.tex"),
    ("R823_HG_T002/source/R823_HG_T002_SOURCE_MANIFEST.json", ROOT / "R823_HG_T002" / "source" / "R823_HG_T002_SOURCE_MANIFEST.json"),
    ("R823_HG_T002/semantic/R823_HG_T002_clause_map.csv", ROOT / "R823_HG_T002" / "semantic" / "R823_HG_T002_clause_map.csv"),
    ("R823_HG_T002/terminology/R823_HG_T002_TERMINOLOGY_v1.csv", ROOT / "R823_HG_T002" / "terminology" / "R823_HG_T002_TERMINOLOGY_v1.csv"),
    ("R823_HG_T002/scripts/prepare_source.py", ROOT / "R823_HG_T002" / "scripts" / "prepare_source.py"),
    ("R823_HG_T002/scripts/build_t002.ps1", ROOT / "R823_HG_T002" / "scripts" / "build_t002.ps1"),
    ("R823_HG_T002/scripts/validate_t002.py", ROOT / "R823_HG_T002" / "scripts" / "validate_t002.py"),
    ("R823_HG_T002/tex/R823_HG_T002_romance.tex", ROOT / "R823_HG_T002" / "tex" / "R823_HG_T002_romance.tex"),
    ("R823_HG_T002/build/R823_HG_T002_romance.pdf", ROOT / "R823_HG_T002" / "build" / "R823_HG_T002_romance.pdf"),
    ("R823_HG_T002/build/R823_HG_T002_lualatex_console.log", ROOT / "R823_HG_T002" / "build" / "R823_HG_T002_lualatex_console.log"),
    ("R823_HG_T002/qa/R823_HG_T002_validation.json", ROOT / "R823_HG_T002" / "qa" / "R823_HG_T002_validation.json"),
    ("R823_HG_T002/qa/R823_HG_T002_VISUAL_QA.md", ROOT / "R823_HG_T002" / "qa" / "R823_HG_T002_VISUAL_QA.md"),
    ("R823_HG_T002/qa/rendered/R823_HG_T002_page-1.png", ROOT / "R823_HG_T002" / "qa" / "rendered" / "R823_HG_T002_page-1.png"),
    ("R823_HG_T002/qa/rendered/R823_HG_T002_page-2.png", ROOT / "R823_HG_T002" / "qa" / "rendered" / "R823_HG_T002_page-2.png"),
]

assert len({label for label, _ in hash_targets}) == len(hash_targets)
hash_rows = []
for label, path in hash_targets:
    assert path.exists(), path
    hash_rows.append({"relative_path": label, "bytes": path.stat().st_size, "sha256": sha(path)})

hash_manifest = QA / "SHA256SUMS_v6.csv"
with hash_manifest.open("w", encoding="utf-8-sig", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=["relative_path", "bytes", "sha256"])
    writer.writeheader()
    writer.writerows(hash_rows)

gate = {
    "artifact": "ROMANCE_ACCEPTANCE_GATE_v6",
    "machine_validation": "PASS",
    "goal_status": "ACTIVE_NOT_COMPLETE",
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
        "evidence_records": 350,
        "relation_records": 402,
        "valid_target_id_relation_edges": 27,
        "concept_to_sense_membership_edges": 106,
        "total_id_resolved_references_including_memberships": 133,
        "occurrence_review_cursor": "T01_T20_complete_plus_RM_RG_T45_T57_next_contiguous_T21",
        "human_observations": 0,
        "core_form_promotions": 0,
    },
    "stage_D": {
        "status": "T001_T002_PRODUCTION_TRANCHES_PASS_NOT_LANGUAGE_VALIDATED",
        "T001_body_lines": "21047-21087",
        "T001_metadata_lines": "20985-20990",
        "T002_body_lines": "21089-21097",
        "next_authority_line": 21099,
        "human_validation": 0,
    },
    "canonical_cohort_topology": {
        "artifact": "ROMANCE_FAMILY_COHORT_TREE_v2",
        "cohort_count": 9,
        "cohort_ids": tree_ids,
        "human_observations": 0,
        "MII_result_feeds_decisions": False,
    },
    "core_evidence_boundary": {
        "inherited_es_fr_records": 120,
        "inherited_core_quotations": 0,
        "extension_context_to_core_promotions": 0,
    },
    "romansh": "one_verified_official_bilingual_general_school_math_body_zero_specialist_algebra_bodies_five_zero_source_idioms",
    "pilot_claim": False,
    "full_R823_romance_translation_claim": False,
    "hash_target_count": len(hash_rows),
    "hash_manifest_sha256": sha(hash_manifest),
    "key_hashes": {row["relative_path"]: row["sha256"] for row in hash_rows},
}
(QA / "ROMANCE_ACCEPTANCE_GATE_v6.json").write_text(json.dumps(gate, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

lines = [
    "PASS machine_validation",
    "goal_status=ACTIVE_NOT_COMPLETE",
    "stage_A=NOT_COMPLETE active_routes=8 explicit_zero_routes=53 romansh_active=1 romansh_specialist_algebra=0",
    "stage_B=CURRENT_CORPUS_TRANCHE_PASS records=146 primary_unique=140 counting_eligible=64",
    "stage_C=PARTIAL concepts=60 senses=106 evidence=350 relation_records=402 valid_target_edges=27 memberships=106 total_resolved=133 reviewed_T01_T20_plus_RM_T45_T57 human=0 promotions=0",
    "stage_D=T001_T002_PRODUCTION_TRANCHES_PASS_NOT_LANGUAGE_VALIDATED next=21099",
    "cohorts=9 human_observations=0 MII_result_feeds_decisions=false",
    "pilot_claim=false full_R823_romance_translation_claim=false",
    f"hash_targets={len(hash_rows)} sha256_manifest={sha(hash_manifest)}",
]
(QA / "ROMANCE_ACCEPTANCE_GATE_v6.log").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
