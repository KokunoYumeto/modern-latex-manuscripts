# Cumulative methodology and special-character translation aid - ES/JA Noether lane

Superseding scope note: this file is cumulative through Paper 30 complete. It incorporates earlier cumulative guidance and the Paper 30 ideal-theory addendum below.

# Cumulative methodology and special-character translation aid - ES/JA Noether lane

This file is cumulative for the Spanish/Japanese Noether lane through Paper 23 complete.

## Packaging and workflow

Use one outer ZIP, one root folder, then subfolders. Keep standalone chunk TeX/PDF, cumulative TeX/PDF, German source, English control, render checks, logs, glossary deltas, and audit notes in their named subfolders. Do not replace hard formulas, tables, or diagrams with screenshots; preserve editable TeX whenever possible. When a source formula looks odd, preserve it and record the issue instead of silently normalizing.

## Engines

Spanish: `pdflatex` with T1/UTF-8 and `babel` options `spanish,es-noquoting,es-noshorthands`.

Japanese: earlier packets used `lualatex` with `jlreq`/`luatexja`. This packet ships Japanese chunk and cumulative PDFs built with `xelatex` + `xeCJK` + `Noto Serif CJK JP` because the local LuaHBTeX/luaotfload run did not complete reliably during this session. The Japanese TeX is UTF-8 and is intentionally simple enough for local Codex to port back to the previous LuaLaTeX style if that environment is stable.

## Core macros currently in use

`\Kfield=\mathfrak{K}`, `\Ssys=\mathfrak{S}`, `\Mfield=\mathfrak{M}`, `\Lsys=\mathfrak{L}`, `\Jdom=\mathfrak{J}`, `\Gdom=\mathfrak{G}`, `\Hgrp=\mathfrak{H}`, `\Omegaint=[\Omega]`, `\eps=\varepsilon`, `\GaloisRes=\Phi`, `\Deltaop`, `\Omegaop`.

## Special-character policy

Keep diacritics in proper names: Lüroth, Castelnuovo, Enriques, Hilbert, Steinitz, Kronecker, König, Mertens, Galois, Lagrange, Clebsch--Gordan, Capelli, Deruyts, Fischer, Zermelo. Do not strip accents in Spanish prose. Japanese output should keep Latin names in roman script unless the established mathematical convention requires otherwise.

