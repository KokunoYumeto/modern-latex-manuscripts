#!/usr/bin/env python3
"""Measure paper-level source drift between two Noether cumulative TeX files.

The report is deliberately conservative: any normalized German-source delta is
treated as English synchronization work until a bilingual review disposes it.
It does not claim that a high similarity score proves source fidelity.
"""

from __future__ import annotations

import argparse
import csv
import difflib
import hashlib
import re
from dataclasses import dataclass
from pathlib import Path


PAPER_MARKER = re.compile(
    r"(?:\{\\Large\\bfseries\s*|\\section\*\{)\s*(\d{1,2})\.\s*",
    re.MULTILINE,
)
FALLBACK_MARKERS = {
    # Some current source-control papers preserve the printed title page and
    # therefore omit the artificial cumulative paper number from that title.
    4: re.compile(
        r"\{\\Large\\bfseries\s+Zur Invariantentheorie\\\\\s*\n"
        r"\s*der Formen von",
        re.MULTILINE,
    ),
    17: re.compile(r"^%\s*Paper 17:", re.MULTILINE),
    18: re.compile(r"^%\s*Paper 18:", re.MULTILINE),
    19: re.compile(
        r"\{\\Large\\bfseries\s+Idealtheorie in Ringbereichen",
        re.MULTILINE,
    ),
}
LAYOUT_ONLY_LINE = re.compile(
    r"^\s*(?:"
    r"\\(?:begin|end)\{center\}|"
    r"\\clearpage|\\newpage|"
    r"\\setcounter\{(?:footnote|page)\}\{[^}]*\}|"
    r"\\vspace\*?\{[^}]*\}|"
    r"\\smallskip|\\medskip|\\bigskip"
    r")\s*$"
)
TOKEN = re.compile(r"\\[A-Za-z@]+|\\.|[\wÀ-ÖØ-öø-ÿ]+|[^\s]", re.UNICODE)
PAPER43_END_MARKERS = (
    # R822 appends a separate long-form source-control work after Paper 43.
    # This heading is the first line of that appended work, not part of Paper 43.
    re.compile(r"^\\section\*\{Einleitung\}\\label\{einleitung\}", re.MULTILINE),
)


@dataclass(frozen=True)
class PaperSlice:
    number: int
    start: int
    end: int
    text: str


def strip_unescaped_comment(line: str) -> str:
    for i, char in enumerate(line):
        if char != "%":
            continue
        backslashes = 0
        j = i - 1
        while j >= 0 and line[j] == "\\":
            backslashes += 1
            j -= 1
        if backslashes % 2 == 0:
            return line[:i]
    return line


def mask_tex_comments(text: str) -> str:
    """Replace real TeX comments with spaces while preserving every offset.

    Structural parsers use offsets into the original source.  Removing comments
    would move those offsets, while merely searching the raw text lets a
    commented-out heading masquerade as live content.  Newlines and escaped
    percent signs are therefore retained exactly and only comment payload is
    blanked.
    """
    masked: list[str] = []
    for line in text.splitlines(keepends=True):
        body = line.rstrip("\r\n")
        ending = line[len(body) :]
        comment_at: int | None = None
        for index, char in enumerate(body):
            if char != "%":
                continue
            backslashes = 0
            cursor = index - 1
            while cursor >= 0 and body[cursor] == "\\":
                backslashes += 1
                cursor -= 1
            if backslashes % 2 == 0:
                comment_at = index
                break
        if comment_at is None:
            masked.append(body + ending)
        else:
            masked.append(body[:comment_at] + (" " * (len(body) - comment_at)) + ending)
    return "".join(masked)


def normalize_tex(text: str) -> str:
    kept: list[str] = []
    for raw in text.splitlines():
        line = strip_unescaped_comment(raw).strip()
        if not line or LAYOUT_ONLY_LINE.match(line):
            continue
        kept.append(line)
    normalized = " ".join(kept)
    normalized = normalized.replace("\\,", " ").replace("\\;", " ")
    normalized = re.sub(r"\s+", " ", normalized).strip()
    return normalized


