# Independent build validation

## Transport and package replay

- Received ZIP: 26,554,754 bytes, SHA-256
  `84035FB7041BE5E54155BB4E5133737F3DB81D5AA22294DF6118F0FCDCD326BF`.
- ZIP extraction: unsafe paths 0.
- Producer manifest: 108 rows, SHA-256
  `DC176B5B2A8EEC75E7201DD06DBC1775157BF88C0FED724AFD7C3472430D7920`;
  missing, byte-mismatch, and hash-mismatch errors 0.

## Current reader

- TeX: 2,153,560 bytes, SHA-256
  `6FCBF5DB4E4378032B7074442C181E3FCFE975275319E49B284CE3B868EE0D5D`.
- Producer PDF: 2,654,413 bytes, 466 A4 pages, SHA-256
  `505A4966299C7292EF272FD54754BF4E5F45B14C72AFA03B487512D4EFED4136`.
- Independent XeLaTeX passes: exit 0/0; pass-2 selected diagnostics 0.
- Independent PDF: 2,654,425 bytes, SHA-256
  `30402725B043E500990211A2FB7946050F3CAA54DE52846B22840FE1DC715F20`.
- Direct producer/rebuild extraction: byte-identical, 1,785,000 bytes,
  SHA-256
  `2097B08120070C59251E577244FD2AEA7AAE1C92D0A3A4CE36F9CCCAC201CA9F`.
- Layout producer/rebuild extraction: byte-identical, 2,260,113 bytes,
  SHA-256
  `929299952B02E882E4D4CFBA07A795E81CC692111BA3BFAD43AD05E4D0640FEA`.

The binary PDFs differ because generated metadata differs. The producer PDF is
unencrypted, A4, untagged, and has no XMP packet. All 48 font rows are embedded
and subsetted; seven specialist mathematical font rows lack Unicode maps.

## Render validation

Output pages 13-17 are the complete changed-page set. Fresh independent
180-dpi renders match the producer's same-renderer current images byte-for-byte
for all five pages. Both current and predecessor images were inspected at
original resolution. No clipping, overlap, missing glyph, blank content, or
incoherent page boundary was found.

The producer also supplied a cross-renderer final set. It was visually clean
but is not the durable public image set because it cannot provide byte-level
replay against the independent renderer. Its identities remain in
`EXCLUDED_VISUAL_EVIDENCE.csv`.

## Public boundary

The public projection excludes the source PDF, all source-derived pixels, raw
path-bearing logs, private broad ledgers, archives, auxiliaries, absolute host
paths, and task identifiers. Rights-sensitive source evidence is represented
by hashes, page loci, dimensions, generation and embedded density, rotation,
crop-coordinate status, structural scope, and QA disposition.
