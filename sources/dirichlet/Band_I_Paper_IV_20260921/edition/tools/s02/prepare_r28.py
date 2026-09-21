"""Create page-bounded derivatives of R28 after visual collation, never modify salvage."""
from pathlib import Path
import re,textwrap,json
ROOT=Path(__file__).resolve().parents[2]
MAP={
75:['par.001','eq.001','par.002','eq.002','par.003','eq.003','eq.004','par.004','eq.005'],
76:['par.005','eq.006','par.006','eq.007','eq.008','par.007','eq.009','eq.010','par.008','eq.011'],
77:['par.009','eq.012','par.010','eq.013','par.011','par.012','par.013','par.014a'],
78:['par.014b','thm.001','par.015','par.016','par.017','par.018','par.019'],
79:['sec.005','par.020','par.021','eq.014','par.022','eq.015','eq.016','eq.017','eq.018a'],
80:['eq.018b','par.023','eq.019','par.024','par.025','par.026','eq.020','par.027','eq.021']}
PARSTART={'par.010','par.011','par.012','par.013','par.014a','par.015','par.016','par.017','par.018','par.019','par.020','par.021','par.023','par.024','par.025','par.026','par.027'}
for lang,sub in [('fr','orig'),('en','en')]:
    src=next((ROOT/'inherited/R28').glob(f'*/new/{sub}/tex/*.tex'))
    raw=src.read_text();ids=list(re.finditer(r'\\unitid\{dirichlet\.v1\.p04b\.(?:en\.)?([^}]+)\}',raw))
    u={}
    for i,m in enumerate(ids):
        s=raw[m.end():ids[i+1].start() if i+1<len(ids) else raw.index(r'\end{document}')].strip()
        s=s.replace(r'\begin{center}','').replace(r'\end{center}','').strip()
        s=s.replace(r'\pmod b',r'\md{b}')
        if lang=='fr':s=s.replace('»','„').replace('«','“')
        else:s=s.replace(r'\emph{Théorie des Nombres}',r'\emph{Theory of Numbers}')
        s=re.sub(r'\\\[\s*\((\\[a-z]+\x27?)\)\\qquad\s*',lambda m:r'\begin{equation*}\tag{$'+m[1]+'$}\n',s)
        if r'\begin{equation*}' in s:s=s.replace(r'\]',r'\end{equation*}',1)
        u[m[1]]=s
    # Source-bound division, not prose bridging.
    split=' de $b$' if lang=='fr' else ' of $b$'
    a,b=u['par.014'].split(split,1)
    u['par.014a']=a;u['par.014b']=split.strip()+b
    # The source leaves h, at the foot of 79; h', h'', ... begin 80.
    split="$h$, $h'$, $h''$, \\ldots{}"
    a,b=u['eq.018'].split(split,1)
    u['eq.018a']=a+'$h$,';u['eq.018b']="$h'$, $h''$, \\ldots{}"+b
    u['sec.005']=r'\sectionnumber{5}'
    u['thm.001']=r'\sourceheading{'+('Théorème I.' if lang=='fr' else 'Theorem I.')+'}'
    # Match source paragraph punctuation in the English without altering the argument.
    if lang=='en':
        replacements={
        'par.001':[("odd), and suppose", "odd) and suppose"),("common divisor; and since", "common divisor, and since")],
        'par.003':[("relatively prime); and it is known, by a known theorem that follows easily", "relatively prime) and one knows by a known theorem that follows easily"),("no. 197), that every", "no. 197) that every")],
        'par.004':[("with respect to $b$; so that", "with respect to $b$, so that")],
        'par.008':[("result: if", "result: If")],
        'par.013':[("$t^2\\pm c\\delta u^2=p$ is soluble", "$t^2\\pm c\\delta u^2=p$, is soluble")],
        'par.015':[("supposed even), one", "supposed even) one"),("$p$: if", "$p$: If"),("biquadratic residue according", "biquadratic residue, according")],
        'par.016':[("$b=7$, etc.", "$b=7$ etc.")],
        'par.017':[("supposed even), one", "supposed even) one")],
        'par.018':[("with respect to $p$ if", "with respect to $p$, if")],
        'par.020':[("$p=t^2-au^2$, where", "$p=t^2-au^2$ where")],
        'par.025':[("therefore be even when", "therefore be even, when")],
        }
        for key,repls in replacements.items():
            for before,after in repls:
                assert before in u[key],(key,before)
                u[key]=u[key].replace(before,after)
    for page,keys in MAP.items():
        out=f'% Authority: exact-scope leaf {page-62}; full PDF page {page+17}; printed p.{page}.\n'
        for key in keys:
            structure='paragraph-start' if key in PARSTART else ('heading' if key.startswith(('thm','sec')) else 'continuation')
            out+=f'% U:p{page:03d}.r28.{key} | {structure}; R28 {key} visually replayed\n'
            if key.startswith('par.') or key=='eq.018b':
                out+=('\\par\\indent\n' if structure=='paragraph-start' else '\\par\\noindent\n')
            content=u[key]
            # wrap source code only; re-typeset lineation is explicitly documented
            out+='\n'.join(textwrap.fill(line,width=98,break_long_words=False,break_on_hyphens=False) if not line.startswith('\\') else line for line in content.splitlines())+'\n'
        (ROOT/f'editions/{lang}/pages/p{page:03d}.tex').write_text(out)
print('Wrote corrected, page-bounded R28 derivatives 75–80, French and English.')
