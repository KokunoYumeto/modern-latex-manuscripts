from __future__ import annotations

import csv, hashlib, html, json, re, unicodedata
from collections import Counter, defaultdict
from html.parser import HTMLParser
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
REPO=ROOT.parents[3]
TRANSFER_ROOT=REPO/'02_native_source_corpora'/'github_language_source_bodies'/'romance-b3-transfer-ready-20260706'
TRANSFER_MANIFEST=TRANSFER_ROOT/'TRANSFER_BODY_FILE_MANIFEST.csv'
HTML_MANIFEST=ROOT/'corpus'/'WIKIMEDIA_HTML_CORPUS_MANIFEST_v1.csv'
HTML_REJECTED=ROOT/'corpus'/'WIKIMEDIA_HTML_REJECTED_AUTOMATIC_SEARCH_v1.csv'
HTML_TOPIC_REVIEW=ROOT/'curation'/'WIKIMEDIA_HTML_TOPIC_REVIEW_v1.csv'
CURATED_MANIFEST=ROOT/'corpus'/'CURATED_EXTERNAL_SOURCE_MANIFEST_v1.csv'
API_ROOT=ROOT/'corpus'/'downloaded_wikimedia'
SEARCH_ROOT=ROOT/'corpus'/'search_text'
SEARCH_ROOT.mkdir(parents=True,exist_ok=True)

class VisibleText(HTMLParser):
    def __init__(self): super().__init__(); self.skip=0; self.parts=[]
    def handle_starttag(self,tag,attrs):
        if tag in {'script','style','noscript','svg','math'}: self.skip+=1
    def handle_endtag(self,tag):
        if tag in {'script','style','noscript','svg','math'} and self.skip: self.skip-=1
    def handle_data(self,data):
        if not self.skip and data.strip(): self.parts.append(data.strip())

def hash_file(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''): h.update(b)
    return h.hexdigest().upper()

def read_csv(path):
    with path.open(encoding='utf-8-sig',newline='') as f: return list(csv.DictReader(f))

def write_csv(path,rows,fields=None):
    rows=list(rows); fields=fields or list(rows[0])
    with path.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(rows)

def license_state(signal):
    s=(signal or '').lower()
    if 'creativecommons.org/licenses/by-sa/4.0' in s: return 'declared_cc_by_sa_4_0'
    if 'cc-by-sa-3.0' in s: return 'declared_cc_by_sa_3_0_needs_attribution_check'
    if 'nonexclusive-distrib' in s: return 'arxiv_distribution_license_not_reuse_clear'
    if 'no license' in s or 'license-gap' in s or 'license null' in s: return 'unresolved_no_explicit_grant'
    if 'generated' in s: return 'generated_artifact_not_native_source'
    return 'unresolved'

def infer_domain(text):
    s=unicodedata.normalize('NFKD',(text or '').lower())
    s=''.join(c for c in s if not unicodedata.combining(c))
    if any(x in s for x in ['group','grup','grupo','groupe']): return 'group_theory'
    if any(x in s for x in ['ring','anill','anneau','anel','anello','inel']): return 'ring_theory'
    if any(x in s for x in ['field','cuerpo','corps','corpo','campo']): return 'field_theory'
    if any(x in s for x in ['module','modul','modulo']): return 'module_theory'
    if any(x in s for x in ['proof','demonstr','dimostraz']): return 'proof_register'
    if 'algebr' in s or 'alxebr' in s: return 'abstract_algebra'
    if 'analisi' in s: return 'analysis'
    return 'mathematics_mixed'

rows=[]; rejected=[]
LANG_NORMALIZE={'french':'fr','spanish':'es','italian':'it','portuguese':'pt','french/spanish':'fr_es'}
STARTING_STANDARDS=('es','fr','pt','ca','it','gl','ro','rm')
LANG_META={
    'es':('es','standard Spanish','Spain and Americas','Latn'),
    'fr':('fr','standard French','France and Francophonie','Latn'),
    'pt':('pt','standard Portuguese','Portugal Africa and Brazil','Latn'),
    'ca':('ca','standard Catalan','Catalan language area','Latn'),
    'it':('it','standard Italian','Italy and Switzerland','Latn'),
    'gl':('gl','standard Galician','Galicia','Latn'),
    'ro':('ro','standard Romanian','Romania and Moldova','Latn'),
    'rm':('rm-rg','Rumantsch Grischun','Graubünden Switzerland','Latn'),
    'fr_es':('fr-es-generated','generated French/Spanish support layer','generated comparator','Latn'),
}
topic_rows=read_csv(HTML_TOPIC_REVIEW)
topic_by_revision={(r['language_code'],r['page_id'],r['revision_id']):r for r in topic_rows}

