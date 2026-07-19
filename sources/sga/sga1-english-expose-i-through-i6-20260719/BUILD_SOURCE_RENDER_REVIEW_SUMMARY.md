# Build, source, render, and review summary

## Source and target

- French arXiv authority main TeX SHA-256:
  `754E9FD6BC04BA52359D0CF4102AA01D2805A00B0E3E298CCD7396564CC7702D`.
- Section I.6 lines: 1168--1216 inclusive.
- Section I.6 source slice: 1,983 bytes; SHA-256
  `7F9831D26582DB33861D2C9D48F6DD09C6956F639C566A92FAFA0514F08DDFCD`.
- Cumulative TeX: 18,388 bytes; SHA-256
  `0D19B0F3FB15766C94B8369BCB27BB671C3717401E74AA86293FA50275A9ADC7`.
- Section I.5 fragment: 8,801 bytes; SHA-256
  `D0959C14AEC3D333EDE96AFFBC6FA8320A223B0A5F2B482B7DCE0268868E8FF9`.
- Section I.6 fragment: 2,168 bytes; SHA-256
  `101CD6F1FC9C46E754E3AD31903863FCA2418DCF31A2E91D47637DF4815291EF`.
- PDF: 10 A4 pages, 464,688 bytes; SHA-256
  `1C3D5539209B2A0D8C9EEA34332C372EED385BFBB9D3D098152545670AC34FC4`.

## Review

Seven source-comparison rows and seven formula/structure rows cover the full
unit. The theorem and corollary hierarchy, reduction functor, categorical
direction, Hom-map variance, quotient reduction, unheaded proof continuations,
and lifted-polynomial construction were checked. No source-original defect or
unresolved source ambiguity was found. Two independent automated read-only
reviews returned PASS; this is not human scholarly peer review or mathematical
certification.

## Build and render

The three final local console transcripts are byte-identical at SHA-256
`6839CE002C7F6ECCFF037C24CCA226F3BD31E4A8647393DBE0CE52B15F237576`.
The three final local full logs are byte-identical at SHA-256
`41BC71DDFF496C248CE5EEC980462019DC1A927A7ECC2CFDDD1C68C0B08F1922`.
These six raw local objects are excluded because they expose compiler paths.
The public payload instead contains three concise synthetic receipts and three
path-scrubbed full logs. All final logs have zero warning, error, box,
undefined-reference, rerun, or fatal matches.

All ten PDF pages were freshly rendered at 180 dpi, inspected together, and
re-rendered independently with 10/10 byte-identical page images. No layout or
glyph defect was found. The freeze builder also performs three clean staging
dependency builds using both included TeX fragments before creating manifests.
