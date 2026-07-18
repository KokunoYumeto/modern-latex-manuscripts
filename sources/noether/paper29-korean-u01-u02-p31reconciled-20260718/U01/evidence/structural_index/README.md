# P29 Korean U01 structural index

`STRUCTURAL_INDEX.jsonl` is the canonical hierarchy-preserving index. `STRUCTURAL_INDEX.csv` is a flat projection for review and must never be treated as the authority when relations or hierarchy matter.

The index covers exactly the U01 work/root, title section, publication citation, author/presenter apparatus, four prose paragraphs, the displayed-in-prose finiteness criterion theorem, and four source footnotes. There is no display equation, proof, definition, lemma, proposition, corollary, example, diagram, table, or bibliography list in this bounded introduction. Inline symbols remain part of their parent prose/theorem records; they are not falsely promoted to display equations.

Coordinates are one-based and inclusive. A null character range selects the complete newline-joined line range. A non-null character range is permitted only within one line and is used here for exact balanced `\footnote{...}` spans. Fragment hashes are SHA-256 over the selected Unicode fragment encoded as UTF-8 with no terminal newline. Artifact hashes are SHA-256 over the file bytes.

`generate_structural_index.py` deterministically rebuilds the JSONL, CSV, and metadata from the current pinned German U01 and Korean target. It finds balanced footnote spans rather than assuming fixed character offsets. `validate_structural_index.py` applies the JSON Schema, recomputes artifact and fragment hashes, checks hierarchy/relations/order, checks metadata counts and source-boundary continuity, and checks every CSV field against the canonical JSONL.

The target remains `private_working` until an archive handoff changes that state through a later, logged regeneration. U01 continuation is exact full-P29 source line 25, `\subsection*{§ 1. Das Endlichkeitskriterium}`; the sealed German head must be rehashed before U02.
