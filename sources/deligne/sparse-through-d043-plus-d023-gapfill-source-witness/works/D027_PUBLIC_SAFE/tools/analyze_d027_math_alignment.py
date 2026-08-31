#!/usr/bin/env python3
"""Produce a page-wise EN/FR mathematical-alignment report for D027."""

from __future__ import annotations

import argparse
import csv
import json
import re
from difflib import SequenceMatcher
from pathlib import Path


INLINE_RE = re.compile(r"\\\((.*?)\\\)", re.DOTALL)
DISPLAY_RE = re.compile(r"\\\[(.*?)\\\]", re.DOTALL)


def read_rows(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def replace_balanced_command(text: str, command: str) -> str:
    marker = command + "{"
    start = 0
    pieces: list[str] = []
    while True:
        index = text.find(marker, start)
        if index < 0:
            pieces.append(text[start:])
            return "".join(pieces)
        pieces.append(text[start:index])
        depth = 1
        cursor = index + len(marker)
        while cursor < len(text) and depth:
            if text[cursor] == "{" and (cursor == 0 or text[cursor - 1] != "\\"):
                depth += 1
            elif text[cursor] == "}" and (cursor == 0 or text[cursor - 1] != "\\"):
                depth -= 1
            cursor += 1
        if depth:
            raise ValueError(f"unbalanced {command} group")
        pieces.append(r"\TEXT{}")
        start = cursor


def formula_skeleton(text: str) -> str:
    normalized = text
    for command in (r"\text", r"\mathrm"):
        normalized = replace_balanced_command(normalized, command)
    normalized = re.sub(r"\s+", "", normalized)
    normalized = re.sub(r"[,.;:]+$", "", normalized)
    return normalized


def clean_cell(text: str) -> str:
    return text.replace("\r", "").replace("\n", r"\n").replace("\t", " ")


def align_layer(kind: str, page: int, source: list[str], french: list[str]) -> list[dict]:
    source_signatures = [formula_skeleton(item) for item in source]
    french_signatures = [formula_skeleton(item) for item in french]
    matcher = SequenceMatcher(a=source_signatures, b=french_signatures, autojunk=False)
    findings: list[dict] = []
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            continue
        span = max(i2 - i1, j2 - j1)
        for offset in range(span):
            source_index = i1 + offset if i1 + offset < i2 else None
            french_index = j1 + offset if j1 + offset < j2 else None
            source_value = source[source_index] if source_index is not None else ""
            french_value = french[french_index] if french_index is not None else ""
            findings.append(
                {
                    "physical_page": page,
                    "kind": kind,
                    "opcode": tag,
                    "source_index": "" if source_index is None else source_index + 1,
                    "french_index": "" if french_index is None else french_index + 1,
                    "source_formula": clean_cell(source_value),
                    "french_formula": clean_cell(french_value),
                    "source_skeleton": clean_cell(formula_skeleton(source_value)),
                    "french_skeleton": clean_cell(formula_skeleton(french_value)),
                    "review_status": "REQUIRES_HUMAN_REVIEW",
                    "review_note": "",
                }
            )
    return findings


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--edition-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    source_rows = read_rows(args.edition_dir / "source_language.ndjson")
    french_rows = read_rows(args.edition_dir / "french_translation.ndjson")
    if [row["physical_page"] for row in source_rows] != [row["physical_page"] for row in french_rows]:
        raise ValueError("EN/FR page topology mismatch")

    findings: list[dict] = []
    totals = {"inline_source": 0, "inline_french": 0, "display_source": 0, "display_french": 0}
    for source_row, french_row in zip(source_rows, french_rows):
        page = int(source_row["physical_page"])
        source_inline = INLINE_RE.findall(source_row["text"])
        french_inline = INLINE_RE.findall(french_row["text"])
        source_display = DISPLAY_RE.findall(source_row["text"])
        french_display = DISPLAY_RE.findall(french_row["text"])
        totals["inline_source"] += len(source_inline)
        totals["inline_french"] += len(french_inline)
        totals["display_source"] += len(source_display)
        totals["display_french"] += len(french_display)
        findings.extend(align_layer("INLINE", page, source_inline, french_inline))
        findings.extend(align_layer("DISPLAY", page, source_display, french_display))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "physical_page",
        "kind",
        "opcode",
        "source_index",
        "french_index",
        "source_formula",
        "french_formula",
        "source_skeleton",
        "french_skeleton",
        "review_status",
        "review_note",
    ]
    with args.output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(findings)
    print(json.dumps({"totals": totals, "findings": len(findings), "output": str(args.output)}, sort_keys=True))


if __name__ == "__main__":
    main()
