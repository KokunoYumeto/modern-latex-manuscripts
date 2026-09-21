#!/usr/bin/env python3
"""Independently reopen and verify the complete S02 four-file handoff.
Usage: python verify_handoff_s02.py RELEASE.zip [MANIFEST.tsv CHECKPOINT.json SOURCE_BACKED_DIFF.tsv]
This verifies packaging/state/evidence bindings, not a substitute for the required later cold source audit.
"""
from __future__ import annotations
from pathlib import Path,PurePosixPath
import csv,hashlib,io,json,re,stat,sys,unicodedata,zipfile
import fitz

def h(b:bytes)->str:return hashlib.sha256(b).hexdigest().upper()
def filehash(p:Path)->str:
 d=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):d.update(b)
 return d.hexdigest().upper()
def table(b:bytes):return list(csv.DictReader(io.StringIO(b.decode('utf-8')),delimiter='\t'))
def check_name(n:str)->str:
 assert n and not n.startswith('/') and '\\' not in n and ':' not in n,('unsafe name',n)
 assert all(x not in ('','..','.') for x in n.split('/')),('unsafe path components',n)
 assert PurePosixPath(n).as_posix()==n
 assert unicodedata.normalize('NFC',n)==n
 return n

def verify(zp:Path,mp:Path,cp:Path,dp:Path)->dict:
 cpj=json.loads(cp.read_text());mr=table(mp.read_bytes());assert len({r['path'] for r in mr})==len(mr)
 assert set(mr[0])=={'path','bytes','sha256','role','acceptance','printed_page_range','provenance'}
 assert [r['path'] for r in mr]==sorted(r['path'] for r in mr)
 for key,p in [('cumulative_zip',zp),('manifest',mp),('source_backed_diff',dp)]:
  binding=cpj['release_artifacts'][key];assert binding['bytes']==p.stat().st_size and binding['sha256']==filehash(p),(key,'standalone binding')
 assert cpj['prompt_completed']==2 and cpj['next_cursor']==3 and cpj['prompt_cursor']==3
 assert cpj['first_untouched_page']==87 and not cpj['whole_paper_complete'] and not cpj['prompt_03_executed'] and not cpj['prompt_04_executed']
 for f in ['accepted_french_pages','accepted_english_pages','accepted_apparatus_pages']:assert cpj[f]==list(range(65,87))
 assert cpj['accepted_copy_matter_pages']==[63,64] and cpj['unresolved_source_ambiguities']==[]
 with zipfile.ZipFile(zp) as z:
  assert z.testzip() is None,'CRC mismatch'
  infos=z.infolist();assert all(not i.is_dir() for i in infos)
  names=[check_name(i.filename) for i in infos];assert len(names)==len(set(names))
  assert names==sorted(names)
  assert not any('CUMULATIVE_FULL_STATE.zip' in n for n in names),'nested cumulative archive'
  assert not any(Path(n).suffix.lower() in {'.ttf','.otf','.ttc','.woff','.woff2'} for n in names),'standalone font file'
  assert not any(stat.S_ISLNK(i.external_attr>>16) for i in infos)
  assert set(names)=={r['path'] for r in mr}==set(cpj['archive_members'])
  assert len(names)==cpj['archive_member_count']
  mm={r['path']:r for r in mr};total=0
  for i in infos:
   b=z.read(i);d=h(b);r=mm[i.filename];s=cpj['archive_members'][i.filename]
   assert re.fullmatch(r'[0-9A-F]{64}',r['sha256'])
   assert len(b)==i.file_size==int(r['bytes'])==s['bytes'] and d==r['sha256']==s['sha256'],i.filename
   assert all(r[k] for k in ['role','acceptance','printed_page_range','provenance']);total+=len(b)
  assert z.read('SOURCE_BACKED_DIFF.tsv')==dp.read_bytes()
  cur=json.loads(z.read('state/CURSOR.json'))
  for k in ['session','prompt_completed','prompt_cursor','next_cursor','accepted_french_pages','accepted_english_pages','accepted_apparatus_pages','accepted_copy_matter_pages','first_untouched_page','current_readers','whole_paper_complete']:
   assert cur[k]==cpj[k],('internal cursor mismatch',k)
  # Page records and actual independent main inputs.
  for l in ['fr','en']:
   main=z.read(f'editions/{l}/main.tex').decode()
   assert re.findall(r'\\input\{pages/p(\d+)\.tex\}',main)==[f'{p:03d}' for p in range(65,87)]
   assert not any(n.startswith(f'editions/{l}/pages/') and not re.fullmatch(rf'editions/{l}/pages/p0(?:6[5-9]|[78][0-9])\.tex',n) for n in names)
   assert {n for n in names if n.startswith(f'editions/{l}/pages/')}=={f'editions/{l}/pages/p{p:03d}.tex' for p in range(65,87)}
  for p in range(65,87):
   record=json.loads(z.read(f'state/pages/p{p:03d}.json'))
   assert record['printed_page']==p and record['authority_pdf_page']==p+17 and record['scope_leaf']==p-62
   for k in ['french','english']:
    x=record[k];assert h(z.read(x['path']))==x['sha256']
   assert h(z.read(record['apparatus_path']))==record['apparatus_sha256']
   assert record['source_ambiguities']==[] and record['accepted_layers']==['fr','en','apparatus']
   assert record['visual_output_audit']=='PASS'
  app=table(z.read('apparatus/CATALOGUE.tsv'));assert [int(x['printed_page']) for x in app]==list(range(65,87))
  topology=table(z.read('ledgers/TOPOLOGY.tsv'));assert [int(x['printed_page']) for x in topology]==list(range(63,99))
  for row in topology:
   p=int(row['printed_page']);assert int(row['authority_pdf_page'])==p+17 and int(row['scope_leaf'])==p-62
   assert int(row['occurrences_in_each_current_reader'])==(1 if 65<=p<=86 else 0)
  # The exact immutable input identities registered in the original packet.
  inp=[n for n in names if n.startswith('input/')];assert len(inp)==21
  for r in table(z.read('input/91_SHA256SUMS.tsv')):
   b=z.read('input/'+r['file']);assert len(b)==int(r['bytes']) and h(b)==r['sha256']
  # All240 S01 members preserved somewhere, with a precise location map.
  prior=json.loads(z.read('prior_evidence/S01/CHECKPOINT.json'));assert prior['next_cursor']==2
  pres=table(z.read('qa/s02/S01_MEMBER_PRESERVATION.tsv'));assert len(pres)==240
  assert {r['s01_member'] for r in pres}==set(prior['archive_members'])
  for r in pres:
   a=prior['archive_members'][r['s01_member']];b=z.read(r['preserved_path'])
   assert len(b)==a['bytes']==int(r['bytes']) and h(b)==a['sha256']==r['sha256']
  for p in range(65,75):
   for path in [f'editions/fr/pages/p{p:03d}.tex',f'editions/en/pages/p{p:03d}.tex',f'apparatus/pages/p{p:03d}.md',f'state/pages/p{p:03d}.json']:
    assert h(z.read(path))==prior['archive_members'][path]['sha256']
  # Actual current readers, all final logs, visual evidence bindings.
  reader_counts={}
  for l,ident in cpj['current_readers'].items():
   b=z.read(ident['path']);assert h(b)==ident['sha256']
   doc=fitz.open(stream=b,filetype='pdf');expected=3 if l=='apparatus' else 22
   assert len(doc)==ident['pages']==expected;reader_counts[l]=len(doc)
   for n in [1,2]:
    text=z.read(f'qa/s02/build/{l}/pass{n}.log').decode()
    assert 'Output written on' in text and not re.findall(r'^.*(?:Overfull|Underfull|Missing character|Warning|^!).*$',text,re.M)
  vis=table(z.read('qa/s02/VISUAL_AUDIT.tsv'));assert len(vis)==47
  for v in vis:assert v['status']=='PASS' and h(z.read(v['render']))==v['render_sha256'] and h(z.read(v['reader']))==v['reader_sha256']
  counts=json.loads(z.read('qa/s02/CONTENT_AUDIT_COUNTS.json'));assert counts['new_author_pages']==list(range(75,87)) and counts['aligned_units']==85 and counts['paired_math_segments']==499
  assert len(table(z.read('qa/s02/UNIT_ALIGNMENT.tsv')))==85 and len(table(z.read('qa/s02/FORMULA_AUDIT.tsv')))==499
  assert len(table(z.read('qa/s02/CUMULATIVE_UNIT_ALIGNMENT.tsv')))==139 and len(table(z.read('qa/s02/CUMULATIVE_FORMULA_AUDIT.tsv')))==914
  diff=table(z.read('SOURCE_BACKED_DIFF.tsv'));newdiff=table(z.read('qa/s02/SOURCE_BACKED_DIFF_S02.tsv'));assert len(diff)==70 and len(newdiff)==26
  assert z.read('SOURCE_BACKED_DIFF.tsv').startswith(z.read('prior_evidence/S01/SOURCE_BACKED_DIFF.tsv'))
  assert all(r['before'] and r['after'] and r['evidence'] and r['disposition'] for r in diff)
  assert all(r['status']=='PASS' for r in table(z.read('qa/s02/PROMPT_02_GATES.tsv')))
  assert len(table(z.read('qa/s02/S01_READER_REGRESSION.tsv')))==20
 return {'status':'PASS','zip_crc':'PASS','path_safety':'PASS','unique_normalized_names':'PASS','sorted_names':'PASS','manifest_exactness':'PASS','all_member_hashes':'PASS','checkpoint_bindings':'PASS','standalone_diff_matches_internal':'PASS','member_count':len(names),'uncompressed_member_bytes':total,'s01_members_preserved':240,'immutable_input_members':21,'accepted_author_pages':list(range(65,87)),'current_pdf_pages':reader_counts,'current_visual_evidence_rows':47,'current_prompt':2,'next_cursor':3,'previous_cumulative_zip_nested':False,'independent_cold_source_audit':'NOT_PERFORMED_BY_THIS_VERIFIER; REMAINS_REQUIRED'}
if __name__=='__main__':
 if len(sys.argv) not in (2,5):raise SystemExit(__doc__)
 zp=Path(sys.argv[1]);mp,cp,dp=map(Path,sys.argv[2:]) if len(sys.argv)==5 else (zp.parent/'MANIFEST.tsv',zp.parent/'CHECKPOINT.json',zp.parent/'SOURCE_BACKED_DIFF.tsv')
 print(json.dumps(verify(zp,mp,cp,dp),indent=2,ensure_ascii=False))
