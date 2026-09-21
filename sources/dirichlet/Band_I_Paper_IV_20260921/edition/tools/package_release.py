#!/usr/bin/env python3
"""Create and independently reopen the deterministic four-file S01 release.
External metadata avoids recursive ZIP/self-hash claims. Requires completed QA.
"""
from __future__ import annotations
from pathlib import Path
import csv,hashlib,importlib.util,json,re,shutil,stat,tempfile,zipfile
R=Path(__file__).resolve().parents[1]
OUT=R.parent
ZIPNAME='DIRICHLET_P04_S01_CUMULATIVE_FULL_STATE.zip'

def sha(p:Path)->str:
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    return h.hexdigest().upper()

def meta(name:str)->tuple[str,str,str,str]:
    p=re.search(r'(?:^|/)p(0\d{2})(?:_|\.)',name)
    pages=str(int(p[1])) if p else '65-74'
    if name.startswith('input/'):
        base=Path(name).name
        if base.startswith('10_'):return ('CONTROLLING_AUTHORITY_PDF','RAW_UNCHANGED_AUTHORITY','63-98','Original attached input package member; 36-leaf controlling projection')
        if base.startswith('11_'):return ('FULL_VOLUME_PROVENANCE_AUTHORITY','RAW_UNCHANGED; OUTSIDE_SCOPE_NOT_INGESTED','63-98 (Paper IV subset)','Original attached input package member; full-volume provenance PDF')
        if base.startswith('12_'):return ('ORIGINAL_R27_ZIP','UNVERIFIED_PRIOR_WORK_PRESERVED','65-74 (witnesses; broader legacy label63-74)','Original input ZIP member preserved byte-for-byte; corrected derivatives accepted separately')
        if base.startswith('13_'):return ('ORIGINAL_R28_ZIP','UNVERIFIED_PRIOR_WORK_NOT_PROCESSED','75-80','Original input ZIP member; CRC/hash validation only in Prompt01')
        return ('GOVERNING_INPUT_OR_REGISTERED_EVIDENCE','ORIGINAL_UNCHANGED_INPUT','63-98','Original attached input package member; not a current acceptance claim')
    if name.startswith('inherited/'):
        return ('UNPACKED_R27_EVIDENCE','PRESERVED_ORIGINAL_NOT_ACCEPTED_EDITION','65-74 (Paper IV portion only)','Byte-identical member of original R27 ZIP; earlier-paper cumulative PDFs preserved only')
    if name.startswith('prior_evidence/'):
        return ('PRIOR_INPUT_ACCESS_CHECKPOINT_EVIDENCE','HISTORICAL_ZERO_AUTHOR_ACCEPTANCE','NONE_ACCEPTED','Earlier input-access return preserved unpacked; superseded as current state')
    if name.startswith('editions/fr/'):
        return ('DIPLOMATIC_FRENCH_EDITABLE_SOURCE','ACCEPTED_SOURCE_BACKED_S01',pages,'Direct comparison with exact-scope authority; R27 only as untrusted comparator')
    if name.startswith('editions/en/'):
        return ('FAITHFUL_ENGLISH_EDITABLE_SOURCE','ACCEPTED_SOURCE_BACKED_S01',pages,'Complete translation aligned with the source-backed French and mathematical witness')
    if name.startswith('copy_matter/'):
        return ('COPY_MATTER_TEXT_RECORD','VERIFIED_COPY_ONLY_EXCLUDED_FROM_AUTHOR_READERS',pages,'Controlling authority leaves1-2; no author-text acceptance')
    if name.startswith('apparatus/'):
        return ('SEPARATE_EDITABLE_APPARATUS','ACCEPTED_SOURCE_BACKED_S01',pages,'Current source-backed pagewise observations; editorial analysis explicitly separate')
    if name.startswith('readers/'):
        return ('CURRENT_COMPILED_READER','ACCEPTED_BUILD_AND_VISUAL_AUDIT','65-74','Current independent XeLaTeX edition or separate apparatus; two successful runs; all pages viewed')
    if name.startswith('qa/source/'):
        return ('AUTHORITY_PAGE_RENDER_OR_DETAIL','VISUALLY_REVIEWED_SOURCE_WITNESS',pages,'Rendered directly from unchanged controlling attached PDF; no OCR')
    if name.startswith('qa/visual/'):
        return ('CURRENT_READER_RENDER','DIRECT_VISUAL_AUDIT_PASS',pages,'126dpi rendering of final current reader; bound to visual audit receipt')
    if name.startswith('qa/build/repair_history/'):
        return ('SUPERSEDED_BUILD_REPAIR_LOG','HISTORICAL_NOT_CURRENT_BUILD','65-74','Actual earlier build defect retained as repair evidence; final logs supersede')
    if name.startswith('qa/build/'):
        return ('CURRENT_BUILD_EVIDENCE','FINAL_BUILD_PASS','65-74','XeLaTeX output; expected first-pass rerun notices resolved on second pass')
    if name.startswith('qa/'):
        return ('QA_RECEIPT_OR_AUDIT_LEDGER','CURRENT_VERIFIED_EVIDENCE','63-74; registered topology63-98','Current Prompt01 validation, comparison, alignment or visual inspection record')
    if name.startswith('state/'):
        return ('CURRENT_CURSOR_OR_PAGE_STATE','PROMPT_01_COMPLETE_NEXT_CURSOR_2',pages,'Current accepted pagewise evidence; no author acceptance beyondp74')
    if name.startswith('ledgers/'):
        return ('CURRENT_SCOPE_OR_COPY_LEDGER','CURRENT_SOURCE_VERIFIED_STATE','63-98 (only63-74 processed)','Fixed source topology and current exact acceptance/copy dispositions')
    if name=='SOURCE_BACKED_DIFF.tsv':
        return ('CURRENT_SOURCE_BACKED_DIFF','AUTHORITY_BACKED_CORRECTIONS','63-74','44 concrete R27 correction/alignment rows with authority evidence')
    if name.startswith('tools/'):
        return ('REPRODUCIBLE_SOURCE_BUILD_OR_VERIFICATION_TOOL','SUPPORTING_EDITABLE_TOOL','63-74','Current authoring/validation scripts; manual inspection not inferred from automation')
    return ('CURRENT_HANDOFF_DOCUMENTATION','CURRENT_INFORMATION','63-98 (Prompt01 only)','Explains current sources, preservation, audit, scope and non-circular hash contract')

