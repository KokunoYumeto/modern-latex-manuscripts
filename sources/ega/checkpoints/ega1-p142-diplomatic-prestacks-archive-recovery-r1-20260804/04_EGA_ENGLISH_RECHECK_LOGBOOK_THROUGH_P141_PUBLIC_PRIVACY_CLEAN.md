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

## 2026-08-02 — EGA I printed p.105 English audit

- Authority was the direct NUMDAM page, inspected from the sole 1,100-dpi
  context render. The page was unambiguous; no additional crop or OCR was
  justified. The French diplomatic transcription independently preserves the
  page through I.3.2.5.
- Repair `EG-EGA-I-P105-EN-PRODUCT-CONDITIONAL-001`: the inherited English
  started a conditional with `If`, inserted `and let`, ended the sentence,
  and then wrote `We then write`. French has one conditional construction.
  The English now has one complete conditional while preserving every object,
  morphism, and displayed product formula. Rationale: grammatical/source
  fidelity only; mathematical delta zero.
- Repair `EG-EGA-I-P105-EN-HYPOTHESIS-NUMBER-001`: changed `the hypotheses on
  f imply` to `the hypothesis on f implies`, because French prints singular
  `l'hypothèse sur f entraîne`. Rationale: exact number agreement; mathematical
  delta zero.
- Retained normalization `affine scheme given by some ring` for `schéma
  affine d'anneau`. This supplies idiomatic English syntax without changing
  the existential content. Retained explicit `Proof` environments for the
  source's unheaded proof paragraphs so the reader has visible structure;
  their proof text remains source-complete. Retained textual `(T, I, 1.1)`
  because reference semantics were outside this page-local prose audit. These
  are not silent choices: all three are rows in the p.105 decision ledger.
- Current `source/ega1/ega1-3.tex`: 56,482 bytes / SHA-256
  `180110F77A0665B749B1F29AB7DE6808E4E9BDEB8A857407572C3D6CF29B693B`.
  Two exact inverse operations restore the 56,496-byte p.104 predecessor at
  SHA-256
  `ED1559A08A41EC54E35C4A1E5E192552EF0B1EC52B4CE5FAF1F6E6BB3E5707FB`.
  Decision ledger: eight rows / 3,438 bytes / SHA-256
  `197F46B25506E94021E7987D7BB54DAC98FE4B649CD232E881DFB87E76004B55`.
- R34 manifest: 127 files / 7,280,421 bytes / SHA-256
  `7E5002ACDB744AE24EE49272325ADE110DAA406E813E3A80F357DB2B91AE472B`;
  ordinal tree SHA-256
  `E02F5175C3DEFA9A2EE35E2844ED39ABE01F7EC998331411E405AA7D87E8C241`.
  Section/full validation SHA-256 values are
  `50039F4AF08B24AA3A50DFFEA37168CBBDD110EAC16B587BDB441769A8E9F2E6`
  and `CAA4B234B7BAB495C977F94484A6B50B6104D6529A056825DB85E1EADD2EFFEC`,
  both PASS/errors empty.
- The 12-page bounded build is 113,608 bytes / SHA-256
  `1C41C73B871FBD4ECC630BF6B904B18356E68B9782157C753342CEE65C1EE2D4`.
  Lead inspection of changed physical page 1 at 600 dpi confirms both prose
  repairs, intact mathematics, and no clipping or overlap. No agent, OCR,
  batch render, or parallel heavy job was used.

## 2026-08-02 — EGA I printed p.106 English audit

- Compared the complete English page with the direct 1,100-dpi NUMDAM page
  after writing the diplomatic French. Every product, inverse image, open
  cover, Greek index, composition, and overlap formula agrees.
- Repair `EG-EGA-I-P106-EN-QED-RESTORE-001`: French visibly ends the proof
  of Lemma 3.2.6.2 with `c.q.f.d.`; inherited English omitted it. Added a
  terminal `\qed`. Rationale: restore source proof structure; no theorem,
  hypothesis, formula, or conclusion changes.
- Retained normalization `The proof proceeds in several steps` for `Nous
  procéderons en plusieurs étapes.`: the word “proof” names the implicit
  referent in idiomatic English and adds no assertion. Retained `there is then
  a unique S-morphism` for `il y a donc un S-morphisme et un seul`: exact
  existence-and-uniqueness content. Retained `and similarly` for `et il en
  est de même`: the second open-cover statement remains explicit by its
  object. Retained `Definition 3.2.1` for `la déf. (3.2.1)`: abbreviation
  expansion only. Retained `proof of Lemma 3.2.6.2` for `prouver
  (3.2.6.2)`: the stable numbered unit is named, not reinterpreted.
- Current `ega1-3.tex`: 56,486 bytes / SHA-256
  `4EE566EFB51DDD19D81E0392070899C2A64A51AF6997D65BC1B4ED07386C317B`.
  One exact inverse operation removes the terminal marker and restores the
  p.105 source, 56,482 bytes / SHA-256
  `180110F77A0665B749B1F29AB7DE6808E4E9BDEB8A857407572C3D6CF29B693B`.
  Decision ledger: eight rows / 3,104 bytes / SHA-256
  `12BD1328BAD114D1B1CF117E03401E60391DA1C63FB078D28B62CC9C76B437F2`.
- R35 manifest: 127 files / 7,280,425 bytes / SHA-256
  `FBEF05B2BDCB707DC1DB7AC8E176981B66F234DA03E1399208F5AE134EA99929`;
  ordinal tree SHA-256
  `BBBCB2AAA9C5A946847B25B2F483024E637558955863F5A1E194CB4FDCD6C52A`.
  Section/full validation SHA-256 values are
  `D7D0E55F9AC38AF76A9302D2A593CFAB0D5C41BBC0AFA6BA957C09BCDB8E752A`
  and `7DF09CABA52388F313CCA150D89C6309FA8A1E6EA685BBC87BF41D212E0CFE9F`,
  both PASS/errors empty.
- The 12-page bounded PDF is 113,629 bytes / SHA-256
  `C1907F6CD2FD0E12A678E231DAF85EE336688EC520646D271FB5DDD9181F8F3C`.
  Personal inspection of physical page 2 at 600 dpi confirms the terminal
  square, all surrounding mathematics, and clean layout. A known Windows
  long-path limitation was handled through one short temporary page copy,
  which was removed after the final evidence was copied and hashed. No agent,
  OCR, batch render, or parallel heavy job was used.

## 2026-08-02 — EGA I printed p.107 paired correction audit

- Direct French authority: PDF one-based p.106 / printed p.107, personally
  inspected from the 1,100-dpi page image SHA-256
  `E28F0B56EA197B2A091AD9F2CD813EDB01A51CEFADCBC1CA260E4603D6568476`.
  No ambiguity, crop, or OCR.
- Repair `EG-EGA-I-P107-EN-3263-CITATION-PLACEMENT-001`: inherited English
  made “by Lemma 3.2.6.1” modify the displayed inverse-image equality. In the
  French, the equality is stated first; `en vertu de (3.2.6.1)` then supports
  the product structure defined by the restricted maps. Moved the citation
  to that sentence. This changes logical attribution but no formula,
  hypothesis, conclusion, or mathematical claim.
- Retained `It follows that we have` for `Il y a par suite`; `We immediately
  see ... and similarly` for `on constate aussitôt ... et de même`; `it
  suffices to prove` for `tout revient à prouver`; and `Theorem 3.2.6` for
  `th. (3.2.6)`. These are idiomatic renderings or abbreviation expansion,
  not mathematical edits.
- Exact inverse replay exposed an unlogged post-R35 formatting drift: two
  leading spaces on each of seven lines, fourteen bytes total. Although TeX
  ignored them visually, retaining them would falsely describe the source
  lineage. Removed those bytes, preserved R36 and bounded build r1 as stale
  exact history, and regenerated the active identities. This is logged as a
  provenance error with zero mathematical effect.
- Final `ega1-3.tex`: 56,478 bytes / SHA-256
  `E6EEAE7CEF181FBB81A6E671AEE221B87E59AB43AD18174CAE570C9161EE3CA7`.
  One inverse citation operation restores R35: 56,486 bytes / SHA-256
  `4EE566EFB51DDD19D81E0392070899C2A64A51AF6997D65BC1B4ED07386C317B`.
  Decision ledger: 8 rows / 3,833 bytes / SHA-256
  `F8470660B18EB6996E57CE2CC9AA3B2DA44991FBF74E0D4D02B8AA40150C54C9`.
- R37 manifest: 127 files / 7,280,417 bytes / SHA-256
  `F5E43F1622CD9BBE5829A18A91771824C0D3426C1D797149F9CB8861FA28861A`;
  ordinal tree SHA-256
  `D9237435250A25A398CFF70A89052955964AA4DFF7113F74DE77E5A26DA748FE`.
  Section/full validations are PASS/errors empty at SHA-256
  `346C47C220692A30C2D0D321B6449EB4786C47F70E0C9B6E6D2DBD753C95D737`
  and `6642BED78416D3DE1CB1F42ECFB91792B8F5C15BDAC338F0FC7304F5DFCC2FDF`.
- Final bounded build r2: 12 pages / 113,641 bytes / SHA-256
  `2CEAC677F19FDA30ED24C911A04E9D43F75162CDAAC914918A54C457C58BD784`.
  All twelve extracted page texts equal r1; the affected-page render is
  pixel-identical at SHA-256
  `056807BFAFF42B8312F9DF9A8FCCC8787290F545AF5435C6C70C9A3BE8BEB390`.
  Personal inspection confirms clean citation placement and intact
  surrounding mathematics.
- No unsupported correction to the authors was made; no mathematical repair,
  reversal, diagram change, target change, or edge change occurred.

## 2026-08-02 -- paired French recheck, EGA I printed p.108

- Applied `EG-EGA-I-P108-EN-331-EMPHASIS-001`: source French emphasizes
  `toute catégorie` and `existent`; English now emphasizes `any category` and
  `exist`. This restores rhetorical/source fidelity only and changes no claim.
- Retained the 3.2.6.5 proof square and the proof environment after Corollary
  3.2.7 as explicit modern structural markup. The lead initially removed the
  square based solely on absence of French `c.q.f.d.`; that was an
  overcorrection and was fully reversed before R38. This mistake and reversal
  are explicitly logged.
- Retained `regarded as a morphism into` for the source restriction phrase:
  domain, codomain subprescheme, and map are unchanged. Retained heading
  punctuation normalization as English style. Retained visibly bracketed
  translator augmentation 3.2.9 as English editorial material only; it is not
  promoted into diplomatic French and still needs direct replay against the
  cited EGA II errata p.221.
- Current source: 56,492 bytes / SHA-256
  `0E9CE7FB4E26EE686D1549407FAB8ACF2B521C73C256EB86221524FD89D39D38`.
  Removing the two emphasis wrappers reproduces R37 exactly at 56,478 bytes /
  SHA-256
  `E6EEAE7CEF181FBB81A6E671AEE221B87E59AB43AD18174CAE570C9161EE3CA7`.
- Decision ledger: 8 rows / 4,420 bytes / SHA-256
  `522199B32536F9713525DC17D9ED21574C1DA8150432B49F293EA0CA2BA48447`.
  Counts: mathematical repairs 0; prose/structure fidelity repairs 1; prior
  English fidelity errors caught 1; lead errors caught and reversed 1;
  reversals 1; diagram/target/edge changes 0.
- R38 manifest: 127 files / 7,280,431 bytes / SHA-256
  `15D8794F8BF6AA98FDE1D527EBD87DFED961A03FE59225D7F52D13C245027961`;
  exact ordinal tree SHA-256
  `85E5FBAAD2D054550D91F893853B51B2AE4DC085E4E831E4B8C4C63F1A62C987`.
  Section/full validation SHA-256 values:
  `BB292CF24461D37BD69201E91D55C51BE78066D45FD15C26D41FB76C5B95687E`
  and `9D9D67D83E60190BA83561D324A72CDE646637162E85F71811A8597D62EE62BF`.
- Final bounded build r2: 12 pages / 113,673 bytes / SHA-256
  `F8D2691252BDFD726BFF1989F7246EC45A110EF0AFDB868724DB13E18642E912`.
  Only page 4 reflowed; whitespace-normalized extracted text is equal on all
  pages, and personal 600-dpi inspection confirms clean emphasis and layout.
- The first build command accidentally created literal `source/$out` build
  artifacts. Their exact target and four generated files were verified, that
  generated directory alone was removed, and a corrected no-overwrite r2 build
  was run. No source byte changed; failed console evidence remains available in
  `controls/ega1_p108_english_bounded_build_r1`.

## 2026-08-02 -- paired French recheck, EGA I printed p.109

- Applied `EG-EGA-I-P109-EN-339-DIAGRAM-PERIOD-001`: removed the period
  attached to the `S''` node in the transitivity diagram. French has no
  punctuation there and the proof continues onto p.110; retaining the period
  falsely closed the sentence at a page seam. Node, arrows, labels, and
  mathematics are unchanged.
- Reconfirmed `EG-EGA-I-P109-EN-338-F-VS-G-001`: French visibly prints `f`
  in the pair used to define the unique map `f`, but the product universal
  property applies to the given map `g:T -> X` and the structure map `psi`.
  English `g` is correct and its immediate translator note transparently
  preserves the source reading. Diplomatic French remains `f`.
- Retained `base change` as standard English for `extension du préschéma de
  base`, retained its synonym beside `inverse image` in 3.3.7, and retained a
  proof environment for the bare source `En effet` proof. Each is structural
  or terminological and changes no object, map, or universal property.
- Current source: 56,491 bytes / SHA-256
  `E5E4C011C43B959AD95657C6B3B79612A0DB6D97A3B926A24A6F853E88861B8C`.
  Restoring the single period reproduces R38 exactly at 56,492 bytes /
  SHA-256
  `0E9CE7FB4E26EE686D1549407FAB8ACF2B521C73C256EB86221524FD89D39D38`.
- Decision ledger: 7 rows / 3,499 bytes / SHA-256
  `A6FB32BFF8443ECEF62EC37435FF9ECF4006DA64E53780838D54273DA0CF0ACA`.
  Counts: mathematical repairs 0; punctuation/structure fidelity repairs 1;
  prior source-backed correction reconfirmed 1; prior English fidelity errors
  caught 1; lead reversals 0; diagram geometry/target/edge changes 0.
- R39 manifest: 127 files / 7,280,430 bytes / SHA-256
  `5582CBE296292FDAD0D5FF8B94C8E660466523DD6DEB9DDF28ACA6B3AEA443DC`;
  exact ordinal tree SHA-256
  `B94674F50196214AF56CD3A4E58BA323CC821B8A61DA7D36669CD1C4B5363BCB`.
  Section/full validation SHA-256 values:
  `3B74BFEFE4AE0B234D56AD2BEBB980F225636B190FE93178CA7BA5A76489EDB2`
  and `5776ECE4968A63C70F9DB3BF93B97F0CA42AB456EC4A340EE3151AD85438EDC5`.
- Final bounded build: 12 pages / 113,669 bytes / SHA-256
  `8E135AF1F53C653F5069EEDCC2C67775F54A6816F2205F5ACE1ADA2E02D95889`.
  Only page 5 changed; personal 600-dpi inspection confirms clean diagram
  punctuation and uninterrupted proof flow.

## 2026-08-02 -- paired French recheck, EGA I printed p.110

- Applied `EG-EGA-I-P110-EN-3311-DIAGRAM-MISSING-PSI-LABEL-001`: the source
  labels `Y_(S')->S'` by `psi_(S')`, while the English diagram left the arrow
  anonymous. The label is restored. This is one mathematical-diagram fidelity
  repair, not a correction to the authors.
- Applied `EG-EGA-I-P109-P110-EN-DIAGRAM-LABEL-SIDE-REPAIR-001`: source upper
  labels occur above and source lower labels below. Because Xy-pic side markers
  are relative to arrow direction, the prior encoding put the lower `phi`,
  `phi-prime`, `psi`, and `f` labels above. Three diagrams are repaired.
