# Build and extraction validation - self gate

- `pdflatex` ran twice with `-interaction=nonstopmode -halt-on-error`.
- The final pass has no LaTeX error, warning, undefined-reference, rerun,
  overfull-box, or underfull-box diagnostic. Package names containing the word
  `rerun` are informational only.
- Output: one unencrypted A4 page, 291362 bytes. Exact final hashes are recorded
  in `UNIT_HASHES.csv` and `MACHINE_READABLE_VALIDATION.json`.
- All 22 font rows reported by `pdffonts` are embedded, subsetted, and Unicode
  mapped.
- Text extraction preserves the visible Corollary 2.2 number, note marker (3),
  condition c), exponent `i-1`, and the complete editor-note chain. Spacing in
  extracted prime marks is a PDF text-layer artifact; the rendered primes are
  visually correct.
- Poppler could not inspect the target reliably at its very long final path.
  The exact PDF was copied byte-for-byte to the short internal inspection path
  `tmp/pdfs/sga2_c22/target.pdf`; hashes were checked equal before inspection.
  The short-path copy is not part of the unit manifest.

Status: build and extraction self-review pass. A fresh isolated rebuild closed
the independent gate; see `INDEPENDENT_BUILD_VALIDATION_20260719.md`.
