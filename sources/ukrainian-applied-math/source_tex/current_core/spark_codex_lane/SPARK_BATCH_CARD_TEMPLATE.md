# Spark batch card

BATCH_ID:
SOURCE_FILE:
SOURCE_STATUS:
PUBLIC_SCOPE: educational / simulation / theory only

## Task
Convert/clean this source into Ukrainian TeX while preserving all math/code invariants.

## Required outputs
- `module_uk.tex`
- `BUILD.md`
- `CHECK_REPORT.md`
- `TERMS.csv`
- `SOURCE_MAP.md`

## Invariants
- Preserve formulas, labels, refs, cite keys, code identifiers.
- Do not change signs, powers, indices, transpose markers, hats, bars, tildes.
- Mark uncertain formula as `[[CHECK: math]]`.
- Mark uncertain term as `[[CHECK: term-stability]]`.
- Mark out-of-public-scope content as `SCOPE_HOLD`.
