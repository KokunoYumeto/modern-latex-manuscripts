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