- Applied `EG-EGA-I-P110-EN-3311-DIAGRAM-PERIOD-001`: removed the period
  attached to the 3.3.11 diagram's lower-right `X`; the French diagram is
  unpunctuated and the proof continues below it.
- Lead-error record `EG-EGA-I-P109-P110-EN-LEAD-QA-MISS-LOG-001` explicitly
  supersedes the earlier p.109 layout PASS. The miss was caused by reasoning
  from source code rather than verifying rendered label side against the
  left-arrow geometry. The global practical rule is now: inspect the rendered
  side for every arrow label; never infer page-side from `^`/`_` alone.
- Retained normalization decisions: `base change` is standard modern English
  for the source construction, and explicit proof environments expose the
  source's proof structure. Neither changes objects, maps, hypotheses, or
  conclusions. New author corrections on p.110: zero.
- Current source: 56,504 bytes / SHA-256
  `6196282B5900DB26B985B1E0E12385B7FA995F7807E8E43D833C0EB8CE8227F8`.
  Seven inverse operations reproduce R39 exactly at 56,491 bytes / SHA-256
  `E5E4C011C43B959AD95657C6B3B79612A0DB6D97A3B926A24A6F853E88861B8C`.
- Decision ledger: 7 rows / 2,844 bytes / SHA-256
  `2BCAF2978B4F893E66607AAD29ED95B0DB799E5E3A5350D26EC211EDAADE130D`.
  Counts: mathematical diagram repairs 1; aggregate layout/punctuation repairs
  2; author corrections 0; prior English fidelity errors caught 3; lead errors
  caught and repaired 1.
- R40 manifest: 127 files / 7,280,443 bytes / SHA-256
  `072C32119B3126F28C96BB6958FDDFA4A8E5F34B949E1E383F57C96D9D75FE00`;
  exact ordinal tree SHA-256
  `17CFEFE9E801D74857E235DD508E72F4C42AD0FB9EF123176E88EE499B26E215`.
  Section/full validation SHA-256 values:
  `6CFA4AF4D781237FEA638A7C75A5825D1598033EF2C4A2D3E2FF03472563844F`
  and `F5F37BBAACF6F350736B7E1E6C74BF8686931953FF8B331B501AD54393EDBEB1`.
- Final bounded build: 12 pages / 113,708 bytes / SHA-256
  `5D4A01B13AB03D0B2D4203FB87C665CBB848B9B6AC05EAC5B1F89B1AC0C8F17A`.
  Pages 4--5 were personally inspected at 600 dpi for compiled layout; source
  detail was adjudicated from the 1,100-dpi direct NUMDAM authority image.

## EGA I printed p.111 paired French/English adjudication

- The direct NUMDAM authority establishes
  `EG-EGA-I-P111-FR-3312-BASECHANGE-TARGET-Y-VS-XPRIME-SRCTYPO-001`:
  3.3.12 prints `f_(S'):X_(S')->Y_(S')` although the quantified morphism is
  `f:X->X'`. The diplomatic French layer keeps `Y_(S')`. The English layer
  keeps its mathematically required `X'_(S')` and now supplies an immediate
  visible source note. This is a confirmed correction to the printed source,
  not an optional English normalization.
- The direct authority also establishes
  `EG-EGA-I-P111-FR-3315-MORPHISM-DIRECTION-SRCTYPO-001`: 3.3.15 prints scheme
  morphisms `Z[T]->X`, whereas 3.3.14 and the displayed local homomorphisms
  `A(T_i)->B_i` require `X->Z[T]`. The diplomatic French layer preserves the
  printed arrow. English was repaired to `X->Z[T]` and given an immediate
  visible note. The local-ring variance is the mathematical justification.
- Retained normalizations, each non-mathematical: `prescheme` for
  *preschema*; `graph morphism` for *morphisme graphe*; `fibre product` for
  *produit fibre*; and numbered theorem/proposition/definition environments
  matching the printed paragraph structure. None changes an object, arrow,
  quantifier, hypothesis, conclusion, or dependency.
- Counts for this page: confirmed printed-source corrections 2; newly changed
  English mathematical text 1; pre-existing correct but previously
  undisclosed English correction 1; visible source notes added 2; unsupported
  author corrections 0; unsupported corrections reversed 0; lead false
  corrections caught 0.
- French decision ledger:
  `FRENCH_DIPLOMATIC_TRANSCRIPTION_APPEND_P111_20260802.jsonl`, 10 rows /
  3,694 bytes / SHA-256
  `1CEDDC361F0EC9409C888F6D3CF6442E8E671FD9465F06F96244FDF81D3CBA5E`.
  English correction ledger:
  `ENGLISH_CORRECTION_RECHECK_APPEND_P111_20260802.jsonl`, 9 rows / 4,909
  bytes / SHA-256
  `284BE03CE61DF450250344244E03E55E6B6EB6110AF5F593144C0F91EAE1636D`.
  Workflow/adverse ledger:
  `WORKFLOW_ERROR_APPEND_P111_20260802.jsonl`, 6 rows / 3,582 bytes /
  SHA-256
  `263C168F7D0655C61722E5607E019E038B7A51FA3E63FE7526ABA44F42A2ECF7`.
- Current English `source/ega1/ega1-3.tex`: 56,850 bytes / SHA-256
  `A9FAD4038374CDC5BEAEC4412096AEC62D437D63A6D232349757BC868E0FB33C`.
  Two inverse source patches reproduce R40 exactly at 56,504 bytes / SHA-256
  `6196282B5900DB26B985B1E0E12385B7FA995F7807E8E43D833C0EB8CE8227F8`.
- R41 manifest: 127 files / 7,280,789 bytes / SHA-256
  `09EB142C493126469764AFEF70825EAF27FC1D7344BE5C422AA35D56AD953BCC`;
  exact ordinal tree SHA-256
  `4021B24BB11E6520EEC75F4748E75044FFDD2E14FB9733606DAD564650B26F33`.
  Scoped/full validation SHA-256 values are
  `68BFE818FA2F0F13F0E2438AEA6F639E4EA61379A0841C08C788942BD695BFBC`
  and `29A6313B09FED8E055CE6D3D5ED7E2928FDF2E4F31DE6C35862FF43D4D49DF30`,
  both PASS with empty error arrays.
- Final bounded English PDF: 13 pages / 115,301 bytes / SHA-256
  `5C2E0ACC6499CA45E330FB01C8A2F40C3C70DA3788B2C8DDC8311662EB22BB03`.
  Pages 1--5 are byte/text stable against p.110; reflowed pages 6--13 were
  personally inspected sequentially at 600 dpi and pass layout QA.
- Workflow error caught and corrected: an ambiguous PowerShell/MiKTeX output
  argument created four generated build files under the literal directory
  `source/$o`. The exact directory was verified, only those generated files
  were removed with native PowerShell, and the build was rerun with an explicit
  argument array. No source file changed. The adverse console is preserved at
  `controls/ega1_p111_english_bounded_build_r1/adverse-pass1-literal-outputdir-console.txt`,
  19,105 bytes / SHA-256
  `B1D5AD2F0F5AD029B0FAF252E1600ED49CB624E87DA8E2921DAD6A291B60897A`.
  Standing rule: never pass a variable-looking output path as a single
  ambiguous TeX-engine argument.

## 2026-08-03 -- paired French recheck, EGA I printed p.112

- Direct NUMDAM comparison used the existing 1,100-dpi p.112 context image and
  one tight 1,800-dpi product-diagram crop. No OCR or batch rendering was run.
- Applied
  `EG-EGA-I-P112-EN-343-PRODUCT-DIAGRAM-PSI-LABEL-SIDE-001`: the lower `psi'`
  label in the 3.4.3 product diagram now renders below, not above, the lower
  arrow. This is a source-fidelity diagram repair with no change to nodes,
  arrow direction, formulae, or mathematical content.
- Retained choices are individually justified in
  `ENGLISH_CORRECTION_RECHECK_APPEND_P112_20260803.jsonl`: the comma after the
  continuing 3.4.2.1 display makes the English sentence grammatical; `fibre
  product` is established reader terminology; and `location` retains the
  literal historical term while its visible note supplies the modern
  clarification. No author-text correction or unsupported reversal occurred.
- Current English source: 56,850 bytes / SHA-256
  `EC3BB57090C0A12EF48CF9572B0EE933DE8E0759E1F51379A921528A6BB1142E`.
  English decision ledger: 7 rows / 2,356 bytes / SHA-256
  `37596E84ECD5F67543993B3CC9066ACC46B06B92FC4F27BB95B65A38C310A0FC`.
- Bounded PDF: 13 pages / 115,253 bytes / SHA-256
  `A6742676640ADC895B1A24922B5119CDCFBBDE351F8EAEF35C9680BF27400D9E`;
  physical pages 7--8 pass serialized layout inspection.
- The complete 127-file source manifest/diff gate has not yet been regenerated
  for this mutation. R41 is the last sealed English tree; R42 is the first
  open control-plane task before a cumulative build or release claim.

## 2026-08-03 -- paired French recheck, EGA I printed p.113

- R42 first sealed the inherited p.112 English bytes: 127 files / 7,280,789
  bytes, manifest SHA-256
  `86A38A31C8FF069983DC42D61280666FF1045388162940C69CB05FAA57BC769A`,
  canonical tree SHA-256
  `186AC1816F3866938D8043F6DB997FE836EFF378AD2BA2BA1872A1559818552B`,
  and PASS diff validation SHA-256
  `9441A1FBCC35B84CE18AD2457673D8112F1EFFA663B87D705360FCB809FBA0B0`.
- Direct p.113 comparison applied two English prose-fidelity repairs:
  `underlying subspace` to source-backed `underlying space`, and additive
  `also` to inferential `thus` for French `ainsi`. Neither changes an object,
  map, formula, hypothesis, or conclusion.
- Compiled cross-layer QA exposed a previously missed p.112 citation error.
  French visibly cites 2.4.4, and I.2.4.4 supplies the relevant local-scheme
  morphism/local-homomorphism correspondence; I.2.2.4 does not. The English
  link is repaired to I.2.4.4 under
  `EG-EGA-I-P112-EN-345-CITATION-224-VS-244-001`. This corrects the English
  citation target, not the authors.
- Current source: 56,847 bytes / SHA-256
  `8D581435C0AC808A879B35C5805834A620BEF657898EAD308744C357B6E537F8`.
  Three unique inverse operations reproduce R42 exactly. English decision
  ledger: 10 rows / 4,125 bytes / SHA-256
  `E24779EE120F21098A3D0FE81979B185554880DBF70784573050E64625B40681`.
- R43 manifest: 127 files / 7,280,786 bytes / SHA-256
  `79DC085957FB058EB002014309BA1DB84FD8AC6E62690DA650FC43893699E62A`;
  canonical tree SHA-256
  `531CBD2815F995C97B1DEDFDE19B68CD93A045FD639D07DF103027969FA86A10`.
  Full diff validation is PASS/errors empty at SHA-256
  `1444F102061A03B68807713A8B119976D8A6E796204EE4D7216A74DE51820BDE`.
- Final bounded build r2: 13 pages / 115,245 bytes / SHA-256
  `4FA5EF4EC8E04E6270E77731022D347B309CED67A74B73B5EBC4064C4AE58440`.
  Physical pages 7--8 pass serialized 600-dpi inspection; page 8 is
  pixel-identical to the already-inspected pre-citation r1 page. No global
  build, OCR, publication, or archive action occurred.
- Next paired cursor: NUMDAM PDF one-based p.113 / printed p.114, proof of
  Corollary 3.4.8.

## 2026-08-03 -- paired French recheck, EGA I printed p.114

- Direct comparison used one 1,100-dpi NUMDAM p.114 context image, 4,817,920
  bytes / SHA-256
  `D9D4AEC70FD58E62C26C28E9DD8712885CD76226211C4BECDC67C96F32FEDD51`.
  No OCR, crop, batch render, whole-page original-detail load, unbounded
  search, or agent was used.
- Applied `EG-EGA-I-P114-EN-348-DIAGRAM-Q-LABEL-SIDE-001`: the `q` label on
  the lower leftward arrow in the proof diagram for 3.4.8 now renders below
  the arrow, matching the printed page. This changes visible label geometry
  only; nodes, arrow direction, maps, and mathematics are unchanged.
- Direct authority confirms
  `EG-EGA-I-P114-FR-349-TENSOR-MONOMORPHISM-SRCTYPO-001`: French prints a
  `monomorphisme` from `k(x) tensor_(k(s)) k(y)` to `k(z)`, although the
  universal property yields only a homomorphism and injectivity can fail. The
  inherited English `homomorphism` and its immediate visible translator note
  are therefore retained. This is one confirmed author-text correction but
  no newly changed English mathematical text.
- Retained normalizations are separately recorded: `types of composite
  extensions`; explicit proof-environment boundaries; and the explicit base
  map `S' -> S` in 3.5.1. None changes a hypothesis, conclusion, object, map,
  or dependency. Unsupported corrections reversed: zero.
- Current source: 56,847 bytes / SHA-256
  `E6CAD01349ABDC5F3AEBA24356E9593C1D1BFC717038E9D35D99E267C9C5416B`.
  One unique context-bound inverse operation reproduces R43 exactly. English
  decision ledger: 8 rows / 2,981 bytes / SHA-256
  `199D5D35A057C7B4C3339CD0CFB61D24DBC38FBE59E6A68D1C5176A0DD605A05`.
- R44 manifest: 127 files / 7,280,786 bytes; 36,060 bytes / SHA-256
  `0574B3D851A04E1023F4D5BDE1D9D1717D9D644BD9EA93D542BF0CBE5950E10D`;
  canonical tree SHA-256
  `BBD421CCBEE4825695882D5C10BEBE12C3663B53D9D9A16F901490372168CB61`.
  Independent ordinal replay reports zero hash/size/order errors, one changed
  row, and no added or removed rows. Full diff validation is PASS/errors empty
  at 4,914 bytes / SHA-256
  `08201B423C2CFEA44F8649A4B2F0AF570B04B6E578717BA91905A0D679186778`.
- Final bounded build: 13 pages / 115,257 bytes / SHA-256
  `2A131D38698F5BDEA731D22CA28FD157C4DD6C4C9164BE578757D1D8A387259D`.
  Physical pages 8--9 pass serialized 600-dpi inspection, including the
  corrected `q` side, the visible translator note, and clean 3.5.1 layout.
  The log has zero hard errors; no global build, publication, or archive
  action occurred.
- Next paired cursor: NUMDAM PDF one-based p.114 / printed p.115,
  continuation of 3.5.1 after clause (ii).

## 2026-08-03 -- paired French recheck, EGA I printed p.115

- Direct comparison used one 1,100-dpi NUMDAM p.115 context image, 3,574,587
  bytes / SHA-256
  `B83B678E23285A2181C3EAE1AFACFFE2A575CF2731B964FA927B6A3D0D521667`.
  No OCR, crop, batch render, whole-page original-detail load, unbounded
  search, or agent was used.
- Applied `EG-EGA-I-P115-EN-351-COMPOSITION-ANTECEDENT-001`. The prior English
  said only that the composite of two morphisms has property P; French says
  the two component morphisms possess P and their composite also possesses P.
  The repair restores that mathematical antecedent and the intended
  composition-stability hypothesis without correcting the authors.
- Applied two prose-fidelity repairs: `we can further say` restores `encore`,
  and `It follows immediately` restores `aussitôt` rather than the prior
  `also`. Applied one geometry repair: `alpha-prime` now renders below the
  lower rightward arrow in 3.5.5, as printed. The p.115 lifting-diagram colon
  and terminal period remain as a justified English grammatical closure.
- Current source: 56,894 bytes / SHA-256
  `AB5F2BBC7E3AD82C0DAF342BC0AD0B3012FCB219FC02F6AFDA7E0DB70C6B347B`.
  Four unique context-bound inverse operations reproduce R44. English
  decision ledger: 9 rows / 3,170 bytes / SHA-256
  `3B6BBFCAD53200981986716F6ECE945A9087ECFDA560643C33492B790A364E7D`.
  Confirmed author-text corrections and unsupported reversals are zero.
