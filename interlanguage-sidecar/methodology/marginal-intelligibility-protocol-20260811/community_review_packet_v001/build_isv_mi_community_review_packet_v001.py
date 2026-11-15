#!/usr/bin/env python3
"""Build the bounded, non-approved v001 community review solicitation packet."""

from __future__ import annotations

import csv
import hashlib
import io
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
PACKAGE = ROOT / "ISV_MI_COMMUNITY_REVIEW_PACKET_v001.json"
SCHEMA = ROOT / "ISV_MI_COMMUNITY_REVIEW_PACKET_v001.schema.json"
CSV_PATH = ROOT / "ISV_MI_COMMUNITY_REVIEW_PACKET_v001.csv"
REVIEWER_MD = ROOT / "ISV_MI_COMMUNITY_REVIEW_PACKET_v001_REVIEWER.md"
FIXTURES = ROOT / "ISV_MI_COMMUNITY_REVIEW_PACKET_v001.hostile_fixtures.json"
MANIFEST = ROOT / "ISV_MI_COMMUNITY_REVIEW_PACKET_v001.manifest.json"
VALIDATOR = ROOT / "validate_isv_mi_community_review_packet_v001.py"
RECEIPT = ROOT / "ISV_MI_COMMUNITY_REVIEW_PACKET_v001.validation.json"

INPUTS: dict[str, tuple[str, int, str]] = {
    "IN-MORPH-PACKAGE": ("C:/Users/user/Documents/interlanguage/03_projects/language_management/slavic_interslavic/00_lane_control/marginal_intelligibility_20260811/morphology_extension_v2/ISV_MI_MORPHOLOGY_BINDING_V2.json", 52159, "86A19C7AD035038A198739AF7BC507ED630BD91D09AACB3173D55E641A7BA1DD"),
    "IN-MORPH-SCHEMA": ("C:/Users/user/Documents/interlanguage/03_projects/language_management/slavic_interslavic/00_lane_control/marginal_intelligibility_20260811/morphology_extension_v2/ISV_MI_MORPHOLOGY_BINDING_V2.schema.json", 13204, "B98CE723F23C8BD8616D4D73575A040A576D2844FBA46FF81A68195AE7798777"),
    "IN-MORPH-RECEIPT": ("C:/Users/user/Documents/interlanguage/03_projects/language_management/slavic_interslavic/00_lane_control/marginal_intelligibility_20260811/morphology_extension_v2/ISV_MI_MORPHOLOGY_BINDING_V2.validation.json", 3437, "10746F698B9D7F90B323AAC41734A2FD813A081C85139E6A3093DA939BE2EAAB"),
    "IN-S39-PARENT": ("C:/Users/user/Documents/interlanguage/03_projects/language_management/slavic_interslavic/00_lane_control/spark_20260811/batch_002/s39_morph_alignment_adversary/parent_review/S39_MORPH_ALIGNMENT_PARENT_REVIEW_20260811.json", 23121, "9C242E646139A0EBBEC6BF0529B898BFBD1B9E77D4B0E810BA5DD3F3C7C2AA79"),
    "IN-HOLD-QUEUE": ("C:/Users/user/Documents/interlanguage/03_projects/language_management/slavic_interslavic/00_lane_control/isv_normalization_20260811/hold_review_queue/ISV_FOREIGN_HOLD_REVIEW_QUEUE.json", 658234, "DB4B22303141B70F1A9306F3DC428F813037066E6FD767ABE9CF61B94387CB36"),
    "IN-HOLD-QUEUE-RECEIPT": ("C:/Users/user/Documents/interlanguage/03_projects/language_management/slavic_interslavic/00_lane_control/isv_normalization_20260811/hold_review_queue/ISV_FOREIGN_HOLD_REVIEW_QUEUE.validation.json", 4961, "334D1970FA376058D0DBCE0FDB3D2E8776C7D10825153504299FBEFE487ADC1F"),
    "IN-ROUTE-B-V002": ("C:/Users/user/Documents/interlanguage/03_projects/language_management/slavic_interslavic/00_lane_control/isv_normalization_20260811/hold_review_queue/route_b_editorial_policy/ISV_ROUTE_B_EDITORIAL_POLICY_DECISIONS_v002.json", 83357, "3AD9625CF31A336021CBD90AE8D3881D676D5AF2BFF0685DDD488D3EF63C3F7A"),
    "IN-ROUTE-B-SCHEMA": ("C:/Users/user/Documents/interlanguage/03_projects/language_management/slavic_interslavic/00_lane_control/isv_normalization_20260811/hold_review_queue/route_b_editorial_policy/ISV_ROUTE_B_EDITORIAL_POLICY_DECISIONS_v002.schema.json", 5741, "DEC166D556B46F6CE47BFF30B5D21C8978D8817342F961C6A81C0621B0A574F6"),
    "IN-ROUTE-B-RECEIPT": ("C:/Users/user/Documents/interlanguage/03_projects/language_management/slavic_interslavic/00_lane_control/isv_normalization_20260811/hold_review_queue/route_b_editorial_policy/ISV_ROUTE_B_EDITORIAL_POLICY_VALIDATION_v002.json", 2604, "FC0A0EBB26635E8B5A0C1F4B0A0A644A8DC4920756A56C11BB3A8BDFD085B11A"),
    "IN-SUCCESSOR-V1": ("C:/Users/user/Documents/interlanguage/03_projects/language_management/slavic_interslavic/00_lane_control/isv_normalization_20260811/successor_input_ledger/ISV_SUCCESSOR_INPUT_LEDGER_20260811.json", 2001706, "D83E601FC4F8528CD852D02F2A22E866D6F61D3B1F0E45F719DB1DA01D07A598"),
    "IN-SUCCESSOR-ADVERSARY": ("C:/Users/user/Documents/interlanguage/03_projects/language_management/slavic_interslavic/00_lane_control/isv_normalization_20260811/successor_input_ledger_adversarial_20260811/ISV_SUCCESSOR_INPUT_LEDGER_ADVERSARIAL_AUDIT_20260811.json", 41145, "02D15452C23ED0472C95B369AA3C2F5D08E3418275C03D06E33E0CC36EF7C89F"),
    "IN-DECISION-040": ("C:/Users/user/Documents/interlanguage/03_projects/language_management/slavic_interslavic/00_lane_control/decision_records/SLISV-20260811-040.json", 7207, "54B3EC0F85068D856CFFAEE47159118AA9F1664EB063799F6EA9CA613DB2F63D"),
    "IN-DECISION-041": ("C:/Users/user/Documents/interlanguage/03_projects/language_management/slavic_interslavic/00_lane_control/decision_records/SLISV-20260811-041.json", 8728, "F9F41C8AFE2B1746C56DFEDD6D1C71182724017CCAB709EC264D8E9E7696BAEE"),
    "IN-DECISION-042": ("C:/Users/user/Documents/interlanguage/03_projects/language_management/slavic_interslavic/00_lane_control/decision_records/SLISV-20260811-042.json", 9812, "913E63683E8F286BDE04E874A543FD804905E59956998226D476137652141C7C"),
    "IN-DECISION-043": ("C:/Users/user/Documents/interlanguage/03_projects/language_management/slavic_interslavic/00_lane_control/decision_records/SLISV-20260811-043.json", 6818, "910D55705AF9A29B26A7172849F895E9F82AE24FD9F2002EB8D935BF57D61CD4"),
    "IN-AUTHORITY-MANIFEST": ("C:/Users/user/Documents/interlanguage/03_projects/language_management/slavic_interslavic/00_lane_control/marginal_intelligibility_20260811/authority_snapshots/AUTHORITY_SNAPSHOT_MANIFEST.json", 107058, "CFF235A721386FB74CB5970C5F7114655EA791E5CC48777CCCC4CD3F83130B9A"),
    "IN-AUTHORITY-RECEIPT": ("C:/Users/user/Documents/interlanguage/03_projects/language_management/slavic_interslavic/00_lane_control/marginal_intelligibility_20260811/authority_snapshots/AUTHORITY_SNAPSHOT_VALIDATION.json", 4026, "1B06B8C703A72A07DC0E6834A4383B09DA6D449C46BDF6740D2F94494467131F"),
}

