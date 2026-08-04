#!/usr/bin/env python3
"""Generate bounded P35 math-locus and structural-TeX audit artifacts."""

from __future__ import annotations

import bisect
from collections import Counter, defaultdict
import difflib
import hashlib
import json
import re
import sys
from pathlib import Path


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest().upper()


def escaped(text: str, index: int) -> bool:
    count = 0
    index -= 1
    while index >= 0 and text[index] == "\\":
        count += 1
        index -= 1
    return count % 2 == 1


def line_starts(text: str) -> list[int]:
    starts = [0]
    starts.extend(match.end() for match in re.finditer("\n", text))
    return starts


def line_col(starts: list[int], offset: int) -> tuple[int, int]:
    line_index = bisect.bisect_right(starts, offset) - 1
    return line_index + 1, offset - starts[line_index] + 1


def body_offsets(text: str) -> tuple[int, int, int, int]:
    lines = text.splitlines(keepends=True)
    start_line = next(
        i for i, line in enumerate(lines, start=1) if line.startswith("\\section*{35.")
    )
    end_line = max(
        i for i, line in enumerate(lines, start=1) if line.strip() == "\\clearpage"
    )
    start_offset = sum(len(line) for line in lines[: start_line - 1])
    end_offset = sum(len(line) for line in lines[:end_line])
    return start_offset, end_offset, start_line, end_line


def find_closing(text: str, start: int, closer: str, limit: int) -> int:
    i = start
    while i < limit:
        if text[i] == "%" and not escaped(text, i):
            newline = text.find("\n", i + 1, limit)
            i = limit if newline == -1 else newline + 1
            continue
        if text.startswith(closer, i) and not escaped(text, i):
            return i
        i += 1
    return -1


def extract_math(text: str, label: str) -> tuple[list[dict], list[str]]:
    start, end, _, _ = body_offsets(text)
    starts = line_starts(text)
    spans: list[dict] = []
    errors: list[str] = []
    i = start
    while i < end:
        if text[i] == "%" and not escaped(text, i):
            newline = text.find("\n", i + 1, end)
            i = end if newline == -1 else newline + 1
            continue
        kind = None
        opener = None
        closer = None
        if text.startswith("\\[", i) and not escaped(text, i):
            kind, opener, closer = "display_bracket", "\\[", "\\]"
        elif text.startswith("\\(", i) and not escaped(text, i):
            kind, opener, closer = "inline_paren", "\\(", "\\)"
        elif text.startswith("$$", i) and not escaped(text, i):
            kind, opener, closer = "display_dollar", "$$", "$$"
        elif text[i] == "$" and not escaped(text, i):
            kind, opener, closer = "inline_dollar", "$", "$"
        if kind is None:
            i += 1
            continue
        content_start = i + len(opener)
        close_at = find_closing(text, content_start, closer, end)
        if close_at == -1:
            line, col = line_col(starts, i)
            errors.append(f"unclosed {kind} at {label}:{line}:{col}")
            i += len(opener)
            continue
        span_end = close_at + len(closer)
        start_line, start_col = line_col(starts, i)
        end_line, end_col = line_col(starts, span_end - 1)
        raw = text[i:span_end]
        content = text[content_start:close_at]
        spans.append(
            {
                "kind": kind,
                "start_line": start_line,
                "start_column": start_col,
                "end_line": end_line,
                "end_column": end_col,
                "raw": raw,
                "content": content,
                "raw_sha256": sha256_text(raw),
            }
        )
        i = span_end
    for ordinal, span in enumerate(spans, start=1):
        span["ordinal"] = ordinal
        span["locus_id"] = f"P35-MATH-{ordinal:03d}"
    return spans, errors


SIMPLE_TEXT_MACRO = re.compile(r"\\(hbox|text)\s*\{[^{}]*\}")


def remove_comments(value: str) -> str:
    return re.sub(r"(?<!\\)%[^\n]*", "", value)


def no_space(value: str) -> str:
    return re.sub(r"\s+", "", remove_comments(value))


def normalize_localized_text(value: str) -> str:
    value = SIMPLE_TEXT_MACRO.sub(lambda m: f"\\{m.group(1)}{{<TEXT>}}", value)
    return no_space(value)


