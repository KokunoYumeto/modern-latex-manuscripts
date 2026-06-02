# Audit note: Noether Paper 06 §§7-15, Spanish/Japanese continuation

## Scope

Completed in this packet: Noether Paper 06 §§7-15 inclusive, ending with the closing line `Erlangen, May 1914.` This completes Paper 06 in the Spanish/Japanese lane.

Previous stopping point: Paper 06 §6. Current stopping point: end of Paper 06. Next logical continuation: Paper 07 from the full Noether source archive.

## Fidelity and source handling

The German source excerpt is the governing witness. The English control excerpt is included only as a checking aid. Spanish and Japanese translations are direct, technical translations rather than summaries.

No declared translation gaps remain in §§7-15. Display formulas, numbered formulas, footnotes, theorem/definition numbering, fraktur notation, primes, Greek letters, colon quotient notation, and reference punctuation have been retained as editable TeX.

The following source-sensitive choices were preserved rather than normalized silently:

- The layered notation for `S_{n\rho}`, `L_{n\rho}`, `J_{n\rho}`, `K_{n\rho}`, and `G_{n\rho}` is kept in fraktur macros across source/control and ES/JA outputs.
- Colon quotient notation such as `f(x):g(x)` is preserved in prose contexts where the source uses quotient-by-colon language.
- In §§14-15, `R_0=\eps` is retained as the unit condition in `[\Omega]`, rather than converting the prose to an unrecorded normalization.
- The §11 use of `A_\tau(G_i(x))` is preserved according to the source/control reading in this packet and should not be silently altered to a starred variant.
- The integer/algebraic-integer terminology in §§14-15 is deliberately more explicit in both Spanish and Japanese to distinguish `ganz rational`, `ganz`, and `ganzzahlig` usages.

## Packaging/methodology

The package includes `methodology_cumulative/`, carrying the cumulative Spanish/Japanese method, glossary, special-character/notation aid, and local Codex build notes. This folder should be carried forward and updated in later packets.

Package structure follows the project rule: one ZIP, one root folder, then subfolders.

## Render and build review

Selected first/middle/last pages for the standalone chunks and tail pages for cumulative outputs were rendered to PNG under `audit/render_checks/`. Visual inspection showed no black squares, major clipping, or missing glyphs on the checked pages.
