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
`03_projects/language_management/english_germanic/03_working_translations/EGA_English_Global_0_IV_complete_linked_reader_20260801_r1`.
Do not rebuild it merely to advance the French cursor. Current source-backed
English repairs accumulate in the separate no-overwrite successor
`EGA_English_Global_0_IV_french_recheck_source_successor_20260802_r1`.

## Authority closure

`controls/AUTHORITY_SHA256.csv` binds the eight NUMDAM PDFs: EGA I, EGA II,
EGA III-1, EGA III-2, and EGA IV-1 through IV-4. They total 1,800 physical PDF
pages. OCR and extracted text are locator/drafting material only; the direct
PDF image decides.

Current EGA I authority:

- `[PRIVATE_DOCUMENTS_ROOT]/Papors/OS/NUMDAM/EGA_I_PMIHES_1960_4.pdf`
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

## Superseding restart surface — printed p.94 complete

Printed p.94 is admitted through the exact incomplete seam after
`l'isomorphisme`. French source: `source/ega1/ega1-1-fr.tex`, 58,853 bytes /
1,336 lines / SHA-256
`E0F4EA3D4AC371A160550ADE7BA8B04A3EC42D6E633DB53CBA834F3CBCDE35C6`.
Checkpoint R17: 9,196 bytes / SHA-256
`87CAAA52DFC8971F4B0374D8040A7F5E67BE4A01974904A954F84F8D00610EB1`,
PASS/errors empty. Authority page SHA-256:
`0C60C72AEB9B5A918792EDDC8FCEF6C3D5E402E9602E0F07115965069B7E840C`.

English is R23, 78,882 bytes / SHA-256
`3839AC1B392AA3B7629B06909D1DAC19AF652963B01D556D1889B1C9ECAB8414`.
The eight-row decision ledger SHA-256 is
`DCCDA3F1B7B9DB60D19903ED0EE20E24B4E88A369FE2D63EA206E5B78EAF32C7`;
manifest/tree SHA-256 values are
`3D744079A8F05F4526BD2446B6636D487D2D258B93722F1861D810BF6408D06A`
and `BB9926BFC40EB87CF106CDDACDDB834F99FF4B78CE99E0C3C3F8F32D638B5419`.

Restart at PDF one-based p.94 / printed p.95, continuing the canonical
functorial isomorphism. Search for reusable p.95 evidence first; otherwise
generate one ordinary-context page and only a genuinely needed detail crop.
Zero agents are active; hard cap two or three low-intensity grunt workers.
Current restart record:
`controls/CONTINUATION_STATE_20260802_P94_R19.json`.

## Superseding restart surface — printed p.95 complete

Printed p.95 is admitted through the terminal comma after the homomorphism
`j` in paragraph 1.6.7. French source: `source/ega1/ega1-1-fr.tex`, 63,197
bytes / 1,432 lines / SHA-256
`B8C18DA8E3661EADD85EAE0FBC8A99779A1CD59285855FF2FCF5C54981265238`.
Checkpoint R18: 9,167 bytes / SHA-256
`7AC4DC5BDC566DF19569AF0EFCD14E1429C6A3A61A042B32895AD1A19AF3CC41`,
PASS/errors empty. Authority page SHA-256:
`A399A19C67962146373AFDAC1A2083E95070510651412DFD79CCE461310E95FC`.

English is R24, 78,891 bytes / SHA-256
`3C1A38B22A9A07315A8CFA2E8F3AC1B65232E0CFCE3F9F8E2E09A30464018617`.
The fourteen-row decision ledger SHA-256 is
`905745E09BAC102CE4B799081490DB9647AE28D5BE0AE3707D6BECFB4C85BD8D`;
manifest/tree SHA-256 values are
`EBA2F1067D485CCD4861EAFEC7F1239C55CA5858E1734714FA91667805E37E3E`
and `099CD37D1BD2E8380DF875A90C61895F7B7BFF743573A4CF5452B22D3AEE5A56`.
The material English correction is the source-exact stalk input
(s'_{x'}) in the formula for (h_x).

Restart at PDF one-based p.95 / printed p.96, continuing paragraph 1.6.7.
Search for reusable p.96 evidence first; otherwise generate one
ordinary-context page and only a genuinely needed detail crop. Zero agents
are active; hard cap two or three low-intensity grunt workers. Current
restart record: `controls/CONTINUATION_STATE_20260802_P95_R20.json`.

## Latest exact continuation — printed p.96 closed

French EGA I Chapter I is now diplomatic through the complete statement of
Theorem 1.7.3 on printed p.96. Current source is 68,010 bytes / 1,548 lines /
SHA-256
`9EAF6027F10D1EC54DC1779FC4C83785950447EE4E9DC8C5A1B3F2454EB672F2`.
Checkpoint R19 is 7,085 bytes / SHA-256
`39B3AEC1B4BEF0DA99558F20D0CEF0AA030115F84C1AD024152F8A86122E4E72`,
PASS/errors empty. Authority image SHA-256:
`D95EA237831E67C943B0A7F03E805D41E7CE6218D6D7F5250B03C261CBECA6BC`.

English is R25, 78,908 bytes / SHA-256
`758885F9505A72DF1A5A2EF8B116D998A41D0505571AD8E7028C438EE5795C6E`.
No mathematical correction or lead-error reversal was found on p.96. The two
applied changes are the exact combined Chapter 0 citation grouping plus a
source-faithful no-confusion phrase. Decision ledger SHA-256:
`69FEE7A8EE3B705A6ABE2F53A66B72969CBFD7B110C4BF9DB89386A3B045842C`;
manifest/tree SHA-256 values:
`516696896ADBB097947CC00005B37C890C505AE9DB1D5B17EC688E0F8E7A475B`
and `8D3BF2A908E654E4B94AC1FFE2BEF606BF4EE92FDCEB400AAC02B737E1D51E4E`.

Restart at PDF one-based p.96 / printed p.97, beginning the proof of Theorem
1.7.3. Search existing evidence first; create no source image unless current
evidence is genuinely insufficient. Zero agents are active; hard cap two or
three low-intensity grunt workers, with no agent source/mathematical judgment,
render/OCR/build swarm, or duplicated range. Current restart record will be
`controls/CONTINUATION_STATE_20260802_P96_R21.json`.

## Latest exact continuation — printed p.97 closed

French EGA I is now diplomatic through Corollary 1.7.5 and its proof, then
through Definition 2.1.2 at the beginning of §2. Current source identities:
`source/ega1/ega1-1-fr.tex`, 71,381 bytes / SHA-256
`D201398091BCC065BE7B5EFC610183E1E2071E01BC8E35C0CE1441DF3E579393`;
`source/ega1/ega1-2-fr.tex`, 607 bytes / SHA-256
`48DF1C2DA45FFC15BED36D50E53AE21B9819B64758A3ACE3D0A7B306FC4F282B`.
The theorem-proof square is native TeX under stable target
`I.1.7.3.diagram-fr`; no raster is active. Checkpoint R20 is 7,273 bytes /
SHA-256
`BF4FD925BA25D4F5572F6B5186BF608A834A0B036BA95717DE74BDD63A275B78`,
PASS/errors empty. Authority image SHA-256:
`F3033D317BF871AF491AE5E472DE64ECDF86D0ECDA79F9007800B7C977FB9AB0`.

English is R26, 78,906 bytes / SHA-256
`EB62DDA7A40E93BFF26BEF9513693192A7C46540E08D244C18218F9BAAEF4FFA`.
The two changes are prose fidelity only: singular hypothesis agreement and
`equivalently` for `c'est-à-dire`. Mathematical repairs, lead errors, and
reversals are all zero. Decision-ledger SHA-256:
`0CA4E32D47D13CBABB1993F7B3F8498A1B9F6152F6EEF28EC7A280811740E06A`;
manifest/tree SHA-256 values:
`A28F89369E461D3B434C5F66F51299B462AB9CE4F457ACA952B94551CDBE4147`
and `F6706D38DCA72AE5A01C4999F52056424809462990F8136C8042D6DE4108210E`.

Restart at PDF one-based p.97 / printed p.98, Proposition 2.1.3. Search for
existing authority evidence first; create at most one right-sized image only
if absent, with a tight higher-resolution crop solely for genuine ambiguity.
Zero agents are active; never exceed three low-intensity bounded grunt agents,
and never delegate source, mathematics, translation, diagram, or visual
judgment. Current restart record will be
`controls/CONTINUATION_STATE_20260802_P97_R22.json`.

## Latest exact continuation — printed p.98 closed

French EGA I is diplomatic through complete Definition 2.2.1. Current
`source/ega1/ega1-2-fr.tex`: 4,664 bytes / 114 lines / SHA-256
`9C52B942A2B935B4201B021491D30EAD82748622FD4696D8909A6D5BEC16CC2B`.
The source's apparent `generic point of X` typo in 2.1.5 is preserved; English
uses contextual $Y$ with a visible note. The first compile exposed and
fail-closed one lead structure error—four non-authorial proof wrappers—which
were removed before the admitted r2 build. Checkpoint R21: 8,005 bytes /
SHA-256
`F8E4DEBF91B6A76F697893324F32EA5E1A1678623B3845E34061F10D88C78D34`,
PASS/errors empty. Authority image SHA-256:
`0B21F79E1BD1E8CDBDB62B647C7B5F01A787AA0D8CD5A7A362AC069E68CD98D4`.

English R27 changed only `source/ega1/ega1-2.tex`, now 25,214 bytes / SHA-256
`9239F37777A793E4A03AFEDCD0479AD55C7D90EC6A92886B20E20F80A031BA18`.
Two prose cleanups were applied; new mathematical repairs zero, retained
disclosed source-typo repairs one, English lead errors zero, reversals zero.
Manifest/tree SHA-256 values are
`1EBEC66D050557D5F20B1EF42B1CF8F3A7717D59ACD2CFDB3384604E0DDD5419`
and `07D146DDD043D20E0D30F09612E645F86A14000E974FE9C44703B6B0D35E239A`.

Restart at PDF one-based p.98 / printed p.99, paragraph 2.2.2. Search for an
existing authority image first; create at most one right-sized image only if
absent, escalating to a tight detail crop solely for genuine ambiguity. Zero
agents are active; cap three low-intensity grunt workers and never delegate
source, mathematical, translation, diagram, or visual judgment. Current
restart record will be `controls/CONTINUATION_STATE_20260802_P98_R23.json`.

## Latest exact continuation — printed p.99 closed

French EGA I is diplomatic through printed p.99. Current
`source/ega1/ega1-2-fr.tex`: 9,213 bytes / 206 lines / SHA-256
`80084D747F88429A8770AC0918B7B07ED8631D1FACCC6619661BCD95EA157A33`.
It stops exactly inside Proposition 2.2.5 after `Il existe alors une`; do not
insert a source-level closing environment before continuing p.100. The
authority image was reused, not regenerated: SHA-256
`446A4BFC0958E1210B5BD21E0F3753A15944D73AF676C1E621AD1522ED784BE1`.
No source correction, diagram, or raster occurs. French decision ledger
SHA-256: `99A0E92FA8B8B4A2CF917CFBB0DD287D1785E360DD827CD33D52CFF99E119DD7`.

English R28 changes only four reversible prose/register phrases. Current
`source/ega1/ega1-2.tex`: 25,214 bytes / SHA-256
`C2C52F7F7543ABEC2A082C294123434E07FFA64E57181A879C033850C8E7DCBC`.
New mathematical repairs, source corrections, lead errors, and reversals are
all zero. Manifest/tree SHA-256 values are
`6E3AE6380AA300004627DEF42A1ECFEFEC6326C8887C525A9930A50623CF5B3C`
and `4C32D118D81AC1B2E89A5AEC33FD0C355B98DD2D509235A64C7A01D274280D01`.

The admitted bounded reader is 15 pages / 168,076 bytes / SHA-256
`2DAE67334A752773F5DA94D0F838B67BF764E8B3BF9A9D6DAD9196D3C7CEB34D`.
Its one small overfull warning is wrapper-only and visually benign on the two
affected seam pages. Checkpoint R22 is 7,709 bytes / SHA-256
`7BA41019FEE8362A644B856E7389E89087AE86911C7528F04D86104A6C8F5532`,
PASS/errors empty.

Restart at PDF one-based p.99 / printed p.100, continuing Proposition 2.2.5
after `Il existe alors une`. Reuse any existing image/crop first. If none
exists, create only one right-sized authority image needed for the immediate
page; use a tight higher-resolution crop only for a real ambiguity. Do not
batch render, load images in parallel, or rerun OCR. Zero agents are active;
at most three low-intensity mechanical workers may ever run, never for source,
mathematical, translation, diagram, or visual judgment. The next restart
record is `controls/CONTINUATION_STATE_20260802_P99_R24.json`.

## Latest exact continuation — printed p.100 closed

French EGA I is diplomatic through Convention de notations 2.2.10. Current
`source/ega1/ega1-2-fr.tex`: 13,093 bytes / 296 lines / SHA-256
`847E41008F84D6C74DAD4BEE3CA0C6DB2D9155BFE1947B7529D14EFF894C09E4`.
No source correction, ambiguity, diagram, or raster occurs. Authority image:
6,427,556 bytes / SHA-256
`33F148CC42DCFD369BBE82C64EFA714084E8950CE8A1C31036CF583A493798BB`;
it was the sole new authority image after reuse search, and no crop/OCR ran.

