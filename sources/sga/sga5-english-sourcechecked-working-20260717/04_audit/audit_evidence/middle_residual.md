# SGA 5 middle residual audit — Exposés III, III B, V, VI, VII, and VIII

Audit date: 2026-07-17 (Europe/Berlin)

Scope: source-critical, read-only audit of the active English cumulative against the final French workpass and, where needed, the original LNM 589 scan. No production TeX was edited by this audit.

## Snapshot and gate result

- Active English workpass: `SGA5_English_sync_workpass.tex`
  - SHA-256 at this audit snapshot: `E7A79F7518D65FE0232FB34DE6E3BC0BC6A799C1E9477B5E9B9FED4A2772F50A`
- Final French authority: `sga5_fr_workpass.tex`
  - SHA-256: `791F4EFFC5E02832D5D77ED03518C8156D6F07E4C8238B03545DB93D883FBB28`
- Exact-candidate receipt: `SOURCE_FORMULA_COMPARISON_EXACT.csv`
  - SHA-256: `EB566F2D37B52214FADE9D045EA20A8B9ECAB0C5DED524CD322601A6F9FFB9A4`
- Original LNM 589 scan: `sga5_src_COMPLETE_SOURCE_PDF.pdf`
  - SHA-256: `E8A3813F28557C1238461AF1B24A6FC43DA8870E2112A5E2CE98F8EB8D1D98E6`

**Gate result: not synchronized.** The receipt layer alone contains 136 still-actionable English corrections in these six exposés. In addition, Exposé III B omits the complete authority block §§5.0–5.8 (source pp. 162–171), Exposé VII omits a proof tail and two diagrams on p. 346, Exposé V omits the p. 245 bidegree diagram, and numerous inherited diagrams in III/III B have lost or reversed mathematically significant arrows and labels.

Current coarse structural comparison at the audit snapshot:

| Exposé | Tags EN/FR | Statements EN/FR | TikZ blocks EN/FR | Footnotes EN/FR | Result |
|---|---:|---:|---:|---:|---|
| III | 142/145 | 18/18 | 60/56 | 3/3 | three source tags absent; four source `tikzpicture` diagrams were reimplemented inaccurately |
| III B | 107/151 | 28/28 | 38/40 | **0/7** | full §§5.0–5.8 missing; two net diagrams and all seven footnotes absent |
| V | 6/8 | 48/48 | 24/25 | 0/0 | tags `(a)`/`(b)` absent; one complete diagram absent |
| VI | 10/10 | 25/25 | 3/3 | 1/1 | coarse parity; one formula correction remains |
| VII | 99/100 | 62/62 | 13/15 | 0/0 | tag `(Q)`, one display, and two complete diagrams absent |
| VIII | 1/1 | 7/7 | 13/13 | 6/6 | coarse parity; seven bounded receipt corrections remain |

Counts alone are not a completion gate: several diagrams have the right environment count but the wrong arrow direction, operator, tensor base, or node.

## Exact-receipt classification

The 197 assigned rows whose receipt disposition was `already-propagated-or-not-bilingual-exact` classify exactly as follows:

| Exposé | Needs nonexact English patch | Current/equivalent | Source-language-only | Total |
|---|---:|---:|---:|---:|
| III | 34 | 4 | 2 | 40 |
| III B | 57 | 0 | 7 | 64 |
| V | 13 | 5 | 6 | 24 |
| VI | 1 | 1 | 2 | 4 |
| VII | 24 | 9 | 9 | 42 |
| VIII | 7 | 7 | 9 | 23 |
| **Total** | **136** | **26** | **35** | **197** |

Every four-digit token below is the suffix of the unique receipt ID `SGA5-EXACT-xxxx`. The `kind`, exact French `old_string`/`new_string`, scan evidence, and source page remain in the CSV and should be carried into the promotion receipt. “Needs” means the corrected French reading must be rendered idiomatically in English; it does not authorize pasting French into the English cumulative.

### Exposé III — 40 rows

- **Needs nonexact English patch (34):**
  `0122 0125 0126 0308 0309 0310 0311 0312 0313 0314 0315 0316 0317 0318 0319 0320 0321 0323 0326 0327 0329 0330 0333 0337 0339 0341 0342 0343 0344 0348 0352 0355 0356 0357`
- **Current/equivalent (4):**
  `0127 0345 0349 0350`
- **Source-language-only (2):**
  `0123 0124`

`0123` preserves the source's ungrammatical French plural and has no English analogue; `0124` restores French `de` in “le carré de 2.6.3,” while the English already expresses the relation idiomatically.

### Exposé III B — 64 rows

- **Needs nonexact English patch (57):**
  `0130 0140 0141 0142 0145 0146 0147 0148 0156 0157 0158 0359 0360 0361 0362 0363 0377 0382 0383 0384 0385 0386 0387 0388 0389 0390 0391 0392 0393 0394 0395 0396 0397 0398 0399 0400 0401 0402 0403 0404 0405 0406 0408 0409 0411 0413 0415 0416 0417 0419 0420 0421 0424 0429 0430 0431 0432`
- **Current/equivalent (0):** none.
- **Source-language-only (7):**
  `0138 0139 0144 0154 0159 0160 0381`

Receipt IDs `0382` through `0406` lie entirely inside the missing §§5.0–5.8 block. Satisfy them through one reviewed full translation of that authority block, not through disconnected sentence patches.

### Exposé V — 24 rows

- **Needs nonexact English patch (13):**
  `0164 0169 0174 0175 0179 0180 0181 0182 0183 0185 0186 0189 0190`
- **Current/equivalent (5):**
  `0161 0166 0167 0177 0184`
- **Source-language-only (6):**
  `0165 0168 0171 0172 0187 0192`

### Exposé VI — 4 rows

- **Needs nonexact English patch (1):** `0031`
- **Current/equivalent (1):** `0037`
- **Source-language-only (2):** `0036 0196`

`0031` is substantive: on p. 277 change the malformed `R^if_!(F)=0` to the source reading `R^i_!f(F)=0`. The sole display-count delta is layout only; direct comparison found no omitted VI block or diagram.

### Exposé VII — 42 rows

- **Needs nonexact English patch (24):**
  `0038 0042 0048 0052 0055 0056 0197 0200 0206 0219 0220 0223 0224 0226 0227 0237 0247 0248 0250 0252 0255 0256 0259 0265`
- **Current/equivalent (9):**
  `0045 0049 0053 0199 0225 0228 0240 0251 0260`
- **Source-language-only (9):**
  `0044 0050 0051 0198 0205 0207 0208 0209 0266`

The most consequential receipt omissions are `0048` (a complete source sentence, p. 294) and `0250` (the displayed identity with `c_d(\check E)` plus “in other words,” p. 340). They must not be reduced to punctuation fixes.

### Exposé VIII — 23 rows

- **Needs nonexact English patch (7):**
  `0275 0280 0286 0289 0290 0294 0298`
- **Current/equivalent (7):**
  `0277 0282 0284 0292 0293 0295 0300`
- **Source-language-only (9):**
  `0272 0273 0274 0278 0279 0283 0296 0297 0302`

The seven patches are bounded: restore quotation marks around “graded” (`0275`), the parenthetical “in $C$, of course” (`0280`), `K'(A) -> K^\bullet(A)` (`0286`), both tildes on `\gamma` (`0289`, `0290`), the proof-heading reference `Proposition 8.1 -> Proposition 5.2` (`0294`), and the source projection-formula punctuation/quotation (`0298`). All thirteen VIII diagrams and its tag are structurally current.

## Exposé III — structural and diagram repair queue

The three missing source tags are independent of receipt prose:

1. Source p. 83, the first proposition square: wrap the current display as an equation and restore tag `(2)` (`0310`; FR around 2044).
2. Source p. 83, the second proposition square: restore tag `(4)` (`0311`; FR around 2060).
3. Source p. 84, the auxiliary displayed identity/diagram: restore the source tag `(*)` (`0313`).

