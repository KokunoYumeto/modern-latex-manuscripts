"""Deterministic task-local D031 build. Never writes input masters or publishes."""
from __future__ import annotations
import argparse, csv, hashlib, io, json, os, re, shutil, subprocess, zipfile
from pathlib import Path
import fitz

TASK = Path(__file__).resolve().parents[1]
BUILD = TASK / 'build/cumulative'
SOURCE = BUILD / 'source_tree'
AUDIT = BUILD / 'audit'
PREDROOT = TASK.parent / 'successor_D013_forward_integration_from_D023'
PRED = PREDROOT / 'build/cumulative'
GATE = TASK.parents[1] / 'Noether_Multilingual_Reconciliation/corpus_gate/D031'
WORK = SOURCE / 'works/D031_PUBLIC_SAFE'
PUBLIC_ARCHIVE = 'DELIGNE_D031_SHIMURA_CANONICAL_MODELS_FINAL_GLOBAL_AUDIT_BUNDLE_PUBLIC_SAFE.zip'
COVERAGE = 'D001-D016; D018; D021-D023; D025-D031; D034-D036; D038-D040; D043'
GAPS = 'D017; D019-D020; D024; D032-D033; D037; D041-D042'
READERS = {'EN':'english_translation', 'FR':'french_diplomatic'}
TOKEN = os.environ['USERNAME'].encode('utf-8')
assert TOKEN
LITERAL = re.compile(re.escape(TOKEN), re.I)
EPOCH = '946684800'
SLOTS = ('compile_slot_label_fixed','verification_twin_label_fixed','cold_replay_label_fixed')

def ident_data(data):
    return {'bytes':len(data), 'sha256':hashlib.sha256(data).hexdigest().upper(),
            'md5':hashlib.md5(data).hexdigest().upper()}

def identity(path):
    hs, hm, size = hashlib.sha256(), hashlib.md5(), 0
    with Path(path).open('rb') as f:
        for block in iter(lambda:f.read(2**20), b''):
            hs.update(block); hm.update(block); size += len(block)
    return {'bytes':size, 'sha256':hs.hexdigest().upper(), 'md5':hm.hexdigest().upper()}

def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2)+'\n', encoding='utf-8', newline='\n')

def tsv(path, rows, fields):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fields, delimiter='\t', lineterminator='\n')
        writer.writeheader(); writer.writerows(rows)

def rows(root, exclude=()):
    files = sorted(p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file())
    return [{'path':name, **{k:v for k,v in identity(root/name).items() if k != 'md5'}}
            for name in files if name not in exclude]

def check_expected(path, expected):
    actual = identity(path)
    assert all(actual[k] == v for k,v in expected.items() if k in actual), path.name
    return actual

def zi(name):
    assert not name.startswith('/') and '..' not in Path(name).parts
    item = zipfile.ZipInfo(name, (2000,1,1,0,0,0))
    item.create_system = 3; item.external_attr = 0o100644 << 16
    item.compress_type = zipfile.ZIP_DEFLATED; item._compresslevel = 6
    return item

def transform(data, path, graph):
    """Only literal replacement in matching non-ZIP leaves; exact unaffected bytes."""
    old = ident_data(data)
    if zipfile.is_zipfile(io.BytesIO(data)):
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            names = z.namelist()
            assert len(set(names)) == len(names)
            assert not any(LITERAL.search(n.encode()) for n in names)
            members = [(n, z.read(n)) for n in names]
        changed = [(n, transform(b, path+'::'+n, graph)) for n,b in members]
        if all(b == out for (_,b),(_,out) in zip(members,changed)):
            result, method = data, 'EXACT_UNCHANGED_ZIP'
        else:
            out = io.BytesIO()
            with zipfile.ZipFile(out, 'w', allowZip64=True) as z:
                for n,b in sorted(changed): z.writestr(zi(n), b)
            result, method = out.getvalue(), 'REPACK_CHANGED_DESCENDANTS_FIXED_METADATA'
    else:
        result, count = LITERAL.subn(b'[LOCAL_ACCOUNT]', data)
        if count:
            assert Path(path).suffix.lower() not in ('.pdf','.png','.jpg','.jpeg','.gif','.ttf','.otf'), path
            # Round-trip validates an ordinary UTF-8 text leaf, not binary patching.
            assert data.decode('utf-8').encode('utf-8') == data
        method = 'LITERAL_ACCOUNT_SUBSTITUTION' if count else 'EXACT_UNCHANGED_LEAF'
    graph.append({'path':path, 'original':old, 'public':ident_data(result), 'method':method,
                  'exact_unchanged':data == result})
    return result

def verify_inputs():
    AUDIT.mkdir(parents=True, exist_ok=True)
    receipt = check_expected(PRED/'BUILD_RELEASE_RECEIPT.json', {'bytes':5181,'sha256':'3C2E07F9311008C1D512921FEB1440FB28791DBF13A91B1E192D274349C6AA65'})
    pred = json.loads((PRED/'BUILD_RELEASE_RECEIPT.json').read_text())
    assert pred['status'] == 'PASS'
    for n,i in pred['release_files'].items(): check_expected(PRED/'release'/n, i)
    manifest = list(csv.DictReader((PRED/'source_tree/PUBLIC_SOURCE_MANIFEST.tsv').open(encoding='utf-8'), delimiter='\t'))
    for r in manifest: check_expected(PRED/'source_tree'/r['path'], {'bytes':int(r['bytes']), 'sha256':r['sha256']})
    gate_id = check_expected(GATE/'gate_acceptance.json', {'bytes':7951,'sha256':'45ACC6E6BC2C3CD60BD09294A84A08AAAD46FD0D9B9DDE81F27C4B98C03477DC'})
    gate = json.loads((GATE/'gate_acceptance.json').read_text())
    assert gate['decision'] == 'PASS_STAGED_NORMALIZED_EDITION'
    for r in gate['outputs']+gate['evidence']: check_expected(GATE/r['path'], r)
    anchor_paths = {
        'publication/release_execution_receipts/d013_20260831/ZENODO_PUBLIC_READBACK_RECEIPT.json':'9D36FB14E90F8E07BB36750D043D237C14AFD68C760DBEF30B6D4A03A47B9644',
        'publication/release_execution_receipts/d013_20260831/D013_CONCEPT_RESOLVER_VERIFIED_RECEIPT.json':'4061D0C2522221E3DF39A09784AAFE5FA59642C87557D4CE8105CF75EA5B2BE3',
        'publication/github/D013_GITHUB_PUBLIC_READBACK_RECEIPT.json':'A464666020522D51FA74FAFCD8E971C72155CBFCD2909E0CBDB11AB748397109'}
    anchors = {p:check_expected(PREDROOT/p, {'sha256':h}) for p,h in anchor_paths.items()}
    public = json.loads((PREDROOT/next(iter(anchor_paths))).read_text())
    assert public['status'] == 'PASS' and public['successor_record_id'] == '22208089'
    for item in public['public_files']: check_expected(PRED/'release'/item['filename'], item)
    inp = json.loads((GATE/'input_identity.json').read_text())
    original = Path(inp['archive'])
    check_expected(original, {'bytes':72931554,'sha256':gate['archive_sha256']})
    dump(AUDIT/'INPUT_REPLAY.json', {'schema':'d031-input-replay-v1','status':'PASS',
         'predecessor_receipt':receipt,'predecessor_source_members':len(manifest)+1,
         'predecessor_public_receipts':anchors,'gate':gate_id, 'gate_bound_files':26,
         'original_archive':{'filename':original.name, **identity(original)},
         'predecessor_record_id':'22208089','gate_disposition':gate['decision']})
    print('Exact predecessor, public identities and all26 D031 gate bindings PASS', flush=True)

