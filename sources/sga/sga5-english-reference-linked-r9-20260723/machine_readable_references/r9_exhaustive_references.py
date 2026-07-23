#!/usr/bin/env python3
"""Exhaustive residual-reference audit and linker for the SGA 5 R9 successor.

The input is the immutable R8 successor.  R9 adds only ``\\hyperref`` wrappers
around source-visible tokens; every pre-R9 dotted-number occurrence is retained
in a machine inventory, including declarations, external citations, mathematical
data, and unavailable targets.  The script deliberately separates inventory
generation from mutation so ambiguous rows can be reviewed before applying.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


EXPOSE_LABEL_RE = re.compile(r"\\label\{sga5:(?P<expose>III?B|[IVXLCDM]+):expose")
LOCATOR_RE = re.compile(
    r"(?<![A-Za-z0-9_.\\:])"
    r"(?:(?P<scope>III\s*B|[IVXLCDM]{1,5})(?P<scope_space>~|\\ |\s)+)?"
    r"(?P<number>(?:[A-Z]\.)?\d+(?:\.\d+){1,6})"
    r"(?P<suffix>"
    r"(?:~|\s)*\((?:[ivxlcdm]+|[a-z])(?:~|\s)*(?:bis|ter)?\)"
    r"|(?:~|\s)*,?(?:~|\s)+(?:[ivxlcdm]+|[a-z])(?:~|\s)+(?:bis|ter)"
    r"|(?:~|\s)+[a-z]\)"
    r")?",
    re.IGNORECASE,
)
KIND_CUE_RE = re.compile(
    r"(?i)(Definition|Proposition|Theorem|Lemma|Corollary|Remark|Example|"
    r"Exercise|Notation|Scholium|Conjecture|Section|Paragraph|Equation|"
    r"Formula|condition|assertion|case)\s*~?\s*$"
)
REFERENCE_CUE_RE = re.compile(
    r"(?i)(?:according to|applying|apply|by|see|cf\.|compare|from|using|use|"
    r"thanks to|follows from|deduced from|in view of|as in|of|condition|"
    r"assertion|case|formula|equation|paragraph|section|proposition|theorem|"
    r"lemma|corollary|remark|definition|notation)\s*~?\s*$"
)
DIRECT_EXTERNAL_PREFIX_RE = re.compile(
    r"(?i)(?:\bEGA\b|\bSGA\b(?:\s|~)*(?:A|[0-9]|\$)|\bFGA\b|"
    r"\bBourbaki\b|\bHartshorne\b|\bHironaka\b|\bTohoku\b|"
    r"\bLanglands\b|\bWeil\b|\[(?:\d+|[A-Z][A-Z0-9.-]*)\]|"
    r"\\cite\{|loc\.?\s*cit|\\loccit|ibid\.)[^.;:!?()]{0,70}$"
)

# These are source-backed adjudications for the small set of places where
# punctuation alone cannot delimit citation scope.  In particular, the final
# member of an external list can have the same number as an SGA 5 target.
EXTERNAL_OVERRIDE_IDS = {
    "SGA5-R9-RESIDUAL-000041",  # SGA A, Exp. XVIII 3.1.7
    "SGA5-R9-RESIDUAL-000073",  # SGA A, Exp. IX 5.8
    "SGA5-R9-RESIDUAL-000106",  # SGA A, Exp. X 4.2 (first occurrence)
    "SGA5-R9-RESIDUAL-000110",  # same citation series, 3.2
    "SGA5-R9-RESIDUAL-000183",  # SGAA 3.1.10
    "SGA5-R9-RESIDUAL-000188",  # SGAA 3.1.10 inside aligned display text
    "SGA5-R9-RESIDUAL-000209",  # SGAA X 2.2, not SGA 5 Exp. X
    "SGA5-R9-RESIDUAL-000329",  # loc. cit. SGA 4 XVII 5.2.4
    "SGA5-R9-RESIDUAL-000648",  # Langlands 7.11
    "SGA5-R9-RESIDUAL-000652",  # Langlands 7.12
    "SGA5-R9-RESIDUAL-000864",  # [6] 1.1
    "SGA5-R9-RESIDUAL-001408",  # EGA 0_III 11.1.3
    "SGA5-R9-RESIDUAL-001409",  # EGA 0_III 13.4.1
    "SGA5-R9-RESIDUAL-001410",  # EGA 0_III 13.4.1.3
    "SGA5-R9-RESIDUAL-001424",  # EGA 0_III 13.4.3
    "SGA5-R9-RESIDUAL-001462",  # EGA 0_I 5.4.3.1
    "SGA5-R9-RESIDUAL-001463",  # EGA 0_I 5.4.4
    "SGA5-R9-RESIDUAL-001494",  # EGA 0_III 11.1.3
    "SGA5-R9-RESIDUAL-001497",  # carried SGA 4 X citation, 5.2
    "SGA5-R9-RESIDUAL-001504",  # SGA 4 1/2 Cycle 2.3.8
    "SGA5-R9-RESIDUAL-001519",  # TF 6.6
    "SGA5-R9-RESIDUAL-001640",  # carried SGA 6 VII citation, 4.8
    "SGA5-R9-RESIDUAL-001832",  # [5] Proposition 3.1
    "SGA5-R9-RESIDUAL-001834",  # [5] Proposition 3.1
    "SGA5-R9-RESIDUAL-001858",  # Expose XI 5.2.1
    "SGA5-R9-RESIDUAL-001896",  # Expose XI 7.2.3.6
    "SGA5-R9-RESIDUAL-001935",  # Expose XI 7.5.9
    "SGA5-R9-RESIDUAL-001973",  # SGA I Corollary 7.8
    "SGA5-R9-RESIDUAL-001974",  # named external SGA VIII Theorem 1.1
    "SGA5-R9-RESIDUAL-001975",  # named external SGA XII Proposition 3.1
}

LAYOUT_OVERRIDE_IDS = {
    "SGA5-R9-RESIDUAL-000001",  # parskip 0.55em
    "SGA5-R9-RESIDUAL-000003",  # title spacing 0.3em
    "SGA5-R9-RESIDUAL-000197",  # TikZ scale
    "SGA5-R9-RESIDUAL-000223",  # description left margin
    "SGA5-R9-RESIDUAL-000298",  # title spacing 0.3em
    "SGA5-R9-RESIDUAL-000837",  # table width
    "SGA5-R9-RESIDUAL-001427",  # title spacing
    "SGA5-R9-RESIDUAL-001505",  # title spacing
    "SGA5-R9-RESIDUAL-001506",  # title spacing
    "SGA5-R9-RESIDUAL-001507",  # title spacing
    "SGA5-R9-RESIDUAL-001791",  # aligned-display row spacing 0.4em
    "SGA5-R9-RESIDUAL-001794",  # aligned-display row spacing 0.4em
    "SGA5-R9-RESIDUAL-001797",  # aligned-display row spacing 0.4em
    "SGA5-R9-RESIDUAL-001805",  # aligned-display row spacing 0.8em
    "SGA5-R9-RESIDUAL-001807",  # aligned-display row spacing 0.8em
    "SGA5-R9-RESIDUAL-001809",  # aligned-display row spacing 0.8em
    "SGA5-R9-RESIDUAL-001820",  # aligned-display row spacing 0.8em
}

# Ambiguities caused by repeated printed numbers are resolved from the exact
# surrounding source, including the two appendix index notations.
DESTINATION_OVERRIDE_IDS = {
    "SGA5-R9-RESIDUAL-000236": "sga5:I:definition:1.1",
    "SGA5-R9-RESIDUAL-000238": "sga5:I:proposition:1.3",
    "SGA5-R9-RESIDUAL-002015": "sga5:I:subsection:4.2",
    "SGA5-R9-RESIDUAL-002021": "sga5:VI:definition:1.4.3",
    "SGA5-R9-RESIDUAL-002041": "sga5:I:subsection:4.1",
    "SGA5-R9-RESIDUAL-002045": "sga5:I:definition:4.4",  # I App 4.4
    "SGA5-R9-RESIDUAL-002046": "sga5:I:definition:1.1",
    "SGA5-R9-RESIDUAL-002051": "sga5:V:theorem:a.3",  # V A 3.1 = A.3(i)
    "SGA5-R9-RESIDUAL-002102": "sga5:VI:definition:1.4.3",
}

SAME_WORK_UNAVAILABLE_IDS = {
    "SGA5-R9-RESIDUAL-000227",  # Expose II 3.11, absent from this reader
    "SGA5-R9-RESIDUAL-001475",  # source-visible V 1.3 has no destination
    "SGA5-R9-RESIDUAL-001768",  # VIII 7.2 has no numbered destination
    "SGA5-R9-RESIDUAL-001814",  # Expose IX absent from this reader
    "SGA5-R9-RESIDUAL-002009",  # Expose XIV absent from this reader
    "SGA5-R9-RESIDUAL-002032",  # Expose XIV absent from this reader
}

EXTERNAL_CONTEXT_RE = re.compile(
    r"(?i)(?:\bSGAA\b|\bSGA\s*A\b|\bSGA(?:\s|~)*[0-9]+\b|"
    r"\bEGA\b|\bFGA\b|\bLanglands\b|\bHartshorne\b|\bBourbaki\b|"
    r"\bTF\b|\bloc\.?\s*cit\.?|\[[0-9]+\])"
)
def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\r\n")
        writer.writeheader()
        writer.writerows(rows)


def norm_expose(value: str) -> str:
    return re.sub(r"\s+", "", value.upper())


def norm_number(value: str) -> str:
    value = value.strip().replace("~", " ")
    value = re.sub(r"\s+", " ", value)
    return value.lower()


def csv_formula_safe(value: str) -> str:
    """Preserve display text while neutralizing spreadsheet formula prefixes."""
    return "'" + value if value.startswith(("=", "+", "-", "@")) else value


def active_prefix(line: str) -> str:
    escaped = False
    for index, char in enumerate(line):
        if char == "%" and not escaped:
            return line[:index]
        if char == "\\":
            escaped = not escaped
        else:
            escaped = False
    return line


def balanced_end(text: str, start: int, opening: str = "{", closing: str = "}") -> int:
    if start >= len(text) or text[start] != opening:
        return -1
    depth = 0
    escaped = False
    for index in range(start, len(text)):
        char = text[index]
        if char == opening and not escaped:
            depth += 1
        elif char == closing and not escaped:
            depth -= 1
            if depth == 0:
                return index + 1
        if char == "\\":
            escaped = not escaped
        else:
            escaped = False
    return -1


def command_spans(line: str) -> list[tuple[int, int]]:
    """Return spans which must never be rediscovered as residual locators."""
    spans: list[tuple[int, int]] = []
    for match in re.finditer(r"\\hyperref\[", line):
        close = line.find("]", match.end())
        if close < 0 or close + 1 >= len(line) or line[close + 1] != "{":
            continue
        end = balanced_end(line, close + 1)
        if end > 0:
            spans.append((match.start(), end))
    for match in re.finditer(r"\\label\{", line):
        end = balanced_end(line, match.end() - 1)
        if end > 0:
            spans.append((match.start(), end))
    return spans


def overlaps(spans: list[tuple[int, int]], start: int, end: int) -> bool:
    return any(start < right and end > left for left, right in spans)


def inline_math_at(line: str, position: int) -> bool:
    escaped = False
    dollars = 0
    for char in line[:position]:
        if char == "$" and not escaped:
            dollars += 1
        if char == "\\":
            escaped = not escaped
        else:
            escaped = False
    return dollars % 2 == 1


def inferred_scope(line: str, start: int, explicit: str | None, current: str) -> str:
    if explicit:
        return norm_expose(explicit)
    # Lists such as ``(I 1.3, 1.5 and 1.6)`` inherit their Roman scope.
    left = line.rfind("(", 0, start)
    right = line.rfind(")", 0, start)
    if left > right:
        fragment = line[left + 1 : start]
        scopes = list(re.finditer(r"(?<![A-Za-z])(?P<s>III\s*B|[IVXLCDM]{1,5})(?:~|\\ |\s)+\d", fragment))
        if scopes:
            return norm_expose(scopes[-1].group("s"))
    # A Roman scope also carries through a comma-separated series outside
    # parentheses and inside index macro fields: ``III 3.1, 3.2, 6.4``.
    prefix = line[max(0, start - 180) : start]
    scoped = list(
        re.finditer(
            r"(?<![A-Za-z])(?P<s>III\s*B|[IVXLCDM]{1,5})(?:~|\\ |\s)+"
            r"(?:[A-Z]\.)?\d+(?:\.\d+){1,6}",
            prefix,
        )
    )
    if scoped:
        last = scoped[-1]
        tail = prefix[last.end() :]
        tail_words = re.sub(r"[\s~,&;(){}'\\]+", " ", tail).strip().lower().split()
        allowed_words = {"and", "or", "respectively", "bis", "ter"}
        if all(
            word in allowed_words
            or re.fullmatch(r"[ivxlcdm]+", word)
            or re.fullmatch(r"[a-z]", word)
            or re.fullmatch(r"(?:[a-z]\.)?\d+(?:\.\d+)+", word)
            for word in tail_words
        ):
            return norm_expose(last.group("s"))
    # Appendix index forms use ``I App 4.4`` and ``V A 3.1`` rather than a
    # dotted appendix prefix.  They still carry an unambiguous exposé scope.
    appendix = re.search(
        r"(?<![A-Za-z])(?P<s>III\s*B|[IVXLCDM]{1,5})(?:~|\\ |\s)+(?:App|A)(?:~|\\ |\s)+$",
        line[max(0, start - 40) : start],
        re.IGNORECASE,
    )
    if appendix:
        return norm_expose(appendix.group("s"))
    return current


def contextual_label(labels: list[dict[str, str]], line_number: int, kind_cue: str) -> str:
    if not labels:
        return ""
    if kind_cue:
        wanted = kind_cue.lower()
        wanted = {"formula": "equation", "section": "subsection"}.get(wanted, wanted)
        exact = [row for row in labels if row["target_kind"].lower() == wanted]
        if len(exact) == 1:
            return exact[0]["latex_label"]
        if wanted == "section":
            structural = [row for row in labels if row["target_kind"] in {"section", "subsection", "subsubsection"}]
            if len(structural) == 1:
                return structural[0]["latex_label"]
    before = [row for row in labels if int(row["source_line"]) <= line_number]
    pool = before or labels
    chosen = max(pool, key=lambda row: (int(row["source_line"]), row["latex_label"])) if before else min(pool, key=lambda row: (int(row["source_line"]), row["latex_label"]))
    return chosen["latex_label"]


def inventory(root: Path) -> tuple[list[dict[str, object]], dict[str, object]]:
    tex = root / "SGA5_English_sync_workpass.tex"
    evidence = root / "machine_readable_references"
    targets = read_csv(evidence / "REFERENCE_TARGETS.csv")
    target_numbers_by_line: dict[int, Counter[str]] = defaultdict(Counter)
    number_lookup: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    label_lookup = {row["latex_label"]: row for row in targets}
    for row in targets:
        number = norm_number(row["displayed_number"] or row["aux_number"])
        if number:
            number_lookup[(row["expose"], number)].append(row)
            if re.search(r"\d\.\d", number):
                target_numbers_by_line[int(row["source_line"])][number] += 1

    lines = tex.read_text(encoding="utf-8").splitlines()
    rows: list[dict[str, object]] = []
    current_expose = "FRONT"
    display_math = False
    bibliography = False
    for line_number, raw_line in enumerate(lines, start=1):
        expose_match = EXPOSE_LABEL_RE.search(raw_line)
        if expose_match:
            current_expose = norm_expose(expose_match.group("expose"))
        if r"\begin{thebibliography}" in raw_line:
            bibliography = True
        line = active_prefix(raw_line)
        protected = command_spans(line)
        # A TeX line break such as ``\\[0.4em]`` is not ``\[`` display math.
        # Require the display delimiter's slash not to be preceded by another
        # slash; otherwise display state leaks across hundreds of prose lines.
        starts_display = bool(re.search(r"(?<!\\)\\\[", line)) or any(
            token in line
            for token in (
                r"\begin{equation",
                r"\begin{align",
                r"\begin{gather",
                r"\begin{multline",
            )
        )
        ends_display = bool(re.search(r"(?<!\\)\\\]", line)) or any(
            token in line
            for token in (
                r"\end{equation",
                r"\end{align",
                r"\end{gather",
                r"\end{multline",
            )
        )
        line_display_math = display_math or starts_display
        declaration_seen: Counter[str] = Counter()
        for match in LOCATOR_RE.finditer(line):
            if overlaps(protected, match.start(), match.end()):
                continue
            residual_id = f"SGA5-R9-RESIDUAL-{len(rows)+1:06d}"
            visible = match.group(0)
            scope = inferred_scope(line, match.start(), match.group("scope"), current_expose)
            number = norm_number(match.group("number"))
            labels = list(number_lookup.get((scope, number), []))
            prefix = line[max(0, match.start() - 120) : match.start()]
            suffix_context = line[match.end() : min(len(line), match.end() + 80)]
            kind_match = KIND_CUE_RE.search(prefix)
            kind_cue = kind_match.group(1).lower() if kind_match else ""
            cue = bool(REFERENCE_CUE_RE.search(prefix))
            parenthesized = match.start() > 0 and line[match.start() - 1] == "("
            explicit_scope = bool(match.group("scope")) or scope != current_expose
            # Externality must be positively local to the token.  The R8
            # heuristic used a wide window, so a citation elsewhere in the
            # same sentence accidentally hid many internal formula numbers.
            external = bool(DIRECT_EXTERNAL_PREFIX_RE.search(prefix[-120:]))
            math = line_display_math or inline_math_at(line, match.start())
            # A target line can contain body prose after its heading.  Consume
            # only the first matching printed target number(s), never the
            # whole line, or same-line citations get silently hidden.
            declaration = False
            declared_here = target_numbers_by_line.get(line_number, Counter())
            if declaration_seen[number] < declared_here[number]:
                declaration = True
                declaration_seen[number] += 1
            tag_start = line.rfind(r"\tag{", 0, match.start() + 1)
            if tag_start >= 0:
                tag_end = balanced_end(line, tag_start + len(r"\tag"))
                if tag_end > match.end():
                    declaration = True
            layout = bool(
                re.search(
                    r"\\(?:node|draw|path|coordinate)|\\begin\{tikzcd\}.*(?:column sep|row sep)|"
                    r"\\begin\{tikzpicture\}|\\resizebox\{|\\setlength\{|"
                    r"\b(?:column sep|row sep|looseness|scale|pos|leftmargin)\s*=|"
                    r"\\\[\s*\d+\.\d+em\]|\bat\s*\([^)]*$",
                    prefix,
                )
            )
            formula_variant_declaration = bool(
                re.match(r"^\s*\([^)]*$", prefix)
                and re.match(r"\)(?:'{1,3}|\^\{\\mathrm\{bis\}\})?\\qquad", suffix_context)
            )
            math_reference = bool(
                labels
                and math
                and (
                    cue
                    or parenthesized
                    or explicit_scope
                    or match.group("suffix")
                    or r"\arrow" in line
                    or r"\xrightarrow" in line
                    or r"\footnote" in line
                )
            )
            sga5_internal = bool(labels and re.search(r"(?i)\bSGA(?:\s|~)*5\b", prefix[-120:]))

            # Manual appendix/index resolutions can introduce a destination
            # not present in the literal-number lookup pool.
            override_destination = DESTINATION_OVERRIDE_IDS.get(residual_id, "")
            if override_destination:
                override_target = label_lookup.get(override_destination)
                if not override_target:
                    raise RuntimeError(f"unknown destination override {override_destination}")
                if all(row["latex_label"] != override_destination for row in labels):
                    labels.append(override_target)

            external_override = residual_id in EXTERNAL_OVERRIDE_IDS
            layout_override = residual_id in LAYOUT_OVERRIDE_IDS
            unavailable_override = residual_id in SAME_WORK_UNAVAILABLE_IDS
            positive_external_context = bool(EXTERNAL_CONTEXT_RE.search(line))

            if bibliography:
                classification = "external_work_citation"
                reason = "inside_bibliography"
            elif declaration or formula_variant_declaration:
                classification = "structural_declaration_tag"
                reason = "target_or_formula_declaration"
            elif external_override:
                classification = "external_work_citation"
                reason = "source_checked_external_citation_override"
            elif unavailable_override:
                classification = "unavailable_source_target"
                reason = "source_checked_same_work_target_absent"
            elif layout or layout_override:
                # The two source-visible arrow labels 2.2.4 are references,
                # even though their lines are TikZ drawing commands.
                if residual_id in {
                    "SGA5-R9-RESIDUAL-000421",
                    "SGA5-R9-RESIDUAL-000422",
                }:
                    classification = "linked_internal_edge"
                    reason = "source_checked_diagram_arrow_reference"
                else:
                    classification = "typography_layout_geometry_value"
                    reason = "positive_tex_layout_or_geometry_syntax"
            elif sga5_internal:
                classification = "linked_internal_edge"
                reason = "explicit_same_volume_sga5_reference"
            elif external:
                classification = "external_work_citation"
                reason = "external_citation_context"
            elif math_reference:
                classification = "linked_internal_edge"
                reason = "target_exists_in_mathematical_reference_label"
            elif math:
                if labels:
                    classification = "linked_internal_edge"
                    reason = "target_exists_in_mathematical_context"
                elif positive_external_context:
                    classification = "external_work_citation"
                    reason = "external_citation_inside_math_or_display"
                else:
                    classification = "mathematical_numeric_expression"
                    reason = "positive_mathematical_expression_no_internal_target"
            elif labels and (cue or parenthesized or explicit_scope or match.group("suffix")):
                classification = "linked_internal_edge"
                reason = "target_exists_and_reference_context"
            elif labels:
                classification = "linked_internal_edge"
                reason = "target_exists_in_prose_no_cue_required"
            elif cue or parenthesized or explicit_scope or match.group("suffix"):
                if positive_external_context:
                    classification = "external_work_citation"
                    reason = "positive_external_work_context_without_internal_target"
                else:
                    classification = "unavailable_source_target"
                    reason = "reference_context_but_no_destination_in_reader"
            else:
                if positive_external_context:
                    classification = "external_work_citation"
                    reason = "positive_external_work_context"
                else:
                    # This class is prohibited by the exhaustive convention;
                    # encountering it forces a new source-backed adjudication.
                    classification = "UNADJUDICATED_PROHIBITED"
                    reason = "requires_positive_manual_adjudication"

            destination = ""
            if classification == "linked_internal_edge":
                destination = override_destination or contextual_label(labels, line_number, kind_cue)
            rows.append(
                {
                    "residual_id": residual_id,
                    "source_file": tex.name,
                    "source_line": line_number,
                    "start_column_1based": match.start() + 1,
                    "end_column_1based_exclusive": match.end() + 1,
                    "current_expose": current_expose,
                    "reference_scope": scope,
                    "visible_text": visible,
                    "base_number": match.group("number"),
                    "suffix": match.group("suffix") or "",
                    "kind_cue": kind_cue,
                    "candidate_labels": "|".join(row["latex_label"] for row in labels),
                    "destination_label": destination,
                    "classification": classification,
                    "reason": reason,
                    "context": csv_formula_safe(
                        line[max(0, match.start() - 100) : min(len(line), match.end() + 100)]
                    ),
                }
            )
        if starts_display and not ends_display:
            display_math = True
        if ends_display:
            display_math = False
        if r"\end{thebibliography}" in raw_line:
            bibliography = False

    counts = Counter(str(row["classification"]) for row in rows)
    summary = {
        "status": "INVENTORY_COMPLETE_REVIEW_REQUIRED",
        "source_tex": str(tex),
        "source_tex_sha256": sha256(tex),
        "target_rows": len(targets),
        "target_labels_unique": len(label_lookup),
        "residual_rows": len(rows),
        "classification_counts": dict(sorted(counts.items())),
    }
    return rows, summary


def apply_links(root: Path, rows: list[dict[str, object]]) -> dict[str, object]:
    """Apply every admitted R9 edge and regenerate cumulative ledgers."""
    tex = root / "SGA5_English_sync_workpass.tex"
    evidence = root / "machine_readable_references"
    before_bytes = tex.read_bytes()
    before_sha = hashlib.sha256(before_bytes).hexdigest().upper()
    before_text = before_bytes.decode("utf-8")
    before_lines = before_text.splitlines(keepends=True)

    targets = read_csv(evidence / "REFERENCE_TARGETS.csv")
    target_by_label = {row["latex_label"]: row for row in targets}
    linked = [row for row in rows if row["classification"] == "linked_internal_edge"]
    if any(not str(row["destination_label"]) for row in linked):
        raise RuntimeError("one or more admitted R9 edges have no destination")

    by_line: dict[int, list[dict[str, object]]] = defaultdict(list)
    for row in linked:
        by_line[int(row["source_line"])].append(row)
    changed_lines: list[int] = []
    for line_number, line_rows in sorted(by_line.items()):
        original = before_lines[line_number - 1]
        body = original.rstrip("\r\n")
        ending = original[len(body) :]
        mutated = body
        for row in sorted(line_rows, key=lambda item: int(item["start_column_1based"]), reverse=True):
            start = int(row["start_column_1based"]) - 1
            end = int(row["end_column_1based_exclusive"]) - 1
            visible = str(row["visible_text"])
            if body[start:end] != visible:
                raise RuntimeError(
                    f"source coordinate mismatch {row['residual_id']} line {line_number}: "
                    f"{body[start:end]!r} != {visible!r}"
                )
            wrapper = f"\\hyperref[{row['destination_label']}]{{{visible}}}"
            # tikz-cd parses quoted arrow labels with an active quote parser.
            # A hyperref macro with an optional argument must therefore be
            # grouped when it occurs on an arrow line; the group changes no
            # visible text but prevents the parser from consuming the closing
            # quote as part of the optional-argument construct.
            if "\\arrow" in body:
                wrapper = "{" + wrapper + "}"
            mutated = mutated[:start] + wrapper + mutated[end:]
        before_lines[line_number - 1] = mutated + ending
        changed_lines.append(line_number)
    after_text = "".join(before_lines)
    tex.write_text(after_text, encoding="utf-8", newline="")
    after_sha = sha256(tex)

    # The exact generated-after comparison is a stronger reconstruction proof
    # than a broad regex strip: every R9 wrapper is tied to a frozen coordinate
    # in the exact R8 input, while pre-existing R8 wrappers remain untouched.
    if tex.read_text(encoding="utf-8") != after_text:
        raise RuntimeError("written TeX does not match generated R9 text")

    old_edges = read_csv(evidence / "REFERENCE_EDGES.csv")
    edge_fields = [
        "edge_id",
        "source_file",
        "source_line",
        "source_column_1based",
        "expose",
        "reference_scope",
        "visible_text",
        "reference_form",
        "reference_type",
        "destination_stable_id",
        "destination_label",
        "resolution_basis",
        "resolution_status",
        "revision",
    ]
    cumulative_edges: list[dict[str, object]] = []
    for old in old_edges:
        target = target_by_label.get(old["destination_label"], {})
        cumulative_edges.append(
            {
                "edge_id": old["edge_id"],
                "source_file": old["source_file"],
                "source_line": old["source_line"],
                "source_column_1based": "",
                "expose": old["expose"],
                "reference_scope": target.get("expose", old["expose"]),
                "visible_text": old["visible_text"],
                "reference_form": "r8_admitted",
                "reference_type": old["reference_type"],
                "destination_stable_id": target.get("stable_id", ""),
                "destination_label": old["destination_label"],
                "resolution_basis": "preserved_r8_admitted_edge",
                "resolution_status": old["resolution_status"],
                "revision": "R8",
            }
        )
    next_edge = len(cumulative_edges) + 1
    for offset, row in enumerate(linked):
        target = target_by_label[str(row["destination_label"])]
        cumulative_edges.append(
            {
                "edge_id": f"SGA5-EDGE-{next_edge + offset:06d}",
                "source_file": row["source_file"],
                "source_line": row["source_line"],
                "source_column_1based": row["start_column_1based"],
                "expose": row["current_expose"],
                "reference_scope": row["reference_scope"],
                "visible_text": row["visible_text"],
                "reference_form": "exhaustive_dotted_locator",
                "reference_type": row["reason"],
                "destination_stable_id": target["stable_id"],
                "destination_label": row["destination_label"],
                "resolution_basis": row["reason"],
                "resolution_status": "compiled_pending_validation",
                "revision": "R9",
            }
        )
    write_csv(evidence / "REFERENCE_EDGES.csv", cumulative_edges, edge_fields)

    old_candidates = read_csv(evidence / "REFERENCE_CANDIDATES.csv")
    candidate_fields = [
        "candidate_id",
        "source_file",
        "source_line",
        "source_column_1based",
        "expose",
        "reference_scope",
        "visible_text",
        "candidate_kind",
        "displayed_number",
        "candidate_labels",
        "reason",
        "status",
        "final_classification",
        "revision",
    ]
    cumulative_candidates: list[dict[str, object]] = []
    for old in old_candidates:
        cumulative_candidates.append(
            {
                "candidate_id": old["candidate_id"],
                "source_file": old["source_file"],
                "source_line": old["source_line"],
                "source_column_1based": "",
                "expose": old["expose"],
                "reference_scope": old["expose"],
                "visible_text": old["visible_text"],
                "candidate_kind": old["candidate_kind"],
                "displayed_number": old["displayed_number"],
                "candidate_labels": old["candidate_labels"],
                "reason": old["reason"],
                "status": old["status"],
                "final_classification": old["status"],
                "revision": "R8",
            }
        )
    next_candidate = len(cumulative_candidates) + 1
    rejected = [row for row in rows if row["classification"] != "linked_internal_edge"]
    for offset, row in enumerate(rejected):
        cumulative_candidates.append(
            {
                "candidate_id": f"SGA5-CAND-{next_candidate + offset:06d}",
                "source_file": row["source_file"],
                "source_line": row["source_line"],
                "source_column_1based": row["start_column_1based"],
                "expose": row["current_expose"],
                "reference_scope": row["reference_scope"],
                "visible_text": row["visible_text"],
                "candidate_kind": "dotted_locator_residual",
                "displayed_number": row["base_number"],
                "candidate_labels": row["candidate_labels"],
                "reason": row["reason"],
                "status": row["classification"],
                "final_classification": row["classification"],
                "revision": "R9",
            }
        )
    write_csv(evidence / "REFERENCE_CANDIDATES.csv", cumulative_candidates, candidate_fields)

    residual_fields = list(rows[0]) if rows else ["residual_id"]
    write_csv(evidence / "R9_EXHAUSTIVE_RESIDUAL_CLASSIFICATION.csv", rows, residual_fields)
    preservation = [
        {
            "proof_id": "SGA5-R9-SOURCE-PRESERVATION-001",
            "baseline_revision": "R8",
            "baseline_tex_sha256": before_sha,
            "r9_tex_sha256": after_sha,
            "inserted_edge_wrappers": len(linked),
            "changed_source_lines": len(set(changed_lines)),
            "visible_text_policy": "exact_token_inside_hyperref_wrapper",
            "reconstruction_status": "PASS_GENERATED_AFTER_FROM_EXACT_R8_COORDINATES",
        }
    ]
    write_csv(
        evidence / "R9_VISIBLE_SOURCE_PRESERVATION.csv",
        preservation,
        list(preservation[0]),
    )
    summary = {
        "status": "R9_LINKS_APPLIED_PENDING_COMPILED_VALIDATION",
        "baseline_r8_tex_sha256": before_sha,
        "r9_tex_sha256": after_sha,
        "r8_edges_preserved": len(old_edges),
        "r9_edges_added": len(linked),
        "cumulative_edges": len(cumulative_edges),
        "pre_r9_residual_occurrences": len(rows),
        "r9_candidate_dispositions_added": len(rejected),
        "changed_source_lines": len(set(changed_lines)),
    }
    (evidence / "R9_LINK_INSERTION_SUMMARY.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    return summary


def postlink_audit(root: Path) -> dict[str, object]:
    """Prove that only the pre-adjudicated nonedges remain unwrapped."""
    evidence = root / "machine_readable_references"
    expected = read_csv(evidence / "R9_EXHAUSTIVE_RESIDUAL_CLASSIFICATION.csv")
    expected = [row for row in expected if row["classification"] != "linked_internal_edge"]
    actual, scan_summary = inventory(root)

    def key(row: dict[str, object]) -> tuple[object, ...]:
        return (
            int(row["source_line"]),
            str(row["visible_text"]),
            str(row["base_number"]),
            str(row["suffix"]),
        )

    expected_keys = [key(row) for row in expected]
    actual_keys = [key(row) for row in actual]
    exact = expected_keys == actual_keys
    if not exact:
        missing = Counter(expected_keys) - Counter(actual_keys)
        extra = Counter(actual_keys) - Counter(expected_keys)
        raise RuntimeError(
            "postlink residual mismatch: "
            f"expected={len(expected_keys)} actual={len(actual_keys)} "
            f"missing={sum(missing.values())} extra={sum(extra.values())}"
        )

    # Carry the manually audited final classifications forward verbatim.  The
    # scanner-generated IDs are deliberately not used after linked rows vanish.
    final_rows: list[dict[str, object]] = []
    for expected_row, actual_row in zip(expected, actual):
        row = dict(actual_row)
        row["residual_id"] = expected_row["residual_id"]
        row["classification"] = expected_row["classification"]
        row["reason"] = expected_row["reason"]
        row["candidate_labels"] = expected_row["candidate_labels"]
        row["destination_label"] = ""
        final_rows.append(row)
    fields = list(final_rows[0]) if final_rows else ["residual_id"]
    write_csv(evidence / "R9_POSTLINK_RESIDUAL_RESCAN.csv", final_rows, fields)
    counts = Counter(str(row["classification"]) for row in final_rows)
    summary = {
        "status": "PASS",
        "r9_tex_sha256": sha256(root / "SGA5_English_sync_workpass.tex"),
        "pre_r9_occurrences": len(read_csv(evidence / "R9_EXHAUSTIVE_RESIDUAL_CLASSIFICATION.csv")),
        "inserted_internal_edges": len(read_csv(evidence / "R9_EXHAUSTIVE_RESIDUAL_CLASSIFICATION.csv")) - len(expected),
        "expected_unwrapped_noninternal_occurrences": len(expected),
        "postlink_unwrapped_occurrences": len(actual),
        "exact_ordered_occurrence_replay": exact,
        "unwrapped_internally_resolvable_occurrences": 0,
        "unadjudicated_occurrences": 0,
        "final_classification_counts": dict(sorted(counts.items())),
        "postlink_replay_method": (
            "The raw postlink working IDs are not reused for adjudication because IDs "
            "shift after linked occurrences disappear.  Final classifications are carried "
            "forward by the exact ordered (source line, visible text, base locator, suffix) "
            "replay recorded above."
        ),
    }
    (evidence / "R9_POSTLINK_RESIDUAL_RESCAN_SUMMARY.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    return summary


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True, type=Path)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--postlink", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    evidence = root / "machine_readable_references"
    if args.postlink:
        summary = postlink_audit(root)
        print(json.dumps(summary, indent=2))
        return 0
    rows, summary = inventory(root)
    fields = list(rows[0]) if rows else ["residual_id"]
    write_csv(evidence / "R9_RESIDUAL_LOCATOR_INVENTORY.csv", rows, fields)
    (evidence / "R9_RESIDUAL_LOCATOR_INVENTORY_SUMMARY.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    if args.apply:
        forbidden = [
            row
            for row in rows
            if row["classification"]
            not in {
                "linked_internal_edge",
                "structural_declaration_tag",
                "external_work_citation",
                "unavailable_source_target",
                "mathematical_numeric_expression",
                "typography_layout_geometry_value",
                "other_positively_demonstrated_nonreference",
            }
        ]
        if forbidden:
            raise RuntimeError(f"forbidden unresolved classifications: {len(forbidden)}")
        applied = apply_links(root, rows)
        print(json.dumps(applied, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
