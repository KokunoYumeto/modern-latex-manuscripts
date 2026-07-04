# SGA5 audit findings — every change, with source evidence

Format per entry: source page · TeX line · level · what the source shows · what the file had ·
action. "level" = prose / equation / symbol / diagram / label.

---

## ★ COMPLETION SUMMARY (2026-06-25)

**Full page-by-page audit COMPLETE — all 484 printed pages of SGA 5 audited against the scan; `sga5_fr_workpass.tex` compiles 307pp/0err.** ~300+ verified fixes; full edit record in `_work/swarm_results/workpass_vs_repair032.diff` (366 changed hunks vs the repair032 base). Method + lessons: `SGA5_AUDIT_METHOD_WRITEUP.md`.

Coverage: manual pass pp.1–5 (logbook entries below) + verify-gated workflow for the bulk (main body p75–484 prior sessions; Exposé I p1–74 finished 2026-06-25). Workflow-era fixes carry per-fix source evidence in `_work/patches_p*.json` and the workflow task outputs, rather than being re-logged page-by-page below.

Exposé I (p1–74), 2026-06-25: p1-2 clean; p3-32 = 14 fixes; p33-62 = 22 fixes (incl. 12 `SGA→SGAA` cross-refs, two Tate-twist signs `⊗d→⊗-d`, the spurious `⊗^L i_?`→`L i_?` functor name ×4); p63-74 = 7 fixes (sheaf-Hom/Ext underlines, a stray stalk subscript on `R i_*(G)`, xref `I 3.5.1→3.3.1`). p346-347: two dropped diagrams (cartesian + commutative, §9.8) reconstructed from the scan and restored, plus dropped connective prose and `v_*→v''_*`.

Deferred items closed: p344 already correct; p199/p201 left as editor paraphrase (improvement, not reverted); p188 (one dropped pair of parens around the §5 Hochschild parenthetical `A⊗^L_{A^e}A`) left as an optional ultra-fidelity item.

---

## Source p103 — Exposé III, diagram (4.4.2) [the big 3×4 Künneth–Lefschetz grid]

- **diagram/symbol — 7 spurious tensor subscripts.** Source draws every derived tensor as a
  bare `⊗` with `L` above and **nothing below**. The file had added base subscripts:
  `⊗_X` (3×) and `⊗_Y` (4×). Removed all 7 → bare `⊗^{\mathbf L}`.
  TeX lines 2966, 2968, 2971, 2973, 2975, 2978, 2980 (work copy).
- **diagram/equation — top-left node regrouped.** Source node (1,1) is
  `(f_*c'_*c'^!P) ⊗^L (f_*c''_*c''^!Q)` — push applied to each factor (consistent with arrow (8)
  being "produit tensoriel des flèches 3.7.3"). The file had `f_*(c'_*c'^!P ⊗_X^L c''_*c''^!Q)` —
  push pulled outside the whole tensor, which is a different object. Restored the factored form.
  TeX line 2966.
- ACTION: fixed in work copy. Source basis: 400 dpi crop of scan p103 (`_work` renders).
- STILL OPEN nearby (not yet done): full all-levels audit of source pp.102–104 prose/other
  diagrams (4.4.1, 4.4.3, 4.4.4, 4.4.5, the (A) grid) — only (4.4.2) was touched here.

---

## Source p1 — Exposé I (Complexes dualisants), title + Introduction
- prose: CLEAN. Title, author/rédaction, intro paragraphs 1–3 match the source verbatim
  (incl. "SGA 4^{1/2} Th. finitude 4.3"). TeX lines 306–319. No change.

## Source p2 — Exposé I, Introduction (cont.) + footnote
- prose: §3/§4/§5 intro paragraphs and footnote (1) match. TeX 321–325.
- **symbol — local-duality pairing flattened (FIXED).** Source writes the perfect pairing
  between `\underline{H}^i(F')_x` (cohomology sheaf of the dual F', then **stalk at x** — x
  *after* the parenthesis) and `\underline{H}^{-i}_x(F)` (**local cohomology** with support x —
  x *before*). The file had both as `\underline{\H}^i_x(...)`, i.e. it turned the first term
  (a stalk) into a local-cohomology group, erasing the asymmetry that *is* local duality.
  Fixed first term → `\underline{\H}^i(F')_x`. TeX line 323. Verified on 400 dpi crop of scan p2.
  NOTE: this is a prose/symbol error — invisible to every prior (diagram-only) pass.

## Source p3 — Exposé I, §1 (Déf 1.1, Rem 1.2 a/b)
- CLEAN. All three chunks match verbatim (incl. the suite exacte (*), Ext formulas, F_ℓ, [X'':X'] div by ℓ).

## Source p4 — Exposé I, §1 (Prop 1.3 + proof, into Déf 1.4 / Prop 1.5)
- **symbol — wrong letter in the dévissage (FIXED).** In the proof of 1.3 (i)⇒(ii), the source reads
  "récurrence sur le nombre d'indices i tels que **I^i ≠ 0**" (the injective complex I's nonzero
  degrees — confirmed by the next clause "I est réduit au degré 0", and it's the correct math:
  the dévissage reduces I to one degree). The file had `\H^i ≠ 0` (cohomology H) — wrong letter,
  wrong object. Fixed → `I^i`. TeX line 357. Verified on 600 dpi zoom of scan p4 (glyph is a
  clean capital I, no H-crossbar).
- rest of p4 top/mid (Prop 1.3 statement (i)(ii)(iii), spectral sequence E_2^{pq}) matches.

- p4 bot (E_2^{0i} iso, (ii)⇒(iii), start of (iii)⇒(i)) matches. p4 otherwise CLEAN.

## Source p5 — Exposé I, §1 (end of 1.3 proof, Rem 1.3.1, Déf 1.4, Prop 1.5 stmt)
- CLEAN. All three chunks match: 1.3 (iii)⇒(i) finish, Rem 1.3.1, Déf 1.4 (dim.q.inj),
  the RHom functor remark, Prop 1.5 statement (cd_n(X)≤N ⟹ …), into "On utilisera … le [Lemme 1.5.1]".

## Source p6 — Exposé I, §1 (Lemme 1.5.1 + proof, Preuve de Prop 1.5)
- CLEAN. All chunks match (Lemme 1.5.1 (i)/(ii), the Tohoku ref, Preuve de 1.5 with the spectral
  sequence E_2^{pq}=H^p(X;Ext^q(F,K))⟹Ext^*(X;F,K), cd_n(X)≤N argument). Short page (ends ~40% down).

## Source p7 — Exposé I, §1 (Rem 1.5.2, Prop 1.6 + proof, start of bidualité)
- CLEAN. Rem 1.5.2, Prop 1.6 (dim.q.inj(R^!f(K))≤N), Main-theorem factorisation proof,
  duality iso f_*Ext^i(F,R^!f(K))→Ext^i(f_*F,K), bidualité construction intro — all match.

## Source p8 — Exposé I, §1 (bidualité, Déf 1.7, Rem 1.8 a/b)
- CLEAN. Canonical homomorphism F→D_K D_K F, the "localement noethériens" bold note, Déf 1.7
  (i)(ii)(iii), Rem 1.8 a)/b) (ii bis) — all match. Short page.