Preserve Noether's historical notation, including colon quotients such as `F(x):G(x)`, prime-marked theorem labels such as `V$'$`, congruence notation, bracketed determinant conventions, and compact operator notation such as `\Omega`, `\nabla`, and polarizing operators.

## Cumulative terminology locks through Paper 08

`lineare Schar` -> ES `familia lineal` / JA `線形族`.
`Integritätsbereich` -> ES `dominio íntegro` / JA `整域`.
`relativ-ganzer Bereich` -> ES `dominio relativamente entero` / JA `相対的整領域`.
`Bereich erster Art` -> ES `dominio de primera especie` / JA `第一種の領域`.
`Involutionsform` -> ES `forma de involución` / JA `インボリューション形式`.
`Involutionsbasis` -> ES `base de involución` / JA `インボリューション基底`.
`Integritätsbasis` -> ES `base íntegra` / JA `整基底`.
`reguläres System` -> ES `sistema regular` / JA `正則系`.
`ganzzahlig` -> ES `entero` or `con coeficientes enteros` by context / JA `整数係数` or `整数上整` by context.
`algebraisch-ganz` -> ES `algebraicamente entero` / JA `代数的に整`.
`Übertragungsprinzip` -> ES `principio de transferencia` / JA `転移原理`.
`Resultante` -> ES `resultante` / JA `終結式`.
`Grundpunkt` -> ES `punto fundamental` / JA `基本点`.
`Gattungsbereich` remains italicized as a historical German named concept.
`ganze rationale Funktion` -> ES `función racional entera` / JA `整有理関数`.
`ganz rational` -> ES `racional entero` / JA `整有理`.
`Grundform` -> ES `forma fundamental` / JA `基本形式`.
`Polarprozess` -> ES `proceso polar` / JA `極化過程`.
`vollständiges System` -> ES `sistema completo` / JA `完全系`.
`Potenzsumme` -> ES `suma de potencias` / JA `冪和`.
`Reihenentwicklung` -> ES `desarrollo en serie` / JA `級数展開`.
`Galoissche Resolvente` -> ES `resolvente de Galois` / JA `Galois resolvent` or `ガロアのレゾルベント` where prose needs explanation.

## Source anomaly policy

Do not silently normalize source anomalies. In earlier Paper 06, preserve and flag: §11 formula (6) with `A_\tau(G_i(x))`; §12 `in inf.`; and the `Gattungsbereich` term. In Papers 07-08, no hard table or diagram gaps were encountered; the main fidelity risks are compact operator formulas, determinant-combination notation, and the German distinction between `ganz rational`, `ganzzahlig`, and ordinary rationality.

## Paper 09 update - complete through Paper 09

Paper 09 introduces the terminology of integral transcendental-number domains and the abstract extension to arbitrary fields. Maintain the historical distinction among `ganz`, `algebraisch-ganz`, `ganz rational`, `rational gebrochen`, and `algebraisch gebrochen`; do not flatten these to a single modern word for integral. Spanish uses `entero`, `algebraicamente entero`, `racionalmente fraccionario`, and `algebraicamente fraccionario` according to context. Japanese uses `整`, `代数的に整`, `有理的に分数的`, and `代数的に分数的`.

For Paper 09, `Bereich` was translated chiefly as Spanish `dominio` and Japanese `領域`; where the integral-domain structure is explicit, Spanish `dominio íntegro` and Japanese `整域` are used. `Zahl` remains `número` / `数` in the original complex-number setting, while `Größe` in §10 becomes `cantidad` / `量` when the discussion passes to arbitrary fields.

The notational family `\mathfrak G`, `\mathfrak H`, `\mathfrak M`, `\mathfrak L`, and `\mathfrak R` is preserved. The basis symbols `H`, `\eta`, `\xi`, `\vartheta`, and `\Theta`, indexed roots such as `\sqrt[\nu]{}` and `\sqrt[\sigma]{}`, and congruence notation `\pmod{...}` remain editable TeX. The source/control phrase `in inf.` in §5/§9 was preserved rather than silently modernized.

Packaging remains one outer ZIP, one root folder, then subfolders. Root-level metadata is placed under `00_README_FOR_CODEX/` and `06_manifest/` so extraction does not clutter the top level.


## Paper 10 additions: functional equations of the isomorphic mapping

Paper 10 introduces a compact terminology cluster around field isomorphisms and wild solutions of Cauchy-type functional equations. Preserve the historical distinction between `eindeutig` (single-valued/unívoco/一価), `eineindeutig` (one-to-one/biunívoco/一対一), and `umkehrbar eindeutig` (bijective/一対一対応). Avoid replacing Noether's wording by later category-theoretic terminology unless the sentence explicitly calls for it.

Notation needing stable treatment: `\Theta` is the rational basis; `\vartheta` is an element of that basis; `\mathfrak K(\vartheta)` is the segment field/cuerpo de segmento/切片体; `H`, `Z`, `\eta`, and `\zeta` encode the algebraic bases and their corresponding image basis. Retain all these symbols.

For §4, keep the real-coordinate convention `z=x+iy`, `f(z)=X+iY`, and the scan-corrected determinant with rows `(x_1,...,x_4)`, `(y_1,...,y_4)`, `(X_1,...,X_4)`, `(Y_1,...,Y_4)`. The rank-three exclusion uses `c_3(X-x)+c_4(Y\mp y)=0` and then `(Y\mp y)=c(X-x)`; do not revert to OCR variants with `c_1,c_2` at this point.

The phrase `extrem unstetig` is rendered as `extremadamente discontinuo` in Spanish and `極端に不連続` in Japanese. This is Hamel/Noether terminology and should be preserved consistently.


## Paper 11 additions: equations with prescribed group

Paper 11 introduces old Galois-theory terminology around equations with prescribed group. Translate `vorgeschriebene Gruppe` as ES `grupo prescrito` and JA `指定された群`. Preserve `Affekt` as a historical technical term: Spanish uses `afecto`, Japanese keeps `Affekt` in roman script. `affektlose Gleichungen` is therefore ES `ecuaciones sin afecto` and JA `Affekt をもたない方程式`, not a modern substitute.

The invariant field notation is kept as `\Omega_\Gamma`; this follows the source scan and avoids OCR variants such as `\mathfrak B_r`. The elementary symmetric functions are `\sigma_i(x)`, not `\theta_i(x)`. Parameters are lowercase `\lambda_i`, as in the scan. Formula (11) visibly has `G'_k(x)/H_k(x)` in the fractional expression and `G_k(x)` after multiplication; this apparent prime/no-prime asymmetry is preserved and flagged rather than normalized.

