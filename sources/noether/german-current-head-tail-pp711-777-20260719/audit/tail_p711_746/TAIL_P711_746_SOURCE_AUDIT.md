# Noether collected pp. 711-746 complete-page source-audit log

## 2026-07-19 setup

The source authority is the same IA-derived 72-page tail packet used for the sealed pp. 747-777 checkpoint. Packet pages 1-36 map to source-PDF pages 725-760 and collected pp. 711-746. An exact 36-page slice and 36 complete-page 650-dpi renders were created. OCR output is retained only as a locator.

The existing canonical per-page ledger contained no records for pp. 711-746. This is first whole-page closure work, not a recheck of an earlier complete-page claim.

## Pages 711-712

Printed p. 711, the title and first contents page, was compared in full. No delta was found.

Printed p. 712 exposed the first confirmed transcription drift. The source Section 25 contents title reads "Normaldarstellung von K_r mit Galoisschen maximalen kommutativen Teilkoerpern", with blackletter K_r and the plural phrase. The live TeX instead has blackletter R_r and changes the phrase to singular "Galoisschem maximalem kommutativem Teilkoerper". A 1300-dpi exact contents crop makes all three distinctions unambiguous. This is logged as TAIL-20260719-F005 and will be integrated into a successor cumulative after the page sweep.

## Page 713

Printed p. 713 was compared through the direct-representation display. Its prose and mathematics are complete. The current transcription removes the source-visible spaces in `z. B.` and two `M. Z.` abbreviations; TAIL-20260719-F006 records this low-risk prose/source-style repair separately from mathematical defects.

## Page 714

The reciprocal-homomorphism display was enlarged at 1300 dpi. The source uses a diagonal-slashed right arrow, while the current TeX substitutes `\mapsto`; TAIL-20260719-F007 restores the exact source symbol as `\nrightarrow`. All remaining page text and formulas were checked through the page-break continuation of the reciprocal-module definition without another delta.

## Page 715

The page's transformation and matrix formulas match the source. TAIL-20260719-F008 restores the source's singular `Die Multiplikation des d. D. M.` in place of the current plural `Die Multiplikationen`; this is a prose correction, not a formula change.

## Page 716

All displayed basis-change, module, and homomorphism identities were checked without a mathematical delta. TAIL-20260719-F009 restores three source-emphasis loci omitted by the current TeX: the first conclusion, proposition 2, and `Beweis.`.

## Page 717

The coefficient-extension identities, commutation rules, and product formula were checked without a mathematical delta. TAIL-20260719-F010 restores all three `M. Z.` spacings in footnote 1 and the source emphasis on the concluding two-sentence statement.

## Page 718

The representation counts, quotient decomposition, and field-isomorphism statements match the source. TAIL-20260719-F011 restores source emphasis on `erster Art`, `zweiter Art`, and the following iff criterion; no mathematical content changes.

## Page 719

The splitting-field, isomorphism, group, and main-theorem text is complete and mathematically correct. TAIL-20260719-F012 restores source emphasis on the phrase defining the Galois group and on both numbered short formulations of the main theorem.

## Page 720

The complete dense degree calculation was checked: both inequalities, the `s\cdot t` degree sum, the `e_\nu^{(i)}` decomposition, and the representation identity match. TAIL-20260719-F013 restores only `w. z. b. w.` spacing and source emphasis on `Zeigen wir noch`.

## Page 721

The automorphism action, orbit decomposition, invariant element, and opening component relation were checked without a mathematical delta. TAIL-20260719-F014 restores the source emphasis on `genügt` in the sufficiency sentence.

## Page 722

Two 1300-dpi focused checks exposed substantive and structural drift. TAIL-20260719-F015 restores the field summands from current blackletter `R_i` to source blackletter `K_i`. TAIL-20260719-F016 adds the third horizontal continuation-dot row omitted from both inverse matrices. TAIL-20260719-F017 separately restores source spacing in `M. Z.`, `d. h.`, and `w. z. b. w.`. The matrix entries and all remaining formulas match.

