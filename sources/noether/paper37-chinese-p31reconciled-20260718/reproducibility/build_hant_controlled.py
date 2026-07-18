#!/usr/bin/env python3
"""Build and audit a controlled generic, explicitly non-localized Hant derivative."""

from collections import Counter
from pathlib import Path
import difflib
import hashlib
import importlib.metadata
import json
import os
import re
import shutil
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT.parents[4]
VENDORED = PROJECT / "tmp/tools/opencc_py"
sys.path.insert(0, str(VENDORED))

from opencc import OpenCC  # type: ignore  # vendored and hash-pinned below


OPENCC_METADATA = VENDORED / "opencc_python_reimplemented-0.1.7.dist-info/METADATA"
OPENCC_CONFIG = VENDORED / "opencc/config/s2t.json"
OPENCC_ST_PHRASES = VENDORED / "opencc/dictionary/STPhrases.txt"
OPENCC_ST_CHARACTERS = VENDORED / "opencc/dictionary/STCharacters.txt"

HANS = ROOT / "zh-Hans-CN/Noether_Paper37_Chinese_P31Reconciled_zh-Hans-CN_v001.tex"
HANT_DIR = ROOT / "zh-Hant-controlled"
HANT = HANT_DIR / "Noether_Paper37_Chinese_P31Reconciled_zh-Hant-controlled_v001.tex"
PDF = HANT.with_suffix(".pdf")
LOG = HANT.with_suffix(".log")
AUX = HANT.with_suffix(".aux")
RENDER_DIR = ROOT / "renders/zh-Hant-controlled_final-candidate_v001"
CONVERSION_REPORT = ROOT / "qa/OPENCC_CONVERSION_RECORD.json"
DIFF_REPORT = ROOT / "qa/HANS_HANT_SCRIPT_DIFF_REPORT.json"

EXPECTED_HANS_SHA256 = "A4A0A97E548840915650FE813AED8FC120D2ABE79F3FA76F9ADF35D5EDAB1B0C"
EXPECTED_RUNTIME_HASHES = {
    "metadata": "0DA812FD9236BE4F841553350A64DCF76F84DD580DE99320B6E3030C1B9C7A4B",
    "config": "246F559AAF3756B280157F4EB2AB1DD22F31EBAC2A9E0AAFA2B4A99C1CB676CE",
    "st_phrases": "A4DE4D2471F73CDB7E5B1B22920139AA4E4BBB1EBEEA8F1FC341F988AA75C586",
    "st_characters": "9207708DA9F2E2A248F39C457B2FCCAD26EC42E7EFAF47A860E6900464F4CAC5",
}


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def math_spans(text: str) -> list[str]:
    spans: list[str] = []
    pattern = r"(?<!\\)\$(.*?)(?<!\\)\$|(?<!\\)\\\[(.*?)\\\]"
    for match in re.finditer(pattern, text, re.S):
        value = match.group(1) if match.group(1) is not None else match.group(2)
        spans.append(value.strip())
    return spans


def math_non_cjk_skeleton(text: str) -> str:
    """Remove script-bearing CJK glyphs while preserving all TeX and math tokens."""
    return re.sub(r"[\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF]", "", text)


def tex_control_tokens(text: str) -> list[str]:
    return re.findall(r"\\(?:[A-Za-z@]+|.)", text)


def environment_tokens(text: str) -> list[str]:
    return re.findall(r"\\(?:begin|end)\{[^{}]+\}", text)


def locate_executable(name: str) -> Path:
    local_app_data = os.environ.get("LOCALAPPDATA")
    candidates: list[Path] = []
    if local_app_data:
        candidates.append(
            Path(local_app_data) / "Programs/MiKTeX/miktex/bin/x64" / f"{name}.exe"
        )
    found = shutil.which(name)
    if found:
        candidates.append(Path(found))
    for candidate in candidates:
        if candidate.is_file():
            return candidate.resolve()
    raise FileNotFoundError(f"Required executable not found: {name}")