For the Tschirnhaus reduction footnote, preserve the source's substitution `y=x a_2/a_3` and the repeated coefficient `a_2^3/a_3^2` in the two terms `y^{n-2}` and `y^{n-3}`. The source scan was used as authority over later OCR snippets.

## Paper 14 cumulative addition

Paper 14 centers on the comparison of algebraic functions of one variable with number-field theory and with the Riemann, Weierstrass, Brill--Noether, Dedekind--Weber, and Hensel--Landsberg frameworks. Maintain a deliberately historical register: Spanish `polígono (divisor)` and Japanese `多角形（除数）` for `Polygon`, Spanish `corresidual` and Japanese `余剰対応` for residual correspondence, Spanish `conductor` and Japanese `導手` for `Führer`, and Spanish `diferente / ideal de ramificación` and Japanese `異なるもの / 分岐イデアル` according to local mathematical context.

When appending Paper 14 to cumulative TeX, include the local macro-support block for `\frS`, `\frp`, `\fra`, `\frb`, `\frc`, `\frf`, `\frr`, `\frm`, `\frD`, `\calA`, `\calB`, `\calN`, and `\p`. Use `\providecommand` only.



## Paper 15 update - integral invariants of binary forms
Paper 15 fixes the invariant-theory terminology around finite bases of integral invariants. Keep `ganzzahlig` context-sensitive: ES `entero`, `con coeficientes enteros`, or `coeficientes enteros racionales`; JA `整数係数`, `整係数`, or `有理整数係数`. Preserve Fraktur module notation (`\frM`, `\frN`, etc.) and determinant shorthand `(ik)` as source notation.

## Paper 16 update - series expansion in form theory
Paper 16 is a compact correction-and-specialization paper. Its main terminology locks are `Reihenentwicklung` -> ES `desarrollo en serie` / JA `級数展開`, `Formentheorie` -> ES `teoría de formas` / JA `形式論`, `Normalform` -> ES `forma normal` / JA `正規形`, `Polarprozess` -> ES `proceso polar` / JA `極化過程`, and `Modulbasis` -> ES `base de módulo` / JA `加群基底`.

Preserve formulas `(1)`--`(10)` and `(2a)` as editable TeX. In formula (5), keep the operator order `S=AB`, `B` then `A`, rather than rewriting it as a modern projection. In formula (7), keep the mixed sequence `\Omega\Delta\Omega\cdots\Delta\Omega`. The corrections section belongs to Paper 16 proper and must be translated, not omitted as back matter.

For Japanese, the term `形式` is used for `Form` in the invariant-theory sense, not `型`; `正規形` is retained for `Normalform`. For Spanish, use `forma`/`forma normal`, not `formulario` or `normalización`.

## Paper 17 §§1-4 update

The Paper 17 opening introduces the main noncommutative module vocabulary. Preserve `Restklasse` as `clase residual` / `剰余類` and `Restgruppe` as `grupo residual` / `剰余群`. Keep the right-sided module convention explicit; do not normalize it into commutative ideal terminology. The Fraktur letters for modules, residue classes, and subgroups remain editable TeX macros rather than images.

---

# Paper 17 §§10-12 and Paper 18 method and special-character note

Scope: Paper 17 §§10-12 complete and Paper 18 complete in Spanish and Japanese. This completes the Spanish/Japanese cumulative translation through Paper 18.

Source basis: the Batch26 German source/control TeX and PDF, the corresponding English control, and the scan slice `Noether_Paper17_sections10_12_and_Paper18_SOURCE_SCAN_collected_pdf_pages354-367_printed_pp340-353.pdf`. The German source remains controlling; the English control is used only as a sense witness and a guard against omissions.

