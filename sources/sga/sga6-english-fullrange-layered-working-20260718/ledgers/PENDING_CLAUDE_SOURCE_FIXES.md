# Hi Claude — this is Codex; merged SGA 6 English-tail source notes

This is the normalized durable handoff for English current-rescribe idx532--702 plus the ten unindexed terminal back-matter pages. I did **not** edit the French workpass. The current French file is commit `8ccdcf8eeef35cba9cc7ca09fe79e6b3f863becc`, SHA-256 `77703F2D7E8FF9000C2C1E7320A903A48ADE00BF62C8F5F240FF88C42ED82703`, and its certified source-rescribe boundary remains **idx662**.

Everything at idx663 onward is scan-checked English draft pending Claude/French-lane certification. The unindexed back matter has no invented current-rescribe indices. It ends at source-PDF 702 / printed page 700 / high-resolution page 714 with `Z(x)`.

## Merge policy

The four tranche notes below are preserved in full, once each, under explicit provenance headings. No exact duplicate note block occurred across the four inputs, so no substantive item was removed. Apparent thematic overlap is retained because the coordinates or editorial decisions differ.

---

## Preserved source note: idx532--646 sealed checkpoint

Source file: `C:\Users\Floris\Documents\interlanguage\03_projects\language_management\english_germanic\03_working_translations\sga6_cumulative_sync_idx532_646_en_20260718\PENDING_CLAUDE_SOURCE_FIXES.md`

<!-- BEGIN PRESERVED TRANCHE NOTE -->

# Pending Claude/source-control review

This file is the explicit draft layer requested by Floris. It separates
English synchronization decisions from corrections that have not yet been
accepted into the French workpass. Nothing here changes
sga6_fr_workpass.tex.

## Current English disposition

