# Artifact Tool ledger QA

All five CSV ledgers were imported through the bundled Artifact Tool, inspected
as tables, scanned for spreadsheet formula errors, styled, and rendered. The
receipt is `ARTIFACT_TOOL_RECEIPT.ndjson`, 3,132 bytes, SHA-256
`F8099439628A1AD2EEA08526DE7CD4EA1A18A3E737C2BAE1DCE8544C050877FB`.
Every receipt reports `artifact_tool_import_inspect_render_pass` and a
zero-match formula-error scan.

The five previews were inspected at original resolution. Headers, complete
stable IDs, evidence classes, authority roles, and unit IDs are visible without
clipping:

- authority preview: 78,817 bytes, SHA-256
  `53F60EC22FB9EA9C431F5D9DD4259649C47A175E8A521033004803DBAB0C9190`;
- alignment preview: 341,368 bytes, SHA-256
  `119E99B193869EFB04C1109FC984F7668C49ED04005E5C098B8FE3A78175B31A`;
- formula preview: 427,074 bytes, SHA-256
  `0AE6F7E33F3BFCF1F01A1C5BD184EA4324FE69BF2D1EA411C3A6849BA54F1303`;
- terminology preview: 333,454 bytes, SHA-256
  `DAE9547D3ED2E46331ECE0CA0196CB7BD9627882165CB83900971C2E485CE80B`;
- source-defect preview: 242,410 bytes, SHA-256
  `CE315B3761AE2F579B7E5A8A1798E2BA9BC215F2DFFB56E14EAE3ED7F8366241`.

This QA verifies machine-ledger readability; it does not independently seal
the translation.
