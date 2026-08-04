#!/usr/bin/env python3
"""Assemble the three non-overlapping Paper 40 Hans translation fragments.

This is a mechanical producer operation. It records bytes and segment order but
does not compare, review, validate, or approve the translations.
"""

from __future__ import annotations

from pathlib import Path
import hashlib
import json


ROOT = Path(__file__).resolve().parents[1]
SEGMENTS = ROOT / "segments"
TARGET_DIR = ROOT / "zh-Hans-CN"
TARGET = TARGET_DIR / "Noether_Paper40_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex"
RECORD = ROOT / "qa/HANS_ASSEMBLY_RECORD.json"

SOURCE_SEGMENTS = [
    (
        "segment_A_source_lines_001_213.tex",
        "FF916923952C33A97995C6C7AD098AF4037766B7FC3A781F4D41263B20919BED",
        [1, 213],
    ),
    (
        "segment_B_source_lines_214_446.tex",
        "1A057A1196950C6E3E4FC49C37A93F6966C2DDD1F344125ACFC4D899289B4F7E",
        [214, 446],
    ),
    (
        "segment_C_source_lines_447_648.tex",
        "5D510253EA3A90C673204122BB447D164FA2A08682EB2A1D52C9D4EB99AC4B4B",
        [447, 648],
    ),
]

TRANSLATION_SEGMENTS = [
    "segment_A_zh-Hans-CN.tex",
    "segment_B_zh-Hans-CN.tex",
    "segment_C_zh-Hans-CN.tex",
]


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def read(path: Path) -> bytes:
    if not path.is_file():
        raise FileNotFoundError(path)
    return path.read_bytes()


source_records = []
for name, expected_hash, source_lines in SOURCE_SEGMENTS:
    path = SEGMENTS / name
    data = read(path)
    actual_hash = sha_bytes(data)
    if actual_hash != expected_hash:
        raise RuntimeError(
            f"Source segment changed: {name}: expected {expected_hash}, found {actual_hash}"
        )
    source_records.append(
        {
            "path": str(path),
            "source_lines": source_lines,
            "bytes": len(data),
            "sha256": actual_hash,
        }
    )

component_paths = [
    SEGMENTS / "P40_STANDALONE_PREAMBLE.tex",
    *(SEGMENTS / name for name in TRANSLATION_SEGMENTS),
    SEGMENTS / "P40_STANDALONE_POSTAMBLE.tex",
]

parts = []
component_records = []
for path in component_paths:
    data = read(path)
    parts.append(data if data.endswith(b"\n") else data + b"\n")
    component_records.append(
        {"path": str(path), "bytes": len(data), "sha256": sha_bytes(data)}
    )

output = b"".join(parts)
TARGET_DIR.mkdir(parents=True, exist_ok=True)
TARGET.write_bytes(output)

record = {
    "schema_version": "1.0.0",
    "work_id": "NOETHER-P40",
    "operation": "mechanical_hans_segment_assembly",
    "source_interval_sha256":
        "7965805D3A75C3354C85BC7A3E4725F07BF869A8833FC19D74E32BE369427937",
    "source_segments": source_records,
    "translation_components_in_order": component_records,
    "output_path": str(TARGET),
    "output_bytes": len(output),
    "output_sha256": sha_bytes(output),
    "review_state": "independent check pending",
    "claim_limit": (
        "Mechanical ordering, concatenation, byte counts, and hashes only; "
        "no source, translation, formula, terminology, visual, regional, human, "
        "external, archive, publication, or certification validation."
    ),
}
RECORD.write_text(
    json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(record, ensure_ascii=True, indent=2))
