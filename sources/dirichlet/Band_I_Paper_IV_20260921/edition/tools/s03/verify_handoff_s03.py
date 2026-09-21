#!/usr/bin/env python3
"""Reopen and verify the complete Prompt03 four-file return.
This is an archive/state/build/evidence verifier, NOT a cold source collation.
Usage: python tools/s03/verify_handoff_s03.py --zip FILE --checkpoint FILE --manifest FILE --diff FILE
"""
from __future__ import annotations
from pathlib import Path,PurePosixPath
import argparse,csv,hashlib,io,json,re,stat,unicodedata,zipfile
import fitz
from PIL import Image

def digest(b:bytes)->str:return hashlib.sha256(b).hexdigest().upper()
def filehash(p:Path)->str:
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest().upper()
def table(b:bytes):return list(csv.DictReader(io.StringIO(b.decode('utf-8')),delimiter='\t'))
def safe(n:str)->str:
 assert n and not n.startswith('/') and '\\' not in n and ':' not in n,('unsafe name',n)
 assert all(p not in ('','.','..') for p in n.split('/')) and not any(ord(c)<32 for c in n)
 assert PurePosixPath(n).as_posix()==n and unicodedata.normalize('NFC',n)==n
 return n

def verify(zp:Path,cp:Path,mp:Path,dp:Path)->dict:
 c=json.loads(cp.read_text());mr=table(mp.read_bytes());assert mr
 assert set(mr[0])=={'path','bytes','sha256','role','acceptance','printed_page_range','provenance'}
 assert [x['path'] for x in mr]==sorted(set(x['path'] for x in mr))
 for key,p in [('cumulative_zip',zp),('manifest',mp),('source_backed_diff',dp)]:
  x=c['release_artifacts'][key];assert x['file']==p.name and x['bytes']==p.stat().st_size and x['sha256']==filehash(p),(key,'binding')
 assert c['prompt_completed']==3 and c['session']==3 and c['next_cursor']==c['prompt_cursor']==4
 assert c['first_untouched_page'] is None and not c['whole_paper_complete'] and c['prompt_03_executed'] and not c['prompt_04_executed']
 for k in ['accepted_french_pages','accepted_english_pages','accepted_apparatus_pages']:assert c[k]==list(range(65,99))
 assert c['accepted_copy_matter_pages']==[63,64] and c['unresolved_source_ambiguities']==[]
 with zipfile.ZipFile(zp) as z:
  assert z.testzip() is None
  infos=z.infolist();names=[safe(i.filename) for i in infos]
  assert names==sorted(set(names)) and len({n.casefold() for n in names})==len(names)
  assert all(not i.is_dir() and not stat.S_ISLNK(i.external_attr>>16) for i in infos)
  assert not any('CUMULATIVE_FULL_STATE.zip' in n for n in names)
  assert not any(Path(n).suffix.lower() in {'.ttf','.otf','.ttc','.woff','.woff2','.pyc'} for n in names)
  assert set(names)=={x['path'] for x in mr}==set(c['archive_members'])
  assert len(names)==c['archive_member_count'];m={x['path']:x for x in mr};total=0
  for i in infos:
   b=z.read(i);r=m[i.filename];a=c['archive_members'][i.filename]
   assert len(b)==i.file_size==int(r['bytes'])==a['bytes']
   assert re.fullmatch('[0-9A-F]{64}',r['sha256']) and digest(b)==r['sha256']==a['sha256']
   assert all(r[k] for k in ['role','acceptance','printed_page_range','provenance']);total+=len(b)
  assert z.read('SOURCE_BACKED_DIFF.tsv')==dp.read_bytes()
  cur=json.loads(z.read('state/CURSOR.json'))
  for k in ['session','prompt_completed','next_cursor','prompt_cursor','accepted_french_pages','accepted_english_pages','accepted_apparatus_pages','accepted_copy_matter_pages','current_readers','first_untouched_page','whole_paper_complete','prompt_04_executed']:
   assert cur[k]==c[k],('internal cursor binding',k)
  # Saved predecessor bindings and exact old-byte locations.
  prev=json.loads(z.read('history/S02/CHECKPOINT.json'));assert prev['next_cursor']==3
  for key,n in [('manifest','MANIFEST.tsv'),('source_backed_diff','SOURCE_BACKED_DIFF.tsv')]:
   b=z.read('history/S02/'+n);x=prev['release_artifacts'][key];assert len(b)==x['bytes'] and digest(b)==x['sha256']
  pres=table(z.read('qa/s03/S02_MEMBER_PRESERVATION.tsv'));assert len(pres)==517
  assert {x['s02_path'] for x in pres}==set(prev['archive_members'])
  for x in pres:
   b=z.read(x['s03_preserved_path']);old=prev['archive_members'][x['s02_path']]
   assert len(b)==int(x['bytes'])==old['bytes'] and digest(b)==x['sha256']==old['sha256']
  prior1=json.loads(z.read('prior_evidence/S01/CHECKPOINT.json'))
  pres1=table(z.read('qa/s02/S01_MEMBER_PRESERVATION.tsv'));assert len(pres1)==240
  for x in pres1:
   b=z.read(x['preserved_path']);old=prior1['archive_members'][x['s01_member']]
   assert len(b)==int(x['bytes'])==old['bytes'] and digest(b)==x['sha256']==old['sha256']
  # Every old accepted editable author/apparatus/page record remains at the original path.
  for p in range(65,87):
   for n in [f'editions/fr/pages/p{p:03}.tex',f'editions/en/pages/p{p:03}.tex',f'apparatus/pages/p{p:03}.md',f'state/pages/p{p:03}.json']:
    assert digest(z.read(n))==prev['archive_members'][n]['sha256']
  assert len([n for n in names if n.startswith('input/')])==21
  for x in table(z.read('input/91_SHA256SUMS.tsv')):
   b=z.read('input/'+x['file']);assert len(b)==int(x['bytes']) and digest(b)==x['sha256']
  fullid='input/11_AUTHORITY_FULL_DIRICHLET_GESAMMELTE_WERKE_BAND_I_1889.pdf'
  assert len(z.read(fullid))==36067858 and digest(z.read(fullid))=='961E55A2D32DDC88191CDD8A99F877A06BB3E721D7705F5A96C6F80AD67F9F6C'
  for l in ['fr','en']:
   main=z.read(f'editions/{l}/main.tex').decode();assert re.findall(r'\\input\{pages/p(\d+)\.tex\}',main)==[f'{p:03}' for p in range(65,99)]
   assert {n for n in names if n.startswith(f'editions/{l}/pages/')}=={f'editions/{l}/pages/p{p:03}.tex' for p in range(65,99)}
  for p in range(65,99):
   r=json.loads(z.read(f'state/pages/p{p:03}.json'));assert (r['printed_page'],r['authority_pdf_page'],r['scope_leaf'])==(p,p+17,p-62)
   for k in ['french','english']:assert digest(z.read(r[k]['path']))==r[k]['sha256']
   assert digest(z.read(r['apparatus_path']))==r['apparatus_sha256'] and digest(z.read(r['source_image']))==r['source_image_sha256']
   assert r['source_ambiguities']==[] and set(r['accepted_layers'])=={'fr','en','apparatus'} and r['visual_output_audit'].startswith('PASS')
  app=table(z.read('apparatus/CATALOGUE.tsv'));assert [int(x['printed_page']) for x in app]==list(range(65,99))
  top=table(z.read('ledgers/TOPOLOGY.tsv'));assert [int(x['printed_page']) for x in top]==list(range(63,99))
  for x in top:
   p=int(x['printed_page']);assert (int(x['authority_pdf_page']),int(x['scope_leaf']))==(p+17,p-62)
   assert int(x['occurrences_in_each_current_reader'])==(0 if p<65 else 1)
  docs={};reader_counts={}
  for l,x in c['current_readers'].items():
   b=z.read(x['path']);assert len(b)==x['bytes'] and digest(b)==x['sha256'];d=fitz.open(stream=b,filetype='pdf')
   assert len(d)==x['pages']==(4 if l=='apparatus' else 34);docs[l]=d;reader_counts[l]=len(d)
   for n in [1,2]:
    text=z.read(f'qa/s03/build/{l}/pass{n}.log').decode();assert 'Output written on' in text
    assert not re.findall(r'^.*(?:Overfull|Underfull|Missing character|Warning|^!).*$',text,re.M)
  vis=table(z.read('qa/s03/VISUAL_AUDIT.tsv'));assert len(vis)==72
  for x in vis:
   assert x['status']=='PASS' and digest(z.read(x['image']))==x['image_sha256']
   pi=docs[x['layer']][int(x['pdf_page'])-1].get_pixmap(matrix=fitz.Matrix(1.75,1.75),alpha=False)
   im=Image.open(io.BytesIO(z.read(x['image']))).convert('RGB')
   assert (pi.width,pi.height)==im.size and pi.samples==im.tobytes(),('render binding',x['image'])
  for l in ['fr','en']:
   old=fitz.open(stream=z.read(f'readers/PAPER_IV_{l.upper()}_PP065_086.pdf'),filetype='pdf')
   for i in range(22):
    assert old[i].get_text()==docs[l][i].get_text()
    assert old[i].get_pixmap(matrix=fitz.Matrix(1.75,1.75),alpha=False).samples==docs[l][i].get_pixmap(matrix=fitz.Matrix(1.75,1.75),alpha=False).samples
  assert len(table(z.read('qa/s03/UNIT_ALIGNMENT.tsv')))==61 and len(table(z.read('qa/s03/FORMULA_AUDIT.tsv')))==547
  assert len(table(z.read('qa/s03/CUMULATIVE_UNIT_ALIGNMENT.tsv')))==200 and len(table(z.read('qa/s03/CUMULATIVE_FORMULA_AUDIT.tsv')))==1461
  diff=table(z.read('SOURCE_BACKED_DIFF.tsv'));assert len(diff)==72
  assert z.read('SOURCE_BACKED_DIFF.tsv').startswith(z.read('history/S02/SOURCE_BACKED_DIFF.tsv'))
  assert len(table(z.read('qa/s03/SOURCE_BACKED_DIFF_S03.tsv')))==2
  assert all(x['before'] and x['after'] and x['evidence'] and x['disposition'] for x in diff)
  assert all(x['status']=='PASS' for x in table(z.read('qa/s03/PROMPT_03_GATES.tsv')))
  bound=json.loads(z.read('qa/s03/BOUNDARY_RECEIPT.json'));assert bound['visible_final_folio']==98 and bound['scope_final_leaf_full_pdf_page']==115 and not bound['author_content_ingested_from_paperV']
 return dict(status='PASS',zip_crc='PASS',path_safety='PASS',unique_normalized_names='PASS',manifest_exactness='PASS',all_member_hashes='PASS',checkpoint_bindings='PASS',standalone_diff_matches_internal='PASS',member_count=len(names),uncompressed_member_bytes=total,s02_members_preserved=517,s01_members_preserved=240,immutable_input_members=21,accepted_author_pages=list(range(65,99)),current_pdf_pages=reader_counts,current_render_bindings_verified=72,s02_pages_text_pixel_identical=44,current_prompt=3,next_cursor=4,previous_cumulative_zip_nested=False,cold_source_audit='NOT_EXECUTED; this verifier checks archive/state/build/evidence, not independent source collation')

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__)
 for k in ['zip','checkpoint','manifest','diff']:p.add_argument('--'+k,type=Path,required=True)
 a=p.parse_args();print(json.dumps(verify(a.zip,a.checkpoint,a.manifest,a.diff),ensure_ascii=False,indent=2))
