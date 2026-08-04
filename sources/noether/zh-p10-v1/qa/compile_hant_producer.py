#!/usr/bin/env python3
"""Run exactly two producer-only XeLaTeX passes for Paper 10 controlled Hant."""

from pathlib import Path
import hashlib
import json
import re
import shutil
import subprocess


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = Path(__file__).resolve()
HANT_DIR = ROOT / "zh-Hant-controlled"
TEX = HANT_DIR / "Noether_Paper10_Chinese_CurrentAuthority_zh-Hant-controlled_v001.tex"
OPENCC_RECORD = ROOT / "qa/OPENCC_PRODUCER_RECORD.json"
BUILD_RECORD = ROOT / "qa/HANT_BUILD_RECORD.json"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def bytes_count(path: Path) -> int:
    return len(path.read_bytes())


def warning_counts(text: str) -> dict[str, int]:
    lines = text.splitlines()
    return {
        "warning_token_lines": sum("warning" in line.lower() for line in lines),
        "latex_warning_lines": sum("LaTeX Warning:" in line for line in lines),
        "package_warning_lines": sum(bool(re.search(r"Package .* Warning:", line)) for line in lines),
        "font_warning_lines": sum("Font Warning:" in line for line in lines),
        "overfull_hbox_lines": sum("Overfull \\hbox" in line for line in lines),
        "underfull_hbox_lines": sum("Underfull \\hbox" in line for line in lines),
        "overfull_vbox_lines": sum("Overfull \\vbox" in line for line in lines),
        "underfull_vbox_lines": sum("Underfull \\vbox" in line for line in lines),
    }


opencc_record = json.loads(OPENCC_RECORD.read_text(encoding="utf-8"))
expected_tex_sha = opencc_record["output_sha256"]
if sha(TEX) != expected_tex_sha:
    raise RuntimeError(f"Hant/OpenCC mismatch: expected {expected_tex_sha}, found {sha(TEX)}")

xelatex_name = shutil.which("xelatex")
if xelatex_name is None:
    raise RuntimeError("xelatex is not available on PATH")
xelatex = Path(xelatex_name).resolve()
version_run = subprocess.run(
    [str(xelatex), "--version"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True
)
version_text = version_run.stdout.decode("utf-8", errors="replace")
command = [
    str(xelatex),
    "-interaction=nonstopmode",
    "-halt-on-error",
    "-file-line-error",
    TEX.name,
]

base = TEX.stem
engine_log = HANT_DIR / f"{base}.log"
pdf = HANT_DIR / f"{base}.pdf"
passes = []
for pass_number in (1, 2):
    run = subprocess.run(
        command,
        cwd=HANT_DIR,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    transcript = ROOT / "qa" / f"P10_HANT_XELATEX_PASS{pass_number}.stdout.log"
    transcript.write_bytes(run.stdout)
    if not engine_log.exists():
        raise RuntimeError(f"XeLaTeX pass {pass_number} did not create an engine log")
    retained_engine_log = ROOT / "qa" / f"P10_HANT_XELATEX_PASS{pass_number}.engine.log"
    shutil.copyfile(engine_log, retained_engine_log)
    log_text = retained_engine_log.read_text(encoding="utf-8", errors="replace")
    page_matches = re.findall(r"\((\d+) pages?(?:,\s*\d+ bytes)?\)", log_text)
    if run.returncode != 0:
        raise RuntimeError(
            f"XeLaTeX pass {pass_number} failed with exit {run.returncode}; see {transcript}"
        )
    if not pdf.exists():
        raise RuntimeError(f"XeLaTeX pass {pass_number} did not create a PDF")
    if not page_matches:
        raise RuntimeError(f"Could not mechanically parse page count from pass {pass_number} log")
    passes.append(
        {
            "pass": pass_number,
            "exit_code": run.returncode,
            "pages": int(page_matches[-1]),
            "transcript_path": str(transcript),
            "transcript_bytes": bytes_count(transcript),
            "transcript_sha256": sha(transcript),
            "retained_engine_log_path": str(retained_engine_log),
            "retained_engine_log_bytes": bytes_count(retained_engine_log),
            "retained_engine_log_sha256": sha(retained_engine_log),
            "warning_counts": warning_counts(log_text),
            "pdf_bytes_after_pass": bytes_count(pdf),
            "pdf_sha256_after_pass": sha(pdf),
        }
    )

final_log_text = engine_log.read_text(encoding="utf-8", errors="replace")
record = {
    "schema_version": "1.0.0",
    "work_id": "NOETHER-P10",
    "operation": "producer_only_two_pass_xelatex_build_controlled_generic_hant",
    "build_script_path": str(SCRIPT),
    "build_script_sha256": sha(SCRIPT),
    "input_tex_path": str(TEX),
    "input_tex_bytes": bytes_count(TEX),
    "input_tex_sha256": sha(TEX),
    "opencc_record_path": str(OPENCC_RECORD),
    "opencc_record_sha256": sha(OPENCC_RECORD),
    "xelatex_executable_path": str(xelatex),
    "xelatex_version_first_line": version_text.splitlines()[0],
    "command": command,
    "working_directory": str(HANT_DIR),
    "requested_passes": 2,
    "successful_passes": len(passes),
    "passes": passes,
    "final_pdf_path": str(pdf),
    "final_pdf_bytes": bytes_count(pdf),
    "final_pdf_sha256": sha(pdf),
    "final_engine_log_path": str(engine_log),
    "final_engine_log_bytes": bytes_count(engine_log),
    "final_engine_log_sha256": sha(engine_log),
    "final_warning_counts": warning_counts(final_log_text),
    "pages": passes[-1]["pages"],
    "rendering_or_visual_inspection_performed": False,
    "source_check_performed": False,
    "translation_or_formula_check_performed": False,
    "localization_status": "controlled generic zh-Hant only; not zh-Hant-TW/HK/MO prose",
    "review_state": "independent check pending",
    "claim_limit": (
        "Successful mechanical compilation only; no source, linguistic, semantic, formula-content, "
        "terminology, visual, regional, human, external, archive, publication, or certification validation."
    ),
}
BUILD_RECORD.write_text(
    json.dumps(record, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
    newline="\n",
)
print(json.dumps(record, ensure_ascii=True, indent=2))
