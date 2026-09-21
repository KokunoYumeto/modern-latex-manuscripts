"""Rebuild existing cumulative editable S03 sources twice and render every page.
Never regenerates or resets the author's text. Requires XeLaTeX and PyMuPDF.
"""
from pathlib import Path
import os,subprocess,shutil,json,re,fitz
R=Path(__file__).resolve().parents[2];Q=R/'qa/s03';receipts={}
for layer,cwd,fn in [('fr',R/'editions/fr','PAPER_IV_FR_PP065_098.pdf'),('en',R/'editions/en','PAPER_IV_EN_PP065_098.pdf'),('apparatus',R/'apparatus','PAPER_IV_APPARATUS_S03.pdf')]:
 out=Q/'build'/layer;out.mkdir(parents=True,exist_ok=True);rows=[]
 for i in (1,2):
  cmd=['xelatex','-interaction=nonstopmode','-halt-on-error',f'-output-directory={out}','main.tex']
  p=subprocess.run(cmd,cwd=cwd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,env={**os.environ,'SOURCE_DATE_EPOCH':'1790006400','FORCE_SOURCE_DATE':'1'})
  (out/f'pass{i}.stdout.txt').write_text(p.stdout)
  if (out/'main.log').exists():shutil.copyfile(out/'main.log',out/f'pass{i}.log')
  print(layer,i,p.returncode,p.stdout[-240:])
  if p.returncode:raise RuntimeError('Inspect and repair the LaTeX error before continuing.')
  log=(out/'main.log').read_text()
  rows.append({'pass':i,'exit_code':p.returncode,'warnings':re.findall(r'^.*Warning.*$',log,re.M),'overfull':re.findall(r'^Overfull.*$',log,re.M),'underfull':re.findall(r'^Underfull.*$',log,re.M),'missing_glyphs':re.findall(r'^Missing character:.*$',log,re.M)})
 shutil.copyfile(out/'main.pdf',R/'readers'/fn);doc=fitz.open(out/'main.pdf');rd=Q/'visual'/layer;rd.mkdir(parents=True,exist_ok=True)
 for i,page in enumerate(doc):
  name=f'page{i+1:02}_p{i+65:03}.png' if layer!='apparatus' else f'page{i+1:02}.png'
  page.get_pixmap(matrix=fitz.Matrix(1.75,1.75),alpha=False).save(rd/name)
 (Q/f'EXTRACTED_TEXT_{layer.upper()}.txt').write_text('\f'.join(p.get_text() for p in doc))
 receipts[layer]={'engine':'XeLaTeX','passes':rows,'pages':len(doc),'reader':f'readers/{fn}','render_dpi':126}
(Q/'BUILD_RUNS.json').write_text(json.dumps(receipts,ensure_ascii=False,indent=2)+'\n')
(Q/'XELATEX_VERSION.txt').write_text(subprocess.check_output(['xelatex','--version'],text=True))
print(json.dumps(receipts,indent=2))
