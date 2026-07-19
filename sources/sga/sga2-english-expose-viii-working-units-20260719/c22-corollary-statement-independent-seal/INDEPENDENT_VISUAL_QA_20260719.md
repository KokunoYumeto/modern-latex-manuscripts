# Independent visual QA - SGA2-VIII-C22

Fresh independent renders were inspected at original resolution:

- source physical p. 79 at 300 dpi: 596847 bytes, SHA-256
  `413899C59819721F60C6C001CB14214BEABA84FC302835F69B14C66D72B65ED2`;
- source physical p. 79 at 600 dpi: 1015075 bytes, SHA-256
  `B1A0E57ED810AB3E7812AFE89CE50279D8EA74071F28B7E5B7041683E7DF79FD`;
- independent target p. 1 at 300 dpi: 280760 bytes, SHA-256
  `A3F37C1D9902106952D84F25ACB347ADDF0887C648E9726AC3726B7A4BDD533D`;
- independent target p. 1 at 600 dpi: 520180 bytes, SHA-256
  `207DD6B67BFAD17262C9F7A58F20A08C3C33A639EC744EEB973D9B0B0612CD93`.

The source renders are byte-identical to the self-gate source renders. The
target renders are byte-identical to the self-gate target renders despite the
new isolated PDF metadata timestamp.

The visible heading is `Corollary 2.2(3).`, with the marker before punctuation.
The statement preserves the condition-a equivalence and every part of
condition c), including `x in U`, `c(x)=1`, the exponent `i-1`, calligraphic
`F`, the stalk subscript, and equality to zero. The complete note visibly
preserves c) implies a), the converse, `Spec(A)`, tilde-M, finite projective
dimension, a'/c', c') implies d) implies a'), the below pointer, and the
reference following 2.4.

No clipping, overlap, blank page, broken glyph, missing prime, arrow, formula,
note text, header, or footer was found. Corollary 2.3 does not leak into the
target. Poppler emitted source-reader font lookup warnings, but both source
renders are visually complete.

Status: independent 300/600 dpi source-target visual pass.