| Current idx | Printed page | Low-res PDF page | Issue | English used now | State |
|---:|---:|---:|---|---|
| 598 | 585 | 588 | French workpass loses the bars in the definitions of \(B_i\) and \(k_i\). | \(B_i=(\bar A_i)_{\mathfrak m_i}\), \(k_i=\bar A_i/\mathfrak m_i\), as printed in both scans. | Clear transcription fix; pending workpass incorporation. |
| 604 | 591 | 594 | French workpass has \(F(k)\to K(K)\). | \(F(k)\to F(K)\), as printed in both scans and required by the paragraph. | Clear transcription fix; pending workpass incorporation. |
| 606 | 593 | 596 | Source and workpass say that \(X_K\) is “still of finite type” although the hypothesis at this point is only that \(X\) is noetherian and \(K/k\) is of finite type. | “\(X_K\) is still noetherian,” the preserved property actually used in the argument. | Provisional mathematical emendation; Claude/editorial decision required. |
| 606 | 593 | 596 | Source and workpass leave the parenthesis after IV 2.12 unmatched. | Parenthesis closed in grammatical English. | Punctuation normalization; pending workpass incorporation. |
| 606 | 593 | 596 | Source and workpass say that regularity of \(X\) makes \(K^\bullet\) and \(K_\bullet\) agree for both \(X\) and \(X_K\). Arbitrary field extension need not preserve regularity. | Source statement retained verbatim in substance; caveat recorded here and in the source/formula ledgers. | Source-sic mathematical caveat; Claude/editorial review required. |
| 610 | 597 | 600 | Source/workpass repeat \(X_{S_1}/S_1\) after introducing \(S_2\), and carry inconsistent bases/primes for the \(Z_i\) Picard term. | Typed as \(X_{S_2}/S_2\), with \(Z_i\) over \(S'\) and \(\operatorname{Pic}_{Z/S'}\). | Source-carried local indices; Claude review required. |
| 613--615 | 600--602 | 603--605 | Stray prime on \(X_i\), omitted coproduct target, and \(\alpha^*L\) where the cocycle requires \(\beta^*L\). | Corrected from the scan/context; every repair is in the formula and correction ledgers. | Local source/workpass corrections pending incorporation. |
| 616 | 603 | 606 | II-star has \(f_*\mathcal O_Y\) instead of \(f_*\mathcal O_X\); terminal factorization subscript looks like \(\eta\) although the sequence ends at \(n\). | Uses \(f_*\mathcal O_X\) and provisionally \(f_n:Y_n=Y\). | First is a clear scan correction; terminal subscript needs editorial decision. |
| 617 | 604 | 607 | Lemma 2.6 uses undefined \(A_i\) in the recursive equalizer argument. | Uses the defined \(B_i\): tensor over \(B_i\), \(\operatorname{Spec}(B_i)\), and \(A=B_i\). | Mathematically forced repair; pending French-source control. |
| 619 | 606 | 609 | Nilradical and lift formula are ill-typed: the element lies in \(\mathcal O_{X'}\), while printed \(h\) is already its image under \(v\). | Uses \(\operatorname{nilrad}\Gamma(X,\mathcal O_{X'})\), defines \(h=\sum h_\beta\otimes t_\beta\), and then applies \(v\). | Mathematically forced typing repair. |
| 621--622 | 608--609 | 611--612 | The filtration \(I_i=N^iI\) is printed with reversed containment and hence reversed closed immersions and Picard arrows. | Uses \(NI_{i-1}\subset I_i\), \(X_{i-1}\to X_i\), \(\operatorname{Pic}_{X_i/S}\to\operatorname{Pic}_{X_{i-1}/S}\), and \(\operatorname{coker}(\operatorname{Pic}_Y^0\to\operatorname{Pic}_X^0)\). | Structural correction; Claude/editorial confirmation required. |
| 625 | 612 | 615 | Source/workpass call the descent data data on \(f^*L\), although \(L\) is on \(X\) and \(\mathrm{Rec}=\operatorname{Isom}(p_1^*L,p_2^*L)\). | Says “gluing data on \(L\).” | Clear typing correction pending source-control incorporation. |
| 626--627 | 613--614 | 616--617 | Workpass has \(\{\varnothing\}\) instead of scan \(\{\phi\}\), \(R^1\) instead of quantified \(R^i\), and source/workpass repeat \(R^n\) where \(R^i\) is quantified. | Follows scan for \(\{\phi\}\)/\(R^i\); uses \(R^i\) in the descending-induction family. | Direct transcription fix plus mathematically forced quantified-index correction. |
| 630--633 | 617--620 | 620--623 | Malformed diagram; impossible cross-references 2.3(i)--(ii); repeated \(\sigma_1\); lost prime on \(S'\); and \(F(1)\) where the proof requires \(F(-1)\). | Diagram reconstructed; references 1.3(i)--(ii), \(\sigma_i\), \(S'\), and \(F(-1)\) used. | Scan/context-supported corrections pending French workpass incorporation. |
| 638--639 | 625--626 | 628--629 | Undefined \(L'_K\) and \(c(L)\) instead of first Chern class. | Uses \(L_{1,K}\) and \(c_1(L)\). | Clear symbol repairs. |
| 640 | 627 | 630 | Text refers to Lemma 2.6, but no Lemma 2.6 is printed in this section. | Reference retained source-faithfully and explicitly flagged; no lemma invented. | Source-sic numbering ambiguity. |
| 641 | 628 | 631 | Lemma 2.8 prints \(+\beta(\beta+1)\), while the displayed calculation appears to imply a minus sign. | Printed plus sign retained. | Mathematical sign review required; no silent emendation. |
| 642 | 629 | 632 | Lemma 2.9 stabilizes \(h^1(L(-n))\), then invokes \(h^1(L(n))=0\) for large \(n\). | Printed signs retained and caveated. | Source-sic logical sign issue; Claude/editorial review required. |
| 644--646 | 631--633 | 634--636 | `supp` where a supremum is required, lost prime on \(L'_\alpha\), and “family \(\Lambda\)” where \(\Lambda\) is a subset. | Uses \(\sup\), restores \(L'_\alpha\), and says subset. | Local mathematical/terminological repairs pending source control. |

The first two items are direct witness-supported transcription corrections.
The third is deliberately **not** presented as a correction to the French
authority: it is a provisional English editorial emendation, recorded in
SOURCE_CORRECTION_LEDGER.csv. If the French lane chooses a source-sic
policy instead, revise that sentence, rebuild the PDF, and regenerate the
hash and visual-QA evidence before publication.

The fifth item follows the conservative policy already used for analogous
regularity caveats at idx597: the printed assertion remains in the English,
but the limitation is explicit in the apparatus rather than silently
rewritten.

## Claude handoff

Durable source-control notes are stored beside, but do not modify, the French
workpass:

- `HI_CLAUDE_CODEX_SGA6_NOTES_IDX598_607_20260718.md`;
- `HI_CLAUDE_CODEX_SGA6_NOTES_IDX608_615_20260718.md`;
- `HI_CLAUDE_CODEX_SGA6_NOTES_IDX616_624_20260718.md`;
- `HI_CLAUDE_CODEX_SGA6_NOTES_IDX625_635_20260718.md`;
- `HI_CLAUDE_CODEX_SGA6_NOTES_IDX636_646_20260718.md`.

They live in
`C:\IL_GitHub\00_main_current\sources\sga\sga6-claude-workpass-source-rescribe-20260704\`.
The earlier idx589--597 note remains there as well. These are coordination
artifacts, not publication payloads, and `sga6_fr_workpass.tex` is untouched.

## Publication rule

This cumulative package is the current source-checked English checkpoint
through idx646. Claude's newer committed French successor extends the direct
source-rescribe to idx662 but does not yet incorporate all untracked notes in
this ledger. The English checkpoint ends inside Definition XIII.3.3 and is
not a whole-volume release. Its publication manifest remains
`DO_NOT_UPLOAD`. Claude/source-control review of the provisional emendations
must either be resolved or explicitly disclosed before a complete SGA6
release is marked publication-ready.

<!-- END PRESERVED TRANCHE NOTE -->

---

## Preserved source note: idx647--665 tranche

Source file: `C:\Users\Floris\Documents\interlanguage\tmp\sga6_idx647_665_agent_20260718\HI_CLAUDE_CODEX_SGA6_NOTES_IDX647_665_20260718.md`

<!-- BEGIN PRESERVED TRANCHE NOTE -->

# Hi Claude — this is Codex; here are the SGA 6 items worth checking

I translated and scan-checked current-rescribe idx647–665. The committed French workpass at 8ccdcf8ee is certified through idx662; idx663–665 is retained as a clearly labeled post-checkpoint draft. I did not edit the French file.

Please inspect these exact points:

1. **idx651 / printed 638 / source-PDF 641, Lemma 3.9.** The sentence defines \(S_\alpha\), then calls the descended map an \(S'_\alpha\)-morphism. No \(S'_\alpha\) has been defined. Proposed repair: \(S_\alpha\)-morphism.
2. **idx651 / printed 638 / source-PDF 641, Remark 3.10.** Commit 8ccdcf8ee spells the name “Abhyankhar,” while the scan and the former snapshot read “Abhyankar.” Proposed repair: restore “Abhyankar.”
3. **idx652 / printed 639 / source-PDF 642, end of the first proof in Theorem 3.8.** The text says \(\mathscr L\) is bounded, but that was already assumed. The proof needs \((f^*)^{-1}(\mathscr L)\) bounded. Proposed repair: name the inverse-image family.
4. **idx656 / printed 643 / source-PDF 646, definition 4.1.** The sentence quantifies an algebraically closed field \(K\), a \(K\)-point \(t\), and two \(K\)-points of \(Z\), but calls \(Z\) a connected \(k\)-scheme. Proposed repair: connected \(K\)-scheme.
5. **idx657 / printed 644 / source-PDF 647, proof of Lemma 4.2.** The workpass has \(\Phi(G'^\tau)\supset G^\tau\), which is ill-typed. The scan reads \(\Phi^{-1}(G'^\tau)\supset G^\tau\). Proposed repair: restore the inverse image.
6. **idx660 / printed 647 / source-PDF 650, proof of Theorem 4.6.** The text introduces distinct \(p,q\) but then compares \(L^{\otimes r}\) and \(L^{\otimes q}\), while the next line concludes with \(L^{\otimes(p-q)}\). Proposed repair: \(L^{\otimes p}\).

Notation note: the typewritten source's superscript \(T\) in the equivalence notation is normalized to \(\tau\), consistently with the definition and the current workpass.

The English fragment marks every one of these choices inline as pending Claude/source correction, so none is silent.

<!-- END PRESERVED TRANCHE NOTE -->

---

## Preserved source note: idx666--684 tranche

Source file: `C:\Users\Floris\Documents\interlanguage\tmp\sga6_idx666_684_agent_20260718\PENDING_CLAUDE_SOURCE_FIXES_IDX666_684.md`

<!-- BEGIN PRESERVED TRANCHE NOTE -->

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

<!-- END PRESERVED TRANCHE NOTE -->

---

## Preserved source note: idx685--702 plus unindexed back matter

Source file: `C:\Users\Floris\Documents\interlanguage\tmp\sga6_idx685_702_agent_20260718\PENDING_CLAUDE_SOURCE_FIXES.md`

<!-- BEGIN PRESERVED TRANCHE NOTE -->

# Hi Claude — source issues noticed by Codex in the SGA 6 tail

This is the durable handoff Floris requested. I did **not** edit the French workpass. The French commit `8ccdcf8ee` is certified only through idx662; all observations below are therefore post-checkpoint and require your source-certification pass.

## Definite scan/workpass discrepancies

1. **idx686 / printed 673 / sourcePDF676** — after `c_i(E)`, the scan says that `E` is a vector bundle on `X`, or more generally an arbitrary element of `K^\bullet(X)`. The workpass omits this explanatory parenthesis. Restore it in the certified French rescribe.

2. **idx694 / printed 681 / sourcePDF684** — the workpass says that the image is contained in `H^2`. Both scans show `H^{2\bullet}`. This is a dropped bullet, not a mathematical editorial choice.

3. **idx695 / printed 682 / sourcePDF685** — the workpass has `\mu_2^{\otimes 3}`. Low- and high-resolution scans show `\mu_\ell^{\otimes 3}` (ell). The surrounding text fixes `\ell` as the cohomological prime. The English draft uses `\mu_\ell^{\otimes3}`.

4. **idx700 / printed 687 / sourcePDF690, bibliography [3]** — the workpass expands Bott--Samelson with a title/page range not printed in the scan. The scan contains only the authors, `Amer. Journ. of Math.`, vol. 80, p. 1004 (1958). Decide whether external bibliographic enrichment belongs in a separate editorial apparatus; it should not be presented as a scan transcription.

5. **unindexed sourcePDF698--702 / printed 696--700, notation index** — the workpass flattens several visible typographic distinctions. Please verify and restore:

   - subscripts in the `D(A_S)` family;
   - the paired ordinary/underlined `parf`, `f-parf`, and `Y-parf` forms;
   - underlined `S` in the third `D(S,A)`-type entry;
   - `E|` (not `F|`);
   - `f_{gr}` (not bare `gr`);
   - `\widehat G_a` and `\widehat G_g`;
   - underlined `\operatorname{Pic}^{\circ}_{X/k}`;
   - `r^0_{\mathcal O_{U\times V}}` (not `X\times V`);
   - `1+\widehat B^+`;
   - terminal `Z(x)` (ordinary `Z`, not `\mathbb Z`).

## Source anomalies to retain or resolve editorially

- **idx701 / bibliography [16]**: the scan itself prints `(SGA 6)` in the Deligne entry. That is historically surprising, but I retained the source text rather than silently changing it.
- **idx701 / bibliography [17]**: the author is printed `U. Mausin`. I retained that spelling pending an explicit editorial decision.
- **volume pagination**: printed page690 is absent from the 702-page scan. The terminological index begins on printed691/sourcePDF693. Please keep this absence explicit rather than forcing a false one-to-one page sequence.

## Coverage/terminal warning

idx702 is only the end of Exposé XIV. Ten additional, unindexed scan pages remain: the terminological index (sourcePDF693--697) and index of notations (sourcePDF698--702). The final physical/semantic leaf is sourcePDF702/printed700 and ends at `Z(x)`.

The English evidence, comparison ledger, and exact page map are in this same directory. The proposed readings are source-checked but remain `PENDING_CLAUDE` until the French lane certifies them.

<!-- END PRESERVED TRANCHE NOTE -->


