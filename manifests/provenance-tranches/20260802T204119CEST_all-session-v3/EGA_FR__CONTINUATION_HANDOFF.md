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

## Controlling exact admitted state — through printed p.77 / 7.7.8

This section supersedes every older continuation snapshot below; older
sections remain append-only history.

- Current production volume: EGA I.
- Admitted French source closes §7.7 through Proposition 7.7.8 and proof.
  `source/ega1/ega0-1-fr.tex`: 277,633 bytes / 5,878 lines / SHA-256
  `1D94EA4889F450CB70BAA4EFD2BB78779F843235064B6350C8941BF1261F5809`.
- Exact next cursor: §7.8 heading and paragraph 7.8.1 on printed p.77,
  continuing onto p.78. No §7.8 text is admitted.
- Direct authority manifest:
  `controls/EGA1_PRINTED75_77_SECTION77_DIRECT_AUTHORITY_IMAGES.json`, nine
  direct 5,000-dpi files / 4,998 bytes / SHA-256
  `6E728F658C5D14E9E36E7D4C069E1AA2F77E6B888CEB3C78C31F12CD2FD3C0E8`.
- Controlling bounded PDF: R62, 61 A4 pages / 407,900 bytes / SHA-256
  `9CB826D387B962B2B3F8305F0E2253AB41CBD1F410B5F2070D43E737AB434875`.
  Passes 2 and 3 are identical; hard diagnostics are zero; output pages 60--61
  pass personal 1,200-dpi layout inspection. The local 7.7.2 `sloppypar` is a
  typesetting-only overflow repair and changes no visible source content.
- Progress: 74 source-bearing pages out of 1,800 (4.1%); approximately 1,726
  physical pages remain.

## Controlling English correction/recheck state — through printed p.77

- The complete decision surface has 153 records. Thirty-two cumulative English
  repairs are applied; four justified no-edit decisions remain. No admitted
  correction has been reversed.
- P77 decision ledger: six rows / 9,404 bytes / SHA-256
  `41BF40298FAF27C1B5825A97E18FE2447890C18E682D5188EE7AF699F432413D`.
  P77 repair-event ledger: six rows / 6,517 bytes / SHA-256
  `C0B96FC24F1238951C1872FFE98D24E8CEDED30BB5DB1DC6197199D89000DC91`.
- Current changed source: `source/ega0/ega0-7.tex`, 75,620 bytes / 1,397 lines /
  SHA-256
  `29008BF15E3674F9B84BACDC8168B38E3C2B4B25497B153B2F96C744629749D8`.
- R10 source manifest: 24,749 bytes / SHA-256
  `D564A77B667290642B5206B29EC32FD667552D543642CE30F6ADF5D08DF325AE`;
  127/127 rows, 7,280,208 bytes, ordinal tree SHA-256
  `07BA24509DBA3162F680445DD535574044B3BB0E6E2BE03604EAFCA170CB71E7`.
- R10 diff validation: 6,716 bytes / SHA-256
  `C4EF8A240F3CEC321AA4437F4D810343E2F06B953F7A8736C99C39775FFD7444`.
  Replay: 3,628 bytes / SHA-256
  `B43869F4F6BC4B04D86E98AC5CE530BF8602360DC3EE70865033D420DFA52A61`.
  Both pass with errors empty; exact inverse reconstruction returns the R9
  source identity.
- The printed 7.7.6 duplicate `et un seul` is preserved in French and
  transparently normalized once in English under stable ID
  `EG-EGA-I-P76-776-DUPLICATE-ET-UN-SEUL-SRC-001`.
- Global build, reference-coordinate replay, privacy-clean projection,
  rights/package closure, dual-DOI logbook custody, archive handoff, and public
  readback remain held. No upload occurred.

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
2. Read the direct authority image personally. Before generating anything,
   search the existing Codex/Claude authority-image and QA holdings and reuse
   an existing exact page/crop whenever it represents the needed detail.
   Generate and inspect at most one new tightly relevant crop only when the
   required evidence is genuinely absent or insufficient. Use roughly
   1,100--1,400 dpi for ordinary context and increase resolution only for a
   genuinely ambiguous small feature; 5,000 dpi is not a default. Never
   batch-render or bulk-load authority images. Do not generate new OCR.