def slice_papers(text: str) -> dict[int, PaperSlice]:
    structural_text = mask_tex_comments(text)
    markers = [
        (int(match.group(1)), match.start())
        for match in PAPER_MARKER.finditer(structural_text)
        if 1 <= int(match.group(1)) <= 43
    ]
    first: dict[int, int] = {}
    for number, position in markers:
        first.setdefault(number, position)

    for number, pattern in FALLBACK_MARKERS.items():
        if number in first:
            continue
        # Papers 17 and 18 intentionally use explicit source-control comment
        # boundaries in the authority and its faithful cumulative targets.  All
        # other fallbacks must be live, non-comment TeX.
        match = pattern.search(text if number in {17, 18} else structural_text)
        if match:
            first[number] = match.start()
            markers.append((number, match.start()))
    markers.sort(key=lambda item: item[1])

    missing = [number for number in range(1, 44) if number not in first]
    if missing:
        raise ValueError(f"Could not find first marker for papers: {missing}")

    end_document = structural_text.rfind("\\end{document}")
    if end_document < 0:
        end_document = len(text)

    slices: dict[int, PaperSlice] = {}
    for number in range(1, 44):
        start = first[number]
        if number < 43:
            end = first[number + 1]
        else:
            # RA10 appends a duplicate Papers 40-43 apparatus block after the
            # first Paper 43 body. R822 instead appends a separate long-form
            # source-control work. Stop at the first applicable boundary.
            later = [
                position
                for marker_number, position in markers
                if position > start and marker_number != number
            ]
            explicit_ends = [
                match.start()
                for pattern in PAPER43_END_MARKERS
                if (match := pattern.search(structural_text, start)) is not None
            ]
            boundaries = later + explicit_ends
            end = min(boundaries) if boundaries else end_document
        if end <= start:
            raise ValueError(f"Invalid slice for Paper {number}: {start}..{end}")
        slices[number] = PaperSlice(number, start, end, text[start:end])
    return slices


def compare(old: str, new: str) -> dict[str, object]:
    old_normalized = normalize_tex(old)
    new_normalized = normalize_tex(new)
    old_tokens = TOKEN.findall(old_normalized)
    new_tokens = TOKEN.findall(new_normalized)
    matcher = difflib.SequenceMatcher(None, old_tokens, new_tokens)

    inserted = deleted = replaced_old = replaced_new = equal = 0
    hunks = 0
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            equal += i2 - i1
        else:
            hunks += 1
            if tag == "insert":
                inserted += j2 - j1
            elif tag == "delete":
                deleted += i2 - i1
            else:
                replaced_old += i2 - i1
                replaced_new += j2 - j1

    if old_normalized == new_normalized:
        band = "normalized-identical"
    elif matcher.ratio() >= 0.995:
        band = "small-delta"
    elif matcher.ratio() >= 0.98:
        band = "moderate-delta"
    else:
        band = "large-delta"

    return {
        "old_chars": len(old_normalized),
        "new_chars": len(new_normalized),
        "old_tokens": len(old_tokens),
        "new_tokens": len(new_tokens),
        "similarity": f"{matcher.ratio():.8f}",
        "delta_band": band,
        "diff_hunks": hunks,
        "inserted_tokens": inserted,
        "deleted_tokens": deleted,
        "replaced_old_tokens": replaced_old,
        "replaced_new_tokens": replaced_new,
        "equal_tokens": equal,
        "old_normalized_sha256": hashlib.sha256(old_normalized.encode()).hexdigest(),
        "new_normalized_sha256": hashlib.sha256(new_normalized.encode()).hexdigest(),
        "english_sync_status": (
            "source-identical-no-delta-detected"
            if old_normalized == new_normalized
            else "review-and-propagation-required"
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--old", type=Path, required=True)
    parser.add_argument("--new", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    old_text = args.old.read_text(encoding="utf-8")
    new_text = args.new.read_text(encoding="utf-8")
    old_papers = slice_papers(old_text)
    new_papers = slice_papers(new_text)

    rows: list[dict[str, object]] = []
    for number in range(1, 44):
        row: dict[str, object] = {"paper": number}
        row.update(compare(old_papers[number].text, new_papers[number].text))
        rows.append(row)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    counts: dict[str, int] = {}
    for row in rows:
        band = str(row["delta_band"])
        counts[band] = counts.get(band, 0) + 1
    print(f"wrote {args.output}")
    for band in ("normalized-identical", "small-delta", "moderate-delta", "large-delta"):
        print(f"{band}: {counts.get(band, 0)}")


if __name__ == "__main__":
    main()
