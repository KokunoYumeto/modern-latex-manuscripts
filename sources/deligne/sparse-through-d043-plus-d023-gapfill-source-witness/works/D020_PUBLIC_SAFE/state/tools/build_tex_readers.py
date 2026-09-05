#!/usr/bin/env python3
from __future__ import annotations

import json
import pathlib
import re
import sys


LAYERS = {
    "source_language": ("French diplomatic edition", "fr"),
    "english_standalone": ("Standalone English edition", "en"),
    "apparatus": ("Restrained apparatus", "en"),
}


def escape(text: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "{": r"\{",
        "}": r"\}",
        "#": r"\#",
        "$": r"\$",
        "%": r"\%",
        "&": r"\&",
        "_": r"\_",
        "^": r"\textasciicircum{}",
        "~": r"\textasciitilde{}",
    }
    pieces: list[str] = []
    for char in text:
        if 0x1D400 <= ord(char) <= 0x1D7FF:
            rendered = r"{\mathtext " + char + "}"
        else:
            rendered = replacements.get(char, char)
        pieces.append(rendered)
        if char in "=,;:+-·→↪↩∩⊗⊕/)]":
            pieces.append(r"\allowbreak{}")
    escaped = "".join(pieces)
    return re.sub(
        r"(?<![0-9A-F])([0-9A-F]{32,})(?![0-9A-F])",
        lambda match: r"\seqsplit{" + match.group(1) + "}",
        escaped,
    )


def render_text(text: str) -> str:
    blocks = []
    for paragraph in re.split(r"\n\s*\n", text.strip()):
        lines = paragraph.splitlines()
        escaped = [escape(line) for line in lines]
        if len(lines) > 1 and any(token in paragraph for token in ("|σ", "|f", "|\n", "->", "<-")):
            body = r" \\{} ".join(escaped)
            blocks.append(r"\begin{center}\mathtext\small " + body + r"\end{center}")
        elif len(lines) > 1:
            blocks.append(r"\begin{quote}\raggedright " + r" \\{} ".join(escaped) + r"\end{quote}")
        elif re.match(r"^(\(?8\.|H_|#|\||T\^|R\^|χ|Σ|X_|Q\s*=|f\(|\[\d\]|SGA|Manuscrit)", paragraph):
            blocks.append(r"\begin{quote}\raggedright\mathtext " + escaped[0] + r"\end{quote}")
        else:
            blocks.append(r"\noindent\raggedright " + escaped[0] + r"\par")
    return "\n\n".join(blocks)


def render_asset(asset: dict) -> str:
    raw_path = "../" + str(asset["raw_path"]).replace("\\", "/")
    presentation_path = "../" + str(asset["presentation_path"]).replace("\\", "/")
    caption = escape(str(asset["caption"]))
    asset_id = escape(str(asset["id"]))
    return (
        r"\begin{center}"
        + "\n"
        + r"\begin{minipage}{0.47\textwidth}\centering"
        + "\n"
        + r"\includegraphics[width=\linewidth]{" + raw_path + "}"
        + r"\\{\scriptsize Raw authority crop}"
        + "\n"
        + r"\end{minipage}\hfill"
        + "\n"
        + r"\begin{minipage}{0.47\textwidth}\centering"
        + "\n"
        + r"\includegraphics[width=\linewidth]{" + presentation_path + "}"
        + r"\\{\scriptsize Conservative presentation derivative}"
        + "\n"
        + r"\end{minipage}"
        + "\n\n"
        + r"{\small " + asset_id + ": " + caption + "}"
        + "\n"
        + r"\end{center}"
    )


def render_record(record: dict) -> str:
    remaining = str(record["text"])
    rendered: list[str] = []
    for asset in record.get("assets", []):
        marker = str(asset.get("placement_after", ""))
        if marker and marker in remaining:
            split_at = remaining.index(marker) + len(marker)
            rendered.append(render_text(remaining[:split_at]))
            rendered.append(render_asset(asset))
            remaining = remaining[split_at:]
        else:
            rendered.append(render_asset(asset))
    if remaining.strip():
        rendered.append(render_text(remaining))
    return "\n\n".join(rendered)


def main() -> None:
    root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    out = root / "tex"
    out.mkdir(parents=True, exist_ok=True)
    for layer, (subtitle, lang) in LAYERS.items():
        records = [
            json.loads(line)
            for line in (root / "edition" / f"{layer}.ndjson").read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        shown = [
            record
            for record in records
            if record["status"] in ("frozen", "accepted")
            and (layer == "apparatus" or record["disposition"] == "INCLUDE_ARTICLE")
        ]
        title = "Pierre Deligne - La conjecture de Weil I" if layer != "english_standalone" else "Pierre Deligne - The Weil Conjecture I"
        body = []
        for record in shown:
            physical = int(record["physical_page"])
            printed = int(record["printed_page"])
            label = (
                f"Authority physical page {physical} - repository-cover boundary disposition"
                if printed == 0
                else f"Printed page {printed} - authority physical page {physical}"
            )
            body.append(r"\section*{" + escape(label) + r"}\addcontentsline{toc}{section}{" + escape(label) + "}")
            body.append(render_record(record))
            body.append(r"\clearpage")
        source = r"""\documentclass[10pt]{article}
\usepackage[a4paper,margin=24mm,headheight=14pt]{geometry}
\usepackage{fontspec}
\setmainfont{DejaVu Sans}
\newfontfamily\mathtext{Cambria Math}
\usepackage{graphicx}
\usepackage{fancyhdr}
\usepackage[hidelinks]{hyperref}
\usepackage{microtype}
\usepackage{seqsplit}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.55em}
\setlength{\emergencystretch}{4em}
\pagestyle{fancy}
\fancyhf{}
\lhead{""" + escape(title) + r"""}
\rhead{""" + escape(subtitle) + r"""}
\cfoot{\thepage}
\begin{document}
\begin{titlepage}
\centering
{\Large """ + escape(title) + r"""\par}
\vspace{1.5cm}
{\LARGE """ + escape(subtitle) + r"""\par}
\vfill
{\small Authority-addressed cumulative edition: 36 physical dispositions / 35 article pages.\par}
\end{titlepage}
\tableofcontents
\clearpage
""" + "\n\n".join(body) + r"""
\end{document}
"""
        (out / f"{layer}.tex").write_text(source, encoding="utf-8", newline="\n")
    print(json.dumps({"result": "PASS", "tex_files": len(LAYERS)}, sort_keys=True))


if __name__ == "__main__":
    main()
