# Visual QA — independently audited bounded checkpoint

Method: the freshly rebuilt checkpoint PDF was rendered with Poppler at 300 dpi. All seven PNG pages were inspected at original resolution, page by page. PDF structure was separately checked with `pdfinfo`, text extraction with `pdftotext`, and font structure with `pdffonts`.

## Independent result

- Seven of seven target pages rendered and were independently inspected.
- Page size is A4 throughout.
- All 24 reported font rows are embedded, subset, and Unicode-mapped.
- Headers, rules, page numbers, display mathematics, tables, source notes, and footnotes are visible without clipping, collision, or overlap.
- The title-state change is confined to front matter outside the twelve component bodies.
- No French source raster or source-page render is included in this payload.

## Fresh render inventory

| Page | Bytes | SHA-256 | Result |
|---:|---:|---|---|
| 1 | 666,533 | `2BB4CEDC89798A5DFA9E0222F31073A96E4E2080ADB29EF860B2151DA692FCFB` | passed original-resolution inspection |
| 2 | 530,763 | `D53A771B3194AA1E2D19BD54F026B2AE1CC1A993676E583D32CC09E11044203F` | passed original-resolution inspection |
| 3 | 526,043 | `364A25CBC5A7DACF4FCBAE6C0C184E5C208DDEE0A08ED8953BCA5B282D59BD90` | passed original-resolution inspection |
| 4 | 520,606 | `131E65FF4481733338ECE34C8AEE549FF39611940A8ED33B341283719F79051E` | passed original-resolution inspection |
| 5 | 509,884 | `F165376F213F149CDE0CF7E01FBD6EF973143278D3A844F1A58B331EEC1A5D9C` | passed original-resolution inspection |
| 6 | 330,073 | `0B49D3271ADF130C822112445C4B288C7A7D8C2F60EB381C8CB38E1A373421DB` | passed original-resolution inspection |
| 7 | 389,027 | `BC73C1FC3461BCB10A84BD0C3925F7C44D09003DDE653C658F5A383DF8F6C9D5` | passed original-resolution inspection |
