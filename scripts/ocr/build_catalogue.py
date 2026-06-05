#!/usr/bin/env python3
"""Build the al-Battani fixed-star catalogue edition from star_catalogue.csv.
Data is the single source of truth (also the reusable dataset). This emits the
LaTeX critical edition grouped by constellation. A trailing '?' on any numeric
value marks a doubtful cell (rendered with a red superscript ?); empty = not read.
CSV columns: constellation, const_ar, const_zh, n, arabic, roman, lon_d, lon_m, lat_d, lat_m, dir, mag, page, note
"""
import csv, os, subprocess
HERE=os.path.dirname(os.path.abspath(__file__))

def cell(v):
    v=(v or '').strip()
    if v=='': return r'\dg{--}'
    if v.endswith('?'): return v[:-1]+r'\dg{}'
    return v

def coord(d,m):
    if (d or '').strip()=='' and (m or '').strip()=='': return r'\dg{--}'
    return f'{cell(d)}°\\,{cell(m)}′'

PRE=r'''\documentclass[10pt,a4paper]{article}
\usepackage{fontspec}\usepackage{polyglossia}\usepackage{xeCJK}\usepackage{bidi}
\usepackage[margin=1.4cm]{geometry}\usepackage{xcolor}\usepackage{longtable,booktabs,array}
\setotherlanguage{arabic}
\setmainfont{Cambria}[Ligatures=TeX]
\newfontfamily\arabicfont[Script=Arabic,Scale=1.15]{Amiri}
\setCJKmainfont{SimSun}
\newcommand{\ar}[1]{{\arabicfont\textarabic{#1}}}
\newcommand{\dg}[1]{#1\textsuperscript{\textcolor{red}{?}}}
\setlength{\tabcolsep}{4pt}\renewcommand{\arraystretch}{1.28}
\begin{document}
\begin{center}{\LARGE\bfseries al-Battānī, \textit{Opus Astronomicum}}\\[3pt]
{\Large Fixed-Star Catalogue \quad\ar{جدول الكواكب الثابتة}\quad 恒星表}\\[4pt]
\small Critical edition from the Nallino 1899 scan. Romanization DIN 31635; ecliptic longitude/latitude;
N/S; magnitude = al-Battānī's rank (\ar{مراتب العظمة}). \textsuperscript{\textcolor{red}{?}} = cell doubtful
on the scan, pending collation. Star order and descriptions follow Ptolemy's \textit{Almagest}.\end{center}
\vspace{6pt}
'''

def main():
    rows=list(csv.DictReader(open(os.path.join(HERE,'star_catalogue.csv'),encoding='utf-8')))
    # group by constellation, preserving first-seen order
    order=[]; groups={}
    for r in rows:
        c=r['constellation']
        if c not in groups: groups[c]=[]; order.append(c)
        groups[c].append(r)
    body=[PRE]
    for c in order:
        g=groups[c]; ar=g[0].get('const_ar',''); zh=g[0].get('const_zh','')
        body.append(rf'\begin{{center}}{{\large\bfseries {c} \quad\ar{{{ar}}}\quad {zh}}}\end{{center}}')
        body.append(r'\begin{center}\begin{longtable}{r >{\raggedright}p{6.4cm} l c c c c}')
        body.append(r'\toprule \# & Description (\ar{الوصف}) & Romanization & Long. & Lat. & Dir. & Mag.\\ \midrule\endhead')
        for r in g:
            body.append(f"{r['n']} & \\ar{{{r['arabic']}}} & {r['roman']} & "
                        f"{coord(r['lon_d'],r['lon_m'])} & {coord(r['lat_d'],r['lat_m'])} & "
                        f"{cell(r['dir'])} & {cell(r['mag'])} \\\\")
        body.append(r'\bottomrule\end{longtable}\end{center}')
    body.append(r'\end{document}')
    tex=os.path.join(HERE,'al_battani_star_catalogue_EDITION.tex')
    open(tex,'w',encoding='utf-8').write('\n'.join(body))
    n_stars=len(rows); n_const=len(order)
    print(f'edition: {n_stars} stars, {n_const} constellations -> {os.path.basename(tex)}')
    r=subprocess.run(['xelatex','-interaction=nonstopmode','-halt-on-error',os.path.basename(tex)],
                     cwd=HERE,capture_output=True,text=True)
    pdf=tex[:-4]+'.pdf'
    print('COMPILE OK' if os.path.exists(pdf) and r.returncode==0 else 'COMPILE ISSUE (see log)')

if __name__=='__main__': main()
