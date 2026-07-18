from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
TRANCHE = HERE.parents[1]
SOURCE_REL = "source/Noether_Paper29_German_P31_U01_Introduction_exact_lf.tex"
FULL_SOURCE_REL = "source/Noether_Paper29_German_P31_Sealed_exact_slice.tex"
TARGET_REL = "ko/Noether_Paper29_Korean_U01_v001.tex"
SOURCE = TRANCHE / SOURCE_REL
FULL_SOURCE = TRANCHE / FULL_SOURCE_REL
TARGET = TRANCHE / TARGET_REL
INDEX = HERE / "STRUCTURAL_INDEX.jsonl"
CSV_PROJECTION = HERE / "STRUCTURAL_INDEX.csv"
METADATA = HERE / "STRUCTURAL_INDEX_METADATA.json"

SEALED_AUTHORITY_PATH = str(
    Path(
        r"evidence://local-workspace/Codex\2026-06-01\we-are-currently-doing-a-massive"
        r"\Noether_LocalCodex_20260718_P31_FullPaperCanonicalReaudit_WEB_DROP\1\01_current"
    )
    / "cum_de_Local_20260718_P31.tex"
)
SEALED_AUTHORITY_SHA256 = "A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F"
SOURCE_AUTHORITY_ID = "P31-sealed-A48CB5C/P29-U01-LF-normalized-prefix"
TARGET_AUTHORITY_ID = "KO-P29-U01-v001"
CONTINUATION = (
    "Rehash the sealed German head before U02; continue at exact full-P29 source line 25, "
    r"\subsection*{§ 1. Das Endlichkeitskriterium}."
)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8-sig").splitlines()


def footnote_span(line: str, occurrence: int) -> tuple[int, int]:
    """Return one-based inclusive coordinates for a balanced \footnote{...} command."""
    needle = r"\footnote{"
    search_from = 0
    start = -1
    for _ in range(occurrence):
        start = line.find(needle, search_from)
        if start < 0:
            raise ValueError(f"footnote occurrence {occurrence} not found")
        search_from = start + len(needle)
    opening = start + len(r"\footnote")
    depth = 0
    for offset in range(opening, len(line)):
        character = line[offset]
        if character == "{":
            depth += 1
        elif character == "}":
            depth -= 1
            if depth == 0:
                return start + 1, offset + 1
    raise ValueError(f"unbalanced footnote occurrence {occurrence}")


def extract_fragment(path: Path, locator: dict) -> str:
    content = lines(path)
    line_start = locator["line_start"]
    line_end = locator["line_end"]
    if not 1 <= line_start <= line_end <= len(content):
        raise ValueError(f"invalid line range {line_start}-{line_end} for {path}")
    char_start = locator["char_start"]
    char_end = locator["char_end"]
    if char_start is None and char_end is None:
        return "\n".join(content[line_start - 1:line_end])
    if line_start != line_end or char_start is None or char_end is None:
        raise ValueError("character ranges require one line and two non-null endpoints")
    selected = content[line_start - 1]
    if not 1 <= char_start <= char_end <= len(selected):
        raise ValueError(f"invalid character range {char_start}-{char_end} for {path}:{line_start}")
    return selected[char_start - 1:char_end]


def locator(
    line_start: int,
    line_end: int,
    printed_page: str,
    *,
    footnote_occurrence: int | None = None,
    content: list[str] | None = None,
) -> dict:
    char_start = None
    char_end = None
    if footnote_occurrence is not None:
        if content is None or line_start != line_end:
            raise ValueError("footnote locator needs one source line")
        char_start, char_end = footnote_span(content[line_start - 1], footnote_occurrence)
    return {
        "line_start": line_start,
        "line_end": line_end,
        "char_start": char_start,
        "char_end": char_end,
        "printed_page": printed_page,
        "pdf_page": 1,
    }


def side(path: Path, relative: str, authority_id: str, language: str, where: dict) -> dict:
    return {
        "artifact_path": relative,
        "artifact_sha256": digest(path.read_bytes()),
        "authority_id": authority_id,
        "language": language,
        "locator": where,
        "fragment_sha256": digest(extract_fragment(path, where).encode("utf-8")),
    }


