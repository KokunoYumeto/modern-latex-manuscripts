# Dirichlet Round 23 - cumulative QA correction

This pass checks the already-produced Band II lane for the failure mode the user flagged: compressed output, source facsimile being used as a reading PDF, screenshots standing in for formulas/tables/symbols, or summarized mathematical content.

## Findings

1. **XXV, posthumous hydrodynamics paper.** The earlier public original-language file was a source-facsimile/source-locator rather than a final typed German source edition. The English file was described as a mathematical reading translation with normalized notation and the main equation systems. That is not a final, complete, line-by-line mathematical translation.

2. **XXVII, Kummer memorial address.** The earlier German original-language file was image-only facsimile. Because the piece is almost entirely prose, the English translation is less formula-risky, but the original-language typed source edition is still not complete.

3. **R22 tail items XXXVII-XLI plus the Volume I errata.** The targeted scan found TeX-typed reading files for the letters, signs, formulae, translation list, and errata. They are carried forward.

4. **Path names.** Package paths are compact and human-readable; the longest relative path is recorded in `audit/path_lengths.csv`.

## Corrective action

The cumulative PDFs in `cum/pdf/` are rebuilt with a QA status sheet prepended. This does not pretend that XXV or XXVII have been fully repaired. It prevents the cumulative record from silently presenting compacted/facsimile material as final clean text.

Source witnesses for XXV and XXVII are retained under `src/25` and `src/27`. Vol. I Paper I is staged under `v1/01/src` for forward continuation.
