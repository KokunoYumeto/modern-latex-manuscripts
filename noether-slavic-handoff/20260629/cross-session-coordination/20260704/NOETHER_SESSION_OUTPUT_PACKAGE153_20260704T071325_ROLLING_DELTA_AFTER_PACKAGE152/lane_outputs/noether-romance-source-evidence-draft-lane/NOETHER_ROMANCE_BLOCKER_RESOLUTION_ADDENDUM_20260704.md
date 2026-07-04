# Noether Romance Blocker Resolution Addendum

Draft / non-canonical / not native reviewed / not approved.

This addendum continues the Romance lane after the Session C audit. It resolves four of the six audited `term_evidence_blocked_no_german_slice` rows into draft corpus prose with explicit source-bridge notes, and leaves two tensor-product rows blocked because the current best German baseline still has no responsible tensor-product source anchor.

No reviewer packet was populated. No gate ledger was promoted or overwritten. No native review or approval is claimed.

## Source Inputs

- Current best German cumulative baseline: `C:\Users\memo_\Documents\Codex\2026-06-09\could-you-look-online-for-me\work\noether-slavic-canonical\tmp\zenodo_20836874_inspect\localcodex\Noether_R124plus_LocalCodex_PostR124_Consolidated_WebDrop_20260624\tex\cum_de_R124plus_localcodex_current_candidate_20260624.tex`
- Baseline SHA256 already recorded in the Romance run log: `C0ACCB2D4EB98F54B41BC3977DFA0CB57A349C74B7B35E06453343D15ACAB4ED`
- Paper 34 German audited slice: `C:\Users\memo_\Documents\Codex\2026-06-09\could-you-look-online-for-me\work\noether-slavic-canonical\sources\paper34\Noether_Paper34_German_FINAL_AUDITED_slice.tex`
  - SHA256: `129325847A1EACF5D8C80F208BDEABB064FA8E29D92CADA6EA89CFDDD3383B3A`
- Paper 34 English audited control slice: `C:\Users\memo_\Documents\Codex\2026-06-09\could-you-look-online-for-me\work\noether-slavic-canonical\sources\paper34\Noether_Paper34_English_FINAL_AUDITED_control_slice.tex`
  - SHA256: `FF13F906A17EAD68F6293E8D4EC1F54D95282D5077EB55A6CA04BC243EF77BD9`
- Paper 34 source-fidelity original scan witness: `C:\Users\memo_\Documents\Codex\2026-06-09\could-you-look-online-for-me\work\noether-slavic-canonical\sources\paper34\source_fidelity\Noether_Paper34_Section22_ORIGINAL_SCAN_WITNESS_v001.tex`
  - SHA256: `AF7F93BC734489578F75FCFE724FE8382D57225D1BDF9C4C623592ABC5104D1D`
- Session C audit: `C:\Users\memo_\Documents\Codex\2026-07-04\noether-non-slavic-core-lane\outputs\NOETHER_SESSION_C_NONSLAVIC_TRANSLATION_COVERAGE_AUDIT_20260704.md`

## Source Discovery Decisions

- Endomorphism: the earlier blocker was caused by searching only for exact `Endomorphismus`. The German source uses `Homomorphismus-in-sich` and `Homomorphismen in sich`, while the audited English control renders the same concept as `endomorphism(s)`. This is sufficient for a draft source-bridge corpus slice.
- Maximal ideal: the German source and original scan witness use `verschiedene Primideale` in the polynomial quotient over the extension field. The audited English control renders the same passage as `distinct maximal ideals`. This is sufficient for a draft source-bridge corpus slice, but it remains flagged for specialist review because the German term is `Primideale`, not an exact `Maximalideal` compound.
- Tensor product: exact searches of the current German baseline for `Tensorprodukt`, `Tensor`, lowercase `tensor`, `\otimes`, and `⊗` returned no hits. Paper 34 also returned no tensor hits. The existing Romance sidecar supports `produit tensoriel` and `producto tensorial` as draft terminology only, not as corpus prose.

## Slice R15: Endomorphism / Homomorphism-In-Itself

Source anchors:
- German cumulative baseline `L16570-L16571`: `Homomorphismen in sich` of an Abelian group.
- German cumulative baseline `L16603`: `Eine operatorhomomorphe Abbildung ... heißt ein Homomorphismus-in-sich`.
- Paper 34 German audited slice `L96-L100`, `L129-L135`.
- Paper 34 English audited control `L96-L100`, `L129-L131`, where the same passages are rendered as `endomorphisms` and `endomorphism`.

