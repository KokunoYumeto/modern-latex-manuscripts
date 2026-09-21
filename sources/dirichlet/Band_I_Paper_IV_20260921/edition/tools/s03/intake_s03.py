from pathlib import Path
import hashlib,json,csv,zipfile,shutil,unicodedata,fitz
R=Path(__file__).resolve().parents[2];D=R.parent;Q=R/'qa/s03';H=R/'history/S02'
def sha(b):return hashlib.sha256(b).hexdigest().upper()
cp=json.loads((D/'CHECKPOINT.json').read_text());assert cp['session']==2 and cp['next_cursor']==3
for k in ('accepted_french_pages','accepted_english_pages','accepted_apparatus_pages'):assert cp[k]==list(range(65,87))
assert cp['accepted_copy_matter_pages']==[63,64] and cp['first_untouched_page']==87
for k,r in cp['release_artifacts'].items():
 b=(D/r['file']).read_bytes();assert len(b)==r['bytes'] and sha(b)==r['sha256']
rows=list(csv.DictReader((D/'MANIFEST.tsv').open(),delimiter='\t'));assert len(rows)==517
with zipfile.ZipFile(D/cp['release_artifacts']['cumulative_zip']['file']) as z:
 assert z.testzip() is None;ns=z.namelist();assert len(ns)==len(set(ns))==517
 assert set(ns)=={r['path'] for r in rows}==set(cp['archive_members'])
 for r in rows:
  n=r['path'];assert n==unicodedata.normalize('NFC',n) and not Path(n).is_absolute() and '..' not in Path(n).parts and '\\' not in n
  b=z.read(n);assert len(b)==int(r['bytes']) and sha(b)==r['sha256'];assert b==(R/n).read_bytes()
  assert cp['archive_members'][n]['sha256']==sha(b)
 assert z.read('SOURCE_BACKED_DIFF.tsv')==(D/'SOURCE_BACKED_DIFF.tsv').read_bytes()
 H.mkdir(parents=True,exist_ok=True)
 for n in ('CHECKPOINT.json','MANIFEST.tsv','SOURCE_BACKED_DIFF.tsv'):shutil.copy2(D/n,H/n)
 # Preserve each member about to be superseded. All other S02 members stay in place.
 for n in ['README.md','SOURCE_BACKED_DIFF.tsv','apparatus/CATALOGUE.tsv','apparatus/main.tex','editions/fr/main.tex','editions/en/main.tex','state/CURSOR.json']+[str(x.relative_to(R)) for x in (R/'ledgers').glob('*') if x.is_file()]:
  p=H/'superseded'/n;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(z.read(n))
for r in csv.DictReader((R/'input/02_INPUT_PAYLOAD_INVENTORY.tsv').open(),delimiter='\t'):
 b=(R/'input'/r['file']).read_bytes();assert len(b)==int(r['bytes']) and sha(b)==r['sha256']
controls=sorted([x for x in (R/'input').iterdir() if x.name[:2] in [f'{i:02}' for i in range(10)]])+[R/'input/22_PROMPT_03_PP087_098.md']
assert len(controls)==11
(Q/'INSTRUCTION_READ_RECEIPT.json').write_text(json.dumps({'controls_read':[{'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())} for p in controls],'prompt_only':3,'initial_state_not_used_for_cursor':True},indent=2)+'\n')
full=fitz.open(R/'input/11_AUTHORITY_FULL_DIRICHLET_GESAMMELTE_WERKE_BAND_I_1889.pdf');scope=fitz.open(R/'input/10_AUTHORITY_EXACT_SCOPE_PDF_PAGES_080_115_PRINTED_PP063_098.pdf')
assert len(full)==657 and len(scope)==36
rr=[]
(Q/'source').mkdir(exist_ok=True)
for p in [74,75,80,81,86]+list(range(87,99)):
 a=scope[p-63].get_pixmap(matrix=fitz.Matrix(3,3));b=full[p+16].get_pixmap(matrix=fitz.Matrix(3,3));assert a.samples==b.samples
 fn=Q/'source'/f'p{p:03}_authority.png';a.save(fn);rr.append({'printed_page':p,'full_pdf_page':p+17,'scope_leaf':p-62,'dpi':216,'pixel_equality':'PASS','image':str(fn.relative_to(R)),'sha256':sha(fn.read_bytes())})
full[115].get_pixmap(matrix=fitz.Matrix(2,2)).save(Q/'source/boundary_pdf116_inspection_only.png')
with (Q/'PAGEWISE_RASTER_EQUIVALENCE.tsv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(rr[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rr)
(Q/'S02_INTAKE_VALIDATION.json').write_text(json.dumps({'schema':'dirichlet-s03-intake-v1','prior_release':cp['release_artifacts'],'members':517,'crc':'PASS','paths':'PASS','manifest':'PASS','member_hashes':'PASS','checkpoint_bindings':'PASS','editable_fr_en_pages_readable':22,'authority_scope_pages':36,'authority_full_pages':657,'next_cursor':3,'accepted_pages':list(range(65,87)),'prior_source_issues_preserved':[66,70,77,82,85],'standalone_sidecars_archived_at':'history/S02','not_a_cold_source_audit':True},indent=2)+'\n')
print('ALL INTAKE GATES PASS; CURRENT AUTHORITY AND EDITABLE S02 BYTES READABLE')
