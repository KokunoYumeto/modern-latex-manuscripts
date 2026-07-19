# Independent build validation - 2026-07-19

- Fresh pass 1 and pass 2 both exited successfully under `pdflatex` with
  `halt-on-error` and file-line diagnostics enabled.
- The final pass contains zero LaTeX/package warnings, undefined references,
  overfull/underfull boxes, missing characters, or fatal diagnostics.
- Both retained local-only build logs are 7405 bytes with SHA-256
  `C35FAF77D91876F21128E6214BB468C355ED8C10C4A08E7CF711AEE6308DE52F`.
- Final PDF: one A4 page; unencrypted; 250328 bytes; SHA-256
  `F7805D26EE491B48CDC7C7518BF29445D3270510CC6FF22AAF99EBE933A13B7C`.
- Final editable TeX: 2652 bytes; SHA-256
  `2CB397095942C0BD7BD9C849DE660F9D0C3C377235A498B7199B6573F3218195`.
- Font audit: 15/15 reported rows are embedded, subsetted, and Unicode mapped.
- Independent text extraction is 2936 bytes, SHA-256
  `366E9A1A9EC3E177FD112E6F9C9863162F22454CE6B973138B7F91A9BDEF668F`,
  with zero forbidden control bytes.

Status: pass for the bounded internal unit.