if HTML_REJECTED.exists():
    for r in read_csv(HTML_REJECTED):
        rejected.append({
            'source':'wikimedia_html_automatic_search',
            'locator':r.get('source_url') or r.get('local_relative_path'),
            'reason':f"{r.get('rejection_reason')}:{r.get('language_code')}:{r.get('title')}:{r.get('query')}",
        })

# Individually reviewed external sources with preserved originals and searchable derivatives.
if CURATED_MANIFEST.exists():
    for r in read_csv(CURATED_MANIFEST):
        path=ROOT/Path(r['local_relative_path'])
        search=ROOT/Path(r['search_text_relative_path'])
        if not path.exists() or not search.exists():
            rejected.append({'source':'curated_external','locator':r['source_url'],'reason':'curated_original_or_search_derivative_missing'})
            continue
        actual=hash_file(path); search_actual=hash_file(search)
        rows.append({
            'record_id':r['source_id'],'logical_source_id':r['logical_source_id'],'language':r['language'],
            'variety_code':r['variety_code'],'standard_or_idiom':r['standard_or_idiom'],'region':r['region'],'script':r['script'],
            'secondary_language':r['secondary_language'],'institution':r['institution'],'publication_date':r['publication_date'],'retrieved_at':r['retrieved_at'],
            'domain':r['domain'],'domain_tags':r['domain_tags'],'domain_review_status':r['content_review_status'],
            'title_or_query':r['title'],'representation':path.suffix.lower().lstrip('.'),
            'absolute_path':str(path.resolve()),'search_text_path':str(search.resolve()),'search_text_sha256':search_actual,
            'bytes':path.stat().st_size,'sha256':actual,'upstream_locator':r['source_url'],'revision_or_version':r['publication_date'],
            'source_use_status':r['source_use_status'],'license_signal':r['license_signal'],'license_status':r['license_status'],
            'hash_verification':'match' if actual==r['sha256'] and search_actual==r['search_text_sha256'] and path.stat().st_size==int(r['bytes']) and search.stat().st_size==int(r['search_text_bytes']) else 'MISMATCH',
            'sense_review_status':'source_topic_reviewed_term_occurrences_require_language_and_sense_review',
            'corpus_topic_eligible':'true','native_source':'true','generated':'false','register':r['register'],
        })

# Recovered package: preserve every transfer row and its original label.
for i,r in enumerate(read_csv(TRANSFER_MANIFEST),1):
    rel=r['package_relative_path'].replace('/',str(Path('/')))
    path=TRANSFER_ROOT/Path(r['package_relative_path'])
    if not path.exists():
        rejected.append({'source':'transfer','locator':r['package_relative_path'],'reason':'file_missing'})
        continue
    actual=hash_file(path)
    expected=(r.get('package_sha256') or '').upper()
    rows.append({
        'record_id':f'TRANSFER-{i:04d}','logical_source_id':f"TRANSFER-{r.get('source_family_or_repo') or i}-{r.get('original_workspace_relative_path') or r['package_relative_path']}",
        'language':LANG_NORMALIZE.get((r.get('language') or 'unknown').lower(),(r.get('language') or 'unknown').lower()),'domain':infer_domain((r.get('source_family_or_repo') or '')+' '+r['package_relative_path']),
        'title_or_query':r.get('source_family_or_repo'),'representation':path.suffix.lower().lstrip('.') or 'binary',
        'absolute_path':str(path.resolve()),'bytes':path.stat().st_size,'sha256':actual,
        'upstream_locator':r.get('original_absolute_path'),'revision_or_version':'recovered_transfer_20260706',
        'source_use_status':r.get('source_use_label'),'license_signal':r.get('license_or_access_signal'),'license_status':license_state(r.get('license_or_access_signal')),
        'hash_verification':'match' if expected==actual else 'MISMATCH','sense_review_status':'not_term_sense_reviewed',
        'domain_tags':infer_domain((r.get('source_family_or_repo') or '')+' '+r['package_relative_path']),
        'domain_review_status':'transfer_manifest_subject_label_not_page_topic_review','corpus_topic_eligible':'true',
        'native_source':str(r.get('source_use_label')=='native-source-body').lower(),'generated':str(r.get('source_use_label')=='generated-draft').lower(),
    })

