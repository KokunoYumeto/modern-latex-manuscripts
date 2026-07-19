# Build validation - SGA2-VIII-L24P

- Two fresh `pdflatex` passes completed successfully after the final
  extraction-safety correction. Both logs contain zero LaTeX errors, warnings,
  undefined-reference diagnostics, overfull boxes, and underfull boxes.
- Final PDF: one unencrypted A4 page, 238809 bytes, SHA-256
  `3A328D88470E36492954511469DD537928FB9D996B9D94C6E10CC8CB7ABBF84E`.
- Editable TeX: 2746 bytes, SHA-256
  `55490989141EAD61491A01B5F19CB085894B6B5A9F94041783D428385074AD8F`.
- Both 24269-byte build logs have SHA-256
  `A1BA050C0FF3B5FFBE018D2099E2C18291441AFC2099424CC83AB64B6F0A087B`.
- `pdffonts` reports 15 font rows; every row is embedded, subsetted, and
  Unicode mapped.
- `pdfinfo -dests` reports exactly `Doc-Start` and `page.1`.
- Poppler inspection used byte-identical short-path copies. The target copy
  retained the final PDF hash above, and the source copy retained authority
  hash
  `41AD02C57321A8D2200FF32A929BC93ADBC3DE0D59DCD5A284D28D859FB87A90`.
- Final layout extraction is 2357 bytes, SHA-256
  `97D27F893B26F91309FD564D5978AAC9E28EE29C5DF807123902EFB993032895`,
  and contains zero forbidden control bytes.
- The final TeX removes only `\bigl`/`\bigr` sizing around the kernel
  argument; the mathematical formula is unchanged. The PDF, logs, target
  renders, extraction, reports, and dependent hashes were regenerated.

Independent validation repeated the build in an isolated directory. Both
passes again report zero diagnostics and one 238809-byte page; independent
extraction and 300/600-dpi target renders are byte-identical to the frozen
evidence. Independent reports again show 15/15 embedded, subsetted, Unicode
fonts and destinations `Doc-Start` and `page.1`.

Public path-sanitized independent logs:

- pass 1: 23025 bytes, SHA-256
  `9335392115CB3F5EEEDEEE438EBA944D86191A042332FC46735F426563EAD743`;
- pass 2: 22894 bytes, SHA-256
  `851EA2FEBDA9BE7D728FB9029CFBE5A700F412D5534D02F4F5466E7C95748814`.

The unsanitized self-build logs, original independent logs, auxiliary TeX
products, short inspection copies, and extracted text are local-only. Only
the two `*_PUBLIC_SANITIZED.log` independent logs enter the checkpoint
manifest.
