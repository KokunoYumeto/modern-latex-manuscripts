# Source audit - Expose VIII first spectral-sequence abutment

This bounded target translates corrected French lines 2611--2616 only.
Direct comparison against source-PDF physical pages 77--78 confirms original
printed page 88 and recomposed running pages 69--70. Line 2617 is blank. The
initial-term computation begins at line 2618 and is excluded.

The audit separately checked the simple-complex identification; the first
statement of the abutment as the homology of underlined `F P^bullet`; the
corrected `projective of finite type` reading; the Hom-complex isomorphism;
the successive maps `a`, `b`, and `c`; equation (1.5); the injective-resolution
claim; Proposition 1.4 and equation (1.1) cross-references; the homotopy
equivalence with `I^bullet`; and the exact final abutment
`R^* underlined-F(M)`.

The corrected source selects `projective` over the deleted `free` reading in
both occurrences. The direct PDF confirms the corrected branch. The
jcreinhold e7a259f Markdown is comparison-only: it is not independent
corroboration. Its `C_A`, flattened functor, and bullet exponents for the
final homology/derived functor are rejected in favor of source `CA`,
underlined `F`, and star exponents.

The source TeX has `\Ref{VIII.1.4}.,`, which the direct PDF prints as
“Proposition 1.4.,”. The target uses the ordinary English punctuation
“Proposition 1.4,”. This is a recorded punctuation normalization rather than
a silent emendation; no mathematical source correction is proposed.

Independent review found and corrected one source-notation regression: the
draft's underlined `F` was italic, whereas the French style authority defines
an upright roman underlined `F`. The review also replaced the standalone
manual `(1.5)` tag with a source-matching automatic counter initialized to 4,
yielding the unique PDF destination `equation.5` without a visible change.

Status: independently source-reviewed bounded unit. Formula, numbering, page,
punctuation, boundary, build, render, extraction, machine-ledger, and privacy
gates pass. Cumulative integration and publication remain open.
