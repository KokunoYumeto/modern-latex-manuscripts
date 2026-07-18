#!/usr/bin/env python3
"""Build and validate bounded Paper 37 mapping and localization-status artifacts."""

from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source" / "Noether_Paper37_German_P31_logical_article_LF.tex"
SOURCE_EXACT = ROOT / "source" / "Noether_Paper37_German_P31_logical_article_exact_CRLF.tex"
SOURCE_INTERVAL = ROOT / "source" / "Noether_Paper37_German_P31_section_interval_exact_CRLF.tex"
TARGET = ROOT / "zh-Hans-CN" / "Noether_Paper37_Chinese_P31Reconciled_zh-Hans-CN_v001.tex"
TARGET_PDF = TARGET.with_suffix(".pdf")
PARITY = ROOT / "qa" / "P37_SOURCE_PARITY.json"

AUTHORITY = Path(
    r"evidence://local-workspace/Codex\2026-06-01\we-are-currently-doing-a-massive\Noether_LocalCodex_20260718_P31_FullPaperCanonicalReaudit_WEB_DROP\1\01_current\cum_de_Local_20260718_P31.tex"
)
AUTHORITY_SHA256 = "A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F"
SOURCE_INTERVAL_SHA256 = "AF2993A83530352893CABA50D196BDE9A17965C0E531297CA1A9E5AEB2D1B00A"
SOURCE_EXACT_SHA256 = "AF3B34ACF4FF8D91850AC56C4F86447ABC61E6641FF9795BEFBFDA004788585D"
SOURCE_LF_SHA256 = "68C72173E0C060BC68CB3651AF078ACE82B4D5806C8A41584632AA2BB4A9B27B"
P31_START_LINE = 18613
P31_LOGICAL_END_LINE = 18799
P31_NEXT_SECTION_LINE = 18805

SOURCE_MAP = ROOT / "SOURCE_UNIT_MAP.csv"
STRUCTURAL_CSV = ROOT / "STRUCTURAL_INDEX.csv"
STRUCTURAL_JSON = ROOT / "STRUCTURAL_INDEX.json"
CURSOR_JSON = ROOT / "qa" / "source_version_cursor.json"
LOCALIZATION_CSV = ROOT / "LOCALIZATION_STATUS.csv"


def unit(
    suffix: str,
    order: str,
    unit_type: str,
    source_start: int,
    source_end: int,
    target_start: int,
    target_end: int,
    title: str,
    parent: str = "U000",
    dependencies: tuple[str, ...] = (),
    review: str = "mapped_and_automated_parity_checked",
    ambiguity: str = "",
) -> dict[str, Any]:
    return {
        "suffix": suffix,
        "order": order,
        "unit_type": unit_type,
        "source_start": source_start,
        "source_end": source_end,
        "target_start": target_start,
        "target_end": target_end,
        "title": title,
        "parent": parent,
        "dependencies": dependencies,
        "review": review,
        "ambiguity": ambiguity,
    }


