# P35 pp. 65-72 Source Audit

Date: 2026-07-11

## Scope and source

This pass independently compared the complete active P35 TeX span with all eight printed source pages of Emmy Noether, *Über Maximalbereiche aus ganzzahligen Funktionen*, Rec. Soc. Math. Moscou 36 (1929), pp. 65-72.

The authority was the complete MathNet source PDF recovered from the R130 intake and its native embedded 600 ppi page images. OCR text was used only as a locator. Every printed page was opened visually; mathematical displays, inline symbol families, notes, the Russian summary, and both article boundaries were checked.

## Promoted source-backed repairs

1. Printed p. 67: corrected the constant-function generator from `1/e` to source `1/c`.
2. Printed p. 70: restored the section-4 algebraic integer `alpha`, ideal-factorization exponents `varrho_i`, and common denominator `delta`, replacing the collapsed `a`, `alpha_i`, and `d` readings.
3. Printed p. 71: carried the same source family through the cross-page continuation, including `gamma alpha` and all lambda exponents `varrho_i`.

The p. 70-71 changes are one coherent proof-level repair, not independent cosmetic substitutions. The source assigns different mathematical roles to `alpha`, `varrho_i`, and `delta`.

## Rejected false positives

- Printed p. 66 explicitly reads `H(u_i^p)`. The current indexed argument is correct.
- Printed p. 67 uses plain `P` in all three residue-field occurrences. An inherited note asserting barred `P` was wrong. A temporary bar patch was reverted before compilation and sealing.
- Printed p. 72 prints primed functions `f'_1(x),...,f'_r(x)` in the Russian summary. The primes remain.

These guardrails are recorded in the adjudication, correction-origin, and page-QC ledgers so future merges do not revive the rejected readings.

## Page outcomes

- p. 65: no secure mathematical delta.
- p. 66: no patch; indexed `H(u_i^p)` source-confirmed.
- p. 67: one mathematical constant repaired; plain `P` source-confirmed.
- p. 68: no secure mathematical delta.
- p. 69: no secure mathematical delta.
- p. 70: linked `alpha/varrho/delta` family repaired.
- p. 71: cross-page `alpha/varrho` continuation repaired.
- p. 72: no patch; primed Russian function family source-confirmed.

## Build and render QA

- XeLaTeX passed twice with halt-on-error.
- Cumulative length remains 466 pages.
- No fatal, emergency-stop, undefined-control-sequence, rerun, overfull, or underfull flags occur in the final pass log.
- The P35 output band is cumulative PDF pp. 350-355.
- Same-renderer pixel comparison changed only pp. 351, 353, and 354. Pages 350, 352, and 355 are pixel-identical to v20.
- All changed final pages were opened at original render resolution. No clipping, overlap, missing line, or unintended downstream reflow was found.

## Error yield and method lesson

Eight complete pages yielded two substantive mathematical error families spanning three pages: one wrong constant and one long cross-page symbol-family collapse. The latter is the more important residual class: plausible prose can conceal a proof whose variable roles have silently merged.

The false barred-`P` handoff claim is also a process lesson. Specific prior-agent notes are evidence leads, not authority. A claim must survive direct source-glyph inspection before it enters the cumulative.

## Status

P35 is closed at the current-head, best-available-source mathematical-fidelity level, subject to the standing rule that contradictory evidence can reopen a page. This is a paper-level closure, not completion of the author-wide Noether goal.