- R45 manifest: 127 files / 7,280,833 bytes; 36,487 bytes / SHA-256
  `DFD8BF3BD7A461608179190AAA5FF72AA5F345ECC46C3127D357BEC7B08088F8`;
  canonical tree SHA-256
  `45B3E3D362F2E4D5227E26BFE4CEAA5620176581466DBF9C83D6D26FC0EADE9C`.
  Independent ordinal replay reports zero hash/size/order errors, one changed
  row, and no additions or removals. Full diff validation is PASS/errors empty
  at 5,100 bytes / SHA-256
  `903FF29D8B9EE60E69B9B523E6813C8F5F824BC6E63E7A7066F5A9DA4BE57198`.
- Final bounded build: 13 pages / 115,338 bytes / SHA-256
  `6798D38939861A320C7046601BA5DD2D6AE4F498CA914F4D84C191F86C3C5A1A`.
  Physical pages 9--10 pass serialized 600-dpi inspection, including the full
  logical antecedent, both prose repairs, and the corrected diagram-label
  side. The log has zero hard errors.
- Two long-path `pdftocairo` attempts produced no PNG. Each affected page was
  then rendered singly through a temporary unused `Q:` mapping, removed in a
  `finally` block. This and the French build/output-path events are bound in
  the five-row workflow ledger, SHA-256
  `FA6FBD1248115669C08F103D8FF664A2D42AC3C11D6471CCEA4EE6F59CA52973`;
  no source changed.
- Next paired cursor: NUMDAM PDF one-based p.115 / printed p.116, continuation
  of 3.5.5 immediately after the displayed diagram.

## 2026-08-03 -- paired French recheck, EGA I printed p.116

- Direct comparison used one 1,100-dpi NUMDAM p.116 context image, 4,186,083
  bytes / SHA-256
  `2E1BF02C59C35317E12B8A2CDBD5265F0B135979F33D437CE186CCCD3647F62E`.
  No OCR, crop, batch render, whole-page original-detail load, unbounded
  search, or agent was used.
- Applied `EG-EGA-I-P116-EN-357-AUSSITOT-ADVERB-001`: `and the proposition
  then follows` is now `and the proposition follows immediately`, restoring
  the printed `en résulte aussitôt` without changing the field-valued product
  argument or conclusion.
- Applied `EG-EGA-I-P116-EN-3510-AUSSITOT-ADVERB-001`: `The first claim
  follows from` is now `The first claim follows immediately from`, restoring
  the second printed `résulte aussitôt` without changing its dependencies on
  3.5.8 and 3.4.8. No mathematical-text, formula, or diagram edit was made.
- The paired identities in 3.5.7 remain in consecutive English displays as a
  justified width normalization; their order, equalities, and joint logical
  role are unchanged. Explicit English proof environments remain as
  reader-facing structural normalization. Unsupported reversals, confirmed
  author-text corrections, and new mathematical source edits are all zero.
- Current source: 56,913 bytes / SHA-256
  `5A1EA6875D95D891D87381A288C33B7184B97A9343A982D82D353EB3DA03F2A6`.
  Two unique context-bound inverse operations reproduce R45 exactly. English
  decision ledger: 7 rows / 2,091 bytes / SHA-256
  `357A58F459A72A72DD1198B188353D2A9EE2C306C2D2A2E264791E470797684C`.
- R46 manifest: 127 files / 7,280,852 bytes; 36,969 bytes / SHA-256
  `37C59DE260A37EEB5D4542C3AF9FF71531CC01A6BE3450FAB280F0C1776BDC70`;
  canonical tree SHA-256
  `83506DB9F2EEE686B2E5A7DC2E72BEF4730A3CD42A2C04667F0955FA16779AAA`.
  Independent ordinal replay reports zero hash/size/order errors, one changed
  row with a +19-byte delta, and no additions or removals. Full diff validation
  is PASS/errors empty at 5,219 bytes / SHA-256
  `8FBD28F268EF1F8601F1F81A188B0D3FF674F5F64EA8F73881066EA9503B9083`.
- Final bounded build: 13 pages / 115,346 bytes / SHA-256
  `450AF97FBF4066D3DCB2A72447CA5CFAE11A3684BC9217F3EBF23AFDA8A1A20B`.
  Physical pages 10--11 pass serialized 600-dpi inspection, with both repairs
  visible in context. The log has zero hard errors.
- The long build path was mapped temporarily to unused `Q:` only for the two
  single-page renders; removal ran in `finally` and Q: was independently
  confirmed absent. All five p.116 workflow/resource entries are preserved at
  SHA-256
  `F2B86DBB70D6243F40D354F4C7635EECE2E578BC6BB88DC7FC3EF8C27E0AF96D`;
  none changed source.
- Next paired cursor: NUMDAM PDF one-based p.116 / printed p.117, beginning
  with the diagram that completes the proof of 3.5.10.

## 2026-08-03 -- paired French recheck, EGA I printed p.117

- Direct comparison used one 1,100-dpi NUMDAM p.117 context image, 4,087,846
  bytes / SHA-256
  `5190145A707154F1BCFD1841A0933CB53FDE850BC7E8A01FAE7E7FCBE700E0FC`.
  No OCR, crop, batch render, whole-page original-detail load, unbounded
  search, or agent was used.
- Applied `EG-EGA-I-P117-EN-3511-DABORD-SEQUENCE-001`: `the condition implies`
  is now `the condition first implies`, restoring French `d'abord` and the
  explicit first step of the converse in Remark 3.5.11. This changes no
  mathematical claim, object, map, formula, dependency, or diagram.
- Retained normalizations are explicitly bound: `X times_Y k(y)` and
  `X times_Y B` make the fibre product visible while preserving the source's
  tensor-over-`O_Y` forms; 3.6.1 retains a reader-facing proof boundary; and a
  terminal period closes the p.117 display before the p.118 continuation.
  Unsupported reversals, confirmed author-text corrections, and new
  mathematical source edits are all zero.
- Current source: 56,919 bytes / SHA-256
  `6CCAAE5D05343975ABD6E68B1265525DDCA2C3F7C4A8D25987649DE73DD6C2AC`.
  One unique context-bound inverse operation reproduces R46 exactly. English
  decision ledger: 7 rows / 2,235 bytes / SHA-256
  `F56EF628800F8D06BB6F667F6F84F113170845AB3FE779C52F220EE900C5A77C`.
- R47 manifest: 127 files / 7,280,858 bytes; 37,432 bytes / SHA-256
  `E8C29077CDC78DFB6A7F8A5544F3199F9E5564F64163B10FFC0047B21FC14E8B`;
  canonical tree SHA-256
  `FA3CD639E1DC14145A9270C641F99F1D3FEF399EE96BFB40CC6B8ACD0F35E6E7`.
  Independent ordinal replay reports zero hash/size/order errors, one changed
  row with a +6-byte delta, and no additions or removals. Full diff validation
  is PASS/errors empty at 5,135 bytes / SHA-256
  `A4E877FFFF87ECE878AFDD93BA29D2C2B4A48527D344B533AF40AF992FF2F5F1`.
- Final bounded build: 13 pages / 115,351 bytes / SHA-256
  `32D71EB8A3CC7E7406F68993AF868F9D250DD5A667065769A90AD2E46E56B00E`.
  Physical page 11 passes serialized 600-dpi inspection, with the `first`
  repair visible in context. The log has zero hard errors.
- The long build path was mapped temporarily to unused `Q:` only for the
  single-page render; removal ran in `finally` and Q: was independently
  confirmed absent. The French-only semantic-anchor rebuild did not change
  the English source, build, or R47 tree. All six workflow/resource entries
  are preserved at SHA-256
  `A3E5BC823F9F391B47CEAA82A1AFCCC1BE575E3B4BE68AF5EC96CB2960659AD4`.
- Next paired cursor: NUMDAM PDF one-based p.117 / printed p.118, continuation
  of 3.6.3 immediately after the displayed fibre-composition identity.

## 2026-08-03 -- paired French recheck, EGA I printed p.118

- Direct comparison used one 1,100-dpi NUMDAM p.118 context image, 4,376,825
  bytes / SHA-256
  `52AA3CF4FB2291B552721C56316EEE5B769BBFDBBA9A514FFF720575653D95B1`.
  No OCR, crop, batch render, whole-page original-detail load, unbounded
  search, or agent was used.
- Applied `EG-EGA-I-P118-EN-37-FOOTNOTE-LATER-CHAPTER-I-SCOPE-001`: the
  subsection footnote now says `notions and results from later in Chapter I
  and from Chapter II`, restoring French `de la suite du chap. Ier et du chap.
  II`. This repairs forward-reference scope without changing a mathematical
  statement, object, map, formula, or dependency.
- Retained normalizations are explicitly bound: the 3.6.4 parenthetical title
  follows the English environment dash; the printed subsection footnote is an
  italic reader-facing paragraph; the reordered phrase `the unique closed
  point` remains intact before the p.119 marker; and 3.6.4--3.6.5 retain
  explicit proof environments. Unsupported reversals, confirmed author-text
  corrections, and new mathematical source edits are all zero.
- Current source: 56,933 bytes / SHA-256
  `55C1E1129E40F1E2F8DB7B46867B3E49AE2556F04C1CFE1FBF5EE3C149B63BD9`.
  One unique context-bound inverse operation reproduces R47 exactly. English
  decision ledger: 8 rows / 2,686 bytes / SHA-256
  `3C330E230922DA8C1D40095CE823D7129F80A52DECD0742F8E18348B3C475976`.
- R48 manifest: 127 files / 7,280,872 bytes; 37,933 bytes / SHA-256
  `309B5B0A48AC2F3AD8903891526D8722ECB2C64C5CF18F5293F398BF89B58668`;
  canonical tree SHA-256
  `E8331E55DEABD57007298B17012BE1E50C20370837535F413F3679EBE3FB646B`.
  Independent ordinal replay reports zero hash/size/order errors, one changed
  row with a +14-byte delta, and no additions or removals. Full diff validation
  is PASS/errors empty at 5,402 bytes / SHA-256
  `FE9746CE8BB49D3DF2F96D9EBF9B49AE67B8EEBFD61FD79FAC972AEDA31D4373`.
- Final bounded build: 13 pages / 115,362 bytes / SHA-256
  `28A75B6834B4151C5CA9CF4FD2C475CA4F809CA8E267CE7EF58113B1E9643689`.
  Physical page 12 passes serialized 600-dpi inspection, with the repaired
  forward scope visible. The log has zero hard errors.
- The long build path was mapped temporarily to unused `Q:` only for the
  single-page render; removal ran in `finally` and Q: was independently
  confirmed absent. The French PDF-string warning and semantic-scaffold order
  were repaired before seal without changing the English source or build. All
  six workflow/resource entries are preserved at SHA-256
  `7E6D1E754282AD8E3AF955D19210901B09B0124567FA4FEF77C8D952B176C60D`.
- Next paired cursor: NUMDAM PDF one-based p.118 / printed p.119, continuation
  of 3.7.2 after French `l'unique point`.

## 2026-08-03 -- paired French recheck, EGA I printed p.119

- Direct comparison used one 1,100-dpi NUMDAM p.119 context image, 4,453,245
  bytes / SHA-256
  `98313EF45F7C1C17800DB643DB2652715FD3B80FEF59F6239E25C67B0BB0B31D`.
  No OCR, crop, batch render, whole-page original-detail load, unbounded
  search, or agent was used.
- The remainder of 3.7.2, all of 3.7.3, the section 4 transition, 4.1.1, and
  Proposition 4.1.2 are source-grounded as inherited. No English source byte
  changed. The 4.1.1 `Theorem`/`Corollary` type words and the explicit p.120
  proof boundary remain documented reader-facing normalizations.
- Current `source/ega1/ega1-3.tex`: 56,933 bytes / SHA-256
  `55C1E1129E40F1E2F8DB7B46867B3E49AE2556F04C1CFE1FBF5EE3C149B63BD9`.
  Current `source/ega1/ega1-4.tex`: 33,365 bytes / SHA-256
  `55FCE2B2C9A51F7FC86DCEB1A8E0BD4EC6E06818C28E302FFE045B4CA323B275`.
  Confirmed author-text corrections, source-fidelity repairs, new English
  mathematical edits, and unsupported reversals are all zero. English
  decision ledger: 10 rows / 2,808 bytes / SHA-256
  `9F4E34AF1CF73A748A760C67F8BD30C6B5B63E36053B9DA770F9F7477EAA4FDB`.
- R49 manifest: 127 files / 7,280,872 bytes; 38,368 bytes / SHA-256
  `0BB20AFE664720F711F04AEC55D88E96DA918C27C26DF26FE6D60A7AE8838E8C`;
  canonical tree SHA-256
  `E8331E55DEABD57007298B17012BE1E50C20370837535F413F3679EBE3FB646B`.
  Independent ordinal replay reports zero hash/size/order errors and zero
  changed, added, or removed rows from R48. Full diff validation is
  PASS/errors empty at 5,564 bytes / SHA-256
  `519B2CBC2EA3FCB9FCCCD3F4FB85907776DAD1D260F48BE86E6ED3D888B82031`.
- The bounded build uses a 17-line prefix verified line-identical to live
  `ega1-4.tex` through Proposition 4.1.2. Visual QA caught and repaired only
  the wrapper's initial section counter. Final bounded build: 13 pages /
  117,660 bytes / SHA-256
  `985FC4F4B0A5BD7E6FA236CDC9AC17720A7FAF34D6859C28DF504E2C1F2F82DA`;
  physical page 13 passes with section 4, subsection 4.1, and Proposition
  4.1.2 complete. The two PDF-string warnings are inherited from the section
  3.7 title; the log has zero hard errors.
- The long path required temporary `Q:` only for the single final page render;
  removal ran in `finally` and Q: was independently confirmed absent. All 14
  workflow/resource entries are preserved at SHA-256
  `77B4C54E3939752892E24135D39139599A467A23CFD7F157CB1C80E89EAEC607`;
  none changed English source.
- Next paired cursor: NUMDAM PDF one-based p.119 / printed p.120, proof of
  Proposition 4.1.2 beginning French `Il suffit évidemment`.

## 2026-08-03 -- paired French recheck, EGA I printed p.120

- Direct comparison used one 1,100-dpi NUMDAM p.120 context image, 4,526,764
  bytes / SHA-256
  `6A978EC28596239DDFEDD191E02DEB3A0149A5C62B34DD69205F7AA6408C8DA7`.
  No OCR, crop, batch render, whole-page original-detail load, unbounded
  search, or agent was used.
- The proof of 4.1.2, terminology paragraph, Definition 4.1.3, canonical
  closed-subprescheme/ideal-sheaf bijection, 4.1.4, Proposition 4.1.5 with
  proof, the open induced-prescheme consequence, and the opening of 4.1.6 are
  source-grounded as inherited. No English source byte changed. Explicit
  proof environments, proof-reference type words, and the whole-word p.121
  page marker are documented reader-facing normalizations.
- Current `source/ega1/ega1-3.tex`: 56,933 bytes / SHA-256
  `55C1E1129E40F1E2F8DB7B46867B3E49AE2556F04C1CFE1FBF5EE3C149B63BD9`.
  Current `source/ega1/ega1-4.tex`: 33,365 bytes / SHA-256
  `55FCE2B2C9A51F7FC86DCEB1A8E0BD4EC6E06818C28E302FFE045B4CA323B275`.
  Confirmed author-text corrections, source-fidelity repairs, new English
  mathematical edits, and unsupported reversals are all zero. English
  decision ledger: 13 rows / 3,669 bytes / SHA-256
  `48EA6332507CFC53013C67985A89E876E773448D8753E490352E34A4F749B7E6`.
- R50 manifest: 127 files / 7,280,872 bytes; 38,864 bytes / SHA-256
  `D6F7AFA347FD3B0B3D63E310394D0D3CE9D77AF57F26C44A9C3FE189C98D43A8`;
  canonical tree SHA-256
  `E8331E55DEABD57007298B17012BE1E50C20370837535F413F3679EBE3FB646B`.
  Independent ordinal replay reports zero hash/size/order errors and zero
  changed, added, or removed rows from R49. Full diff validation is
  PASS/errors empty at 6,347 bytes / SHA-256
  `988292B9754053803D7AEDDD1817D95A7543D6A1361F806F91BC2C29E1DD4FC0`.