def normalize_symbolic(value: str) -> str:
    """Compare mathematical symbols while excluding localized prose macros."""
    value = SIMPLE_TEXT_MACRO.sub("", value)
    return no_space(value)


TOKEN_RE = re.compile(r"\\[A-Za-z@]+|\\.|[A-Za-z]+|\d+|[^\s]")


def tokens(value: str) -> list[str]:
    return TOKEN_RE.findall(remove_comments(value))


def token_diff(source: str, target: str) -> list[dict]:
    a = tokens(source)
    b = tokens(target)
    out = []
    for op, a0, a1, b0, b1 in difflib.SequenceMatcher(a=a, b=b).get_opcodes():
        if op != "equal":
            out.append(
                {
                    "operation": op,
                    "source_tokens": a[a0:a1],
                    "target_tokens": b[b0:b1],
                }
            )
    return out


STRUCTURAL_PATTERNS = [
    ("section", re.compile(r"\\section\*\{")),
    ("numbered_section", re.compile(r"\\S~\\textbf\{")),
    ("bold_locus", re.compile(r"\\(?:medskip\\noindent|noindent)\\textbf\{")),
    ("italic_locus", re.compile(r"\\noindent\\textit\{")),
    ("environment_begin", re.compile(r"\\begin\{([^}]+)\}")),
    ("environment_end", re.compile(r"\\end\{([^}]+)\}")),
    ("item", re.compile(r"\\item(?:\[([^]]+)\])?")),
    ("display_open", re.compile(r"\\\[")),
    ("display_close", re.compile(r"\\\]")),
    ("equation_tag", re.compile(r"\\tag\{([^}]+)\}")),
    ("footnote_mark", re.compile(r"\\textsuperscript\{([^}]+)\}")),
    ("counter_reset", re.compile(r"\\setcounter\{footnote\}\{0\}")),
    ("clearpage", re.compile(r"\\clearpage")),
]


def structural_loci(text: str, label: str) -> dict:
    start, end, start_line, end_line = body_offsets(text)
    starts = line_starts(text)
    loci = []
    for kind, pattern in STRUCTURAL_PATTERNS:
        for match in pattern.finditer(text, start, end):
            line, column = line_col(starts, match.start())
            line_end = text.find("\n", match.start(), end)
            if line_end == -1:
                line_end = end
            loci.append(
                {
                    "kind": kind,
                    "line": line,
                    "column": column,
                    "capture": match.group(1) if match.lastindex else None,
                    "line_text": text[starts[line - 1] : line_end].rstrip("\r"),
                }
            )
    loci.sort(key=lambda x: (x["line"], x["column"], x["kind"]))
    env_sequence = [
        {"action": "begin" if x["kind"] == "environment_begin" else "end", "name": x["capture"], "line": x["line"]}
        for x in loci
        if x["kind"] in {"environment_begin", "environment_end"}
    ]
    signature = [
        f"{x['kind']}:{x['capture'] or ''}"
        for x in loci
        if x["kind"] not in {"footnote_mark"}
    ]
    return {
        "label": label,
        "body_start_line": start_line,
        "body_end_line": end_line,
        "locus_count": len(loci),
        "loci": loci,
        "environment_sequence": env_sequence,
        "signature": signature,
    }


