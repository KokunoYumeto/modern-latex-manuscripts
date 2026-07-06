# Codex normalization patch task spec v1

Purpose: convert approved R1 normalization decisions into safe, reviewable patches in the Interslavic Latin corpus, then regenerate Cyrillic sidecars. This spec is not approval to apply all proposals.

## Inputs
- `NORMALIZATION_PATCH_ROW_SUMMARY_v1_20260705.csv`
- `NORMALIZATION_PATCH_OCCURRENCE_QUEUE_v1_20260705.csv`
- `NORMALIZATION_APPLY_PASS_DESIGN_v1_CHATGPT_20260705.json`
- `NORMALIZATION_DECISIONS_R1_DRAFT_v1_20260705.json`

## Guardrails
- Never patch rows with `risk in {human_review_only, deferred_no_apply}`.
- Never remove sanctioned doublets; only normalize obvious orthographic leakage inside a row when approved.
- Use TeX-aware replacement; do not patch command names, labels, filenames, bibliography, or source citations.
- Every replacement must carry an audit row with before/after context.
- After patching, run render validation and Cyrillic sync.

## Recommended first approved batch candidates

- `step` (57 hits): krok-family; morphology must be inflected by reviewer/Codex
- `corresponds` (737 hits): odpovědati-family; rehead lemma; manual inflection
- `reg-pytanje` (34 hits): pytanje/pytańje-family; manual inflection
- `reg-obći` (132 hits): obće / obć*-family; orthography/flavor normalization
- `follows-from` (32 hits): slěduje/slědovati-family, but keep W gloss; manual
- `length` (62 hits): dolgost/dȯlgosť; orthographic normalization
- `take-vzeti` (55 hits): vzęti/vzęto; nasal orthography
- `reg-odnovrěmenno` (151 hits): jednočasno; high-value W+S switch; manual review
- `reg-imenno` (38 hits): imenno plus mandatory W/S gloss; manual

## Explicitly blocked until reviewer input

- `holds-is-valid`: REGISTER-EXTENSION row: document explicitly that math sense extends dict sense; candidate for reviewer question
- `reg-rěšenje`: dict-sense tension (decision vs solution) documented; cs řešení supports the math usage — no change needed, note kept
- `series-sequence-red`: HIGH-DIVERGENCE ROW: no pan lexeme (F12c); ред(S/E)=order homograph; final texts should gloss on first use per paper; strongest candidate for reviewer sign-off
- `however`: HOMOGRAPH WARNING: hr/sr jednak(o)=equal(ly) — in math prose where 'equally' is frequent, prefer sentence positions that disambiguate, or use ipak for contrast; this row NEEDS the reviewer
- `case-instance`: hr pripada=belongs homograph noted (F12c)