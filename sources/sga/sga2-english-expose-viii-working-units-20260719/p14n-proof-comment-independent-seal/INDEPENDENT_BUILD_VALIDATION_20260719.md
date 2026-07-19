# Independent build validation - SGA2-VIII-P14N

Result: PASS for this bounded internal unit.

- Fresh pdfTeX pass 1 exit: 0.
- Fresh pdfTeX pass 2 exit: 0.
- Final-pass diagnostics: 0 TeX errors, warnings, unresolved references,
  overfull boxes, underfull boxes, missing characters, or fatal errors.
- TeX: 1,977 bytes; SHA-256
  `604193CF5E4DC1B4BE6DA2D0A6280EEF0FDBD464DF8C2F71AA784A2D7B9DB066`.
- PDF: 285,390 bytes; one unencrypted A4 page; SHA-256
  `F9505784012F4DA28123C1F0B7BB6E6BAB0C0731D7D8CB294342A8E7742941DF`.
- Independent pass-1 local-only log SHA-256:
  `16F1593AB46C9B7716D1B5F58603F4C038A2321F84CE727E62987BDD3E9CAFF9`.
- Independent pass-2 local-only log SHA-256:
  `16F1593AB46C9B7716D1B5F58603F4C038A2321F84CE727E62987BDD3E9CAFF9`.
- Font report: 18/18 rows embedded, subsetted, and Unicode mapped; SHA-256
  `6BCC2F708701F3715A40DEAE48C2A90028D58278488DBD75C17BF12F40130E1E`.
- PDF information receipt SHA-256:
  `563945CA7FE3CD6E6741E8AA6C86BBDF90375E0927EF9FF9BB3DA06E22C0358A`.
- Independent target text extraction: 1,649 bytes; one expected form-feed page
  separator and zero other forbidden control characters; SHA-256
  `A1ABFA440166B7648C9A405C5F4F3A7C4D0A4EDCDDF766F8F9F4F47481B8E902`.

The earlier U+0001 extraction defect is absent. The PDF is an internal bounded
reader; it is untagged and has no XMP metadata stream. Those are release-level
caveats rather than failures of this seal.
