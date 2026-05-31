# Cayley Claude Current Pickup Coverage

Generated: 2026-05-31 22:13:07

This report treats Claude's `cayley_codex_pickup` folder as the current clean-ish, scan-grounded Cayley surface. It does not promote the older full-volume cumulative PDFs as clean; those remain working drafts and provenance material until their bad sections are replaced.

## Headline

- Current pickup PDFs: **223**.
- Range/slice PDFs counted for source-page coverage: **220**.
- Surgical one-paper/one-section fix PDFs: **3**.
- Rendered pages in pickup PDFs: **5,378**.
- Unique source-scan page coverage from named ranges: **6,304 / 8,304 pages = 75.9%** across the 13 main Cayley volumes.
- Pickup size on disk: **65.1 MB**.

## Per-Volume Coverage

| Vol | Source scan pages | Covered source pages | Coverage | Missing source pages | Range PDFs | Surgical fix PDFs | Main missing ranges |
|---:|---:|---:|---:|---:|---:|---:|---|
| I | 620 | 423 | 68.2% | 197 | 16 | 0 | 1-12; 38-50; 251-300; 376-400; 426-450; 501-525; 574-620 |
| II | 628 | 462 | 73.6% | 166 | 15 | 0 | 388-400; 476-628 |
| III | 594 | 288 | 48.5% | 306 | 13 | 0 | 101-137; 176-225; 276-287; 388-594 |
| IV | 648 | 520 | 80.2% | 128 | 19 | 2 | 1-25; 546-648 |
| V | 650 | 578 | 88.9% | 72 | 18 | 0 | 579-650 |
| VI | 636 | 636 | 100.0% | 0 | 13 | 0 |  |
| VII | 652 | 507 | 77.8% | 145 | 17 | 1 | 401-450; 476-500; 583-652 |
| VIII | 640 | 570 | 89.1% | 70 | 18 | 0 | 571-640 |
| IX | 650 | 405 | 62.3% | 245 | 19 | 0 | 19-25; 38-50; 76-112; 201-250; 276-375; 563-575; 626-650 |
| X | 640 | 586 | 91.6% | 54 | 20 | 0 | 587-640 |
| XI | 672 | 412 | 61.3% | 260 | 15 | 0 | 26-50; 276-325; 438-450; 501-672 |
| XII | 680 | 467 | 68.7% | 213 | 19 | 0 | 238-262; 276-300; 326-350; 491-500; 553-680 |
| XIII | 594 | 450 | 75.8% | 144 | 18 | 0 | 151-200; 501-594 |

## Interpretation

- The pickup is now much larger than the older 124/127-file reports: **223 PDFs** are present.
- The page count is a lower-bound productivity measure, because it excludes surgical fixes that do not have a page-span filename and it excludes broad but unverified working TeX/PDF.
- The current state is best described as: a large validated slice corpus, not yet a clean per-volume edition.
- Good next archive shape: keep these slices public and clearly labeled as scan-grounded repair slices, keep old cumulative volumes in artifact/provenance status, and only promote reconstructed per-volume readers once gaps are filled and visual equation QA is done.

## Cost / Grant Baseline

- If one uses the recent Claude Code subscription run as a rough baseline, the work produced at least this many scan-grounded Cayley source pages while also doing Gauss, EGA, downloads, and orchestration. That means the Cayley-only page-per-dollar estimate is conservative in the sense that other work consumed part of the same budget.
- Do not present this as final proofread scholarly quality. Present it as evidence that AI-assisted scan-to-TeX repair can convert thousands of pages into usable, inspectable modern TeX/PDF in days, with a remaining human/AI verification layer.
- For grant planning, budget multipliers should account for hard pages: dense invariant tables, large displayed formulae, diagrams, multilingual passages, and final source comparison.

## Pickup Sync Check

- Source-TeX PDFs under `cayley_v2_fixes/sources_tex_Vol_*`: **209**.
- Source PDFs named in pickup manifest: **227**.
- No current source-TeX PDFs are missing from the pickup manifest.
- Manifest source names no longer visible in `sources_tex`: **18**. Usually harmless if they came from older staging or hand-built fixes; see JSON.

## Key Paths

- Pickup folder: `LOCAL_CLAUDE_OUTPUTS\cayley_codex_pickup`
- Pickup manifest: `LOCAL_CLAUDE_OUTPUTS\cayley_codex_pickup\MANIFEST.md`
- Active Claude fixes: `LOCAL_CLAUDE_OUTPUTS\cayley_v2_fixes`
- Local source scans: `LOCAL_SOURCE_LIBRARY\OS\Cayley`
- Machine-readable JSON: `LOCAL_CODEX_WORKSPACE\manuscript_translation_project\reports\cayley_claude_current_pickup_coverage_20260531.json`
- CSV: `LOCAL_CODEX_WORKSPACE\manuscript_translation_project\reports\cayley_claude_current_pickup_coverage_20260531.csv`

