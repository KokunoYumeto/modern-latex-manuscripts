#!/usr/bin/env python3
"""Explicit source-side signature38 inventory, frozen before propagation."""
import csv,hashlib,json,pathlib,sys
root=pathlib.Path(sys.argv[1]).resolve()
def canonical(x):return json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'))
def sha(x):return hashlib.sha256(x).hexdigest().upper()
path=root/'edition/source_language.ndjson';src=[json.loads(x) for x in path.read_text(encoding='utf-8').splitlines()]
with (root/'audit/FINAL_SOURCE_FREEZE_V6.tsv').open(encoding='utf-8',newline='') as f:prior=list(csv.DictReader(f,delimiter='\t'))
assert len(src)==len(prior)==36 and all(sha(canonical(s).encode())==r['canonical_record_sha256'] and sha((root/r['french_record_path']).read_bytes())==r['sha256'] for s,r in zip(src,prior))
r=src[25];old=sha(canonical(r).encode());assert len(r['objects'])==7
r['objects'].append({'disposition':'EXCLUDE_BODY_RETAIN_PROVENANCE','id':'P0026-O08','kind':'printer_signature_38'})
folder=root/'edition/source_freeze_final_v7';assert not folder.exists();folder.mkdir()
freeze=folder/'P0026.fr.txt';data=(r['text']+'\n').encode();freeze.write_bytes(data)
r['final_french_freeze']={'path':freeze.relative_to(root).as_posix(),'bytes':len(data),'sha256':sha(data),'policy':'Authority signature38 explicitly inventoried; scholarly text unchanged; frozen before V7 English/apparatus propagation.','pre_repair_record_sha256':old,'superseded_freeze':dict(r['final_french_freeze'])}
path.write_text('\n'.join(canonical(r) for r in src)+'\n',encoding='utf-8',newline='\n')
with (root/'audit/FINAL_SOURCE_FREEZE_V7.tsv').open('w',encoding='utf-8',newline='') as f:
    w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(['physical_page','printed_page','french_record_path','bytes','sha256','canonical_record_sha256'])
    for r in src:
        v=r['final_french_freeze'];w.writerow([r['physical_page'],r['printed_page'],v['path'],v['bytes'],v['sha256'],sha(canonical(r).encode())])
print(canonical({'french_freeze':'V7','source_ndjson_sha256':sha(path.read_bytes()),'metadata_repair_page':26,'article_text_changed':False}))