# Revision-identified Wikimedia HTML; reject zero-page placeholders and create searchable derivatives.
for i,r in enumerate(read_csv(HTML_MANIFEST),1):
    path=ROOT/Path(r['local_relative_path'])
    if not path.exists(): rejected.append({'source':'wikimedia_html','locator':r['local_relative_path'],'reason':'file_missing'});continue
    text=path.read_text(encoding='utf-8',errors='replace')
    rev=int(r.get('revision_id') or 0); pageid=int(r.get('page_id') or 0)
    if rev==0 or pageid==0:
        rejected.append({'source':'wikimedia_html','locator':r['local_relative_path'],'reason':'zero_page_or_revision_search_placeholder'});continue
    m=re.search(r'"wgTitle":"([^"]+)"',text)
    title=html.unescape(m.group(1)) if m else (r.get('title') or r['query'])
    topic=topic_by_revision.get((r['language_code'],str(pageid),str(rev)))
    if not topic:
        raise AssertionError(f'missing HTML topic review: {r["language_code"]} {pageid} {rev} {title}')
    if topic['title'] != title:
        raise AssertionError(f'topic title mismatch: review={topic["title"]!r} saved={title!r}')
    lic=re.search(r'<link rel="license" href="([^"]+)"',text)
    license_url=html.unescape(lic.group(1)) if lic else r.get('license_url')
    parser=VisibleText();parser.feed(text)
    visible='\n'.join(parser.parts)
    visible=re.sub(r'\n{3,}','\n\n',visible)
    txtdir=SEARCH_ROOT/r['language_code'];txtdir.mkdir(parents=True,exist_ok=True)
    txtpath=txtdir/f"WIKIHTML-{pageid}-{rev}.txt"
    txtpath.write_text(visible+'\n',encoding='utf-8')
    rows.append({
        'record_id':f'WIKIHTML-{r["language_code"].upper()}-{pageid}-{rev}','logical_source_id':f'WIKI-{r["language_code"]}-{pageid}-{rev}',
        'language':r['language_code'],'domain':topic['domain_primary'],'domain_tags':topic['domain_tags'],'title_or_query':title,'representation':'html',
        'absolute_path':str(path.resolve()),'search_text_path':str(txtpath.resolve()),'search_text_sha256':hash_file(txtpath),'bytes':path.stat().st_size,'sha256':hash_file(path),
        'upstream_locator':r['source_url'],'revision_or_version':str(rev),'source_use_status':'native_revision_pinned_context_shelf',
        'license_signal':license_url,'license_status':license_state(license_url),'hash_verification':'local_computed',
        'sense_review_status':'page_topic_reviewed_term_occurrences_require_context_review','domain_review_status':topic['review_status'],
        'corpus_topic_eligible':str(topic['topic_status']=='mathematics_relevant').lower(),'native_source':'true','generated':'false',
    })

