#!/usr/bin/env python3
"""Mechanically assemble four non-overlapping Paper 43 Hans fragments."""

from pathlib import Path
import hashlib
import json


ROOT = Path(__file__).resolve().parents[1]
SEGMENTS = ROOT / "segments"
TARGET_DIR = ROOT / "zh-Hans-CN"
TARGET = TARGET_DIR / "Noether_Paper43_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex"
RECORD = ROOT / "qa/HANS_ASSEMBLY_RECORD.json"

SOURCE_SEGMENTS = [
    ("prod_segment_A_source_lines_001_197.tex", "B8D26391C1AC7371E4778D1E78BDE37AF9C930549BF4C453E4DA8D55C76A96A3", [1, 197]),
    ("prod_segment_B_source_lines_198_427.tex", "8E76626F92CF250A6E903C745131A553B700760CEE64D93C65CBC9E7FDFE9C96", [198, 427]),
    ("prod_segment_C_source_lines_428_611.tex", "F51B496A6D1928362F96B36F992D5062A7ABD427F41FC9D2FB5E7BC5C1DD6995", [428, 611]),
    ("prod_segment_D_source_lines_612_811.tex", "0CAC2A241CACE25013E5E765A1B4E84556DCDB9CF3CC7E93CC30297B130869C9", [612, 811]),
]

TRANSLATION_SEGMENTS = [
    "prod_segment_A_zh-Hans-CN.tex",
    "prod_segment_B_zh-Hans-CN.tex",
    "prod_segment_C_zh-Hans-CN.tex",
    "prod_segment_D_zh-Hans-CN.tex",
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
        {"path": str(path), "source_lines": source_lines, "bytes": len(data), "sha256": actual_hash}
    )

component_paths = [
    SEGMENTS / "P43_STANDALONE_PREAMBLE.tex",
    *(SEGMENTS / name for name in TRANSLATION_SEGMENTS),
    SEGMENTS / "P43_STANDALONE_POSTAMBLE.tex",
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
    "work_id": "NOETHER-P43",
    "operation": "mechanical_hans_segment_assembly",
    "source_interval_sha256": "657799FA62D58538E6AFC810221DE2C9E1F7DC481E7DDEF2CAD76506DDEB8176",
    "source_segments": source_records,
    "translation_components_in_order": component_records,
    "output_path": str(TARGET),
    "output_bytes": len(output),
    "output_sha256": sha_bytes(output),
    "review_state": "independent check pending",
    "claim_limit": (
        "Mechanical ordering, concatenation, byte counts, and hashes only; no source, "
        "translation, formula, terminology, visual, regional, human, external, archive, "
        "publication, or certification validation."
    ),
}
RECORD.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(record, ensure_ascii=True, indent=2))
