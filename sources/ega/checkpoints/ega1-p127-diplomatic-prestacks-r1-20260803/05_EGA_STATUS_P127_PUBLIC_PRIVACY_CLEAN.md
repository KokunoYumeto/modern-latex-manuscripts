# Status

Date: 2026-08-02

Status: ACTIVE — canonical French source transcription.

Authority closure: eight NUMDAM PDFs, 1,800 physical PDF pages total; exact
identities are in `controls/AUTHORITY_SHA256.csv`.

Current production volume: EGA I.

## Controlling quick status — 2026-08-02, through printed p.77 / 7.7.8

This block supersedes every older point-in-time quick-status block below; they
remain append-only history.

- The admitted diplomatic French source now includes the complete §7.7 heading,
  paragraphs 7.7.1--7.7.6, Proposition 7.7.7 and proof, and Proposition 7.7.8
  and proof on printed pp.75--77. No §7.8 text is admitted.
- `source/ega1/ega0-1-fr.tex`: 277,633 bytes / 5,878 lines / SHA-256
  `1D94EA4889F450CB70BAA4EFD2BB78779F843235064B6350C8941BF1261F5809`.
  Exact next cursor: the §7.8 heading and paragraph 7.8.1 on printed p.77,
  continuing onto p.78.
- Direct authority evidence:
  `controls/EGA1_PRINTED75_77_SECTION77_DIRECT_AUTHORITY_IMAGES.json`, 4,998
  bytes / SHA-256
  `6E728F658C5D14E9E36E7D4C069E1AA2F77E6B888CEB3C78C31F12CD2FD3C0E8`.
  It binds nine direct 5,000-dpi source bands. The lead personally read every
  admitted line; extraction remained locator material only.
- Printed French 7.7.6 repeats `et un seul` within one uniqueness clause. The
  diplomatic French preserves both occurrences. English states uniqueness once
  and carries the immediate visible stable-ID note
  `EG-EGA-I-P76-776-DUPLICATE-ET-UN-SEUL-SRC-001`.
- Six new English decisions are individually justified in
  `controls/ENGLISH_CORRECTION_RECHECK_APPEND_P77_20260802.jsonl`, six rows /
  9,404 bytes / SHA-256
  `41BF40298FAF27C1B5825A97E18FE2447890C18E682D5188EE7AF699F432413D`.
  Their six applied events are in
  `controls/ENGLISH_CORRECTION_REPAIR_APPLICATION_P77_20260802.jsonl`, 6,517
  bytes / SHA-256
  `C0B96FC24F1238951C1872FFE98D24E8CEDED30BB5DB1DC6197199D89000DC91`.
- Current English source: `source/ega0/ega0-7.tex`, 75,620 bytes / 1,397 lines /
  SHA-256
  `29008BF15E3674F9B84BACDC8168B38E3C2B4B25497B153B2F96C744629749D8`.
  The R10 manifest is 24,749 bytes / SHA-256
  `D564A77B667290642B5206B29EC32FD667552D543642CE30F6ADF5D08DF325AE`;
  independent Python and PowerShell replay 127/127 rows, 7,280,208 bytes, and
  ordinal tree SHA-256
  `07BA24509DBA3162F680445DD535574044B3BB0E6E2BE03604EAFCA170CB71E7`.
  R10 diff validation is 6,716 bytes / SHA-256
  `C4EF8A240F3CEC321AA4437F4D810343E2F06B953F7A8736C99C39775FFD7444`;
  replay is 3,628 bytes / SHA-256
  `B43869F4F6BC4B04D86E98AC5CE530BF8602360DC3EE70865033D420DFA52A61`.
  Both pass with errors empty, and exact inverse reconstruction reproduces the
  R9 English source identity.
- The bounded French reader is R62: 61 A4 pages / 407,900 bytes / SHA-256
  `9CB826D387B962B2B3F8305F0E2253AB41CBD1F410B5F2070D43E737AB434875`.
  Passes 2 and 3 are identical (SHA-256
  `80E1AB98AE356AA89684A8B863AF0C93BF8FFDBF20735B7FC56455A8C2CD5007`)
  and all checked diagnostics are zero. Output pages 60--61 were personally
  inspected at 1,200 dpi and pass line flow, formulas, seam, clipping, and page
  envelope. A local `sloppypar` in 7.7.2 is a logged typesetting-only measure
  that removes a 9.62384 pt overflow without changing visible source content.
- The complete decision surface is 153 records. Thirty-two cumulative English
  repairs are applied; four source-faithful no-edit decisions remain. No
  admitted English correction has been reversed.
- Corpus progress is 74 source-bearing pages out of 1,800 (4.1%); approximately
  1,726 physical pages remain. Global rebuild, reference-coordinate replay,
  privacy-clean projection, rights/package closure, archive handoff, public
  readback, and dual-DOI logbook binding remain held. No upload occurred.

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
  `03_projects/language_management/english_germanic/03_working_translations/EGA_English_Global_0_IV_french_recheck_source_successor_20260802_r1`.
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
  `03_projects/language_management/english_germanic/03_working_translations/EGA_English_Global_0_IV_french_recheck_source_successor_20260802_r1`.
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
calls $w:\mathcal G_1\to\mathcal G_2$ a homomorphism of presheaves of sets,
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

## Current continuation — EGA I through printed p.78 / complete §7.8 text

The diplomatic French source now includes §7.8 through `(A suivre.)` on
printed p.78: 282,088 bytes / SHA-256
`359E04723FCCB70D8BB758184B85C4A6A467ACC549A7B5F7D40A0AE92FF053AC`.
The inherited English §7.8 has four source-backed repairs and is now 75,637
bytes / SHA-256
`96983D270206173230D51B70885CB846FD03BB1692D5DFAC03667EE7F4156252`.
Decision ledger SHA-256:
`FA9F3D79F64EB856EF919934E44F581D24641719B8ED0662FDB73D472AB23811`;
application ledger SHA-256:
`BE5F779257515C1705A26FDBF623FE89714E7F0B747A0A6C70A384EBCE96739C`;
exact inverse replay validation SHA-256:
`FEF06E5F4EBBF4A9F5FB4BB2B161471BAC4F127BB9699B397757C8F32605DDE5`.

This is not yet a built §7.8 checkpoint. The next operation must remain small,
sequential, and RAM-light: first regenerate the bounded source identity, then
run at most one serialized build when genuinely needed. No bulk rendering,
image batch, OCR, parallel heavy work, or release-scale audit is authorized.
Image evidence is one tightly relevant crop at a time, at the minimum useful
resolution; 5,000 dpi is reserved for an actually ambiguous small detail.
Existing Codex/Claude page renders and detail crops must be searched and reused
first; a new crop is permitted only when the required source detail is absent
or inadequately represented.
Agent concurrency is capped at two or three low-intensity, disjoint grunt-work
tasks. No agent swarm, duplicated range, bulk rendering, OCR, parallel build,
release-scale audit, or delegated final source/mathematical judgment is allowed.

## Superseding §7.8 build closure — R64

French source is now 282,508 bytes / 5,978 lines / SHA-256
`5B6E27ADF94611E5B135E2316C1EEAB4B1EE5A067146E7C22DC7DE67C6138005`.
R63 failed solely because the new French text used undefined `\Hom`; all
thirty §7.8 occurrences now use portable `\operatorname{Hom}` with no visible
or mathematical change. R64 passes three serialized builds; PDF 62 A4 pages /
413,424 bytes / SHA-256
`C13330C0BE44ED2750AD936DAE29E7B932818C9272FFAE96D6609C0A66E6DB36`.
Pass 2 equals pass 3; checked diagnostics are zero. Physical pp.61--62 were
rendered one at a time at 1,100 dpi and personally pass. Exact validation:
`controls/EGA1_SECTION78_BUILD_VALIDATION_R64.json`, SHA-256
`90C7FDBCA641A9712050C2D811FC7EA8528AB46F6B84E12EDF606B1B8AE156C8`.

The complete current English source manifest is R11: 127 files / 7,280,225
bytes / tree SHA-256
`D3FCAFB187DF2A812ABEB019BBE4AD50E7EB6D143CADF2C51EB357D256E95B13`;
manifest SHA-256
`BFF25F76B2DD8C58A895D7722F97EF711262757CCD42257AE59807A38F4C6F61`;
diff validation SHA-256
`F29FF0F856DFCDD9E0491398D0292769250F7C4CD312D555BE9E884A2CF2A12E`.
Global English build and release gates remain held.

The pre-Stacks machine-readable indexing scaffold is controlling under SHA-256
`803F9DD750F521B52C02DD02A99A20D904D1E47C4204DD73350B419F2CA5BE4D`.

## Current cursor — EGA I Chapter I, printed p.79 complete

The same controlling EGA-I authority continues into Chapter I. Physical PDF
p.78 / printed p.79 is complete in
`source/ega1/chapter1-frontmatter-fr.tex`, 2,045 bytes / SHA-256
`DE7D2CC5ED4918280120E35DB2BF3C90CB53F08D22D5E9241E63B1C06D387EE5`.
It contains the complete chapter title, ten-entry Sommaire, and orientation
paragraph, without source correction or modernization.

Authority/cursor control SHA-256:
`4F4D0F994859EB7FAC0268190A721D36CA37178826F01D59E7FE64F0F6440A04`.
One-page bounded PDF SHA-256:
`62072018461E2FB12F20D83980A7D1F033AE4F1A08664176C747F9336D194088`.
Validation SHA-256:
`E404FE4223BC22890DC5F005A70330490535EA433E35CBFE2B6C7C6A9C498C42`,
errors empty. English comparison required no edit; decision SHA-256
`5D9E76F96C0008486BD0DD83A9D963885B09431C6C64595158F5C704BD4DEE59`.

Exact next cursor is physical PDF p.79 / printed p.80, §1, §1.1,
paragraph 1.1.1. Agents active: zero. Agent cap: two or three disjoint,
low-intensity grunt-work agents only; heavy/image/OCR/build/audit/final-judgment
delegation remains forbidden.

## Superseding current cursor — EGA I printed p.80 complete

Diplomatic French now continues through all of printed p.80, including §1.1.1
and Proposition 1.1.2 with proof and footnote. Current sources:

- `source/ega1/chapter1-frontmatter-fr.tex`: 2,057 bytes / SHA-256
  `7B2D0F8F812EBA3121202F0AE6415FFC6C281B8428DA8F0F72D89DF1CEC01708`;
- `source/ega1/ega1-1-fr.tex`: 3,639 bytes / 106 lines / SHA-256
  `1CECBFC4D2CD0D595D46B7588721C334D06050DC97B40BAAE96FFD05E4218A23`.

The bounded two-page PDF is 46,494 bytes / SHA-256
`6F238B0D3F015C1F8791435494FEED7FC17CC0571D7401D5973C36FBC09EDF37`;
only output p.2 was rendered and personally passed. The small Fraktur
ambiguity was adjudicated from one tight 5,000-dpi crop: source prints
`\mathfrak j_x`. The lead's tentative `j→p` suspicion was wrong and rejected
before mutation.

English p.80 has exactly two justified edits—standard “fraction field of the
integral domain” and source-exact “relations” rather than “equations”—and one
rejected notation candidate. Current English file SHA-256:
`7F3A34C3E03F3497A4BD406E9E7A48ED6EDC72CCDA99768DD516EEF948202C64`.
Decision ledger SHA-256:
`363742C913D367889348FD4D554B6F53B22AC1ECE859BD9FDD8F83F4F9747A3E`.

Complete English R12 source closure is 127 files / 7,280,223 bytes / ordinal
tree SHA-256
`5410571C0C44F559B1474FFFACE408BE3137F71D418FD09F22B70B798A601191`;
manifest SHA-256
`491EC4E6FD5410C54986400B0CE1B975E502481537E846521CC24B7A20AA15ED`;
diff validation SHA-256
`3102F963D936C1A15641FF49F9CEF4D61810B8CEE1FFD259A170816A8703447D`.
French checkpoint validation R3 SHA-256:
`919E4AA8D21E17CDA058D20468F20E688696CAC1B3915AA2F59BD61D702E9A61`,
errors empty.

Exact next cursor: physical PDF p.80 / printed p.81, paragraph 1.1.3. Zero
agents are active. Work remains sequential and RAM-light; existing images are
reused first, and no new image is generated absent a concrete source need.

## Superseding current cursor — EGA I printed p.81 complete

French `source/ega1/ega1-1-fr.tex` now covers printed pp.80--81 through 1.1.9:
7,710 bytes / 206 lines / SHA-256
`1A3C8979F95B51594029DE4D2C3EDB3C18B3331DF38F0DEAB2F65D9ED6F101C6`.
The bounded 3-page PDF is 54,293 bytes / SHA-256
`5C9C3AE13B9A7B14E95D04848FCB0826B50E083865E98E0B98D5BD45B8849BEC`;
two affected output pages personally pass. R4 checkpoint validation SHA-256:
`D71C9D2A525AE7DD280BF28559573D727DE3E21FBA5C86D2A7DE0B2313B6FD92`,
errors empty.

English p.81 has three applied corrections and two explicitly retained
translation choices. Current source is 78,928 bytes / SHA-256
`8413A5B1710F1B932A4F69D8F7E8D501FCE909B0EE9BAC46809F4A3DEE20E221`.
Decision ledger SHA-256:
`51830FA1B2D263DDBDE91380EA04B6C6028D2A6711344A6E8038AAF8A05360D6`.
R13 manifest: 127 files / 7,280,251 bytes / tree SHA-256
`C73A0D59938FB18E3B9DEC6BB9E1C4BC8033360DA5C1B4F0BD948A9FCED76430` /
manifest SHA-256
`CC593E9C9D01D8053CF7757DAB745197E9481FF9308DA0C3D2623F25AD7406DF`.
Complete diff validation SHA-256:
`DA38B1A6554799334D70C5C9EEFB7CF4C9615BC8041CBDBEFAEE289E8FA13030`.

The first p.81 render selector was off by one; it produced p.82, was recognized
before source mutation, and is now correctly preserved for immediate reuse at
SHA-256
`212A6AC00972E745CF7F7C4C33D6302B050BCFAA2B0D920B738AA982E104C1DA`.
Exact next cursor: physical PDF p.81 / printed p.82, Proposition 1.1.10. Zero
agents active; no new p.82 context rendering is permitted because the exact
page already exists.

## Superseding current cursor — EGA I printed p.82 complete

French `source/ega1/ega1-1-fr.tex` now reaches the p.82 seam inside the proof
of Corollary 1.1.14: 11,938 bytes / 297 lines / SHA-256
`8CFF1ED1AF6AD16875A0EB87E1C9C4DA453799BC2FD29A1AE80BEFEEE90AB4F2`.
The final bounded PDF is 4 pages / 61,661 bytes / SHA-256
`CBD2C0707C64BA7D38EC3EBC00422A64955B8D4013DDD96D566D48A0EE0D1E3D`;
affected pp.3--4 personally pass. R5 validation SHA-256
`066BA00C2B441021C925BF8A580E73CA5E1852D41EA7CF5EBA2588275A762C53`,
errors empty.

English current source is 78,952 bytes / SHA-256
`B01302DA521F1FE09DBDE748CE5BF50199BD3C8CE6CA0BA21003B27161C65A14`.
P.82 decision ledger SHA-256:
`71711DFF7E0D5C21C8F32EF5A159585B22F61D574C20BBAAA91B4CB634719421`.
R14 manifest SHA-256:
`27038C5278D96F411B98E72780432BC2663B4923587FECED104ADC9AEE88CE59`;
tree SHA-256
`01613437EE956CADF50FE90C8C18CE8E73F2F731E3D1C94398C1410D12175A3D`;
diff validation SHA-256
`2E42656AE40BE12F5EEA3DB21A41602A6B1C4D1C5DE798DA83B990D1AB0BE509`.

Exact next cursor: physical PDF p.82 / printed p.83, continuation after `un
point générique`. Zero agents active; sequential/RAM-light rules unchanged.

## Superseding current cursor — EGA I printed p.83 complete

Diplomatic French now reaches the end of printed p.83: completion of the
Corollary 1.1.14 proof, Proposition 1.1.15, §1.2.1, Proposition 1.2.2,
Corollary 1.2.3, and the terminal functoriality remark. Current
`source/ega1/ega1-1-fr.tex` is 16,053 bytes / 403 lines / SHA-256
`5EF98CFE63E6F1A87283D59EA419FC069D475F896510409FB99EEE8129384CD7`.
The French preserves both the printed omission of the properness condition in
the proof of 1.1.15 and the historical composition-order formula.

