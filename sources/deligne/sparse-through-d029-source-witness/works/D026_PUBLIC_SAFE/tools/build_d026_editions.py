#!/usr/bin/env python3
"""Build the independently maintained D026 French and English TeX editions.

The terminal web-session HTML is never used as a reader source.  This builder
reads the frozen page records, validates their authority identity and topology,
escapes only prose, and preserves the already semantic TeX mathematics and
diagrams as editable source.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


WORK_ID = "DELIGNE_D026_LOCAL_CONSTANTS_ARTIN_ORTHOGONAL"
AUTHORITY_SHA256 = "9951F00E4E8E2673ABBAFB44D28B03FA31A45E60EF03BCFE6DA0A5E102167FC6"
EXPECTED_PAGES = list(range(1, 19))
EXPECTED_FOLIOS = list(range(299, 317))


def read_ndjson(path: Path) -> list[dict]:
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    pages = [int(row["authority_pdf_page"]) for row in rows]
    folios = [int(row["paper_folio"]) for row in rows]
    if pages != EXPECTED_PAGES:
        raise ValueError(f"{path.name}: expected authority pages 1-18, found {pages}")
    if folios != EXPECTED_FOLIOS:
        raise ValueError(f"{path.name}: expected printed folios 299-316, found {folios}")
    for row in rows:
        if row.get("source_sha256", "").upper() != AUTHORITY_SHA256:
            raise ValueError(f"{path.name}: authority mismatch on page {row['authority_pdf_page']}")
        if row.get("disposition") != "INCLUDE_AUTHORITY_PAGE":
            raise ValueError(f"{path.name}: excluded page {row['authority_pdf_page']}")
    return rows


SPECIALS = {
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
    "\\": r"\textbackslash{}",
}


def escape_prose(text: str) -> str:
    """Escape TeX prose while retaining typographic source characters."""
    text = text.replace("\u2011", "-").replace("\u2013", "--").replace("\u2014", "---")
    text = text.replace("\u2026", r"\ldots{}")
    return "".join(SPECIALS.get(char, char) for char in text)


MATH_RE = re.compile(r"(\\\((?:.|\n)*?\\\)|\\\[(?:.|\n)*?\\\])", re.DOTALL)


def render_mixed(text: str) -> str:
    pieces = MATH_RE.split(text)
    rendered: list[str] = []
    for piece in pieces:
        if not piece:
            continue
        if (piece.startswith(r"\(") and piece.endswith(r"\)")) or (
            piece.startswith(r"\[") and piece.endswith(r"\]")
        ):
            rendered.append(piece)
        else:
            leading_space = bool(re.match(r"\s", piece))
            trailing_space = bool(re.search(r"\s$", piece))
            normalized = re.sub(r"\s+", " ", piece.strip())
            escaped = escape_prose(normalized)
            rendered.append((" " if leading_space else "") + escaped + (" " if trailing_space else ""))
    return "".join(rendered)


def render_page(text: str, language: str, authority_page: int) -> str:
    blocks = [block.strip() for block in re.split(r"\n\s*\n", text.strip()) if block.strip()]
    out: list[str] = []
    for index, block in enumerate(blocks):
        if authority_page == 1 and index == 0:
            title_lines = [escape_prose(line.strip()) for line in block.splitlines() if line.strip()]
            out.append(r"\begin{center}\fontsize{15}{17}\selectfont\bfseries " + r"\\".join(title_lines) + r"\end{center}")
            continue
        if authority_page == 1 and index == 1:
            out.append(r"\begin{center}\large " + render_mixed(block) + r"\end{center}")
            continue
        if authority_page == 1 and index == 2:
            out.append(r"\begin{center}\itshape " + render_mixed(block) + r"\end{center}")
            continue

        plain = block.replace("\n", " ").strip()
        if plain in {"Sommaire", "Contents", "Bibliographie", "Bibliography"}:
            out.append(r"\EditionHeading{" + escape_prose(plain) + "}")
        elif authority_page == 18 and re.match(r"^[1-3]\. ", block):
            out.append(r"\noindent\hangindent=1.5em\hangafter=1 " + render_mixed(block) + r"\par")
        elif authority_page == 18 and plain in {"Reçu le 20 septembre 1975", "Received 20 September 1975"}:
            out.append(r"\medskip\noindent\itshape " + render_mixed(block) + r"\par\normalfont")
        elif authority_page == 18 and block.startswith("Pierre Deligne\n"):
            address_lines = [render_mixed(line) for line in block.splitlines() if line.strip()]
            out.append(r"\medskip\noindent " + r"\\".join(address_lines) + r"\par")
        elif len(block) < 120 and re.fullmatch(r"[1-5]\. [^\n]+", block):
            out.append(r"\EditionSection{" + render_mixed(block) + "}")
        elif authority_page == 1 and re.match(r"^1\. ", block):
            lines = [render_mixed(line) for line in block.splitlines() if line.strip()]
            out.append(r"{\footnotesize\setlength{\parskip}{0pt}" + "\n".join(line + r"\par" for line in lines) + "}")
        elif block.startswith(r"\[") and block.endswith(r"\]"):
            out.append(block)
        else:
            out.append(render_mixed(block) + r"\par")
    return "\n\n".join(out)


def edition_preamble(language: str) -> str:
    if language == "fr":
        title = "Les constantes locales de l'équation fonctionnelle de la fonction L d'Artin d'une représentation orthogonale"
        subtitle = "Édition critique française"
        running = "Constantes locales - édition française"
        lang_package = r"\usepackage[french]{babel}"
    else:
        title = "Local Constants in the Functional Equation of the Artin L-Function of an Orthogonal Representation"
        subtitle = "Standalone faithful English edition"
        running = "Local constants - English edition"
        lang_package = r"\usepackage[english]{babel}"

    return rf"""\documentclass[9pt,twoside]{{extarticle}}