English R29 changes only the missing `is` in 2.2.7(ii) and source-register
`Assertions`; current source is 25,221 bytes / SHA-256
`33AF57E584C85A17B7E0A18D22E0C504793BD0C71A30DC864EE0775DC349F5F2`.
Mathematical/source repairs, lead errors, and reversals are zero. R29
manifest/tree SHA-256 values are
`3FC26BF7E9F628BF33AF9834C304C89071A21644DE923E6BCAC42FED6CE6AEE1`
and `7B25527C49B34E8EBB847D5887FAE707DBAB1DD9649A4508D0912407BAEAA96A`.

Bounded reader: 16 pages / 173,098 bytes / SHA-256
`2F2D5983DA0C539D607641859E6F6575BC6986B34261E8C5909427F7509F9F5B`.
Checkpoint R23: 6,479 bytes / SHA-256
`BB8583C50950D3831D2CC2E5E35380E52AD56A4AC60710A15F883A10C2C1D9E1`,
PASS/errors empty.

Restart at PDF one-based p.100 / printed p.101, opening §2.3 `Recollement des
préschémas`. Reuse existing evidence first; if absent, create exactly one
right-sized page, with a tight higher-resolution crop only for an actual
ambiguity. Do not use `Get-Content` on raster files. Zero agents are active;
at most three low-intensity mechanical workers are allowed, never for source,
mathematical, translation, diagram, or visual judgment. Next restart record:
`controls/CONTINUATION_STATE_20260802_P100_R25.json`.

## Latest exact continuation — printed p.101 closed

French EGA I is diplomatic through the canonical morphism in 2.4.1. Current
`source/ega1/ega1-2-fr.tex`: 16,814 bytes / 373 lines / SHA-256
`73968E89E47D9DB989CAAD204BB32699BDE5EBE500387BB4C166FE44CB167FF4`.
The page includes the native `B'`, `B`, `O_y` triangle and has no source
correction, ambiguity, typo, or raster. Authority image: 6,407,754 bytes /
SHA-256
`3DE6FB3D2EB090764E6B7404BFBE7BF024DBB82D1ED93972119B84A654333341`;
it was the sole new authority image after reuse search, and no crop/OCR ran.

English R30 contains five prose/logic/register fidelity repairs and no
mathematical/source correction, lead error, or reversal. Current source is
25,205 bytes / SHA-256
`39D017669DCEFD7B859A5851D112CD2605720CB68F2C7A695C8BEE3FAA6D3535`.
R30 manifest/tree SHA-256 values are
`0643CFD16D04791CC6865EA67D4C8FC19E0C77D38A073DB7BB0C4EE694AFAC4D`
and `E6C94B0401070FA4EA758DA90A03829EE7ED40D97A611A3EA86F751D13E64245`.

The no-overwrite bounded reader is 16 pages / 178,349 bytes / SHA-256
`238F7406BB562042BAEA00C1520169FDAB3F42FD8F64AFA82DA93F4DAA63A3C4`.
It also restores source-order `Exemple (number)` headings. Pages 11, 15, and
16 were personally reviewed and pass. Checkpoint R24: 7,918 bytes / SHA-256
`2B8A9A673EC9DE56E26E13566CF11568F8DD5F3474A602B95F6F7EDE6410781B`,
PASS/errors empty.

Restart at PDF one-based p.101 / printed p.102, Proposition 2.4.2. Reuse
existing evidence first. Create at most one right-sized image when absent and
only a tight higher-resolution crop for a genuine ambiguity. Never read a
raster as text. Zero agents are active; at most three low-intensity mechanical
workers are allowed, never for source, mathematical, translation, diagram, or
visual judgment. Next restart record:
`controls/CONTINUATION_STATE_20260802_P101_R26.json`.

## Latest exact continuation — printed p.102 closed

French EGA I is diplomatic through the p.102 colon in 2.4.5. Current
`source/ega1/ega1-2-fr.tex`: 21,434 bytes / 461 lines / SHA-256
`81031D76811A088C7A4B777D60F15FB1EBBCA837B5CB4CD24ABBD688B65B4C1F`.
No source correction, ambiguity, typo, diagram, or raster occurs. Sole new
authority image: 7,241,110 bytes / SHA-256
`370CD729724B078B34089C58DA7D8FEB4A5F9CB31460EC6664239EEE493A5F21`;
no crop/OCR ran.

English R31 makes nine prose/logic/register fidelity repairs and no
mathematical/source correction, lead error, or reversal. Current source is
25,259 bytes / SHA-256
`C9C8D501845AC6FDAF6E6172D308C90C5D34B22AED6C3059DF132F48F8B6E04B`.
R31 manifest/tree SHA-256 values are
`AACB1E16646D6DAAEDF384728D9106CF1D752DDC6223B0F405C2BCC8551562ED`
and `D90DDDD991E64D1C022D4BD1CABCD597D46B4FF6ECD23DFAA12B06DB07FEA72E`.

Controlling XeLaTeX bounded reader: 17 pages / 184,393 bytes / SHA-256
`2601FE3650929E0E0F11E23DC98A7A05DFE620C1EF59B9618C30D73563675845`.
Pages 16--17 personally pass; pages 1--15 are text-exact. The earlier
pdfLaTeX outputs are explicitly non-adjudicative workflow history. Checkpoint
R25: 8,036 bytes / SHA-256
`8DDC1F5216FE7D1E210C6F6AE57393F677BCDBAE965D948E5890846C59C66CF4`,
PASS/errors empty.

Restart at PDF one-based p.102 / printed p.103, continuation of 2.4.5. Reuse
only exact EGA/NUMDAM evidence; do not search all Papors by generic page
number. Generate at most one right-sized page when absent, with one tight
higher-resolution crop only for a genuine ambiguity. Zero agents are active;
no parallel heavy work. Next restart record:
`controls/CONTINUATION_STATE_20260802_P102_R27.json`.

## Latest exact continuation — printed p.103 closed

French source `source/ega1/ega1-2-fr.tex` is now diplomatic through the end of
I.2.5.2: 25,350 bytes / 549 lines / SHA-256
`E1A20C84C2BB1914106EF14B280F5C3B41B5AFA975E5761828167C50206CAA01`.
It includes 2.4.6--2.4.8, §2.5, 2.5.1--2.5.2, and a native
`I.2.5.2.diagram-fr` triangle. Source corrections, typos, ambiguities, and
rasters: zero. French ledger: nine rows / 4,215 bytes / SHA-256
`B520493D1CA931E46505DACB158597147EAC7DC84B9F53EF5AFAB21771AF13A7`.

Authority evidence is exactly one reuse-first/then-generated 1100-dpi page,
6,908,140 bytes / SHA-256
`68B9B43166B66DE85232A58E9084482CCC1AF3EDB11CFD7973FD5827B53453F3`;
no crop or OCR. English R32 makes three reversible prose/register repairs and
no mathematical/source repair, diagram change, lead error, or reversal.
Current English source: 25,275 bytes / SHA-256
`5CFC1E90B2C64C7E2E71FC9EA27DC56E0B03F6ECC48E4C440D613097AB82E191`.
R32 manifest/tree SHA-256 values are
`9E77BB96A68A09C711439AF2D22FFC4166B844288E6E85F82B69D515B4CD7680`
and `5220A1B928990312262D72AC84A3BABAA67B2AED3189AFFD25333911B16B3D22`.

Bounded reader: 18 pages / 190,068 bytes / SHA-256
`E0FA8D1C9A7D31496940AC72F7C7331966C19AB219B0825EC3D13D2B11F86D86`.
Only changed/new compiled pages 17--18 were rendered; both personally pass.
Checkpoint R26: 8,157 bytes / SHA-256
`E12D1BAFBF55F86BA7DC24349E7439E518A82397C649E51CA3186B13383BB78A`,
PASS/errors empty. Preserve/exclude the literal `$out` directory and the full
nine-row source-neutral workflow ledger. Continue at PDF one-based p.103 /
printed p.104, I.2.5.3. Search exact existing evidence first; generate one
ordinary image only if absent and one tighter crop only for a real ambiguity.
Do not batch, OCR, or parallelize heavy work. Zero agents are active.

## Latest exact continuation — printed p.104 closed

French EGA I is diplomatic through the p.104 seam in 3.2.1. Current sources:
`source/ega1/ega1-2-fr.tex`, 27,463 bytes / SHA-256
`AE6B128092ACBB8C1AFB4899EEA003FB966B6FF6669A264B59FD5F095AF4F029`;
new `source/ega1/ega1-3-fr.tex`, 1,706 bytes / SHA-256
`76F6B21FA566B11FA80E6538875E2A122B67616B37331EFE6E39794B697F6B93`.
The exact p.104 scope is 2.5.3--2.5.5, §3.1, and 3.2.1 through `est un produit
des`. French ledger: nine rows / 4,498 bytes / SHA-256
`C997C1D70DD5C6F32E67538657AB7DDE820ADF495BEF7EA8AF9BD3309F74769F`.

Important source adjudication: French 2.5.5 visibly prints `Si X est un
S-morphisme`. Preserve it in diplomatic French. The paired English correctly
uses `S-prescheme` because the following structure map and section definition
require that type, and it now carries a visible source note. Direct evidence:
one 1100-dpi page SHA
`B6EF43C83B262486BDCF22618765C16F692428CF2EBA02C007694183909ABF0A`
plus one tight 2500-dpi crop SHA
`4800122869C732889E83BF080FAC3923451157B73CAD92D2ABC043825933296B`.
No OCR or other image was made.

English R33 current `ega1-2.tex`: 25,429 bytes / SHA-256
`5785621211C98B1A4452864F3D408325ECED8F84C6CB16DE0875E052A6E7984F`;
audited `ega1-3.tex` remains SHA
`ED1559A08A41EC54E35C4A1E5E192552EF0B1EC52B4CE5FAF1F6E6BB3E5707FB`.
R33 manifest/tree SHA-256 values are
`9FE51AAA429E7749F926D04B52B05891820F4FE6CC3BCCA49FF318AE3402C213`
and `85C3EE351B174E4C8C4CE49E782EA151C72D91E6A35A96674E633E10BA0E6956`.

Bounded PDF: 18 pages / 194,458 bytes / SHA-256
`E6B26C091A3B982E3E8677E890A50775BEB32CA9D49F9CA269A02F20F6DA5DCD`.
Pages 1--17 are text-exact; page 18 alone changed and personally passes.
Checkpoint R27: 8,883 bytes / SHA-256
`D21A97F27507F42FC20848B422599877D5F04F4653E8A799DD1A5266B5FD49EF`,
PASS/errors empty. The three-row workflow ledger includes one repaired lead
transcription error: an explicit `X` initially copied into French 2.5.4 was
removed after direct source rereading. Continue at PDF one-based p.104 /
printed p.105, completing 3.2.1. Move the temporary closing definition marker
after the admitted continuation. Reuse first; create one ordinary page only
if absent, and a tighter crop only for an actual ambiguity. Zero agents are
active; do not batch, OCR, or parallelize heavy work.

## Current restart surface — printed p.105 closed

The controlling diplomatic French cursor is now the end of printed p.105,
through Corollary I.3.2.5. Current `source/ega1/ega1-3-fr.tex`: 6,117 bytes /
121 lines / SHA-256
`66E0EF2BBE7234C578E07E7465C0EEA8A86E8CB39310ACABD2AFA31A05716C22`.
Authority image:
`qa/authority_reuse/ega1_chapter1_opening/EGAI_pdfonebased104_printed105_context_1100dpi.png`,
9,091x11,428 / 6,192,099 bytes / SHA-256
`303FC3F3301AFC83E03CC8692C126A5D2777A1A000A4132C3DB32483EA642D5A`.
No p.105 crop, OCR, source typo, or unresolved reading exists.

English p.105 changes only the malformed product-morphism conditional and
plural `hypotheses/imply`. Current `ega1-3.tex`: 56,482 bytes / SHA-256
`180110F77A0665B749B1F29AB7DE6808E4E9BDEB8A857407572C3D6CF29B693B`;
two-operation inverse replay exactly restores SHA-256
`ED1559A08A41EC54E35C4A1E5E192552EF0B1EC52B4CE5FAF1F6E6BB3E5707FB`.
R34 manifest/tree SHA-256 values are
`7E5002ACDB744AE24EE49272325ADE110DAA406E813E3A80F357DB2B91AE472B`
and `E02F5175C3DEFA9A2EE35E2844ED39ABE01F7EC998331411E405AA7D87E8C241`.

Final French bounded PDF: 19 pages / 202,390 bytes / SHA-256
`B182ED823AB1F6ED7778AF30B96D11095B3284997CBA642234490D896472B206`;
pages 18--19 personally pass. Checkpoint R28: 9,118 bytes / SHA-256
`E09FD9270B63CA943059DDEDCA557FB420C4C65D60DCF2D46FC68AA51ECCE022`,
PASS/errors empty. French/English/workflow ledger SHA-256 values are
`4F85769E94A2E8EF7C3B4A6C7A8400D062313CC218BD5C97596C0109C947D8DB`,
`197F46B25506E94021E7987D7BB54DAC98FE4B649CD232E881DFB87E76004B55`,
and `3C472FDEC297A20F9A13F0E694A0347435AB84A9143BF96FA05A202BF77147C2`.

Resume at PDF one-based p.105 / printed p.106. The source begins with the
one-line proof of Corollary 3.2.5 and then Theorem 3.2.6. Search exact reuse
first; create one ordinary context image only if absent and one tighter crop
only for a real ambiguity. No agents are active. Do not repeat broad recursive
searches, batch rendering, new OCR, or parallel heavy work.

## Restart after printed p.106

