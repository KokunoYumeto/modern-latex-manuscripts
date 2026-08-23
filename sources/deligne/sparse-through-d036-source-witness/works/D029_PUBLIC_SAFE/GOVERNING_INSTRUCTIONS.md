# Governing instructions — DELIGNE_D029_CENTRAL_EXTENSIONS_ARITHMETIC_GROUPS

## Authority, identity, and scope

Work only on this six-leaf paper. `20_AUTHORITY_DELIGNE_D029_CENTRAL_EXTENSIONS_ARITHMETIC_GROUPS_6PP_IAS_290DPI.pdf` (SHA-256 `CC9759F6D12980328126AF4CE6B5ACA8309FEC24D9ADC5F43A0D9FC88992C125`) is the controlling IAS scan. It alone controls words, accents, punctuation, formulas, arrow direction, diagram topology, labels, numbering, reading order, pagination, and boundaries. `21_COMPARATOR_DELIGNE_D029_CENTRAL_EXTENSIONS_ARITHMETIC_GROUPS_6PP_COLLECTED_SPLIT.pdf` (SHA-256 `94194945C6514025CAB62F2BD6A471C00384173BB096600087929629D97F5C92`) is comparison-only and cannot override authority pixels.

The inspected source reads `THÉORIE DES GROUPES. —`, **Extensions centrales non résiduellement finies de groupes arithmétiques**, and `Note (*) de M. Pierre Deligne, Membre de l'Académie`. Authorship is Pierre Deligne alone. The source is French and includes its own English abstract immediately after the French abstract. Preserve that English abstract explicitly as source matter; do not misclassify it as a later translation.

## Required targets and replay order

Maintain three separate cumulative layers: a diplomatic/source-faithful French edition, a standalone faithful English edition, and restrained apparatus. For every physical page, inspect and record the authority pixels first. Freeze the French source record before consulting any inherited candidate for that page and before drafting its English target. Only a frozen page may feed candidate comparison, translation, or final acceptance.

The English target translates all French source matter faithfully while preserving the already-English source abstract as such and documenting its relationship to the translated French abstract. The apparatus records only material textual decisions, scan ambiguity, exact diagram/crop choices, and necessary translation notes.

## Mandatory replay gates

The five concrete inherited defects in `14_AUTHORITY_REPLAY_DISCREPANCY_LEDGER.tsv` are minimum known hazards, not an exhaustive correction list. Authority replay must establish:

1. On physical page 2, both relevant arrows originate at `G(F)`: splitting `s` goes to `E`, and the vertical inclusion goes to `G(A)`.
2. On page 3, the displayed definition of `R` ends with a right arrow labeled `σ` from `⊕ μ_v` to `μ`, not an inclusion hook.
3. On page 4, diagram (3) has its splitting arrow start at `G(F)` and rise to the central extension; the theorem and problem remain unnumbered.
4. On page 5, the modular substitution is exactly `f(-z^{-1})`.
5. On page 6, retain the session note, notes (1)–(5), full IHÉS address, and EOF boundary; no received-date line exists.

Record the exact `authority_replay_facts` key/value pairs required by the state validator on each frozen source page. Replay every other formula, morphism, label, and structure independently from pixels as well.

## Prior work and image policy

`30_UNTRUSTED_PRIOR_WORK_DELIGNE_D029.zip` has 30 unique members (SHA-256 `9CE31D3FE7C45D27BB3279F561B3BFD71B666DE53DD6B2DF28F3108A1EBB54F7`): five deduplicated local snapshot objects, eight exact scoped provenance extracts, the complete 14-file public D029 checkpoint delta, predecessor and successor controls, and one canonical D029 identity receipt. Every member remains `ZERO_ACCEPTED` until page-local comparison after source freeze. The six discovered local snapshot paths are all retained in `13_SCOPED_SNAPSHOT_DEDUP_PROVENANCE.tsv`. The named D021–D045 diagram carrier contains no D029-named member, so no carrier byte is included.

Prefer semantic text, LaTeX, and SVG reconstruction. If safe semantic replay is impossible, crop only the smallest necessary region from the controlling authority, preserve an immutable lossless raw crop, create a separately hashed conservative presentation derivative, and log bounding box and every operation. Never use comparator, candidate, public, or render-check pixels as source. Never use a full-page screenshot as an edition page.

Running headers, repeated journal/date strings, folios, issue furniture, scanner margins, and terminal blank remainder are structural/copy matter rather than body transcription. Retain publication and boundary facts in apparatus; retain session note, notes, address, and substantive terminal text.

## Session and completion contract

P01 owns physical pages 1–6 exactly once. Every response, including partial progress, returns the cumulative ZIP, checkpoint JSON, and manifest TSV for S01. Workflow status vocabulary is only `IN_PROGRESS` and `COMPLETE`. Completion is validation- and coverage-based. The final audit is performed on a newly unpacked production candidate without editing the audit copy; corrections occur only in production followed by a new build and a new clean audit.
