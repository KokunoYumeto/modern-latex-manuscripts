# Build record

The packaged TeX was copied byte-for-byte into a fresh isolated directory and compiled twice with `pdflatex -interaction=nonstopmode -halt-on-error -file-line-error`.

- Packaged TeX: 10,811 bytes; SHA-256 `259F46CAB6552D09007174CFE9A5BEFC5DBE31FDF6535BF99F5EC0D13C94244A`.
- Packaged PDF: 279,036 bytes; SHA-256 `41E8C1FAA1A2B2305C1A72E7C07A10901DA44AEF07321C045BA2CAF86F9F3D7C`.
- Isolated rebuilt PDF: 279,036 bytes; SHA-256 `E9461EEC05C6D858BD4DDBD15CD5248C9A659FC008A6D76EEDF5A814729BFD39`.
- Packaged and isolated PDF text extractions: byte-identical, 10,871 bytes, SHA-256 `60FD8F5147BEF39C455593B20A3308D086DC08FC9530BBD004D5CE10DAE4906A`.

The rebuilt PDF differs at the container-byte level because it was generated under a different job name and timestamp. Its extracted text and every 200-dpi page render are byte- and pixel-identical to the packaged PDF.

The final isolated pass has zero actionable diagnostics. The PDF has two A4 pages, descriptive title/author/subject metadata, no encryption, forms, JavaScript, or suspicious PDF actions, and 24/24 embedded, subset fonts with Unicode mappings. It is not tagged for accessibility.

