# Errata to SGA 5 (Lecture Notes in Math. 589) — printed-source errors

**What this is.** A running list of errors, typos and internal inconsistencies found in the *printed*
book **SGA 5, LNM 589** (Cohomologie ℓ-adique et fonctions L), identified while preparing a
symbol-level source-faithful LaTeX edition (`sga5_fr_workpass.tex`, the curated 10-exposé selection
I / III / IIIB / V / VI / VII / VIII / X / XII / XV). Each entry records what the book prints and the
reading the edition adopts. Two dispositions:

- **[corrected]** — a genuine typo (occurs once, contradicts a sibling formula or the mathematics);
  the edition silently prints the correct reading. Disclosed here for transparency.
- **[faithful]** — a source error or coherent notational abuse that recurs or is load-bearing; the
  edition **keeps the printed reading** and this note is the erratum.
- **[normalized]** — orthographic / typographic modernization (accents, spacing, `C^•` vs `C^*`,
  full-caps → small-caps); meaning-preserving, listed only where noted, never a math change.

**Provenance & status.** Items on p77–483 were **surfaced by the audit swarm** and their edition
readings were cross-checked during the page-by-page hand pass (`CERT_LOG.md`); a dedicated
scan re-verification of each entry is ongoing. **All seven substantive `[corrected]` mathematical
entries — p88, p97, p147, p150, p170, p277, p390 — were independently re-zoomed 2026-07-02 and each
confirmed** (marked `✓`): in every case the printed book genuinely errs and the edition's correction
is right (a 100% hit rate on the checked sample). Re-zoom of the remaining `[faithful]` and minor
`[corrected]` (spelling/orthographic) entries is still pending — see "To finish". Items on p1–72 (Exposé I) and the recent by-hand pages (p462–480, index) come from
the hand pass logged in `CERT_LOG.md` / `FINDINGS.md`; the p34 and index items were re-zoomed
2026-07-02. This is **provisional and
motivated**, NOT a claim of completeness or correctness — it is what the hand+swarm passes have found
so far, each entry traceable to a scan page.

**Note on `[corrected]` vs `[faithful]` (sweep complete).** For the swarm-surfaced items
(p77–483) these disposition tags were initially inferred from the swarm's prose, then **verified
against the edition's actual `.tex` reading** (2026-07-02). That verification found the initial tags
were **systematically wrong**: ~35 items first marked `[faithful]` are in fact `[corrected]` (the
edition silently fixes the book's typo). The error was one-directional — it always **undersold** the
edition (crediting a book error as "kept" when the edition had corrected it), never the reverse. **Every
swarm item has now been `.tex`-verified.** The genuine `[faithful]` entries are the loose-citation slips
the edition reproduces: Exposé I (p14/p16/p26/p30/p43), p111, p208, p209, p386, p281, p289, and the
index XIV/XV. Several queries turned out **not to be book errors** at all (p166, p171-5.9.1, p286,
p312, p388, p464, p474 — mostly `^e`-tic or scan-rendering false flags). A `✓` mark means a given entry
was `.tex`-verified. Throughout, the *description* of each entry (what the book prints, what the correct
reading is) is reliable. The by-hand items (Exposé I, XV, index)
were tagged from direct inspection.

---

## Exposé I (Verdier, *Complexes dualisants* + Illusie *Appendice*) — scan p1–72

Detailed per-page findings for Exposé I live in `FINDINGS.md` (p1–65) and `CERT_LOG.md`. The book's
own errors (TYPE-B) on these pages are almost all **loose citations, kept faithful**:

- **p14** (Cor 1.13 proof chain): book prints `Rf_*F ≅ … ≅ D_Y Rf_* D_X F (par a)(i)) ≅ D_Y D_Y Rf_* F (par a)(i))`
  — the intermediate object is `Rf_* D_X F` and **both** steps are cited as `a)(i)`. Correct: the
  intermediate should be `D_Y Rf_! D_X F` and the second step should cite **`a)(ii)`**
  (a)(i) = Rf_*D_X ≅ D_YRf_!, a)(ii) = Rf_!D_X ≅ D_YRf_*). Recurs in the f-fini case just below. **[faithful]**
- **p16** (Théorème 2.1): book cites `(1.6)` for "complexe dualisant", which is defined in Déf **`(1.7)`**.
  Probable cross-ref slip. **[faithful]**
- **p26** (Prop 3.2.1 proof): book leaves the projection-formula reference number **blank** — prints
  `(SGAA XVIII  )` with an empty slot. **[faithful]**
- **p30** (Prop 3.3.1, at the cqfd): book writes `RHom(M, Ri^!(G)) ∈ D_c^+(X)` → should be **`D_c^+(Y)`**
  (M and Ri^!(G) both live on Y); source typo `X` for `Y`, or loose `i_*`-shorthand. **[faithful]**
- **p34** (Cor 3.4.3 preuve, penult. line): book prints `R^!f'(A_S) localement isomorphe à A_X` →
  should be **`A_{X'}`** (R^!f' is on X', since f':X'→S). **[corrected]** *(600dpi-zoom confirmed 2026-07-02; silent in baseline, newly disclosed.)*
