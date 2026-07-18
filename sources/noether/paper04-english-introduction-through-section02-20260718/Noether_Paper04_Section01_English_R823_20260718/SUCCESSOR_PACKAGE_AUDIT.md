# Successor package audit

This `r2` directory is a sanitized successor to an unpublished local package that was held before repository preservation. The predecessor remains separate and unchanged. This successor supersedes no public artifact or repository version.

## Artifact preservation

- The editable TeX, reader PDF, three visual-QA images, three scholarly ledgers, and four substantive review/caveat documents copied from the predecessor are byte-identical: twelve artifacts in all.
- Only `README.md`, `PUBLICATION_READINESS.md`, and the descriptive role in the fourth ledger, `SOURCE_CONTROL_HASHES.csv`, were changed to use neutral repository language.
- The predecessor hold notice and its obsolete generated inventories are excluded.

## Independent build and PDF checks

- The preserved TeX SHA-256 is `47A3BCC58743A9C34441255DD23518FBA38DD804C5D37220439F1F883DCC0CDF`.
- Two fresh pdfLaTeX passes exited successfully. The final log contained no actual LaTeX/package warning, overfull or underfull box, undefined control sequence, fatal error, or emergency stop.
- The fresh rebuild produced two A4 pages and the same 240,446-byte file size. Its byte hash differs because pdfTeX records a new creation time, but its extracted text is byte-identical to the preserved PDF: 5,307 bytes, SHA-256 `2D4532571606CF867C3F5B48A67F5DD307C47C2765D89C01774EDE827C13A35F`.
- The preserved reader PDF SHA-256 is `815F9063D1313CC7E615B31C5EF22FA4867657DB33A6D1359D1092AA6CDC6123`. It has two unencrypted A4 pages, nonblank title/author/subject/keyword metadata, no forms or JavaScript, and eighteen embedded, subsetted fonts with Unicode mappings.
- Fresh 180 dpi renders of both rebuilt pages were decoded and visually inspected. The preserved page renders and contact sheet were also inspected. No clipping, overlap, missing glyph, black box, broken formula, unintended blank page, or illegible element was found.

## Package hygiene and tabular checks

- Text, normalized whitespace/slashes, PDF metadata and extracted text, raw file bytes, and PNG metadata were scanned for machine-specific user paths, personal user names, task/thread identifiers, UUIDs, and internal-workflow nomenclature; no hit remained.
- The four scholarly CSV ledgers are UTF-8-readable and rectangular: 7 formula/symbol rows, 6 source-alignment rows, 4 source-control rows, and 10 terminology/adverse rows. No cell begins with a spreadsheet formula trigger.
- The two generated inventories were recomputed against the frozen tree and validated for exact path, byte-size, and SHA-256 agreement.

This audit establishes packaging, build, render, and hygiene evidence for this bounded checkpoint. It does not add a claim of complete Paper 4 coverage, critical editing, mathematical certification, peer review, external scholarly validation, or rights determination.
