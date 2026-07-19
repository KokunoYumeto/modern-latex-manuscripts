# Independent re-review and bounded seal

Review ID: `SGA2-VIII-APP31-IREVIEW-20260719-0001`.

An independent re-review passed the immutable `SGA2-VIII-APP31` target after
the producer's extraction and public-log repairs and after the manager closed
F/G Option A. No target or pre-existing evidence file was repaired during this
review.

## Source boundary and locators

The sealed body is corrected French lines 2874--2886: section 3
`Applications`, its bridge, Theorem 3.1, and the complete proof. Structural
blanks 2875, 2877, and 2881 are included. Blank 2887 and Proposition 3.2 are
excluded; the exact cursor is French line 2888.

The source unit occupies original printed pp. 96--97, direct same-edition PDF
physical p. 84, and recomposed running p. 76. The printed-p. 97 token occurs
inside line 2886 immediately after `vérifiée`. The corrected branch's “page
74” resolves to running p. 74; condition (iv) is source line 2811 on original
printed p. 93 and physical p. 82. Fresh PDF extraction independently confirmed
both page systems and the Proposition 3.2 boundary.

## Translation, formula, and symbol review

The review passed every hypothesis and conclusion of Theorem 3.1, including
the nonproper application bridge versus proper `f`, `f:X\to Y`, locally
Noetherian `Y`, local embeddability in a regular prescheme, `n`, `U`, the
coherent sheaf, both closures in the codimension-one condition, the depth
bound, the composite higher direct image, canonical immersion `g`, Leray
abutment, the full `E_2^{p,q}` term, coherent extension, both EGA references,
strict bounds, and the no-QED close.

Manager decision `EG-SGA2-FG-NOTATION-ADJUDICATION-20260719-0001` closes
Option A. Corrected-source `\Fa`/`\Ga` are upright `F/G`; the target's
calligraphic `F/G` are a deliberate established-English normalization and
never literal source-glyph preservation. The append-only `@1` to `@2`
difficulty revisions, all terminal revision-2 CSV controls, the 3,093-byte
addendum SHA-256
`B6870E65A6A36DD6B4A6291CF38A36AC95BF4903541BF65147C0CB60D6E7858D`,
and manager prose SHA-256
`8ED4C58A288E22002BF88A098D52661D392D663436E63C63CD011B7AC099F0ED`
were independently rechecked. The immutable target authority box retains its
historical cautious word “provisional”; the terminal controls supersede only
that policy-state description, not the target identity.

Two other typography policies remain separately provisional: source
`\ZZ=\mathbf Z` to target `\mathbb Z`, and source upright `\R`/`\E` to
target math-italic `R/E`. In line 2884 the source already uses plain `R^p`
outside but upright `\R^q` inside; the target's uniform italic `R` is disclosed
under that still-provisional R/E policy. No formula degree, index, functor,
bound, or sheaf identity is changed.

The jcreinhold e7a259f Markdown remains one comparison-only LLM lineage. Its
bullet abutment, fenced formula, closure shorthand, raw depth notation,
inequality typography, unqualified page 74, and linked citation apparatus were
not treated as authority or independent corroboration.

## Build, render, machine, and privacy gates

- Frozen TeX: 3,154 bytes, SHA-256
  `1CBB3EF71309ED5C5AABEDA6DB5ED840E2C007B70DE112667A78A4AE5F9B207D`.
- Frozen PDF: 292,372 bytes, one A4 page, SHA-256
  `B2973258EE71F71D55CA4F167B74D41AE43388CB498A81B92E3E920F1ED6933D`.
- A fresh two-pass independent rebuild exited zero with no diagnostic. Its
  timestamp-variant PDF was 292,372 bytes, SHA-256
  `D3AA27CF79C97CC0021BE7915DD567651E78247481601ABD48CCB562F404ABDC`;
  its 2,529-byte extraction and 180-dpi render were byte-identical to the
  frozen QA artifacts.
- Final extraction: one formfeed, zero forbidden controls, SHA-256
  `E229FB8A83914F093EFB19006FBB60A92CB2330A6010314917900744712B7CAE`.
- Final render: 291,729 bytes, SHA-256
  `C86B40146D38F464F726547125BB613CD20C5E4F27785DCE82CECFC63CDCE8C2`.
- All 19 fonts are embedded, subset, and Unicode-mapped.
- Five CSV ledgers contain 71 substantive rows; all are rectangular, have
  unique primary IDs, and contain no formula-trigger cells.
- The two JSONL ledgers contain 28 records across 23 stable IDs; parse,
  schema, hierarchy, local-reference, revision, supersession, and reciprocal
  closure checks pass.
- All five existing Artifact Tool receipts and previews match their hashes,
  and a fresh independent import/inspect/formula-scan/render pass succeeded.
- The strengthened scan of public-candidate text found no private path,
  user/profile, drive-qualified, split-continuation, or stale redaction-token
  hit. Raw and local-only logs remain excluded from release.

The direct French PDF is generated from the corrected edition and is not an
independent witness. This automated review is not human scholarly peer review.
The seal applies only to this bounded unit; it claims neither a complete
Exposé VIII nor a complete SGA2 volume, archive custody, publication, or remote
readback.
