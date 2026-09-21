"""Append only concrete source-backed S02 corrections; retain all 44 S01 rows verbatim."""
from pathlib import Path
import csv,io,json
R=Path(__file__).resolve().parents[2]; rows=[]
fields=['printed_page','authority_pdf_page','layer','before','after','evidence','disposition']
def add(pages,layer,before,after,location,disposition='CORRECTED_FROM_ATTACHED_AUTHORITY'):
 if isinstance(pages,int):pages=[pages]
 rows.append(dict(zip(fields,[';'.join(map(str,pages)),';'.join(str(p+17) for p in pages),layer,before,after,'; '.join(f'full PDF {p+17} = scope leaf {p-62}: qa/s02/source/p{p:03d}_authority.png' for p in pages)+'; '+location,disposition])))
add(75,'FR_EN_STRUCTURE',"R28 added display title and ‘1er Mémoire. Suite: pages imprimées 75–80.’ / corresponding English continuation title",'No added title; p75 continues section 4 directly with the E/F coprimality proof, under the printed running head','Top of p75: running head, folio 75, then Il est très facile; no memoir title here')
add(list(range(75,81)),'FR_EN_TOPOLOGY','R28 free-flow units build to 5 French / 5 English reader pages; no source-bounded folios or running heads','Six source-bounded page records p075–p080 in each edition, with folios 75–80 and alternating source running heads; cumulative readers retain p065–p074 before them','All six full leaves; English running heads translated','SOURCE_PAGE_BOUNDARIES_RESTORED')
add(75,'FR_EN_FURNITURE','No source signature in R28 editable author readers','Printed signature 10* retained at the foot of p75','Bottom signature below the delta-prime display')
seams=[(75,76,'(δ′) t±ψ≡0 (mod.b), ((t∓ψ)/b)=1.','Il résulte du théorème énoncé'),(76,77,'(t/b)=1 ou (t/b)=−1.','Il suffira de chercher un nombre'),(77,78,'pour toutes les valeurs','de b, telles que'),(78,79,'etc.','5. / Désignons par a'),(79,80,'les nombres premiers h,',"h′, h″, … sont en nombre pair ou impair.")]
for a,b,end,start in seams:
 add([a,b],'FR_EN_PAGE_SEAM',f'R28 continuous flow at {end} | {start}',f'{end} | EXPLICIT SOURCE PAGE BREAK | {start}','Last/first source lines; English breaks at the corresponding clause, including the split factor list','SOURCE_PAGE_SEAM_RESTORED')
add([75,79,80],'FR_EN_EQUATION_LABELS','(δ), (δ′), (ε), (ζ) inserted as ordinary material at the left of a centred display','Each label aligned at the left display margin; epsilon/zeta braces and every array entry retained','p75 delta and delta-prime; p79 epsilon brace; p80 zeta brace')
for p in [75,76,77,78]:
 n=(R/f'editions/fr/pages/p{p:03d}.tex').read_text().count(r'\md{b}')
 add(p,'FR_EN_MODULAR_PUNCTUATION',f'R28 (mod b), without printed abbreviation point, at {n} occurrence(s)',f'(mod.b), with printed abbreviation point, at all {n} occurrence(s)','Congruences on this leaf; no congruence sign or modulus changed')
add(77,'FR_QUOTATION_MARKS','»c désignant … soit résoluble.«','„c désignant … soit résoluble.“','Quoted auxiliary theorem in the lower part of the leaf')
add(78,'FR_QUOTATION_MARKS','»…« around Theorem I and the two particular theorems','Printed „…“ around all three statements','Theorem I and the p=12n+1 / p=28n+1,28n+9,28n+25 quoted statements')
add(78,'FR_EN_HEADING','R28 small capitals for Théorème I. / Theorem I.','Source mixed-case, letter-spaced centred heading; English title translated without small-cap normalization','Centred Théorème I. heading')
add([75,76,77,78,79,80],'FR_EN_PARAGRAPH_STRUCTURE','R28 generic paragraph spacing/indentation, detached from physical source continuations','Unindented continuing blocks on pp75–76 and at heads of pp77–78/80; source paragraph starts retained, including quoted statements and section 5','Visible source paragraph indentation and the two cross-page text splits; see qa/s02/UNIT_ALIGNMENT.tsv','SOURCE_PARAGRAPH_STRUCTURE_RESTORED')
add([75,78],'EN_BIBLIOGRAPHICAL_TITLE','Untranslated italic Théorie des Nombres in the English R28 text','Italic Theory of Numbers, consistent with accepted S01 translation treatment','p75 reciprocal-law citation and p78 table reference; French titles remain unchanged','SOURCE_TITLE_TRANSLATED')
add(75,'EN_TEXT_AND_PUNCTUATION','relatively prime); and it is known, by a known theorem that follows easily … (… no. 197), that every','relatively prime) and one knows by a known theorem that follows easily … (… no. 197) that every','French: (où … sont premiers entre eux) et l’on sait par un théorème connu qui se déduit facilement … (… no. 197) que tout','FULL_SOURCE_CORRESPONDENCE_RESTORED')
add(75,'EN_PUNCTUATION','odd), and suppose; common divisor; and since; with respect to b; so that','odd) and suppose; common divisor, and since; with respect to b, so that','French corresponding junctions: impair) et supposons; diviseur commun, et comme; par rapport à b, de sorte')
add(76,'EN_PUNCTUATION','remarkable result: if','remarkable result: If','Final unindented source paragraph: résultat remarquable: Si')
add(77,'EN_PUNCTUATION','the equation t²±cδu²=p is soluble','the equation t²±cδu²=p, is soluble','Source auxiliary theorem retains a comma after the displayed-in-prose relation p, before soit résoluble')
add(78,'EN_PUNCTUATION','(where ψ is supposed even), one; p: if; biquadratic residue according; b=7, etc.; with respect to p if','(where ψ is supposed even) one; p: If; biquadratic residue, according; b=7 etc.; with respect to p, if','All corresponding punctuation in Theorem I, the b=3,b=7 introduction and the two quoted corollaries; both inserted commas after the even-parenthesis removed')
add(79,'EN_PUNCTUATION','p=t²−au², where','p=t²−au² where','First paragraph of section 5: p=t²−au² où, without a comma after the relation')
add(80,'EN_PUNCTUATION','The number of changes will therefore be even when','The number of changes will therefore be even, when','Source: Le nombre des changements sera donc pair, lorsque')
add(86,'FR_EN_DISPLAY_PUNCTUATION','S02 first direct-source draft: three trailing baseline dots in each of the last two reciprocity rows','Three baseline ellipsis dots plus the printed terminal point in both rows (four visible dots per row)','Two final rows, enlarged in qa/s02/source/p086_reciprocity_detail.png; before-draft files preserved in qa/s02/build/repair_history','DIRECT_SOURCE_DRAFT_CORRECTED')
f=io.StringIO(newline='');w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
s=f.getvalue();(R/'qa/s02/SOURCE_BACKED_DIFF_S02.tsv').write_text(s)
old=(R/'prior_evidence/S01/SOURCE_BACKED_DIFF.tsv').read_bytes();assert old.endswith(b'\n')
(R/'SOURCE_BACKED_DIFF.tsv').write_bytes(old+s.split('\n',1)[1].encode())
print('S02 correction rows:',len(rows),'cumulative:',44+len(rows))