\usepackage[a4paper,top=14mm,bottom=14mm,left=16mm,right=16mm,headheight=12pt,headsep=3.5mm,footskip=7mm,includeheadfoot]{{geometry}}
\usepackage{{fontspec}}
\defaultfontfeatures{{Ligatures=TeX,Scale=MatchLowercase}}
\setmainfont{{Libertinus Serif}}
\setsansfont{{Libertinus Sans}}
\usepackage{{mathtools}}
\usepackage{{array}}
\usepackage{{unicode-math}}
\setmathfont{{Libertinus Math}}
{lang_package}
\usepackage{{microtype}}
\usepackage{{adjustbox}}
\usepackage{{fancyhdr}}
\usepackage{{ragged2e}}
\usepackage[hidelinks,unicode]{{hyperref}}
\usepackage{{bookmark}}
\hypersetup{{pdftitle={{{title}}},pdfauthor={{Pierre Deligne}},pdfsubject={{{subtitle}}},pdfkeywords={{Deligne, Artin L-function, local constants, orthogonal representations, editable LaTeX}}}}
\pagestyle{{fancy}}
\fancyhf{{}}
\fancyhead[LE,RO]{{\footnotesize\sffamily {running}}}
\fancyhead[LO,RE]{{\footnotesize\sffamily Printed folio \thepage}}
\fancyfoot[C]{{\footnotesize\thepage}}
\renewcommand{{\headrulewidth}}{{0.25pt}}
\renewcommand{{\footrulewidth}}{{0pt}}
\setlength{{\parindent}}{{1em}}
\setlength{{\parskip}}{{0.13em}}
\setlength{{\abovedisplayskip}}{{3.2pt plus 1pt minus 1pt}}
\setlength{{\belowdisplayskip}}{{3.2pt plus 1pt minus 1pt}}
\setlength{{\abovedisplayshortskip}}{{2pt}}
\setlength{{\belowdisplayshortskip}}{{2pt}}
\setlength{{\jot}}{{1.5pt}}
\emergencystretch=1.4em
\providecommand{{\dashrightarrow}}{{\mathrel{{⇢}}}}
\newcommand{{\EditionHeading}}[1]{{\par\medskip{{\noindent\centering\large\bfseries #1\par}}\smallskip}}
\newcommand{{\EditionSection}}[1]{{\par\medskip{{\noindent\large\bfseries #1\par}}\smallskip}}
\newcommand{{\EditionPage}}[3]{{%
  \ifnum#1>1\clearpage\fi
  \pdfbookmark[1]{{Printed folio #2}}{{{language}-folio-#2}}%
  \hypertarget{{{language}-page-#1}}{{}}%
  \noindent\begin{{adjustbox}}{{max totalsize={{\textwidth}}{{0.915\textheight}},center}}
  \begin{{minipage}}[t]{{\textwidth}}
  \fontsize{{8.45}}{{10.05}}\selectfont\justifying
  #3
  \end{{minipage}}
  \end{{adjustbox}}%
}}
\begin{{document}}
\setcounter{{page}}{{299}}
\pdfbookmark[0]{{{title}}}{{d026-title-{language}}}
"""


def edition_postamble() -> str:
    return "\\end{document}\n"


def build_edition(rows: list[dict], language: str, out_path: Path) -> None:
    chunks = [edition_preamble(language)]
    for row in rows:
        page = int(row["authority_pdf_page"])
        folio = int(row["paper_folio"])
        body = render_page(row["text"], language, page)
        chunks.append(f"\\EditionPage{{{page}}}{{{folio}}}{{%\n{body}\n}}\n")
    chunks.append(edition_postamble())
    out_path.write_text("\n".join(chunks), encoding="utf-8", newline="\n")


def build_apparatus(rows: list[dict], out_path: Path) -> None:
    chunks = [r"""\documentclass[10pt]{article}
\usepackage[a4paper,margin=24mm]{geometry}
\usepackage{fontspec}
\setmainfont{Libertinus Serif}
\usepackage{mathtools}
\usepackage{unicode-math}
\setmathfont{Libertinus Math}
\usepackage[english]{babel}
\usepackage{microtype}
\usepackage[hidelinks,unicode]{hyperref}
\hypersetup{pdftitle={D026 restrained textual and translation apparatus},pdfauthor={Pierre Deligne}}
\providecommand{\dashrightarrow}{\mathrel{⇢}}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.55em}
\begin{document}
\begin{center}
{\Large\bfseries D026: restrained textual and translation apparatus}\par
\smallskip
Authority pages 1--18; printed folios 299--316
\end{center}
This apparatus records only material readings, logged repairs, translation choices, and semantic diagram decisions. It does not promote inherited comparison work or copy matter into the canonical editions.
"""]
    for row in rows:
        page = int(row["authority_pdf_page"])
        folio = int(row["paper_folio"])
        chunks.append(rf"\subsection*{{Authority page {page} / printed folio {folio}}}")
        chunks.append(render_mixed(row["text"]) + r"\par")
    chunks.append("\\end{document}\n")
    out_path.write_text("\n\n".join(chunks), encoding="utf-8", newline="\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--state-root", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    args = parser.parse_args()

    edition_dir = args.state_root / "edition"
    source_rows = read_ndjson(edition_dir / "source_language.ndjson")
    english_rows = read_ndjson(edition_dir / "english_standalone.ndjson")
    apparatus_rows = read_ndjson(edition_dir / "apparatus.ndjson")

    if any(row.get("language") != "fr" or row.get("status") != "frozen" for row in source_rows):
        raise ValueError("French records are not uniformly frozen")
    if any(row.get("language") != "en" or row.get("status") != "accepted" for row in english_rows):
        raise ValueError("English records are not uniformly accepted")
    if any(row.get("status") != "accepted" for row in apparatus_rows):
        raise ValueError("Apparatus records are not uniformly accepted")

    args.output_root.mkdir(parents=True, exist_ok=True)
    build_edition(source_rows, "fr", args.output_root / "Deligne_D026_FR.tex")
    build_edition(english_rows, "en", args.output_root / "Deligne_D026_EN.tex")
    build_apparatus(apparatus_rows, args.output_root / "Deligne_D026_APPARATUS.tex")
    print(json.dumps({
        "result": "PASS",
        "work_id": WORK_ID,
        "authority_sha256": AUTHORITY_SHA256,
        "french_pages": len(source_rows),
        "english_pages": len(english_rows),
        "apparatus_pages": len(apparatus_rows),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
