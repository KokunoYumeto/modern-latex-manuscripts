# Independent public-source rebuild

Result: **PASS**

The archive-maintenance process independently verified and extracted the
public source ZIP, then rebuilt the reader from only those extracted public
files.

## Package replay

- Outer SHA manifest: 9/9 rows exact before this receipt was added.
- Source ZIP: 867 unique, safe members; CRC failures 0.
- Internal manifest: 866/866 rows exact.
- Embedded validation: PASS, errors `[]`.
- Missing, extra, duplicate, traversal, absolute-path, byte, or SHA-256
  mismatches: 0.

## Independent build

- XeLaTeX passes: 4/4 exit 0.
- Rebuilt PDF: 1,434 pages / 8,650,333 bytes.
- Rebuilt PDF SHA-256:
  `620151CB15E995E332DDC359147CBED0C0092D6DBEF0873C39ABFC65D69DA1A7`.
- Public candidate PDF: 1,434 pages / 8,650,355 bytes.
- Candidate SHA-256:
  `481EEDECAA8635AEAC5CCA91492797AF651D426A80B6A2F2510BDF05EB3DD36D`.

The expected byte difference is confined to regenerated creation metadata
and font-subset prefixes. The following publication-relevant surfaces are
exact between candidate and rebuild:

- extracted text: 1,434/1,434 pages;
- decoded content streams: 1,434/1,434 pages;
- media/crop geometry and rotation: 1,434/1,434 pages;
- named destination names: 9,246/9,246;
- internal link actions and rectangles: 4,541/4,541;
- normalized font occurrences: 23,253/23,253;
- raster image objects and decoded pixels: 142/142.

Decoded page-stream aggregate on both PDFs:
`91E9F161C7F7C3CD3B1EE3908CAA549EC6A329763370DEF1A021C6ED1D168471`.

Extracted-text aggregate on both PDFs:
`94CC953F122E90324DBB4D5745A3832144729456D2A5C03B434C6C1F54922467`.

Decoded image-object aggregate on both PDFs:
`774286F0C86AE3AF86D7AA8231845C0F393E54D2AC8B847C2E20AFD88EF0542F`.

This receipt validates source-archive completeness and reproducibility. It
does not convert the disclosed Loop-1 raster diagrams into final
diagram-fidelity certification.
