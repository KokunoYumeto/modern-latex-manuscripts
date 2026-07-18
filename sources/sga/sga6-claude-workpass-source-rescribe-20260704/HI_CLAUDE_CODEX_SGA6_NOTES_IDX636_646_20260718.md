# Hi, this is Codex - SGA 6 notes for Claude, idx636-646

I source-checked current-rescribe idx636-646 against printed volume pages
623-633 (declared sga6.pdf source-PDF pages 626-636). These are the items
I think you will want to know about while repairing the French workpass.
The English fragment keeps every unresolved issue explicit; it does not
silently turn a conjectural repair into French authority.

## Clear workpass transcription repairs

1. idx639 / printed p. 626 / source-PDF p. 629: in the proof of Lemma
   2.4, the scan has
   \(\langle c_1(L)\cdot c_1(H)^{r-1}\rangle\). The workpass has
   \(c(L)\). The English restores \(c_1(L)\).

2. idx641 / printed p. 628 / source-PDF p. 631: the workpass has
   \(h^2(L(-a_1-2)=0\); the closing parenthesis after \(L(-a_1-2)\) is
   missing. The English closes it.

3. idx645 / printed p. 632 / source-PDF p. 635: the scan says that
   \(L'\) is the inverse image of \(L'_\alpha\). The workpass drops the
   prime in that occurrence and says \(L_\alpha\). The English restores
   \(L'_\alpha\).

## Printed-source issues that need a substantive decision

1. idx638 / printed p. 625: after defining \(L_1\to E'\), the printed
   composite is \(L'_K\to E'_K\to E_K\), although \(L'\) is not defined.
   The very next clause says that the composite comes from
   \(\delta:L_{1,K}\to L_K\), and the universal map has domain
   \(L_{1,K}\oplus L_{2,K}\). The English therefore uses \(L_{1,K}\) in
   the composite and flags this as pending.

2. The text passes directly from Lemma 2.5 to Lemma 2.7, but the proof
   of Lemma 2.7 begins, "By 1.7 and 2.6." There is no printed Lemma 2.6
   in this section or on the intervening pages. I retained the reference
   and flagged the missing lemma/number.

3. idx641 / Lemma 2.8: the printed lower bound ends with
   \(+\beta(\beta+1)\). The proof obtains
   \(a_0=\cdots-\beta_0\) and then invokes
   \(\beta_0\le\beta(\beta+1)\), which appears to yield
   \(-\beta(\beta+1)\), not a plus. The English preserves the printed
   plus sign and marks it source-sic pending mathematical review.

4. idx642 / proof of Lemma 2.9: equation (2.9.1) is used to show
   \(h^1(L(-n-1))=h^1(L(-n))\) for large positive \(n\). The next
   printed sentence invokes \(h^1(L(n))=0\) for \(n\gg0\) and concludes
   (i). The signs do not connect as written. The English preserves the
   printed positive sign and flags it; please decide whether \(L(-n)\)
   was intended or whether a missing duality argument resolves it.

5. idx644 / proof of Lemma 2.11: both the scan and workpass say
   \(\delta=\operatorname{supp}\{d(L_K)\}\). The following sentence
   twists every member by \(-\delta\) and requires a numerical upper
   bound, so the intended operation is plainly
   \(\delta=\sup\{d(L_K)\}\). The English uses \(\sup\) and flags the
   correction.

6. idx646 / Proposition 3.2(iii): item (ii) calls \(\Lambda\) a
   partie of the Picard scheme, item (iii) calls it a famille, and the
   proof again calls it a partie. The English normalizes item (iii) to
   "subset" and flags the normalization.

## Endpoint

idx646 is not a semantic endpoint. It ends after the displayed arrow

\[
\underline{\Pic}_{Y/S}\longrightarrow\underline{\Pic}_{X/S}
\]

in Definition 3.3. idx647 continues:

"is said to be of finite type if the inverse image of every bounded
family of classes of invertible sheaves on the fibers of \(X/S\) is a
bounded family of classes of sheaves on the fibers of \(Y/S\)."

No idx647 source text is included in the idx636-646 fragment.
