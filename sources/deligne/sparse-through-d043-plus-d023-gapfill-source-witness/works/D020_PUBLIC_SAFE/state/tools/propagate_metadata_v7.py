#!/usr/bin/env python3
"""Post-French-freeze signature38 English/apparatus propagation."""
import csv,hashlib,json,pathlib,sys
root=pathlib.Path(sys.argv[1]).resolve()
def canonical(x):return json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'))
def sha(x):return hashlib.sha256(x).hexdigest().upper()
def load(name):return [json.loads(x) for x in (root/f'edition/{name}.ndjson').read_text(encoding='utf-8').splitlines()]
src=load('source_language')
with (root/'audit/FINAL_SOURCE_FREEZE_V7.tsv').open(encoding='utf-8',newline='') as f:freeze=list(csv.DictReader(f,delimiter='\t'))
assert len(src)==len(freeze)==36 and all(sha(canonical(s).encode())==r['canonical_record_sha256'] and sha((root/r['french_record_path']).read_bytes())==r['sha256'] for s,r in zip(src,freeze))
en=load('english_standalone');app=load('apparatus')
assert len(en[25]['objects'])==7
en[25]['objects'].append(dict(src[25]['objects'][-1]))
app[25]['text']+='\n\nThe printer signature 38 below the lower folio 297 is retained in source-image provenance and explicitly inventoried as P0026-O08; it is excluded from both scholarly bodies.'
for s,e,a in zip(src,en,app):
    e['based_on_source_record_sha256']=sha(canonical(s).encode());e['translation_policy']['final_freeze_receipt']='audit/FINAL_SOURCE_FREEZE_V7.tsv; every record and freeze byte verified before propagation'
    a['source_record_sha256']=sha(canonical(s).encode());a['english_record_sha256']=sha(canonical(e).encode())
for name,recs in [('english_standalone',en),('apparatus',app)]:
    (root/f'edition/{name}.ndjson').write_text('\n'.join(canonical(r) for r in recs)+'\n',encoding='utf-8',newline='\n')
cp=root/'coverage/coverage.tsv'
with cp.open(encoding='utf-8',newline='') as f:rows=list(csv.DictReader(f,delimiter='\t'));fields=list(rows[0])
for row,s,e,a in zip(rows,src,en,app):
    row['record_sha256_source']=sha(canonical(s).encode());row['record_sha256_english']=sha(canonical(e).encode());row['record_sha256_apparatus']=sha(canonical(a).encode())
with cp.open('w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
print(canonical({name:sha((root/f'edition/{name}.ndjson').read_bytes()) for name in ('source_language','english_standalone','apparatus')}))
