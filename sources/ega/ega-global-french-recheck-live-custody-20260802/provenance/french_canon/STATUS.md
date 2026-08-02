# Status

Date: 2026-08-02

Status: ACTIVE — canonical French source transcription.

Authority closure: eight NUMDAM PDFs, 1,800 physical PDF pages total; exact
identities are in `controls/AUTHORITY_SHA256.csv`.

Current production volume: EGA I.

## Controlling quick status — 2026-08-02, through printed p.75 / 7.6.18

This block supersedes all older point-in-time quick-status blocks below; they
remain append-only history.

- The admitted diplomatic French source is complete through paragraph
  7.6.15, Proposition 7.6.16 and proof, Proposition 7.6.17 and proof, and
  Corollary 7.6.18 and proof on EGA I printed pp.74--75. Section 7.7 and
  paragraph 7.7.1 are wholly unadmitted.
- source/ega1/ega0-1-fr.tex: 270,458 bytes / 5,726 lines / SHA-256
  CBE2C566A9DE9366F3F5859AD2563C7EFCB36FA9DAC9A17C7DE73186692ADBB8.
- Exact next cursor: the section 7.7 heading and paragraph 7.7.1 on printed
  p.75, continuing onto p.76. No section-7.7 text is admitted.
- Direct-authority evidence:
  controls/EGA1_PRINTED74_75_SECTION7615_7618_DIRECT_AUTHORITY_IMAGES.json,
  2,993 bytes / SHA-256
  A5623387606C16D2DC3360971781F36E8D5BDF65FA70CD8C41D55636C8F39675.
  It binds the direct 5,000-dpi p.74 continuation band and four overlapping
  direct 5,000-dpi p.75 bands. The lead personally read every admitted line;
  extraction remained locator material only. The p.75 bands are grayscale to
  avoid unnecessary memory pressure while retaining the full source detail.
- The controlling bounded French reader is
  qa/ega1_chapter0_build/ega0-pages11-75-through-7618-check-r58.pdf, 59 A4
  pages / 399,323 bytes / SHA-256
  4C9F136C4A8C5DBDF939F4B0A0B4A68530BA52C9BAD8BD15669C968EC863ABF8.
  Three serialized XeLaTeX passes exit 0; passes 2 and 3 are byte-identical,
  14,908 bytes / SHA-256
  80DD0813E039BF798BB7C400D0D042F752E5D214E05DF4FD70D9E6D9F9E1A16F.
  Hard, undefined, reference, multiply-defined, duplicate-destination,
  missing-character, fatal, rerun, and overfull diagnostics are zero. The sole
  underfull line predates this batch. Output pages 58 and 59 were rendered at
  1,200 dpi and personally inspected: SHA-256
  2575AF72F7837C76C2DBF7EB62925E5844ACA80A59B8A6536E71D8332CACB193
  and 470E6D0DA9B50B3B27CF8DCF2D57F5F7A433EFF1EB3F839ABB5917E45D9E062B.
  The p.74/p.75 seam, theorem typography, localization exponents and
  subscripts, inverse formula, line flow, clipping, and page envelope pass.
- Three new inherited-English dispositions are individually justified in
  controls/ENGLISH_CORRECTION_RECHECK_APPEND_P75_20260802.jsonl, three rows /
  4,464 bytes / SHA-256
  8FEEADF8588E430401C865293AE55DE34B9A73CC61894140FE475674183F2D52.
  They normalize the technical relation flat over, restore the finite copula
  in the assertion that A_{S} is local, and replace the nonidiomatic “we know
  from before” by the source-faithful “we already know.” The third is logged
  explicitly as a register normalization without semantic change.
- Repair events are append-only in
  controls/ENGLISH_CORRECTION_REPAIR_APPLICATION_P75_20260802.jsonl, three
  rows / 3,047 bytes / SHA-256
  A2623653DFAB44EAB81F4657A05328BF283B1E77F8F35EB6D77E294FDD206CAC.
- Current English changed source: source/ega0/ega0-7.tex, 75,432 bytes /
  SHA-256
  81196521B4A963CFD614452C63C1669482B4C58A6A2E250DD593B1B11159F036.
  controls/SOURCE_INPUT_SHA256_R9.json, 24,485 bytes / SHA-256
  203A7E34F3BC5683E4612DA4300358B4A5DD295EA2781454811EB2C15A38B05D,
  replays 127/127 rows, 7,280,020 bytes, and ordinal tree SHA-256
  B20246760E9A19F7050C457EC91697105B6CB255FBBDDEFF15DD0718716698AE
  under independent Python and PowerShell ordinal implementations.
  controls/SOURCE_DIFF_VALIDATION_R9.json, 5,421 bytes / SHA-256
  40AC5CDB5B686B5468DCD67B26BD9C5BFCA329D080D0FC696181AAE6DF6E9C90,
  and its 2,556-byte replay SHA-256
  0C984F40AA06735D214D7E3264FD7C5DC3C5AF1FFE5EEFACF2E0CE4C9A84A8AA
  both pass with errors empty. Exact inverse reconstruction of the three-line
  patch reproduces the prior R8 source hash, so all 26 earlier assertions
  remain bound; the six new required/obsolete assertions also pass.
- The complete decision surface is now 147 rows. Twenty-six cumulative
  English repairs are applied; four source-faithful no-edit decisions remain.
  No admitted English source-correction judgment has been reversed.
- One lead-authored encoding mistake is append-only in
  controls/WORKFLOW_ERROR_APPEND_P75_20260802.jsonl, one row / 1,003 bytes /
  SHA-256
  A95844DDAA237547B777E1EE745AD24AE5F39347D84BFF9DBEB3CBCB0005F51B.
  A patch-string escape briefly produced an exponent with a comma; immediate
  source-line replay caught it before build or admission, and the source was
  repaired to the exact printed exponent.
- Corpus-scale progress is 72 source-bearing pages admitted out of 1,800
  physical pages (4.0%); approximately 1,728 physical pages remain.
- Global reader rebuild, reference-coordinate replay, privacy-clean
  projection, rights/caveat and package gates, explicit archive handoff,
  dual-DOI logbook binding, and public readback remain pending. No GitHub or
  Zenodo mutation has occurred from this mutable successor.

## Controlling quick status — 2026-08-02, through printed p.74 / 7.6.14

This block supersedes all older point-in-time quick-status blocks below; they
remain append-only history.

- The admitted diplomatic French source is complete through Corollary 7.6.14
  and its proof on EGA I printed p.74. Proposition 7.6.10 includes its exact
  p.73/p.74 seam. Section 7.6.15 is wholly unadmitted.
- source/ega1/ega0-1-fr.tex: 266,060 bytes / 5,641 lines / SHA-256
  C5D6E1F1367641E914C184892DEBDABF3B0EDDF2E2F2BD167835CD7430343A7D.
- Exact next cursor: 7.6.15 on printed p.74, continuing onto p.75. No 7.6.15
  text has been admitted.
- Direct-authority evidence is split append-only by source batch:
  - controls/EGA1_PRINTED73_PROP764_7610_DIRECT_AUTHORITY_IMAGES.json,
    3,354 bytes / SHA-256
    8DCD975AEC1239EC200674C02ABB201C39377A0FE3848B56BBD8CDBB7B6F9849;
  - controls/EGA1_PRINTED74_PROP7611_7614_DIRECT_AUTHORITY_IMAGES.json,
    2,650 bytes / SHA-256
    0C4CEC360787E787DB968EB8CAF6DB919BC9BAFF572790DF8843EC35B9EAC7B4.
  Together they bind ten direct 5,000-dpi p.73--p.74 bands plus one direct
  5,000-dpi p.74 seam band and one 1,400-dpi navigation page. The lead
  personally read every admitted line from the 5,000-dpi bands; OCR and
  extraction remained locator material only.
- The controlling bounded French reader is
  qa/ega1_chapter0_build/ega0-pages11-74-through-7614-check-r57.pdf, 59 A4
  pages / 394,596 bytes / SHA-256
  BE505741832275CA07930B1C931F23094C74F8A2EAD8003628D95E4927A3837D.
  Three serialized XeLaTeX passes exit 0; passes 2 and 3 are byte-identical,
  15,210 bytes / SHA-256
  A179DD91DFD948C44E01AA60199EA05F20AF7CE8293E10C9BB196DCB7745C458.
  Hard, undefined, reference, multiply-defined, duplicate-destination,
  missing-character, fatal, and overfull diagnostics are zero. The sole
  underfull line predates this batch. Output pages 58 and 59 were rendered at
  1,200 dpi and personally inspected: SHA-256
  2444183C9E2AA198B793B92A820FB3CF271281CB184392059D684407D5895802 and
  34C744C4C081EFA867767747CED6F2A1F0CEEC2E6B9502D2459046874E7B13BC.
  Page seams, theorem/item typography, formula exponents and primes, clipping,
  and page envelopes pass.
- Six new English/source dispositions are individually justified:
  - controls/ENGLISH_CORRECTION_RECHECK_APPEND_P73_20260802.jsonl, four
    records / 5,321 bytes / SHA-256
    E1438205B716BF612974FDDCB0E996DB69F08084FB30B0AE951839BF4F6D6E48;
  - controls/ENGLISH_CORRECTION_RECHECK_APPEND_P74_20260802.jsonl, two
    records / 2,939 bytes / SHA-256
    3F6280B1A1ED8E663597081ABC0F23FBEEDA199D348369CFC1E22F39F746F41B.
  The repairs restore topological adherence in 7.6.4, singular agreement and
  the correct unit quantifier in 7.6.6, the missing inverse exponent in
  7.6.13, and the contextually forced 7.6.11 closing locator. The printed
  French 7.2.8 typo remains exact in the diplomatic source; English exposes it
  in an immediate note.
- Repair events are append-only in the P73 and P74 repair-application JSONL
  files: four records / SHA-256
  BAFB5569FED2135065F3807BF0FCE094886F14723A3B18C9536E13BDC125680B,
  and two records / SHA-256
  F3A407E38723F125B98DB9DD147BA04757C07E756F82ABE2E60ACC603C4E2CD0.
- Current English changed source: source/ega0/ega0-7.tex, 75,427 bytes /
  SHA-256
  3A7611B105182E45AA33C945C85E34A48A2C46369568A686F7E6F73810D54AA7.
  controls/SOURCE_INPUT_SHA256_R8.json, 24,222 bytes / SHA-256
  6087C82E314965389977E80D4E964EBB47AA2A205D699B1160B5455FB21AE851,
  replays 127/127 rows, 7,280,015 bytes, and ordinal tree SHA-256
  7A0E4D9FB6A352C04009029A692E3E9D133015ECBFBBF52005BEF95F0A6B5F1A
  under independent Python and PowerShell implementations.
  controls/SOURCE_DIFF_VALIDATION_R8.json, 5,055 bytes / SHA-256
  33F169EA742114018CA857D6391CEE89ECD9ABDB92B77AE79952EBC6D1731C32,
  and its 1,481-byte replay SHA-256
  0B6D72131B9918330D525A4932841A4D6244A709D4DFE4A88F9DB782E05D843C
  both pass with errors empty. R4's archive-reported stale diff binding is
  therefore superseded by exact R8 source-manifest and diff validation; all
  later release gates remain held.
- The complete decision surface is now 144 rows: the prior 138 plus six new
  source-bound records. Twenty-three cumulative English repairs are applied;
  four source-faithful no-edit decisions remain. No admitted English
  source-correction judgment has been reversed.
- One lead-authored workflow mistake is append-only in
  controls/WORKFLOW_ERROR_APPEND_P74_20260802.jsonl, one record / 1,027 bytes
  / SHA-256
  D34D6F0B0246D12038C7EBB403AEF62DA9A1A37119F6E24F093ECDAC7AD00DC9.
  R56 used an unsupported proof wrapper and failed on pass 1. The wrapper was
  removed without changing any source word or formula; R57 is the corrected
  controlling build.
- Corpus-scale progress is 71 source-bearing pages admitted out of 1,800
  physical pages (about 3.9%); approximately 1,729 physical pages remain.
- Global reader rebuild, reference-coordinate replay, privacy-clean
  projection, rights/caveat and package gates, explicit archive handoff,
  dual-DOI logbook binding, and public readback remain pending. No GitHub or
  Zenodo mutation has occurred from this mutable successor.

## Controlling quick status — 2026-08-02, through printed p.72 / 7.6.3

This block supersedes all older point-in-time quick-status blocks below; they
remain append-only history.

- The admitted diplomatic French source is complete through Proposition
  7.5.5, §7.6.1, Proposition 7.6.2 with proof, Corollary 7.6.3, and the
  terminal cautionary paragraph on EGA I printed p.72 / physical PDF page 71.
- source/ega1/ega0-1-fr.tex: 257,449 bytes / 5,463 lines / SHA-256
  2F511A63F9F13EDC8DB12A365731B392F2931ADE690290A09151A5DC4DD0A2A1.
- Exact next cursor: Corollary 7.6.4 on printed p.73. No p.73 text is
  admitted.
- Direct-authority evidence:
  controls/EGA1_PRINTED71_72_PROP755_763_DIRECT_AUTHORITY_IMAGES.json,
  3,483 bytes / SHA-256
  668DF770147CA68EC7EEA4D8A06D7B06BFBB9E684AAEFF85AA4427FBC4B4CA24.
  It binds seven direct 5,000-dpi reading bands across pp.71--72 plus one
  1,400-dpi p.72 navigation page. The lead personally read every admitted
  line from the 5,000-dpi bands; OCR/extracted text was locator material only.
- The controlling bounded French reader is
  qa/ega1_chapter0_build/ega0-pages11-72-through-763-check-r54.pdf, 57 A4
  pages / 385,147 bytes / SHA-256
  FAC9F2A96AFAB501D852E27FC3CB2873B0BC5504718E2ABFAB3EE576708B21F8.
  Three serialized XeLaTeX passes exit 0; passes 2 and 3 are byte-identical,
  15,194 bytes / SHA-256
  E5A74E816A209D8A140E714F197F0AFDF9DDDF2D37B51CA350A479CF2B4FCED2;
  final checked diagnostics are zero. Output page 56 is byte-identical to the
  already-inspected R53 page. Output page 57 was rendered at 1,200 dpi and
  personally inspected: 2,732,387 bytes / SHA-256
  B3B959464FB0AA9EFCB1A44E95A85C47E73A5BECD0B8F45B9B6D39B57BF0235B.
  The p.71/p.72 seam, projective-limit maps, completion formulas, proposition
  typography, section transition, clipping, and page envelope pass.
- Eight new English dispositions are individually justified in
  controls/ENGLISH_CORRECTION_RECHECK_APPEND_P71_P72_20260802.jsonl, eight
  records / 10,398 bytes / SHA-256
  502D5089998CE3BE4D69237730C99FE89F803FE3FED70CAEE521041DBA01F700.
  Five are inherited English errors now repaired: Notherian, and A-algebra,
  the broken quotient parenthesis/clause, this isomorphic, and the omitted
  kernel formula in 7.6.2. Three no-edit decisions justify the preserved
  B_n=B_m/... formula, idiomatic on A, and the standard term separated
  completion.
- Repair events are append-only in
  controls/ENGLISH_CORRECTION_REPAIR_APPLICATION_P71_P72_20260802.jsonl,
  five records / 4,314 bytes / SHA-256
  55655CBB9E63D509534923F04A35E9171B2F0DEFB79557515973A32FB8EDE513.