3. Preserve printed French typos diplomatically and catalogue their English
   disposition. Do not silently normalize the French source.
   At most two or three agents may be active, and only for genuinely disjoint,
   low-intensity grunt work such as provisional typing, locator preparation,
   small inventories, or mechanical hashes. Do not create agent swarms or
   duplicate ranges. Agents may not run bulk rendering, OCR, parallel builds,
   release-scale audits, or final mathematical/source-fidelity adjudication.
   The lead personally verifies and integrates every admitted result.
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

## Latest exact checkpoint — EGA I printed p.78 / complete §7.8 text

- French source: `source/ega1/ega0-1-fr.tex`, 282,088 bytes / 5,978 lines /
  SHA-256
  `359E04723FCCB70D8BB758184B85C4A6A467ACC549A7B5F7D40A0AE92FF053AC`.
  It ends with §7.8.3 and `(A suivre.)` on printed p.78.
- English source: `source/ega0/ega0-7.tex` in the English repair successor,
  75,637 bytes / 1,397 lines / SHA-256
  `96983D270206173230D51B70885CB846FD03BB1692D5DFAC03667EE7F4156252`.
- Four new decision records: SHA-256
  `FA9F3D79F64EB856EF919934E44F581D24641719B8ED0662FDB73D472AB23811`.
  Four repair-application records: SHA-256
  `BE5F779257515C1705A26FDBF623FE89714E7F0B747A0A6C70A384EBCE96739C`.
  Exact four-edit inverse replay: SHA-256
  `FEF06E5F4EBBF4A9F5FB4BB2B161471BAC4F127BB9699B397757C8F32605DDE5`,
  errors empty.
- This is a text checkpoint only. No §7.8 build or layout claim exists yet.
  The next cursor is the opening of the next bounded NUMDAM EGA I
  publication following printed p.78; freeze its exact PDF identity and first
  printed source unit before editing it.
- The task-history failure was caused by generating twenty very large
  5,000-dpi bands and loading them all at original detail. Do not repeat that
  workflow. All future work is sequential and RAM-light.

### Superseding R64 build identity

The portable current French source is 282,508 bytes / 5,978 lines / SHA-256
`5B6E27ADF94611E5B135E2316C1EEAB4B1EE5A067146E7C22DC7DE67C6138005`.
R64 PDF: 62 A4 pages / 413,424 bytes / SHA-256
`C13330C0BE44ED2750AD936DAE29E7B932818C9272FFAE96D6609C0A66E6DB36`.
Validation SHA-256:
`90C7FDBCA641A9712050C2D811FC7EA8528AB46F6B84E12EDF606B1B8AE156C8`,
errors empty. R63 is failed macro-portability history only.

English R11 is the current complete source manifest: 127 rows / 7,280,225
bytes / tree SHA-256
`D3FCAFB187DF2A812ABEB019BBE4AD50E7EB6D143CADF2C51EB357D256E95B13`;
manifest SHA-256
`BFF25F76B2DD8C58A895D7722F97EF711262757CCD42257AE59807A38F4C6F61`;
validation SHA-256
`F29FF0F856DFCDD9E0491398D0292769250F7C4CD312D555BE9E884A2CF2A12E`.

### Superseding cursor after Chapter I printed p.79

The next unit was not a new NUMDAM file: it is Chapter I within the same EGA-I
authority. Physical PDF p.78 / printed p.79 is now complete in
`source/ega1/chapter1-frontmatter-fr.tex`, 2,045 bytes / SHA-256
`DE7D2CC5ED4918280120E35DB2BF3C90CB53F08D22D5E9241E63B1C06D387EE5`.
Authority/cursor control SHA-256:
`4F4D0F994859EB7FAC0268190A721D36CA37178826F01D59E7FE64F0F6440A04`.
Bounded one-page PDF SHA-256:
`62072018461E2FB12F20D83980A7D1F033AE4F1A08664176C747F9336D194088`;
validation SHA-256
`E404FE4223BC22890DC5F005A70330490535EA433E35CBFE2B6C7C6A9C498C42`,
errors empty. The English chapter-opening comparison required no correction;
decision record SHA-256
`5D9E76F96C0008486BD0DD83A9D963885B09431C6C64595158F5C704BD4DEE59`.

