# Build validation

The final TeX was built twice with `pdflatex -interaction=nonstopmode
-halt-on-error`. Both processes exited 0. The final pass contains no LaTeX
warning, overfull box, underfull box, or fatal diagnostic. Public transcripts
are whitelist-sanitized; raw dependency-bearing logs and the sanitizer remain
under `internal_private` and are excluded from any release payload.

- TeX: 2,110 bytes; SHA-256
  `E90C54618D3778DDB0809F21A58BB89F439177672765D4221AE995735310FF2D`.
- PDF: 236,785 bytes; SHA-256
  `393FA644253A6C4CA2EBA700939A02C09B1E4B191934A6BEE92507EB808B7518`.
- Pass-1 sanitized log: 1,119 bytes; SHA-256
  `60C3BED16E698810E272DEC53CDEEE8DC2B1CB5E09DEC17EBD5342A743579577`.
- Pass-2 sanitized log: 1,119 bytes; SHA-256
  `62615A99711619CB8FFCD55F4BD04B8B9C3DC66FEC2FBC0AA358A073C9EC7B57`.

The final PDF is one unencrypted A4 page. All 15 font rows are embedded,
subsetted, and Unicode mapped. Plain and layout-preserving extraction are
searchable. Final extraction contains zero forbidden C0 controls and one
ordinary form feed. PDF metadata has no XMP stream and the PDF is not tagged;
these are disclosed publication-quality limitations, not body failures.
