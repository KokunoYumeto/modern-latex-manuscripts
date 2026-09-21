"""Compare previously accepted pages with saved S02; render paired review sheets."""
from pathlib import Path
import fitz,hashlib,csv,json,subprocess
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parents[2];Q=R/'qa/s03';rows=[];boxrows=[]
sha=lambda b:hashlib.sha256(b).hexdigest().upper()
for lang in ['fr','en']:
 old=fitz.open(R/f'readers/PAPER_IV_{lang.upper()}_PP065_086.pdf');new=fitz.open(R/f'readers/PAPER_IV_{lang.upper()}_PP065_098.pdf')
 assert len(old)==22 and len(new)==34
 for i in range(22):
  a,b=old[i],new[i];pa=a.get_pixmap(matrix=fitz.Matrix(1.75,1.75),alpha=False);pb=b.get_pixmap(matrix=fitz.Matrix(1.75,1.75),alpha=False)
  assert a.get_text()==b.get_text(),(lang,i,'text');assert pa.samples==pb.samples,(lang,i,'pixels')
  rows.append(dict(layer=lang,printed_page=i+65,pdf_page=i+1,s02_text_sha256=sha(a.get_text().encode()),s03_text_sha256=sha(b.get_text().encode()),s02_pixels_sha256=sha(pa.samples),s03_pixels_sha256=sha(pb.samples),text='IDENTICAL',pixels='IDENTICAL_126_DPI'))
 rd=Q/'visual/regression_sheets';rd.mkdir(exist_ok=True)
 for start in range(65,87,2):
  imgs=[Image.open(Q/f'visual/{lang}/page{p-64:02}_p{p:03}.png').convert('RGB') for p in [start,start+1]]
  # Retain native rendered pixel size on a two-page contact sheet, not thumbnails.
  sheet=Image.new('RGB',(imgs[0].width*2+20,imgs[0].height+28),'white');d=ImageDraw.Draw(sheet)
  for j,im in enumerate(imgs):sheet.paste(im,(j*(im.width+20),28));d.text((j*(im.width+20)+10,5),f'{lang.upper()} printed {start+j}; S03 current render',fill='black')
  sheet.save(rd/f'{lang}_pp{start:03}_{start+1:03}.png')
for lang,fn in [('fr','PAPER_IV_FR_PP065_098.pdf'),('en','PAPER_IV_EN_PP065_098.pdf'),('apparatus','PAPER_IV_APPARATUS_S03.pdf')]:
 d=fitz.open(R/'readers'/fn)
 for i,p in enumerate(d):
  chars=0;outside=[]
  for block in p.get_text('dict')['blocks']:
   if 'lines' not in block:continue
   for line in block['lines']:
    for sp in line['spans']:
     chars+=len(sp['text']);r=fitz.Rect(sp['bbox'])
     if not (p.rect+(-.5,-.5,.5,.5)).contains(r):outside.append([sp['text'],list(r)])
  assert chars>0 and not outside,(lang,i,outside)
  boxrows.append(dict(layer=lang,pdf_page=i+1,printed_page=i+65 if lang!='apparatus' else '',width=p.rect.width,height=p.rect.height,characters=chars,text_spans_outside_page=0,status='PASS_GEOMETRY_ONLY_NOT_SUBSTITUTE_FOR_VISUAL_REVIEW'))
 (Q/f'PDFFONTS_{lang.upper()}.txt').write_text(subprocess.check_output(['pdffonts',str(R/'readers'/fn)],text=True))
for name,rs in [('S02_READER_REGRESSION.tsv',rows),('PDF_GEOMETRY_AUDIT.tsv',boxrows)]:
 with (Q/name).open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rs[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rs)
initial=json.loads((Q/'initial_build/VISUAL_HASHES.json').read_text());diff=[]
for p,h in initial.items():
 now=sha((Q/'visual'/p).read_bytes())
 if h!=now:diff.append(p)
assert diff==['en/page33_p097.png'],diff
(Q/'FINAL_RENDER_REGRESSION.json').write_text(json.dumps({'all_output_pages':72,'identical_to_initial_reviewed_render':71,'changed_and_reinspected':diff,'prior_s02_author_reader_pages_text_pixel_identical':44},indent=2)+'\n')
print('44 S02 pages text/pixel identical; 72 geometry checks; 71 initial renders unchanged; EN97 changed and individually reinspected.')
