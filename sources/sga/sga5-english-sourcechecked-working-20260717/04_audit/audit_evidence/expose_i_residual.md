# SGA 5 English synchronization — Exposé I residual audit

Audit frozen 2026-07-17. A contemporaneous whole-workpass state had SHA-256
`006043F10F5897B1A4814616DF1F0DC51B1531292C9C0BE889577DD47C02BACB`
(15,193 lines); later-exposé edits continued after that read. The controlling stable
Exposé-I slice is therefore pinned independently: lines 1--2108,
ending immediately before the Exposé III title at line 2109, have SHA-256
`C70E01880114015ADA72EC076E8FD6DA6471E01BF6D6430E8B25C057C4C055AB`
after LF normalization and UTF-8 encoding without BOM. Every anchor below was re-read
after the final Exposé-I change observed during this audit.

Authorities:

- English workpass: `SGA5_English_sync_workpass.tex`.
- Current source-checked French authority: `sga5_fr_workpass.tex`, SHA-256
  `791F4EFFC5E02832D5D77ED03518C8156D6F07E4C8238B03545DB93D883FBB28`.
- Original LNM 589 scan: `C:\Users\Floris\Documents\Papors\OS\SGA5 (1).pdf`,
  SHA-256 `B256EBD072A8C68209518412A263C9289C6F1854A346733D86F885930D5FE6CA`.
  Printed page = PDF page minus 12.
- `FINDINGS.md`, local and authoritative `CERT_LOG.md`, scan-derived patch JSON,
  and `SOURCE_FORMULA_COMPARISON_EXACT.csv`, SHA-256
  `EB566F2D37B52214FADE9D045EA20A8B9ECAB0C5DED524CD322601A6F9FFB9A4`.
- English SGA 1–4 examples were located on disk, notably
  `03_projects/language_management/english_germanic/01_recovered_witnesses/sga1_4_english_baselines/`
  and the current SGA 4 cumulative under
  `Papors/modern-latex-manuscripts-github/sources/sga/00 SGA - Current Sources and SGA 5 High-Fidelity Edition/`.

## Verdict

Exposé I is **not yet current**. The exact-match propagation has landed correctly, but
42 residual patch groups remain. They include two dropped/source-flattened diagrams,
three wrong Tate-twist signs not covered by the exact matcher, a wrong functor name,
the page-34 `A_{Y_p}` object, the page-40 `i` correction, the page-52 uppercase `X`,
and a systematic but locally source-controlled set of missing underlines.

After the patches in the table below, the English will be synchronized to the current
French authority at every audited Exposé-I correction site, including the Illusie
appendix through printed page 72. Publication certification will still require the
editorial decisions recorded later in this file; those are documented source
errata/normalizations, not unlocated synchronization debt.

## Exact residual patch table

`FR` means the current French authority; `scan` means the original LNM 589 printed
page; `CERT` means the source-certification log. Line numbers refer to the frozen
English hash above.