def prepare():
    verify_inputs()
    done = AUDIT/'SOURCE_PREPARATION_RECEIPT.json'
    if done.exists():
        assert json.loads(done.read_text())['status'] == 'PASS'
        print('Preparation already complete; preserving staged files', flush=True); return
    assert not SOURCE.exists(), 'Inspect existing partial source before resuming'
    shutil.copytree(PRED/'source_tree', SOURCE)
    WORK.mkdir(parents=True)
    gate = json.loads((GATE/'gate_acceptance.json').read_text())
    graph = []
    selected = {'gate_acceptance.json'} | {r['path'] for r in gate['outputs']+gate['evidence']}
    selected |= {p.relative_to(GATE).as_posix() for p in (GATE/'input_state').rglob('*') if p.is_file() and p.suffix.lower() != '.zip'}
    for name in sorted(selected):
        p = WORK/name; p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(transform((GATE/name).read_bytes(), 'gate/'+name, graph))
    original = Path(json.loads((GATE/'input_identity.json').read_text())['archive'])
    original_data = original.read_bytes()
    arc_graph = []
    derivative = transform(original_data, original.name, arc_graph)
    # A second transformation from original bytes proves deterministic derivation.
    assert transform(original_data, original.name, []) == derivative
    arc_path = WORK/'source_archive'/PUBLIC_ARCHIVE
    arc_path.parent.mkdir(); arc_path.write_bytes(derivative)
    dump(AUDIT/'D031_ARCHIVE_DERIVATIVE_RECEIPT.json', {
        'schema':'d031-archive-public-derivative-v1','status':'PASS',
        'original_private_archive':{'filename':original.name, **ident_data(original_data)},
        'public_archive':{'filename':PUBLIC_ARCHIVE, **ident_data(derivative)},
        'source_zip_member':arc_path.relative_to(SOURCE).as_posix(), 'source_zip_copy_count':1,
        'repeat_derivation_byte_identical':True, 'original_preserved_untouched':True,
        'substitution':'Only case-insensitive literal local-account substring becomes [LOCAL_ACCOUNT]',
        'inherited_disposition':'ZERO_ACCEPTED', 'unique_evidence_objects_removed':0,
        'historical_manifest_policy':'Internal historical manifests identify original bytes; this external graph records all derivative identities without rewriting historical assertions.',
        'archive_graph':arc_graph, 'gate_file_graph':graph})
    for language,name in READERS.items():
        for ext in ('pdf','tex'):
            assert identity(WORK/'normalized'/f'{name}.{ext}') == identity(GATE/'normalized'/f'{name}.{ext}')
        text = (SOURCE/f'Deligne_{language}.tex').read_text(encoding='utf-8')
        text = text.replace('D025--D030','D025--D031').replace('D031--D033','D032--D033')
        title = {'EN':'Shimura Varieties and Canonical Models','FR':'Variétés de Shimura et modèles canoniques'}[language]
        line = rf'\includepdf[pages=-,pagecommand={{}},addtotoc={{1,section,1,{{D031 - {title}}},d031}}]{{works/D031_PUBLIC_SAFE/normalized/{name}.pdf}}'
        lines = text.splitlines()
        index = next(i for i,v in enumerate(lines) if r'\includepdf' in v and '{D034' in v)
        lines.insert(index,line)
        (SOURCE/f'Deligne_{language}.tex').write_text('\n'.join(lines)+'\n', encoding='utf-8',newline='\n')
    readme = (SOURCE/'README.md').read_text(encoding='utf-8')
    readme = readme.replace('D025-D030','D025-D031').replace('D031-D033','D032-D033')
    readme = readme.replace('790 English and 804 French','833 English and 847 French')
    readme += ('\n## D031 gap insertion\n\nD031, *Shimura Varieties: Modular Interpretation and Techniques for Constructing Canonical Models*, is inserted after D030 and before D034. Both accepted readers contain43 physical pages aligned to printed247-289; page290 is absent. French is diplomatic and English is a standalone translation. Exact native editable TeX, Markdown,12-page apparatus, controlling authority and comparison-only witness are under `works/D031_PUBLIC_SAFE`. The native readers contain23 TikZ-CD and7 native Dynkin diagrams each, no image fallbacks.\n\nCompile `normalized/english_translation.tex`, `normalized/french_diplomatic.tex`, or `normalized/apparatus.tex` with pdfLaTeX twice from that directory. These self-contained native sources reproduce the gate readers; the cumulative XeLaTeX instructions above remain applicable. Historical gate build scripts with literal local-account substitutions are evidentiary derivatives, not portable entrypoints.\n\nThe supplied original archive remains private and unchanged. Its original name/size/hash and every original-to-public member identity are in `D031_ARCHIVE_DERIVATIVE_RECEIPT.json`; the public-safe archive is included exactly once. Only literal local-account substrings in matching text leaves were replaced, while all unaffected member bytes remain exact. Historical internal manifests still attest original bytes, with the external derivative graph explaining changed ancestors. The nested raw editions and215 inherited salvage records remain ZERO_ACCEPTED and are not accepted reader input.\n')
    (SOURCE/'README.md').write_text(readme,encoding='utf-8',newline='\n')
    shutil.copy2(AUDIT/'D031_ARCHIVE_DERIVATIVE_RECEIPT.json', WORK/'D031_ARCHIVE_DERIVATIVE_RECEIPT.json')
    dump(done, {'status':'PASS','predecessor_source_files':2373,'gate_files_copied':len(selected),
               'derivative':identity(AUDIT/'D031_ARCHIVE_DERIVATIVE_RECEIPT.json'),
               'source_masters_modified':False,'predecessor_modified':False})
    print('Prepared maintained source and original-to-public derivative graph',flush=True)

