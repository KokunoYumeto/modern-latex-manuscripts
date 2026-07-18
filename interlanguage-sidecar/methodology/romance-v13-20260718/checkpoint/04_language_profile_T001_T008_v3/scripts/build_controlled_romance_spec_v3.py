from __future__ import annotations

import csv
import hashlib
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LANG = ROOT / "language"
QA = ROOT / "qa"

OLD_GRAMMAR = LANG / "CONTROLLED_ROMANCE_GRAMMAR_DECISIONS_T001_T007_v2.csv"
OLD_FUNCTIONS = LANG / "CONTROLLED_ROMANCE_FUNCTION_WORDS_T001_T007_v2.csv"
OLD_TERMS = LANG / "CONTROLLED_ROMANCE_TERM_INVENTORY_T001_T007_v2.csv"
OLD_SUMMARY = LANG / "CONTROLLED_ROMANCE_LANGUAGE_PROFILE_T001_T007_v2.json"
OLD_AUDIT = QA / "CONTROLLED_ROMANCE_LANGUAGE_PROFILE_AUDIT_v2.json"
OLD_REPLAY_STATUS = QA / "CONTROLLED_ROMANCE_LANGUAGE_PROFILE_v2_REPLAY_LOG_STATUS.md"
T008_GRAMMAR = ROOT / "R823_HG_T008/grammar/CONTROLLED_ROMANCE_GRAMMAR_T008_DELTA_v1.csv"
T008_TERMS = ROOT / "R823_HG_T008/terminology/R823_HG_T008_TERMINOLOGY_v1.csv"
T008_TEX = ROOT / "R823_HG_T008/tex/R823_HG_T008_romance.tex"
T008_VALIDATION = ROOT / "R823_HG_T008/qa/R823_HG_T008_validation.json"
T008_MANIFEST = ROOT / "R823_HG_T008/source/R823_HG_T008_SOURCE_MANIFEST.json"
WORDWEB = ROOT / "wordweb/PAN_ROMANCE_WORDWEB_v10.json"
RENDER = QA / "PDF_RENDER_REPRODUCIBILITY_v12.json"

GRAMMAR_OUT = LANG / "CONTROLLED_ROMANCE_GRAMMAR_DECISIONS_T001_T008_v3.csv"
FUNCTION_OUT = LANG / "CONTROLLED_ROMANCE_FUNCTION_WORDS_T001_T008_v3.csv"
TERMS_OUT = LANG / "CONTROLLED_ROMANCE_TERM_INVENTORY_T001_T008_v3.csv"
PROFILE_OUT = LANG / "CONTROLLED_ROMANCE_LANGUAGE_PROFILE_T001_T008_v3.md"
SUMMARY_OUT = LANG / "CONTROLLED_ROMANCE_LANGUAGE_PROFILE_T001_T008_v3.json"
LOG_OUT = QA / "CONTROLLED_ROMANCE_LANGUAGE_PROFILE_BUILD_v3.log"


