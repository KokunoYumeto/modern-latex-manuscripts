from __future__ import annotations

import csv
import hashlib
import json
import re
import subprocess
import sys
import unicodedata
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LANG = ROOT / "language"
QA = ROOT / "qa"
BUILDER = ROOT / "scripts/build_controlled_romance_spec_v3.py"
GRAMMAR = LANG / "CONTROLLED_ROMANCE_GRAMMAR_DECISIONS_T001_T008_v3.csv"
FUNCTIONS = LANG / "CONTROLLED_ROMANCE_FUNCTION_WORDS_T001_T008_v3.csv"
TERMS = LANG / "CONTROLLED_ROMANCE_TERM_INVENTORY_T001_T008_v3.csv"
PROFILE = LANG / "CONTROLLED_ROMANCE_LANGUAGE_PROFILE_T001_T008_v3.md"
SUMMARY = LANG / "CONTROLLED_ROMANCE_LANGUAGE_PROFILE_T001_T008_v3.json"
BUILD_LOG = QA / "CONTROLLED_ROMANCE_LANGUAGE_PROFILE_BUILD_v3.log"
OLD_GRAMMAR = LANG / "CONTROLLED_ROMANCE_GRAMMAR_DECISIONS_T001_T007_v2.csv"
OLD_FUNCTIONS = LANG / "CONTROLLED_ROMANCE_FUNCTION_WORDS_T001_T007_v2.csv"
OLD_TERMS = LANG / "CONTROLLED_ROMANCE_TERM_INVENTORY_T001_T007_v2.csv"
OLD_AUDIT = QA / "CONTROLLED_ROMANCE_LANGUAGE_PROFILE_AUDIT_v2.json"
OLD_REPLAY_STATUS = QA / "CONTROLLED_ROMANCE_LANGUAGE_PROFILE_v2_REPLAY_LOG_STATUS.md"
OLD_REPLAY_1 = QA / "CONTROLLED_ROMANCE_LANGUAGE_PROFILE_AUDIT_v2_replay1.log"
OLD_REPLAY_2 = QA / "CONTROLLED_ROMANCE_LANGUAGE_PROFILE_AUDIT_v2_replay2.log"
T008_GRAMMAR = ROOT / "R823_HG_T008/grammar/CONTROLLED_ROMANCE_GRAMMAR_T008_DELTA_v1.csv"
T008_TERMS = ROOT / "R823_HG_T008/terminology/R823_HG_T008_TERMINOLOGY_v1.csv"
T008_VALIDATION = ROOT / "R823_HG_T008/qa/R823_HG_T008_validation.json"
T008_MANIFEST = ROOT / "R823_HG_T008/source/R823_HG_T008_SOURCE_MANIFEST.json"
WORDWEB = ROOT / "wordweb/PAN_ROMANCE_WORDWEB_v10.json"
RENDER = QA / "PDF_RENDER_REPRODUCIBILITY_v12.json"
REPORT = QA / "CONTROLLED_ROMANCE_LANGUAGE_PROFILE_AUDIT_v3.json"
LOG = QA / "CONTROLLED_ROMANCE_LANGUAGE_PROFILE_AUDIT_v3.log"


