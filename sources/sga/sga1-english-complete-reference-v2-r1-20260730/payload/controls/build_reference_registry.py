#!/usr/bin/env python3
r"""Build the first stable-target layer for the complete SGA 1 reader.

The script reads the converged baseline AUX, the recursively loaded TeX
closure, and the bibliography declarations.  It emits:

* a TeX registry that adds zero-content stable PDF destinations whenever an
  active ``\label`` or ``\bibitem`` is executed;
* a rectangular target ledger; and
* the exact active source closure and hashes.

It deliberately does not guess prose edges.  Edge discovery and adjudication
are a separate, reviewable step.
"""

from __future__ import annotations

import csv
import hashlib
import re
import sys
from collections import Counter, deque
from dataclasses import dataclass
from pathlib import Path

from pypdf import PdfReader


MASTER_REL = "SGA1_English_source_sync_workpass.tex"
ROMANS = (
    ("XIII", 13),
    ("XII", 12),
    ("XI", 11),
    ("X", 10),
    ("IX", 9),
    ("VIII", 8),
    ("VII", 7),
    ("VI", 6),
    ("V", 5),
    ("IV", 4),
    ("III", 3),
    ("II", 2),
    ("I", 1),
)

ENV_KIND = {
    "proposition": "prop",
    "subproposition": "prop",
    "theorem": "thm",
    "theoreme": "thm",
    "theoremstar": "thm",
    "theoremedepurete": "thm",
    "theoremedefinition": "thm",
    "lemma": "lem",
    "lemme": "lem",
    "sublemme": "lem",
    "corollary": "cor",
    "corollaire": "cor",
    "corollaries": "cor",
    "definition": "def",
    "sectiondefinition": "def",
    "definitions": "def",
    "subdefinition": "def",
    "remark": "rem",
    "remarque": "rem",
    "remarques": "rem",
    "remarquestar": "rem",
    "remarquesstar": "rem",
    "subremarque": "rem",
    "example": "ex",
    "exemple": "ex",
    "exemples": "ex",
    "equation": "eq",
    "equation*": "eq",
    "align": "eq",
    "align*": "eq",
    "multline": "eq",
    "multline*": "eq",
}


@dataclass
class AuxLabel:
    key: str
    locator: str
    page: str
    title: str
    destination: str


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def read_group(text: str, start: int) -> tuple[str, int]:
    if start >= len(text) or text[start] != "{":
        raise ValueError(f"Expected braced group at offset {start}: {text!r}")
    depth = 0
    escaped = False
    for index in range(start, len(text)):
        char = text[index]
        if escaped:
            escaped = False
            continue
        if char == "\\":
            escaped = True
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return text[start + 1 : index], index + 1
    raise ValueError(f"Unclosed group: {text!r}")


def parse_aux_label(line: str) -> AuxLabel | None:
    prefix = r"\newlabel"
    if not line.startswith(prefix):
        return None
    key, position = read_group(line, len(prefix))
    outer, _ = read_group(line, position)
    if not outer.startswith("{"):
        # AMS TOC-indent cache entries are also written with \newlabel, but
        # their scalar payload is not a semantic document label.
        return None
    values: list[str] = []
    position = 0
    while position < len(outer):
        if outer[position].isspace():
            position += 1
            continue
        value, position = read_group(outer, position)
        values.append(value)
    while len(values) < 5:
        values.append("")
    return AuxLabel(key, values[0], values[1], values[2], values[3])


def active_closure(root: Path) -> list[str]:
    queue: deque[str] = deque([MASTER_REL])
    seen: list[str] = []
    while queue:
        relpath = queue.popleft().replace("\\", "/")
        if relpath in seen:
            continue
        path = root / Path(relpath)
        if not path.is_file():
            raise FileNotFoundError(f"Missing active dependency {relpath}")
        seen.append(relpath)
        text = path.read_text(encoding="utf-8")
        for match in re.finditer(r"\\(?:input|include)\{([^}]+)\}", text):
            queue.append(match.group(1))
    return seen


