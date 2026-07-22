# Build and QA record

Date: 2026-07-22

## Source pin

- Repository: <https://github.com/jcreinhold/sga>
- Commit: `e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e`
- Source class: Jacob Reinhold's LLM-generated English translation lineage
- Translation-contribution license: CC BY 4.0
- French authority status: comparison/convenience source only, never authority

The generated readers concatenate the SGA 1 and SGA 2 Markdown in the pinned
upstream order. The exact tracked upstream repository snapshot is included as
`provenance/reinhold-sga-e7a259f-source.zip`. Its 111 file entries replayed
byte-for-byte against the pinned checkout, with zero absolute or traversal
entry names.

## Presentation build

- Pandoc 3.9.0.2
- MiKTeX-XeTeX 4.18 (MiKTeX 26.5)
- A4 page size
- Cambria text and Cambria Math
- Plain page-number footers to prevent long running heads from colliding

The first page of each reader is an attribution and claim-limit notice. Narrow
renderer-safety changes were made only in the generated presentation layer:
Unicode glyph fallbacks, raw-TeX escaping, and diagram layout. One overwide
SGA 1 commutative diagram was reformatted, and one SGA 2 ASCII diagram was
kept together across a page boundary. These are not claims of semantic or
mathematical editorial review.

## Final build results

| Check | SGA 1 | SGA 2 |
| --- | ---: | ---: |
| Pages | 286 | 200 |
| Final-pass TeX errors | 0 | 0 |
| Final-pass LaTeX warnings | 0 | 0 |
| Missing-glyph diagnostics | 0 | 0 |
| Label-change diagnostics | 0 | 0 |
| Overfull boxes | 60 | 3 |
| Maximum overfull width | 1.21689 pt | 3.55179 pt |
| Underfull boxes | 15 | 8 |

All SGA 1 overfull reports are small table-of-contents lines. Neither reader
has an overfull box greater than 5 pt in the final pass.

## PDF inspection

| Check | SGA 1 | SGA 2 |
| --- | ---: | ---: |
| A4 MediaBox | pass | pass |
| Encrypted | no | no |
| AcroForm | absent | absent |
| JavaScript | absent | absent |
| Embedded files | absent | absent |
| Fonts embedded/subset/Unicode | 5/5 | 4/4 |
| Tagged PDF | no | no |
| XMP metadata | absent | absent |

The PDF open action is a normal destination array, not executable content.

## Text and privacy

Poppler 24.04.0 extracted all 286 SGA 1 pages and all 200 SGA 2 pages. The
reader notices, Jacob Reinhold attribution, exact source commit, and CC BY 4.0
license statement are present. Searches for private Windows home paths, agent
work directories, build-workspace paths, and application-data paths returned
zero hits in the extracted PDF text and public text files.

## Visual review

Representative pages were rendered with MuPDF 1.23.0 and assembled with
ImageMagick 7.1.2-22. The review includes both title/notice pages, mathematical
body pages, indexes, and the post-repair SGA 2 diagram page. The reviewed
images are in `qa/`; no clipping, overlap, missing glyph, or divided diagram
remains in those pages.

This QA establishes that the convenience readers build and render coherently.
It does not establish French-source fidelity or mathematical correctness.
