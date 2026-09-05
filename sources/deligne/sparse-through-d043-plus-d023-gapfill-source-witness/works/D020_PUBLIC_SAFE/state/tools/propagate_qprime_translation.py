#!/usr/bin/env python3
import csv,hashlib,json,pathlib,sys
root=pathlib.Path(sys.argv[1]).resolve()
def canonical(x):return json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'))
def sha(x):return hashlib.sha256(x).hexdigest().upper()
def load(name):return [json.loads(x) for x in (root/f'edition/{name}.ndjson').read_text(encoding='utf-8').splitlines()]
src=load('source_language')
with (root/'audit/FINAL_SOURCE_FREEZE_V4.tsv').open(encoding='utf-8',newline='') as f:freeze=list(csv.DictReader(f,delimiter='\t'))
assert all(sha(canonical(s).encode())==r['canonical_record_sha256'] for s,r in zip(src,freeze))
en=load('english_standalone');app=load('apparatus')
assert en[27]['text'].count('F_(q^r)')==3;en[27]['text']=en[27]['text'].replace('F_(q^r)','F_(q′)')
assert en[12]['text'].count('positive')==5;en[12]['text']=en[12]['text'].replace('positive','nonnegative')
app[27]['text']+='\n\nThe three extension-field labels in the first paragraph are F_(q′), as printed. The source subsequently states that q is replaced by q^r; that separate power is unchanged.'
app[12]['text']+='\n\nTranslation: “positifs” in (3.3)-(3.5) is rendered “nonnegative”; the proof explicitly gives ≥0 and an even trace power can vanish. This is the source meaning, not a strict-positivity assertion.'
for s,e,a in zip(src,en,app):
    e['based_on_source_record_sha256']=sha(canonical(s).encode());e['translation_policy']['final_freeze_receipt']='audit/FINAL_SOURCE_FREEZE_V4.tsv; verified before this final propagation'
    a['source_record_sha256']=sha(canonical(s).encode());a['english_record_sha256']=sha(canonical(e).encode())
for name,records in [('english_standalone',en),('apparatus',app)]:
    (root/f'edition/{name}.ndjson').write_text('\n'.join(canonical(x) for x in records)+'\n',encoding='utf-8',newline='\n')
cp=root/'coverage/coverage.tsv'
with cp.open(encoding='utf-8',newline='') as f:rows=list(csv.DictReader(f,delimiter='\t'));fields=list(rows[0])
for row,s,e,a in zip(rows,src,en,app):
    row['record_sha256_source']=sha(canonical(s).encode());row['record_sha256_english']=sha(canonical(e).encode());row['record_sha256_apparatus']=sha(canonical(a).encode())
with cp.open('w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
print(json.dumps({name:sha((root/f'edition/{name}.ndjson').read_bytes()) for name in ('source_language','english_standalone','apparatus')}))