- Current English changed source: source/ega0/ega0-7.tex, 75,260 bytes /
  SHA-256
  C576296A78A1303323C7296A7CCF9B989FCA8FF7C2C8A981140F66651B17A747.
  controls/SOURCE_INPUT_SHA256_R6.json, 23,692 bytes / SHA-256
  C47C6AAD610A7FF3A15A54C5E3931C2E1E28A2D237D3D4D26FD845947C523B35,
  replays 127/127 rows, 7,279,848 bytes, and exact ordinal tree SHA-256
  0B11488A0F866FBF0AF5575AF6E6F77B322C08969BD9034821210EF2F47A00A7
  under independent Python and PowerShell implementations.
  controls/SOURCE_DIFF_VALIDATION_R6.json, 4,058 bytes / SHA-256
  9C210905CE159FED2B4CA6745CD5AAF3CC5F039502DC04FAD6805A44B7D34311,
  and its 1,356-byte replay SHA-256
  23BB830C291DC10C349DC825A49FE41F2F78F271D746E528F0FD6863C3C64D11
  both pass with errors empty. Global rebuild/public supersession remains
  pending; no frozen/public predecessor was mutated.
- The decision surface is now 138 individually bound records: 108 confirmed
  English errors, 22 French-source issues, two official erratum/addendum
  decisions, and three external additions. Thirty-one are formally
  source-justified. No admitted English source-correction judgment has been
  reversed.
- Two lead-authored workflow mistakes in this block are append-only in
  controls/WORKFLOW_ERROR_APPEND_P72_20260802.jsonl, two records / 1,825
  bytes / SHA-256
  C98159F5C93A3FB73E589E8191A56B898EC60CCBF2A7F7AE4A431DE9229A517C:
  the initially misplaced 7.5.5 block and an insufficient first line-break
  hint. Both were caught before admission; R54 contains the exact corrected
  source and a clean layout.
- Corpus-scale progress is 69 source-bearing pages admitted out of 1,800
  physical pages (about 3.8%); approximately 1,731 physical pages remain.
- Archive custody has acknowledged the dual-logbook-DOI rule under decision
  EG-ARCHIVE-DUAL-DOI-LOGBOOK-CUSTODY-CONTROL-20260802-0001. Methodology
  concept: 10.5281/zenodo.21124403; replication concept:
  10.5281/zenodo.20461174. Mutable EGA remains excluded and no upload has
  occurred.

## Controlling quick status — 2026-08-02, through printed p.71 / 7.5.4

This block supersedes all older point-in-time quick-status blocks below; they
remain append-only history.

- The admitted diplomatic French source is complete through Proposition 7.5.4
  and its proof on EGA I printed p.71 / physical PDF page 70. Proposition 7.5.5
  is wholly unadmitted.
- `source/ega1/ega0-1-fr.tex`: 251,121 bytes / 5,341 lines / SHA-256
  `52B886E42D7B2C904074DEC2725475D43519D95EC5D7A6C9BF94291B4B505561`.
- Exact next cursor: Proposition 7.5.5 on printed p.71; it continues on p.72.
- Direct-authority evidence:
  `controls/EGA1_PRINTED70_71_PROP754_DIRECT_AUTHORITY_IMAGES.json`, 2,663
  bytes / SHA-256
  `D4AC485571C2BA8DC4E2DE59664728D5488A29217B6E723825E198A399489C58`.
  It binds the direct 5,000-dpi p.70 terminal band and three overlapping
  direct 5,000-dpi p.71 bands. The 1,400-dpi p.71 page is navigation context
  only. The lead personally read every admitted line from the 5,000-dpi
  surface; OCR/extracted text was locator material only.
- The controlling bounded French reader is
  `qa/ega1_chapter0_build/ega0-pages11-71-through-754-check-r50.pdf`, 56 A4
  pages / 378,288 bytes / SHA-256
  `BA4E1BAA58FD8DE9DED8C48E6C6A7AE92898083CA770FC7590FE8655A84C3598`.
  Three correctly constructed serialized XeLaTeX passes exit 0; passes 2 and
  3 are byte-identical, 14,898 bytes / SHA-256
  `10BBD2479D4BCF451FB56E9E715653B145FDDBABF4704F607D72349E79E7C90B`;
  final checked diagnostics are zero. Output pages 54--56 were personally
  inspected at 1,200 dpi and pass the predecessor seam, printed-p.70/p.71
  seam, indices, powers, projective-system notation, theorem/proof typography,
  clipping, and page envelopes. Their exact PNG identities are respectively
  2,553,404 bytes / SHA-256
  `D6F6016CB439611906074ED996AE71461C660BD95650F28190DB05358033A9D3`,
  2,377,354 bytes / SHA-256
  `20C0956CAF24B7DDDE7743155806BEE3038BF3E07F07FBBD67F33DB043042F1D`,
  and 937,967 bytes / SHA-256
  `43D1CCF4F45E924BA6E46C950E0F9019AC620234103D65E6FA0DEC24DE7D58E4`.
- Four new inherited English errors are individually justified in
  `controls/ENGLISH_CORRECTION_RECHECK_APPEND_P71_20260802.jsonl`, four
  records / 5,116 bytes / SHA-256
  `99CF1649C8AB3128F57192C7D759907D6398DDEB071BDF8F232571A5C986518C`:
  missing primes on `u'_{0i}` and the kernel-use `u'_{ij}`, wrong product
  ideal subscript `i` for source `j`, and `Notherian` for `Noetherian`.
  All four repairs are applied in the complete copied English source
  successor. Repair events: four records / 3,424 bytes / SHA-256
  `E174622ECF18029DF74D0B2022D9DDD79B1C2C96A6BF33B6F7972A000FE3FDB0`.
- Current English changed source: `source/ega0/ega0-7.tex`, 75,199 bytes /
  SHA-256
  `8DD6840E73ADBE9D529AE39979B495BB7BC2D4CAFC8DE72C2F2EA870E46D1528`.
  `controls/SOURCE_INPUT_SHA256_R5.json`, 24,084 bytes / SHA-256
  `38E8BD3642A7CBDE07428D9D13447A75DBFD6AAEE0A8B2B682B9F989DEEDB61C`,
  independently replays 127/127 rows and exact ordinal tree SHA-256
  `30E8197C89FCE61EEB9ACAC82EE40985CB7C1B8F277FE627181B9C4195A8DCDA`.
  `controls/SOURCE_DIFF_VALIDATION_R5.json`, 4,489 bytes / SHA-256
  `F0987DB31A57930111FD97A551DC379E6D68AA5701FC93673E0C229FC5B3956E`,
  and its replay both pass with errors empty. Global rebuild/public
  supersession remains pending; no frozen/public predecessor was mutated.
- The decision surface is now 130 individually bound records: 103 confirmed
  English errors, 22 French-source issues, two official erratum/addendum
  decisions, and three external additions. Twenty-three are formally
  source-justified. No admitted English source-correction judgment has been
  reversed.
- Seven current-run workflow events are classified; six are lead-authored
  control/tool mistakes. The two p.71 events are the over-wide Cairo crop and
  a repeated PowerShell equals-form build-path quoting error, recorded in
  `controls/WORKFLOW_ERROR_APPEND_P71_20260802.jsonl`, two records / 1,426
  bytes / SHA-256
  `34A0C65B16136EE976CC18FEC12294B50FDBC991528A4341F900FF3B7A5A0042`.
  Neither changed any source byte.
- Corpus-scale progress is 68 source-bearing pages admitted out of 1,800
  physical pages (about 3.8%); approximately 1,732 physical pages remain.
- Archive custody has acknowledged the dual-logbook-DOI rule under decision
  `EG-ARCHIVE-DUAL-DOI-LOGBOOK-CUSTODY-CONTROL-20260802-0001`. Methodology
  concept: `10.5281/zenodo.21124403`; replication concept:
  `10.5281/zenodo.20461174`. Mutable EGA remains excluded and no upload has
  occurred.

## Controlling quick status — 2026-08-02, through printed p.70

This block supersedes all older point-in-time quick-status blocks below; they
remain append-only history.

- The admitted diplomatic French source is complete through numbered
  paragraph 7.5.3 on EGA I printed p.70 / physical PDF page 69. It includes
  the section-7.5 heading and complete 7.5.1 across the p.69/p.70 seam,
  followed by complete 7.5.2 and 7.5.3. Proposition 7.5.4 is wholly
  unadmitted.
- `source/ega1/ega0-1-fr.tex`: 248,060 bytes / 5,282 lines / SHA-256
  `7F7758B1F6891D1B58E40C240C74C3FD359D04614410948B8D3CAAA037A23F5E`.
- Exact next cursor: Proposition 7.5.4 at the bottom of printed p.70,
  continuing on p.71.
- The direct-authority evidence manifest is
  `controls/EGA1_PRINTED69_70_SECTION751_753_DIRECT_AUTHORITY_IMAGES.json`,
  3,841 bytes / SHA-256
  `5B7BC847AF9B6765D6C8C62C14A439B97B74DCBEFB186C2421E0B9F260DE90D7`.
  It binds one 1,400-dpi context page, one direct 5,000-dpi full page, five
  overlapping direct 5,000-dpi bands, and the targeted direct 9,000-dpi crop
  used to resolve the 7.5.2 bracket. The lead personally read the admitted
  scope from these direct authority images; OCR/extracted text was locator
  material only.
- The controlling bounded French reader is
  `qa/ega1_chapter0_build/ega0-pages11-70-through-753-check-r48.pdf`, 55 A4
  pages / 374,459 bytes / SHA-256
  `D2F0393B08389251626806CE801EE73D319EADB8F4D6A89D6240DB88930B6631`.
  Three serialized XeLaTeX passes exit 0; passes 2 and 3 have identical
  console SHA-256
  `9686CB238B8CD6A3ED5A9B3975E291D9E6866844F45FEA5D3C85384EDAE294CA`;
  checked diagnostics are zero. Output pages 53--55 were personally inspected
  at 1,200 dpi and pass the predecessor seam, p.69/p.70 source seam, formulas,
  theorem typography, clipping, and page-envelope checks. Their exact PNG
  identities are respectively 3,643,207 bytes / SHA-256
  `86AB8FA32B089BBF48ED017C954F9737909320CF00C63B99ADBA68322E1FCD5F`,
  3,626,156 bytes / SHA-256
  `41A41D1A0F7EE130391BDEDB9CA3D34E6B29531DD21D72517319E6424B7637E4`,
  and 2,625,027 bytes / SHA-256
  `3051DA3529ED3C4C9A32E3A050A0672AB9B23ADFC71A9495D306DC1DE763CEC5`.
- Six new source-backed English dispositions are individually justified in
  `controls/ENGLISH_CORRECTION_RECHECK_APPEND_P70_20260802.jsonl`, six
  records / 8,437 bytes / SHA-256
  `A49C199D52DB2623B86B880FC22951014A8C60558C4B1DD0DE58419A2D920494`.
  Five are inherited English errors now repaired: `compliments` for
  `complements`, missing `J_\lambda` subscript, missing definite article,
  `is remains`, and singular-agreement `characterize`. The sixth is a printed
  French typographical defect: the direct 9,000-dpi crop proves a lone
  unmatched opening bracket in 7.5.2. Diplomatic French preserves it; the
  existing English omission is justified and unchanged.
- All eight p.69/p.70 English repairs are present in the complete copied
  source successor
  `03_projects/language_management/english_germanic/<REDACTED_INTERNAL_WORKSPACE>/EGA_English_Global_0_IV_french_recheck_source_successor_20260802_r1`.
  Its only changed source file is `source/ega0/ega0-7.tex`, 75,196 bytes /
  SHA-256
  `1E33F146B32D3EDEEF978DE63A9FB06F856E027D02F0C8BDD7F49B4482C96CE5`.
  `controls/SOURCE_INPUT_SHA256_R4.json`, 23,160 bytes / SHA-256
  `E2D57DA04123015CA761E081142152EB4DF60029A914C94B3E4C89C180F81FD0`,
  replays 127/127 rows and exact ordinal tree SHA-256
  `0E7BBF54FB4C5EC7C6EE5660909351A8788D7581F0DA8AAFB6C991D2CE490CAD`.
  `controls/SOURCE_DIFF_VALIDATION_R4.json`, 3,893 bytes / SHA-256
  `C20119C23B354AE4EB56E0EB22F9C9DECF5F356235FA433EFCC7F21514BEEEC4`,
  and its replay both pass with errors empty. A global rebuild/public
  supersession remains pending; no frozen/public predecessor was mutated.
- The decision surface is now 126 individually bound records: 99 confirmed
  English errors, 22 French-source issues, two official erratum/addendum
  decisions, and three external additions. Nineteen are formally
  source-justified. No admitted English source-correction judgment has been
  reversed.
- Five current-run workflow events are classified across the three
  append-only workflow files; four are lead-authored control/tool mistakes.
  The latest records preserve R2's null/ordering failure and R3's
  list-order-versus-declared-ordinal aggregate failure. Neither changed any
  French or English source byte.
- Corpus-scale progress is 67 source-bearing pages admitted out of 1,800
  physical pages (about 3.7%); approximately 1,733 physical pages remain.
- Archive custody has acknowledged the dual-logbook-DOI rule under decision
  `EG-ARCHIVE-DUAL-DOI-LOGBOOK-CUSTODY-CONTROL-20260802-0001`. Methodology
  concept: `10.5281/zenodo.21124403`; replication concept:
  `10.5281/zenodo.20461174`. Mutable EGA remains excluded and no upload has
  occurred.

## Controlling quick status — 2026-08-02, through printed p.69

This block supersedes all older point-in-time quick-status blocks below; those
blocks remain append-only history.

- The admitted diplomatic French source is complete through Corollary 7.4.5
  and its proof on EGA I printed p.69 / physical PDF page 68. This includes
  Proposition 7.4.2 across the p.68/p.69 seam, Corollary 7.4.3, numbered
  paragraph 7.4.4, and Corollary 7.4.5. Section 7.5 is wholly unadmitted.
- `source/ega1/ega0-1-fr.tex`: 242,901 bytes / 5,180 lines / SHA-256
  `9A072E70A9652DA484529BC2F136FF2D682C4244C7C9F6B0E0445E4CDDA729AC`.
- Exact next cursor: section 7.5, numbered paragraph 7.5.1, beginning on
  printed p.69 and crossing to p.70.
- The p.69 direct-authority evidence manifest is
  `controls/EGA1_PRINTED69_SECTION742_745_DIRECT_AUTHORITY_IMAGES.json`,
  3,115 bytes / SHA-256
  `2CCF0BDFEDC221B1B6C9298EBCF1442E20B79BA72AF4D50411A309E8C959B9E1`.
  It binds one 1,400-dpi navigation page, one direct 5,000-dpi full page, and
  five overlapping direct 5,000-dpi bands. The lead personally read the
  admitted scope from the direct 5,000-dpi surface. A failed blank Poppler
  crop is explicitly excluded and preserved as workflow history.
- The controlling bounded French reader is
  `qa/ega1_chapter0_build/ega0-pages11-69-through-745-check-r47.pdf`, 54 A4
  pages / 367,924 bytes / SHA-256
  `1F0C8B44B9C8026014D5521736896A2510F1706D7EF9A78487DC0A35A51EF72F`.
  Three correctly quoted serialized XeLaTeX passes exit 0; passes 2 and 3 have
  identical console SHA-256
  `A9806224D1203C928B92EC965824A9CFD0D320B21DF040AC5A093D464211467B`;
  checked diagnostics are zero. Output pages 52--54 were personally inspected
  at 1,200 dpi and pass the p.68/p.69 seam, formula, theorem typography,
  clipping, and page-envelope checks.
