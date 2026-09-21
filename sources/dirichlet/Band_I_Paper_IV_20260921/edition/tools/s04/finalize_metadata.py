"""Finalize current records only after the actual manual audit and output review.
Preserve every replaced S03 file. Historical evidence is never relabelled as current.
"""
from pathlib import Path
import csv,json,re,zipfile,shutil
from audit_support import R,Q,h,preserve

def readj(p):return json.loads((R/p).read_text())
def writej(p,d):
 path=R/p;path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def rows(p):return list(csv.DictReader((R/p).open(),delimiter='\t'))
def writetsv(p,rr,keys=None):
 with (R/p).open('w') as f:
  w=csv.DictWriter(f,fieldnames=keys or list(rr[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rr)
def binding(p):
 b=(R/p).read_bytes();return {'path':p,'bytes':len(b),'sha256':h(b)}

manual=readj('qa/s04/MANUAL_COLD_COLLATION.json');review=readj('qa/s04/MANUAL_OUTPUT_REVIEW.json')
build=readj('qa/s04/BUILD_RUNS.json');mechanical=readj('qa/s04/GLOBAL_CHECKS.json');preflight=readj('qa/s04/OUTPUT_PREFLIGHT.json')
repairs=readj('qa/s04/REPAIRS.json');units=rows('qa/s04/UNIT_ALIGNMENT.tsv');old_manifest=rows('history/S03/MANIFEST.tsv')
assert sorted(map(int,manual))==list(range(63,99));assert len(review)==73
assert not mechanical['mismatches'] and mechanical['aligned_units']==200
assert preflight['all_final_six_build_passes_clean'] and not preflight['unexpected_page_regressions']
assert len(rows('qa/s04/ALL_AUTHOR_SEAMS.tsv'))==33
assert len(rows('SOURCE_BACKED_DIFF.tsv'))==72+len(repairs)==93
assert (R/'SOURCE_BACKED_DIFF.tsv').read_bytes().startswith((R/'history/S03/SOURCE_BACKED_DIFF_CANONICAL.tsv').read_bytes())

# Trace each concrete repair through saved immediate-before bytes and the final file.
rr=[]
for e in repairs:
 prior=(R/e['snapshot']).read_text();current=(R/e['file']).read_text()
 assert prior.count(e['before'])==e['occurrences']
 assert e['after'] in current,(e['id'],'after absent')
 assert (R/f"qa/s04/source/p{int(e['printed_page']):03}_authority.png").exists()
 rr.append({'id':e['id'],'printed_page':e['printed_page'],'file':e['file'],'before_snapshot':e['snapshot'],'before_snapshot_sha256':h((R/e['snapshot']).read_bytes()),'current_sha256':h((R/e['file']).read_bytes()),'after_present':True,'source_locator':e['evidence'],'status':'REPAIR_INTEGRATED_AND_RECHECKED'})
writetsv('qa/s04/REPAIR_VERIFICATION.tsv',rr)
writetsv('qa/s04/SOURCE_BACKED_DIFF_S04.tsv',repairs,['printed_page','authority_pdf_page','layer','before','after','evidence','disposition']) if False else None
# Deliberately project only contract columns, without repair helper metadata.
keys=['printed_page','authority_pdf_page','layer','before','after','evidence','disposition']
writetsv('qa/s04/SOURCE_BACKED_DIFF_S04.tsv',[{k:e[k] for k in keys} for e in repairs])

# Fresh scope identity and exact-once topology, including the two excluded copy leaves.
inputmap=rows('input/05_PAGE_MAP.tsv');rasters=rows('qa/s04/SCOPE_RASTER_EQUIVALENCE.tsv')
assert len(inputmap)==len(rasters)==36
top=[];audit=[]
for p,row,ras in zip(range(63,99),inputmap,rasters):
 assert int(row['printed_page'])==int(ras['printed_page'])==p
 assert int(row['authority_pdf_page_1based'])==int(ras['full_pdf_page'])==p+17
 assert int(row['scope_pdf_page_1based'])==int(ras['scope_leaf'])==p-62
 assert h((R/ras['image_path']).read_bytes())==ras['image_sha256']
 assert ras['result']=='IDENTICAL_216DPI'
 m=manual[str(p)];assert m['observations'] and m['mathematical_token_review']
 top.append({'printed_page':p,'authority_pdf_page':p+17,'scope_leaf':p-62,'role':'COPY_MATTER' if p<65 else 'AUTHOR_TEXT','fr_status':'COPY_LOGGED_COLD_REPLAYED' if p<65 else 'COLD_AUDIT_ACCEPTED_S04','en_status':'COPY_LOGGED_COLD_REPLAYED' if p<65 else 'COLD_AUDIT_ACCEPTED_S04','apparatus_status':'COPY_LOGGED_COLD_REPLAYED' if p<65 else 'COLD_AUDIT_ACCEPTED_S04','occurrences_in_each_current_reader':0 if p<65 else 1})
 audit.append({'printed_page':p,'full_pdf_page':p+17,'scope_leaf':p-62,'role':row['role'],'source_image':ras['image_path'],'source_image_sha256':ras['image_sha256'],'manual_record':f'qa/s04/MANUAL_COLD_COLLATION.json#/{p}','scope_replay':'COMPLETE','author_reader_occurrences':0 if p<65 else 1})
preserve('ledgers/TOPOLOGY.tsv');writetsv('ledgers/TOPOLOGY.tsv',top)
writetsv('qa/s04/COLD_SCOPE_REPLAY.tsv',audit)
copy=rows('ledgers/COPY_MATTER_LEDGER.tsv');preserve('ledgers/COPY_MATTER_LEDGER.tsv')
for d in copy:
 p=int(d['printed_page']);d['evidence']=f'qa/s04/source/p{p:03}_authority.png; qa/s04/MANUAL_COLD_COLLATION.json#/{p}';d['status']='COLD_REPLAYED_S04_EXCLUDED_FROM_AUTHOR_READERS'
writetsv('ledgers/COPY_MATTER_LEDGER.tsv',copy)
assert (R/'copy_matter/p064.txt').stat().st_size==0
furniture=rows('ledgers/PAGE_FURNITURE.tsv');preserve('ledgers/PAGE_FURNITURE.tsv')
for d in furniture:
 p=int(d['printed_page']);d['evidence']=f'qa/s04/source/p{p:03}_authority.png; qa/s04/MANUAL_COLD_COLLATION.json#/{p}'
writetsv('ledgers/PAGE_FURNITURE.tsv',furniture)
plan=rows('ledgers/SESSION_PLAN_STATUS.tsv');preserve('ledgers/SESSION_PLAN_STATUS.tsv')
plan[2]['status']='PROMPT_03_COMPLETE_SUPERSEDED_BY_FINAL_COLD_AUDIT'
plan[3]['status']='PROMPT_04_COMPLETE_ALL_GATES';plan[3]['next_cursor']='COMPLETE'
writetsv('ledgers/SESSION_PLAN_STATUS.tsv',plan)

# Current page records point exclusively to final sources/readers and current manual audit.
for p in range(65,99):
 rel=f'state/pages/p{p:03}.json';preserve(rel);old=readj(rel);m=manual[str(p)]
 rec={'schema':'dirichlet-page-record-v3','schema_version':3,'printed_page':p,'authority_pdf_page':p+17,'scope_leaf':p-62,'role':'AUTHOR_TEXT_FRENCH','origin':old.get('origin','SOURCE_REPLAYED_INHERITED_DERIVATIVE' if p<=80 else 'DIRECT_AUTHORITY_TRANSCRIPTION'),'source_image':m['source_image'],'source_image_sha256':h((R/m['source_image']).read_bytes()),'french':binding(f'editions/fr/pages/p{p:03}.tex'),'english':binding(f'editions/en/pages/p{p:03}.tex'),'apparatus':binding(f'apparatus/pages/p{p:03}.md'),'units':[u for u in units if int(u['printed_page'])==p],'manual_cold_collation':m,'notes':m['notes_and_anchors'],'source_ambiguities':[],'accepted_layers':['fr','en','apparatus'],'source_audit':'INDEPENDENT_COLD_SCAN_COLLATION_COMPLETE_S04','english_alignment':'COMPLETE_STRUCTURAL_CORRESPONDENCE_COLD_REVIEWED','acceptance':'COLD_AUDIT_ACCEPTED_S04','cold_audit':'COMPLETE','source_backed_repairs':[e['id'] for e in repairs if int(e['printed_page'])==p],'visual_output_audit':'ALL_CURRENT_PAGE_IMAGES_INDIVIDUALLY_REVIEWED','visual_evidence':[review[f'{l}:{p-64}'] for l in ['fr','en']],'build_receipt':'qa/s04/BUILD_RUNS.json','superseded_s03_record':f'history/S03/superseded/{rel}','locator_note':'TeX line/unit indices locate current editable sources, not physical scan-line counts. The manual collation read physical source lines and tokens directly.'}
 writej(rel,rec)

# Note and anomaly review distinguish printed readings from explanations and inherited errors.
issues=[(66,'unqualified converse for B','Unrestricted printed statement retained; square-factor counterexample is editorial.'),(70,'plus in prose φ′²+2u′²','Literal plus retained despite earlier minus in the factorization.'),(77,'t in the residue-class sentence','Literal t retained; theorem I on p.78 says b.'),(82,'p²=φ²+ψ²','Literal superscript on p retained.'),(85,'t²+au²=ps','Literal unsquared s retained in the parenthesis.'),(89,'ψ is not divisible by b','Literal b restored; inferred intended δ belongs only in apparatus.')]
writej('qa/s04/RETAINED_SOURCE_ISSUES.json',{'issues':[{'printed_page':p,'full_pdf_page':p+17,'scope_leaf':p-62,'reading':reading,'treatment':treatment,'apparatus':f'apparatus/pages/p{p:03}.md','evidence':f'qa/s04/source/p{p:03}_authority.png'} for p,reading,treatment in issues],'not_source_errors':[{'page':71,'finding':'R27 rewriting and missing ± were inherited defects, not permission to change the witness. The printed footnote is retained completely.'},{'pages':[72,73],'finding':'The local absence of an ellipsis after hh′h″ is retained, without regularizing the factor lists.'},{'pages':[87,93],'finding':'Oddly even translates impairement pair. Its arithmetic explanation remains separate.'},{'page':90,'finding':'Greater-than with two equality strokes and all exponent brackets retain printed notation.'}],'genuinely_illegible_source_ambiguities':[]})
notes=[]
for p in range(65,99):
 for l in ('fr','en'):
  t=(R/f'editions/{l}/pages/p{p:03}.tex').read_text();n=t.count('\\sourcefootnote{');assert n==(1 if p==71 else 0)
  notes.append({'printed_page':p,'layer':l,'author_note_count':n,'anchor':'*) after impair/odd, before full stop' if n else 'NONE','source_observation':manual[str(p)]['notes_and_anchors'],'inspection':'SOURCE_NOTE_AND_ANCHOR_REPLAYED' if n else 'SOURCE_READ_NO_AUTHOR_NOTE'})
writetsv('qa/s04/NOTE_AUDIT.tsv',notes)
writej('qa/s04/EDITORIAL_CALCULATION_CHECK.json',{'page':66,'kind':'editorial counterexample, not witness text','A':3,'B':9,'prime_factor_3_has_solution':any((x**4-3)%3==0 for x in range(3)),'fourth_power_residues_mod_9':sorted({x**4%9 for x in range(9)}),'no_solution_mod_9':not any((x**4-3)%9==0 for x in range(9))})

# The original input originals and both original/unpacked salvage archives remain intact.
immutable=[]
for o in old_manifest:
 if not o['path'].startswith('input/'):continue
 b=(R/o['path']).read_bytes();assert len(b)==int(o['bytes']) and h(b)==o['sha256']
 immutable.append({'path':o['path'],'bytes':len(b),'sha256':h(b),'comparison':'EXACT_SAVED_S03_ORIGINAL_BYTES','status':'PRESERVED_UNCHANGED'})
assert len(immutable)==21;writetsv('qa/s04/IMMUTABLE_INPUT_PRESERVATION.tsv',immutable)
salvage=[]
for num,name in [(12,'R27'),(13,'R28')]:
 arc=next((R/'input').glob(f'{num}_*.zip'))
 with zipfile.ZipFile(arc) as z:
  assert z.testzip() is None
  for inf in z.infolist():
   if inf.is_dir():continue
   rel=f'inherited/{name}/{inf.filename}';b=z.read(inf);assert (R/rel).read_bytes()==b
   salvage.append({'bundle':name,'member':inf.filename,'preserved_path':rel,'bytes':len(b),'sha256':h(b),'status':'EXACT_ORIGINAL_BYTES_NOT_TEXTUAL_AUTHORITY'})
assert len(salvage)==97;writetsv('qa/s04/INHERITED_ORIGINAL_REVALIDATION.tsv',salvage)

# Supplementary Poppler spot review, after all 73 primary images were individually read.
spot=[('en',7,'qa/s04/poppler/en/page-07.png','Full footnote, body anchor and dense inline math match the reviewed layout; no glyph/anchor defect.'),('fr',26,'qa/s04/poppler/fr/page-26.png','Nested-power formulas, geqq sign and split last word render clearly.'),('apparatus',4,'qa/s04/poppler/apparatus/page-4.png','New printed-b explanation and detail path fit; no clipped text or math.')]
writej('qa/s04/POPLER_SPOT_REVIEW.json',{'renderer':'pdftoppm 126dpi','all_pages_rendered':73,'individual_spot_reviews':[{'layer':l,'reader_page':n,**binding(p),'observation':s,'result':'NO_VISIBLE_DEFECT'} for l,n,p,s in spot],'primary_individual_review':'All73 final pages separately opened in qa/s04/visual and bound in MANUAL_OUTPUT_REVIEW.json.'})

# Internal state has no archive hash, avoiding a circular self-reference.
preserve('state/CURSOR.json');state=readj('state/CURSOR.json')
state.update({'schema':'dirichlet-paper-iv-state-v3','schema_version':3,'session':4,'prompt_completed':4,'prompt_cursor':'COMPLETE','next_cursor':'COMPLETE','status':'COMPLETE','first_untouched_page':None,'first_untouched_page_meaning':'No untouched author page or pending project prompt remains. Paper V is excluded.','build_state':'PASS_TWO_FINAL_ACCEPTANCE_RUNS_PER_READER_FROM_CLEAN_INITIALIZATION','visual_state':'PASS_ALL_73_FINAL_PAGES_INDIVIDUALLY_REVIEWED','prompt_04_executed':True,'whole_paper_complete':True,'cold_audit_state':'COMPLETE_INDEPENDENT_FULL_SCOPE_REPLAY','author_coverage_complete':True,'known_author_content_defects':[],'unresolved_source_ambiguities':[],'next_required_action':None,'retained_source_print_issues':[{'page':p,'reading':reading,'apparatus':f'apparatus/pages/p{p:03}.md'} for p,reading,_ in issues],'previous_accepted_release':{'file':'DIRICHLET_P04_S03_CUMULATIVE_FULL_STATE.zip','bytes':210121951,'sha256':'E60E5A926AFCF66800C25C357690D0097AE4573B840F836755B3581B12923007','nested_in_this_release':False},'current_readers':{l:{**binding(d['reader']),'pages':d['pages']} for l,d in build.items()},'handoff_metadata':'Stage-specific external DIRICHLET_P04_S04_CHECKPOINT.json binds the ZIP, stage-specific external manifest, stage-specific external diff, and every archive member. No circular self-hash; this internal cursor does not contain an archive hash.','evidence':{'intake':'qa/s04/INTAKE_VALIDATION.json','manual_cold_collation':'qa/s04/MANUAL_COLD_COLLATION.json','exact_scope_replay':'qa/s04/COLD_SCOPE_REPLAY.tsv','unit_alignment':'qa/s04/UNIT_ALIGNMENT.tsv','math_segment_alignment':'qa/s04/MATH_SEGMENT_ALIGNMENT.tsv','source_bindings':'qa/s04/CURRENT_SOURCE_BINDINGS.tsv','notes':'qa/s04/NOTE_AUDIT.tsv','retained_source_issues':'qa/s04/RETAINED_SOURCE_ISSUES.json','all_seams':'qa/s04/ALL_AUTHOR_SEAMS.tsv','boundary':'qa/s04/BOUNDARY_AUDIT.json','builds':'qa/s04/BUILD_RUNS.json','manual_output_review':'qa/s04/MANUAL_OUTPUT_REVIEW.json','output_preflight':'qa/s04/OUTPUT_PREFLIGHT.json','regression':'qa/s04/S03_READER_REGRESSION.tsv','repairs':'qa/s04/REPAIR_VERIFICATION.tsv','gates':'qa/s04/FINAL_COLD_AUDIT_GATES.json','predecessor_preservation':'qa/s04/S03_MEMBER_PRESERVATION.tsv','immutable_preservation':'qa/s04/IMMUTABLE_INPUT_PRESERVATION.tsv','copy_ledger':'ledgers/COPY_MATTER_LEDGER.tsv','diff':'SOURCE_BACKED_DIFF.tsv'}})
writej('state/CURSOR.json',state)

# Current README must not point readers at superseded build tools or pending-stage claims.
preserve('README.md')
(R/'README.md').write_text('''# Dirichlet, Band I, Paper IV — S04 final cold-audited state

**Status: COMPLETE. Prompt completed: 04. Next cursor: COMPLETE.** No pending author page or further project prompt remains. Only Paper IV is edited. Printed63–64 are separately logged title/blank copy matter; author pp.65–98 occur exactly once in each monolingual reader. The readers are re-typeset, not photographic facsimiles: physical within-page line wrapping is reflowed, while wording, lexical hyphens, paragraph boundaries, formula grouping, page seams, notes and source furniture are retained. The French der-/nière split across90/91 is explicit; the English breaks at the corresponding phrase. Editorial explanations never enter either author text.

## Current sources and readers

French: `editions/fr/main.tex` and `editions/fr/pages/p065.tex` through `p098.tex`; reader `readers/PAPER_IV_FR_PP065_098.pdf` (34pages).

English: `editions/en/main.tex` and independent page files; reader `readers/PAPER_IV_EN_PP065_098.pdf` (34pages).

Apparatus: `apparatus/main.tex`, `apparatus/pages/` and `apparatus/CATALOGUE.tsv`; reader `readers/PAPER_IV_APPARATUS_S04.pdf` (5pages). Previous apparatus readers are historical evidence only.

The current cursor is `state/CURSOR.json`. Every current `state/pages/` record binds the final editable page, apparatus entry, fresh source image and individually inspected final reader images. `ledgers/TOPOLOGY.tsv` covers all36 leaves; `copy_matter/` and the copy ledger retain63–64 outside the author readers. The original blank diplomatic copy file remains zero bytes.

## Actual fresh intake and authority

The actual S03 ZIP was freshly unpacked: 210121951bytes, SHA256 E60E5A926AFCF66800C25C357690D0097AE4573B840F836755B3581B12923007. All793 carried members and checkpoint/manifest bindings were validated. This was sequential continuation, not acceptance of an earlier zero-page access checkpoint. The canonical inherited S03 diff is its 27503-byte72-row ZIP member, SHA256 8EF129DB12EA2FD89AFFE781AE90243FA8138591F034653329192F7D2C04BE78. The stale26591-byte browser sidecar is preserved separately under `history/S03/` and was not used as current text.

Controls00–09 and literal Prompt04 are unchanged under `input/`. The controlling exact-scope PDF has36 leaves. The full-volume witness has657pages,36067858bytes,SHA256 961E55A2D32DDC88191CDD8A99F877A06BB3E721D7705F5A96C6F80AD67F9F6C. All21 immutable input originals are embedded unchanged; no external assembly dependency remains. Original R27/R28 archives and all97 unpacked members are preserved, not promoted to authority. Their out-of-scope cumulative readers remain evidence only.

## Independent cold audit

Every one of the36 source leaves was opened freshly at216dpi and replayed against the fixed map. The34 French author pages were read line-by-line and mathematical-token-by-token against full-PDF82–115; every English paragraph was checked for complete structural correspondence. This included the inherited R27/R28 regions65–80, all headings, local labels, signs, operators, accents, primes, superscripts/subscripts, brackets, punctuation, the complete p.71 note and its anchor, all33 author-page seams, and terminal matter. Full-PDF115 visibly ends PaperIV at printed98;116 was inspected only as the next-work exclusion boundary. No PaperV text was ingested.

The actual observations are `qa/s04/MANUAL_COLD_COLLATION.json`; fresh scans and detail crops are under `qa/s04/source/`. Counts and TeX-line ledgers are supplementary and are not presented as source-reading evidence. `COLD_SCOPE_REPLAY.tsv`, `ALL_AUTHOR_SEAMS.tsv`, `NOTE_AUDIT.tsv` and `BOUNDARY_AUDIT.json` bind the scope, seams, note and exclusion checks. `UNIT_ALIGNMENT.tsv` and `MATH_SEGMENT_ALIGNMENT.tsv` pair200 structural units and1461 mathematical segments; segments include isolated variables and display blocks, not1461 distinct equations.

Twenty-one new concrete correction rows are appended to the canonical72 inherited rows, for93 cumulative rows in `SOURCE_BACKED_DIFF.tsv`. They restore heading tracking, locally absent product ellipses on72–73, the printed b (not contextual delta) on89, and explicit English conditionals. The new p.89 apparatus explains the distinction without repairing the author text. Exact before/after/source locators, immediate-before snapshots and repair verification remain under `qa/s04/`. The witness issues on66,70,77,82,85 and89 remain literal; the p.71 inherited alterations are distinguished from genuine printed readings. There are no unresolved illegible-source ambiguities and no known remaining author-content defect after this audit.

## Clean builds and complete output review

Each reader was built in its own initially empty directory. The initialization pass has expected outline/page-label rerun notices; they are preserved, not hidden. Two subsequent final acceptance passes per reader (six clean passes total) had no warnings, overfull/underfull boxes or missing-glyph reports, and the two final PDFs per layer are byte-identical. Logs, recorder files and outputs are under `qa/s04/build/`; `BUILD_RUNS.json` binds them.

All73 final output pages (34French,34English,5apparatus) were rendered at126dpi and each individual page image was opened and inspected. `MANUAL_OUTPUT_REVIEW.json` binds every reviewed image to its final reader; no clipping, broken formula, missing glyph, wrong-order page or note overflow was found. Independent Poppler renders of all73 pages, font embedding and text geometry provide additional checks. The52 author-reader pages not affected by a cold-audit correction match S03 extracted text and rendered pixels exactly; the16 affected pages have source-backed revisions. Regression identity is not used as fidelity evidence.

## Preservation, reproducibility and verification

Every S03 member byte sequence remains available. Unchanged files retain their path; originals of replaced files reside under `history/S03/superseded/`, and the canonical old diff is separately preserved. `qa/s04/S03_MEMBER_PRESERVATION.tsv` supplies a793-row exact original-to-preserved path/size/SHA256 map. Earlier S01/S02 preservation evidence remains unchanged. No earlier cumulative ZIP is nested. Historical checkpoints, source claims, logs and scripts retain their original stage meanings; they do not override the current state. Do not run earlier-stage source generators on this final tree.

To rebuild the final sources with XeLaTeX and the standard packages named in the mains:

```sh
python tools/s04/build_s04.py
```

The script uses separate clean build directories, one initialization pass followed by two acceptance passes, and captures all evidence. Rebuilding changes current build evidence and requires renewed binding/visual checks before repackaging. Fonts are standard TeX-distributed Latin Modern/Computer Modern; no font files are redistributed. Edition input paths are relative; recorder logs preserve the execution environment's actual paths.

The release ZIP is built twice from frozen member bytes with fixed metadata and sorted safe normalized paths; the two archives must be identical. This determinism applies to the frozen member bytes, not a promise of PDF byte identity under a different TeX installation. The external stage-specific checkpoint and manifest are not their own archive members, avoiding circular hashes. The external checkpoint binds the ZIP, exact manifest, standalone cumulative diff and every member; the internal diff is byte-identical to the linked stage-specific standalone file. Historical sidecars remain ordinary evidence members.

Use `tools/s04/verify_handoff_s04.py` with `--zip`, `--checkpoint`, `--manifest` and `--diff` to reopen and verify CRCs, safe unique names, membership, every hash, cursor/accepted sets, current reader and visual bindings, immutable inputs and all predecessor bytes. The four final linked filenames are stage-specific to prevent reuse of stale generic browser basenames. No public upload or outside-work expansion was performed.

**Completed Prompt04. Next cursor: COMPLETE.**
''')

# Preservation map is computed from actual prior bytes, never an earlier PASS label.
prior=[]
for o in old_manifest:
 rel=o['path'];candidates=[rel,f'history/S03/superseded/{rel}']
 if rel=='SOURCE_BACKED_DIFF.tsv':candidates.append('history/S03/SOURCE_BACKED_DIFF_CANONICAL.tsv')
 found=None
 for pp in candidates:
  path=R/pp
  if path.is_file() and path.stat().st_size==int(o['bytes']) and h(path.read_bytes())==o['sha256']:
   found=pp;break
 assert found is not None,('lost S03 member',rel)
 prior.append({'s03_path':rel,'preserved_path':found,'bytes':o['bytes'],'sha256':o['sha256'],'disposition':'UNCHANGED_AT_ORIGINAL_PATH' if found==rel else 'ORIGINAL_BYTES_RELOCATED','status':'BYTE_IDENTITY_VERIFIED'})
assert len(prior)==793;writetsv('qa/s04/S03_MEMBER_PRESERVATION.tsv',prior)

# Every prerequisite checked above; archive-specific gates are verified after packaging externally.
gates={'schema':'dirichlet-s04-final-cold-audit-gates-v1','status':'ALL_CONTENT_BUILD_VISUAL_GATES_PASS','prompt_completed':4,'next_cursor':'COMPLETE','fresh_actual_zip_intake':True,'source_leaf_manual_replay':36,'french_author_pages_linewise_tokenwise_collated':34,'english_author_pages_full_structural_correspondence_reviewed':34,'inherited_regions_independently_replayed':[list(range(65,75)),list(range(75,81))],'all_author_seams_rechecked':33,'copy_title_blank_separately_logged':True,'paper_v_boundary_checked_and_excluded':True,'author_note_complete_and_anchor_rechecked':True,'retained_print_issues':[p for p,_,_ in issues],'source_resolvable_repairs_integrated':len(repairs),'cumulative_source_backed_diff_rows':93,'new_diff_snapshot_verification':True,'final_acceptance_build_passes_clean':6,'initialization_passes_with_expected_rerun_notices_preserved':3,'final_reader_pages':{l:d['pages'] for l,d in build.items()},'all_final_pages_individually_rendered_opened_and_reviewed':73,'unexpected_regressions':[],'all_s03_member_bytes_preserved':793,'immutable_originals_preserved':21,'inherited_archive_members_preserved':97,'unresolved_source_ambiguities':[],'known_author_content_defects':[],'publication_acceptance_scope':'Only the attached PaperIV witness and independent English/apparatus; preserved printed anomalies are not transcription defects.','archive_integrity_gate':'Performed after frozen-state packaging by external checkpoint and verifier; not circularly asserted here.'}
writej('qa/s04/FINAL_COLD_AUDIT_GATES.json',gates)
print('Finalized',len(prior),'preserved S03 members;',sum(x['disposition']=='UNCHANGED_AT_ORIGINAL_PATH' for x in prior),'unchanged paths;',len(repairs),'new correction rows; final cursor COMPLETE')
