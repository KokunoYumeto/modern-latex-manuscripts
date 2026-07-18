# PDF text-extraction check

Both final PDFs were processed with `pdftotext -layout` after the visual check.

- extraction exit code: `0` for both PDFs;
- target-language body text, mathematical variables, headings, and footer text
  were returned;
- no replacement-character or empty-text failure was observed;
- line-break hyphenation in the lower status sentence is a layout artifact, not
  a missing-glyph condition.

This check is diagnostic only. The TeX files remain the authoritative editable
target text within this tranche.