French is admitted through printed p.106 / Lemma I.3.2.6.2. Current
`source/ega1/ega1-3-fr.tex`: 10,254 bytes / 216 lines / SHA-256
`D928E7E21AB6B3C97A5A4B8692A75033075A61A58BA44F2E10E17A6603E81E14`.
Authority image:
`qa/authority_reuse/ega1_chapter1_opening/EGAI_pdfonebased105_printed106_context_1100dpi.png`,
9,091x11,428 / 4,965,020 bytes / SHA-256
`8ECB4E558B1E60B0C989B2000844C2806C77765669CDFFBAF73C0D7678E4B7FF`.
No crop, OCR, source correction, source typo, unresolved reading, diagram, or
raster exists. The first append put p.106 before 3.2.4--3.2.5; this lead error
is repaired and logged, and both pre-repair builds are adverse only.

Final French bounded PDF:
`qa/ega1_chapter1_build/chapter1-p79-106-build-r3-xelatex/chapter1-p79-106-check-r1.pdf`,
20 pages / 207,270 bytes / SHA-256
`B35FD477AAAB362ABC38A6A957275635795E083F10AA2D3AA726D1D8A362EA6D`.
Pages 1--18 are predecessor-text exact; pages 19--20 personally pass. French
decision ledger: 11 rows / SHA-256
`E6757586AB33B973673E229E307EE9914AF5836EEC815643968DBD8F1C2A8F5D`.

English p.106 adds only the source-backed terminal `\qed` omitted from the
proof of Lemma 3.2.6.2. Current `ega1-3.tex`: 56,486 bytes / SHA-256
`4EE566EFB51DDD19D81E0392070899C2A64A51AF6997D65BC1B4ED07386C317B`;
one inverse operation exactly restores the p.105 source. R35 manifest/tree
SHA-256 values are
`FBEF05B2BDCB707DC1DB7AC8E176981B66F234DA03E1399208F5AE134EA99929`
and `BBBCB2AAA9C5A946847B25B2F483024E637558955863F5A1E194CB4FDCD6C52A`.
English section/full validations are PASS/errors empty at SHA-256
`D7D0E55F9AC38AF76A9302D2A593CFAB0D5C41BBC0AFA6BA957C09BCDB8E752A`
and `7DF09CABA52388F313CCA150D89C6309FA8A1E6EA685BBC87BF41D212E0CFE9F`.

Checkpoint R29: 10,362 bytes / SHA-256
`FA89227CD8E5CCBBA1EE733B93BE9C87782A39ADA29234C1F316646C942BBAD1`,
PASS/errors empty. French/English/workflow ledger SHA-256 values are
`E6757586AB33B973673E229E307EE9914AF5836EEC815643968DBD8F1C2A8F5D`,
`12BD1328BAD114D1B1CF117E03401E60391DA1C63FB078D28B62CC9C76B437F2`,
and `BD5C5881BBD39B639E4E7611D3514A2DEA177AA74AEF3AF5180A56A6A1B759C9`.

Resume at PDF one-based p.106 / printed p.107, Lemma 3.2.6.3. Search exact
reuse first; if absent, generate one context image only. Use a tighter
higher-resolution crop only for an actual ambiguity. No agents are active;
never use parallel builds, batch images, new OCR, the literal `$out`
directory, or Poppler directly on the known overlong English output path.

## Current exact continuation after printed p.107

Printed p.107 is closed at checkpoint R30, 10,050 bytes / SHA-256
`15657B56D2904F07954F47CC0414038EB9C5D1A24CA41E53EB214EBEBE6BC713`,
PASS/errors empty. Authority image SHA-256:
`E28F0B56EA197B2A091AD9F2CD813EDB01A51CEFADCBC1CA260E4603D6568476`.
French `ega1-3-fr.tex` is 14,987 bytes / SHA-256
`6D6DF12A04AEA3B2788983A70AB8A474A156C889369F0FD70CF560439E8F2D51`;
it contains all of 3.2.6.3 and 3.2.6.4 plus the exact p.107 fragment of
3.2.6.5. Final French bounded PDF: 20 pages / 212,863 bytes / SHA-256
`0FEA473F2FF2389C7AFB005930BEFA9A03004873BD1C4C9105D58BC3F7507D1B`.
French ledger SHA-256:
`0BBB806A5B6AE6AB72327A3BA47D222AFAD5DFA5C1FFCCFF711CA928660498AF`.

English p.107 moves the 3.2.6.1 citation to the product-structure assertion it
actually justifies. Final source: 56,478 bytes / SHA-256
`E6EEAE7CEF181FBB81A6E671AEE221B87E59AB43AD18174CAE570C9161EE3CA7`.
One inverse operation restores R35 exactly. R37 manifest/tree SHA-256 values:
`F5E43F1622CD9BBE5829A18A91771824C0D3426C1D797149F9CB8861FA28861A`
and `D9237435250A25A398CFF70A89052955964AA4DFF7113F74DE77E5A26DA748FE`.
Section/full validation SHA-256 values:
`346C47C220692A30C2D0D321B6449EB4786C47F70E0C9B6E6D2DBD753C95D737`
and `6642BED78416D3DE1CB1F42ECFB91792B8F5C15BDAC338F0FC7304F5DFCC2FDF`.
R36 and bounded build r1 are stale history after removal of fourteen visually
inert post-R35 indentation bytes. Final English bounded PDF r2: 12 pages /
SHA-256
`2CEAC677F19FDA30ED24C911A04E9D43F75162CDAAC914918A54C457C58BD784`.

Resume at PDF one-based p.107 / printed p.108. Before appending, remove the
temporary `\end{env}` after the p.107 fragment `d'après ce qui` and continue
the same 3.2.6.5 environment. Reuse exact imagery first; generate only one
relevant image or crop if genuinely needed, at resolution appropriate to the
detail. Up to two or three disjoint low-intensity grunt workers are permitted
when useful, but not for source, mathematical, translation, or final visual
judgment and never for render, OCR, or build swarms.

## Superseding continuation state after printed p.108

The earlier p.108 cursor above is closed. Current French
`source/ega1/ega1-3-fr.tex` is 18,863 bytes / 403 lines / SHA-256
`C818114F3BAE8B049C945F9AEFE79F2D74AED1959EAB8DB3ED667D4DEA9F367F`.
It is complete through printed p.108 and ends at the exact first-page fragment
of 3.3.5. Remove only the temporary terminal `\end{env}` for that fragment,
then continue the same environment from PDF one-based p.108 / printed p.109.

French checkpoint R31 is PASS/errors empty: 10,181 bytes / SHA-256
`C2990F06616057C1051F1CA6B4ED3A68BB04BA9B966E7D05B22738A657394282`.
French bounded PDF: 21 pages / 218,138 bytes / SHA-256
`4F013282A7F82AA7D6AAB44F7C41BB2CDEEFA904B7BA96622AB5F8A217B1B3D6`.
French ledger: 13 rows / SHA-256
`61815DBE2CE8BA37209E8FB59DDAF7C7B718E79061993C8277098D5E8420EC6F`.

Current English `source/ega1/ega1-3.tex` is 56,492 bytes / SHA-256
`0E9CE7FB4E26EE686D1549407FAB8ACF2B521C73C256EB86221524FD89D39D38`.
The sole admitted p.108 repair restores two source emphases in 3.3.1; two
inverse operations reproduce R37 exactly. R38 manifest/tree SHA-256 values:
`15D8794F8BF6AA98FDE1D527EBD87DFED961A03FE59225D7F52D13C245027961`
and `85E5FBAAD2D054550D91F893853B51B2AE4DC085E4E831E4B8C4C63F1A62C987`.
The visibly bracketed translator augmentation 3.2.9 remains English-only and
requires separate replay against its cited EGA II p.221 authority before final
editorial-augmentation closure.

Continue sequentially and reuse imagery first. Generate a single new page or
tight crop only when the next source decision actually needs it. Agents are
permitted for useful bounded, RAM-light mechanical support (normally no more
than two or three), but final source, mathematical, translation, and visual
judgment remains with the lead.

## Superseding continuation state after printed p.109

The earlier p.109 cursor above is closed. Current French
`source/ega1/ega1-3-fr.tex` is 22,550 bytes / 484 lines / SHA-256
`6C99E997042971815820CF5AF3145EB3E1EF37A8630538B61FB502F339FEBF09`.
It is complete through printed p.109 and ends immediately after the native
I.3.3.9 transitivity diagram. Printed p.110 continues the same proof sentence;
there is no temporary environment close or punctuation to remove.

French checkpoint R32 is PASS/errors empty: 10,719 bytes / SHA-256
`188004628018FCA04FD5FE31A8A8E690908FA57195DE2B6A33042A81CAF1CFCD`.
French bounded PDF: 22 pages / 223,448 bytes / SHA-256
`3FEAD5020F46956CD02F67268B3E1B568B38666D42322997DCAAF0614D285587`.
French ledger: 12 rows / SHA-256
`0936AEE282CBEF59C4C613DC3AB891BDEEE7BFDB086DAE6E16521D61DB0F19E1`.

Current English `source/ega1/ega1-3.tex` is 56,491 bytes / SHA-256
`E5E4C011C43B959AD95657C6B3B79612A0DB6D97A3B926A24A6F853E88861B8C`.
The p.109 repair removes one false period from the transitivity diagram; one
inverse operation reproduces R38 exactly. R39 manifest/tree SHA-256 values:
`5582CBE296292FDAD0D5FF8B94C8E660466523DD6DEB9DDF28ACA6B3AEA443DC`
and `B94674F50196214AF56CD3A4E58BA323CC821B8A61DA7D36669CD1C4B5363BCB`.

Do not silently alter French 3.3.8: it prints `f`, catalogued as
`EG-EGA-I-P109-FR-338-F-VS-G-SRCTYPO-001`. English correctly uses `g` and
immediately preserves the source witness in a translator note. Resume at PDF
one-based p.109 / printed p.110, the first sentence after the diagram.

## Superseding continuation state after printed p.110

Current French `source/ega1/ega1-3-fr.tex` is 25,782 bytes / 567 lines /
SHA-256
`EBB451F8E44FF4382A351AD5F19A9D3C657E8F7AAEB9B340073D42BB126989C6`.
It is complete through printed p.110 and 3.3.12 through `u=v`. Before adding
p.111, remove the final temporary `\end{env}` because 3.3.12 continues.

Checkpoint R33 is PASS/errors empty: 11,587 bytes / SHA-256
`66E00BE78EEB8B6B4E8E470C2DAFEC901274DC24B6E845FBE477BE2DB5034B76`.
French bounded PDF: 22 pages / 227,511 bytes / SHA-256
`04DAA9D0016A0D95C17CF68BF7468F9ACD2DD2B05EF0FBDB153A16B560B38D88`.

Do not rely on R32's old diagram-layout PASS. Direct p.110 comparison exposed
that lower-row labels in the p.109 3.3.6 and 3.3.9 left-arrow diagrams were
on the wrong side. R33 repairs those in French and English. It also restores
the previously omitted `psi_(S')` label in the English 3.3.11 diagram and
removes that diagram's false terminal period.

Current English `source/ega1/ega1-3.tex` is 56,504 bytes / SHA-256
`6196282B5900DB26B985B1E0E12385B7FA995F7807E8E43D833C0EB8CE8227F8`.
Seven inverse operations reproduce R39 exactly. R40 manifest/tree SHA-256:
`072C32119B3126F28C96BB6958FDDFA4A8E5F34B949E1E383F57C96D9D75FE00`
and `17CFEFE9E801D74857E235DD508E72F4C42AD0FB9EF123176E88EE499B26E215`.

Resume at PDF one-based p.110 / printed p.111. Continue sequentially, reuse
existing imagery first, and generate one source page or tight ambiguity crop
only when needed. Agents remain permitted for bounded RAM-light mechanical
support, but source, mathematical, translation, and visual adjudication stays
with the lead.

## Superseding continuation state after printed p.111

Current French `source/ega1/ega1-3-fr.tex` is 30,015 bytes / 654 lines /
SHA-256
`5C0481F52B66A1402C2B692B57F497B0CBEBE14763960CC43878CEEA7084F065`.
It is complete through printed p.111 and ends after the words `la partie de`
in 3.4.2. Before adding p.112, remove the final temporary `\end{env}` because
the sentence continues.

Checkpoint R34 is PASS/errors empty: 12,101 bytes / SHA-256
`7FBFDD83E08BC65055A19F18FEB29EED152777414894DBE6A4A6844668AA3AE3`.
French bounded PDF: 23 pages / 234,431 bytes / SHA-256
`13D29B451526DB13EE31A6DDCD2B904C8CDD759A2C56FEC8D6164F678751B538`.

Do not silently alter the two p.111 source typos. French diplomatically keeps
3.3.12 codomain `Y_(S')` and 3.3.15 direction `Z[T]->X`. English uses the
source-required `X'_(S')` and `X->Z[T]`, each with an immediate visible note.
Stable source IDs are
`EG-EGA-I-P111-FR-3312-BASECHANGE-TARGET-Y-VS-XPRIME-SRCTYPO-001` and
`EG-EGA-I-P111-FR-3315-MORPHISM-DIRECTION-SRCTYPO-001`.

Current English `source/ega1/ega1-3.tex` is 56,850 bytes / SHA-256
`A9FAD4038374CDC5BEAEC4412096AEC62D437D63A6D232349757BC868E0FB33C`.
Two inverse patches reproduce R40 exactly. R41 manifest/tree SHA-256:
`09EB142C493126469764AFEF70825EAF27FC1D7344BE5C422AA35D56AD953BCC`
and `4021B24BB11E6520EEC75F4748E75044FFDD2E14FB9733606DAD564650B26F33`.

Resume at PDF one-based p.111 / printed p.112. Continue sequentially, reuse
existing imagery first, and generate only one relevant source page or tight
crop at the detail actually required. Agents remain permitted for bounded,
RAM-light mechanical support; final source, mathematical, translation, and
visual adjudication remains with the lead.

