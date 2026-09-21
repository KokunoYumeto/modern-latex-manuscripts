"""Encode the completed manual S03 collation and mechanically test bilingual math.
These are editable TeX line numbers, not physical scan-line coordinates. This
script does not read images, OCR, or perform an independent cold source audit.
"""
from pathlib import Path
import re,csv,json,hashlib
R=Path(__file__).resolve().parents[2];Q=R/'qa/s03'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest().upper()
def wt(path,rows,fields=None):
 with path.open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields or list(rows[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
def rd(p):return list(csv.DictReader(p.open(),delimiter='\t'))
def wj(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def units(s):
 ms=list(re.finditer(r'^% U:(\S+) \| ([^\n]+)\n',s,re.M));out=[]
 for i,m in enumerate(ms):
  end=ms[i+1].start() if i+1<len(ms) else len(s)
  out.append(dict(id=m[1],structure=m[2],body=s[m.end():end],start=s[:m.end()].count('\n')+1,end=s[:end].count('\n')))
 return out
mp=re.compile(r'(?<!\\)\$(.*?)(?<!\\)\$|\\\[(.*?)\\\]|\\begin\{equation\*\}(.*?)\\end\{equation\*\}',re.S)
def math(s):
 s=re.sub(r'%[^\n]*','',s)
 # An equation enclosing prose in a minipage is a statement, not all mathematics.
 # Retain/extract its explicit tag and each internal inline/display segment.
 s=re.sub(r'\\begin\{equation\*\}(.*?)\\end\{equation\*\}',lambda m:m[1] if r'\begin{minipage}' in m[1] else m[0],s,flags=re.S)
 return [('inline' if m[1] is not None else 'display',next(v for v in m.groups() if v is not None).strip()) for m in mp.finditer(s)]
def canon(s):
 s=re.sub(r'\\(?:text|hbox)\{(ou|or)\}',r'\\text{or}',s);s=s.replace(r'\dfrac',r'\frac');s=re.sub(r'\\(?:quad|qquad)\b','',s)
 return re.sub(r'\s+','',s)
locs={
87:['Faisant le produit: identity with 2^nu, full written k/k-prime product and result','Le nombre p: both residue classes, impairement pair, nu=1, and label beta-prime','Reprenons: both three-prime l rows, four terminal dots, product identity and label gamma-prime','En mettant: congruence t²=bu², exponent (p−1)/4, full two-step substitution using beta-prime'],
88:['Cette dernière: comparison of u/p and t/b using gamma-prime','label delta-prime, complete residue/non-residue alternatives','Décomposons: p=phi²+psi², equation with ps² and transposition','Les nombres s,t,u: s non-divisible by b, gcd m, primed substitution and divisor citation no.197','La dernière: both factors, E/F/K/L block in original two-by-two order','Il est facile: complete first half of coprimality proof, through D’un autre'],
89:['côté: second half of coprimality proof and both square-factor symbols','On a aussi: K/b,L/b, multiplied identities, reversed psi order, epsilon-prime with free signs','Comme on a: both roots between ±b/2, t²=chi²s², paired signs and substituting for ±t'],
90:['D’un autre côté: reciprocity sign, multiplying equations, cancelling s²','comparison with delta-prime: labelled zeta-prime and both product tests','Cette proposition: divisible case, exact b powers k and h, definitions of primed quantities and product','Il faut: k greater-or-double-equal h versus k<h, all three b-power factorizations, reuse of h, ending der-'],
91:['nière: product m²b^r(g²+bh²), impossibility of both factors divisible, paired signs and E/K factorization','Or: E square, K/b=1 and EK/b relation','Il est permis: adding t±psi s to t∓psi s, 2t/b=t/b times2/b, b=8n+7 or8n+3','inset statement: −b criterion based on b=8n+7 versus8n+3','En réunissant: theoremI conclusion and singular parvenu as printed','Occupons-nous: theoremII setup, a,p reciprocal conditions, end plusieurs'],
92:['fois: eta-prime equation t²+au²=ps² and full coprimality and parity conditions','Décomposons: both explicit prime products with nu and mu, one exponent zero','L’équation eta-prime: p/k row ends three dots; k/p row ends four; complete u/p product with2^nu','Il résulte: both a/l and l/a reciprocal rows with four terminal dots, full l-product and mu factors','Distinguons: parity cases, source ends Si'],
93:['u est pair: mu=0, t/a=t/p, u/p=(-1)^((p−1)/4), complete p=8n+1/8n+5 proof','Passons: t even,u odd, nu=0, u/p=1','Si les nombres: both equal-form and mixed-form cases, impairement pair, mu=1 and exponent order a then p','Si nous réunissons: inset complete two-case summary, exponent order p then a','En comparant: full congruence including u exponent, announcement of theorem at next page'],
94:['label open-theta-prime, entire two-case inset statement and both paired alternatives','Décomposons: p as sum of squares, psi even, product with ps andau²','Premier cas: phi not divisible by a','Comme: gcd m, primed product, all coprimality clauses and citation no.197','Désignant: E,K,F,L, original two-by-two factor array, coprime squares and E/a,F/a','Il faut: u even first, u-prime=u/m, odd binomial, page ends seront donc'],
95:['dans ce cas: K/a,L/a then EK/a,FL/a, reversing t−psi s and free-sign formula','Passons: u odd, both 8n cases, K=2^beta K-prime, highest power of2, complete proof forK andL and repeated product identities','Le nombre u: a=8n+5, binomial8n+4, both K,L even, ends chacun'],
96:['d’eux: K=2K-prime,L=2L-prime, all individual signs, multiplied products and double-sign result','En résumant: full quoted u-even/u-odd statement','On a vu: even case compared with open-theta-prime, both equal/opposite character alternatives','On a également vu: odd case, both power signs and full comparison, ends lorsque'],
97:['u est impair: repeated equality/opposite alternatives and common conclusion','quoted theorem: biquadratic and non-biquadratic cases, both free double signs','Comme: full root choice and congruence comparison, replacement of ±t by chi s, product identity','D’un autre côté: other character equation, memberwise product including s²/a, both final chi(chi+psi) tests','Ces résultats: phi divisibility cases, end L’analyse qu’il faut appliquer'],
98:['à ce second cas: explicit statement that analogous proof is not developed here','quoted phi-divisible-by-a conclusion, 8n+1 versus8n+5','Ce résultat: theoremII linkage','On a sans doute: replacing even-square root psi by odd-square root phi','Les résultats: delta-prime and open-theta-prime, singular appuyé, Gauss, a=5 introduction','complete quoted20n+1 and20n+9 examples, p=t²+5u² and parity reversal','Les théorèmes: both displayed original equations and both in-text alternative equations','En traitant: first alternative equation and b=3 example introduction','complete quoted12n+1 example, p=t²+3u², t odd, 12n±1 versus12n±5','final horizontal rule; no following author text']}
notes={
87:'Direct source continuation of the Addition. The labels beta-prime and gamma-prime retain local scope. The printed phrase impairement pair is rendered oddly even, not silently replaced by modern terminology; nu=1 gives its local meaning. All repeated prime-factor and reciprocity rows remain.',
88:'The label delta-prime marks the whole statement. Factors t+psi s and t−psi s are decomposed in the printed two-by-two E/F/K/L order. The full coprimality argument continues across the original page boundary. No conjectural emendation.',
89:'The coprimality proof continues without an inserted transition. Epsilon-prime preserves its paired signs and the instruction that they are at will in both members. Signature 12 and the volume imprint remain page furniture, not new author prose.',
90:'The comparison glyph has two equality strokes below the greater-than stroke, represented by \\geqq. The powers b^(2k+2), b^(2h+1), b^(k−h), and b^(h−k−1), and the later reuse of h, are retained as printed. The word dernière divides der-/nière at90/91.',
91:'The opening nière completes the word divided on p90. All paired-sign factor arguments and the inset −b statement remain. The singular parvenu in nous sommes parvenu is retained. The theoremII proof begins on this page; signature12* is retained.',
92:'Eta-prime retains the equation t²+au²=ps². Both factorizations in primes and both reciprocity chains are present. The first p/k row has three terminal dots; the following reciprocal row and the two l rows have three ellipsis dots plus a full stop. No uniform punctuation normalization is imposed.',
93:'Both parity cases and the complete mixed-residue-class argument remain. Impairement pair is translated oddly even; the text itself states mu=1. Exponent order is retained in each occurrence, including a then p in one formula and p then a in the summary.',
94:'The source open theta is represented by \\vartheta in the primed local label. The whole two-case statement is kept together. All coprimality clauses and the source order of the E/K/F/L two-by-two array are preserved. No extra author note is supplied.',
95:'The repeated square-factor and reciprocal-symbol reasoning is retained, not replaced by a reference to an earlier argument. Both proof cases for a and all K/L factors remain. The final sentence continues on p96.',
96:'The full K-prime/L-prime argument, quoted two-case summary, and separate even/odd comparisons are retained. No mathematical correction or new editorial anchor is inserted into either author reader.',
97:'The quoted common theorem, complete two-root substitution, and both final product tests remain. Two source-backed English drafting refinements restore explicit conditional syntax and the printed punctuation junction; see qa/s03/SOURCE_BACKED_DIFF_S03.tsv. Signature13 and the volume imprint are retained.',
98:'Final author page: full-PDF115/exact-scope36 visibly bears folio98. All closing conclusions and examples a=5 and b=3 are retained, including both pairs of equations. The singular appuyé in nous nous sommes appuyé is preserved. Extended running head and terminal horizontal rule retained. Full-PDF116 is inspected only for the next-paper boundary and supplies no edition content.'}
all_u=[];all_m=[];all_l=[];catalog=rd(R/'history/S02/superseded/apparatus/CATALOGUE.tsv')
for p in range(87,99):
 paths={l:R/f'editions/{l}/pages/p{p:03}.tex' for l in ['fr','en']};tx={l:q.read_text() for l,q in paths.items()};uu={l:units(s) for l,s in tx.items()}
 assert [x['id'] for x in uu['fr']]==[x['id'] for x in uu['en']]
 assert len(locs[p])==len(uu['fr']),(p,len(locs[p]),len(uu['fr']))
 for a,b,loc in zip(uu['fr'],uu['en'],locs[p]):
  assert a['structure']==b['structure'] or a['id'] in ['p090.u04','p091.u01'],(p,a['id'])
  ev=f'qa/s03/source/p{p:03}_authority.png; full PDF {p+17}; scope leaf {p-62}; '+loc
  ma,mb=math(a['body']),math(b['body']);assert len(ma)==len(mb),(p,a['id'],len(ma),len(mb))
  for n,((ka,va),(kb,vb)) in enumerate(zip(ma,mb),1):
   assert ka==kb and canon(va)==canon(vb),(p,a['id'],n,va,vb)
   all_m.append(dict(printed_page=p,authority_pdf_page=p+17,unit_id=a['id'],formula_id=a['id']+f'.m{n:03}',placement=ka,french_tex=va.replace('\n',' '),english_tex=vb.replace('\n',' '),cross_layer_tokens='IDENTICAL_EXCEPT_EXPLICIT_OU_OR_TRANSLATION_AND_SPACING',authority_evidence=ev,scan_comparison='MANUALLY_VISUALLY_CHECKED'))
  all_u.append(dict(printed_page=p,authority_pdf_page=p+17,scope_leaf=p-62,unit_id=a['id'],structure=a['structure'],fr_tex_lines=f"{a['start']}-{a['end']}",en_tex_lines=f"{b['start']}-{b['end']}",math_segments=len(ma),authority_evidence=ev,french_audit='SOURCE_CONFIRMED',english_audit='FULL_CORRESPONDENCE_REVIEWED'))
  for l,u in [('fr',a),('en',b)]:
   for n,line in enumerate(u['body'].splitlines(),u['start']):
    if line.strip():all_l.append(dict(printed_page=p,authority_pdf_page=p+17,layer=l,unit_id=u['id'],edition_tex_line=n,tex_line=line,authority_evidence=ev,status='CHECKED_AGAINST_PRINT' if l=='fr' else 'FULL_STRUCTURAL_TRANSLATION_CHECKED',note='Editable TeX line, not physical scan-line number. Manual source collation plus mechanical cross-layer math check; control lines encode source structure.'))
 app=R/f'apparatus/pages/p{p:03}.md';app.write_text(f'# Printed p. {p}\n\nAuthority: exact-scope leaf {p-62}; full-PDF page {p+17}.\n\n{notes[p]}\n\nSource ambiguity: none.\nBody conjectural emendation: none.\nAuthor footnotes on this page: none.\nReview: Prompt03 direct source collation; final independent Prompt04 cold audit not executed.\n')
 catalog.append(dict(printed_page=p,authority_pdf_page=p+17,scope_leaf=p-62,entry=str(app.relative_to(R)),classification='Direct authority transcription; local notation, continuities and furniture retained.',source_ambiguity='NONE',body_emendation='NONE',status='SOURCE_REVIEWED_S03'))
 rec=dict(schema='dirichlet-page-record-v2',printed_page=p,authority_pdf_page=p+17,scope_leaf=p-62,role='AUTHOR_TEXT_FRENCH',origin='DIRECT_AUTHORITY_TRANSCRIPTION',source_image=f'qa/s03/source/p{p:03}_authority.png',source_image_sha256=sha(R/f'qa/s03/source/p{p:03}_authority.png'),french=dict(path=str(paths['fr'].relative_to(R)),sha256=sha(paths['fr'])),english=dict(path=str(paths['en'].relative_to(R)),sha256=sha(paths['en'])),units=[u for u in all_u if u['printed_page']==p],source_ambiguities=[],apparatus_path=str(app.relative_to(R)),apparatus_sha256=sha(app),source_audit='VISUAL_PAGEWISE_AND_LINEWISE_COMPLETED_S03',english_alignment='FULL_ARGUMENT_AND_MATH_REVIEWED',accepted_layers=['fr','en','apparatus'],notes='No author footnote on this leaf.',cold_audit='NOT_EXECUTED_PROMPT04_REQUIRED')
 wj(R/f'state/pages/p{p:03}.json',rec)
wt(R/'apparatus/CATALOGUE.tsv',catalog)
for suffix,rows in [('UNIT_ALIGNMENT.tsv',all_u),('FORMULA_AUDIT.tsv',all_m),('SOURCE_LINE_AUDIT.tsv',all_l)]:
 wt(Q/suffix,rows);old=rd(R/'qa/s02'/('CUMULATIVE_'+suffix));wt(Q/('CUMULATIVE_'+suffix),old+rows)
wj(Q/'CONTENT_AUDIT_COUNTS.json',dict(new_author_pages=list(range(87,99)),aligned_units=len(all_u),paired_math_segments=len(all_m),french_editable_lines=sum(x['layer']=='fr' for x in all_l),english_editable_lines=sum(x['layer']=='en' for x in all_l),author_footnotes_added=0,source_ambiguities=[],prior_source_issues_retained=[66,70,77,82,85],new_diff_rows=2,method='Manual visual source comparison; complete translation alignment; mechanical math pairing. Not independent cold audit.',math_count_limit='Includes isolated variables, inline formulae, display blocks, and labels; not a count of equations. Mixed prose/display minipages are recursively tokenized.'))
print('S03:',len(all_u),'aligned units,',len(all_m),'paired math segments,',len(all_l),'TeX lines; 12 pages and apparatus records; cumulative ledgers expanded.')