def source_occurrences(
    root: Path, closure: list[str], command: str
) -> dict[str, list[tuple[str, int, str]]]:
    occurrences: dict[str, list[tuple[str, int, str]]] = {}
    pattern = re.compile(
        rf"\\{command}(?:\[[^\]]*\])?\{{([^}}]+)\}}"
    )
    for relpath in closure:
        text = (root / Path(relpath)).read_text(encoding="utf-8")
        for match in pattern.finditer(text):
            line = text.count("\n", 0, match.start()) + 1
            occurrences.setdefault(match.group(1), []).append(
                (relpath, line, text[max(0, match.start() - 700) : match.start()])
            )
    return occurrences


def infer_expose(key: str) -> tuple[str, int | None]:
    probe = re.sub(r"^(?:eq|cor|prop|thm|lem|def|rem|note|page):", "", key)
    probe = re.sub(r"^(?:n|p)(?=[IVX])", "", probe)
    for roman, number in ROMANS:
        if re.match(rf"^{roman}(?:[.:]|$)", probe):
            return roman, number
    return "", None


def infer_kind(label: AuxLabel, before: str) -> str:
    key = label.key
    if key.startswith(("eq:", "eq")):
        return "eq"
    if key.startswith("cor:"):
        return "cor"
    if key.startswith(("indnot:", "ind:")):
        return "index"
    if key.startswith(("note-", "n")) and infer_expose(key)[1] is not None:
        return "note"
    if key.startswith("page-"):
        return "page"

    destination_prefix = label.destination.split(".", 1)[0].rstrip("*")
    if destination_prefix in {"chapter", "section", "subsection", "subsubsection"}:
        return {
            "chapter": "chapter",
            "section": "sec",
            "subsection": "subsec",
            "subsubsection": "subsubsec",
        }[destination_prefix]
    if destination_prefix == "equation":
        return "eq"
    if destination_prefix == "footnote":
        return "note"

    begin_matches = list(
        re.finditer(r"\\begin\{([A-Za-z*]+)\}", before)
    )
    end_matches = list(re.finditer(r"\\end\{([A-Za-z*]+)\}", before))
    if begin_matches:
        last_begin = begin_matches[-1]
        last_end_position = end_matches[-1].start() if end_matches else -1
        if last_begin.start() > last_end_position:
            environment = last_begin.group(1)
            if environment in ENV_KIND:
                return ENV_KIND[environment]

    tail = before[-350:]
    paragraph_match = re.search(
        r"\\paragraph\{([^}]*)\}[^{}]*$", tail, re.DOTALL
    )
    if paragraph_match:
        heading = paragraph_match.group(1).lower()
        for word, kind in (
            ("remark", "rem"),
            ("definition", "def"),
            ("theorem", "thm"),
            ("proposition", "prop"),
            ("corollary", "cor"),
            ("lemma", "lem"),
            ("example", "ex"),
        ):
            if word in heading:
                return kind
        return "para"

    if destination_prefix == "proposition":
        return "statement"
    return destination_prefix or "anchor"


def slug(value: str) -> str:
    value = value.replace(r"\mathrm", "").replace(r"\textup", "")
    value = value.lower()
    value = value.replace("*", "star").replace("'", "prime")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "unnamed"


