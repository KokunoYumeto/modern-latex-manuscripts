from __future__ import annotations

import hashlib
import json
from datetime import datetime
from pathlib import Path


HERE = Path(__file__).resolve().parent
TRANCHE = HERE.parents[1]
LEDGER = HERE / "DIFFICULTY_LEDGER.jsonl"
FAILURE_HISTORY = TRANCHE / "qa/U02_AUTHORITY_VALIDATOR_FAILURE_HISTORY.md"
FINAL_VALIDATOR = TRANCHE / "qa/validate_authority_u02.py"
FINAL_REPORT = TRANCHE / "qa/U02_AUTHORITY_VALIDATION.json"
PREAPPEND_SHA = "EF7DC41703475A96D970ADD9021E3A7059561DCA2E57CF6251403F30DDAF8F56"
PREAPPEND_HEAD = "BD0C376BD8AF1683AC830DA584E262BA29A53CA3C0617C6FE172863EE7CA4D8C"
EXPECTED_FILES = {
    FAILURE_HISTORY: ("D16C05736D7916C78E6B3F4E23B86D3DA33DDB214304303E217D606FD47D0B95", 1660),
    FINAL_VALIDATOR: ("A3C0C8B87813B4980F4669BB3D2FC8CD3F43EFD298711F3303C2062231806C63", 6000),
    FINAL_REPORT: ("FEFCE289DCB293CC3E6E9758CBC7142BC1ACE00CBCF4D63000D539D3011FD4B6", 5451),
}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def canonical_hash(record: dict) -> str:
    body = {key: value for key, value in record.items() if key != "record_sha256"}
    encoded = json.dumps(body, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return digest(encoded)


def main() -> int:
    raw = LEDGER.read_bytes()
    if digest(raw) != PREAPPEND_SHA:
        raise SystemExit(f"REFUSING APPEND: expected eight-record ledger SHA {PREAPPEND_SHA}, got {digest(raw)}")
    if not raw.endswith(b"\n"):
        raise SystemExit("REFUSING APPEND: canonical JSONL lacks terminal newline")
    records = [json.loads(line) for line in raw.decode("utf-8").splitlines() if line.strip()]
    if len(records) != 8 or records[-1].get("issue_id") != "CJK-KO-P29-U02-HARD-008" or records[-1].get("record_sha256") != PREAPPEND_HEAD:
        raise SystemExit("REFUSING APPEND: expected HARD-008 chain head not found")
    for path, (expected_hash, expected_bytes) in EXPECTED_FILES.items():
        if not path.is_file() or digest(path.read_bytes()) != expected_hash or path.stat().st_size != expected_bytes:
            raise SystemExit(f"REFUSING APPEND: final validator-evidence drift: {path}")
    report = json.loads(FINAL_REPORT.read_text(encoding="utf-8"))
    occurrences = list(report.get("authority_occurrences", {}).values())
    if report.get("errors") != [] or len(occurrences) != 2:
        raise SystemExit("REFUSING APPEND: final authority report is not a two-head zero-error pass")
    if any(item.get("raw_ordinal_count") != 0 or item.get("lf_normalized_ordinal_count") != 1 for item in occurrences):
        raise SystemExit("REFUSING APPEND: final authority report does not preserve raw-zero/normalized-one results")

    recorded_at = datetime.now().astimezone().replace(microsecond=0).isoformat()
    record = {
        "schema_version": "1.0.0",
        "ledger_sequence": 9,
        "issue_id": "CJK-KO-P29-U02-HARD-009",
        "record_sha256": "",
        "previous_record_sha256": PREAPPEND_HEAD,
        "recorded_at": recorded_at,
        "occurrence_time": {"value": "approximately 2026-07-18 20:54 and 20:56 Europe/Berlin", "precision": "minute"},
        "work_unit": "P29-KO-U02 authority-validator development failure history",
        "authority_cursor": r"sealed P31 A48CB5CD...CF814F; U02 exact lines 25-39; line 40 blank; line 41 begins 2. \srcspaced{Beweis des Endlichkeitskriteriums.} and continues with proof prose on the same physical line",
        "structural_ids": ["NOE-P29-KO-U02-ROOT-001"],
        "source_locator": "qa/validate_authority_u02.py development states and full-P29 line 41 cursor check",
        "target_locator": "qa/U02_AUTHORITY_VALIDATION.json final zero-error replay and append-only HARD-009",
        "difficulty_class": "validator_development_false_failures_and_text_mode_normalization",
        "symptom": "The reproducibility validator first failed to parse, then falsely rejected the correct line-41 cursor, and initially risked mislabeling Python's automatically newline-normalized text as a raw occurrence scan.",
        "severity": "high",
        "discovery_channel": "validator development and replay audit preserved in qa/U02_AUTHORITY_VALIDATOR_FAILURE_HISTORY.md",
        "cause": {
            "evidence": "A raw Windows-path string fragment ended in a backslash and caused an unterminated-string SyntaxError; the next version required whole-line equality even though proof prose follows the item heading on physical line 41; text-mode reads applied universal-newline translation before the nominal raw scan.",
            "inference": "All three failures were validator implementation defects, not German-source, cursor, authority-survival, or Korean-translation defects."
        },
        "attempted_approaches": [
            {"approach": "Build an authority path with a raw Python string fragment ending in a backslash.", "outcome": "failed", "evidence": "The first run stopped before execution with SyntaxError: unterminated string literal; the patched-over failed state was not hashed."},
            {"approach": "Require full-P29 physical line 41 to equal only the item heading.", "outcome": "failed", "evidence": "The second run passed pinned hashes, U02 equality, and authority occurrences but emitted an error because the first proof sentence legitimately shares line 41; the patched-over failed state was not hashed."},
            {"approach": "Use Python text-mode read results as a nominally raw line-ending-sensitive haystack.", "outcome": "rejected", "evidence": "Universal-newline translation silently converted CRLF to LF and would make a normalized match look raw."},
            {"approach": "Use forward-slash path fragments, test the pinned line-41 heading as a prefix while recording the complete line, and decode read_bytes() for the raw scan before explicit CRLF/CR-to-LF normalization.", "outcome": "resolved", "evidence": "Final validator exits successfully; report errors=[]; both raw counts are 0 and both LF-normalized counts are 1."}
        ],
        "resolution_state": "resolved",
        "resolution_or_workaround": "Retain every failure in the append-oriented history; use syntactically safe path literals, semantically scoped prefix checks for mixed heading/prose lines, and byte-decoded text for raw scans. The final report must preserve raw-zero and normalized-one counts rather than collapsing them.",
        "evidence_artifacts": [
            {"path_or_reference": "qa/U02_AUTHORITY_VALIDATOR_FAILURE_HISTORY.md", "hash_or_test": "SHA-256:D16C05736D7916C78E6B3F4E23B86D3DA33DDB214304303E217D606FD47D0B95;bytes=1660", "role": "durable failed-approach history", "evidence_kind": "current_file"},
            {"path_or_reference": "qa/validate_authority_u02.py first SyntaxError state", "hash_or_test": "UNAVAILABLE:patched in place before hashing; the failure history preserves approximate time, symptom, cause, and repair", "role": "unavailable first failed validator state", "evidence_kind": "unavailable_historical_state"},
            {"path_or_reference": "qa/validate_authority_u02.py second whole-line-equality failure state", "hash_or_test": "UNAVAILABLE:patched in place before hashing; the failure history preserves passed gates, false error, cause, and repair", "role": "unavailable second failed validator state", "evidence_kind": "unavailable_historical_state"},
            {"path_or_reference": "qa/validate_authority_u02.py", "hash_or_test": "SHA-256:A3C0C8B87813B4980F4669BB3D2FC8CD3F43EFD298711F3303C2062231806C63;bytes=6000", "role": "final corrected authority validator", "evidence_kind": "current_file"},
            {"path_or_reference": "qa/U02_AUTHORITY_VALIDATION.json", "hash_or_test": "SHA-256:FEFCE289DCB293CC3E6E9758CBC7142BC1ACE00CBCF4D63000D539D3011FD4B6;bytes=5451", "role": "final zero-error authority replay", "evidence_kind": "current_file"},
            {"path_or_reference": "final authority-validator replay", "hash_or_test": "PASS:errors=[];heads=2;raw_counts=0,0;lf_normalized_counts=1,1;cursor_line_41_prefix=true", "role": "validator outcome", "evidence_kind": "computation"}
        ],
        "residual_risk": "The failed scripts cannot be reconstructed byte-for-byte because they were patched before hashing. A future validator can regress if it reintroduces universal-newline text mode, exact whole-line equality, or unsafe path literal construction.",
        "recurrence_cues": ["raw string literal ends with a backslash", "cursor heading shares a physical line with prose", "Path.read_text result called raw", "failed validator state patched before hashing", "zero-error report collapses raw and normalized counts"],
        "transferable_lesson": "Validator failures are methodological evidence. Preserve their exact symptom and unavailable-hash status, then make the successful validator test the semantic boundary and the representation-sensitive failure mode separately.",
        "future_check": "Before U03 and archive handoff, rerun qa/validate_authority_u02.py and the difficulty validator; revisit HARD-009 if the final script/report hashes change or any failed mode recurs.",
        "related_decision_ids": ["CJK-KO-P29-006"],
        "changed_artifacts": ["qa/U02_AUTHORITY_VALIDATOR_FAILURE_HISTORY.md", "qa/validate_authority_u02.py", "qa/U02_AUTHORITY_VALIDATION.json", "evidence/difficulty_ledger_u02/DIFFICULTY_LEDGER.jsonl", "evidence/difficulty_ledger_u02/DIFFICULTY_LEDGER.csv", "evidence/difficulty_ledger_u02/DIFFICULTY_LEDGER_METADATA.json"],
        "supersedes": [],
        "supersession_state": "not_applicable",
        "validation_state": {
            "internal": "Final validator script/report hashes, empty error list, raw/normalized counts, cursor prefix, unavailable historical states, JSONL chain, schema, CSV, and metadata are checked.",
            "external_human": "No external or human validation is claimed; the failure history is lane-authored reproducibility evidence."
        },
        "continuation_or_revisit": r"Next exact cursor remains full-P29 line 41, 2. \srcspaced{Beweis des Endlichkeitskriteriums.}; replay before U03 and any archive handoff."
    }
    record["record_sha256"] = canonical_hash(record)
    with LEDGER.open("ab") as handle:
        handle.write((json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n").encode("utf-8"))
    print(f"appended={record['issue_id']} recorded_at={recorded_at} head={record['record_sha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
