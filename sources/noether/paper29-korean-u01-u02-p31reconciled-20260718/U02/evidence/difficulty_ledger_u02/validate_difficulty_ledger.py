from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker
from pypdf import PdfReader


HERE = Path(__file__).resolve().parent
TRANCHE = HERE.parents[1]
LEDGER, CSV_PATH, SCHEMA, METADATA = HERE / "DIFFICULTY_LEDGER.jsonl", HERE / "DIFFICULTY_LEDGER.csv", HERE / "DIFFICULTY_LEDGER.schema.json", HERE / "DIFFICULTY_LEDGER_METADATA.json"
STRUCT_INDEX = HERE.parent / "structural_index_u02/STRUCTURAL_INDEX.jsonl"
STRUCT_META = HERE.parent / "structural_index_u02/STRUCTURAL_INDEX_METADATA.json"
FILE_HASH = re.compile(r"^SHA-256:([0-9A-F]{64})(?:;bytes=([0-9]+))?$")
EXPECTED_FINAL = {"tex": "B694D05E57B58E1B0373D976356E6B3B3F4883D7CC9398081DB12111877B6A7C", "pdf": "EE0A0ED2E150A5EC48945EA7E47C3F394667F288FF5E933BB00DDF193FBE8988", "png": "F2F772AE57371BA57020C4E816203D3DC154EB46186457846AE2DEBCBEC1FD9E"}
PRECORRECTION_SHA = "9A1110510931019912D2C95BDA43E8D2AB62ADC8CEC6A6B3FB5BDADAACC930BE"
PRECORRECTION_HEAD = "A8A4F8769F8CF93A44C8B02FA470D2B6257A297718A5AAD5E2C6E2760B5B5869"
PRIOR_IDS = [f"CJK-KO-P29-U02-HARD-{number:03d}" for number in range(1, 7)]
SEALED_AUTHORITY = Path(r"evidence://local-workspace/Codex\2026-06-01\we-are-currently-doing-a-massive\Noether_LocalCodex_20260718_P31_FullPaperCanonicalReaudit_WEB_DROP\1\01_current\cum_de_Local_20260718_P31.tex")
UNSEALED_CANDIDATE = Path(r"evidence://local-workspace/Codex\2026-06-01\we-are-currently-doing-a-massive\Noether_LocalCodex_20260718_P04p133_Eq28_SourceFix\1\01_current\cum_de_Local_20260718_P04p133_Eq28_SourceFix.tex")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def canonical_hash(record: dict) -> str:
    body = {k: v for k, v in record.items() if k != "record_sha256"}
    return digest(json.dumps(body, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8"))


def load_jsonl(path: Path) -> tuple[list[dict], list[str]]:
    rows, errors = [], []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            errors.append(f"{path.name}:{number}: {exc}")
    return rows, errors


def project(r: dict) -> dict[str, str]:
    return {"ledger_sequence": str(r["ledger_sequence"]), "issue_id": r["issue_id"], "difficulty_class": r["difficulty_class"], "severity": r["severity"], "resolution_state": r["resolution_state"], "structural_ids": ";".join(r["structural_ids"]), "related_decision_ids": ";".join(r["related_decision_ids"]), "recorded_at": r["recorded_at"], "occurrence_time": r["occurrence_time"]["value"], "occurrence_precision": r["occurrence_time"]["precision"], "source_locator": r["source_locator"], "target_locator": r["target_locator"], "record_sha256": r["record_sha256"], "previous_record_sha256": r["previous_record_sha256"] or "", "supersedes": ";".join(r["supersedes"]), "continuation_or_revisit": r["continuation_or_revisit"]}


def resolved(reference: str) -> Path:
    path = Path(reference)
    return path if path.is_absolute() else TRANCHE / path


def main() -> int:
    errors: list[str] = []
    for path in (LEDGER, CSV_PATH, SCHEMA, METADATA, STRUCT_INDEX, STRUCT_META):
        if not path.is_file():
            errors.append(f"missing {path}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    records, parse_errors = load_jsonl(LEDGER)
    structural, structural_errors = load_jsonl(STRUCT_INDEX)
    errors.extend(parse_errors); errors.extend(structural_errors)
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    metadata = json.loads(METADATA.read_text(encoding="utf-8"))
    structural_meta = json.loads(STRUCT_META.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    schema_error_count = 0

    raw_lines = LEDGER.read_bytes().splitlines(keepends=True)
    if len(raw_lines) < 9 or digest(b"".join(raw_lines[:6])) != PRECORRECTION_SHA:
        errors.append("append-only correction damaged or replaced the immutable six-line prefix")
    if records[:6] and records[5].get("record_sha256") != PRECORRECTION_HEAD:
        errors.append("immutable six-record prefix head changed")
    for number, record in enumerate(records, 1):
        for problem in validator.iter_errors(record):
            schema_error_count += 1
            where = "/".join(str(x) for x in problem.absolute_path) or "<record>"
            errors.append(f"line {number} {record.get('issue_id')} schema {where}: {problem.message}")

    ids = [r.get("issue_id") for r in records]
    if len(ids) != len(set(ids)):
        errors.append("duplicate issue IDs")
    if ids != metadata.get("ordered_issue_ids"):
        errors.append("issue ID/order differs from metadata")
    structural_ids = {r["structural_id"] for r in structural}
    previous = None
    earlier: set[str] = set()
    for sequence, record in enumerate(records, 1):
        issue = record.get("issue_id", "<missing>")
        if record.get("ledger_sequence") != sequence:
            errors.append(f"{issue}: sequence mismatch")
        if record.get("previous_record_sha256") != previous:
            errors.append(f"{issue}: previous hash mismatch")
        actual = canonical_hash(record)
        if actual != record.get("record_sha256"):
            errors.append(f"{issue}: record hash mismatch {actual}")
        previous = record.get("record_sha256")
        for sid in record.get("structural_ids", []):
            if sid not in structural_ids:
                errors.append(f"{issue}: unresolved structural ID {sid}")
        for prior in record.get("supersedes", []):
            if prior not in earlier:
                errors.append(f"{issue}: supersedes non-earlier ID {prior}")
        earlier.add(issue)
        if record.get("resolution_state") in {"held", "unresolved"} and not any(x in record.get("continuation_or_revisit", "").lower() for x in ("revisit", "retry", "clearance")):
            errors.append(f"{issue}: held/unresolved item lacks revisit condition")
        for artifact in record.get("evidence_artifacts", []):
            kind, ref, proof = artifact.get("evidence_kind"), artifact.get("path_or_reference", ""), artifact.get("hash_or_test", "")
            if kind == "current_file":
                match = FILE_HASH.fullmatch(proof)
                path = resolved(ref)
                if not match:
                    errors.append(f"{issue}: malformed current-file hash {ref}")
                elif not path.is_file():
                    errors.append(f"{issue}: missing evidence file {path}")
                else:
                    if digest(path.read_bytes()) != match.group(1):
                        errors.append(f"{issue}: current-file hash mismatch {ref}")
                    if match.group(2) and path.stat().st_size != int(match.group(2)):
                        errors.append(f"{issue}: current-file byte mismatch {ref}")
            elif kind == "historical_hash":
                if not FILE_HASH.fullmatch(proof):
                    errors.append(f"{issue}: malformed historical hash {ref}")
            elif kind == "unavailable_historical_state":
                if not proof.startswith("UNAVAILABLE:") or len(proof) <= len("UNAVAILABLE:"):
                    errors.append(f"{issue}: unavailable state lacks explicit reason {ref}")
            elif kind == "external_url" and not ref.startswith(("http://", "https://")):
                errors.append(f"{issue}: malformed external URL {ref}")

    states = Counter(r["resolution_state"] for r in records)
    if metadata.get("append_only") is not True or metadata.get("record_count") != len(records):
        errors.append("metadata append/count mismatch")
    if metadata.get("chain_head_sha256") != previous or metadata.get("canonical_jsonl_sha256") != digest(LEDGER.read_bytes()):
        errors.append("metadata chain/canonical hash mismatch")
    if metadata.get("resolution_state_counts") != dict(states):
        errors.append("metadata state counts mismatch")

    correction = next((record for record in records if record.get("issue_id") == "CJK-KO-P29-U02-HARD-007"), None)
    if correction is None:
        errors.append("missing append-only decision-link correction HARD-007")
    else:
        if len(records) < 7 or records[6].get("issue_id") != "CJK-KO-P29-U02-HARD-007":
            errors.append("HARD-007 is not the seventh chained record")
        if set(correction.get("supersedes", [])) != set(PRIOR_IDS):
            errors.append("HARD-007 does not supersede exactly HARD-001 through HARD-006 metadata")
        if set(correction.get("related_decision_ids", [])) != {"CJK-KO-P29-001", "CJK-KO-P29-006"}:
            errors.append("HARD-007 lacks the exact claim plus substantive U02 decision links")
        if correction.get("supersession_state") != "corrects_prior":
            errors.append("HARD-007 supersession state is not corrects_prior")
        if "Supersede only their incomplete decision-link metadata" not in correction.get("resolution_or_workaround", ""):
            errors.append("HARD-007 does not limit supersession to decision-link metadata")
    for prior in records[:6]:
        if prior.get("related_decision_ids") != ["CJK-KO-P29-001"]:
            errors.append(f"{prior.get('issue_id')}: immutable original decision-link field changed")

    replay = next((record for record in records if record.get("issue_id") == "CJK-KO-P29-U02-HARD-008"), None)
    if replay is None:
        errors.append("missing append-only normalized authority-replay record HARD-008")
    else:
        if len(records) < 8 or records[7].get("issue_id") != "CJK-KO-P29-U02-HARD-008":
            errors.append("HARD-008 is not the eighth chained record")
        if replay.get("related_decision_ids") != ["CJK-KO-P29-006"]:
            errors.append("HARD-008 lacks the exact substantive U02 decision link")
        if replay.get("supersedes") != [] or replay.get("supersession_state") != "not_applicable":
            errors.append("HARD-008 incorrectly supersedes an earlier factual record")
        if "raw ordinal substring scan reported zero" not in replay.get("symptom", ""):
            errors.append("HARD-008 does not preserve the raw-scan failure")
        if "character offset 1,219,101" not in json.dumps(replay, ensure_ascii=False) or "offset 1,219,565" not in json.dumps(replay, ensure_ascii=False):
            errors.append("HARD-008 lacks both normalized character offsets")

    validator_history = next((record for record in records if record.get("issue_id") == "CJK-KO-P29-U02-HARD-009"), None)
    if validator_history is None:
        errors.append("missing append-only authority-validator failure-history record HARD-009")
    else:
        if records[-1].get("issue_id") != "CJK-KO-P29-U02-HARD-009":
            errors.append("HARD-009 is not the latest chained record")
        if validator_history.get("related_decision_ids") != ["CJK-KO-P29-006"]:
            errors.append("HARD-009 lacks the substantive U02 decision link")
        if validator_history.get("supersedes") != [] or validator_history.get("supersession_state") != "not_applicable":
            errors.append("HARD-009 incorrectly supersedes earlier records")
        unavailable = [artifact for artifact in validator_history.get("evidence_artifacts", []) if artifact.get("evidence_kind") == "unavailable_historical_state"]
        if len(unavailable) != 2 or any(not artifact.get("hash_or_test", "").startswith("UNAVAILABLE:patched in place before hashing") for artifact in unavailable):
            errors.append("HARD-009 does not honestly preserve both unavailable failed-script hashes")
        attempts = json.dumps(validator_history.get("attempted_approaches", []), ensure_ascii=False)
        for required in ("unterminated string literal", "whole-line-equality", "Path.read_text"):
            if required not in attempts and required not in json.dumps(validator_history, ensure_ascii=False):
                errors.append(f"HARD-009 lacks validator failure mode: {required}")

    with CSV_PATH.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle); csv_rows = list(reader); header = reader.fieldnames
    expected = [project(r) for r in records]
    if header != (list(expected[0]) if expected else []):
        errors.append("CSV header mismatch")
    if len(csv_rows) != len(expected):
        errors.append("CSV row count mismatch")
    else:
        for number, (actual, wanted) in enumerate(zip(csv_rows, expected), 2):
            if actual != wanted:
                errors.append(f"CSV row {number} mismatch: {[k for k in wanted if actual.get(k) != wanted[k]]}")

    # Assigned final source/target and exact cursor.
    full_path = TRANCHE / "source/Noether_Paper29_German_P31_Sealed_exact_slice.tex"
    source_path = TRANCHE / "source/Noether_Paper29_German_P31_U02_Rationalbasis_exact_lf.tex"
    full = full_path.read_text(encoding="utf-8-sig").splitlines()
    source = source_path.read_text(encoding="utf-8-sig").splitlines()
    if len(source) != 15 or full[24:39] != source or full[39] != "" or not full[40].startswith(r"2. \srcspaced{Beweis des Endlichkeitskriteriums.}"):
        errors.append("HARD-001 source boundary/cursor reproduction failed")
    needle = source_path.read_bytes().decode("utf-8")
    for label, path, expected_hash, expected_offset in (
        ("sealed", SEALED_AUTHORITY, "A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F", 1219101),
        ("candidate", UNSEALED_CANDIDATE, "5D159B7457F2ACBAD583C82D391476659101F9519E7A4B45C97D4BD8A48C7AFD", 1219565),
    ):
        if not path.is_file():
            errors.append(f"HARD-008 missing {label} cumulative source")
            continue
        raw_bytes = path.read_bytes()
        if digest(raw_bytes) != expected_hash:
            errors.append(f"HARD-008 {label} cumulative hash mismatch")
            continue
        raw_text = raw_bytes.decode("utf-8")
        normalized = raw_text.replace("\r\n", "\n").replace("\r", "\n")
        if raw_text.count(needle) != 0 or raw_text.find(needle) != -1:
            errors.append(f"HARD-008 {label} failed raw scan is not reproducible")
        if normalized.count(needle) != 1 or normalized.find(needle) != expected_offset:
            errors.append(f"HARD-008 {label} normalized count/offset mismatch")
    target_paths = {"tex": TRANCHE / "ko/Noether_Paper29_Korean_U02_v001.tex", "pdf": TRANCHE / "ko/Noether_Paper29_Korean_U02_v001.pdf", "png": TRANCHE / "visual_inspection/Noether_Paper29_Korean_U02_v001.png"}
    for kind, path in target_paths.items():
        if digest(path.read_bytes()) != EXPECTED_FINAL[kind]:
            errors.append(f"final target {kind} hash mismatch")
    if structural_meta.get("authority", {}).get("target_tex_sha256") != EXPECTED_FINAL["tex"]:
        errors.append("structural metadata final target hash mismatch")

    authority_report_path = TRANCHE / "qa/U02_AUTHORITY_VALIDATION.json"
    authority_report = json.loads(authority_report_path.read_text(encoding="utf-8"))
    report_occurrences = list(authority_report.get("authority_occurrences", {}).values())
    if authority_report.get("errors") != [] or len(report_occurrences) != 2:
        errors.append("HARD-009 final authority report is not a two-head zero-error pass")
    elif any(item.get("raw_ordinal_count") != 0 or item.get("lf_normalized_ordinal_count") != 1 for item in report_occurrences):
        errors.append("HARD-009 final authority report does not retain raw-zero/normalized-one counts")
    next_line = authority_report.get("cursor", {}).get("next_substantive_line", "")
    if not next_line.startswith(r"2. \srcspaced{Beweis des Endlichkeitskriteriums.}") or "Die Bedingung" not in next_line:
        errors.append("HARD-009 final authority report does not preserve prefix-plus-prose line 41")

    # Footnote and display parity after the stranded-marker repair.
    by_sid = {r["structural_id"]: r for r in structural}
    note = by_sid.get("NOE-P29-KO-U02-NOTE-002")
    if not note or note["target"]["locator"]["line_start"] != 30:
        errors.append("HARD-002 note-2 final locator is not target line 30")
    displays = [r for r in structural if r["unit_type"] == "display"]
    if len(displays) != 3 or [r["target"]["locator"]["line_start"] for r in displays] != [23, 31, 35]:
        errors.append("HARD-006 three-display parity locators mismatch")

    # Required historical evidence, including honest unavailable state.
    historical_hashes = set()
    unavailable_refs = []
    for record in records:
        for artifact in record.get("evidence_artifacts", []):
            match = FILE_HASH.fullmatch(artifact.get("hash_or_test", ""))
            if artifact.get("evidence_kind") == "historical_hash" and match:
                historical_hashes.add(match.group(1))
            if artifact.get("evidence_kind") == "unavailable_historical_state":
                unavailable_refs.append(artifact.get("path_or_reference", ""))
    required_historical = {
        "9487BDA552D89D5CFF995DB79B96DDFD7B8D72F30837933ADC612EFE6FAABAA2",
        "757942045B900ED62288C9B94986D4156114887A6C4A6E9C79FF79F57CBAD26D",
        "D396477CDA351685D4885692CAF518E7A99DCCCADF71B7F9CE321D69CFB9481D",
        "3745EE1BFA0551F4BE6F2681A966872AD0C65A2CD87057F3AB80915CB4DA3935",
    }
    if not required_historical.issubset(historical_hashes):
        errors.append(f"required historical hashes missing: {required_historical - historical_hashes}")
    if not any("stranded marker" in ref for ref in unavailable_refs):
        errors.append("overwritten stranded-marker state is not explicitly recorded as hash-unavailable")
    for rel, expected_hash in (("visual_inspection/Noether_Paper29_German_U02_control-1.png", "82BDD45D00170B83510D9E120D65106F84C95BCDE2F9729EBF8EC1C4F2DD149E"), ("visual_inspection/Noether_Paper29_German_U02_control-2.png", "8FF7B58292BB6576A84E8BCB9F0CBFA7FD2167BED686EA98FFFD87C96757C927")):
        if digest((TRANCHE / rel).read_bytes()) != expected_hash:
            errors.append(f"superseded German render hash mismatch: {rel}")

    if len(PdfReader(str(TRANCHE / "source/Noether_Paper29_German_P31_U02_control.pdf")).pages) != 1:
        errors.append("current compact German control is not one page")
    if len(PdfReader(str(target_paths["pdf"])).pages) != 1:
        errors.append("final Korean U02 PDF is not one page")
    log_text = (TRANCHE / "ko/Noether_Paper29_Korean_U02_v001.log").read_text(encoding="utf-8", errors="replace")
    warning_patterns = ("Underfull", "Overfull", "Missing character", "Undefined control", "Fatal error", "LaTeX Error")
    hits = [pattern for pattern in warning_patterns if pattern.lower() in log_text.lower()]
    if hits:
        errors.append(f"final Korean build warning-pattern hits: {hits}")

    print(f"issues={len(records)} states={dict(states)} csv_rows={len(csv_rows)} chain_head={previous} schema_errors={schema_error_count} warning_hits={len(hits)} total_errors={len(errors)}")
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
