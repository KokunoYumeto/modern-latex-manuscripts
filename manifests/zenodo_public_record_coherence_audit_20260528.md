# Zenodo Public Record Coherence Audit

Generated: 2026-05-28

## Current Entry Points

- Main landing page: https://zenodo.org/records/20415117
- EGA working translation: https://zenodo.org/records/20425537
- SGA working translation: https://zenodo.org/records/20427838
- Non-European and multilingual mathematics consolidated corpus: https://zenodo.org/records/20427329
- Weber author record: https://zenodo.org/records/20425697
- Noether author record: https://zenodo.org/records/20422936

## Metadata Cleanups Applied

- The main landing page now points to SGA `20427838`, states that the current SGA 5 reader is complete, and explains that older cross-author shelves are preservation surfaces while author/corpus pages are the recommended public entry points where they exist.
- The historical-reference record was retitled from a witness-centered name to `Historical Reference Texts for Non-European Mathematics: LaTeX and Translation Drafts`, with a description explaining that it is a focused slice of the consolidated non-European corpus.
- The classical algebra/arithmetic record was retitled to `Cayley, Dedekind, Dirichlet, Gauss, Weber, and Noether: Classical Algebra and Arithmetic LaTeX Drafts`, with explicit author coverage and a note that Weber/Noether author pages supersede duplicate front-facing material.

## Keep / Supersede Map

- Keep `20415117` as the single project landing and broad preservation surface.
- Keep `20427329` as the main non-European/multilingual front door.
- Keep `20421647`, `20421650`, `20421656`, and `20421657` as focused non-European corpus slices for smaller downloads, but describe them as subordinate slices of the consolidated corpus.
- Keep `20418609` as a legacy classical algebra/arithmetic shelf until Cayley, Dedekind, Dirichlet, and Gauss each have checked author-level pages.
- Treat Weber `20425697` and Noether `20422936` as cleaner author-level public entry points that supersede duplicate Weber/Noether material in the classical shelf.
- Keep `20416839` as an author-cluster page for now; split into author-level records only when individual authors have enough checked, human-readable material to justify the extra DOI surface.
- Keep Deligne separate so it can be revised or removed independently if needed.

## Next Coherence Work

- Build author-level pages only when the reader-facing quality is good enough and the page has a clear title, author list, status, and artifact ZIP.
- Do not publish new DOI surfaces named after internal drops, repair passes, or tool workflows.
- Prefer metadata-only cleanups over deletion when a record is already public and contains useful work.
- When an author-level page supersedes duplicate material in a shelf, say so in both records rather than silently removing files.
- Keep top-level PDFs reader-facing and keep TeX/source/provenance/repair queues in ZIP artifacts.

