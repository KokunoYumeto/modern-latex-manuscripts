# SGA6 English synchronization handoff through idx588

Date: 2026-07-17

Current sealed working package:

`03_working_translations\sga6_exposeX_cumulative_sync_idx532_588_en_20260717`

Coverage:

- current-rescribe indices 532--588;
- printed volume pages 519--575;
- source-PDF pages 526--582;
- Exposé X Sections 1--6 complete and Appendix Section 7 through the end of
  7.12.

Primary artifacts:

- `SGA6_Expose_X_idx532_588_English_SourceChecked.tex`
  - bytes: 89,984
  - SHA-256: `ABE6A53F9CF86D7F9FFD1E1611AC47D8E2AE4FB67D522A215E910A41DB80E6B0`
- `SGA6_Expose_X_idx532_588_English_SourceChecked.pdf`
  - bytes: 458,850
  - pages: 31 A4
  - SHA-256: `6C3596AA361F7613B17BB0EFE2A6E3A6C9A0B4DE8BE4E5B5ED56EF3631766789`
- `SHA256SUMS.csv`
  - 117 exact artifact rows, excluding itself and transient `.aux` / `.out`
  - self SHA-256: `0568B59B7C19990B940B9CA5B57D4E8AA1FEEF75BF5E3B20274E6A29D14CA9BD`

All three independent final gates returned CLEAN. Two pdfLaTeX passes completed
without errors, warnings, overfull boxes, or underfull boxes. All 31 pages were
rendered; pages 29--31 and the full contact sheet passed visual inspection.

Next cursor: **idx589 / printed page 576 / source-PDF page 583**, opening 7.13
on relations with l-adic cohomology. The source-controlled gap through idx646
is 58 indices.

Source-coordinate warning: `OS\sga6.pdf` (702 pages, SHA-256
`5194436E...E3D76`) omits idx593 and idx595--597. The French source-control
workpass used the 720-page 360-dpi Internet Archive witness
`OS\Théorie des Intersections et Théorème de Riemann-Roch.pdf` (SHA-256
`73FBBAD41340C12ECCDCFCF6C3A1656953FE3D712AA8E391678458CCD17B4BAA`),
which contains them. Future ledgers must mark the declared scan page as absent
for those indices and cite the high-resolution witness separately.

Publication remains blocked. The package is `DO_NOT_UPLOAD`; no duplicate
Zenodo record may be minted. Coordinate a completed payload under concept DOI
`10.5281/zenodo.20410947` (audited live version `10.5281/zenodo.21416482`).
