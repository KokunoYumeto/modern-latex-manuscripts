# Independent review seal - SGA2-VIII-L12S

This bounded internal unit is independently source-reviewed and sealed.

## Exact scope

- Corrected French lines 2553-2559.
- Original printed page 85.
- Physical source-PDF page 76.
- Recomposed running page 68.
- Blank line 2560 excluded; continuation cursor line 2561 at the proof.

## Substantive result

Independent comparison against the corrected French TeX and direct PDF
confirms the transition sentence, Noetherian ring, category of modules,
underlined functor and domain/codomain, left exactness and additivity, every
finite-generation and injectivity quantifier, degree-one vanishing, both
hypotheses on `M`, and the complete spectral-sequence display.

The literal source has `R^* F(M)` on the left of a long left arrow and
`Ext_F^p(Ext^{-q}(M,A),A)` on the right. The target preserves the star, `p`,
`-q`, argument nesting, arrow direction, and the definition of `Ext_F^p` as
the `p`-th right derived functor of `F` composed with `Hom`. Immediate source
context at lines 2544-2546 fixes derivation in the second argument and the
contravariant/covariant category variance. No English mathematical correction
was required.

The comparison candidate's explicit `E_2^{p,q}` equality and
`R^{p+q}F(M)` abutment are a reasonable explanatory expansion, but those
symbols are absent from the printed French statement. They remain recorded as
comparison-only and rejected from the substantive body, together with the
candidate's flattened functor/category typography.

## Gates

- Fresh two-pass build: pass, zero diagnostics.
- PDF/text/font inspection: pass; 1 A4 page; 14/14 font rows embedded,
  subsetted, and Unicode mapped; zero forbidden text-control bytes.
- Source and target visual QA: pass at 300 dpi full-page and 600 dpi critical
  crops.
- CSV/JSONL validation: pass for stable IDs, rectangularity, formula safety,
  schema, revision links, and reference closure.
- Authority hashes, privacy scan, Artifact Tool imports/renders, and exact
  manifest closure: pass.

This seal is internal and bounded. Cumulative Expose VIII integration, release
review, and publication remain open.
