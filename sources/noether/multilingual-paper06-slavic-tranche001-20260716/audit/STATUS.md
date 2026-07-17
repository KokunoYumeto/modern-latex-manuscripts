# Noether Paper 06 Interslavic Tranche 001

## Scope

This tranche applies the reviewed Fable orthographic decisions to all sixteen Paper 06 Interslavic Latin units and mirrors only those approved deltas into their sixteen existing Cyrillic siblings. Russian and Ukrainian files were held byte-for-byte unchanged.

The tranche is an orthographic synchronization pass, not a new semantic translation or a declaration that Paper 06 is source-closed in these languages.

## Applied changes

- Latin `obšč` was normalized to the approved `obć`: 7 replacements.
- Latin `vzet` was normalized to `vzęt`: 1 replacement.
- Cyrillic `obshch`-equivalent forms were synchronized from `обшч` to `обч`: 7 replacements.
- Cyrillic `voobshche`-equivalent `вообче` was synchronized to `обче`: 1 replacement.
- Cyrillic `взет` was synchronized to `взят`: 1 replacement.

The exact Unicode forms, paths, counts, and before/after hashes are recorded in `tranche_output/CHANGE_LEDGER.csv` and `tranche_output/ORTHOGRAPHY_SYNC_REPORT.json`.

## Verification

- Changed files: 9.
- Total replacements: 17.
- Idempotence check: pass.
- Russian/Ukrainian unchanged check: pass.
- XeLaTeX builds: 16 Latin and 16 Cyrillic, all successful.
- TeX errors: 0.
- Overfull boxes: 0.
- Visual QA: all changed-output pages were rendered and inspected; no clipping, missing glyphs, or formula overflow was found.

## Authority warning

The Paper 06 translations were generated from the June 2026 Paper 06 German slice and its English control. The current German project authority is the later R821-integrated cumulative source. R821 itself changes Paper 20, but the Paper 06 branch has not yet received a fresh, line-by-line semantic reconciliation against the current cumulative authority. This package must therefore be described as a checked orthographic tranche within a working translation corpus, not as a critical or final translation.

## Next continuation

1. Diff the complete Paper 06 generation slice against the Paper 06 span in the current German cumulative authority and classify every substantive delta.
2. Propagate any semantic/source corrections into Ukrainian, Russian, Interslavic Latin, and Interslavic Cyrillic together.
3. Build cumulative readers only after that source synchronization pass.
