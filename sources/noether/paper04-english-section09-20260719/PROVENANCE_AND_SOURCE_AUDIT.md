# Provenance and source audit

## Authority layers

The editable textual authority is the cumulative R823 German TeX, 2,125,031
bytes, SHA-256
`EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21`.
The exact 22-line LF-terminated Section 9 slice is 6,896 bytes, SHA-256
`8829FC38E81C8BD644F863ED08F02C9FA7F5804BE0B6BC4C10E37E7D4BB37E91`.

The 1911 original-print scan was used only to adjudicate glyphs, emphasis,
punctuation, notes, defects, and page boundaries. Its whole-file SHA-256 is
`D7F7CE6D4B311FFD968ED47DC9C1478CFFCF9F446A86BF90263E0C9D1B41C9EF`.
The scan and all source-derived images are excluded.

Inherited English was comparison-only, never textual authority or drafting
substrate. Its whole-file SHA-256 is
`200C9F9115C22D93455A3B7AA372687059E539C6D01959D30EEB25BBEEFFE722`;
the bounded comparison-slice SHA-256 is
`20AB4998B379103BC0F9E255D393DE77ADB0DF7F8FA1741E018EADF2206428BD`.
Both bodies are excluded.

## Audited target

- English TeX: 8,499 bytes; SHA-256
  `2D035DC4571AA2220920AF814AE16E9126E815E95E260A87B5C067C7DA348518`.
- Reader PDF: 269,106 bytes; two A4 pages; SHA-256
  `33DDE37F1F33CD7ADB8D1857C4B0EA05007180B4E47FA58F3C9A9C03561EB4F8`.
- Layout-preserving English extraction: 7,908 bytes; SHA-256
  `3A649C0A7CB4B822A5DCA364C8270F28B622DB6A2EB71A316B13F43A13B8A018`.

All 22 authority lines and every target clause, inline formula, symbol role,
reference, emphasis run, theorem statement, and original note were reviewed.
Section 9 has no numbered or displayed equation; formula (70) belongs to
Section 8 and is not imported. All three original notes are retained with
their page-local identities.

Twelve original-print-confirmed source-defect classes are restored and
disclosed. Three source-faithful controls remain explicit. The inherited
comparison records ten regression classes comprising seventeen physical
losses and three zero-count ambiguity controls.
