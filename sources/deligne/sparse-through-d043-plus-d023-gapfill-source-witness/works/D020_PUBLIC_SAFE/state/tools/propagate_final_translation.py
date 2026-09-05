#!/usr/bin/env python3
"""Propagate English and apparatus only after the exact final French freeze."""
import csv,hashlib,json,pathlib,sys
root=pathlib.Path(sys.argv[1]).resolve()
def canonical(x):return json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'))
def sha(x):return hashlib.sha256(x).hexdigest().upper()
def load(layer):return [json.loads(x) for x in (root/f'edition/{layer}.ndjson').read_text(encoding='utf-8').splitlines()]
source=load('source_language')
with (root/'audit/FINAL_SOURCE_FREEZE_V3.tsv').open(encoding='utf-8',newline='') as f:freeze=list(csv.DictReader(f,delimiter='\t'))
for r,row in zip(source,freeze):
    assert sha(canonical(r).encode())==row['canonical_record_sha256']
    assert sha((root/row['french_record_path']).read_bytes())==row['sha256']
english=load('english_standalone');app=load('apparatus');changes=[]
assert not (root/'audit/FINAL_ENGLISH_REPAIRS.ndjson').exists()
def change(rec,old,new,count=1):
    assert rec['text'].count(old)==count,(rec['physical_page'],old,rec['text'].count(old),count)
    rec['text']=rec['text'].replace(old,new);changes.append({'physical_page':rec['physical_page'],'old':old,'new':new,'count':count})
