# Independent visual QA - SGA2-VIII-L24

Fresh independent renders were inspected at original resolution:

- source physical p. 80 at 300 dpi: 641993 bytes, SHA-256
  `3F7D8648A9D98CF406BE4A44B3B4BD2709AAB3B60730175CEFFEDA97ABFC95C4`;
- source physical p. 80 at 600 dpi: 1060671 bytes, SHA-256
  `6525F602B43F2F00005D36F29D8F80BC55FE71813D7E9A0DDCF97A1C5EC1E85E`;
- independent target p. 1 at 300 dpi: 249924 bytes, SHA-256
  `7D21010814FE54843EB064AD88FFC80188E9BDBCF20726825758163A6C4FBC89`;
- independent target p. 1 at 600 dpi: 509208 bytes, SHA-256
  `390A5E8C42B0CDA838032190F2C81954A5B920232B9458B3D26EF4CA2FEEB2AC`.

Both source renders and both target renders are byte-identical to their
self-gate counterparts. The target visibly preserves both reduction
paragraphs, causal `by covering`, `F=tilde M`, the automatic heading
`Lemma 2.4`, regular Noetherian prescheme, lowercase `O_X-module`, and the
prose assertion that the projective-dimension assignment is bounded above.
No invented `pd` operator or displayed map is present.

No clipping, overlap, blank page, broken glyph, missing tilde, missing prime
on `X'`, missing hypothesis, or proof leakage was found. Poppler emitted
legacy source-reader display-font lookup warnings, but the in-scope source
page is visually complete.

Status: independent 300/600 dpi source-target visual pass.

