# SGA2 Exposé X — purity theorem part (ii), privacy successor R2

R2 is a no-overwrite technical successor to `SGA2-X-L3573-PURITY-II-PROOF@1`. It does not revise the source scope, translation, source-defect adjudications, target TeX, target PDF, extracted target text, font report, PDF report, or rendered page. It repairs a producer privacy-validation defect only.

## Scope and unchanged target

The admitted authority remains French lines 3573–3574: the complete proof of Theorem 3.4(ii) plus its proof close. The 978-byte Latin-1/LF slice has SHA-256 `B05278589CC78D89064D5DCB7F8DFCBC1E83E992E4CA3DDB38861B0865731A8D`. Its locator is printed 122 / physical 105 / running 97. Blank line 3575 is the raw cursor; Theorem 3.10 at line 3576 is the substantive cursor.

The copied target TeX is 3,063 bytes, SHA-256 `385556B1AE857E855163EF2A7F26A9BA69010BD054616C01AFD48BD54BAB5499`. The copied target PDF is 210,031 bytes, SHA-256 `4A4200DE92635B265CDCA1BE28DFBAA7D318E09217EC481149B1E5B358B288CA`. Both are byte-identical to R1. The translation therefore continues to say “Let us prove (ii),” cite Corollary 3.8 for completion, and say “a complete intersection,” with the same immediate consolidated visible note naming all three final source-defect IDs.

## Predecessor privacy failure

R1's privacy validator scanned only a selected list of target-facing files and incorrectly reported zero hits. It omitted the three raw build logs and the target engine log. The fresh independent review found 316 line-dewrapped private user-profile occurrences across those four logs: 79 in each. In each raw build log these comprise 61 backslash-form occurrences and 18 forward-slash-form occurrences. Raw pass 1 is 7,577 bytes, SHA-256 `7F2E9262BCFA12C933949079EEDE8298D2F335FEA3539D7049E4BDA89A3F84C8`; raw passes 2 and 3 are each 7,467 bytes, SHA-256 `09BCF4FE0BA5BD6EEC0D243335B73B786A1783D02150C369E0BD0CF89ABD826B`.

Those raw logs remain immutable in the R1 predecessor and are classified as restricted internal operational evidence. They are not copied into R2. R2 substitutes three public-safe build summaries recording exit status, diagnostics, output identity, predecessor-log identity, and dewrapped hit counts without reproducing private paths.

## Post-validation predecessor contamination

R1's `PRIVACY_SCAN.csv`, `SHA256SUMS.csv`, and `VALIDATION.json` were finalized at approximately 02:11 local time. A reviewer subsequently created `independent_review_20260722_001` inside the R1 root beginning at approximately 02:15. R2 does not delete, move, copy, or normalize that directory. Its complete relative-path inventory and hashes are bound in `PREDECESSOR_CONTAMINATION_MANIFEST.csv`, while the original twenty top-level producer files are separately bound in `PREDECESSOR_TOPLEVEL_BINDING.csv`.

Accordingly, R2 does not claim that the original root remained unchanged after review: its pre-existing top-level producer files remain hash-bound, but the tree gained a 13-file review subdirectory after the original manifest and validation were finalized. The contaminated directory is excluded from R2 and treated as restricted adverse evidence.

## Revision and review policy

`SGA2-X-L3573-PURITY-II-PROOF@2` reciprocally supersedes R1 `@1`; the R1 snapshot is retained in the R2 machine ledgers with `superseded_by` pointing to `@2`. The historical privacy record `SGA2-X-L3573-PRIVACY@1` is similarly retained and superseded by `SGA2-X-L3573-PRIVACY@2`. Each raw-build-log record has a matching clean-summary revision.

The three provisional `SRCCAND-001@1` records and their three final `SRCDEF-001@1` successors remain append-only and unchanged. R2 is not sealed or archived. The fresh independent FAIL review is a required bound input; R2 remains review-ready rather than independently passed until a fresh review of R2 closes that failure.
