# Build validation

The bounded target builds with two stabilized `pdflatex` passes, zero errors,
and no LaTeX warning, overfull-box, underfull-box, undefined-control, or
missing-character diagnostics. The result is one A4 page, 233,031 bytes.

- TeX SHA-256: `6C5BBC56388F226DFE46E39593AFD1E54BD099D76EDB4499EDB46E506F48CEA7`
- PDF SHA-256: `4AE4E00EFBF7BFBEA6AAB13DFD682514CCFD1347F2E234CBFE9EA17C51EB389D`
- pass-1 sanitized log SHA-256: `99DCD6C6B176F1070F8F719413B399228E4C5179D22C30465627AC988FBE4DF9`
- pass-2 sanitized log SHA-256: `99DCD6C6B176F1070F8F719413B399228E4C5179D22C30465627AC988FBE4DF9`
- PDF metadata report SHA-256: `7BF70D6A0EE751F5282D4A0FAF797E1FCA678391485A72F2410EEE79EBFEE168`
- font report SHA-256: `8E8B39DF4F238F5A00A74A0D7DD4A58AAFDBC3D194C516A12C466E3AEA8FC5D4`
- extracted target text SHA-256: `0C7D084E98F7D10117572FEE789B02FBB02A50241552C41CC3769E998B5E5BA6`

Independent review found one prose-only defect: the first target's sentence
about the quasi-coherent subsheaf repeated “coherent” through an ambiguous
`which`/`it` chain. The repaired target explicitly identifies the coherent
sheaf `F`; French and mathematical logic are unchanged.

Final extracted text has zero forbidden non-layout control bytes and one
ordinary form-feed page delimiter. All 14 fonts are embedded, subset, and
Unicode mapped. The raw local logs name a user-specific TeX installation and
are excluded from the public set. Both sanitized logs have zero real build
diagnostics and zero contiguous or whitespace-elided private-path hits.

A fresh isolated two-pass build also exits zero. Its 233,031-byte PDF has
SHA-256 `A468287796D57FCC575FD58F1D38627808947F2B937D40E4719D37C530C1013B`.
The independent and target extracted text are byte-identical, as are their
300-dpi rendered pages. The PDF hash difference is confined to creation and
modification timestamps and the derived trailer identifier. Independent
pass-1 and pass-2 stdout-log SHA-256 values are
`49C007BED44F276D9A264DCBA4B7FFE1627967F6BC743B03D10E080C36D9E839`
and `FCD50EB995CCC339B71F6DF631472F65798298BF90237B64EB25812A7B4810F7`;
the final independent TeX-log SHA-256 is
`9EAB7A1A54DC3E45D0A01C65DB165C4F1A5547DA57E02E911C5C5241F1E1F4C1`.
