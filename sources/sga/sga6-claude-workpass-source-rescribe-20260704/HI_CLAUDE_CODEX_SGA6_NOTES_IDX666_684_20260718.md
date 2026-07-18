# Hi Claude - Codex notes for SGA 6 idx666--684

This note is intended to be copied beside the provisional French workpass at:

`C:\IL_GitHub\00_main_current\sources\sga\sga6-claude-workpass-source-rescribe-20260704`

I did not edit the French workpass. Its current committed certification stops at idx662 (commit `8ccdcf8ee`; SHA-256 `77703F2D7E8FF9000C2C1E7320A903A48ADE00BF62C8F5F240FF88C42ED82703`), so all items below concern provisional text. Coordinates keep current-rescribe index, printed page, and source-PDF page distinct.

## Clear scan/workpass differences

| idx | Printed | Source PDF | Observation | English handling / requested French action |
|---:|---:|---:|---|---|
| 670 | 657 | 660 | In Theorem 6.7(ii), the scan writes the Hilbert polynomial with `sum_{i=0}^r`; the workpass has `sum_{i=0}^q`. | English follows the scan (`r`). Please correct or annotate the workpass. |
| 673 | 660 | 663 | The scan begins with the proof of Corollary 6.11: the first assertion follows from 6.7(i), the second from 6.10, 1.8(i), 6.2 applied to `0 -> I -> O_P -> O_X -> 0`, and 1.3; then (ii) follows from (i) and 1.13. This paragraph is absent from the workpass. | English restores the full paragraph. Please insert it. |
| 673 | 660 | 663 | In Remark 6.12 the scan defines `O_{X_n}=O_Y/O_Y(-2Z)` and then has `0 -> O_{X_n}(-Z) -> O_{X_n} -> O_Z -> 0`. The workpass instead writes `0 -> O_X(-2Z) -> O_X -> O_Z -> 0`. | English follows the scan. Please correct the subscripts and twist. |
| 674 | 661 | 664 | In the proof of Corollary 6.14, the scan includes the reduction by a general codimension-`q` linear space and the inequalities `deg(X^q)=h^0(O_{X^q})`, `h^0(O_{X^q}) <= h^0(O_Y) <= e_q`. These steps are absent from the workpass. | English restores them. Please insert them. |
| 678 | 665 | 668 | Near the end of the proof of Corollary 7.4(i), the scan has `\langle c_1(L|_{X'})^2\rangle >= 0`; the workpass has `\langle c_1(L_{X'}^2)\rangle >= 0`. | English uses the scan's square of the first Chern class. Please correct the workpass. |
| 679 | 666 | 669 | Bibliography [6] and [7] include titles in the scan; the workpass drops both titles. Bibliography [2] repeats the journal/year/pages line in the scan, while the workpass silently collapses it. | English restores the titles and retains the source repetition pending an editorial decision. Please record the normalization explicitly if the repetition is removed. |
| 680--681 | 667--668 | 670--671 | The scan writes the derived exterior-power operation with a lowercase lambda, `widehat lambda^i`, throughout the section heading, functor, formulas (1.1)--(1.2), Dold--Puppe paragraph, and translation formula. The workpass uses capital `widehat Lambda^i`. Targeted 300-dpi high-resolution renders make the lowercase form clear. | English follows the scan (`\widehat{\lambda}^{i}`). Please change the capital Lambda instances in the workpass. |
| 681 | 668 | 671 | The scan states that the degree-`n` component of the semisimplicial module is `widehat lowercase lambda^i L'_n`. This parenthetical detail is absent from the workpass. | English restores it. Please insert it. |
| 681--682 | 668--669 | 671--672 | In Expose XIV 2.1, the scan names the relative cotangent complex `T_f`; the workpass substitutes `L^bullet`. | English follows the scan (`T_f`). Please correct or explain the normalization. |
| 682--683 | 669--670 | 672--673 | In Expose XIV 3.1, with `N` declared the conormal sheaf, the scan uses the dual `check N` in `Todd(-check N)`, `c_d(check N)`, and the `c_beta(check N)` arguments of (3.1). The workpass retains the check only in the Todd term and drops it in the other two formulas. | English restores all three checks. Please correct the two dropped checks. |
| 684 | 671 | 674 | The scan says formula (3.1) is of interest for `i >= d`, immediately followed by “Even for i=d=2...”. The workpass has `i>d`. | English uses `i >= d`. Please correct the workpass. |
| 684 | 671 | 674 | The added-note footnote is attached to the discussion of the groups `A^i(X)` in 3.2 and ends on this page with `Cf.`; both it and the main text of 3.3 continue on idx685. The workpass moves it into a freestanding note and completes it from later text. | English keeps a footnote at the source location and stops at `Cf.`. Please preserve a page-boundary marker if the workpass is resegmented. |

## Source-print corrections or ambiguities needing an explicit editorial ruling

| idx | Printed | Source PDF | Issue | Provisional English choice |
|---:|---:|---:|---|---|
| 670 | 657 | 660 | Theorem 6.7 defines `A_i^(q)(X_0,...,X_q;Y)` but later uses `A_{r-i}^{(r-q)}(c_{q-1},...,c_r;m)`, whose displayed argument count does not match the definition. | Source formula retained exactly; caveat logged. |
| 676 | 663 | 666 | In 7.1.3, expanding `L_1=L^p tensor H_1^q` should normally produce a `2pq <c_1(L)c_1(H_1)>` cross term. The printed equality instead reads `<c_1(L_1)^2> = p^2<c_1(L)^2> + q^2<c_1(H_1)^2> > 0`. Together with the preceding orthogonality equation, this deserves mathematical review. | Printed formula retained exactly; no silent repair. |
| 676 | 663 | 666 | Lemma 7.1.2 prints `H_Y^1(N^n(p))`; it is not explicit whether this is cohomology on `Y` of a restriction or support notation. | Literal `H_Y^1` retained. Please normalize only with an explicit note. |
| 677 | 664 | 667 | The scan says “the ideal `I` of `O_Y`” when defining the blow-up of the ideal of `Y` in `X`; mathematically the ideal is a subsheaf of `O_X`. The workpass already uses `O_X`. | English uses `I subset O_X` and records this source-print correction. |
| 677--678 | 664--665 | 667--668 | Corollaries 7.3 and 7.4 assume only that `M` is not numerically equivalent to `H`, but the asserted strict Hodge inequality fails for other numerical multiples such as `M=H^2`. The usual hypothesis is that `M` is not numerically proportional to `H`. | Source wording retained and flagged; do not publish without mathematical review. |
| 677 | 664 | 667 | The running header says `XII App.` although the text is Expose XIII Appendix. | Body unaffected; record as a scan header typo. |
| 679 | 666 | 669 | Bibliography [2] duplicates `Amer. J. Math. 1967 p. 94--103` on consecutive lines. | Retained in English pending explicit normalization. |

## Cursor

Continue at idx685 / printed672 / source-PDF675 / high-resolution page686. Do not supply punctuation before continuing: both the sentence after “relative cohomological purity theorem” and the footnote after `Cf.` are open at the idx684 boundary.
