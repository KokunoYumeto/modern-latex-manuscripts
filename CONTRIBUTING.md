# Contributing

Useful contributions include:

- checking a modern LaTeX draft against the original scan;
- fixing TeX compilation or layout problems;
- repairing diagrams, tables, theorem numbering, and cross-references;
- improving translation drafts while preserving mathematical content;
- pointing to better public-domain source scans;
- opening issues for illegible pages, corrupted files, or doubtful provenance.

Before starting, check:

- [Browse index](docs/browse-index.md) for the fastest route to the right corpus;
- [Noether translation coverage](docs/noether-map.md) before starting or assigning any Noether translation;
- [By author and work](docs/by-author-and-work.md) for a named-work overview;
- [Archive guide](docs/archive-guide.md) for the right Zenodo record;
- [Project status dashboard](docs/project-status-dashboard.md) for current public-surface counts;
- [Quality rubric](docs/quality-rubric.md) for draft/review vocabulary;
- [Public file catalog](docs/public-file-catalog.md) for the exact filename;
- [Known gaps](docs/known-gaps.md) to avoid duplicating already-known unfinished areas;
- [Work queue](docs/work-queue.md) for concrete next tasks.

For Noether, an unchecked target or a missing cumulative reader is still an existing translation. Review or correct a complete target; continue a partial target only at the cursor recorded in `docs/noether-map.md`. Any change that adds or advances a Noether translation checkpoint must update that map in the same commit with the language, work, exact coverage, current path, quality state, and next cursor. The map is navigation only: include the actual source and artifact bytes, never just an inventory or status claim.

Please include:

- the author/work title;
- the Zenodo record and filename;
- page, theorem, section, or equation number where possible;
- a source scan or bibliographic reference;
- a short explanation of the proposed correction.

GitHub issue templates are provided for correction reports and source/work suggestions. Pull requests should use the template checklist and keep changes focused on the named work or file.

For translation corrections, preserve the mathematical assertion first. Prefer a literal but readable translation over stylistic rewriting that changes scope, hypotheses, numbering, or dependency structure.

For TeX corrections, keep changes narrow: fix the broken environment, cross-reference, display, diagram, table, or page break without reformatting unrelated sections.

Do not add copyrighted front matter, publisher wrappers, editorial prefaces, or collected-volume apparatus unless it is clearly public-domain or explicitly licensed. The project aims to preserve the original public-domain mathematical works and their machine-assisted transcriptions, not modern publisher packaging.
