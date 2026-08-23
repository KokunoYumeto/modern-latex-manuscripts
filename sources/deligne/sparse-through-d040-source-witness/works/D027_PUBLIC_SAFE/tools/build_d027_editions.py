#!/usr/bin/env python3
"""Build canonical D027 English, French, and apparatus TeX editions.

The returned HTML readers and inherited PDFs are evidence only.  This builder
reads the frozen page records, checks their authority identity and exact page
topology, excludes the JSTOR cover from both scholarly editions, and emits one
canonical edition page for each printed article page (103--161).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


WORK_ID = "DELIGNE_LUSZTIG_D027_REDUCTIVE_GROUPS"
AUTHORITY_SHA256 = "8037B883D391A17534F2B5C7A55B9593AD6A3F5C15045EC8751BD1FFCED83BDF"
EXPECTED_PHYSICAL_PAGES = list(range(1, 61))
EXPECTED_ARTICLE_PAGES = list(range(2, 61))
EXPECTED_PRINTED_PAGES = list(range(103, 162))
EXCLUDED_DISPOSITION = "EXCLUDE_FROM_SCHOLARLY_BODIES_RETAIN_PROVENANCE"
INCLUDED_DISPOSITION = "INCLUDE_ARTICLE"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def read_ndjson(path: Path, expected_status: str) -> list[dict]:
    rows = [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    physical = [int(row["physical_page"]) for row in rows]
    if physical != EXPECTED_PHYSICAL_PAGES:
        raise ValueError(f"{path.name}: physical topology mismatch: {physical}")

    if rows[0].get("disposition") != EXCLUDED_DISPOSITION:
        raise ValueError(f"{path.name}: physical page 1 is not provenance-only")
    if int(rows[0].get("printed_page", -1)) != 0:
        raise ValueError(f"{path.name}: physical page 1 unexpectedly has a printed folio")

    article = rows[1:]
    if [int(row["physical_page"]) for row in article] != EXPECTED_ARTICLE_PAGES:
        raise ValueError(f"{path.name}: article physical-page topology mismatch")
    if [int(row["printed_page"]) for row in article] != EXPECTED_PRINTED_PAGES:
        raise ValueError(f"{path.name}: printed-page topology mismatch")

    for row in rows:
        page = int(row["physical_page"])
        if row.get("source_sha256", "").upper() != AUTHORITY_SHA256:
            raise ValueError(f"{path.name}: authority mismatch on physical page {page}")
        expected_disposition = EXCLUDED_DISPOSITION if page == 1 else INCLUDED_DISPOSITION
        if row.get("disposition") != expected_disposition:
            raise ValueError(f"{path.name}: disposition mismatch on physical page {page}")
        if row.get("status") != expected_status:
            raise ValueError(f"{path.name}: status mismatch on physical page {page}")
        if not isinstance(row.get("text"), str) or not row["text"].strip():
            raise ValueError(f"{path.name}: empty text on physical page {page}")
        if row.get("assets") not in ([], None):
            raise ValueError(f"{path.name}: unexpected promoted asset on physical page {page}")
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
    text = text.replace("\u2011", "-").replace("\u2013", "--").replace("\u2014", "---")
    text = text.replace("\u2026", r"\ldots{}")
    return "".join(SPECIALS.get(char, char) for char in text)


MATH_RE = re.compile(r"(\\\((?:.|\n)*?\\\)|\\\[(?:.|\n)*?\\\])", re.DOTALL)
SEMANTIC_TEX_REPAIRS = (
    (r"\toE", r"\to E", "insert token boundary after relation command"),
    (r"\inE", r"\in E", "insert token boundary after relation command"),
)
LINEBREAK_LITERAL_BRACKET_RE = re.compile(
    r"\\\\\[(?!\s*(?:\d+(?:\.\d+)?|\.\d+)\s*(?:pt|mm|cm|em|ex|in|bp|pc|dd|cc|sp)\s*\])"
)


def repair_semantic_tex(text: str, layer: str, physical_page: int, repairs: list[dict]) -> str:
    repaired = text
    for before, after, reason in SEMANTIC_TEX_REPAIRS:
        count = repaired.count(before)
        if count:
            repaired = repaired.replace(before, after)
            repairs.append(
                {
                    "layer": layer,
                    "physical_page": physical_page,
                    "before": before,
                    "after": after,
                    "count": count,
                    "reason": reason,
                }
            )
    repaired, count = LINEBREAK_LITERAL_BRACKET_RE.subn(lambda _match: r"\\{}[", repaired)
    if count:
        repairs.append(
            {
                "layer": layer,
                "physical_page": physical_page,
                "before": r"\\[",
                "after": r"\\{}[",
                "count": count,
                "reason": "disambiguate a displayed line break before a literal opening bracket",
            }
        )
    return repaired


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


def is_chapter_heading(plain: str) -> bool:
    return bool(re.fullmatch(r"\d+\.\s+[^\n]{3,90}", plain))


def render_article_page(text: str, language: str, physical_page: int) -> str:
    blocks = [block.strip() for block in re.split(r"\n\s*\n", text.strip()) if block.strip()]
    out: list[str] = []
    for index, block in enumerate(blocks):
        plain = re.sub(r"\s+", " ", block).strip()

        if physical_page == 2 and index == 0:
            out.append(r"\begin{center}\footnotesize " + render_mixed(block) + r"\end{center}")
        elif physical_page == 2 and index == 1:
            out.append(r"\begin{center}\fontsize{14.5}{16.5}\selectfont\bfseries " + render_mixed(block) + r"\end{center}")
        elif physical_page == 2 and index == 2:
            out.append(r"\begin{center}\large " + render_mixed(block) + r"\end{center}")
        elif plain in {"Introduction", "TABLE OF CONTENTS", "TABLE DES MATIÈRES", "REFERENCES", "RÉFÉRENCES"}:
            out.append(r"\EditionHeading{" + escape_prose(plain) + "}")
        elif is_chapter_heading(plain):
            out.append(r"\EditionChapter{" + render_mixed(plain) + "}")
        elif re.match(r"^(THEOREM|PROPOSITION|COROLLARY|LEMMA|DEFINITION|THÉORÈME|COROLLAIRE|LEMME|DÉFINITION)\b", plain):
            statement = re.match(
                r"^((?:THEOREM|PROPOSITION|COROLLARY|LEMMA|DEFINITION|THÉORÈME|COROLLAIRE|LEMME|DÉFINITION)\s+[0-9.]+(?:\s*\([^)]+\))?\.)\s*(.*)$",
                block,
                re.DOTALL,
            )
            if statement:
                out.append(
                    r"\noindent\textbf{"
                    + escape_prose(statement.group(1))
                    + "} "
                    + render_mixed(statement.group(2))
                    + r"\par"
                )
            else:
                out.append(r"\noindent " + render_mixed(block) + r"\par")
        elif re.match(r"^(ADDED IN PROOF|AJOUTÉ AUX ÉPREUVES)", plain):
            out.append(r"\medskip\noindent\textbf{" + render_mixed(block) + r"}\par")
        elif physical_page == 60 and re.match(r"^\[\d+\]\s", plain):
            out.append(r"\noindent\hangindent=1.7em\hangafter=1 " + render_mixed(block) + r"\par")
        elif physical_page == 60 and plain.startswith("(") and ("Received" in plain or "Reçu" in plain):
            out.append(r"\medskip\noindent\itshape " + render_mixed(block) + r"\par\normalfont")
        elif physical_page == 60 and ("INSTITUTE" in plain or "INSTITUT" in plain or "UNIVERSITY" in plain or "UNIVERSITÉ" in plain):
            out.append(r"\medskip\noindent\textsc{" + render_mixed(block) + r"}\par")
        elif block.startswith(r"\[") and block.endswith(r"\]"):
            out.append(block)
        else:
            out.append(render_mixed(block) + r"\par")
    return "\n\n".join(out)


def edition_preamble(language: str) -> str:
    if language == "en":
        title = "Representations of Reductive Groups over Finite Fields"
        subtitle = "Source-language critical edition"
        running = "Reductive groups over finite fields - English source edition"
        lang_package = r"\usepackage[english]{babel}"
    else:
        title = "Représentations des groupes réductifs sur les corps finis"
        subtitle = "Édition française fidèle"
        running = "Groupes réductifs sur les corps finis - édition française"
        lang_package = r"\usepackage[french]{babel}"

    return rf"""\documentclass[9pt,twoside]{{extarticle}}
