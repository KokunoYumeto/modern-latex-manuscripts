#!/usr/bin/env python3
"""Independent, deterministic, no-write validator for the v2 morphology binding."""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import io
import json
import sys
from pathlib import Path
from typing import Any

try:
    import jsonschema
except ModuleNotFoundError as exc:  # pragma: no cover - explicit environment failure
    raise SystemExit("jsonschema is required; run with the repository Python 3.13 environment") from exc


ROOT = Path(__file__).resolve().parent
PACKAGE_PATH = ROOT / "ISV_MI_MORPHOLOGY_BINDING_V2.json"
SCHEMA_PATH = ROOT / "ISV_MI_MORPHOLOGY_BINDING_V2.schema.json"
CSV_PATH = ROOT / "ISV_MI_MORPHOLOGY_BINDING_V2.csv"
FIXTURES_PATH = ROOT / "ISV_MI_MORPHOLOGY_BINDING_V2.hostile_fixtures.json"
RECEIPT_PATH = ROOT / "ISV_MI_MORPHOLOGY_BINDING_V2.validation.json"


class DuplicateKeyError(ValueError):
    pass


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_unique_object)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256_text(text: str) -> str:
    return sha256_bytes(text.encode("utf-8"))


def file_identity(path: Path) -> dict[str, Any]:
    data = path.read_bytes()
    return {"path": path.name, "bytes": len(data), "sha256": sha256_bytes(data)}


EXPECTED_SOURCES: dict[str, tuple[str, int, str]] = {
    "SRC-PARENT-BINDING": (
        "C:/Users/user/Documents/interlanguage/03_projects/language_management/slavic_interslavic/00_lane_control/marginal_intelligibility_20260811/item_binding/ISV_MI_ITEM_BINDING.json",
        145339,
        "8A9E733E7269ECB0DBAAC4FD7BBB5D9F7642AD11EB777D7F130773C39A8D37B7",
    ),
    "SRC-DE-POINTER": (
        "C:/Users/user/Documents/interlanguage/03_projects/noether/07_german_canon_control/CURRENT_GERMAN_AUTHORITY_POINTER.json",
        132270,
        "0053EA0B7E44DDE7EA7DC285ABC115DFC43F4A74B34C54DE8F39DE4E445D5BEA",
    ),
    "SRC-DE-BODY": (
        "C:/Users/user/Documents/interlanguage/03_projects/noether/07_german_canon_control/candidates/ED0011/noether.tex",
        2153594,
        "9E6BF2BC3155ECE3DF98CD8A408C23662BEFB047A1DDF200CA1DC8476A488BF3",
    ),
    "SRC-V018-ASSEMBLY": (
        "C:/Users/user/Documents/interlanguage/03_projects/language_management/slavic_interslavic/noether_slavic_v018/release/evidence/source_assembly.json",
        110244,
        "3714EF5767CCBDC5D95DAC45ED0EFFAF8A886CC2B9D2AC19FA62D2CA7BF4232D",
    ),
    "SRC-V018-RU": (
        "C:/Users/user/Documents/interlanguage/03_projects/language_management/slavic_interslavic/noether_slavic_v018/release/source/base-papers1-43-ru.tex",
        2861855,
        "48B2B46DE1735CEC55E0C176294D3C1CF07F9FAF28BE6698BADF62A74779CE45",
    ),
    "SRC-V018-UK": (
        "C:/Users/user/Documents/interlanguage/03_projects/language_management/slavic_interslavic/noether_slavic_v018/release/source/base-papers1-43-uk.tex",
        2690965,
        "61414A4D8A56B2574A234D60D3DBC663B4646D47757B2806746C184D17D7E2D8",
    ),
    "SRC-V018-ISV": (
        "C:/Users/user/Documents/interlanguage/03_projects/language_management/slavic_interslavic/noether_slavic_v018/release/source/base-papers1-43-isv.tex",
        1883717,
        "23629202D0F65BE1AD4A7E66E1A726693B7AC07DE56D183C288D80182B6DCC1A",
    ),
    "SRC-AUTHORITY-MANIFEST": (
        "C:/Users/user/Documents/interlanguage/03_projects/language_management/slavic_interslavic/00_lane_control/marginal_intelligibility_20260811/authority_snapshots/AUTHORITY_SNAPSHOT_MANIFEST.json",
        107058,
        "CFF235A721386FB74CB5970C5F7114655EA791E5CC48777CCCC4CD3F83130B9A",
    ),
    "SRC-GRAMMAR-ADJECTIVES": (
        "C:/Users/user/Documents/interlanguage/03_projects/language_management/slavic_interslavic/00_lane_control/marginal_intelligibility_20260811/authority_snapshots/snapshots/official_site/docs/learn/grammar/adjectives.md",
        8142,
        "184348005ACB532868DAEB35DBFB7A8E05A493D550B4D6FA2E1A3BCFC906D84F",
    ),
    "SRC-GRAMMAR-CONJUNCTIONS": (
        "C:/Users/user/Documents/interlanguage/03_projects/language_management/slavic_interslavic/00_lane_control/marginal_intelligibility_20260811/authority_snapshots/snapshots/official_site/docs/learn/grammar/conjunctions.md",
        2435,
        "3E986444A77D27A01586B15BFDDE96937E0A265AAEDE09E3A313BE403489B2AB",
    ),
    "SRC-GRAMMAR-NOUNS": (
        "C:/Users/user/Documents/interlanguage/03_projects/language_management/slavic_interslavic/00_lane_control/marginal_intelligibility_20260811/authority_snapshots/snapshots/official_site/docs/learn/grammar/nouns.md",
        12310,
        "BCE65A602F5DAFFF86BD132C6CBD0F5F1A4D5BDE9750A0394F78E5D4A8E9F09E",
    ),
    "SRC-GRAMMAR-PREPOSITIONS": (
        "C:/Users/user/Documents/interlanguage/03_projects/language_management/slavic_interslavic/00_lane_control/marginal_intelligibility_20260811/authority_snapshots/snapshots/official_site/docs/learn/grammar/prepositions.md",
        6363,
        "56D7FFAF2D99CB63F889606E237AE0534A4924B37D72974C8BB2C6D2CA0E4EF0",
    ),
    "SRC-GRAMMAR-PRONOUNS": (
        "C:/Users/user/Documents/interlanguage/03_projects/language_management/slavic_interslavic/00_lane_control/marginal_intelligibility_20260811/authority_snapshots/snapshots/official_site/docs/learn/grammar/pronouns.md",
        10370,
        "AB4F7B04FD55618DE2EB5FEB282558BEDEC6C205BEBB0E6BBD612CB3FBC88141",
    ),
    "SRC-GRAMMAR-SYNTAX": (
        "C:/Users/user/Documents/interlanguage/03_projects/language_management/slavic_interslavic/00_lane_control/marginal_intelligibility_20260811/authority_snapshots/snapshots/official_site/docs/learn/grammar/syntax.md",
        3816,
        "6ECF3059BA1CC64C3EDE2B80099B93CF3CC079C69B186F5879CC017212B1159B",
    ),
    "SRC-GRAMMAR-VERBS": (
        "C:/Users/user/Documents/interlanguage/03_projects/language_management/slavic_interslavic/00_lane_control/marginal_intelligibility_20260811/authority_snapshots/snapshots/official_site/docs/learn/grammar/verbs.md",
        21426,
        "3684BE0634F0163DDD4BEC09719280C3C0E1E2367009AA3DAE584C50DD6249AD",
    ),
}


