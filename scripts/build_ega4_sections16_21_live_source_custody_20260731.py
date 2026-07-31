#!/usr/bin/env python3
"""Capture a stable, buildable EGA IV Sections 16-21 source snapshot."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
import subprocess
import tempfile
from datetime import datetime
from pathlib import Path


AUTHORITY_SHA256 = (
    "B4277FB99C6EDF8FEEC5B01F54368E4B8521BCD52871316C0EDF6FF4AE69389E"
)
FORBIDDEN_TEXT = [
    re.compile(pattern, re.IGNORECASE)
    for pattern in (
        r"C:\\Users\\",
        r"AppData",
        r"Papors",
        r"Chatnotes",
        r"Claude",
        r"Codex",
        r"ChatGPT",
        r"Fable",
        r"source_thread_id",
        r"019f[0-9a-f-]{20,}",
    )
]
HARD_TEX_PATTERNS = (
    "! LaTeX Error",
    "Undefined control sequence",
    "Emergency stop",
    "Fatal error",
    "Missing character:",
    "destination with the same identifier",
)


LANES = (
    {
        "key": "sections16-18",
        "master": "ega4_sections16_18_source_aligned_successor_r1.tex",
        "sources": ("ega4-16.tex", "ega4-17.tex", "ega4-18.tex"),
        "checkpoint": "checkpoint_printed132_r34",
        "aligned_from": 5,
        "aligned_through": 132,
        "next_page": 133,
        "output": "EGA4_sections16_18_live_source_20260731T0526.pdf",
    },
    {
        "key": "sections19-21",
        "master": "ega4_sections19_21_source_aligned_successor_r1.tex",
        "sources": ("ega4-19.tex", "ega4-20.tex", "ega4-21.tex"),
        "checkpoint": "build_p185_251_r13",
        "aligned_from": 185,
        "aligned_through": 251,
        "next_page": 252,
        "output": "EGA4_sections19_21_live_source_20260731T0526.pdf",
    },
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def identity(path: Path) -> dict[str, object]:
    return {"bytes": path.stat().st_size, "sha256": sha256(path)}


def run(command: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=cwd,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )


def pdf_pages(path: Path) -> int:
    result = run(["pdfinfo", str(path)], path.parent)
    if result.returncode != 0:
        raise RuntimeError(f"pdfinfo failed for {path}: {result.stdout}")
    match = re.search(r"^Pages:\s+(\d+)\s*$", result.stdout, re.MULTILINE)
    if not match:
        raise RuntimeError(f"Could not parse page count for {path}")
    return int(match.group(1))


def scan_text(label: str, text: str) -> list[str]:
    return [f"{label}: {pattern.pattern}" for pattern in FORBIDDEN_TEXT if pattern.search(text)]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sections16-18-root", type=Path, required=True)
    parser.add_argument("--sections19-21-root", type=Path, required=True)
    parser.add_argument("--destination", type=Path, required=True)
    parser.add_argument("--captured-at", required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    roots = {
        "sections16-18": args.sections16_18_root.resolve(),
        "sections19-21": args.sections19_21_root.resolve(),
    }
    destination = args.destination.resolve()
    if destination.exists():
        raise RuntimeError(f"Destination already exists: {destination}")

    expected: dict[str, dict[str, object]] = {}
    source_paths: list[tuple[Path, Path]] = []
    for lane in LANES:
        root = roots[lane["key"]]
        for name in (lane["master"], "preamble.tex", "preamble-base.tex"):
            source = root / "build_harness" / name
            relative = (
                Path("lanes") / lane["key"] / "build_harness" / name
            )
            source_paths.append((source, relative))
        for name in lane["sources"]:
            source = root / "source" / "source_aligned" / name
            relative = (
                Path("lanes")
                / lane["key"]
                / "source"
                / "source_aligned"
                / name
            )
            source_paths.append((source, relative))

    for source, relative in source_paths:
        if not source.is_file():
            raise FileNotFoundError(source)
        expected[relative.as_posix()] = identity(source)

    destination.mkdir(parents=True)
    for source, relative in source_paths:
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)

    copy_mismatches: list[str] = []
    source_changed_during_capture: list[str] = []
    for source, relative in source_paths:
        key = relative.as_posix()
        copied = identity(destination / relative)
        after = identity(source)
        if copied != expected[key]:
            copy_mismatches.append(key)
        if after != expected[key]:
            source_changed_during_capture.append(key)
    if copy_mismatches or source_changed_during_capture:
        raise RuntimeError(
            "Unstable source capture: "
            f"copy={copy_mismatches}, changed={source_changed_during_capture}"
        )

    build_results: list[dict[str, object]] = []
    with tempfile.TemporaryDirectory(prefix="ega4_live_source_build_") as temp_name:
        temp_root = Path(temp_name)
        for lane in LANES:
            lane_source = destination / "lanes" / lane["key"]
            lane_temp = temp_root / lane["key"]
            shutil.copytree(lane_source, lane_temp)
            harness = lane_temp / "build_harness"
            outputs: list[str] = []
            returncodes: list[int] = []
            for _ in range(3):
                result = run(
                    [
                        "xelatex",
                        "-interaction=nonstopmode",
                        "-halt-on-error",
                        "-file-line-error",
                        lane["master"],
                    ],
                    harness,
                )
                returncodes.append(result.returncode)
                outputs.append(result.stdout)
            if any(returncodes):
                raise RuntimeError(
                    f"XeLaTeX failed for {lane['key']}: {returncodes}\n{outputs[-1]}"
                )
            combined = "\n".join(outputs)
            hard_hits = [pattern for pattern in HARD_TEX_PATTERNS if pattern in combined]
            if hard_hits:
                raise RuntimeError(f"Hard TeX diagnostics for {lane['key']}: {hard_hits}")
            built_pdf = harness / Path(lane["master"]).with_suffix(".pdf")
            output_pdf = destination / "checkpoints" / lane["output"]
            output_pdf.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(built_pdf, output_pdf)
            extracted = run(["pdftotext", str(output_pdf), "-"], output_pdf.parent)
            if extracted.returncode != 0:
                raise RuntimeError(f"pdftotext failed for {lane['key']}")
            pdf_text_hits = scan_text(lane["output"], extracted.stdout)
            if pdf_text_hits:
                raise RuntimeError(f"Reader process/privacy hits: {pdf_text_hits}")
            build_results.append(
                {
                    "scope": lane["key"],
                    "producer_checkpoint_bound": lane["checkpoint"],
                    "aligned_from_printed_page": lane["aligned_from"],
                    "aligned_through_printed_page": lane["aligned_through"],
                    "conservative_next_page": lane["next_page"],
                    "fresh_build_passes": 3,
                    "hard_tex_diagnostics": 0,
                    "pdf": lane["output"],
                    "pdf_pages": pdf_pages(output_pdf),
                    "pdf_bytes": output_pdf.stat().st_size,
                    "pdf_sha256": sha256(output_pdf),
                    "reader_process_or_private_hits": 0,
                }
            )

    privacy_hits: list[str] = []
    for path in destination.rglob("*"):
        if path.is_file() and path.suffix.lower() in {".tex", ".md", ".csv", ".json"}:
            privacy_hits.extend(
                scan_text(path.relative_to(destination).as_posix(), path.read_text(encoding="utf-8"))
            )
    if privacy_hits:
        raise RuntimeError(f"Privacy/process hits: {privacy_hits}")

    (destination / ".gitattributes").write_text("*.tex -text\n", encoding="ascii")
    readme = f"""# EGA IV Sections 16-21 live source custody snapshot

