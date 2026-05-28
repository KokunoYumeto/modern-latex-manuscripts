# Deligne Packet Style Reference for the SGA Translation Project

The uploaded `Deligne.zip` was treated as a style reference, not as a source to be merged into SGA. The completed examples in the packet use a direct mathematical English style: short titles in modern English, standard theorem/proposition/definition environments, and minimal editorial intrusion. I will follow that model for SGA unless there is a reason to preserve SGA's historical wording.

Operational choices adopted from the reference packet and from batch 001:

1. Preserve mathematical structure and numbering. Original section, proposition, definition, lemma, corollary, and example numbers remain visible.
2. Translate in contemporary mathematical English while retaining historically important SGA terms. In particular, `limite projective` remains `projective limit`, and `limite inductive` remains `inductive limit`; the modern readings `limit` and `colimit` are implicit.
3. Prefer standard current terminology in algebraic geometry and category theory: `presheaf`, `sieve`, `fiber product`, `base change`, `representable`, `fully faithful`, `left exact`, `right exact`, `filtered`, `cofiltered`, `adjoint`.
4. Do not recast proofs. Improve readability only at the sentence level; do not silently strengthen, weaken, or modernize the mathematics.
5. Use coherent, compileable LaTeX as the working artifact. Each translation chunk should include a rendered PDF and render-check images.
6. Place a continuation anchor at the end of each chunk so the next batch can continue without searching.

Notes from this batch:

- The Deligne examples favor uncluttered article-style documents and concise preambles. Batch 002 follows that practice.
- The Deligne packet contains both completed PDFs and working draft TeX. For SGA, every new deliverable should include both source `.tex` and rendered `.pdf` in the top-level batch ZIP.
