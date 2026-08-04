#!/usr/bin/env python3
"""Produce controlled-generic Hant from the frozen Paper 36 Hans producer file."""

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


HANS = ROOT / "zh-Hans-CN/Noether_Paper36_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex"
HANT_DIR = ROOT / "zh-Hant-controlled"
HANT = HANT_DIR / "Noether_Paper36_Chinese_CurrentAuthority_zh-Hant-controlled_v001.tex"
RECORD = ROOT / "qa/OPENCC_PRODUCER_RECORD.json"
EXPECTED_HANS_SHA256 = "928C90ED8A02FA9F5BAA5E891CE780CCFF76878BB86515D84F7064E8998E6416"

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

hant = OpenCC("s2t").convert(HANS.read_text(encoding="utf-8"))
normalizations = {
    "Microsoft YaHei": "Microsoft JhengHei",
    "% Noether Paper 36 complete zh-Hans-CN translated producer draft.": "% Noether Paper 36 controlled-generic zh-Hant producer draft.",
    "% Status: translated producer draft; independent check pending.": "% Status: controlled-generic script draft; independent check pending.",
    "爲": "為",
    "裏": "裡",
    "羣": "群",
    "衆": "眾",
    "纔": "才",
}
counts = {}
for old, new in normalizations.items():
    counts[f"{old}->{new}"] = hant.count(old)
    hant = hant.replace(old, new)

status_marker = "% Status: controlled-generic script draft; independent check pending."
claim_limit = (
    status_marker
    + "\n% Controlled generic Traditional script only; not zh-Hant-TW/HK/MO prose."
    + "\n% Hans wording remains the lexical base; independent Hant checking is pending."
    + "\n% Compilation is mechanical production only. No source, apparatus, semantic,"
    + "\n% formula, terminology, visual, regional, publication, or certification check is claimed."
)
if status_marker not in hant:
    raise RuntimeError("Producer status marker missing")
hant = hant.replace(status_marker, claim_limit, 1)

HANT_DIR.mkdir(parents=True, exist_ok=True)
HANT.write_text(hant, encoding="utf-8", newline="\n")
record = {
    "schema_version": "1.0.0",
    "work_id": "NOETHER-P36",
    "operation": "producer_only_hans_to_controlled_generic_hant",
    "input_path": str(HANS),
    "input_sha256": hans_sha,
    "expected_input_sha256": EXPECTED_HANS_SHA256,
    "output_path": str(HANT),
    "output_sha256": sha(HANT),
    "converter": "opencc-python-reimplemented",
    "converter_version": importlib.metadata.version("opencc-python-reimplemented"),
    "configuration": "s2t",
    "runtime_custody": {
        label: {"path": str(path), "sha256": sha(path)}
        for label, path in RUNTIME_PATHS.items()
    },
    "controlled_normalization_counts": counts,
    "localization_status": "controlled generic zh-Hant only",
    "explicitly_not": ["zh-Hant-TW", "zh-Hant-HK", "zh-Hant-MO"],
    "lexical_base": "zh-Hans-CN producer draft",
    "review_state": "independent check pending",
    "claim_limit": "Mechanical script transformation and file custody only; no linguistic, source, apparatus, formula, terminology, visual, regional, human, external, archive, publication, or certification validation.",
}
RECORD.write_text(
    json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(record, ensure_ascii=True, indent=2))
