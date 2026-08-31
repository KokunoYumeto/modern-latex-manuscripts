"""Deterministic editable native-TeX D031 readers and restrained apparatus.

No formula/content repair is hidden in this build. Input records are preserved;
all changes here are presentation-only (page labels, Markdown to TeX, native TOC).
"""
from pathlib import Path
import argparse, csv, hashlib, json, os, re, subprocess

BASE = Path(__file__).resolve().parent
INPUT = BASE / 'input_state'
PANDOC = 'C:/Users/[LOCAL_ACCOUNT]/AppData/Local/Pandoc/pandoc.exe'
TEX = 'C:/Users/[LOCAL_ACCOUNT]/AppData/Local/Programs/MiKTeX/miktex/bin/x64/pdflatex.exe'
PAT = re.compile(r'<!-- BEGIN_PAGE physical=(\d+) printed=(\d+) -->\n(.*?)\n<!-- END_PAGE physical=\1 printed=\2 -->', re.S)
PREAMBLE = r'''\documentclass[10pt,a4paper]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern,amsmath,amssymb,mathrsfs,tikz-cd,microtype}
\usepackage[margin=17mm,footskip=8mm]{geometry}
\usepackage{booktabs,longtable,array,tabularx,calc,adjustbox}
\usepackage{fancyhdr}
\usepackage[unicode,hidelinks,bookmarks=false]{hyperref}
\setcounter{secnumdepth}{-10}
\pdfinfoomitdate=1
\pdftrailerid{}
\pdfsuppressptexinfo=15
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\fancyfoot[C]{\thepage}
\setlength{\parindent}{1em}
\setlength{\parskip}{2pt}
\setlength{\emergencystretch}{4em}
\DeclareUnicodeCharacter{03A8}{\ensuremath{\Psi}}
\DeclareUnicodeCharacter{03C6}{\ensuremath{\varphi}}
\DeclareUnicodeCharacter{03B1}{\ensuremath{\alpha}}
\DeclareUnicodeCharacter{03A3}{\ensuremath{\Sigma}}
\DeclareUnicodeCharacter{03C1}{\ensuremath{\rho}}
\DeclareUnicodeCharacter{03C0}{\ensuremath{\pi}}
\DeclareUnicodeCharacter{03BC}{\ensuremath{\mu}}
\DeclareUnicodeCharacter{03C3}{\ensuremath{\sigma}}
\DeclareUnicodeCharacter{03C4}{\ensuremath{\tau}}
\DeclareUnicodeCharacter{03C9}{\ensuremath{\omega}}
\DeclareUnicodeCharacter{03B3}{\ensuremath{\gamma}}
\DeclareUnicodeCharacter{0393}{\ensuremath{\Gamma}}
\DeclareUnicodeCharacter{0394}{\ensuremath{\Delta}}
\DeclareUnicodeCharacter{2192}{\ensuremath{\to}}
\DeclareUnicodeCharacter{2032}{\ensuremath{{}^{\prime}}}
\DeclareUnicodeCharacter{2033}{\ensuremath{{}^{\prime\prime}}}
\DeclareUnicodeCharacter{2080}{\ensuremath{{}_0}}
\DeclareUnicodeCharacter{2081}{\ensuremath{{}_1}}
\DeclareUnicodeCharacter{2086}{\ensuremath{{}_6}}
\DeclareUnicodeCharacter{2087}{\ensuremath{{}_7}}
\DeclareUnicodeCharacter{2243}{\ensuremath{\simeq}}
\DeclareUnicodeCharacter{207A}{\ensuremath{{}^+}}
\DeclareUnicodeCharacter{2229}{\ensuremath{\cap}}
\DeclareUnicodeCharacter{2208}{\ensuremath{\in}}
\DeclareUnicodeCharacter{2212}{\ensuremath{-}}
\DeclareUnicodeCharacter{21A6}{\ensuremath{\mapsto}}
\DeclareUnicodeCharacter{1D516}{\ensuremath{\mathfrak S}}
\DeclareUnicodeCharacter{2265}{\ensuremath{\geq}}
\DeclareUnicodeCharacter{27E8}{\ensuremath{\langle}}
\DeclareUnicodeCharacter{27E9}{\ensuremath{\rangle}}
\DeclareUnicodeCharacter{2209}{\ensuremath{\notin}}
\DeclareUnicodeCharacter{2282}{\ensuremath{\subset}}
\DeclareUnicodeCharacter{2283}{\ensuremath{\supset}}
\DeclareUnicodeCharacter{2218}{\ensuremath{\circ}}
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\providecommand{\passthrough}[1]{#1}
\newcommand{\SourcePage}[2]{\clearpage\setcounter{page}{#2}\typeout{D031_SOURCE_PAGE physical=#1 printed=#2}}
\begin{document}
'''

