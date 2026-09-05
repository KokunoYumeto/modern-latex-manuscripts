#!/usr/bin/env python3
"""Translation propagation is permitted only after exact V5 French verification."""
import csv,hashlib,json,pathlib,sys
root=pathlib.Path(sys.argv[1]).resolve()
def canonical(x):return json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'))
def sha(x):return hashlib.sha256(x).hexdigest().upper()
def load(name):return [json.loads(s) for s in (root/f'edition/{name}.ndjson').read_text(encoding='utf-8').splitlines()]
src=load('source_language')
with (root/'audit/FINAL_SOURCE_FREEZE_V5.tsv').open(encoding='utf-8',newline='') as f:freeze=list(csv.DictReader(f,delimiter='\t'))
assert len(src)==len(freeze)==36 and all(sha(canonical(s).encode())==r['canonical_record_sha256'] and sha((root/r['french_record_path']).read_bytes())==r['sha256'] for s,r in zip(src,freeze))
en=load('english_standalone');app=load('apparatus')
repairs=[(4,'=_(1.4.1) ∑_{n>0}','=_(1.4.1) ∑_n',1),(16,'→_(x↦(x,δ))','→^{x↦(x,δ)}',1),(17,'→_(x↦Tr(x∪δ))','→^{x↦Tr(x∪δ)}',1),(21,'ι_(r)','ι_{(r)}',3)]
for page,old,new,count in repairs:
    assert en[page-1]['text'].count(old)==count,(page,old);en[page-1]['text']=en[page-1]['text'].replace(old,new)
notes={4:'The last sum in (1.5.2) has subscript n only. The immediately preceding double sum retains n>0; no condition is supplied to the last sum.',16:'The map x↦(x,δ) is printed above its exact-sequence arrow; the editable encoding records an above-arrow label.',17:'In (4.3.3), x↦Tr(x∪δ) is printed above the arrow, not below it.',21:'The Veronese subscript is literally (r), whereas the later composite is denoted with plain r. Braces in the machine-readable encoding disambiguate those literal parentheses.'}
for page,note in notes.items():app[page-1]['text']+='\n\n'+note
for s,e,a in zip(src,en,app):
    e['based_on_source_record_sha256']=sha(canonical(s).encode());e['translation_policy']['final_freeze_receipt']='audit/FINAL_SOURCE_FREEZE_V5.tsv; every record and freeze byte verified before propagation'
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
