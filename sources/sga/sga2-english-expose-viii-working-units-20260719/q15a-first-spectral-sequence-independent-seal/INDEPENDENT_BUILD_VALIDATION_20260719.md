# Independent build validation - 19 July 2026

Unit `SGA2-VIII-Q15A` was rebuilt from the final TeX in a new short-path
directory and again in the unit directory. Both two-pass `pdflatex` sequences
ended with zero errors, warnings, overfull boxes, underfull boxes, or PDF
destination diagnostics on pass 2.

- Final TeX: 2,335 bytes; SHA-256
  `A10FA6B313AC43CE5BA790E925BEE38BB83CC36EDDE87D059CBD3B7ED0444F67`.
- Final unit PDF: 201,828 bytes; SHA-256
  `EB9AEB01104D8635C1177C595301D60024FA40359BE954964CB71F6BCF1EC4F0`.
- Independent clean-build PDF: 201,828 bytes; SHA-256
  `76A27F61BDA44F7AD09938455BD11590F8D4B7BDD90137BC6824D4E625D4D871`.
  The byte difference is build-time PDF metadata; both render to identical
  target PNGs.
- PDF properties: one unencrypted A4 page; no forms or JavaScript.
- Fonts: 11 of 11 reported rows are embedded, subsetted, and Unicode-mapped.
- Text extraction: zero forbidden control characters; one normal form-feed
  page separator.
- Equation auxiliary destination: automatic label `(1.5)` resolves as the
  unique `equation.5` destination after the counter is initialized to 4.

The installed Poppler executable could not open the final PDF through its very
long absolute path. The exact final PDF was therefore copied byte-for-byte to
a short inspection directory for `pdfinfo`, `pdffonts`, `pdftotext`, and final
rendering; its SHA-256 was checked before and after that operation. This is a
tool-path workaround, not a content substitution.

Status: independent build gate passed for this bounded internal unit.
Cumulative integration and publication remain open.
