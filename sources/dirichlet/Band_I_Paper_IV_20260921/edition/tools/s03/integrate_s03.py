"""One-time S03 integration from preserved S02 main sources; do not run on later state."""
from pathlib import Path
R=Path(__file__).resolve().parents[2]
for lang in ('fr','en'):
 base=(R/f'history/S02/superseded/editions/{lang}/main.tex').read_text()
 base=base.replace('pp.65–86','pp.65–98').replace('Prompt 02;','Prompt 03;')
 add=''
 for p in range(87,99):
  add+=f'\n\\clearpage\n\\setcounter{{page}}{{{p}}}\\pdfbookmark[0]{{{p}}}{{p{p}}}\n\\fancyfoot{{}}\n'
  if p in (89,97):
   imp='G. Lejeune Dirichlet’s Werke.' if lang=='fr' else 'G. Lejeune Dirichlet’s Works.'
   add+=rf'\fancyfoot[L]{{\fontsize{{7}}{{9}}\selectfont {imp}}}'+'\n'
  if p in (89,91,97):
   sig={89:'12',91:'12*',97:'13'}[p]
   add+=rf'\fancyfoot[C]{{\small {sig}}}'+'\n'
  if p==98:
   head="RECHERCHES SUR LES DIVISEURS PREMIERS D'UNE CLASSE DE FORMULES ETC." if lang=='fr' else 'RESEARCHES ON THE PRIME DIVISORS OF A CLASS OF FORMULAE ETC.'
   add+=rf'\fancyhead[CE]{{\fontsize{{7.4}}{{10}}\selectfont {head}}}'+'\n'
  add+=rf'\input{{pages/p{p:03}.tex}}'+'\n'
 (R/f'editions/{lang}/main.tex').write_text(base.replace(r'\end{document}',add+r'\end{document}'))
# Preserve all existing apparatus discussions; update extent and add S03 treatment.
p=R/'apparatus/main.tex';s=(R/'history/S02/superseded/apparatus/main.tex').read_text()
s=s.replace('Prompt 02}', 'Prompt 03}').replace('pp. 65–86','pp. 65–98').replace('Prompts 01–02.','Prompts 01–03.')
s=s.replace('leaves 3–24','leaves 3–36').replace('pages 82–103','pages 82–115').replace('Pages 81–86 are transcribed','Pages 81–98 are transcribed')
s=s.replace('twenty-two accepted author pages','thirty-four author pages accepted for sequential intake')
s=s.replace('All earlier page sources remain byte-identical. The cumulative readers now stop\nafter the reciprocity row at the foot of p.86, not at the end of Paper IV.\nPages 87–98 are not accepted by this checkpoint; the final cold audit remains pending.',
'All earlier page sources remain byte-identical. The reciprocity row at the foot\nof p.86 is followed on p.87 by its product. The integrated readers cover author\npp.65–98 exactly once; the independent final cold audit remains pending.')
s=s.replace(r'\section*{New page records and seams}',r'\section*{Pp. 75–86: page records and seams}')
add=r'''
\newpage
\section*{Pp. 87–98: the concluding pages}
These twelve pages are transcribed directly from exact-scope leaves 25–36,
full-PDF pages 104–115. No inherited transcription supplies their text.
No conjectural emendation is introduced. The seven new local labels
$(\beta'),(\gamma'),(\delta'),(\varepsilon'),(\zeta'),(\eta'),(\vartheta')$
and their references remain as printed; in particular, the renewed primed
labels in the \emph{Addition} are not renumbered to avoid earlier repetitions.
The source's open theta form is represented by $\vartheta$ in these new labels.

The source uses \emph{impairement pair} on pp.87 and 93; the translation
retains the term as \emph{oddly even}. In these passages it means twice an odd
number, as the source's accompanying conditions $\nu=1$ and $\mu=1$ indicate.
This explanation belongs to the apparatus, not the author text.

On p.90 the comparison sign has two equality strokes beneath the greater-than
stroke and is represented by $\geqq$. The factors $b^{2k+2}$, $b^{2h+1}$,
$b^{k-h}$, and $b^{h-k-1}$, and the subsequent reuse of $h$ in $g^2+bh^2$,
are retained. The two-by-two factor arrays on pp.88 and 94 preserve the printed
order; no symmetric rearrangement has been substituted.

\section*{Continuities and source furniture}
Seams 74/75 and 80/81 were rechecked against the scans: the first continues the
factor proof, and the second combines its two sign cases in $(\eta)$.
The 86/87 seam continues the prime-factor reciprocal-symbol row with its
product, without a new heading or an invented connecting sentence.

The French source divides \emph{der-nière} across 90/91: the page records retain
\emph{der-} at the end of p.90 and \emph{nière} at the start of p.91. The English
breaks at the corresponding phrase, \emph{the last / equation}. Other incomplete
sentences pass through the original page boundaries; the theorem announced on
p.93 is the labelled statement at the head of p.94. Pages 97/98 continue the
sentence about the second case. No new author footnote occurs on pp.87–98.

Signatures $12$, $12^*$, and $13$ occur on pp.89, 91, and 97. The volume imprint
occurs on pp.89 and 97. The extended running head and the final horizontal rule
on p.98 are retained in both readers, with the running head translated in English.
All closing examples for $a=5$ and $b=3$, and both alternative pairs of equations,
are included. No terminal word or further text is supplied after the rule.

\section*{Boundary and remaining audit}
Full-volume PDF page 115 is visibly printed p.98 and ends Paper IV. Page 116
is the next paper's title leaf and is inspected only to confirm exclusion.
It supplies no text to these editions. The immutable full-volume file and the
separately labelled boundary inspection image are provenance evidence, not
additional reader content.

The catalogue now has thirty-four author-page entries; title leaf63 and blank
verso64 remain only in the copy-matter and topology records. The retained source
issues on pp.66, 70, 77, 82, and 85 remain unchanged. Completion of Prompt03 does
not constitute the independent cold source audit required by Prompt04.
'''
p.write_text(s.replace(r'\end{document}',add+'\n'+r'\end{document}'))