## Superseding continuation state after printed p.112

Printed p.112 is closed under French checkpoint R35. Current diplomatic
French `source/ega1/ega1-3-fr.tex` is 33,565 bytes / 733 lines / SHA-256
`F8C95EAD1820DC660F61AA52C163C23D5F60C2A0F234DC668029F2B35E9F9ACE`.
It is complete through 3.4.5 and ends at the exact page-seam words `la donnée
de sa`. The final `\end{env}` is a temporary bounded-build close; remove that
single close before appending printed p.113.

The direct authority is NUMDAM EGA I, 31,680,717 bytes / 227 pages / SHA-256
`9ABA23020217535977E279BDD06A0413F48DA703086865BA4C00766C85DF4AE6`.
The reused p.112 context image is 2,428,045 bytes / SHA-256
`57FDC1EFF2D7518381671863DA5C4EC7A0AE547CA51D852D8766B46FEFDBB3E8`;
the only added detail crop is the 1,800-dpi product diagram, 63,797 bytes /
SHA-256
`8E18B69CEE5004BD71468F3A703A3C9C71E162B0555F5C2E01B761537841EFD3`.
No OCR was run. The page adds seven stable targets. Diplomatic French source
corrections and unresolved readings are both zero.

Checkpoint `controls/EGA1_CHAPTER1_P112_VALIDATION_R35.json` is 5,090 bytes /
SHA-256
`2024E09325ECB75B7398699C954856DA99CC13DB130E242357CF870C31110B9F`,
status
`PASS_DIPLOMATIC_FRENCH_THROUGH_P112_AND_PAIRED_ENGLISH_DIAGRAM_RECHECK__READY_PRINTED_P113`,
errors empty. The French bounded PDF is 24 pages / 239,546 bytes / SHA-256
`D0D8A789017B3931C4B2255DA3700FEF47C167CD9DB3982EF1B010C8A0420160`.

The paired English source is presently 56,850 bytes / SHA-256
`EC3BB57090C0A12EF48CF9572B0EE933DE8E0759E1F51379A921528A6BB1142E`.
One p.112 source-fidelity repair places the lower `psi'` label below, rather
than above, the lower arrow in the 3.4.3 product diagram. Its bounded English
PDF is 13 pages / 115,253 bytes / SHA-256
`A6742676640ADC895B1A24922B5119CDCFBBDE351F8EAEF35C9680BF27400D9E`.
The last complete 127-file English manifest/diff gate remains R41 at the
p.111 bytes; a new R42 manifest and diff validation for the p.112 source are
the first control-plane action still open.

Exact next cursor: NUMDAM PDF one-based p.112 / printed p.113, continuation of
3.4.5. Before any source mutation, read this handoff, `STATUS.md`, `LOGBOOK.md`,
the normalization/revision policy, R35 validation, and all three p.112 ledgers
in full. Continue sequentially and RAM-light. Do not run OCR, batch rendering,
an unbounded recursive search, or parallel heavy builds. Reuse existing images
first and create at most one tightly relevant page/crop at the resolution the
actual reading requires.

## Successor checkpoint: use this cursor, not the earlier p.113 cursor

Printed p.113 is complete and validated. French source is 37,418 bytes /
SHA-256
`C457C0F47862A74CABBCEC04E9F5B91919DAE184C3DBBD61DF896FEF4D14EF15`;
English source is 56,847 bytes / SHA-256
`8D581435C0AC808A879B35C5805834A620BEF657898EAD308744C357B6E537F8`.
R43 is the active complete English gate, with 127 files / 7,280,786 bytes and
canonical tree SHA-256
`531CBD2815F995C97B1DEDFDE19B68CD93A045FD639D07DF103027969FA86A10`.
R36 validation is PASS/errors empty at SHA-256
`06D68E902E48B278C0AB683D1992FFE739104AE7B670D55FD316EDF22046FA30`.

Next cursor: NUMDAM PDF one-based p.113 / printed p.114, proof of Corollary
3.4.8 beginning `En effet`. Do not remove any closing environment: the
Corollary 3.4.8 statement is genuinely complete and closed. Reuse the current
witness discipline: one bounded page image only if no exact witness exists,
no OCR, no unbounded recursive search, and serialized builds after real edits.

## Successor checkpoint: use this printed-p.115 cursor

Printed p.114 is complete and validated. French source is 41,097 bytes / 885
lines / SHA-256
`9545DE0E3DB01EB04591FBD65F5CDB406530A28F906132E331531ADD0B0C76BE`;
English source is 56,847 bytes / SHA-256
`E6CAD01349ABDC5F3AEBA24356E9593C1D1BFC717038E9D35D99E267C9C5416B`.
R44 is the active complete English gate, with 127 files / 7,280,786 bytes,
manifest SHA-256
`0574B3D851A04E1023F4D5BDE1D9D1717D9D644BD9EA93D542BF0CBE5950E10D`,
canonical tree SHA-256
`BBD421CCBEE4825695882D5C10BEBE12C3663B53D9D9A16F901490372168CB61`,
and PASS diff validation SHA-256
`08201B423C2CFEA44F8649A4B2F0AF570B04B6E578717BA91905A0D679186778`.
R37 validation is PASS/errors empty at 7,090 bytes / SHA-256
`C0575FC4F2215613939BC4657407D123370967A385B83E11229333D005CCFAE1`.

The direct French text in 3.4.9 prints `monomorphisme` for the induced map
from `k(x) tensor_(k(s)) k(y)`. Preserve it diplomatically and retain source
record `EG-EGA-I-P114-FR-349-TENSOR-MONOMORPHISM-SRCTYPO-001`. The English
`homomorphism` and immediate translator note are confirmed; do not revert
them. The p.114 English `q`-label-side repair is final diagram geometry only.

Next cursor: first remove only the temporary final `\end{env}` from
`source/ega1/ega1-3-fr.tex`, then continue the same 3.5.1 environment at
NUMDAM PDF one-based p.114 / printed p.115 after clause (ii). Reuse existing
witnesses first; if none is exact, create only one bounded page image. Keep
source/math/translation/visual judgment with the sole producer, run no OCR or
unbounded recursive search, and serialize all builds after real edits.

## Successor checkpoint: use this printed-p.116 cursor

Printed p.115 is complete and validated. French source is 44,578 bytes / 969
lines / SHA-256
`FCDD412953CDC75797758BCF4FA29B42BF90B703D497D5AA70B83BE8DF8173ED`;
English source is 56,894 bytes / SHA-256
`AB5F2BBC7E3AD82C0DAF342BC0AD0B3012FCB219FC02F6AFDA7E0DB70C6B347B`.
R45 is the active complete English gate: 127 files / 7,280,833 bytes,
manifest SHA-256
`DFD8BF3BD7A461608179190AAA5FF72AA5F345ECC46C3127D357BEC7B08088F8`,
tree SHA-256
`45B3E3D362F2E4D5227E26BFE4CEAA5620176581466DBF9C83D6D26FC0EADE9C`,
and PASS diff validation SHA-256
`903FF29D8B9EE60E69B9B523E6813C8F5F824BC6E63E7A7066F5A9DA4BE57198`.
R38 validation is PASS/errors empty at 7,651 bytes / SHA-256
`8D0C007424BBFAECD5F59CE33A25567EE6923C4A88D461BB87CE86ADA2496E1B`.

The p.115 English repairs are final: restore the two-component property-P
antecedent in 3.5.1, `further` for `encore`, `immediately` for `aussitôt`, and
the lower `alpha-prime` label below its arrow in 3.5.5. Four unique inverse
operations reproduce R44. Do not revert these repairs.

Next cursor: first remove only the temporary final `\end{env}` from
`source/ega1/ega1-3-fr.tex`, then continue the same 3.5.5 environment at
NUMDAM PDF one-based p.115 / printed p.116 immediately after the displayed
diagram. Reuse existing witnesses first; otherwise create one bounded page
image. Keep source/math/translation/visual judgment with the sole producer,
run no OCR or unbounded recursive search, and serialize builds after edits.

## Successor checkpoint: use this printed-p.117 cursor

Printed p.116 is complete and validated. French source is 48,499 bytes / 1,059
lines / SHA-256
`0B41FE7CCF850924D06C8F8BB2099555506985FCFF23A70CED2952C4AD7ED4EA`;
English source is 56,913 bytes / SHA-256
`5A1EA6875D95D891D87381A288C33B7184B97A9343A982D82D353EB3DA03F2A6`.
R46 is the active complete English gate: 127 files / 7,280,852 bytes,
manifest SHA-256
`37C59DE260A37EEB5D4542C3AF9FF71531CC01A6BE3450FAB280F0C1776BDC70`,
tree SHA-256
`83506DB9F2EEE686B2E5A7DC2E72BEF4730A3CD42A2C04667F0955FA16779AAA`,
and PASS diff validation SHA-256
`8FBD28F268EF1F8601F1F81A188B0D3FF674F5F64EA8F73881066EA9503B9083`.
R39 validation is PASS/errors empty at 7,251 bytes / SHA-256
`083D997689E74C8E7610C0894F978E643753D73DCCA4D8BB61B1FBA17A72339A`.

The p.116 English repairs are final: retain `proposition follows
immediately` in 3.5.7 and `first claim follows immediately` in 3.5.10. Two
unique inverse operations reproduce R45. The consecutive English displays for
the two field-valued product identities are an accepted width normalization;
do not alter their order or mathematical content.

Next cursor: append directly to `source/ega1/ega1-3-fr.tex` at NUMDAM PDF
one-based p.116 / printed p.117, beginning with the diagram that completes the
proof of 3.5.10. There is no temporary final `\end{env}` to remove. Reuse
existing witnesses first; otherwise create one bounded page image. Keep
source/math/translation/visual judgment with the sole producer, run no OCR or
unbounded recursive search, and serialize builds only after real edits.

## Successor checkpoint: use this printed-p.118 cursor

Printed p.117 is complete and validated. French source is 52,851 bytes / 1,156
lines / SHA-256
`DF4B43CE4A6D15D2C0295DFBF173A00ABC998A98C38AEE127E76AF9593D35153`;
English source is 56,919 bytes / SHA-256
`6CCAAE5D05343975ABD6E68B1265525DDCA2C3F7C4A8D25987649DE73DD6C2AC`.
R47 is the active complete English gate: 127 files / 7,280,858 bytes,
manifest SHA-256
`E8C29077CDC78DFB6A7F8A5544F3199F9E5564F64163B10FFC0047B21FC14E8B`,
tree SHA-256
`FA3CD639E1DC14145A9270C641F99F1D3FEF399EE96BFB40CC6B8ACD0F35E6E7`,
and PASS diff validation SHA-256
`A4E877FFFF87ECE878AFDD93BA29D2C2B4A48527D344B533AF40AF992FF2F5F1`.
R40 validation is PASS/errors empty at 7,122 bytes / SHA-256
`F35A37B89CB1DEE40A79D0C4E7AA708A006B608C166B153E241E2FB662A6464E`.

The p.117 English repair is final: retain `the condition first implies` in
Remark 3.5.11. One unique inverse operation reproduces R46. Retain the
documented fibre-product sign, explicit proof boundary, and terminal display
period normalizations. Do not remove the stable French formula anchor
`I.3.6.1.localization-fraction-fr`.

Next cursor: first remove only the temporary final `\end{env}` from
`source/ega1/ega1-3-fr.tex`, then continue the same 3.6.3 environment at
NUMDAM PDF one-based p.117 / printed p.118 immediately after the displayed
fibre-composition identity. Reuse existing witnesses first; otherwise create
one bounded page image. Keep source/math/translation/visual judgment with the
sole producer, run no OCR or unbounded recursive search, and serialize builds
only after real edits.

## Successor checkpoint: use this printed-p.119 cursor

Printed p.118 is complete and validated. French source is 57,071 bytes / 1,241
lines / SHA-256
`2EDB68A378FE6C959B048180148FF7E69E42916D261F92207A24DA793B120192`;
English source is 56,933 bytes / SHA-256
`55C1E1129E40F1E2F8DB7B46867B3E49AE2556F04C1CFE1FBF5EE3C149B63BD9`.
R48 is the active complete English gate: 127 files / 7,280,872 bytes,
manifest SHA-256
`309B5B0A48AC2F3AD8903891526D8722ECB2C64C5CF18F5293F398BF89B58668`,
tree SHA-256
`E8331E55DEABD57007298B17012BE1E50C20370837535F413F3679EBE3FB646B`,
and PASS diff validation SHA-256
`FE9746CE8BB49D3DF2F96D9EBF9B49AE67B8EEBFD61FD79FAC972AEDA31D4373`.
R41 validation is PASS/errors empty at 7,161 bytes / SHA-256
`40CE9BF9A4180940D00ACA2E0A69BA3D3F51CF059F9BFD037D26B4A7D83AEF7A`.

The p.118 English repair is final: retain `from later in Chapter I and from
Chapter II` in the subsection 3.7 footnote. One unique inverse operation
reproduces R47. Retain the documented English title position, inline footnote,
proof-boundary, and p.119 noun-phrase marker normalizations. The French
bounded footnote-marker style remains an explicit cumulative-reader concern,
not a missing text item.

Next cursor: first remove only the temporary final `\end{env}` from
`source/ega1/ega1-3-fr.tex`, then continue the same 3.7.2 environment at
NUMDAM PDF one-based p.118 / printed p.119 after the exact words `l'unique
point`, beginning `fermé y=\mathfrak{J}`. Reuse existing witnesses first;
otherwise create one bounded page image. Keep source/math/translation/visual
judgment with the sole producer, run no OCR or unbounded recursive search, and
serialize builds only after real edits.