Retroactive title standardization: the new cumulative Spanish/Japanese outputs update Paper 17's displayed title to include both `Differential- und Differenzenausdrücke`. Spanish now reads `expresiones diferenciales y de diferencias`; Japanese now reads `微分式および差分式`. This follows the Batch26 title and is clearer for the full paper. It does not change formulas or theorem content.

Paper 17 §§10-12: preserve the noncommutative module language from §§1-9. `Restgruppe` remains `grupo residual` / `剰余群`; `vollständig reduzibel` remains `completamente reducible` / `完全可約`; and `von gleicher Art` remains `del mismo tipo` / `同種`. The sequence of Theorems VIII-XII is retained, and formulas (31)--(44) remain editable TeX.

Paper 18: use `forma resultante` / `終結式形式` for `Resultantenform`. The abstract ideal-theory terms are translated as `ideal primario` / `準素イデアル` and `factor primario` / `準素因子`; avoid Japanese `一次イデアル` here, because the intended algebraic term is primary, not linear. Preserve the bracket decomposition `[\mathfrak Q,\mathfrak Q_1,\ldots,\mathfrak Q_r]=[\mathfrak Q,\mathfrak L]` as editable TeX.

No tables or diagrams occur in this scope. No formulas were converted to images, and no source-visible footnotes were omitted.

## Paper 19 introduction--§5 update


Scope: Paper 19, `Idealtheorie in Ringbereichen`, from the title and introduction through \S 5 inclusive. The packet stops before \S 6. Later sections \S 6--\S 12 are not represented as translated body text in this packet, though the source scan for the full paper is included for continuity.

Terminology policy for this block: `Ringbereich` is rendered as Spanish `dominio de anillos` and Japanese `環領域`; `Integritätsbereich` in the opening transfer statement is rendered as Spanish `dominio íntegro` and Japanese `整域`. The latter is a deliberate algebraic-domain standardization for Paper 19; earlier cumulative helper files may contain the less idiomatic `dominio íntegro` / `整域` in older contexts.

Formula policy: least-common-multiple notation `[A,B]`, greatest-common-divisor notation `(A,B)`, congruences `f\equiv0(\ideal M)`, and fraktur ideal letters are preserved as editable TeX. The English control text has a formula-sensitive defect in the \S 2 footnote (`\lambda gtr 2`); the German source reading `\lambda\ge2` is used in Spanish and Japanese.

No tables or diagrams occur in the completed block. No translation gaps are declared for the introduction through \S 5.


## Paper 19 part 2 update

# Paper 19 part 2 methodology note

Scope: Paper 19, §§6--12, completing `Idealtheorie in Ringbereichen`.

Terminology:
- `relativprim` is directional in Definition V and is translated as Spanish `relativamente primo respecto de` and Japanese `に対して相対的に素`.
- Mutual `gegenseitig relativprim` remains distinct from `teilerfremd`; the latter is reserved for gcd equal to the unit ideal in §8 and is translated as Spanish `coprimo`, Japanese `互いに素`.
- `Doppelbereich (Σ,T)` is rendered as `dominio doble` / `二重領域`.
- Matrix `Klassen` in §12 are kept as classes/類, with Fraktur capitals preserved.
- All divisibility and congruence statements are preserved in source notation `\equiv0(\ideal A)` or `\eqzero{\ideal A}` rather than converted into subset notation.

Source/control policy:
- The German and English control excerpts use the paper-level TeX for §§6--12.
- Batch-tail helper commands after §8 and the final `\end{document}` in the cumulative control source were not treated as source text.
- Source scan excerpt is pages 22--43 of the Paper 19 scan, corresponding to §§6--12.

Build/packaging:
- Strict one-ZIP/one-root-folder/subfolders-only layout.
- Internal path names intentionally shortened for Windows path-length safety.


---

# Method note: Paper 20-21 Spanish/Japanese continuation

Scope completed: Paper 20 complete and Paper 21 complete. The German Batch 30 source/control files and the English control files were retained, with the source scan sidecar included for local checking.

Faithfulness policy: all formulas, footnotes, dates, titles, and numbered displays are preserved as editable TeX. No diagrams or hard mathematical material were replaced by screenshots. No translation gaps are declared.

