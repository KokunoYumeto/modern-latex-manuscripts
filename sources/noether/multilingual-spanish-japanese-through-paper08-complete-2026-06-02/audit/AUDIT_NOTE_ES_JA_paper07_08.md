# Audit note - Noether Papers 07-08 ES/JA

Scope completed in this packet: Paper 07 complete and Paper 08 complete in Spanish and Japanese. The stopping point is the end of Paper 08, after `Erlangen, 5 January 1915.` Paper 09 begins next.

## Source range and witnesses

German source and English control excerpts are included as editable TeX/PDF in `new_work_this_round/source_and_control/`. Paper 07 and Paper 08 source scans are included for local visual checking.

## Fidelity notes

No declared translation gaps in Paper 07 or Paper 08. No tables or diagrams were silently omitted. Formulas and operator notation were kept as editable TeX.

Paper 07: preserved the finite group notation `\mathfrak{H}`, the Galois resolvent `\Phi(z,u)`, the power-sum invariant notation `J_{\mu_1\ldots\mu_n}`, and the statement that the coefficients of the Galois resolvent form a finite complete system of invariants.

Paper 08: preserved the distinction among polar processes, determinant combinations, `\Delta`, `\Omega`, `\nabla`, and calligraphic families `\mathcal L`, `\mathcal S`, `\mathcal T`. The final development formulas (3), (4), and (5) were kept editable rather than converted to images.

## Terminology decisions added this round

- `ganze rationale Darstellung` -> ES `representación racional entera`; JA `整有理表示`.
- `Invarianten eines Systems beliebig vieler Grundformen` -> ES `invariantes de un sistema de arbitrariamente muchas formas fundamentales`; JA `任意に多くの基本形式からなる系の不変式`.
- `Galoissche Resolvente` -> ES `resolvente de Galois`; JA `Galois resolvent` in formulas/prose, with the Japanese aid noting `ガロアのレゾルベント` as an explanatory rendering.
- `Polarprozess` -> ES `proceso polar`; JA `極化過程`.
- `Reihenentwicklung` -> ES `desarrollo en serie`; JA `級数展開`.

## Build note

Spanish chunk and Spanish cumulative compile with pdfLaTeX. Japanese chunk and Japanese cumulative compile with XeLaTeX/xeCJK in this packet. Earlier Japanese packets used LuaLaTeX; this divergence is recorded because local LuaHBTeX/luaotfload did not complete reliably during this run. The Japanese TeX remains UTF-8 and portable for local adaptation.
