#!/usr/bin/env python3
"""Mechanically produce corrected controlled-generic Hant v002 from Hans v002."""

from pathlib import Path
import hashlib
import importlib.metadata
import json
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT.parents[4]
VENDORED = PROJECT / "tmp/tools/opencc_py"
sys.path.insert(0, str(VENDORED))

from opencc import OpenCC  # type: ignore


HANS = ROOT / "build/zh-Hans-CN-v002/Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_v002.tex"
ASSEMBLY_RECORD = ROOT / "controls/HANS_ASSEMBLY_RECORD_v002.json"
HANT_DIR = ROOT / "build/zh-Hant-controlled-v002"
HANT = HANT_DIR / "Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_v002.tex"
RECORD = ROOT / "controls/OPENCC_PRODUCER_RECORD_v002.json"
SCRIPT = Path(__file__).resolve()

RUNTIME_PATHS = {
    "metadata": VENDORED / "opencc_python_reimplemented-0.1.7.dist-info/METADATA",
    "config": VENDORED / "opencc/config/s2t.json",
    "st_phrases": VENDORED / "opencc/dictionary/STPhrases.txt",
    "st_characters": VENDORED / "opencc/dictionary/STCharacters.txt",
}

MATH_PATTERN = re.compile(
    r"(?s)"
    r"(\\\[.*?\\\]|\\\(.*?\\\)|\$\$.*?\$\$|(?<!\\)\$(?!\$).*?(?<!\\)\$|"
    r"\\begin\{(?:equation\*?|align\*?|aligned|gather\*?|multline\*?|array|cases|matrix|pmatrix|bmatrix|vmatrix|Vmatrix)\}.*?"
    r"\\end\{(?:equation\*?|align\*?|aligned|gather\*?|multline\*?|array|cases|matrix|pmatrix|bmatrix|vmatrix|Vmatrix)\})"
)
CONTROL_SEQUENCE_PATTERN = re.compile(r"\\(?:[A-Za-z@]+|.)")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


assembly = json.loads(ASSEMBLY_RECORD.read_text(encoding="utf-8"))
hans_sha = sha(HANS)
if hans_sha != assembly["output"]["sha256"]:
    raise RuntimeError(
        f"Hans/assembly mismatch: expected {assembly['output']['sha256']}, found {hans_sha}"
    )

hans = HANS.read_text(encoding="utf-8")
converter = OpenCC("s2t")
converted: list[str] = []
cursor = 0
for match in MATH_PATTERN.finditer(hans):
    converted.append(converter.convert(hans[cursor:match.start()]))
    converted.append(match.group(0))
    cursor = match.end()
converted.append(converter.convert(hans[cursor:]))
raw_hant = "".join(converted)
hant = raw_hant

normalizations = {
    "Microsoft YaHei": "Microsoft JhengHei",
    "% Noether Paper 35 corrected zh-Hans-CN producer revision 2.":
        "% Noether Paper 35 corrected controlled-generic zh-Hant producer revision 2.",
    "% Exact checker-frozen target corrections integrated; independent recheck pending.":
        "% Controlled-generic script transport of corrected Hans; independent recheck pending.",
    "爲": "為",
    "裏": "裡",
    "羣": "群",
    "衆": "眾",
    "纔": "才",
    "這隻會": "這只會",
    "幷": "並",
    "代數無關係統": "代數無關系統",
}
normalization_counts: dict[str, int] = {}
for old, new in normalizations.items():
    normalization_counts[f"{old}->{new}"] = hant.count(old)
    hant = hant.replace(old, new)

claim_marker = "% Controlled-generic script transport of corrected Hans; independent recheck pending."
claim_replacement = (
    claim_marker
    + "\n% Controlled generic Traditional script only; not zh-Hant-TW/HK/MO prose."
    + "\n% Corrected Hans wording remains the lexical base; independent Hant recheck is pending."
)
if hant.count(claim_marker) != 1:
    raise RuntimeError("Expected exactly one producer claim-limit marker")
hant = hant.replace(claim_marker, claim_replacement, 1)

# Mechanical transport invariants only; these are not formula-content checks.
hans_math = MATH_PATTERN.findall(hans)
hant_math = MATH_PATTERN.findall(hant)
if hans_math != hant_math:
    raise RuntimeError("Math spans changed during script transport")
hans_controls = CONTROL_SEQUENCE_PATTERN.findall(hans)
hant_controls = CONTROL_SEQUENCE_PATTERN.findall(hant)
if hans_controls != hant_controls:
    raise RuntimeError("TeX control-sequence stream changed during script transport")

HANT_DIR.mkdir(parents=True, exist_ok=True)
HANT.write_text(hant, encoding="utf-8", newline="\n")
record = {
    "schema_version": "1.0.0",
    "work_id": "NOETHER-P35-ZH",
    "operation": "producer_only_corrected_hans_to_controlled_generic_hant_v002",
    "decision_id": "ZH-D131",
    "checker_findings_applied": ["ZHCHK-P35-F012", "ZHCHK-P35-F014"],
    "producer_script_path": str(SCRIPT),
    "producer_script_sha256": sha(SCRIPT),
    "input_path": str(HANS),
    "input_bytes": len(HANS.read_bytes()),
    "input_sha256": hans_sha,
    "assembly_record_path": str(ASSEMBLY_RECORD),
    "assembly_record_sha256": sha(ASSEMBLY_RECORD),
    "raw_opencc_output_utf8_bytes": len(raw_hant.encode("utf-8")),
    "raw_opencc_output_utf8_sha256": sha_bytes(raw_hant.encode("utf-8")),
    "output_path": str(HANT),
    "output_bytes": len(HANT.read_bytes()),
    "output_sha256": sha(HANT),
    "converter": "opencc-python-reimplemented",
    "converter_version": importlib.metadata.version("opencc-python-reimplemented"),
    "configuration": "s2t",
    "runtime_custody": {
        label: {"path": str(path), "sha256": sha(path)}
        for label, path in RUNTIME_PATHS.items()
    },
    "controlled_normalization_counts": normalization_counts,
    "mechanical_invariants": {
        "math_spans_compared": len(hans_math),
        "math_spans_protected_from_script_conversion": True,
        "math_spans_unchanged": True,
        "tex_control_sequences_compared": len(hans_controls),
        "tex_control_sequence_stream_unchanged": True
    },
    "localization_status": "controlled generic zh-Hant only",
    "explicitly_not": ["zh-Hant-TW", "zh-Hant-HK", "zh-Hant-MO"],
    "lexical_base": "zh-Hans-CN producer translation",
    "review_state": "independent recheck pending",
    "claim_limit": (
        "Mechanical script transformation, structural invariants, compilation, and file custody only; "
        "no linguistic, source, semantic, apparatus, formula-content, terminology, visual, regional, "
        "human, external, archive, publication, approval, or certification validation."
    )
}
RECORD.write_text(
    json.dumps(record, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
    newline="\n",
)
print(json.dumps(record, ensure_ascii=True, indent=2))
