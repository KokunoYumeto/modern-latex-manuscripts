#!/usr/bin/env python3
"""Produce the P39 v003 controlled-generic Hant integration target.

This is a mechanical producer transformation only.  It performs no linguistic,
source, visual, regional, or publication checking.  The v003 package carries
the accepted v002 Hans bytes unchanged and deterministically integrates the
seven exact Hant corrections frozen by ZHCHK-NOETHER-P39-V002-RETURN-001.
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


HANS = ROOT / "zh-Hans-CN/Noether_Paper39_Chinese_CurrentAuthority_zh-Hans-CN_v003.tex"
HANT_DIR = ROOT / "zh-Hant-controlled"
HANT = HANT_DIR / "Noether_Paper39_Chinese_CurrentAuthority_zh-Hant-controlled_v003.tex"
RECORD = ROOT / "qa/OPENCC_PRODUCER_RECORD_v003.json"
EXPECTED_HANS_SHA256 = "101836C41985DEE9B1A8FCC74A76CD9DF082BE2D07E2A3D45E22BC4DE68C6FE6"
EXPECTED_HANT_SHA256 = "F0E9425763D5E075A5ED1810FE2B1DC2BDAAF6FD48691BE8C3D64F4B158AF1C8"

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
    "% Noether Paper 39 complete zh-Hans-CN translated draft, authority-bound v002.":
        "% Noether Paper 39 controlled-generic zh-Hant translated draft, authority-bound v002.",
    "% Status: translated draft; independent check pending.":
        "% Status: controlled-generic script draft; independent check pending.",
    "爲": "為",
    "裏": "裡",
    "羣": "群",
    "衆": "眾",
    "纔": "才",
    # Exact F001 integration frozen by the independent checker return.
    "超復": "超複",
    "一箇": "一個",
    "着手": "著手",
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

hant_sha = sha(HANT)
if hant_sha != EXPECTED_HANT_SHA256:
    raise RuntimeError(
        f"Hant v003 integration changed: expected {EXPECTED_HANT_SHA256}, found {hant_sha}"
    )

record = {
    "schema_version": "1.0.0",
    "work_id": "NOETHER-P39",
    "producer_version": "v003",
    "authority_binder_id": "NOETH-DE-BINDER-P39-ZH-COMPLETE-20260804-001",
    "authority_pointer_id": "NOETH-DE-AUTH-v006-20260804",
    "operation": "producer_only_hans_to_controlled_generic_hant",
    "input_path": str(HANS),
    "input_sha256": hans_sha,
    "output_path": str(HANT),
    "output_sha256": hant_sha,
    "converter": "opencc-python-reimplemented",
    "converter_version": importlib.metadata.version("opencc-python-reimplemented"),
    "configuration": "s2t",
    "runtime_custody": {
        label: {"path": str(path), "sha256": sha(path)}
        for label, path in RUNTIME_PATHS.items()
    },
    "controlled_normalization_counts": normalization_counts,
    "checker_return_id": "ZHCHK-NOETHER-P39-V002-RETURN-001",
    "integrated_findings": ["ZHCHK-P39-F001"],
    "expected_exact_candidate_sha256": EXPECTED_HANT_SHA256,
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