Exact next cursor: physical PDF p.79 / printed p.80, §1, §1.1,
paragraph 1.1.1. Zero agents are active. Never exceed two or three disjoint
low-intensity grunt-work agents, and never assign them bulk images, OCR, builds,
audits, or final authority/mathematical/visual decisions.

### Superseding restart boundary after printed p.80

Printed p.80 is complete. French source identities are
`source/ega1/chapter1-frontmatter-fr.tex`, 2,057 bytes / SHA-256
`7B2D0F8F812EBA3121202F0AE6415FFC6C281B8428DA8F0F72D89DF1CEC01708`,
and `source/ega1/ega1-1-fr.tex`, 3,639 bytes / SHA-256
`1CECBFC4D2CD0D595D46B7588721C334D06050DC97B40BAAE96FFD05E4218A23`.
The two-page bounded PDF is 46,494 bytes / SHA-256
`6F238B0D3F015C1F8791435494FEED7FC17CC0571D7401D5973C36FBC09EDF37`.

English p.80 has two accepted changes and one rejected-before-mutation
candidate. Current `source/ega1/ega1-1.tex` is 78,900 bytes / SHA-256
`7F3A34C3E03F3497A4BD406E9E7A48ED6EDC72CCDA99768DD516EEF948202C64`.
The rejected candidate records that the lead initially misread a small
Fraktur `j` as possible `p`; the one necessary tight 5,000-dpi crop proves `j`
and no notation edit was made. Decision ledger SHA-256
`363742C913D367889348FD4D554B6F53B22AC1ECE859BD9FDD8F83F4F9747A3E`;
exact inverse validation SHA-256
`01CC60CDDA76790566C19EFE18399426CA9CF883765745CDA0DE89161A659D0F`.

Complete English source manifest R12 is 127 rows / 7,280,223 bytes / tree
SHA-256
`5410571C0C44F559B1474FFFACE408BE3137F71D418FD09F22B70B798A601191`;
manifest SHA-256
`491EC4E6FD5410C54986400B0CE1B975E502481537E846521CC24B7A20AA15ED`;
diff validation SHA-256
`3102F963D936C1A15641FF49F9CEF4D61810B8CEE1FFD259A170816A8703447D`.
Checkpoint validation R3 SHA-256
`919E4AA8D21E17CDA058D20468F20E688696CAC1B3915AA2F59BD61D702E9A61`.

Restart at physical PDF p.80 / printed p.81 / paragraph 1.1.3. Search and reuse
existing page/crop evidence first. Generate at most one image for a concrete
missing detail; use ordinary resolution for context and higher resolution only
for a small ambiguity. No OCR, batch rendering, parallel build, or agent final
judgment. The forthcoming exact restart record is
`controls/CONTINUATION_STATE_20260802_P80_R5.json`.

### Superseding restart boundary after printed p.81

French `source/ega1/ega1-1-fr.tex` is 7,710 bytes / 206 lines / SHA-256
`1A3C8979F95B51594029DE4D2C3EDB3C18B3331DF38F0DEAB2F65D9ED6F101C6`
and ends at paragraph 1.1.9 on printed p.81. The 3-page bounded PDF is 54,293
bytes / SHA-256
`5C9C3AE13B9A7B14E95D04848FCB0826B50E083865E98E0B98D5BD45B8849BEC`.
Checkpoint validation R4 SHA-256
`D71C9D2A525AE7DD280BF28559573D727DE3E21FBA5C86D2A7DE0B2313B6FD92`.

English current source SHA-256:
`8413A5B1710F1B932A4F69D8F7E8D501FCE909B0EE9BAC46809F4A3DEE20E221`.
P.81 decision ledger SHA-256:
`51830FA1B2D263DDBDE91380EA04B6C6028D2A6711344A6E8038AAF8A05360D6`.
R13 complete manifest SHA-256:
`CC593E9C9D01D8053CF7757DAB745197E9481FF9308DA0C3D2623F25AD7406DF`;
tree SHA-256
`C73A0D59938FB18E3B9DEC6BB9E1C4BC8033360DA5C1B4F0BD948A9FCED76430`;
diff validation SHA-256
`DA38B1A6554799334D70C5C9EEFB7CF4C9615BC8041CBDBEFAEE289E8FA13030`.