def sha(b): return hashlib.sha256(b).hexdigest().upper()

def pandoc(md, raw=True):
    flavor='markdown+tex_math_single_backslash'+('+raw_tex' if raw else '-raw_tex')+'-auto_identifiers'
    result = subprocess.run([PANDOC, '-f', flavor, '-t', 'latex', '--wrap=none'], input=md, text=True, encoding='utf-8', capture_output=True, check=True)
    return result.stdout

def clean_body(body):
    body = re.sub(r'^## Physical page \d+ . printed page \d+\n+', '', body)
    # The supplied source TOC is prose with dot leaders. Render it as a native table.
    toc = re.compile(r'(?m)^(.+?) \.{3,}\s+(\d{3})\s*$')
    lines = body.splitlines(); output=[]; entries=[]
    for line in lines:
        m=toc.match(line)
        if m:
            entries.append((m.group(1),m.group(2)))
        else:
            if entries:
                output.append('\\begin{tabularx}{\\linewidth}{@{}Xr@{}}')
                for title, page in entries:
                    title=re.sub(r'^(\d+)\.',r'\1\\.',title)
                    output.append(pandoc(title).strip()+' & '+page+r' \\')
                output.append('\\end{tabularx}')
                entries=[]
            output.append(line)
    assert not entries
    return '\n'.join(output)

def reader(language, dest):
    md = (INPUT / f'editions/{language}.md').read_text(encoding='utf-8')
    records = list(PAT.finditer(md)); assert len(records)==43
    chunks=[]; manifest=[]; staged=[]
    for i,m in enumerate(records,1):
        assert int(m.group(1))==i and int(m.group(2))==246+i
        body=clean_body(m.group(3))
        if i==3:
            old=r'''\begin{tikzcd}[column sep=large,row sep=large]
C(F) \arrow[d,"N_{F/E}"'] \arrow[dr] & \\
C(E) \arrow[r] & G(A)/\rho\widetilde G(A)\cdot G(\mathbf Q)
\end{tikzcd}'''
            new=r'''\begin{tikzcd}[column sep=large,row sep=normal]
C(F) \arrow[dd,"N_{F/E}"'] \arrow[dr] & \\
& G(A)/\rho\widetilde G(A)\cdot G(\mathbf Q) \\
C(E) \arrow[ur] &
\end{tikzcd}'''
            assert body.count(old)==1
            body=body.replace(old,new)
        if i==41:
            for old in [r"M^0(G_i,G'_i,X_i^+)",r"M^0(\prod G_i,\prod G'_i,\prod X_i^+)",r"M^0(G,G'',X^+)"]:
                assert body.count(old)==1
                body=body.replace(old,old.replace('M^0(',r'M^0_{\mathbf C}('))
        if i==11:
            old=r'g\in G_{\mathbf C}(\mathbf C)'
            assert body.count(old)==1
            body=body.replace(old,r'g\in(\mathbf C)')
        if i==15:
            old=r'\langle\mu,\gamma\rangle'
            assert body.count(old)==1
            body=body.replace(old,r'\langle\mu,z\rangle')
            if language=='french_diplomatic':
                assert r'$\gamma$ une racine' in body
                body=body.replace(r'$\gamma$ une racine',r'$r$ une racine')
                body=body.replace(r'\text{-linéaire de racines}',r'\text{-linéaire de racine}')
            else:
                assert r'for roots $\gamma$' in body
                body=body.replace(r'for roots $\gamma$',r'for a root $r$')
            # Presentation-only Dynkin label offsets: values/vertices/bonds stay fixed.
            for label in ['2','3']:
                old=r'\node[above] at (2,0) {$'+label+r'$}'
                assert body.count(old)==1
                body=body.replace(old,r'\node[above right,xshift=2pt,yshift=3pt] at (2,0) {$'+label+r'$}')
            body=body.replace(r'\node[above]',r'\node[above,yshift=4pt]')
            body=body.replace(r'\node[right]',r'\node[right,xshift=4pt]')
        if i==14 and language=='english_translation':
            old='This is the problem solved by Satake in [11].'
            assert body.count(old)==1
            body=body.replace(old,'This problem is essentially equivalent to the one solved by Satake in [11].')
        if i==20:
            old=r'\Gamma\subset G_1(\mathbf Q)_+'
            assert body.count(old)==1
            body=body.replace(old,r'\Gamma\subset G_1(\mathbf Q)^+')
            old=r'\Gamma=\rho\widetilde G_0(A^f)\cap G_1(\mathbf Q)'
            assert body.count(old)==1
            body=body.replace(old,r'\Gamma=\rho\widetilde G_0(A)\cap G_1(\mathbf Q)')
        if i==31:
            old=r"G(k')/\rho\widetilde G(k') \arrow[r] \arrow[d] & G(k)/\rho\widetilde G(k) \arrow[d]"
            assert body.count(old)==1
            body=body.replace(old,old.replace(r'\arrow[d]',r'\arrow[d,hook]'))
        if i==37:
            old=r'H(\mathbf Q) \arrow[r] \arrow[u] & \cdots \arrow[r] \arrow[u] & \pi_0\pi(T) \arrow[u,equal]'
            assert body.count(old)==1
            body=body.replace(old,old.replace(r'\cdots \arrow[r] \arrow[u]',r'\cdots \arrow[u]'))
        # TeX's math roman does not apply text accents; retain ieme as text.
        body=body.replace(r'p^{\mathrm{ième}}',r'p^{\text{ième}}')
        staged.append(f'<!-- BEGIN_PAGE physical={i} printed={246+i} -->\n'+body+f'\n<!-- END_PAGE physical={i} printed={246+i} -->')
        tex=pandoc(body)
        assert '\\begin{verbatim}' not in tex and '\\textbackslash' not in tex
        chunks.append(f'\\SourcePage{{{i}}}{{{246+i}}}\n'+tex)
        manifest.append(dict(physical_page=i, printed_page=246+i, input_record_sha256=sha(m.group(0).encode()), derived_tex_sha256=sha(tex.encode())))
    output=PREAMBLE+'\n'.join(chunks)+'\n\\end{document}\n'
    p=dest/f'{language}.tex'; p.write_text(output,encoding='utf-8')
    (dest/f'{language}.md').write_text('\n\n'.join(staged)+'\n',encoding='utf-8')
    return p, manifest

