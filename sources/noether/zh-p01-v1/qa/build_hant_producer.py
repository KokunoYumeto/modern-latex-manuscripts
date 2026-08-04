#!/usr/bin/env python3
"""Produce controlled-generic Hant from assembled Paper 1 Hans mechanically."""

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


HANS = ROOT / "zh-Hans-CN/Noether_Paper01_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex"
ASSEMBLY_RECORD = ROOT / "qa/HANS_ASSEMBLY_RECORD.json"
HANT_DIR = ROOT / "zh-Hant-controlled"
HANT = HANT_DIR / "Noether_Paper01_Chinese_CurrentAuthority_zh-Hant-controlled_v001.tex"
RECORD = ROOT / "qa/OPENCC_PRODUCER_RECORD.json"

RUNTIME_PATHS = {
    "metadata": VENDORED / "opencc_python_reimplemented-0.1.7.dist-info/METADATA",
    "config": VENDORED / "opencc/config/s2t.json",
    "st_phrases": VENDORED / "opencc/dictionary/STPhrases.txt",
    "st_characters": VENDORED / "opencc/dictionary/STCharacters.txt",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


assembly = json.loads(ASSEMBLY_RECORD.read_text(encoding="utf-8"))
expected_hans_sha = assembly["output_sha256"]
hans_sha = sha(HANS)
if hans_sha != expected_hans_sha:
    raise RuntimeError(f"Hans producer file changed: expected {expected_hans_sha}, found {hans_sha}")

hans = HANS.read_text(encoding="utf-8")
hant = OpenCC("s2t").convert(hans)

normalizations = {
    "Microsoft YaHei": "Microsoft JhengHei",
    "% Noether Paper 1 complete zh-Hans-CN translated producer draft.": "% Noether Paper 1 controlled-generic zh-Hant producer draft.",
    "% Status: translated producer draft; independent check pending.": "% Status: controlled-generic script draft; independent check pending.",
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
    "% Compilation is mechanical production only. No source, semantic, formula,\n"
    "% terminology, visual, regional, publication, or certification check is claimed."
)
replacement = marker + "\n% Controlled generic Traditional script only; not zh-Hant-TW/HK/MO prose.\n% Hans wording remains the lexical base; independent Hant checking is pending."
if marker not in hant:
    raise RuntimeError("Producer claim-limit marker missing")
hant = hant.replace(marker, replacement, 1)

HANT_DIR.mkdir(parents=True, exist_ok=True)
HANT.write_text(hant, encoding="utf-8", newline="\n")

record = {
    "schema_version": "1.0.0",
    "work_id": "NOETHER-P01",
    "operation": "producer_only_hans_to_controlled_generic_hant",
    "input_path": str(HANS),
    "input_sha256": hans_sha,
    "assembly_record_path": str(ASSEMBLY_RECORD),
    "assembly_record_sha256": sha(ASSEMBLY_RECORD),
    "output_path": str(HANT),
    "output_sha256": sha(HANT),
    "converter": "opencc-python-reimplemented",
    "converter_version": importlib.metadata.version("opencc-python-reimplemented"),
    "configuration": "s2t",
    "runtime_custody": {label: {"path": str(path), "sha256": sha(path)} for label, path in RUNTIME_PATHS.items()},
    "controlled_normalization_counts": normalization_counts,
    "localization_status": "controlled generic zh-Hant only",
    "explicitly_not": ["zh-Hant-TW", "zh-Hant-HK", "zh-Hant-MO"],
    "lexical_base": "zh-Hans-CN producer draft",
    "review_state": "independent check pending",
    "claim_limit": "Mechanical script transformation and file custody only; no linguistic, source, formula, terminology, visual, regional, human, external, archive, publication, or certification validation.",
}
RECORD.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(record, ensure_ascii=True, indent=2))
