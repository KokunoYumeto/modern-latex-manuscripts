"""Bounded, non-publishing D019 cumulative integration from frozen D017.

All writes are confined to this task. Canonical bytes are never replaced by
transport bytes; the latter are separate admitted reader derivatives.
"""
from __future__ import annotations
import argparse, csv, ctypes, datetime, hashlib, json, os, re, shutil
import subprocess, sys, time, zipfile
from pathlib import Path
import fitz

TASK = Path(__file__).resolve().parents[1]
BUILD = TASK / 'build/cumulative'
SOURCE = BUILD / 'source_tree'
AUDIT = BUILD / 'audit'
PRED = TASK.parent / 'successor_D017_gapfill_from_D031/build/cumulative'
D019 = TASK.parent.parent / 'Noether_Multilingual_Reconciliation/corpus_gate/D019'
TRANSPORT = D019 / 'transport_derivatives/method03_zopfli'
PRED_HASH = 'BB3E6E7A81FD76BDBCF46B55828318C3D2FE2BC2D8477F2ED201A1303D2DA381'
GATE_HASH = '7A2AB6F8E967122AA973E96A3C74EDC52D3517D6D89C17DF27541436B4C094EB'
WORK = SOURCE / 'works/D019_PUBLIC_SAFE'
RECEIPTS = SOURCE / 'release_receipts/D019_FORWARD_INTEGRATION'
EXPECTED = {
    'EN': ('ENGLISH', 155, 96950348, 'FD8277444D0E21DCC62938D51F259243F9D21895B692A6461021D7ACEE4E15F5'),
    'FR': ('SOURCE_LANGUAGE', 154, 96955847, '36D19867B309DC38A51431D0817B30F48B4679D75F9AD15618A3A7ED50FAA296'),
}
MUTABLE = {'Deligne_EN.tex', 'Deligne_FR.tex', 'Deligne_EN.pdf', 'Deligne_FR.pdf', 'README.md', 'PUBLIC_SOURCE_MANIFEST.tsv'}

class Failure(RuntimeError): pass

def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def read(path): return json.loads(Path(path).read_text(encoding='utf-8'))
def sha(path):
    p = Path(path)
    if not p.is_file() or p.is_symlink(): raise Failure('not a plain input: ' + p.name)
    h, m, size = hashlib.sha256(), hashlib.md5(), 0
    with p.open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block); m.update(block); size += len(block)
    return {'bytes': size, 'sha256': h.hexdigest().upper(), 'md5': m.hexdigest().upper()}
def check(path, identity):
    actual = sha(path)
    for key in ('bytes', 'sha256', 'md5'):
        if key in identity and actual[key] != identity[key]: raise Failure('input identity mismatch: ' + Path(path).name)
    return actual
def safe(path):
    p = Path(path).resolve()
    if not p.is_relative_to(TASK.resolve()): raise Failure('write outside task')
    return p
def write(path, value):
    path = safe(path); path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + '\n', encoding='utf-8', newline='\n')
    return sha(path)
def write_text(path, text):
    path = safe(path); path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8', newline='\n')
def copy(src, dst):
    dst = safe(dst); dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists(): check(dst, sha(src))
    else: shutil.copy2(src, dst)
    check(dst, sha(src))
def rows(root):
    out = []
    for p in sorted(Path(root).rglob('*')):
        if p.is_symlink(): raise Failure('symlink in bounded tree')
        if p.is_file(): out.append({'path': p.relative_to(root).as_posix(), **sha(p)})
    return out
def tsv(path, entries):
    path = safe(path); path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(entries[0]), delimiter='\t', lineterminator='\n'); w.writeheader(); w.writerows(entries)
    return sha(path)
def cursor(stage, next_action, **extra):
    return write(TASK / 'CURSOR.json', {'schema': 'd019-cumulative-integration-cursor-v1', 'status': stage,
      'updated_utc': now(), 'write_boundary': '.', 'build_root': 'build/cumulative', 'predecessor_build_receipt_sha256': PRED_HASH,
      'canonical_gate_sha256': GATE_HASH, 'no_git_or_publication': True, 'next_action': next_action, **extra})

def predecessor():
    check(PRED / 'BUILD_RELEASE_RECEIPT.json', {'sha256': PRED_HASH})
    receipt = read(PRED / 'BUILD_RELEASE_RECEIPT.json')
    if receipt['status'] != 'PASS': raise Failure('predecessor gate')
    manifest = PRED / 'source_tree/PUBLIC_SOURCE_MANIFEST.tsv'
    check(manifest, receipt['source_tree']['manifest'])
    with manifest.open(encoding='utf-8', newline='') as f: expected = list(csv.DictReader(f, delimiter='\t'))
    actual = rows(PRED / 'source_tree')
    lookup = {r['path']: r for r in actual if r['path'] != 'PUBLIC_SOURCE_MANIFEST.tsv'}
    if set(lookup) != {r['path'] for r in expected}: raise Failure('predecessor manifest coverage')
    for r in expected:
        if lookup[r['path']]['bytes'] != int(r['bytes']) or lookup[r['path']]['sha256'] != r['sha256']: raise Failure('predecessor manifest replay')
    for name, identity in receipt['release_files'].items(): check(PRED / 'release' / name, identity)
    result = {'status': 'PASS', 'build_receipt': sha(PRED / 'BUILD_RELEASE_RECEIPT.json'), 'source_manifest': sha(manifest),
      'files': len(actual), 'pages': {'EN': 885, 'FR': 899}, 'source_tree_replayed': True,
      'public_identity_supplied_by_parent': {'record': '22236378', 'concept': '20410853',
      'github_payload_commit': 'db7f1038c8f77f36d24cea9e3dc916444226114c', 'github_crosslink_commit': '389e10b33e89e323e375b547342bcd484e5426fc'},
      'independent_publication_readback_responsibility': 'parent', 'inputs_modified': False}
    write(AUDIT / 'D017_BASELINE_BINDING.json', result)
    return result

