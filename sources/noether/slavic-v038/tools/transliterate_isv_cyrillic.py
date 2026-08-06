#!/usr/bin/env python3
"""Create a deterministic Cyrillic reader projection from Latin Interslavic.

Latin Interslavic remains the editable linguistic source of truth.  The tool
protects preamble, mathematics, TeX controls, labels/references, foreign spans,
comments, dimensions, and structural arguments; it transliterates only reader
prose and emits a validation receipt.  It never treats the projection as an
independent translation witness.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime
from pathlib import Path

import draft_translations as legacy


WORD_RE = re.compile(r"[A-Za-zČĆŠŽĚŲÅĘčćšžěųåę]+")
PROTECT_EXTRA = [
    re.compile(r"\\begin\{(?:enumerate|itemize|description)\}\[[^\]]*\]"),
    re.compile(r"(?m)^\\setlength\b.*$"),
    re.compile(r"(?m)^\\setcounter\b.*$"),
    re.compile(r"\\addcontentsline\{[^{}]*\}\{[^{}]*\}"),
    re.compile(r"\\(?:thispagestyle|pagestyle|pagenumbering)\{[^{}]*\}"),
    re.compile(r"\b[A-Z](?:\.[A-Z])*\."),
    re.compile(r"\b[IVXLCDM]{2,}\b"),
    re.compile(r"(?<=Glava )[IVXLCDM]+\b"),
    re.compile(r"(?<=Čest )[IVXLCDM]+\b"),
    re.compile(r"(?<=Глава )[IVXLCDM]+\b"),
    re.compile(r"(?<=Чест )[IVXLCDM]+\b"),
    re.compile(r"\d+(?:\.\d+)?(?:pt|cm|mm|em|ex|in)\b"),
    # LaTeX counter identifiers are code, even when nested inside a prose-side
    # definition such as \def\labelenumi{\arabic{enumi}.}.
    re.compile(r"\{enum(?:i|ii|iii|iv)\}"),
]


LOWER_MAP = {
    "a": "а",
    "b": "б",
    "c": "ц",
    "č": "ч",
    "ć": "ч",
    "d": "д",
    "e": "е",
    "ě": "е",
    "ę": "я",
    "f": "ф",
    "g": "г",
    "h": "х",
    "i": "и",
    "j": "ј",
    "k": "к",
    "l": "л",
    "m": "м",
    "n": "н",
    "o": "о",
    "å": "о",
    "p": "п",
    "q": "к",
    "r": "р",
    "s": "с",
    "š": "ш",
    "t": "т",
    "u": "у",
    "ų": "у",
    "v": "в",
    "w": "в",
    "x": "кс",
    "y": "ы",
    "z": "з",
    "ž": "ж",
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def preserve_case(source: str, target: str) -> str:
    if source.isupper():
        return target.upper()
    if source[:1].isupper():
        return target[:1].upper() + target[1:]
    return target


def transliterate_word(word: str) -> str:
    lower = word.lower()
    output: list[str] = []
    index = 0
    while index < len(lower):
        pair = lower[index : index + 2]
        if pair == "lj":
            output.append("ль")
            index += 2
            continue
        if pair == "nj":
            output.append("нь")
            index += 2
            continue
        character = lower[index]
        # The lane's observed Cyrillic convention writes ę as я, except after
        # č/ć/š/ž where the consonant already carries the appropriate value.
        if character == "ę" and index > 0 and lower[index - 1] in "čćšž":
            output.append("а")
        else:
            output.append(LOWER_MAP.get(character, character))
        index += 1
    return preserve_case(word, "".join(output))


def protect_body(body: str) -> tuple[str, list[str]]:
    values: list[str] = []

    def token(value: str) -> str:
        index = len(values)
        values.append(value)
        return f"¤¤{index:06d}¤¤"

    current = body
    for pattern in legacy.PROTECTED_FULL:
        current = pattern.sub(lambda match: token(match.group(0)), current)
    current = re.sub(r"\\srcfn\{[^{}]*\}", lambda match: token(match.group(0)), current)
    for pattern in PROTECT_EXTRA:
        current = pattern.sub(lambda match: token(match.group(0)), current)
    current = re.sub(
        r"\\begin\{[^{}]*\}|\\end\{[^{}]*\}",
        lambda match: token(match.group(0)),
        current,
    )
    current = re.sub(r"\\item(?:\[[^\]]*\])?", lambda match: token(match.group(0)), current)
    current = re.sub(
        r"\\[A-Za-z@]+\*?|\\\\|\\[^A-Za-z\s]",
        lambda match: token(match.group(0)),
        current,
    )
    return current, values


def restore(text: str, values: list[str]) -> str:
    output = text
    # Protection passes may wrap text that already contains an earlier token.
    # Restore newest wrappers first so every reintroduced older token is still
    # visited later in this loop.
    for index in range(len(values) - 1, -1, -1):
        value = values[index]
        output = output.replace(f"¤¤{index:06d}¤¤", value)
    if re.search(r"¤¤\d{6}¤¤", output):
        raise RuntimeError("unrestored protection token")
    return output


def transliterate_document(text: str) -> tuple[str, dict]:
    begin = text.find(r"\begin{document}")
    end = text.rfind(r"\end{document}")
    if begin < 0 or end < begin:
        raise ValueError("input must be a complete TeX document")
    body_start = begin + len(r"\begin{document}")
    prefix = text[:body_start]
    body = text[body_start:end]
    suffix = text[end:]
    protected, values = protect_body(body)
    words = [match.group(0) for match in WORD_RE.finditer(protected)]
    converted = WORD_RE.sub(lambda match: transliterate_word(match.group(0)), protected)
    restored = restore(converted, values)
    output = prefix + restored + suffix
    input_structure = legacy.protect(text)[1]
    output_structure = legacy.protect(output)[1]
    errors = []
    if input_structure != output_structure:
        errors.append(
            f"TeX/math structural-value mismatch: {len(input_structure)} versus {len(output_structure)}"
        )
    if re.search(r"\\(?:arabic|roman|Roman|alph|Alph|value)\{[^\x00-\x7F]", output):
        errors.append("transliterated LaTeX counter identifier")
    if re.search(r"\\begin\{(?:enumerate|itemize|description)\}\[[^\]]*[А-Яа-я]", output):
        errors.append("transliterated enumitem option")
    latin_words_remaining = sorted(
        set(match.group(0) for match in WORD_RE.finditer(protect_body(restored)[0]))
    )
    return output, {
        "protected_span_count": len(values),
        "transliterated_word_occurrences": len(words),
        "unique_input_words": sorted(set(word.lower() for word in words)),
        "remaining_unprotected_latin_words": latin_words_remaining,
        "structure_token_count": len(input_structure),
        "errors": errors,
        "pass": not errors and not latin_words_remaining,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    source_bytes = args.input.read_bytes()
    source_text = source_bytes.decode("utf-8-sig")
    output_text, validation = transliterate_document(source_text)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(output_text, encoding="utf-8", newline="\n")
    report = {
        "schema": "noether-slavic-v038-interslavic-cyrillic-projection/1.0",
        "generated_at": datetime.now().astimezone().isoformat(),
        "classification": (
            "deterministic reader projection from Latin Interslavic; not an independent translation witness"
        ),
        "input": {
            "path": args.input.resolve().as_posix(),
            "bytes": len(source_bytes),
            "sha256": sha256(source_bytes),
        },
        "output": {
            "path": args.output.resolve().as_posix(),
            "bytes": args.output.stat().st_size,
            "sha256": sha256(args.output.read_bytes()),
        },
        "rule_notes": [
            "Latin Interslavic is the source of truth; Cyrillic is a deterministic reader projection.",
            "Math, TeX controls, labels/references, foreign spans, comments, and preamble are byte-preserved.",
            "Fallback maps ě->е, ų->у, å->о, y->ы, č/ć->ч, š->ш, ž->ж, c->ц, j->ј.",
            "Fallback maps ę->я except after č/ć/š/ž, where it maps to а.",
            "The observed lane convention maps lj->ль and nj->нь.",
        ],
        "validation": validation,
    }
    args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"{'PASS' if validation['pass'] else 'FAIL'} words={validation['transliterated_word_occurrences']} "
        f"output={args.output} report={args.report}"
    )
    return 0 if validation["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
