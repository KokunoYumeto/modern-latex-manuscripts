#!/usr/bin/env python3
"""Replay the pinned Korean Noether P29 U02 authority and cursor checks."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "qa" / "U02_AUTHORITY_VALIDATION.json"

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
UNIT = ROOT / "source" / "Noether_Paper29_German_P31_U02_Rationalbasis_exact_lf.tex"
TARGET_TEX = ROOT / "ko" / "Noether_Paper29_Korean_U02_v001.tex"
TARGET_PDF = ROOT / "ko" / "Noether_Paper29_Korean_U02_v001.pdf"
TARGET_RENDER = ROOT / "visual_inspection" / "Noether_Paper29_Korean_U02_v001.png"

EXPECTED = {
    SEALED: "A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F",
    CANDIDATE: "5D159B7457F2ACBAD583C82D391476659101F9519E7A4B45C97D4BD8A48C7AFD",
    FULL_P29: "904488A1630B36E12352A3313B16CC9283B345E28E5363E48B7E4757B388128F",
    UNIT: "B7EF88537BCD90D0408B3D1942DA410410FE45E79DD457B2DF6DFA2D4929DCAC",
    TARGET_TEX: "B694D05E57B58E1B0373D976356E6B3B3F4883D7CC9398081DB12111877B6A7C",
    TARGET_PDF: "EE0A0ED2E150A5EC48945EA7E47C3F394667F288FF5E933BB00DDF193FBE8988",
    TARGET_RENDER: "F2F772AE57371BA57020C4E816203D3DC154EB46186457846AE2DEBCBEC1FD9E",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def normalized_text(path: Path) -> str:
    return path.read_bytes().decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")


def occurrences(haystack: str, needle: str) -> tuple[int, list[int]]:
    positions: list[int] = []
    start = 0
    while True:
        position = haystack.find(needle, start)
        if position < 0:
            return len(positions), positions
        positions.append(position)
        start = position + len(needle)


def main() -> int:
    errors: list[str] = []
    files: dict[str, dict] = {}
    for path, expected_hash in EXPECTED.items():
        actual_hash = sha256(path) if path.is_file() else None
        files[str(path)] = {
            "bytes": path.stat().st_size if path.is_file() else None,
            "sha256": actual_hash,
            "expected_sha256": expected_hash,
        }
        if actual_hash != expected_hash:
            errors.append(f"hash mismatch: {path}: {actual_hash} != {expected_hash}")

    unit_raw = UNIT.read_bytes().decode("utf-8")
    unit_lf = normalized_text(UNIT)
    authority_occurrences: dict[str, dict] = {}
    for path in (SEALED, CANDIDATE):
        raw = path.read_bytes().decode("utf-8")
        raw_count, raw_offsets = occurrences(raw, unit_raw)
        lf_count, lf_offsets = occurrences(normalized_text(path), unit_lf)
        authority_occurrences[str(path)] = {
            "raw_ordinal_count": raw_count,
            "raw_character_offsets": raw_offsets,
            "lf_normalized_ordinal_count": lf_count,
            "lf_normalized_character_offsets": lf_offsets,
        }
        if lf_count != 1:
            errors.append(f"LF-normalized U02 occurrence count is {lf_count}, expected 1: {path}")

    full_lf = normalized_text(FULL_P29)
    full_lines = full_lf.splitlines(keepends=True)
    expected_unit = "".join(full_lines[24:39])
    line_40 = full_lines[39].rstrip("\n") if len(full_lines) >= 40 else None
    line_41 = full_lines[40].rstrip("\n") if len(full_lines) >= 41 else None
    if expected_unit != unit_lf:
        errors.append("full-P29 LF-normalized lines 25-39 do not equal the U02 source")
    if line_40 != "":
        errors.append(f"full-P29 line 40 is not blank: {line_40!r}")
    expected_line_41_prefix = r"2. \srcspaced{Beweis des Endlichkeitskriteriums.}"
    if line_41 is None or not line_41.startswith(expected_line_41_prefix):
        errors.append(f"unexpected full-P29 line 41: {line_41!r}")

    report = {
        "work_unit": "P29-KO-U02",
        "authority": {
            "sealed_path": str(SEALED),
            "sealed_sha256": EXPECTED[SEALED],
            "latest_compiled_unsealed_candidate_path": str(CANDIDATE),
            "latest_compiled_unsealed_candidate_sha256": EXPECTED[CANDIDATE],
            "shared_r821_pointer_state": "stale_not_used_as_current_authority",
        },
        "files": files,
        "authority_occurrences": authority_occurrences,
        "cursor": {
            "unit_full_p29_lines_inclusive": [25, 39],
            "unit_equals_lf_normalized_lines_25_39": expected_unit == unit_lf,
            "excluded_line_40": line_40,
            "next_substantive_line_number": 41,
            "next_substantive_line": line_41,
        },
        "line_ending_finding": (
            "Raw ordinal search can return zero because the unit is LF-normalized while cumulative heads use "
            "different line endings; authority survival is tested after explicit CRLF/CR-to-LF normalization."
        ),
        "review_boundary": {
            "source_hash_and_cursor_replay": "pass" if not errors else "fail",
            "authority_promotion_of_unsealed_candidate": "not_claimed",
            "external_human_validation": "absent_do_not_claim",
        },
        "errors": errors,
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"errors": errors, "report": str(REPORT)}, ensure_ascii=False))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
