import json, re
from pathlib import Path

OUT = Path(r"local workspace\Documents\local repair pass PLEASE DONT DELETE WINDOWS 32\local repair pass_OUTPUTS\cayley_clean_per_volume")
inv = json.loads((OUT / "_inventory.json").read_text(encoding="utf-8"))

ROMAN = {"vol00":"Front_Matter","vol01":"Vol_I","vol02":"Vol_II","vol03":"Vol_III",
         "vol04":"Vol_IV","vol05":"Vol_V","vol06":"Vol_VI","vol07":"Vol_VII",
         "vol09":"Vol_IX","vol10":"Vol_X","vol11":"Vol_XI","vol12":"Vol_XII","vol13":"Vol_XIII"}
ROMAN_PRETTY = {"vol00":"Front Matter","vol01":"Vol. I","vol02":"Vol. II","vol03":"Vol. III",
         "vol04":"Vol. IV","vol05":"Vol. V","vol06":"Vol. VI","vol07":"Vol. VII",
         "vol09":"Vol. IX","vol10":"Vol. X","vol11":"Vol. XI","vol12":"Vol. XII","vol13":"Vol. XIII"}

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
\fancyhead[RE]{\nouppercase{\leftmark}}
\fancyhead[LO]{\nouppercase{\rightmark}}
\renewcommand{\headrulewidth}{0pt}

\titleformat{\section}{\normalfont\Large\bfseries}{\thesection}{1em}{}
\titleformat{\subsection}{\normalfont\large\bfseries}{\thesubsection}{1em}{}

\newtheorem*{theorem}{Theorem}
\newtheorem*{lemma}{Lemma}
\newtheorem*{proposition}{Proposition}
\newtheorem*{corollary}{Corollary}
\newtheorem*{definition}{Definition}
\newtheorem*{remark}{Remark}

\setlength{\emergencystretch}{3em}
\tolerance=2000
\hbadness=10000
\hfuzz=10pt
\vbadness=10000