UNITS = [
    unit("U000", "0", "article", 1, 187, 29, 214, "Paper 37 complete logical article", parent=""),
    unit("U001", "1", "metadata", 1, 5, 29, 33, "title and journal citation", dependencies=()),
    unit("U002", "2", "author", 7, 9, 35, 37, "author and Göttingen byline", dependencies=("U001",)),
    unit("U003", "3", "opening", 11, 19, 39, 48, "opening argument and announced normal-basis result", dependencies=("U002",)),
    unit("N001", "3.1", "footnote", 11, 11, 39, 39, "Speiser necessary-condition citation", parent="U003", review="footnote_locus_and_text_checked"),
    unit("N002", "3.2", "footnote", 15, 15, 43, 43, "Artin conductor citation", parent="U003", review="footnote_locus_and_text_checked"),
    unit("N003", "3.3", "footnote", 15, 15, 43, 44, "dated Deuring nonmaximal-order example", parent="U003", review="footnote_locus_and_text_checked", ambiguity="target footnote occupies two physical lines; four source multiplication products restored"),
    unit("N004", "3.4", "footnote", 17, 17, 46, 46, "Hasse maximal-order citation and localization qualification", parent="U003", review="footnote_locus_and_text_checked"),
    unit("S001", "10", "subsection", 21, 43, 50, 72, "§1 p-adically extended integral group ring", dependencies=("U003",)),
    unit("U010", "10.1", "subsection_opening", 23, 25, 52, 54, "§1 notation and semisimplicity setup", parent="S001"),
    unit("U011", "11", "theorem", 27, 38, 56, 67, "Theorem 1 maximality criterion", parent="S001", dependencies=("U010",)),
    unit("N005", "11.1", "footnote", 30, 30, 59, 59, "Noether 1929 group-ring discriminant citation", parent="U011", review="footnote_locus_and_text_checked"),
    unit("E001", "11.2", "display", 33, 37, 62, 66, "trivial-representation order extension and unindexed group sum", parent="U011", review="display_semantic_signature_checked", ambiguity="source unindexed sum retained exactly"),
    unit("U012", "12", "theorem", 40, 43, 69, 72, "Theorem 2 principal ideals in the maximal order", parent="S001", dependencies=("U011",)),
    unit("N006", "12.1", "footnote", 43, 43, 72, 72, "Hasse principal-ideal extension to semisimple systems", parent="U012", review="footnote_locus_and_text_checked"),
    unit("S002", "20", "subsection", 45, 95, 74, 124, "§2 Galois modules operator isomorphism and normal bases", dependencies=("S001",)),
    unit("U020", "20.1", "subsection_opening", 47, 51, 76, 80, "§2 Galois action as group-algebra module", parent="S002"),
    unit("E002", "20.2", "display", 48, 51, 77, 80, "group-algebra action formula", parent="U020", review="display_semantic_signature_checked"),
    unit("U021", "21", "definition", 53, 54, 82, 83, "definition of rational and integral Galois modules", parent="S002", dependencies=("U020",)),
    unit("U022", "22", "theorem", 56, 67, 85, 96, "Theorem 3 rational operator isomorphism", parent="S002", dependencies=("U021",)),
    unit("N007", "22.1", "footnote", 59, 59, 88, 88, "normal-basis specialization argument", parent="U022", review="footnote_locus_and_text_checked"),
    unit("E003", "22.2", "display", 60, 66, 89, 95, "operator-isomorphism correspondence", parent="U022", review="display_semantic_signature_checked"),
    unit("U023", "23", "theorem", 69, 72, 98, 101, "Theorem 4 integral Galois modules of rank n", parent="S002", dependencies=("U022",)),
    unit("U024", "24", "theorem", 74, 79, 103, 108, "Theorem 5 local normal-basis criterion", parent="S002", dependencies=("U023",)),
    unit("N008", "24.1", "footnote", 75, 75, 104, 104, "Abelian quotient-ring qualification", parent="U024", review="footnote_locus_and_text_checked"),
    unit("U025", "25", "supplement", 81, 95, 110, 124, "supplement to Theorem 3 and representation consequence", parent="S002", dependencies=("U022",)),
    unit("N009", "25.1", "footnote", 82, 82, 111, 111, "Deuring finite-field proof observation", parent="U025", review="footnote_locus_and_text_checked"),
    unit("N010", "25.2", "footnote", 82, 82, 111, 111, "Speiser Galois-module attribution", parent="U025", review="footnote_locus_and_text_checked"),
    unit("E004", "25.3", "display", 91, 94, 120, 123, "representation matrix on Galois-module basis", parent="U025", review="display_semantic_signature_checked", ambiguity="source terminal index t retained; inherited l drift rejected"),
    unit("S003", "30", "subsection", 97, 185, 126, 214, "§3 discriminant as group determinant", dependencies=("S002",)),
    unit("U030", "30.1", "subsection_opening", 99, 99, 128, 128, "§3 reduction to ramified places with normal bases", parent="S003"),
    unit("U031", "31", "theorem", 101, 156, 130, 185, "Theorem 6 discriminant factorization by characters", parent="S003", dependencies=("U030",)),
    unit("E005", "31.1", "display", 105, 107, 134, 136, "group determinant from a normal basis", parent="U031", review="display_semantic_signature_checked"),
    unit("E006", "31.2", "display", 111, 115, 140, 144, "determinant and group-matrix decomposition", parent="U031", review="display_semantic_signature_checked"),
    unit("E007", "31.3", "display", 117, 122, 146, 151, "lambda matrix transformation", parent="U031", review="display_semantic_signature_checked"),
    unit("E008", "31.4", "display", 124, 126, 153, 155, "lambda determinant transformation", parent="U031", review="display_semantic_signature_checked"),
    unit("E009", "31.5", "display", 132, 136, 161, 165, "adjoint determinant pair", parent="U031", review="display_semantic_signature_checked"),
    unit("E010", "31.6", "display", 140, 143, 169, 172, "Delta-lambda invariance", parent="U031", review="display_semantic_signature_checked"),
    unit("N011", "31.7", "footnote", 144, 148, 173, 177, "coefficient-extension direct-sum argument", parent="U031", review="footnote_locus_and_text_checked", ambiguity="roman P is source-exact coefficient field; fraktur-P drift rejected"),
    unit("E011", "31.7.1", "display", 145, 147, 174, 176, "coefficient direct-sum decomposition inside footnote 11", parent="N011", review="display_semantic_signature_checked"),
    unit("E012", "31.8", "display", 151, 153, 180, 182, "discriminant-factor decomposition", parent="U031", review="display_semantic_signature_checked"),
    unit("X001", "31.9", "cross_reference", 154, 154, 183, 183, "source cross-reference [vgl. 2a)] restored as 参见 2a", parent="U031", review="cross_reference_restoration_checked"),
    unit("U032", "32", "theorem", 158, 181, 187, 210, "Theorem 7 cyclic prime-degree conductor identification", parent="S003", dependencies=("U031",)),
    unit("N012", "32.1", "footnote", 161, 161, 190, 190, "Hilbert Zahlbericht citation and localization qualification", parent="U032", review="footnote_locus_and_text_checked"),
    unit("E013", "32.2", "display", 162, 166, 191, 195, "ramified-prime factorization", parent="U032", review="display_semantic_signature_checked", ambiguity="generic prime notation in following prose is unindexed; display family remains indexed"),
    unit("E014", "32.3", "display", 168, 173, 197, 202, "root-number ideal factorizations", parent="U032", review="display_semantic_signature_checked"),
    unit("E015", "32.4", "display", 175, 180, 204, 209, "Delta-lambda ideal chain and conductor", parent="U032", review="display_semantic_signature_checked"),
    unit("U099", "99", "receipt", 183, 185, 212, 214, "received 24 August 1931", dependencies=("U032",)),
]