- The p.120 continuation projection has 50 lines exactly matching live
  `ega1-4.tex` lines 18--67 and one final balancing close. Final bounded
  build: 14 pages / 122,887 bytes / SHA-256
  `172F4C958CEFE1BAA310557229E6F73D0FEB58A3462A6BA8634A1296BA2546F8`;
  physical page 14 passes serialized 600-dpi inspection. The two PDF-string
  warnings are inherited from the section 3.7 title; the log has zero hard
  errors.
- Temporary `Q:` was used only for the single terminal-page render and page
  count, then removed and independently confirmed absent. All 11
  workflow/resource entries are preserved at SHA-256
  `4CFA1980B9D7A926667D08D631524DFB28BB4F0BC92FB9B81A370429EA687215`;
  none changed English source.
- Next paired cursor: NUMDAM PDF one-based p.120 / printed p.121,
  continuation of Proposition 4.1.6 after French `d'un sous-`.

## 2026-08-03 -- paired French recheck, EGA I printed p.121

- Direct comparison used one 1,100-dpi NUMDAM p.121 context image, 4,515,600
  bytes / SHA-256
  `466CF45909A29FEAA5AAD19DB13F1BEE4C898C1D82A4AB1A89CA7FA4525EEFD7`.
  No OCR, crop, batch render, whole-page original-detail load, unbounded
  search, or agent was used.
- Proposition 4.1.6 with proof, the standing identification convention,
  4.1.7, 4.1.8, Proposition 4.1.9, and its proof through the terminal morphism
  are source-grounded as inherited. No English source byte changed. The
  whole-word marker, explicit proof environments, translator note on
  `majoré`, and English `g` for French `g'` remain documented reader-facing
  normalizations.
- Current `source/ega1/ega1-3.tex`: 56,933 bytes / SHA-256
  `55C1E1129E40F1E2F8DB7B46867B3E49AE2556F04C1CFE1FBF5EE3C149B63BD9`.
  Current `source/ega1/ega1-4.tex`: 33,365 bytes / SHA-256
  `55FCE2B2C9A51F7FC86DCEB1A8E0BD4EC6E06818C28E302FFE045B4CA323B275`.
  Confirmed author-text corrections, source-fidelity repairs, new English
  mathematical edits, and unsupported reversals are all zero. English
  decision ledger: 11 rows / 3,332 bytes / SHA-256
  `DBF5BDEE551BE26F11A15F8456BC5AEDAAC089EE09A443A223A25AEEAA15A93D`.
- R51 manifest: 127 files / 7,280,872 bytes; 39,418 bytes / SHA-256
  `F6736445D6C310C85A5FA44E5B718C71EC6B6574DCC28CFF1BD8AD673EBF46A8`;
  canonical tree SHA-256
  `E8331E55DEABD57007298B17012BE1E50C20370837535F413F3679EBE3FB646B`.
  Independent ordinal replay reports zero hash/size/order errors and zero
  changed, added, or removed rows from R50. Full diff validation is
  PASS/errors empty at 6,385 bytes / SHA-256
  `8E0A9E1AD4122E6320D288A3CDE75D7262C4608FEB2D7983ADBD2101FAE6C6BC`.
- The p.121 continuation projection has 96 lines exactly matching live
  `ega1-4.tex` lines 18--113 and one final balancing close. Final bounded
  build: 14 pages / 128,025 bytes / SHA-256
  `148D326B436272E09B8C644CD29F1F05064517B4B02EC6006220935D04A43472`;
  physical page 14 passes serialized 600-dpi inspection. The two PDF-string
  warnings are inherited from the section 3.7 title; the log has zero hard
  errors.
- Temporary `Q:` was used only for the single terminal-page render and page
  count, then removed and independently confirmed absent. All 12
  workflow/resource entries are preserved at SHA-256
  `2431D227B193C56F583A0637A87EF1AC28B7AE9F7A88ABBD90E0B8323715F23A`;
  none changed English source.
- Next paired cursor: NUMDAM PDF one-based p.121 / printed p.122,
  continuation of the proof of Proposition 4.1.9 after French `g':Z\to Y`.

## 2026-08-03 -- paired French recheck, EGA I printed p.122

- Direct comparison used one 1,100-dpi NUMDAM p.122 context image, 4,084,576
  bytes / SHA-256
  `AA56A3CA45D405ACC6699DC7E139A72643B204715E5FA3E1FEEEB799383AB4D4`.
  No OCR, crop, batch render, whole-page original-detail load, unbounded
  search, or agent was used.
- The completion of 4.1.9, Corollary 4.1.10, the order notation, Definition
  4.2.1, Proposition 4.2.2, and its proof through the p.122 terminal phrase
  are source-grounded as inherited. Printed proof 4.2.2(a) reverses the
  source and target of `\theta^\sharp`; the inherited English gives the
  mathematically typed direction and exposes the correction in a translator
  footnote. English `g` across the printed `g'`/`g` fluctuation and the p.123
  marker before the complete direct-image object remain documented
  reader-facing normalizations. No English source byte changed.
- Current `source/ega1/ega1-3.tex`: 56,933 bytes / SHA-256
  `55C1E1129E40F1E2F8DB7B46867B3E49AE2556F04C1CFE1FBF5EE3C149B63BD9`.
  Current `source/ega1/ega1-4.tex`: 33,365 bytes / SHA-256
  `55FCE2B2C9A51F7FC86DCEB1A8E0BD4EC6E06818C28E302FFE045B4CA323B275`.
  Confirmed author-text corrections: one inherited and explicit; new English
  mathematical edits, source-fidelity repairs, and unsupported reversals are
  zero. English decision ledger: 11 rows / 3,731 bytes / SHA-256
  `DF71BFA7B1FBF4F72D40E469AF4916C5DE9743944C1EBCB096A938F563B35AC5`.
- R52 manifest: 127 files / 7,280,872 bytes; 40,084 bytes / SHA-256
  `B2BCA961EEE011D9E5F03147CD696F9888D96E6A58F944DD1A2ED6FB292EE614`;
  canonical tree SHA-256
  `E8331E55DEABD57007298B17012BE1E50C20370837535F413F3679EBE3FB646B`.
  Independent ordinal replay reports zero hash/size/order errors and zero
  changed, added, or removed rows from R51. Full diff validation is
  PASS/errors empty at 6,974 bytes / SHA-256
  `75B3BC2A7E09CDDBCBAEA5D558E9F37095FA4052C908330323F43F2D50A2AF4D`.
- The p.122 continuation projection has 144 lines exactly matching live
  `ega1-4.tex` lines 18--161 and two final balancing closes. Final bounded
  build: 15 pages / 133,594 bytes / SHA-256
  `D4EF20AEA2BC89EF7924C5B42870B64DE05F5E6F6AE39B8D2D66E67C566E676C`;
  physical pages 14--15 pass serialized 600-dpi inspection. The two
  PDF-string warnings and two overfull boxes are inherited; the log has zero
  hard errors.
- Temporary `Q:` was used only for long-path Poppler access, removed in each
  `finally`, and confirmed absent. All 11 workflow/resource entries are
  preserved at SHA-256
  `0E7D40B3BB0A586606DE20CF181043610C8EA8062FA7CEB8F1E7B8606C7F132B`;
  none changed English source.
- Next paired cursor: NUMDAM PDF one-based p.122 / printed p.123,
  continuation of Proposition 4.2.2(b) after French
  `restriction à $U$ de l'image`.

## 2026-08-03 -- paired French recheck, EGA I printed p.123

- Direct comparison used one 1,100-dpi NUMDAM p.123 context image, 4,233,219
  bytes / SHA-256
  `91F7D24B15E1C76360049B11212C7284F87F3DAEC9366C4CEAD3B91C3DA721DF`.
  No OCR, crop, batch render, whole-page original-detail load, unbounded
  search, or agent was used.
- The completion of Proposition 4.2.2, Corollary 4.2.3, and the opening of
  Corollary 4.2.4(a) are source-grounded as inherited. The p.123 direct-image
  boundary placement remains a documented normalization. The explicit p.122
  correction of the reversed `\theta^\sharp` direction is carried and
  visible but is not a new p.123 correction. No English source byte changed.
- Current `source/ega1/ega1-3.tex`: 56,933 bytes / SHA-256
  `55C1E1129E40F1E2F8DB7B46867B3E49AE2556F04C1CFE1FBF5EE3C149B63BD9`.
  Current `source/ega1/ega1-4.tex`: 33,365 bytes / SHA-256
  `55FCE2B2C9A51F7FC86DCEB1A8E0BD4EC6E06818C28E302FFE045B4CA323B275`.
  New author-text corrections, new English mathematical edits,
  source-fidelity repairs, and unsupported reversals are zero. English
  decision ledger: 9 rows / 2,991 bytes / SHA-256
  `F948EE8915F1F1CE7A1C1A6352A13D4F218B6A084F36678DA3E9A20C12822321`.
- R53 manifest: 127 files / 7,280,872 bytes; 40,442 bytes / SHA-256
  `A66887EBE9AA70959C970051C08550FD8A4DE525CD78D23A21662B4C75F18ED5`;
  canonical tree SHA-256
  `E8331E55DEABD57007298B17012BE1E50C20370837535F413F3679EBE3FB646B`.
  Independent replay reports zero hash/size/order errors and zero changed,
  added, or removed rows from R52. Full diff validation is PASS/errors empty
  at 7,465 bytes / SHA-256
  `465F8FE2D3DC7B10BA4CC74792B81A8BD65B51FD29C03B37B0AD2495F5979DD9`.
- The first live-marker bounded wrapper did not terminate within 60 seconds;
  its sole surviving XeLaTeX process was identity-checked and stopped. Four
  incomplete files / 105,879 bytes are retained as superseded evidence and
  excluded from final claims. The replacement projection has 187 lines
  exactly matching live `ega1-4.tex` lines 18--204 and two balancing closes.
- Final bounded build: 16 pages / 139,048 bytes / SHA-256
  `892949ADB0BED5773CC14933B0CCD79860D21FBA1501CC9639A61DC835B6C24E`;
  physical pages 15--16 pass serialized 600-dpi inspection. The two
  PDF-string warnings and two overfull boxes are inherited; the log has zero
  hard errors.
- Temporary `Q:` mappings were removed after use. All 15 workflow/resource
  entries are preserved at SHA-256
  `E2DC27D9F1A1EEC4E569AE7099334370BA2FA931E43FFDAEAC9E93F0BA5FCC8A`;
  no XeLaTeX process remains and none of the workflow events changed English
  source.
- Next paired cursor: NUMDAM PDF one-based p.123 / printed p.124,
  continuation of Corollary 4.2.4(a) after French `il faut et il suffit`.

## 2026-08-03 -- paired French recheck, EGA I printed p.124

- Direct comparison used one 1,100-dpi NUMDAM p.124 context image, 4,297,349
  bytes / SHA-256
  `DBA58C282E3CF63EA81EF4C57669371DC063F9BCD34A54BB9F60D08E01F1EA31`.
  No OCR, crop, batch render, whole-page original-detail load, unbounded
  search, or agent was used.
- Corollary 4.2.4, Proposition 4.2.5, subsection 4.3, Proposition 4.3.1, and
  its proof through the p.124 terminal phrase are source-grounded as
  inherited. The p.124 marker before `for its restriction` is a documented
  semantic-boundary normalization. The explicit p.122 correction of the
  reversed `\theta^\sharp` direction is carried and visible but is not a new
  p.124 correction. No English source byte changed.
- Current `source/ega1/ega1-3.tex`: 56,933 bytes / SHA-256
  `55C1E1129E40F1E2F8DB7B46867B3E49AE2556F04C1CFE1FBF5EE3C149B63BD9`.
  Current `source/ega1/ega1-4.tex`: 33,365 bytes / SHA-256
  `55FCE2B2C9A51F7FC86DCEB1A8E0BD4EC6E06818C28E302FFE045B4CA323B275`.
  New author-text corrections, new English mathematical edits,
  source-fidelity repairs, and unsupported reversals are zero. English
  decision ledger: 10 rows / 2,954 bytes / SHA-256
  `979851360743216CD781D3F08CC0174EFA8E3B0A6498DB5C8515FFD6A4AFB988`.
- R54 manifest: 127 files / 7,280,872 bytes; 40,800 bytes / SHA-256
  `9A53F6C16D4DD5D366696988C95321DCE2062E1010CF981526C7233296F541A4`;
  canonical tree SHA-256
  `E8331E55DEABD57007298B17012BE1E50C20370837535F413F3679EBE3FB646B`.
  Independent replay reports zero hash/size/order errors and zero changed,
  added, or removed rows from R53. Full diff validation is PASS/errors empty
  at 7,092 bytes / SHA-256
  `BA53F085977613E2ABA88B3CF943837204E3BBB9A9C2D1EFF80D59891EA8B43C`.
- The bounded projection has 233 lines exactly matching live `ega1-4.tex`
  lines 18--250 and one balancing close. Its initially over-escaped balancer
  was caught and corrected before build without touching live source.
- Final bounded build: 17 pages / 144,319 bytes / SHA-256
  `5BF1482C1EB63A89EAADB179DEB06C10B4F88D49116C462AB46C919AECAC17E1`;
  physical pages 16--17 pass serialized 600-dpi inspection. The two
  PDF-string warnings and two overfull boxes are inherited; the log has zero
  hard errors.
- Temporary `Q:` mappings were removed after use. All 16 workflow/resource
  entries are preserved at SHA-256
  `B4765811FDBA57F5747F249A1249DDAA0290F20E20E5E54757063B11BE7D9493`;
  no XeLaTeX process remains and none of the workflow events changed English
  source.
- Next paired cursor: NUMDAM PDF one-based p.124 / printed p.125,
  continuation of Proposition 4.3.1 after French `la restriction de
  $\alpha\times_S\beta$`.

## 2026-08-03 -- paired French recheck, EGA I printed p.125

- Direct comparison used one 1,100-dpi NUMDAM p.125 context image, 4,462,107
  bytes / SHA-256
  `B1C2D6C0BD2C5538DC3E65EF64304E7CBFD6B6D936ADEB6319826F2D833B8616`.
  No OCR, crop, batch render, whole-page original-detail load, unbounded
  search, or agent was used.
- The completion of Proposition 4.3.1, Corollary 4.3.2, subsection 4.4,
  Proposition 4.4.1, and the inverse-image terminology through the p.125
  terminal phrase are source-grounded as inherited. The p.125 and p.126
  marker placements follow the same semantic seams. The explicit p.122
  correction of the reversed `\theta^\sharp` direction is carried and
  visible but is not a new p.125 correction. No English source byte changed.
- Current `source/ega1/ega1-3.tex`: 56,933 bytes / SHA-256
  `55C1E1129E40F1E2F8DB7B46867B3E49AE2556F04C1CFE1FBF5EE3C149B63BD9`.
  Current `source/ega1/ega1-4.tex`: 33,365 bytes / SHA-256
  `55FCE2B2C9A51F7FC86DCEB1A8E0BD4EC6E06818C28E302FFE045B4CA323B275`.
  New author-text corrections, new English mathematical edits,
  source-fidelity repairs, and unsupported reversals are zero. English
  decision ledger: 10 rows / 2,897 bytes / SHA-256
  `5BF77F44C13123E01245F52C2F44C6046120FFC6B8973B6BB7E3D1709F40E068`.
- R55 manifest: 127 files / 7,280,872 bytes; 41,158 bytes / SHA-256
  `2C76ACD405EDA12EF0D89A89FFF7388410B770F4940C9F55EC8476859218E165`;
  canonical tree SHA-256
  `E8331E55DEABD57007298B17012BE1E50C20370837535F413F3679EBE3FB646B`.
  Independent replay reports zero hash/size/order errors and zero changed,
  added, or removed rows from R54. Full diff validation is PASS/errors empty
  at 7,453 bytes / SHA-256
  `38C475CFA262D891E3747AFF0FF517E3E81602ADBFA733131602F30B6F412A31`.
