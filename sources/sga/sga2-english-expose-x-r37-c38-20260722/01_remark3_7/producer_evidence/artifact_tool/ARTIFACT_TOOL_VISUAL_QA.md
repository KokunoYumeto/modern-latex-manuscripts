# Artifact Tool visual QA — producer machine evidence

## Result

**PASS at the producer gate.** I inspected all three Artifact Tool panels at
original detail. Together they expose the complete `A1:V39` range: 22 columns,
one header row, and all 38 stable-ID evidence rows.

- Panel 1, `A1:H39`: 250,925 B; SHA-256
  `8FC4DDF804AFA9D7BE83C8B63ACFC6C661904C086ADDE2C1143E582BCB29D169`.
- Panel 2, `I1:P39`: 485,698 B; SHA-256
  `9CD75240FC978D8BAD5F9B33C99BBDB2A21265BEDD63F276BD9DDAA18ACD8CB2`.
- Panel 3, `Q1:V39`: 436,594 B; SHA-256
  `433D5940B80559EEF11EBA8C8B6719857E4C63AB9AE940E373D46B65AFD449EC`.

The headers, record types, parent IDs, revision fields, source lines and
locators, source/target readings, statuses, cursors, target identities,
evidence hashes, and release states remain legible. Wrapped text stays within
the intended cells. No missing row or column, clipping, overlap, black box,
formula error, or hidden out-of-range content is visible.

The Artifact Tool 2.8.24 receipt reports unique nonempty IDs, zero formula-error
values, zero spreadsheet-formula triggers, and status `pass`. This remains
producer evidence pending a genuinely independent review.
