# Rules Acknowledgement: Arabic RTL Fable Ledger Block

Status: generated-draft / non-canonical / Arabic-only support.

## Directive Files Read

- `FABLE_INTERLANGUAGE_PROGRAM_BLOCKING_DIRECTIVE_20260705.md` from side-branch commit `2d72c779f8bb8e46ee3ce0ba76731eb9cf4a2914`.
- `interlanguage-sidecar/20260705/fable_chatgpt_interlingua_program_full/interlingua_program_20260704/ARTIFACT_INDEX.md` from B3 payload mirror.
- `interlanguage-sidecar/20260705/fable_chatgpt_interlingua_program_full/interlingua_program_20260704/SOURCE_USE_POLICY.md` from B3 payload mirror.
- `interlanguage-sidecar/20260705/fable_chatgpt_interlingua_program_full/interlingua_program_20260704/user made flr with chat web stuff/WEIGHTED_INTELLIGIBILITY_SCORES_v3_20260704.md` from B3 payload mirror.
- `interlanguage-sidecar/20260705/fable_chatgpt_interlingua_program_full/interlingua_program_20260704/user made flr with chat web stuff/WHOLE_INTERLANGUAGE_MAP_v0_20260704.md` from B3 payload mirror.

## Done

- Implemented `languages.csv` for the Arabic rooted-family witness row.
- Implemented `source_documents.csv` from the local Arabic source-body package manifest.
- Refreshed `source_documents.csv` after Arabic source-canon round 3; it now tracks 240 package manifest rows from the Arabic source-body package.
- Added round-3 algebra-specific Arabic TeX/source-package recovery evidence at `SOURCE_RECOVERY_ROUND3_ALGEBRA_TEX_LEDGER_20260705.csv`; this records searches and blocker status rather than a recovered algebra source body.
- Implemented `lexemes.jsonl` for the six active Arabic rows.
- Implemented `forms.csv` with Arabic source forms, alternatives, witness categories, and formula-neighboring notes.
- Implemented `word_weights.csv` with branch weights, marginal scores, dominance penalties, adverse forms, and final draft statuses.
- Implemented `branch_weight_ledger.csv` as the Arabic sublane rooted-tree witness measure.
- Implemented `marginal_intelligibility.csv` with accept/review status per candidate.
- Implemented `do_not_use.csv` with false-friend/adverse/default-blocking rows.
- Kept generated draft support separate from source bodies.
- Added a separate Arabic RTL codepoint/extraction ledger and six-row interlinear pretranslation scaffold under `interlanguage-sidecar/20260705/arabic_rtl_codepoint_extraction_ledger_20260705/`.

## Not Done / Unsatisfied

- Arabic technical/LaTeX and Arabic math-rendering TeX-like source bodies are available in the local Arabic package, but no algebra-specific Arabic TeX/LaTeX/arXiv/e-print source archive is available yet; round-3 GitHub/web/CTAN searches did not recover one.
- No Persian, Persianate, Dari, Tajik, Urdu, Ottoman, or Turkic evidence is covered by this Arabic ledger.
- No native review, accepted terminology, source certification, license clearance, gate promotion, or translation completion exists.
- Specialist invariant/covariant Arabic source-body coverage remains source-acquisition/gap status.
- RTL TeX/PDF visual QA remains required before reviewer/canonical use.
- Codepoint/extraction QA reduces silent Unicode/bidi drift risk but does not certify final TeX/PDF page layout.

## Non-Claim Boundary

This package is a Fable data implementation for Arabic draft support and source-use bookkeeping. It is not a term approval, native review, canonical translation, bridge-language promotion, or public-ready source certification.

## G15 Addendum

- Implemented Arabic G15 invariant ledger at `G15_INVARIANT_LEDGER_20260705.csv`.
- Recorded source-use separation, Arabic-only language boundary, eponym/prose split, formula-neighboring RTL layout, and source-package availability invariants.
- Source-use and Arabic-only invariants are satisfied for the current package; formula-neighboring RTL/PDF QA now has a compiled/rendered first probe, with `Im*` adjacency and final-context visual QA still active. Arabic math-rendering `.dtx` source has been recovered, but algebra-specific TeX/source-package recovery remains active after round 3.