## Successor checkpoint: use this printed-p.120 cursor

Printed p.119 is complete and validated. French section 3 is complete in
`source/ega1/ega1-3-fr.tex`, 59,766 bytes / 1,282 lines / SHA-256
`DB4F986C9FDC1B66FF2D627C5E9121BCE0490563B7C14415320B5DDD7424B851`.
Section 4 now begins in `source/ega1/ega1-4-fr.tex`, 1,292 bytes / 29 lines /
SHA-256
`BEDC1B141252E20EE298389D39C3B9C38D9403E08AF57F5ED53CD25BB115916F`,
through the complete statement of Proposition 4.1.2. There is no temporary
environment close to remove.

The p.119 English pass requires no source mutation. R49 is the active complete
English gate: 127 files / 7,280,872 bytes, manifest SHA-256
`0BB20AFE664720F711F04AEC55D88E96DA918C27C26DF26FE6D60A7AE8838E8C`,
tree SHA-256
`E8331E55DEABD57007298B17012BE1E50C20370837535F413F3679EBE3FB646B`,
and PASS zero-delta diff validation SHA-256
`519B2CBC2EA3FCB9FCCCD3F4FB85907776DAD1D260F48BE86E6ED3D888B82031`.
R42 validation is PASS/errors empty at 8,838 bytes / SHA-256
`B82C5D63AF34111BBE4D94700582770A36CFF1A005E76C8C088E960421DE83CC`.

Retain the English reference-type expansion in 4.1.1, the explicit p.120
proof boundary, and the bounded-wrapper section-counter seed as documented
reader/QA normalizations. The 17-line English section-4 prefix is a verified
build projection, not source. Temporary `Q:` was removed and is absent.

Next cursor: append directly to `source/ega1/ega1-4-fr.tex` at NUMDAM PDF
one-based p.119 / printed p.120, beginning the proof of Proposition 4.1.2
with `Il suffit évidemment`. Reuse existing witnesses first; otherwise create
one bounded page image. Keep source/math/translation/visual judgment with the
sole producer, run no OCR or unbounded recursive search, and serialize builds
only after real edits.

## Successor checkpoint: use this printed-p.121 cursor

Printed p.120 is complete and validated. French `source/ega1/ega1-4-fr.tex`
is 5,966 bytes / 118 lines / SHA-256
`90C1D93784F8A1817702732BE9E69B513F9D538A4F878688894D131F24F20B71`,
through the exact p.120 seam `d'un sous-` in the open Proposition 4.1.6. One
temporary final `\end{proposition}` must be removed before continuation. The
p.120 inverse replay restores the p.119 source exactly.

The p.120 English pass requires no source mutation. R50 is the active complete
English gate: 127 files / 7,280,872 bytes, manifest SHA-256
`D6F7AFA347FD3B0B3D63E310394D0D3CE9D77AF57F26C44A9C3FE189C98D43A8`,
tree SHA-256
`E8331E55DEABD57007298B17012BE1E50C20370837535F413F3679EBE3FB646B`,
and PASS zero-delta diff validation SHA-256
`988292B9754053803D7AEDDD1817D95A7543D6A1361F806F91BC2C29E1DD4FC0`.
R43 validation is PASS/errors empty at 9,149 bytes / SHA-256
`4721AB517C81B0770246C1F1CC1A4FF1C579FB50A0392A767E83DD9B51F5EF20`.

Retain the English explicit proof environments, proof-reference type words,
and whole-word p.121 marker as documented reader-facing normalizations. The
51-line English p.120 projection is a verified build-only artifact: its first
50 lines equal live `ega1-4.tex` lines 18--67 and its last line only balances
the open proposition. Temporary `Q:` was removed and is absent.

Next cursor: first remove only the temporary final `\end{proposition}` from
`source/ega1/ega1-4-fr.tex`, then continue the live Proposition 4.1.6 from
direct NUMDAM PDF one-based p.120 / printed p.121 authority after `d'un
sous-`. Reuse existing witnesses first; otherwise create one bounded page
image. Keep source/math/translation/visual judgment with the sole producer,
run no OCR or unbounded recursive search, and serialize builds only after
real edits.

## Successor checkpoint: use this printed-p.122 cursor

Printed p.121 is complete and validated. French `source/ega1/ega1-4-fr.tex`
is 10,356 bytes / 203 lines / SHA-256
`52A11F6F8AFE416C5D1999C463FE328060F3E1009BB14E0781A636C6761C6169`,
through the exact terminal words `est un morphisme Z\to Y` in the proof of
Proposition 4.1.9. There is no temporary environment close to remove. The
p.121 inverse replay restores the p.120 source exactly.

The p.121 English pass requires no source mutation. R51 is the active complete
English gate: 127 files / 7,280,872 bytes, manifest SHA-256
`F6736445D6C310C85A5FA44E5B718C71EC6B6574DCC28CFF1BD8AD673EBF46A8`,
tree SHA-256
`E8331E55DEABD57007298B17012BE1E50C20370837535F413F3679EBE3FB646B`,
and PASS zero-delta diff validation SHA-256
`8E0A9E1AD4122E6320D288A3CDE75D7262C4608FEB2D7983ADBD2101FAE6C6BC`.
R44 validation is PASS/errors empty at 9,607 bytes / SHA-256
`16F74B50E79D3AFF7373FB8104C9507FC028D7E151523550C8165ACC3D668EF8`.

Retain the whole-word English page marker, explicit proof environments,
translator footnote on `majoré`, and English `g` for French `g'` as documented
reader-facing normalizations. The 97-line English p.121 projection is a
verified build-only artifact: its first 96 lines equal live `ega1-4.tex`
lines 18--113 and its last line only balances the open proof. Temporary `Q:`
was removed and is absent.

Next cursor: append directly to `source/ega1/ega1-4-fr.tex` from direct NUMDAM
PDF one-based p.121 / printed p.122 authority, continuing the proof of
Proposition 4.1.9 after the morphism `g':Z\to Y`. Reuse existing witnesses
first; otherwise create one bounded page image. Keep source/math/translation/
visual judgment with the sole producer, run no OCR or unbounded recursive
search, and serialize builds only after real edits.

## Successor checkpoint: use this printed-p.123 cursor

Printed p.122 is complete and validated. French `source/ega1/ega1-4-fr.tex`
is 14,467 bytes / 285 lines / SHA-256
`984EFEEB45E09398B9B1E0E7DAB3602D89119F2AC2A860A19872CFEC0494992E`,
through the exact terminal words `restriction à $U$ de l'image` in the proof
of Proposition 4.2.2(b). The final `\end{enumerate}` is temporary. The p.122
inverse truncation restores the p.121 source exactly at 10,356 bytes / SHA-256
`52A11F6F8AFE416C5D1999C463FE328060F3E1009BB14E0781A636C6761C6169`.

Printed proof 4.2.2(a) reverses the source and target of `\theta^\sharp`.
The canonical French preserves this single catalogued printed mathematical
error; the inherited English gives the typed direction and an explicit
translator footnote. No English source byte changed. R52 is the active
complete English gate: 127 files / 7,280,872 bytes, manifest SHA-256
`B2BCA961EEE011D9E5F03147CD696F9888D96E6A58F944DD1A2ED6FB292EE614`,
tree SHA-256
`E8331E55DEABD57007298B17012BE1E50C20370837535F413F3679EBE3FB646B`,
and PASS zero-delta diff validation SHA-256
`75B3BC2A7E09CDDBCBAEA5D558E9F37095FA4052C908330323F43F2D50A2AF4D`.
R45 validation is PASS/errors empty at 10,598 bytes / SHA-256
`B188DC15970531829D52CDC27BEC574A7DC056E05C5BCB9814F326657C680B14`.

Retain English `g` across the printed `g'`/`g` fluctuation and the p.123
marker before the complete direct-image object as documented reader-facing
normalizations. The 146-line English p.122 projection is a verified
build-only artifact: its first 144 lines equal live `ega1-4.tex` lines
18--161 and its final two lines only balance the open enumerate and proof.
Temporary `Q:` was removed and is absent.

Next cursor: first remove only the temporary final `\end{enumerate}` from
`source/ega1/ega1-4-fr.tex`, then continue from direct NUMDAM PDF one-based
p.122 / printed p.123 authority after `restriction à $U$ de l'image`. Reuse
existing witnesses first; otherwise create one bounded page image. Keep
source/math/translation/visual judgment with the sole producer, run no OCR
or unbounded recursive search, and serialize builds only after real edits.

## Successor checkpoint: use this printed-p.124 cursor

Printed p.123 is complete and validated. French `source/ega1/ega1-4-fr.tex`
is 18,980 bytes / 365 lines / SHA-256
`B75325670BDB54B9B6F17AF3945110A86E2506F3EF41A699FE3032B5B5EEFACC`,
through the exact terminal words `il faut et il suffit` in Corollary
4.2.4(a). The final `\end{enumerate}` and `\end{corollary}` are temporary.
The p.123 inverse suffix replacement restores the p.122 source exactly at
14,467 bytes / SHA-256
`984EFEEB45E09398B9B1E0E7DAB3602D89119F2AC2A860A19872CFEC0494992E`.
The caught delimiter-selection error was exactly restored before
continuation and has no remaining effect.

The p.123 English pass requires no source mutation and no new author
correction. R53 is the active complete English gate: 127 files / 7,280,872
bytes, manifest SHA-256
`A66887EBE9AA70959C970051C08550FD8A4DE525CD78D23A21662B4C75F18ED5`,
tree SHA-256
`E8331E55DEABD57007298B17012BE1E50C20370837535F413F3679EBE3FB646B`,
and PASS zero-delta diff validation SHA-256
`465F8FE2D3DC7B10BA4CC74792B81A8BD65B51FD29C03B37B0AD2495F5979DD9`.
R46 validation is PASS/errors empty at 10,743 bytes / SHA-256
`859AE56FAFA479F12F68B1080E61100CD9B0F2C750DFA9041774516BC3CDF20C`.

Retain the p.123 direct-image page-boundary normalization and the carried,
explicit p.122 theta correction. The 189-line English p.123 projection is a
verified build-only artifact: its first 187 lines equal live `ega1-4.tex`
lines 18--204 and its final two lines only balance the open enumerate and
corollary. The superseded live-marker build is retained as workflow evidence;
no XeLaTeX process or `Q:` mapping remains.

Next cursor: first remove only the temporary final `\end{enumerate}` and
`\end{corollary}` from `source/ega1/ega1-4-fr.tex`, then continue from direct
NUMDAM PDF one-based p.123 / printed p.124 authority after `il faut et il
suffit`. Reuse existing witnesses first; otherwise create one bounded page
image. Keep source/math/translation/visual judgment with the sole producer,
run no OCR or unbounded recursive search, and serialize builds only after
real edits.

## Successor checkpoint: use this printed-p.125 cursor

Printed p.124 is complete and validated. French `source/ega1/ega1-4-fr.tex`
is 23,239 bytes / 440 lines / SHA-256
`E9061031DB90102A99851D0397A879CCF422F50A820F8C2A30AF30E222CC9185`,
through the exact terminal phrase `la restriction de
$\alpha\times_S\beta$` in the proof of Proposition 4.3.1. No temporary final
environment close is present. The p.124 inverse suffix replacement restores
the p.123 source exactly at 18,980 bytes / SHA-256
`B75325670BDB54B9B6F17AF3945110A86E2506F3EF41A699FE3032B5B5EEFACC`.

The p.124 English pass requires no source mutation and no new author
correction. R54 is the active complete English gate: 127 files / 7,280,872
bytes, manifest SHA-256
`9A53F6C16D4DD5D366696988C95321DCE2062E1010CF981526C7233296F541A4`,
tree SHA-256
`E8331E55DEABD57007298B17012BE1E50C20370837535F413F3679EBE3FB646B`,
and PASS zero-delta diff validation SHA-256
`BA53F085977613E2ABA88B3CF943837204E3BBB9A9C2D1EFF80D59891EA8B43C`.
R47 validation is PASS/errors empty at 10,336 bytes / SHA-256
`49BAFE90DBC08F35258F8C1AB4C3B476971B3B9B5359667B8C9D0564CC4E6A54`.

Retain the p.124 marker immediately before English `for its restriction`
and the carried, explicit p.122 theta correction. The 234-line English p.124
projection is a verified build-only artifact: its first 233 lines equal live
`ega1-4.tex` lines 18--250 and its final line only balances the open proof.
The corrected pre-build projection attempt and semantic-block placement
retries are recorded in the workflow ledger; no XeLaTeX process or `Q:`
mapping remains.

Next cursor: append directly to `source/ega1/ega1-4-fr.tex` from direct NUMDAM
PDF one-based p.124 / printed p.125 authority after `la restriction de
$\alpha\times_S\beta$`. Do not remove any closing environment first. Reuse
existing witnesses first; otherwise create one bounded page image. Keep
source/math/translation/visual judgment with the sole producer, run no OCR
or unbounded recursive search, and serialize builds only after real edits.

## Successor checkpoint: use this printed-p.126 cursor

Printed p.125 is complete and validated. French `source/ega1/ega1-4-fr.tex`
is 27,679 bytes / 522 lines / SHA-256
`E26B5510C2DF88911C36C57755D6D5AAF6EF23174C9B30DA70BB95FC6A955FA2`,
through the exact terminal phrase `qui s'accorde avec celle introduite` in
the inverse-image terminology following Proposition 4.4.1. No temporary
final environment close is present. The p.125 inverse suffix truncation
restores the p.124 source exactly at 23,239 bytes / SHA-256
`E9061031DB90102A99851D0397A879CCF422F50A820F8C2A30AF30E222CC9185`.