- The bounded projection has 281 lines exactly matching live
  `ega1-4.tex` lines 18--298 and no balancing addition.
- Final bounded build: 18 pages / 150,482 bytes / SHA-256
  `27703818224457A02D4AB5C0C69B919FAE515324520F7A40293FEEB08130996E`;
  physical pages 17--18 pass serialized 600-dpi inspection. The two
  PDF-string warnings and two overfull boxes are inherited; the log has zero
  hard errors.
- Temporary `Q:` mappings were removed after use. All 13 workflow/resource
  entries are preserved at SHA-256
  `6C43336E861955435F203EAA89EA40E4F53B9B7FC9274748380E35115B93612E`;
  no XeLaTeX process remains and none of the workflow events changed English
  source.
- Next paired cursor: NUMDAM PDF one-based p.125 / printed p.126,
  continuation of the inverse-image terminology after French `qui s'accorde
  avec celle introduite`.

## 2026-08-03 -- paired French recheck, EGA I printed p.126

- Direct comparison used one 1,100-dpi NUMDAM p.126 context image, 5,448,546
  bytes / SHA-256
  `7ADA8D9A25FCFAC30112DBD4744EB192F32BA63F7FD80500DEA9B063173C1DDA`.
  No OCR, crop, batch render, whole-page original-detail load, unbounded
  search, or agent was used.
- The inverse-image consequences 4.4.2--4.4.6, subsection 4.5, Definition
  4.5.1, and the p.126 opening of Definition 4.5.2 are source-grounded.
  Direct authority confirms the printed 4.4.5 algebra-direction error;
  inherited English correctly says (A) is a (B)-algebra and exposes the
  official correction with `Err₂`.
- One inherited formula-fidelity error was repaired in Corollary 4.4.6:
  `f^*(\sh{K})\subset\sh{J}` became
  `f^*(\sh{K})\sh{O}_X\subset\sh{J}`, matching direct French,
  Proposition 4.4.5, and parallel corpus uses in 5.2.4 and 10.5.
- Current `source/ega1/ega1-3.tex`: 56,933 bytes / SHA-256
  `55C1E1129E40F1E2F8DB7B46867B3E49AE2556F04C1CFE1FBF5EE3C149B63BD9`.
  Current `source/ega1/ega1-4.tex`: 33,373 bytes / SHA-256
  `CE8036FF9EF584DD794C7D4925EA62FE7937229E57212873B1C25DE68F8715A5`.
  One unique inverse reproduces the R56 source at 33,365 bytes / SHA-256
  `55FCE2B2C9A51F7FC86DCEB1A8E0BD4EC6E06818C28E302FFE045B4CA323B275`.
- R57 manifest: 127 files / 7,280,880 bytes; 41,920 bytes / SHA-256
  `A8C6D3E4AA6E478CBFCD1A144C6460D9DF03195C09758C713C9CC4C0048739A1`;
  canonical tree SHA-256
  `C22FBDE03D3833584E83A448F5BB74B51399798C4B1E1C82769659211DCAE1E2`.
  Independent replay reports exactly one changed source row from R56 and no
  added or removed path. Full diff validation is PASS/errors empty at 8,647
  bytes / SHA-256
  `421DC3016B112F2CD3E1CA92A3E7C76E4FA438B44C83B05C98CD280048C251B5`.
- English decision ledger: 15 rows / 5,172 bytes / SHA-256
  `A4F7CB99DD848E81EB82EC772FF65DDD9F8F5CE8DA6039EA95A43C03E3FF780C`.
  The first 353 projection lines equal repaired live `ega1-4.tex` lines
  18--370; one final `\end{definition}` balances the bounded build.
- Final repaired build: 19 pages / 156,047 bytes / SHA-256
  `D3B4CA5FC24BE58C62C3E602953E6FE78AF20B7AA7B39834364228DD6AD5E534`;
  physical pages 18--19 pass serialized inspection, and both the Err-II
  marker and restored (\mathscr O_X) factor are visible. The two PDF-string
  warnings and two overfull boxes are inherited; hard errors are zero.
- The pre-repair PDF is retained only as superseded detection evidence.
  Twenty-one workflow/resource entries are preserved at SHA-256
  `4F508B34BE1E897DE19669F85C7783AA25A463DBCCAB66C275BB1605D2DD2153`.
  No XeLaTeX process or `Q:` mapping remains.
- Next paired cursor: NUMDAM PDF one-based p.126 / printed p.127,
  continuation of Definition 4.5.2 after French `un isomorphisme local en`.

## 2026-08-03 -- corrected scope receipt and p.127 production hold

- The full source-task thread `[PRIVATE_TASK_376B7BA66C40]`, its
  initial attachment, the complete successor handoff read order, both live
  STATUS/LOGBOOK histories, the controlling normalization/reversal policy, the
  current pre-Stacks scaffold, and the dual-DOI logbook rule were reread through
  EOF before this entry. The detailed audit, historical/current handoff-binding
  distinction, transcript lessons, and exact live hashes are recorded in the
  paired French `LOGBOOK.md` under “full source-thread reread, scope correction,
  and production hold.”
- The previous durable goal was deleted because it omitted an explicit
  pre-Stacks/Stacks deliverable. The corrected English scope is not merely a
  translated reader: every functional departure from direct NUMDAM French must
  have an individual reversible rationale, every active standalone and
  cumulative/global source must be repaired together after a reversal, and the
  English layer must attach to the same stable bilingual semantic IDs,
  statement/proof/formula/diagram nodes, terminology bindings, typed
  dependencies, and correction provenance as diplomatic French.
- During source work, capture source-certain semantic anchors without stalling
  continuous transcription. At meaningful cumulative/final checkpoints,
  regenerate the co-current standalone/global readers, ordinal source
  manifests, exhaustive reference/coordinate and target/edge/residual replay,
  semantic indices, privacy-clean logbooks, rights/caveats, package/handoff,
  and authorized public readback. After canonical French/English freeze, deepen
  the shared graph into the requested Stacks-style reconstruction. Do not claim
  completed Stacks exposition or formalization from the preparatory scaffold.
- P.126 remains the last sealed paired checkpoint. P.127 English is unsealed at
  `source/ega1/ega1-4.tex`, 33,644 bytes / 413 lines / SHA-256
  `C933CDFEB1C7F64B0BFFB8D510A732349B196E3E53B8044A70098D999CAB1BF8`.
  R59 independently replays 127/127 files / 7,281,151 bytes / canonical tree
  SHA-256
  `BF73FCED73F50B5A18F310A4206EC14955E1DC8512BD50DC6847BCE60A19005D`,
  but no p.127 validation/status/logbook closure exists. Production stays held
  until the corrected durable goal and both logbook receipts are reported.
- The exact corpus is the eight bounded NUMDAM EGA publications EGA I, II,
  III-1, III-2, and IV-1 through IV-4, with Chapter 0 inside EGA I. Deligne,
  SGA, FAC, and GAGA are excluded. Do not duplicate the completed standalone
  EGA IV archive handoff or perform any upload/archive mutation without
  separate authorization.
- Pre-append identity of this English logbook: 127,929 bytes / 2,155 lines /
  SHA-256
  `4315C3DE7066D234078714601FCA7DF1BE10140A72B0CB5E3775EB0F884BFD3E`.
  Removing only this appended receipt must reproduce that predecessor.

## 2026-08-03 -- paired French recheck, EGA I printed p.127 sealed

- Direct authority confirms the p.127 inherited English except for two
  necessary interventions in proof 4.5.5: typed transitivity citation
  `(4.2.5)` against printed `(4.2.4)`, and introduction of `z,z'` omitted by
  French. Both are now visibly disclosed in translator footnotes; no other
  functional departure or source-fidelity repair was admitted.
- Current `source/ega1/ega1-4.tex`: 33,644 bytes / 413 lines / SHA-256
  `C933CDFEB1C7F64B0BFFB8D510A732349B196E3E53B8044A70098D999CAB1BF8`.
  Removing the two unique notes exactly reproduces R58 at 33,373 bytes /
  SHA-256
  `CE8036FF9EF584DD794C7D4925EA62FE7937229E57212873B1C25DE68F8715A5`.
- R59 is 42,723 bytes / SHA-256
  `3D874D60FA7AB1CE4C0A0496BD20C3B096481E0A35463D851ACD295CCBD08569`:
  127 files / 7,281,151 bytes / ordinal tree SHA-256
  `BF73FCED73F50B5A18F310A4206EC14955E1DC8512BD50DC6847BCE60A19005D`.
  Independent replay has zero row/membership/order error. R59 diff validation
  is PASS/errors empty at 7,763 bytes / SHA-256
  `C68E010B34CF050695FCDC5AC8A1AC5F405A4AC05661A0558979214547426C73`.
- The section-4 projection exactly equals live `ega1-4.tex` lines 18--413;
  the section-5 projection exactly equals live `ega1-5.tex` lines 1--12.
  Final bounded PDF: 19 pages / 161,909 bytes / SHA-256
  `E344A519B0DDC19DF372296FA1829FBBCAE0BEC68EDDE4FD0A60BCB60A938BD6`.
  Physical page 19 passes serialized inspection with both notes visible and
  no clipped, overlapping, broken, or unreadable content. Hard errors are zero;
  the two PDF-string warnings, two overfull boxes, and bounded undefined-
  reference summary are inherited.
- The shared pre-Stacks p.127 block binds the bilingual slices, statement,
  proof, source-error, terminology, and dependency nodes at SHA-256
  `5DD244CCB3A223D0EEDB67E233027A1A338ACD24232C7639023723F8B98BACBC`.
  R50 combined validation is PASS/errors empty at 11,010 bytes / SHA-256
  `D631DC20C4EF98C822AA61FF29A02176382A23E40077C1D36338FE359E80EA25`.
  Next paired cursor is printed p.128, proof of Proposition 5.1.1.

## 2026-08-03 -- paired French recheck, EGA I printed p.128 sealed

- Direct p.128 authority admits the proof of 5.1.1 through the opening of
  5.1.5. English receives exactly two source-fidelity repairs in
  `ega1-5.tex`: `mathfrak I subset mathfrak j_x` replaces the inherited
  left-hand stalk subscript, and `thus means` restores French `signifie` as a
  defining equivalence. The French printed 5.1.2 word-order defect is logged;
  inherited English already resolves it grammatically without altering the
  mathematics.
- Current `source/ega1/ega1-5.tex`: 46,829 bytes / 828 lines / SHA-256
  `D3BB566847A24BD268157D7171BD9F5B282FA2C9B8F4D1A1ABD9B84F656FEFF3`.
  Two unique inverse substitutions reproduce R60 exactly at 46,833 bytes /
  SHA-256
  `1585EC164F57E55BA86264F86F428523D7659442AAE5046D43D9E5FA49B5F777`.
- R61 is 43,455 bytes / SHA-256
  `D7EFC8554A3B01C0FD5D715131B553EC95701D718FE7683315EFBA5FA0F219EE`:
  127 files / 7,281,147 bytes / ordinal tree SHA-256
  `658ACB58DBE08F3641410EF071EBA6D80DB628C0560940DF6BEFE8AFBAF091AD`.
  Independent replay has zero row, membership, size, hash, or order error.
  R61 diff validation is PASS/errors empty at 9,672 bytes / SHA-256
  `BD43E7FD61B33CC687B09F1EF7F51FF8E6CB5CEC2B5090B78A291A85A5761C0D`.
- The section-5 projection is exactly live lines 1--68, 4,685 bytes / SHA-256
  `009A2F2E53F459D6D7901B4D8F6928FFA7254216582E455373F2210851BC4485`.
  One wrapper-local `end-env` balances the page-open environment without
  mutating live source. Final bounded PDF: 20 pages / 166,762 bytes /
  SHA-256
  `B033E23E0E5FDD50DBAC6404E752636BDB7BC99E8B62383AB70816A6E6C45614`.
  Physical page 20 passes direct visual inspection with both repaired readings
  visible and no clipped, overlapping, broken, or unreadable content. Hard
  errors are zero; the two PDF-string warnings, two overfull boxes, and
  bounded undefined-reference summary are inherited.
- The shared p.128 pre-Stacks block binds the bilingual slices, proof,
  terminology, definition, equivalence, consequence, source-error, correction,
  and continuation nodes at 55,476 bytes / SHA-256
  `387C86432463544C2DB0B5146A1164F07A4AF49D3876FFA1C50655E7333DFF09`.
  Decision ledgers are French 2,521 bytes / SHA-256
  `F8B4BBED89CD3F39161ED3FA1312D036F59110E030E3C5098871B945BDEF2CA3`,
  English 4,339 bytes / SHA-256
  `002D5CA696A0D85152DC7B5858FC0829437B74DA6C544FBFEF46209EEAE3AD07`,
  and workflow 10,113 bytes / SHA-256
  `F2B03BFD6A91BE884EBCA88A40F57965A14A486862BB18EECEC76192407D546E`.
- The independent manifest replay found four generated products under literal
  English `source/$out`; their hashes are retained, and only that verified
  directory was removed. All output-routing, balancing, projection-metadata,
  helper-name, PDF-tool, and control-filename retries are explicit in the
  workflow ledger. Temporary `Q:` mappings were removed and no XeLaTeX process
  remains. No global build, publication, upload, or archive action occurred.
- R51 combined validation is PASS/errors empty at 10,926 bytes / SHA-256
  `94F833E316F3726489EEF9254871BB55B12EBA691B7BFEAF918F76C285A7DE41`.
  Next paired cursor is printed p.129, continuation of 5.1.5 after
  `l'homomor-`; remove only the temporary French final `end-env` first.

## 2026-08-03 -- paired French recheck, EGA I printed p.129 sealed

- Direct authority confirms the reduced-morphism functoriality and naturality
  square in 5.1.5, preservation results in 5.1.6, the product comparison in
  5.1.7, Corollary 5.1.8, and the nilpotent-product warning. No English source
  edit, new source error, unsupported correction, or unresolved reading is
  admitted. Established omega-flat, residue-field, and page-seam notation is
  retained.
- Current `source/ega1/ega1-5.tex`: 46,829 bytes / 828 lines / SHA-256
  `D3BB566847A24BD268157D7171BD9F5B282FA2C9B8F4D1A1ABD9B84F656FEFF3`.
  The p.129 slice is exactly live lines 69--125, 3,457 bytes / SHA-256
  `1613516E5198693420370041667CE6EC2B8B2C67209B6501722684839729D779`.
- R63 is 44,173 bytes / SHA-256
  `13659CCA1A6298345AC1EF029422A1BD4ADCFCDD75763B9D0331B7846ED58605`:
  127 files / 7,281,147 bytes / unchanged ordinal tree SHA-256
  `658ACB58DBE08F3641410EF071EBA6D80DB628C0560940DF6BEFE8AFBAF091AD`.
  Independent replay has zero row, membership, size, hash, or order error and
  no R62 delta. R63 validation is PASS/errors empty at 8,581 bytes / SHA-256
  `0AC289389C15769AC85CEF5AD442CCDAE0B9BF77226EF48666BC0DB8AF5F250E`.
- The p.128 prefix plus p.129 continuation exactly reproduce live lines 1--125
  at 8,142 bytes / SHA-256
  `9BEF395F1E37CFFC7819B25487C4A9F54B8505FE547E2131752EAB830A565B78`
  with no balancing addition. Final bounded PDF: 21 pages / 171,271 bytes /
  SHA-256
  `2B568041BF9DF9E7EADA134DF4986696BA4472B6B50A982E8E38B62696B2686D`.
  Physical page 21 passes visual inspection with no clipped, overlapping,
  broken, or unreadable content. Hard errors are zero; inherited diagnostics
  are unchanged.
