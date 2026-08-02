# EGA French canonical TeX — compact continuation handoff

Date: 2026-08-02

## Durable objective

Produce a diplomatic, source-faithful French TeX corpus for the eight bounded
NUMDAM publications comprising EGA I--IV. Preserve printed French wording,
formulae, numbering, punctuation, and source oddities; do not silently create
a corrected French edition. In parallel, recheck each prior English correction
or normalization against the direct authority image and record an individual
rationale. Reverse any unsupported English correction append-only and repair
every active English source carrying it.

The complete English standalone and cumulative readers already exist. The
global predecessor is
`03_projects/language_management/english_germanic/<REDACTED_INTERNAL_WORKSPACE>/EGA_English_Global_0_IV_complete_linked_reader_20260801_r1`.
Do not rebuild it merely to advance the French cursor. Current source-backed
English repairs accumulate in the separate no-overwrite successor
`EGA_English_Global_0_IV_french_recheck_source_successor_20260802_r1`.

## Authority closure

`controls/AUTHORITY_SHA256.csv` binds the eight NUMDAM PDFs: EGA I, EGA II,
EGA III-1, EGA III-2, and EGA IV-1 through IV-4. They total 1,800 physical PDF
pages. OCR and extracted text are locator/drafting material only; the direct
PDF image decides.

Current EGA I authority:

- `<REDACTED_USER_HOME>/Documents/Papors/OS/NUMDAM/EGA_I_PMIHES_1960_4.pdf`
- 31,680,717 bytes / 227 physical PDF pages
- SHA-256
  `9ABA23020217535977E279BDD06A0413F48DA703086865BA4C00766C85DF4AE6`.

## Controlling exact admitted state — through printed p.75 / 7.6.18

This section supersedes the older p.74 continuation snapshot below; the older
section remains append-only history.

- Current production volume: EGA I.
- Admitted source: source/ega1/frontmatter-fr.tex,
  source/ega1/intro-fr.tex, and source/ega1/ega0-1-fr.tex through complete
  paragraph 7.6.15, Proposition 7.6.16 and proof, Proposition 7.6.17 and
  proof, and Corollary 7.6.18 and proof.
- Main source identity: 270,458 bytes / 5,726 lines / SHA-256
  CBE2C566A9DE9366F3F5859AD2563C7EFCB36FA9DAC9A17C7DE73186692ADBB8.
- Exact next cursor: the section 7.7 heading and paragraph 7.7.1 on printed
  p.75, continuing onto p.76. No section-7.7 text is admitted.
- Direct authority manifest:
  controls/EGA1_PRINTED74_75_SECTION7615_7618_DIRECT_AUTHORITY_IMAGES.json,
  2,993 bytes / SHA-256
  A5623387606C16D2DC3360971781F36E8D5BDF65FA70CD8C41D55636C8F39675.
- Controlling bounded PDF: R58, 59 pages / 399,323 bytes / SHA-256
  4C9F136C4A8C5DBDF939F4B0A0B4A68530BA52C9BAD8BD15669C968EC863ABF8.
  Passes 2 and 3 are identical, checked hard diagnostics are zero, and output
  pages 58--59 pass personal 1,200-dpi layout inspection.
- Progress: 72 source-bearing pages admitted out of 1,800 physical pages,
  4.0%; approximately 1,728 physical pages remain.

## Controlling English correction/recheck state — through printed p.75

- The complete decision surface has 147 records. Twenty-six cumulative
  English repairs are applied; four justified no-edit decisions remain. No
  admitted correction has been reversed.
- P75 decision ledger: three rows / 4,464 bytes / SHA-256
  8FEEADF8588E430401C865293AE55DE34B9A73CC61894140FE475674183F2D52.
  The repairs are flat for→flat over, restoration of the omitted copula in
  the local-ring assertion, and a logged nonsemantic “We already know”
  register normalization.
- Current sole changed source: source/ega0/ega0-7.tex, 75,432 bytes /
  SHA-256
  81196521B4A963CFD614452C63C1669482B4C58A6A2E250DD593B1B11159F036.
