# EGA IV Sections 16-21 live source custody snapshot

This directory preserves a coherent, privacy-clean snapshot from the two
active EGA IV Part 4 source-alignment lanes. It advances the earlier
`20260731T0208` GitHub custody snapshot without changing any public EGA reader
or Zenodo record.

## Captured source state

### Sections 16-18 lane

The copied source is the exact closure used by producer checkpoint
`checkpoint_printed070_r21`:

- source alignment through printed page 70;
- `ega4-16.tex`: 177,024 bytes, SHA-256
  `117AA3D848923C3FF849713BA124C5E106FA9A89EBF5557FA6055ACDC7631E2F`;
- `ega4-17.tex`: 159,772 bytes, SHA-256
  `7FAACDCDD8EAF10BDB0034D8F042A7DEE8FF94C103C84497FAF47BBF03884453`;
- `ega4-18.tex`: 316,925 bytes, SHA-256
  `9874F3A55EA9A857AB91F5F339643F1C8A0FC1056C649533C274989818E46713`;
- bounded checkpoint PDF: 122 pages / 834,359 bytes, SHA-256
  `CD9FE68D1DD28F092DAE15AD90DEBDB68396626A34C9316DBAAA6E7D84DD6A68`.

Authority images for later pages were being prepared when this snapshot was
taken. They do not establish additional aligned-text coverage here.

### Sections 19-21 lane

The copied source is the exact closure used by producer checkpoint
`build_p185_210_r9`:

- source alignment from printed page 185 through printed page 210;
- `ega4-19.tex`: 175,032 bytes, SHA-256
  `E253A01041EDF61B6CB6DF7C73AFE6B0FDAD2905E3D2A04416AD987151496E50`;
- `ega4-20.tex`: 108,984 bytes, SHA-256
  `18AB10403EC13A0AF82F8548B35A90F70CC2999CAA9838828875EAF0D7004565`;
- `ega4-21.tex`: 311,137 bytes, SHA-256
  `F1D80A58C2743578FEBFA9C8BE7B9C19E52186AE8FF5914C26536A7BF9D76D4D`;
- bounded checkpoint PDF: 101 pages / 698,596 bytes, SHA-256
  `BBE9DAC3C7DB977E622BB7F6CA17C8744EC5E36091E1A6D17F60CE05423A511A`.

## Build and quality scope

Both producer checkpoints were built in three XeLaTeX passes. Their final
logs contain zero TeX errors, undefined control sequences, fatal stops,
missing-character events, or duplicate-destination diagnostics. The two PDFs
contain mathematical reader content only and have no project, model, task, or
review-status preface.

The PDFs include the inherited remainder of their bounded section ranges.
Only the page ranges stated above are newly source-aligned by these active
lanes. They are not complete EGA IV, cumulative EGA I-IV readers, exhaustive
reference-v2 releases, critical editions, or accessibility certifications.

## Authority and exclusions

The controlling authority is the 360-page NUMDAM EGA IV Part 4 PDF, SHA-256
`B4277FB99C6EDF8FEEC5B01F54368E4B8521BCD52871316C0EDF6FF4AE69389E`.
It, all authority pixels, OCR bodies, private logs, scripts, caches, and raw
build intermediates are excluded.

No blanket license grant or rights-clearance decision is asserted. Rights
remain with their respective holders. This is GitHub source survival and a
bounded build snapshot only; Zenodo remains unchanged.

