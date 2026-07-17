# SGA 5 independent residual audit — Exposés V, VI, and VIII

Audit date: 2026-07-17 (Europe/Berlin)

Scope: independent source-critical comparison of the active English cumulative against the final French authority and the original LNM 589 scan. The pass was deliberately broader than the exact-candidate receipt: it compared all inline mathematics, all display blocks, and every paired diagram topology in Exposés V, VI, and VIII.

## Snapshot before this tranche

- Active English TeX SHA-256: `272EB79D01EED8F07D2EEA1F71C10CDAD6A7B0B599AA6903649C2D1624C61DEE`
- Final French authority SHA-256: `791F4EFFC5E02832D5D77ED03518C8156D6F07E4C8238B03545DB93D883FBB28`
- Original scan SHA-256: `B256EBD072A8C68209518412A263C9289C6F1854A346733D86F885930D5FE6CA`
- Active English line numbers below refer to that pre-tranche snapshot.

Gate result at the snapshot: **not synchronized**. The receipt-listed V/VI/VIII corrections were present, and all coarse statement/tag/item/footnote counts were current, but the broader audit found source-critical notation and diagram-topology debt outside the receipt list.

## Structural parity and why it was insufficient

| Exposé | Diagrams EN/FR | Tags EN/FR | Statements EN/FR | Footnotes EN/FR | Displays EN/FR | Finding |
|---|---:|---:|---:|---:|---:|---|
| V | 26/26 | 8/8 | 48/48 | 0/0 | 185/185 | counts exact, but three paired diagrams have wrong topology |
| VI | 3/3 | 10/10 | 25/25 | 1/1 | 122/123 | the one-display delta is only the inline rendering of `U(X)` in Notation 1.5.4; seven source-notation repairs and two bounded prose/notation repairs remain |
| VIII | 13/13 | 1/1 | 7/7 | 6/6 | 110/110 | counts exact, but the §8 tensor variables are systematically assigned to the wrong module sides |

## Exact production operations

### Exposé V

1. **Printed p. 206; FR 6683; EN 6876 — internal Hom underline.**

   Old:
   ```tex
   \Hom_{\widehat{\cC}}(M\otimes_A X,Y)=\Hom_A(M,\Hom_{\cC}(X,Y)).
   ```
   New:
   ```tex
   \Hom_{\widehat{\cC}}(M\otimes_A X,Y)=\uHom_A(M,\Hom_{\cC}(X,Y)).
   ```

2. **Printed p. 209; FR 6791; EN 6984 — variable in the extension proof.**

   Old: `the integer $s+t$`

   New: `the integer $r+t$`

   Authority decision: the French control is controlling. The scan itself visibly reads `s+t`; that is the rejected source-error reading, because the proof has introduced only `r` and `t`. Scan evidence: `v_vi_viii_scan_evidence/scan_printed_p209-221.png`.

3. **Printed p. 212; FR 6894–6897; EN 7086–7089 — target of `v_{rY}`.** Replace the whole current block:

   ```tex
   \begin{tikzcd}[column sep=large,row sep=large]
   Y[r] \arrow[d,"{v_{rY}}"']\\
   X \arrow[r] & Y .
   \end{tikzcd}
   ```

   with:

   ```tex
   \begin{tikzcd}[column sep=large,row sep=large]
   & Y[r] \arrow[d,"{v_{rY}}"]\\
   X \arrow[r] & Y .
   \end{tikzcd}
   ```

   The old code sends the canonical map from `Y[r]` to `X`; the source sends it to `Y`. Scan evidence: `v_vi_viii_scan_evidence/scan_printed_p212-224.png`.

4. **Printed p. 216; FR 7019–7022; EN 7210–7214 — omitted side of the canonical triangle.** Replace:

   ```tex
   \begin{tikzcd}[column sep=large,row sep=large]
   & X[s] \arrow[dl,"\rho"']\\
   X[r] \arrow[d,"{v_{rX}}"']\\
   X
   \end{tikzcd}
   ```

   with:

   ```tex
   \begin{tikzcd}[column sep=large,row sep=large]
   X[r] \arrow[d,"{v_{rX}}"'] & X[s] \arrow[l,"\rho"'] \arrow[dl,"{v_{sX}}"]\\
   X & {}
   \end{tikzcd}
   ```

   Scan evidence: `v_vi_viii_scan_evidence/scan_printed_p216-228.png`.

