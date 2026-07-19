# Scope and merge receipt

## Inputs

- Repository German cumulative base:
  `sources/noether/paper04-sections06-07-source-repair-20260719/current/german/Noether_German_Cumulative_P02_P04S07_current.tex`
  - 2,152,414 bytes
  - SHA-256 `8851AF561D7C40B2295DB5D4108684A06015756B9B6FDD7CCE67466E0F7F8134`
- New producer archive:
  `Web_P04_p144_154_CurrentHeadReaudit_20260719_COMPLETE.zip`
  - 191,444,582 bytes
  - SHA-256 `49D05E0F92B63619F1209AFA1B6A621198FA73D1A45B471CE63A006E4C3557E1`
- Producer input cumulative TeX:
  - SHA-256 `6AC8F355BF3BABD9610F52240D48BDE359284DB7D775E47C489ECADAC8B940D5`
- Audited replacement extract:
  - 28,528 bytes
  - SHA-256 `76CB3DEFE55B1CA23E2C4E1D38F2F86D250536943188718E2647A2C028CF190F`
- Producer localized diff:
  - 36,652 bytes
  - SHA-256 `4898140A8CEC632FC1F70ABD52697D8660B8257ECD5D097AA558C953F054A888`

The producer input and repository base were not identical outside the assigned
band. A whole-file replacement would therefore have overwritten unrelated live
work. The merge replaced only repository lines 4200-4507, matched by bounded
content anchors, with the audited replacement extract. The resulting file has
24,102 lines.

## Result

- Hybrid current-head TeX:
  - 2,152,748 bytes
  - SHA-256 `2B4E001C3FDDD6C4A35B02DA306F26BBF7B994E93C6332A375F59FBF376186B0`
- Hybrid current-head PDF:
  - 2,650,466 bytes
  - 466 A4 pages
  - SHA-256 `BA03AA9AF88A73D5768DB753E645465E9A4313B134AA558B7C4DCA16813AE9D3`

Two XeLaTeX passes exited zero. The only diagnostic was the inherited benign
`inputenc` warning under XeLaTeX. At 150 dpi, hybrid output pages 58-68 are
byte-identical, 11/11, to the corresponding pages from the producer's audited
final cumulative PDF. Pages 59-66 carry the bounded repair; pages 58, 67, and
68 are negative controls.

The producer's full final cumulative hashes (`3FE2270E...` TeX and
`DD7FE993...` PDF) remain evidence controls, not installed current files,
because the repository base had independently advanced outside the audited
span.
