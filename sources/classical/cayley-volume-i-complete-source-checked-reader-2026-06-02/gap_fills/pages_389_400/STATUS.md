# STATUS

Slice: Arthur Cayley, Collected Mathematical Papers, Volume I, PDF pages 389--400 (book pages 367--378).

## Output Files

- `cayley_vol01_pages389_400_source_checked.tex`
- `cayley_vol01_pages389_400_source_checked.pdf`
- `STATUS.md`

## Source Checking

- OCR was used as the first pass.
- Page starts/ends, paper titles, mathematical displays, and equation layout were checked against the local PNG page images `p-389.png` through `p-400.png`.
- Higher-resolution images were used where available for formula-heavy pages: `hi-p389-389.png`, `hi-p390-390.png`, `hi-p394-394.png`, `hi-p395-395.png`, `hi-p397-397.png`, and `hi-p398-398.png`.
- Neighboring completed slices were used for preamble and formatting style.

## Compile

- Command: `pdflatex -interaction=nonstopmode -halt-on-error cayley_vol01_pages389_400_source_checked.tex`
- Runs: 2
- Status: success
- PDF page count: 8

## Warnings

- Overfull boxes: 0
- Underfull boxes: 0
- LaTeX warnings: 0
- Rerun warnings: 0

## Caveats

- No screenshots or facsimile placeholders are used in the PDF.
- No formula was judged impossible to reconstruct.
- The large determinant on PDF page 395 / book page 373 was typeset as a sparse LaTeX matrix reconstructed from the printed equations and syzygies, and checked against the visible scan entries.
- On PDF page 390 / book page 368, the coefficient is transcribed as the coefficient of `a^{2n}` in `f a`; this follows the scan context and the degree statement for `(F a)^2`.