5. **Printed p. 220; FR 7124–7127; EN 7316–7319 — shifted exact-sequence diagram.** Add the source's leading empty top cell:

   Old top row begins:
   ```tex
   A/J^{n+1}\otimes_A X_m ...
   ```
   New top row begins:
   ```tex
   {} & A/J^{n+1}\otimes_A X_m ...
   ```

   Without this cell, the English vertical maps `f_{nm}`, `g_{nm}`, `h_{nm}` land one object too far left (in particular `f_{nm}` lands at the bottom `0`). Scan evidence: `v_vi_viii_scan_evidence/scan_printed_p220-232.png`.

6. **Printed p. 226; FR 7310; EN 7502 — wrong target index.**

   Old: `\gr^p(X_m)\longrightarrow\gr^p(X_{p+r})`

   New: `\gr^p(X_m)\longrightarrow\gr^p(X_{n+r})`

   Scan evidence: `v_vi_viii_scan_evidence/scan_printed_p226-238.png`.

7. **Printed pp. 247 and 249; FR 8089–8092 and 8149–8152; EN 8281–8284 and 8341–8344 — lost epimorphism markings.** In both copies of diagram `(d_3)`, change both horizontal arrows:

   Old: `\xrightarrow{\theta_s^{pq}}` and `\xrightarrow{\theta_r^{pq}}`

   New: `\xrightarrow[\epi]{\theta_s^{pq}}` and `\xrightarrow[\epi]{\theta_r^{pq}}`

   Scan evidence: `v_vi_viii_scan_evidence/scan_printed_p247-259.png` and `scan_printed_p249-261.png`.

No action is required for the nearby wording `the functor $P\to P_{AR}$`: the French control names it in that sentence, but the scan prints the functor without a label and the preceding Proposition 2.4.4 has already fixed the name `p_{AR}`. The current English is mathematically and source-equivalent there.

### Exposé VI

1. **Printed p. 261; FR 8447; EN 8637 — omitted proof-step label.**

   Old:
   ```tex
   It is clear that (ii) implies (iii). If \(F\) satisfies (iii), ...
   ```
   New:
   ```tex
   It is clear that (ii) implies (iii).

   (iii) \(\Longrightarrow\) (i): If \(F\) satisfies (iii), ...
   ```

2. **Printed p. 272; FR 8736; EN 8926 — category-pair punctuation.**

   Old: `\((AR-\mathbb Z_\ell)\)-sheaves`

   New: `\((AR,\mathbb Z_\ell)\)-sheaves`

   Authority decision: the French control is controlling. The scan visibly prints a hyphen at this locus; it is rejected as inconsistent with the defined category name `(AR,\mathbb Z_\ell)`. Scan evidence: `v_vi_viii_scan_evidence/scan_printed_p271_273-284.png`.

3. **Printed pp. 274–275; FR 8807–8848; EN 8994–9035 — six unpropagated shriek-under-`R` forms.** Apply these exact replacements within Exposé VI:

   - `R^if_!(M)` -> `R^i_!f(M)`
   - `R^if_!(F)` -> `R^i_!f(F)`
   - `(R^if_!)_{i\in\mathbb Z}` -> `(R^i_!f)_{i\in\mathbb Z}` (two occurrences)
   - prose `the functors \(R^if_!\)` -> `the functors \(R^i_!f\)`
   - `R^if_!:\mathbb Z_\ell...` -> `R^i_!f:\mathbb Z_\ell...`

4. **Printed p. 275; FR 8860; EN 9047 — Leray statement still uses the rejected operator-side shrieks.**

   Old:
   ```tex
   R^i g_!\bigl(R^j f_!(F)\bigr)\Longrightarrow R^{i+j}(g\circ f)_!(F).
   ```
   New:
   ```tex
   R^i_!g\bigl(R^j_!f(F)\bigr)\Longrightarrow R^{i+j}_!(g\circ f)(F).
   ```

   The immediately following tagged `(S)` display was already current. Scan evidence for all shriek placements: `v_vi_viii_scan_evidence/scan_printed_p274_276-286.png`, `-287.png`, and `-288.png`.

All three VI diagrams are exact paired matches. The sole display-count delta is the harmless inline rendering of `U(X)` in English Notation 1.5.4.

