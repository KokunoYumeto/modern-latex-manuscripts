# Build record

The final TeX was compiled twice with pdfLaTeX in nonstop, halt-on-error mode after removing stale auxiliary and outline files. Both final passes exited successfully.

The first diagnostic build produced duplicate PDF destinations for manual source formula tags. The final source sets `hypertexnames=false`, preserving visible tags (1)–(6) while removing the collision.

The final PDF parses as two pages. The final log has no actual warning, overfull/underfull box, fatal error, or emergency stop. The remaining literal word “warning” belongs only to the loaded `infwarerr` package description.

Both pages were rendered at 180 dpi and inspected. Raw build logs are excluded because they contain machine-specific paths.