EXPECTED_GRAMMAR: dict[str, tuple[str, int]] = {
    "GRAM-ADJ-AGREEMENT": ("SRC-GRAMMAR-ADJECTIVES", 14),
    "GRAM-GENITIVE-POSSESSION": ("SRC-GRAMMAR-ADJECTIVES", 45),
    "GRAM-NOUN-CASES": ("SRC-GRAMMAR-NOUNS", 12),
    "GRAM-VERB-INFINITIVE": ("SRC-GRAMMAR-VERBS", 62),
    "GRAM-SYNTAX-WORD-ORDER": ("SRC-GRAMMAR-SYNTAX", 12),
    "GRAM-SYNTAX-MODIFIER-ORDER": ("SRC-GRAMMAR-SYNTAX", 14),
    "GRAM-CONJ-CLAUSES": ("SRC-GRAMMAR-CONJUNCTIONS", 12),
    "GRAM-ZE-THAT": ("SRC-GRAMMAR-CONJUNCTIONS", 66),
    "GRAM-POD-INSTRUMENTAL": ("SRC-GRAMMAR-PREPOSITIONS", 89),
    "GRAM-POD-LEXEME": ("SRC-GRAMMAR-PREPOSITIONS", 95),
    "GRAM-RELATIVE-KTORY": ("SRC-GRAMMAR-PRONOUNS", 84),
}