NOTES={
4:'Final authority replay: the orbit-set notation is |X|_F, with F a subscript. A quotient slash in the earlier French record was removed.',
6:'Final authority replay: the category map is rightward mapsto, printed again at the wrapped line. The repeated glyph indicates the same continued map, not a reverse equivalence arrow.',
7:'The two canonical sheaf isomorphisms retain the source rightward arrows with a tilde above.',
8:'Both the field isomorphism and induced cohomology isomorphism retain their source rightward arrows with a tilde above.',
9:'Final authority replay restores the printed dual superscript vee in the negative Tate twist.',
11:'Final authority replay restores all seven printed dual superscript vees and the rightward isomorphism arrow in (2.9.1).',
12:'Final authority replay restores the three printed dual superscript vees in the chain of pairings (2.12).',
14:'The coinvariant comparison uses a rightward isomorphism arrow; the following H_c^2 comparison has the undirected sign ≃. These distinct source forms are retained.',
16:'The first specialization composite has a leftward isomorphism arrow; the later comparison to the generic fiber has a rightward isomorphism arrow. Neither is an undirected congruence sign.',
17:'In (4.2.1) the first isomorphism points left; (4.3.2) points right. Both source directions are preserved.',
24:'The source literally prints R^i f_*Q_ℓ and R^i f_(0*)Q_ℓ in the sentence beginning “Ce dernier est défini”. These two i indices are retained; adjacent occurrences of n are not silently substituted for them.',
26:'The divisibility hypothesis in (6.8) literally has product index i and δ_i. This printed choice is retained, alongside the surrounding δ_j family.',
27:'In the Chebotarev sentence of (6.13), the source prints β_j^deg(x), not δ_j^deg(x). The same source reading is now retained in English.',
28:'The source Leray superscript is pq without an inserted comma. The two projective-embedding arrows in the prose are ordinary rightward arrows; the weak Lefschetz comparison in case A is an injection, not an asserted isomorphism.',
30:'The first displayed inequality of (7.3) literally has kd/2−1/2 in both exponents. The next display has upper exponent d/2+1/(2k). This source anomaly is preserved rather than silently repaired. The source also retains the α component index in c) and P_0 in the ambient space of (8.1).',
35:'The cohomological comparison in (8.11) retains its rightward isomorphism arrow and tilde.'
}
for r in english:
    p=r['physical_page']
    if p==6:change(r,'on X)\n           ↔','on X) ↦\n           ↦')
    if p in (7,8):change(r,'≅','→^{~}',2)
    if p in (9,11,12):change(r,'^~','^∨',{9:1,11:7,12:3}[p])
    if p==11:change(r,'≅','→^{~}')
    if p==14:
        change(r,'_Sp ≅','_Sp →^{~}');change(r,'≅','≃')
    if p==16:
        change(r,'H^i(X_0,Z) ≅ H^i(X,Z)','H^i(X_0,Z) ←^{~} H^i(X,Z)');change(r,'≅','→^{~}')
    if p==17:
        change(r,'H^i(X_s,Q_ℓ) ≅ H^i(X,Q_ℓ)','H^i(X_s,Q_ℓ) ←^{~} H^i(X,Q_ℓ)');change(r,'≅','→^{~}')
    if p==24:change(r,'The latter is defined over F_q: R^n f_*Q_ℓ is the inverse image of the Q_ℓ-sheaf R^n f_(0*)Q_ℓ','The latter is defined over F_q: R^i f_*Q_ℓ is the inverse image of the Q_ℓ-sheaf R^i f_(0*)Q_ℓ')
    if p==26:change(r,'∏_j(1−δ_j^deg(x)t) divides','∏_i(1−δ_i^deg(x)t) divides')
    if p==27:change(r,'some δ_j^deg(x) is an eigenvalue','some β_j^deg(x) is an eigenvalue')
    if p==28:
        change(r,'i:X↪P','i:X→P');change(r,'X_0↪P_0','X_0→P_0')
        change(r,'H^(n−1)(X_u,Q_ℓ)(−1) ≅ H^(n−1)(Y,Q_ℓ)(−1)','H^(n−1)(X_u,Q_ℓ)(−1) ↪ H^(n−1)(Y,Q_ℓ)(−1)')
    if p==30:
        change(r,'X_0^a','X_0^α',2);change(r,'X_0⊂P^(n+r)','X_0⊂P_0^(n+r)')
        change(r,'q^(kd/2−1/2) ≤ |α^k| ≤ q^(kd/2+1/2)','q^(kd/2−1/2) ≤ |α^k| ≤ q^(kd/2−1/2)')
    if p==35:change(r,'->~','→^{~}')
    r['based_on_source_record_sha256']=sha(canonical(source[p-1]).encode())
    r['objects']=source[p-1].get('objects',[])
    r.setdefault('translation_policy',{})['final_freeze_receipt']='audit/FINAL_SOURCE_FREEZE_V3.tsv; verified before this final propagation'
    r['translation_policy']['technical_notation']='Source mathematical symbols and directed arrows preserved; native math-typeset TeX is an editable presentation layer, not a correction of the authority.'
    a=app[p-1]
    a['text']=a['text'].replace('Included objects: running author head; ','Included article objects: ').replace('Included objects: running title head; ','Included article objects: ')
    a['text']=a['text'].replace('^~','^∨')
    a['text']=a['text'].replace('Paragraph (6.13) uses δ_j^deg(x).','Paragraph (6.13) uses β_j^deg(x).')
    a['text']=a['text'].replace('q^(kd/2−1/2)≤|α^k|≤q^(kd/2+1/2)','q^(kd/2−1/2)≤|α^k|≤q^(kd/2−1/2)')
    a['text']=a['text'].replace('editable text/linear mathematics','editable native mathematical TeX').replace('editable aligned text','editable mathematical arrays').replace('editable linear notation','editable mathematical TeX')
    if p in NOTES:a['text']+='\n\n'+NOTES[p]
    if p==1:a['text']+='\n\nPresentation policy: the French and English readers are separate editable native-math TeX editions. Running heads and repeated folios are excluded from the article bodies and retained only as provenance/page anchors. Source anomalies are identified in this apparatus; no emendation is silently substituted. Synthetic TIFF-header serialization differences across runtimes are separated from reproducible one-bit source-pixel identity in FINAL_PIXEL_PROVENANCE.tsv.'
    a['source_record_sha256']=sha(canonical(source[p-1]).encode());a['english_record_sha256']=sha(canonical(r).encode())
for name,rs in [('english_standalone',english),('apparatus',app)]:
    (root/f'edition/{name}.ndjson').write_text('\n'.join(canonical(x) for x in rs)+'\n',encoding='utf-8',newline='\n')
(root/'audit/FINAL_ENGLISH_REPAIRS.ndjson').write_text('\n'.join(canonical(x) for x in changes)+'\n',encoding='utf-8',newline='\n')
cp=root/'coverage/coverage.tsv'
with cp.open(encoding='utf-8',newline='') as f:rows=list(csv.DictReader(f,delimiter='\t'));fields=list(rows[0])
for row,s,e,a in zip(rows,source,english,app):
    row['record_sha256_source']=sha(canonical(s).encode());row['record_sha256_english']=sha(canonical(e).encode());row['record_sha256_apparatus']=sha(canonical(a).encode())
with cp.open('w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
print(json.dumps({'status':'FINAL_TRANSLATION_AND_APPARATUS_PROPAGATED_FOR_QA','records_per_layer':36,'english_repair_operations':len(changes),'hashes':{name:sha((root/f'edition/{name}.ndjson').read_bytes()) for name in ('source_language','english_standalone','apparatus')}}))
