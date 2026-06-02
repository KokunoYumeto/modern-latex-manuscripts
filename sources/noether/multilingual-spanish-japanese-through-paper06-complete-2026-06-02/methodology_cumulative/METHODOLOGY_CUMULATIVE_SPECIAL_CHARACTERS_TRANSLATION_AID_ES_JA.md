# Cumulative methodology and special-character translation aid - ES/JA Noether lane

This file is cumulative for the Spanish/Japanese Noether lane through Paper 06 complete. It is intended for local Codex agents that need stable terminology, TeX macros, and character-handling conventions without re-reading all prior audit notes.

## Packaging and workflow

Use one outer ZIP, one root folder, then subfolders. Keep standalone chunk TeX/PDF, cumulative TeX/PDF, German source, English control, render checks, logs, glossary deltas, and audit notes in their named subfolders. Do not replace hard formulas, tables, or diagrams with screenshots; preserve editable TeX whenever possible.

## Engines

Spanish: `pdflatex` with T1/UTF-8 and `babel` options `spanish,es-noquoting,es-noshorthands`.
Japanese: `lualatex` with `jlreq` and `luatexja`.

## Core macros currently in use

`\Kfield=\mathfrak{K}`, `\Ssys=\mathfrak{S}`, `\Mfield=\mathfrak{M}`, `\Lsys=\mathfrak{L}`, `\Jdom=\mathfrak{J}`, `\Gdom=\mathfrak{G}`, `\Omegaint=[\Omega]`, `\eps=\varepsilon`.

## Special-character policy

Keep diacritics in proper names: Lüroth, Castelnuovo, Enriques, Hilbert, Steinitz, Kronecker, König, Mertens, Galois, Lagrange. Do not strip accents in Spanish prose. Japanese output should keep Latin names in roman script unless the established mathematical convention requires otherwise.

Preserve Noether's historical notation, including colon quotients such as `F(x):G(x)`, prime-marked theorem labels such as `V$'$`, and source abbreviations such as `in inf.` when explicitly used as such.

## Current Paper 06 terminology locks

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

## Source anomaly policy

Do not silently normalize source anomalies. For this round, preserve and flag: §11 formula (6) with `A_\tau(G_i(x))`; §12 `in inf.`; and the `Gattungsbereich` term. Future agents should only normalize after source-level review, not while translating.