## Source p9 — Exposé I, §1 (Rem 1.8 c/d/e, formules d'échange, tor-dimension)
- CLEAN. Equivalences (D_c(X))°≈D_c(X) etc., "On ignore si…", tor-dimension paragraph,
  footnote (*) "Voir aussi (SGA 6 I 5)" — all match. Short page.

## Source p10 — Exposé I, §1 (Lemme 1.9 + proof, Notation 1.10, Prop 1.11 a)
- **symbol — spurious minus in Lemme 1.9 a) hypothesis (FIXED).** Source: "Soient X un préschéma,
  F ∈ ob D_c(X), G ∈ ob D_c^-(X)". The file had F ∈ ob **D_c^-(X)** in the hypothesis. The minus is
  wrong: the conclusion is "F⊗^L G ∈ D_c(X) **si F ∈ D_c^-(X)** ou si G de tor-dim finie", so the
  hypothesis on F must be the general D_c(X) or that sufficient condition is vacuous. Verified on
  600 dpi zoom (the conclusion D_c(X) and the condition D_c^-(X) are both visible; the hypothesis F
  carries no minus). Fixed first occurrence only (G keeps its minus). TeX line 459.
- rest of p10 (Lemme 1.9 proof, spectral seq, Notation 1.10, Prop 1.11 a) matches.

## Source p11 — Exposé I, §1 (Prop 1.11 b/c/d + proof a/b/c)
- CLEAN. b) torf⟹qinjf implication, c) dualisant iso D_K(F⊗^L D_K(G))→RHom(F,G), d) equivalences,
  proof a)/b)/c) — all match. Short page.

## Source p12 — Exposé I, §1 (Prop 1.11 proof d, Rem 1.11.1, Prop 1.12 stmt + a(i))
- **math/symbol — wrong functor in Prop 1.12 a)(i) (FIXED).** The duality iso reads, in the source,
  `R f_* D_X(F) →~ D_Y R_!f(F)` (the manuscript writes f_! as "R_!f" — the SHRIEK). The file had
  `D_Y R f_*(F)` (STAR) on the right, which made a)(i) identical to a)(ii) — impossible. Verdier
  duality / SGAA XVIII 3.1.9.6 (cited in the proof, TeX 534) gives R f_* D_X ≅ D_Y R f_!. Fixed the
  right side *→! → `\underline{D}_Y \R f_{!}(F)` (kept the TeX's \R f_! notation; a)(ii) correctly
  keeps \R f_*). TeX line 517. Confirmed on 600 dpi zoom of scan p12 (i) — shriek clearly visible.
- rest of p12 (Prop 1.11 d proof, Rem 1.11.1 a/b, Prop 1.12 statement) matches. Short page.

## METHODOLOGY REFINEMENT (learned p13-15) — two kinds of discrepancy
1. **Transcription error**: TeX ≠ source AND source is right → fix TeX to match source (e.g. p12, p13).
2. **Source error**: the source itself is wrong/imprecise → produce the CORRECT, source-faithful reading,
   do NOT silently reproduce the slip; LOG it as a source erratum / emendation. Sub-cases seen:
   - source TYPO that the TeX already fixed → KEEP the TeX's correct reading, log "emendation kept" (p15).
   - source IMPRECISION the TeX faithfully copied → leave TeX as-is (faithful), log erratum for a future
     editorial footnote; do NOT "fix" it away (p14 Cor 1.13).
   Rule of thumb: the edition should be mathematically correct AND document every departure from the scan.

## Source p13 — Exposé I, §1 (Prop 1.12 a(ii)/b, Preuve, Scholie, footnotes)
- **symbol — wrong functor in a)(ii) finitude step (FIXED).** Proof of a)(ii) cites the finitude th.
  "qui assure que **R_!f(D_X(F)) ∈ D_c(Y)**" (SHRIEK — f finite type, so Rf_! preserves D_c; and the
  derivation needs Rf_!(D_X F)). The file had `R f_*` (star). Fixed → `\R f_{!}`. TeX line 536.
  Verified on 600 dpi zoom (R_!f shriek clearly visible).
- a)(ii)/b)(i)/b)(ii) duality isos, Scholie (R f_* ↔ R_!f exchange), footnotes (1)(2) all match.
  [This page also CONFIRMS the p12 a)(i)=shriek fix: a)(ii) LHS is R_!f, RHS R f_*, the proper Verdier pair.]

## Source p14 — Exposé I, §1 (Scholie end, Cor 1.13 + proof, Lemme 1.14 a)
- **SOURCE ERRATUM (no TeX change) — Cor 1.13 proof chain.** Source prints the chain
  `R f_* F ≅ R f_* D_X D_X F ≅ D_Y R f_* D_X F (par a)(i)) ≅ D_Y D_Y R f_* F (par a)(i))` — i.e. STAR
  intermediate and BOTH steps cited as a)(i). Mathematically (given a)(i)=R f_* D_X≅D_Y R f_!,
  a)(ii)=R f_! D_X≅D_Y R f_*), the intermediate should be `D_Y R f_! D_X F` and the 2nd step should
  cite a)(ii). The TeX faithfully reproduces the source's loose version, so NO transcription fix;
  flagged for a future editorial footnote. (Same loose "double application de a)(i)" recurs in the
  f-fini case lower on the page — same erratum.)
- **prose (FIXED).** "ce qui démontre la première assertion" → source reads "démontre**(ra)**" (author's
  future-tense parenthetical); restored. TeX line 555.

## Source p15 — Exposé I, §1 (Lemme 1.14 b + proof, Cor 1.15 stmt)
- **EMENDATION KEPT (no TeX change) — Lemme 1.14 b).** Source prints `f_*F ∈ ob D_c(F)` — a typo, since
  f_*F lives on Y. The TeX already has the correct `D_c(Y)`. Kept the TeX's correct reading (did NOT
  reintroduce the source typo). Verified source = "D_c(F)" on 600 dpi zoom.
- Lemme 1.14 b) proof (the (Y_i) decomposition, u_i radiciel / v_i étale, change-of-base), Cor 1.15
  statement — all match.

## Source p16 — Exposé I (Cor 1.15 proof end, §2 intro, Théorème 2.1 stmt)
- **EMENDATION KEPT (no TeX change).** Cor 1.15 proof opens "On sait déjà **(1.5)**" in the source —
  a typo: the cited result (q-injective dim preserved by R^!f) is **Prop 1.6**, not 1.5 (1.5 is q-inj vs
  inj dim, nothing about R^!f). The TeX already has the correct **(1.6)**; kept. Verified source="(1.5)"
  on 600 dpi zoom.
- **source cross-ref note (no change).** Théorème 2.1 cites "(1.6)" for "complexe dualisant" (defined
  in Déf **1.7**). Both source AND TeX print (1.6), so TeX is faithful; flagged as a probable source
  cross-ref slip for a future editorial footnote. No change.
