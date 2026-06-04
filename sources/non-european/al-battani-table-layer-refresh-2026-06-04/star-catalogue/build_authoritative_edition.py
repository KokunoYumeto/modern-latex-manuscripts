#!/usr/bin/env python3
"""Typeset the COMPLETE al-Battani fixed-star catalogue (authoritative coordinates).
Reads albattani_catalogue_authoritative.csv (built by build_authoritative_catalogue.py)
and emits a professional XeLaTeX edition grouped by constellation in Ptolemaic order,
with the documented codex lacuna shown in place. Coordinates: Nallino Pars II (1907),
epoch 1191 Alexandri (~880 CE); longitude absolute ecliptic; N/S = plaga; magnitude =
al-Battani's rank. Modern Bayer/Flamsteed IDs and named stars from Nallino's margins.
"""
import csv, os, subprocess
HERE=os.path.dirname(os.path.abspath(__file__))
CSVF=os.path.join(HERE,'albattani_catalogue_authoritative.csv')

def esc(s):
    return (s or '').replace('&',r'\&').replace('%',r'\%').replace('_',r'\_').replace('#',r'\#')
def coord(d,m):
    d=(d or '').strip(); m=(m or '').strip()
    if d=='' and m=='': return '--'
    return f'{d}°\\,{m or "0"}′'

PRE=r'''\documentclass[9pt,a4paper]{extarticle}
\usepackage{fontspec}\usepackage{polyglossia}\usepackage{xeCJK}\usepackage{bidi}
\usepackage[margin=1.3cm]{geometry}\usepackage{xcolor}\usepackage{longtable,booktabs,array}
\setotherlanguage{arabic}
\setmainfont{Cambria}[Ligatures=TeX]
\newfontfamily\arabicfont[Script=Arabic,Scale=1.12]{Amiri}
\setCJKmainfont{SimSun}
\newcommand{\ar}[1]{{\arabicfont\textarabic{#1}}}
\setlength{\tabcolsep}{4pt}\renewcommand{\arraystretch}{1.22}
\begin{document}
\begin{center}
{\LARGE\bfseries al-Battānī — Catalogue of the Fixed Stars}\\[2pt]
{\large \ar{جدول الكواكب الثابتة لمحمد بن جابر البتّاني}\quad·\quad 巴塔尼恒星表}\\[6pt]
\end{center}
\small
\noindent\textbf{Source \& method.} Coordinates and magnitudes are al-Battānī's, as
established in C.~A.~Nallino's critical edition (\textit{Al-Battānī sive Albatenii Opus
Astronomicum}, Pars~II, Milan 1907), printed table \textit{``Situs et magnitudines
stellarum fixarum anno 1191 a Dhū 'l-qarnayn''} (epoch $\approx$880~CE). Ecliptic
\textbf{longitude} is absolute (0--360°); \textbf{latitude} is north/south of the
ecliptic; \textbf{Dir.} gives the hemisphere (N\,=\,\textit{borealis}, S\,=\,\textit{australis});
\textbf{Mag.} is al-Battānī's magnitude rank (\ar{مراتب العظمة}; ``neb.''\,=\,nebulous,
``obsc.''\,=\,obscure). \textbf{ID} is Nallino's modern identification (Bayer/Flamsteed)
and the traditional proper name. Bright-star latitudes were independently checked against
modern values (e.g.\ Sirius $-39.6°$, Vega $+61.7°$, Arcturus $+30.7°$, Aldebaran $-5.5°$,
Fomalhaut $-21.1°$). Where the project's trilingual reading of the Arabic abjad table
aligns one-to-one, al-Battānī's Arabic star-description is given; the remaining Arabic
descriptions are being collated. Star order follows Ptolemy's \textit{Almagest}.\\[4pt]
\noindent\textbf{Coverage.} 485 stars in 47 of the 48 Ptolemaic figures. A leaf is
\textbf{missing from the Escorial codex} (Nallino: \textit{``desideratur in codice
folium''}) carrying \textbf{Argo Navis} (incl.\ Canopus), \textbf{Hydra}, and the first
stars of \textbf{Crater}; this lacuna is shown in place below, not silently closed.
\vspace{4pt}
'''

def main():
    rows=list(csv.DictReader(open(CSVF,encoding='utf-8')))
    body=[PRE]
    # group preserving order
    order=[]; groups={}
    for r in rows:
        c=r['const']
        if c not in groups: groups[c]=[]; order.append(c)
        groups[c].append(r)
    nstars=0
    for c in order:
        g=groups[c]
        if c=='LACUNA':
            body.append(r'''\vspace{3pt}\begin{center}\fbox{\parbox{0.92\textwidth}{\centering
\textbf{[ Lacuna in the source codex ]}\\ A leaf is missing here in the Escorial manuscript,
containing \textbf{Argo Navis} (with Canopus), \textbf{Hydra}, and the opening stars of
\textbf{Crater}. Recorded by Nallino; these stars are not recoverable from this witness.}}\end{center}\vspace{3pt}''')
            continue
        g0=g[0]
        head=f"{esc(g0['const_lat'])}"
        ar=g0['const_ar']; zh=g0['const_zh']; tr=esc(g0['const_artr'])
        body.append(rf'\vspace{{4pt}}\noindent{{\large\bfseries {head}}}\quad\ar{{{ar}}}\quad{{\small\textit{{{tr}}}}}\quad {zh}')
        body.append(r'\begin{longtable}{r l >{\raggedright\arraybackslash}p{6.7cm} c c c c}')
        body.append(r'\toprule \# & ID & Description (\ar{الوصف}) & Long. & Lat. & Dir. & Mag.\\ \midrule\endhead')
        for r0 in g:
            nstars+=1
            ident=esc(r0['bayer'])
            if r0['common']: ident=(ident+' 'if ident else '')+esc(r0['common'])
            desc=(r'\ar{%s}'%r0['arabic']) if r0['arabic'] else r'\textcolor{gray}{—}'
            body.append(f"{r0['n']} & {ident} & {desc} & {coord(r0['lon_d'],r0['lon_m'])} & "
                        f"{coord(r0['lat_d'],r0['lat_m'])} & {r0['dir']} & {esc(r0['mag'])}\\\\")
        body.append(r'\bottomrule\end{longtable}')
    body.append(rf'\vfill\begin{{center}}\small {nstars} stars · authoritative coordinates from Nallino (1907) · '
                r'compiled for the open trilingual edition.\end{center}')
    body.append(r'\end{document}')
    tex=os.path.join(HERE,'al_battani_catalogue_COMPLETE.tex')
    open(tex,'w',encoding='utf-8').write('\n'.join(body))
    print('stars typeset:',nstars)
    r=subprocess.run(['xelatex','-interaction=nonstopmode','-halt-on-error',os.path.basename(tex)],
                     cwd=HERE,capture_output=True,text=True)
    pdf=tex[:-4]+'.pdf'
    ok=os.path.exists(pdf) and r.returncode==0
    print('COMPILE OK' if ok else 'COMPILE ISSUE')
    if not ok: print(r.stdout[-1500:])

if __name__=='__main__': main()
