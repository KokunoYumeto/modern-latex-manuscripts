#!/usr/bin/env python3
import csv,hashlib,json,pathlib,sys
root=pathlib.Path(sys.argv[1]).resolve()
def canonical(x):return json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'))
def sha(x):return hashlib.sha256(x).hexdigest().upper()
def load(name):return [json.loads(s) for s in (root/f'edition/{name}.ndjson').read_text(encoding='utf-8').splitlines()]
src=load('source_language')
with (root/'audit/FINAL_SOURCE_FREEZE_V5.tsv').open(encoding='utf-8',newline='') as f:freeze=list(csv.DictReader(f,delimiter='\t'))
assert len(src)==len(freeze)==36 and all(sha(canonical(s).encode())==r['canonical_record_sha256'] for s,r in zip(src,freeze))
en=load('english_standalone');app=load('apparatus')
assert en[7]['text'].count('=_(def)')==2;en[7]['text']=en[7]['text'].replace('=_(def)','=_(dfn)')
assert app[2]['text'].count('Included objects: running author head, continuation')==1
app[2]['text']=app[2]['text'].replace('Included objects: running author head, continuation','Included article objects: continuation').replace('Repeated printed folio 274 is retained only as page provenance.','The running author head and repeated printed folio 274 are retained only as page provenance, excluded from the scholarly body.')
assert app[18]['text'].count('The running author head is retained;')==1
app[18]['text']=app[18]['text'].replace('The running author head is retained;','The running author head is retained only as provenance, excluded from the scholarly body;')
app[7]['text']+='\n\nThe equality annotations in (1.14.2) and (1.15.2) preserve the printed abbreviation dfn, including in the English reader; they are centered below the equality sign.'
for s,e,a in zip(src,en,app):
    e['based_on_source_record_sha256']=sha(canonical(s).encode());a['source_record_sha256']=sha(canonical(s).encode());a['english_record_sha256']=sha(canonical(e).encode())
for name,recs in [('english_standalone',en),('apparatus',app)]:
    (root/f'edition/{name}.ndjson').write_text('\n'.join(canonical(r) for r in recs)+'\n',encoding='utf-8',newline='\n')
cp=root/'coverage/coverage.tsv'
with cp.open(encoding='utf-8',newline='') as f:rows=list(csv.DictReader(f,delimiter='\t'));fields=list(rows[0])
for row,s,e,a in zip(rows,src,en,app):
    row['record_sha256_source']=sha(canonical(s).encode());row['record_sha256_english']=sha(canonical(e).encode());row['record_sha256_apparatus']=sha(canonical(a).encode())
with cp.open('w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
receipt={name:sha((root/f'edition/{name}.ndjson').read_bytes()) for name in ('source_language','english_standalone','apparatus')}
(root/'audit/FINAL_EN_APP_V5_REPAIRS.json').write_text(canonical({'repairs':'ENp8 def->dfn twice; APPp3/p19 head exclusion; APPp8 notation explanation','final_layer_sha256':receipt})+'\n',encoding='utf-8',newline='\n')
print(canonical(receipt))
