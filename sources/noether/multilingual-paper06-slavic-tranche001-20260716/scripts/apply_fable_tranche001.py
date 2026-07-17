#!/usr/bin/env python3
"""Apply Fable Tranche 001 to Noether Paper 06 without touching protected TeX.

Latin Interslavic remains the lexical authority.  The existing Cyrillic files
contain reviewed manual normalizations that a full transliterator rerun would
lose, so this script mirrors only the approved orthographic deltas into the
Cyrillic sibling.
"""

from __future__ import annotations

import csv
import difflib
import hashlib
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LANE = (
    ROOT
    / "03_projects"
    / "noether"
    / "03_translation_workspaces"
    / "interslavic_tranche_001_paper06"
)
WORK = LANE / "work"
OUTPUT = LANE / "tranche_output"

LATIN_DIR = WORK / "interslavic" / "v001"
CYRILLIC_DIR = WORK / "interslavic-cyrillic" / "v001"

LATIN_MAPPINGS = (
    ("voobče", "obće"),
    ("vobče", "obće"),
    ("dlugost", "dolgost"),
    ("obšč", "obć"),
    ("vzet", "vzęt"),
)

# Script synchronization for the project's established Cyrillic convention.
# In particular, Latin ę is rendered as я by the existing generator.
CYRILLIC_MAPPINGS = (
    ("вообче", "обче"),
    ("вобче", "обче"),
    ("длугост", "долгост"),
    ("обшч", "обч"),
    ("взет", "взят"),
)

PROTECTED_COMMAND_ARGS = {
    "cite": 1,
    "citep": 1,
    "citet": 1,
    "label": 1,
    "ref": 1,
    "pageref": 1,
    "eqref": 1,
    "bibitem": 1,
    "href": 2,
    "url": 1,
    "texttt": 1,
}

MATH_ENVIRONMENTS = {
    "align",
    "align*",
    "aligned",
    "array",
    "displaymath",
    "equation",
    "equation*",
    "gather",
    "gather*",
    "gathered",
    "math",
    "multline",
    "multline*",
    "split",
}


@dataclass
class Change:
    path: str
    script: str
    source: str
    target: str
    count: int


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_text(path: Path) -> tuple[str, bool]:
    raw = path.read_bytes()
    has_bom = raw.startswith(b"\xef\xbb\xbf")
    return raw.decode("utf-8-sig"), has_bom


def write_text(path: Path, text: str, has_bom: bool) -> None:
    encoding = "utf-8-sig" if has_bom else "utf-8"
    with path.open("w", encoding=encoding, newline="") as handle:
        handle.write(text)


def is_escaped(text: str, index: int) -> bool:
    slashes = 0
    cursor = index - 1
    while cursor >= 0 and text[cursor] == "\\":
        slashes += 1
        cursor -= 1
    return slashes % 2 == 1


def balanced_end(text: str, start: int, opening: str, closing: str) -> int:
    if start >= len(text) or text[start] != opening:
        return start
    depth = 0
    cursor = start
    while cursor < len(text):
        char = text[cursor]
        if char == opening and not is_escaped(text, cursor):
            depth += 1
        elif char == closing and not is_escaped(text, cursor):
            depth -= 1
            if depth == 0:
                return cursor + 1
        cursor += 1
    return len(text)


def skip_space(text: str, index: int) -> int:
    while index < len(text) and text[index].isspace():
        index += 1
    return index


def apply_case(source: str, target: str, candidate: str) -> str:
    if candidate.isupper():
        return target.upper()
    if candidate[:1].isupper():
        return target[:1].upper() + target[1:]
    return target


def replace_plain(
    text: str,
    mappings: tuple[tuple[str, str], ...],
    counts: dict[tuple[str, str], int],
) -> str:
    output: list[str] = []
    cursor = 0
    lower = text.lower()
    while cursor < len(text):
        matched = False
        for source, target in mappings:
            if lower.startswith(source.lower(), cursor):
                candidate = text[cursor : cursor + len(source)]
                output.append(apply_case(source, target, candidate))
                counts[(source, target)] = counts.get((source, target), 0) + 1
                cursor += len(source)
                matched = True
                break
        if not matched:
            output.append(text[cursor])
            cursor += 1
    return "".join(output)


