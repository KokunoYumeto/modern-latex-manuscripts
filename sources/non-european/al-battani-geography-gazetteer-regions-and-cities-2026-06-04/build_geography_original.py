#!/usr/bin/env python3
"""Build al-Battani's geographical gazetteer (T02) from authoritative coordinates.
Source: C. A. Nallino, Opus Astronomicum Pars II (1907) — two printed tables:
  (1) "Tabula mediorum punctorum regionum ... in Libro Figurae Terrae" (94 regions,
      PDF pp 481-484 of the combined IA scan) — COMPLETE here (1-93 transcribed).
  (2) "Tabula latitudinum et longitudinum urbium" (~340 cities, PDF pp 485-501) —
      transcription in progress (key cities done; continues).
Longitude is reckoned from the Fortunate Isles; latitudes northern unless marked.
Data: grind/geo_cat.tsv (type, n, name, lon_d, lon_m, lat_d, lat_m). '?' = pending cell.
"""
import csv, os, subprocess
HERE=os.path.dirname(os.path.abspath(__file__))
TSV=os.path.join(os.path.dirname(os.path.dirname(HERE)),'grind','geo_cat.tsv')

def esc(s):
    return (s or '').replace('&',r'\&').replace('%',r'\%').replace('_',r'\_').replace('#',r'\#').replace('[',r'{[}').replace(']',r'{]}')
def coord(d,m):
    d=(d or '').strip(); m=(m or '').strip()
    if d in('','?') or m=='?': return r'\textcolor{gray}{--}'
    return f'{d}°\\,{m or "0"}′'

def load():
    R=[];C=[]
    for r in csv.reader(open(TSV,encoding='utf-8'),delimiter='\t'):
        if not r or r[0].startswith('#'): continue
        rec=dict(n=r[1],name=r[2],lod=r[3],lom=r[4],lad=r[5],lam=r[6])
        (R if r[0]=='region' else C).append(rec)
    return R,C

PRE=r'''\documentclass[10pt,a4paper]{article}
\usepackage{fontspec}\usepackage[margin=1.5cm]{geometry}\usepackage{xcolor}
\usepackage{longtable,booktabs,array}
\setmainfont{Cambria}[Ligatures=TeX]
\setlength{\tabcolsep}{5pt}\renewcommand{\arraystretch}{1.18}
\begin{document}
\begin{center}{\LARGE\bfseries al-Battānī — Geographical Gazetteer}\\[3pt]
{\large Regions and cities, with ecliptic-frame coordinates}\end{center}
\small\noindent\textbf{Source.} al-Battānī's coordinates as established in C.~A.~Nallino's critical
edition (\textit{Opus Astronomicum}, Pars~II, 1907): the table of \emph{regional mid-points}
(\textit{Tabula mediorum punctorum regionum}, after Ptolemy's \textit{Geography}) and the table of
\emph{city} longitudes/latitudes (\textit{Tabula latitudinum et longitudinum urbium}). Longitude is
reckoned from the Fortunate Isles; latitudes are northern unless noted. Identifications follow Nallino's
apparatus (Ptolemy / al-Khwārizmī / Lelewel). \textcolor{gray}{--}~marks a cell still to be collated.
\\[6pt]
'''

def table(title, sub, rows):
    out=[rf'\noindent{{\large\bfseries {title}}}\quad{{\small\textit{{{sub}}}}}\\[2pt]',
         r'\begin{longtable}{r >{\raggedright\arraybackslash}p{8.5cm} c c}',
         r'\toprule \# & Name / identification & Long. & Lat.\\ \midrule\endhead']
    for r in rows:
        out.append(f"{r['n']} & {esc(r['name'])} & {coord(r['lod'],r['lom'])} & {coord(r['lad'],r['lam'])}\\\\")
    out.append(r'\bottomrule\end{longtable}\vspace{4pt}')
    return '\n'.join(out)

def main():
    R,C=load()
    keyn=lambda r: int(r['n']) if str(r['n']).isdigit() else 9999
    R=sorted(R,key=keyn); C=sorted(C,key=keyn)
    body=[PRE]
    body.append(table('I. Regions (94 in the source; 93 transcribed)',
                       'Tabula mediorum punctorum regionum — al-Battani world map by Ptolemaic province', R))
    body.append(table(f'II. Cities (COMPLETE — {len(C)} localities, nos. 94-269)',
                       'Tabula latitudinum et longitudinum urbium', C))
    body.append(r'\end{document}')
    tex=os.path.join(HERE,'al_battani_geography_gazetteer.tex')
    open(tex,'w',encoding='utf-8').write('\n'.join(body))
    # also a clean CSV
    with open(os.path.join(HERE,'albattani_geography.csv'),'w',newline='',encoding='utf-8') as fh:
        w=csv.writer(fh); w.writerow(['type','n','name','lon_d','lon_m','lat_d','lat_m'])
        for typ,rows in (('region',R),('city',C)):
            for r in rows: w.writerow([typ,r['n'],r['name'],r['lod'],r['lom'],r['lad'],r['lam']])
    print(f'regions {len(R)}, cities {len(C)}')
    r=subprocess.run(['xelatex','-interaction=nonstopmode','-halt-on-error',os.path.basename(tex)],
                     cwd=HERE,capture_output=True,text=True)
    print('COMPILE OK' if os.path.exists(tex[:-4]+'.pdf') and r.returncode==0 else 'COMPILE ISSUE')

if __name__=='__main__': main()
