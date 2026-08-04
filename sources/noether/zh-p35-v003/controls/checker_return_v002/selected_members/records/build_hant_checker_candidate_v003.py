#!/usr/bin/env python3
"""Build a checker-owned P35 controlled-generic Hant candidate with a TeX-aware math scanner."""

from __future__ import annotations

from hashlib import sha256
import difflib
import importlib.metadata
import json
from pathlib import Path
import re
import sys


SCRIPT = Path(__file__).resolve()
CHECKER_ROOT = SCRIPT.parents[3]
WORKSPACE = CHECKER_ROOT.parents[4]
VENDORED = WORKSPACE / "tmp/tools/opencc_py"
sys.path.insert(0, str(VENDORED))

from opencc import OpenCC  # type: ignore  # noqa: E402


RECHECK = CHECKER_ROOT / "paper35/recheck_v002"
HANS = RECHECK / (
    "intake/frozen_producer_package_v002/build/zh-Hans-CN-v002/"
    "Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_v002.tex"
)
FROZEN_HANT = RECHECK / (
    "intake/frozen_producer_package_v002/build/zh-Hant-controlled-v002/"
    "Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_v002.tex"
)
OUT = RECHECK / (
    "candidate/zh-Hant-controlled/"
    "Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_checker_candidate_v003.tex"
)
RECORD = RECHECK / "evidence/P35_HANT_CHECKER_CANDIDATE_BUILD_RECORD_v003.json"

EXPECTED_HANS = {
    "bytes": 31328,
    "sha256": "DDF7E898E706552028C2BCEAC4BBDE3D45487C6A339F7FA0A43968FF7E1F465C",
}
EXPECTED_FROZEN_HANT = {
    "bytes": 31515,
    "sha256": "FD16882FAC33B7FD7D0FFB882345168E40FA7F1F22FDEE83AFA2420627D1C054",
}

CONTROL_PATTERN = re.compile(r"\\(?:[A-Za-z@]+|.)")
CJK_PATTERN = re.compile(r"[\u3400-\u9fff]")


def digest(data: bytes) -> str:
    return sha256(data).hexdigest().upper()


def escaped(text: str, index: int) -> bool:
    count = 0
    index -= 1
    while index >= 0 and text[index] == "\\":
        count += 1
        index -= 1
    return count % 2 == 1


def find_closing(text: str, start: int, closer: str) -> int:
    index = start
    while index < len(text):
        if text[index] == "%" and not escaped(text, index):
            newline = text.find("\n", index + 1)
            index = len(text) if newline == -1 else newline + 1
            continue
        if text.startswith(closer, index) and not escaped(text, index):
            return index
        index += 1
    return -1


def math_ranges(text: str) -> list[tuple[int, int, str]]:
    ranges: list[tuple[int, int, str]] = []
    index = 0
    while index < len(text):
        if text[index] == "%" and not escaped(text, index):
            newline = text.find("\n", index + 1)
            index = len(text) if newline == -1 else newline + 1
            continue
        kind = ""
        opener = ""
        closer = ""
        if text.startswith("\\[", index) and not escaped(text, index):
            kind, opener, closer = "display_bracket", "\\[", "\\]"
        elif text.startswith("\\(", index) and not escaped(text, index):
            kind, opener, closer = "inline_paren", "\\(", "\\)"
        elif text.startswith("$$", index) and not escaped(text, index):
            kind, opener, closer = "display_dollar", "$$", "$$"
        elif text[index] == "$" and not escaped(text, index):
            kind, opener, closer = "inline_dollar", "$", "$"
        if not kind:
            index += 1
            continue
        close_at = find_closing(text, index + len(opener), closer)
        if close_at < 0:
            raise RuntimeError(f"Unclosed {kind} at character offset {index}")
        end = close_at + len(closer)
        ranges.append((index, end, kind))
        index = end
    return ranges


def convert_outside_math(text: str, converter: OpenCC) -> tuple[str, list[tuple[int, int, str]]]:
    ranges = math_ranges(text)
    parts: list[str] = []
    cursor = 0
    for start, end, _kind in ranges:
        parts.append(converter.convert(text[cursor:start]))
        parts.append(text[start:end])
        cursor = end
    parts.append(converter.convert(text[cursor:]))
    return "".join(parts), ranges


