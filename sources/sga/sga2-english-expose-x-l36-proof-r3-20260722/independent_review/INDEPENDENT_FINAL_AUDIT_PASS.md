# Fresh independent final audit — PASS

Review ID: `SGA2-X-L3522-L3530-L36P-LOCATOR-R3-IREVIEW@1`  
Disposition: `PASS_INDEPENDENTLY_SEALED_INTERNAL_CHECKPOINT`  
Release state: `internal_not_for_release`  
Archive handoff by this reviewer: `false`

## Outcome

The no-overwrite R3 evidence-only successor passes the fresh independent gate. It correctly repairs the full physical-page-104 locator envelope while preserving the French authority, bounded unit, English target, and cursors. No source ambiguity or target correction remains in this unit.

The bounded proof remains French lines 3522–3530; printed pages 119–120; physical pages 103–104; running pages 95–96. Raw cursor 3531 is blank, and substantive cursor 3532 is Remark 3.7. Both same-lineage controls independently show that full physical page 104 / running page 96 begins on printed 120 and crosses marker 121, so its full-page coverage is 120–121 with `transition=true`. The line-3530 continuation at the top of that page remains on printed 120 only.

## Authority and unchanged target

- French authority: 586,789 bytes, SHA-256 `C2F899E92A904E312B550C6452A117FF23D30AF984B2254A0961D2DF0DACD042`.
- Exact French lines 3522–3530: 1,072 bytes, SHA-256 `852F3DAA8492A96586D17CDFE81114859A8E226803AC75E064666CC869FCAEC3`.
- Target TeX: 2,361 bytes, SHA-256 `F451600AF171DB989672478DF177D266B5282CE196C166EDEB554EA34291E26D`.
- Preserved target PDF: 266,866 bytes, one A4 page, SHA-256 `8D1280BF8E170787B7D6C883E564FB2733E9A918131B143BE90D1FE86110205E`.
- The target TeX/PDF are byte-identical across the original, R2, and R3 producer packages.

## Independent build, source, and visual gates

Three fresh pdfLaTeX passes completed without warnings, errors, overfull boxes, underfull boxes, or stderr. Passes 2 and 3 have identical 7,421-byte stdout logs, SHA-256 `7B66EAC9D2B0D33C21CDD9AF7A84975F30BB28F64DFE0373973169FD490DF92D`. The independent PDF is 266,854 bytes, SHA-256 `414D7C6B6CC178A1F473F889D5917D667205783E144C0DED182CDCD2F01C5D7F`; its decoded page stream, PyPDF text, 300-dpi raster, and 17 embedded/subsetted/Unicode-mapped font rows agree with the preserved target. The binary difference is timestamp-only.

Both 2005 and 2008 same-lineage controls were independently extracted and rendered at 300 dpi for physical pages 103 and 104. The source/target formula, structure, terminology, rejected-choice, footnote, and citation audit passes. Same-lineage PDFs are manifestation and locator controls only, not independent original-print corroboration.

## Machine and revision gates

- Producer CSV: 67 rows × 32 columns, SHA-256 `328062CC723FE64B577EA2899E70D8D6530F7953F4E5E233C49424CAC414A72F`.
- Producer JSONL: 67 records, SHA-256 `FA9B4BFB7E1CDF53D34E7F3801FCF4E3A3583CD6743442D5408DDE449C952BCC`.
- Fresh review CSV: 24 rows × 32 columns, SHA-256 `9A3FB587169C9EE5C98783C143B643A9478D8FBF14E958ECDB38BA8739341AF4`.
- Fresh review JSONL: 24 records, SHA-256 `C240ED31F85F493946DAE62E4868B08C7C2290B4ACC7BE9A5A7078D35D1E77D6`.
- Fresh review control validation: PASS/errors `[]`, SHA-256 `B996940AB50920D311C112736C3D11D2A6C10F10C17F40A5AE71253893C13DC3`.
- Producer recursive manifest: 213 rows rehashed with contiguous ordinals, unique safe paths, and no public-release row.

All 54 R2 record IDs remain present; 13 R3 records are added. The four affected historical R2 records are visibly retained as `SUPERSEDED` and have reciprocal `@3` revision/supersession links. Both earlier independent FAIL audits and their supporting controls are hash-bound; the eight copied second-FAIL artifacts are byte-identical to the original review files.

Artifact Tool independently inspected the producer 67×32 table and review 24×32 table, rendered four panels for each, and found zero formula-error or formula-trigger values. Original-detail visual inspection passed all eight panels. Receipt SHA-256 values are `AF9796EB7197949B1703BEEF6DBBB2F7137AF9D73131BDD865646206963526A9` and `54F9D350BF27DDA152C4D197C6C79E327A87100CAA87058DB610D6C9AD3FA575`.

## Custody caveat

This review establishes an independently sealed internal checkpoint, not a public package. Producer privacy evidence contains restricted private-path hits, and all producer/review controls remain `internal_not_for_release`. Any archive handoff must curate a privacy-clean no-overwrite successor and preserve the same-lineage/rightsholder caveats. This reviewer did not edit shared controls, contact archive maintenance, or modify producer files.