The initial selector mistake produced printed p.82 and caused no transcription
or source mutation. Reuse it exactly at
`qa/authority_reuse/ega1_chapter1_opening/EGAI_physical081_printed082_context_1400dpi.png`,
SHA-256
`212A6AC00972E745CF7F7C4C33D6302B050BCFAA2B0D920B738AA982E104C1DA`.
Do not render another p.82 context page. Restart at Proposition 1.1.10. The
forthcoming exact restart record is
`controls/CONTINUATION_STATE_20260802_P81_R6.json`.

### Superseding restart boundary after printed p.82

Current French `source/ega1/ega1-1-fr.tex`: 11,938 bytes / 297 lines /
SHA-256
`8CFF1ED1AF6AD16875A0EB87E1C9C4DA453799BC2FD29A1AE80BEFEEE90AB4F2`.
It stops exactly at the p.82 seam after `un point générique` in the proof of
Corollary 1.1.14. Final bounded PDF SHA-256
`CBD2C0707C64BA7D38EC3EBC00422A64955B8D4013DDD96D566D48A0EE0D1E3D`;
validation R5 SHA-256
`066BA00C2B441021C925BF8A580E73CA5E1852D41EA7CF5EBA2588275A762C53`.

English current source SHA-256:
`B01302DA521F1FE09DBDE748CE5BF50199BD3C8CE6CA0BA21003B27161C65A14`.
Decision ledger SHA-256:
`71711DFF7E0D5C21C8F32EF5A159585B22F61D574C20BBAAA91B4CB634719421`.
R14 manifest SHA-256
`27038C5278D96F411B98E72780432BC2663B4923587FECED104ADC9AEE88CE59` /
tree SHA-256
`01613437EE956CADF50FE90C8C18CE8E73F2F731E3D1C94398C1410D12175A3D` /
diff validation SHA-256
`2E42656AE40BE12F5EEA3DB21A41602A6B1C4D1C5DE798DA83B990D1AB0BE509`.

Restart at physical PDF p.82 / printed p.83. Search/reuse existing p.83
evidence before rendering. Forthcoming exact restart record:
`controls/CONTINUATION_STATE_20260802_P82_R7.json`.

### Superseding restart boundary after printed p.83

Current French `source/ega1/ega1-1-fr.tex`: 16,053 bytes / 403 lines /
SHA-256
`5EF98CFE63E6F1A87283D59EA419FC069D475F896510409FB99EEE8129384CD7`.
It closes printed p.83 through Corollary 1.2.3 and the functoriality remark.
Bounded PDF: 4 pages / 68,147 bytes / SHA-256
`747BD13DB1201010DB9E89BCB40E7412C915B4ED78491287E84C2B0BFD9BFE8E`.
Validation R6 SHA-256:
`17D33B17D4D56F85879208360879B0AA997A831A59EF77CB778DA27A631BD872`.

Current English `source/ega1/ega1-1.tex`: 78,962 bytes / SHA-256
`1A203AD96C8C8AEF46C5884492B50CAD3E69590CA154ADBA58C4609AEB2A2C1E`.
P.83 decision ledger SHA-256:
`D2CE7E4C7FAC883AB1F68902655472B0559C4B40ED7A9C7EC95471A8DF36E9A7`.
R15 manifest SHA-256
`E9A16CF44BB22B03540A64BDA62F21013D7030DA0B170EC7B66A335A15588108` /
tree SHA-256
`B62B297758730E9DB6D10818DFD815A6BD9F7CE2BD418DECE13D6DA662D4CF0B` /
diff validation SHA-256
`05B18115426FBB140190E05B1AB7833852F3EAEBF3EDDC5A4A88909EC970DEEE`.

Restart at physical PDF p.83 / printed p.84, Corollary 1.2.4. Reuse any exact
p.84 image already on disk before rendering. Forthcoming exact restart record:
`controls/CONTINUATION_STATE_20260802_P83_R8.json`.

### Superseding restart boundary after printed p.84

