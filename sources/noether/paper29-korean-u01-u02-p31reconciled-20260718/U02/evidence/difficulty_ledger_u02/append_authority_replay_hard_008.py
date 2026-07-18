from __future__ import annotations

import hashlib
import json
from datetime import datetime
from pathlib import Path


HERE = Path(__file__).resolve().parent
TRANCHE = HERE.parents[1]
LEDGER = HERE / "DIFFICULTY_LEDGER.jsonl"
U02_SOURCE = TRANCHE / "source/Noether_Paper29_German_P31_U02_Rationalbasis_exact_lf.tex"
SEALED = Path(r"evidence://local-workspace/Codex\2026-06-01\we-are-currently-doing-a-massive\Noether_LocalCodex_20260718_P31_FullPaperCanonicalReaudit_WEB_DROP\1\01_current\cum_de_Local_20260718_P31.tex")
CANDIDATE = Path(r"evidence://local-workspace/Codex\2026-06-01\we-are-currently-doing-a-massive\Noether_LocalCodex_20260718_P04p133_Eq28_SourceFix\1\01_current\cum_de_Local_20260718_P04p133_Eq28_SourceFix.tex")
PREAPPEND_SHA = "FF2230A22614B344250E74DCD7307868E49295489FCD8E7B7F4C994333B40898"
PREAPPEND_HEAD = "C78EB237E42185DC42E6B8542030239C9DD652202800F25D0C6A5C764EA3E9E8"
EXPECTED_FILE_HASHES = {
    U02_SOURCE: "B7EF88537BCD90D0408B3D1942DA410410FE45E79DD457B2DF6DFA2D4929DCAC",
    SEALED: "A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F",
    CANDIDATE: "5D159B7457F2ACBAD583C82D391476659101F9519E7A4B45C97D4BD8A48C7AFD",
}
EXPECTED_NORMALIZED_OFFSETS = {SEALED: 1219101, CANDIDATE: 1219565}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def canonical_hash(record: dict) -> str:
    body = {key: value for key, value in record.items() if key != "record_sha256"}
    encoded = json.dumps(body, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return digest(encoded)


def normalize_newlines(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")


def scan(haystack: str, needle: str) -> tuple[int, int]:
    count = haystack.count(needle)
    return count, haystack.find(needle)


def main() -> int:
    raw_ledger = LEDGER.read_bytes()
    if digest(raw_ledger) != PREAPPEND_SHA:
        raise SystemExit(f"REFUSING APPEND: expected seven-record ledger SHA {PREAPPEND_SHA}, got {digest(raw_ledger)}")
    if not raw_ledger.endswith(b"\n"):
        raise SystemExit("REFUSING APPEND: canonical JSONL lacks terminal newline")
    records = [json.loads(line) for line in raw_ledger.decode("utf-8").splitlines() if line.strip()]
    if len(records) != 7 or records[-1].get("issue_id") != "CJK-KO-P29-U02-HARD-007" or records[-1].get("record_sha256") != PREAPPEND_HEAD:
        raise SystemExit("REFUSING APPEND: expected HARD-007 chain head not found")

    for path, expected_hash in EXPECTED_FILE_HASHES.items():
        if not path.is_file() or digest(path.read_bytes()) != expected_hash:
            raise SystemExit(f"REFUSING APPEND: authority/source hash mismatch: {path}")

    needle = U02_SOURCE.read_bytes().decode("utf-8")
    results: dict[Path, dict[str, int]] = {}
    for path in (SEALED, CANDIDATE):
        text = path.read_bytes().decode("utf-8")
        raw_count, raw_offset = scan(text, needle)
        normalized_count, normalized_offset = scan(normalize_newlines(text), normalize_newlines(needle))
        results[path] = {
            "raw_count": raw_count,
            "raw_offset": raw_offset,
            "normalized_count": normalized_count,
            "normalized_offset": normalized_offset,
            "crlf_count": text.count("\r\n"),
            "bare_lf_count": text.count("\n") - text.count("\r\n"),
        }
        if raw_count != 0 or raw_offset != -1:
            raise SystemExit(f"REFUSING APPEND: raw-scan failure is no longer reproducible: {path}")
        if normalized_count != 1 or normalized_offset != EXPECTED_NORMALIZED_OFFSETS[path]:
            raise SystemExit(f"REFUSING APPEND: normalized authority scan differs: {path}: {results[path]}")

    recorded_at = datetime.now().astimezone().replace(microsecond=0).isoformat()
    record = {
        "schema_version": "1.0.0",
        "ledger_sequence": 8,
        "issue_id": "CJK-KO-P29-U02-HARD-008",
        "record_sha256": "",
        "previous_record_sha256": PREAPPEND_HEAD,
        "recorded_at": recorded_at,
        "occurrence_time": {"value": "2026-07-18", "precision": "date_only"},
        "work_unit": "P29-KO-U02 fresh sealed/candidate authority-occurrence replay",
        "authority_cursor": r"sealed P31 A48CB5CD...CF814F and unsealed candidate 5D159B74...C7AFD; U02 lines 25-39; next substantive cursor exact full-P29 line 41, 2. \srcspaced{Beweis des Endlichkeitskriteriums.}",
        "structural_ids": ["NOE-P29-KO-U02-ROOT-001"],
        "source_locator": "the complete LF-normalized U02 source string, 5,659 UTF-8 bytes, scanned ordinally against both cumulative German TeX heads",
        "target_locator": "append-only reproducibility record HARD-008 for the source-survival claim in CJK-KO-P29-006",
        "difficulty_class": "newline_sensitive_authority_occurrence_false_negative",
        "symptom": "A fresh raw ordinal substring scan reported zero U02 occurrences in both cumulative heads, apparently contradicting the recorded one-occurrence source-survival result.",
        "severity": "high",
        "discovery_channel": "fresh pre-continuation sealed-head authority replay",
        "cause": {
            "evidence": "The U02 source file is LF-normalized. The sealed cumulative head contains 24,005 CRLF pairs and 113 bare LF characters; the candidate contains 23,999 CRLF pairs and 114 bare LF characters. An exact multi-line LF needle therefore does not byte/character-match the CRLF representation.",
            "inference": "The zero result was a line-ending representation false negative, not evidence that the U02 text disappeared from either authority head."
        },
        "attempted_approaches": [
            {"approach": "Search each cumulative UTF-8 text for the complete LF U02 string without canonicalizing line endings.", "outcome": "failed", "evidence": "Ordinal raw counts were 0 with offset -1 in sealed and candidate."},
            {"approach": "Treat the earlier one-occurrence assertion as sufficient and omit the contradictory replay.", "outcome": "rejected", "evidence": "That would erase a reproducible false-negative mode and leave the authority claim unauditable."},
            {"approach": "Normalize CRLF to LF, then remaining CR to LF, in both haystack and needle before an ordinal count and offset scan.", "outcome": "resolved", "evidence": "Normalized count is exactly 1 at character offset 1,219,101 in sealed P31 and exactly 1 at offset 1,219,565 in the candidate."}
        ],
        "resolution_state": "resolved",
        "resolution_or_workaround": "For multi-line authority survival checks, first decode strict UTF-8 and canonicalize CRLF and lone CR to LF in both the cumulative head and bounded source needle; then require exactly one ordinal occurrence and record its normalized character offset. Preserve the failed raw result as evidence.",
        "evidence_artifacts": [
            {"path_or_reference": str(U02_SOURCE), "hash_or_test": "SHA-256:B7EF88537BCD90D0408B3D1942DA410410FE45E79DD457B2DF6DFA2D4929DCAC;bytes=5659", "role": "LF-normalized U02 occurrence needle", "evidence_kind": "current_file"},
            {"path_or_reference": str(SEALED), "hash_or_test": "SHA-256:A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F;bytes=2150562", "role": "sealed German P31 authority haystack", "evidence_kind": "current_file"},
            {"path_or_reference": str(CANDIDATE), "hash_or_test": "SHA-256:5D159B7457F2ACBAD583C82D391476659101F9519E7A4B45C97D4BD8A48C7AFD;bytes=2151027", "role": "compiled but unsealed German source-survival witness", "evidence_kind": "current_file"},
            {"path_or_reference": "fresh raw ordinal replay", "hash_or_test": "PASS:sealed_raw_count=0;sealed_raw_offset=-1;candidate_raw_count=0;candidate_raw_offset=-1", "role": "retained failed scan", "evidence_kind": "computation"},
            {"path_or_reference": "newline-normalized ordinal replay", "hash_or_test": "PASS:sealed_count=1;sealed_char_offset=1219101;candidate_count=1;candidate_char_offset=1219565", "role": "resolved occurrence scan", "evidence_kind": "computation"}
        ],
        "residual_risk": "Line-ending normalization establishes textual survival but does not promote the candidate to sealed authority; Unicode normalization, decoding drift, or future source edits can still invalidate the scan and offsets.",
        "recurrence_cues": ["multi-line exact slice uses LF while cumulative source uses CRLF", "raw full-string occurrence unexpectedly equals zero", "source-survival claim lacks normalization method or offset", "candidate occurrence is mistaken for authority promotion"],
        "transferable_lesson": "A multi-line source-survival scan must declare encoding and newline normalization. A raw zero is a diagnostic to preserve and explain, not grounds to silently replace a prior result.",
        "future_check": "Before U03 and every later bounded unit, rehash the live sealed head, normalize line endings explicitly, require one occurrence, and record the new normalized offset; stop on zero or multiple matches.",
        "related_decision_ids": ["CJK-KO-P29-006"],
        "changed_artifacts": ["evidence/difficulty_ledger_u02/DIFFICULTY_LEDGER.jsonl", "evidence/difficulty_ledger_u02/DIFFICULTY_LEDGER.csv", "evidence/difficulty_ledger_u02/DIFFICULTY_LEDGER_METADATA.json"],
        "supersedes": [],
        "supersession_state": "not_applicable",
        "validation_state": {
            "internal": "Strict file hashes, the failed raw scan, normalized counts, normalized offsets, chain integrity, schema, CSV projection, and metadata are replayed by local validators.",
            "external_human": "No external or human source certification is claimed; the candidate remains unsealed."
        },
        "continuation_or_revisit": r"Next exact source cursor is full-P29 line 41, 2. \srcspaced{Beweis des Endlichkeitskriteriums.}; rerun normalized occurrence checks after any authority-head change."
    }
    record["record_sha256"] = canonical_hash(record)
    with LEDGER.open("ab") as handle:
        handle.write((json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n").encode("utf-8"))
    print(f"appended={record['issue_id']} recorded_at={recorded_at} head={record['record_sha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