Bounded French PDF: 4 pages / 68,147 bytes / SHA-256
`747BD13DB1201010DB9E89BCB40E7412C915B4ED78491287E84C2B0BFD9BFE8E`;
two passes, checked diagnostics zero, output p.4 layout PASS. Checkpoint R6:
6,790 bytes / SHA-256
`17D33B17D4D56F85879208360879B0AA997A831A59EF77CB778DA27A631BD872`,
errors empty.

English p.83 has one applied terminology repair and four explicitly retained
choices under decision ledger SHA-256
`D2CE7E4C7FAC883AB1F68902655472B0559C4B40ED7A9C7EC95471A8DF36E9A7`.
Current English source is 78,962 bytes / SHA-256
`1A203AD96C8C8AEF46C5884492B50CAD3E69590CA154ADBA58C4609AEB2A2C1E`.
R15 manifest: 127 files / 7,280,285 bytes / tree SHA-256
`B62B297758730E9DB6D10818DFD815A6BD9F7CE2BD418DECE13D6DA662D4CF0B` /
manifest SHA-256
`E9A16CF44BB22B03540A64BDA62F21013D7030DA0B170EC7B66A335A15588108`;
diff validation SHA-256
`05B18115426FBB140190E05B1AB7833852F3EAEBF3EDDC5A4A88909EC970DEEE`.

Exact next cursor: physical PDF p.83 / printed p.84, Corollary 1.2.4. Zero
agents active. Reuse-first, one-image-at-a-time, sequential/RAM-light rules
remain controlling.

## Superseding current cursor — EGA I printed p.84 complete

Diplomatic French now reaches Equation 1.3.3.1 at the end of printed p.84.
Current `source/ega1/ega1-1-fr.tex`: 20,132 bytes / 508 lines / SHA-256
`02C040DC7CB2DA53E4E6F2EE710BCAF37E99CA70AFC6960A1BAEF5FADC775E5B`.
The page preserves the printed 1.1.12 cross-reference in 1.2.5 and the three
unprimed ambient symbols X/A/A in the 1.2.7 proof. The English already carries
the source-backed 1.1.11 and X'/A'/A' corrections; both are now individually
proved and logged.

Bounded French PDF: 5 pages / 75,818 bytes / SHA-256
`527FDC5FDFDF86463F8F27384F183FD697926C086984F0EC9240015C90AE7F01`;
two passes, checked diagnostics zero, affected output pp.4--5 personally PASS.
Checkpoint R7: 6,320 bytes / SHA-256
`FBFA113F4CED15ABB0694A7329A6EFB0A8795E42A971D1F94BFBA42C6783572B`,
errors empty.

English source is unchanged at 78,962 bytes / SHA-256
`1A203AD96C8C8AEF46C5884492B50CAD3E69590CA154ADBA58C4609AEB2A2C1E`.
Three retained decisions are bound by ledger SHA-256
`67464F6931246807CB6478BBA49E9384E53ECC2399F0100241B14F49D605D20F`;
no-mutation validation SHA-256
`615D7EAABBF75650F9EAFF26D8DD64475CD1615450D31ECCBD6DCC668A6B0C9F`.
R15 remains the current complete English manifest without regeneration.

Exact next cursor: physical PDF p.84 / printed p.85, continuation of 1.3.3
after Equation 1.3.3.1. Zero agents active; resource rules unchanged.

## Superseding current cursor — EGA I printed p.85 complete

Diplomatic French now reaches the end of the proof of Proposition 1.3.5 on
printed p.85. Current `source/ega1/ega1-1-fr.tex`: 23,758 bytes / 589 lines /
SHA-256
`D48927FDFB91B3A898965E5259B2C72B8BFB317FC60D716266104A7BD465BAA0`.
The native 1.3.5 square preserves all four source label sides, including
`u_g` below the lower horizontal arrow.

Bounded French PDF: 6 pages / 86,036 bytes / SHA-256
`7BE67411894028C10EE670652D8EC183866F51F9EC98C9FC31D3B2121829BD39`;
two correct-directory passes, checked diagnostics zero, output pp.5--6
personally PASS. Checkpoint R8: 6,708 bytes / SHA-256
`5911A199F6EC01D4682B6913009B2E70731F9659E5B57F2EAD4EA592B13B8BF8`,
errors empty.

English p.85 has one applied source-fidelity diagram repair and two explicitly
retained choices under ledger SHA-256
`5A6AEAE4C1E6445364608FB234174915345D2B54E20E7C62A7BCA66860E8537D`.
Current English source is 78,962 bytes / SHA-256
`87F31A92CE21021768DB10B4C1F39A51992CF9949C61205E599CBD03E2E276AC`.
R16 manifest: 127 files / 7,280,285 bytes / tree SHA-256
`64C5266D3BB6553B6D3B1BBC42DF136042F6A5F83AFF0262CE22DF9500E35C30` /
manifest SHA-256
`39D7F529579466028B44E6E6BED9CDB547B4BDC2E4EDCD85783FCF1F8D9B7A34`;
full diff validation SHA-256
`DEA89BB808D3E6EF8221DE87C5DCA2007A868FD66847F992F1B109008926D28C`.

The explicit sequential/RAM-light/reuse-first rule is
`controls/SEQUENTIAL_RAM_LIGHT_REUSE_FIRST_WORK_RULE_20260802.md`, 2,055 bytes,
SHA-256
`99526B90F942BC00325F2A72E4C597CE886D433E4491D0FBC7950BCDBDA38B5E`.
Zero agents are active. Exact next cursor: physical PDF p.85 / printed p.86,
continuation after Proposition 1.3.5.

## Superseding current cursor — EGA I printed p.86 complete

Diplomatic French now reaches printed p.86: Proposition 1.3.6 and proof,
Theorem 1.3.7, and its proof through Equation 1.3.7.2 and the terminal words
`On en conclut`. Current `source/ega1/ega1-1-fr.tex` is 27,527 bytes / 664
lines / SHA-256
`9189ABAEC2E1599F3F03D34D8687312EA1F59A9B994A81CBCDDEB43546CDEB20`.

The controlling authority page is PDF one-based p.85 / printed p.86:
`EGAI_physical085_printed086_context_1400dpi_r2.png`, 10,870×14,409 /
7,630,440 bytes / SHA-256
`B7BEC3BAC68ACB643C558229D88E4B17F8AB3F2AF3A9DC0BF76B145516DE8B42`.
The earlier non-r2 file with the same nominal locator is actually printed
p.87; it is preserved unchanged as adverse/mislabeled history, not admitted
as p.86 evidence.

The corrected bounded build ran twice serially with zero checked diagnostics.
Its seven-page PDF is 93,397 bytes / SHA-256
`F2800A0E48B79217DE13500AD95E6D31FF0673DF66FA35B3F9EC86BA353E1BD9`.
Output pp.6--7 were personally checked at 600 dpi strictly for compiled
layout and both pass. The first build is adverse because two omitted TeX
backslashes visibly produced `emphinjectif` and `emphsurjectif`; the source
was repaired before checkpoint admission.

Three inherited English phrasings in the proof of 1.3.7 were wrong and have
been repaired with individual rationale: `ring homomorphism`, all `m_{ij}`
equal to the same integer `m`, and `we are reduced to the case`. The exact
three-row ledger is 3,316 bytes / SHA-256
`47ADE114A1A2161E71166C2BAD84C0E2EAEB06469B1703440524A06A46B456E7`.
Current English source is 78,953 bytes / SHA-256
`26747DCB22FCB736BBD1D025015C81E268F08CE42EB14D98518E4F21EA70DD99`.
R17 covers 127 files / 7,280,276 bytes / tree SHA-256
`CE854184377B48F388C46D5D4808E0A23A2E168F23909714C7E6F9C10B880DF8`;
manifest SHA-256
`63BA95B4C3C9B2E7C50C5878A523D7C5D032ABBB84C5D2B09AB967E904E78674`;
full diff validation SHA-256
`394F541895BE2619FE30D5562F28EA01FD28AF23B923C89B79BFFB9DC89D5D70`.

P.86 checkpoint: `controls/EGA1_CHAPTER1_P86_VALIDATION_R9.json`, 8,297
bytes / SHA-256
`3B5598B9D9CB608D84DB54E9F70E6D1572157E62E46B66F2694E2DAF0E7A20AA`,
PASS/errors empty. Two workflow errors are explicit in the p.86 ledger: the
page-base locator mistake and the two omitted formatting-command backslashes.
The resource cap remains at two or three low-intensity grunt-work agents;
zero agents are active. Exact next cursor: PDF one-based p.86 / printed p.87,
continuation of the proof of Theorem 1.3.7 after `On en conclut`.

## Superseding current cursor — EGA I printed p.87 complete

Diplomatic French now reaches the end of printed p.87: completion of Theorem
1.3.7, Corollary 1.3.8 and proof with native diagram, and Corollary 1.3.9 and
proof through the statement that $v_x$ is the identity. Current
`source/ega1/ega1-1-fr.tex` is 31,549 bytes / 755 lines / SHA-256
`389A015AA2E5D3C595939B9B8396320810F6A25C73128C4E6EC47F8A7F86E9D8`.

No new authority page was rendered. The existing 1,400-dpi image SHA-256
`3E861071076111EEBB9572225C6EEDBEBB3664DE47E2FEB09C605071793E9AC3`
was reused under its corrected locator: PDF one-based p.86 / printed p.87.
Two tight crops from those same bytes resolved actual small questions: the
absence of punctuation after both exact-sequence displays and the position of
`w` below the lower horizontal arrow in the 1.3.8 diagram.

The seven-page bounded PDF is 100,645 bytes / SHA-256
`140C8F9DC7F6A28409918FB10E0E8AD43F35C8BB57811535A6211D9BDA598FBC`.
Two serialized passes have zero checked diagnostics. Only output p.7 was
rendered at 600 dpi for layout and personally passes.

The inherited English put `w` above the lower arrow; it now places `w` below,
exactly as printed. This one-character repair is individually justified in
ledger SHA-256
`B4BC74E1FADA4448F35488502A81EFFA0C883572581F25A3BDEFDA0483E4AB32`.
Current English source is 78,953 bytes / SHA-256
`8C3145A4A41947759A191809C582163EF9FB590FBE9DC92211D719F205877D49`.
R18 covers 127 files / 7,280,276 bytes / tree SHA-256
`D2A7BC6831E8F15D10CCE2C52C0D6907937D32DFA2EC5C4BC3779B7936AAC465`;
manifest SHA-256
`2355C8043243D22BFA826AE8664D8A3563DA28C60CCB81BD35DD28ABF1D64BCE`;
full diff validation SHA-256
`0FDA5725A45AAF1C21EBA5FCF51684B5FA5E4E1ED2129F7C69AFACFF943192F5`.

P.87 checkpoint: `controls/EGA1_CHAPTER1_P87_VALIDATION_R10.json`, 8,101
bytes / SHA-256
`2E036C9C4E5240A10EB4299312E3FD98AEE87429FBF871730FC119E7EA5469BE`,
PASS/errors empty. One lead draft mistake is explicit: I initially added a
period after the second exact-sequence display, then removed it before compile
after a targeted authority crop. Zero agents are active; the two-or-three
low-intensity-agent cap remains binding. Next cursor: PDF one-based p.87 /
printed p.88, beginning `Enfin, si M est la somme directe...`.

## Superseding current cursor — EGA I printed p.88 complete

Diplomatic French now reaches the terminal isomorphism display on printed
p.88 in the proof of Corollary 1.3.12(i). Current
`source/ega1/ega1-1-fr.tex` is 35,477 bytes / 844 lines / SHA-256
`BF5E28152E1AEE70E34819CF64A9A2CC95A2B88DAC536D8B58421D5859C91A03`.
One ordinary-context authority page was generated after a reuse search found
none: 10,462×14,273 / 7,919,506 bytes / SHA-256
`A0269AB9268BF48B6C3B10923F9C31737F56EA9376C6A64567E988C07DA6E67F`.
No detail crop was needed.

The bounded eight-page PDF is 106,742 bytes / SHA-256
`10A333E18BB2466D7CCEE6C815EDC2423E4FF682DC647F0820DA5DD043571946`;
two serial passes have zero checked diagnostics. Output pp.7--8 personally
pass at 600 dpi for layout only.

English R18 remains byte-identical. Three page-specific normalizations were
reviewed and retained with individual rationale: the composite-module
`\supertilde` macro, the `\shHom` macro, and explicit theorem/proposition kind
words on the same clickable references. Ledger: three rows / 3,276 bytes /
SHA-256
`39E247CAA4BA6F67384FB4EB535D49D2B0ADB6DAC73A3975642F310D8678DE76`;
no-mutation validation SHA-256
`C6FF77518A41AD662643CD1F39EF4880FB311B9C88B9FD310A7A93EC76F9960D`.

P.88 checkpoint: `controls/EGA1_CHAPTER1_P88_VALIDATION_R11.json`, 6,384
bytes / SHA-256
`3C9CC554D618C44E72EE0FEEBBAB828DEB0245F24B0C2BF83A87CBE69940C132`,
PASS/errors empty. Zero agents are active; the cap remains two or three
low-intensity grunt workers. Next cursor: PDF one-based p.88 / printed p.89,
continuing Corollary 1.3.12(i) after the terminal display.

## Superseding current cursor — EGA I printed p.89 complete

Diplomatic French now reaches the final finite-type statement on printed p.89
in 1.3.13. Current `source/ega1/ega1-1-fr.tex` is 39,112 bytes / 930 lines /
SHA-256
`F670F2FD67371DF61A7E41A994AC94376B835158DC6EF50B7A6765D8C346F688`.
Authority image: 10,423×14,137 / 2,878,227 bytes / SHA-256
`9F357BAF256A9D27FE9E0B1647AEB08DF134D84F990F1195D57FE21669A96179`;
one page only, no detail crop.

English R19 corrects three inherited source-fidelity deviations: source
condition numbers `1^\circ/2^\circ` replace invented `(a)/(b)`, and the lower
`\varphi` and `\psi` labels are below their arrows. English SHA-256:
`755474860ACB423698A25393EB56CE06396F321131B7EACBBF2624478089BDC5`.
Decision ledger SHA-256:
`38712B6F457B308FD650DDD19537321207EF7D256BDCD2622535EF1BC90D99C9`.
R19 manifest/tree SHA-256 values are
`8A2618EE6EB0A895A6DE54B83A30F165D901504410CCB89177047325DAA59F80`
and `FD8D86B665DACA629F4FE1ED320D15EF2BFA25A751B8527905C85457C78998C7`.

The bounded nine-page PDF is 113,444 bytes / SHA-256
`36CC5F5FAAFF6AD88B55DEEF9C74293A74402440AAF9793FE2B006C53440D4EC`;
two passes have zero checked diagnostics and output pp.8--9 personally pass.
Four lead/workflow mistakes are recorded under ledger SHA-256
`E31E92A826C8570A1946B064C3D046A4FB784C7E9439FB5C74B234C66DF7C030`.
Checkpoint R12 is 7,365 bytes / SHA-256
`C674208138DB0C5528C4B842D006FDF141C6C553E04F220859F7FAC68F9D180A`,
PASS/errors empty. Zero agents are active. Next cursor: PDF one-based p.89 /
printed p.90, continuing 1.3.13 with `Si M, N sont des B-modules...`.

## Superseding current cursor — EGA I printed p.90 complete

Diplomatic French now reaches the proof that c) implies b) in Theorem 1.4.1.
Current source: 43,364 bytes / 1,010 lines / SHA-256
`209E5EF26239495DC1B1540FF7EB06E9E57122770D66EC37401FCA413DFE56E9`.
Authority page SHA-256 is
`5B3D64B713A7E01460F1FC4637E85FC34284C656153033BF856F0A33DAA67AFC`;
one ambiguity crop SHA-256 is
`C1D0FC9811194B519FBDFF385CD637AAAD3FE2FC33545A6978C5E671CED4C33D`.

English R19 is unchanged. Five retained choices, including the explicit
correction of the printed misplaced-tilde phrase, are logged under SHA-256
`A5C0174B7820E383F6FA9B55FFC3D0E2C066C0B4C20CC5FBCE2D29E4DABE66C6`;
no-mutation validation SHA-256 is
`95E3671D4EB366F23D6C403B4E9D89D145D4EDBC9904CD3A218C111E142AE1F9`.

The bounded nine-page PDF is 119,551 bytes / SHA-256
`44FDD1A2620174F0A8A39FACB34F37355C09F5EB47151CD529DBB19C6015CA50`;
two final passes have zero checked diagnostics and output p.9 passes layout.
Checkpoint R13 SHA-256:
`0DCD4476C7F3170509395EAD0A9B983810A19725AC185A3D188A248FE316DF39`.
Zero agents are active. Next cursor: PDF one-based p.90 / printed p.91,
continuing the proof of Theorem 1.4.1.

