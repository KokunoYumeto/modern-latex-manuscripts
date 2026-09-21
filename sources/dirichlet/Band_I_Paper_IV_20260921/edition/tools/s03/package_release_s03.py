#!/usr/bin/env python3
"""Freeze, package twice, and reopen the self-contained cumulative Prompt03 release.
Usage: python tools/s03/package_release_s03.py [unpacked_root] [output_directory]
Outputs are outside the cumulative tree; current external checkpoint/manifest avoid circular hashes.
"""
from __future__ import annotations
from pathlib import Path
import csv,hashlib,importlib.util,io,json,re,shutil,stat,sys,zipfile
sys.dont_write_bytecode=True
ZIPNAME='DIRICHLET_P04_S03_CUMULATIVE_FULL_STATE.zip'
FIELDS=['path','bytes','sha256','role','acceptance','printed_page_range','provenance']
STAMP=(2026,9,21,0,0,0)
def dh(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest().upper()
def ident(p):return dict(file=p.name,bytes=p.stat().st_size,sha256=dh(p))
def wj(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def rd(p):return list(csv.DictReader(p.open(),delimiter='\t'))
def cls(n,old,cur):
 page=re.search(r'(?:^|/)p(\d{3})(?:[_.]|$)',n);pr=page[1] if page else '65-98 author;63-64 copy matter'
 if n.startswith('input/'):return ('IMMUTABLE_ORIGINAL_INPUT','UNCHANGED_FIXED_AUTHORITY_OR_CONTROL',old[n]['printed_page_range'],'Exact S02 member bytes and original packet hashes revalidated; controlling PDFs and instructions unchanged')
 if n.startswith('inherited/') or n.startswith('copy_matter/'):
  x=old[n];return tuple(x[k] for k in ['role','acceptance','printed_page_range','provenance'])
 if n.startswith('history/S02/'):
  orig=n.removeprefix('history/S02/superseded/');x=old.get(orig)
  return ('PRESERVED_S02_SIDECAR_OR_SUPERSEDED_BYTES','HISTORICAL_ACCEPTED_S02_NOT_CURRENT_STATE',x['printed_page_range'] if x else '63-86 S02 acceptance','Original predecessor bytes preserved, including external sidecars; exact map in qa/s03/S02_MEMBER_PRESERVATION.tsv')
 if n.startswith('prior_evidence/'):
  x=old[n];return tuple(x[k] for k in ['role','acceptance','printed_page_range','provenance'])
 if n.startswith('editions/'):
  layer='EDITABLE_FRENCH_DIPLOMATIC_SOURCE' if '/fr/' in n else 'EDITABLE_FAITHFUL_ENGLISH_SOURCE'
  if page:
   a='ACCEPTED_S01_S02_BYTES_UNCHANGED' if int(page[1])<87 else 'ACCEPTED_DIRECT_AUTHORITY_S03'
   return (layer,a,pr,'Page-bounded author text; earlier pages unchanged;87-98 direct authority comparison; independent monolingual source')
  return (layer,'CURRENT_CUMULATIVE_EDITABLE_MAIN','65-98','Exactly34 page-file inclusions; current independent reader main; no copy matter or PaperV author text')
 if n.startswith('apparatus/'):
  return ('SEPARATE_EDITABLE_APPARATUS','SOURCE_REVIEWED_NO_CONJECTURAL_BODY_REPAIR',pr,'Current apparatus independent of author editions; earlier page records retain original session context; cumulative main and catalogue cover34 pages')
 if n=='state/CURSOR.json':return ('CURRENT_CUMULATIVE_CURSOR','PROMPT03_COMPLETE_CURSOR4_COLD_AUDIT_PENDING','65-98 author;63-64 copy','Exact accepted sets; no untouched author page; Prompt04 not executed; current readers and evidence hashes')
 if n.startswith('state/pages/'):
  return ('PAGEWISE_ACCEPTANCE_AND_EVIDENCE','ACCEPTED_S01_S02_UNCHANGED' if int(page[1])<87 else 'ACCEPTED_S03',pr,'Page mapping, source and edition hashes, full alignment units, apparatus and visual status; historical reader bindings remain evidence')
 if n.startswith('ledgers/'):return ('CURRENT_CUMULATIVE_LEDGER','CURRENT_SOURCE_BACKED_STATE','63-98','Exact36-leaf topology,34 author pages,2 copy leaves, source furniture and session status; cold audit not executed')
 if n.startswith('readers/'):
  if n in {x['path'] for x in cur['current_readers'].values()}:return ('CURRENT_CUMULATIVE_READER','BUILT_TWICE_AND_ALL_PAGES_REVIEWED','65-98','Prompt03 reader;34 French,34 English or4 apparatus pages; six final passes clean')
  x=old[n];return ('PRESERVED_EARLIER_ACCEPTED_READER','HISTORICAL_NOT_CURRENT_EXTENT',x['printed_page_range'],'Unchanged S01/S02 PDF retained as evidence and for regression; not a substitute for current cumulative reader')
 if n.startswith('qa/s03/initial_build/'):
  return ('S03_INITIAL_DRAFT_AND_BUILD_EVIDENCE','SUPERSEDED_NOT_CURRENT_BUILD',pr,'Actual initial draft/build evidence preserved before English97 correction and final two clean passes; final current evidence elsewhere')
 if n.startswith('qa/s03/'):
  if 'boundary_pdf116' in n:return ('OUT_OF_SCOPE_BOUNDARY_INSPECTION_ONLY','NOT_INGESTED_AS_AUTHOR_CONTENT','PaperIV98 / next-paper boundary','Full PDF116 observed only for exclusion; no PaperV content in author readers')
  if '/source/' in n:return ('CONTROLLING_SOURCE_RASTER','AUTHORITY_DERIVED_REVIEW_EVIDENCE',pr,'Exact-scope216dpi source render; fixed full/source projection checked; raw originals unchanged')
  if '/visual/' in n:return ('CURRENT_READER_VISUAL_EVIDENCE','RENDERED_AND_MANUALLY_REVIEWED',pr,'126dpi current render or native-size pair sheet; every current output page reviewed; full hash/render bindings in visual ledger')
  if '/build/' in n:return ('CURRENT_S03_BUILD_EVIDENCE','SIX_FINAL_PASSES_CLEAN','65-98','XeLaTeX pass logs and build assets; separate French, English, apparatus outputs')
  return ('S03_SOURCE_QA_OR_PRESERVATION_EVIDENCE','RECORDED_AND_CHECKED','63-98 topology;87-98 new source collation','Manual collation/visual observations distinguished from mechanical checks; no independent cold-audit claim')
 if n.startswith('qa/'):
  x=old[n];return ('PRESERVED_PRIOR_QA_EVIDENCE','HISTORICAL_UNCHANGED_'+x['acceptance'],x['printed_page_range'],'Unchanged S01/S02 evidence. Current S03 checks under qa/s03. '+x['provenance'])
 if n.startswith('tools/s03/'):
  return ('S03_EDITABLE_REPRODUCIBILITY_TOOL','IMPLEMENTATION_NOT_SOURCE_AUTHORITY','65-98','Intake, generation, build, audit-record, preservation or release helper; code does not perform independent source collation')
 if n.startswith('tools/'):
  x=old[n];return ('PRESERVED_PRIOR_REPRODUCIBILITY_TOOL','HISTORICAL_NOT_CURRENT_ORCHESTRATOR',x['printed_page_range'],'Earlier scripts retained unchanged; do not run earlier source generators to reset current extent')
 if n=='README.md':return ('CURRENT_HANDOFF_DOCUMENTATION','CURRENT_INFORMATION','63-98','Exact current extent, authority, evidence, preservation, rebuild and handoff contract; Prompt04 remains required')
 if n=='SOURCE_BACKED_DIFF.tsv':return ('CUMULATIVE_SOURCE_BACKED_DIFF','AUTHORITY_BACKED_CORRECTIONS','63-98','70 S01/S02 rows preserved verbatim plus2 source-backed S03 English drafting corrections on97; no fabricated missing-page correction rows')
 raise AssertionError(('unclassified',n))
def archive(root,out,rows):
 with zipfile.ZipFile(out,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6,allowZip64=True) as z:
  for r in rows:
   info=zipfile.ZipInfo(r['path'],STAMP);info.create_system=3;info.external_attr=(stat.S_IFREG|0o644)<<16;info.compress_type=zipfile.ZIP_DEFLATED;info._compresslevel=6
   with (root/r['path']).open('rb') as f,z.open(info,'w',force_zip64=True) as g:shutil.copyfileobj(f,g,1048576)
def main(root,out):
 root=root.resolve();out=out.resolve();out.mkdir(exist_ok=True,parents=True);assert root!=out and root not in out.parents
 spec=importlib.util.spec_from_file_location('verify_s03',root/'tools/s03/verify_handoff_s03.py');ver=importlib.util.module_from_spec(spec);spec.loader.exec_module(ver)
 old={x['path']:x for x in rd(root/'history/S02/MANIFEST.tsv')};cur=json.loads((root/'state/CURSOR.json').read_text())
 assert cur['next_cursor']==4 and cur['prompt_completed']==3 and not cur['prompt_04_executed'] and not cur['whole_paper_complete']
 prev=out/'DIRICHLET_P04_S02_CUMULATIVE_FULL_STATE.zip'
 if prev.exists():assert prev.stat().st_size==180461785 and dh(prev)=='7B0D13BED693B98E8D1C665DDCFA54939CBACFCFFF5FF328F137825E349665C4'
 for x in rd(root/'qa/s03/S02_MEMBER_PRESERVATION.tsv'):
  p=root/x['s03_preserved_path'];assert p.stat().st_size==int(x['bytes']) and dh(p)==x['sha256']
 pre=dict(schema='dirichlet-s03-release-preflight-v1',session=3,cursor=4,author_pages=list(range(65,99)),copy_pages=[63,64],current_output_pages=72,s02_preserved_members=517,immutable_originals_embedded=21,transport='SELF_CONTAINED_COMPLETE_MUTABLE_AND_IMMUTABLE_STATE; no external assembly references',prior_cumulative_zip_nested=False,source_batch_complete=True,cold_audit='NOT_EXECUTED_PROMPT04_REQUIRED',archive_verification='Recorded in external CHECKPOINT.json after archive reopening, avoiding circular member hashes')
 wj(root/'qa/s03/RELEASE_PREFLIGHT.json',pre)
 files=sorted((p for p in root.rglob('*') if p.is_file()),key=lambda p:p.relative_to(root).as_posix());rows=[]
 for p in files:
  n=ver.safe(p.relative_to(root).as_posix());assert not p.is_symlink() and '__pycache__' not in n and 'CUMULATIVE_FULL_STATE.zip' not in n
  assert p.suffix.lower() not in {'.pyc','.ttf','.otf','.ttc','.woff','.woff2'}
  role,acc,pr,prov=cls(n,old,cur);rows.append(dict(path=n,bytes=p.stat().st_size,sha256=dh(p),role=role,acceptance=acc,printed_page_range=pr,provenance=prov))
 mp,cp,dp,zp=out/'MANIFEST.tsv',out/'CHECKPOINT.json',out/'SOURCE_BACKED_DIFF.tsv',out/ZIPNAME
 with mp.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=FIELDS,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
 shutil.copyfile(root/'SOURCE_BACKED_DIFF.tsv',dp);archive(root,zp,rows)
 other=out/'.S03_DETERMINISM_CHECK.tmp.zip';archive(root,other,rows);assert ident(zp)['bytes']==other.stat().st_size and dh(zp)==dh(other);other.unlink()
 cpj=dict(cur);counts=json.loads((root/'qa/s03/CONTENT_AUDIT_COUNTS.json').read_text())
 cpj.update(schema='dirichlet-paper-iv-checkpoint-v2',schema_version=2,prompt_file='input/22_PROMPT_03_PP087_098.md',completion_claim_scope='Prompt03 complete only;34 French/English/apparatus author pages65-98 accepted for sequential intake. Independent final cold audit not executed; not final publication readiness.',input_package=json.loads((root/'history/S02/CHECKPOINT.json').read_text())['input_package'],immutable_input_revalidation='qa/s03/IMMUTABLE_INPUT_PRESERVATION.tsv; all21 original files embedded unchanged',copy_topology_state='PASS_63_TITLE_64_BLANK_EXCLUDED_FROM_AUTHOR_READERS',build_and_visual=json.loads((root/'qa/s03/BUILD_VISUAL_RECEIPT.json').read_text()),source_comparison=dict(new_author_pages=list(range(87,99)),new_authority_full_pdf_pages=list(range(104,116)),new_exact_scope_leaves=list(range(25,37)),direct_source_pages=list(range(87,99)),new_aligned_units=61,new_paired_math_segments=547,new_french_editable_lines_audited=526,new_english_editable_lines_audited=526,cumulative_aligned_units=200,cumulative_paired_math_segments=1461,cumulative_diff_rows=72,new_diff_rows=2,prior_source_acceptance='S01/S02 accepted page bytes and evidence preserved; no independent full cold source collation this session',rechecked_seams=['74/75','80/81','86/87'],no_new_author_footnotes=True,source_print_issues_retained=[66,70,77,82,85],genuinely_illegible_ambiguities=[],boundary='Full PDF115 is printed98;116 next paper inspected only; no PaperV author content ingested',cold_source_audit='NOT_EXECUTED_PROMPT04_REQUIRED'),s02_member_preservation=json.loads((root/'qa/s03/S02_PRESERVATION_SUMMARY.json').read_text()),release_artifacts=dict(cumulative_zip=ident(zp),manifest=ident(mp),source_backed_diff=ident(dp)),archive_member_count=len(rows),archive_members={r['path']:dict(bytes=r['bytes'],sha256=r['sha256']) for r in rows},hash_binding_policy=dict(external_checkpoint_binds='ZIP, external exact manifest, external cumulative diff and every archive member',current_internal_state='state/CURSOR.json, independent of the external ZIP hash',manifest='External inventory, exactly one row per regular ZIP member',diff='Internal SOURCE_BACKED_DIFF.tsv is byte-identical to standalone sibling',self_hash='No circular self-hash; checkpoint is external; historic checkpoints/manifests are preserved evidence'),deterministic_zip=dict(method='Sorted NFC paths; fixed2026-09-21 timestamp; Unix0644 regular files; DEFLATE6; no directory entries',identical_second_build=True,reproducibility_scope='Same frozen member bytes; rebuilding PDFs in another TeX environment is not asserted byte-identical'),transport=dict(mode='SELF_CONTAINED_FULL_STATE',immutable_originals_embedded=21,cumulative_mutable_files_included=True,external_assembly_required=False,multipart_threshold_bytes=350000000,numbered_parts_required=zp.stat().st_size>350000000),archive_validation={'status':'PENDING_REOPEN'})
 wj(cp,cpj);report=ver.verify(zp,cp,mp,dp);cpj['archive_validation']=report;wj(cp,cpj);assert ver.verify(zp,cp,mp,dp)==report
 # This release is expected below the requested transport threshold. If it grows,
 # emit exact sequential chunks in addition to the verified complete ZIP.
 if zp.stat().st_size>350000000:
  parts=[];offset=0
  with zp.open('rb') as f:
   for n in range(1,10000):
    b=f.read(300000000)
    if not b:break
    p=out/(ZIPNAME+f'.part{n:03}');p.write_bytes(b);parts.append(dict(part=p.name,offset=offset,length=len(b),sha256=hashlib.sha256(b).hexdigest().upper()));offset+=len(b)
  wj(out/'PARTS.json',dict(archive=ident(zp),parts=parts,reassemble='Concatenate numbered parts in ascending order; verify archive size/hash.'))
 print(json.dumps(dict(release=cpj['release_artifacts'],checkpoint=ident(cp),archive_validation=report),ensure_ascii=False,indent=2))
 return cpj
if __name__=='__main__':
 root=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parents[2]
 out=Path(sys.argv[2]) if len(sys.argv)>2 else root.parent
 main(root,out)
