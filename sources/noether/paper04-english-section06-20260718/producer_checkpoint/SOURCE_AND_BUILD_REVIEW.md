# Source and build review

## Source review

- Exact authority span: R823 lines 4045--4110 inclusive, 66 lines.
- Authority whole-file SHA-256: `EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21`.
- Authority slice SHA-256: `F8DDFA72D3BC0A8AC71F77C12C7778B4645907740868102D181436667AFA3031`.
- Original-print scan SHA-256: `D7F7CE6D4B311FFD968ED47DC9C1478CFFCF9F446A86BF90263E0C9D1B41C9EF`.
- Inherited English comparison SHA-256: `200C9F9115C22D93455A3B7AA372687059E539C6D01959D30EEB25BBEEFFE722`.

Ten source-alignment rows partition all 66 authority lines exactly once. Eighteen formula/note rows cover formulas (40), (41), (42), (43), (42a), (43a), (44), and (45), three named theorems, six unnumbered formula structures, and two Clebsch notes.

The original print confirms that R823 line 4048 incorrectly separates the compound `Schlussausdruecke`. The target follows the printed compound semantically, visibly distinguishes the split and compound readings in its footnote, and records the upstream correction debt without exposing a machine evidence identifier in the reader.

The inherited comparison had four substantive regressions. The target removes spurious minus-mu subscripts, restores ordinary-product versus pairing roles, restores the second construction identity's source structure, and uses `min(sigma,n-tau)` in formula (45), as both R823 and the print require.

## Build and render review

The sanitized TeX was copied alone into an isolated directory and built in two halt-on-error pdfLaTeX passes. Pass 1 had only the expected rerun warning. Pass 2 had zero LaTeX/package warnings, overfull or underfull boxes, undefined commands, fatal errors, emergency stops, or rerun requests.

The final reader has two A4 pages, descriptive title/author/subject metadata, no encryption, no JavaScript, and 22 embedded/subset font rows. Both pages were rendered at 200 dpi and inspected at original resolution. No clipping, overlap, broken glyph, margin loss, formula collision, or footnote-flow defect was found.

PDF text comparison against the pre-sanitization working reader changed only the source-defect footnote: it now displays the R823 word break accurately and replaces the machine evidence identifier with public prose. The mathematical body is unchanged.
