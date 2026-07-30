#!/usr/bin/env python3
"""Inventory source-visible SGA 1 locators not already in link commands."""

from __future__ import annotations

import csv
import hashlib
import re
import sys
from collections import defaultdict
from pathlib import Path


ROMAN_SGA1 = r"(?:XIII|XII|XI|VIII|VII|VI|IV|III|II|IX|X|V|I)"
ROMAN_ALL = (
    r"(?:XXVI|XXV|XXIV|XXIII|XXII|XXI|XX|XIX|XVIII|XVII|XVI|XV|XIV|"
    r"XIII|XII|XI|VIII|VII|VI|IV|III|II|IX|X|V|I)"
)
SGA1_EXPOSES = {
    "I",
    "II",
    "III",
    "IV",
    "V",
    "VI",
    "VII",
    "VIII",
    "IX",
    "X",
    "XI",
    "XII",
    "XIII",
}
EXPOSE_RE = re.compile(
    rf"(?i:\bExpos(?:e|é|\\'e))\s*~?\s*(?P<roman>{ROMAN_ALL})\b"
)
CHAPTER_RE = re.compile(
    rf"(?i:\bChapter)\s*~?\s*(?P<roman>{ROMAN_ALL})\b"
)
NAMED_RE = re.compile(
    rf"(?i:\b(?:Proposition|Theorem|Lemma|Corollary|Definition|"
    rf"Remarks?|Examples?|Sections?|no\.))"
    rf"\s*(?:~|\\ |\s)*"
    rf"(?P<roman>{ROMAN_ALL})[\s~.,]+"
    rf"(?P<number>\d+(?:\.\d+){{0,3}}(?:\s*(?:bis|ter))?)"
)
NAMED_LOCAL_RE = re.compile(
    r"(?i:\bno\.)\s*~?\s*(?P<number>\d+(?:\.\d+){1,3})"
)
FULL_DOT_RE = re.compile(
    rf"(?<![A-Za-z\\])(?P<roman>{ROMAN_ALL})\."
    rf"(?P<number>\d+(?:\.\d+){{0,3}})(?![\d])"
)
FULL_SPACE_RE = re.compile(
    rf"(?<![A-Za-z\\])(?P<roman>{ROMAN_ALL})(?:~|\\ |[\s,])+"
    rf"(?:§+\s*)?(?P<number>\d+(?:\.\d+){{0,3}})(?![\d])"
)
BARE_RE = re.compile(
    r"(?<![A-Za-z0-9\\])(?P<number>\d+\.\d+(?:\.\d+){0,2})"
    r"(?:\s*(?:bis|ter))?(?![\d])"
)
MASK_RE = re.compile(
    r"\\(?:ref|Ref|eqref|pageref|cite|Cref|autoref)\*?"
    r"(?:\[[^\]]*\])?\{[^{}]*\}"
    r"|\\hyperref\[[^\]]+\]\{[^{}]*\}"
    r"|\\label\{[^{}]*\}"
    r"|\\bibitem(?:\[[^\]]*\])?\{[^{}]*\}"
    r"|\\tag\{[^{}]*\}"
)
FILE_EXPOSE_RE = re.compile(
    rf"SGA1_(?P<roman>{ROMAN_SGA1})(?:_|\.|$)"
)
DECLARATION_RE = re.compile(
    r"\\(?:chapter|section|subsection|subsubsection|paragraph)"
    r"\*?\{|\\begin\{[^{}]*(?:theorem|proposition|lemma|corollary|"
    r"definition|remark|example)[^{}]*\}(?:\[[^\]]*\])?",
    re.IGNORECASE,
)
EXTERNAL_RE = re.compile(
    r"(?:"
    r"\bEGA\b|"
    r"\bSGA\s*~?\s*(?:[2456]|0|XIII|XII|XI|VIII|VII|VI|IV|III|II|IX|X|V|I)"
    r"|Bourbaki|Alg[eè]bre|Commutative Algebra|GAGA|multiplodoque"
    r")",
    re.IGNORECASE,
)
KIND_PRIORITY = {
    "chapter": 0,
    "sec": 1,
    "prop": 2,
    "thm": 3,
    "cor": 4,
    "lem": 5,
    "def": 6,
    "statement": 7,
    "rem": 8,
    "ex": 9,
    "eq": 10,
    "bib": 11,
    "note": 12,
    "footnote": 13,
    "page": 14,
    "index": 15,
    "anchor": 16,
    "generated": 17,
}
OVERRIDES = {
    (
        "SGA1_English_source_sync_workpass.tex",
        339,
        "no.~1.2",
    ): (
        "internal_reference",
        "insert_link",
        "anaphoric continuation of Exposé III on the same line",
        "III.1.2",
    ),
    (
        "SGA1_English_source_sync_workpass.tex",
        448,
        "no.~1.2",
    ): (
        "internal_reference",
        "insert_link",
        "anaphoric continuation of Exposé III on the preceding line",
        "III.1.2",
    ),
    (
        "drafts/SGA1_IV_INTRODUCTION_English.texfrag",
        8,
        "Chapter~IV",
    ): (
        "external_work_reference",
        "positive_residual",
        "forthcoming EGA chapter, not SGA 1 Exposé IV",
        "",
    ),
    (
        "drafts/SGA1_I_11_English.texfrag",
        16,
        "Chapter~VI",
    ): (
        "external_work_reference",
        "positive_residual",
        "future multiplodoque chapter, not SGA 1 Exposé VI",
        "",
    ),
    (
        "drafts/SGA1_I_5_English_source_draft.texfrag",
        213,
        "no.~5.9",
    ): (
        "internal_reference",
        "insert_link",
        "anaphoric continuation of preceding Exposé IV locator",
        "IV.5.9",
    ),
    (
        "drafts/SGA1_V_OPENING_THROUGH_1_4_English.texfrag",
        12,
        "no.~9.7",
    ): (
        "internal_reference",
        "insert_link",
        "anaphoric continuation of preceding Exposé I locator",
        "I.9.7",
    ),
    (
        "drafts/SGA1_II_5_6_THROUGH_5_7_English.texfrag",
        41,
        "Exposé~II",
    ): (
        "internal_reference",
        "insert_link",
        "explicit reference to terminal Exposé II errata",
        "II.fin.errata",
    ),
    (
        "drafts/SGA1_I_6_English_source_draft.texfrag",
        12,
        "no.~I.7",
    ): (
        "internal_reference",
        "insert_link",
        "explicit SGA 1 Exposé I §7 locator",
        "I.7",
    ),
    (
        "drafts/SGA1_I_9_2_English_source_draft.texfrag",
        19,
        "I.9.2",
    ): (
        "ambiguous_duplicate_source_number",
        "positive_residual",
        "sentence explicitly discusses two statements printed as I.9.2",
        "",
    ),
    (
        "drafts/SGA1_VI_OPENING_THROUGH_1_English.texfrag",
        130,
        "VI.1",
    ): (
        "bibliography_reference",
        "insert_link",
        "phrase says reference cited as VI.1",
        "bib:VI.1",
    ),
    (
        "drafts/SGA1_VI_OPENING_THROUGH_1_English.texfrag",
        179,
        "VI.1",
    ): (
        "bibliography_reference",
        "insert_link",
        "VI.1 is the cited bibliography work containing locator I.1.2",
        "bib:VI.1",
    ),
    (
        "drafts/SGA1_VI_OPENING_THROUGH_1_English.texfrag",
        179,
        "I.1.2",
    ): (
        "external_work_reference",
        "positive_residual",
        "locator inside bibliography item VI.1, not an SGA 1 locator",
        "",
    ),
    (
        "drafts/SGA1_VIII_1_A_English.texfrag",
        113,
        "VII,~8",
    ): (
        "unavailable_expose_reference",
        "positive_residual",
        "printed reference to nonexistent SGA 1 Exposé VII",
        "",
    ),
    (
        "drafts/SGA1_VIII_7_A_English.texfrag",
        11,
        "VII,~9",
    ): (
        "inactive_source_branch",
        "positive_residual",
        "inactive orig=true branch; Exposé VII does not exist",
        "",
    ),
    (
        "drafts/SGA1_VIII_7_A_English.texfrag",
        12,
        "VII,~9",
    ): (
        "unavailable_expose_reference",
        "positive_residual",
        "active corrected branch explicitly discloses nonexistent section",
        "",
    ),
    (
        "drafts/SGA1_XIII_2_2_OPENING_THROUGH_THEOREM_English.texfrag",
        42,
        "III~2.1.7",
    ): (
        "inactive_source_branch",
        "positive_residual",
        "inactive orig=true branch; active branch uses a bibliography citation",
        "",
    ),
    (
        "drafts/SGA1_X_2_B_English.texfrag",
        95,
        "Theorem X~3.10",
    ): (
        "external_work_reference",
        "positive_residual",
        "explicit SGA 2 theorem locator in the preceding footnote",
        "",
    ),
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def active_prefix(line: str) -> str:
    escaped = False
    for index, char in enumerate(line):
        if char == "%" and not escaped:
            return line[:index]
        escaped = char == "\\" and not escaped
        if char != "\\":
            escaped = False
    return line


def canonical_rows(
    rows: list[dict[str, str]],
) -> dict[str, dict[str, str]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        for locator in (row["latex_label"], row["aux_locator"]):
            if locator:
                grouped[locator].append(row)
    return {
        locator: min(
            candidates,
            key=lambda row: (
                0 if row["aux_locator"] == locator else 1,
                KIND_PRIORITY.get(row["kind"], 99),
                row["target_id"],
            ),
        )
        for locator, candidates in grouped.items()
    }


def infer_file_expose(
    relpath: str,
    line_number: int,
    target_rows: list[dict[str, str]],
) -> str:
    prior = [
        row
        for row in target_rows
        if row["source_relpath"] == relpath
        and row["expose"]
        and int(row["source_line"] or 0) <= line_number
    ]
    if prior:
        return max(prior, key=lambda row: int(row["source_line"]))["expose"]
    match = FILE_EXPOSE_RE.search(Path(relpath).name)
    return match.group("roman") if match else ""


def normalized_locator(
    family: str,
    match: re.Match[str],
    current_expose: str,
) -> str:
    if family in {"expose", "chapter"}:
        return match.group("roman")
    if family in {"named", "full_dot", "full_space"}:
        number = re.sub(r"\s+", " ", match.group("number").strip())
        return f"{match.group('roman')}.{number}".replace(" ", ".")
    number = re.sub(r"\s+", " ", match.group("number").strip())
    return f"{current_expose}.{number}".replace(" ", ".") if current_expose else ""


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit("usage: discover_raw_reference_candidates.py ROOT")
    root = Path(sys.argv[1]).resolve()
    controls = root / "controls"
    with (controls / "SOURCE_CLOSURE.csv").open(
        "r", encoding="utf-8-sig", newline=""
    ) as handle:
        closure = list(csv.DictReader(handle))
    with (controls / "REFERENCE_TARGETS.csv").open(
        "r", encoding="utf-8-sig", newline=""
    ) as handle:
        target_rows = list(csv.DictReader(handle))
    target_by_locator = canonical_rows(target_rows)

    candidates: list[dict[str, object]] = []
    detector_patterns = (
        ("named", NAMED_RE),
        ("named_local", NAMED_LOCAL_RE),
        ("expose", EXPOSE_RE),
        ("chapter", CHAPTER_RE),
        ("full_dot", FULL_DOT_RE),
        ("full_space", FULL_SPACE_RE),
        ("bare_local", BARE_RE),
    )
    for closure_row in closure:
        relpath = closure_row["relative_path"]
        path = root / Path(relpath)
        text = path.read_text(encoding="utf-8", errors="replace")
        original_lines = text.splitlines()
        globally_masked = MASK_RE.sub(
            lambda match: "".join(
                "\n" if char == "\n" else " " for char in match.group()
            ),
            text,
        )
        masked_lines = globally_masked.splitlines()
        if len(original_lines) != len(masked_lines):
            raise RuntimeError(f"Mask changed line count: {relpath}")
        for line_number, (original_line, masked_line) in enumerate(
            zip(original_lines, masked_lines), 1
        ):
            active = active_prefix(original_line)
            if any(
                command in active
                for command in (
                    r"\newcommand",
                    r"\renewcommand",
                    r"\providecommand",
                    r"\newtheorem",
                    r"\DeclareMathOperator",
                    r"\bibitem",
                    r"\tag{",
                )
            ):
                continue
            if any(
                marker in active
                for marker in (r"\xymatrix", r"\ar@", r"@C=", r"@R=")
            ):
                continue
            masked = masked_line[: len(active)]
            current_expose = infer_file_expose(
                relpath, line_number, target_rows
            )
            matches: list[tuple[int, int, int, str, re.Match[str]]] = []
            for priority, (family, pattern) in enumerate(detector_patterns):
                for match in pattern.finditer(masked):
                    matches.append(
                        (match.start(), match.end(), priority, family, match)
                    )
            selected: list[tuple[int, int, int, str, re.Match[str]]] = []
            for item in sorted(
                matches, key=lambda value: (value[0], value[2], -value[1])
            ):
                start, end, _, _, _ = item
                if any(
                    start < chosen_end and end > chosen_start
                    for chosen_start, chosen_end, *_ in selected
                ):
                    continue
                selected.append(item)

            for start, end, _, family, match in selected:
                visible = active[start:end]
                locator = normalized_locator(family, match, current_expose)
                target = target_by_locator.get(locator)
                preceding = " ".join(
                    original_lines[max(0, line_number - 3) : line_number - 1]
                )
                left_context = (
                    preceding + " " + active[max(0, start - 100) : start]
                )
                full_context = active.strip()
                declaration = bool(DECLARATION_RE.search(active[:end]))
                external = bool(EXTERNAL_RE.search(left_context))
                roman = (
                    match.groupdict().get("roman")
                    if "roman" in match.groupdict()
                    else ""
                )

                if declaration:
                    classification = "structural_declaration"
                    disposition = "positive_residual"
                    reason = "source-visible declaration, not a reference edge"
                    target = target or target_by_locator.get(locator)
                elif roman == "VII" and target is None:
                    classification = "unavailable_expose_reference"
                    disposition = "positive_residual"
                    reason = "Exposé VII does not exist in SGA 1"
                    target = None
                elif external or (roman and roman not in SGA1_EXPOSES):
                    classification = "external_work_reference"
                    disposition = "positive_residual"
                    reason = "nearby work identifier scopes locator outside SGA 1"
                    target = None
                elif target is not None:
                    classification = "internal_reference"
                    disposition = "insert_link"
                    reason = "unique active SGA 1 target"
                else:
                    classification = "unresolved_locator_like"
                    disposition = "needs_review"
                    reason = "no unique active SGA 1 target"

                override = OVERRIDES.get(
                    (relpath, line_number, visible)
                )
                if override is not None:
                    (
                        classification,
                        disposition,
                        reason,
                        override_locator,
                    ) = override
                    target = (
                        target_by_locator.get(override_locator)
                        if override_locator
                        else None
                    )
                    if override_locator and target is None:
                        raise RuntimeError(
                            f"Override target missing: {override_locator}"
                        )
                    if override_locator:
                        locator = override_locator

                # Bare dotted strings are admitted only when they resolve
                # locally or are positively scoped as external/declarative.
                if (
                    family == "bare_local"
                    and disposition == "needs_review"
                ):
                    continue

                identity = (
                    f"{relpath}\0{line_number}\0{start + 1}\0{visible}"
                ).encode("utf-8")
                candidates.append(
                    {
                        "candidate_id": (
                            "sga1.candidate.sha256."
                            + hashlib.sha256(identity).hexdigest()
                        ),
                        "source_relpath": relpath,
                        "source_line": line_number,
                        "source_column": start + 1,
                        "detector_family": family,
                        "visible_text": visible,
                        "normalized_locator": locator,
                        "current_expose": current_expose,
                        "target_label": target["latex_label"] if target else "",
                        "target_id": target["target_id"] if target else "",
                        "classification": classification,
                        "disposition": disposition,
                        "reason": reason,
                        "context": full_context,
                        "context_sha256": sha256_bytes(
                            full_context.encode("utf-8")
                        ),
                        "source_sha256": closure_row["sha256"],
                        "status": (
                            "adjudicated"
                            if disposition != "needs_review"
                            else "needs_review"
                        ),
                    }
                )

    candidates.sort(
        key=lambda row: (
            str(row["source_relpath"]),
            int(row["source_line"]),
            int(row["source_column"]),
        )
    )
    output = controls / "REFERENCE_CANDIDATES.csv"
    fields = [
        "candidate_id",
        "source_relpath",
        "source_line",
        "source_column",
        "detector_family",
        "visible_text",
        "normalized_locator",
        "current_expose",
        "target_label",
        "target_id",
        "classification",
        "disposition",
        "reason",
        "context",
        "context_sha256",
        "source_sha256",
        "status",
    ]
    with output.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(candidates)
    counts: dict[str, int] = defaultdict(int)
    for row in candidates:
        counts[str(row["classification"])] += 1
    print(
        {
            "candidates": len(candidates),
            "classification_counts": dict(sorted(counts.items())),
            "needs_review": sum(
                row["status"] == "needs_review" for row in candidates
            ),
            "output": str(output),
        }
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
