# Cayley Vol. I Pages 251-262 Repair Slice

## Source Pages Used

- Source PNGs: `[local source path redacted]` through `p-262.png`.
- OCR helper: `[local source path redacted]`.
- Style/context checked against:
  - `[local source path redacted]`
  - `[local source path redacted]`

## Page Count

- Source scan pages transcribed: 12 pages, PDF pages 251-262.
- Book pages covered: 229-240.
- Compiled output PDF pages: 13 pages, including title/table-of-contents page plus the 12 source-page transcription pages.

## Compile Command / Status

- Command run in this directory:
  `pdflatex -interaction=nonstopmode -halt-on-error cayley_vol01_pages251_262_suspect_draft.tex`
- Status: successful.
- Output: `cayley_vol01_pages251_262_suspect_draft.pdf`
- `pdfinfo` result: 13 pages, A4 page size, PDF 1.5.

## Log Audit

- Log file: `cayley_vol01_pages251_262_suspect_draft.log`.
- No LaTeX errors.
- No actionable LaTeX/package warnings.
- No overfull or underfull box reports found.
- A second compile was run after replacing old-style `\over` fractions, so the table of contents is settled.

## Caveats / Uncertain Formulas

- The source scan itself omits long formulas in paper 35 with dotted placeholders for equations (10), (13), (14), and (20). These omissions are preserved rather than reconstructed from later papers.
- Large determinants in paper 35, equations (11) and (21), were visually compared against the PNGs during the 2026-06-02 repair pass and typeset compactly with zero entries where the scan uses dots.
- Paper 37 continues on PDF page 263; this slice stops at book page 240 with equation (18), matching the assigned range.