## Page 723

The general-extension proof formulas match. In the group-ring proof opening, a 1300-dpi crop confirms that the source has `h\equiv0(p)`, not the current equality; TAIL-20260719-F018 records the mathematical repair. TAIL-20260719-F019 restores `M. Z.` spacing and source emphasis on `Gruppenring von G in P`.

## Page 724

TAIL-20260719-F020 restores the three source `\not\equiv` relations currently flattened to `\ne`: the opening reversal and the two later `h`/`h_i` loci. A second 1300-dpi crop confirms that the parenthetical `h=0(p)` and `h_i=0(p)` are genuinely ordinary equalities and must remain unchanged. TAIL-20260719-F021 restores `M. Z.` and `w. z. b. w.` spacing plus the source emphasis on the character terminology.

## Page 725

TAIL-20260719-F022 restores the remaining source `h\not\equiv0(p)` relation at the idempotent conclusion. The character case formulas and sum relation match. TAIL-20260719-F023 restores `d. h.` spacing and the source emphasis on the full concluding character relation.

## Page 726

The dual-group product, root-of-unity correspondence, invariant definitions, and every displayed formula were checked without a mathematical delta. TAIL-20260719-F024 restores the source emphasis that the current TeX flattened in the opening proposition, `Beweis.` label, complete main theorem, and both numbered formulations.

## Page 727

The continuation proof, homomorphism-product array, translated invariant statements, and final character sum all match the source. TAIL-20260719-F025 restores three abbreviation spacings. TAIL-20260719-F026 separates the source's bold paragraph marker `2.` from its roman continuation; the current paragraph command incorrectly bolds the whole phrase.

## Page 728

The Chapter IV setup, inner-automorphism definition, module action, invariant-module construction, and proof opening were checked in full. TAIL-20260719-F027 restores the complete lemma statement as a source-emphasized block; its formulas and prose are already complete.

## Page 729

The basis extension, equations (1)--(3), coefficient comparison, and conclusion were checked without a mathematical delta. TAIL-20260719-F028 restores the source's numbered proof marker, and TAIL-20260719-F029 restores `d. h.` and `w. z. b. w.` spacing.

## Page 730

The simplicity theorem proof, both ideal-containment chains, reciprocal-module definition, and the opening well-definedness argument match the source. TAIL-20260719-F030 restores the source-emphasized theorem statement, TAIL-20260719-F031 restores the second proof marker, and TAIL-20260719-F032 restores `w. z. b. w.` spacing.

## Page 731

This dense page was checked line by line. The coefficient-reduction formula, every expanded module-action row, continuation dots, margin annotations, distributive laws, and both sides of the associativity comparison match the source. No patch is required.

## Page 732

Satz 2, the representation-degree argument, Satz 3, the direct/reciprocal module passage, and both tensor-extension displays were checked without a mathematical delta. TAIL-20260719-F033 restores one `w. z. b. w.` spacing.

## Page 733

The algebraic-closure center proof, simplicity proof, matrix-ring form, absolute component count, splitting-field definition, footnote, and Satz 4 statement all match. TAIL-20260719-F034 restores `w. z. b. w.` spacing in the first two proofs.

## Page 734

Both parts of the Satz 4 proof and both parts of the Satz 5 proof were compared through every field-extension, centralizer, and module formula. No mathematical delta was found. TAIL-20260719-F035 restores `w. z. b. w.` spacing at the three proof conclusions. TAIL-20260719-F036 restores the source's bold numbered marker `2.` while leaving the following proof text roman.

## Page 735

Satz 6, its page-local footnote, the full Satz 7 statement and conjugacy formula, Satz 8, and the opening of Satz 9 were checked directly. The footnote identity and bibliographic text are present and the mathematics matches. TAIL-20260719-F037 restores the one remaining `w. z. b. w.` spacing in the Satz 7 proof.

