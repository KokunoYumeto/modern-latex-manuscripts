# Logbook

## 2026-08-02 — successor opened from the frozen global reader

- Copied the complete 127-file editable source tree from the frozen
  `EGA_English_Global_0_IV_complete_linked_reader_20260801_r1` package into
  this no-overwrite working root. No predecessor file was edited.
- Applied the three individually reasoned decisions
  `EG-EGA-I-P69-742-NHK-MISSING-M-EN-001`,
  `EG-EGA-I-P69-743-742-VS-724-XREF-EN-001`, and
  `EG-EGA-I-P69-744-PRECEDING-JUSTIFICATION-OMISSION-EN-001` to
  `source/ega0/ega0-7.tex`.
- These changes were decided by direct comparison with NUMDAM EGA I printed
  page 69 at 5000-dpi detail. They are inherited English-reader defects, not
  reversals of an admitted lead source correction.
- The workspace search found seven copies of each inherited wording, including
  frozen publication candidates, historical working trees, and an external
  comparison lineage. Those historical/frozen trees remain unchanged. This
  successor is the controlling repair surface; a later exact integration must
  replace the active standalone/global deliverables and prove the obsolete
  readings absent from the final source closure.
- No build, publication claim, or archive action has yet been made from this
  successor.

## 2026-08-02 — exact diff replay and validator supersession

- Exact tree comparison confirms 127 predecessor files, 127 successor files,
  and one changed file only: `source/ega0/ega0-7.tex`. The predecessor and
  successor source-tree digests are respectively
  `AF8C65ECE68B1226FB79CAD68DC6587D1F7D21CEF1F78EC7D09C1F795A741E6B`
  and
  `E515BD84DFC325585EBDE71CE8031E35B03E4BF6F5338DAEFED834AB92F172E7`.
- The first diff validator falsely reported FAIL because it counted a generic
  cross-reference target rather than the complete repaired Corollary sentence.
  It found two valid `0.7.4.2` uses and incorrectly expected one. The record is
  preserved byte-for-byte at 849 bytes / SHA-256
  `CC93AAC01C58349764783D1E298C5E43EC2D3F8772F9F73AA46BD466C951392C`.
  This was a lead-authored validator assertion error, caught on immediate exact
  replay; it did not affect the mathematical source.
- The no-overwrite R2 validator binds the complete Corollary 7.4.3 sentence
  and exact formula instead of the generic target. It is 1,588 bytes / SHA-256
  `CCD7E96E872A65E36CEF6F7CF6F8B2436CE4332DD1865DA81CE0AA17809FEA9F`,
  status `PASS_SOURCE_SUCCESSOR_DIFF`, errors empty.
- The three repair-state transitions are recorded append-only in the French
  canon's
  `controls/ENGLISH_CORRECTION_REPAIR_APPLICATION_20260802.jsonl`, three
  records / 2,760 bytes / SHA-256
  `3F12C0504D7A24802A18DBA525F7395FB63F6E87F8C632B8230825713FEE459A`.
  They are applied in this complete editable source successor but remain held
  for global build, reference-coordinate replay, privacy-clean projection, and
  public supersession.

## 2026-08-02 — EGA I 7.5.1--7.5.3 source replay and p.70 repair batch

- Compared the complete English 7.5.1--7.5.3 passage against the diplomatic
  French transcription and direct NUMDAM authority images. The authority
  surface includes five overlapping direct 5,000-dpi bands and a targeted
  9,000-dpi formula crop; OCR/extracted text was locator material only.
- Applied five additional inherited English repairs to
  `source/ega0/ega0-7.tex`: `compliments` to `complements`; missing subscript
  in `A/\mathfrak J_\lambda`; missing definite article before the unique
  coefficient; `is remains` to `it remains`; and `characterize` to
  `characterizes`. Each decision has its own source-bound rationale in
  `ENGLISH_CORRECTION_RECHECK_APPEND_P70_20260802.jsonl` in the French canon.
- Confirmed one deliberate no-edit normalization. The direct 9,000-dpi crop
  visibly shows a lone unmatched opening square bracket in the second 7.5.2
  display. The diplomatic French TeX preserves it. The existing English
  formula omits it because it has no closing mate or grouping role; decision
  `EG-EGA-I-P70-752-STRAY-OPEN-BRACKET-SRC-001` records that rationale.
- The resulting current source is 75,196 bytes / SHA-256
  `1E33F146B32D3EDEEF978DE63A9FB06F856E027D02F0C8BDD7F49B4482C96CE5`.
  Exact comparison against the frozen predecessor finds 127 files on each
  side and exactly one changed file, `ega0/ega0-7.tex`.
- The five p.70 repair applications are preserved in
  `ENGLISH_CORRECTION_REPAIR_APPLICATION_P70_20260802.jsonl`, five records /
  4,362 bytes / SHA-256
  `739A28F3C6E989BCA2E999BABA73CC019E05BFDA6F3D97DBC0598D5FA271F421`.

## 2026-08-02 — source-manifest canonicalization failures and exact R4 rebind

- The R2 source manifest was wrong: an ordered-dictionary implementation
  yielded a null total and failed to implement the declared path ordering.
  It is preserved at 23,157 bytes / SHA-256
  `46004287EF4E97F288487258E09231F7545BFE338D45349EC46D33048A718097`.
- R3 repaired all 127 rows and the total, but made a subtler lead-authored
  mistake: it stated ordinal path ordering while hashing JSON/list order.
  Archive maintenance caught this by independent Python and PowerShell
  replays. All R3 rows were exact, but its aggregate `A6BBB177...` did not
  implement its own schema. R3 is preserved at 23,434 bytes / SHA-256
  `8D34B9C811699BF1844412D714FA77E69187E426E71E6549D77528DABBDD5E5D`.
  This was a control-plane error and changed no English or French source byte.
- R4 is the current exact manifest: 127 rows / 7,279,784 bytes, 23,160 bytes /
  SHA-256
  `E2D57DA04123015CA761E081142152EB4DF60029A914C94B3E4C89C180F81FD0`.
  Its Unicode-code-point ordinal order begins with
  `EGA4_reference_v2_links.tex`; the canonical aggregate independently replays
  exactly as
  `0E7BBF54FB4C5EC7C6EE5660909351A8788D7581F0DA8AAFB6C991D2CE490CAD`.
- The current source-diff gate is
  `controls/SOURCE_DIFF_VALIDATION_R4.json`, 3,893 bytes / SHA-256
  `C20119C23B354AE4EB56E0EB22F9C9DECF5F356235FA433EFCC7F21514BEEEC4`,
  with errors empty. Its independent replay is 1,824 bytes / SHA-256
  `2DA2C5DBDBE07C8FD923DFA27BE882F83A3F0A53210B0271B75FF679C47CB6FA`.
  All eight applied repairs occur exactly once in their bound context; every
  obsolete reading occurs zero times.
- The R3-to-R4 validation transition is append-only in the French-canon file
  `ENGLISH_REPAIR_VALIDATION_SUPERSESSION_P70_20260802.jsonl`, 1,588 bytes /
  SHA-256
  `C57BB7E0C71ED5ECCDF3FC0B5B3D779E17E374611CFA38147FDC188D0E3E41EC`.
  Global rebuild, reference-coordinate replay, privacy projection, package,
  archive handoff, and dual-DOI logbook deposit remain held.

## 2026-08-02 — EGA I Proposition 7.5.4 repair batch and R5 source gate

- Compared Proposition 7.5.4 line by line against direct 5,000-dpi NUMDAM
  crops spanning printed pp.70--71. Four inherited English defects were found;
  none is a correction of the French author:
  - the kernel defining `\mathfrak J'_i` named unprimed `u_{0i}` instead of the
    induced polynomial-ring map `u'_{0i}`;
  - the later kernel claim similarly named `u_{ij}` instead of `u'_{ij}`;
  - the final monomial argument used `\mathfrak J'_i` where the authority
    explicitly uses `\mathfrak J'_j`, the ideal in `A'_j`; and
  - the conclusion misspelled `Noetherian` as `Notherian`.
- The four individual rationales are in the French-canon file
  `ENGLISH_CORRECTION_RECHECK_APPEND_P71_20260802.jsonl`, 4 records / 5,116
  bytes / SHA-256
  `99CF1649C8AB3128F57192C7D759907D6398DDEB071BDF8F232571A5C986518C`.
  All four repairs are applied to the sole changed source file, now 75,199
  bytes / SHA-256
  `8DD6840E73ADBE9D529AE39979B495BB7BC2D4CAFC8DE72C2F2EA870E46D1528`.
- Repair-state events are append-only in
  `ENGLISH_CORRECTION_REPAIR_APPLICATION_P71_20260802.jsonl`, four records /
  3,424 bytes / SHA-256
  `E174622ECF18029DF74D0B2022D9DDD79B1C2C96A6BF33B6F7972A000FE3FDB0`.
  The R4-to-R5 validation transition is separately recorded in
  `ENGLISH_REPAIR_VALIDATION_SUPERSESSION_P71_20260802.jsonl`, 1,293 bytes /
  SHA-256
  `EA68A38E2E9DE87E0045CF4D4E5BD34628D9DAA00032B46C091F54028ABCDC5A`.
- Generated R5 with the already-correct ordinal canonicalization. Independent
  Python replay confirms 127/127 exact source rows, 7,279,787 bytes, ordinal
  first path `EGA4_reference_v2_links.tex`, and exact aggregate
  `30E8197C89FCE61EEB9ACAC82EE40985CB7C1B8F277FE627181B9C4195A8DCDA`,
  errors empty. Manifest identity: 24,084 bytes / SHA-256
  `38E8BD3642A7CBDE07428D9D13447A75DBFD6AAEE0A8B2B682B9F989DEEDB61C`.