- Three new source-backed English defects were found and individually
  justified in
  `controls/ENGLISH_CORRECTION_RECHECK_APPEND_20260802.jsonl`, three records /
  4,790 bytes / SHA-256
  `0AC3732031D359DA8F547BDCFA1B9850A353BF5ADF1604B4BBABA9C487480560`:
  missing module factor `M` in 7.4.2, wrong 7.2.4-for-7.4.2 cross-reference in
  7.4.3, and omission of the preceding-argument justification plus the exact
  two-condition conjunction in 7.4.4.
- All three English repairs are applied in the complete copied source
  successor
  `03_projects/language_management/english_germanic/<REDACTED_INTERNAL_WORKSPACE>/EGA_English_Global_0_IV_french_recheck_source_successor_20260802_r1`.
  Its only changed source file is `source/ega0/ega0-7.tex`, SHA-256
  `BF941F818AC3F174FD4C9DD3013761BB19A9811898D970FCBB686C8EDEE3BCB7`.
  `controls/SOURCE_DIFF_VALIDATION_R2.json`, 1,588 bytes / SHA-256
  `CCD7E96E872A65E36CEF6F7CF6F8B2436CE4332DD1865DA81CE0AA17809FEA9F`,
  passes with errors empty. A full global rebuild/public supersession is still
  pending; no frozen/public predecessor was mutated.
- The decision surface is now 120 individually bound records: 94 confirmed
  English errors, 21 French-source issues, two official erratum/addendum
  decisions, and three external additions. Thirteen are formally
  source-justified. No admitted English source-correction judgment has been
  reversed. The three repair-state transitions are separately append-only in
  `controls/ENGLISH_CORRECTION_REPAIR_APPLICATION_20260802.jsonl`, three
  records / 2,760 bytes / SHA-256
  `3F12C0504D7A24802A18DBA525F7395FB63F6E87F8C632B8230825713FEE459A`.
- Three current-run workflow events, including two lead-authored mistakes, are
  classified in `controls/WORKFLOW_ERROR_APPEND_20260802.jsonl`, three records
  / 2,222 bytes / SHA-256
  `08611645794C98E11A5356D5C200FFE6C42662C18158A9BCF84CD6A4D30FFD68`.
  None changed French or English source bytes.
- Corpus-scale progress is 66 source-bearing pages admitted out of 1,800
  physical pages (about 3.7%); approximately 1,734 physical pages remain.
- Archive custody has acknowledged the dual-logbook-DOI rule under decision
  `EG-ARCHIVE-DUAL-DOI-LOGBOOK-CUSTODY-CONTROL-20260802-0001`. Methodology
  concept: `10.5281/zenodo.21124403`; replication concept:
  `10.5281/zenodo.20461174`. Mutable EGA remains excluded and no upload has
  occurred.

## Controlling quick status — 2026-08-02, through printed p.68

This block supersedes the older point-in-time summary immediately below; the
later dated sections remain append-only history.

- The admitted diplomatic French source is complete through EGA I printed
  p.68 / physical PDF page 67, ending after Definition 7.4.1 and its two
  explanatory paragraphs.
- `source/ega1/ega0-1-fr.tex`: 239,076 bytes / 5,100 lines / SHA-256
  `B67D532198A8C7E4DFCAD5E39246D162960AAC351DBB2F805F321AABA363AAAB`.
- The exact next cursor is Proposition 7.4.2 on printed p.68. It continues on
  p.69 and remains wholly unadmitted.
- The controlling bounded reader is
  `qa/ega1_chapter0_build/ega0-pages11-68-through-741-check-r46.pdf`:
  53 A4 pages / 363,893 bytes / SHA-256
  `625D17308AEDC519272E92C6447E9FD22D4829AA34DE1AC6C01E9C386022FC37`.
  Three XeLaTeX passes exit 0; pass 2 and pass 3 console files are
  byte-identical at SHA-256
  `19ED29D2C03DF1D52FB93A82FD357651198785DD56B4A8B19FAB3A441A11FF61`;
  checked diagnostics are zero.
- The p.68 authority surface is bound by
  `controls/EGA1_PRINTED68_SECTION735_741_DIRECT_AUTHORITY_IMAGES.csv`, seven
  rows / 1,474 bytes / SHA-256
  `A0C0FD4A8A58224F9C93A3A19C23337051079154EF999C8ECCF0DE936D1F8420`.
  The full page and five overlapping bands were personally re-read from the
  direct 5000-dpi authority images. The unusual printed clause
  `$x\in\mathfrak Jx$` is retained diplomatically.
- The English correction ledger remains 117 data rows / 89,159 bytes /
  SHA-256
  `3F56E5F7F24E321BB7AECECFC26174937139527744AD834A7CF509ED3CFD3652`;
  no new correction or normalization was admitted for 7.3.5--7.4.1.
- Per-decision rationale and append-only reversal accounting are now governed
  by
  `controls/ENGLISH_NORMALIZATION_DECISION_AND_REVISION_POLICY_20260802.md`.
  The 117 adjudicated rows split exactly into 91 confirmed English errors, 21
  French-source issues, two official EGA II erratum/addendum decisions, and
  three separately unbound external additions. Ten decisions are currently
  marked formally source-justified. No admitted English source-correction
  decision has yet been reversed; one proposed mathematical correction was
  rejected before admission. Five historical rationale rows have unquoted
  commas, so the original annex is preserved and any machine-corrected version
  must be a no-overwrite, reciprocally superseding successor.
- Corpus-scale progress is 65 source-bearing authority pages admitted out of
  1,800 physical PDF pages (about 3.6%). Approximately 1,735 physical pages
  remain; blank and publisher-only leaves mean this is a conservative physical
  workload count rather than a claim about text density.
- A compact restart surface is maintained in `CONTINUATION_HANDOFF.md`.

Current admitted EGA I files:

- `source/ega1/frontmatter-fr.tex`: original title and legal/imprint pages,
  transcribed from authority physical PDF pages 2–3. The publisher's graphic
  device is identified in a TeX comment but is not reproduced as a raster.
- `source/ega1/intro-fr.tex`: the complete Introduction, printed pages 5–9,
  checked page by page against authority physical PDF pages 4–8.
- `source/ega1/ega0-1-fr.tex`: Chapter 0 through 5.3.7, printed pages 11–47 /
  physical PDF pages 10–46. Formula-rich passages on printed pages 11 and
  13–47 were checked in direct 5000-dpi authority images. All sixteen diagram
  blocks through 5.3.7 are native TeX/TikZ, not rasters. The current file is
  153,059 bytes, SHA-256
  `F0DCEA46C6D128E41DE1AD93E3376CB1658DEFC8CC7B1CA8AABB4F36FA1A8DEF`.

Current exact cursor: EGA I printed page 47 / physical PDF page 46, immediately
after complete 5.3.7 and before 5.3.8 on printed page 48.
Printed page 10 / physical PDF page 9 is blank.

The bounded Chapter-0 QA reader through 5.3.7 is thirty-five pages, 260,113
bytes, SHA-256
`4AAD617D6331BD69A3B4F73C1E81E47016953C190F7DF7F8BAFB253E8B600192`.
Three XeLaTeX passes completed without errors, undefined references, or layout
diagnostics; pass 2 and pass 3 console logs are byte-identical at SHA-256
`5D9F83D8803D89E3D94E6B3F6F9C9D8EAC929D032CC26F0D3E9148566C5A603E`.
The only log noise is XeLaTeX's harmless notice that `inputenc` is ignored and
the expected PDF-bookmark warning caused by mathematical subsection titles.
The changed output and adjoining seam were personally inspected on output
pages 33–35 at 1200 dpi. The controlling identity is the no-overwrite R21
build. An earlier R12 command used
PowerShell's automatic `$args` variable and reached the XeTeX terminal without
an input filename; it is a non-controlling invocation failure and did not
alter the source. Preliminary misplaced-source, equation-tagging, and
wrong-page-mapping attempts were caught before admission and are
non-controlling; the final source and build above are internally consistent.
The 13 direct
5000-dpi authority crops
for printed pages 13–15 are bound in
`controls/EGA1_PRINTED13_15_DIRECT_AUTHORITY_5000DPI_CROPS.csv`, 2,514 bytes,
SHA-256
`B56B08ED9958A1CF4FD3C417953C5E2B6CB1EDA502A4F1E0F0C919F00C4E2D49`.
The whole-page and 5000-dpi authority evidence for printed pages 15–16 is
bound in `controls/EGA1_PRINTED15_16_DIRECT_AUTHORITY_IMAGES.csv`, 2,483 bytes,
SHA-256
`7DA744A8488A80EB98C4E2FF6A285DE428E73779C330F4029C46176C904F8AE4`.
The whole-page and 5000-dpi authority evidence for printed pages 17–18 is
bound in `controls/EGA1_PRINTED17_18_DIRECT_AUTHORITY_IMAGES.csv`, 2,683 bytes,
SHA-256
`FB4FA838AB77DD9504B2D3F0143D6628AFB0B40E0BA6A503DF3650635028DF27`.
The whole-page and direct 5000-dpi authority evidence for printed pages 19–20
is bound in `controls/EGA1_PRINTED19_20_DIRECT_AUTHORITY_IMAGES.csv`, 2,426
bytes, SHA-256
`A02A0271C21E1A037F942B018C57306D3719068164E5714B105CEFE508087FDF`;
all 11 rows replay against disk without size or hash error.
The printed-page-21 authority evidence is bound in
`controls/EGA1_PRINTED21_DIRECT_AUTHORITY_IMAGES.csv`, 5 rows / 1,163 bytes,
SHA-256
`F921AF92129D1B1CEADD8FA5CEFAC3EF18AC1F97879CFD042C76F34242139295`.
The printed-page-22 authority evidence is bound in
`controls/EGA1_PRINTED22_DIRECT_AUTHORITY_IMAGES.csv`, 5 rows / 1,164 bytes,
SHA-256
`7A8D101AB8AD123818D4B4C2771C758505A219B071D5B5BAA646DB64A88BB645`.
The printed-pages-23–24 authority evidence is bound in
`controls/EGA1_PRINTED23_24_DIRECT_AUTHORITY_IMAGES.csv`, 12 rows / 2,780
bytes, SHA-256
`274E7BD39765061551AF521987A1CD96AA3EF254F8448AEC198E1FEB70964E8A`.
The printed-page-25 authority evidence is bound in
`controls/EGA1_PRINTED25_DIRECT_AUTHORITY_IMAGES.csv`, 5 rows / 1,228 bytes,
SHA-256
`ED36A97EB8CB526EDC8CB5443B5DF63E626FD9CEA8615904039216462C6CE774`.
The complete subsection-3.2 authority surface is bound in
`controls/EGA1_SECTION32_PRINTED25_28_DIRECT_AUTHORITY_IMAGES.csv`, 14 rows /
3,091 bytes, SHA-256
`49B5F664F971CBBA66EFB4C4BCC0E36F1EF5789C6BBA4E86C293DBFC9E78F847`.
The complete subsection-3.3 authority surface is bound in
`controls/EGA1_SECTION33_PRINTED28_29_DIRECT_AUTHORITY_IMAGES.csv`, 7 rows /
1,633 bytes, SHA-256
`81BB8A99773638880D0B8E92E1FB192EF76FA8C56E9ACEAA41D0432D140F4DD4`.
The complete subsection-3.4 authority surface is bound in
`controls/EGA1_SECTION34_PRINTED29_30_DIRECT_AUTHORITY_IMAGES.csv`, 7 rows /
1,535 bytes, SHA-256
`4C6ECB7292E0220849F27DF58398E24F3717C74C62CBE38327E22A46496546AA`.
The complete 3.5-through-3.6.2 authority surface is bound in
`controls/EGA1_SECTION35_36_PRINTED30_33_DIRECT_AUTHORITY_IMAGES.csv`, 25 rows /
5,221 bytes, SHA-256
`24DA0E86025CACB1043F1EF1E4C1DE10B8978DB24B00EEA3CCA0BAE47D7A1971`.
All 25 rows replay against disk without size or hash error. Direct Poppler
5000-dpi full-page attempts for printed page 31 failed with memory-allocation
errors and produced blank artifacts; they were segregated unchanged. A direct
MuPDF 5000-dpi full-page image and five overlapping bands were used instead.
The complete printed-page-34 authority surface is bound in
`controls/EGA1_PRINTED34_DIRECT_AUTHORITY_IMAGES.csv`, 7 rows / 1,614 bytes,
SHA-256
`49652D8AB9280E8DF627FF952B4D8E0DE387AC0602C49E5808F8F07E93CEEBE0`;
replay is 7/7 with errors 0. The first page-34 rendering attempt used the PDF
command page 34, which is printed page 35; the header check caught the
off-by-one error before transcription and the mislabeled images were
segregated unchanged. The controlling printed-page-34 evidence uses physical
PDF page 33.
The complete subsection-3.8 authority surface on printed page 35 is bound in
`controls/EGA1_PRINTED35_SECTION38_DIRECT_AUTHORITY_IMAGES.csv`, 7 rows /
1,637 bytes, SHA-256
`1B8B2AAA69FFAA459B0340AFADAD2D3B14A5C2AB00FBC74D4DB6D2F4255FA68F`;
replay is 7/7 with errors 0. The source image also records the opening of
section 4 as the exact seam.
The printed-page-36 authority surface for the completion of 4.1.1 and all of
4.1.2 is bound in
`controls/EGA1_PRINTED36_SECTION411_412_DIRECT_AUTHORITY_IMAGES.csv`, 6 rows /
1,445 bytes, SHA-256
`96C554F48528EB3DC102B96CA58A9BFEFB1D4D117EB4A6CECA1EB951E9FB6B4E`;
replay is 6/6 with errors 0.
The printed-page-37 authority surface for the completion of 4.1.3 and all of
4.1.4 is bound in
`controls/EGA1_PRINTED37_SECTION413_414_DIRECT_AUTHORITY_IMAGES.csv`, 7 rows /
1,693 bytes, SHA-256
`6F332655F35196B09BF03CA6A556E1BDEE425445A15F082A3F0A09D98A4BFF05`;
replay is 7/7 with errors 0.
The printed-pages-38–39 authority surface for the completion of 4.1.5 and all
of 4.1.6–4.1.7 is bound in
`controls/EGA1_PRINTED38_39_SECTION415_417_DIRECT_AUTHORITY_IMAGES.csv`, 14
rows / 3,174 bytes, SHA-256
`802227EA49F2DFC0D164F893B0F358E94B735FB3739DA4364E62EA78C2592DDE`;
replay is 14/14 with errors 0. The first page-generation command used PDF page
38, which is printed page 39. Its images were identified by their visible
header before transcription and preserved under corrected `p39` names; the
true printed-page-38 authority was then generated from PDF page 37.
The printed-page-40 authority surface for the completion of 4.2.2 and all of
4.2.3–4.2.6 is bound in
`controls/EGA1_PRINTED40_SECTION422_426_DIRECT_AUTHORITY_IMAGES.csv`, 7 rows /
1,580 bytes, SHA-256
`0A5BF4FD58281BDA78E11B5413049016FD004DA2B4CDE8DAEE217AFE9786781F`;
replay is 7/7 with errors 0. The last band also records the opening of 4.3.1 as
the exact next seam.
The printed-page-41 authority surface for complete 4.3.1–4.3.3 and the opening
of 4.3.4 is bound in
`controls/EGA1_PRINTED41_SECTION431_433_DIRECT_AUTHORITY_IMAGES.csv`, 7 rows /
1,611 bytes, SHA-256
`DF271BCBBACFD18FAE6765EBBD6FCE378627DC4F0BB67FA063DE864410C24587`;
disk replay is 7/7 with errors 0. The full page and all five overlapping bands
were personally read at direct 5000-dpi detail.
The printed-page-44 authority surface for the completion of 4.4.6 and complete
4.4.7–4.4.8 is bound in
`controls/EGA1_PRINTED44_SECTION446_448_DIRECT_AUTHORITY_IMAGES.csv`, 8 rows /
1,703 bytes, SHA-256
`546E619E921611A06771E1EF81CCDF66BBA8741E631818A26CC3A053F6342408`;
disk replay is 8/8 with errors 0. It includes a targeted 5000-dpi crop proving
that the source introduces $u'$ but immediately composes and thereafter uses
$v'$ in 4.4.8.
The printed-page-45 authority surface for the completion of 5.1.1 and complete
5.1.2–5.2.1 is bound in
`controls/EGA1_PRINTED45_SECTION5_521_DIRECT_AUTHORITY_IMAGES.csv`, 8 rows /
1,701 bytes, SHA-256
`3FA07D46A97EFDEDE063129AB26D6CED9001610194B5A551801AEEA191B83133`;
disk replay is 8/8 with errors 0. It includes a targeted 5000-dpi crop settling
the complete finite-type sentence in 5.2.1.
The printed-page-46 authority surface for the completion of 5.2.2 and complete
5.2.3–5.2.6 is bound in
`controls/EGA1_PRINTED46_SECTION522_526_DIRECT_AUTHORITY_IMAGES.csv`, 8 rows /
1,720 bytes, SHA-256
`ADE04AE72ED6BAB56B05F7E7DBD3BD8A7874AC872A94212BB2F6822B6F568EE0`;
disk replay is 8/8 with errors 0. The targeted 5000-dpi crop proves that the
printed source omits the star from $f_U^*$ in the right-exactness clause of
5.2.4.
The printed-page-47 authority surface for the completion of 5.2.7 and complete
5.3.1–5.3.7 is bound in
`controls/EGA1_PRINTED47_SECTION527_537_DIRECT_AUTHORITY_IMAGES.csv`, 7 rows /
1,466 bytes, SHA-256
`6ABD7E86F2F6DA7C2A46BE8B5481274CFF00FD62D59FF2844C7D29EBDF90033E`;
disk replay is 7/7 with errors 0. The full page and all five overlapping bands
were personally read at 5000-dpi detail.
The printed-page-42 authority surface for the completion of 4.3.4, complete
4.3.5–4.3.6, and complete 4.4.1–4.4.2 is bound in
`controls/EGA1_PRINTED42_SECTION434_442_DIRECT_AUTHORITY_IMAGES.csv`, 7 rows /
1,447 bytes, SHA-256
`E513C415CCC0CE2C80B77E966C4FCD9F4BEB41568655DA4B4D3061B9CC3E6B35`;
disk replay is 7/7 with errors 0. The full page and all five overlapping bands
were personally read at direct 5000-dpi detail. Section 4.4.3 begins at the
bottom of the page and crosses the next seam; it was therefore transcribed
with the printed-page-43 unit rather than split.
The printed-page-43 authority surface for the completion of 4.4.3, complete
4.4.4–4.4.5, and the opening of 4.4.6 is bound in
`controls/EGA1_PRINTED43_SECTION443_445_DIRECT_AUTHORITY_IMAGES.csv`, 7 rows /
1,447 bytes, SHA-256
`040B9F12688AE6C01EB0CE4E6CF83F196C1B59332E54F4ABE5E8A3E5D4AA25D0`;
disk replay is 7/7 with errors 0. The full page and all five overlapping bands
were personally read at direct 5000-dpi detail.
All manifests replay against disk without size or hash error.

