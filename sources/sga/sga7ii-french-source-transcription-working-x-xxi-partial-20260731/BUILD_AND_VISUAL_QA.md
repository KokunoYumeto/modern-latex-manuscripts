# Build and visual QA

- Engine: pdfLaTeX
- Passes: four with `SOURCE_DATE_EPOCH=1785456000`; pass 3 and pass 4 PDFs
  are byte-identical
- Result: 201 A4 pages
- Reader SHA-256:
  `6A4569194DBECC1475C46FE6896D01379C637603ABD6FB940B8DAB661EBE1646`
- Fatal, undefined-control, missing-math, and LaTeX errors: 0
- Overfull boxes: one inherited 11.38159 pt paragraph warning
- Underfull boxes: 18 nonblocking diagnostics
- Font resources: 22, all embedded; five inherited Type 3 glyph resources
- Tagged PDF: no

The final clean-source reader was rendered at 200 dpi and directly checked on
pages 1, 112, 141, 188, 190, 191, 192, 197, and 201. Every sampled render is
pixel-identical to the previously reviewed candidate. This set covers the
opening, the sole overfull-warning expose opening, the corrected bidirectional
diagram, both formerly clipped displays, the corrected Galois notation, both
repaired math boundaries, and the exact terminal hard stop. No clipping,
overlap, blank page, or malformed corrected diagram was found. All 201 decoded
page-content streams, extracted text streams, and page boxes also match the
previously reviewed candidate exactly.

Raw build logs are excluded because they contain machine-local paths. The
reader, editable sources, source leaves, and this summary are the durable
surface.