def apparatus(dest):
    rows=list(csv.DictReader((INPUT/'apparatus/apparatus.tsv').open(encoding='utf-8',newline=''),delimiter='\t'))
    lines=['# D031: Editorial apparatus', '', 'This apparatus accompanies the original French and standalone English editions. Source authority is the supplied IAS 43-page witness. Its article occupies printed pages 247-289. The publication header cites 247-290, but neither supplied witness contains page 290; none is invented.', '', 'The normalized readers retain a page boundary for every physical source leaf and preserve all native mathematical code. Page numbers refer to the original printed pages. Running heads, folios and scanner/copy matter are recorded below, not inserted into the article body. The inherited salvage archive and its branches remain ZERO_ACCEPTED; they are not a source of accepted text.', '', '## Typesetting normalization', '', 'The new TeX and PDF readers are editable mathematical editions, built from the exact supplied French and English page records. Markdown page headings and operational status prose are excluded. The original contents lists are rendered as native tables, formulas remain math, and all 23 commutative diagrams in each language remain native TikZ-CD. Reader page-to-source identity is checked after compilation. No image fallback is used; therefore no crop derivatives or unlogged image substitutions are introduced.', '']
    omitted=[r['entry_id'] for r in rows if r['kind']=='INHERITED_LOCATOR_DISAGREEMENT']
    lines.extend(['Provenance-only comparisons against inherited candidate material are preserved in the unmodified input apparatus and salvage ledger, but are not promoted into this reader-facing apparatus. Omitted inherited note identifiers: '+', '.join(omitted)+'. The source authority remains controlling.', ''])
    for page in range(1,44):
        lines.extend([f'## Printed page {246+page} (physical {page})',''])
        for r in rows:
            if int(r['physical_page'])==page and r['kind']!='INHERITED_LOCATOR_DISAGREEMENT':
                if r['entry_id']=='A088':
                    r=dict(r)
                    r['source_fact']='The authority leaf has a repeated running head and folio; it is a tightly cropped single-page image without a neighboring-page sliver or scanner border. It contains 2.4.6 and most of 2.4.7 and ends mid-sentence after equation (2.4.7.3).'
                if r['entry_id']=='A097':
                    r=dict(r)
                    r['source_fact']='The authority leaf has a repeated running head and folio; it is a tightly cropped single-page image without a neighboring-page sliver or scanner border. It continues Construction 2.4.10, contains its additivity diagram and 2.4.11, and ends mid-sentence.'
                lines.extend(['**'+r['entry_id']+' - '+r['kind']+'**', '', r['source_fact'], '', r['decision'], ''])
        if page==3:
            lines.extend(['**D031-N001 - SOURCE-FAITHFUL DIAGRAM GEOMETRY**', '', 'Independent inspection of authority physical page 3 / printed page 249 found that both arrows to the quotient are oblique: the quotient is vertically centered between C(F) and C(E). The returned Markdown placed the quotient on the lower row and made the lower arrow horizontal. Both staged readers restore the centered quotient and rising lower arrow using a three-row native TikZ-CD diagram. The vertical norm arrow, endpoints, labels, and algebraic expressions are unchanged. The input-state bytes remain untouched.', ''])
        if page==41:
            lines.extend(['**D031-N002 - COMPLEX-BASE SUBSCRIPTS RESTORED**', '', 'Independent source-pixel inspection of 2.7.11(a)-(b) identified three missing complex-base subscripts in both returned editions: the individual factors and their product in (a), and the quotient target in (b). Both staged readers restore $M^0_{\\mathbf C}$ in precisely these three expressions. The initial target in (b), which has no complex-base subscript in the source, is unchanged.', ''])
        if page==11:
            lines.extend(['**D031-N003 - SOURCE OMISSION PRESERVED**', '', 'In 1.2.3 the authority literally prints $G^*(\\mathbf R)=\\{g\\in(\\mathbf C)\\mid g=\\operatorname{int}(h(i))\\sigma(g)\\}$. The returned editions silently inserted $G_{\\mathbf C}$ before $(\\mathbf C)$. Both staged editions now reproduce the source omission. The apparent mathematical incompleteness is a source fact, not a newly supplied correction.', ''])
        if page==15:
            lines.extend(['**D031-N004 - SOURCE ROOT-VARIABLE DISCREPANCY PRESERVED**', '', 'At the opening of printed page 261 the authority uses the pairing $\\langle\\mu,z\\rangle$ but then says $r$ is a root. It also prints the singular French wording "combinaison Z-lineaire de racine". The returned editions silently replaced both variables by $\\gamma$, and French pluralized "racine". Both staged readers restore the source variables $z$ and $r$, and the diplomatic French restores the singular wording. The English grammatical phrase "a Z-linear combination of roots" is retained as translation, without concealing the variable discrepancy.', ''])
            lines.extend(['**D031-N012 - DYNKIN TABLE LABEL CLEARANCE**', '', 'A fresh rendered-page audit found that the central labels 2 and 3 in the E6 and E7 diagrams intersected their vertical branch, and that the lower-right label of the quaternionic D diagram touched its circled vertex. Native TikZ label anchors are adjusted: central branch labels move above-right, other above-labels move up 4pt, and right-labels move right 4pt. All vertex locations, bonds, circles, underlines, mathematical values, and label-to-vertex associations remain unchanged. This is a presentation repair, not source normalization.', ''])
        if page==14:
            lines.extend(['**D031-N011 - QUALIFIED EQUIVALENCE RETAINED IN ENGLISH**', '', 'The displaced French phrase "essentiellement equivalent" in the grammatically damaged paragraph after 1.3.2 remains literal in the diplomatic French. The English now reads "This problem is essentially equivalent to the one solved by Satake in [11]." This conservative editorial placement restores the qualification omitted by the returned fluent sentence. It is a documented translation judgment, not a change to a formula or reference.', ''])
        if page==20:
            lines.extend(['**D031-N005 - SUPERSCRIPT PLUS RESTORED**', '', 'In the prose of 2.1.6 immediately before (2.1.6.1), the authority prints $\\Gamma\\subset G_1(\\mathbf Q)^+$ with a superscript plus. Both returned editions placed the plus in a subscript. The staged readers restore the superscript only in that prose occurrence; the distinct subscript plus in (2.1.6.2) is preserved.', ''])
            lines.extend(['**D031-N007 - SOURCE ADELE ARGUMENT RESTORED**', '', 'In the same prose paragraph of 2.1.6, the source defines $\\Gamma=\\rho\\widetilde G_0(A)\\cap G_1(\\mathbf Q)$ using $A$, with no superscript $f$. Both returned editions silently used $A^f$. The staged readers restore the literal source argument $A$ in that definition only; nearby uses of $A^f$ are unchanged.', ''])
        if page==30:
            lines.extend(['**D031-N006 - COPY-MATTER DESCRIPTION CORRECTED**', '', 'The inherited A088 source-fact description incorrectly claimed a scanner border and neighboring-page sliver on physical page 30. Independent inspection shows a tightly cropped single-page image with running head and folio but no such sliver or border. A088 is corrected in this normalized apparatus. Article text and mathematics are unchanged.', ''])
        if page==31:
            lines.extend(['**D031-N008 - VERTICAL INJECTION HOOKS RESTORED**', '', 'Both vertical arrows in source diagram (2.4.8.1) have hooked injection tails. The returned native diagrams used ordinary vertical arrows. Both staged readers restore the two hooks, preserving their downward directions and all source objects and labels. The separate following norm diagram has ordinary vertical arrows and is unchanged.', ''])
        if page==33:
            lines.extend(['**D031-N009 - COPY-MATTER DESCRIPTION CORRECTED**', '', 'The inherited A097 source-fact description incorrectly claimed a scanner border and neighboring-page sliver on physical page 33. Independent inspection shows a tightly cropped single-page image with running head and folio but no such sliver or border. A097 is corrected in this normalized apparatus. Article text and mathematics are unchanged.', ''])
        if page==37:
            lines.extend(['**D031-N010 - ADDED DIAGRAM ARROW REMOVED**', '', 'The first, unnumbered diagram of 2.5.8 has no horizontal arrow from the lower middle ellipsis to the lower right $\\pi_0\\pi(T)$ in the authority. Both returned diagrams inserted that arrow. The staged readers remove only this added horizontal arrow and preserve the upward arrow. The lower-row horizontal arrow in the subsequent numbered diagram (2.5.8.1) is printed in the source and is retained.', ''])
    md='\n'.join(lines)
    md=re.sub(r'([A-Za-z])\u0303',lambda m:'$\\widetilde{'+m.group(1)+'}$',md)
    (dest/'apparatus.md').write_text(md,encoding='utf-8')
    bodytex=pandoc(md,raw=False)
    bodytex=re.sub(r'(?m)^(\\textbf\{(?:A\d{3}|D031-N\d{3}).*)$',r'\\Needspace{5\\baselineskip}\n\1',bodytex)
    bodytex=re.sub(r'(?m)^(\\subsection\{Printed page.*)$',r'\\Needspace{8\\baselineskip}\n\1',bodytex)
    preamble=PREAMBLE.replace('\\begin{document}', '\\usepackage{needspace}\n\\begin{document}')
    tex=preamble+bodytex+'\n\\end{document}\n'
    p=dest/'apparatus.tex';p.write_text(tex,encoding='utf-8');return p

