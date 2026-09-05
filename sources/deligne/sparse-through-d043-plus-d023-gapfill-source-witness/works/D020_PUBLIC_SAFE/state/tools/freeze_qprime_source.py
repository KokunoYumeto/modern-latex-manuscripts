#!/usr/bin/env python3
import csv,hashlib,json,pathlib,sys
root=pathlib.Path(sys.argv[1]).resolve()
def canonical(x):return json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'))
def sha(x):return hashlib.sha256(x).hexdigest().upper()
p=root/'edition/source_language.ndjson';records=[json.loads(x) for x in p.read_text(encoding='utf-8').splitlines()]
r=records[27];assert r['text'].count('F_(q^r)')==3;r['text']=r['text'].replace('F_(q^r)','F_(q′)')
folder=root/'edition/source_freeze_final_v2';assert not folder.exists();folder.mkdir();target=folder/'P0028.fr.txt';data=(r['text']+'\n').encode();target.write_bytes(data)
r['final_french_freeze']['superseded_freeze']=dict(r['final_french_freeze'])
r['final_french_freeze'].update(path=target.relative_to(root).as_posix(),bytes=len(data),sha256=sha(data))
p.write_text('\n'.join(canonical(x) for x in records)+'\n',encoding='utf-8',newline='\n')
with (root/'audit/FINAL_SOURCE_FREEZE_V4.tsv').open('w',encoding='utf-8',newline='') as f:
    w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(['physical_page','printed_page','french_record_path','bytes','sha256','canonical_record_sha256'])
    for r in records:
        v=r['final_french_freeze'];w.writerow([r['physical_page'],r['printed_page'],v['path'],v['bytes'],v['sha256'],sha(canonical(r).encode())])
(root/'audit/FINAL_SOURCE_QPRIME_REPAIR.json').write_text(canonical({'physical_page':28,'old':'F_(q^r)','new':'F_(q′)','count':3,'authority':'Original first paragraph field labels q-prime; separate q^r phrase unchanged.','source_ndjson_sha256':sha(p.read_bytes())})+'\n',encoding='utf-8',newline='\n')
print(sha(p.read_bytes()))
