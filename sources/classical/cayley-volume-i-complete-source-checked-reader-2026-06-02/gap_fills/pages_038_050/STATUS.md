# Cayley Vol. I Pages 038-050 Source-Checked Slice

## Source Pages Used

- Primary scan PNGs: `p-038.png` through `p-050.png` from `scan_pngs_vol01_p26_50`.
- Continuity/style references:
  - `cayley_vol01_pages_026_037.tex`
  - `cayley_vol01_pages_051_075.tex`
- OCR/base text aids:
  - `pdftotext -f 38 -l 50 -layout` on `Cayley_Vol_I_source_scan.pdf`
  - `work_vol01_026_050/ocr.txt`

## Output

- TeX: `cayley_vol01_pages038_050_source_checked.tex`
- PDF: `cayley_vol01_pages038_050_source_checked.pdf`
- PDF page count: 13 pages

## Compile

- Command run twice:

```powershell
pdflatex -interaction=nonstopmode -halt-on-error cayley_vol01_pages038_050_source_checked.tex
```

- Status: successful.
- Output reported by log: `cayley_vol01_pages038_050_source_checked.pdf (13 pages, 236403 bytes)`.

## Log Audit

- Overfull boxes: none in final log.
- Underfull boxes: none in final log.
- Warnings: three LaTeX font substitution warnings:
  - `Font shape 'T1/cmr/m/scit' undefined`, using `T1/cmr/m/scsl`.
  - These come from italic text containing small-caps volume numerals in bibliographic headers.

## Caveats / Uncertain Items

- The slice is a text/math transcription, not a facsimile; no scan images are embedded.
- Paper 3 printed pp. 16-18 contains dense formulas carried over from p. 15. The main formulas were visually checked against the PNGs, but the top-of-page p. 16 continuation and the long restored integral formula should be treated as the highest-priority review points.
- Paper 4 uses Cayley's long overbar/brace notation for taking selected terms in Laurent expansions. This was represented with a local `\br{...}` macro using `\overbracket`; the semantic transcription is preserved, but the visual glyph is not an exact typographic duplicate.
- The largest Paper 4 formula blocks, especially equations (38), (42), (43), and (47)-(50), were checked from the scan but remain the most likely places for small subscript/sign errors.
- Paper 6 p. 28 begins only; it intentionally stops before the formulas continued in the neighboring pages 051-075 slice.
