# SGA 6 — book-vs-edition differences (hand transcription, started 2026-07-03)

Method mirrors the SGA5 `ERRATA_LNM589.md`. Dispositions:
`[corrected]` (genuine book typo the edition fixes) · `[faithful]` (book reading reproduced) ·
`[normalized]` (meaning-preserving notation/prose/typography normalization) · `[non-error]`.

**Scope of THIS file:** it records only *book-side* differences — typos in the printed 1971 LNM 225 that
the edition corrects, plus deliberate typographic normalizations (capital-accent restoration, French
thin-spaces, `n°`→`n\textsuperscript{o}`, guillemets). It does **NOT** track transcription paraphrase/drops:
those are defects in the Codex workpass that I FIX in place to match the scan, and are logged as fixes in
`CERT_LOG.md`, page by page. Reference scan = the Internet Archive 360 dpi copy
(`theoriedesinters0225bert`).

**Global normalization conventions (applied silently, edition-standard, per SGA5):**
- capital accents the 1966–71 typewriter could not set are restored: `A`→`À`, `Ecole`→`École`,
  `Eléments`→`Éléments`, etc. `[normalized]`
- French high punctuation gets a thin non-breaking space: `~;` `~:` `~!` `~?`, and guillemets `«~ ~»`. `[normalized]`
- the numéro abbreviation `n°`/`n°s` is set as `n\textsuperscript{o}` / `n\textsuperscript{os}`. `[normalized]`
- name-pairs use en-dashes: Riemann--Roch, Borel--Serre, Lefschetz--Verdier, Atiyah--Singer. `[normalized]`
- the book's underlined emphasis (typewriter) is reproduced as `\underline{...}` (NOT italic — the book
  does not italicize; referenced titles it leaves in plain type are kept plain). `[faithful]`

---

## Front matter (Préface, Introduction) — scan idx6, idx8–10

- **Préface (idx6)** — book prints «n'a pas été **régigé**» for «rédigé» (dittography g→g). Edition: **rédigé**. `[corrected]`
- **Introduction (idx8)** — book «à **coéfficients** discrets» for «coefficients» (parasitic acute). Edition: **coefficients**. `[corrected]`
- **Introduction (idx8)** — book «un principe d'unification **extrêment** commode» for «extrêmement» (dropped syllable). Edition: **extrêmement**. `[corrected]`
- **Introduction (idx8)** — book «en dehors de la Géométrie **Algèbrique**» (grave è) for «Algébrique». Edition: **Algébrique**. `[corrected]`
  *(the first occurrence on the same page, «en Géométrie Algébrique», is correctly accented — the grave is an isolated slip.)*
- **Introduction (idx9)** — book capitalizes «Géométrie Algébrique» throughout; reproduced faithfully (the Codex workpass had lowercased it — restored to the book). `[faithful]`

