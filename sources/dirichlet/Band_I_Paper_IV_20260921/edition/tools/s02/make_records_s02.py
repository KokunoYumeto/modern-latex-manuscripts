"""Encode completed human page/line collation; mechanically check bilingual math and inherited continuity.
The line numbers below refer to editable TeX, never purported physical scan lines.
This script does not perform OCR or replace visual source collation.
"""
from pathlib import Path
import re,csv,json,hashlib,difflib,collections
R=Path(__file__).resolve().parents[2];Q=R/'qa/s02'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest().upper()
def wt(name,rows,fields=None):
 with (Q/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields or list(rows[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
def wj(name,x):(Q/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def units(s):
 ms=list(re.finditer(r'^% U:(\S+) \| ([^\n]+)\n',s,re.M));out=[]
 for i,m in enumerate(ms):
  end=ms[i+1].start() if i+1<len(ms) else len(s)
  out.append({'id':m[1],'structure':m[2],'body':s[m.end():end],'start':s[:m.end()].count('\n')+1,'end':s[:end].count('\n')})
 return out
mp=re.compile(r'(?<!\\)\$(.*?)(?<!\\)\$|\\\[(.*?)\\\]|\\begin\{equation\*\}(.*?)\\end\{equation\*\}',re.S)
def math(s):return [('inline' if m[1] is not None else 'display',next(v for v in m.groups() if v is not None).strip()) for m in mp.finditer(re.sub(r'%[^\n]*','',s))]
def canon(s):
 s=re.sub(r'\\(?:text|hbox)\{(ou|or)\}',r'\\text{or}',s)
 s=s.replace(r'\dfrac',r'\frac');s=re.sub(r'\\(?:quad|qquad)\b','',s)
 return re.sub(r'\s+','',s)
locs={
75:['opening Il est très facile through On a donc','first E/b and F/b row','Quant aux nombres K et L','K/b and L/b row','En effet, on voit par la dernière équation (p.74), through citation no.197','EK/b and FL/b row, then ou, ce qui est la même chose','label (δ), two plus/minus-psi symbols','En examinant: case φ divisible by b','label (δ′), congruence and opposite-sign symbol'],
76:['Il résulte: preceding theorem and elimination of t','psi+t / psi−t symbol row','On tire immédiatement: congruence and first root choice','positive-root symbol row and car il est évident explanation','first repeated product identity','Considérons maintenant: negative-root case','negative-root symbol row and explanation of substitution for −t','second repeated product identity','Nous sommes donc arrivés','terminal t/b=1 ou t/b=−1 row'],
77:['Il suffira: finding χ','third occurrence of product identity','Venons maintenant: φ divisible by b','opposite-sign congruence row and addition of t±ψ giving 2t/b','En combinant: printed variable t before the 8n+7 / 8n+3 alternatives','En comparant: complete generalization, t²±Mu²=p, and announced auxiliary theorem','quoted auxiliary theorem, c and δ','Quoi qu’il en soit; page ends after pour toutes les valeurs'],
78:['page-head de b: quadratic-divisor condition, table limit136, exception79, complete generality discussion','centred Théorème I. heading','whole quoted Theorem I, both divisibility cases and χ-product alternatives','En faisant successivement b=3,b=7 etc.','whole quoted p=12n+1 corollary','whole quoted 28n+1,28n+9,28n+25 corollary','indented etc.'],
79:['section number5','Désignons par a: setup, u factor2^ν and fourth-power result','Décomposons: all written g/h factors','label (ε), brace and both three-entry rows','L’équation t²−au²=p donne immédiatement','both −ap rows and following Comparant sentence','both p rows and following reciprocal-law introduction','both reciprocal g/h rows and conclusion introduction','whole product equality and following sentence ending at h,'],
80:['page-head h′,h″,… and first paragraph conclusion about second members of (ε)','On peut: sign changes replacing −a by a','label (ζ), brace and both ±1 rows','En comparant: number of sign changes','Le nombre: parity condition and both products of second members','D’un autre côté: complete inversion/product argument','t/p=t/a display','Ce résultat: t=4n+1 versus t=4n+3','t/p=−t/a display'],
81:['Ces deux cas and labelled (η) pair','L’équation: both congruences and replacement of t/p,u/p','indented proposition (θ), both exponent sums, and result sentence','Posons: decomposition and transposition','Il y a maintenant: first divisibility case, gcd m, primed substitution','Cette équation: factors and original two-by-two E/F/K/L block','On s’assurera: coprimality, squares and E/a,F/a row'],
82:['La différence: complete parity argument; printed p²=φ²+ψ² retained','Les nombres: single parity exponent statement','Il résulte: primed formula, general odd divisor R, citation no.196','Appliquant: K/a=L/a and both subsequent plus/minus-psi identities'],
83:['Si l’on compare: both sign alternatives in two separate displays','L’équation: arbitrary root χ, congruences, and common psi+chi symbol','On conclut: both equivalent product conditions','Ce résultat: divisible case, paired signs and resulting 2t symbol','En comparant: final condition, ending ou, ce qui est la'],
84:['page-head même chose, with both forms of a','Il en est: entire extension argument and t²±Mu²=p','Théorème II. heading','whole quoted theorem, both φ-divisibility cases','En faisant successivement a=5,a=13 and quadratic-divisor statement'],
85:['whole quoted 20n+1,20n+9 corollary','indented etc.','En indiquant: entire methodological revision; printed ps retained in replacement equation; Legendre citation','La démonstration ainsi modifiée','long separator rule before Addition heading','Addition au mémoire précédent. heading','short rule below Addition heading','Quoique l’indication; page ends after d’être beaucoup'],
86:['page-head simplifiées and introductory conclusion','Désignons par p and local label (α′), t²−bu²=ps²','complete solvability, coprimality, parity reduction and p71 note reference; t′/u′ construction','complete factorization, three-prime rows in both directions; four visible terminal dots in each row']}
all_u=[];all_m=[];all_l=[];all_pages=[]
for p in range(75,87):
 paths={l:R/f'editions/{l}/pages/p{p:03d}.tex' for l in ['fr','en']};tx={l:q.read_text() for l,q in paths.items()};uu={l:units(s) for l,s in tx.items()}
 assert [x['id'] for x in uu['fr']]==[x['id'] for x in uu['en']]
 assert len(locs[p])==len(uu['fr'])
 for a,b,loc in zip(uu['fr'],uu['en'],locs[p]):
  ev=f'qa/s02/source/p{p:03d}_authority.png; full PDF {p+17}; scope leaf {p-62}; '+loc
  ma,mb=math(a['body']),math(b['body']);assert len(ma)==len(mb),(p,a['id'],len(ma),len(mb))
  for n,((ka,va),(kb,vb)) in enumerate(zip(ma,mb),1):
   assert ka==kb and canon(va)==canon(vb),(p,a['id'],n,va,vb)
   all_m.append({'printed_page':p,'authority_pdf_page':p+17,'unit_id':a['id'],'formula_id':a['id']+f'.m{n:03d}','placement':ka,'french_tex':va.replace('\n',' '),'english_tex':vb.replace('\n',' '),'cross_layer_tokens':'IDENTICAL_EXCEPT_EXPLICIT_OU_OR_TRANSLATION_AND_SPACING','authority_evidence':ev,'scan_comparison':'MANUALLY_VISUALLY_CHECKED'})
  all_u.append({'printed_page':p,'authority_pdf_page':p+17,'scope_leaf':p-62,'unit_id':a['id'],'structure':a['structure'],'fr_tex_lines':f"{a['start']}-{a['end']}",'en_tex_lines':f"{b['start']}-{b['end']}",'math_segments':len(ma),'authority_evidence':ev,'french_audit':'SOURCE_CONFIRMED','english_audit':'FULL_CORRESPONDENCE_REVIEWED'})
  for l,u in [('fr',a),('en',b)]:
   for n,line in enumerate(u['body'].splitlines(),u['start']):
    if not line.strip():continue
    all_l.append({'printed_page':p,'authority_pdf_page':p+17,'layer':l,'unit_id':u['id'],'edition_tex_line':n,'tex_line':line,'authority_evidence':ev,'status':'CHECKED_AGAINST_PRINT' if l=='fr' else 'FULL_STRUCTURAL_TRANSLATION_CHECKED','note':'Editable TeX line, not a claimed physical scan-line number; control lines encode source structure. Manual source collation plus mechanical cross-layer math check.'})
 rec={'schema':'dirichlet-page-record-v2','printed_page':p,'authority_pdf_page':p+17,'scope_leaf':p-62,'role':'AUTHOR_TEXT_FRENCH','origin':'R28_PAGEWISE_REPLAYED_DERIVATIVE' if p<=80 else 'DIRECT_AUTHORITY_TRANSCRIPTION','source_image':f'qa/s02/source/p{p:03d}_authority.png','source_image_sha256':sha(R/f'qa/s02/source/p{p:03d}_authority.png'),'french':{'path':str(paths['fr'].relative_to(R)),'sha256':sha(paths['fr'])},'english':{'path':str(paths['en'].relative_to(R)),'sha256':sha(paths['en'])},'units':[x for x in all_u if x['printed_page']==p],'source_ambiguities':[],'apparatus_path':f'apparatus/pages/p{p:03d}.md','apparatus_sha256':sha(R/f'apparatus/pages/p{p:03d}.md'),'source_audit':'VISUAL_PAGEWISE_AND_LINEWISE_COMPLETED','english_alignment':'FULL_ARGUMENT_AND_MATH_REVIEWED','accepted_layers':['fr','en','apparatus'],'notes':'No new author footnote on this leaf. Source p86 refers back to the author note on p71.' if p==86 else 'No author footnote on this leaf.'}
 all_pages.append(rec)
wt('UNIT_ALIGNMENT.tsv',all_u);wt('FORMULA_AUDIT.tsv',all_m);wt('SOURCE_LINE_AUDIT.tsv',all_l)
# Classify every original R28 editable-source line, without changing original bytes.
oldrows=[];collation=[]
for lang,sub in [('fr','orig'),('en','en')]:
 f=next((R/'inherited/R28').glob(f'*/new/{sub}/tex/*.tex'));raw=f.read_text();ms=list(re.finditer(r'\\unitid\{dirichlet\.v1\.p04b\.(?:en\.)?([^}]+)\}',raw));uid='';line_to_unit={}
 newunits={}
 for p in range(75,81):
  for u in units((R/f'editions/{lang}/pages/p{p:03d}.tex').read_text()):
   key=u['id'].split('.r28.')[1];key=re.sub(r'(?<=\d)[ab]$','',key);newunits.setdefault(key,[]).append((p,u))
 for j,m in enumerate(ms):
  stop=ms[j+1].start() if j+1<len(ms) else raw.index(r'\end{document}')
  oldbody=raw[m.end():stop]
  key=m[1];pairs=newunits[key];pp=[p for p,u in pairs]
  for n in range(raw[:m.start()].count('\n')+1,raw[:stop].count('\n')+1):line_to_unit[n]=key
  nb=' '.join(u['body'] for p,u in pairs)
  def comparable(s):
   s=re.sub(r'%[^\n]*','',s)
   s=s.replace(r'\pmod b',r'\md{b}').replace('»','„').replace('«','“')
   s=re.sub(r'\\begin\{equation\*\}\\tag\{\$(\\[a-z]+\x27?)\$\}',lambda m:r'\[('+m[1]+r')\qquad',s)
   s=s.replace(r'\end{equation*}',r'\]')
   s=s.replace(r'\sourceheading{',r'\textsc{').replace(r'\sectionnumber{5}','5.')
   s=s.replace(r'\begin{center}','').replace(r'\end{center}','')
   s=re.sub(r'\\(?:par|indent|noindent)\b','',s)
   return re.findall(r'\\[a-zA-Z]+|[^\W\d_]+|\d+|[^\w\s]',s)
  aa,bb=comparable(oldbody),comparable(nb)
  dd=[]
  for op,a,b,c,d in difflib.SequenceMatcher(None,aa,bb,autojunk=False).get_opcodes():
   if op!='equal':dd.append({'operation':op,'before':' '.join(aa[a:b]),'after':' '.join(bb[c:d]),'left_context':' '.join(bb[max(0,c-8):c]),'right_context':' '.join(bb[d:d+8])})
  if lang=='fr':assert not dd,(key,dd)
  collation.append({'layer':lang,'r28_unit':key,'printed_pages':pp,'inherited_unit_sha256':hashlib.sha256(oldbody.encode()).hexdigest().upper(),'new_units':[u['id'] for p,u in pairs],'token_comparison':'IDENTICAL_AFTER_DOCUMENTED_LAYOUT_QUOTE_MOD_NOTATION_NORMALIZATIONS' if not dd else 'CONCRETE_EN_CHANGES_RECORDED_IN_DIFF','differences':dd,'source_replay':'ALL_WORDS_AND_FORMULAS_VISUALLY_REPLAYED_AGAINST_ATTACHED_LEAVES'})
 for n,line in enumerate(raw.splitlines(),1):
  key=line_to_unit.get(n,'');pairs=newunits.get(key,[]);pp=sorted(set(p for p,u in pairs))
  role='AUTHOR_TEXT_MATH_OR_STRUCTURE' if key and line.strip() else ('ADDED_EDITORIAL_TITLE' if n in (16,17,18) else 'WRAPPER_OR_BLANK')
  oldrows.append({'layer':lang,'inherited_path':str(f.relative_to(R)),'inherited_tex_line':n,'inherited_unit':key,'printed_pages':';'.join(map(str,pp)) if key else '','line':line,'role':role,'disposition':'SOURCE_REPLAYED; CORRECTED_DERIVATIVE_ONLY_ACCEPTED' if key else 'PRESERVED_NOT_INGESTED_AS_AUTHOR_TEXT','evidence':'; '.join(f'qa/s02/source/p{p:03d}_authority.png' for p in pp)})
wt('INHERITED_TEX_LINE_AUDIT.tsv',oldrows);wj('R28_TOKEN_COLLATION_REVIEW.json',{'normalizations':'Whitespace and TeX paragraph/centre wrappers; documented quote direction, modular abbreviation point, display-label placement and heading presentation. French tokens then identical; English differences enumerated below. This equality is not substituted for visual source collation.','units':collation})
for rec in all_pages:(R/f"state/pages/p{rec['printed_page']:03d}.json").write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
wj('CONTENT_AUDIT_COUNTS.json',{'new_author_pages':list(range(75,87)),'aligned_units':len(all_u),'paired_math_segments':len(all_m),'french_editable_lines':sum(r['layer']=='fr' for r in all_l),'english_editable_lines':sum(r['layer']=='en' for r in all_l),'inherited_tex_lines_classified':len(oldrows),'inherited_units_per_language':len(collation)//2,'author_footnotes_added':0,'source_ambiguities':[],'retained_legible_source_issues':[77,82,85],'formula_audit_limit':'Segments include isolated variables, inline relations, full displays and their labels. Count is not a count of numbered equations or physical printed lines.'})
print('Complete new content records:',len(all_pages),'units',len(all_u),'paired math segments',len(all_m),'TeX lines',len(all_l),'inherited lines',len(oldrows))
