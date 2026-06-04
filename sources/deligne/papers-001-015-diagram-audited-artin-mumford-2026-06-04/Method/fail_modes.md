# Observed failure modes and fixes

## OCR and symbol failures

- `\kappa(x)` misread as `\chi(x)`. Fix by visual inspection of Greek kappa vs chi.
- `\mathcal J` reduced to plain `J`. Fix by inspecting the glyph and the local use as an ideal/sheaf.
- Prime/double-prime factorization symbols \(\pi'\), \(\pi''\) dropped or merged. Fix by rendering formula crops and checking all primes.
- Matrix entries transposed by text extraction. Fix by reading the rendered image, not the extracted text.

## Diagram and layout failures

- Contraction diagrams can collide or produce visually broken arrows if reconstructed with crude arrays. Use TikZ or aligned displays; render-check the page.
- Cumulative TeX can develop visible gaps if each installment is pasted as a page chunk with forced breaks. The cumulative file must be one continuous paper with only mathematical section breaks.
- Long adèlic expressions and Hom/Isom quotients can overrun margins. Use display equations and, if needed, line breaks with `aligned`.

## Source-packet issues

- Some source PDFs have a useful text layer, but mathematical extraction still corrupts symbols, line order, and matrices.
- Some source PDFs are already typed translations. For the paper lane, include the scan sidecar and state the source used only in the delivery summary, not inside the clean PDF.
- If a source contains obvious typographical damage from a prior typed copy, correct the modern TeX while preserving the mathematics, and leave the scan sidecar for comparison.

## Package hygiene

Paper ZIPs should contain no logs, reports, notes, screenshots, or process files. Keep those in this methodology ZIP.