def stable_target_id(
    label: AuxLabel,
    kind: str,
    used: set[str],
) -> tuple[str, str, str]:
    roman, expose_number = infer_expose(label.key)
    context = f"e{expose_number:02d}" if expose_number is not None else "reader"
    locator = label.locator or label.key
    locator = re.sub(rf"^{roman}\.?", "", locator) if roman else locator
    locator_slug = slug(locator)
    if kind in {"index", "note", "page", "anchor"}:
        locator_slug = slug(label.key)
    candidate = f"sga1.{context}.{kind}.{locator_slug}"
    if candidate in used:
        candidate = f"{candidate}.key-{slug(label.key)}"
    if candidate in used:
        raise RuntimeError(f"Stable target collision for {label.key}: {candidate}")
    used.add(candidate)
    return candidate, roman, context


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="raise")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    if len(sys.argv) not in {2, 3}:
        raise SystemExit(
            "usage: build_reference_registry.py ROOT [BUILD_DIRECTORY]"
        )
    root = Path(sys.argv[1]).resolve()
    build_directory = (
        Path(sys.argv[2]) if len(sys.argv) == 3 else Path("build_hypertexnames_false")
    )
    aux_path = root / build_directory / (
        "SGA1_English_source_sync_workpass.aux"
    )
    if not aux_path.is_file():
        raise FileNotFoundError(aux_path)

    closure = active_closure(root)
    label_occurrences = source_occurrences(root, closure, "label")
    bib_occurrences = source_occurrences(root, closure, "bibitem")

    aux_labels: list[AuxLabel] = []
    for line in aux_path.read_text(encoding="utf-8", errors="replace").splitlines():
        label = parse_aux_label(line)
        if label is not None:
            aux_labels.append(label)
    aux_counts = Counter(label.key for label in aux_labels)
    duplicate_aux = {key: count for key, count in aux_counts.items() if count > 1}
    if duplicate_aux:
        raise RuntimeError(f"Duplicate compiled AUX labels: {duplicate_aux}")

    used_ids: set[str] = set()
    target_rows: list[dict[str, object]] = []
    label_to_target: dict[str, str] = {}
    closure_order = {relpath: index for index, relpath in enumerate(closure)}
    for label in aux_labels:
        occurrences = label_occurrences.get(label.key, [])
        if not occurrences:
            # Hyperref and AMS may create internal AUX labels.  Only
            # source-declared semantic labels are admitted here.
            continue
        relpath, line, before = occurrences[-1]
        kind = infer_kind(label, before)
        target_id, roman, context = stable_target_id(label, kind, used_ids)
        label_to_target[label.key] = target_id
        target_rows.append(
            {
                "target_id": target_id,
                "latex_label": label.key,
                "aux_locator": label.locator,
                "baseline_pdf_destination": label.destination,
                "expose": roman,
                "context": context,
                "kind": kind,
                "title": label.title,
                "compiled_page": label.page,
                "source_relpath": relpath,
                "source_line": line,
                "source_occurrence_count": len(occurrences),
                "compiled_status": "baseline_aux_present",
            }
        )

    bib_rows: list[dict[str, object]] = []
    for key, occurrences in bib_occurrences.items():
        relpath, line, _ = occurrences[-1]
        roman, expose_number = infer_expose(key)
        context = f"e{expose_number:02d}" if expose_number is not None else "reader"
        target_id = f"sga1.{context}.bib.{slug(key)}"
        if target_id in used_ids:
            raise RuntimeError(f"Bibliography target collision: {target_id}")
        used_ids.add(target_id)
        bib_rows.append(
            {
                "target_id": target_id,
                "latex_label": f"bib:{key}",
                "aux_locator": key,
                "baseline_pdf_destination": f"cite.{key}",
                "expose": roman,
                "context": context,
                "kind": "bib",
                "title": "",
                "compiled_page": "",
                "source_relpath": relpath,
                "source_line": line,
                "source_occurrence_count": len(occurrences),
                "compiled_status": "source_bibitem_present",
            }
        )

    target_rows.extend(bib_rows)

    # Some live PDF links target generated anchors that have no explicit
    # source \label: footnote return anchors and a small number of unlabelled
    # chapter/section anchors.  They still need stable aliases if every
    # internal action in the delivered reader is to resolve through the
    # stable namespace.
    baseline_pdf = (
        root
        / build_directory
        / "SGA1_English_source_sync_workpass.pdf"
    )
    baseline_reader = PdfReader(str(baseline_pdf))
    incoming_destinations: Counter[str] = Counter()
    for page in baseline_reader.pages:
        for annotation_ref in page.get("/Annots", []):
            annotation = annotation_ref.get_object()
            if annotation.get("/Subtype") != "/Link":
                continue
            action_ref = annotation.get("/A")
            if action_ref is None:
                continue
            action = action_ref.get_object()
            if action.get("/S") == "/GoTo":
                incoming_destinations[str(action.get("/D"))] += 1

    represented_destinations = {
        str(row["baseline_pdf_destination"]) for row in target_rows
    }
    missing_compiled_destinations = sorted(
        set(incoming_destinations).difference(baseline_reader.named_destinations)
    )
    if missing_compiled_destinations:
        raise RuntimeError(
            "Baseline GoTo actions have no named destination: "
            f"{missing_compiled_destinations[:20]}"
        )

    generated_rows: list[dict[str, object]] = []
    for destination in sorted(
        set(incoming_destinations).difference(represented_destinations)
    ):
        if destination.startswith("Hfootnote."):
            kind = "footnote"
            suffix = destination.removeprefix("Hfootnote.")
            target_id = f"sga1.reader.footnote.{slug(suffix)}"
        else:
            kind = "generated"
            target_id = f"sga1.reader.generated.{slug(destination)}"
        if target_id in used_ids:
            raise RuntimeError(
                f"Generated-link target collision for {destination}: {target_id}"
            )
        used_ids.add(target_id)
        compiled_destination = baseline_reader.named_destinations[destination]
        generated_rows.append(
            {
                "target_id": target_id,
                "latex_label": "",
                "aux_locator": destination,
                "baseline_pdf_destination": destination,
                "expose": "",
                "context": "reader",
                "kind": kind,
                "title": "",
                "compiled_page": (
                    baseline_reader.get_destination_page_number(
                        compiled_destination
                    )
                    + 1
                ),
                "source_relpath": "",
                "source_line": "",
                "source_occurrence_count": incoming_destinations[destination],
                "compiled_status": "baseline_generated_link_target",
            }
        )
    target_rows.extend(generated_rows)

    target_rows.sort(
        key=lambda row: (
            closure_order.get(str(row["source_relpath"]), len(closure)),
            int(row["source_line"] or 0),
            str(row["target_id"]),
        )
    )

    controls = root / "controls"
    write_csv(
        controls / "REFERENCE_TARGETS.csv",
        target_rows,
        [
            "target_id",
            "latex_label",
            "aux_locator",
            "baseline_pdf_destination",
            "expose",
            "context",
            "kind",
            "title",
            "compiled_page",
            "source_relpath",
            "source_line",
            "source_occurrence_count",
            "compiled_status",
        ],
    )

    closure_rows: list[dict[str, object]] = []
    for order, relpath in enumerate(closure, 1):
        path = root / Path(relpath)
        closure_rows.append(
            {
                "dependency_order": order,
                "relative_path": relpath,
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
        )
    write_csv(
        controls / "SOURCE_CLOSURE.csv",
        closure_rows,
        ["dependency_order", "relative_path", "bytes", "sha256"],
    )

    registry_lines = [
        "% Generated stable semantic destinations for the SGA 1 reader.",
        "% Visible text and numbering are unchanged.",
        r"\makeatletter",
        (
            r"\newcommand{\sgaStableTarget}[1]{"
            r"\pdfdest name{#1} xyz}"
        ),
    ]
    for key, target_id in sorted(label_to_target.items()):
        registry_lines.append(
            rf"\expandafter\def\csname sga@target@{key}\endcsname{{{target_id}}}"
        )
    for row in sorted(bib_rows, key=lambda row: str(row["latex_label"])):
        key = str(row["latex_label"])[4:]
        registry_lines.append(
            rf"\expandafter\def\csname sga@bib@{key}\endcsname"
            rf"{{{row['target_id']}}}"
        )
    registry_lines.extend(
        [
            r"\let\sgaOriginalLabel\label",
            r"\renewcommand{\label}[1]{%",
            r"  \sgaOriginalLabel{#1}%",
            r"  \ifcsname sga@target@#1\endcsname",
            (
                r"    \expandafter\sgaStableTarget\expandafter"
                r"{\csname sga@target@#1\endcsname}%"
            ),
            r"  \fi",
            r"}",
            r"\let\sgaOriginalBibitem\bibitem",
            r"\newcommand{\sgaBibTarget}[1]{%",
            r"  \ifcsname sga@bib@#1\endcsname",
            (
                r"    \expandafter\sgaStableTarget\expandafter"
                r"{\csname sga@bib@#1\endcsname}%"
            ),
            r"  \fi",
            r"}",
            r"\newcommand{\sgaBibitemPlain}[1]{%",
            r"  \sgaOriginalBibitem{#1}\sgaBibTarget{#1}}",
            r"\newcommand{\sgaBibitemOptional}[2][]{%",
            r"  \sgaOriginalBibitem[#1]{#2}\sgaBibTarget{#2}}",
            r"\renewcommand{\bibitem}{%",
            r"  \@ifnextchar[\sgaBibitemOptional\sgaBibitemPlain}",
            r"\makeatother",
            "",
        ]
    )
    (root / "SGA1_reference_v2_registry.tex").write_text(
        "\n".join(registry_lines), encoding="utf-8", newline="\n"
    )

    link_lines = [
        "% Generated stable-link dispatch for the SGA 1 reader.",
        "% Stable destinations are emitted by SGA1_reference_v2_registry.tex.",
        r"\makeatletter",
    ]
    for key, target_id in sorted(label_to_target.items()):
        link_lines.append(
            rf"\expandafter\def\csname sga@target@{key}\endcsname{{{target_id}}}"
        )
    link_lines.extend(
        [
            r"\let\sgaOriginalRef\ref",
            r"\let\sgaOriginalPageref\pageref",
            r"\renewcommand{\ref}[1]{%",
            r"  \ifcsname sga@target@#1\endcsname",
            (
                r"    \hyperlink{\csname sga@target@#1\endcsname}"
                r"{\sgaOriginalRef*{#1}}%"
            ),
            r"  \else",
            r"    \sgaOriginalRef{#1}%",
            r"  \fi",
            r"}",
            r"\renewcommand{\pageref}[1]{%",
            r"  \ifcsname sga@target@#1\endcsname",
            (
                r"    \hyperlink{\csname sga@target@#1\endcsname}"
                r"{\sgaOriginalPageref*{#1}}%"
            ),
            r"  \else",
            r"    \sgaOriginalPageref{#1}%",
            r"  \fi",
            r"}",
            r"\renewcommand{\eqref}[1]{%",
            r"  \ifcsname sga@target@#1\endcsname",
            (
                r"    \hyperlink{\csname sga@target@#1\endcsname}"
                r"{\textup{\tagform@{\sgaOriginalRef*{#1}}}}%"
            ),
            r"  \else",
            r"    \textup{\tagform@{\sgaOriginalRef{#1}}}%",
            r"  \fi",
            r"}",
            r"\makeatother",
            "",
        ]
    )
    (root / "SGA1_reference_v2_links.tex").write_text(
        "\n".join(link_lines), encoding="utf-8", newline="\n"
    )

    summary = {
        "closure_files": len(closure),
        "closure_bytes": sum(
            (root / Path(relpath)).stat().st_size for relpath in closure
        ),
        "compiled_aux_labels": len(aux_labels),
        "source_semantic_targets": len(label_to_target),
            "bibliography_targets": len(bib_rows),
            "generated_link_targets": len(generated_rows),
            "total_stable_targets": len(target_rows),
        "unique_target_ids": len(used_ids),
    }
    print(summary)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
