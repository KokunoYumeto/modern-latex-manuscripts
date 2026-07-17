#!/usr/bin/env python3
"""Reproduce the arithmetic and structural caveats in the research layer.

Standard-library only. This audits the exact v3 and v6.2 packages staged under
01_methodology/weighted_automaton. It does not certify linguistic claims.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable


V3_NAME = "INTERSLAVIC_WEIGHTED_AUTOMATON_STATE_C_PLUS_W0_v3_20260705"
UNIFIED_NAME = "UNIFIED_MARKER_AUTOMATON_v6_2_20260706"


def parse_args() -> argparse.Namespace:
    script = Path(__file__).resolve()
    methodology = script.parents[2]
    weighted = methodology / "weighted_automaton"
    default_output = script.parents[1] / "audit_outputs" / "AUDIT_RESULTS.json"
    parser = argparse.ArgumentParser()
    parser.add_argument("--v3-dir", type=Path, default=weighted / V3_NAME)
    parser.add_argument("--unified-dir", type=Path, default=weighted / UNIFIED_NAME)
    parser.add_argument("--output", type=Path, default=default_output)
    parser.add_argument("--stdout", action="store_true")
    return parser.parse_args()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def truthy(value: str) -> bool:
    return value.strip().lower() in {"1", "true", "yes", "y"}


def fsum(rows: Iterable[dict[str, str]], field: str) -> float:
    return math.fsum(float(row[field] or 0.0) for row in rows)


def distribution(values: Iterable[float]) -> list[float]:
    vals = list(values)
    total = math.fsum(vals)
    if total <= 0:
        return [0.0 for _ in vals]
    return [value / total for value in vals]


def d1(values: Iterable[float]) -> float:
    probs = distribution(values)
    return math.exp(-math.fsum(p * math.log(p) for p in probs if p > 0))


def d2(values: Iterable[float]) -> float:
    probs = distribution(values)
    return 1.0 / math.fsum(p * p for p in probs if p > 0)


def kl_uniform(values: Iterable[float]) -> float:
    probs = distribution(values)
    n = len(probs)
    return math.fsum(p * math.log(p * n) for p in probs if p > 0)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def verify_manifest(directory: Path, manifest_name: str) -> dict[str, Any]:
    manifest_path = directory / manifest_name
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    checks: list[dict[str, Any]] = []
    for entry in manifest.get("files", []):
        path = directory / entry["file"]
        actual_size = path.stat().st_size if path.exists() else None
        actual_hash = sha256(path) if path.exists() else None
        checks.append(
            {
                "file": entry["file"],
                "exists": path.exists(),
                "size_matches": actual_size == entry.get("bytes"),
                "sha256_matches": actual_hash == entry.get("sha256"),
                "actual_bytes": actual_size,
                "actual_sha256": actual_hash,
            }
        )
    return {
        "manifest": str(manifest_path),
        "entries": len(checks),
        "all_outputs_verified": all(
            item["exists"] and item["size_matches"] and item["sha256_matches"]
            for item in checks
        ),
        "checks": checks,
        "input_chain_hashed": False,
        "input_chain_note": "The package manifest lists outputs only; full generation inputs and code are not pinned here.",
    }


def audit_v3(directory: Path) -> dict[str, Any]:
    ledger_path = directory / "INTERSLAVIC_WEIGHTED_AUTOMATON_STATE_C_PLUS_W0_TERM_LEDGER_v3.csv"
    edges_path = directory / "INTERSLAVIC_WEIGHTED_AUTOMATON_STATE_C_PLUS_W0_EDGES_v3.csv"
    rows = read_csv(ledger_path)
    edges = read_csv(edges_path)

    ids = Counter(row["term_id"] for row in rows)
    duplicate_ids = {term_id: count for term_id, count in ids.items() if count > 1}

    state_c = [fsum(rows, field) for field in ("E_state_C", "W_state_C", "S_state_C")]
    w0 = [fsum(rows, field) for field in ("E_w0_projection", "W_w0_projection", "S_w0_projection")]

    provenance: dict[str, dict[str, float | int]] = {}
    for row in rows:
        key = row["witness_writeback_level"].strip() or "blank"
        bucket = provenance.setdefault(key, {"rows": 0, "E": 0.0, "W": 0.0, "S": 0.0})
        bucket["rows"] = int(bucket["rows"]) + 1
        bucket["E"] = float(bucket["E"]) + float(row["E_state_C"] or 0)
        bucket["W"] = float(bucket["W"]) + float(row["W_state_C"] or 0)
        bucket["S"] = float(bucket["S"]) + float(row["S_state_C"] or 0)

    channel_fields = {
        "support": "support_channel_present",
        "adverse": "adverse_channel_present",
        "gap": "gap_channel_present",
        "candidate": "candidate_channel_present",
    }
    channels = {
        channel: sum(truthy(row[field]) for row in rows)
        for channel, field in channel_fields.items()
    }

    state_c_stats = {
        "mass": {"E": state_c[0], "W": state_c[1], "S": state_c[2]},
        "total": math.fsum(state_c),
        "distribution": dict(zip(("E", "W", "S"), distribution(state_c))),
        "D1": d1(state_c),
        "D2": d2(state_c),
        "KL_to_uniform": kl_uniform(state_c),
    }
    w0_stats = {
        "mass": {"E": w0[0], "W": w0[1], "S": w0[2]},
        "total": math.fsum(w0),
        "distribution": dict(zip(("E", "W", "S"), distribution(w0))),
        "D1": d1(w0),
        "D2": d2(w0),
        "KL_to_uniform": kl_uniform(w0),
        "status": "projection_only",
    }

    expected = {
        "rows": 1229,
        "unique_term_ids": 1215,
        "duplicate_id_rows": 27,
        "concept_buckets": 100,
        "edges": 9124,
        "state_c_mass": [2341.0, 223.0, 239.0],
        "state_c_D1": 1.753704378503014,
        "state_c_KL": 0.5368819502551803,
        "w0_mass": [2341.0, 333.0, 348.0],
    }
    reproduced = {
        "rows": len(rows) == expected["rows"],
        "unique_term_ids": len(ids) == expected["unique_term_ids"],
        "duplicate_id_rows": sum(duplicate_ids.values()) == expected["duplicate_id_rows"],
        "concept_buckets": len({row["concept_current"] for row in rows}) == expected["concept_buckets"],
        "edges": len(edges) == expected["edges"],
        "state_c_mass": state_c == expected["state_c_mass"],
        "state_c_D1": math.isclose(state_c_stats["D1"], expected["state_c_D1"], rel_tol=0, abs_tol=1e-12),
        "state_c_KL": math.isclose(state_c_stats["KL_to_uniform"], expected["state_c_KL"], rel_tol=0, abs_tol=1e-12),
        "w0_mass": w0 == expected["w0_mass"],
    }

    return {
        "directory": str(directory),
        "ledger_rows": len(rows),
        "unique_term_ids": len(ids),
        "duplicate_term_ids": len(duplicate_ids),
        "rows_participating_in_duplicate_ids": sum(duplicate_ids.values()),
        "concept_buckets": len({row["concept_current"] for row in rows}),
        "edge_rows": len(edges),
        "state_c": state_c_stats,
        "w0_projection": w0_stats,
        "channel_row_counts": channels,
        "witness_writeback_provenance": provenance,
        "f10_counts": dict(Counter(row["f10_flag"] for row in rows)),
        "safe_to_show_external_counts": dict(Counter(row["safe_to_show_external"] for row in rows)),
        "action_band_counts": dict(Counter(row["v3_action_band"] for row in rows)),
        "expected_values_reproduced": reproduced,
        "all_expected_values_reproduced": all(reproduced.values()),
        "manifest_verification": verify_manifest(
            directory, "INTERSLAVIC_WEIGHTED_AUTOMATON_STATE_C_PLUS_W0_v3_manifest.json"
        ),
        "status_normalization": "current reconciled serialized dataset snapshot; not external/community certification",
    }


def pseudo_concept_reason(concept: str) -> str | None:
    value = concept.strip()
    lowered = value.lower()
    if not value:
        return "blank"
    if lowered == "all" or lowered.startswith("all "):
        return "scope_or_policy_token"
    if "-lex-" in lowered or lowered.startswith(("ar-lex-", "cjk-w")):
        return "marker_id"
    policy_fragments = (
        "rows are addendum",
        "generated output is not",
        "draft scaffolds",
        "review material only",
        "transfer",
        "ledgers",
    )
    if any(fragment in lowered for fragment in policy_fragments):
        return "policy_or_routing_sentence"
    return None


def audit_unified(directory: Path) -> dict[str, Any]:
    lanes_path = directory / "UNIFIED_MARKER_AUTOMATON_LANE_SUMMARY_v6_2_20260706.csv"
    markers_path = directory / "UNIFIED_MARKER_AUTOMATON_MARKERS_v6_2_20260706.csv"
    edges_path = directory / "UNIFIED_MARKER_AUTOMATON_EDGES_v6_2_20260706.csv"
    concepts_path = directory / "UNIFIED_MARKER_AUTOMATON_CONCEPT_SUMMARY_v6_2_20260706.csv"
    lanes = read_csv(lanes_path)
    markers = read_csv(markers_path)
    edges = read_csv(edges_path)
    concepts = read_csv(concepts_path)

    formula_checks: list[dict[str, Any]] = []
    for row in lanes:
        mass = float(row["support_candidate_mass"] or 0)
        adverse = float(row["adverse_mass"] or 0)
        reported = float(row["readiness_proxy_0_100"] or 0)
        inferred = 100.0 * mass / (mass + adverse + 1.0)
        formula_checks.append(
            {
                "lane": row["lane"],
                "support_candidate_mass": mass,
                "adverse_mass": adverse,
                "reported": reported,
                "inferred_unrounded": inferred,
                "inferred_rounded_1dp": round(inferred, 1),
                "matches_reported": math.isclose(round(inferred, 1), reported, rel_tol=0, abs_tol=0.05),
            }
        )

    candidate_only_high = [
        {
            "lane": row["lane"],
            "support_rows": int(row["support_rows"]),
            "candidate_rows": int(row["candidate_rows"]),
            "reported_proxy": float(row["readiness_proxy_0_100"]),
        }
        for row in lanes
        if int(row["support_rows"]) == 0
        and int(row["candidate_rows"]) > 0
        and float(row["readiness_proxy_0_100"]) >= 90
    ]

    pseudo = [
        {"concept": row["concept"], "reason": reason}
        for row in concepts
        if (reason := pseudo_concept_reason(row["concept"])) is not None
    ]

    return {
        "directory": str(directory),
        "lane_rows": len(lanes),
        "marker_rows": len(markers),
        "edge_rows": len(edges),
        "concept_rows": len(concepts),
        "readiness_formula_inferred": "100 * support_candidate_mass / (support_candidate_mass + adverse_mass + 1)",
        "readiness_formula_matches_all_rows": all(item["matches_reported"] for item in formula_checks),
        "readiness_formula_checks": formula_checks,
        "candidate_only_lanes_scoring_at_least_90": candidate_only_high,
        "readiness_disposition": "rejected_as_decision_measure; at most preserve as evidence_mass_saturation_proxy",
        "pseudo_concepts_detected": pseudo,
        "lexical_authority_disposition": "routing/source-discovery graph after cleaning; not direct lexical authority",
        "manifest_verification": verify_manifest(
            directory, "UNIFIED_MARKER_AUTOMATON_v6_2_manifest.json"
        ),
    }


def main() -> int:
    args = parse_args()
    for directory in (args.v3_dir, args.unified_dir):
        if not directory.is_dir():
            raise SystemExit(f"Missing required directory: {directory}")

    v3 = audit_v3(args.v3_dir.resolve())
    unified = audit_unified(args.unified_dir.resolve())
    hard_checks = {
        "v3_expected_values": v3["all_expected_values_reproduced"],
        "v3_output_manifest": v3["manifest_verification"]["all_outputs_verified"],
        "unified_readiness_formula": unified["readiness_formula_matches_all_rows"],
        "unified_output_manifest": unified["manifest_verification"]["all_outputs_verified"],
    }
    report = {
        "artifact": "interlanguage_research_package_audit",
        "version": "1.0.0",
        "generated_at": datetime.now().astimezone().isoformat(),
        "overall_status": "pass_with_documented_caveats" if all(hard_checks.values()) else "check_failed",
        "hard_checks": hard_checks,
        "interslavic_state_c_v3": v3,
        "unified_v6_2": unified,
        "caveats": [
            "Output manifests verify package files but do not hash the complete generation input chain or code.",
            "State C is a reconciled data snapshot; most West/South gain is concept-shelf provenance.",
            "W0 is a projection only.",
            "Unified readiness_proxy is rejected as readiness.",
            "No arithmetic result certifies term correctness, intelligibility, or community acceptance.",
        ],
    }

    rendered = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(rendered, encoding="utf-8")
    if args.stdout:
        print(rendered, end="")
    else:
        print(f"Wrote {args.output}")
        print(f"Status: {report['overall_status']}")
    return 0 if all(hard_checks.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
