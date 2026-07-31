# SGA 7 II French source transcription, working Exposes X-XVII

This package preserves a readable cumulative transcription of SGA 7 II
Exposes X-XVII without altering the live production workspace.

## Reader

`reader/SGA7II_French_Source_Transcription_Working_X-XVII_20260731.pdf`
contains continuous source-page coverage from source-PDF index 8 through index
260, corresponding to book folios 1-253:

- Expose X: indices 8-45;
- Expose XI: indices 46-68;
- Expose XII: indices 69-89;
- Expose XIII: indices 90-122;
- Expose XIV: indices 123-171;
- Expose XV: indices 172-203;
- Expose XVI: indices 204-218;
- Expose XVII: indices 219-260.

The cumulative reader is 130 A4 pages. It contains the mathematical
transcription only: no archive status page, production preface, worker note,
or process commentary is inserted into the PDF. Expose XVIII and later are
excluded.

## Editable source

The complete buildable source closure is under `source/`: one master and eight
Expose body files. The source was built with pdfLaTeX using a fixed source-date
epoch. The final two passes produced the same PDF bytes.

`work-in-progress/expose_XVIII_partial.tex` preserves useful later work but is
not included in the reader. Its gaps and boundary are stated in the adjacent
WIP README.

## Recovered pages

The earlier working tree omitted scan indices 197 and 211 and contained a
non-source refusal placeholder at index 198. Index 212 existed only in a
preserved transcription result. This successor transcribes all four pages and
checks them directly against the source images. The repaired source pages are
book folios 190, 191, 204, and 205.

The actual 600-dpi source-page renders and six labeled detail crops are under
`visual-evidence/`. They are public evidence objects, not manifest-only
stand-ins. `VISUAL_EVIDENCE_INDEX.csv` records the parent PDF identity, page,
folio, dimensions, crop box, and SHA-256 for every image.

## Source basis and claim boundary

The controlling source is the publicly available 446-page Institute for
Advanced Study scan locally identified as `Number12.pdf`, 12,587,545 bytes,
SHA-256
`FA679DEBFC8ADA3232D7E752A1837FC6CE474488E20A44D7641CF296876E1297`.
Its OCR layer was a locator and drafting witness; source images controlled the
recovered-page readings.

This is a working source transcription and continuity checkpoint, not a
critical edition, complete SGA 7 II volume, mathematical certification, or
accessibility-remediated PDF.
