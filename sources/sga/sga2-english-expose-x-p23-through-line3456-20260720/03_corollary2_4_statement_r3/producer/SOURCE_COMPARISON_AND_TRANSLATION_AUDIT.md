# Source comparison: SGA2-X-COROLLARY2.4-STATEMENT R3 manifest-order successor

This is a no-overwrite, append-only evidence successor to the R2 bounded
source-aligned unit. It corrects only the false root-manifest ordering claim
identified by independent review. It is not an independent seal, publication
payload, archive handoff, or volume-completion claim.

## R3 evidence-only correction

The R2 producer and its `independent_review_20260720` directory remain
unchanged. Their complete 76-file surface is bound by
`PREDECESSOR_R2_PRODUCER_AND_REVIEW_IDENTITY_MANIFEST.csv`, 15,294 bytes,
SHA-256
`CA0768A465E6C09D51BA98DFE23FA1FDD0F0571D023C907917DB98FE1B6ED0FC`.
All 76 identities replay: 32 producer files and 44 independent-review files.
The true ordinal canonical aggregate is
`DEDB5F8DCD4E1851631C573A441258AD353A9F6FDB21F1E8AA499F1D84482FBC`.

R2 independent review `SGA2-X-C24-STMT-R2-IR@1` is preserved as a failure,
not rewritten into a pass. Its final audit is 6,610 bytes, SHA-256
`44333AED1B1407140F6CF5D9DCE229FECCC613223D3B64BB16F87DE5ACC62419`,
and its validation is 10,283 bytes, SHA-256
`E07B2DEB99405E53222913B8583ECF532E690A12D9480C348D107CCAB349CC03`.
That review passed the target, source replay, comparison correction, formulas,
build, fonts, text, renders, predecessor history, and unchanged-artifact
binding. It fail-closed only the root manifest.

The faulty R2 root `SHA256SUMS.csv` is 6,148 bytes, SHA-256
`6A7E4B9F8A96DB6CC13192F3DE8ABA08BCA939D8A7C057BB5080C5ACD93AB602`.
It claims `.NET StringComparer.Ordinal` but places lowercase
`artifact_tool_machine_qa.mjs` at one-based data row 5 instead of its true
ordinal position, row 29. The actual current-order canonical aggregate is
`6E371C71C3CA2E7E1D0724807BE11788E4ADA0452E2417DDD794CCEC57C9F79C`;
the true ordinal aggregate over those same 30 identities is
`53169F045FCC7E86B45011C8980E74247ECA5035EA07533B0853FEA5781FFAAA`.
The identities, byte counts, hashes, paths, coverage, and formula safety were
otherwise correct.

R3 preserves blocker
`SGA2-X-C24-STMT-R2-IR-ERR-MANIFEST-ORDINAL-001@1` and resolves it only in
append-only successor `@2`. Unit `SGA2-X-C24-STMT@3` reciprocally supersedes
`@2`; the R2 unit itself remains historical. The R3 root manifest is generated
by `.NET StringComparer.Ordinal` on normalized relative paths. Its validation
must report the independently replayed ordinal order and canonical aggregate.
R3 remains pending a fresh independent review.

## Authority and boundary

- Authority: corrected French arXiv TeX `smf_doc-math_4_01.tex`, 586,789
  bytes, SHA-256
  `C2F899E92A904E312B550C6452A117FF23D30AF984B2254A0961D2DF0DACD042`.
- Scope: French lines 3429--3431 inclusive, the complete statement of
  Corollary 2.4. Blank 3432 is excluded; raw cursor 3432 and next substantive
  cursor 3433, the proof.
- Coordinates: original printed p. 116, physical source-PDF p. 101, and
  recomposed running p. 93. No `\pageoriginale` marker occurs in the slice.
- Terminal-LF source slice: 351 bytes, SHA-256
  `374361D7850F93B348F1CDB311AA4FCF4F1F728D22C5ECC9C6A79A212D36BF11`.
- Same-edition physical-p. 101 render: 407,075 bytes, SHA-256
  `E59A5DADE48D40EA47B11A4747A72A21ABA090FA09F697F403FC5B4ACD0FB793`.