| ID | Source page | Current English line / exact old string | Exact new string | Authority | Classification |
|---|---:|---|---|---|---|
| I-R001 | 3 | L343: `the section of $\Ext^1(F,A_X)$` | `the section of $\underline{\Ext}^1(F,A_X)$` | FR L346; scan p3 | sheaf-operator underline |
| I-R002 | 8 | L429: `\subsection*{Remark 1.8}` | `\subsection*{Remarks 1.8}` | FR L432; scan p8 | source heading/prose |
| I-R003 | 9 | L450: `for $i>N$`; `the commutation of tensor product with filtered inductive limits` | `for $i\geqslant N$`; `the commutation of $\otimes^{\mathrm L}$ with filtered inductive limits` | FR L455; scan p9 | inequality + derived operator |
| I-R004 | 10 | L455: `$G\in\ob\D_c^-(Y)$` | `$G\in\ob\D_c(Y)$` | FR L460; scan p10 | boundedness error |
| I-R005 | 12 | L540: `\underline D_Y\R f_!(F)` | `\underline D_Y\R_!f(F)` | FR L517; scan p12 | source formula notation |
| I-R006 | 13 | L544: `\R f_!\underline D_X(F)` | `\R_!f\,\underline D_X(F)` | FR L521; scan p13 | source formula notation |
| I-R007 | 13 | L561: `$\R f_!(\underline D_X(F))\in\ob\D_c(Y)$` | `$\R_!f(\underline D_X(F))\in\ob\D_c(Y)$` | FR L536; scan p13 | source formula notation |
| I-R008 | 13 | L569: `the usual and unusual direct images, $\R f_*$ and $\R f_!$` | `the usual and unusual direct images, $\R f_*$ and $\R_!f$` | FR L543; scan p13 | source notation consistency |
| I-R009 | 14 | L583: `this proves the first assertion.` | `this will prove the first assertion.` | FR L555; scan p14 (`démontre(ra)`) | source prose fidelity |
| I-R010 | 18 | L744: both `\Hh^i(P_{\ol{x}})` and `\Hh^i(P'_{\ol{x}})` | respectively `\uH^i(P_{\ol{x}})` and `\uH^i(P'_{\ol{x}})` | FR L643; scan p18 | local source underline |
| I-R011 | 19 | L748, L752, L754, L777: `\Hh^i(P)`, `\Hh^i(P')`, `\Hh^{-r_0}(P)`, `\Hh^{r_0}(P')`, `\Hh^m(P')` | replace each listed `\Hh` by `\uH`, leaving all arguments and exponents unchanged | FR L643/L655; scan p19 | local source underline |
| I-R012 | 20 | L797, L799, L801: `\Hh^0(P)`, `\Hh^{-a}(P)`, and `P\to\Hh^0(P)`; L814: `already the degree-zero cohomology sheaves are not isomorphic` | replace each listed `\Hh` by `\uH`; at L814 use `already the sheaves $\uH^0$ are not isomorphic` | FR L665/L675; scan p20 | local source underline |
| I-R013 | 23 | L858: `f\in\Gamma\bigl(\wt Y(\ol y),\cO_{\wt Y,\ol y}\bigr),` | `f\in\Gamma\bigl(\wt Y(\ol y),\cO_{Y,\ol y}\bigr),` | FR L717; scan p23 top/c1 | wrong structure-sheaf subscript |
| I-R014 | 24 | L889: `\Gamma^*(X,\cO_X)` | `\Gamma(X,\cO_X)` | FR L741; scan p24 | spurious superscript |
| I-R015 | 26 | L942: `(\mu_n)^{\otimes d}_Y[-2d]` | `(\mu_n)^{\otimes -d}_Y[-2d]` | FR L778; scan p26 | substantive Tate-twist sign |
| I-R016 | 26 | L944: `Put $T=(\mu_n)^{\otimes d}_Y$.` | `Put $T=(\mu_n)^{\otimes -d}_Y$.` | FR L780; scan p26 | propagated-definition sign |
| I-R017 | 26 | L970: `\dim\cO_{Z,\ol x}`; L974: `\codim_{\ol x}(Z,X)` and `\dim\cO_{X,\ol x}`; L978–979: the same geometric-point subscripts | use `\dim\cO_{Z,x}`, `\codim_x(Z,X)`, and `\dim\cO_{X,x}` respectively; retain the geometric point in the earlier strict-localization and stalk formulas | FR L784; scan p26 | point/geometric-point source correction |
| I-R018 | 30 | After L1104, the sentence says a distinguished triangle exists but the triangle is absent | insert exact block D002 below | FR L862–868; scan p30 | dropped diagram/content |
| I-R019 | 31 | L1124–1128 linearize `\R i_*F\to\R i_*\R j_*j^*F\to\R i_*M\xrightarrow{[1]}` | replace with exact block D003 below | FR L876–883; scan p31 | source diagram topology/layout |
| I-R020 | 34 | L1208: `reduced to biduality for this pair on $Y_p$` (antecedent is `(A'_{Y_p\cap Y'},A_X)`) | `reduced to biduality for $(A'_{Y_p\cap Y'},A_{Y_p})$ on $Y_p$` | FR L931; scan p34 | wrong ambient dualizing sheaf |
| I-R021 | 37 | L1280: `(SGA~VIII~4.2)` | `(SGAA~VIII~4.2)` | FR L990; scan p37 | citation anchor |
| I-R022 | 37 | L1288: `$\overset{\mathbf L}{\otimes} i_?$ extends` | `$\mathbf L\, i_?$ extends` | FR L998; scan p37 | missed fifth functor-name correction |
| I-R023 | 40 | L1375: `put $K_Y=\R^{!}j(K_X)$` | `put $K_Y=\R^{!}i(K_X)$` | FR L1085; scan p40 confirms printed `j` is the source typo | mathematically necessary source emendation |
| I-R024 | 41 | L1401: `(4.5.3)''\qquad \H^i(\underline{D}_X(F))_{\ol{x}}\times \H_{\ol{x}}^{-i}(F)\longrightarrow A,` | `(4.5.3)''\qquad \uH^i(\underline{D}_X(F)_{\ol{x}})\times \uH_{\ol{x}}^{-i}(F)\longrightarrow A,` | FR L1111; scan p41 | stalk placement + local underlines |
| I-R025 | 41 | L1403: `where $\H_{\ol{x}}^i=\H^i\R\Gamma_{\ol{x}}$.` | `where $\uH_{\ol{x}}^i=\uH^i\R\Gamma_{\ol{x}}$.` | FR L1113; scan p41 | definition underline |
| I-R026 | 44 | L1470: `(4.6.1)''\qquad \H_Y^i(F)_{\ol{x}}\times \H_{\ol{x}}^{-i}(\underline{D}_X(F)|Y)\longrightarrow A.` | `(4.6.1)''\qquad \uH_Y^i(F)_{\ol{x}}\times \uH_{\ol{x}}^{-i}(\underline{D}_X(F)|Y)\longrightarrow A.` | FR L1180; scan p44 | local-cohomology underlines |
| I-R027 | 44 | L1476: `\H_Y^i(F)_{\ol{x}}\times \H_{\ol{x}}^{2d-i}(F'|Y)\longrightarrow A,` | `\uH_Y^i(F)_{\ol{x}}\times \uH_{\ol{x}}^{2d-i}(F'|Y)\longrightarrow A,` | FR L1186; scan p44 | local-cohomology underlines |
| I-R028 | 44 | L1484: `(SGA~VIII~4.2)` | `(SGAA~VIII~4.2)` | FR L1194; scan p44 | citation anchor |
| I-R029 | 45 | L1528: `But $K_V=j^*K_X$` | `But $K_V=j^!K_X$` | FR L1238; scan p45 | source-exact open-immersion notation; equivalent functors |
| I-R030 | 51 | L1668 `\H_x^i(A_X)`; L1670 the two local terms `\H_x^0(A_X)`, `\H_x^1(A_X)`; L1674 `\H_x^i(A_X)`; L1676 both local terms | replace only those local-cohomology occurrences by `\uH_x^i`, `\uH_x^0`, `\uH_x^1`; leave global `\H^0(X,-)` and `\H^0(U,-)` plain | FR L1389–1397; scan p51 | local-cohomology underlines |
| I-R031 | 52 | L1719: `\H^{1-i}(U,\Hom(M,A_U)) ... (\mu_n)_x^{\otimes -1}` | `\H^{1-i}(U,\uHom(M,A_U)) ... (\mu_n)_X^{\otimes -1}` | FR L1440; scan `p052_mu_zoom` | sheaf-Hom underline + uppercase scheme subscript |
| I-R032 | 53 | L1757: `\Hom(M,A)^P` and `\Hom(M^P,A)` | `\uHom(M,A)^P` and `\uHom(M^P,A)` | FR L1478; scan p53 | Hom underlines |
| I-R033 | 55 | L1785 and L1787: each `\H^i(E)` | each `\uH^i(E)` | FR L1506/L1508; scan p55 | appendix cohomology-object underlines |
| I-R034 | 61 | L1867: `(\mu_n^{\otimes d})_Y[-2d]` | `(\mu_n^{\otimes -d})_Y[-2d]` | FR L1588; scan p61 | substantive Tate-twist sign |
| I-R035 | 62 | L1893: `every $\H^i(F)$` | `every $\uH^i(F)$` | FR L1614; scan p62 | appendix cohomology-object underline |
| I-R036 | 62 | L1897: `the $\H^i(F)$ are locally constant` | `the $\uH^i(F)$ are locally constant` | FR L1618; scan p62 | appendix cohomology-object underline |
| I-R037 | 63 | L1905: `the $\H^i(F)$ are locally constant` | `the $\uH^i(F)$ are locally constant` | FR L1626; scan p63 | appendix cohomology-object underline |
| I-R038 | 64 | L1927: `(\mu_n^{\otimes d})_Y[-2d]` | `(\mu_n^{\otimes -d})_Y[-2d]` | FR L1648; scan p64 | substantive Tate-twist sign |
| I-R039 | 64 | L1931 and L1935: right-hand `\R\Hom(M_{\bar y},...)` | right-hand `\R\underline{\Hom}(M_{\bar y},...)` in both formulas | FR L1652/L1656; scan p64 | Hom underlines |
| I-R040 | 64 | L1937: `the $\H^i(F)$ are locally constant` | `the $\uH^i(F)$ are locally constant` | FR L1658; scan p64 | cohomology-object underline |
| I-R041 | 64 | L1939: `\Ext^i(M_{\bar y},F_{\bar y})=0` | `\underline{\Ext}^i(M_{\bar y},F_{\bar y})=0` | FR L1660; scan p64 | Ext underline |
| I-R042 | 66 | L1990: `\Ext^p(M',F_{\bar x})\ne0` | `\underline{\Ext}^p(M',F_{\bar x})\ne0` | FR L1711; scan p66 | Ext underline |

