#!/usr/bin/env python3
"""Build and independently verify the complete Prompt02 four-file handoff.

The current manifest/checkpoint are external siblings, deliberately avoiding
circular hashes. The internal cursor and cumulative diff are members. Original
S01 bytes are retained either in place or under prior_evidence/S01; no previous
cumulative ZIP is nested. This script does not perform source collation.

Usage: python tools/s02/package_release_s02.py [unpacked_root] [output_directory]
"""
from __future__ import annotations
from pathlib import Path, PurePosixPath
import csv, hashlib, importlib.util, io, json, re, shutil, stat, sys, unicodedata, zipfile
sys.dont_write_bytecode = True

EXPECTED_S01_BYTES = 131808818
EXPECTED_S01_SHA = 'DEE2786989BCE3556912265B110856DB4578181386E322E4FC97CE64D583F162'
ZIP_NAME = 'DIRICHLET_P04_S02_CUMULATIVE_FULL_STATE.zip'
STAMP = (2026, 9, 21, 0, 0, 0)
FIELDS = ['path','bytes','sha256','role','acceptance','printed_page_range','provenance']


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda: f.read(1024*1024), b''):
            h.update(b)
    return h.hexdigest().upper()


def identity(path: Path) -> dict:
    return {'file': path.name, 'bytes': path.stat().st_size, 'sha256': digest(path)}