- **p34** (same cqfd line): book prints `(ii) et (ii) de (1.7)` → should be **`(ii) et (iii)`**
  (matches the proof's own earlier "(ii) et (iii)" + the math). **[corrected]**
- **p40** (§4.5): in `K_Y = ℝ^!j(K_X)` the book prints the functor letter as `j`, but `j:U→X` is declared
  (same page, first line) as the *open* complement of `Y`, so `ℝ^!j = j^*` lands on `U`, not on the closed
  `Y`; `K_Y` (dualizing complex on `Y`) requires the closed immersion `i:Y→X`, i.e. `ℝ^!i` — which is
  exactly what the book uses in the parallel `ℝ^!i` on line 1 and in the `(D_XF)_x̄` computation below.
  Internal `j`-for-`i` typo; edition prints **`ℝ^!i(K_X)`**. **[corrected]** ✓ *scan 850dpi-confirmed
  2026-07-03 (book prints `j`, descender clear); .tex L1085 reads `\R^{!}i(K_X)`.*
- **p43** (§4.6, TeX L1167): the "induction ordinaire (1.12 b)(i)" step cites an item whose intent is
  ambiguous at current scan resolution — flagged, left faithful pending a clearer scan. **[faithful]**

*(Not errata: the many Exposé I edition-side corrections — `SGA`→`SGAA` citation A-restorations,
sheaf `Hom`/`Ext` underline restorations, the `⊗d`→`⊗−d` twist on p26, `H^i`→`I^i` on p4 — are
**transcription** fixes, where the printed book was correct and the edition draft had erred. They are
logged in `FINDINGS.md`, not here, since this file lists errors in the printed book.)*

---

## Exposés III–XV (scan p73–480) — swarm-flagged, hand-verified

### Exposé III — *La formule de Lefschetz* (Illusie), scan p73–137  (Künneth / bidualité)
- **p85** (2.6.1.1) & upper-right RHom node: book prints second argument `F'` (stray prime) → edition
  prints **`F`** (only E,F ∈ D_ctf(X) defined). **[corrected]** ✓ *.tex-confirmed 2026-07-02 (L2182 `\uRHom(E,F)`).*
- **p85** lower/bottom-right node: book prints a stray `1` in `f*(E ⊗ 1)` → edition prints
  **`f^*(E ⊗^L L)`** (derived tensor, parallel to the upper-right node). **[corrected]** ✓ *.tex-confirmed 2026-07-02 (L2189).*
- **p88** (v:F→f_*F): book prints `v : f ⟶ f_*F` with a lowercase `f` as source (a morphism, not an
  object — malformed) → the edition reads the object **`F`**. **[corrected]** ✓ *re-zoom-confirmed
  2026-07-02 (scan clearly prints lowercase `f`, matching the surrounding `f_*E`/`f_*F`).*
- **p91** (3.2.6) RHom: book prints `c_1(F*)*L_1` with a spurious star *inside* the paren after F, in
  addition to the outer pullback star → edition prints **`c_1(F)^*L_1`** (no inner star). **[corrected]**
  ✓ *.tex-confirmed 2026-07-02.*
- **p97** (Rp_{2!} coeff): book prints `A_{X_2}` → should be **`A_X`** (p_2:X→X_2, so the
  constant sheaf lives on the source X). **[corrected]** ✓ *re-zoom-confirmed 2026-07-02 (600dpi: scan prints `Rp_{2!}A_{X_2}`).*
- **p104** (4.4.5) bottom-left node: book prints stray prime `RHom(f_{i*}L'_i,…)` → edition prints
  **`f_{i*}L_i`** (no prime). **[corrected]** ✓ *.tex-confirmed 2026-07-02 (L3044 reads `f_{i*}L_i`).*
- **p105** (8)/(9) square right column: book prints `c_*c'^!(…)`, `d_*d'^!(…)` with a stray prime on the
  second letter → edition prints **`c_*c^!`, `d_*d^!`** (no prime). **[corrected]** ✓ *.tex-confirmed 2026-07-02 (L3076/L3081).*
- **p106** lower square bottom-right: book prints a **bare `d`** (no shriek) in `d(P⊗^L Q)` where the
  analogous corners carry a shriek → edition prints **`d^!(P⊗^L Q)`**. **[corrected]** ✓ *.tex-confirmed 2026-07-02 (L3161).*
- **p110** Cor 4.9: book prints `Hom(Rf_*A, Rf_{1*}A)` (no numeric subscript on first factor) → edition
  prints **`Hom(Rf_{2*}A, Rf_{1*}A)`** (cl(C'')_* is the transpose Rf_{2*}A→Rf_{1*}A). **[corrected]**
  ✓ *.tex-confirmed 2026-07-02 (L3367).*
- **p111**: book prints `au-dessus de s` (lowercase) → geometric point lies above base **`S`**. **[faithful]**
- **p113** (5.1.5): book prints second arg of first Hom as `c_2^! L_1` → edition prints **`c_2^!L_2`**
  (a cohomological correspondence is "de L_1 à L_2"). **[corrected]** ✓ *.tex-confirmed 2026-07-02 (edition uses `c_2^!L_2` throughout).*
- **p116** (5.2.6): book prints `M_3 = f_{3*}M_3` (self-referential, mathematically wrong) → edition
  prints **`M_3 = f_{3*}L_3`** (pattern M_1=f_{1!}L_1, M_2=f_{2*}L_2). **[corrected]** ✓ *.tex-confirmed 2026-07-02.*
- **p116** left square upper-right node: book prints plain `C` → edition prints **`C'`** (the node maps
  `c':C'→X_{12}`; the parallel right square has `C''`). **[corrected]** ✓ *.tex-confirmed 2026-07-02 (L3574 `X_{12} ← C'`).*
- **p120** (§6 appendix, opening line): book prints `S désigne un shcéma noethérien` — `sch`→`shc`
  letter transposition → **`schéma`**. The edition prints `schéma`. **[corrected]** ✓ *scan 850dpi-confirmed
  2026-07-03; .tex L3704. (Rest of §6.1–6.2 — (6.1.1)/(6.1.2)/(6.1.3), the six operations — matches symbol-exact.)*
- **p126** Théorème 6.7 (the `On pose` definitions): book prints `d''_i = p_i d''` → should be
  **`q_i d''`** (parallel to `d'_i = q_i d'`; d'' maps into Y, so the projection is q_i:Y→Y_i).
  **[corrected]** ✓ *scan + .tex confirmed 2026-07-02 (scan p126 prints `p_i d''`; `.tex` L3862 has `d''_i=q_i d''`).*
- **p127** (6.8): book prints the morphism as `f = X ⟶ S` (equals, wrong) → edition uses the colon
  **`f : X → S`**. **[corrected]** ✓ *.tex-confirmed 2026-07-02 (edition writes `f:X→…` throughout; no equals-morphism).*
- **p128** (ΛN⊗Ω): book prints conormal subscript `N_{Y/S}` (3 spots) → edition prints **`N_{Y/X}`**
  (cf. `N_{Y/X}=I/I²`). **[corrected]** ✓ *.tex-confirmed 2026-07-02 (all sites L3915–3932 read `N_{Y/X}`).*
- **p128**: book prints internal xref `6.83` (missing a dot) → edition prints properly-dotted refs
  (`6.8.2`, `6.1.1`, …); no `6.83` in the edition. **[corrected]** ✓ *.tex-confirmed 2026-07-02.*

### Exposé III B — *Calculs de termes locaux* (Illusie), scan p138–203  (trace / non-commutatif)
- **p143** (§1.4): book prints the dual homomorphism `(Du)_z ∈ Hom((DM)_y, (DM)_x)` — the codomain `(DM)_x`
  should be **`(DL)_x`**, since `Du∈Hom(a_2^*DM, a_1^!DL)` maps `DM→DL` (confirmed by the dual
  `(Dv)_z∈Hom((DL)_x,(DM)_y)`, which book and edition agree on). The edition prints `(DL)_x`. **[corrected]**
  ✓ *600dpi + .tex-confirmed 2026-07-03 (book `(DM)_x`, .tex L4307 `(DL)_x`).*
- **p146** (Lemme 2.2 b): book prints `M|U = 0` (flat-bottom U, should parallel `L|U`) → edition prints
  **`M|V = 0`**. **[corrected]** ✓ *.tex-confirmed 2026-07-02 (L4367 `L|U=0, M|V=0`).*
- **p147**: resp.-branch final arrow labelled `u` → should be **`v`** (v defined above). **[corrected]**
- **p147** (contrast clause): book prints `tandis que gr^0L (resp. gr^1M) est concentré` → the resp.
  to `gr^0L` must be **`gr^0M`** (it contrasts the gr^1 "fibre nulle" clause). **[corrected]**
  ✓ *re-zoom-confirmed 2026-07-02.*
- **p147**: projections `s → S` → should be **`x → S, y → S`** (closed points x on X, y on Y). **[corrected]**
- **p147**: `m = h_{2*}M''` → object being defined is **`M`** (capital). **[corrected]**
- **p150** (rel.-cohomology iso RHS): book prints `RΓ_A(T,(DL⊗^L_S M)T)[1]` — **omits the restriction
  bar** `|` before the final T (the LHS `(…)|T−A` and every display above carry it). The edition
  supplies `(…)|T`. **[corrected]** ✓ *re-zoom-confirmed 2026-07-02.*
- **p155** (2): third inequality `λ'_j ≠ μ'_j` → edition prints **`λ_i ≠ μ_j`**. **[corrected]** ✓ *.tex-confirmed 2026-07-02 (L4744).*
- **p155**: resp.-range for (y_j) printed `1≤i≤m` → edition prints **`1≤j≤n`** (y_j over n points). **[corrected]** ✓ *.tex-confirmed 2026-07-02 (L4733).*
- **p155**: fourth uniformisante `v''` → edition prints **`v'`** (pattern u/v/u'/v'). **[corrected]** ✓ *.tex-confirmed 2026-07-02 (L4740).*
- **p159**: book prints `R^q j_* L = 0 pour p>2` (wrong index variable — p is undefined) → edition uses
  the cohomological degree **`q`** (condition (P): `R^q j_*(Z/ℓ)=0 pour q>1`). **[corrected]** ✓ *.tex-confirmed 2026-07-02 (L4809).*
- **p162** (5.0.7): first arg `\uRHom_K(E;K)` uses a **semicolon** → comma `(E,K)` (cf. 5.0.6). **[corrected]**
- **p166** (5.3.4)/(5.3.5): the swarm queried whether the left derived-tensor subscript `⊗_A` should be
  `⊗_{A^e}`. The `.tex` reads `E⊗^L_A F ⥲ (E⊗^L_K F)⊗^L_{A^e}A` (5.3.4) — the left `⊗_A` is **correct**
  (the standard A-vs-A^e identity); same `^e`-tic false flag as p171 (5.9.1). **[non-error]**
- **p170** (5.8.1 relation `axb⊗y − x⊗bya`): book prints `a,b ∈ K` → should be **`a,b ∈ A`** (a,b act
  as algebra elements sandwiching the bimodule elements; K-scalars are already in ⊗_K). **[corrected]**
  ✓ *re-zoom-confirmed 2026-07-02 (scan prints `a,b ∈ K`).*
- **p170** (same line): book prints `y ∈ P, y ∈ Q` → first should be **`x ∈ P`** (the relation's
  P-element is x). **[corrected]** ✓ *re-zoom-confirmed 2026-07-02 (scan prints `y∈P, y∈Q`).*
- **p171**: book prints second Hom `Hom(F, Q⊗^L_A E)` missing the subscript → edition prints **`Hom_A`**
  (so Tr_A(uv) 5.8.5 works). **[corrected]** ✓ *.tex-confirmed 2026-07-02 (L5174 `v∈uHom_A(F,…)`).*
- **p171**: book prints `ob D^b(B^o)` → edition prints **`D^b(B^e)`** (both args are B^e-modules). **[corrected]** ✓ *.tex-confirmed 2026-07-02 (L5196).*
- **p171** (5.9.1 nodes): the swarm queried whether outer-tensor subscripts `⊗_A`/`⊗_B` should be
  `⊗_{A^e}`/`⊗_{B^e}`. The by-hand review found `⊗_A`/`⊗_B` **correct** here (the spurious `^e` was the
  transcription draft's error, not the book's — cf. the `^e`-tic note in `METHOD_AND_LESSONS`). **[non-error]**
- **p174** (5.10.5 prose): book prints `flèche de D(X)` → edition prints **`D(K)`** (RHom_K target). **[corrected]** ✓ *.tex-confirmed 2026-07-02 (L5244).*
- **p178** (5.11.4 boundary diagram): the typescript carries the derived-tensor superscript `L` only on
  the lead node and drops it on repeats. The edition restores `⊗^L` on all nodes. **[normalized]**
  ✓ *.tex-confirmed 2026-07-02 (L5380+ all use the derived tensor).*
- **p181**: book prints trace xref `Les traces 5.14.2` (no such item) → edition prints a valid ref
  (`5.4.2`/`5.13.2`). **[corrected]** ✓ *.tex-confirmed 2026-07-02 (no `5.14.2` in edition).*
- **p182**: book prints `N ∈ ob D^b(K)` then immediately uses the object as **`M`** in (5.13.5) — a
  self-contradiction; the edition prints `M`. **[corrected]** ✓ *by-hand grind finding (source contradicts itself).*
- **p190** (6.8.2 prose): book names the second element `c` → edition prints **`v`** (matching the
  formula `Tr_R(u⊗v)`; c is the correspondence morphism). **[corrected]** ✓ *.tex-confirmed 2026-07-02 (L5916 `Tr_R(u⊗v)`).*
- **p190** (6.8.3): fixed-point superscripts `Z^c` / `(A⊗B)_{Z^d}` → target lives on
  **`Z^e`** (= X^c ×_S Y^d). **[corrected]** ✓ *.tex-confirmed 2026-07-02 (L5901+ all read `Z^e`).*

### Exposé V — *Systèmes projectifs J-adiques* (Jouanolou), scan p204–250

- **p208**: composition `w_{ts} ∘ w_{sr}` printed with factors **swapped** (w_ts left, w_sr right). **[faithful]**
- **p209** (Prop 2.2.2 proof): book prints the sum `s + t`, but `s` is undefined here (the proof introduces
  only `r` for X and `t` for Z); the correct integer whose shift kills Y is **`r + t`** (X[r]→X and Z[t]→Z
  null ⟹ Y[r+t]→Y null). The edition prints `r + t`. **[corrected]** ✓ *600dpi + .tex-confirmed 2026-07-03
  (book `s+t`, .tex L6791 `r+t`; disposition was mislabeled `[faithful]`, fixed to `[corrected]`).*
- **p214**: book prints first Hom term `Hom_P(X, Y')` (spurious prime on Y) → edition prints
  **`Hom_P(X, Y)`** (Y is the fixed system). **[corrected]** ✓ *.tex-confirmed 2026-07-02 (L6928/L6945 first terms have no prime).*
- **p234**: book prints `fonctions canoniques` → edition prints **`foncteurs`** (P^n_AR / P^f_AR are
  functors). **[corrected]** ✓ *.tex-confirmed 2026-07-02 (L7613 "les foncteurs canoniques").*
- **p235** (§5.1, Hilbert-basis proof): in the increasing chain of graded submodules the book prints the
  first term with a **subscript**, `N_1 ⊂ N^2 ⊂ … ⊂ N^p ⊂ …`, while the remaining terms carry superscripts;
  this is the superscript-indexed sequence `N^1 ⊂ N^2 ⊂ …` (and `N_1` would collide with the *component*
  chain `N_0 ⊂ N_1 ⊂ …` just above). Sub-for-super slip on the first term; edition prints **`N^1`**.
  **[corrected]** ✓ *scan 800dpi-confirmed 2026-07-03; .tex L7643 reads `N^1\subset N^2`.*

### Exposé VI — *Cohomologie ℓ-adique* (Jouanolou), scan p251–281
- **p277** (Leray): book prints `R^i_!f(R^j_!g(F)) ⟹ R^{i+j}_!(g∘f)(F)` with outer f / inner g
  → mathematically the outer should be **g**, inner **f**: `R^i_!g(R^j_!f(F))` (abutment is `g∘f`, so
  f applies first / g last). **[corrected]** ✓ *re-zoom-confirmed 2026-07-02 (scan shows outer-f/inner-g).*
- **p280** (§3.2, cycle-class transition): book prints `γ_X^{(n)}(Y)` / `γ_X^{(n')}(Y)` (`Y`) in the
  transition phrase, but the cycle is `Z` (defined `γ_X(Z)` just before and after) → edition prints
  **`(Z)`**. **[corrected]** ✓ *600dpi-zoom confirmed.*
- **p281**: footnote marker `(**)` reused as the display-tag on both the (ii) and (iii) displays. **[faithful]**

### Exposé VII — *Cohomologie de quelques schémas classiques & classes de Chern* (Jouanolou), scan p282–350

- **p284** (ii)c): book prints trace display `R^{2r} q(q^*L)` with **no shriek** on R → edition prints
  **`R_!^{2r}q(q^*L)`**. **[corrected]** ✓ *.tex-confirmed 2026-07-02 (L9164).*
