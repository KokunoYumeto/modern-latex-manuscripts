"""Validate the accepted S01 bytes and the immutable packet, never its initial cursor as current state."""
from pathlib import Path,PurePosixPath
import csv,hashlib,json,zipfile,stat,io
import fitz
R=Path(__file__).resolve().parents[2]; Q=R/'qa/s02';Q.mkdir(parents=True,exist_ok=True)
def digest(b):return hashlib.sha256(b).hexdigest().upper()
def props(p):
 b=p.read_bytes();return {'file':p.name,'bytes':len(b),'sha256':digest(b)}
def writej(name,data):(Q/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def writet(name,rows,fields):
 with (Q/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
def safe(z):
 seen=set()
 for i in z.infolist():
  n=i.filename
  assert '\\' not in n and not n.startswith('/') and ':' not in n
  p=PurePosixPath(n);assert all(x not in ('..','.') for x in p.parts)
  norm=p.as_posix();assert norm not in seen;seen.add(norm)
  assert not stat.S_ISLNK(i.external_attr>>16)
 assert z.testzip() is None
 return {'crc':'PASS','normalized_names_unique':'PASS','path_safety':'PASS','regular_files':sum(not i.is_dir() for i in z.infolist()),'directory_entries':sum(i.is_dir() for i in z.infolist())}
prior=R/'prior_evidence/S01';cp=json.loads((prior/'CHECKPOINT.json').read_text()); zpath=R.parent/'DIRICHLET_P04_S01_CUMULATIVE_FULL_STATE.zip'
assert props(zpath)==cp['release_artifacts']['cumulative_zip']
assert zpath.stat().st_size==131808818 and props(zpath)['sha256']=='DEE2786989BCE3556912265B110856DB4578181386E322E4FC97CE64D583F162'
for field,filename in [('manifest','MANIFEST.tsv'),('source_backed_diff','SOURCE_BACKED_DIFF.tsv')]:assert props(prior/filename)==cp['release_artifacts'][field]
mr=list(csv.DictReader((prior/'MANIFEST.tsv').open(),delimiter='\t'));m={r['path']:r for r in mr}
with zipfile.ZipFile(zpath) as z:
 za=safe(z); names=[i.filename for i in z.infolist() if not i.is_dir()];assert len(names)==240
 assert set(names)==set(m)==set(cp['archive_members'])
 rows=[]
 for name in names:
  b=z.read(name);d=digest(b)
  assert len(b)==int(m[name]['bytes'])==cp['archive_members'][name]['bytes']
  assert d==m[name]['sha256']==cp['archive_members'][name]['sha256']
  rows.append({'path':name,'bytes':len(b),'sha256':d,'manifest_match':'PASS','checkpoint_match':'PASS'})
 assert z.read('SOURCE_BACKED_DIFF.tsv')==(prior/'SOURCE_BACKED_DIFF.tsv').read_bytes()
assert cp['prompt_completed']==1 and cp['next_cursor']==2 and cp['prompt_cursor']==2
for field in ['accepted_french_pages','accepted_english_pages','accepted_apparatus_pages']:assert cp[field]==list(range(65,75))
assert cp['accepted_copy_matter_pages']==[63,64]
writet('S01_INTAKE_MEMBER_VALIDATION.tsv',rows,list(rows[0]))
writej('S01_INTAKE_VALIDATION.json',{'schema':'dirichlet-s02-intake-v1','actual_zip':props(zpath),'archive_checks':za,'standalone_checkpoint':props(prior/'CHECKPOINT.json'),'standalone_manifest':props(prior/'MANIFEST.tsv'),'standalone_diff':props(prior/'SOURCE_BACKED_DIFF.tsv'),'bindings':'PASS','accepted_layers_exact':list(range(65,75)),'cursor_validated':2,'input_access_checkpoint_is_current':False,'initial_state_is_current':False,'member_audit':'qa/s02/S01_INTAKE_MEMBER_VALIDATION.tsv','user_local_intake':'User reported successful sequential intake and reader rebuild; this receipt independently verifies actual bytes, not a claim of a new full source collation of S01.'})
packet=R.parent/'DIRICHLET_PAPER_IV_INPUT_PACKAGE(1).zip'
with zipfile.ZipFile(packet) as z:
 pc=safe(z);files=[i for i in z.infolist() if not i.is_dir()];assert len(files)==21
 ir=[]
 for i in files:
  name=PurePosixPath(i.filename).name;b=z.read(i);p=R/'input'/name
  assert p.read_bytes()==b
  ir.append({'file':name,'bytes':len(b),'sha256':digest(b),'packet_to_preserved_input':'BYTE_IDENTICAL'})
checks=list(csv.DictReader((R/'input/91_SHA256SUMS.tsv').open(),delimiter='\t'))
for r in checks:
 p=R/'input'/r['file'];assert p.stat().st_size==int(r['bytes']) and props(p)['sha256']==r['sha256']
writet('INPUT_PRESERVATION.tsv',ir,list(ir[0]))
writej('INPUT_PACKET_VALIDATION.json',{'packet':props(packet),'checks':pc,'files':21,'hash_list_rows_validated':len(checks),'member_byte_equality':'PASS','raw_sources_modified':False,'packet_zip_not_nested_in_cumulative':'Its 21 files are preserved individually; original R27/R28 ZIPs are immutable members.'})
# Verify every R28 regular member against the packet's 97-row inherited member index.
iz=R/'input/13_UNVERIFIED_INHERITED_R28_PAPER_IV_PP075_080.zip';idx=list(csv.DictReader((R/'input/14_UNVERIFIED_INHERITED_MEMBER_INDEX.tsv').open(),delimiter='\t'));im={v['member']:v for v in idx if 'R28_' in v['bundle']}
with zipfile.ZipFile(iz) as z:
 za=safe(z);nm={i.filename for i in z.infolist() if not i.is_dir()};assert len(nm)==51 and nm==set(im)
 rr=[]
 for name in sorted(nm):
  b=z.read(name);p=R/'inherited/R28'/name;assert p.read_bytes()==b
  assert len(b)==int(im[name]['bytes']) and digest(b)==im[name]['sha256']
  rr.append({'member':name,'bytes':len(b),'sha256':digest(b),'index_match':'PASS','unpacked_byte_match':'PASS','original_acceptance':'UNVERIFIED_PRIOR_WORK'})
writet('R28_MEMBER_VALIDATION.tsv',rr,list(rr[0]));writej('R28_ARCHIVE_VALIDATION.json',{'original_archive':props(iz),'archive_checks':za,'index_and_extraction':'PASS_51_FILES','scope_restriction':'Only new/orig/tex and new/en/tex pp75–80 replayed; cumulative earlier-paper readers remain archival, not author-edition input.'})
mp=list(csv.DictReader((R/'input/05_PAGE_MAP.tsv').open(),delimiter='\t'));assert [int(x['printed_page']) for x in mp]==list(range(63,99))
for x in mp: assert int(x['authority_pdf_page_1based'])==int(x['printed_page'])+17 and int(x['scope_pdf_page_1based'])==int(x['printed_page'])-62
full=fitz.open(R/'input/11_AUTHORITY_FULL_DIRICHLET_GESAMMELTE_WERKE_BAND_I_1889.pdf');exact=fitz.open(R/'input/10_AUTHORITY_EXACT_SCOPE_PDF_PAGES_080_115_PRINTED_PP063_098.pdf')
assert len(full)==657 and len(exact)==36
ra=[]
for p in range(74,87):
 a=exact[p-63].get_pixmap(alpha=False);b=full[p+16].get_pixmap(alpha=False)
 assert a.width==b.width and a.height==b.height and a.samples==b.samples
 ra.append({'printed_page':p,'authority_pdf_page':p+17,'scope_leaf':p-62,'dpi':72,'sample_width':a.width,'sample_height':a.height,'projection_samples_sha256':digest(a.samples),'full_volume_samples_sha256':digest(b.samples),'exact_equality':'PASS'})
writet('PAGEWISE_RASTER_EQUIVALENCE.tsv',ra,list(ra[0]))
# R28's six page witnesses: compare embedded images where identity is provable; preserve their different render geometry.
wr=[]
base=R/'inherited/R28/Dirichlet_R28_V1_IVb75_80_20260607'
from PIL import Image
for p in range(75,81):
 png=base/f'src/pages/v1-{p+17:03d}.png';im=Image.open(png)
 wr.append({'printed_page':p,'authority_pdf_page':p+17,'scope_leaf':p-62,'r28_witness':str(png.relative_to(R)),'r28_witness_sha256':props(png)['sha256'],'r28_dimensions':f'{im.width}x{im.height}','controlling_witness':f'qa/s02/source/p{p:03d}_authority.png','replay':'VISUAL_PAGEWISE_CORRESPONDENCE; RAW_R28_NOT_AUTHORITY'})
writet('R28_WITNESS_REPLAY.tsv',wr,list(wr[0]))
controls=[next((R/'input').glob(f'{i:02d}_*')) for i in range(10)]+[R/'input/21_PROMPT_02_PP075_086.md']
writej('INSTRUCTION_READ_RECEIPT.json',{'scope':'Prompt02 only','governing_files_read':[props(p) for p in controls],'precedence':'Controlling authority projection, fixed map, accepted S01 checkpoint; initial zero state is historical, R28 is unverified salvage.','initial_zero_access_checkpoint_not_resumed':True,'prompt03_executed':False})
print('S01 240 actual members and sibling bindings PASS; input packet 21 actual files PASS; R28 51 actual files PASS; source mapping/equality 74–86 PASS.')

# Six R28 witness PNGs are exact grayscale renders of the controlling projection at110dpi.
from PIL import Image
wr=[]
for p in range(75,81):
 f=R/f'inherited/R28/Dirichlet_R28_V1_IVb75_80_20260607/src/pages/v1-{p+17:03d}.png'
 im=Image.open(f);pix=exact[p-63].get_pixmap(matrix=fitz.Matrix(110/72,110/72),colorspace=fitz.csGRAY,alpha=False)
 assert im.size==(pix.width,pix.height) and im.tobytes()==pix.samples
 wr.append({'printed_page':p,'r28_witness':str(f.relative_to(R)),'projection_dpi':110,'pixel_dimensions':f'{pix.width}x{pix.height}','pixel_exact':True,'mean_absolute_pixel_difference':0.0,'source_png_pixels_sha256':digest(im.tobytes()),'projection_pixels_sha256':digest(pix.samples)})
writet('R28_WITNESS_RASTER_COMPARISON.tsv',wr,list(wr[0]))
print('All6 R28 witness PNGs are pixel-identical to the matching authority renders at110dpi.')
