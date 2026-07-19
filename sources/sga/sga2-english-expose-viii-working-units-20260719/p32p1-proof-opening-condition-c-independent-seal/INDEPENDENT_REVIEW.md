# Independent review - SGA2-VIII-P32P1

Review ID: `SGA2-VIII-P32P1-IREVIEW-20260719-0001`.

Result: **PASS for this bounded unit**. The target TeX and frozen PDF were not
changed. This is an independent source/formula/build/render/machine/privacy
review, not independent human peer review, archive acceptance, publication, or
certification of a complete Expose VIII or complete SGA2.

## Boundary and authority

The admitted source boundary is corrected French lines 2901-2907. It includes
the proof opening and the complete condition (c), and excludes blank line 2908.
French line 2909, `(a) => (b)`, is the exact continuation cursor. The unit is on
original printed p. 97, crossing physical source-PDF pp. 84-85 and recomposed
running pp. 76-77. The next `pageoriginale` token is at French line 2915, so
physical p. 85 does not make this unit original printed p. 98.

The corrected arXiv TeX is authority: 586,789 bytes, SHA-256
`C2F899E92A904E312B550C6452A117FF23D30AF984B2254A0961D2DF0DACD042`.
The exact LF/no-EOL source slice is 373 bytes, SHA-256
`1E20E77BC16306F1C78586A1CF508B7635CB3266F7B23B05F2BA2EB3DD39280A`;
the CRLF/no-EOL representation is 379 bytes, SHA-256
`131A6EF6E986122AC381B3AD55A8B14E39BCA76595B4C05C03E76369169D8ABD`.

The 216-page French PDF is byte-identical to the recorded same-edition reader,
SHA-256 `41AD02C57321A8D2200FF32A929BC93ADBC3DE0D59DCD5A284D28D859FB87A90`.
Its physical pp. 84-85 renders confirm the page mapping and formulas, but it is
the same corrected edition and therefore not independent corroboration.

## Body and formula audit

The English body preserves all substantive source content:

- coherent extension `G` as an `O_X`-module;
- the restriction `G|_U` and its isomorphism with `F`;
- EGA I, 9.4.3 and the application of Corollary 2.3 to `G`;
- equivalence of conditions (a) and (c), not a one-way implication;
- `for every x in S`, the strict inequality, `prof F_x`, and `n-c(x)`;
- both singleton closures, intersection with `Y`, and codimension argument
  order in the definition of `c(x)`;
- the item label (c), enumeration boundary, and absence of a premature QED.

The jcreinhold e7a259f comparison file is one LLM-generated comparison lineage,
not authority or independent corroboration. Its `x in overline S` reading at
comparison line 653 is a regression: corrected French line 2904 and the visual
source page both read `x in S`. The target correctly rejects that enlargement
of the quantifier domain.

The source does not redefine `Y` inside Proposition 3.2. Corollary 2.3 and the
Section 2 convention use closed `Y` with `U=X-Y`. The target keeps `Y` in the
formula and discloses that inherited context in the authority box. This is an
editorial locator clarification, not a French emendation.

Manager decision `EG-SGA2-FG-NOTATION-ADJUDICATION-20260719-0001` closes Option
A. Target calligraphic F/G are an explicit English normalization from source
upright F/G, never literal glyph preservation. No Z, R, E, or set-minus policy
change is introduced in the translated body.

## Build, extraction, render, and privacy

The immutable target identities are:

- TeX: 2,110 bytes, SHA-256
  `E90C54618D3778DDB0809F21A58BB89F439177672765D4221AE995735310FF2D`;
- PDF: 236,785 bytes, one A4 page, SHA-256
  `393FA644253A6C4CA2EBA700939A02C09B1E4B191934A6BEE92507EB808B7518`.

A fresh independent two-pass `pdflatex` rebuild exited 0/0. Pass 1 had only the
expected rerunfilecheck warning; pass 2 had no warning, overfull/underfull box,
or fatal diagnostic. Its timestamp-variant PDF was 236,785 bytes, SHA-256
`DD9B29F0CB683B56B824672AE25F0DE2A651D86092177D8B4A8932CF28CACAE4`.
Its 1,461-byte layout extraction, SHA-256
`72305041C0D60F4E61E7934F36B760908A1EBD9D5F477081B5C91AC25555D700`,
and 288,680-byte 300-dpi render, SHA-256
`AD63205253E2466A418F3FC0492095FF039A9488872F481B03217FC84D042C67`,
are byte-identical to the frozen QA artifacts. Extraction has zero forbidden C0
controls and one ordinary form feed. All 15 font rows are embedded, subsetted,
and Unicode mapped. The final target render and both source renders were
visually inspected and have no clipping, overlap, broken overline, missing
glyph, or unreadable formula.

The public-text surface was rescanned in ordinary and whitespace-compacted
forms: 27 production public-text candidates, zero private path or profile hits.
Raw logs, auxiliary files, scripts, the same-edition reader, and source-page
renders remain internal. The PDF has no XMP stream and is not tagged; those are
disclosed accessibility/metadata limitations, not body failures.

## Machine evidence

Independent validation passed:

- five substantive CSV ledgers, 54 data rows total, rectangular, unique
  nonempty primary IDs, and zero formula-trigger cells;
- 8 structural JSONL records with closed parent/child and local reference
  links;
- 12 revision JSONL records / 10 stable IDs, including reciprocal
  `@1 -> @2` closure for the quantifier-domain decision and the scalable-to-
  ordinary-parenthesis extraction repair;
- five producer Artifact Tool receipts/previews and five fresh independent
  Artifact Tool imports, full-range inspections, formula-error scans, and
  renders;
- the original 37-row unit-hash and 37-row Zenodo hold manifests, with exact
  path/byte/hash closure and no formula triggers.

The original 37-row manifests remain historical production-hold controls. The
terminal independent seal uses separately named successor manifests so the
pre-seal record is not silently rewritten.

