#!/usr/bin/env python3
"""Generate controlled-generic Hant from the hash-pinned P08 Hans target."""

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
VENDORED = WORKSPACE / "tmp" / "tools" / "opencc_py"
sys.path.insert(0, str(VENDORED))

from opencc import OpenCC  # type: ignore  # noqa: E402


HANS = ROOT / "zh-Hans-CN" / "hans.tex"
HANT = ROOT / "zh-Hant-controlled" / "hant.tex"
RECORD = ROOT / "qa" / "hant.json"
EXPECTED_HANS = {
    "bytes": 25041,
    "sha256": "C103A219FEC5CD43090305E5720A7BB17DC2DB9BB682778F9CEC40E8124C4A53",
}
CONTROL_PATTERN = re.compile(r"\\(?:[A-Za-z@]+|.)")
RUNTIME_PATHS = {
    "metadata": VENDORED / "opencc_python_reimplemented-0.1.7.dist-info" / "METADATA",
    "config": VENDORED / "opencc" / "config" / "s2t.json",
    "phrases": VENDORED / "opencc" / "dictionary" / "STPhrases.txt",
    "characters": VENDORED / "opencc" / "dictionary" / "STCharacters.txt",
}


def digest(data: bytes) -> str:
    return sha256(data).hexdigest().upper()


def meta(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    return {"path": str(path), "bytes": len(data), "sha256": digest(data)}


def escaped(text: str, index: int) -> bool:
    count = 0
    index -= 1
    while index >= 0 and text[index] == "\\":
        count += 1
        index -= 1
    return count % 2 == 1


def find_close(text: str, start: int, closer: str) -> int:
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
    """Recognize unescaped TeX math delimiters, including the P35 F015 fix."""

    ranges: list[tuple[int, int, str]] = []
    index = 0
    while index < len(text):
        if text[index] == "%" and not escaped(text, index):
            newline = text.find("\n", index + 1)
            index = len(text) if newline == -1 else newline + 1
            continue
        kind = opener = closer = ""
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
        close_at = find_close(text, index + len(opener), closer)
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
    if HANT.exists() or RECORD.exists():
        raise RuntimeError(f"Refusing to overwrite Hant output: {HANT}; {RECORD}")
    hans_bytes = HANS.read_bytes()
    observed_hans = {"bytes": len(hans_bytes), "sha256": digest(hans_bytes)}
    if observed_hans != EXPECTED_HANS:
        raise RuntimeError(f"Hans identity mismatch: {observed_hans}")

    hans = hans_bytes.decode("utf-8")
    converter = OpenCC("s2t")
    raw_hant, hans_ranges = convert_outside_math(hans, converter)
    hant = raw_hant

    replacements = [
        (
            "% Noether Paper 8 complete zh-Hans-CN producer translation, v001.",
            "% Noether Paper 8 controlled-generic zh-Hant producer transport, v001.",
        ),
        (
            "% Producer translation/build/package only; independent check pending.",
            "% Controlled generic Traditional script only; not zh-Hant-TW/HK/MO prose.\n"
            "% Producer transport/build/package only; independent check pending.",
        ),
        ("Microsoft YaHei", "Microsoft JhengHei"),
        ("爲", "為"),
        ("裏", "裡"),
        ("羣", "群"),
        ("衆", "眾"),
        ("纔", "才"),
        ("幷", "並"),
        ("代數無關係統", "代數無關系統"),
        ("超復", "超複"),
        ("一箇", "一個"),
        ("着手", "著手"),
    ]
    replacement_counts: dict[str, int] = {}
    for old, new in replacements:
        count = hant.count(old)
        replacement_counts[f"{old}->{new}"] = count
        hant = hant.replace(old, new)

    if "not zh-Hant-TW/HK/MO prose" not in hant:
        raise RuntimeError("Controlled-Hant claim-limit marker is absent")
    hant_ranges = math_ranges(hant)
    hans_math = [hans[start:end] for start, end, _kind in hans_ranges]
    hant_math = [hant[start:end] for start, end, _kind in hant_ranges]
    if hans_math != hant_math:
        raise RuntimeError("Math span stream changed during controlled script transport")
    hans_controls = CONTROL_PATTERN.findall(hans)
    hant_controls = CONTROL_PATTERN.findall(hant)
    if hans_controls != hant_controls:
        raise RuntimeError("TeX control stream changed during controlled script transport")
    false_spans = [
        (start, end)
        for start, end, kind in hans_ranges
        if kind == "display_bracket"
        and "\\\\[" in hans[max(0, start - 2) : min(len(hans), end)]
    ]
    if false_spans:
        raise RuntimeError(f"Escaped display delimiter misread: {false_spans}")

    output = hant.encode("utf-8")
    HANT.parent.mkdir(parents=True, exist_ok=True)
    HANT.write_bytes(output)
    record = {
        "schema_version": "1.0.0",
        "record_type": "producer_controlled_hant_transport",
        "recorded_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "work_id": "NOETHER-P08-ZH",
        "authority_binder": "NOETH-DE-BINDER-P08-ZH-COMPLETE-20260804-001",
        "input_hans": meta(HANS),
        "converter": {
            "implementation": "opencc-python-reimplemented",
            "version": importlib.metadata.version("opencc-python-reimplemented"),
            "configuration": "s2t",
            "runtime": {name: meta(path) for name, path in RUNTIME_PATHS.items()},
        },
        "scanner": {
            "type": "escaped-delimiter recognizer inherited from accepted P35 F015 fix",
            "math_spans": len(hans_ranges),
            "math_stream_equal": hans_math == hant_math,
            "tex_controls": len(hans_controls),
            "tex_control_stream_equal": hans_controls == hant_controls,
            "false_display_spans": len(false_spans),
        },
        "raw_opencc": {
            "bytes": len(raw_hant.encode("utf-8")),
            "sha256": digest(raw_hant.encode("utf-8")),
        },
        "controlled_replacement_counts": replacement_counts,
        "output": meta(HANT),
        "localization_status": "controlled generic zh-Hant only",
        "explicitly_not": ["zh-Hant-TW", "zh-Hant-HK", "zh-Hant-MO"],
        "review_state": "producer mechanical transport complete; independent check pending",
        "epistemic_boundary": {
            "source_or_scan_check_performed": False,
            "semantic_or_formula_content_check_performed": False,
            "translation_quality_check_performed": False,
            "visual_check_performed": False,
            "native_or_regional_validation_performed": False,
            "human_or_external_validation_claimed": False,
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
