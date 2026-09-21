from pathlib import Path
import csv,json,hashlib,subprocess,os,shutil,fitz
R=Path(__file__).resolve().parents[1]
def write_tsv(rel,rows,cols=None):
 p=R/rel;p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('w',encoding='utf8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=cols or list(rows[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
def hashfile(p):return hashlib.sha256(p.read_bytes()).hexdigest().upper()
copy=R/'copy_matter';copy.mkdir(exist_ok=True)
(copy/'p063.txt').write_text("RECHERCHES SUR LES DIVISEURS PREMIERS\nD’UNE CLASSE DE FORMULES DU QUATRIÈME\nDEGRÉ.\n\nPAR\n\nM. G. LEJEUNE DIRICHLET,\nPROF. DE MATH. A BRESLAU.\n\nCrelle, Journal für die reine und angewandte Mathematik, Bd. 3 p. 35—69.\n",encoding='utf8')
(copy/'p064.txt').write_bytes(b'')
write_tsv('ledgers/COPY_MATTER_LEDGER.tsv',[
{'printed_page':63,'authority_pdf_page':80,'scope_leaf':1,'role':'REPRINT_TITLE_COPY_MATTER','folio_visible':'NO','reader_action':'EXCLUDED_FROM_BOTH_AUTHOR_READERS','record':'copy_matter/p063.txt','verified_observation':'Title in three lines; PAR; M. G. LEJEUNE DIRICHLET,; PROF. DE MATH. A BRESLAU.; Crelle citation Bd. 3 p. 35—69. between two rules. Digital Google watermark recorded separately, not original print.','evidence':'qa/source/p063_authority.png','status':'VISUALLY_VERIFIED'},
{'printed_page':64,'authority_pdf_page':81,'scope_leaf':2,'role':'BLANK_VERSO_COPY_MATTER','folio_visible':'NO','reader_action':'EXCLUDED_FROM_BOTH_AUTHOR_READERS','record':'copy_matter/p064.txt','verified_observation':'No original printed text. Empty diplomatic text file (zero bytes). Digital Google watermark is not author text.','evidence':'qa/source/p064_authority.png','status':'VISUALLY_VERIFIED'}])
rows=[]
for p in range(63,99):
 role='COPY_MATTER' if p<65 else 'AUTHOR_TEXT'
 status='COPY_LOGGED' if p<65 else ('ACCEPTED_S01' if p<=74 else 'UNPROCESSED_UNVERIFIED_R28' if p<=80 else 'UNPROCESSED_NO_INHERITED_TEXT')
 rows.append({'printed_page':p,'authority_pdf_page':p+17,'scope_leaf':p-62,'role':role,'fr_status':status,'en_status':status,'apparatus_status':status,'occurrences_in_each_current_reader':1 if 65<=p<=74 else 0})
write_tsv('ledgers/TOPOLOGY.tsv',rows)
furniture=[]
for p in range(65,75):
 furniture.append({'printed_page':p,'folio_as_printed':'' if p==65 else str(p),'running_head_as_printed':'' if p==65 else 'RECHERCHES SUR LES DIVISEURS PREMIERS' if p%2==0 else 'D’UNE CLASSE DE FORMULES DU QUATRIÈME DEGRÉ.','imprint_as_printed':'G. Lejeune Dirichlet’s Werke.' if p in [65,73] else '', 'signature_as_printed':{65:'9',67:'9*',73:'10'}.get(p,''),'rules':'short rule below title; rule after opening paragraph' if p==65 else 'footnote separator' if p==71 else '','evidence':f'qa/source/p{p:03d}_authority.png','disposition':'FR furniture reproduced; EN running heads and imprint translated; not counted as additional author pages'})
write_tsv('ledgers/PAGE_FURNITURE.tsv',furniture)
seams=[
(65,66,'dans la suite.','1. / „Si l’on peut attribuer','paragraph closes; section 1 begins'),
(66,67,'résidus quadratiques par rapport à p.','„Si les nombres A et A\'','new quoted proposition'),
(67,68,'on aura, p étant','de la forme 4n+1, (k/p)=1.','same sentence; no invented connective'),
(68,69,'(h/p)=-1, (h\'/p)=-1, (h\'\'/p)=-1, etc.','d’où il suit, en multipliant:','same argument; lower-case d'),
(69,70,'celle que nous venons de considérer.','Nous aurons ainsi:','source paragraph boundary retained'),
(70,71,'8n+4.“','Il y a un troisième théorème','new theorem introduction'),
(71,72,'relation identique (2^ν/p)=(2^ν/p),','on aura ce résultat: / (α)','same sentence; author footnote stays on p71'),
(72,73,'b étant de la forme 4n+3:','(g/b)=1, ...; (h/b)=-1, ...','the announced displayed relations start p73'),
(73,74,'En substituant la valeur qu’elle donne','pour u^((p-1)/2) dans la congruence','same sentence, same substitution'),
]
write_tsv('qa/PAGE_SEAM_AUDIT.tsv',[{'left_page':a,'right_page':b,'left_explicit':x,'right_explicit':y,'observation':obs,'authority_evidence':f'qa/source/p{a:03d}_authority.png; qa/source/p{b:03d}_authority.png','fr':'CHECKED','en':'CHECKED'} for a,b,x,y,obs in seams])
write_tsv('ledgers/SESSION_PLAN_STATUS.tsv',[{'prompt':1,'scope':'63-74','author_pages':'65-74','status':'SOURCE_AND_BUILD_COMPLETE; FINAL_VISUAL_RECEIPT_REQUIRED','next_cursor':2},{'prompt':2,'scope':'75-86','author_pages':'75-86','status':'NOT_EXECUTED','next_cursor':3},{'prompt':3,'scope':'87-98','author_pages':'87-98','status':'NOT_EXECUTED','next_cursor':4},{'prompt':4,'scope':'63-98','author_pages':'65-98','status':'NOT_EXECUTED','next_cursor':'COMPLETE_ONLY_AFTER_FINAL_GATES'}])
notes={
65:('No conjectural emendation.','The title, memoir heading, both rules, and the signature/imprint are recorded. The source does not show the folio 65; that number is supplied by the fixed topology, not as printed text.'),
66:('Unqualified converse retained.','The second paragraph asserts that solvability for every prime factor of B implies solvability for B. That unrestricted assertion is reproduced in both editions. As an editorial check, A=3 and B=9 give a counterexample: x^4≡3 (mod.3) is solvable, whereas fourth powers modulo 9 are 0, 1, 4, 7, never 3. No qualification is silently inserted.'),
67:('No conjectural emendation.','The two quoted residue assertions and the opening of section 2 are source-confirmed. The author explicitly allows repeated odd prime factors. The sentence ending “p étant” continues on p.68.'),
68:('Lexical and display fidelity.','The print reads “en vertu de théorèmes connus”, not R27’s “en vertu des théorèmes connus”. All four two-row relation displays are retained in full. This leaf continues the paragraph begun on p.67.'),
69:('No conjectural emendation.','The leaf begins with lower-case “d’où”. Both sign alternatives, the parenthesis that (p−1)/4 is even, and both 8n residue-class pairs are retained. The final sentence introducing the sum of two squares ends on this leaf.'),
70:('Legible printed sign inconsistency retained.','In the prose beginning “Le produit”, K is called a divisor of φ′²+2u′². The plus is clear in the witness, whereas the earlier factorization on the same leaf has φ′²−2u′². The plus is retained in both editions. The surrounding argument indicates a likely printed error; this is an editorial diagnosis, not an emendation.'),
71:('Footnote restored to the witness.','R27’s r=ρ²∓1 is replaced by the printed r=bσ²±1. In the norm identity both occurrences reduced to + in R27 are restored to ±: (rt±bsu)²−b(ru±st)²=p. The printed *) anchor, note text, and italic book title are retained. The extra closing parenthesis after R27’s French footnote is removed. This is repair of the inherited transcription, not correction of the source.'),
72:('No conjectural emendation.','Labels (α), (β), and (β′), their placement, all six-term relation arrays, and the concluding sentence announcing the next leaf’s reciprocity relations are retained. No generic product symbol replaces the written factors.'),
73:('No conjectural emendation.','The initial relation array, label (γ), both congruences, the two cases p=8n+1 and p=8n+5, and the in-text final congruence are retained. The final substitution sentence continues on p.74.'),
74:('Batch boundary, not an end of the paper.','The beginning completes p.73’s substitution sentence. Section 4 begins here. The two-by-two factor display at the bottom is retained with its final full stop. No terminal rule or completion statement is supplied. Page 75 has not been transcribed or accepted in Prompt 01.')
}
for p,(head,body) in notes.items():
 (R/f'apparatus/pages/p{p:03d}.md').write_text(f'# Printed p. {p}\n\nAuthority: exact-scope leaf {p-62}; full-PDF page {p+17}; `qa/source/p{p:03d}_authority.png`.\n\n**{head}** {body}\n',encoding='utf8')
write_tsv('apparatus/CATALOGUE.tsv',[{'printed_page':p,'authority_pdf_page':p+17,'scope_leaf':p-62,'entry':f'apparatus/pages/p{p:03d}.md','classification':h,'source_ambiguity':'NONE','body_emendation':'NONE','status':'SOURCE_REVIEWED'} for p,(h,t) in notes.items()])
write_tsv('qa/NOTE_AUDIT.tsv',[{'printed_page':71,'authority_pdf_page':88,'note_id':'p071.fn01','source_anchor':'*) after impair, before full stop','english_anchor':'*) after odd, before full stop','source_region':'qa/source/p071_footnote_detail.png','r27_defects':'r=ρ²∓1; two + signs in norm identity; numeric marker; extra ) in FR; non-italic title','accepted_readings':'r=bσ²±1; (rt±bsu)²−b(ru±st)²=p; printed *) marker; no extra ); italic title','status':'FULL_NOTE_TRANSCRIBED_TRANSLATED_AND_REVIEWED'}])
(R/'qa/SOURCE_PRINT_ISSUES.json').write_text(json.dumps({'unresolved_source_ambiguities':[],'retained_source_issues':[{'page':66,'kind':'unqualified assertion','editorial_counterexample':{'A':3,'B':9,'fourth_power_residues_mod_9':sorted({pow(x,4,9) for x in range(9)})},'emendation':False},{'page':70,'kind':'legible plus sign conflicts with preceding minus sign','printed_prose':'phi_prime_squared + 2*u_prime_squared','earlier_display':'phi_prime_squared - 2*u_prime_squared','emendation':False}]},indent=2)+'\n')
# Separate, restrained two-page apparatus reader.
tex=r'''\documentclass[11pt]{article}
\usepackage[a4paper,margin=26mm]{geometry}
\usepackage{fontspec}
\setmainfont{lmroman10-regular.otf}[BoldFont=lmroman10-bold.otf,ItalicFont=lmroman10-italic.otf,BoldItalicFont=lmroman10-bolditalic.otf]
\usepackage{amsmath,amssymb,microtype}
\usepackage[unicode,hidelinks]{hyperref}
\setlength{\parindent}{0pt}\setlength{\parskip}{7pt}
\hypersetup{pdftitle={Paper IV — Apparatus — Prompt 01},pdfauthor={Editorial apparatus}}
\begin{document}
{\LARGE Paper IV}\par
{\large Apparatus to printed pp. 65–74}\par
Prompt 01. French source edition and independent English translation.

\section*{Witness and editorial treatment}
The controlling witness is the attached exact-scope PDF, leaves 3–12, corresponding
to full-volume PDF pages 82–91. All ten inherited R27 scan leaves agree with these
authority pages at 72 dpi. R27 is a comparator, not the authority; its original
bytes remain preserved. Pages 63–64 are copy matter, not author prose.

The French preserves the printed wording, notation, quoted statements, display
grouping, and page seams. The English preserves all arguments and mathematical
relations, including the legible source problems described below. No conjectural
repair is inserted into either text. Running heads and the imprint are translated
in the English reader. The author’s note remains a footnote; editorial comments
appear only here.

\section*{P. 66: unqualified converse}
In the paragraph beginning \emph{Il est facile de voir}, the print states a converse
from solvability for every prime factor of $B$ to solvability for $B$ itself.
The unrestricted statement is retained. It needs qualification when repeated prime
factors occur: for example, $A=3$, $B=9$ gives a solution modulo the prime factor $3$,
but no solution modulo $9$, whose fourth-power residues are $0,1,4,7$.
This counterexample is an editorial calculation, not text supplied by the witness.

Authority: exact-scope leaf 4 / full-PDF page 83, second paragraph.

\section*{P. 70: the printed plus sign}
In the paragraph beginning \emph{Le produit}, the print calls $K$ a divisor of
$\varphi'^2+2u'^2$. The plus sign is legible. Earlier on the same page, the factorization
uses $\varphi'^2-2u'^2$. The plus is reproduced in both editions. The surrounding
argument indicates a likely printed error; that diagnosis is editorial and does
not change the diplomatic reading.

Authority: exact-scope leaf 8 / full-PDF page 87, the paragraph before the quoted theorem.

\newpage
\section*{P. 71: restoration of the author’s note}
The inherited formula $r=\rho^2\mp1$ is an algebraic rewriting, not the printed
expression. The witness reads $r=b\sigma^2\pm1$, followed by $s=\rho\sigma$.
The two signs reduced to $+$ in R27’s norm identity are also printed as $\pm$:
\[
(rt\pm bsu)^2-b(ru\pm st)^2=p.
\]
Both editions restore the printed forms. The source marker is $*)$, attached after
\emph{impair} (\emph{odd} in English), before the sentence’s full stop. R27’s extra
closing parenthesis in the French body is not present in the source. The book title
\emph{Théorie des Nombres} is italic in the source; it is rendered as
\emph{Theory of Numbers} in English. The citation’s printed numbering is retained.

Authority: exact-scope leaf 9 / full-PDF page 88, complete footnote.

Detail witness: \path{qa/source/p071_footnote_detail.png}.

\section*{Other page records}
Pages 65, 67–69, and 72–74 require no conjectural emendation. The separate pagewise
apparatus files record the title and rules, the lexical reading \emph{de théorèmes}
on p.68, lower-case \emph{d’où} on p.69, the equation labels and repeated factor
arrays, and the exact continuation points. The catalogue has one record for each
of the ten author pages.

The sentence at the foot of p.67 resumes at the head of p.68; that at the foot of
p.71 resumes with the result labelled $(\alpha)$ on p.72. The reciprocity display
announced at the end of p.72 begins p.73. The substitution sentence at the foot of
p.73 resumes with its power of $u$ on p.74. No bridging prose is supplied.

Section 4 begins on p.74 and continues beyond this batch. The reader stops after
the two-by-two factor display on p.74. This is the Prompt 01 boundary, not the end
of Paper IV. Pages 75–98 are not accepted by this checkpoint.

\section*{Layout record}
The readers are re-typeset, not photographic facsimiles. Original page boundaries,
paragraph starts, display membership, formula punctuation, and the author-note
anchor are retained. Physical within-page line wrapping and justification are not
copied; line-end word division is reflowed, without changing lexical hyphens such
as \emph{tout-à-fait} and \emph{à-peu-près}. These layout choices are explicit, not
silent lexical normalization. The untouched authority and page images remain the
reference for the original lineation and letterforms.
\end{document}
'''
(R/'apparatus/main.tex').write_text(tex,encoding='utf8')
out=R/'qa/build/apparatus';out.mkdir(parents=True,exist_ok=True)
for k in [1,2]:
 proc=subprocess.run(['xelatex','-interaction=nonstopmode','-halt-on-error',f'-output-directory={out}','main.tex'],cwd=R/'apparatus',stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,env={**os.environ,'SOURCE_DATE_EPOCH':'1790006400','FORCE_SOURCE_DATE':'1'})
 (out/f'pass{k}.stdout.txt').write_text(proc.stdout);shutil.copyfile(out/'main.log',out/f'pass{k}.log')
 print('apparatus',k,proc.returncode,proc.stdout[-300:]);assert proc.returncode==0
reader=R/'readers/PAPER_IV_APPARATUS_S01.pdf';shutil.copyfile(out/'main.pdf',reader);doc=fitz.open(reader)
od=R/'qa/visual/apparatus';od.mkdir(parents=True,exist_ok=True)
for i,page in enumerate(doc):page.get_pixmap(matrix=fitz.Matrix(1.75,1.75),alpha=False).save(od/f'page{i+1:02d}.png')
print('APPARATUS PAGES',len(doc))
