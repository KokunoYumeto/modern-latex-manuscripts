# Independent visual QA - SGA2 Exposé X, Corollary 2.5 statement

## Outcome

PASS at original image detail. The source and target renders are legible and
complete, and all producer and independent machine-ledger panels are readable.

## Source render

`../SOURCE_PHYSICAL_PAGE_101_200DPI.png` is 407,075 bytes, SHA-256
`E59A5DADE48D40EA47B11A4747A72A21ABA090FA09F697F403FC5B4ACD0FB793`.
It visibly establishes physical page 101, recomposed running page 93, the
embedded original printed-page marker 117, the complete Corollary 2.5, and the
opening of Corollary 2.6. The image confirms bold `Et`, arrow direction, both
hypotheses, the prime, fiber product over `U`, and the isomorphism. It is a
same-edition manifestation and locator control only, not independent
original-print corroboration.

## Fresh target render

`rebuild/REVIEW_RENDER_150DPI.png` is 107,275 bytes, SHA-256
`345A0FB54EF9FF36FA17849308C2A18DBED6198FA62FABE549287C6748C39F98`.
It is byte-identical to the producer render. Original-detail inspection finds
no clipping, overlap, missing line, broken accent, black box, malformed prime,
or formula displacement. The authority box, Corollary 2.5 label, bold `Et`,
arrow, `Lef`, `Leff`, `R'`, `R' times_U Y`, and isomorphism are all clear.

## Producer machine-ledger panels

Artifact Tool 2.8.24 independently replayed the producer CSV as 8 rows by 22
columns. These three panels are byte-identical to the producer panels and pass
original-detail inspection:

- `artifact_tool_csv_replay/ARTIFACT_TOOL_MACHINE_QA_A_H.png`, 63,975 bytes,
  SHA-256 `D81FBA6F293319A905788FD30C5EEA8C4F6AFCE8B02E58E03A36FA5AF7AA094B`;
- `artifact_tool_csv_replay/ARTIFACT_TOOL_MACHINE_QA_I_P.png`, 142,180 bytes,
  SHA-256 `B2DBE767A8A65C5FF07F808C8EBF7CF5A8B4913540E76AF2B6B5E21EA8D3B14A`;
- `artifact_tool_csv_replay/ARTIFACT_TOOL_MACHINE_QA_Q_V.png`, 121,479 bytes,
  SHA-256 `58109589AADF5DA5C19B5A0E63812AB51C604B70385C2B05D80A6D24E316EEC3`.

## Independent machine-ledger panels

Artifact Tool 2.8.24 imported the append-only independent CSV as 13 rows by 25
columns. All columns are covered across these three inspected panels:

- `artifact_tool_independent_evidence/INDEPENDENT_EVIDENCE_QA_A_I.png`,
  175,910 bytes, SHA-256
  `2583ECCC29D4B070AA0E6561CF5BA9C55500180DB5CC5230F3418AE7C4F1010E`;
- `artifact_tool_independent_evidence/INDEPENDENT_EVIDENCE_QA_J_R.png`,
  275,933 bytes, SHA-256
  `0179C1586211D154981F850E7426595FFA75E1370DBC9A39A72355273530E2F6`;
- `artifact_tool_independent_evidence/INDEPENDENT_EVIDENCE_QA_S_Y.png`,
  148,857 bytes, SHA-256
  `500C059FFD7488E3BCDE552B89D8D16D6B141EE695C747E276C1F83CA7555995`.

No visual defect remains. This QA does not change the internal-only release
state or sanitize path-bearing build logs.