# Preserve incomplete API wikitext acquisition as a separately labelled representation layer.
if API_ROOT.exists():
    for path in sorted(API_ROOT.glob('*/*.wikitext')):
        lang=path.parent.name
        m=re.match(r'(\d+)_(\d+)_(.*)\.wikitext$',path.name)
        if not m: rejected.append({'source':'wikimedia_api_partial','locator':str(path),'reason':'unparsed_filename'});continue
        pageid,rev,title=m.groups()
        topic=topic_by_revision.get((lang,pageid,rev))
        domain=topic['domain_primary'] if topic else infer_domain(title)
        domain_tags=topic['domain_tags'] if topic else domain
        rows.append({
            'record_id':f'WIKITEXT-{lang.upper()}-{pageid}-{rev}','logical_source_id':f'WIKI-{lang}-{pageid}-{rev}',
            'language':lang,'domain':domain,'domain_tags':domain_tags,'title_or_query':title.replace('_',' '),'representation':'wikitext',
            'absolute_path':str(path.resolve()),'search_text_path':str(path.resolve()),'search_text_sha256':hash_file(path),'bytes':path.stat().st_size,'sha256':hash_file(path),
            'upstream_locator':f'https://{lang}.wikipedia.org/w/index.php?curid={pageid}&oldid={rev}','revision_or_version':rev,
            'source_use_status':'partial_api_acquisition_preserved','license_signal':'Wikimedia project text; verify page footer/rightsinfo','license_status':'declared_cc_by_sa_4_0_project_terms_pending_page_match',
            'hash_verification':'local_computed','sense_review_status':'page_topic_reviewed_term_occurrences_require_context_review' if topic else 'automatic_search_result_requires_manual_review',
            'domain_review_status':topic['review_status'] if topic else 'unreviewed_partial_api_title_inference',
            'corpus_topic_eligible':str(bool(topic) and topic['topic_status']=='mathematics_relevant').lower(),'native_source':'true','generated':'false',
        })

# Plain-text source records use their source file as the canonical search path;
# rendered HTML uses the visible-text derivative created above.
text_representations={'tex','txt','csv','json','bib','bibtex','md','markdown','wikitext'}
for r in rows:
    meta=LANG_META.get(r['language'],(r['language'],'unresolved_standard','unresolved_region','Latn'))
    r.setdefault('variety_code',meta[0]);r.setdefault('standard_or_idiom',meta[1]);r.setdefault('region',meta[2]);r.setdefault('script',meta[3])
    r.setdefault('secondary_language','');r.setdefault('institution','');r.setdefault('publication_date','');r.setdefault('retrieved_at','');r.setdefault('register','unresolved_register')
    if not r.get('search_text_path') and r['representation'] in text_representations:
        r['search_text_path']=r['absolute_path']
        r['search_text_sha256']=r['sha256']
        r['search_text_contract']='source_file_is_canonical_search_text'
    elif r.get('search_text_path'):
        r['search_text_contract']='source_file_is_canonical_search_text' if r['search_text_path']==r['absolute_path'] else 'derived_visible_text'
    else:
        r['search_text_contract']='not_plain_text_searchable'

# Byte and logical dedupe. Prefer wikitext for search, then HTML, then TeX; retain every alias.
preference={'wikitext':0,'tex':1,'html':2,'txt':3,'csv':4,'json':5,'zip':9}
rows.sort(key=lambda r:(r['logical_source_id'],preference.get(r['representation'],8),r['record_id']))
seen_hash={};seen_logical={}
for r in rows:
    reasons=[]
    if r['sha256'] in seen_hash: reasons.append('byte_duplicate_of:'+seen_hash[r['sha256']])
    else: seen_hash[r['sha256']]=r['record_id']
    if r['logical_source_id'] in seen_logical: reasons.append('representation_alias_of:'+seen_logical[r['logical_source_id']])
    else: seen_logical[r['logical_source_id']]=r['record_id']
    r['dedupe_status']=';'.join(reasons) if reasons else 'primary_unique'
    native=r['native_source']=='true' and r['generated']=='false'
    topic_ok=r.get('corpus_topic_eligible')=='true'
    r['counting_eligible']=str(native and topic_ok and not reasons).lower()
    r['term_promotion_eligible']='false'

fields=['record_id','logical_source_id','language','variety_code','standard_or_idiom','region','script','secondary_language','institution','publication_date','retrieved_at','domain','domain_tags','domain_review_status','register','title_or_query','representation','absolute_path','search_text_path','search_text_sha256','search_text_contract','bytes','sha256','upstream_locator','revision_or_version','source_use_status','license_signal','license_status','hash_verification','sense_review_status','corpus_topic_eligible','native_source','generated','dedupe_status','counting_eligible','term_promotion_eligible']
for r in rows:
    for f in fields:r.setdefault(f,'')
write_csv(ROOT/'corpus'/'ROMANCE_CONSOLIDATED_CORPUS_v2.csv',rows,fields)
write_csv(ROOT/'corpus'/'ROMANCE_CORPUS_REJECTED_OR_EXCLUDED_v2.csv',rejected,['source','locator','reason'])

