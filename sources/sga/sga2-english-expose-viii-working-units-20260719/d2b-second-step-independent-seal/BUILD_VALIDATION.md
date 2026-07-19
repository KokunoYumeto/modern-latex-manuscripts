# Build validation

The bounded target builds with two stabilized `pdflatex` passes, zero errors,
and no LaTeX warning, overfull-box, underfull-box, undefined-control, or
missing-character diagnostics. The result is one A4 page, 272,771 bytes.

- TeX SHA-256: `4F339AD2E60C1620EB7F773B30025A1F2BA676EC80F8D46EB6FC03B7E64D44EE`
- PDF SHA-256: `78E0B96D6A1EC4D1CC778155370BF8D6A4A2FB048F25D017F9CF5072023AAAC9`
- pass-1 local log SHA-256: `880FA5A0C825E107425D3EA0DF9951BCF09CFA95EC94F58D05EC76BBDCEF33E8`
- pass-2 local log SHA-256: `880FA5A0C825E107425D3EA0DF9951BCF09CFA95EC94F58D05EC76BBDCEF33E8`
- pass-1 sanitized log SHA-256: `152B32F484C1D0456BB037A843EF0C1153215ED259EC076E9156373AB177C74B`
- pass-2 sanitized log SHA-256: `152B32F484C1D0456BB037A843EF0C1153215ED259EC076E9156373AB177C74B`
- PDF metadata report SHA-256: `4F00D0B4263C9B2654FF8980A292AF69DE02FEB7B00FC5DE4FB725D38A926165`
- font report SHA-256: `641577765FB606FE11B4D63FA1019EC047764C8696246CDFA5EA242EBBF206FB`
- extracted target text SHA-256: `0C127459BB45CDD2453B39C1BCE42D291CF38390CB1454CB203C98D6C6849ECA`

The first rendered draft exposed an unwanted space in the source-note compound
`finite-projective-dimension`; keeping the compound on one TeX source line
fixed the visible typography. A later searchable-text gate found two U+0001
bytes emitted by `pdftotext` after sized parentheses in the nested Ext
displays. Replacing only `\bigl`/`\bigr` with ordinary parentheses removed
those bytes. The formulas and French authority are unchanged. Final extracted
text has zero forbidden non-layout control bytes and one ordinary form-feed
page delimiter. All 17 fonts are embedded, subset, and Unicode mapped.

The raw local logs name a user-specific TeX installation and are excluded from
the public set. The sanitized logs have zero contiguous or whitespace-elided
private-path hits and zero real build diagnostics.

A fresh isolated two-pass build also exits zero. Its 272,771-byte PDF has
SHA-256 `0352A5749D260E7FDB038D6B95EEAF19B807710BDD78343B45B6F764916D75E7`.
The independent and target extracted text are byte-identical, as are their
300-dpi rendered pages. The PDF hash difference is confined to creation and
modification timestamps and the derived trailer identifier. Independent
pass-1 and pass-2 TeX-log SHA-256 values are
`1BCDC6BC693992B59F34AC8F5200B64FDB86377CE5B82EDC66E86E3E4EAEBFE3`
and `D2C950582F122EADC733E5AC7DE5D1C0B40FB959E0AAFD3139DBA5021F8993F7`.