Current French `source/ega1/ega1-1-fr.tex`: 20,132 bytes / 508 lines /
SHA-256
`02C040DC7CB2DA53E4E6F2EE710BCAF37E99CA70AFC6960A1BAEF5FADC775E5B`.
It stops exactly after Equation 1.3.3.1 at the printed p.84 boundary. The
source's wrong 1.1.12 cross-reference and unprimed X/A/A cluster are preserved
diplomatically and separately adjudicated for English. Bounded PDF SHA-256
`527FDC5FDFDF86463F8F27384F183FD697926C086984F0EC9240015C90AE7F01`;
validation R7 SHA-256
`FBFA113F4CED15ABB0694A7329A6EFB0A8795E42A971D1F94BFBA42C6783572B`.

English source remains 78,962 bytes / SHA-256
`1A203AD96C8C8AEF46C5884492B50CAD3E69590CA154ADBA58C4609AEB2A2C1E`.
P.84 decision ledger SHA-256
`67464F6931246807CB6478BBA49E9384E53ECC2399F0100241B14F49D605D20F`;
no-mutation validation SHA-256
`615D7EAABBF75650F9EAFF26D8DD64475CD1615450D31ECCBD6DCC668A6B0C9F`.
R15 manifest/tree identities remain current and unchanged.

Restart at physical PDF p.84 / printed p.85, continuing 1.3.3 after Equation
1.3.3.1. Search/reuse exact p.85 evidence before rendering. Forthcoming exact
restart record: `controls/CONTINUATION_STATE_20260802_P84_R9.json`.

### Superseding restart boundary after printed p.85

Current French `source/ega1/ega1-1-fr.tex`: 23,758 bytes / 589 lines /
SHA-256
`D48927FDFB91B3A898965E5259B2C72B8BFB317FC60D716266104A7BD465BAA0`.
It stops exactly after the proof of Proposition 1.3.5. Bounded PDF SHA-256
`7BE67411894028C10EE670652D8EC183866F51F9EC98C9FC31D3B2121829BD39`;
validation R8 SHA-256
`5911A199F6EC01D4682B6913009B2E70731F9659E5B57F2EAD4EA592B13B8BF8`.

English `ega1-1.tex` is 78,962 bytes / SHA-256
`87F31A92CE21021768DB10B4C1F39A51992CF9949C61205E599CBD03E2E276AC`.
P.85 decision ledger SHA-256
`5A6AEAE4C1E6445364608FB234174915345D2B54E20E7C62A7BCA66860E8537D`;
R16 manifest/tree SHA-256 values are respectively
`39D7F529579466028B44E6E6BED9CDB547B4BDC2E4EDCD85783FCF1F8D9B7A34`
and `64C5266D3BB6553B6D3B1BBC42DF136042F6A5F83AFF0262CE22DF9500E35C30`.

Restart at physical PDF p.85 / printed p.86, continuing after Proposition
1.3.5. Reuse exact p.86 evidence before generating anything. The controlling
resource rule is `controls/SEQUENTIAL_RAM_LIGHT_REUSE_FIRST_WORK_RULE_20260802.md`
(SHA-256
`99526B90F942BC00325F2A72E4C597CE886D433E4491D0FBC7950BCDBDA38B5E`).
Forthcoming exact restart record:
`controls/CONTINUATION_STATE_20260802_P85_R10.json`.

## Superseding restart surface — printed p.86 complete

Printed p.86 is admitted through Equation 1.3.7.2 and the words `On en
conclut`. French source: `source/ega1/ega1-1-fr.tex`, 27,527 bytes / 664 lines /
SHA-256
`9189ABAEC2E1599F3F03D34D8687312EA1F59A9B994A81CBCDDEB43546CDEB20`.
Checkpoint: `controls/EGA1_CHAPTER1_P86_VALIDATION_R9.json`, 8,297 bytes /
SHA-256
`3B5598B9D9CB608D84DB54E9F70E6D1572157E62E46B66F2694E2DAF0E7A20AA`,
PASS/errors empty. Correct authority is PDF one-based p.85 / printed p.86,
image SHA-256
`B7BEC3BAC68ACB643C558229D88E4B17F8AB3F2AF3A9DC0BF76B145516DE8B42`.

English R17 source is 78,953 bytes / SHA-256
`26747DCB22FCB736BBD1D025015C81E268F08CE42EB14D98518E4F21EA70DD99`;
manifest/tree SHA-256 values are
`63BA95B4C3C9B2E7C50C5878A523D7C5D032ABBB84C5D2B09AB967E904E78674`
and `CE854184377B48F388C46D5D4808E0A23A2E168F23909714C7E6F9C10B880DF8`.
The three applied p.86 decisions and all lead-error rationales are in ledger
SHA-256
`47ADE114A1A2161E71166C2BAD84C0E2EAEB06469B1703440524A06A46B456E7`.

