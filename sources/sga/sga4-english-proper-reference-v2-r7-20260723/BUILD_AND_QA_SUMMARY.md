# Build and QA summary

## Frozen identities

- Source projection: 300 files; tree SHA-256
  `AE306A05563020D4996679269C52EDFC80EBB0861A10CBC31CB581D71A90C92D`.
- Master TeX: 3,741 bytes; SHA-256
  `3B9D15ACC5F102CA399823DA5A0C1AF58254F85B4DF696214922E1399AD7BB1B`.
- Reader PDF: 4,421,240 bytes; 864 pages; SHA-256
  `A4057C39E5BF54AD12E7B2E5DBBACA884B9738F376B3418E8D97EDAB4E3A88B2`.
- Source ZIP: 1,195,997 bytes; SHA-256
  `1818A02307853ABDC138643EEAB6B062D8D34531FE083400251AEAD5B03D3580`.
- QA ZIP: 5,194,387 bytes; 54 members; SHA-256
  `5502E8EC5C7B59A8CB3776E690BA3349EC70D957C0D73ADD90435F2E149C26A6`.

## Build and reader checks

A clean extraction of the source ZIP passed three XeLaTeX runs, producing 860,
864, and 864 pages. The final AUX hash is
`953E7B393E98373E06E2EBAA8C648F115768C4BA19AAE95AD45CB548B0A044F3`.
There are no fatal errors, undefined references, multiply-defined labels,
duplicate destinations, missing characters, rerun requests, or visible `??`.

The frozen and clean-rebuilt PDFs agree across all 864 pages on extracted text,
word geometry, page geometry, and 72-dpi grayscale raster. Destination, action,
outline, font, and metadata content also agree except for creation time.
The reader has 9,421 named destinations, 6,800 internal GoTo actions, two URI
actions, 183 outline entries, and 17 of 17 fonts embedded.

Sixty-three pages were rendered at 144 dpi: the rights page, repaired diagrams,
formula/glyph/link targets, and both sides of all 20 exposé transitions. Five
contact sheets were reviewed with no visible blocker.

## Complete reference graph

The QA archive includes co-current `REFERENCE_CANDIDATES.csv`,
`REFERENCE_TARGETS.csv`, `REFERENCE_EDGES.csv`, and
`REFERENCE_RESIDUALS.csv`, plus the full source-closure and revision controls.
All 8,701 candidate IDs and occurrence keys are unique and map bijectively to
8,701 residual dispositions. Exactly 5,998 linked candidates each own one
candidate-bound edge. The other 2,703 candidates own no edge and have a closed
positive-nonedge disposition. The 116 supplemental source records and their
116 edges are unique and disjoint from candidate IDs. Hence the exhaustive edge
partition is `5,998 + 116 = 6,114`, with no omission, duplicate, or conflicting
active disposition.

The QA ZIP self-excluding manifest has 53 rows, covering 22,542,243 bytes, and
SHA-256 `5D741DA91A03C162F8DE4B8B1B74C2A8BB3F069A9D9D9CF02B3C85C08101792C`.
All packaged CSV files are rectangular and formula-safe; JSON and JSONL parse;
private paths, raw local logs, scans, and superseded package evidence are
excluded.