- Current exact source manifest: controls/SOURCE_INPUT_SHA256_R9.json, 24,485
  bytes / SHA-256
  203A7E34F3BC5683E4612DA4300358B4A5DD295EA2781454811EB2C15A38B05D;
  127/127 rows, 7,280,020 bytes, ordinal tree SHA-256
  B20246760E9A19F7050C457EC91697105B6CB255FBBDDEFF15DD0718716698AE.
- Current diff validation: controls/SOURCE_DIFF_VALIDATION_R9.json, 5,421
  bytes / SHA-256
  40AC5CDB5B686B5468DCD67B26BD9C5BFCA329D080D0FC696181AAE6DF6E9C90.
  Replay is 2,556 bytes / SHA-256
  0C984F40AA06735D214D7E3264FD7C5DC3C5AF1FFE5EEFACF2E0CE4C9A84A8AA.
  Both pass with errors empty; exact inverse reconstruction returns the R8
  source hash.
- The lead's malformed overline-f exponent was caught before build and is
  closed append-only in controls/WORKFLOW_ERROR_APPEND_P75_20260802.jsonl,
  SHA-256
  A95844DDAA237547B777E1EE745AD24AE5F39347D84BFF9DBEB3CBCB0005F51B.
- Continue source-first from direct p.75/p.76 images. Do not reconstruct the
  next French text from English; English is comparison and repair surface
  only. Keep high-detail crops serialized, global English rebuild deferred,
  and release/archive gates held.

## Controlling exact admitted state — through printed p.74 / 7.6.14

This section supersedes the older p.72 continuation snapshot below; the older
section remains append-only history.

- Current production volume: EGA I.
- Admitted source: source/ega1/frontmatter-fr.tex,
  source/ega1/intro-fr.tex, and source/ega1/ega0-1-fr.tex through complete
  Corollary 7.6.14 and its proof. Proposition 7.6.10 includes its exact
  p.73/p.74 seam.
- Main source identity: 266,060 bytes / 5,641 lines / SHA-256
  C5D6E1F1367641E914C184892DEBDABF3B0EDDF2E2F2BD167835CD7430343A7D.
- Exact next cursor: 7.6.15 on printed p.74, continuing on p.75. No 7.6.15
  text is admitted.
- Direct authority manifests:
  - controls/EGA1_PRINTED73_PROP764_7610_DIRECT_AUTHORITY_IMAGES.json,
    3,354 bytes / SHA-256
    8DCD975AEC1239EC200674C02ABB201C39377A0FE3848B56BBD8CDBB7B6F9849;
  - controls/EGA1_PRINTED74_PROP7611_7614_DIRECT_AUTHORITY_IMAGES.json,
    2,650 bytes / SHA-256
    0C4CEC360787E787DB968EB8CAF6DB919BC9BAFF572790DF8843EC35B9EAC7B4.
- Controlling bounded PDF: R57, 59 pages / 394,596 bytes / SHA-256
  BE505741832275CA07930B1C931F23094C74F8A2EAD8003628D95E4927A3837D.
  Passes 2 and 3 are identical; checked hard diagnostics are zero; final two
  output pages pass personal 1,200-dpi layout inspection.
- Progress: 71 source-bearing pages admitted out of 1,800 physical pages,
  approximately 3.9%; approximately 1,729 physical pages remain.

## Controlling English correction/recheck state — through printed p.74

- The complete decision surface has 144 records: the prior 138 plus six new
  p.73--p.74 records. Twenty-three cumulative English repairs are applied;
  four justified no-edit decisions remain. No admitted correction has been
  reversed.
- Current sole changed source: source/ega0/ega0-7.tex, 75,427 bytes /
  SHA-256
  3A7611B105182E45AA33C945C85E34A48A2C46369568A686F7E6F73810D54AA7.
