#!/usr/bin/env python3
"""Produce a controlled-generic Hant draft from the Paper 42 Hans producer file.

This is a mechanical producer transformation only. It performs no linguistic,
source, visual, regional, or publication checking.
"""

from pathlib import Path
import hashlib
import importlib.metadata
import json
import sys


ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT.parents[4]
VENDORED = PROJECT / "tmp/tools/opencc_py"
sys.path.insert(0, str(VENDORED))

from opencc import OpenCC  # type: ignore


HANS = ROOT / "zh-Hans-CN/Noether_Paper42_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex"
HANT_DIR = ROOT / "zh-Hant-controlled"
HANT = HANT_DIR / "Noether_Paper42_Chinese_CurrentAuthority_zh-Hant-controlled_v001.tex"
RECORD = ROOT / "qa/OPENCC_PRODUCER_RECORD.json"
EXPECTED_HANS_SHA256 = "B326FA4696A29D4B6393E85651FDF07EF072C452CAB3BDD93A9BB271285E6625"

RUNTIME_PATHS = {
    "metadata": VENDORED / "opencc_python_reimplemented-0.1.7.dist-info/METADATA",
    "config": VENDORED / "opencc/config/s2t.json",
    "st_phrases": VENDORED / "opencc/dictionary/STPhrases.txt",
    "st_characters": VENDORED / "opencc/dictionary/STCharacters.txt",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


hans_sha = sha(HANS)
if hans_sha != EXPECTED_HANS_SHA256:
    raise RuntimeError(
        f"Hans producer file changed: expected {EXPECTED_HANS_SHA256}, found {hans_sha}"
    )

hans = HANS.read_text(encoding="utf-8")
hant = OpenCC("s2t").convert(hans)

normalizations = {
    "Microsoft YaHei": "Microsoft JhengHei",
    "% Noether Paper 42 complete zh-Hans-CN translated draft.":
        "% Noether Paper 42 controlled-generic zh-Hant translated draft.",
    "% Status: translated draft; independent check pending.":
        "% Status: controlled-generic script draft; independent check pending.",
    "爲": "為",
    "裏": "裡",
    "羣": "群",
    "衆": "眾",
    "纔": "才",
}

normalization_counts = {}
for old, new in normalizations.items():
    normalization_counts[f"{old}->{new}"] = hant.count(old)
    hant = hant.replace(old, new)

marker = (
    "% Mechanical compilation is recorded separately; no source checking, branch comparison,\n"
    "% visual approval, semantic approval, or publication approval is claimed."
)
replacement = (
    marker
    + "\n% Controlled generic Traditional script only; not zh-Hant-TW/HK/MO prose."
    + "\n% Hans wording remains the lexical base; independent Hant checking is pending."
)
if marker not in hant:
    raise RuntimeError("Producer claim-limit marker missing")
hant = hant.replace(marker, replacement, 1)

HANT_DIR.mkdir(parents=True, exist_ok=True)
HANT.write_text(hant, encoding="utf-8", newline="\n")

record = {
    "schema_version": "1.0.0",
    "work_id": "NOETHER-P42",
    "operation": "producer_only_hans_to_controlled_generic_hant",
    "input_path": str(HANS),
    "input_sha256": hans_sha,
    "output_path": str(HANT),
    "output_sha256": sha(HANT),
    "converter": "opencc-python-reimplemented",
    "converter_version": importlib.metadata.version("opencc-python-reimplemented"),
    "configuration": "s2t",
    "runtime_custody": {
        label: {"path": str(path), "sha256": sha(path)}
        for label, path in RUNTIME_PATHS.items()
    },
    "controlled_normalization_counts": normalization_counts,
    "localization_status": "controlled generic zh-Hant only",
    "explicitly_not": ["zh-Hant-TW", "zh-Hant-HK", "zh-Hant-MO"],
    "lexical_base": "zh-Hans-CN producer draft",
    "review_state": "independent check pending",
    "claim_limit": (
        "Mechanical script transformation and file custody only; no linguistic, "
        "source, visual, regional, human, external, or publication validation."
    ),
}
RECORD.write_text(
    json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(record, ensure_ascii=True, indent=2))