The inherited 6,179-byte introduction seed is retained only as provenance.
Two non-diplomatic accent regularizations in it were reversed (`A Oscar
Zariski` and `A titre informatif`), and the remainder of the Introduction was
transcribed directly from the authority.

No French correction layer is authorized. No separate French full reader is
in scope. English correction claims are mandatory image-recheck points.

The mechanical English-correction recheck queue is frozen in
`controls/ENGLISH_CORRECTION_RECHECK_MASTER_QUEUE.csv`, 60 unique rows / 57,785
bytes, SHA-256
`BF17F5ADEC2CD3E26B3AE30C463EEB4803ED55B5279AED5812852FBF34DD9CDA`.
It is a locator queue only: every substantive row remains subject to personal
direct-NUMDAM image adjudication while the corresponding French locus is
transcribed.

Confirmed English recheck finding: NUMDAM EGA I printed page 8 says
`chap. IX`, while the current English introduction says `Chapter XI`. This is
an English translation error to be corrected in an append-only English
successor; the canonical French remains exactly `chap. IX`.

Confirmed source-typo recheck finding
`EG-EGA-I-P25-GAMMA-U-V-SRC-TYPO-001`: NUMDAM EGA I printed page 25 says
`u_V(s)` but quantifies `s\in\Gamma(U,\mathcal F)`. The current English
erratum to `\Gamma(V,\mathcal F)` is source-justified. The canonical French
TeX nevertheless retains the printed `U` without silent correction.

Confirmed source-typo recheck finding
`EG-EGA-I-P27-BASE-X-VS-U-SRC-TYPO-001`: NUMDAM EGA I printed page 27 calls
the subfamily of basis opens lying in the covering of $U$ a basis of the
topology of `X`. The current English correction to the topology of `U` is
source-justified. The canonical French TeX retains the printed `X`.

Confirmed English mathematical transcription error
`EG-EGA-I-P28-THETA-CODOMAIN-MISSING-LAMBDA-EN-001`: NUMDAM EGA I printed
page 28 defines the codomain of $\theta_{\lambda\mu}$ as
$\mathcal F_\lambda|(U_\lambda\cap U_\mu)$, whereas the current English drops
the subscript and prints $\mathcal F|(U_\lambda\cap U_\mu)$. The canonical
French TeX transcribes the printed $\mathcal F_\lambda$.

Confirmed source-typo recheck finding
`EG-EGA-I-P33-SECOND-RESTRICTION-U-V-SRC-TYPO-001`: NUMDAM EGA I printed
page 33 repeats $\mathcal F(X)\to\mathcal F(U)$ as the second restriction map,
although the subsequent comparison requires $\mathcal F(X)\to\mathcal F(V)$.
The canonical French TeX retains the printed `U`; the current English also
repeats `U` and requires a transparent append-only correction to `V`.

Three confirmed English source-fidelity errors occur on EGA I printed page 34.
In two local-representative conditions NUMDAM prints
$s'_z=s_{\psi(z)}$, whereas the inherited English prints
$s'_z=s_{\psi(x)}$; both English occurrences require $\psi(z)$. NUMDAM also
calls $<REDACTED_LOCAL_ROOT>/mathcal G_1\to\mathcal G_2$ a homomorphism of presheaves of sets,
whereas the inherited English narrows this to sheaves. Stable IDs are
`EG-EGA-I-P34-GPRIME-LOCAL-SECTION-PSI-Z-EN-001`,
`EG-EGA-I-P34-USHARP-LOCAL-SECTION-PSI-Z-EN-001`, and
`EG-EGA-I-P34-W-PRESHEAVES-VS-SHEAVES-EN-001`.

Confirmed source-typo recheck finding
`EG-EGA-I-P36-THETA-GF-VS-BA-SRC-TYPO-001`: after defining a morphism
$(X,\mathcal A)\to(Y,\mathcal B)$, NUMDAM prints the structure-sheaf map as
$\theta:\mathcal G\to\mathcal F$. The morphism data require
$\theta:\mathcal B\to\mathcal A$, exactly as the inherited English erratum
has it. Canonical French retains the printed $\mathcal G\to\mathcal F$.

Four direct-image English defects are confirmed across printed pages 37–38:
the first sheaf-Hom bifunctor must be
$\mathcal H\!om_{\mathcal A}(\mathcal F,\mathcal G)$ rather than
$\mathcal H\!om_{\mathcal A}(\mathcal F,\mathcal F)$; `sommes directes
finies` means finite direct sums, not finite direct limits; the displayed
$\Gamma(U,\mathcal H\!om(\mathcal F,\mathcal G))$ identity lacks its closing
parenthesis in English; and the domain sheaf in $\varphi_{\lambda\mu}$ is
restricted to $V_{\mu\lambda}$, not $V_{\lambda\mu}$. These are bound under
stable IDs `EG-EGA-I-P37-SHHOM-F-F-VS-F-G-EN-001`,
`EG-EGA-I-P38-FINITE-DIRECT-SUMS-VS-LIMITS-EN-001`,
`EG-EGA-I-P38-GAMMA-HOM-MISSING-PAREN-EN-001`, and
`EG-EGA-I-P38-PHI-DOMAIN-RESTRICTION-INDEX-EN-001`. The technically frozen
global English reader remains unchanged; all four require one later
no-overwrite English correction successor.

Two further English defects are confirmed on printed page 41. NUMDAM heads
4.3 as the inverse image of a $\mathcal B$-Module, whereas the inherited
English heading says $\mathcal A$-module; the construction itself confirms
that $\mathcal B$-modules are sent to $\mathcal A$-modules. In 4.3.1 the
English also prints the duplicated articles `with the a` where the sentence
must read `with a`. Stable IDs are
`EG-EGA-I-P41-INVERSE-IMAGE-HEADING-A-VS-B-EN-001` and
`EG-EGA-I-P41-ENDOWS-WITH-THE-A-EN-001`.

One English grammar error is confirmed in 4.4.1 on printed page 42. NUMDAM
defines singularly `un Psi-morphisme`, while the inherited English prints the
ungrammatical `a Psi-morphisms`. Stable ID
`EG-EGA-I-P42-PSI-MORPHISM-PLURAL-EN-001` requires `a Psi-morphism` in the
later no-overwrite English correction successor.

Four further English errors are confirmed while closing 4.4.3–4.4.5. `We
obtain (3.7.1)` drops the required `from`; the unit construction wrongly names
the identity of $\Psi^*(\mathcal B)$ instead of $\Psi^*(\mathcal G)$; `neither
injective or surjective` requires `nor`; and the family $(u_\lambda)$ forms an
inductive system, not an inductive limit. Stable IDs are
`EG-EGA-I-P42-ON-EN-DEDUIT-MISSING-FROM-EN-001`,
`EG-EGA-I-P43-IDENTITY-PSISTAR-B-VS-G-EN-001`,
`EG-EGA-I-P43-NEITHER-OR-VS-NOR-EN-001`, and
`EG-EGA-I-P43-INDUCTIVE-SYSTEM-VS-LIMIT-EN-001`.

Three further dispositions are closed across printed pages 43–44. In 4.4.6
the English misspells `normally` and repeats the articles in `with the a`.
In 4.4.8 NUMDAM introduces $u'$ once, but the definition, composition, arrow,
and induced morphism all use $v'$; this is a confirmed French source typo.
Canonical French retains the printed $u'$, while English must use $v'$
consistently with an immediate visible note. Stable IDs are
`EG-EGA-I-P43-NORMALLY-MISSPELLED-EN-001`,
`EG-EGA-I-P43-WITH-THE-A-DUPLICATE-ARTICLE-EN-001`, and
`EG-EGA-I-P44-UPRIME-VS-VPRIME-SRC-TYPO-001`.

Two further dispositions are closed on printed page 45. In 5.1.3 NUMDAM
introduces an open neighbourhood $U$ but then prints $V$ in all three
restrictions; canonical French retains the three printed $V$ occurrences,
while the inherited English correction to $U$ is mathematically and
source-contextually justified under
`EG-EGA-I-P45-QUASICOHERENT-U-V-SRC-TYPO-001`. The extra sentence marked
`Erratum II` in English 5.1.2 is absent from the bounded NUMDAM body. It is not
imported into diplomatic French and remains separately conditioned on binding
the Erratum-II authority under
`EG-EGA-I-P45-ERRATUM-II-EXTERNAL-ADDITION-001`.

At the printed-page-45 checkpoint the English-recheck ledger had 25 rows,
19,637 bytes, SHA-256
`9F0332653D1CA64063F48BAFAB79007C3AD702D54737551BD176FA6B8DC93CB2`.

Four additional p.45–46 dispositions are closed. English 5.2.2 changes the
source's $y\in V$ to $y\in Y$; English 5.2.3 changes $V(x)$ to $V(s)$ and
turns an index greater than all finitely many $\lambda(x_k)$ into a maximal
index. All three are confirmed English mathematical errors. In 5.2.4 NUMDAM
prints $f_U$ where right exactness and the surrounding identities require
$f_U^*$; canonical French retains the missing star, while the inherited
English Erratum-II restoration is justified. Stable IDs are
`EG-EGA-I-P45-522-Y-IN-Y-VS-V-EN-001`,
`EG-EGA-I-P46-523-V-S-VS-V-X-EN-001`,
`EG-EGA-I-P46-523-MAXIMAL-VS-UPPER-INDEX-EN-001`, and
`EG-EGA-I-P46-FU-MISSING-STAR-SRC-TYPO-001`.

At the printed-page-46 checkpoint the English-recheck ledger had 29 rows,
22,495 bytes, SHA-256
`A444F30926F1A879586824094EB8F8B1E2BA1E9316DE0B544353E34B171BA192`.

Four p.47 English dispositions are closed. The heading sentence in 5.3.1
requires idiomatic `the following two conditions`; the logical term in 5.3.2
is `converse`, not `inverse`; the extra five-term exact-sequence sentence in
English 5.3.4 is absent from the bounded NUMDAM body and remains conditioned
on a separately bound Erratum-II authority; and English 5.3.5 contains a
duplicated `are` where the source coordinates the tensor product and sheaf
Hom. Stable IDs are
`EG-EGA-I-P47-531-TWO-FOLLOWING-WORD-ORDER-EN-001`,
`EG-EGA-I-P47-532-INVERSE-VS-CONVERSE-EN-001`,
`EG-EGA-I-P47-534-ERRATUM-II-EXTERNAL-ADDITION-001`, and
`EG-EGA-I-P47-535-DUPLICATE-ARE-EN-001`.

The adjudicated English-recheck ledger now has 33 rows, 25,414 bytes, SHA-256
`D865284F9B7C07B80C8644E0FACE968B02FF783036CD53D2D6DCB2C0E6DEDCE1`.

The disjoint Deligne D046–D090/letters lane is paused at D090 authority page
22 of 27 and resumes after this French EGA source corpus closes. The other task
continues D001–D045 without overlap.

## EGA I printed-page-48 closure

Printed page 48 has been transcribed diplomatically through the complete end
of 5.3.12. The admitted French source is now 155,985 bytes, SHA-256
`062A2C2E54DD0741953584E8444812FDE32CF41294947CC47D160830BCB3C988`.
The next exact cursor is the heading of section 5.4 and 5.4.1 across the
printed-page-48/49 seam; no partial 5.4.1 text has been admitted.

The direct-authority surface is bound by
`controls/EGA1_PRINTED48_SECTION538_5312_DIRECT_AUTHORITY_IMAGES.csv`, eight
rows / 1,695 bytes / SHA-256
`520DA1A67477B1DD2D4A210DDA22F141914081B32E2B94FC09CB2DE0F223357F`.
It covers the 1400-dpi context page, direct 5000-dpi full page, five
overlapping 5000-dpi bands, and a targeted 5000-dpi witness for the 5.3.9
source reading. Manifest replay is 8/8 with size/hash errors 0.

