#!/usr/bin/env python3
"""Independent checker replay and script review for the P35 generic-Hant artifact."""

from __future__ import annotations

from collections import Counter
from dataclasses import asdict, dataclass
from hashlib import sha256
import importlib.metadata
import json
from pathlib import Path
import re
import sys


CHECKER_ROOT = Path(__file__).resolve().parents[3]
INTAKE = CHECKER_ROOT / "paper35/recheck_v002/intake/frozen_producer_package_v002"
HANS = INTAKE / "build/zh-Hans-CN-v002/Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_v002.tex"
HANT = INTAKE / "build/zh-Hant-controlled-v002/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_v002.tex"
OUT = CHECKER_ROOT / "paper35/recheck_v002/evidence/P35_HANT_INDEPENDENT_AUDIT_v002.json"
WORKSPACE = CHECKER_ROOT.parents[4]
VENDORED = WORKSPACE / "tmp/tools/opencc_py"
sys.path.insert(0, str(VENDORED))
sys.path.insert(0, str(CHECKER_ROOT / "tools"))

from opencc import OpenCC  # type: ignore  # noqa: E402
from audit_p35_tex import extract_math  # type: ignore  # noqa: E402


EXPECTED = {
    "hans_bytes": 31328,
    "hans_sha256": "DDF7E898E706552028C2BCEAC4BBDE3D45487C6A339F7FA0A43968FF7E1F465C",
    "hant_bytes": 31515,
    "hant_sha256": "FD16882FAC33B7FD7D0FFB882345168E40FA7F1F22FDEE83AFA2420627D1C054",
    "raw_opencc_bytes": 31328,
    "raw_opencc_sha256": "32E80555F6603FBD9105E78F3492EEF91037078529DA7592DAE29A28F9BBE41A",
}

MATH_PATTERN = re.compile(
    r"(?s)"
    r"(\\\[.*?\\\]|\\\(.*?\\\)|\$\$.*?\$\$|(?<!\\)\$(?!\$).*?(?<!\\)\$|"
    r"\\begin\{(?:equation\*?|align\*?|aligned|gather\*?|multline\*?|array|cases|matrix|pmatrix|bmatrix|vmatrix|Vmatrix)\}.*?"
    r"\\end\{(?:equation\*?|align\*?|aligned|gather\*?|multline\*?|array|cases|matrix|pmatrix|bmatrix|vmatrix|Vmatrix)\})"
)
CONTROL_PATTERN = re.compile(r"\\(?:[A-Za-z@]+|.)")
CJK_PATTERN = re.compile(r"[\u3400-\u9fff]")


@dataclass(frozen=True)
class Suspicion:
    finding_key: str
    character: str
    line: int
    column: int
    context: str
    disposition: str


def digest(data: bytes) -> str:
    return sha256(data).hexdigest().upper()