### D002 — exact insertion after English L1104 (source p30)

The words “gives a distinguished triangle” must be followed by:

```tex
\[
\begin{tikzcd}[column sep=large,row sep=large]
& \R\,\underline{\Hom}(A_{U,X},G) \arrow[dl] & \\
\R\,\underline{\Hom}(A_Y,G) \arrow[rr] & & \R\,\underline{\Hom}(A_X,G) \arrow[ul]
\end{tikzcd}
\]
```

The present “Since ...” sentence follows this display unchanged. Visual inspection of
`p030_full.png` confirms all three nodes and the cycle of arrows.

### D003 — exact replacement for English L1124–1128 (source p31)

```tex
Applying $\R i_*$ gives a distinguished triangle
\[
\begin{tikzcd}[column sep=large,row sep=large]
& \R i_*(M) \arrow[dl,"{(+1)}"'] & \\
\R i_*(F) \arrow[rr] & & \R i_*\R j_*j^*(F) \arrow[ul]
\end{tikzcd}
\]
```

The existing linear display is mathematically equivalent, but the current authority and
scan preserve this topology and the explicit `(+1)` label. Visual inspection of
`p031_top.png`, `p031_mid.png`, and `p031_bot.png` confirms it.

## Required classification of `already-propagated-or-not-bilingual-exact`

