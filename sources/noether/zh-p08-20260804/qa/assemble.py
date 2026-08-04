#!/usr/bin/env python3
"""Assemble the P08 zh-Hans-CN producer target from hash-pinned units."""

from __future__ import annotations

from datetime import datetime
from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "zh-Hans-CN" / "hans.tex"
RECORD = ROOT / "qa" / "assemble.json"

PARTS = [
    (
        ROOT / "segments" / "P08_STANDALONE_PREAMBLE.tex",
        1418,
        "D26F563802B60116A2B8B09E6175807F5B2445A38298579DB39DE6993A5A1119",
        "producer preamble",
    ),
    (
        ROOT
        / "segments"
        / "zh-Hans-CN"
        / "assembly_normalized"
        / "P08_S01_INTRO_I_zh-Hans-CN_assembly_v001.tex",
        5310,
        "08038923D412BD6452BC0F79A7D6527277D023F253FB56B28D44096289C45652",
        "S01 normalized producer translation",
    ),
    (
        ROOT / "segments" / "zh-Hans-CN" / "P08_S02_II_zh-Hans-CN_v001.tex",
        11536,
        "F0088AAB791F84B1033CD502046DC2BC7175AABFC113ADC44ABD97BDEFE618EA",
        "S02 worker translation",
    ),
    (
        ROOT
        / "segments"
        / "zh-Hans-CN"
        / "assembly_normalized"
        / "P08_S03_III_zh-Hans-CN_assembly_v001.tex",
        6723,
        "8C35C68B76146875575196C7BB2E0506F931DDAC0C08D085F00BD58772F5E54E",
        "S03 normalized producer translation",
    ),
    (
        ROOT / "segments" / "P08_STANDALONE_POSTAMBLE.tex",
        54,
        "82205E7D6205BB5B565E7F72345F9FB252586B17F6A5A164B6B368B212DA845C",
        "producer postamble with complete-binder trailing controls",
    ),
]


def digest(data: bytes) -> str:
    return sha256(data).hexdigest().upper()


def main() -> int:
    if OUT.exists() or RECORD.exists():
        raise RuntimeError(f"Refusing to overwrite assembled output: {OUT}; {RECORD}")

    payloads: list[bytes] = []
    members: list[dict[str, object]] = []
    for path, expected_bytes, expected_sha, role in PARTS:
        data = path.read_bytes()
        observed = (len(data), digest(data))
        expected = (expected_bytes, expected_sha)
        if observed != expected:
            raise RuntimeError(f"Identity mismatch for {role}: {observed} != {expected}")
        payloads.append(data)
        members.append(
            {
                "role": role,
                "path": str(path),
                "bytes": len(data),
                "sha256": digest(data),
            }
        )

    assembled = b"".join(payloads)
    text = assembled.decode("utf-8")
    gates = {
        "documentclass_count": text.count("\\documentclass"),
        "begin_document_count": text.count("\\begin{document}"),
        "end_document_count": text.count("\\end{document}"),
        "paper08_section_count": text.count("\\section*{8."),
        "subsection_i_count": text.count("\\subsection*{I."),
        "subsection_ii_count": text.count("\\subsection*{II."),
        "subsection_iii_count": text.count("\\subsection*{III."),
        "clearpage_count": text.count("\\clearpage"),
        "footnote_reset_count": text.count("\\setcounter{footnote}{0}"),
    }
    expected_gates = {
        "documentclass_count": 1,
        "begin_document_count": 1,
        "end_document_count": 1,
        "paper08_section_count": 1,
        "subsection_i_count": 1,
        "subsection_ii_count": 1,
        "subsection_iii_count": 1,
        "clearpage_count": 1,
        "footnote_reset_count": 2,
    }
    if gates != expected_gates:
        raise RuntimeError(f"Assembly structural gate failed: {gates}")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_bytes(assembled)
    output = {
        "path": str(OUT),
        "bytes": len(assembled),
        "sha256": digest(assembled),
    }
    record = {
        "schema_version": "1.0.0",
        "record_type": "producer_hans_assembly",
        "recorded_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "work_id": "NOETHER-P08-ZH",
        "authority_binder": "NOETH-DE-BINDER-P08-ZH-COMPLETE-20260804-001",
        "authority_lf_sha256": "7E5EEBEB8F569F101490D8262072027C876C8102D2841A2A57F96E0DC2708E71",
        "members": members,
        "operation": "exact byte concatenation in listed order",
        "structural_gates": gates,
        "output": output,
        "translation_state": "producer translation complete; independent check pending",
        "epistemic_boundary": {
            "source_or_scan_check_performed": False,
            "independent_target_check_performed": False,
            "visual_check_performed": False,
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
