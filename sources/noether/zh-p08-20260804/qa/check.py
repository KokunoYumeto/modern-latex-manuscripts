#!/usr/bin/env python3
"""Run producer-side mechanical gates for P08 without substantive checking."""

from __future__ import annotations

import csv
from datetime import datetime
from hashlib import sha256
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "qa" / "check.json"
CONTROL = re.compile(r"\\(?:[A-Za-z@]+|.)")
ENV = re.compile(r"\\(begin|end)\{([^{}]+)\}")
ENV_MATH = re.compile(
    r"\\begin\{(equation\*?|align\*?|gather\*?|multline\*?)\}(.*?)\\end\{\1\}",
    re.DOTALL,
)

SEGMENTS = [
    (
        "S01",
        ROOT / "segments" / "source" / "P08_S01_INTRO_I_source_LF.tex",
        ROOT / "segments" / "zh-Hans-CN" / "assembly_normalized" / "P08_S01_INTRO_I_zh-Hans-CN_assembly_v001.tex",
    ),
    (
        "S02",
        ROOT / "segments" / "source" / "P08_S02_II_source_LF.tex",
        ROOT / "segments" / "zh-Hans-CN" / "P08_S02_II_zh-Hans-CN_v001.tex",
    ),
    (
        "S03",
        ROOT / "segments" / "source" / "P08_S03_III_source_LF.tex",
        ROOT / "segments" / "zh-Hans-CN" / "assembly_normalized" / "P08_S03_III_zh-Hans-CN_assembly_v001.tex",
    ),
]
PINNED = {
    "segments/source/P08_S01_INTRO_I_source_LF.tex": (5921, "2FFAD37FC535DBCAC04D8A6D41A8E7397A44FFD151FB5920A2DAC9E5CCF5F161"),
    "segments/source/P08_S02_II_source_LF.tex": (12345, "BAB839C8BB814FE91D3A0BD420981E861E1D11AE315B3005281E8F3A2677668E"),
    "segments/source/P08_S03_III_source_LF.tex": (7112, "9DE743A4238F62E16002032BCFBE2F20A4EC12005959B2BE5393D0122AA219FA"),
    "segments/zh-Hans-CN/assembly_normalized/P08_S01_INTRO_I_zh-Hans-CN_assembly_v001.tex": (5310, "08038923D412BD6452BC0F79A7D6527277D023F253FB56B28D44096289C45652"),
    "segments/zh-Hans-CN/P08_S02_II_zh-Hans-CN_v001.tex": (11536, "F0088AAB791F84B1033CD502046DC2BC7175AABFC113ADC44ABD97BDEFE618EA"),
    "segments/zh-Hans-CN/assembly_normalized/P08_S03_III_zh-Hans-CN_assembly_v001.tex": (6723, "8C35C68B76146875575196C7BB2E0506F931DDAC0C08D085F00BD58772F5E54E"),
    "zh-Hans-CN/hans.tex": (25041, "C103A219FEC5CD43090305E5720A7BB17DC2DB9BB682778F9CEC40E8124C4A53"),
    "zh-Hant-controlled/hant.tex": (25124, "9C7BFA338E342311AC5F711D07F7FE9FF66E35B55132458E6D5CB2076515148B"),
    "build/hans2/hans.pdf": (241593, "67B1E2FBC7CCA53D4B63A3DF760E20201A7C301505CCC83C6372686401E226CE"),
    "build/hant/hant.pdf": (250934, "23AAC5666C5FEF11D87E36FA9E3E0FFFC3AC49879FB36125267FFAD4A1EA8115"),
    "evidence/terms.csv": (36239, "43E2E2451609294FAFD3FB9FFA6DF11C134076AC3AFA5B0F50594CDD4AD0B643"),
    "evidence/adverse.csv": (31918, "263F646A446DE8C33F9DA777ECA3A86721AC2AB767161D603685C4BDA92F7447"),
    "evidence/crosswalk.csv": (33196, "1D8F5E105A97B6B350CDB6EA0AC098435136EF55C83C37564F21F6A8DE75EB09"),
    "evidence/graph.json": (85276, "4F8A5B3E25A60B290AC7AB1AA254046F3600DC8F108B32CE9BD6217B89C6815C"),
}
MATH_TEXT_NORMALIZATIONS = [
    ("\\text{其中 }", "\\text{wo }", 2),
    ("\\text{由变量组构成的行列式 }", "\\text{Determinanten der }", 1),
]


