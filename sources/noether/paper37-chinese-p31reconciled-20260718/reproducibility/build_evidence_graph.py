#!/usr/bin/env python3
"""Add the controlled-Hant slice to the pinned Paper 37 evidence DAG and validate it."""
from __future__ import annotations

from collections import Counter, defaultdict, deque
from copy import deepcopy
from datetime import datetime
from pathlib import Path
import csv
import hashlib
import json


ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / "evidence/NOE-P37_TYPED_EVIDENCE_GRAPH.json"
REPORT = ROOT / "qa/EVIDENCE_GRAPH_VALIDATION_REPORT.json"
DECISIONS = ROOT / "decisions"
CROSSWALK = ROOT / "evidence/NOE-P37_CJKV_CROSSWALK.csv"
NATIVE_LEDGER = ROOT / "evidence/CHINESE_NATIVE_EVIDENCE_LEDGER.csv"
ADVERSE_LEDGER = ROOT / "evidence/CHINESE_ADVERSE_EVIDENCE_LEDGER.csv"

BASE_GRAPH_ID = "NOE-P37-ZH-HANS-TYPED-EVIDENCE-GRAPH-20260718"
GRAPH_ID = "NOE-P37-ZH-HANS-HANT-TYPED-EVIDENCE-GRAPH-20260718"
BASE_CANONICAL_SHA256 = "5FCB644FCAB3D9CE547AFC57010A1F25371631E538F0FA705B0C36AD0524570D"
HANS_HASH = "A4A0A97E548840915650FE813AED8FC120D2ABE79F3FA76F9ADF35D5EDAB1B0C"
HANT_HASH = "FC2493ADE14D66835C0EBAAD7C84C78AFFD33A357594F45384CD518C94F32012"
HANT_DECISION_HASH = "6DCACC6A7BC51FDABD796AC154157F8A0E86D0B40F12707774B4736283F18372"
DIFF_HASH = "C3104D31D2B9A464E6520979D9D5A4FB888B45BBF74654CB20A500849F6B164D"
FIELD_POLICY_HASH = "EDACDCFDBE4859CB833B2E8D8C0DFA7106C2D905A516ADF39A2BC0B4041A9350"

