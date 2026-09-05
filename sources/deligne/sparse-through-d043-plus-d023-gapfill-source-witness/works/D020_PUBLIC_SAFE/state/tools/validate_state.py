#!/usr/bin/env python3
import csv,hashlib,json,pathlib,re,subprocess,sys,zipfile
ROOT=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else '.').resolve();PAGES=36;PROMPTS=6;AUTH='20_AUTHORITY_DELIGNE_D020_WEIL_I_NUMDAM_36PP.pdf';AUTH_SHA='8392B345D4854E6DC55FB42CFC0B616D941935983723627237239A87348F42E5';COMP='21_COMPARATOR_DELIGNE_D020_IAS_NUMBER23_35PP.pdf';COMP_SHA='DE78B2D6DA99954167DF07F84AAE330172F8268A8C004D37F43DCAE55576C7E9';SALV='30_UNTRUSTED_PRIOR_WORK_DELIGNE_D020.zip';SALV_SHA='D9A1EA75B555D4373D17BB1129ACB929B8C840748930B4E0C3812506B4C07F4C'
LAYERS=[('source_language','record_sha256_source','source_status'),('english_standalone','record_sha256_english','english_status'),('apparatus','record_sha256_apparatus','apparatus_status')]
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest().upper()
def rows(p):
 with p.open(encoding='utf-8',newline='') as f:return list(csv.DictReader(f,delimiter='\t'))
