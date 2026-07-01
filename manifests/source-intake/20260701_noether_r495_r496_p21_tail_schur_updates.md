# Noether R495-R496 P21 Survival and Tail/Schur Source Fixes

Date registered: 2026-07-01

Local Noether root:
`C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Noether Multilingual`

## R495

`Noether_R495_LocalCodex_R485_P21_CurrentSurvivalClosure_NoPatch_20260701.zip`

- Bytes: 6,069,608
- ZIP entries: 12
- SHA256: `9139BC381334718372154F245DC48DA030A18A68562A556751BF328C4344CB11`
- Classification: no-patch current-span survival closure / guardrail.
- Base: R485 cumulative German TeX/PDF.
- Scope: Paper 21 current survival closure.
- Finding: R485 Paper 21 span and R476 source-vetted bridge Paper 21 span are byte-identical.
- Guardrails carried forward: the R299/R476 source-backed `\varrho` repair survives in R485; the final invariant-variational-problems paragraph keeps source-backed `G_\varrho` and the associated `\varrho` parameter/function/dependency readings.
- Source caveat: this is survival closure against already source-vetted bridge evidence, not a fresh full Paper 21 page-by-page certification.

## R496

`Noether_R496_LocalCodex_R485_WebB_R484_TailSchurDenseFixes_20260701.zip`

- Bytes: 34,681,872
- ZIP entries: 27
- SHA256: `4C734842CEF9796880BD90399D68E62FB60E089F067955224030ED0972E3FABF`
- Classification: narrow TeX-changing source-backed repair candidate on top of R485.
- Base: local R485 cumulative. WebB R484 is not adopted as a whole new base.
- Scope: exactly five source-image-confirmed R101/post-P43 tail fixes from WebB R484 that were still absent from R485.
- Patched loci:
  - Collected p748 / source PDF page 38: removed non-source `(k)` superscript from the second `\alpha_{ij}` in the homomorphism chain.
  - Collected p753 / source PDF page 43: removed source-invisible orphan period after display.
  - Collected p754 / source PDF page 44: restored multiplication dot after `d_{\mu\nu}` in the Kronecker-product display.
  - Collected p755 / source PDF page 45: restored two multiplication dots in crossed associativity law.
  - Collected p755 / source PDF page 45: restored multiplication dot after `a_{S,T}^{R^{-1}}` in the following derivation.
- Included evidence: patched cumulative TeX/PDF after two XeLaTeX passes; `audit/confirmed_fixes_R496.csv`; `audit/diff_R485_to_R496.diff`; WebB R484 provenance ZIP; extracted source zoom crops/source-page PDF; rendered fixed output pages where render tooling was available.
- Source caveat: fixes are accepted from WebB only because they are tied to explicit source-page images/zoom crops and exact old/new TeX; OCR/AI prose is not used as authority.

## Refreshed Second-Web Intake Count

Folder: `Noether_SecondWebProject_Intake_20260701`

- Added payloads: `32_R495_P21_CURRENT_SURVIVAL_CLOSURE_NOPATCH.zip` and `33_R496_WEBB_R484_TAIL_SCHUR_FIXES_PROMOTED.zip`
- Total ZIP payloads: 31
- Total ZIP bytes: 4,280,844,139
- Top-level files: 36
- Top-level file bytes: 4,280,860,376
- Classification: source-and-state intake for a second concurrent ChatGPT Pro/Web Noether project; not a reader-facing release.

## Public Classification

R495 is a no-patch current-survival guardrail on top of R485. R496 is a narrow source-backed TeX-changing repair candidate on top of R485 for five post-P43 tail/Schur loci. R496 should supersede R485 for those five loci only; it is not a whole new Noether source closure and not a blanket adoption of WebB R484.

These materials should be folded into the next curated Noether rollup or used as source-audit continuation guardrails; they should not be uploaded loose above useful reader PDFs while the Noether Zenodo record is at the file ceiling.

They are not reader releases, Noether closure, whole-corpus page-by-page certification, multilingual synchronization, global source closure, or critical-edition material.
