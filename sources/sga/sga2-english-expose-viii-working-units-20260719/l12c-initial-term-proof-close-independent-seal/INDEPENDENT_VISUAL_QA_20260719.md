# Independent visual QA - 2026-07-19

Fresh source physical page 78 renders were inspected at 300 and 600 dpi. They
visibly confirm running page 70, printed page 88, the complete initial-term
calculation, the printed `H^q` defect in the derived Ext display, the separate
correct `H^{-q}` input above it, the universal `Ext^q = H^q` identity, QED, and
the start of printed page 89 / Section 2 on the same physical page.

The independent source renderer reported fallback diagnostics for unused
legacy display-font aliases in the PDF environment. Full-resolution review
confirmed that all relevant prose, prime marks, underlines, signs, bullets,
Hom/Ext operators, and formula glyphs are actually present and legible.

Fresh target page 1 renders were inspected at 300 and 600 dpi. The authority
box, every display, the source note, transparent-emendation caveat, projective
resolution paragraph, universal identity, explicit negative substitution,
and proof square are legible and unclipped. Section 2 is absent as required.

- Independent source 300 dpi: 479492 bytes; SHA-256
  `438DFD7441D1E388144E9BAAEB8B47B5F51DFB8270CEE68A79CC278A1B6784FC`.
- Independent source 600 dpi: 983010 bytes; SHA-256
  `61657D8A0BF8DA5352BFF6057A9C9C6A199F7C6FACFA7DD8A41D27165B6AAF81`.
- Independent target 300 dpi: 437999 bytes; SHA-256
  `2C7AB3D93F6C56284603984585BB2C910DC40F380CC551F3D410D5FC0EFBC2C2`.
- Independent target 600 dpi: 969334 bytes; SHA-256
  `4EB4006EE0AFF61571A5E062CF86856175FC6B5DC471E1F30CBEA11423D2E289`.

Status: independent source and target visual QA pass.

