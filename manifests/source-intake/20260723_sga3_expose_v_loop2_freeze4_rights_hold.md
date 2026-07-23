# SGA3 Expose V Loop2 r4 freeze4 rights hold

Date: 2026-07-23

## Intake identity

Exact producer root label:

`public_projection_sga3_exposeV_loop2_native_r4_freeze4`

The private absolute transport path is deliberately omitted from this public
receipt; the producer handoff and local audit retain it.

- Tree: 298 files / 27,920,910 bytes
- `ZENODO_PAYLOAD_MANIFEST.csv`: 296 rows / 93,001 bytes, SHA-256
  `D3E936A9AD1EAF3ECC1AD46445135030863D0B97FB9FC880868A1DDFF876199E`
- `PUBLIC_PROJECTION_VALIDATION.json`: 5,403 bytes, SHA-256
  `1111BE20138BD80F9837941E05A29432C02AA487B8E6C9E93FCB78AEA5E76C75`
- Reader PDF: 361,493 bytes / 51 A4 pages, SHA-256
  `E4682CBED71922AF8C1C2851D8B69F2CF6A1E089CC4CC52EDF0318708F65F6F2`
- Editable master: 7,202 bytes, SHA-256
  `92AB24AB2E104618AB4E97AC4A2F23554BECB741258F7E9739EC463E6B99C37E`

## Independent technical result

Technical validation passed:

- 298/298 files and 296/296 manifest rows exact;
- 14 CSV files / 19,083 data rows, with zero rectangularity or formula
  errors;
- seven JSON files and four JSONL files / 4,623 records parse-clean;
- zero private-path hits;
- isolated three-pass XeLaTeX rebuild passed;
- direct and rebuilt PDFs rendered byte-identically on all 51 pages at
  120 dpi;
- pages 1, 24, 49, and 51 passed direct visual review; and
- freeze3 to freeze4 is exactly 294 byte-identical files plus four changed
  controls: `STATUS.md`, `PUBLIC_PROJECTION_VALIDATION.json`,
  `ZENODO_PAYLOAD_MANIFEST.csv`, and
  `controls/loop2/LOOP2_REVISION_EVENTS_R4.jsonl`.

The two supplied independent reports also replayed exactly:

- tree/privacy/machine report SHA-256
  `BC110B84C8011C6DDBFDE26BFD354C28AC4F4B37904A80FD27018851ADCBCE8A`
  and validation SHA-256
  `56A4447E9D761A21DCA2BAC728F6D40C47C46EB9906DC69AF887D7C690C54CFE`;
- PDF/reference/render report SHA-256
  `81B9F5724E770009C42D51E78FF2588998DB183DAA246ADABF04AA0AF2422225`
  and validation SHA-256
  `0652D85C963832DE2FF62FA88EAD44A2C3B388DBF41A212916834929AD9B0F8D`.

The machine-readable audit is
`20260723_sga3_expose_v_loop2_freeze4_independent_audit.json`, 2,819
committed bytes, SHA-256
`A6CF8203A6EB07DA2DF1CD1068B81F8E67ECA5E4EF07056C390222B1F083AB19`.

## Blocking rights result

Freeze4 contains 66 cropped PNG witnesses derived from the controlling
Polo-Gille PDF. Together they occupy 344,264 bytes and have ordered aggregate
SHA-256
`C30EF1C441844235F7F8C58C261259C2A67992990FE1025B14E7AE19571A262D`.
They are source pixels, not project-generated native diagrams.

No affirmative redistribution grant for those source-derived pixels was found
in the package. Package text instead states that the witnesses inherit the
underlying French-rights caveat. Technical PASS therefore does not establish
public redistribution authority.

Disposition:

`BLOCK_SOURCE_PIXELS_PENDING_AFFIRMATIVE_REDISTRIBUTION_RIGHTS`

## Archive action

- Freeze4 is accepted as exact local custody evidence.
- No freeze4 GitHub publication was made.
- No Zenodo draft, version, or duplicate concept was created.
- No current public file was superseded by freeze4.
- The already-published rights-curated successor remains current at
  <https://doi.org/10.5281/zenodo.21511144>, with the same reader PDF and
  master TeX, native diagram sources, zero public source-witness pixels, and
  66-row public metadata ledgers for the withheld witnesses.

Revisit freeze4 only after an affirmative redistribution-rights decision or a
separately frozen rights-curated successor. Its technical exactness and its
rights hold must remain separate claims.