- **p286**: the scan shows trailing space after `(SGA 4 XVII` in "résolution de Godement de A_X", but
  `SGA 4 XVII` is a complete exposé reference; the edition prints `(SGA 4 XVII)`. **Not a book error**
  (typewriter spacing, no missing number). *(The genuinely-blank citation is at p426, Exposé XII.)*
- **p287** Prop 2.2.2 b): book prints target `⊕_i R^2 p_*(μ_P^{⊗i})` (exponent `2`) → edition prints
  **`⊕_i R^{2i} p_*(μ_P^{⊗i})`**. **[corrected]** ✓ *.tex-confirmed 2026-07-02 (L9299).*
- **p289** (2.2.5/2.2.6): graded ring printed `A^•` (raised dot) → edition uses `A^*`. **[normalized]**
- **p289** Cor 2.2.6: states basis 1,ξ,…,ξ^r (r+1 elts) yet calls A^*(P) "de même rang que E" (rank r) —
  internal inconsistency. **[faithful]**
- **p296** (3.8.1): book prints `c_i(E) ∈ H^i(X(C),Z/νZ)` (exponent i) → edition prints **`H^{2i}`**
  (a Chern class c_i sits in degree 2i). **[corrected]** ✓ *.tex-confirmed 2026-07-02 (L9619).*
