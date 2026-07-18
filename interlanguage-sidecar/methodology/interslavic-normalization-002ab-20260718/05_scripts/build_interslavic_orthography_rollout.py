#!/usr/bin/env python3
"""Compile and verify every TeX unit changed by orthography Tranche 002A.

The build is deliberately serial.  Each XeLaTeX process finishes before the
next starts, console output is streamed to a file rather than retained in
memory, and a durable JSONL journal permits a safe resume after interruption.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "03_projects" / "noether" / "02_slavic_working_corpus" / "translations"
WORKSPACE = (
    ROOT
    / "03_projects"
    / "language_management"
    / "slavic_interslavic"
    / "normalization_20260718"
    / "tranche_002a_orthography"
)
EVIDENCE = WORKSPACE / "evidence"
PREFLIGHT = EVIDENCE / "ORTHOGRAPHY_ROLLOUT_PREFLIGHT.json"
JOURNAL = EVIDENCE / "BUILD_JOURNAL.jsonl"
REPORT = EVIDENCE / "BUILD_REPORT.json"
COMPILE_REPAIR_REPORT = EVIDENCE / "COMPILE_REPAIR_REPORT.json"
BUILD_ROOT = WORKSPACE / "build"
PDF_ROOT = WORKSPACE / "compiled_pdfs"
LOG_ROOT = WORKSPACE / "build_logs"

WARNING_PATTERNS = {
    "latex_warning": re.compile(r"LaTeX Warning:", re.IGNORECASE),
    "package_warning": re.compile(r"Package .+ Warning:", re.IGNORECASE),
    "missing_character": re.compile(r"Missing character:", re.IGNORECASE),
    "overfull_box": re.compile(r"Overfull \\.[hv]box", re.IGNORECASE),
    "underfull_box": re.compile(r"Underfull \\.[hv]box", re.IGNORECASE),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def load_previous_successes() -> dict[str, dict[str, object]]:
    successes: dict[str, dict[str, object]] = {}
    if not JOURNAL.is_file():
        return successes
    with JOURNAL.open("r", encoding="utf-8") as handle:
        for line in handle:
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            if row.get("success"):
                successes[str(row["path"])] = row
    return successes


def prior_is_valid(row: dict[str, object], source: Path, expected_source_hash: str) -> bool:
    if row.get("source_sha256") != expected_source_hash or sha256(source) != expected_source_hash:
        return False
    pdf = Path(str(row.get("pdf", "")))
    return (
        pdf.is_file()
        and row.get("pdf_sha256") == sha256(pdf)
        and int(row.get("pages", 0)) > 0
    )


def count_log_findings(log: Path) -> dict[str, int]:
    counts = {key: 0 for key in WARNING_PATTERNS}
    with log.open("r", encoding="utf-8", errors="replace") as handle:
        for line in handle:
            for key, pattern in WARNING_PATTERNS.items():
                if pattern.search(line):
                    counts[key] += 1
    return counts


def log_tail(log: Path, lines: int = 30) -> list[str]:
    tail: list[str] = []
    with log.open("r", encoding="utf-8", errors="replace") as handle:
        for line in handle:
            tail.append(line.rstrip())
            if len(tail) > lines:
                tail.pop(0)
    return tail


def build_one(index: int, total: int, item: dict[str, object]) -> dict[str, object]:
    relative = Path(str(item["path"]))
    source = CORPUS / relative
    expected_hash = str(item["projected_after_sha256"])
    actual_hash = sha256(source)
    if actual_hash != expected_hash:
        raise RuntimeError(
            f"Source hash differs from reviewed rollout for {relative}: "
            f"expected {expected_hash}, found {actual_hash}"
        )

    relative_parent = relative.parent
    # MiKTeX still encounters Windows path limits for deeply nested corpus
    # paths.  Keep its disposable aux/output directory deliberately short;
    # the copied PDF and logs retain the readable corpus-relative structure.
    build_dir = BUILD_ROOT / f"u{index:03d}"
    pdf_dir = PDF_ROOT / relative_parent
    log_dir = LOG_ROOT / relative_parent
    build_dir.mkdir(parents=True, exist_ok=True)
    pdf_dir.mkdir(parents=True, exist_ok=True)
    log_dir.mkdir(parents=True, exist_ok=True)

    console_log = log_dir / f"{source.stem}.console.log"
    started = time.monotonic()
    command = [
        "latexmk",
        "-silent",
        "-g",
        "-xelatex",
        "-interaction=nonstopmode",
        "-halt-on-error",
        "-file-line-error",
        f"-outdir={build_dir}",
        source.name,
    ]
    env = os.environ.copy()
    env["max_print_line"] = "1000"
    with console_log.open("w", encoding="utf-8", errors="replace") as console:
        completed = subprocess.run(
            command,
            cwd=source.parent,
            env=env,
            stdout=console,
            stderr=subprocess.STDOUT,
            check=False,
            timeout=180,
        )
    duration = round(time.monotonic() - started, 3)

    built_pdf = build_dir / f"{source.stem}.pdf"
    built_tex_log = build_dir / f"{source.stem}.log"
    delivered_pdf = pdf_dir / f"{source.stem}.pdf"
    delivered_tex_log = log_dir / f"{source.stem}.tex.log"
    if built_pdf.is_file():
        shutil.copy2(built_pdf, delivered_pdf)
    if built_tex_log.is_file():
        shutil.copy2(built_tex_log, delivered_tex_log)

    success = completed.returncode == 0 and delivered_pdf.is_file()
    pages = 0
    pdf_hash = None
    pdf_bytes = 0
    pdf_error = None
    if success:
        try:
            pages = len(PdfReader(str(delivered_pdf)).pages)
            if pages < 1:
                raise RuntimeError("compiled PDF has no pages")
            pdf_hash = sha256(delivered_pdf)
            pdf_bytes = delivered_pdf.stat().st_size
        except Exception as exc:  # preserve failure evidence in the journal
            success = False
            pdf_error = str(exc)

    scanned_log = delivered_tex_log if delivered_tex_log.is_file() else console_log
    result: dict[str, object] = {
        "path": relative.as_posix(),
        "script": item["script"],
        "source_sha256": actual_hash,
        "success": success,
        "returncode": completed.returncode,
        "duration_seconds": duration,
        "pdf": str(delivered_pdf) if delivered_pdf.is_file() else None,
        "pdf_sha256": pdf_hash,
        "pdf_bytes": pdf_bytes,
        "pages": pages,
        "tex_log": str(delivered_tex_log) if delivered_tex_log.is_file() else None,
        "console_log": str(console_log),
        "findings": count_log_findings(scanned_log),
        "pdf_error": pdf_error,
    }
    if not success:
        result["console_tail"] = log_tail(console_log)
    print(
        f"[{index:03d}/{total:03d}] {'PASS' if success else 'FAIL'} "
        f"{item['script']} {relative.as_posix()} pages={pages} seconds={duration}",
        flush=True,
    )
    return result


def main() -> int:
    global WORKSPACE, EVIDENCE, PREFLIGHT, JOURNAL, REPORT
    global COMPILE_REPAIR_REPORT, BUILD_ROOT, PDF_ROOT, LOG_ROOT
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--workspace",
        type=Path,
        default=WORKSPACE,
        help="Tranche workspace containing evidence/<preflight-name>",
    )
    parser.add_argument(
        "--preflight-name",
        default="ORTHOGRAPHY_ROLLOUT_PREFLIGHT.json",
    )
    args = parser.parse_args()

    WORKSPACE = args.workspace.resolve()
    EVIDENCE = WORKSPACE / "evidence"
    PREFLIGHT = EVIDENCE / args.preflight_name
    JOURNAL = EVIDENCE / "BUILD_JOURNAL.jsonl"
    REPORT = EVIDENCE / "BUILD_REPORT.json"
    COMPILE_REPAIR_REPORT = EVIDENCE / "COMPILE_REPAIR_REPORT.json"
    BUILD_ROOT = WORKSPACE / "build"
    PDF_ROOT = WORKSPACE / "compiled_pdfs"
    LOG_ROOT = WORKSPACE / "build_logs"

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if not PREFLIGHT.is_file():
        raise RuntimeError(f"Missing reviewed preflight: {PREFLIGHT}")
    preflight = json.loads(PREFLIGHT.read_text(encoding="utf-8"))
    items = [dict(item) for item in preflight["planned_files"]]
    expected_count = int(preflight["planned_changed_files"])
    if len(items) != expected_count:
        raise RuntimeError(f"Expected {expected_count} changed files, found {len(items)}")

    compile_repairs: list[dict[str, object]] = []
    if COMPILE_REPAIR_REPORT.is_file():
        repair = json.loads(COMPILE_REPAIR_REPORT.read_text(encoding="utf-8"))
        matching = [item for item in items if item["path"] == repair["path"]]
        if len(matching) != 1:
            raise RuntimeError(f"Compile repair path is outside this build: {repair['path']}")
        item = matching[0]
        if item["projected_after_sha256"] != repair["before_sha256"]:
            raise RuntimeError("Compile repair preimage does not match orthography output")
        item["orthography_projected_sha256"] = item["projected_after_sha256"]
        item["projected_after_sha256"] = repair["after_sha256"]
        compile_repairs.append(repair)

    EVIDENCE.mkdir(parents=True, exist_ok=True)
    prior = load_previous_successes()
    final_by_path: dict[str, dict[str, object]] = {}
    for path, row in prior.items():
        source = CORPUS / Path(path)
        if source.is_file() and prior_is_valid(row, source, str(row["source_sha256"])):
            final_by_path[path] = row

    with JOURNAL.open("a", encoding="utf-8", newline="\n") as journal:
        for index, item in enumerate(items, start=1):
            key = str(item["path"])
            previous = final_by_path.get(key)
            if previous and prior_is_valid(
                previous, CORPUS / Path(key), str(item["projected_after_sha256"])
            ):
                print(f"[{index:03d}/{len(items):03d}] RESUME-PASS {key}", flush=True)
                continue
            try:
                result = build_one(index, len(items), item)
            except subprocess.TimeoutExpired as exc:
                result = {
                    "path": key,
                    "script": item["script"],
                    "source_sha256": sha256(CORPUS / Path(key)),
                    "success": False,
                    "timeout_seconds": exc.timeout,
                    "error": "latexmk timeout",
                }
                print(f"[{index:03d}/{len(items):03d}] FAIL timeout {key}", flush=True)
            journal.write(json.dumps(result, ensure_ascii=False) + "\n")
            journal.flush()
            final_by_path[key] = result

    ordered = [final_by_path[str(item["path"])] for item in items]
    failures = [row for row in ordered if not row.get("success")]
    report = {
        "schema": "interslavic-orthography-build-v1",
        "generated_at": datetime.now().astimezone().isoformat(),
        "scope": f"All {expected_count} canonical TeX units listed by {preflight.get('schema', 'the tranche preflight')}",
        "tranche_workspace": str(WORKSPACE),
        "build_policy": {
            "engine": "latexmk/XeLaTeX",
            "parallel_processes": 1,
            "console_capture": "streamed directly to per-file logs",
            "resume_journal": str(JOURNAL),
        },
        "expected_files": len(items),
        "successful_files": len(items) - len(failures),
        "failed_files": len(failures),
        "total_pages": sum(int(row.get("pages", 0)) for row in ordered),
        "total_pdf_bytes": sum(int(row.get("pdf_bytes", 0)) for row in ordered),
        "finding_totals": {
            key: sum(int(row.get("findings", {}).get(key, 0)) for row in ordered)
            for key in WARNING_PATTERNS
        },
        "compile_repairs": compile_repairs,
        "failures": failures,
        "results": ordered,
        "status_limit": "Compilation evidence for reviewed orthography only; not lexical or community validation.",
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {key: report[key] for key in (
                "successful_files",
                "failed_files",
                "total_pages",
                "total_pdf_bytes",
                "finding_totals",
            )},
            ensure_ascii=False,
            indent=2,
        ),
        flush=True,
    )
    print(f"wrote {REPORT}", flush=True)
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