## Superseding current cursor — EGA I printed p.91 complete

Diplomatic French now reaches the printed p.91 terminal fragment `g^m t se`
in the proof of Theorem 1.4.1. Current source: 47,381 bytes / 1,080 lines /
SHA-256
`9F7FE068AB53F83ADF9CF58C3692D0CACCF2A3571A26C07F3AB9C164656E2ABE`.
The single 1,400-dpi authority page is 10,423×13,962 / 3,431,666 bytes /
SHA-256
`B9AA4889898ED3D09E542ED7C34D59BFBA7F4611B4F419FC5AA4E7BD02C4D83F`;
no detail crop or diagram was needed.

English R20 repairs two inherited grammatical defects: the malformed lemma
transition `To finish the proof, that...` and `It is evident for (d1)`.
Current English source is 78,945 bytes / SHA-256
`776A8D8FB7B5ACA95CC45F939C8BF11E5CF45B00709BC281F9FFB007C58A86A9`.
Six decision rows, including four retained normalizations, have SHA-256
`4ADAD1B6997F3B699E36BF7F95E33D6F0FA68D7483FB5D1406C73EB190612510`.
Two inverse substitutions reproduce R19 exactly. R20 manifest/tree SHA-256
values are
`864B73E7553E086F64D7AD32B4DD8494823505E3956A28DBED39EFBB8EA990D5`
and `1C39A53AA1AFE22E39606C93EADB7FBE6C0D0705AE43C35C9D6DBD345DDFE5AD`.

The admitted bounded build is r2: 10 pages / 124,336 bytes / SHA-256
`5B8761E5AEDA30ECBE6E7475A9489A6AEBCD5F895BF0372971B66286E12FCA03`;
two serial passes have zero checked diagnostics. Output pp.9--10 were rendered
one at a time at 600 dpi for layout only and personally pass. The wrong-CWD
r1 build remains adverse history. Three workflow errors, including the
repeated culture-sort mistake, are explicit under SHA-256
`546982E90BF81244EE22F6986CDA458065D2C37621666DBFDB1274DA1744E355`.

Checkpoint R14 is 7,885 bytes / SHA-256
`E48DC2814D020CA3C9EA06719BE864354A2276D533C6505DC5BDD978A11266C1`,
PASS/errors empty. Zero agents are active; the maximum remains two or three
bounded low-intensity grunt workers. Next cursor: PDF one-based p.91 /
printed p.92, continuing after `g^m t se`.

## Superseding current cursor — EGA I printed p.92 complete

Diplomatic French now reaches the complete statement of Theorem 1.5.1.
Current source: 51,644 bytes / 1,164 lines / SHA-256
`B5E58A9430A49E9A19C0B792A1B4F41549A5092AFB8000BA8CE023C1AC4D264B`.
Exactly one 1,100-dpi authority page was generated after reuse search:
8,266×11,184 / 6,642,775 bytes / SHA-256
`57FCD19DD19BCF8D20CC7AC5F64F7981D794DF3854DB4EAEE27B3538574DCD85`;
no crop or diagram was needed.

English R21 repairs two inherited prose/scope defects in the proof of 1.4.3.
Current English source SHA-256 is
`E79237CB465C8F0EF7C3FE573F568C4FCD122DC5D618463C46B914DE218459F9`.
Nine decision rows / SHA-256
`A12D4F80F39AD47269CA79400EBE3B8CCF5DE8C11FE5D21BE85B665A45722A89`
record two applied repairs and seven retained normalizations. R21 manifest/tree
SHA-256 values are
`DA77D11422EEB0CD94709729824171B1D9B33A1C7B71E5BBE68C9CAF9679717A`
and `870E97EB71F44AA795F47332B655738011DB772C226899E1FFDE66A3741A4B82`.

The admitted r2 bounded PDF is 10 pages / 129,151 bytes / SHA-256
`393E1FBD1AC8C7A93A7D23FEB7E0F283666A0041D2623C58C03C686EB0407E74`,
with zero checked diagnostics. Page 9 reused prior layout evidence after exact
content-stream identity; only page 10 was newly rendered and personally passes.
Four caught workflow/draft errors are logged under SHA-256
`ED85AD247BE5BFDC21A0BDF46B9465BE2A45CB82ED13DA4619EE5AD3891151CB`.
Checkpoint R15 is 8,540 bytes / SHA-256
`051E8D04A57A6094FA52E94B1061E774331FB691A3FD62B95125C29A1E0EFD7C`,
PASS/errors empty. Zero agents are active. Next cursor: PDF one-based p.92 /
printed p.93, proof of Theorem 1.5.1.

## Superseding current cursor — EGA I printed p.93 complete

Diplomatic French now reaches the terminal displayed ring homomorphism on
printed p.93 in paragraph 1.6.1. Current source: 55,165 bytes / 1,253 lines /
SHA-256
`94FAA233686C9C44B8B492C7F772DAB3CC70D2F8BC0B5DCB047ECB758B2BC4ED`.
Exactly one 1,100-dpi authority page was generated after reuse search:
8,189×10,970 / 5,464,710 bytes / SHA-256
`274B90A70A72E0812131425C82664C9F47D82F66C1E1A821B574AA67C183C8F0`;
no detail crop or diagram was needed.

English R22 repairs three inherited prose/register errors and changes no
formula, object, or reference target. Current English source is 78,920 bytes /
SHA-256
`08B58F1484E0195D637512C27528BF77F665DCE03D1B3C4F29A7FC685A956E5E`.
The nine-row decision ledger records three lead errors and six retained
normalizations under SHA-256
`211B3C3A460DB008F6E01ECE0D6444448053525A42A816B86069515D7F63D54E`.
R22 manifest/tree SHA-256 values are
`4B2C325B73D8DCF3027A5A6BE0FEB651AD6477200E71E33916E91399CD9262F8`
and `4B01E8D9D30053F942E2570915BB92365BC754DA5A95ABA6C0AB8BA2DF9329B3`.

The admitted bounded PDF is 11 pages / 134,806 bytes / SHA-256
`6060F18A680F8F34A33E298FB2573A8A842AA0171022114C9A5E23944487B84D`,
with zero checked diagnostics. Pages 1--9 are content-stream-identical to the
prior build; only changed pages 10--11 were rendered sequentially for layout
and personally pass. Checkpoint R16 is 8,061 bytes / SHA-256
`6637A091AE9F1BEFC60E1E0365E3422DF2DBFBD2ED901DC079322861F23A90F0`,
PASS/errors empty. Zero agents are active; the cap remains two or three
low-intensity grunt workers. Next cursor: PDF one-based p.93 / printed p.94,
continuing paragraph 1.6.1 with `En outre, ces homomorphismes satisfont...`.

## Superseding current cursor — EGA I printed p.94 complete

Diplomatic French now reaches the exact p.94 seam after the incomplete phrase
`l'isomorphisme`. Current source: 58,853 bytes / 1,336 lines / SHA-256
`E0F4EA3D4AC371A160550ADE7BA8B04A3EC42D6E633DB53CBA834F3CBCDE35C6`.
The page closes paragraph 1.6.1, includes one source-faithful native
compatibility square, gives Example 1.6.2 and Proposition 1.6.3 with proof,
and begins the following unnumbered consequence. No raster diagram is active.

After reuse search, exactly one 1,100-dpi authority page was generated:
8,266×11,184 / 2,430,848 bytes / SHA-256
`0C60C72AEB9B5A918792EDDC8FCEF6C3D5E402E9602E0F07115965069B7E840C`.
The lead inspected it at original detail; no higher-detail crop was needed.

English R23 repairs two inherited prose/register errors and changes no
formula, object, or reference target. Current English source is 78,882 bytes /
SHA-256
`3839AC1B392AA3B7629B06909D1DAC19AF652963B01D556D1889B1C9ECAB8414`.
The eight-row decision ledger records two lead errors and six retained choices
under SHA-256
`DCCDA3F1B7B9DB60D19903ED0EE20E24B4E88A369FE2D63EA206E5B78EAF32C7`.
R23 manifest/tree SHA-256 values are
`3D744079A8F05F4526BD2446B6636D487D2D258B93722F1861D810BF6408D06A`
and `BB9926BFC40EB87CF106CDDACDDB834F99FF4B78CE99E0C3C3F8F32D638B5419`.

The admitted bounded PDF is 12 pages / 140,464 bytes / SHA-256
`C70DC227F37A613D4667A67135F71DE49A8E3F72D4975988A8DAB1EB8A9793B5`,
with zero checked diagnostics. Pages 1--10 are content-stream-identical to the
prior build; only pages 11--12 were rendered sequentially at 600 dpi for
compiled-output layout and personally pass. Checkpoint R17 is 9,196 bytes /
SHA-256
`87CAAA52DFC8971F4B0374D8040A7F5E67BE4A01974904A954F84F8D00610EB1`,
PASS/errors empty. Four caught workflow/documentation mistakes are preserved
in a four-row ledger, 3,194 bytes / SHA-256
`AAD7CED994CE3BA26B35A526C048596F974A659C0215F2F39E58AB195CC8A7FA`;
none affected source mathematics. Zero agents are active. Next cursor: PDF
one-based p.94 / printed p.95, continuing the canonical functorial
isomorphism introduced at the p.94 seam.

## Superseding current cursor — EGA I printed p.95 complete

Diplomatic French now reaches the terminal comma in the opening sentence of
paragraph 1.6.7 on printed p.95. Current source: 63,197 bytes / 1,432 lines /
SHA-256
`B8C18DA8E3661EADD85EAE0FBC8A99779A1CD59285855FF2FCF5C54981265238`.
The page contains Corollaries 1.6.4 and 1.6.6, Proposition 1.6.5 with equation
1.6.5.1, their proof prose, and the opening of 1.6.7. No diagram or raster is
active.

Exactly one 1,100-dpi authority page was generated after reuse search:
8,296×11,107 / 5,343,755 bytes / SHA-256
`A399A19C67962146373AFDAC1A2083E95070510651412DFD79CCE461310E95FC`.
The lead personally inspected the complete page at original detail; no crop
was needed.