Two English dispositions are confirmed. In 5.3.8 the singular subject `This
result` requires `imposes`, not inherited `impose`. In 5.3.9 NUMDAM visibly
prints `un voisinage ouvert U de X`, although the module is over
$\mathcal{O}_x$, $\mathcal{F}_x=M$, and the construction immediately uses a
neighbourhood of $x$. This is a French source typo: diplomatic French retains
printed uppercase $X$, while the later English successor must use lowercase
$x$ with a visible source note. Stable IDs are
`EG-EGA-I-P48-538-IMPOSE-VS-IMPOSES-EN-001` and
`EG-EGA-I-P48-539-NEIGHBOURHOOD-OF-X-VS-XPOINT-SRC-TYPO-001`. The
English-recheck ledger now has 35 rows / 27,214 bytes / SHA-256
`64B77FD1BE05F01601C594D41678800A39CC82DEE9672C3EBFB37A951567FD26`.

The bounded reader was rebuilt in three converged XeLaTeX passes as
`qa/ega1_chapter0_build/ega0-pages11-48-through-5312-check-r22.pdf`, 36 A4
pages / 263,182 bytes / SHA-256
`50C3C0FD0308BB6A53F46FAA2167ADC055E633798F7F11D37BB250728AAEC618`.
Passes 2 and 3 have identical console SHA-256
`4FB0EBE20EAA6E7FDA4F63835C47D6A8FC53D2B2650BD93EA837CA498FBBFA88`;
fatal, undefined-reference, rerun, overfull, and underfull diagnostics are all
zero. Output pages 34–36 were rendered at 1200 dpi and personally inspected.
The p.47/p.48 seam, formula placement, paragraph flow, old-page marker,
clipping, and page envelopes pass. The blank remainder after 5.3.12 is the
intentional bounded-source stop before the cross-page 5.4.1 unit.

## EGA I printed-page-49 closure

The section 5.4 heading, complete 5.4.1 across the p.48/p.49 seam, and
complete 5.4.2–5.4.3 have been transcribed diplomatically. The admitted
French source is now 161,804 bytes, SHA-256
`A6F08C833F94C736E4F0C266C99EDADA972422CB5DFA2A71FE621BE7E8F1996B`.
The next exact cursor is 5.4.4 across the printed-page-49/50 seam; no partial
5.4.4 text has been admitted.

The direct-authority surface is bound by
`controls/EGA1_PRINTED49_SECTION541_543_DIRECT_AUTHORITY_IMAGES.csv`, eight
rows / 1,735 bytes / SHA-256
`A4B1602FED878CD1118C5D88F7E92BFC4C3D9CC72F89EA1EBA31ED1221FF1F57`.
It covers the 1400-dpi context page, direct 5000-dpi full page, five
overlapping 5000-dpi bands, and a targeted 5000-dpi witness for both arrow
forms in 5.4.3. Manifest replay is 8/8 with size/hash errors 0.

Five English/source dispositions are confirmed. English 5.4.1 has a spurious
comma between $\mathcal F|U$ and its predicate, and its marked Erratum-II
sentence is absent from the bounded NUMDAM body. English 5.4.3 cites 5.3.2
where NUMDAM correctly cites 5.4.2, and it drops the first conditional `if`
from the local-ring argument. Finally, NUMDAM visibly prints an isomorphism
arrow in the general scalar-endomorphism map
$\mathcal O_X\to\mathcal H\!om(\mathcal F,\mathcal F)$, although the next
sentence explicitly says bijectivity remains to be proved when
$\mathcal F=\mathcal L$ is invertible. This is a French source typo:
diplomatic French retains the printed isomorphism arrow; English must use an
ordinary arrow with a visible source note. Stable IDs are
`EG-EGA-I-P48-541-SPURIOUS-COMMA-EN-001`,
`EG-EGA-I-P49-541-ERRATUM-II-EXTERNAL-ADDITION-001`,
`EG-EGA-I-P49-543-XREF-532-VS-542-EN-001`,
`EG-EGA-I-P49-543-OX-ENDOMORPHISM-ISOTO-VS-TO-SRC-TYPO-001`, and
`EG-EGA-I-P49-543-MISSING-IF-EN-001`. The English-recheck ledger now has 40
unique rows / 31,582 bytes / SHA-256
`7B7CAD6B168DCC6F6A31EA90BEC43F0A7EF0FB26C89E4E46498E0B9D1DD14D2A`.

The first p.49 build exposed wrong glyphs for literal Unicode guillemets in
the current French font setup. The source-faithful quotation was therefore
encoded with the established `\og ... \fg{}` form; the preliminary R23 build
is non-controlling. The corrected bounded reader was rebuilt in three
converged XeLaTeX passes as
`qa/ega1_chapter0_build/ega0-pages11-49-through-543-check-r24.pdf`, 37 A4
pages / 269,084 bytes / SHA-256
`DE653E85A7F3A4C6EAA7A2015AA5201D00EC3C9B2640D62991173CEEB03A6790`.
Passes 2 and 3 have identical console SHA-256
`D9A0FF5973C1AA8BBFD6DC9D3EFBA6DEEFC61A7A9DB5A9934C8C9C9D5C8E3025`;
fatal, undefined-reference, rerun, overfull, and underfull diagnostics are all
zero. Output pages 36–37 were rendered at 1200 dpi and personally inspected.
The p.48/p.49 seam, formulas and arrows, corrected guillemets, paragraph
flow, clipping, and page envelopes pass. The blank remainder after 5.4.3 is
the intentional bounded-source stop before the cross-page 5.4.4 unit.

## EGA I printed-page-50 closure

Complete 5.4.4 across the p.49/p.50 seam and complete 5.4.5 have been
transcribed diplomatically. The admitted French source is now 163,898 bytes,
SHA-256
`7654EF35DB83CA45584C2747F4FC71DAD809D8E1EDB9974092312995460BE17D`.
The next exact cursor is 5.4.6 across the printed-page-50/51 seam; no partial
5.4.6 text has been admitted.

The direct-authority surface is bound by
`controls/EGA1_PRINTED50_SECTION544_545_DIRECT_AUTHORITY_IMAGES.csv`, seven
rows / 1,446 bytes / SHA-256
`3CD12BCAE16C58351D220A8D2E6308FE050DDF15FE5203342DEC49BA9EBCEF79`.
It covers the 1400-dpi context page, direct 5000-dpi full page, and five
overlapping 5000-dpi bands. Manifest replay is 7/7 with size/hash errors 0.

Three dispositions are confirmed. English 5.4.4 has singular `notation`
after plural `these`; English 5.4.5 uses the ungrammatical construction `from
that` instead of `from the fact that`. In the same paragraph NUMDAM prints a
single plain italic $L$ where every surrounding occurrence denotes the same
script $\mathcal L$; diplomatic French retains the plain $L$, while the
English normalization to script $\mathcal L$ is source-justified. Stable IDs
are `EG-EGA-I-P50-544-NOTATION-VS-NOTATIONS-EN-001`,
`EG-EGA-I-P50-545-FROM-THAT-VS-FROM-THE-FACT-EN-001`, and
`EG-EGA-I-P50-545-ROMAN-L-VS-SCRIPT-L-SRC-TYPO-001`. The English-recheck
ledger now has 43 unique rows / 34,111 bytes / SHA-256
`6ECC9DB41A80F464648EE560FB32514C684E6C1A9C7B49CC7C88B82619DE546C`.

The bounded reader was rebuilt in three converged XeLaTeX passes as
`qa/ega1_chapter0_build/ega0-pages11-50-through-545-check-r25.pdf`, 37 A4
pages / 271,048 bytes / SHA-256
`3CBD0696455326294FE4075CB8871891E5B5D7929497166F5C8F44244534D4AD`.
Passes 2 and 3 have identical console SHA-256
`C829F63C39A00B58126D033A02D1CA91991C45F5F226BFAE6A412E2F8050D56E`;
fatal, undefined-reference, rerun, overfull, and underfull diagnostics are all
zero. Output pages 36–37 were rendered at 1200 dpi; page 36 is byte-identical
to its already-inspected R24 render, and page 37 was personally inspected.
The p.49/p.50 seam, tensor-power formula, dual map, notation, paragraph flow,
clipping, and page envelope pass. The blank remainder after 5.4.5 is the
intentional bounded-source stop before the cross-page 5.4.6 unit.

## EGA I printed-page-51 closure

Complete 5.4.6 across the p.50/p.51 seam has been transcribed diplomatically.
The admitted French source is now 167,228 bytes, SHA-256
`05648F5BFFBE435DEAAF138F301EA58F7E4674E29C1DA3517317856967F39653`.
The next exact cursor is 5.4.7 across the printed-page-51/52 seam; no partial
5.4.7 text has been admitted.

The direct-authority surface is bound by
`controls/EGA1_PRINTED51_SECTION546_DIRECT_AUTHORITY_IMAGES.csv`, seven rows /
1,446 bytes / SHA-256
`651B83BD450FE474F23B34AE77DA817A033FA3C6CA8C0BF4CAAA96E75A0B587B`.
It covers the 1400-dpi context page, direct 5000-dpi full page, and five
overlapping 5000-dpi bands. Manifest replay is 7/7 with size/hash errors 0.

Four English defects are confirmed. In 5.4.6, `by corresponding to a pair`
must be replaced by the source-backed sense `by associating with a pair`;
`the verification ... are immediate` requires singular `is`; the pullback
identity has one unmatched extra closing parenthesis; and the p.51 conclusion
prints singular `these homomorphism` where plural `homomorphisms` is required.
Stable IDs are
`EG-EGA-I-P50-546-BY-CORRESPONDING-VS-ASSOCIATING-EN-001`,
`EG-EGA-I-P50-546-AXIOMS-ARE-VS-IS-EN-001`,
`EG-EGA-I-P50-546-EXTRA-CLOSING-PAREN-EN-001`, and
`EG-EGA-I-P51-546-HOMOMORPHISM-VS-HOMOMORPHISMS-EN-001`. A proposed fifth
candidate was rejected during exact replay because the current English
already prints the source-correct exponent $m$ in
$s_m\in\Gamma(X,\mathcal L^{\otimes m})$. The English-recheck ledger now has
47 unique rows / 36,998 bytes / SHA-256
`0F33C1828BD84F71BC0EA7CA52D4384D6DB7B727C7A5C402454F0CEF4F7CEC49`.

The bounded reader was rebuilt in three converged XeLaTeX passes as
`qa/ega1_chapter0_build/ega0-pages11-51-through-546-check-r26.pdf`, 38 A4
pages / 274,341 bytes / SHA-256
`501A3CB4BD16B9525686FFDCB7AAD52B94EB4EEE6FCDB2FF593386F3EB5D821D`.
Passes 2 and 3 have identical console SHA-256
`B23964557AB54464617BCC91EB3EF639280141B44CA762A21D763FB288F02381`;
fatal, undefined-reference, rerun, overfull, and underfull diagnostics are all
zero. Output pages 37–38 were rendered at 1200 dpi and personally inspected:
page 37 is 3,688,909 bytes / SHA-256
`C04FF07E9266E76BB10337D626FBD9333023751F3E8E66CC8AEB6BDDCB21EFED`,
and page 38 is 1,286,309 bytes / SHA-256
`677016CD39C249C3E41FF12405DAF8E3D948464E4643184A16E4A8824A8AD7A4`.
The p.50/p.51 seam, graded-ring and graded-module formulas, pullback maps,
old-page marker, paragraph flow, clipping, and page envelopes pass. The blank
remainder after 5.4.6 is the intentional bounded-source stop before 5.4.7.

## EGA I printed-page-52 closure

Complete 5.4.7 across the p.51/p.52 seam and complete 5.4.8–5.4.9 have been
transcribed diplomatically. The admitted French source is now 175,807 bytes,
SHA-256
`54E686F5ED3FC619A1CE60EF8F61222E4C448C630646DC3FB54E6F5C98FBCADB`.
The next exact cursor is 5.4.10 across the printed-page-52/53 seam; no partial
5.4.10 text has been admitted.

The direct-authority surface is bound by
`controls/EGA1_PRINTED52_SECTION547_549_DIRECT_AUTHORITY_IMAGES.csv`, eight
rows / 1,689 bytes / SHA-256
`3E21A336A425ED1C39670F1800201CD6B6F8E6F0B967077C3A919C4113DD73D2`.
It covers the 1400-dpi p.52 context page, direct 5000-dpi full page, five
overlapping 5000-dpi bands, and a targeted 5000-dpi p.51 coefficient crop.
Manifest replay is 8/8 with size/hash errors 0; the remainder of the p.51 side
of 5.4.7 remains bound by the preceding seven-row p.51 manifest.

