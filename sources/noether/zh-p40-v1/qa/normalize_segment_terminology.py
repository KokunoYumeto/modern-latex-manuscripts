#!/usr/bin/env python3
"""Apply two explicit cross-segment Paper 40 producer terminology decisions.

This is an editorial translation-production normalization, not a source or
translation check. It operates only on the declared segment files and fails
closed on input-hash or replacement-count drift.
"""

from pathlib import Path
import hashlib
import json


ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / "qa/TERMINOLOGY_NORMALIZATION_RECORD.json"

OPERATIONS = [
    {
        "path": ROOT / "segments/segment_A_zh-Hans-CN.tex",
        "expected_input_sha256":
            "C5E4551ACB2D011C5C5B06562AEB66FB251531A14FE0D091CFCA8FA94EAA525E",
        "old": "分出域",
        "new": "析出域",
        "expected_count": 2,
        "motivation": "Use one Paper-40 term for Abspaltungskörper across A and C.",
    },
    {
        "path": ROOT / "segments/segment_B_zh-Hans-CN.tex",
        "expected_input_sha256":
            "929FB13B6B2DC412A78C2998863CAE8F34C4526EAD8BC8C127FAE2EFD5673615",
        "old": "斜域",
        "new": "除环",
        "expected_count": 42,
        "motivation": (
            "Use one Paper-40 term for historical noncommutative Körper/division-ring "
            "contexts across A, B, and C; explicitly commutative 域 wording is untouched."
        ),
    },
]


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


records = []
for operation in OPERATIONS:
    path = operation["path"]
    raw = path.read_bytes()
    input_hash = digest(raw)
    if input_hash != operation["expected_input_sha256"]:
        raise RuntimeError(
            f"Input drift for {path}: expected {operation['expected_input_sha256']}, "
            f"found {input_hash}"
        )
    text = raw.decode("utf-8")
    count = text.count(operation["old"])
    if count != operation["expected_count"]:
        raise RuntimeError(
            f"Replacement-count drift for {path}: expected {operation['expected_count']}, "
            f"found {count}"
        )
    output = text.replace(operation["old"], operation["new"]).encode("utf-8")
    path.write_bytes(output)
    records.append(
        {
            "path": str(path),
            "input_sha256": input_hash,
            "output_sha256": digest(output),
            "old": operation["old"],
            "new": operation["new"],
            "replacement_count": count,
            "motivation": operation["motivation"],
        }
    )

record = {
    "schema_version": "1.0.0",
    "work_id": "NOETHER-P40",
    "operation": "explicit_cross_segment_producer_terminology_normalization",
    "operations": records,
    "epistemic_status": "editorial translation-production choice",
    "review_state": "independent check pending",
    "claim_limit": (
        "Exact-string replacement counts and hashes only; no source, semantic, formula, "
        "terminology, visual, regional, human, external, archive, publication, or "
        "certification validation."
    ),
}
RECORD.write_text(
    json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(record, ensure_ascii=True, indent=2))