def canonical():
    gate = D019 / 'receipts/D019_CANONICAL_FINAL_GATE.json'
    check(gate, {'sha256': GATE_HASH}); data = read(gate)
    if data['status'] != 'PASS' or data['remaining_issues'] or data['article_pages'] != 73 or data['authority_pdf_pages'] != 74: raise Failure('canonical gate invalid')
    selected = list(data['outputs_and_receipts']) + [{'path': 'receipts/D019_CANONICAL_FINAL_GATE.json', **sha(gate)}]
    for r in selected: check(D019 / r['path'], r)
    # Presentation assets are gate-bound by the accepted build manifest and TSV.
    asset_manifest = D019 / 'canonical_build/output/assets/D019_PRESENTATION_ASSET_MANIFEST.tsv'
    with asset_manifest.open(encoding='utf-8', newline='') as f: assets = list(csv.DictReader(f, delimiter='\t'))
    if len(assets) != 144: raise Failure('canonical presentation asset count')
    for asset in assets:
        check(asset_manifest.parent / asset['output_filename'], {'bytes': int(asset['bytes']), 'sha256': asset['sha256']})
    result = {'status': 'PASS', 'gate': sha(gate), 'files': selected, 'asset_manifest_rows': len(assets),
      'article_pages': 73, 'authority_pdf_pages': 74, 'cover_excluded': True,
      'canonical_reader_pages': {'EN': 155, 'FR': 154}, 'inherited_disposition': 'ZERO_ACCEPTED'}
    write(AUDIT / 'D019_CANONICAL_INPUT_VERIFICATION.json', result)
    return result

def prepare():
    if SOURCE.exists(): raise Failure('source tree exists; resume from cursor, do not rebuild')
    base, can = predecessor(), canonical()
    safe(SOURCE).mkdir(parents=True)
    for r in rows(PRED / 'source_tree'): copy(PRED / 'source_tree' / r['path'], SOURCE / r['path'])
    for r in can['files']: copy(D019 / r['path'], WORK / r['path'])
    for sub in ('assets', 'asset_overrides'):
        src = D019 / 'canonical_build/output' / sub
        for r in rows(src): copy(src / r['path'], WORK / 'canonical_build/output' / sub / r['path'])
    packet = WORK / 'canonical_build/output/source_packet/D019_CANONICAL_SOURCE_PACKET.zip'
    with zipfile.ZipFile(packet) as z:
        authority_name = 'replay_primary/corpus/source/20_AUTHORITY_DELIGNE_D019_HODGE_III_IAS_NUMBER19_74PP.pdf'
        info = z.getinfo(authority_name)
        if info.file_size <= 0: raise Failure('empty authority in full source packet')
        authority = WORK / 'authority/D019_PRINTED_AUTHORITY_74PP.pdf'
        safe(authority).parent.mkdir(parents=True)
        with z.open(info) as a, authority.open('wb') as b: shutil.copyfileobj(a, b, 1024 * 1024)
        check(authority, sha(D019 / authority_name))
        if len(fitz.open(authority)) != 74: raise Failure('authority page topology')
        member_replay = []
        for i in z.infolist():
            h = hashlib.sha256(); size = 0
            with z.open(i) as f:
                for b in iter(lambda: f.read(1024 * 1024), b''): h.update(b); size += len(b)
            if size != i.file_size: raise Failure('canonical source packet member mismatch')
            member_replay.append({'path': i.filename, 'bytes': size, 'sha256': h.hexdigest().upper()})
        tsv(AUDIT / 'D019_CANONICAL_PACKET_MEMBER_REPLAY.tsv', member_replay)
    copy(AUDIT / 'D017_BASELINE_BINDING.json', RECEIPTS / 'D017_BASELINE_BINDING.json')
    copy(AUDIT / 'D019_CANONICAL_INPUT_VERIFICATION.json', RECEIPTS / 'D019_CANONICAL_INPUT_VERIFICATION.json')
    copy(PRED / 'BUILD_RELEASE_RECEIPT.json', RECEIPTS / 'D017_PREDECESSOR_BUILD_RELEASE_RECEIPT.json')
    identity = tsv(AUDIT / 'D019_PRESERVED_SOURCE_MANIFEST.tsv', rows(WORK))
    result = {'status': 'SOURCE_PRESERVATION_PASS_TRANSPORT_ADMISSION_PENDING', 'canonical_inputs': can,
      'predecessor': base, 'preserved_manifest': identity, 'authority': sha(authority), 'full_source_packet': sha(packet),
      'source_inputs_modified': False, 'reader_transport_accepted': False}
    write(AUDIT / 'SOURCE_PREPARATION_RECEIPT.json', result)
    cursor('SOURCE_PRESERVED_TRANSPORT_ADMISSION_PENDING', 'Validate supplied final transport receipt; admit exact lossless reader derivatives; patch cumulative masters; build under global TeX mutex.', source_preparation=sha(AUDIT / 'SOURCE_PREPARATION_RECEIPT.json'))
    return result

