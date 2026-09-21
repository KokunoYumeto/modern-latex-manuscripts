"""Clean, reproducible XeLaTeX builds and fresh full-reader rasters.
The first pass initializes cross-references; passes 2 and 3 are the two final
passes. This script never regenerates the diplomatic text. Run from any cwd.
"""
from pathlib import Path
import os,subprocess,shutil,json,re,hashlib
import fitz
from audit_support import R,Q,preserve,h
receipts={}
for layer,rel,fn in [('fr','editions/fr','PAPER_IV_FR_PP065_098.pdf'),('en','editions/en','PAPER_IV_EN_PP065_098.pdf'),('apparatus','apparatus','PAPER_IV_APPARATUS_S04.pdf')]:
 cwd=R/rel;out=Q/'build'/layer
 if out.exists():
  i=1
  while (Q/f'build_attempts/attempt{i:02}/{layer}').exists():i+=1
  target=Q/f'build_attempts/attempt{i:02}/{layer}';target.parent.mkdir(parents=True,exist_ok=True);shutil.move(out,target)
 out.mkdir(parents=True);runs=[]
 for n in (1,2,3):
  cmd=['xelatex','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','-recorder',f'-output-directory={out}','main.tex']
  result=subprocess.run(cmd,cwd=cwd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,env={**os.environ,'SOURCE_DATE_EPOCH':'1790006400','FORCE_SOURCE_DATE':'1'})
  (out/f'pass{n}.stdout.txt').write_text(result.stdout)
  if (out/'main.log').exists():shutil.copyfile(out/'main.log',out/f'pass{n}.log')
  if result.returncode:raise RuntimeError(f'{layer} pass{n}: repair actual build error; logs retained')
  log=(out/'main.log').read_text();alerts={key:re.findall(pat,log,re.M) for key,pat in [('warnings',r'^.*Warning.*$'),('overfull',r'^Overfull.*$'),('underfull',r'^Underfull.*$'),('missing_glyphs',r'^Missing character:.*$')]}
  runs.append({'pass':n,'purpose':'clean-directory initialization' if n==1 else 'final acceptance pass','exit_code':result.returncode,**alerts,'pdf_sha256':h((out/'main.pdf').read_bytes())})
  print(layer,n,alerts,flush=True)
 dest=R/'readers'/fn
 if dest.exists():preserve(str(dest.relative_to(R)))
 shutil.copyfile(out/'main.pdf',dest)
 doc=fitz.open(dest);vis=Q/'visual'/layer;vis.mkdir(parents=True,exist_ok=True);renders=[]
 for i,page in enumerate(doc):
  name=f'page{i+1:02}_p{i+65:03}.png' if layer!='apparatus' else f'page{i+1:02}.png';pix=page.get_pixmap(matrix=fitz.Matrix(1.75,1.75),alpha=False);image=vis/name;pix.save(image)
  renders.append({'reader_page':i+1,'printed_page':i+65 if layer!='apparatus' else None,'image':str(image.relative_to(R)),'bytes':image.stat().st_size,'sha256':h(image.read_bytes()),'raw_pixel_sha256':h(pix.samples),'extracted_text_sha256':h(page.get_text().encode())})
 (Q/f'EXTRACTED_TEXT_{layer.upper()}.txt').write_text('\f'.join(page.get_text() for page in doc))
 (Q/f'PDF_METADATA_{layer.upper()}.json').write_text(json.dumps({'metadata':doc.metadata,'bookmarks':doc.get_toc(),'page_count':len(doc)},indent=2)+'\n')
 receipts[layer]={'engine':'XeLaTeX','source':rel+'/main.tex','clean_directory_at_start':True,'passes':runs,'pages':len(doc),'reader':str(dest.relative_to(R)),'reader_sha256':h(dest.read_bytes()),'render_dpi':126,'renders':renders}
(Q/'BUILD_RUNS.json').write_text(json.dumps(receipts,indent=2)+'\n')
(Q/'XELATEX_VERSION.txt').write_text(subprocess.check_output(['xelatex','--version'],text=True))
for layer,row in receipts.items():
 assert all(not r[k] for r in row['passes'][1:] for k in ['warnings','overfull','underfull','missing_glyphs']),layer
 assert layer=='apparatus' or row['pages']==34
print('Clean final passes and page counts verified. Manual inspection still required.')
