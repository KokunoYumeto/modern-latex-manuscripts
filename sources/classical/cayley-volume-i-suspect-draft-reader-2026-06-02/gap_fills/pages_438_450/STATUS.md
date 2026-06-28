# Cayley Vol. I, PDF pages 438--450

## Output

- `cayley_vol01_pages438_450_suspect_draft.tex`
- `cayley_vol01_pages438_450_suspect_draft.pdf`

## Compile Status

- Compiler: `pdflatex -interaction=nonstopmode -halt-on-error cayley_vol01_pages438_450_suspect_draft.tex`
- Status: successful
- Final PDF page count: 13
- PDF page size: A4
- Source slice covered: PDF pages 438--450, corresponding to printed book pages 416--428

## Warnings

- Overfull boxes: 0
- Underfull boxes: 0
- LaTeX/package warnings: 0 actual emitted warnings in the final log

## Source Checking Notes

- OCR was used as the first pass, then checked against the supplied PNG page images.
- Formula-heavy pages 418--420 were checked against the higher-resolution images where available.
- The normalized matrix on printed page 418 uses diagonal `1`s; printed page 420 later introduces the separate abbreviation `l`.
- The source-page breaks were kept manually in the TeX so the PDF has one compiled page per source page.
- No screenshots, facsimile images, or placeholder pages are included in the PDF.

## Caveats

- No formula was judged impossible to reconstruct from the scan.
- Paper 74 begins on the final page of the slice and continues in the neighboring slice. This output stops at the visible end of printed page 428, after the displayed formula ending with a comma.
