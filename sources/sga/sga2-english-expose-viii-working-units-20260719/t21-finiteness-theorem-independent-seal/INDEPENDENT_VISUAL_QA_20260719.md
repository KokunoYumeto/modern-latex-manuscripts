# Independent visual QA - SGA2-VIII-T21

Date: 2026-07-19  
Result: pass for the bounded unit

The direct French control pages and the independently rebuilt target were
inspected at 600 dpi, with the corresponding 300-dpi renders retained as a
second scale check.

- French physical page 78 / running page 70 visibly begins original printed
  page 89 at Section 2 and contains the theorem heading, condition a), its
  vanishing display, the regular-prescheme note, and the Raynaud note.
- French physical page 79 / running page 71 visibly completes condition a),
  equation (2.1), and condition b). The printed-page-90 marker occurs later,
  at the paragraph beginning from French line 2685, outside this unit.
- The target visibly renders `Theorem 2.1(1).`, `Mme Raynaud`, acute `Éc.`,
  the star note, note (2), labels a) and b), exponent `i-c(x)`, both closure
  bars in equation (2.1), and sheaf local cohomology `\mathcal H^i_Y`.
- No text, formula, footnote, marker, closure bar, glyph, or boundary content
  is clipped, missing, overlapping, or displaced.
- Independent target render SHA-256 values are
  `DED7EA1CC39272CE4A03597012F73311453D673BE88249C3174677B1A069C466`
  at 300 dpi and
  `1819EF2FC709F2B2CA6DE5C2B7ADD81B3860210D4A8AA4C27D99567E08C01971`
  at 600 dpi. They exactly match the frozen target renders.

The direct PDF is the compiled output of the same corrected French edition,
not an independent original-typescript scan. Visual agreement therefore checks
page location, notation, notes, and rendering; it is not independent textual
corroboration.