- Current exact source manifest: controls/SOURCE_INPUT_SHA256_R8.json, 24,222
  bytes / SHA-256
  6087C82E314965389977E80D4E964EBB47AA2A205D699B1160B5455FB21AE851;
  127/127 rows, 7,280,015 bytes, ordinal tree SHA-256
  7A0E4D9FB6A352C04009029A692E3E9D133015ECBFBBF52005BEF95F0A6B5F1A.
- Current diff validation: controls/SOURCE_DIFF_VALIDATION_R8.json, 5,055
  bytes / SHA-256
  33F169EA742114018CA857D6391CEE89ECD9ABDB92B77AE79952EBC6D1731C32.
  Replay is 1,481 bytes / SHA-256
  0B6D72131B9918330D525A4932841A4D6244A709D4DFE4A88F9DB782E05D843C.
  Both pass with errors empty.
- The printed French closing locator 7.2.8 in the proof of 7.6.11 is preserved
  diplomatically. English uses 7.6.11 with an immediate source note. Never
  erase that provenance by silently changing the French.
- R56 is adverse history for my unsupported proof wrapper; the exact closed
  workflow-error record is
  controls/WORKFLOW_ERROR_APPEND_P74_20260802.jsonl, SHA-256
  D34D6F0B0246D12038C7EBB403AEF62DA9A1A37119F6E24F093ECDAC7AD00DC9.

## Controlling exact admitted state — through printed p.72

- Current production volume: EGA I.
- Admitted source: source/ega1/frontmatter-fr.tex,
  source/ega1/intro-fr.tex, and source/ega1/ega0-1-fr.tex through complete
  Proposition 7.5.5, 7.6.1, Proposition 7.6.2 with proof, Corollary 7.6.3,
  and the terminal cautionary paragraph on printed p.72 / physical PDF page
  71.
- Main source identity: 257,449 bytes / 5,463 lines / SHA-256
  2F511A63F9F13EDC8DB12A365731B392F2931ADE690290A09151A5DC4DD0A2A1.
- Exact next cursor: Corollary 7.6.4 on printed p.73. No p.73 text is
  admitted.
- Controlling authority-image manifest:
  controls/EGA1_PRINTED71_72_PROP755_763_DIRECT_AUTHORITY_IMAGES.json,
  3,483 bytes / SHA-256
  668DF770147CA68EC7EEA4D8A06D7B06BFBB9E684AAEFF85AA4427FBC4B4CA24.
- Controlling bounded PDF: R54, 57 pages / 385,147 bytes / SHA-256
  FAC9F2A96AFAB501D852E27FC3CB2873B0BC5504718E2ABFAB3EE576708B21F8.
  Three serialized passes converge; checked diagnostics are zero; output
  page 57 was personally inspected at 1,200 dpi and passes. Source fidelity
  comes from the direct 5,000-dpi authority bands.
- Progress: 69 source-bearing pages admitted out of 1,800 physical pages,
  approximately 3.8%; approximately 1,731 physical pages remain.

## Controlling English correction/recheck state — through printed p.72

- Current total decision surface: 138 individually bound records = 108
  confirmed English errors + 22 French-source issues + two official
  erratum/addendum decisions + three external additions. Thirty-one are
  formally source-justified. No admitted English correction has been
  reversed.
- The new pp.71--72 decision file has eight rows / 10,398 bytes / SHA-256
  502D5089998CE3BE4D69237730C99FE89F803FE3FED70CAEE521041DBA01F700.
  Five repairs are applied and three decisions justify no edit.
- Seventeen cumulative English repairs are now applied in the complete copied
  source successor. Its sole changed file is source/ega0/ega0-7.tex, 75,260
  bytes / SHA-256
  C576296A78A1303323C7296A7CCF9B989FCA8FF7C2C8A981140F66651B17A747.
- Current manifest: controls/SOURCE_INPUT_SHA256_R6.json, 23,692 bytes /
  SHA-256
  C47C6AAD610A7FF3A15A54C5E3931C2E1E28A2D237D3D4D26FD845947C523B35;
  127/127 rows, 7,279,848 bytes, exact ordinal tree SHA-256
  0B11488A0F866FBF0AF5575AF6E6F77B322C08969BD9034821210EF2F47A00A7.
