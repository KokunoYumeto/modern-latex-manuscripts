#!/usr/bin/env python3
"""Mechanically concatenate the frozen Paper 35 Hans producer segments."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
import hashlib
import json


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = Path(__file__).resolve()
PREAMBLE = ROOT / "controls/P35_STANDALONE_PREAMBLE.tex"
SEGMENTS = [
    ROOT / "translation/current_segments/P35_A_zh-Hans-CN_current.tex",
    ROOT / "translation/current_segments/P35_B_zh-Hans-CN_current.tex",
    ROOT / "translation/current_segments/P35_C_zh-Hans-CN_current.tex",
]
POSTAMBLE = ROOT / "controls/P35_STANDALONE_POSTAMBLE.tex"
TARGET_DIR = ROOT / "build/zh-Hans-CN"
TARGET = TARGET_DIR / "Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex"
RECORD = ROOT / "controls/HANS_ASSEMBLY_RECORD.json"
SOURCE_RECORD = ROOT / "controls/SOURCE_SEGMENTATION_RECORD.json"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def meta(path: Path) -> dict[str, object]:
    return {
        "path": str(path.relative_to(ROOT)).replace("\\", "/"),
        "bytes": len(path.read_bytes()),
        "sha256": sha(path),
    }


inputs = [PREAMBLE, *SEGMENTS, POSTAMBLE]
missing = [str(path) for path in inputs if not path.is_file()]
if missing:
    raise FileNotFoundError("Missing assembly inputs: " + "; ".join(missing))

pieces: list[str] = []
for path in inputs:
    value = path.read_text(encoding="utf-8")
    pieces.append(value if value.endswith("\n") else value + "\n")
assembled = "".join(pieces)

TARGET_DIR.mkdir(parents=True, exist_ok=True)
TARGET.write_text(assembled, encoding="utf-8", newline="\n")

record = {
    "schema_version": "1.0.0",
    "work_id": "NOETHER-P35-ZH",
    "operation": "producer_only_segment_concatenation",
    "recorded_at": datetime.now().astimezone().isoformat(timespec="seconds"),
    "decision_id": "ZH-D120",
    "script": meta(SCRIPT),
    "source_segmentation_record": meta(SOURCE_RECORD),
    "inputs_in_order": [meta(path) for path in inputs],
    "output": meta(TARGET),
    "target_scope": "PRC-oriented Simplified Chinese producer translation",
    "review_state": "independent check pending",
    "claim_limit": (
        "Mechanical concatenation and file identity only; no source, linguistic, semantic, "
        "formula-content, terminology, visual, regional, human, external, archive, "
        "publication, approval, or certification validation."
    ),
}
RECORD.write_text(
    json.dumps(record, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
    newline="\n",
)
print(json.dumps(record, ensure_ascii=True, indent=2))

