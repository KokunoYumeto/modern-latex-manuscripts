# Provenance and source audit

## Authority layers

The editable textual authority is the cumulative R823 German TeX, 2,125,031
bytes, SHA-256
`EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21`.
The exact 206-line Section 8 CRLF slice is 15,980 bytes, SHA-256
`632F0D39480AE22CC73DAB2839E5E883110FF5210D6A8C7F5E26C81982778427`.

The 1911 original-print scan was used only to adjudicate glyphs, formulas,
notes, defects, and page boundaries. Its whole-file SHA-256 is
`D7F7CE6D4B311FFD968ED47DC9C1478CFFCF9F446A86BF90263E0C9D1B41C9EF`.
The scan and all ten source-derived image controls are excluded.

Inherited English was comparison-only, never textual authority or formula
substrate. Its whole-file SHA-256 is
`200C9F9115C22D93455A3B7AA372687059E539C6D01959D30EEB25BBEEFFE722`;
the bounded comparison-slice SHA-256 is
`6325DC6DE34F4631453645DEECB2D7065DEADE9BBEC9057E25A5DD1619A7A966`.
Both bodies are excluded.

## Audited target

- English TeX: 17,228 bytes; SHA-256
  `5D579A47B0736102E0AB842A3CD0E1FF2232940226F608CBB33FCF88668CA22A`.
- Reader PDF: 328,554 bytes; four A4 pages; SHA-256
  `779B24EFD7B81006BC5A1994E49A7778422EAEE158320650FA50913F4A9858A3`.
- Layout-preserving English extraction: 17,173 bytes; SHA-256
  `F69D75EEC9557591B1F535279AC8DF0A6F9E2200584BDBCF2D799C0BC7DFB885`.

All 206 authority lines and all 411 target-TeX lines were reviewed. The target
preserves 25 bracket displays, formulas (62)-(70) exactly once, two `align*`
chains, and both original notes. Its six footnotes comprise the two original
notes and four immediate source-defect disclosures.

Three source ambiguities remain explicit: paired bounds in (62), the paired
bound at R823 line 4312, and the coordinated
`alpha_0 = alpha_n = 0` boundary reading after (70).