- Current validation: controls/SOURCE_DIFF_VALIDATION_R6.json, 4,058 bytes /
  SHA-256
  9C210905CE159FED2B4CA6745CD5AAF3CC5F039502DC04FAD6805A44B7D34311,
  PASS/errors empty. Replay: 1,356 bytes / SHA-256
  23BB830C291DC10C349DC825A49FE41F2F78F271D746E528F0FD6863C3C64D11.
- Global rebuild, reference-coordinate replay, privacy-clean projection,
  rights/caveat and package closure, explicit archive handoff, public
  readback, and dual-DOI logbook binding remain held.

The older p.71 state below is append-only point-in-time history.

## Exact admitted state

- Current production volume: EGA I.
- Admitted source: `source/ega1/frontmatter-fr.tex`,
  `source/ega1/intro-fr.tex`, and `source/ega1/ega0-1-fr.tex` through complete
  Proposition 7.5.4 and its proof on printed p.71 / physical PDF page 70.
- Main source identity: 251,121 bytes / 5,341 lines / SHA-256
  `52B886E42D7B2C904074DEC2725475D43519D95EC5D7A6C9BF94291B4B505561`.
- Exact next cursor: Proposition 7.5.5 on printed p.71, continuing on p.72.
  No 7.5.5 text is admitted.
- Controlling authority-image manifest:
  `controls/EGA1_PRINTED70_71_PROP754_DIRECT_AUTHORITY_IMAGES.json`, 2,663
  bytes / SHA-256
  `D4AC485571C2BA8DC4E2DE59664728D5488A29217B6E723825E198A399489C58`.
  It binds the direct 5,000-dpi p.70/p.71 reading surface.
- Controlling bounded PDF: R50, 56 pages / 378,288 bytes / SHA-256
  `BA4E1BAA58FD8DE9DED8C48E6C6A7AE92898083CA770FC7590FE8655A84C3598`.
  Three serialized passes converged; checked diagnostics are zero; output
  pages 54--56 were personally inspected at 1,200 dpi and pass.
- Progress: 68 source-bearing pages admitted out of 1,800 physical pages,
  approximately 3.8%; approximately 1,732 physical pages remain.

## English correction/recheck state

- Baseline rationale annex:
  `controls/ENGLISH_CORRECTION_RECHECK.csv`, 117 data rows / 89,159 bytes /
  SHA-256
  `3F56E5F7F24E321BB7AECECFC26174937139527744AD834A7CF509ED3CFD3652`.
- P.69 append: `controls/ENGLISH_CORRECTION_RECHECK_APPEND_20260802.jsonl`,
  three records / 4,790 bytes / SHA-256
  `0AC3732031D359DA8F547BDCFA1B9850A353BF5ADF1604B4BBABA9C487480560`.
- Pp.69--70 append:
  `controls/ENGLISH_CORRECTION_RECHECK_APPEND_P70_20260802.jsonl`, six records
  / 8,437 bytes / SHA-256
  `A49C199D52DB2623B86B880FC22951014A8C60558C4B1DD0DE58419A2D920494`.
- P.71 append:
  `controls/ENGLISH_CORRECTION_RECHECK_APPEND_P71_20260802.jsonl`, four
  records / 5,116 bytes / SHA-256
  `99CF1649C8AB3128F57192C7D759907D6398DDEB071BDF8F232571A5C986518C`.
- Current total decision surface: 130 individually bound records = 103
  confirmed English errors + 22 French-source issues + two official
  erratum/addendum decisions + three external additions. Twenty-three are
  formally source-justified. No admitted English source-correction judgment
  has been reversed.
- Twelve English repairs are applied in the complete copied source successor.
  Its only changed source file is `source/ega0/ega0-7.tex`, 75,199 bytes /
  SHA-256
  `8DD6840E73ADBE9D529AE39979B495BB7BC2D4CAFC8DE72C2F2EA870E46D1528`.
