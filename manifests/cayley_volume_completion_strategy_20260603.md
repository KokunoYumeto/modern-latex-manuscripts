# Cayley Volume Completion Strategy - 2026-06-03

This note switches Cayley from a global "fill visible gaps anywhere" mode to a volume-by-volume completion mode.

## Policy

The reader-facing status should be understandable without decoding a scattered residual list:

- certify Volume I, then Volume II, then Volume III, and so on through Volume XIII;
- within the active volume, fix all public-reader residuals and source-visible placeholder/table notices that affect faithful transcription;
- only jump ahead for truly cheap or blocking repairs, or when a later fix is already staged and verified;
- keep source scans, TeX chunks, rendered reader PDFs, and residual manifests tied to the same volume status.

This does not discard the global residual list. It changes how we schedule it.

## Why Volume Order Wins

The global gap list is efficient for opportunistic repairs, but confusing for readers and funders. A volume ledger makes the public claim clearer:

- "Volumes I-III are source-checked first-pass readers; Volume IV is the current dense-table blocker" is legible.
- "17 residual markers remain somewhere in a 13-volume corpus" is not legible.
- Volume certification also gives a clean cost model: the late work is hard-page weighted, not page-count weighted.

## Current Residual Distribution

The public residual marker scan currently finds 17 reader-visible hits:

| Volume | Residual hits | Main type |
|---|---:|---|
| I | 0 | Candidate for certificate. |
| II | 0 | Candidate for certificate after source-package scan. |
| III | 0 | Candidate for certificate after source-package scan. |
| IV | 10 | Dense determinant/coefficient/Tschirnhausen tables. |
| V | 2 | Plate III and axial-system table. |
| VI | 0 | Candidate for certificate after source-package scan. |
| VII | 0 | Candidate for certificate after source-package scan. |
| VIII | 0 | Candidate for certificate after source-package scan. |
| IX | 1 | Tree plate/foldout. |
| X | 1 | Table No. 93 bis. |
| XI | 2 | Reuschle prime-root power tables. |
| XII | 0 | Candidate for certificate after source-package scan. |
| XIII | 1 | Table of Conjugates. |

## Active Order

1. Certify Volumes I-III as clean reader surfaces, checking source-package marker scans rather than only public-reader text.
2. Complete Volume IV. This is the first real blocker and has the largest residual cluster.
3. Complete Volume V.
4. Certify Volumes VI-VIII.
5. Complete Volumes IX-XI.
6. Certify Volume XII.
7. Complete Volume XIII.

If a later-volume repair is already staged and cheap, it can be folded in, but the public "done through volume N" line should advance only when every prior volume is clean by the same rule.

## Definition of Done for a Cayley Volume

A volume is "first-pass source-faithful complete" only when:

- the front-facing reader has no visible placeholder markers such as `[Figure:]`, `too dense`, `unreadable`, or "reader is referred to the original";
- the source TeX chunks have no source-visible placeholder summaries for formulas, tables, diagrams, or plates;
- known diagrams are native TeX/TikZ or explicitly source-faithful table/array TeX, not screenshots;
- compile logs do not show fatal errors and the reader opens with expected page count;
- source scans are present or the scan-location exception is documented;
- the manifest states remaining non-fatal caveats, if any.

## Immediate Next Work

The next repair target is Volume IV. Its current public residual hits are clustered at reader pages 37, 243, 250, 252, 272, 287, 373, 375, 376, and 380. These are mostly dense tables, so the efficient workflow is:

- locate the exact source TeX chunk and scan page;
- render/crop the printed table pages locally;
- reconstruct one bounded table block at a time;
- compile the affected slice;
- rebuild Volume IV after a batch, not after every single cell.

