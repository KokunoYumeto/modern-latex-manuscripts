# FAC accidental independent-translation comparator — final methodology report

## Outcome

Codex translated Jean-Pierre Serre's *Faisceaux Algébriques Cohérents* nos. 1--79 from the controlling French source before Floris discovered the existing English translation by Piotr Achinger and Łukasz Krupa. The discovery therefore created an accidental blind comparator rather than a drafting lineage.

All 79 chronology-bounded units have now been personally adjudicated against the corrected French layer and the source-critical decisions already established from the 1955 journal authority. The result is:

- 79/79 units reviewed;
- 20 units with substantive agreement and no material finding;
- 59 units with one or more material external-lineage findings;
- 138 exact findings, each with French, Codex, and external locators, a selected form, and rationale;
- 0 Codex-English changes required by the comparator review;
- 0 corrected-French changes required by the comparator review;
- 95/95 frozen input identities replayed with zero byte or SHA-256 mismatch.

This is qualitative evidence, not a score, leaderboard, certification, or claim that either English lineage is source authority. The 138 count is not a scalar measure of translation quality: findings vary in kind and scope, and repeated consequences may arise from one local decision. The auditable evidence is the row-level rationale, not the total.

## How the control arose

The overlap was accidental. Codex had already translated, compiled, and source-reviewed through no. 79 when Floris found the Achinger--Krupa PDF and then its editable source archive. No. 79 therefore supplies the exact blind boundary. Nos. 80--81 were completed after discovery and are excluded from blind-performance claims; they form a small comparator-aware process control instead.

This chronology must not be rewritten as a planned benchmark. It matters because the external wording and formulas could not have influenced the Codex no. 1--79 draft. Conversely, the Achinger--Krupa English is a target-language comparator only; the French source, not agreement between English versions, adjudicates every reading.

## Method

Mechanical differences routed attention into 11 high-, 25 medium-, and 43 low-difference units. Mechanical similarity never decided correctness. The session lead reviewed every unit and recorded:

1. the exact French locator;
2. the exact Codex locator;
3. the exact external locator;
4. whether the difference was substantive or harmless;
5. the selected source-faithful form;
6. whether English or corrected French required a change;
7. the reason for accepting or rejecting the alternative.

The aggregate review set equals the 79-row inventory exactly. Finding IDs are unique and contiguous from `FAC-BLIND-F0001` through `FAC-BLIND-F0138`; every finding resolves to exactly one review; the sum of per-review material counts is 138. Spreadsheet imports, compact inspection, formula-injection checks, and the 95-row input-identity replay pass with no error.

## What the evidence shows—and does not show

Within the blind no. 1--79 cohort, source adjudication did not identify a reading that required changing the admitted Codex English or corrected French. It did identify external-lineage defects including symbol substitutions, omitted hypotheses, ill-typed maps, lost indices and superscripts, malformed TeX, silently preserved printed-source defects, broken reference locators, and one material weakening from “biregularly” to “birationally.” Twenty units instead supplied substantive independent agreement.

That outcome supports the usefulness of the source-first comparator workflow and supplies regression examples for future translation-comparison tools. It does not establish general superiority, assign probabilities of correctness, or permit either English translation to replace the French authority.

## Rights and reproducibility

The Achinger--Krupa PDF and source are credited and hash-bound in the evidence, but are not redistributed in this package. The package contains analytical ledgers, locators, hashes, methodology records, and project logbook snapshots. Any later redistribution of the external PDF/source requires its own rights determination.

## DOI role

This bounded package is evidence for the methodology DOI because it documents an unplanned blind comparison with exact chronology, inputs, adjudications, and adverse findings. Under `PROJECT_LOGBOOK_METHODOLOGY_REPLICATION_DOI_REQUIREMENT_20260802.md`, the same privacy-clean provenance package is also required in the replication DOI. Archive maintenance owns DOI mutation and public readback; this producer package itself makes no publication claim.

## Controlling files

- `FAC_ACCIDENTAL_DUPLICATION_BLIND_COMPARATOR_METHODOLOGY_EVIDENCE.md` preserves the discovery chronology and experimental boundary.
- `FAC_BLIND_COMPARATOR_INVENTORY.csv` defines the 79-unit universe.
- `BLIND_COMPARATOR_INPUT_IDENTITIES.csv` binds the exact compared inputs.
- `FAC_BLIND_COMPARATOR_ALL_79_UNIT_REVIEWS.csv` contains one review per unit.
- `FAC_BLIND_COMPARATOR_ALL_79_FINDINGS.csv` contains all 138 selected/rejected readings and rationales.
- `FAC_BLIND_COMPARATOR_ALL_79_VALIDATION.json` records exact set, identity, reference, and artifact-tool closure.