Captured at `{args.captured_at}` after exact pre/copy/post identity checks.
This directory preserves the current editable source closures for the two
active EGA IV Part 4 alignment lanes and provides fresh three-pass convenience
builds from those copied bytes.

## Conservative checkpoint boundary

- Sections 16-18: producer checkpoint `checkpoint_printed132_r34`, aligned
  through printed page 132; conservative next page 133.
- Sections 19-21: producer checkpoint `build_p185_251_r13`, aligned through
  printed page 251; conservative next page 252.

The copied source files were newer than one or both named producer checkpoints.
Those later bytes are preserved because they are valuable live work, and the
fresh builds prove a coherent TeX closure. This snapshot does not promote
alignment coverage beyond the conservative checkpoint boundaries above.

## Build and public-reader hygiene

Both copied source closures built in three XeLaTeX passes with zero hard TeX
diagnostics. Extracted PDF text has zero private-path, task-ID, model-name, or
project-process hits. The convenience readers contain mathematical content,
title, and contents only; no status or AI preface is injected.

## Authority and exclusions

The controlling authority is the 360-page NUMDAM EGA IV Part 4 PDF, SHA-256
`{AUTHORITY_SHA256}`. The authority PDF, source pixels, OCR bodies, raw logs,
auxiliary files, caches, and private process material are excluded here. The
actual high-detail source images are preserved separately on the existing EGA
Zenodo concept.