def includes(root, language):
    text = (root/f'Deligne_{language}.tex').read_text(encoding='utf-8')
    result, first = [], 3
    for path in re.findall(r'\\includepdf\[.*?\]\{([^}]+)\}',text):
        with fitz.open(root/path) as doc: pages = len(doc)
        work = re.search(r'D\d{3}',path).group()
        result.append({'work':work,'path':path,'first':first,'last':first+pages-1,'pages':pages,'identity':identity(root/path)})
        first += pages
    assert [r['work'] for r in result] == sorted(set(r['work'] for r in result))
    return result

def cold():
    path = AUDIT/'COLD_REPRODUCIBILITY_RECEIPT.json'
    if path.exists() and json.loads(path.read_text()).get('status') == 'PASS':
        prior = json.loads(path.read_text())
        for lang in READERS: assert identity(SOURCE/f'Deligne_{lang}.pdf') == prior['languages'][lang]['reference']
        print('Existing cold PASS bytes verified',flush=True); return
    deps = {f'Deligne_{l}.tex' for l in READERS}
    for lang in READERS: deps.update(r['path'] for r in includes(SOURCE,lang))
    manifest = {n:identity(SOURCE/n) for n in sorted(deps)}
    dump(AUDIT/'COLD_INPUT_MANIFEST.json', {'status':'PASS','files':manifest,'clean_start':'Entrypoint TeX and referenced PDFs only; no cumulative PDF/aux/toc/log'})
    engine = shutil.which('xelatex'); assert engine
    env = dict(os.environ,SOURCE_DATE_EPOCH=EPOCH,FORCE_SOURCE_DATE='1',TZ='UTC')
    results = {'schema':'deligne-d031-cold-reproducibility-v1','status':'RUNNING',
               'engine':{'name':Path(engine).name, **identity(engine)},'languages':{},
               'environment':{k:env[k] for k in ('SOURCE_DATE_EPOCH','FORCE_SOURCE_DATE','TZ')},
               'inputs':identity(AUDIT/'COLD_INPUT_MANIFEST.json')}
    for slotname in SLOTS:
        slot = BUILD/slotname
        complete = AUDIT/f'{slotname}_COMPLETE.json'
        if complete.exists():
            saved = json.loads(complete.read_text())
            for lang in READERS: assert identity(slot/f'Deligne_{lang}.pdf') == saved[lang]['pdf']
            print('Reusing completed',slotname,flush=True); continue
        assert not slot.exists(), 'Existing incomplete slot must be inspected before bounded retry'
        slot.mkdir()
        for n in deps:
            (slot/n).parent.mkdir(parents=True,exist_ok=True); shutil.copy2(SOURCE/n,slot/n)
        saved = {}
        for lang in READERS:
            passes = []
            for i in (1,2):
                with (AUDIT/f'{slotname}_{lang}_{i}.stdout.txt').open('w',encoding='utf-8') as out:
                    run = subprocess.run([engine,'-interaction=nonstopmode','-halt-on-error',f'Deligne_{lang}.tex'],cwd=slot,env=env,stdout=out,stderr=subprocess.STDOUT,timeout=240)
                assert run.returncode == 0, (slotname,lang,i)
                log = (slot/f'Deligne_{lang}.log').read_text(encoding='utf-8',errors='replace')
                anomalies = {'errors':len(re.findall(r'^!',log,re.M)), 'missing_glyphs':log.count('Missing character:'),'overfull_boxes':log.count('Overfull ')}
                assert not any(anomalies.values()), (slotname,lang,i,anomalies)
                passes.append({'pass':i,'pdf':identity(slot/f'Deligne_{lang}.pdf'),'anomalies':anomalies})
                print(slotname,lang,'pass',i,'complete',flush=True)
            with fitz.open(slot/f'Deligne_{lang}.pdf') as doc: assert len(doc) == {'EN':833,'FR':847}[lang],len(doc)
            saved[lang] = {'pdf':identity(slot/f'Deligne_{lang}.pdf'),'passes':passes}
        assert all(identity(slot/n) == value for n,value in manifest.items())
        dump(complete,saved)
    for lang in READERS:
        copies = {s:identity(BUILD/s/f'Deligne_{lang}.pdf') for s in SLOTS}
        assert len({v['sha256'] for v in copies.values()}) == 1
        shutil.copy2(BUILD/SLOTS[0]/f'Deligne_{lang}.pdf',SOURCE/f'Deligne_{lang}.pdf')
        results['languages'][lang] = {'status':'PASS','reference':identity(SOURCE/f'Deligne_{lang}.pdf'),'independent_copies':copies,'pages':{'EN':833,'FR':847}[lang]}
    results.update(status='PASS',passes_per_language=2,independent_clean_builds=3,overlapping_builds=False,input_bytes_preserved=True)
    dump(path,results)
    print('Three clean cumulative builds byte-identical',flush=True)

def signature(page):
    pix = page.get_pixmap(matrix=fitz.Matrix(1,1),alpha=False,colorspace=fitz.csRGB)
    text = page.get_text()
    return {'raster_sha256':hashlib.sha256(pix.samples).hexdigest().upper(),'width':pix.width,'height':pix.height,
            'text_sha256':hashlib.sha256(text.encode()).hexdigest().upper(),'text_characters':len(text)}

