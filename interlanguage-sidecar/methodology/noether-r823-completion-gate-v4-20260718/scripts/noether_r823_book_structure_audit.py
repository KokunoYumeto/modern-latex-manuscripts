#!/usr/bin/env python3
"""Report gross structural parity for the 31-section R823 long-form book.

This verifier is intentionally narrower than linguistic review.  It detects
missing or suspiciously compressed sections and compares TeX display structure;
it never treats similar counts as proof of translation accuracy.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
from dataclasses import dataclass, asdict
from pathlib import Path

from noether_sync_audit import mask_tex_comments


R823_TEX_SHA256 = "EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21"
SOURCE_BOOK_START = r"\section*{Einleitung}\label{einleitung}"
SOURCE_BOOK_END = r"\subsection*{Notwendige und hinreichende Multiplizitätsbedingungen"
SUBSECTION_LINE = re.compile(r"^\\subsection\*\{[^\r\n]+", re.MULTILINE)
SECTION_NUMBER = re.compile(r"(?:§|\\S)[^0-9\r\n]{0,20}([1-9]|[12][0-9]|3[01])\.")
DISPLAY = re.compile(
    r"(?<!\\)\\\[|\\begin\{(?:equation\*?|align\*?|alignat\*?|gather\*?|"
    r"multline\*?|displaymath)\}"
)
DISPLAY_ROWS = re.compile(r"\\\\(?:\[[^\]]*\])?")
INLINE_MATH = re.compile(r"\\\(|(?<!\\)\$(?!\$)")
COMMANDS = re.compile(r"\\[A-Za-z@]+")


@dataclass
class SectionAudit:
    authority_sha256: str
    target_document_sha256: str
    section: int
    source_chars: int
    target_chars: int
    char_ratio: str
    source_displays: int
    target_displays: int
    source_display_rows: int
    target_display_rows: int
    source_inline_math_openers: int
    target_inline_math_openers: int
    source_commands: int
    target_commands: int
    status: str
    note: str


def uncommented_length(text: str) -> int:
    kept: list[str] = []
    for raw in text.splitlines():
        line = re.sub(r"(?<!\\)%.*$", "", raw).strip()
        if line:
            kept.append(line)
    return len(" ".join(kept))


def source_book(text: str) -> str:
    structural_text = mask_tex_comments(text)
    start = structural_text.find(SOURCE_BOOK_START)
    if start < 0:
        raise ValueError(f"R823 book start marker not found: {SOURCE_BOOK_START}")
    end = structural_text.find(SOURCE_BOOK_END, start)
    if end < 0:
        raise ValueError(f"R823 book end marker not found: {SOURCE_BOOK_END}")
    return text[start:end]


def section_slices(text: str) -> dict[int, str]:
    structural_text = mask_tex_comments(text)
    markers: list[tuple[int, int]] = []
    for heading in SUBSECTION_LINE.finditer(structural_text):
        number_match = SECTION_NUMBER.search(heading.group(0))
        if number_match:
            markers.append((int(number_match.group(1)), heading.start()))

    ordered = sorted((position, number) for number, position in markers)
    candidates: dict[int, list[str]] = {}
    for index, (position, number) in enumerate(ordered):
        end = ordered[index + 1][0] if index + 1 < len(ordered) else len(text)
        candidates.setdefault(number, []).append(text[position:end])

    # Parallel workers may leave an early heading-only placeholder and later
    # deliver the complete section in a separate fragment.  Keep the largest
    # non-comment candidate for each section, rather than allowing the first
    # placeholder to mask the substantive body.
    return {
        number: max(parts, key=uncommented_length)
        for number, parts in candidates.items()
    }


def count(pattern: re.Pattern[str], text: str) -> int:
    return len(pattern.findall(text))


def audit(source: str, target: str) -> list[SectionAudit]:
    authority_hash = hashlib.sha256(source.encode("utf-8")).hexdigest().upper()
    target_hash = hashlib.sha256(target.encode("utf-8")).hexdigest().upper()
    source_sections = section_slices(source_book(source))
    target_sections = section_slices(target)
    rows: list[SectionAudit] = []

    for number in range(1, 32):
        source_text = source_sections.get(number, "")
        target_text = target_sections.get(number, "")
        source_chars = uncommented_length(source_text)
        target_chars = uncommented_length(target_text)
        ratio = target_chars / source_chars if source_chars else 0.0
        source_displays = count(DISPLAY, source_text)
        target_displays = count(DISPLAY, target_text)

        notes: list[str] = []
        if not source_text:
            status = "source-parser-failure"
            notes.append("section not recovered from authority")
        elif not target_text:
            status = "missing"
            notes.append("target section absent")
        else:
            display_delta = abs(target_displays - source_displays)
            display_tolerance = max(1, round(source_displays * 0.15))
            if ratio < 0.65:
                notes.append(f"target/source non-comment character ratio {ratio:.2f} below 0.65")
            if display_delta > display_tolerance:
                notes.append(
                    f"display-count delta {display_delta} exceeds tolerance {display_tolerance}"
                )
            status = "gross-structural-risk" if notes else "present-structural-review"

        rows.append(
            SectionAudit(
                authority_sha256=authority_hash,
                target_document_sha256=target_hash,
                section=number,
                source_chars=source_chars,
                target_chars=target_chars,
                char_ratio=f"{ratio:.4f}",
                source_displays=source_displays,
                target_displays=target_displays,
                source_display_rows=count(DISPLAY_ROWS, source_text),
                target_display_rows=count(DISPLAY_ROWS, target_text),
                source_inline_math_openers=count(INLINE_MATH, source_text),
                target_inline_math_openers=count(INLINE_MATH, target_text),
                source_commands=count(COMMANDS, source_text),
                target_commands=count(COMMANDS, target_text),
                status=status,
                note="; ".join(notes),
            )
        )
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--authority-tex", type=Path, required=True)
    parser.add_argument(
        "--target-book-tex",
        type=Path,
        nargs="+",
        required=True,
        help="ordered target TeX fragments; all are concatenated before section slicing",
    )
    parser.add_argument("--output-csv", type=Path, required=True)
    args = parser.parse_args()

    authority_hash = hashlib.sha256(args.authority_tex.read_bytes()).hexdigest().upper()
    if authority_hash != R823_TEX_SHA256:
        raise ValueError(
            f"authority hash mismatch: found {authority_hash}; expected {R823_TEX_SHA256}"
        )
    target = "\n".join(path.read_text(encoding="utf-8") for path in args.target_book_tex)
    rows = audit(args.authority_tex.read_text(encoding="utf-8"), target)
    args.output_csv.parent.mkdir(parents=True, exist_ok=True)
    with args.output_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(asdict(rows[0])))
        writer.writeheader()
        writer.writerows(asdict(row) for row in rows)

    counts: dict[str, int] = {}
    for row in rows:
        counts[row.status] = counts.get(row.status, 0) + 1
    print(f"wrote {args.output_csv}")
    for status in ("present-structural-review", "gross-structural-risk", "missing", "source-parser-failure"):
        print(f"{status}: {counts.get(status, 0)}")
    accepted = counts.get("present-structural-review", 0) == 31
    return 0 if accepted else 1


if __name__ == "__main__":
    raise SystemExit(main())
