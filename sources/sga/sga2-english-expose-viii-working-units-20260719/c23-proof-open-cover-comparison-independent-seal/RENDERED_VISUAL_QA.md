# Rendered visual QA - SGA2-VIII-C23-POC

Directly compiled French source physical pages 79-80 and target page 1 were
rendered at both 300 and 600 dpi and visually inspected at original resolution.

Checks passed:

- source headers distinguish running pages 71-72, while the marginal printed
  page marker 90 begins at French line 2685 on physical page 79;
- the target starts with the regular-affine assumed case and contains no text
  from the next reduction at French line 2715;
- `c_j(x)` visibly retains both closure bars, both intersections with `X_j`,
  support `Y`, and codimension argument order;
- `c_j(x)>=c(x)`, the dimension equality, and `c_j(x)=c(x)` are intact;
- condition (a) for the `X_j` visibly implies condition (a) for `X`;
- the equality-qualified partial converse is not silently expanded;
- the sentence period visibly precedes marker (5);
- note (5) is complete, *below* is italic, every prime/subscript and every
  implication/equivalence symbol is legible; and
- no clipping, collision, broken line, missing symbol, blank render, or
  out-of-scope continuation is present.

Render SHA-256 values:

- source physical 79, 300 dpi:
  `413899C59819721F60C6C001CB14214BEABA84FC302835F69B14C66D72B65ED2`;
- source physical 79, 600 dpi:
  `B1A0E57ED810AB3E7812AFE89CE50279D8EA74071F28B7E5B7041683E7DF79FD`;
- source physical 80, 300 dpi:
  `3F7D8648A9D98CF406BE4A44B3B4BD2709AAB3B60730175CEFFEDA97ABFC95C4`;
- source physical 80, 600 dpi:
  `6525F602B43F2F00005D36F29D8F80BC55FE71813D7E9A0DDCF97A1C5EC1E85E`;
- target page 1, 300 dpi:
  `FDAF0F885E8625CE7DA89465EEDEE9C0D5F119DCFC07D7DE0701EAEB1E38E136`;
- target page 1, 600 dpi:
  `AF9935C4CF5DBE122F34AD80F2B5D8348C83DB594039500A432BE9C1BA7B089A`.

The source renderer emitted legacy display-font lookup warnings, but all four
source renders are visually complete. This is a same-edition rendering caveat,
not evidence of an independent original witness.

Independent closure: six fresh 300/600 dpi renders were inspected at original
resolution and are byte-identical to these self-gate renders. See
`INDEPENDENT_VISUAL_QA_20260719.md`.
