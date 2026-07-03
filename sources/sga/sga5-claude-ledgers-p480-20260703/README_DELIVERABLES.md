# SGA 5 — source-faithful LaTeX edition + errata: deliverables

This folder holds a hand-certified, source-faithful LaTeX edition of **SGA 5** (Lecture Notes in Math.
589, *Cohomologie ℓ-adique et fonctions L*), covering the 10 curated exposés
**I / III / III B / V / VI / VII / VIII / X / XII / XV**. Every printed page was read against the scan
by hand, symbol by symbol, and every discrepancy was fixed or flagged. The build is stable at
**306 pages, 0 LaTeX errors**.

## The deliverables

| File | What it is |
|------|------------|
| [`sga5_fr_workpass.tex`](sga5_fr_workpass.tex) | **The edition.** Compiles to `sga5_fr_workpass.pdf` (306 pp / 0 err). |
| [`sga5_fr_workpass.pdf`](sga5_fr_workpass.pdf) | The compiled edition. |
| [`ERRATA_LNM589.md`](ERRATA_LNM589.md) | **Errata to the printed book** — every source typo / inconsistency found, by exposé and page, each tagged `[corrected]` (edition silently fixed it), `[faithful]` (edition reproduces the book), or `[normalized]`. Every disposition is verified against the edition's `.tex`. |
| [`METHOD_AND_LESSONS.md`](METHOD_AND_LESSONS.md) | **Method & lessons write-up** for the open-source release — how the by-hand certification was done, the taxonomy of transcription defects, the swarm scorecard, and an honest status disclaimer. |
| [`CERT_LOG.md`](CERT_LOG.md) | The per-page certification ledger + the live resume cursor. |
| [`AGENT_SCORECARD.md`](AGENT_SCORECARD.md) | Scoring of the prior audit-swarm's precision/recall, page by page. |
| [`FINDINGS.md`](FINDINGS.md) / [`FINDINGS_consolidated_20260624.md`](FINDINGS_consolidated_20260624.md) | The raw per-page findings logs (Exposé I hand-pass; swarm-era changelog). |
| [`_work/swarm_results/workpass_vs_repair032.diff`](_work/swarm_results/workpass_vs_repair032.diff) | Full diff of the edition against the pre-audit `repair032` baseline (386 hunks). |
| [`_work/chunk_page.py`](_work/chunk_page.py), `_work/src/zoom/*.py` | Rerunnable page-render / 600 dpi zoom tooling. |

## What was found (headline numbers)

- **480 printed pages** certified by hand (p435 is a physical duplicate of p434 in the book).
- **52 `.tex` fixes** (+1 cosmetic) — all wrong-symbol-in-display or dropped word/paragraph; the
  mathematics was faithful throughout.
- **193 diagrams** verified edge-by-edge; **8/8 `cqfd` markers** confirmed present in the scan.
- **Errata:** the printed book's own typos, organized by exposé. The edition silently corrected the
  clear ones (disclosed) and kept coherent notational abuses faithful (noted).

## Status — read this

This is a **complete by-hand, page-by-page pass** — a trustworthy base, **not** a proof of correctness
or completeness. Error rates of ~1 per 2 pages persist even in clean prose, so a second independent
pass would still find things. Treat the edition as a strong, motivated, *provisional* base: better than
the raw scan and better than the machine-audit output it was built from, but a working draft, not a
theorem. See `METHOD_AND_LESSONS.md` § *Status* for the full disclaimer.

*Source scan: `…/OS/SGA5 (1).pdf` (LNM 589, 496 PDF pp = printed p1–484; printed page = PDF page − 12).*
