# Audit Status

- Authority: direct Paper 30 source slice, pages 37-61.
- Baseline: public cumulative German R823 TeX.
- Candidate: web-session hard-math patch.
- Archive review: all six hunks inspected; four principal loci checked with enlarged source/before/after stacks.
- Rejected candidate: `durch` -> `dnrch` at the composition-series sentence. The scan's Fraktur `u` was misread as `n`; the corrected patch retains `durch`.
- Accepted classes: `x` -> `\varkappa` where the scan uses kappa; `\varrho`/`\sigma` repair where source exponents differ; Fraktur `X` -> `T`; source line-flow and quotation repairs.
- Build: two-pass LuaLaTeX, 466 pages, zero forbidden diagnostics in the final log.
- Public classification: bounded source-control supplement; not a complete paper certification, not translation synchronization, and not a critical edition.
