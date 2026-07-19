# Artifact Tool ledger QA

All five CSV evidence ledgers were imported through the bundled Artifact Tool,
inspected as tables, scanned for spreadsheet formula errors, styled, and
rendered after the manager-closed Option-A revisions. The receipt is
`ARTIFACT_TOOL_RECEIPT.ndjson`, 2,792 bytes,
SHA-256
`FD59107FC323ED0CDD7333DB835838422350EEFC934D02353644556C03AB84E8`.
Every receipt reports `artifact_tool_import_inspect_render_pass` and a
zero-match formula-error scan.

The five previews were inspected at original resolution. Headers, complete
stable IDs, evidence classes, authority roles, and unit IDs are visible without
clipping:

- authority: 57,712 bytes, SHA-256
  `50CA08A5CF3A88DF27C05B3749875367FC26DB290D1CDDE1B120FEC02D19F400`;
- alignment: 97,954 bytes, SHA-256
  `ABB3126F977FB9EFC8FAF72C2B0B86DB705D6A8E55B95D7DA9292D749581776B`;
- formula/structure: 169,444 bytes, SHA-256
  `1676372014124BEACB3B7CB71D542D96F11B102B3FDA5AA08BAC7F9DB17DC682`;
- terminology/adverse choices: 128,229 bytes, SHA-256
  `C6B384156F7F481A240B11118DA1F734457FD47F601BA636B6267409735571A0`;
- source defects/emendations: 104,417 bytes, SHA-256
  `01BFD29FA5BDBAD8C1F3D2626CBA8878DB829C10B201042D277E8AF493B2C9AA`.

Ledger counts are 8 authority rows, 12 alignment rows, 21 formula/structure
rows, 17 terminology rows, and 13 source-defect rows: 71 substantive CSV rows.
Artifact Tool QA verifies ledger readability; it does not independently seal
the translation.
