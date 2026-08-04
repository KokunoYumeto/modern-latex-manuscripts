#!/usr/bin/env python3
"""Run two serial producer-only XeLaTeX passes for one Paper 35 target."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
import argparse
import hashlib
import json
import re
import shutil
import subprocess


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = Path(__file__).resolve()
XELATEX = Path(r"C:\Users\Floris\AppData\Local\Programs\MiKTeX\miktex\bin\x64\xelatex.exe")

TARGETS = {
    "hans": {
        "label": "zh-Hans-CN",
        "short": "HANS",
        "tex": ROOT / "build/zh-Hans-CN/Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex",
        "upstream": ROOT / "controls/HANS_ASSEMBLY_RECORD.json",
        "upstream_key": ("output", "sha256"),
        "record": ROOT / "controls/HANS_MECHANICAL_BUILD_RECORD.json",
        "localization": "PRC-oriented Simplified Chinese producer translation",
    },
    "hant": {
        "label": "zh-Hant-controlled",
        "short": "HANT",
        "tex": ROOT / "build/zh-Hant-controlled/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_v001.tex",
        "upstream": ROOT / "controls/OPENCC_PRODUCER_RECORD.json",
        "upstream_key": ("output_sha256",),
        "record": ROOT / "controls/HANT_MECHANICAL_BUILD_RECORD.json",
        "localization": "controlled generic zh-Hant only; not zh-Hant-TW/HK/MO prose",
    },
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def meta(path: Path) -> dict[str, object]:
    return {"path": str(path), "bytes": len(path.read_bytes()), "sha256": sha(path)}


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
        "error_pattern_matches": len(re.findall(r"(?m)^!|Emergency stop|Fatal error", text)),
    }


parser = argparse.ArgumentParser()
parser.add_argument("target", choices=sorted(TARGETS))
args = parser.parse_args()
cfg = TARGETS[args.target]
tex: Path = cfg["tex"]
upstream: Path = cfg["upstream"]
record_path: Path = cfg["record"]

if not XELATEX.is_file():
    raise FileNotFoundError(f"Missing XeLaTeX executable: {XELATEX}")
if not tex.is_file() or not upstream.is_file():
    raise FileNotFoundError(f"Missing target or upstream record: {tex}; {upstream}")

upstream_data = json.loads(upstream.read_text(encoding="utf-8"))
expected = upstream_data
for key in cfg["upstream_key"]:
    expected = expected[key]
if sha(tex) != expected:
    raise RuntimeError(f"Target/upstream hash mismatch: expected {expected}, found {sha(tex)}")

version = subprocess.run(
    [str(XELATEX), "--version"],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    check=True,
).stdout.decode("utf-8", errors="replace")

target_dir = tex.parent
base = tex.stem
engine_log = target_dir / f"{base}.log"
pdf = target_dir / f"{base}.pdf"
command = [
    str(XELATEX),
    "--quiet",
    "-interaction=nonstopmode",
    "-halt-on-error",
    "-file-line-error",
    "-no-shell-escape",
    tex.name,
]
passes: list[dict[str, object]] = []

for number in (1, 2):
    run = subprocess.run(
        command,
        cwd=target_dir,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    transcript = ROOT / "controls" / f"P35_{cfg['short']}_XELATEX_PASS{number}.stdout.log"
    transcript.write_bytes(run.stdout)
    if not engine_log.exists():
        raise RuntimeError(f"Pass {number} did not create an engine log; see {transcript}")
    retained_log = ROOT / "controls" / f"P35_{cfg['short']}_XELATEX_PASS{number}.engine.log"
    shutil.copyfile(engine_log, retained_log)
    log_text = retained_log.read_text(encoding="utf-8", errors="replace")
    page_matches = re.findall(r"\((\d+) pages?(?:,\s*\d+ bytes)?\)", log_text)
    pass_record = {
        "pass": number,
        "exit_code": run.returncode,
        "transcript": meta(transcript),
        "retained_engine_log": meta(retained_log),
        "warning_counts": warning_counts(log_text),
        "pages": int(page_matches[-1]) if page_matches else None,
        "pdf_after_pass": meta(pdf) if pdf.exists() else None,
    }
    passes.append(pass_record)
    if run.returncode != 0:
        failure = ROOT / "controls" / f"P35_{cfg['short']}_FAILED_BUILD_PASS{number}.json"
        failure.write_text(
            json.dumps(pass_record, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        raise RuntimeError(f"XeLaTeX pass {number} failed with exit {run.returncode}; see {transcript}")
    if not pdf.exists() or not page_matches:
        raise RuntimeError(f"Pass {number} lacks expected PDF/page evidence")

final_log_text = engine_log.read_text(encoding="utf-8", errors="replace")
record = {
    "schema_version": "1.0.0",
    "work_id": "NOETHER-P35-ZH",
    "operation": f"producer_only_two_pass_xelatex_{cfg['label']}",
    "recorded_at": datetime.now().astimezone().isoformat(timespec="seconds"),
    "build_script": meta(SCRIPT),
    "upstream_record": meta(upstream),
    "input_tex": meta(tex),
    "xelatex": {
        **meta(XELATEX),
        "version_first_line": version.splitlines()[0],
    },
    "command": command,
    "working_directory": str(target_dir),
    "requested_passes": 2,
    "successful_passes": len(passes),
    "passes": passes,
    "final_pdf": {**meta(pdf), "pages_reported_by_log": passes[-1]["pages"], "opened_or_rendered_by_producer": False},
    "final_engine_log": {**meta(engine_log), "warning_counts": warning_counts(final_log_text)},
    "localization_status": cfg["localization"],
    "review_state": "independent check pending",
    "epistemic_boundary": {
        "compilation_success_is_translation_validation": False,
        "source_check_performed": False,
        "semantic_or_formula_check_performed": False,
        "translation_quality_check_performed": False,
        "visual_check_performed": False,
        "native_or_regional_validation_performed": False,
    },
}
record_path.write_text(
    json.dumps(record, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
    newline="\n",
)
print(json.dumps(record, ensure_ascii=True, indent=2))