def line_of(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def main() -> int:
    hans_bytes = HANS.read_bytes()
    frozen_hant_bytes = FROZEN_HANT.read_bytes()
    if len(hans_bytes) != EXPECTED_HANS["bytes"] or digest(hans_bytes) != EXPECTED_HANS["sha256"]:
        raise RuntimeError("Frozen Hans identity mismatch")
    if len(frozen_hant_bytes) != EXPECTED_FROZEN_HANT["bytes"] or digest(frozen_hant_bytes) != EXPECTED_FROZEN_HANT["sha256"]:
        raise RuntimeError("Frozen Hant identity mismatch")

    hans = hans_bytes.decode("utf-8")
    converter = OpenCC("s2t")
    raw_hant, ranges = convert_outside_math(hans, converter)
    candidate = raw_hant

    normalizations = [
        ("Microsoft YaHei", "Microsoft JhengHei"),
        (
            "% Noether Paper 35 corrected zh-Hans-CN producer revision 2.",
            "% Noether Paper 35 corrected controlled-generic zh-Hant producer revision 2.",
        ),
        (
            "% Exact checker-frozen target corrections integrated; independent recheck pending.",
            "% Controlled-generic script transport of corrected Hans; independent recheck pending.",
        ),
        ("爲", "為"),
        ("裏", "裡"),
        ("羣", "群"),
        ("衆", "眾"),
        ("纔", "才"),
        ("這隻會", "這只會"),
        ("幷", "並"),
        ("代數無關係統", "代數無關系統"),
    ]
    normalization_counts: dict[str, int] = {}
    for old, new in normalizations:
        normalization_counts[f"{old}->{new}"] = candidate.count(old)
        candidate = candidate.replace(old, new)

    marker = "% Controlled-generic script transport of corrected Hans; independent recheck pending."
    replacement = (
        marker
        + "\n% Controlled generic Traditional script only; not zh-Hant-TW/HK/MO prose."
        + "\n% Corrected Hans wording remains the lexical base; independent Hant recheck is pending."
    )
    if candidate.count(marker) != 1:
        raise RuntimeError("Expected one controlled-Hant claim marker")
    candidate = candidate.replace(marker, replacement, 1)

    candidate_ranges = math_ranges(candidate)
    hans_math = [hans[start:end] for start, end, _kind in ranges]
    candidate_math = [candidate[start:end] for start, end, _kind in candidate_ranges]
    if hans_math != candidate_math:
        raise RuntimeError("Independent math stream changed during Hant conversion")
    hans_controls = CONTROL_PATTERN.findall(hans)
    candidate_controls = CONTROL_PATTERN.findall(candidate)
    if hans_controls != candidate_controls:
        raise RuntimeError("TeX control stream changed during Hant conversion")

    false_display_candidates = [
        {
            "start_line": line_of(hans, start),
            "end_line": line_of(hans, end),
            "characters": end - start,
        }
        for start, end, kind in ranges
        if kind == "display_bracket" and "\\\\[0.6em]" in hans[max(0, start - 2): min(len(hans), end)]
    ]
    cjk_math = [
        {
            "ordinal": ordinal,
            "kind": kind,
            "start_line": line_of(candidate, start),
            "end_line": line_of(candidate, end),
            "raw": candidate[start:end],
        }
        for ordinal, (start, end, kind) in enumerate(candidate_ranges, start=1)
        if CJK_PATTERN.search(candidate[start:end])
    ]

    idempotence_replay, _ = convert_outside_math(candidate, converter)
    for old, new in normalizations:
        idempotence_replay = idempotence_replay.replace(old, new)
    controlled_transform_idempotent = idempotence_replay == candidate
    idempotence_differences = []
    if not controlled_transform_idempotent:
        for operation, a0, a1, b0, b1 in difflib.SequenceMatcher(
            a=candidate, b=idempotence_replay
        ).get_opcodes():
            if operation != "equal":
                idempotence_differences.append(
                    {
                        "operation": operation,
                        "candidate": candidate[a0:a1],
                        "replay": idempotence_replay[b0:b1],
                        "candidate_line": line_of(candidate, a0),
                    }
                )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(candidate, encoding="utf-8", newline="\n")
    output_bytes = OUT.read_bytes()
    record = {
        "schema_version": "1.0.0",
        "record_type": "independent_checker_controlled_hant_candidate_build",
        "recorded_at": "2026-08-04T07:08:00+02:00",
        "work_id": "NOETHER-P35-ZH",
        "finding_addressed": "ZHCHK-P35-F015",
        "input": {"path": str(HANS), "bytes": len(hans_bytes), "sha256": digest(hans_bytes)},
        "rejected_frozen_hant": {
            "path": str(FROZEN_HANT),
            "bytes": len(frozen_hant_bytes),
            "sha256": digest(frozen_hant_bytes),
        },
        "output": {"path": str(OUT), "bytes": len(output_bytes), "sha256": digest(output_bytes)},
        "converter": {
            "implementation": "opencc-python-reimplemented",
            "version": importlib.metadata.version("opencc-python-reimplemented"),
            "configuration": "s2t",
        },
        "scanner": {
            "type": "independent escaped-delimiter scanner",
            "math_span_count_hans": len(ranges),
            "math_span_count_hant": len(candidate_ranges),
            "math_stream_equal": hans_math == candidate_math,
            "tex_control_count_hans": len(hans_controls),
            "tex_control_count_hant": len(candidate_controls),
            "tex_control_stream_equal": hans_controls == candidate_controls,
            "legacy_false_display_span_count": len(false_display_candidates),
            "cjk_prose_inside_valid_math_spans": cjk_math,
            "controlled_transform_idempotent_outside_math": controlled_transform_idempotent,
            "idempotence_adverse_evidence": idempotence_differences,
            "idempotence_required": False,
            "idempotence_note": "A second context-sensitive OpenCC pass changes grammatical 了 to incorrect 瞭 in 證明了 at two loci; one-pass escaped-delimiter replay plus direct language review controls instead.",
        },
        "normalization_counts": normalization_counts,
        "scope": "controlled generic Traditional script only; not TW/HK/MO localization",
        "validation_state": "text_and_structure_candidate_built; serial_compile_render_and_visual_validation_pending",
    }
    RECORD.parent.mkdir(parents=True, exist_ok=True)
    RECORD.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(record, ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