TARGET_LEDGER_IDS = [
    "SLISV-SUCC-IN-0001", "SLISV-SUCC-IN-0002", "SLISV-SUCC-IN-0003",
    "SLISV-SUCC-IN-0022", "SLISV-SUCC-IN-0023", "SLISV-SUCC-IN-0024",
    "SLISV-SUCC-IN-0069", "SLISV-SUCC-IN-0070", "SLISV-SUCC-IN-0071",
    "SLISV-SUCC-IN-0073", "SLISV-SUCC-IN-0074", "SLISV-SUCC-IN-0075",
    "SLISV-SUCC-IN-0078", "SLISV-SUCC-IN-0080",
]

NOETHER_COMPARATORS = {
    "SLISV-SUCC-IN-0069": ((23742, "Noetherschen", 1), (33, "Нётер", 1), (33, "Нетерової", 1)),
    "SLISV-SUCC-IN-0070": ((23750, "Noetherschen", 1), (42, "Нётер", 1), (42, "Нетерової", 1)),
    "SLISV-SUCC-IN-0071": ((23750, "Noetherschen", 2), (44, "Нётер", 1), (44, "Нетерової", 1)),
    "SLISV-SUCC-IN-0073": ((23761, "Max Noethers", 1), (76, "Макса Нётер", 1), (74, "Макса Нетер", 1)),
    "SLISV-SUCC-IN-0074": ((23767, "Noethers Satz", 1), (87, "Нётер", 1), (85, "Нетер", 1)),
    "SLISV-SUCC-IN-0075": ((23767, "M. Noethers", 1), (93, "М. Нётер", 1), (91, "М. Нетер", 1)),
    "SLISV-SUCC-IN-0078": ((24081, "Noetherschen", 1), (165, "ноэтеровой", 1), (165, "Ноетерової", 1)),
}

DE = Path("C:/Users/user/Documents/interlanguage/03_projects/noether/07_german_canon_control/candidates/ED0011/noether.tex")
BASE_RU = Path("C:/Users/user/Documents/interlanguage/03_projects/language_management/slavic_interslavic/noether_slavic_v018/release/source/base-papers1-43-ru.tex")
BASE_UK = Path("C:/Users/user/Documents/interlanguage/03_projects/language_management/slavic_interslavic/noether_slavic_v018/release/source/base-papers1-43-uk.tex")
P45_RU = Path("C:/Users/user/Documents/interlanguage/03_projects/language_management/slavic_interslavic/noether_slavic_v018/release/source/45-ru.tex")
P45_UK = Path("C:/Users/user/Documents/interlanguage/03_projects/language_management/slavic_interslavic/noether_slavic_v018/release/source/45-uk.tex")
BIB_RU = Path("C:/Users/user/Documents/interlanguage/03_projects/language_management/slavic_interslavic/noether_slavic_v018/release/source/bib-ru.tex")
BIB_UK = Path("C:/Users/user/Documents/interlanguage/03_projects/language_management/slavic_interslavic/noether_slavic_v018/release/source/bib-uk.tex")


class DuplicateKeyError(ValueError):
    pass


def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha_text(text: str) -> str:
    return sha_bytes(text.encode("utf-8"))


def identity(path: Path, role: str | None = None, input_id: str | None = None) -> dict[str, Any]:
    data = path.read_bytes()
    row: dict[str, Any] = {"path": path.as_posix(), "bytes": len(data), "sha256": sha_bytes(data)}
    if role is not None:
        row["role"] = role
    if input_id is not None:
        row = {"input_id": input_id, **row}
    return row


def write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def strict_input_pins() -> list[dict[str, Any]]:
    rows = []
    for input_id, (raw, expected_bytes, expected_sha) in INPUTS.items():
        path = Path(raw)
        actual = identity(path, input_id=input_id)
        if actual["bytes"] != expected_bytes or actual["sha256"] != expected_sha:
            raise RuntimeError(f"input identity drift: {input_id}")
        actual["read_only"] = True
        rows.append(actual)
    return rows


def line(path: Path, number: int) -> str:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not 1 <= number <= len(lines):
        raise RuntimeError(f"line out of range: {path}:{number}")
    return lines[number - 1]


def nth_column(text: str, surface: str, occurrence: int = 1) -> int:
    start = 0
    found = -1
    for _ in range(occurrence):
        found = text.find(surface, start)
        if found < 0:
            raise RuntimeError(f"surface not found: {surface!r}")
        start = found + len(surface)
    return found + 1


def line_comparator(role: str, path: Path, number: int, surface: str, occurrence: int, alignment_note: str) -> dict[str, Any]:
    text = line(path, number)
    col = nth_column(text, surface, occurrence)
    return {
        "role": role,
        "evidence_role": "german_meaning_authority" if role == "de" else "east_only_comparator_not_native_validated",
        "branch_scope": "meaning_authority" if role == "de" else "east_slavic_only",
        "path": path.as_posix(),
        "file_sha256": identity(path)["sha256"],
        "line_1based": number,
        "column_start_scalar_1based": col,
        "column_end_scalar_exclusive_1based": col + len(surface),
        "surface": surface,
        "surface_sha256": sha_text(surface),
        "logical_line_sha256": sha_text(text),
        "context_excerpt": text,
        "context_excerpt_sha256": sha_text(text),
        "alignment_note": alignment_note,
    }


def effect_comparator(record: dict[str, Any]) -> dict[str, Any]:
    effect = record["effect_locus"]
    path = Path(effect["path"])
    text = line(path, effect["start_line_1based"])
    if sha_text(text) != effect["start_line_sha256"]:
        raise RuntimeError(f"effect line hash mismatch: {record['ledger_id']}")
    return {
        "role": "isv",
        "evidence_role": "current_editable_latin_baseline_not_official_grammar",
        "branch_scope": "constructed_interslavic_baseline",
        "path": path.as_posix(),
        "file_sha256": effect["file_sha256"],
        "line_1based": effect["start_line_1based"],
        "column_start_scalar_1based": effect["start_column_scalar_1based"],
        "column_end_scalar_exclusive_1based": effect["end_column_scalar_exclusive_1based"],
        "surface": effect["span_text"],
        "surface_sha256": effect["span_sha256"],
        "logical_line_sha256": effect["start_line_sha256"],
        "context_excerpt": record["context_window"]["window_text"],
        "context_excerpt_sha256": record["context_window"]["window_text_sha256"],
        "alignment_note": "exact current Latin effect locus; not official grammar, native review, or independent branch evidence",
    }


def existing_comparator(raw: dict[str, Any]) -> dict[str, Any]:
    path = Path(raw["path"])
    text = line(path, raw["line_1based"])
    surface = raw["surface"]
    col = raw["column_scalar_1based"]
    if text[col - 1 : col - 1 + len(surface)] != surface or sha_text(text) != raw["logical_line_sha256"]:
        raise RuntimeError(f"comparison locator mismatch: {path}:{raw['line_1based']}")
    return {
        "role": "de" if raw["role"] == "german_body" else raw["role"],
        "evidence_role": "german_meaning_authority" if raw["role"] == "german_body" else "east_only_comparator_not_native_validated",
        "branch_scope": "meaning_authority" if raw["role"] == "german_body" else "east_slavic_only",
        "path": path.as_posix(),
        "file_sha256": raw["file_sha256"],
        "line_1based": raw["line_1based"],
        "column_start_scalar_1based": col,
        "column_end_scalar_exclusive_1based": col + len(surface),
        "surface": surface,
        "surface_sha256": sha_text(surface),
        "logical_line_sha256": raw["logical_line_sha256"],
        "context_excerpt": raw["context_excerpt"],
        "context_excerpt_sha256": sha_text(raw["context_excerpt"]),
        "alignment_note": "exact documentary comparator from fixed successor v1; same-information review remains pending",
    }


def normalize_alternatives(items: list[dict[str, Any]]) -> list[dict[str, str]]:
    return [
        {
            "label": str(item.get("label", item.get("option", ""))),
            "state": str(item.get("state", "unspecified")),
            "basis_or_reason": str(item.get("basis_or_reason", item.get("reason", ""))),
        }
        for item in items
    ]


