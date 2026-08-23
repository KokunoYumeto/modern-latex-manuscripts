#!/usr/bin/env python3
"""Build the bounded D036 French, English, and apparatus PDF/TeX editions.

The input is the immutable extracted web-session packet.  Authority pixels and
frozen NDJSON records are never modified.  All generated files are written to
the explicit output directory.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any


WORK_ID = "D036"
AUTHORITY_SHA256 = "278125A52E24555349D7A7B56A5EE828FF2BC1952F752969B20E7BDD8228A74D"
PACKET_SHA256 = "E6DB9439BC4730513768CF526AE0E67DCB659AF6379006CDA5CABFB44594F55E"
SOURCE_DATE_EPOCH = "312768000"  # 1979-11-30T00:00:00Z


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest().upper()


def load_escape_helper(script_dir: Path):
    helper_path = script_dir / "tools" / "unicode_math_escape_reference.py"
    spec = importlib.util.spec_from_file_location("d036_unicode_math_helper", helper_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load helper {helper_path.name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.MATH_SYMBOLS.update("↠⇔∀∅∨≠")
    return module


def read_records(packet_root: Path, filename: str) -> list[dict[str, Any]]:
    path = packet_root / "edition" / filename
    records = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    pages = [int(row["authority_pdf_page"]) for row in records]
    if pages != list(range(1, 11)):
        raise ValueError(f"{filename}: expected authority pages 1..10, got {pages}")
    for row in records:
        if row.get("status") != "COMPLETE" or row.get("source_pdf_sha256") != AUTHORITY_SHA256:
            raise ValueError(f"{filename}: incomplete or wrong authority binding on page {row.get('authority_pdf_page')}")
    return records


def normalize_math_fragments(text: str) -> str:
    replacements = {
        "⁻¹": "^{-1}",
        "⁻": "^{-}",
        "²": "^2",
        "¹": "^1",
        "³": "^3",
        "ᵐ": "^m",
        "ⁿ": "^n",
        "ʳ": "^r",
        "ⁱ": "^i",
        "ᴺ": "^N",
        "ᵢ": "_i",
        "ᵣ": "_r",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = re.sub(r"([A-Za-z])\u0304", lambda match: r"\bar{" + match.group(1) + "}", text)
    return text


def escape_line(helper, line: str) -> str:
    return helper.escape_text(normalize_math_fragments(line))


ASSET_MAP = {
    "P08-A01": "assets/P08-A01_three_stage_compactification_present.png",
    "P09-A01": "assets/P09-A01_local_perpendicular_present.png",
}


def render_asset(asset_id: str) -> str:
    rel = ASSET_MAP.get(asset_id)
    if rel is None:
        raise ValueError(f"unknown asset placeholder {asset_id}")
    return (
        r"\begin{center}\begin{adjustbox}{max width=0.96\linewidth,max height=0.25\textheight}"
        r"\includegraphics{"
        + rel.replace("\\", "/")
        + r"}\end{adjustbox}\end{center}"
    )


def render_record(helper, record: dict[str, Any], layer: str) -> str:
    page = int(record["authority_pdf_page"])
    folio = str(record["printed_folio"])
    blocks: list[str] = []
    if page > 1:
        blocks.append(r"\newpage")
    blocks.extend(
        [
            r"\noindent\begin{adjustbox}{max totalsize={\textwidth}{0.945\textheight},center}",
            r"\begin{minipage}{\textwidth}",
            rf"\noindent\hfill\scriptsize Authority physical page {page} / printed folio {folio}\par\normalsize",
        ]
    )

    text = str(record.get("text", ""))
    used_assets: set[str] = set()
    paragraphs = text.split("\n\n")
    for index, paragraph in enumerate(paragraphs):
        stripped = paragraph.strip()
        if not stripped:
            continue
        if stripped.startswith("[[ASSET:") and stripped.endswith("]]" ):
            asset_id = stripped[len("[[ASSET:") : -2]
            blocks.append(render_asset(asset_id))
            used_assets.add(asset_id)
            continue
        lines = [escape_line(helper, line) for line in stripped.splitlines()]
        joined = r"\\".join(lines)
        if page == 1 and layer != "apparatus" and index <= 3:
            style = r"\bfseries " if index == 1 else ""
            blocks.append(r"\begin{center}" + style + joined + r"\end{center}")
        else:
            blocks.append(r"\noindent " + joined + r"\par\smallskip")

    for asset in record.get("assets", []):
        asset_id = str(asset.get("id", ""))
        if asset_id and asset_id not in used_assets:
            blocks.append(render_asset(asset_id))

    blocks.extend([r"\end{minipage}", r"\end{adjustbox}"])
    return "\n".join(blocks)


def preamble(title: str, language: str, layer: str) -> str:
    babel = "french" if language == "fr" else "english"
    fontsize = "8.05" if layer != "apparatus" else "8.7"
    leading = "9.15" if layer != "apparatus" else "10.0"
    return rf"""% D036 canonical bounded edition generated from frozen packet records.
