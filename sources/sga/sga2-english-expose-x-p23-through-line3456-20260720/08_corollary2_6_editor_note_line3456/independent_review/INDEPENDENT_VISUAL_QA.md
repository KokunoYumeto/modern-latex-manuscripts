# Independent visual QA -- SGA2 Expose X, Corollary 2.6 editor's note (3)

Status: PASS. Review date: 2026-07-20. This is internal review evidence,
not a publication payload or archive handoff.

## Source pages

Both same-edition source-page rasters were inspected at original detail.
They are manifestation and layout evidence only, not independent
original-print corroboration.

- Physical page 101 / printed page 117 / running page 93: the note begins
  below Corollary 2.6 and the line-3455 derivation. The first five note
  sentences are present, including the depth thresholds, purity statement,
  first three fundamental-group map occurrences, the Bost title, acute
  accent in `Ec.`, journal data, pages, and Theorems 1.1 and 2.1. Raster:
  407,075 bytes; SHA-256
  `E59A5DADE48D40EA47B11A4747A72A21ABA090FA09F697F403FC5B4ACD0FB793`.
- Physical page 102 / printed page 118 / running page 94: Section 3 begins
  in the main body while the note continues at the foot of the page. The
  remaining geometric and arithmetic surface cases, nef self-intersection,
  Belyi diacritic, Ihara data, projection-induced map, section-induced
  inverse map, and Theorem 1.2 are present and legible. Raster: 386,852
  bytes; SHA-256
  `70EA3E1FBDB313FDD2F832170D35457AA0BA38A2F1E93FF61C12F99411B813E3`.

The unusual continuation after Section 3 begins is ordinary footnote layout;
it does not change the line boundary or cursor. The rasters remain
rights-gated internal evidence.

## Target and fresh rebuild

The producer render and independently regenerated render were inspected at
original detail. Both are byte-identical:

- 200-dpi PNG: 419,804 bytes; SHA-256
  `BBC2E912CFA9BCC0B255FE4B6807978F8868D2EEF9A2C72E0790571E80BC5BB5`.
- Page count: 1; page size: A4.
- No clipping, overlap, black box, missing glyph, broken arrow, malformed
  subscript, or footer defect was found.
- All five map occurrences are directionally legible. All eight `pi_1`
  tokens render correctly.
- The depth thresholds, purity and complete-intersection language, positive
  self-intersection, Bost and Ihara citations, acute `Ec.`, Belyi diacritic,
  lowercase `noetherian`, and the visible accepted-normalization note are
  legible.
- Fourteen font rows are embedded, subsetted, and Unicode-mapped; font-table
  SHA-256
  `2FCFC61208B42C0D8EEA48E94E1688FF116735FD0EF54B7FEBE897D89A347D18`.

The fresh PDF has the same 275,147-byte size as the producer PDF. Its PDF
bytes differ only because the creation and modification timestamps were
regenerated. Extracted text, raster, font table, and all non-time PDF metadata
match exactly.

## Machine-evidence panels

Artifact Tool 2.8.24 independently imported and rendered the producer CSV as
three complete panels: `A1:H33`, `I1:P33`, and `Q1:V33`. It also rendered the
36-row independent evidence CSV as `A1:J37`, `K1:T37`, and `U1:AB37`.
Every panel was inspected at original detail. Headers, IDs, source locators,
readings, statuses, cursors, hashes, actual review timestamps, release state,
and notes are visible. Formula-error and formula-trigger counts are zero.

The initial review-only render allowed blank revision-link columns to collapse
and displayed the ISO timestamp as an unformatted serial. The review script
was corrected to set explicit widths and a `yyyy-mm-dd hh:mm:ss` format, then
rerun. This changed no CSV or producer byte.