def morph_surface(raw: dict[str, Any], source: dict[str, Any]) -> dict[str, Any]:
    path = Path(source["absolute_path"])
    lines = path.read_text(encoding="utf-8").splitlines()
    context = raw["context"]
    context_text = "\n".join(lines[context["line_start"] - 1 : context["line_end"]])
    focus = context_text if context["focus_kind"] == "whole_context" else context["focus_text"]
    if sha_text(context_text) != context["sha256_utf8_lf"] or sha_text(focus) != context["focus_sha256_utf8"]:
        raise RuntimeError(f"morphology surface hash mismatch: {raw['source_id']}")
    return {
        "source_id": raw["source_id"],
        "language": raw["language"],
        "script": raw["script"],
        "evidence_role": raw["evidence_role"],
        "branch_scope": raw["branch_scope"],
        "controlled_occurrence": raw["controlled_occurrence"],
        "source_path": path.as_posix(),
        "source_file_sha256": source["sha256"],
        "context": raw["context"],
        "context_text": context_text,
        "resolved_focus_text": focus,
        "structural_anchor": raw["structural_anchor"],
    }


def build_morphology_requests(morph: dict[str, Any]) -> list[dict[str, Any]]:
    sources = {row["source_id"]: row for row in morph["source_pins"]}
    grammar = {row["rule_id"]: row for row in morph["grammar_rules"]}
    rows = []
    for ordinal, locus in enumerate(morph["loci"], 1):
        request_id = f"CRP-MORPH-{ordinal:02d}"
        evidence = {lang: morph_surface(raw, sources[raw["source_id"]]) for lang, raw in locus["surfaces"].items()}
        rows.append({
            "request_id": request_id,
            "request_kind": "morphology_same_information_branch_arms",
            "source_locus_id": locus["locus_id"],
            "paper_id": locus["paper_id"],
            "locus_role": locus["locus_role"],
            "semantic_focus": {
                "phenomenon": locus["parent_pin"]["phenomenon"],
                "contrast_class": locus["contrast_requirement"]["contrast_class"],
                "exact_coherent_contrast_required": locus["contrast_requirement"]["exact_coherent_contrast_required"],
                "preserve": locus["contrast_requirement"]["preserve"],
                "prohibited": locus["contrast_requirement"]["prohibited"],
            },
            "evidence_surfaces": evidence,
            "grammar_constraints": [grammar[rule_id] for rule_id in locus["grammar_rule_ids"]],
            "coverage": locus["coverage"],
            "required_arms": [
                {"arm_id": f"{request_id}-WEST", "macrobranch": "west", "state": "missing_not_authored", "authored_whole_sentence": None, "author_identity": None, "author_native_language": None, "source_evidence": None},
                {"arm_id": f"{request_id}-SOUTH", "macrobranch": "south", "state": "missing_not_authored", "authored_whole_sentence": None, "author_identity": None, "author_native_language": None, "source_evidence": None},
            ],
            "questions": [
                {"question_id": f"{request_id}-Q-WEST", "reviewer_profile_id": "RP-WEST-AUTHOR", "question": f"Author one coherent West-branch whole sentence for {locus['locus_id']} that preserves the pinned meaning and changes only the declared {locus['contrast_requirement']['contrast_class']} contrast; explain case/agreement/government/order choices.", "response": None},
                {"question_id": f"{request_id}-Q-SOUTH", "reviewer_profile_id": "RP-SOUTH-AUTHOR", "question": f"Author one coherent South-branch whole sentence for {locus['locus_id']} that preserves the pinned meaning and changes only the declared {locus['contrast_requirement']['contrast_class']} contrast; explain case/agreement/government/order choices.", "response": None},
                {"question_id": f"{request_id}-Q-GRAMMAR", "reviewer_profile_id": "RP-INDEPENDENT-GRAMMAR", "question": "After both authored arms exist, independently check same-information alignment, morphology, mathematical sense, register, and branch naturalness; do not infer intelligibility.", "response": None},
            ],
            "review_state": "held_missing_west_south_authored_arms_and_qualified_independent_review",
            "adverse_evidence": locus["adverse_evidence"],
            "source_record_semantic_sha256": sha_text(json.dumps(locus, ensure_ascii=False, sort_keys=True, separators=(",", ":"))),
            "application_state": "no_application_no_release_no_claim",
        })
    return rows


def normalization_comparators(record: dict[str, Any]) -> list[dict[str, Any]]:
    ledger_id = record["ledger_id"]
    if record["family_or_route"] in {"lexeme:simultaneous", "lexeme:step"}:
        return [existing_comparator(raw) for raw in record["comparison_locators"]] + [effect_comparator(record)]
    if ledger_id in NOETHER_COMPARATORS:
        de, ru, uk = NOETHER_COMPARATORS[ledger_id]
        ru_path, uk_path = (BIB_RU, BIB_UK) if ledger_id == "SLISV-SUCC-IN-0078" else (P45_RU, P45_UK)
        note = "exact policy comparator; same-information and preferred Interslavic name treatment remain pending qualified review"
        return [
            line_comparator("de", DE, *de, note),
            line_comparator("ru", ru_path, *ru, note),
            line_comparator("uk", uk_path, *uk, note),
            effect_comparator(record),
        ]
    if ledger_id == "SLISV-SUCC-IN-0080":
        note = "exact same-topic comparator; proposed Interslavic recast remains model-authored and unreviewed"
        return [
            line_comparator("de", DE, 8612, "Weierstraßsche Parameterdarstellung", 1, note),
            line_comparator("ru", BASE_RU, 9297, "параметрическое представление Вейерштрасса", 1, note),
            line_comparator("uk", BASE_UK, 9258, "параметричне подання Вейєрштрасса", 1, note),
            effect_comparator(record),
        ]
    raise RuntimeError(f"unexpected normalization record: {ledger_id}")


def build_normalization_requests(successor: dict[str, Any]) -> list[dict[str, Any]]:
    by_id = {row["ledger_id"]: row for row in successor["records"]}
    if not all(ledger_id in by_id for ledger_id in TARGET_LEDGER_IDS):
        raise RuntimeError("normalization target set incomplete")
    rows = []
    for ordinal, ledger_id in enumerate(TARGET_LEDGER_IDS, 1):
        source = by_id[ledger_id]
        proposal = source["proposal"]
        if source["family_or_route"] == "lexeme:simultaneous":
            group = "simultaneity"
            focus = source["sense_and_morphology"]
        elif source["family_or_route"] == "lexeme:step":
            group = "korak_step"
            focus = source["sense_and_morphology"]
        elif ledger_id == "SLISV-SUCC-IN-0080":
            group = "weierstrass_recast"
            focus = {"mathematical_or_prose_sense": "Weierstrass-type parametric representation in a complete mathematical sentence", "part_of_speech": "inflected eponym versus exact-name construction", "inflection_or_features": "whole-surface syntax must be grammatical and script-safe", "classification": "model-authored recast pending competent grammar review"}
        else:
            group = "noether_neter"
            focus = {"mathematical_or_prose_sense": "morphologically integrated Noether eponym or running-name surface; citation spellings remain exact", "part_of_speech": "proper-name/eponym surface with Interslavic inflection", "inflection_or_features": "review the complete surface, not a protected stem plus projected suffix", "classification": "editorial Neter proposal pending competent native/community review"}
        request_id = f"CRP-NORM-{ordinal:02d}"
        rows.append({
            "request_id": request_id,
            "request_kind": "normalization_context_choice",
            "choice_group": group,
            "source_ledger_id": ledger_id,
            "upstream_id": source["upstream_id"],
            "effect_locus": source["effect_locus"],
            "context_window": source["context_window"],
            "comparison_surfaces": normalization_comparators(source),
            "comparison_alignment_state": "exact_locators_and_hashes_bound_same_information_or_policy_alignment_pending_qualified_review",
            "semantic_focus": focus,
            "current_surface": proposal["current_text"],
            "candidate_latin_surface": proposal["candidate_latin_text"],
            "candidate_cyrillic_surface": proposal["candidate_cyrillic_text"],
            "alternatives": normalize_alternatives(proposal["alternatives"]),
            "adverse_evidence": [item["text"] for item in proposal["adverse_evidence"]],
            "evidence_facts": [item["text"] for item in proposal["evidence_facts"]],
            "primary_question": {"question_id": f"{request_id}-Q-CONTEXT", "question": f"For exact context {source['upstream_id']} ({proposal['current_text']}), {proposal['review_question']}", "response": None},
            "required_reviewer_profiles": ["RP-WEST-AUTHOR", "RP-SOUTH-AUTHOR", "RP-INDEPENDENT-GRAMMAR", "RP-COMMUNITY-GOVERNANCE"],
            "response_slots": {"west_branch_review": None, "south_branch_review": None, "independent_grammar_review": None, "community_governance_comment": None},
            "review_state": "held_no_attributable_review_return",
            "source_record_semantic_sha256": source["record_semantic_sha256"],
            "application_state": "no_application_no_release_no_claim",
        })
    return rows


