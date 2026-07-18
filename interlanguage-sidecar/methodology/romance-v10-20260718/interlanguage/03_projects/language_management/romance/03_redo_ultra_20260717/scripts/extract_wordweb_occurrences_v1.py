from __future__ import annotations
import csv, hashlib, json, re, unicodedata
from collections import Counter, defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
WORDWEB=ROOT/'wordweb'/'PAN_ROMANCE_WORDWEB_v3.json'
CORPUS=ROOT/'corpus'/'ROMANCE_CONSOLIDATED_CORPUS_v2.csv'
OUT=ROOT/'wordweb'/'ROMANCE_TERM_OCCURRENCES_v1.csv'

def read_csv(p):
    with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def fold(s):
    s=unicodedata.normalize('NFKD',s or '')
    return ''.join(c for c in s if not unicodedata.combining(c)).lower()
def key(s):return re.sub(r'[^a-z0-9]+',' ',fold(s)).strip()
def sha_text(s):return hashlib.sha256(s.encode('utf-8')).hexdigest().upper()
def context(line,form):
    words=re.findall(r'\S+',line.strip())
    head=(key(form).split() or [''])[0]
    idx=0
    for i,w in enumerate(words):
        if head and head in key(w).replace(' ',''):
            idx=i;break
    a=max(0,idx-8);b=min(len(words),idx+13)
    q=' '.join(words[a:b])
    return q+(' …' if b<len(words) else '')

ww=json.loads(WORDWEB.read_text(encoding='utf-8-sig'))
corpus=[r for r in read_csv(CORPUS) if r['counting_eligible'].lower()=='true' and r['language'] in {'es','fr','pt','gl','ca','it','ro','rm'}]
bylang=defaultdict(list)
for r in corpus:bylang[r['language']].append(r)

expected_domain={
 'T01':'ring_theory','T02':'field_theory','T03':'ring_theory','T04':'abstract_algebra','T05':'module_theory','T06':'ring_theory',
 'T07':'ring_theory','T08':'ring_theory','T09':'ring_theory','T10':'ring_theory','T17':'abstract_algebra','T18':'abstract_algebra',
 'T19':'abstract_algebra','T20':'abstract_algebra','T39':'group_theory','T40':'group_theory','T41':'proof_register','T42':'proof_register',
 'T43':'proof_register','T44':'proof_register','T45':'proof_register','T46':'proof_register','T47':'proof_register','T48':'proof_register',
 'T49':'proof_register','T50':'proof_register'
}

occ=[]; seen=set()
for node in ww['core_concepts']:
    tid=node['term_id']
    forms_by_lang=defaultdict(list)
    for f in node.get('forms',[]):
        lang=f['language']
        for val in (f.get('surface_as_inherited'),f.get('lemma_candidate')):
            if val and key(val) and key(val) not in {key(x) for x in forms_by_lang[lang]}:forms_by_lang[lang].append(val)
    for lang,forms in forms_by_lang.items():
        selected=0
        for src in bylang.get(lang,[]):
            if selected>=3:break
            p=Path(src.get('search_text_path') or src['absolute_path'])
            if not p.exists() or p.suffix.lower() not in {'.txt','.tex','.wikitext'}:continue
            try:lines=p.read_text(encoding='utf-8-sig',errors='replace').splitlines()
            except Exception:continue
            found_source=False
            for n,line in enumerate(lines,1):
                kl=' '+key(line)+' '
                for form in forms:
                    kf=key(form)
                    if not kf:continue
                    # Boundary on the normalized word sequence; never sum folded aliases.
                    if re.search(r'(?<![a-z0-9])'+re.escape(kf)+r'(?![a-z0-9])',kl):
                        q=context(line,form)
                        norm_group=f'{tid}:{lang}:{kf}'
                        oid='OCC-'+sha_text(f"{tid}|{lang}|{src['logical_source_id']}|{n}|{kf}|{q}")[:16]
                        dedupe=(src['logical_source_id'],n,kf,sha_text(q))
                        if dedupe in seen:continue
                        seen.add(dedupe)
                        tier='topic_shelf_context_candidate' if src['domain']==expected_domain.get(tid) else 'mechanical_context_candidate'
                        occ.append({
                          'occurrence_id':oid,'term_id':tid,'sense_ids':' | '.join(node['sense_ids']),'concept':node['concept'],'language':lang,
                          'surface_query':form,'normalization_group':norm_group,'logical_source_id':src['logical_source_id'],'record_id':src['record_id'],
                          'source_sha256':src['sha256'],'license_status':src['license_status'],'locator_path':str(p.resolve()),'line_number':n,
                          'quote':q,'quote_sha256':sha_text(q),'source_domain':src['domain'],'evidence_tier':tier,
                          'sense_review_status':'unreviewed_context_window','acceptance':'candidate_not_promoted'
                        })
                        selected+=1;found_source=True;break
                if found_source:break

fields=list(occ[0])
with OUT.open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(occ)

coverage=[]
for node in ww['core_concepts']:
    rs=[r for r in occ if r['term_id']==node['term_id']]
    coverage.append({'term_id':node['term_id'],'concept':node['concept'],'occurrences':len(rs),'languages_with_context':len({r['language'] for r in rs}),'languages':' '.join(sorted({r['language'] for r in rs})),'sense_reviewed_occurrences':0,'promotion_status':'blocked_pending_context_review'})
with (ROOT/'wordweb'/'ROMANCE_TERM_OCCURRENCE_COVERAGE_v1.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(coverage[0]));w.writeheader();w.writerows(coverage)

summary={'artifact':'ROMANCE_TERM_OCCURRENCES_v1','occurrence_count':len(occ),'terms_with_context':sum(r['occurrences']>0 for r in coverage),'terms_without_context':sum(r['occurrences']==0 for r in coverage),'languages':dict(Counter(r['language'] for r in occ)),'sense_reviewed':0,'promotion_eligible':0,'boundary':'Context windows are mechanical candidates. Diacritic-folded aliases share normalization groups and are not summed. No hit is a bridge decision.'}
(ROOT/'wordweb'/'ROMANCE_TERM_OCCURRENCES_v1.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(ROOT/'qa'/'TERM_OCCURRENCE_EXTRACTION_v1.log').write_text('\n'.join([f'PASS occurrences={len(occ)}',f'terms_with_context={summary["terms_with_context"]}',f'terms_without_context={summary["terms_without_context"]}',f'languages={summary["languages"]}','sense_reviewed=0','promotion_eligible=0'])+'\n',encoding='utf-8')
print(json.dumps(summary,ensure_ascii=False,indent=2))
