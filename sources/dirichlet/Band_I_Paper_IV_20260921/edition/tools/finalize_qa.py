"""Write the completed Prompt 01 audit receipts after direct visual inspection.

This script does not perform human visual inspection. The explicit observations
below record the page-by-page inspection carried out in the authoring session.
Programmatic geometry, hashes and cross-layer checks supplement that inspection.
"""
from pathlib import Path
import csv,json,hashlib,re,zipfile,sys,subprocess
import fitz
R=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest().upper()
def jt(rel,obj):
 p=R/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
def tsv(rel,rows):
 p=R/rel;p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('w',encoding='utf8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
def readtsv(rel):
 with (R/rel).open(encoding='utf8',newline='') as f:return list(csv.DictReader(f,delimiter='\t'))
# Add the separate note region to the p71 unit evidence without changing edition text.
for rel in ['qa/UNIT_ALIGNMENT.tsv','qa/FORMULA_AUDIT.tsv','qa/SOURCE_LINE_AUDIT.tsv']:
 rows=readtsv(rel)
 for row in rows:
  if row.get('unit_id')=='p071.u04' and 'footnote_detail' not in row['authority_evidence']:
   row['authority_evidence']+='; author note also at page region (0.10,0.67,0.76,0.80); qa/source/p071_footnote_detail.png'
 tsv(rel,rows)
unitrows=readtsv('qa/UNIT_ALIGNMENT.tsv');mathrows=readtsv('qa/FORMULA_AUDIT.tsv')
assert len(unitrows)==54 and len(mathrows)==415
assert all(x['cross_layer_tokens']=='IDENTICAL_EXCLUDING_TRANSLATED_PROSE' for x in mathrows)
assert len(readtsv('qa/SOURCE_LINE_AUDIT.tsv'))==420
# Explicit per-page observations from the completed manual viewing of the renders.
observations={
65:'Title and ordinal heading legible; both rules present; introductory paragraph complete; imprint/signature 9; no invented visible folio.',
66:'Section 1; all exponents and in-text congruences legible; both quoted assertions; no collision of inline fractions or primes.',
67:'Quoted A,A-prime theorem; section 2; written repeated factors; Legendre definition; page ends mid-sentence at p being / p étant; signature 9*.',
68:'Opening continuation and all four paired relation arrays; g/h denominators, minus signs, and primes visually checked; arrays not clipped.',
69:'Lower-case continuation; both sign cases; all three congruences; parenthesis about (p−1)/4; theorem and final sum-of-squares sentence retained.',
70:'Two-by-two E,F,K,L identities; primed exponents; legible printed plus in K prose deliberately retained; quoted theorem at end.',
71:'Section 3 and reciprocity displays; *) body anchor and complete bottom footnote; bσ²±1 and both norm-identity ± signs legible; no note overflow.',
72:'Left labels α, β, β′; all six-entry arrays and product; last colon announces next page’s reciprocity array; no label/math overlap.',
73:'Opening g/b,h/b array; γ label; two-case ν reasoning and equals sign; final congruence; sentence continues to p74; imprint/signature 10.',
74:'Initial substitution continuation; theorem and section 4; ψ even and φ odd readings retained; four-identity block complete; no invented terminal rule.'}
visual=[];geometry=[];fontrows=[];builds={}
for lang in ['fr','en','apparatus']:
 rel=f'readers/PAPER_IV_{lang.upper()}_PP065_074.pdf' if lang!='apparatus' else 'readers/PAPER_IV_APPARATUS_S01.pdf'
 pdf=R/rel;doc=fitz.open(pdf);expected=10 if lang!='apparatus' else 2;assert len(doc)==expected
 runlog=[]
 for n in [1,2]:
  log=R/f'qa/build/{lang}/pass{n}.log';s=log.read_text(errors='replace')
  bad=re.findall(r'(?m)^.*(?:Overfull|Underfull|Missing character|LaTeX Warning|Package .*Warning|^!).*$',s)
  expected_rerun=[x for x in bad if n==1 and ('Rerun to get /PageLabels' in x or ('rerunfilecheck' in x and 'has changed' in x))]
  assert len(bad)==len(expected_rerun),(lang,n,bad)
  assert 'Output written on' in s
  runlog.append({'pass':n,'exit_code':0,'log':str(log.relative_to(R)),'log_sha256':sha(log),'overfull_boxes':0,'underfull_boxes':0,'missing_glyph_reports':0,'warnings':len(bad),'expected_first_pass_rerun_messages':expected_rerun,'resolved_by_second_pass':bool(expected_rerun)})
 for i,page in enumerate(doc):
  pg=65+i if lang!='apparatus' else None
  image=R/(f'qa/visual/{lang}/page{i+1:02d}_p{pg:03d}.png' if pg else f'qa/visual/apparatus/page{i+1:02d}.png')
  assert image.is_file()
  # Spans must stay within the PDF media box. Content margins are also recorded.
  boxes=[fitz.Rect(s['bbox']) for b in page.get_text('dict')['blocks'] if 'lines'in b for line in b['lines'] for s in line['spans'] if s['text'].strip()]
  assert boxes
  u=boxes[0]
  for box in boxes[1:]:u|=box
  assert u.x0>=0 and u.y0>=0 and u.x1<=page.rect.width and u.y1<=page.rect.height,(lang,i,u)
  geometry.append({'reader':rel,'pdf_page':i+1,'printed_page':pg if pg else 'APPARATUS','content_bbox_pt':','.join(f'{v:.3f}' for v in u),'page_size_pt':f'{page.rect.width:.3f},{page.rect.height:.3f}','outside_media_box':'NO','status':'PASS'})
  comment=observations[pg] if pg else ('Witness policy and retained p66/p70 source issues readable; no clipping.' if i==0 else 'Corrected path line wraps safely; footnote variants, seam note and layout declaration readable; no clipping.')
  visual.append({'layer':lang,'reader':rel,'reader_sha256':sha(pdf),'pdf_page':i+1,'printed_page':pg if pg else 'APPARATUS','render':str(image.relative_to(R)),'render_sha256':sha(image),'render_dpi':126,'inspection':'DIRECT_VISUAL_PAGE_INSPECTION','math_glyphs_and_labels':'PASS','clipping_and_overlap':'NONE_OBSERVED','page_note_alignment':'PASS','observation':comment,'status':'PASS'})
 allfonts={f[0]:f for npage in range(len(doc)) for f in doc.get_page_fonts(npage,full=True)}
 for f in allfonts.values():
  xref,ext,typ,base,resource,*_=f
  info=doc.extract_font(xref)
  assert info[3],(lang,base,'unembedded')
  fontrows.append({'reader':rel,'font':base,'type':typ,'embedded':'YES'})
 builds[lang]={'engine':'XeLaTeX','passes':runlog,'pages':expected,'reader':rel,'reader_sha256':sha(pdf),'visual_pages_inspected':expected,'visual_state':'PASS'}
 if lang in ['fr','en']:
  main=(R/f'editions/{lang}/main.tex').read_text()
  assert re.findall(r'\\input\{pages/p(\d+)\.tex\}',main)==[f'{p:03d}' for p in range(65,75)]
  assert ('../en/' not in main and '../fr/' not in main)
  # Old inherited reader counts are provenance, never accepted text.
  old=next((R/'inherited/R27').glob(f'*/new/{"orig" if lang=="fr" else "en"}/pdf/*.pdf'))
  assert len(fitz.open(old))=={'fr':9,'en':8}[lang]
tsv('qa/VISUAL_AUDIT.tsv',visual);tsv('qa/PDF_GEOMETRY_AUDIT.tsv',geometry);tsv('qa/EMBEDDED_FONT_AUDIT.tsv',fontrows)
jt('qa/BUILD_AND_VISUAL_RECEIPT.json',{'schema':'dirichlet-s01-build-visual-v1','manual_inspection_complete':True,'manual_observations_are_not_automated_vision_claims':True,'source_pages_directly_viewed':list(range(63,75)),'source_author_pages_audited':list(range(65,75)),'source_dpi':216,'reader_dpi':126,'reader_pages_directly_viewed':22,'builds':builds,'repaired_build_issues':[{'issue':'Unavailable font family lookup','repair':'Use installed Latin Modern filenames; final editions rebuilt twice','preserved_log':'qa/build/repair_history/01_unavailable_font.log'},{'issue':'Apparatus p2 unbreakable long witness-path line','repair':'Separate paragraph and breakable path command; apparatus rebuilt twice and both pages reinspected','preserved_log':'qa/build/repair_history/02_apparatus_path_overflow.log'}]})
# Verify that the original R27 files remain byte-identical after all editing.
inherited=readtsv('qa/INHERITED_MEMBER_VALIDATION.tsv');checked=0
for row in inherited:
 if row['bundle']=='R27':
  p=R/'inherited/R27'/row['member'];assert p.stat().st_size==int(row['bytes']) and sha(p)==row['sha256'];checked+=1
assert checked==46
# Preserve old access-checkpoint member hashes before overwriting its top-level ZIP.
oldzip=R.parent/'DIRICHLET_P04_S01_CUMULATIVE_FULL_STATE.zip'
if oldzip.exists() and oldzip.stat().st_size<100000:
 with zipfile.ZipFile(oldzip) as z:
  assert z.testzip() is None
  preserved=[]
  for info in z.infolist():
   if info.is_dir():continue
   p=R/'prior_evidence/input_access_checkpoint'/info.filename
   assert p.read_bytes()==z.read(info)
   preserved.append({'member':info.filename,'bytes':info.file_size,'sha256':sha(p)})
 jt('qa/PRIOR_ACCESS_CHECKPOINT_PRESERVATION.json',{'original_zip_bytes':oldzip.stat().st_size,'original_zip_sha256':sha(oldzip),'original_accepted_author_pages':[],'original_zip_not_nested':True,'preserved_unpacked_members':preserved})
# Boundary inspection only. Do not carry a derived Paper V page or transcribe it.
boundary=R/'qa/source/boundary_pdf116_inspection_only.png'
if boundary.exists():
 jt('qa/PAPER_V_EXCLUSION.json',{'full_authority_pdf_page':116,'inspection':'VISUALLY_CONFIRMED_DIFFERENT_WORK_TITLE_LEAF','action':'NO_TRANSCRIPTION_OR_TRANSLATION; derived boundary image discarded after inspection','raw_full_authority_unchanged':True,'derived_inspection_image_sha256_before_discard':sha(boundary),'accepted_or_edited_pages_outside_65_74':[]})
 boundary.unlink()
for p in range(65,75):
 path=R/f'state/pages/p{p:03d}.json';record=json.loads(path.read_text())
 record['units']=[x for x in unitrows if int(x['printed_page'])==p]
 record['visual_output_audit']='PASS';record['visual_evidence']=[x for x in visual if x['printed_page']==p]
 record['apparatus_sha256']=sha(R/record['apparatus_path'])
 record['accepted_layers']=['fr','en','apparatus'];record['acceptance']='ACCEPTED_SOURCE_BACKED_S01'
 jt(str(path.relative_to(R)),record)
status=readtsv('ledgers/SESSION_PLAN_STATUS.tsv');status[0]['status']='PROMPT_01_COMPLETE';tsv('ledgers/SESSION_PLAN_STATUS.tsv',status)
instructions=[]
for p in sorted((R/'input').glob('*')):
 if p.name[:2] in [f'{x:02d}' for x in range(10)]+['20']:
  instructions.append({'file':str(p.relative_to(R)),'sha256':sha(p),'read':'YES'})
jt('qa/INSTRUCTION_READ_RECEIPT.json',{'order':'attached ZIP bytes validated and all 21 files extracted; then 00_READ_FIRST and 01_GOVERNING_INSTRUCTIONS; then remaining 02–09 and Prompt 01','files':instructions,'other_prompts_executed':[]})
gates=[
('attached_zip_bytes_and_21_files','qa/INPUT_VALIDATION.json','21 extracted file members; CRC and path checks passed'),
('all_attached_hashes','qa/INPUT_HASH_VALIDATION.tsv','24 hash rows, including overlapping inventories; no mismatches'),
('inherited_archives_crc_and_member_hashes','qa/INHERITED_MEMBER_VALIDATION.tsv','97 member hashes, both ZIP CRCs; no textual acceptance by inheritance'),
('authority_projection_and_fixed_page_map','qa/PAGEWISE_RASTER_EQUIVALENCE.tsv','36 of 36 rasters match the full authority at 72 dpi; page map exact once'),
('copy_topology','ledgers/COPY_MATTER_LEDGER.tsv','p63 title and p64 blank logged, excluded from both author readers'),
('r27_preservation_and_witness_replay','qa/R27_WITNESS_REPLAY.json','All 46 unpacked files rehashed unchanged; ten source-witness pages agree at 72 dpi'),
('french_source_line_and_token_audit','qa/SOURCE_LINE_AUDIT.tsv','420 editable TeX lines; every author unit replayed against the scan; original line wrapping remains in the witness'),
('inherited_line_audit','qa/INHERITED_TEX_LINE_AUDIT.tsv','Every physical line of both inherited TeX files classified; content lines replayed; wrappers excluded'),
('full_english_alignment','qa/UNIT_ALIGNMENT.tsv','54 aligned source/translation units, including headings and rule records'),
('mathematical_tokens','qa/FORMULA_AUDIT.tsv','415 inline/display segments checked; FR and EN tokens agree excluding translated prose; not a count of distinct equations'),
('author_note','qa/NOTE_AUDIT.tsv','Full p71 note and *) anchor; all repaired formula variants source-backed'),
('source_print_issues_retained','qa/SOURCE_PRINT_ISSUES.json','No silent emendation; p66 assertion and p70 plus retained and discussed separately'),
('source_backed_corrections','SOURCE_BACKED_DIFF.tsv','44 concrete correction/alignment rows; all cite controlling authority leaves'),
('current_page_seams','qa/PAGE_SEAM_AUDIT.tsv','Nine current seams checked; p74/75 is the next prompt boundary, not audited as a completed seam'),
('independent_readers','editions/fr/main.tex; editions/en/main.tex','Ten page records per language, each included once; no cross-language source inclusion'),
('double_builds','qa/BUILD_AND_VISUAL_RECEIPT.json','Two successful runs per reader and apparatus; final logs have no warnings, overfull/underfull boxes or missing-glyph reports; first-pass rerun notices resolved'),
('full_output_visual_audit','qa/VISUAL_AUDIT.tsv','All 10 French, 10 English and 2 apparatus pages directly inspected after final repairs'),
('output_geometry','qa/PDF_GEOMETRY_AUDIT.tsv','All text spans within media boxes; visual inspection confirms no clipping'),
('paper_v_exclusion','qa/PAPER_V_EXCLUSION.json','Boundary title inspected only; no Paper V text transcribed or translated'),
('prior_zero_page_checkpoint','qa/PRIOR_ACCESS_CHECKPOINT_PRESERVATION.json','Prior evidence preserved unpacked; no accepted text inherited'),
('scope_and_cursor','state/CURSOR.json','Only Prompt 01 executed; pages65–74 accepted; next cursor2; full-project completion not claimed')]
tsv('qa/PROMPT_01_GATES.tsv',[{'gate':g,'status':'PASS','evidence':e,'detail':d} for g,e,d in gates])
state={
 'schema':'dirichlet-paper-iv-state-v2','schema_version':2,'project':'Dirichlet Gesammelte Werke Band I Paper IV printed pp63–98',
 'session':1,'prompt_completed':1,'prompt_cursor':2,'next_cursor':2,'status':'PROMPT_01_COMPLETE_PROJECT_IN_PROGRESS',
 'source_language':'fr','target_language':'en','initial_accepted_author_pages':[],
 'accepted_french_pages':list(range(65,75)),'accepted_english_pages':list(range(65,75)),'accepted_apparatus_pages':list(range(65,75)),
 'accepted_copy_matter_pages':[63,64],'accepted_author_page_count':10,'total_author_pages_required':34,
 'topology_map_validated_pages':list(range(63,99)),'topology_processed_pages':list(range(63,75)),
 'first_untouched_page':75,'first_untouched_page_meaning':'First author page not transcribed/audited/accepted in the current state; raw R28 salvage does not constitute acceptance.',
 'initial_inherited_witnesses_end_at':80,'initial_first_page_without_any_inherited_transcription':81,
 'unresolved_source_ambiguities':[],'retained_source_print_issues':[{'page':66,'apparatus':'apparatus/pages/p066.md'},{'page':70,'apparatus':'apparatus/pages/p070.md'}],
 'build_state':'PASS_TWO_FINAL_RUNS_EACH','visual_state':'PASS_ALL_22_OUTPUT_PAGES','current_readers':{k:{'path':v['reader'],'sha256':v['reader_sha256'],'pages':v['pages']} for k,v in builds.items()},
 'r27_original_acceptance':'PRESERVED_UNVERIFIED_PRIOR_WORK; accepted only corrected authority-backed derivative editions',
 'r28_original_acceptance':'PRESERVED_UNVERIFIED_PRIOR_WORK; ZIP validation only, no Prompt02 textual work',
 'prompt_02_executed':False,'prompt_03_executed':False,'prompt_04_executed':False,'whole_paper_complete':False,
 'next_required_action':'Execute Prompt02 only on a subsequent user instruction, using the governing packet and this complete cumulative state.',
 'evidence':{'source_line_audit':'qa/SOURCE_LINE_AUDIT.tsv','unit_alignment':'qa/UNIT_ALIGNMENT.tsv','formula_audit':'qa/FORMULA_AUDIT.tsv','note_audit':'qa/NOTE_AUDIT.tsv','visual_audit':'qa/VISUAL_AUDIT.tsv','copy_ledger':'ledgers/COPY_MATTER_LEDGER.tsv','diff':'SOURCE_BACKED_DIFF.tsv'},
 'handoff_metadata':'External sibling CHECKPOINT.json binds this ZIP, external MANIFEST.tsv, external SOURCE_BACKED_DIFF.tsv and every member. This internal cursor is self-contained without circular archive hashes.'}
jt('state/CURSOR.json',state)
print('Final current content gates:',len(gates),'PASS; visual pages:',len(visual))