def build_authority_captures(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    authority_ids = {"ISV-AUTH-002", "ISV-AUTH-003", "ISV-AUTH-004"}
    root = Path(INPUTS["IN-AUTHORITY-MANIFEST"][0]).parent
    rows = []
    for capture in manifest["captures"]:
        if capture["authority_id"] not in authority_ids or capture["capture_mode"] != "exact_local_bytes":
            continue
        path = root / capture["local_path"]
        actual = identity(path)
        if actual["bytes"] != capture["bytes"] or actual["sha256"] != capture["sha256"]:
            raise RuntimeError(f"authority capture drift: {capture['entry_id']}")
        rows.append({
            "capture_id": capture["entry_id"], "authority_id": capture["authority_id"],
            "path": path.as_posix(), "bytes": capture["bytes"], "sha256": capture["sha256"],
            "disposition": capture["disposition"], "claim_boundary": capture["claim_boundary"],
        })
    return rows


def build_source_pins(morphology: list[dict[str, Any]], normalization: list[dict[str, Any]]) -> list[dict[str, Any]]:
    roles: dict[str, set[str]] = {}
    for request in morphology:
        for lang, surface in request["evidence_surfaces"].items():
            roles.setdefault(surface["source_path"], set()).add(f"morphology_{lang}")
    for request in normalization:
        for surface in request["comparison_surfaces"]:
            roles.setdefault(surface["path"], set()).add(f"normalization_{surface['role']}")
    return [{**identity(Path(path)), "roles": sorted(role_set)} for path, role_set in sorted(roles.items())]


def reviewer_profiles() -> list[dict[str, Any]]:
    return [
        {"profile_id": "RP-WEST-AUTHOR", "role": "west_branch_native_or_near_native_author", "macrobranch": "west", "minimum_qualifications": ["declare native/dominant Slavic language and relevant dialect", "demonstrate competent Interslavic reading and writing", "understand the mathematical sentence or work with a named subject reviewer", "author a coherent whole sentence rather than a token mosaic", "declare conflicts and whether the answer is individual or organizational"], "not_sufficient": ["East-only evidence", "machine translation", "model-generated surface without attributable human authorship", "anonymous approval"]},
        {"profile_id": "RP-SOUTH-AUTHOR", "role": "south_branch_native_or_near_native_author", "macrobranch": "south", "minimum_qualifications": ["declare native/dominant Slavic language and relevant dialect", "demonstrate competent Interslavic reading and writing", "understand the mathematical sentence or work with a named subject reviewer", "author a coherent whole sentence rather than a token mosaic", "declare conflicts and whether the answer is individual or organizational"], "not_sufficient": ["East-only evidence", "machine translation", "model-generated surface without attributable human authorship", "anonymous approval"]},
        {"profile_id": "RP-INDEPENDENT-GRAMMAR", "role": "independent_interslavic_grammar_and_math_prose_reviewer", "macrobranch": None, "minimum_qualifications": ["document Interslavic grammar competence", "be independent of the surface author for the reviewed arm", "check meaning, morphology, syntax, register, and mathematical sense", "retain adverse evidence and uncertainty"], "not_sufficient": ["schema validation alone", "official grammar citation without context review", "self-review presented as independent"]},
        {"profile_id": "RP-COMMUNITY-GOVERNANCE", "role": "attributable_community_or_governance_reviewer", "macrobranch": None, "minimum_qualifications": ["state identity, role, and authority to speak only for self or named body", "distinguish editorial recommendation from measured intelligibility", "declare conflicts and scope", "return a dated review artifact"], "not_sufficient": ["packet preparation", "silence", "prior unrelated community activity", "a claim that Jan van Steenbergen has seen this packet without an attributable return"]},
    ]


def build_schema() -> dict[str, Any]:
    sha = {"type": "string", "pattern": "^[A-F0-9]{64}$"}
    nullable_string = {"type": ["string", "null"]}
    identity_schema = {"type": "object", "additionalProperties": False, "required": ["input_id", "path", "bytes", "sha256", "read_only"], "properties": {"input_id": {"type": "string", "pattern": "^IN-"}, "path": {"type": "string", "pattern": "^[A-Za-z]:/"}, "bytes": {"type": "integer", "minimum": 1}, "sha256": sha, "read_only": {"const": True}}}
    question = {"type": "object", "additionalProperties": False, "required": ["question_id", "question", "response"], "properties": {"question_id": {"type": "string"}, "reviewer_profile_id": {"type": "string"}, "question": {"type": "string", "minLength": 1}, "response": {"type": "null"}}}
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema", "$id": "ISV_MI_COMMUNITY_REVIEW_PACKET_v001.schema.json",
        "title": "Interslavic Noether community review solicitation v001", "type": "object", "additionalProperties": False,
        "required": ["$schema", "schema_id", "packet_id", "recorded_at", "status", "classification", "scope", "claims", "input_pins", "governance_boundaries", "authority_context", "authority_capture_pins", "source_file_pins", "reviewer_qualification_profiles", "morphology_requests", "normalization_requests", "counts", "review_submission_contract", "limitations", "next_cursor"],
        "properties": {
            "$schema": {"const": "ISV_MI_COMMUNITY_REVIEW_PACKET_v001.schema.json"}, "schema_id": {"const": "ISV-MI-COMMUNITY-REVIEW-PACKET-v001"}, "packet_id": {"const": "ISV-MI-COMMUNITY-REVIEW-PACKET-20260811-v001"}, "recorded_at": {"const": "2026-08-11"},
            "status": {"const": "pre_review_non_approved_all_response_slots_empty"}, "classification": {"const": "internal_review_solicitation_only_no_contact_no_application_no_publication"},
            "scope": {"type": "object", "additionalProperties": False, "required": ["morphology_units", "normalization_units", "west_arms_present", "south_arms_present", "network_contact_performed", "publication_performed"], "properties": {"morphology_units": {"const": 5}, "normalization_units": {"const": 14}, "west_arms_present": {"const": 0}, "south_arms_present": {"const": 0}, "network_contact_performed": {"const": False}, "publication_performed": {"const": False}}},
            "claims": {"type": "object", "additionalProperties": False, "required": ["approved", "jan_contacted", "jan_has_seen_packet", "community_contacted", "native_review_received", "west_arms_complete", "south_arms_complete", "intelligibility_measured", "application_authorized", "reader_mutation_authorized", "release_ready", "publication_ready", "canonical_claim"], "properties": {key: {"const": False} for key in ["approved", "jan_contacted", "jan_has_seen_packet", "community_contacted", "native_review_received", "west_arms_complete", "south_arms_complete", "intelligibility_measured", "application_authorized", "reader_mutation_authorized", "release_ready", "publication_ready", "canonical_claim"]}},
            "input_pins": {"type": "array", "minItems": len(INPUTS), "maxItems": len(INPUTS), "items": identity_schema},
            "governance_boundaries": {"type": "array", "minItems": 4, "maxItems": 4, "items": {"type": "object", "additionalProperties": False, "required": ["decision_id", "input_id", "fixed_fact", "authority_boundary"], "properties": {"decision_id": {"enum": ["SLISV-20260811-040", "SLISV-20260811-041", "SLISV-20260811-042", "SLISV-20260811-043"]}, "input_id": {"enum": ["IN-DECISION-040", "IN-DECISION-041", "IN-DECISION-042", "IN-DECISION-043"]}, "fixed_fact": {"type": "string", "minLength": 20}, "authority_boundary": {"type": "string", "minLength": 20}}}},
            "authority_context": {"type": "object", "additionalProperties": False, "required": ["snapshot_id", "snapshot_status", "snapshot_review_state", "design_voting_boundary", "historical_voting_machine_boundary", "grammar_boundary", "orthography_boundary", "human_validation_boundary"], "properties": {"snapshot_id": {"type": "string"}, "snapshot_status": {"type": "string"}, "snapshot_review_state": {"const": "first_bounded_snapshot_parent_verification_pending"}, "design_voting_boundary": {"type": "string"}, "historical_voting_machine_boundary": {"const": "A historical Interslavic Voting Machine is documented as statistical design/governance background; this packet does not reconstruct an exact current algorithm or coefficient table and does not infer community approval."}, "grammar_boundary": {"type": "string"}, "orthography_boundary": {"type": "string"}, "human_validation_boundary": {"const": "absent_no_response_no_native_certification_no_community_vote_no_Jan_return"}}},
            "authority_capture_pins": {"type": "array", "minItems": 11, "items": {"type": "object", "additionalProperties": False, "required": ["capture_id", "authority_id", "path", "bytes", "sha256", "disposition", "claim_boundary"], "properties": {"capture_id": {"type": "string"}, "authority_id": {"enum": ["ISV-AUTH-002", "ISV-AUTH-003", "ISV-AUTH-004"]}, "path": {"type": "string"}, "bytes": {"type": "integer"}, "sha256": sha, "disposition": {"type": "string"}, "claim_boundary": {"type": "string"}}}},
            "source_file_pins": {"type": "array", "minItems": 4, "items": {"type": "object", "additionalProperties": False, "required": ["path", "bytes", "sha256", "roles"], "properties": {"path": {"type": "string"}, "bytes": {"type": "integer"}, "sha256": sha, "roles": {"type": "array", "minItems": 1, "uniqueItems": True, "items": {"type": "string"}}}}},
            "reviewer_qualification_profiles": {"type": "array", "minItems": 4, "maxItems": 4, "items": {"type": "object", "additionalProperties": False, "required": ["profile_id", "role", "macrobranch", "minimum_qualifications", "not_sufficient"], "properties": {"profile_id": {"type": "string", "pattern": "^RP-"}, "role": {"type": "string"}, "macrobranch": {"enum": ["west", "south", None]}, "minimum_qualifications": {"type": "array", "minItems": 4, "items": {"type": "string"}}, "not_sufficient": {"type": "array", "minItems": 3, "items": {"type": "string"}}}}},
            "morphology_requests": {"type": "array", "minItems": 5, "maxItems": 5, "items": {"$ref": "#/$defs/morphology_request"}},
            "normalization_requests": {"type": "array", "minItems": 14, "maxItems": 14, "items": {"$ref": "#/$defs/normalization_request"}},
            "counts": {"type": "object", "additionalProperties": False, "required": ["review_units", "morphology_units", "normalization_units", "simultaneity", "korak", "noether_neter", "weierstrass", "west_authored_arms", "south_authored_arms", "review_responses", "approvals", "application_claims"], "properties": {"review_units": {"const": 19}, "morphology_units": {"const": 5}, "normalization_units": {"const": 14}, "simultaneity": {"const": 5}, "korak": {"const": 1}, "noether_neter": {"const": 7}, "weierstrass": {"const": 1}, "west_authored_arms": {"const": 0}, "south_authored_arms": {"const": 0}, "review_responses": {"const": 0}, "approvals": {"const": 0}, "application_claims": {"const": 0}}},
            "review_submission_contract": {"type": "object", "additionalProperties": False, "required": ["v001_is_immutable_pre_review", "responses_must_be_separate_attributable_artifacts", "identity_and_qualification_required", "no_silence_as_approval", "no_merged_branch_authorship", "no_model_filled_arms", "no_application_effect"], "properties": {key: {"const": True} for key in ["v001_is_immutable_pre_review", "responses_must_be_separate_attributable_artifacts", "identity_and_qualification_required", "no_silence_as_approval", "no_merged_branch_authorship", "no_model_filled_arms", "no_application_effect"]}},
            "limitations": {"type": "array", "minItems": 6, "items": {"type": "string"}}, "next_cursor": {"type": "string", "minLength": 20},
        },
        "$defs": {
            "sha": sha,
            "context_locator": {"type": "object", "additionalProperties": False, "required": ["line_start", "line_end", "sha256_utf8_lf", "focus_kind", "focus_sha256_utf8"], "properties": {"line_start": {"type": "integer", "minimum": 1}, "line_end": {"type": "integer", "minimum": 1}, "sha256_utf8_lf": sha, "focus_kind": {"enum": ["whole_context", "exact_substring"]}, "focus_text": {"type": "string"}, "focus_sha256_utf8": sha}},
            "anchor": {"type": "object", "additionalProperties": False, "required": ["line", "text", "sha256_utf8"], "properties": {"line": {"type": "integer"}, "text": {"type": "string"}, "sha256_utf8": sha}},
            "morph_surface": {"type": "object", "additionalProperties": False, "required": ["source_id", "language", "script", "evidence_role", "branch_scope", "controlled_occurrence", "source_path", "source_file_sha256", "context", "context_text", "resolved_focus_text", "structural_anchor"], "properties": {"source_id": {"type": "string"}, "language": {"enum": ["de", "ru", "uk", "isv"]}, "script": {"enum": ["Latn", "Cyrl"]}, "evidence_role": {"type": "string"}, "branch_scope": {"type": "string"}, "controlled_occurrence": {"type": "string"}, "source_path": {"type": "string"}, "source_file_sha256": sha, "context": {"$ref": "#/$defs/context_locator"}, "context_text": {"type": "string"}, "resolved_focus_text": {"type": "string"}, "structural_anchor": {"$ref": "#/$defs/anchor"}}},
            "grammar_rule": {"type": "object", "additionalProperties": False, "required": ["rule_id", "source_id", "line", "text", "sha256_utf8", "role_boundary"], "properties": {"rule_id": {"type": "string"}, "source_id": {"type": "string"}, "line": {"type": "integer"}, "text": {"type": "string"}, "sha256_utf8": sha, "role_boundary": {"type": "string"}}},
            "arm": {"type": "object", "additionalProperties": False, "required": ["arm_id", "macrobranch", "state", "authored_whole_sentence", "author_identity", "author_native_language", "source_evidence"], "properties": {"arm_id": {"type": "string"}, "macrobranch": {"enum": ["west", "south"]}, "state": {"const": "missing_not_authored"}, "authored_whole_sentence": {"type": "null"}, "author_identity": {"type": "null"}, "author_native_language": {"type": "null"}, "source_evidence": {"type": "null"}}},
            "morph_semantic_focus": {"type": "object", "additionalProperties": False, "required": ["phenomenon", "contrast_class", "exact_coherent_contrast_required", "preserve", "prohibited"], "properties": {"phenomenon": {"type": "string"}, "contrast_class": {"enum": ["direct_morphology", "direct_morphosyntax", "direct_morphology_and_morphosyntax"]}, "exact_coherent_contrast_required": {"type": "string"}, "preserve": {"type": "array", "minItems": 1, "items": {"type": "string"}}, "prohibited": {"type": "array", "minItems": 4, "items": {"type": "string"}}}},
            "coverage": {"type": "object", "additionalProperties": False, "required": ["german", "east", "official_grammar", "west", "south", "native"], "properties": {"german": {"const": "exact_meaning_authority_span_bound"}, "east": {"const": "ru_and_uk_exact_spans_east_only_not_independent_branch_breadth"}, "official_grammar": {"const": "partial_constraint_only_not_branch_or_intelligibility_evidence"}, "west": {"const": "missing_zero_surfaces"}, "south": {"const": "missing_zero_surfaces"}, "native": {"const": "missing_zero_authorship_and_review_records"}}},
            "morphology_request": {"type": "object", "additionalProperties": False, "required": ["request_id", "request_kind", "source_locus_id", "paper_id", "locus_role", "semantic_focus", "evidence_surfaces", "grammar_constraints", "coverage", "required_arms", "questions", "review_state", "adverse_evidence", "source_record_semantic_sha256", "application_state"], "properties": {"request_id": {"pattern": "^CRP-MORPH-0[1-5]$", "type": "string"}, "request_kind": {"const": "morphology_same_information_branch_arms"}, "source_locus_id": {"pattern": "^MI-MORPH-GAP-0[1-5]$", "type": "string"}, "paper_id": {"type": "string"}, "locus_role": {"type": "string"}, "semantic_focus": {"$ref": "#/$defs/morph_semantic_focus"}, "evidence_surfaces": {"type": "object", "additionalProperties": False, "required": ["de", "ru", "uk", "isv"], "properties": {lang: {"$ref": "#/$defs/morph_surface"} for lang in ["de", "ru", "uk", "isv"]}}, "grammar_constraints": {"type": "array", "minItems": 2, "items": {"$ref": "#/$defs/grammar_rule"}}, "coverage": {"$ref": "#/$defs/coverage"}, "required_arms": {"type": "array", "minItems": 2, "maxItems": 2, "items": {"$ref": "#/$defs/arm"}}, "questions": {"type": "array", "minItems": 3, "maxItems": 3, "items": question}, "review_state": {"const": "held_missing_west_south_authored_arms_and_qualified_independent_review"}, "adverse_evidence": {"type": "array", "items": {"type": "string"}}, "source_record_semantic_sha256": sha, "application_state": {"const": "no_application_no_release_no_claim"}}},
            "effect": {"type": "object", "additionalProperties": False, "required": ["path", "file_sha256", "start_line_1based", "start_column_scalar_1based", "end_line_1based", "end_column_scalar_exclusive_1based", "start_byte_utf8_0based", "end_byte_utf8_exclusive_0based", "byte_length_utf8", "scalar_length", "span_text", "span_sha256", "start_line_sha256", "end_line_sha256"], "properties": {"path": {"type": "string"}, "file_sha256": sha, "start_line_1based": {"type": "integer", "minimum": 1}, "start_column_scalar_1based": {"type": "integer", "minimum": 1}, "end_line_1based": {"type": "integer", "minimum": 1}, "end_column_scalar_exclusive_1based": {"type": "integer", "minimum": 2}, "start_byte_utf8_0based": {"type": "integer", "minimum": 0}, "end_byte_utf8_exclusive_0based": {"type": "integer", "minimum": 1}, "byte_length_utf8": {"type": "integer", "minimum": 1}, "scalar_length": {"type": "integer", "minimum": 1}, "span_text": {"type": "string", "minLength": 1}, "span_sha256": sha, "start_line_sha256": sha, "end_line_sha256": sha}},
            "context": {"type": "object", "additionalProperties": False, "required": ["line_1based", "window_start_column_scalar_1based", "window_end_column_scalar_exclusive_1based", "candidate_start_in_window_scalar_0based", "candidate_end_in_window_scalar_exclusive_0based", "line_scalar_length", "line_text_sha256", "window_text", "window_text_sha256", "hash_convention"], "properties": {"line_1based": {"type": "integer", "minimum": 1}, "window_start_column_scalar_1based": {"type": "integer", "minimum": 1}, "window_end_column_scalar_exclusive_1based": {"type": "integer", "minimum": 2}, "candidate_start_in_window_scalar_0based": {"type": "integer", "minimum": 0}, "candidate_end_in_window_scalar_exclusive_0based": {"type": "integer", "minimum": 1}, "line_scalar_length": {"type": "integer", "minimum": 1}, "line_text_sha256": sha, "window_text": {"type": "string", "minLength": 1}, "window_text_sha256": sha, "hash_convention": {"const": "UTF-8 scalar text without line terminator"}}},
            "norm_semantic_focus": {"type": "object", "additionalProperties": False, "required": ["mathematical_or_prose_sense", "part_of_speech", "inflection_or_features", "classification"], "properties": {"mathematical_or_prose_sense": {"type": "string"}, "part_of_speech": {"type": "string"}, "inflection_or_features": {"type": "string"}, "classification": {"type": "string"}}},
            "comparison": {"type": "object", "additionalProperties": False, "required": ["role", "evidence_role", "branch_scope", "path", "file_sha256", "line_1based", "column_start_scalar_1based", "column_end_scalar_exclusive_1based", "surface", "surface_sha256", "logical_line_sha256", "context_excerpt", "context_excerpt_sha256", "alignment_note"], "properties": {"role": {"enum": ["de", "ru", "uk", "isv"]}, "evidence_role": {"type": "string"}, "branch_scope": {"enum": ["meaning_authority", "east_slavic_only", "constructed_interslavic_baseline"]}, "path": {"type": "string"}, "file_sha256": sha, "line_1based": {"type": "integer"}, "column_start_scalar_1based": {"type": "integer"}, "column_end_scalar_exclusive_1based": {"type": "integer"}, "surface": {"type": "string"}, "surface_sha256": sha, "logical_line_sha256": sha, "context_excerpt": {"type": "string"}, "context_excerpt_sha256": sha, "alignment_note": {"type": "string"}}},
            "alternative": {"type": "object", "additionalProperties": False, "required": ["label", "state", "basis_or_reason"], "properties": {"label": {"type": "string"}, "state": {"type": "string"}, "basis_or_reason": {"type": "string"}}},
            "normalization_request": {"type": "object", "additionalProperties": False, "required": ["request_id", "request_kind", "choice_group", "source_ledger_id", "upstream_id", "effect_locus", "context_window", "comparison_surfaces", "comparison_alignment_state", "semantic_focus", "current_surface", "candidate_latin_surface", "candidate_cyrillic_surface", "alternatives", "adverse_evidence", "evidence_facts", "primary_question", "required_reviewer_profiles", "response_slots", "review_state", "source_record_semantic_sha256", "application_state"], "properties": {"request_id": {"type": "string", "pattern": "^CRP-NORM-(0[1-9]|1[0-4])$"}, "request_kind": {"const": "normalization_context_choice"}, "choice_group": {"enum": ["simultaneity", "korak_step", "noether_neter", "weierstrass_recast"]}, "source_ledger_id": {"type": "string"}, "upstream_id": {"type": "string"}, "effect_locus": {"$ref": "#/$defs/effect"}, "context_window": {"$ref": "#/$defs/context"}, "comparison_surfaces": {"type": "array", "minItems": 4, "maxItems": 4, "items": {"$ref": "#/$defs/comparison"}}, "comparison_alignment_state": {"const": "exact_locators_and_hashes_bound_same_information_or_policy_alignment_pending_qualified_review"}, "semantic_focus": {"$ref": "#/$defs/norm_semantic_focus"}, "current_surface": {"type": "string"}, "candidate_latin_surface": {"type": ["string", "null"]}, "candidate_cyrillic_surface": nullable_string, "alternatives": {"type": "array", "minItems": 1, "items": {"$ref": "#/$defs/alternative"}}, "adverse_evidence": {"type": "array", "minItems": 1, "items": {"type": "string"}}, "evidence_facts": {"type": "array", "minItems": 1, "items": {"type": "string"}}, "primary_question": question, "required_reviewer_profiles": {"type": "array", "minItems": 4, "maxItems": 4, "uniqueItems": True, "items": {"enum": ["RP-WEST-AUTHOR", "RP-SOUTH-AUTHOR", "RP-INDEPENDENT-GRAMMAR", "RP-COMMUNITY-GOVERNANCE"]}}, "response_slots": {"type": "object", "additionalProperties": False, "required": ["west_branch_review", "south_branch_review", "independent_grammar_review", "community_governance_comment"], "properties": {key: {"type": "null"} for key in ["west_branch_review", "south_branch_review", "independent_grammar_review", "community_governance_comment"]}}, "review_state": {"const": "held_no_attributable_review_return"}, "source_record_semantic_sha256": sha, "application_state": {"const": "no_application_no_release_no_claim"}}},
        },
    }


