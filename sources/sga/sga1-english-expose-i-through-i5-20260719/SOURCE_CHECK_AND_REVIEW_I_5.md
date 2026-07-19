# Source check and review - SGA 1 Expose I section I.5

Date: 2026-07-18.

## Authority and boundary

- Authority archive SHA-256: `0A33C9C06908705A2525690FAAE02F6F07980A4AA069A8B6CFF9B1D9BC39ACD3`.
- French main TeX SHA-256: `754E9FD6BC04BA52359D0CF4102AA01D2805A00B0E3E298CCD7396564CC7702D`.
- Included section I.5 span: lines 952-1167 inclusive.
- LF-normalized source slice: 8,131 bytes; SHA-256 `4E0A4AA4FBB2C5F74E83C626A1DCCF0D20456E28922F65F08E5AD7016824F285`.
- Line 1168 begins section I.6 and is excluded.

The French TeX is the sole textual authority. External English files were used
only as target-language comparison controls. Original-print physical PDF pages
23-26, corresponding to printed Expose I pages 6-9, were used only for page,
diagram, formula, and source-original reading adjudication.

## Source, formula, and structure disposition

All 13 source-comparison rows and all 13 formula/structure rows passed the
bounded review. The target preserves Theorem I.5.1 with two proof branches,
Corollaries I.5.2-I.5.4, Theorem I.5.5, its Scholium, Corollary I.5.6,
Proposition I.5.7, and Corollaries I.5.8-I.5.9 in source order. The completion
formula, Hom variance, disjoint union, four-arrow square, fiber maps, forward
references, notes, and printed-page transitions were checked explicitly.

Corollary I.5.3 contains a shared source defect. The French TeX and original
print say that a connected-component projection is an isomorphism equivalently
when it is surjective and radicial, while citing I.5.1. The cited theorem also
requires etaleness. The uncorrected criterion is false for the nilpotent closed
immersion `Spec(k) -> Spec(k[epsilon]/epsilon^2)`. The English body therefore
uses `surjective, etale, and radicial` and immediately discloses the correction
and counterexample in a source-defect footnote.

The target also corrects the grammatical source form `type finis` to `of finite
type`, follows active corrected source branches in the first proof, preserves
the complete Scholium and commutative square, and rejects reversed Hom
arguments, corrupted completion glyphs, silent source-note deletion, and
unexplained use of the historical term `net`.

## Public projection artifacts

- Section I.5 fragment: 8,801 bytes; SHA-256 `D0959C14AEC3D333EDE96AFFBC6FA8320A223B0A5F2B482B7DCE0268868E8FF9`.
- Projected cumulative TeX: 18,290 bytes; SHA-256 `2080CE09178D54869A227617B81E104F64145BF7169BAABA16B82A3945C78760`.
- Projected cumulative PDF: 9 A4 pages, 447,024 bytes; SHA-256 `182F111492114FA3818C828FD8182688E64144DC31ACD86C9815FD923634A215`.
- Three projection builds completed; passes 2 and 3 are byte-stable and all selected diagnostics are zero.
- All nine projected pages were rendered at 180 dpi and decoded; pages 3-9 are pixel-identical to the frozen r6 renders.

## Machine-readable gate

The public projection retains 14 CSV files with 252 rows and four JSONL files
with 55 records. Stable IDs, hierarchy, revision state, source locators,
continuation cursor, and the section I.5 fragment hash are unchanged. Target
locators for the cumulative TeX/PDF are updated to the projected byte counts
and SHA-256 values. The package-local validation receipt is regenerated.

This closes the bounded content/build/render/machine gate only. It does not
establish complete SGA 1 coverage, a critical edition, peer review,
mathematical certification, independent human review, or rights clearance.
