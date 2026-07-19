# Independent build validation

## Transport and package replay

- Received ZIP: 158,527,445 bytes, SHA-256
  B5162EAD48F3A2B1A3C74D53D7A888E9AAB6AE1E92DD243AB73B56CF32AE4AF8.
- ZIP entries: 140; decompressed files: 119; decompressed bytes:
  178,221,139; unsafe paths: 0.
- Producer manifest: 116 rows, 16,615 bytes, SHA-256
  DDBF5D2AB605C235D2215D3D061BCBBCA2945F9C9FDA2F2D9333D718BC589C89;
  missing, byte-mismatch, and hash-mismatch errors: 0.
- Nested Web Paper 4 ZIP: 47 entries, 31,397,588 decompressed bytes,
  SHA-256
  8ACB934E9E793AC16542765FE9C6806FF90B4DF0CD84EE86E73E43D57DB8A7DC;
  unsafe paths: 0. It was unpacked and read before classification.

## Current reader

- TeX: 2,153,006 bytes, SHA-256
  4B4A8DDBE3809548BE2882E489861A9BE18F8029724318A17210F66FECE9294C.
- Producer PDF: 2,652,677 bytes, 466 A4 pages, SHA-256
  572CF1EAA7F4895D0DA3644AE872D228AE40F6BCD81EC87DC3DEE1ADC9183C92.
- Independent XeLaTeX passes: exit 0/0; selected fatal, undefined-control,
  rerun, box, and missing-character diagnostics: 0.
- Independent rebuild PDF: 2,652,674 bytes, 466 A4 pages, SHA-256
  B0CA9C33E2011F2FD1CF02040BDEE788AB7EE9F1734929B2C1E879B188DC77D7.
- Producer/rebuild extracted text: byte-identical, 2,263,990 bytes, SHA-256
  E6DC206B565AC7B68B2AE75905BC425869A713E00594521CF07BDB04FFE87608.

The PDF is unencrypted, A4, untagged, and has no JavaScript or forms. All 47
font rows are embedded and subsetted. Seven specialist mathematical font rows
lack Unicode maps; extraction is useful but is not an accessibility claim.
There is no XMP packet.

## Render validation

The 16 changed output pages are 5-10, 49-55, and 57-59. Each page was freshly
rendered from both the producer PDF and the independent rebuild at 400 dpi.
All 16 producer/rebuild render pairs are byte-identical. The corresponding
producer-supplied final renders use a different renderer or antialiasing
signature, but have matching dimensions and passed original-detail visual
inspection. RENDER_REPLAY_VALIDATION.csv carries the exact hashes.

The 16-page contact sheet passed visual review. No clipping, collision,
missing glyph, broken display, overflow, blank page, or incoherent page
boundary was found.

## Public-boundary validation

The public projection excludes source PDFs, source pages and strips, mixed
source/target composites, nested archives, raw logs, auxiliaries, absolute
host paths, and task/thread identifiers. Rights-sensitive source evidence is
represented by hashes, page loci, dimensions, density basis, rotation, crop
coordinate status, structural scope, and QA disposition.
