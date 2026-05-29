"""Build cumulative Vol VIII master TeX + compiled PDF from current chunks.
Re-run any time more chunks are added. Output goes to top-level cayley_clean_per_volume/.
"""
import re, subprocess, shutil
from pathlib import Path
from pypdf import PdfReader, PdfWriter

ROOT = Path(__file__).parent
SRC = ROOT / "sources_tex_Vol_VIII"
OUT_PDF = ROOT / "Cayley_Collected_Mathematical_Papers_Vol_VIII.pdf"
OUT_TEX = ROOT / "Cayley_Collected_Mathematical_Papers_Vol_VIII.tex"
PDFLATEX = r"local workspace\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe"

CHUNK_RE = re.compile(r"cayley_vol08_pages_(\d+)_(\d+)\.tex$")

PREAMBLE_END = re.compile(r"\\begin\{document\}", re.M)
DOC_END = re.compile(r"\\end\{document\}", re.M)
STRIP_RE = re.compile(r"\\(maketitle|tableofcontents)\b", re.M)


def extract_body(tex_text):
    m1 = PREAMBLE_END.search(tex_text)
    if not m1:
        return None
    m2 = DOC_END.search(tex_text, m1.end())
    body = tex_text[m1.end():m2.start()] if m2 else tex_text[m1.end():]
    return STRIP_RE.sub("", body).strip()


UNIFIED_PREAMBLE = r"""\documentclass[11pt,a4paper]{book}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[shorthands=off,english,french,german]{babel}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{geometry}
\usepackage{graphicx}
\usepackage{fancyhdr}
\usepackage{titlesec}
\usepackage{enumitem}
\usepackage{array}
\usepackage{longtable}
\usepackage{multirow}
\usepackage{booktabs}
\usepackage{url}
\usepackage[protrusion=true,expansion=false]{microtype}
\usepackage[bookmarks=true,hidelinks]{hyperref}

\geometry{paperwidth=6.5in,paperheight=9.5in,margin=1in,footskip=0.5in}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE,RO]{\thepage}
\renewcommand{\headrulewidth}{0pt}

\providecommand{\modd}{\ \mathrm{mod}\ }
\providecommand{\tome}[1]{t.~#1}
\providecommand{\pages}[1]{pp.~#1}
\providecommand{\page}[1]{p.~#1}
\providecommand{\vols}[1]{vols.~#1}
\providecommand{\vol}[1]{vol.~#1}
\providecommand{\Hessian}{\mathrm{Hess}}
\providecommand{\asterism}{\par\smallskip\centerline{$\ast\,\ast\,\ast$}\smallskip\par}

\title{The Collected Mathematical Papers of Arthur Cayley\\Vol. VIII}
\author{Arthur Cayley}
\date{Modern \LaTeX{} reconstruction --- direct from scan}

\begin{document}
\maketitle

\frontmatter
\section*{Note on this volume}
\noindent
This volume is reconstructed directly from the 1895 Cambridge University Press
scan using local repair pass (Opus 4.7) image-direct typesetting in 50-page chunks. The
math content is verified against the original page images; in particular,
\(\Delta\), \(\partial\), subscripts, superscripts, brace nesting, summations
and integrals are preserved literally. Some dense numerical tables are marked
\texttt{[table omitted]} where transcription would have required undue effort
in this batch; their structural framing is preserved.

\clearpage
"""

UNIFIED_TAIL = "\n\\end{document}\n"


def main():
    chunks = []
    for tex_path in sorted(SRC.glob("cayley_vol08_pages_*.tex")):
        m = CHUNK_RE.search(tex_path.name)
        if not m:
            continue
        start, end = int(m.group(1)), int(m.group(2))
        chunks.append((start, end, tex_path))
    chunks.sort()

    pieces = [UNIFIED_PREAMBLE]
    last_end = 0
    gap_count = 0
    for start, end, tex_path in chunks:
        # Insert gap placeholder if there's a discontinuity
        if last_end > 0 and start > last_end + 1:
            pieces.append(f"\n\n\\clearpage\n\\section*{{Gap: book pages {last_end+1}--{start-1}}}\n")
            pieces.append("\\noindent These pages were not completed in the current pass (not completed in the current pass). "
                          "Refer to the source scan PDF for this range.\n\\clearpage\n")
            gap_count += 1
        text = tex_path.read_text(encoding="utf-8", errors="replace")
        body = extract_body(text)
        if body:
            pieces.append(f"\n\n% =================== {tex_path.name} (book pp {start}-{end}) ===================\n")
            pieces.append(body)
            pieces.append("\n\\clearpage\n")
        last_end = end

    pieces.append(UNIFIED_TAIL)
    OUT_TEX.write_text("".join(pieces), encoding="utf-8")
    print(f"Wrote master TeX: {OUT_TEX} ({sum(len(p) for p in pieces):,} chars)")
    print(f"Chunks: {len(chunks)}, gaps marked: {gap_count}")

    # Compile
    print(f"Compiling...")
    workdir = ROOT / "_build_vol8"
    workdir.mkdir(exist_ok=True)
    shutil.copy(OUT_TEX, workdir / "book.tex")
    proc = subprocess.run([PDFLATEX, "-interaction=nonstopmode", "book.tex"],
                          cwd=str(workdir), capture_output=True, text=True, timeout=900)
    if (workdir / "book.pdf").exists():
        shutil.copy(workdir / "book.pdf", OUT_PDF)
        pages = len(PdfReader(str(OUT_PDF)).pages)
        print(f"Compiled: {OUT_PDF} ({pages} pages)")
    else:
        print(f"Compile failed. Last errors:")
        for line in proc.stdout.splitlines()[-30:]:
            if line.startswith("!") or "rror" in line.lower():
                print(f"  {line}")


if __name__ == "__main__":
    main()
