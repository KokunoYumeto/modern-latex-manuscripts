#!/usr/bin/env python3
"""One-shot authority-only long-separator repair; no English is opened."""
import csv,hashlib,json,pathlib,sys
root=pathlib.Path(sys.argv[1]).resolve()
def canonical(x):return json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'))
def sha(x):return hashlib.sha256(x).hexdigest().upper()
srcpath=root/'edition/source_language.ndjson'
src=[json.loads(s) for s in srcpath.read_text(encoding='utf-8').splitlines()]
with (root/'audit/FINAL_SOURCE_FREEZE_V5.tsv').open(encoding='utf-8',newline='') as f:prior=list(csv.DictReader(f,delimiter='\t'))
assert len(src)==len(prior)==36
assert all(sha(canonical(s).encode())==r['canonical_record_sha256'] and sha((root/r['french_record_path']).read_bytes())==r['sha256'] for s,r in zip(src,prior))
folder=root/'edition/source_freeze_final_v6';assert not folder.exists();folder.mkdir()
events=[]
for page,count in [(31,3),(32,1),(33,2),(35,2)]:
    r=src[page-1];old=sha(canonical(r).encode())
    assert r['text'].count('). - ')==count,(page,count)
    r['text']=r['text'].replace('). - ','). — ')
    path=folder/f'P{page:04d}.fr.txt';data=(r['text']+'\n').encode();path.write_bytes(data)
    previous=dict(r['final_french_freeze'])
    r['final_french_freeze']={'path':path.relative_to(root).as_posix(),'bytes':len(data),'sha256':sha(data),'policy':'Frozen directly from the authority before V6 English/apparatus propagation.','pre_repair_record_sha256':old,'superseded_freeze':previous}
    events.append({'physical_page':page,'old':'). - ','new':'). — ','count':count,'authority_reason':'The source prints a long dash after each theorem/remark/lemma numbered label, not a hyphen. Original scans inspected directly.','before_record_sha256':old,'after_record_sha256':sha(canonical(r).encode())})
srcpath.write_text('\n'.join(canonical(r) for r in src)+'\n',encoding='utf-8',newline='\n')
with (root/'audit/FINAL_SOURCE_FREEZE_V6.tsv').open('w',encoding='utf-8',newline='') as f:
    w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(['physical_page','printed_page','french_record_path','bytes','sha256','canonical_record_sha256'])
    for r in src:
        v=r['final_french_freeze'];w.writerow([r['physical_page'],r['printed_page'],v['path'],v['bytes'],v['sha256'],sha(canonical(r).encode())])
(root/'audit/FINAL_SOURCE_COLD_V6_REPAIRS.ndjson').write_text('\n'.join(canonical(x) for x in events)+'\n',encoding='utf-8',newline='\n')
print(canonical({'french_freeze':'V6','source_ndjson_sha256':sha(srcpath.read_bytes()),'repair_pages':[31,32,33,35],'separator_count':8}))