def digest(data: bytes) -> str:
    return sha256(data).hexdigest().upper()


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


def math_spans(text: str) -> list[str]:
    spans: list[str] = []
    index = 0
    while index < len(text):
        if text[index] == "%" and not escaped(text, index):
            newline = text.find("\n", index + 1)
            index = len(text) if newline == -1 else newline + 1
            continue
        opener = closer = ""
        if text.startswith("\\[", index) and not escaped(text, index):
            opener, closer = "\\[", "\\]"
        elif text.startswith("\\(", index) and not escaped(text, index):
            opener, closer = "\\(", "\\)"
        elif text.startswith("$$", index) and not escaped(text, index):
            opener = closer = "$$"
        elif text[index] == "$" and not escaped(text, index):
            opener = closer = "$"
        if not opener:
            index += 1
            continue
        close = find_close(text, index + len(opener), closer)
        if close < 0:
            raise RuntimeError(f"Unclosed math delimiter at {index}")
        end = close + len(closer)
        spans.append(text[index:end])
        index = end
    return spans


def environment_math_spans(text: str) -> list[str]:
    return [match.group(0) for match in ENV_MATH.finditer(text)]


def csv_gate(path: Path, fields: int, required: set[str]) -> dict[str, object]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        headers = reader.fieldnames or []
    if len(headers) != fields or len(rows) != 28 or not required.issubset(headers):
        raise RuntimeError(f"CSV gate failed for {path}: {len(headers)} fields, {len(rows)} rows")
    return {"fields": len(headers), "rows": len(rows), "required_fields_present": True}


