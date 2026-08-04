#!/usr/bin/env python3
"""Produce controlled-generic Hant v003 from the accepted Paper 35 Hans body.

This is a producer-owned mechanical script-transport step.  It implements the
checker-sealed F015 delimiter fix and deliberately performs no linguistic,
source, formula-content, regional, or visual review.
"""

from __future__ import annotations

from datetime import datetime
from hashlib import sha256
import importlib.metadata
import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parents[4]
VENDORED = WORKSPACE / "tmp/tools/opencc_py"
sys.path.insert(0, str(VENDORED))

from opencc import OpenCC  # type: ignore  # noqa: E402


SCRIPT = Path(__file__).resolve()
HANS = ROOT / (
    "build/zh-Hans-CN-v002/"
    "Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_v002.tex"
)
V002_HANT = ROOT / (
    "build/zh-Hant-controlled-v002/"
    "Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_v002.tex"
)
CHECKER_CANDIDATE = ROOT / (
    "controls/checker_return_v002/selected_members/candidate/zh-Hant-controlled/"
    "Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_checker_candidate_v003.tex"
)
HANT_DIR = ROOT / "build/zh-Hant-controlled-v003"
HANT = HANT_DIR / "Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_v003.tex"
RECORD = ROOT / "controls/OPENCC_PRODUCER_RECORD_v003.json"

EXPECTED_HANS = {
    "bytes": 31328,
    "sha256": "DDF7E898E706552028C2BCEAC4BBDE3D45487C6A339F7FA0A43968FF7E1F465C",
}
EXPECTED_V002_HANT = {
    "bytes": 31515,
    "sha256": "FD16882FAC33B7FD7D0FFB882345168E40FA7F1F22FDEE83AFA2420627D1C054",
}
EXPECTED_CHECKER_CANDIDATE = {
    "bytes": 31515,
    "sha256": "54DE9B43850376FD19306A11FC682166D8F34A4CA6D73E0940695357CE74A005",
}
SEGMENTS = {
    "A": {
        "path": ROOT / "translation/corrected_segments_v002/P35_A_zh-Hans-CN_v002.tex",
        "bytes": 11737,
        "sha256": "26A7615B9EFD825ADF20DABF9DE34673CB1F52807AC7E07A0F0118F79E8DD3EF",
    },
    "B": {
        "path": ROOT / "translation/corrected_segments_v002/P35_B_zh-Hans-CN_v002.tex",
        "bytes": 7451,
        "sha256": "5A2EB988239E78102D18F22AC552978AD987CE299E5B6A0D738FFA87034B2424",
    },
    "C": {
        "path": ROOT / "translation/corrected_segments_v002/P35_C_zh-Hans-CN_v002.tex",
        "bytes": 10620,
        "sha256": "5F62E3139C5528ABCD4ACB978EA6CC14AF1B052E6E3E78CBAFBB10161B5B01B3",
    },
}
RUNTIME_PATHS = {
    "metadata": VENDORED / "opencc_python_reimplemented-0.1.7.dist-info/METADATA",
    "config": VENDORED / "opencc/config/s2t.json",
    "st_phrases": VENDORED / "opencc/dictionary/STPhrases.txt",
    "st_characters": VENDORED / "opencc/dictionary/STCharacters.txt",
}
CONTROL_PATTERN = re.compile(r"\\(?:[A-Za-z@]+|.)")


def digest(data: bytes) -> str:
    return sha256(data).hexdigest().upper()