- The shared p.129 pre-Stacks block binds the reduced-functor, diagram,
  preservation, product, corollary, warning, and English-confirmation nodes at
  58,492 bytes / SHA-256
  `88D8A1AF0020C8F0561F837B9C01DB7494FBD7CE4193B215A44645E9DCE9BA19`.
  Decision ledgers are French 2,134 bytes / SHA-256
  `17270D6F74A26E3916ECEC8EEA53D2B2327F252DCEA14C1267E53DE36516AB91`,
  English 2,239 bytes / SHA-256
  `4B5E9FA82FFD01C936C2F0E22B62FCCD24D534B62C39E2AC37578BF193D64D1E`,
  and workflow 5,454 bytes / SHA-256
  `3BA6C0B6D2EEB7F7FDF79D715C11486B61D61BEBBDFA35B3E4D26CA7E24AB674`.
- Both read-only PowerShell parser retries are explicit in the workflow ledger
  and changed no source or artifact. Temporary `Q:` mappings were removed and
  no XeLaTeX process remains. No global build, publication, upload, or archive
  action occurred.
- R52 combined validation is PASS/errors empty at 10,074 bytes / SHA-256
  `2A69BDB7C8D978A1BC2864A66A738A5C7450A3DE567EB7A67A937817EB1E2902`.
  Next paired cursor is printed p.130, Proposition 5.1.9; no temporary French
  close must be removed.

## 2026-08-03 -- paired French recheck, EGA I printed p.130 sealed

- Direct authority confirms Proposition 5.1.9 through the square-zero
  reduction, exact sequence (5.1.9.1), global ideal construction, canonical
  affine comparison morphism, two diagrams, and five-lemma argument. No
  English source edit, new source error, unsupported correction, or unresolved
  reading is admitted.
- Current `source/ega1/ega1-5.tex`: 46,829 bytes / 828 lines / SHA-256
  `D3BB566847A24BD268157D7171BD9F5B282FA2C9B8F4D1A1ABD9B84F656FEFF3`.
  The p.130 build continuation is exactly live lines 126--177, 3,172 bytes /
  SHA-256
  `AB1B318C93CEB0F2CA17E6DF96C5C438F27AD5E4390D296E67BB0F6A4B2EEC56`.
  Established `I`, `K`, and `vphi` notation is retained. The English sentence
  keeps `H^1(X,I)=0` before its p.131 marker while French places the formula on
  p.131; the reversible seam decision is explicit.
- R65 is 44,891 bytes / SHA-256
  `76207E6D99DA99033EB431B51886630B4A917FDEEDEE29308FD97FBE2DCDE7F0`:
  127 files / 7,281,147 bytes / unchanged ordinal tree SHA-256
  `658ACB58DBE08F3641410EF071EBA6D80DB628C0560940DF6BEFE8AFBAF091AD`.
  Independent replay has zero row, membership, size, hash, or order error and
  no R64 delta. R65 validation is PASS/errors empty at 9,004 bytes / SHA-256
  `498854BC46966003417E66D90A21777E3B62DEB7729244C45E064AF467D7A287`.
- All section-5 projections reproduce live lines 1--177 at 11,314 bytes /
  SHA-256
  `C48CBD81D34FB48E0B8756F6B9C23960B3E207A466FD68C54FF69787F2E51D08`
  with no balancing addition. Final bounded PDF: 22 pages / 176,102 bytes /
  SHA-256
  `5989A16F1CB50EF183F849C55E64C0DBB79468CDDF385E70583C0C470F349BD2`.
  Physical pages 21--22 pass targeted visual inspection with no clipped,
  overlapping, broken, or unreadable content. The new 11.2554 pt warning is
  bounded and visually harmless.
- The shared p.130 pre-Stacks block binds the nilpotent-thickening,
  square-zero, exact-sequence, ideal, canonical-map, diagram, five-lemma,
  continuation, and English-confirmation nodes at 61,902 bytes / SHA-256
  `2D2E022FCF22DC3C47278D7273F4B6B4BB79DDD0BFE73D87E65628D520E1E66A`.
  Decision ledgers are French 2,300 bytes / SHA-256
  `B194FDA4EC7E739E8E21667EE99D732E877CDF872FA6AD8969F9BDEF4CA986CC`,
  English 2,247 bytes / SHA-256
  `FC3BFC8EA3B73DE3693139C1807312FCD3115F3972481BC0D9D58A8F17A68904`,
  and workflow 6,362 bytes / SHA-256
  `2DD72D9B2ED6839E63DB8556CCF479D1741CF8FD6D0F62E3EF050FF0962823A6`.
- The read-only marker and checkpoint-order verifier retries, corrected
  handoff placement, and targeted second reader page are explicit in the
  workflow ledger. Temporary `Q:` mappings were removed;
  no XeLaTeX process or literal `source/$out` remains. No global build,
  publication, upload, or archive action occurred.
- R53 combined validation is PASS/errors empty at 10,676 bytes / SHA-256
  `BDD7227EE137F2B61A57438AB84D3B564131AD214C9A1F8AFD918CE7A2472F8F`.
  Next paired cursor is printed p.131, continuation of Proposition 5.1.9 after
  `ce qui résultera de`; no temporary French close must be removed.

## 2026-08-03 -- paired French recheck, EGA I printed p.131 sealed

- Direct authority confirms the completion of Proposition 5.1.9, Lemma
  5.1.9.2, Corollary 5.1.10, Propositions 5.2.1--5.2.2, and the statement of
  Corollary 5.2.3. One author-text error is admitted: the French local
  splitting formula prints `F|Y`, while restriction to the neighbourhood `V`
  requires `F|V`. Diplomatic French preserves `F|Y`; English retains `F|V`
  and adds one immediately visible translator footnote.
- Current `source/ega1/ega1-5.tex`: 46,962 bytes / 828 lines / SHA-256
  `89CB70021FE8386126FAAEBFE2C823A07A71F177BEEB8AD0862209391111E543`.
  The p.131 projection is exactly live lines 178--238, 3,856 bytes / SHA-256
  `B8C9CC0121AC191F2AA7585204797D1E398BEA228B74EF5D9F5F6B27E6AFB4B8`.
  All section-5 projections reproduce live lines 1--238 at 15,170 bytes /
  SHA-256
  `011C647717CF82BC45CA3AA9C41A60AAFBE410FE779DD0D1DB9C1BDE67F124AD`
  with no balancing addition. Removing the unique note reproduces the sealed
  R66 file exactly.
- R67 is 45,669 bytes / SHA-256
  `F9DF2387D0B08F4269B8307DCD7268DD93AA47706F5B024967ED6D8149571EE1`:
  127 files / 7,281,280 bytes / ordinal tree SHA-256
  `B12D07B194C59E154BE7F7DB383C9B52E0AC6E4ADCAEEF9E0E567522090558A7`.
  Independent replay has zero row, membership, size, hash, or order error and
  exactly one R66 delta, `ega1/ega1-5.tex`. R67 validation is PASS/errors
  empty at 9,356 bytes / SHA-256
  `3AC5F994DC237FDDBCCF5A839D5B5212502B5560F1D92AAD366AB6971B106EAE`.
- Final bounded PDF: 23 pages / 181,229 bytes / SHA-256
  `7B5CB44FE6196E36B3475D879A59F6013EF38C52C054E5B0FE071602C2237057`.
  Physical page 22 passes visual inspection with the translator note visible;
  page 23 passes text-layout inspection. There is no clipped, overlapping,
  broken, or unreadable content.
- The shared p.131 pre-Stacks block binds the cohomology, extension,
  `F|Y`/`F|V`, reduction, reduced-subscheme, factorization, and continuation
  nodes at 65,174 bytes / SHA-256
  `57EC4614738F849349AC91BC57EDC92E85D17B92CCC33F9AE6A57C6A80BBBCB8`.
  Decision ledgers are French 2,558 bytes / SHA-256
  `C22B1C247490E56610CB584D9F4B104CF79F060C21FD21158A75B9CE5E598547`,
  English 2,308 bytes / SHA-256
  `DF223382341C820F9DA7D5AA71DCE8982B564C5DA4AD29D86EE65B31D9770E15`,
  and workflow 11,870 bytes / SHA-256
  `6286274C0B1502E61D26F9D34C85A937FE2BED30903225D030BB6A769BC0D63F`.
- The workflow preserves all renderer, metadata, projection, placement,
  parser, path, and obsolete-wrapper retries. The final French r2 wrapper
  retires only one build-only placeholder and changes no source byte. No OCR,
  global build/render, publication, upload, or archive action occurred; no
  XeLaTeX process or `Q:` mapping remains.
- R54 combined validation is PASS/errors empty at 11,936 bytes / SHA-256
  `4B51F8C9B847D1D4A3C8C759CAEE6E09DD1F5EA00D5291E9623A44AF69990AA4`.
  Next paired cursor is printed p.132, proof of Corollary 5.2.3; no temporary
  French close must be removed.

## 2026-08-04 -- paired French recheck, EGA I printed p.137 sealed

- Direct NUMDAM authority confirms the completion of Proposition 5.5.1 and
  its reduction diagram, Corollaries 5.5.2--5.5.3, Proposition 5.5.4 and its
  proof, and the irreducible-component reduction. The authority image is
  5,057,783 bytes / SHA-256
  85D4DC363A051C5EA7D369D41B0756B13FB29BBC286EF1F77505E32A2B3A109E;
  no OCR was run.
- The paired recheck made three separately ledgered and reversible English
  repairs: visible (3.3.9.1) now links to exact target I.3.3.9.1; Delta_X is
  below the lower diagram arrow as printed; and “leads to the idea of
  separation” is replaced by an actual reduction claim matching ramène.
  Current source/ega1/ega1-5.tex is 47,345 bytes / 827 lines / SHA-256
  BE2123101A28F8BEB6BBB5B32FC09CCA17F1B01BA491C9799229D9810B89BE2E.
  Exact inverse replay restores R79 at 47,337 bytes / SHA-256
  520D28FBEE094AFC930E09D6A27ED8257D4E4F802FAAE0E2C5135F8F8641D798.
- R80 is the complete one-row successor of R79: 127 files / 7,281,663
  bytes, manifest 50,731 bytes / 1,114 lines / SHA-256
  1ECABBC856950C7EDB083D9FA502DBF86F68B56D74C2AB84F6AE460704D93F7B,
  canonical tree SHA-256
  E179D8E2393A34B50CA89B4C26616FE685F0A96FE74F5F91B20A921689CA3FFB.
  Independent ordinal replay passes with exactly one changed source row and
  no added or removed row.
- Exact live lines 622--680 are 3,499 bytes / SHA-256
  A67BE199B4179065BF5BE53CAEC3C9639BD95B5D3B00635CA2BD90DB1736CEBD.
  The exact lines 239--680 projection is 21,204 bytes / SHA-256
  0F477657D318698B5FB3FEBBD90E6768AD3AB7AFB93432A17F88699892FDCCB2
  with no balancing addition. The three-pass English PDF is 28 pages /
  211,829 bytes / SHA-256
  2A041B3BAD2EB9F64BE88FE8A4E9F5B3A881FADC84FD53AA4ED894B360B37B62;
  pages 27--28 pass text-layout QA with the diagram and reduction visible.
- Paired French source is 38,044 bytes / SHA-256
  9F316E9901A7DC8F069853E0DC3A9061FA49779CB59CE2016CFF95B2D11FD4BE;
  its 40-page bounded PDF has SHA-256
  480AA13E0D0694556D4AA2FA5025754F421513D62B8581D44C08276CD68B87F4
  and page 40 passes visual QA.
- The p.137 scaffold is 92,172 bytes / 1,571 lines / SHA-256
  248460C70D5B42F30E254761EC31C30F9F3AD6EFAFDFC41C768AEC50581D10C6.
  French, English, and workflow ledgers parse at 9, 10, and 20 rows; the
  workflow SHA-256 is
  C07847BA8242D286A7303249DAF56E85DFC3070623A633AFB56330819CD9663C.
  The adverse attempts, including the accidental read-only broad lane search,
  remain explicit with no-mutation resolutions.
- English R80 validation is PASS/errors empty at 10,978 bytes / 249 lines /
  SHA-256
  4034C5B336955026E9210E7D2FD3EFC5EBF4A8FA4C93C68BF45FFD4B119AA93C;
  French R60 is PASS/errors empty at 12,962 bytes / 277 lines / SHA-256
  A91D65AB7FCA43D68A6AF62301105872ED5A61EDC938B98BDFE2C50DE694B999.
  No OCR, global build/render, publication, upload, archive, remaining
  XeLaTeX process, temporary source/$out, or Q: mapping remains.
- Next paired cursor: create and independently replay R81, then direct NUMDAM
  PDF one-based p.137 / printed p.138, beginning Proposition 5.5.5. No
  temporary French close must be removed.

## 2026-08-03 -- paired French recheck, EGA I printed p.132 sealed

- Direct authority confirms the proof of 5.2.3, Corollary 5.2.4, diagonal
  items 5.3.1, 5.3.2, and 5.3.4, and Proposition 5.3.5 through diagram
  (5.3.5.1). One author-text omission is admitted: French prints
  `f:X→S, Y→S`, while `π=f∘p=g∘q` and the diagram require `g:Y→S`.
  Diplomatic French preserves the omission; English retains `g` and adds one
  immediately visible translator footnote.
- Initial bounded-reader layout found the inherited empty 5.3.3 environment
  rendered a stray period. Direct French jumps from 5.3.2 to 5.3.4. The final
  source replaces the empty environment with `\phantomsection`, keeps label
  `I.5.3.3`, and emits no visible 5.3.3 text. Current `ega1-5.tex` is 47,147
  bytes / 827 lines / SHA-256
  `F28E52859F1D3CF5393BEED2D882180197D6B27DF81976E343864863B9DF821F`.
  The two logged inverse operations restore exact R68.
- R70 is 46,901 bytes / SHA-256
  `18F2EF15DF53015AE384D8CD148FBF4D8B378A82C5CE0A90F6FA398D0DF2B952`:
  127 files / 7,281,465 bytes / ordinal tree SHA-256
  `49B83F1B0ED89440DCC3759038AC626EED7C2C869766D1D6D1E55B07E448F210`.
  Independent replay has zero row, membership, size, hash, or order error and
  one cumulative R68 delta, `ega1/ega1-5.tex`. R70 validation is PASS/errors
  empty at 11,413 bytes / SHA-256
  `9218CF601B450135DB63656B3E6A66E638FF33368792BA6C0F5A7B50FF71D740`.
- The final p.132 projection is exact live lines 239--320 plus one temporary
  `\end{proposition}`, 3,597 bytes / SHA-256
  `A371A89C1EEF3922B618F0BC32E0F005A1E667F752B57844267BB48ECD26F773`.
  Final r2 PDF is 23 pages / 186,413 bytes / SHA-256
  `D34DD7AE50939B003451C06CBA06BD7E8788F533197D846415A92EE1002E5A1E`.
  Page 23 passes visual inspection with the footnote visible, the stray period
  absent, diagram complete, and no clipped, overlapping, broken, or unreadable
  content.
- The shared p.132 pre-Stacks block binds the two source decisions, diagonal
  identities, numbering gap, diagram, and continuation at 69,454 bytes /
  SHA-256
  `EB95123847A5B6B08D50C20ECF0857D31E0D3E3599D15153FECEF8EEC3E58E82`.
  Decision ledgers are French 3,069 bytes / SHA-256
  `D3EF82B165D8F351F62F098C6511B13F5D2B39581348C3CFD3482A7D4E62EA20`,
  English 2,805 bytes / SHA-256
  `6F433E72C6281D4237D31E9336093BE8595201186E5CCC7362EC0DD782E79040`,
  and workflow 11,957 bytes / SHA-256
  `8A129466B462CF28A5D1B9EE5CAD71BD58218026192C12C3B94AC660917F0BE4`.
- The workflow preserves the R68/R69/R70 chain, path and parser retries,
  scaffold placement correction, diagnostic r1 reader, and r2 fidelity repair.
  No OCR, global build/render, publication, upload, or archive action occurred;
  no XeLaTeX process or `Q:` mapping remains.
- R55 combined validation is PASS/errors empty at 12,290 bytes / SHA-256
  `C97366E68C0A41EF8D55E74D17F01A661A274F7850BB9EE24C897D1F67996C7A`.
  Next paired cursor is printed p.133, after removing only the temporary final
  French `\end{proposition}`, then continuing with `est commutatif`.

