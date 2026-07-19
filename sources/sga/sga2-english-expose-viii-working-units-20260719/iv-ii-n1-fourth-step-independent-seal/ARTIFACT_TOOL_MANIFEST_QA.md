# Artifact Tool ledger QA

The five substantive CSV ledgers were imported separately with
@oai/artifact-tool, inspected through its table interface, and rendered as
primary-ID previews. Final post-review import counts are 4x12, 15x20,
17x21, 14x17, and 8x15.

All five inspections returned structured content. The previews use a wide
first column and show every ID completely, without clipping or hidden rows.
All five PNGs were visually reviewed at original resolution.

The five-record receipt is ARTIFACT_TOOL_RECEIPT.ndjson, 895 bytes, SHA-256
372EFCF1FB5B54B7C015E6C833E444C7DA5F17B8A67DB40E7EC24357FD2EDBD3.
This pass checks spreadsheet ingestion and rendered ID visibility; semantic
and reference closure remain separate machine/source-review gates.