- The current diff validation is 4,489 bytes / SHA-256
  `F0987DB31A57930111FD97A551DC379E6D68AA5701FC93673E0C229FC5B3956E`;
  its replay is 2,138 bytes / SHA-256
  `F8E9B03EE5FE51A51C3EEB4BD2105692A599E383681F4F7A5CDB915388BB4108`.
  All twelve repaired readings are exact and all bound obsolete readings are
  absent. Global rebuild and all release gates remain pending.

## 2026-08-02 — direct French replay through 7.6.3 / R6

- Replayed Proposition 7.5.5 and §7.6.1--7.6.3 personally against seven
  direct NUMDAM 5,000-dpi bands spanning printed pp.71--72. Authority manifest
  in the French-canon root: 3,483 bytes / SHA-256
  668DF770147CA68EC7EEA4D8A06D7B06BFBB9E684AAEFF85AA4427FBC4B4CA24.
- Applied five individually justified inherited-English repairs:
  Notherian→Noetherian; making B and A-algebra→making B an A-algebra; repair
  of the malformed quotient parenthesis/clause; this→thus; and restoration of
  the omitted formula ker(v_lambda)=S^{-1}J_lambda before the assertion that
  v_lambda is surjective.
- Recorded three source-faithful no-edit decisions: preserve the printed
  B_n=B_m/J^{n+1}B_m transition formula; use idiomatic English on A for the
  French restriction phrase dans A; and use separated completion for the
  standard term séparé complété.
- The eight-row authority decision file is 10,398 bytes / SHA-256
  502D5089998CE3BE4D69237730C99FE89F803FE3FED70CAEE521041DBA01F700.
  The five repair-state events are 4,314 bytes / SHA-256
  55655CBB9E63D509534923F04A35E9171B2F0DEFB79557515973A32FB8EDE513.
- Current ega0-7.tex is 75,260 bytes / SHA-256
  C576296A78A1303323C7296A7CCF9B989FCA8FF7C2C8A981140F66651B17A747.
  No other source input differs from the frozen predecessor.
- Generated R6 from a checked-in deterministic manifest builder. R6 has
  127/127 exact rows / 7,279,848 bytes and ordinal tree SHA-256
  0B11488A0F866FBF0AF5575AF6E6F77B322C08969BD9034821210EF2F47A00A7.
  Python and PowerShell ordinal implementations agree exactly. Manifest:
  23,692 bytes / SHA-256
  C47C6AAD610A7FF3A15A54C5E3931C2E1E28A2D237D3D4D26FD845947C523B35.
- R6 source-diff validation is 4,058 bytes / SHA-256
  9C210905CE159FED2B4CA6745CD5AAF3CC5F039502DC04FAD6805A44B7D34311,
  PASS/errors empty. Replay is 1,356 bytes / SHA-256
  23BB830C291DC10C349DC825A49FE41F2F78F271D746E528F0FD6863C3C64D11,
  PASS/errors empty.
- No global build was triggered for this small source batch. That deliberate
  hold avoids repeatedly rebuilding the 651-page reader during the pagewise
  French replay. The final/global build, reference-coordinate replay,
  privacy-clean projection, package/archive handoff, rights/caveat closure,
  dual-DOI logbook binding, and public readback remain pending.

## 2026-08-02 — EGA I printed p.92 source recheck

- Direct NUMDAM comparison found two inherited English defects. Line 767 now
  repeats `from` after `as well as`, matching source `ainsi que de`. Line 768
  now says to establish quasi-coherence and *then conclude in the same way*;
  previously its commas attached “in a similar way” to the wrong proof step.
  Both rows record lead error and preserve all formulas and targets.
- Seven retained rows separately justify the proof-environment marker for
  `C.Q.F.D.`, marker typography, verified reference-kind words, heading idiom
  and punctuation, module/algebra capitalization, logical-present proof tense,
  and English capitalization of `Noetherian`. Ledger: nine rows / 6,778 bytes /
  SHA-256
  `A12D4F80F39AD47269CA79400EBE3B8CCF5DE8C11FE5D21BE85B665A45722A89`.
- English R21 is 78,943 bytes / SHA-256
  `E79237CB465C8F0EF7C3FE573F568C4FCD122DC5D618463C46B914DE218459F9`.
  Two exact inverse substitutions reproduce R20 SHA-256
  `776A8D8FB7B5ACA95CC45F939C8BF11E5CF45B00709BC281F9FFB007C58A86A9`.
- R21 manifest: 127 files / 7,280,266 bytes / tree SHA-256
  `870E97EB71F44AA795F47332B655738011DB772C226899E1FFDE66A3741A4B82`;
  manifest SHA-256
  `DA77D11422EEB0CD94709729824171B1D9B33A1C7B71E5BBE68C9CAF9679717A`.
  Exact ordinal and inverse replays pass. No English global build or render ran.

## 2026-08-02 — EGA I printed pp.73--74 French recheck

- Personally compared the complete admitted range against direct NUMDAM
  5,000-dpi bands. P73 manifest: 3,354 bytes / SHA-256
  8DCD975AEC1239EC200674C02ABB201C39377A0FE3848B56BBD8CDBB7B6F9849.
  P74 manifest: 2,650 bytes / SHA-256
  0C4CEC360787E787DB968EB8CAF6DB919BC9BAFF572790DF8843EC35B9EAC7B4.
- Applied four individually justified p.73 English repairs: two mistranslated
  adherence conditions, singular agreement for the couple, and the correct
  scope of invertible elements in the universal property. Decision SHA-256
  E1438205B716BF612974FDDCB0E996DB69F08084FB30B0AE951839BF4F6D6E48;
  repair-event SHA-256
  BAFB5569FED2135065F3807BF0FCE094886F14723A3B18C9536E13BDC125680B.
- Applied two p.74 dispositions. The inherited English omitted the exponent
  marker in S^{-1}J. The printed French also closes the proof of Proposition
  7.6.11 by naming “proposition (7.2.8),” although 7.2.8 is an earlier
  corollary. French remains exact; English now names Proposition 7.6.11 and
  exposes the printed locator in an immediate footnote. Decision SHA-256
  3F6280B1A1ED8E663597081ABC0F23FBEEDA199D348369CFC1E22F39F746F41B;
  repair-event SHA-256
  F3A407E38723F125B98DB9DD147BA04757C07E756F82ABE2E60ACC603C4E2CD0.
- Current ega0-7.tex is 75,427 bytes / SHA-256
  3A7611B105182E45AA33C945C85E34A48A2C46369568A686F7E6F73810D54AA7.
  No other source input differs from the frozen predecessor.
- R8 has 127/127 exact rows / 7,280,015 bytes and ordinal tree SHA-256
  7A0E4D9FB6A352C04009029A692E3E9D133015ECBFBBF52005BEF95F0A6B5F1A.
  Python and PowerShell ordinal implementations agree exactly. Manifest:
  24,222 bytes / SHA-256
  6087C82E314965389977E80D4E964EBB47AA2A205D699B1160B5455FB21AE851.
- R8 diff validation is 5,055 bytes / SHA-256
  33F169EA742114018CA857D6391CEE89ECD9ABDB92B77AE79952EBC6D1731C32,
  PASS/errors empty. Replay is 1,481 bytes / SHA-256
  0B6D72131B9918330D525A4932841A4D6244A709D4DFE4A88F9DB782E05D843C,
  PASS/errors empty. All 26 cumulative source assertions replay.
- No global reader build was triggered for this pagewise source batch. The
  final/global build, reference-coordinate replay, privacy-clean projection,
  package/archive handoff, rights/caveat closure, dual-DOI logbook binding,
  and public readback remain pending.

## 2026-08-02 — EGA I printed p.94 English recheck / R23

- Direct NUMDAM comparison identified two inherited English register defects.
  `For purposes of abbreviation, we write ... we put` is now the concise,
  source-aligned `For brevity, put ... also put`, preserving the two definitions
  and the repetition in `posons ... posons encore`. `We note that, in a precise
  way ... can be considered as` is now idiomatic mathematical English: `More
  precisely ... may be regarded as`. The homomorphism and restriction-of-scalars
  structures are unchanged.
- Six retained decisions are logged individually rather than silently treated
  as obvious: native-square fidelity; hash-to-sharp glyph modernization;
  capitalization; semantic environments; visible-equivalent tilde/isomorphism
  macros; and display punctuation/clickable-reference treatment. Decision
  ledger: eight rows / 6,931 bytes / SHA-256
  `DCCDA3F1B7B9DB60D19903ED0EE20E24B4E88A369FE2D63EA206E5B78EAF32C7`.
- The first draft ledger had two stale applied-edit line locators and three
  approximate retained ranges. Final-source replay corrected these before
  admission; this lead documentation error is itself recorded in the workflow
  ledger rather than hidden.
- Current source: 78,882 bytes / 1,267 lines / SHA-256
  `3839AC1B392AA3B7629B06909D1DAC19AF652963B01D556D1889B1C9ECAB8414`.
  Two inverse substitutions reproduce exact R22. R23: 127 rows / 7,280,205
  bytes / ordinal tree SHA-256
  `BB9926BFC40EB87CF106CDDACDDB834F99FF4B78CE99E0C3C3F8F32D638B5419`;
  manifest SHA-256
  `3D744079A8F05F4526BD2446B6636D487D2D258B93722F1861D810BF6408D06A`.
  Section/full validation SHA-256 values are
  `2E02BFF6F5B0725B629A7CA4E98B8C22CA49A1F4440627BCD62D2DC8DD906089`
  and
  `6D474E302F830412894BC3A394E631ED5A78BC220FFEBCD2DF45080A0BC7E2BC`,
  both PASS/errors empty.
- No global reader build or English render ran. Global build, reference and
  pre-Stacks coordinates, privacy-clean projection, rights/package closure,
  archive handoff/readback, and dual-DOI logbook custody remain pending.

## 2026-08-02 — EGA I printed p.95 English recheck / R24

- Direct NUMDAM comparison found seven inherited English defects. Six are
  prose/register issues: two literal constructions in the deduction sentence,
  inverted correspondence word order, two misplaced `respectively` markers,
  and an unjustified past perfect. Each is separately logged and justified.
