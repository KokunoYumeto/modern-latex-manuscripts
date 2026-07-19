# Rendered visual QA - self gate

- Direct source-PDF physical page 79 / running page 71 was freshly rendered at
  300 and 600 dpi. It shows Corollary 2.2 and note (3) above the margin marker
  that begins original printed page 90 at French line 2685; the bounded unit is
  therefore on original printed page 89.
- The final target page was freshly rendered at 300 and 600 dpi after the
  two-pass build. Both resolutions were inspected at original resolution.
- The heading reads `Corollary 2.2(3).`: the number is correct and the note
  marker precedes the punctuation, matching the source structure.
- Condition c), every quantifier, `c(x)=1`, `H^{i-1}(F_x)=0`, all prime labels,
  the c)-to-a) direction, c')-to-d)-to-a') chain, `Spec(A)`, tilde on `M`, and
  both source references are legible and unclipped.
- No collision, overlap, broken italic, missing glyph, missing prime, missing
  arrow, clipping, or Corollary 2.3 boundary leakage is visible.
- Poppler emitted legacy source-reader display-font lookup warnings while
  rendering the source page. The page itself is complete and all in-scope
  glyphs were checked visually at both resolutions; target rendering emitted
  no such warning.

Status: rendered source/target self-review pass. Fresh independent 300/600 dpi
renders closed the visual gate; see `INDEPENDENT_VISUAL_QA_20260719.md`.