def dump(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')


def tsv(path: Path, fields: list[str], rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter='\t', lineterminator='\n')
        w.writeheader(); w.writerows(rows)


def safe_name(name: str) -> None:
    assert name and not name.startswith('/') and '\\' not in name and ':' not in name, name
    assert all(s not in ('', '.', '..') for s in name.split('/')), name
    assert unicodedata.normalize('NFC', name) == name and PurePosixPath(name).as_posix() == name, name


def same(path: Path, ident: dict) -> bool:
    return path.is_file() and path.stat().st_size == ident['bytes'] and digest(path) == ident['sha256']


def preservation(root: Path) -> dict:
    prior = json.loads((root/'prior_evidence/S01/CHECKPOINT.json').read_text())
    assert prior['next_cursor'] == 2 and len(prior['archive_members']) == 240
    z = prior['release_artifacts']['cumulative_zip']
    assert z['bytes'] == EXPECTED_S01_BYTES and z['sha256'] == EXPECTED_S01_SHA
    for key, name in [('manifest', 'MANIFEST.tsv'), ('source_backed_diff', 'SOURCE_BACKED_DIFF.tsv')]:
        assert same(root/'prior_evidence/S01'/name, prior['release_artifacts'][key]), name
    rows = []
    for name, ident in sorted(prior['archive_members'].items()):
        if same(root/name, ident):
            location, disposition = name, 'UNCHANGED_AT_ORIGINAL_PATH'
        else:
            location = 'prior_evidence/S01/'+name
            assert same(root/location, ident), ('S01 bytes not preserved', name)
            disposition = 'ORIGINAL_BYTES_PRESERVED_BEFORE_CUMULATIVE_UPDATE'
        rows.append({'s01_member':name, 'preserved_path':location, 'bytes':ident['bytes'],
                     'sha256':ident['sha256'], 'preservation':disposition})
    tsv(root/'qa/s02/S01_MEMBER_PRESERVATION.tsv',
        ['s01_member','preserved_path','bytes','sha256','preservation'], rows)
    return {'original_member_count':len(rows),
            'unchanged_at_original_path':sum(r['s01_member']==r['preserved_path'] for r in rows),
            'original_changed_member_bytes_relocated':sum(r['s01_member']!=r['preserved_path'] for r in rows),
            'all_original_member_bytes_preserved':True, 'previous_cumulative_zip_nested':False,
            'map':'qa/s02/S01_MEMBER_PRESERVATION.tsv'}


def classify(name: str, old: dict, cur: dict) -> tuple[str,str,str,str]:
    page = re.search(r'(?:^|/)p(\d{3})(?:[._/]|$)', name)
    pr = str(int(page[1])) if page else '65-86'
    # Prior evidence, including zero-page access evidence, is never current state.
    if name.startswith('prior_evidence/S01/'):
        source = name.removeprefix('prior_evidence/S01/')
        p = old.get(source, {}).get('printed_page_range', '65-74')
        return ('PRESERVED_ACCEPTED_S01_EVIDENCE','HISTORICAL_S01_NOT_CURRENT_EXTENT',p,
                'Byte-identical accepted S01 original or external handoff metadata; see preservation map')
    if name.startswith('prior_evidence/'):
        prior = old.get(name)
        if prior:
            return tuple(prior[k] for k in FIELDS[3:])
        return ('PRESERVED_PRIOR_EVIDENCE','HISTORICAL_NOT_CURRENT_STATE','N/A',
                'Preserved history only; zero-page access checkpoint is not transcription acceptance')
    if name.startswith('input/'):
        prior = old.get(name)
        assert prior is not None
        return tuple(prior[k] for k in FIELDS[3:])
    if name.startswith('inherited/R28/'):
        mixed = '/cum/' in name or '/checks/cum/' in name
        return ('PRESERVED_UNPACKED_R28_MEMBER','UNVERIFIED_PRIOR_WORK_BYTES_PRESERVED',
                'MIXED_PRIOR_PAPERS_OUTSIDE_READER_SCOPE' if mixed else '75-80',
                'Exact original R28 archive member; hashes and witness replay recorded in qa/s02; only corrected derivative editions accepted')
    if name.startswith('inherited/'):
        prior = old.get(name); assert prior is not None
        return tuple(prior[k] for k in FIELDS[3:])
    if name.startswith('copy_matter/') or name == 'ledgers/COPY_MATTER_LEDGER.tsv':
        prior = old.get(name); assert prior is not None
        return tuple(prior[k] for k in FIELDS[3:])
    if name.startswith('editions/'):
        layer = 'DIPLOMATIC_FRENCH_EDITABLE_SOURCE' if '/fr/' in name else 'FAITHFUL_ENGLISH_EDITABLE_SOURCE'
        if page and int(page[1]) <= 74:
            return (layer,'ACCEPTED_SOURCE_BACKED_S01_UNCHANGED',pr,
                    'Accepted S01 page bytes unchanged; current output exactly text/pixel-regressed against S01')
        origin = 'R28 replay against controlling full-PDF92-97' if page and int(page[1])<=80 else 'Direct transcription/translation from controlling full-PDF98-103'
        if not page: origin = 'Current cumulative main includes exactly printed65-86; independent monolingual reader'
        return (layer,'ACCEPTED_SOURCE_BACKED_S02',pr,origin)
    if name.startswith('apparatus/'):
        return ('SEPARATE_EDITABLE_APPARATUS',
                'ACCEPTED_SOURCE_BACKED_S01_UNCHANGED' if page and int(page[1])<=74 else 'ACCEPTED_SOURCE_BACKED_S02',
                pr,'Pagewise editorial observations kept separate from both author editions; legible print discrepancies not silently repaired')
    if name == 'state/CURSOR.json':
        return ('CURRENT_CUMULATIVE_CURSOR','CURRENT_PROMPT02_COMPLETE_CURSOR3','63-86 processed;87-98 untouched',
                'Exact accepted layer lists65-86; copy63-64 excluded; first untouched87; not whole-paper completion')
    if name.startswith('state/pages/'):
        return ('PAGEWISE_ACCEPTANCE_AND_EVIDENCE',
                'ACCEPTED_SOURCE_BACKED_S01_UNCHANGED' if page and int(page[1])<=74 else 'ACCEPTED_SOURCE_BACKED_S02',
                pr,'Source mapping, editable hashes, aligned units, apparatus, and visual evidence; prior S01 page records retain historical reader bindings')
    if name.startswith('ledgers/'):
        p = '63-98 topology;65-86 accepted' if 'TOPOLOGY' in name else '63-98 project;S02 processed through86'
        return ('CURRENT_CUMULATIVE_LEDGER','CURRENT_SOURCE_BACKED_STATE',p,
                'S01 retained and S02 acceptance appended; copy matter and remaining author pages distinguished')
    if name.startswith('readers/'):
        if name in {v['path'] for v in cur['current_readers'].values()}:
            return ('CURRENT_CUMULATIVE_READER','ACCEPTED_SOURCE_BACKED_S02','65-86',
                    'Built twice with XeLaTeX; all final logs clean; all current pages rendered and reviewed')
        return ('PRESERVED_S01_READER','HISTORICAL_ACCEPTED_S01_READER','65-74',
                'Unchanged previous reader, retained for reproducibility and exact old-page regression; not current extent')
    if name.startswith('qa/s02/'):
        if '/repair_history/' in name:
            return ('S02_REPAIRED_DRAFT_HISTORY','SUPERSEDED_NOT_CURRENT_BUILD',pr,
                    'Preserved draft/build evidence before repair; final clean pass logs and readers are elsewhere')
        if '/source/' in name:
            return ('CONTROLLING_SOURCE_RASTER_OR_DETAIL','AUTHORITY_DERIVED_REVIEW_EVIDENCE',pr if page else '74-86',
                    '216dpi exact-scope source render or explicit detail crop; controlling raw PDF unchanged')
        if '/visual/' in name:
            return ('CURRENT_OUTPUT_VISUAL_EVIDENCE','RENDERED_AND_REVIEWED',pr,
                    '126dpi current reader rendering or S01-regression pair sheet; manual method stated in VISUAL_AUDIT.tsv')
        if '/build/' in name:
            return ('CURRENT_S02_BUILD_EVIDENCE','FINAL_BUILDS_PASS',pr,
                    'Final XeLaTeX run output; all six final pass logs checked for warnings and missing glyphs')
        return ('S02_VALIDATION_AND_COLLATION_EVIDENCE','RECORDED_AND_CHECKED',
                '63-98 mapping;65-86 acceptance;75-86 new collation',
                'Prompt02 source replay, alignment, preservation or QA ledger; manual observations distinguished from mechanical checks')
    if name.startswith('qa/'):
        prior = old.get(name); assert prior is not None
        return ('PRESERVED_S01_'+prior['role'],'HISTORICAL_S01_'+prior['acceptance'],prior['printed_page_range'],
                'Unchanged S01 QA evidence; current cumulative S02 QA is under qa/s02. Original: '+prior['provenance'])
    if name.startswith('tools/s02/'):
        return ('CURRENT_S02_REPRODUCIBILITY_TOOL','EDITABLE_IMPLEMENTATION_NOT_SOURCE_AUTHORITY','65-86',
                'Build, validation, alignment-record or packaging helper; executing code does not replace manual source/layout audit')
    if name.startswith('tools/'):
        return ('PRESERVED_S01_REPRODUCIBILITY_TOOL','HISTORICAL_S01_NOT_CURRENT_ORCHESTRATOR','63-74',
                'Unchanged S01 script; do not use to reset current cumulative state')
    if name == 'SOURCE_BACKED_DIFF.tsv':
        return ('CUMULATIVE_SOURCE_BACKED_DIFF','AUTHORITY_BACKED_CORRECTIONS','63-86',
                '44 original S01 rows retained verbatim, followed by26 source-backed S02 corrections; no fabricated missing-page correction rows')
    if name == 'README.md':
        return ('CURRENT_HANDOFF_DOCUMENTATION','CURRENT_INFORMATION','63-98 project;65-86 accepted',
                'Current extent, immutable preservation, source policy, QA, build instructions, and non-circular handoff hash contract')
    raise AssertionError(('unclassified member',name))


def archive(root: Path, target: Path, rows: list[dict]) -> None:
    with zipfile.ZipFile(target, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6, allowZip64=True) as z:
        for row in rows:
            info = zipfile.ZipInfo(row['path'], STAMP)
            info.create_system = 3; info.external_attr = (stat.S_IFREG | 0o644) << 16
            info.compress_type = zipfile.ZIP_DEFLATED; info._compresslevel = 6
            with (root/row['path']).open('rb') as inp, z.open(info,'w',force_zip64=True) as out:
                shutil.copyfileobj(inp,out,1024*1024)


def main(root: Path, out: Path) -> dict:
    root=root.resolve(); out=out.resolve(); out.mkdir(parents=True,exist_ok=True)
    assert out != root and root not in out.parents, 'Output must be outside the cumulative tree'
    # Reconfirm actual S01 ZIP bytes when available; prior verified intake remains in release.
    prev=out/'DIRICHLET_P04_S01_CUMULATIVE_FULL_STATE.zip'
    if prev.exists():
        assert prev.stat().st_size==EXPECTED_S01_BYTES and digest(prev)==EXPECTED_S01_SHA
    preserve=preservation(root)
    cur=json.loads((root/'state/CURSOR.json').read_text())
    assert cur['next_cursor']==3 and cur['prompt_completed']==2 and not cur['whole_paper_complete']
    for k in ['accepted_french_pages','accepted_english_pages','accepted_apparatus_pages']:
        assert cur[k]==list(range(65,87))
    dump(root/'qa/s02/RELEASE_PREFLIGHT.json',{
        'schema':'dirichlet-s02-release-preflight-v1', 'session':2,
        'current_cursor':3,'first_untouched_page':87,'source_batch_complete':True,
        's01_preservation':preserve,
        'immutable_input_count':21,'original_r27_r28_archives_preserved':True,
        'current_qa_gates':'qa/s02/PROMPT_02_GATES.tsv',
        'cold_source_audit':'NOT_EXECUTED; REQUIRED_AFTER_PROMPT03',
        'archive_verification_location':'External CHECKPOINT.json archive_validation after ZIP reopening; no circular hash in a member'})
    with (root/'prior_evidence/S01/MANIFEST.tsv').open(encoding='utf-8',newline='') as f:
        old={r['path']:r for r in csv.DictReader(f,delimiter='\t')}
    files=sorted((p for p in root.rglob('*') if p.is_file()),key=lambda p:p.relative_to(root).as_posix())
    rows=[]
    for p in files:
        n=p.relative_to(root).as_posix();safe_name(n)
        assert not p.is_symlink() and '__pycache__' not in n and p.suffix.lower() not in {'.pyc','.ttf','.otf','.ttc','.woff','.woff2'}, n
        assert 'CUMULATIVE_FULL_STATE.zip' not in n,n
        role,acc,pr,prov=classify(n,old,cur)
        rows.append(dict(path=n,bytes=p.stat().st_size,sha256=digest(p),role=role,acceptance=acc,printed_page_range=pr,provenance=prov))
    assert len(rows)==len({r['path'] for r in rows})
    mp,cp,dp,zp=(out/'MANIFEST.tsv',out/'CHECKPOINT.json',out/'SOURCE_BACKED_DIFF.tsv',out/ZIP_NAME)
    tsv(mp,FIELDS,rows);shutil.copyfile(root/'SOURCE_BACKED_DIFF.tsv',dp)
    archive(root,zp,rows)
    second=out/'.S02_DETERMINISM_CHECK.tmp.zip'
    archive(root,second,rows)
    assert zp.stat().st_size==second.stat().st_size and digest(zp)==digest(second),'ZIP determinism mismatch'
    second.unlink()
    checkpoint=dict(cur)
    checkpoint.update({
        'schema':'dirichlet-paper-iv-checkpoint-v2','schema_version':2,
        'prompt_file':'input/21_PROMPT_02_PP075_086.md',
        'completion_claim_scope':'Prompt02 only; printed65-86 accepted cumulatively; final full-paper cold audit remains required',
        'input_package':json.loads((root/'qa/s02/INPUT_PACKET_VALIDATION.json').read_text()),
        'copy_topology_state':'PASS_63_TITLE_64_BLANK_EXCLUDED_FROM_AUTHOR_READERS',
        'build_and_visual':json.loads((root/'qa/s02/BUILD_AND_VISUAL_RECEIPT.json').read_text()),
        'source_comparison':{
            'new_author_pages':list(range(75,87)), 'new_authority_full_pdf_pages':list(range(92,104)),
            'new_exact_scope_leaves':list(range(13,25)),
            'r28_replayed_pages':list(range(75,81)), 'direct_source_pages':list(range(81,87)),
            'new_aligned_units':85,'new_paired_math_segments':499,
            'new_french_editable_lines_audited':508,'new_english_editable_lines_audited':508,
            'inherited_tex_lines_classified':396,
            'cumulative_aligned_units':139,'cumulative_paired_math_segments':914,
            'cumulative_diff_rows':70,'new_diff_rows':26,
            'old_s01_source_acceptance':'PRESERVED; no independent cold source collation claimed this session',
            'seam_74_75':'PASS','seam_80_81':'PASS', 'no_new_author_footnotes':True,
            'genuinely_illegible_ambiguities':[],
            'source_print_issues_retained_this_session':[77,82,85],
            'cold_source_audit':'NOT_EXECUTED_REQUIRED_AFTER_PROMPT03'},
        's01_member_preservation':preserve,
        'release_artifacts':{'cumulative_zip':identity(zp),'manifest':identity(mp),'source_backed_diff':identity(dp)},
        'archive_member_count':len(rows),
        'archive_members':{r['path']:{'bytes':r['bytes'],'sha256':r['sha256']} for r in rows},
        'hash_binding_policy':{
            'external_checkpoint_binds':'ZIP, external exact manifest, external cumulative diff, all archive members',
            'current_internal_state':'state/CURSOR.json; independent of external archive hash',
            'manifest':'External normalized path inventory; exactly one row per regular ZIP member',
            'diff':'Identical internal SOURCE_BACKED_DIFF.tsv and external sibling bytes',
            'no_circular_self_hash':'Current external checkpoint/manifest are not embedded; historical S01 metadata is preserved as evidence'},
        'deterministic_zip':{'method':'Sorted NFC relative paths; fixed2026-09-21 timestamp; Unix regular0644; DEFLATE6; no directory entries',
                             'identical_second_build':True,'reproducibility_scope':'Same frozen member bytes; rebuilding PDFs may change PDF producer timestamps'},
        'archive_validation':{'status':'PENDING_REOPEN_IN_THIS_PACKAGING_RUN'}})
    dump(cp,checkpoint)
    spec=importlib.util.spec_from_file_location('s02_release_verifier',root/'tools/s02/verify_handoff_s02.py')
    assert spec and spec.loader
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    receipt=module.verify(zp,mp,cp,dp)
    checkpoint['archive_validation']=receipt;dump(cp,checkpoint)
    final_receipt=module.verify(zp,mp,cp,dp)
    assert final_receipt==receipt
    final_receipt.update({'release_artifacts':{**checkpoint['release_artifacts'],'checkpoint':identity(cp)},
                          'deterministic_second_build':'BYTE_IDENTICAL'})
    dump(out/'S02_RELEASE_RECEIPT.json',final_receipt)
    return final_receipt

if __name__=='__main__':
    if len(sys.argv)>3:raise SystemExit(__doc__)
    root=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parents[2]
    out=Path(sys.argv[2]) if len(sys.argv)>2 else root.parent
    print(json.dumps(main(root,out),indent=2,ensure_ascii=False))
