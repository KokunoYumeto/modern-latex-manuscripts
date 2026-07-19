# Draft source audit - Expose VIII Lemma 1.2 statement

The bounded target translates corrected French lines 2553-2559 only. Direct
comparison against source-PDF physical page 76 confirms original printed page
85 and recomposed running page 68. The line-2561 proof opening falls after the
lemma and is excluded; the exact continuation cursor is line 2561 after blank
line 2560.

The ring, category, functor signature, left-exact/additive hypotheses,
finite-generation and injectivity quantifiers, degree-one vanishing, finite
projective dimension, spectral-sequence arrow, `*`, `p`, `-q`, nested Ext
arguments, and definition of `Ext_F^p` were checked individually. No French
source correction was needed in this unit.

The jcreinhold comparison candidate at lines 78-93 expands the printed display
to an explicit `E_2^{p,q}` term and `R^{p+q}F(M)` abutment. That is a useful
interpretation, but those symbols are not present in the French authority, so
the expansion is recorded and rejected from the substantive source-aligned
translation. Its plain typography is likewise not copied over the authority's
distinct category, functor, and abelian-group symbols.

The first target build used extensible parentheses and was visually correct,
but text extraction emitted control characters for the closing delimiters.
Ordinary TeX parentheses were substituted without changing the visible or
mathematical content; the final extraction retains the complete delimiters.

Status: source-compared production draft, self-gate pending build, render, and
machine validation. Independent review remains required before sealing.