NEW_FUNCTION_LOCATORS = {
    "segun": "R823_HG_T008:T-080",
    "aqui": "R823_HG_T008:T-083",
    "al maxime": "R823_HG_T008:T-083",
    "il existe": "R823_HG_T008:T-085",
    "pois": "R823_HG_T008:editorial-note",
    "ante": "R823_HG_T003:editorial-note",
    "solmente": "R823_HG_T001:T-016",
    "mesmo": "R823_HG_T008:T-080",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def truth(value: object) -> bool:
    return str(value).casefold() == "true"


def norm(value: str) -> str:
    return re.sub(r"\s+", " ", unicodedata.normalize("NFC", value).casefold().strip())


def alternatives(value: str) -> list[str]:
    return [item.strip() for item in re.split(r"[|;]", value or "") if item.strip()]


def exact_carrier(surface: str, values: str) -> bool:
    return norm(surface) in {norm(item) for item in alternatives(values)}


def diagnostic(es: bool, fr: bool) -> str:
    return "both_exact" if es and fr else "spanish_exact" if es else "french_exact" if fr else "no_exact_dominant_carrier"


def link_tokens(value: str) -> list[str]:
    return [item.strip() for item in re.split(r"\s*\+\s*|\s*;\s*", value or "") if item.strip()]


def surface_pattern(surface: str) -> re.Pattern[str]:
    if " ... " in surface:
        left, right = surface.split(" ... ", 1)
        body = re.escape(left) + r"[\s\S]*?" + re.escape(right)
    else:
        body = re.escape(surface)
    return re.compile(r"(?<![\w])" + body + r"(?![\w])", re.IGNORECASE)


def ordered_controlled_blocks(tranche: str) -> list[tuple[set[str], str]]:
    path = ROOT / f"{tranche}/tex/{tranche}_romance.tex"
    lines = path.read_text(encoding="utf-8").splitlines()
    editorial_line = next((i for i, line in enumerate(lines) if line == r"\section*{Nota editorial de senso}"), len(lines))
    limits_line = next((i for i, line in enumerate(lines) if line == r"\section*{Limites del tranche}"), len(lines))
    source_end = min(editorial_line, limits_line)
    starts: list[tuple[int, set[str]]] = []
    for index, line in enumerate(lines):
        if index < source_end and line.startswith("% T-") and not line.startswith(("% T-E", "% T-H")):
            identifiers = set(re.findall(r"T-\d+[A-Z]?", line))
            if identifiers:
                starts.append((index, identifiers))
    blocks: list[tuple[set[str], str]] = []
    for position, (start, identifiers) in enumerate(starts):
        end = starts[position + 1][0] if position + 1 < len(starts) else source_end
        blocks.append((identifiers, "\n".join(lines[start + 1:end])))
    full_text = "\n".join(lines)
    editorial_marker = r"\section*{Nota editorial de senso}"
    limits_marker = r"\section*{Limites del tranche}"
    if editorial_marker in full_text:
        editorial = full_text.split(editorial_marker, 1)[1]
        if limits_marker in editorial:
            editorial, limits = editorial.split(limits_marker, 1)
            blocks.append(({"editorial-note"}, editorial))
            blocks.append(({"limits-note"}, limits))
        else:
            blocks.append(({"editorial-note"}, editorial))
    elif limits_marker in full_text:
        blocks.append(({"limits-note"}, full_text.split(limits_marker, 1)[1]))
    return blocks


def main() -> None:
    grammar = read_csv(GRAMMAR)
    functions = read_csv(FUNCTIONS)
    terms = read_csv(TERMS)
    summary = json.loads(SUMMARY.read_text(encoding="utf-8"))
    render = json.loads(RENDER.read_text(encoding="utf-8"))
    validation = json.loads(T008_VALIDATION.read_text(encoding="utf-8"))
    wordweb = json.loads(WORDWEB.read_text(encoding="utf-8"))
    old_grammar = read_csv(OLD_GRAMMAR)
    old_functions = read_csv(OLD_FUNCTIONS)
    old_terms = read_csv(OLD_TERMS)
    raw_t008_grammar = read_csv(T008_GRAMMAR)
    raw_t008_terms = read_csv(T008_TERMS)
    valid_ids = {sense["sense_id"] for sense in wordweb["senses"]} | {node["concept_id"] for node in wordweb["c2_extension_nodes"]}
    checks: dict[str, bool] = {}

    expected_grammar = len(old_grammar) + len(raw_t008_grammar)
    checks["grammar_predecessor_prefix_preserved"] = grammar[:len(old_grammar)] == old_grammar
    checks["grammar_T008_count_and_features_exact"] = len(grammar) == expected_grammar and len(raw_t008_grammar) == 13 and [row["feature"] for row in grammar[len(old_grammar):]] == [row["feature"] for row in raw_t008_grammar]
    checks["grammar_ids_unique_ordered"] = [row["decision_id"] for row in grammar] == [f"G{i:03d}" for i in range(1, expected_grammar + 1)]
    checks["grammar_T008_source_hash_bound"] = all(row["source_ledger_path"] == rel(T008_GRAMMAR) and row["source_ledger_sha256"] == sha(T008_GRAMMAR) for row in grammar[len(old_grammar):])
    checks["grammar_source_hashes_current"] = all((ROOT / row["source_ledger_path"]).exists() and sha(ROOT / row["source_ledger_path"]) == row["source_ledger_sha256"] for row in grammar)
    checks["grammar_rationale_adverse_alternatives_nonempty"] = all(row["supporting_rationale"] and row["adverse_evidence"] and row["alternatives_considered"] for row in grammar)
    checks["grammar_zero_human_no_promotion"] = all(row["human_observations"] == "0" and not truth(row["native_validation"]) and row["promotion_effect"] == "none" for row in grammar)
    anti_row = next(row for row in grammar if row["source_tranche"] == "R823_HG_T008" and row["feature"] == "anti_dominance_surface")
    checks["grammar_T008_invariant_iste_rejects_istes"] = "invariant iste" in anti_row["decision"] and "plural istes" in anti_row["decision"] and "would contradict" in anti_row["adverse_evidence"]

    expected_functions = len(old_functions) + len(NEW_FUNCTION_LOCATORS)
    checks["function_count_and_ids_exact"] = len(functions) == expected_functions and [row["function_id"] for row in functions] == [f"F{i:03d}" for i in range(1, expected_functions + 1)]
    checks["function_surface_unique"] = len({row["surface_form"] for row in functions}) == len(functions)
    checks["function_new_set_and_locators_exact"] = {row["surface_form"]: row["first_controlled_use"] for row in functions[len(old_functions):]} == NEW_FUNCTION_LOCATORS
    ordinary_mutable = {"controlled_use_tranches", "usage_check", "exact_spanish_carrier", "exact_french_carrier", "dominance_diagnostic"}
    special_mutable = ordinary_mutable | {"supporting_rationale", "adverse_evidence"}
    predecessor_semantics = True
    for new, old in zip(functions[:len(old_functions)], old_functions, strict=True):
        mutable = special_mutable if old["surface_form"] in {"iste", "mesme"} else ordinary_mutable
        predecessor_semantics = predecessor_semantics and all(new[key] == old[key] for key in old if key not in mutable)
    checks["function_predecessor_semantics_preserved_with_two_documented_reconciliations"] = predecessor_semantics
    checks["function_all_used_or_structural"] = all(row["usage_check"] in {"surface_sequence_found_in_target_tex", "structural_rule_not_token_counted"} for row in functions)
    checks["function_new_forms_all_used_in_T008"] = all("R823_HG_T008" in row["controlled_use_tranches"].split(";") for row in functions[len(old_functions):])
    checks["function_rationale_adverse_comparators_nonempty"] = all(row["supporting_rationale"] and row["adverse_evidence"] and row["spanish_comparators"] and row["french_comparators"] for row in functions)
    carrier_truth = True
    function_diagnostics: Counter[str] = Counter()
    for row in functions:
        es = exact_carrier(row["surface_form"], row["spanish_comparators"])
        fr = exact_carrier(row["surface_form"], row["french_comparators"])
        expected = diagnostic(es, fr)
        carrier_truth = carrier_truth and truth(row["exact_spanish_carrier"]) == es and truth(row["exact_french_carrier"]) == fr and row["dominance_diagnostic"] == expected
        function_diagnostics[expected] += 1
    checks["function_carrier_flags_and_diagnostics_recomputed"] = carrier_truth
    checks["function_summary_diagnostic_partition_recomputed"] = summary["anti_collapse"]["function_word_diagnostics"] == dict(sorted(function_diagnostics.items()))
    checks["function_first_use_matches_earliest_detected_tranche"] = all(row["controlled_use_tranches"].split(";")[0] == row["first_controlled_use"].split(":")[0] for row in functions)
    block_cache: dict[str, list[tuple[set[str], str]]] = {}
    locator_truth = True
    for row in functions:
        if row["surface_form"] == "-s":
            continue
        tranche, declared = row["first_controlled_use"].split(":", 1)
        blocks = block_cache.setdefault(tranche, ordered_controlled_blocks(tranche))
        matching_blocks = [ids for ids, text in blocks if surface_pattern(row["surface_form"]).search(text)]
        locator_truth = locator_truth and any(ids & set(declared.split("+")) for ids in matching_blocks)
    checks["function_first_use_exact_locator_contains_surface"] = locator_truth
    checks["function_zero_human_no_promotion"] = all(row["human_observations"] == "0" and not truth(row["native_validation"]) and row["promotion_effect"] == "none" for row in functions)
    function_map = {row["surface_form"]: row for row in functions}
    all_tex = "\n".join((ROOT / f"R823_HG_T{i:03d}/tex/R823_HG_T{i:03d}_romance.tex").read_text(encoding="utf-8") for i in range(1, 9))
    checks["invariant_iste_live_and_istes_absent"] = "R823_HG_T008" in function_map["iste"]["controlled_use_tranches"].split(";") and not re.search(r"(?<![\w])istes(?![\w])", all_tex, re.IGNORECASE)
    checks["mesme_mesmo_sense_separated_not_allomorphic"] = function_map["mesme"]["function"] == "anaphoric identity/emphasis marker" and function_map["mesmo"]["function"] == "scalar emphasis particle (even/just)" and "not licensed as an agreement variant" in function_map["mesme"]["adverse_evidence"] and "not an agreement variant" in function_map["mesmo"]["adverse_evidence"]

    expected_terms = len(old_terms) + len(raw_t008_terms)
    checks["terms_predecessor_prefix_preserved"] = terms[:len(old_terms)] == old_terms
    checks["terms_T008_count_and_source_ids_exact"] = len(terms) == expected_terms and len(raw_t008_terms) == 21 and [row["term_id"] for row in terms[len(old_terms):]] == [row["term_id"] for row in raw_t008_terms]
    checks["term_inventory_ids_unique_ordered"] = [row["inventory_id"] for row in terms] == [f"L{i:03d}" for i in range(1, expected_terms + 1)]
    checks["term_source_ids_unique"] = len({(row["tranche"], row["term_id"]) for row in terms}) == len(terms)
    checks["terms_T008_source_hash_bound"] = all(row["source_ledger_path"] == rel(T008_TERMS) and row["source_ledger_sha256"] == sha(T008_TERMS) for row in terms[len(old_terms):])
    checks["term_source_hashes_current"] = all((ROOT / row["source_ledger_path"]).exists() and sha(ROOT / row["source_ledger_path"]) == row["source_ledger_sha256"] for row in terms)
    checks["term_rationale_adverse_alternatives_nonempty"] = all(row["source_rationale"] and row["adverse_evidence"] and row["alternatives_or_crosswalk"] for row in terms)
    checks["term_zero_human_no_promotion"] = all(row["human_observations"] == "0" and not truth(row["native_validation"]) and row["promotion_effect"] == "none" and row["attestation_effect"].startswith("none") for row in terms)
    normalization_truth = True
    gap_count = 0
    for raw, row in zip(raw_t008_terms, terms[len(old_terms):], strict=True):
        tokens = link_tokens(raw["wordweb_link"])
        resolved = [item for item in tokens if item in valid_ids]
        gaps = [item for item in tokens if item.startswith("none_")]
        invalid = [item for item in tokens if item not in valid_ids and not item.startswith("none_")]
        gap_count += len(gaps)
        normalization_truth = normalization_truth and not invalid and row["effective_wordweb_link"] == ";".join(resolved) and all(gap in row["semantic_compatibility_rationale"] for gap in gaps)
    checks["T008_mixed_wordweb_links_normalized_with_gaps_recorded"] = normalization_truth and gap_count == validation["counts"]["explicit_wordweb_gap_links"]
    checks["term_effective_links_have_no_none_sentinels"] = all(not any(item.startswith("none_") for item in link_tokens(row["effective_wordweb_link"])) for row in terms)
    linked_ids = [item for row in terms for item in link_tokens(row["effective_wordweb_link"])]
    checks["term_links_resolve_wordweb_v10"] = all(item in valid_ids for item in linked_ids)
    term_carrier_truth = True
    term_diagnostics: Counter[str] = Counter()
    for row in terms:
        if row["comparison_method"] == "not_comparable":
            es = fr = False
            expected = "not_comparable_no_exact_standard_row"
        else:
            es = exact_carrier(row["target_term"], row["spanish_comparators"])
            fr = exact_carrier(row["target_term"], row["french_comparators"])
            expected = diagnostic(es, fr)
        term_carrier_truth = term_carrier_truth and truth(row["exact_spanish_carrier"]) == es and truth(row["exact_french_carrier"]) == fr and row["dominance_diagnostic"] == expected
        term_diagnostics[expected] += 1
    checks["term_carrier_flags_and_diagnostics_recomputed"] = term_carrier_truth
    checks["term_summary_diagnostic_partition_recomputed"] = summary["anti_collapse"]["terminology_diagnostics"] == dict(sorted(term_diagnostics.items()))

    linked_rows = sum(bool(row["effective_wordweb_link"]) for row in terms)
    expected_counts = {
        "grammar_decisions": len(grammar),
        "function_word_decisions": len(functions),
        "terminology_decisions": len(terms),
        "distinct_target_terms": len({row["target_term"] for row in terms}),
        "linked_terminology_rows": linked_rows,
        "explicitly_unlinked_terminology_rows": len(terms) - linked_rows,
        "effective_wordweb_identifier_references": len(linked_ids),
        "T008_explicit_gap_sentinels_recorded_not_linked": gap_count,
        "source_keyed_tranches": 8,
        "rendered_pages": 19,
        "human_observations": 0,
        "native_validations": 0,
        "form_promotions": 0,
    }
    checks["summary_counts_recomputed_exact"] = summary["counts"] == expected_counts
    checks["summary_next_line_21309"] = summary["next_source_line"] == 21309
    checks["summary_input_hashes_current"] = all((ROOT / label).exists() and sha(ROOT / label) == digest for label, digest in summary["input_hashes"].items())
    checks["summary_output_hashes_current"] = all((ROOT / label).exists() and sha(ROOT / label) == digest for label, digest in summary["output_hashes"].items())
    checks["summary_zero_empirical_boundary"] = summary["empirical_claim_boundary"] == {"human_observations": 0, "native_validated": False, "intelligibility_claim": False, "MII_claim": False, "pilot_claim": False, "full_R823_translation_claim": False}
    checks["summary_no_dominant_pivot_or_slash_bundles"] = summary["anti_collapse"]["spanish_or_french_pivot_authorized"] is False and summary["anti_collapse"]["slash_bundles_authorized_in_running_prose"] is False
    checks["summary_link_normalization_contract_explicit"] = summary["link_normalization_contract"]["unknown_non_sentinel_identifiers_allowed"] is False and "excluded" in summary["link_normalization_contract"]["none_sentinels"]
    checks["predecessor_replay_logs_preserved_and_marked_historical"] = sha(OLD_REPLAY_1) == sha(OLD_REPLAY_2) == "CB604C5E56D7727B938CA67A4E994D3FAFEC863039F1DA6499E4CAC31A72F79F" and "historical" in OLD_REPLAY_STATUS.read_text(encoding="utf-8").casefold() and "must not be cited" in OLD_REPLAY_STATUS.read_text(encoding="utf-8").casefold()
    live_old_audit = json.loads(OLD_AUDIT.read_text(encoding="utf-8"))
    checks["predecessor_live_audit_is_50_of_50"] = live_old_audit["status"] == "PASS" and live_old_audit["counts"]["checks"] == live_old_audit["counts"]["checks_passed"] == 50

    production = summary["production"]
    checks["production_exact_T001_T008"] = [row["tranche"] for row in production] == [f"R823_HG_T{i:03d}" for i in range(1, 9)]
    checks["production_19_pages_and_cursor"] = sum(int(row["pages"]) for row in production) == 19 and production[-1]["next_source_line"] == 21309
    checks["production_validators_pass"] = all(str(row["validation_status"]).startswith("PASS") for row in production)
    checks["production_pdf_hashes_current"] = all(sha(ROOT / f"{row['tranche']}/build/{row['tranche']}_romance.pdf") == row["pdf_sha256"] for row in production)
    output_root = ROOT.parents[3] / "output/pdf"
    checks["production_output_copies_identical"] = all((ROOT / f"{row['tranche']}/build/{row['tranche']}_romance.pdf").read_bytes() == (output_root / f"{row['tranche']}_controlled_romance.pdf").read_bytes() for row in production)
    checks["T008_validation_live_hashes_bound"] = production[-1]["target_tex_sha256"] == validation["hashes"]["target_tex"] and production[-1]["pdf_sha256"] == validation["hashes"]["build_pdf"] and production[-1]["source_slice_sha256"] == validation["authority_slice_sha256"]
    checks["render_v12_exact_surface_PASS"] = render["status"] == "PASS" and render["totals"] == {"tranches": 8, "build_pdfs": 8, "final_output_pdfs": 8, "pinned_pages": 19, "fresh_pages": 19, "all_build_output_pdfs_byte_identical": True, "all_fresh_pinned_pngs_byte_identical": True}
    t008_render = next(row for row in render["tranches"] if row["tranche"] == "R823_HG_T008")
    checks["render_v12_T008_matches_live_validation"] = t008_render["build_pdf"]["sha256"] == validation["hashes"]["build_pdf"] and t008_render["final_output_pdf"]["sha256"] == validation["hashes"]["output_pdf"] and [page["pinned_render"]["sha256"] for page in t008_render["pages"]] == [validation["render_sha256"][f"R823_HG_T008_page-{i}.png"] for i in (1, 2)]
    lexical_bundle = re.compile(r"(?<![\w])[^\W\d_]+/[^\W\d_]+(?![\w])", re.UNICODE)
    checks["production_no_lexical_slash_bundles"] = all(not lexical_bundle.search((ROOT / f"R823_HG_T{i:03d}/tex/R823_HG_T{i:03d}_romance.tex").read_text(encoding="utf-8")) for i in range(1, 9))

    profile = PROFILE.read_text(encoding="utf-8")
    checks["profile_claim_boundaries_explicit"] = all(phrase.casefold() in profile.casefold() for phrase in ["zero human observations", "zero native validation", "form promotions = 0", "pilot claim = false", "full-R823 translation claim = false", "not a claim"])
    checks["profile_T008_pages_cursor_explicit"] = all(phrase in profile for phrase in ["T001-T008", "19 rendered pages", "21309", "§7"])
    checks["profile_mesme_mesmo_iste_reconciliation_explicit"] = all(phrase in profile for phrase in ["`mesme` and `mesmo` are not free variants", "invariant `iste`", "`istes` is not licensed"])

    generated = [GRAMMAR, FUNCTIONS, TERMS, PROFILE, SUMMARY, BUILD_LOG]
    before = {rel(path): sha(path) for path in generated}
    replay = subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, text=True, capture_output=True)
    after = {rel(path): sha(path) for path in generated}
    checks["builder_replay_exit_zero"] = replay.returncode == 0
    checks["builder_replay_byte_stable"] = before == after

    passed = all(checks.values())
    payload = {
        "artifact": "CONTROLLED_ROMANCE_LANGUAGE_PROFILE_AUDIT_v3",
        "status": "PASS" if passed else "FAIL",
        "scope": "Independent structural replay, exact first-use locators, source/hash integrity, per-token WordWeb-link normalization, anti-collapse registry, T001-T008 production/output/render binding, and explicit zero-human boundary.",
        "counts": {"checks": len(checks), "checks_passed": sum(checks.values()), **expected_counts},
        "checks": checks,
        "computed_diagnostics": {
            "function_word_diagnostics": dict(sorted(function_diagnostics.items())),
            "terminology_diagnostics": dict(sorted(term_diagnostics.items())),
        },
        "replay": {"command": [sys.executable, rel(BUILDER)], "exit_code": replay.returncode, "stdout": replay.stdout, "stderr": replay.stderr, "before_hashes": before, "after_hashes": after},
        "artifact_hashes": {rel(path): sha(path) for path in [GRAMMAR, FUNCTIONS, TERMS, PROFILE, SUMMARY, BUILD_LOG, BUILDER, Path(__file__).resolve(), RENDER, T008_VALIDATION, OLD_REPLAY_STATUS]},
        "claim_boundary": summary["empirical_claim_boundary"],
    }
    REPORT.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    failed = [key for key, value in checks.items() if not value]
    lines = [
        f"{'PASS' if passed else 'FAIL'} controlled Romance language profile v3 checks={len(checks)} passed={sum(checks.values())}",
        f"grammar={len(grammar)} functions={len(functions)} terms={len(terms)} linked={linked_rows} unlinked={len(terms)-linked_rows} identifier_refs={len(linked_ids)} T008_gaps={gap_count} tranches=8 pages=19 next=21309",
        "human_observations=0 native_validations=0 promotions=0 pilot_claim=false",
        f"audit_sha256={sha(REPORT)}",
    ] + [f"FAIL {item}" for item in failed]
    LOG.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print("\n".join(lines))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