def transform_tex(
    text: str,
    mappings: tuple[tuple[str, str], ...],
    counts: dict[tuple[str, str], int],
    *,
    in_footnote: bool = False,
) -> str:
    """Transform prose nodes while preserving comments, math, and raw IDs."""

    output: list[str] = []
    plain: list[str] = []
    cursor = 0
    dollar_math = False
    paren_math = False
    bracket_math = False
    math_env_depth = 0

    def flush_plain() -> None:
        if plain:
            output.append(replace_plain("".join(plain), mappings, counts))
            plain.clear()

    def in_math() -> bool:
        return dollar_math or paren_math or bracket_math or math_env_depth > 0

    while cursor < len(text):
        char = text[cursor]

        if char == "%" and not is_escaped(text, cursor):
            flush_plain()
            end = text.find("\n", cursor)
            if end < 0:
                output.append(text[cursor:])
                break
            output.append(text[cursor : end + 1])
            cursor = end + 1
            continue

        if in_footnote and text.startswith("``", cursor) and not in_math():
            flush_plain()
            end = text.find("''", cursor + 2)
            if end < 0:
                output.append(text[cursor:])
                break
            output.append(text[cursor : end + 2])
            cursor = end + 2
            continue

        if char == "$" and not is_escaped(text, cursor):
            flush_plain()
            delimiter = "$$" if text.startswith("$$", cursor) else "$"
            output.append(delimiter)
            dollar_math = not dollar_math
            cursor += len(delimiter)
            continue

        if char == "\\":
            flush_plain()
            if text.startswith("\\(", cursor):
                output.append("\\(")
                paren_math = True
                cursor += 2
                continue
            if text.startswith("\\)", cursor):
                output.append("\\)")
                paren_math = False
                cursor += 2
                continue
            if text.startswith("\\[", cursor):
                output.append("\\[")
                bracket_math = True
                cursor += 2
                continue
            if text.startswith("\\]", cursor):
                output.append("\\]")
                bracket_math = False
                cursor += 2
                continue

            command_match = re.match(r"\\([A-Za-z@]+\*?)", text[cursor:])
            if not command_match:
                output.append(text[cursor : cursor + 2])
                cursor += min(2, len(text) - cursor)
                continue

            raw_command = command_match.group(0)
            command = command_match.group(1).rstrip("*")
            output.append(raw_command)
            cursor += len(raw_command)

            if command in {"begin", "end"}:
                spaced = skip_space(text, cursor)
                output.append(text[cursor:spaced])
                cursor = spaced
                if cursor < len(text) and text[cursor] == "{":
                    end = balanced_end(text, cursor, "{", "}")
                    raw_arg = text[cursor:end]
                    output.append(raw_arg)
                    environment = raw_arg[1:-1]
                    if environment in MATH_ENVIRONMENTS:
                        if command == "begin":
                            math_env_depth += 1
                        else:
                            math_env_depth = max(0, math_env_depth - 1)
                    cursor = end
                continue

            if command == "footnote" and not in_math():
                spaced = skip_space(text, cursor)
                output.append(text[cursor:spaced])
                cursor = spaced
                if cursor < len(text) and text[cursor] == "{":
                    end = balanced_end(text, cursor, "{", "}")
                    inner = text[cursor + 1 : end - 1]
                    output.append("{")
                    output.append(
                        transform_tex(inner, mappings, counts, in_footnote=True)
                    )
                    output.append("}")
                    cursor = end
                continue

            if command in PROTECTED_COMMAND_ARGS:
                spaced = skip_space(text, cursor)
                output.append(text[cursor:spaced])
                cursor = spaced
                while cursor < len(text) and text[cursor] == "[":
                    end = balanced_end(text, cursor, "[", "]")
                    output.append(text[cursor:end])
                    cursor = skip_space(text, end)
                for _ in range(PROTECTED_COMMAND_ARGS[command]):
                    spaced = skip_space(text, cursor)
                    output.append(text[cursor:spaced])
                    cursor = spaced
                    if cursor < len(text) and text[cursor] == "{":
                        end = balanced_end(text, cursor, "{", "}")
                        output.append(text[cursor:end])
                        cursor = end
                continue

            continue

        if in_math():
            output.append(char)
        else:
            plain.append(char)
        cursor += 1

    flush_plain()
    return "".join(output)


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    if not LATIN_DIR.is_dir() or not CYRILLIC_DIR.is_dir():
        raise SystemExit(f"Paper 06 workspace is incomplete: {WORK}")

    OUTPUT.mkdir(parents=True, exist_ok=True)
    files = sorted(LATIN_DIR.glob("*.tex")) + sorted(CYRILLIC_DIR.glob("*.tex"))
    before_hashes = {path: sha256(path) for path in files}
    protected_before = {
        path: sha256(path)
        for language in ("russian", "ukrainian")
        for path in sorted((WORK / language).rglob("*"))
        if path.is_file()
    }

    changes: list[Change] = []
    diffs: list[str] = []
    changed_files: list[Path] = []

    for script_name, directory, mappings in (
        ("Latin", LATIN_DIR, LATIN_MAPPINGS),
        ("Cyrillic", CYRILLIC_DIR, CYRILLIC_MAPPINGS),
    ):
        for path in sorted(directory.glob("*.tex")):
            original, has_bom = read_text(path)
            counts: dict[tuple[str, str], int] = {}
            transformed = transform_tex(original, mappings, counts)
            idempotence_counts: dict[tuple[str, str], int] = {}
            second_pass = transform_tex(transformed, mappings, idempotence_counts)
            if transformed != second_pass or any(idempotence_counts.values()):
                raise RuntimeError(f"Non-idempotent mapping result: {path}")
            if transformed == original:
                continue

            write_text(path, transformed, has_bom)
            changed_files.append(path)
            relative = path.relative_to(WORK).as_posix()
            for (source, target), count in sorted(counts.items()):
                changes.append(Change(relative, script_name, source, target, count))
            diffs.extend(
                difflib.unified_diff(
                    original.splitlines(keepends=True),
                    transformed.splitlines(keepends=True),
                    fromfile=f"a/{relative}",
                    tofile=f"b/{relative}",
                    n=3,
                )
            )

    protected_after = {path: sha256(path) for path in protected_before}
    altered_protected = [
        str(path.relative_to(WORK))
        for path, digest in protected_before.items()
        if protected_after[path] != digest
    ]
    if altered_protected:
        raise RuntimeError(
            "Russian/Ukrainian payload changed unexpectedly: "
            + ", ".join(altered_protected)
        )

    with (OUTPUT / "CHANGE_LEDGER.csv").open(
        "w", encoding="utf-8", newline=""
    ) as handle:
        writer = csv.writer(handle)
        writer.writerow(["path", "script", "source", "target", "count"])
        for change in changes:
            writer.writerow(
                [change.path, change.script, change.source, change.target, change.count]
            )

    (OUTPUT / "TRANCHE001.diff").write_text(
        "".join(diffs), encoding="utf-8", newline=""
    )

    after_hashes = {path: sha256(path) for path in files}
    report = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "spec": "00_governance/FABLE_TRANCHE_001_EXECUTABLE_SPEC_20260710.md",
        "scope": "Noether Paper 06 Interslavic Latin and Cyrillic only",
        "latin_authority": True,
        "cyrillic_policy": (
            "Mirrored approved orthographic deltas into the existing Cyrillic "
            "sibling; prior manual Cyrillic normalizations were preserved."
        ),
        "changed_files": [path.relative_to(WORK).as_posix() for path in changed_files],
        "changed_file_count": len(changed_files),
        "replacement_count": sum(change.count for change in changes),
        "changes": [change.__dict__ for change in changes],
        "idempotence_check": "pass",
        "russian_ukrainian_unchanged": not altered_protected,
        "before_after_sha256": {
            path.relative_to(WORK).as_posix(): {
                "before": before_hashes[path],
                "after": after_hashes[path],
            }
            for path in files
            if before_hashes[path] != after_hashes[path]
        },
    }
    (OUTPUT / "ORTHOGRAPHY_SYNC_REPORT.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    print(
        f"changed {len(changed_files)} files; "
        f"applied {report['replacement_count']} approved replacements"
    )
    for change in changes:
        print(
            f"{change.script}: {change.path}: "
            f"{change.source} -> {change.target} ({change.count})"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
