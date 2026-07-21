# Independent visual QA — SGA2 Exposé X, Corollary 2.6 statement R2

Status: **PASS**. This is internal review evidence, not a publication or archive handoff.

## Source page

I inspected `../SOURCE_PHYSICAL_PAGE_101_200DPI.png` at original detail
(407,075 bytes; SHA-256
`E59A5DADE48D40EA47B11A4747A72A21ABA090FA09F697F403FC5B4ACD0FB793`).
The image visibly distinguishes physical source-PDF page 101, running page 93,
and printed page 117. Corollary 2.6 carries marker (3), follows Corollary 2.5
without an intervening proof, and contains both homomorphisms, the inverse
limit, the isomorphism assertion, and the parenthetical base-point convention.
The one-line derivation and the long editorial note are visibly later material
and remain outside this statement-only unit. The page is a same-edition
manifestation/locator witness, not independent original-print corroboration.

## Producer and fresh target render

I inspected both `../RENDER_PAGE_001_150DPI.png` and
`rebuild/INDEPENDENT_REBUILD_RENDER_PAGE_001_150DPI.png` at original detail.
Both are one clean A4 page. The authority box, marker (3), Lef/Leff
hypotheses, connectedness and surjectivity assertions, displayed inverse-limit
map, isomorphism sentence, and base-point note are legible. No clipping,
overlap, missing glyph, broken formula, or displaced page number is visible.

The producer and fresh render are byte-identical at 117,486 bytes and SHA-256
`72975B1C2C209A3140F04FB63B406BF19F96F43201B5C2F31E02B36F293BCA76`.
An independent ImageMagick pixel comparison reports `0 (0)` absolute-error
pixels. Fresh extracted text is byte-identical to the producer text at 1,350
bytes and SHA-256
`984F7A5D41DCF693FE7EBAC0EAD29B52E5FC0D56D54F0A65C5888878442B7522`.
The fresh font table is also byte-identical at 1,235 bytes and SHA-256
`FDBA2D33215659347C6F00F1F00A6C9C849B96281E50C660FD969287373EF37E`:
exactly 11 data rows, all embedded, subsetted, and Unicode-mapped. Producer
and fresh PDF metadata differ only in creation/modification time; normalized
non-time metadata is exact.

## Machine-ledger panels

I inspected all three producer replay panels at original detail:

- `artifact_tool_producer_csv_replay/ARTIFACT_TOOL_MACHINE_QA_A_H.png` —
  163,635 bytes, SHA-256
  `64227DAE770754CD380AAF3B88CA006C65DCD37B25ABBA9459D45F25B22F2806`;
- `artifact_tool_producer_csv_replay/ARTIFACT_TOOL_MACHINE_QA_I_P.png` —
  316,869 bytes, SHA-256
  `DE533030BF18138BC3614837C1A38828FFA0DB70D47C57BB2701CC17C0BA0FD4`;
- `artifact_tool_producer_csv_replay/ARTIFACT_TOOL_MACHINE_QA_Q_V.png` —
  257,380 bytes, SHA-256
  `02FE30CD1C8C9C568969578430583799CBD6585363582DE26AFE1DCE226AE15B`.

Together they visibly cover all 18 producer rows and all 22 columns. The old
12-row font claim remains visible in revision 1; revision 2 visibly carries
11 and the unit, render, and review-defect successor links are present.

I also inspected all three independent-review ledger panels at original
detail:

- `artifact_tool_independent_evidence/INDEPENDENT_EVIDENCE_ARTIFACT_TOOL_A_I.png`
  — 251,034 bytes, SHA-256
  `3537E623A86D00025143D8ED2861D6DB038C6A6840D1B542CD13F9E6D353D097`;
- `artifact_tool_independent_evidence/INDEPENDENT_EVIDENCE_ARTIFACT_TOOL_J_R.png`
  — 364,644 bytes, SHA-256
  `970CF4CB0B4020A36AEE19D52BC320DA91992B1166AA0DC56951AFA4A31AB46F`;
- `artifact_tool_independent_evidence/INDEPENDENT_EVIDENCE_ARTIFACT_TOOL_S_Y.png`
  — 258,859 bytes, SHA-256
  `8CE3CA910901984C599B9EE88450A09AA01A70BE2EE619F8DDE3E4C4E166245C`.

These panels visibly cover all 18 independent-review rows and all 25 columns;
IDs, status, locators, decisions, revisions, evidence paths/hashes, and release
state remain readable. Both Artifact Tool receipts report version 2.8.24,
zero formula-error values, zero formula-trigger values, and PASS.

## Disposition

Direct visual QA supports PASS. The target is unchanged. The only active R2
correction is the evidence count 12 to 11; the predecessor FAIL remains
preserved. Private-path build/engine logs keep this review internal until they
are sanitized or excluded by a later release process.
