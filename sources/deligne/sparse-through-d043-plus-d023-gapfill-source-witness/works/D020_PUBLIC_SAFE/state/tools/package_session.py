#!/usr/bin/env python3
import argparse,csv,hashlib,json,pathlib,subprocess,sys,zipfile
PREFIX='DELIGNE_D020_WEIL_I';AUTH_SHA='8392B345D4854E6DC55FB42CFC0B616D941935983723627237239A87348F42E5';PROMPTS=6
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest().upper()
def rows(p):
 with p.open(encoding='utf-8',newline='') as f:return list(csv.DictReader(f,delimiter='\t'))
def writej(p,o):p.write_bytes((json.dumps(o,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n').encode())
p=argparse.ArgumentParser();p.add_argument('root');p.add_argument('output_dir');p.add_argument('session_id');p.add_argument('prompt_id');p.add_argument('status',choices=('IN_PROGRESS','COMPLETE'));p.add_argument('--diagnostic',action='append',default=[]);a=p.parse_args();root=pathlib.Path(a.root).resolve();out=pathlib.Path(a.output_dir).resolve();out.mkdir(parents=True,exist_ok=True);n=int(a.prompt_id[1:]);assert a.session_id==f'S{n:02d}' and 1<=n<=PROMPTS
plan=rows(root/'control'/'SESSION_PLAN.tsv');row=plan[n-1];assert row['prompt_id']==a.prompt_id;cov=rows(root/'coverage'/'coverage.tsv');src=sum(r['source_status'] in ('ACCEPTED','FROZEN') for r in cov);en=sum(r['english_status']=='ACCEPTED' for r in cov);app=sum(r['apparatus_status']=='ACCEPTED' for r in cov);final=sum(r['final_status']=='ACCEPTED' for r in cov)
expected=tuple(int(row[k]) for k in ('cumulative_source_on_complete','cumulative_english_on_complete','cumulative_apparatus_on_complete','cumulative_final_on_complete'))
if a.status=='COMPLETE':
 assert (src,en,app,final)==expected;owned=set(range(int(row['physical_start']),int(row['physical_end'])+1));assert all(int(r['physical_page']) not in owned or (r['source_status']=='FROZEN' and r['english_status']=='ACCEPTED' and r['apparatus_status']=='ACCEPTED' and r['final_status']=='ACCEPTED') for r in cov)
 if n==PROMPTS:receipt=root/'audit'/f'S{n:02d}_COLD_AUDIT.tsv';assert receipt.is_file() and '\tPASS' in receipt.read_text(encoding='utf-8')
assert not any(r['source_status']=='DRAFT' or r['english_status']=='DRAFT' or r['apparatus_status']=='DRAFT' for r in cov) if a.status=='COMPLETE' else True
subprocess.run([sys.executable,str(root/'tools'/'validate_state.py'),str(root)],check=True);subprocess.run([sys.executable,str(root/'tools'/'build_readers.py'),str(root),'--check'],check=True);stem=f'{PREFIX}_S{n:02d}_CUMULATIVE';z=out/f'{stem}_FULL_STATE.zip';c=out/f'{stem}_CHECKPOINT.json';m=out/f'{stem}_MANIFEST.tsv';subprocess.run([sys.executable,str(root/'tools'/'package_state.py'),str(root),str(z)],check=True)
checkpoint={'schema_version':'deligne-exact-work-checkpoint-v2','work_id':PREFIX,'current_session':a.session_id,'prompt_id':a.prompt_id,'status':a.status,'source_page_count':src,'english_page_count':en,'apparatus_page_count':app,'final_accepted_page_count':final,'source_pdf_sha256':AUTH_SHA,'source_pdf_pages':36,'full_state':{'filename':z.name,'bytes':z.stat().st_size,'sha256':sha(z)},'next_prompt':('NONE_PROJECT_PASS' if n==PROMPTS and a.status=='COMPLETE' else (a.prompt_id if a.status=='IN_PROGRESS' else f'P{n+1:02d}')),'resume_rule':'Use newest same-session trio including IN_PROGRESS; otherwise predecessor COMPLETE; never roll back.','internal_diagnostics':a.diagnostic};writej(c,checkpoint)
lines=['scope\tpath\tbytes\tsha256',f'TRIO\t{z.name}\t{z.stat().st_size}\t{sha(z)}',f'TRIO\t{c.name}\t{c.stat().st_size}\t{sha(c)}']
with zipfile.ZipFile(z) as archive:
 for name in archive.namelist():data=archive.read(name);lines.append(f'STATE_MEMBER\t{name}\t{len(data)}\t{hashlib.sha256(data).hexdigest().upper()}')
m.write_text('\n'.join(lines)+'\n',encoding='utf-8',newline='\n')
