# Self-review seal - SGA2-VIII-T21

This seal applies only to corrected French lines 2640-2659: Section 2 heading
and the statement of Theorem 2.1. It is a self-gated bounded unit pending an
independent source seal. It makes no Corollary 2.2, proof, Expose VIII, volume,
critical-edition, public-authority, or publication-readiness claim.

## Source and translation gate

- French TeX authority SHA-256:
  `C2F899E92A904E312B550C6452A117FF23D30AF984B2254A0961D2DF0DACD042`.
- Direct compiled same-edition PDF SHA-256:
  `41AD02C57321A8D2200FF32A929BC93ADBC3DE0D59DCD5A284D28D859FB87A90`.
- Locators: original printed p. 89; physical PDF pp. 78-79; re-composed
  running pp. 70-71.
- Theorem number, three notes, all hypotheses and quantifiers, conditions a)
  and b), local-cohomology notation, both closures, codimension order, and
  equation (2.1) were compared directly with TeX and rendered PDF.
- The jcreinhold e7a259f Markdown remains one comparison-only lineage. Its
  missing theorem numeral, fenced equation, and false original-page-71 locator
  were rejected.

## Build and render gate

- Editable TeX: 2885 bytes; SHA-256
  `56B4A0F8E1C7D8D2F88E70960AA0023BA50E7ADE43B9F6E69EC606B98B54EFB5`.
- Built PDF: 330480 bytes; one unencrypted A4 page; SHA-256
  `CE751502A12C33CD650460850B4C1F01C5134E7BAB3762BBA1BDE9149CF92EF6`.
- Clean `pdflatex` pass 1 and pass 2 succeeded; final diagnostics are zero.
- All 26 font rows are embedded, subsetted, and Unicode mapped.
- Named destinations include `section.2`, `theorem.2.1`, and `equation.2.1`.
- Source pp. 78-79 and target p. 1 were freshly rendered and inspected at 300
  and 600 dpi. No clipping, overlap, lost footnote, lost closure bar, formula
  defect, or continuation-boundary leak was found.
- Target extraction has zero forbidden control bytes and one ordinary form feed.

## Machine gate and cursor

The machine corpus contains 32 substantive CSV rows; 17 structural records / 12
stable IDs; and 14 difficulty/revision events / 10 stable IDs. CSV
rectangularity, formula safety and uniqueness; JSONL parse, schema, parent-child,
stable-ID, revision, and event closure; authority hashes; PDF/font/extraction
checks; manifest exactness; and privacy checks pass.

Exact next cursor: French source line 2661 after blank line 2660.