def topology():
    path = AUDIT/'CUMULATIVE_PAGE_QA.json'
    if path.exists() and json.loads(path.read_text()).get('status') == 'PASS':
        for lang,value in json.loads(path.read_text())['languages'].items(): assert identity(SOURCE/f'Deligne_{lang}.pdf') == value['pdf']
        print('Existing all-page topology PASS verified',flush=True); return
    result = {'schema':'deligne-d031-cumulative-page-qa-v1','status':'RUNNING','languages':{},
              'renderer':f'PyMuPDF {fitz.VersionBind}; RGB72dpi alpha=false',
              'predecessor_receipt':identity(PRED/'BUILD_RELEASE_RECEIPT.json')}
    page_rows, include_rows = [], []
    visual = AUDIT/'changed_pages_144dpi'; visual.mkdir(exist_ok=True)
    for lang in READERS:
        newmap, oldmap = includes(SOURCE,lang), includes(PRED/'source_tree',lang)
        old_lookup = {r['work']:r for r in oldmap}; assert len(newmap) == len(oldmap)+1
        addition = next(r for r in newmap if r['work'] == 'D031'); assert addition['pages'] == 43
        for r in newmap:
            if r['work'] != 'D031': assert r['identity'] == old_lookup[r['work']]['identity']
            include_rows.append({'language':lang,**{k:r[k] for k in ('work','path','first','last','pages')},'source_sha256':r['identity']['sha256']})
        with fitz.open(SOURCE/f'Deligne_{lang}.pdf') as new, fitz.open(PRED/'release'/f'Deligne_{lang}.pdf') as old, fitz.open(SOURCE/addition['path']) as standalone:
            assert len(new) == len(old)+43 == newmap[-1]['last']
            retained, changed, insertion_raster_exact = 0, [], 0
            for i,page in enumerate(new):
                n=i+1; sig=signature(page); assert sig['text_characters'] > 0
                if addition['first'] <= n <= addition['last']:
                    kind='D031_INSERTION'; oldn=''; changed.append(n)
                    one=standalone[n-addition['first']]
                    assert re.sub(r'\s','',page.get_text()) == re.sub(r'\s','',one.get_text()),(lang,n)
                    insertion_raster_exact += (sig == signature(one))
                else:
                    oldn=n if n < addition['first'] else n-43
                    before=signature(old[oldn-1])
                    if n == 2:
                        kind='CONTENTS_UPDATED'; changed.append(n); assert sig != before and 'D031' in page.get_text()
                    else:
                        kind='PREDECESSOR_EXACT_RASTER_AND_TEXT'
                        assert sig == before,(lang,n,oldn); retained+=1
                page_rows.append({'language':lang,'page':n,'predecessor_page':oldn,'disposition':kind,**sig})
                if n in changed or n in (1,addition['first']-1,addition['last']+1):
                    page.get_pixmap(matrix=fitz.Matrix(2,2),alpha=False,colorspace=fitz.csRGB).save(visual/f'{lang}-{n:03}.png')
                if n%100 == 0: print('Raster/text replay',lang,n,'/',len(new),flush=True)
            result['languages'][lang]={'status':'PASS','pdf':identity(SOURCE/f'Deligne_{lang}.pdf'),
                'predecessor_pdf':identity(PRED/'release'/f'Deligne_{lang}.pdf'),'pages':len(new),'predecessor_pages':len(old),
                'd031_first':addition['first'],'d031_last':addition['last'],'new_work_pages':43,
                'contents_changed_pages':[2],'predecessor_exact_pages':retained,'rasterized_live_pages':len(new),
                'changed_visual_pages':changed,'new_work_standalone_raster_exact_pages':insertion_raster_exact,
                'new_work_all_text_exact':True,'all_later_work_input_bytes_identical':True,'all_later_pages_exact':True}
        dump(path,result)
    tsv(AUDIT/'PAGE_IDENTITY_MAP.tsv',page_rows,list(page_rows[0]))
    tsv(AUDIT/'INCLUDE_TOPOLOGY.tsv',include_rows,list(include_rows[0]))
    result.update(status='PASS',later_page_regression=False,rendered_live_page_total=sum(v['pages'] for v in result['languages'].values()),
                  exact_predecessor_pages=sum(v['predecessor_exact_pages'] for v in result['languages'].values()),
                  page_identity_map=identity(AUDIT/'PAGE_IDENTITY_MAP.tsv'),include_topology=identity(AUDIT/'INCLUDE_TOPOLOGY.tsv'))
    dump(path,result); print('Full retained-page non-regression PASS',flush=True)

def zip_tree(root,path):
    names=sorted(p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file())
    with zipfile.ZipFile(path,'w',allowZip64=True) as z:
        for name in names:
            with (root/name).open('rb') as src, z.open(zi(name),'w',force_zip64=True) as dst:
                shutil.copyfileobj(src,dst,2**20)
    actual=identity(path)
    return actual

def verify_zip(root,path):
    expected={r['path']:r for r in rows(root)}
    with zipfile.ZipFile(path) as z:
        assert z.namelist() == sorted(expected)
        for info in z.infolist():
            assert info.date_time == (2000,1,1,0,0,0)
            hs,size=hashlib.sha256(),0
            with z.open(info) as f:
                for block in iter(lambda:f.read(2**20),b''): hs.update(block); size+=len(block)
            assert size == expected[info.filename]['bytes']
            assert hs.hexdigest().upper() == expected[info.filename]['sha256'], info.filename
    return {'status':'PASS','members':len(expected),'every_member_hash_matches':True,
            'deterministic_metadata':True,'identity':identity(path)}