### Exposé VIII

1. **Printed p. 352; FR 11622/11638; EN 11776/11792 — wrong Greek proof label.**

   - display `\psi)` -> `\varphi)`
   - prose `To prove $\psi)$` -> `To prove $\varphi)$`

   Scan evidence: `v_vi_viii_scan_evidence/scan_printed_p352-364.png`.

2. **Printed pp. 364–365; FR 12004–12029; EN 12158–12183 — left/right module categories reversed throughout §8's derived tensor setup.** Apply the following exact replacements:

   - `Let $X^\bullet$ be an object of $K^-({}_A\cC)$` -> `... $K^-(\cC_A)$`
   - functor domain `K^-(\cC_A)\longrightarrow K^-(\Ab)` -> `K^-({}_A\cC)\longrightarrow K^-(\Ab)`
   - `Every object $Y^\bullet$ of $K^-(\cC_A)$` -> `... $K^-({}_A\cC)$`
   - derived-functor domain `D^-(\cC_A)\longrightarrow D^-(\Ab)` -> `D^-({}_A\cC)\longrightarrow D^-(\Ab)`
   - `for each object $Y^\bullet$ of $D^-(\cC_A)$` -> `... $D^-({}_A\cC)$`
   - functor domain `K^-({}_A\cC)\longrightarrow D^-(\Ab)` -> `K^-(\cC_A)\longrightarrow D^-(\Ab)`

   This restores the required pairing of a right-module complex `X^\bullet` with a left-module complex `Y^\bullet` over `A`. Scan evidence: `v_vi_viii_scan_evidence/scan_printed_p364-376.png`, `scan_printed_p365_366-377.png`, and `-378.png`.

The receipt repair `K'(A)` -> `K^\bullet(A)` is current throughout Exposé VIII: the section contains no residual `K'`, and all thirteen live instances use `K^\bullet`. The two `\widetilde\gamma_A` repairs are likewise current.

## Verification of the parent's recent V/VI/VIII tranche

The exact-candidate fixes listed in `middle_residual.md` are all present in the audited snapshot:

- V: `0164 0169 0174 0175 0179 0180 0181 0182 0183 0185 0186 0189 0190`
- VI: `0031`
- VIII: `0275 0280 0286 0289 0290 0294 0298`

Rendered pages in `tmp/sga5_audits/render_v_vi_viii` were inspected at original resolution. The restored V p. 240 snake diagram and p. 245 bidegree diagram are legible, aligned, and unclipped. The rendered VIII pages containing the `K^\bullet(A)` and projection-formula fixes are likewise clean. These visual checks do not close the residuals above; the residuals had not yet been applied at the pre-tranche snapshot.

## Post-application receipt

All exact operations above were applied to the active cumulative, and no other exposé was edited by this tranche.

- Audit-snapshot English SHA-256: `272EB79D01EED8F07D2EEA1F71C10CDAD6A7B0B599AA6903649C2D1624C61DEE`
- Immediate pre-application SHA-256: `3B404B06D5C97639D46E3A4A309ACA5579878C4A0BA961A2D926679578F59E25`
- Immediate post-application SHA-256: `35CFDA1D7F3C08401F4091DED20122768340A0E2768F730B31907256FCD3858B`

The two pre-application hashes differ because concurrent, task-authorized III B/VII work landed between the read-only audit snapshot and this bounded V/VI/VIII application. The exact old-string anchors remained live; the V/VI/VIII patch did not touch those concurrent regions.

Post-application machine checks found:

- V: all 193 display/equation blocks paired; all three repaired diagrams now match the French/source topology; the only remaining diagram differences are the source-equivalent compact layout of `(D_1)` and the English restoration of the two explicit `u` labels in Example 1.1.1.
- VI: after accounting for the documented inline `U(X)` representation, all 122 English displays pair exactly with the remaining 122 French displays; all three diagrams are exact matches; no `R^if_!` remains in the cumulative.
- VIII: all 110 display blocks and all thirteen diagrams pair; there is no residual `K'`; all left/right module-side assignments in §8 now match the authority and scan.

Compilation was intentionally deferred on the parent manager's instruction until the concurrent III B and VII writes settle. The post-application hash above therefore records reviewed TeX, not a compile claim.