CSV_FIELDS = ["request_id", "request_kind", "source_id", "group_or_role", "current_surface", "candidate_latin_surface", "de_locator", "ru_locator", "uk_locator", "isv_locator", "required_reviewers", "state", "primary_question"]


def locator(surface: dict[str, Any]) -> str:
    if "source_path" in surface:
        c = surface["context"]
        return f"{surface['source_path']}:{c['line_start']}-{c['line_end']}#{c['sha256_utf8_lf']}"
    return f"{surface['path']}:{surface['line_1based']}:{surface['column_start_scalar_1based']}-{surface['column_end_scalar_exclusive_1based']}#{surface['logical_line_sha256']}"


def csv_projection(packet: dict[str, Any]) -> str:
    out = io.StringIO(newline="")
    writer = csv.DictWriter(out, fieldnames=CSV_FIELDS, lineterminator="\n")
    writer.writeheader()
    for row in packet["morphology_requests"]:
        s = row["evidence_surfaces"]
        writer.writerow({"request_id": row["request_id"], "request_kind": row["request_kind"], "source_id": row["source_locus_id"], "group_or_role": row["locus_role"], "current_surface": s["isv"]["controlled_occurrence"], "candidate_latin_surface": "", "de_locator": locator(s["de"]), "ru_locator": locator(s["ru"]), "uk_locator": locator(s["uk"]), "isv_locator": locator(s["isv"]), "required_reviewers": "RP-WEST-AUTHOR|RP-SOUTH-AUTHOR|RP-INDEPENDENT-GRAMMAR", "state": row["review_state"], "primary_question": row["semantic_focus"]["exact_coherent_contrast_required"]})
    for row in packet["normalization_requests"]:
        surfaces = {s["role"]: s for s in row["comparison_surfaces"]}
        writer.writerow({"request_id": row["request_id"], "request_kind": row["request_kind"], "source_id": row["source_ledger_id"], "group_or_role": row["choice_group"], "current_surface": row["current_surface"], "candidate_latin_surface": row["candidate_latin_surface"] or "", "de_locator": locator(surfaces["de"]), "ru_locator": locator(surfaces["ru"]), "uk_locator": locator(surfaces["uk"]), "isv_locator": locator(surfaces["isv"]), "required_reviewers": "|".join(row["required_reviewer_profiles"]), "state": row["review_state"], "primary_question": row["primary_question"]["question"]})
    return out.getvalue()


