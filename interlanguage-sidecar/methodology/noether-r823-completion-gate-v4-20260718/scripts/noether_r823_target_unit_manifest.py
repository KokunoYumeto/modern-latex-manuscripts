#!/usr/bin/env python3
"""Create exact 81-unit hashes for a complete Spanish or French cumulative.

The output is target-side evidence only.  It does not assign the status
``source-reconciled``; bilingual review must make that judgment separately.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
from dataclasses import asdict, dataclass
from pathlib import Path

from noether_r823_book_structure_audit import SECTION_NUMBER, SUBSECTION_LINE
from noether_sync_audit import mask_tex_comments, slice_papers


INPUT_COMMAND = re.compile(r"\\(?:input|include)(?![A-Za-z@])")
INPUT = re.compile(
    r"\\(?:input|include)(?![A-Za-z@])\s*(?:\{([^{}\r\n]+)\}|([^\s{}%]+))"
)

HEADING_COMMAND = {
    "book": re.compile(r"\\(?:LARGE|Large)\b|\\(?:section|part)\*\{"),
    "post45": re.compile(
        r"\\(?:subsection|section|part)\*\{|"
        r"\\(?:LARGE|Large)\b.*\\(?:textbf|bfseries)"
    ),
    "supplement": re.compile(r"\\(?:subsection|section|part)\*\{"),
    "bibliography": re.compile(
        r"\\(?:subsection|section|part)\*\{"
    ),
    "notices": re.compile(
        r"\\(?:subsection|section|part)\*\{"
    ),
    "reviews": re.compile(
        r"\\(?:subsection|section|part)\*\{"
    ),
    "books": re.compile(
        r"\\(?:subsection|section|part)\*\{"
    ),
}
CENTERED_HEADING_STYLE = {
    "bibliography": re.compile(r"\\(?:LARGE|Large)\b|\\(?:bfseries|textbf)\b"),
    "notices": re.compile(r"\\(?:LARGE|Large)\b|\\(?:bfseries|textbf)\b"),
    "reviews": re.compile(
        r"\\(?:LARGE|Large)\b|\\(?:bfseries|textbf|emph)\b"
    ),
    "books": re.compile(
        r"\\(?:LARGE|Large)\b|\\(?:bfseries|textbf|emph)\b"
    ),
}


MARKERS = {
    "spanish": {
        "book": (
            "Álgebra de las magnitudes hipercomplejas",
            "Álgebra de las grandezas hipercomplejas",
            "Álgebra de las cantidades hipercomplejas",
        ),
        "post45": (
            "Condiciones necesarias y suficientes de multiplicidad",
            "Condiciones de multiplicidad necesarias y suficientes",
        ),
        "supplement": ("Suplemento, en colaboración con E. Noether",),
        "bibliography": ("Bibliografía",),
        "notices": ("Lista de comunicaciones breves", "Lista de notas breves"),
        "reviews": ("Reseñas bibliográficas", "Reseñas de libros"),
        "books": ("Libros realizados con la colaboración de Emmy Noether",),
    },
    "french": {
        "book": ("Algèbre des grandeurs hypercomplexes",),
        "post45": (
            "Conditions de multiplicité nécessaires et suffisantes",
            "Conditions nécessaires et suffisantes de multiplicité",
        ),
        "supplement": (
            "Complément, en commun avec E. Noether",
            "Supplément, en collaboration avec E. Noether",
        ),
        "bibliography": ("Bibliographie",),
        "notices": ("Liste des communications", "Liste des notices"),
        "reviews": ("Comptes rendus", "Recensions", "Notices bibliographiques"),
        "books": (
            "Livres réalisés avec la collaboration d'Emmy Noether",
            "Livres réalisés avec la participation d'Emmy Noether",
            "Livres élaborés avec la participation d'Emmy Noether",
            "Livres auxquels Emmy Noether a collaboré",
        ),
    },
}


@dataclass
class Unit:
    unit_id: str
    target_start_line: int
    target_end_line: int
    target_chars: int
    target_utf8_bytes: int
    target_sha256: str
    target_document_sha256: str
    target_root_tex: str
    start_excerpt: str


def read_utf8(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="strict")


def resolve_input(base: Path, raw: str) -> Path:
    candidate = (base / raw).resolve()
    if candidate.suffix:
        return candidate
    return candidate.with_suffix(".tex")


def expand_tex(path: Path, seen: set[Path] | None = None) -> tuple[str, set[Path], list[str]]:
    """Expand every live local ``input``/``include`` form exactly.

    Braced and unbraced commands may occur inline.  Commented commands are
    ignored, duplicate inclusions remain duplicated (as TeX would process
    them), and only an actual recursion cycle is suppressed.
    """
    dependencies = set() if seen is None else set(seen)
    active: set[Path] = set()

    def visit(current: Path) -> tuple[str, list[str]]:
        resolved = current.resolve()
        if resolved in active:
            return "", [f"input cycle suppressed: {resolved}"]
        active.add(resolved)
        dependencies.add(resolved)
        raw_text = read_utf8(resolved)
        structural_text = mask_tex_comments(raw_text)
        matches = list(INPUT.finditer(structural_text))
        warnings: list[str] = []

        covered_commands = [
            command
            for command in INPUT_COMMAND.finditer(structural_text)
            if not any(match.start() <= command.start() < match.end() for match in matches)
        ]
        for command in covered_commands:
            line = structural_text.count("\n", 0, command.start()) + 1
            warnings.append(f"unparsed input/include command in {resolved}:{line}")

        pieces: list[str] = []
        cursor = 0
        for match in matches:
            pieces.append(raw_text[cursor : match.start()])
            raw_name = (match.group(1) or match.group(2) or "").strip()
            child = resolve_input(resolved.parent, raw_name)
            if not child.is_file():
                warnings.append(f"missing input: {child}")
                pieces.append(raw_text[match.start() : match.end()])
            else:
                child_text, child_warnings = visit(child)
                pieces.append(child_text)
                warnings.extend(child_warnings)
            cursor = match.end()
        pieces.append(raw_text[cursor:])
        active.remove(resolved)
        return "".join(pieces), warnings

    expanded, warnings = visit(path)
    return expanded, dependencies, warnings


def locate_any(
    text: str,
    alternatives: tuple[str, ...],
    start: int,
    kind: str | None = None,
) -> int:
    """Locate a live heading line, never a comment or prose mention."""
    structural_text = mask_tex_comments(text)
    positions: list[tuple[int, str]] = []
    for marker in alternatives:
        cursor = start
        while True:
            position = structural_text.find(marker, cursor)
            if position < 0:
                break
            line_start = structural_text.rfind("\n", 0, position) + 1
            line_end = structural_text.find("\n", position)
            if line_end < 0:
                line_end = len(structural_text)
            line = structural_text[line_start:line_end]
            center_context = structural_text[max(0, line_start - 1000) : line_start]
            center_is_open = center_context.rfind(r"\begin{center}") > center_context.rfind(
                r"\end{center}"
            )
            pattern = HEADING_COMMAND.get(kind or "book")
            explicit_heading = pattern is not None and pattern.search(line)
            centered_heading = (
                kind in {"bibliography", "notices", "reviews", "books"}
                and CENTERED_HEADING_STYLE[kind].search(line) is not None
                and (
                    r"\begin{center}" in line
                    or center_is_open
                )
            )
            if explicit_heading or centered_heading:
                positions.append((line_start, marker))
                break
            cursor = position + len(marker)
    if not positions:
        label = kind or "heading"
        raise ValueError(
            f"none of the required live {label} headings found after offset {start}: "
            f"{alternatives}"
        )
    return min(positions)[0]


def line_number(text: str, position: int) -> int:
    return text.count("\n", 0, position) + 1


def add_unit(rows: list[Unit], root: Path, text: str, unit_id: str, start: int, end: int) -> None:
    if end <= start:
        raise ValueError(f"invalid target span for {unit_id}: {start}..{end}")
    fragment = text[start:end]
    encoded = fragment.encode("utf-8")
    excerpt = next((line.strip() for line in fragment.splitlines() if line.strip()), "")[:160]
    rows.append(
        Unit(
            unit_id=unit_id,
            target_start_line=line_number(text, start),
            target_end_line=line_number(text, end - 1),
            target_chars=len(fragment),
            target_utf8_bytes=len(encoded),
            target_sha256=hashlib.sha256(encoded).hexdigest().upper(),
            target_document_sha256=hashlib.sha256(text.encode("utf-8")).hexdigest().upper(),
            target_root_tex=str(root.resolve()),
            start_excerpt=excerpt,
        )
    )


def build(root: Path, text: str, language: str) -> list[Unit]:
    markers = MARKERS[language]
    papers = slice_papers(text)
    p43_start = papers[43].start
    book_start = locate_any(text, markers["book"], p43_start, "book")
    post45_start = locate_any(text, markers["post45"], book_start, "post45")
    supplement_start = locate_any(text, markers["supplement"], post45_start, "supplement")
    bibliography_start = locate_any(text, markers["bibliography"], supplement_start, "bibliography")
    notices_start = locate_any(text, markers["notices"], bibliography_start, "notices")
    reviews_start = locate_any(text, markers["reviews"], notices_start, "reviews")
    books_start = locate_any(text, markers["books"], reviews_start, "books")
    structural_text = mask_tex_comments(text)
    document_end = structural_text.find(r"\end{document}", books_start)
    if document_end < 0:
        document_end = len(text)

    rows: list[Unit] = []
    for number in range(1, 44):
        paper = papers[number]
        end = book_start if number == 43 else paper.end
        add_unit(rows, root, text, f"P{number:02d}", paper.start, end)

    section_positions: dict[int, int] = {}
    for heading in SUBSECTION_LINE.finditer(structural_text, book_start, post45_start):
        number_match = SECTION_NUMBER.search(heading.group(0))
        if number_match:
            section_positions.setdefault(int(number_match.group(1)), heading.start())
    missing = [number for number in range(1, 32) if number not in section_positions]
    if missing:
        raise ValueError(f"target book section markers missing: {missing}")
    ordered_sections = [section_positions[number] for number in range(1, 32)]

    add_unit(rows, root, text, "BOOK_TITLE_INTRO", book_start, ordered_sections[0])
    for index, number in enumerate(range(1, 32)):
        end = ordered_sections[index + 1] if index + 1 < len(ordered_sections) else post45_start
        add_unit(rows, root, text, f"BOOK_S{number:02d}", ordered_sections[index], end)

    add_unit(rows, root, text, "POST45_MAIN", post45_start, supplement_start)
    add_unit(rows, root, text, "POST45_NOETHER_SUPPLEMENT", supplement_start, bibliography_start)
    add_unit(rows, root, text, "BIBLIOGRAPHY", bibliography_start, notices_start)
    add_unit(rows, root, text, "SHORT_NOTICES", notices_start, reviews_start)
    add_unit(rows, root, text, "BOOK_REVIEWS", reviews_start, books_start)
    add_unit(rows, root, text, "BOOKS_WITH_NOETHER", books_start, document_end)
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--language", choices=tuple(MARKERS), required=True)
    parser.add_argument("--target-tex", type=Path, required=True)
    parser.add_argument("--output-csv", type=Path, required=True)
    args = parser.parse_args()

    expanded, dependencies, warnings = expand_tex(args.target_tex)
    if warnings:
        raise ValueError("; ".join(warnings))
    rows = build(args.target_tex, expanded, args.language)
    args.output_csv.parent.mkdir(parents=True, exist_ok=True)
    with args.output_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(asdict(rows[0])))
        writer.writeheader()
        writer.writerows(asdict(row) for row in rows)
    print(f"expanded {len(dependencies)} TeX files")
    print(f"wrote {len(rows)} target units to {args.output_csv}")
    print(f"target_document_sha256={rows[0].target_document_sha256}")


if __name__ == "__main__":
    main()
