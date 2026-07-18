#!/usr/bin/env python3
"""Report gross structural parity for R823 Papers 1--43.

This is an omission detector, not a bilingual-quality judgment.  It compares
non-comment TeX volume and display structure after expanding the target's local
inputs.  A passing row still requires source-keyed linguistic review.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
from dataclasses import asdict, dataclass
from pathlib import Path

from noether_r823_book_structure_audit import (
    COMMANDS,
    DISPLAY,
    DISPLAY_ROWS,
    INLINE_MATH,
    R823_TEX_SHA256,
    count,
    uncommented_length,
)
from noether_r823_target_unit_manifest import expand_tex
from noether_r823_target_unit_manifest import MARKERS, locate_any
from noether_sync_audit import mask_tex_comments, slice_papers


@dataclass
class PaperAudit:
    authority_sha256: str
    target_document_sha256: str
    paper: int
    source_chars: int
    target_chars: int
    char_ratio: str
    source_displays: int
    target_displays: int
    source_display_rows: int
    target_display_rows: int
    source_inline_math_openers: int
    target_inline_math_openers: int
    source_math_tokens: int
    target_math_tokens: int
    math_token_ratio: str
    source_commands: int
    target_commands: int
    status: str
    note: str


MATH_ENV = re.compile(
    r"\\begin\{(equation\*?|align\*?|alignat\*?|gather\*?|multline\*?|displaymath)\}"
    r"(.*?)\\end\{\1\}",
    re.DOTALL,
)
MATH_BRACKET = re.compile(r"(?<!\\)\\\[(.*?)\\\]|\\\((.*?)\\\)", re.DOTALL)
MATH_DOLLAR = re.compile(r"(?<!\\)\$(?!\$)(.*?)(?<!\\)\$", re.DOTALL)
MATH_TOKEN = re.compile(r"\\[A-Za-z@]+|[A-Za-zÀ-ÖØ-öø-ÿ]+|\d+|[^\s]", re.UNICODE)


def math_token_count(text: str) -> int:
    """Count math-span tokens independent of inline/display presentation."""
    spans = [match.group(2) for match in MATH_ENV.finditer(text)]
    spans.extend(
        match.group(1) if match.group(1) is not None else match.group(2)
        for match in MATH_BRACKET.finditer(text)
    )
    spans.extend(match.group(1) for match in MATH_DOLLAR.finditer(text))
    return len(MATH_TOKEN.findall(" ".join(spans)))


def audit(source: str, target: str, language: str) -> list[PaperAudit]:
    authority_hash = hashlib.sha256(source.encode("utf-8")).hexdigest().upper()
    target_hash = hashlib.sha256(target.encode("utf-8")).hexdigest().upper()
    source_papers = slice_papers(source)
    target_papers = slice_papers(target)
    source_book_title = mask_tex_comments(source).find(
        "Algebra der hyperkomplexen Größen",
        source_papers[43].start,
    )
    if source_book_title < 0:
        raise ValueError("R823 long-form book title not found after Paper 43")
    source_book_start = source.rfind("\n", 0, source_book_title) + 1
    target_book_start = locate_any(
        target,
        MARKERS[language]["book"],
        target_papers[43].start,
        "book",
    )
    rows: list[PaperAudit] = []

    for number in range(1, 44):
        source_text = (
            source[source_papers[number].start : source_book_start]
            if number == 43
            else source_papers[number].text
        )
        target_text = (
            target[target_papers[number].start : target_book_start]
            if number == 43
            else target_papers[number].text
        )
        source_chars = uncommented_length(source_text)
        target_chars = uncommented_length(target_text)
        ratio = target_chars / source_chars if source_chars else 0.0
        source_displays = count(DISPLAY, source_text)
        target_displays = count(DISPLAY, target_text)
        source_display_structure = source_displays + count(DISPLAY_ROWS, source_text)
        target_display_structure = target_displays + count(DISPLAY_ROWS, target_text)
        source_math_tokens = math_token_count(source_text)
        target_math_tokens = math_token_count(target_text)
        math_ratio = target_math_tokens / source_math_tokens if source_math_tokens else 1.0

        notes: list[str] = []
        if ratio < 0.65:
            notes.append(f"target/source non-comment character ratio {ratio:.2f} below 0.65")
        if source_math_tokens >= 20 and math_ratio < 0.70:
            notes.append(f"target/source math-token ratio {math_ratio:.2f} below 0.70")
        if source_displays >= 3 and target_displays / source_displays < 0.50:
            notes.append(
                "target/source display-block ratio "
                f"{target_displays / source_displays:.2f} below 0.50"
            )
        if (
            ratio < 0.80
            and source_display_structure
            and target_display_structure / source_display_structure < 0.70
        ):
            notes.append(
                "target/source display-structure ratio "
                f"{target_display_structure / source_display_structure:.2f} below 0.70"
            )
        status = "gross-structural-risk" if notes else "present-structural-review"

        rows.append(
            PaperAudit(
                authority_sha256=authority_hash,
                target_document_sha256=target_hash,
                paper=number,
                source_chars=source_chars,
                target_chars=target_chars,
                char_ratio=f"{ratio:.4f}",
                source_displays=source_displays,
                target_displays=target_displays,
                source_display_rows=count(DISPLAY_ROWS, source_text),
                target_display_rows=count(DISPLAY_ROWS, target_text),
                source_inline_math_openers=count(INLINE_MATH, source_text),
                target_inline_math_openers=count(INLINE_MATH, target_text),
                source_math_tokens=source_math_tokens,
                target_math_tokens=target_math_tokens,
                math_token_ratio=f"{math_ratio:.4f}",
                source_commands=count(COMMANDS, source_text),
                target_commands=count(COMMANDS, target_text),
                status=status,
                note="; ".join(notes),
            )
        )
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--language", choices=tuple(MARKERS), required=True)
    parser.add_argument("--authority-tex", type=Path, required=True)
    parser.add_argument("--target-tex", type=Path, required=True)
    parser.add_argument("--output-csv", type=Path, required=True)
    args = parser.parse_args()

    authority_hash = hashlib.sha256(args.authority_tex.read_bytes()).hexdigest().upper()
    if authority_hash != R823_TEX_SHA256:
        raise ValueError(
            f"authority hash mismatch: found {authority_hash}; expected {R823_TEX_SHA256}"
        )
    target, dependencies, warnings = expand_tex(args.target_tex)
    if warnings:
        raise ValueError("; ".join(warnings))
    rows = audit(args.authority_tex.read_text(encoding="utf-8"), target, args.language)
    args.output_csv.parent.mkdir(parents=True, exist_ok=True)
    with args.output_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(asdict(rows[0])))
        writer.writeheader()
        writer.writerows(asdict(row) for row in rows)

    counts: dict[str, int] = {}
    for row in rows:
        counts[row.status] = counts.get(row.status, 0) + 1
    print(f"expanded {len(dependencies)} target TeX files")
    print(f"wrote {args.output_csv}")
    for status in ("present-structural-review", "gross-structural-risk"):
        print(f"{status}: {counts.get(status, 0)}")
    return 0 if counts.get("gross-structural-risk", 0) == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
