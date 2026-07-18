# SGA 5 reopened TeX delta review

Review date: 2026-07-18, Europe/Berlin.

## Exact baselines

- Preserved pre-reopen English TeX SHA-256:
  `3CC5204680B2A2CE92FDF09401AB1A4654F9E0A4B0ED932D110FC0B1B024720F`.
- Repaired English TeX SHA-256:
  `5A79546320606564E0FEF609A13E7F71D42487281325C4CCF97DC20990B7F4C4`.
- French control TeX SHA-256:
  `791F4EFFC5E02832D5D77ED03518C8156D6F07E4C8238B03545DB93D883FBB28`.
- Original LNM 589 scan SHA-256:
  `B256EBD072A8C68209518412A263C9289C6F1854A346733D86F885930D5FE6CA`.

## Exhaustive delta

A `git diff --no-index` against the preserved pre-reopen TeX has exactly three
hunks:

1. the former link-only `\hypersetup` becomes a multiline block with nonblank
   Title, Author, Subject, and Keywords metadata;
2. one explicit editorial footnote is attached to the printed-p.14 Corollary
   1.13 chain; and
3. one explicit editorial footnote is attached to the printed-p.43 ordinary-
   induction display.

An in-memory reverse-delta check removed those exact three additions and
recovered a character-for-character copy of the preserved baseline (796,369
characters; equality true). Thus no inherited translated sentence, displayed
formula, diagram, item, tag, statement, or citation was silently changed.

## Source disposition

At printed p.14 (scan PDF page 26; rebuilt English PDF page 8), the scan and
French control reproduce the defective intermediate `R f_*` term and cite
Proposition 1.12(a)(i) twice. The English display remains source-faithful. Its
new note states that the coherent chain instead needs `R_!f` and (a)(ii).

At printed p.43 (scan PDF page 55; rebuilt English PDF page 26), the scan does
not adjudicate the D-subscript or the first pullback mark. The English retains
the French-control `D_{\ol{x}}` reading and now discloses both the unresolved
glyph and the type-checking pressure toward `D_{\ol{\{x\}}}`. The ambiguity
remains open; the note is not an adjudication.

The corresponding exact decisions and rejected silent alternatives are in
`REOPENED_SOURCE_ADJUDICATION_20260718.csv` and
`TERMINOLOGY_REJECTED_CHOICES.csv`.

## Structural consequence

All pre-existing mathematical/display/diagram counts remain unchanged. Exposé
I now has 10 English footnotes against 8 French footnotes: the exact +2 delta is
the two disclosed editorial notes. It is recorded explicitly in
`STRUCTURAL_PARITY_SUMMARY_FINAL.csv`,
`STRUCTURAL_PARITY_DIFFERENCES_FINAL.csv`, and
`STRUCTURAL_PARITY_REPRESENTATION_REVIEW.csv`; it is not described as source
footnote parity.

