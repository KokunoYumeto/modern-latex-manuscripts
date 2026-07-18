# Hi Claude - Codex notes for SGA 6 idx616--624

These are marks placed where the SGA 6 English synchronization found a
French-workpass or printed-source problem. The English fragment is a
provisional, source-checked draft wherever a correction below has not yet
been resolved in the French authority. Nothing here edits or silently
promotes the French workpass.

## Clear workpass transcription defects

1. **idx616 / printed 603 / source-PDF 606 / workpass around line 14307**
   - Workpass: `O_Y -> f_* O_Y ==> ...`
   - Scan: `O_Y -> f_* O_X ==> ...`
   - English draft: uses `f_* O_X`.

2. **idx618 / printed 605 / source-PDF 608 / workpass around line 14364**
   - Workpass: `R'(f_T)_*(O_(X'_T)^*)`.
   - Scan: `R^1(f_T)_*(O_(X'_T)^*)`.
   - English draft: uses `R^1`.

## Printed-source defects requiring an editorial ruling

3. **idx616 / printed 603 / source-PDF 606: terminal eta/n index**
   - The first factorization on the page prints `f_eta:Y_eta=Y`.
   - Lemma 2.6 immediately below describes the same finite-factorization
     mechanism with terminal `Y_n=Y`.
   - The English draft provisionally uses `f_n:Y_n=Y`. If eta is intentional
     and carries a distinct role, that role needs to be stated; none is
     visible in the page or proof.

4. **idx617 / printed 604 / source-PDF 607: undefined `A_i` family**
   - The page defines only `A=O_Y`, `B_0=f_*O_X`, and the recursive `B_i`.
   - It then prints
     `B_(i-1) tensor_(A_i) B_(i-1)`, `Spec(A_i)`, and
     `B subset A_i, B=A_i`.
   - The equalizer construction forces
     `B_(i-1) tensor_(B_i) B_(i-1)`, `Spec(B_i)`, and
     `A subset B_i, A=B_i`.
   - The English draft uses those forced corrections. Both the low-resolution
     scan and the high-resolution supplement confirm that the printed page
     itself has `A_i`; this is not merely OCR.

5. **idx619 / printed 606 / source-PDF 609: missing prime and lowercase `t`**
   - In the reverse-inclusion paragraph, `g_beta` lies in
     `Gamma(X,O_X')`, but the page's second nilradical occurrence prints
     `nilrad Gamma(X,O_X)`. The argument requires
     `nilrad Gamma(X,O_X')`, as in the first occurrence.
   - The exact sequence then prints one isolated `f_t` among otherwise
     consistent `f_T` terms.
   - The same paragraph defines
     `v:Gamma(X,O_X)->Gamma(X,O_X')` and then prints
     `h=sum v(h_beta) tensor t_beta in Gamma(X_T,O_XT)`. This is ill-typed:
     the summands on the right live on `X'`. The lift in the displayed target
     is `h=sum h_beta tensor t_beta`; applying `v` recovers the printed sum.
   - The English draft uses `O_X'`, `f_T`, and the typed lift `h`
     consistently.

6. **idx621 / printed 608 / source-PDF 611: reversed filtration indices**
   - Printed: `I_0=I superset I_1 ... superset I_n=0`,
     `N I_i subset I_(i-1)`, example `I_i=N^i I`, and immersions
     `X_i -> X_(i-1)` where `X_i` is defined by `I_i`.
   - With that decreasing filtration and example, the operative relations
     must be `N I_(i-1) subset I_i` and
     `X_(i-1) -> X_i`.
   - The English draft uses the coherent indexing. Please either amend the
     French workpass with an editorial/source note or tell the English lane
     to revert to a literal-but-inconsistent transcription.

7. **idx622 / printed 609 / source-PDF 612: Remark 3.6 arrows inherit the
   idx621 reversal**
   - Printed exact sequence:
     `Pic_(X_(i-1)/S) -> Pic_(X_i/S) -> V(Q_i)`.
   - Once the filtration is coherently read as an immersion
     `X_(i-1) -> X_i`, Proposition 3.1 gives pullback in the opposite
     direction:
     `Pic_(X_i/S) -> Pic_(X_(i-1)/S) -> V(Q_i)`.
   - Printed cokernel:
     `coker(Pic^0_(X_s/s) -> Pic^0_(Y_s/s))`.
   - For the original nilpotent immersion `X -> Y`, pullback is
     `Pic^0_(Y_s/s) -> Pic^0_(X_s/s)`, so the unipotent cokernel must use
     this latter direction.
   - The English draft provisionally corrects both arrows. These corrections
     should be resolved together with item 6, not independently.

## Notation caveat, not silently normalized

8. **idx621--622 / printed 608--609 / source-PDF 611--612**
   - Proposition 3.5 states `f:X -> Y` as the nilpotent immersion, but its
     proof then resumes Proposition 3.1's symbols `X'` and structural `f` in
     `O_(X')`, `R^i f_*(I)`, and `(f_K)_*O_(X'_K)`.
   - The English fragment retains those symbols and explicitly says that the
     notation is that of 3.1. This is an editorial clarity addition, not a
     claim that the printed notation is self-contained.

## Exact continuation

The English draft through idx624 ends cleanly after `Z` is identified with
`Deff`. Continue at idx625 / printed 612 / source-PDF 615, beginning with the
canonical monomorphism from `Deff` to `Rec`.
