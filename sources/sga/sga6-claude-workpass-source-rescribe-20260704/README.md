# SGA6 Source-Rescribe Workpass Mirror

This folder mirrors the active Claude/Codex SGA6 source-rescribe workpass lane from `SGA continuation 2/_claude_aid/sga6_full_audit_20260703`.

Current public classification: source-rescribe/workpass provenance only. This is not a completed SGA6 reader release, not English synchronization, not whole-SGA6 source-faithfulness certification, not an index audit, not publication readiness, and not a critical edition.

Current GitHub frontier: `CERT_LOG.md` entry #355, scan idx358 / volume p345 / Exposé V p49; next cursor idx359 / volume p346 / Exposé V p50. The mirrored workpass compiles to 391 pages with no fatal LaTeX error. The log still reports a missing `Hfootnote.424` destination and harmless infinite-glue warnings.

The current immutable Zenodo release is [record 21300786](https://doi.org/10.5281/zenodo.21300786), frozen three source pages earlier at entry #352 / scan idx355. This GitHub mirror is deliberately allowed to move ahead between curated Zenodo releases; do not confuse the live mirror frontier with the frozen release boundary.

The audit found that earlier SGA6 material could compile cleanly while still containing compressed or missing pages, invented headings or statements, wrong relations, notation drift, and unsupported equation tags. Entry #355 restores an entire source page that the older scaffold silently skipped. The repair method therefore reads each scan page independently rather than trusting the scaffold's page structure. Use this mirror for continuation and provenance, not as closure.
