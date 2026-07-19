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

## Final local artifacts

- Section I.5 fragment: 8,801 bytes; SHA-256 `D0959C14AEC3D333EDE96AFFBC6FA8320A223B0A5F2B482B7DCE0268868E8FF9`.
- Cumulative TeX: 18,273 bytes; SHA-256 `D9B747DC9CEF1753D7F55B0F2F2AF400307AB5C73A3B82DE1552D2FFCF3D432E`.
- Cumulative PDF: 9 A4 pages, 446,807 bytes; SHA-256 `20B3421F69B041DD6C9CC2953C2EA79958DE73CF884DB9B17474399B41012F0B`.
- Three private local console transcripts are byte-identical at 9,015 bytes and SHA-256 `B2F8073F473E74C107626F36DC78EB0E733E2BAC2EA2E80E73E36ED7E64A342E`; they are excluded from public payloads.
- Three private local full compiler logs are byte-identical at 28,031 bytes and SHA-256 `FD13AEA37133369E7D74ECD6C066BE2C3FD3B0244100EC05142D63EC4C3FFD22`; only path-scrubbed derivatives may be public.
- Warning, error, undefined-reference, rerun, overfull, underfull, and fatal diagnostic matches: zero on every final pass.
- All nine pages were freshly rendered at 180 dpi and inspected; no clipping, overlap, malformed formula, missing glyph, or page-structure defect was found.
- PDF metadata is populated; the PDF is A4, unencrypted, and contains no JavaScript.

## Machine-readable gate

- Source comparison: 13 rows; SHA-256 `29AEDE9C405B64C0F64F70E2C1FE7B6A0420A4A7BB37D525E4B347992C1CDDC9`.
- Formula and structure comparison: 13 rows; SHA-256 `45357CC4A8C072FB6F51B935F51CFA8A22FB643715B29C515BA6BE792024BD64`.
- Section I.5 evidence graph: 13 records; SHA-256 `78BFE6AB02BC461741B02004651FBF45FC94F93D734B08990586DCFC26BD8124`.
- Local append-only difficulty/failure/revision ledger: 42 total records, including the rejected r1-r5 freeze attempts; SHA-256 `C79C24C3B2BDF950C0180A0A70FFDBBE8C680238E4465EB393D6A7675BD54B62`. This working-history ledger is excluded from the public payload.
- Combined local machine validation: 189 CSV rows, 68 unique JSONL records, zero failures; receipt SHA-256 `D94802B4FBF470C88B998DE5E72BFE85312E60FDC60EEB25667C49F6FC511E42`. The public projection instead contains 14 CSV files with 252 rows and four JSONL files with 55 records; its package-local validation receipt is regenerated during freezing.

This closes the bounded local content/build/render/machine gate only. It does
not establish complete SGA 1 coverage, a critical edition, peer review,
mathematical certification, independent human review, or rights clearance.