- Cor 1.15 proof body (f=f'i factorisation, f-fini case, D_Y f_*(F)≅f_* D_X(F) by 1.12 a)(i) — correct
  since f finite ⇒ f_*=f_!), §2 intro (A=Z/ℓ^ν Z), Théorème 2.1 statement (K'≅K⊗^L L[r]) — all match.

## Source p17 — Exposé I, Théorème 2.1 proof (start)
- **math — L^∨[-r] error CLUSTER (3 FIXED).** In the proof, the source consistently writes plain
  **L[r]** where the TeX wrongly had **L^∨[-r]** (or L^∨[r]). Correct math: D'F = RHom(F, K⊗L[r]) ≅
  RHom(F,K)⊗L[r] = DF⊗L[r] for invertible L (the transcriber grabbed the L^∨[-r] from the *left* side
  of the (*) isomorphism instead of the L[r] result). Fixed:
  - TeX 599 `D'F ≅ DF ⊗^L L^∨[-r]` → `… ⊗^L L[r]`.
  - TeX 601 `D'K ≅ L^∨[-r]` → `D'K ≅ L[r]`.
  - TeX 603 "ce qui montre que `L^∨[r]`" → "`L[r]`".
  All three verified against 600 dpi source zoom (plain L[r], no vee, no minus) + the mathematics.
- (*) three RHom isos, P = D'K = RHom(K,K'), goals a)/b), (**) F⊗^L P ≅ D'DF — all match.

---

## Source p18 — Exposé I, Théorème 2.1 proof end + Lemme 2.2 (stmt + proof start)
- **EMENDATION KEPT (no TeX change).** Source prints `H^{-i(x)}(P_x̄) ≅ A_x̄` — a typo: the exponent
  should be `-r(x)` (the index is `r(x)`, the local cohomological amplitude, not the running index `i`).
  The TeX already has the correct `\H^{-r(x)}`. Kept the TeX's correct reading. Read at chunk res
  (clear enough: superscript reads "-i(x)").
- Th. 2.1 proof end (K⊗^L P ≅ D'DK ≅ D'A_X = K'; P'⊗^L P = D'DDD'A_X ≅ A_X), Lemme 2.2 stmt
  (`P ≅ L[r], P' ≅ L^∨[-r]` — matches source), two-step proof, "2) Cas général" r(x) argument — all match.

## Source p19 — Exposé I, Lemme 2.2 proof (specialization square + r-locally-constant)
- Specialization commutative square **(*)** at TeX 647–652 checked node-by-node: TL `L_ȳ⊗L'_ȳ`
  →(~) `A_ȳ`; left vertical `u^*⊗u'^*`; right vertical (unlabeled); BL `L_x̄⊗L'_x̄` →(~) `A_x̄`.
  All nodes, both iso-tildes, and arrow directions match. No drop.
- `H^{-r_0}(P)=L`, `H^{r_0}(P')=L'`; base/dual-base e,e' argument; `λλ'=1`; `P ≅ L[-r_0]`,
  `P' ≅ L^∨[+r_0]` (matches source — consistent with their shift convention) — all match. CLEAN.

## Source p20 — Exposé I, Lemme 2.2 proof end (contradiction argument)
- Suite exacte **(**)** `0 → i_!(P|U) → P → j_*j^*P → 0`; splitting `P ≅ i_!(P|U) + j_*j^*P`;
  the `P⊗^L P'` chain → `i_!(A_U) + j_*(A_x)` (absurde) — all match. CLEAN.

## Source p21 — Exposé I §3 head, §3.1 Préliminaires, 3.1.1 Lieu singulier
- §3 title, §3.1, intro paras, 3.1.1 condition (reg) (i)/(ii), EGA citations — all match. CLEAN.

## Source p22 — Exposé I, 3.1.2 Dévissage de faisceaux constructibles
- 3.1.2 stmt, conditions (i)/(ii)/(iii) (`f_*i_!(A'_U)`, `A'=Z/ℓZ`), (ii bis)/(iii bis), affine
  remark, Preuve, 3.1.3 head — all match. CLEAN.

## Source p23 — Exposé I, 3.1.3 Dimension cohomologique + 3.1.4 Pureté
- (cdloc)_n condition + displayed `cd_n(Ỹ(ȳ)−V(f)) ≤ dim O_{Y,ȳ}`; 3.1.4 absolute-purity
  condition `H^i_Y(A_X)=0 (i≠2d)` and the fundamental-class iso `A_Y → H^{2d}_Y((μ_n)^{⊗d}_X)`;
  footnote (*) (G. Ofer) — all match. CLEAN.

## Source p24 — Exposé I, 3.1.5 Résolution des singularités à la Hironaka
- **symbol — spurious `^*` on Γ (FIXED).** TeX 741 had `d'éléments de $\Gamma^{*}(X;\cO_X)$`; the
  source reads plain `Γ(X;O_X)` (no star) — verified at 500 dpi zoom, the Γ glyph carries no
  superscript. On a regular X the f_i are automatically nonzerodivisors where (f_i)_x ∈ m_x, so the
  source's plain Γ is mathematically valid; the TeX had silently added a star. Fixed `\Gamma^{*}` → `\Gamma`.
- 3.1.5 a) (strictement à croisements normaux, `D=Σ div(f_i)`), b) fortement désingularisable +
  cases a)/b)/c), both footnotes (Hironaka/Bennett) — all match.

## Source p25 — Exposé I, 3.1.6 Finitude cohomologique + §3.2, Prop 3.2.1 stmt
- 3.1.6 (`R f_*(F) ∈ D_c^+(Y)`, cases a)/b)(i)(ii)(iii)); §3.2 head; Prop 3.2.1 stmt + formula
  `(*) Ext^i(F,A_X)_x = 0 pour i > 2 dim O_{X,x}`; Preuve start — all match. CLEAN.

## Source p26 — Exposé I, Prop 3.2.1 proof (math-dense) + Rem 3.2.2 start
- **symbol — fibre-product base `×_Z` vs source `×_X` (FIXED to source).** TeX 784 had
  `$\wt{Y} = \wt{Z} \times_Z Y$`; the source reads `Ỹ = Z̃ ×_X Y` (subscript X, verified at 600 dpi).
  These are mathematically EQUAL here — since Y ⊆ Z, `Z ×_X Y = Y`, hence `Z̃ ×_X Y = Z̃ ×_Z Y =
  Z̃ − V(f̃)` — so the source's `×_X` is correct; the TeX had silently changed it to the more
  "natural" `×_Z`. Reverted to source: `\times_Z` → `\times_X` (faithfulness fix, not a math fix).
- Everything else on this dense page matches: projection formula `R Hom(i_!G,A_X) ≅ Ri_* R Hom(G,R^!i A_X)`;
  purity `R^!i(A_X) ≅ (μ_n)^{⊗d}_Y[-2d]`; `Ext^p(G,T)_ȳ ≅ Ext^p(G_ȳ,T_ȳ)`, T_ȳ injectif;
  `R Hom(F,A_X) ≅ Ri_*(H)[-2d]`; Z = adhérence schématique, the localized-strict computation,
  `Ext^q(F,A_X)_x̄ ≅ H^{q-2d}(Ỹ,H̃)`, the codim/dim relations → `Ext^q = 0 for q > 2 dim O_{X,x}`, cqfd.
  (Note: source leaves the SGAA XVIII projection-formula reference number blank; TeX faithfully has just "(SGAA XVIII)".)