The p.125 English pass requires no source mutation and no new author
correction. R55 is the active complete English gate: 127 files / 7,280,872
bytes, manifest SHA-256
`2C76ACD405EDA12EF0D89A89FFF7388410B770F4940C9F55EC8476859218E165`,
tree SHA-256
`E8331E55DEABD57007298B17012BE1E50C20370837535F413F3679EBE3FB646B`,
and PASS zero-delta diff validation SHA-256
`38C475CFA262D891E3747AFF0FF517E3E81602ADBFA733131602F30B6F412A31`.
R48 validation is PASS/errors empty at 10,341 bytes / SHA-256
`0B5B2C235F4E2166F5A15F084A4B8FC9592EA7426D2CB663EB916DBDAD9CA1F0`.

Retain the p.125 marker and the carried, explicit p.122 theta correction. The
281-line English p.125 projection is a verified build-only artifact exactly
equal to live `ega1-4.tex` lines 18--298, with no balancing additions. The
semantic-anchor and read-only audit-helper corrections are recorded in the
workflow ledger; no XeLaTeX process or `Q:` mapping remains.

Next cursor: append directly to `source/ega1/ega1-4-fr.tex` from direct
NUMDAM PDF one-based p.125 / printed p.126 authority after `qui s'accorde
avec celle introduite`. Do not remove any closing environment first. Reuse
existing witnesses first; otherwise create one bounded page image. Keep
source/math/translation/visual judgment with the sole producer, run no OCR
or unbounded recursive search, and serialize builds only after real edits.

## Successor checkpoint: use this printed-p.127 cursor

Printed p.126 is complete and validated. French `source/ega1/ega1-4-fr.tex`
is 31,712 bytes / 619 lines / SHA-256
`96BA0D70ADCFA3758DEBB25113B8AE0CA71CCC8D4CE12C1FBBFA8CECBF75D1A7`,
through the exact terminal phrase `un isomorphisme local en` in Definition
4.5.2. Its final `\end{definition}` is temporary and is the only source
delimiter to remove before p.127. The p.126 inverse suffix truncation restores
the p.125 source exactly at 27,679 bytes / SHA-256
`E26B5510C2DF88911C36C57755D6D5AAF6EF23174C9B30DA70BB95FC6A955FA2`.

Canonical French preserves the official printed 4.4.5 error `B est une
A-algèbre`; the typed direction is (A) a (B)-algebra, retained visibly
by English `\erratum[II]`. English Corollary 4.4.6 also now restores the
source-explicit (\mathscr O_X) factor. Current English `ega1-4.tex` is
33,373 bytes / SHA-256
`CE8036FF9EF584DD794C7D4925EA62FE7937229E57212873B1C25DE68F8715A5`.
One context-bound inverse removes that eight-byte addition and reproduces R56.

R57 is the active English gate: manifest SHA-256
`A8C6D3E4AA6E478CBFCD1A144C6460D9DF03195C09758C713C9CC4C0048739A1`,
tree SHA-256
`C22FBDE03D3833584E83A448F5BB74B51399798C4B1E1C82769659211DCAE1E2`,
and PASS diff validation SHA-256
`421DC3016B112F2CD3E1CA92A3E7C76E4FA438B44C83B05C98CD280048C251B5`.
R49 validation is PASS/errors empty at 12,000 bytes / SHA-256
`98501091AB4641EEAFB20F2FFC7E25225189C2A2784E3EDE0AEA7773F1E19DE9`.

Retain the p.126 marker, the visible 4.4.5 Err-II correction, the repaired
4.4.6 ideal criterion, and the carried p.122 theta correction. The 354-line
English projection is build-only: its first 353 lines equal repaired live
`ega1-4.tex` lines 18--370 and its last line only balances Definition
4.5.2. No XeLaTeX process or `Q:` mapping remains.

Next cursor: remove only the temporary final `\end{definition}` from
`source/ega1/ega1-4-fr.tex`, then continue from direct NUMDAM PDF one-based
p.126 / printed p.127 authority after `un isomorphisme local en`. Reuse
existing witnesses first; otherwise create one bounded page image. Keep
source/math/translation/visual judgment with the sole producer, run no OCR
or unbounded recursive search, and serialize builds only after real edits.

## Successor checkpoint: use this printed-p.128 cursor

Printed p.127 is complete and validated. French section 4 is complete in
`source/ega1/ega1-4-fr.tex`, 34,793 bytes / 682 lines / SHA-256
`9775A6A8EA2AC2415CCE4DC64EEA356382ECED4F06C59FB67C602C6C7ED6F0C1`.
Section 5 begins in `source/ega1/ega1-5-fr.tex`, 681 bytes / 17 lines /
SHA-256
`E4893706A6EFAEB40D74BECC0FFA3C7E32A1FB3FCA64374CC4B6F9EDCD17163C`,
through Proposition 5.1.1's terminal words `de B.`. No temporary close is
present. The exact inverse restores p.126 and removes only the p.127-new file
from the predecessor set.

French preserves the printed 4.5.5 miscitation `(4.2.4)` and unintroduced
`z,z'`. English keeps the typed citation and required point introduction with
two visible translator notes. R59 is the active 127-file English gate:
manifest SHA-256
`3D874D60FA7AB1CE4C0A0496BD20C3B096481E0A35463D851ACD295CCBD08569`,
tree SHA-256
`BF73FCED73F50B5A18F310A4206EC14955E1DC8512BD50DC6847BCE60A19005D`,
and PASS diff validation SHA-256
`C68E010B34CF050695FCDC5AC8A1AC5F405A4AC05661A0558979214547426C73`.
R50 combined validation is PASS/errors empty at SHA-256
`D631DC20C4EF98C822AA61FF29A02176382A23E40077C1D36338FE359E80EA25`.
The p.127 pre-Stacks block is present and current.

Next cursor: append directly to `source/ega1/ega1-5-fr.tex` from direct NUMDAM
PDF one-based p.127 / printed p.128, beginning the proof of Proposition 5.1.1.
Do not remove a closing environment first. Reuse exact witnesses first; if
none exists, create one bounded context image only. Keep source, mathematics,
translation, semantic, and visual judgment with the sole producer; run no OCR
or unbounded search and build serially only after real edits.

## Successor checkpoint: use this printed-p.129 cursor

Printed p.128 is complete and validated. French `source/ega1/ega1-5-fr.tex`
is 5,091 bytes / 103 lines / SHA-256
`EB37539C7AAD273C7A780E087FDB8863CD86A0C284D0BA532B72D395FC5860A0`,
through the exact physical-page fragment `l'homomor-` in 5.1.5. Its final
`\end{env}` is temporary and is the only source delimiter to remove before
p.129. The exact inverse truncation to 681 bytes reproduces sealed p.127 at
SHA-256
`E4893706A6EFAEB40D74BECC0FFA3C7E32A1FB3FCA64374CC4B6F9EDCD17163C`.

Preserve the printed 5.1.2 word-order defect diplomatically. Retain the two
settled English p.128 repairs: ideal `\mathfrak{I}` rather than the erroneous
`\mathfrak{I}_x` on the left of the prime-ideal inclusion, and defining
`means` rather than one-way `implies`. English `ega1-5.tex` is 46,829 bytes /
SHA-256
`D3BB566847A24BD268157D7171BD9F5B282FA2C9B8F4D1A1ABD9B84F656FEFF3`;
two unique inverse substitutions reproduce R60 exactly.

R61 is the active 127-file English gate: manifest SHA-256
`D7EFC8554A3B01C0FD5D715131B553EC95701D718FE7683315EFBA5FA0F219EE`,
tree SHA-256
`658ACB58DBE08F3641410EF071EBA6D80DB628C0560940DF6BEFE8AFBAF091AD`,
and PASS diff validation SHA-256
`BD43E7FD61B33CC687B09F1EF7F51FF8E6CB5CEC2B5090B78A291A85A5761C0D`.
R51 combined validation is PASS/errors empty at SHA-256
`94F833E316F3726489EEF9254871BB55B12EBA691B7BFEAF918F76C285A7DE41`.
The p.128 pre-Stacks block is present at SHA-256
`387C86432463544C2DB0B5146A1164F07A4AF49D3876FFA1C50655E7333DFF09`.

Next cursor: remove only the temporary final `\end{env}` from
`source/ega1/ega1-5-fr.tex`, then continue from direct NUMDAM PDF one-based
p.128 / printed p.129 authority after `l'homomor-`. Reuse an existing exact
witness first; otherwise create one bounded context image only. Keep source,
mathematics, translation, semantic, and visual judgment with the sole
producer; run no OCR or unbounded search and build serially only after real
edits.

## Successor checkpoint: use this printed-p.130 cursor

Printed p.129 is complete and validated. French `source/ega1/ega1-5-fr.tex`
is 9,060 bytes / 190 lines / SHA-256
`D3DEC590DD38DE0A1CB5F756F7970AC4434CF1E5521379855BCC0592B4E7941C`,
through the exact terminal sentence ending `éléments nilpotents.` after
Corollary 5.1.8. There is no temporary final close. The context-bound inverse
replaces the p.129 marker-to-EOF region with one `end-env` line and reproduces
p.128 exactly at 5,091 bytes / SHA-256
`EB37539C7AAD273C7A780E087FDB8863CD86A0C284D0BA532B72D395FC5860A0`.

The English p.129 pass is zero mutation. Retain established `omega-flat`,
residue-field notation, and normalized whole-word placement across the French
physical-page seam. R63 is the active 127-file gate: manifest SHA-256
`13659CCA1A6298345AC1EF029422A1BD4ADCFCDD75763B9D0331B7846ED58605`,
tree SHA-256
`658ACB58DBE08F3641410EF071EBA6D80DB628C0560940DF6BEFE8AFBAF091AD`,
and PASS zero-delta validation SHA-256
`0AC289389C15769AC85CEF5AD442CCDAE0B9BF77226EF48666BC0DB8AF5F250E`.
R52 combined validation is PASS/errors empty at SHA-256
`2A69BDB7C8D978A1BC2864A66A738A5C7450A3DE567EB7A67A937817EB1E2902`.
The p.129 pre-Stacks block is present at SHA-256
`88D8A1AF0020C8F0561F837B9C01DB7494FBD7CE4193B215A44645E9DCE9BA19`.

Next cursor: append directly to `source/ega1/ega1-5-fr.tex` from direct
NUMDAM PDF one-based p.129 / printed p.130 authority, beginning Proposition
5.1.9. Do not remove a closing environment first. Reuse an existing exact
witness first; otherwise create one bounded context image only. Keep source,
mathematics, translation, semantic, and visual judgment with the sole
producer; run no OCR or unbounded search and build serially only after real
edits.

## Successor checkpoint: use this printed-p.131 cursor

Printed p.130 is complete and validated. French `source/ega1/ega1-5-fr.tex`
is 12,517 bytes / 267 lines / SHA-256
`4F6DDD36624D115FF3571344674D5B3D49E101F4851D2E634ED094359F3DC7A2`,
through the exact words `ce qui résultera de` in the proof of Proposition
5.1.9. There is no temporary final close. Truncation to the first 9,060 UTF-8
bytes reproduces sealed p.129 at SHA-256
`D3DEC590DD38DE0A1CB5F756F7970AC4434CF1E5521379855BCC0592B4E7941C`.

The English p.130 pass is zero mutation. Retain the systematic `I`, `K`, and
`vphi` notation and the explicit page-seam placement of `H^1(X,I)=0` before
the inherited p.131 marker. R65 is the active 127-file gate: manifest SHA-256
`76207E6D99DA99033EB431B51886630B4A917FDEEDEE29308FD97FBE2DCDE7F0`,
tree SHA-256
`658ACB58DBE08F3641410EF071EBA6D80DB628C0560940DF6BEFE8AFBAF091AD`,
and PASS zero-delta validation SHA-256
`498854BC46966003417E66D90A21777E3B62DEB7729244C45E064AF467D7A287`.
R53 combined validation is PASS/errors empty at SHA-256
`BDD7227EE137F2B61A57438AB84D3B564131AD214C9A1F8AFD918CE7A2472F8F`.
The p.130 pre-Stacks block is present at SHA-256
`2D2E022FCF22DC3C47278D7273F4B6B4BB79DDD0BFE73D87E65628D520E1E66A`.

Next cursor: append directly to `source/ega1/ega1-5-fr.tex` from direct
NUMDAM PDF one-based p.130 / printed p.131 authority after `ce qui résultera
de`. Do not remove a closing environment first. Reuse an existing exact
witness first; otherwise create one bounded context image only. Keep source,
mathematics, translation, semantic, and visual judgment with the sole
producer; run no OCR or unbounded search and build serially only after real
edits.

## Successor checkpoint: use this printed-p.132 cursor

Printed p.131 is complete and validated. French `source/ega1/ega1-5-fr.tex`
is 16,480 bytes / 350 lines / SHA-256
`C6F64E7AD05183672B3F709BE452A0EA0EA3D5013030AE0A03792D3D0B85B6EA`,
through the statement of Corollary 5.2.3 and exact terminal words
`un sous-préschéma induit sur un ouvert de Z.` There is no temporary final
close. Truncation to the first 12,517 UTF-8 bytes reproduces sealed p.130 at
SHA-256
`4F6DDD36624D115FF3571344674D5B3D49E101F4851D2E634ED094359F3DC7A2`.