EXPECTED_LOCI: dict[str, dict[str, Any]] = {
    "MI-MORPH-GAP-01": {
        "paper_id": "P09",
        "role": "candidate_direct_morphology_nominal_agreement_and_compound_order",
        "contrast": "direct_morphology",
        "parent_line": 8349,
        "parent_surface": "kvocientno polje",
        "grammar": {"GRAM-ADJ-AGREEMENT", "GRAM-SYNTAX-MODIFIER-ORDER"},
        "surfaces": {
            "de": ("SRC-DE-BODY", 7643, 7648, "Quotientenkörper"),
            "ru": ("SRC-V018-RU", 8380, 8384, "поле частных"),
            "uk": ("SRC-V018-UK", 8341, 8345, "поле часток"),
            "isv": ("SRC-V018-ISV", 8347, 8351, "kvocientno polje"),
        },
    },
    "MI-MORPH-GAP-02": {
        "paper_id": "P02",
        "role": "candidate_direct_morphosyntax_predicate_modality_and_periphrasis",
        "contrast": "direct_morphosyntax",
        "parent_line": 1041,
        "parent_surface": "ima važiti",
        "grammar": {"GRAM-VERB-INFINITIVE", "GRAM-SYNTAX-WORD-ORDER"},
        "surfaces": {
            "de": ("SRC-DE-BODY", 1323, 1327, "soll der Modul"),
            "ru": ("SRC-V018-RU", 1036, 1042, "считается более высоким"),
            "uk": ("SRC-V018-UK", 1036, 1042, "вважатимемо вищим"),
            "isv": ("SRC-V018-ISV", 1035, 1041, "ima važiti"),
        },
    },
    "MI-MORPH-GAP-03": {
        "paper_id": "P19",
        "role": "candidate_direct_morphology_and_morphosyntax_genitive_chain_agreement",
        "contrast": "direct_morphology_and_morphosyntax",
        "parent_line": 12451,
        "parent_surface": "elementov kolca",
        "grammar": {"GRAM-NOUN-CASES", "GRAM-GENITIVE-POSSESSION", "GRAM-ADJ-AGREEMENT"},
        "surfaces": {
            "de": ("SRC-DE-BODY", 11319, 11319, "aus je zwei Ringelementen"),
            "ru": ("SRC-V018-RU", 12484, 12484, "из каждых двух элементов кольца"),
            "uk": ("SRC-V018-UK", 12445, 12445, "з кожних двох елементів кільця"),
            "isv": ("SRC-V018-ISV", 12451, 12451, "iz každih dvoh elementov kolca"),
        },
    },
    "MI-MORPH-GAP-04": {
        "paper_id": "P01",
        "role": "candidate_direct_morphosyntax_inferential_linkage_complementizer_order",
        "contrast": "direct_morphosyntax",
        "parent_line": 63,
        "parent_surface": "slěduje, že",
        "grammar": {"GRAM-CONJ-CLAUSES", "GRAM-ZE-THAT", "GRAM-SYNTAX-WORD-ORDER"},
        "surfaces": {
            "de": ("SRC-DE-BODY", 403, 403, "muß dies Verfahren notwendig"),
            "ru": ("SRC-V018-RU", 63, 63, "Благодаря общей теореме Гильберта"),
            "uk": ("SRC-V018-UK", 63, 63, "Завдяки загальній теоремі Гільберта"),
            "isv": ("SRC-V018-ISV", 63, 63, "slěduje, že"),
        },
    },
    "MI-MORPH-GAP-05": {
        "paper_id": "P01",
        "role": "candidate_direct_morphosyntax_case_government_relative_clause_integration",
        "contrast": "direct_morphosyntax",
        "parent_line": 100,
        "parent_surface": 'Pod "rędom form"',
        "grammar": {"GRAM-POD-INSTRUMENTAL", "GRAM-POD-LEXEME", "GRAM-RELATIVE-KTORY", "GRAM-NOUN-CASES"},
        "surfaces": {
            "de": ("SRC-DE-BODY", 440, 440, "Als \\glqq{}Formenreihe"),
            "ru": ("SRC-V018-RU", 100, 104, 'Под "рядом форм"'),
            "uk": ("SRC-V018-UK", 100, 104, 'Під "рядом форм"'),
            "isv": ("SRC-V018-ISV", 100, 104, 'Pod "rędom form"'),
        },
    },
}


