"""Record the completed manual page inspections and verify all mechanical S02 gates.
Manual observations are authored evidence, not a claim that this script can inspect print.
"""
from pathlib import Path
import csv,json,hashlib,re,subprocess,zipfile
import fitz
R=Path(__file__).resolve().parents[2];Q=R/'qa/s02'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest().upper()
def rts(p):return list(csv.DictReader(p.open(),delimiter='\t'))
def wt(p,rows):
 p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
def wj(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
obs={
75:'Continuation of section4, all five displays; δ and δ′ aligned, paired opposite signs and prime on u legible; original folio/running head and 10* signature; no added R28 title.',
76:'Both χ choices, two occurrences of the repeated product identity, all six display blocks and final alternatives remain on source p76; no fractional collisions or clipping.',
77:'Third product-identity occurrence and divisible case; printed t in the 8n+7/8n+3 sentence retained; whole auxiliary theorem and cδ relation; final clause ends at values/valeurs.',
78:'Opening continuation of b/de b; entire table discussion incl136 and79; mixed-case Theorem I; both divisibility cases and two full corollaries; final etc.; no clipped inline symbols.',
79:'Section5, ν superscript and every g/h factor; ε brace, three further two-row arrays and product; primes and all minus signs legible; page ends with h, without bridge text.',
80:'Opening h-prime,h-double-prime list; ζ brace with six ±1 entries; all sign-count/inversion reasoning and both terminal t-symbol cases; no source paragraph omitted.',
81:'η pair and θ alternatives, all exponent sums legible; full decomposition and two-by-two E/F/K/L block; footer imprint/signature11; no label overlap.',
82:'Complete parity argument; printed p² retained; primed factors and all four display blocks with correct numerator order and exponent order; no note inserted into author body.',
83:'Both comparison alternatives, root χ congruences, repeated equivalent product conditions, divisible case and 2t result; footer11*; last sentence continues after which is the/ce qui est la.',
84:'Opening same-thing/même-chose continuation; entire general extension argument; mixed-case Theorem II and complete quoted conditions; a=5,a=13 examples and quadratic-divisor statement.',
85:'Complete quoted 5-corollary, both methodological paragraphs; printed ps without exponent retained; source long and short rules bracket Addition heading; first Addition sentence remains open at page end.',
86:'Local α′ label and whole existence/parity/primed-solution argument; reference back to author note on p71; both final reciprocity rows have printed four-dot endings; no fabricated terminal rule or next-page text.'}
visual=[];geom=[];fonts=[];reg=[];builds={}
for layer in ['fr','en','apparatus']:
 rel=f'readers/PAPER_IV_{layer.upper()}_PP065_086.pdf' if layer!='apparatus' else 'readers/PAPER_IV_APPARATUS_S02.pdf'
 pdf=R/rel;doc=fitz.open(pdf);count=22 if layer!='apparatus' else 3;assert len(doc)==count
 logs=[]
 for n in [1,2]:
  p=R/f'qa/s02/build/{layer}/pass{n}.log';s=p.read_text()
  bad=re.findall(r'^.*(?:Overfull|Underfull|Missing character|Warning|^!).*$',s,re.M)
  assert not bad,(layer,n,bad);assert 'Output written on' in s
  logs.append({'pass':n,'exit_code':0,'log':str(p.relative_to(R)),'sha256':sha(p),'warning_count':0,'overfull_count':0,'underfull_count':0,'missing_glyph_count':0})
 if layer!='apparatus':
  old=fitz.open(R/f'readers/PAPER_IV_{layer.upper()}_PP065_074.pdf')
  main=(R/f'editions/{layer}/main.tex').read_text();assert re.findall(r'\\input\{pages/p(\d+)\.tex\}',main)==[f'{p:03d}' for p in range(65,87)]
  assert len(doc.get_toc())==22
  for i in range(10):
   a=doc[i].get_pixmap(matrix=fitz.Matrix(1.75,1.75),alpha=False);b=old[i].get_pixmap(matrix=fitz.Matrix(1.75,1.75),alpha=False)
   assert a.samples==b.samples and a.width==b.width and a.height==b.height
   assert doc[i].get_text()==old[i].get_text()
   for root in ['editions/'+layer+'/pages','apparatus/pages','state/pages']:
    ext='tex' if root.startswith('editions') else ('md' if root.startswith('apparatus') else 'json')
    name=f'{root}/p{i+65:03d}.{ext}';
    with zipfile.ZipFile(R.parent/'DIRICHLET_P04_S01_CUMULATIVE_FULL_STATE.zip') as z:assert (R/name).read_bytes()==z.read(name)
   reg.append({'layer':layer,'printed_page':i+65,'current_reader':rel,'s01_reader':f'readers/PAPER_IV_{layer.upper()}_PP065_074.pdf','render_dpi':126,'width':a.width,'height':a.height,'current_pixel_sha256':hashlib.sha256(a.samples).hexdigest().upper(),'s01_pixel_sha256':hashlib.sha256(b.samples).hexdigest().upper(),'text_equal':'PASS','raster_equal':'PASS','page_source_apparatus_record_byte_identity':'PASS'})
 for i,page in enumerate(doc):
  p=i+65 if layer!='apparatus' else None
  image=R/(f'qa/s02/visual/{layer}/page{i+1:02d}_p{p:03d}.png' if p else f'qa/s02/visual/apparatus/page{i+1:02d}.png');assert image.is_file()
  boxes=[fitz.Rect(s['bbox']) for b in page.get_text('dict')['blocks'] if 'lines'in b for line in b['lines'] for s in line['spans'] if s['text'].strip()]
  assert boxes;bb=fitz.Rect(boxes[0])
  for box in boxes[1:]:bb|=box
  assert bb.x0>=0 and bb.y0>=0 and bb.x1<=page.rect.width and bb.y1<=page.rect.height,(layer,i,bb)
  geom.append({'reader':rel,'pdf_page':i+1,'printed_page':p or 'APPARATUS','content_bbox_pt':','.join(f'{v:.3f}' for v in bb),'page_size_pt':f'{page.rect.width:.3f},{page.rect.height:.3f}','outside_media_box':'NO','status':'PASS'})
  if p and p<=74:
   a=65+2*((p-65)//2);sheet=f'qa/s02/visual/regression_sheets/{layer}_pp{a:03d}_{a+1:03d}.png'
   method='VISUAL_REVIEW_OF_CURRENT_RENDER_PAIR_SHEET_AND_EXACT_PIXEL_REGRESSION';comment='All visible layout and page furniture retained. Current extracted text and full 126dpi raster are identical to accepted S01. This is a regression check, not a new independent cold source collation.'
  elif p:sheet='';method='DIRECT_INDIVIDUAL_FINAL_PAGE_VISUAL_INSPECTION';comment=obs[p]
  else:
   sheet='';method='DIRECT_INDIVIDUAL_FINAL_PAGE_VISUAL_INSPECTION';comment=['Current witness and translation policy; preserved p66 and p70 source issues; no clipping or overflow.','p71 note discussion; current continuation to p86; source-layout declaration and pending cold audit; no clipped paths or text.','Separate p77 t, p82 p² and p85 ps observations; exact label/seam/footnote/signature notes; no overflow or author-body emendation.'][i]
  visual.append({'layer':layer,'reader':rel,'reader_sha256':sha(pdf),'pdf_page':i+1,'printed_page':p or 'APPARATUS','render':str(image.relative_to(R)),'render_sha256':sha(image),'render_dpi':126,'inspection':method,'supplementary_review_sheet':sheet,'math_glyphs_and_labels':'PASS','clipping_and_overlap':'NONE_OBSERVED','page_note_alignment':'PASS','observation':comment,'status':'PASS'})
 allfonts={x[0]:x for page in doc for x in page.get_fonts(full=True)}
 for x in allfonts.values():
  assert doc.extract_font(x[0])[3],(layer,x)
  fonts.append({'reader':rel,'font':x[3],'type':x[2],'embedded':'YES','font_file_shared':'NO'})
 (Q/f'PDFFONTS_{layer.upper()}.txt').write_text(subprocess.run(['pdffonts',str(pdf)],capture_output=True,text=True,check=True).stdout)
 # Preserve searchable text only for author/apparatus readers, never substitute it for scan collation.
 (Q/f'EXTRACTED_TEXT_{layer.upper()}.txt').write_text('\f'.join(page.get_text() for page in doc))
 builds[layer]={'engine':'XeLaTeX','passes':logs,'pages':count,'reader':rel,'reader_sha256':sha(pdf),'rendered_pages':count,'visual_pages_reviewed':count,'visual_status':'PASS'}
wt(Q/'VISUAL_AUDIT.tsv',visual);wt(Q/'PDF_GEOMETRY_AUDIT.tsv',geom);wt(Q/'EMBEDDED_FONT_AUDIT.tsv',fonts);wt(Q/'S01_READER_REGRESSION.tsv',reg)
(Q/'XELATEX_VERSION.txt').write_text(subprocess.run(['xelatex','--version'],capture_output=True,text=True,check=True).stdout)
wj(Q/'BUILD_AND_VISUAL_RECEIPT.json',{'schema':'dirichlet-s02-build-visual-v1','source_author_pages_manually_audited':list(range(75,87)),'source_seam_page_rechecked':74,'source_dpi':216,'render_dpi':126,'manual_inspection_complete':True,'added_affected_output_pages_individually_viewed':27,'unchanged_s01_output_pages_reviewed_in_pair_sheets':20,'total_current_output_pages_rendered_and_reviewed':47,'old_output_regression':'All20 prior author reader pages exactly match accepted S01 text and 126dpi pixels. No new independent full source collation is claimed for S01 here.','manual_observations_are_not_automated_vision_claims':True,'builds':builds,'repaired_draft_issues':[{'issue':'LaTeX tag math-mode error','repair':'Put mathematical label inside math mode in tag; all final runs clean.','evidence':'qa/s02/build/repair_history/01_tag_math_mode.log'},{'issue':'Missing source terminal dot after two ellipses on p86 in first draft','repair':'Restore both dots in French and English; rebuild each twice; both final p86 pages individually re-inspected.','evidence':'qa/s02/source/p086_reciprocity_detail.png'}]})
# Note anchors and retained print discrepancies remain outside the author text.
notes=[{'printed_page':71,'role':'AUTHOR_NOTE_CARRIED_FROM_S01','anchor':'*)','body':'Complete author note remains byte-identical in each edition and pixel-identical in each cumulative reader.','evidence':'qa/NOTE_AUDIT.tsv; qa/s02/S01_READER_REGRESSION.tsv','status':'PASS'}]
for p in range(75,87):notes.append({'printed_page':p,'role':'NO_NEW_AUTHOR_NOTE','anchor':'NONE','body':'Explicit cross-reference to the note near the start of section3 on p71 retained; no duplicate note inserted.' if p==86 else 'No author footnote or anchor on controlling leaf; no editorial note inserted into body.','evidence':f'qa/s02/source/p{p:03d}_authority.png','status':'PASS'})
wt(Q/'NOTE_AUDIT.tsv',notes)
issues=[{'printed_page':77,'reading':'t in the 8n+7/8n+3 sentence','detail':'qa/s02/source/p077_variable_t_detail.png','apparatus':'apparatus/pages/p077.md','disposition':'LEGIBLE_PRINT_RETAINED_IN_BOTH_EDITIONS','ambiguity':False}, {'printed_page':82,'reading':'p²=φ²+ψ²','detail':'qa/s02/source/p082_p_squared_detail.png','apparatus':'apparatus/pages/p082.md','disposition':'LEGIBLE_PRINT_RETAINED_IN_BOTH_EDITIONS','ambiguity':False}, {'printed_page':85,'reading':'t²+au²=ps (no superscript on s)','detail':'qa/s02/source/p085_unsquared_s_detail.png','apparatus':'apparatus/pages/p085.md','disposition':'LEGIBLE_PRINT_RETAINED_IN_BOTH_EDITIONS','ambiguity':False}]
wj(Q/'SOURCE_PRINT_ISSUES.json',{'new_issues':issues,'prior_issues_retained':[66,70],'editorial_emendations_in_author_readers':[],'unresolved_source_ambiguities':[]})
# Every seam has direct source and structural translation evidence.
seamdata={
(74,75):('φ′²+bu′²=KL.','Il est très facile de s’assurer','Section4 factor block is followed by E/F coprimality, not a new title. Existing p74 source unchanged.'),
(75,76):('(δ′): t±ψ≡0 (mod.b), ((t∓ψ)/b)=1.','Il résulte du théorème énoncé','The next page uses the preceding section3 theorem and δ results.'),
(76,77):('(t/b)=1 ou (t/b)=−1.','Il suffira de chercher','Prose explains how to decide the just-stated alternatives.'),
(77,78):('pour toutes les valeurs','de b, telles que','Single source paragraph split; no full stop or bridge added.'),
(78,79):('etc.','5. / Désignons par a','Section5 begins on the next printed page.'),
(79,80):('les nombres premiers h,',"h′, h″, … sont en nombre pair ou impair.",'Prime-factor list split after the unprimed h, with comma.'),
(80,81):('(t/p)=−(t/a).','Ces deux cas sont compris','Both preceding t parity cases reunited in η; no formula omitted or repeated.'),
(81,82):('(E/a)=1, (F/a)=1.','La différence des nombres impairs','Squared E,F factors lead to the following parity argument.'),
(82,83):('((ψ+t)/a)=((ψ−t)/a)=(−1)^((p−1)/4+(t−1)/2).','Si l’on compare','Next leaf compares this result with θ; numerator order remains ψ±t.'),
(83,84):('ou, ce qui est la','même chose, d’après un théorème connu','Single sentence split, no inserted punctuation.'),
(84,85):('étant lui-même de la forme t²−au².','„p désignant un nombre premier','Announced particular theorem follows on next leaf.'),
(85,86):('ces démonstrations étant susceptibles d’être beaucoup','simplifiées au moyen','Addition introductory sentence continues, no bridge text or capitalized restart.')}
sr=[]
for (a,b),(end,start,note) in seamdata.items():sr.append({'from_printed_page':a,'to_printed_page':b,'authority_pdf_pages':f'{a+17};{b+17}','source_end':end,'source_start':start,'french':'EXACT_SOURCE_BREAK_RETAINED','english':'BREAK_AT_CORRESPONDING_FULL_ARGUMENT_POSITION','evidence':f'qa/s02/source/p{a:03d}_authority.png; qa/s02/source/p{b:03d}_authority.png','observation':note,'status':'PASS'})
wt(Q/'PAGE_SEAM_AUDIT.tsv',sr)
wj(Q/'SESSION_BOUNDARY.json',{'last_processed_printed_page':86,'last_processed_full_pdf_page':103,'last_processed_scope_leaf':24,'last_body':'reciprocity row ending (k″/p)=1, four dots','first_untouched_printed_page':87,'first_untouched_full_pdf_page':104,'first_untouched_scope_leaf':25,'prompt03_executed':False,'paper_v_excluded':True,'raw_full_volume_preserved':True,'paper_v_boundary_evidence_carried':'qa/PAPER_V_EXCLUSION.json','no_author_source_created_outside_65_86':True})
# Write source-backed page records' final visual bindings; prior records untouched.
for p in range(75,87):
 f=R/f'state/pages/p{p:03d}.json';j=json.loads(f.read_text());j['acceptance']='ACCEPTED_SOURCE_BACKED_S02';j['visual_output_audit']='PASS';j['visual_evidence']=[v for v in visual if v['printed_page']==p];j['build_receipt']='qa/s02/BUILD_AND_VISUAL_RECEIPT.json';wj(f,j)
# Update only cumulative ledgers; their S01 bytes were saved before modification.
t=rts(R/'prior_evidence/S01/ledgers/TOPOLOGY.tsv')
for row in t:
 p=int(row['printed_page'])
 if 75<=p<=86:
  for k in ['fr_status','en_status','apparatus_status']:row[k]='ACCEPTED_S02'
  row['occurrences_in_each_current_reader']='1'
wt(R/'ledgers/TOPOLOGY.tsv',t)
s=rts(R/'prior_evidence/S01/ledgers/SESSION_PLAN_STATUS.tsv');s[1]['status']='PROMPT_02_COMPLETE';wt(R/'ledgers/SESSION_PLAN_STATUS.tsv',s)
f=rts(R/'prior_evidence/S01/ledgers/PAGE_FURNITURE.tsv')
for p in range(75,87):f.append({'printed_page':p,'folio_as_printed':p,'running_head_as_printed':"D’UNE CLASSE DE FORMULES DU QUATRIÈME DEGRÉ." if p%2 else 'RECHERCHES SUR LES DIVISEURS PREMIERS','imprint_as_printed':'G. Lejeune Dirichlet’s Werke.' if p==81 else '', 'signature_as_printed':{75:'10*',81:'11',83:'11*'}.get(p,''),'rules':'long rule before Addition heading; short rule below heading' if p==85 else '', 'evidence':f'qa/s02/source/p{p:03d}_authority.png','disposition':'FR furniture reproduced; EN running heads and imprint translated; no additional author page counted'})
wt(R/'ledgers/PAGE_FURNITURE.tsv',f)
for name in ['UNIT_ALIGNMENT.tsv','FORMULA_AUDIT.tsv']:
 a=rts(R/'qa'/name);b=rts(Q/name);wt(Q/('CUMULATIVE_'+name),a+b)
a=rts(R/'qa/SOURCE_LINE_AUDIT.tsv');b=rts(Q/'SOURCE_LINE_AUDIT.tsv');a=[{k:('fr' if k=='layer' else row[k]) for k in b[0]} for row in a];wt(Q/'CUMULATIVE_SOURCE_LINE_AUDIT.tsv',a+b)
c=json.loads((Q/'CONTENT_AUDIT_COUNTS.json').read_text());assert c['aligned_units']==85 and c['paired_math_segments']==499
assert len(rts(Q/'CUMULATIVE_UNIT_ALIGNMENT.tsv'))==139 and len(rts(Q/'CUMULATIVE_FORMULA_AUDIT.tsv'))==914
assert len(rts(R/'SOURCE_BACKED_DIFF.tsv'))==70
assert len(rts(R/'apparatus/CATALOGUE.tsv'))==22
assert all([int(x['printed_page']) for x in rts(R/'apparatus/CATALOGUE.tsv')]==list(range(65,87)) for _ in [0])
gates=[]
def g(name,evidence,note):gates.append({'gate':name,'status':'PASS','evidence':evidence,'note':note})
g('ACCEPTED_S01_ACTUAL_BYTES','qa/s02/S01_INTAKE_VALIDATION.json','Correct131808818-byte S01 archive; all240 member and sibling hashes; exact65–74 acceptance and cursor2.')
g('IMMUTABLE_INPUTS','qa/s02/INPUT_PRESERVATION.tsv','All21 packet members unchanged; raw authority and both inherited ZIPs preserved.')
g('R28_PAGEWISE_REPLAY','qa/s02/INHERITED_TEX_LINE_AUDIT.tsv','All396 lines of two inherited editable files classified; 50 author/structure units per language replayed against92–97; no cumulative earlier-paper content ingested.')
g('DIRECT_SOURCE_81_86','qa/s02/UNIT_ALIGNMENT.tsv','All six untouched leaves transcribed and translated from attached authority; no external text/OCR substituted.')
g('FULL_BILINGUAL_MATH','qa/s02/FORMULA_AUDIT.tsv','499 paired new inline/display segments token-checked after visual source review; all85 new units aligned.')
g('SOURCE_ERRORS_NOT_SILENTLY_REPAIRED','qa/s02/SOURCE_PRINT_ISSUES.json','Legible t,p²,ps readings retained in both editions; apparatus separate; no illegible-source uncertainty.')
g('CUMULATIVE_EXACT_ONCE','ledgers/TOPOLOGY.tsv','Both readers22 pages65–86; apparatus22 page records; copy63–64 excluded,87–98 untouched.')
g('OLD_ACCEPTANCE_PRESERVED','qa/s02/S01_READER_REGRESSION.tsv','Old page sources, apparatus page notes, state pages byte-identical;20 old output pages text/pixel-identical.')
g('SEAMS_AND_NOTES','qa/s02/PAGE_SEAM_AUDIT.tsv; qa/s02/NOTE_AUDIT.tsv','74/75,80/81 and all intermediate joins reviewed. Author note71 retained; no new footnotes75–86.')
g('SIX_CLEAN_FINAL_BUILDS','qa/s02/BUILD_AND_VISUAL_RECEIPT.json','Two XeLaTeX passes per current FR/EN/apparatus;22/22/3 pages; all six final runs without warnings, overfull/underfull boxes or missing glyphs.')
g('ALL_CURRENT_OUTPUT_PAGES_REVIEWED','qa/s02/VISUAL_AUDIT.tsv','27 added/affected pages individually inspected;20 unchanged pages reviewed in pair sheets and exactly regressed; all47 rendered.')
g('CURSOR_3_ONLY','qa/s02/SESSION_BOUNDARY.json','Stops at printed86; next87. Prompt03 and final cold audit remain unexecuted.')
wt(Q/'PROMPT_02_GATES.tsv',gates)
prev=json.loads((R/'prior_evidence/S01/state/CURSOR.json').read_text());state=dict(prev)
state.update({'session':2,'prompt_completed':2,'prompt_cursor':3,'next_cursor':3,'status':'PROMPT_02_COMPLETE_PROJECT_IN_PROGRESS','accepted_french_pages':list(range(65,87)),'accepted_english_pages':list(range(65,87)),'accepted_apparatus_pages':list(range(65,87)),'accepted_author_page_count':22,'topology_processed_pages':list(range(63,87)),'first_untouched_page':87,'first_untouched_page_meaning':'First author page not transcribed/audited/accepted in the current sequential state.','retained_source_print_issues':[{'page':p,'apparatus':f'apparatus/pages/p{p:03d}.md'} for p in [66,70,77,82,85]],'build_state':'PASS_TWO_FINAL_RUNS_EACH_ALL_SIX_CLEAN','visual_state':'PASS_ALL_47_CURRENT_OUTPUT_PAGES','current_readers':{l:{'path':b['reader'],'sha256':b['reader_sha256'],'pages':b['pages']} for l,b in builds.items()},'r28_original_acceptance':'PRESERVED_UNVERIFIED_PRIOR_WORK; only pagewise source-confirmed corrected derivative pp75–80 accepted','prompt_02_executed':True,'prompt_03_executed':False,'prompt_04_executed':False,'whole_paper_complete':False,'next_required_action':'Execute Prompt03 only after a subsequent user instruction, starting at printed87 / full PDF104 / scope leaf25. Final cold audit remains required.','previous_accepted_release':{'file':'DIRICHLET_P04_S01_CUMULATIVE_FULL_STATE.zip','bytes':131808818,'sha256':'DEE2786989BCE3556912265B110856DB4578181386E322E4FC97CE64D583F162','nested_in_this_release':False},'evidence':{'intake':'qa/s02/S01_INTAKE_VALIDATION.json','source_line_audit':'qa/s02/CUMULATIVE_SOURCE_LINE_AUDIT.tsv','unit_alignment':'qa/s02/CUMULATIVE_UNIT_ALIGNMENT.tsv','formula_audit':'qa/s02/CUMULATIVE_FORMULA_AUDIT.tsv','note_audit':'qa/s02/NOTE_AUDIT.tsv','visual_audit':'qa/s02/VISUAL_AUDIT.tsv','copy_ledger':'ledgers/COPY_MATTER_LEDGER.tsv','diff':'SOURCE_BACKED_DIFF.tsv','seam_audit':'qa/s02/PAGE_SEAM_AUDIT.tsv','gates':'qa/s02/PROMPT_02_GATES.tsv'},'cold_audit_state':'NOT_EXECUTED_REQUIRED_AFTER_PROMPT03'})
wj(R/'state/CURSOR.json',state)
print('S02 gates PASS; source units85; paired math499; cumulative139 units/914 math segments; current visual47 pages; next cursor3.')
