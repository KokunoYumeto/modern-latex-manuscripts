# Contributing

Useful contributions include:

- checking a modern LaTeX draft against the original scan;
- fixing TeX compilation or layout problems;
- repairing diagrams, tables, theorem numbering, and cross-references;
- improving translation drafts while preserving mathematical content;
- pointing to better public-domain source scans;
- opening issues for illegible pages, corrupted files, or doubtful provenance.

Before starting, check:

- [Adoption and mirror board](docs/adopt.md) for current work,
  ready-for-adoption work, future scopes, exact cursors, and declared mirrors;
- [Reusable workflow protocols](docs/adopt-flows.md) for the exact start,
  inputs, evidence, stop, and handback contract behind each board token;
- [GitHub coverage maps](docs/github-maps.md) for the author, work, series, or corpus;
- [GitHub reader shelves](reader-pdfs/README.md) for direct PDFs already present;
- [GitHub source shelves](sources/README.md) for exact tracked source generations;
- [GitHub archive history](docs/github-archive.md) for manifests and commit-pinned readback receipts;
- [Browse index](docs/browse-index.md) for the fastest route to the right corpus;
- [Noether translation coverage](docs/noether-map.md) before starting or assigning any Noether translation;
- [By author and work](docs/by-author-and-work.md) for a named-work overview;
- [Quality rubric](docs/quality-rubric.md) for draft/review vocabulary;
- [Known gaps](docs/known-gaps.md) to avoid duplicating already-known unfinished areas;
- [Work queue](docs/work-queue.md) for concrete next tasks.

An unchecked, source-only, non-cumulative, or partial target is still existing
work. Do not start a new translation merely because there is no polished reader
or because an older directory name sorts first. Open the coverage map, locate
the exact generation, and continue only from its recorded cursor. If the map is
wrong, correct the map and preserve the contradictory evidence rather than
silently replacing either generation.

For Noether, review or correct a complete target; continue a partial target only at the cursor recorded in `docs/noether-map.md`. Any change that adds or advances a Noether translation checkpoint must update that map and the `GitHub Source Checkpoints` section of `docs/records/noether.md` in the same commit with the language, work, exact coverage, current path, quality state, and next cursor. The catalog generator preserves that section on overwrite. Navigation is not custody: include the actual source and artifact bytes, never just an inventory or status claim.

Please include:

- the author/work title;
- the exact GitHub path and, when reporting a fixed generation, its commit or byte hash;
- page, theorem, section, or equation number where possible;
- a source scan or bibliographic reference;
- a short explanation of the proposed correction.

An external producer receipt may be included as additional evidence, but it is
not a substitute for identifying the GitHub path that needs cataloging or
correction.

GitHub issue templates are provided for correction reports and source/work suggestions. Pull requests should use the template checklist and keep changes focused on the named work or file.

For a new continuation, repair lane, independent mirror, or source-intake
effort, open one
[adoption issue](https://github.com/KokunoYumeto/modern-latex-manuscripts/issues/new?template=adopt.yml).
Name the exact board ID and bounded scope. The issue makes overlap visible; it
does not reserve the work or prevent an independent check. Return an inspectable
repository/branch/result identity and the exact checks performed when the work
is ready.

Return a completed or partial result, paused scope, or withdrawal through the
[handback issue](https://github.com/KokunoYumeto/modern-latex-manuscripts/issues/new?template=handback.yml).
Bind it to the original adoption issue and include the achieved scope, exact
commit and output identities, manifest hashes, checks/failures/reversals, next
cursor, and reusable workflow findings. A handback is evidence, not an
automatic completion or certification claim.

For translation corrections, preserve the mathematical assertion first. Prefer a literal but readable translation over stylistic rewriting that changes scope, hypotheses, numbering, or dependency structure.

For TeX corrections, keep changes narrow: fix the broken environment, cross-reference, display, diagram, table, or page break without reformatting unrelated sections.

Preserve rights and provenance notes exactly and do not invent a license. Keep
modern publisher wrappers or unrelated third-party apparatus distinguishable
from the mathematical work, but do not silently drop already-custodied
mathematical bytes because a catalog-level rights note is incomplete.