def admit(receipt_path):
    receipt_path = Path(receipt_path).resolve()
    if receipt_path != (TRANSPORT.parent/'TRANSPORT_RESULT.json').resolve(): raise Failure('not the named terminal transport receipt')
    check(receipt_path, {'sha256':'958851CCB55B8D3E8357D451EBBA80F7110E7AC281D7550FBD1C8747840B8BE2'})
    receipt = read(receipt_path)
    # Admission additionally requires the parent/transport agent to identify the exact final PASS receipt.
    if receipt.get('status') != 'PASS': raise Failure('transport acceptance receipt not PASS')
    if receipt['content_gate_sha256'] != GATE_HASH or receipt['remaining_transport_issues']: raise Failure('transport gate binding')
    checks=('all_144_native_images_per_pdf_exact','all_309_page_rasters_pixel_identical_at_200dpi','all_image_noncompression_dictionaries_equal','all_page_content_font_streams_text_geometry_equal','complete_catalog_and_resource_graph_equal')
    if not all(receipt['validation'].get(key) is True for key in checks): raise Failure('transport validation incomplete')
    for key in ('lossless_verification','page_tree_normalization_audit','visual_spotcheck'):
        item=receipt['validation'][key]; check(TRANSPORT.parent/item['path'],item)
    for item in receipt['selected_pdfs']:
        check(TRANSPORT.parent/item['path'],item); check(TRANSPORT.parent/item['assembly_replay']['path'],item['assembly_replay'])
    serialized = json.dumps(receipt, sort_keys=True).upper()
    if any(v[3] not in serialized for v in EXPECTED.values()): raise Failure('transport acceptance missing reader hash')
    mapping = []
    for lang, (stem, pages, size, hash_) in EXPECTED.items():
        src = TRANSPORT / 'pdf' / f'D019_{stem}_LOSSLESS_TRANSPORT.pdf'
        identity = check(src, {'bytes': size, 'sha256': hash_})
        with fitz.open(src) as pdf:
            if len(pdf) != pages: raise Failure('transport page count')
        dst = WORK / 'readers' / f'D019_{lang}.pdf'; copy(src, dst)
        mapping.append({'language': lang, 'reader': dst.relative_to(SOURCE).as_posix(), 'pages': pages, **identity})
    copy(receipt_path, WORK / 'transport_evidence' / receipt_path.name)
    for item in receipt['reproduction_files']+receipt['legacy_verification_dependencies']:
        check(TRANSPORT.parent/item['path'],item)
        copy(TRANSPORT.parent/item['path'],WORK/'transport_recipe'/item['path'])
    method=read(TRANSPORT/'METHOD_RECEIPT.json')
    for item in method['encoded_streams']:
        check(TRANSPORT/item['path'],item)
        copy(TRANSPORT/item['path'],WORK/'transport_recipe/method03_zopfli'/item['path'])
    for p in sorted(TRANSPORT.glob('*.json')):
        if p.name not in ('PROGRESS.json', 'VERIFICATION_PROGRESS.json'):
            copy(p, WORK / 'transport_evidence' / p.name)
    result = {'status': 'PASS', 'receipt': sha(receipt_path), 'receipt_filename': receipt_path.name,
      'readers': mapping, 'canonical_bytes_preserved': True, 'acceptance_scope': 'lossless transport derivative only'}
    write(AUDIT / 'D019_TRANSPORT_ADMISSION.json', result); copy(AUDIT / 'D019_TRANSPORT_ADMISSION.json', RECEIPTS / 'D019_TRANSPORT_ADMISSION.json')
    for lang in ('EN', 'FR'):
        p = SOURCE / f'Deligne_{lang}.tex'; s = p.read_text(encoding='utf-8')
        if 'D019_PUBLIC_SAFE' in s: raise Failure('master already patched')
        if s.count('D001--D018;') != 1 or s.count('D019--D020;') != 1: raise Failure('coverage anchors')
        s = s.replace('D001--D018;', 'D001--D019;', 1).replace('D019--D020;', 'D020;', 1)
        s = s.replace(r'\@pnumwidth{2.2em}',r'\@pnumwidth{2.8em}').replace(r'\@tocrmarg{3.2em}',r'\@tocrmarg{3.8em}')
        if lang=='FR':s=s.replace(r'\begingroup\small\sloppy',r'\begingroup\fontsize{9.5}{10.8}\selectfont\sloppy')
        lines = s.splitlines(); anchors = [i for i, x in enumerate(lines) if 'd021}' in x]
        if len(anchors) != 1 or 'D018_PUBLIC_SAFE' not in lines[anchors[0]-1]: raise Failure('D019 numerical insertion anchors')
        title = 'Hodge Theory III' if lang == 'EN' else 'Théorie de Hodge III'
        lines.insert(anchors[0], r'\includepdf[pages=-,pagecommand={},addtotoc={1,section,1,{D019 - ' + title + r'},d019}]{works/D019_PUBLIC_SAFE/readers/D019_' + lang + '.pdf}')
        write_text(p, '\n'.join(lines) + '\n')
    cursor('SOURCE_READY', 'Build cumulative EN and FR PDFs in clean replicas under Global\\InterlanguageTeXSlotV1; compute actual frontmatter/page topology.', transport_admission=sha(AUDIT / 'D019_TRANSPORT_ADMISSION.json'))
    return result

class Mutex:
    def __enter__(self):
        k = ctypes.windll.kernel32
        k.CreateMutexW.argtypes = [ctypes.c_void_p, ctypes.c_bool, ctypes.c_wchar_p]; k.CreateMutexW.restype = ctypes.c_void_p
        k.WaitForSingleObject.argtypes = [ctypes.c_void_p, ctypes.c_uint32]; k.WaitForSingleObject.restype = ctypes.c_uint32
        self.handle = k.CreateMutexW(None, False, 'Global\\InterlanguageTeXSlotV1')
        if not self.handle: raise Failure('CreateMutex failed')
        t = time.monotonic(); result = k.WaitForSingleObject(self.handle, 600000); self.wait_ms = round((time.monotonic()-t)*1000)
        if result not in (0, 0x80): k.CloseHandle(ctypes.c_void_p(self.handle)); raise Failure('bounded TeX mutex acquisition failed')
        self.abandoned = result == 0x80
        return self
    def __exit__(self, *args):
        k = ctypes.windll.kernel32; k.ReleaseMutex(ctypes.c_void_p(self.handle)); k.CloseHandle(ctypes.c_void_p(self.handle))

