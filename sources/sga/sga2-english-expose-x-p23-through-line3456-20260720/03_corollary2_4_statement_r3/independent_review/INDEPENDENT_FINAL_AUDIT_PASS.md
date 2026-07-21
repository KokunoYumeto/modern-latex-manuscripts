# Independent final audit PASS — SGA2 Exposé X, Corollary 2.4 statement R3

## Decision

**PASS.** The R3 producer successor resolves the R2 package's sole blocking
evidence defect: the root manifest now follows its claimed true ordinal
comparator. The French slice, English target, formulas, comparison excerpt,
build controls, extracted text, raster, and font table are unchanged. The
predecessor producer and its independent evidence-only FAIL remain preserved.
This is an internal bounded review; it is not a publication claim, archive
handoff, or whole-exposé/volume seal.

## Exact scope and continuation

- Unit: complete Corollary 2.4 statement, French authority lines 3429–3431.
- Locator systems: printed page 116; physical source-PDF page 101;
  recomposed running page 93.
- Blank line 3432 is excluded. Raw cursor: 3432. Next substantive cursor:
  3433, the proof line carrying the next `\pageoriginale` marker.
- Editable target units: one TeX file. Built target: one A4 PDF page.
- French authority: 586,789 bytes, SHA-256
  `C2F899E92A904E312B550C6452A117FF23D30AF984B2254A0961D2DF0DACD042`.
- Exact source slice: 351 bytes, SHA-256
  `374361D7850F93B348F1CDB311AA4FCF4F1F728D22C5ECC9C6A79A212D36BF11`.

Direct replay confirms that the statement ends at line 3431, line 3432 is
blank, and line 3433 begins the proof. The source page confirms the locators
without conflating them. The same-edition page image is manifestation/layout
evidence only, not independent original-print corroboration. No source defect
or unresolved mathematical ambiguity was found in this bounded statement.

## Source, translation, formula, and comparison audit

The target preserves `Lef(X,Y)`; the finite flat covering `R` of an open
neighborhood `U` of `Y`; connectedness if and only if connectedness of
`R\times_U\widehat X`; and the final equivalence between connectedness of
`Y`, `U`, and ordinary `X`. The completed `\widehat X` occurs exactly once,
in the fiber product. The final condition is ordinary `X`, not completed
`\widehat X`. Quantification, directions, subscripts, hats, equivalence
status, and terminology agree with the French TeX.

The jcreinhold e7a259f chapter remains comparison-only. Its readable English
register is useful, but its final “completed hat-X” reading is rejected under
stable adverse ID
`SGA2-X-C24-JCREINHOLD-L234-HATX-ADVERSE-001@1`; French authority and the
English target require ordinary `X` there.

Target identities remain:

- TeX: 1,525 bytes, SHA-256
  `DC1CA697B77344CFF33C631A253A52C5132C346E7B77E0965E6891A9DA09E02F`;
- frozen producer PDF: 172,038 bytes, one A4 page, SHA-256
  `3B179631D2658B6CF593F95BAC76F9CE1CF3C990909DB11B606FACC17FBF5677`.

## Manifest-only successor and predecessor retention

The corrected root `SHA256SUMS.csv` has 30 rows × 5 columns, exact root-file
coverage, exact identities, and `.NET StringComparer.Ordinal` order on the
relative paths. The first seven data rows are uppercase Artifact Tool
evidence names; lowercase `artifact_tool_machine_qa.mjs` is data row 29 and
`generate_ordinal_manifest.ps1` is data row 30. Independently serialized as
`relative_path<TAB>bytes<TAB>sha256<LF>`, the ordinal canonical SHA-256 is
`AB86275F45EFC78EA344704891182A2B61545C1E5DE75A344C7C5275C916444D`.
The manifest file itself is 6,169 bytes, SHA-256
`2B78AF5FEB02B109C6D75C03B3787376B26AC7FE87357686F5A18BD7FCB3356D`.

The old R2 manifest remains preserved at SHA-256
`6A7E4B9F8A96DB6CC13192F3DE8ABA08BCA939D8A7C057BB5080C5ACD93AB602`.
Its order mismatch remains visible under
`SGA2-X-C24-STMT-R2-IR-ERR-MANIFEST-ORDINAL-001@1`; the append-only
resolution is revision `@2`. The predecessor FAIL audit remains 6,610 bytes,
SHA-256
`44333AED1B1407140F6CF5D9DCE229FECCC613223D3B64BB16F87DE5ACC62419`,
and its validation remains 10,283 bytes, SHA-256
`E07B2DEB99405E53222913B8583ECF532E690A12D9480C348D107CCAB349CC03`,
with status `FAIL_CLOSED_MANIFEST_ORDER_ONLY`.

