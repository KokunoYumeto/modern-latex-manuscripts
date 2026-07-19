# Artifact Tool ledger QA

After the independent seal rows were appended, all five substantive CSV
evidence ledgers were re-imported in full through bundled Artifact Tool 2.8.24,
inspected as tables, scanned for formula records, styled, and rendered. The
receipt is `ARTIFACT_TOOL_RECEIPT.ndjson`, 3,447 bytes, SHA-256
`404232F77C9F9E1DE12073C8299EF2F60D8051F24C0844E6965A483B9BD3BE87`.
All five records report the post-seal import/inspect/render pass, no formula
records, and literal formula safety `true`.

The five post-seal previews were inspected at original resolution. Headers,
stable IDs, authority roles, source/target locators, record revisions,
continuation cursor, closed Option-A policy, and independent-seal rows are
visible without clipping:

- authority: 137,877 bytes, SHA-256
  `EFDBBFF190CADACB4D182BE02704DA5828638B4CE1EFBC255381419A1BCE11C5`;
- alignment: 140,911 bytes, SHA-256
  `8BFAC59C7BA4278CD984D54351CA6C2E6BA66952765A02DC62E8FCDD7308192F`;
- formula/structure: 217,784 bytes, SHA-256
  `DD780080EDA08FA68C5335994F13770AF73D255FAFCBFE156E48A1904E731000`;
- terminology/adverse choices: 168,251 bytes, SHA-256
  `6CF7466E77D197B75F91D6ABA72C5931C5798FDEC50574101B32EF4735CBEAAE`;
- source defects/emendations: 122,925 bytes, SHA-256
  `202E77B6350968ABE728DC55CA285465AFB2226D1A5143963AD3A178ED68A483`.

Ledger counts are 12 authority rows, 9 alignment rows, 14 formula/structure
rows, 13 terminology rows, and 10 source-defect rows: 58 substantive CSV
rows. Rectangularity, unique primary IDs, UTF-8 parsing, and formula safety
also pass under the independent strict parser. `UNIT_HASHES.csv` and
`ZENODO_PAYLOAD_MANIFEST.csv` receive their own later Artifact Tool receipts,
previews, and exact-reference validation because they are freeze manifests.