Rows resolved in this addendum:
- `term-fr-0011`: endomorphism -> `endomorphisme`
- `term-es-0013`: endomorphism -> `endomorfismo`

Evidence note: This is a source-bridge resolution, not an exact German lexical match. The draft target term follows the audited English control and established modern mathematical register; the German source wording should remain visible to reviewers.

Unresolved flags:
- Needs specialist/native review before any canonical promotion.
- Keep first mention glossable as `endomorphisme (homomorphisme-in-sich)` / `endomorfismo (homomorfismo en sí mismo)` if a future reviewer wants to preserve Noether's historical German wording.

French draft:

**Endomorphismes et anneau des automorphismes.** Pour les homomorphismes d'un groupe abélien dans lui-même, écrit additivement, on peut définir une addition et une multiplication par
`(H+\Theta)a=Ha+\Theta a` et `(H\Theta)a=H(\Theta a)`.
Les opérations ainsi définies représentent encore des homomorphismes et appartiennent donc au même système. Ce système forme un anneau, et le groupe abélien peut être considéré comme un module relativement à cet anneau.

Une application opérateur-homomorphe d'un groupe `G` sur lui-même ou sur un sous-groupe est un homomorphisme de `G` dans lui-même, c'est-à-dire, dans le registre moderne de l'audition anglaise, un endomorphisme de `G`. Si `G` est en particulier un groupe abélien avec opérateurs, écrit additivement, et si l'on définit comme ci-dessus la somme et le produit des homomorphismes, alors les homomorphismes d'opérateurs du groupe dans lui-même forment un anneau, l'anneau des automorphismes.

L'anneau des automorphismes d'un groupe abélien simple avec opérateurs est un corps. En effet, tout homomorphisme envoie le groupe soit sur lui-même, soit sur le groupe nul; les homomorphismes qui n'envoient pas tout sur zéro sont des isomorphismes, et les applications isomorphes d'un groupe sur lui-même forment un groupe.

Spanish draft:

**Endomorfismos y anillo de automorfismos.** Para los homomorfismos de un grupo abeliano en sí mismo, escrito aditivamente, se pueden definir una suma y una multiplicación por
`(H+\Theta)a=Ha+\Theta a` y `(H\Theta)a=H(\Theta a)`.
Las operaciones así definidas representan de nuevo homomorfismos y pertenecen por tanto al mismo sistema. Este sistema forma un anillo, y el grupo abeliano puede considerarse como un módulo respecto de este anillo.

Una aplicación operador-homomorfa de un grupo `G` sobre sí mismo o sobre un subgrupo es un homomorfismo de `G` en sí mismo, es decir, en el registro moderno del control inglés auditado, un endomorfismo de `G`. Si `G` es en particular un grupo abeliano con operadores, escrito aditivamente, y si se definen como antes la suma y el producto de los homomorfismos, entonces los homomorfismos de operadores del grupo en sí mismo forman un anillo, el anillo de automorfismos.

El anillo de automorfismos de un grupo abeliano simple con operadores es un cuerpo. En efecto, todo homomorfismo envía el grupo o bien sobre sí mismo, o bien sobre el grupo cero; los homomorfismos que no envían todo a cero son isomorfismos, y las aplicaciones isomorfas de un grupo sobre sí mismo forman un grupo.

## Slice R16: Maximal Ideals / Prime-Ideal Source Bridge

Source anchors:
- German cumulative baseline `L18004`: `Das definierende Ideal wird Produkt oder Durchschnitt lauter verschiedener Primideale`.
- Paper 34 German audited slice `L1537-L1541`.
- Paper 34 source-fidelity original scan witness `L51-L55`: `\mathfrak m` becomes the product or intersection of distinct prime ideals with one zero.
- Paper 34 English audited control `L1578-L1582`: `the defining ideal is the product, or intersection, of distinct maximal ideals`.

Rows resolved in this addendum:
- `term-fr-0020`: maximal ideal -> `idéal maximal`
- `term-es-0024`: maximal ideal -> `ideal maximal`

Evidence note: This is a source-bridge resolution through the audited English control. The German text says `Primideale`; in the displayed quotient over the extension field, the listed ideals `(x_1-\xi_1,...,x_r-\xi_r)` are exactly the zero-point ideals rendered by the English control as maximal ideals. The addendum therefore supplies draft corpus prose but keeps the row review-sensitive.