NEW_FUNCTIONS = [
    (
        "segun",
        "source-attribution preposition",
        "R823_HG_T008:T-080",
        "según|de acuerdo con",
        "selon|d'après",
        "Introduces the exact M. Z. section locator without turning it into a proof premise.",
        "Portuguese/Galician-adjacent and one accent away from Spanish; the form has no human access evidence.",
    ),
    (
        "aqui",
        "local discourse-anchor adverb",
        "R823_HG_T008:T-083",
        "aquí",
        "ici",
        "Anchors the local definition of t to the immediately displayed quotient rank.",
        "Exact in Portuguese/Galician and accent-adjacent to Spanish; discourse processing is untested.",
    ),
    (
        "al maxime",
        "upper-bound operator",
        "R823_HG_T008:T-083",
        "como máximo|a lo sumo",
        "au plus|tout au plus",
        "Marks the non-strict upper bound t less than or equal to n in prose beside the formulaic variables.",
        "An analytic constructed sequence rather than a native-neutral pan-Romance form.",
    ),
    (
        "il existe",
        "existential clause operator",
        "R823_HG_T008:T-085",
        "existe|hay",
        "il existe",
        "Introduces the exact cardinality assertion for the t homomorphisms.",
        "Exact French carrier and therefore an explicit French-dominance risk.",
    ),
    (
        "pois",
        "causal-sequential connector",
        "R823_HG_T008:editorial-note",
        "pues|puesto que|después",
        "puisque|puis",
        "Makes the algebraic-closure step follow the finite-degree-field decomposition in the source audit.",
        "Portuguese/Galician-shaped and semantically spans causal and sequential uses; fixed here to the stated inference.",
    ),
    (
        "ante",
        "temporal-before preposition",
        "R823_HG_T003:editorial-note",
        "antes de",
        "avant",
        "Marks temporal deferral: T003 postpones modernization until historical review, and T008 keeps section-7 map types out of section 6.",
        "Spanish ante has broader literary and spatial readings; this registry permits only the temporal-before reading.",
    ),
    (
        "solmente",
        "restrictive focus particle",
        "R823_HG_T001:T-016",
        "solamente|solo",
        "seulement|uniquement",
        "Scopes a restriction over one constituent; its paired use inside non solmente ... ma etiam remains separately registered.",
        "Close to both dominant standards and potentially confused with the longer biconditional and not-only constructions.",
    ),
    (
        "mesmo",
        "scalar emphasis particle (even/just)",
        "R823_HG_T008:T-080",
        "incluso|aun|hasta",
        "même",
        "In il suffice mesmo, adds scalar emphasis to the permitted restriction without expressing referential identity.",
        "Portuguese/Galician form; it is not an agreement variant or free allomorph of controlled mesme.",
    ),
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def norm(value: str) -> str:
    return re.sub(r"\s+", " ", unicodedata.normalize("NFC", value).casefold().strip())


def alternatives(value: str) -> list[str]:
    return [item.strip() for item in re.split(r"[|;]", value or "") if item.strip()]


def exact(surface: str, values: str) -> bool:
    return norm(surface) in {norm(value) for value in alternatives(values)}


def diagnostic(es: bool, fr: bool) -> str:
    return "both_exact" if es and fr else "spanish_exact" if es else "french_exact" if fr else "no_exact_dominant_carrier"


def surface_pattern(surface: str) -> re.Pattern[str]:
    if " ... " in surface:
        left, right = surface.split(" ... ", 1)
        body = re.escape(left) + r"[\s\S]*?" + re.escape(right)
    else:
        body = re.escape(surface)
    return re.compile(r"(?<![\w])" + body + r"(?![\w])", re.IGNORECASE)


def normalize_link_cell(value: str, valid_ids: set[str]) -> tuple[list[str], list[str], list[str]]:
    tokens = [item.strip() for item in re.split(r"\s*\+\s*|\s*;\s*", value or "") if item.strip()]
    resolved = [item for item in tokens if item in valid_ids]
    gaps = [item for item in tokens if item.startswith("none_")]
    invalid = [item for item in tokens if item not in valid_ids and not item.startswith("none_")]
    return resolved, gaps, invalid


def build_grammar() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = [dict(row) for row in read_csv(OLD_GRAMMAR)]
    source_hash = sha(T008_GRAMMAR)
    for source in read_csv(T008_GRAMMAR):
        rows.append({
            "decision_id": f"G{len(rows) + 1:03d}",
            "source_tranche": "R823_HG_T008",
            "source_ledger_path": rel(T008_GRAMMAR),
            "source_ledger_sha256": source_hash,
            "feature": source["feature"],
            "decision": source["decision"],
            "alternatives_considered": source["alternatives_considered"],
            "supporting_rationale": source["supporting_rationale"],
            "adverse_evidence": source["adverse_evidence"],
            "status": source["status"],
            "scope": "source_keyed_test_tranche_T008_only",
            "evidence_tier": "E0_constructed_control_with_source_use",
            "human_observations": 0,
            "native_validation": False,
            "promotion_effect": "none",
        })
    return rows


def build_functions() -> list[dict[str, object]]:
    texts = {
        f"R823_HG_T{n:03d}": (ROOT / f"R823_HG_T{n:03d}/tex/R823_HG_T{n:03d}_romance.tex").read_text(encoding="utf-8")
        for n in range(1, 9)
    }
    rows: list[dict[str, object]] = []
    for old in read_csv(OLD_FUNCTIONS):
        row: dict[str, object] = dict(old)
        surface = old["surface_form"]
        if surface == "-s":
            uses = list(texts)
            usage = "structural_rule_not_token_counted"
        else:
            pattern = surface_pattern(surface)
            uses = [tranche for tranche, text in texts.items() if pattern.search(text)]
            usage = "surface_sequence_found_in_target_tex" if uses else "surface_sequence_not_found"
        row["controlled_use_tranches"] = ";".join(uses)
        row["usage_check"] = usage
        es_match = exact(surface, old["spanish_comparators"])
        fr_match = exact(surface, old["french_comparators"])
        row["exact_spanish_carrier"] = es_match
        row["exact_french_carrier"] = fr_match
        row["dominance_diagnostic"] = diagnostic(es_match, fr_match)
        if surface == "iste":
            row["supporting_rationale"] = old["supporting_rationale"] + " T008 confirms the invariant surface after repairing the rejected plural istes."
            row["adverse_evidence"] = old["adverse_evidence"] + " Number-inflected istes is explicitly rejected by the live T008 contract."
        elif surface == "mesme":
            row["supporting_rationale"] = old["supporting_rationale"] + " T008 retains mesme for referential identity while scalar mesmo receives a separate entry."
            row["adverse_evidence"] = old["adverse_evidence"] + " Mesmo is not licensed as an agreement variant or free allomorph."
        rows.append(row)
    for surface, function, first_use, es_values, fr_values, rationale, adverse in NEW_FUNCTIONS:
        pattern = surface_pattern(surface)
        uses = [tranche for tranche, text in texts.items() if pattern.search(text)]
        es_match = exact(surface, es_values)
        fr_match = exact(surface, fr_values)
        rows.append({
            "function_id": f"F{len(rows) + 1:03d}",
            "surface_form": surface,
            "function": function,
            "construction_status": "active_test_operator_unreviewed",
            "first_controlled_use": first_use,
            "controlled_use_tranches": ";".join(uses),
            "usage_check": "surface_sequence_found_in_target_tex" if uses else "surface_sequence_not_found",
            "spanish_comparators": es_values,
            "french_comparators": fr_values,
            "exact_spanish_carrier": es_match,
            "exact_french_carrier": fr_match,
            "dominance_diagnostic": diagnostic(es_match, fr_match),
            "supporting_rationale": rationale,
            "adverse_evidence": adverse,
            "human_observations": 0,
            "native_validation": False,
            "promotion_effect": "none",
            "review_status": "human_and_multibranch_review_required",
        })
    return rows


def build_terms(valid_ids: set[str]) -> tuple[list[dict[str, object]], int]:
    rows: list[dict[str, object]] = []
    for predecessor in read_csv(OLD_TERMS):
        row: dict[str, object] = dict(predecessor)
        resolved, gaps, invalid = normalize_link_cell(predecessor["effective_wordweb_link"], valid_ids)
        assert not gaps and not invalid, (predecessor["inventory_id"], gaps, invalid)
        row["effective_wordweb_link"] = ";".join(resolved)
        rows.append(row)
    source_hash = sha(T008_TERMS)
    gap_count = 0
    for source in read_csv(T008_TERMS):
        resolved, gaps, invalid = normalize_link_cell(source["wordweb_link"], valid_ids)
        assert not invalid, (source["term_id"], invalid)
        gap_count += len(gaps)
        comps = alternatives(source["alternatives_or_crosswalk"])
        fr_values = comps[0] if comps else ""
        es_values = comps[1] if len(comps) > 1 else ""
        es_match = exact(source["target_term"], es_values)
        fr_match = exact(source["target_term"], fr_values)
        if resolved and gaps:
            semantic_status = "approved_T008_validator_resolved_links_with_explicit_gaps"
            semantic_rationale = f"Retained resolvable WordWeb v10 identifiers {';'.join(resolved)}; excluded gap sentinels {';'.join(gaps)} from graph linkage while preserving them here as unresolved requirements."
        elif resolved:
            semantic_status = "approved_T008_validator_resolved_link"
            semantic_rationale = f"Retained the T008 validator-resolved WordWeb v10 identifiers {';'.join(resolved)}."
        else:
            semantic_status = "explicit_unlinked_outside_reviewed_spine"
            semantic_rationale = f"No WordWeb v10 identifier is available; excluded and recorded explicit gap sentinels {';'.join(gaps)} without nearest-neighbour inference."
        rows.append({
            "inventory_id": f"L{len(rows) + 1:03d}",
            "tranche": "R823_HG_T008",
            "term_id": source["term_id"],
            "source_term": source["source_term"],
            "target_term": source["target_term"],
            "sense": source["sense"],
            "construction_status": source["status"],
            "source_evidence": source["source_evidence"],
            "source_ledger_path": rel(T008_TERMS),
            "source_ledger_sha256": source_hash,
            "effective_wordweb_link": ";".join(resolved),
            "semantic_compatibility_status": semantic_status,
            "semantic_compatibility_rationale": semantic_rationale,
            "alternatives_or_crosswalk": source["alternatives_or_crosswalk"],
            "adverse_evidence": source["adverse_evidence"],
            "source_rationale": source["rationale"],
            "comparison_method": "ordered_T008_french_then_spanish_comparator",
            "spanish_comparators": es_values,
            "french_comparators": fr_values,
            "exact_spanish_carrier": es_match,
            "exact_french_carrier": fr_match,
            "dominance_diagnostic": diagnostic(es_match, fr_match),
            "attestation_effect": "none_existing_evidence_only",
            "human_observations": 0,
            "native_validation": False,
            "promotion_effect": "none",
        })
    return rows, gap_count


def build_production(old: dict[str, object], validation: dict[str, object], manifest: dict[str, object], render: dict[str, object]) -> list[dict[str, object]]:
    rows = list(old["production"])
    t_render = next(row for row in render["tranches"] if row["tranche"] == "R823_HG_T008")
    assert t_render["build_pdf"]["sha256"] == validation["hashes"]["build_pdf"]
    assert t_render["final_output_pdf"]["sha256"] == validation["hashes"]["output_pdf"]
    rows.append({
        "tranche": "R823_HG_T008",
        "source_lines": f"{manifest['line_start']}-{manifest['line_end']}",
        "source_slice_sha256": manifest["exact_slice_sha256"],
        "target_tex_sha256": validation["hashes"]["target_tex"],
        "pdf_sha256": validation["hashes"]["build_pdf"],
        "pages": t_render["expected_page_count"],
        "validation_status": validation["status"],
        "next_source_line": manifest["next_line"],
    })
    return rows


def build_profile(grammar: list[dict[str, object]], functions: list[dict[str, object]], terms: list[dict[str, object]], production: list[dict[str, object]], gap_count: int) -> str:
    linked = sum(bool(row["effective_wordweb_link"]) for row in terms)
    function_risks = Counter(str(row["dominance_diagnostic"]) for row in functions)
    term_risks = Counter(str(row["dominance_diagnostic"]) for row in terms)
    return "\n".join([
        "# Controlled Romance language profile, T001-T008 v3",
        "",
        "Status: **provisional constructed written register; machine-validated production state, zero human observations, zero native validation, zero form promotions.** This profile records the language actually used in eight source-keyed R823 tranches. It is not a claim that any cohort finds the forms intelligible or natural.",
        "",
        "## Production and source boundary",
        "",
        f"The live sample comprises {len(production)} separately source-bound units and {sum(int(row['pages']) for row in production)} rendered pages. It reaches German authority line 21307; line 21308 is blank and the next semantic unit begins at line 21309 (§7). Each unit retains its own source slice, clause map, terminology, grammar, validation, PDF and visual evidence.",
        "",
        "## Reusable grammar contract",
        "",
        f"The grammar ledger contains {len(grammar)} source-keyed decisions. T008 adds thirteen controls for section scope, the stronger field hypothesis, two-direction reduction, basis sufficiency, regular representation, unspecialized radical, the reducibility chain, identity-element sense, representation classes and degree, singleton conjugation, homomorphism endpoints, anti-dominance surface, and the zero-human boundary.",
        "",
        "## Function and connective layer",
        "",
        f"The function registry contains {len(functions)} declared forms. V3 registers `segun`, `aqui`, `al maxime`, `il existe`, `pois`, temporal `ante`, standalone restrictive `solmente`, and scalar `mesmo`. Dominant-carrier diagnostics, recomputed from the comparator fields, are {dict(sorted(function_risks.items()))}. Exact-string resemblance is a design diagnostic only, never an intelligibility measurement.",
        "",
        "`mesme` and `mesmo` are not free variants: `mesme` marks referential identity or self-reference, while T008 `mesmo` is the scalar emphasis particle in `il suffice mesmo`. The established demonstrative is invariant `iste`; the rejected number-inflected `istes` is not licensed.",
        "",
        "## Terminology and sense control",
        "",
        f"The terminology inventory contains {len(terms)} decisions and {len({str(row['target_term']) for row in terms})} distinct target strings; {linked} rows have one or more explicit WordWeb links and {len(terms)-linked} remain explicitly unlinked. T008 contributes 21 decisions. Its mixed link cells retain every resolvable v10 identifier and remove {gap_count} `none_*` sentinels from graph linkage while preserving each sentinel in the compatibility rationale as an unresolved gap. Term carrier diagnostics, recomputed from the comparator fields, are {dict(sorted(term_risks.items()))}.",
        "",
        "## Anti-collapse contract",
        "",
        "No Spanish or French pivot is authorized. Exact Spanish/French carriers are labelled rather than treated as neutral. T008 retains mixed morphology and invariant articles/demonstratives, but those constructed choices remain E0 source-use evidence with adverse review, not reader-access evidence.",
        "",
        "## Empirical boundary and next cursor",
        "",
        "Human observations = 0; native validations = 0; empirical MII observations = 0; form promotions = 0; pilot claim = false; full-R823 translation claim = false. The next source-keyed unit starts at authority line **21309**, §7, on the isomorphisms of a field.",
        "",
    ])


def main() -> None:
    old = json.loads(OLD_SUMMARY.read_text(encoding="utf-8"))
    validation = json.loads(T008_VALIDATION.read_text(encoding="utf-8"))
    manifest = json.loads(T008_MANIFEST.read_text(encoding="utf-8"))
    render = json.loads(RENDER.read_text(encoding="utf-8"))
    wordweb = json.loads(WORDWEB.read_text(encoding="utf-8"))
    assert validation["status"].startswith("PASS") and render["status"] == "PASS"
    assert validation["hashes"]["wordweb_v10"] == sha(WORDWEB)
    valid_ids = {sense["sense_id"] for sense in wordweb["senses"]} | {node["concept_id"] for node in wordweb["c2_extension_nodes"]}
    grammar = build_grammar()
    functions = build_functions()
    terms, gap_count = build_terms(valid_ids)
    production = build_production(old, validation, manifest, render)
    write_csv(GRAMMAR_OUT, grammar, list(grammar[0]))
    write_csv(FUNCTION_OUT, functions, list(functions[0]))
    write_csv(TERMS_OUT, terms, list(terms[0]))
    PROFILE_OUT.write_text(build_profile(grammar, functions, terms, production, gap_count), encoding="utf-8", newline="\n")
    linked = sum(bool(row["effective_wordweb_link"]) for row in terms)
    function_diagnostics = dict(sorted(Counter(str(row["dominance_diagnostic"]) for row in functions).items()))
    term_diagnostics = dict(sorted(Counter(str(row["dominance_diagnostic"]) for row in terms).items()))
    inputs = [OLD_GRAMMAR, OLD_FUNCTIONS, OLD_TERMS, OLD_SUMMARY, OLD_AUDIT, OLD_REPLAY_STATUS, T008_GRAMMAR, T008_TERMS, T008_TEX, T008_VALIDATION, T008_MANIFEST, WORDWEB, RENDER]
    summary = {
        "artifact": "CONTROLLED_ROMANCE_LANGUAGE_PROFILE_T001_T008_v3",
        "supersedes": "CONTROLLED_ROMANCE_LANGUAGE_PROFILE_T001_T007_v2",
        "status": "STRUCTURAL_LANGUAGE_CONTRACT_PASS_HUMAN_VALIDATION_ABSENT",
        "scope": "Consolidates actual grammar, function-word and terminology decisions used by R823_HG_T001 through R823_HG_T008 without mutating predecessor tranches.",
        "counts": {
            "grammar_decisions": len(grammar),
            "function_word_decisions": len(functions),
            "terminology_decisions": len(terms),
            "distinct_target_terms": len({row["target_term"] for row in terms}),
            "linked_terminology_rows": linked,
            "explicitly_unlinked_terminology_rows": len(terms) - linked,
            "effective_wordweb_identifier_references": sum(len([item for item in str(row["effective_wordweb_link"]).split(";") if item]) for row in terms),
            "T008_explicit_gap_sentinels_recorded_not_linked": gap_count,
            "source_keyed_tranches": len(production),
            "rendered_pages": sum(int(row["pages"]) for row in production),
            "human_observations": 0,
            "native_validations": 0,
            "form_promotions": 0,
        },
        "predecessor_evidence": {
            "v2_profile_status": old["status"],
            "v2_live_audit_status": json.loads(OLD_AUDIT.read_text(encoding="utf-8"))["status"],
            "v2_replay_log_status_note": rel(OLD_REPLAY_STATUS),
            "boundary": "The two preserved 46/46 replay logs are historical outputs of an earlier validator surface; the live v2 audit has 50 checks and neither constitutes v3 evidence.",
        },
        "link_normalization_contract": {
            "delimiter_normalization": "plus-separated and semicolon-separated tokens are parsed individually",
            "resolved_identifiers": "only identifiers present in WordWeb v10 senses or C2 extension nodes enter effective_wordweb_link",
            "none_sentinels": "none_* tokens are excluded from effective links and copied into semantic_compatibility_rationale as unresolved gaps",
            "unknown_non_sentinel_identifiers_allowed": False,
        },
        "anti_collapse": {
            "spanish_or_french_pivot_authorized": False,
            "slash_bundles_authorized_in_running_prose": False,
            "invariant_demonstrative": "iste",
            "rejected_demonstrative": "istes",
            "mesme_mesmo_relation": "sense-separated_not_allomorphs: mesme=referential_identity; mesmo=scalar_emphasis",
            "function_word_diagnostics": function_diagnostics,
            "terminology_diagnostics": term_diagnostics,
            "diagnostic_boundary": "Exact-string carrier comparisons are structural diagnostics, not intelligibility or marginal-access measurements.",
        },
        "production": production,
        "next_source_line": 21309,
        "input_hashes": {rel(path): sha(path) for path in inputs},
        "output_hashes": {rel(path): sha(path) for path in [GRAMMAR_OUT, FUNCTION_OUT, TERMS_OUT, PROFILE_OUT]},
        "empirical_claim_boundary": {
            "human_observations": 0,
            "native_validated": False,
            "intelligibility_claim": False,
            "MII_claim": False,
            "pilot_claim": False,
            "full_R823_translation_claim": False,
        },
    }
    SUMMARY_OUT.write_text(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    LOG_OUT.write_text("\n".join([
        "PASS controlled Romance language profile v3",
        f"grammar={len(grammar)} functions={len(functions)} terms={len(terms)} linked={linked} unlinked={len(terms)-linked} effective_identifier_references={summary['counts']['effective_wordweb_identifier_references']} T008_gap_sentinels={gap_count}",
        f"tranches={len(production)} pages={sum(int(row['pages']) for row in production)} next_source_line=21309",
        "human_observations=0 native_validations=0 form_promotions=0 pilot_claim=false",
        f"grammar_sha256={sha(GRAMMAR_OUT)}",
        f"functions_sha256={sha(FUNCTION_OUT)}",
        f"terms_sha256={sha(TERMS_OUT)}",
        f"profile_sha256={sha(PROFILE_OUT)}",
        f"summary_sha256={sha(SUMMARY_OUT)}",
    ]) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
