# D017 independent nonpatching cold audit: physical pages 27-51

## Verdict and scope

REPAIR_REQUIRED. All 25 physical pages, 27 through 51 inclusive, were read in both candidate language streams and compared directly with the frozen authority pixels. This is not a whole-paper PASS, a PDF layout audit, or authorization to treat inherited claims as validated. Every inherited correctness claim remains ZERO_ACCEPTED. No candidate, extraction, source master, or shared ledger was changed by this audit.

The decisive failures include the sign of the last diagonal matrix on page 27; multiplication grouping in (2.5.1.1) on page 34; and turning representation notation into an ill-typed map on page 40. French diplomatic fidelity additionally fails in the exact, page-addressed places below. Repair these in a separate candidate, retain source anomalies explicitly, then conduct a new nonpatching check of all changed passages and final PDF renderings.

## Frozen inputs and method

- Authority: `20_AUTHORITY_DELIGNE_D017_GL2_51PP_IAS_300DPI.pdf`, 51 pages; SHA-256 independently recomputed as `4E735CA05197F215F4D45CF485D45C1F646B3B1EFD1F4A4A5A399524A02E624B`.
- Frozen `cold_27_51/source_language.ndjson`: `47C913BEA2C2A5963399AC21D9C467E6CFFB3710B1C938E58352D175883F3778`.
- Frozen `cold_27_51/english_standalone.ndjson`: `29103A6C749C9044C3E86101C3431500AAC7C1639556CDE10061E68C18C603C1`.
- Reviewed field: `editable_latex`, physical pages 27-51, in both snapshots. These are copied candidate bytes, not original returned claims.
- Full authority pages rendered at 120 dpi and visually read; pages 28, 29, 34, 37, 40, 48, 51 additionally read at 200 dpi; pages 32 and 35 at 220 dpi. No repair ledger was used as a correctness oracle.
- Paper page = physical page +54. Running Del-n and centered folios remain outside scholarly body; their absence is not a coverage failure.
- This report separates semantic/math errors, diplomatic symbol changes, and source-language literal changes. English is allowed idiomatic translation, but not mathematical changes.

## Formula and mathematical-notation findings

| ID | Physical page | Languages | Exact finding and executable repair |
|---|---:|---|---|
| M01 | 27 | FR+EN | The final `La transformation` / `The transformation` matrix is **diag(1, pi^i)** in the authority, with positive i. Candidate writes pi^(-i). Change only this last transformation. The earlier direct-sum-lines matrix on the same page genuinely is diag(1, pi^(-i)). The positive exponent is consistent with the next page's support shift pi^ell to pi^(ell-i). |
| M02 | 29 | FR+EN | Before the primed matrix, authority visibly has `gamma' in [matrix]`; candidate silently substitutes `gamma' = [matrix]`. Retain `\gamma'\in` in the diplomatic transcription, and explicitly disclose the apparent source anomaly rather than silently correcting it. The first unprimed gamma genuinely uses equals. |
| M03 | 31 | FR+EN | Newform definition `v=\bigotimes_p v_p` adds lower index p absent in authority. Use `v=\bigotimes v_p`. The earlier display `V=\bigotimes_p V_p` genuinely has lower p and must not be changed. |
| M04 | 32 | FR+EN | Theorem 2.4.4 prints conductor `n/ell m < n`; candidate silently rebrackets and stacks this as n/(ell m)<n. Preserve `n/\ell m<n` in the diplomatic source. The previous paragraph genuinely contains a stacked n/(ell m). An interpretation of the slash's denominator belongs in apparatus, not an unannounced source correction. |
| M05 | 34 | FR+EN | In (2.5.1.1), authority integrand is `f( ((z,1), diag(1,a^-1)) * unipotent(u) )`: the unipotent multiplies the complete real/finite pair. Candidate groups `f((z,1),diag*unipotent)`, suggesting u acts only on the finite component. Restore the source's pair parentheses exactly. |
| M06 | 37 | FR+EN | First display `f(z;sigma)=sum a(n)e^(2pi inz)` has no lower n on sum in source; candidate adds it. Remove the index only from this first sum. |
| M07 | 39 | FR+EN | In the final decomposition of V, source places lower tau on the first direct sum only. Candidate adds tau to the second direct sum before R(tau). Remove that added lower index. |
| M08 | 39 | FR+EN | In the single sentence defining sp(n), source writes `W(bar K/K)'` with the prime after the closing parenthesis. Candidate moves it onto W. Preserve the source's exact placement here, with an apparatus note if normalizing the mathematical reading. Other occurrences correctly have W'. |
| M09 | 40 | FR+EN | In case (a), source says `la représentation W' - V^chi`, i.e. the W'-representation on V^chi. Candidate creates `W'\to V^chi`, an ill-typed group-to-vector-space map. Restore hyphen representation notation in FR; English may say `the representation of W' on V^chi`. |
| M10 | 40 | FR+EN | In Example 3.1.5, source visibly says representations of `W(bar K/K)`, with no prime. Candidate silently inserts W'. Retain unprimed source and record the apparent source inconsistency in apparatus. The preceding proof's W' is genuine and unrelated. |
| M11 | 48 | FR+EN | Initial condition uses crossed isomorphism sign: `K\not\simeq\C`. Candidate replaces it by `K\ne\C`. Restore the non-isomorphism condition. |