- The seventh is mathematical. The authority prints (h_x(s'_{x'}\otimes
  t_x)=t_x\cdot s_x). The inherited English TeX had the prime after
  (s_x), omitting the prime on the point index and thereby obscuring or
  changing the stalk. The source now explicitly has (s'_{x'}). This is
  counted as a lead error and formula correction, not copyediting.
- Three localized module/ring expressions were also changed to put the prime
  on the base symbol before its subscript. That change is visible-equivalent
  and is logged as source-order normalization, not mathematical correction.
- Six retained decisions record stalk terminology, hash-to-sharp notation,
  English capitalization, semantic environments, visible-equivalent project
  macros, and the exact visible locator `0, 4.4.3.2` held for the stabilized
  cumulative reference/pre-Stacks pass.
- Decision ledger: fourteen rows / 11,105 bytes / SHA-256
  `905745E09BAC102CE4B799081490DB9647AE28D5BE0AE3707D6BECFB4C85BD8D`.
  Seven rows explicitly mark prior lead errors; one is mathematical.
- Current source: 78,891 bytes / 1,266 lines / SHA-256
  `3C1A38B22A9A07315A8CFA2E8F3AC1B65232E0CFCE3F9F8E2E09A30464018617`.
  Eight inverse substitutions reproduce R23. R24: 127 rows / 7,280,214
  bytes / ordinal tree SHA-256
  `099CD37D1BD2E8380DF875A90C61895F7B7BFF743573A4CF5452B22D3AEE5A56`;
  manifest SHA-256
  `EBA2F1067D485CCD4861EAFEC7F1239C55CA5858E1734714FA91667805E37E3E`.
  Section/full validation SHA-256 values are
  `865A67A3ADAAE8D2C380E5087200BE4E904E9F9699600DB16182BBA7485EAFF0`
  and
  `D53AED014E05339D9BB7106A60D15CC150C257325A6B9A6D93350D729980AA0A`,
  both PASS/errors empty.
- No global reader build or English render ran. Global build, reference and
  pre-Stacks coordinates, privacy-clean projection, rights/package closure,
  archive handoff/readback, and dual-DOI logbook custody remain pending.

## Printed p.93 recheck — R22

Three inherited English prose/register defects were repaired against the
direct NUMDAM authority. `remarquons déjà` now introduces the current step as
`first note` rather than adding the unsupported clause `we have previously
seen`; singular $M_\lambda$ now `ranges over` rather than `run over`; and the
ordered ring identifications place `respectively` naturally while removing a
doubled space. No formula, object, proof dependency, or reference target
changed.

Six retained differences are documented individually: logical-marker house
style, Noetherian capitalization, proof-environment closure, semantic
corollary/reference structure, English heading idiom/punctuation, and
visible-equivalent project TeX macros. The complete nine-row ledger is 7,782
bytes / SHA-256
`211B3C3A460DB008F6E01ECE0D6444448053525A42A816B86069515D7F63D54E`;
three rows explicitly record `lead_was_wrong:true`.

Current English source is 78,920 bytes / SHA-256
`08B58F1484E0195D637512C27528BF77F665DCE03D1B3C4F29A7FC685A956E5E`.
Three exact inverse substitutions reproduce R21 byte-for-byte. R22 has 127
rows / 7,280,243 bytes / ordinal tree SHA-256
`4B01E8D9D30053F942E2570915BB92365BC754DA5A95ABA6C0AB8BA2DF9329B3`;
manifest SHA-256
`4B2C325B73D8DCF3027A5A6BE0FEB651AD6477200E71E33916E91399CD9262F8`.
Section/full validation SHA-256 values are
`92DAB4E502B3D03E863F764B026301016E17CFDE769DD29C5E9E9C1E5D745B0F`
and
`24D47EAD70C2AC404F7F85D0C1DCA7D9962291579B58785897855ECE91A71276`,
both PASS/errors empty. No global English build was run for these prose-only
edits; cumulative build/reference/pre-Stacks/privacy/package gates remain
held during diplomatic French production.

## 2026-08-02 — EGA I printed pp.88--91 source-recheck catch-up

- P.88 changed no English byte. Its three retained choices separately justify
  the composite-tilde macro, sheaf-Hom macro, and verified kind words before
  existing linked targets. P.89 repaired the invented `(a)/(b)` replacement
  of printed `1^\circ/2^\circ` and restored two lower arrow-label sides;
  all three are lead errors. P.90 retained five documented choices, including
  a source-typo correction that distinguishes module $N$ from sheaf
  $\widetilde N$ while diplomatic French preserves the printed oddity.
- On p.91, `To finish the proof, that...` was ungrammatical and now reads `To
  finish proving that...`; `It is evident for (d1)` now reads `This is clear
  for (d1)`. These are two translation-prose repairs, not corrections of the
  mathematics or French author. Four retained rows justify list-marker style,
  verified reference-kind words, the conventional present tense for `il
  suffira`, and the script-sheaf macro. Ledger: six rows / 4,740 bytes /
  SHA-256
  `4ADAD1B6997F3B699E36BF7F95E33D6F0FA68D7483FB5D1406C73EB190612510`.
- Current English source is 78,945 bytes / SHA-256
  `776A8D8FB7B5ACA95CC45F939C8BF11E5CF45B00709BC281F9FFB007C58A86A9`.
  Two exact inverse substitutions reproduce R19 SHA-256
  `755474860ACB423698A25393EB56CE06396F321131B7EACBBF2624478089BDC5`.
- R20 manifest: 127 files / 7,280,268 bytes / tree SHA-256
  `1C39A53AA1AFE22E39606C93EADB7FBE6C0D0705AE43C35C9D6DBD345DDFE5AD`;
  manifest SHA-256
  `864B73E7553E086F64D7AD32B4DD8494823505E3956A28DBED39EFBB8EA990D5`.
  Explicit ordinal replay and both inverse-replay validations pass with no
  errors. No English global build or render was triggered.
- The complete rationale remains in page-specific JSONL rather than being
  compressed into an unexplained edit count. Final/global build, coordinate
  replay, privacy-clean projection, package/archive handoff, rights/caveat,
  dual-DOI logbook binding, and public readback remain pending.

## 2026-08-02 — EGA I printed p.89 source-fidelity replay

- Direct NUMDAM inspection found three inherited English deviations in
  1.3.13. The source's conditions `1^\circ/2^\circ` had been silently changed
  to `(a)/(b)`, and the lower `\varphi` and `\psi` diagram labels had been
  placed above rather than below their arrows. All three are now corrected.
- Each decision has an individual rationale and `lead_was_wrong:true` in
  `ENGLISH_CORRECTION_RECHECK_APPEND_P89_20260802.jsonl`, three rows / 3,633
  bytes / SHA-256
  `38712B6F457B308FD650DDD19537321207EF7D256BDCD2622535EF1BC90D99C9`.
  These are structural/diagram-fidelity repairs with no mathematical effect.
- Current `source/ega1/ega1-1.tex`: 78,948 bytes / 1,267 lines / SHA-256
  `755474860ACB423698A25393EB56CE06396F321131B7EACBBF2624478089BDC5`.
  Four unique reverse substitutions reconstruct exact R18 SHA-256
  `8C3145A4A41947759A191809C582163EF9FB590FBE9DC92211D719F205877D49`.
- R19 manifest: 127 files / 7,280,271 bytes / ordinal tree SHA-256
  `FD8D86B665DACA629F4FE1ED320D15EF2BFA25A751B8527905C85457C78998C7`;
  manifest SHA-256
  `8A2618EE6EB0A895A6DE54B83A30F165D901504410CCB89177047325DAA59F80`.
  Section/full validations are respectively SHA-256
  `B564E6300F6EADA968A87DDCDE254D9520F1FCE32C9BF52F9C4D20B140C28946`
  and `BD9853BCE7A0FD3BDFAF7B7B3F606798EFA5C1F0105C5F9A6F31926F62BF13BA`,
  PASS/errors empty.
- No global English build or render was triggered. Global build,
  reference/pre-Stacks coordinates, privacy-clean projection, package/archive
  handoff, rights/caveat closure, dual-DOI logbook binding, and readback remain
  pending while diplomatic French work continues pagewise.

## 2026-08-02 — EGA I printed p.90 no-mutation source replay

- The direct p.90 crop confirms that French literally prints the inconsistent
  phrase `au faisceau associé au module \widetilde N, conoyau...`. The English
  correctly identifies N as the module cokernel and \widetilde N as its
  associated sheaf. That correction is retained and individually justified;
  diplomatic French remains uncorrected.
- Four additional retained choices document idiomatic “over a prime spectrum,”
  English parenthesized condition labels, correct target-kind words before the
  same references, and established tilde/script macros. Complete page ledger:
  five rows / 4,613 bytes / SHA-256
  `A5C0174B7820E383F6FA9B55FFC3D0E2C066C0B4C20CC5FBCE2D29E4DABE66C6`.
- English source remains R19, 78,948 bytes / SHA-256
  `755474860ACB423698A25393EB56CE06396F321131B7EACBBF2624478089BDC5`.
  No-mutation validation: 2,924 bytes / SHA-256
  `95E3671D4EB366F23D6C403B4E9D89D145D4EDBC9904CD3A218C111E142AE1F9`,
  PASS/errors empty. No global English build/render was run; global reference,
  pre-Stacks, privacy, package, rights, archive, and readback gates remain held.

## 2026-08-02 — EGA I printed p.86 English source recheck / R17

- Authority: NUMDAM EGA I PDF SHA-256
  `9ABA23020217535977E279BDD06A0413F48DA703086865BA4C00766C85DF4AE6`,
  PDF one-based p.85 / printed p.86. The personally inspected authority image
  is SHA-256
  `B7BEC3BAC68ACB643C558229D88E4B17F8AB3F2AF3A9DC0BF76B145516DE8B42`.
