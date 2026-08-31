"""One authorized label-position derivative, with exact witness preservation."""
import argparse, difflib, json, os, re, shutil, subprocess
import fitz
import build_d031_release as b

def native():
    witness=b.WORK/'gate_normalized_witness'
    engine=shutil.which('pdflatex'); assert engine
    env=dict(os.environ,SOURCE_DATE_EPOCH=b.EPOCH,FORCE_SOURCE_DATE='1',TZ='UTC')
    result={'schema':'d031-presentation-validation-v1','status':'RUNNING',
            'repair':'Physical33 printed279: right vertical-arrow label moved to pos=0.75 to clear upper-right oblique arrow shaft',
            'scope':'Label position only; no text, symbols, arrows, endpoints, graph incidence or page topology changed',
            'original_gate':b.identity(b.GATE/'gate_acceptance.json'),'gate_master_unchanged':True,
            'languages':{},'independent_visual_status':'PENDING_NEW_RENDER_REVIEW'}
    for lang,name in b.READERS.items():
        original=(witness/f'{name}.tex').read_bytes()
        current=(b.WORK/'normalized'/f'{name}.tex').read_bytes()
        old=b'"{(g,m(t_1))+(g,m(t_2))}"]'
        new=b'"{(g,m(t_1))+(g,m(t_2))}"{pos=0.75}]'
        assert original.count(old)==1
        expected=original.replace(old,new)
        # The patch editor changed the edited line's terminator. Restore only
        # that formatting difference, after verifying the complete content.
        assert current.replace(b'\r\n',b'\n')==expected.replace(b'\r\n',b'\n')
        if current != expected:
            (b.WORK/'normalized'/f'{name}.tex').write_bytes(expected)
            current=expected
        diff=''.join(difflib.unified_diff(original.decode().splitlines(True),current.decode().splitlines(True),fromfile='gate_normalized_witness/'+name+'.tex',tofile='normalized/'+name+'.tex'))
        (b.AUDIT/f'PRESENTATION_LABEL_DELTA_{lang}.diff').write_text(diff,encoding='utf-8',newline='\n')
        outputs=[]
        for index in (1,2):
            slot=b.BUILD/f'native_label_fix_{lang}_{index}'; assert not slot.exists()
            slot.mkdir(); shutil.copy2(b.WORK/'normalized'/f'{name}.tex',slot/f'{name}.tex')
            for pass_number in (1,2):
                with (b.AUDIT/f'native_label_fix_{lang}_{index}_{pass_number}.stdout.txt').open('w',encoding='utf-8') as out:
                    run=subprocess.run([engine,'-interaction=nonstopmode','-halt-on-error',f'{name}.tex'],cwd=slot,env=env,stdout=out,stderr=subprocess.STDOUT,timeout=240)
                assert run.returncode==0,(lang,index,pass_number)
            log=(slot/f'{name}.log').read_text(encoding='utf-8',errors='replace')
            anomalies={'errors':len(re.findall(r'^!',log,re.M)),'missing_glyphs':log.count('Missing character:'),'overfull_boxes':log.count('Overfull ')}
            assert not any(anomalies.values()),anomalies
            outputs.append(b.identity(slot/f'{name}.pdf'))
            print('Native label-only build',lang,index,'PASS',flush=True)
        assert outputs[0]==outputs[1]
        shutil.copy2(b.BUILD/f'native_label_fix_{lang}_1'/f'{name}.pdf',b.WORK/'normalized'/f'{name}.pdf')
        unchanged=[]
        with fitz.open(witness/f'{name}.pdf') as oldpdf, fitz.open(b.WORK/'normalized'/f'{name}.pdf') as newpdf:
            assert len(oldpdf)==len(newpdf)==43
            for i in range(43):
                oldsig,newsig=b.signature(oldpdf[i]),b.signature(newpdf[i])
                assert oldpdf[i].get_text()==newpdf[i].get_text(),(lang,i+1,'text')
                if i!=32:
                    assert oldsig==newsig,(lang,i+1,'raster')
                    unchanged.append(i+1)
                else: assert oldsig['raster_sha256']!=newsig['raster_sha256']
            newpdf[32].get_pixmap(matrix=fitz.Matrix(240/72,240/72),alpha=False,colorspace=fitz.csRGB).save(b.AUDIT/f'{lang}_LABEL_FIXED_PHYSICAL_33_240DPI.png')
        result['languages'][lang]={'status':'PASS','original_pdf':b.identity(witness/f'{name}.pdf'),
            'original_tex':b.identity(witness/f'{name}.tex'),'new_pdf':b.identity(b.WORK/'normalized'/f'{name}.pdf'),
            'new_tex':b.identity(b.WORK/'normalized'/f'{name}.tex'),'original_witness_path':f'works/D031_PUBLIC_SAFE/gate_normalized_witness/{name}.pdf',
            'current_reader_path':f'works/D031_PUBLIC_SAFE/normalized/{name}.pdf',
            'literal_diff':b.identity(b.AUDIT/f'PRESENTATION_LABEL_DELTA_{lang}.diff'),
            'pages':43,'all43_extracted_text_exact':True,'unchanged42_pages_raster_text_exact':unchanged,
            'only_changed_physical_page':33,'repeat_native_build_byte_identical':True,
            'corrected_render':b.identity(b.AUDIT/f'{lang}_LABEL_FIXED_PHYSICAL_33_240DPI.png')}
        b.dump(b.AUDIT/'D031_PRESENTATION_VALIDATION_RECEIPT.json',result)
    result['status']='PASS_MECHANICAL_PENDING_VISUAL'
    b.dump(b.AUDIT/'D031_PRESENTATION_VALIDATION_RECEIPT.json',result)
    b.dump(b.WORK/'normalized/output_manifest.json',{'schema':'d031-maintained-presentation-derivative-output-manifest-v1',
        'status':'PASS_MECHANICAL_PENDING_VISUAL','source_gate_readers_retained_in':'../gate_normalized_witness',
        'files':{p.name:b.identity(p) for p in sorted((b.WORK/'normalized').iterdir()) if p.is_file() and p.name!='output_manifest.json'},
        'presentation_validation':b.identity(b.AUDIT/'D031_PRESENTATION_VALIDATION_RECEIPT.json')})

