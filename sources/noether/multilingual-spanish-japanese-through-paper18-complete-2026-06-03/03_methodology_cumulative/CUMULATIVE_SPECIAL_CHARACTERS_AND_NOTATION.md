# Cumulative special characters and notation aid

## Mathematical alphabets and macros
- `\Kfield = \mathfrak{K}`: function field/body, rendered as $\mathfrak{K}$.
- `\Ssys = \mathfrak{S}`: system, rendered as $\mathfrak{S}$.
- `\Jdom = \mathfrak{J}`: integrality domain, rendered as $\mathfrak{J}$.
- `\Gdom = \mathfrak{G}`: relatively integral domain, rendered as $\mathfrak{G}$.
- `\Lsys = \mathfrak{L}`: linear family, rendered as $\mathfrak{L}$.
- `\Hgrp = \mathfrak{H}`: finite group in Paper 07, rendered as $\mathfrak{H}$.
- `\mathcal L`, `\mathcal S`, `\mathcal T`: linear families in Paper 08; keep calligraphic letters.
- `\Phi(z,u)`: Galois resolvent in Paper 07; preserve `\Phi`.
- `\nabla`, `\Omega`, `\Delta`: operator/determinant notation in Paper 08; do not normalize or paraphrase formulas.
- `\Omegaint = [\Omega]`: algebraic integers of the coefficient field in Paper 06 §§14-15.
- `\eps = \varepsilon`: unit notation when used.

## Diacritics and proper names
Keep Lüroth, Castelnuovo, Enriques, Hilbert, Steinitz, Kronecker, König, Mertens, Galois, Lagrange, Clebsch--Gordan, Capelli, Deruyts, Fischer, Zermelo unchanged in TeX source. Spanish PDF uses T1/UTF-8; Japanese in this packet uses XeLaTeX/xeCJK with Noto Serif CJK JP.

## German-to-target terminology fixed in this lane
- Rationalbasis -> base racional / 有理基底
- Minimalbasis -> base mínima / 最小基底
- Involutionsbasis -> base de involución / インボリューション基底
- Integritätsbasis -> base de integridad / 整性基底
- ganze rationale Funktion -> función racional entera / 整有理関数
- ganz rational -> racional entero / 整有理
- ganzzahlig -> entero or con coeficientes enteros / 整数係数 or 整数上整, according to context
- Abbildungsbereich -> dominio de aplicación / 写像領域
- relativ-ganze Bereiche erster Art -> dominios relativamente enteros de primera especie / 第一種の相対的整領域
- reguläres System -> sistema regular / 正則系
- Grundpunkt -> punto fundamental / 基本点
- Grundform -> forma fundamental / 基本形式
- Polarprozess -> proceso polar / 極化過程
- vollständiges System -> sistema completo / 完全系
- Potenzsumme -> suma de potencias / 冪和
- Reihenentwicklung -> desarrollo en serie / 級数展開
- Galoissche Resolvente -> resolvente de Galois / Galois resolvent（ガロアのレゾルベント）
- Polare -> polar / 極化形
- Determinantenkombination -> combinación determinantal / 行列式の組合せ

## TeX safety notes for local Codex
Use `es-noquoting,es-noshorthands` for Spanish babel to avoid shorthand collisions in formulas. Avoid replacing colon notation `F(x):G(x)` by fractions where the source uses colon notation. Do not normalize historical source punctuation, congruence notation, operator notation, or determinant notation in Papers 07-08 without a source-level audit.


## Paper 10 notation

- `\Theta`: rational basis of all numbers.
- `\vartheta`: a basis element; `\mathfrak K(\vartheta)`: the segment field attached to it.
- `H`, `Z`, `\eta`, `\zeta`: algebraic basis and selected image basis.
- `X,Y`: real and imaginary coordinates of the value `f(z)` or `\varphi(z)`.
- `\pm`/`\mp`: sign-paired formulas in the rank-three exclusion; preserve pairing exactly.


## Paper 12 notation
- `\bdelta = \bar{\delta}`: second variation/process parameter in formulas (3), (5), and the discussion around (6). Keep distinct from ordinary `\delta`.
- `f_\delta`, `f_{\delta^\sigma}`: polar notation in formulas (2)--(4); do not expand silently into prose.
- `\Omega_\rho`, `[\Omega_\rho^{(\nu)}]`: normal variation forms and covariant derivatives/fundamental functions.
- `\varphi_\rho^{(i)}` and `\Psi_\rho`: normal-coordinate expansion and resulting fundamental functions.
- `p,q,r,\ldots`: cogredient replacements for higher differentials.


## Paper 15 notation
- `\frH`, `\frK`, `\frM`, `\frN`, `\frG`, `\frS`: Fraktur/module/group notation in the finiteness theorem for integral invariants. Use `\providecommand` in cumulative TeX.
- `(ik)`: determinant shorthand in the binary-form invariant notation; do not expand unless the source does.
- `f_{ik,rs}` and residue-class normalization notation: preserve indices and comma placement.

## Paper 16 notation
- `\p = \partial`: local macro for partial derivatives in compact operator formulas.
- `\modu{M}` and `\modu{\Delta}`: source-like congruence modulo a module/determinant. Keep as congruence notation, not prose.
- `\Phi`, `\Omega`, `\Delta`: normal form, Omega process, and determinant; preserve exactly.
- `p_{ik}=(x_i y_k-x_k y_i)`: line-coordinate substitution.
- `t_i,t_{ik},t_{ikl},\ldots`: complex-coordinate hierarchy; do not replace by modern tensor notation.
- `S=AB`, `BF(z)=F(f(\xi))`, and Fischer's operator formula (5): preserve operator order.
- Formula tags `(1)`--`(10)` plus `(2a)` are present and must stay editable TeX.

---

# Paper 17 §§10-12 and Paper 18 method and special-character note

Scope: Paper 17 §§10-12 complete and Paper 18 complete in Spanish and Japanese. This completes the Spanish/Japanese cumulative translation through Paper 18.

Source basis: the Batch26 German source/control TeX and PDF, the corresponding English control, and the scan slice `Noether_Paper17_sections10_12_and_Paper18_SOURCE_SCAN_collected_pdf_pages354-367_printed_pp340-353.pdf`. The German source remains controlling; the English control is used only as a sense witness and a guard against omissions.

Retroactive title standardization: the new cumulative Spanish/Japanese outputs update Paper 17's displayed title to include both `Differential- und Differenzenausdrücke`. Spanish now reads `expresiones diferenciales y de diferencias`; Japanese now reads `微分式および差分式`. This follows the Batch26 title and is clearer for the full paper. It does not change formulas or theorem content.

Paper 17 §§10-12: preserve the noncommutative module language from §§1-9. `Restgruppe` remains `grupo residual` / `剰余群`; `vollständig reduzibel` remains `completamente reducible` / `完全可約`; and `von gleicher Art` remains `del mismo tipo` / `同種`. The sequence of Theorems VIII-XII is retained, and formulas (31)--(44) remain editable TeX.

Paper 18: use `forma resultante` / `終結式形式` for `Resultantenform`. The abstract ideal-theory terms are translated as `ideal primario` / `準素イデアル` and `factor primario` / `準素因子`; avoid Japanese `一次イデアル` here, because the intended algebraic term is primary, not linear. Preserve the bracket decomposition `[\mathfrak Q,\mathfrak Q_1,\ldots,\mathfrak Q_r]=[\mathfrak Q,\mathfrak L]` as editable TeX.

No tables or diagrams occur in this scope. No formulas were converted to images, and no source-visible footnotes were omitted.

