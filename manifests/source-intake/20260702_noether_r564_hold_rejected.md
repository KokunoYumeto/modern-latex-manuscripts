# Noether R564 Hold / Rejection Receipt

Date: 2026-07-02

Local artifact:

`C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Noether Multilingual\Noether_R564_LocalCodex_R563_Tail_p730_731_xVariableDenseFormulaFix_20260702`

Role: newer local Noether tail folder found during sweep, but **not** promoted. R563 remains the current promoted local TeX-changing German source-control head.

## Decision

Hold / reject for public promotion.

R564 changes a dense tail passage from `x_i`, `x_q`, `x_{q+1}`, etc. to `\chi_i`, `\chi_q`, `\chi_{q+1}`, etc. The source witness for collected p731 visibly uses `x`, not `\chi`, throughout the checked passage. This is therefore a source-mismatch trap, not a source-confirmed correction.

## Evidence Observed

- Cumulative German TeX: `cum\cum_de_R564_tail_p730_731_xvariable_densefix.tex`
- Cumulative German PDF: `cum\cum_de_R564_tail_p730_731_xvariable_densefix.pdf`
- Build logs: `cum\xelatex_R564_pass1.log`, `cum\xelatex_R564_pass2.log`
- Render checks: `renders\R564_cum_output_p433_434-433.png`, `renders\R564_cum_output_p433_434-434.png`
- Source witness: `source_witnesses\tail_src_collected_p731_1000dpi.png`
- Diff file present but empty: `audit\diff_R563_to_R564.diff`

The folder does not contain a README, confirmed-fix ledger, source-quality ledger, SHA256 provenance list, or a non-empty exact diff comparable to R563.

## Verification

- R563 TeX SHA256: `25DA49C074DA9768A87021EBAF99F2631CA285E1F7473C80F123C876A2031F54`
- R564 TeX SHA256: `54FC055A384782466F0A91418C98E83AD1EB0413284C7C67BBBA076745D63CEE`
- R564 pass-2 log scan found no fatal/runaway/missing-dollar failures, only font-substitution warnings.
- Source image check on collected p731 confirms the printed formula passage uses `x`, not `\chi`, at the candidate change loci.

## Public Caveat

Do not describe R564 as current, repaired, source-confirmed, or promoted. If mentioned publicly, it should only be mentioned as a held local false-positive candidate found during the July 2 sweep. R563 remains the current promoted local Noether source-control head until a later source-confirmed package supersedes it.

