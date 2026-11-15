#!/usr/bin/env python3
"""Independent, no-write validator for ISV_MI_ITEM_BINDING.json."""

from __future__ import annotations

import copy
import csv
import hashlib
import json
import re
import sys
from pathlib import Path

from jsonschema import Draft202012Validator


HERE = Path(__file__).resolve().parent
PACKAGE_PATH = HERE / "ISV_MI_ITEM_BINDING.json"
SCHEMA_PATH = HERE / "ISV_MI_ITEM_BINDING.schema.json"
CSV_PATH = HERE / "ISV_MI_ITEM_BINDING.csv"
BUILDER_PATH = HERE / "build_isv_mi_item_binding.py"


class ValidationFailure(RuntimeError):
    pass


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest().upper()


def sha_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest().upper()


def fail(message: str) -> None:
    raise ValidationFailure(message)


def walk_keys(value, path="$"):
    if isinstance(value, dict):
        for key, child in value.items():
            yield path, key, child
            yield from walk_keys(child, f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk_keys(child, f"{path}[{index}]")


def validate(package: dict, schema: dict, *, verify_files: bool = True) -> dict:
    errors = sorted(Draft202012Validator(schema).iter_errors(package), key=lambda error: list(error.path))
    if errors:
        first = errors[0]
        fail(f"schema: {'/'.join(map(str, first.path))}: {first.message}")

    if package["status"] != "candidate_binding_preregistration_input_only":
        fail("status promotion is forbidden")
    claims = package["claims"]
    if claims != {
        "participant_ready": False,
        "human_response_records": 0,
        "qualified_native_review_records": 0,
        "community_approval": False,
        "certification": False,
        "publication_status": "not_a_publication_payload",
    }:
        fail("fabricated readiness/validation/publication claim")

    pins = package["source_pins"]
    source_ids = [pin["source_id"] for pin in pins]
    if len(source_ids) != len(set(source_ids)):
        fail("duplicate source IDs")
    required_sources = {
        "SRC-PROTOCOL", "SRC-TREE", "SRC-TYPED-GRAPH", "SRC-R823-TERM", "SRC-FABLE-R1",
        "SRC-FABLE-TABLE", "SRC-FABLE-BRANCH", "SRC-F10", "SRC-RETROFIT", "SRC-CONCEPT-WEB",
        "SRC-FABLE-LOGBOOK", "SRC-OFFICIAL-ISV", "SRC-V018-BASE", "SRC-GERMAN-ED0011",
        "SRC-ASSEMBLY", "SRC-NORM-CROSSWALK", "SRC-NORM-AUDIT", "SRC-CHANGE-LEX",
        "SRC-CHANGE-CORR", "SRC-CHANGE-SIM", "SRC-RING-REVIEW",
    }
    if not required_sources.issubset(set(source_ids)):
        fail(f"required source omission: {sorted(required_sources - set(source_ids))}")
    pin_by_id = {pin["source_id"]: pin for pin in pins}
    if verify_files:
        for pin in pins:
            path = Path(pin["absolute_path"])
            if not path.is_file():
                fail(f"pinned source absent: {path}")
            if path.stat().st_size != pin["bytes"]:
                fail(f"pinned size mismatch: {pin['source_id']}")
            if sha256(path) != pin["sha256"]:
                fail(f"pinned hash mismatch: {pin['source_id']}")

    evidence = package["evidence_registry"]
    evidence_ids = [record["evidence_id"] for record in evidence]
    if len(evidence_ids) != len(set(evidence_ids)):
        fail("duplicate evidence IDs")
    evidence_by_id = {record["evidence_id"]: record for record in evidence}
    for record in evidence:
        if record["edge_type"] not in {"support", "competitor", "adverse", "absence", "veto"}:
            fail(f"bad evidence edge {record['evidence_id']}")
        for source_id in record["source_ids"]:
            if source_id not in pin_by_id:
                fail(f"unresolved evidence source {source_id}")

    families = package["families"]
    expected_ids = [f"MI-FAM-{number:02d}" for number in range(1, 13)]
    if [family["family_id"] for family in families] != expected_ids:
        fail("family IDs/order do not match frozen 12-family protocol")
    protocol_path = Path(pin_by_id["SRC-PROTOCOL"]["absolute_path"])
    protocol = json.loads(protocol_path.read_text(encoding="utf-8"))
    if [row["id"] for row in protocol["decision_family_plan"]["families"]] != expected_ids:
        fail("frozen protocol family frame changed")

    concept_senses = [(family["concept_id"], family["sense_id"]) for family in families]
    if len(concept_senses) != len(set(concept_senses)):
        fail("duplicate concept/sense family")
    if any(not family["sense_id"].strip() for family in families):
        fail("missing controlled sense")

    expected_roles = ["exact_current_v018", "official_isv", "dominant_east_baseline", "branch_balanced_candidate", "native_control"]
    context_count = 0
    held_context_requirements = 0
    for family in families:
        if family["final_choice"] is not None:
            fail(f"final choice invented in {family['family_id']}")
        if family["status"] != "candidate_binding_preregistration_input_only":
            fail(f"family status promoted in {family['family_id']}")
        roles = [arm["role"] for arm in family["arms"]]
        if roles != expected_roles or len(set(roles)) != 5:
            fail(f"missing/duplicate concept arms in {family['family_id']}")
        native = family["arms"][4]
        if native["surface_candidates"] or native["availability"] != "absent_requires_qualified_native_source":
            fail(f"fabricated native control in {family['family_id']}")
        branches = [row["branch"] for row in family["branch_evidence"]]
        if branches != ["east", "west", "south"] or len(set(branches)) != 3:
            fail(f"branch omission/duplication in {family['family_id']}")
        for branch in family["branch_evidence"]:
            if "evidence_ids" not in branch or not branch["evidence_ids"]:
                fail(f"branch evidence omitted in {family['family_id']}")
            for evidence_id in branch["evidence_ids"]:
                if evidence_id not in evidence_by_id:
                    fail(f"unresolved branch evidence {evidence_id}")
        for edge_type in ["support", "competitor", "adverse", "absence", "veto"]:
            ids = family["evidence_edges"].get(edge_type, [])
            if not ids:
                fail(f"{edge_type} evidence omitted in {family['family_id']}")
            for evidence_id in ids:
                record = evidence_by_id.get(evidence_id)
                if not record or record["edge_type"] != edge_type:
                    fail(f"unresolved or mistyped evidence {evidence_id}")
        if family["context_requirement_state"] != "met_at_binding_level":
            held_context_requirements += 1
        for context in family["contexts"]:
            context_count += 1
            target = context["target_locator"]
            source_pin = pin_by_id.get(target["source_id"])
            if not source_pin:
                fail(f"unresolved target source in {context['context_id']}")
            source_lines = Path(source_pin["absolute_path"]).read_text(encoding="utf-8").splitlines()
            line_number = target["line"]
            if not (1 <= line_number <= len(source_lines)):
                fail(f"target line out of range in {context['context_id']}")
            line = source_lines[line_number - 1]
            if sha_text(line) != target["line_sha256_utf8"]:
                fail(f"target line hash mismatch in {context['context_id']}")
            if context["controlled_occurrence_surface"] not in line:
                fail(f"controlled surface absent in {context['context_id']}")
            german = context["german_authority_locator"]
            german_pin = pin_by_id.get(german["source_id"])
            if not german_pin:
                fail(f"unresolved German source in {context['context_id']}")
            german_lines = Path(german_pin["absolute_path"]).read_text(encoding="utf-8").splitlines()
            start, end = german["line_start"], german["line_end"]
            if not (1 <= start <= end <= len(german_lines)):
                fail(f"German range invalid in {context['context_id']}")
            normalized = "\n".join(german_lines[start - 1:end]) + "\n"
            if sha_text(normalized) != german["range_sha256_utf8_lf"]:
                fail(f"German range hash mismatch in {context['context_id']}")
            if "sentence-level German alignment held" not in context["alignment_state"]:
                fail(f"fabricated sentence alignment in {context['context_id']}")

    morphology = package["morphology_scope_audit"]
    if morphology["direct_morphology_or_morphosyntax_contrast_count"] != 0:
        fail("fabricated morphology/morphosyntax contrast count")
    if morphology["families_with_direct_morphology_or_morphosyntax_contrast"]:
        fail("frozen lexical families falsely promoted to morphology contrasts")
    if morphology["lexically_overconcentrated"] is not True or len(morphology["extension_loci"]) < 5:
        fail("lexical overconcentration or bounded morphology-extension loci omitted")
    for locus in morphology["extension_loci"]:
        context = locus["locator"]
        target = context["target_locator"]
        source_pin = pin_by_id.get(target["source_id"])
        if not source_pin:
            fail(f"unresolved morphology target source in {locus['locus_id']}")
        source_lines = Path(source_pin["absolute_path"]).read_text(encoding="utf-8").splitlines()
        line = source_lines[target["line"] - 1]
        if sha_text(line) != target["line_sha256_utf8"] or context["controlled_occurrence_surface"] not in line:
            fail(f"morphology locus target/hash mismatch in {locus['locus_id']}")
        german = context["german_authority_locator"]
        german_pin = pin_by_id.get(german["source_id"])
        german_lines = Path(german_pin["absolute_path"]).read_text(encoding="utf-8").splitlines()
        normalized = "\n".join(german_lines[german["line_start"] - 1:german["line_end"]]) + "\n"
        if sha_text(normalized) != german["range_sha256_utf8_lf"]:
            fail(f"morphology locus German hash mismatch in {locus['locus_id']}")

    forbidden_keys = {"participant_text", "sentence_text", "passage_text", "token_mosaic", "selected", "winner", "community_certified"}
    for path, key, value in walk_keys(package):
        if key in forbidden_keys:
            fail(f"forbidden generated/promotion field {path}.{key}")
    serialized = json.dumps(package, ensure_ascii=False).casefold()
    for phrase in ["native certified", "community certified", "participant-ready", "final winner"]:
        if phrase in serialized:
            fail(f"fabricated readiness phrase: {phrase}")

    controls = package["control_reconciliation"]
    positive = controls["current_v018_positive_control_inventory"]
    if {key: positive[key]["total"] for key in ["jednočas", "odpověd", "krok"]} != {"jednočas": 159, "odpověd": 498, "krok": 44}:
        fail("positive-control exact counts changed")
    residual = controls["exact_current_residual_adverse_evidence"]
    if {key: residual[key]["count"] for key in residual} != {"simultaneous_pre_switch": 5, "correspondence_pre_switch": 18, "step_pre_switch": 1}:
        fail("residual adverse counts changed")
    if "gated_not_applied" not in controls["stale_control_contradiction"]["statement"]:
        fail("stale R823 contradiction erased")

    with CSV_PATH.open("r", encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    if len(rows) != 60:
        fail(f"CSV projection row count {len(rows)} != 60")
    expected_pairs = {(family["family_id"], arm["role"]) for family in families for arm in family["arms"]}
    if {(row["family_id"], row["role"]) for row in rows} != expected_pairs:
        fail("CSV projection does not exactly cover 12x5 family/arm pairs")

    return {
        "family_count": len(families),
        "arm_count": sum(len(family["arms"]) for family in families),
        "context_count": context_count,
        "held_context_requirement_count": held_context_requirements,
        "source_pin_count": len(pins),
        "evidence_record_count": len(evidence),
        "native_control_hold_count": sum(1 for family in families if family["arms"][4]["availability"] == "absent_requires_qualified_native_source"),
        "participant_passage_hold_count": sum(1 for family in families for arm in family["arms"] if "held" in arm["availability"] or "absent" in arm["availability"]),
        "direct_morphology_contrast_count": morphology["direct_morphology_or_morphosyntax_contrast_count"],
        "morphology_extension_locus_count": len(morphology["extension_loci"]),
    }


def hostile_tests(package: dict, schema: dict) -> list[dict]:
    tests = []

    def add(name, mutate):
        fixture = copy.deepcopy(package)
        mutate(fixture)
        rejected = False
        reason = None
        try:
            validate(fixture, schema, verify_files=False)
        except Exception as exc:  # Every hostile mutation must fail closed.
            rejected = True
            reason = type(exc).__name__
        if not rejected:
            fail(f"hostile fixture accepted: {name}")
        tests.append({"fixture": name, "rejected": True, "failure_class": reason})

    add("source_omission", lambda p: p["source_pins"].pop(0))
    add("source_hash_blank", lambda p: p["source_pins"][0].__setitem__("sha256", ""))
    add("sense_omission", lambda p: p["families"][0].pop("sense_id"))
    add("branch_omission", lambda p: p["families"][0]["branch_evidence"].pop())
    add("adverse_omission", lambda p: p["families"][0]["evidence_edges"].__setitem__("adverse", []))
    add("duplicate_arm_role", lambda p: p["families"][0]["arms"][1].__setitem__("role", "exact_current_v018"))
    add("duplicate_concept_sense", lambda p: (p["families"][1].__setitem__("concept_id", p["families"][0]["concept_id"]), p["families"][1].__setitem__("sense_id", p["families"][0]["sense_id"])))
    add("generated_participant_text", lambda p: p["families"][0].__setitem__("participant_text", "fabricated"))
    add("token_mosaic_promotion", lambda p: p.__setitem__("token_mosaic", True))
    add("fabricated_participant_readiness", lambda p: p["claims"].__setitem__("participant_ready", True))
    add("fabricated_native_review", lambda p: p["claims"].__setitem__("qualified_native_review_records", 1))
    add("invented_final_choice", lambda p: p["families"][0].__setitem__("final_choice", "kolco"))
    add("target_line_hash_tamper", lambda p: p["families"][0]["contexts"][0]["target_locator"].__setitem__("line_sha256_utf8", "0" * 64))
    add("controlled_surface_tamper", lambda p: p["families"][0]["contexts"][0].__setitem__("controlled_occurrence_surface", "FABRICATED"))
    add("source_path_tamper", lambda p: p["source_pins"][0].__setitem__("absolute_path", r"C:\absent\fabricated"))
    add("unresolved_evidence", lambda p: p["families"][0]["evidence_edges"]["support"].append("EV-FABRICATED"))
    add("status_promotion", lambda p: p.__setitem__("status", "approved"))
    add("fabricated_morphology_coverage", lambda p: p["morphology_scope_audit"].__setitem__("direct_morphology_or_morphosyntax_contrast_count", 1))
    return tests


def main() -> int:
    package = json.loads(PACKAGE_PATH.read_text(encoding="utf-8"))
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    summary = validate(package, schema, verify_files=True)
    hostile = hostile_tests(package, schema)
    files = []
    for path in [PACKAGE_PATH, SCHEMA_PATH, CSV_PATH, BUILDER_PATH, Path(__file__).resolve()]:
        files.append({"absolute_path": str(path), "bytes": path.stat().st_size, "sha256": sha256(path)})
    receipt = {
        "receipt_id": "ISV-MI-ITEM-BINDING-VALIDATION-v1-20260811",
        "status": "PASS",
        "validator_no_write": True,
        "package_status": package["status"],
        "summary": summary,
        "positive_control_counts": {key: package["control_reconciliation"]["current_v018_positive_control_inventory"][key]["total"] for key in ["jednočas", "odpověd", "krok"]},
        "residual_adverse_counts": {key: value["count"] for key, value in package["control_reconciliation"]["exact_current_residual_adverse_evidence"].items()},
        "hostile_tests": hostile,
        "hostile_rejected": len(hostile),
        "files": files,
        "next_cursor": package["continuation_cursor"],
    }
    print(json.dumps(receipt, ensure_ascii=True, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(json.dumps({"status": "FAIL", "error_type": type(exc).__name__, "error": str(exc)}, ensure_ascii=True, sort_keys=True), file=sys.stderr)
        raise
