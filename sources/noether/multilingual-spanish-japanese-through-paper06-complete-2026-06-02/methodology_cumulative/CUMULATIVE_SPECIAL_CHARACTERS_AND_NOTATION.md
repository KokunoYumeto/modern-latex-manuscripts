# Cumulative special characters and notation aid

## Mathematical alphabets
- `\Kfield` = `\mathfrak{K}`: function field/body, rendered as $\mathfrak{K}$.
- `\Ssys` = `\mathfrak{S}`: system, rendered as $\mathfrak{S}$.
- `\Jdom` = `\mathfrak{J}`: integrality domain, rendered as $\mathfrak{J}$.
- `\Gdom` = `\mathfrak{G}`: relatively integral domain, rendered as $\mathfrak{G}$.
- `\Lsys` = `\mathfrak{L}`: linear family, rendered as $\mathfrak{L}$.
- `\Omegaint` = `[\Omega]`: algebraic integers of the coefficient field in §§14-15.
- `\eps` = `\varepsilon`: unit in `[\Omega]` in integer-regular systems.

## Diacritics and proper names
Keep Lüroth, Castelnuovo, Enriques, Hilbert, Steinitz, Kronecker, König, Mertens, Galois, Lagrange unchanged in TeX source. Spanish PDF uses T1/UTF-8; Japanese PDF uses LuaLaTeX/luatexja.

## German-to-target terminology fixed in this lane
- Rationalbasis -> base racional / 有理基底
- Minimalbasis -> base mínima / 最小基底
- Involutionsbasis -> base de involución / インボリューション基底
- Integritätsbasis -> base de integridad / 整性基底
- ganz rational -> racional entero / 整有理
- ganzzahlig -> entero over `[\Omega]` / 整数係数 or 整数上整, according to context
- Abbildungsbereich -> dominio de aplicación / 写像領域
- relativ-ganze Bereiche erster Art -> dominios relativamente enteros de primera especie / 第一種の相対的整領域
- reguläres System -> sistema regular / 正則系
- Grundpunkt -> punto fundamental / 基本点

## TeX safety notes for local Codex
Use `es-noquoting,es-noshorthands` for Spanish babel to avoid shorthand collisions in formulas. Avoid replacing colon notation `F(x):G(x)` by fractions where the source uses colon notation. Do not normalize `R_0=\eps` to `R_0=\varepsilon` in prose-only patches unless the macro is present.