coverage=[]
for lang in sorted({r['language'] for r in rows}|set(STARTING_STANDARDS)):
    rs=[r for r in rows if r['language']==lang]
    prim=[r for r in rs if r['dedupe_status']=='primary_unique']
    counted_rows=[r for r in rs if r['counting_eligible']=='true']
    counted=sum(r['counting_eligible']=='true' for r in rs)
    if lang=='rm' and counted==0:
        body_status='explicit_zero_body_gap'
    elif counted:
        body_status='substantive_body_present'
    else:
        body_status='auxiliary_or_generated_only'
    coverage.append({
        'language':lang,'records':len(rs),'primary_unique_records':len(prim),'unique_logical_sources':len({r['logical_source_id'] for r in rs}),
        'bytes':sum(int(r['bytes']) for r in counted_rows),'all_primary_bytes':sum(int(r['bytes']) for r in prim),'declared_open_license_primary':sum(r['license_status'].startswith('declared_cc') for r in prim),
        'license_unresolved_primary':sum('unresolved' in r['license_status'] or 'not_reuse_clear' in r['license_status'] for r in prim),
        'domains':';'.join(sorted({tag for r in counted_rows for tag in r['domain_tags'].split(';') if tag})),'counting_eligible':counted,
        'term_promotion_eligible':0,'body_status':body_status,
    })
write_csv(ROOT/'corpus'/'ROMANCE_CORPUS_LANGUAGE_DOMAIN_COVERAGE_v2.csv',coverage)

summary={
    'artifact':'ROMANCE_CONSOLIDATED_CORPUS_v2','record_count':len(rows),'primary_unique_count':sum(r['dedupe_status']=='primary_unique' for r in rows),
    'byte_alias_count':sum('byte_duplicate' in r['dedupe_status'] for r in rows),'representation_alias_count':sum('representation_alias' in r['dedupe_status'] for r in rows),
    'excluded_count':len(rejected),'languages':coverage,'license_boundary':'Only explicit CC rows are treated as declared open; arXiv distribution and missing GitHub licenses remain unresolved.',
    'term_boundary':'No corpus record alone is term-promotion eligible. Every occurrence still requires sense/POS/register context review.',
    'domain_boundary':'Wikimedia domain labels come from the reviewed page-title ledger, never from the search query. Multi-domain tags are explicit.',
    'search_contract':'Every counting-eligible plain-text record declares a hash-verified search_text_path; source-native text may serve as its own canonical search path.',
    'starting_standard_status':{lang:next(x['body_status'] for x in coverage if x['language']==lang) for lang in STARTING_STANDARDS},
    'romansh_boundary':'Four downloaded automatic-search false hits remain quarantined. The only active Romansh body is an individually verified official German–Rumantsch Grischun school mathematics exam; it is not specialist algebra evidence.',
    'manifest_sha256':hash_file(ROOT/'corpus'/'ROMANCE_CONSOLIDATED_CORPUS_v2.csv'),
}
(ROOT/'corpus'/'ROMANCE_CONSOLIDATED_CORPUS_v2.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

assert {'es','fr','pt','gl','ca','it','ro'}.issubset({r['language'] for r in rows})
assert sum(r['language']=='rm' and r['counting_eligible']=='true' for r in rows)==1
assert next(x for x in coverage if x['language']=='rm')['body_status']=='substantive_body_present'
assert all(r['term_promotion_eligible']=='false' for r in rows)
assert not any(r['hash_verification']=='MISMATCH' for r in rows)
assert len({r['record_id'] for r in rows})==len(rows)
assert all(r['search_text_path'] and Path(r['search_text_path']).exists() and hash_file(Path(r['search_text_path']))==r['search_text_sha256'] for r in rows if r['counting_eligible']=='true')
log=[f"PASS consolidated_records={len(rows)}",f"primary_unique={summary['primary_unique_count']}",f"excluded={len(rejected)}",f"coverage_rows={len(coverage)}",'romansh_active_bodies=1','romansh_specialist_algebra_bodies=0',f"manifest_sha256={summary['manifest_sha256']}"]
(ROOT/'qa'/'CORPUS_BUILD_v2.log').write_text('\n'.join(log)+'\n',encoding='utf-8')
print('\n'.join(log))