Seven dispositions are confirmed. Three are printed French source defects
retained diplomatically: the automorphism formula over an open $U$ says
$x\in X$ where only $x\in U$ is defined; one injectivity map visibly omits
the star from coefficients $\mathcal O_X^*$; and the opening sentence of
5.4.8 incorrectly calls $f^*(\mathcal L)$ the functor and sends it to free
$\mathcal O_X$-modules although the induced map is obtained from the
inverse-image functor carrying invertible $\mathcal O_X$-modules to
invertible $\mathcal O_Y$-modules. English must correct each with a visible
source note. Four further English defects are the broken `and say ...
meaning` construction, the misspelling `coycles`, replacement of the product
transition cocycle
$(\varepsilon_{\lambda\mu}\varepsilon'_{\lambda\mu})$ by a comma-separated
pair, and plural-subject `automorphisms corresponds`. Stable IDs are
`EG-EGA-I-P51-547-X-IN-X-VS-X-IN-U-SRC-TYPO-001`,
`EG-EGA-I-P51-547-SAY-VS-SAYING-EN-001`,
`EG-EGA-I-P51-547-COYCLES-VS-COCYCLES-EN-001`,
`EG-EGA-I-P51-547-MISSING-STAR-IN-H1U-SRC-TYPO-001`,
`EG-EGA-I-P52-547-COCYCLE-COMMA-VS-PRODUCT-EN-001`,
`EG-EGA-I-P52-548-FSTAR-L-OX-FREE-SRC-TYPO-001`, and
`EG-EGA-I-P52-548-AUTOMORPHISMS-CORRESPONDS-VS-CORRESPOND-EN-001`. The
English-recheck ledger now has 54 unique rows / 42,917 bytes / SHA-256
`F7B79B66644531A84E8D60FD2024400A4208FD2902D5DDEF39504A95F3DC9E9A`.

The first p.52 build R27 exposed one missing-glyph diagnostic for literal
Unicode `Č`. The same printed word is encoded source-faithfully as
`\v{C}ech`; R27 is non-controlling. The corrected bounded reader was rebuilt
in three converged XeLaTeX passes as
`qa/ega1_chapter0_build/ega0-pages11-52-through-549-check-r28.pdf`, 39 A4
pages / 285,696 bytes / SHA-256
`25ED34E2ADA1014A20C2170BC800B28F8D5D05AF72A51EDE05DA8E889FB9B872`.
Passes 2 and 3 have identical console SHA-256
`E4F21AF445B532C71DBA9E5DD9D1381C4DDD68DFC0E9C8B552627435F4AA40D0`;
fatal, missing-character, undefined-reference, rerun, overfull, and underfull
diagnostics are all zero. Output pages 38–39 were rendered at 1200 dpi and
personally inspected: page 38 is 3,203,642 bytes / SHA-256
`5E3015B0E3214ABA07012FFF4059BA4DAEC13B51490D563B628DA973A08732C7`,
and page 39 is 3,657,687 bytes / SHA-256
`B4C96E41BD20416598EF9E04E44F7EC9A99A0B976DD123101FAC64F30474CAC8`.
The p.51/p.52 seam, cohomology diagram, transition-cocycle product, exact
sequence, old-page marker, both source footnotes, paragraph flow, clipping,
and page envelopes pass.

## EGA I printed-page-53 closure

Complete 5.4.10 across the p.52/p.53 seam and complete 5.5.1--5.5.3 have
been transcribed diplomatically. The admitted French source is now 180,145
bytes, SHA-256
`5338C7BFD794F17665FE476E453E3AB7EC3448FB9F8789766FEF263DB69D24B6`.
The next exact cursor is printed p.54 at 5.5.4; no p.54 body has been admitted.

The direct-authority surface is bound by
`controls/EGA1_PRINTED53_SECTION5410_553_DIRECT_AUTHORITY_IMAGES.csv`, seven
rows / 1,447 bytes / SHA-256
`D80E416FE9A1CD9B92ED629735D7DC929D043B61BB4EBFF7BDA9D7FC047B5087`.
It covers the 1400-dpi context page, direct 5000-dpi full page, and five
overlapping 5000-dpi bands. Manifest replay is 7/7 with size/hash errors 0.

Five English-only defects are confirmed. In 5.4.10 English prints
`$\mathcal L=\mathcal O_X^n$` although both the French authority and the
typing of the immediately preceding sentence require
`$\mathcal L=\mathcal O_Y^n$`; it also uses plural `questions` for singular
`question`. In 5.5.2 it again uses plural `questions`, and the singular
subject `equivalence` incorrectly takes `are`. In 5.5.3 the same
singular/plural `question` defect recurs. Stable IDs are
`EG-EGA-I-P53-5410-OX-N-VS-OY-N-EN-001`,
`EG-EGA-I-P53-5410-QUESTIONS-VS-QUESTION-EN-001`,
`EG-EGA-I-P53-552-QUESTIONS-VS-QUESTION-EN-001`,
`EG-EGA-I-P53-552-EQUIVALENCE-ARE-VS-IS-EN-001`, and
`EG-EGA-I-P53-553-QUESTIONS-VS-QUESTION-EN-001`. No French body correction
was made. The English-recheck ledger now has 59 unique rows / 46,176 bytes /
SHA-256
`EC6373F1966E1CD4F25E42B9A65DAC07A5C177E31EE9BA8D687B3A0F6AFD5415`.

R29 compiled cleanly but exposed a QA-wrapper-only numbering defect: the
artificial book chapter made the new subsection display as `0.5.5` although
NUMDAM prints `5.5`. R29 is therefore non-controlling. The diplomatic source
was not changed. The wrapper now explicitly renders EGA 0 sections as
`1, 2, ...` and subsections as `1.0, 1.1, ...`; it is 833 bytes / SHA-256
`5631F8ACC3089B0C3FFF3C33602C930A874225FE6E67AB0DCFE2881660B9D4AE`.

The controlling bounded reader was rebuilt in three converged XeLaTeX passes
as `qa/ega1_chapter0_build/ega0-pages11-53-through-553-check-r30.pdf`, 40 A4
pages / 291,332 bytes / SHA-256
`E4A85294D94BAA64062247A0528C0AB885ACB214F739BC7D784A3AF777FC16E5`.
Passes 2 and 3 have identical console SHA-256
`B7942978F819DDBBF4559DD9B6B2374130DD015588D9DAB382809A3C2543D4D1`;
fatal, missing-character, undefined-reference, rerun, overfull, and underfull
diagnostics are all zero. Output pages 1, 36--37, and 39--40 were rendered at
1200 dpi and personally inspected. Page 1 is 2,759,460 bytes / SHA-256
`D99C8F1403E674FF6E908140EB88B9B4762F755B40E1D1464D17C1C6289AF057`;
page 36 is 3,685,942 bytes / SHA-256
`C20C426FEFCBAD433825B8D7BD70DBADBDA84FCBD574F20342AAD4F6A763CB6F`;
page 37 is 3,688,909 bytes / SHA-256
`C04FF07E9266E76BB10337D626FBD9333023751F3E8E66CC8AEB6BDDCB21EFED`;
page 39 is 3,888,459 bytes / SHA-256
`5C5A2EFA60660B0B73099A490B6F0E6F6E5EA711799E00E06B9A78E160D2E8F6`;
and page 40 is 2,860,188 bytes / SHA-256
`C2EF4885DF5E5DB0F486CE63093104611B6A3FE39A4F314BFC958EBC637D092C`.
The visible `1` / `1.0`, `5.4`, and `5.5` headings, p.52/p.53 seam,
formulas, list items, old-page marker, paragraph flow, clipping, and page
envelopes pass.

## EGA I printed-page-54 5.5.4--5.5.5 closure

Complete 5.5.4 and 5.5.5 have been transcribed diplomatically from printed
p.54. The admitted French source is now 184,246 bytes, SHA-256
`775C63BB9CECD6ACA331C1FFF5DFCCF862E223A5CF42A2936E3FAD47F7C017B3`.
The next exact cursor remains on printed p.54 at the heading of section 6 and
the opening 6.0 paragraph, which crosses to p.55; no section-6 body has yet
been admitted.

The direct-authority surface is bound by
`controls/EGA1_PRINTED54_SECTION554_555_DIRECT_AUTHORITY_IMAGES.csv`, seven
rows / 1,447 bytes / SHA-256
`CF1F04FDAFF0AC28DFF4FE0926E541AE53143BE3ED105272838797EB35607305`.
It covers the 1400-dpi context page, direct 5000-dpi full page, and five
overlapping 5000-dpi bands. Manifest replay is 7/7 with size/hash errors 0.

Six source-backed dispositions are confirmed. NUMDAM prints one isolated
plain $F$ where the proposition otherwise uses calligraphic $\mathcal F$;
prints lowercase $u$ for the sought neighbourhood although $u$ already
denotes the homomorphism and the restriction is to uppercase $U$; and, after
shrinking to $U\subset V$, says that the basis condition holds for every
$y\in V$ rather than every $y\in U$. All three are retained in the diplomatic
French; English normalization/correction requires a visible source note.
English independently omits `module` from `locally free
$\mathcal O_X$-module`, breaks the `saying that ... means` construction, and
changes the authority's $y\in X$ to the nonexistent $y\in Y$. Stable IDs are
`EG-EGA-I-P54-554-PLAIN-F-VS-CALLIGRAPHIC-F-SRC-TYPO-001`,
`EG-EGA-I-P54-554-MISSING-MODULE-EN-001`,
`EG-EGA-I-P54-554-SAY-VS-SAYING-EN-001`,
`EG-EGA-I-P54-555-LOWER-U-VS-UPPER-U-SRC-TYPO-001`,
`EG-EGA-I-P54-555-Y-IN-Y-VS-Y-IN-X-EN-001`, and
`EG-EGA-I-P54-555-Y-IN-V-VS-Y-IN-U-SRC-TYPO-001`. The English-recheck
ledger now has 65 unique rows / 51,003 bytes / SHA-256
`AECC7EA7C57868B78CCD088EF45C103405459FE79A82B2705923A49129FF30EE`.

R31 was preserved as non-controlling after its first layout replay exposed
one 11.02023-pt overfull line at the long exterior-power expression. The same
formula was moved to display math without changing any printed symbol or
word. The controlling bounded reader was rebuilt in three converged
XeLaTeX passes as
`qa/ega1_chapter0_build/ega0-pages11-54-through-555-check-r32.pdf`, 41 A4
pages / 296,746 bytes / SHA-256
`19AC8BDE910E284B4FF6061342AFBB1A33CDD6865BB3C5F91CB9A168E2EC28FE`.
Passes 2 and 3 have identical console SHA-256
`0BA30D989A6FD0F6280DD3175C02DA2EE0F82DCB04205B7098CDD8B86962CA92`;
fatal, missing-character, undefined-reference, rerun, overfull, and underfull
diagnostics are all zero. Output pages 40--41 were rendered at 1200 dpi and
personally inspected. Page 40 is 3,243,948 bytes / SHA-256
`525963B8F184F209096B00CEE9AA875D24DD46E768C929573574B16BD510083A`;
page 41 is 2,662,383 bytes / SHA-256
`1A576A7651A4DC747E1607689D71DB895176277F474405C886B7D3ECADC4B36B`.
The p.53/p.54 seam, exterior-power formulas, quotient display, line breaks,
source-defect forms, clipping, and page envelopes pass. The blank remainder
of output p.41 is the intentional bounded-source stop before section 6.

## EGA I section-6 opening through printed p.55

The section-6 heading, complete 6.0 across the p.54/p.55 seam, complete
6.1.1--6.1.4, and the introductory paragraph of 6.2 have been transcribed
diplomatically. The admitted French source is now 187,861 bytes, SHA-256
`98C2C9B574C7BD688E16CDA31702A29C2A367B7400FE55B290E5B131587BD123`.
The next exact cursor is 6.2.1 on printed p.55, which crosses to p.56; no
6.2.1 text has been admitted.

The p.55 authority surface is bound by
`controls/EGA1_PRINTED55_SECTION60_614_62INTRO_DIRECT_AUTHORITY_IMAGES.csv`,
seven rows / 1,447 bytes / SHA-256
`1965466651C6FBF81973A4DB75309F50E6A7FE5DC1663337208E1A6A2718152D`.
It covers the 1400-dpi context page, direct 5000-dpi full page, and five
overlapping 5000-dpi bands. Manifest replay is 7/7 with size/hash errors 0;
the p.54 side of 6.0 remains bound by the preceding p.54 manifest.

Seven new dispositions are confirmed. The printed French begins 6.1.3 with
plural `Soient` before singular `M un ...`; the diplomatic body retains it
and English's grammatical normalization requires a visible source note.
English independently mangles the 6.0 footnote, prints `a flat A-modules`,
uses interrogative `is it necessary` in a declarative sentence, omits the
separator between $N'$ and $N''$, drops the second $\operatorname{Im}$ from
the right-hand side of the 6.1.4 submodule identity, and writes `multiple
modules structures`. Stable IDs are
`EG-EGA-I-P54-60-FOOTNOTE-CITED-OF-FROM-EN-001`,
`EG-EGA-I-P55-612-FLAT-A-MODULES-VS-MODULE-EN-001`,
`EG-EGA-I-P55-612-IS-IT-VS-IT-IS-EN-001`,
`EG-EGA-I-P55-613-SOIENT-VS-SOIT-SRC-TYPO-001`,
`EG-EGA-I-P55-613-MISSING-AND-EN-001`,
`EG-EGA-I-P55-614-MISSING-IM-RHS-EN-001`, and
`EG-EGA-I-P55-62-MODULES-STRUCTURES-VS-MODULE-STRUCTURES-EN-001`. The
English-recheck ledger now has 72 unique rows / 56,274 bytes / SHA-256
`9C7DE2AE913B4FDF4621D81561A8F7749414F27D1C2FA1B9996A279040F284F8`.

The bounded reader was rebuilt in three converged XeLaTeX passes as
`qa/ega1_chapter0_build/ega0-pages11-55-through-614-62intro-check-r33.pdf`,
42 A4 pages / 301,875 bytes / SHA-256
`9102756F4A26615E6FAEC3AB3F07BF78D16364FDF0858AB0439EDEA77CC3B71C`.
Passes 2 and 3 have identical console SHA-256
`C1A61AAA9AE4E9423CC762361EA47DB3F6D418512D4EBF66AE715004371148F3`;
fatal, missing-character, undefined-reference, rerun, overfull, and underfull
diagnostics are all zero. Output pages 40--42 were rendered at 1200 dpi and
personally inspected. Page 40 is 3,243,948 bytes / SHA-256
`525963B8F184F209096B00CEE9AA875D24DD46E768C929573574B16BD510083A`;
page 41 is 3,425,812 bytes / SHA-256
`77167E737B39FCEE5927F9D23838960FED8C8965236DC3064F8B2B5ADE7D8A2C`;
and page 42 is 1,918,087 bytes / SHA-256
`1C90CE65D2656670A14BBE5DE2DB7D6D8DADF22FAC948F907A2D0D3A73FFF42A`.
The p.54/p.55 seam, section and subsection numbering, citation text, source
footnote, exact sequences, tensor/image formulas, source grammar defect,
clipping, and page envelopes pass.

## EGA I through printed p.56 / complete 6.3.2

Complete 6.2.1--6.2.3 and 6.3.1--6.3.2 have been transcribed
diplomatically, including the printed-page-56 break inside 6.2.1. The
admitted French source is now 191,592 bytes, SHA-256
`746A77E2CA711DF2084051EBB08C7583C4F656A3ABC672750A131C2016C53A61`.
The next exact cursor is 6.3.3 on printed p.56, which crosses to p.57; no
6.3.3 text has been admitted.

The p.56 authority surface is bound by
`controls/EGA1_PRINTED56_SECTION621_623_631_632_DIRECT_AUTHORITY_IMAGES.csv`,
seven rows / 1,447 bytes / SHA-256
`728AF04240DE5039760D40E4ADDC3A2D2F3017BFD0DE958795010745F2DB0C8C`.
It covers one 1400-dpi context page, one direct 5000-dpi full page, and five
overlapping direct 5000-dpi bands. Manifest replay is 7/7 with size/hash
errors 0. The English comparison was checked through the same bounded unit;
no new substantive source-correction conflict or English mathematical
defect was found. The English-recheck ledger therefore remains 72 unique
rows / 56,274 bytes / SHA-256
`9C7DE2AE913B4FDF4621D81561A8F7749414F27D1C2FA1B9996A279040F284F8`.

The bounded reader was rebuilt in three converged XeLaTeX passes as
`qa/ega1_chapter0_build/ega0-pages11-56-through-632-check-r34.pdf`, 43 A4
pages / 306,535 bytes / SHA-256
`66BDF8635CFD51F1193FF4079D527B116BDDDE5CB89246B9B5097664378AE802`.
Passes 2 and 3 have identical console SHA-256
`7058A2C73E485145F307BA3DEFE6D233AA1E27F0219157EA2C2B4B562A342A55`;
fatal, missing-character, undefined-reference, rerun, overfull, and underfull
diagnostics are all zero. Output pages 41--43 were rendered at 1200 dpi and
personally inspected. Page 41 is 3,425,812 bytes / SHA-256
`77167E737B39FCEE5927F9D23838960FED8C8965236DC3064F8B2B5ADE7D8A2C`;
page 42 is 2,799,471 bytes / SHA-256
`5E84FED6AE4DD0235ED005043AC5C2A97DEFD99AC5FB3E902CB887A262648D88`;
and page 43 is 1,827,876 bytes / SHA-256
`076EC68F28A5655425C4334E10DC51CA22A6FEE0CA81BDC5D50D659711D8AA30`.
The p.55/p.56 seam, tagged Hom formula, inductive-limit formula, subsection
transition, localization identities, margin locator, clipping, and page
envelopes pass.

## EGA I through printed p.57 / complete 6.4.1

Complete 6.3.3 across the p.56/p.57 seam, complete 6.3.4, and complete 6.4.1
have been transcribed diplomatically. The admitted French source is now
195,972 bytes, SHA-256
`DFDA4F3C4A60EC3E4613EDE672E133C7F5E5DE51E05445D4A8857CEDD0E9FD90`.
The next exact cursor is 6.4.2 on printed p.58; no 6.4.2 text has been
admitted.

The p.57 authority surface is bound by
`controls/EGA1_PRINTED57_SECTION633_634_641_DIRECT_AUTHORITY_IMAGES.csv`,
seven rows / 1,447 bytes / SHA-256
`225AAD25B7CD588994C8246F6590A04F3FADD61B52E8194F686BFFF034C15E87`.
It covers one 1400-dpi context page, one direct 5000-dpi full page, and five
overlapping direct 5000-dpi bands. Manifest replay is 7/7 with size/hash
errors 0.

Eight new source/English dispositions are bound. The printed French in
6.3.4 visibly says `et != {0}` without the subject $B$; the diplomatic body
retains that source omission and English must restore $B\neq\{0\}$ with a
visible source note. English independently misspells `homomorphism`, writes
`none other that`, mistranslates `n'est pas diviseur de 0` as `does not
divide 0`, writes `follows ... from that`, loses the conjunction in 6.4.1
items $b)$ and $d)$, and in item $c)$ both loses the conjunction and wholly
omits the conclusion $v=0$. Stable IDs are
`EG-EGA-I-P57-633-HOMOMORHISM-VS-HOMOMORPHISM-EN-001`,
`EG-EGA-I-P57-633-THAT-VS-THAN-EN-001`,
`EG-EGA-I-P57-634-DIVIDE-ZERO-VS-ZERO-DIVISOR-EN-001`,
`EG-EGA-I-P57-634-FROM-THAT-VS-FROM-THE-FACT-EN-001`,
`EG-EGA-I-P57-634-MISSING-B-BEFORE-NEQ-SRC-TYPO-001`,
`EG-EGA-I-P57-641-B-MISSING-AND-EN-001`,
`EG-EGA-I-P57-641-C-MISSING-IMPLIES-V-EQUALS-ZERO-EN-001`, and
`EG-EGA-I-P57-641-D-MISSING-AND-EN-001`. The English-recheck ledger now has
80 unique rows / 61,977 bytes / SHA-256
`67A07EFE5792C6CC69A11312DC724285FE32E2EE4D97000FFC8DF4EE846673B1`.