## French literal-source findings

These are scoped failures of the diplomatic French contract, even where the English paraphrase remains semantically sound. Formatting whitespace may change; actual words, parentheses, and semantic emphasis require a source-grounded disposition.

| ID | Page | Exact source and required disposition |
|---|---:|---|
| F01 | 29 | Restore `l'algèbre (pour le produit de convolution) des...`; candidate substitutes commas for this parenthetical. |
| F02 | 30 | Remove inserted `on obtient` between F_0(0)=1 and the recurrence. Authority proceeds directly to the recurrence. |
| F03 | 31 | Restore `avec` before c≡0 (mod n), currently omitted. |
| F04 | 31 | Preserve source emphasis on predicate `nouvelle`, `conducteur`, and `caractère`; the scholium is also underlined as a statement. Candidate has only isolated newform-name emphasis. See the general typography disposition below. |
| F05 | 32 | Restore source parenthetical `(ell, m entiers >=1, avec ell m|n; [matrix] est considéré comme dans GL(2,A^f)) avec f_{ell,m} combinaison linéaire...`. Candidate replaces this with `où`, `sont des`, `et où`, and `est`. |
| F06 | 32 | Restore `(produit scalaire de Petersson)` rather than unparenthesized words. Restore `pour ell m !=1` and `pour ell m !=ell' m'`, currently converted to bare parenthesized conditions without `pour`. |
| F07 | 32 | List (a)/(b) ends with commas, not semicolons. No comma follows C^infty in source. Preserve the original list punctuation. |
| F08 | 33 | Restore opening `(pi_f représentation de GL(2,A^f), k>=1)`; candidate substitutes `où pi_f est une représentation...`. |
| F09 | 34 | Restore parenthetical Whittaker explanation `(l'ensemble ... f_p(e)=1)`, not inserted `c'est-à-dire`. Restore `(au même sens)` rather than comma-delimited wording. |
| F10 | 35 | Restore `Supposons f de niveau N (ou divisant N). f est alors déterminée...`; candidate changes this to comma phrasing and starts `Alors f est déterminée...`. |
| F11 | 35 | Restore `avec` before a_0∈(Z/NZ)*, currently omitted. |
| F12 | 36 | Source has `sous-groupes unipotent inférieurs`, singular unipotent; candidate silently changes to plural `unipotents`. Preserve source grammar. |
| F13 | 36 | Restore `le vecteur de V_p qui`; candidate omits `de V_p`. |
| F14 | 36 | Restore normalization parenthetical `(on normalise v_p(x) ... v_p(1)=1)`, currently changed to a semicolon clause. |
| F15 | 36 | Final source says `V est déterminé`, not `V est déterminée`. |
| F16 | 37 | Restore `(indépendant de sigma)`, the parenthetical valuation explanation beginning `(nu_p désigne...)` rather than inserted `Ici`, and terminal `(traduction de 2.5.6)`. |
| F17 | 37 | Remove inserted `alors:` before list (a)-(c). |
| F18 | 38 | Source `consiste en` has no added colon. Restore parenthetical `(triviale sur un sous-groupe ouvert du groupe d'inertie I)` in (a), and `(normalisé pour transformer Frobenius géométriques en uniformisantes)` in the class-field sentence. |
| F19 | 38 | Restore `(ell != p)` after Q_ell rather than comma-delimited condition. |
| F20 | 39 | Basis condition is source `e_i(0<=i<n)` and the N-action condition is `(0<=i<n)`, not comma-delimited or inserted `pour` wording. Preserve the printed endpoint n even though the next equation separately gives N e_(n-1)=0. |
| F21 | 40 | Restore `(mais non K)`, `(limitée à p)`, `(ou profini)`, `(ou V^chi)`, and case (a)'s final `(W' est de la forme ...)`. Candidate replaces these with commas/semicolon and inserts `de` before V^chi. |
| F22 | 41 | Source says `tel que pi([a 0;0 a]) soit omega_pi(a). : on a`; candidate silently replaces `soit` with an equality sign and capitalizes/separates the next sentence. Keep literal prose and disclose unusual source punctuation if normalizing its presentation. |
| F23 | 42 | Restore `(en fait, déjà par (E))`; candidate turns this into comma prose and omits source comma after `fait`. Source explanatory label in (A)(3) begins capital `Automorphismes` and uses nested `(cf. 3.2.2.1)`; candidate lowercases and rewrites punctuation. |
| F24 | 43 | Restore `(induction unitaire)` rather than comma prose. Definition uses equals with subscript `dfn`, not `:=` with an extra colon. Preserve `(d^*g est une mesure de Haar sur GL(2,F))`, not substituted `où`. Heading is printed `Equation`, without capital accent. |
| F25 | 44 | Restore `(intégrale définie par prolongement analytique en s)` rather than inserted `l'intégrale étant...`. Heading is printed `Equation`, without capital accent. |
| F26 | 46 | Restore entire `(Pour dx quelconque, multiplier le membre de droite par dx/dx')` parenthetical. Source heads `(C) (Induction) devient:` and `(D) (Représentations dégénérées) devient:`; candidate inserts `Cela` and changes the grouping. |
| F27 | 48 | Restore `(de dimension finie)` rather than comma phrasing in the correspondence description. |
| F28 | 49 | Restore `(équations fonctionnelles de Tate et de Hecke)` rather than comma phrasing in 3.2.9.3. |
| F29 | 50 | Restore `(voir par exemple [2])` rather than comma phrasing. Keep duplicated source label 3.2.9.8, source singular `les représentation`, and `constituents` unchanged. |
| F30 | 51 | Bibliography typography/punctuation needs an explicit disposition: original volume numbers are underlined, not bold; titles are not newly italicized. Source [1] has no comma after `(1970)`; source [13] has no comma after `317`. Do not introduce bibliographic normalization without marking it as such. |

