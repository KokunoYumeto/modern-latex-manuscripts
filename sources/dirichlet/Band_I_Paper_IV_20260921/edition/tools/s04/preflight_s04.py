"""Post-collation regression, geometry, fonts and independent renderer checks.
These mechanical checks are explicitly not a substitute for the manual source audit.
"""
from pathlib import Path
import csv,json,re,subprocess,zipfile
import fitz
from audit_support import R,Q,h

build=json.loads((Q/'BUILD_RUNS.json').read_text())
review=json.loads((Q/'MANUAL_OUTPUT_REVIEW.json').read_text())
expected={f'{l}:{n}' for l,d in build.items() for n in range(1,d['pages']+1)}
assert set(review)==expected and len(review)==73
reg=[];bounds=[];fonts=[];poppler=[]
changed_expected={'fr':{65,72,73,89},'en':{65,68,72,73,74,88,89,90,91,92,93,96}}
for lang,d in build.items():
 path=R/d['reader'];assert h(path.read_bytes())==d['reader_sha256']
 doc=fitz.open(path);assert len(doc)==d['pages']
 assert d['clean_directory_at_start']
 for run in d['passes'][-2:]:
  assert run['exit_code']==0 and all(not run[k] for k in ('warnings','overfull','underfull','missing_glyphs'))
 assert d['passes'][-2]['pdf_sha256']==d['passes'][-1]['pdf_sha256']==d['reader_sha256']
 if lang in ('fr','en'):
  old=fitz.open(R/'history/S03/superseded'/d['reader']); assert len(old)==34
  toc=doc.get_toc(); assert len(toc)==34
 for i,p in enumerate(doc):
  rev=review[f'{lang}:{i+1}'];assert rev['reader_sha256']==h(path.read_bytes())
  assert rev['sha256']==h((R/rev['image']).read_bytes())
  pix=p.get_pixmap(matrix=fitz.Matrix(1.75,1.75),alpha=False)
  assert h(pix.samples)==rev['raw_pixel_sha256']
  assert h(p.get_text().encode())==rev['extracted_text_sha256']
  words=p.get_text('words');out=[w for w in words if w[0]<0 or w[1]<0 or w[2]>p.rect.width or w[3]>p.rect.height]
  assert not out
  assert '\ufffd' not in p.get_text()
  bounds.append({'layer':lang,'reader_page':i+1,'printed_page':i+65 if lang!='apparatus' else '', 'word_boxes':len(words),'outside_page':len(out),'replacement_character':False,'result':'PASS'})
  if lang in ('fr','en'):
   oldp=old[i];eqtext=oldp.get_text()==p.get_text();eqpix=oldp.get_pixmap(matrix=fitz.Matrix(1.75,1.75),alpha=False).samples==pix.samples
   expectedchange=(i+65) in changed_expected[lang]
   assert (eqtext and eqpix) or expectedchange,(lang,i+65,'unexplained regression')
   reg.append({'layer':lang,'printed_page':i+65,'s03_text_sha256':h(oldp.get_text().encode()),'s04_text_sha256':h(p.get_text().encode()),'text_equal':eqtext,'pixels_equal':eqpix,'expected_source_backed_revision':expectedchange,'result':'SOURCE_BACKED_REVISION' if expectedchange else 'EXACT_UNCHANGED_PAGE'})
 # All font objects must be embedded; only subsets in PDFs, not standalone font files.
 proc=subprocess.run(['pdffonts',str(path)],capture_output=True,text=True,check=True)
 (Q/f'PDFFONTS_{lang.upper()}.txt').write_text(proc.stdout+proc.stderr)
 for line in proc.stdout.splitlines()[2:]:
  parts=line.split();assert parts[-5]=='yes',line
  fonts.append({'layer':lang,'font':parts[0],'embedded':True})
 outdir=Q/'poppler'/lang;outdir.mkdir(parents=True,exist_ok=True)
 cmd=['pdftoppm','-r','126','-png',str(path),str(outdir/'page')]
 p=subprocess.run(cmd,capture_output=True,text=True,check=True)
 (outdir/'render.stdout.txt').write_text(p.stdout);(outdir/'render.stderr.txt').write_text(p.stderr)
 assert not p.stderr.strip(),p.stderr
 images=sorted(outdir.glob('page-*.png'));assert len(images)==len(doc)
 for image in images:
  poppler.append({'layer':lang,'reader_page':int(image.stem.split('-')[-1]),'path':str(image.relative_to(R)),'bytes':image.stat().st_size,'sha256':h(image.read_bytes()),'renderer':'pdftoppm126dpi','result':'RENDERED_WITHOUT_DIAGNOSTIC'})
for file,rows in [('S03_READER_REGRESSION.tsv',reg),('PDF_TEXT_GEOMETRY.tsv',bounds),('EMBEDDED_FONT_CHECK.tsv',fonts),('POPLER_RENDER_BINDINGS.tsv',poppler)]:
 with (Q/file).open('w') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
report={'manual_output_pages':73,'manual_reader_image_bindings_checked':True,'all_final_six_build_passes_clean':True,'unchanged_author_reader_pages_exact_text_and_pixels':sum(not x['expected_source_backed_revision'] for x in reg),'revised_author_reader_pages':sum(x['expected_source_backed_revision'] for x in reg),'unexpected_page_regressions':[],'all_font_objects_embedded':True,'all_text_word_boxes_within_pages':True,'poppler_independent_pages_rendered_without_diagnostic':len(poppler),'limitation':'Regression, geometry, math equality and rendering are supplementary checks, not source-fidelity proof.'}
(Q/'OUTPUT_PREFLIGHT.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
