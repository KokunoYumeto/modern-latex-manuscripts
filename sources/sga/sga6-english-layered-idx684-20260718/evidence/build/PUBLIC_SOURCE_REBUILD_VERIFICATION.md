# Public-source rebuild verification

Date: 2026-07-18  
Result: **PASS**

After public-language sanitization, the twelve TeX files in `source/` were
copied, without any other project files, to a fresh verification directory and
compiled twice with pdfLaTeX.
Dependency closure was therefore tested against the exact proposed public
source set rather than against the larger production workspace.

- TeX files available: 12/12
- compile passes: 2/2 successful
- stabilized diagnostics: 0 errors, 0 warnings, 0 overfull boxes, 0 underfull
  boxes, and 0 undefined references
- rebuilt PDF: 377 A4 pages
- rebuilt PDF SHA-256:
  `B67BDEBF0001AEB015209BB7CC6179A0041DED937BE655C7960911A9AA62475D`
- layout-preserving text extraction from the frozen and rebuilt PDFs was
  byte-identical; both have SHA-256
  `53D51EAFD45862AA2CCD7CB01A2A8C57384186909DA06318E20E28CE771B52AB`.

The rebuilt PDF hash differs from the frozen reader hash because PDF creation
metadata is generated at build time. Page count, page size, source structure,
and stabilized build diagnostics agree. This verification did not alter the
frozen 377-page reader in `reader/`.
