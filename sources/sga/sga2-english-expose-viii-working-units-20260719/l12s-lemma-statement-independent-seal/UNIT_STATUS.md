# Unit status - Expose VIII Lemma 1.2 statement

Status: independently source-reviewed and sealed bounded internal unit. Fresh
two-pass build, direct source/target render inspection, extracted-text and font
checks, spreadsheet-artifact inspection, and strict machine validation pass.
Cumulative Expose VIII integration, release review, and publication remain
pending.

- Unit ID: `SGA2-VIII-L12S`.
- Authority scope: corrected French lines 2553-2559; original printed page 85;
  physical source-PDF page 76; recomposed running page 68.
- Continuation cursor: French source line 2561 after blank line 2560.
- Coverage: transition sentence; complete Lemma 1.2 hypotheses; spectral
  sequence; definition of `Ext_F^p`; lemma close.
- Excluded: blank line 2560 and the proof from line 2561 onward.
- Comparison control: jcreinhold e7a259f remains comparison-only. Independent
  review confirms its explicit `E_2^{p,q}` and `R^{p+q}F(M)` expansion is an
  unprinted interpretation and must remain outside the source-aligned body;
  its flattened typography is also rejected.
- Source correction: none required. Immediate French context at lines
  2544-2546 supplies second-argument derivation and bifunctor variance; the
  bounded lemma accurately preserves its abbreviated definition.
- Build: fresh independent two-pass `pdflatex` PASS with zero final
  diagnostics. The PDF is one unencrypted A4 page with 14 embedded, subsetted
  Unicode font rows; 234774 bytes; SHA-256
  `2397DEA97C66AC3D378A3AA1CD63E8519F249F6E8D622B80E46D0CDAAC7B8690`.
  Editable TeX is 1810 bytes; SHA-256
  `0022D33C2E47D85FB286B82728D3B05EA0DCF8D29F46D1356B84F2FB4F17FF61`.
- Render: source physical page 76 and target page 1 were independently rendered
  at 300 dpi with critical 600-dpi crops and inspected at original resolution
  without visual defect. Extracted target text has zero forbidden controls.
- Machine evidence: 33 substantive CSV records plus a 27-row exact manifest;
  13 structural JSONL records / 9 stable IDs; 10 difficulty and revision events
  / 8 stable IDs. Rectangularity, formula safety, authority hashes, JSONL parse,
  schema and reference closure, privacy, and exact-manifest gates pass.
  Artifact Tool imported, inspected, styled, and rendered all five CSV tables.