## 2026-08-03 -- paired French recheck, EGA I printed p.133 sealed

- Direct authority confirms the completion of Proposition 5.3.5,
  Corollaries 5.3.6--5.3.7, Propositions 5.3.8--5.3.9, and Corollaries
  5.3.10--5.3.11. French Proposition 5.3.8 says that `X(Z)_Y` is likewise
  reduced to one element after injecting it into the singleton `Y(Z)_Y`.
  Since the source set may be empty, English retains “at most one element”
  and adds one immediately visible translator footnote naming the French
  wording.
- Current `source/ega1/ega1-5.tex` is 47,337 bytes / 827 lines / SHA-256
  `520D28FBEE094AFC930E09D6A27ED8257D4E4F802FAAE0E2C5135F8F8641D798`.
  Removing only the unique 190-byte p.133 note restores exact R71 at 47,147
  bytes / SHA-256
  `F28E52859F1D3CF5393BEED2D882180197D6B27DF81976E343864863B9DF821F`.
- R71 is the complete pre-edit gate: manifest 47,259 bytes / SHA-256
  `5C2864AB0D734217A601220A5702D3C1077AA1C2ACF6522B882979981FBDB65A`,
  127 files / 7,281,465 bytes / tree SHA-256
  `49B83F1B0ED89440DCC3759038AC626EED7C2C869766D1D6D1E55B07E448F210`.
  R72 is 47,710 bytes / SHA-256
  `1942000C1077F279EC63EE894E15F0830C925753E3ADC0A5E18370B3DF948C2A`:
  127 files / 7,281,655 bytes / tree SHA-256
  `29EB38A85D6F0DEC1644A9B2C4AA2A52D7185A83875E115B6AD0C44C627F9D37`.
  Independent replay has zero row, membership, size, hash, or order error and
  exactly one R71 delta, `ega1/ega1-5.tex`. R72 validation is PASS/errors
  empty at 9,300 bytes / SHA-256
  `4B637E88F650B3479D9F6545361D7895A4B0145BEE9B81425826C64387595C21`.
- The p.132--p.133 seam projection is exact live lines 239--401, 7,292 bytes /
  SHA-256
  `509C0BCCBE4B7FA86F642D2032B36BD63C662DBF70881E85E1C47A04F91B543F`,
  with no balancing addition. Its p.133 marker slice is 3,713 bytes / SHA-256
  `0F8884F778BD6E84AE70F4812688FB99511FB1D4ADE1E9F6BE7868CAD3A946CF`.
  Cumulative live lines 1--401 are 22,462 bytes / SHA-256
  `20C09CBE4E058340D3E23C26C6377233C358FFA49CB706EDF5F2E62341DA9187`.
- Final bounded PDF is 24 pages / 191,842 bytes / SHA-256
  `5EF5926DA9FFC164E1E60D3228F0F46132F42259D3F66EB8188C0CDC5B73AB7D`.
  Physical page 23 passes text-layout inspection; physical page 24 passes
  visual inspection with the new note visible and no clipped, overlapping,
  broken, or unreadable content.
- The shared p.133 pre-Stacks block binds the completed fibre-product
  universal property, diagonal/monomorphism/separatedness criteria, the
  printed one-element defect, and graph continuation at 72,982 bytes / 1,246
  lines / SHA-256
  `B95A07D25C9773FE9AC06725E4B9833A9E8851EFA9328F76ED8739EF0994EA44`.
  Decision ledgers are French 3,109 bytes / SHA-256
  `AA2FB8063F3093212BEFD7888972AAFB4B924E3CB5191B7FA2192D4247EB1F6B`,
  English 2,285 bytes / SHA-256
  `7A2DBEC3A4474C0FB4FB3ED92D52C9B58D2D47DE038674BD0A080B57200D7EE6`,
  and workflow 7,402 bytes / SHA-256
  `E05C22AC16A379B4E2CF21FCE496EC6DDCE5AF827BB4A080308F0B7F7BCB05A4`.
- The workflow preserves the R71/R72 gate, bounded authority and text-layer
  checks, seam removal, projection/build/QA events, resource closure, and the
  late receipt-tail command-composition failure plus successful retry. No
  OCR, global build/render, publication, upload, or archive action occurred;
  no XeLaTeX process, temporary `source/$out`, or `Q:` mapping remains.
- R56 combined validation is PASS/errors empty at 11,033 bytes / SHA-256
  `025D9BB49D0B2305199EBE54D56822E6CE7E4E38E4AAA93819EC67A560CCB091`.
  Next paired cursor is printed p.134, graph terminology after Corollary
  5.3.11; no temporary French close must be removed.

## 2026-08-04 -- paired French recheck, EGA I printed p.134 sealed

- Direct NUMDAM PDF one-based p.133 / printed p.134 confirms the graph
  terminology, Corollaries 5.3.12--5.3.14, Proposition 5.3.15, and
  Corollary 5.3.16 through z=Delta_Y(y). The 4,681,976-byte authority image
  has SHA-256
  6D57CB50CF18A51FF996D8F71D10516D12E499365B62F2EA8F3B6DAF25F40F8A;
  no OCR was run.
- The inherited English printed-p.134 slice is source-grounded and requires
  no mutation, correction note, normalization, or rejected repair. R73 and
  R74 each replay 127 source files / 7,281,655 bytes to exact tree SHA-256
  29EB38A85D6F0DEC1644A9B2C4AA2A52D7185A83875E115B6AD0C44C627F9D37.
  R74 is 48,428 bytes / SHA-256
  E4A8F263163EE68710CC572F81E63E7A0DBAFC72B728985D2E6519CF27F86D9D;
  R74 minus R73 has zero changed, added, or removed rows.
- The English p.134 projection is 10,700 bytes / SHA-256
  9399F92A8CC4F49BCD546E3C693F9BF0851B260CA3F0FD3F717EF2D66CD3ED33.
  Its first 10,688 bytes reproduce exact live lines 239--472; the sole
  addition is one build-only proof close because the page ends inside the
  proof. The three-pass bounded PDF is 25 pages / 196,609 bytes / SHA-256
  629DF4EF410D01F22290444C82BDD350AB8399D2BD108772E973F5469C968F73.
  Pages 24--25 pass text-layout/visual QA, including the diagram, with no
  clipping or overlap.
- Paired French source/ega1/ega1-5-fr.tex is 27,093 bytes / 629 lines /
  SHA-256
  2BF15FE97B29DE032BB338E83897243673A7CC9C5956049AB1A29E195281DC2F.
  The two-pass French bounded PDF is 38 pages / 352,013 bytes / SHA-256
  1DD0BA9C886D8C3BAFDC8AC3504848B5F180EAAFEC63FF9C2ECD820F1585A052;
  terminal pages pass.
- The p.134 pre-Stacks block is at true EOF, after p.133, at 77,945 bytes /
  1,329 lines / SHA-256
  C2697E538722F21711C2833A524D689CD084E6F283E058AB37FB1AD40BAB5EA3.
  French, English, and workflow ledgers parse at 9, 8, and 23 rows, with
  SHA-256 values
  342FF6BAF4F870B459C209966437144A008C8AB365BE44C2BBF4C9EE10970AE9,
  F4266810E5D1C1D56C373ECEA8349B8751D9E8905D62AE431C546A11CC443B55,
  and
  546920CB0A701EF12C3E8B1FB2CD7405EB5247943D85A7E35C26D21A9D2B332A.
  The workflow preserves both failed receipt-patch compositions and their
  successful bounded successor.
- English R74 validation is PASS/errors empty at 10,891 bytes / SHA-256
  E153071E1444563D15BDF45A440C05A9441CF325D534E04654DDBCB0F2867B34;
  French R57 is PASS/errors empty at 11,389 bytes / SHA-256
  26FAB757B306D0046E7169404721530AF65A9308A23A95CA37A138DB4931E3CC.
  No OCR, global build/render, publication, upload, archive, XeLaTeX process,
  temporary source/$out, or Q: mapping remains. The user-moved unrelated tree
  is [PRIVATE_DOCUMENTS_ROOT]\CHat translates and clean; its former
  Papors\Chatnotes location was not recursed.
- Next paired cursor: create/replay complete R75 before source mutation, then
  direct NUMDAM PDF one-based p.134 / printed p.135, continuing after
  z=Delta_Y(y). No temporary French close must be removed.

### 2026-08-04 -- p.134 retained-raster metadata correction

- The bounded p.134 build-directory listing located
  EGA1_P134_ENGLISH_BOUNDED_CHECK_R1-page25-150dpi.png at 259,908 bytes /
  SHA-256
  390A1151EB9A661083D57C67CD880C7A98326BD95912165C6006E5E8871324DD.
  It was retained before the p.134 seal; the earlier ephemeral/not-retained
  inference is superseded. Source, build, and visual conclusions did not
  change.
- The append-only correction is in the final 25-row p.134 workflow ledger,
  19,178 bytes / SHA-256
  280759893633110B6019F6D6E65E025BB44573CE099380B64B2E4DECF9C24C65.
  Corrected English R74 is 11,546 bytes / SHA-256
  70EE5C3DF4C68F4549EF55E7D6C572998706C32572288653D75932BA50042B7A;
  corrected French R57 is 12,367 bytes / SHA-256
  AA264ADF86D4AF5B1A1BE075DC5293920009B08E57C8218993865E958BF9EC18.

## 2026-08-04 -- paired French recheck, EGA I printed p.135 sealed

- Direct NUMDAM authority confirms the completion of 5.3.16, Corollary
  5.3.17 and both diagrams, Definition 5.4.1, Proposition 5.4.2, and
  Corollaries 5.4.3--5.4.4. The authority image is 4,299,800 bytes /
  SHA-256
  AA876A55EC9FD2FE0B3140B0F00AB9031D7C0D1909146B1B2396CD508126BB0A;
  no OCR was run.
- The inherited English p.135 slice remains byte-identical. The visible
  historical terminology footnote at 5.4.1 is retained and ledgered as
  translator paratext rather than French source. R75/R76 are zero-delta
  127-file manifests; R76 is 49,155 bytes / SHA-256
  67192F831823DB9C25E6951DF7CFB69A69C81422CF594EE33C84C3B3ACB386E3.
- The exact live projection lines 239--551 are 14,244 bytes / SHA-256
  DEA714B7DC7D922B851FF8CB629CD13E46F9A0CB0666DCE0CF92B8119457E779
  with no balancing additions. The three-pass English PDF is 26 pages /
  201,867 bytes / SHA-256
  AB575233DAD6613B4CBFD411C085443EDDDB10967D13D9E2A28996099A2293FE;
  pages 25--26 pass text-layout QA with the diagrams and footnote visible.
- Paired French source is 30,547 bytes / SHA-256
  E1DBCD8A7DEF99161EE00A439D8BC4C1144D57B79DAB4853B0BDC80716B350F5;
  its 39-page bounded PDF has SHA-256
  EECC102968EB25B18C92A369BFCB5350FCB35B4E1651F00F2BA28BA14CF81BA2
  and page 39 passes visual QA.
- The p.135 scaffold is 82,678 bytes / 1,408 lines / SHA-256
  9545858861D9E506F65069F7E65FCD0403D29C78A7DAC4D6A7A7AFE56348E183.
  French, English, and workflow ledgers parse at 9, 8, and 11 rows, with
  workflow SHA-256
  6968A314768BE84F01C685A4D9A25C6DE20F29D55C5198870758E2986EADB33E.
- English R76 validation is PASS/errors empty at 10,513 bytes / SHA-256
  A344A70C00EBEE10693A5B7CF9AE38CBF9A6E69B6F5914DD4CC69DF913D61398;
  French R58 is PASS/errors empty at 12,751 bytes / SHA-256
  A170A999DBA4BB832A693D406172FF83398FC61413A922C455CC84DC25321C10.
  The corrected p.134 raster custody is carried forward; no OCR, global
  build/render, publication, upload, archive, XeLaTeX process, temporary
  source/$out, or Q: mapping remains.
- Next paired cursor: create/replay R77, then direct NUMDAM PDF one-based
  p.135 / printed p.136, beginning Corollary 5.4.5. No temporary French close
  must be removed.

## 2026-08-04 -- paired French recheck, EGA I printed p.136 sealed

- Direct NUMDAM authority confirms Corollaries 5.4.5--5.4.7, Remark 5.4.8,
  the 5.5 heading, all six clauses of Proposition 5.5.1, and its proof through
  the triangular diagonal diagram and exact terminal word which. The authority
  image is 4,742,222 bytes / SHA-256
  E0116F6D3509552A6308EBD99DABAFAD63D60ECCCB12EF1907415E734085921E;
  no OCR was run.
- The inherited English p.136 slice remains byte-identical. Exact live lines
  552--621 are 3,461 bytes / SHA-256
  FF6AE4299248F4ED0B7B10A1229B6687A93A87A5A5D538ACEDEACF0501DE2E10.
  R77/R78 are zero-delta 127-file manifests; R78 is 49,882 bytes / SHA-256
  803A294EC3F3CF1EFBC42ED8C3CDEE057FF2DA8142483676ED5B2E0B74F85F7B.
- The cumulative p.136 projection is 17,717 bytes / SHA-256
  9892021E9733F25826BA7B8F6B7C259CDA98759113F13BDCD2D79225657D38A4.
  It reproduces live lines 239--621 exactly before one 12-byte build-only
  proof close. The three-pass English PDF is 27 pages / 206,911 bytes /
  SHA-256
  1E4A283AC89786A08A3DC0B5AB5C979D783490E0A4DA47DD2FDBA888F777E5B8;
  pages 26--27 pass text-layout QA with the diagram and all six clauses.
- Paired French source is 34,221 bytes / SHA-256
  E025EFA76D8F9C9BBDA04042337FA59D653F93E403AAB5FD3BC287F2712FDE67;
  its 40-page bounded PDF has SHA-256
  2616D0F29294FF83B73C6BEF0B27728B8C8D5EF1633D3ED0B5DA84EEAEBB6C42
  and page 40 passes visual QA.
- The p.136 scaffold is 86,845 bytes / 1,481 lines / SHA-256
  908D82E0E7063B91CFDE8C2765AD49F7DA2A9B60E5F8E782A4B1C0A697FE1DA2.
  French, English, and workflow ledgers parse at 8, 8, and 18 rows; the
  workflow SHA-256 is
  C3B242A5B9B4130D3AF2A7FC27A459B0D551F30BD232EF53D5C98635919CFCDE.
  All failed diagnostic attempts remain explicitly logged with no-mutation
  resolutions.
- English R78 validation is PASS/errors empty at 10,320 bytes / SHA-256
  2877803FF2CE1394874B34E53E7F5734EA3071E63E78CA26D81CB78720559127;
  French R59 is PASS/errors empty at 12,413 bytes / SHA-256
  0B7EFF6AC3741D1FB7B4CF326CCAC9872C6E4EC6FBFD5C83D6F0FA9A54651A9C.
  No OCR, global build/render, publication, upload, archive, remaining
  XeLaTeX process, temporary source/$out, or Q: mapping remains.
- Next paired cursor: create/replay R79, then direct NUMDAM PDF one-based
  p.136 / printed p.137, continuing the proof after ce qui. No temporary
  French close must be removed.

## 2026-08-04 -- paired French recheck, EGA I printed p.138 sealed

- This terminal entry supersedes the stale p.132--p.136 checkpoints that were
  previously appended after the valid p.137 receipt. Their append-only bytes
  remain intact; the p.138 workflow ledger records the chronology anomaly and
  its non-destructive resolution.
- Direct NUMDAM authority confirms Proposition 5.5.5 and proof, the
  affine-target reduction, Proposition 5.5.6 and proof, Corollaries
  5.5.7--5.5.9 and proofs, the affine-morphism consequence, and Proposition
  5.5.10 through the terminal underlying-space phrase. The bounded authority
  image is 1,956,101 bytes / SHA-256
  C5104A4DB04052A58074BF34EDD92726FE3C25FC1E5F68D59C46E286F50A240F;
  no OCR was run.