Global optimization pass: the cumulative Japanese TeX contained one pre-existing long display alignment in the Paper 21 range. It was rewritten as an `aligned` display with the same mathematical content to remove an overfull box in the cumulative build. This is a layout-only cumulative optimization.

Terminology optimization: `endliche Gruppe mit \rho wesentlichen Parametern` is treated in Lie's finite-parameter sense, not as a finite abstract group. Spanish uses `grupo de parámetros finitos con \rho parámetros esenciales`; Japanese uses `\rho 個の本質的パラメータをもつ有限パラメータ群`.

Path policy: file and directory names were kept short for local Codex/Windows path safety while retaining human-readable structure.


---

# Paper 22 methodology note

Scope: Paper 22 complete, `Bearbeitung von K. Hentzelt: Zur Theorie der Polynomideale und Resultanten`, in Spanish and Japanese. The continuation uses both source batches: the introduction through §3/Satz VI and §§4--7 complete. The German source is controlling; the English translation is a sense witness and omission guard.

Title optimization: to avoid the ambiguity that Hentzelt authored the revision, the Spanish title is `Reelaboración de un trabajo de K. Hentzelt`, and the Japanese title is `K. Hentzelt の論文の改作`. This is a wording optimization only; the German title and bibliographic meaning are unchanged.

Terminology: `Polynomideal` is `ideal de polinomios` / `多項式イデアル`; `Resultantenform` is `forma resultante` / `終結式形式`; `Grundmodul` is `módulo fundamental` / `基本加群`; `Grundideal` is `ideal fundamental` / `基本イデアル`; `Elementarteiler` is `divisor elemental` / `初等因子`. `Divisor` is kept in the algebraic divisibility sense, not the geometric-divisor sense.

Formula policy: formulas (1)--(36), all named definitions and theorems I--XIII, the Dedekind quotient of modules, the norm notation `N(G|A)`, the explicit decomposition of `ar R^{(i)}(z,x)`, and all source footnotes are preserved as editable TeX. No formula was converted to an image.

Global optimization check: this packet adds Paper 22 terminology and symbol policies to the cumulative methodology aids, but does not alter earlier translated paper text except through normal cumulative appending. Internal package paths remain short for Windows/Codex path safety.


---

# Paper 23 methodology note

Scope: Paper 23, `Algebraische und Differentialvarianten`, complete in Spanish and Japanese.

The German source/control TeX and scan witness were used as the governing source set. The English control was used only to stabilize sense in long technical sentences. All numbered formulas (1)--(5), footnotes, and bracketed differential-invariant symbols `[\Omega_i]`, `[\Omega_i^{(1)}]`, `[\Omega_i^{(2)}]` are retained as editable TeX.

Global refinement applied in the new cumulative TeX: older wording `dominio de integridad` / `整性領域` was standardized to `dominio íntegro` / `整域`, and `base de integridad` / `整性基底` to `base íntegra` / `整基底`. This affects wording only, not formulas or paper order, and is intended to keep the Spanish/Japanese lane coherent for later algebraic-number-theory integration.

Terminology:
- `Algebraische und Differentialvarianten` is rendered by mathematical sense as `Invariantes algebraicos y diferenciales` / `代数不変式と微分不変式`.
- `Übertragung`, in the Weyl--Schouten setting, is rendered as `conexión (transmisión)` / `接続（伝達）`.
- `cogredient` is rendered explicitly in Japanese as “following the same linear transformation law” to avoid ambiguity with later covariance terminology.

---

# Paper 24 p1 methodology note

Scope: Paper 24 title/introduction through §3 inclusive. The next source point is §4.

Source policy: German Batch34 and the source scan for collected pages 458--477 / printed pages 444--463 are controlling. English Batch34 is a sense witness and omission guard.

Translation policy: definitions, theorem labels, lemmas, all displayed formulas, and all footnotes remain editable TeX. No formula, table, or diagram substitute was used.

Terminology focus: elimination theory is linked with general ideal theory through norms, elementary-divisor forms, prime/primary ideals, residue-class bodies, and zero bodies. The terminology in `gloss_p24p1.csv` is intended to be reused in later Takagi/algebraic-number-theory integration.