The bounded reader was rebuilt in three converged XeLaTeX passes as
`qa/ega1_chapter0_build/ega0-pages11-57-through-641-check-r35.pdf`, 44 A4
pages / 311,283 bytes / SHA-256
`F554E94F990D817146A58077545C2746F7F761041B65B0352D3082BED2DE753D`.
Passes 2 and 3 have identical console SHA-256
`48023EF3871B8605CB7CA0EFF29B209032CABCD67713F7416B57FF5666D8714C`;
fatal, missing-character, undefined-reference, rerun, overfull, and underfull
diagnostics are all zero. Output pages 42--44 were rendered at 1200 dpi and
personally inspected. Page 42 is 2,799,471 bytes / SHA-256
`5E84FED6AE4DD0235ED005043AC5C2A97DEFD99AC5FB3E902CB887A262648D88`;
page 43 is 2,836,583 bytes / SHA-256
`C1048A887503A57D7AE012A995945E5A34423F11894784A828A06D7033DDDA09`;
and page 44 is 2,202,501 bytes / SHA-256
`032DA974C4C2DC397EA43DDE77346602FAF600F845A2F02989CF2FDBBDC1B4AF`.
The p.56/p.57 seam, all localization displays, retained source omission,
6.4 transition, four-condition list, clipping, and page envelopes pass.

## EGA I through printed p.58 / complete 6.5.2

Complete 6.4.2--6.4.5 and 6.5.1--6.5.2 have been transcribed
diplomatically. The admitted French source is now 199,269 bytes, SHA-256
`006DFC0A52E7EB879648591B4FC87670B105A88786E091A03C46F5B4D558F00E`.
The next exact cursor is the 6.6 heading and 6.6.1 on printed p.58, which
crosses to p.59; neither the heading nor any 6.6.1 text has been admitted.

The p.58 authority surface is bound by
`controls/EGA1_PRINTED58_SECTION642_645_651_652_DIRECT_AUTHORITY_IMAGES.csv`,
seven rows / 1,447 bytes / SHA-256
`78BC0A6854B3B1705A9C72240EB75AFB2E4F01CA169A1B342BF8FEBE4ADE1A1D`.
It covers one 1400-dpi context page, one direct 5000-dpi full page, and five
overlapping direct 5000-dpi bands. Manifest replay is 7/7 with size/hash
errors 0. French has no newly identified source defect in this unit.

Two new English dispositions are confirmed. In 6.4.2 English changes the
necessary condition `only if` into `if`, reversing the logical direction;
6.4.5 also prints plural `a faithfully flat A-modules`. Stable IDs are
`EG-EGA-I-P58-642-IF-VS-ONLY-IF-EN-001` and
`EG-EGA-I-P58-645-A-MODULES-VS-A-MODULE-EN-001`. The English-recheck ledger
now has 82 unique rows / 63,427 bytes / SHA-256
`B0ED90E7BE413555FA0FF3B30E30A823F0B2869854AA1254F6FFC862921F7BD5`.

The bounded reader was rebuilt in three converged XeLaTeX passes as
`qa/ega1_chapter0_build/ega0-pages11-58-through-652-check-r36.pdf`, 45 A4
pages / 315,041 bytes / SHA-256
`95917CC03E3FABCBF3669BE4DC035D5F49BE5ACDA96FDB8FAC950B8664A47958`.
Passes 2 and 3 have identical console SHA-256
`E9C79F315FD9F4ED909AF28BEB9060B2B75442A5845E7CE3004BCB27D321E70E`;
fatal, missing-character, undefined-reference, rerun, overfull, and underfull
diagnostics are all zero. Output pages 43--45 were rendered at 1200 dpi and
personally inspected. Page 43 is 2,836,583 bytes / SHA-256
`C1048A887503A57D7AE012A995945E5A34423F11894784A828A06D7033DDDA09`;
page 44 is 3,220,453 bytes / SHA-256
`C8999B67033C58AAE938E0F2D788B4C33944DCB11637B5D929ECB601E53B6174`;
and page 45 is 1,432,058 bytes / SHA-256
`D6B35686FDF1BCFD18377173489A71914124B3224560573DBB36C68F6E42626F`.
The p.57/p.58 seam, exact sequence, base-change identity, 6.5 transition,
ideal formulas, clipping, and page envelopes pass.

## EGA I through printed p.59 / complete 6.7.2

The complete 6.6 heading, 6.6.1 across the p.58/p.59 seam, 6.6.2--6.6.4,
the 6.7 heading, and 6.7.1--6.7.2 have been transcribed diplomatically. The
admitted French source is now 203,404 bytes, SHA-256
`E7B1880BCA2ECCDF5C59B998C53254221F21EA15C08D7CDC744BC6472C5CA3FF`.
The next exact cursor is 6.7.3 on printed p.59, which crosses to p.60; no
6.7.3 text has been admitted.

The p.59 authority surface is bound by
`controls/EGA1_PRINTED59_SECTION661_664_671_672_DIRECT_AUTHORITY_IMAGES.csv`,
seven rows / 1,447 bytes / SHA-256
`46682F34F101948F853CC8BACA93EA5E3160DF016784E015D17ECB5FD50309AA`.
It covers one 1400-dpi context page, one direct 5000-dpi full page, and five
overlapping direct 5000-dpi bands; manifest replay is 7/7 with errors 0.

The inherited English 6.6.2 replacement and 6.7.1 insertion were separately
rechecked against the direct EGA II errata/addenda authority. EGA II physical
page 214 / printed page 217, rendered directly at 5000 dpi, is 5,918,370
bytes / SHA-256
`33244FCCC124FDCE60F914E761D0200ADBCF5B93C949DA4585F802ECD62FD61A`;
its one-row manifest is
`controls/EGA2_PHYSICAL214_EGA1_662_671_ERRATA_ADDENDA_DIRECT_AUTHORITY_IMAGE.csv`,
290 bytes / SHA-256
`2480045D4ABDFB477D44EFF5116B84DDD6ED2FA2A4BB20CE913C2AB67EF5F6EE`.
Both English editorial changes are exactly supported by the official EGA II
printing, while the diplomatic French body retains the original EGA I text.
One independent English defect is newly confirmed: 6.6.1 prints a period
after `A-module M` where the continuing clause requires a comma. The ledger
now has 85 unique rows / 65,928 bytes / SHA-256
`EE1E740681900BDF79B611E79D86BB129AD526177E1A18476248D98D44DA9641`.

The bounded reader was rebuilt in three converged XeLaTeX passes as
`qa/ega1_chapter0_build/ega0-pages11-59-through-672-check-r37.pdf`, 46 A4
pages / 319,537 bytes / SHA-256
`AE962AB263ACD96D95177F4AD9890ADD8B8EFAF289C40226F540F381D0012B32`.
Passes 2 and 3 have identical console SHA-256
`6718B4DA395258F085E9406504E1A5B3FED3DC40AF8E9FCA6681089616128D3E`;
fatal, missing-character, undefined-reference, rerun, overfull, and underfull
diagnostics are all zero. Output pages 44--46 were rendered at 1200 dpi and
personally inspected. Page 44 is 3,220,453 bytes / SHA-256
`C8999B67033C58AAE938E0F2D788B4C33944DCB11637B5D929ECB601E53B6174`;
page 45 is 3,059,301 bytes / SHA-256
`E5FE326A05264C1207958D9E71A9C709DC9C15FD270A172B8FF3ACCA78BCE1AF`;
and page 46 is 1,335,428 bytes / SHA-256
`2775A76D2C289B26157F3DA5F004E1DA8FB90016C7750D7BC20375FD6CAC5A9B`.
The p.58/p.59 seam, five-condition list, retained original 6.6.2 proof,
6.6/6.7 transition, stalk formulas, clipping, and page envelopes pass.

## EGA I through printed p.60 / complete 7.1.1

Complete 6.7.3 across the p.59/p.60 seam, 6.7.4--6.7.6, 6.7.8, the
section-7 and 7.1 headings, and 7.1.1 have been transcribed diplomatically.
The source's direct jump from 6.7.6 to 6.7.8 is retained without silently
renumbering it. The admitted French source is now 207,550 bytes, SHA-256
`56983D016FAE9271CF8C306C7D3F60F7F89D0AFB641F4E2CBCB7D187ABAC8DD2`.
The next exact cursor is Definition 7.1.2 on printed p.60, which crosses to
p.61; no 7.1.2 text has been admitted.

The p.60 authority surface is bound by
`controls/EGA1_PRINTED60_SECTION673_678_711_DIRECT_AUTHORITY_IMAGES.csv`,
seven rows / 1,447 bytes / SHA-256
`634F47AD20AA8FF26EF1872D7286D868A389408C33DA08B1E9B40C44C6108221`.
It covers one 1400-dpi context page, one direct 5000-dpi full page, and five
overlapping direct 5000-dpi bands; replay is 7/7 with errors 0.

Six new English dispositions are confirmed. In 6.7.4 English writes `with
are` and `a ... modules`; in 6.7.6 it writes plural `questions`, uses `have
reduced`, and, substantively, reverses the French `left exact` assertion to
`right exact`; in 6.7.8 it ends after `is` and omits the predicate that
$f^*(\mathcal G)$ is also $Y$-flat. The ledger now has 91 unique rows /
70,001 bytes / SHA-256
`C90F445519FB3A88797D521797663A4B1A899A0068897A1C3C9934DEC9D5BBFA`.

The bounded reader was rebuilt in three converged XeLaTeX passes as
`qa/ega1_chapter0_build/ega0-pages11-60-through-711-check-r38.pdf`, 47 A4
pages / 323,586 bytes / SHA-256
`35DADAF587129C410F1DF581449B0DD213027F25334C338828A1D672D3280DDB`.
Passes 2 and 3 have identical console SHA-256
`A00E0BC7BBCD49B7734B78A52E725693E5E52C36BBC28BC05EF30BB38B5FF714`;
fatal, missing-character, undefined-reference, rerun, overfull, and underfull
diagnostics are all zero. Output pages 45--47 were rendered at 1200 dpi and
personally inspected. Page 45 is 3,059,301 bytes / SHA-256
`E5FE326A05264C1207958D9E71A9C709DC9C15FD270A172B8FF3ACCA78BCE1AF`;
page 46 is 3,513,647 bytes / SHA-256
`822258F085CC5A754A23448CB4283D70E48118B88E64DD13DF44BC15738D74CC`;
and page 47 is 822,877 bytes / SHA-256
`6A969DC54822CEC2763918749DF81788907E6D2201A90C82702D3A66661796BC`.
The p.59/p.60 seam, exact sequence, Hom display and tag, retained numbering,
section transition, clipping, and page envelopes pass.

## EGA I through printed p.61 / complete 7.1.6

Definition 7.1.2 across the p.60/p.61 seam, Lemma 7.1.3, Proposition
7.1.4, and Corollaries 7.1.5--7.1.6 have been transcribed diplomatically.
The printed theorem-type headings are retained explicitly; the bounded QA
wrapper now supplies matching French statement environments without changing
the source wording. The admitted French source is 211,874 bytes, SHA-256
`69222FB71F35905E5EC4744AC2DBCE06ADE2C3BABFF5BDF477D93E67446EB910`.
The next exact cursor is Corollary 7.1.7 on printed p.62; no 7.1.7 text has
been admitted.

The p.61 authority surface is bound by
`controls/EGA1_PRINTED61_SECTION712_716_DIRECT_AUTHORITY_IMAGES.csv`, seven
rows / 1,447 bytes / SHA-256
`03F54754548026D57E6445BEEBFC8ACE730F96BE00D4CC7C996848DC12ECC3C3`.
It covers one 1400-dpi context page, one direct 5000-dpi full page, and five
overlapping direct 5000-dpi bands; replay is 7/7 with errors 0.

Five new English grammar defects are confirmed against the source: `a
integer` in 7.1.2; missing `is` in the proof of 7.1.4; singular `that` for
the plural notation and hypotheses in 7.1.6; the malformed 7.1.6 existence
criterion; and the spurious `and` in the final $A_{\mathrm{red}}$ notation
sentence. No mathematical/source correction is introduced into the French
body. The ledger now has 96 unique rows / 73,652 bytes / SHA-256
`807B29B2E2E309A05A36851B0BD568DBFC86729A881C771D2848A0066A678ABE`.

The bounded reader was rebuilt in three converged XeLaTeX passes as
`qa/ega1_chapter0_build/ega0-pages11-61-through-716-check-r39.pdf`, 48 A4
pages / 329,654 bytes / SHA-256
`88278F266E4FD5A3D217C4D5A287CD512859657AA0E641193F32BB0DC04236B1`.
Passes 2 and 3 have identical console SHA-256
`16BF8B4B7F5F494D63864578C081A4959FBF3C35BA1F4845F590DB16B5A67F76`;
fatal, missing-character, undefined-reference, rerun, multiply-defined,
duplicate-destination, overfull, and underfull diagnostics are all zero.
Output pages 46--48 were rendered at 1200 dpi and personally inspected. Page
46 is 3,513,647 bytes / SHA-256
`822258F085CC5A754A23448CB4283D70E48118B88E64DD13DF44BC15738D74CC`;
page 47 is 3,220,301 bytes / SHA-256
`6D38376D9CDF5F985C6978489A56719F5DC1312EF6AA2FCADB7FB043DF2F50FA`;
and page 48 is 879,157 bytes / SHA-256
`0F8F6A41C7415A05ABC9334376296600F9EDACDE82D7DA2EA299D16E1C28CF0B`.
The page marker seam, statement/proof typography, list labels, fraktur
symbols, exponents, final quotient notation, clipping, and page envelopes
pass.

## EGA I through printed p.62 / complete 7.1 and 7.2 heading