def reviewer_markdown(packet: dict[str, Any]) -> str:
    lines = [
        "# Interslavic Noether pilot — bounded review solicitation v001", "",
        "> **NON-APPROVED / NOT SENT.** This packet contains no West or South authored arm, no native or community return, no participant result, and no application or release authority. Jan van Steenbergen has not been contacted and is not claimed to have seen this packet.", "",
        "Return any review as a separate, dated, attributable artifact. State your native/dominant language, relevant competence, role, conflicts, and whether you speak only for yourself or for a named body. Do not edit this immutable v001 packet.", "",
        "## Reviewer qualification profiles", "",
    ]
    for profile in packet["reviewer_qualification_profiles"]:
        lines += [f"### {profile['profile_id']} — {profile['role']}", "", "Required: " + "; ".join(profile["minimum_qualifications"]) + ".", "", "Not sufficient: " + "; ".join(profile["not_sufficient"]) + ".", ""]
    lines += ["## A. Five morphology/morphosyntax loci", ""]
    for row in packet["morphology_requests"]:
        lines += [f"### {row['request_id']} — {row['source_locus_id']} ({row['paper_id']})", "", f"**Focus:** {row['semantic_focus']['phenomenon']}", "", f"**Required coherent contrast:** {row['semantic_focus']['exact_coherent_contrast_required']}", ""]
        for lang in ["de", "ru", "uk", "isv"]:
            s = row["evidence_surfaces"][lang]
            lines += [f"- **{lang.upper()}** `{locator(s)}` — `{s['controlled_occurrence']}` — role `{s['evidence_role']}`", "", "```text", s["context_text"], "```", ""]
        lines += ["West authored arm: **MISSING / NULL**", "", "South authored arm: **MISSING / NULL**", ""]
        for q in row["questions"]:
            lines += [f"- `{q['question_id']}` ({q['reviewer_profile_id']}): {q['question']}"]
        lines += ["", "No response is recorded in v001.", ""]
    lines += ["## B. Fourteen normalization contexts", ""]
    for row in packet["normalization_requests"]:
        lines += [f"### {row['request_id']} — {row['source_ledger_id']} / {row['upstream_id']} ({row['choice_group']})", "", f"**Current:** `{row['current_surface']}`", "", f"**Candidate Latin:** `{row['candidate_latin_surface']}`", "", f"**Question:** {row['primary_question']['question']}", ""]
        for s in row["comparison_surfaces"]:
            lines += [f"- **{s['role'].upper()}** `{locator(s)}` — `{s['surface']}` — {s['alignment_note']}"]
        lines += ["", "**Context:**", "", "```text", row["context_window"]["window_text"], "```", "", "**Alternatives/adverse evidence:**"]
        for item in row["alternatives"]:
            lines += [f"- {item['label']} — {item['state']}: {item['basis_or_reason']}"]
        for item in row["adverse_evidence"]:
            lines += [f"- Adverse: {item}"]
        lines += ["", "West review: **NULL**; South review: **NULL**; independent grammar review: **NULL**; community comment: **NULL**.", ""]
    lines += ["## Return boundary", "", "A returned review can be evidence only after identity, qualification, exact request IDs, source hashes, independence, conflicts, and response custody are verified. Silence is not approval. A response does not itself authorize reader edits, release, publication, or an intelligibility claim.", ""]
    return "\n".join(lines)


