# Source, formula, and build review

## Authority receipts

- Current R823 cumulative German TeX: 2,125,031 bytes; SHA-256 `EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21`.
- Exact R823 line slice 3839-3951, CRLF joined with terminal CRLF: 8,107 bytes; SHA-256 `EAE24CB938D254B7725C418CC25442ACF19ECF83D29AD82131AFD549EB9E1E1E`.
- Original 38-page Paper 4 scan: 72,444,867 bytes; SHA-256 `D7F7CE6D4B311FFD968ED47DC9C1478CFFCF9F446A86BF90263E0C9D1B41C9EF`.
- Inherited English comparison body: 109,132 bytes; SHA-256 `200C9F9115C22D93455A3B7AA372687059E539C6D01959D30EEB25BBEEFFE722`.

The source and comparison bodies are not redistributed here.

## Complete bounded comparison

The complete German span was checked line by line against the English target. Fresh 300-dpi renders of physical scan pages 15-17 were inspected at original resolution. They cover the visible section 4 heading, every prose block, relations (22)-(31), the four-case array, the two polar-process pairings, and the visible section 5 boundary.

- Numbered relations: 10/10 present and checked.
- Additional displayed groups: four-case array 1/1 and polar-process pairing 1/1.
- Source notes in section 4: 0/0. The target adds one clearly identified editorial note at relation (28).
- Formula controls include all signs, nested subscripts, index ranges, combined summation bounds, dotted variables, and the `i_0=0` convention.

Adjudications:

- Relation (23): printed and R823 `q_(rho-1)^(1)` retained; inherited-target `q_rho^(1)` rejected.
- Relation (28): original-print `q_(rho-(tau-sigma))` and `p_(tau-(tau-sigma))` restored over collapsed R823 readings and disclosed in the body.
- Four-case array: original print has `tau >= sigma` in case 3; R823 and target use `tau > sigma`, a coherent editorial normalization creating a disjoint partition, not a source defect.
- Relations (30) and (31): historical paired lower/upper summation limits retained together with their explanatory sentence; silent max/min modernization rejected.

No additional scan-backed source defect was found in the bounded section.

## Independent build review

The exact packaged TeX was compiled in an isolated directory for three consecutive halt-on-error pdfLaTeX passes. All exits were zero. The final log had zero LaTeX or package warnings, box warnings, undefined controls or references, fatal errors, emergency stops, or rerun requests. Raw path-bearing logs and auxiliary files are excluded.

The resulting PDF parses as two A4 pages, carries title/author/subject metadata, contains no JavaScript or forms, and reports 22/22 embedded, subsetted fonts with Unicode mappings. Extracted text is 12,056 bytes with SHA-256 `D33515B0C82B8AA2E7545B4B6AD8230F3C652C1CC77F680AB5886EDA3F6B69CE`; it contains every relation label (22)-(31) and the relation (28) disclosure.
