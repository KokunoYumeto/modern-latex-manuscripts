#!/usr/bin/env python3
"""Independent, no-write validator for the bounded community-review packet v001."""

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

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parent
EXPECTED_ROOT = Path("C:/Users/user/Documents/interlanguage/03_projects/language_management/slavic_interslavic/00_lane_control/marginal_intelligibility_20260811/community_review_packet_v001")
PACKAGE = ROOT / "ISV_MI_COMMUNITY_REVIEW_PACKET_v001.json"
SCHEMA = ROOT / "ISV_MI_COMMUNITY_REVIEW_PACKET_v001.schema.json"
CSV_PATH = ROOT / "ISV_MI_COMMUNITY_REVIEW_PACKET_v001.csv"
REVIEWER_MD = ROOT / "ISV_MI_COMMUNITY_REVIEW_PACKET_v001_REVIEWER.md"
FIXTURES = ROOT / "ISV_MI_COMMUNITY_REVIEW_PACKET_v001.hostile_fixtures.json"
MANIFEST = ROOT / "ISV_MI_COMMUNITY_REVIEW_PACKET_v001.manifest.json"
BUILDER = ROOT / "build_isv_mi_community_review_packet_v001.py"
VALIDATOR = Path(__file__).resolve()
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

NOETHER = {
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

GOVERNANCE = [
    {"decision_id": "SLISV-20260811-040", "input_id": "IN-DECISION-040", "fixed_fact": "Route-B v002 supplies fourteen exact validated internal editorial inputs.", "authority_boundary": "It supplies no reader, release, publication, human, native, community, Jan, or marginal-intelligibility authority."},
    {"decision_id": "SLISV-20260811-041", "input_id": "IN-DECISION-041", "fixed_fact": "The exact successor-v1 bytes remain a bounded candidate/control evidence object.", "authority_boundary": "Its supplied validator is suspended as an application gate after nine of nine additional hostile false passes; no reader mutation is authorized."},
    {"decision_id": "SLISV-20260811-042", "input_id": "IN-DECISION-042", "fixed_fact": "Both Spark waves were parent-dispositioned and archived after all forty-two task outcomes were consumed.", "authority_boundary": "No Spark output was promoted directly into a reader, release, human-intelligibility claim, or publication payload."},
    {"decision_id": "SLISV-20260811-043", "input_id": "IN-DECISION-043", "fixed_fact": "The additive methodology lesson records the fixed-evidence versus validator/application-authority distinction and open gates.", "authority_boundary": "A completed agent artifact or retrospective is not parent verification, qualified human review, application authority, or publication authority."},
]

CSV_FIELDS = ["request_id", "request_kind", "source_id", "group_or_role", "current_surface", "candidate_latin_surface", "de_locator", "ru_locator", "uk_locator", "isv_locator", "required_reviewers", "state", "primary_question"]


class DuplicateKeyError(ValueError):
    pass


class ValidationFailure(Exception):
    def __init__(self, code: str, message: str):
        super().__init__(message)
        self.code = code


def reject_constant(value: str) -> None:
    raise ValueError(f"non-finite JSON constant: {value}")


def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def decode_json(data: bytes, label: str, enforce_transport: bool) -> Any:
    if enforce_transport:
        if data.startswith(b"\xef\xbb\xbf"):
            raise ValidationFailure("TRANSPORT", f"{label}: UTF-8 BOM forbidden")
        if b"\r" in data:
            raise ValidationFailure("TRANSPORT", f"{label}: CR bytes forbidden")
        if not data.endswith(b"\n"):
            raise ValidationFailure("TRANSPORT", f"{label}: terminal LF required")
    try:
        text = data.decode("utf-8")
        return json.loads(text, object_pairs_hook=unique_object, parse_constant=reject_constant)
    except (UnicodeDecodeError, json.JSONDecodeError, DuplicateKeyError, ValueError) as exc:
        raise ValidationFailure("STRICT_JSON", f"{label}: {exc}") from exc


def load_json(path: Path, enforce_transport: bool = False) -> Any:
    return decode_json(path.read_bytes(), path.as_posix(), enforce_transport)


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha_text(text: str) -> str:
    return sha_bytes(text.encode("utf-8"))


def canonical_sha(value: Any) -> str:
    raw = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")
    return sha_bytes(raw)


def identity(path: Path, role: str | None = None, input_id: str | None = None) -> dict[str, Any]:
    data = path.read_bytes()
    row: dict[str, Any] = {"path": path.as_posix(), "bytes": len(data), "sha256": sha_bytes(data)}
    if role is not None:
        row["role"] = role
    if input_id is not None:
        row = {"input_id": input_id, **row}
    return row


def require(condition: bool, code: str, message: str) -> None:
    if not condition:
        raise ValidationFailure(code, message)


def exact(actual: Any, expected: Any, label: str, code: str = "ALTERED_LOCATOR_OR_HASH") -> None:
    require(actual == expected, code, f"{label} differs from independently reconstructed value")


def line(path: Path, number: int) -> str:
    lines = path.read_text(encoding="utf-8").splitlines()
    require(1 <= number <= len(lines), "ALTERED_LOCATOR_OR_HASH", f"line out of range: {path}:{number}")
    return lines[number - 1]


def nth_column(text: str, surface: str, occurrence: int) -> int:
    start = 0
    found = -1
    for _ in range(occurrence):
        found = text.find(surface, start)
        require(found >= 0, "ALTERED_LOCATOR_OR_HASH", f"surface absent: {surface!r}")
        start = found + len(surface)
    return found + 1


def expected_inputs() -> list[dict[str, Any]]:
    rows = []
    for input_id, (raw, expected_bytes, expected_sha) in INPUTS.items():
        path = Path(raw)
        actual = identity(path, input_id=input_id)
        exact(actual["bytes"], expected_bytes, f"input bytes {input_id}", "INPUT_DRIFT")
        exact(actual["sha256"], expected_sha, f"input hash {input_id}", "INPUT_DRIFT")
        load_json(path, enforce_transport=False)
        actual["read_only"] = True
        rows.append(actual)
    return rows


def expected_morph_surface(raw: dict[str, Any], source: dict[str, Any]) -> dict[str, Any]:
    path = Path(source["absolute_path"])
    file_identity = identity(path)
    exact(file_identity["sha256"], source["sha256"], f"morph source {source['source_id']}")
    lines = path.read_text(encoding="utf-8").splitlines()
    context = raw["context"]
    text = "\n".join(lines[context["line_start"] - 1:context["line_end"]])
    focus = text if context["focus_kind"] == "whole_context" else context["focus_text"]
    exact(sha_text(text), context["sha256_utf8_lf"], "morph context hash")
    exact(sha_text(focus), context["focus_sha256_utf8"], "morph focus hash")
    anchor = raw["structural_anchor"]
    anchor_text = lines[anchor["line"] - 1]
    exact(anchor_text, anchor["text"], "morph structural anchor text")
    exact(sha_text(anchor_text), anchor["sha256_utf8"], "morph structural anchor hash")
    return {
        "source_id": raw["source_id"], "language": raw["language"], "script": raw["script"],
        "evidence_role": raw["evidence_role"], "branch_scope": raw["branch_scope"],
        "controlled_occurrence": raw["controlled_occurrence"], "source_path": path.as_posix(),
        "source_file_sha256": source["sha256"], "context": context, "context_text": text,
        "resolved_focus_text": focus, "structural_anchor": anchor,
    }


def expected_line_comparator(role: str, path: Path, number: int, surface: str, occurrence: int, note: str) -> dict[str, Any]:
    text = line(path, number)
    col = nth_column(text, surface, occurrence)
    return {
        "role": role,
        "evidence_role": "german_meaning_authority" if role == "de" else "east_only_comparator_not_native_validated",
        "branch_scope": "meaning_authority" if role == "de" else "east_slavic_only",
        "path": path.as_posix(), "file_sha256": identity(path)["sha256"], "line_1based": number,
        "column_start_scalar_1based": col, "column_end_scalar_exclusive_1based": col + len(surface),
        "surface": surface, "surface_sha256": sha_text(surface), "logical_line_sha256": sha_text(text),
        "context_excerpt": text, "context_excerpt_sha256": sha_text(text), "alignment_note": note,
    }


def expected_existing_comparator(raw: dict[str, Any]) -> dict[str, Any]:
    path = Path(raw["path"])
    text = line(path, raw["line_1based"])
    surface = raw["surface"]
    col = raw["column_scalar_1based"]
    exact(text[col - 1:col - 1 + len(surface)], surface, "fixed v1 comparator span")
    exact(sha_text(text), raw["logical_line_sha256"], "fixed v1 comparator line hash")
    role = "de" if raw["role"] == "german_body" else raw["role"]
    return {
        "role": role,
        "evidence_role": "german_meaning_authority" if role == "de" else "east_only_comparator_not_native_validated",
        "branch_scope": "meaning_authority" if role == "de" else "east_slavic_only",
        "path": path.as_posix(), "file_sha256": raw["file_sha256"], "line_1based": raw["line_1based"],
        "column_start_scalar_1based": col, "column_end_scalar_exclusive_1based": col + len(surface),
        "surface": surface, "surface_sha256": sha_text(surface), "logical_line_sha256": raw["logical_line_sha256"],
        "context_excerpt": raw["context_excerpt"], "context_excerpt_sha256": sha_text(raw["context_excerpt"]),
        "alignment_note": "exact documentary comparator from fixed successor v1; same-information review remains pending",
    }


def replay_effect(record: dict[str, Any]) -> None:
    effect = record["effect_locus"]
    path = Path(effect["path"])
    data = path.read_bytes()
    exact(sha_bytes(data), effect["file_sha256"], f"effect file hash {record['ledger_id']}")
    raw_span = data[effect["start_byte_utf8_0based"]:effect["end_byte_utf8_exclusive_0based"]]
    exact(raw_span.decode("utf-8"), effect["span_text"], f"effect byte span {record['ledger_id']}")
    exact(len(raw_span), effect["byte_length_utf8"], f"effect byte length {record['ledger_id']}")
    exact(len(effect["span_text"]), effect["scalar_length"], f"effect scalar length {record['ledger_id']}")
    start_line = line(path, effect["start_line_1based"])
    end_line = line(path, effect["end_line_1based"])
    exact(sha_text(start_line), effect["start_line_sha256"], "effect start-line hash")
    exact(sha_text(end_line), effect["end_line_sha256"], "effect end-line hash")
    require(effect["start_line_1based"] == effect["end_line_1based"], "ALTERED_LOCATOR_OR_HASH", "all 14 bounded effects must be single-line")
    scalar_span = start_line[effect["start_column_scalar_1based"] - 1:effect["end_column_scalar_exclusive_1based"] - 1]
    exact(scalar_span, effect["span_text"], "effect scalar span")
    exact(sha_text(effect["span_text"]), effect["span_sha256"], "effect span hash")
    context = record["context_window"]
    exact(context["line_1based"], effect["start_line_1based"], "context/effect line")
    exact(sha_text(start_line), context["line_text_sha256"], "context line hash")
    exact(len(start_line), context["line_scalar_length"], "context line scalar length")
    window = start_line[context["window_start_column_scalar_1based"] - 1:context["window_end_column_scalar_exclusive_1based"] - 1]
    exact(window, context["window_text"], "context window text")
    exact(sha_text(window), context["window_text_sha256"], "context window hash")


def expected_effect_comparator(record: dict[str, Any]) -> dict[str, Any]:
    replay_effect(record)
    effect = record["effect_locus"]
    return {
        "role": "isv", "evidence_role": "current_editable_latin_baseline_not_official_grammar",
        "branch_scope": "constructed_interslavic_baseline", "path": Path(effect["path"]).as_posix(),
        "file_sha256": effect["file_sha256"], "line_1based": effect["start_line_1based"],
        "column_start_scalar_1based": effect["start_column_scalar_1based"],
        "column_end_scalar_exclusive_1based": effect["end_column_scalar_exclusive_1based"],
        "surface": effect["span_text"], "surface_sha256": effect["span_sha256"],
        "logical_line_sha256": effect["start_line_sha256"], "context_excerpt": record["context_window"]["window_text"],
        "context_excerpt_sha256": record["context_window"]["window_text_sha256"],
        "alignment_note": "exact current Latin effect locus; not official grammar, native review, or independent branch evidence",
    }


def expected_comparators(record: dict[str, Any]) -> list[dict[str, Any]]:
    ledger_id = record["ledger_id"]
    if record["family_or_route"] in {"lexeme:simultaneous", "lexeme:step"}:
        return [expected_existing_comparator(row) for row in record["comparison_locators"]] + [expected_effect_comparator(record)]
    if ledger_id in NOETHER:
        de, ru, uk = NOETHER[ledger_id]
        ru_path, uk_path = (BIB_RU, BIB_UK) if ledger_id == "SLISV-SUCC-IN-0078" else (P45_RU, P45_UK)
        note = "exact policy comparator; same-information and preferred Interslavic name treatment remain pending qualified review"
        return [
            expected_line_comparator("de", DE, *de, note), expected_line_comparator("ru", ru_path, *ru, note),
            expected_line_comparator("uk", uk_path, *uk, note), expected_effect_comparator(record),
        ]
    require(ledger_id == "SLISV-SUCC-IN-0080", "TARGET_SET", f"unexpected target {ledger_id}")
    note = "exact same-topic comparator; proposed Interslavic recast remains model-authored and unreviewed"
    return [
        expected_line_comparator("de", DE, 8612, "Weierstraßsche Parameterdarstellung", 1, note),
        expected_line_comparator("ru", BASE_RU, 9297, "параметрическое представление Вейерштрасса", 1, note),
        expected_line_comparator("uk", BASE_UK, 9258, "параметричне подання Вейєрштрасса", 1, note),
        expected_effect_comparator(record),
    ]


def expected_alternatives(items: list[dict[str, Any]]) -> list[dict[str, str]]:
    return [{
        "label": str(item.get("label", item.get("option", ""))),
        "state": str(item.get("state", "unspecified")),
        "basis_or_reason": str(item.get("basis_or_reason", item.get("reason", ""))),
    } for item in items]


def validate_security_boundaries(packet: dict[str, Any]) -> None:
    claims = packet.get("claims", {})
    fake_keys = ["approved", "jan_contacted", "jan_has_seen_packet", "community_contacted", "native_review_received", "canonical_claim"]
    if any(claims.get(key) is not False for key in fake_keys):
        raise ValidationFailure("FAKE_APPROVAL", "approval, native/community contact, Jan, and canonical claims must all remain false")
    application_keys = ["application_authorized", "reader_mutation_authorized", "release_ready", "publication_ready"]
    if any(claims.get(key) is not False for key in application_keys):
        raise ValidationFailure("APPLICATION_OR_RELEASE_CLAIM", "application/release/publication claims must remain false")
    require(claims.get("west_arms_complete") is False and claims.get("south_arms_complete") is False and claims.get("intelligibility_measured") is False, "FAKE_APPROVAL", "coverage/intelligibility claims must remain false")
    morph = packet.get("morphology_requests", [])
    require(len(morph) == 5, "TARGET_SET", "exactly five morphology requests required")
    for request in morph:
        arms = request.get("required_arms", [])
        if len(arms) != 2:
            raise ValidationFailure("MISSING_REQUIRED_ARMS", "each morphology request requires two explicit null arm slots")
        branches = [arm.get("macrobranch") for arm in arms]
        if branches != ["west", "south"]:
            raise ValidationFailure("BRANCH_MERGING", "West and South arms must remain distinct and ordered")
        for arm in arms:
            if arm.get("state") != "missing_not_authored" or any(arm.get(key) is not None for key in ["authored_whole_sentence", "author_identity", "author_native_language", "source_evidence"]):
                raise ValidationFailure("MODEL_FILLED_ARM", "v001 arm slots must remain null and unauthored")
        surfaces = request.get("evidence_surfaces", {})
        for lang in ["ru", "uk"]:
            if surfaces.get(lang, {}).get("branch_scope") != "east_slavic_only":
                raise ValidationFailure("EAST_AS_PAN_SLAVIC", f"{lang} evidence must remain East-only")
    norm = packet.get("normalization_requests", [])
    require(len(norm) == 14, "TARGET_SET", "exactly fourteen normalization contexts required")
    for request in norm:
        if any(value is not None for value in request.get("response_slots", {}).values()) or request.get("primary_question", {}).get("response") is not None:
            raise ValidationFailure("FAKE_APPROVAL", "v001 contains no attributable response")
        for surface in request.get("comparison_surfaces", []):
            if surface.get("role") in {"ru", "uk"} and surface.get("branch_scope") != "east_slavic_only":
                raise ValidationFailure("EAST_AS_PAN_SLAVIC", "RU/UK normalization comparisons remain East-only")


def validate_morphology(packet: dict[str, Any], morph: dict[str, Any]) -> None:
    sources = {row["source_id"]: row for row in morph["source_pins"]}
    grammar = {row["rule_id"]: row for row in morph["grammar_rules"]}
    expected_ids = [row["locus_id"] for row in morph["loci"]]
    exact([row["source_locus_id"] for row in packet["morphology_requests"]], expected_ids, "morphology locus sequence", "TARGET_SET")
    for ordinal, (actual, locus) in enumerate(zip(packet["morphology_requests"], morph["loci"]), 1):
        exact(actual["request_id"], f"CRP-MORPH-{ordinal:02d}", "morph request id", "TARGET_SET")
        exact(actual["paper_id"], locus["paper_id"], "morph paper")
        exact(actual["locus_role"], locus["locus_role"], "morph role")
        focus = {
            "phenomenon": locus["parent_pin"]["phenomenon"],
            "contrast_class": locus["contrast_requirement"]["contrast_class"],
            "exact_coherent_contrast_required": locus["contrast_requirement"]["exact_coherent_contrast_required"],
            "preserve": locus["contrast_requirement"]["preserve"],
            "prohibited": locus["contrast_requirement"]["prohibited"],
        }
        exact(actual["semantic_focus"], focus, "morph semantic focus")
        exact(actual["coverage"], locus["coverage"], "morph coverage")
        exact(actual["adverse_evidence"], locus["adverse_evidence"], "morph adverse evidence")
        expected_rules = [grammar[rule_id] for rule_id in locus["grammar_rule_ids"]]
        exact(actual["grammar_constraints"], expected_rules, "grammar-rule bindings")
        for lang in ["de", "ru", "uk", "isv"]:
            raw = locus["surfaces"][lang]
            expected = expected_morph_surface(raw, sources[raw["source_id"]])
            exact(actual["evidence_surfaces"][lang], expected, f"morph surface {locus['locus_id']} {lang}")
        exact(actual["source_record_semantic_sha256"], canonical_sha(locus), "morph source semantic hash")
        exact([q["question_id"] for q in actual["questions"]], [f"CRP-MORPH-{ordinal:02d}-Q-WEST", f"CRP-MORPH-{ordinal:02d}-Q-SOUTH", f"CRP-MORPH-{ordinal:02d}-Q-GRAMMAR"], "morph question IDs")
        require(all(q["response"] is None for q in actual["questions"]), "FAKE_APPROVAL", "morph responses must be null")
        exact(actual["application_state"], "no_application_no_release_no_claim", "morph application boundary", "APPLICATION_OR_RELEASE_CLAIM")


def normalization_group(record: dict[str, Any]) -> tuple[str, dict[str, str]]:
    if record["family_or_route"] == "lexeme:simultaneous":
        return "simultaneity", record["sense_and_morphology"]
    if record["family_or_route"] == "lexeme:step":
        return "korak_step", record["sense_and_morphology"]
    if record["ledger_id"] == "SLISV-SUCC-IN-0080":
        return "weierstrass_recast", {"mathematical_or_prose_sense": "Weierstrass-type parametric representation in a complete mathematical sentence", "part_of_speech": "inflected eponym versus exact-name construction", "inflection_or_features": "whole-surface syntax must be grammatical and script-safe", "classification": "model-authored recast pending competent grammar review"}
    return "noether_neter", {"mathematical_or_prose_sense": "morphologically integrated Noether eponym or running-name surface; citation spellings remain exact", "part_of_speech": "proper-name/eponym surface with Interslavic inflection", "inflection_or_features": "review the complete surface, not a protected stem plus projected suffix", "classification": "editorial Neter proposal pending competent native/community review"}


def validate_normalization(packet: dict[str, Any], successor: dict[str, Any]) -> None:
    by_id = {row["ledger_id"]: row for row in successor["records"]}
    exact([row["source_ledger_id"] for row in packet["normalization_requests"]], TARGET_LEDGER_IDS, "normalization target sequence", "TARGET_SET")
    groups = []
    for ordinal, (actual, ledger_id) in enumerate(zip(packet["normalization_requests"], TARGET_LEDGER_IDS), 1):
        record = by_id[ledger_id]
        group, focus = normalization_group(record)
        groups.append(group)
        proposal = record["proposal"]
        exact(actual["request_id"], f"CRP-NORM-{ordinal:02d}", "normalization request id", "TARGET_SET")
        exact(actual["choice_group"], group, "normalization choice group", "TARGET_SET")
        exact(actual["upstream_id"], record["upstream_id"], "normalization upstream ID")
        exact(actual["effect_locus"], record["effect_locus"], "normalization effect")
        exact(actual["context_window"], record["context_window"], "normalization context")
        exact(actual["comparison_surfaces"], expected_comparators(record), "normalization exact comparison surfaces")
        exact([surface["role"] for surface in actual["comparison_surfaces"]], ["de", "ru", "uk", "isv"], "comparison role order")
        exact(actual["semantic_focus"], focus, "normalization semantic focus")
        exact(actual["current_surface"], proposal["current_text"], "normalization current surface")
        exact(actual["candidate_latin_surface"], proposal["candidate_latin_text"], "normalization candidate Latin")
        exact(actual["candidate_cyrillic_surface"], proposal["candidate_cyrillic_text"], "normalization candidate Cyrillic")
        exact(actual["alternatives"], expected_alternatives(proposal["alternatives"]), "normalization alternatives")
        exact(actual["adverse_evidence"], [item["text"] for item in proposal["adverse_evidence"]], "normalization adverse evidence")
        exact(actual["evidence_facts"], [item["text"] for item in proposal["evidence_facts"]], "normalization evidence facts")
        expected_question = f"For exact context {record['upstream_id']} ({proposal['current_text']}), {proposal['review_question']}"
        exact(actual["primary_question"], {"question_id": f"CRP-NORM-{ordinal:02d}-Q-CONTEXT", "question": expected_question, "response": None}, "per-context review question")
        exact(actual["required_reviewer_profiles"], ["RP-WEST-AUTHOR", "RP-SOUTH-AUTHOR", "RP-INDEPENDENT-GRAMMAR", "RP-COMMUNITY-GOVERNANCE"], "normalization reviewer profiles")
        exact(actual["source_record_semantic_sha256"], record["record_semantic_sha256"], "normalization semantic hash")
        exact(actual["application_state"], "no_application_no_release_no_claim", "normalization application boundary", "APPLICATION_OR_RELEASE_CLAIM")
    exact({name: groups.count(name) for name in set(groups)}, {"simultaneity": 5, "korak_step": 1, "noether_neter": 7, "weierstrass_recast": 1}, "normalization group counts", "TARGET_SET")


def expected_authority_captures(authority: dict[str, Any]) -> list[dict[str, Any]]:
    root = Path(INPUTS["IN-AUTHORITY-MANIFEST"][0]).parent
    rows = []
    for capture in authority["captures"]:
        if capture["authority_id"] not in {"ISV-AUTH-002", "ISV-AUTH-003", "ISV-AUTH-004"} or capture["capture_mode"] != "exact_local_bytes":
            continue
        path = root / capture["local_path"]
        actual = identity(path)
        exact((actual["bytes"], actual["sha256"]), (capture["bytes"], capture["sha256"]), f"authority capture {capture['entry_id']}", "INPUT_DRIFT")
        rows.append({"capture_id": capture["entry_id"], "authority_id": capture["authority_id"], "path": path.as_posix(), "bytes": capture["bytes"], "sha256": capture["sha256"], "disposition": capture["disposition"], "claim_boundary": capture["claim_boundary"]})
    return rows


def expected_source_pins(packet: dict[str, Any]) -> list[dict[str, Any]]:
    roles: dict[str, set[str]] = {}
    for request in packet["morphology_requests"]:
        for lang, surface in request["evidence_surfaces"].items():
            roles.setdefault(surface["source_path"], set()).add(f"morphology_{lang}")
    for request in packet["normalization_requests"]:
        for surface in request["comparison_surfaces"]:
            roles.setdefault(surface["path"], set()).add(f"normalization_{surface['role']}")
    return [{**identity(Path(path)), "roles": sorted(values)} for path, values in sorted(roles.items())]


def validate_authority(packet: dict[str, Any], authority: dict[str, Any]) -> None:
    exact(packet["governance_boundaries"], GOVERNANCE, "decision authority boundaries", "AUTHORITY_BOUNDARY")
    by_role = {row["role"]: row for row in authority["authorities"]}
    expected_context = {
        "snapshot_id": authority["snapshot_id"], "snapshot_status": authority["status"],
        "snapshot_review_state": authority["supersession"]["review_state"],
        "design_voting_boundary": by_role["design_voting"]["claim_boundary"],
        "historical_voting_machine_boundary": "A historical Interslavic Voting Machine is documented as statistical design/governance background; this packet does not reconstruct an exact current algorithm or coefficient table and does not infer community approval.",
        "grammar_boundary": by_role["grammar"]["claim_boundary"], "orthography_boundary": by_role["orthography"]["claim_boundary"],
        "human_validation_boundary": "absent_no_response_no_native_certification_no_community_vote_no_Jan_return",
    }
    exact(packet["authority_context"], expected_context, "official authority boundary", "AUTHORITY_BOUNDARY")
    exact(packet["authority_capture_pins"], expected_authority_captures(authority), "official capture pins")
    exact(packet["source_file_pins"], expected_source_pins(packet), "source file pins")


def validate_profiles(packet: dict[str, Any]) -> None:
    profiles = packet["reviewer_qualification_profiles"]
    exact([row["profile_id"] for row in profiles], ["RP-WEST-AUTHOR", "RP-SOUTH-AUTHOR", "RP-INDEPENDENT-GRAMMAR", "RP-COMMUNITY-GOVERNANCE"], "reviewer profiles", "QUALIFICATION")
    exact([row["macrobranch"] for row in profiles], ["west", "south", None, None], "reviewer profile branches", "QUALIFICATION")
    combined = json.dumps(profiles, ensure_ascii=False)
    for phrase in ["native/dominant Slavic language", "whole sentence", "independent", "identity", "conflicts", "silence", "Jan van Steenbergen"]:
        require(phrase in combined, "QUALIFICATION", f"qualification contract missing {phrase!r}")


def validate_packet(packet: dict[str, Any], schema: dict[str, Any], morph: dict[str, Any], successor: dict[str, Any], authority: dict[str, Any], input_pins: list[dict[str, Any]], run_schema: bool = True) -> None:
    validate_security_boundaries(packet)
    exact(packet.get("input_pins"), input_pins, "input pins", "INPUT_DRIFT")
    exact(packet.get("counts"), {"review_units": 19, "morphology_units": 5, "normalization_units": 14, "simultaneity": 5, "korak": 1, "noether_neter": 7, "weierstrass": 1, "west_authored_arms": 0, "south_authored_arms": 0, "review_responses": 0, "approvals": 0, "application_claims": 0}, "closed review-unit counts", "TARGET_SET")
    validate_morphology(packet, morph)
    validate_normalization(packet, successor)
    validate_authority(packet, authority)
    validate_profiles(packet)
    if run_schema:
        Draft202012Validator.check_schema(schema)
        errors = sorted(Draft202012Validator(schema).iter_errors(packet), key=lambda item: list(item.absolute_path))
        require(not errors, "SCHEMA", errors[0].message if errors else "schema failure")


def locator(surface: dict[str, Any]) -> str:
    if "source_path" in surface:
        context = surface["context"]
        return f"{surface['source_path']}:{context['line_start']}-{context['line_end']}#{context['sha256_utf8_lf']}"
    return f"{surface['path']}:{surface['line_1based']}:{surface['column_start_scalar_1based']}-{surface['column_end_scalar_exclusive_1based']}#{surface['logical_line_sha256']}"


def expected_csv(packet: dict[str, Any]) -> str:
    out = io.StringIO(newline="")
    writer = csv.DictWriter(out, fieldnames=CSV_FIELDS, lineterminator="\n")
    writer.writeheader()
    for row in packet["morphology_requests"]:
        surfaces = row["evidence_surfaces"]
        writer.writerow({"request_id": row["request_id"], "request_kind": row["request_kind"], "source_id": row["source_locus_id"], "group_or_role": row["locus_role"], "current_surface": surfaces["isv"]["controlled_occurrence"], "candidate_latin_surface": "", "de_locator": locator(surfaces["de"]), "ru_locator": locator(surfaces["ru"]), "uk_locator": locator(surfaces["uk"]), "isv_locator": locator(surfaces["isv"]), "required_reviewers": "RP-WEST-AUTHOR|RP-SOUTH-AUTHOR|RP-INDEPENDENT-GRAMMAR", "state": row["review_state"], "primary_question": row["semantic_focus"]["exact_coherent_contrast_required"]})
    for row in packet["normalization_requests"]:
        surfaces = {surface["role"]: surface for surface in row["comparison_surfaces"]}
        writer.writerow({"request_id": row["request_id"], "request_kind": row["request_kind"], "source_id": row["source_ledger_id"], "group_or_role": row["choice_group"], "current_surface": row["current_surface"], "candidate_latin_surface": row["candidate_latin_surface"] or "", "de_locator": locator(surfaces["de"]), "ru_locator": locator(surfaces["ru"]), "uk_locator": locator(surfaces["uk"]), "isv_locator": locator(surfaces["isv"]), "required_reviewers": "|".join(row["required_reviewer_profiles"]), "state": row["review_state"], "primary_question": row["primary_question"]["question"]})
    return out.getvalue()


def expected_markdown(packet: dict[str, Any]) -> str:
    lines = [
        "# Interslavic Noether pilot — bounded review solicitation v001", "",
        "> **NON-APPROVED / NOT SENT.** This packet contains no West or South authored arm, no native or community return, no participant result, and no application or release authority. Jan van Steenbergen has not been contacted and is not claimed to have seen this packet.", "",
        "Return any review as a separate, dated, attributable artifact. State your native/dominant language, relevant competence, role, conflicts, and whether you speak only for yourself or for a named body. Do not edit this immutable v001 packet.", "", "## Reviewer qualification profiles", "",
    ]
    for profile in packet["reviewer_qualification_profiles"]:
        lines += [f"### {profile['profile_id']} — {profile['role']}", "", "Required: " + "; ".join(profile["minimum_qualifications"]) + ".", "", "Not sufficient: " + "; ".join(profile["not_sufficient"]) + ".", ""]
    lines += ["## A. Five morphology/morphosyntax loci", ""]
    for row in packet["morphology_requests"]:
        lines += [f"### {row['request_id']} — {row['source_locus_id']} ({row['paper_id']})", "", f"**Focus:** {row['semantic_focus']['phenomenon']}", "", f"**Required coherent contrast:** {row['semantic_focus']['exact_coherent_contrast_required']}", ""]
        for lang in ["de", "ru", "uk", "isv"]:
            surface = row["evidence_surfaces"][lang]
            lines += [f"- **{lang.upper()}** `{locator(surface)}` — `{surface['controlled_occurrence']}` — role `{surface['evidence_role']}`", "", "```text", surface["context_text"], "```", ""]
        lines += ["West authored arm: **MISSING / NULL**", "", "South authored arm: **MISSING / NULL**", ""]
        for question in row["questions"]:
            lines += [f"- `{question['question_id']}` ({question['reviewer_profile_id']}): {question['question']}"]
        lines += ["", "No response is recorded in v001.", ""]
    lines += ["## B. Fourteen normalization contexts", ""]
    for row in packet["normalization_requests"]:
        lines += [f"### {row['request_id']} — {row['source_ledger_id']} / {row['upstream_id']} ({row['choice_group']})", "", f"**Current:** `{row['current_surface']}`", "", f"**Candidate Latin:** `{row['candidate_latin_surface']}`", "", f"**Question:** {row['primary_question']['question']}", ""]
        for surface in row["comparison_surfaces"]:
            lines += [f"- **{surface['role'].upper()}** `{locator(surface)}` — `{surface['surface']}` — {surface['alignment_note']}"]
        lines += ["", "**Context:**", "", "```text", row["context_window"]["window_text"], "```", "", "**Alternatives/adverse evidence:**"]
        for item in row["alternatives"]:
            lines += [f"- {item['label']} — {item['state']}: {item['basis_or_reason']}"]
        for item in row["adverse_evidence"]:
            lines += [f"- Adverse: {item}"]
        lines += ["", "West review: **NULL**; South review: **NULL**; independent grammar review: **NULL**; community comment: **NULL**.", ""]
    lines += ["## Return boundary", "", "A returned review can be evidence only after identity, qualification, exact request IDs, source hashes, independence, conflicts, and response custody are verified. Silence is not approval. A response does not itself authorize reader edits, release, publication, or an intelligibility claim.", ""]
    return "\n".join(lines)


def apply_pointer(document: Any, operation: dict[str, Any]) -> None:
    tokens = [token.replace("~1", "/").replace("~0", "~") for token in operation["path"].split("/")[1:]]
    target = document
    for token in tokens[:-1]:
        target = target[int(token)] if isinstance(target, list) else target[token]
    final = tokens[-1]
    if operation["op"] == "replace":
        if isinstance(target, list):
            target[int(final)] = operation["value"]
        else:
            require(final in target, "FIXTURE_DEFINITION", f"replace target absent: {operation['path']}")
            target[final] = operation["value"]
    elif operation["op"] == "remove":
        if isinstance(target, list):
            del target[int(final)]
        else:
            require(final in target, "FIXTURE_DEFINITION", f"remove target absent: {operation['path']}")
            del target[final]
    else:
        raise ValidationFailure("FIXTURE_DEFINITION", f"unsupported fixture operation {operation['op']}")


def validate_fixtures(fixtures: dict[str, Any], packet: dict[str, Any], schema: dict[str, Any], morph: dict[str, Any], successor: dict[str, Any], authority: dict[str, Any], pins: list[dict[str, Any]]) -> list[dict[str, str]]:
    expected_ids = ["fake_approval_and_Jan_claim", "fake_native_approval_return", "model_filled_west_arm", "missing_required_south_arm", "merged_west_south_branch", "east_promoted_to_pan_slavic", "altered_exact_locator", "altered_context_hash", "application_and_release_claim"]
    exact(fixtures.get("fixture_set_id"), "ISV-MI-COMMUNITY-REVIEW-PACKET-v001-HOSTILE", "fixture set", "FIXTURE_DEFINITION")
    exact([row.get("fixture_id") for row in fixtures.get("fixtures", [])], expected_ids, "fixture IDs", "FIXTURE_DEFINITION")
    results = []
    for fixture in fixtures["fixtures"]:
        mutated = copy.deepcopy(packet)
        for operation in fixture["operations"]:
            apply_pointer(mutated, operation)
        try:
            validate_packet(mutated, schema, morph, successor, authority, pins, run_schema=False)
        except ValidationFailure as exc:
            exact(exc.code, fixture["expected_error"], f"fixture outcome {fixture['fixture_id']}", "FIXTURE_FALSE_PASS")
            results.append({"fixture_id": fixture["fixture_id"], "result": "REJECT", "error_code": exc.code})
        else:
            raise ValidationFailure("FIXTURE_FALSE_PASS", f"hostile fixture falsely accepted: {fixture['fixture_id']}")
    return results


def validate_manifest(manifest: dict[str, Any], packet: dict[str, Any]) -> None:
    roles = {
        PACKAGE: "canonical_packet", SCHEMA: "draft_2020_12_schema", CSV_PATH: "review_projection",
        REVIEWER_MD: "human_reviewer_projection", FIXTURES: "hostile_fixture_definitions",
        BUILDER: "deterministic_builder", VALIDATOR: "independent_no_write_validator",
    }
    generated = [{**identity(path), "role": roles[path]} for path in [PACKAGE, SCHEMA, CSV_PATH, REVIEWER_MD, FIXTURES, BUILDER, VALIDATOR]]
    expected = {
        "manifest_id": "ISV-MI-COMMUNITY-REVIEW-PACKET-v001-MANIFEST", "packet_id": packet["packet_id"], "status": packet["status"],
        "generated_artifacts": generated, "source_inputs": packet["input_pins"], "counts": packet["counts"], "claims": packet["claims"],
        "self_identity_policy": "manifest does not contain its own byte identity to avoid circular self-reference",
        "receipt_policy": "validation receipt binds this manifest and all seven generated artifacts; receipt does not contain its own identity",
        "validation_receipt_path": RECEIPT.as_posix(), "next_cursor": packet["next_cursor"],
    }
    exact(manifest, expected, "artifact manifest", "MANIFEST")


def validate_projections(packet: dict[str, Any]) -> None:
    csv_data = CSV_PATH.read_bytes()
    md_data = REVIEWER_MD.read_bytes()
    for path, data in [(CSV_PATH, csv_data), (REVIEWER_MD, md_data)]:
        require(not data.startswith(b"\xef\xbb\xbf") and b"\r" not in data and data.endswith(b"\n"), "TRANSPORT", f"projection transport: {path}")
    exact(csv_data.decode("utf-8"), expected_csv(packet), "CSV projection", "PROJECTION")
    exact(md_data.decode("utf-8"), expected_markdown(packet), "reviewer Markdown projection", "PROJECTION")
    parsed = list(csv.DictReader(io.StringIO(csv_data.decode("utf-8"))))
    exact(len(parsed), 19, "CSV row count", "PROJECTION")
    exact([row["request_id"] for row in parsed], [f"CRP-MORPH-{i:02d}" for i in range(1, 6)] + [f"CRP-NORM-{i:02d}" for i in range(1, 15)], "CSV request sequence", "PROJECTION")


ARTIFACT_ROLES = {
    PACKAGE: "canonical_packet", SCHEMA: "draft_2020_12_schema", CSV_PATH: "review_projection",
    REVIEWER_MD: "human_reviewer_projection", FIXTURES: "hostile_fixture_definitions",
    MANIFEST: "artifact_manifest", BUILDER: "deterministic_builder", VALIDATOR: "independent_no_write_validator",
}


CHECKS = [
    "strict_utf8_json_transport_and_duplicate_key_rejection", "draft_2020_12_schema_meta_validation",
    "draft_2020_12_instance_validation", "seventeen_exact_read_only_input_pins",
    "five_exact_morphology_locus_replays", "twenty_morphology_surface_context_hash_replays",
    "structural_anchor_replays", "official_grammar_rule_bindings", "zero_west_and_zero_south_authored_arms",
    "fourteen_exact_normalization_context_replays", "fifty_six_normalization_comparator_replays",
    "five_simultaneity_one_korak_seven_noether_one_weierstrass_partition", "east_only_scope_enforcement",
    "official_authority_capture_replay", "decision_and_application_authority_boundaries",
    "reviewer_qualification_and_independence_contract", "nineteen_row_csv_projection_replay",
    "human_reviewer_markdown_projection_replay", "manifest_identity_replay", "nine_hostile_fixture_rejections",
    "deterministic_receipt_basis",
]


def build_receipt(packet: dict[str, Any], pins: list[dict[str, Any]], fixture_results: list[dict[str, str]]) -> dict[str, Any]:
    artifacts = [{**identity(path), "role": ARTIFACT_ROLES[path]} for path in [PACKAGE, SCHEMA, CSV_PATH, REVIEWER_MD, FIXTURES, MANIFEST, BUILDER, VALIDATOR]]
    basis = {"artifacts": artifacts, "inputs": pins, "counts": packet["counts"], "claims": packet["claims"], "fixtures": fixture_results, "checks": CHECKS}
    return {
        "schema_id": "ISV-MI-COMMUNITY-REVIEW-PACKET-VALIDATION-v001",
        "receipt_id": "ISV-MI-COMMUNITY-REVIEW-PACKET-20260811-v001-VALIDATION",
        "packet_id": packet["packet_id"], "status": "PASS", "validator_mode": "independent_no_write",
        "writes_performed": False, "network_contact_performed": False, "publication_performed": False,
        "validated_artifacts": artifacts, "source_input_count": len(pins), "source_input_pins_sha256": canonical_sha(pins),
        "review_unit_counts": packet["counts"], "claims": packet["claims"], "checks": CHECKS,
        "hostile_fixtures": {"total": len(fixture_results), "rejected_as_expected": len(fixture_results), "results": fixture_results},
        "determinism": {"basis_sha256": canonical_sha(basis), "receipt_contains_no_clock_or_random_value": True, "receipt_excludes_own_identity": True},
        "limitations": ["PASS validates custody, exact bindings, empty response slots, projections, and fail-closed semantics only.", "PASS is not native/community approval, a claim that Jan has seen the packet, measured intelligibility, application authority, release authority, or publication authority."],
        "next_cursor": packet["next_cursor"],
    }


def run() -> tuple[dict[str, Any], dict[str, Any]]:
    require(ROOT == EXPECTED_ROOT, "CUSTODY", "validator must run from exact packet custody")
    packet = load_json(PACKAGE, enforce_transport=True)
    schema = load_json(SCHEMA, enforce_transport=True)
    fixtures = load_json(FIXTURES, enforce_transport=True)
    manifest = load_json(MANIFEST, enforce_transport=True)
    pins = expected_inputs()
    morph = load_json(Path(INPUTS["IN-MORPH-PACKAGE"][0]))
    successor = load_json(Path(INPUTS["IN-SUCCESSOR-V1"][0]))
    authority = load_json(Path(INPUTS["IN-AUTHORITY-MANIFEST"][0]))
    validate_packet(packet, schema, morph, successor, authority, pins, run_schema=True)
    validate_projections(packet)
    validate_manifest(manifest, packet)
    fixture_results = validate_fixtures(fixtures, packet, schema, morph, successor, authority, pins)
    receipt = build_receipt(packet, pins, fixture_results)
    exact(receipt, build_receipt(packet, pins, fixture_results), "deterministic receipt replay", "DETERMINISM")
    return packet, receipt


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--emit-receipt", action="store_true", help="print deterministic receipt JSON to stdout")
    parser.add_argument("--check-receipt", action="store_true", help="compare stored receipt with deterministic reconstruction")
    parser.add_argument("--compact", action="store_true", help="print one compact PASS line")
    args = parser.parse_args()
    try:
        _, receipt = run()
        if args.check_receipt:
            stored = load_json(RECEIPT, enforce_transport=True)
            exact(stored, receipt, "stored deterministic receipt", "RECEIPT_DRIFT")
        if args.emit_receipt:
            sys.stdout.write(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")
        elif args.compact or not args.check_receipt:
            sys.stdout.write(f"PASS review_units=19 morphology=5 normalization=14 fixtures={receipt['hostile_fixtures']['rejected_as_expected']}/{receipt['hostile_fixtures']['total']} receipt_check={'PASS' if args.check_receipt else 'NOT_REQUESTED'}\n")
        else:
            sys.stdout.write("PASS receipt_check=PASS\n")
        return 0
    except (ValidationFailure, KeyError, IndexError, TypeError, OSError) as exc:
        code = exc.code if isinstance(exc, ValidationFailure) else "STRUCTURE_OR_IO"
        sys.stderr.write(f"FAIL {code}: {exc}\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