## Source p27 — Exposé I, Rem 3.2.2 end, Cor 3.2.3, Lemme 3.2.4 (stmt + proof start)
- Rem 3.2.2 `Ext^{2d}(A_U,A_X)|U = (μ_n)^{⊗d}_U`; Cor 3.2.3 + `dim.q.inj(A_X) ≤ 2d` + proof;
  Lemme 3.2.4 (`dim.inj(A_X) ≤ 2d+N`, and `≤ N` under the codim/cd_n hypothesis) + proof start
  (`Ext^i(X;F,A_X)=0 for i>N`, suite spectrale) — all match. CLEAN.

---

## Source p28 — Exposé I, Lemme 3.2.4 proof end, Cor 3.2.5, §3.3 head, Prop 3.3.1 a) start
- E_2 spectral sequence `E_2^{pq}=H^p(X;Ext^q(F,A_X)) ⟹ Ext^*(X;F,A_X)`, concentration argument;
  Cor 3.2.5 (`dim.inj(A_X)=2d`) + proof (`Ext^{2d}(X,A_x,A_X)=H^{2d}_x(A_X) ≅ (μ_n)^{⊗d}(k)≠0`);
  §3.3 head; Prop 3.3.1 a) conditions (i)/(i bis)/(ii) — all match. CLEAN.

## Source p29 — Exposé I, Prop 3.3.1 a) (ii bis/ter/iii), b), Preuve start
- conditions (ii bis)/(ii ter)/(iii) (`R^!f(F)∈D_c^+(Y)` shriek correct), b) (i)/(ii); Preuve:
  (i bis)⟹(ii) duality `Ri_*(F) ≅ R Hom(i_!(A_U),F̄)` (both `i^!` shrieks correct), (ii)⟹(ii bis),
  (ii bis)⟹(i bis) start — all match. CLEAN.

## Source p30 — Exposé I, Prop 3.3.1 proof (projection formula, distinguished triangle)
- **source erratum FLAGGED (no TeX change).** At the "cqfd" the source writes `R Hom(M,Ri^!(G)) ∈ D_c^+(X)`,
  but the goal stated 3 lines up (TeX 860) and the math call for `D_c^+(Y)` (the complex `R Hom(M,Ri^!(G))`
  lives on Y; M and Ri^!(G) are both on Y). Either a source typo (X for Y) or loose `i_*`-shorthand
  (i closed ⇒ i_* reflects constructibility). TeX faithfully copies the source's `X`; flagged for a future
  editorial footnote, NO change (same handling as the p16 source cross-ref slip).
- Distinguished triangle (TeX 868–871) checked node-by-node: top `R Hom(A_{U,X},G)` [dl]→ BL `R Hom(A_Y,G)`
  [rr]→ BR `R Hom(A_X,G)` [ul]→ top. All nodes/arrows match. Projection formula, the
  `0→A_{U,X}→A_X→A_Y→0` sequence, `R Hom(A_X,G)=G`, `R Hom(A_{U,X},G)≅Rj_*j^!(G)`,
  `R Hom(A_Y,G)≅i_*Ri^!(G)` — all match.

## Source p31 — Exposé I, Prop 3.3.1 proof end (mapping-cylinder triangle, récurrence)
- Mapping-cylinder triangle (TeX 879–882) checked: top `Ri_*(M)` [dl,(+1)]→ BL `Ri_*(F)` [rr]→
  BR `Ri_*Rj_*j^*(F)` [ul]→ top. The `(+1)` label and all arrows match. `Ri_*Rj_*j^*(F)≅R(ij)_*j^*(F)`,
  `Rj_*j^*(F)≅i^*R(ij)_*j^*(F)`, the récurrence on `U∩Z̄→Z̄`, (i)–(ii ter)⇔(iii) by 1.14, b)(i)/(ii) — all match. CLEAN.

## Source p32 — Exposé I, §3.4 bidualité, Théorème 3.4.1 + Démonstration start
- §3.4 head, Th. 3.4.1 stmt ([H] V 2.2; X reg, fortement désing., reg/cdloc_n, pureté ⇒ A_X dualisant);
  Démonstration: `F→D_X D_X F`, `D_X=R Hom(_,A_X)`, dévissage to `F=f_*i_!(A'_U)`, change-of-base
  `i_!(A'_U)≅Rh_*i'_!(A'_{U'})`, `f_*i_!(A'_U)≅Rg_*i'_!(A'_{U'})` (g=fh) — all match. CLEAN.

## Source p33 — Exposé I, Démonstration 3.4.1 end + Lemme 3.4.2 (stmt + proof a) p=1, b) p≥2 start)
- `(i'_!(A'_{U'}),R^!g(A_X))` bidualisant, `R^!g(A_X)` loc. iso to `A_{Y'}`; Lemme 3.4.2 stmt
  (`(A'_{U,X},A_X)` bidualisant); proof a) p=1 purity `R^!i(A_X)≅(μ_n)^{⊗1}_Y[-2]`, Pontryagin;
  b) p≥2 sequences `0→A'_{(Y-Y'),X}→A'_Y→A'_{Y'}→0` and `0→A'_{(Y-Y'),X}→A'_{Y_p}→A'_{Y_p∩Y'}→0` — all match. CLEAN.

## Source p34 — Exposé I, Lemme 3.4.2 proof end, Cor 3.4.3 + proof, Cor 3.4.4 stmt
- **math — wrong dualizing sheaf `A_X`→`A_{Y_p}` (FIXED).** TeX 931 read "ramené à vérifier la bidualité
  pour `(A'_{Y_p∩Y'}, A_X)` sur Y_p"; the source has `A_{Y_p}` (verified 600 dpi). Working *on Y_p*
  (via 1.11+purity) the dualizing sheaf is `A_{Y_p}`; `A_X` doesn't even live on Y_p. Fixed `A_X`→`A_{Y_p}`.
  (The two earlier pairs in the same sentence, both on X, correctly keep `A_X` — only the "sur Y_p" pair was wrong.)
