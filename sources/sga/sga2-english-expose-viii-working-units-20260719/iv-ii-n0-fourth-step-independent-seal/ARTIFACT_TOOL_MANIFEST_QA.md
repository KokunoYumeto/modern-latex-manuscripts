# Artifact Tool ledger QA

The five substantive CSV ledgers were imported separately with
`@oai/artifact-tool`, inspected through its table interface, and rendered as
primary-ID previews. Final import counts were 4x12, 8x20, 8x21, 8x17, and
4x15 after adding the independent-review rows.

All five inspections returned structured content. The final previews use a
wide first column and show every ID completely, without clipping or hidden
rows. The five PNGs were visually reviewed after the width correction.

The five-record receipt is `ARTIFACT_TOOL_RECEIPT.ndjson`, 892 bytes, SHA-256
`BA700ACD60B3D9E29444C062A1A9FA56A2DF9C3A8F65384315726AD8197064C8`.
This pass checks spreadsheet ingestion and rendered ID visibility; semantic
and reference closure remain separate machine/source-review gates.