English R24 records seven source-backed repairs and one visible-equivalent
prime/subscript source-order normalization. One repair is mathematical: the
tensor input to (h_x) is now the source-exact stalk (s'_{x'}), not the
inherited (s'_x)-style expression. Current English source is 78,891 bytes /
SHA-256
`3C1A38B22A9A07315A8CFA2E8F3AC1B65232E0CFCE3F9F8E2E09A30464018617`.
The fourteen-row decision ledger has SHA-256
`905745E09BAC102CE4B799081490DB9647AE28D5BE0AE3707D6BECFB4C85BD8D`.
R24 manifest/tree SHA-256 values are
`EBA2F1067D485CCD4861EAFEC7F1239C55CA5858E1734714FA91667805E37E3E`
and `099CD37D1BD2E8380DF875A90C61895F7B7BFF743573A4CF5452B22D3AEE5A56`.

The admitted bounded PDF is 12 pages / 145,648 bytes / SHA-256
`D6F9892A0FBFBFFD6EFC135A29191E0EFA4C69494A2670C5A4A961EFCEC3536C`,
with zero checked diagnostics. Pages 1--11 are content-stream-identical to the
prior build; only page 12 was rendered at 600 dpi for compiled-output layout
and personally passes. Checkpoint R18 is 9,167 bytes / SHA-256
`7AC4DC5BDC566DF19569AF0EFCD14E1429C6A3A61A042B32895AD1A19AF3CC41`,
PASS/errors empty. Two workflow rows preserve the r1 open-environment wrapper
failure and nonfatal one-page renderer warnings under SHA-256
`0E04DD82A9C4BB0DA0F4F1B60A0E0161102FC0627B37FEDE7CC0A9600702EBC0`.
Zero agents are active. Next cursor: PDF one-based p.95 / printed p.96,
continuing paragraph 1.6.7 after the terminal comma.

## 2026-08-02 — EGA I printed p.96 closed

Diplomatic French now runs continuously through the complete statement of
Theorem 1.7.3. Current `source/ega1/ega1-1-fr.tex` is 68,010 bytes / 1,548
lines / SHA-256
`9EAF6027F10D1EC54DC1779FC4C83785950447EE4E9DC8C5A1B3F2454EB672F2`.
The existing 1100-dpi authority page was reused and personally inspected at
original detail; no authority page, detail crop, OCR, or agent work was added.
The eight-row French decision ledger is 3,583 bytes / SHA-256
`9B3F9948724B518DB513537ED3932E51B23475A85946DD01B4A24BC23280AD4D`.
It records the p.95 seam, both Hom formulas, the ideal/module reading, all
functor-composition orders, the exact retained functor wording, the §1.7
boundary, and the fact that no source correction was made.

English p.96 recheck applied two nonmathematical fidelity cleanups: the source's
single combined volume-0 citation parenthesis is restored while both locators
are clickable, and `when no confusion results` replaces the inherited
probabilistic embellishment. No mathematical correction, lead error, or
reversal was found. Current English source is 78,908 bytes / SHA-256
`758885F9505A72DF1A5A2EF8B116D998A41D0505571AD8E7028C438EE5795C6E`.
R25 manifest/tree SHA-256 values are
`516696896ADBB097947CC00005B37C890C505AE9DB1D5B17EC688E0F8E7A475B`
and `8D3BF2A908E654E4B94AC1FFE2BEF606BF4EE92FDCEB400AAC02B737E1D51E4E`.

The admitted bounded French build is 13 pages / 152,080 bytes / SHA-256
`013E31E9AC94D2153113C9EDC619DB8C8DBF2C33A35597F7F78FADAECB8BC159`,
with zero checked diagnostics. Exactly one compiled-output page was rendered
at 600 dpi and personally passes layout. The literal-`$out` build-routing
mistake and two output-wrapper renderer failures are preserved in the
two-row workflow ledger, 1,522 bytes / SHA-256
`78F2BD3A94168E18E121212CC7DD2DF2C860D4E8E07D8E7C45FC216CD8A4FD61`;
none changed source or mathematics. Checkpoint R19 is 7,085 bytes / SHA-256
`39B3AEC1B4BEF0DA99558F20D0CEF0AA030115F84C1AD024152F8A86122E4E72`,
PASS/errors empty. Zero agents are active. Next cursor: PDF one-based p.96 /
printed p.97, beginning the proof of Theorem 1.7.3.

## 2026-08-02 — EGA I printed p.97 closed

Diplomatic French now runs continuously through Corollary 1.7.5 and its proof,
then begins §2 and reaches the complete Definition 2.1.2. The page crosses the
natural source-file boundary: `source/ega1/ega1-1-fr.tex` is 71,381 bytes /
1,624 lines / SHA-256
`D201398091BCC065BE7B5EFC610183E1E2071E01BC8E35C0CE1441DF3E579393`,
and new `source/ega1/ega1-2-fr.tex` is 607 bytes / 19 lines / SHA-256
`48DF1C2DA45FFC15BED36D50E53AE21B9819B64758A3ACE3D0A7B306FC4F282B`.
The proof square is native TeX with stable target `I.1.7.3.diagram-fr`; active
raster diagrams remain zero. No French source correction was made.

Exactly one authority page was created only after reuse search: 8,296×11,107,
5,490,961 bytes, SHA-256
`F3033D317BF871AF491AE5E472DE64ECDF86D0ECDA79F9007800B7C977FB9AB0`.
The lead inspected the entire page at original detail, including every square
node, arrow, label, residue-field symbol, formula, and the §2 seam; no detail
crop was needed. The nine-row French decision ledger is 4,154 bytes / SHA-256
`C26F809FDAB1E8AB820C76F874061C5777E6D0648F0FAA26EF9396B04ED6EB9C`.

English p.97 recheck found no mathematical mismatch, unsupported source
correction, lead error, or reversal. Two prose-fidelity repairs were applied:
singular `The hypothesis ... means` and the source-faithful `equivalently` in
the definition of the affine-scheme morphism. Current English source is
78,906 bytes / SHA-256
`EB62DDA7A40E93BFF26BEF9513693192A7C46540E08D244C18218F9BAAEF4FFA`.
The ten-row decision ledger is 3,871 bytes / SHA-256
`0CA4E32D47D13CBABB1993F7B3F8498A1B9F6152F6EEF28EC7A280811740E06A`.
R26 covers 127 inputs / 7,280,229 bytes, manifest SHA-256
`A28F89369E461D3B434C5F66F51299B462AB9CE4F457ACA952B94551CDBE4147`,
ordinal tree SHA-256
`F6706D38DCA72AE5A01C4999F52056424809462990F8136C8042D6DE4108210E`.

The serialized two-pass bounded build is 14 pages / 157,916 bytes / SHA-256
`8564A2C082E637A33B5FEE69D8C18FD54585EDF32832AE51948182EAD2AB4DE6`,
with zero checked diagnostics. Exactly one compiled-output page was rendered
at 600 dpi for layout only and personally passes. The two workflow rows record
the failed dependency wrapper and nonfatal renderer font warnings; neither
affected source or mathematics. Checkpoint R20 is 7,273 bytes / SHA-256
`BF4FD925BA25D4F5572F6B5186BF608A834A0B036BA95717DE74BDD63A275B78`,
PASS/errors empty. Zero agents are active; the standing cap is at most three
low-intensity grunt workers. Next cursor: PDF one-based p.97 / printed p.98,
beginning Proposition 2.1.3.

## 2026-08-02 — EGA I printed p.98 closed

Diplomatic French now reaches the complete Definition 2.2.1. Current
`source/ega1/ega1-2-fr.tex` is 4,664 bytes / 114 lines / SHA-256
`9C52B942A2B935B4201B021491D30EAD82748622FD4696D8909A6D5BEC16CC2B`.
It contains Propositions 2.1.3--2.1.5, paragraphs 2.1.6 and 2.1.8,
Proposition 2.1.7, and the §2.2 opening. No diagram or raster occurs.

One NUMDAM authority page was created after reuse search: 8,144×11,230 /
5,258,418 bytes / SHA-256
`0B21F79E1BD1E8CDBDB62B647C7B5F01A787AA0D8CD5A7A362AC069E68CD98D4`.
The lead inspected it at original detail; no crop or OCR was needed. The source
prints `point générique de X` in the proof of 2.1.5 although the proposition
and preceding sentence concern $Y$. The French preserves $X$ diplomatically;
the English correction to $Y$ remains immediately disclosed and was
reverified. No French source byte was corrected.

The first bounded build exposed one lead structural error: four explanatory
paragraphs had been put in `proof` environments, which would add headings the
source does not print. The r1 build is preserved adverse; the wrappers were
removed without changing words or mathematics. The no-overwrite r2 build is
14 pages / 162,529 bytes / SHA-256
`6908050489FFA9A1200F421B3DF0A4165489A0DD05D9B933C6891383EFEE201D`,
zero checked diagnostics. Pages 1--13 are content-stream-identical to the p.97
build; compiled page 14 alone was rendered at 600 dpi for layout and personally
passes. French decisions: nine rows / SHA-256
`2CFE6171523633BD8730600BD3B513C4D81D7AD1F524B126F47A8934C66086F2`.

English R27 applies two prose-only repairs in Proposition 2.1.3: direct
`there exists f` and standard `contained in`. Current `ega1-2.tex` is 25,214
bytes / SHA-256
`9239F37777A793E4A03AFEDCD0479AD55C7D90EC6A92886B20E20F80A031BA18`.
New mathematical repairs zero; retained disclosed source-typo repairs one;
lead errors zero; reversals zero. R27 manifest/tree SHA-256 values are
`1EBEC66D050557D5F20B1EF42B1CF8F3A7717D59ACD2CFDB3384604E0DDD5419`
and `07D146DDD043D20E0D30F09612E645F86A14000E974FE9C44703B6B0D35E239A`.
Checkpoint R21 is 8,005 bytes / SHA-256
`F8E4DEBF91B6A76F697893324F32EA5E1A1678623B3845E34061F10D88C78D34`,
PASS/errors empty. Zero agents are active. Next cursor: PDF one-based p.98 /
printed p.99, paragraph 2.2.2.

## 2026-08-02 — EGA I printed p.99 closed / checkpoint R22

The diplomatic French transcription is now continuous through printed p.99.
Current `source/ega1/ega1-2-fr.tex` is 9,213 bytes / 206 lines / SHA-256
`80084D747F88429A8770AC0918B7B07ED8631D1FACCC6619661BCD95EA157A33`.
This page contains the residue-field consequence after Definition 2.2.1,
2.2.2, Example 2.2.3, Proposition 2.2.4 and its proof (including displayed
formula 2.2.4.1), and the opening of Proposition 2.2.5. The file stops at the
exact page seam after `Il existe alors une`; the proposition intentionally
remains open for printed p.100. Formula 2.2.4.1 has no terminal period in the
authority and none was invented. No source typo, source correction, diagram,
or raster occurs on this page.

The already-existing 1,100-dpi authority image was reused and inspected at
original detail; no new image, crop, OCR, agent, or parallel job was used.
Image SHA-256 is
`446A4BFC0958E1210B5BD21E0F3753A15944D73AF676C1E621AD1522ED784BE1`.
French decision ledger: nine rows / 3,925 bytes / SHA-256
`99A0E92FA8B8B4A2CF917CFBB0DD287D1785E360DD827CD33D52CFF99E119DD7`.

English R28 applies four prose/logical-register repairs only: `therefore gives
a monomorphism`, `as follows from the formula`, `contained in`, and `hence,
by the relations`. It changes no formula, mathematical assertion, source
reading, or diagram. Current `source/ega1/ega1-2.tex` is 25,214 bytes / SHA-256
`C2C52F7F7543ABEC2A082C294123434E07FFA64E57181A879C033850C8E7DCBC`;
four inverse substitutions reproduce R27 byte-for-byte. New mathematical
repairs zero; source corrections zero; English lead errors zero; reversals
zero. English decision ledger SHA-256 is
`2198C5F835E8539CA737193AD32E41F58E4F47E1CF66AD20A9EAC1842DDD8251`.

The bounded p.79--99 reader is 15 pages / 168,076 bytes / SHA-256
`2DAE67334A752773F5DA94D0F838B67BF764E8B3BF9A9D6DAD9196D3C7CEB34D`.
Two passes have zero hard/undefined/missing/duplicate diagnostics. One
6.31696-point overfull box is confined to the temporary page-seam wrapper;
direct inspection of compiled pages 14 and 15 at 600 dpi shows no clipping,
overlap, or illegibility, so the diplomatic source was not altered to hide a
wrapper-only warning. R28 manifest/tree SHA-256 values are
`6E3AE6380AA300004627DEF42A1ECFEFEC6326C8887C525A9930A50623CF5B3C`
and `4C32D118D81AC1B2E89A5AEC33FD0C355B98DD2D509235A64C7A01D274280D01`.
Checkpoint R22 is 7,709 bytes / SHA-256
`7BA41019FEE8362A644B856E7389E89087AE86911C7528F04D86104A6C8F5532`,
PASS/errors empty. Next cursor: PDF one-based p.99 / printed p.100,
continuing Proposition 2.2.5 after `Il existe alors une`.

## 2026-08-02 — EGA I printed p.100 closed / checkpoint R23

The diplomatic French transcription is continuous through Convention de
notations 2.2.10. Current `source/ega1/ega1-2-fr.tex` is 13,093 bytes / 296
lines / SHA-256
`847E41008F84D6C74DAD4BEE3CA0C6DB2D9155BFE1947B7529D14EFF894C09E4`.
Printed p.100 completes Proposition 2.2.5, defines open/closed/dominant/
surjective morphisms, proves the composition and open-cover locality results,
defines birational morphisms, and states the notation convention. Five new
stable targets were added. No source typo, source correction, ambiguity,
diagram, or raster occurs.

Reuse search found no p.100 image, so exactly one 1,100-dpi authority page was
created and inspected at original detail: 8,220×11,077 / 6,427,556 bytes /
SHA-256
`33F148CC42DCFD369BBE82C64EFA714084E8950CE8A1C31036CF583A493798BB`.
No crop or OCR was needed. French decision ledger: ten rows / 4,528 bytes /
SHA-256
`282926E7B47BFC07FB6A87F39B4651AB6DE49C3A37CCF50E84F523D02DB92215`.

English R29 restores the missing finite verb in 2.2.7(ii) (`g\circ f is
closed`) and replaces inherited `Claims` with source-register `Assertions`.
Both are prose/grammar repairs with zero mathematical effect. Current English
source is 25,221 bytes / SHA-256
`33AF57E584C85A17B7E0A18D22E0C504793BD0C71A30DC864EE0775DC349F5F2`;
two inverse substitutions reproduce R28. New mathematical/source repairs,
lead errors, and reversals are zero. R29 manifest/tree SHA-256 values are
`3FC26BF7E9F628BF33AF9834C304C89071A21644DE923E6BCAC42FED6CE6AEE1`
and `7B25527C49B34E8EBB847D5887FAE707DBAB1DD9649A4508D0912407BAEAA96A`.

The bounded p.79--100 reader is 16 pages / 173,098 bytes / SHA-256
`2F2D5983DA0C539D607641859E6F6575BC6986B34261E8C5909427F7509F9F5B`.
Two passes have zero hard/undefined/missing/duplicate diagnostics. The one
small pre-existing temporary-wrapper overfull warning remains visually
benign. Only affected pages 14--16 were rendered sequentially at 600 dpi and
personally pass; pages 1--13 have identical extracted text to the predecessor.
Checkpoint R23 is 6,479 bytes / SHA-256
`BB8583C50950D3831D2CC2E5E35380E52AD56A4AC60710A15F883A10C2C1D9E1`,
PASS/errors empty. Next cursor: PDF one-based p.100 / printed p.101, opening
§2.3, `Recollement des préschémas`.

## 2026-08-02 — EGA I printed p.101 closed

French EGA I is now diplomatic through the canonical morphism
`Spec(O_y) -> Y` in 2.4.1. Current `source/ega1/ega1-2-fr.tex` is 16,814
bytes / 373 lines / SHA-256
`73968E89E47D9DB989CAAD204BB32699BDE5EBE500387BB4C166FE44CB167FF4`.
Printed p.101 adds 2.3, Example 2.3.2, 2.4, and 2.4.1, including the native
three-arrow `B'`, `B`, `O_y` triangle. Six stable targets were added. No
source correction, source typo, ambiguous reading, raster, or mathematical
normalization was admitted.

Reuse search found no p.101 authority image, so exactly one 1,100-dpi page was
created: 8,220×11,077 / 6,407,754 bytes / SHA-256
`3DE6FB3D2EB090764E6B7404BFBE7BF024DBB82D1ED93972119B84A654333341`.
Original-detail lead inspection resolved the small triangle completely, so no
crop, higher-resolution render, or OCR was justified. French decision ledger:
nine rows / 4,235 bytes / SHA-256
`F7329A53C494396C09C8C6DED894FB40E40254977C66E25172CF50B19A3C297A`.

English R30 makes five source-fidelity repairs on the same page: restores the
causal `since`; repairs the two-ring/two-scheme parallel grammar; restores
`We shall encounter again later`; defines a local scheme by saying its ring is
local; and restores the source's singular universal quantifiers. None changes
the mathematics. Current English source is 25,205 bytes / SHA-256
`39D017669DCEFD7B859A5851D112CD2605720CB68F2C7A695C8BEE3FAA6D3535`;
five inverse substitutions reproduce R29 exactly. New mathematical/source
repairs, lead errors, and reversals are zero. R30 manifest/tree SHA-256 values
are `0643CFD16D04791CC6865EA67D4C8FC19E0C77D38A073DB7BB0C4EE694AFAC4D`
and `E6C94B0401070FA4EA758DA90A03829EE7ED40D97A611A3EA86F751D13E64245`.

The no-overwrite p.79--101 wrapper also corrects a temporary-wrapper-only
heading defect: `Exemple (number)` now follows the NUMDAM order. The 16-page
bounded reader is 178,349 bytes / SHA-256
`238F7406BB562042BAEA00C1520169FDAB3F42FD8F64AFA82DA93F4DAA63A3C4`.
Two passes have zero hard/undefined/missing/duplicate diagnostics; the one
small pre-existing wrapper-only overfull remains visually benign. Extracted
text changes only on pages 11 and 15 for the heading correction and page 16
for new content. Those three already-existing 600-dpi layout renders were
personally reviewed and pass, including the diagram.

Checkpoint R24 is 7,918 bytes / SHA-256
`2B8A9A673EC9DE56E26E13566CF11568F8DD5F3474A602B95F6F7EDE6410781B`,
PASS/errors empty. Six source-neutral workflow events are closed in
`WORKFLOW_ERROR_APPEND_P101_20260802.jsonl`, 3,541 bytes / SHA-256
`AA6E37F48D368D8F89CCF598369328AFA3F8EEB2808583B86B1647F4E113E137`.
Next cursor: PDF one-based p.101 / printed p.102, Proposition 2.4.2.

## 2026-08-02 — EGA I printed p.102 closed

French EGA I is now diplomatic through the colon ending the p.102 portion of
2.4.5. Current `source/ega1/ega1-2-fr.tex` is 21,434 bytes / 461 lines /
SHA-256
`81031D76811A088C7A4B777D60F15FB1EBBCA837B5CB4CD24ABBD688B65B4C1F`.
The page adds Propositions 2.4.2 and 2.4.4, Corollary 2.4.3, and 2.4.5 with
four stable targets. No source typo, source correction, ambiguity, diagram,
or raster occurs.

No reusable EGA/NUMDAM p.102 image existed, so exactly one 1,100-dpi authority
page was made: 7,241,110 bytes / SHA-256
`370CD729724B078B34089C58DA7D8FEB4A5F9CB31460EC6664239EEE493A5F21`.
All topology, stalk maps, prime/maximal ideals, localizations, field arrows,
and punctuation were clear at original detail; no crop or OCR was needed.
French decision ledger: nine rows / 4,159 bytes / SHA-256
`7325833EC8890A9A8A0A627E14902F5DD3160A7CD019F880A41ABAB31EA3BD7E`.

English R31 makes nine prose/logic/register fidelity repairs and leaves four
mathematical units unchanged. The repairs cover universal-quantifier register,
homeomorphism phrasing, `in other words`, proof-reduction wording, two `donc`
connectives, identification of ring A, statement/proof referents, and the
residue-field `that is` clause. Current English source is 25,259 bytes /
SHA-256
`C9C8D501845AC6FDAF6E6172D308C90C5D34B22AED6C3059DF132F48F8B6E04B`;
nine inverse substitutions reproduce R30 exactly. Mathematical/source
repairs, lead errors, and reversals are zero. R31 manifest/tree SHA-256 values
are `AACB1E16646D6DAAEDF384728D9106CF1D752DDC6223B0F405C2BCC8551562ED`
and `D90DDDD991E64D1C022D4BD1CABCD597D46B4FF6ECD23DFAA12B06DB07FEA72E`.

The controlling bounded build uses the predecessor's XeLaTeX engine: 17 pages
/ 184,393 bytes / SHA-256
`2601FE3650929E0E0F11E23DC98A7A05DFE620C1EF59B9618C30D73563675845`.
Two passes have zero hard/undefined/missing/duplicate diagnostics and the same
benign 6.31696-point wrapper overfull. Extracted text is exact on pages 1--15;
only page 16 reflows and page 17 is new. Those two pages were rendered
sequentially at 600 dpi and personally pass.

The first build and one isolation diagnostic mistakenly used pdfLaTeX and are
preserved as non-adjudicative workflow history; their 38 automatic-equation
destination warnings are an engine mismatch, not a source defect. Workflow
ledger: three rows / 2,066 bytes / SHA-256
`5589AE6D1F0425794F948201B4EFB08BE2CAD99B2B79AAE042934C09125B31AB`.
Checkpoint R25 is 8,036 bytes / SHA-256
`8DDC1F5216FE7D1E210C6F6AE57393F677BCDBAE965D948E5890846C59C66CF4`,
PASS/errors empty. Next cursor: PDF one-based p.102 / printed p.103,
continuation of 2.4.5.

## Latest exact continuation — printed p.103 closed

French EGA I is now diplomatic through the end of I.2.5.2 on printed p.103.
Current `source/ega1/ega1-2-fr.tex`: 25,350 bytes / 549 lines / SHA-256
`E1A20C84C2BB1914106EF14B280F5C3B41B5AFA975E5761828167C50206CAA01`.
The page adds Corollaries 2.4.6--2.4.7, Remark 2.4.8, the opening of §2.5,
Definitions 2.5.1--2.5.2, and one native `X -> Y` over `S` triangle. It adds
no raster, source correction, catalogued typo, or unresolved reading.

The exact scoped reuse search found no printed-p.103 authority image, so one
1100-dpi page was generated and personally inspected; no crop or OCR was
needed. Image: 6,908,140 bytes / SHA-256
`68B9B43166B66DE85232A58E9084482CCC1AF3EDB11CFD7973FD5827B53453F3`.
The nine-row French decision ledger is 4,215 bytes / SHA-256
`B520493D1CA931E46505DACB158597147EAC7DC84B9F53EF5AFAB21771AF13A7`.

English R32 makes three individually reversible fidelity repairs: singular
`every y`; grammatical source-register `as one also says, is trivial`; and
`entails ... every s and every x ... must also be over s`, restoring the
French consequence, quantifiers, and necessity. No formula, theorem, source
correction, diagram, target, edge, lead error, or reversal changed. Current
English source: 25,275 bytes / SHA-256
`5CFC1E90B2C64C7E2E71FC9EA27DC56E0B03F6ECC48E4C440D613097AB82E191`.
Eleven-row English ledger: 3,899 bytes / SHA-256
`F889E3A1981064D8F9629E844A4C2996EB480BD55240322365453EDA90898A47`.
Three inverse substitutions reproduce R31 exactly.

R32 source manifest: 127 files / 7,280,281 bytes / SHA-256
`9E77BB96A68A09C711439AF2D22FFC4166B844288E6E85F82B69D515B4CD7680`;
ordinal tree SHA-256
`5220A1B928990312262D72AC84A3BABAA67B2AED3189AFFD25333911B16B3D22`.
Section/full validations have SHA-256
`EB30391344D138D692FDC95AFD80C95C4831BCEE8545E97A08B27AEF38ACB811`
and `EB5C64209251AC0EAB23185C2992E2741F3FE2C7D4A6D3F79D9AD462B4D01683`,
both PASS/errors empty.

The controlling two-pass XeLaTeX reader is 18 pages / 190,068 bytes /
SHA-256 `E0FA8D1C9A7D31496940AC72F7C7331966C19AB219B0825EC3D13D2B11F86D86`.
Pages 1--16 retain exact predecessor text; affected pages 17--18 were the only
compiled pages rendered and personally pass. The triangle is clear and the
blank lower envelope of page 18 is intentional. The literal `$out` build and
other source-neutral harness mistakes remain preserved/excluded in the
nine-row workflow ledger, 5,592 bytes / SHA-256
`0D55851828D617A65EB63D8952244FC1E0B37098E4D02B6D4AB6FD9B380E22F7`.

Checkpoint R26 is 8,157 bytes / SHA-256
`E12D1BAFBF55F86BA7DC24349E7439E518A82397C649E51CA3186B13383BB78A`,
PASS/errors empty. Next cursor: PDF one-based p.103 / printed p.104,
I.2.5.3. Zero agents, no OCR, no bulk render, and no parallel heavy job were
used.

## Latest exact continuation — printed p.104 closed

French EGA I is diplomatic through the p.104 seam in Definition 3.2.1.
`source/ega1/ega1-2-fr.tex` is 27,463 bytes / 592 lines / SHA-256
`AE6B128092ACBB8C1AFB4899EEA003FB966B6FF6669A264B59FD5F095AF4F029`;
new `source/ega1/ega1-3-fr.tex` is 1,706 bytes / 34 lines / SHA-256
`76F6B21FA566B11FA80E6538875E2A122B67616B37331EFE6E39794B697F6B93`.
The admitted scope is 2.5.3--2.5.5, §3.1, and the exact 3.2.1 fragment through
`est un produit des`. No diagram or raster was added.

One source typo is now conclusively catalogued but not corrected in diplomatic
French: 2.5.5 prints `Si X est un S-morphisme`. The following structure map
and section definition require `S-préschéma`; the English already has the
type-correct reading and now carries a visible source note. One 1100-dpi page
(7,176,786 bytes / SHA-256
`B6EF43C83B262486BDCF22618765C16F692428CF2EBA02C007694183909ABF0A`)
handled general transcription, and one tight 2500-dpi crop (146,163 bytes /
SHA-256
`4800122869C732889E83BF080FAC3923451157B73CAD92D2ABC043825933296B`)
proved the type word. No OCR or further image was made. French ledger:
nine rows / 4,498 bytes / SHA-256
`C997C1D70DD5C6F32E67538657AB7DDE820ADF495BEF7EA8AF9BD3309F74769F`.

English R33 changes only `is therefore`, singular `every pair`, and the new
source-note footnote. It retains the confirmed source-backed `S-prescheme`
correction, the plural English topic headings, and all mathematics. Current
`ega1-2.tex`: 25,429 bytes / SHA-256
`5785621211C98B1A4452864F3D408325ECED8F84C6CB16DE0875E052A6E7984F`;
audited `ega1-3.tex` remains 56,496 bytes / SHA-256
`ED1559A08A41EC54E35C4A1E5E192552EF0B1EC52B4CE5FAF1F6E6BB3E5707FB`.
Three inverse operations reproduce R32 exactly. Nine-row English ledger:
3,834 bytes / SHA-256
`B9BEC0096EDDEE9AEDD842F8F9197C31B5C770AA687840BB281944C32E915CF7`.

R33 manifest: 127 files / 7,280,435 bytes / SHA-256
`9FE51AAA429E7749F926D04B52B05891820F4FE6CC3BCCA49FF318AE3402C213`;
ordinal tree SHA-256
`85C3EE351B174E4C8C4CE49E782EA151C72D91E6A35A96674E633E10BA0E6956`.
Section/full validations have SHA-256
`0697B5A637FBE0835EDAC71560C2F7825BD2700A0C39441E107AEE9C0CF23259`
and `835E4222FC24AE496D907DE67B42A61F39EF0D097B41650E89C34C7023490B7D`,
both PASS/errors empty.

The sequential two-pass bounded XeLaTeX PDF is 18 pages / 194,458 bytes /
SHA-256 `E6B26C091A3B982E3E8677E890A50775BEB32CA9D49F9CA269A02F20F6DA5DCD`.
Pages 1--17 retain exact predecessor text; only changed page 18 was rendered
at 600 dpi and personally passes. The three-row workflow ledger records one
lead transcription error repaired before admission—an explicit `X` copied
from the clearer English into diplomatic 2.5.4—and two read-only harness
mistakes; 1,691 bytes / SHA-256
`BF163D055DE9F9AD04CA705051E61A615B146AD3BAB75FFB20A9D9DBF14EC82A`.

Checkpoint R27 is 8,883 bytes / SHA-256
`D21A97F27507F42FC20848B422599877D5F04F4653E8A799DD1A5266B5FD49EF`,
PASS/errors empty. Next cursor: PDF one-based p.104 / printed p.105,
continuation of I.3.2.1. Zero agents, no OCR, no batch render, and no parallel
heavy job were used.

## Printed p.105 closure (2026-08-02)

Diplomatic French now continues through the end of Corollary I.3.2.5. The
current `source/ega1/ega1-3-fr.tex` is 6,117 bytes / 121 lines / SHA-256
`66E0EF2BBE7234C578E07E7465C0EEA8A86E8CB39310ACABD2AFA31A05716C22`.
One direct authority page was generated at 1100 dpi only after an exact reuse
search found none: 9,091x11,428 / 6,192,099 bytes / SHA-256
`303FC3F3301AFC83E03CC8692C126A5D2777A1A000A4132C3DB32483EA642D5A`.
It resolves every p.105 reading; no crop or OCR was needed.

The French page covers the completed universal property in 3.2.1, categorical
product notation and functoriality, affine products by tensor products in
3.2.2, the explicit rho/sigma/tau formula in 3.2.3, invariance under a
monomorphic base map in 3.2.4, and the open-subset corollary 3.2.5. There is
no source correction, typo adjudication, ambiguity, diagram, or raster on this
page. Nine-row French ledger: 4,143 bytes / SHA-256
`4F85769E94A2E8EF7C3B4A6C7A8400D062313CC218BD5C97596C0109C947D8DB`.

Paired English recheck made two reversible grammar/fidelity repairs in
`source/ega1/ega1-3.tex`: the malformed `If ..., and let ... . We then write`
construction is now one complete conditional, and plural `the hypotheses on f
imply` now follows source-singular `the hypothesis on f implies`. No
mathematical formula or assertion changed. Current English file: 56,482 bytes /
SHA-256
`180110F77A0665B749B1F29AB7DE6808E4E9BDEB8A857407572C3D6CF29B693B`.
Two inverse operations reproduce the p.104 source exactly. English ledger:
eight rows / 3,438 bytes / SHA-256
`197F46B25506E94021E7987D7BB54DAC98FE4B649CD232E881DFB87E76004B55`.

R34 has 127 files / 7,280,421 bytes / manifest SHA-256
`7E5002ACDB744AE24EE49272325ADE110DAA406E813E3A80F357DB2B91AE472B` /
ordinal tree SHA-256
`E02F5175C3DEFA9A2EE35E2844ED39ABE01F7EC998331411E405AA7D87E8C241`.
Section and full validations have SHA-256
`50039F4AF08B24AA3A50DFFEA37168CBBDD110EAC16B587BDB441769A8E9F2E6`
and `CAA4B234B7BAB495C977F94484A6B50B6104D6529A056825DB85E1EADD2EFFEC`,
both PASS/errors empty.

The final French bounded build is 19 pages / 202,390 bytes / SHA-256
`B182ED823AB1F6ED7778AF30B96D11095B3284997CBA642234490D896472B206`;
pages 1--17 retain exact predecessor text and pages 18--19 personally pass at
600 dpi. The English bounded check is 12 pages / 113,608 bytes / SHA-256
`1C41C73B871FBD4ECC630BF6B904B18356E68B9782157C753342CEE65C1EE2D4`;
its changed physical page 1 personally passes. Checkpoint R28 is 9,118 bytes /
SHA-256
`E09FD9270B63CA943059DDEDCA557FB420C4C65D60DCF2D46FC68AA51ECCE022`,
PASS/errors empty.

Twelve workflow rows preserve two repaired lead presentation/transcription
slips, nine closed read-only/postprocessing/documentation harness errors, and one resource
lapse: a broad executable search was terminated after about 22 seconds.
Workflow ledger SHA-256:
`3C472FDEC297A20F9A13F0E694A0347435AB84A9143BF96FA05A202BF77147C2`.
No source or mathematics remains affected. Zero agents were used. Next cursor:
PDF one-based p.105 / printed p.106, immediately after I.3.2.5.

## Printed p.106 closure

Printed p.106 is now diplomatically transcribed through the end of Lemma
I.3.2.6.2. Authority is the single direct NUMDAM context image
`EGAI_pdfonebased105_printed106_context_1100dpi.png`, 9,091x11,428 /
4,965,020 bytes / SHA-256
`8ECB4E558B1E60B0C989B2000844C2806C77765669CDFFBAF73C0D7678E4B7FF`.
It was personally inspected at original detail; the page was unambiguous, so
no crop or OCR was made. Current `source/ega1/ega1-3-fr.tex`: 10,254 bytes /
216 lines / SHA-256
`D928E7E21AB6B3C97A5A4B8692A75033075A61A58BA44F2E10E17A6603E81E14`.
New targets are `I.3.2.6-fr`, `I.3.2.6.1-fr`, and
`I.3.2.6.2-fr`. No source correction, source typo, ambiguity, diagram, or
raster exists on this page.

One lead source-integration error was caught before admission. The first append
anchor matched Corollary 3.2.3 and placed p.106 before 3.2.4--3.2.5. Personal
inspection of compiled pages 19--20 exposed the wrong order. The intact
3.2.4--3.2.5 block was moved before the p.106 marker, exact locator order was
replayed, and both earlier builds remain adverse history. The final French
build is 20 pages / 207,270 bytes / SHA-256
`B35FD477AAAB362ABC38A6A957275635795E083F10AA2D3AA726D1D8A362EA6D`;
pages 1--18 retain exact predecessor text and changed pages 19--20 personally
pass at 600 dpi. French decision ledger: 11 rows / 4,400 bytes / SHA-256
`E6757586AB33B973673E229E307EE9914AF5836EEC815643968DBD8F1C2A8F5D`.

The paired English audit found one source-fidelity omission: the proof of
Lemma 3.2.6.2 dropped the printed terminal `c.q.f.d.`. A terminal `\qed`
now restores it; no mathematical assertion changes. Logged retained
normalizations include the explicit English referent in “The proof proceeds,”
the standard “unique S-morphism” compression, “similarly,” the expansion of
`déf.` to `Definition`, and naming numbered 3.2.6.2 as a lemma. Current
English `ega1-3.tex`: 56,486 bytes / SHA-256
`4EE566EFB51DDD19D81E0392070899C2A64A51AF6997D65BC1B4ED07386C317B`;
one inverse operation restores the p.105 source exactly. R35 manifest/tree
SHA-256 values are
`FBEF05B2BDCB707DC1DB7AC8E176981B66F234DA03E1399208F5AE134EA99929`
and `BBBCB2AAA9C5A946847B25B2F483024E637558955863F5A1E194CB4FDCD6C52A`.
Section/full validation SHA-256 values are
`D7D0E55F9AC38AF76A9302D2A593CFAB0D5C41BBC0AFA6BA957C09BCDB8E752A`
and `7DF09CABA52388F313CCA150D89C6309FA8A1E6EA685BBC87BF41D212E0CFE9F`,
both PASS/errors empty. The bounded 12-page English PDF is 113,629 bytes /
SHA-256
`C1907F6CD2FD0E12A678E231DAF85EE336688EC520646D271FB5DDD9181F8F3C`;
physical page 2 personally passes with the terminal square visible.

Nine workflow rows preserve the source-order mistake, literal-`$out` build
routing, and seven closed patch/read-only/path/syntax failures. Ledger SHA-256:
`BD5C5881BBD39B639E4E7611D3514A2DEA177AA74AEF3AF5180A56A6A1B759C9`.
No source or mathematical effect remains. Checkpoint R29: 10,362 bytes /
SHA-256
`FA89227CD8E5CCBBA1EE733B93BE9C87782A39ADA29234C1F316646C942BBAD1`,
PASS/errors empty. Zero agents were used. Next cursor: PDF one-based p.106 /
printed p.107, Lemma I.3.2.6.3.

## EGA I printed p.107 closed

Printed p.107 was read personally from the single authority image
`qa/authority_reuse/ega1_chapter1_opening/EGAI_pdfonebased106_printed107_context_1100dpi.png`
(9,091 x 11,428; 5,888,753 bytes; SHA-256
`E28F0B56EA197B2A091AD9F2CD813EDB01A51CEFADCBC1CA260E4603D6568476`).
It was unambiguous; no crop, OCR, or additional authority image was needed.
French `ega1-3-fr.tex` now runs through the exact p.107 fragment of 3.2.6.5:
14,987 bytes / 307 lines / SHA-256
`6D6DF12A04AEA3B2788983A70AB8A474A156C889369F0FD70CF560439E8F2D51`.
New stable targets are `I.3.2.6.3-fr`, `I.3.2.6.4-fr`, and
`I.3.2.6.5-fr`. No authorial correction or source typo was asserted. One lead
TeX error was caught: the missing command backslash before the emphasized
phrase `schéma affine` was restored. The partial 3.2.6.5 environment has a
temporary bounded-build close; p.108 must remove it and continue the same
environment.

The final French bounded PDF is 20 pages / 212,863 bytes / SHA-256
`0FEA473F2FF2389C7AFB005930BEFA9A03004873BD1C4C9105D58BC3F7507D1B`.
Pages 1--19 are predecessor-text exact; changed page 20 personally passes at
600 dpi. French ledger: 9 rows / 4,017 bytes / SHA-256
`0BBB806A5B6AE6AB72327A3BA47D222AFAD5DFA5C1FFCCFF711CA928660498AF`.

The paired English audit repaired one prior source-fidelity error. The old
English attached “by Lemma 3.2.6.1” to the displayed inverse-image equality;
the French applies it to the following assertion that the restricted maps
define a product. The citation now modifies the correct sentence. No
mathematical content changed. Logged retained choices are “It follows that
we have,” “We immediately see ... and similarly,” “it suffices to prove,”
and expansion of `th.` to `Theorem`.

An exact inverse check also caught fourteen visually inert leading-space
bytes that had appeared after R35. They were removed. R36 and the first
bounded p.107 build remain stale history. Final English `ega1-3.tex`: 56,478
bytes / SHA-256
`E6EEAE7CEF181FBB81A6E671AEE221B87E59AB43AD18174CAE570C9161EE3CA7`;
one inverse operation restores R35 exactly at 56,486 bytes / SHA-256
`4EE566EFB51DDD19D81E0392070899C2A64A51AF6997D65BC1B4ED07386C317B`.
R37 manifest/tree SHA-256 values are
`F5E43F1622CD9BBE5829A18A91771824C0D3426C1D797149F9CB8861FA28861A`
and `D9237435250A25A398CFF70A89052955964AA4DFF7113F74DE77E5A26DA748FE`.
Section/full validations are PASS/errors empty at SHA-256
`346C47C220692A30C2D0D321B6449EB4786C47F70E0C9B6E6D2DBD753C95D737`
and `6642BED78416D3DE1CB1F42ECFB91792B8F5C15BDAC338F0FC7304F5DFCC2FDF`.
The final 12-page English bounded PDF is 113,641 bytes / SHA-256
`2CEAC677F19FDA30ED24C911A04E9D43F75162CDAAC914918A54C457C58BD784`;
its affected page is pixel-identical to the personally inspected clean
pre-closure render.

Four workflow rows preserve two bundled-render-shim failures, one read-only
PowerShell syntax failure, and the fourteen-byte provenance drift. Ledger:
2,255 bytes / SHA-256
`9263FC48129B321445889E776AF4CC47083DF5F852898FFB0788CD69EAF5445C`.
Checkpoint R30: 10,050 bytes / SHA-256
`15657B56D2904F07954F47CC0414038EB9C5D1A24CA41E53EB214EBEBE6BC713`,
PASS/errors empty. Next cursor: PDF one-based p.107 / printed p.108,
continuation of I.3.2.6.5.
The incremental p.107 pre-Stacks scaffold is 5,566 bytes / SHA-256
`188BD70453BAAF986CC5764E9B46B9C82EF8DFBD93A65DA9ACCC99AAEDBC9FFE`;
it records only source-certain semantic nodes/dependencies and leaves final
coordinate/edge closure to a cumulative checkpoint.

## Current checkpoint: EGA I printed p.108 (2026-08-02)

Printed p.108 is now diplomatically transcribed and paired against the English
reader. Current French `source/ega1/ega1-3-fr.tex`: 18,863 bytes / 403 lines /
SHA-256
`C818114F3BAE8B049C945F9AEFE79F2D74AED1959EAB8DB3ED667D4DEA9F367F`.
The page completes 3.2.6.5, adds 3.2.7 and 3.2.8, opens section 3.3, carries
3.3.1--3.3.4, and stops at the exact first-page seam of 3.3.5. Eight stable
French targets and one native `xymatrix` diagram were added; active raster
diagrams remain zero.

The 21-page French bounded PDF is 218,138 bytes / SHA-256
`4F013282A7F82AA7D6AAB44F7C41BB2CDEEFA904B7BA96622AB5F8A217B1B3D6`.
Physical pages 20 and 21 were personally inspected at 600 dpi and pass without
clipping or overlap; the simple diagram was already unambiguous in the single
1,100-dpi direct-authority page image, so no detail crop was generated.

The English recheck restored the French emphasis on `any category` and
`exist` in 3.3.1. Current English `ega1-3.tex`: 56,492 bytes / SHA-256
`0E9CE7FB4E26EE686D1549407FAB8ACF2B521C73C256EB86221524FD89D39D38`.
Two inverse operations reproduce R37 exactly. R38 covers 127 files /
7,280,431 bytes; manifest SHA-256
`15D8794F8BF6AA98FDE1D527EBD87DFED961A03FE59225D7F52D13C245027961`
and tree SHA-256
`85E5FBAAD2D054550D91F893853B51B2AE4DC085E4E831E4B8C4C63F1A62C987`.
Section/full validation SHA-256 values are
`BB292CF24461D37BD69201E91D55C51BE78066D45FD15C26D41FB76C5B95687E`
and `9D9D67D83E60190BA83561D324A72CDE646637162E85F71811A8597D62EE62BF`.

One lead overcorrection was caught and reversed before admission: the existing
English proof square after 3.2.6.5 was initially removed, then restored after
checking the documented modern proof-structure normalization. One failed
build argument created a literal generated `source/$out` directory; its exact
four build artifacts were verified and removed, the console evidence remains
adverse history, and no source byte was affected. Workflow ledger: 3 rows /
2,022 bytes / SHA-256
`697722F29CB151A4487D6C66EA35C8EA0FBCD2B4DD13A188DBFBD9FE53197224`.

Checkpoint R31 is PASS/errors empty: 10,181 bytes / SHA-256
`C2990F06616057C1051F1CA6B4ED3A68BB04BA9B966E7D05B22738A657394282`.
Next cursor: PDF one-based p.108 / printed p.109, continuing 3.3.5 after
removing the temporary bounded environment close.

## Current checkpoint: EGA I printed p.109 (2026-08-02)

Printed p.109 is now diplomatically transcribed and paired against the English
reader. Current French `source/ega1/ega1-3-fr.tex`: 22,550 bytes / 484 lines /
SHA-256
`6C99E997042971815820CF5AF3145EB3E1EF37A8630538B61FB502F339FEBF09`.
The page completes 3.3.5, adds 3.3.6--3.3.8 and Proposition 3.3.9, and ends
after the unpunctuated transitivity diagram whose proof continues on p.110.
Six stable targets and two native `xymatrix` diagrams were added; active raster
diagrams remain zero.

One source typo is now explicitly catalogued: 3.3.8 prints that the product
definition is applied to `f` and `psi`, although the defining pair is `g` and
`psi`. Diplomatic French retains printed `f`. The English reader already uses
`g` and immediately discloses the French `f` in a translator note; direct
authority recheck reconfirms that correction.

The 22-page French bounded PDF is 223,448 bytes / SHA-256
`3FEAD5020F46956CD02F67268B3E1B568B38666D42322997DCAAF0614D285587`.
Physical pages 21 and 22 were personally inspected at 600 dpi and pass. The
single 1,100-dpi authority page was clear; one attempted unnecessary 3,000-dpi
crop produced a blank file, which was inspected and removed rather than
retained as evidence.

The English recheck removed a false terminal period from the `S''` node in the
3.3.9 diagram because the proof sentence continues on p.110. Current English
`ega1-3.tex`: 56,491 bytes / SHA-256
`E5E4C011C43B959AD95657C6B3B79612A0DB6D97A3B926A24A6F853E88861B8C`.
One inverse operation reproduces R38 exactly. R39 covers 127 files /
7,280,430 bytes; manifest SHA-256
`5582CBE296292FDAD0D5FF8B94C8E660466523DD6DEB9DDF28ACA6B3AEA443DC`
and tree SHA-256
`B94674F50196214AF56CD3A4E58BA323CC821B8A61DA7D36669CD1C4B5363BCB`.
Section/full validation SHA-256 values are
`3B74BFEFE4AE0B234D56AD2BEBB980F225636B190FE93178CA7BA5A76489EDB2`
and `5776ECE4968A63C70F9DB3BF93B97F0CA42AB456EC4A340EE3151AD85438EDC5`.

Checkpoint R32 is PASS/errors empty: 10,719 bytes / SHA-256
`188004628018FCA04FD5FE31A8A8E690908FA57195DE2B6A33042A81CAF1CFCD`.
Next cursor: PDF one-based p.109 / printed p.110, the sentence immediately
following the transitivity diagram; there is no temporary environment close.

## Current checkpoint: EGA I printed p.110 (2026-08-02)

Printed p.110 is now diplomatically transcribed through 3.3.12. Current French
`source/ega1/ega1-3-fr.tex`: 25,782 bytes / 567 lines / SHA-256
`EBB451F8E44FF4382A351AD5F19A9D3C657E8F7AAEB9B340073D42BB126989C6`.
The page adds seven stable targets, equations 3.3.9.1, 3.3.9.2, and 3.3.10.1,
Corollaries 3.3.10--3.3.11, one native diagram, and 3.3.12 through `u=v`.
French source corrections remain zero; raster diagrams remain zero.

The p.110 diagram comparison exposed a real prior lead-QA miss. In Xy-pic,
label sides are direction-relative: the lower-row `varphi`, `varphi'`, `psi`,
and `f` labels in three p.109--p.110 left-arrow diagrams had rendered above
instead of below. Both French and English sources now match the printed label
sides. The p.109 R32 text/source checkpoint remains preserved, but its diagram
layout-PASS statement is superseded by R33.

The English Corollary 3.3.11 diagram also omitted the mathematical label
`psi_(S')` and attached a false period to its lower-right `X` node. Both are
repaired. Current English `ega1-3.tex`: 56,504 bytes / SHA-256
`6196282B5900DB26B985B1E0E12385B7FA995F7807E8E43D833C0EB8CE8227F8`.
Seven inverse operations reproduce R39 exactly. R40 covers 127 files /
7,280,443 bytes; manifest SHA-256
`072C32119B3126F28C96BB6958FDDFA4A8E5F34B949E1E383F57C96D9D75FE00`
and tree SHA-256
`17CFEFE9E801D74857E235DD508E72F4C42AD0FB9EF123176E88EE499B26E215`.
Section/full validation SHA-256 values are
`6CFA4AF4D781237FEA638A7C75A5825D1598033EF2C4A2D3E2FF03472563844F`
and `F5F37BBAACF6F350736B7E1E6C74BF8686931953FF8B331B501AD54393EDBEB1`.

The final French bounded PDF is 22 pages / 227,511 bytes / SHA-256
`04DAA9D0016A0D95C17CF68BF7468F9ACD2DD2B05EF0FBDB153A16B560B38D88`;
pages 21--22 were personally re-inspected at 600 dpi. The English bounded PDF
is 12 pages / 113,708 bytes / SHA-256
`5D4A01B13AB03D0B2D4203FB87C665CBB848B9B6AC05EAC5B1F89B1AC0C8F17A`;
pages 4--5 were personally re-inspected at 600 dpi. These are compiled-layout
checks; source detail came from the single 1,100-dpi NUMDAM page.

Checkpoint R33 is PASS/errors empty: 11,587 bytes / SHA-256
`66E00BE78EEB8B6B4E8E470C2DAFEC901274DC24B6E845FBE477BE2DB5034B76`.
Next cursor: PDF one-based p.110 / printed p.111, continuing 3.3.12 after first
removing the temporary bounded `\end{env}`.

## Current checkpoint: EGA I printed p.111 (2026-08-02)

Printed p.111 is now diplomatically transcribed through the first words of
3.4.2. Current French `source/ega1/ega1-3-fr.tex`: 30,015 bytes / 654 lines /
SHA-256
`5C0481F52B66A1402C2B692B57F497B0CBEBE14763960CC43878CEEA7084F065`.
The page adds eight stable targets covering the completion of 3.3.12,
3.3.13--3.3.15, the canonical Hom correspondence, the 3.4 heading, 3.4.1,
and the opening of 3.4.2. The exact inverse truncation plus restoration of the
p.110 temporary close reproduces the p.110 source byte-for-byte.

Two printed source typos are preserved diplomatically and catalogued rather
than silently repaired. In 3.3.12 French prints codomain `Y_(S')`, although the
statement assumes `f:X->X'`; in 3.3.15 it prints scheme morphisms `Z[T]->X`,
although 3.3.14 and the same paragraph's ring maps require `X->Z[T]`. Stable
source IDs are
`EG-EGA-I-P111-FR-3312-BASECHANGE-TARGET-Y-VS-XPRIME-SRCTYPO-001` and
`EG-EGA-I-P111-FR-3315-MORPHISM-DIRECTION-SRCTYPO-001`. The paired English
reader uses the mathematically required forms and gives each an immediate
visible translator note.

Current English `ega1-3.tex`: 56,850 bytes / SHA-256
`A9FAD4038374CDC5BEAEC4412096AEC62D437D63A6D232349757BC868E0FB33C`.
Two inverse source patches reproduce R40 exactly. R41 covers 127 files /
7,280,789 bytes; manifest SHA-256
`09EB142C493126469764AFEF70825EAF27FC1D7344BE5C422AA35D56AD953BCC`
and tree SHA-256
`4021B24BB11E6520EEC75F4748E75044FFDD2E14FB9733606DAD564650B26F33`.
Section/full validation SHA-256 values are
`68BFE818FA2F0F13F0E2438AEA6F639E4EA61379A0841C08C788942BD695BFBC`
and `29A6313B09FED8E055CE6D3D5ED7E2928FDF2E4F31DE6C35862FF43D4D49DF30`.

The final French bounded PDF is 23 pages / 234,431 bytes / SHA-256
`13D29B451526DB13EE31A6DDCD2B904C8CDD759A2C56FEC8D6164F678751B538`;
pages 21--23 were personally inspected sequentially at 600 dpi. The English
bounded PDF is 13 pages / 115,301 bytes / SHA-256
`5C2E0ACC6499CA45E330FB01C8A2F40C3C70DA3788B2C8DDC8311662EB22BB03`;
all reflowed pages 6--13 were personally inspected sequentially at 600 dpi.
Source reading used the single 1,100-dpi authority page and one tight 5,000-dpi
formula crop; no OCR or bulk rendering occurred.

Checkpoint R34 is PASS/errors empty: 12,101 bytes / SHA-256
`7FBFDD83E08BC65055A19F18FEB29EED152777414894DBE6A4A6844668AA3AE3`.
Next cursor: PDF one-based p.111 / printed p.112, continuing 3.4.2 after first
removing the temporary bounded `\end{env}`.

## Superseding current checkpoint: EGA I printed p.112 (2026-08-03)

Printed p.112 is diplomatically transcribed and paired against the English
reader. Current French `source/ega1/ega1-3-fr.tex` is 33,565 bytes / 733 lines /
SHA-256
`F8C95EAD1820DC660F61AA52C163C23D5F60C2A0F234DC668029F2B35E9F9ACE`.
It closes 3.4.2, adds 3.4.2.1, 3.4.3 with formulas 3.4.3.1--3.4.3.2 and a
native product diagram, 3.4.4, and the p.112 fragment of 3.4.5 through `la
donnée de sa`. French source corrections, raster diagrams, and unresolved
readings are zero. Two draft errors--a false period after 3.4.2.1 and a
mis-sided lower `psi'` diagram label--were caught from the authority image and
repaired before checkpoint admission.

R35 validation is 5,090 bytes / SHA-256
`2024E09325ECB75B7398699C954856DA99CC13DB130E242357CF870C31110B9F`,
PASS/errors empty. French bounded PDF: 24 pages / 239,546 bytes / SHA-256
`D0D8A789017B3931C4B2255DA3700FEF47C167CD9DB3982EF1B010C8A0420160`.
Source reading used one 1,100-dpi context image and one tight 1,800-dpi diagram
crop; no OCR or batch rendering occurred.

The paired English source is 56,850 bytes / SHA-256
`EC3BB57090C0A12EF48CF9572B0EE933DE8E0759E1F51379A921528A6BB1142E`.
The sole p.112 mutation repairs the lower `psi'` label side in the 3.4.3
diagram. English bounded PDF: 13 pages / 115,253 bytes / SHA-256
`A6742676640ADC895B1A24922B5119CDCFBBDE351F8EAEF35C9680BF27400D9E`.
The complete English source-tree gate is still R41/p.111; R42 manifest and
diff validation for the current p.112 bytes remain open.

Exact next cursor: PDF one-based p.112 / printed p.113, continuation of 3.4.5.
Remove only the temporary final `\end{env}` before appending the next page.

## Successor checkpoint: printed p.113 complete

The earlier p.112 cursor above is superseded. Diplomatic French is now admitted
through printed p.113, ending with the displayed equality in Corollary 3.4.8.
Current `source/ega1/ega1-3-fr.tex`: 37,418 bytes / SHA-256
`C457C0F47862A74CABBCEC04E9F5B91919DAE184C3DBBD61DF896FEF4D14EF15`.
No printed-source typo, unresolved reading, or French correction was admitted.

Paired English is 56,847 bytes / SHA-256
`8D581435C0AC808A879B35C5805834A620BEF657898EAD308744C357B6E537F8`.
This checkpoint repairs two p.113 prose-fidelity defects and one inherited
p.112 citation target, I.2.2.4 to source-backed I.2.4.4. R43 is the current
complete 127-file gate: manifest SHA-256
`79DC085957FB058EB002014309BA1DB84FD8AC6E62690DA650FC43893699E62A`;
canonical tree SHA-256
`531CBD2815F995C97B1DEDFDE19B68CD93A045FD639D07DF103027969FA86A10`;
diff validation PASS/errors empty at SHA-256
`1444F102061A03B68807713A8B119976D8A6E796204EE4D7216A74DE51820BDE`.

R36 validation is PASS/errors empty at SHA-256
`06D68E902E48B278C0AB683D1992FFE739104AE7B670D55FD316EDF22046FA30`.
Final bounded PDFs are French 24 pages / 244,482 bytes / SHA-256
`ABD2CB513FAC8DEA62CF3E67227301F319EA4A935AA589292CA93AD984D0EFDE`
and English 13 pages / 115,245 bytes / SHA-256
`4FA5EF4EC8E04E6270E77731022D347B309CED67A74B73B5EBC4064C4AE58440`;
all affected pages pass serialized visual QA.

Exact next cursor: NUMDAM PDF one-based p.113 / printed p.114, proof of
Corollary 3.4.8 beginning `En effet`. The French source has no temporary close
to remove.

## Successor checkpoint: printed p.114 complete

The earlier p.113 cursor is superseded. Diplomatic French is now admitted
through printed p.114: the proof of 3.4.8, Proposition 3.4.9 and proof,
subsection 3.5, and 3.5.1 clauses (i)--(ii). Current
`source/ega1/ega1-3-fr.tex`: 41,097 bytes / 885 lines / SHA-256
`9545DE0E3DB01EB04591FBD65F5CDB406530A28F906132E331531ADD0B0C76BE`.
French preserves and catalogues the printed 3.4.9 tensor-product
`monomorphisme` as
`EG-EGA-I-P114-FR-349-TENSOR-MONOMORPHISM-SRCTYPO-001`; no diplomatic source
correction was applied and no reading remains unresolved.

Paired English is 56,847 bytes / SHA-256
`E6CAD01349ABDC5F3AEBA24356E9593C1D1BFC717038E9D35D99E267C9C5416B`.
The only p.114 English source mutation moves the `q` label below its leftward
arrow to match authority. The inherited correction `monomorphism` to
`homomorphism` and its visible translator note are confirmed and retained;
no new English mathematical wording was introduced. R44 is the current
complete 127-file gate: manifest 36,060 bytes / SHA-256
`0574B3D851A04E1023F4D5BDE1D9D1717D9D644BD9EA93D542BF0CBE5950E10D`;
canonical tree SHA-256
`BBD421CCBEE4825695882D5C10BEBE12C3663B53D9D9A16F901490372168CB61`;
diff validation PASS/errors empty at SHA-256
`08201B423C2CFEA44F8649A4B2F0AF570B04B6E578717BA91905A0D679186778`.

R37 validation is 7,090 bytes / SHA-256
`C0575FC4F2215613939BC4657407D123370967A385B83E11229333D005CCFAE1`,
PASS/errors empty. Final bounded PDFs are French 25 pages / 250,775 bytes /
SHA-256
`B3BC332189B2A9A80D04603178136E6B41EEC71B2DA5B2E8C7818AB4C321E134`
and English 13 pages / 115,257 bytes / SHA-256
`2A131D38698F5BDEA731D22CA28FD157C4DD6C4C9164BE578757D1D8A387259D`;
all affected pages pass serialized visual QA. One 1,100-dpi authority image
was used; no OCR, batch rendering, unbounded search, or whole-page
original-detail load occurred.

Exact next cursor: remove only the temporary final `\end{env}`, then continue
at NUMDAM PDF one-based p.114 / printed p.115, continuation of 3.5.1 after
clause (ii).

## Successor checkpoint: printed p.115 complete

The earlier p.115 cursor is superseded. Diplomatic French is admitted through
the displayed diagram in 3.5.5. Current `source/ega1/ega1-3-fr.tex`: 44,578
bytes / 969 lines / SHA-256
`FCDD412953CDC75797758BCF4FA29B42BF90B703D497D5AA70B83BE8DF8173ED`.
The page completes 3.5.1, adds 3.5.2--3.5.4, and opens 3.5.5. French source
corrections, catalogued p.115 typos, and unresolved readings are zero.

Paired English is 56,894 bytes / SHA-256
`AB5F2BBC7E3AD82C0DAF342BC0AD0B3012FCB219FC02F6AFDA7E0DB70C6B347B`.
The p.115 pass repairs one mathematical logical antecedent, two prose adverbs,
and one diagram-label side. R45 is the current complete 127-file gate:
manifest SHA-256
`DFD8BF3BD7A461608179190AAA5FF72AA5F345ECC46C3127D357BEC7B08088F8`,
canonical tree SHA-256
`45B3E3D362F2E4D5227E26BFE4CEAA5620176581466DBF9C83D6D26FC0EADE9C`,
and PASS/errors-empty diff validation SHA-256
`903FF29D8B9EE60E69B9B523E6813C8F5F824BC6E63E7A7066F5A9DA4BE57198`.

R38 validation is 7,651 bytes / SHA-256
`8D0C007424BBFAECD5F59CE33A25567EE6923C4A88D461BB87CE86ADA2496E1B`,
PASS/errors empty. Final bounded PDFs are French 26 pages / 255,527 bytes /
SHA-256
`0A610E2218F4AEC0F1529ADF7975E4927B54E30E8A215A7581308075A8C29AE1`
and English 13 pages / 115,338 bytes / SHA-256
`6798D38939861A320C7046601BA5DD2D6AE4F498CA914F4D84C191F86C3C5A1A`;
all affected pages pass serialized visual QA. The five workflow/path events
are fully recorded and had no source effect.

Exact next cursor: remove only the temporary final `\end{env}`, then continue
at NUMDAM PDF one-based p.115 / printed p.116 immediately after the 3.5.5
diagram.

## Successor checkpoint: printed p.116 complete

The earlier p.116 cursor is superseded. Diplomatic French is admitted through
the exact words `de la commutativité du diagramme` in the proof of 3.5.10.
Current `source/ega1/ega1-3-fr.tex`: 48,499 bytes / 1,059 lines / SHA-256
`0B41FE7CCF850924D06C8F8BB2099555506985FCFF23A70CED2952C4AD7ED4EA`.
The page completes 3.5.5, adds 3.5.6--3.5.9, and opens the proof of 3.5.10.
French source corrections, catalogued p.116 typos, and unresolved readings are
zero. There is no temporary environment close at the current seam.

Paired English is 56,913 bytes / SHA-256
`5A1EA6875D95D891D87381A288C33B7184B97A9343A982D82D353EB3DA03F2A6`.
The p.116 pass restores two omitted source instances of `aussitôt` as
`immediately`; no English mathematical claim, formula, dependency, or diagram
changed. R46 is the current complete 127-file gate: manifest 36,969 bytes /
SHA-256
`37C59DE260A37EEB5D4542C3AF9FF71531CC01A6BE3450FAB280F0C1776BDC70`,
canonical tree SHA-256
`83506DB9F2EEE686B2E5A7DC2E72BEF4730A3CD42A2C04667F0955FA16779AAA`,
and PASS/errors-empty diff validation 5,219 bytes / SHA-256
`8FBD28F268EF1F8601F1F81A188B0D3FF674F5F64EA8F73881066EA9503B9083`.

R39 validation is 7,251 bytes / SHA-256
`083D997689E74C8E7610C0894F978E643753D73DCCA4D8BB61B1FBA17A72339A`,
PASS/errors empty. Final bounded PDFs are French 27 pages / 260,286 bytes /
SHA-256
`904FC054DFAF507D1D65ADCEC64338CF05F9C993D4856C231512CA0A9D2158D2`
and English 13 pages / 115,346 bytes / SHA-256
`450AF97FBF4066D3DCB2A72447CA5CFAE11A3684BC9217F3EBF23AFDA8A1A20B`;
all affected pages pass serialized visual QA. The five workflow/resource
entries are fully recorded and had no source effect.

Exact next cursor: append directly at NUMDAM PDF one-based p.116 / printed
p.117, beginning with the diagram that completes the proof of 3.5.10. Do not
remove any closing environment before continuing.

## Successor checkpoint: printed p.117 complete

The earlier p.117 cursor is superseded. Diplomatic French is admitted through
the complete displayed fibre-composition identity in 3.6.3. Current
`source/ega1/ega1-3-fr.tex`: 52,851 bytes / 1,156 lines / SHA-256
`DF4B43CE4A6D15D2C0295DFBF173A00ABC998A98C38AEE127E76AF9593D35153`.
The page completes 3.5.10, adds 3.5.11, opens 3.6, admits 3.6.1--3.6.2, and
begins 3.6.3. French source corrections, catalogued p.117 typos, and
unresolved readings are zero. The final `\end{env}` is a temporary bounded
close for the continuing 3.6.3 paragraph.

Paired English is 56,919 bytes / SHA-256
`6CCAAE5D05343975ABD6E68B1265525DDCA2C3F7C4A8D25987649DE73DD6C2AC`.
The p.117 pass restores one omitted `d'abord` as `first`; no mathematical
claim, formula, dependency, or diagram changed. R47 is the current complete
127-file gate: manifest 37,432 bytes / SHA-256
`E8C29077CDC78DFB6A7F8A5544F3199F9E5564F64163B10FFC0047B21FC14E8B`,
canonical tree SHA-256
`FA3CD639E1DC14145A9270C641F99F1D3FEF399EE96BFB40CC6B8ACD0F35E6E7`,
and PASS/errors-empty diff validation 5,135 bytes / SHA-256
`A4E877FFFF87ECE878AFDD93BA29D2C2B4A48527D344B533AF40AF992FF2F5F1`.

R40 validation is 7,122 bytes / SHA-256
`F35A37B89CB1DEE40A79D0C4E7AA708A006B608C166B153E241E2FB662A6464E`,
PASS/errors empty. Final bounded PDFs are French 27 pages / 265,378 bytes /
SHA-256
`A41C256BC56DA3705B8DCFC20DD8818010A78B496536C8547F62D9CD9D0581F2`
and English 13 pages / 115,351 bytes / SHA-256
`32D71EB8A3CC7E7406F68993AF868F9D250DD5A667065769A90AD2E46E56B00E`;
all affected pages pass serialized visual QA. The six workflow/resource
entries are fully recorded and had no diplomatic-text or English-tree effect.

Exact next cursor: remove only the temporary final `\end{env}`, then continue
3.6.3 at NUMDAM PDF one-based p.117 / printed p.118 immediately after the
displayed fibre-composition identity.

## Successor checkpoint: printed p.118 complete

The earlier p.118 cursor is superseded. Diplomatic French is admitted through
the exact words `l'unique point` in 3.7.2. Current
`source/ega1/ega1-3-fr.tex`: 57,071 bytes / 1,241 lines / SHA-256
`2EDB68A378FE6C959B048180148FF7E69E42916D261F92207A24DA793B120192`.
The page completes 3.6.3, adds 3.6.4--3.6.5, opens subsection 3.7 with its
footnote, adds 3.7.1, and begins 3.7.2. French source corrections, catalogued
p.118 typos, and unresolved readings are zero. The final `\end{env}` is a
temporary bounded close for continuing 3.7.2.

Paired English is 56,933 bytes / SHA-256
`55C1E1129E40F1E2F8DB7B46867B3E49AE2556F04C1CFE1FBF5EE3C149B63BD9`.
The p.118 pass restores the footnote's forward scope from later in Chapter I
and from Chapter II; no mathematical claim, formula, dependency, or diagram
changed. R48 is the current complete 127-file gate: manifest 37,933 bytes /
SHA-256
`309B5B0A48AC2F3AD8903891526D8722ECB2C64C5CF18F5293F398BF89B58668`,
canonical tree SHA-256
`E8331E55DEABD57007298B17012BE1E50C20370837535F413F3679EBE3FB646B`,
and PASS/errors-empty diff validation 5,402 bytes / SHA-256
`FE9746CE8BB49D3DF2F96D9EBF9B49AE67B8EEBFD61FD79FAC972AEDA31D4373`.

R41 validation is 7,161 bytes / SHA-256
`40CE9BF9A4180940D00ACA2E0A69BA3D3F51CF059F9BFD037D26B4A7D83AEF7A`,
PASS/errors empty. Final bounded PDFs are French 28 pages / 272,098 bytes /
SHA-256
`9AA2E9A7A387F1881BC861C0AED7CCBD9BDADA9F2F558F6A3E45005375536DD0`
and English 13 pages / 115,362 bytes / SHA-256
`28A75B6834B4151C5CA9CF4FD2C475CA4F809CA8E267CE7EF58113B1E9643689`;
all affected pages pass serialized visual QA. The six workflow/resource
entries are fully recorded and had no diplomatic wording or English-tree
effect beyond the intended repair.

Exact next cursor: remove only the temporary final `\end{env}`, then continue
3.7.2 at NUMDAM PDF one-based p.118 / printed p.119 after `l'unique point`.

## Successor checkpoint: printed p.119 complete

The earlier p.119 cursor is superseded. Diplomatic French is admitted through
the complete statement of Proposition 4.1.2, ending with `(Y, O_Y) est un
préschéma.` Section 3 now closes in `source/ega1/ega1-3-fr.tex`, 59,766 bytes /
1,282 lines / SHA-256
`DB4F986C9FDC1B66FF2D627C5E9121BCE0490563B7C14415320B5DDD7424B851`.
New `source/ega1/ega1-4-fr.tex` is 1,292 bytes / 29 lines / SHA-256
`BEDC1B141252E20EE298389D39C3B9C38D9403E08AF57F5ED53CD25BB115916F`.
French source corrections, catalogued p.119 typos, and unresolved readings are
zero. No temporary environment close is present; an in-memory two-operation
inverse reproduces the sealed p.118 source exactly.

The paired English recheck changes no source byte. `ega1-3.tex` remains
56,933 bytes / SHA-256
`55C1E1129E40F1E2F8DB7B46867B3E49AE2556F04C1CFE1FBF5EE3C149B63BD9`;
`ega1-4.tex` remains 33,365 bytes / SHA-256
`55FCE2B2C9A51F7FC86DCEB1A8E0BD4EC6E06818C28E302FFE045B4CA323B275`.
R49 is the active complete 127-file gate: 7,280,872 bytes, manifest 38,368
bytes / SHA-256
`0BB20AFE664720F711F04AEC55D88E96DA918C27C26DF26FE6D60A7AE8838E8C`,
tree SHA-256
`E8331E55DEABD57007298B17012BE1E50C20370837535F413F3679EBE3FB646B`,
and PASS/errors-empty zero-delta validation 5,564 bytes / SHA-256
`519B2CBC2EA3FCB9FCCCD3F4FB85907776DAD1D260F48BE86E6ED3D888B82031`.

R42 validation is PASS/errors empty at 8,838 bytes / SHA-256
`B82C5D63AF34111BBE4D94700582770A36CFF1A005E76C8C088E960421DE83CC`.
Final bounded PDFs are French 29 pages / 276,883 bytes / SHA-256
`CB39695477CB9CE1791569D358BE74EBAC2B733F317E92C33DDE497D4225E0AF`
and English 13 pages / 117,660 bytes / SHA-256
`985FC4F4B0A5BD7E6FA236CDC9AC17720A7FAF34D6859C28DF504E2C1F2F82DA`;
all affected pages pass serialized visual QA. Fourteen workflow/resource
entries are complete, and temporary `Q:` is absent.

Exact next cursor: append directly to `source/ega1/ega1-4-fr.tex` at NUMDAM
PDF one-based p.119 / printed p.120, beginning the proof of Proposition 4.1.2
with `Il suffit évidemment`. Do not remove any closing environment first.

## Successor checkpoint: printed p.120 complete

The earlier p.120 cursor is superseded. Diplomatic French is admitted through
the exact printed-page words `d'un sous-` opening Proposition 4.1.6.
`source/ega1/ega1-4-fr.tex` is 5,966 bytes / 118 lines / SHA-256
`90C1D93784F8A1817702732BE9E69B513F9D538A4F878688894D131F24F20B71`.
One temporary final `\end{proposition}` balances the checkpoint; one inverse
operation restores the p.119 file exactly at SHA-256
`BEDC1B141252E20EE298389D39C3B9C38D9403E08AF57F5ED53CD25BB115916F`.
French source corrections, catalogued p.120 typos, and unresolved readings
are zero.

The paired English recheck changes no source byte. R50 is the active complete
127-file gate: 7,280,872 bytes, manifest 38,864 bytes / SHA-256
`D6F7AFA347FD3B0B3D63E310394D0D3CE9D77AF57F26C44A9C3FE189C98D43A8`,
tree SHA-256
`E8331E55DEABD57007298B17012BE1E50C20370837535F413F3679EBE3FB646B`,
and PASS/errors-empty zero-delta validation 6,347 bytes / SHA-256
`988292B9754053803D7AEDDD1817D95A7543D6A1361F806F91BC2C29E1DD4FC0`.

R43 validation is PASS/errors empty at 9,149 bytes / SHA-256
`4721AB517C81B0770246C1F1CC1A4FF1C579FB50A0392A767E83DD9B51F5EF20`.
Final bounded PDFs are French 29 pages / 281,746 bytes / SHA-256
`2ADC022DE0787263913EBEC8BD06BDDDE5706B480AC059C2354C126E5519B871`
and English 14 pages / 122,887 bytes / SHA-256
`172F4C958CEFE1BAA310557229E6F73D0FEB58A3462A6BA8634A1296BA2546F8`;
both terminal pages pass serialized visual QA. Eleven workflow/resource
entries are complete, and temporary `Q:` is absent.

Exact next cursor: remove only the temporary final `\end{proposition}`, then
continue Proposition 4.1.6 from direct NUMDAM PDF one-based p.120 / printed
p.121 authority after the exact p.120 hyphenation `d'un sous-`.

## Successor checkpoint: printed p.121 complete

The earlier p.121 cursor is superseded. Diplomatic French is admitted through
the exact terminal words `est un morphisme Z\to Y` in the open proof of
Proposition 4.1.9. `source/ega1/ega1-4-fr.tex` is 10,356 bytes / 203 lines /
SHA-256
`52A11F6F8AFE416C5D1999C463FE328060F3E1009BB14E0781A636C6761C6169`.
No temporary environment close is present; one inverse operation restores the
p.120 file exactly at SHA-256
`90C1D93784F8A1817702732BE9E69B513F9D538A4F878688894D131F24F20B71`.
French source corrections, catalogued p.121 typos, and unresolved readings
are zero.

The paired English recheck changes no source byte. R51 is the active complete
127-file gate: 7,280,872 bytes, manifest 39,418 bytes / SHA-256
`F6736445D6C310C85A5FA44E5B718C71EC6B6574DCC28CFF1BD8AD673EBF46A8`,
tree SHA-256
`E8331E55DEABD57007298B17012BE1E50C20370837535F413F3679EBE3FB646B`,
and PASS/errors-empty zero-delta validation 6,385 bytes / SHA-256
`8E0A9E1AD4122E6320D288A3CDE75D7262C4608FEB2D7983ADBD2101FAE6C6BC`.

R44 validation is PASS/errors empty at 9,607 bytes / SHA-256
`16F74B50E79D3AFF7373FB8104C9507FC028D7E151523550C8165ACC3D668EF8`.
Final bounded PDFs are French 30 pages / 287,123 bytes / SHA-256
`220A7280A4420D338E9A910B4A971E2357DEB62390F4E61DE018738AFDDEC732`
and English 14 pages / 128,025 bytes / SHA-256
`148D326B436272E09B8C644CD29F1F05064517B4B02EC6006220935D04A43472`;
all affected pages pass serialized visual QA. Twelve workflow/resource
entries are complete, and temporary `Q:` is absent.

Exact next cursor: append directly from NUMDAM PDF one-based p.121 / printed
p.122, continuing the proof of Proposition 4.1.9 after `g':Z\to Y`. Do not
remove any closing environment first.

## Successor checkpoint: printed p.122 complete

The earlier p.122 cursor is superseded. Diplomatic French is admitted through
the exact terminal words `restriction à $U$ de l'image` in the open proof of
Proposition 4.2.2(b). `source/ega1/ega1-4-fr.tex` is 14,467 bytes / 285 lines /
SHA-256
`984EFEEB45E09398B9B1E0E7DAB3602D89119F2AC2A860A19872CFEC0494992E`.
Its final `\end{enumerate}` is temporary; one inverse truncation restores the
p.121 file exactly at SHA-256
`52A11F6F8AFE416C5D1999C463FE328060F3E1009BB14E0781A636C6761C6169`.
The diplomatic source preserves and catalogues one printed mathematical
error: proof 4.2.2(a) reverses the source and target of `\theta^\sharp`.
French source corrections and unresolved readings remain zero.

The paired English recheck changes no source byte and retains the explicit,
mathematically typed correction with translator footnote. R52 is the active
complete 127-file gate: 7,280,872 bytes, manifest 40,084 bytes / SHA-256
`B2BCA961EEE011D9E5F03147CD696F9888D96E6A58F944DD1A2ED6FB292EE614`,
tree SHA-256
`E8331E55DEABD57007298B17012BE1E50C20370837535F413F3679EBE3FB646B`,
and PASS/errors-empty zero-delta validation 6,974 bytes / SHA-256
`75B3BC2A7E09CDDBCBAEA5D558E9F37095FA4052C908330323F43F2D50A2AF4D`.

R45 validation is PASS/errors empty at 10,598 bytes / SHA-256
`B188DC15970531829D52CDC27BEC574A7DC056E05C5BCB9814F326657C680B14`.
Final bounded PDFs are French 31 pages / 291,778 bytes / SHA-256
`3B5CF6685A40A87632D6B6A269669504A62EB540D6205E022173EE3239BBD5E4`
and English 15 pages / 133,594 bytes / SHA-256
`D4EF20AEA2BC89EF7924C5B42870B64DE05F5E6F6AE39B8D2D66E67C566E676C`;
all four affected pages pass serialized visual QA. Eleven workflow/resource
entries are complete, and temporary `Q:` is absent.

Exact next cursor: remove only the temporary final `\end{enumerate}`, then
continue Proposition 4.2.2(b) from direct NUMDAM PDF one-based p.122 /
printed p.123 authority after `restriction à $U$ de l'image`.

## Successor checkpoint: printed p.123 complete

The earlier p.123 cursor is superseded. Diplomatic French is admitted through
the exact terminal words `il faut et il suffit` in Corollary 4.2.4(a).
`source/ega1/ega1-4-fr.tex` is 18,980 bytes / 365 lines / SHA-256
`B75325670BDB54B9B6F17AF3945110A86E2506F3EF41A699FE3032B5B5EEFACC`.
Its final `\end{enumerate}` and `\end{corollary}` are temporary; one inverse
suffix replacement restores the p.122 file exactly at SHA-256
`984EFEEB45E09398B9B1E0E7DAB3602D89119F2AC2A860A19872CFEC0494992E`.
The initially mis-targeted delimiter removal was caught and exactly restored
before continuation, with no remaining effect. French source corrections,
new p.123 printed-source errors, and unresolved readings are zero.

The paired English recheck changes no source byte. R53 is the active complete
127-file gate: 7,280,872 bytes, manifest 40,442 bytes / SHA-256
`A66887EBE9AA70959C970051C08550FD8A4DE525CD78D23A21662B4C75F18ED5`,
tree SHA-256
`E8331E55DEABD57007298B17012BE1E50C20370837535F413F3679EBE3FB646B`,
and PASS/errors-empty zero-delta validation 7,465 bytes / SHA-256
`465F8FE2D3DC7B10BA4CC74792B81A8BD65B51FD29C03B37B0AD2495F5979DD9`.

R46 validation is PASS/errors empty at 10,743 bytes / SHA-256
`859AE56FAFA479F12F68B1080E61100CD9B0F2C750DFA9041774516BC3CDF20C`.
Final bounded PDFs are French 31 pages / 297,263 bytes / SHA-256
`E52987A1F74065FE13BE9177DE04E7DBFD0B00D456D1212397DE9AA4A59AC6E7`
and English 16 pages / 139,048 bytes / SHA-256
`892949ADB0BED5773CC14933B0CCD79860D21FBA1501CC9639A61DC835B6C24E`;
all affected pages pass serialized visual QA. The hung English R1 diagnostic
is retained and excluded from final claims; no XeLaTeX process or `Q:`
mapping remains.

Exact next cursor: remove only the temporary final `\end{enumerate}` and
`\end{corollary}`, then continue Corollary 4.2.4(a) from direct NUMDAM PDF
one-based p.123 / printed p.124 authority after `il faut et il suffit`.

## Successor checkpoint: printed p.124 complete

The earlier p.124 cursor is superseded. Diplomatic French is admitted through
the exact terminal phrase `la restriction de $\alpha\times_S\beta$` in the
open proof of Proposition 4.3.1. `source/ega1/ega1-4-fr.tex` is 23,239 bytes /
440 lines / SHA-256
`E9061031DB90102A99851D0397A879CCF422F50A820F8C2A30AF30E222CC9185`.
No temporary final environment close is present. One inverse suffix
replacement restores the p.123 file exactly at SHA-256
`B75325670BDB54B9B6F17AF3945110A86E2506F3EF41A699FE3032B5B5EEFACC`.
French source corrections, new p.124 printed-source errors, and unresolved
readings are zero.

The paired English recheck changes no source byte. R54 is the active complete
127-file gate: 7,280,872 bytes, manifest 40,800 bytes / SHA-256
`9A53F6C16D4DD5D366696988C95321DCE2062E1010CF981526C7233296F541A4`,
tree SHA-256
`E8331E55DEABD57007298B17012BE1E50C20370837535F413F3679EBE3FB646B`,
and PASS/errors-empty zero-delta validation 7,092 bytes / SHA-256
`BA53F085977613E2ABA88B3CF943837204E3BBB9A9C2D1EFF80D59891EA8B43C`.

R47 validation is PASS/errors empty at 10,336 bytes / SHA-256
`49BAFE90DBC08F35258F8C1AB4C3B476971B3B9B5359667B8C9D0564CC4E6A54`.
Final bounded PDFs are French 32 pages / 302,104 bytes / SHA-256
`E9524E042DFC8936359BE9C6AECF3BA24943CB25E8EB0F3BBF7F147C326CE25B`
and English 17 pages / 144,319 bytes / SHA-256
`5BF1482C1EB63A89EAADB179DEB06C10B4F88D49116C462AB46C919AECAC17E1`;
all affected pages pass serialized visual QA. No XeLaTeX process or `Q:`
mapping remains.

Exact next cursor: append directly from NUMDAM PDF one-based p.124 / printed
p.125, continuing the proof of Proposition 4.3.1 after `la restriction de
$\alpha\times_S\beta$`. Do not remove any closing environment first.

## Successor checkpoint: printed p.125 complete

The earlier p.125 cursor is superseded. Diplomatic French is admitted through
the exact terminal phrase `qui s'accorde avec celle introduite` in the
inverse-image terminology following Proposition 4.4.1.
`source/ega1/ega1-4-fr.tex` is 27,679 bytes / 522 lines / SHA-256
`E26B5510C2DF88911C36C57755D6D5AAF6EF23174C9B30DA70BB95FC6A955FA2`.
No temporary final environment close is present. One inverse suffix
truncation restores the p.124 file exactly at 23,239 bytes / SHA-256
`E9061031DB90102A99851D0397A879CCF422F50A820F8C2A30AF30E222CC9185`.
French source corrections, new p.125 printed-source errors, and unresolved
readings are zero.

The paired English recheck changes no source byte. R55 is the active complete
127-file gate: 7,280,872 bytes, manifest 41,158 bytes / SHA-256
`2C76ACD405EDA12EF0D89A89FFF7388410B770F4940C9F55EC8476859218E165`,
tree SHA-256
`E8331E55DEABD57007298B17012BE1E50C20370837535F413F3679EBE3FB646B`,
and PASS/errors-empty zero-delta validation 7,453 bytes / SHA-256
`38C475CFA262D891E3747AFF0FF517E3E81602ADBFA733131602F30B6F412A31`.

R48 validation is PASS/errors empty at 10,341 bytes / SHA-256
`0B5B2C235F4E2166F5A15F084A4B8FC9592EA7426D2CB663EB916DBDAD9CA1F0`.
Final bounded PDFs are French 32 pages / 307,609 bytes / SHA-256
`859CFDB406BE148825CE270EC587A01C90490B2434A371BF8F36E1C45A2CBF9E`
and English 18 pages / 150,482 bytes / SHA-256
`27703818224457A02D4AB5C0C69B919FAE515324520F7A40293FEEB08130996E`;
all affected pages pass serialized visual QA. No XeLaTeX process or `Q:`
mapping remains.

Exact next cursor: append directly from NUMDAM PDF one-based p.125 / printed
p.126, continuing the inverse-image terminology after `qui s'accorde avec
celle introduite`. Do not remove any closing environment first.

## Successor checkpoint: printed p.126 complete

The earlier p.126 cursor is superseded. Diplomatic French is admitted through
the exact terminal phrase `un isomorphisme local en` in Definition 4.5.2.
`source/ega1/ega1-4-fr.tex` is 31,712 bytes / 619 lines / SHA-256
`96BA0D70ADCFA3758DEBB25113B8AE0CA71CCC8D4CE12C1FBBFA8CECBF75D1A7`.
Its final `\end{definition}` is temporary. One inverse suffix truncation
restores p.125 exactly at 27,679 bytes / SHA-256
`E26B5510C2DF88911C36C57755D6D5AAF6EF23174C9B30DA70BB95FC6A955FA2`.

French preserves one new official printed mathematical error in 4.4.5:
`B est une A-algèbre` is incompatible with the displayed tensor product
over (B). English retains the visible list-II correction to (A) being a
(B)-algebra. The paired recheck also repairs one inherited English omission
in 4.4.6 by restoring the factor `\sh{O}_X`. English `ega1-4.tex` is
33,373 bytes / SHA-256
`CE8036FF9EF584DD794C7D4925EA62FE7937229E57212873B1C25DE68F8715A5`.

R57 is the active complete English gate: 127 files / 7,280,880 bytes,
manifest 41,920 bytes / SHA-256
`A8C6D3E4AA6E478CBFCD1A144C6460D9DF03195C09758C713C9CC4C0048739A1`,
tree SHA-256
`C22FBDE03D3833584E83A448F5BB74B51399798C4B1E1C82769659211DCAE1E2`,
and PASS exact one-row diff validation 8,647 bytes / SHA-256
`421DC3016B112F2CD3E1CA92A3E7C76E4FA438B44C83B05C98CD280048C251B5`.

R49 validation is PASS/errors empty at 12,000 bytes / SHA-256
`98501091AB4641EEAFB20F2FFC7E25225189C2A2784E3EDE0AEA7773F1E19DE9`.
Final bounded PDFs are French 33 pages / 313,109 bytes / SHA-256
`E9E0486B63CAD646E6C961B6435919FFA00C47A2022C30A5668757FA4F1EBB8A`
and repaired English 19 pages / 156,047 bytes / SHA-256
`D3B4CA5FC24BE58C62C3E602953E6FE78AF20B7AA7B39834364228DD6AD5E534`;
all affected pages pass serialized visual QA. No XeLaTeX process or `Q:`
mapping remains.

Exact next cursor: remove only the temporary final `\end{definition}`,
then continue Definition 4.5.2 from direct NUMDAM PDF one-based p.126 /
printed p.127 authority after `un isomorphisme local en`.

## Successor checkpoint: printed p.127 complete

The earlier p.127 cursor is superseded. Diplomatic French is admitted through
the exact terminal words `de B.` in Proposition 5.1.1. Section 4 is complete.
`source/ega1/ega1-4-fr.tex` is 34,793 bytes / 682 lines / SHA-256
`9775A6A8EA2AC2415CCE4DC64EEA356382ECED4F06C59FB67C602C6C7ED6F0C1`;
new `source/ega1/ega1-5-fr.tex` is 681 bytes / 17 lines / SHA-256
`E4893706A6EFAEB40D74BECC0FFA3C7E32A1FB3FCA64374CC4B6F9EDCD17163C`.
The two-operation inverse restores the exact p.126 `ega1-4-fr.tex` and removes
the p.127-new file from the predecessor set. No temporary environment close
is present.

Canonical French preserves two printed defects in 4.5.5: the transitivity
citation `(4.2.4)` instead of typed target `(4.2.5)`, and use of `z,z'`
without their introduction. English retains the typed citation and necessary
point introduction with two immediate translator footnotes. Removing those
two unique notes reproduces the exact R58 English source. Current English
`ega1-4.tex` is 33,644 bytes / SHA-256
`C933CDFEB1C7F64B0BFFB8D510A732349B196E3E53B8044A70098D999CAB1BF8`.

R59 is the active complete English gate: 127 files / 7,281,151 bytes,
manifest 42,723 bytes / SHA-256
`3D874D60FA7AB1CE4C0A0496BD20C3B096481E0A35463D851ACD295CCBD08569`,
ordinal tree SHA-256
`BF73FCED73F50B5A18F310A4206EC14955E1DC8512BD50DC6847BCE60A19005D`,
and PASS one-row diff validation 7,763 bytes / SHA-256
`C68E010B34CF050695FCDC5AC8A1AC5F405A4AC05661A0558979214547426C73`.

R50 validation is PASS/errors empty at 11,010 bytes / SHA-256
`D631DC20C4EF98C822AA61FF29A02176382A23E40077C1D36338FE359E80EA25`.
Source-current bounded PDFs are French 34 pages / 317,866 bytes / SHA-256
`CF636F3492F8B81E34BD5E4417393071F3910EDE1AEEA0CDAFB627179606F25E`
and English 19 pages / 161,909 bytes / SHA-256
`E344A519B0DDC19DF372296FA1829FBBCAE0BEC68EDDE4FD0A60BCB60A938BD6`;
the affected pages pass serialized visual QA and both English notes are
visible. The p.127 pre-Stacks block is current at SHA-256
`5DD244CCB3A223D0EEDB67E233027A1A338ACD24232C7639023723F8B98BACBC`.
No XeLaTeX process or `Q:` mapping remains.

Exact next cursor: append directly to `source/ega1/ega1-5-fr.tex` from NUMDAM
PDF one-based p.127 / printed p.128, beginning the proof of Proposition 5.1.1.
Do not remove a closing environment first.
