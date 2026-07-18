# Tranche 003 correspondence: source and context check

Date: 2026-07-18

## Scope and authority

The bounded editorial scope is the historical `sootvět*` / Cyrillic `соотв*` correspondence family in the 221 paired canonical Noether Interslavic TeX units. The change is a normalization of existing Interslavic translations, not a new translation from the German originals.

Authority used:

- the user's 2026-07-18 activation of the accepted normalization work;
- the completed Fable/ChatGPT R1 direction to re-head this family to `odpovědati`;
- the official Interslavic first-conjugation participle and soft-adjective paradigms recorded in `CORRESPONDENCE_MAPPING_REVIEW.json`;
- the local Interslavic dictionary headword `odpovědati` and established Noether-corpus terminology.

The evidence is typed and contextual. No scalar score, W0 projection, or community-certification claim made the decision.

## Checks completed

- Preimage hashes and projected after-hashes were checked before mutation.
- Every changed file has a retained preimage and an entry in `CHANGE_LEDGER.csv`.
- The resulting unified diff was reviewed as a bounded family substitution; no changes outside the explicit contextual and surface maps were authorized.
- Independent post-apply inventories found zero residual Latin and zero residual Cyrillic correspondence-family surfaces.
- A second transformation pass found zero changes (`idempotence_pass: true`).
- Source TeX and extracted PDF text were checked for both context-sensitive exceptions:
  - Paper 09 section 09, TeX line 123 and PDF page 2 contain `iz odpovědanja` / `из одповеданьа`. The genitive is governed by `iz`; the five non-genitive `-nosti` contexts use `odpovědanju`.
  - Paper 31 section 07 entry 02, TeX line 32 and PDF page 1 contain `pridružene proste idealy` / `придружене просте идеалы`, matching the already dominant technical term for associated prime ideals rather than inventing a new compound.
- All 179 changed TeX units compiled; PDF text extraction confirmed the context-sensitive outputs survived compilation.

## Honest limit

This check establishes that the normalization is morphologically and contextually justified within the declared authority, paired across scripts, limited to the reviewed family, and faithfully propagated from editable TeX into the compiled PDFs. It does **not** independently re-audit every sentence against every German source page and therefore does not label the full translations source-faithful or certified.