SOURCE_MAP_FIELDS = [
    "unit_id", "order", "unit_type", "source_locator", "target_locator",
    "title_or_function", "dependencies", "source_status", "target_status",
    "review_state", "confidence", "ambiguity",
]
STRUCTURAL_FIELDS = [
    "structural_id", "parent_id", "order", "unit_type", "source_locator",
    "target_locator", "title", "dependencies", "completion_state", "review_state",
    "publication_state", "boundary_confidence", "ambiguity",
]
LOCALIZATION_FIELDS = [
    "record_id", "language_tag", "script", "artifact", "status", "evidence_scope",
    "prohibited_claim", "next_gate", "mandarin_simplified_dominance_debt_qualitative",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def file_record(path: Path, relative: bool = True) -> dict[str, Any]:
    data = path.read_bytes()
    return {
        "path": path.relative_to(ROOT).as_posix() if relative else path.as_posix(),
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest().upper(),
        "crlf_delimiters": data.count(b"\r\n"),
        "lf_delimiters": data.count(b"\n"),
    }


def source_locator(start: int, end: int) -> str:
    p31_start = P31_START_LINE + start - 1
    p31_end = P31_START_LINE + end - 1
    local = f"source line {start}" if start == end else f"source lines {start}-{end}"
    cumulative = f"P31 line {p31_start}" if p31_start == p31_end else f"P31 lines {p31_start}-{p31_end}"
    return f"{cumulative}; {local}"


def target_locator(start: int, end: int) -> str:
    return f"Hans line {start}" if start == end else f"Hans lines {start}-{end}"


def sid(suffix: str) -> str:
    return f"NOE-P37-{suffix}"


def zid(suffix: str) -> str:
    return f"NOE-P37-ZH-{suffix}"


def write_csv(path: Path, fields: list[str], rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, dialect="excel", extrasaction="raise")
        writer.writeheader()
        writer.writerows(rows)


def source_rows() -> list[dict[str, str]]:
    rows = []
    for item in UNITS:
        rows.append({
            "unit_id": sid(item["suffix"]),
            "order": item["order"],
            "unit_type": item["unit_type"],
            "source_locator": source_locator(item["source_start"], item["source_end"]),
            "target_locator": target_locator(item["target_start"], item["target_end"]),
            "title_or_function": item["title"],
            "dependencies": ";".join(sid(value) for value in item["dependencies"]),
            "source_status": "sealed_p31_exact",
            "target_status": "complete",
            "review_state": item["review"],
            "confidence": "high",
            "ambiguity": item["ambiguity"],
        })
    return rows


def structural_rows() -> list[dict[str, str]]:
    rows = []
    for item in UNITS:
        rows.append({
            "structural_id": zid(item["suffix"]),
            "parent_id": zid(item["parent"]) if item["parent"] else "",
            "order": item["order"],
            "unit_type": item["unit_type"],
            "source_locator": source_locator(item["source_start"], item["source_end"]),
            "target_locator": target_locator(item["target_start"], item["target_end"]),
            "title": item["title"],
            "dependencies": ";".join(zid(value) for value in item["dependencies"]),
            "completion_state": "complete",
            "review_state": item["review"],
            "publication_state": "handoff_ready",
            "boundary_confidence": "high",
            "ambiguity": item["ambiguity"],
        })
    return rows


def localization_rows() -> list[dict[str, str]]:
    return [
        {
            "record_id": "ZH-P37-L001", "language_tag": "zh-Hans-CN", "script": "Hans",
            "artifact": "zh-Hans-CN/Noether_Paper37_Chinese_P31Reconciled_zh-Hans-CN_v001.tex",
            "status": "prc_oriented_internal_source_checked_build_render_frozen",
            "evidence_scope": "sealed P31 source; PRC-oriented Simplified Chinese internal production; automated source parity and structural mapping; no external validation",
            "prohibited_claim": "external or community certification; Singapore Taiwan Hong Kong or Macao localization or acceptance",
            "next_gate": "independent PRC Chinese algebra review and human-comprehension review",
            "mandarin_simplified_dominance_debt_qualitative": "present: PRC-oriented Mandarin Simplified Chinese dominates the current target and much of the available evidence shelf; this cannot authorize any other locale",
        },
        {
            "record_id": "ZH-P37-L002", "language_tag": "zh-Hans-SG", "script": "Hans", "artifact": "",
            "status": "held_unvalidated_no_separate_localization",
            "evidence_scope": "script compatibility only; no Singapore-specific mathematical-prose evidence or reviewer return",
            "prohibited_claim": "Singapore localization or acceptance",
            "next_gate": "Singapore-specific mathematical terminology and prose evidence plus reviewer return",
            "mandarin_simplified_dominance_debt_qualitative": "unresolved: PRC-Hans lexical and prose attractors may mask Singapore usage; PRC evidence is not transferable validation",
        },
        {
            "record_id": "ZH-P37-L003", "language_tag": "zh-Hant", "script": "Hant",
            "artifact": "zh-Hant-controlled/Noether_Paper37_Chinese_P31Reconciled_zh-Hant-controlled_v001.tex",
            "status": "controlled_generic_hant_internal_build_render_validated_nonlocalized",
            "evidence_scope": "controlled generic Traditional-script artifact generated from the pinned Hans TeX; converter custody, TeX/math integrity, two-pass build, and four-page internal render review pass; no locale prose validation",
            "prohibited_claim": "Taiwan Hong Kong or Macao localization; generic script conversion as localized prose",
            "next_gate": "seek separate Taiwan Hong Kong or Macao terminology/prose evidence and human review only after explicit locale routing",
            "mandarin_simplified_dominance_debt_qualitative": "present: this generic Hant artifact inherits the audited Hans-Mandarin lexical and prose base; script integrity does not establish regional naturalness or acceptance",
        },
        {
            "record_id": "ZH-P37-L004", "language_tag": "zh-Hant-TW", "script": "Hant", "artifact": "",
            "status": "held_unvalidated_no_localization",
            "evidence_scope": "no Taiwan-specific terminology adaptation prose evidence or reviewer return",
            "prohibited_claim": "Taiwan localization or acceptance",
            "next_gate": "Taiwan-specific algebra terminology and prose review",
            "mandarin_simplified_dominance_debt_qualitative": "unresolved: PRC-Mandarin Simplified evidence does not establish Taiwan mathematical register or prose",
        },
        {
            "record_id": "ZH-P37-L005", "language_tag": "zh-Hant-HK", "script": "Hant", "artifact": "",
            "status": "held_unvalidated_no_localization",
            "evidence_scope": "no Hong Kong-specific terminology adaptation prose evidence or reviewer return",
            "prohibited_claim": "Hong Kong localization or acceptance",
            "next_gate": "Hong Kong-specific algebra terminology and prose review",
            "mandarin_simplified_dominance_debt_qualitative": "unresolved: PRC-Mandarin Simplified evidence does not establish Hong Kong written mathematical register or prose",
        },
        {
            "record_id": "ZH-P37-L006", "language_tag": "zh-Hant-MO", "script": "Hant", "artifact": "",
            "status": "held_unvalidated_no_localization",
            "evidence_scope": "no Macao-specific terminology adaptation prose evidence or reviewer return",
            "prohibited_claim": "Macao localization or acceptance",
            "next_gate": "Macao-specific algebra terminology and prose review",
            "mandarin_simplified_dominance_debt_qualitative": "unresolved: PRC-Mandarin Simplified evidence does not establish Macao written mathematical register or prose",
        },
    ]


def occurrence_lines(lines: list[str], needle: str) -> list[int]:
    found: list[int] = []
    for number, line in enumerate(lines, 1):
        found.extend([number] * line.count(needle))
    return found


def validate_source_target(source_lines: list[str], target_lines: list[str]) -> None:
    expected = {
        "source_subsections": [21, 45, 97],
        "target_subsections": [50, 74, 126],
        "source_headings": [27, 40, 53, 56, 69, 74, 81, 101, 158],
        "target_headings": [56, 69, 82, 85, 98, 103, 110, 130, 187],
        "source_footnotes": [11, 15, 15, 17, 30, 43, 59, 75, 82, 82, 144, 161],
        "target_footnotes": [39, 43, 43, 46, 59, 72, 88, 104, 111, 111, 173, 190],
        "source_displays": [33, 48, 60, 91, 105, 111, 117, 124, 132, 140, 145, 151, 162, 168, 175],
        "target_displays": [62, 77, 89, 120, 134, 140, 146, 153, 161, 169, 174, 180, 191, 197, 204],
    }
    observed = {
        "source_subsections": occurrence_lines(source_lines, r"\subsection*{"),
        "target_subsections": occurrence_lines(target_lines, r"\subsection*{"),
        "source_headings": occurrence_lines(source_lines, r"\paragraph{"),
        "target_headings": occurrence_lines(target_lines, r"\paragraph{"),
        "source_footnotes": occurrence_lines(source_lines, r"\footnote{"),
        "target_footnotes": occurrence_lines(target_lines, r"\footnote{"),
        "source_displays": occurrence_lines(source_lines, r"\["),
        "target_displays": occurrence_lines(target_lines, r"\["),
    }
    if observed != expected:
        raise AssertionError(f"Structural event loci drifted:\nobserved={observed}\nexpected={expected}")
    if "Von \\emph{Emmy Noether} in Göttingen." not in source_lines[7]:
        raise AssertionError("Source author line drift")
    if "作者：\\emph{Emmy Noether}，哥廷根。" not in target_lines[35]:
        raise AssertionError("Target author line drift")
    if "vgl. 2a" not in source_lines[153] or "参见 2a" not in target_lines[182]:
        raise AssertionError("2a cross-reference locus drift")
    if "Eingegangen 24. August 1931." not in source_lines[183]:
        raise AssertionError("Source receipt locus drift")
    if "1931 年 8 月 24 日收稿。" not in target_lines[212]:
        raise AssertionError("Target receipt locus drift")


def validate_unit_coverage(source_lines: list[str], target_lines: list[str]) -> None:
    nonroot = [item for item in UNITS if item["suffix"] != "U000"]
    covered_source = set()
    covered_target = set()
    for item in nonroot:
        covered_source.update(range(item["source_start"], item["source_end"] + 1))
        covered_target.update(range(item["target_start"], item["target_end"] + 1))
    missing_source = [n for n in range(1, 188) if source_lines[n - 1].strip() and n not in covered_source]
    missing_target = [n for n in range(29, 215) if target_lines[n - 1].strip() and n not in covered_target]
    if missing_source or missing_target:
        raise AssertionError(f"Nonblank unit coverage gap: source={missing_source}, target={missing_target}")
    suffixes = {item["suffix"] for item in UNITS}
    for item in UNITS:
        if item["parent"] and item["parent"] not in suffixes:
            raise AssertionError(f"Missing parent for {item['suffix']}: {item['parent']}")
        if not (1 <= item["source_start"] <= item["source_end"] <= 187):
            raise AssertionError(f"Bad source range: {item}")
        if not (29 <= item["target_start"] <= item["target_end"] <= 214):
            raise AssertionError(f"Bad target range: {item}")


def validate_csv(path: Path, expected_fields: list[str], expected_rows: int) -> None:
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
    if reader.fieldnames != expected_fields:
        raise AssertionError(f"Header mismatch in {path.name}: {reader.fieldnames}")
    if len(rows) != expected_rows:
        raise AssertionError(f"Row-count mismatch in {path.name}: {len(rows)} != {expected_rows}")
    for row_number, row in enumerate(rows, 2):
        if None in row or set(row) != set(expected_fields):
            raise AssertionError(f"Nonrectangular row {row_number} in {path.name}")
        for field, value in row.items():
            if value is None:
                raise AssertionError(f"Null cell {field} row {row_number} in {path.name}")
            if value.lstrip().startswith(("=", "+", "-", "@")):
                raise AssertionError(f"Spreadsheet-formula-like cell {field} row {row_number} in {path.name}")


def main() -> int:
    if sha256(AUTHORITY) != AUTHORITY_SHA256:
        raise AssertionError("Sealed P31 authority hash mismatch")
    expected_hashes = {
        SOURCE_INTERVAL: SOURCE_INTERVAL_SHA256,
        SOURCE_EXACT: SOURCE_EXACT_SHA256,
        SOURCE: SOURCE_LF_SHA256,
    }
    for path, expected_hash in expected_hashes.items():
        actual = sha256(path)
        if actual != expected_hash:
            raise AssertionError(f"Source custody mismatch for {path}: {actual} != {expected_hash}")

    source_lines = SOURCE.read_text(encoding="utf-8").splitlines()
    target_lines = TARGET.read_text(encoding="utf-8").splitlines()
    validate_source_target(source_lines, target_lines)
    validate_unit_coverage(source_lines, target_lines)

    smap_rows = source_rows()
    sindex_rows = structural_rows()
    loc_rows = localization_rows()
    write_csv(SOURCE_MAP, SOURCE_MAP_FIELDS, smap_rows)
    write_csv(STRUCTURAL_CSV, STRUCTURAL_FIELDS, sindex_rows)
    write_csv(LOCALIZATION_CSV, LOCALIZATION_FIELDS, loc_rows)

    parity_data = json.loads(PARITY.read_text(encoding="utf-8"))
    target_sha = sha256(TARGET)
    target_pdf_record = file_record(TARGET_PDF) if TARGET_PDF.exists() else None
    cursor = {
        "record_id": "ZH-NOE-P37-SOURCE-CURSOR-20260718",
        "work": "Noether complete corpus",
        "unit": "Paper 37 complete logical article",
        "checked_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "authority": {
            "status": "sealed_P31",
            "tex_path": AUTHORITY.as_posix(),
            "tex_sha256_recomputed": sha256(AUTHORITY),
            "tex_sha256_expected": AUTHORITY_SHA256,
            "cumulative_logical_lines": f"{P31_START_LINE}-{P31_LOGICAL_END_LINE}",
            "next_section_starts_at_line": P31_NEXT_SECTION_LINE,
            "logical_half_open_bytes": [1649789, 1672068],
            "ordinary_section_half_open_bytes": [1649789, 1672136],
        },
        "frozen_local_source": {
            "ordinary_section_interval_exact_crlf": file_record(SOURCE_INTERVAL),
            "logical_article_exact_crlf": file_record(SOURCE_EXACT),
            "logical_article_lf": file_record(SOURCE),
        },
        "target": {
            "tex": file_record(TARGET),
            "logical_article_target_lines": "29-214",
            "pdf": target_pdf_record,
        },
        "parity_checkpoint": {
            "path": PARITY.relative_to(ROOT).as_posix(),
            "sha256": sha256(PARITY),
            "status": parity_data.get("status"),
            "unresolved_parity_issues": parity_data.get("unresolved_parity_issues"),
            "captured_target_sha256": parity_data.get("hashes", {}).get("target", {}).get("sha256"),
            "captured_target_matches_current": parity_data.get("hashes", {}).get("target", {}).get("sha256") == target_sha,
        },
        "mapping": {
            "source_unit_map": SOURCE_MAP.relative_to(ROOT).as_posix(),
            "structural_index_csv": STRUCTURAL_CSV.relative_to(ROOT).as_posix(),
            "structural_index_json": STRUCTURAL_JSON.relative_to(ROOT).as_posix(),
            "unit_rows": len(UNITS),
        },
        "shared_pointer_debt": {
            "path": "evidence://local-workspace/interlanguage/03_projects/noether/00_current_german_authority",
            "observed_state": "stale at R821 per controlling CJK brief and Paper 37 claim",
            "use_as_current_authority": False,
            "interim_rule": "continue citing and re-hashing the exact sealed P31 authority above",
        },
        "decision": "Paper 37 mapping remains keyed to the sealed P31 logical article. The inherited Chinese reader is witness material only. This cursor records an internal source-checked, compiled, rendered freeze and does not confer regional or external validation.",
    }

    coverage = {
        "article": 1,
        "metadata": 1,
        "author": 1,
        "opening": 1,
        "subsections": 3,
        "subsection_openings": 3,
        "heading_units_total": 9,
        "theorems": 7,
        "definitions": 1,
        "supplements": 1,
        "footnotes": 12,
        "displays": 15,
        "cross_references": 1,
        "receipt": 1,
        "indexed_total": len(UNITS),
        "known_unindexed_nonblank_source_lines": 0,
        "known_unindexed_nonblank_target_article_lines": 0,
    }
    structural = {
        "schema_version": "1.0.0",
        "index_id": "NOE-P37-ZH-STRUCTURE-20260718",
        "work_id": "NOETHER-P37",
        "language_tag": "zh-Hans-CN",
        "source_authority": {
            "path": SOURCE.relative_to(ROOT).as_posix(),
            "whole_p31_path": AUTHORITY.as_posix(),
            "whole_p31_sha256": AUTHORITY_SHA256,
            "logical_article_exact_crlf_sha256": SOURCE_EXACT_SHA256,
            "logical_article_lf_sha256": SOURCE_LF_SHA256,
            "cumulative_lines": f"{P31_START_LINE}-{P31_LOGICAL_END_LINE}",
        },
        "target": {
            "path": TARGET.relative_to(ROOT).as_posix(),
            "tex_sha256": target_sha,
            "pdf_path": TARGET_PDF.relative_to(ROOT).as_posix() if TARGET_PDF.exists() else None,
            "pdf_sha256": sha256(TARGET_PDF) if TARGET_PDF.exists() else None,
            "completion_state": "complete",
            "review_state": "source_parity_typed_evidence_build_render_pass",
            "publication_state": "handoff_ready",
        },
        "projection": STRUCTURAL_CSV.name,
        "unit_map": SOURCE_MAP.name,
        "localization_status": LOCALIZATION_CSV.name,
        "coverage": coverage,
        "relation_model": {
            "parent": "parent_id",
            "order": "numeric sequence order; decimals retain embedded footnotes displays and cross-reference loci",
            "dependencies": "semicolon-separated structural IDs in CSV",
            "confidence": "high medium or low",
            "ambiguity": "retained explicitly; never silently inferred",
        },
        "validation": {
            "source_target_event_loci": "pass",
            "nonblank_logical_unit_coverage": "pass",
            "source_subsection_count": 3,
            "target_subsection_count": 3,
            "source_heading_count": 9,
            "target_heading_count": 9,
            "source_footnote_count": 12,
            "target_footnote_count": 12,
            "source_display_count": 15,
            "target_display_count": 15,
            "parity_checkpoint_status": parity_data.get("status"),
            "status": "internally_frozen",
            "external_or_human_validation": False,
        },
        "continuation_cursor": "regional localization and independent human algebra review remain open; no SGA work is authorized",
    }

    STRUCTURAL_JSON.write_text(json.dumps(structural, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    CURSOR_JSON.write_text(json.dumps(cursor, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    validate_csv(SOURCE_MAP, SOURCE_MAP_FIELDS, len(UNITS))
    validate_csv(STRUCTURAL_CSV, STRUCTURAL_FIELDS, len(UNITS))
    validate_csv(LOCALIZATION_CSV, LOCALIZATION_FIELDS, 6)
    json.loads(STRUCTURAL_JSON.read_text(encoding="utf-8"))
    json.loads(CURSOR_JSON.read_text(encoding="utf-8"))

    print(f"PASS units={len(UNITS)} localization_rows={len(loc_rows)}")
    for artifact in [SOURCE_MAP, STRUCTURAL_CSV, STRUCTURAL_JSON, CURSOR_JSON, LOCALIZATION_CSV]:
        print(f"{artifact.relative_to(ROOT).as_posix()} SHA256={sha256(artifact)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