Restart at PDF one-based p.86 / printed p.87, continuing the proof of Theorem
1.3.7 after `On en conclut`. Reuse the existing image whose current filename
ends `printed086_context_1400dpi.png` but whose visible folio is 87 and whose
SHA-256 is
`3E861071076111EEBB9572225C6EEDBEBB3664DE47E2FEB09C605071793E9AC3`;
do not generate a replacement merely to improve its filename. The hard agent
cap remains two or three low-intensity grunt workers; zero are active.
Forthcoming exact restart record:
`controls/CONTINUATION_STATE_20260802_P86_R11.json`.

## Superseding restart surface — printed p.87 complete

Printed p.87 is admitted through the proof of Corollary 1.3.9(ii), ending
with `$v_x$ est l'identité`. French source: `source/ega1/ega1-1-fr.tex`,
31,549 bytes / 755 lines / SHA-256
`389A015AA2E5D3C595939B9B8396320810F6A25C73128C4E6EC47F8A7F86E9D8`.
Checkpoint: `controls/EGA1_CHAPTER1_P87_VALIDATION_R10.json`, 8,101 bytes /
SHA-256
`2E036C9C4E5240A10EB4299312E3FD98AEE87429FBF871730FC119E7EA5469BE`,
PASS/errors empty. The reused authority image's stale filename is preserved,
but its true locator is PDF one-based p.86 / printed p.87 and its SHA-256 is
`3E861071076111EEBB9572225C6EEDBEBB3664DE47E2FEB09C605071793E9AC3`.

English R18 source is 78,953 bytes / SHA-256
`8C3145A4A41947759A191809C582163EF9FB590FBE9DC92211D719F205877D49`;
manifest/tree SHA-256 values are
`2355C8043243D22BFA826AE8664D8A3563DA28C60CCB81BD35DD28ABF1D64BCE`
and `D2A7BC6831E8F15D10CCE2C52C0D6907937D32DFA2EC5C4BC3779B7936AAC465`.
The exact p.87 diagram-label decision is in ledger SHA-256
`B4BC74E1FADA4448F35488502A81EFFA0C883572581F25A3BDEFDA0483E4AB32`.

Restart at PDF one-based p.87 / printed p.88, beginning `Enfin, si M est la
somme directe...`. Search for reusable p.88 authority evidence before any new
render. If none exists, generate only one page at ordinary context resolution;
crop further only for a real ambiguity. Zero agents are active and the hard
cap remains two or three low-intensity grunt workers. Forthcoming exact
restart record: `controls/CONTINUATION_STATE_20260802_P87_R12.json`.

## Superseding restart surface — printed p.88 complete

Printed p.88 is admitted through the first canonical-isomorphism display in
Corollary 1.3.12(i). French source: `source/ega1/ega1-1-fr.tex`, 35,477 bytes /
844 lines / SHA-256
`BF5E28152E1AEE70E34819CF64A9A2CC95A2B88DAC536D8B58421D5859C91A03`.
Checkpoint: `controls/EGA1_CHAPTER1_P88_VALIDATION_R11.json`, 6,384 bytes /
SHA-256
`3C9CC554D618C44E72EE0FEEBBAB828DEB0245F24B0C2BF83A87CBE69940C132`,
PASS/errors empty. Authority page SHA-256:
`A0269AB9268BF48B6C3B10923F9C31737F56EA9376C6A64567E988C07DA6E67F`.

English source remains R18, 78,953 bytes / SHA-256
`8C3145A4A41947759A191809C582163EF9FB590FBE9DC92211D719F205877D49`.
Three retained p.88 normalizations are logged under SHA-256
`39E247CAA4BA6F67384FB4EB535D49D2B0ADB6DAC73A3975642F310D8678DE76`;
no-mutation validation SHA-256 is
`C6FF77518A41AD662643CD1F39EF4880FB311B9C88B9FD310A7A93EC76F9960D`.

