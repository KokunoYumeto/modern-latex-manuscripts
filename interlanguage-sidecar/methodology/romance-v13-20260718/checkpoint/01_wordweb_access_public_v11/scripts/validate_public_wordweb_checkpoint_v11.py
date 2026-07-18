#!/usr/bin/env python3
"""Independently validate the public WordWeb/access checkpoint v11."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from pathlib import Path


HUMAN_FIELDS = [
    "human_n",
    "human_correct",
    "human_incorrect",
    "human_abstain",
    "human_latency_ms",
    "human_confidence",
    "effect_interval",
]
FORBIDDEN_KEYS = {
    "locator",
    "source_locator",
    "source_path",
    "quote",
    "macro_locator",
    "macro_quote",
    "context_evidence",
}
FORBIDDEN_PATTERNS = {
    "windows_absolute_path": re.compile(r"[A-Za-z]:[\\/]+"),
    "file_uri": re.compile(r"file://", re.I),
    "unix_home_path": re.compile(r"/(?:Users|home)/[^/]+/"),
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest().upper()


def walk(value: object, path: str = "$"):
    if isinstance(value, dict):
        for key, child in value.items():
            yield path, key, child
            yield from walk(child, f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk(child, f"{path}[{index}]")


def add(checks: dict[str, bool], errors: list[str], name: str, value: bool, detail: str) -> None:
    checks[name] = bool(value)
    if not value:
        errors.append(f"{name}: {detail}")


def validate(output: Path, project_root: Path | None = None) -> dict:
    ww_path = output / "data" / "PAN_ROMANCE_WORDWEB_PUBLIC_v11.json"
    access_path = output / "data" / "PAN_ROMANCE_ACCESS_LEDGER_PUBLIC_v11.json"
    access_csv_path = output / "data" / "PAN_ROMANCE_ACCESS_LEDGER_PUBLIC_v11.csv"
    gaps_path = output / "data" / "WORDWEB_UNRESOLVED_SENSE_GAPS_v11.csv"
    cohorts_path = output / "data" / "ROMANCE_READER_COHORTS_v2.csv"
    method_path = output / "method" / "MII_METHOD_PUBLIC_v11.md"
    provenance_path = output / "PROVENANCE_INPUT_HASHES.json"
    required = [
        ww_path,
        access_path,
        access_csv_path,
        gaps_path,
        cohorts_path,
        method_path,
        provenance_path,
        output / "README.md",
    ]
    checks: dict[str, bool] = {}
    errors: list[str] = []
    add(checks, errors, "required_files", all(path.is_file() for path in required), "missing public file")
    if errors:
        return {"artifact": "PUBLIC_WORDWEB_CHECKPOINT_VALIDATION_v11", "status": "FAIL", "checks": checks, "errors": errors}

    ww = json.loads(ww_path.read_text(encoding="utf-8"))
    access = json.loads(access_path.read_text(encoding="utf-8"))
    provenance = json.loads(provenance_path.read_text(encoding="utf-8"))
    with gaps_path.open(encoding="utf-8", newline="") as handle:
        gaps = list(csv.DictReader(handle))
    with cohorts_path.open(encoding="utf-8", newline="") as handle:
        cohort_csv = list(csv.DictReader(handle))
    with access_csv_path.open(encoding="utf-8", newline="") as handle:
        access_csv_reader = csv.DictReader(handle)
        access_csv_fields = access_csv_reader.fieldnames or []
        access_csv = list(access_csv_reader)

    concepts = ww["core_concepts"]
    senses = ww["senses"]
    extensions = ww["c2_extension_nodes"]
    evidence = ww["evidence_metadata"]
    decisions = ww["decisions"]
    rows = access["rows"]
    cohorts = access["cohorts"]

    add(checks, errors, "artifact_names", ww["artifact"] == "PAN_ROMANCE_WORDWEB_PUBLIC_v11" and access["artifact"] == "PAN_ROMANCE_ACCESS_LEDGER_PUBLIC_v11", "artifact name drift")
    add(checks, errors, "topology_60_106_39", (len(concepts), len(senses), len(extensions)) == (60, 106, 39), "semantic topology drift")
    add(checks, errors, "unique_term_ids", len({row["term_id"] for row in concepts}) == 60, "duplicate term ID")
    add(checks, errors, "unique_sense_ids", len({row["sense_id"] for row in senses}) == 106, "duplicate sense ID")
    add(checks, errors, "evidence_811_unique", len(evidence) == 811 and len({row["evidence_id"] for row in evidence}) == 811, "evidence index drift")
    add(checks, errors, "decisions_106_unique", len(decisions) == 106 and len({row["decision_id"] for row in decisions}) == 106, "decision topology drift")

    all_relations = [relation for concept in concepts for relation in concept.get("relations", [])]
    valid_ids = {row["term_id"] for row in concepts} | {row["sense_id"] for row in senses} | {row["concept_id"] for row in extensions}
    target_relations = [row for row in all_relations if row.get("target_id")]
    add(checks, errors, "relation_records_406", len(all_relations) == 406, "relation record count drift")
    add(checks, errors, "target_id_edges_27", len(target_relations) == 27, "target-ID graph edge count drift")
    add(checks, errors, "all_relation_targets_resolve", all(row["target_id"] in valid_ids for row in target_relations), "invalid relation target")
    add(checks, errors, "id_resolved_references_133", len(target_relations) + len(senses) == 133, "membership-plus-edge boundary drift")

    exact_t51 = ["function_domain", "integral_domain", "generic_domain_or_region", "coefficient_domain_linkage"]
    exact_t60 = ["neutral_or_identity_element", "identity_map", "algebraic_identity", "unit_or_invertible_element"]
    labels = {row["sense_id"]: row["sense_label"] for row in senses}
    add(checks, errors, "T51_four_exact_senses", [labels[f"T51-S{i}"] for i in range(1, 5)] == exact_t51, "T51 sense contract drift")
    add(checks, errors, "T60_four_exact_senses", [labels[f"T60-S{i}"] for i in range(1, 5)] == exact_t60, "T60 sense contract drift")

    forbidden_key_hits = []
    forbidden_pattern_hits = []
    for label, value in [("wordweb", ww), ("access", access), ("provenance", provenance)]:
        for path, key, child in walk(value):
            if key in FORBIDDEN_KEYS:
                forbidden_key_hits.append(f"{label}:{path}.{key}")
            if isinstance(child, str):
                for pattern_name, pattern in FORBIDDEN_PATTERNS.items():
                    if pattern.search(child):
                        forbidden_pattern_hits.append(f"{label}:{path}.{key}:{pattern_name}")
    add(checks, errors, "no_quote_locator_or_host_path_keys", not forbidden_key_hits, str(forbidden_key_hits[:5]))
    add(checks, errors, "no_absolute_host_path_values", not forbidden_pattern_hits, str(forbidden_pattern_hits[:5]))
    add(checks, errors, "extension_context_counts_only", all("context_evidence" not in row and row.get("public_context_policy", "").startswith("counts_only") for row in extensions), "extension snippet leaked or policy missing")

    gap_ids = [row["sense_id"] for row in gaps]
    expected_gap_ids = ww["core_evidence_boundary"]["final_unsupported_sense_ids"]
    add(checks, errors, "supported_78_unsupported_28", ww["counts"]["supported_senses_internal"] == 78 and len(gaps) == 28 and len(expected_gap_ids) == 28, "support/gap totals drift")
    add(checks, errors, "gap_csv_exact_ids", gap_ids == expected_gap_ids and len(set(gap_ids)) == 28, "gap list mismatch")
    add(checks, errors, "inherited_core_zero_quotes", ww["core_evidence_boundary"]["inherited_es_fr_core_records"] == 120 and ww["core_evidence_boundary"]["inherited_core_quotation_count"] == 0, "core evidence boundary drift")
    add(checks, errors, "zero_extension_to_core_promotions", ww["core_evidence_boundary"]["extension_context_to_core_promotions"] == 0, "extension evidence promoted")

    cohort_ids = [row["cohort_id"] for row in cohorts]
    sense_ids = [row["sense_id"] for row in senses]
    row_keys = [(row["sense_id"], row["cohort_id"]) for row in rows]
    expected_keys = [(sense_id, cohort_id) for sense_id in sense_ids for cohort_id in cohort_ids]
    add(checks, errors, "nine_unique_cohorts", len(cohort_ids) == 9 and len(set(cohort_ids)) == 9, "cohort topology drift")
    add(checks, errors, "cohort_csv_matches_json", [row["cohort_id"] for row in cohort_csv] == cohort_ids, "cohort CSV mismatch")
    add(checks, errors, "complete_106_by_9_grid", len(rows) == 954 and row_keys == expected_keys, "access grid incomplete or reordered")
    add(checks, errors, "access_csv_954_rows", len(access_csv) == 954, "access CSV row drift")
    add(checks, errors, "access_csv_keys_match_json", [(row["sense_id"], row["cohort_id"]) for row in access_csv] == row_keys, "access CSV key mismatch")
    add(checks, errors, "access_csv_fields_match_json", access_csv_fields == list(rows[0].keys()), "access CSV schema mismatch")
    add(checks, errors, "zero_human_fields", all(all(row.get(field) is None for field in HUMAN_FIELDS) for row in rows), "nonnull human result")
    add(checks, errors, "zero_human_counts", access["human_observation_count"] == 0 and all(row.get("source_audit_v11_human_observations", 0) == 0 for row in rows), "human count nonzero")
    add(checks, errors, "zero_pilot_eligibility", access["pilot_eligible_count"] == 0 and all(row["pilot_eligible"] is False for row in rows) and all(row["pilot_eligible"] is False for row in decisions), "pilot flag set")
    add(checks, errors, "zero_form_promotions", access["form_promotion_count"] == 0 and ww["counts"]["controlled_form_promotions"] == 0 and all(not row.get("core_form_promotion", False) and not row.get("bridge_form_promotion_eligible", False) for row in evidence), "form promotion leaked")

    method_text = method_path.read_text(encoding="utf-8")
    add(checks, errors, "method_current_106_by_9", "106 × 9 = 954" in method_text and "zero human observations" in method_text.lower(), "method stale")
    add(checks, errors, "method_graph_boundary", "406 relation records" in method_text and "27" in method_text and "133" in method_text, "graph boundary missing")

    source_binding_checked = project_root is not None
    source_binding_ok = True
    if project_root is not None:
        source_paths = {
            "PAN_ROMANCE_WORDWEB_v11": project_root / "wordweb" / "PAN_ROMANCE_WORDWEB_v11.json",
            "PAN_ROMANCE_ACCESS_LEDGER_v11_json": project_root / "access" / "PAN_ROMANCE_ACCESS_LEDGER_v11.json",
            "PAN_ROMANCE_ACCESS_LEDGER_v11_csv": project_root / "access" / "PAN_ROMANCE_ACCESS_LEDGER_v11.csv",
            "MII_METHOD_v11": project_root / "access" / "MII_METHOD_v11.md",
        }
        for name, path in source_paths.items():
            if not path.is_file() or sha256(path) != provenance["input_hashes"].get(name):
                source_binding_ok = False
    add(checks, errors, "source_input_hash_binding", (not source_binding_checked) or source_binding_ok, "source hash mismatch")

    payload_paths = [
        ww_path,
        access_path,
        access_csv_path,
        gaps_path,
        cohorts_path,
        method_path,
        provenance_path,
        output / "README.md",
        output / "scripts" / "build_public_wordweb_checkpoint_v11.py",
        output / "scripts" / "validate_public_wordweb_checkpoint_v11.py",
        output / "scripts" / "reproduce_public_wordweb_checkpoint_v11.py",
    ]
    hashes = {path.relative_to(output).as_posix(): sha256(path) for path in payload_paths}
    return {
        "artifact": "PUBLIC_WORDWEB_CHECKPOINT_VALIDATION_v11",
        "status": "PASS" if not errors else "FAIL",
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "checks": checks,
        "errors": errors,
        "counts": {
            "concepts": len(concepts),
            "senses": len(senses),
            "extensions": len(extensions),
            "evidence_metadata": len(evidence),
            "decisions": len(decisions),
            "relations": len(all_relations),
            "target_id_edges": len(target_relations),
            "supported_senses_internal": ww["counts"]["supported_senses_internal"],
            "unsupported_senses": len(gaps),
            "access_rows": len(rows),
            "cohorts": len(cohorts),
            "human_observations": access["human_observation_count"],
            "pilot_eligible": access["pilot_eligible_count"],
            "form_promotions": access["form_promotion_count"],
        },
        "source_binding_checked": source_binding_checked,
        "payload_hashes": hashes,
        "claim_boundary": (
            "Projection integrity and internal-input binding only; no source-rights, human-access, "
            "pilot, linguistic-correctness, or lane-completion certification."
        ),
    }


def write_report(path: Path, report: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--project-root", type=Path)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    report = validate(
        args.output.resolve(),
        args.project_root.resolve() if args.project_root else None,
    )
    if args.report:
        write_report(args.report.resolve(), report)
    print(json.dumps(report, ensure_ascii=False, sort_keys=True))
    if report["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
