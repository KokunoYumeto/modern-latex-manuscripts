#!/usr/bin/env python3
"""Independent read-only validator for the evidence-DAG successor.

Only Python's standard library is used.  This module does not import or execute
the producer.  It re-derives pins, lineage, channel invariants, and topology from
the pinned predecessor and the serialized successor.
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import heapq
import json
import re
import sys
from pathlib import Path, PurePosixPath
from typing import Any


BASE = Path(__file__).resolve().parent
GRAPH = BASE / "TYPED_EVIDENCE_DAG_SUCCESSOR_V001.json"
SCHEMA = BASE / "TYPED_EVIDENCE_DAG_SUCCESSOR_V001.schema.json"
MANIFEST = BASE / "MANIFEST.json"
RECEIPT = BASE / "VALIDATION_RECEIPT.json"
FIXTURE_DIR = BASE / "HOSTILE_FIXTURES"
PRED_REL = "03_projects/noether/03_translation_workspaces/slavic_r823_book_reconciliation_20260717/evidence/TYPED_EVIDENCE_GRAPH.json"
PRED_SHA = "783D9718BAD8FC61198B7A74EF86814B749FE01BD751A396211B0C79822B7F36"
PRED_BYTES = 5348
CHANNELS = ["support", "candidate", "competitor", "adverse", "absence", "veto"]
EXPECTED_EDGE_CHANNELS = [
    "structural", "support", "support", "candidate", "structural", "support", "adverse", "veto",
    "structural", "candidate", "candidate", "candidate", "competitor", "candidate", "veto", "candidate",
    "veto", "structural", "veto", "absence",
]
EXPECTED_NODE_CHANNELS = {
    "old_post44_witness": "support",
    "old_post44_scope_gap": "adverse",
    "concept_ledger": "candidate",
    "retrofit_ledger": "candidate",
    "isv_wordlist": "candidate",
    "fable_held_rows": "veto",
    "fable_tranche002_gate": "veto",
    "surface_kolco": "candidate",
    "surface_prsten": "competitor",
    "missing_branch_rows": "absence",
}


class DuplicateKeyError(ValueError):
    pass


def workspace_root() -> Path:
    for candidate in [BASE, *BASE.parents]:
        if (candidate / "01_methodology" / "research_department").is_dir() and (candidate / "03_projects").is_dir():
            return candidate.resolve()
    raise RuntimeError("workspace root not found")


WORKSPACE = workspace_root()


def reject_duplicate_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(f"duplicate JSON object key: {key}")
        result[key] = value
    return result


def strict_load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=reject_duplicate_pairs)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def canonical_sha256(value: Any) -> str:
    encoded = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest().upper()


def err(code: str, detail: str) -> dict[str, str]:
    return {"code": code, "detail": detail}


def type_matches(value: Any, declared: str) -> bool:
    if declared == "null":
        return value is None
    if declared == "object":
        return isinstance(value, dict)
    if declared == "array":
        return isinstance(value, list)
    if declared == "string":
        return isinstance(value, str)
    if declared == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if declared == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if declared == "boolean":
        return isinstance(value, bool)
    return False


def schema_errors(instance: Any, schema: dict[str, Any], root: dict[str, Any] | None = None,
                  pointer: str = "") -> list[dict[str, str]]:
    """Validate the deliberately used Draft 2020-12 keyword subset."""
    if root is None:
        root = schema
    errors: list[dict[str, str]] = []
    if "$ref" in schema:
        ref = schema["$ref"]
        if not isinstance(ref, str) or not ref.startswith("#/"):
            return [err("SCHEMA_ENGINE", f"{pointer or '/'}: unsupported reference {ref!r}")]
        target: Any = root
        for raw in ref[2:].split("/"):
            target = target[raw.replace("~1", "/").replace("~0", "~")]
        return schema_errors(instance, target, root, pointer)

    declared = schema.get("type")
    if declared is not None:
        types = declared if isinstance(declared, list) else [declared]
        if not any(type_matches(instance, item) for item in types):
            return [err("SCHEMA_INSTANCE", f"{pointer or '/'}: expected type {types}, got {type(instance).__name__}")]
    if "const" in schema and instance != schema["const"]:
        errors.append(err("SCHEMA_INSTANCE", f"{pointer or '/'}: value differs from const"))
    if "enum" in schema and instance not in schema["enum"]:
        errors.append(err("SCHEMA_INSTANCE", f"{pointer or '/'}: value is outside enum"))

    if isinstance(instance, str):
        if len(instance) < schema.get("minLength", 0):
            errors.append(err("SCHEMA_INSTANCE", f"{pointer or '/'}: string is too short"))
        pattern = schema.get("pattern")
        if pattern is not None and re.search(pattern, instance) is None:
            errors.append(err("SCHEMA_INSTANCE", f"{pointer or '/'}: string does not match pattern {pattern}"))
    if isinstance(instance, (int, float)) and not isinstance(instance, bool):
        if "minimum" in schema and instance < schema["minimum"]:
            errors.append(err("SCHEMA_INSTANCE", f"{pointer or '/'}: number is below minimum"))
    if isinstance(instance, list):
        if len(instance) < schema.get("minItems", 0):
            errors.append(err("SCHEMA_INSTANCE", f"{pointer or '/'}: array has too few items"))
        if "maxItems" in schema and len(instance) > schema["maxItems"]:
            errors.append(err("SCHEMA_INSTANCE", f"{pointer or '/'}: array has too many items"))
        if schema.get("uniqueItems"):
            serialized = [json.dumps(item, ensure_ascii=False, sort_keys=True, separators=(",", ":")) for item in instance]
            if len(serialized) != len(set(serialized)):
                errors.append(err("SCHEMA_INSTANCE", f"{pointer or '/'}: array items are not unique"))
        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for index, value in enumerate(instance):
                errors.extend(schema_errors(value, item_schema, root, f"{pointer}/{index}"))
    if isinstance(instance, dict):
        required = schema.get("required", [])
        for key in required:
            if key not in instance:
                errors.append(err("SCHEMA_INSTANCE", f"{pointer or '/'}: missing required property {key}"))
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            for key in instance:
                if key not in properties:
                    errors.append(err("SCHEMA_INSTANCE", f"{pointer or '/'}: unexpected property {key}"))
        for key, child_schema in properties.items():
            if key in instance:
                escaped = key.replace("~", "~0").replace("/", "~1")
                errors.extend(schema_errors(instance[key], child_schema, root, f"{pointer}/{escaped}"))
    return errors


def schema_document_errors(schema: dict[str, Any]) -> list[dict[str, str]]:
    errors: list[dict[str, str]] = []
    if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        errors.append(err("SCHEMA_DOCUMENT", "Schema must declare Draft 2020-12."))
    if schema.get("type") != "object" or schema.get("additionalProperties") is not False:
        errors.append(err("SCHEMA_DOCUMENT", "Root schema must be a closed object."))
    if not isinstance(schema.get("$id"), str) or not schema["$id"].startswith("https://"):
        errors.append(err("SCHEMA_DOCUMENT", "Schema requires a stable HTTPS $id."))
    allowed = {
        "$schema", "$id", "$ref", "$defs", "$comment", "title", "description", "type", "properties", "required",
        "additionalProperties", "items", "minItems", "maxItems", "uniqueItems", "minLength", "pattern", "minimum",
        "const", "enum",
    }

    def walk(value: Any, pointer: str) -> None:
        if isinstance(value, dict):
            for key, child in value.items():
                if pointer != "/properties" and key not in allowed and not pointer.endswith("/properties"):
                    # Property names inside a properties map are data, not keywords.
                    if "/properties/" not in pointer or pointer.count("/properties/") == pointer.count("/properties"):
                        pass
                walk(child, f"{pointer}/{key}")
        elif isinstance(value, list):
            for index, child in enumerate(value):
                walk(child, f"{pointer}/{index}")

    walk(schema, "")
    return errors


def safe_workspace_relative(raw: Any) -> bool:
    if not isinstance(raw, str) or not raw or "\\" in raw:
        return False
    pure = PurePosixPath(raw)
    return not pure.is_absolute() and all(part not in {"", ".", ".."} for part in pure.parts) and pure.parts[0] in {"01_methodology", "03_projects"}


def expected_input_paths() -> list[str]:
    paths = [PRED_REL]
    prereg = WORKSPACE / "03_projects/language_management/slavic_interslavic/00_lane_control/marginal_intelligibility_20260811/preregistration_v001"
    paths.extend(path.relative_to(WORKSPACE).as_posix() for path in sorted(x for x in prereg.rglob("*") if x.is_file()))
    methodology = WORKSPACE / "01_methodology/research_department"
    paths.extend(
        path.relative_to(WORKSPACE).as_posix()
        for path in sorted(x for x in methodology.rglob("*") if x.is_file() and "__pycache__" not in x.parts and x.suffix.lower() != ".pyc")
    )
    return paths


def pin_errors(graph: dict[str, Any]) -> list[dict[str, str]]:
    errors: list[dict[str, str]] = []
    pins = graph.get("input_pins", [])
    observed_paths = [item.get("workspace_relative_path") for item in pins if isinstance(item, dict)]
    expected_paths = expected_input_paths()
    if observed_paths != expected_paths:
        errors.append(err("INPUT_PIN", "Input inventory does not exactly match predecessor, preregistration package, and methodology files."))
    pin_ids = [item.get("pin_id") for item in pins if isinstance(item, dict)]
    if len(pin_ids) != len(set(pin_ids)):
        errors.append(err("INPUT_PIN", "Input pin IDs are not unique."))
    for item in pins:
        if not isinstance(item, dict):
            errors.append(err("INPUT_PIN", "Input pin is not an object."))
            continue
        raw = item.get("workspace_relative_path")
        if not safe_workspace_relative(raw):
            errors.append(err("PATH_SAFETY", f"Unsafe workspace-relative input path: {raw!r}"))
            continue
        path = (WORKSPACE / raw).resolve()
        try:
            path.relative_to(WORKSPACE)
        except ValueError:
            errors.append(err("PATH_SAFETY", f"Resolved input path escapes workspace: {raw}"))
            continue
        if not path.is_file():
            errors.append(err("INPUT_PIN", f"Pinned input is missing: {raw}"))
            continue
        if path.stat().st_size != item.get("bytes") or sha256_file(path) != item.get("sha256"):
            errors.append(err("INPUT_PIN", f"Byte/hash drift for pinned input: {raw}"))
    predecessor_pins = [item for item in pins if isinstance(item, dict) and item.get("role") == "cyclic_typed_evidence_graph_predecessor"]
    if len(predecessor_pins) != 1:
        errors.append(err("INPUT_PIN", "Exactly one predecessor pin is required."))
    elif predecessor_pins[0].get("workspace_relative_path") != PRED_REL or predecessor_pins[0].get("bytes") != PRED_BYTES or predecessor_pins[0].get("sha256") != PRED_SHA:
        errors.append(err("INPUT_PIN", "The predecessor pin differs from the mandated exact bytes/hash/path."))
    return errors


def predecessor() -> dict[str, Any]:
    path = WORKSPACE / PRED_REL
    if path.stat().st_size != PRED_BYTES or sha256_file(path) != PRED_SHA:
        raise RuntimeError("pinned predecessor mismatch")
    value = strict_load(path)
    if not isinstance(value, dict):
        raise RuntimeError("predecessor is not a JSON object")
    return value


def lineage_errors(graph: dict[str, Any], pred: dict[str, Any]) -> list[dict[str, str]]:
    errors: list[dict[str, str]] = []
    nodes = graph.get("nodes", [])
    edges = graph.get("edges", [])
    by_node_id = {item.get("id"): item for item in nodes if isinstance(item, dict)}
    by_edge_id = {item.get("id"): item for item in edges if isinstance(item, dict)}
    if len(by_node_id) != len(nodes):
        errors.append(err("LINEAGE", "Successor node IDs must be unique."))
    if len(by_edge_id) != len(edges):
        errors.append(err("LINEAGE", "Successor edge IDs must be unique."))

    node_map = graph.get("predecessor_to_successor_mapping", {}).get("nodes", [])
    edge_map = graph.get("predecessor_to_successor_mapping", {}).get("edges", [])
    if [item.get("predecessor_index") for item in node_map] != list(range(len(pred.get("nodes", [])))):
        errors.append(err("MAPPING", "Predecessor node mapping must cover every node exactly once in source order."))
    if [item.get("predecessor_index") for item in edge_map] != list(range(len(pred.get("edges", [])))):
        errors.append(err("MAPPING", "Predecessor edge mapping must cover every edge exactly once in source order."))

    for index, legacy in enumerate(pred.get("nodes", [])):
        node_id = legacy.get("id")
        node = by_node_id.get(node_id)
        if node is None:
            errors.append(err("LINEAGE", f"Predecessor node missing in successor: {node_id}"))
            continue
        expected_fingerprint = canonical_sha256(legacy)
        lineage = node.get("lineage", {})
        if node.get("legacy_payload") != legacy or node.get("id") != legacy.get("id") or node.get("type") != legacy.get("type") or node.get("label") != legacy.get("label"):
            errors.append(err("LINEAGE", f"Legacy payload or identity drift for node {node_id}."))
        if lineage.get("predecessor_pointer") != f"/nodes/{index}" or lineage.get("predecessor_fingerprint_sha256") != expected_fingerprint or lineage.get("operation") != "preserved_with_typed_metadata":
            errors.append(err("LINEAGE", f"Broken node lineage for {node_id}."))
        if index < len(node_map):
            mapping = node_map[index]
            if mapping != {
                "predecessor_index": index,
                "predecessor_id": node_id,
                "successor_id": node_id,
                "operation": "preserved_with_typed_metadata",
                "predecessor_fingerprint_sha256": expected_fingerprint,
            }:
                errors.append(err("MAPPING", f"Incorrect node mapping at predecessor index {index}."))

    expected_new = {"claim_old_post44_full_r823_equivalence"}
    if set(by_node_id) - {item.get("id") for item in pred.get("nodes", [])} != expected_new:
        errors.append(err("LINEAGE", "The explicit equivalence-claim node must be the only added node."))
    claim = by_node_id.get("claim_old_post44_full_r823_equivalence", {})
    claim_lineage = claim.get("lineage", {})
    if claim_lineage != {"operation": "added_for_acyclic_claim_target", "predecessor_pointer": None, "predecessor_fingerprint_sha256": None, "motivation_id": "M001"}:
        errors.append(err("LINEAGE", "Added claim node lineage is not exact."))

    for index, legacy in enumerate(pred.get("edges", [])):
        edge_id = f"edge_{index:03d}"
        edge = by_edge_id.get(edge_id)
        if edge is None:
            errors.append(err("LINEAGE", f"Predecessor edge mapping missing successor {edge_id}."))
            continue
        expected_fingerprint = canonical_sha256(legacy)
        expected_operation = "preserved_with_typed_metadata"
        expected_relation = dict(legacy)
        if index == 7:
            expected_relation = {"from": "old_post44_scope_gap", "to": "claim_old_post44_full_r823_equivalence", "type": "vetoes_claim"}
            expected_operation = "redirected_and_retyped"
        elif index == 19:
            expected_relation = {"from": "missing_branch_rows", "to": "unified_v62", "type": "records_absence_for_claim"}
            expected_operation = "retyped_for_channel_separation"
        if edge.get("legacy_payload") != legacy:
            errors.append(err("LINEAGE", f"Legacy edge payload drift at index {index}."))
        if {key: edge.get(key) for key in ["from", "to", "type"]} != expected_relation:
            errors.append(err("LINEAGE", f"Unpermitted active relation at edge index {index}."))
        lineage = edge.get("lineage", {})
        if lineage.get("predecessor_pointer") != f"/edges/{index}" or lineage.get("predecessor_fingerprint_sha256") != expected_fingerprint or lineage.get("operation") != expected_operation:
            errors.append(err("LINEAGE", f"Broken edge lineage at index {index}."))
        if index < len(edge_map):
            mapping = edge_map[index]
            if mapping != {
                "predecessor_index": index,
                "predecessor_edge_fingerprint_sha256": expected_fingerprint,
                "successor_edge_id": edge_id,
                "operation": expected_operation,
            }:
                errors.append(err("MAPPING", f"Incorrect edge mapping at predecessor index {index}."))

    mapping_root = graph.get("predecessor_to_successor_mapping", {})
    if mapping_root.get("added_nodes") != ["claim_old_post44_full_r823_equivalence"] or mapping_root.get("added_edges") != [] or mapping_root.get("unmapped_predecessor_nodes") != [] or mapping_root.get("unmapped_predecessor_edges") != []:
        errors.append(err("MAPPING", "Mapping additions/unmapped sets are not exact."))
    return errors


def topology_errors(graph: dict[str, Any]) -> list[dict[str, str]]:
    errors: list[dict[str, str]] = []
    nodes = graph.get("nodes", [])
    edges = graph.get("edges", [])
    ids = [node.get("id") for node in nodes if isinstance(node, dict)]
    idset = set(ids)
    if len(ids) != len(idset) or None in idset:
        errors.append(err("DAG_CYCLE", "Node IDs must be unique and non-null before topology replay."))
        return errors
    adjacency = {node_id: [] for node_id in idset}
    indegree = {node_id: 0 for node_id in idset}
    edge_ids: set[str] = set()
    for edge in edges:
        if not isinstance(edge, dict):
            errors.append(err("DAG_CYCLE", "Edge is not an object."))
            continue
        edge_id, source, target = edge.get("id"), edge.get("from"), edge.get("to")
        if edge_id in edge_ids:
            errors.append(err("DAG_CYCLE", f"Duplicate edge ID {edge_id}."))
        edge_ids.add(edge_id)
        if source not in idset or target not in idset:
            errors.append(err("DAG_CYCLE", f"Unknown edge endpoint in {edge_id}."))
            continue
        adjacency[source].append(target)
        indegree[target] += 1
    queue = [node_id for node_id, degree in indegree.items() if degree == 0]
    heapq.heapify(queue)
    replay: list[str] = []
    while queue:
        node_id = heapq.heappop(queue)
        replay.append(node_id)
        for target in sorted(adjacency[node_id]):
            indegree[target] -= 1
            if indegree[target] == 0:
                heapq.heappush(queue, target)
    if len(replay) != len(idset):
        errors.append(err("DAG_CYCLE", "Topological replay did not consume every node; graph is cyclic."))
        return errors
    if graph.get("topological_order") != replay:
        errors.append(err("TOPOLOGICAL_REPLAY", "Declared topological order differs from deterministic replay."))
    positions = {node_id: index for index, node_id in enumerate(replay)}
    for edge in edges:
        if edge.get("from") in positions and edge.get("to") in positions and positions[edge["from"]] >= positions[edge["to"]]:
            errors.append(err("TOPOLOGICAL_REPLAY", f"Edge {edge.get('id')} does not move forward in replay order."))
    return errors


def channel_errors(graph: dict[str, Any]) -> list[dict[str, str]]:
    errors: list[dict[str, str]] = []
    definitions = graph.get("channel_definitions", [])
    if [item.get("channel") for item in definitions if isinstance(item, dict)] != CHANNELS:
        errors.append(err("CHANNEL_SEPARATION", "Required channels must appear exactly once in frozen order."))
    for item in definitions:
        channel = item.get("channel")
        if set(item.get("cannot_count_as", [])) != set(CHANNELS) - {channel}:
            errors.append(err("CHANNEL_SEPARATION", f"Channel exclusion set is incomplete for {channel}."))

    nodes = graph.get("nodes", [])
    node_ids = {node.get("id") for node in nodes if isinstance(node, dict)}
    for node in nodes:
        evidence = node.get("evidence")
        expected_channel = EXPECTED_NODE_CHANNELS.get(node.get("id"))
        if expected_channel is None:
            if evidence is not None:
                errors.append(err("CHANNEL_SEPARATION", f"Unexpected evidence channel on node {node.get('id')}."))
            continue
        if not isinstance(evidence, dict) or evidence.get("channel") != expected_channel:
            errors.append(err("CHANNEL_SEPARATION", f"Wrong evidence channel on node {node.get('id')}."))
            continue
        provenance = evidence.get("source_provenance", {})
        sense = evidence.get("sense", {})
        if provenance.get("predecessor_graph_sha256") != PRED_SHA or not isinstance(sense.get("concept_or_claim_id"), str) or not sense.get("intended_sense") or not sense.get("scope"):
            errors.append(err("SOURCE_SENSE_PROVENANCE", f"Incomplete source/sense provenance on node {node.get('id')}."))
        if not set(provenance.get("evidence_source_node_ids", [])).issubset(node_ids):
            errors.append(err("SOURCE_SENSE_PROVENANCE", f"Unknown evidence source node on {node.get('id')}."))

    edges = graph.get("edges", [])
    observed_channels = []
    for index, edge in enumerate(edges):
        if index >= len(EXPECTED_EDGE_CHANNELS) or edge.get("channel") != EXPECTED_EDGE_CHANNELS[index]:
            errors.append(err("CHANNEL_SEPARATION", f"Wrong or unexpected channel at edge index {index}."))
        channel = edge.get("channel")
        if channel in CHANNELS:
            observed_channels.append(channel)
            provenance = edge.get("source_provenance", {})
            sense = edge.get("sense")
            if provenance.get("predecessor_graph_sha256") != PRED_SHA or not isinstance(sense, dict) or not sense.get("concept_or_claim_id") or not sense.get("intended_sense") or not sense.get("scope"):
                errors.append(err("SOURCE_SENSE_PROVENANCE", f"Evidence edge {edge.get('id')} lacks exact source/sense provenance."))
        elif channel == "structural":
            if edge.get("sense") is not None:
                errors.append(err("CHANNEL_SEPARATION", f"Structural edge {edge.get('id')} must not masquerade as sense evidence."))
        else:
            errors.append(err("CHANNEL_SEPARATION", f"Unknown channel on edge {edge.get('id')}."))
    if set(observed_channels) != set(CHANNELS):
        errors.append(err("CHANNEL_SEPARATION", "All six evidence channels must be represented in active edges."))
    if len(edges) > 19:
        absence_edge = edges[19]
        if absence_edge.get("channel") != "absence" or absence_edge.get("type") != "records_absence_for_claim" or "adverse" in absence_edge.get("type", ""):
            errors.append(err("CHANNEL_SEPARATION", "Missing branch rows must remain absence, not adverse evidence."))
    if len(edges) > 7:
        repaired = edges[7]
        if repaired.get("from") != "old_post44_scope_gap" or repaired.get("to") != "claim_old_post44_full_r823_equivalence" or repaired.get("type") != "vetoes_claim" or repaired.get("channel") != "veto":
            errors.append(err("CHANNEL_SEPARATION", "Scope-gap veto must target the explicit equivalence claim."))
    return errors


def contract_errors(graph: dict[str, Any], pred: dict[str, Any]) -> list[dict[str, str]]:
    errors: list[dict[str, str]] = []
    if graph.get("schema_id") != "slisv-typed-evidence-dag-successor-v001" or graph.get("graph_id") != "SLISV-EVIDENCE-DAG-SUCCESSOR-20260811-001":
        errors.append(err("IDENTITY", "Successor identity drift."))
    scope = graph.get("scope", {})
    if scope.get("writes_outside_package") is not False or scope.get("upstream_files_modified") != [] or scope.get("predecessor_copied") is not False or scope.get("predecessor_bytes_preserved") is not True:
        errors.append(err("APPEND_ONLY", "Append-only scope contract is not fail-closed."))
    if any(scope.get(key) != 0 for key in ["human_response_records", "native_witness_records_added", "community_or_named_person_review_records_added"]):
        errors.append(err("CLAIM_BOUNDARY", "Human, native-witness, or community review records may not be invented."))
    contract = graph.get("append_only_contract", {})
    exact_contract = {
        "predecessor_graph_path": PRED_REL,
        "predecessor_graph_bytes": PRED_BYTES,
        "predecessor_graph_sha256": PRED_SHA,
        "predecessor_mutated": False,
        "successor_is_new_artifact": True,
        "active_edge_replacements_are_mapped_not_silently_deleted": True,
        "predecessor_payloads_embedded_per_lineage_record": True,
    }
    if contract != exact_contract:
        errors.append(err("APPEND_ONLY", "Append-only predecessor contract differs from the exact pin."))

    if len(pred.get("nodes", [])) != 21 or len(pred.get("edges", [])) != 20:
        errors.append(err("PREDECESSOR", "Pinned predecessor shape changed unexpectedly."))
    cycle_edges = [pred.get("edges", [])[index] for index in [6, 7]] if len(pred.get("edges", [])) > 7 else []
    expected_cycle = [
        {"from": "old_post44_witness", "to": "old_post44_scope_gap", "type": "exhibits"},
        {"from": "old_post44_scope_gap", "to": "old_post44_witness", "type": "vetoes_full_r823_equivalence_claim_for"},
    ]
    if cycle_edges != expected_cycle:
        errors.append(err("PREDECESSOR", "The exact adverse predecessor cycle is not bound."))
    repair = graph.get("repair", {})
    binding = repair.get("cycle_binding", {})
    if binding.get("predecessor_path") != ["old_post44_witness", "old_post44_scope_gap", "old_post44_witness"] or binding.get("predecessor_edge_indices") != [6, 7] or binding.get("successor_path") != ["old_post44_witness", "old_post44_scope_gap", "claim_old_post44_full_r823_equivalence"]:
        errors.append(err("REPAIR_BINDING", "Adverse cycle binding or successor path is not exact."))
    expected_cycle_fingerprints = [canonical_sha256(pred["edges"][6]), canonical_sha256(pred["edges"][7])]
    if binding.get("predecessor_edge_fingerprints_sha256") != expected_cycle_fingerprints:
        errors.append(err("REPAIR_BINDING", "Cycle binding fingerprints do not match predecessor bytes."))
    changes = repair.get("changes", [])
    if [item.get("predecessor_edge_index") for item in changes] != [7, 19]:
        errors.append(err("REPAIR_BINDING", "Only edge 7 and edge 19 may be transformed."))
    if len(repair.get("alternatives", [])) < 4 or any(item.get("disposition") != "rejected" or not item.get("reason") for item in repair.get("alternatives", [])):
        errors.append(err("REPAIR_BINDING", "Rejected alternatives and reasons must remain explicit."))

    counts = graph.get("counts", {})
    expected_counts = {
        "predecessor_nodes": 21, "successor_nodes": 22, "predecessor_edges": 20, "successor_edges": 20,
        "added_nodes": 1, "redirected_or_retyped_edges": 2, "required_evidence_channels": 6,
    }
    if counts != expected_counts:
        errors.append(err("COUNTS", "Graph and repair counts are not exact."))
    decision = graph.get("decision_contract", {})
    if decision != {
        "scalar_decision": None,
        "automatic_decision": False,
        "positive_mass_may_offset_adverse": False,
        "absence_may_be_imputed_as_zero": False,
        "candidate_may_be_counted_as_support": False,
        "graph_role": "typed provenance and routing only",
    }:
        errors.append(err("SCALAR_DECISION", "No-scalar and channel non-substitution contract drift."))
    coverage = {item.get("layer"): item for item in graph.get("layer_coverage", []) if isinstance(item, dict)}
    if coverage.get("review_record") != {"layer": "review_record", "state": "absent_not_invented", "node_ids": []}:
        errors.append(err("CLAIM_BOUNDARY", "Review records must remain explicitly absent."))
    claim = {node.get("id"): node for node in graph.get("nodes", []) if isinstance(node, dict)}.get("claim_old_post44_full_r823_equivalence", {})
    attributes = claim.get("attributes", {})
    if attributes.get("claim_status") != "rejected_by_typed_adverse_evidence" or attributes.get("decision_kind") != "typed_veto_disposition_not_scalar":
        errors.append(err("SCALAR_DECISION", "New claim target must be a non-scalar rejected claim."))
    boundary = graph.get("claim_boundary", {})
    prohibited_terms = ["native", "human intelligibility", "community", "canonical", "release", "scalar"]
    does_not = " | ".join(boundary.get("does_not_prove", [])).lower()
    if not all(term in does_not for term in prohibited_terms) or "G007 through G012" not in boundary.get("preregistration_effect", ""):
        errors.append(err("CLAIM_BOUNDARY", "Nonclaim boundary or unaffected blocked gates are incomplete."))
    return errors


def all_graph_errors(graph: dict[str, Any], schema: dict[str, Any], check_pins: bool = True) -> list[dict[str, str]]:
    errors = schema_errors(graph, schema)
    if check_pins:
        errors.extend(pin_errors(graph))
    try:
        pred = predecessor()
    except Exception as exc:
        return errors + [err("PREDECESSOR", str(exc))]
    errors.extend(lineage_errors(graph, pred))
    errors.extend(topology_errors(graph))
    errors.extend(channel_errors(graph))
    errors.extend(contract_errors(graph, pred))
    return errors


def pointer_parent(doc: Any, pointer: str) -> tuple[Any, str]:
    if not isinstance(pointer, str) or not pointer.startswith("/"):
        raise ValueError("mutation pointer must be absolute")
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer[1:].split("/")]
    current = doc
    for part in parts[:-1]:
        current = current[int(part)] if isinstance(current, list) else current[part]
    return current, parts[-1]


def apply_mutation(doc: dict[str, Any], fixture: dict[str, Any]) -> None:
    mutation = fixture["mutation"]
    if mutation.get("op") != "replace":
        raise ValueError("only replace mutations are supported")
    parent, key = pointer_parent(doc, mutation["json_pointer"])
    if isinstance(parent, list):
        parent[int(key)] = mutation["value"]
    else:
        if key not in parent:
            raise KeyError(key)
        parent[key] = mutation["value"]


def hostile_errors(graph: dict[str, Any], schema: dict[str, Any]) -> tuple[list[dict[str, str]], int, int]:
    errors: list[dict[str, str]] = []
    expectations = strict_load(FIXTURE_DIR / "EXPECTATIONS.json")
    rejected = 0
    for item in expectations.get("fixtures", []):
        path = FIXTURE_DIR / item.get("path", "")
        expected_code = item.get("expected_rejection_code")
        if path.name == "duplicate_key.json":
            try:
                strict_load(path)
            except DuplicateKeyError:
                rejected += 1
                continue
            except Exception as exc:
                errors.append(err("HOSTILE_FIXTURE", f"Duplicate-key fixture failed for wrong reason: {exc}"))
                continue
            errors.append(err("HOSTILE_FIXTURE", "Duplicate-key fixture was accepted."))
            continue
        try:
            fixture = strict_load(path)
            if fixture.get("baseline") != "../TYPED_EVIDENCE_DAG_SUCCESSOR_V001.json" or fixture.get("expected_rejection_code") != expected_code:
                errors.append(err("HOSTILE_FIXTURE", f"Fixture metadata drift: {path.name}"))
                continue
            mutated = copy.deepcopy(graph)
            apply_mutation(mutated, fixture)
            observed = {item["code"] for item in all_graph_errors(mutated, schema, check_pins=True)}
            if expected_code in observed:
                rejected += 1
            else:
                errors.append(err("HOSTILE_FIXTURE", f"{path.name} did not produce {expected_code}; got {sorted(observed)}"))
        except Exception as exc:
            errors.append(err("HOSTILE_FIXTURE", f"Fixture execution error for {path.name}: {exc}"))
    count = expectations.get("fixture_count", -1)
    if count != len(expectations.get("fixtures", [])):
        errors.append(err("HOSTILE_FIXTURE", "Fixture count metadata is inconsistent."))
    return errors, rejected, count


def safe_package_relative(raw: Any) -> bool:
    if not isinstance(raw, str) or not raw or "\\" in raw:
        return False
    pure = PurePosixPath(raw)
    return not pure.is_absolute() and all(part not in {"", ".", ".."} for part in pure.parts)


def manifest_errors(include_receipt: bool) -> list[dict[str, str]]:
    errors: list[dict[str, str]] = []
    manifest = strict_load(MANIFEST)
    artifacts = manifest.get("artifacts", [])
    declared = [item.get("path") for item in artifacts if isinstance(item, dict)]
    if manifest.get("artifact_count") != len(artifacts) or len(declared) != len(set(declared)):
        errors.append(err("MANIFEST", "Manifest count or path uniqueness failed."))
    for item in artifacts:
        raw = item.get("path")
        if not safe_package_relative(raw):
            errors.append(err("PATH_SAFETY", f"Unsafe manifest path: {raw!r}"))
            continue
        path = (BASE / raw).resolve()
        try:
            path.relative_to(BASE.resolve())
        except ValueError:
            errors.append(err("PATH_SAFETY", f"Manifest path escapes package: {raw}"))
            continue
        if not path.is_file() or path.stat().st_size != item.get("bytes") or sha256_file(path) != item.get("sha256"):
            errors.append(err("MANIFEST", f"Manifest byte/hash mismatch: {raw}"))
    if manifest.get("control_files") != ["MANIFEST.json", "VALIDATION_RECEIPT.json"] or manifest.get("unlisted_files_permitted") is not False:
        errors.append(err("MANIFEST", "Manifest control-file or exact-inventory policy drift."))
    actual = sorted(
        path.relative_to(BASE).as_posix()
        for path in BASE.rglob("*")
        if path.is_file() and "__pycache__" not in path.parts and path.suffix.lower() != ".pyc"
    )
    expected = sorted(declared + ["MANIFEST.json"] + (["VALIDATION_RECEIPT.json"] if RECEIPT.is_file() else []))
    if actual != expected:
        errors.append(err("MANIFEST", f"Exact inventory mismatch; declared={expected}, actual={actual}"))
    if include_receipt and not RECEIPT.is_file():
        errors.append(err("RECEIPT", "Receipt was requested but is absent."))
    return errors


def projection_errors(graph: dict[str, Any]) -> list[dict[str, str]]:
    errors: list[dict[str, str]] = []

    def rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
        with path.open("r", encoding="utf-8", newline="") as stream:
            reader = csv.DictReader(stream)
            return list(reader.fieldnames or []), list(reader)

    node_fields = ["id", "type", "layer", "channel", "predecessor_pointer", "lineage_operation", "label"]
    fields, observed_nodes = rows(BASE / "NODES.csv")
    expected_nodes = []
    for node in graph.get("nodes", []):
        expected_nodes.append({
            "id": node["id"], "type": node["type"], "layer": node["layer"],
            "channel": node["evidence"]["channel"] if node["evidence"] else "structural",
            "predecessor_pointer": node["lineage"]["predecessor_pointer"] or "",
            "lineage_operation": node["lineage"]["operation"], "label": node["label"],
        })
    if fields != node_fields or observed_nodes != expected_nodes:
        errors.append(err("CSV_PROJECTION", "NODES.csv is not an exact ordered projection of successor nodes."))

    edge_fields = ["id", "from", "to", "type", "channel", "predecessor_pointer", "lineage_operation", "concept_or_claim_id", "scope"]
    fields, observed_edges = rows(BASE / "EDGES.csv")
    expected_edges = []
    for edge in graph.get("edges", []):
        expected_edges.append({
            "id": edge["id"], "from": edge["from"], "to": edge["to"], "type": edge["type"],
            "channel": edge["channel"], "predecessor_pointer": edge["lineage"]["predecessor_pointer"],
            "lineage_operation": edge["lineage"]["operation"],
            "concept_or_claim_id": edge["sense"]["concept_or_claim_id"] if edge["sense"] else "",
            "scope": edge["sense"]["scope"] if edge["sense"] else "",
        })
    if fields != edge_fields or observed_edges != expected_edges:
        errors.append(err("CSV_PROJECTION", "EDGES.csv is not an exact ordered projection of successor edges."))

    map_fields = ["kind", "predecessor_index", "predecessor_id_or_fingerprint", "successor_id", "operation"]
    fields, observed_mapping = rows(BASE / "PREDECESSOR_TO_SUCCESSOR_MAPPING.csv")
    expected_mapping = []
    mapping = graph.get("predecessor_to_successor_mapping", {})
    for item in mapping.get("nodes", []):
        expected_mapping.append({
            "kind": "node", "predecessor_index": str(item["predecessor_index"]),
            "predecessor_id_or_fingerprint": item["predecessor_id"], "successor_id": item["successor_id"],
            "operation": item["operation"],
        })
    for item in mapping.get("edges", []):
        expected_mapping.append({
            "kind": "edge", "predecessor_index": str(item["predecessor_index"]),
            "predecessor_id_or_fingerprint": item["predecessor_edge_fingerprint_sha256"],
            "successor_id": item["successor_edge_id"], "operation": item["operation"],
        })
    if fields != map_fields or observed_mapping != expected_mapping:
        errors.append(err("CSV_PROJECTION", "PREDECESSOR_TO_SUCCESSOR_MAPPING.csv is not an exact ordered projection of lineage mapping."))
    return errors


def receipt_errors() -> list[dict[str, str]]:
    if not RECEIPT.is_file():
        return [err("RECEIPT", "Validation receipt is absent.")]
    receipt = strict_load(RECEIPT)
    errors: list[dict[str, str]] = []
    if receipt.get("status") != "PASS" or receipt.get("bounded_result") != "PARENT_REVIEW_READY_PASS_FOR_DAG_SUCCESSOR_ONLY":
        errors.append(err("RECEIPT", "Receipt is not a bounded DAG-only PASS."))
    if receipt.get("validator_mode") != "independent_read_only_python_standard_library_no_producer_import":
        errors.append(err("RECEIPT", "Validator independence statement drift."))
    expected_paths = ["TYPED_EVIDENCE_DAG_SUCCESSOR_V001.json", "TYPED_EVIDENCE_DAG_SUCCESSOR_V001.schema.json", "validate_evidence_dag_successor_v001.py", "MANIFEST.json"]
    pins = receipt.get("artifact_pins", [])
    if [item.get("path") for item in pins if isinstance(item, dict)] != expected_paths:
        errors.append(err("RECEIPT", "Receipt artifact pin set is not exact."))
    for item in pins:
        path = BASE / item.get("path", "")
        if not path.is_file() or path.stat().st_size != item.get("bytes") or sha256_file(path) != item.get("sha256"):
            errors.append(err("RECEIPT", f"Receipt pin mismatch: {item.get('path')}"))
    if receipt.get("checks", {}).get("hostile_fixtures") != "PASS_6_OF_6_REJECTED":
        errors.append(err("RECEIPT", "Receipt hostile-fixture result is incomplete."))
    launch = receipt.get("launch_state", "")
    if "G007_THROUGH_G012_REMAIN_BLOCKED_AND_UNCHANGED" not in launch:
        errors.append(err("RECEIPT", "Receipt must preserve unrelated launch blockers."))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--include-receipt", action="store_true")
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args()
    errors: list[dict[str, str]] = []
    try:
        graph = strict_load(GRAPH)
        schema = strict_load(SCHEMA)
    except Exception as exc:
        result = {"status": "FAIL", "errors": [{"code": "JSON_PARSE", "detail": str(exc)}]}
        print(json.dumps(result, ensure_ascii=False, separators=(",", ":") if args.compact else None, indent=None if args.compact else 2))
        return 1
    errors.extend(schema_document_errors(schema))
    errors.extend(all_graph_errors(graph, schema, check_pins=True))
    hostile, rejected, fixture_count = hostile_errors(graph, schema)
    errors.extend(hostile)
    errors.extend(projection_errors(graph))
    errors.extend(manifest_errors(args.include_receipt))
    if args.include_receipt:
        errors.extend(receipt_errors())
    result = {
        "status": "PASS" if not errors else "FAIL",
        "graph_id": graph.get("graph_id"),
        "errors": errors,
        "checks": {
            "draft_2020_12_schema_declared": not any(item["code"].startswith("SCHEMA") for item in errors),
            "input_pins_checked": len(graph.get("input_pins", [])),
            "predecessor_sha256": PRED_SHA,
            "nodes_replayed": len(graph.get("nodes", [])),
            "edges_replayed": len(graph.get("edges", [])),
            "hostile_fixtures_rejected": rejected,
            "hostile_fixture_count": fixture_count,
            "manifest_checked": True,
            "receipt_checked": args.include_receipt,
        },
        "bounded_result": "PARENT_REVIEW_READY_PASS_FOR_DAG_SUCCESSOR_ONLY" if not errors else "FAIL_CLOSED",
    }
    print(json.dumps(result, ensure_ascii=False, separators=(",", ":") if args.compact else None, indent=None if args.compact else 2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
