from pathlib import Path
import csv,io
R=Path(__file__).resolve().parents[2]
s=(R/'prior_evidence/S01/apparatus/main.tex').read_text()
s=s.replace('Apparatus — Prompt 01','Apparatus — Prompt 02').replace('Apparatus to printed pp. 65–74','Apparatus to printed pp. 65–86').replace('Prompt 01. French source edition','Prompts 01–02. French source edition')
s=s.replace('leaves 3–12, corresponding\nto full-volume PDF pages 82–91. All ten inherited R27 scan leaves agree with these\nauthority pages at 72 dpi. R27 is a comparator, not the authority; its original\nbytes remain preserved.', 'leaves 3–24, corresponding\nto full-volume PDF pages 82–103. The original R27 and R28 bytes remain preserved\nas unverified prior work; only source-replayed derivative text is accepted.\nPages 81–86 are transcribed directly from the authority.')
s=s.replace('The catalogue has one record for each\nof the ten author pages.', 'The cumulative catalogue has one record for each\nof the twenty-two accepted author pages.')
s=s.replace('Section 4 begins on p.74 and continues beyond this batch. The reader stops after\nthe two-by-two factor display on p.74. This is the Prompt 01 boundary, not the end\nof Paper IV. Pages 75–98 are not accepted by this checkpoint.', 'Section 4 begins on p.74. Prompt 01 ended after its two-by-two factor display;\nPrompt 02 resumes with the proof that $E$ and $F$ are relatively prime on p.75.\nAll earlier page sources remain byte-identical. The cumulative readers now stop\nafter the reciprocity row at the foot of p.86, not at the end of Paper IV.\nPages 87–98 are not accepted by this checkpoint; the final cold audit remains pending.')
extra=r'''
\newpage
\section*{P. 77: the printed variable $t$}
The paragraph beginning \emph{En combinant ce résultat} says that the outcome
depends on whether $t$ has the form $8n+7$ or $8n+3$. The letter is visibly $t$,
not $b$. Both editions retain it. The preceding equality is
$\left(\frac{t}{b}\right)=\left(\frac{2}{b}\right)$, while Theorem I on p.78 gives the
corresponding alternatives in terms of $b$. This discrepancy is recorded only
here; no substitution is made in the author text.

Authority: exact-scope leaves 15–16 / full-PDF pages 94–95.

\section*{P. 82: the printed square on $p$}
In the first paragraph, following \emph{On voit, par l'équation}, the source
reads $p^2=\varphi^2+\psi^2$. The superscript 2 is legible and is reproduced in
both editions. On p.81 the decomposition is introduced as $p=\varphi^2+\psi^2$.
The extra square is likely a printing error, but that diagnosis is editorial,
not a warrant for changing the diplomatic reading.

Authority: exact-scope leaf 20 / full-PDF page 99, first paragraph.

\section*{P. 85: $ps$, not $ps^2$}
The parenthetical replacement equation reads $t^2+au^2=ps$. There is no
superscript on this $s$, whereas the two immediately preceding equations
both have $ps^2$ on the right. The printed difference is retained in both
editions without supplying a conjectural exponent.

Authority: exact-scope leaf 23 / full-PDF page 102, the long methodological paragraph.

\section*{New page records and seams}
No conjectural emendation is required on pp.75–76, 78–81, 83–84, or 86. The
source equation labels $(\delta),(\delta'),(\varepsilon),(\zeta),(\eta),(\theta)$ and
$(\alpha')$ retain their local scope; the renewed $(\alpha')$ on p.86 belongs to the
\emph{Addition}. No renumbering is imposed.

The phrase ending p.77 continues with \emph{de $b$} on p.78. The factor list at
the foot of p.79 ends with $h,$ and resumes with $h',h'',\ldots$ on p.80.
The two sign cases on p.80 are joined in $(\eta)$ on p.81. The sentence at the
foot of p.83 continues with \emph{même chose} on p.84. The \emph{Addition au mémoire
précédent} heading and both adjacent rules are on p.85; its opening sentence
continues with \emph{simplifiées} on p.86. No bridging prose is inserted.

There are no new author footnotes on pp.75–86. The note mentioned on p.86
refers to the note near the beginning of section 3 on p.71, preserved in the
cumulative readers. Source signatures $10^*$, $11$, and $11^*$ occur on
pp.75, 81, and 83 respectively; p.81 also carries the volume imprint.
'''
s=s.replace(r'\end{document}',extra+'\n'+r'\end{document}')
(R/'apparatus/main.tex').write_text(s)
notes={
75:('R28 replay; continuation of section 4. Equations (delta) and (delta-prime), all five displays, and signature 10* retained. The added R28 title is not in the source and is excluded. The opening proof uses exactly the E,F,K,L factorization on p.74.','NONE'),
76:('Both choices of chi are retained separately, with the repeated product identity in each case. All six displays and all modular punctuation are retained. No author footnote.','NONE'),
77:('The paragraph En combinant ce resultat visibly uses t in the alternatives 8n+7 and 8n+3; both editions preserve t. Compare the preceding (t/b)=(2/b) and the b alternatives in Theorem I on p.78. This source discrepancy is discussed separately, not silently repaired. The final sentence resumes with de b on p.78.','LEGIBLE_SOURCE_DISCREPANCY_RETAINED'),
78:('Theorem I and both quoted corollaries are complete. The author\'s explicit restriction of the earlier proof, the bound 136, and the exception 79 are retained. No claim of general proof is inserted here.','NONE'),
79:('Section 5 begins here. All six entries of each two-row factor array, the brace and label (epsilon), and the full signed product remain. The final list stops at h, and resumes with h-prime on p.80.','NONE'),
80:('The (zeta) array, full discussion of the sign changes, and separate results for t=4n+1 and t=4n+3 are retained. The p.81 formula (eta) unites these two cases. No new theorem heading or terminal rule is supplied.','NONE'),
81:('Direct authority transcription. Labels (eta) and (theta), both congruences in one display, both alternatives, all four factor identities, and final E,F symbols retained. Signature 11 and volume imprint included.','NONE'),
82:('The first paragraph visibly prints p^2=phi^2+psi^2, following On voit, par l\'equation. Both editions preserve the squared p; compare p=phi^2+psi^2 on p.81. Likely printing error is an editorial diagnosis only. All exponent sums keep their printed order.','LEGIBLE_SOURCE_DISCREPANCY_RETAINED'),
83:('Direct authority transcription. Both residue alternatives and both divisibility cases are preserved, with paired plus/minus and minus/plus signs. Final sentence continues on p.84; signature 11* retained.','NONE'),
84:('Direct authority transcription. Theorem II, its two cases, and the precise generalization claim relying on the auxiliary proposition are preserved; a=5 and a=13 examples are introduced as printed.','NONE'),
85:('Direct authority transcription. In the parenthetical replacement equation the source reads t^2+au^2=ps, without a superscript on s, unlike the preceding ps^2 equations; retained without conjectural completion. Complete methodological discussion and Addition heading with both rules preserved. Opening sentence continues on p.86.','LEGIBLE_SOURCE_VARIANT_RETAINED'),
86:('Direct authority transcription. New local label (alpha-prime), the full parity argument, t-prime/u-prime construction and reference to the p.71 note, and all three factorization/reciprocity displays retained. No content from p.87 is transcribed or accepted.','NONE')}
rows=list(csv.DictReader((R/'prior_evidence/S01/apparatus/CATALOGUE.tsv').open(),delimiter='\t'));print('CAT FIELDS',rows[0].keys())
for page,(note,issue) in notes.items():
    (R/f'apparatus/pages/p{page:03d}.md').write_text(f'# Printed p. {page}\n\nAuthority: exact-scope leaf {page-62}; full-PDF page {page+17}.\n\n{note}\n\nSource ambiguity: none.\nSource issue status: {issue}.\n')
# Keep same catalogue columns.
fields=list(rows[0])
for page,(note,issue) in notes.items():
    d={k:'' for k in fields}
    for k in fields:
        if k=='printed_page':d[k]=page
        elif 'path' in k or k in ('apparatus_file','entry'):d[k]=f'apparatus/pages/p{page:03d}.md'
        elif 'authority_pdf' in k:d[k]=page+17
        elif 'scope' in k:d[k]=page-62
        elif 'status' in k or 'acceptance' in k:d[k]='ACCEPTED_SOURCE_BACKED_S02'
        elif k=='classification':d[k]=issue
        elif k=='source_ambiguity':d[k]='NONE'
        elif k=='body_emendation':d[k]='NONE'
        else:d[k]=note
    rows.append(d)
with (R/'apparatus/CATALOGUE.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