The retained source lines replay exactly against the authority. The PDF/render
is same-edition manifestation, formula, and layout evidence only, not
independent original-print corroboration. No source defect or unresolved
mathematical ambiguity occurs, and the French authority remains
byte-identical.

## Translation, formula, and comparison preservation

The target preserves `Lef(X,Y)`, the finite flat covering `R` of an open
neighborhood `U` of `Y`, and the fiber product
`R \times_U \widehat X`. It retains both directions of the first connectivity
equivalence and ordinary `X` in the final equivalence. Hats, subscripts, the
fiber-product base, and the distinct final subjects `Y`, `U`, and ordinary `X`
remain checked directly.

The jcreinhold comparison excerpt remains lines 228--234, 397 bytes, SHA-256
`52E63FECE61D36C64DB13D25B88F88450CF0A07CB9966663DD70DEDB24EC9436`.
It is comparison-only. Stable adverse-delta record
`SGA2-X-C24-JCREINHOLD-L234-HATX-ADVERSE-001@1` still rejects its line-234
completed `hat X` regression and binds authority ordinary `X`, candidate
completed `hat X`, and target ordinary `X`. No comparison or target wording is
changed in R3.

The 13-row `R3_UNCHANGED_ARTIFACT_IDENTITY.csv`, 3,110 bytes, SHA-256
`E1489E363D580606915BB9B7C02CDEB7076F226CB74A040955C33801046A953D`,
binds the French slice, candidate excerpt, source render, target TeX/PDF/render,
two build logs, engine artifacts, font report, and extracted text byte-for-byte
to R2.

## Preserved build and render identities

R3 does not rebuild or alter the target because the independent R2 audit
passed its content and found only a manifest-order defect.

- Target TeX: 1,525 bytes, SHA-256
  `DC1CA697B77344CFF33C631A253A52C5132C346E7B77E0965E6891A9DA09E02F`.
- Target PDF: 172,038 bytes, one A4 page, SHA-256
  `3B179631D2658B6CF593F95BAC76F9CE1CF3C990909DB11B606FACC17FBF5677`.
- Pass-1 log: 7,207 bytes, SHA-256
  `54B5ECB57E660920416D4D2A2B1435AEEC64265E5FCA727B5287722B6E55EFDD`.
- Pass-2 log: 7,087 bytes, SHA-256
  `DFB3253AE46B2BD31C506E3AAFBAE02CC5E1A2E2C74ADA04280EF05633C08C02`.
- Final engine log: 24,056 bytes, SHA-256
  `4C3DD16F1DE95E1E8865831973C0CDF9D1F98D517E524A8EED800D406BCD17A2`.
- Target render: 97,293 bytes, SHA-256
  `49C9867865134729AD59C93E463F2A8F3250576F69C58986F516400EC0FDD65A`.
- Extracted text: 956 bytes, SHA-256
  `7597F1AAC5798080690680FF16975B70EAB3E40F1ADFBF6468A250320DA1B0A9`.
- Font report: 1,235 bytes, SHA-256
  `74C646E9A719B20AB02430DD81E756F96BD2862BAA8FA2EBA519283EA4CF42FC`;
  all 11 rows are embedded, subsetted, and Unicode-mapped.

## Machine, privacy, and release state

The R3 CSV/JSONL controls preserve all R1/R2 records, append the R2 independent
failure, append the R3 unit and exact blocker resolution, and bind the 76-file
R2 history plus 13 unchanged current artifacts. Revision, parent, child,
resolution, and supersession references must close reciprocally. CSV must be
rectangular, CRLF-only, ID-unique, and formula-safe; JSONL must be strict-parse
and duplicate-key clean with exact CSV ID parity.

Three copied build/engine logs contain private local paths:
`BUILD_PASS1.log`, `BUILD_PASS2.log`, and
`SGA2_Expose_X_Corollary_2_4_Statement_English_SourceAligned.log`. They must be
sanitized or excluded before any public payload. R3 is
`internal_not_for_release` pending fresh independent review. No archive
handoff is made. Continue at raw 3432 / substantive 3433.