- **p307** (Q) display: book prints `P_T(F) → F` → edition prints **`P_T(F) → T`** (a projective bundle
  projects to its base T). **[corrected]** ✓ *.tex-confirmed 2026-07-02 (L9517/L10037).*
- **p308**: the swarm reported the α-map upper bound as `1≤j_i≤p_m` (a source slip, since the bound
  should depend on i) and thought the edition carried it faithfully. In fact the edition prints the
  **correct `1≤j_i≤p_i`**. **[corrected]** *(or non-error if the book too reads `p_i`)* ✓ *.tex-confirmed 2026-07-02 (L10075/L10108).*
- **p309**: `l'idéal de 1 anneau de polynômes` — numeral `1` for article **`l'`**. **[corrected]**
- **p309**: `fonctions symétrique` (number mismatch). **[corrected]**
- **p310** (§5.4 démo, morphisme de `A^*(S)`-algèbres): book prints the target as `A^•[U_k]` (no `(S)`)
  in the display `A^•(S)[T_{i,j_i}] → A^•[U_k]`, whereas the map is explicitly of `A^•(S)`-algebras and
  the diagram just above writes the target fully as `A^•(S)[U_k]/J_D`; the bare `A^•[U_k]` is ill-defined
  (drops the `(S)` argument). The edition restores **`A^*(S)[U_k]`**. **[corrected]** ✓ *scan 800dpi-confirmed
  2026-07-03 (book omits `(S)`); .tex L10140 reads `A^*(S)[U_k]`.*