def main() -> int:
    source_lines = lines(SOURCE)
    target_lines = lines(TARGET)
    full_lines = lines(FULL_SOURCE)
    if len(source_lines) != 24:
        raise SystemExit(f"expected 24 U01 source lines, found {len(source_lines)}")
    if full_lines[:24] != source_lines:
        raise SystemExit("U01 source is not the exact LF-normalized first 24 lines of the full P29 slice")
    if len(full_lines) < 25 or not full_lines[24].startswith(r"\subsection*{§ 1. Das Endlichkeitskriterium}"):
        raise SystemExit("full-P29 continuation line 25 does not match the frozen U01 cursor")
    if len(target_lines) < 36 or target_lines[35] != r"\end{document}":
        raise SystemExit("target document boundary shifted: expected end document at line 36")

    source_note_locators = {
        1: locator(15, 15, "28", footnote_occurrence=1, content=source_lines),
        2: locator(15, 15, "28", footnote_occurrence=2, content=source_lines),
        3: locator(17, 17, "28", footnote_occurrence=1, content=source_lines),
        4: locator(23, 23, "29", footnote_occurrence=1, content=source_lines),
    }
    target_note_locators = {
        1: locator(26, 26, "28", footnote_occurrence=1, content=target_lines),
        2: locator(26, 26, "28", footnote_occurrence=2, content=target_lines),
        3: locator(28, 28, "28", footnote_occurrence=1, content=target_lines),
        4: locator(34, 34, "29", footnote_occurrence=1, content=target_lines),
    }

    common = {
        "schema_version": "1.0.0",
        "work_id": "noether.paper29.ko.u01",
        "completion_state": "complete",
        "review_state": "internally_source_checked",
        "publication_state": "private_working",
        "boundary_confidence": "high",
        "continuation_cursor": CONTINUATION,
        "supersedes": [],
    }

    specs = [
        {
            "structural_id": "NOE-P29-KO-U01-ROOT-001",
            "unit_type": "work",
            "parent_id": None,
            "order_index": 0,
            "source_locator": locator(1, 23, "28-29"),
            "target_locator": locator(12, 34, "28-29"),
            "cross_references": ["NOE-P29-KO-U01-SEC-001"],
            "dependencies": [],
            "boundary_note": "Complete substantive U01 front matter and introduction. The trailing blank source line 24 and standalone target preamble/document terminator are build apparatus outside the work-text boundary.",
        },
        {
            "structural_id": "NOE-P29-KO-U01-SEC-001",
            "unit_type": "section",
            "parent_id": "NOE-P29-KO-U01-ROOT-001",
            "order_index": 1,
            "source_locator": locator(1, 1, "28"),
            "target_locator": locator(12, 12, "28"),
            "cross_references": [
                "NOE-P29-KO-U01-CIT-001",
                "NOE-P29-KO-U01-AUTH-001",
                "NOE-P29-KO-U01-PARA-001",
                "NOE-P29-KO-U01-THM-001",
                "NOE-P29-KO-U01-PARA-002",
                "NOE-P29-KO-U01-PARA-003",
                "NOE-P29-KO-U01-PARA-004",
            ],
            "dependencies": ["NOE-P29-KO-U01-ROOT-001"],
            "boundary_note": "Explicit unnumbered LaTeX section heading representing the complete Paper 29 title.",
        },
        {
            "structural_id": "NOE-P29-KO-U01-CIT-001",
            "unit_type": "bibliography_item",
            "parent_id": "NOE-P29-KO-U01-SEC-001",
            "order_index": 1,
            "source_locator": locator(4, 4, "publication citation: article pp. 28-35"),
            "target_locator": locator(15, 15, "publication citation: article pp. 28-35"),
            "cross_references": [],
            "dependencies": ["NOE-P29-KO-U01-SEC-001"],
            "boundary_note": "Centered journal citation retained verbatim as publication apparatus; it names the full article page range rather than a single scanned page.",
        },
        {
            "structural_id": "NOE-P29-KO-U01-AUTH-001",
            "unit_type": "apparatus",
            "parent_id": "NOE-P29-KO-U01-SEC-001",
            "order_index": 2,
            "source_locator": locator(9, 13, "28"),
            "target_locator": locator(20, 24, "28"),
            "cross_references": [],
            "dependencies": ["NOE-P29-KO-U01-SEC-001"],
            "boundary_note": "Closed centered author, affiliation, presenter, and meeting-date apparatus including its LaTeX environment boundaries.",
        },
        {
            "structural_id": "NOE-P29-KO-U01-PARA-001",
            "unit_type": "paragraph",
            "parent_id": "NOE-P29-KO-U01-SEC-001",
            "order_index": 3,
            "source_locator": locator(15, 15, "28"),
            "target_locator": locator(26, 26, "28"),
            "cross_references": [
                "NOE-P29-KO-U01-NOTE-001",
                "NOE-P29-KO-U01-NOTE-002",
                "NOE-P29-KO-U01-THM-001",
            ],
            "dependencies": ["NOE-P29-KO-U01-SEC-001"],
            "boundary_note": "First complete introductory paragraph, including two embedded footnote calls, ending in the syntactic lead-in to the criterion.",
        },
        {
            "structural_id": "NOE-P29-KO-U01-NOTE-001",
            "unit_type": "note",
            "parent_id": "NOE-P29-KO-U01-PARA-001",
            "order_index": 1,
            "source_locator": source_note_locators[1],
            "target_locator": target_note_locators[1],
            "cross_references": [],
            "dependencies": ["NOE-P29-KO-U01-PARA-001"],
            "boundary_note": "Balanced first footnote command on the introduction line, citing Noether's 1916 elementary finiteness proof.",
        },
        {
            "structural_id": "NOE-P29-KO-U01-NOTE-002",
            "unit_type": "note",
            "parent_id": "NOE-P29-KO-U01-PARA-001",
            "order_index": 2,
            "source_locator": source_note_locators[2],
            "target_locator": target_note_locators[2],
            "cross_references": [],
            "dependencies": ["NOE-P29-KO-U01-PARA-001"],
            "boundary_note": "Balanced second footnote command on the introduction line, citing Steinitz for field-theory terminology.",
        },
        {
            "structural_id": "NOE-P29-KO-U01-THM-001",
            "unit_type": "theorem",
            "parent_id": "NOE-P29-KO-U01-SEC-001",
            "order_index": 4,
            "source_locator": locator(17, 17, "28"),
            "target_locator": locator(28, 28, "28"),
            "cross_references": ["NOE-P29-KO-U01-NOTE-003"],
            "dependencies": ["NOE-P29-KO-U01-SEC-001", "NOE-P29-KO-U01-PARA-001"],
            "boundary_note": "Complete named Endlichkeitskriterium statement. It is prose-formatted rather than a LaTeX theorem environment but functions as the introduction's criterion theorem.",
        },
        {
            "structural_id": "NOE-P29-KO-U01-NOTE-003",
            "unit_type": "note",
            "parent_id": "NOE-P29-KO-U01-THM-001",
            "order_index": 1,
            "source_locator": source_note_locators[3],
            "target_locator": target_note_locators[3],
            "cross_references": [],
            "dependencies": ["NOE-P29-KO-U01-THM-001"],
            "boundary_note": "Balanced criterion footnote command preserving Noether's correction from Modulbasis relative to R to a basis relative to a subring of R.",
        },
        {
            "structural_id": "NOE-P29-KO-U01-PARA-002",
            "unit_type": "paragraph",
            "parent_id": "NOE-P29-KO-U01-SEC-001",
            "order_index": 5,
            "source_locator": locator(19, 19, "28-29"),
            "target_locator": locator(30, 30, "28-29"),
            "cross_references": [],
            "dependencies": ["NOE-P29-KO-U01-THM-001"],
            "boundary_note": "Second complete introductory paragraph; the original printed paragraph begins on p. 28 and continues on p. 29.",
        },
        {
            "structural_id": "NOE-P29-KO-U01-PARA-003",
            "unit_type": "paragraph",
            "parent_id": "NOE-P29-KO-U01-SEC-001",
            "order_index": 6,
            "source_locator": locator(21, 21, "29"),
            "target_locator": locator(32, 32, "29"),
            "cross_references": [],
            "dependencies": ["NOE-P29-KO-U01-THM-001"],
            "boundary_note": "Third complete introductory paragraph on symmetric functions, the Galois resolvent, and relative/modular invariants.",
        },
        {
            "structural_id": "NOE-P29-KO-U01-PARA-004",
            "unit_type": "paragraph",
            "parent_id": "NOE-P29-KO-U01-SEC-001",
            "order_index": 7,
            "source_locator": locator(23, 23, "29"),
            "target_locator": locator(34, 34, "29"),
            "cross_references": ["NOE-P29-KO-U01-NOTE-004"],
            "dependencies": ["NOE-P29-KO-U01-PARA-003"],
            "boundary_note": "Fourth and final complete introductory paragraph, ending immediately before the section-one boundary.",
        },
        {
            "structural_id": "NOE-P29-KO-U01-NOTE-004",
            "unit_type": "note",
            "parent_id": "NOE-P29-KO-U01-PARA-004",
            "order_index": 1,
            "source_locator": source_note_locators[4],
            "target_locator": target_note_locators[4],
            "cross_references": [],
            "dependencies": ["NOE-P29-KO-U01-PARA-004"],
            "boundary_note": "Balanced Dickson bibliography footnote command, including the Madison Colloquium and later Transactions literature pointer.",
        },
    ]

    records = []
    for spec in specs:
        record = dict(common)
        record.update(
            structural_id=spec["structural_id"],
            unit_type=spec["unit_type"],
            parent_id=spec["parent_id"],
            order_index=spec["order_index"],
            source=side(SOURCE, SOURCE_REL, SOURCE_AUTHORITY_ID, "de", spec["source_locator"]),
            target=side(TARGET, TARGET_REL, TARGET_AUTHORITY_ID, "ko-KR", spec["target_locator"]),
            relations={
                "cross_references": spec["cross_references"],
                "dependencies": spec["dependencies"],
            },
            boundary_note=spec["boundary_note"],
        )
        records.append(record)

    with INDEX.open("w", encoding="utf-8", newline="\n") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")

    csv_fields = [
        "structural_id",
        "unit_type",
        "parent_id",
        "order_index",
        "source_path",
        "source_line_start",
        "source_line_end",
        "source_char_start",
        "source_char_end",
        "source_printed_page",
        "source_fragment_sha256",
        "target_path",
        "target_line_start",
        "target_line_end",
        "target_char_start",
        "target_char_end",
        "target_printed_page",
        "target_fragment_sha256",
        "cross_references",
        "dependencies",
        "completion_state",
        "review_state",
        "publication_state",
        "boundary_confidence",
        "continuation_cursor",
    ]
    with CSV_PROJECTION.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=csv_fields, lineterminator="\n")
        writer.writeheader()
        for record in records:
            source = record["source"]
            target = record["target"]
            writer.writerow(
                {
                    "structural_id": record["structural_id"],
                    "unit_type": record["unit_type"],
                    "parent_id": record["parent_id"] or "",
                    "order_index": record["order_index"],
                    "source_path": source["artifact_path"],
                    "source_line_start": source["locator"]["line_start"],
                    "source_line_end": source["locator"]["line_end"],
                    "source_char_start": source["locator"]["char_start"] or "",
                    "source_char_end": source["locator"]["char_end"] or "",
                    "source_printed_page": source["locator"]["printed_page"] or "",
                    "source_fragment_sha256": source["fragment_sha256"],
                    "target_path": target["artifact_path"],
                    "target_line_start": target["locator"]["line_start"],
                    "target_line_end": target["locator"]["line_end"],
                    "target_char_start": target["locator"]["char_start"] or "",
                    "target_char_end": target["locator"]["char_end"] or "",
                    "target_printed_page": target["locator"]["printed_page"] or "",
                    "target_fragment_sha256": target["fragment_sha256"],
                    "cross_references": ";".join(record["relations"]["cross_references"]),
                    "dependencies": ";".join(record["relations"]["dependencies"]),
                    "completion_state": record["completion_state"],
                    "review_state": record["review_state"],
                    "publication_state": record["publication_state"],
                    "boundary_confidence": record["boundary_confidence"],
                    "continuation_cursor": record["continuation_cursor"],
                }
            )

    counts = Counter(record["unit_type"] for record in records)
    metadata = {
        "schema_version": "1.0.0",
        "index_id": "NOE-P29-KO-U01-STRUCTURAL-INDEX-001",
        "work_id": "noether.paper29.ko.u01",
        "authority": {
            "sealed_cumulative_path": SEALED_AUTHORITY_PATH,
            "sealed_cumulative_sha256": SEALED_AUTHORITY_SHA256,
            "full_p29_slice_path": FULL_SOURCE_REL,
            "full_p29_slice_sha256": digest(FULL_SOURCE.read_bytes()),
            "u01_source_path": SOURCE_REL,
            "u01_source_sha256": digest(SOURCE.read_bytes()),
            "target_tex_path": TARGET_REL,
            "target_tex_sha256": digest(TARGET.read_bytes()),
            "source_cursor": "exact full-P29 slice lines 1-24; substantive structural root lines 1-23; printed pp. 28-29",
            "target_cursor": "Korean TeX substantive lines 12-34; compiled PDF p. 1",
        },
        "expected_record_count": len(records),
        "expected_type_counts": dict(counts),
        "expected_structural_ids": [record["structural_id"] for record in records],
        "absent_after_complete_unit_inspection": [
            "subsection",
            "closed_prose_unit",
            "proposition",
            "lemma",
            "corollary",
            "definition",
            "remark",
            "example",
            "proof",
            "proof_step",
            "equation",
            "display",
            "diagram",
            "table",
            "other",
        ],
        "coverage_note": "U01 contains four prose paragraphs, one named criterion theorem, four footnotes, title, citation, and author/presenter apparatus. It contains no display equation; inline p, S, and R notation remains indexed inside its parent prose or theorem.",
        "continuation_cursor": CONTINUATION,
    }
    METADATA.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"records={len(records)} types={dict(counts)} target_sha256={digest(TARGET.read_bytes())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