HANT_NODE_IDS = {
    "SRC-CJKV-FIELD-POLICY",
    "SRC-ZH-HANS-P37",
    "SRC-ZH-HANT-P37",
    "CMP-P37-HANS-HANT-SCRIPT-DIFF",
    "CONCEPT-CONTROLLED-HANT-SCRIPT",
    "FORM-CONTROLLED-HANT-SCRIPT",
    "DECISION-ZH-HANT-SCRIPT",
    "TARGET-P37-ZH-HANT",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def canonical_sha(value: object) -> str:
    payload = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest().upper()


def read_rows(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


graph = json.loads(GRAPH.read_text(encoding="utf-8"))

# Reconstruct and pin the pre-existing Hans graph semantically. This makes the
# augmentation idempotent while ensuring the original 62-node/123-edge tranche
# is never silently rewritten by this script.
base = deepcopy(graph)
base["graph_id"] = BASE_GRAPH_ID
base["nodes"] = [node for node in base["nodes"] if node.get("id") not in HANT_NODE_IDS]
base["edges"] = [
    edge
    for edge in base["edges"]
    if edge.get("from") not in HANT_NODE_IDS and edge.get("to") not in HANT_NODE_IDS
]
base_digest = canonical_sha(base)
if base_digest != BASE_CANONICAL_SHA256:
    raise SystemExit(
        f"Pinned Hans graph base changed: expected {BASE_CANONICAL_SHA256}, got {base_digest}"
    )
if len(base["nodes"]) != 62 or len(base["edges"]) != 123:
    raise SystemExit(
        f"Unexpected Hans graph base size: {len(base['nodes'])} nodes, {len(base['edges'])} edges"
    )

graph = deepcopy(base)
graph["graph_id"] = GRAPH_ID
graph["nodes"].extend(
    [
        {
            "id": "SRC-CJKV-FIELD-POLICY",
            "type": "SOURCE",
            "source_class": "governance_policy",
            "path": "03_projects/language_management/cjk/04_comparison_web/CJKV_CROSSWALK_FIELD_POLICY_20260718.md",
            "sha256": FIELD_POLICY_HASH,
            "claim_limit": "Mandarin-Simplified evidence cannot authorize Taiwan, Hong Kong, or Macao localization.",
        },
        {
            "id": "SRC-ZH-HANS-P37",
            "type": "SOURCE",
            "source_class": "draft_translation",
            "path": "zh-Hans-CN/Noether_Paper37_Chinese_P31Reconciled_zh-Hans-CN_v001.tex",
            "sha256": HANS_HASH,
            "language_tag": "zh-Hans-CN",
            "claim_limit": "Script-conversion input only; not independent Hant or regional evidence.",
        },
        {
            "id": "SRC-ZH-HANT-P37",
            "type": "SOURCE",
            "source_class": "draft_translation",
            "path": "zh-Hant-controlled/Noether_Paper37_Chinese_P31Reconciled_zh-Hant-controlled_v001.tex",
            "sha256": HANT_HASH,
            "language_tag": "zh-Hant",
            "localization_status": "controlled_generic_nonregional",
            "external_validation": False,
            "human_comprehension_validation": False,
        },
        {
            "id": "CMP-P37-HANS-HANT-SCRIPT-DIFF",
            "type": "COMPUTATION",
            "path": "qa/HANS_HANT_SCRIPT_DIFF_REPORT.json",
            "sha256": DIFF_HASH,
            "input_sha256": HANS_HASH,
            "output_sha256": HANT_HASH,
            "status": "pass",
            "scope": "computational Hans-to-Hant script/TeX/build integrity only",
            "interpretation_limit": "Not regional prose suitability, human comprehension, or external certification.",
        },
        {
            "id": "CONCEPT-CONTROLLED-HANT-SCRIPT",
            "type": "CONCEPT",
            "concept_id": "NOE-P37-CONTROLLED-HANT-SCRIPT",
            "sense_window": "Controlled generic Traditional-script rendering of the audited Hans Paper 37 target; not Taiwan-, Hong Kong-, or Macao-localized prose.",
        },
        {
            "id": "FORM-CONTROLLED-HANT-SCRIPT",
            "type": "FORM",
            "language_tag": "zh-Hant",
            "form": "受控繁体字形（通用、非地域化）",
            "basin_membership": "mixed_or_contested",
            "status": "candidate_after_context_check",
        },
        {
            "id": "DECISION-ZH-HANT-SCRIPT",
            "type": "DECISION",
            "record_path": "decisions/NOE-P37-ZH-HANT-SCRIPT.json",
            "record_sha256": HANT_DECISION_HASH,
            "status": "candidate_after_context_check",
            "external_certification": False,
            "human_comprehension_validation": False,
            "regional_localization": False,
        },
        {
            "id": "TARGET-P37-ZH-HANT",
            "type": "TARGET",
            "path": "zh-Hant-controlled/Noether_Paper37_Chinese_P31Reconciled_zh-Hant-controlled_v001.tex",
            "sha256": HANT_HASH,
            "language_tag": "zh-Hant",
            "status": "controlled_generic_nonregional",
            "regional_localization": False,
            "external_certification": False,
            "human_comprehension_validation": False,
        },
    ]
)
graph["edges"].extend(
    [
        {"from": "SRC-P31-P37", "to": "CONCEPT-CONTROLLED-HANT-SCRIPT", "type": "support", "scope": "source mathematical sense and apparatus"},
        {"from": "SRC-ZH-HANS-P37", "to": "FORM-CONTROLLED-HANT-SCRIPT", "type": "candidate", "scope": "declared script-conversion base"},
        {"from": "SRC-ZH-HANT-P37", "to": "FORM-CONTROLLED-HANT-SCRIPT", "type": "checkpoint", "scope": "exact controlled-generic Hant output"},
        {"from": "SRC-CJKV-FIELD-POLICY", "to": "DECISION-ZH-HANT-SCRIPT", "type": "adverse", "scope": "regional localization and evidence-transfer prohibition"},
        {"from": "CONCEPT-CONTROLLED-HANT-SCRIPT", "to": "FORM-CONTROLLED-HANT-SCRIPT", "type": "candidate", "scope": "source-constrained script form"},
        {"from": "FORM-CONTROLLED-HANT-SCRIPT", "to": "DECISION-ZH-HANT-SCRIPT", "type": "selected_as", "scope": "internal lane script decision"},
        {"from": "CTRL-MANDARIN-SIMPLIFIED-DOMINANCE", "to": "DECISION-ZH-HANT-SCRIPT", "type": "control", "scope": "qualitative dominance debt; never a readiness scalar"},
        {"from": "DECISION-ZH-HANT-SCRIPT", "to": "TARGET-P37-ZH-HANT", "type": "implemented_in", "scope": "controlled generic Hant checkpoint"},
        {"from": "TARGET-P37-ZH-HANS", "to": "CMP-P37-HANS-HANT-SCRIPT-DIFF", "type": "input_to", "scope": "pinned Hans SHA-256"},
        {"from": "CMP-P37-HANS-HANT-SCRIPT-DIFF", "to": "TARGET-P37-ZH-HANT", "type": "verifies", "scope": "script/TeX/build integrity only"},
    ]
)

GRAPH.write_text(json.dumps(graph, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

errors: list[dict] = []
node_ids = [node.get("id") for node in graph["nodes"]]
node_by_id = {node["id"]: node for node in graph["nodes"]}
duplicate_nodes = sorted(node_id for node_id, count in Counter(node_ids).items() if count > 1)
for node_id in duplicate_nodes:
    errors.append({"kind": "duplicate_node_id", "node_id": node_id})

edge_keys: set[str] = set()
for edge in graph["edges"]:
    if edge.get("from") not in node_by_id or edge.get("to") not in node_by_id:
        errors.append({"kind": "edge_endpoint", "edge": edge})
    key = json.dumps(edge, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    if key in edge_keys:
        errors.append({"kind": "duplicate_edge", "edge": edge})
    edge_keys.add(key)

# Directed-acyclic validation.
adjacency: dict[str, list[str]] = defaultdict(list)
indegree = {node_id: 0 for node_id in node_by_id}
for edge in graph["edges"]:
    if edge.get("from") in node_by_id and edge.get("to") in node_by_id:
        adjacency[edge["from"]].append(edge["to"])
        indegree[edge["to"]] += 1
queue = deque(sorted(node_id for node_id, degree in indegree.items() if degree == 0))
visited: list[str] = []
while queue:
    node_id = queue.popleft()
    visited.append(node_id)
    for target in adjacency[node_id]:
        indegree[target] -= 1
        if indegree[target] == 0:
            queue.append(target)
if len(visited) != len(node_by_id):
    errors.append({"kind": "graph_cycle", "visited": len(visited), "nodes": len(node_by_id)})

# Every typed record, concept, and evidence-source reference must resolve in the graph.
decision_paths = sorted(DECISIONS.glob("*.json"))
graph_decision_nodes = [node for node in graph["nodes"] if node.get("type") == "DECISION"]
graph_decision_paths = {node.get("record_path"): node for node in graph_decision_nodes}
graph_concepts = {node.get("concept_id") for node in graph["nodes"] if node.get("type") == "CONCEPT"}
typed_source_ids: set[str] = set()
claim_control_record_count = 0
for path in decision_paths:
    data = json.loads(path.read_text(encoding="utf-8"))
    relative = str(path.relative_to(ROOT)).replace("\\", "/")
    dnode = graph_decision_paths.get(relative)
    if dnode is None:
        errors.append({"kind": "decision_graph_reference_missing", "record": relative})
    else:
        if dnode.get("status") != data["decision"]["status"]:
            errors.append({"kind": "decision_status_mismatch", "record": relative, "graph": dnode.get("status"), "record_status": data["decision"]["status"]})
        if dnode.get("external_certification") is not False or dnode.get("human_comprehension_validation") is not False:
            errors.append({"kind": "unsupported_validation_claim", "record": relative})
        else:
            claim_control_record_count += 1
    if data["concept"]["concept_id"] not in graph_concepts:
        errors.append({"kind": "concept_graph_reference_missing", "record": relative, "concept_id": data["concept"]["concept_id"]})
    for channel in ("support", "candidate", "competitor", "adverse", "veto"):
        for item in data["evidence"][channel]:
            source_id = item["source"]["source_id"]
            typed_source_ids.add(source_id)
            if source_id not in node_by_id:
                errors.append({"kind": "typed_evidence_source_missing", "record": relative, "evidence_id": item["evidence_id"], "source_id": source_id})

# Crosswalk and native-ledger joins remain Hans-only; the Hant decision is script metadata.
crosswalk_rows = read_rows(CROSSWALK)
for row in crosswalk_rows:
    path = ROOT / row["decision_record_path"]
    if not path.exists():
        errors.append({"kind": "crosswalk_decision_missing", "concept_id": row["concept_id"], "path": str(path)})
    elif json.loads(path.read_text(encoding="utf-8"))["concept"]["concept_id"] != row["concept_id"]:
        errors.append({"kind": "crosswalk_concept_mismatch", "concept_id": row["concept_id"]})
    if row["concept_id"] not in graph_concepts:
        errors.append({"kind": "crosswalk_graph_concept_missing", "concept_id": row["concept_id"]})

source_nodes = [node for node in graph["nodes"] if node.get("type") == "SOURCE"]
source_path_hashes = {(node.get("path"), node.get("sha256")) for node in source_nodes}
source_hashes = {node.get("sha256") for node in source_nodes}
native_rows = read_rows(NATIVE_LEDGER)
for row in native_rows:
    if row["concept_id"] not in graph_concepts:
        errors.append({"kind": "native_graph_concept_missing", "evidence_id": row["evidence_id"], "concept_id": row["concept_id"]})
    if (row["source_path_or_uri"], row["sha256"]) not in source_path_hashes:
        errors.append({"kind": "native_graph_source_missing", "evidence_id": row["evidence_id"], "path": row["source_path_or_uri"], "sha256": row["sha256"]})

adverse_rows = read_rows(ADVERSE_LEDGER)
adverse_concept_rows = 0
adverse_nonlexical_unit_rows = 0
for row in adverse_rows:
    reference = row["concept_or_unit"]
    if reference in graph_concepts:
        adverse_concept_rows += 1
    elif row["channel"] == "translation_defect" and reference.startswith("NOE-P37-"):
        adverse_nonlexical_unit_rows += 1
    else:
        errors.append({"kind": "adverse_graph_reference_missing", "adverse_id": row["adverse_id"], "reference": reference})
    version = row["sha256_or_version"]
    if len(version) == 64 and all(ch in "0123456789ABCDEFabcdef" for ch in version):
        if (row["evidence_path_or_source"], version.upper()) not in source_path_hashes:
            errors.append({"kind": "adverse_graph_source_missing", "adverse_id": row["adverse_id"]})
    elif ";" in version and all(len(item) == 64 for item in version.split(";")):
        for item in version.split(";"):
            if item.upper() not in source_hashes:
                errors.append({"kind": "adverse_graph_source_hash_missing", "adverse_id": row["adverse_id"], "sha256": item.upper()})
    elif "scope=71-tex-files" in version and "CMP-ZH-71-TEX" not in node_by_id:
        errors.append({"kind": "adverse_scope_computation_missing", "adverse_id": row["adverse_id"]})

# Exact Hant custody bindings in graph nodes and computation.
for node_id, expected in (
    ("SRC-ZH-HANS-P37", HANS_HASH),
    ("SRC-ZH-HANT-P37", HANT_HASH),
    ("TARGET-P37-ZH-HANT", HANT_HASH),
):
    if node_by_id.get(node_id, {}).get("sha256") != expected:
        errors.append({"kind": "hant_binding_mismatch", "node_id": node_id, "expected": expected, "actual": node_by_id.get(node_id, {}).get("sha256")})
if node_by_id.get("DECISION-ZH-HANT-SCRIPT", {}).get("record_sha256") != HANT_DECISION_HASH:
    errors.append({"kind": "hant_decision_hash_mismatch"})

node_counts = dict(sorted(Counter(node["type"] for node in graph["nodes"]).items()))
report = {
    "schema_version": "1.0.0",
    "validation_id": "NOE-P37-ZH-EVIDENCE-GRAPH-20260718",
    "recorded_at": datetime.now().astimezone().isoformat(timespec="seconds"),
    "graph_path": str(GRAPH),
    "graph_sha256": sha(GRAPH),
    "pinned_hans_base_canonical_sha256": base_digest,
    "pinned_hans_base_node_count": len(base["nodes"]),
    "pinned_hans_base_edge_count": len(base["edges"]),
    "hant_added_node_count": len(HANT_NODE_IDS),
    "hant_added_edge_count": len(graph["edges"]) - len(base["edges"]),
    "node_counts": node_counts,
    "edge_count": len(graph["edges"]),
    "typed_decision_count": len(decision_paths),
    "graph_decision_reference_count": len(graph_decision_nodes),
    "typed_unique_evidence_source_reference_count": len(typed_source_ids),
    "typed_evidence_source_reference_coverage_count": sum(1 for source_id in typed_source_ids if source_id in node_by_id),
    "crosswalk_rows": len(crosswalk_rows),
    "native_ledger_rows": len(native_rows),
    "adverse_ledger_rows": len(adverse_rows),
    "adverse_concept_reference_rows": adverse_concept_rows,
    "adverse_nonlexical_translation_unit_rows": adverse_nonlexical_unit_rows,
    "claim_control_record_count": claim_control_record_count,
    "dag_topological_visit_count": len(visited),
    "error_count": len(errors),
    "errors": errors,
    "status": "pass" if not errors else "fail",
    "validation_scope": "Pinned Hans graph preservation; Hant decision/target custody; unique node and edge references; endpoint resolution; typed record, concept, and evidence-source coverage; crosswalk/native/adverse joins; explicit nonregional/nonexternal claim controls; and DAG acyclicity. The four adverse translation-defect unit rows are verified as nonlexical unit evidence rather than promoted to terminology concepts. No external linguistic certification.",
}
REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(
    json.dumps(
        {
            "graph": str(GRAPH),
            "graph_sha256": sha(GRAPH),
            "report": str(REPORT),
            "report_sha256": sha(REPORT),
            "status": report["status"],
            "nodes": len(graph["nodes"]),
            "edges": len(graph["edges"]),
            "errors": len(errors),
        },
        ensure_ascii=True,
        indent=2,
    )
)
raise SystemExit(0 if not errors else 1)
