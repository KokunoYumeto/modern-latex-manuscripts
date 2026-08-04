# Successor-session bootstrap and logbook protocol

Status: controlling for successor work in the SGA / FAC / GAGA production lane

## Primary principle

The logbooks, decision ledgers, correction/reversal histories, source identities, and validation records are primary scholarly deliverables. A TeX/PDF body without that reviewable provenance is not an admissible continuation base, regardless of filename, compilation success, or prior readiness language.

## Mandatory first action in every successor session

Before editing, translating, rebuilding, normalizing, packaging, or assigning work, the successor must:

1. read the current user-verbatim brief and active pursuit goal;
2. read the project `STATUS.md`, project logbook, editorial-decision logbook, revision history, correction/application/reversal ledgers, validation JSON, exact manifests, and every retained FAIL/HOLD report relevant to the next cursor;
3. identify the controlling authority and rehash every frozen input named at the continuation boundary;
4. reproduce the exact admitted coverage and next cursor from disk, rather than trusting prose summaries or filenames;
5. inspect live task ownership and obtain a disjoint range before mutation;
6. list unresolved ambiguities, rejected choices, known defects, and downstream artifacts affected by any proposed change;
7. record the intake and its exact input identities in the successor's own append-only log before the first substantive edit.

If any identity, cursor, ownership boundary, or validation claim cannot be reproduced, the successor must fail closed and resolve the discrepancy before mutation. It must not rebuild history from memory or silently select a plausible-looking file.

## Decision and reversal discipline

- Every functional departure from the authority or inherited English must have a stable ID, exact source/target locator, selected reading, rejected alternative, rationale, evidence channel, revision link, and downstream scope.
- Cosmetic/house-style changes are prohibited unless explicitly adopted and justified. Authorial wording and notation are not errors merely because another form is preferred.
- A later-discovered mistake must append a reversal/supersession record, preserve the adverse history, enumerate every affected downstream artifact, and close a global repair replay before promotion.
- Diplomatic French, corrected French, and English are distinct layers. A correction applied to one layer must state whether and why it propagates to the others.
- Workflow/status/AI prose belongs in external controls, never in reader bodies.

## Resource safety

- Never run an unbounded search over `[PRIVATE_DOCUMENTS_ROOT]`, a drive root, or other multi-terabyte trees.
- Search only explicitly named bounded roots. Run one heavy build/render process at a time.
- Do not regenerate OCR when Floris's existing OCR is available; OCR remains locator/witness material unless separately admitted.
- Escalate image detail only as required by the mark: ordinary layout may use modest resolution; small source characters, primes, indices, arrows, and ambiguous punctuation require high-detail direct-authority inspection.

## Comparator evidence

The FAC accidental blind-comparator is a front-facing methodology control. The Codex FAC translation/source review for nos. 1--79 existed before Floris discovered the Achinger--Krupa English translation; nos. 80--81 postdate discovery and are excluded from blind claims. Its privacy-clean immutable package is:

`[PROJECT_ROOT]\03_projects\language_management\english_germanic\06_publication_candidates\FAC_Accidental_Blind_Comparator_Methodology_Evidence_20260803_r1`

It contains 79/79 unit reviews, 138 exact findings, 95/95 frozen-input replay, project and editorial logbook snapshots, and the append-only self-correction ledger. It must be conspicuous on both the methodology DOI `10.5281/zenodo.21124403` and replication DOI `10.5281/zenodo.20461174`, not buried as an incidental source attachment. The external comparator PDF/source are identified but not redistributed absent a demonstrated license.

## Handoff completeness

Every bounded/final handoff must state exact absolute root, scope and cursor, authority and comparison lineages, editable-source and PDF counts, build/render/reference/source checks actually completed, unresolved holds, superseded artifacts, and SHA-256 for every proposed public file. Privacy-clean logbooks and decision/reversal histories must accompany both methodology and replication deposits under the controlling dual-DOI requirement.