## General typography disposition

The authority repeatedly underlines theorem/proposition/corollary statements and defined terms on pages 27-29, 31-33, 35-37, 39-40. The candidate generally reduces these to bold paragraph labels with ordinary statement bodies. A modern reader may consistently map typewritten statement underlining to theorem-body italics and term underlining to emphasis, but that mapping must be explicit and actually implemented, not silently omit every semantic font distinction. Full-page source witnesses preserve the original visual form but do not by themselves explain a missing semantic distinction in the editable diplomatic edition.

## Per-page audit coverage and notable non-findings

| Page | Result of this pass |
|---:|---|
| 27 | Entire theorem, proof, matrices and EN read; M01. Earlier negative-i direct-sum matrix is correct and must remain. |
| 28 | Entire page and EN read; no additional substantive formula/translation failure identified. Source singular `les restriction` is preserved; support shift and both intersection signs agree. |
| 29 | Entire page and EN read; M02/F01. Character factors alpha(a')^-1 beta(d')^-1 and right-coset matrices agree. |
| 30 | Entire page and EN read; F02. Script function-space glyph is A^0(k), not G^0(k); candidate mathcal A^0 is supported. Recurrence and generating function agree. |
| 31 | Entire page and EN read; M03/F03-F04. Character omega(a), c-congruence, and inverse-gamma argument agree. |
| 32 | Entire page and EN read; M04/F05-F07. Source visibly has omega(-1)=k, not (-1)^k; do not silently repair it. The slash denominator letter after ell is m, not n. |
| 33 | Entire page and EN read; F08. Both action formulas, completion subgroup, and induced representation statement agree. |
| 34 | Entire page and EN read; M05/F09. Fourier signs and primed K/W notation otherwise agree. |
| 35 | Entire page and EN read; F10-F11. Higher-resolution check confirms integration region 1/M, not 1/N. EN `First` plus p36 `of all` correctly translates split `Tout d'abord`. |
| 36 | Entire page and EN read; F12-F15. Source p-in-S wording in proof is preserved, not silently corrected by inference. |
| 37 | Entire page and EN read; M06/F16-F17. Product of local coefficients, p^k T_p, and Euler-factor polynomial agree. |
| 38 | Entire page and EN read; F18-F19. W'/nilpotent relation, Frobenius 1/q, and omega_n(x)=omega(x)^n agree. |
| 39 | Entire page and EN read; M07-M08/F20. Nilpotent endpoint condition n is preserved despite apparent source anomaly. |
| 40 | Entire page and EN read; M09-M10/F21. Jordan decomposition and induced/quadratic cases otherwise agree. |
| 41 | Entire page and EN read; F22. Central-character identities, dual twist and Kirillov-space relation agree. |
| 42 | Entire page and EN read; F23. Pairing sign v_2(-x), functoriality source pi without subscript on (A)(1) RHS, and discrete-series equivalences agree. |
| 43 | Entire page and EN read; F24. Real/complex degenerate formulas, including visible negative m, and Fourier definition agree. |
| 44 | Entire page and EN read; F25. Transposed Z, duals, half-twists and Hecke integrals agree. |
| 45 | Entire page and EN read; no additional formula/translation failure identified. All conductor shifts, q^(-n/2), t^(nd), and Tate correspondence twists agree. |
| 46 | Entire page and EN read; F26. Source label 5.2.3.1 and 5.2.6, product chi_1 omega_1(a), negative m, and missing g in final source matrix expression are preserved as printed rather than silently repaired. |
| 47 | Entire page and EN read; no additional formula/translation failure identified. The Weyl operator w phi, dx'/dx, conductor shift and H_1(E,Z_ell)=T_ell(E) agree. |
| 48 | Entire page and EN read; M11/F27. H1-H3, conductor, character-sign and formal-degree statements agree. |
| 49 | Entire page and EN read; F28. First L denominator correctly uses unprimed dual pi as in authority; second functional equation has minus epsilon. |
| 50 | Entire page and EN read; F29. Both occurrences of label 3.2.9.8 and exceptional Q_2 paragraph are retained. |
| 51 | All 16 bibliography entries [1]-[15] including [9 bis] read in both streams; F30. Intentionally incomplete P. Cartier [2] is preserved. Reprecht and Kajdan source spellings are retained. |

## English semantic assessment

No independent English-only substantive translation failure was identified in the 25-page scope beyond the shared mathematical/notation changes enumerated above. This is not a PASS: M01, M05 and M09 affect mathematical meaning, and source anomalies must be distinguished from editorial corrections. The split sentence across pages 35-36 was explicitly rechecked and is correct. Source typography and final rendered reader layout require the parent's separate fresh review.

## Next executable action

Repair the eleven numbered mathematical/notation findings and thirty literal-source finding groups in a new candidate, with explicit dispositions for source anomalies and semantic typography. Rebuild FR and EN PDFs, then cold-check changed passages and rendered mathematical objects without patching during that audit. Do not mark this audited snapshot PASS or publish it as a passed corpus candidate.
