# Source and build review

## Source review

- Authority whole-file SHA-256: EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21.
- Authority slice, R823 lines 4112--4268: 13,024 bytes; SHA-256 6A693F9E3936CDD0EC07DE8B66C925839CA989FC5D80932D5D8916E5B1AD5CFA.
- Original-print scan SHA-256: D7F7CE6D4B311FFD968ED47DC9C1478CFFCF9F446A86BF90263E0C9D1B41C9EF.
- Inherited English comparison SHA-256: 200C9F9115C22D93455A3B7AA372687059E539C6D01959D30EEB25BBEEFFE722.

Latest source-alignment revisions partition all 157 authority lines exactly once. Thirty-four formula/note rows cover formulas (46)--(61), nine unnumbered displays, four original source notes, both defining properties, and Theorem VII.

The print governs five confirmed source-defect occurrences. R823 line 4121 has strict rho < n, while the print has rho <= n; formula (54) and the later explicit rho = n case corroborate inclusion. R823 line 4183 drops dots from complementary q and p, line 4187 substitutes a prime for the printed dotted p, and line 4189 drops the dotted p in prose. The reader restores and immediately discloses all five readings. Specialist interpretation of the dotted complementary notation remains external-review debt.

Two inherited-English formula regressions are repaired: the inclusive relation sigma >= tau and the defining equality for Delta. Three non-silent judgments remain explicit: formula (46) uses the equivalent min(tau,n-sigma) notation; formula (48) follows the coherent R823 multiplication continuation; and the passage after (56) follows R823's internally consistent rho dummy index rather than the print's sigma dummy index.

## Build and render review

The sanitized TeX was built alone in three halt-on-error pdfLaTeX passes. Pass 1 had only the expected outline rerun notice. Passes 2 and 3 had zero warning, box, undefined-command, fatal, emergency-stop, or rerun diagnostics. TeX SHA-256: 55F55AF1A09AE756B449FF119EF98EFB5E9B7AB15E52A9F49A330BFA8AFDB7F3. PDF SHA-256: 657894B2F36996FD5AC543113E32C5C7D8B723C8959ECB9E482673D7C97E6CF5.

An independent fresh three-pass rebuild also succeeded; its passes 2 and 3 had zero diagnostics. Packaged and fresh layout-preserving text extractions were byte-identical: 16745 bytes, SHA-256 DB26F14773E5D452F31A34F05C28A1032558F55E6DC95D59D04F3FFD68D5BF13. All three fresh 200-dpi page renders were byte- and pixel-identical to the packaged renders (absolute error 0).

The PDF has three A4 pages, descriptive metadata, 22/22 embedded subset font rows, no encryption, JavaScript, attachments, forms, collection, or unsafe action. Its initial action and eight annotations are internal GoTo navigation only. Tagged: no is disclosed; accessibility conformance is not claimed.
