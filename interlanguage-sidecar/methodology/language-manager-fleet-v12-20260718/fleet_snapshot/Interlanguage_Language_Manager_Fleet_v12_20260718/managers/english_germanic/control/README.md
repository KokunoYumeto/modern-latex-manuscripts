# English and Germanic language-management lane

This manager owns translation into English and selected Germanic targets for
every work in the corpus. Noether, SGA 5, and SGA 6 are the current active
production queue; SGA 1--4 English examples remain style and terminology
controls. German may be source authority, target, or comparison language
depending on the work, and those roles must remain distinct.

## Authority order

1. Source scans and the current source-checked transcription or rescribe.
2. For Noether, the current German source-control witness (R823).
3. Existing English translations, used as translation controls rather than as
   source authorities.
4. Older English cumulative files, retained as recovery witnesses and never
   promoted wholesale without synchronization.

## Directory map

- `00_lane_control/`: status, witness register, exact continuation cursors, and
  machine-generated drift triage.
- `01_recovered_witnesses/`: recovered English TeX/PDF witnesses.
- `02_native_examples/`: terminology controls and current non-English workpass
  material needed for synchronization.
- `03_working_translations/`: active source-checked English work.
- `04_comparison_web/`: reserved for comparison renderings.
- `05_worker_returns/`: reserved for reviewed returns from bounded tasks.
- `06_publication_candidates/`: only for candidates that have passed source,
  build, and visual checks.
- `90_logs/`: lane-level operational logs.

## Current entry points

- `STATUS.md`: concise work-by-work state and next cursors.
- `WITNESS_MANIFEST.csv`: hashes and roles of the principal witnesses.
- `NOETHER_RA10_TO_R822_SOURCE_DRIFT.csv`: paper-level Noether source-drift
  triage.
- `SGA5_LEGACY_ENGLISH_BASE_TO_CURRENT_FRENCH_DRIFT.csv`: exposé-level SGA 5
  synchronization triage.
- `../02_native_examples/SGA_ENGLISH_STYLE_AND_TERMINOLOGY.md`: controlled
  English choices drawn from SGA 1--4.
- `RESEARCH_HANDOFF_INTEGRATION_20260717.md`: adopted department controls and
  existing-state conflict resolution.
- `GERMANIC_TARGET_EXPANSION_QUEUE_20260717.md`: same-manager sequencing rule
  for SGA 5 and SGA 6 German target editions after stable source-aligned
  English baselines.
- `ENGLISH_GERMANIC_EVIDENCE_GRAPH_v1.json`: typed provenance/routing DAG,
  currently routing the Paper 29 barred coefficient field, Paper 25 barred
  Galois-closure, Paper 36 `the different`, and Paper 27 `Hilbert numbers` plus
  plain-italic `q,p`, the Paper 18 resultant endpoint, and the Paper 5
  coefficient-domain versus field-of-scalars distinction; dependent witnesses
  and target-evidence cohorts are declared explicitly.
- `ENGLISH_GERMANIC_FAMILY_COHORT_TREE_v1.json`: declared dependence models;
  no quantitative edge weights or certification claims.
- `DECISION_NOETHER_P29_BARRED_COEFFICIENT_FIELD_20260717.json`: first
  schema-valid concrete decision record.
- `DECISION_NOETHER_P36_DIFFERENT_20260717.json`: English target-domain term
  decision separating the independent MIT witness from the project translation
  family and retaining the 600 ppi source caveat.
- `DECISION_NOETHER_P27_HILBERT_NUMBERS_20260717.json`: historical English-term
  decision separating Macaulay's original English article from the inherited
  RA10 family and rejecting both Hilbert-function concept collapse and
  source-incompatible fraktur ideal letters.
- `DECISION_NOETHER_P18_RESULTANT_ENDPOINT_20260717.json`: source-locked
  mathematical decision restoring the final factor index and congruence while
  keeping the R366 audits and R823 transcription in one German-source family.
- `DECISION_NOETHER_P05_DOMAIN_ROLE_DISTINCTION_20260717.json`: paired
  historical-role decision distinguishing the coefficient domain from the
  scalar field and rejecting inherited narrowing to `coefficient field` and
  modern `number field`.
- `../03_working_translations/noether_r823_paper25_english_sync_tranche008/`
  `SOURCE_DEPENDENCY.md`: typed Paper 25 decision/provenance record, including
  the later collected-edition facsimile as dependent adverse evidence.
- `../03_working_translations/noether_r823_paper27_english_sync_tranche010/`
  `SOURCE_DEPENDENCY.md`: typed Paper 27 source, audit, target-term, notation,
  boundary, and QA dependency record.
- `../03_working_translations/noether_r823_paper18_english_sync_tranche011/`
  `SOURCE_DEPENDENCY.md`: typed Paper 18 source, audit, inherited-candidate,
  formula, boundary, and QA dependency record.
- `../03_working_translations/noether_r823_paper05_english_sync_tranche012/`
  `SOURCE_DEPENDENCY.md`: typed Paper 5 source, audit, inherited-candidate,
  historical-role, boundary, and QA dependency record.

The drift reports are routing aids. They establish that source slices differ;
they do not by themselves certify which differences require changed English
prose. Similarity and delta bands never auto-promote, auto-reject, or establish
publication readiness.
