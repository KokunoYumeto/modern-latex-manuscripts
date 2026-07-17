# Fable 5 instruction and completion state

## What Fable 5 told this lane to do

The executable authority is:

`C:\Users\Floris\Documents\interlanguage\00_governance\FABLE_TRANCHE_001_EXECUTABLE_SPEC_20260710.md`

It ordered a deliberately bounded Paper 06 pilot, not a whole-corpus rewrite:

1. Change only Interslavic Latin translation TeX for Paper 06.
2. Apply line-wide and idempotent orthography mappings: `vzet-→vzęt-`, `obšč-→obć-`, `dlugost-→dolgost-`, `vobče→obće`, and `voobče→obće`.
3. Protect TeX/math/comments, citations, URLs, labels/references, code-like material, and German titles.
4. Regenerate Interslavic Cyrillic in the same run because Latin and Cyrillic are one language in two scripts.
5. Compile and provide TeX, PDFs/logs, render check, terminology note, manifest, and acknowledgement.
6. Do not apply lexeme switches. `jednočasno`, `odpovědati`, and `krok` belong to a separate Tranche 002 after Floris's sign-off. Do not touch held `ręd`, `jednako`, `važiti`, `slučaj`, or the ring family.

## How it was already done

The durable completion record is:

`C:\Users\Floris\Documents\interlanguage\00_governance\WORK_LOG_20260716.md`

Recorded result:

- 9 Paper 06 files changed;
- 17 constrained orthographic replacements;
- Russian and Ukrainian remained byte-identical;
- rerun verified idempotence;
- 16 Interslavic Latin and 16 Interslavic Cyrillic units compiled;
- zero compile errors and zero overfull boxes;
- changed-page render sheets visually inspected;
- verified files promoted into the localized Paper 06 corpus with pre/post hashes and a change ledger;
- handoff `Noether_Paper06_Interslavic_Tranche001_20260716.zip`;
- handoff SHA-256 `21C82BC38265755340941D829A2E0372A7EA82AD5A313269850071E2AC3F1EF6`.

The working evidence remains at:

`C:\Users\Floris\Documents\interlanguage\03_projects\noether\03_translation_workspaces\interslavic_tranche_001_paper06`

Relevant machine-readable artifacts include `MANIFEST.csv`, `tranche_output/CHANGE_LEDGER.csv`, `tranche_output/ORTHOGRAPHY_SYNC_REPORT.json`, `tranche_output/BUILD_RESULTS.csv`, and `tranche_output/TRANCHE001.diff`.

Fable's 2026-07-17 lane note explicitly assesses Tranche 001 as “WELL DONE — spec honored.” That note is evidence/review state, not a new directive:

`C:\Users\Floris\Documents\interlanguage\03_projects\noether\FABLE_FINDINGS_FOR_SLAVIC_NOETHER_LANE_20260717.md`

## Effect on this R823 unit

The present unit does not replay Tranche 001 and does not start Tranche 002. It follows the held-row boundary: `kolco` remains corpus-primary; `slučaj` is not switched; gated citation switches are absent. Interslavic Cyrillic is regenerated deterministically from the Latin target and is not treated as a separate language translation.
