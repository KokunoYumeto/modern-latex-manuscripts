#!/usr/bin/env python3
"""Index touched numbered-paper loci and every post-P43 structural unit."""

from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "release" / "source"
EVIDENCE = ROOT / "release" / "evidence"
AUTHORITY_MANIFEST = ROOT / "evidence" / "authority_units.json"
OUTPUT = EVIDENCE / "structural_index.jsonl"
CSV_OUTPUT = EVIDENCE / "structural_index.csv"
REPORT = EVIDENCE / "structural_index_build_report.json"
TARGETS = ("ru", "uk", "isv", "isv-cy")
LANGUAGE = {"ru": "ru-Cyrl", "uk": "uk-Cyrl", "isv": "isv-Latn", "isv-cy": "isv-Cyrl"}
SCRIPT = {"ru": "Cyrillic", "uk": "Cyrillic", "isv": "Latin", "isv-cy": "Cyrillic"}
SURFACE_ORDER = {"ru-Cyrl": 0, "uk-Cyrl": 1, "isv-Latn": 2, "isv-Cyrl": 3}

HEADING_RE = re.compile(r"\\(part|chapter|section|subsection|subsubsection|paragraph)\*?\s*\{")
BEGIN_RE = re.compile(r"\\begin\{(equation\*?|align\*?|gather\*?|multline\*?|displaymath)\}")
END_RE = re.compile(r"\\end\{(equation\*?|align\*?|gather\*?|multline\*?|displaymath)\}")
DISPLAY_OPEN_RE = re.compile(r"(?<!\\)\\\[")
DISPLAY_CLOSE_RE = re.compile(r"(?<!\\)\\\]")
LABEL_RE = re.compile(r"\\label\{([^{}]+)\}")
REF_RE = re.compile(r"\\(?:ref|eqref|pageref|autoref)\{([^{}]+)\}")
FOOTNOTE_RE = re.compile(r"\\footnote\{")
TOC_RE = re.compile(r"\\tocsec\{")
WORD_RE = re.compile(r"[A-Za-zÀ-žА-Яа-яІіЇїЄєҐґЈј]{3,}")
NEW_P06_FORMULA = (
    r"\Psi(z,u)=x_1^2z^2-x_1^4u_1^2-2x_1^3x_2u_1u_2-x_1^2x_2^2u_2^2."
)