def tex_pass(engine, slot, name, output):
    """Launch suspended, assign a private kill-on-close job, then resume.

    All descendants remain captured. Timeout/failure terminates only this job;
    successful return requires an empty captured job before the mutex releases.
    """
    from ctypes import wintypes as w
    class Basic(ctypes.Structure):
        _fields_ = [('ProcessUserTimeLimit', ctypes.c_int64), ('JobUserTimeLimit', ctypes.c_int64), ('LimitFlags', w.DWORD), ('MinimumWorkingSetSize', ctypes.c_size_t), ('MaximumWorkingSetSize', ctypes.c_size_t), ('ActiveProcessLimit', w.DWORD), ('Affinity', ctypes.c_size_t), ('PriorityClass', w.DWORD), ('SchedulingClass', w.DWORD)]
    class IO(ctypes.Structure): _fields_ = [(n, ctypes.c_uint64) for n in ('ReadOperationCount','WriteOperationCount','OtherOperationCount','ReadTransferCount','WriteTransferCount','OtherTransferCount')]
    class Extended(ctypes.Structure): _fields_ = [('BasicLimitInformation', Basic), ('IoInfo', IO), ('ProcessMemoryLimit', ctypes.c_size_t), ('JobMemoryLimit', ctypes.c_size_t), ('PeakProcessMemoryUsed', ctypes.c_size_t), ('PeakJobMemoryUsed', ctypes.c_size_t)]
    class Accounting(ctypes.Structure): _fields_ = [(n, ctypes.c_int64) for n in ('TotalUserTime','TotalKernelTime','ThisPeriodTotalUserTime','ThisPeriodTotalKernelTime')] + [(n,w.DWORD) for n in ('TotalPageFaultCount','TotalProcesses','ActiveProcesses','TotalTerminatedProcesses')]
    k = ctypes.windll.kernel32; ntdll = ctypes.windll.ntdll
    k.CreateJobObjectW.argtypes=[ctypes.c_void_p,ctypes.c_wchar_p]; k.CreateJobObjectW.restype=ctypes.c_void_p
    k.SetInformationJobObject.argtypes=[ctypes.c_void_p,ctypes.c_int,ctypes.c_void_p,w.DWORD]
    k.AssignProcessToJobObject.argtypes=[ctypes.c_void_p,ctypes.c_void_p]
    k.QueryInformationJobObject.argtypes=[ctypes.c_void_p,ctypes.c_int,ctypes.c_void_p,w.DWORD,ctypes.c_void_p]
    k.TerminateJobObject.argtypes=[ctypes.c_void_p,w.UINT]
    ntdll.NtResumeProcess.argtypes=[ctypes.c_void_p]
    job=k.CreateJobObjectW(None,None)
    if not job: raise Failure('CreateJobObject failed')
    limits=Extended(); limits.BasicLimitInformation.LimitFlags=0x2000
    if not k.SetInformationJobObject(job,9,ctypes.byref(limits),ctypes.sizeof(limits)): raise Failure('set captured tree policy failed')
    proc=None; started=time.monotonic()
    env=os.environ.copy(); env.update(SOURCE_DATE_EPOCH='946684800', FORCE_SOURCE_DATE='1', TZ='UTC')
    try:
        proc=subprocess.Popen([engine,'-no-shell-escape','-interaction=nonstopmode','-halt-on-error','-file-line-error',name],cwd=slot,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,creationflags=0x00000004|0x08000000)
        if not k.AssignProcessToJobObject(job,ctypes.c_void_p(int(proc._handle))): raise Failure('captured tree assignment failed')
        if ntdll.NtResumeProcess(ctypes.c_void_p(int(proc._handle))) != 0: raise Failure('captured process resume failed')
        raw,_=proc.communicate(timeout=900)
        deadline=time.monotonic()+30
        while True:
            ac=Accounting()
            if not k.QueryInformationJobObject(job,1,ctypes.byref(ac),ctypes.sizeof(ac),None): raise Failure('captured tree observation failure')
            if ac.ActiveProcesses == 0: break
            if time.monotonic()>deadline: raise Failure('captured descendants did not terminate')
            time.sleep(.1)
        out=raw.decode('utf-8','replace'); write_text(output,out)
        anomalies={k_: len(re.findall(p,out,re.MULTILINE|re.IGNORECASE)) for k_,p in {'errors':r'^!','missing_glyphs':'Missing character:','overfull':'Overfull ','fatal':'fatal error','emergency':'emergency stop'}.items()}
        if proc.returncode or any(anomalies.values()): raise Failure('TeX deterministic QA failure: '+json.dumps(anomalies))
        return {'status':'PASS','return_code':proc.returncode,'anomalies':anomalies,'stdout':sha(output),'captured_processes':ac.TotalProcesses,'active_descendants_at_return':ac.ActiveProcesses,'elapsed_seconds':round(time.monotonic()-started,3)}
    finally:
        k.TerminateJobObject(job,1)
        if proc is not None:
            if proc.poll() is None: proc.kill()
            proc.wait(timeout=30)
        k.CloseHandle(ctypes.c_void_p(job))

def includes(root, lang, pdf=None):
    names = re.findall(r'\\includepdf\[.*?\]\{([^}]+)\}', (root / f'Deligne_{lang}.tex').read_text(encoding='utf-8'))
    first=3
    if pdf:
        with fitz.open(pdf) as d:
            matches=[r for r in d.get_toc() if re.search(r'\bD001\b',r[1])]
            if len(matches)!=1: raise Failure('first work bookmark topology')
            first=matches[0][2]
    out=[]
    for name in names:
        with fitz.open(root/name) as d: pages=len(d)
        work=re.search(r'D\d{3}',name).group()
        out.append({'work':work,'path':name,'first':first,'last':first+pages-1,'pages':pages}); first+=pages
    if [r['work'] for r in out] != sorted({r['work'] for r in out}): raise Failure('not unique numerical order')
    return out