Direct authority confirms one printed source error in Lemma 5.1.9.2: French
prints `F|Y` where the restriction required on the neighbourhood is `F|V`.
Preserve `F|Y` in diplomatic French. English keeps `F|V` with one visible
translator footnote; deleting only that note restores sealed R66 exactly.
R67 is the active 127-file gate: manifest SHA-256
`F9DF2387D0B08F4269B8307DCD7268DD93AA47706F5B024967ED6D8149571EE1`,
tree SHA-256
`B12D07B194C59E154BE7F7DB383C9B52E0AC6E4ADCAEEF9E0E567522090558A7`,
and PASS validation SHA-256
`3AC5F994DC237FDDBCCF5A839D5B5212502B5560F1D92AAD366AB6971B106EAE`.
R54 combined validation is PASS/errors empty at SHA-256
`4B51F8C9B847D1D4A3C8C759CAEE6E09DD1F5EA00D5291E9623A44AF69990AA4`.
The p.131 pre-Stacks block is present at SHA-256
`57EC4614738F849349AC91BC57EDC92E85D17B92CCC33F9AE6A57C6A80BBBCB8`.

Next cursor: append directly to `source/ega1/ega1-5-fr.tex` from direct
NUMDAM PDF one-based p.131 / printed p.132 authority, beginning the proof of
Corollary 5.2.3. Do not remove a closing environment first. Reuse an existing
exact witness first; otherwise create one bounded context image only. Keep
source, mathematics, translation, semantic, and visual judgment with the sole
producer; run no OCR or unbounded search and build serially only after real
edits.

## Successor checkpoint: use this printed-p.133 cursor

Printed p.132 is complete and validated. French `source/ega1/ega1-5-fr.tex`
is 19,923 bytes / 442 lines / SHA-256
`EE969AFC8501A89A9D5A079E7A9503FD2D355E89C557F97D50825C806D2A0FAC`,
through diagram (5.3.5.1) in Proposition 5.3.5. Truncation to the first 16,480
UTF-8 bytes reproduces sealed p.131 at SHA-256
`C6F64E7AD05183672B3F709BE452A0EA0EA3D5013030AE0A03792D3D0B85B6EA`.
The unique terminal `\end{proposition}` is a temporary bounded close.

Preserve the printed omission `f:X→S, Y→S` in French. English retains the
required `g:Y→S` with a visible note, and its former visible 5.3.3 stray period
has been replaced by a non-rendering anchor. R70 is the active 127-file gate:
manifest SHA-256
`18F2EF15DF53015AE384D8CD148FBF4D8B378A82C5CE0A90F6FA398D0DF2B952`,
tree SHA-256
`49B83F1B0ED89440DCC3759038AC626EED7C2C869766D1D6D1E55B07E448F210`,
and PASS validation SHA-256
`9218CF601B450135DB63656B3E6A66E638FF33368792BA6C0F5A7B50FF71D740`.
R55 combined validation is PASS/errors empty at SHA-256
`C97366E68C0A41EF8D55E74D17F01A661A274F7850BB9EE24C897D1F67996C7A`.
The p.132 pre-Stacks block is present at SHA-256
`EB95123847A5B6B08D50C20ECF0857D31E0D3E3599D15153FECEF8EEC3E58E82`.

Next cursor: first remove only the temporary final `\end{proposition}` from
`source/ega1/ega1-5-fr.tex`, then continue from direct NUMDAM PDF one-based
p.132 / printed p.133 authority with `est commutatif`. Reuse an existing exact
witness first; otherwise create one bounded context image only. Keep source,
mathematics, translation, semantic, and visual judgment with the sole
producer; run no OCR or unbounded search and build serially only after real
edits.

## Successor checkpoint: use this printed-p.134 cursor

Printed p.133 is complete and validated. French `source/ega1/ega1-5-fr.tex`
is 23,519 bytes / 538 lines / SHA-256
`DC5D2863A197CE33C9AAC314696ABDD36E840183D8DA735ACE6E99613A60FB91`,
through Corollary 5.3.11 and exact terminal sentence `C'est le cas particulier
du cor. (5.3.10) où l'on remplace S par Y et T par S (cf. (5.3.7)).` No
temporary close remains. Replacing the p.133 marker-to-EOF suffix with the
18-byte temporary p.132 close reproduces sealed p.132 exactly.

Preserve the printed “one element” wording for `X(Z)_Y` in Proposition 5.3.8.
English retains the mathematically correct “at most one element” with a
visible note disclosing the French. R72 is the active 127-file gate: manifest
SHA-256
`1942000C1077F279EC63EE894E15F0830C925753E3ADC0A5E18370B3DF948C2A`,
tree SHA-256
`29EB38A85D6F0DEC1644A9B2C4AA2A52D7185A83875E115B6AD0C44C627F9D37`,
and PASS validation SHA-256
`4B637E88F650B3479D9F6545361D7895A4B0145BEE9B81425826C64387595C21`.
R56 combined validation is PASS/errors empty at SHA-256
`025D9BB49D0B2305199EBE54D56822E6CE7E4E38E4AAA93819EC67A560CCB091`.
The p.133 pre-Stacks block is present at SHA-256
`B95A07D25C9773FE9AC06725E4B9833A9E8851EFA9328F76ED8739EF0994EA44`.

Next cursor: append directly to `source/ega1/ega1-5-fr.tex` from direct
NUMDAM PDF one-based p.133 / printed p.134 authority, beginning the graph
terminology after Corollary 5.3.11. Do not remove a closing environment first.
Reuse an existing exact witness first; otherwise create one bounded context
image only. Keep source, mathematics, translation, semantic, and visual
judgment with the sole producer; run no OCR or unbounded search and build
serially only after real edits.

## Successor checkpoint: use this printed-p.135 cursor

Printed p.134 is sealed from direct NUMDAM PDF one-based p.133 through
“z in Delta_Y(Y) intersect p_1^{-1}(X), on a z=Delta_Y(y)”, inside the proof
of Corollary 5.3.16. Current French source/ega1/ega1-5-fr.tex is 27,093
bytes / 629 lines / SHA-256
2BF15FE97B29DE032BB338E83897243673A7CC9C5956049AB1A29E195281DC2F;
there is no temporary close.

English R73/R74 are exact zero-delta 127-file manifests. R74 is 48,428 bytes /
SHA-256
E4A8F263163EE68710CC572F81E63E7A0DBAFC72B728985D2E6519CF27F86D9D
with tree SHA-256
29EB38A85D6F0DEC1644A9B2C4AA2A52D7185A83875E115B6AD0C44C627F9D37.
English R74 validation is PASS at SHA-256
E153071E1444563D15BDF45A440C05A9441CF325D534E04654DDBCB0F2867B34;
French R57 is PASS/errors empty at SHA-256
26FAB757B306D0046E7169404721530AF65A9308A23A95CA37A138DB4931E3CC.
Bounded French and English PDFs are respectively SHA-256
1DD0BA9C886D8C3BAFDC8AC3504848B5F180EAAFEC63FF9C2ECD820F1585A052
and
629DF4EF410D01F22290444C82BDD350AB8399D2BD108772E973F5469C968F73;
terminal QA passes. The p.134 scaffold is SHA-256
C2697E538722F21711C2833A524D689CD084E6F283E058AB37FB1AD40BAB5EA3.

First create and replay the complete R75 English pre-edit manifest. Then use
direct NUMDAM PDF one-based p.134 / printed p.135 and append the continuation
after z=Delta_Y(y) to source/ega1/ega1-5-fr.tex. Do not remove a closing
environment first. Continue sequentially and RAM-light: no OCR, unbounded
search, batch rendering/building, whole-page original-detail load, or
delegated source/math/translation/semantic/visual judgment. Treat
[PRIVATE_DOCUMENTS_ROOT]\CHat translates and clean as the moved unrelated
tree and do not recurse its former Papors\Chatnotes location.

### Correction bound before continuing printed p.135

The p.134 English page-25 150-dpi QA raster is retained, not ephemeral:
259,908 bytes / SHA-256
390A1151EB9A661083D57C67CD880C7A98326BD95912165C6006E5E8871324DD.
The visual result and all source/build bytes are unchanged. Use corrected
English R74 SHA-256
70EE5C3DF4C68F4549EF55E7D6C572998706C32572288653D75932BA50042B7A,
corrected French R57 SHA-256
AA264ADF86D4AF5B1A1BE075DC5293920009B08E57C8218993865E958BF9EC18,
and final 25-row p.134 workflow SHA-256
280759893633110B6019F6D6E65E025BB44573CE099380B64B2E4DECF9C24C65.

## Successor checkpoint: use this printed-p.136 cursor

Printed p.135 is sealed through Corollary 5.4.4 and its proof. Current French
source/ega1/ega1-5-fr.tex is 30,547 bytes / 718 lines / SHA-256
E1DBCD8A7DEF99161EE00A439D8BC4C1144D57B79DAB4853B0BDC80716B350F5;
there is no temporary close. English R76 is a zero-delta successor of R75:
127 files / 7,281,655 bytes, manifest SHA-256
67192F831823DB9C25E6951DF7CFB69A69C81422CF594EE33C84C3B3ACB386E3.

English R76 validation is PASS at SHA-256
A344A70C00EBEE10693A5B7CF9AE38CBF9A6E69B6F5914DD4CC69DF913D61398;
French R58 is PASS/errors empty at SHA-256
A170A999DBA4BB832A693D406172FF83398FC61413A922C455CC84DC25321C10.
Bounded French and English PDFs are respectively SHA-256
EECC102968EB25B18C92A369BFCB5350FCB35B4E1651F00F2BA28BA14CF81BA2
and
AB575233DAD6613B4CBFD411C085443EDDDB10967D13D9E2A28996099A2293FE.
The p.135 scaffold is SHA-256
9545858861D9E506F65069F7E65FCD0403D29C78A7DAC4D6A7A7AFE56348E183.

First create and replay complete R77. Then use direct NUMDAM PDF one-based
p.135 / printed p.136 and append Corollary 5.4.5 onward to
source/ega1/ega1-5-fr.tex. Do not remove a closing environment first. Keep
the moved unrelated tree at [PRIVATE_DOCUMENTS_ROOT]\CHat translates and
clean and do not recurse its former Papors\Chatnotes location.

## Successor checkpoint: use this printed-p.137 cursor

Printed p.136 is sealed through Corollaries 5.4.5--5.4.7, Remark 5.4.8,
all six clauses of Proposition 5.5.1, and its proof through the exact terminal
words ce qui. Current French source/ega1/ega1-5-fr.tex is 34,221 bytes / 810
lines / SHA-256
E025EFA76D8F9C9BBDA04042337FA59D653F93E403AAB5FD3BC287F2712FDE67;
there is no temporary close. Its exact inverse is truncation to the first
30,547 bytes, restoring p.135 SHA-256
E1DBCD8A7DEF99161EE00A439D8BC4C1144D57B79DAB4853B0BDC80716B350F5.

English R78 is the zero-delta successor of complete pre-edit R77: 127 files /
7,281,655 bytes, manifest SHA-256
803A294EC3F3CF1EFBC42ED8C3CDEE057FF2DA8142483676ED5B2E0B74F85F7B.
English R78 validation is PASS/errors empty at SHA-256
2877803FF2CE1394874B34E53E7F5734EA3071E63E78CA26D81CB78720559127;
French R59 is PASS/errors empty at SHA-256
0B7EFF6AC3741D1FB7B4CF326CCAC9872C6E4EC6FBFD5C83D6F0FA9A54651A9C.
Bounded French and English PDFs are respectively SHA-256
2616D0F29294FF83B73C6BEF0B27728B8C8D5EF1633D3ED0B5DA84EEAEBB6C42
and
1E4A283AC89786A08A3DC0B5AB5C979D783490E0A4DA47DD2FDBA888F777E5B8.
The p.136 scaffold is SHA-256
908D82E0E7063B91CFDE8C2765AD49F7DA2A9B60E5F8E782A4B1C0A697FE1DA2.

First create and independently replay complete R79. Then use direct NUMDAM
PDF one-based p.136 / printed p.137 and continue the proof after ce qui. Do
not remove a closing environment first. Continue sequentially and RAM-light;
do not recurse the former Papors\Chatnotes tree.

## Successor checkpoint: use this printed-p.138 cursor

Printed p.137 is sealed through the completion of Proposition 5.5.1,
Corollaries 5.5.2--5.5.3, Proposition 5.5.4 and its proof, and the terminal
irreducible-component reduction. Current French source/ega1/ega1-5-fr.tex is
38,044 bytes / 889 lines / SHA-256
9F316E9901A7DC8F069853E0DC3A9061FA49779CB59CE2016CFF95B2D11FD4BE;
there is no temporary close. Its exact inverse is truncation to the first
34,221 bytes, restoring p.136 SHA-256
E025EFA76D8F9C9BBDA04042337FA59D653F93E403AAB5FD3BC287F2712FDE67.

The paired English source has three p.137 fidelity repairs and is 47,345
bytes / SHA-256
BE2123101A28F8BEB6BBB5B32FC09CCA17F1B01BA491C9799229D9810B89BE2E.
Three exact inverse replacements restore the R79-gated 47,337-byte source at
SHA-256
520D28FBEE094AFC930E09D6A27ED8257D4E4F802FAAE0E2C5135F8F8641D798.
R80 is the one-row successor: 127 files / 7,281,663 bytes, manifest SHA-256
1ECABBC856950C7EDB083D9FA502DBF86F68B56D74C2AB84F6AE460704D93F7B,
tree SHA-256
E179D8E2393A34B50CA89B4C26616FE685F0A96FE74F5F91B20A921689CA3FFB.

