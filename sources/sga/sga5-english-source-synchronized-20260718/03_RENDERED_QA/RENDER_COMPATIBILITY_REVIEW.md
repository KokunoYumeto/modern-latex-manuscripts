# Contact-sheet compatibility review

Review date: 2026-07-18, Europe/Berlin.

The private contact-sheet sources comprised twelve 16-bit sRGB PNGs and four
16-bit grayscale PNGs. Four grayscale sheets—pages 141-160, 161-180, 201-220,
and 301-309—appeared blank in one application viewer despite containing image
data.

All sixteen bundled contact sheets were regenerated from the preserved private
copies as PNG24, 8-bit sRGB images. Pixel dimensions and page-range filenames
were preserved. Exact private-source and packaged bytes, formats, and SHA-256
values are recorded row by row in
`RENDER_COMPATIBILITY_NORMALIZATION.csv`.

Programmatic checks reopened every normalized PNG and confirmed the expected
dimensions. The four formerly viewer-blank sheets were then opened at original
detail and visually inspected; all four are populated with the expected page
content. The normalization is a publication-compatibility transform of
English-reader contact sheets, not OCR, source-scan evidence, or a change to the
PDF.

The private original contact sheets remain unchanged outside this bundle.
