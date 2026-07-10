# SGA6 Source-Rescribe Workpass Mirror

This folder mirrors the active Claude/Codex SGA6 source-rescribe workpass lane from `SGA continuation 2/_claude_aid/sga6_full_audit_20260703`.

Current public classification: source-rescribe/workpass provenance only. This is not a completed SGA6 reader release, not English synchronization, not whole-SGA6 source-faithfulness certification, not an index audit, not publication readiness, and not a critical edition.

Current frozen GitHub frontier: `CERT_LOG.md` entry #376, scan idx379 / volume p366 / Exposé VI p2; next cursor idx380 / volume p367 / Exposé VI p3. The mirrored workpass compiles to 390 pages with no fatal LaTeX error, overfull boxes, or underfull boxes. The log retains three accent-command warnings in math mode and a missing `Hfootnote.424` destination.

The current immutable Zenodo release is [record 21302915](https://doi.org/10.5281/zenodo.21302915), frozen at the same entry #376 / scan idx379 boundary. This GitHub mirror may move ahead between later curated Zenodo releases, but this checked-in snapshot matches the July 11 release.

The audit found that earlier SGA6 material could compile cleanly while still containing compressed or missing pages, invented headings or statements, wrong relations, notation drift, and unsupported equation tags. Entries #355 and #356 restore two entire source pages that the older scaffold silently skipped. The pagewise cursor has traversed Exposé V pp47-68 and entered Exposé VI through p2, including diagram and notation repairs in the Exposé V tail. The repair method therefore reads each scan page independently rather than trusting the scaffold's page structure. Use this mirror for continuation and provenance, not as closure; material after the stated cursor in the compiled PDF remains inherited scaffold until directly checked.
