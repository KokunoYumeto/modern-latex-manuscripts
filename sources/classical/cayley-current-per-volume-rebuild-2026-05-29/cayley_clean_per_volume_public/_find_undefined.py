import re
from pathlib import Path
from collections import Counter

OUT = Path(r"local workspace\Documents\local repair pass PLEASE DONT DELETE WINDOWS 32\local repair pass_OUTPUTS\cayley_clean_per_volume")

# Standard LaTeX/AMS commands - allowlist
STANDARD = set("""
documentclass usepackage begin end newcommand renewcommand providecommand title author date maketitle
section subsection subsubsection chapter paragraph item itemize enumerate description tableofcontents
ref label cite bibitem includegraphics
frac sqrt cdot ldots cdots dots vdots ddots times div pm mp ast star circ bullet
sum prod int oint partial nabla infty cdot
alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa lambda mu nu xi
pi varpi rho varrho sigma varsigma tau upsilon phi varphi chi psi omega
Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega
sin cos tan cot sec csc arcsin arccos arctan sinh cosh tanh log ln exp lim limsup liminf
max min sup inf det dim ker hom mod gcd lcm Pr deg arg
left right big Big bigg Bigg langle rangle lvert rvert lceil rceil lfloor rfloor
text textit textbf textrm texttt mathbb mathcal mathfrak mathbf mathit mathrm mathsf mathtt
displaystyle textstyle scriptstyle scriptscriptstyle
overline underline overbrace underbrace overrightarrow overleftarrow vec hat tilde bar dot ddot
quad qquad space hspace vspace par newpage clearpage cleardoublepage pagebreak linebreak
center centering raggedright raggedleft flushleft flushright
makeatletter makeatother input include
emph small footnotesize scriptsize tiny normalsize large Large LARGE huge Huge
bf it rm tt sf sl em strut vfill hfill phantom mathstrut
le ge ne neq leq geq sim simeq approx equiv cong propto perp parallel
in notin ni subset supset subseteq supseteq cup cap setminus emptyset
forall exists Re Im aleph hbar imath jmath ell wp prime
to gets mapsto rightarrow leftarrow Rightarrow Leftarrow leftrightarrow Leftrightarrow uparrow downarrow
quad qquad noindent indent setlength addtolength stretch fill
LaTeX TeX i j l O o S P AA aa ss
thinspace medspace thickspace negthinspace negmedspace negthickspace negspace
ensuremath mathop mathrel mathbin mathopen mathclose mathpunct nolimits limits substack
binom dbinom tbinom choose pmod bmod
multicolumn multirow hline cline toprule midrule bottomrule
caption label ref pageref vref autoref
url href hyperlink hypertarget href
fancyhf fancyhead fancyfoot pagestyle thispagestyle headrulewidth footrulewidth
geometry topmargin bottommargin leftmargin rightmargin paperwidth paperheight textwidth textheight
chaptername thechapter thesection thesubsection thepage thefigure thetable thefootnote
titleformat titlespacing titlecontents titlerule titlelabel
fnsymbol footnotemark footnotetext footnote thanks
newtheorem newtheoremstyle theoremstyle theorembodyfont theoremheaderfont
spaceskip xspaceskip glueexpr lineskip baselineskip parindent parskip
relax penalty break nobreak allowbreak nonumber tag eqlabel
intertext aligned alignat array matrix bmatrix pmatrix vmatrix Bmatrix Vmatrix smallmatrix cases
empty thispagestyle null
nouppercase leftmark rightmark headheight footskip
parbox makebox framebox raisebox rule
arabic roman Roman alph Alph
maketitlepage half third diff dd
emergencystretch tolerance hbadness vbadness hfuzz vfuzz
overfullrule
columnwidth columnsep linewidth
addtolength setlength
char unicode
medskip smallskip bigskip
mskip mu kern
pageref number numberline
contentsname listfigurename listtablename refname bibname indexname figurename tablename partname
appendixname abstractname keywordname proofname theoremname lemmaname propositionname corollaryname
definitionname remarkname examplename exercisename problemname
roman arabic Roman alph Alph
acute grave check breve dot ddot ring slash bar overlinetilde
not neg vee wedge oplus otimes odot ominus
""".split())

undefined = Counter()
files_with = {}

cmd_re = re.compile(r"\\([A-Za-z]+)")
for vol_dir in sorted(OUT.glob("sources_tex_*")):
    for tex_file in sorted(vol_dir.glob("*.tex")):
        text = tex_file.read_text(encoding="utf-8", errors="replace")
        # Strip preamble (it has \newcommand definitions)
        idx = text.find(r"\begin{document}")
        body = text[idx:] if idx >= 0 else text
        # Strip comments
        body = re.sub(r"%.*$", "", body, flags=re.M)
        for m in cmd_re.findall(body):
            if m not in STANDARD:
                undefined[m] += 1
                files_with.setdefault(m, set()).add(tex_file.name)

# Filter out probably-fine commands (those that appear in chunk preambles)
print("=== Top 40 non-standard commands seen (likely needing fallback) ===")
for cmd, count in undefined.most_common(40):
    examples = list(files_with[cmd])[:2]
    print(f"  \\{cmd}: {count} uses ({examples})")