There are 12 Exposé-I rows with this disposition. Against the live hash, all 12 have a
verified English analogue and are already current. None now requires a nonexact English
patch, and none must be dismissed as source-language-only.

| Candidate | Page | Verified English anchor | Classification | Exact English replacement |
|---|---:|---|---|---|
| SGA5-EXACT-0001 | 33 | L1196 `(\mu_n)^{\otimes -1}_Y[-2]` | confirmed already current | none |
| SGA5-EXACT-0006 | 38 | L1309 `SGAA~VI~I~3.7` | confirmed already current | none |
| SGA5-EXACT-0007 | 38 | L1317 `SGAA~IX~2.7` | confirmed already current | none |
| SGA5-EXACT-0008 | 38 | L1324 `SGAA~XVIII~3.1.10` | confirmed already current | none |
| SGA5-EXACT-0009 | 38 | L1334 `SGAA~XVII` | confirmed already current | none |
| SGA5-EXACT-0010 | 39 | L1338 `SGAA~VII~5.11` | confirmed already current | none |
| SGA5-EXACT-0011 | 39 | L1346 `SGAA~IX~2.7.4` | confirmed already current | none |
| SGA5-EXACT-0012 | 40 | L1369 `SGAA~VII~5.11` | confirmed already current | none |
| SGA5-EXACT-0013 | 40 | L1373 `SGAA~V~4.3` | confirmed already current | none |
| SGA5-EXACT-0017 | 47 | L1572 `SGAA~3.1.10` | confirmed already current | none |
| SGA5-EXACT-0025 | 65 | L1952 `since otherwise $\R i_*(G)=0$` | confirmed already current | none |
| SGA5-EXACT-0026 | 66 | L1994 `(I 3.3.1)` | confirmed already current | none |

The stale candidate SGA5-EXACT-0014 must **not** be applied: its disposition is
`rejected-not-in-final-french-authority`. The actual final-authority repair is I-R024,
which includes both the stalk placement and the underlines.

## Confirmed-current correction groups (do not redo)

The following have already landed correctly in the English workpass:

- p2 asymmetric local-duality pairing; p4 `I^i`; p10 Lemma 1.9(a) unbounded `F`;
  p12 `Remarks 1.11.1` and the star-to-shriek correction.
- p17 all three `L[r]` repairs; p26 `\widetilde Z\times_XY`.
- p33 purity twist; p36 `(μ_n)_X`; four of the five p37 `\mathbf L\,i_?` repairs.
- p38–40 exact SGAA citation rows; p41 `(4.5.3)'` and the non-circular biduality step;
  p42 underlined functor; p43 closure notation.
