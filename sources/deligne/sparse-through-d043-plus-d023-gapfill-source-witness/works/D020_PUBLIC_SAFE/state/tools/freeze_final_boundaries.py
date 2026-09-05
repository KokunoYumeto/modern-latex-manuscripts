#!/usr/bin/env python3
"""Freeze corrected disposition metadata; does not change frozen French text."""
import csv,hashlib,json,pathlib,sys
root=pathlib.Path(sys.argv[1]).resolve()
def canonical(x):return json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'))
def sha(x):return hashlib.sha256(x).hexdigest().upper()
p=root/'edition/source_language.ndjson';records=[json.loads(x) for x in p.read_text(encoding='utf-8').splitlines()]
out=root/'audit/FINAL_SOURCE_FREEZE_V2.tsv';assert not out.exists()
for r in records:
    for o in r.get('objects',[]):
        if o['kind'].startswith('running_head_'):o['disposition']='EXCLUDE_BODY_RETAIN_PROVENANCE'
        elif o['disposition']=='INCLUDE_EDITABLE_LINEAR_MATH':o['disposition']='INCLUDE_EDITABLE_TYPESET_MATH'
        elif o['disposition']=='INCLUDE_EDITABLE_TEXT_DIAGRAM':o['disposition']='INCLUDE_EDITABLE_MATH_DIAGRAM'
    r['editorial_policy']['running_head_boundary']='Running-head strings remain in source provenance records; excluded from both scholarly reader bodies by explicit object disposition.'
    f=r['final_french_freeze'];assert sha((root/f['path']).read_bytes())==f['sha256']
p.write_text('\n'.join(canonical(x) for x in records)+'\n',encoding='utf-8',newline='\n')
with out.open('w',encoding='utf-8',newline='') as stream:
    w=csv.writer(stream,delimiter='\t',lineterminator='\n');w.writerow(['physical_page','printed_page','french_record_path','bytes','sha256','canonical_record_sha256'])
    for r in records:
        f=r['final_french_freeze'];w.writerow([r['physical_page'],r['printed_page'],f['path'],f['bytes'],f['sha256'],sha(canonical(r).encode())])
print(json.dumps({'status':'SOURCE_AND_BOUNDARIES_FROZEN','ndjson_sha256':sha(p.read_bytes()),'receipt':str(out)}))