- Current source manifest:
  `controls/SOURCE_INPUT_SHA256_R5.json`, 24,084 bytes / SHA-256
  `38E8BD3642A7CBDE07428D9D13447A75DBFD6AAEE0A8B2B682B9F989DEEDB61C`;
  127/127 rows, 7,279,787 bytes, exact ordinal tree SHA-256
  `30E8197C89FCE61EEB9ACAC82EE40985CB7C1B8F277FE627181B9C4195A8DCDA`.
- Current source-diff gate:
  `controls/SOURCE_DIFF_VALIDATION_R5.json`, 4,489 bytes / SHA-256
  `F0987DB31A57930111FD97A551DC379E6D68AA5701FC93673E0C229FC5B3956E`,
  PASS/errors empty. Replay:
  `controls/SOURCE_DIFF_VALIDATION_R5_REPLAY.json`, 2,138 bytes / SHA-256
  `F8E9B03EE5FE51A51C3EEB4BD2105692A599E383681F4F7A5CDB915388BB4108`.
- R1 diff validation and R2/R3 source manifests remain adverse history. R3
  had exact rows but a list-order aggregate mislabeled as ordinal. The error
  and R4 supersession are append-only and had no source effect.
- Global rebuild, reference-coordinate replay, privacy-clean projection,
  rights/caveat and package closure, explicit archive handoff, public readback,
  and dual-DOI logbook binding remain held.

## Required working method

1. Work sequentially from the exact cursor; keep printed page, physical PDF
   page, and TeX locus distinct.
2. Read the direct authority image personally. Use roughly 1,100--9,000 dpi
   according to the represented detail: lower detail for page context,
   approximately 5,000 dpi for dense mathematics, and 9,000 dpi only where an
   ambiguity remains. Do not generate new OCR.
3. Preserve printed French typos diplomatically and catalogue their English
   disposition. Do not silently normalize the French source.
4. Recheck the parallel English before admitting a correction. Each decision
   row must state the source reading, English state, decision, and rationale.
5. Compile only after real edits, serialized. Inspect changed output pages and
   seams; output-layout renders are not authority evidence.
6. Append every admitted range, decision, failure, supersession, exact cursor,
   file identity, and build identity to `LOGBOOK.md`. Keep the newest
   controlling block at the top of `STATUS.md` current.
7. Avoid embedding large images or huge command output in task history.
   Compaction of large histories has caused CPU/RAM spikes and machine crashes.
8. Treat
   `controls/ENGLISH_NORMALIZATION_DECISION_AND_REVISION_POLICY_20260802.md`
   as controlling. Every functional English departure from printed French
   needs its own authority-bound rationale.
9. Never rewrite a wrong decision silently. Append a superseding record,
   explain what was wrong and how it was caught, and repair every active source
   carrying it before calling the reversal closed.
10. At an authorized bounded/final archive handoff, bind privacy-clean exact
    logbooks, decision ledgers, revision history, and continuation identities.
    Deposit those provenance surfaces in both the methodology DOI and the
    replication DOI under
    `PROJECT_LOGBOOK_METHODOLOGY_REPLICATION_DOI_REQUIREMENT_20260802.md`.

## Natural non-overlapping future bounds

- Finish EGA I: approximately 161 remaining physical pages.
- EGA II: 219 pages.
- EGA III-1 plus III-2: 254 pages total.
- EGA IV-1: 258 pages.
- EGA IV-2: 228 pages.
- EGA IV-3: 254 pages.
- EGA IV-4: 360 pages; split only at an exact section boundary if task-history
  size becomes unsafe.

Do not let two tasks mutate the same publication/range. Any allocation change
must state exact opening cursor, terminal cursor, authority identity, and hard
stop.

## Post-EGA routing

Do not continue Deligne in this already large task. Once the EGA corpus and
its self-contained logbook close, hand the distinct later Deligne scope to one
smaller existing Deligne task with an exact no-overlap receipt. Intended later
scope: D046--D090 plus L007--L011 and L013; D001--D045 and L001--L006 remain
outside it.
