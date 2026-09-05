#!/usr/bin/env python3
"""Authority-only repairs following the all-36-page independent cold replay."""
import csv,hashlib,json,pathlib,sys
root=pathlib.Path(sys.argv[1]).resolve()
def canonical(x):return json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'))
def sha(x):return hashlib.sha256(x).hexdigest().upper()
srcpath=root/'edition/source_language.ndjson';src=[json.loads(s) for s in srcpath.read_text(encoding='utf-8').splitlines()]
with (root/'audit/FINAL_SOURCE_FREEZE_V4.tsv').open(encoding='utf-8',newline='') as f:prior=list(csv.DictReader(f,delimiter='\t'))
assert len(src)==len(prior)==36 and all(sha(canonical(s).encode())==r['canonical_record_sha256'] for s,r in zip(src,prior))
repairs=[
 (4,'=_(1.4.1) ∑_{n>0}','=_(1.4.1) ∑_n',1,'Last sum of (1.5.2) prints subscript n only; earlier sum n>0 remains.'),
 (16,'→_(x↦(x,δ))','→^{x↦(x,δ)}',1,'Map label is above the exact-sequence arrow in authority.'),
 (17,'→_(x↦Tr(x∪δ))','→^{x↦Tr(x∪δ)}',1,'Map label is above the arrow in (4.3.3).'),
 (21,'ι_(r)','ι_{(r)}',3,'Explicit literal parentheses belong inside the subscript and differ from subsequent plain r.')]
folder=root/'edition/source_freeze_final_v3';assert not folder.exists();folder.mkdir()
events=[]
for page,old,new,count,reason in repairs:
    r=src[page-1];assert r['text'].count(old)==count,(page,old)
    before=sha(canonical(r).encode());r['text']=r['text'].replace(old,new)
    path=folder/f'P{page:04d}.fr.txt';data=(r['text']+'\n').encode();path.write_bytes(data)
    previous=dict(r['final_french_freeze']);r['final_french_freeze']={'path':path.relative_to(root).as_posix(),'bytes':len(data),'sha256':sha(data),'policy':'Frozen from authority before V5 English/apparatus propagation.','pre_repair_record_sha256':before,'superseded_freeze':previous}
    events.append({'physical_page':page,'old':old,'new':new,'count':count,'authority_reason':reason,'before_record_sha256':before,'after_record_sha256':sha(canonical(r).encode())})
srcpath.write_text('\n'.join(canonical(r) for r in src)+'\n',encoding='utf-8',newline='\n')
with (root/'audit/FINAL_SOURCE_FREEZE_V5.tsv').open('w',encoding='utf-8',newline='') as f:
    w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(['physical_page','printed_page','french_record_path','bytes','sha256','canonical_record_sha256'])
    for r in src:
        v=r['final_french_freeze'];w.writerow([r['physical_page'],r['printed_page'],v['path'],v['bytes'],v['sha256'],sha(canonical(r).encode())])
(root/'audit/FINAL_SOURCE_COLD_V5_REPAIRS.ndjson').write_text('\n'.join(canonical(x) for x in events)+'\n',encoding='utf-8',newline='\n')
print(canonical({'french_freeze':'V5','source_ndjson_sha256':sha(srcpath.read_bytes()),'repair_pages':[r[0] for r in repairs]}))