def build():
    if read(AUDIT/'D019_TRANSPORT_ADMISSION.json')['status']!='PASS': raise Failure('transport not admitted')
    if (AUDIT/'COLD_REPRODUCIBILITY_RECEIPT.json').exists(): raise Failure('build already complete; use qa')
    engine=shutil.which('xelatex')
    if not engine: raise Failure('xelatex unavailable')
    receipt={'status':'RUNNING','name':'Global\\InterlanguageTeXSlotV1','timeout_ms':600000,'passes':0,'owner_pid':os.getpid(),'captured_tree_policy':'private kill-on-close job assigned before resume; no shell escape; zero active descendants at return'}
    write(AUDIT/'TEX_MUTEX_RECEIPT.json',receipt)
    results={'status':'RUNNING','engine':{'name':'xelatex.exe',**sha(engine)},'languages':{}}
    try:
        with Mutex() as mutex:
            receipt.update(acquired_utc=now(),abandoned_recovery=mutex.abandoned,wait_ms=mutex.wait_ms); write(AUDIT/'TEX_MUTEX_RECEIPT.json',receipt)
            for lang in ('EN','FR'):
                deps=[f'Deligne_{lang}.tex']+[r['path'] for r in includes(SOURCE,lang)]
                records=[]
                for replica in ('compile_A','compile_B','cold_replay'):
                    slot=safe(BUILD/'tex_slot'/lang)
                    if slot.exists(): raise Failure('existing TeX slot: resume evidence, do not duplicate')
                    slot.mkdir(parents=True)
                    for dep in deps: copy(SOURCE/dep,slot/dep)
                    passes=[]
                    for i in (1,2):
                        passes.append(tex_pass(engine,slot,f'Deligne_{lang}.tex',AUDIT/'tex_logs'/f'{replica}_{lang}_{i}.txt'))
                        receipt['passes']+=1; write(AUDIT/'TEX_MUTEX_RECEIPT.json',receipt)
                    pdf=slot/f'Deligne_{lang}.pdf'
                    topology=includes(SOURCE,lang,pdf)
                    with fitz.open(pdf) as d: total=len(d)
                    if total != topology[-1]['last']: raise Failure('compiled total differs from include topology')
                    dest=BUILD/'cold_replay'/replica/lang/f'Deligne_{lang}.pdf'; copy(pdf,dest)
                    records.append({'replica':replica,'pdf':sha(pdf),'pages':total,'frontmatter_pages':topology[0]['first']-1,'passes':passes})
                    # Only our exact validated scratch directory is removed.
                    if slot.parent != (BUILD/'tex_slot').resolve() or slot.name not in ('EN','FR'): raise Failure('scratch cleanup boundary')
                    shutil.rmtree(slot)
                if len({r['pdf']['sha256'] for r in records})!=1: raise Failure('clean TeX replay hash mismatch')
                shutil.copy2(BUILD/'cold_replay/compile_A'/lang/f'Deligne_{lang}.pdf',safe(SOURCE/f'Deligne_{lang}.pdf'))
                results['languages'][lang]={'replicas':records,'byte_identical':True,'pages':records[0]['pages']}
            receipt.update(status='PASS',captured_trees_ended=True,release_utc=now()); write(AUDIT/'TEX_MUTEX_RECEIPT.json',receipt)
    except Exception as e:
        receipt.update(status='FAIL',failure=str(e),released_utc=now()); write(AUDIT/'TEX_MUTEX_RECEIPT.json',receipt); raise
    results.update(status='PASS',tex_mutex=sha(AUDIT/'TEX_MUTEX_RECEIPT.json'),passes_per_replica=2,clean_replicas=3)
    write(AUDIT/'COLD_REPRODUCIBILITY_RECEIPT.json',results)
    cursor('TEX_REPRODUCIBILITY_PASS','Run every-page source/predecessor identity QA; render changed frontmatter and D019 insertion boundaries; inspect visual contact sheets.',cold_reproducibility=sha(AUDIT/'COLD_REPRODUCIBILITY_RECEIPT.json'))
    return results

def signature(page):
    pix=page.get_pixmap(matrix=fitz.Matrix(1,1),alpha=False,colorspace=fitz.csRGB)
    text=re.sub(r'\s+',' ',page.get_text()).strip()
    return {'raster_sha256':hashlib.sha256(pix.samples).hexdigest().upper(),'text_sha256':hashlib.sha256(text.encode()).hexdigest().upper(),'text_characters':len(text),'width':pix.width,'height':pix.height}