Corollaries 7.1.7--7.1.8, Definition 7.1.9 and its notation paragraph,
Proposition 7.1.10, Corollaries 7.1.11--7.1.14, the complete proof, and the
7.2 heading have been transcribed diplomatically. The admitted French source
is 215,508 bytes, SHA-256
`52CFC6A0EF8956A0E65B3D8E3A692AA64BA6E329624BF5BE0EDC14D1119CEB33`.
The next exact cursor is 7.2.1 on printed p.62, which crosses to p.63; no
7.2.1 text has been admitted.

The p.62 authority surface is bound by
`controls/EGA1_PRINTED62_SECTION717_7114_72INTRO_DIRECT_AUTHORITY_IMAGES.csv`,
seven rows / 1,447 bytes / SHA-256
`877A516F22E787D3CEC096C92E482DE4F5910F2E3162B6B93EC90791F59D34B2`.
It covers one 1400-dpi context page, one direct 5000-dpi full page, and five
overlapping direct 5000-dpi bands; replay is 7/7 with errors 0. A first band
crop invocation failed to preserve the full-page image on its stack after
the initial crop; those unused `r1` band artifacts are excluded. The
manifested `r2` bands were regenerated directly from the exact full-page
witness and personally inspected.

Two new English defects are confirmed: 7.1.14 omits the predicate that the
induced map is surjective, and the proof duplicates the 7.1.10 reference in
the sentence relating 7.1.10 and 7.1.13. The ledger now has 98 unique rows /
75,120 bytes / SHA-256
`8831FBB0D1B556DC9CC8F1DF9C8D64F6E3ED343C4E2808943AEF30640B5AFB2B`.

The bounded reader was rebuilt in three converged XeLaTeX passes as
`qa/ega1_chapter0_build/ega0-pages11-62-through-72intro-check-r40.pdf`, 48
A4 pages / 334,188 bytes / SHA-256
`92CF6A6C128A0849F6EAA1EB661D761F6E6663C49903E4335327BDE2BD3B026E`.
Passes 2 and 3 have identical console SHA-256
`BF7A7EEACE5965C15044CB4063B45CD833DCC4947FD2CC4B833A0636BB5455AD`;
all checked diagnostics are zero. Output pages 47--48 were rendered at 1200
dpi and personally inspected. Page 47 is 3,220,301 bytes / SHA-256
`6D38376D9CDF5F985C6978489A56719F5DC1312EF6AA2FCADB7FB043DF2F50FA`;
page 48 is 3,356,685 bytes / SHA-256
`6180F59D3D8ABCDC230F528631B8401219A688847F2D8D8DAE9E7B3338C46C6B`.
The p.61/p.62 marker, theorem typography, inline tensor map, Bourbaki
citation, geometric series, 7.2 transition, clipping, and page envelope pass.

## EGA I through printed p.63 / complete 7.2.4

The complete p.62/p.63 unit 7.2.1, Lemma 7.2.2 and its proof, 7.2.3, and
Proposition 7.2.4 and its proof have been transcribed diplomatically. The
admitted French source is 219,631 bytes, SHA-256
`B4E394E896495784839CFD45036349C06FA1E28E92C3E0D93FC18AD652B40E1C`.
The next exact cursor is Corollary 7.2.5 on printed p.63, which crosses to
p.64; no 7.2.5 text has been admitted.

The p.63 authority surface is bound by
`controls/EGA1_PRINTED63_SECTION721_724_DIRECT_AUTHORITY_IMAGES.csv`, seven
rows / 1,447 bytes / SHA-256
`8CA2E17263D239A2B5133947B1FAB092AE3A08A737D1A2C035F8A8CF8A9CBDD4`.
It covers one 1400-dpi context page, one direct 5000-dpi full page, and five
overlapping direct 5000-dpi bands; replay is 7/7 with errors 0.

Six English defects are confirmed. In 7.2.1, `complete` is changed to the
mathematically different `compact`; in 7.2.2, a projective system is called a
projective limit, the index-set noun is lost, `surjective` is misspelled, and
`ideals of definition` is pluralized incorrectly; in 7.2.3, the source's
intersection $\bigcap_n\mathfrak J^n=0$ is reversed to a union. The ledger
now has 104 unique rows / 79,486 bytes / SHA-256
`7A53979127C12062692F55E601AF68F6C66D958EE51C0E344AA84A72A244C26B`.

The bounded reader was rebuilt in three converged XeLaTeX passes as
`qa/ega1_chapter0_build/ega0-pages11-63-through-724-check-r41.pdf`, 49 A4
pages / 338,837 bytes / SHA-256
`EFF056875D4C4258897846C8D759B3B11025BF5E708A0EE502B2DD94D88871C9`.
Passes 2 and 3 have identical console SHA-256
`A26572AD94E35C68C000437BF963784AAC00E80B6597C20501691DE4B8FA957C`;
all checked diagnostics are zero. Output pages 48--49 were rendered at 1200
dpi and personally inspected. Page 48 is 3,540,370 bytes / SHA-256
`23D5A6D6528533450ADA6BF5AFB5DCCC9C055334C8729823FEFE41DE9A8CF831`;
page 49 is 2,768,443 bytes / SHA-256
`C5DC2E5543484957792AE577AA67DDB5B92AD5EDF4A9069E64A95E28AB826FBB`.
The p.62/p.63 seam, inverse-limit symbols, index notation, intersection,
completion maps, theorem typography, clipping, and page envelopes pass.

## EGA I through printed p.64 / complete 7.2.6

Corollary 7.2.5 across the p.63/p.64 seam and Corollary 7.2.6 with its proof
have been transcribed diplomatically. The admitted French source is 221,260
bytes, SHA-256
`164886484D2F354B8DAF7652DAC6702F38968E41887E4085E906121B3D536C14`.
The next exact cursor is Proposition 7.2.7 on printed p.64, which crosses to
p.65; no 7.2.7 text has been admitted.

The p.64 authority surface is bound by
`controls/EGA1_PRINTED64_SECTION725_726_DIRECT_AUTHORITY_IMAGES.csv`, seven
rows / 1,447 bytes / SHA-256
`F5F0A65DA113928401C5969130E93709F70694799AB8BCCDA5755D43A9B0F3E4`.
It covers one 1400-dpi context page, one direct 5000-dpi full page, and five
overlapping direct 5000-dpi bands; replay is 7/7 with errors 0.

Four new English defects are confirmed: `bicontinous` for `bicontinuous` in
7.2.5; a duplicated `A` in the 7.2.6 statement; omission of the predicate
that the associated graded ring is Noetherian; and `a A/J-module` instead of
`an A/J-module`. The ledger now has 108 unique rows / 82,187 bytes / SHA-256
`4811A80272E7B6B2B6BD02FF9C336F22A68D175E32BB4549BA6B58CCB5903598`.

The bounded reader was rebuilt in three converged XeLaTeX passes as
`qa/ega1_chapter0_build/ega0-pages11-64-through-726-check-r42.pdf`, 50 A4
pages / 341,080 bytes / SHA-256
`9FC0CBB681C799BDE99E9F38B6DB02095C6F88B25E2857FB5062C869E38C1FF1`.
Passes 2 and 3 have identical console SHA-256
`B6DE06A3F857E1686415B08D7CDB8D5AB739E19ADAD0EBB99929E0B6018AE905`;
all checked diagnostics are zero. Output pages 49--50 were rendered at 1200
dpi and personally inspected. Page 49 is 3,638,943 bytes / SHA-256
`5ABEE3C9D0345C4E9434AEA5FEDC3B2D7CCEE74C717EB91DD4F74970757C82B8`;
page 50 is 646,446 bytes / SHA-256
`E84B764ADDDAAEEC6BD6DE9EA40DD131011F60664B265C0F5D1D5BFC117CB767`.
The p.63/p.64 seam, corollary list, powers and quotients, graded-ring
notation, citation, polynomial ring, clipping, and page envelopes pass.

## EGA I through printed p.65 / complete 7.2.10

Proposition 7.2.7 across the p.64/p.65 seam, Corollary 7.2.8,
Proposition 7.2.9, and Corollary 7.2.10 with their proofs have been
transcribed diplomatically. The admitted French source is 228,325 bytes /
4,845 lines / SHA-256
5DF72B3392DBADB9C3328F2CB7540E38312563092D1C59AAE4DD03EC2E41B3ED.
The next exact cursor is Remark 7.2.11 on printed p.65, which crosses to
p.66; no 7.2.11 text has been admitted.

The p.65 authority surface is bound by
controls/EGA1_PRINTED65_SECTION727_7210_DIRECT_AUTHORITY_IMAGES.csv, seven
rows / 1,447 bytes / SHA-256
E17C62749CA61C6B2F2DAF9CC8BB7F99C1DA1A3D58AC5657FCE59A10479BAF31.
It covers one 1400-dpi context page, one direct 5000-dpi full page, and five
overlapping direct 5000-dpi bands; replay is 7/7 with errors 0.

Six source-backed English dispositions are added. Two ordinary transcription
errors are “and the a_j” for “in the a_j” and duplicated “to”; the canonical
map in the 7.2.9 proof loses the factor M; and the continuity clause in
7.2.10 has singular agreement for a plural antecedent. Two printed French
source defects are retained diplomatically: classes modulo M^(0) would all
vanish and must mathematically be classes modulo M^(1), while
J^(n)M=M^(n) is the kernel of M→M_(n-1), not M→M_n. The latter confirms
that the existing English erratum correction is justified. The ledger now
has 114 unique rows / 86,824 bytes / SHA-256
51FAE3C1233B7FDCA0B0C758C4F13BB5C749A737A86302ABF2DE06A106C2842C.

The bounded reader was rebuilt in three converged XeLaTeX passes as
qa/ega1_chapter0_build/ega0-pages11-65-through-7210-check-r43.pdf, 51 A4
pages / 349,890 bytes / SHA-256
DA44BCB63605AF4B422816D9C3AF83C4043F93EA2F7BCA81A12875E34545775C.
Passes 2 and 3 have identical console SHA-256
D839C2544F7EB2ADB3CACDB3C5921036E8917109725A6839E3F23C0D9A5BA8A7;
all checked diagnostics are zero. Output pages 50--51 were rendered at 1200
dpi and personally inspected. Page 50 is 3,940,359 bytes / SHA-256
D5446AD9EAF3DE399588897E7BB007A99B241CC7DE3F7D51356A68DEE8A693AF;
page 51 is 1,851,943 bytes / SHA-256
D1B92E185AD7DF73C0429755CC12C55B896D445F8EEA0A2FAFC1E3EDDECE0FBB.
The p.64/p.65 seam, inverse-limit indices, filtration powers, projective
systems, quotient and tensor-product formulas, statement/proof boundaries,
clipping, and page envelopes pass.

## EGA I through printed p.66 / complete 7.3.2.1

Remark 7.2.11 across the p.65/p.66 seam, Example 7.2.12, the 7.3 heading,
7.3.1, Krull's Theorem 7.3.2, and the Artin--Rees Lemma 7.3.2.1 have been
transcribed diplomatically. The admitted French source is 232,399 bytes /
4,943 lines / SHA-256
00F9756104A5EC737A024AF23F9A63D649BE321A7F172B4AC774175B1FA574F3.
The next exact cursor is Corollary 7.3.3 on printed p.67; no 7.3.3 text has
been admitted.

The p.66 authority surface is bound by
controls/EGA1_PRINTED66_SECTION7211_7321_DIRECT_AUTHORITY_IMAGES.csv, eight
rows / 1,684 bytes / SHA-256
B5669D92399E248E6BCDAF4F43DA21254CDBBCCEF331C0D2A4FE9DF9E7B12A6C.
It covers one 1400-dpi context page, one direct 5000-dpi full page, five
overlapping direct 5000-dpi bands, and one targeted direct 5000-dpi crop;
replay is 8/8 with errors 0. The targeted crop proves that the printed second
inverse-limit subscript in 7.3.1 is u, not n.

Three source-backed English dispositions are added. The English correction
from the printed inverse-limit subscript u to the mathematically required n
is confirmed as source-justified, while canonical French retains u. The
phrase “coincide with the z” omits “those of”, and the Noetherian sentence
contains an English comma splice. The ledger now has 117 unique rows /
89,159 bytes / SHA-256
3F56E5F7F24E321BB7AECECFC26174937139527744AD834A7CF509ED3CFD3652.

The bounded reader was rebuilt in three converged XeLaTeX passes as
qa/ega1_chapter0_build/ega0-pages11-66-through-7321-check-r44.pdf, 52 A4
pages / 355,473 bytes / SHA-256
BD1AD40130731C8E75C4D6FFB1D930E0D994FF1E0097733967DD475EE132A85A.
Passes 2 and 3 have identical console SHA-256
BF131B661A21612535CD1C90A46C44B8E9AADBD951BBBFFD1468546D03884A37;
all checked diagnostics are zero. Output pages 51--52 were rendered at 1200
dpi and personally inspected. Page 51 is 3,761,495 bytes / SHA-256
AC32143123DB98E227A503B1E802B5DF0918FC435768C9886F1B4DE4522AA1F9;
page 52 is 1,211,406 bytes / SHA-256
080F04F2D05E2BF78596BEDBC7613378CCBD44930E4A8C37C160510F8393E3AB.
The p.65/p.66 seam, closure bars, inverse-limit indices, exact sequences,
completion hats, Krull/Artin--Rees statements, clipping, and page envelopes
pass.

## EGA I through printed p.67 / complete 7.3.4

Corollary 7.3.3 with its proof and Corollary 7.3.4 have been transcribed
diplomatically. The commutative completion diagram in 7.3.3 is reconstructed
as native TikZ-cd from the direct 5000-dpi authority image. The admitted
French source is 234,944 bytes / 5,010 lines / SHA-256
C56C46877E10DCC2D3E8050E752C0FC56C5A9C7DBC930F5C277FEBD6BCA45188.
The next exact cursor is Corollary 7.3.5 on printed p.67, which crosses to
p.68; no 7.3.5 text has been admitted.

The p.67 authority surface is bound by
controls/EGA1_PRINTED67_SECTION733_734_DIRECT_AUTHORITY_IMAGES.csv, seven
rows / 1,481 bytes / SHA-256
5DBA53780E8CEC0EC459F39F1E189B8A988525F9C8DDAC4F8C4999B3FAE22594.
It covers one 1400-dpi context page, one direct 5000-dpi full page, and five
overlapping direct 5000-dpi bands; replay is 7/7 with errors 0. No new
English defect was found in the admitted 7.3.3--7.3.4 range; the English
ledger remains 117 unique rows / 89,159 bytes / SHA-256
3F56E5F7F24E321BB7AECECFC26174937139527744AD834A7CF509ED3CFD3652.

The bounded reader was rebuilt in three converged XeLaTeX passes as
qa/ega1_chapter0_build/ega0-pages11-67-through-734-check-r45.pdf, 52 A4
pages / 359,144 bytes / SHA-256
8542F9A492F245FBC2CA656D23E3CF027076A50F9CAF7D3EF702C992DFE0FA1F.
Passes 2 and 3 have identical console SHA-256
B9F7FAE777D48400536463D1BD61565947AFA9934E691348EA0DA2EF3863332E;
all checked diagnostics are zero. Output page 51 is byte-identical to the
already-inspected R44 page, and output page 52 was rendered at 1200 dpi and
personally inspected: 2,753,631 bytes / SHA-256
BF1EA4FE16215514A693EDF0FF129304388659E65AB18DC0048AD18E9CB35DCE.
The p.66/p.67 seam, completion maps, exact rows, all six diagram arrows,
tensor/Hom completion formulas, clipping, and page envelope pass.