*(All Introduction paraphrase deviations — dropped Hartshorne citation, paren→comma swaps, expanded
abbreviations, interpolated «le/de/du», dropped underlines — were transcription defects, now FIXED in the
`.tex` to match the scan; see `CERT_LOG.md` #7. They are not book errata.)*

## Table des matières — scan idx12–13

- **Exposé VI title** — book prints «Le K° d'un **Fibre** Projectif» (missing acute on the lowercase e) for
  «Fibré». Edition: **Fibré**. `[corrected]`
- The TdM sets exposé titles in **Title Case** and the headings as **EXPOSE N** (all caps, underlined);
  reproduced with capital-accent restoration `EXPOSE`→`EXPOSÉ`, `Eclaté`→`Éclaté`. `[normalized]`

*(The workpass's TdM had wrong page numbers for I/III/IV, lowercased every title, paraphrased the Exp VII
title, mislabelled the RRR appendix, and dropped both Index entries — those are transcription defects now
FIXED to the scan; see `CERT_LOG.md` #8. Not book errata.)*

## Exposé 0 (Esquisse) — scan idx14 (p1)

- **Intro** — book «Le présent exposé est de nature **introductif**» (masculine, for the feminine «nature»).
  Edition: **introductive**. `[corrected]`
- **§1** — book «à **coéfficients** dans $\mathbb{Q}$» (recurs, cf. Introduction). Edition: **coefficients**. `[corrected]`
- **§1, formula (1.2)** — book prints `ch_Y(f_*(cℓ(F))` with a missing closing parenthesis. Edition
  balances to `ch_Y(f_*(cℓ(F)))`. `[corrected]`
- Book notation reproduced faithfully (not errata, listed for reference): class map **cℓ** (`\cl` redefined
  `\mathrm{c}\ell`); pushforward **f_∗** with a star — used for BOTH the K-theory and the cycle pushforward
  (the workpass had rendered the K-theory one as `f_!`); **⊗_ℤ**; the product dot in (1.2). `[faithful]`
- **§1→§2 (p2), list a)** — book «Se **débarasser**» (single r) for «débarrasser». Edition: **débarrasser**. `[corrected]`
- **§2.1 (p3)** — book «définissant le **sous-schémas** fermé $X$» (plural, disagrees with «le…fermé») for «sous-schéma». Edition: **sous-schéma**. `[corrected]`
- **§2.2 (p3)** — book «lisses et **quasi-porjectifs**» (transposition) for «quasi-projectifs». Edition: **quasi-projectifs**. `[corrected]`
- **§2.2 (p3)** — book «$X$ lisse sur un **coprs** $k$» (transposition) for «corps». Edition: **corps**. `[corrected]`
- **★ CONVENTION (recurring, p3+):** the book **underlines Module / sheaf / ideal letters** in math (e.g. $\underline\Omega^1_{X'/Y}$, $\underline N_{X/X'}$, $\underline J/\underline J^2$); reproduced as `\underline{...}`. Not to be confused with underlined *prose* emphasis — same glyph, both reproduced. `[faithful]`
- **§2.2 tail (p4)** — book «(**tranformant** la classe…» (missing s) for «transformant». Edition: **transformant**. `[corrected]`
- **★ CONVENTION (p4+):** the **structure sheaf is underlined** in the book ($\underline O_Z$, $\underline O_X$…); rendered `\underline O` (NOT `\mathcal O`) for fidelity — the workpass's `\mathcal O` is converted to `\underline O` per page as the sweep reaches it. `[faithful]`
- **§3.1 (p6)** — book «l'observation qui avait **servie** de point de départ» (spurious agreement) for «servi». Edition: **servi**. `[corrected]`
- **§3.1 (p6), naive formula** — book LHS reads `f_*(cℓ^•(`**`E`**`))` while the RHS and surrounding text use `F` (`R^i f_*(F)`, «car même si F…»); the LHS `E` is a typo for `F`. **Reproduced faithfully as `E`** (math-formula glyph — reproduce + flag rather than silently alter). `[faithful — flagged typo]`
- **★ CONVENTION (p6+):** three class maps distinguished by the book — `cℓ` (plain), `cℓ_•` (covariant, into `K_•`), `cℓ^•` (contravariant, into `K^•`); reproduced with sub/superscript `\bullet`. And **long multi-line underlined emphasis** uses `\uline` (ulem, `[normalem]`); short underlines stay `\underline`. `[faithful]`
- **§3.2 (p8)** — book «identifie $X$ à un **sous-schémas** de $X'$» (plural, disagrees with «un») for «sous-schéma» (recurs, cf. p3). Edition: **sous-schéma**. `[corrected]`
- **§3.2 (p8)** — book «la classe $T_f$ **défini** par la formule» (masc., for fem. «la classe») for «définie». Edition: **définie**. `[corrected]`
- **§3.2 (p8)** — book «localement d'**insersection** complète» (transposition) for «intersection». Edition: **intersection**. `[corrected]`
- **§2.3 (p4, formula 2.3 context)** — book «combinaison linéaire des $\lambda^j$ (j**=**i)» prints `=`, but a *linear combination* requires $j\le i$ (a single term if $j=i$); the `=` is a typo (or typewriter rendering) for `≤`. Edition: **(j ≤ i)**. `[corrected]`
- **§4.1 (p10)** — book «la définition de $K^\bullet(X)$ **adopté** maintenant» (masc., for fem. «la définition») for «adoptée». Edition: **adoptée**. `[corrected]`
- **§4.2 (p10)** — book «Cette question n'a pas encore été **tiré** au clair» (masc., for fem. «question») for «tirée». Edition: **tirée**. `[corrected]`
- **§4.4 (p12)** — book «défini par l'homomorphisme **naturelle**» (fem., for masc. «homomorphisme») for «naturel». Edition: **naturel**. `[corrected]`
- **§4.5 (p12)** — book «les sections qui **précédent**» (é, noun/adj form) for the verb «précèdent» (è). Edition: **précèdent**. `[corrected]`
- **§5 (p14)** — book «[1] un homomorphisme **groupes**» (missing «de») for «un homomorphisme **de** groupes» (introducing (5.2); cf. the same phrase correctly set on p13 and in §6). Edition: **de groupes**. `[corrected]` *(1100 dpi crop: the space between «homomorphisme» and «groupes» holds no «de».)*
- **★ CONVENTION (recurring, §5 p14+):** cohomology total-degree is set with a **star** — $H^{2*}(X,\mathbb Q)$, $H^{2*}(X,\mathbb Z)$ — visibly a multi-pointed asterisk in the typescript, **distinct from the round bullet** of the K-theory grading $K^\bullet$ (both glyphs occur side-by-side in diagram (5.4), confirmed at 1000 dpi). Reproduced as `H^{2*}` vs `K^\bullet` respectively (the workpass had wrongly unified them to `\bullet`). `[faithful]`
- **§5 (p14), diagram (5.4)** — the horizontal maps are labelled with a **plain long arrow** «$x\longrightarrow \mathrm{ch}(x)\,\mathrm{Todd}(T_X)$» (typewriter had no $\mapsto$); reproduced with `\longrightarrow`, not `\mapsto`. The **vertical arrows carry no labels** in the book (they are named in the following sentence — «la première flèche verticale est la même que dans (5.3), et la deuxième est l'homomorphisme de Gysin»); the workpass's interpolated $f_*$ labels were removed. `[faithful]`
- **§5–§6 (p15)** — book «cohomologie **rationelle**» and «l'équivalence **rationelle**» (single n) for «**rationnelle**» (recurs twice on the page). Edition: **rationnelle**. `[corrected]`
- **§6 (p15)** — book «dont l'existence a été **signalé** dans 3.1» (masc., for fem. «l'existence») for «signalée». Edition: **signalée**. `[corrected]`
- **§6 (p15), (6.1)** — book prints «$\mathrm{Filt}_j\mathbf{(}\mathrm{K}_\bullet(\mathrm X)$» with an **unbalanced open parenthesis** (the two neighbouring factors $\mathrm{Filt}^i\mathrm K^\bullet(\mathrm X)$ and $\mathrm{Filt}_{j-i}\mathrm K_\bullet(\mathrm X)$ carry no such paren). Edition sets $\mathrm{Filt}_j\mathrm K_\bullet(\mathrm X)$ for balance/consistency. `[corrected]` *(750 dpi crop)*
- **★ CONVENTION (§6 p15+):** the filtration operator is set **«Filt»** (four letters), not «Fil» — confirmed 750 dpi on (6.1) and «$\mathrm{Filt}_i\mathrm K_\bullet(\mathrm X)$». The `\Fil` macro (all 236 uses) now expands to `\operatorname{Filt}`. `[faithful]`
- **§6 (p15)** — support of a coherent sheaf is set **lowercase** «$\dim\,\mathrm{supp}\,F$» in the book (not «Supp»); reproduced lowercase. And the base field here is written **capital** «$K$» («un corps de base $K$»), inconsistent with the lowercase «$k$» used in §2.2 p3 — reproduced as printed ($K$). `[faithful]`
- **§6 (p15), footnote** — the book's «cap-produit» footnote (marker «(\*)») was **entirely dropped** by the workpass; restored to the scan (text: «Cette analogie n'est d'ailleurs pas purement verbale… la structure de module sur $\mathrm{Gr}_\bullet(X)$ et l'opération “cap”.»). Marker normalised to a numbered `\footnote` (edition style). `[faithful]`
- **§6 (p16)** — book writes «jouent des rôles **duals**» (non-standard plural of the adjective «dual»; the regular form is «duaux»). **Reproduced faithfully as «duals»** — an authorial spelling, not a mechanical typo (contrast the gender-agreement slips corrected elsewhere). `[faithful]`
- **★ CONVENTION (§6 p16):** the Euler–Poincaré characteristic homomorphism is denoted **$\lambda_X$** (lambda, not $\chi$) and the structural projection **$f^X$** (not $\pi_X$): «$\lambda_X=f^X_*:K_\bullet(X)\to K_\bullet(\mathrm{point})=\mathbb Z$» (6.4). The workpass had $\pi_X/\chi_X/\pi_{X*}$ throughout — all three corrected to the book's symbols (850–1000 dpi). *(Transcription fix, not a book erratum — logged for the notation record.)*
- **§7 (p17)** — book writes «…certains raffinements (incluant…) **occupe** l'exposé XII» (singular) with the compound subject «la démonstration et certains raffinements (…)». **Reproduced faithfully as «occupe»** — a proximity/notional agreement with «la démonstration» (the parenthetical «et certains raffinements (…)» read as an aside), not a clear mechanical slip. `[faithful]` *(1000 dpi crop)*
- **★ CONVENTION (§7 p18):** the determinant functor is set **$\det^*$** (star superscript — the same asterisk glyph as the cohomology-star, distinct from the K-theory bullet), and (7.3) relates its value by a **canonical isomorphism $\simeq$**, not `=`: «$\det^*(L)\simeq\bigotimes_i\det(L_i)^{(-1)^i}$». The workpass had `\det^\bullet` and `=`; both corrected (900 dpi crops). The category names **$\underline{\mathrm{Parf}_{\mathrm{is}}}$**, **$\underline{\mathrm{Inv}}$** are underlined in (7.2) (names only, not «(X)»). `[faithful]`

## Bibliographie (Exposé 0) — scan p19 (idx32)

- **[1] Atiyah–Hirzebruch** — book prints «vol. 3, **Différential** Geometry» (parasitic acute on the English word «Differential»). Edition: **Differential**. `[corrected]`
- **Edition normalizations in the bibliography** (`[normalized]`): en-dashes for page ranges («7--38», «97--136», «5--64», «151--166») and year-spans («1957--1962»); the numéro «n\textsuperscript{o}~5» for «n° 5» ([3]); a thin space in «t.\ 86» / «vol.\ 3»; cited article/book titles set in italic (`\emph`) though the typescript sets them in plain type (edition convention, consistent with headings set bold rather than underlined). «J.-P. Serre» kept (hyphenated Jean-Pierre) though the entry prints «J.P.»; «IHES» reproduced without periods as printed ([6], where the workpass had «I.H.E.S.»).

---

## RRR Appendix (Grothendieck, «Classes de faisceaux…») — appendix-internal page numbering

- **CHAP. I §1 (app. p3, idx36)** — book «si l'**homomorphimse** additif $\lambda_t$» (m/s transposition) for «homomorphisme». Edition: **homomorphisme**. `[corrected]` *(900 dpi crop)*
- **CHAP. I §1 (app. p3), (1.10)** — book prints «$\lambda_t(\lambda^i(x))=\lambda^i(\lambda_t(x)$» with an **unbalanced open paren** (final «)» dropped). Edition balances: «$\lambda^i(\lambda_t(x))$». `[corrected]` *(850 dpi crop)*
- **CHAP. I §1 (app. p3), (1.11) 3rd line** — book prints «$\lambda^n(\lambda^i(x))=P_{i,n}(\lambda^1x,\dots,\lambda^{\mathbf n}x)$» — the last argument is $\lambda^{n}x$, whereas (1.8) writes $P_{i,n}(a_1,\dots,a_{in})$ (up to $a_{in}$). **Reproduced faithfully as $\lambda^n x$** (the workpass had silently "corrected" it to $\lambda^{in}x$); the $n$-vs-$in$ upper index is likely a book slip, but it is a math glyph, reproduced as printed. `[faithful]` *(850 dpi crop)*

- **CHAP. I §2 (app. p4, idx37), ex. 1** — book «où $\rho$ est une **présentation** extension de $\rho'$ par $\rho''$» (dropped «re-»; $\rho$ is a *representation*). Edition: **représentation**. `[corrected]` *(1000 dpi crop)*
- **★ CONVENTION (§2 p4+):** the representation Grothendieck-group is set with an **underlined K** — $\underline{K}(G)$, $\underline{K}_r(G)$ (1000 dpi crop) — the workpass had dropped the underline (plain $K$). Restored `\underline{K}` on this page; **apply on subsequent appendix pages** wherever the book underlines the representation/K-group. `[faithful]`
- **CHAP. I §2 (app. p4)** — the footnote «(\*) Il est inutile que $k$ soit algébriquement clos…» is referenced by **two** «(\*)» markers in the book (after «caractéristique 0» and after «algébriquement clos»); the edition attaches the numbered `\footnote` at the first only (the double-reference is a typographic detail not reproduced). Also «cf.(VI 3.3)» → set «cf.\ (VI 3.3)» (parens kept). `[normalized]`

- **CHAP. I §2 (app. p6, idx39), ex. 3 footnote** — book «Cf. Séminaire Chevalley 1956/58 Groupes de Lie **albébriques** (École Normale Supérieure)» (l/g swap) for «algébriques». Edition: **algébriques**. `[corrected]`
- **CHAP. I §2 (app. p6), ex. 3** — the radical of $G$ is written «isomorphe à $\mathbf{k^{*s}}$» (compact for $(k^*)^s$, an $s$-torus). **Reproduced as printed $k^{*s}$** (the workpass had expanded it to $(k^*)^s$). `[faithful]` *(crop)*

- **CHAP. I §2 (app. p7, idx40), Corollaire footnote** — book «Il faut supposer le groupe **dévisé** $G'$ de $G$» (v/r transposition) for «dérivé». Edition: **dérivé**. `[corrected]`
- **CHAP. I §2 (app. p7)** — the base of homomorphisms is indexed «$(\sigma_i)_{1\leq i\leq r''}$» (index $i$) in the running text but the Corollaire writes «en les $\rho_i$ et les $\sigma_j$» (index $j$). Both **reproduced as printed** ($\sigma_i$ in the text, $\sigma_j$ in the Corollaire — the workpass had unified them to $\sigma_j$; the text one is reverted to $\sigma_i$). `[faithful]` *(1000 dpi crop)*

- **CHAP. I §3 (app. p8, idx41)** — book «compatible avec sa **strucutre** additive» (u/t transposition) for «structure». Edition: **structure**. `[corrected]`

- **★ CONVENTION (§3 p12+, Todd operator):** Grothendieck's Todd operator is a **script / calligraphic C** («$\mathcal C$», «$\mathcal C_f$», «$\mathcal C(x)$»; «l'initiale de Todd»), a flowing cursive glyph (1100 dpi crop) — NOT the angular Fraktur $\mathfrak C$ ($\mathfrak C=\mathfrak{C}$) the workpass had used. Switched all 10 occurrences `\mathfrak C`→`\mathcal C`. `[faithful]`

- **CHAP. I §4 (app. p14, idx47), Démonstration of Théorème 1.4** — the auxiliary element is printed with **unbalanced parentheses**: «$\ell^p(N)=\underline{E}_G((\wedge(N^{(p)})^{\mathrm{alt}})$» has 3 opening vs 2 closing parens (the inner group $\wedge(N^{(p)})$ is not closed before the `alt` exponent). By analogy with the balanced (1.33) «$\underline{E}_G((\ldots)^{\mathrm{alt}})$», the edition supplies the missing paren: $\underline{E}_G((\wedge(N^{(p)}))^{\mathrm{alt}})$. `[corrected]` *(34× crop)*
- **★ CONVENTION (§4 p14+, Euler–Poincaré operator & representation ring):** on app. p14 the operator $E_G$ (alternating sum of classes / Euler–Poincaré char. in the representation ring) is printed **underlined**, $\underline{E}_G$, matching the underlined representation Grothendieck-group $\underline{K}(G)$ (crisp at 16×). The workpass had dropped both underlines ($E_G$, $K(G)$). Restored $\underline{E}_G$ (×3) and $\underline{K}(G)$ on this page; the field of fractions $K$ (no $(G)$) stays plain. `[faithful]`
- **CHAP. I §4 (app. p14), N.B.** — workpass had written the substituted classes as $\lambda^i(N),\lambda^i(F)$; the book prints the **exterior powers** $\wedge^i(N),\wedge^i(F)$ (the $G$-modules whose classes are the variables $\lambda^iN,\lambda^iF$). Corrected $\lambda^i(N)\!\to\!\Lambda^i(N)$, $\lambda^i(F)\!\to\!\Lambda^i(F)$; and the variables $\lambda^i_N,\lambda^i_F$ (spurious subscripts) → product form $\lambda^iN,\lambda^iF$ as printed. `[faithful]`
- **CHAP. I §4 (app. p14)** — «$\mathrm{Gl}(N)\times\mathrm{Gl}(F)\eqqcolon G$» uses the **defines-the-RHS** sign «$=:$» (34× crop; embedded-OCR dropped the colon and read a bare `=`); the workpass had a plain `=`. Reproduced with `\eqqcolon`. Operator glyph is the **cursive $\ell$** ($\ell^p(N)$, not $\mathscr L$) — workpass `\mathscr L^p` → `\ell^p`. `[faithful]`

- **CHAP. II §1 (app. p21, idx54), formula (2.8)** — the Chern-class condition is printed «$C^i(L(D))=0\quad(i\geq 1)$», but this is **mathematically wrong**: since $C^1(L(D))=\ell(D)\neq0$, the vanishing holds only for $i>1$. Obvious book typo ($\geq$ for $>$). **Edition corrects to $(i>1)$** (12× crop of the «$\geq$» on the (2.8) row). `[corrected]`

- **CHAP. II §1 (app. p22, idx55), Corollaire** — book «Tout élément … est **combinaisons linéaire** de composantes» (plural noun + singular adjective — agreement error) for «combinaison linéaire». 13× crop confirms the trailing «s». **Edition corrects to «combinaison linéaire».** `[corrected]`

- **CHAP. II §2 (app. p26, idx59), Corollaire 2 au théorème 2.3** — book «les fonctions **addtives** $f$ de fibrés vectoriels» (missing «i») for «additives» — the very next line has the correct «additives $g$». Edition: **additives**. `[corrected]`

- **CHAP. II §3 (app. p29, idx62), after (2.15 bis)** — book «l'homomorphisme canonique de $\underline K(\xi(X)$ dans $\underline K(X)$» — **unbalanced parens**: «$\underline K(\xi(X)$» has 2 opening «(» but only 1 closing «)» (the outer $\underline K($ is not closed). 13× crop confirms. **Edition supplies the missing «)»**: $\underline K(\xi(X))$. `[corrected]`

- **CHAP. II §3 (app. p30, idx63), $\lambda^i$-in-char-0 remark** — book prints «…que si le corps $k$ est de caractéristique $0$ (c'est la raison qui nous a empêché de démontrer le théorème de Riemann–Roch lorsque $k$ **n'est pas de caractéristique $\neq0$**)». The clause is a **double negative** — «n'est pas de caractéristique ≠ 0» literally reads «is not of characteristic ≠ 0» (i.e. char 0), the opposite of the evidently intended «lorsque $k$ est de caractéristique $\neq0$» (positive characteristic, where the sheaf-theoretic definition of $\lambda^i$ fails). Both the «≠» and the double negative are confirmed at high zoom (10× crop of «ristique ≠ 0)»). This is an **authorial slip in the 1971 printing**, reproduced **verbatim** (the edition does *not* silently emend it; the Codex workpass had "corrected" it to «caractéristique $0$», dropping the «≠» — that Codex edit is reverted to the book reading). `[faithful]`

- **CHAP. II §3 (app. p30 + p33, idx63/idx66), congruence relation sign** — the two mod-filtration congruences are set with **different relation signs in the book**: (2.18) «$\gamma(Y)\gamma(Z)=\gamma(Y.Z)\quad\mathrm{mod.}\ \underline K(X)^{i+j+1}$» uses **«=»** (2-bar, 24× crop), while (2.23) «$f^!(\gamma_Y(Z))\equiv\gamma_X(f^{-1}(Z)).\quad\mathrm{mod.}\ \underline K(X)^{i+1}$» uses **«$\equiv$»** (3-bar, 26× crop) — even though both are congruences modulo the $\gamma$-filtration. Reproduced **as printed** (=/≡ respectively); the «=» in (2.18) is a book inconsistency (or a scan-degraded «$\equiv$»), not emended. `[faithful]`

- **CHAP. II §3 (app. p34, idx67), before (2.28)** — book «si $X$ est un sous-espace algébrique de $Y$ et si $i$ est l'injection canonique **de $Y$ dans $X$**» — the direction is **transposed**: for a subspace $X\subset Y$ the canonical injection is $i:X\to Y$ («de $X$ dans $Y$»), and (2.28) $i_*(\gamma_X(F))=\gamma_Y(F)$ confirms $i$ goes $X\to Y$. Book slip (X/Y swapped), 10× crop of «de Y dans» confirms. **Reproduced as printed** («de $Y$ dans $X$»); not silently emended (the Codex workpass had "corrected" it to «de $X$ dans $Y$» — reverted to the book reading). `[faithful]`

- **CHAP. II §4 (app. p35, idx68), Prop 2.9 proof** — book «d'après la proposition 2.10, $\gamma_{X\times k}(D)-p^!(y))$ provient d'un élément…» has an **unbalanced closing paren** (stray extra «)» after $p^!(y)$; the element is $\gamma_{X\times k}(D)-p^!(y)$, as written balanced two clauses earlier «la restriction de $\gamma_{X\times k}(D)-p^!(y)$ à $U\times k$»). 10× crop confirms «p'(y))». **Edition balances to $\gamma_{X\times k}(D)-p^!(y)$** (drops the stray «)»). `[corrected]`

- **CHAP. II §4 (app. p37, idx70), Lemme 2.11 proof** — book «…dont la restriction à $U\cap V$ est **une section de $V$**» — should be «une section de **$G$**» (the subsheaf $G$ on $U$; «une section de $V$» is meaningless, $V$ being an open set). Book slip $G\to V$ (single-letter, angular «V» crop-confirmed 16×). **Reproduced as printed** («de $V$»); the Codex workpass had silently "corrected" it to «de $G$» — reverted to the book reading. `[faithful]`

- **CHAP. II §4 (app. p41 ff., idx74 ff.), spelling «grasmanienne»** — the book consistently spells the Grassmannian «**grasmanienne**»/«grasmaniennes» (one «s», one «n»), not the standard «grassmannienne». Reproduced **as printed** (the Codex workpass had "corrected" it to «grassmanniennes» — reverted to the book's spelling). `[faithful]`

- **CHAP. II §4 (app. p42, idx75), duplicate «Lemme 2.15»** — the book labels **two different lemmas «Lemme 2.15»** on the same page: (i) «Supposons que $X$ soit un produit de grasmaniennes … $G(\underline K(X))\to G(A)$ … injectif» and (ii) «Soient $X^n$ une variété projective non singulière, $Z^{n-p}$ un cycle … numériquement équivalent à zéro» (the 2nd should evidently be «2.16»). 14× crop confirms both read «2.15». **Reproduced as printed** (both «Lemme 2.15»); not renumbered. `[faithful]`
- **CHAP. II §4 (app. p42, idx75), Lemme 2.15 proof** — book «**Pour le prouver le lemme**, nous utiliserons la théorie de Chow…» — redundant «le» (either «Pour prouver le lemme» or «Pour le prouver» was intended). 9× crop confirms «Pour le prouver le lemme». **Reproduced as printed** (the Codex workpass had "corrected" it to «Pour prouver le lemme»). `[faithful]`
- **CHAP. II §4 (app. p48, idx81), formule (2.37 bis), dropped tilde** — the numerator reads «$\widetilde c(x)*\lambda_{-1}(c(N))-1$» with a **bare $c(N)$** (no tilde on the inner $c$), whereas the parallel formula (2.37) on app. p47 (idx80) writes «$\lambda_{-1}(\widetilde c(N))$» with the tilde (26× crops of both pages confirm: p47 inner $c$ tilded, p48 inner $c$ bare). The math intends the total sheaf-Chern class $\widetilde c(N)$; the typescript drops the tilde in (2.37 bis). **Reproduced as printed** (bare $c(N)$). `[faithful]`
- **CHAP. II §4 (app. p48, idx81), Remarques, «est nulle»** — book «… que le produit de leur différence par $N^q$ **est nulle**» — feminine «nulle» disagreeing with the masculine subject «le produit» (grammatically «nul»). 13× crop confirms «nulle». **Reproduced as printed** (the Codex workpass had "corrected" it to «est nul»). `[faithful]`
- **§6 (app. p49, idx82), formule (2.39) RHS, «$f_*$» for «$f_!$»** — the theorem reads «$f_*(\ch_Y(x)\,\check{\mathcal C}(Y))=\ch_X(f_*(x))\,\check{\mathcal C}(X)$» — the second membre has **$f_*$** (30× crop confirms a 6-arm asterisk subscript, identical to the LHS $f_*$), whereas both the surrounding text («les classes de Chern de $f_!(x)$», «l'homomorphisme $f_!$ de $\underline K(Y)\otimes\mathbb Q$…», 16× crop confirms the shriek «$!$») and the mathematics require the K-theory Gysin $f_!$. The typescript writes $f_*$ in the display (2.39). **Reproduced as printed** ($f_*$; the Codex workpass had "corrected" it to $f_!(x)$). `[faithful]`
- **§6 (app. p49, idx82), double period** — book «…et l'on démontre (2.39) pour chacun de ces deux **morphismes..**» — a doubled full stop (typewriter double-strike). 14× crop confirms two dots. **Reproduced as printed** («morphismes..»; the Codex workpass had a single period). `[faithful]`
- **Démonstration RRR / Références (app. p51, idx84), citation forms** — [1] book prints «Neue **topologischen** Methoden in der algebraischen Geometrie» (German declension slip; Hirzebruch's actual title is «Neue **topologische** Methoden»), 12× crop confirms the «-en» ending; [2] book prints «Ann. of **Maths.**» (with «s»), 14× crop confirms. **Both reproduced as printed** (the Codex workpass had "corrected" them to «topologische» and «Ann. of Math.»). `[faithful]`
- **Démonstration RRR / Rappel de notations (app. p52, idx85), «cylces»** — book «On note $A(X)$ l'anneau gradué des classes de **cylces** de $X$» — «cylces» (letters «l»/«c» transposed) for «cycles». 14× crop confirms. **Reproduced as printed** (the Codex workpass had "corrected" it to «cycles»); the later occurrences on the same page («cycles de codimension $i$», «cycles de Schubert») are spelt correctly in the book. `[faithful]`
- **Démonstration RRR / N.B. (app. p56, idx89), «grassmaniennes» + «obtenu»** — (i) book «sans passer par les **grassmaniennes**» (double-s, single-n-after-«ma»), 15× crop — this DIFFERS from the earlier CHAP II spelling «grasmanienne» (single-s, cf. line above): the book's Grassmannian spelling **varies** (both non-standard vs «grassmannienne»). Reproduced as printed (Codex had «grassmanniennes» double-n). (ii) «Extrait d'une lettre» opening: «soit une variété **obtenu** par éclatement» — masc. «obtenu» for fem. «variété» (grammatically «obtenue»), band4/5 crop. **Both reproduced as printed** (the Codex workpass had "corrected" to «grassmanniennes»/«obtenue»). `[faithful]`

## Exposé III (cohéreur Q, Prop 3.5) — scan p189–190 — PENDING (sweep not yet reached)

- **p190 (Prop 3.5.1, spectral-sequence abutment)**: book sets the abutment total degree with a
  heavy-asterisk superscript `E_1^{pq} ⟹ R^{*}Q(E)`; edition expands to explicit `R^{p+q}Q(E)`. Same object.
  `[normalized]` *(700 dpi confirmed on the old 118 dpi scan; re-confirm on the 360 dpi scan when the sweep
  reaches Exp III.)*
- **p189–190 (Prop 3.5, «Dans le cas général»)**: the workpass dropped an authored clause
  (`f_i:U_i→S sont des morphismes affines, ainsi d'ailleurs que…` and the `U_{i_0…i_p}=` shorthand). This is
  a **transcription drop to FIX** when the sweep reaches Exp III — not a book erratum. Tracked here only as a
  reminder; the fix will be logged in `CERT_LOG.md`.
