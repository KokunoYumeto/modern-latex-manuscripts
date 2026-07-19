# Independent build validation - SGA2-VIII-C23-POC

The exact frozen TeX, 2970 bytes and SHA-256
`118405B69862ED1FA9E9710D100D214A1C847D0F54DB99054AB5BD8D7AAE08E2`,
was copied to an isolated temporary directory and built twice with
`pdflatex`. Both passes exited zero; pass 2 contained no warning, error,
undefined-reference, rerun, overfull-box, underfull-box, or missing-character
diagnostic. Privacy-sanitized logs are preserved; raw logs remain local-only.

The independent PDF is one unencrypted A4 page, 271312 bytes, SHA-256
`1247F2C6647BD6998D34F7640C7EFD4912E586E397047A98E83FC9B25012EF49`.
All 20 font rows are embedded, subsetted, and Unicode mapped. Three named
destinations are present. Extracted text has zero forbidden control characters
and contains the complete body and editor note (5).

The frozen PDF remains 271312 bytes, SHA-256
`47D12027336F93169F5CDDDF7FB7F7AD34BCF51C5E43CD02FFDFD6D3C79647DA`.
Its hash differs from the isolated PDF because build metadata is timestamped;
extracted text is identical and all six independent renders are byte-identical
to the self-gate renders.

Status: independent build, extraction, font, and destination pass.