% Controlling authority SHA-256: {AUTHORITY_SHA256}.
\documentclass[10pt,a4paper]{{article}}
\usepackage{{fontspec}}
\usepackage{{unicode-math}}
\setmainfont{{Latin Modern Roman}}
\setsansfont{{Latin Modern Sans}}
\setmonofont{{Latin Modern Mono}}
\setmathfont{{Latin Modern Math}}
\usepackage{{amsmath,mathtools,graphicx,adjustbox,geometry,microtype,hyperref,bookmark}}
\usepackage[{babel}]{{babel}}
\geometry{{top=13mm,bottom=13mm,left=13mm,right=13mm}}
\hypersetup{{hidelinks,pdftitle={{{title}}},pdfauthor={{Pierre Deligne}},pdfcreator={{D036 canonical XeLaTeX builder}},pdfproducer={{XeTeX}},pdfcreationdate={{D:19791101000000Z}},pdfmoddate={{D:19791101000000Z}}}}
\pagestyle{{empty}}
\setlength{{\parindent}}{{0pt}}
\setlength{{\parskip}}{{0.10em}}
\setlength{{\emergencystretch}}{{3em}}
\tolerance=2500
\hfuzz=1.5pt
\raggedbottom
\begin{{document}}
\fontsize{{{fontsize}}}{{{leading}}}\selectfont
"""


def write_tex(out_dir: Path, helper, name: str, title: str, language: str, layer: str, records: list[dict[str, Any]]) -> Path:
    body = "\n".join(render_record(helper, row, layer) for row in records)
    path = out_dir / name
    path.write_text(preamble(title, language, layer) + body + "\n\\end{document}\n", encoding="utf-8", newline="\n")
    return path


def run_xelatex(tex: Path) -> None:
    env = os.environ.copy()
    env["SOURCE_DATE_EPOCH"] = SOURCE_DATE_EPOCH
    for pass_number in (1, 2):
        proc = subprocess.run(
            ["xelatex", "-interaction=nonstopmode", "-halt-on-error", "-file-line-error", "-no-shell-escape", tex.name],
            cwd=tex.parent,
            env=env,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            encoding="utf-8",
            errors="replace",
            timeout=300,
        )
        (tex.parent / f"{tex.stem}.pass{pass_number}.log.txt").write_text(proc.stdout, encoding="utf-8", newline="\n")
        if proc.returncode != 0:
            raise RuntimeError(f"XeLaTeX failed for {tex.name}, pass {pass_number}\n{proc.stdout[-5000:]}")


def main() -> int:
    if len(sys.argv) != 3:
        print(f"usage: {Path(sys.argv[0]).name} PACKET_ROOT OUTPUT_DIR", file=sys.stderr)
        return 2
    packet_root = Path(sys.argv[1]).resolve()
    out_dir = Path(sys.argv[2]).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    helper = load_escape_helper(Path(__file__).resolve().parent)

    layers = [
        ("source_french.ndjson", "D036_FR.tex", "Le groupe fondamental du complement d'une courbe plane", "fr", "source"),
        ("english_translation.ndjson", "D036_EN.tex", "The Fundamental Group of the Complement of a Plane Curve", "en", "english"),
        ("apparatus.ndjson", "D036_APPARATUS.tex", "D036 Authority Replay Apparatus", "en", "apparatus"),
    ]
    tex_files: list[Path] = []
    for filename, tex_name, title, language, layer in layers:
        tex_files.append(write_tex(out_dir, helper, tex_name, title, language, layer, read_records(packet_root, filename)))

    assets_out = out_dir / "assets"
    assets_out.mkdir(exist_ok=True)
    for source_name, target_name in [
        ("P08-A01_three_stage_compactification_present.png", "P08-A01_three_stage_compactification_present.png"),
        ("P09-A01_local_perpendicular_present.png", "P09-A01_local_perpendicular_present.png"),
    ]:
        shutil.copy2(Path(__file__).resolve().parent / "assets" / source_name, assets_out / target_name)

    for tex in tex_files:
        run_xelatex(tex)

    authority_source = packet_root / "source" / "20_AUTHORITY_DELIGNE_D036_NUMBER39_10PP.pdf"
    authority_output = out_dir / authority_source.name
    shutil.copy2(authority_source, authority_output)
    if sha256(authority_output) != AUTHORITY_SHA256:
        raise RuntimeError("authority hash mismatch")

    from pypdf import PdfReader

    receipt: dict[str, Any] = {
        "schema": "deligne-d036-canonical-build-v1",
        "status": "PASS",
        "work_id": WORK_ID,
        "packet_sha256": PACKET_SHA256,
        "authority": {"filename": authority_output.name, "bytes": authority_output.stat().st_size, "pages": len(PdfReader(str(authority_output)).pages), "sha256": sha256(authority_output)},
        "outputs": {},
    }
    for tex in tex_files:
        pdf = tex.with_suffix(".pdf")
        receipt["outputs"][tex.name] = {"bytes": tex.stat().st_size, "sha256": sha256(tex)}
        receipt["outputs"][pdf.name] = {"bytes": pdf.stat().st_size, "pages": len(PdfReader(str(pdf)).pages), "sha256": sha256(pdf)}
    (out_dir / "BUILD_RECEIPT.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(receipt, ensure_ascii=True, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