def file_meta(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    return {"path": str(path), "bytes": len(data), "sha256": digest(data)}


def require_identity(path: Path, expected: dict[str, object], label: str) -> bytes:
    if not path.is_file():
        raise FileNotFoundError(f"Missing {label}: {path}")
    data = path.read_bytes()
    observed = {"bytes": len(data), "sha256": digest(data)}
    if observed != expected:
        raise RuntimeError(f"{label} identity mismatch: expected {expected}, found {observed}")
    return data


def escaped(text: str, index: int) -> bool:
    """Return whether the backslash/token at index follows an odd slash run.

    In particular, the second slash of ``\\\\[0.6em]`` is escaped by the
    first and therefore cannot begin a TeX ``\\[`` display delimiter.
    """

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
    """Locate TeX math delimiters without recognizing escaped delimiter starts."""

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


def main() -> int:
    hans_bytes = require_identity(HANS, EXPECTED_HANS, "accepted Hans v002")
    v002_hant_bytes = require_identity(V002_HANT, EXPECTED_V002_HANT, "rejected Hant v002")
    checker_candidate_bytes = require_identity(
        CHECKER_CANDIDATE, EXPECTED_CHECKER_CANDIDATE, "sealed checker Hant v003 candidate"
    )

    segment_meta: dict[str, dict[str, object]] = {}
    segment_bytes: list[bytes] = []
    for label, expected in SEGMENTS.items():
        path = expected["path"]
        data = require_identity(
            path,
            {"bytes": expected["bytes"], "sha256": expected["sha256"]},
            f"corrected Hans segment {label}",
        )
        segment_bytes.append(data)
        segment_meta[label] = file_meta(path)
    joined_segments = b"".join(segment_bytes)
    if len(joined_segments) != 29808 or digest(joined_segments) != (
        "54061274DFDE806F491EE424277886ED4C4CEEF3F7E0315DFD1039AACF69F18A"
    ):
        raise RuntimeError("Corrected Hans segment concatenation identity mismatch")
    if hans_bytes.count(joined_segments) != 1:
        raise RuntimeError("Accepted Hans does not contain the exact corrected segment concatenation once")

    hans = hans_bytes.decode("utf-8")
    converter = OpenCC("s2t")
    raw_hant, hans_ranges = convert_outside_math(hans, converter)
    hant = raw_hant

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
        normalization_counts[f"{old}->{new}"] = hant.count(old)
        hant = hant.replace(old, new)

    marker = "% Controlled-generic script transport of corrected Hans; independent recheck pending."
    replacement = (
        marker
        + "\n% Controlled generic Traditional script only; not zh-Hant-TW/HK/MO prose."
        + "\n% Corrected Hans wording remains the lexical base; independent Hant recheck is pending."
    )
    if hant.count(marker) != 1:
        raise RuntimeError("Expected exactly one controlled-Hant claim-limit marker")
    hant = hant.replace(marker, replacement, 1)

    hant_ranges = math_ranges(hant)
    hans_math = [hans[start:end] for start, end, _kind in hans_ranges]
    hant_math = [hant[start:end] for start, end, _kind in hant_ranges]
    if hans_math != hant_math:
        raise RuntimeError("Math span stream changed during controlled script transport")
    hans_controls = CONTROL_PATTERN.findall(hans)
    hant_controls = CONTROL_PATTERN.findall(hant)
    if hans_controls != hant_controls:
        raise RuntimeError("TeX control-sequence stream changed during controlled script transport")

    false_display_spans = [
        (start, end)
        for start, end, kind in hans_ranges
        if kind == "display_bracket"
        and "\\\\[0.6em]" in hans[max(0, start - 2): min(len(hans), end)]
    ]
    if false_display_spans:
        raise RuntimeError(f"Legacy F015 false display spans remain: {false_display_spans}")

    output_bytes = hant.encode("utf-8")
    observed_output = {"bytes": len(output_bytes), "sha256": digest(output_bytes)}
    if observed_output != EXPECTED_CHECKER_CANDIDATE:
        raise RuntimeError(
            "Generated Hant v003 does not match sealed checker candidate: "
            f"expected {EXPECTED_CHECKER_CANDIDATE}, found {observed_output}"
        )
    if output_bytes != checker_candidate_bytes:
        raise RuntimeError("Generated Hant v003 bytes differ from the sealed checker candidate")

    if HANT.exists() or RECORD.exists():
        raise RuntimeError(f"Refusing to overwrite existing v003 output or record: {HANT}; {RECORD}")
    HANT_DIR.mkdir(parents=True, exist_ok=True)
    HANT.write_bytes(output_bytes)

    record = {
        "schema_version": "1.0.0",
        "record_type": "producer_controlled_hant_v003_transport",
        "recorded_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "work_id": "NOETHER-P35-ZH",
        "provenance_decision_id": "ZH-D135",
        "freeze_decision_state": "freeze_decision_pending",
        "checker_return_id": "ZHCHK-NOETHER-P35-V002-RETURN-001",
        "finding_applied": "ZHCHK-P35-F015",
        "operation": "producer_only_accepted_hans_to_controlled_generic_hant_v003",
        "producer_script": file_meta(SCRIPT),
        "input_accepted_hans": file_meta(HANS),
        "input_corrected_segments": segment_meta,
        "segment_concatenation": {
            "bytes": len(joined_segments),
            "sha256": digest(joined_segments),
            "occurrences_in_hans": hans_bytes.count(joined_segments),
        },
        "rejected_hant_v002": {
            **file_meta(V002_HANT),
            "custody_only": True,
            "bytes_read_for_identity": len(v002_hant_bytes),
        },
        "sealed_checker_candidate": file_meta(CHECKER_CANDIDATE),
        "converter": {
            "implementation": "opencc-python-reimplemented",
            "version": importlib.metadata.version("opencc-python-reimplemented"),
            "configuration": "s2t",
            "runtime_custody": {
                label: file_meta(path) for label, path in RUNTIME_PATHS.items()
            },
        },
        "scanner": {
            "type": "producer escaped-delimiter recognizer replaying checker-sealed F015 correction",
            "math_span_count_hans": len(hans_ranges),
            "math_span_count_hant": len(hant_ranges),
            "math_stream_equal": hans_math == hant_math,
            "tex_control_count_hans": len(hans_controls),
            "tex_control_count_hant": len(hant_controls),
            "tex_control_stream_equal": hans_controls == hant_controls,
            "legacy_false_display_span_count": len(false_display_spans),
            "f015_rule": (
                "A delimiter start is ignored when preceded by an odd run of backslashes; "
                "therefore the second backslash of \\\\[0.6em] cannot begin \\[."
            ),
        },
        "raw_opencc_output": {
            "bytes": len(raw_hant.encode("utf-8")),
            "sha256": digest(raw_hant.encode("utf-8")),
        },
        "controlled_normalization_counts": normalization_counts,
        "output": file_meta(HANT),
        "exact_checker_candidate_equality": HANT.read_bytes() == checker_candidate_bytes,
        "localization_status": "controlled generic zh-Hant only",
        "explicitly_not": ["zh-Hant-TW", "zh-Hant-HK", "zh-Hant-MO"],
        "lexical_base": "accepted exact zh-Hans-CN v002 producer translation",
        "review_state": "producer transport complete; mechanical compile and independent recheck pending",
        "epistemic_boundary": {
            "source_check_performed": False,
            "semantic_or_formula_content_check_performed": False,
            "translation_quality_check_performed": False,
            "visual_check_performed": False,
            "pdf_opened_or_rendered": False,
            "native_or_regional_validation_performed": False,
            "human_or_external_validation_claimed": False,
            "approval_publication_archive_or_certification_claimed": False,
        },
    }
    RECORD.write_text(
        json.dumps(record, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps(record, ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