def visual_receipt():
    """Run only after direct main/independent final-image inspection recorded in WORKLOG."""
    presentation=json.loads((AUDIT/'D031_PRESENTATION_VALIDATION_RECEIPT.json').read_text())
    independent=json.loads((AUDIT/'D031_RELEASE_INDEPENDENT_CONTENT_AUDIT.json').read_text())
    pageqa=json.loads((AUDIT/'CUMULATIVE_PAGE_QA.json').read_text())
    assert presentation['status']==independent['status']==pageqa['status']=='PASS'
    languages={}
    for lang,first,last,fixed in (('EN',642,684,674),('FR',656,698,688)):
        p=presentation['languages'][lang]
        assert p['cumulative']['new_pdf']==identity(SOURCE/f'Deligne_{lang}.pdf')
        assert p['cumulative']['all_other_pages_raster_text_exact']
        image_paths=[f'changed_pages_144dpi/{lang}-{n:03}.png' for n in [2,first-1,*range(first,last+1),last+1]]
        languages[lang]={'status':'PASS','pdf':identity(SOURCE/f'Deligne_{lang}.pdf'),
            'd031_pages':list(range(first,last+1)),'contents_pages':[2],'seam_pages':[first-1,last+1],
            'all43_new_pages_reviewed':True,'native_math':'Editable TeX;23 TikZ-CD diagrams,7 native Dynkin diagrams and36 tagged displays; no image fallback',
            'initial_full_review':'Main direct whole-page Poppler144dpi review of all43 EN pages and seams; independent direct whole-page144dpi review of all43 FR pages, contents and seams',
            'presentation_repair_page':fixed,
            'unchanged42_review_reused_only_after_exact_raster_text_proof':True,
            'final_corrected_page_direct240dpi_review':'PASS_MAIN_AND_INDEPENDENT',
            'final_native_corrected_render':p['corrected_render'],
            'final_cumulative_corrected_render':p['cumulative']['render'],
            'fresh_final144dpi_renders':{n:identity(AUDIT/n) for n in image_paths},
            'observations':'Title, source numbering, formulas, diagram labels, section flow, contents and integration seams remain legible. Final label clears the oblique shaft. No unresolved integration clipping, overlap, missing glyph or reordering found.'}
    result={'schema':'deligne-d031-changed-page-visual-qa-v1','status':'PASS','languages':languages,
        'scope':'All86 inserted cumulative pages,2 revised contents pages,4 seam pages; enhanced240dpi direct review of corrected native/cumulative physical33 in both languages.',
        'renderer':'Final144dpi/240dpi PyMuPDF RGB; initial EN full sequence Poppler144dpi; independent nativeFR full sequence Poppler144dpi',
        'inherited_gate_scope':'Controlling43-page authority and original26gatebindings preserved; existing source/math gate not replaced by a claim of glyph-by-glyph authority recertification.',
        'original_visual_finding':'One diagram label crossed an oblique shaft; corrected by the sole10-byte pos=0.75 option and exact-original witness preservation.',
        'unresolved_visual_findings':[],'math_text_changed':False,'inherited_disposition':'ZERO_ACCEPTED__NO_PROMOTION',
        'presentation_validation':identity(AUDIT/'D031_PRESENTATION_VALIDATION_RECEIPT.json'),
        'independent_content_audit':identity(AUDIT/'D031_RELEASE_INDEPENDENT_CONTENT_AUDIT.json'),
        'independent_presentation_replay':identity(AUDIT/'D031_INDEPENDENT_PRESENTATION_REPLAY.json'),
        'pre_repair_fr_full_review':identity(AUDIT/'D031_FR_CUMULATIVE_VISUAL_REVIEW_PRE_PRESENTATION.json'),
        'all_page_identity':identity(AUDIT/'CUMULATIVE_PAGE_QA.json')}
    dump(AUDIT/'CHANGED_PAGE_VISUAL_QA.json',result)
    print('Final changed-page visual receipt PASS',flush=True)

