#!/usr/bin/env python3
"""Read English/apparatus only after verifying the new French freeze."""
import csv,hashlib,json,pathlib,sys
root=pathlib.Path(sys.argv[1]).resolve()
def canonical(x):return json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'))
def sha(x):return hashlib.sha256(x).hexdigest().upper()
def load(name):return [json.loads(s) for s in (root/f'edition/{name}.ndjson').read_text(encoding='utf-8').splitlines()]
src=load('source_language')
with (root/'audit/FINAL_SOURCE_FREEZE_V6.tsv').open(encoding='utf-8',newline='') as f:freeze=list(csv.DictReader(f,delimiter='\t'))
assert len(src)==len(freeze)==36 and all(sha(canonical(s).encode())==r['canonical_record_sha256'] and sha((root/r['french_record_path']).read_bytes())==r['sha256'] for s,r in zip(src,freeze))
en=load('english_standalone');app=load('apparatus')
for page,count in [(31,3),(32,1),(33,2),(35,2)]:
    assert en[page-1]['text'].count('). - ')==count,(page,count)
    en[page-1]['text']=en[page-1]['text'].replace('). - ','). — ')
    app[page-1]['text']+='\n\nThe long dash separating each numbered theorem, lemma, or remark label from its statement is retained from the authority; it is not replaced by a hyphen.'
for s,e,a in zip(src,en,app):
    e['based_on_source_record_sha256']=sha(canonical(s).encode());e['translation_policy']['final_freeze_receipt']='audit/FINAL_SOURCE_FREEZE_V6.tsv; every record and freeze byte verified before propagation'
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