- Four source-fidelity repairs update source/ega1/ega1-5.tex: restore the
  omitted first 3.2.5 dependency; state the actual reduction to affine
  targets; restore singular criterion; and correct Corollary 5.5.9 from a
  false broad biconditional to distinct necessary and sufficient scopes. The
  last repair is mathematical, not stylistic. The mapsto glyph, structural
  proof environments, and structured clause display are explicitly retained
  normalizations rather than unrecorded claims that the printed author was
  wrong. Current source is 47,354 bytes / SHA-256
  29761A8C85CC1608E3EC80A7397B0847306F8A5F8C61AEA4772E1C79A3E493E3;
  all four old/new fragment hashes replay and the exact inverse restores R81
  SHA-256
  BE2123101A28F8BEB6BBB5B32FC09CCA17F1B01BA491C9799229D9810B89BE2E.
- R82 is the one-row successor: 127 files / 7,281,672 bytes, manifest 51,613
  bytes / SHA-256
  CE696DDADDBAD9D41D2086BC0B849F9D57531BA086B77826DC1FA0F0BFA771F9,
  canonical ordinal tree SHA-256
  863DC6BD6E3C752E94DDA9B58EEBD8AE9378CF64B525F663359EFDAE146E85CD.
  Membership, row, order, total, tree, and inverse gates pass.
- The exact live projection is lines 239--749, 25,922 bytes / SHA-256
  1B1CCE5050ADD9E0889175B7E07EC242EEF8B6079AAC438D7C07C0B02180EAD5;
  the wrapper adds one build-only end-proof token because the proof continues
  on p.139. The three-pass English PDF is 29 pages / 217,374 bytes / SHA-256
  1B4A7532D8DF1C832CBE61249EF6395CC36A3EEFEA1C1C886472ECA62D0297C4;
  pages 28--29 pass text-layout QA with all four repairs visible.
- Paired French source is 42,953 bytes / SHA-256
  2619437E655E33F819B8A965B48F8DA2D9B0F6890A0E9314EA285D8C99DF87CB;
  its 41-page bounded PDF has SHA-256
  96E1279700FDCBEFFC38E7E1E28A28D6CA9C4F08BB9B87A3D1BD7C91B8FD2687
  and page 41 passes visual QA.
- The p.138 scaffold is 98,950 bytes / 1,682 lines / SHA-256
  1B024552FFE71D56EB1BB2BA50304961073B55B0CEE76D5F514EDDFB65D49BB4.
  French, English, and workflow ledgers parse at 9, 14, and 22 rows; workflow
  SHA-256 is
  A1FFA5B192BE640F4BE13E876823E1F255AF2CF1E0560DCB3B89DA76D8EEB7C4.
- English R82 validation is PASS/errors empty at 15,740 bytes / 335 lines /
  SHA-256
  9B73FA281982CBC243DDEA33272650265A40A64E1FF7FBB18D217D9C63F4E58A;
  French R61 is PASS/errors empty at 13,736 bytes / 295 lines / SHA-256
  61DEE7FD8760F32CF965CB8D10E85FC4572B766ADCDFC16978EA297FCFA22E73.
  No global build/render, OCR, publication, upload, archive, remaining
  XeLaTeX process, temporary source/$out, or Q: mapping remains.
- Next paired cursor: create/replay complete R83 before any p.139 English
  source mutation, then direct NUMDAM PDF one-based p.138 / printed p.139,
  continuing the proof of Proposition 5.5.10. No temporary French close must
  be removed.

## 2026-08-04 -- paired French recheck, EGA I printed p.139 sealed

- This terminal entry supersedes every older cursor receipt while preserving
  all append-only historical bytes.
- Direct NUMDAM authority confirms the completion of Proposition 5.5.10,
  Examples 5.5.11, and Remark 5.5.12 clauses (i)--(iii). The page image is
  1,882,379 bytes / SHA-256
  DCA1F394B632C3CCA5BB86F9BD2FCDB1CD29BDE66A4051AAAE99DBBD53550DDC;
  no OCR was run.
- Three source-grounded repairs update source/ega1/ega1-5.tex. Both
  printed/inherited doubled-origin ideal tokens change from (0) to (s), with
  a visible translator note that preserves the French reading and explains
  that (0) is generic. Singular agreement is restored after neither. The
  doubled-plane clause is strengthened from a weak plural negation to the
  exact assertion that neither condition is satisfied. Current source is
  47,538 bytes / SHA-256
  E4E6D19A7C19B69E61CBBE8792DB0EED1AD6DAA0DD559E61811057F11641651C;
  all three old/new fragment hashes replay and the exact inverse restores
  R83 SHA-256
  29761A8C85CC1608E3EC80A7397B0847306F8A5F8C61AEA4772E1C79A3E493E3.
- R84 is the one-row successor: 127 files / 7,281,856 bytes, manifest 52,489
  bytes / SHA-256
  4C4EF213763A4E9838AF2E8E23A89C8DB0FC45DEBEA0DA078908BED01EA6CFB8,
  canonical ordinal tree SHA-256
  3DD3F9B92DBC78C7334C1F194836E9F4181DF2FE87A8A3905D64947F51576F6C.
  Membership, row, order, total, tree, fragment, and inverse gates pass.
- The exact live projection is lines 239--781, 29,803 bytes / SHA-256
  F34AA6F07CEE12F29A8C9307EABAB9F387AA6CB1BE3411FAFB6EF32DE67DFDBB.
  Its wrapper adds only the end-enumerate and end-remark tokens needed for
  the p.140-continuing scopes. The three-pass English PDF is 29 pages /
  223,477 bytes / SHA-256
  D9DCC6A8D435A42A762FCE1B60E465873540FBCE8487DDAAB1ACB7353FB505CC;
  pages 28--29 pass text-layout QA with all three repairs and the visible
  note.
- Paired French source is 47,116 bytes / SHA-256
  D8168125192DF12B1765D4F81E8DD2A15D37378370454F4370E0A3F18C3BC055;
  its 42-page bounded PDF has SHA-256
  47E016E105621346051731757945D7110492D3D25F34C1DCE93CBC08896DAB07
  and terminal page 42 passes visual QA. The source preserves and catalogues
  both printed (0) ideal tokens; only English performs the visible correction.
- The p.139 scaffold is 104,604 bytes / 1,773 lines / SHA-256
  BE3FB4F09303AAF6D12C972D38D1590E94201A6952223A35BD32A9CECADA282B.
  French, English, and workflow ledgers parse at 10, 10, and 24 rows;
  workflow SHA-256 is
  02D0EEEB094CDBB8DD974883E2A5D124FBB123A2EF8BF70B5C4A598425639327.
- English R84 validation is PASS/errors empty at 16,128 bytes / 332 lines /
  SHA-256
  1BBFC3699FA46963B0818E655DC8A52D11BE53D8A81B2A0772E2ABB19EB551AE;
  French R62 is PASS/errors empty at 15,178 bytes / 310 lines / SHA-256
  6463BC1513088A20797B180C252BE4AFD7B609B260B525C958C237CD382B27CE.
  No global build/render, OCR, publication, upload, archive, remaining
  XeLaTeX process, temporary crop, or drive mapping remains.
- Next paired cursor: create/replay complete R85 before any p.140 English
  source mutation, then direct NUMDAM PDF one-based p.139 / printed p.140,
  beginning Remark 5.5.12 clause (iv). Do not place or remove a temporary
  French source close.

## 2026-08-04 -- paired French recheck, EGA I printed p.140 sealed

- This terminal entry supersedes every older cursor receipt while preserving
  all append-only historical bytes and superseded evidence.
- Direct NUMDAM printed p.140 confirms Remark 5.5.12 clauses (iv)--(vi), both
  arguments and the reduction square, 5.5.13, section 6, subsection 6.1,
  Definition 6.1.1, and the following paragraph. The exact paired English
  slices total 3,214 bytes / SHA-256
  AECF8D9C3BD19AA2CDB86B074270F09921732D829417AFA04F67C41FB0E775A7
  and require zero source mutation.
- Three otherwise silent translation choices are explicitly classified:
  oldpage 141 follows the complete reordered English compound; Noetherian is
  conventionally capitalized; and the English comma after the displayed
  reduction square is retained as sentence punctuation, not attributed as a
  French glyph. The bounded direct-authority crop proved that French has no
  comma there, and the French prefidelity source/build remain preserved.
- source/ega1/ega1-5.tex remains 47,538 bytes / SHA-256
  E4E6D19A7C19B69E61CBBE8792DB0EED1AD6DAA0DD559E61811057F11641651C;
  source/ega1/ega1-6.tex remains 54,682 bytes / SHA-256
  357725613444BBBD373C6F7983A958807EC2C94AF1A972BDF5B2519A5A74FE9D.
  R86 is a complete no-change successor at 53,233 bytes / SHA-256
  1AACEE47C3D247A51FAC9790F44B8B4291AD670DB299986CEC6F056638063F8B;
  its 127-file / 7,281,856-byte ordinal tree SHA-256 is
  3DD3F9B92DBC78C7334C1F194836E9F4181DF2FE87A8A3905D64947F51576F6C,
  identical to R85 with zero changed, added, or removed rows.
- The exact two-source projection wrapper has no balancing additions or
  build-only closes. The three-pass English bounded reader is 30 pages /
  227,500 bytes / SHA-256
  29AA995989C8EED0293505EEBF32CFDA4C40C4743C443B041C1566CA5ECBF267;
  pages 29--30 pass text-layout QA with all three choices visible and no new
  warning class.
- Paired French source/ega1/ega1-5-fr.tex is 50,232 bytes / SHA-256
  4610C5F9E732D99948AA809ED64C85D236423990C2750A06F0DC7A805D317701,
  and source/ega1/ega1-6-fr.tex is 694 bytes / SHA-256
  0292AFD987807F3045A61D94F56A2344684A539439013DE19091181E369F859F.
  The final 43-page French bounded PDF has SHA-256
  3952A572810DD80868F84C80C4FDD3165C538F1F27576546D2C87AD9F0E887F6
  and passes terminal text/visual QA.
- The p.140 scaffold is 110,209 bytes / 1,867 lines / SHA-256
  42B41EE3099E81D8D32B59ED957F1790EFBF83BC1BC09F535B5D53D04CC0CD32.
  French, English, and workflow ledgers parse at 11, 13, and 26 rows; workflow
  SHA-256 is
  738585AFF1AE7363E113DB039FC29859E1FDECE29EC51F24B73652E42E856CDD.
- English R86 validation is PASS/errors empty at 14,728 bytes / 315 lines /
  SHA-256
  0CA69172635D18391445CD58E9186CD96F0428B505D4A1602C8E31C93B094DF9;
  French R63 is PASS/errors empty at 15,819 bytes / 329 lines / SHA-256
  947BF36318ABA08B46674E6C94D49078651B817BAFE1C53DB059CE9F1109FDD6.
  No global build/render, OCR, publication, upload, archive, remaining
  XeLaTeX process, temporary crop, drive mapping, or agent remains.
- Next paired cursor: create/replay complete R87 before any p.141 English
  source mutation, then direct NUMDAM PDF one-based p.140 / printed p.141,
  continuing source/ega1/ega1-6-fr.tex after
  `Tout sous-$\mathscr{O}_X$-`. No temporary French close must be removed.

## 2026-08-04 -- printed p.140 control-identity successor

- The complete French STATUS p.140 receipt matched a repeated append anchor
  before its historical p.139 successor. The misplaced block remains visible;
  a terminal successor controls, and no source/build/index byte changed.
- Final workflow ledger is 20,658 bytes / 27 parse-clean unique-ID rows /
  SHA-256
  E58DBC28BE8369CA3649CC4E106825206A8517970B3EC221134216B0B9CA5A0E.
  Rebound English R86 validation is PASS/errors empty at 14,728 bytes / 315
  lines / SHA-256
  09041AA2A2E206C09256857D4A9A6447E0EF6322D8FD6CB9A4524FA2D4EB5F23;
  rebound French R63 is PASS/errors empty at 15,819 bytes / 329 lines /
  SHA-256
  730E1C8D71CF9F063349CE6797D0C4F3966615A45E2BF66F8D957F3E7E4E9FCD.
- Printed p.140 remains sealed through `Tout sous-$\mathscr{O}_X$-`. First
  create/replay complete R87; then continue direct NUMDAM PDF one-based p.140
  / printed p.141. No French source close must be removed.

## 2026-08-04 -- final printed p.140 control-identity successor

- Receipt placement, not source or mathematics, required two further
  append-only reversals. Every misplaced block remains visible, and the final
  successors use unique terminal anchors.
- Final workflow ledger is 23,071 bytes / 29 parse-clean unique-ID rows /
  SHA-256
  A736395707953F046D095A6A6F2EF4CB856F752F5045A1714260B32295C5E1D0.
  Final English R86 validation is PASS/errors empty at 14,728 bytes / 315
  lines / SHA-256
  17324EC59ECCC5E0E9B9C5905190B841435EE7C07F5C485665E765215FE6F4DC;
  final French R63 is PASS/errors empty at 15,819 bytes / 329 lines / SHA-256
  3D8088D1C25BD1925B80083CF44618FE2CDEACFF2C254E09FCCD792FD9C75235.
- Printed p.140 remains sealed through `Tout sous-$\mathscr{O}_X$-`. Create
  and replay R87, then continue direct NUMDAM PDF one-based p.140 / printed
  p.141 with no French close to remove.

## 2026-08-04 -- final printed p.141 control-identity successor

- Direct French reconstruction exposed one inherited English mathematical
  imprecision: Proposition 6.1.3 requires the corresponding ideal-sheaf
  sequence to remain increasing. The same exact line had omitted citation
  1.3.7 and weakened canonical equivalence to bare equality. One reversible
  repair restores all three; this is a translation precision correction, not
  a claim that the French author was wrong.
- A separate reversible 17-byte line restores oldpage 142. Current
  source/ega1/ega1-6.tex is 54,737 bytes / 839 lines / SHA-256
  BA45F1965B6085D84CA7E3723E4078039093ACFDDD916FD191AD43DE251CA980.
  The exact two-operation inverse reproduces R87 SHA-256
  357725613444BBBD373C6F7983A958807EC2C94AF1A972BDF5B2519A5A74FE9D.
  Cross-page placement, Noetherian capitalization, and parenthesized
  condition letters remain explicitly logged retained normalizations.
- R88 is 54,107 bytes / 1,162 lines / SHA-256
  76E4ACFF554773770EBC1C53C87E02A3F4CC54D3EA8CE81898DA6D5B9BF9B0E6.
  Its 127-file / 7,281,911-byte ordinal tree SHA-256 is
  5AAE163319428FB1DDB52411C7F5CAB6AFA90235FB32C7ADE2AFD6203E6D4C25.
- The exact projection builds to 31 pages / SHA-256
  B0802C9A4F68EA07E9EA785330C8722956B91FD74F408274E8F772CA81DCED65;
  pages 30--31 carry the repair and terminal semicolon with no new warning.
  Paired French source SHA-256 is
  75A77003BDC90E8F0809F0DBF324A1F45268BC7A39C557D5A78C62816168B95B,
  and its 43-page PDF SHA-256 is
  833844565C2D05E098455F36DF403B2438671716B32E30E0F48F52374C070C1D.
- The p.141 scaffold SHA-256 is
  E5BCB61BB2C8CBF65B628253E62B2F5579D9821C15078BFF25A12880ADDDC689.
  Final 22-row workflow SHA-256 is
  8744745815106FA65635512D34E1EA9DC3C93090735583DF2247F200600DA90F.
  English R88 and French R64 validations are PASS/errors empty at SHA-256
  288BC03CD1D8E9DB2B291B9CA7369DD8670A9D912C0C70EBE2FCE126F4C8F529
  and
  027E1BB4FC646376CAC767DCFA08933C86AE657719BAAA99A8DBF68A6DF6CAF7.
- Next gate: create/replay R89 before any English p.142 mutation, then
  continue direct NUMDAM PDF one-based p.141 / printed p.142 in the open
  French proof. No temporary French close exists to remove.
