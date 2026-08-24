# D026 maintained source package

This directory contains the independently maintained, editable editions of
Pierre Deligne's *Les constantes locales de l'équation fonctionnelle de la
fonction L d'Artin d'une représentation orthogonale*.

- `Deligne_D026_FR.tex` is the corrected French source-language edition.
- `Deligne_D026_EN.tex` is the independently checked standalone English edition.
- `Deligne_D026_APPARATUS.tex` is the restrained textual and translation apparatus.
- `ASSET_LEDGER.tsv` is deliberately empty: every diagram is represented by
  editable mathematical markup, so no authority-page raster was promoted.

The controlling authority is the 18-page IAS scan, SHA-256
`9951F00E4E8E2673ABBAFB44D28B03FA31A45E60EF03BCFE6DA0A5E102167FC6`.
Authority PDF pages 1--18 map one-to-one to printed folios 299--316 and to the
18 pages of each maintained edition. Running heads, original folios, journal
masthead, copyright line, scanner margins, and terminal blank remainder were
excluded from body transcription. The edition's own unobtrusive headers and
folio labels are navigational matter, not transcribed source text.

Returned HTML and the inherited prior-work archive remain byte-preserved in the
local maintenance evidence and are not used as canonical readers. They are not
carried in this public-ready source ZIP because inherited ledgers contain local
profile paths. `maintenance_evidence/ZERO_ACCEPTED_PRESERVATION_RECEIPT.json`
records their exact identities, and
`maintenance_evidence/SANITIZED_ZERO_ACCEPTED_PRIOR_WORK_LEDGER.tsv` preserves
all 64 dispositions without private paths. Every inherited member remains
`ZERO_ACCEPTED`; no inherited reading is promoted merely because it agrees.

Build with LuaLaTeX. The build script validates all three page-record layers
against the controlling authority identity before writing TeX.
