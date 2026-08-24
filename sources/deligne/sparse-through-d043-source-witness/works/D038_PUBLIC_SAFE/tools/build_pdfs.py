#!/usr/bin/env python3
"""Compile all canonical TeX sources twice and require byte identity."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import pathlib
import re
import shutil
import subprocess

from pypdf import PdfReader


TEX_NAMES = (
    "D038_SOURCE_LANGUAGE_CANONICAL.tex",
    "D038_ENGLISH_CANONICAL.tex",
    "D038_RESTRAINED_APPARATUS.tex",
)
EXPECTED_PAGES = 58
SOURCE_DATE_EPOCH = "1787529600"


def sha256_file(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def compile_run(candidate: pathlib.Path, run_dir: pathlib.Path, engine: str) -> dict[str, pathlib.Path]:
    if run_dir.exists():
        shutil.rmtree(run_dir)
    run_dir.mkdir(parents=True)
    for tex_name in TEX_NAMES:
        shutil.copyfile(candidate / tex_name, run_dir / tex_name)
    shutil.copytree(candidate / "assets", run_dir / "assets")
    env = dict(os.environ)
    env.update(
        {
            "SOURCE_DATE_EPOCH": SOURCE_DATE_EPOCH,
            "FORCE_SOURCE_DATE": "1",
            "TZ": "UTC",
            "LC_ALL": "C",
        }
    )
    outputs: dict[str, pathlib.Path] = {}
    for tex_name in TEX_NAMES:
        command = [
            engine,
            "--interaction=nonstopmode",
            "--halt-on-error",
            "--file-line-error",
            tex_name,
        ]
        for pass_number in (1, 2):
            result = subprocess.run(
                command,
                cwd=run_dir,
                env=env,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                encoding="utf-8",
                errors="replace",
                check=False,
            )
            (run_dir / f"{pathlib.Path(tex_name).stem}.pass{pass_number}.stdout.txt").write_text(
                result.stdout, encoding="utf-8", newline="\n"
            )
            if result.returncode:
                raise RuntimeError(f"{engine} failed for {tex_name} pass {pass_number}\n{result.stdout[-5000:]}")
        log = (run_dir / pathlib.Path(tex_name).with_suffix(".log")).read_text(encoding="utf-8", errors="replace")
        forbidden = [
            r"^! ",
            r"Missing character:",
            r"Overfull \\[hv]box",
            r"TeX capacity exceeded",
            r"Emergency stop",
        ]
        for pattern in forbidden:
            if re.search(pattern, log, flags=re.MULTILINE):
                raise RuntimeError(f"forbidden TeX diagnostic {pattern!r} in {tex_name}")
        pdf = run_dir / pathlib.Path(tex_name).with_suffix(".pdf")
        reader = PdfReader(str(pdf))
        if len(reader.pages) != EXPECTED_PAGES:
            raise RuntimeError(f"page count {len(reader.pages)} for {pdf.name}; expected {EXPECTED_PAGES}")
        outputs[pdf.name] = pdf
    return outputs


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=pathlib.Path, required=True)
    parser.add_argument("--engine", default="lualatex")
    args = parser.parse_args()
    root = args.root.resolve()
    candidate = root / "candidate"
    build = root / "build"
    manifests = root / "manifests"
    run_a = compile_run(candidate, build / "run_a", args.engine)
    run_b = compile_run(candidate, build / "run_b", args.engine)

    outputs = []
    for name in sorted(run_a):
        hash_a = sha256_file(run_a[name])
        hash_b = sha256_file(run_b[name])
        if hash_a != hash_b or run_a[name].read_bytes() != run_b[name].read_bytes():
            raise RuntimeError(f"nondeterministic PDF build: {name}")
        final_path = candidate / name
        shutil.copyfile(run_a[name], final_path)
        reader = PdfReader(str(final_path))
        media = []
        for page in reader.pages:
            box = page.mediabox
            media.append((round(float(box.width), 3), round(float(box.height), 3)))
        if set(media) != {(461.0, 684.0)}:
            raise RuntimeError(f"unexpected page geometry in {name}: {sorted(set(media))}")
        outputs.append(
            {
                "path": final_path.relative_to(root).as_posix(),
                "bytes": final_path.stat().st_size,
                "sha256": sha256_file(final_path),
                "pages": len(reader.pages),
                "media_box_points": [461.0, 684.0],
                "run_a_sha256": hash_a,
                "run_b_sha256": hash_b,
                "byte_identical_runs": True,
            }
        )

    tex_outputs = []
    for name in TEX_NAMES:
        path = candidate / name
        tex_outputs.append(
            {
                "path": path.relative_to(root).as_posix(),
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
                "canonical_page_markers": path.read_text(encoding="utf-8").count("% CANONICAL_PAGE "),
            }
        )
    receipt = {
        "schema": "d038-deterministic-build-v1",
        "status": "PASS",
        "engine": args.engine,
        "source_date_epoch": SOURCE_DATE_EPOCH,
        "build_runs": ["build/run_a", "build/run_b"],
        "pdf_outputs": outputs,
        "tex_outputs": tex_outputs,
        "deterministic_pdf_byte_identity": True,
    }
    receipt_path = manifests / "BUILD_RECEIPT.json"
    receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print("PASS_DETERMINISTIC_BUILD")


if __name__ == "__main__":
    main()
