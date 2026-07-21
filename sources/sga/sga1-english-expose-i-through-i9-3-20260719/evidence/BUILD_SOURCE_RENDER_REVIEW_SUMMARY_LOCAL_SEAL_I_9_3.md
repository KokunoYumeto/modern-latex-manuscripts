# SGA 1 I.9.3 — build, PDF, and render summary

The first build attempt is rejected and preserved. It invoked pdfTeX outside
the isolated source directory, so the driver was not found and no PDF was
created. Its console is 580 bytes, SHA-256
`50830D6C6742750489B635D9668B29D20A88FA0E240ADD9BD48CBBBEE4CC952B`.

The clean successor is
`build/i9_3_working_r2_correct_workdir_20260719`. Its copied driver and all nine
fragments are byte-identical to the live sources.

- PDF: 17 A4 pages / 548,916 bytes / SHA-256
  `EB263F584F72C9116B0DD46B1930366B52D12739ADFBFE53958DF8AC9C1F9E4C`.
- Passes 2 and 3 console: each 9,601 bytes / SHA-256
  `98B720B2F1709AE2756DC76DAE6C750BC8FA11DC9650D034C5FB42C2BD7912EE`.
- Passes 2 and 3 log: each 28,611 bytes / SHA-256
  `C26B67A22D3C51377E7829FB05A571874E71D5E694F149A602F2B1F44C4CA2B3`.
- Declared pass-2/pass-3 diagnostics: zero in both logs and consoles, including
  errors, package warnings, undefined references, missing characters,
  over/underfull boxes, and duplicate PDF destinations.
- PDF metadata is populated; it is A4, unencrypted, has no form, JavaScript, or
  attachment, and all 30 fonts are embedded, subset, and Unicode-mapped.
- AUX/PDF destinations contain exactly one `proposition.1.9.3`, alongside the
  two distinct inherited I.9.2 destinations.
- Render: 17 PNG files / 6,554,540 bytes; sorted
  `name|bytes|sha256` LF-final digest
  `54976F68334AB14C9EC3C9590B14FB807644A28C6CC5EADF5B7CC16CDF3FEBD7`.

Independent build review rechecked every identity, diagnostic, font, security,
anchor, extraction, and render assertion and found no blocker. The historical
root PDF remains the prior public locator and was not overwritten.
