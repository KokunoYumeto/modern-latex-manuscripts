# Noether Persianate/Tajik Completed-Reader Integration Fix Pass

Generated: 2026-07-04

Status: draft/non-canonical/not native reviewed/no approval/no gate promotion/no Git push.

## Scope

This pass follows completion of the Persianate/Tajik LocalCodex corpus draft through German baseline line 24017 (`\end{document}`). It verifies that the fa_IR and prs_AF corpus sidecar is structurally consumable as a completed-reader draft, while preserving the Tajik Cyrillic zero-promoted-row boundary.

## Inputs Verified

- `NOETHER_FA_IR_PRS_AF_CORPUS_TRANSLATION_SLICES_DRAFT_20260704.md`
- `NOETHER_PERSIANATE_TAJIK_DURABLE_RUN_LOG_20260704.md`
- `NOETHER_PERSIANATE_TAJIK_LANE_DRAFT_ARTIFACTS_MANIFEST_20260704.json`
- `NOETHER_PERSIANATE_TAJIK_LANE_DRAFT_ARTIFACTS_20260704.sha256`

## Structural Checks

- Checksum sidecar entries verified OK before this integration artifact was added.
- Manifest stated completed slices `001-301`, last German range `23521-24017`, and next anchor `LocalCodex baseline complete at line 24017; next integration/fix pass`.
- Corpus sidecar contained 301 slice headings, 301 `fa_IR` draft headings, 301 `prs_AF` draft headings, and 301 notes headings.
- Corpus sidecar contained exactly one Tajik Cyrillic non-row continuation section and exactly one gate statement.
- Durable run log contained no stale `001-082`, `22761 onward`, `23521 onward`, `slices 001-293`, or `line 23520` frontier text after the prior reseal.

## Reader Integration Decisions

- Treat `NOETHER_FA_IR_PRS_AF_CORPUS_TRANSLATION_SLICES_DRAFT_20260704.md` as a completed draft reader sidecar for the current LocalCodex German baseline, not as canonical translation.
- Keep fa_IR and prs_AF as separate lanes. Iranian Persian terminology in the corpus sidecar must not authorize Dari terms.
- Keep Tajik Cyrillic as source-discovery/non-row only. No Tajik corpus translation or term rows are created by this pass.
- Treat slice 301 as bibliography/back-matter routing metadata, not theorem-prose translation.
- Preserve all unresolved register flags in the run log. The completed-reader state does not remove the need for specialist and native review.

## Remaining Blockers

- Native review is absent for fa_IR and prs_AF.
- Tajik Cyrillic has zero promoted term rows and no source-language reviewer decision.
- High-risk terms remain unresolved, especially `verschränkte Darstellung/Produkt`, `Hauptgeschlecht`, `Normensatz`, `Differente`, `Restklassenring`, `Idealquotient`, and the Persian/Dari split for loan-heavy algebraic vocabulary.
- The current completed-reader status covers the on-disk LocalCodex baseline only; it is not a claim that Zenodo/live/canonical sources cannot receive later repair witnesses.

## Outcome

No textual correction was required during this pass beyond recording this integration state. The next responsible action is to use this completed-reader sidecar in a non-canonical SGA5/Zenodo or reader-integration/fix workflow, with manifest/checksum refresh after any new sidecar is added.
