from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
TRANCHE = HERE.parents[1]
SOURCE_REL = "source/Noether_Paper29_German_P31_U02_Rationalbasis_exact_lf.tex"
FULL_REL = "source/Noether_Paper29_German_P31_Sealed_exact_slice.tex"
TARGET_REL = "ko/Noether_Paper29_Korean_U02_v001.tex"
SOURCE, FULL, TARGET = (TRANCHE / SOURCE_REL, TRANCHE / FULL_REL, TRANCHE / TARGET_REL)
INDEX = HERE / "STRUCTURAL_INDEX.jsonl"
CSV_PATH = HERE / "STRUCTURAL_INDEX.csv"
METADATA = HERE / "STRUCTURAL_INDEX_METADATA.json"
SEALED_PATH = str(Path(r"evidence://local-workspace/Codex\2026-06-01\we-are-currently-doing-a-massive\Noether_LocalCodex_20260718_P31_FullPaperCanonicalReaudit_WEB_DROP\1\01_current") / "cum_de_Local_20260718_P31.tex")
SEALED_SHA = "A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F"
SOURCE_AUTHORITY = "P31-sealed-A48CB5C/P29-U02-lines25-39-LF-normalized"
TARGET_AUTHORITY = "KO-P29-U02-v001-independent-review-final"
CONTINUATION = r"Rehash the sealed German head before U03; continue at exact full-P29 source line 41, 2. \srcspaced{Beweis des Endlichkeitskriteriums.}; line 40 is a blank separator."


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8-sig").splitlines()


def footnote_span(line: str, occurrence: int) -> tuple[int, int]:
    needle = r"\footnote{"
    start = -1
    search = 0
    for _ in range(occurrence):
        start = line.find(needle, search)
        if start < 0:
            raise ValueError(f"footnote occurrence {occurrence} not found")
        search = start + len(needle)
    opening = start + len(r"\footnote")
    depth = 0
    for index in range(opening, len(line)):
        if line[index] == "{":
            depth += 1
        elif line[index] == "}":
            depth -= 1
            if depth == 0:
                return start + 1, index + 1
    raise ValueError("unbalanced footnote")


def exact_span(line: str, needle: str) -> tuple[int, int]:
    start = line.find(needle)
    if start < 0 or line.find(needle, start + 1) >= 0:
        raise ValueError(f"expected exactly one source display substring: {needle}")
    return start + 1, start + len(needle)


def locator(line_start: int, line_end: int, printed_page: str, chars: tuple[int, int] | None = None) -> dict:
    return {
        "line_start": line_start,
        "line_end": line_end,
        "char_start": chars[0] if chars else None,
        "char_end": chars[1] if chars else None,
        "printed_page": printed_page,
        "pdf_page": 1,
    }


def fragment(path: Path, where: dict) -> str:
    content = read_lines(path)
    a, b = where["line_start"], where["line_end"]
    if not 1 <= a <= b <= len(content):
        raise ValueError(f"invalid lines {a}-{b} for {path}")
    cs, ce = where["char_start"], where["char_end"]
    if cs is None and ce is None:
        return "\n".join(content[a - 1:b])
    if a != b or cs is None or ce is None or not 1 <= cs <= ce <= len(content[a - 1]):
        raise ValueError(f"invalid characters {cs}-{ce} for {path}:{a}")
    return content[a - 1][cs - 1:ce]


def side(path: Path, relative: str, authority: str, language: str, where: dict) -> dict:
    return {
        "artifact_path": relative,
        "artifact_sha256": digest(path.read_bytes()),
        "authority_id": authority,
        "language": language,
        "locator": where,
        "fragment_sha256": digest(fragment(path, where).encode("utf-8")),
    }