- Applied `EG-EGA-I-P86-137-RING-HOMOMORPHISM-EN-001`: changed
  `homomorphism of structure rings` to `ring homomorphism`. French has
  `homomorphisme de structure d'anneau`; the inherited plural falsely evokes
  a separate technical object. No mathematical content changes.
- Applied `EG-EGA-I-P86-137-COMMON-MIJ-EN-001`: changed `the m_{ij} are equal
  to the one single m` to `all the m_{ij} are equal to the same integer m`.
  This restores the explicit universal and noun in `tous ... un même entier
  m`; the common-bound argument is unchanged.
- Applied `EG-EGA-I-P86-137-REDUCED-CASE-EN-001`: changed `it remains to
  prove the case where m=0` to `we are reduced to the case where m=0`.
  French `on est ramené` describes the reduction caused by rescaling; it does
  not introduce a separate proposition still awaiting proof.
- These are all explicit corrections of previously accepted lead output, not
  unlogged stylistic polishing. All three ledger rows say
  `lead_was_wrong:true`. No correction is claimed to prove or alter a theorem.
  Decision ledger: three rows / 3,316 bytes / SHA-256
  `47ADE114A1A2161E71166C2BAD84C0E2EAEB06469B1703440524A06A46B456E7`.
- Current `source/ega1/ega1-1.tex` is 78,953 bytes / 1,267 lines / SHA-256
  `26747DCB22FCB736BBD1D025015C81E268F08CE42EB14D98518E4F21EA70DD99`.
  Three unique inverse substitutions reproduce the exact R16 source: 78,962
  bytes / SHA-256
  `87F31A92CE21021768DB10B4C1F39A51992CF9949C61205E599CBD03E2E276AC`.
  Section validation: 3,793 bytes / SHA-256
  `A438CD78B18CAADC9EA051A06CA04D065C74034A27A500B3A6F80384B31A697E`,
  PASS/errors empty.
- R17 manifest: 127 files / 7,280,276 bytes / ordinal tree SHA-256
  `CE854184377B48F388C46D5D4808E0A23A2E168F23909714C7E6F9C10B880DF8`;
  file SHA-256
  `63BA95B4C3C9B2E7C50C5878A523D7C5D032ABBB84C5D2B09AB967E904E78674`.
  Full validation: 2,885 bytes / SHA-256
  `394F541895BE2619FE30D5562F28EA01FD28AF23B923C89B79BFFB9DC89D5D70`,
  PASS/errors empty. An independent .NET ordinal replay matched all rows,
  sizes, hashes, total bytes, and tree hash.
- No global build, English render, OCR, reference replay, packaging, or
  archive action occurred. The production lead worked sequentially with zero
  agents active; the durable maximum remains two or three bounded,
  low-intensity grunt-work agents and no heavy-job swarm.

## 2026-08-02 — EGA I printed p.87 English diagram recheck / R18

- Direct NUMDAM authority, PDF one-based p.86 / printed p.87, shows `w` below
  the lower horizontal arrow in the 1.3.8 square. The reused whole-page image
  has SHA-256
  `3E861071076111EEBB9572225C6EEDBEBB3664DE47E2FEB09C605071793E9AC3`;
  the tight crop from those same bytes has SHA-256
  `B16C7CBE18ECFC564B58298294029CEA3837386FC4B4886255A5F89723B7822C`.
- Applied `EG-EGA-I-P87-138-DIAGRAM-W-LABEL-BELOW-EN-001`: changed
  `M_f\\ar[r]^w & N_f` to `M_f\\ar[r]_w & N_f`. This is a one-character
  strict layout-fidelity repair; nodes, arrows, direction, labels, and
  mathematical meaning are otherwise unchanged. Because the above-arrow
  placement had previously been accepted, the row explicitly records
  `lead_was_wrong:true`.
- Decision ledger: one row / 1,277 bytes / SHA-256
  `B4BC74E1FADA4448F35488502A81EFFA0C883572581F25A3BDEFDA0483E4AB32`.
  Current source: 78,953 bytes / SHA-256
  `8C3145A4A41947759A191809C582163EF9FB590FBE9DC92211D719F205877D49`.
  One unique inverse substitution reconstructs R17 SHA-256
  `26747DCB22FCB736BBD1D025015C81E268F08CE42EB14D98518E4F21EA70DD99`.
- Section validation: 2,722 bytes / SHA-256
  `C5F2A10806376B6DC2D528213D2D3F03221FEA1865E60AE53E8F73244FEAAC82`.
  R18 manifest: 127 files / 7,280,276 bytes / tree SHA-256
  `D2A7BC6831E8F15D10CCE2C52C0D6907937D32DFA2EC5C4BC3779B7936AAC465`;
  manifest SHA-256
  `2355C8043243D22BFA826AE8664D8A3563DA28C60CCB81BD35DD28ABF1D64BCE`;
  full validation SHA-256
  `0FDA5725A45AAF1C21EBA5FCF51684B5FA5E4E1ED2129F7C69AFACFF943192F5`,
  PASS/errors empty.
- No global build, English render, OCR, packaging, or archive action occurred.
  Zero agents were active; the hard maximum remains two or three bounded,
  low-intensity grunt workers without rendering, OCR, or build swarms.

## 2026-08-02 — EGA I printed p.88 English normalization replay

- Direct authority is PDF one-based p.87 / printed p.88, image SHA-256
  `A0269AB9268BF48B6C3B10923F9C31737F56EA9376C6A64567E988C07DA6E67F`.
- Retained the corpus `\supertilde` macro for the same source tildes over
  `N+P`, `N\cap P`, and `M\otimes_A N`; grouping and meaning are unchanged.
- Retained `\shHom_{\widetilde A}` as the established macro spelling of the
  same internal sheaf-Hom functor printed with a script H.
- Retained the added unit-kind words “Theorem” and “Proposition” before the
  source's same references 1.3.7 and 1.3.6; this is linked-reader navigation,
  not a claim that the author printed those words there.
- All three choices have separate stable IDs and rationale in the 3,276-byte
  ledger, SHA-256
  `39E247CAA4BA6F67384FB4EB535D49D2B0ADB6DAC73A3975642F310D8678DE76`.
  No applied change and no newly discovered lead error occurred.
- Current English source remains 78,953 bytes / SHA-256
  `8C3145A4A41947759A191809C582163EF9FB590FBE9DC92211D719F205877D49`.
  R18 remains exact. No-mutation validation: 2,729 bytes / SHA-256
  `C6FF77518A41AD662643CD1F39EF4880FB311B9C88B9FD310A7A93EC76F9960D`,
  PASS/errors empty.
- No global build, English render, OCR, reference replay, packaging, or
  archive action occurred. Zero agents were active; at most two or three
  low-intensity grunt workers may be used, never a heavy-job swarm.

## 2026-08-02 — EGA I printed p.85 English source recheck

- Authority: NUMDAM EGA I physical PDF p.84 / printed p.85. The direct
  2,200-dpi diagram crop proves `u_f` is above the top arrow and `u_g` below
  the bottom arrow, with the two vertical rho labels on opposite outer sides.
- Applied one source-fidelity repair: `M_g\ar[r]^{u_g}` became
  `M_g\ar[r]_{u_g}`. This changes no mathematical content; it restores exact
  label placement. The lead did not previously catch this inherited layout
  miss, but the current source recheck did.
- Retained two justified English choices: `\setmin` is typographic spacing for
  the printed set-minus operation, and “structure sheaf” is standard English
  for *faisceau structural*. Neither changes the author's claim.
- Exact decision ledger: 3 rows / 3,111 bytes / SHA-256
  `5A6AEAE4C1E6445364608FB234174915345D2B54E20E7C62A7BCA66860E8537D`.
  Exact inverse replay reproduces the R15 source SHA-256; section validation
  SHA-256
  `0E9EB76A5A19EA2F6F3A43F395F8C009D420CF15F2D804095F9CBABDEF67FF2E`.
- Current source SHA-256:
  `87F31A92CE21021768DB10B4C1F39A51992CF9949C61205E599CBD03E2E276AC`.
  Complete R16 manifest SHA-256:
  `39D7F529579466028B44E6E6BED9CDB547B4BDC2E4EDCD85783FCF1F8D9B7A34`;
  tree SHA-256:
  `64C5266D3BB6553B6D3B1BBC42DF136042F6A5F83AFF0262CE22DF9500E35C30`;
  full diff validation SHA-256:
  `DEA89BB808D3E6EF8221DE87C5DCA2007A868FD66847F992F1B109008926D28C`.
- No global build or release audit was run. Pagewise French work continues at
  printed p.86 under the sequential/RAM-light/reuse-first rule.

## 2026-08-02 — EGA I printed p.83 / §§1.1.14--1.2.3 recheck

- Direct NUMDAM p.83 review and two genuinely targeted detail checks support
  five recorded decisions. One edit was applied: “it is integral” became “it
  is an integral domain” for `donc est intègre`.
- Four existing choices were retained with individual rationale: “at most one
  generic point”; the explicit name “Jacobson radical”; insertion of the
  necessary `a≠A` omitted by the printed proof sentence; and the modern
  right-to-left composition order used consistently throughout the English
  corpus. The last two are functionally different from the printed French and
  are therefore explicit audit entries, not silent editorial changes.
- Decision ledger: 5 rows / 5,615 bytes / SHA-256
  `D2CE7E4C7FAC883AB1F68902655472B0559C4B40ED7A9C7EC95471A8DF36E9A7`.
  Exact one-edit inverse validation: 1,692 bytes / SHA-256
  `E6810C527CF47F6A6B8C9BFDFF047D1FDE82D97FA4BB1E4DF12395CDBD2FFFF2`;
  it reconstructs the exact R14 source hash.
