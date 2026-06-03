# Cumulative methodology and special-character translation aid - ES/JA Noether lane

This file is cumulative for the Spanish/Japanese Noether lane through Paper 16 complete. It is intended for local Codex/Claude agents that need stable terminology, TeX macros, and character-handling conventions without re-reading all prior audit notes.

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
`Integritätsbereich` -> ES `dominio de integridad` / JA `整性領域`.
`relativ-ganzer Bereich` -> ES `dominio relativamente entero` / JA `相対的整領域`.
`Bereich erster Art` -> ES `dominio de primera especie` / JA `第一種の領域`.
`Involutionsform` -> ES `forma de involución` / JA `インボリューション形式`.
`Involutionsbasis` -> ES `base de involución` / JA `インボリューション基底`.
`Integritätsbasis` -> ES `base de integridad` / JA `整性基底`.
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

For Paper 09, `Bereich` was translated chiefly as Spanish `dominio` and Japanese `領域`; where the integral-domain structure is explicit, Spanish `dominio de integridad` and Japanese `整域` are used. `Zahl` remains `número` / `数` in the original complex-number setting, while `Größe` in §10 becomes `cantidad` / `量` when the discussion passes to arbitrary fields.

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

---

# Paper 17 §§10-12 and Paper 18 method and special-character note

Scope: Paper 17 §§10-12 complete and Paper 18 complete in Spanish and Japanese. This completes the Spanish/Japanese cumulative translation through Paper 18.

Source basis: the Batch26 German source/control TeX and PDF, the corresponding English control, and the scan slice `Noether_Paper17_sections10_12_and_Paper18_SOURCE_SCAN_collected_pdf_pages354-367_printed_pp340-353.pdf`. The German source remains controlling; the English control is used only as a sense witness and a guard against omissions.

Retroactive title standardization: the new cumulative Spanish/Japanese outputs update Paper 17's displayed title to include both `Differential- und Differenzenausdrücke`. Spanish now reads `expresiones diferenciales y de diferencias`; Japanese now reads `微分式および差分式`. This follows the Batch26 title and is clearer for the full paper. It does not change formulas or theorem content.

Paper 17 §§10-12: preserve the noncommutative module language from §§1-9. `Restgruppe` remains `grupo residual` / `剰余群`; `vollständig reduzibel` remains `completamente reducible` / `完全可約`; and `von gleicher Art` remains `del mismo tipo` / `同種`. The sequence of Theorems VIII-XII is retained, and formulas (31)--(44) remain editable TeX.

Paper 18: use `forma resultante` / `終結式形式` for `Resultantenform`. The abstract ideal-theory terms are translated as `ideal primario` / `準素イデアル` and `factor primario` / `準素因子`; avoid Japanese `一次イデアル` here, because the intended algebraic term is primary, not linear. Preserve the bracket decomposition `[\mathfrak Q,\mathfrak Q_1,\ldots,\mathfrak Q_r]=[\mathfrak Q,\mathfrak L]` as editable TeX.

No tables or diagrams occur in this scope. No formulas were converted to images, and no source-visible footnotes were omitted.

