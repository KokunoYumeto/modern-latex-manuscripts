# P29 Korean U02 structural index

`STRUCTURAL_INDEX.jsonl` is the canonical U02 hierarchy. `STRUCTURAL_INDEX.csv` is only a flat projection. U01 artifacts and chains are not read as mutable inputs and are never rewritten by these scripts.

Coverage includes the semantic §1 heading, the two-formulation Rationalbasis theorem, its first source note, the equivalence paragraph, the complete proof with its `t=n` and `t<n` steps, all three Korean display blocks, the second source note, and the corollary. The first display contains the paired definitions of the two overlined fields; the other two display the coefficient-extension chain and the final `K=M` relation. Inline formulae not promoted to displayed layout remain within their prose/proof parent.

Coordinates are one-based and inclusive. Null character ranges select complete newline-joined line ranges. Non-null ranges identify balanced `\footnote{...}` commands or exact source substrings corresponding to target display blocks. Fragment hashes use UTF-8 without a terminal newline; artifact hashes use exact file bytes.

The generator verifies that U02 is exactly normalized full-P29 lines 25–39 and that line 41—not blank separator line 40—is the next substantive cursor. The validator applies JSON Schema, recomputes all hashes and locators, checks hierarchy/order/relations, checks the exact CSV projection and metadata, verifies the sealed P31 authority hash, and rechecks the line-41 cursor.