This is GitHub source survival and a buildable working snapshot. It is not a
complete EGA IV reader, critical edition, rights determination, peer review,
accessibility certification, or mathematical certification.
"""
    (destination / "README.md").write_text(readme, encoding="ascii")
    status = """# Public custody status

- Sections 16-18 checkpoint-backed alignment: printed pages 5-132.
- Sections 19-21 checkpoint-backed alignment: printed pages 185-251.
- Later live editable bytes: preserved without a stronger coverage claim.
- Editable source closure: included for Sections 16-21.
- Fresh convenience builds: included; three XeLaTeX passes each.
- Reader-facing AI/process prose: none.
- Authority scan, pixels, OCR, raw logs, and auxiliaries: excluded.
- Complete EGA IV or exhaustive reference-v2 claim: no.
- Classification: public GitHub live source survival plus fresh build closure.
- Zenodo mutation: none.
- Rights: no blanket license grant asserted.
"""
    (destination / "STATUS_PUBLIC.md").write_text(status, encoding="ascii")

    represented: list[dict[str, object]] = []
    role_map = {
        ".gitattributes": "byte_preservation_control",
        "README.md": "public_scope_and_caveat",
        "STATUS_PUBLIC.md": "public_status",
    }
    for path in sorted(destination.rglob("*"), key=lambda item: item.as_posix()):
        if not path.is_file() or path.name in {"SHA256SUMS.csv", "CUSTODY_VALIDATION.json"}:
            continue
        relative = path.relative_to(destination).as_posix()
        if relative.startswith("checkpoints/"):
            role = "fresh_snapshot_build"
        elif "/source/source_aligned/" in relative:
            role = "editable_source"
        elif "/build_harness/" in relative:
            role = "build_dependency"
        else:
            role = role_map[relative]
        represented.append(
            {
                "path": relative,
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
                "role": role,
                "status": "github_live_custody",
            }
        )

    manifest_path = destination / "SHA256SUMS.csv"
    with manifest_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=("path", "bytes", "sha256", "role", "status")
        )
        writer.writeheader()
        writer.writerows(represented)

    validation = {
        "status": "PASS_GITHUB_LIVE_SOURCE_AND_FRESH_BUILD_CUSTODY",
        "checked_at": datetime.now().astimezone().isoformat(),
        "captured_at": args.captured_at,
        "package_files": len(represented) + 2,
        "represented_files": len(represented),
        "manifest": {
            "rows": len(represented),
            "bytes": manifest_path.stat().st_size,
            "sha256": sha256(manifest_path),
            "exact": True,
        },
        "authority": {
            "description": "NUMDAM EGA IV Part 4 PDF",
            "pages": 360,
            "sha256": AUTHORITY_SHA256,
            "included": False,
        },
        "lanes": build_results,
        "gates": {
            "source_copy_mismatches": len(copy_mismatches),
            "source_changed_during_capture": len(source_changed_during_capture),
            "manifest_exact": True,
            "privacy_or_process_hits": len(privacy_hits),
            "authority_files_included": 0,
            "source_pixels_included": 0,
            "ocr_bodies_included": 0,
            "private_logs_included": 0,
            "raw_build_intermediates_included": 0,
        },
        "classification": "public_github_live_source_survival_plus_fresh_build_closure",
        "complete_ega4_claim": False,
        "zenodo_mutation": False,
        "errors": [],
    }
    (destination / "CUSTODY_VALIDATION.json").write_text(
        json.dumps(validation, ensure_ascii=True, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(validation, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