- p47 SGAA citation; p48 removed spurious support subscript; p49 underlined `G^\circ`;
  p50 and p52 exact citations; p51 spectral-sequence abutment; p54 `[SGAA]`.
- Appendix p55 module-category/subscript repairs; p56 proposition prose; p60 residual
  characteristics of `Y`; p61 unbounded category; p62 exact `(4.3)` twist; p65 stalk-zero
  and `\bar f`; p65 exact Ext rows; p66 cross-reference; all p68 exact Hom/Ext rows.
- Source pp69–71: the two appendix diagrams and their surrounding formulas are present and
  source-topology complete.

## Appendix/source-page boundary, pp66–74

- p66 has one residual (I-R042); the `I 3.3.1` cross-reference is already current.
- p67 is current at the audited correction sites.
- p68 has all three exact Hom/Ext repairs already current.
- pp69–71 diagrams and connective prose are present.
- p72 is textually current against the French authority; the `R^!g` versus `Rg^!`
  normalization is an editorial-policy item below.
- Printed pp73–74 begin Exposé III. They are not part of Exposé I and must not be used to
  inflate Exposé-I coverage.

## Source errors and editorial/rejected choices

These are not hidden synchronization debt. They must be preserved in a durable editorial
ledger so the final edition does not silently reproduce or silently repair the scan.

| Page | Issue | English disposition / proposed editorial action |
|---:|---|---|
| 14 | Cor. 1.13 prints the wrong intermediate `R f_*` and cites (a)(i) twice. | The current English faithfully repeats it at L579–581. For mathematical correctness, an editorial emendation should use `\underline D_Y\R_!f\,\underline D_XF` on the second line and cite `(a)(ii)` on the third, with a footnote recording the scan. Do not make this silently. |
| 15 | Source has meaningless `f_*F\in D_c(F)`. | English correctly has `D_c(Y)`; keep and log emendation. |
| 16 | Cor. 1.15 source cites 1.5, but the relevant result is 1.6. | English L627 correctly says Proposition 1.6; do not regress to current-French source literalism. |
| 16 | Theorem 2.1 source cites 1.6 for the definition of dualizing complex. | English correctly names Definition 1.7. |
| 18 | Source has `H^{-i(x)}` where the index must be `r(x)`. | English is mathematically correct; keep. |
| 30 | Source conclusion says `D_c^+(X)` although the object lives on `Y`. | English L1098/L1114 correctly uses `Y`; keep and footnote if desired. |
| 34 | Source has `A_X` instead of `A_{X'}` and repeats `(ii),(ii)`. | English already has the mathematically correct `A_{X'}` and `(ii),(iii)`; keep. |
| 40 | Source prints `K_Y=R^!j(K_X)` although the closed immersion is `i`. | Current French emends to `i`; I-R023 must propagate that emendation. |
| 41 | Source reuses label `(4.5.3)`. | English/French use `(4.5.3)^{\mathrm{bis}}`; keep the disambiguation. |
| 43 | The D-subscript in the ordinary-induction step is unresolved even in the high-resolution crop. | Preserve the current authority reading and retain an explicit ambiguity note; do not guess. |
| 44 | Source says a closed `Y` contains `X`, where it must contain the point `x`. | English is correct; keep and log. |
| 45 | Source locally writes `j^!`, while the setup writes `j^*`; for an open immersion they agree. | I-R029 follows the current French/scan locally. Retain a note that the mixed notation is intentional, not an algebraic change. |
| 47 | Source writes `R\Gamma_V(i_!G')`, while the edition uses `R\Gamma(V,i_!G')`. | Same object; keep the English normalized space-argument notation. |
| 52 | Older ledger prose called the subscript lowercase `x`; the 600-dpi crop clearly shows uppercase `X`. | Follow the scan/current French: I-R031. |
| 72 | Scan places shriek before `g` (`R^!g`); current French and English normalize to `Rg^!`. | Keep current form pending a document-wide exceptional-inverse-image notation policy; record as a rejected literal choice. |

## Completion statement

Applying I-R001 through I-R042 will make Exposé I current against the source-checked
French authority and the audited scan evidence. It will **not by itself** make the whole
SGA 5 cumulative current: nine other published exposés remain outside this audit. For
Exposé I publication readiness specifically, the p43 ambiguity and the p14/p72 editorial
choices must remain visibly logged even after every patch is applied.
