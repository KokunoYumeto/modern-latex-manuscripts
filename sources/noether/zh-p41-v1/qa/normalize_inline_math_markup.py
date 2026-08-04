#!/usr/bin/env python3
r"""Mechanically normalize parenthesized inline math in the Paper 41 Hans TeX.

The producer draft inherited plain-parenthesis notation such as ``(\mathfrak G)``.
This formatter changes only TeX math delimiters. It performs no linguistic,
semantic, source, or visual checking.
"""

from pathlib import Path
import hashlib
import json
import re


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "zh-Hans-CN/Noether_Paper41_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex"
RECORD = ROOT / "qa/INLINE_MATH_MARKUP_RECORD.json"
EXPECTED_INPUT_SHA256 = "95679E6C6EC9E67C1A3670A36A4D5428DDFC167FA97361D6698799ABF6AFEC3F"


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


MATH_TOKENS = (
    "_", "^", "=", "\\mathfrak", "\\overline", "\\bar", "\\sum",
    "\\prod", "\\frac", "\\in", "\\sim", "\\mapsto", "\\longmapsto",
    "\\alpha", "\\beta", "\\gamma", "\\delta", "\\varepsilon",
    "\\lambda", "\\mu", "\\nu", "\\xi", "\\rho", "\\sigma",
    "\\tau", "\\ell", "\\ldots", "\\cdots", "\\{", "\\}",
    "\\cdot", "\\subset", "\\supset", "\\not", "\\operatorname",
)


def looks_math(value: str) -> bool:
    stripped = value.strip()
    if not stripped:
        return False
    if any(token in stripped for token in MATH_TOKENS):
        return True
    if re.fullmatch(r"[A-Za-z]", stripped):
        return True
    if re.fullmatch(r"[A-Za-z][A-Za-z0-9]*(?:/[A-Za-z][A-Za-z0-9]*)+", stripped):
        return True
    if re.fullmatch(r"[A-Za-z](?:,[A-Za-z])+", stripped):
        return True
    if re.search(r"[A-Za-z].*[+*/<>-]|[+*/<>-].*[A-Za-z]", stripped):
        return True
    return False


def process_segment(value: str) -> tuple[str, int]:
    out: list[str] = []
    changes = 0
    i = 0
    while i < len(value):
        if value.startswith(r"\(", i):
            end = value.find(r"\)", i + 2)
            if end < 0:
                out.append(value[i:])
                break
            out.append(value[i:end + 2])
            i = end + 2
            continue
        if value[i] == "$" and (i == 0 or value[i - 1] != "\\"):
            end = i + 1
            while end < len(value):
                if value[end] == "$" and value[end - 1] != "\\":
                    break
                end += 1
            if end >= len(value):
                out.append(value[i:])
                break
            out.append(value[i:end + 1])
            i = end + 1
            continue
        if value[i] == "(" and (i == 0 or value[i - 1] != "\\"):
            depth = 1
            end = i + 1
            escaped_close = False
            while end < len(value):
                if value.startswith(r"\(", end):
                    inline_end = value.find(r"\)", end + 2)
                    if inline_end < 0:
                        break
                    end = inline_end + 2
                    continue
                if value.startswith(r"\)", end) and depth == 1:
                    escaped_close = True
                    break
                if value[end] == "(" and value[end - 1] != "\\":
                    depth += 1
                elif value[end] == ")" and value[end - 1] != "\\":
                    depth -= 1
                    if depth == 0:
                        break
                end += 1
            if end >= len(value):
                out.append(value[i])
                i += 1
                continue
            content = value[i + 1:end]
            processed, nested_changes = process_segment(content)
            changes += nested_changes
            if looks_math(content):
                out.append(r"\(" + processed + r"\)")
                changes += 1
            else:
                out.append("(" + processed + ("" if escaped_close else ")"))
                if escaped_close:
                    out.append(r"\)")
            i = end + (2 if escaped_close else 1)
            continue
        out.append(value[i])
        i += 1
    return "".join(out), changes


input_bytes = TARGET.read_bytes()
input_sha = sha_bytes(input_bytes)
if input_sha != EXPECTED_INPUT_SHA256:
    raise RuntimeError(f"Input changed: expected {EXPECTED_INPUT_SHA256}, found {input_sha}")

lines = input_bytes.decode("utf-8").splitlines(keepends=True)
result: list[str] = []
display_math = False
change_count = 0
for line in lines:
    stripped = line.lstrip()
    if display_math:
        result.append(line)
        if r"\]" in line:
            display_math = False
        continue
    if stripped.startswith(r"\["):
        display_math = r"\]" not in stripped[2:]
        result.append(line)
        continue
    if stripped.startswith(r"\srcnumdisplay"):
        result.append(line)
        continue
    normalized, count = process_segment(line)
    result.append(normalized)
    change_count += count

output_text = "".join(result)
TARGET.write_text(output_text, encoding="utf-8", newline="\n")
output_sha = sha_bytes(TARGET.read_bytes())

record = {
    "work_id": "NOETHER-P41",
    "operation": "mechanical_inline_math_delimiter_normalization",
    "input_sha256": input_sha,
    "output_sha256": output_sha,
    "parenthesized_spans_changed": change_count,
    "claim_limit": "TeX delimiter formatting only; no linguistic, semantic, source, or visual checking.",
}
RECORD.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
print(json.dumps(record, indent=2))
