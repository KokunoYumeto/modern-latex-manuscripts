# EGA I reader-clean R2 build summary

Date: 2026-07-30

Status: **PASS**

- Build sequence: BibTeX once, then five XeLaTeX passes.
- XeLaTeX passes 4 and 5 were byte-identical at SHA-256
  `A51AA18FC0CFF58547EBE0902EB7BC8B068BC6AE4049475DF676B90FD3FEB24C`.
- Compiled source PDF: 779,062 bytes, SHA-256
  `E2B5A407C92A131E27073DB07B05AC27CFA532B52705C9AC88D9942247882024`.
- Final stable-link reader: 1,356,401 bytes, 113 pages, SHA-256
  `0DC301F1998AA4E6A97ABD92197BB94A3F7FBEE1847261CC7BB69E0F8E6D8C58`.
- Release-blocking diagnostics: 0.
- Retained nonblocking diagnostics: 2 font-substitution warnings, 18 overfull
  boxes, and 2 PDF-string warnings.
- Final reader resources: 21/21 fonts embedded and subset, Type 3 fonts 0,
  raster image XObjects 0.

Raw engine logs are intentionally excluded because they contain host-local
paths. The package includes the build script, exact source closure, graph
ledgers, and read-only package verifier needed for independent replay.
