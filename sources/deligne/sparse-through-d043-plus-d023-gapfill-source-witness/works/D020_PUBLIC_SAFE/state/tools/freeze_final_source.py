#!/usr/bin/env python3
"""One-shot authority-derived versioned French repair and freeze.

Never reads English or apparatus.  Exact substitutions are asserted; every
before/after identity is preserved in the repair ledger.  The preceding
S06_candidate remains untouched.
"""
import csv,hashlib,json,pathlib,sys
root=pathlib.Path(sys.argv[1]).resolve()
def digest(data):return hashlib.sha256(data).hexdigest().upper()
def canonical(r):return json.dumps(r,ensure_ascii=False,sort_keys=True,separators=(',',':'))
path=root/'edition/source_language.ndjson'
records=[json.loads(x) for x in path.read_text(encoding='utf-8').splitlines() if x]
assert [x['physical_page'] for x in records]==list(range(1,37))
freeze=root/'edition/source_freeze_final_v1';assert not freeze.exists();freeze.mkdir()
changes=[]
def change(rec,old,new,count=1,reason='Authority pixel replay'):
    assert rec['text'].count(old)==count,(rec['physical_page'],old,rec['text'].count(old),count)
    rec['text']=rec['text'].replace(old,new)
    changes.append({'physical_page':rec['physical_page'],'old':old,'new':new,'count':count,'reason':reason})
for r in records:
    p=r['physical_page'];before=digest(canonical(r).encode())
    if p==4:change(r,'|X|/F','|X|_F',reason='Printed subscript orbit notation; quotient slash was not printed.')
    if p==6:
        change(r,'sur X)\n           ↔','sur X) ↦\n           ↦',reason='One rightward mapsto, repeated by source at its physical line wrap.')
    if p in (7,8):change(r,'≅','→^{~}',count=2,reason='Printed rightward isomorphism arrows, not undirected congruence signs.')
    if p in (9,11,12):change(r,'^~','^∨',count={9:1,11:7,12:3}[p],reason='Source dual superscript vee, not tilde.')
    if p==11:change(r,'≅','→^{~}',reason='Source (2.9.1) has a rightward isomorphism arrow.')
    if p==14:
        change(r,'_Sp ≅','_Sp →^{~}',reason='Source coinvariant comparison has a rightward isomorphism arrow.')
        change(r,'≅','≃',reason='Source next H_c^2 comparison is undirected simeq, separately distinguished.')
    if p==16:
        change(r,'H^i(X_0,Z) ≅ H^i(X,Z)','H^i(X_0,Z) ←^{~} H^i(X,Z)',reason='Specialization composite has source-directed leftward isomorphism.')
        change(r,'≅','→^{~}',reason='Source comparison to generic-fiber cohomology is a rightward isomorphism.')
    if p==17:
        change(r,'H^i(X_s,Q_ℓ) ≅ H^i(X,Q_ℓ)','H^i(X_s,Q_ℓ) ←^{~} H^i(X,Q_ℓ)',reason='Source (4.2.1) has a leftward isomorphism.')
        change(r,'≅','→^{~}',reason='Source (4.3.2) has a rightward isomorphism.')
    if p==24:change(r,'Ce dernier est défini sur F_q : R^n f_*Q_ℓ est l’image réciproque du Q_ℓ-faisceau R^n f_(0*)Q_ℓ','Ce dernier est défini sur F_q : R^i f_*Q_ℓ est l’image réciproque du Q_ℓ-faisceau R^i f_(0*)Q_ℓ',reason='Preserve the two printed R^i occurrences; do not silently normalize to R^n.')
    if p==26:change(r,'∏_j(1−δ_j^deg(x)t) divise','∏_i(1−δ_i^deg(x)t) divise',reason='Preserve source product index i and delta_i in (6.8).')
    if p==28:change(r,'E_2^(p,q)','E_2^(pq)',count=2,reason='Source Leray superscript pq has no inserted comma.')
    if p==30:change(r,'q^(kd/2−1/2) ≤ |α^k| ≤ q^(kd/2+1/2)','q^(kd/2−1/2) ≤ |α^k| ≤ q^(kd/2−1/2)',reason='Printed (7.3) first upper exponent has minus; source anomaly retained without mathematical correction.')
    if p==35:change(r,'->~','→^{~}',reason='Source comparison is a directed rightward isomorphism.')
    r.setdefault('editorial_policy',{})['final_authority_replay']='2026-08-31 independent all-36-page replay plus author magnification of proved discrepancies; older acceptance receipts do not replace this replay.'
    r['editorial_policy']['editable_math_encoding']='Machine-readable linear notation is retained in this record; the separate native mathematical TeX layer renders scripts, fractions, sums, matrices, and arrow topology and has a span ledger.'
    data=(r['text'].rstrip('\n')+'\n').encode('utf-8');fp=freeze/f'P{p:04d}.fr.txt';fp.write_bytes(data)
    r['final_french_freeze']={'path':fp.relative_to(root).as_posix(),'bytes':len(data),'sha256':digest(data),'pre_repair_record_sha256':before,'policy':'Frozen before final English and apparatus propagation.'}
path.write_text('\n'.join(canonical(r) for r in records)+'\n',encoding='utf-8',newline='\n')
(root/'audit/FINAL_SOURCE_REPAIRS.ndjson').write_text('\n'.join(canonical(x) for x in changes)+'\n',encoding='utf-8',newline='\n')
with (root/'audit/FINAL_SOURCE_FREEZE.tsv').open('w',encoding='utf-8',newline='') as f:
    w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(['physical_page','printed_page','french_record_path','bytes','sha256','canonical_record_sha256'])
    for r in records:
        freeze=r['final_french_freeze'];w.writerow([r['physical_page'],r['printed_page'],freeze['path'],freeze['bytes'],freeze['sha256'],digest(canonical(r).encode())])
print(json.dumps({'status':'SOURCE_FROZEN_NOT_TERMINALLY_ACCEPTED','records':36,'repair_operations':len(changes),'source_ndjson_sha256':digest(path.read_bytes())}))
