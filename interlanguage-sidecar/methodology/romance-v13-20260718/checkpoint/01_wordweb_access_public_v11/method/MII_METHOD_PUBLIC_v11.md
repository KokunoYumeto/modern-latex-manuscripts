# Public marginal-access method v11

## Purpose and topology

This checkpoint implements a **design ledger**, not an intelligibility result. It contains one row for every combination of 106 semantic senses and nine declared reader cohorts: **106 × 9 = 954 rows**. There are **zero human observations**. Sense splitting is mandatory; in particular, `domain` has four senses (`T51-S1`–`T51-S4`) and `identity` has four senses (`T60-S1`–`T60-S4`).

The canonical cohort topology is:

- `C-ES-STD` — adult readers literate in standard Spanish (standard Spanish).
- `C-FR-STD` — adult readers literate in standard French (standard French).
- `C-PT-STD` — adult readers literate in standard Portuguese (European/Brazilian profile must be recorded).
- `C-GL-STD` — adult readers literate in standard Galician (standard Galician).
- `C-CA-STD` — adult readers literate in standard Catalan (standard Catalan; Valencian exposure must be recorded).
- `C-IT-STD` — adult readers literate in standard Italian (standard Italian).
- `C-RO-STD` — adult readers literate in standard Romanian (standard Romanian).
- `C-RM-RG` — adult readers literate in Rumantsch Grischun (Rumantsch Grischun; seed provenance still needs idiom audit).
- `C-RM-ID` — adult readers literate primarily in a Romansh regional idiom (Sursilvan/Sutsilvan/Surmiran/Putèr/Vallader must be recorded separately).

The regional-Romansh cohort must later name Sursilvan, Sutsilvan, Surmiran, Putèr, or Vallader. It is separate from Rumantsch Grischun; neither cohort proxies the other.

## Stored design diagnostic

The populated numeric values are deterministic orthographic comparisons. For strings `a` and `b`, normalized similarity is `1 - Levenshtein(a,b) / max(len(a),len(b))`, with the empty/empty case defined as 1. Candidate surfaces are compared with inherited cohort forms and with Spanish and French dominance carriers. Stored deltas are candidate proxy minus the corresponding dominant-standard proxy.

These values are **not** comprehension, pronunciation, semantic transparency, acceptability, processing time, or marginal intelligibility. The Boolean comparison field merely reports whether the stored orthographic proxy exceeds both dominance-carrier proxies by 0.05; it is not a successful test result.

Candidate construction uses equal total weight across five branch zones. Spanish and French receive no population bonus, and a form carried only by Spanish or only by French receives the recorded single-zone dominance penalty. Candidate scores remain hypotheses; no score promotes a controlled form.

## Evidence and adverse evidence

Every ledger row names its sense, cohort, candidates, dominant-standard comparator forms, penalties, supporting evidence IDs, adverse evidence, confidence state, and review status. Accepted sense support, wrong-sense/adverse evidence, held evidence, lexical-navigation evidence, and running-body evidence remain distinct. Evidence IDs in the public WordWeb resolve to metadata-only evidence records. Underlying quotations, locators, host paths, and raw source bodies remain internal because reuse rights are unresolved or not publication-cleared.

The 120 inherited Spanish/French core records remain unresolved locator claims with **zero quotations** and are not promoted by contextual extension-node snippets. The internal v11 layer contains 811 evidence records. Seventy-eight of 106 senses have accepted internal support; 28 remain explicit gaps. This is source-evidence coverage, not reader validation.

## Human protocol and hard gate

All seven human-result fields are null on all 954 rows, the human observation count is zero, every row and every decision has `pilot_eligible=false`, and no controlled bridge form is promoted. Therefore no MII result feeds a vocabulary or grammar decision in this checkpoint.

A future human study must record the exact cohort (and Romansh idiom where applicable), mathematical-literacy band, other Romance exposure, randomized and blinded item order, task instructions, correct/incorrect/abstain outcomes, latency, confidence, uncertainty, consent, exclusions, and review state. Only cohort-level observations with an approved analysis plan may support a marginal-gain or intelligibility statement.

## Graph boundary

The WordWeb has 406 descriptive relation records. Exactly 27 are target-ID graph edges. Adding 106 concept-to-sense memberships yields 133 ID-resolved references. It is incorrect to report all 406 relation records as graph edges.

## Publication boundary

This public projection deliberately excludes raw sources, quotations, locators, and host paths. It does not declare a license for the underlying source bodies and does not certify the controlled Romance language, a pilot, or the four-stage lane as complete.
