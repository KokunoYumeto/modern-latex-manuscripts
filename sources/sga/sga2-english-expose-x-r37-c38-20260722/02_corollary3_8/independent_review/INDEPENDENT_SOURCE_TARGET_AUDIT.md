# Independent source-target audit — SGA2 Exposé X, Corollary 3.8

Review ID: `SGA2-X-C38-IR-20260722@1`

Result: **PASS on the exact producer target**. This is an independent bounded source review, not an archive handoff or a publication-readiness claim. No producer file and no French-authority byte was modified.

## Controlled identities and scope

- Producer package: `<USER_HOME>\Documents\interlanguage\03_projects\language_management\english_germanic\03_working_translations\sga2_source_aligned_en_arxiv_math0511279v1_20260718\working\unit_X_corollary3_8_statement_proof_lines3536_3540_20260720`.
- Corrected French TeX authority: `smf_doc-math_4_01.tex`, 586,789 bytes, SHA-256 `C2F899E92A904E312B550C6452A117FF23D30AF984B2254A0961D2DF0DACD042`.
- Reviewed authority range: lines 3536–3540 inclusive, 218 Latin-1/LF bytes, SHA-256 `94D108BA11D32F382E082BC77136954852D98A5FCBD1DE545A67C4064F9F3E2D`.
- Boundary replay: lines 3534–3542, 326 bytes, SHA-256 `0773A5923A4656A65C3D9F2EB2444BFF1B35EDD2EDDAD2D6FAC05DC48206F5CE`. Both saved producer slices are byte-identical to fresh slices from the live authority.
- Locators remain distinct: original printed page 120; source-PDF physical page 104; recomposed running page 96.
- Raw continuation cursor: blank line 3541, exactly one LF byte, SHA-256 `01BA4719C80B6FE911B091A7C05124B64EEECE964E09C058EF8F9805DACA546B`.
- Next substantive cursor: line 3542, 90 bytes without EOL, SHA-256 `DF17A55BC0E31E17B96E03B83BF2108252101010433948276728DB4A0D519B84`.

The same-edition reader is 1,576,954 bytes, SHA-256 `41AD02C57321A8D2200FF32A929BC93ADBC3DE0D59DCD5A284D28D859FB87A90`. It was used only for manifestation and locator checking. It is not independent original-print corroboration. Its physical page 104 shows running page 96; Corollary 3.8 occurs before the marginal printed-page 121 transition, confirming the corollary's original printed-page locator as 120.

## Source-to-target findings

The exact producer TeX is 1,563 bytes, SHA-256 `856B396D68A41AD2F6EAFD17AB50C0B2167519D4361E378EFE1F758BFEF9146B`. It passes all substantive checks:

- `corollaire`, label `X.3.8` becomes visibly numbered `Corollary 3.8.`.
- `A` remains a noetherian local ring.
- `\prof A\geq 2` becomes the established English normalization `depth A ≥ 2`; the base symbol, value, and inequality direction are unchanged.
- `\hat{A}` becomes typographically explicit `\widehat{A}`; the completed-ring hat is present and attached to `A`.
- The implication retains its direction: purity of the completed ring implies purity of `A`.
- `\Ref{X.3.5}` and `\Ref{X.3.6}` become `Lemma 3.5` and `Lemma 3.6`, in source order. The authority defines those labels at lines 3501 and 3519.
- The conventional label `Proof.` is supplied, but no unsourced QED mark is added.

No grammatical, mathematical, numbering, reference, or symbol defect was found in this bounded French unit. No silent emendation is present.

The jcreinhold `e7a259f` file is 31,425 bytes, SHA-256 `2BDDBC3D15EECE7A47FDBDFBE31DAE735446BC14480A75113E704F63901C7BF5`, and was used only as a comparison lineage. Its hidden numbering, literal `prof`, degraded code-form completion glyph, “Then if” ordering, and absence of a proof label were not adopted without source checking.

## Independent build and machine evidence

Three fresh pdfLaTeX passes on the exact producer TeX exited zero. Each preserved pass log is 24,294 bytes, SHA-256 `9953FEEBDBB43AC6BA27844E43D2D9B2468FD39A679117BFC82C75483E497E19`; scans found no TeX error, LaTeX/package warning, overfull/underfull box, undefined control sequence, emergency stop, or fatal error.

The independent PDF is 184,318 bytes, SHA-256 `B9B66D0D33C3172416AFFC7E38A5F50C095D6D25672EC7FB1BC5E19C71648C67`. It is byte-different from the producer PDF, as expected for a fresh TeX build, but its 200-dpi render and layout-text extraction are respectively byte-identical to the producer render and extraction.

Fresh validation independently confirms:

- producer combined CSV: 43 rows × 26 columns, SHA-256 `1B4FF2A58E85BCD7A3C45AD7633BCBDCD0CD663070EF51B520D5B9B34E05D863`; rectangular, canonical CRLF, unique nonempty IDs, zero formula-safety triggers;
- producer JSONL: 43 records, SHA-256 `E41272510B2DBC86286F0228766DC5EBBAAB6B0D03D4CD96815C855A1810130E`; parse/schema/reference closure and acyclicity pass, with evidence identities exact;
- producer SHA-256 manifest: 60 rows × 7 columns, SHA-256 `47FF6E48DD1E8A1356702A7F7F43AE9B099BAAD90AEB53ACA9A08FB40555ED19`; all 60 represented identities exact;
- independent review CSV: 17 rows × 26 columns, SHA-256 `7253D63AE523828F146D2FFB3578DD06F7AC9921038EFBF48B1C4F7BE116053B`;
- independent review JSONL: 17 records, SHA-256 `2579E0AAA0C7F3D7A92C40C539B7B172873DC9C4D47AC0A524C8A69D31803CA0`;
- independent validation: PASS with `errors: []`, SHA-256 `3AB175EB1EDF86184F43760FA796158B03967C0DA1B41350CFEDA13D42915AA2`.

All review artifacts remain `internal_not_for_release`. No shared manager status/log was edited and no archive, GitHub, or Zenodo handoff was made.
