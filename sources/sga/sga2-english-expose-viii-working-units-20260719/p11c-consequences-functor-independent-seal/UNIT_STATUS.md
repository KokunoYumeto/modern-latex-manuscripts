# Unit status - Expose VIII Proposition 1.1 consequences and functor setup

Status: independently source-reviewed and sealed bounded internal unit. Fresh
two-pass build, direct source/target render inspection, extracted-text and font
checks, spreadsheet-artifact inspection, and strict machine validation pass.
Cumulative Expose VIII integration, release review, and publication remain
pending.

- Unit ID: `SGA2-VIII-P11C`.
- Authority scope: corrected French lines 2527-2551; printed pages 84-85;
  physical source-PDF pages 75-76; recomposed running pages 67-68.
- Continuation cursor: line 2553 after blank line 2552.
- Coverage: deduction of Proposition 1.1(2) from (1); three sheafification
  isomorphisms; categories and functor; Expose II and VI derived-functor
  identifications; injective/flasque/R1 vanishing observation.
- Excluded: blank line 2552 and Lemma 1.2 from line 2553 onward.

Independent review found no English mathematical error. It documented one
French-TeX grouping defect: at line 2530 the outer tilde closes before the
final parenthesis; the target correctly places the complete `Ext_Y(F,G)`
expression inside the associated-sheaf tilde. The notice
`SGA2_EXPOSE_VIII_LINE2530_TILDE_GROUPING_CODEX_20260719.md` is 1812 bytes,
SHA-256
`1A9EE2185E585464A20232C799BB00969BE522C98764A94C9C7451D5489A3694`.
The jcreinhold `Ñ`, malformed sheaf-Hom tilde scope, and plain-text operator
losses remain rejected as comparison regressions. The only target-side edit
was replacing extensible delimiters in the final one-line vanishing formula
with ordinary parentheses, removing an extracted control character without
changing visible mathematics.

The final PDF is one unencrypted A4 page, 245199 bytes, SHA-256
`3ADFA9902AF3F4216EF279C67A4B38B96150AA5ADFDCBA6B811E3BA5F562C007`;
all 16 reported font rows are embedded, subsetted, and Unicode mapped. The
editable TeX is 2849 bytes, SHA-256
`756FC12C7AF42D5729BC259DAE5E03E6DD975E8A86DC54B52730936A5DCDDFF8`.
Machine evidence comprises 36 substantive CSV records plus a 30-row exact
manifest, 14 structural JSONL records / 10 stable IDs, and 10
difficulty/revision events / 8 stable IDs. Rectangularity, formula safety,
revision/reference closure, exact authority hashes, privacy, manifest closure,
and Artifact Tool render checks pass.
