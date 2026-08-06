#!/usr/bin/env python3
"""Compile four ED0005-bound v038 cumulative Slavic readers.

All XeLaTeX runs are deliberately serial to avoid the memory spikes that
previously interrupted this lane.  Each exact archive-normalized 219-unit
Papers 1--43 TeX base is rebuilt first; Work 44, Post45, and PostBib follow.
"""

from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
from datetime import datetime
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "release" / "source"
PDF = ROOT / "release" / "pdf"
BUILD = ROOT / "release" / "build"
EVIDENCE = ROOT / "release" / "evidence"
TARGETS = ("ru", "uk", "isv", "isv-cy")
COMPONENTS = ("44-book", "45", "bib")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def record(path: Path) -> dict:
    return {
        "path": path.resolve().as_posix(),
        "bytes": path.stat().st_size,
        "sha256": sha256(path),
    }


def page_count(path: Path) -> int:
    return len(PdfReader(str(path)).pages)


def run_xelatex(source: Path, build_dir: Path, jobname: str) -> tuple[Path, list[dict]]:
    build_dir.mkdir(parents=True, exist_ok=True)
    logs = []
    for pass_number in (1, 2):
        command = [
            "xelatex",
            "-interaction=nonstopmode",
            "-halt-on-error",
            f"-jobname={jobname}",
            f"-output-directory={build_dir}",
            str(source.resolve()),
        ]
        completed = subprocess.run(
            command,
            cwd=source.parent,
            text=True,
            encoding="utf-8",
            errors="replace",
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        log = build_dir / f"pass{pass_number}.stdout.log"
        log.write_text(completed.stdout, encoding="utf-8", newline="\n")
        logs.append({"pass": pass_number, "exit_code": completed.returncode, **record(log)})
        if completed.returncode:
            raise RuntimeError(f"XeLaTeX failed for {source}; see {log}")
    produced = build_dir / f"{jobname}.pdf"
    if not produced.exists():
        raise FileNotFoundError(produced)
    return produced, logs


def cumulative_recipe(target: str, inputs: list[Path]) -> Path:
    recipe = SOURCE / f"noether-{target}-v038.tex"
    lines = [
        "% Generated cumulative recipe; exact inputs are hash-bound in build_manifest.json.",
        r"\documentclass{article}",
        r"\usepackage{pdfpages}",
        r"\begin{document}",
    ]
    for path in inputs:
        relative = Path("..") / "pdf" / path.name
        lines.append(r"\includepdf[pages=-]{" + relative.as_posix() + "}")
    lines.append(r"\end{document}")
    recipe.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return recipe


def main() -> int:
    PDF.mkdir(parents=True, exist_ok=True)
    BUILD.mkdir(parents=True, exist_ok=True)
    EVIDENCE.mkdir(parents=True, exist_ok=True)

    base_records: dict[str, dict] = {}
    for target in TARGETS:
        source = SOURCE / f"base-papers1-43-{target}.tex"
        if not source.exists():
            raise FileNotFoundError(source)
        jobname = f"base-papers1-43-{target}"
        produced, logs = run_xelatex(source, BUILD / "base" / target, jobname)
        output = PDF / f"{jobname}.pdf"
        shutil.copy2(produced, output)
        base_records[target] = {
            "scope": "complete numbered Papers 1--43 / 219 exact producer units",
            "source": record(source),
            "pdf": {**record(output), "pages": page_count(output)},
            "build_logs": logs,
        }

    component_records: dict[str, list[dict]] = {target: [] for target in TARGETS}
    for target in TARGETS:
        for stem in COMPONENTS:
            source = SOURCE / f"{stem}-{target}.tex"
            if not source.exists():
                raise FileNotFoundError(source)
            jobname = f"{stem}-{target}"
            produced, logs = run_xelatex(source, BUILD / "components" / target / stem, jobname)
            output = PDF / f"{jobname}.pdf"
            shutil.copy2(produced, output)
            component_records[target].append(
                {
                    "component": stem,
                    "source": record(source),
                    "pdf": {**record(output), "pages": page_count(output)},
                    "build_logs": logs,
                }
            )

    cumulative_records = []
    for target in TARGETS:
        base_pdf = PDF / f"base-papers1-43-{target}.pdf"
        inputs = [base_pdf] + [PDF / f"{stem}-{target}.pdf" for stem in COMPONENTS]
        recipe = cumulative_recipe(target, inputs)
        jobname = f"noether-{target}-v038"
        produced, logs = run_xelatex(recipe, BUILD / "cumulative" / target, jobname)
        output = PDF / f"{jobname}.pdf"
        shutil.copy2(produced, output)
        input_records = [{**record(path), "pages": page_count(path)} for path in inputs]
        cumulative_records.append(
            {
                "target": target,
                "recipe": record(recipe),
                "numbered_paper_base": base_records[target],
                "inputs": input_records,
                "input_page_sum": sum(item["pages"] for item in input_records),
                "pdf": {**record(output), "pages": page_count(output)},
                "build_logs": logs,
            }
        )

    manifest = {
        "schema": "noether-slavic-v038-build-manifest/1.0",
        "generated_at": datetime.now().astimezone().isoformat(),
        "authority": {
            "pointer_id": "NOETH-DE-AUTH-v038-20260805",
            "pointer_sha256": "666FCB863C8599778BB1B48DCD0D4E444D6486133B7FE703E6CDE073F15FFBAE",
            "authority_id": "NOETH-DE-ED-0005",
            "authority_sha256": "1A44F967B29972E8F99E5C323A479162AD82A23FC457395915A4BB9DDF51AD41",
        },
        "scope": "rebuilt 219-unit Papers 1--43 bases plus complete post-P43 Work 44, Post45, and PostBib on four Slavic surfaces",
        "build_policy": "serial XeLaTeX, two passes per numbered-paper base, component, and cumulative reader",
        "base_records": base_records,
        "component_records": component_records,
        "cumulative_records": cumulative_records,
        "review_state": "build evidence only; source, text, page, render, and language review are separate gates",
    }
    output = EVIDENCE / "build_manifest.json"
    output.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        "PASS "
        + json.dumps(
            {
                "components": sum(len(items) for items in component_records.values()),
                "cumulative": [
                    {"target": item["target"], "pages": item["pdf"]["pages"]}
                    for item in cumulative_records
                ],
                "manifest": {**record(output)},
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