\usepackage[a4paper,top=14mm,bottom=14mm,left=19mm,right=19mm,headheight=12pt,headsep=3.5mm,footskip=7mm,includeheadfoot]{{geometry}}
\usepackage{{fontspec}}
\defaultfontfeatures{{Ligatures=TeX,Scale=MatchLowercase}}
\setmainfont{{Libertinus Serif}}
\setsansfont{{Libertinus Sans}}
\usepackage{{mathtools}}
\usepackage{{amssymb}}
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
\hypersetup{{pdftitle={{{title}}},pdfauthor={{P. Deligne and G. Lusztig}},pdfsubject={{{subtitle}}},pdfkeywords={{Deligne, Lusztig, reductive groups, finite fields, editable LaTeX}}}}
\pagestyle{{fancy}}
\fancyhf{{}}
\fancyhead[LE,RO]{{\footnotesize\sffamily {running}}}
\fancyhead[LO,RE]{{\footnotesize\sffamily Printed page \thepage}}
\fancyfoot[C]{{\footnotesize\thepage}}
\renewcommand{{\headrulewidth}}{{0.25pt}}
\renewcommand{{\footrulewidth}}{{0pt}}
\setlength{{\parindent}}{{1em}}
\setlength{{\parskip}}{{0.11em}}
\setlength{{\abovedisplayskip}}{{2.8pt plus 1pt minus 1pt}}
\setlength{{\belowdisplayskip}}{{2.8pt plus 1pt minus 1pt}}
\setlength{{\abovedisplayshortskip}}{{1.8pt}}
\setlength{{\belowdisplayshortskip}}{{1.8pt}}
\setlength{{\jot}}{{1.2pt}}
\emergencystretch=1.5em
\newcommand{{\EditionHeading}}[1]{{\par\medskip{{\noindent\centering\large\bfseries #1\par}}\smallskip}}
\newcommand{{\EditionChapter}}[1]{{\par\medskip{{\noindent\large\bfseries #1\par}}\smallskip}}
\newcommand{{\EditionPage}}[3]{{%
  \ifnum#1>2\clearpage\fi
  \pdfbookmark[1]{{Printed page #2}}{{{language}-folio-#2}}%
  \hypertarget{{{language}-physical-#1}}{{}}%
  \noindent\begin{{adjustbox}}{{max totalsize={{\textwidth}}{{0.918\textheight}},center}}
  \begin{{minipage}}[t]{{\textwidth}}
  \fontsize{{9.4}}{{11.1}}\selectfont\justifying
  #3
  \end{{minipage}}
  \end{{adjustbox}}%
}}
\begin{{document}}
\setcounter{{page}}{{103}}
\pdfbookmark[0]{{{title}}}{{d027-title-{language}}}
"""


def build_edition(rows: list[dict], language: str, output: Path, repairs: list[dict]) -> None:
    chunks = [edition_preamble(language)]
    for row in rows[1:]:
        physical = int(row["physical_page"])
        printed = int(row["printed_page"])
        repaired = repair_semantic_tex(row["text"], language, physical, repairs)
        body = render_article_page(repaired, language, physical)
        chunks.append(f"\\EditionPage{{{physical}}}{{{printed}}}{{%\n{body}\n}}\n")
    chunks.append("\\end{document}\n")
    output.write_text("\n".join(chunks), encoding="utf-8", newline="\n")


def apparatus_preamble() -> str:
    return r"""\documentclass[10pt]{article}
\usepackage[a4paper,margin=20mm]{geometry}
\usepackage{fontspec}
\defaultfontfeatures{Ligatures=TeX,Scale=MatchLowercase}
\setmainfont{Libertinus Serif}
\usepackage{mathtools}
\usepackage{amssymb}
\usepackage{unicode-math}
\setmathfont{Libertinus Math}
\usepackage[english]{babel}
\usepackage{microtype}
\usepackage[hidelinks,unicode]{hyperref}
\usepackage{bookmark}
\hypersetup{pdftitle={D027 restrained textual and translation apparatus},pdfauthor={P. Deligne and G. Lusztig}}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.42em}
\begin{document}
\begin{center}
{\Large\bfseries D027: restrained textual and translation apparatus}\par
\smallskip
Authority physical pages 1--60; article printed pages 103--161
\end{center}
The controlling authority is the 60-page JSTOR scan identified in the publication manifest. Physical page 1 is retained only as provenance and is excluded from both scholarly bodies. The English edition is the source-language edition; the French edition is a faithful translation. Inherited readers, TeX, OCR, and comparator files remain evidentiary until separately verified.

Nine TeX parser-boundary repairs are applied independently in each scholarly edition. Two instances of \verb|\toE| become \verb|\to E| on physical page 9, and one instance of \verb|\inE| becomes \verb|\in E| on physical page 10. Six displayed line breaks immediately followed by a literal opening bracket become \verb|\\{}[| on physical pages 35, 55, 56, and 57, preventing TeX from treating the bracketed expression as an optional spacing argument. The genuine \verb|\\[2mm]| spacing command on physical page 53 is preserved. These changes restore the intended token boundaries and do not alter any mathematical reading.
"""


def build_apparatus(rows: list[dict], output: Path) -> None:
    chunks = [apparatus_preamble()]
    for row in rows:
        physical = int(row["physical_page"])
        if physical == 1:
            heading = "Physical page 1 / provenance-only cover"
        else:
            heading = f"Physical page {physical} / printed page {int(row['printed_page'])}"
        chunks.append(r"\subsection*{" + escape_prose(heading) + "}")
        for block in [b.strip() for b in re.split(r"\n\s*\n", row["text"].strip()) if b.strip()]:
            chunks.append(render_mixed(block) + r"\par")
    chunks.append("\\end{document}\n")
    output.write_text("\n\n".join(chunks), encoding="utf-8", newline="\n")


def write_repair_log(repairs: list[dict], output_root: Path) -> None:
    expected = {
        ("en", 9, r"\toE", r"\to E"): 2,
        ("en", 10, r"\inE", r"\in E"): 1,
        ("en", 35, r"\\[", r"\\{}["): 1,
        ("en", 55, r"\\[", r"\\{}["): 2,
        ("en", 56, r"\\[", r"\\{}["): 2,
        ("en", 57, r"\\[", r"\\{}["): 1,
        ("fr", 9, r"\toE", r"\to E"): 2,
        ("fr", 10, r"\inE", r"\in E"): 1,
        ("fr", 35, r"\\[", r"\\{}["): 1,
        ("fr", 55, r"\\[", r"\\{}["): 2,
        ("fr", 56, r"\\[", r"\\{}["): 2,
        ("fr", 57, r"\\[", r"\\{}["): 1,
    }
    actual = {
        (row["layer"], row["physical_page"], row["before"], row["after"]): row["count"]
        for row in repairs
    }
    if actual != expected:
        raise ValueError(f"semantic TeX repair set mismatch: {actual}")

    payload = {
        "result": "PASS",
        "work_id": WORK_ID,
        "authority_sha256": AUTHORITY_SHA256,
        "policy": "deterministic render-layer token-boundary repair; frozen records unchanged",
        "repairs": repairs,
    }
    (output_root / "D027_SEMANTIC_TEX_REPAIRS.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    lines = ["layer\tphysical_page\tbefore\tafter\tcount\treason"]
    for row in repairs:
        lines.append(
            "\t".join(
                str(row[key])
                for key in ("layer", "physical_page", "before", "after", "count", "reason")
            )
        )
    (output_root / "D027_SEMANTIC_TEX_REPAIRS.tsv").write_text(
        "\n".join(lines) + "\n", encoding="utf-8", newline="\n"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--state-root", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    args = parser.parse_args()

    edition_dir = args.state_root / "edition"
    source_rows = read_ndjson(edition_dir / "source_language.ndjson", "frozen")
    french_rows = read_ndjson(edition_dir / "french_translation.ndjson", "accepted")
    apparatus_rows = read_ndjson(edition_dir / "apparatus.ndjson", "accepted")

    args.output_root.mkdir(parents=True, exist_ok=True)
    repairs: list[dict] = []
    build_edition(source_rows, "en", args.output_root / "Deligne_D027_EN.tex", repairs)
    build_edition(french_rows, "fr", args.output_root / "Deligne_D027_FR.tex", repairs)
    build_apparatus(apparatus_rows, args.output_root / "Deligne_D027_APPARATUS.tex")
    write_repair_log(repairs, args.output_root)

    summary = {
        "result": "PASS",
        "work_id": WORK_ID,
        "authority_sha256": AUTHORITY_SHA256,
        "authority_physical_pages": 60,
        "excluded_physical_pages": [1],
        "english_article_pages": 59,
        "french_article_pages": 59,
        "printed_page_range": [103, 161],
        "repair_events": sum(int(row["count"]) for row in repairs),
        "outputs": {
            path.name: sha256_file(path)
            for path in sorted(args.output_root.glob("*.tex"))
        },
    }
    print(json.dumps(summary, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
