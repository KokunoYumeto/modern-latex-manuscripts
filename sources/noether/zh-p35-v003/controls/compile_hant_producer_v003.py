#!/usr/bin/env python3
"""Run two serial producer-only XeLaTeX passes for Paper 35 Hant v003."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
import hashlib
import json
import re
import shutil
import subprocess


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = Path(__file__).resolve()
XELATEX = Path(r"C:\Users\Floris\AppData\Local\Programs\MiKTeX\miktex\bin\x64\xelatex.exe")
TEX = ROOT / (
    "build/zh-Hant-controlled-v003/"
    "Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_v003.tex"
)
UPSTREAM = ROOT / "controls/OPENCC_PRODUCER_RECORD_v003.json"
RECORD = ROOT / "controls/HANT_MECHANICAL_BUILD_RECORD_v003.json"


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


def main() -> int:
    if not XELATEX.is_file():
        raise FileNotFoundError(f"Missing XeLaTeX executable: {XELATEX}")
    if not TEX.is_file() or not UPSTREAM.is_file():
        raise FileNotFoundError(f"Missing target or upstream record: {TEX}; {UPSTREAM}")
    if RECORD.exists():
        raise RuntimeError(f"Refusing to overwrite existing Hant v003 build record: {RECORD}")

    upstream_data = json.loads(UPSTREAM.read_text(encoding="utf-8"))
    expected = upstream_data["output"]["sha256"]
    if sha(TEX) != expected:
        raise RuntimeError(f"Target/upstream hash mismatch: expected {expected}, found {sha(TEX)}")
    if upstream_data["exact_checker_candidate_equality"] is not True:
        raise RuntimeError("Upstream record does not assert exact checker-candidate equality")

    version = subprocess.run(
        [str(XELATEX), "--version"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    ).stdout.decode("utf-8", errors="replace")

    target_dir = TEX.parent
    base = TEX.stem
    engine_log = target_dir / f"{base}.log"
    pdf = target_dir / f"{base}.pdf"
    aux = target_dir / f"{base}.aux"
    stale_outputs = [path for path in (engine_log, pdf, aux) if path.exists()]
    if stale_outputs:
        raise RuntimeError(
            "Refusing to reuse pre-existing v003 build outputs: "
            + "; ".join(str(path) for path in stale_outputs)
        )

    command = [
        str(XELATEX),
        "--quiet",
        "-interaction=nonstopmode",
        "-halt-on-error",
        "-file-line-error",
        "-no-shell-escape",
        TEX.name,
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
        transcript = ROOT / "controls" / f"P35_HANT_V003_XELATEX_PASS{number}.stdout.log"
        transcript.write_bytes(run.stdout)
        if not engine_log.exists():
            raise RuntimeError(f"Pass {number} did not create an engine log; see {transcript}")
        retained_log = ROOT / "controls" / f"P35_HANT_V003_XELATEX_PASS{number}.engine.log"
        shutil.copyfile(engine_log, retained_log)
        log_text = retained_log.read_text(encoding="utf-8", errors="replace")
        page_matches = re.findall(r"\((\d+) pages?(?:,\s*\d+ bytes)?\)", log_text)
        pass_record = {
            "pass": number,
            "exit_code": run.returncode,
            "transcript": meta(transcript),
            "retained_engine_log": meta(retained_log),
            "warning_counts": warning_counts(log_text),
            "pages_reported_by_log": int(page_matches[-1]) if page_matches else None,
            "pdf_after_pass": meta(pdf) if pdf.exists() else None,
        }
        passes.append(pass_record)
        if run.returncode != 0:
            failure = ROOT / "controls" / f"P35_HANT_V003_FAILED_BUILD_PASS{number}.json"
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
        "record_type": "producer_hant_v003_mechanical_build",
        "work_id": "NOETHER-P35-ZH",
        "operation": "producer_only_two_pass_xelatex_v003_zh-Hant-controlled",
        "provenance_decision_id": "ZH-D135",
        "freeze_decision_state": "freeze_decision_pending",
        "checker_return_id": "ZHCHK-NOETHER-P35-V002-RETURN-001",
        "finding_applied": "ZHCHK-P35-F015",
        "recorded_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "build_script": meta(SCRIPT),
        "upstream_record": meta(UPSTREAM),
        "input_tex": meta(TEX),
        "xelatex": {**meta(XELATEX), "version_first_line": version.splitlines()[0]},
        "command": command,
        "working_directory": str(target_dir),
        "requested_passes": 2,
        "successful_passes": len(passes),
        "passes": passes,
        "final_pdf": {
            **meta(pdf),
            "pages_reported_by_log": passes[-1]["pages_reported_by_log"],
            "opened_or_rendered_by_producer": False,
        },
        "final_engine_log": {**meta(engine_log), "warning_counts": warning_counts(final_log_text)},
        "localization_status": "controlled generic zh-Hant only; not zh-Hant-TW/HK/MO prose",
        "review_state": "mechanical compile complete; producer freeze and independent recheck pending",
        "epistemic_boundary": {
            "compilation_success_is_translation_validation": False,
            "source_check_performed": False,
            "semantic_or_formula_content_check_performed": False,
            "translation_quality_check_performed": False,
            "visual_check_performed": False,
            "pdf_opened_or_rendered": False,
            "native_or_regional_validation_performed": False,
            "human_or_external_validation_claimed": False,
            "approval_publication_archive_or_certification_claimed": False,
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
