# Independent source-archive rebuild

Status: `PASS`

The public source archive was extracted into a fresh isolated directory and
rebuilt without access to the producer build tree.

## Archive replay

- source archive members: 989
- self-excluding source manifest rows: 988
- uncompressed member bytes: 16,610,078
- CRC failures: 0
- unsafe or duplicate paths: 0
- missing or extra members: 0

## Rebuild

- engine: XeLaTeX
- passes: 3
- exit failures: 0
- hard TeX errors: 0
- undefined references: 0
- duplicate destinations: 0
- missing glyphs: 0
- overfull boxes: 0

The isolated rebuild produced a 1,008-page PDF. Its file-level identity differs
from the released reader only in nondeterministic PDF metadata:

- isolated PDF bytes: 6,014,753
- isolated PDF SHA-256:
  `333DC9487BAC1A4B5640519990D01BA6525E0029B5C83D589E842B0C7609FEB2`
- page content streams equal: 1,008/1,008
- extracted page text equal: 1,008/1,008
- page geometry equal: 1,008/1,008
- named destination sets equal: 6,304/6,304
- internal GoTo sequences equal: 3,849/3,849
- sampled seam and raster-witness renders equal: 17/17

This receipt validates rebuildability and semantic/render equivalence. It does
not expand the reader's stated scope, rights, diagram, or certification claims.
