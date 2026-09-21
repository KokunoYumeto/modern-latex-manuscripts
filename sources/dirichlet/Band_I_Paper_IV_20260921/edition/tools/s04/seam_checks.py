"""Bind manual seam observations to current bilingual source excerpts and fresh scan images."""
from audit_support import R,Q
from global_checks import write_tsv
notes={
65:'Introduction closes before its rule; section1 begins at p66, without merging title/blank copy matter into prose.',
66:'Quadratic-residue assumptions for A,A-prime,p are followed by the next quoted multiplication proposition; no invented connective sentence.',
67:'The incomplete p étant continues de la forme4n+1; source signature9* is furniture, not an interruption of the sentence.',
68:'Final reciprocal-symbol array is multiplied at opening d’où on p69; all factors and lowercase opening retained.',
69:'The sum-of-two-squares substitution is announced before the equations beginning Nous aurons ainsi on p70.',
70:'Second theorem closes in quotation; p71 starts the distinct third theorem and then section3.',
71:'Multipliant ... comma continues on aura ce résultat and alpha display; the full author note remains anchored and printed on p71.',
72:'Final colon announces the two-row reciprocity array at the head of p73; no relation moved to the preceding page.',
73:'En substituant la valeur qu’elle donne continues pour u^((p-1)/2) and its congruence on p74.',
74:'Four E,F,K,L identities close p74; p75 immediately proves E,F coprime. No inherited continuation title or new section inserted.',
75:'Delta-prime display closes p75; p76 uses it to decide the sign of t/b.',
76:'The announced task of deciding t/b=±1 continues with finding chi satisfying chi^2=p modulo b at p77.',
77:'The sentence ends toutes les valeurs and resumes de b, telles que; no extension of the stated restricted proof.',
78:'Quoted 7 corollary ends followed by etc.; p79 begins section5, without an invented missing corollary.',
79:'Final list deliberately ends h, and resumes h-prime,h-double-prime,... at p80; no duplicated h.',
80:'Separate t=4n+1 and t=4n+3 sign cases are united in eta at p81.',
81:'Final E/a,F/a symbols are followed by the difference2psi parity argument at p82; the later printed p^2 anomaly remains untouched.',
82:'Final psi±t symbol formula is compared with theta at opening of p83; numerator order retained.',
83:'The phrase ou, ce qui est la continues même chose on p84 before the 8n alternatives.',
84:'The a=5,a=13 discussion continues with the actual 20n± forms example on p85; no invented a=13 example.',
85:'The Addition opening sentence ends beaucoup and resumes simplifiées on p86; its heading and both rules remain on p85.',
86:'The full three-prime reciprocal row continues with its product on p87, with no new heading; terminal ellipsis/point remains in the row.',
87:'Final congruence is interpreted at p88 opening, then compared with gamma-prime to form delta-prime.',
88:'D’un autre continues côté in the same coprimality proof. The third prose line of p89 literally uses b, restored from the scan.',
89:'Last psi s+chi s symbol with matched ± sign is multiplied using reciprocity at p90; the sign-choice explanation spans neither omission nor duplication.',
90:'French lexical division der-/nière retained exactly across page boundary; English corresponding phrase is the last/equation.',
91:'Theorem citation ends plusieurs and resumes fois, que l’équation: followed by eta-prime on p92.',
92:'Last word Si continues u est pair; the condition is not lost or duplicated at p93.',
93:'Final colon announces the full theta-prime labelled statement at p94, not an unlabelled new theorem.',
94:'Les nombres K et L seront donc continues dans ce cas impairs l’un et l’autre at p95.',
95:'Sentence ends chacun and continues d’eux sera de la forme4n+2 at p96.',
96:'The comparison ends lorsque and resumes u est impair at p97; negative and positive alternatives both retained.',
97:'L’analyse qu’il faut appliquer continues à ce second cas at p98, where the author explicitly declines to repeat the proof.'}
rows=[]
for p,note in notes.items():
 row={'printed_seam':f'{p}/{p+1}','authority_pdf_pages':f'{p+17}/{p+18}','scope_leaves':f'{p-62}/{p-61}','manual_observation':note,'source_images':f'qa/s04/source/p{p:03}_authority.png;qa/s04/source/p{p+1:03}_authority.png','result':'MANUALLY_RECHECKED'}
 for lang in ['fr','en']:
  a=[x for x in (R/f'editions/{lang}/pages/p{p:03}.tex').read_text().splitlines() if x.strip() and not x.startswith('%')]
  b=[x for x in (R/f'editions/{lang}/pages/p{p+1:03}.tex').read_text().splitlines() if x.strip() and not x.startswith('%')]
  row[f'{lang}_ending_tex']=' '.join(a[-3:]);row[f'{lang}_opening_tex']=' '.join(b[:3])
 rows.append(row)
write_tsv(Q/'ALL_AUTHOR_SEAMS.tsv',rows)
print('33 manual seam observations bound to current source excerpts')
