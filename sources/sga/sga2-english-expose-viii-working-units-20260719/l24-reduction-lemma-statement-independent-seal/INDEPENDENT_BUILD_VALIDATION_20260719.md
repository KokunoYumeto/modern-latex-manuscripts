# Independent build validation - SGA2-VIII-L24

The frozen TeX was copied byte-for-byte to a clean isolated build directory.
Its SHA-256 was
`0F1477028F6C2004622BF3D67B296024DD38EC92EC9788F86F812901349ECC3E`,
equal to the frozen unit TeX.

Two fresh `pdflatex` passes completed successfully. Pass 1 contained only the
expected first-run rerun-file warning; pass 2 contained zero warnings, errors,
overfull boxes, underfull boxes, undefined references, or missing-character
diagnostics. Complete privacy-sanitized logs are retained as
`INDEPENDENT_BUILD_PASS1_SANITIZED.log` and
`INDEPENDENT_BUILD_PASS2_SANITIZED.log`; raw logs and the isolated PDF remain
local-only and outside the checkpoint manifest.

The isolated PDF is one unencrypted A4 page, 231209 bytes, SHA-256
`35C7D3E929D0B7CA2B9DDAC383BC63289EF3EE272C34C971B3BE9C4BE2DEF496`.
All 14 font rows report embedded=yes, subset=yes, and Unicode=yes. Named
destinations are `Doc-Start`, `lemma.2.4`, and `page.1`. Extracted text
contains zero forbidden C0 controls and is byte-identical to the frozen
checkpoint extraction, SHA-256
`AE595B1F747DD15F71A1934EF0CEDFCB571D94A1C33FAAA7CC70AE71D4E9CBC3`.

The frozen checkpoint PDF remains the earlier clean build, 231209 bytes,
SHA-256
`B94EF7A72A3C1A9B363FBA9F632B8BAFE1535DCBEF365C618EE7C20D33423FEB`.
Its different hash is expected because PDF creation/modification metadata is
timestamped. Independent 300 and 600 dpi target renders are byte-identical to
the frozen target renders.

Status: independent build, extraction, font, destination, and reproducibility
pass.