def fixtures() -> dict[str, Any]:
    return {"fixture_set_id": "ISV-MI-COMMUNITY-REVIEW-PACKET-v001-HOSTILE", "fixtures": [
        {"fixture_id": "fake_approval_and_Jan_claim", "expected_error": "FAKE_APPROVAL", "operations": [{"op": "replace", "path": "/claims/approved", "value": True}, {"op": "replace", "path": "/claims/jan_has_seen_packet", "value": True}]},
        {"fixture_id": "fake_native_approval_return", "expected_error": "FAKE_APPROVAL", "operations": [{"op": "replace", "path": "/claims/native_review_received", "value": True}, {"op": "replace", "path": "/normalization_requests/0/response_slots/west_branch_review", "value": {"identity": "invented", "approval": True}}]},
        {"fixture_id": "model_filled_west_arm", "expected_error": "MODEL_FILLED_ARM", "operations": [{"op": "replace", "path": "/morphology_requests/0/required_arms/0/state", "value": "model_filled"}, {"op": "replace", "path": "/morphology_requests/0/required_arms/0/authored_whole_sentence", "value": "fabricated West surface"}]},
        {"fixture_id": "missing_required_south_arm", "expected_error": "MISSING_REQUIRED_ARMS", "operations": [{"op": "remove", "path": "/morphology_requests/0/required_arms/1"}]},
        {"fixture_id": "merged_west_south_branch", "expected_error": "BRANCH_MERGING", "operations": [{"op": "replace", "path": "/morphology_requests/0/required_arms/1/macrobranch", "value": "west"}]},
        {"fixture_id": "east_promoted_to_pan_slavic", "expected_error": "EAST_AS_PAN_SLAVIC", "operations": [{"op": "replace", "path": "/morphology_requests/0/evidence_surfaces/ru/branch_scope", "value": "pan_slavic"}]},
        {"fixture_id": "altered_exact_locator", "expected_error": "ALTERED_LOCATOR_OR_HASH", "operations": [{"op": "replace", "path": "/morphology_requests/0/evidence_surfaces/de/context/line_start", "value": 1}]},
        {"fixture_id": "altered_context_hash", "expected_error": "ALTERED_LOCATOR_OR_HASH", "operations": [{"op": "replace", "path": "/normalization_requests/0/comparison_surfaces/0/logical_line_sha256", "value": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"}]},
        {"fixture_id": "application_and_release_claim", "expected_error": "APPLICATION_OR_RELEASE_CLAIM", "operations": [{"op": "replace", "path": "/claims/application_authorized", "value": True}, {"op": "replace", "path": "/claims/release_ready", "value": True}]},
    ]}


def build_packet() -> dict[str, Any]:
    pins = strict_input_pins()
    morph = load_json(Path(INPUTS["IN-MORPH-PACKAGE"][0]))
    successor = load_json(Path(INPUTS["IN-SUCCESSOR-V1"][0]))
    authority = load_json(Path(INPUTS["IN-AUTHORITY-MANIFEST"][0]))
    morphology = build_morphology_requests(morph)
    normalization = build_normalization_requests(successor)
    authority_by_role = {row["role"]: row for row in authority["authorities"]}
    return {
        "$schema": SCHEMA.name, "schema_id": "ISV-MI-COMMUNITY-REVIEW-PACKET-v001", "packet_id": "ISV-MI-COMMUNITY-REVIEW-PACKET-20260811-v001", "recorded_at": "2026-08-11",
        "status": "pre_review_non_approved_all_response_slots_empty", "classification": "internal_review_solicitation_only_no_contact_no_application_no_publication",
        "scope": {"morphology_units": 5, "normalization_units": 14, "west_arms_present": 0, "south_arms_present": 0, "network_contact_performed": False, "publication_performed": False},
        "claims": {key: False for key in ["approved", "jan_contacted", "jan_has_seen_packet", "community_contacted", "native_review_received", "west_arms_complete", "south_arms_complete", "intelligibility_measured", "application_authorized", "reader_mutation_authorized", "release_ready", "publication_ready", "canonical_claim"]},
        "input_pins": pins,
        "governance_boundaries": [
            {"decision_id": "SLISV-20260811-040", "input_id": "IN-DECISION-040", "fixed_fact": "Route-B v002 supplies fourteen exact validated internal editorial inputs.", "authority_boundary": "It supplies no reader, release, publication, human, native, community, Jan, or marginal-intelligibility authority."},
            {"decision_id": "SLISV-20260811-041", "input_id": "IN-DECISION-041", "fixed_fact": "The exact successor-v1 bytes remain a bounded candidate/control evidence object.", "authority_boundary": "Its supplied validator is suspended as an application gate after nine of nine additional hostile false passes; no reader mutation is authorized."},
            {"decision_id": "SLISV-20260811-042", "input_id": "IN-DECISION-042", "fixed_fact": "Both Spark waves were parent-dispositioned and archived after all forty-two task outcomes were consumed.", "authority_boundary": "No Spark output was promoted directly into a reader, release, human-intelligibility claim, or publication payload."},
            {"decision_id": "SLISV-20260811-043", "input_id": "IN-DECISION-043", "fixed_fact": "The additive methodology lesson records the fixed-evidence versus validator/application-authority distinction and open gates.", "authority_boundary": "A completed agent artifact or retrospective is not parent verification, qualified human review, application authority, or publication authority."},
        ],
        "authority_context": {"snapshot_id": authority["snapshot_id"], "snapshot_status": authority["status"], "snapshot_review_state": authority["supersession"]["review_state"], "design_voting_boundary": authority_by_role["design_voting"]["claim_boundary"], "historical_voting_machine_boundary": "A historical Interslavic Voting Machine is documented as statistical design/governance background; this packet does not reconstruct an exact current algorithm or coefficient table and does not infer community approval.", "grammar_boundary": authority_by_role["grammar"]["claim_boundary"], "orthography_boundary": authority_by_role["orthography"]["claim_boundary"], "human_validation_boundary": "absent_no_response_no_native_certification_no_community_vote_no_Jan_return"},
        "authority_capture_pins": build_authority_captures(authority), "source_file_pins": build_source_pins(morphology, normalization), "reviewer_qualification_profiles": reviewer_profiles(),
        "morphology_requests": morphology, "normalization_requests": normalization,
        "counts": {"review_units": 19, "morphology_units": 5, "normalization_units": 14, "simultaneity": 5, "korak": 1, "noether_neter": 7, "weierstrass": 1, "west_authored_arms": 0, "south_authored_arms": 0, "review_responses": 0, "approvals": 0, "application_claims": 0},
        "review_submission_contract": {key: True for key in ["v001_is_immutable_pre_review", "responses_must_be_separate_attributable_artifacts", "identity_and_qualification_required", "no_silence_as_approval", "no_merged_branch_authorship", "no_model_filled_arms", "no_application_effect"]},
        "limitations": ["No reviewer has been contacted through this work unit.", "Jan van Steenbergen is not claimed to have received or seen this packet.", "No West or South morphology arm is authored or model-filled.", "Russian and Ukrainian are East-only evidence and never pan-Slavic coverage.", "Official grammar and voting sources constrain or compare; they do not supply native approval or measured comprehension.", "All fourteen normalization choices and five morphology loci remain held.", "No response can authorize application, release, publication, or a canonical claim without later parent-controlled gates."],
        "next_cursor": "Parent-verify this immutable pre-review packet. If authorized separately, send only to attributable qualified reviewers under the declared roles; preserve every return as a separate artifact; verify identity, qualification, branch independence, source hashes, same-information content, conflicts, and rights; retain missing or adverse rows; then build a versioned response/disposition package. Do not mutate readers or claim approval from packet preparation or silence.",
    }


def build_manifest(packet: dict[str, Any]) -> dict[str, Any]:
    generated = [PACKAGE, SCHEMA, CSV_PATH, REVIEWER_MD, FIXTURES, Path(__file__).resolve(), VALIDATOR]
    return {
        "manifest_id": "ISV-MI-COMMUNITY-REVIEW-PACKET-v001-MANIFEST", "packet_id": packet["packet_id"], "status": packet["status"],
        "generated_artifacts": [{"path": path.as_posix(), "bytes": len(path.read_bytes()), "sha256": sha_bytes(path.read_bytes()), "role": {PACKAGE: "canonical_packet", SCHEMA: "draft_2020_12_schema", CSV_PATH: "review_projection", REVIEWER_MD: "human_reviewer_projection", FIXTURES: "hostile_fixture_definitions", Path(__file__).resolve(): "deterministic_builder", VALIDATOR: "independent_no_write_validator"}[path]} for path in generated],
        "source_inputs": packet["input_pins"], "counts": packet["counts"], "claims": packet["claims"],
        "self_identity_policy": "manifest does not contain its own byte identity to avoid circular self-reference",
        "receipt_policy": "validation receipt binds this manifest and all seven generated artifacts; receipt does not contain its own identity",
        "validation_receipt_path": RECEIPT.as_posix(), "next_cursor": packet["next_cursor"],
    }


def main() -> int:
    if ROOT != Path("C:/Users/user/Documents/interlanguage/03_projects/language_management/slavic_interslavic/00_lane_control/marginal_intelligibility_20260811/community_review_packet_v001"):
        raise SystemExit("refusing unexpected output custody")
    packet = build_packet()
    write_json(PACKAGE, packet)
    write_json(SCHEMA, build_schema())
    CSV_PATH.write_text(csv_projection(packet), encoding="utf-8", newline="\n")
    REVIEWER_MD.write_text(reviewer_markdown(packet), encoding="utf-8", newline="\n")
    write_json(FIXTURES, fixtures())
    write_json(MANIFEST, build_manifest(packet))
    run = subprocess.run([sys.executable, "-B", str(VALIDATOR), "--emit-receipt"], cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if run.returncode:
        sys.stderr.buffer.write(run.stderr)
        sys.stderr.buffer.write(run.stdout)
        return run.returncode
    receipt = json.loads(run.stdout.decode("utf-8"), object_pairs_hook=unique_object)
    write_json(RECEIPT, receipt)
    print(f"BUILT review_units={packet['counts']['review_units']} morphology=5 normalization=14 status={receipt['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
