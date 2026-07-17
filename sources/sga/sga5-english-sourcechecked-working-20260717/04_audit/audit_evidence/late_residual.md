# SGA 5 late residual audit — Exposés X, XII, XV, and Index

Audit date: 2026-07-17 (Europe/Berlin)

Scope: source-critical, read-only audit of the active English cumulative against the scan-backed final French authority. This audit made no production-TeX edits.

## Moving-workpass reconciliation and exact continuation cursor

The production workpass is being patched concurrently. The semantic anchors and replacement blocks in this report are authoritative; line numbers are only a convenience for the following frozen reconciliation snapshot:

- English SHA-256: `DA857F8ECC69E6C43397C131CB43632618834396ECF5BBE4E3C37ED2B19F9028`
- English size / timestamp: `786891` bytes; `2026-07-17 21:22:33 +02:00`
- Reconciliation result: **not synchronized**.

The following items were confirmed present in that snapshot and must not be reapplied: the X p. 375 transition, p. 392 corrections, pp. 394–395 corrections, pp. 399–400 self-duality/`hom` derivation, and `[T] chap. V`; XII p. 410, the `NW_f` name, formula (5.2), and the p. 435 `v` correction; XV's p. 444 diagram, the p. 454–458 exact-row/FIX corrections, both scan-corrected `embedding` readings, bare `F`, bare `K'`, and the two indexed tuples on p. 478.

The following semantic anchors remain actionable in that snapshot. Each row points to a complete old→new replacement below; do not infer completion from a larger surrounding block or from successful compilation.

| Exposé | Frozen line(s) | Current old anchor | Required replacement in this report |
|---|---:|---|---|
| X | 12849 | `j:V\to X` in the extension-by-zero notation | X item 6: `j:V\hookrightarrow X` |
| X | 13069–13107 | sheaf-level `R\Gamma^G`, `\Gamma^G`, and prose without underlines | X item 5: all five exact formula blocks and the §7(c) terminal chain; retain global `R\Gamma^G` un-underlined |
| XII | 13712–13778 | `If the vector space ...` through `Therefore $c\mid(r-1)$` | XII item 3: replace the whole interval with the complete proof block. The current expanded text is still incomplete and contains a false three-link zero calculation |
| XII | 13929 | multiplicity-one subheading with `g^{-1}_{X'}` and `Y'\cap{X'_x}^{g^{-1}f'}` | XII item 6: replace the full subheading |
| XII | 14121 | `Let $x'=X_x'{}^{f'}$` | XII item 7: `Let $x'\in X_x'{}^{f'}$` |
| XII | 14278 onward | `F_\eta \arrow[r,"u_\eta"]` and unbarred adjoining module notation | XII item 8: replace the whole `H`-module block, preserving the deliberately unbarred final constructibility reference |
| XV | 14601–14603 | quotient by `\JJ^{(p)}` and use of the same symbol for its image | XV additional item 1: restore the `\JJ'` / `\JJ^{(p)}` distinction |
| XV | 14858–14884 | Proposition 3's swapped identity factors and `F=X` | XV additional item 2: replace the proposition display and use `F=\Lambda_X` |
| XV | 14898 onward | compact five-node Corollary diagram | XV item 4: replace with the seven-node/eight-edge scan-backed block |
| XV | 14921 onward | geometric-Frobenius paragraph beginning `X'=e=...` | XV additional item 3: replace the complete paragraph with the barred `\bar e`, `\overline{\fr}_X`, and `\overline{\Fr}` block |
| XV | 15200 onward | p. 471 paragraph without the coefficient-field footnote and with `\Fr^*_{\bar F/X}:\fr_X^*(F)` | XV additional item 4: replace the complete paragraph and both downstream occurrences |

The 45-row tables below record the **initial audit baseline**. Where the reconciliation above says that a row is already present, that newer status supersedes the baseline classification. The tables remain here as an exact receipt and provenance record, not as a command to reapply patches.

## Snapshot and gate result

- English workpass: `SGA5_English_sync_workpass.tex`
  - SHA-256 at initial late-audit snapshot: `DC71926BA141B0E5BC1EA996EED3C2B3D512805044F5EA68B171252115DCCB71`
- French authority: `sga5_fr_workpass.tex`
  - SHA-256: `791F4EFFC5E02832D5D77ED03518C8156D6F07E4C8238B03545DB93D883FBB28`
- Exact-candidate receipt: `SOURCE_FORMULA_COMPARISON_EXACT.csv`
  - SHA-256: `EB566F2D37B52214FADE9D045EA20A8B9ECAB0C5DED524CD322601A6F9FFB9A4`

**Gate result: not synchronized.** The large inherited omissions previously found in X §§3.6–3.9 and XII §4.9, Proposition 5.1, and §§6.2–6.3 are now restored in the shared workpass and must not be reintroduced as debt. Genuine residuals remain in X, XII, and XV. XV also lacks an entire scan-confirmed relative-Frobenius diagram.

Current structural comparison:

| Exposé | Tags EN/FR | Statements EN/FR | TikZ blocks EN/FR | Result |
|---|---:|---:|---:|---|
| X | 38/38 | 13/13 | 7/7 | coarse parity; residual prose/formula corrections below |
| XII | 53/53 | 3/3 | 4/4 | coarse parity; bounded residual corrections below |
| XV | 5/5 | 23/23 | **4/5** | one complete source diagram omitted; one retained diagram is not edge-equivalent |

The 45 late receipt rows with disposition `already-propagated-or-not-bilingual-exact` now classify as:

- `needs nonexact English patch`: 14
- `source-language-only`: 16
- `current`: 15

There are no XII rows in this receipt-disposition class; XII debt was found by direct source/formula comparison.

## Exact-row classification: Exposé X

| Candidate | p. | Classification | Current English evidence / required action |
|---|---:|---|---|
| SGA5-EXACT-0059 | 376 | current | EN 12182 has `full subcategory $\mathcal E$`. |
| SGA5-EXACT-0060 | 376 | current | EN 12194 has `$M\in\Ob(\mathcal E)$`. |
| SGA5-EXACT-0062 | 376 | current | EN 12198 has `$R^{\bullet}_{\Lambda}(G)$`. |
| SGA5-EXACT-0065 | 378 | current | EN 12240–12243 consistently uses `t` and `g`. |
| SGA5-EXACT-0066 | 378 | current | EN 12247–12249 restores the source `A`/`B` variables and `${}_{A-B}Y^\bullet`. |
| SGA5-EXACT-0067 | 379 | current | EN 12262 has unsubscripted `\RHom` and `D(C)_\Delta`. |
| SGA5-EXACT-0069 | 383 | current | EN 12377/12385 has `$A\widehat\otimes A$`. |
| SGA5-EXACT-0070 | 384 | current | EN 12411 has `(Lemma 5.1)`, the printed/source-faithful reading. |
| SGA5-EXACT-0073 | 386 | current | EN 12473 has `the point $y'$ and $C'$ above $y$`. |
| SGA5-EXACT-0074 | 386 | current | EN 12473 has the asymmetric source reading `$(C,y',G)$`. |
| SGA5-EXACT-0075 | 388 | current | EN 12545 has `$Sw_{y'}$, $Sw'_{y'}$, $Art_{y'}$`. |
| SGA5-EXACT-0076 | 388 | current | EN 12545 has `$Sw_{y'}=0$`. |
| SGA5-EXACT-0304 | 372 | needs nonexact English patch | EN 12091 has `([T], chap. V)`. Remove the comma after `[T]`: the final French and scan read `([T] chap. V)`. Retain idiomatic English `or simply a ...`. |
| SGA5-EXACT-0305 | 372 | current | EN 12085 now uses parentheses around the viewpoint clause. |
| SGA5-EXACT-0306 | 372 | current | EN 12087 now has no comma after `loc. cit.`. |

The original p. 386 scan crop `p386_top.png` visibly reads both `point y' et C'` and the asymmetric pair `(C',y'',G)` / `(C,y',G)`. These are not OCR guesses.

## Exact-row classification: Exposé XV

| Candidate | p. | Classification | Current English evidence / required action |
|---|---:|---|---|
| SGA5-EXACT-0078 | 454 | needs nonexact English patch | EN 14401: `$\widehat X_{\et}$` -> `$\widetilde X_{\et}$`. |
| SGA5-EXACT-0079 | 454 | needs nonexact English patch | EN 14406: `$F\in\Ob\widehat X_{\et}$` -> `$F\in\Ob\widetilde X_{\et}$`. |
| SGA5-EXACT-0081 | 454 | needs nonexact English patch | EN 14411: `$\Fr^*$` -> `$\Fr^*_{/}$`. |
| SGA5-EXACT-0082 | 455 | needs nonexact English patch | EN 14429: `$F(\Fr_{/X'})^{-1}$` -> `$F'(\Fr_{/X'})^{-1}$`. |
| SGA5-EXACT-0084 | 455 | needs nonexact English patch | EN 14441: `$F\to g_*g^*F$` -> `$F\xrightarrow{\alpha}g_*g^*F$`. |
| SGA5-EXACT-0085 | 456 | source-language-only | Full stop/comma versus French semicolon; no content loss. |
| SGA5-EXACT-0086 | 456 | source-language-only | Lowercase English `modules` is correct prose, not a coefficient-symbol change. |
| SGA5-EXACT-0087 | 456 | source-language-only | The English clause/new sentence retains Proposition 1a); punctuation only. |
| SGA5-EXACT-0088 | 456 | source-language-only | `in the usual sense` need not be parenthesized in English. |
| SGA5-EXACT-0089 | 456 | needs nonexact English patch | EN 14470 drops the printed trailing reference. Append ` (Proposition 1a), b)).` or an equivalently faithful English rendering. |
| SGA5-EXACT-0091 | 456 | source-language-only | The English copula and clause order retain both arrows and the full meaning. |
| SGA5-EXACT-0092 | 457 | needs nonexact English patch | EN 14487: `endomorphism of $\RGamma(X,F)$` -> `endomorphism of $\RGamma_X(F)$`. |
| SGA5-EXACT-0096 | 462 | needs nonexact English patch | EN 14674: `defined by an extension of` -> `defined by an embedding of`. |
| SGA5-EXACT-0097 | 462 | source-language-only | Comma-delimited apposition is equivalent to the French parenthetical. |
| SGA5-EXACT-0098 | 463 | source-language-only | Full stop versus French colon; no content loss. |
| SGA5-EXACT-0099 | 464 | source-language-only | Semicolon versus French comma; no formula or scope change. |
| SGA5-EXACT-0100 | 467 | source-language-only | English `Proposition 1a` has balanced punctuation; do not add a gratuitous second `)`. |
| SGA5-EXACT-0102 | 470 | source-language-only | Comma after `In the general case` is optional English punctuation. |
| SGA5-EXACT-0105 | 471 | needs nonexact English patch | EN 14902: `defined by an extension of` -> `defined by an embedding of`. |
| SGA5-EXACT-0107 | 472 | needs nonexact English patch | EN 14929: `with $F_\nu$ annihilated` -> `with $F$ annihilated`. Scan `p472_mid.png` unambiguously has bare `F`. |
| SGA5-EXACT-0108 | 473 | source-language-only | Comma-delimited `independent of $\nu$` is equivalent to the French parenthetical. |
| SGA5-EXACT-0109 | 475 | needs nonexact English patch | EN 15017: `endomorphism of $K'_\nu$` -> `endomorphism of $K'$`. Scan `p475_bot.png` unambiguously has bare `K'`. |
| SGA5-EXACT-0110 | 476 | source-language-only | English comma clause is equivalent to the French parenthetical. |
| SGA5-EXACT-0111 | 477 | source-language-only | `the nilpotent ideal` carries the same content as French `(nilpotent)`. |
| SGA5-EXACT-0112 | 478 | needs nonexact English patch | EN 15050: `$k_0=(k_0^i)$` -> `$k_0=(k_0^i)_i$`. |
| SGA5-EXACT-0113 | 478 | needs nonexact English patch | EN 15054: `$k=(k^i)$` -> `$k=(k^i)_i$`. |
| SGA5-EXACT-0114 | 478 | source-language-only | `after replacing ... if necessary` is faithful English; French parentheses are stylistic. |
| SGA5-EXACT-0116 | 480 | source-language-only | `by Lemma 3(ii)` is the natural English form of the parenthetical citation. |
| SGA5-EXACT-0117 | 480 | source-language-only | `being surjective with acyclic kernel` preserves the causal aside. |

