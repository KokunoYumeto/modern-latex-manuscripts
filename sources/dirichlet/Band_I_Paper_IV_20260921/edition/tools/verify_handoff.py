#!/usr/bin/env python3
"""Verify the four-file, non-circular Dirichlet cumulative handoff.

Usage: verify_handoff.py RELEASE.zip MANIFEST.tsv CHECKPOINT.json DIFF.tsv
No extraction is necessary; every member is reopened, streamed and hashed.
"""
from __future__ import annotations
import csv,hashlib,json,re,stat,sys,unicodedata,zipfile
from pathlib import Path,PurePosixPath

def digest_file(path:Path)->str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
    return h.hexdigest().upper()

def safe_name(name:str)->bool:
    p=PurePosixPath(name)
    return bool(name) and name==unicodedata.normalize('NFC',name) and not p.is_absolute() and p.as_posix()==name and all(c not in ('.','..','') for c in name.split('/')) and '\\' not in name and not re.match(r'^[A-Za-z]:',name)

def verify(zip_path:Path,manifest_path:Path,checkpoint_path:Path,diff_path:Path)->dict:
    with manifest_path.open(encoding='utf8',newline='') as f:
        rows=list(csv.DictReader(f,delimiter='\t'))
    assert rows and list(rows[0])==['path','bytes','sha256','role','acceptance','printed_page_range','provenance']
    paths=[r['path'] for r in rows]
    assert paths==sorted(paths) and len(paths)==len(set(paths))
    assert all(safe_name(p) for p in paths)
    assert all(re.fullmatch(r'[0-9A-F]{64}',r['sha256']) for r in rows)
    manifest={r['path']:r for r in rows}
    checkpoint=json.loads(checkpoint_path.read_text(encoding='utf8'))
    for key,path in [('cumulative_zip',zip_path),('manifest',manifest_path),('source_backed_diff',diff_path)]:
        rec=checkpoint['release_artifacts'][key]
        assert rec['file']==path.name and rec['bytes']==path.stat().st_size
        assert rec['sha256']==digest_file(path),(key,'external hash')
    inv=checkpoint['archive_members']
    assert set(inv)==set(manifest)
    with zipfile.ZipFile(zip_path) as z:
        assert z.testzip() is None
        infos=z.infolist();names=[i.filename for i in infos]
        assert names==sorted(names) and len(names)==len(set(names)) and set(names)==set(manifest)
        assert len({n.casefold() for n in names})==len(names)
        for info in infos:
            name=info.filename
            assert safe_name(name) and not info.is_dir()
            assert not stat.S_ISLNK(info.external_attr>>16)
            assert not (name.lower().endswith('.zip') and 'cumulative' in PurePosixPath(name).name.lower())
            assert PurePosixPath(name).suffix.lower() not in {'.ttf','.otf','.woff','.woff2','.ttc'}
            h=hashlib.sha256();length=0
            with z.open(info) as stream:
                for block in iter(lambda:stream.read(1024*1024),b''):
                    h.update(block);length+=len(block)
            got=h.hexdigest().upper();row=manifest[name]
            assert length==info.file_size==int(row['bytes'])==inv[name]['bytes']
            assert got==row['sha256']==inv[name]['sha256'],name
        assert z.read('SOURCE_BACKED_DIFF.tsv')==diff_path.read_bytes()
        cursor=json.loads(z.read('state/CURSOR.json'))
        for key in ['prompt_completed','next_cursor','prompt_cursor','accepted_french_pages','accepted_english_pages','accepted_apparatus_pages','accepted_copy_matter_pages','first_untouched_page','whole_paper_complete']:
            assert cursor[key]==checkpoint[key],key
        assert cursor['prompt_completed']==1 and cursor['next_cursor']==2
        for key in ['accepted_french_pages','accepted_english_pages','accepted_apparatus_pages']:
            assert cursor[key]==list(range(65,75))
        assert cursor['accepted_copy_matter_pages']==[63,64] and cursor['first_untouched_page']==75
        assert not cursor['prompt_02_executed'] and not cursor['whole_paper_complete']
        for lang in ['fr','en']:
            actual=sorted(n for n in names if re.fullmatch(fr'editions/{lang}/pages/p\d{{3}}\.tex',n))
            assert actual==[f'editions/{lang}/pages/p{p:03d}.tex' for p in range(65,75)]
        for pg in range(65,75):
            rec=json.loads(z.read(f'state/pages/p{pg:03d}.json'))
            assert rec['printed_page']==pg and rec['authority_pdf_page']==pg+17 and rec['scope_leaf']==pg-62
            assert rec['acceptance']=='ACCEPTED_SOURCE_BACKED_S01' and rec['visual_output_audit']=='PASS'
            for lang in ['french','english']:
                assert rec[lang]['sha256']==manifest[rec[lang]['path']]['sha256']
            assert rec['apparatus_sha256']==manifest[rec['apparatus_path']]['sha256']
            assert rec['source_image_sha256']==manifest[rec['source_image']]['sha256']
        for rec in cursor['current_readers'].values():
            assert rec['sha256']==manifest[rec['path']]['sha256']
        visual=list(csv.DictReader(z.read('qa/VISUAL_AUDIT.tsv').decode('utf8').splitlines(),delimiter='\t'))
        assert len(visual)==22 and all(r['status']=='PASS' for r in visual)
        for r in visual:
            assert r['render_sha256']==manifest[r['render']]['sha256']
            assert r['reader_sha256']==manifest[r['reader']]['sha256']
        diffs=list(csv.DictReader(diff_path.read_text(encoding='utf8').splitlines(),delimiter='\t'))
        assert len(diffs)==44 and all(r['before']!='NONE' and r['evidence'] for r in diffs)
    return {'status':'PASS','zip_crc':'PASS','path_safety':'PASS','unique_normalized_names':'PASS','manifest_exactness':'PASS','member_lengths_and_sha256':'PASS','checkpoint_artifact_bindings':'PASS','checkpoint_member_bindings':'PASS','cursor_and_page_sets':'PASS','page_record_bindings':'PASS','diff_identity':'PASS','visual_evidence_bindings':'PASS','no_nested_prior_cumulative_zip':'PASS','members_verified':len(rows),'accepted_pages_per_layer':list(range(65,75)),'next_cursor':2}

if __name__=='__main__':
    if len(sys.argv)!=5:
        raise SystemExit(__doc__)
    print(json.dumps(verify(*(Path(x) for x in sys.argv[1:])),indent=2))