The following blocks require full source-shape replacement or a targeted mathematical repair. Authority line numbers refer to the immutable French SHA above; the English line numbers are intentionally omitted because the shared workpass is changing in parallel.

| Source locus | Required English repair | Why full/targeted replacement is required |
|---|---|---|
| FR 2095–2127, diagram 2.4.0 (pp. 83–84) | Replace the inherited compact `tikzcd` by the exact source topology. | EN omits the labelled nodes `(P,Q)` and `(P_2,Q_2)` and does not preserve the source paths. |
| FR 2145–2165, diagram 2.5.1 (p. 84) | Full source-topology replacement. | EN has only six of the source's eight arrows; the paths through the two lower intermediate nodes are lost. |
| FR around 2203 (p. 86) | Restore the vertical arrow label `\otimes_S^{\mathbf L}`. | The current arrow is unlabeled, obscuring the operation used (`0316`). |
| FR around 2322, projection diagram (p. 89) | Use uppercase `P_1,P_2` and restore the `L_1`/`L_2` decorations. | The scan and CERT control both confirm uppercase projections and the side labels; inherited lowercase `p_i` is not the authority. |
| FR around 2467 | Full four-node correspondence square. | EN drops the vertical `f'_1:X_1\times_S Y_2\to Y` and inserts a spurious equality node. |
| FR around 2482, diagram 3.3.1 | Full replacement. | Wrong primes/operators and missing arrows alter the source comparison. |
| FR around 2520 | Full replacement of the large triangle/rectangle. | EN loses the `(1)`–`(5)` path structure and changes primes. |
| FR 2531 and 2544 | Full replacement of both diagrams. | Wrong primes and $X/Y$ subscripts; the right-hand arrows `(1)`/`(2)` are absent. |
| FR 2557 and 2570 | Restore the source long vertical arrows `(3)` and `(4)`. | Both right-hand vertical morphisms are omitted. |
| FR 2682–2706, diagrams 3.7.1 and 3.7.2 | Full replacement. | In 3.7.1 EN reverses $f:X\to Y$; in 3.7.2 it duplicates $D$, adds a spurious $D\to C'$, and omits $X\to Y$. |
| FR around 2834, diagram 4.2.5 (p. 100) | Bottom-left node `X' -> X`. | The final authority and scan have `X`; inherited `X'` is wrong. |
| FR 2901–2927, cube 4.4.0 (p. 102) | Full source `tikzpicture` replacement. | EN reverses the $C\to C'$ and $D\to D'$ edges. |
| FR around 2935, diagram 4.4.1 | Restore star/shriek pairing exactly. | Bottom RHoms must be `\RHom(d_2''{}^*M_2,d_1''{}^!M_1)` and `\RHom(d_1'{}^*M_1,d_2'{}^!M_2)` (`0126`, `0329`). |
| FR around 2965, diagram 4.4.2 (p. 103) | Full exact replacement, including phantom `(A)`–`(D)` labels. | Current nodes/operators and the route labelling are materially different. |
| FR around 3071, the large proof diagram (p. 105) | Full exact replacement. | Inherited compression changes nodes, maps, and the numbered route used by the proof. |
| FR around 3097 and 3116 | Correct both adjunction strings and the tensor decoration. | Source has `d'_!d'^!P`, `d''_!d''^!Q`; EN repeats `d'^!d'^!P`, `d''^!d''^!Q`. At FR 3116 the outer tensor is underived. |
| FR 3178 and 3183 | Restore each missing left vertical arrow. | The two squares are not squares in the current rendering. |
| FR around 3192, diagram 4.4.6 | Remove the spurious `_Y` from the top-left outer tensor. | Tensor base is not present in the source. |
| FR around 3210, diagram 4.4.7 | `d'{}^!f_*(...) -> d^!f_*(...)`. | Wrong pullback functor in the top-right node. |
| FR around 3513, diagram 5.1.7 (p. 114) | Full replacement. | Right-hand objects use the wrong $f_i^!$/$f_i^*$ pattern. |
| FR 3573, 3578, 3668, 3673 | Reverse the inherited vertical arrows to the source direction. | EN draws $f_{12},f_{23},f_{34}$ bottom-to-top; the source morphisms run top-to-bottom. This is mathematical, not cosmetic. |
| FR around 3681, diagram 5.3.6 (p. 118) | `f_{12*}\otimes f_{34*} -> f_{12}\otimes f_{34}` on the left vertical label. | Source has the unstarred maps. |
| FR around 3865, diagram 6.7.1 (p. 126) | Restore `^{\mathbf L}` on both outer tensor products. | Current English silently makes the two derived products underived. |

