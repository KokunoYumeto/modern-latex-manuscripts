#!/usr/bin/env python3
"""Verify the S04 four-file handoff from archive bytes, without extracting paths.
This checks transport, state and evidence bindings; it does not pretend that an
algorithm can replace the separately recorded human/model scan reading.
"""
from __future__ import annotations
from pathlib import Path,PurePosixPath
import argparse,csv,hashlib,io,json,re,stat,unicodedata,zipfile
import fitz
from PIL import Image


def digest(b:bytes)->str:return hashlib.sha256(b).hexdigest().upper()
def filehash(p:Path)->str:
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1<<20),b''):h.update(b)
    return h.hexdigest().upper()
def table(b:bytes)->list[dict]:return list(csv.DictReader(io.StringIO(b.decode('utf-8')),delimiter='\t'))
def safe(n:str)->str:
    assert n and not n.startswith('/') and '\\' not in n and ':' not in n,('unsafe path',n)
    assert all(p not in ('','.','..') for p in n.split('/')) and not any(ord(c)<32 for c in n)
    assert PurePosixPath(n).as_posix()==n and unicodedata.normalize('NFC',n)==n
    return n

def verify(zp:Path,cp:Path,mp:Path,dp:Path)->dict:
    c=json.loads(cp.read_text());mr=table(mp.read_bytes())
    assert set(mr[0])=={'path','bytes','sha256','role','acceptance','printed_page_range','provenance'}
    assert [r['path'] for r in mr]==sorted({r['path'] for r in mr})
    expected_names={'cumulative_zip':'DIRICHLET_P04_S04_CUMULATIVE_FULL_STATE.zip','manifest':'DIRICHLET_P04_S04_MANIFEST.tsv','source_backed_diff':'DIRICHLET_P04_S04_SOURCE_BACKED_DIFF.tsv'}
    assert cp.name=='DIRICHLET_P04_S04_CHECKPOINT.json'
    for key,p in [('cumulative_zip',zp),('manifest',mp),('source_backed_diff',dp)]:
        a=c['release_artifacts'][key]
        assert a['file']==p.name==expected_names[key]
        assert a['bytes']==p.stat().st_size and a['sha256']==filehash(p),(key,'sidecar binding')
    assert c['session']==c['prompt_completed']==4
    assert c['status']==c['next_cursor']==c['prompt_cursor']=='COMPLETE'
    assert c['prompt_04_executed'] and c['whole_paper_complete'] and c['first_untouched_page'] is None
    for k in ['accepted_french_pages','accepted_english_pages','accepted_apparatus_pages']:assert c[k]==list(range(65,99))
    assert c['accepted_copy_matter_pages']==[63,64] and c['unresolved_source_ambiguities']==[] and c['known_author_content_defects']==[]
    with zipfile.ZipFile(zp) as z:
        assert z.testzip() is None
        infos=z.infolist();names=[safe(i.filename) for i in infos]
        assert names==sorted(set(names)) and len({n.casefold() for n in names})==len(names)
        assert all(not i.is_dir() and not stat.S_ISLNK(i.external_attr>>16) for i in infos)
        assert all(i.compress_type==zipfile.ZIP_DEFLATED and i.date_time==(2026,9,21,0,0,0) for i in infos)
        assert all((i.external_attr>>16)==(stat.S_IFREG|0o644) for i in infos)
        assert not any('CUMULATIVE_FULL_STATE.zip' in n for n in names)
        assert not any(Path(n).suffix.lower() in {'.ttf','.otf','.ttc','.woff','.woff2','.pyc'} for n in names)
        assert set(names)=={r['path'] for r in mr}==set(c['archive_members'])
        assert len(names)==c['archive_member_count']
        m={r['path']:r for r in mr}; hashes={};sizes={}
        for i in infos:
            b=z.read(i);r=m[i.filename];a=c['archive_members'][i.filename]
            assert len(b)==i.file_size==int(r['bytes'])==a['bytes']
            sha=digest(b);assert re.fullmatch(r'[0-9A-F]{64}',r['sha256']) and sha==r['sha256']==a['sha256']
            assert all(r[k] for k in ['role','acceptance','printed_page_range','provenance'])
            hashes[i.filename]=sha;sizes[i.filename]=len(b)
        j=lambda n:json.loads(z.read(n))
        cur=j('state/CURSOR.json')
        for k in ['session','prompt_completed','next_cursor','prompt_cursor','status','accepted_french_pages','accepted_english_pages','accepted_apparatus_pages','accepted_copy_matter_pages','current_readers','first_untouched_page','whole_paper_complete','prompt_04_executed','known_author_content_defects']:
            assert cur[k]==c[k],('cursor binding',k)
        assert z.read('SOURCE_BACKED_DIFF.tsv')==dp.read_bytes()
        dif=table(dp.read_bytes());assert len(dif)==93
        prev=j('history/S03/CHECKPOINT.json');assert prev['next_cursor']==4 and not prev['prompt_04_executed']
        oldmanifest=z.read('history/S03/MANIFEST.tsv');old_diff=z.read('history/S03/SOURCE_BACKED_DIFF_CANONICAL.tsv')
        for key,b in [('manifest',oldmanifest),('source_backed_diff',old_diff)]:
            a=prev['release_artifacts'][key];assert len(b)==a['bytes'] and digest(b)==a['sha256']
        assert len(old_diff)==27503 and len(table(old_diff))==72 and dp.read_bytes().startswith(old_diff)
        stale=z.read('history/S03/SOURCE_BACKED_DIFF_STALE_STANDALONE.tsv')
        assert len(stale)==26591 and digest(stale)=='42125A0817A23F31FDA381C862A9ED55557CA8FBDEC91BB42EA6109878186020'
        pres=table(z.read('qa/s04/S03_MEMBER_PRESERVATION.tsv'))
        assert len(pres)==793 and {r['s03_path'] for r in pres}==set(prev['archive_members'])
        for r in pres:
            a=prev['archive_members'][r['s03_path']];n=r['preserved_path']
            assert sizes[n]==int(r['bytes'])==a['bytes'] and hashes[n]==r['sha256']==a['sha256']
        for r in table(z.read('qa/s04/ALL_PRIOR_MEMBER_PRESERVATION.tsv')):
            assert sizes[r['preserved_path']]==int(r['bytes']) and hashes[r['preserved_path']]==r['sha256']
        assert len([n for n in names if n.startswith('input/')])==21
        for r in table(z.read('input/91_SHA256SUMS.tsv')):
            n='input/'+r['file'];assert sizes[n]==int(r['bytes']) and hashes[n]==r['sha256']
        for r in table(z.read('qa/s04/IMMUTABLE_INPUT_PRESERVATION.tsv')):
            assert sizes[r['path']]==int(r['bytes']) and hashes[r['path']]==r['sha256']
        for r in table(z.read('qa/s04/INHERITED_ORIGINAL_REVALIDATION.tsv')):
            assert sizes[r['preserved_path']]==int(r['bytes']) and hashes[r['preserved_path']]==r['sha256']
        # All36 source images remain bound to the actual controlling/provenance PDFs.
        fullpath='input/11_AUTHORITY_FULL_DIRICHLET_GESAMMELTE_WERKE_BAND_I_1889.pdf'
        scopepath='input/10_AUTHORITY_EXACT_SCOPE_PDF_PAGES_080_115_PRINTED_PP063_098.pdf'
        assert sizes[fullpath]==36067858 and hashes[fullpath]=='961E55A2D32DDC88191CDD8A99F877A06BB3E721D7705F5A96C6F80AD67F9F6C'
        full=fitz.open(stream=z.read(fullpath),filetype='pdf');scope=fitz.open(stream=z.read(scopepath),filetype='pdf')
        assert len(full)==657 and len(scope)==36
        manual=j('qa/s04/MANUAL_COLD_COLLATION.json');assert sorted(map(int,manual))==list(range(63,99))
        raster=table(z.read('qa/s04/SCOPE_RASTER_EQUIVALENCE.tsv'));assert len(raster)==36
        for i,r in enumerate(raster):
            p=i+63;assert int(r['printed_page'])==p and int(r['full_pdf_page'])==p+17 and int(r['scope_leaf'])==p-62
            a=scope[i].get_pixmap(matrix=fitz.Matrix(3,3));b=full[i+79].get_pixmap(matrix=fitz.Matrix(3,3))
            assert a.samples==b.samples and digest(a.samples)==r['raw_pixel_sha256']
            im=Image.open(io.BytesIO(z.read(r['image_path']))).convert('RGB')
            assert im.size==(a.width,a.height) and im.tobytes()==a.samples and hashes[r['image_path']]==r['image_sha256']
            assert manual[str(p)]['source_image']==r['image_path']
        boundary=full[115].get_pixmap(matrix=fitz.Matrix(3,3));im=Image.open(io.BytesIO(z.read('qa/s04/source/boundary_pdf116_inspection_only.png'))).convert('RGB')
        assert boundary.samples==im.tobytes() and not j('qa/s04/BOUNDARY_AUDIT.json')['paper_v_ingested']
        # Current exact-once monolingual sources and final page records.
        for l in ['fr','en']:
            main=z.read(f'editions/{l}/main.tex').decode()
            assert re.findall(r'\\input\{pages/p(\d+)\.tex\}',main)==[f'{p:03}' for p in range(65,99)]
            assert {n for n in names if n.startswith(f'editions/{l}/pages/')}=={f'editions/{l}/pages/p{p:03}.tex' for p in range(65,99)}
        for p in range(65,99):
            r=j(f'state/pages/p{p:03}.json');assert (r['printed_page'],r['authority_pdf_page'],r['scope_leaf'])==(p,p+17,p-62)
            for k in ['french','english','apparatus']:
                a=r[k];assert sizes[a['path']]==a['bytes'] and hashes[a['path']]==a['sha256']
            assert hashes[r['source_image']]==r['source_image_sha256']
            assert r['source_ambiguities']==[] and r['acceptance']=='COLD_AUDIT_ACCEPTED_S04' and r['cold_audit']=='COMPLETE'
        app=table(z.read('apparatus/CATALOGUE.tsv'));assert [int(r['printed_page']) for r in app]==list(range(65,99))
        top=table(z.read('ledgers/TOPOLOGY.tsv'));assert [int(r['printed_page']) for r in top]==list(range(63,99))
        for r in top:
            p=int(r['printed_page']);assert (int(r['authority_pdf_page']),int(r['scope_leaf']))==(p+17,p-62)
            assert int(r['occurrences_in_each_current_reader'])==(0 if p<65 else 1)
        assert sizes['copy_matter/p064.txt']==0
        assert len(table(z.read('qa/s04/ALL_AUTHOR_SEAMS.tsv')))==33
        # Final PDF/text/render bindings are regenerated on reopen, not assumed.
        builds=j('qa/s04/BUILD_RUNS.json');vis=j('qa/s04/MANUAL_OUTPUT_REVIEW.json');assert len(vis)==73
        reader_counts={}
        for l,a in c['current_readers'].items():
            n=a['path'];assert hashes[n]==a['sha256'] and sizes[n]==a['bytes']
            doc=fitz.open(stream=z.read(n),filetype='pdf');assert len(doc)==a['pages']==(5 if l=='apparatus' else 34)
            reader_counts[l]=len(doc);d=builds[l]
            assert d['clean_directory_at_start'] and d['reader']==n and d['reader_sha256']==a['sha256']
            for run in d['passes'][-2:]:
                assert run['exit_code']==0 and all(not run[k] for k in ['warnings','overfull','underfull','missing_glyphs'])
                assert run['pdf_sha256']==a['sha256']
                log=z.read(f"qa/s04/build/{l}/pass{run['pass']}.log").decode()
                assert 'Output written on' in log and not re.findall(r'^.*(?:Overfull|Underfull|Missing character|Warning|^!).*$',log,re.M)
            assert hashes[f'qa/s04/build/{l}/main.pdf']==a['sha256']
            for i,page in enumerate(doc):
                v=vis[f'{l}:{i+1}'];assert v['reader_sha256']==a['sha256'] and hashes[v['image']]==v['sha256']
                pix=page.get_pixmap(matrix=fitz.Matrix(1.75,1.75),alpha=False)
                im=Image.open(io.BytesIO(z.read(v['image']))).convert('RGB')
                assert im.size==(pix.width,pix.height) and im.tobytes()==pix.samples
                assert digest(pix.samples)==v['raw_pixel_sha256'] and digest(page.get_text().encode())==v['extracted_text_sha256']
                assert not any(v[k] for k in ['clipping','broken_math','missing_glyphs','note_overflow','wrong_order'])
                assert v['result']=='REVIEWED_NO_VISIBLE_DEFECT'
        checks=j('qa/s04/GLOBAL_CHECKS.json');assert checks['mismatches']==[] and checks['aligned_units']==200 and checks['paired_math_segments']==1461
        rr=j('qa/s04/REPAIRS.json');assert len(rr)==21
        for r in rr:
            before=z.read(r['snapshot']).decode();after=z.read(r['file']).decode()
            assert before.count(r['before'])==r['occurrences'] and r['after'] in after
            assert any(all(row[k]==r[k] for k in ['printed_page','authority_pdf_page','layer','before','after','evidence','disposition']) for row in dif[72:])
        gates=j('qa/s04/FINAL_COLD_AUDIT_GATES.json')
        assert gates['next_cursor']=='COMPLETE' and gates['known_author_content_defects']==gates['unresolved_source_ambiguities']==[]
        return {'status':'PASS','zip_crc':'PASS','safe_unique_normalized_paths':'PASS','exact_manifest_and_member_hashes':'PASS','checkpoint_and_stage_specific_sidecar_bindings':'PASS','reader_source_render_bindings':'PASS','all36_source_images_bound_to_actual_authority':'PASS','canonical93_row_diff':'PASS','s03_member_byte_sequences_preserved':793,'immutable_originals':21,'archive_members':len(names),'uncompressed_bytes':sum(sizes.values()),'reader_pages':reader_counts,'current_individual_output_reviews_bound':73,'next_cursor':'COMPLETE','source_fidelity_basis':'Actual manual cold collation and corrections recorded separately; this verifier authenticates their evidence bindings, not the act of reading.'}

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ['zip','checkpoint','manifest','diff']:parser.add_argument('--'+name,type=Path,required=True)
    args=parser.parse_args();print(json.dumps(verify(args.zip,args.checkpoint,args.manifest,args.diff),indent=2))