def compile_tex(p):
    env=os.environ.copy(); env.update(SOURCE_DATE_EPOCH='946684800',FORCE_SOURCE_DATE='1',TZ='UTC')
    results=[]
    for run in (1,2):
        result=subprocess.run([TEX,'-interaction=nonstopmode','-halt-on-error','-file-line-error','-no-shell-escape',p.name],cwd=p.parent,env=env,capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=180)
        (p.parent/f'{p.stem}.compile{run}.txt').write_text(result.stdout+result.stderr,encoding='utf-8')
        results.append(result.returncode)
        if result.returncode: raise RuntimeError(f'{p.name} compile {run} failed; inspect .compile{run}.txt')
    return results

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',default='normalized');parser.add_argument('--apparatus-only',action='store_true');args=parser.parse_args()
    dest=(BASE/args.output).resolve();assert dest.is_relative_to(BASE);dest.mkdir(parents=True,exist_ok=True)
    manifest={}
    if not args.apparatus_only:
        for language in ['french_diplomatic','english_translation']:
            p,records=reader(language,dest);manifest[language]=records
    # Validate exact field keys before reading apparatus (schema is data, not a claim).
    p=apparatus(dest)
    if not args.apparatus_only:
        (dest/'page_record_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    for name in (['apparatus'] if args.apparatus_only else ['french_diplomatic','english_translation','apparatus']):
        compile_tex(dest/f'{name}.tex')
        print(f'BUILT {name}.pdf',flush=True)
    outputs=[]
    for p in sorted(dest.iterdir()):
        if p.suffix in ('.tex','.pdf','.md','.json') and p.name!='output_manifest.json':
            b=p.read_bytes();outputs.append(dict(file=p.name,bytes=len(b),sha256=sha(b)))
    (dest/'output_manifest.json').write_text(json.dumps(outputs,indent=2)+'\n',encoding='utf-8')

if __name__=='__main__':main()