Restart at PDF one-based p.88 / printed p.89, continuing Corollary 1.3.12(i)
after the displayed isomorphism. Search for reusable evidence before rendering;
otherwise generate one ordinary-context page only. Zero agents are active;
hard cap two or three low-intensity grunt workers. Forthcoming exact restart
record: `controls/CONTINUATION_STATE_20260802_P88_R13.json`.

## Superseding restart surface — printed p.89 complete

Printed p.89 is admitted through the finite-type statement in 1.3.13.
French source: `source/ega1/ega1-1-fr.tex`, 39,112 bytes / 930 lines /
SHA-256
`F670F2FD67371DF61A7E41A994AC94376B835158DC6EF50B7A6765D8C346F688`.
Checkpoint: `controls/EGA1_CHAPTER1_P89_VALIDATION_R12.json`, 7,365 bytes /
SHA-256
`C674208138DB0C5528C4B842D006FDF141C6C553E04F220859F7FAC68F9D180A`,
PASS/errors empty. Authority page SHA-256:
`9F357BAF256A9D27FE9E0B1647AEB08DF134D84F990F1195D57FE21669A96179`.

English R19 source is 78,948 bytes / SHA-256
`755474860ACB423698A25393EB56CE06396F321131B7EACBBF2624478089BDC5`.
Three applied p.89 decisions are logged under SHA-256
`38712B6F457B308FD650DDD19537321207EF7D256BDCD2622535EF1BC90D99C9`.
Manifest/tree SHA-256 values are
`8A2618EE6EB0A895A6DE54B83A30F165D901504410CCB89177047325DAA59F80`
and `FD8D86B665DACA629F4FE1ED320D15EF2BFA25A751B8527905C85457C78998C7`.

Restart at PDF one-based p.89 / printed p.90, beginning `Si M, N sont des
B-modules...`. Search existing evidence before rendering; otherwise generate
one ordinary-context page only and crop solely for a real ambiguity. Zero
agents are active; hard cap two or three low-intensity grunt workers.
Forthcoming exact restart record:
`controls/CONTINUATION_STATE_20260802_P89_R14.json`.

## Superseding restart surface — printed p.90 complete

Printed p.90 is admitted through the proof that c) implies b) in Theorem
1.4.1. French source: `source/ega1/ega1-1-fr.tex`, 43,364 bytes / 1,010 lines /
SHA-256
`209E5EF26239495DC1B1540FF7EB06E9E57122770D66EC37401FCA413DFE56E9`.
Checkpoint R13: 7,030 bytes / SHA-256
`0DCD4476C7F3170509395EAD0A9B983810A19725AC185A3D188A248FE316DF39`,
PASS/errors empty.

English remains R19, SHA-256
`755474860ACB423698A25393EB56CE06396F321131B7EACBBF2624478089BDC5`.
The five-row decision ledger SHA-256 is
`A5C0174B7820E383F6FA9B55FFC3D0E2C066C0B4C20CC5FBCE2D29E4DABE66C6`.
The direct crop proving the printed misplaced-tilde phrase is SHA-256
`C1D0FC9811194B519FBDFF385CD637AAAD3FE2FC33545A6978C5E671CED4C33D`.

Restart at PDF one-based p.90 / printed p.91, beginning `Pour démontrer que
b) entraîne d 1) et d 2)...`. Reuse evidence first; otherwise generate one
ordinary-context page and only a genuinely needed crop. Zero agents are
active. Forthcoming restart record:
`controls/CONTINUATION_STATE_20260802_P90_R15.json`.

## Superseding restart surface — printed p.91 complete

Printed p.91 is admitted through the terminal fragment `g^m t se` in the
proof of Theorem 1.4.1. French source:
`source/ega1/ega1-1-fr.tex`, 47,381 bytes / 1,080 lines / SHA-256
`9F7FE068AB53F83ADF9CF58C3692D0CACCF2A3571A26C07F3AB9C164656E2ABE`.
Checkpoint R14: 7,885 bytes / SHA-256
`E48DC2814D020CA3C9EA06719BE864354A2276D533C6505DC5BDD978A11266C1`,
PASS/errors empty. Authority page SHA-256:
`B9AA4889898ED3D09E542ED7C34D59BFBA7F4611B4F419FC5AA4E7BD02C4D83F`.

