"""Rebuild the independent cumulative readers; leave every S01 evidence file intact."""
from pathlib import Path
import os,shutil,subprocess,json,re,fitz
R=Path(__file__).resolve().parents[2]
for lang in ['fr','en']:
    path=R/f'editions/{lang}/main.tex'
    base=(R/f'prior_evidence/S01/editions/{lang}/main.tex').read_text()
    base=base.replace('pp.65–74','pp.65–86').replace('Prompt 01;', 'Prompt 02;')
    # This definition does not affect any previously accepted page.
    macro=r'\newcommand{\sourceheading}[1]{\par\vspace{12pt}{\centering\addfontfeatures{LetterSpace=3}#1\par}\vspace{4pt}}'+'\n'
    base=base.replace(r'\begin{document}',macro+r'\begin{document}')
    add=''
    for p in range(75,87):
        add+=f'\n\\clearpage\n\\setcounter{{page}}{{{p}}}\\pdfbookmark[0]{{{p}}}{{p{p}}}\n\\fancyfoot{{}}\n'
        if p==81:
            imprint="G. Lejeune Dirichlet’s Werke." if lang=='fr' else "G. Lejeune Dirichlet’s Works."
            add+=rf'\fancyfoot[L]{{\fontsize{{7}}{{9}}\selectfont {imprint}}}'+'\n'
        if p in (75,81,83):
            add+=rf'\fancyfoot[C]{{\small { {75:"10*",81:"11",83:"11*"}[p] }}}'+'\n'
        add+=rf'\input{{pages/p{p:03d}.tex}}'+'\n'
    path.write_text(base.replace(r'\end{document}',add+r'\end{document}'))
# Build all documents, including apparatus. Both final runs logged separately.
receipts={}
for layer,cwd,reader in [('fr',R/'editions/fr','PAPER_IV_FR_PP065_086.pdf'),('en',R/'editions/en','PAPER_IV_EN_PP065_086.pdf'),('apparatus',R/'apparatus','PAPER_IV_APPARATUS_S02.pdf')]:
    out=R/f'qa/s02/build/{layer}';out.mkdir(parents=True,exist_ok=True)
    rows=[]
    for i in (1,2):
        cmd=['xelatex','-interaction=nonstopmode','-halt-on-error',f'-output-directory={out}','main.tex']
        p=subprocess.run(cmd,cwd=cwd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,env={**os.environ,'SOURCE_DATE_EPOCH':'1790006400','FORCE_SOURCE_DATE':'1'})
        (out/f'pass{i}.stdout.txt').write_text(p.stdout)
        if (out/'main.log').exists():shutil.copyfile(out/'main.log',out/f'pass{i}.log')
        print(layer,i,p.returncode,p.stdout[-400:])
        if p.returncode:raise RuntimeError('Inspect and repair LaTeX error')
        log=(out/'main.log').read_text()
        rows.append({'pass':i,'exit_code':p.returncode,'warnings':re.findall(r'^.*Warning.*$',log,re.M),'overfull':re.findall(r'^Overfull.*$',log,re.M),'underfull':re.findall(r'^Underfull.*$',log,re.M),'missing_glyphs':re.findall(r'^Missing character:.*$',log,re.M)})
    shutil.copyfile(out/'main.pdf',R/'readers'/reader)
    doc=fitz.open(out/'main.pdf');rend=R/f'qa/s02/visual/{layer}';rend.mkdir(parents=True,exist_ok=True)
    for i,page in enumerate(doc):
        name=f'page{i+1:02d}_p{i+65:03d}.png' if layer!='apparatus' else f'page{i+1:02d}.png'
        page.get_pixmap(matrix=fitz.Matrix(1.75,1.75),alpha=False).save(rend/name)
    receipts[layer]={'engine':'XeLaTeX','passes':rows,'pages':len(doc),'reader':f'readers/{reader}','render_dpi':126}
(R/'qa/s02/BUILD_RUNS.json').write_text(json.dumps(receipts,ensure_ascii=False,indent=2)+'\n')
