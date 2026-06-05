#!/usr/bin/env python3
"""Build al-Battani's zodiac auxiliary tables (T03): the planetary TERMS (Egyptian
bounds) and the FACES (decans). Consumes grind/wf_zodiac.json produced from the
parallel transcription workflow:
  {"terms": {"found":bool,"pages":str,"signs":[{"sign","terms":[{"planet","from_deg","to_deg"}]}]},
   "faces": {"found":bool,"pages":str,"signs":[{"sign","faces":[{"decan","planet"}]}]}}
Emits a XeLaTeX edition. Defensive: renders whatever blocks are present.
"""
import json, os, subprocess
HERE=os.path.dirname(os.path.abspath(__file__))
SRC=os.path.join(os.path.dirname(os.path.dirname(HERE)),'grind','wf_zodiac.json')
SIGNS=['Aries','Taurus','Gemini','Cancer','Leo','Virgo','Libra','Scorpio','Sagittarius','Capricorn','Aquarius','Pisces']

PRE=r'''\documentclass[10pt,a4paper]{article}
\usepackage{fontspec}\usepackage[margin=1.6cm]{geometry}\usepackage{booktabs,array,longtable}
\setmainfont{Cambria}[Ligatures=TeX]\renewcommand{\arraystretch}{1.2}
\begin{document}
\begin{center}{\LARGE\bfseries al-Battānī — Zodiac Auxiliary Tables}\\[2pt]
{\large Planetary terms (bounds) and faces (decans)}\end{center}
\small\noindent Source: C.~A.~Nallino, \textit{Opus Astronomicum}, Pars~II. Terms = the Egyptian
planetary bounds (each sign split into five unequal segments by planet); faces = the three decans of
each sign and their ruling planets.\\[6pt]
'''

def terms_table(data):
    out=[r'\noindent{\large\bfseries Terms (Egyptian bounds)}\quad{\small pages '+str(data.get('pages',''))+r'}\\[2pt]',
         r'\begin{longtable}{l l l l l l}\toprule Sign & \multicolumn{5}{l}{Term (planet: degree range within the sign)}\\\midrule\endhead']
    for s in data.get('signs',[]):
        cells=[f"{t['planet']} {t['from_deg']}--{t['to_deg']}" for t in s.get('terms',[])]
        cells+=['']*(5-len(cells))
        out.append(f"{s['sign']} & "+' & '.join(cells[:5])+r' \\')
    out.append(r'\bottomrule\end{longtable}\vspace{4pt}')
    return '\n'.join(out)

def faces_table(data):
    out=[r'\noindent{\large\bfseries Faces (decans)}\quad{\small pages '+str(data.get('pages',''))+r'}\\[2pt]',
         r'\begin{longtable}{l c c c}\toprule Sign & 1st face (0--10°) & 2nd (10--20°) & 3rd (20--30°)\\\midrule\endhead']
    for s in data.get('signs',[]):
        f={x['decan']:x['planet'] for x in s.get('faces',[])}
        out.append(f"{s['sign']} & {f.get(1,'')} & {f.get(2,'')} & {f.get(3,'')} "+r'\\')
    out.append(r'\bottomrule\end{longtable}')
    return '\n'.join(out)

def main():
    if not os.path.exists(SRC):
        print('no wf_zodiac.json yet'); return
    z=json.load(open(SRC,encoding='utf-8'))
    body=[PRE]
    if z.get('terms',{}).get('signs'): body.append(terms_table(z['terms']))
    else: body.append(r'\noindent\textit{Terms table: not recovered from the Latin volume.}\\[6pt]')
    if z.get('faces',{}).get('signs'): body.append(faces_table(z['faces']))
    else: body.append(r'\noindent\textit{Faces table: not recovered from the Latin volume.}')
    body.append(r'\end{document}')
    tex=os.path.join(HERE,'al_battani_zodiac_tables.tex')
    open(tex,'w',encoding='utf-8').write('\n'.join(body))
    r=subprocess.run(['xelatex','-interaction=nonstopmode','-halt-on-error',os.path.basename(tex)],cwd=HERE,capture_output=True,text=True)
    print('COMPILE OK' if os.path.exists(tex[:-4]+'.pdf') and r.returncode==0 else 'COMPILE ISSUE')

if __name__=='__main__': main()