English R80 validation is PASS/errors empty at SHA-256
4034C5B336955026E9210E7D2FD3EFC5EBF4A8FA4C93C68BF45FFD4B119AA93C;
French R60 is PASS/errors empty at SHA-256
A91D65AB7FCA43D68A6AF62301105872ED5A61EDC938B98BDFE2C50DE694B999.
Bounded French and English PDFs are respectively SHA-256
480AA13E0D0694556D4AA2FA5025754F421513D62B8581D44C08276CD68B87F4
and
2A041B3BAD2EB9F64BE88FE8A4E9F5B3A881FADC84FD53AA4ED894B360B37B62.
The p.137 scaffold is SHA-256
248460C70D5B42F30E254761EC31C30F9F3AD6EFAFDFC41C768AEC50581D10C6;
the final 20-row workflow ledger is SHA-256
C07847BA8242D286A7303249DAF56E85DFC3070623A633AFB56330819CD9663C.

First create and independently replay complete R81. Then use direct NUMDAM
PDF one-based p.137 / printed p.138, beginning Proposition 5.5.5, and append
to source/ega1/ega1-5-fr.tex. Do not remove a closing environment first.
Continue sequentially and RAM-light; use only named EGA roots and do not
recurse the moved unrelated tree or its former Papors\Chatnotes location.

## Printed-p.140 control-identity successor

The first five-file receipt pass placed the complete French STATUS p.140
block before an existing p.139 successor because a repeated append anchor was
matched. Historical blocks remain untouched; a terminal French STATUS
successor now controls. No source, manifest row, build, scaffold, or decision
ledger changed.

Final workflow ledger: 20,658 bytes / 27 parse-clean unique-ID rows / SHA-256
E58DBC28BE8369CA3649CC4E106825206A8517970B3EC221134216B0B9CA5A0E.
Final English R86 validator: 14,728 bytes / 315 lines / SHA-256
09041AA2A2E206C09256857D4A9A6447E0EF6322D8FD6CB9A4524FA2D4EB5F23.
Final French R63 validator: 15,819 bytes / 329 lines / SHA-256
730E1C8D71CF9F063349CE6797D0C4F3966615A45E2BF66F8D957F3E7E4E9FCD.

Cursor remains R87 first, then direct NUMDAM PDF one-based p.140 / printed
p.141 after `Tout sous-$\mathscr{O}_X$-`; no French close must be removed.

## Successor checkpoint: use this printed-p.139 cursor

Printed p.138 is sealed from Proposition 5.5.5 through the opening proof of
Proposition 5.5.10, ending exactly at “s'identifie à l'espace sous-jacent
au”. French source/ega1/ega1-5-fr.tex is 42,953 bytes / 1,003 lines /
SHA-256
2619437E655E33F819B8A965B48F8DA2D9B0F6890A0E9314EA285D8C99DF87CB;
there is no temporary close. Its exact inverse is truncation to the first
38,044 bytes, restoring p.137 SHA-256
9F316E9901A7DC8F069853E0DC3A9061FA49779CB59CE2016CFF95B2D11FD4BE.

The paired English source has four p.138 fidelity repairs and is 47,354
bytes / SHA-256
29761A8C85CC1608E3EC80A7397B0847306F8A5F8C61AEA4772E1C79A3E493E3.
Four exact inverse replacements restore the R81-gated 47,345-byte source at
SHA-256
BE2123101A28F8BEB6BBB5B32FC09CCA17F1B01BA491C9799229D9810B89BE2E.
R82 is the one-row successor: 127 files / 7,281,672 bytes, manifest SHA-256
CE696DDADDBAD9D41D2086BC0B849F9D57531BA086B77826DC1FA0F0BFA771F9,
tree SHA-256
863DC6BD6E3C752E94DDA9B58EEBD8AE9378CF64B525F663359EFDAE146E85CD.

English R82 validation is PASS/errors empty at SHA-256
9B73FA281982CBC243DDEA33272650265A40A64E1FF7FBB18D217D9C63F4E58A;
French R61 is PASS/errors empty at SHA-256
61DEE7FD8760F32CF965CB8D10E85FC4572B766ADCDFC16978EA297FCFA22E73.
Bounded French and English PDFs are respectively SHA-256
96E1279700FDCBEFFC38E7E1E28A28D6CA9C4F08BB9B87A3D1BD7C91B8FD2687
and
1B4A7532D8DF1C832CBE61249EF6395CC36A3EEFEA1C1C886472ECA62D0297C4.
The p.138 scaffold is SHA-256
1B024552FFE71D56EB1BB2BA50304961073B55B0CEE76D5F514EDDFB65D49BB4;
the final 22-row workflow ledger is SHA-256
A1FFA5B192BE640F4BE13E876823E1F255AF2CF1E0560DCB3B89DA76D8EEB7C4.
This terminal checkpoint supersedes any stale later p.130--p.136 receipt
cursor while preserving every append-only historical entry.

First create and independently replay complete R83. Then use direct NUMDAM
PDF one-based p.138 / printed p.139 and continue the proof of Proposition
5.5.10 in source/ega1/ega1-5-fr.tex. Do not remove a closing environment
first. Continue sequentially and RAM-light; use only the named EGA roots and
do not recurse the moved unrelated tree or its former Papors\Chatnotes
location.

## Successor checkpoint: use this printed-p.140 cursor

Printed p.139 is sealed from the completion of Proposition 5.5.10 through
Examples 5.5.11 and Remark 5.5.12 clauses (i)--(iii), ending exactly at
“possède la propriété P.” French source/ega1/ega1-5-fr.tex is 47,116 bytes /
1,076 lines / SHA-256
D8168125192DF12B1765D4F81E8DD2A15D37378370454F4370E0A3F18C3BC055.
Its exact inverse is truncation to the first 42,953 bytes, restoring p.138
SHA-256
2619437E655E33F819B8A965B48F8DA2D9B0F6890A0E9314EA285D8C99DF87CB.
The remark and its enumerate remain intentionally open; there is no temporary
French close to remove.

The printed doubled-origin ideal (0) error is preserved in French and
catalogued. Paired English visibly corrects both ideal tokens to (s) with a
translator note, restores singular neither-agreement, and restores the exact
negative quantifier for the doubled affine plane. English source is 47,538
bytes / SHA-256
E4E6D19A7C19B69E61CBBE8792DB0EED1AD6DAA0DD559E61811057F11641651C;
three exact inverse replacements restore R83 SHA-256
29761A8C85CC1608E3EC80A7397B0847306F8A5F8C61AEA4772E1C79A3E493E3.

R84 is the one-row successor: 127 files / 7,281,856 bytes, manifest SHA-256
4C4EF213763A4E9838AF2E8E23A89C8DB0FC45DEBEA0DA078908BED01EA6CFB8,
tree SHA-256
3DD3F9B92DBC78C7334C1F194836E9F4181DF2FE87A8A3905D64947F51576F6C.
English R84 validation is PASS/errors empty at SHA-256
1BBFC3699FA46963B0818E655DC8A52D11BE53D8A81B2A0772E2ABB19EB551AE;
French R62 is PASS/errors empty at SHA-256
6463BC1513088A20797B180C252BE4AFD7B609B260B525C958C237CD382B27CE.

Bounded French and English PDFs are respectively SHA-256
47E016E105621346051731757945D7110492D3D25F34C1DCE93CBC08896DAB07
and
D9DCC6A8D435A42A762FCE1B60E465873540FBCE8487DDAAB1ACB7353FB505CC.
The p.139 scaffold is SHA-256
BE3FB4F09303AAF6D12C972D38D1590E94201A6952223A35BD32A9CECADA282B;
the final 24-row workflow ledger is SHA-256
02D0EEEB094CDBB8DD974883E2A5D124FBB123A2EF8BF70B5C4A598425639327.
This terminal checkpoint supersedes every older receipt cursor while
preserving all append-only evidence.

First create and independently replay complete R85. Then use direct NUMDAM
PDF one-based p.139 / printed p.140, beginning Remark 5.5.12 clause (iv), and
append to source/ega1/ega1-5-fr.tex. Do not place or remove a temporary French
source close. Continue sequentially and RAM-light; use only the named EGA
roots and do not recurse the moved unrelated tree or its former
Papors\Chatnotes location.

## Successor checkpoint: use this printed-p.141 cursor

Printed p.140 is sealed through the exact French terminal fragment
`Tout sous-$\mathscr{O}_X$-`. French source/ega1/ega1-5-fr.tex is 50,232
bytes / SHA-256
4610C5F9E732D99948AA809ED64C85D236423990C2750A06F0DC7A805D317701;
truncation to 47,116 bytes restores sealed p.139 at SHA-256
D8168125192DF12B1765D4F81E8DD2A15D37378370454F4370E0A3F18C3BC055.
The new section-6 file source/ega1/ega1-6-fr.tex is 694 bytes / SHA-256
0292AFD987807F3045A61D94F56A2344684A539439013DE19091181E369F859F
and is reversible by hash-guarded removal. All environments are balanced;
there is no temporary French close.

The direct-authority crop rejected an inherited English comma after the
reduction square's bottom-right Y. Final French has no comma; the superseded
comma-bearing source and first build remain recorded. Paired English changes
no source and retains three explicit normalizations: reordered page-boundary
placement, Noetherian capitalization, and its comma as English sentence
punctuation. R86 has 127 files / 7,281,856 bytes, manifest SHA-256
1AACEE47C3D247A51FAC9790F44B8B4291AD670DB299986CEC6F056638063F8B,
and unchanged ordinal tree SHA-256
3DD3F9B92DBC78C7334C1F194836E9F4181DF2FE87A8A3905D64947F51576F6C.

Final French and English bounded PDFs are respectively SHA-256
3952A572810DD80868F84C80C4FDD3165C538F1F27576546D2C87AD9F0E887F6
and
29AA995989C8EED0293505EEBF32CFDA4C40C4743C443B041C1566CA5ECBF267.
The current p.140 scaffold is SHA-256
42B41EE3099E81D8D32B59ED957F1790EFBF83BC1BC09F535B5D53D04CC0CD32;
the final 26-row workflow ledger is SHA-256
738585AFF1AE7363E113DB039FC29859E1FDECE29EC51F24B73652E42E856CDD.
English R86 validation is PASS/errors empty at SHA-256
0CA69172635D18391445CD58E9186CD96F0428B505D4A1602C8E31C93B094DF9;
French R63 is PASS/errors empty at SHA-256
947BF36318ABA08B46674E6C94D49078651B817BAFE1C53DB059CE9F1109FDD6.
This terminal checkpoint supersedes every older cursor while preserving all
append-only and superseded evidence.

First create and independently replay complete R87. Then use direct NUMDAM
PDF one-based p.140 / printed p.141 and continue the sentence in
source/ega1/ega1-6-fr.tex after `Tout sous-$\mathscr{O}_X$-`, placing the
p.141 marker at the true continuation. Do not remove a closing environment
first. Continue sequentially and RAM-light in the two live EGA roots; do not
recurse the moved unrelated tree or its former Papors\Chatnotes location.

## Final printed-p.140 control-identity successor

This append follows the unique terminal R87/p.141 cursor. Earlier misplaced
identity blocks remain visible; no source/build/index byte changed. Final
workflow ledger is 23,071 bytes / 29 parse-clean unique-ID rows / SHA-256
A736395707953F046D095A6A6F2EF4CB856F752F5045A1714260B32295C5E1D0.
Final English R86 validation is PASS/errors empty at 14,728 bytes / 315 lines
/ SHA-256
17324EC59ECCC5E0E9B9C5905190B841435EE7C07F5C485665E765215FE6F4DC;
final French R63 is PASS/errors empty at 15,819 bytes / 329 lines / SHA-256
3D8088D1C25BD1925B80083CF44618FE2CDEACFF2C254E09FCCD792FD9C75235.
Cursor remains: create/replay R87, then direct NUMDAM PDF one-based p.140 /
printed p.141 after `Tout sous-$\mathscr{O}_X$-`; remove no French close.

## Final printed-p.141 control-identity successor

Printed p.141 is sealed through the exact finite-$D(f_i)$-cover semicolon in
the open proof of Proposition 6.1.4. French source/ega1/ega1-6-fr.tex is
5,074 bytes / SHA-256
75A77003BDC90E8F0809F0DBF324A1F45268BC7A39C557D5A78C62816168B95B;
its exact inverse restores sealed p.140 SHA-256
0292AFD987807F3045A61D94F56A2344684A539439013DE19091181E369F859F.

Paired English source/ega1/ega1-6.tex is 54,737 bytes / SHA-256
BA45F1965B6085D84CA7E3723E4078039093ACFDDD916FD191AD43DE251CA980.
Its precision repair restores increasing, citation 1.3.7, and canonical
equivalence; its structural repair restores oldpage 142. R88 manifest and
tree SHA-256 values are
76E4ACFF554773770EBC1C53C87E02A3F4CC54D3EA8CE81898DA6D5B9BF9B0E6
and
5AAE163319428FB1DDB52411C7F5CAB6AFA90235FB32C7ADE2AFD6203E6D4C25.

French PDF, English PDF, and p.141 scaffold SHA-256 values are
833844565C2D05E098455F36DF403B2438671716B32E30E0F48F52374C070C1D,
B0802C9A4F68EA07E9EA785330C8722956B91FD74F408274E8F772CA81DCED65,
and
E5BCB61BB2C8CBF65B628253E62B2F5579D9821C15078BFF25A12880ADDDC689.
Final workflow, English validator, and French validator SHA-256 values are
8744745815106FA65635512D34E1EA9DC3C93090735583DF2247F200600DA90F,
288BC03CD1D8E9DB2B291B9CA7369DD8670A9D912C0C70EBE2FCE126F4C8F529,
and
027E1BB4FC646376CAC767DCFA08933C86AE657719BAAA99A8DBF68A6DF6CAF7.

Create and replay complete R89 before any p.142 English mutation. Then
continue direct NUMDAM PDF one-based p.141 / printed p.142 in the already-open
proof, placing oldpage 142 at the true French continuation. No temporary
French close exists to remove.
