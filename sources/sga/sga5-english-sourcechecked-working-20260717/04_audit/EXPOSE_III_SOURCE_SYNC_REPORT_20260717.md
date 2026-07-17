# Exposé III source-critical synchronization report

Date: 2026-07-17 (Europe/Berlin)

Scope: Exposé III only, in `SGA5_English_sync_workpass.tex`. No inherited French, legacy-English, or scan artifact was edited.

## Result

The 34 actionable exact-receipt rows assigned to Exposé III were independently revalidated at their live English anchors and all pass. The complete structural/diagram queue from `audit_evidence/middle_residual.md` was applied against the immutable French workpass and the original LNM 589 scan. No unresolved source ambiguity remains in this tranche.

The machine-readable page/anchor/correction/evidence/disposition ledger is `EXPOSE_III_REPAIR_MAP_20260717.csv`. It contains all 34 receipt IDs and 19 structural repair IDs.

## Authorities and style controls

- French control: `sga5_fr_workpass.tex`, SHA-256 `791F4EFFC5E02832D5D77ED03518C8156D6F07E4C8238B03545DB93D883FBB28`.
- Original LNM 589 scan: `C:\Users\Floris\Documents\Papors\OS\SGA5 (1).pdf`; the exact-receipt ledger identifies the scan-derived evidence for each receipt row.
- Exact-receipt control: `SOURCE_FORMULA_COMPARISON_EXACT.csv`, SHA-256 `EB566F2D37B52214FADE9D045EA20A8B9ECAB0C5DED524CD322601A6F9FFB9A4` at the audit snapshot.
- SGA 1–4 English precedents consulted at `01_recovered_witnesses/sga1_4_english_baselines/text_extraction/`; established English such as “base-change”, “direct image”, “adjunction”, and “Künneth” was retained.

## SHA-256 handoff

The stable tranche slice begins with the first prose line of §1.6 (`Let, for $i=1,2$...`) and ends immediately before the Exposé III B heading. It contains 2,248 LF-terminated lines.

| Object | Before | After |
|---|---|---|
| Exposé III tranche slice | `16EDE02536460FA5C652CABBC14156382236FBEF06884DC2191BEB9F1EC0D61C` (128,696 bytes) | `57EF63C62AF7E9C4C39AC0844A9E923C6AF671C323E3B719CCEAAD9784E33CC7` (123,647 bytes) |
| Full shared cumulative, observed | `AD48DF288B4928BB58B16B1F3A39A202BE086C852546ABC91FAE25732A11297B` | `237ACFB99BBD51A83495662F9D56260768DB7CFB4F22AE132583B2A3D71EF978` |

The tranche hashes are the authoritative before/after pair. The full-file pair is an observed integration pair only, because other agents edited disjoint exposés in the shared cumulative during this tranche.

## Receipt validation

- Required receipt IDs: 34.
- Expected-anchor criteria: 31/31 pass; combined criteria cover paired IDs 0318/0319, 0341/0343, 0342/0344, and 0355/0356.
- Old-form exclusion criteria: 25/25 applicable anchor-specific exclusions pass. Three global old-string searches were intentionally not used as exclusions because the strings occur legitimately at other source anchors (`smooth` without emphasis, `f'^!(Q...)`, and `g_*g^!`); the required receipt anchors themselves were checked directly and pass.
- Receipt 0314 received an additional source-direction correction: `f_!E\otimes^L_SP' \xrightarrow[\sim]{c} f'_!(E\otimes^L_SP')`.

## Structural and source-formula checks

Post-repair coarse parity for Exposé III is exact:

| Feature | English | French | Delta |
|---|---:|---:|---:|
| tags | 145 | 145 | 0 |
| equation environments | 145 | 145 | 0 |
| diagram blocks | 60 | 60 | 0 |
| `tikzcd` | 56 | 56 | 0 |
| `tikzpicture` | 4 | 4 | 0 |
| statements | 18 | 18 | 0 |
| footnotes | 3 | 3 | 0 |

Sixteen high-risk tagged equation/diagram blocks compare exactly after whitespace normalization and the mechanical French `\uRHom` to English `\RHom` spelling change: 2.4.0, 2.5.1, 3.3.0, 3.3.1, 3.4.1, 3.7.1, 3.7.2, 4.4.0, 4.4.1, 4.4.2, 4.4.6, 4.4.7, 5.1.7, 5.2.6, 5.3.6, and 6.7.1.

Sequential comparison of all 60 diagram blocks gives 54 textually exact normalized blocks. The remaining six were manually checked: two differ only by source punctuation, two by translated French labels, and two pre-existing source-equivalent layout/label-placement choices outside the repair queue. None has a missing/reversed arrow, wrong operator, or wrong node after this pass.

The generated parity evidence is:

- `audit_evidence/expose_iii_post_structural_summary.csv`
- `audit_evidence/expose_iii_post_structural_differences.csv`

## Scan-backed visual evidence

Rendered source pages used for topology and arrow-direction checks are under `audit_evidence/expose_iii_scan/`. They include printed pp. 83, 84, 86, 89, 94, 95, 98, 100, 102, 103, 105, 107, 114, 115, 116, 117, 118, and 126. The scan confirms the four source `tikzpicture` shapes, the p.105 proof routes, the p.107 arrows/operators, and the p.116/p.118 downward direct-image squares.

## Build gate and continuation

Compilation was deliberately deferred: the parent manager requested that Exposé III return before the final frozen cumulative build, because other agents were writing disjoint exposés. The parent should now freeze the cumulative, compile twice, render the affected pages, and add that build/visual-QA evidence to the final promotion manifest. A successful compile alone is not a completion claim; this report records the independent source/formula/topology checks that precede it.

Continuation disposition: Exposé III source-critical receipt and structural queue closed; no ambiguity carried forward.
