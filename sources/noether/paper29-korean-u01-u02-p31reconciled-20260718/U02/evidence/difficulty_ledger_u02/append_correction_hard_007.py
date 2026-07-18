from __future__ import annotations

import hashlib
import json
from datetime import datetime
from pathlib import Path


HERE = Path(__file__).resolve().parent
TRANCHE = HERE.parents[1]
LEDGER = HERE / "DIFFICULTY_LEDGER.jsonl"
PREAPPEND_SHA = "9A1110510931019912D2C95BDA43E8D2AB62ADC8CEC6A6B3FB5BDADAACC930BE"
PREAPPEND_HEAD = "A8A4F8769F8CF93A44C8B02FA470D2B6257A297718A5AAD5E2C6E2760B5B5869"
PRIOR_IDS = [f"CJK-KO-P29-U02-HARD-{number:03d}" for number in range(1, 7)]


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def canonical_hash(record: dict) -> str:
    body = {key: value for key, value in record.items() if key != "record_sha256"}
    encoded = json.dumps(body, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return digest(encoded)


def main() -> int:
    raw = LEDGER.read_bytes()
    if digest(raw) != PREAPPEND_SHA:
        raise SystemExit(f"REFUSING APPEND: canonical pre-append SHA changed: {digest(raw)}")
    if not raw.endswith(b"\n"):
        raise SystemExit("REFUSING APPEND: canonical JSONL lacks terminal newline")
    records = [json.loads(line) for line in raw.decode("utf-8").splitlines() if line.strip()]
    if [record["issue_id"] for record in records] != PRIOR_IDS or records[-1]["record_sha256"] != PREAPPEND_HEAD:
        raise SystemExit("REFUSING APPEND: expected six-record immutable prefix/head not found")

    recorded_at = datetime.now().astimezone().replace(microsecond=0).isoformat()
    record = {
        "schema_version": "1.0.0",
        "ledger_sequence": 7,
        "issue_id": "CJK-KO-P29-U02-HARD-007",
        "record_sha256": "",
        "previous_record_sha256": PREAPPEND_HEAD,
        "recorded_at": recorded_at,
        "occurrence_time": {"value": "2026-07-18", "precision": "date_only"},
        "work_unit": "P29-KO-U02 difficulty-ledger decision-link correction",
        "authority_cursor": r"sealed P31 A48CB5CD...CF814F; completed U02 normalized full-P29 lines 25-39; next substantive cursor line 41",
        "structural_ids": ["NOE-P29-KO-U02-ROOT-001"],
        "source_locator": "immutable difficulty-ledger records CJK-KO-P29-U02-HARD-001 through HARD-006, related_decision_ids field",
        "target_locator": "append-only supplement record CJK-KO-P29-U02-HARD-007; applies as metadata overlay to prior six records",
        "difficulty_class": "incomplete_substantive_decision_link_metadata",
        "symptom": "The six initial U02 difficulty records cited only the earlier Paper-29 claim decision CJK-KO-P29-001 and omitted the substantive U02 production/review decision CJK-KO-P29-006.",
        "severity": "medium",
        "discovery_channel": "pre-handoff decision-link quality audit",
        "cause": {
            "evidence": "The immutable six-record prefix contains CJK-KO-P29-001 in every related_decision_ids array; the lane log contains CJK-KO-P29-006, produce and independently fidelity-review U02.",
            "inference": "The original records' source/build/review facts remain valid, but their decision linkage was incomplete because the later substantive decision ID was not incorporated before chain initialization."
        },
        "attempted_approaches": [
            {"approach": "Rewrite related_decision_ids inside the six existing JSONL lines.", "outcome": "rejected", "evidence": "That would violate the append-only chain and erase the audit history of the omission."},
            {"approach": "Leave the omission implicit because CJK-KO-P29-001 identifies the paper claim.", "outcome": "rejected", "evidence": "A claim decision does not identify the substantive U02 production and independent-review choice required for handoff traceability."},
            {"approach": "Append one chained supplement that links all six prior issue IDs to CJK-KO-P29-006 and limits supersession to incomplete decision-link metadata.", "outcome": "resolved", "evidence": "The original byte prefix and factual records remain unchanged; the new head provides the missing traceable relation."}
        ],
        "resolution_state": "resolved",
        "resolution_or_workaround": "Interpret each of HARD-001 through HARD-006 with related decisions CJK-KO-P29-001 and CJK-KO-P29-006. Supersede only their incomplete decision-link metadata; preserve every prior fact, hash, state, alternative, and consequence.",
        "evidence_artifacts": [
            {"path_or_reference": "pre-append six-record DIFFICULTY_LEDGER.jsonl", "hash_or_test": f"SHA-256:{PREAPPEND_SHA};bytes={len(raw)}", "role": "immutable original ledger prefix", "evidence_kind": "historical_hash"},
            {"path_or_reference": "00_lane_control/CJK_DECISION_LOGBOOK_20260718.md at CJK-KO-P29-006", "hash_or_test": "SHA-256:E5A5F75C6B6EEFAF06A9AB1BBC7B1FBC227A219AF0AD77F3EF07FFA2D52C8FCC", "role": "decision-log snapshot containing substantive U02 decision", "evidence_kind": "historical_hash"},
            {"path_or_reference": "evidence/structural_index_u02/STRUCTURAL_INDEX.jsonl", "hash_or_test": "SHA-256:F6954C84D72F3E5C02DAEF3B7B1BFF239587A1ECEEA6D7472B8A6EC00C96B60A;bytes=26183", "role": "unchanged U02 structural scope linked by the correction", "evidence_kind": "current_file"},
            {"path_or_reference": "decision-link overlay", "hash_or_test": "PASS:prior_issue_count=6;added_decision=CJK-KO-P29-006;factual_supersession=false", "role": "correction semantics", "evidence_kind": "computation"}
        ],
        "residual_risk": "Consumers that stop at HARD-006 or ignore supersession relations may still miss the substantive decision link.",
        "recurrence_cues": ["difficulty records cite only a claim decision", "substantive production decision is appended after ledger initialization", "handoff metadata does not name the latest correction ID"],
        "transferable_lesson": "Decision linkage is versioned evidence: repair omissions by appending a narrowly scoped relation overlay, never by silently changing chained historical records.",
        "future_check": "Before handoff, require the latest difficulty ID and verify both CJK-KO-P29-001 and CJK-KO-P29-006 are discoverable through the supplement.",
        "related_decision_ids": ["CJK-KO-P29-001", "CJK-KO-P29-006"],
        "changed_artifacts": ["evidence/difficulty_ledger_u02/DIFFICULTY_LEDGER.jsonl", "evidence/difficulty_ledger_u02/DIFFICULTY_LEDGER.csv", "evidence/difficulty_ledger_u02/DIFFICULTY_LEDGER_METADATA.json"],
        "supersedes": PRIOR_IDS,
        "supersession_state": "corrects_prior",
        "validation_state": {
            "internal": "Validator checks immutable-prefix SHA/head, exact supersedes set, CJK-KO-P29-006 linkage, chain, schema, CSV, and metadata.",
            "external_human": "The correction was directly required by the controlling user/session quality audit; no external mathematical review claim changes."
        },
        "continuation_or_revisit": "Revisit before archive handoff and after any later substantive decision-link correction; preserve the first six lines byte-for-byte."
    }
    record["record_sha256"] = canonical_hash(record)
    with LEDGER.open("ab") as handle:
        handle.write((json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n").encode("utf-8"))
    print(f"appended={record['issue_id']} recorded_at={recorded_at} head={record['record_sha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
