# Independent visual QA — SGA2 Exposé X, Corollary 2.4 statement R3

Status: **PASS**. This is internal review evidence. It is not a publication,
archive handoff, or whole-exposé seal.

## Source page and locator systems

I inspected `../SOURCE_PHYSICAL_PAGE_101_200DPI.png` at original detail
(407,075 bytes; SHA-256
`E59A5DADE48D40EA47B11A4747A72A21ABA090FA09F697F403FC5B4ACD0FB793`).
The page visibly identifies recomposed running page 93. Corollary 2.4 lies on
original printed page 116; the printed-page 117 marker occurs later, inside
the proof. Physical source-PDF page 101, printed page 116, and running page 93
are therefore kept distinct. The image is a same-edition manifestation and
locator witness, not independent original-print corroboration.

The complete statement visibly contains the `Lef(X,Y)` hypothesis, a finite
flat covering `R` of an open neighborhood `U`, the fiber product with
completed `X`, and the three connectivity conditions. The proof begins at the
next substantive cursor, authority line 3433, and remains outside this unit.

## Producer and fresh target pages

I inspected both `../RENDER_PAGE_001_150DPI.png` and
`rebuild/INDEPENDENT_REBUILD_RENDER_PAGE_001_150DPI.png` at original detail.
Both are clean single A4 pages. The authority box, Corollary 2.4 heading,
finite-flat-cover condition, fiber product, hats, subscripts, equivalence
language, and final ordinary `X` are legible. No clipping, overlap, missing
glyph, broken formula, or displaced line is visible.

The producer and fresh renders are byte-identical at 97,293 bytes and
SHA-256
`49C9867865134729AD59C93E463F2A8F3250576F69C58986F516400EC0FDD65A`.
The independent pixel comparison reports `0 (0)` absolute-error pixels.
Extracted text is byte-identical at 956 bytes and SHA-256
`7597F1AAC5798080690680FF16975B70EAB3E40F1ADFBF6468A250320DA1B0A9`.
The font table is byte-identical at 1,235 bytes and SHA-256
`74C646E9A719B20AB02430DD81E756F96BD2862BAA8FA2EBA519283EA4CF42FC`:
all 11 rows are embedded, subsetted, and Unicode-mapped. Producer and fresh
PDF metadata differ only in creation/modification timestamps; normalized
non-time metadata is exact.

## Producer machine-ledger panels

I inspected all three independent replays of the producer CSV at original
detail:

- `artifact_tool_producer_csv_replay/ARTIFACT_TOOL_MACHINE_QA_A_H.png` —
  201,943 bytes, SHA-256
  `051065AFFF6C1FA14133A08ADA07119CE2C1CEBC36449749E3AD0F9A47242480`;
- `artifact_tool_producer_csv_replay/ARTIFACT_TOOL_MACHINE_QA_I_P.png` —
  376,142 bytes, SHA-256
  `BF149B7C4A5420A0B8FBF418219D0D5D0EACC918D0DD9288C87DCA23BDEEAEE9`;
- `artifact_tool_producer_csv_replay/ARTIFACT_TOOL_MACHINE_QA_Q_V.png` —
  278,594 bytes, SHA-256
  `DA192E10CDB231FD879D1F923307B332FFC542AD4AD79BD53B61029B52A1C489`.

Together they visibly cover all 21 producer records and all 22 columns. The
unit revisions 1–3, comparison correction, stable adverse ID, preserved R2
independent FAIL, manifest-order blocker and resolution, 76-row predecessor
history, 13-row unchanged-artifact binding, locators, hashes, cursors, and
internal release state are readable.

## Independent-review ledger panels

I inspected all three panels for the 17-record independent ledger at original
detail:

- `artifact_tool_independent_evidence/INDEPENDENT_EVIDENCE_ARTIFACT_TOOL_A_I.png`
  — 233,315 bytes, SHA-256
  `800E21C14FB5F014DC1DC0242E9F4A3D3F8950F158C99630F14E2500AB63A3B8`;
- `artifact_tool_independent_evidence/INDEPENDENT_EVIDENCE_ARTIFACT_TOOL_J_R.png`
  — 354,270 bytes, SHA-256
  `57C10FE5A9B59E31DA7B763A409956747B69D5F1C71E87519AC448B314AB778F`;
- `artifact_tool_independent_evidence/INDEPENDENT_EVIDENCE_ARTIFACT_TOOL_S_Y.png`
  — 222,571 bytes, SHA-256
  `DCCC71CB07A2387BA77BC10D3599A0EAA44A9E1AEE74022D121F9511DBFDBC59`.

These panels cover all 17 rows and 25 columns. Stable IDs, source/target
locators, statuses, decisions, revision links, evidence paths and hashes,
cursors, and release state remain readable. Artifact Tool 2.8.24 reports zero
formula-error values, zero formula-trigger values, and PASS for both the
producer replay and the independent ledger.

## Disposition

Direct visual QA supports PASS. The R3 successor changes only root-manifest
ordering evidence; target TeX/PDF and source/comparison controls are unchanged.
The predecessor evidence-only FAIL remains immutable. Private-path build and
engine logs keep the package internal until they are sanitized or excluded by
a later release process.
