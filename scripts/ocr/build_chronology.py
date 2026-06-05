#!/usr/bin/env python3
"""Build al-Battani's chronology tables (T01): calendar ERAS and the CANON OF KINGS
(regnal years). Consumes grind/wf_chrono.json from the parallel transcription workflow:
  {"eras":  {"found":bool,"pages":str,"eras":[{"name","detail"}]},
   "kings": {"found":bool,"pages":str,"dynasties":[{"name","rulers":[{"ruler","years"}]}]}}
Emits a XeLaTeX edition. Defensive: renders whatever blocks are present.
"""
import json, os, subprocess
HERE=os.path.dirname(os.path.abspath(__file__))
SRC=os.path.join(os.path.dirname(os.path.dirname(HERE)),'grind','wf_chrono.json')

def esc(s):
    return str(s or '').replace('&',r'\&').replace('%',r'\%').replace('_',r'\_').replace('#',r'\#')

PRE=r'''\documentclass[10pt,a4paper]{article}
\usepackage{fontspec}\usepackage[margin=1.6cm]{geometry}\usepackage{booktabs,array,longtable}
\setmainfont{Cambria}[Ligatures=TeX]\renewcommand{\arraystretch}{1.2}
\begin{document}
\begin{center}{\LARGE\bfseries al-Battānī — Chronological Tables}\\[2pt]
{\large Calendar eras and the canon of kings}\end{center}
\small\noindent Source: C.~A.~Nallino, \textit{Opus Astronomicum}, Pars~II — the eras section and the
\textit{Tabula regum} (al-Battānī's recension of Ptolemy's \textit{Canon of Kings}, pp.~449--454),
which he extends from Nabonassar down to the Umayyad caliphs. \textbf{Reliability note:} ruler names,
dynastic order, and the Rāshidūn/Umayyad caliph reign-lengths (y\,m\,d) are sound; the \emph{ancient}
regnal-year figures were read by automated transcription and must be collated against the printed table
(the reading confused the regnal and cumulative columns in places). The era epochs are the standard
historical values; the framework (which eras, and their intervals) is al-Battānī's.\\[6pt]
'''

def eras_block(d):
    out=[r'\noindent{\large\bfseries Calendar eras}\quad{\small pages '+esc(d.get('pages',''))+r'}\\[2pt]',
         r'\begin{longtable}{l >{\raggedright\arraybackslash}p{11cm}}\toprule Era & Detail\\\midrule\endhead']
    for e in d.get('eras',[]):
        out.append(f"{esc(e.get('name'))} & {esc(e.get('detail'))}"+r' \\')
    out.append(r'\bottomrule\end{longtable}\vspace{4pt}')
    return '\n'.join(out)

def kings_block(d):
    out=[r'\noindent{\large\bfseries Canon of kings (regnal years)}\quad{\small pages '+esc(d.get('pages',''))+r'}\\[2pt]']
    for dyn in d.get('dynasties',[]):
        out.append(rf"\noindent\textbf{{{esc(dyn.get('name'))}}}\\[1pt]")
        out.append(r'\begin{longtable}{>{\raggedright\arraybackslash}p{9cm} l}\toprule Ruler & Years\\\midrule\endhead')
        for r0 in dyn.get('rulers',[]):
            out.append(f"{esc(r0.get('ruler'))} & {esc(r0.get('years'))}"+r' \\')
        out.append(r'\bottomrule\end{longtable}\vspace{3pt}')
    return '\n'.join(out)

def main():
    if not os.path.exists(SRC):
        print('no wf_chrono.json yet'); return
    c=json.load(open(SRC,encoding='utf-8'))
    body=[PRE]
    if c.get('eras',{}).get('eras'): body.append(eras_block(c['eras']))
    else: body.append(r'\noindent\textit{Eras table: not recovered as a clean table from the Latin volume.}\\[6pt]')
    if c.get('kings',{}).get('dynasties'): body.append(kings_block(c['kings']))
    else: body.append(r'\noindent\textit{Canon of kings: not recovered from the Latin volume.}')
    body.append(r'\end{document}')
    tex=os.path.join(HERE,'al_battani_chronology_tables.tex')
    open(tex,'w',encoding='utf-8').write('\n'.join(body))
    r=subprocess.run(['xelatex','-interaction=nonstopmode','-halt-on-error',os.path.basename(tex)],cwd=HERE,capture_output=True,text=True)
    print('COMPILE OK' if os.path.exists(tex[:-4]+'.pdf') and r.returncode==0 else 'COMPILE ISSUE')

if __name__=='__main__': main()
