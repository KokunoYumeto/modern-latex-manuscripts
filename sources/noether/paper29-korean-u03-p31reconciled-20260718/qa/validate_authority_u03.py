#!/usr/bin/env python3
"""Replay pinned authority, exact-slice, cursor, and final-binary checks for P29-KO-U03."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "qa" / "U03_AUTHORITY_VALIDATION.json"
SEALED = Path(
    "evidence://local-workspace/Codex/2026-06-01/we-are-currently-doing-a-massive/"
    "Noether_LocalCodex_20260718_P31_FullPaperCanonicalReaudit_WEB_DROP/1/01_current/"
    "cum_de_Local_20260718_P31.tex"
)
CANDIDATE = Path(
    "evidence://local-workspace/Codex/2026-06-01/we-are-currently-doing-a-massive/"
    "Noether_LocalCodex_20260718_P04p133_Eq28_SourceFix/1/01_current/"
    "cum_de_Local_20260718_P04p133_Eq28_SourceFix.tex"
)
FULL_P29 = ROOT / "source" / "Noether_Paper29_German_P31_Sealed_exact_slice.tex"
UNIT = ROOT / "source" / "Noether_Paper29_German_P31_U03_FinitenessCriterionProofSetup_exact_lf.tex"
TARGET_TEX = ROOT / "ko" / "Noether_Paper29_Korean_U03_v001.tex"
TARGET_PDF = ROOT / "ko" / "Noether_Paper29_Korean_U03_v001.pdf"
TARGET_RENDER = ROOT / "visual_inspection" / "Noether_Paper29_Korean_U03_v001.png"

EXPECTED = {
    SEALED: "A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F",
    CANDIDATE: "5D159B7457F2ACBAD583C82D391476659101F9519E7A4B45C97D4BD8A48C7AFD",
    FULL_P29: "904488A1630B36E12352A3313B16CC9283B345E28E5363E48B7E4757B388128F",
    UNIT: "1CD2F142F472BE2A590EC8AACA45CEB49966A09FE803CC410D138B3F7BDE7458",
    TARGET_TEX: "0DFEE79E2DF3A81005BDAF8488E108D9E324703133D0B9548F5A54933975CC60",
    TARGET_PDF: "4E6DEC776EE572EFCC97138F21D0AE98ABA5A8F3DD4E3362E1BD2808A23D7A19",
    TARGET_RENDER: "42E78806891372C91FDB089A5374103B8BD8E4E7BECFC14D1C94C719F7911579",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def decoded(path: Path) -> str:
    return path.read_bytes().decode("utf-8")


def normalized(path: Path) -> str:
    return decoded(path).replace("\r\n", "\n").replace("\r", "\n")


def occurrence_offsets(haystack: str, needle: str) -> list[int]:
    offsets: list[int] = []
    start = 0
    while True:
        found = haystack.find(needle, start)
        if found < 0:
            return offsets
        offsets.append(found)
        start = found + len(needle)


def main() -> int:
    errors: list[str] = []
    file_results: dict[str, dict] = {}
    for path, expected in EXPECTED.items():
        actual = sha256(path) if path.is_file() else None
        file_results[str(path)] = {
            "bytes": path.stat().st_size if path.is_file() else None,
            "sha256": actual,
            "expected_sha256": expected,
        }
        if actual != expected:
            errors.append(f"hash mismatch: {path}: {actual} != {expected}")

    unit_raw = decoded(UNIT)
    unit_lf = normalized(UNIT)
    occurrences: dict[str, dict] = {}
    for authority in (SEALED, CANDIDATE):
        raw_offsets = occurrence_offsets(decoded(authority), unit_raw)
        normalized_offsets = occurrence_offsets(normalized(authority), unit_lf)
        occurrences[str(authority)] = {
            "raw_count": len(raw_offsets),
            "raw_character_offsets": raw_offsets,
            "lf_normalized_count": len(normalized_offsets),
            "lf_normalized_character_offsets": normalized_offsets,
        }
        if len(normalized_offsets) != 1:
            errors.append(f"LF-normalized U03 occurrence count {len(normalized_offsets)} != 1: {authority}")

    full_lines = normalized(FULL_P29).splitlines(keepends=True)
    expected_unit = "".join(full_lines[40:45])
    line_46 = full_lines[45].rstrip("\n") if len(full_lines) >= 46 else None
    line_47 = full_lines[46].rstrip("\n") if len(full_lines) >= 47 else None
    if expected_unit != unit_lf:
        errors.append("full-P29 LF-normalized lines 41-45 do not equal U03 exact source")
    if line_46 != "":
        errors.append(f"full-P29 line 46 is not blank: {line_46!r}")
    expected_47 = "Es sei vorerst vorausgesetzt, daß der Koeffizientenbereich $P$ unendlich viele Elemente enthält."
    if line_47 is None or not line_47.startswith(expected_47):
        errors.append(f"unexpected full-P29 line 47: {line_47!r}")

    report = {
        "schema_version": "1.0.0",
        "work_unit": "P29-KO-U03",
        "authority": {
            "sealed_path": str(SEALED),
            "sealed_sha256": EXPECTED[SEALED],
            "latest_compiled_unsealed_candidate_path": str(CANDIDATE),
            "latest_compiled_unsealed_candidate_sha256": EXPECTED[CANDIDATE],
            "shared_r821_pointer_state": "stale_not_used_as_current_authority",
        },
        "files": file_results,
        "authority_occurrences": occurrences,
        "cursor": {
            "unit_full_p29_lines_inclusive": [41, 45],
            "unit_equals_lf_normalized_lines_41_45": expected_unit == unit_lf,
            "excluded_line_46": line_46,
            "next_substantive_line_number": 47,
            "next_substantive_line": line_47,
        },
        "source_witness_discrepancy": {
            "sealed_tex": "two identical footnote calls and therefore two numbered note bodies",
            "printed_page_31": "two anchors share printed marker 1 and one printed note body",
            "target_choice": "preserve sealed TeX as target authority with two translated numbered note bodies; retain printed mismatch as held source-check debt",
        },
        "review_boundary": {
            "source_hash_and_cursor_replay": "pass" if not errors else "fail",
            "unsealed_candidate_promoted": False,
            "external_human_validation": "absent_do_not_claim",
        },
        "errors": errors,
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"errors": errors, "report": str(REPORT)}, ensure_ascii=False))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