def main() -> int:
    if len(sys.argv) != 4:
        print("usage: audit_p35_tex.py SOURCE_TEX HANS_TEX OUTPUT_DIR", file=sys.stderr)
        return 2
    source_path = Path(sys.argv[1])
    target_path = Path(sys.argv[2])
    output_dir = Path(sys.argv[3])
    output_dir.mkdir(parents=True, exist_ok=True)
    source_text = source_path.read_text(encoding="utf-8")
    target_text = target_path.read_text(encoding="utf-8")

    source_spans, source_errors = extract_math(source_text, "source")
    target_spans, target_errors = extract_math(target_text, "hans")
    for ordinal, span in enumerate(target_spans, start=1):
        span["locus_id"] = f"P35-HANS-MATH-{ordinal:03d}"

    source_body_start = body_offsets(source_text)[2]
    target_body_start = body_offsets(target_text)[2]
    pre_collapse_offset = target_body_start - source_body_start
    post_collapse_offset = pre_collapse_offset - 1

    def mapped_target_line(source_line: int) -> int | None:
        if 1 <= source_line <= 91:
            return source_line + pre_collapse_offset
        if source_line == 92:
            return None
        if 93 <= source_line <= 264:
            return source_line + post_collapse_offset
        raise ValueError(f"source line outside P35 body map: {source_line}")

    source_by_target_line: dict[int, list[dict]] = defaultdict(list)
    target_by_line: dict[int, list[dict]] = defaultdict(list)
    for span in source_spans:
        target_line = mapped_target_line(span["start_line"])
        if target_line is None:
            raise ValueError(f"math span unexpectedly starts on unmapped source line {span['start_line']}")
        source_by_target_line[target_line].append(span)
    for span in target_spans:
        target_by_line[span["start_line"]].append(span)

    pairs = []
    line_groups = []
    counts = {
        "exact_raw": 0,
        "whitespace_only": 0,
        "localized_text_only": 0,
        "missing_source_formula_in_target": 0,
        "extra_target_formula": 0,
    }
    reordered_lines = []
    for target_line in sorted(set(source_by_target_line) | set(target_by_line)):
        source_group = source_by_target_line.get(target_line, [])
        target_group = target_by_line.get(target_line, [])
        source_sequence = [normalize_localized_text(x["raw"]) for x in source_group]
        target_sequence = [normalize_localized_text(x["raw"]) for x in target_group]
        if Counter(source_sequence) == Counter(target_sequence) and source_sequence != target_sequence:
            reordered_lines.append(target_line)

        target_queues: dict[str, list[dict]] = defaultdict(list)
        for span in target_group:
            target_queues[normalize_localized_text(span["raw"])].append(span)
        matched_target_ids = set()
        group_pairs = []
        missing = []
        for source in source_group:
            key = normalize_localized_text(source["raw"])
            if target_queues[key]:
                target = target_queues[key].pop(0)
                matched_target_ids.add(target["locus_id"])
                if source["raw"] == target["raw"]:
                    status = "exact_raw"
                elif no_space(source["raw"]) == no_space(target["raw"]):
                    status = "whitespace_only"
                else:
                    status = "localized_text_only"
                counts[status] += 1
                pair = {
                    "source_locus_id": source["locus_id"],
                    "target_locus_id": target["locus_id"],
                    "status": status,
                    "source": source,
                    "target": target,
                }
                pairs.append(pair)
                group_pairs.append(pair)
            else:
                missing.append(source)
                counts["missing_source_formula_in_target"] += 1
        extra = [span for span in target_group if span["locus_id"] not in matched_target_ids]
        counts["extra_target_formula"] += len(extra)
        line_groups.append(
            {
                "source_start_line": source_group[0]["start_line"] if source_group else None,
                "expected_target_start_line": target_line,
                "source_formula_count": len(source_group),
                "target_formula_count": len(target_group),
                "same_normalized_multiset": not missing and not extra,
                "order_changed": Counter(source_sequence) == Counter(target_sequence)
                and source_sequence != target_sequence,
                "matched_pairs": [
                    {"source_locus_id": p["source_locus_id"], "target_locus_id": p["target_locus_id"], "status": p["status"]}
                    for p in group_pairs
                ],
                "missing_source_formulas": missing,
                "extra_target_formulas": extra,
            }
        )

    global_target_queues: dict[str, list[dict]] = defaultdict(list)
    for span in target_spans:
        global_target_queues[normalize_localized_text(span["raw"])].append(span)
    global_matches = []
    global_missing = []
    globally_matched_target_ids = set()
    for source in source_spans:
        key = normalize_localized_text(source["raw"])
        if global_target_queues[key]:
            target = global_target_queues[key].pop(0)
            globally_matched_target_ids.add(target["locus_id"])
            global_matches.append(
                {"source_locus_id": source["locus_id"], "target_locus_id": target["locus_id"]}
            )
        else:
            global_missing.append(source)
    global_extra = [
        span for span in target_spans if span["locus_id"] not in globally_matched_target_ids
    ]

    symbolic_target_queues: dict[str, list[dict]] = defaultdict(list)
    for span in target_spans:
        symbolic_target_queues[normalize_symbolic(span["raw"])].append(span)
    symbolic_matches = []
    symbolic_missing = []
    symbolically_matched_target_ids = set()
    for source in source_spans:
        key = normalize_symbolic(source["raw"])
        if symbolic_target_queues[key]:
            target = symbolic_target_queues[key].pop(0)
            symbolically_matched_target_ids.add(target["locus_id"])
            symbolic_matches.append(
                {"source_locus_id": source["locus_id"], "target_locus_id": target["locus_id"]}
            )
        else:
            symbolic_missing.append(source)
    symbolic_extra = [
        span for span in target_spans if span["locus_id"] not in symbolically_matched_target_ids
    ]

    source_structure = structural_loci(source_text, "selected_german")
    target_structure = structural_loci(target_text, "hans")
    structure = {
        "paper_id": "NOETHER-P35",
        "source": source_structure,
        "target": target_structure,
        "environment_name_action_sequences_equal": [
            (x["action"], x["name"]) for x in source_structure["environment_sequence"]
        ]
        == [(x["action"], x["name"]) for x in target_structure["environment_sequence"]],
        "structural_signatures_equal_excluding_footnote_numbers": source_structure["signature"]
        == target_structure["signature"],
    }
    math_index = {
        "paper_id": "NOETHER-P35",
        "source_path": str(source_path),
        "target_path": str(target_path),
        "source_formula_count": len(source_spans),
        "target_formula_count": len(target_spans),
        "matched_formula_count": len(pairs),
        "line_map": {
            "source_1_91": f"target = source + {pre_collapse_offset}",
            "source_92": "blank source separator collapsed in target",
            "source_93_264": f"target = source + {post_collapse_offset}",
        },
        "parser_errors": source_errors + target_errors,
        "comparison_counts": counts,
        "reordered_target_lines": reordered_lines,
        "global_formula_inventory": {
            "matched_source_formula_count": len(global_matches),
            "missing_source_formulas": global_missing,
            "extra_target_formulas": global_extra,
            "source_formula_preservation_pass": len(global_missing) == 0,
        },
        "symbolic_formula_inventory_excluding_localized_text_macros": {
            "matched_source_formula_count": len(symbolic_matches),
            "missing_source_formulas": symbolic_missing,
            "extra_target_formulas": symbolic_extra,
            "source_symbolic_formula_preservation_pass": len(symbolic_missing) == 0,
        },
        "line_groups": line_groups,
        "pairs": pairs,
    }
    summary = {
        "paper_id": "NOETHER-P35",
        "source_formula_count": len(source_spans),
        "target_formula_count": len(target_spans),
        "formula_counts_equal": len(source_spans) == len(target_spans),
        "matched_formula_count": len(pairs),
        "parser_error_count": len(source_errors) + len(target_errors),
        "comparison_counts": counts,
        "global_missing_source_formula_count": len(global_missing),
        "global_extra_target_formula_count": len(global_extra),
        "source_formula_preservation_pass": len(global_missing) == 0,
        "symbolic_missing_source_formula_count": len(symbolic_missing),
        "symbolic_extra_target_formula_count": len(symbolic_extra),
        "source_symbolic_formula_preservation_pass": len(symbolic_missing) == 0,
        "mismatch_line_groups": [
            {"source_start_line": g["source_start_line"], "target_start_line": g["expected_target_start_line"]}
            for g in line_groups
            if not g["same_normalized_multiset"]
        ],
        "reordered_target_lines": reordered_lines,
        "environment_name_action_sequences_equal": structure["environment_name_action_sequences_equal"],
        "structural_signatures_equal_excluding_footnote_numbers": structure["structural_signatures_equal_excluding_footnote_numbers"],
        "source_body_lines": [source_structure["body_start_line"], source_structure["body_end_line"]],
        "target_body_lines": [target_structure["body_start_line"], target_structure["body_end_line"]],
    }

    artifacts = {
        "P35_MATH_LOCUS_INDEX.json": math_index,
        "P35_TEX_STRUCTURE_INDEX.json": structure,
        "P35_TEX_AUDIT_SUMMARY.json": summary,
    }
    for name, value in artifacts.items():
        (output_dir / name).write_text(
            json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n"
        )
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if summary["parser_error_count"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