% Fallback macros for commands used in source chunks
\providecommand{\modd}{\ \mathrm{mod}\ }
\providecommand{\tome}[1]{t.~#1}
\providecommand{\pages}[1]{pp.~#1}
\providecommand{\page}[1]{p.~#1}
\providecommand{\vols}[1]{vols.~#1}
\providecommand{\vol}[1]{vol.~#1}
\providecommand{\Hessian}{\mathrm{Hess}}
\providecommand{\Jacobian}{\mathrm{Jac}}
\providecommand{\Jac}{\mathrm{Jac}}
\providecommand{\Pf}{\mathrm{Pf}}
\providecommand{\nominaltimes}{\cdot}
\providecommand{\nthroot}[2]{\sqrt[#1]{#2}}
\providecommand{\half}{\tfrac{1}{2}}
\providecommand{\third}{\tfrac{1}{3}}
\providecommand{\diff}{\,d}
\providecommand{\dd}{\,d}
\providecommand{\sn}{\mathrm{sn}}
\providecommand{\cn}{\mathrm{cn}}
\providecommand{\dn}{\mathrm{dn}}
\providecommand{\qform}[1]{(#1)}
\providecommand{\V}[1]{#1}
\providecommand{\uth}{\textsuperscript{th}}
\providecommand{\fA}{\mathfrak{A}}
\providecommand{\tocentry}[2]{#1\dotfill #2\par}
\providecommand{\IndexEntry}[2]{#1\dotfill #2\par}
\providecommand{\paperentry}[3]{#1.\ #2\dotfill #3\par}
\providecommand{\mypar}{\par}
\providecommand{\wrule}{\noindent\rule{\linewidth}{0.5pt}\par}
\providecommand{\art}[1]{Art.~#1}
\providecommand{\arto}[1]{Art.~#1}
\providecommand{\asterism}{\par\smallskip\centerline{$\ast\,\ast\,\ast$}\smallskip\par}
\providecommand{\Bigast}{$\ast$}
\providecommand{\canont}{\mathop{\mathrm{canon}}\nolimits}
\providecommand{\Canon}{\mathop{\mathrm{Canon}}\nolimits}
\providecommand{\Disc}{\mathop{\mathrm{Disc}}\nolimits}
\providecommand{\Res}{\mathop{\mathrm{Res}}\nolimits}
\providecommand{\between}{,}
\providecommand{\nthcomma}[1]{,}
% Pre-declare counters that some chunks expect
\makeatletter
\@ifundefined{c@art}{\newcounter{art}}{}
\makeatother

\title{The Collected Mathematical Papers of Arthur Cayley\\__SUBTITLE__}
\author{Arthur Cayley}
\date{Modern \LaTeX{} reconstruction}

\begin{document}
\maketitle
"""

UNIFIED_TAIL = "\n\\end{document}\n"

PREAMBLE_END = re.compile(r"\\begin\{document\}", re.M)
DOC_END = re.compile(r"\\end\{document\}", re.M)
STRIP_RE = re.compile(r"\\(maketitle|tableofcontents)\b", re.M)

def extract_body(tex_text):
    m1 = PREAMBLE_END.search(tex_text)
    if not m1:
        return None
    m2 = DOC_END.search(tex_text, m1.end())
    body = tex_text[m1.end():m2.start()] if m2 else tex_text[m1.end():]
    body = STRIP_RE.sub("", body)
    return body.strip()

results = []
for vol, info in sorted(inv.items()):
    chunks = info["chunks"]
    if not chunks:
        continue
    label = ROMAN[vol]
    pretty = ROMAN_PRETTY[vol]
    chunk_dir = OUT / f"sources_tex_{label}"
    chunk_dir.mkdir(parents=True, exist_ok=True)
    master = OUT / f"Cayley_Collected_Mathematical_Papers_{label}.tex"

    preamble = UNIFIED_PREAMBLE.replace("__SUBTITLE__", pretty)
    pieces = [preamble]
    chunk_records = []
    for c in chunks:
        tex_path = Path(c["tex_path"])
        # Prefer local patched copy if it exists (in sources_tex_VolX dir)
        local = chunk_dir / tex_path.name
        if local.exists():
            try:
                text = local.read_text(encoding="utf-8", errors="replace")
            except Exception as e:
                text = tex_path.read_text(encoding="utf-8", errors="replace")
        else:
            try:
                text = tex_path.read_text(encoding="utf-8", errors="replace")
            except Exception as e:
                chunk_records.append({"chunk": c["name"], "error": str(e)})
                continue
        body = extract_body(text)
        if body is None:
            chunk_records.append({"chunk": c["name"], "error": "no begin document"})
            continue
        # Only write to local if not already there (preserves my patches)
        if not local.exists():
            local.write_text(text, encoding="utf-8")
        pieces.append(
            "\n\n% =========================================================\n"
            f"% Chunk: {tex_path.name}  (orig pages {c['start']}--{c['end']})\n"
            "% =========================================================\n"
        )
        pieces.append(body)
        pieces.append("\n\\clearpage\n")
        chunk_records.append({"chunk": c["name"], "pages": f"{c['start']}-{c['end']}",
                              "body_chars": len(body)})

    if info["missing_ranges"]:
        pieces.append("\n\n\\clearpage\n\\section*{Repair TODO}\n")
        pieces.append(
            "The following page ranges were not present in the source TeX drops "
            "and are missing from this reconstruction:\n\\begin{itemize}\n"
        )
        for r in info["missing_ranges"]:
            pieces.append("\\item Pages " + r.replace("_", "--") + "\n")
        pieces.append("\\end{itemize}\n")

    pieces.append(UNIFIED_TAIL)
    master.write_text("".join(pieces), encoding="utf-8")
    print(f"  {vol} -> {master.name}: {len(chunks)} chunks, "
          f"{sum(r.get('body_chars',0) for r in chunk_records):,} chars")
    results.append({
        "vol": vol, "label": pretty, "master_tex": str(master),
        "chunks_dir": str(chunk_dir), "chunk_records": chunk_records,
        "missing_ranges": info["missing_ranges"],
    })

(OUT / "_master_tex_summary.json").write_text(json.dumps(results, indent=2), encoding="utf-8")
print(f"\nWrote summary to _master_tex_summary.json")
