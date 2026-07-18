# SGA 6 English tail ledger merge report

## Outcome

The continuous English tail is normalized from current-rescribe idx532 through idx702, followed by exactly ten explicitly unindexed back-matter pages. No French file and no cumulative/final TeX workspace was edited.

The certification boundary is explicit:

- idx532--662: source-checked English against a French checkpoint certified for the corresponding scope;
- idx663--702: source-checked English draft after the French certified frontier, pending Claude;
- source-PDF 693--702: scan-checked unindexed back matter, pending Claude and never assigned invented current-rescribe indices.

## Inputs and normalized row counts

| Ledger family | Sealed idx532--646 | Agent idx647--665 | Agent idx666--684 | Agent idx685--702/back matter | Normalized rows | Exact duplicates removed |
|---|---:|---:|---:|---:|---:|---:|
| Page/index map | 115 | 19 | 19 | 28 | 181 | 0 |
| Formula/symbol comparison | 197 | 19 | 61 | 47 | 324 | 0 |
| Terminology/rejected choices | 130 | 23 | 32 | 28 | 213 | 0 |
| Claude/source-fix notes | 1 complete note | 1 complete note | 1 complete note | 1 complete note | 4 preserved note blocks / 218 lines | 0 |

Deduplication keys excluded only the provenance field. If an exact normalized duplicate had occurred, it would have been retained once with combined source-ledger provenance. No such duplicate occurred. Similar-looking entries with different indices, witnesses, or editorial dispositions were preserved separately.

## Output files

| File | Data rows or lines | Bytes | SHA-256 |
|---|---:|---:|---|
| `PAGE_INDEX_LEDGER.csv` | 181 data rows | 73,928 | `214F7682A456193D9E64872FBB3594561CB76CF3321E81D409BA8CA70796B0C4` |
| `SOURCE_FORMULA_SYMBOL_COMPARISON.csv` | 324 data rows | 114,442 | `1D11A7B92BFD1B3E5A9FAD9B67FE78717F7B90876CEF74C49C7CB17DEA3EFCDC` |
| `TERMINOLOGY_AND_REJECTED_CHOICES.csv` | 213 data rows | 81,718 | `210DF4FE7E7E76247457DBB1F7F554156171EDBB866D68BBDDA90D0131A4BC9A` |
| `PENDING_CLAUDE_SOURCE_FIXES.md` | 218 lines | 21,581 | `0742B6684822AF4E92F18F7AB71EB5892795CA5EA0A79F2A832F27790076F428` |
| `AUTHORITY_LAYER_LEDGER.csv` | 18 data rows | 7,901 | `746135071EBF05793F18C53935B2BBC2AE10E2095F68088478A520F0DD6EBFF7` |

The final hash of this report is intentionally supplied in the parent handoff rather than embedded here, because embedding a file's own hash changes the file.

## Coordinate validation

Validation result: **PASS**.

- Indexed row count: 171, exactly idx532--702 inclusive.
- Current-rescribe sequence: continuous, strictly one row per index, no duplicates or gaps.
- Printed-page relation: `printed = idx - 13` on every indexed row.
- High-resolution relation: `highres = idx + 1` on every indexed row.
- Declared source-PDF mapping:
  - idx532--592: `sourcePDF = idx - 6`;
  - idx593: absent from the declared scan;
  - idx594: `sourcePDF = idx - 7`;
  - idx595--597: absent from the declared scan;
  - idx598--702: `sourcePDF = idx - 10`.
- Unindexed row count: 10, exactly source-PDF 693--702 / printed 691--700 / high-resolution 705--714.
- Printed page 690 remains explicitly absent from the declared 702-page scan.
- Exactly one row is marked as the physical terminal: source-PDF 702 / printed 700 / high-resolution 714, ending at `Z(x)`.
- idx702 is marked as the Exposé XIV terminal but not as the volume terminal.

All 324 formula/symbol rows were re-imported after export. Every indexed formula row with page coordinates reconciles to the normalized page ledger; every unindexed formula row maps within source-PDF 693--702. Coordinate errors: 0.

Terminology scopes retain their original location text while also separating current-rescribe, printed, source-PDF, and high-resolution coordinate scopes. Declared-scan omissions are encoded as `ABSENT_FOR_IDX`, not assigned false page numbers.

## Certification validation

Validation result: **PASS**.

Page ledger:

- 131 indexed rows at or before idx662 are in a certified French-control layer;
- 40 indexed rows idx663--702 are labelled draft after the certified checkpoint;
- 10 unindexed back-matter rows are scan-checked and pending Claude.

Formula/symbol ledger:

- 213 records belong to certified-French-control indices;
- 99 records belong to post-idx662 draft indices;
- 12 records concern unindexed back matter.

The French workpass remains at SHA-256 `77703F2D7E8FF9000C2C1E7320A903A48ADE00BF62C8F5F240FF88C42ED82703`; its last modifying commit is `8ccdcf8eeef35cba9cc7ca09fe79e6b3f863becc`. It was read only.

## Authority model

The authority ledger separates:

1. the 702-page scan as ultimate source;
2. the 720-page high-resolution scan as corroboration/supplement;
3. the historical French checkpoint through idx646;
4. the current French successor through idx662;
5. promoted/source-checked English and post-checkpoint draft tranches;
6. inherited English comparison witnesses that are never authority;
7. SGA1--4 English style witnesses that never override the SGA6 scan.

It also records exact hashes for the tail TeX artifacts, including the physically terminal back-matter fragment.

## Merge method and reproducibility note

All source CSVs were parsed structurally, normalized to explicit schemas, exported as UTF-8 CSV, re-imported, and validated with independent assertions for counts, uniqueness, coordinate equations, certification status, and terminal state. The workbook dependency loader did not return during two bounded, memory-safe attempts after the reported PC memory incident; because the requested deliverables are plain CSV/Markdown rather than an XLSX workbook, the merge used PowerShell's CSV parser/exporter and a second parse-validation pass. No visual workbook artifact was required or created.

