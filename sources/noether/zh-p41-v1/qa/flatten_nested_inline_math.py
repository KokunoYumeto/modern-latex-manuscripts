#!/usr/bin/env python3
r"""Flatten mechanically introduced nested ``\(...\)`` delimiters in P41."""

from pathlib import Path
import hashlib
import json


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "zh-Hans-CN/Noether_Paper41_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex"
RECORD = ROOT / "qa/INLINE_MATH_NESTING_RECORD.json"
EXPECTED_INPUT_SHA256 = "46F63B97E81D770818397DA536D7F0A9802B5FC16440D4E161056ADF18D74EE2"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


source = TARGET.read_bytes()
source_sha = sha(source)
if source_sha != EXPECTED_INPUT_SHA256:
    raise RuntimeError(f"Input changed: expected {EXPECTED_INPUT_SHA256}, found {source_sha}")

text = source.decode("utf-8")
out: list[str] = []
depth = 0
i = 0
nested_opens = 0
nested_closes = 0
while i < len(text):
    if text.startswith(r"\(", i):
        if depth == 0:
            out.append(r"\(")
        else:
            out.append("(")
            nested_opens += 1
        depth += 1
        i += 2
        continue
    if text.startswith(r"\)", i):
        if depth > 1:
            out.append(")")
            nested_closes += 1
            depth -= 1
        elif depth == 1:
            out.append(r"\)")
            depth = 0
        else:
            out.append(r"\)")
        i += 2
        continue
    out.append(text[i])
    i += 1

if depth != 0:
    raise RuntimeError(f"Unbalanced inline-math depth after scan: {depth}")

TARGET.write_text("".join(out), encoding="utf-8", newline="\n")
output_sha = sha(TARGET.read_bytes())
record = {
    "work_id": "NOETHER-P41",
    "operation": "mechanical_nested_inline_math_flattening",
    "input_sha256": source_sha,
    "output_sha256": output_sha,
    "nested_opens_flattened": nested_opens,
    "nested_closes_flattened": nested_closes,
    "claim_limit": "TeX delimiter formatting only; no linguistic, semantic, source, or visual checking.",
}
RECORD.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
print(json.dumps(record, indent=2))
