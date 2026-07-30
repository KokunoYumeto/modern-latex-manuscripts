# EGA IV Sections 16-18 working custody through printed page 18

At `2026-07-31T00:20:14+02:00`, archive maintenance captured the next closed
source-alignment gate from the active EGA IV Sections 16-18 lane. The source,
status, logbook, progress ledger, and build controls remained exact during two
complete package builds.

## Exact custody package

`sources/ega/ega4-sections16-18-source-aligned-through-printed18-working-custody-20260731`

- 13 files / 678,129 bytes;
- 12-row self-excluding `SHA256SUMS.csv`, SHA-256
  `FE0150ECCD68788E57874B02183B19E42F6D72D3FB2DE9CD672BD5507135CD50`;
- validation SHA-256
  `4153C4E591460CF29D28172A5CFF3B8C0ED29B1CB7C93325096BEA3C7D1E2DF6`,
  status `PASS_SOURCE_CUSTODY_ONLY`, errors `[]`;
- active `ega4-16.tex`, 176,685 bytes, SHA-256
  `88D983C556603FB3552BFCC2091EF5D4F270055A1B21A8D64EE39515E2F53E6C`;
- exact source-alignment progress CSV, 14 rows / 3,227 bytes, SHA-256
  `CBD9DE865D501EBA5C7EF869AA499D6ACBB9F411C9CDFC1E8A1C12A5EE1F90D2`.

Printed pages 5-18 / authority physical pages 4-17 are closed. The continuation
cursor is printed page 19 / physical page 18 / Proposition 16.4.5,
`ega4-16.tex` line 737. Pages 15-18 restore the Erratum IV item 11 locator,
correct the limit map from graded rings to augmented sheaves of rings, repair
the transitivity data from `u'',v'',f,f''` to `u'',w'',f,f''`, and preserve
direct diagram-by-diagram review.

The copied package builds in an isolated one-pass XeLaTeX replay to 120 pages
with exit code 0 and zero TeX error lines. The producer's clean three-pass r9
checkpoint is 121 pages / 827,157 bytes, SHA-256
`3C90B846762303B16A98447EE9B543970764175DE8D7B3D21335BECF8782CAE6`,
but remains excluded and unpromoted. Two complete package builds were
byte-identical, and privacy hits were zero.

This no-overwrite package supersedes the printed-page-14 package only as the
current active source-survival snapshot; earlier packages remain public
history. Authority PDFs, source pixels, raw logs, and reader PDFs remain
excluded. This is not a reader release, Sections 16-18 completion claim,
critical edition, rights clearance, accessibility review, or reference-v2
certification. No Zenodo mutation is requested.