def freeze():
    proof_names=['INPUT_REPLAY.json','D031_INDEPENDENT_INPUT_AUDIT.json','D031_ARCHIVE_DERIVATIVE_RECEIPT.json',
                 'COLD_INPUT_MANIFEST.json','COLD_REPRODUCIBILITY_RECEIPT.json','CUMULATIVE_PAGE_QA.json',
                 'PAGE_IDENTITY_MAP.tsv','INCLUDE_TOPOLOGY.tsv','CHANGED_PAGE_VISUAL_QA.json',
                 'D031_RELEASE_INDEPENDENT_CONTENT_AUDIT.json','D031_PUBLIC_DERIVATIVE_REPLAY.json',
                 'D031_PRESENTATION_VALIDATION_RECEIPT.json','PRESENTATION_LABEL_DELTA_EN.diff','PRESENTATION_LABEL_DELTA_FR.diff',
                 'D031_INDEPENDENT_PRESENTATION_REPLAY.json','D031_MAINTAINED_PUBLIC_LITERAL_SCAN.json',
                 'D031_FR_CUMULATIVE_VISUAL_REVIEW_PRE_PRESENTATION.json','D031_FR_NORMALIZED_VISUAL_REVIEW.json',
                 'D031_FINAL_CUMULATIVE_INDEPENDENT_REBIND.json']
    proof_names += [f'{slot}_COMPLETE.json' for slot in SLOTS]
    for name in ('COLD_REPRODUCIBILITY_RECEIPT.json','CUMULATIVE_PAGE_QA.json','CHANGED_PAGE_VISUAL_QA.json','D031_RELEASE_INDEPENDENT_CONTENT_AUDIT.json','D031_PRESENTATION_VALIDATION_RECEIPT.json'):
        assert json.loads((AUDIT/name).read_text())['status'] == 'PASS',name
    dest=SOURCE/'release_receipts/D031_GAPFILL'; dest.mkdir(parents=True,exist_ok=True)
    for name in proof_names: shutil.copy2(AUDIT/name,dest/name)
    shutil.copy2(AUDIT/'D031_PRESENTATION_VALIDATION_RECEIPT.json',WORK/'D031_PRESENTATION_VALIDATION_RECEIPT.json')
    # Every old path must remain; only the two cumulative PDFs/TeX, README and manifest change.
    before={r['path']:r for r in rows(PRED/'source_tree')}
    after={r['path']:r for r in rows(SOURCE)}
    assert set(before) <= set(after)
    changed=[n for n in before if before[n] != after[n]]
    allowed={'Deligne_EN.pdf','Deligne_FR.pdf','Deligne_EN.tex','Deligne_FR.tex','README.md','PUBLIC_SOURCE_MANIFEST.tsv'}
    assert set(changed) <= allowed,changed
    changed=sorted(set(changed)|{'PUBLIC_SOURCE_MANIFEST.tsv'})
    preserved={'schema':'d031-maintained-source-preservation-v1','status':'PASS',
               'predecessor_source_files':len(before),'no_removed_paths':True,
               'exact_unchanged_files':len(before)-len(changed),'changed_paths':changed,
               'intentional_changes':'Only cumulative entrypoints/readers, coverage/readme and source manifest; every work/source/evidence path retained unchanged.',
               'predecessor_receipt':identity(PRED/'BUILD_RELEASE_RECEIPT.json')}
    dump(AUDIT/'SOURCE_PRESERVATION_RECEIPT.json',preserved)
    shutil.copy2(AUDIT/'SOURCE_PRESERVATION_RECEIPT.json',dest/'SOURCE_PRESERVATION_RECEIPT.json')
    shutil.copy2(Path(__file__),dest/'build_d031_release.py')
    shutil.copy2(TASK/'scripts/repair_label_layout.py',dest/'repair_label_layout.py')
    source_receipt={'schema':'deligne-d031-gapfill-source-receipt-v1','status':'PASS',
        'predecessor_record_id':'22208089','concept_doi':'10.5281/zenodo.20410853',
        'included_complete_works':COVERAGE,'explicit_gaps':GAPS,'insertion':'D031 after D030 and before D034',
        'standalone':{l:{'pdf':identity(WORK/'normalized'/f'{n}.pdf'),'tex':identity(WORK/'normalized'/f'{n}.tex'),
                         'pages':43,'path':f'works/D031_PUBLIC_SAFE/normalized/{n}.pdf'} for l,n in READERS.items()},
        'archive_derivative_receipt':identity(AUDIT/'D031_ARCHIVE_DERIVATIVE_RECEIPT.json'),
        'local_unredacted_gate':identity(GATE/'gate_acceptance.json'),
        'public_gate':identity(WORK/'gate_acceptance.json'),'gate_bound_original_files':26,
        'accepted_reader_policy':'Original gate PDFs/TeX preserved exactly as witnesses; maintained readers have independently validated one-label-position presentation derivative; mathematical source untouched',
        'presentation_validation':identity(AUDIT/'D031_PRESENTATION_VALIDATION_RECEIPT.json'),
        'inherited_evidence_disposition':'ZERO_ACCEPTED__NO_PROMOTION','inputs_modified':False,'predecessor_modified':False}
    dump(dest/'D031_GAPFILL_SOURCE_RECEIPT.json',source_receipt)
    tsv(SOURCE/'PUBLIC_SOURCE_MANIFEST.tsv',rows(SOURCE,('PUBLIC_SOURCE_MANIFEST.tsv',)),['path','bytes','sha256'])
    print('Source manifest frozen',identity(SOURCE/'PUBLIC_SOURCE_MANIFEST.tsv'),flush=True)

def prepare_provenance():
    root=BUILD/'provenance_tree'; root.mkdir(exist_ok=True)
    pred_dir=root/'predecessor/record_22208089'; (pred_dir/'files').mkdir(parents=True,exist_ok=True)
    paths=[PREDROOT/'publication/release_execution_receipts/d013_20260831/ZENODO_PUBLIC_READBACK_RECEIPT.json',
           PREDROOT/'publication/release_execution_receipts/d013_20260831/D013_CONCEPT_RESOLVER_VERIFIED_RECEIPT.json',
           PREDROOT/'publication/github/D013_GITHUB_PUBLIC_READBACK_RECEIPT.json',
           PREDROOT/'publication/D013_FINAL_PUBLICATION_LEDGER_RECEIPT.json',PRED/'BUILD_RELEASE_RECEIPT.json']
    graph=[]
    for p in paths: (pred_dir/p.name).write_bytes(transform(p.read_bytes(),'predecessor/'+p.name,graph))
    public=json.loads(paths[0].read_text())
    assert public['status'] == 'PASS' and public['successor_record_id'] == '22208089'
    prior_carrier='DELIGNE_PROVENANCE_AUDIT_D013_FORWARD_INTEGRATION.zip'
    for item in public['public_files']:
        local=PRED/'release'/item['filename']; check_expected(local,item)
        if item['filename'] != prior_carrier: shutil.copy2(local,pred_dir/'files'/item['filename'])
    # Preserve compact superseded legacy D013 reader witnesses from the preceding carrier.
    old_legacy=PRED/'provenance_tree/superseded_github_standalones'
    shutil.copytree(old_legacy,root/'superseded_github_d013_standalones',dirs_exist_ok=True)
    with zipfile.ZipFile(PRED/'release'/prior_carrier) as z:
        for p in (root/'superseded_github_d013_standalones').iterdir():
            assert b'' != p.read_bytes() == z.read('superseded_github_standalones/'+p.name)
    compact=root/'d031_terminal_evidence'; compact.mkdir(exist_ok=True)
    shutil.copytree(SOURCE/'release_receipts/D031_GAPFILL',compact/'integration_receipts',dirs_exist_ok=True)
    for name in ('gate_acceptance.json','D031_ARCHIVE_DERIVATIVE_RECEIPT.json'):
        shutil.copy2(WORK/name,compact/name)
    for name in ('D031_FINAL_MANIFEST_REPLAY.json','SOURCE_PRESERVATION_RECEIPT.json'):
        shutil.copy2(AUDIT/name,compact/name)
    derivative=json.loads((AUDIT/'D031_ARCHIVE_DERIVATIVE_RECEIPT.json').read_text())
    dump(compact/'CURRENT_SOURCE_CARRIER_BINDING.json',{
         'schema':'d031-current-source-carrier-binding-v1','status':'PASS','carrier_filename':'Deligne_Source.zip',
         'source_manifest':identity(SOURCE/'PUBLIC_SOURCE_MANIFEST.tsv'),
         'archive':{k:derivative[k] for k in ('original_private_archive','public_archive','source_zip_member','source_zip_copy_count')},
         'authority_members':[{'path':r['path'],**{k:r[k] for k in ('bytes','sha256')}} for r in json.loads((GATE/'gate_acceptance.json').read_text())['outputs'] if r['role'] in ('CONTROLLING_AUTHORITY','COMPARISON_ONLY')],
         'no_duplicate_current_archive':True,'inherited_disposition':'ZERO_ACCEPTED',
         'gate_original_to_public_file_bindings':derivative['gate_file_graph']})
    dump(pred_dir/'PUBLIC_RECEIPT_DERIVATIVE_BINDINGS.json',{'status':'PASS','members':graph,
        'method':'Only literal account-name substring redacted where present; original SHA values remain original-byte evidence.'})
    (root/'README.md').write_text(
        '# D031 consolidated provenance\n\nThis carrier preserves byte-exact superseded D013 cumulative PDFs, TeX and maintained Source ZIP from public record22208089, the public-readback and Git commit evidence, compact predecessor legacy D013 reader witnesses, and current D031 integration gates. All six predecessor files, including its provenance carrier, retain their exact immutable public URL, size and hashes in the public readback receipt. The prior provenance ZIP is not recursively nested. Its already public older-history evidence remains linked through the exact predecessor receipt and source carrier.\n\nThe current complete D031 editable editions, authority/comparison witnesses, gate files and entire public-safe inherited archive are in the adjacent Deligne_Source.zip exactly as bound by its source manifest. The current73MB archive is represented once there rather than duplicated here; CURRENT_SOURCE_CARRIER_BINDING.json binds its member path and original-private versus public-derivative identities. Every inherited salvage row remains ZERO_ACCEPTED. No mathematical acceptance is inferred from archival inclusion.\n',encoding='utf-8',newline='\n')
    tsv(root/'PROVENANCE_MANIFEST.tsv',rows(root,('PROVENANCE_MANIFEST.tsv',)),['path','bytes','sha256'])
    return root

