from pathlib import Path
import csv,hashlib,json,zipfile,unicodedata,fitz
ROOT=Path(__file__).resolve().parents[1]; P=ROOT/'input'; QA=ROOT/'qa'
def sha(b):return hashlib.sha256(b).hexdigest().upper()
def tsv(p):return list(csv.DictReader(p.open(encoding='utf8'),delimiter='\t'))
def write(name,cols,rows):
 with (QA/name).open('w',encoding='utf8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=cols,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
checks=[]
for table in ['91_SHA256SUMS.tsv','02_INPUT_PAYLOAD_INVENTORY.tsv']:
 for row in tsv(P/table):
  b=(P/row['file']).read_bytes();h=sha(b)
  assert len(b)==int(row['bytes']) and h==row['sha256']
  checks.append(dict(check=table,file=row['file'],bytes=len(b),sha256=h,status='PASS'))
write('INPUT_HASH_VALIDATION.tsv',list(checks[0]),checks)
rows=tsv(P/'05_PAGE_MAP.tsv')
assert len(rows)==36
assert [int(r['printed_page']) for r in rows]==list(range(63,99))
assert [int(r['authority_pdf_page_1based']) for r in rows]==list(range(80,116))
assert [int(r['scope_pdf_page_1based']) for r in rows]==list(range(1,37))
assert all(r['role']=='AUTHOR_TEXT_FRENCH' for r in rows[2:])
idx=tsv(P/'14_UNVERIFIED_INHERITED_MEMBER_INDEX.tsv');zchecks=[]
for label,prefix in [('R27','12_'),('R28','13_')]:
 fn=next(P.glob(prefix+'*.zip'))
 with zipfile.ZipFile(fn) as z:
  assert z.testzip() is None
  names=[i.filename for i in z.infolist() if not i.is_dir()]
  assert len(names)==(46 if label=='R27' else 51)
  norm=[unicodedata.normalize('NFC',n) for n in names]
  assert len(set(norm))==len(norm)
  for n in names:
   assert not Path(n).is_absolute() and '..' not in Path(n).parts and '\\' not in n
  records=[r for r in idx if ('_'+label+'_') in r['bundle']]
  # Index may use short relative paths, keep exact recorded member.
  print(label,len(records),records[0])
  assert len(records)==len(names)
  for r in records:
   n=r['member'];b=z.read(n)
   assert len(b)==int(r['bytes']) and sha(b)==r['sha256']
   zchecks.append(dict(bundle=label,member=n,bytes=len(b),sha256=sha(b),crc='PASS',index='PASS'))
write('INHERITED_MEMBER_VALIDATION.tsv',list(zchecks[0]),zchecks)
scope=fitz.open(next(P.glob('10_*.pdf')));full=fitz.open(next(P.glob('11_*.pdf')))
assert len(scope)==36 and len(full)==657
ras=[]
for i in range(36):
 a=scope[i].get_pixmap(matrix=fitz.Matrix(1,1),alpha=False)
 b=full[79+i].get_pixmap(matrix=fitz.Matrix(1,1),alpha=False)
 assert a.width==b.width and a.height==b.height and a.samples==b.samples
 ras.append(dict(printed_page=63+i,authority_pdf_page=80+i,scope_leaf=1+i,dpi=72,width=a.width,height=a.height,raster_sha256=sha(a.samples),equivalence='PASS'))
 if i<12:
  scope[i].get_pixmap(matrix=fitz.Matrix(3,3),alpha=False).save(QA/'source'/f'p{63+i:03d}_authority.png')
write('PAGEWISE_RASTER_EQUIVALENCE.tsv',list(ras[0]),ras)
# Boundary inspection only: no Paper V text is transcribed into the editions.
full[115].get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False).save(QA/'source'/'boundary_pdf116_inspection_only.png')
receipt={'schema':'dirichlet-s01-input-validation-v1','input_zip_file':'DIRICHLET_PAPER_IV_INPUT_PACKAGE(1).zip','input_zip_bytes':93695662,'input_zip_sha256':'8450ABEBC78FECD44FC253406BC52DF4726129C3167DEB27B38675C77CE8E85B','input_zip_files':21,'input_zip_crc':'PASS','hash_entries_checked':len(checks),'inherited_files_checked':len(zchecks),'scope_leaves':36,'full_pdf_pages':657,'page_map':'PASS','raster_equivalence':'36/36 at 72 dpi','initial_accepted_pages':[],'prior_checkpoint':'Input access only; zero acceptance; preserved unpacked in prior_evidence.'}
(QA/'INPUT_VALIDATION.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(receipt,indent=2))