def main() -> int:
    sl, tl, fl = read_lines(SOURCE), read_lines(TARGET), read_lines(FULL)
    if len(sl) != 15 or fl[24:39] != sl:
        raise SystemExit("U02 is not exact normalized full-P29 lines 25-39")
    if len(fl) < 41 or fl[39] != "" or not fl[40].startswith(r"2. \srcspaced{Beweis des Endlichkeitskriteriums.}"):
        raise SystemExit("full-P29 line-41 cursor or blank line 40 shifted")
    if len(tl) != 42 or tl[41] != r"\end{document}":
        raise SystemExit(f"target boundary shifted: expected 42 lines and end document at line 42, got {len(tl)}")

    note1s = locator(5, 5, "29", footnote_span(sl[4], 1))
    note1t = locator(16, 16, "29", footnote_span(tl[15], 1))
    note2s = locator(13, 13, "30", footnote_span(sl[12], 1))
    note2t = locator(30, 30, "30", footnote_span(tl[29], 1))
    display_needles = [
        r"$\overline{\mathfrak K}=\mathfrak K(x_{t+1},\ldots,x_n)$ bezw. $\overline{\mathfrak M}=\mathfrak M(x_{t+1},\ldots,x_n)$",
        r"$\overline P<\overline{\mathfrak K}<\overline P(x_1,\ldots,x_t)$",
        r"$\mathfrak K$ gleich $\mathfrak M=P(y_1,\ldots,y_t;z_1,\ldots,z_s)$",
    ]
    display_sources = [
        locator(11, 11, "30", exact_span(sl[10], display_needles[0])),
        locator(13, 13, "30", exact_span(sl[12], display_needles[1])),
        locator(13, 13, "30-31", exact_span(sl[12], display_needles[2])),
    ]
    display_targets = [locator(23, 27, "30"), locator(31, 33, "30"), locator(35, 37, "30-31")]

    common = {
        "schema_version": "1.0.0",
        "work_id": "noether.paper29.ko.u02",
        "completion_state": "complete",
        "review_state": "internally_source_checked",
        "publication_state": "private_working",
        "boundary_confidence": "high",
        "continuation_cursor": CONTINUATION,
        "supersedes": [],
    }
    specs = [
        ("NOE-P29-KO-U02-ROOT-001", "work", None, 0, locator(1, 15, "29-31"), locator(12, 40, "29-31"), ["NOE-P29-KO-U02-SEC-001"], [], "Complete U02 §1 Rationalbasis theorem, proof, and corollary; source/full blank separator after line 15 and target document apparatus are excluded."),
        ("NOE-P29-KO-U02-SEC-001", "subsection", "NOE-P29-KO-U02-ROOT-001", 1, locator(1, 1, "29"), locator(12, 12, "29"), ["NOE-P29-KO-U02-THM-001", "NOE-P29-KO-U02-COR-001"], ["NOE-P29-KO-U02-ROOT-001"], "Semantic §1 section heading encoded as an unnumbered LaTeX subsection within the cumulative reader hierarchy."),
        ("NOE-P29-KO-U02-THM-001", "theorem", "NOE-P29-KO-U02-SEC-001", 1, locator(3, 13, "29-31"), locator(14, 38, "29-31"), ["NOE-P29-KO-U02-FORM-001", "NOE-P29-KO-U02-FORM-002", "NOE-P29-KO-U02-PARA-001", "NOE-P29-KO-U02-PROOF-001"], ["NOE-P29-KO-U02-SEC-001"], "Complete theorem complex: both formulations, equivalence explanation, and proof through K=M."),
        ("NOE-P29-KO-U02-FORM-001", "closed_prose_unit", "NOE-P29-KO-U02-THM-001", 1, locator(3, 3, "29"), locator(14, 14, "29"), [], ["NOE-P29-KO-U02-THM-001"], "First formulation of the Rationalbasis existence theorem, including its finite rational-generation explanation."),
        ("NOE-P29-KO-U02-FORM-002", "closed_prose_unit", "NOE-P29-KO-U02-THM-001", 2, locator(5, 5, "29"), locator(16, 16, "29"), ["NOE-P29-KO-U02-NOTE-001"], ["NOE-P29-KO-U02-FORM-001"], "Second formulation in field-extension language, including the embedded Steinitz note call."),
        ("NOE-P29-KO-U02-NOTE-001", "note", "NOE-P29-KO-U02-FORM-002", 1, note1s, note1t, [], ["NOE-P29-KO-U02-FORM-002"], "Balanced first U02 source note defining Steinitz's irreducible system and transcendence degree."),
        ("NOE-P29-KO-U02-PARA-001", "paragraph", "NOE-P29-KO-U02-THM-001", 3, locator(7, 7, "30"), locator(18, 18, "30"), [], ["NOE-P29-KO-U02-FORM-001", "NOE-P29-KO-U02-FORM-002"], "Complete paragraph proving equivalence of the two theorem formulations."),
        ("NOE-P29-KO-U02-PROOF-001", "proof", "NOE-P29-KO-U02-THM-001", 4, locator(9, 13, "30-31"), locator(20, 38, "30-31"), ["NOE-P29-KO-U02-STEP-001", "NOE-P29-KO-U02-STEP-002", "NOE-P29-KO-U02-STEP-003"], ["NOE-P29-KO-U02-PARA-001"], "Complete proof of the second formulation, partitioned into equal-transcendence, t<n, and coefficient-extension reduction steps."),
        ("NOE-P29-KO-U02-STEP-001", "proof_step", "NOE-P29-KO-U02-PROOF-001", 1, locator(9, 9, "30"), locator(20, 20, "30"), [], ["NOE-P29-KO-U02-PROOF-001"], "First proof paragraph: case where K has the same transcendence degree n as the full rational-function field."),
        ("NOE-P29-KO-U02-STEP-002", "proof_step", "NOE-P29-KO-U02-PROOF-001", 2, locator(11, 11, "30"), locator(22, 28, "30"), ["NOE-P29-KO-U02-DSP-001"], ["NOE-P29-KO-U02-STEP-001"], "Second proof paragraph: t<n case, pure transcendental extensions, and paired overlined-field definitions."),
        ("NOE-P29-KO-U02-DSP-001", "display", "NOE-P29-KO-U02-STEP-002", 1, display_sources[0], display_targets[0], [], ["NOE-P29-KO-U02-STEP-002"], "First Korean display block; source presents the paired K-bar and M-bar definitions inline with bezw."),
        ("NOE-P29-KO-U02-STEP-003", "proof_step", "NOE-P29-KO-U02-PROOF-001", 3, locator(13, 13, "30-31"), locator(30, 38, "30-31"), ["NOE-P29-KO-U02-NOTE-002", "NOE-P29-KO-U02-DSP-002", "NOE-P29-KO-U02-DSP-003"], ["NOE-P29-KO-U02-STEP-002"], "Third proof paragraph: coefficient-field reduction, finite Rationalbasis, and final K=M identification."),
        ("NOE-P29-KO-U02-NOTE-002", "note", "NOE-P29-KO-U02-STEP-003", 1, note2s, note2t, [], ["NOE-P29-KO-U02-STEP-003"], "Balanced second U02 note defining the field-inclusion notation P<K; target marker is kept inline before the displays."),
        ("NOE-P29-KO-U02-DSP-002", "display", "NOE-P29-KO-U02-STEP-003", 2, display_sources[1], display_targets[1], [], ["NOE-P29-KO-U02-STEP-003"], "Second Korean display block: the overline-P < overline-K < overline-P(x) field chain."),
        ("NOE-P29-KO-U02-DSP-003", "display", "NOE-P29-KO-U02-STEP-003", 3, display_sources[2], display_targets[2], [], ["NOE-P29-KO-U02-STEP-003"], "Third Korean display block: the target equality K=M=P(y;z), expressed with gleich in source prose."),
        ("NOE-P29-KO-U02-COR-001", "corollary", "NOE-P29-KO-U02-SEC-001", 2, locator(15, 15, "31"), locator(40, 40, "31"), [], ["NOE-P29-KO-U02-THM-001", "NOE-P29-KO-U02-PROOF-001"], "Complete Folgerung/corollary closing U02 immediately before the blank separator and full-source line-41 cursor."),
    ]

    records = []
    for sid, kind, parent, order, sw, tw, xrefs, deps, note in specs:
        records.append({
            **common,
            "structural_id": sid,
            "unit_type": kind,
            "parent_id": parent,
            "order_index": order,
            "source": side(SOURCE, SOURCE_REL, SOURCE_AUTHORITY, "de", sw),
            "target": side(TARGET, TARGET_REL, TARGET_AUTHORITY, "ko-KR", tw),
            "relations": {"cross_references": xrefs, "dependencies": deps},
            "boundary_note": note,
        })

    with INDEX.open("w", encoding="utf-8", newline="\n") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")

    fields = ["structural_id", "unit_type", "parent_id", "order_index", "source_path", "source_line_start", "source_line_end", "source_char_start", "source_char_end", "source_printed_page", "source_fragment_sha256", "target_path", "target_line_start", "target_line_end", "target_char_start", "target_char_end", "target_printed_page", "target_fragment_sha256", "cross_references", "dependencies", "completion_state", "review_state", "publication_state", "boundary_confidence", "continuation_cursor"]
    with CSV_PATH.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for r in records:
            s, t = r["source"], r["target"]
            writer.writerow({
                "structural_id": r["structural_id"], "unit_type": r["unit_type"], "parent_id": r["parent_id"] or "", "order_index": r["order_index"],
                "source_path": s["artifact_path"], "source_line_start": s["locator"]["line_start"], "source_line_end": s["locator"]["line_end"], "source_char_start": s["locator"]["char_start"] or "", "source_char_end": s["locator"]["char_end"] or "", "source_printed_page": s["locator"]["printed_page"], "source_fragment_sha256": s["fragment_sha256"],
                "target_path": t["artifact_path"], "target_line_start": t["locator"]["line_start"], "target_line_end": t["locator"]["line_end"], "target_char_start": t["locator"]["char_start"] or "", "target_char_end": t["locator"]["char_end"] or "", "target_printed_page": t["locator"]["printed_page"], "target_fragment_sha256": t["fragment_sha256"],
                "cross_references": ";".join(r["relations"]["cross_references"]), "dependencies": ";".join(r["relations"]["dependencies"]), "completion_state": r["completion_state"], "review_state": r["review_state"], "publication_state": r["publication_state"], "boundary_confidence": r["boundary_confidence"], "continuation_cursor": r["continuation_cursor"],
            })

    counts = Counter(r["unit_type"] for r in records)
    metadata = {
        "schema_version": "1.0.0", "index_id": "NOE-P29-KO-U02-STRUCTURAL-INDEX-001", "work_id": "noether.paper29.ko.u02",
        "authority": {"sealed_cumulative_path": SEALED_PATH, "sealed_cumulative_sha256": SEALED_SHA, "full_p29_slice_path": FULL_REL, "full_p29_slice_sha256": digest(FULL.read_bytes()), "u02_source_path": SOURCE_REL, "u02_source_sha256": digest(SOURCE.read_bytes()), "target_tex_path": TARGET_REL, "target_tex_sha256": digest(TARGET.read_bytes()), "source_cursor": "normalized full-P29 lines 25-39; printed pp. 29-31", "target_cursor": "Korean TeX substantive lines 12-40; compiled PDF p. 1"},
        "expected_record_count": len(records), "expected_type_counts": dict(counts), "expected_structural_ids": [r["structural_id"] for r in records],
        "absent_after_complete_unit_inspection": ["section", "proposition", "lemma", "definition", "remark", "example", "equation", "diagram", "table", "bibliography_item", "apparatus", "other"],
        "coverage_note": "The three target display blocks are all indexed. Inline source mathematics remains attached to exact character spans for those displays; other inline formulae remain in their proof/formulation parents.",
        "continuation_cursor": CONTINUATION,
    }
    METADATA.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"records={len(records)} types={dict(counts)} target_sha256={digest(TARGET.read_bytes())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
