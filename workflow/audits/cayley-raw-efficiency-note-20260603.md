# Cayley Raw Efficiency Note - 2026-06-03

This is a rough operational note, not an invoice or controlled benchmark. It records what the Cayley repair pass taught about cost, agent instructions, and likely remaining expenditure.

## Current Measurement Baseline

The Cayley corpus has to be measured in original source/book pages, not rendered modern-PDF pages. Reflowed TeX readers are shorter or longer than scans, so page counts are only approximate indicators.

Current best working numbers:

- Conservative pre-wave validated-pickup baseline from 2026-05-31: `3917 / 8394 = 46.7%`.
- June 1 repaired-tree baseline: `5922 / 8394 = 70.6%` strict, about `77.3%` inclusive.
- Current 2026-06-03 state: `5986 / 8394 = 71.3%` strict, about `79.7%` inclusive.
- Public TeX representation: `8234 / 8394 = 98.1%`, but this includes scaffold/OCR-risk material and must not be called faithful completion.
- Front-facing reader PDFs moved from 5439 rendered pages to 5713 rendered pages during the June 2-3 window, but that undercounts quality work inside already represented intervals.

Plain-language status: Cayley is roughly 70% strict and roughly 80% inclusive for first-pass source-faithful transcription. Nearly the whole corpus is represented somewhere in TeX, but the remaining 20-30% is disproportionately hard: coefficient tables, foldouts, plates, diagrams, dense numerical arrays, and old OCR scaffold.

## Raw Cost Heuristic

No per-agent telemetry is available in the repository. The useful cost statement is therefore directional:

- Claude and earlier swarm work converted much of the easier coverage into rough TeX and source-checked slices, but left many dense objects, tables, plates, and scaffold-risk ranges.
- The June 2-3 Codex-side repair wave used the weekly allowance plus roughly a 100 USD credit tranche while also maintaining GitHub, Zenodo staging, incoming-drop sweeps, and release manifests.
- Raw added page count is not the right output measure for this wave. Much of the value was turning already represented but not public-grade material into faithful TeX, repairing diagrams, reducing residual markers, and rebuilding public readers.

The broad takeaway is that early coverage is cheap per page; the last 20-30% is hard-page weighted. One remaining source page with a full coefficient table can cost more than ten prose pages.

## Expected Cost for the Rest of Cayley

These are planning ranges, not promises.

Assuming the improved workflow is used - bounded source slices, no blind retries, local OCR/crop preparation, local GPU where useful, and batched compile/render checks - the remaining faithful first pass is likely in this range:

- Low/optimistic: 250-400 USD equivalent if most remaining pages are scaffold cleanup and local GPU/OCR supplies adequate witnesses.
- Middle: 500-900 USD equivalent for a source-faithful first pass of remaining dense tables, plates, formulas, plus reader rebuilds.
- High/conservative: 1000-1500 USD equivalent if the remaining numerical tables require cell-by-cell verification and multiple visual QA passes.

This assumes no major platform blocking, no repeated failed agent swarms, no hallucinated replacement chunks, no repeated upload churn, and no decision to polish the whole corpus to final-proofreader quality in the same pass. A final scholarly typography pass would be a separate layer.

## Agent Instruction Lessons

Do not give a broad instruction such as "fix Cayley" and let agents improvise. That caused waste in earlier runs: agents spent context reading scans, then produced unusable output, partial summaries, screenshots, or blocked/frozen attempts.

Better agent contract:

- Give one bounded source range with explicit volume, source PDF pages, printed pages, and expected output path.
- State the output shape: TeX source, compiled PDF, source-scan slice, manifest, SHA/check note, and uncertainty list.
- Prohibit screenshots as substitutes for TeX in public reader material.
- Prohibit summaries or paraphrases being promoted as faithful transcription.
- Require source-page anchors and visible uncertainty markers instead of silent invention.
- Ask for cumulative replacement only when the range is small enough to rebuild safely; otherwise ask for a clean delta plus compile instructions.
- Require a final self-audit: page coverage, formulas/tables/diagrams present, visible TeX leakage, font failures, and overfull boxes.

## Token-Efficiency Lessons

Use cheap local work before expensive model vision:

- Run `pdftotext` or OCR text extraction first; use images only for formulas, tables, diagrams, or ambiguous readings.
- Render ordinary pages at 120-150 dpi. Use 300-600 dpi only for dense formula/table regions, and higher resolution only for genuinely unreadable cells.
- Do a cheap text-only probe before a vision-heavy sub-agent attempt on known blocked/filter-resistant ranges.
- Do not blind-retry a failed range more than once without changing the plan.
- Batch repairs, then compile. Avoid one-page-edit/one-full-reader-rebuild loops.
- Separate coverage categories in all reports: represented somewhere, source-checked repaired slice, promoted reader, fully audited final.

Local compilation, PDF rendering, hashing, zipping, and page counting are machine costs, not model-token costs. The model should spend tokens deciding ambiguous math and structure, not repeatedly discovering paths, re-rendering pages, or reading pages that local tools already summarized.

## Practical Next Strategy

For Cayley specifically:

- Continue from the residual-marker list and dense-object audit, not from naive page order alone.
- Use local crop/OCR witnesses to localize formulas/tables, but promote only scan-compared TeX.
- Keep raw provenance in the shared raw/provenance DOI and keep the Cayley author DOI compact.
- Rebuild readers after a small batch of related fixes, not after every page.
- Treat the final 20-30% as "hard-page weighted"; page count alone will make progress look slower than the actual quality gain.