Ready bounded replacements for three recurring high-risk shapes (use the English workpass's established `\RHom` spelling in place of French `\uRHom`):

```tex
% p. 89 projection diagram
\begin{tikzcd}[column sep=1.8em,row sep=1.5em]
& X \arrow[dl,"P_1"'] \arrow[dr,"P_2"] & \\
L_1\quad X_1 \arrow[dr,"q_1"'] & & X_2\quad L_2 \arrow[dl,"q_2"] \\
& S &
\end{tikzcd}
```

```tex
% four-node correspondence square, FR around 2467
\begin{tikzcd}[column sep=3.8em,row sep=2.4em]
X_1\times_S Y_2 \arrow[d,"f'_1"'] & X \arrow[l,"p'_1"'] \arrow[dl,"f" description] \arrow[d,"p'_2"] \\
Y & Y_1\times_S X_2 \arrow[l,"f'_2"]
\end{tikzcd}
```

```tex
% 3.3.1, FR around 2482
\begin{tikzcd}[column sep=4.5em,row sep=2.6em]
D(f_{1!}L_1)\overset{\mathbf L}{\otimes}_S f_{2*}L_2
  \arrow[r,"3.1.1"] \arrow[d,"(1)"']
& \RHom_S(f_{1!}L_1,f_{2*}L_2) \arrow[d] \\
f_{1*}DL_1\overset{\mathbf L}{\otimes}_S f_{2*}L_2
  \arrow[r,"(2)"']
& f_*\RHom_S(L_1,L_2),
\end{tikzcd}
```

No additional III prose block omission was found outside the 34 actionable receipt rows. The four source `tikzpicture` blocks were all present only as inaccurate inherited `tikzcd` substitutes; replacing them closes the apparent 60-versus-56 environment anomaly.

## Exposé III B — full missing block and residual queue

### 1. Duplicate title and complete missing §§5.0–5.8

The current English contains the correct title at the start of the exposé and a second, source-absent title immediately before §2:

```tex
\section*{Exposé III B: Calculations of Local Terms}
```

Delete only that second heading; the authority proceeds directly to §2.

The English then jumps from §4.3 directly to:

```tex
\subsubsection*{5.9. Traces and extension of scalars}
```

Insert a complete reviewed English translation of French authority lines 4934–5178 immediately before that heading. This is source pp. 162–171 and contains:

- nine subsections, §5.0 through §5.8;
- 38 `\tag{...}` occurrences in 32 equation environments;
- one diagram, equation/diagram 5.8.4;
- one footnote explaining that `x\in M` means a local section when $M$ is a sheaf;
- receipt corrections `0382`–`0406`.

The 38 missing tag occurrences are exactly:

`5.0.1–5.0.11; 5.2.1–5.2.3; 5.3.1–5.3.6; 5.4.1–5.4.2; 5.6.1–5.6.6; 5.7.1–5.7.5; 5.8.1–5.8.5`.

There are no §5.1 or §5.5 numbered tags in the authority; do not invent them. A filename, compile, or matching statement count cannot close this omission.

### 2. Seven omitted footnotes

The French authority has seven III B footnotes; current English has zero. One lies in the missing §§5.0–5.8 block and will be restored with it. Restore the other six at these exact loci:

| Authority / English anchor | Required English footnote |
|---|---|
| FR 4665; after the sentence saying $(A',B')$, $(A',X')$, $(Y',B')$ are each in general position | `\footnote{(*) with the usual abuse of notation $X'=X'\times\{y'\}$, etc. (where $x'$ (resp.\ $y'$) is the closed point of $X'$ (resp.\ $Y'$).}` |
| FR 5244; after “define an arrow in $D(K)$” | `\footnote{In no.~6 we shall apply the constructions that follow to the case where $M$ is a dualizing complex (6.7).}` |
| FR 5357; immediately after `$|G|$` in Proposition 5.11.1 | `\footnote{If $X$ is a set, $|X|$ denotes the cardinality of $X$.}` |
| FR 5934; after “an action of $G$ by $S$-automorphisms” | `\footnote{We agree that $G$ acts on spaces on the right.}` |
| FR 5934; after “$A$ is a $\Lambda$-algebra” | `\footnote{We are chiefly interested in the case of commutative $\Lambda$-algebras.}` |
| FR 6574; after the sentence defining the lower horizontal arrow | `\footnote{One should be able to replace $P$ by a perfect complex (over $\Lambda[G]$) (or even $P'$ by an object of $D_{\mathrm{ctf}}({}_{\Lambda[G]}Y)$).}` |

The seventh footnote, inside the missing block at FR 4989, should read: `\footnote{If $M$ is a sheaf, the notation $x\in M$ means that $x$ is a local section of $M$.}`

### 3. Early proof and diagrams, source pp. 144–161

| Source locus | Required repair |
|---|---|
| FR 4351–4359, first two diagrams (p. 146) | Replace with the exact source diagrams: restore both vertical `i` labels and phantom region labels `(1)`–`(4)`. |
| Lemma 2.3 proof, FR 4478–4493 | The prose/formulas are present but EN dropped equation tags `(1)`, `(2)`, `(3)`. Restore them on `u=h_*u', v=h_*v'` and the two comparison equalities. |
| Lemma 3.5, FR 4689–4692 | Restore the missing vertical arrow `f:X'\to X`; the `g:Y'\to Y` arrow is already present. |
| FR 4726–4732 (p. 154) | Replace the normalization diagram exactly and restore tag `(*)`; current EN omits the vertical $Z'\to Z$. |
| FR 4756–4764 | Restore the left vertical $X'\to X$ arrow in each of the two trait diagrams. |
| FR around 4801 | Full source replacement of the inclusion diagram; inherited topology and directions are wrong. |
| FR around 4882 | Full source replacement of the specialization square; inherited arrows run in the wrong directions. |

### 4. §5.9 onward, source pp. 171–202

| Source locus | Required repair |
|---|---|
| FR around 5184, diagram 5.9.1 (p. 171) | Top tensor is over $A$, not $A^e$; bottom tensor is over $B$, not $B^e$. Replace the full square. |
| FR around 5276, proof of 5.10 | Restore the complete left label `E\otimes_K 5.10.5`; replace the abbreviated right `res` label by the source label. |
| FR around 5283 and 5320 | Restore the source phantom `(*)` aliases/nodes in both diagrams. |
| FR 5354–5358, Proposition 5.11.1 | Replace inherited tag `5.11.1` by the source tag `(*)`, restore the cardinality footnote, and retain the exact formula. |
| FR 5377–5402, Proposition 5.11.3 proof (pp. 177–178) | Replace the inherited simplified drawing and compressed prose by the exact square 5.11.4, the complete 3-by-2 boundary diagram, and its explanation. The proposition's preceding trace equality is unnumbered; tag `5.11.4` belongs to the square, not to that equality. |
| FR around 6170–6195, diagram 6.14.1 | Replace the inherited array by the source graph or at minimum restore labels `i` and `j`; the exact graph below is preferred. |
| FR around 6356 | Restore vertical labels `d_1^*a` and `d_2^!a`. |
| FR around 6445 | Full source replacement: restore arrows `(1)`–`(5)`, the full middle morphism chain, and phantom labels. |
| FR 6552–6560 (p. 201) | Full replacement and tag `(*)`: restore tensor bases `_\Lambda` and arrows `(1)`–`(3)`. |
| FR 6587–6595 (p. 202) | Full replacement and tag `(**)`: restore arrows `(1)`–`(3)`. |

Exact source graph for 6.14.1:

```tex
\begin{equation}
\begin{tikzpicture}[baseline=(current bounding box.center),>=stealth]
\node (U1) at (0,3.0) {$U$};
\node (C1U) at (2.8,3.0) {$c_1^{-1}(U)$};
\node (C2U) at (2.8,2.15) {$c_2^{-1}(U)$};
\node (U2) at (5.2,2.15) {$U$};
\node (X1) at (0,1.15) {$X$};
\node (C) at (2.8,1.15) {$C$};
\node (X2) at (5.2,1.15) {$X$};
\node (XU1) at (0,0) {$X-U$};
\node (C2XU) at (2.8,0) {$c_2^{-1}(X-U)$};
\node (XU2) at (5.2,0) {$X-U$};
\draw[->] (C1U) -- (U1);
\draw[->] (C1U) -- (C2U);
\draw[->] (C2U) -- (U2);
\draw[->] (U1) -- node[left] {$i$} (X1);
\draw[->] (U2) -- (X2);
\draw[->] (C2U) -- (C);
\draw[->] (C2XU) -- (C);
\draw[->] (C) -- node[above] {$c_1$} (X1);
\draw[->] (C) -- node[above] {$c_2$} (X2);
\draw[->] (XU1) -- node[left] {$j$} (X1);
\draw[->] (XU2) -- (X2);
\draw[->] (C2XU) -- (XU1);
\draw[->] (C2XU) -- (XU2);
\end{tikzpicture}
\tag{6.14.1}
\end{equation}
```

The III B tag delta is explained exactly as follows: 38 tags are inside the missing §§5.0–5.8 block; outside it the source has seven further absent occurrences—three tags `(*)`, one tag `(**)`, and `(1)`, `(2)`, `(3)`—while inherited English adds the source-absent tag `5.11.1`. Net English-minus-French is therefore `-44`.

## Exposé V — residual formula and diagram queue

1. Apply the thirteen receipt patches listed above. In particular, receipt `0180` must restore equation tags `(a)` and `(b)` on p. 224; do not merely parenthesize the labels in prose.
2. Source p. 240, FR 7813–7816: replace the inherited array by the exact snake diagram below. The inherited drawing omits the two source isomorphism labels on the $X$ and $Z$ vertical arrows.
3. Source p. 245, FR 7984–7998: restore “(cf. the adjoining diagram)” and the entire bidegree diagram. This is the one net missing V TikZ block.

```tex
% p. 240
\begin{tikzcd}[column sep=1.35em,row sep=large]
0 \arrow[r] & S_n^k \arrow[r] \arrow[d] & X_{n+k}/J^{n+1}X_{n+k} \arrow[r] \arrow[d,"\sim"'] & Y_{n+k}/J^{n+1}Y_{n+k} \arrow[r] \arrow[d] & Z_{n+k}/J^{n+1}Z_{n+k} \arrow[r] \arrow[d,"\sim"'] & 0\\
0 \arrow[r] & T_n \arrow[r] & X_n \arrow[r] & Y_n \arrow[r] & Z_n \arrow[r] & 0 .
\end{tikzcd}
```

```tex
% p. 245, insert after “it is clear (cf. the adjoining diagram) that ...”
\begin{tikzpicture}[baseline=(current bounding box.center),x=1.0cm,y=1.0cm,>=latex]
\draw[->] (-2.0,0) -- (2.2,0);
\draw[->] (0,-1.0) -- (0,1.6);
\node[below left] at (0,0) {$O$};
\node[below] at (0,0) {$\alpha$};
\draw[->] (0,0) -- (0,1.1);
\draw[->] (0,1.1) -- (1.35,0);
\draw[->] (0,0) -- (1.35,0);
\node[above] at (.22,1.1) {$(p,q)$};
\node[left] at (0,0.55) {$1-r$};
\node[above] at (.72,0.08) {$r$};
\end{tikzpicture}
```

No other V block omission was found. The remaining paired diagrams are mathematically equivalent; small label-side/layout differences are not source debt.

## Exposé VI — bounded correction only

Apply receipt `0031` at p. 277:

```tex
R^i_!f(F)=0\qquad\text{for }i>2d.
```

Receipt `0037` is current; `0036` and `0196` are French-only punctuation/grammar phenomena. All three diagrams, all ten tags, the footnote, and all statement blocks are present. No source block replacement is required.

## Exposé VII — omitted display, tag, proof tail, and diagrams

1. Apply the 24 receipt patches. Receipt `0250` must restore the p. 340 display and transition:

   ```tex
   (9.1.6), it follows that
   \[
   c_d(\check E)\,j_1^*(j_1)_*(y)=c_d(E)\,j_1^*(j_1)_*g_1^*(a_0);
   \]
   in other words, we are reduced to proving 9.4 when ...
   ```

2. Source FR 10035–10039: the projective-bundle display is present in English, but its source tag `(Q)` is absent. Restore it as an equation/tagged display:

   ```tex
   \begin{equation}
   P_T(F)\to T\qquad(F\text{ a locally free }\mathcal O_T\text{-module}),
   \tag{Q}
   \end{equation}
   ```

3. Source p. 333, FR 10916–10921: in Proposition 8.6.3(a), change the left vertical label from inherited `\cup` to source `(8.6.1)`. The right vertical label remains `\cup`.

4. Source p. 346, FR 11419–11434: replace the proof tail after equation 9.8.8 by a complete English translation, including the Hironaka citation and both diagrams. The current English concatenates the argument, omits both diagrams, and ends with the wrong/circular identity. The correct final identity is

   ```tex
   (f_1)_*\circ v_*=u_*\circ f_*.
   ```

   The conclusion uses that $f_*$ is an isomorphism and $u_*$ is a direct monomorphism because $u$ admits a retraction; it does **not** use the preceding base-change identity again.

Exact missing p. 346 diagrams:

```tex
\begin{tikzcd}[column sep=huge,row sep=large]
H\arrow[r,hook,"{t\mapsto(t,0)}"]\arrow[d,"g"']&H\times\mathbb P^1\arrow[r,hook,"{j\times\operatorname{id}}"]\arrow[d,"{g\times\operatorname{id}}"']&X'\times\mathbb P^1=Z'_1\arrow[d,"{f\times\operatorname{id}}"]\\
Y\arrow[r,hook,"\gamma"]&Y\times\mathbb P^1\arrow[r,hook,"{i\times\operatorname{id}}"]&X\times\mathbb P^1
\end{tikzcd}
```

```tex
\begin{tikzcd}[column sep=large,row sep=large]
&X'\arrow[r,hook,"v''"]\arrow[d,"f''"']&Z''\arrow[d,"f''_1"]\\
H\arrow[r,hook]&X'\arrow[r,hook,"v'"]&X'\times\mathbb P^1\\
&t\arrow[r,mapsto]&{(t,0)}
\end{tikzcd}
```

These two omissions exactly explain the 13-versus-15 TikZ count. Apart from the p. 333 label, direct comparison found the other thirteen paired VII diagrams structurally current.

### Controlling Exposé VII production package

The independently compiled and literal-anchor-validated Exposé VII package supersedes the manual line anchors in this section wherever the live file has moved:

- `expose_vii_repair_map.json` — all 24 VII receipt rows, tag `(Q)`, the p. 333 label, and the p. 346 proof tail; every `old_tex` anchor occurred exactly once in English snapshot `8B30D84552E2A9EB04502A28935B4DE15466A171CE7C21136D9A47CE57B2FF82`; SHA-256 `17E4286BEABCE358C996B18150BF5A7E31E8D6561F164D80074DCC010BBBB06D`.
- `expose_vii_p346_replacement.tex` — scan-checked complete proof-tail replacement; SHA-256 `9F79B711B743A5C650D5C1CFD49B8BC5C12469E2B974E0F33FCC741B5BAF2F6B`.
- `expose_vii_repair_package.md` — compile, formula, rendered-page, and scan-evidence handoff; SHA-256 `3B39C80CDA19A87C3F0385073B938F43BE6FE118FDD8119549C9711AEF68AF78`.

The JSON map is the controlling machine patch artifact for VII. In particular, its scan adjudications govern receipts `0248` and `0259`: retain the mathematically necessary symbol $E$ in English despite its omission from the French prose, and use $Z\setminus Y$ rather than the workpass transcription $Z\doteq Y$.

## Exposé VIII — explicit no-block finding

VIII has exact coarse structural parity: thirteen diagrams, one tag, seven statements, six footnotes, and 110 display openings in each authority. Apply only the seven bounded receipt patches already classified. No diagram or prose block replacement is required.

## Rejected-choice / authority ledger entries required with promotion

| Location | Authority reading to retain | Rejected inherited/smoother reading |
|---|---|---|
| III p. 89 | uppercase projections `P_1,P_2` with `L_1,L_2` side decorations | lowercase `p_i` and omitted side labels |
| III 3.7.1/3.7.2 | $f:X\to Y$ in the source direction | reversed $Y\to X$ or omitted $f$ |
| III 4.4.0 | $C\to C'$ and $D\to D'$ | reversed vertical edges |
| III B Prop. 5.11.1 | tag `(*)` and source cardinality footnote | invented tag `5.11.1` |
| III B Prop. 5.11.3 | the trace equality is unnumbered; the full square is 5.11.4 | inherited tag 5.11.4 attached to the equality and untagged simplified square |
| V p. 240 | `\sim` on both the $X$ and $Z$ vertical arrows | unlabeled vertical arrows |
| VII 9.3 (`0248`) | `Denote by $E$ ...`; the following exact sequence begins `0\to E` | literal omission of $E$ in the French/scan prose, which leaves the sentence grammatically and mathematically incomplete |
| VII 9.5 (`0259`) | $Z\setminus Y$, confirmed by the original scan | French-workpass transcription $Z\doteq Y$ |
| VII p. 346 | `(f_1)_*\circ v_*=u_*\circ f_*` and direct monomorphism $u_*$ | circular reuse of $(f'_1)^*\circ v_*=v''_*\circ(f')^*$ and the wrong monomorphism |

## Continuation cursor and parent patch order

Recommended non-overlapping production order:

1. **III receipt tranche:** apply its 34 receipt patches and restore tags `(2)`, `(4)`, `(*)`.
2. **III diagram tranche:** replace the source-critical blocks from 2.4.0 through 6.7.1, compiling and visually comparing each changed source page.
3. **III B early tranche, pp. 144–161:** delete the duplicate title; apply receipt rows through `0377`; restore tags `(1)`–`(3)`, the early diagrams, and the first missing footnote.
4. **III B missing-block tranche, pp. 162–171:** translate FR 4934–5178 as one continuous block, satisfying `0382`–`0406`; preserve all 38 tags, diagram 5.8.4, and the local-section footnote.
5. **III B late tranche, pp. 171–202:** apply remaining receipts; restore §5.11's exact tag ownership and boundary diagram; restore five remaining footnotes and all diagram labels/tags through `(**)`.
6. **V/VI tranche:** apply the bounded receipts, replace the p. 240 snake diagram, insert the p. 245 diagram, and apply VI `0031`.
7. **VII tranche:** apply receipts, add `(Q)`, repair the p. 333 label, and restore the full p. 346 proof tail and two diagrams.
8. **VIII tranche:** apply seven bounded receipt patches only.

After every tranche: compile TeX to PDF; retain the full log; render all changed pages; compare formulas and diagrams against the French authority and scan; update the exact page/correction ledger, terminology/rejected-choice ledger, continuation cursor, and SHA-256 manifest. A successful compile is necessary but not sufficient.

## Audit closure

- All 197 assigned receipt rows are classified once: 136 needs patch, 26 current/equivalent, 35 source-language-only. A set check confirmed 197 unique IDs with no overlap or omission.
- No unresolved receipt ambiguity remains in these six exposés.
- The scan settled the potentially ambiguous III p. 89 uppercase `P_i` reading and all listed arrow/operator disputes.
- This audit does **not** claim that the cumulative is synchronized. Its continuation cursor is the start of the III receipt tranche above; the parent manager must promote only reviewed, compiled, rendered, ledgered tranches.

## Live refresh after parent integration of III B §§5.0–5.8

This section supersedes the earlier snapshot statements about the 38-tag missing block. The parent integrated §§5.0–5.8 while this audit was in progress. At English SHA-256 `2A0B341893FF1996C04DAC49DF7F753A232D00A1C29AFA38A88E1A6A36926B40`, the inserted block is present at the unique heading `\subsubsection*{5.0. Introduction}` and runs continuously through 5.8.5 before `\subsubsection*{5.9. Traces and extension of scalars}`. All 38 block tags, diagram 5.8.4, and the local-section footnote are present. Receipt rows `0382`–`0406` are thereby current in production.

The remaining III B structural delta is now exact:

| Feature | French | English | Delta EN−FR |
|---|---:|---:|---:|
| tags | 151 | 145 | −6 |
| equation environments | 145 | 139 | −6 |
| `tikzcd` | 40 | 39 | −1 |
| `tikzpicture` | 1 | 0 | −1 |
| footnotes | 7 | 1 | −6 |

The six missing equation environments/tags are exactly:

1. Lemma 2.3: restore wrappers/tags `(1)`, `(2)`, `(3)` at FR 4478–4493.
2. Normalization diagram on p. 154: restore its `equation` wrapper and tag `(*)` at FR 4726–4732.
3. Lemma 6.23.3 diagram on p. 201: restore wrapper and tag `(*)` at FR 6551–6560.
4. The induced square on p. 202: restore wrapper and tag `(**)` at FR 6586–6595.

Separately, Proposition 5.11.1 currently has the source-absent tag `5.11.1`; replace it by `(*)`. This changes tag identity but not the equation count. Tag `5.11.4` must remain attached to the full square in the following proof, not to the proposition's preceding unnumbered trace equality.

The two net diagram deficits are exact:

1. FR 5389–5400, the unnumbered 3-by-2 boundary diagram in the proof of Proposition 5.11.3, is entirely absent.
2. FR 6170–6194, diagram 6.14.1, is represented by an inherited `array`; replace it by the exact source `tikzpicture` already transcribed above. Its topology is mostly encoded by the array, but the source labels `i` and `j` are absent, so the source graph remains the completion target.

The six remaining footnotes are precisely those listed in the footnote table above at FR 4665, 5244, 5357, 5934 (two notes), and 6574. The duplicate source-absent III B title immediately before §2 also remains present and should be deleted.

## Machine-usable production appendix — all 136 NEED rows

The line numbers in this appendix refer to the live English SHA `2A0B341893FF1996C04DAC49DF7F753A232D00A1C29AFA38A88E1A6A36926B40`; use the quoted old fragment as the durable anchor if subsequent edits shift lines. `FR` is the exact line in the immutable French authority. For a grouped diagram/block row, the full replacement block earlier in this report is controlling.

### Exposé III — 34 rows

| ID | FR / live EN anchor | Exact production operation |
|---|---|---|
| 0122 | FR 1947 / EN 2233 | `1.7.2 gives a Künneth arrow` -> `1.7.2 gives a \emph{Künneth arrow}`. |
| 0125 | FR 2360 / EN 2602 | `If $X_1$ is smooth, purely ...` -> `If $X_1$ is \emph{smooth}, purely ...`. |
| 0126 | FR 2941 / EN 3155 | `d''_*\RHom(d_2''{}^!M_2,d_1''{}^!M_1)` -> `d''_*\RHom(d_2''{}^*M_2,d_1''{}^!M_1)`. |
| 0308 | FR 1969 / EN 2255 | `$u_i\in\Hom_{f_i}^{(4)}(L_i,M_i)$` -> `$u_i\in\Hom_f^{(4)}(L_i,M_i)$`. |
| 0309 | FR 2045 / EN 2331 | `\RHom(E_1,F_1)\otimes\RHom(E_2,F_2)` -> `\RHom(E_1,F_1)\otimes^{L}\RHom(E_2,F_2)`. Preserve the rest of 2.2.3. |
| 0310 | FR 2063–2069 / EN 2349–2354 | Replace the surrounding `\[ ... \]` of the first square by `\begin{equation}\tag{2} ... \end{equation}`. Diagram body unchanged. |
| 0311 | FR 2074–2080 / EN 2360–2365 | Replace the surrounding `\[ ... \]` of the second square by `\begin{equation}\tag{4} ... \end{equation}`. Diagram body unchanged. |
| 0312 | FR 2080 / EN 2366 | `the commutativity of this square` -> `the commutativity of (4)`. |
| 0313 | FR 2219–2222 / EN 2461–2464 | Replace the display by `\begin{equation}\tag{*}` with `f'_*\RHom(E\otimes^L_SP',f^!Q\otimes^L_SQ')\to\RHom(f'_!(E\otimes^L_SP'),f'_!(f^!Q\otimes^L_SQ'))`, then `\end{equation}`. This removes both inherited `f'^!(Q\otimes Q')` occurrences. |
| 0314 | FR 2210–2212 / EN 2452–2454 | Add the source arrow labels: `\xrightarrow[\sim]{c}` on the first isomorphism and `\xrightarrow[\sim]{d}` on the second. |
| 0315 | FR 2238 / EN 2480 | `as the composite of the arrow above` -> `as the composite of (*)`. |
| 0316 | FR 2204 / EN 2446 | Arrow label `{a\otimes\RHom(P',Q')}` -> `{a\otimes^L_S\RHom(P',Q')}`. |
| 0317 | FR 2295 / EN 2537 | Prefix the sentence by `(2.1.4)`: `(2.1.4) is none other than the arrow deduced ...`. |
| 0318 | FR 2380 / EN 2622 | `\H^0\bigl(C,\RHom(c_1^*L_1,c_2^!L_2)\bigr)` -> `\H^0\bigl(X,c_!\RHom(c_1^*L_1,c_2^!L_2)\bigr)`. |
| 0319 | FR 2398 / EN 2640 | Apply the identical `H^0(C,...)` -> `H^0(X,c_!...)` replacement in formula 3.2.3. |
| 0320 | FR 2438 / EN 2680 | `\Delta_X^!\RHom_S(L_1,L_1)` -> `\Delta_*\Delta^!\RHom_S(L_1,L_1)`. |
| 0321 | FR 2655 / EN 2896 | `\operatorname{cl}(c)\in` -> `\operatorname{cl}(C)\in`. |
| 0323 | FR 2650 / EN 2891 | `denoted $\gamma^*_{X,X_1}$` -> `denoted $\eta_{X_2,X_1}$`. |
| 0326 | FR 2720 / EN 2952 | `g'_!d'^!\xrightarrow{\sim}d^!f_*` -> `g'_*d'^!\xrightarrow{\sim}d^!f_*`. |
| 0327 | FR 2722 / EN 2954 | `f_*c_!c^!\RHom_S(L_1,L_2)` -> `f_*c_*c^!\RHom_S(L_1,L_2)`. |
| 0329 | FR 2940 / EN 3154 | `d'_*\RHom(d_1'{}^!M_1,d_2'{}^!M_2)` -> `d'_*\RHom(d_1'{}^*M_1,d_2'{}^!M_2)`. |
| 0330 | FR 2950 / EN 3164 | In `$g_*K_C=g_*g^!K_D\to K_D$`, change only the second `g_*` to `g_!`: `$g_*K_C=g_!g^!K_D\to K_D$`. |
| 0333 | FR 3118 / EN 3324 | Replace the entire top-left node by `d'_!d'{}^!P\otimes d''_!d''{}^!Q`. This simultaneously restores the two missing shriek-direct-images and makes the outer tensor underived. |
| 0337 | FR 3230 / EN 3434 | Both occurrences `c'{}^!(P\otimes Q)\to d'{}^!f_*(P\otimes Q)` -> `c'{}^!(P\otimes^{\mathbf L}Q)\to d^!f_*(P\otimes^{\mathbf L}Q)`; the missing prime on the target is covered by the structural diagram replacement. |
| 0339 | FR 3420 / EN 3624 | `$\EP(T_s^F)$` -> `$\EP(T^F)$`. |
| 0341 | FR 3552 / EN 3757 | `\RHom(p_{12}^*p_{12,1}^*L_1,p_{12}^!p_{12,2}^*L_2)` -> `\RHom(p_1^*L_1,p_{12}^*p_{12,2}^!L_2)`. |
| 0342 | FR 3554 / EN 3759 | `\RHom(p_{23}^!p_{23,2}^*L_2,p_{23}^!p_{23,3}^!L_3)` -> `\RHom(p_{23}^!p_{23,2}^*L_2,p_3^!L_3)`. |
| 0343 | FR 3552 / EN 3761 prose formula | `\RHom(p_{12}^*L_1,p_{12}^!L_2)` -> `\RHom(p_1^*L_1,p_{12}^*p_{12,2}^!L_2)`. |
| 0344 | FR 3554 / EN 3761 prose formula | `\RHom(p_{23}^!L_2,p_{23}^!L_3)` -> `\RHom(p_{23}^!p_{23,2}^*L_2,p_3^!L_3)`. |
| 0348 | FR 3778 / EN 3983 | `L_1\otimes^{\mathbf L}\cO_{X_2}` -> `L_1\otimes_S^{\mathbf L}\cO_{X_2}`. |
| 0352 | FR 3930 / EN 4135 | In the definition of $\omega$, replace both exterior-power exponents `N` by `d`: `\Lambda^dN_{Y/X}^{\vee}\otimes\Omega^d_{X/S}`. |
| 0355 | FR 3948 / EN 4153 | `$\cl^N_{X/S}(Y)$` -> `$\cl_{X/S}(Y)$`. |
| 0356 | FR 3953 / EN 4158 | Apply the same `$\cl^N_{X/S}(Y)$` -> `$\cl_{X/S}(Y)$` replacement. |
| 0357 | FR 4108 / EN 4313 | `$L_0\in\ob D^b_{\ctf}(X_0,\mathbb F_p)$` -> `$L_0\in\ob D_{\ctf}(X_0,\mathbb F_p)$`. |

### Exposé III B — 57 rows

| ID | FR / live EN anchor | Exact production operation |
|---|---|---|
| 0130 | FR 4512 / EN 4719 | `$P,Q\in\Ob D_{\mathrm{ctf}}^b(Z)$` -> `$P,Q\in\Ob D_{\mathrm{ctf}}(Z)$`. |
| 0140 | FR 4527 / EN 4734 | `into a base-change arrow` -> `into a ``base-change arrow''`. |
| 0141 | FR 4531 / EN 4738 | `followed by projection arrows` -> `followed by ``projection arrows''`. |
| 0142 | FR 4537 / EN 4744 | `Taking $P=DL\lten_{\Lambda}M'$, $Q=L\lten_{\Lambda}DM$` -> `Taking $P=DL\lten_SM'$, $Q=L\lten_SDM$`. |
| 0145 | FR 5325 / EN 5535 | `the tensor-product arrows` -> `the ``tensor-product'' arrows`. |
| 0146 | FR 5332 / EN 5542 | Replace `the tensor product over $K$ of 5.10.1 ... the upper horizontal arrow, respectively the lower horizontal arrow, of the square identifies under these isomorphisms with the tensor product over $K$ of` by `the tensor product (over $K$) of 5.10.1 ... the upper (resp. lower) horizontal arrow of (*) identifies by (2) (resp. (3)) with the tensor product (over $K$) of`. Preserve the displayed Hom factors. |
| 0147 | FR 5713 / EN 5892 | Before `It follows at once from the definition that, for $X=S$`, insert `(where $KA_X\lten_{A^e}A$ has been identified with $KA_{X,L_{\natural}}$ by means of 6.3.2, $K_X\otimes A=KA_X$).` |
| 0148 | FR 6081 / EN 6260 | `is the Gysin morphism` -> `is the ``Gysin'' morphism`. |
| 0156 | FR 6488 / EN 6644–6648 | Replace the displayed condition `$d_1^{-1}(V)=d_2^{-1}(V)$` and its surrounding grammar by `such that $(fc_1)^{-1}(V)$ is connected, and that $f$ induces ...`. |
| 0157 | FR 6596 / EN 6755 | `where the vertical arrow is the external tensor product, the upper horizontal arrow is given by` -> `where (2) is the external tensor product, (1) is given by`. |
| 0158 | FR 6600 / EN 6759 | `and the lower horizontal arrow by $\Tr_{\Lambda[G]}(-)(e)$. By descent` -> `(traces in the sense of no.~5), (3) by $\Tr_{\Lambda[G]}(-)(e)$. By descent`. |
| 0359 | FR 4332 / EN 4537 | In the first Langlands datum only, `$b$ the correspondence $\Phi$` -> `$b$ the correspondence $\phi$`. |
| 0360 | FR 4361 / EN 4568 | Replace the long topology paraphrase by `where squares (1) and (4) are cartesian.` The full source diagrams must also carry phantom labels `(1)`–`(4)`. |
| 0361 | FR 4391 / EN 4596 | `since $a_2$ is finite and the square is cartesian` -> `since $a_2$ is finite and square (1) is cartesian`. |
| 0362 | FR 4490 / EN 4697 | `On the other hand, by the Lefschetz formula ...` -> `On the other hand, by (1), $u_*=u'_*$ and $v_*=v'_*$; hence, by the Lefschetz formula ...`. |
| 0363 | FR 4494 / EN 4701 | `the conclusion follows by comparing these two equalities` -> `the conclusion follows by comparing (2) and (3)`. |
| 0377 | FR 4665 / EN 4872 | After `are each in general position (in the sense of 1.2)~(*)`, insert the exact usual-abuse footnote transcribed in the footnote table. This row and the structural footnote debt are the same operation. |
| 0382 | FR 4950 / EN 5156 | Prior wrong `\Hom_K^\bullet(E,K)` -> `\uHom_K^\bullet(E,K)`; **current after block integration**. |
| 0383 | FR 4951 / EN 5157 | Prior wrong plain `\Hom_K^\bullet` in both source/target -> underlined `\uHom_K^\bullet`; **current**. |
| 0384 | FR 4987 / EN 5193 | Remove the source-absent appended equality `=E/[A,E]`; exact line ends `E\otimes_{A^e}A`; **current**. |
| 0385 | FR 5009 / EN 5215–5217 | Formula 5.2.3 outer functors `\uRHom_A/\uRHom_B` -> `\uHom_A/\uHom_B`, inner `\uRHom_B` unchanged; **current**. |
| 0386 | FR 5015 / EN 5221 | Module situation `$({}_AE,{}_{A^\circ}F)$` -> `$(E_A,{}_AF)$`; **current**. |
| 0387 | FR 5017 / EN 5223 | `E\otimes_{A^e}F` -> `E\otimes_AF`; **current**. |
| 0388 | FR 5020 / EN 5226 | `$({}_AE,{}_AF)$` -> `$({}_AE,{}_AF_A)$`; **current**. |
| 0389 | FR 5027 / EN 5233 | `\uHom_A(E,F)\otimes_{A^e}E` -> `\uHom_A(E,F)\otimes_AE`; **current**. |
| 0390 | FR 5039 / EN 5245 | `$F\in\ob D^-(A^\circ)$`, `$\uRHom_A(E,F)\in D^-(A^\circ)$` -> `$F\in\ob D^b(A^e)$`, `$\uRHom_A(E,F)\in D^b(A^\circ)$`; **current**. |
| 0391 | FR 5035 / EN 5241 | After `$E\in D^-(A^\circ)$, $F\in D^-(A)$`, add `(resolve $E$ and $F$ by flat modules)`; **current**. |
| 0392 | FR 5054 / EN 5260 | First tensor base in the adjoint arrow `E\otimes_A\uHom_A(E,F)` -> `E\otimes_K\uHom_A(E,F)`; **current**. |
| 0393 | FR 5047 / EN 5253 | Module situation `$({}_AE,{}_AF_{A^\circ},{}_AG_A)$` -> `$({}_AE,{}_AF_A,{}_AG)$`; **current**. |
| 0394 | FR 5062 / EN 5268 | Append the exact equality before the derived form: `\Hom_A^\bullet(E,F\otimes_AG)\to\uRHom_A(E,F\otimes_AG)=\uRHom_A(E,F\lten_AG)`; **current**. |
| 0395 | FR 5066 / EN 5272 | `regarded as a right $A^\circ$-module` -> `regarded as a right $A$-module`; **current**. |
| 0396 | FR 5066 / EN 5272 | `$F=M\otimes_KA^\circ$` -> `$F=M\lten_KA$`; **current**. |
| 0397 | FR 5070 / EN 5276 | Restore the filtered degree hypotheses `$E\in D^-F(A)$, $F\in D^-F(B,A)=D^-F(B\otimes_KA^\circ)$, $G\in D^+F(B)$`; **current**. |
| 0398 | FR 5076 / EN 5282 | `\Tr_A:\uRHom_A(...)` -> source `\Tr_A=\uRHom_A(...)`; **current/source-faithful**, notwithstanding the unusual equals sign. |
| 0399 | FR 5060 / EN 5266 | `identifies with $\Hom_A^\bullet(E,F)\otimes_AG$` -> `indeed identifies with ...`; the mathematical expression is current, add `indeed` if preserving the discourse marker literally. |
| 0400 | FR 5089 / EN 5295 | `$F\in\ob DF^b(A^e)$` -> `$F\in\ob D^bF(A^e)$`; **current**. |
| 0401 | FR 5121 / EN 5327 | After `$u=\sum u_{ij}\otimes1\in\uHom_A(E,E)$`, add `$(u_{ij}\otimes1\in\uHom_A(E_i,A)\otimes_AE_j)$`; **current**. |
| 0402 | FR 5129 / EN 5335 | `$u\in\uHom_A(E,E)$ is a homomorphism of complexes` -> `$u\in\Hom_A(E,E)$ ...`; **current**. |
| 0403 | FR 5149 / EN 5355 | `$P,Q\in\ob D^b(A^e)$` -> `$P,Q\in\ob D^-(A^e)$`; **current**. |
| 0404 | FR 5133 / EN 5339 | `complexes $\Hom_A^\bullet(E,E)\to A$` -> `$\uHom_A^\bullet(E,E)\to A$`; **current**. |
| 0405 | FR 5133 / EN 5339 | `$u,v\in\uHom_A(E,E)$ are homotopic` -> `$u,v\in\Hom_A(E,E)$ are homotopic`; **current**. |
| 0406 | FR 5189 / live §5.9 opening | In the boundedness hypothesis, `$(F\lten_{A^e}B^e)\lten_BG` -> `$(F\lten_{A^e}B^e)\lten_AG`. Verify at the first paragraph of 5.9; this is the only row whose anchor lies just after the integrated block. |
| 0408 | FR 5404 / EN 5595 | `the value at $g^{-1}$ of the image of $h$ in $B_\natural$` -> `... in $B$`. |
| 0409 | FR 5502 / EN 5681 | `defined by an endomorphism of $G$` -> `defined by an endomorphism $\varphi$ of $G$`. |
| 0411 | FR 5581 / EN 5760 | Second argument `p_1^*F_1\lten_{S,A_2}F_2` -> `F_1\lten_{S,A_2}F_2`. |
| 0413 | FR 5577 / EN 5756 | After `a canonical arrow in $D^+(X)$`, insert `($D^+(X,A_2)$ when $A_2$ is commutative)`. |
| 0415 | FR 5548 / EN 5727 | `$L_2\in\Ob D^-(X_{2A}^o)$` -> `$L_2\in\Ob D^-({}_AX_2)$`. |
| 0416 | FR 5564 / EN 5743 | Replace `$D^-(Y_{BC})$, $D^-(X_{B1A})$, $D^-(X_{A2B})$, $D^-(Y_{2A}^o)$` by `$D^-({}_BY_C)$`, `$D^-({}_BX_{1A})$`, `$D^-({}_AX_{2B})$`, `$D^-({}_AY_2)$`, respectively. |
| 0417 | FR 5571 / EN 5750 | `$M_1\in D^-(Y_{B1A})$, $M_2\in D^-(Y_{A2C})$` -> `$M_1\in D^-({}_BY_{1A})$, $M_2\in D^-({}_AY_{2C})$`. |
| 0419 | FR 5691 / EN 5870 | `\Tr_A:\delta^*c_*\RHom_A(p_1^*L,p_2^!L)` -> `\Tr_A:\delta^*\RHom_A(p_1^*L,p_2^!L)`. |
| 0420 | FR 5770–5774 / EN 5949–5953 | Restore tensor bases in order: first `\lten` -> `\lten_A`, middle `\lten` -> `\lten_{\Lambda}`, last `\lten` -> `\lten_A`. |
| 0421 | FR 5787 / EN 5966 | Inner tensor `$KA_{X_1}\lten_{\Lambda}KA_{X_2}$` -> `$KA_{X_1}\lten_AKA_{X_2}$`. |
| 0424 | FR 6032 / EN 6211 | `a commutative equivariant square of $G$-$S$-schemes` -> `a commutative $G$-equivariant square of $G$-$S$-schemes`. |
| 0429 | FR 6557 / EN 6716 | In the lower-left diagram node, `p_2^!(P'\lten_{\Lambda}Q)` -> `p_2^!P'\lten_{\Lambda}Q`. |
| 0430 | FR 6574 / missing EN footnote at 6735 | In the restored footnote, use `$D_{\mathrm{ctf}}({}_{\Lambda[G]}Y)$`, not `$D^-_{\mathrm{ctf}}(...)$`. Exact English footnote is in the footnote table. |
| 0431 | FR 6585 / EN 6746 | `the square induced by the preceding square` -> `the square induced by (*)`. |
| 0432 | FR 6585 / EN 6746 | `The square then reads` -> `The square (*) then reads`. |

### Exposé V — 13 rows; Exposé VI — 1 row

These rows were already current in the live file by the time this appendix was written; the old→new mappings below are the machine-checkable promotion receipt.

| ID | FR / live EN anchor | Exact old -> new operation / live result |
|---|---|---|
| 0164 | FR 6757 / EN 6914 | `by the transition morphisms` -> `by the ``transition morphisms''`; current. |
| 0169 | FR 6931–6934 / EN 7086–7089 | Replace the separate `$T_n=0$` display and erroneous `w_n=u_{n-r}$ only “otherwise” with: `$T_n$ is the zero object for $n\ge r-1$ and $Y_{n-r}$ otherwise`, followed by `w_n=0\ (n\ge r-1),\ w_n=u_{n-r}`; current. |
| 0174 | FR 7166 / EN 7322 | `AR-isomorphic to $X'$` -> `AR-isomorphic (2.4.6) to $X'$`; current. |
| 0175 | FR 7154 / EN 7310 | `the transition morphism below` -> `the ``transition morphism'' below`; current. |
| 0179 | FR 7226 / EN 7382 | `$\widetilde X\to X$` -> `$\widetilde{\widetilde X}\to X$`; current. |
| 0180 | FR 7245–7251 / EN 7401–7406 | Convert the two displays to equation environments tagged `(a)` and `(b)`; current. |
| 0181 | FR 7296 / EN 7452 | `for every $s\ge r$` -> `for every $s>r$`; current. |
| 0182 | FR 7306–7311 / EN 7461–7469 | Restore the local enumeration `(a) If $p\ge n+1$ ...`, `(b) if $p\le n$ ...`; current. |
| 0183 | FR 7319 / EN 7475 | `the quotient filtration` -> `the ``quotient'' filtration`; current. |
| 0185 | FR 7556 / EN 7712 | `\id(J^p/J^{p+1})\otimes\varphi` -> `\id(J^p/J^{p+1})\otimes_A\varphi`; current. |
| 0186 | FR 7711 / EN 7867 | Reference `3.2.4 (ii)` -> `3.2.4 (i)`; current. |
| 0189 | FR 7919 / EN 8075 | After `method of “exact couples”`, restore `(cf., e.g., Maclane, \emph{Homology}, p.~336)`; current. |
| 0190 | FR 7959 / EN 8115 | `denoting by the letter $F$ the first filtration` -> `denoting by the letter $F$ (as in A.1) the first filtration`; current. |
| 0031 | FR 8908 / EN 9058 | `R^if_!(F)=0` -> `R^i_!f(F)=0`; current. |

### Exposé VII — 24 rows

| ID | FR / live EN anchor | Exact production operation |
|---|---|---|
| 0038 | FR 9115 / EN 9301 | `$H^*(X,p^*L)=H^*(S,Rp_*p^*(L))$` -> `$H^*(X,p^*L)\simeq H^*(S,Rp_*p^*(L))$`. |
| 0042 | FR 9387 / EN 9573 | `$Y\lten_A\mathrm{id}_L$` -> `$\gamma\lten_A\mathrm{id}_L$`. |
| 0048 | FR 9556–9558 / EN 9742–9744 | Replace the colon after `defined by an ideal $J$ of $\mathcal O_X$` by a full stop and insert `It satisfies the projection formula` before the display `u_*(x\,u^*(y))=u_*(x)y`. |
| 0052 | FR 9776 / EN 9962 | `$Y'=P_Y(N)$` -> `$Y'\simeq P_Y(N)$`. |
| 0055 | FR 9996 / EN 10182 | `and let $(p_i)_{1\le i\le m}$ be integers` -> `and let $(p_i)_{1\le i\le m}$ be $m$ integers`. |
| 0056 | FR 10100 / EN 10285 | `let $(a_i)_{1\le i\le r}$ be elements of $R$` -> `... be $r$ elements of $R$`. |
| 0197 | FR 9923 / EN 10109 | `$N=f^*\Omega^1_{X/S}$` -> `$N\simeq f^*\Omega^1_{X/S}$`. |
| 0200 | FR 10267 / EN 10449 | `\varphi^*q^*` -> `\varphi^*\circ q^*`, and `$(\pr_2)^*p^*$` -> `$(\pr_2)^*\circ p^*`. |
| 0206 | FR 10379 / EN 10561 | In Lemma 7.1.1(a) only, `$H_c^i(U,F)=0$` -> `$H^i(U,F)=0$`. Keep compact support in part (b). |
| 0219 | FR 10544 / EN 10725 | `an integer $<2n$` -> `an integer $\le2n$`. |
| 0220 | FR 10541 / EN 10722 | `$X_1,\ldots,X_r$` -> `$X_1,X_2,\ldots,X_r$`. |
| 0223 | FR 10589 / EN 10770 | `$H^2(X,\mathbb Q_\ell(1))$` -> `$H^2(X,\mathbb Z_\ell(1))$`. The later coefficient sheaf remains $\mathbb Q_\ell$ as printed unless separately sourced. |
| 0224 | FR 10589 / EN 10770 | `every integer $p<n$` -> `every integer $p\le n$`. |
| 0226 | FR 10611 / EN 10792 | `$j:X\to\mathbb P^r$` -> `$j:X\hookrightarrow\mathbb P^r$`. |
| 0227 | FR 10611 / EN 10792 | `$\alpha:Y\to X$` -> `$\alpha:Y\hookrightarrow X$`. |
| 0237 | FR 10866 / EN 11043 | First displayed identity only: `f^*f_*j_*=j_*\gamma j_*+j_*` -> `f^*f_*f^*=j_*\gamma f^*+f^*`. Leave the second identity at EN 11047 unchanged; it corresponds to FR 10870. |
| 0247 | FR 11074 / EN 11251 | `$s:Y\to\widehat N$` -> `$s:Y\hookrightarrow\widehat N$`; later `V(N)\hookrightarrow\widehat N` -> `V(N)\subset\widehat N`. |
| 0248 | FR 11102 / EN 11279 | Replace `Let $E$ be the locally free $\mathcal O_{\widehat N}$-module defined by ...` by `Denote by $E$ the locally free $\mathcal O_{\widehat N}$-module defined by ...`. The scan/French prose omits the symbol even though the immediately following exact sequence begins `0\to E`; retain $E$ in idiomatic English and record this source omission in the rejected-choice ledger. |
| 0250 | FR 11184–11189 / EN 11361 | Replace `Using ... (9.1.6), one is reduced to proving 9.4 when` by `Using ... (9.1.6), it follows that` + display `c_d(\check E)\,j_1^*(j_1)_*(y)=c_d(E)\,j_1^*(j_1)_*g_1^*(a_0);` + `in other words, one is reduced to proving 9.4 when`. |
| 0252 | FR 11203 / EN 11376 | `Substituting in this equality` -> `Substituting in (9.4.4)`. |
| 0255 | FR 11229 / EN 11402 | `since $\gamma$ is injective, $Y$ having an evident retraction` -> `since $\gamma_*$ is injective ($\gamma$ admits an evident retraction)`. |
| 0256 | FR 11233 / EN 11406 | `$p:X\times\mathbb P^1\to X$` -> `$p:X\times\mathbb P^1_k\to X$`. |
| 0259 | FR 11247 / EN 11420 | After `Let $\theta$ denote the strict transform of $T\times\mathbb P^1$ by $f_1$`, insert `, i.e. the closure of the inverse image of $T\times\mathbb P^1$ over $Z\setminus Y$`. The original scan confirms set difference; reject the French workpass transcription `$Z\doteq Y$`. |
| 0265 | FR 11419 / EN 11588 | After `by the commutativity property of blow-ups`, insert `(see, for example, Hironaka, ``Smoothing of algebraic cycles'', \emph{American Journal of Mathematics} (1968), Lemma 4.1)`. Then restore the full proof tail and diagrams as specified above. |

### Exposé VIII — 7 rows

All seven were current in the live file when this appendix was written.

| ID | FR / live EN anchor | Exact old -> new operation / live result |
|---|---|---|
| 0275 | FR 11731 / EN 11885 | `an additive graded functor` -> `an additive ``graded'' functor`; current. |
| 0280 | FR 11835 / EN 11989 | `is an epimorphism in $\cC$` -> `is an epimorphism (in $\cC$, of course)`; current. |
| 0286 | FR 11972 / EN 12126 | `the group $K'(A)$` -> `the group $K^\bullet(A)$`; current. |
| 0289 | FR 11998 / EN 12152 | First `$\gamma_A$ is neither injective nor surjective` -> `$\widetilde\gamma_A$ ...`; current. |
| 0290 | FR 11998 / EN 12152 | Second `$\gamma_A$ is therefore an isomorphism` -> `$\widetilde\gamma_A$ ...`; current. |
| 0294 | FR 12094 / EN 12248 | `Proof of Proposition 8.1` -> `Proof of Proposition 5.2`; current. |
| 0298 | FR 12163 / EN 12317 | `the following identity, the ``projection formula'':` -> `the following identity (``the projection formula''):`; current. |

This appendix contains exactly 136 NEED IDs: 34 (III) + 57 (III B) + 13 (V) + 1 (VI) + 24 (VII) + 7 (VIII). Rows marked current were closed by production that landed after the original receipt classification; they remain in the appendix so the promotion ledger records the exact source correction and does not silently lose provenance.
