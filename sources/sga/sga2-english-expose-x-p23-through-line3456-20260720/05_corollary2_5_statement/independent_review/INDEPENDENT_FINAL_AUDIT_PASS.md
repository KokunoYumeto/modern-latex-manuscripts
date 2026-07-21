# Independent final audit - SGA2 Exposé X, Corollary 2.5 statement

## Outcome

**PASS.** The bounded producer unit for French lines 3439-3444 passes
independent authority replay, translation and register review, same-edition
locator review, current comparison-candidate/adverse-delta review, fresh
build/render/text/font reproduction, producer-ledger validation, Artifact Tool
replay, manifest replay, and privacy classification. This is an internal
seal-quality review of the Corollary 2.5 statement, not a public payload,
archive handoff, whole-exposé claim, or whole-volume claim.

## Authority, boundary, and continuation

- French authority: 586,789 bytes, SHA-256
  `C2F899E92A904E312B550C6452A117FF23D30AF984B2254A0961D2DF0DACD042`.
- Terminal-LF lines 3439-3444: 333 bytes, SHA-256
  `92F6573CE4524B6839658A73C9621D897422B8354F1577097179851E4B0EA86D`.
- Coordinates: original printed page 117, physical source-PDF page 101,
  recomposed running page 93.
- Line 3445 is blank. Raw cursor: 3445. Next substantive cursor: 3446.

The stored six-line slice is byte-identical to a fresh projection of authority
lines 3439-3444. Original-detail inspection of physical page 101 confirms the
complete corollary, all three locator systems, and the transition to
Corollary 2.6. The PDF is same-edition presence, typography, formula, and
layout evidence only. No source defect or unresolved mathematical ambiguity
occurs in this scope, and the French authority remains byte-identical.

## Translation, formulas, and terminology

The target preserves the two independent hypotheses `Lef(X,Y)` and
`Leff(X,Y)`, universal quantification, the direction and endpoints of

`Et(U) -> Et(Y)`,

full faithfulness, existential `U` and `R'`, the fiber-product base, and

`R' times_U Y isomorphic to R`.

Expanding the standing section convention behind French `pour tout U` to
"for every open neighborhood U of Y" makes the already fixed variable domain
explicit and adds no hypothesis.

The authority explicitly says an étale covering `R` but only a covering `R'`.
The English target retains that literal distinction. It does not silently add
a second "étale," and the distinction is not promoted to a source defect.
The established register "open neighborhood," "covering," "étale covering,"
"fully faithful," and "isomorphism" is sound.

## External comparison candidate

The current jcreinhold e7a259f chapter is 31,425 bytes, SHA-256
`2BDDBC3D15EECE7A47FDBDFBE31DAE735446BC14480A75113E704F63901C7BF5`.
Lines 249-254 supply useful ordinary English register and preserve the same
`R` versus `R'` adjective distinction. They also expose a substantive adverse
notation delta: the candidate writes `\hat{E}t(U)` and `\hat{E}t(Y)`, whereas
the French authority's `\Et` macro and the target require bold `Et`. That
candidate reading is rejected. The lineage remains comparison-only and does
not corroborate the French independently.

## Producer machine controls and manifest

- `MACHINE_EVIDENCE.csv`: 8 rows by 22 columns, 5,287 bytes, SHA-256
  `E3C45B624DDC723708BEDD43557377A11830A0A85FE44D0A85FFBE9A0BA5153A`;
  rectangular, CRLF-only, unique IDs, zero formula triggers, and complete
  internal reference closure.
- `MACHINE_EVIDENCE.jsonl`: 8 records, 3,548 bytes, SHA-256
  `000624849562976B1642624A309BB0575C0922BB03200C20F5D37BC9C7B663AD`;
  parse-clean, duplicate-key clean, unique IDs, reference-closed, and exact
  record-ID parity with the CSV.
- `SHA256SUMS.csv`: 25 rows by 5 columns, 4,063 bytes, SHA-256
  `02165542242A5DB1B9F8A422451D007D6A43C62D22EBE9953DF5BB58877C3C55`;
  sequential artifact IDs, CRLF-only, exact intended root-file coverage,
  exact identity replay, and zero formula triggers.

The append-only independent evidence is likewise machine-readable:

- CSV: 13 rows by 25 columns, 9,719 bytes, SHA-256
  `56957745E82A92BC8DC9444B1E0185FD8665A42CA6396E0ED7D5FB954BABD56E`;
- JSONL: 13 records, 10,091 bytes, SHA-256
  `CB2CCFDAEECB0E5765476FCE4D53401B26DEB467E417B290804D41C4A215F37D`.

Artifact Tool 2.8.24 independently re-imported the producer CSV as 8 by 22
and the review CSV as 13 by 25. Both have zero formula-error or
formula-trigger values. Original-detail inspection passed for all six rendered
column panels. Producer replay is byte-exact for region, error scan, and all
panels; its overview differs only in newly generated workbook and sheet IDs.

## Fresh build, text, fonts, and render

Three fresh pdfLaTeX passes completed. Pass 1 has the single expected
`rerunfilecheck` request; passes 2 and 3 have no matched warning, undefined
control, overfull/underfull box, emergency stop, fatal error, or LaTeX error.

- Producer TeX: 1,701 bytes, SHA-256
  `62855478F9EFA28BA875AE3A15BFF72D3572575249458DE90680A47B30AD92BD`.
- Producer PDF: 196,847 bytes, SHA-256
  `135EDC77C71D6B2FD0D375B62268CCC8CEEBD870BA9C0CCAD29D7F73E31C20E3`.
- Fresh PDF: 196,847 bytes, SHA-256
  `1E3FE4069987467C2A4D46DDEFD8110F0E32B12BB356DB39129091B08D739CF4`.
- Fresh and producer extracted text: byte-identical at 1,101 bytes, SHA-256
  `B532363FE1F0838CFBB1B3F5160BFA18F77F054643B2AF115DEE02393E70E7C9`.
- Fresh and producer raster: byte-identical at 107,275 bytes, SHA-256
  `345A0FB54EF9FF36FA17849308C2A18DBED6198FA62FABE549287C6748C39F98`.
- Fresh and producer font tables: byte-identical at 1,330 bytes, SHA-256
  `76B7C0336D8E8FE1049EE57117791C713F71E9379E4785B25D2B95AE571E0C6F`;
  all 12 rows are embedded, subsetted, and Unicode-mapped.

The PDF byte hash varies across builds because of regenerated timestamp and
identifier bytes. Page count, A4 size, non-time metadata, extracted text,
raster, and font table are exact. Original-detail review finds no clipping,
overlap, missing glyph, broken accent, or mathematical-layout defect.

## Privacy and release state

The producer has exactly three path-bearing text logs: `BUILD_PASS1.log`,
`BUILD_PASS2.log`, and the final engine `.log`. The independent review has
seven path-bearing build/engine logs. These remain internal evidence and must
be sanitized or excluded before release. Producer bytes were not changed.

Decision: independent internal **PASS** with raw cursor 3445 and substantive
cursor 3446. No archive handoff or publication is authorized by this review.
