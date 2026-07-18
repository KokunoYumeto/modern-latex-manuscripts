# Build and independent-review evidence

Evidence date: 2026-07-18

## Bounded unit

- Work: SGA 2, Exposé I, §1.
- Editable source: `working/unit_I_1/SGA2_Expose_I_section_1_English_SourceAligned.tex`.
- Built artifact: `working/unit_I_1/SGA2_Expose_I_section_1_English_SourceAligned.pdf`.
- Output extent: one editable TeX unit and a six-page English PDF.
- French authority: `source_control/french_arxiv/smf_doc-math_4_01.tex`,
  corrected branch, full heading/content envelope lines 87--279 and
  substantive §1 lines 90--279.
- Source coordinates: printed-volume envelope pages 5--12, substantive §1
  pages 6--12; rendered French PDF physical pages 13--17.

## Build gate

The final TeX was built twice with `pdflatex` using nonstop, halt-on-error,
and file-line-error behavior. The retained final log is
`logs/SGA2_Expose_I_section_1_English_SourceAligned_final.log`.

Build engine: MiKTeX-pdfTeX 4.27 (MiKTeX 26.5).

Final log result:

- output written successfully: six pages, 331650 bytes;
- LaTeX warnings: 0;
- package warnings: 0;
- overfull boxes: 0;
- underfull boxes: 0;
- TeX error lines: 0;
- fatal errors or emergency stops: 0.

## Source/formula gate

The source comparison covered all ten numbered statements and every displayed
source label from (1) through (18), including (6 bis), (8'), (8''), (15'),
and (16 bis). It separately checked:

- plain global `Gamma_Z` against underlined sheaf-valued `Gamma_Z`;
- every star, shriek, prime, subscript, and arrow direction;
- `i^*`, `i^!`, `i_!`, `i_*`, `j^*`, and `k^*`;
- global `Hom` against underlined sheaf `Hom`;
- exact-sequence object order and terminal zeros;
- statement numbering and printed-page markers.

The detailed evidence is in `ledgers/SOURCE_FORMULA_COMPARISON.csv` and
`ledgers/SOURCE_ALIGNMENT.csv`.

## Independent review

The first independent review failed one locator detail only: the target's
printed-page-12 marker preceded Proposition 1.8, while the French authority
places printed page 12 at source line 251, within its proof. The marker was
moved to the exact source position and the PDF was rebuilt and rerendered.

The second independent review passed. It explicitly reconfirmed:

- the corrected printed-page-12 marker position;
- all equations, statements, underlines, stars, shrieks, arrows, primes, and
  subscripts;
- the semantic source reading of the translated prose;
- legibility and absence of clipping on the corrected rendered page 5.

Hashes of the independently passed pair:

- TeX: `5341CAB508E6F49B25476E843041A983451A4E950AF0D2A623EECA8D638E8BCA`;
- PDF: `68B924EE8DFE1FFE4709D459D49A4DDCB1B19E94B9909D73CC83BF5D267A1500`.

This pass applies only to Exposé I, §1. It does not certify the recovered
full-volume English witness or the remainder of SGA 2.