- Current `ega1-1.tex`: 78,962 bytes / SHA-256
  `1A203AD96C8C8AEF46C5884492B50CAD3E69590CA154ADBA58C4609AEB2A2C1E`.
  R15 exact closure: 127 files / 7,280,285 bytes / tree SHA-256
  `B62B297758730E9DB6D10818DFD815A6BD9F7CE2BD418DECE13D6DA662D4CF0B`;
  manifest SHA-256
  `E9A16CF44BB22B03540A64BDA62F21013D7030DA0B170EC7B66A335A15588108`;
  diff validation SHA-256
  `05B18115426FBB140190E05B1AB7833852F3EAEBF3EDDC5A4A88909EC970DEEE`.
- No global build or English render was run. French pagewise work continues;
  English global/reference/privacy/package/release gates remain held.

## 2026-08-02 — EGA I printed p.84 / §§1.2.4--1.3.3 recheck

- The inherited English source required no new byte change, but three
  functionally relevant differences from the French were individually
  justified rather than passed silently.
- In 1.2.5, French visibly prints `on retrouve (1.1.12)`. Proposition 1.1.11,
  not Corollary 1.1.12, is the arbitrary quotient-spectrum identification;
  English 1.1.11 remains correct.
- In 1.2.6, French uses the historical left-superscript localization map
  `{}^S i_A`; English `i_A^S` denotes the same map under the corpus-wide
  notation policy.
