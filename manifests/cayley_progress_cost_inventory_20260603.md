# Cayley Progress and Cost Inventory - 2026-06-03

This note records the current Cayley state using three separate page notions.
They should not be collapsed into a single completion percentage.

## Page notions

| Measure | Current meaning | Current observed value |
|---|---:|---:|
| Original scan/book pages | The historical Cayley volumes as scanned or printed. Scan PDF pages include front matter and sometimes do not match printed book pages exactly. | About 8000+ pages; prior chunk map counted 8394 source book pages. |
| Front-facing reader pages | Pages produced by the current modern TeX reader PDFs. These are reflowed and can be shorter or longer than the original. They are now treated as draft/provenance readers, not promoted source-faithful editions. | 13 PDFs, 5713 rendered pages, 71571613 bytes. |
| Older assembled scaffold pages | Earlier broad assembly before the later filtering and repair pass. Useful provenance, not a clean completion claim. | 7216 rendered pages in the older inventory. |

The current front-facing Cayley readers are therefore not a one-to-one 5713/8394
coverage claim. They are a reader/provenance surface after several repair and
reconciliation passes, but later source comparison found substantial symbol/text
mismatches in Volume I material. No Cayley range is currently promoted as
source-faithful until a new page-by-page glyph/source audit re-promotes it.

## Current front-facing reader surface

| Volume | Reader pages | Bytes |
|---|---:|---:|
| I | 488 | 7764737 |
| II | 421 | 3977622 |
| III | 322 | 3774202 |
| IV | 496 | 5883389 |
| V | 443 | 6186480 |
| VI | 407 | 4159529 |
| VII | 336 | 4852925 |
| VIII | 536 | 6015885 |
| IX | 348 | 5211862 |
| X | 576 | 6833979 |
| XI | 415 | 4779372 |
| XII | 437 | 6001148 |
| XIII | 488 | 6130483 |

## Withdrawn faithful-transcription percentage

The table below is retained as a historical 2026-06-03 project-management
estimate only. It must not be cited as a current faithful-transcription
percentage. Later direct source comparison showed that material previously
counted as repaired/source-checked can still contain substantial symbol/text
mismatches. The honest current status is: nearly the whole corpus has some TeX
representation, but the source-faithful percentage is not certified and must be
re-established by page-by-page audit.

| Basis | Original book-page intervals counted | Against old 8394-page chunk map | Against current 8234-page public chunk map | Interpretation |
|---|---:|---:|---:|---|
| Strict repaired-slice tree only | 5986 | 71.3% | 72.7% | Historical count of pages sitting in the then-current repaired/source-checked slice tree; current source-faithfulness withdrawn pending re-audit. |
| Inclusive reader estimate | about 6690 | 79.7% | 81.3% | Historical reader-surface estimate including Volume I and Volume VIII lanes; current source-faithfulness withdrawn pending re-audit. |
| Represented somewhere in public TeX | 8234 | 98.1% | 100% | Includes scaffold/OCR-risk pages and therefore must not be called faithful completion. |

So the human-facing status should be: Cayley has broad TeX representation and
many useful repair surfaces, but **no current certified source-faithful
completion percentage**. The remaining visible and invisible risk includes
coefficient tables, foldouts, plates, dense numerical arrays, old OCR scaffold,
and ordinary formula/prose passages whose symbols may not match the source.

## Approximate starting point for the current repair wave

Using the same interval-counting method at Git commit
`706f1813f0f793843b6b69e3ebe22ed8dd1c33bc` (2026-06-01 04:32 +0200, the last
Cayley-relevant snapshot before the June 1 daytime repair wave):

| Basis | June 1 snapshot | Current snapshot | Change |
|---|---:|---:|---:|
| Strict repaired-slice intervals | 5922 / 8394 = 70.6% | 5986 / 8394 = 71.3% | +64 original-page intervals; source-faithfulness later withdrawn pending re-audit |
| Inclusive estimate | about 6490 / 8394 = 77.3% | about 6690 / 8394 = 79.7% | about +200 original-page intervals; source-faithfulness later withdrawn pending re-audit |
| Represented somewhere in public TeX | 8234 / 8394 = 98.1% | 8234 / 8394 = 98.1% | unchanged |
| Front-facing rendered reader pages | 5439 pages | 5713 pages | +274 rendered pages |

This shows that the June 2--3 work was not mainly "add raw pages that had no TeX
file." It was mostly quality conversion inside already represented intervals:
removing placeholders, replacing screenshots/prose witnesses with native TeX or
TikZ, fixing source-visible formulas, rebuilding readers, and reducing visible
residual markers.

There is also an older conservative pre-wave inventory from 2026-05-31:
`3917 / 8394 = 46.7%` validated pickup book pages. That number is stricter
because it only counted slices explicitly marked as scan-validated pickup
material, while the June 1 repaired-tree count includes more already-imported
repair/source material. For cost/progress claims, these figures should now be
described as workflow-throughput and represented-coverage estimates, not as
current source-faithful completion percentages.

## What "not missing ordinary coverage" means

In the 2026-06-03 Cayley repair notes, this phrase means only that the visible
remaining markers in the promoted readers are concentrated in dense mathematical
objects: coefficient tables, Reuschle tables, plates, foldouts, or source-visible
diagram/table witnesses.

It does **not** mean:

- every original Cayley source page has been verified;
- every old scaffold chunk has been promoted;
- rendered reader pages can be compared one-for-one with original printed pages.

The honest status is: the public Cayley DOI is now a much better reader surface,
but the project remains in source-audit mode until the remaining dense tables and
any source-page coverage gaps are closed.

## Cost and throughput notes

No per-agent billing telemetry is visible in this repository. The cost notes are
therefore project-management context, not invoiced measurements.

- Prior user-side estimate for the first Claude/Cayley push: roughly 3000+
  pages of material from scratch, plus EGA/Gauss/download triage in parallel,
  against roughly 30-50 USD of subscription-equivalent usage.
- Later user-side note on 2026-06-03: the weekly allowance plus an additional
  100 USD Codex credit tranche had been used or partly used while Cayley repair
  and archive management were running.
- Verifiable local output over the current repair window: a dedicated Cayley
  author DOI exists, the GitHub mirror has 13 front-facing reader PDFs, and the
  residual marker scan has been reduced to 17 visible public-reader hits after
  the Volume XIII square-diagram repair.

The practical lesson is that the cheapest reliable workflow is not "one page,
compile, repeat." It is: local source/OCR/scan preparation, batched repair of a
bounded slice, short-path compile and render verification, then reader rebuild
only after the slice passes. GPU/local OCR or crop-localisation work should be
used to reduce expensive model vision reads, but candidate TeX is not promoted
without scan comparison.

Efficiency caveat, 2026-06-03: the current Codex spend context should be read as
"weekly allowance plus roughly a 100 USD credit tranche used while doing Cayley
repair and project management," not as a page-price measurement. The last wave
was disproportionately spent on harder residual work left after earlier easy
coverage: dense tables, diagrams, source-visible formulas, reader rebuilds, DOI
patches, and manifest/accounting cleanup. For that reason the raw page-count
increase from June 1 to June 3 underreports the value of the work: many pages
were already represented by filename range but were not yet public-grade
faithful TeX.

## Known provenance/source note

The Claude `_scans` subfolder currently holds source scans for twelve Cayley
volumes. Volume VIII's source scan is present elsewhere in the Claude output tree
as `Cayley_Collected_Mathematical_Papers_Vol_VIII_source_scan.pdf`, but is not in
that `_scans` subfolder. This is a provenance-location cleanup item, not evidence
that Volume VIII reader material is missing.
