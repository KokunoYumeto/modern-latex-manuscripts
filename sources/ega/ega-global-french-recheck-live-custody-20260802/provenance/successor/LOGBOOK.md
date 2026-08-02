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
