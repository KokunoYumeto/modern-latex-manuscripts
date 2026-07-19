# Source and input mapping

## Live base

The combined TeX was advanced from the sealed P05 p316 source-repair head:

`Noether_LocalCodex_20260719_P05p316_Sperrdruck_SourceFix_COMPLETE`

The exact base-to-current diff is `03_audit/diff_P05head_to_P02p028_034_WebP04p118_143.diff`.

## Paper 2 authority

- Worked source slice: `02_source/P02_p028_034/P02_source_boundary_p027_058.pdf`
- Page map: `02_source/P02_p028_034/P02_SOURCE_PAGE_MAP_p027_058.csv`
- Full-page witnesses: `02_source/P02_p028_034/full_650dpi/`
- Enlarged three-strip witnesses: `02_source/P02_p028_034/strips_1000dpi/`

The filenames describe render settings; the scan itself is the authority. Every page and every strip in pp. 28-34 was opened at original detail. OCR was not used as adjudicating evidence.

## Paper 4 authority

- Complete original article scan: `02_source/P04_original/paper_04_crelle139_pp118_154_ORIGINAL.pdf`
- SHA-256: `D7F7CE6D4B311FFD968ED47DC9C1478CFFCF9F446A86BF90263E0C9D1B41C9EF`
- Web evidence package: `07_provenance/input_packages/Web_P04_p118_143_CurrentHeadAudit_20260719_CORE.zip`
- Web core ZIP SHA-256: `8ACB934E9E793AC16542765FE9C6806FF90B4DF0CD84EE86E73E43D57DB8A7DC`

Web's validation cumulative had a different base hash from the live head and is preserved only as evidence. The localized bounded diff and page ledgers were adjudicated against the live cumulative by content.

## Authority policy

1. Original print outranks OCR, inherited TeX, filenames, revision numbers, and self-report.
2. An authenticated editorial ruling may intentionally preserve a disclosed print/editorial delta; it must remain in the apparatus.
3. Merge source-backed hunks by content, never by nominal revision order.
4. Compilation proves TeX validity, not source fidelity. Changed-page render comparison is mandatory.
5. A page closes only with page-addressable source, audit-depth, current-head, evidence, and disposition records.