def cumulative():
    result=json.loads((b.AUDIT/'D031_PRESENTATION_VALIDATION_RECEIPT.json').read_text())
    for lang,page_number in (('EN',674),('FR',688)):
        newpath=b.SOURCE/f'Deligne_{lang}.pdf'; oldpath=b.BUILD/'compile_slot'/f'Deligne_{lang}.pdf'
        unchanged=[]
        with fitz.open(oldpath) as oldpdf,fitz.open(newpath) as newpdf:
            assert len(oldpdf)==len(newpdf)
            for i in range(len(newpdf)):
                assert oldpdf[i].get_text()==newpdf[i].get_text(),(lang,i+1)
                if i+1!=page_number:
                    assert b.signature(oldpdf[i])==b.signature(newpdf[i]),(lang,i+1)
                    unchanged.append(i+1)
            newpdf[page_number-1].get_pixmap(matrix=fitz.Matrix(240/72,240/72),alpha=False,colorspace=fitz.csRGB).save(b.AUDIT/f'{lang}_LABEL_FIXED_CUMULATIVE_{page_number}_240DPI.png')
        result['languages'][lang]['cumulative']={'original_pdf':b.identity(oldpath),'new_pdf':b.identity(newpath),
            'changed_page':page_number,'all_extracted_text_exact':True,'all_other_pages_raster_text_exact':True,
            'exact_unchanged_page_count':len(unchanged),
            'render':b.identity(b.AUDIT/f'{lang}_LABEL_FIXED_CUMULATIVE_{page_number}_240DPI.png')}
    b.dump(b.AUDIT/'D031_PRESENTATION_VALIDATION_RECEIPT.json',result)
    print('All cumulative pages except the two label-position pages are raster/text identical',flush=True)