def main() -> int:
    if OUT.exists():
        raise RuntimeError(f"Refusing to overwrite check record: {OUT}")
    identities: dict[str, object] = {}
    for relative, expected in PINNED.items():
        path = ROOT / relative
        data = path.read_bytes()
        observed = (len(data), digest(data))
        if observed != expected:
            raise RuntimeError(f"Identity mismatch for {relative}: {observed}")
        identities[relative] = {"bytes": observed[0], "sha256": observed[1]}

    segment_results: list[dict[str, object]] = []
    source_all = ""
    target_all = ""
    normalization_totals = {old: 0 for old, _new, _count in MATH_TEXT_NORMALIZATIONS}
    for label, source_path, target_path in SEGMENTS:
        source = source_path.read_text(encoding="utf-8")
        target = target_path.read_text(encoding="utf-8")
        source_all += source
        target_all += target
        source_controls_raw = CONTROL.findall(source)
        target_controls_raw = CONTROL.findall(target)
        # Explicit line-break controls are target-layout typography, not formula structure.
        source_controls = [token for token in source_controls_raw if token != "\\\\"]
        target_controls = [token for token in target_controls_raw if token != "\\\\"]
        source_env = ENV.findall(source)
        target_env = ENV.findall(target)
        source_delimited_math = math_spans(source)
        target_delimited_math = math_spans(target)
        source_environment_math = environment_math_spans(source)
        target_environment_math = environment_math_spans(target)
        source_math = source_delimited_math + source_environment_math
        target_math_raw = target_delimited_math + target_environment_math
        target_math = list(target_math_raw)
        applied: dict[str, int] = {}
        for old, new, expected_count in MATH_TEXT_NORMALIZATIONS:
            count = sum(span.count(old) for span in target_math)
            if count > expected_count:
                raise RuntimeError(f"Unexpected {label} math-text normalization count: {old}: {count}")
            normalization_totals[old] += count
            applied[f"{old}->{new}"] = count
            target_math = [span.replace(old, new) for span in target_math]
        if source_controls != target_controls:
            first = next(
                (
                    i
                    for i, pair in enumerate(zip(source_controls, target_controls))
                    if pair[0] != pair[1]
                ),
                min(len(source_controls), len(target_controls)),
            )
            raise RuntimeError(
                f"{label} TeX control stream differs: source={len(source_controls)}, "
                f"target={len(target_controls)}, first={first}, "
                f"source_token={source_controls[first:first+3]}, "
                f"target_token={target_controls[first:first+3]}"
            )
        if source_env != target_env:
            raise RuntimeError(f"{label} environment action stream differs")
        if source_math != target_math:
            mismatches = [i for i, pair in enumerate(zip(source_math, target_math)) if pair[0] != pair[1]]
            raise RuntimeError(f"{label} normalized math stream differs at {mismatches[:10]}")
        segment_results.append(
            {
                "segment": label,
                "controls": len(source_controls),
                "source_linebreak_controls": source_controls_raw.count("\\\\"),
                "target_linebreak_controls": target_controls_raw.count("\\\\"),
                "environments": len(source_env),
                "math_spans": len(source_math),
                "delimited_math_spans": len(source_delimited_math),
                "environment_math_spans": len(source_environment_math),
                "math_text_normalizations": applied,
                "all_streams_equal_after_declared_target_language_text_normalization": True,
            }
        )

    for old, _new, expected_count in MATH_TEXT_NORMALIZATIONS:
        if normalization_totals[old] != expected_count:
            raise RuntimeError(
                f"Whole-body math-text normalization count differs for {old}: "
                f"{normalization_totals[old]} != {expected_count}"
            )

    preamble = (ROOT / "segments" / "P08_STANDALONE_PREAMBLE.tex").read_text(encoding="utf-8")
    postamble = (ROOT / "segments" / "P08_STANDALONE_POSTAMBLE.tex").read_text(encoding="utf-8")
    hans = (ROOT / "zh-Hans-CN" / "hans.tex").read_text(encoding="utf-8")
    hant = (ROOT / "zh-Hant-controlled" / "hant.tex").read_text(encoding="utf-8")
    if hans != preamble + target_all + postamble:
        raise RuntimeError("Final Hans is not the exact declared assembly")
    if CONTROL.findall(hans) != CONTROL.findall(hant):
        raise RuntimeError("Hans/Hant TeX control streams differ")
    if math_spans(hans) != math_spans(hant):
        raise RuntimeError("Hans/Hant math streams differ")

    evidence = {
        "terms": csv_gate(
            ROOT / "evidence" / "terms.csv",
            15,
            {"sense_window", "lexical_attractor_basin", "mandarin_simplified_dominance_risk_debt"},
        ),
        "adverse": csv_gate(
            ROOT / "evidence" / "adverse.csv",
            13,
            {"trap_or_adverse_reading", "lexical_attractor_basin", "mandarin_simplified_dominance_risk_debt"},
        ),
        "crosswalk": csv_gate(
            ROOT / "evidence" / "crosswalk.csv",
            16,
            {"sense_window", "lexical_attractor_basin", "mandarin_simplified_dominance_risk_debt"},
        ),
    }
    graph = json.loads((ROOT / "evidence" / "graph.json").read_text(encoding="utf-8"))
    nodes = graph.get("nodes", [])
    edges = graph.get("edges", [])
    node_ids = {node["id"] for node in nodes}
    dangling = [edge["id"] for edge in edges if edge["from"] not in node_ids or edge["to"] not in node_ids]
    if len(nodes) != 140 or len(edges) != 140 or len(node_ids) != 140 or dangling:
        raise RuntimeError("Concept-graph topology gate failed")
    evidence["graph"] = {"nodes": len(nodes), "edges": len(edges), "dangling": len(dangling)}

    record = {
        "schema_version": "1.0.0",
        "record_type": "producer_mechanical_gate",
        "recorded_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "work_id": "NOETHER-P08-ZH",
        "identities": identities,
        "segment_stream_gates": segment_results,
        "whole_target_gate": {
            "exact_declared_hans_assembly": True,
            "hans_hant_tex_controls_equal": True,
            "hans_hant_math_spans_equal": True,
            "source_body_controls": len(CONTROL.findall(source_all)),
            "target_body_controls": len(CONTROL.findall(target_all)),
            "complete_binder_trailing_clearpage_and_footnote_reset_present": (
                "\\clearpage" in postamble and "\\setcounter{footnote}{0}" in postamble
            ),
        },
        "evidence_gates": evidence,
        "all_pass": True,
        "claim_limit": (
            "Producer file identity, declared assembly, TeX/control/math transport, data-shape, "
            "and build-artifact gates only; not source, formula-content, linguistic, visual, "
            "native/regional, human, approval, publication, archive, or certification validation."
        ),
    }
    OUT.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(record, ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
