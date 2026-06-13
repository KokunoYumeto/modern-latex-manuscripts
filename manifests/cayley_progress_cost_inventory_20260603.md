# Cayley Progress and Cost Inventory - 2026-06-03

This note records the current Cayley state using three separate page notions.
They should not be collapsed into a single completion percentage.

## Page notions

| Measure | Current meaning | Current observed value |
|---|---:|---:|
| Original scan/book pages | The historical Cayley volumes as scanned or printed. Scan PDF pages include front matter and sometimes do not match printed book pages exactly. | About 8000+ pages; prior chunk map counted 8394 source book pages. |
| Front-facing reader pages | Pages produced by the current promoted modern TeX reader PDFs. These are reflowed and can be shorter or longer than the original. | 13 PDFs, 5713 rendered pages, 71571613 bytes. |
| Older assembled scaffold pages | Earlier broad assembly before the current source-faithful filtering and repair pass. Useful provenance, not a clean completion claim. | 7216 rendered pages in the older inventory. |

The current front-facing Cayley readers are therefore not a one-to-one 5713/8394
coverage claim. They are the promoted reader surface after source-checked slice
repairs, public-source reconciliation, and removal or quarantine of worse OCR
scaffold material.

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

## Approximate faithful-transcription percentage

For the specific question "what percent is first-pass but complete faithful
transcription done?", the best current answer is an interval, not one magic
number.

| Basis | Original book-page intervals counted | Against old 8394-page chunk map | Against current 8234-page public chunk map | Interpretation |
|---|---:|---:|---:|---|
| Strict repaired-slice tree only | 5986 | 71.3% | 72.7% | Conservative count: pages sitting in the canonical repaired/source-checked slice tree. |
| Inclusive promoted-reader estimate | about 6690 | 79.7% | 81.3% | Adds the complete source-checked Volume I reader and the promoted Volume VIII lane, which currently live outside the repaired-slice tree. |
| Represented somewhere in public TeX | 8234 | 98.1% | 100% | Includes scaffold/OCR-risk pages and therefore must not be called faithful completion. |

So the human-facing status should be: Cayley is roughly **70% strict** and
roughly **80% inclusive** for first-pass source-faithful transcription, while
nearly all of the corpus is represented somewhere in TeX. The remaining
20--30% is disproportionately hard material: coefficient tables, foldouts,
plates, dense numerical arrays, and old OCR scaffold that should not be promoted
without source comparison.

## Approximate starting point for the current repair wave

Using the same interval-counting method at Git commit
`706f1813f0f793843b6b69e3ebe22ed8dd1c33bc` (2026-06-01 04:32 +0200, the last
Cayley-relevant snapshot before the June 1 daytime repair wave):

| Basis | June 1 snapshot | Current snapshot | Change |
|---|---:|---:|---:|
| Strict repaired-slice intervals | 5922 / 8394 = 70.6% | 5986 / 8394 = 71.3% | +64 original-page intervals |
| Inclusive estimate | about 6490 / 8394 = 77.3% | about 6690 / 8394 = 79.7% | about +200 original-page intervals |
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
repair/source material. For cost/progress claims, use the 46.7% number for the
first Claude/Cayley validated-pickup baseline and the 70--80% band for the
current promoted-source-tree baseline.

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
