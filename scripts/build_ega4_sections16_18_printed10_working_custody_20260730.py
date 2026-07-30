#!/usr/bin/env python3
"""Build a privacy-clean GitHub custody snapshot for active EGA IV 16-18."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import shutil
import subprocess
import tempfile
from datetime import datetime
from pathlib import Path

import fitz


AUTHORITY_SHA256 = (
    "B4277FB99C6EDF8FEEC5B01F54368E4B8521BCD52871316C0EDF6FF4AE69389E"
)
PRIVATE_MARKERS = (
    "c:\\users\\",
    "c:/users/",
    "appdata",
    "papors",
    "chatnotes",
    ".claude",
    ".codex",
)
COPY_PATHS = (
    "STATUS.md",
    "LOGBOOK.md",
    "build_harness/ega4_sections16_18_source_aligned_successor_r1.tex",
    "build_harness/preamble-base.tex",
    "build_harness/preamble.tex",
    "controls/SOURCE_ALIGNMENT_PROGRESS.csv",
    "source/source_aligned/ega4-16.tex",
    "source/source_aligned/ega4-17.tex",
    "source/source_aligned/ega4-18.tex",
)
PREDECESSOR_HASHES = {
    "source/source_aligned/ega4-16.tex": (
        "AF07AD719C55502159F525428CA43F8768A95B2FA5B71A460026ADF5017D1638"
    ),
    "source/source_aligned/ega4-17.tex": (
        "AF1F4E01C8176100BA83332EDCF0411B5B8613D969DF7A5C365DD351C50B1DFB"
    ),
    "source/source_aligned/ega4-18.tex": (
        "9874F3A55EA9A857AB91F5F339643F1C8A0FC1056C649533C274989818E46713"
    ),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--destination-root", type=Path, required=True)
    parser.add_argument("--captured-at", required=True)
    return parser.parse_args()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def identity(path: Path) -> tuple[int, str]:
    return path.stat().st_size, sha256(path)


def write_text(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(value)


def write_json(path: Path, value: object) -> None:
    write_text(path, json.dumps(value, indent=2, ensure_ascii=True) + "\n")


def scan_privacy(root: Path) -> list[str]:
    hits: list[str] = []
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        if path.suffix.lower() not in {".md", ".tex", ".csv", ".json", ""}:
            continue
        text = path.read_text(encoding="utf-8", errors="replace").lower()
        for marker in PRIVATE_MARKERS:
            if marker in text:
                hits.append(f"{path.relative_to(root).as_posix()}:{marker}")
    return hits


def isolated_build(destination: Path, captured_at: str) -> dict[str, object]:
    master = "ega4_sections16_18_source_aligned_successor_r1.tex"
    harness = destination / "build_harness"
    with tempfile.TemporaryDirectory(prefix="ega4_16_18_custody_") as temp_name:
        temp = Path(temp_name)
        command = [
            "xelatex",
            "-interaction=nonstopmode",
            "-halt-on-error",
            f"-output-directory={temp}",
            master,
        ]
        environment = os.environ.copy()
        environment.update(
            {
                "SOURCE_DATE_EPOCH": str(
                    int(datetime.fromisoformat(captured_at).timestamp())
                ),
                "FORCE_SOURCE_DATE": "1",
                "TZ": "UTC",
            }
        )
        result = subprocess.run(
            command,
            cwd=harness,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
            env=environment,
        )
        pdf = temp / Path(master).with_suffix(".pdf")
        if result.returncode != 0 or not pdf.is_file():
            tail = result.stdout.decode("utf-8", errors="replace")[-2000:]
            raise RuntimeError(f"Isolated XeLaTeX build failed: {tail}")
        with fitz.open(pdf) as document:
            pages = document.page_count
        console = result.stdout.decode("utf-8", errors="replace")
        return {
            "exit_code": result.returncode,
            "pages": pages,
            "hard_error_markers": sum(
                line.startswith("!") for line in console.splitlines()
            ),
            "source_date_epoch": environment["SOURCE_DATE_EPOCH"],
            "output_included": False,
        }


def main() -> None:
    args = parse_args()
    source = args.source_root.resolve()
    destination = args.destination_root.resolve()
    if not source.is_dir():
        raise FileNotFoundError(source)
    if destination.exists():
        shutil.rmtree(destination)
    destination.mkdir(parents=True)

    source_paths = [source / relative for relative in COPY_PATHS]
    missing = [str(path) for path in source_paths if not path.is_file()]
    if missing:
        raise FileNotFoundError(missing)
    before = {path: identity(path) for path in source_paths}
    for relative, source_path in zip(COPY_PATHS, source_paths, strict=True):
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source_path, target)
    after = {path: identity(path) for path in source_paths}
    copy_stable = before == after
    copy_mismatches = [
        relative
        for relative, source_path in zip(COPY_PATHS, source_paths, strict=True)
        if identity(destination / relative) != before[source_path]
    ]
    if not copy_stable or copy_mismatches:
        raise RuntimeError(
            {"source_changed": not copy_stable, "copy_mismatches": copy_mismatches}
        )

    write_text(destination / ".gitattributes", "* -text\n")
    build = isolated_build(destination, args.captured_at)
    changed_from_predecessor = [
        path
        for path, predecessor_hash in PREDECESSOR_HASHES.items()
        if sha256(destination / path) != predecessor_hash
    ]

    copied_bytes = sum((destination / path).stat().st_size for path in COPY_PATHS)
    readme = f"""# EGA IV Sections 16-18 active source custody through printed page 10

