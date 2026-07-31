# Build and QA summary

- Frozen wrapper: 9,639 bytes, SHA-256 `5F961FCF47C38663922F251502CB36165328A851769E675D63B037A152BBEE94`.
- Editable closure: one wrapper plus 127 referenced component files, with no missing or unreferenced component.
- Reader: 181 A4 pages, 1,433,416 bytes, SHA-256 `21A9DC25B45F1D67450675F46E6374791483C88F6DBAA051C4B4BF133675361D`.
- Isolated build: three pdfLaTeX passes, exit codes 0/0/0; pass 2 and pass 3 console output byte-identical; no errors, warnings, overfull or underfull boxes, undefined references, missing inputs, or rerun requests.
- Isolated rebuild comparison: 181/181 page geometries, decoded content streams, and extracted texts exact. The rebuilt file differs only in PDF timestamp metadata.
- Reader inspection: 181/181 pages contain extractable text; 37/37 font resources embedded; 7 Type 3 resources; zero image XObjects.
- Direct visual review: pages 134-135 and 180-181 rendered at 600 dpi, covering the Expose VII/VIII join and the terminal Expose VIII pages; no blank page, clipping, overlap, or malformed displayed mathematics found.
- Privacy and reader-surface review: no private absolute path, pending-review note, process note, or internal tooling text in the editable source, PDF metadata, or extracted reader text.
