# Build-log sanitization

All three logs and consoles came from the isolated public rebuild and were
scrubbed of the private build root, working-tree root, user-home path, and
personal workspace tokens. The verifier scans every public text file for any
residual private path or identifier. Passes 2 and 3 have zero configured TeX,
LaTeX, package, reference, box, rerun, missing-character, pdfTeX ext4, or
duplicate-destination diagnostics. Unsanitized outputs remain outside.