def package():
    final=BUILD/'BUILD_RELEASE_RECEIPT.json'
    if final.exists() and json.loads(final.read_text()).get('status') == 'PASS':
        for n,v in json.loads(final.read_text())['release_files'].items(): assert identity(BUILD/'release'/n) == v
        print('Existing final release verified',flush=True); return
    independent=json.loads((AUDIT/'D031_FINAL_MANIFEST_REPLAY.json').read_text())
    assert independent['status'] == 'PASS'
    expected=rows(SOURCE,('PUBLIC_SOURCE_MANIFEST.tsv',))
    manifest=list(csv.DictReader((SOURCE/'PUBLIC_SOURCE_MANIFEST.tsv').open(encoding='utf-8'),delimiter='\t'))
    assert [{**r,'bytes':int(r['bytes'])} for r in manifest] == expected
    source_manifest=identity(SOURCE/'PUBLIC_SOURCE_MANIFEST.tsv')
    release=BUILD/'release'; release.mkdir(exist_ok=True)
    twin=BUILD/'zip_verification_twin'; twin.mkdir(exist_ok=True)
    for name in ('Deligne_EN.pdf','Deligne_FR.pdf','Deligne_EN.tex','Deligne_FR.tex'): shutil.copy2(SOURCE/name,release/name)
    provenance=prepare_provenance()
    zip_results={}
    for root,name in ((SOURCE,'Deligne_Source.zip'),(provenance,'DELIGNE_PROVENANCE_AUDIT_D031_GAPFILL.zip')):
        if (release/name).exists() and (twin/name).exists():
            actual=identity(release/name); assert actual == identity(twin/name)
        else:
            actual=zip_tree(root,release/name); print('Built',name,actual,flush=True)
            assert zip_tree(root,twin/name) == actual
        zip_results[name]=verify_zip(root,release/name)
        zip_results[name]['repeat_build_byte_identical']=True
        print('Full ZIP member replay PASS',name,flush=True)
    assert rows(SOURCE,('PUBLIC_SOURCE_MANIFEST.tsv',)) == expected
    assert identity(SOURCE/'PUBLIC_SOURCE_MANIFEST.tsv') == source_manifest
    files={p.name:identity(p) for p in sorted(release.iterdir()) if p.is_file()}
    assert len(files)==6 and sum(v['bytes'] for v in files.values()) <= 50_000_000_000
    tsv(BUILD/'SIX_FILE_RELEASE_MANIFEST.tsv',[{'filename':n,'bytes':v['bytes'],'sha256':v['sha256']} for n,v in files.items()],['filename','bytes','sha256'])
    topology_receipt=json.loads((AUDIT/'CUMULATIVE_PAGE_QA.json').read_text())
    proof_names=['INPUT_REPLAY.json','D031_INDEPENDENT_INPUT_AUDIT.json','D031_ARCHIVE_DERIVATIVE_RECEIPT.json',
                 'COLD_REPRODUCIBILITY_RECEIPT.json','CUMULATIVE_PAGE_QA.json','CHANGED_PAGE_VISUAL_QA.json',
                 'D031_RELEASE_INDEPENDENT_CONTENT_AUDIT.json','D031_FINAL_MANIFEST_REPLAY.json','SOURCE_PRESERVATION_RECEIPT.json',
                 'D031_PUBLIC_DERIVATIVE_REPLAY.json','D031_PRESENTATION_VALIDATION_RECEIPT.json']
    receipt={'schema':'deligne-d031-gapfill-release-build-receipt-v1','status':'PASS',
        'build_identity':'D031-GAPFILL-FROM-D013-20260831','predecessor_record_id':'22208089',
        'predecessor_version_doi':'10.5281/zenodo.22208089','concept_doi':'10.5281/zenodo.20410853',
        'predecessor_receipt':identity(PRED/'BUILD_RELEASE_RECEIPT.json'),
        'predecessor_github_payload_commit':'60fffd570685021c78c26a77bd406d10337a035f',
        'included_complete_works':COVERAGE,'explicit_gaps':GAPS,'insertion':'D031 after D030 and before D034',
        'release_files':files,'six_file_manifest':identity(BUILD/'SIX_FILE_RELEASE_MANIFEST.tsv'),
        'source_manifest':source_manifest,'source_tree_files_excluding_manifest':len(expected),
        'source_zip_members':zip_results['Deligne_Source.zip']['members'],
        'provenance_zip_members':zip_results['DELIGNE_PROVENANCE_AUDIT_D031_GAPFILL.zip']['members'],
        'zip_verification':zip_results,
        'compiled':{l:{'cumulative_pages':topology_receipt['languages'][l]['pages'],
            'predecessor_pages':topology_receipt['languages'][l]['predecessor_pages'],'standalone_d031_pages':43,
            'd031_first':topology_receipt['languages'][l]['d031_first'],'d031_last':topology_receipt['languages'][l]['d031_last'],
            'pdf':files[f'Deligne_{l}.pdf']} for l in READERS},
        'd031_archive':{k:v for k,v in json.loads((AUDIT/'D031_ARCHIVE_DERIVATIVE_RECEIPT.json').read_text()).items() if k in ('original_private_archive','public_archive','source_zip_member','source_zip_copy_count')},
        'receipts':{n:identity(AUDIT/n) for n in proof_names},
        'inherited_evidence_disposition':'ZERO_ACCEPTED__NO_PROMOTION','inputs_modified':False,'predecessor_modified':False,
        'git_operations':'NONE','publication_operations':'NONE',
        'ordinary_record_limit_bytes':50_000_000_000,'aggregate_release_bytes':sum(v['bytes'] for v in files.values()),
        'aggregate_within_record_limit':True,'all_files_observed_below_500mb':all(v['bytes']<500_000_000 for v in files.values()),
        'size_scope':'500MB is not a cumulative publication gate; six-file aggregate within documented50GB ordinary record limit',
        'size_scope_authority':identity(TASK/'publication/PUBLICATION_SIZE_SCOPE.md')}
    dump(final,receipt); print('Six-file deterministic package PASS',flush=True)

