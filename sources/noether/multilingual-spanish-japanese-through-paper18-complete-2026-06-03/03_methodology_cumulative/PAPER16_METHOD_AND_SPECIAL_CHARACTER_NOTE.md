# Paper 16 method and special-character note

Scope: Paper 16, `Zur Reihenentwicklung in der Formentheorie`, complete in Spanish and Japanese.

Source basis: the Paper 16 source scan slice `Noether_Paper16_SOURCE_SCAN_pages326-331_Zur_Reihenentwicklung_in_der_Formentheorie.pdf`, the paper-level German excerpt extracted from the full Noether source/provenance packet, and the paper-level English control excerpt.

Translation policy: preserve the invariant-theory language rather than silently modernizing it. Spanish uses `desarrollo en serie`, `teoría de formas`, `forma normal`, `coordenadas complejas`, `coordenadas de recta`, `proceso polar`, `base de módulo`, and `dominio de racionalidad`. Japanese uses `級数展開`, `形式論`, `正規形`, `複素座標`, `直線座標`, `極化過程`, `加群基底`, and `有理性領域`.

Mathematical structure: all numbered formulas `(1)` through `(10)`, including `(2a)`, are preserved as editable TeX. The central operator notation `S=AB`, Fischer's operations `A` and `B`, the Omega process `\Omega`, the determinant `\Delta`, the module congruences `\modu{M}` and `\modu{\Delta}`, and the sequence `\Omega\Delta\Omega\cdots\Delta\Omega` are not paraphrased into screenshots or prose.

Corrections section: the final `Correcciones` / `訂正` section is part of Paper 16 and has been translated. It includes Noether's corrections to Paper 09 and Paper 11, including Ostrowski's point that `Zahlkörper \Omega` in the formulation of Hilbert's irreducibility theorem should be read more precisely as a finite algebraic number field.

Macro policy: Paper 16 introduces or reuses `\p` for `\partial`, `\modu{#1}` for congruence-style modulo notation, and ordinary Greek/operator notation `\Phi`, `\Omega`, `\Delta`. The cumulative TeX supplies these by `\providecommand`, so they do not override earlier macros.

Audit flags: no translation gaps are declared. The render checks cover all standalone Spanish/Japanese pages and the cumulative tails containing Paper 16. The source scan renders are included under `05_audit/render_checks/source_scan/` for local comparison.