- **p311** (Prop 5.5, 2nd base-change iso): book prints `A^*(D)⊗_{A^*(X)}Q(X,g^*L) → Q(D,g^*L)` with
  `g^*L` in both Q-slots — an apparent source infelicity (cf. the p199–200 `f^*v=h^*v` base-change
  abuse). The edition reproduces it faithfully. **[faithful]**
- **p315** (Prop 6.2): book cites `(SGA 4 XXII 5.5.1)` → should be **`SGA 3 XXII`** (SGA 4 has no exposé
  XXII; SGA 4 = exp I–XIX). Source cross-ref quirk; edition faithful. **[faithful]**
- **p317** (Cor 6.5): book prints an **incomplete citation** `(SGA ___)` — a blank where the exposé
  number should be. Edition keeps the lacuna faithfully. **[faithful]**
- **p312**: `Q(S/T,L) = ⊕_{n,i} R^n u_*(L⊗μ^{⊗i})` sums over the pair (n,i). **Correct as printed**
  (n indexes `R^n`, i the twist); the edition matches. Listed only because an early pass queried it —
  no error. **[non-error]**
- **p328** (Lemme 8.2 c)): book prints the hyperplane class as `ξ = cℓ(𝒪_P(1))` — the book's "class of"
  map `cℓ` (cf. p324 "ξ la classe de 𝒪_P(1)") — where the edition prints **`ξ = c_1(𝒪_P(1))`** (first Chern
  class). Same element (the hyperplane class of `P=ℙ^r`); edition normalises `cℓ`→`c_1`. **[normalized]**
  ✓ *600dpi-confirmed 2026-07-03 (book `cℓ`, .tex L10668 `c_1`).*

- **p340** (Lemme 9.4 reduction): book prints `c_d(Ě) = c_d(E)` — LHS `Ě` (with check), RHS `E`
  (no check): an internal inconsistency (the RHS should be `Ě`; the `=0` conclusion is unaffected,
  `Ě` vs `E` being a unit ±1). The edition reproduces the printed reading. **[faithful]**
- **p345** (§9.8, projection-formula display after "…pour k"): the book closes the LHS with a **mismatched
  bracket**, `v_*j_*(g^*(y)c_{d-1}(F̌)]` — the `j_*(` is opened with `(` but closed with `]`. Should be
  `)`. Edition prints **`v_*j_*(g^*(y)c_{d-1}(F̌))`**. **[corrected]** ✓ *scan 850dpi-confirmed 2026-07-03;
  .tex L11373. (Rest of the dense §9.8 computation (9.8.1)–(9.8.6) matches the edition symbol-exact.)*

### Exposé VIII — *Groupes de classes des catégories abéliennes et triangulées* (Bucur), scan p351–371

- **p351** (§1, def. of additive function): book prints the target group of the first occurrence as
  `un groupe abélien C` — but `C` is the abelian *category* `𝒞`; the target of an additive function is the
  group **`G`** (confirmed by the very next sentence, `une fonction additive de 𝒟 dans un groupe abélien G`,
  and by the math). The edition prints `G`. **[corrected]** ✓ *600dpi + .tex-confirmed 2026-07-03 (book `C`, .tex L11584 `G`).*
- **p365** (§6, derived-tensor construction): two typewriter-notation normalizations (both 850–900dpi-confirmed
  2026-07-03; same object). (a) In the Künneth iso the book writes the decomposition with a summation sign,
  `∑_{p+q=n}H_p(X^•)⊗H_q(N^•)`; the edition prints the precise direct sum **`⊕_{p+q=n}`** (`\bigoplus`, .tex
  L12012). (b) The book denotes the (bounded-above) left-derived functor `L^-` (underlined L + minus superscript);
  the edition prints plain bold **`𝐋`** (`\mathbf L`, .tex L12018), dropping the `^-` boundedness marker. The
  module-side `_A𝒟`/`_A𝒞`/`𝒞_A` (left/right) discrimination is correct throughout. **[normalized]**
- **p367** (Dém. Prop 8.1): book heads the proof "Démonstration de la proposition **5.2**" but the
  proof is of **Proposition 8.1** (a referent slip). The edition reproduces "5.2" faithfully. **[faithful]**