def source_map(package: dict[str, Any]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for source in package.get("source_pins", []):
        source_id = source.get("source_id")
        if source_id in result:
            continue
        result[source_id] = source
    return result


def lines_for(source: dict[str, Any], cache: dict[str, list[str]]) -> list[str]:
    source_id = source["source_id"]
    if source_id not in cache:
        cache[source_id] = Path(source["absolute_path"]).read_text(encoding="utf-8").splitlines()
    return cache[source_id]


def validate_schema(instance: dict[str, Any], schema: dict[str, Any]) -> list[str]:
    errors = sorted(jsonschema.Draft202012Validator(schema).iter_errors(instance), key=lambda e: list(e.path))
    return ["SCHEMA_VALIDATION_FAILURE"] if errors else []


def validate_semantics(
    package: dict[str, Any],
    *,
    verify_files: bool,
    schema: dict[str, Any] | None = None,
    check_csv: bool = False,
) -> list[str]:
    errors: set[str] = set()
    if schema is not None:
        errors.update(validate_schema(package, schema))

    claims = package.get("claims", {})
    if any(claims.get(key) is not False for key in (
        "participant_ready",
        "intelligibility_measured",
        "branch_complete",
        "native_approved",
        "direct_morphology_contrast_established",
        "community_approval",
        "canonical_claim",
    )):
        errors.add("FABRICATED_CLAIM")

    sources = source_map(package)
    if set(sources) != set(EXPECTED_SOURCES) or len(package.get("source_pins", [])) != len(EXPECTED_SOURCES):
        errors.add("SOURCE_REGISTRY_MISMATCH")
    line_cache: dict[str, list[str]] = {}
    for source_id, (expected_path, expected_bytes, expected_hash) in EXPECTED_SOURCES.items():
        source = sources.get(source_id)
        if not source:
            continue
        if (source.get("absolute_path"), source.get("bytes"), source.get("sha256")) != (
            expected_path,
            expected_bytes,
            expected_hash,
        ):
            errors.add("SOURCE_REGISTRY_MISMATCH")
        if verify_files:
            path = Path(source["absolute_path"])
            if not path.is_file():
                errors.add("SOURCE_FILE_MISSING")
                continue
            data = path.read_bytes()
            if len(data) != source["bytes"] or sha256_bytes(data) != source["sha256"]:
                errors.add("SOURCE_HASH_MISMATCH")

    rules = {rule.get("rule_id"): rule for rule in package.get("grammar_rules", [])}
    if set(rules) != set(EXPECTED_GRAMMAR) or len(package.get("grammar_rules", [])) != len(EXPECTED_GRAMMAR):
        errors.add("GRAMMAR_REGISTRY_MISMATCH")
    for rule_id, (expected_source, expected_line) in EXPECTED_GRAMMAR.items():
        rule = rules.get(rule_id)
        if not rule:
            continue
        if (rule.get("source_id"), rule.get("line")) != (expected_source, expected_line):
            errors.add("GRAMMAR_REGISTRY_MISMATCH")
        if verify_files and expected_source in sources:
            file_lines = lines_for(sources[expected_source], line_cache)
            if not 1 <= expected_line <= len(file_lines):
                errors.add("GRAMMAR_LOCATOR_MISMATCH")
            else:
                actual = file_lines[expected_line - 1]
                if actual != rule.get("text") or sha256_text(actual) != rule.get("sha256_utf8"):
                    errors.add("GRAMMAR_LOCATOR_MISMATCH")

    loci = package.get("loci", [])
    locus_ids = [locus.get("locus_id") for locus in loci]
    if locus_ids != list(EXPECTED_LOCI):
        errors.add("LOCUS_REGISTRY_MISMATCH")
    for locus in loci:
        locus_id = locus.get("locus_id")
        expected = EXPECTED_LOCI.get(locus_id)
        if expected is None:
            errors.add("LOCUS_REGISTRY_MISMATCH")
            continue
        if (locus.get("paper_id"), locus.get("locus_role")) != (expected["paper_id"], expected["role"]):
            errors.add("LEXICAL_ONLY_RELABEL")
        contrast = locus.get("contrast_requirement", {}).get("contrast_class")
        if contrast != expected["contrast"] or contrast == "lexical_only":
            errors.add("LEXICAL_ONLY_RELABEL")
        prohibited = set(locus.get("contrast_requirement", {}).get("prohibited", []))
        if "lexical_only_relabel" not in prohibited or "model_filled_branch_surface" not in prohibited:
            errors.add("LEXICAL_ONLY_RELABEL")
        if set(locus.get("grammar_rule_ids", [])) != expected["grammar"]:
            errors.add("GRAMMAR_REGISTRY_MISMATCH")

        coverage = locus.get("coverage", {})
        if coverage.get("west") != "missing_zero_surfaces" or coverage.get("south") != "missing_zero_surfaces":
            errors.add("FABRICATED_BRANCH_COVERAGE")
        if coverage.get("east") != "ru_and_uk_exact_spans_east_only_not_independent_branch_breadth":
            errors.add("FABRICATED_BRANCH_COVERAGE")
        if coverage.get("official_grammar") != "partial_constraint_only_not_branch_or_intelligibility_evidence":
            errors.add("FABRICATED_BRANCH_COVERAGE")

        review = locus.get("review_state", {})
        if (
            review.get("native_authorship_records") != 0
            or review.get("native_review_records") != 0
            or review.get("native_review_status") != "missing"
            or review.get("participant_response_records") != 0
        ):
            errors.add("FAKE_NATIVE_APPROVAL")
        if locus.get("experimental_item_state") != "held_missing_west_south_branch_coherent_surfaces_and_qualified_native_review":
            errors.add("FABRICATED_CLAIM")

        parent = locus.get("parent_pin", {})
        if parent.get("isv_target_line") != expected["parent_line"] or parent.get("controlled_occurrence_surface") != expected["parent_surface"]:
            errors.add("PARENT_LOCUS_MISMATCH")

        surfaces = locus.get("surfaces", {})
        if set(surfaces) != {"de", "ru", "uk", "isv"}:
            errors.add("FABRICATED_BRANCH_COVERAGE")
        for lang, expected_surface in expected["surfaces"].items():
            surface = surfaces.get(lang)
            if not surface:
                errors.add("SWAPPED_OR_MISBOUND_LOCATOR")
                continue
            expected_source, expected_start, expected_end, expected_token = expected_surface
            context = surface.get("context", {})
            if (
                surface.get("source_id"),
                surface.get("language"),
                context.get("line_start"),
                context.get("line_end"),
                surface.get("controlled_occurrence"),
            ) != (expected_source, lang, expected_start, expected_end, expected_token):
                errors.add("SWAPPED_OR_MISBOUND_LOCATOR")
            if lang in {"ru", "uk"}:
                if surface.get("branch_scope") != "east_slavic_only" or surface.get("evidence_role") != "east_only_comparator_not_native_validated":
                    errors.add("FABRICATED_BRANCH_COVERAGE")
            elif lang == "de":
                if surface.get("branch_scope") != "meaning_authority" or surface.get("evidence_role") != "german_meaning_authority":
                    errors.add("SWAPPED_OR_MISBOUND_LOCATOR")
            elif lang == "isv":
                if surface.get("branch_scope") != "constructed_interslavic_baseline" or surface.get("evidence_role") != "current_editable_latin_baseline_not_official_grammar":
                    errors.add("FABRICATED_BRANCH_COVERAGE")
            if verify_files and surface.get("source_id") in sources:
                file_lines = lines_for(sources[surface["source_id"]], line_cache)
                start, end = context.get("line_start"), context.get("line_end")
                if not isinstance(start, int) or not isinstance(end, int) or start < 1 or end < start or end > len(file_lines):
                    errors.add("SWAPPED_OR_MISBOUND_LOCATOR")
                    continue
                actual_context = "\n".join(file_lines[start - 1 : end])
                if sha256_text(actual_context) != context.get("sha256_utf8_lf"):
                    errors.add("HASH_MUTATION")
                if surface.get("controlled_occurrence") not in actual_context:
                    errors.add("SWAPPED_OR_MISBOUND_LOCATOR")
                focus_kind = context.get("focus_kind")
                if focus_kind == "whole_context":
                    if context.get("focus_sha256_utf8") != sha256_text(actual_context):
                        errors.add("HASH_MUTATION")
                elif focus_kind == "exact_substring":
                    focus = context.get("focus_text", "")
                    if focus not in actual_context or sha256_text(focus) != context.get("focus_sha256_utf8"):
                        errors.add("HASH_MUTATION")
                else:
                    errors.add("HASH_MUTATION")
                anchor = surface.get("structural_anchor", {})
                anchor_line = anchor.get("line")
                if not isinstance(anchor_line, int) or not 1 <= anchor_line <= len(file_lines):
                    errors.add("SWAPPED_OR_MISBOUND_LOCATOR")
                else:
                    actual_anchor = file_lines[anchor_line - 1]
                    if actual_anchor != anchor.get("text") or sha256_text(actual_anchor) != anchor.get("sha256_utf8"):
                        errors.add("SWAPPED_OR_MISBOUND_LOCATOR")

    if verify_files:
        validate_authority_links(package, sources, errors)
        validate_parent_loci(package, sources, errors)
    if check_csv:
        validate_csv_projection(package, errors)
    return sorted(errors)


def validate_authority_links(
    package: dict[str, Any], sources: dict[str, dict[str, Any]], errors: set[str]
) -> None:
    pointer = load_json(Path(sources["SRC-DE-POINTER"]["absolute_path"]))
    authority = pointer.get("default_translation_authority", {})
    if (
        pointer.get("pointer_id") != "NOETH-DE-AUTH-v047-20260808"
        or authority.get("authority_id") != "NOETH-DE-ED-0011"
        or authority.get("path") != sources["SRC-DE-BODY"]["absolute_path"]
        or authority.get("raw_bytes") != sources["SRC-DE-BODY"]["bytes"]
        or authority.get("raw_sha256") != sources["SRC-DE-BODY"]["sha256"]
    ):
        errors.add("GERMAN_POINTER_BODY_MISMATCH")

    assembly = load_json(Path(sources["SRC-V018-ASSEMBLY"]["absolute_path"]))
    assembly_authority = assembly.get("authority", {})
    if (
        assembly_authority.get("pointer_id") != pointer.get("pointer_id")
        or assembly_authority.get("pointer_sha256") != sources["SRC-DE-POINTER"]["sha256"]
        or assembly_authority.get("authority_id") != authority.get("authority_id")
        or assembly_authority.get("authority_sha256") != authority.get("raw_sha256")
    ):
        errors.add("V018_ASSEMBLY_AUTHORITY_MISMATCH")
    for target, source_id in (("ru", "SRC-V018-RU"), ("uk", "SRC-V018-UK"), ("isv", "SRC-V018-ISV")):
        rows = [row for row in assembly.get("numbered_paper_base_lineage", []) if row.get("target") == target]
        if len(rows) != 1:
            errors.add("V018_ASSEMBLY_AUTHORITY_MISMATCH")
            continue
        row = rows[0]
        if (
            row.get("release_path") != sources[source_id]["absolute_path"]
            or row.get("release_sha256") != sources[source_id]["sha256"]
            or row.get("copy_identity") is not True
        ):
            errors.add("V018_ASSEMBLY_AUTHORITY_MISMATCH")

    manifest = load_json(Path(sources["SRC-AUTHORITY-MANIFEST"]["absolute_path"]))
    context = package.get("authority_context", {})
    grammar_authorities = [a for a in manifest.get("authorities", []) if a.get("authority_id") == "ISV-AUTH-004"]
    collections = [c for c in manifest.get("collections", []) if c.get("collection_id") == "ISV-AUTH-COLLECTION-002"]
    repo_pins = [r for r in manifest.get("repository_pins", []) if r.get("commit_sha1") == context.get("official_site_commit_sha1")]
    if (
        manifest.get("snapshot_id") != context.get("official_snapshot_id")
        or manifest.get("supersession", {}).get("review_state") != context.get("snapshot_review_state")
        or len(grammar_authorities) != 1
        or grammar_authorities[0].get("state") != "commit_pinned_exact_bytes"
        or len(collections) != 1
        or collections[0].get("bytes") != context.get("grammar_collection_bytes")
        or collections[0].get("sha256") != context.get("grammar_collection_sha256")
        or len(repo_pins) != 1
        or repo_pins[0].get("tree_sha1") != context.get("official_site_tree_sha1")
    ):
        errors.add("OFFICIAL_GRAMMAR_AUTHORITY_MISMATCH")


def validate_parent_loci(
    package: dict[str, Any], sources: dict[str, dict[str, Any]], errors: set[str]
) -> None:
    parent = load_json(Path(sources["SRC-PARENT-BINDING"]["absolute_path"]))
    old_loci = parent.get("morphology_scope_audit", {}).get("extension_loci", [])
    old_by_id = {row.get("locus_id"): row for row in old_loci}
    if len(old_loci) != 5 or set(old_by_id) != set(EXPECTED_LOCI):
        errors.add("PARENT_LOCUS_MISMATCH")
        return
    for locus in package.get("loci", []):
        old = old_by_id.get(locus.get("locus_id"), {})
        pin = locus.get("parent_pin", {})
        locator = old.get("locator", {})
        target = locator.get("target_locator", {})
        german = locator.get("german_authority_locator", {})
        if (
            old.get("phenomenon") != pin.get("phenomenon")
            or locator.get("controlled_occurrence_surface") != pin.get("controlled_occurrence_surface")
            or target.get("line") != pin.get("isv_target_line")
            or target.get("line_sha256_utf8") != pin.get("isv_target_line_sha256_utf8")
            or target.get("producer_declaration_line") != pin.get("producer_declaration_line")
            or target.get("producer_source_path") != pin.get("producer_source_path")
            or target.get("producer_source_sha256") != pin.get("producer_source_sha256")
            or german.get("line_start") != pin.get("german_paper_range", {}).get("line_start")
            or german.get("line_end") != pin.get("german_paper_range", {}).get("line_end")
            or german.get("range_sha256_utf8_lf") != pin.get("german_paper_range", {}).get("sha256_utf8_lf_with_final_lf")
        ):
            errors.add("PARENT_LOCUS_MISMATCH")


CSV_FIELDS = [
    "locus_id",
    "paper_id",
    "locus_role",
    "de_locator",
    "ru_locator",
    "uk_locator",
    "isv_locator",
    "alignment_state",
    "experimental_item_state",
    "east_scope",
    "west_status",
    "south_status",
    "native_review_records",
    "grammar_state",
]


def csv_rows(package: dict[str, Any]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for locus in package["loci"]:
        surfaces = locus["surfaces"]
        row: dict[str, str] = {
            "locus_id": locus["locus_id"],
            "paper_id": locus["paper_id"],
            "locus_role": locus["locus_role"],
            "alignment_state": locus["alignment_state"],
            "experimental_item_state": locus["experimental_item_state"],
            "east_scope": locus["coverage"]["east"],
            "west_status": locus["coverage"]["west"],
            "south_status": locus["coverage"]["south"],
            "native_review_records": str(locus["review_state"]["native_review_records"]),
            "grammar_state": locus["coverage"]["official_grammar"],
        }
        for lang in ("de", "ru", "uk", "isv"):
            surface = surfaces[lang]
            context = surface["context"]
            row[f"{lang}_locator"] = f"{surface['source_id']}:{context['line_start']}-{context['line_end']}"
        rows.append(row)
    return rows


def validate_csv_projection(package: dict[str, Any], errors: set[str]) -> None:
    with CSV_PATH.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        actual_fields = reader.fieldnames
        actual_rows = list(reader)
    if actual_fields != CSV_FIELDS or actual_rows != csv_rows(package):
        errors.add("CSV_PROJECTION_MISMATCH")


def resolve_path(root: Any, dotted: str) -> tuple[Any, str | int]:
    parts = dotted.split(".")
    current = root
    for part in parts[:-1]:
        current = current[int(part)] if isinstance(current, list) else current[part]
    final: str | int = int(parts[-1]) if isinstance(current, list) else parts[-1]
    return current, final


def mutate(instance: dict[str, Any], mutations: list[dict[str, Any]]) -> None:
    for mutation in mutations:
        op = mutation.get("op")
        if op == "replace":
            parent, key = resolve_path(instance, mutation["path"])
            parent[key] = mutation["value"]
        elif op == "swap":
            left_parent, left_key = resolve_path(instance, mutation["paths"][0])
            right_parent, right_key = resolve_path(instance, mutation["paths"][1])
            left_parent[left_key], right_parent[right_key] = right_parent[right_key], left_parent[left_key]
        else:
            raise ValueError(f"unsupported fixture mutation: {op}")


def validate_fixture_manifest(fixtures: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    expected_ids = [
        "swapped_locators",
        "fabricated_branch_coverage",
        "lexical_only_relabeling_as_morphology",
        "context_hash_mutation",
        "fake_native_approval",
    ]
    if fixtures.get("schema_id") != "ISV-MI-MORPHOLOGY-BINDING-V2-HOSTILE-FIXTURES-v1":
        errors.append("FIXTURE_MANIFEST_MISMATCH")
    if [f.get("fixture_id") for f in fixtures.get("fixtures", [])] != expected_ids:
        errors.append("FIXTURE_MANIFEST_MISMATCH")
    for fixture in fixtures.get("fixtures", []):
        if set(fixture) != {"fixture_id", "mutations", "expected_error"}:
            errors.append("FIXTURE_MANIFEST_MISMATCH")
    return sorted(set(errors))


def run_fixtures(
    package: dict[str, Any], schema: dict[str, Any], fixtures: dict[str, Any]
) -> tuple[list[dict[str, Any]], list[str]]:
    results: list[dict[str, Any]] = []
    errors = validate_fixture_manifest(fixtures)
    for fixture in fixtures.get("fixtures", []):
        candidate = copy.deepcopy(package)
        mutate(candidate, fixture["mutations"])
        observed = validate_semantics(candidate, verify_files=True, schema=schema, check_csv=False)
        expected_error = fixture["expected_error"]
        rejected = expected_error in observed
        if not rejected:
            errors.append("HOSTILE_FIXTURE_NOT_REJECTED")
        results.append(
            {
                "fixture_id": fixture["fixture_id"],
                "expected_error": expected_error,
                "observed_errors": observed,
                "rejected": rejected,
            }
        )
    return results, sorted(set(errors))


def deterministic_receipt(
    package: dict[str, Any], base_errors: list[str], fixture_results: list[dict[str, Any]], fixture_errors: list[str]
) -> dict[str, Any]:
    all_errors = sorted(set(base_errors + fixture_errors))
    return {
        "schema_id": "ISV-MI-MORPHOLOGY-BINDING-V2-VALIDATION-v1",
        "package_id": package.get("package_id"),
        "status": "PASS" if not all_errors else "FAIL",
        "validator_mode": "independent_no_write_deterministic",
        "inputs": [
            file_identity(PACKAGE_PATH),
            file_identity(SCHEMA_PATH),
            file_identity(CSV_PATH),
            file_identity(FIXTURES_PATH),
            file_identity(Path(__file__).resolve()),
        ],
        "checks": {
            "draft_2020_12_schema": "PASS" if "SCHEMA_VALIDATION_FAILURE" not in base_errors else "FAIL",
            "source_pins_verified": len(EXPECTED_SOURCES),
            "official_grammar_rules_verified": len(EXPECTED_GRAMMAR),
            "loci_verified": len(EXPECTED_LOCI),
            "surface_bindings_verified": len(EXPECTED_LOCI) * 4,
            "german_meaning_authority_spans": len(EXPECTED_LOCI),
            "east_only_ru_uk_spans": len(EXPECTED_LOCI) * 2,
            "west_surfaces": 0,
            "south_surfaces": 0,
            "native_authorship_records": 0,
            "native_review_records": 0,
            "participant_response_records": 0,
            "direct_morphology_contrasts_established": 0,
            "csv_projection": "PASS" if "CSV_PROJECTION_MISMATCH" not in base_errors else "FAIL",
        },
        "base_errors": all_errors,
        "hostile_fixtures": fixture_results,
        "claims": package.get("claims"),
        "next_cursor": package.get("next_cursor"),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true", help="run all hostile fixtures")
    parser.add_argument("--check-receipt", action="store_true", help="require byte-equivalent stored deterministic receipt")
    parser.add_argument("--emit-receipt", action="store_true", help="print the deterministic receipt JSON")
    parser.add_argument("--compact", action="store_true", help="print one concise status line")
    args = parser.parse_args()

    try:
        package = load_json(PACKAGE_PATH)
        schema = load_json(SCHEMA_PATH)
        fixtures = load_json(FIXTURES_PATH)
        jsonschema.Draft202012Validator.check_schema(schema)
    except (OSError, json.JSONDecodeError, DuplicateKeyError, jsonschema.SchemaError) as exc:
        print(f"FAIL LOAD_OR_SCHEMA_ERROR {exc}", file=sys.stderr)
        return 1

    base_errors = validate_semantics(package, verify_files=True, schema=schema, check_csv=True)
    fixture_results: list[dict[str, Any]] = []
    fixture_errors: list[str] = []
    if args.self_test:
        fixture_results, fixture_errors = run_fixtures(package, schema, fixtures)
    receipt = deterministic_receipt(package, base_errors, fixture_results, fixture_errors)

    if args.check_receipt:
        try:
            stored = load_json(RECEIPT_PATH)
        except (OSError, json.JSONDecodeError, DuplicateKeyError) as exc:
            receipt["status"] = "FAIL"
            receipt["base_errors"] = sorted(set(receipt["base_errors"] + ["RECEIPT_MISSING_OR_INVALID"]))
            if args.compact:
                print(f"FAIL receipt {exc}")
            else:
                print(json.dumps(receipt, ensure_ascii=False, indent=2))
            return 1
        if stored != receipt:
            receipt["status"] = "FAIL"
            receipt["base_errors"] = sorted(set(receipt["base_errors"] + ["RECEIPT_MISMATCH"]))

    if args.emit_receipt:
        print(json.dumps(receipt, ensure_ascii=False, indent=2))
    elif args.compact:
        checks = receipt["checks"]
        print(
            f"{receipt['status']} loci={checks['loci_verified']} surfaces={checks['surface_bindings_verified']} "
            f"west={checks['west_surfaces']} south={checks['south_surfaces']} native_reviews={checks['native_review_records']} "
            f"fixtures={sum(1 for f in fixture_results if f['rejected'])}/{len(fixture_results)}"
        )
        if receipt["base_errors"]:
            print("ERRORS " + " ".join(receipt["base_errors"]))
    else:
        print(json.dumps(receipt, ensure_ascii=False, indent=2))
    return 0 if receipt["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