The 76-row predecessor identity manifest replays with zero errors: 32
producer files and 44 prior independent-review files. Its SHA-256 is
`CA0768A465E6C09D51BA98DFE23FA1FDD0F0571D023C907917DB98FE1B6ED0FC`
and ordinal canonical SHA-256 is
`DEDB5F8DCD4E1851631C573A441258AD353A9F6FDB21F1E8AA499F1D84482FBC`.
The separate 13-row unchanged-artifact ledger replays byte identity for the
source, target, comparison, build, text, font, and raster controls; its
SHA-256 is
`E1489E363D580606915BB9B7C02CDEB7076F226CB74A040955C33801046A953D`.

## Fresh isolated build and render

I copied the target TeX into `rebuild/` and ran three independent pdfLaTeX
passes. Pass 1 has only the expected rerunfilecheck warning; passes 2 and 3
have no warning/error matches. The fresh PDF is 172,038 bytes, SHA-256
`C589DFE9BE317F0BE29D469B0C03EBF5728D54543E65209B5DAB86F3905E413F`.
Its binary hash differs from the frozen producer PDF because of timestamps;
normalized non-time `pdfinfo`, extracted text, 150-dpi raster, and font table
are exact. The raster SHA-256 is
`49C9867865134729AD59C93E463F2A8F3250576F69C58986F516400EC0FDD65A`,
with pixel absolute error `0 (0)`. All 11 font rows are embedded, subsetted,
and Unicode-mapped.

Direct visual review at original detail passed for the source page, producer
target page, fresh target page, all three producer-ledger panels, and all
three independent-ledger panels. Details are in `INDEPENDENT_VISUAL_QA.md`
(4,493 bytes; SHA-256
`200CDF0D419DF1EFEE47FEF6359E84C135BD846ECC5B707B4C254B2ED33FF35B`).

## Machine-readable gates

Independent replay results:

- producer CSV: 21 rows × 22 columns, 14,325 bytes, SHA-256
  `4EA221C92A13D94089950AB8A7ABD66733CC45CB2BFBB28C04E0DEAE79A02617`;
  rectangular, CRLF-only, formula-safe, schema-valid, ID-unique,
  reference-closed, and supersession-consistent;
- producer JSONL: 21 records, 12,319 bytes, SHA-256
  `7FC6E826EAE31579C3D25984F73FD588222ADD36AFFF8CE8415C194FFB0120A7`;
  duplicate-key-safe parse/schema/ID/reference/supersession closure PASS,
  exact CSV ID parity, and reciprocal required revision families;
- corrected producer root manifest: 30 rows × 5 columns, exact identities,
  coverage, ordinal order, and formula safety PASS;
- predecessor history manifest: 76 rows × 5 columns, 76/76 identities PASS;
- unchanged-artifact ledger: 13 rows × 7 columns, 13/13 identities PASS;
- independent review CSV: 17 rows × 25 columns, 13,527 bytes, SHA-256
  `8556BCAE118035B9EF9C7941CEE29A3726383968FE749A9804EEDEB0D85A570B`;
- independent review JSONL: 17 records, 19,131 bytes, SHA-256
  `0D3A1AADB7AE0EA9E37000BFE306384B14753BB029FB5A525C5E4750207E90EC`.

Artifact Tool 2.8.24 replayed the producer 21×22 CSV and the independent
17×25 CSV with zero formula-error values and zero formula-trigger values.
Producer replay is exact outside nondeterministic workbook object IDs. The
producer replay receipt SHA-256 is
`CCE90F1566B9C2A5EA062BA5FA4E67771987C3E0DB30D2E0B7154FA99840EAF8`;
the independent-ledger receipt SHA-256 is
`3CE0600B903ADB9C7BD91A222BD790995FB1759018A232B70A8EC18F64DE97A8`.

## Privacy and release disposition

The producer root has exactly three disclosed private-path text files:
`BUILD_PASS1.log`, `BUILD_PASS2.log`, and the final TeX engine `.log`. The
independent review has four path-bearing build/engine logs. They must be
sanitized or excluded before any public payload. Every current record remains
`internal_not_for_release`.

No producer byte was modified. No archive handoff was made. PASS authorizes
the parent/manager to treat this bounded manifest-order evidence defect as
independently resolved; it does not itself seal, publish, upload, or advance
past the preserved substantive cursor 3433.
