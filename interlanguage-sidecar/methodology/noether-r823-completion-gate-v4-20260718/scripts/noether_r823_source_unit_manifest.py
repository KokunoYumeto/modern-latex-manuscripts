#!/usr/bin/env python3
"""Create an exact source-unit manifest for the complete R823 authority.

The manifest establishes non-overlapping source spans for Papers 1--43, the
31-section long-form book, the Kapferer--Noether material, bibliography, and
terminal lists.  Target-language parity ledgers can then cite these hashes.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
from dataclasses import asdict, dataclass
from pathlib import Path

from noether_sync_audit import slice_papers


TITLE_MARKER = r"{\LARGE\bfseries Algebra der hyperkomplexen Größen\par}"
POST45_MARKER = r"\subsection*{Notwendige und hinreichende Multiplizitätsbedingungen"
SUPPLEMENT_MARKER = r"\subsection*{Zusatz, gemeinsam mit E. Noether"
BIBLIOGRAPHY_MARKER = r"{\Large\bfseries Bibliographie}"
SHORT_NOTICES_MARKER = r"{\Large\bfseries Liste der Kurzmitteilungen und Buchbesprechungen"
BOOK_REVIEWS_MARKER = r"\emph{Buchbesprechungen, erschienen in den Jahresberichten"
BOOKS_MARKER = r"\emph{Bücher, entstanden unter Mitwirkung von Emmy Noether}"
SUBSECTION_LINE = re.compile(r"^\\subsection\*\{[^\r\n]+", re.MULTILINE)
SECTION_NUMBER = re.compile(r"(?:§|\\S)[^0-9\r\n]{0,20}([1-9]|[12][0-9]|3[01])\.")


@dataclass
class Unit:
    unit_id: str
    start_line: int
    end_line: int
    chars: int
    utf8_bytes: int
    source_sha256: str
    source_path: str
    start_excerpt: str


def locate(text: str, marker: str, start: int = 0) -> int:
    position = text.find(marker, start)
    if position < 0:
        raise ValueError(f"required marker not found after offset {start}: {marker}")
    return position


def line_number(text: str, position: int) -> int:
    return text.count("\n", 0, position) + 1


def add_unit(rows: list[Unit], source: Path, text: str, unit_id: str, start: int, end: int) -> None:
    if end <= start:
        raise ValueError(f"invalid span for {unit_id}: {start}..{end}")
    fragment = text[start:end]
    encoded = fragment.encode("utf-8")
    excerpt = next((line.strip() for line in fragment.splitlines() if line.strip()), "")[:160]
    rows.append(
        Unit(
            unit_id=unit_id,
            start_line=line_number(text, start),
            end_line=line_number(text, end - 1),
            chars=len(fragment),
            utf8_bytes=len(encoded),
            source_sha256=hashlib.sha256(encoded).hexdigest().upper(),
            source_path=str(source.resolve()),
            start_excerpt=excerpt,
        )
    )


def build(source: Path, text: str) -> list[Unit]:
    title_start = locate(text, TITLE_MARKER)
    post45_start = locate(text, POST45_MARKER, title_start)
    supplement_start = locate(text, SUPPLEMENT_MARKER, post45_start)
    bibliography_start = locate(text, BIBLIOGRAPHY_MARKER, supplement_start)
    notices_start = locate(text, SHORT_NOTICES_MARKER, bibliography_start)
    reviews_start = locate(text, BOOK_REVIEWS_MARKER, notices_start)
    books_start = locate(text, BOOKS_MARKER, reviews_start)
    document_end = locate(text, r"\end{document}", books_start)

    rows: list[Unit] = []
    papers = slice_papers(text)
    for number in range(1, 44):
        paper = papers[number]
        end = title_start if number == 43 else paper.end
        add_unit(rows, source, text, f"P{number:02d}", paper.start, end)

    section_positions: dict[int, int] = {}
    for heading in SUBSECTION_LINE.finditer(text, title_start, post45_start):
        match = SECTION_NUMBER.search(heading.group(0))
        if match:
            section_positions.setdefault(int(match.group(1)), heading.start())
    missing = [number for number in range(1, 32) if number not in section_positions]
    if missing:
        raise ValueError(f"book section markers missing: {missing}")
    ordered_sections = [section_positions[number] for number in range(1, 32)]

    add_unit(rows, source, text, "BOOK_TITLE_INTRO", title_start, ordered_sections[0])
    for index, number in enumerate(range(1, 32)):
        end = ordered_sections[index + 1] if index + 1 < len(ordered_sections) else post45_start
        add_unit(rows, source, text, f"BOOK_S{number:02d}", ordered_sections[index], end)

    add_unit(rows, source, text, "POST45_MAIN", post45_start, supplement_start)
    add_unit(rows, source, text, "POST45_NOETHER_SUPPLEMENT", supplement_start, bibliography_start)
    add_unit(rows, source, text, "BIBLIOGRAPHY", bibliography_start, notices_start)
    add_unit(rows, source, text, "SHORT_NOTICES", notices_start, reviews_start)
    add_unit(rows, source, text, "BOOK_REVIEWS", reviews_start, books_start)
    add_unit(rows, source, text, "BOOKS_WITH_NOETHER", books_start, document_end)
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--authority-tex", type=Path, required=True)
    parser.add_argument("--output-csv", type=Path, required=True)
    args = parser.parse_args()

    text = args.authority_tex.read_text(encoding="utf-8")
    rows = build(args.authority_tex, text)
    args.output_csv.parent.mkdir(parents=True, exist_ok=True)
    with args.output_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(asdict(rows[0])))
        writer.writeheader()
        writer.writerows(asdict(row) for row in rows)
    print(f"wrote {len(rows)} source units to {args.output_csv}")


if __name__ == "__main__":
    main()
