# Build and QA summary

- Frozen wrapper: 10,181 bytes, SHA-256 `71F2D7A16CCEABEDC4E2E3E1F0612B2CA1895583751EB43C7361C6949CBEC2A4`.
- Editable closure: one wrapper plus 137 referenced component files, with no missing or unreferenced component.
- Reader: 198 A4 pages, 1,551,833 bytes, SHA-256 `BF474B377BBFF5BECB561A0FBDBF8E426842F70FDE3043572687D159F864395F`.
- Isolated build: three pdfLaTeX passes, exit codes 0/0/0; pass 2 and pass 3 console output byte-identical; no errors, overfull or underfull boxes, undefined references, missing inputs, or rerun requests. One inherited component-97 font-size warning remains disclosed and is visually harmless.
- Isolated rebuild comparison: 198/198 page geometries, decoded content streams, and extracted texts exact. The rebuilt file differs only in PDF timestamp metadata.
- Reader inspection: 198/198 pages contain extractable text; 38/38 font resources embedded; 8 Type 3 resources; zero image XObjects.
- Direct visual review: pages 181-182 and 196-198 rendered at 600 dpi, covering the Expose VIII/IX join and the terminal section-3.4 pages; no blank page, clipping, overlap, or malformed displayed mathematics found.
- Privacy and reader-surface review: no private absolute path, pending-review note, process note, or internal tooling text in the editable source, PDF metadata, or extracted reader text.