## Page 736

The quaternion conjugation identities, basis display, real-square argument, Wedderburn theorem, finite-group count, and Section 21 quotient-group definition all match. TAIL-20260719-F038 restores `w. z. b. w.` spacing. TAIL-20260719-F039 restores the source's emphasis on `eines`, `abgeschlossen`, and `Null`.

## Page 737

Satz 11, its three subclaims, the reciprocal-isomorphism reduction, the field tower, and the extension-count statement were checked through the page break. No mathematical delta was found. TAIL-20260719-F040 restores `d. h.` spacing.

## Page 738

The complete extension-lemma dimension argument was checked: every ideal decomposition, rank equality, idempotent product, and invariance conclusion matches. TAIL-20260719-F041 restores `d. h.` at the page opening and `w. z. b. w.` at the proof close.

## Page 739

This dense page is a no-patch closure. Both direct-product matrix-ring derivations, all class representatives, the class homomorphism, and the inverse-class rank calculation match the source.

## Page 740

The simple-body factorization theorem was checked through all class identities, degree inequalities, inner-conjugation steps, and the final product decomposition. The Section 23 opening hypothesis also matches. No patch is required.

## Page 741

The splitting-field decomposition, conjugate ideals, matrix-unit expansion, operator isomorphisms, and induced index action all match. TAIL-20260719-F042 restores one `d. h.` spacing.

## Page 742

Every pseudomatrix-unit relation, factor-system index, conjugacy law, and associated-system quotient was checked directly. TAIL-20260719-F043 restores source emphasis on `Pseudomatrizeneinheiten` and the first defining occurrence of `assoziiert`.

## Page 743

The factor-system invariance argument and multiplication Hilfsbetrachtung were checked through equation (1). TAIL-20260719-F044 is a substantive symbol repair: the source defines `\mathfrak l_i=\mathfrak K_{r\Gamma}e_i`, while the active TeX drops `\Gamma` and incorrectly writes `\mathfrak K_r e_i`.

## Page 744

The conjugate-left-ideal Hilfssatz and proof parts 1--4 were checked through all idempotent, isomorphism, product, and complementary-ideal identities. No mathematical delta was found. TAIL-20260719-F045 restores the source-emphasized opening clauses of proof parts 1 and 2.

## Page 745

The Hilfssatz inverse-element close, transported pseudomatrix units, factor-system product theorem, and opening product decomposition all match. TAIL-20260719-F046 restores source emphasis on the product-definition phrase and the `Zum Beweis` marker.

## Page 746

The invariant ideal, factor-system product, pseudomatrix-unit, conjugacy, and `\xi` relations were checked through the page break. TAIL-20260719-F047 restores source emphasis on the descended `\mathfrak K_r`-ideal statement. No formula delta was found on this page.

## Final bounded disposition

All 36 assigned source pages were opened and disposed. The 43 logged fix groups were integrated into `cum_de_Local_20260719_Tail_p711_777.tex`; 32 pages required at least one patch and four pages closed with no patch. XeLaTeX passed twice. The cumulative remains 466 pages, and pass 2 has no unresolved-reference, rerun, fatal, emergency-stop, undefined-control, or LaTeX-error flag.

Output pp. 416-446 were rendered before and after at 220 dpi. Twenty-five pages changed and six control pages were pixel-identical. The complete after-render contact and the dense mathematical loci were visually reopened; no clipping, overlap, broken glyph, or incoherent reflow was found. The exact predecessor-to-successor diff is `../diff_Tail_p747_777_to_Tail_p711_777_plus_P04_followup.diff`.

Bounded status: collected pp. 711-746 are closed against the included best available complete witness on this exact head. Together with the preceding pp. 747-777 checkpoint, the complete collected-volume tail pp. 711-777 now has page-level source dispositions. This statement does not certify any earlier collected-volume page or the complete author.
