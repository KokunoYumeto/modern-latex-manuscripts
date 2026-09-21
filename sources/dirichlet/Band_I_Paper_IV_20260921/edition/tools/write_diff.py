"""Record source-backed R27 repairs; this ledger is not a diplomatic edition."""
from pathlib import Path
import csv
R=Path(__file__).resolve().parents[1]
rows=[]
def add(p,layer,before,after,where,disposition='CORRECTED_FROM_ATTACHED_AUTHORITY'):
    pages=[p] if isinstance(p,int) else list(p)
    evidence='; '.join(f'full PDF {q+17} = scope leaf {q-62}: qa/source/p{q:03d}_authority.png' for q in pages)
    rows.append(dict(printed_page=';'.join(map(str,pages)),authority_pdf_page=';'.join(str(q+17) for q in pages),layer=layer,before=before,after=after,evidence=evidence+'; '+where,disposition=disposition))
add([63,64],'TOPOLOGY','R27 broad pp.63–74 label, with only ten witnesses (PDF82–91); no title/blank author-text distinction in that label','p63 title and p64 blank verso logged as copy matter, excluded from both author readers; ten R27 witnesses map to pp65–74','Title and blank directly inspected; fixed page map checked','COVERAGE_LABEL_CORRECTED; ZERO_INHERITED_ACCEPTANCE')
add(65,'FR_EN_STRUCTURE','No horizontal rules in R27 title/opening text','Short rule between title and memoir heading; rule after the introductory paragraph','Rule below title and rule above bottom imprint/signature')
add(65,'EN_HEADING','First memoir.','1st Memoir. (ordinal superscript in reader)','Printed 1er Mémoire.','SOURCE_HEADING_ALIGNMENT')
add([65,67,73],'FR_EN_FURNITURE','Original signatures/imprints absent from R27 editable readers','p65: signature 9 and imprint; p67: 9*; p73: signature 10 and imprint; English imprint translated','Bottom furniture on each authority leaf')
add(list(range(65,75)),'FR_EN_TOPOLOGY','R27 freely flowing author files (9 French / 8 English PDF pages), not ten source-page records','Independent p065.tex–p074.tex and ten pages in each reader; original folios/running heads, with no visible folio on p65','Full current source batch; no copy leaf in either reader','SOURCE_PAGE_BOUNDARIES_RESTORED')
for a,b,end,start in [
(65,66,'dans la suite.','1. / „Si l’on peut attribuer'),
(66,67,'résidus quadratiques par rapport à p.','„Si les nombres A et A\''),
(67,68,'p étant','de la forme 4n+1'),
(68,69,'(h″/p)=−1, etc.','d’où il suit'),
(69,70,'celle que nous venons de considérer.','Nous aurons ainsi:'),
(70,71,'8n+4.“','Il y a un troisième théorème'),
(71,72,'relation identique (2^ν/p)=(2^ν/p),','on aura ce résultat: (α)'),
(72,73,'b étant de la forme 4n+3:','(g/b)=1, …; (h/b)=−1, …'),
(73,74,'En substituant la valeur qu’elle donne','pour u^((p−1)/2) dans la congruence')]:
    add([a,b],'FR_EN_PAGE_SEAM','No source page break at '+end+' | '+start,end+' | EXPLICIT SOURCE PAGE BREAK | '+start,'Last/first source lines; English breaks at corresponding argument position','SOURCE_PAGE_SEAM_RESTORED')
