#!/usr/bin/env python3
"""Append U03 visual-loss/reconstruction history without mutating the existing chain."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
LEDGER = HERE / "DIFFICULTY_LEDGER.jsonl"
NEW_ID = "CJK-KO-P29-U03-HARD-008"


def payload_hash(record: dict) -> str:
    payload = {key: value for key, value in record.items() if key != "record_hash"}
    encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest().upper()


records = [json.loads(line) for line in LEDGER.read_text(encoding="utf-8").splitlines() if line.strip()]
if any(record["difficulty_id"] == NEW_ID for record in records):
    print(json.dumps({"state": "already_present", "difficulty_id": NEW_ID}))
    raise SystemExit(0)

record = {
    "schema_version": "1.0.0",
    "difficulty_id": NEW_ID,
    "recorded_at": "2026-07-18T21:39:21+02:00",
    "time_precision": "second precision for durable batch recording; reconstruction occurred later in the same U03 closure interval",
    "work_unit": "P29-KO-U03",
    "authority": "sealed P31 A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F; exact U03 1CD2F142F472BE2A590EC8AACA45CEB49966A09FE803CC410D138B3F7BDE7458",
    "source_locator": "first Korean U03 render created from pre-review TeX",
    "target_locator": "evidence/visual_evidence_u03/reconstruction",
    "symptom": "The first visually inspected PNG was overwritten by the accepted rerender before its original binary was hashed or copied.",
    "cause_evidence": "The stable output filename was reused after translation refinements; only the exact pre-review TeX hash survived. The first reconstruction command also doubled the workdir-relative path and failed before producing any new artifact.",
    "attempted_approaches": [
        "Recovered the exact initial TeX from the durable production patch and verified SHA-256 379C3A064823F94FDACD2419F5BCF9DAA54002FC7AA99F99A231DA0DE5FBE877.",
        "First reconstruction command used an already-prefixed path under the reconstruction workdir and failed; no failed-state binary or hash exists.",
        "Retried with the correct workdir-relative filename, compiled twice, rendered at 180 DPI, and visually inspected the reconstruction."
    ],
    "rejected_approaches": [
        "Claim the reconstructed PNG is the unavailable overwritten original.",
        "Omit the lost visual state because a clean final render exists.",
        "Invent an original PNG hash."
    ],
    "state": "workaround",
    "resolution_or_hold": "Exact initial TeX survives and generated reconstruction PDF/PNG are archived with explicit reconstructed-not-original status; original PNG binary/hash remain unavailable.",
    "evidence_hashes_and_tests": [
        "reconstructed TeX 379C3A064823F94FDACD2419F5BCF9DAA54002FC7AA99F99A231DA0DE5FBE877 exact match to recorded initial TeX hash",
        "reconstructed PDF F271C3B61FA32468C5B4313D1ED62C62613B3347A5947C53C73CB96050CD72DE",
        "reconstructed PNG 5103667C63B1CB8B114F28C1A3E5316B03B0B91E493FABB095E1382BBE0DDC6E",
        "original overwritten PNG hash unavailable",
        "first failed reconstruction command produced no artifact; hash unavailable"
    ],
    "residual_risk": "Pixel identity with the overwritten original cannot be proven because no original render hash survives.",
    "recurrence_cues": [
        "A before/after render reuses one stable filename before the before-state is hashed.",
        "A reconstruction claim lacks a recorded expected render hash.",
        "A command path repeats the workdir prefix."
    ],
    "related_decision_ids": ["CJK-KO-P29-010"],
    "related_structural_ids": ["NOE-P29-KO-U03-ROOT-001", "NOE-P29-KO-U03-EQ-001", "NOE-P29-KO-U03-NOTE-001", "NOE-P29-KO-U03-NOTE-002"],
    "transferable_lesson": "Hash and copy every visual state before overwriting; when that fails, reconstruct only what can be proven and label unavailable identities honestly.",
    "revisit_condition": "Original first PNG is recovered from a cache or an expected historical render hash becomes available.",
    "previous_hash": records[-1]["record_hash"]
}
record["record_hash"] = payload_hash(record)
with LEDGER.open("a", encoding="utf-8", newline="\n") as stream:
    stream.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")
print(json.dumps({"state": "appended", "difficulty_id": NEW_ID, "record_hash": record["record_hash"]}))