def qa():
    if read(AUDIT/'COLD_REPRODUCIBILITY_RECEIPT.json')['status']!='PASS': raise Failure('build gate')
    details=[]; topology=[]; result={'status':'RUNNING','languages':{}}
    visual=safe(AUDIT/'visual'); visual.mkdir(parents=True,exist_ok=True)
    for lang in ('EN','FR'):
        current=SOURCE/f'Deligne_{lang}.pdf'; before=PRED/'release'/f'Deligne_{lang}.pdf'
        new=includes(SOURCE,lang,current); old=includes(PRED/'source_tree',lang,before)
        old_lookup={r['work']:r for r in old}; addition=next(r for r in new if r['work']=='D019')
        if addition['pages']!=EXPECTED[lang][1]: raise Failure('D019 include pages')
        if set(r['work'] for r in new)-set(old_lookup)!={'D019'}: raise Failure('work inventory delta')
        retained=inserted=exact=0
        with fitz.open(current) as d,fitz.open(before) as b,fitz.open(SOURCE/addition['path']) as standalone:
            # Frontmatter may grow but is never inferred from expected total.
            front=new[0]['first']-1
            if signature(d[0])!=signature(b[0]): raise Failure('cover regression')
            for i in range(front):
                sig=signature(d[i]); details.append({'language':lang,'page':i+1,'work':'FRONTMATTER','reference_page':i+1,'disposition':'COVER_EXACT' if i==0 else 'FRONTMATTER_UPDATED',**sig})
                d[i].get_pixmap(matrix=fitz.Matrix(2,2),alpha=False).save(visual/f'{lang}-front-{i+1:03}.png')
            if 'D019' not in ''.join(d[i].get_text() for i in range(front)): raise Failure('D019 missing from contents')
            for part in new:
                topology.append({'language':lang,**part,'input_sha256':sha(SOURCE/part['path'])['sha256']})
                for offset in range(part['pages']):
                    num=part['first']+offset; page=d[num-1]; sig=signature(page)
                    if not sig['text_characters']: raise Failure('empty reader page')
                    if part['work']=='D019':
                        ref=standalone[offset]; ref_num=offset+1; rs=signature(ref)
                        if sig['text_sha256']!=rs['text_sha256']: raise Failure(f'D019 text regression {lang} {num}')
                        # Exact geometry and math/image placement are checked; pdfpages can round scaling by <0.01pt.
                        if abs(page.rect.width-ref.rect.width)>.1 or abs(page.rect.height-ref.rect.height)>.1: raise Failure('inserted page size regression')
                        inserted+=1; exact+=int(sig==rs); disposition='D019_INSERTED_TEXT_EXACT'
                        if offset in (0,1,2,part['pages']//2,part['pages']-2,part['pages']-1):
                            page.get_pixmap(matrix=fitz.Matrix(2,2),alpha=False).save(visual/f'{lang}-D019-{offset+1:03}.png')
                    else:
                        ref_num=old_lookup[part['work']]['first']+offset
                        if sig!=signature(b[ref_num-1]): raise Failure(f'predecessor page regression {lang} {part["work"]} {num}')
                        retained+=1; disposition='PREDECESSOR_RASTER_AND_TEXT_EXACT'
                    details.append({'language':lang,'page':num,'work':part['work'],'reference_page':ref_num,'disposition':disposition,**sig})
                if part['work'] in ('D018','D021'):
                    index=part['last']-1 if part['work']=='D018' else part['first']-1
                    d[index].get_pixmap(matrix=fitz.Matrix(2,2),alpha=False).save(visual/f'{lang}-{part["work"]}-boundary.png')
            marks=[r for r in d.get_toc() if 'D019' in r[1]]
            if len(marks)!=1 or marks[0][2]!=addition['first']: raise Failure('D019 bookmark regression')
            result['languages'][lang]={'pages':len(d),'frontmatter_pages':front,'d019':addition,'retained_work_pages_raster_and_text_exact':retained,'inserted_text_exact':inserted,'inserted_raster_exact':exact,'bookmark':marks[0],'pdf':sha(current)}
    result.update(status='PASS',page_identity_map=tsv(AUDIT/'PAGE_IDENTITY_MAP.tsv',details),include_topology=tsv(AUDIT/'INCLUDE_TOPOLOGY.tsv',topology),every_cumulative_page_rendered_at_72dpi=True,source_inputs_modified=False)
    write(AUDIT/'CUMULATIVE_PAGE_QA.json',result)
    cursor('PAGE_QA_PASS_VISUAL_INSPECTION_NEXT','Inspect rendered current frontmatter, D019 representative pages and boundaries; then write visual inspection receipt and package.',page_qa=sha(AUDIT/'CUMULATIVE_PAGE_QA.json'))
    return result

def nonregression():
    base=rows(PRED/'source_tree'); changed=[]; exact=0
    for row in base:
        actual=sha(SOURCE/row['path'])
        if actual['sha256']!=row['sha256']:
            if row['path'] not in MUTABLE: raise Failure('unexpected predecessor source change: '+row['path'])
            changed.append({'path':row['path'],'predecessor':{k:row[k] for k in ('bytes','sha256')},'current':actual})
        else: exact+=1
    result={'status':'PASS','all_predecessor_paths_retained':True,'byte_identical_predecessor_files':exact,'allowed_changed_files':changed,'source_master_writes':False}
    write(AUDIT/'SOURCE_NONREGRESSION.json',result); return result

def archive(root,dest):
    dest=safe(dest); dest.parent.mkdir(parents=True,exist_ok=True)
    if dest.exists(): raise Failure('archive exists, do not duplicate')
    members=rows(root)
    with zipfile.ZipFile(dest,'w',allowZip64=True) as z:
        for r in members:
            info=zipfile.ZipInfo(r['path'],(2000,1,1,0,0,0)); info.create_system=3; info.external_attr=0o100644<<16; info.compress_type=zipfile.ZIP_DEFLATED; info._compresslevel=6
            with (root/r['path']).open('rb') as a,z.open(info,'w',force_zip64=True) as b: shutil.copyfileobj(a,b,1024*1024)
    with zipfile.ZipFile(dest) as z:
        if z.namelist()!=[r['path'] for r in members]: raise Failure('ZIP member order')
        for r in members:
            h=hashlib.sha256(); size=0
            with z.open(r['path']) as f:
                for b in iter(lambda:f.read(1024*1024),b''):h.update(b);size+=len(b)
            if size!=r['bytes'] or h.hexdigest().upper()!=r['sha256']:raise Failure('ZIP replay')
    return {'status':'PASS','members':len(members),'expanded_bytes':sum(r['bytes'] for r in members),'identity':sha(dest)}

def split(path,dest):
    safe(dest).mkdir(parents=True,exist_ok=True); all_hash=hashlib.sha256(); parts=[]; offset=0
    with path.open('rb') as f:
        while True:
            b=f.read(90000000)
            if not b:break
            name=f'{path.name}.part{len(parts)+1:03d}'; p=dest/name
            if p.exists(): raise Failure('transfer part exists')
            p.write_bytes(b); all_hash.update(b); parts.append({'filename':name,'offset':offset,**sha(p)});offset+=len(b)
    identity=sha(path)
    if all_hash.hexdigest().upper()!=identity['sha256'] or offset!=identity['bytes']:raise Failure('split roundtrip')
    return {'status':'PASS','original':{'filename':path.name,**identity},'parts':parts,'reassemble':'Concatenate part files in their listed order, then verify the whole SHA-256 before opening the ZIP.'}

def package():
    pageqa=read(AUDIT/'CUMULATIVE_PAGE_QA.json'); visual=read(AUDIT/'VISUAL_INSPECTION.json')
    if pageqa['status']!='PASS' or visual['status']!='PASS':raise Failure('QA incomplete')
    for name in ('D019_INSERTED_GLYPH_IMAGE_GEOMETRY.json','PUBLIC_SURFACE_PRIVACY.json','FINAL_CONTENTS_CONVERGENCE.json'):
        if read(AUDIT/name)['status']!='PASS':raise Failure('final '+name+' gate incomplete')
    portable=BUILD/'portable_transport_replay/PORTABLE_ASSEMBLY_REPLAY.json'
    if read(portable)['status']!='PASS':raise Failure('portable transport replay incomplete')
    copy(portable,AUDIT/'PORTABLE_ASSEMBLY_REPLAY.json')
    readme=SOURCE/'README.md'; text=readme.read_text(encoding='utf-8')
    text=text.replace('Included complete works, in numerical order: D001-D018,','Included complete works, in numerical order: D001-D019,',1)
    text=text.replace('Explicit gaps through the current sparse sequence: D019-D020,','Explicit gaps through the current sparse sequence: D020,',1)
    pages={lang:pageqa['languages'][lang]['pages'] for lang in ('EN','FR')}
    text=text.replace('This release contains 885 English and 899 French pages.',f'This release contains {pages["EN"]} English and {pages["FR"]} French pages.',1)
    text=text.replace('Run XeLaTeX twice on `Deligne_EN.tex` or `Deligne_FR.tex` from this directory.','Run XeLaTeX twice on `Deligne_EN.tex` and three times on `Deligne_FR.tex` from this directory; the third French pass verifies settled contents numbers.',1)
    text=text.replace('and remains between D015 and D018.','and remains between D015 and D017.',1)
    positions={lang:next(r for r in includes(SOURCE,lang,SOURCE/f'Deligne_{lang}.pdf') if r['work']=='D031') for lang in ('EN','FR')}
    text=text.replace('D031 occupies English pages642-684 and French pages656-698.',f'D031 occupies English pages {positions["EN"]["first"]}-{positions["EN"]["last"]} and French pages {positions["FR"]["first"]}-{positions["FR"]["last"]}.',1)
    text=text.replace('Current cold-build, include-map, all-page identity, and changed-page visual receipts are under `release_receipts/D031_GAPFILL/`.','Current cold-build, include-map, all-page identity, and changed-page visual receipts are under `release_receipts/D019_FORWARD_INTEGRATION/`. Earlier D031 and D017 release receipts and their release-specific narratives are retained as historical evidence.',1)
    text=text.replace('## D031 gap insertion','## D031 gap insertion (historical release narrative)',1).replace('## D017 gap insertion','## D017 gap insertion (historical release narrative)',1)
    text=text.replace('then run `xelatex -interaction=nonstopmode -halt-on-error` twice for each entrypoint, sequentially.','then run `xelatex -no-shell-escape -interaction=nonstopmode -halt-on-error` twice for English and three times for French, sequentially. On the originating Windows workspace, acquire `Global\\InterlanguageTeXSlotV1` with a bounded timeout before any TeX process, hold it continuously through the full captured process tree and all passes/log checks, and release it in a finally path after the tree ends.',1)
    text+='\n## D019 gap insertion\n\nD019, *Hodge Theory III* / *Théorie de Hodge III*, is inserted after D018 and before D021. '
    text+=f'The current cumulative books contain {pages["EN"]} English and {pages["FR"]} French pages. '
    text+='The independently accepted canonical editions contain 155 English and 154 French reader pages aligned to 73 article pages; the 74-page authority includes an excluded cover. '
    text+='Exact canonical PDF/TeX/data/assets, the complete reproducible source packet with its original authority, and canonical acceptance evidence are preserved under `works/D019_PUBLIC_SAFE`. '
    text+='The separately admitted lossless transport PDFs used for cumulative inclusion preserve all text and image samples. They do not replace canonical bytes. '
    text+='All inherited source witnesses remain byte-identical and inherited evidence remains ZERO_ACCEPTED. Earlier release-specific narrative remains historical.\n'
    text+='\n## Nonincluded work status snapshot (2026-09-04)\n\nThis parent-supplied intake snapshot does not promote a returned browser packet to normalized acceptance. D032 S20 and D037 S05-GA01 are complete return claims awaiting independent deterministic gates, not active partial claims. D048 S14 is a returned facsimile-witness packet at 84/86 physical and 83/85 article pages; next P15 covers physical 85-86 / printed 88-89. It is not normalized acceptance. D020 remains 30/36 with P06 next; D044 remains 54/174 with P10 next. These works are not inserted by this D019 release.\n'
    write_text(readme,text)
    for name in ('CUMULATIVE_PAGE_QA.json','COLD_REPRODUCIBILITY_RECEIPT.json','TEX_MUTEX_RECEIPT.json','FR_FINAL_TEX_MUTEX_RECEIPT.json','VISUAL_INSPECTION.json','D019_INSERTED_GLYPH_IMAGE_GEOMETRY.json','PORTABLE_ASSEMBLY_REPLAY.json','FINAL_CONTENTS_CONVERGENCE.json'):
        copy(AUDIT/name,RECEIPTS/name)
    for script in sorted((TASK/'scripts').glob('*.py')):copy(script,RECEIPTS/'build_scripts'/script.name)
    subprocess.run([sys.executable,str(TASK/'scripts/check_public_surface.py')],check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    copy(AUDIT/'PUBLIC_SURFACE_PRIVACY.json',RECEIPTS/'PUBLIC_SURFACE_PRIVACY.json')
    nonregression()
    srcrows=[r for r in rows(SOURCE) if r['path']!='PUBLIC_SOURCE_MANIFEST.tsv']
    source_manifest=tsv(SOURCE/'PUBLIC_SOURCE_MANIFEST.tsv',[{k:r[k] for k in ('path','bytes','sha256')} for r in srcrows])
    # Complete predecessor provenance stays byte-for-byte intact as an inherited carrier.
    prov=safe(BUILD/'provenance_tree');prov.mkdir(parents=True,exist_ok=True)
    copy(PRED/'release/DELIGNE_PROVENANCE_AUDIT_D017_GAPFILL.zip',prov/'inherited/DELIGNE_PROVENANCE_AUDIT_D017_GAPFILL.zip')
    copy(WORK/'canonical_build/output/source_packet/D019_CANONICAL_SOURCE_PACKET.zip',prov/'D019/D019_CANONICAL_SOURCE_PACKET.zip')
    for r in rows(WORK/'receipts'):copy(WORK/'receipts'/r['path'],prov/'D019/receipts'/r['path'])
    for r in rows(WORK/'transport_evidence'):copy(WORK/'transport_evidence'/r['path'],prov/'D019/transport_evidence'/r['path'])
    for p in AUDIT.glob('*.json'):copy(p,prov/'integration_audits'/p.name)
    for p in AUDIT.glob('*.tsv'):copy(p,prov/'integration_audits'/p.name)
    subprocess.run([sys.executable,str(TASK/'scripts/check_public_surface.py'),'--provenance'],check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    copy(AUDIT/'PUBLIC_PROVENANCE_PRIVACY.json',prov/'PUBLIC_PROVENANCE_PRIVACY.json')
    tsv(prov/'PROVENANCE_MANIFEST.tsv',[{k:r[k] for k in ('path','bytes','sha256')} for r in rows(prov)])
    release=safe(BUILD/'release');release.mkdir(parents=True,exist_ok=True)
    for name in ('Deligne_EN.pdf','Deligne_FR.pdf','Deligne_EN.tex','Deligne_FR.tex'):copy(SOURCE/name,release/name)
    archives={}
    for root,name in ((SOURCE,'Deligne_Source.zip'),(prov,'DELIGNE_PROVENANCE_AUDIT_D019_GAPFILL.zip')):
        archives[name]=archive(root,release/name)
        twin=BUILD/'zip_verification_twin'/name; repeat=archive(root,twin)
        if archives[name]['identity']!=repeat['identity']:raise Failure('archive deterministic twin mismatch')
        archives[name]['byte_identical_independent_zip_twin']=repeat['identity']
        # The verified twin is only this task's temporary duplicate; the release archive remains.
        safe(twin).unlink()
    identities={p.name:sha(p) for p in sorted(release.iterdir()) if p.is_file()}
    if len(identities)!=6:raise Failure('six-file inventory mismatch')
    tsv(BUILD/'SIX_FILE_RELEASE_MANIFEST.tsv',[{'filename':name,**identities[name]} for name in sorted(identities)])
    transfer={name:split(release/name,BUILD/'github_transfer'/name) for name in archives if identities[name]['bytes']>=2147483648}
    oversized=[r for r in rows(SOURCE) if r['bytes']>=100000000]
    route={'status':'READY_FOR_PARENT_RELEASE','reader_pdf_route':'Existing-repository GitHub Release assets for complete cumulative PDFs; do not add oversized PDFs to ordinary Git blobs.',
      'archive_route':'Full source/provenance ZIPs are exact GitHub Release assets when each is below 2 GiB. Only archives reaching that threshold receive exact 90,000,000-byte maximum binary parts; concatenate in order and verify SHA-256. No redundant parts are made for smaller archives.',
      'release_asset_files':{n:i for n,i in identities.items() if n.endswith('.pdf') or (n.endswith('.zip') and i['bytes']<2147483648)},'archive_splits':transfer,
      'source_tree_files_requiring_archive_or_release_asset_transport':oversized,'no_image_degradation':True,'no_source_witness_omission':True,'publication_operations':'NONE'}
    write(BUILD/'TRANSPORT_ROUTE.json',route)
    result={'schema':'deligne-d019-gapfill-build-release-v1','status':'PASS','predecessor_record_id':'22236378','concept_doi':'10.5281/zenodo.20410853',
      'included_complete_works':'D001-D019; D021-D023; D025-D031; D034-D036; D038-D040; D043','explicit_gaps':'D020; D024; D032-D033; D037; D041-D042',
      'insertion':'D019 after D018 and before D021','release_files':identities,'pages':pages,'source_manifest':source_manifest,'archives':archives,
      'page_qa':sha(AUDIT/'CUMULATIVE_PAGE_QA.json'),'visual_inspection':sha(AUDIT/'VISUAL_INSPECTION.json'),'tex_reproducibility':sha(AUDIT/'COLD_REPRODUCIBILITY_RECEIPT.json'),
      'inserted_glyph_image_geometry':sha(AUDIT/'D019_INSERTED_GLYPH_IMAGE_GEOMETRY.json'),'public_provenance_privacy':sha(AUDIT/'PUBLIC_PROVENANCE_PRIVACY.json'),'public_source_privacy':sha(AUDIT/'PUBLIC_SURFACE_PRIVACY.json'),
      'contents_convergence':sha(AUDIT/'FINAL_CONTENTS_CONVERGENCE.json'),'portable_transport_replay':sha(AUDIT/'PORTABLE_ASSEMBLY_REPLAY.json'),
      'source_nonregression':sha(AUDIT/'SOURCE_NONREGRESSION.json'),'transport_route':sha(BUILD/'TRANSPORT_ROUTE.json'),'source_inputs_modified':False,'git_operations':'NONE','publication_operations':'NONE'}
    write(BUILD/'BUILD_RELEASE_RECEIPT.json',result)
    cursor('LOCAL_RELEASE_BUILD_PASS','Parent independently adopts exact six-file release and any required transport parts, performs authorized publication and anonymous public-byte verification.',build_receipt=sha(BUILD/'BUILD_RELEASE_RECEIPT.json'))
    return result

def main():
    p=argparse.ArgumentParser();p.add_argument('stage',choices=['prepare','admit','build','qa','package']);p.add_argument('--transport-receipt');a=p.parse_args()
    try:
        result={'prepare':prepare,'admit':lambda:admit(a.transport_receipt),'build':build,'qa':qa,'package':package}[a.stage]()
        print(json.dumps(result,ensure_ascii=False,indent=2))
    except Exception as e:
        cursor('OPERATION_FAILED', 'Resume exact failed stage from retained inputs and artifacts; no duplicate workers or publication.',failed_stage=a.stage,failure=str(e)); raise

if __name__=='__main__': main()