def finalize_visual():
    path=b.AUDIT/'D031_PRESENTATION_VALIDATION_RECEIPT.json'
    result=json.loads(path.read_text())
    independent=b.AUDIT/'D031_RELEASE_INDEPENDENT_CONTENT_AUDIT.json'
    independent_native=b.AUDIT/'D031_INDEPENDENT_PRESENTATION_REPLAY.json'
    assert json.loads(independent.read_text())['status']=='PASS'
    assert json.loads(independent_native.read_text())['status']=='PASS'
    for lang,name in b.READERS.items():
        row=result['languages'][lang]
        assert row['new_pdf']==b.identity(b.WORK/'normalized'/f'{name}.pdf')
        assert row['new_tex']==b.identity(b.WORK/'normalized'/f'{name}.tex')
        assert row['cumulative']['new_pdf']==b.identity(b.SOURCE/f'Deligne_{lang}.pdf')
        assert row['all43_extracted_text_exact'] and len(row['unchanged42_pages_raster_text_exact'])==42
        assert row['cumulative']['all_other_pages_raster_text_exact']
        row['text_extraction_method']='PyMuPDF raw get_text exact on all43 pages; independent pypdf whitespace-normalized text exact on all43, one inter-label whitespace changes on physical33'
    result.update(status='PASS',independent_visual_status='PASS',
        independent_content_audit=b.identity(independent),
        independent_native_presentation_replay=b.identity(independent_native),
        final_visual_observations='Main and independent auditor directly viewed corrected physical33 and cumulative674/688 at240dpi: right vertical label clears oblique shaft; no new clipping, collision, missing glyph or change in graph incidence observed.',
        presentation_only=True,mathematical_content_changed=False)
    b.dump(path,result)
    print('Presentation mechanical and independent visual validation PASS',flush=True)

def finish_metadata():
    receipt=json.loads((b.AUDIT/'D031_PRESENTATION_VALIDATION_RECEIPT.json').read_text())
    assert receipt['status']=='PASS' and receipt['independent_visual_status']=='PASS'
    witness=b.WORK/'gate_normalized_witness'
    records=json.loads((witness/'page_record_manifest.json').read_text())
    pattern=re.compile(r'\\SourcePage\{(\d+)\}\{(\d+)\}\n(.*?)(?=\\SourcePage\{\d+\}\{\d+\}\n|\\end\{document\})',re.S)
    for name in b.READERS.values():
        oldparts=pattern.findall((witness/f'{name}.tex').read_text(encoding='utf-8'))
        newparts=pattern.findall((b.WORK/'normalized'/f'{name}.tex').read_text(encoding='utf-8'))
        assert len(oldparts)==len(newparts)==43
        for old,new,row in zip(oldparts,newparts,records[name]):
            assert old[0]==new[0]==str(row['physical_page'])
            assert b.ident_data(old[2][:-1].encode())['sha256']==row['derived_tex_sha256']
            row['derived_tex_sha256']=b.ident_data(new[2][:-1].encode())['sha256']
    b.dump(b.WORK/'normalized/page_record_manifest.json',records)
    shutil.copy2(b.AUDIT/'D031_PRESENTATION_VALIDATION_RECEIPT.json',b.WORK/'D031_PRESENTATION_VALIDATION_RECEIPT.json')
    b.dump(b.WORK/'normalized/output_manifest.json',{'schema':'d031-maintained-presentation-derivative-output-manifest-v1',
        'status':'PASS','source_gate_readers_retained_in':'../gate_normalized_witness',
        'files':{p.name:b.identity(p) for p in sorted((b.WORK/'normalized').iterdir()) if p.is_file() and p.name!='output_manifest.json'},
        'presentation_validation':b.identity(b.AUDIT/'D031_PRESENTATION_VALIDATION_RECEIPT.json')})
    print('Current native output and per-page TeX manifests rebased to presentation derivative',flush=True)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('stage',choices=['native','cumulative','finalize_visual','finish_metadata'])
    globals()[parser.parse_args().stage]()