English is R20, 78,945 bytes / SHA-256
`776A8D8FB7B5ACA95CC45F939C8BF11E5CF45B00709BC281F9FFB007C58A86A9`.
The six-row decision ledger SHA-256 is
`4ADAD1B6997F3B699E36BF7F95E33D6F0FA68D7483FB5D1406C73EB190612510`;
manifest/tree SHA-256 values are
`864B73E7553E086F64D7AD32B4DD8494823505E3956A28DBED39EFBB8EA990D5`
and `1C39A53AA1AFE22E39606C93EADB7FBE6C0D0705AE43C35C9D6DBD345DDFE5AD`.

Restart at PDF one-based p.91 / printed p.92, continuing after `g^m t se`.
Search for reusable p.92 evidence first; if absent, generate one ordinary
context page only and crop solely for a real ambiguity. Zero agents are active;
hard cap two or three low-intensity grunt workers. Forthcoming restart record:
`controls/CONTINUATION_STATE_20260802_P91_R16.json`.

## Superseding restart surface — printed p.92 complete

Printed p.92 is admitted through the statement of Theorem 1.5.1. French
source: `source/ega1/ega1-1-fr.tex`, 51,644 bytes / 1,164 lines / SHA-256
`B5E58A9430A49E9A19C0B792A1B4F41549A5092AFB8000BA8CE023C1AC4D264B`.
Checkpoint R15: 8,540 bytes / SHA-256
`051E8D04A57A6094FA52E94B1061E774331FB691A3FD62B95125C29A1E0EFD7C`,
PASS/errors empty. Authority page SHA-256:
`57FCD19DD19BCF8D20CC7AC5F64F7981D794DF3854DB4EAEE27B3538574DCD85`.

English is R21, 78,943 bytes / SHA-256
`E79237CB465C8F0EF7C3FE573F568C4FCD122DC5D618463C46B914DE218459F9`.
The nine-row decision ledger SHA-256 is
`A12D4F80F39AD47269CA79400EBE3B8CCF5DE8C11FE5D21BE85B665A45722A89`;
manifest/tree SHA-256 values are
`DA77D11422EEB0CD94709729824171B1D9B33A1C7B71E5BBE68C9CAF9679717A`
and `870E97EB71F44AA795F47332B655738011DB772C226899E1FFDE66A3741A4B82`.

Restart at PDF one-based p.92 / printed p.93, proof of Theorem 1.5.1. Search
for reusable p.93 evidence first; otherwise generate one ordinary-context page
and only a genuinely needed crop. Zero agents are active. Forthcoming restart
record: `controls/CONTINUATION_STATE_20260802_P92_R17.json`.

## Superseding restart surface — printed p.93 complete

Printed p.93 is admitted through the terminal displayed ring homomorphism in
paragraph 1.6.1. French source: `source/ega1/ega1-1-fr.tex`, 55,165 bytes /
1,253 lines / SHA-256
`94FAA233686C9C44B8B492C7F772DAB3CC70D2F8BC0B5DCB047ECB758B2BC4ED`.
Checkpoint R16: 8,061 bytes / SHA-256
`6637A091AE9F1BEFC60E1E0365E3422DF2DBFBD2ED901DC079322861F23A90F0`,
PASS/errors empty. Authority page SHA-256:
`274B90A70A72E0812131425C82664C9F47D82F66C1E1A821B574AA67C183C8F0`.

English is R22, 78,920 bytes / SHA-256
`08B58F1484E0195D637512C27528BF77F665DCE03D1B3C4F29A7FC685A956E5E`.
The nine-row decision ledger SHA-256 is
`211B3C3A460DB008F6E01ECE0D6444448053525A42A816B86069515D7F63D54E`;
manifest/tree SHA-256 values are
`4B2C325B73D8DCF3027A5A6BE0FEB651AD6477200E71E33916E91399CD9262F8`
and `4B01E8D9D30053F942E2570915BB92365BC754DA5A95ABA6C0AB8BA2DF9329B3`.

Restart at PDF one-based p.93 / printed p.94, continuing paragraph 1.6.1
with `En outre, ces homomorphismes satisfont...`. Search for reusable p.94
evidence first; otherwise generate one ordinary-context page and only a
genuinely needed crop. Zero agents are active; hard cap two or three
low-intensity grunt workers. Current restart record:
`controls/CONTINUATION_STATE_20260802_P93_R18.json`.
