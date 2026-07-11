# SGA6 Source-Rescribe Workpass Mirror

This folder mirrors the active Claude/Codex SGA6 source-rescribe workpass lane from `SGA continuation 2/_claude_aid/sga6_full_audit_20260703`.

Current public classification: source-rescribe/workpass provenance only. This is not a completed SGA6 reader release, not English synchronization, not whole-SGA6 source-faithfulness certification, not an index audit, not publication readiness, and not a critical edition.

Current frozen GitHub frontier: `CERT_LOG.md` entry #410, scan idx413 / volume p400 / Exposé VI p36; next cursor idx414 / volume p401 / Exposé VI p37. The mirrored workpass compiles to 389 pages with no fatal LaTeX error, overfull boxes, or underfull boxes. The log retains four inherited accent-command warnings and a missing `Hfootnote.424` destination.

The current immutable Zenodo release is [record 21306092](https://doi.org/10.5281/zenodo.21306092), frozen at the same entry #410 / scan idx413 boundary. This GitHub mirror may move ahead between later curated Zenodo releases, but this checked-in snapshot matches the July 11 release.

The audit found that earlier SGA6 material could compile cleanly while still containing compressed or missing pages, invented headings or statements, wrong relations, notation drift, and unsupported equation tags. Entries #355 and #356 restore two entire source pages that the older scaffold silently skipped. The pagewise cursor has now traversed Exposé V pp47-68 and Exposé VI pp1-36, including substantial notation, relation, display-structure, and diagram repairs. The first page beyond the cursor already shows known `K^\bullet`/`K'` drift, so the stated boundary must not be read as whole-volume coverage. The repair method reads each scan page independently rather than trusting the scaffold's page structure. Use this mirror for continuation and provenance, not as closure.
