# EGA IV Sections 16-21 live source custody

At `2026-07-31T02:08+02:00`, archive maintenance copied the current editable
source state from both active EGA IV Part 4 lanes into one compact GitHub-only
survival snapshot:

`sources/ega/ega4-sections16-21-live-source-custody-20260731T0208`

The package has 22 files / 1,300,270 bytes. Its 21-row self-excluding
`SHA256SUMS.csv` is 2,538 bytes with SHA-256
`2ECFD77B747DC1E786F73D3997B435B3C0B6CA88E1C083E20BEE8F94DF66AAE0`
and replays exactly.

The copied Sections 16-18 source includes `ega4-16.tex`, 177,054 bytes,
SHA-256
`FC4DFDC9A88A97B1920662496D61A43D6B95413CAF0AC9B2DFD1C83403009883`.
The copied Sections 19-21 source includes `ega4-19.tex`, 169,911 bytes,
SHA-256
`BA36FA26C55DCE8F969F8C5E7DD9848E1ECC8A988EBC2CD6DF64EE5ECF6DDF8B`.
Both producer lanes remained active, and their copied source can be newer than
the latest formally recorded cursor in their status files. These bytes are
therefore preserved without promoting an inferred alignment or review claim.

Each copied harness completed one isolated XeLaTeX pass with zero hard TeX
markers. The Sections 16-18 harness produced 120 pages; the Sections 19-21
harness produced 100 pages. The transient PDFs and logs were deleted after
validation and are not duplicated in the package.

Private paths, task identifiers, credentials, authority files, authority
pixels, OCR bodies, reader PDFs, build logs, and auxiliaries are excluded.
Privacy hits are zero. This is public GitHub source-survival custody only, not
a completed EGA IV reader, source-alignment certification, rights clearance,
or Zenodo mutation. Existing cumulative EGA readers remain current until a
producer-sealed successor is ready.