files=sorted(p for p in R.rglob('*') if p.is_file() and '__pycache__' not in p.parts)
assert not any(p.is_symlink() for p in files)
assert not any(p.suffix.lower() in ['.ttf','.otf','.woff','.woff2','.ttc'] for p in files)
assert len(list((R/'input').iterdir()))==21
cursor=json.loads((R/'state/CURSOR.json').read_text())
assert cursor['prompt_completed']==1 and cursor['next_cursor']==2 and cursor['accepted_french_pages']==list(range(65,75))
manifest=[]
for p in files:
    name=p.relative_to(R).as_posix()
    role,acc,pages,prov=meta(name)
    manifest.append({'path':name,'bytes':p.stat().st_size,'sha256':sha(p),'role':role,'acceptance':acc,'printed_page_range':pages,'provenance':prov})
manifest_path=OUT/'MANIFEST.tsv'
with manifest_path.open('w',encoding='utf8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['path','bytes','sha256','role','acceptance','printed_page_range','provenance'],delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(manifest)
shutil.copyfile(R/'SOURCE_BACKED_DIFF.tsv',OUT/'SOURCE_BACKED_DIFF.tsv')

def write_zip(path:Path)->None:
    with zipfile.ZipFile(path,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6,allowZip64=True) as z:
        for p in files:
            info=zipfile.ZipInfo(p.relative_to(R).as_posix(),date_time=(2026,9,21,0,0,0))
            info.create_system=3;info.external_attr=(stat.S_IFREG|0o644)<<16
            info.compress_type=zipfile.ZIP_DEFLATED
            with p.open('rb') as src,z.open(info,'w',force_zip64=True) as dst:
                shutil.copyfileobj(src,dst,1024*1024)
zip_path=OUT/ZIPNAME
write_zip(zip_path)
# A separate second construction proves deterministic archive bytes.
with tempfile.TemporaryDirectory(prefix='dirichlet_determinism_') as td:
    second=Path(td)/ZIPNAME;write_zip(second)
    assert sha(second)==sha(zip_path),'Deterministic ZIP mismatch'
cp={**cursor,'schema':'dirichlet-paper-iv-checkpoint-v2','schema_version':2,
    'prompt_file':'input/20_PROMPT_01_PP063_074.md',
    'input_package':json.loads((R/'qa/INPUT_VALIDATION.json').read_text()),
    'copy_topology_state':'PASS; 63 title,64 blank; both excluded from author readers',
    'build_and_visual':json.loads((R/'qa/BUILD_AND_VISUAL_RECEIPT.json').read_text()),
    'source_comparison':{'units':54,'editable_french_tex_lines':420,'inline_and_display_math_segments':415,'author_footnotes':1,'diff_rows':44,'source_language':'French','source_ambiguities':[]},
    'release_artifacts':{},
    'archive_member_count':len(manifest),
    'archive_members':{r['path']:{'bytes':r['bytes'],'sha256':r['sha256']} for r in manifest},
    'hash_binding_policy':'External checkpoint binds the ZIP, external manifest, external diff, and every archive member. No recursive self-hash. ZIP includes internal state/CURSOR.json and byte-identical diff, not the external checkpoint/manifest.',
    'deterministic_zip':{'second_independent_construction':'BYTE_IDENTICAL_SHA256','fixed_timestamp':'2026-09-21T00:00:00','sorted_normalized_paths':True,'regular_file_mode':'0644'},
    'archive_validation':{'status':'AWAITING_REOPEN_VALIDATION'}}
for key,p in [('cumulative_zip',zip_path),('manifest',manifest_path),('source_backed_diff',OUT/'SOURCE_BACKED_DIFF.tsv')]:
    cp['release_artifacts'][key]={'file':p.name,'bytes':p.stat().st_size,'sha256':sha(p)}
cp_path=OUT/'CHECKPOINT.json'
def save_cp():cp_path.write_text(json.dumps(cp,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
save_cp()
spec=importlib.util.spec_from_file_location('verify_handoff',R/'tools/verify_handoff.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
receipt=mod.verify(zip_path,manifest_path,cp_path,OUT/'SOURCE_BACKED_DIFF.tsv')
cp['archive_validation']=receipt;save_cp()
# Reopen again after writing the final checkpoint: all final sibling bindings pass.
receipt=mod.verify(zip_path,manifest_path,cp_path,OUT/'SOURCE_BACKED_DIFF.tsv')
print(json.dumps({'release_artifacts':cp['release_artifacts'],'checkpoint':{'file':cp_path.name,'bytes':cp_path.stat().st_size,'sha256':sha(cp_path)},'validation':receipt},indent=2))
