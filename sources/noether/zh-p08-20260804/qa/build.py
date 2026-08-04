#!/usr/bin/env python3
"""Compile P08 Hans and controlled Hant serially; do not render or open PDFs."""

from __future__ import annotations

from datetime import datetime
from hashlib import sha256
import json
from pathlib import Path
import re
import shutil
import subprocess


ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / "qa" / "build.json"
TARGETS = {
    "hans": {
        "source": ROOT / "zh-Hans-CN" / "hans.tex",
        "expected": {
            "bytes": 25041,
            "sha256": "C103A219FEC5CD43090305E5720A7BB17DC2DB9BB682778F9CEC40E8124C4A53",
        },
    },
    "hant": {
        "source": ROOT / "zh-Hant-controlled" / "hant.tex",
        "expected": {
            "bytes": 25124,
            "sha256": "9C7BFA338E342311AC5F711D07F7FE9FF66E35B55132458E6D5CB2076515148B",
        },
    },
}
OUT_NAMES = {"hans": "hans2", "hant": "hant"}
FAILED_PROBE = {
    "hans.aux": (32, "67B32DCE0F49801FFE559BB8D2B4FBDC43A6C18522E08615B67A0263201F0807"),
    "hans.log": (21134, "B62E582499AB4F52C7AA1EAABC2822B95B5170459BB5AEB6DE9F99A1009686FF"),
    "hans.pdf": (241592, "60A60E628D64168AA9AA2BFBF73532038594CA8A1FBBCA6D656FA69245452252"),
    "pass1.txt": (4177, "BB542DE7321A335A8F6482880F12C04584BB0B86E78A34695DCF145D3E7DD331"),
    "pass2.txt": (4327, "44C14B4EFFFBF2E4DB212E606AD02096CA224E47355F46C173DEB1609049B278"),
}


def digest(data: bytes) -> str:
    return sha256(data).hexdigest().upper()


def meta(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    return {"path": str(path), "bytes": len(data), "sha256": digest(data)}


def main() -> int:
    if RECORD.exists():
        raise RuntimeError(f"Refusing to overwrite build record: {RECORD}")
    compiler_text = shutil.which("xelatex")
    if not compiler_text:
        raise RuntimeError("xelatex not found")
    compiler = Path(compiler_text).resolve()
    version = subprocess.run(
        [str(compiler), "--version"],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    ).stdout.splitlines()[0]

    failed_probe_dir = ROOT / "build" / "hans"
    failed_probe: dict[str, object] = {}
    for name, expected in FAILED_PROBE.items():
        path = failed_probe_dir / name
        observed = (path.stat().st_size, digest(path.read_bytes()))
        if observed != expected:
            raise RuntimeError(f"Failed-probe custody mismatch for {path}: {observed}")
        failed_probe[name] = meta(path)

    results: dict[str, object] = {}
    for label, spec in TARGETS.items():
        source = spec["source"]
        source_data = source.read_bytes()
        observed = {"bytes": len(source_data), "sha256": digest(source_data)}
        if observed != spec["expected"]:
            raise RuntimeError(f"{label} source identity mismatch: {observed}")
        out = ROOT / "build" / OUT_NAMES[label]
        if out.exists() and any(out.iterdir()):
            raise RuntimeError(f"Refusing to overwrite nonempty build directory: {out}")
        out.mkdir(parents=True, exist_ok=True)

        passes: list[dict[str, object]] = []
        for number in (1, 2):
            command = [
                str(compiler),
                "-interaction=nonstopmode",
                "-halt-on-error",
                "-file-line-error",
                f"-output-directory={out}",
                str(source),
            ]
            run = subprocess.run(
                command,
                cwd=ROOT,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
            )
            transcript = run.stdout + run.stderr
            transcript_path = out / f"pass{number}.txt"
            transcript_path.write_text(transcript, encoding="utf-8", newline="\n")
            passes.append(
                {
                    "pass": number,
                    "exit_code": run.returncode,
                    "transcript": meta(transcript_path),
                }
            )
            if run.returncode != 0:
                raise RuntimeError(f"{label} XeLaTeX pass {number} failed; evidence preserved")

        pdf = out / f"{source.stem}.pdf"
        log = out / f"{source.stem}.log"
        if not pdf.is_file() or not log.is_file():
            raise RuntimeError(f"{label} build lacks expected PDF/log")
        log_text = log.read_text(encoding="utf-8", errors="replace")
        flags = {
            "fatal": len(re.findall(r"Fatal error|Emergency stop", log_text, re.I)),
            "undefined_control": len(re.findall(r"Undefined control sequence", log_text, re.I)),
            "overfull": len(re.findall(r"Overfull \\[hv]box", log_text)),
            "underfull": len(re.findall(r"Underfull \\[hv]box", log_text)),
            "missing_character": len(re.findall(r"Missing character", log_text, re.I)),
        }
        page_matches = re.findall(r"\((\d+) pages?\)", log_text)
        pages = int(page_matches[-1]) if page_matches else None
        if flags["fatal"] or flags["undefined_control"] or pages is None:
            raise RuntimeError(f"{label} log gate failed: {flags}; pages={pages}")
        results[label] = {
            "source": meta(source),
            "passes": passes,
            "pdf": meta(pdf),
            "log": meta(log),
            "pages_by_compiler_log": pages,
            "log_flags": flags,
        }

    record = {
        "schema_version": "1.0.0",
        "record_type": "producer_serial_build",
        "recorded_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "work_id": "NOETHER-P08-ZH",
        "compiler": {"path": str(compiler), "version": version},
        "execution_order": ["hans-pass1", "hans-pass2", "hant-pass1", "hant-pass2"],
        "preserved_failed_probe": {
            "cause": "first page-count parser did not tolerate MiKTeX path line wrapping",
            "effect": "both Hans compiler passes exited zero; post-build parser returned pages=None and stopped before Hant",
            "path": str(failed_probe_dir),
            "members": failed_probe,
            "mutation_after_failure": False,
        },
        "results": results,
        "review_state": "mechanical compile complete; independent checking and visual inspection pending",
        "epistemic_boundary": {
            "pdf_rendered_or_opened": False,
            "visual_check_performed": False,
            "source_or_scan_check_performed": False,
            "translation_quality_check_performed": False,
            "human_or_external_validation_claimed": False,
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