- In the proof of 1.2.7, French visibly prints X/A/A. Since φ:A'→A, its kernel
  is an ideal of A', its vanishing set lies in X'=Spec(A'), and the relevant
  prime ideals/nilradical belong to A'. English X'/A'/A' is therefore the
  uniquely correct source-backed repair.
- Decision ledger: 3 rows / 4,064 bytes / SHA-256
  `67464F6931246807CB6478BBA49E9384E53ECC2399F0100241B14F49D605D20F`.
  No-mutation validation: 1,978 bytes / SHA-256
  `615D7EAABBF75650F9EAFF26D8DD64475CD1615450D31ECCBD6DCC668A6B0C9F`.
  R15 remains exact and current; no global build or English render was run.

## 2026-08-02 — EGA I printed p.80 / §1.1.1 English authority recheck

Direct comparison against the controlling NUMDAM page produced two accepted
changes in `source/ega1/ega1-1.tex`:

- `EG-EGA-I-P80-111-INTEGRAL-DOMAIN-TERMINOLOGY-EN-001`: “the field of
  fractions of the integral ring” became “the fraction field of the integral
  domain.” This is the standard precise rendering of `corps des fractions de
  l'anneau intègre`; it does not alter the assertion.
- `EG-EGA-I-P80-111-RELATIONS-VS-EQUATIONS-EN-001`: “the equations
  $f(x)=0$ and $f\in\mathfrak j_x$” became “the relations ...”. The French
  says `les relations`, and membership is not itself an equation.

One source-reading suspicion was wrong and was caught before mutation:
`EG-EGA-I-P80-111-JX-VS-PX-CANDIDATE-REJECTED-001`. At 1,400-dpi context
resolution the lead suspected `\mathfrak p_x`; one tightly cropped 5,000-dpi
authority image proved the source prints `\mathfrak j_x`, which the inherited
English already had. This batch therefore contains two correct admitted edits,
one self-caught wrong candidate, and zero wrong edits admitted.

Current source: 78,900 bytes / 1,267 lines / SHA-256
`7F3A34C3E03F3497A4BD406E9E7A48ED6EDC72CCDA99768DD516EEF948202C64`.
Decision ledger: three rows / SHA-256
`363742C913D367889348FD4D554B6F53B22AC1ECE859BD9FDD8F83F4F9747A3E`.
The corrected two-edit inverse replay exactly reconstructs the 78,902-byte
predecessor SHA-256
`263C48F2E102980DB1700F57B7CAB6235CFE940656A7873F637EE3C37F8A2D02`;
validation SHA-256
`01CC60CDDA76790566C19EFE18399426CA9CF883765745CDA0DE89161A659D0F`.
The first inverse harness omitted one closing math delimiter, failed without
writing a file, and is retained here as tooling-error history.

Complete R12 source closure: 127 files / 7,280,223 bytes / ordinal tree
SHA-256
`5410571C0C44F559B1474FFFACE408BE3137F71D418FD09F22B70B798A601191`.
Manifest SHA-256
`491EC4E6FD5410C54986400B0CE1B975E502481537E846521CC24B7A20AA15ED`;
complete source/diff validation SHA-256
`3102F963D936C1A15641FF49F9CEF4D61810B8CEE1FFD259A170816A8703447D`,
errors empty. No global build, English render, OCR, agent, or archive action
was used.

## 2026-08-02 — EGA I printed p.81 / §§1.1.3--1.1.9 recheck

Three changes were applied to `source/ega1/ega1-1.tex`: plural
“intersections of prime ideals”; source-exact “the example of a
non-Noetherian integral domain having exactly one prime ideal distinct from
(0)” in place of an inherited universal `any` statement; and the missing
article in “an example of a ring.” Two choices were audited and retained with
explicit rationale: classical `fonctions continues numériques` means
real-valued functions here, and `topologie initiale de Y` means Y's original
given topology rather than a categorical initial-topology construction.

Five-row decision ledger SHA-256:
`51830FA1B2D263DDBDE91380EA04B6C6028D2A6711344A6E8038AAF8A05360D6`.
Exact three-edit inverse replay SHA-256:
`6C46D53DB24F27BA8BEA6474EF39D13A40196E407728F2573DA9FE87D7407E9C`.
Current source: 78,928 bytes / SHA-256
`8413A5B1710F1B932A4F69D8F7E8D501FCE909B0EE9BAC46809F4A3DEE20E221`.
No lead decision was reversed in this batch.

R13 complete source closure is 127 files / 7,280,251 bytes / tree SHA-256
`C73A0D59938FB18E3B9DEC6BB9E1C4BC8033360DA5C1B4F0BD948A9FCED76430`.
Manifest SHA-256
`CC593E9C9D01D8053CF7757DAB745197E9481FF9308DA0C3D2623F25AD7406DF`;
complete diff validation SHA-256
`DA38B1A6554799334D70C5C9EEFB7CF4C9615BC8041CBDBEFAEE289E8FA13030`,
errors empty. No global English build/render, OCR, agent, or archive action was
used.

## 2026-08-02 — EGA I printed p.82 / §§1.1.10--1.1.14 recheck

Three edits were applied. The printed and valid $n\geq0$ was restored in
place of an inherited silent $n>0$ normalization. Both translations of
`anneau intègre` in Proposition 1.1.13 and its proof now use standard
“integral domain.” “Canonically homeomorphic” and “proper closed subsets” were
audited and retained as standard exact equivalents of `isomorphes` for
topological spaces and `distinctes de X`.

Five-row decision ledger SHA-256:
`71711DFF7E0D5C21C8F32EF5A159585B22F61D574C20BBAAA91B4CB634719421`.
Exact three-edit inverse replay SHA-256:
`9096728741F07D4C9DA96C703E7381E53E16FC3B5D56140B029B1AFD2B787887`.
Current source: 78,952 bytes / SHA-256
`B01302DA521F1FE09DBDE748CE5BF50199BD3C8CE6CA0BA21003B27161C65A14`.

R14 complete source closure: 127 files / 7,280,275 bytes / tree SHA-256
`01613437EE956CADF50FE90C8C18CE8E73F2F731E3D1C94398C1410D12175A3D`.
Manifest SHA-256
`27038C5278D96F411B98E72780432BC2663B4923587FECED104ADC9AEE88CE59`;
complete diff validation SHA-256
`2E42656AE40BE12F5EEA3DB21A41602A6B1C4D1C5DE798DA83B990D1AB0BE509`,
errors empty. The initially malformed unsealed JSONL was corrected and all
five rows reparsed before admission; neither TeX source was affected.

## 2026-08-02 — EGA I Chapter I printed p.79 authority recheck

- Direct NUMDAM page authority: EGA-I PDF SHA-256
  `9ABA23020217535977E279BDD06A0413F48DA703086865BA4C00766C85DF4AE6`,
  physical p.78 / printed p.79. The lead inspected one sequential 1,100-dpi
  whole-page image, SHA-256
  `C4CFD1479D83E858F171625D2806B673CFDB4285321D726E7FE81FA14928917C`.
- English file checked: `source/global_volume_ega1.tex`, 2,709 bytes /
  SHA-256
  `895A6D9D4E4977802CF88EF0E108A7E5921D9EF2ECF7DCB16E99645C40B592BE`,
  lines 1--28. Its title, ten-entry summary, orientation paragraph, cited
  authors, section priorities, formal-scheme motivation, and defer-reading
  recommendation agree in substance with the French authority.
- Decision: ordinary English translation and hyperlinking only; no hidden
  correction of the authors and no English source mutation. Exact rationale
  record in the French diplomatic root:
  `controls/ENGLISH_CORRECTION_RECHECK_APPEND_P79_20260802.jsonl`, 1,356 bytes /
  SHA-256
  `5D9E76F96C0008486BD0DD83A9D963885B09431C6C64595158F5C704BD4DEE59`.

## 2026-08-02 — EGA I §7.8 source-authority recheck

Four individually justified repairs were applied to `source/ega0/ega0-7.tex`:
the omitted noun `topology` was restored in 7.8.2; `following proof` was
corrected to source-exact `preceding proof`; `injective` was corrected to
`surjective` at the opening of the 7.8.3 proof; and the final induction's
logical direction was restored so that membership in every power is the
conclusion of the induction rather than its premise. The third and fourth
repairs alter mathematical meaning; the first two repair grammar/discourse
without changing the theorem.

The current source is 75,637 bytes / 1,397 lines / SHA-256
`96983D270206173230D51B70885CB846FD03BB1692D5DFAC03667EE7F4156252`.
The four-row authority decision ledger has SHA-256
`FA9F3D79F64EB856EF919934E44F581D24641719B8ED0662FDB73D472AB23811`;
the four-row repair-event ledger has SHA-256
`BE5F779257515C1705A26FDBF623FE89714E7F0B747A0A6C70A384EBCE96739C`.
`controls/SOURCE_DIFF_VALIDATION_R11_SECTION78.json`, SHA-256
`FEF06E5F4EBBF4A9F5FB4BB2B161471BAC4F127BB9699B397757C8F32605DDE5`,
uses four unique inverse substitutions and reproduces the exact preceding
75,620-byte source SHA-256
`29008BF15E3674F9B84BACDC8168B38E3C2B4B25497B153B2F96C744629749D8`.
No build, render, OCR, reference replay, or archive action was run.

Operational correction: bulk generation/loading of twenty extremely large
5,000-dpi authority bands destabilized the PC and is prohibited. Future image
work is sequential and RAM-light: at most one tightly relevant crop, using
roughly 1,100--1,400 dpi for ordinary context and higher resolution only for
an actually ambiguous small feature. Agents remain permitted only for bounded,
nonduplicative, RAM-light support; source and mathematical adjudication remain
with the lead.

### R11 complete source manifest

`controls/SOURCE_INPUT_SHA256_R11.json` is 25,013 bytes / SHA-256
`BFF25F76B2DD8C58A895D7722F97EF711262757CCD42257AE59807A38F4C6F61`.
It replays 127/127 rows, 7,280,225 bytes, with exact ordinal tree SHA-256
`D3FCAFB187DF2A812ABEB019BBE4AD50E7EB6D143CADF2C51EB357D256E95B13`.
`controls/SOURCE_DIFF_VALIDATION_R11.json` is 2,603 bytes / SHA-256
`F29FF0F856DFCDD9E0491398D0292769250F7C4CD312D555BE9E884A2CF2A12E`,
PASS/errors empty. The initial generator call used the wrong source-root and
wrote no output; the first PowerShell order check used culture sorting and was
superseded by exact `.NET StringComparer.Ordinal` replay. No global build or
release action occurred.

## 2026-08-02 — EGA I §7.7 French replay and English R10

- Direct NUMDAM 5,000-dpi authority review closed printed pp.75--77 through
  Proposition 7.7.8 and proof. Authority manifest: 4,998 bytes / SHA-256
  `6E728F658C5D14E9E36E7D4C069E1AA2F77E6B888CEB3C78C31F12CD2FD3C0E8`.
- Six individually justified English decisions were applied: “If we note” for
  `Si l'on remarque`; “in the category” for `dans la catégorie`; existential
  “an open ideal/such an ideal” rather than a false definite/unique reading;
  one stated uniqueness plus a visible source note for duplicated French `et
  un seul`; topology “on” its carrier; and singular “tensor product.” The
  reference to Corollary 7.3.6 was directly checked and left unchanged.
- Decision ledger: six rows / 9,404 bytes / SHA-256
  `41BF40298FAF27C1B5825A97E18FE2447890C18E682D5188EE7AF699F432413D`.
  Repair events: six rows / 6,517 bytes / SHA-256
  `C0B96FC24F1238951C1872FFE98D24E8CEDED30BB5DB1DC6197199D89000DC91`.
  No decision was reversed and no new lead mathematical/source judgment was
  found wrong in this batch.
- Current `source/ega0/ega0-7.tex`: 75,620 bytes / 1,397 lines / SHA-256
  `29008BF15E3674F9B84BACDC8168B38E3C2B4B25497B153B2F96C744629749D8`.
  Six exact inverse substitutions reproduce the prior R9 source, 75,432 bytes
  / SHA-256
  `81196521B4A963CFD614452C63C1669482B4C58A6A2E250DD593B1B11159F036`.
- `controls/SOURCE_INPUT_SHA256_R10.json` is 24,749 bytes / SHA-256
  `D564A77B667290642B5206B29EC32FD667552D543642CE30F6ADF5D08DF325AE`.
  Independent Python and PowerShell ordinal replays agree on 127 rows,
  7,280,208 bytes, first path `EGA4_reference_v2_links.tex`, and tree SHA-256
  `07BA24509DBA3162F680445DD535574044B3BB0E6E2BE03604EAFCA170CB71E7`.
- R10 diff validation is 6,716 bytes / SHA-256
  `C4EF8A240F3CEC321AA4437F4D810343E2F06B953F7A8736C99C39775FFD7444`,
  PASS/errors empty. Its independent replay is 3,628 bytes / SHA-256
  `B43869F4F6BC4B04D86E98AC5CE530BF8602360DC3EE70865033D420DFA52A61`,
  PASS/errors empty. This current manifest/diff pair supersedes the stale R3
  aggregate binding reported by archive maintenance while preserving R3 as
  adverse history.
- No global reader build was triggered. Global build, reference coordinates,
  privacy-clean projection, rights/package closure, archive handoff/readback,
  and methodology/replication DOI logbook custody remain pending.

## 2026-08-02 — EGA I printed p.75 French recheck

- Personally compared paragraph 7.6.15, Propositions 7.6.16--7.6.17 and their
  proofs, and Corollary 7.6.18 and its proof against direct NUMDAM 5,000-dpi
  bands. Authority manifest: 2,993 bytes / SHA-256
  A5623387606C16D2DC3360971781F36E8D5BDF65FA70CD8C41D55636C8F39675.
- Applied three separately justified English repairs:
  - “flat for each of the rings” became standard mathematical “flat over each
    of the rings,” directly reflecting French “plat sur”;
  - restored “is” in “A_{S} is a local ring,” because French explicitly has
    “est” and the inherited sentence lacked its finite verb;
  - replaced nonidiomatic “We know from before” with “We already know” for
    “On sait déjà.” This last change has no mathematical effect and is logged
    as register normalization rather than hidden as copyediting.
- Decision ledger: three rows / 4,464 bytes / SHA-256
  8FEEADF8588E430401C865293AE55DE34B9A73CC61894140FE475674183F2D52.
  Repair-event ledger: three rows / 3,047 bytes / SHA-256
  A2623653DFAB44EAB81F4657A05328BF283B1E77F8F35EB6D77E294FDD206CAC.
- Current ega0-7.tex is 75,432 bytes / SHA-256
  81196521B4A963CFD614452C63C1669482B4C58A6A2E250DD593B1B11159F036.
  No other source input differs from the frozen predecessor.
- R9 has 127/127 exact rows / 7,280,020 bytes and ordinal tree SHA-256
  B20246760E9A19F7050C457EC91697105B6CB255FBBDDEFF15DD0718716698AE.
  Python and PowerShell ordinal implementations agree exactly. Manifest:
  24,485 bytes / SHA-256
  203A7E34F3BC5683E4612DA4300358B4A5DD295EA2781454811EB2C15A38B05D.
- R9 diff validation is 5,421 bytes / SHA-256
  40AC5CDB5B686B5468DCD67B26BD9C5BFCA329D080D0FC696181AAE6DF6E9C90,
  PASS/errors empty. Replay is 2,556 bytes / SHA-256
  0C984F40AA06735D214D7E3264FD7C5DC3C5AF1FFE5EEFACF2E0CE4C9A84A8AA,
  PASS/errors empty. Inverse reconstruction of the three new edits reproduces
  the exact R8 source hash, so the 26 earlier assertions plus six new
  required/obsolete assertions are closed.
- No global reader build was triggered for this pagewise source batch. The
  final/global build, reference-coordinate replay, privacy-clean projection,
  package/archive handoff, rights/caveat closure, dual-DOI logbook binding,
  and public readback remain pending.

## 2026-08-02 — EGA I printed p.96 English recheck / R25

- Direct comparison against NUMDAM p.96 found no mathematical deviation,
  unsupported correction, or prior lead error. The ideal/module notation,
  both Hom displays, all functor-composition orders, and Theorem 1.7.3 are
  source-exact.
- Two nonmathematical changes were applied and individually justified. The
  inherited doubled Chapter 0 parenthesis is replaced by the source's single
  shared parenthesis, and the previously plain 3.5.4.4 locator becomes a new
  clickable edge. `When no confusion results` replaces the less literal
  `when there is no chance of confusion`.
- The visible translator footnote at Theorem 1.7.3 is retained because it is
  explicitly marked and points to the later errata-added §1.8; it is not
  silently represented as authorial French text. Established visible-equivalent
  macros and semantic environments are separately logged as retained choices.
- Decision ledger: ten rows / 4,144 bytes / SHA-256
  `69FEE7A8EE3B705A6ABE2F53A66B72969CBFD7B110C4BF9DB89386A3B045842C`.
  Applied mathematical repairs: zero. Lead errors: zero. Reversals: zero.
- Current source: 78,908 bytes / 1,266 lines / SHA-256
  `758885F9505A72DF1A5A2EF8B116D998A41D0505571AD8E7028C438EE5795C6E`.
  Two inverse substitutions reproduce exact R24.
- R25: 127 rows / 7,280,231 bytes / ordinal tree SHA-256
  `8D3BF2A908E654E4B94AC1FFE2BEF606BF4EE92FDCEB400AAC02B737E1D51E4E`;
  manifest SHA-256
  `516696896ADBB097947CC00005B37C890C505AE9DB1D5B17EC688E0F8E7A475B`.
  Section/full validation SHA-256 values are
  `25124EBCA38FF5C5583ED1B85D1D3FD19DF40AD5EE4C740ED4D0804262FA091F`
  and
  `C748F5AD369E150BC8BFCFDE9E870AC2C7CFD914FE4A72032FE9DEE4F04BA945`,
  both PASS/errors empty.
- No global English build, English render, OCR, agent, or heavy parallel job ran.
  Global build, cumulative reference/pre-Stacks replay, privacy, rights,
  package/archive, dual-DOI logbook custody, and readback remain held until the
  pagewise French/source-recheck production stabilizes.

## 2026-08-02 — EGA I printed p.97 English recheck / R26

- Direct comparison against the full authority page found the proof of
  Theorem 1.7.3, its square, Corollaries 1.7.4--1.7.5, and Definition 2.1.2
  mathematically source-faithful. No prior correction was invalidated.
- Two local prose repairs were applied and separately justified. The source
  has one singular hypothesis, so `The hypotheses ... mean` became `The
  hypothesis ... means`. French `c'est-à-dire` is equivalence, so the
  unsupported temporal phrase `and we now write` became `equivalently`.
  Mathematical repairs zero; diagram repairs zero; lead errors zero;
  reversals zero.
- Ten decision rows / 3,871 bytes / SHA-256
  `0CA4E32D47D13CBABB1993F7B3F8498A1B9F6152F6EEF28EC7A280811740E06A`.
  Current source is 78,906 bytes / SHA-256
  `EB62DDA7A40E93BFF26BEF9513693192A7C46540E08D244C18218F9BAAEF4FFA`;
  two exact inverse substitutions reproduce R25.
- R26 manifest: 127 rows / 7,280,229 bytes / SHA-256
  `A28F89369E461D3B434C5F66F51299B462AB9CE4F457ACA952B94551CDBE4147`;
  ordinal tree SHA-256
  `F6706D38DCA72AE5A01C4999F52056424809462990F8136C8042D6DE4108210E`.
  Section/full validation SHA-256 values are
  `B5AA88938FE6ADB0D44B3A0C41DAEA8EFFAD407B28FE783C3C6EA2BF9A5E54EE`
  and
  `64E386E2F1EA05F1D41B7E8AA4EA42B786CF7B5DB9BA9F10127B744588874976`,
  both PASS/errors empty.
- No English build/render, OCR, agent, or parallel heavy job ran. This pagewise
  audit remains source-first; cumulative build, reference/pre-Stacks,
  privacy, rights, package/archive, logbook DOI custody, and public readback
  remain deferred to the stabilized corpus checkpoint.

## 2026-08-02 — EGA I printed p.98 English recheck / R27

- Personally compared all p.98 English units against direct NUMDAM authority.
  Proposition 2.1.3 had two inherited register deviations: `there exists
  some` was reduced to the source-exact existential `there exists`, and
  `contained inside` became standard mathematical `contained in`. These are
  separately logged and have no mathematical effect.
- NUMDAM really prints `generic point of X` in the proof of Proposition 2.1.5.
  The proposition and preceding sentence concern $Y$, so the existing English
  correction to $Y$ is correct and remains immediately disclosed in its
  translator note. This is one retained/reverified source-typo correction,
  not a new correction and not a reversal.
- All rings, open sets, closures, maps, local-ring notation, logical
  conditions, and Definition 2.2.1 agree with authority. Established `sh{O}`,
  sharp, semantic-environment, and clickable-target encodings are retained as
  visible-equivalent reader normalization.
- Decision ledger: nine rows / 4,042 bytes / SHA-256
  `B1F157AC5909DD65497B34C67BA44A17E2362869C92402548E99A8E3F579C323`.
  Current source: 25,214 bytes / SHA-256
  `9239F37777A793E4A03AFEDCD0479AD55C7D90EC6A92886B20E20F80A031BA18`.
  Two exact inverse substitutions reproduce R26 byte-for-byte.
- R27 manifest: 127 rows / 7,280,220 bytes / SHA-256
  `1EBEC66D050557D5F20B1EF42B1CF8F3A7717D59ACD2CFDB3384604E0DDD5419`;
  ordinal tree SHA-256
  `07D146DDD043D20E0D30F09612E645F86A14000E974FE9C44703B6B0D35E239A`.
  Section/full validation SHA-256 values are
  `848CB0B5D0C789952E7E7B74D76C69C033BF6158A889ED33237323C8D8C9ADBA`
  and
  `804FF9CD84297A0C20B4AA027BED4EF42F54371CEA69E0B18FB18DE5D64D663F`,
  both PASS/errors empty. New mathematical repairs zero; English lead errors
  zero; reversals zero; diagram changes zero.
- No English build/render, OCR, agent, or parallel heavy work ran. Cumulative
  build, exhaustive reference/pre-Stacks replay, privacy, rights, package,
  archive, dual-DOI logbook custody, and public readback remain deferred until
  the diplomatic/source-recheck corpus stabilizes.

## 2026-08-02 — EGA I printed p.99 / English R28 source comparison

- Personally compared the residue-field paragraph, 2.2.2, Example 2.2.3,
  Proposition 2.2.4 with equation 2.2.4.1, and the opening of Proposition
  2.2.5 against the direct NUMDAM authority. Formulae, quantifiers, maps,
  ideals, residue fields, and the page seam agree. No diagram occurs.
- Made four reversible prose/register repairs, each justified by the French:
  `gives us a monomorphism` became `therefore gives a monomorphism` to retain
  `donc`; `since it is given by the formula` became `as follows from the
  formula` because the formula supplies the inference; `contained inside`
  became standard mathematical `contained in`; and `so, with the equation`
  became `hence, by the relations` because multiple displayed relations are
  invoked. None is a mathematical or source-text correction.
- Preserved the absence of terminal punctuation at equation 2.2.4.1 and the
  exact page seam after the source's unfinished `Il existe alors une`.
- Current source: 25,214 bytes / SHA-256
  `C2C52F7F7543ABEC2A082C294123434E07FFA64E57181A879C033850C8E7DCBC`.
  Decision ledger: nine rows / 4,121 bytes / SHA-256
  `2198C5F835E8539CA737193AD32E41F58E4F47E1CF66AD20A9EAC1842DDD8251`.
  Four inverse substitutions reproduce exact R27. New mathematical repairs
  zero; source corrections zero; lead errors zero; reversals zero.
- R28 manifest: 127 rows / 7,280,220 bytes / SHA-256
  `6E3AE6380AA300004627DEF42A1ECFEFEC6326C8887C525A9930A50623CF5B3C`;
  ordinal tree SHA-256
  `4C32D118D81AC1B2E89A5AEC33FD0C355B98DD2D509235A64C7A01D274280D01`.
  Section/full validation SHA-256 values are
  `063C3EFAA094A4A9C31494D2815F750CD1BED12BB8043C045BD330C0E78F13CF`
  and
  `B2FDF41EE8C27785E81EAAE0EA8050FA5049FDD9B0B7B1B3175F97FEC46B13FF`,
  both PASS/errors empty.
- Reused the already-created authority image; generated no image, crop, OCR,
  build, or render in the English tree. Zero agents and zero parallel jobs ran.

## 2026-08-02 — EGA I printed p.100 / English R29 source comparison

- Personally compared the completion/proof of 2.2.5, definitions 2.2.6 and
  2.2.9, Propositions 2.2.7--2.2.8 with proofs, and Convention 2.2.10 against
  direct NUMDAM authority. Every map direction, inverse image, prime, sharp
  stalk map, irreducible-component index, property, and locator agrees.
- Restored the finite verb in 2.2.7(ii): `g\circ f closed` became `g\circ f
  is closed`, matching French `g\circ f est fermé`. Replaced `Claims` by
  `Assertions`, directly matching `Les assertions`. These are separately
  reversible grammar/register repairs with zero mathematical effect.
- Retained established visible-equivalent reader normalization (`sh{O}`,
  `vphi`, semantic environments, proof headings, and stable clickable
  locators). Proof headings are English-reader structure, not claimed French
  source text; this distinction is explicit in the decision ledger.
- Current source: 25,221 bytes / SHA-256
  `33AF57E584C85A17B7E0A18D22E0C504793BD0C71A30DC864EE0775DC349F5F2`.
  Ten-row decision ledger: 4,145 bytes / SHA-256
  `81A07441311D728DA84936E0AE8C9C7708753527DE7D80CDF8F366CBFC63864C`.
  Two inverse substitutions reproduce R28. Mathematical/source corrections,
  lead errors, and reversals: zero.
- R29 manifest: 127 rows / 7,280,227 bytes / SHA-256
  `3FC26BF7E9F628BF33AF9834C304C89071A21644DE923E6BCAC42FED6CE6AEE1`;
  ordinal tree SHA-256
  `7B25527C49B34E8EBB847D5887FAE707DBAB1DD9649A4508D0912407BAEAA96A`.
  Section/full validations have SHA-256
  `9AE6449765D5C1F8478EEC1E4A7E622D583BAE33CADC75CC22B4ACE6F8FCF73D`
  and
  `A391D6647EF46501FB39B3E3D313385B97FD15CDC17566A53D0133AE964797BD`,
  both PASS/errors empty.
- No English build/render, OCR, agent, or parallel job ran. The French bounded
  build and three affected-page layout checks are logged in the French corpus;
  global English build/reference/pre-Stacks/privacy/package gates remain held
  until the pagewise source recheck advances further.

## 2026-08-02 — EGA I printed p.101 / English R30 source comparison

- Personally compared 2.3.1, Example 2.3.2, and 2.4.1 through the canonical
  local-scheme morphism against the direct NUMDAM authority. The field and
  polynomial rings, localizations, reciprocal substitution, nonaffineness
  argument, specialization relation, ring-map directions, and the native
  `B'`, `B`, `O_y` triangle all agree mathematically.
- Replaced inherited `although every prescheme` with `since every prescheme`
  because French `puisque` states a causal implication, not a concession.
  Repaired the next construction sentence so `B=K[s]` and `C=K[t]` are two
  polynomial rings and `X_1`, `X_2` are two isomorphic affine schemes; this is
  grammatical fidelity, not mathematical normalization.
- Replaced `We later show` with `We shall encounter again later`. The French
  `Nous retrouverons plus tard` promises a later recurrence as a special case,
  not a later proof of the current assertion. This matters to the author's
  expository claim but not to the theorem content.
- Replaced `associated to a local ring` with `whose ring A is local`, matching
  the direct definition `dont l'anneau A est local`. Replaced plural `For all
  preschemes Y and points y` with `For every prescheme Y and every point y`,
  restoring the source's individual universal quantifiers.
- Retained the established reader normalizations for notation, semantic
  environments, proof headings, and stable clickable locators. They are
  visible-equivalent editorial structure, not claimed French diplomatic text.
  No formula, citation, diagram, target, or edge changed on the English side.
- Current source: 25,205 bytes / SHA-256
  `39D017669DCEFD7B859A5851D112CD2605720CB68F2C7A695C8BEE3FAA6D3535`.
  Ten-row decision ledger: 4,870 bytes / SHA-256
  `A487312FE9ECD0087CFC885B6E20D307CB98659A1B3216DDFD1C151FCD4316B2`.
  Five inverse substitutions reproduce R29 byte-for-byte. Mathematical/source
  corrections, lead errors, and reversals: zero.
- R30 manifest: 127 rows / 7,280,211 bytes / SHA-256
  `0643CFD16D04791CC6865EA67D4C8FC19E0C77D38A073DB7BB0C4EE694AFAC4D`;
  ordinal tree SHA-256
  `E6C94B0401070FA4EA758DA90A03829EE7ED40D97A611A3EA86F751D13E64245`.
  Section/full validations have SHA-256
  `0297DA8CFFFE2870F360923A79CFCF8C8D4FD462538CC65A35F7037D7BA45B8F`
  and `0F533AF99A7BA7A2381ABA387ABCCF01841934A72B772AD2A49C555E0B442F62`,
  both PASS/errors empty.
- No English build/render, OCR, agent, or parallel heavy job ran. The French
  bounded build restored source-order example headings and passed lead layout
  review, including the native triangle. Global English build/reference/
  pre-Stacks/privacy/package gates remain held until the pagewise recheck
  advances further.

## 2026-08-02 — EGA I printed p.102 / English R31 source comparison

- Personally compared Proposition 2.4.2, Corollary 2.4.3, Proposition 2.4.4,
  and the opening of 2.4.5 against the direct NUMDAM authority. The local-ring
  criterion, residue-field morphism, closed-point consequence, dimension-zero
  criterion, and the beginning of the factorization argument agree
  mathematically. No source correction or mathematical normalization was
  admitted.
- Restored the source's individual quantifiers with `for every y` and `for
  every x`. Recast the topology sentence as a homeomorphism onto the subset
  consisting precisely of the indicated points, matching the French logical
  restriction rather than merely smoothing the prose.
- Restored the proof's exact connective structure: `we can reduce ... but in
  that case`, the omitted `therefore`, and `the factorization asserted in the
  statement therefore`. These are argument-signposting repairs, not new
  mathematical inferences.
- Replaced `local scheme associated with A` by `local scheme with ring A`,
  restored `completes the proof`, and made the final consequence explicit as
  `that is ... Proposition therefore gives`. These changes preserve the
  author's register and logical force without altering formulas or claims.
- Retained four mathematical units without intervention: 2.4.2, 2.4.3,
  2.4.4, and the p.102 portion of 2.4.5. No English-side formula, citation,
  diagram, target, or edge changed.
- Current source: 25,259 bytes / SHA-256
  `C9C8D501845AC6FDAF6E6172D308C90C5D34B22AED6C3059DF132F48F8B6E04B`.
  Fifteen-row decision ledger: 5,278 bytes / SHA-256
  `C54DDBC3E12EB17048F5346E33FC8830A8BD341874BDEA1E187C454A997AE69D`.
  Nine inverse substitutions reproduce R30 byte-for-byte. Mathematical/source
  corrections, lead errors, and reversals: zero.
- R31 manifest: 127 rows / 7,280,265 bytes / SHA-256
  `AACB1E16646D6DAAEDF384728D9106CF1D752DDC6223B0F405C2BCC8551562ED`;
  ordinal tree SHA-256
  `D90DDDD991E64D1C022D4BD1CABCD597D46B4FF6ECD23DFAA12B06DB07FEA72E`.
  Section/full validations have SHA-256
  `DFFFA52C8E8CDAD313C2FF3E0722141CB1346503D625CE43295BD6F7E75A964A`
  and `6C30C88EAF95271CC613320EFF2CCBB50282EB71E6801619872F2D1011F94563`,
  both PASS/errors empty.
- No English build/render, OCR, agent, or parallel heavy job ran. The bounded
  French XeLaTeX build passed after the engine was corrected from a preserved
  nonadjudicative pdfLaTeX diagnostic; affected pages 16–17 passed personal
  layout review. Global English build/reference/pre-Stacks/privacy/package
  gates remain held until the pagewise source recheck advances further.

## 2026-08-02 — EGA I printed p.103 / English R32 source comparison

- Personally compared Corollaries 2.4.6--2.4.7, Remark 2.4.8, §2.5, 2.5.1,
  and 2.5.2 through the printed-page end against the direct NUMDAM authority.
  The residue-field factorization, quotient-spectrum monomorphism,
  invertible-module claim, base-prescheme definitions, structural maps,
  category, `Hom_S`, identity, and native `X -> Y` over `S` triangle all agree
  mathematically.
- Changed `For all y` to `For every y`, exactly reflecting singular `Pour tout
  y`; there is no quantifier change.
- Changed `(or, as we say, again, trivial)` to `(or, as one also says, is
  trivial)`. The inherited wording lacked a usable English predicate and
  mistranslated `comme on dit encore`; the repair is grammatical/register
  fidelity, not a module-theoretic intervention.
- Changed `this ensures that, for all s and x, u(x) also lies over s` to `this
  entails that, for every s and every x, u(x) must also be over s`. This
  restores `cela entraîne`, the two singular universal quantifiers, and
  `doit aussi être`; it does not strengthen or weaken the commutative-triangle
  consequence.
- Retained all mathematical text and the native triangle unchanged. No source
  correction, formula, citation, target, edge, diagram, lead error, or
  reversal changed.
- Current source: 25,275 bytes / SHA-256
  `5CFC1E90B2C64C7E2E71FC9EA27DC56E0B03F6ECC48E4C440D613097AB82E191`.
  Eleven-row decision ledger: 3,899 bytes / SHA-256
  `F889E3A1981064D8F9629E844A4C2996EB480BD55240322365453EDA90898A47`.
  Three inverse substitutions reproduce R31 byte-for-byte.
- R32 manifest: 127 files / 7,280,281 bytes / SHA-256
  `9E77BB96A68A09C711439AF2D22FFC4166B844288E6E85F82B69D515B4CD7680`;
  ordinal tree SHA-256
  `5220A1B928990312262D72AC84A3BABAA67B2AED3189AFFD25333911B16B3D22`.
  Section/full validations have SHA-256
  `EB30391344D138D692FDC95AFD80C95C4831BCEE8545E97A08B27AEF38ACB811`
  and `EB5C64209251AC0EAB23185C2992E2741F3FE2C7D4A6D3F79D9AD462B4D01683`,
  both PASS/errors empty.
- No English build, render, OCR, agent, or parallel heavy job ran. The French
  bounded XeLaTeX reader and only its changed/new pages 17--18 passed personal
  layout review. Global reader/reference/pre-Stacks/privacy/package gates
  remain held while sequential source work continues at printed p.104.

## 2026-08-02 — EGA I printed p.104 / English R33 source comparison

- Personally compared 2.5.3--2.5.5, the section 3 and 3.1 headings, §3.1,
  and the p.104 fragment of 3.2.1 against direct NUMDAM authority.
- Replaced `is also an S-morphism` with `is therefore an S-morphism` because
  French `est donc` explicitly marks the logical consequence of restricting
  the morphism. Replaced `for all pairs of indices` with `for every pair of
  indices`, restoring singular `pour tout couple d'indices`. Neither changes
  the gluing condition.
- Direct 2500-dpi evidence establishes that 2.5.5 prints `Si X est un
  S-morphisme`. Retained inherited English `If X is an S-prescheme`: the
  appositive structure morphism `X -> S` and the definition of an `S`-section
  require that object type. Added an immediate footnote identifying the exact
  French wording so the correction is auditable rather than silent.
- Retained the explicit English variable in `for every S'-prescheme X` even
  though the source leaves it unnamed immediately before the formula. This is
  grammatical referent supply, not an additional quantified object. Retained
  plural English headings `Products` and `Sums` for singular French generic
  topic titles; that established normalization is now individually justified.
- Retained all sums, sheaves, homeomorphisms, Hom-product formulas, structure
  maps, binary sum notation, `Spec(A\times B)`, and the opening product
  definition unchanged. No diagram or reference changed.
- Current `ega1-2.tex`: 25,429 bytes / SHA-256
  `5785621211C98B1A4452864F3D408325ECED8F84C6CB16DE0875E052A6E7984F`.
  Audited unchanged `ega1-3.tex`: 56,496 bytes / SHA-256
  `ED1559A08A41EC54E35C4A1E5E192552EF0B1EC52B4CE5FAF1F6E6BB3E5707FB`.
  Nine-row ledger: 3,834 bytes / SHA-256
  `B9BEC0096EDDEE9AEDD842F8F9197C31B5C770AA687840BB281944C32E915CF7`.
  Three inverse operations reproduce R32 byte-for-byte.
- R33 manifest: 127 files / 7,280,435 bytes / SHA-256
  `9FE51AAA429E7749F926D04B52B05891820F4FE6CC3BCCA49FF318AE3402C213`;
  ordinal tree SHA-256
  `85C3EE351B174E4C8C4CE49E782EA151C72D91E6A35A96674E633E10BA0E6956`.
  Only `ega1/ega1-2.tex` differs from R32. Section/full validation SHA-256
  values are
  `0697B5A637FBE0835EDAC71560C2F7825BD2700A0C39441E107AEE9C0CF23259`
  and `835E4222FC24AE496D907DE67B42A61F39EF0D097B41650E89C34C7023490B7D`,
  both PASS/errors empty.
- No English build, render, OCR, agent, or parallel heavy job ran. The French
  bounded reader is 18 pages / SHA-256
  `E6B26C091A3B982E3E8677E890A50775BEB32CA9D49F9CA269A02F20F6DA5DCD`;
  pages 1--17 retain exact predecessor text and changed page 18 personally
  passes. Global reader/reference/pre-Stacks/privacy/package gates remain held
  while sequential source work continues at printed p.105.
