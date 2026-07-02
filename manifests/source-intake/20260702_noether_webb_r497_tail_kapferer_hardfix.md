# Noether WebB R497 Tail/Kapferer Hard-Source Fix

Date registered: 2026-07-02

Local artifact:

`C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Noether Multilingual\Noether_R497_WebB_TailKapfererHardFix_20260701_COMPLETE.zip`

Artifact metrics:

- Bytes: 21,442,329
- ZIP entries: 64
- SHA256: `05BF3A26A0714383002612C0AC4E5B0B9E5ACCF078554AEC333E0AF173855462`

## Classification

This is a self-contained WebB source-evidence companion and TeX-changing source-control artifact on the R496 WebB R485TailSchurRebase line. It is distinct from the similarly numbered local `Noether_R497_LocalCodex_R496_P22_CurrentSurvivalClosure_NoPatch_20260701.zip`, which is only a no-patch Paper 22 survival guardrail.

Treat this WebB R497 package as source-control/provenance for the later R527 Noether line, not as a standalone reader release and not as Noether closure.

## Promoted Fixes

The package README and `confirmed_fixes_R497.csv` identify three promoted source-backed repairs:

1. Post-P43 / Deuring collected p757: the conclusion changes from `\mathfrak a=\mathfrak Z\cdot\mathfrak H` to source `\mathfrak o=\mathfrak Z\cdot\mathfrak H`.
2. Kapferer/Noether, Math. Ann. 97 p559: the section title no longer includes non-source `: von H. Kapferer`; the source title period is restored.
3. Kapferer/Noether, Math. Ann. 97 p559: restores `Von Heinrich Kapferer in Freiburg i. Br.` and restores `in Göttingen` in the subtitle `(Mit einem Zusatz, gemeinsam mit E. Noether in Göttingen.)`.

## QA Evidence

- XeLaTeX pass 1 and pass 2 succeeded.
- `PDF_CHECKS_R497.json` reports cumulative PDF `cum_de_R497.pdf` with 471 pages.
- Changed output pages: 457 and 462.
- Included evidence: exact diff `diff_R496_to_R497.diff`, source witnesses for the Deuring tail and Kapferer opening, source zoom crops, before/after output crops, render manifests, guard checks, and SHA256 sums.

## Caveats

- This is not a critical edition, not whole-tail closure, not Noether closure, not whole-corpus page-by-page certification, and not multilingual synchronization.
- Source quality is mixed: the Deuring tail witness is best-available native about 360ppi zoomed evidence; the Kapferer witness is a stronger GDZ publication page image.
- Because Noether is at the Zenodo file ceiling, do not upload this as a loose micro-ZIP. Fold the repair and evidence into the next curated compact Noether rollup.

