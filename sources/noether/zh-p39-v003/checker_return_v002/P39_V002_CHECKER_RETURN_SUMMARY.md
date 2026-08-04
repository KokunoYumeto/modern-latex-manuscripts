# ZHCHK-NOETHER-P39-V002-RETURN-001

**Disposition: `rejected_correction_required`.** The frozen P39 v002 Hans artifact is accepted. The frozen controlled-generic Hant artifact and its producer evidence package are rejected pending exact correction.

## Frozen custody and authority

- Producer manifest: 42 unique non-self members, 5,065 bytes, SHA-256 `CAD0EDDD79A9C1182CD133C47F4ED03C0C644A1EFAB8E9A23387331B6C240FC1`; independent replay 42/42, zero failure.
- Freeze receipt: 6,342 bytes / `88F57B06F241F7E50F6AF8AE1BB3C4BAF8DCF08FCA3295ECE3C4FC8D7B3C2DB0`.
- Handoff: 3,539 bytes / `DEE14047A00DAA16B007332BFE211BD19C098C71137D6CC7FB6140FC71C30375`.
- Authority remains binder `NOETH-DE-BINDER-P39-ZH-COMPLETE-20260804-001`; exact LF source 18,724 bytes / `4F6355189925F249DE27FE5FD25C22FB3A2226088EBB7CAF5CB486607A112B7C`. No German defect or packet is warranted.

## Artifact disposition

- **Accepted Hans:** TeX 16,141 / `101836C41985DEE9B1A8FCC74A76CD9DF082BE2D07E2A3D45E22BC4DE68C6FE6`; PDF 261,533 / `367061323E97D9D7431B883D48F190A214A224D62F3901C8E01DD1BCA7125BA1`.
- **Rejected Hant:** TeX 16,322 / `DEF7DFDCF1545066447880698B1A1C109D4BBED2CEDC4B8409D786044FCEEE33`; PDF 276,331 / `EE22B4475DB19B48FDD7838A307C0069CE06682EBDC370AB4A9BBE46DEC431C5`.
- **Validated checker Hant candidate:** TeX 16,322 / `F0E9425763D5E075A5ED1810FE2B1DC2BDAAF6FD48691BE8C3D64F4B158AF1C8`; PDF 274,924 / `8DE2CAB0FB81E604CF365550FD081B3C2227A1546E98759BE0B35A766F303090`.

## F001 — exact Hant corrections

Apply exactly seven replacements in `Noether_Paper39_Chinese_CurrentAuthority_zh-Hant-controlled_v002.tex`:

1. `34:15 超復→超複`
2. `45:1 超復→超複`
3. `50:69 着手→著手`
4. `50:150 一箇→一個`
5. `52:58 超復→超複`
6. `52:347 超復→超複`
7. `72:70 一箇→一個`

The checker candidate contains exactly these seven textual changes, retains the complete non-Han TeX stream, builds in two serial XeLaTeX passes, extracts to exactly the seven expected PDF-text changes, and passes all four fresh-page visual checks.

## F002 — exact evidence corrections

The three CSV ledgers and corresponding concept-graph nodes must describe the target/source that actually exists:

- T002: `单纯正规代数/單純正規代數` → `中心单代数/中心單代數`.
- T012: `阿廷导子/阿廷導子` → `Artin 导子/Artin 導子`.
- T013: `素位` → `位／分歧位`.
- T016: `平方化` → `平方映射`.
- T018 exact German phrase: `zerfallende Algebra | zerfallenden Algebren` → `zerfallende Algebrenklasse | zerfallenden Algebren | zerfallende Algebren`.

Hash-pinned corrected candidates for all four evidence artifacts are in `selected/candidates/evidence/`.

## Independent validation

- All 23 formula witnesses, five numbered displays, five prime-labelled cyclic displays, 12 ordinary footnotes plus the separate mark/text pair, and 14 bibliography/apparatus witnesses are preserved.
- Exact original Hans, exact original Hant, and candidate Hant each completed two serial XeLaTeX passes with four pages and no fatal, overfull, underfull, or missing-character event.
- Five PDFs were freshly extracted and rendered with Poppler at 180 dpi. All 20 pages were opened and visually inspected. Layout failures: zero.
- Producer and checker-built original Hans/Hant pages have exact text and raster identity. Candidate pages 1-2 contain only the expected corrected-glyph/local-reflow changes; pages 3-4 are raster-identical to the original Hant.

## Required producer response

Carry Hans forward unchanged, integrate F001 and F002, serially rebuild and freeze a successor package, and re-hand it to this persistent checker. Hant remains controlled generic only: no zh-Hant-TW/HK/MO localization is claimed. zh-Hans-SG is absent. German and SGA remain untouched.