NAMED = (
    ("definition", re.compile(r"(?i)definic|определени|означенн")),
    ("theorem", re.compile(r"(?i)teorem|теорем")),
    ("proposition", re.compile(r"(?i)propozic|tvrdžen|утвержден|твердженн")),
    ("lemma", re.compile(r"(?i)lem(?:a|u|y|ma)|лем(?:а|м|и)")),
    ("corollary", re.compile(r"(?i)korolar|poslěd|следств|наслід")),
    ("proof", re.compile(r"(?i)dokaz|доказательств|доведенн")),
    ("remark", re.compile(r"(?i)primět|zamětk|remark|замечани|примечани|зауваженн|примітк")),
    ("example", re.compile(r"(?i)priměr|primjer|пример|приклад")),
)


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha_file(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def command_end(lines: list[str], start_line: int, start_col: int) -> int:
    depth = 0
    opened = False
    escaped = False
    for index in range(start_line - 1, len(lines)):
        segment = lines[index][start_col:] if index == start_line - 1 else lines[index]
        for char in segment:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == "{":
                depth += 1
                opened = True
            elif char == "}" and opened:
                depth -= 1
                if depth == 0:
                    return index + 1
        start_col = 0
    return start_line


def preview(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()[:240]


def span_hash(lines: list[str], start: int, end: int) -> str:
    return sha_bytes("\n".join(lines[start - 1 : end]).encode("utf-8"))


def target_unit_spans(target: str) -> list[dict]:
    book = SOURCE / f"44-book-{target}.tex"
    post45 = SOURCE / f"45-{target}.tex"
    postbib = SOURCE / f"bib-{target}.tex"
    for path in (book, post45, postbib):
        if not path.exists():
            raise FileNotFoundError(path)

    spans = []
    lines = book.read_text(encoding="utf-8-sig").splitlines()
    begin_doc = next(index for index, line in enumerate(lines, 1) if r"\begin{document}" in line)
    markers = {}
    for index, line in enumerate(lines, 1):
        match = re.match(r"% BEGIN (BOOK_S\d{2})$", line.strip())
        if match:
            markers[match.group(1)] = [index + 1, None]
        match = re.match(r"% END (BOOK_S\d{2})$", line.strip())
        if match:
            markers[match.group(1)][1] = index - 1
    first_marker = min(start for start, _end in markers.values())
    spans.append({"unit_id": "BOOK_TITLE_INTRO", "path": book, "start": begin_doc, "end": first_marker - 2})
    for section in range(1, 32):
        unit_id = f"BOOK_S{section:02d}"
        start, end = markers[unit_id]
        spans.append({"unit_id": unit_id, "path": book, "start": start, "end": end})

    for unit_id, path in (("POST45", post45), ("POSTBIB", postbib)):
        lines = path.read_text(encoding="utf-8-sig").splitlines()
        start = next(index for index, line in enumerate(lines, 1) if r"\begin{document}" in line)
        end = next(index for index, line in enumerate(lines, 1) if r"\end{document}" in line)
        spans.append({"unit_id": unit_id, "path": path, "start": start, "end": end})
    return spans


def touched_numbered_paper_records(target: str, manifest: dict) -> list[dict]:
    """Index the inherited base as a bounded dependency and the exact P06 locus touched here."""
    path = SOURCE / f"base-papers1-43-{target}.tex"
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    file_hash = sha_file(path)
    authority_path = Path(manifest["authority"]["path"])
    authority_lines = authority_path.read_text(encoding="utf-8-sig").splitlines()
    authority_hash = manifest["authority"]["sha256"]
    first_post_p43 = min(unit["start_line"] for unit in manifest["units"])
    base_authority_end = first_post_p43 - 1
    formula_target_lines = [
        index for index, line in enumerate(lines, 1) if line.strip() == NEW_P06_FORMULA
    ]
    formula_authority_lines = [
        index for index, line in enumerate(authority_lines, 1) if line.strip() == NEW_P06_FORMULA
    ]
    if len(formula_target_lines) != 1 or len(formula_authority_lines) != 1:
        raise RuntimeError(
            f"{target}: expected one accepted P06 formula in target and authority; "
            f"got {formula_target_lines} / {formula_authority_lines}"
        )

    surface_role = (
        "deterministic_reader_projection" if target == "isv-cy" else "inherited_editable_translation"
    )
    records = []
    base_id = f"SLISV-V038-{target.upper().replace('-', '_')}-PAPERS_1_43_BASE-WORK_UNIT-0001"
    base_body = "\n".join(lines)
    records.append(
        {
            "schema_version": "noether-slavic-v038-structural-index/1.0",
            "structural_id": base_id,
            "work_id": "NOETHER-CUMULATIVE",
            "work_unit_id": "PAPERS_1_43_BASE",
            "structure_type": "work_unit",
            "type_ordinal": 1,
            "language": LANGUAGE[target],
            "script": SCRIPT[target],
            "surface_role": surface_role,
            "parent_id": None,
            "order_index": 0,
            "relations": {
                "pair_group": "PAPERS_1_43_BASE:work_unit:1",
                "paired_surface_ids": [],
                "labels": LABEL_RE.findall(base_body),
                "references": REF_RE.findall(base_body),
                "dependencies": [
                    "NOETH-DE-ED-0005",
                    "r19 archive-normalized 219-unit numbered-paper source",
                    "v014 producer freeze",
                ],
            },
            "authority_locator": {
                "path": authority_path.resolve().as_posix(),
                "start_line": 1,
                "end_line": base_authority_end,
                "file_sha256": authority_hash,
                "unit_sha256": span_hash(authority_lines, 1, base_authority_end),
                "mapping_precision": "work_unit",
            },
            "target_locator": {
                "path": path.resolve().as_posix(),
                "start_line": 1,
                "end_line": len(lines),
                "file_sha256": file_hash,
                "span_sha256": span_hash(lines, 1, len(lines)),
            },
            "completion_state": "release_source_present",
            "review_state": "machine_formula_and_structure_checked_no_native_review",
            "publication_state": "candidate_for_owner_handoff",
            "boundary_confidence": "high",
            "boundary_basis": (
                "exact archive-normalized Papers 1--43 base boundary; 219 producer units retained "
                "as inherited v014/r19 custody rather than reclassified as newly reviewed paragraphs"
            ),
            "continuation_cursor": None,
            "text_preview": "Archive-normalized complete cumulative translated source, numbered Papers 1--43.",
        }
    )

    target_line = formula_target_lines[0]
    authority_line = formula_authority_lines[0]
    p06_id = f"SLISV-V038-{target.upper().replace('-', '_')}-P06-WORK_UNIT-0001"
    p06_locator = {
        "path": path.resolve().as_posix(),
        "start_line": target_line,
        "end_line": target_line,
        "file_sha256": file_hash,
        "span_sha256": span_hash(lines, target_line, target_line),
    }
    p06_authority = {
        "path": authority_path.resolve().as_posix(),
        "start_line": authority_line,
        "end_line": authority_line,
        "file_sha256": authority_hash,
        "unit_sha256": span_hash(authority_lines, authority_line, authority_line),
        "mapping_precision": "work_unit",
    }
    common = {
        "work_id": "NOETHER-CUMULATIVE",
        "work_unit_id": "P06",
        "language": LANGUAGE[target],
        "script": SCRIPT[target],
        "surface_role": surface_role,
        "completion_state": "release_source_present",
        "review_state": "machine_formula_and_structure_checked_no_native_review",
        "publication_state": "candidate_for_owner_handoff",
        "boundary_confidence": "high",
        "boundary_basis": "exact accepted ED0005 P06 formula line matched on authority and target",
        "continuation_cursor": None,
        "text_preview": NEW_P06_FORMULA,
    }
    records.append(
        {
            "schema_version": "noether-slavic-v038-structural-index/1.0",
            "structural_id": p06_id,
            "structure_type": "work_unit",
            "type_ordinal": 1,
            "parent_id": base_id,
            "order_index": authority_line * 10,
            "relations": {
                "pair_group": "P06:work_unit:1",
                "paired_surface_ids": [],
                "labels": [],
                "references": [],
                "dependencies": ["NOETH-DE-ED-0005", "P06 accepted primary-print formula repair"],
            },
            "authority_locator": p06_authority,
            "target_locator": p06_locator,
            **common,
        }
    )
    records.append(
        {
            "schema_version": "noether-slavic-v038-structural-index/1.0",
            "structural_id": f"SLISV-V038-{target.upper().replace('-', '_')}-P06-EQUATION-0001",
            "structure_type": "equation",
            "type_ordinal": 1,
            "parent_id": p06_id,
            "order_index": authority_line * 10 + 1,
            "relations": {
                "pair_group": "P06:equation:1",
                "paired_surface_ids": [],
                "labels": [],
                "references": [],
                "dependencies": ["NOETH-DE-ED-0005", "P06 accepted primary-print formula repair"],
            },
            "authority_locator": p06_authority,
            "target_locator": p06_locator,
            **common,
        }
    )
    return records


def parse_span(target: str, unit: dict, authority: dict) -> list[dict]:
    path: Path = unit["path"]
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    file_hash = sha_file(path)
    start, end = unit["start"], unit["end"]
    structures = [
        {
            "type": "work_unit",
            "start": start,
            "end": end,
            "confidence": "high",
            "basis": "explicit release unit boundary",
        }
    ]

    # Headings and explicit structural commands.
    for line_number in range(start, end + 1):
        line = lines[line_number - 1]
        for match in HEADING_RE.finditer(line):
            heading_end = command_end(lines, line_number, match.start())
            kind = match.group(1).lower()
            structures.append(
                {
                    "type": kind,
                    "start": line_number,
                    "end": min(heading_end, end),
                    "confidence": "high",
                    "basis": f"explicit TeX {kind} command",
                }
            )
        for match in FOOTNOTE_RE.finditer(line):
            structures.append(
                {
                    "type": "note",
                    "start": line_number,
                    "end": min(command_end(lines, line_number, match.start()), end),
                    "confidence": "high",
                    "basis": "balanced TeX footnote argument",
                }
            )
        for match in TOC_RE.finditer(line):
            structures.append(
                {
                    "type": "toc_item",
                    "start": line_number,
                    "end": min(command_end(lines, line_number, match.start()), end),
                    "confidence": "high",
                    "basis": "explicit TeX tocsec command",
                }
            )

    # Display math, both bracketed and named environments.
    display_start = None
    env_stack: list[tuple[str, int]] = []
    for line_number in range(start, end + 1):
        line = lines[line_number - 1]
        if display_start is None and DISPLAY_OPEN_RE.search(line):
            display_start = line_number
        if display_start is not None and DISPLAY_CLOSE_RE.search(line):
            structures.append(
                {
                    "type": "equation_display",
                    "start": display_start,
                    "end": line_number,
                    "confidence": "high",
                    "basis": "explicit TeX bracketed display",
                }
            )
            display_start = None
        for match in BEGIN_RE.finditer(line):
            env_stack.append((match.group(1), line_number))
        for match in END_RE.finditer(line):
            env = match.group(1)
            for stack_index in range(len(env_stack) - 1, -1, -1):
                if env_stack[stack_index][0] == env:
                    _env, env_start = env_stack.pop(stack_index)
                    structures.append(
                        {
                            "type": "equation_display",
                            "start": env_start,
                            "end": line_number,
                            "confidence": "high",
                            "basis": f"explicit TeX {env} environment",
                        }
                    )
                    break

    # Blank-line-delimited closed prose units, including named mathematical prose.
    blocks: list[tuple[int, int]] = []
    block_start = None
    for line_number in range(start, end + 2):
        line = lines[line_number - 1] if line_number <= end else ""
        if line.strip() and not line.lstrip().startswith("%"):
            if block_start is None:
                block_start = line_number
        elif block_start is not None:
            blocks.append((block_start, line_number - 1))
            block_start = None
    for block_start, block_end in blocks:
        body = "\n".join(lines[block_start - 1 : block_end])
        stripped = body.strip()
        display_only = (
            (stripped.startswith(r"\[") and stripped.endswith(r"\]"))
            or stripped.startswith(r"\begin{align")
            or stripped.startswith(r"\begin{equation")
            or stripped.startswith(r"\begin{gather")
        )
        if not WORD_RE.search(body) or display_only:
            continue
        structure_type = "closed_prose_unit"
        prefix = re.sub(r"\\[A-Za-z@]+\*?", " ", body[:320])
        for named_type, expression in NAMED:
            if expression.search(prefix):
                structure_type = named_type
                break
        structures.append(
            {
                "type": structure_type,
                "start": block_start,
                "end": block_end,
                "confidence": "medium",
                "basis": "blank-line-delimited TeX source block"
                + (f" with {structure_type} lexical heading" if structure_type != "closed_prose_unit" else ""),
            }
        )

    # Bibliography items are important closed units even when they span lines.
    if unit["unit_id"] == "POSTBIB":
        item_lines = [
            line_number
            for line_number in range(start, end + 1)
            if re.match(r"\s*\\item(?:\[[^]]*\])?\b", lines[line_number - 1])
        ]
        for index, item_start in enumerate(item_lines):
            item_end = item_lines[index + 1] - 1 if index + 1 < len(item_lines) else end - 1
            structures.append(
                {
                    "type": "bibliography_item",
                    "start": item_start,
                    "end": max(item_start, item_end),
                    "confidence": "high",
                    "basis": "explicit TeX item within post-numbered bibliography",
                }
            )

    # Deduplicate same type/range; assign stable type ordinals.
    unique = {(item["type"], item["start"], item["end"]): item for item in structures}
    structures = sorted(unique.values(), key=lambda item: (item["start"], item["end"], item["type"]))
    type_counts = Counter()
    records = []
    authority_path = Path(authority["authority_path"])
    authority_locator = {
        "path": authority_path.resolve().as_posix(),
        "start_line": authority["start_line"],
        "end_line": authority["end_line"],
        "file_sha256": authority["authority_sha256"],
        "unit_sha256": authority["unit_sha256"],
        "mapping_precision": "work_unit",
    }
    for local_order, item in enumerate(structures):
        type_counts[item["type"]] += 1
        ordinal = type_counts[item["type"]]
        structural_id = (
            f"SLISV-V038-{target.upper().replace('-', '_')}-{unit['unit_id']}-"
            f"{item['type'].upper()}-{ordinal:04d}"
        )
        body = "\n".join(lines[item["start"] - 1 : item["end"]])
        records.append(
            {
                "schema_version": "noether-slavic-v038-structural-index/1.0",
                "structural_id": structural_id,
                "work_id": "NOETHER-CUMULATIVE",
                "work_unit_id": unit["unit_id"],
                "structure_type": item["type"],
                "type_ordinal": ordinal,
                "language": LANGUAGE[target],
                "script": SCRIPT[target],
                "surface_role": (
                    "deterministic_reader_projection" if target == "isv-cy" else "editable_model_authored_translation"
                ),
                "parent_id": None,
                "order_index": authority["order"] * 10000 + local_order,
                "relations": {
                    "pair_group": f"{unit['unit_id']}:{item['type']}:{ordinal}",
                    "paired_surface_ids": [],
                    "labels": LABEL_RE.findall(body),
                    "references": REF_RE.findall(body),
                    "dependencies": ["NOETH-DE-ED-0005", unit["unit_id"]],
                },
                "authority_locator": authority_locator,
                "target_locator": {
                    "path": path.resolve().as_posix(),
                    "start_line": item["start"],
                    "end_line": item["end"],
                    "file_sha256": file_hash,
                    "span_sha256": span_hash(lines, item["start"], item["end"]),
                },
                "completion_state": "release_source_present",
                "review_state": "machine_formula_and_structure_checked_no_native_review",
                "publication_state": "candidate_for_owner_handoff",
                "boundary_confidence": item["confidence"],
                "boundary_basis": item["basis"],
                "continuation_cursor": None,
                "text_preview": preview(body),
            }
        )

    # Attach non-unit structures to the smallest containing heading, or unit.
    unit_id = next(record["structural_id"] for record in records if record["structure_type"] == "work_unit")
    headings = [
        record
        for record in records
        if record["structure_type"] in {"part", "chapter", "section", "subsection", "subsubsection", "paragraph"}
    ]
    for record in records:
        if record["structure_type"] == "work_unit":
            continue
        start_line = record["target_locator"]["start_line"]
        containing = [
            heading
            for heading in headings
            if heading["target_locator"]["start_line"] <= start_line
        ]
        record["parent_id"] = containing[-1]["structural_id"] if containing else unit_id
    return records


def main() -> int:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    manifest = json.loads(AUTHORITY_MANIFEST.read_text(encoding="utf-8-sig"))
    authority_path = manifest["authority"]["path"]
    authority_sha = manifest["authority"]["sha256"]
    authority_units = {
        unit["unit_id"]: {
            "order": unit["order"],
            "start_line": unit["start_line"],
            "end_line": unit["end_line"],
            "unit_sha256": unit["lf_sha256"],
            "authority_path": authority_path,
            "authority_sha256": authority_sha,
        }
        for unit in manifest["units"]
    }
    records = []
    for target in TARGETS:
        records.extend(touched_numbered_paper_records(target, manifest))
        for unit in target_unit_spans(target):
            records.extend(parse_span(target, unit, authority_units[unit["unit_id"]]))

    pair_groups: dict[str, list[str]] = defaultdict(list)
    for record in records:
        pair_groups[record["relations"]["pair_group"]].append(record["structural_id"])
    for record in records:
        record["relations"]["paired_surface_ids"] = sorted(
            item
            for item in pair_groups[record["relations"]["pair_group"]]
            if item != record["structural_id"]
        )
    records.sort(
        key=lambda record: (
            SURFACE_ORDER[record["language"]],
            record["order_index"],
            record["structural_id"],
        )
    )
    for index, record in enumerate(records):
        record["continuation_cursor"] = records[index + 1]["structural_id"] if index + 1 < len(records) else None

    with OUTPUT.open("w", encoding="utf-8", newline="\n") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")

    fields = [
        "structural_id", "work_unit_id", "structure_type", "type_ordinal", "language", "script",
        "surface_role", "parent_id", "order_index", "authority_path", "authority_start_line",
        "authority_end_line", "target_path", "target_start_line", "target_end_line", "target_span_sha256",
        "completion_state", "review_state", "publication_state", "boundary_confidence", "continuation_cursor",
    ]
    with CSV_OUTPUT.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for record in records:
            writer.writerow(
                {
                    "structural_id": record["structural_id"],
                    "work_unit_id": record["work_unit_id"],
                    "structure_type": record["structure_type"],
                    "type_ordinal": record["type_ordinal"],
                    "language": record["language"],
                    "script": record["script"],
                    "surface_role": record["surface_role"],
                    "parent_id": record["parent_id"],
                    "order_index": record["order_index"],
                    "authority_path": record["authority_locator"]["path"],
                    "authority_start_line": record["authority_locator"]["start_line"],
                    "authority_end_line": record["authority_locator"]["end_line"],
                    "target_path": record["target_locator"]["path"],
                    "target_start_line": record["target_locator"]["start_line"],
                    "target_end_line": record["target_locator"]["end_line"],
                    "target_span_sha256": record["target_locator"]["span_sha256"],
                    "completion_state": record["completion_state"],
                    "review_state": record["review_state"],
                    "publication_state": record["publication_state"],
                    "boundary_confidence": record["boundary_confidence"],
                    "continuation_cursor": record["continuation_cursor"],
                }
            )

    report = {
        "schema": "noether-slavic-v038-structural-index-build-report/1.0",
        "generated_at": datetime.now().astimezone().isoformat(),
        "records": len(records),
        "surface_counts": dict(Counter(record["language"] for record in records)),
        "type_counts": dict(Counter(record["structure_type"] for record in records)),
        "work_units_per_surface": dict(
            Counter(record["language"] for record in records if record["structure_type"] == "work_unit")
        ),
        "unpaired_records": sum(not record["relations"]["paired_surface_ids"] for record in records),
        "outputs": {
            "jsonl": {"path": OUTPUT.resolve().as_posix(), "bytes": OUTPUT.stat().st_size, "sha256": sha_file(OUTPUT)},
            "csv": {"path": CSV_OUTPUT.resolve().as_posix(), "bytes": CSV_OUTPUT.stat().st_size, "sha256": sha_file(CSV_OUTPUT)},
        },
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({**report, "report_sha256": sha_file(REPORT)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
