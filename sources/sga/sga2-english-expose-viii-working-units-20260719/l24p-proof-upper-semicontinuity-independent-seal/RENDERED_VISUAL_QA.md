# Rendered visual QA - SGA2-VIII-L24P

Directly compiled French source physical page 80 and target page 1 were
rendered at both 300 and 600 dpi and visually inspected at original resolution.

Checks passed:

- the source header gives running page 72 and the proof crosses the printed
  page marker from 90 to 91 on physical source-PDF page 80;
- the target authority box separates source TeX lines, printed pages, physical
  PDF page, running page, and the exact outbound line-2733 cursor;
- the proof retains the affine neighborhood, finite projective resolution,
  regular local ring, projective dimension `d`, and kernel
  `K = ker(L^{-d} -> L^{-d+1})`;
- the localized resolution visibly uses `M_f` and `(L^{-d})_f`, while the
  source note discloses both departures from the printed French proof;
- the upper-semicontinuity and quasi-compactness conclusion is present;
- no clipping, collision, broken line, missing symbol, blank render, or
  accidental extra source text after line 2731 is present.

Render SHA-256 values:

- source physical 80, 300 dpi:
  `3F7D8648A9D98CF406BE4A44B3B4BD2709AAB3B60730175CEFFEDA97ABFC95C4`;
- source physical 80, 600 dpi:
  `6525F602B43F2F00005D36F29D8F80BC55FE71813D7E9A0DDCF97A1C5EC1E85E`;
- target page 1, 300 dpi:
  `9CD95973FA497905135C157073780A1E6D1F778DF0E37AC0D6880BDDF4926BA9`;
- target page 1, 600 dpi:
  `533BC1FB9A9CFB1F444641C32319C5756B5940BB8AB65A612B597FC84AC9FA69`.

The source renderer emitted legacy display-font lookup warnings, but both
source images are visually complete. Line 2723 is an equation-counter reset
with no visible body and is controlled by TeX and machine ledgers.

Independent review repeated both source and target renders at 300 and 600 dpi.
All four independent images are byte-identical to their self-gate
counterparts, and original-resolution inspection found no clipping, collision,
missing glyph, malformed formula, blank content, or boundary drift. Only the
two target renders are proposed public files; source renders remain internal.