## Exact-row classification: Index

| Candidate | p. | Classification | Evidence |
|---|---:|---|---|
| SGA5-EXACT-0118 | 481 | current | EN 15116 reads `\sgaindexentry{constructible $A$-sheaf}{VI 1.4.1, 1.4.3}`. |

The English and French indexes each contain 108 `\sgaindexentry` records. The eleven printed `XIV` references to Houzel's final exposé remain deliberately source-faithful even though the title page says Exposé XV.

## Additional residual debt outside those 45 rows

### Exposé X

1. **p. 375, dropped transition paragraph (French FIX #37).** After EN 12174 `\end{prooftext}` and before the §3 heading, insert:

   ```tex
   The Weil formula 6.1 will give an expression for the class
   $\operatorname{cl}_{K^\bullet(\Lambda[G])}(R\Gamma_X(\Lambda_{V,X}))$,
   when $X$ is a curve, in terms of known global invariants and local invariants
   that we shall define in no.~5.
   ```

2. **p. 392 (French FIX #38–#40).** At EN 12657–12681:

   - restore the aligned middle equality saying the trace is “the number of fixed points of the restriction $g_{Y'}$ of $g$ to $Y'$” before the sum;
   - `(SGA 4 IX 4)` -> `(SGA 4 IX 47)`;
   - `$H^*(C',\Lambda_{n,C'})$` -> `$H^1(C',\Lambda_{n,C'})$`.

3. **pp. 394–395 (French FIX #41–#43).** At EN 12714, 12718, 12734, 12738–12740, and 12750:

   - replace the affected `\Hom^\bullet_{A[G]}(Sw^A,...)` pairings with `\Hom^\bullet_{\Lambda[G]}(Sw^\Lambda,...)` (and likewise for `G'`);
   - replace `$F_{\bar\eta'}\simeq[F_{\bar\eta''}]_\varphi$` with `$F_{\bar\eta''}\simeq[F_{\bar\eta'}]_{(\varphi)}$`.

4. **pp. 399–400 (French FIX #45–#47 plus omitted derivation).**

   - EN 12858 and 12888: `\RHom_{A[G]}` -> `\RHom_{\Lambda[G]}`.
   - After the sentence introducing Weil formula (5.2), restore the source self-duality display
     `\clKstar{\Lambda[G]}(\RG_{C'}(\Lambda_{U',C'})) = \clKstar{\Lambda[G]}(\RG_{C'}(\Lambda_{U',C'})^\vee)`
     and the full `\operatorname{hom}` aligned calculation from FR 13049–13066. The current English compresses the entire derivation to its final equality and therefore is not a complete translation.

5. **§7(a)–(c), the sheaf-invariants functor has lost every underline.** The source distinguishes the global-sections invariants functor `\Gamma^G` from the sheaf functor `\underline{\Gamma}^G`. Apply the following exact formula blocks and use `\underline{\Gamma}^G` in all adjoining prose that says “subsheaf of $G$-invariant sections”:

   ```tex
   \[
   R\Gamma^G(\RG_C(\Psi))
   \simeq\RG_C(R\underline{\Gamma}^G(\Psi)),
   \tag{7.3}
   \]
   \[
   \Gamma^G\circ\Gamma_C
   =\Gamma_C\circ\underline{\Gamma}^G.
   \]
   \[
   \Phi\simeq R\underline{\Gamma}^G(p_*(\Phi')),
   \qquad \Phi'=p^*(\Phi).
   \tag{7.4}
   \]
   \[
   \Phi\simeq
   R\bigl((\underline{\Gamma}^G\circ p_*)\circ p^*\bigr)(\Phi).
   \]
   \[
   \Phi\simeq
   R(\underline{\Gamma}^G\circ p_*)(p^*(\Phi))
   \simeq(R\underline{\Gamma}^G)(p_*p^*(\Phi)).
   \]
   ```

   In §7(c), the proof chain must end with:

   ```tex
   \[
   (R\Gamma^G)(\RG_{C'}(\Phi'))
   \simeq(R\Gamma^G)(\RG_C(p_*(\Phi')))
   \simeq\RG_C(R\underline{\Gamma}^G(p_*(\Phi'))).
   \]
   ```

   Authority: FR 12943–12985. The global `R\Gamma^G` occurrences remain un-underlined; only the functor acting on sheaves takes the underline.

6. **p. 391 immersion arrow.** In the notation introducing extension by zero, use `j:V\hookrightarrow X`, not the inherited `j:V\to X`.

7. **Current/no patch.** X §§3.6–3.9, including tags (3.6.3), (3.7.1), and (3.7.2), are restored. French FIX #44 at p. 397 is current (`C'`). Formula (7.15) at p. 403 is current and diagram-exact.

### Exposé XII

1. **p. 410 (French FIX #48).** EN 13148:
   `(f'_{H_{n,U'}})^\vee` -> `(f'_{H_{n,U',X'}})^\vee`.

2. **p. 413 invariant name.** EN 13227 first introduces `\mathrm{NW}_{f'}^{G,\varphi}(x)`, while the definition and authority use `\mathrm{NW}_{f}^{G,\varphi}(x)`. Remove the prime in this first occurrence.

3. **pp. 418–422, Lemma 4.7 is substantially abridged and internally broken.** On the refreshed audit snapshot, replace EN 13424–13490 (from `If the vector space` through the false shortcut `as was required`) with the complete translation below. This restores the proof that `u(f'_R)` is `k[G]`-linear, the definition of `x_0=x/x'`, the nonzero argument, the corrected four-link calculation, and the final one-dimensional `\varepsilon` argument:

   ```tex
   The homomorphism $u(f'_R)$ is a homomorphism of $k[G]$-modules. Indeed,
   for $x\in\fm$ one has
   \[
   \begin{aligned}
   u(f'_R)\bigl(g(x\bmod\fm^2)\bigr)
   &=(f'_R(gx)-gx)\bmod\fm^{r+1}\\
   &=g(f'_R(x)-x)\bmod\fm^{r+1}
   =g\,u(f'_R)(x\bmod\fm^2).
   \end{aligned}
   \]

   Finally, $u(f'_R)\ne0$. Indeed, by condition b) there exists an element
   $x_0\in R$ such that
   $f'_R(x_0)-x_0\notin\fm^{r+1}$. But we need such an element in $\fm$.
   To obtain one, write $x_0$ in the form
   \[
   x_0=\frac{x}{x'},\qquad x,x'\in\fm,\quad x'\notin\fm^{r+1}.
   \]
   At least one of the elements $x,x'$ satisfies the required condition.

   Suppose, for contradiction, that simultaneously
   \[
   f'_R(x)-x\in\fm^{r+1},
   \qquad
   f'_R(x')-x'\in\fm^{r+1}.
   \]
   Then, in the field of fractions $K$ of $A$, one has
   \[
   \frac{f'_R(x)}{x}\in1+\fm^r,
   \qquad
   \frac{f'_R(x')}{x'}\in1+\fm^r.
   \]
   We may suppose that $f'_R(x')\ne0$, since otherwise $x'$ is the desired
   element. Since $1+\fm^r$ is a multiplicative group, it follows that
   \[
   \frac{x'}{f'_R(x')}\in1+\fm^r,
   \]
   and consequently
   \[
   \frac{f'_R(x)}{x}\cdot\frac{x'}{f'_R(x')}\in1+\fm^r.
   \]
   This last relation implies
   \[
   \frac{f'_R(x_0)}{x_0}\in1+\fm^r.
   \]
   Indeed,
   \[
   \begin{aligned}
   \frac{f'_R(x_0)}{x_0}
   -\frac{f'_R(x)}{x}\cdot\frac{x'}{f'_R(x')}
   &=\frac{f'_R(\frac{x}{x'})}{\frac{x}{x'}}
   -\frac{f'_R(x)}{x}\cdot\frac{x'}{f'_R(x')}\\
   &=\frac{x'f'_R(\frac{x}{x'})}{x}
   -\frac{f'_R(x)}{x}\cdot\frac{x'}{f'_R(x')}\\
   &=\frac1x\left(
   \frac{x'f'_R(x')f'_R(\frac{x}{x'})-x'f'_R(x)}
   {f'_R(x')}\right)=0.
   \end{aligned}
   \]
   Thus $f'_R(x_0)-x_0\in\fm^{r+1}$, a contradiction.

   If the vector space
   \[
   \Hom_k(\fm/\fm^2,\fm^r/\fm^{r+1})
   \]
   is endowed with its usual $G$-module structure, its element $u(f'_R)$
   belongs to the subspace
   \[
   \Hom_k(\fm/\fm^2,\fm^r/\fm^{r+1})^G
   \]
   of $G$-invariants.

   It is classical that the vector space $\fm^i/\fm^{i+1}$ identifies
   canonically with the $i$-th tensor power
   $\bigotimes_k^i(\fm/\fm^2)$. Consequently
   $\Hom_k(\fm/\fm^2,\fm^r/\fm^{r+1})$ identifies by the homomorphism of
   contraction with the $(r-1)$-st tensor power
   $\bigotimes_k^{r-1}(\fm/\fm^2)$:
   \[
   \gamma:\Hom_k(\fm/\fm^2,\fm^r/\fm^{r+1})
   \longrightarrow\bigotimes_k^{r-1}(\fm/\fm^2).
   \]
   Through $\gamma$, the $G$-module structure on the Hom-space is
   transported to the $G$-module structure on
   $\bigotimes_k^{r-1}(\fm/\fm^2)$ induced by that on $\fm/\fm^2$:
   \[
   g(\xi_1\otimes\xi_2\otimes\cdots\otimes\xi_{r-1})
   =g\xi_1\otimes\cdots\otimes g\xi_{r-1}.
   \]
   Denote by $\mu(f'_R)$ the image of $u(f'_R)$ under $\gamma$. Thus:
   \begin{enumerate}
   \item[I)] $0\ne\mu(f'_R)\in\bigotimes_k^{r-1}(\fm/\fm^2)$;
   \item[II)] $\mu(f'_R)$ is invariant under $G$.
   \end{enumerate}

   We can now conclude the proof of Lemma 4.7. Since the vector space
   $\fm/\fm^2$ has dimension one,
   \[
   \Aut_k(\fm/\fm^2)=k^*.
   \]
   Therefore the image of $G\to\Aut_k(\fm/\fm^2)$ is a finite cyclic
   subgroup of $k^*$, generated by a primitive $c$-th root of unity
   $\varepsilon$. It is generated by the automorphism
   \[
   \chi:\fm/\fm^2\longrightarrow\fm/\fm^2,
   \qquad \xi\longmapsto\varepsilon\xi.
   \]
   Since $\mu(f'_R)$ is invariant under $G$,
   \[
   \mu(f'_R)
   =\chi\mu(f'_R)
   =\chi\sum_i\xi_{1i}\otimes\xi_{2i}\otimes\cdots\otimes\xi_{r-1,i}
   =\sum_i\varepsilon\xi_{1i}\otimes\varepsilon\xi_{2i}
     \otimes\cdots\otimes\varepsilon\xi_{r-1,i}
   =\varepsilon^{r-1}\mu(f'_R),
   \]
   that is,
   \[
   (1-\varepsilon^{r-1})\mu(f'_R)=0.
   \]
   Since $\mu(f'_R)\ne0$, it follows that
   $1-\varepsilon^{r-1}=0$, that is, $c\mid(r-1)$.
   ```

   Authority: FR 13568–13658. The former English not only dropped displays; it referred to `x_0`, `x`, and `x'` without ever introducing them and replaced the actual final argument by an unsupported conclusion.

4. **p. 435 source correction.** EN 13841 and 13845 on the audit snapshot use `\nu=p_2(u)` and pass `\nu` to `\alpha_{x'}`. The final French/source-corrected reading is `v=p_2(u)` and `v` in both places. The printed glyph `U` was adjudicated as a slip for `v`.

5. **p. 425, formula (5.2) is still internally abridged.** EN 13581–13584 on the audit snapshot has the tag but omits the second equality present at FR 13757–13763. Replace it with:

   ```tex
   \begin{equation}\tag{5.2}
   \begin{aligned}
   c^\varphi(g)\,\Tr_{\bZ_\ell[G],\varphi}
     (f'^\vee_{H_{U',X'}(\ell)})(g)
   &=\Tr_{\bZ_\ell}(g_{X'}^{-1}f')^\vee_{H_{U',X'}(\ell)}\\
   &=\Tr_{\bZ_\ell}(g_{X'}^{-1}f')_{H^\vee_{U',X'}(\ell)}.
   \end{aligned}
   \end{equation}
   ```

   This omission is invisible to tag-count parity and was detected by comparing the content of every matched tagged formula.

6. **§5.10(b), the multiplicity-one hypothesis was changed.** Replace the full subheading by:

   ```tex
   \subsubsection*{b) The case of multiplicities $1$:
   $\nu_{x'}(g_{X'}^{-1}f')=1$ for every
   $x'\in {Y'}^{g_{Y'}^{-1}f'_{Y'}}$ and every $g\in G$.}
   ```

   Authority: FR 13814. The inherited `g^{-1}_{X'}` and `Y'\cap{X'_x}^{g^{-1}f'}` are not the printed/source-checked hypothesis.

7. **§6.4(b), membership was mistranscribed as equality.** Replace the opening `Let $x'=X_x'{}^{f'}$` with `Let $x'\in X_x'{}^{f'}$`. Authority: final French FR 14011 and its source-correction note.

8. **§7, geometric-generic-point bars are missing in the `H`-module block.** Replace the block from `one obtains the isomorphisms` through the existence of `H_1` with:

   ```tex
   one obtains the isomorphisms
   \[
   \begin{tikzcd}[column sep=large]
   H \arrow[r,"\Psi"] & H
   \end{tikzcd}
   \qquad
   \begin{tikzcd}[column sep=large]
   F_{\bar\eta} \arrow[r,"u_{\bar\eta}"] & F_{\bar\eta},
   \end{tikzcd}
   \]
   where $F_{\bar\eta}$ has an $H$-module structure and the following
   relation holds:
   \[
   u_{\bar\eta}(gx)=\Psi(g)\,u_{\bar\eta}x,
   \qquad g\in H,\quad x\in F_{\bar\eta}.
   \]
   If $H_1$ is the largest distinguished subgroup of $H$ of finite index
   such that $F_{\bar\eta}^{H_1}=F_{\bar\eta}$, then
   $\Psi(H_1)=H_1$. Such a subgroup exists because the sheaf $F_\eta$ is
   constructible.
   ```

   Authority: FR 14176–14192. The last `F_\eta` is deliberately unbarred in the source; only the fibre representation and `u` carry `\bar\eta`.

9. **Restored/current; do not duplicate work.** Formula (4.9.2), Proposition 5.1 with (5.1.1), and the full §§6.2–6.3 source blocks through (6.3.12) are present. XII now has exact coarse parity: 53 tags, three statements, four TikZ blocks, and 42 `equation` environments in each language. Printed p. 435 duplicates p. 434; both authorities correctly transcribe the content once. The pp. 438–439 §7.1-to-Proposition 7.2 flow is current.

### Exposé XV

1. **p. 444, entire relative-Frobenius diagram omitted.** EN 14084–14088 says that one obtains a commutative diagram with cartesian square, but the diagram is absent. Insert the following final-French block **after the sentence ending `in which the square is cartesian.` and before EN 14090 `It is clear that ...`**:

   ```tex
   \[
   \begin{tikzpicture}[baseline=(current bounding box.center),>=stealth]
   \node (XL) at (0,2.0) {$X$};
   \node (XM) at (3.0,2.0) {$X^{(p/S)}$};
   \node (XR) at (6.0,2.0) {$X$};
   \node (SL) at (0,0) {$S$};
   \node (SM) at (3.0,0) {$S$};
   \draw[->] (XM) -- node[below] {$\pi_{X/S}$} (XL);
   \draw[->] (XR) -- node[below] {$\Fr_{X/S}$} (XM);
   \draw[->] (XR) .. controls (5.1,3.2) and (0.9,3.2) .. node[above] {$\fr_X$} (XL);
   \draw[->] (XL) -- node[left] {$g$} (SL);
   \draw[->] (XM) -- node[right] {$g^{(p)}$} (SM);
   \draw[->] (XR) -- node[pos=.55,above right] {$g$} (SM);
   \draw[->] (SM) -- node[below] {$\fr_S$} (SL);
   \end{tikzpicture}
   \]
   ```

   Authority: final French FR 14284–14299. Original LNM 589 crop `p444_top.png` visibly confirms all five nodes, the curved $\fr_X$ arrow, the two $g$ arrows, $g^{(p)}$, $\pi_{X/S}$, $\Fr_{X/S}$, and $\fr_S$. This closes the 4-versus-5 TikZ discrepancy.

2. **p. 455 editorial gloss (French FIX #59).** After adding the `\alpha` label at EN 14441, delete EN 14445 `where $\alpha:F\to g_*g^*F$ is the adjunction.` Continue with `In other words, for every prescheme $U$ étale over $X$, ...`.

3. **p. 458 pushforward (French FIX #52).** Replace the affected part of EN 14527 so it identifies `\RGamma_X(F)` with `H^0(X,I)` and `\RGamma_X(\fr_{X*}F)` with `H^0(X,\fr_{X*}I)`. It currently has the wrong pullback `\fr_X^*F` and noncanonical `\RGamma(X,...)` notation.

4. **p. 460, the proof-of-Corollary diagram is topologically incomplete.** Replace the compact English diagram following `This follows from the commutative diagram` with the complete final-French block:

   ```tex
   \[
   \resizebox{\textwidth}{!}{%
   \begin{tikzpicture}[baseline=(current bounding box.center),>=stealth,font=\scriptsize]
   \node (A) at (0,3.6) {$\RGamma_{X\times X'}(F\boxt F')$};
   \node (B) at (4.7,3.6) {$\RGamma_{X\times X'}(F\boxt\fr_{X'}^*(F'))$};
   \node (C) at (9.4,3.6) {$\RGamma_{X\times X'}(F\boxt F')$};
   \node (D) at (3.3,1.9) {$\RGamma_{X\times X'}(\fr^*_{X\times X'}(F\boxt F'))$};
   \node (E) at (9.4,1.9) {$\RGamma_{X\times X'}(\fr_X^*(F)\boxt F')$};
   \node (F) at (4.4,0.25) {$\RGamma(\Fr^*_{F\boxt F'/X\times X'})$};
   \node (G) at (9.4,0.25) {$\RGamma_{X\times X'}(F\boxt F')$};
   \draw[->] (A) -- node[above] {$\id_X\times\fr_{X'}$} (B);
   \draw[->] (B) -- node[above] {$\RGamma(\id_F\otimes\Fr^*_{F'/X'})$} (C);
   \draw[->] (A) -- node[below left] {$\fr_{X\times X'}$} (D);
   \draw[->] (B) -- node[left] {$\fr_X\times\id_{X'}$} (D);
   \draw[->] (C) -- node[right] {$\fr_X\times\id_{X'}$} (E);
   \draw[->] (D) -- node[above] {$\RGamma(\id_{\fr_X^*(F)}\otimes\Fr^*_{F'/X'})$} (E);
   \draw[->] (E) -- node[right] {$\RGamma(\Fr^*_{F/X}\otimes\id_{F'})$} (G);
   \draw[->] (D) -- (G);
   \end{tikzpicture}%
   }
   \]
   ```

   Authority: FR 14794–14814 and original LNM crop `p460_top.png`. The source has seven nodes and eight edges. The compact English five-node version removes the intermediate `\RGamma(\fr_X^*F\boxt F')` node and the first of the two lower morphisms, while labeling the collapsed arrow by only the second morphism.

5. **p. 445 transitivity diagram: current.** The audited English block matches the final French, including `\Fr_{X/Y}` and the bent `\Fr_{X/S}` arrow.

6. Apart from the two diagram repairs, the exact-row tranche above, and FIX #52/#59, XV has coarse parity (five tags and 23 statements in both languages).

#### Additional XV formula/notation debt found by ordered-math audit

1. **Affine/projective presentation: `\JJ'` was conflated with `\JJ^{(p)}`.** Replace the affected formula and opening of the next sentence with:

   ```tex
   \[
   \mathcal{A}^{(p)}
   \simeq \OO_S[T_1,\ldots,T_n]/\JJ',
   \]
   where $\JJ'$ is the image in $\OO_S[T_1,\ldots,T_n]$ of
   $\JJ^{(p)}=\JJ\otimes_{\OO_S}\OO_{(S,\fr_S)}$; the ideal $\JJ'$ is
   deduced from $\JJ$ by raising the coefficients of the polynomials to
   the $p$-th power.
   ```

   Authority: FR 14498–14501. The inherited English uses `\JJ^{(p)}` for both the base-changed ideal and its image in the polynomial ring, erasing the source's distinction.

2. **p. 459, Proposition 3 has its two identity factors swapped.** Replace the three inherited displays in the proposition by:

   ```tex
   \[
   \begin{aligned}
   \Fr^*_{F\boxt_\Lambda F'/X\times X'}
   &=\Fr^*_{F/X}\otimes\Fr^*_{F'/X'}\\
   &=(\Fr^*_{F/X}\otimes\id_{\fr_{X'}^*F'})
     \circ(\id_F\otimes\Fr^*_{F'/X'})\\
   &=(\id_{\fr_X^*F}\otimes\Fr^*_{F'/X'})
     \circ(\Fr^*_{F/X}\otimes\id_{F'}).
   \end{aligned}
   \]
   ```

   Immediately afterward, replace `the case where $F=X$ and $F'=\Lambda_{X'}$` with `the case where $F=\Lambda_X$ and $F'=\Lambda_{X'}$`.

   Authority: FR 14755–14779 and original LNM crops `p459_top.png` / `p459_mid.png`.

3. **pp. 460–461, bars were systematically dropped from the geometric-Frobenius construction.** Replace the paragraph from `We shall apply this result to the particular case` through the definition of the arithmetic inverse by:

   ```tex
   We shall apply this result to the particular case where
   $X'=\bar e=\Spec(\overline{\mathbb F}_p)$ is the spectrum of an
   algebraic closure $\overline{\mathbb F}_p$ of $\mathbb F_p$ and where
   $F'=\Lambda_{\bar e}$ is the constant sheaf with fibre $\Lambda$.
   In this case put
   \[
   \overline X=X\times_e\bar e
   =X\otimes_{\mathbb F_p}\overline{\mathbb F}_p,
   \qquad
   \overline F=F\otimes_\Lambda\Lambda_{\bar e},
   \]
   the inverse image of $F$ by the projection $\overline X\to X$.
   The Frobenius endomorphism $\fr_{\bar e}$ is identified with the
   canonical generator
   \[
   f:\lambda\longmapsto\lambda^p
   \qquad(\lambda\in\overline{\mathbb F}_p)
   \]
   of the Galois group
   \[
   \pi_e=\Gal(\overline{\mathbb F}_p/\mathbb F_p),
   \]
   where $f$ determines an isomorphism
   $\widehat{\mathbb Z}\simeq\pi_e$, and
   \[
   \Fr^*_{\Lambda_{\bar e}/\bar e}=\id_{\Lambda_{\bar e}}
   \]
   since $\Lambda_{\bar e}$ is a constant sheaf. Put
   \[
   \overline{\fr}_X=\fr_X\times\id_{\bar e},
   \]
   the inverse image of $\fr_X$ by $\overline X\to X$,
   \[
   f_X=\id_X\times\fr_{\bar e},
   \]
   the automorphism of $\overline X$ defined by $f$ by transport of
   structure, and
   \[
   \overline{\Fr}^*_{F/X}
   =\Fr^*_{F/X}\otimes\id_{\Lambda_{\bar e}},
   \]
   the inverse image of $\Fr^*_{F/X}$ by $\overline X\to X$. We may write
   \[
   \fr_{\overline X}
   =\overline{\fr}_X\circ f_X
   =f_X\circ\overline{\fr}_X,
   \qquad
   \Fr^*_{\overline F/\overline X}
   =\overline{\Fr}^*_{F/X}.
   \]
   The corollary of Proposition 3 shows that the endomorphism of
   $\RGamma_{\overline X}(\overline F)$ defined by the pair
   $(\overline{\fr}_X,\overline{\Fr}^*_{F/X})$ is the inverse of the
   automorphism defined by $f_X$. We shall say that
   $(\overline{\fr}_X,\overline{\Fr}^*_{F/X})$ is the geometric
   Frobenius correspondence; it is the inverse image by
   $\overline X\to X$ of the Frobenius correspondence on $(X,F)$. Denote by
   \[
   \fr_{\RGamma_{\overline X}(\overline F)}
   \]
   the automorphism of $\RGamma_{\overline X}(\overline F)$ which it
   defines. The arithmetic Frobenius operation, coming by transport of
   structure from $f\in\pi_e$, is its inverse.
   ```

   Authority: FR 14825–14865 and original LNM crops `p460_bot.png` / `p461_top.png`. The inherited English drops the bar on `e` in every occurrence and, more seriously, twice writes the defining pair with `\fr_X` instead of `\overline{\fr}_X`.

4. **p. 471, missing coefficient-field footnote and misplaced bars on `\Fr`.** Replace the paragraph beginning `Transform formula (2) further` through the equality preceding `Apply this result` with:

   ```tex
   Transform formula (2) further by supposing that $X$ is proper, which
   allows us to write ordinary cohomology instead of cohomology with
   proper support. Recall that the category of $\mathbb Q_\ell$-sheaves
   on $X$ is a category of fractions of the category of $\ell$-adic
   sheaves. By abuse of notation, we shall henceforth denote by
   $F=(F_\nu)_{\nu\in\mathbb N}$ the $\ell$-adic
   sheaf\footnote{To simplify the notation, for the remainder of the
   proof we shall suppose that $\Omega=\mathbb Q_\ell$. In the general
   case, one would have to replace $\mathbb Z_\ell$ by the normal closure
   of $\mathbb Z_\ell$ in $\Omega$. (Details left to the reader.)}
   on $X$ corresponding to the $\mathbb Q_\ell$-sheaf underlying $F$.
   Then $\bar F=(\bar F_\nu)$ and the Frobenius morphisms
   $\overline{\Fr}^*_{F_\nu/X}$ define a morphism of $\ell$-adic sheaves
   \[
   \overline{\Fr}^*_{F/X}:
   \fr_X^*(\bar F)\longrightarrow\bar F,
   \]
   hence an $\ell$-adic correspondence on $(\bar X,\bar F)$. For every
   integer $\nu$, the endomorphism
   $\fr_{R\Gamma_{\bar X}(\bar F_\nu)}$ defined by
   $(\bar{\fr}_X,\overline{\Fr}^*_{F_\nu/X})$ is the inverse of
   $f_{R\Gamma_{\bar X}(\bar F)}$ (§2, no.~3, Corollary to Proposition 3).
   Using the definition of $\ell$-adic cohomology, it follows that the
   endomorphism $\fr_{H^i(\bar X,\bar F)}$ of $H^i(\bar X,\bar F)$
   defined by $(\bar{\fr}_X,\overline{\Fr}^*_{F/X})$ is the inverse of
   $f_{H^i(\bar X,\bar F)}$; thus
   \[
   f^{-n}_{H^i(\bar X,\bar F)}
   =\fr^n_{H^i(\bar X,\bar F)}
   \]
   for every $n\ge1$ and every $i$.
   ```

   Two downstream occurrences must match this notation:

   - after formula (2'), use the correspondence `$(\bar{\fr}_X,\overline{\Fr}^*_{F/X})$`;
   - in the notation-lightening sentence, use `$(\overline{\Fr}^*_{F/X})^n$`.

   Authority: FR 15104–15128. The inherited display `\Fr^*_{\bar F/X}:\fr_X^*(F)\to\bar F` is wrong in both the morphism name and its domain. Footnote count is FR/EN = 1/0 before repair.

## Independent ordered-display cross-check

A second audit extracted every outer `equation`/display block in source order and aligned the French and English sequences by normalized TeX similarity, with tagged displays forced to their matching tag. This is independent of the correction-receipt classifications above.

- **X:** 142 French / 142 English outer display blocks. There were no extreme mismatches or unmatched source displays. This supports—but does not by itself prove—the bounded X residual list above.
- **XII:** 137 French / 141 English blocks. The count excess comes from inherited English choices to set some definitions as standalone displays. The source-only aligned cluster at French local lines 329, 338, and 403–415 is precisely the missing Lemma 4.7 material recorded in item 3: the `k[G]` calculation, `x_0=x/x'`, and the final `\varepsilon` argument. No additional source-only mathematical cluster was found outside that known proof debt.
- **XV:** 164 French / 167 English blocks. The only extreme source/English topology mismatch is the known p. 460 seven-node/eight-edge diagram versus the compact five-node English block. The extra English Proposition 3 display is a formatting split that remains substantively wrong for the identity-factor reason in additional item 2. No additional unlisted source-only display cluster was found.
- **Index:** 108 `\sgaindexentry` records in each language; the eleven `XIV` readings remain the printed/source-faithful choice documented below.

This cross-check is a guard against display omissions, not a completion claim: prose, inline mathematics, terminology, and scan ambiguities still require the exact source-critical review and promotion gates specified by the parent task.

## Explicit no-patch checks

- p. 338, D1/D2: current English and final French have the same seven nodes and ten edges in each diagram. The D2 label-side placement is graphical only.
- p. 403, (7.15): exact node/edge match.
- pp. 438–439: source-continuous flow preserved.
- p. 445: exact relative-Frobenius labels preserved.

## Rejected-choice / authority ledger entries required with promotion

| Location | Authority reading to retain | Rejected smoother reading |
|---|---|---|
| X p. 384 | `(Lemma 5.1)` | local numbering suggests `Lemma 4.1` |
| X p. 386 | `point y' and C'`; `(C,y',G)` | inherited `point y' of C'`; `(C',y',G)` |
| X p. 388 | `Sw_{y'}`, `Sw'_{y'}`, `Art_{y'}` in Remark 4.6 | inherited unprimed `y` |
| XV p. 472 | bare `$F$` annihilated by `\ell^{\nu+1}` | smoother `$F_\nu$` |
| XV p. 475 | bare `$K'$` in the transported-endomorphism sentence | stagewise `$K'_\nu$` |
| Index pp. 481–484 | eleven `XIV` final-exposé references | title-consistent `XV` |

## Recommended parent patch order

1. Apply the bounded X residuals; do not touch the now-restored §§3.6–3.9 block except for verified corrections above.
2. Replace the full XII Lemma 4.7 proof interval, then apply the remaining bounded XII corrections listed above; do not replace the now-restored §4.9, Proposition 5.1, or §§6.2–3.
3. Insert the p. 444 XV diagram, restore the complete p. 460 diagram, then apply the 13 XV exact-row corrections and FIX #52/#59.
4. Re-run tag/statement/TikZ parity, compile, render and inspect every changed source page, then update the shared continuation cursor and promotion receipts.