Unresolved flags:
- Needs specialist review before canonical use because the German lexical surface is `Primideale`.
- Do not reuse this bridge for unrelated `Primideal` contexts; it applies only to this polynomial quotient / extension-field passage.

French draft:

**Idéaux maximaux dans la décomposition du centre.** Le groupe annulaire `Z` se compose de toutes les sommes
`\sum A_{\alpha_1\ldots\alpha_r}a_1^{\alpha_1}\cdots a_r^{\alpha_r}`,
avec coefficients dans `P`, et il est image homomorphe de l'anneau de polynômes `P[x_1,\ldots,x_r]` par l'application `x_i -> a_i`. Ainsi,
`Z \simeq P[x_1,\ldots,x_r]/(x_1^{h_1}-e,\ldots,x_r^{h_r}-e)`.

Dans le corps d'extension `Omega`, les polynômes `x_i^{h_i}-e` se décomposent en facteurs distincts. L'idéal définissant devient alors le produit, ou l'intersection, d'idéaux maximaux distincts de la forme
`(x_1-\xi_1^{(\alpha_1)},\ldots,x_r-\xi_r^{(\alpha_r)})`,
chacun correspondant à un unique zéro. À cette formation par intersection correspond une décomposition en somme directe
`Z Omega = Z_1+\cdots+Z_h`.

Spanish draft:

**Ideales maximales en la descomposición del centro.** El anillo de grupo `Z` consta de todas las sumas
`\sum A_{\alpha_1\ldots\alpha_r}a_1^{\alpha_1}\cdots a_r^{\alpha_r}`,
con coeficientes en `P`, y es imagen homomorfa del anillo de polinomios `P[x_1,\ldots,x_r]` mediante la aplicación `x_i -> a_i`. Así,
`Z \simeq P[x_1,\ldots,x_r]/(x_1^{h_1}-e,\ldots,x_r^{h_r}-e)`.

En el cuerpo de extensión `Omega`, los polinomios `x_i^{h_i}-e` se descomponen en factores distintos. El ideal definidor se convierte entonces en el producto, o la intersección, de ideales maximales distintos de la forma
`(x_1-\xi_1^{(\alpha_1)},\ldots,x_r-\xi_r^{(\alpha_r)})`,
cada uno correspondiente a un único cero. A esta formación por intersección le corresponde una descomposición en suma directa
`Z Omega = Z_1+\cdots+Z_h`.

## Tensor Product Rows Still Blocked

Rows still blocked:
- `term-fr-0008`: tensor product -> draft terminology `produit tensoriel`
- `term-es-0010`: tensor product -> draft terminology `producto tensorial`

Evidence status:
- Current best German cumulative baseline exact search: no hits for `Tensorprodukt`, `Tensor`, lowercase `tensor`, `\otimes`, or `⊗`.
- Paper 34 exact search: no hits for the same tensor patterns.
- Romance termbase/source sidecar has non-canonical target evidence only:
  - French `produit tensoriel`: 93 target-family hits in 20 local Romance evidence files.
  - Spanish `producto tensorial`: 3 target-family hits in 3 local Romance evidence files.
- The existing queue note for Spanish reported 0 exact page hits for its original checked page, so Spanish remains especially review-sensitive.

Decision:
- Do not insert tensor-product prose into the corpus translation artifact without a canon German source slice.
- Keep both rows as terminology/evidence sidecar rows with `not_reviewed` / `not_approved` status.
- If later canon/arXiv/Zenodo TeX discovery yields an actual Noether source occurrence, create a new corpus slice rather than reusing this blocker note as if it were a translation.

## Coverage After Addendum

Starting audit state for blockers:
- 6 Romance rows were `term_evidence_blocked_no_german_slice`.

This addendum changes the working draft state as follows:
- 4 rows moved to draft corpus prose via source-bridge addendum slices:
  - `term-fr-0011`, `term-es-0013`, `term-fr-0020`, `term-es-0024`
- 2 rows remain blocked with a deeper blocker ledger:
  - `term-fr-0008`, `term-es-0010`

Working Romance coverage after this addendum:
- 46 total active rows remain `not_reviewed` and `not_approved`.
- 44 row instances now have translated corpus prose or source-note prose coverage in draft sidecars.
- 2 row instances remain blocked pending a real German/canon tensor-product source slice.

