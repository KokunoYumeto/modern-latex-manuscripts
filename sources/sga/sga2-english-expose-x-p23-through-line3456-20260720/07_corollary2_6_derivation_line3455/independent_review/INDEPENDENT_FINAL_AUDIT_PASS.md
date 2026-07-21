# Independent final audit — SGA2 Exposé X, Corollary 2.6 derivation

## Outcome

**PASS.** French line 3455, its boundaries, both proposition-reference
targets, the English sentence, the accepted/rejected register choice,
producer machine controls, fresh build, extracted text, raster, fonts, and
non-time PDF metadata all pass independent review. No source defect or
unresolved ambiguity was found. Producer bytes were not modified, and this
review makes no archive handoff.

## Authority, boundary, and locators

- French authority: 586,789 bytes, SHA-256
  `C2F899E92A904E312B550C6452A117FF23D30AF984B2254A0961D2DF0DACD042`.
- Terminal-LF line-3455 slice: 93 bytes, SHA-256
  `8FF4A86B4B0D2A4CE56FBB97964E24A83F583985CA15FD0C54BDDD0C5BEC8A2D`.
- Coordinates: original printed page 117, physical source-PDF page 101,
  recomposed running page 93.
- Line 3454 is blank and excluded. Line 3456 begins the long `ndetext`
  editor note and is excluded. Raw and substantive cursor: 3456.

The stored source line replays byte-exactly against the authority. The
source page visibly places the complete derivation between Corollary 2.6 and
editor note (3). The PDF is same-edition manifestation and locator evidence
only, not independent original-print corroboration.

## Translation and cross-references

The target sentence “All of this follows immediately from Propositions 1.1
and 2.3.” preserves `Tout ceci`, the derivational relation, and both
references. Coordinating the two repeated French abbreviations under one
English plural “Propositions” does not alter either referent.

Both labels resolve exactly:

- `X.1.1`, authority lines 3327–3329: the natural functor from
  `Et(hat X)` to `Et(Y)` is an equivalence of categories; 213-byte slice,
  SHA-256
  `8D26CF3517241995FD7ABF24F94BC59E5D0BCEE195A494C5C81D21FADB9FF1C5`.
- `X.2.3`, authority lines 3414–3423: the locally free-module, finite-flat
  covering, and étale-covering functors are fully faithful under `Lef` and
  algebraize under `Leff`; 924-byte slice, SHA-256
  `0ADFF5B4A4FDD17DFF772AAF4AFA55FDFE23BC061351A440BC54CAD0ACC43B72`.

No reference is omitted, renumbered, missing, or misdirected. The unit has
no mathematical formula and exactly two structured numerical references.

## Comparison and rejected register

The current jcreinhold e7a259f chapter is 31,425 bytes, SHA-256
`2BDDBC3D15EECE7A47FDBDFBE31DAE735446BC14480A75113E704F63901C7BF5`.
Its line 270 excerpt is 72 bytes, SHA-256
`DE70675A97363E141810E0658E2618A01CFA715A4A9CEDDB22111829B5A113B2`.
It preserves both proposition numbers and ordinary sentence structure, but
uses “follows trivially.” The target’s “follows immediately” preserves the
derivational force in the established English register. “Trivially” remains
an explicitly rejected over-literal comparison choice, not a French source
defect. The candidate remains comparison-only.

## Build, render, and machine controls

Three fresh pdfLaTeX passes completed. Pass 1 has only the expected
`rerunfilecheck` request; passes 2 and 3 have no matched warnings, box
problems, undefined controls, emergency stops, fatal errors, or LaTeX
errors.

- Producer TeX: 1,209 bytes, SHA-256
  `6072C2E73CCD8A9063D9B4671E84059ED699ECF8EB2D480FBC2F9EBEF95CABAA`.
- Producer PDF: 135,713 bytes, SHA-256
  `74E3B33F70C99399096DA0B020C94D7DDB828CE2AD49F1E2DBFD9DB681AFD837`.
- Fresh PDF: 135,713 bytes, SHA-256
  `6507DFF3647DB93828AE248D31B53AFD9D0B5A2715F3DAC142E04B1F22B1FF18`.
- Text, raster, and five-row font table are producer-exact; the PDF-byte
  difference is regenerated metadata only, with non-time metadata exact.

Producer evidence passes: CSV 10×22, JSONL 10 records, and manifest 29×3;
all are parse-clean, rectangular where applicable, formula-safe, unique-ID,
reference-closed, and identity/coverage exact. Artifact Tool 2.8.24 replayed
the producer CSV with exact rendered panels and zero formula errors or
triggers.

Independent evidence contains 14×25 CSV rows and 14 JSONL records. Artifact
Tool imports and renders all 25 columns with zero formula errors or triggers.

## Privacy and disposition

The producer has three path-bearing build/engine logs. The review has seven.
These logs require sanitization or exclusion before public use.

Decision: **PASS**, raw/substantive cursor 3456. The parent may seal this
bounded unit; publication and archive custody remain separate actions.
