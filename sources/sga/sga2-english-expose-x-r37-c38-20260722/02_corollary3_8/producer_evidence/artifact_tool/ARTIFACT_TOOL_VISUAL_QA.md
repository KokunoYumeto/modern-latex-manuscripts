# Artifact Tool visual QA — Corollary 3.8 producer evidence

## Result

**PASS at the producer gate.** I inspected all six Artifact Tool panels at
original detail. Together they expose the complete `A1:Z44` range: 26 columns,
one header row, and all 43 stable-ID evidence rows.

- `A1:D44`: 297,515 B; SHA-256
  `C5C4822750CF8CAFC066FB362BEF492EB6F9B5367CB8D6177BC2A68FCF91F866`.
- `E1:H44`: 96,817 B; SHA-256
  `6409BB2A053D7F019075E1A53B3E98F8F4F72BBA4979E1C043180DDC2B8841C4`.
- `I1:L44`: 319,242 B; SHA-256
  `992000FE87B7628B0CB988B210D20DFA04D3DCF4FEBB91754CDBA528B9FF7B36`.
- `M1:P44`: 735,834 B; SHA-256
  `455AE83888AA6CAA0A73C559611D1FD5C34F7903AB3107C3D4F611CD0CF36DBB`.
- `Q1:T44`: 410,537 B; SHA-256
  `762BE441A71838ADF1B9CF0E64AA7CDDC3085CFAC7EC7594A0BE058102510BF7`.
- `U1:Z44`: 685,399 B; SHA-256
  `923A5A38D9F99484915538B5781B5181917029424DEB9CEF3B945350D8A8488F`.

The panels keep the stable IDs, types, hierarchy, revisions, distinct source
locators, authority roles and hashes, source and target readings, decisions,
statuses, evidence identities, cursors, release states, and revisit conditions
legible. Wrapped cells stay within their boundaries. I found no missing row or
column, clipping, overlap, black box, formula error, or hidden out-of-range
content.

The Artifact Tool 2.8.24 receipt reports unique nonempty primary IDs, zero
formula-error values, zero spreadsheet-formula triggers, and status `pass`.
This is producer QA only; an independent review remains required.