### Exposé X — *Formule d'Euler-Poincaré en cohomologie étale* (Grothendieck/Bucur), scan p372–406
- **p378** (§3.4): book writes the derived category as `D^•(A)` (bullet superscript, twice — "`X^•` est un
  objet de `D^•(A)`" and "dépendant fonctoriellement de `X^•` dans `D^•(A)`"), but the construction takes a
  *projective resolution* `P^•→X^•`, which needs `X^•` bounded above; the edition prints the required
  **`D^-(A)`**. Book bullet-for-minus; edition uses `D^-(A)`. **[corrected]** ✓ *scan 750dpi-confirmed
  2026-07-03 (bullet, matches `X^•`/`Y^•` bullets); .tex L12400 reads `D^-(A)`.*
- **p378** (§3.4, 3rd para): book prints "comme plus haut et `X` **et** un complexe de `A`-modules à droite
  et borné `a` droite" — the second `et` is a slip for **`est`** (X *is* a complex), `X` drops its bullet,
  and `a`→**`à`** (accent). Edition prints "`X^•` **est** un complexe … borné **à** droite". **[corrected]**
  ✓ *scan 750dpi-confirmed 2026-07-03; .tex L12402.*
- **p381**: `Soit A un algèbre` (masc.) → **`une algèbre`**. **[corrected]**
- **p381**: `DE module sur A` → **`le module`** (typewriter slip; edition prints the definite article). **[corrected]** ✓ *.tex-confirmed 2026-07-03 (L12472 `le module sur A`).*
- **p381**: `à partir DO ses opérations` → **`de`**. **[corrected]**
- **p381** (démo de 3.8, remark): book prose prints `M̌^•` (with check) where `M^•` is meant — a glyph
  slip. The edition keeps the printed `M̌^•` faithfully. **[faithful]**
- **p381** (3.8/3.9): book prints the second Hom/tensor arg as plain `M` (typescript bullet-drop
  convention) → edition restores **`M^•`**. **[normalized]** ✓ *.tex-confirmed 2026-07-02 (edition uses `M^\bullet` throughout §3).*
- **p382**: book prints RHS last arg as `M'` (prime) in `Hom°_{Λ[G]}(P•, M')` → edition prints
  **`M^•`**. **[corrected]** ✓ *.tex-confirmed 2026-07-02.*
- **p383**: book types `γ` as the first symbol on **both** immersion lines → edition prints `γ` then
  **`δ`**. **[corrected]** ✓ *.tex-confirmed 2026-07-02 (L12522 `γ:E→E×E`, L12523 `δ:E→E×E`).*
- **p383**: book prints the homomorphism pair `γ*, ν*` (second glyph reads as ν) and starts *both*
  pullback equations with `γ*` → edition prints **`γ*, δ*`** with **`δ*(a⊗b)=ab`**, `γ*(a⊗b)=a g*(b)`.
  **[corrected]** ✓ *.tex-confirmed 2026-07-02 (L12527, L12532–33).*
- **p384** (§4.2): book cites `(lemme 5.1)` as the reference for the fixed-point multiplicity, but this
  is a referent-slip (wrong cross-ref). The edition reproduces `(lemme 5.1)` faithfully. **[faithful]**
- **p385** (4.2.6): book prints différente subscript `𝔇_{C/C'}` → edition prints the standard
  **`𝔇_{C'/C}`**. **[corrected]** ✓ *.tex-confirmed 2026-07-02 (all sites L12585+ read `𝔇_{C'/C}`).*
- **p385**: `désigné part Art_{y'}` → **`par`**. **[corrected]**
- **p385** (closing character list): book begins the list `σ_{y'}` (prime on y) → edition prints
  **`σ_y`** (list `σ_y, σ'_y, a_y`). **[corrected]** ✓ *.tex-confirmed 2026-07-02 (L12619).*
- **p386** (§4.3): book prints "la situation `(C',y'',G)` se déduit de `(C,y',G)`" — the second triple
  has an **unprimed `C`** where the parallel calls for `C'` (both situations live on the cover C'; the
  isomorphism is "g sur C'"). The edition reproduces the printed `(C,y',G)`. **[faithful]**
  ✓ *scan + .tex confirmed 2026-07-02 (L12623).*
- **p388**: the edition renders the residue-field extension `K'_1=k(η'_1)⊃k(η_1)=K_1` (L12687), which
  is correct and internally consistent. The swarm flagged something about the argument of `k(…)` but its
  description was incomplete; nothing in the edition reading is wrong. **[likely non-error]**
- **p389**: `L'homormorphisme de reduction` → **`homomorphisme`** (missing o). **[corrected]**
- **p389** graded K-group printed `K^•` (raised dot) → edition `K^*`. **[normalized]**
- **p389** (mono-trace citation): book cites `(3.3.1)` for the monomorphism `tr:K^•(Z_ℓ[G])→𝓕(G,Z_ℓ)`,
  but that statement is Prop 3.2 (p377); `(3.3.1)` is the induction formula. Referent-slip; edition
  reproduces `(3.3.1)` faithfully. **[faithful]**
- **p390** Prop 5.1: book prints `Y' = p^{-1}(X) = C'−U'` → `X` is undefined here (setup uses C/C'/U/U'),
  and `Y = C−U` was just defined, so `Y' = C'−U' = p^{-1}(C−U) = ` **`p^{-1}(Y)`**. **[corrected]**
  ✓ *re-zoom-confirmed 2026-07-02 (scan prints `p^{-1}(X)`).*
- **p390** (below the Weil formula, tagged (5.2)): book prints `le premier membre de (6.2)` → should
  reference **`(5.2)`** (the formula immediately above). **[corrected]** ✓ *re-zoom-confirmed 2026-07-02.*
- **p390** trace map `K^*(Z_ℓ[G]) → F(G,Z_ℓ)`: book labels the arrow `tv` → edition labels it **`tr`**
  (the trace / character map; the book's `tv` is a typo for `tr`). **[corrected]** ✓ *.tex-confirmed 2026-07-02 (L12362/L12749).*
- **p391** (§6, trace-reduction proof): the book writes the reduction map on the *trace-function* ring `𝓕`
  with a natural-sign superscript **`λ_n^♮`** — e.g. `𝓕(G,Z_ℓ)→^{λ_n^♮}𝓕(G,Z/ℓ^nZ)` and
  `λ_n^♮(tr(μ_ν(S_1)))=λ_n^♮(σ_2)` — reserving `λ_n^*` (asterisk) for the parallel reduction on `K^•`
  (as in `tr(λ_n^*(μ_ν(S_1)))`); the two intertwine by `λ_n^♮∘tr = tr∘λ_n^*`. The edition uses `λ_n^*`
  for **both** (the domain, `𝓕` vs `K^•`, disambiguates). Same maps, superscript conflated `♮`→`*`.
  **[normalized]** ✓ *scan 700dpi-confirmed 2026-07-03; .tex L12764/L12772 print `\lambda_n^*`.*

- **p402** (§7): book writes "(η le point générique de **S**)" where `S` is undefined at that point
  (the base is `W = Spec K`); the intended scheme is `W`. Edition reproduces the printed `S` faithfully. **[faithful]**

### Exposé XII — *Formules de Nielsen-Wecken et de Lefschetz* (Grothendieck/Bucur), scan p407–441

- **p410** (bot): `en térmes` (spurious acute) → **`en termes`**. **[corrected]**
- **p410** (top, 2nd display): book prints inner subscript `(f'_{H_{n,U'}})^∨` truncated (missing `X'`)
  → edition prints **`(f'_{H_{n,U',X'}})^∨`** (full — this was edition FIX #48). **[corrected]** ✓ *.tex-confirmed 2026-07-02.*
- **p410** (§1, trace target `(*)`): book prints **`Λ_n[G_{♮,φ}]`** — the `♮,φ` subscript sits *inside*
  the bracket, on `G` (i.e. the free `Λ_n`-module on the set `G_{♮,φ}` of φ-twisted conjugacy classes,
  the same notation as IIIB §6.10 `Λ[G_♮]`, .tex L5984, and reproduced faithfully there). The edition renders **`Λ_n[G]_{♮,φ}`** (subscript
  *outside* the bracket = φ-twisted **cocenter** of the group ring, i.e. the `A_{♮,φ}` notation of
  III B 5.13 with `A=Λ_n[G]`). Canonically isomorphic; both `≃ 𝓕_!(G_{♮,φ},Λ_n)`. Edition normalizes to
  the ring-cocenter form. **[normalized]** ✓ *1000dpi-confirmed 2026-07-03.*
- **p413** (§3, def. of the local Nielsen-Wecken invariant): on its **first** occurrence the book prints the
  subscript with a prime, `NW_{f'}^{G,φ}(x)`, in "on va lui associer une classe de φ-conjugaison `NW_{f'}^{G,φ}(x)`"
  — but `x` is a fixed point *de f*, and the book's own definitive statement three lines down designates the
  invariant **`NW_f^{G,φ}(x)`** (no prime), as do all later occurrences. Internal `f'`-for-`f` slip on the first
  use; the edition uses `NW_f^{G,φ}(x)` throughout. **[corrected]** ✓ *scan 850dpi-confirmed 2026-07-03; .tex L13380.*

- **p426** (§5, formule de Lefschetz (5.4)): book prints "formule classique de Lefschetz **(cf.  )**"
  with an **empty citation** — the reference number is left blank. The edition keeps the blank faithfully
  (+ comment). **[faithful]** ✓ *by-hand grind 2026-06-2x.*
- **p427** (§5.10 b)): book prints `ν_x(f)=1 pour tout y∈Y` — the subscript is `x` but the bound
  variable is `y`, so it should read **`ν_y(f)`**. The edition keeps the printed `ν_x` (+ comment). **[faithful]**
- **p431** (§6.3): book prints a capital `F'` where the lowercase `f'` is meant (F'/f' glyph slip). The
  edition keeps the printed reading faithfully (+ comment). **[faithful]**
- **p435** (§6.4, formula (6.4.3)): the 2nd argument of `α_{x'}` is printed **`U`** (capital) —
  `α_{x'}(f'/G_{x'},U,f',G_{x'},φ_{x'})` — but this slot is the *homomorphism* (the RHS `α_x(f,u,f',G,φ)`
  has `u` there), and the homomorphism for the `x'` situation is `v=p_2(u)`, explicitly defined one line
  above. `U`-for-`v` glyph slip (same F'/f'-type capitalization confusion as p431/L14016). The edition
  prints **`v`**. **[corrected]** ✓ *scan 900dpi-confirmed 2026-07-03; .tex L14035. (Rest of §6.4 —
  factorization, (6.4.4) `S_{x,ℓ^n}(...)(e)Tr_A(u_M^∨)` — matches symbol-exact.)*

### Exposé XV — *Morphisme de Frobenius et rationalité des fonctions L* (Houzel), scan p442–480

- **p462** (§3 n°1, définition de L_F): on its first mention the book writes the direct image as
  `g(F)` (no lower star) where `g_*(F)` is meant; the edition normalizes to `g_*(F)` (600dpi-zoom
  confirmed). **[normalized]**
- **p464** (bot eq): the first relation sign in `H^i_!(X̄,F̄)=R^i_!ḡ(F̄)` is a malformed/double-struck
  `=` glyph in the typescript; it denotes an ordinary equality, rendered `=` in the edition. **Not a
  book error** (typewriter rendering of `=`).
- **p465** (n°1 prop ref): `(n°1, proposition 1c))` — **spurious double `)`**. **[corrected]**
- **p466** (§3 n°2, réduction): the exponents in the double-product Leray spectral sequence
  `R^j_!v(R^i_!u(F)) ⟹ R^k_!(v∘u)(F)` are typewriter-normalized in the edition (600dpi-zoom); faithful
  in meaning. **[normalized]**
- **p472** (§3, torsion Lefschetz formula (3), LHS): the book writes the summand as `Tr(h_{(F_ν)_x})` —
  `h` subscripted by the *stalk module* `(F_ν)_x`, parallel to the book's own `h_{H^i(X,F)}` in (2″).
  The edition writes **`Tr((h_{F_ν})_x)`** (the stalk *at x* of the sheaf-morphism `h_{F_ν}`). Same
  endomorphism of `(F_ν)_x`, subscript arrangement differs. Edition normalizes to the stalk-of-morphism
  form. **[normalized]** ✓ *scan 850dpi-confirmed 2026-07-03; .tex L15140.*
- **p474** (top): the swarm tentatively read the second `Γ_X` in `h_ν = h_{RΓ_X(F_ν)}` as carrying a
  stray subscript i (X_i). The edition prints a clean `RΓ_X(F_ν)` (L15140/15159), and the surrounding
  formulas confirm `X` (not `X_i`). **Likely a scan mis-read — not a book error** (or silently normalized).
- **p475** (§3 n°3, Remarque): the text cites a **non-numbered Remarque** as "remarque 2"; the edition
  keeps the printed cross-ref faithfully. **[faithful]**
- **p476** (Lemme 3(i), mid): `est projecfif` → **`projectif`**. **[corrected]**
- **p478** (Démonstration lemme 1): `quite` → **`quitte`**. **[corrected]**

---

## Recent by-hand additions (Exposé XV + index, scan p442–484)

- **Index terminologique / des notations** (scan p481–484): the book's index numbers Houzel's final
  exposé **"XIV"** in all 11 Frobenius / fonctions-L cross-refs (correspondance de Frobenius XIV 2.1,
  fr_X XIV 1, Fr_{X/S} XIV 2, L_F(t) XIV p.21, …), while the exposé's own title page (scan p442) and
  running head print **"EXPOSÉ XV"**. Index/title mismatch for the last exposé. The edition keeps both
  faithfully (index=XIV, title=XV). **[faithful]** *(Also: index sends "rationalité des fonctions L →
  XIV 2 n°2" but the theorem is at Houzel §3 n°2 — a stale section number, index predating a
  restructuring; edition faithful.)*

---

## Systematic notational conventions of the printed typescript (not errata)

These are the book's own recurring conventions — *not* errors. The edition either keeps them faithfully
or applies a meaning-preserving typographic normalization; listed so a reader is not surprised.

- **Derived-functor `R` as blackboard-bold.** The typescript renders total derived functors `Rf_*`,
  `RΓ`, `RHom`, `Ri_*` with a double-struck / blackboard-bold `R` (looks like `ℝ`). The edition uses
  an upright roman `R`. Meaning identical. (Throughout; e.g. p286, p474.) **[normalized]**
- **Graded objects with a raised dot.** Graded rings/groups are printed with a raised-dot superscript:
  `A^•(X)`, `A^•(S)`, `A^•(P)` (Exposé VII, p289), the graded K-group `K^•` (p389), and the Godement
  complex `C^•` (p285). The edition writes `A^*`, `K^*`, `C^*`. **[normalized]**
- **`A` overloaded for a base ring.** In Bucur's exposés `A` is the coefficient algebra (`Z/nZ`, a
  `Λ_n`-algebra) but is also reused for the local ring `R` of a DVR (Exposé XII §4, e.g. `A/𝔪^r`,
  p417), recurring across the a)/b) cases. The edition keeps the printed `A`. **[faithful]**
