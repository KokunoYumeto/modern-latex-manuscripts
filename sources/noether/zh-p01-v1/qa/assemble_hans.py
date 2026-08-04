#!/usr/bin/env python3
"""Mechanically assemble three non-overlapping Paper 1 Hans fragments."""

from pathlib import Path
import hashlib
import json


ROOT = Path(__file__).resolve().parents[1]
SEGMENTS = ROOT / "segments"
TARGET_DIR = ROOT / "zh-Hans-CN"
TARGET = TARGET_DIR / "Noether_Paper01_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex"
RECORD = ROOT / "qa/HANS_ASSEMBLY_RECORD.json"

SOURCE_SEGMENTS = [
    ("prod_segment_A_source_lines_001_024.tex", "4FAFC711A18FBE0B9C328DB74E8FB8BD88D46B168F2446B84310222014409AAE", [1, 24]),
    ("prod_segment_B_source_lines_025_059.tex", "52BA4686D0C7DEBF68ECF9D4811971B31DA89E86369EB4DF1C010BFEF5AF67CA", [25, 59]),
    ("prod_segment_C_source_lines_060_080.tex", "5642B68567271B6E3236371ECDE02E67C514499AA53EBE728BCCDA47E5D38BF3", [60, 80]),
]

TRANSLATION_SEGMENTS = [
    "prod_segment_A_zh-Hans-CN.tex",
    "prod_segment_B_zh-Hans-CN.tex",
    "prod_segment_C_zh-Hans-CN.tex",
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
        raise RuntimeError(f"Source segment changed: {name}: expected {expected_hash}, found {actual_hash}")
    source_records.append({"path": str(path), "source_lines": source_lines, "bytes": len(data), "sha256": actual_hash})

component_paths = [
    SEGMENTS / "P01_STANDALONE_PREAMBLE.tex",
    *(SEGMENTS / name for name in TRANSLATION_SEGMENTS),
    SEGMENTS / "P01_STANDALONE_POSTAMBLE.tex",
]

parts = []
component_records = []
for path in component_paths:
    data = read(path)
    parts.append(data if data.endswith(b"\n") else data + b"\n")
    component_records.append({"path": str(path), "bytes": len(data), "sha256": sha_bytes(data)})

output = b"".join(parts)
TARGET_DIR.mkdir(parents=True, exist_ok=True)
TARGET.write_bytes(output)

record = {
    "schema_version": "1.0.0",
    "work_id": "NOETHER-P01",
    "operation": "mechanical_hans_segment_assembly",
    "source_interval_sha256": "0499985866E646747EC31533775FF31B55556F2C694F4C2608384829DE248D2F",
    "source_segments": source_records,
    "translation_components_in_order": component_records,
    "output_path": str(TARGET),
    "output_bytes": len(output),
    "output_sha256": sha_bytes(output),
    "review_state": "independent check pending",
    "claim_limit": "Mechanical ordering, concatenation, byte counts, and hashes only; no source, translation, formula, terminology, visual, regional, human, external, archive, publication, or certification validation.",
}
RECORD.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(record, ensure_ascii=True, indent=2))
