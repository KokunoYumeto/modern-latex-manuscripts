# Chinese / Japanese / Korean research handoff

## Manager scope

The manager coordinates translation of every work into Chinese, Japanese, and Korean target standards. This is one administrative manager with distinct linguistic sublanes, not a pan-CJK constructed language.

Maintain separate source shelves, terminology standards, scripts, typography, and reviewer paths for:

- Chinese varieties and written standards, including an explicit Simplified/Traditional policy where applicable;
- Japanese;
- Korean, including the relevant Hangul/Hanja policy.

Cross-language concept links are crosswalks, not evidence that one language witnesses another.

## Current research state

- Seventeen concepts in the current CJK source-body pass survived internal sense audit.
- Four concepts entered the shared map through this lane: finite-dimensional, finitely generated, free module, and quotient ring.
- Spot-checked standard terms include Japanese `環`, `可換環`, `商環`, `加群`, `自由加群`, `イデアル`, `準同型`, `体` and Korean `환`, `가군`, `몫환`, `체`.
- The historical CJK package’s `SOURCE_BODIES.csv` mislabels generated/audit material as native source bodies. Its `manifest.csv` is the authority for source classification.
- Unified v6.2 has 184 CJK candidate rows and 11 adverse/competitor rows, but zero support rows under that package’s own classification. Its 87.6 score is not readiness.

## Required controls

- Use local mathematical standards and native source bodies per language.
- Preserve script form, character variants, spacing, punctuation, vertical/horizontal layout assumptions, names, and formula interaction as explicit invariants.
- Do not count shared Han characters as semantic equivalence without language-specific sense and register checks.
- Do not infer Korean evidence from Chinese/Japanese character forms or vice versa.
- Separate source-body candidates, terminology-standard entries, corpus attestations, and external review.
- Retain false-sense and transliteration collisions in adverse channels.
- Keep formula/notation as a comparator layer; it does not replace target-language proof prose.

## Manager output

For every work, maintain one concept ID with distinct `zh`, `ja`, and `ko` target records, each with its own source provenance and decision status. Shared comparison rows may link them, but promotion remains language-specific.

The default intervention is `local_standard_crosswalk`. Any proposal for a cross-CJK bridge requires new sociolinguistic and human-comprehension evidence and cannot be inferred from the present corpus.