- **`A` (crossbar) vs `Λ` (caret, no bar) — a transcription hazard, now resolved.** Bucur's typescript
  distinguishes a full-size crossbar-`A` (coefficient algebra) from a caret glyph with no crossbar
  meaning `Λ` (= `Z/ℓ^nZ`, base for group-ring / Swan constructions). Not book errors, but the draft
  edition mis-read them in **both** directions in Exposé X (fixes #41/#42/#45/#47: `Sw^Λ`,
  `Hom_{Λ[G]}`, `RHom_{Λ[G]}`, `D(A[G])`). Rule: coefficient / `A`-module contexts → `A`; pairing
  subscripts on `Sw` / `RΓ_{C'}(Λ_{U',C'})` (which are `Λ[G]`-perfect) → `Λ`. Verified correct in
  Exposé XII §6. **[resolved in edition]**
- **Citations to SGA 4 written "SGAA".** The typescript cites SGA 4 in a doubled "SGAA" form; the
  edition normalizes/preserves per a dedicated citation pass (logged in `FINDINGS.md`, edition-side —
  not a book error).
- **French prose lightly normalized — mathematics is strict.** The edition transcribes all *mathematics*
  symbol-for-symbol, but the author's *French prose* is occasionally smoothed in meaning-preserving ways:
  a parenthetical restated as a clause (p465, XV §3: book `(ē = spectre d'une clôture algébrique de 𝔽_p)`
  → edition `ē étant le spectre…`), or an archaism modernised (p408, XII §1: book `Par conséquence` — the
  edition had normalised it to `conséquent`, since restored to the book form, FIX #56). Such prose
  paraphrases are *not* individually enumerated: treat the prose as a lightly-normalised transcription and
  the mathematics as a strict one. (1000dpi-sampled 2026-07-03.) **[normalized]**

---

## To finish (next passes)
1. ✅ **Exposé I (p1–65) book errata imported** (p14 / p16 / p26 / p30 / p34×2 / p43) — transcription
   fixes (SGA→SGAA, underlines, `⊗−d`, `H→I`) correctly excluded as edition-side, not book errors.
2. ✅ **Internal `.tex` line-refs removed** (2026-07-02) — they were stale swarm-era line numbers that
   no longer match the curated edition and are meaningless for a *book* errata; page + location is the
   locator a reader of LNM 589 needs.
3. ✅ **All 7 substantive `[corrected]` mathematical entries re-zoomed 2026-07-02** — p88 / p97 / p147 /
   p150 / p170 / p277 / p390, all confirmed (book errs, edition right). Remaining: re-zoom the
   `[faithful]` entries and the minor spelling `[corrected]` fixes (lower stakes) — the honesty gap
   flagged in Provenance is now closed for the substantive corrections.
4. ✅ **Grouped by exposé** — III / IIIB / V / VI / VII / X / XII / XV subsection headers with correct
   scan-page boundaries (2026-07-02; fixed a draft mis-grouping of p208–234 as IIIB → they are Exposé V).
5. ✅ **Systematic-conventions subsection added** (blackboard `R`; raised-dot `A^•`/`K^•`/`C^•`;
   `A`-overload for a DVR ring; `A`/`Λ` glyph hazard; "SGAA" citations) — distinct from per-page errata.
6. Note on counts: this errata merges the swarm-era TYPE-B list (p77–483, ~70 entries) with the
   by-hand items (Exposé I p1–72, XV, index). The by-hand grind's own tally is 162 source-level items
   (114 book-correct + 19 corrected + 29 faithful). The two schemes count different scopes, so the
   errata's entry count and that tally are not expected to coincide.