def run_checked(command: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        command,
        cwd=cwd,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if result.returncode != 0:
        tail = result.stdout[-4000:]
        raise RuntimeError(
            f"Command failed with exit code {result.returncode}: {command!r}\n{tail}"
        )
    return result


def log_count(pattern: str, text: str) -> int:
    return len(re.findall(pattern, text, re.I | re.M))


runtime_paths = {
    "metadata": OPENCC_METADATA,
    "config": OPENCC_CONFIG,
    "st_phrases": OPENCC_ST_PHRASES,
    "st_characters": OPENCC_ST_CHARACTERS,
}
runtime_hashes = {label: sha(path) for label, path in runtime_paths.items()}
runtime_hash_checks = {
    label: runtime_hashes[label] == expected
    for label, expected in EXPECTED_RUNTIME_HASHES.items()
}
if not all(runtime_hash_checks.values()):
    raise RuntimeError(f"Vendored OpenCC custody mismatch: {runtime_hash_checks}")

hans_bytes = HANS.read_bytes()
hans_sha256 = sha_bytes(hans_bytes)
if hans_sha256 != EXPECTED_HANS_SHA256:
    raise RuntimeError(
        f"Hans input changed: expected {EXPECTED_HANS_SHA256}, found {hans_sha256}"
    )
hans = hans_bytes.decode("utf-8")

cc = OpenCC("s2t")
raw = cc.convert(hans)

normalizations = {
    "Microsoft YaHei": "Microsoft JhengHei",
    # JhengHei's line metrics otherwise leave only the receipt line on a fifth
    # page. These bounded layout adjustments retain the Hans TeX structure.
    "margin=2.15cm": "margin=2.10cm",
    "\\setlength{\\parskip}{0.30em}": "\\setlength{\\parskip}{0.25em}",
    "% Complete zh-Hans-CN reconciliation candidate of Noether Paper 37.":
        "% Controlled generic zh-Hant reconciliation of Noether Paper 37.",
    "% The inherited Chinese text is translation/adverse witness material only.":
        "% Mechanical base: declared OpenCC 0.1.7 s2t from the audited Hans TeX.\n"
        "% Controlled generic Traditional script only; not Taiwan-, Hong Kong-, or Macao-localized prose.\n"
        "% No external, regional, or human validation is claimed.",
    "爲": "為",
    "裏": "裡",
    "羣": "群",
    "衆": "眾",
    "纔": "才",
    # OpenCC's second s2t pass changes the aspect particle in this exact
    # P37 phrase from 了 to 瞭 after the surrounding characters are already
    # Traditional. Keep the grammatical particle and make the declared full
    # conversion pipeline stable without globally collapsing lexical 瞭.
    "證明瞭主理想性質": "證明了主理想性質",
}
required_anchor_counts = {
    "Microsoft YaHei->Microsoft JhengHei": 2,
    "margin=2.15cm->margin=2.10cm": 1,
    "\\setlength{\\parskip}{0.30em}->\\setlength{\\parskip}{0.25em}": 1,
    "% Complete zh-Hans-CN reconciliation candidate of Noether Paper 37.->% Controlled generic zh-Hant reconciliation of Noether Paper 37.": 1,
    "% The inherited Chinese text is translation/adverse witness material only.->% Mechanical base: declared OpenCC 0.1.7 s2t from the audited Hans TeX.\n% Controlled generic Traditional script only; not Taiwan-, Hong Kong-, or Macao-localized prose.\n% No external, regional, or human validation is claimed.": 1,
}

hant = raw
normalization_counts: dict[str, int] = {}
for old, new in normalizations.items():
    key = f"{old}->{new}"
    count = hant.count(old)
    normalization_counts[key] = count
    hant = hant.replace(old, new)

anchor_count_checks = {
    key: normalization_counts.get(key) == expected
    for key, expected in required_anchor_counts.items()
}

HANT_DIR.mkdir(parents=True, exist_ok=True)
HANT.write_text(hant, encoding="utf-8", newline="\n")

hans_math = math_spans(hans)
hant_math = math_spans(hant)
hans_math_skeletons = [math_non_cjk_skeleton(span) for span in hans_math]
hant_math_skeletons = [math_non_cjk_skeleton(span) for span in hant_math]
math_script_changes = [
    {"index": index, "hans": before, "hant": after}
    for index, (before, after) in enumerate(zip(hans_math, hant_math))
    if before != after
]

prohibited = ["爲", "裏", "羣", "衆", "纔"]
hans_controls = tex_control_tokens(hans)
hant_controls = tex_control_tokens(hant)
hans_environments = environment_tokens(hans)
hant_environments = environment_tokens(hant)
display_open_hans = len(re.findall(r"(?<!\\)\\\[", hans))
display_open_hant = len(re.findall(r"(?<!\\)\\\[", hant))
display_close_hans = len(re.findall(r"(?<!\\)\\\]", hans))
display_close_hant = len(re.findall(r"(?<!\\)\\\]", hant))

normalization_idempotent = hant
for old, new in normalizations.items():
    normalization_idempotent = normalization_idempotent.replace(old, new)


def declared_conversion_pipeline(text: str) -> str:
    converted = cc.convert(text)
    for old, new in normalizations.items():
        converted = converted.replace(old, new)
    return converted


second_raw = cc.convert(hant)
second_raw_divergences = Counter()
for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(
    a=hant, b=second_raw, autojunk=False
).get_opcodes():
    if tag != "equal":
        second_raw_divergences[f"{hant[i1:i2]}->{second_raw[j1:j2]}"] += 1

script_checks = {
    "input_hash_matches_pinned_hans": sha(HANS) == EXPECTED_HANS_SHA256,
    "vendored_opencc_hashes_match": all(runtime_hash_checks.values()),
    "required_controlled_normalization_anchors_match": all(anchor_count_checks.values()),
    "ordered_math_span_counts_match": len(hans_math) == len(hant_math),
    "ordered_math_non_cjk_skeletons_identical": hans_math_skeletons == hant_math_skeletons,
    "tex_control_tokens_identical": hans_controls == hant_controls,
    "environment_tokens_identical": hans_environments == hant_environments,
    "brace_counts_match_and_balance": (
        hans.count("{") == hans.count("}") == hant.count("{") == hant.count("}")
    ),
    "dollar_counts_match_and_are_even": (
        hans.count("$") == hant.count("$") and hans.count("$") % 2 == 0
    ),
    "display_delimiters_match_and_balance": (
        display_open_hans
        == display_close_hans
        == display_open_hant
        == display_close_hant
    ),
    "declared_s2t_plus_controlled_normalizations_idempotent": (
        declared_conversion_pipeline(hant) == hant
    ),
    "controlled_normalizations_idempotent": normalization_idempotent == hant,
    "prohibited_variant_counts_zero": not any(hant.count(value) for value in prohibited),
    "font_profile_switched": (
        hant.count("Microsoft JhengHei") == 2 and "Microsoft YaHei" not in hant
    ),
    "generic_nonlocalized_label_present": (
        "Controlled generic Traditional script only" in hant
        and "not Taiwan-, Hong Kong-, or Macao-localized prose" in hant
        and "No external, regional, or human validation is claimed" in hant
    ),
}
script_status = "pass" if all(script_checks.values()) else "fail"

conversion = {
    "schema_version": "1.1.0",
    "work_id": "NOETHER-P37",
    "input_path": str(HANS),
    "input_sha256": sha(HANS),
    "output_path": str(HANT),
    "output_sha256": sha(HANT),
    "converter": "opencc-python-reimplemented",
    "converter_version": importlib.metadata.version("opencc-python-reimplemented"),
    "configuration": "s2t",
    "vendored_module_path": str(VENDORED / "opencc"),
    "runtime_custody": {
        "metadata_path": str(OPENCC_METADATA),
        "metadata_sha256": runtime_hashes["metadata"],
        "config_path": str(OPENCC_CONFIG),
        "config_sha256": runtime_hashes["config"],
        "st_phrases_path": str(OPENCC_ST_PHRASES),
        "st_phrases_sha256": runtime_hashes["st_phrases"],
        "st_characters_path": str(OPENCC_ST_CHARACTERS),
        "st_characters_sha256": runtime_hashes["st_characters"],
        "hash_checks": runtime_hash_checks,
    },
    "controlled_normalizations": normalization_counts,
    "required_anchor_count_checks": anchor_count_checks,
    "localization_status": (
        "controlled generic Traditional script; explicitly not zh-Hant-TW/HK/MO"
    ),
    "external_or_human_validation": "none",
}
CONVERSION_REPORT.write_text(
    json.dumps(conversion, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)

matcher = difflib.SequenceMatcher(a=hans, b=hant, autojunk=False)
opcodes = Counter(tag for tag, *_ in matcher.get_opcodes())

report = {
    "schema_version": "1.1.0",
    "work_id": "NOETHER-P37",
    "input_sha256": sha(HANS),
    "output_sha256": sha(HANT),
    "input_characters": len(hans),
    "output_characters": len(hant),
    "sequence_match_ratio": matcher.ratio(),
    "opcode_counts": dict(opcodes),
    "ordered_math_span_count_hans": len(hans_math),
    "ordered_math_span_count_hant": len(hant_math),
    "ordered_math_raw_identical_count": sum(
        before == after for before, after in zip(hans_math, hant_math)
    ),
    "ordered_math_script_change_count": len(math_script_changes),
    "ordered_math_script_changes": math_script_changes,
    "ordered_math_non_cjk_skeletons_identical": (
        hans_math_skeletons == hant_math_skeletons
    ),
    "tex_control_token_count_hans": len(hans_controls),
    "tex_control_token_count_hant": len(hant_controls),
    "tex_control_tokens_identical": hans_controls == hant_controls,
    "environment_token_count_hans": len(hans_environments),
    "environment_token_count_hant": len(hant_environments),
    "environment_tokens_identical": hans_environments == hant_environments,
    "brace_counts": {
        "hans_open": hans.count("{"),
        "hans_close": hans.count("}"),
        "hant_open": hant.count("{"),
        "hant_close": hant.count("}"),
    },
    "dollar_counts": {"hans": hans.count("$"), "hant": hant.count("$")},
    "display_delimiter_counts": {
        "hans_open": display_open_hans,
        "hans_close": display_close_hans,
        "hant_open": display_open_hant,
        "hant_close": display_close_hant,
    },
    "prohibited_variant_counts": {value: hant.count(value) for value in prohibited},
    "raw_s2t_second_pass_idempotent": second_raw == hant,
    "raw_s2t_second_pass_divergence_counts": dict(second_raw_divergences),
    "script_integrity_checks": script_checks,
    "script_integrity_status": script_status,
    "status_scope": (
        "computational Hans-to-Hant script/TeX integrity only; not regional prose "
        "suitability or external validation"
    ),
    "review_limits": (
        "Two math spans contain CJK hbox prose; one has an expected Hans-to-Hant "
        "script change and one is already script-invariant. All "
        "ordered non-CJK math and TeX skeletons must remain identical. Regional "
        "prose suitability and human comprehension are not tested or claimed."
    ),
}

if script_status != "pass":
    report["status"] = "fail"
    DIFF_REPORT.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    raise RuntimeError(f"Script integrity checks failed: {script_checks}")

xelatex = locate_executable("xelatex")
pdftoppm = locate_executable("pdftoppm")
build_passes = []
for pass_number in (1, 2):
    result = run_checked(
        [
            str(xelatex),
            "-interaction=nonstopmode",
            "-halt-on-error",
            HANT.name,
        ],
        cwd=HANT_DIR,
    )
    build_passes.append(
        {
            "pass": pass_number,
            "return_code": result.returncode,
            "console_sha256": sha_bytes(result.stdout.encode("utf-8")),
        }
    )

if not (PDF.is_file() and LOG.is_file() and AUX.is_file()):
    raise RuntimeError("XeLaTeX did not produce the expected PDF, log, and aux files")

log_text = LOG.read_text(encoding="utf-8", errors="replace")
log_findings = {
    "latex_warning_count": log_count(r"LaTeX Warning:", log_text),
    "package_warning_count": log_count(r"Package\s+\S+\s+Warning:", log_text),
    "font_warning_count": log_count(r"(?:fontspec|LaTeX Font)\s+Warning", log_text),
    "overfull_box_count": log_count(r"Overfull \\[hv]box", log_text),
    "underfull_box_count": log_count(r"Underfull \\[hv]box", log_text),
    "missing_character_count": log_count(r"Missing character:", log_text),
    "undefined_control_count": log_count(r"Undefined control sequence", log_text),
    "fatal_error_count": log_count(r"Fatal error|Emergency stop", log_text),
    "rerun_warning_count": log_count(r"Rerun to get|Label\(s\) may have changed", log_text),
}
log_clean = not any(log_findings.values())
if not log_clean:
    raise RuntimeError(f"Final XeLaTeX log is not clean: {log_findings}")

RENDER_DIR.mkdir(parents=True, exist_ok=True)
for old_page in RENDER_DIR.glob("page-*.png"):
    old_page.unlink()
run_checked(
    [str(pdftoppm), "-png", "-r", "180", str(PDF), str(RENDER_DIR / "page")],
    cwd=ROOT,
)
render_pages = sorted(
    RENDER_DIR.glob("page-*.png"),
    key=lambda path: int(path.stem.split("-")[-1]),
)
if not render_pages:
    raise RuntimeError("No rendered PNG pages were produced")

build_checks = {
    "two_halt_on_error_passes_succeeded": (
        len(build_passes) == 2 and all(item["return_code"] == 0 for item in build_passes)
    ),
    "expected_pdf_log_aux_exist": PDF.is_file() and LOG.is_file() and AUX.is_file(),
    "final_log_clean": log_clean,
    "render_pages_present": bool(render_pages),
}
build_status = "pass" if all(build_checks.values()) else "fail"

report["build"] = {
    "xelatex_path": str(xelatex),
    "pdftoppm_path": str(pdftoppm),
    "passes": build_passes,
    "pdf_path": str(PDF),
    "pdf_sha256": sha(PDF),
    "log_path": str(LOG),
    "log_sha256": sha(LOG),
    "aux_path": str(AUX),
    "aux_sha256": sha(AUX),
    "log_findings": log_findings,
    "page_count_from_render_set": len(render_pages),
    "render_dpi": 180,
    "render_directory": str(RENDER_DIR),
    "render_pages": [
        {"path": str(path), "sha256": sha(path), "bytes": path.stat().st_size}
        for path in render_pages
    ],
    "build_checks": build_checks,
    "build_status": build_status,
}
report["status"] = "pass" if script_status == build_status == "pass" else "fail"
DIFF_REPORT.write_text(
    json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)

print(
    json.dumps(
        {
            "conversion": conversion,
            "script_integrity_status": script_status,
            "build_status": build_status,
            "page_count": len(render_pages),
            "pdf_sha256": sha(PDF),
            "log_findings": log_findings,
            "status": report["status"],
        },
        ensure_ascii=True,
        indent=2,
    )
)
raise SystemExit(0 if report["status"] == "pass" else 1)
