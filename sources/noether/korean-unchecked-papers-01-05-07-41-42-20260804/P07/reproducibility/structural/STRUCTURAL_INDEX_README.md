# Structural index contract

STRUCTURAL_INDEX.jsonl is the hierarchy-preserving authority. STRUCTURAL_INDEX.csv is a flat projection for inspection and does not replace the JSONL.

Each record has a stable structural ID, work and unit IDs, structure kind, exact source and target line locators, authority and target identities, LF-normalized slice hashes, parent/order relations, cross-references, language, production/review/publication state, and continuation cursor.

Slice hashing rule: normalize CRLF or CR to LF, select the inclusive one-based line range, join the lines with LF, and include one terminal LF. Source whole line equals 5841 plus source local line. Overlapping structures such as a note embedded in a paragraph intentionally share line-level locators and hashes but have distinct stable IDs and parent relations.

The builder verifies the exact authority file hash, Paper 7 interval hash, and all eight frozen target hashes before writing the projections. The validator independently recomputes all source and target slice hashes, target file hashes, relationship integrity, order, state controls, kind coverage, and CSV shape. Neither operation is a linguistic, formula, source, or scan review.
