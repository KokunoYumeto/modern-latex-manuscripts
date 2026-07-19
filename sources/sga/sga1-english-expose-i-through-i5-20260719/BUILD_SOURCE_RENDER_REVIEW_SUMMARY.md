# Build, source, render, and review summary

## Source and target

- French arXiv authority main TeX SHA-256: `754E9FD6BC04BA52359D0CF4102AA01D2805A00B0E3E298CCD7396564CC7702D`.
- Section I.5 lines: 952-1167 inclusive.
- Section I.5 source slice: 8,131 bytes; SHA-256 `4E0A4AA4FBB2C5F74E83C626A1DCCF0D20456E28922F65F08E5AD7016824F285`.
- Projected cumulative TeX: 18,290 bytes; SHA-256 `2080CE09178D54869A227617B81E104F64145BF7169BAABA16B82A3945C78760`.
- Byte-identical section I.5 fragment: 8,801 bytes; SHA-256 `D0959C14AEC3D333EDE96AFFBC6FA8320A223B0A5F2B482B7DCE0268868E8FF9`.
- Projected PDF: 9 A4 pages, 447,024 bytes; SHA-256 `182F111492114FA3818C828FD8182688E64144DC31ACD86C9815FD923634A215`.

## Review

Thirteen source-comparison rows and thirteen formula/structure rows cover the
complete bounded section. Formula variance, completion notation, page markers,
the theorem hierarchy, the four-arrow square, notes, terminology, and source
defects were reviewed. Corollary I.5.3 is openly corrected to include the
missing etale hypothesis; the target footnote gives the source reading and a
counterexample.

## Build and render

The audience-neutral projection was built in three isolated passes. Passes 2
and 3 are byte-stable and all passes have zero warning, error, box,
undefined-control, rerun, or fatal matches. Each pass has a concise public
receipt and path-scrubbed full compiler log. All nine pages were freshly
rendered at 180 dpi and decoded; pages 3-9 are pixel-identical to the frozen r6
renders. Pages 1-2 differ only in public-status wording. No mathematical body,
formula, theorem, proof, or continuation cursor changed.
