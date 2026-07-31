# SGA 7 I English working reader through complete Expose VI

This current-progress reader contains complete English Exposes I and II and the
complete printed-English Expose VI, through Section 6.8 at source folio 132.
Expose VI has been checked against the printed source; Exposes I and II are
source-first English translations.

The exact continuation cursor is the opening of Expose VII at zero-based scan
index 144 / source folio 133. Exposes VII-IX are not included. This is not a
complete English SGA 7 I, critical edition, peer review, mathematical
certification, accessibility certification, or rights-clearance decision.

## Direct reading and source

- `reader/SGA7I_English_SourceFirst_Working_I_II_VI_Complete_20260731.pdf`
  is the 96-page A4 mathematical reader.
- `source/SGA7I_English_SourceFirst_Working_I_II_VI_Complete_20260731.tex`
  is the build wrapper.
- `source/components/` contains the exact 62 editable components used by the
  wrapper.
- `SGA7I_English_SourceFirst_Working_I_II_VI_Complete_Reader_and_TeX_20260731.zip`
  groups the reader, editable source, and package notices for one-click use.

The PDF starts directly with mathematical text. Workflow notes remain outside
the reader. A fresh isolated build completed with no TeX warnings, errors,
overfull boxes, underfull boxes, missing inputs, or rerun requests. All 96 page
geometries match the producer checkpoint. The only intentional textual delta
from that checkpoint is the source-reference correction recorded below.

## Source-reference correction

Direct review of source scan index 124, printed page 113, showed that the last
paragraph of Remark 4.16 refers to `4.12(b)`. The producer component said
`4.13(b)`. This frozen successor corrects that one reference to `4.12(b)` and
was rebuilt after the correction. No other mathematical text was changed by
archive maintenance.

The resulting PDF uses embedded fonts, but five EC bitmap resources are Type 3
and lack Unicode mappings. The PDF is not claimed to be tagged or
accessibility-remediated; the editable TeX is the durable text surface.