def canonical(o):return hashlib.sha256(json.dumps(o,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest().upper()
def pdfpages(p):
 out=subprocess.check_output(['pdfinfo',str(p)],text=True,errors='replace');return int(next(x.split(':',1)[1].strip() for x in out.splitlines() if x.startswith('Pages:')))
def records(layer):
 out={}
 for line in (ROOT/'edition'/f'{layer}.ndjson').read_text(encoding='utf-8').splitlines():
  if not line.strip():continue
  obj=json.loads(line);assert line==json.dumps(obj,ensure_ascii=False,sort_keys=True,separators=(',',':'));assert {'physical_page','printed_page','disposition','status','source_sha256','text','assets'}.issubset(obj);page=int(obj['physical_page']);assert page not in out;out[page]=obj
 return out
source=ROOT/'source'/AUTH;comp=ROOT/'comparators'/COMP;salv=ROOT/'salvage'/SALV;comp2=ROOT/'comparators'/'22_COMPARATOR_DELIGNE_D020_COLLECTED_SPLIT_35PP.pdf';COMP2_SHA='1B51C0D248DBD0AF50D9084EBEE35DAF1143691FF998F559F1192626D6918D5F'
assert source.is_file() and source.stat().st_size==3582172 and sha(source)==AUTH_SHA and pdfpages(source)==PAGES
assert comp.is_file() and sha(comp)==COMP_SHA and pdfpages(comp)==35
assert comp2.is_file() and sha(comp2)==COMP2_SHA and pdfpages(comp2)==35
assert salv.is_file() and sha(salv)==SALV_SHA
ledger=rows(ROOT/'control'/'PRIOR_WORK_LEDGER.tsv')
with zipfile.ZipFile(salv) as z:
 assert z.testzip() is None and len(z.namelist())==272 and set(z.namelist())=={r['archive_path'] for r in ledger}
 for r in ledger:
  data=z.read(r['archive_path']);assert len(data)==int(r['bytes']) and hashlib.sha256(data).hexdigest().upper()==r['sha256'] and r['accepted_state']=='ZERO_ACCEPTED'
mapping=rows(ROOT/'control'/'PAGE_MAP.tsv');assert len(mapping)==PAGES and [int(r['physical_page']) for r in mapping]==list(range(1,PAGES+1)) and [int(r['printed_page']) for r in mapping]==[0]+list(range(273,308)) and mapping[0]['disposition']=='EXCLUDE_NUMDAM_COVER_FROM_SCHOLARLY_BODY_RETAIN_PROVENANCE' and all(r['disposition']=='INCLUDE_ARTICLE' for r in mapping[1:])
plan=rows(ROOT/'control'/'SESSION_PLAN.tsv');assert len(plan)==PROMPTS and [r['prompt_id'] for r in plan]==[f'P{n:02d}' for n in range(1,PROMPTS+1)] and plan[-1]['mode']=='END_TO_END_PAGE_UNIT_FINAL_CLEAN_NONPATCHING_AUDIT'
owned=[]
for r in plan:owned.extend(range(int(r['physical_start']),int(r['physical_end'])+1))
assert owned==list(range(1,PAGES+1)) and all(mapping[n-1]['prompt_id']==f'P{((n-1)//6)+1:02d}' for n in range(1,PAGES+1))
coverage=rows(ROOT/'coverage'/'coverage.tsv');assert len(coverage)==PAGES and [int(r['physical_page']) for r in coverage]==list(range(1,PAGES+1));loaded={layer:records(layer) for layer,_,_ in LAYERS};refs={layer:{} for layer,_,_ in LAYERS}
for row,mapped in zip(coverage,mapping):
 page=int(row['physical_page']);assert row['printed_page']==mapped['printed_page'] and row['prompt_id']==mapped['prompt_id'] and row['disposition']==mapped['disposition'];assert row['source_status'] in ('UNACCEPTED','DRAFT','ACCEPTED','FROZEN') and row['english_status'] in ('UNACCEPTED','DRAFT','ACCEPTED') and row['apparatus_status'] in ('UNACCEPTED','DRAFT','ACCEPTED') and row['final_status'] in ('UNACCEPTED','ACCEPTED')
 if row['english_status']!='UNACCEPTED':assert row['source_status']=='FROZEN'
 if row['apparatus_status']!='UNACCEPTED':assert row['source_status']=='FROZEN' and row['english_status']=='ACCEPTED'
 if row['final_status']=='ACCEPTED':assert row['source_status']=='FROZEN' and row['english_status']=='ACCEPTED' and row['apparatus_status']=='ACCEPTED'
 for layer,hcol,scol in LAYERS:
  recs=loaded[layer];status=row[scol]
  if status in ('ACCEPTED','FROZEN'):
   assert page in recs;rec=recs[page];assert rec['status']==status.lower() and rec['source_sha256']==AUTH_SHA and int(rec['printed_page'])==int(row['printed_page']) and rec['disposition']==row['disposition'] and row[hcol]==canonical(rec)
  elif page in recs:assert status=='DRAFT' and recs[page]['status']=='draft'
  else:assert not row[hcol]
  if page in recs:
   for asset in recs[page].get('assets',[]):refs[layer].setdefault(str(asset['id']),set()).add(page)
assets=rows(ROOT/'edition'/'asset_ledger.tsv');byid={}
for r in assets:
 aid=r['asset_id'];assert re.fullmatch(r'P\d{4}-A\d{2}',aid) and aid not in byid;page=int(r['physical_page']);assert 1<=page<=PAGES and int(r['printed_page'])==(0 if page==1 else page+271)
 for pkey,hkey,prefix,exts in [('raw_crop_path','raw_crop_sha256','assets/raw_crops/',('.png',)),('presentation_path','presentation_sha256','assets/presentation_derivatives/',('.png','.svg'))]:
  rel=pathlib.PurePosixPath(r[pkey]);assert not rel.is_absolute() and '..' not in rel.parts and r[pkey].startswith(prefix) and r[pkey].lower().endswith(exts);p=ROOT/pathlib.Path(*rel.parts);assert p.is_file() and sha(p)==r[hkey]
 assert r['raw_crop_path']!=r['presentation_path'] and r['operations'].strip();byid[aid]=r
for layer in refs:
 for aid,pages in refs[layer].items():assert aid in byid and pages=={int(byid[aid]['physical_page'])}
subprocess.run([sys.executable,str(ROOT/'tools'/'build_readers.py'),str(ROOT),'--check'],check=True)
for reader in (ROOT/'readers').glob('*.html'):
 text=reader.read_text(encoding='utf-8').lower();assert 'http://' not in text and 'https://' not in text and '<script' not in text
print(json.dumps({'result':'PASS','pages':PAGES,'prior_members':len(ledger)},sort_keys=True))
