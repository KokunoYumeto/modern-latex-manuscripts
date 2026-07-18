# SGA 6 English sync handoff at idx646

Date: 2026-07-18.

Current sealed English checkpoint:

`C:\Users\Floris\Documents\interlanguage\03_projects\language_management\english_germanic\03_working_translations\sga6_cumulative_sync_idx532_646_en_20260718`

- Main TeX: `SGA6_idx532_646_English_SourceChecked.tex`
  - SHA-256 `69A5252F51384964178A92384F66D39924B55265C64E65650C032EBD738292E7`
- PDF: `SGA6_idx532_646_English_SourceChecked.pdf`
  - 71 A4 pages, 732,848 bytes
  - SHA-256 `317D34C7EA3FDC6C080D811701BAE065E65525DC06C80200A9D226C9C617A173`
- `SHA256SUMS.csv`: 232 verified entries, excluding itself and transient
  `.aux`/`.out` files
  - manifest self SHA-256
    `ECB5EA383864A00CE13C688818F7CEF5624B2E961E6CA737F7D2B90C9AADCE3E`

Build: two successful pdfLaTeX passes; stabilized log has zero errors,
warnings, undefined references, overfull boxes, or underfull boxes. All 71
pages were rendered at 150 dpi and visually checked. Formula/source,
correction, inherited-English, terminology, page-coordinate, and source-
witness ledgers are current through idx646.

French control used for this package: predecessor SHA-256
`DCCF1BE9533FAC29E6F12989537F017EFC41340A2D2B2F0B89CB8FE9A4A236FB`,
source-checked through idx646. Live successor discovered before sealing:
commit `8ccdcf8ee`, SHA-256
`77703F2D7E8FF9000C2C1E7320A903A48ADE00BF62C8F5F240FF88C42ED82703`,
direct source-rescribe through idx662. Git comparison shows that this
successor leaves the idx532--646 control prefix unchanged.

Exact continuation: idx647 / printed 634 / source-PDF 637, continuing the
predicate of Definition XIII.3.3. Use the live French successor for
idx647--662. Treat idx663 onward as explicit scan-checked draft beyond the
current French checkpoint.

Claude notes through idx646 are stored beside the French workpass; the French
file was not edited by the English task. `PENDING_CLAUDE_SOURCE_FIXES.md`
mirrors unresolved decisions inside the package.

Publication: `DO_NOT_UPLOAD`. Existing concept DOI
`10.5281/zenodo.20410947`; current public SGA version found in the repository
`10.5281/zenodo.21420146`; idx662 predecessor
`10.5281/zenodo.21419947`. Do not mint a duplicate record.
