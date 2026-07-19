# Independent visual QA - 2026-07-19

Fresh independent evidence inspected at original resolution:

- source physical 76, 300 dpi: 526199 bytes, SHA-256
  `E3EFDB05C525745D95970F4AF61531AED6A542E24F33E0AE4935DD8D6F3FD183`;
- source physical 76 critical crop, 600 dpi: 310170 bytes, SHA-256
  `78D829C97E1978813E81B77511E2C3678AB7D5B2D0DA6437D57538CFEFDBD540`;
- target page 1, 300 dpi: 232124 bytes, SHA-256
  `7538B3438DEEB0BDEC8F6A7825EE153EA33C4FD09C9B251ADA51AB8FD4F353FC`;
- target critical crop, 600 dpi: 221224 bytes, SHA-256
  `D5FC3B53AF663E9222D99FA2D5B432B269C0BC4EB2883DB446458AEDDAA64D43`.

PASS: no clipping, overlap, blank output, glyph loss, broken formula, or
boundary spill. Printed page 85, physical page 76, and running page 68 are
confirmed for the lemma. The blank line 2560 and proof opening at line 2561
are outside the target; the marginal printed-page marker 86 occurs later in
the proof on the same physical page. Every functor identifier, quantifier,
degree, arrow, nested argument, and variance-relevant symbol is legible.