add([66,67,69,70,71,74],'FR_QUOTATION','»…« in seven quoted propositions','„…“ in all seven propositions (two on p66, one on each other listed page)','Opening and closing quotation marks on authority pages')
add([66,67,69,73,74],'FR_EN_NOTATION','\\pmod p / \\pmod k, printed by R27 without the source’s dot','(mod.p) / (mod.k); 11 occurrences: p66×3, p67×1, p69×3, p73×3, p74×1','Every modular-congruence occurrence on the listed authority pages')
add([67,68,69,71,72,73],'FR_EN_NOTATION','Centered \\cdots in written prime-factor products','Baseline \\ldots in u=2^νkk′k″… and t=gg′g″…×hh′h″… and their Legendre-symbol products','Printed factor ellipses; repeated factors retained, not replaced by product notation')
add([66,67,68,73],'FR_EN_DISPLAY_MEMBERSHIP','R27 separate displays for A-congruences; p=t²+2u²; (p/k)=1; opening (k/p)=1; final (u/p) and u-congruence','These relations restored to the source prose lines; subsequent original displays retained','p66 three in-text congruences; p67 two in-text relations; p68 opening; p73 final prose')
add(68,'FR_EN_DISPLAY_MEMBERSHIP','Eight separately delimited one-row displays; FR also contains a spurious row break after (2p/g)=1','Four two-row arrays: (2p/g_i),(2p/h_i); (2/g_i),(2/h_i); (p/g_i),(p/h_i); (g_i/p),(h_i/p); all written entries preserved','Four paired source arrays, including all primes, signs, equalities and etc.')
add([72,73],'FR_EN_DISPLAY_MEMBERSHIP','Separate one-row displays for corresponding g- and h-relations','Three paired arrays on p72, followed by the paired reciprocity array at the head of p73','Source grouping of all six entries in each pair')
add([70,74],'FR_EN_DISPLAY_MEMBERSHIP','Two successive displays for the four E,F,K,L factor identities','One two-by-two displayed block per source page, preserving row/column order','Four-identity blocks near bottom of each source page')
add([72,73],'FR_EN_EQUATION_LABELS','(α), (β), (β′), (γ) placed in prose before a separate display','Same labels placed at the left of their corresponding equations','p72 labels α, β, β′; p73 label γ')
add(68,'FR_TEXT','en vertu des théorèmes connus','en vertu de théorèmes connus','Line immediately before the (2/g_i),(2/h_i) array')
add(69,'FR_EN_TEXT','D’où / Hence','d’où / hence','First prose line, continuing preceding page')
add(70,'FR_PUNCTUATION','de l’une de celles-ci 8n+1','de l’une de celles-ci: 8n+1','Le produit paragraph, after the parenthesis about φ′ and u′')
add(71,'FR_EN_MATH','r=ρ²∓1','r=bσ²±1','Complete author footnote; detail qa/source/p071_footnote_detail.png')
add(71,'FR_EN_MATH','(rt+bsu)²','(rt±bsu)²','Footnote norm identity, first binomial; qa/source/p071_footnote_detail.png')
add(71,'FR_EN_MATH','−b(ru+st)²','−b(ru±st)²','Footnote norm identity, second binomial; qa/source/p071_footnote_detail.png')
add(71,'FR_EN_NOTE_ANCHOR','Automatic numeric footnote marker','Printed *) marker after impair / odd, before full stop','Body anchor and corresponding source footnote')
add(71,'FR_PUNCTUATION','impair\\footnote{…}). Faisons','impair\\sourcefootnote{…}. Faisons','Source body has no closing parenthesis after its footnote anchor')
add(71,'FR_EN_NOTE_TYPOGRAPHY','Théorie des Nombres / Theory of Numbers in roman type','Théorie des Nombres / Theory of Numbers in italics','Footnote bibliographical title; qa/source/p071_footnote_detail.png')
add(71,'EN_CITATION','nos. 44, 45','no. 44. 45','Printed footnote citation, no.44.45; qa/source/p071_footnote_detail.png','SOURCE_CITATION_PUNCTUATION_RESTORED')
add(73,'EN_MATH_PROSE','the number ν is equal to 1','the number ν is =1 (equality sign retained as mathematical token)','Source: le nombre ν est =1','PRINTED_RELATION_RESTORED')
# Each English punctuation/phrase adjustment is enumerated. Alternate faithful phrasing is not called a mistranslation.
punct={
66:('…±1 (mod p), and…; …residue with respect to p; in the second…','…±1 (mod.p) and…; …residue with respect to p, in the second…','Source congruence punctuation and quoted two-case sentence'),
68:('one of these two forms, …; h,h′,h″,… contained in these two forms, …','one of these two forms: …; h,h′,h″,…, contained in these two forms: …','Both class definitions and their printed colons'),
69:('on multiplying,; these forms,; one of these,; theorem …8n+7, or…','on multiplying:; these forms:; one of these:; theorem …8n+7 or…','Opening product, residue-class explanation and quoted theorem'),
70:('We shall thus have [no colon]; after transposing,; changes it into [no colon]; one of these forms,','We shall thus have:; after transposing:; changes it into:; one of these forms:','Equation introductions and three residue-class introductions'),
71:('or of one of these, 8n+5, 8n+7','or of one of these: 8n+5, 8n+7','Third theorem at top of page'),
72:('one has the result [no colon]; are such that [no colon, twice]; that is,; gives/obtains/will have [no colons]; 4n+3,','one has the result:; are such that: [twice]; that is:; gives/obtains/will have:; 4n+3:','Introductions to all nine mathematical displays/continuations on this source leaf'),
73:('give [no colon]; one always has [no colon]; one obtains [no colon]','give:; one always has:; one obtains:','Introductions to product, γ, and raised congruence'),
74:('one has [no colon, twice]; after transposing,; changes it into [no colon]; the equations [no colon]','one has: [twice]; after transposing:; changes it into:; the equations:','Initial congruence and section 4 equation introductions')}
for p,(a,b,e) in punct.items(): add(p,'EN_PUNCTUATION',a,b,e,'SOURCE_PUNCTUATION_ALIGNMENT')
add(69,'EN_TRANSLATION','Therefore; Let us return','Thus one has:; Return','On a donc:; Reprenons l’équation','FULLER_SOURCE_CORRESPONDENCE; NO_SEMANTIC_ERROR_ASSERTED')
add(70,'EN_TRANSLATION','We therefore have','We therefore have the equations:','Nous avons donc les équations:','OMITTED_NOUN_RESTORED')
add([68,69,72,73,74],'FR_EN_PARAGRAPHS','Free-flow layout does not retain source paragraph continuation across the reconstructed page seams','Continuation blocks remain unindented; actual new paragraphs retained separately; p73 Si p… stays in its source paragraph','Printed paragraph starts and exact page seams; see qa/UNIT_ALIGNMENT.tsv','SOURCE_PARAGRAPH_STRUCTURE_RESTORED')
with (R/'SOURCE_BACKED_DIFF.tsv').open('w',encoding='utf8',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['printed_page','authority_pdf_page','layer','before','after','evidence','disposition'],delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
print('Source-backed diff rows:',len(rows))
