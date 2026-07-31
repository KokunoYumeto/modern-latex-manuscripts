# Build and QA summary

- Frozen wrapper: 8,479 bytes, SHA-256
  `89F8F81E122829C86ADB9EB8C93895A7EC8FA6417B156081C425E0EE1A4D5EE3`.
- Editable closure: one wrapper plus 108 referenced component files, with no
  missing or unreferenced component.
- Reader: 160 A4 pages, 1,277,083 bytes, SHA-256
  `52F65D358E1F4ADCDD947D8993E98AD395E986CBFE1AB6FB6C3711574B01D2FA`.
- Isolated build: three pdfLaTeX passes, exit codes 0/0/0; pass 2 and pass 3
  console output byte-identical; no errors, warnings, overfull or underfull
  boxes, undefined references, missing inputs, or rerun requests.
- Independent rebuild comparison: 160/160 page geometries, decoded content
  streams, and extracted texts exact. The rebuilt file differs only in PDF
  timestamp metadata.
- Reader inspection: 160/160 pages contain extractable text; 37/37 font
  resources embedded; seven Type 3 resources; zero image XObjects; zero
  internal links or named destinations.
- Direct visual review: pages 134-135 and 159-160 rendered at 600 dpi, covering
  the Expose VII/VIII join and the terminal Proposition 3.7 page; no blank page,
  clipping, overlap, or malformed displayed mathematics found.
- Privacy and reader-surface review: no private absolute path, pending-review
  note, process note, or internal tooling text in the editable source, PDF
  metadata, or extracted reader text.