def surface():
    receipt_path=BUILD/'BUILD_RELEASE_RECEIPT.json'
    receipt=json.loads(receipt_path.read_text()); assert receipt['status']=='PASS'
    release=BUILD/'release'
    assert sorted(p.name for p in release.iterdir() if p.is_file()) == sorted(receipt['release_files'])
    assert len(receipt['release_files'])==6
    for n,v in receipt['release_files'].items(): assert identity(release/n)==v
    findings=[]; text_count=pdf_count=pdf_pages=0
    token=TOKEN.decode().casefold()
    # Exact immutable inherited ZIPs use their prior literal-scan evidence; current
    # D031 recursive ZIP contents have a fresh independent zero-finding receipt.
    for root in (SOURCE,BUILD/'provenance_tree'):
        for p in sorted(root.rglob('*')):
            if not p.is_file(): continue
            rel=p.relative_to(root).as_posix()
            if token in rel.casefold(): findings.append({'path':rel,'kind':'filename'})
            if p.suffix.lower() in ('.md','.txt','.json','.tsv','.csv','.tex','.py','.ps1','.yaml','.yml','.html','.js','.bib','.log'):
                text_count+=1
                if token in p.read_text(encoding='utf-8',errors='replace').casefold(): findings.append({'path':rel,'kind':'text'})
            elif p.suffix.lower()=='.pdf':
                pdf_count+=1
                with fitz.open(p) as doc:
                    pdf_pages+=len(doc)
                    if token in json.dumps(doc.metadata,ensure_ascii=False).casefold() or any(token in page.get_text().casefold() for page in doc): findings.append({'path':rel,'kind':'pdf_text_or_metadata'})
    assert not findings,findings
    arc=json.loads((AUDIT/'D031_ARCHIVE_DERIVATIVE_RECEIPT.json').read_text())
    with zipfile.ZipFile(release/'Deligne_Source.zip') as z:
        assert z.namelist().count(arc['source_zip_member'])==1
        with z.open(arc['source_zip_member']) as f:
            digest,size=hashlib.sha256(),0
            for block in iter(lambda:f.read(2**20),b''): digest.update(block);size+=len(block)
        assert size==arc['public_archive']['bytes'] and digest.hexdigest().upper()==arc['public_archive']['sha256']
        assert not any(Path(n).name==arc['original_private_archive']['filename'] for n in z.namelist())
    result={'schema':'deligne-d031-release-surface-replay-v1','status':'PASS',
        'exact_file_count':6,'release_files':receipt['release_files'],
        'source_manifest':identity(SOURCE/'PUBLIC_SOURCE_MANIFEST.tsv'),'source_tree_frozen':True,
        'source_manifest_final_independent_replay':identity(AUDIT/'D031_FINAL_MANIFEST_REPLAY.json'),
        'source_zip_every_member_verified':True,'provenance_zip_every_member_verified':True,
        'source_zip_members':receipt['source_zip_members'],'provenance_zip_members':receipt['provenance_zip_members'],
        'd031_archive':{k:arc[k] for k in ('original_private_archive','public_archive','source_zip_member','source_zip_copy_count')},
        'literal_account_check':{'status':'PASS','findings':[],'ordinary_text_files':text_count,'pdf_files':pdf_count,'pdf_pages':pdf_pages,
          'method':'One literal case-insensitive account-name check only; filenames, ordinary text and PDF extracted text/metadata; no OCR or inferred privacy patterns',
          'nested_current_archive_proof':identity(AUDIT/'D031_PUBLIC_DERIVATIVE_REPLAY.json'),
          'nested_inherited_archive_basis':'Exact unchanged maintained source bytes and predecessor source manifest carry previously completed public-safe archive gates; no old archive is changed'},
        'aggregate_release_bytes':sum(v['bytes'] for v in receipt['release_files'].values()),
        'ordinary_record_limit_bytes':50_000_000_000,'aggregate_within_record_limit':True,
        'publication_operations':'NONE','git_operations':'NONE'}
    dump(AUDIT/'RELEASE_SURFACE_REPLAY.json',result)
    receipt['literal_account_name_check']='PASS_ZERO_FINDINGS'
    receipt['release_surface_replay']=identity(AUDIT/'RELEASE_SURFACE_REPLAY.json')
    dump(receipt_path,receipt);print('Final exact-six surface PASS',identity(receipt_path),flush=True)

if __name__ == '__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('stage',choices=['verify_inputs','prepare','cold','topology','visual_receipt','freeze','package','surface'])
    globals()[parser.parse_args().stage]()
