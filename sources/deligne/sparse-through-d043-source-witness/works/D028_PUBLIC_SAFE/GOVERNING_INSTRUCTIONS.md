# Governing instructions — D028

## Frozen identity and precedence

- Work ID: `DELIGNE_D028_CIRCLE_DIFFEO_HERMAN`.
- Exact title: *Les difféomorphismes du cercle [d’après M. R. Herman]*; standalone English title: *Circle Diffeomorphisms [after M. R. Herman]*.
- Sole author: Pierre Deligne. `M. R. Herman is the subject/source attribution in the bracketed subtitle, not a coauthor`.
- Controlling source: `20_AUTHORITY_DELIGNE_D028_CIRCLE_DIFFEO_HERMAN_IAS_NUMBER30_23PP.pdf`, physical pages 1–23, printed pages 99–121, SHA-256 `A1A58A397BA1D2DA9249323E6627860E9D6CD0FCE80A071EF0D91893A4E9897C`.
- `21_COMPARATOR_DELIGNE_D028_CIRCLE_DIFFEO_HERMAN_COLLECTED_23PP.pdf` is `COMPARISON_ONLY` and may never overrule the authority.
- `30_ZERO_ACCEPTED_DEDUP_PRIOR_WORK_DELIGNE_D028.zip` has SHA-256 `EE20DF29622D3EEBC299F3B69C6A95F4E6A6A870D4873A21C540EFEB3B965BC7`; all 20 unique members and all 30 path-provenance rows begin `ZERO_ACCEPTED`.

## Required page-local order

For each owned physical page, work from the attached authority bytes: (1) inspect pixels at useful magnification; (2) replay complete source-faithful French, including mathematics and layout-sensitive objects; (3) render and compare back to the same pixels; (4) correct and freeze French; (5) only after freeze, compare inherited TeX/PDF and comparator evidence; (6) make the standalone English translation from frozen French, checking again against authority; (7) record only restrained source/translation apparatus. Never use OCR, inherited TeX, or a reflowed PDF as truth.

The French target preserves title, bracketed attribution, Deligne byline, prose, numbered sections, theorem/proposition/corollary/lemma/remark structure, equations, four positional diagrams, and bibliography. Exclude the Bourbaki running header, leaf codes, repeated folios, and terminal blank remainder from both language bodies; record publication facts in apparatus. M. R. Herman must not enter author metadata.

If a formula, diagram, or character cannot be represented faithfully as text, create an untouched lossless crop from `20_AUTHORITY_DELIGNE_D028_CIRCLE_DIFFEO_HERMAN_IAS_NUMBER30_23PP.pdf` only and a separate presentation derivative. Log page, pixel bounding box, command/extraction parameters, every derivative operation, and SHA-256 for both. Never crop inherited or comparator bytes as source evidence. The four positional diagrams on physical pages 15–16 require this paired treatment unless a fully faithful native reconstruction is independently compared to the pixels; raw crops remain decisive evidence.

## Known inherited faults and gates

`13_KNOWN_CANDIDATE_FAULT_AND_DIAGRAM_LEDGER.tsv` is mandatory replay evidence, not an optional errata list. In particular: replay Theorem 2.3’s `q^(1/2)` bound and `sqrt(q)` gain from physical page 7; restore `x^(1-epsilon) < r/s < x` and the missing quotient on page 16; preserve all four positional diagrams from pages 15–16; remove the inherited extra `-beta` from Theorem 9.1 only after replaying page 21; and repair both malformed Hölder strings from pages 2 and 18. Do not silently patch inherited text. Each repair must cite authority page, record before/after evidence, pass render comparison, and only then be frozen.

## Sessions and response contract

There are exactly `ceil(23/6) = 4` prompts with contiguous, disjoint ownership: 1–6, 7–12, 13–18, and 19–23. A page belongs to one prompt only. Continue repairing from attached authority bytes until the owned unit is complete; there is no ordinary terminal HOLD/FAIL state and no attempt/time cap. Workflow status values are only `IN_PROGRESS` and `COMPLETE`.

Every response, including an incomplete one, must attach exactly the current session’s deterministic cumulative full-state ZIP, checkpoint JSON, and manifest TSV. Package the entire state, verify the manifest, reopen it, and reproduce the identical ZIP hash by a second clean packaging run. Resume from the newest valid same-session trio while `IN_PROGRESS`; after a session is `COMPLETE`, advance exactly once.

P04 additionally integrates all 23 pages, rebuilds all three readers, and performs a fresh full audit in a clean workspace without reading prior audit conclusions or applying patch-only review. Audit identity/byline, topology, copy-matter decisions, French, English, apparatus restraint, every formula, all four diagrams, bibliography, and beginning/middle/end. If it finds an error, repair in the normal source state and restart the fresh full audit from page 1. Mark project `COMPLETE` only after this succeeds.
