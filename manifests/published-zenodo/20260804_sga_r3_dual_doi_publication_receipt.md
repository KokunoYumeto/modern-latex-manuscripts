# SGA R3 provenance on methodology and replication DOI lineages

Status: **PASS — the same exact SGA R3 provenance set is public and
anonymously read back on both required existing concepts.**

## Shared provenance set

Both records expose the same seven direct objects:

1. `07_SGA_R3__00_COMPLETE_PROVENANCE_CONTROLS_20260804.zip`
2. `07_SGA_R3__01_PACKAGE_LOGBOOK.md`
3. `07_SGA_R3__02_CROSS_VOLUME_LOGBOOK.md`
4. `07_SGA_R3__03_CONTINUATION.md`
5. `07_SGA_R3__04_SUPERSESSION_AND_ORDER.csv`
6. `07_SGA_R3__05_PREDECESSOR_DECISION_LOG.csv`
7. `07_SGA_R3__06_PREDECESSOR_REVISION_HISTORY.csv`

The deterministic controls ZIP is `11,118,234` bytes, SHA-256
`69E21D1ABB6C39282889E85ED6FF132594DB6A719F5DCEEB7763CCE0F0E50F76`,
with `113` members. Its internal 112-row member manifest has SHA-256
`A1C38CE48670B7A45528C94E7A3E253D5E416793DB31A21B74896F25631F208B`.

## Methodology surface

- Existing concept DOI: `10.5281/zenodo.21124403`
- Predecessor: record `21781388`, DOI `10.5281/zenodo.21781388`
- Successor: record [`21782511`](https://zenodo.org/records/21782511), DOI
  [`10.5281/zenodo.21782511`](https://doi.org/10.5281/zenodo.21782511)
- Public surface: `100` files / `5,004,414,281` bytes
- New SGA objects: `7/7` anonymous raw readback exact
- Provenance ZIP: `113/113` members exact
- Unrelated retained predecessor objects: `93/93` exact
- Default preview retained:
  `00_Interlanguage_Methodology_Current_v13_20260718.pdf`
- Active draft after publication: `false`

## Replication surface

- Existing concept DOI: `10.5281/zenodo.20461174`
- Predecessor: record `21781392`, DOI `10.5281/zenodo.21781392`
- Successor: record [`21782515`](https://zenodo.org/records/21782515), DOI
  [`10.5281/zenodo.21782515`](https://doi.org/10.5281/zenodo.21782515)
- Public surface: `77` files / `22,843,758` bytes
- New SGA objects: `7/7` anonymous raw readback exact
- Provenance ZIP: `113/113` members exact
- Unrelated retained predecessor objects: `70/70` exact
- Default preview retained:
  `00_AI_Run_Modern_LaTeX_Manuscript_Workflow_Current_20260728.pdf`
- Active draft after publication: `false`

To remain within the methodology record's 100-file ceiling, six machine-only
direct duplicates were compacted from the new broad heads only after exact
proof that the same bytes remain uniquely recoverable inside retained GAGA or
FAC provenance ZIPs. Human-readable logbooks, decision rationale, reversal and
error history, and continuation surfaces remain direct. Immutable predecessor
versions retain every former direct object. No distinct content was curated
away, and no duplicate concept was created.

The complete machine-readable proof is
`20260804_sga_r3_dual_doi_publication_receipt.json`, with record-specific
proofs in the adjacent methodology and replication JSON receipts.