This directory preserves an exact, privacy-clean snapshot of the active
no-overwrite EGA IV Sections 16-18 English source-alignment successor at
`{args.captured_at}`.

## Scope and cursor

Printed pages 5-10 / authority physical pages 4-9 are source-aligned. The next
authority page is printed page 11 / physical page 10, continuing the proof of
Proposition 16.2.2 at `source/source_aligned/ega4-16.tex` line 278. Sections
17-18 are retained as inherited build closure and are not promoted as newly
source-aligned by this snapshot.

The checkpoint corrects, among other inherited defects, a lost exponent in
`I/I^{{n+1}}`, `I^n=I^{{n+1}}`, the containment direction around `Y`, the
coefficient ring `O_{{Y'}}` in diagram (16.2.1.4), and the tensor factor `1`
in `Gr(u)=gr(u)\\otimes 1`. The authority's visibly reversed transition-map
indices at 16.1.9(b) are documented in a TeX comment rather than silently
attributed to the source-alignment process.

## Authority and contents

The controlling EGA IV Part 4 PDF has SHA-256
`{AUTHORITY_SHA256}`. The authority PDF and all page/crop pixels are excluded.
Direct authority images decide readings; existing OCR is locator/drafting
material only.

The nine copied source, harness, progress, and logbook files total
{copied_bytes:,} bytes. Their relative layout is retained, and
`SHA256SUMS.csv` identifies every other file in this directory. Only
`source/source_aligned/ega4-16.tex` differs from the preceding public EGA IV
Sections 11-21 custody closure.

The copied source builds in an isolated one-pass XeLaTeX replay to
{build['pages']} pages with exit code 0. The disposable PDF and console output
are not included. The active producer checkpoint remains a three-pass,
121-page PDF with SHA-256
`EE8147A87CC2AF28B45BF9720D77AA1922E95CDD8CC38DB40E71E7C758AFBABC`.

This is GitHub source-survival custody, not a reader release, Sections 16-18
completion claim, critical edition, rights clearance, accessibility review,
or exhaustive reference-v2 certification. The EGA Zenodo record is unchanged.
"""
    write_text(destination / "README.md", readme)

    privacy_hits = scan_privacy(destination)
    validation = {
        "schema": "ega_working_source_custody_v1",
        "status": "PASS_SOURCE_CUSTODY_ONLY" if not privacy_hits else "FAIL",
        "captured_at": args.captured_at,
        "scope": (
            "EGA IV Sections 16-18 active source tree; documented source-"
            "alignment gate through printed page 10; next authority page 11"
        ),
        "authority_sha256": AUTHORITY_SHA256,
        "copied_files": len(COPY_PATHS),
        "copied_bytes": copied_bytes,
        "changed_files_from_preceding_public_closure": changed_from_predecessor,
        "copy_source_stable_during_capture": copy_stable,
        "copy_hash_mismatches": len(copy_mismatches),
        "privacy_scan_hits": len(privacy_hits),
        "authority_files_included": 0,
        "qa_images_included": 0,
        "raw_build_logs_included": 0,
        "reader_pdf_included": False,
        "isolated_one_pass_build": build,
        "active_three_pass_build_pages": 121,
        "active_three_pass_build_bytes": 826688,
        "active_three_pass_build_sha256": (
            "EE8147A87CC2AF28B45BF9720D77AA1922E95CDD8CC38DB40E71E7C758AFBABC"
        ),
        "release_authorized": False,
        "zenodo_mutation_requested": False,
        "errors": privacy_hits,
    }
    write_json(destination / "CUSTODY_VALIDATION.json", validation)
    if validation["status"] != "PASS_SOURCE_CUSTODY_ONLY":
        raise RuntimeError(validation)

    manifest_path = destination / "SHA256SUMS.csv"
    rows = []
    for path in sorted(
        (item for item in destination.rglob("*") if item.is_file()),
        key=lambda item: item.relative_to(destination).as_posix().casefold(),
    ):
        if path == manifest_path:
            continue
        rows.append(
            {
                "path": path.relative_to(destination).as_posix(),
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
        )
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["path", "bytes", "sha256"],
            lineterminator="\n",
            quoting=csv.QUOTE_ALL,
        )
        writer.writeheader()
        writer.writerows(rows)

    summary = {
        "status": validation["status"],
        "files": len(rows) + 1,
        "bytes": sum(path.stat().st_size for path in destination.rglob("*") if path.is_file()),
        "manifest_rows": len(rows),
        "manifest_bytes": manifest_path.stat().st_size,
        "manifest_sha256": sha256(manifest_path),
        "changed_files": changed_from_predecessor,
        "isolated_build": build,
    }
    print(json.dumps(summary, indent=2, ensure_ascii=True))


if __name__ == "__main__":
    main()