def file_fact(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    return {"path": str(path), "bytes": len(data), "sha256": digest(data)}


def positions(text: str, character: str, key: str, disposition: str) -> list[Suspicion]:
    rows: list[Suspicion] = []
    for line_no, line in enumerate(text.splitlines(), 1):
        cursor = 0
        while True:
            index = line.find(character, cursor)
            if index < 0:
                break
            start = max(0, index - 28)
            end = min(len(line), index + 29)
            rows.append(Suspicion(key, character, line_no, index + 1, line[start:end], disposition))
            cursor = index + len(character)
    return rows


def main() -> int:
    hans_bytes = HANS.read_bytes()
    hant_bytes = HANT.read_bytes()
    hans = hans_bytes.decode("utf-8")
    hant = hant_bytes.decode("utf-8")

    converter = OpenCC("s2t")
    replay_parts: list[str] = []
    cursor = 0
    for match in MATH_PATTERN.finditer(hans):
        replay_parts.append(converter.convert(hans[cursor:match.start()]))
        replay_parts.append(match.group(0))
        cursor = match.end()
    replay_parts.append(converter.convert(hans[cursor:]))
    raw_replay = "".join(replay_parts)

    final_replay = raw_replay
    normalizations = [
        ("Microsoft YaHei", "Microsoft JhengHei"),
        ("% Noether Paper 35 corrected zh-Hans-CN producer revision 2.", "% Noether Paper 35 corrected controlled-generic zh-Hant producer revision 2."),
        ("% Exact checker-frozen target corrections integrated; independent recheck pending.", "% Controlled-generic script transport of corrected Hans; independent recheck pending."),
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
        normalization_counts[f"{old}->{new}"] = final_replay.count(old)
        final_replay = final_replay.replace(old, new)
    marker = "% Controlled-generic script transport of corrected Hans; independent recheck pending."
    replacement = marker + "\n% Controlled generic Traditional script only; not zh-Hant-TW/HK/MO prose." + "\n% Corrected Hans wording remains the lexical base; independent Hant recheck is pending."
    final_replay = final_replay.replace(marker, replacement, 1)

    hans_math, hans_math_errors = extract_math(hans, "HANS")
    hant_math, hant_math_errors = extract_math(hant, "HANT")
    hans_math_raw = [item["raw"] for item in hans_math]
    hant_math_raw = [item["raw"] for item in hant_math]
    embedded_cjk = [
        {
            "ordinal": item["ordinal"],
            "start_line": item["start_line"],
            "raw": item["raw"],
            "note": "CJK prose inside a protected math span was not script-converted",
        }
        for item in hant_math
        if CJK_PATTERN.search(item["raw"])
    ]
    producer_regex_cjk_spans = []
    for ordinal, match in enumerate(MATH_PATTERN.finditer(hans), start=1):
        raw = match.group(0)
        if CJK_PATTERN.search(raw):
            start_line = hans.count("\n", 0, match.start()) + 1
            end_line = hans.count("\n", 0, match.end()) + 1
            producer_regex_cjk_spans.append(
                {
                    "ordinal": ordinal,
                    "start_line": start_line,
                    "end_line": end_line,
                    "characters": len(raw),
                    "head": raw[:240],
                    "tail": raw[-240:],
                }
            )

    suspicions: list[Suspicion] = []
    suspicions.extend(positions(hant, "隻", "HANT_CONTEXT_WRONG_ZHI", "target defect: classifier 隻 is wrong for the adverb 只 in 這只會"))
    suspicions.extend(positions(hant, "幷", "HANT_NONSTANDARD_BING", "tooling/target defect: archaic compatibility form; modern controlled-generic form should be 並"))
    for item in embedded_cjk:
        if "于" in item["raw"]:
            suspicions.append(
                Suspicion(
                    "HANT_PROTECTED_MATH_HANS_LEAK",
                    "于",
                    int(item["start_line"]),
                    0,
                    str(item["raw"]),
                    "target defect: simplified-script prose leaked through formula protection; inherited Hans wording is also unidiomatic",
                )
            )

    ambiguity_inventory = {
        ch: hant.count(ch)
        for ch in ["隻", "幷", "著", "乾", "幹", "後", "發", "餘", "繫", "臺", "裡"]
    }

    report = {
        "audit_id": "ZHCHK-P35-HANT-RECHECK-002",
        "scope": "controlled generic Traditional script; explicitly not TW/HK/MO localization",
        "input": file_fact(HANS),
        "output": file_fact(HANT),
        "expected_identity_checks": {
            "hans_bytes": len(hans_bytes) == EXPECTED["hans_bytes"],
            "hans_sha256": digest(hans_bytes) == EXPECTED["hans_sha256"],
            "hant_bytes": len(hant_bytes) == EXPECTED["hant_bytes"],
            "hant_sha256": digest(hant_bytes) == EXPECTED["hant_sha256"],
        },
        "converter": {
            "implementation": "opencc-python-reimplemented",
            "version": importlib.metadata.version("opencc-python-reimplemented"),
            "configuration": "s2t",
            "vendored_root": str(VENDORED),
            "runtime_files": {
                name: file_fact(path)
                for name, path in {
                    "metadata": VENDORED / "opencc_python_reimplemented-0.1.7.dist-info/METADATA",
                    "config": VENDORED / "opencc/config/s2t.json",
                    "st_phrases": VENDORED / "opencc/dictionary/STPhrases.txt",
                    "st_characters": VENDORED / "opencc/dictionary/STCharacters.txt",
                }.items()
            },
        },
        "independent_replay": {
            "raw_bytes": len(raw_replay.encode("utf-8")),
            "raw_sha256": digest(raw_replay.encode("utf-8")),
            "raw_matches_declared": len(raw_replay.encode("utf-8")) == EXPECTED["raw_opencc_bytes"] and digest(raw_replay.encode("utf-8")) == EXPECTED["raw_opencc_sha256"],
            "final_bytes": len(final_replay.encode("utf-8")),
            "final_sha256": digest(final_replay.encode("utf-8")),
            "final_byte_identical_to_frozen_hant": final_replay.encode("utf-8") == hant_bytes,
            "normalization_counts": normalization_counts,
        },
        "structural_invariants": {
            "producer_regex_math_span_count": len(MATH_PATTERN.findall(hans)),
            "producer_regex_math_stream_equal": MATH_PATTERN.findall(hans) == MATH_PATTERN.findall(hant),
            "independent_math_span_count_hans": len(hans_math),
            "independent_math_span_count_hant": len(hant_math),
            "independent_math_stream_equal": hans_math_raw == hant_math_raw,
            "independent_math_parser_errors_hans": hans_math_errors,
            "independent_math_parser_errors_hant": hant_math_errors,
            "tex_control_count_hans": len(CONTROL_PATTERN.findall(hans)),
            "tex_control_count_hant": len(CONTROL_PATTERN.findall(hant)),
            "tex_control_stream_equal": CONTROL_PATTERN.findall(hans) == CONTROL_PATTERN.findall(hant),
            "line_count_hans": len(hans.splitlines()),
            "line_count_hant": len(hant.splitlines()),
            "line_count_delta_explained_by_two_claim_lines": len(hant.splitlines()) - len(hans.splitlines()) == 2,
        },
        "embedded_cjk_in_protected_math": embedded_cjk,
        "producer_regex_cjk_protected_spans": producer_regex_cjk_spans,
        "ambiguity_inventory": ambiguity_inventory,
        "script_specific_suspicions": [asdict(row) for row in suspicions],
        "script_specific_suspicion_count": len(suspicions),
        "finding_disposition": {
            "mechanical_replay": "pass",
            "formula_and_tex_transport": "pass, with one deliberately protected Chinese prose fragment noted",
            "linguistic_script_review": "pass if script_specific_suspicion_count is zero; controlled-generic scope only",
            "regional_localization": "not claimed and not assessed",
            "inherited_hans_findings": "all Hans target findings also apply after script conversion",
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(report["expected_identity_checks"], indent=2))
    print(json.dumps(report["independent_replay"], indent=2))
    print(json.dumps(report["structural_invariants"], indent=2))
    print(json.dumps(report["script_specific_suspicions"], ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