- **EMENDATION KEPT.** Cor 3.4.3 proof: source reads `R^!f'(A_S)` loc. iso to `A_X` (verified 650 dpi),
  a typo — `R^!f'(A_S)` lives on X' (source of the smooth f'), so it's `A_{X'}`. TeX already correct (`A_{X'}`), kept.
- **EMENDATION KEPT.** Cor 3.4.3 last line: source reads "vérifie les conditions `(ii) et (ii)` de (1.7)"
  (verified 650 dpi) — typo; proof verifies (ii) and (iii). TeX already correct (`(ii) et (iii)`), kept.
- (Cor 3.4.4 proof on p35 uses `A_X[2d]` correctly — there f is reduced to lisse on X, so A_X is right.)

## Source p35 — Exposé I, Cor 3.4.4 proof, Rem 3.4.5, §4 Dualité locale, §4.1
- Cor 3.4.4 proof (`f^!(A_S)≅A_X[2d]` localement, by 3.4.1); Rem 3.4.5; §4 intro; §4.1 normalisation
  (`K_{\{x\}}=R^!i(K_X)≅A[r]`, normalisé en x ⇔ r=0 + iso `K_{\{x\}}≅A`) — all match. CLEAN.

## Source p36 — Exposé I, §4.1 example, §4.2 (formule d'induction + duality pairings)
- **symbol — dropped base subscript `μ_n^{⊗d}`→`(μ_n)_X^{⊗d}` in (4.2.2)''' (FIXED).** TeX 986 had
  `\mu_n^{\otimes d}`; the source reads `(μ_n)_X^{⊗d}` with explicit X base subscript (verified 700 dpi),
  matching the document's convention everywhere else (e.g. `(μ_n)_X^{⊗d}[2d]` on this same page). Restored `_X`.
- §4.1 example (`(μ_n)_X^{⊗d}[2d]` normalisé), §4.2: (4.2.1) `i^*D_X(F)≅D_Y R^!i(F)`, (4.2.2)
  `D_X(F)_x≅Hom^*(R^!i(F),A)`, (4.2.2)' `D_X(F)_x×RΓ_x(F)→A`, (4.2.2)'' `H^i(D_X(F))_x×H^{-i}_x(F)→A` — all match.
  (Source writes "dans (D(A))"; TeX `\D(A)` — extra paren ambiguous at native res, immaterial, treated faithful.)

## Source p37 — Exposé I, Exercice 4.2.3 (local duality), §4.3 start
- Exercice 4.2.3: `⊗i_? : D^b(A)→D^-(X)`, `⊗i_?(M)=M⊗^L_A K`; (*) `R Hom(L,⊗i_?(M))≅R Hom(R^!i(L),M)`;
  trace hint; dualité locale `RΓ_x(L)×R Hom(L,K)→A` and `H^i_x(L)×Ext^{-i}(L,K)→A`; §4.3 head — all match. CLEAN.

---
## SYSTEMATIC — "SGA" vs "SGAA" citation A-drop (flagged for a dedicated pass; NOT bulk-fixed)
The document cites SGA 4 (étale cohomology) as **"SGAA"** throughout (verified on early pages and again
on p38: source reads "SGAA IX 2.7", "SGAA VI I 3.7", "SGAA XVII", "SGAA VII 5.11"). From ~§4.3 (TeX ~1019)
onward the transcription frequently drops an A → **"SGA"** (e.g. TeX 1019/1027/1034/1044/1048/1056 etc.).
Counts in workpass.tex: **55 `SGA~` vs 36 `SGAA~`**. BUT `SGA~` is a MIX: many are legitimate volume refs
(`SGA~$4^{1/2}$`, SGA 1/6/7, the SGA5 self-title, the preamble at TeX 55/77/315…), so a blind global
replace would corrupt them. Resolution requires per-instance classification (SGA4-exposé ref → `SGAA`;
genuine volume ref → keep `SGA`). DEFERRED to a dedicated citation-consistency pass so the page-by-page
math audit keeps moving; recorded here so it is not lost. (Math unaffected — citation labels only.)

---

## Source p38 — Exposé I, §4.3 Lemme 4.3 + proof (cartesian square)
- Lemme 4.3 stmt (`f^*R Hom(F,G) ≅ R Hom(f^*F,f^*G)` for localisé strict), proof: carré cartésien
  (U←g←U' / i,i' down / X←f←X') checked node-by-node — matches; dualité isos `R Hom(F,G)←R i_*i^*G`,
  `R Hom(f^*F,f^*G)←R i'_*g^*i^*G`; base-change `f^*Ri_*i^*(G)→Ri'_*g^*i^*(G)` — all match.
  (SGA→SGAA citation slips present, see SYSTEMATIC above; deferred.)

## Source p39 — Exposé I, Lemme 4.3 proof end, Lemme 4.4, §4.5 start
- Lemme 4.4 (K dualisant ⇔ f^*K dualisant for all localisé strict) + proof; §4.5 start;
  (4.5.1) `RΓ_x̄ = g^*R^!i` — all match. CLEAN (modulo deferred SGAA).

## Source p40 — Exposé I, §4.5 (4.5.2, K_X setup, (4.5.3))
- (4.5.2) `RΓ_x̄ ≅ R^!i' f^*`; K_Y=R^!j(K_X), K_X'=f^*K_X, K_x̄=RΓ_x̄(K_X), K_x̄≅A[d]; normalisé en x̄;
  the `(D_X F)_x̄ ≅ g^*i^*D_X F ≅ g^*D_Y R^!iF ≅ D_x̄ g^*R^!i(F)` chain (4.5.3) — all match. CLEAN.

## Source p41 — Exposé I, §4.5 (pairings 4.5.3'/4.5.3'', Inversement, bidualité) — TWO FIXES
- **math — (4.5.3)' wrong formula (FIXED).** TeX 1108 had `\H_Y^i(F)_{\ol{x}}\times \R^{-i}\Gamma_{\ol{x}}(F)→A`;
  the source reads `D_X(F)_{\ol{x}}\times \R\Gamma_{\ol{x}}(F)→A` (verified 650 dpi). The text says (4.5.3)'
  "généralise (4.2.2)'", and (4.2.2)' = `D_X(F)_x × RΓ_x(F) → A` (complex-level pairing) — so the source is
  right and the TeX had an unrelated/corrupted LHS. Fixed to `\underline{D}_X(F)_{\ol{x}}\times\R\Gamma_{\ol{x}}(F)`.
- **math — circular bidualité step (FIXED).** TeX 1128 ended the stalk chain with `D_{\ol{x}}D_{\ol{x}}(F)_{\ol{x}}`,
  but `(F)_{\ol{x}}=F_{\ol{x}}` makes that equal to step 1's RHS `D_{\ol{x}}D_{\ol{x}}(F_{\ol{x}})` — circular,
  proving nothing. The conclusion must be `(D_X D_X F)_{\ol{x}}`; source reads `D_X D_X(F)_{\ol{x}}` (verified 650 dpi).
  Fixed `\underline{D}_{\ol{x}}\underline{D}_{\ol{x}}(F)_{\ol{x}}` → `\underline{D}_X\underline{D}_X(F)_{\ol{x}}`.
- (4.5.3)'' `H^i(D_X(F))_x̄ × H^{-i}_x̄(F) → A` matches. 
- **label note (no change):** the inversement flèche is labelled `(4.5.3)` in the source but `(4.5.3)^{bis}`
  in the TeX (since `(4.5.3)` is already used at TeX 1098); the TeX's disambiguation is consistent (also at
  Prop 4.5.4) and helpful — kept, departure noted.

## Source p42 — Exposé I, §4.5 (Prop 4.5.4, Rem 4.5.5, Exercice 4.5.6)
- Prop 4.5.4, Rem 4.5.5 (dualité globale `D_Y R_!f(F) ≅ R f_* D_X(F)`), Exercice 4.5.6 (conservative family
  `H^i_x̄ : D_c^b(X) → A-modules`) — all match. CLEAN.

## Source p43 — Exposé I, §4.6 (the (4.6.1) iso chain) — ONE FLAGGED
- §4.6 setup, factorisation `x̄ →i' {x̄} →i'' Y`, (4.6.1) `R^!j(F)_x̄ ≅ D_x̄ RΓ_x̄ j^*D_X(F)` — match.
- **FLAGGED, UNRESOLVED (no change):** the "induction ordinaire (1.12 b)(i)" step (TeX 1167) is ambiguous
  at 650 dpi. Math expects `i'^* D_{\{x̄\}} i''^* R^!j(F)` (dualizing on the *closure* {x̄}); the TeX has
  `i'^* D_{\ol{x}} i''^* R^!j(F)`; the source glyphs read approximately `i''^* D_X i''^* R^!j(F)`. None of the
  three cleanly agree and the D-subscript ({x̄} vs x̄ vs X) and first operator can't be resolved at native
  resolution. Left as-is per "flag, don't guess"; revisit if a higher-res source ever appears.

## Source p44 — Exposé I, §4.6 end (4.6.1'/4.6.1''), Exemple 4.6.2, §4.7 start
- (4.6.1)' `R^!j(F)_x̄ × RΓ_x̄ j^*D_X(F) → A`, (4.6.1)'' `H^i_Y(F)_x̄ × H^{-i}_x̄(D_X(F)|Y) → A`; Exemple 4.6.2
  (`K_X=(μ_n)_X^{⊗d}[2d]`, pairing `H^i_Y(F)_x̄ × H^{2d-i}_x̄(F'|Y) → A`, `F'=R Hom(F,(μ_n)_X^{⊗d})`);
  §4.7 setup (`U→V→X`, K_V/K_U/K_Y), (4.7.1) `RΓ(U,G)×RΓ(V,i_!G')[-1]→A` — all match.
- **EMENDATION KEPT:** source reads "fermé Y contenant **X**" (Exemple 4.6.2) — a typo (Y contains the *point* x,
  not all of X; Y⊇X would force Y=X). TeX already correct with lowercase `x`. Kept.

---

## Source p45 — Exposé I, §4.7 (the (4.7.1)' construction, (4.7.2)–(4.7.8))
- (4.7.1)' `RΓ(U,G)⊗^L_A RΓ(V,i_!G')[-1]→A`; tensor-product caveat (A=Z/ℓZ inf. coh. dim.) + footnote (*)(ajouté
  en 77); (4.7.2) `i_!(G')≅D_V(Ri_*G)`, (4.7.3) `R Hom(A_U,G)≅R Hom(A_V,Ri_*G)`, (4.7.4) `Ri_*G⊗^L D_V(Ri_*G)→K_V`,
  (4.7.5) `RΓ(U,G)⊗^L_A RΓ(V,i_!G')→R Hom(A_V,K_V)`, (4.7.6) `R Hom(A_V,K_V)≅R Hom(A_{V,X},K_X)` — all match. CLEAN.
- **note (no change):** at (4.7.6) the source writes `K_V = j^!K_X` (shriek), but the §4.7 setup (p44) wrote
  `K_V = j^*K_X` and the TeX uses `j^*` throughout. For the OPEN immersion j, `j^!=j^*`, so they are equal; the
  source is internally inconsistent (j^* in setup, j^! here). TeX standardizes on the correct, consistent `j^*`. Kept.

## Source p46 — Exposé I, §4.7 (4.7.7/4.7.8, perfectness, triangle (b))
- (4.7.7) `0→A_{V,X}→A_X→A_x→0`, (4.7.8) `R Hom(A_{V,X},K_X)→R Hom(A_x,K_X)≅A`; perfectness setup `G=(ji)^*F`,
  `F'=D_X(F)`, `F'_{U,X}=(ji)_!G'`, (4.7.9) `0→F'_{U,X}→F'→F'|Y→0`; triangle (b) checked node-by-node
  (top `RΓ_x(F'_{U,X})`, [dr]/[ur,+1]/[ll]); (4.7.10) `R Hom(A_{V,X},F'_{U,X})[1]≅RΓ_x(F'_{U,X})` — all match. CLEAN.

## Source p47 — Exposé I, §4.7 (4.7.10 derivation, triangle (a), 4.7.12–4.7.14)
- (4.7.10) `RΓ(V,i_!G')[-1]≅RΓ_x(F'_{U,X})` (via dualité `R Hom(j_!A_V,j_!i_!G')≅R Hom(A_V,i_!G')`), (4.7.11)
  `0→A_{U,X}→A_X→A_Y→0`; triangle (a) checked (top `RΓ(U,F|U)`, [dl,+1]/[rr]/[ul]); accouplements (4.7.12)
  `RΓ(U,F|U)×RΓ_x(F'_{U,X})→A`, (4.7.13) `RΓ_Y(F)×RΓ_x(F'|Y)→A`, (4.7.14) `RΓ(X,F)×RΓ_x(F')→A`;
  compatibility remark — all match. CLEAN.
- **note (no change):** at (4.7.10) the source writes `RΓ_V(i_!G')` (V as subscript) where the TeX writes
  `RΓ(V,i_!G')` (V as the space). Same object here (cohomology of the open V); TeX consistent with the surrounding
  (4.7.x) `RΓ(space, coeff)` notation. Kept.

---

## Source p48 — Exposé I, §4.7 ((4.7.15) suites, Prop 4.7.16 + two triangles) — ONE FIX
- **symbol — spurious `_x` on (4.7.15) 3rd term (FIXED).** TeX 1320 had the transposed sequence ending
  `… ⟵ \H_x^{-i}(X,F') ⟵ \H_x^{-i-1}(V,F'_{U,V})`. The source (verified 600 dpi) writes the third term as
  `H^{-i-1}(V,F'_{U,V})` with NO `_x` — the first two terms carry `_x` (local cohomology RΓ_x of X/Y), but the
  third is plain cohomology of the open V (via 4.7.10 `RΓ_x(F'_{U,X}) ≅ RΓ(V,F'_{U,V})[-1]`, the `(V,·)` form
  has no support subscript). Removed the spurious `_x`: `\H_x^{-i-1}(V,F'_{U,V})` → `\H^{-i-1}(V,F'_{U,V})`.
- (4.7.15) first row `…→H^i_Y(X,F)→H^i(X,F)→H^i(U,F)→…`; Prop 4.7.16 stmt (*) `RΓ(U,G)×RΓ(V,i_!G')[-1]→A`,
  (**) `RΓ(V,i_!G')[-1]≅RΓ_x(F'_{U,X})`, `F'_{U,X}=(ji)_!(F'|U)=(ji)_!(G')`; the TWO triangles checked
  node-by-node (triangle 1: top `RΓ(U,F|U)`, BL `RΓ_Y(F)`, BR `RΓ(X,F)`, arrows aL→aR/aR→aT/aT→aL(+1);
  triangle 2: top `RΓ_x(F'_{U,X})`, BL `RΓ_x(F'|Y)`, BR `RΓ_x(F')`, arrows bT→bR/bR→bL/bL→bT(+1)) — all match.

## Source p49 — Exposé I, §4.7 end (Rem 4.7.17)
- Rem 4.7.17 (Y={x} case: accouplement needs only K_X normalised, `RΓ_x(K_X)≅A`; local⇔global dualité on U=X-x;
  `RΓ(U,G)×RΓ(U,G')[-1]→A`, `H^i(U,G)×H^{-i-1}(U,G')→A`; the excellent/U-regular-dim-d case `K_U=K_X|U≅(μ_n)_U^{⊗d}[2d]`,
  Poincaré-type `H^i(U,G)×H^{2d-1-i}(U,G^∘)→A`, `G^∘=Hom(G,(μ_n)_U^{⊗d})`) — all match. CLEAN.

## Source p50 — Exposé I, §5 Dualité locale sur les courbes (Théorème 5.1 + Démonstration start)
- §5 head; Th. 5.1 (X noeth. régulier dim 1, n prime to resid. char ⇒ pureté vraie + A_X dualisant);
  Démonstration: reduction to X strictement local (dim.q.inj(A_X)=2 via 3.2.1, cond (ii) via 3.3.1b(i), 4.4);
  setup x/η/U=Spec k(η), G=Gal(k(η̄)/k(η)), (5.1.1) `1→P→G→H→1`, `H=∏_{ℓ≠π}Z_ℓ(1)`, `Z_ℓ(1)=lim μ_{ℓ^ν}`,
  P pro-π-group; cohomology étale of U = Galois cohomology of G — all match. CLEAN.

---

## Source p51 — Exposé I, §5.1 (Hochschild–Serre, (5.1.4)–(5.1.6)) — ONE FIX
- **symbol — spectral-sequence abutment `H^{p+q}`→`H^*` (FIXED).** TeX 1401 had the Hochschild–Serre s.s.
  `E_2^{pq}=H^p(H,H^q(P,M)) ⟹ \H^{p+q}(G,M)`; the source writes the abutment as `H^*(G,M)` (star) — verified
  on p51 chunk + confirmed on p51 mid. The document's convention for s.s. abutments is `*` (cf. `\Ext^{*}`
  in the p28 spectral sequence). Both denote the abutment, but the source uses `*`. Fixed `\H^{p+q}`→`\H^{*}`.
- (5.1.2) `0→H^0_x(A_X)→H^0(X,A_X)→H^0(U,A_U)→H^1_x(A_X)→0`, (5.1.3) `H^i_x(A_X)≅H^{i-1}(U,A_U)` (i≥2),
  H^0=A so H^0_x=H^1_x=0; `H^q(P,M)=0` (q≠0), (5.1.4) `H^p(G,M)≅H^p(H,M^P)`, (5.1.5) `H^p(G,M)≅H^p(Ẑ(1),M^P)`,
  (5.1.6) `H^i(Ẑ,N)=0 (i≥2), H^0=N^Ẑ, H^1=N_Ẑ` — all match.

## Source p52 — Exposé I, §5.1 (H^i(U,A_U), (5.1.7), (5.1.8), Lemme 5.1.9)
- `H^i(U,A_U)=0 (i≥2)`, `H^1(U,A_U)≅A`; (5.1.7) `H^1(U,μ_n)≅A` (classe fondamentale locale); pureté démontrée;
  (5.1.8) `H^i(U,M)×H^{1-i}(U,Hom(M,A_U))→H^1(U,A_U)≅(μ_n)_x^{⊗-1}`; Lemme 5.1.9 (i) `D(M^G)≅(DM)_G`,
  (ii) `M^G→M_G` iso (G pro-order prime to n) — all match. CLEAN.

## Source p53 — Exposé I, §5.1 end (Lemme 5.1.9 proof, (5.1.8)')
- Lemme 5.1.9 proof (`M^G=lim Ker(s-1)`, `D(M^G)≅lim Coker(s-1)≅(DM)_G`; (ii) via `0→M'→M→M_G→0`, H^1(G,M')=0);
  application to M,P (`Hom(M,A)^P≅Hom(M^P,A)`); (5.1.8)' `H^i(Ẑ,M^P)×H^{1-i}(Ẑ,D(M^P))→H^1(Ẑ,A)≅A`;
  perfect — end of Th. 5.1 / Exposé I §5 — all match. CLEAN.

## Source p54 — Exposé I, Bibliographie — ONE FIX (citation anchor)
- **citation key `[SGA]`→`[SGAA]` (FIXED).** The bibliography entry for SGA 4 has key `[SGAA]` in the source
  (verified) — "Séminaire de Géométrie Algébrique de l'IHES, Cohomologie étale des schémas, Artin–Grothendieck,
  1963–64". The TeX had `\item[{[SGA]}]` (one A). Fixed to `[SGAA]`. **This is the anchor of the SYSTEMATIC
  SGA→SGAA issue: the bibliography defines the key as SGAA, so every in-text SGA-4 reference must read `SGAA`.**
  Strengthens the deferred citation-consistency pass (the §4.3+ `SGA~<exposé>` instances → `SGAA~<exposé>`).
- Entries [2] Hironaka, [1] Abhyankar, [H] Hartshorne, [CL]/[CG] Serre — all match.

## Source p55 — Exposé I, Appendice (Illusie) §1.1 Faisceaux constructibles — TWO FIXES
- **notation — module category `A^X`→`{}_A X` (FIXED).** TeX 1504 wrote the category of left A_X-modules as
  `$A^{X}$` and its derived cat as `$\D_A(X)$`; the source (verified 600 dpi) writes `_A X` (left-subscript A,
  the standard left-modules notation) and `D(_A X)`. Fixed `A^{X}`→`{}_A X`, `\D_A(X)`→`\D({}_A X)`.
- **subscript — `A_U`→`A_{U_i}` (FIXED).** The constructibility def replaces "loc. constant de présentation finie"
  by "de présentation finie comme `A_{U_i}`-Module" (U_i = the partition pieces); the TeX dropped the `i` (`A_U`).
  Verified 650 dpi. Fixed.
- Appendice header (par L. Illusie), intro (provisoire footnote "Selon Grothendieck!"), `D_c(X)` def — all match.

---

## Source p56 — Appendice §1.2 + Prop 1.3 (lemme de dévissage) — ONE FIX (boundary p56/57)
- §1.2 pseudo-cohérent (`D(X)_coh`), Prop 1.3 stmt: conditions (i)/(ii)/(iii) (`f_*i_!(M_U)`, M_U monogène) — match.
- **prose — "équivaut à (i) si"→"équivaut à la condition analogue où" (FIXED).** The last sentence of Prop 1.3
  (spanning p56 bot→p57 top) reads in the source: "la condition (ii) (resp. (iii)) **équivaut à la condition
  analogue où** l'on suppose en outre Y (resp. U) régulier" (verified). The TeX 1519 had "équivaut à **(i) si**
  l'on suppose…" — a different statement (source: (ii)⇔the analogous condition with Y regular, matching the
  main-text (ii)⇔(ii bis) structure). Fixed to source.

## Source p57 — Appendice §1, Prop 1.3 Preuve (cartesian square)
- Preuve: (i)⇔(ii) via SGAA IX 2.4/2.5; (iii)⇒(ii): `M=⊕_ℓ M_ℓ`, Sylow H, trace `F→h_*h^*(F)`, Main Theorem
  (EGA IV 8.12.6); cartesian square (U→i→Y / h,f down / Z→j→X) checked — all match. CLEAN.

## Source p58 — Appendice §1, Lemme 1.3.1 (stmt + proof)
- `j_!h_*h^*(F)≅f_*i_!h^*(F)`; Lemme 1.3.1 (H ℓ-group, M annulé par ℓ^ν ⇒ filtration with monogenic quotients,
  H trivial); proof (`0→ℓM→M→M/ℓM→0`, Nakayama `F_ℓ[H]→F_ℓ` nilpotent, M≠0⇒M^H≠0) — all match. CLEAN.

## Source p59 — Appendice §2 Dimension quasi-injective
- §2: dim.q.inj ponctuelle (`Ext^i(F,K)_x̄=0, i>N`), `dim.q.inj(K)=sup_x̄ dim.q.inj_x̄`; dim. topologique stricte
  (Verdier, `Ext^i(A_Y,K)_x̄=H^i_Y(K)_x̄=0`) — all match. CLEAN.
- **note (deferred to notation pass):** the source's abbreviation for "dimension topologique stricte" is `dimstop`
  (3× consistent, p59–60); the TeX uses `dim.top`. Cosmetic; grouped with the SGA→SGAA notation-consistency pass.

## Source p60 — Appendice §2 end, §3 Complexes dualisants, §4 Pureté absolue start — ONE FIX
- **letter swap — `de X`→`de Y` (FIXED).** §3: "Les énoncés (I 1.12, 1.13, 1.15) sont valables, mais à condition
  de supposer A annulé par un entier n>0 premier aux caractéristiques résiduelles de **Y**" — source reads Y
  (verified 650 dpi); TeX had `de X`. I 1.12/1.13/1.15 are the énoncés about a morphism f: X→Y, so "Y" (the base)
  is the sensible reading and is what the source says; the TeX's "X" was an unwarranted change. Fixed (only this
  instance — the later "x̄ de X" is correctly X). [§4's own "résiduelles de X" IS correctly X — its X is the ambient scheme.]
- `dimstop_x̄(K)≤dim.q.inj_x̄(K)`; §3 (couple bidualisant/complexe dualisant as I 1.7, énoncés I 1.9/1.11/1.14,
  unicité I 2.1 needs Spec(A_x̄) connexe); §4 setup (X reg, i:Y→X codim d, classe fondamentale locale SGA 4½ Cycle 2.2) — match.

---

## Source p61 — Appendice §4 ((4.1)–(4.3), Déf 4.4 prep) — ONE FIX
- **bounded vs unbounded derived cat — spurious `+` on `\D_A^+` (FIXED).** TeX 1608 had "la flèche (4.2) se
  définit pour tout $F\in\ob\D_A^+(X)$"; the source reads `D(_A X)` with NO `+` (verified 600 dpi) — the whole point
  is that finite cohomological dimension of `i^!` extends (4.2) from D^+ to the UNBOUNDED D. The next line (the
  (4.3) composite) correctly has `D^+(_A X)` in both source and TeX. Fixed the first: `\D_A^+(X)`→`\D_A(X)`.
- (4.1) `(μ_n^{⊗d})_Y[-2d]→Ri^!(Z/nZ)_X` iso; (4.2) `i^*(F)⊗^L Ri^!(G)→Ri^!(F⊗^L G)` (Künneth+trace);
  the i^! finite-cohom-dim conditions — all match.
- **note (deferred to notation pass):** the source writes the derived cat of left A_X-modules as `D(_A X)` / `D^+(_A X)`
  (the `_A X` notation, cf. p55); the TeX uses `\D_A(X)` / `\D_A^+(X)`. Same object; grouped with the SGA→SGAA /
  dimstop notation-consistency pass (so the p55 inline `{}_A X` fix is propagated uniformly later, not piecemeal).

## Source p62 — Appendice §4 ((4.3), pureté au sens fort, Déf 4.4)
- (4.3) `i^*(F)⊗^L(μ_n^{⊗d})_Y[-2d]→Ri^!(F)`; the iso claim (loc. const. H^i(F), i^! fin. cohom. dim ⇒ (4.2)/(4.3) iso)
  + its proof (dévissage to F=(Z/nZ)_X, (4.2)=identity); Déf 4.4 (pureté au sens fort); pureté fort ⇐ pureté ordinaire
  + i^! fin. cohom. dim — all match. CLEAN.

## Source p63 — Appendice §5 Majoration de la dim. q.inj (Prop 5.1 + Démonstration start)
- Prop 5.1 (X reg loc noeth, A_X loc const annulé par n, (reg)+(cdloc)_n+pureté fort ⇒ `dim.q.inj_x̄(F)=2dim(O_{X,x})+dim.inj(F_x̄)`);
  Démonstration: the inequality ≤ N, relation (*) `Ext^i(E,F)_x̄=0, i>N`; dévissage to E=i_!(M), Y reg in D(f) codim d — all match. CLEAN.

## Source p64 — Appendice §5 (Prop 5.1 proof: duality, (4.3), cartesian square)
- duality `R Hom(i_!(M),F)≅Ri_* R Hom(M,Ri^!F)`; (4.3); `R Hom(M,Ri^!F)_ȳ ≅ R Hom(M_ȳ,(Ri^!F)_ȳ) ≅ R Hom(M_ȳ,F_ȳ)[-2d]`;
  `F_x̄≅F_ȳ`, Ext bounds `Ext^q(M,Ri^!F)=0, q>2d+dim.inj(F_x̄)`; cartesian square (Y→D(f) / Y→j→Z, D(f)→X / Z→k→X) checked — all match. CLEAN.

## Source p65 — Appendice §5 (Prop 5.1 proof end) — TWO FIXES
- **dropped bar — `D(f)`→`D(f̄)` (FIXED).** TeX 1673 had `\bar{Z}\cap D(f)`; the source reads `Z̄ ∩ D(f̄)` (f-bar,
  the localized image of f in O_{Z,x̄}, defined in the same sentence). Verified 650 dpi. Fixed `D(f)`→`D(\bar{f})`.
  (The `×_Z` here matches the TeX — independently consistent; cf. the main-text I 3.2.1 which used `×_X`.)
- **spurious subscript — `M'_x̄`→`M'` (FIXED).** TeX 1697 had `\Ext^f(M'_{\bar{x}},F_{\bar{x}})`; the source reads
  `Ext^f(M', F_x̄)` (M' has NO x̄ subscript — M' is already an A_x̄-module = M_x̄, so a stalk of it is meaningless).
  The TeX's own earlier line 1693 correctly has `\Ext^f(M',F_{\bar{x}})`, so 1697 was internally inconsistent. Fixed.
- the R^p i_* bound + `dim(O_{Z,x})=dim(O_{X,x})-d`, "ce qui démontre (*)"; the meilleure-possible argument
  (`Ext^f(M',F_x̄)≠0`, Y=U∩Z, M_x̄=M', `Ext^{2d+f}(M,F|U)_x̄≅Ext^f(M',F_x̄)≠0`) — all match (after the 2 fixes).

---
(new entries appended below as the ordered pass runs)