Global refinement: the cumulative output keeps the earlier standardization to `dominio íntegro` / `整域` and `base íntegra` / `整基底`. No additional older-paper rewrite was required in this pass.

Build/path policy: package paths are short and Windows/Codex-safe; standalone and cumulative translation logs have no overfull/underfull reports.


## Paper 24 complete update
Paper 24 complete was added. Keep elimination-theory terminology coherent with Papers 19, 22, and 23. Absolute-prime and reduction-modulo-prime terminology should be reusable for later algebraic-number-theory integration.


## Papers 25--29 complete update

Papers 25--29 were added in one package. This block is short but important for coherence: it closes the elimination-theory bridge after Paper 24, then records short ideal-theory notices and Noether's finite-invariant theorem in characteristic p. The cumulative methodology has been corrected to use the Paper 24-complete branch rather than the earlier Paper 24 part-1 branch.


# Method note - Paper 30

Paper 30, `Abstrakter Aufbau der Idealtheorie in algebraischen Zahl- und Funktionenkörpern`, is translated as a single completed paper in the cumulative branch. The new continuation work in this package is §§6--10; the package also includes a complete standalone Paper 30 built by combining the previously checked §§1--5 translation with the new §§6--10 translation.

Global-coherence decision: the cumulative files are built from the checked Papers 25--29 cumulative branch before appending complete Paper 30, rather than from the older partial Paper 30 branch, to avoid regression in Paper 24--29 wording and page structure.

Terminology policy for future Takagi/algebraic-number-theory integration:
- `Teilerkettensatz`/`Teilerkettenbedingung`: Spanish `condición de cadena de divisores`; Japanese `約イデアル鎖条件`.
- `Vielfachenkettensatz`/`Vielfachenkettenbedingung`: Spanish `condición de cadena de múltiplos`; Japanese `倍イデアル鎖条件`.
- `Doppelkettensatz`: Spanish `doble condición de cadena`; Japanese `二重鎖条件`.
- `teilerfremd` is ordinary coprimality (`coprimo` / `互いに素`); directional `prim zu` remains `primo respecto de` / `に対して素`.
- `Einheitsideal` and `Einselement` are kept distinct: `ideal unitario` / `単位イデアル` versus `elemento identidad` / `単位元`.
- `Kompositionsreihe` in §10 is rendered as `serie de composición` / `組成列`; it is not silently modernized into subgroup-series language.

---

# Paper 31 methodology note

Scope: Paper 31 complete, `Der Diskriminantensatz für die Ordnungen eines algebraischen Zahl- oder Funktionenkörpers`, in Spanish and Japanese. The translated range includes title/front matter, introduction, §§1--8, final location/date, all source-visible footnotes, and all displayed formulas.

Source/control policy: the German source was split across the Batch40 intro/§§1--2 file and the Batch41 §§3--8 completion file. For this package the split was recombined into one German control excerpt and one English control excerpt. The scan witness is the full Paper 31 page slice, pp. 82--104. The split continuation heading and footnote reset are not treated as source text in the Spanish/Japanese standalone or cumulative outputs.

Terminology: Spanish uses `teorema del discriminante` and masculine `el discriminante`, which is the idiomatic mathematical gender and is recorded as a retroactive-style guidance point for future Spanish number-theory material. `Ordnung` is `orden` / `オーダー`; this keeps algebraic orders distinct from group order/位数. `erste/zweite Art` is kept as `primera/segunda especie` / `第一種/第二種`, aligned with the Steinitz terminology already present in the paper.

Global coherence: Paper 31 is tied directly to Paper 30's abstract ideal theory and to later Takagi-style algebraic number theory. The cumulative aids now include discriminant-theorem, order, residue-field/ring, quotient-ring, and multiplication-ring vocabulary. No older translated paper body needed rewriting in this packet beyond appending the new cumulative Paper 31 material and adding the Spanish discriminant gender policy to the methodology aids.

Formula policy: all bracket lcm decompositions, contraction notation `[\mathfrak R,\overline{\mathfrak p}]`, trace/norm symbols, discriminant determinants, and quotient-ring subscripts are preserved as editable TeX. No formulas, diagrams, or tables were converted into images. No tables or diagrams occur in Paper 31.
