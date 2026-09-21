from pathlib import Path
import re,csv,json,hashlib,collections
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest().upper()
def writetsv(rel,cols,rows):
 p=ROOT/rel;p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('w',encoding='utf8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=cols,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
def units(s):
 matches=list(re.finditer(r'^% U:([^ ]+) \| ([^\n]+)\n',s,re.M));res=[]
 for i,m in enumerate(matches):
  end=matches[i+1].start() if i+1<len(matches) else len(s)
  res.append({'id':m[1],'structure':m[2],'body':s[m.end():end], 'start_tex_line':s[:m.end()].count('\n')+1,'end_tex_line':s[:end].count('\n')})
 return res
mathpat=re.compile(r'(?<!\\)\$(.*?)(?<!\\)\$|\\\[(.*?)\\\]|\\begin\{equation\*\}(.*?)\\end\{equation\*\}',re.S)
def mathblocks(s):
 s=re.sub(r'%[^\n]*','',s)
 return [('inline' if m[1] is not None else 'display',next(g for g in m.groups() if g is not None).strip()) for m in mathpat.finditer(s)]
def canonical(s):
 s=re.sub(r'\\text\{[^}]*\}','',s)
 s=s.replace(r'\dfrac',r'\frac')
 s=re.sub(r'\\(?:quad|qquad)\b','',s)
 return re.sub(r'\s+','',s)
# Reading coordinates are fractions of full authority page; no OCR-derived text.
regions={
65:{'p065.title':(.10,.23,.76,.33),'p065.u01':(.10,.33,.76,.76),'p065.rule':(.33,.76,.51,.78)},
66:{'p066.section':(.54,.14,.59,.16),'p066.u01':(.25,.16,.91,.20),'p066.u02':(.25,.20,.91,.33),'p066.u03':(.25,.33,.91,.47),'p066.u04':(.25,.47,.91,.57),'p066.u05':(.25,.57,.91,.66),'p066.u06':(.25,.66,.91,.79)},
67:{'p067.u01':(.10,.13,.76,.23),'p067.u02':(.10,.23,.76,.33),'p067.section':(.39,.34,.44,.37),'p067.u03':(.10,.37,.76,.79)},
68:{'p068.u01':(.25,.14,.91,.31),'p068.u02':(.25,.31,.91,.52),'p068.u03':(.25,.52,.91,.61),'p068.u04':(.25,.61,.91,.70),'p068.u05':(.25,.70,.91,.80)},
69:{'p069.u01':(.10,.14,.76,.37),'p069.u02':(.10,.37,.76,.61),'p069.u03':(.10,.61,.76,.68),'p069.u04':(.10,.68,.76,.76),'p069.u05':(.10,.75,.76,.80)},
70:{'p070.u01':(.25,.14,.91,.22),'p070.u02':(.25,.21,.91,.29),'p070.u03':(.25,.29,.91,.40),'p070.u04':(.25,.40,.91,.55),'p070.u05':(.25,.55,.91,.74),'p070.u06':(.25,.73,.91,.80)},
71:{'p071.u01':(.10,.14,.76,.20),'p071.u02':(.10,.20,.76,.26),'p071.u03':(.10,.26,.76,.35),'p071.section':(.39,.37,.44,.39),'p071.u04':(.10,.39,.76,.58),'p071.u05':(.10,.58,.76,.64),'p071.u06':(.10,.63,.76,.67)},
72:{'p072.u01':(.25,.14,.91,.20),'p072.u02':(.25,.20,.91,.29),'p072.u03':(.25,.29,.91,.36),'p072.u04':(.25,.36,.91,.50),'p072.u05':(.25,.49,.91,.58),'p072.u06':(.25,.58,.91,.67),'p072.u07':(.25,.67,.91,.79)},
73:{'p073.u01':(.10,.14,.76,.31),'p073.u02':(.10,.31,.76,.39),'p073.u03':(.10,.39,.76,.51),'p073.u04':(.10,.50,.76,.80)},
74:{'p074.u01':(.25,.14,.91,.29),'p074.u02':(.25,.28,.91,.38),'p074.section':(.54,.39,.59,.41),'p074.u03':(.25,.41,.91,.57),'p074.u04':(.25,.57,.91,.68),'p074.u05':(.25,.68,.91,.80)}
}
allunits=[];mathrows=[];lineaudit=[];pages=[]
for pg in range(65,75):
 paths={l:ROOT/f'editions/{l}/pages/p{pg:03d}.tex' for l in ['fr','en']}
 txt={l:p.read_text() for l,p in paths.items()};u={l:units(t) for l,t in txt.items()}
 assert [x['id'] for x in u['fr']]==[x['id'] for x in u['en']]
 for a,b in zip(u['fr'],u['en']):
  uid=a['id'];reg=regions[pg][uid];evidence=f'qa/source/p{pg:03d}_authority.png; full PDF {pg+17}; scope leaf {pg-62}; region_xyxy_fraction={reg}'
  fa=mathblocks(a['body']);fb=mathblocks(b['body'])
  if len(fa)!=len(fb):print('COUNT MISMATCH',uid,len(fa),len(fb))
  assert len(fa)==len(fb),uid
  for n,((ta,ma),(tb,mb)) in enumerate(zip(fa,fb),1):
   ok=canonical(ma)==canonical(mb) and ta==tb
   if not ok:print('MATH MISMATCH',uid,n,ma,mb)
   assert ok,(uid,n)
   mathrows.append({'printed_page':pg,'authority_pdf_page':pg+17,'unit_id':uid,'formula_id':f'{uid}.m{n:03d}','placement':ta,'french_tex':ma.replace('\n',' '),'english_tex':mb.replace('\n',' '),'cross_layer_tokens':'IDENTICAL_EXCLUDING_TRANSLATED_PROSE','authority_evidence':evidence,'scan_comparison':'VISUALLY_CHECKED'})
  allunits.append({'printed_page':pg,'authority_pdf_page':pg+17,'scope_leaf':pg-62,'unit_id':uid,'structure':a['structure'],'fr_tex_lines':f"{a['start_tex_line']}-{a['end_tex_line']}",'en_tex_lines':f"{b['start_tex_line']}-{b['end_tex_line']}",'math_segments':len(fa),'authority_evidence':evidence,'french_audit':'SOURCE_CONFIRMED','english_audit':'FULL_CORRESPONDENCE_REVIEWED'})
  for n,line in enumerate(a['body'].splitlines(),a['start_tex_line']):
   if not line.strip() or line.startswith('%'):continue
   lineaudit.append({'printed_page':pg,'authority_pdf_page':pg+17,'unit_id':uid,'edition_tex_line':n,'tex_line':line,'authority_evidence':evidence,'status':'CHECKED_AGAINST_PRINT','note':'Edition source line, not an asserted physical scan-line number; TeX control lines retain structure.'})
 rec={'schema':'dirichlet-page-record-v1','printed_page':pg,'authority_pdf_page':pg+17,'scope_leaf':pg-62,'role':'AUTHOR_TEXT_FRENCH','source_image':f'qa/source/p{pg:03d}_authority.png','source_image_sha256':sha(ROOT/f'qa/source/p{pg:03d}_authority.png'),'french':{'path':str(paths['fr'].relative_to(ROOT)),'sha256':sha(paths['fr'])},'english':{'path':str(paths['en'].relative_to(ROOT)),'sha256':sha(paths['en'])},'units':[x for x in allunits if x['printed_page']==pg],'source_ambiguities':[],'apparatus_path':f'apparatus/pages/p{pg:03d}.md','source_audit':'VISUAL_PAGEWISE_AND_LINEWISE_COMPLETED','english_alignment':'FULL_ARGUMENT_AND_MATH_REVIEWED','visual_output_audit':'PENDING_FINAL_RECEIPT'}
 pages.append(rec)
 d=ROOT/'state/pages';d.mkdir(parents=True,exist_ok=True);(d/f'p{pg:03d}.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
writetsv('qa/UNIT_ALIGNMENT.tsv',list(allunits[0]),allunits)
writetsv('qa/FORMULA_AUDIT.tsv',list(mathrows[0]),mathrows)
writetsv('qa/SOURCE_LINE_AUDIT.tsv',list(lineaudit[0]),lineaudit)
print('Units',len(allunits),'math segments',len(mathrows),'French editable lines audited',len(lineaudit))
# Each physical line of both inherited TeX files is classified. No cumulative reader is used.
unitmap={'par.001':'65','par.002':'66','par.003':'66','par.004':'66','par.005':'66','thm.001':'66','par.006':'66','thm.002':'67','par.007':'67','par.008':'67;68','par.009':'68','par.010':'69','par.011':'69','thm.003':'69','par.012':'69','par.013':'69;70','par.014':'70','par.015':'70','thm.004':'70','par.016':'71','thm.005':'71','par.017':'71','par.018':'71;72','par.019':'72;73','par.020':'73','par.021':'73;74','thm.006':'74','par.022':'74'}
oldrows=[]
for lang,folder in [('fr','orig'),('en','en')]:
 f=next((ROOT/'inherited/R27').glob(f'*/new/{folder}/tex/*.tex'));inside=False;unit='';pgr='65'
 for num,line in enumerate(f.read_text().splitlines(),1):
  if r'\begin{document}' in line:inside=True
  if r'\end{document}' in line:inside=False
  m=re.search(r'\\unitid\{[^}]*\.(par|thm)\.(\d+)\}',line)
  if m:unit=m[1]+'.'+m[2];pgr=unitmap[unit]
  role='AUTHOR_OR_MATH_OR_STRUCTURE' if inside and line.strip() else 'WRAPPER_OR_BLANK'
  oldrows.append({'layer':lang,'inherited_path':str(f.relative_to(ROOT)),'inherited_tex_line':num,'inherited_unit':unit,'printed_pages':pgr if role!='WRAPPER_OR_BLANK' else '', 'line':line,'disposition':'REPLAYED_AGAINST_AUTHORITY; SEE_SOURCE_BACKED_DIFF' if role!='WRAPPER_OR_BLANK' else 'PRESERVED_ONLY_NOT_AUTHOR_CONTENT','evidence':';'.join(f'qa/source/p{int(p):03d}_authority.png' for p in pgr.split(';')) if role!='WRAPPER_OR_BLANK' else ''})
writetsv('qa/INHERITED_TEX_LINE_AUDIT.tsv',list(oldrows[0]),oldrows)
