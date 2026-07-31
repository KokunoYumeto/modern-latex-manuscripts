# Serre GAGA first-pass transcription custody snapshot

This directory preserves the complete first-pass TeX transcription of
Jean-Pierre Serre's 1956 paper *Geometrie algebrique et geometrie analytique*
(GAGA), printed pages 1-42. It is a GitHub source-survival checkpoint, not a
clean public reader, critical edition, mathematical certification, or rights
clearance.

## Preserved mathematical work

- `gaga_body.tex`: the complete 42-page transcribed body, 125,800 bytes,
  SHA-256
  `AD4AE8CAC24D353D4018E331ED6BF64721CB40C0BD3ACA146230BBE190D34DCF`.
- `gaga.tex`: the compilable wrapper, 3,085 bytes, SHA-256
  `285ADFBF0B17912416C4616D5FA4CF33BC3A8FF5EE3D36264DF9CD37B1143566`.
- `SOURCE_NOTES.md`: 21 recorded source defects and 82 uncertain readings,
  26,026 bytes, SHA-256
  `0BC22F8420220305608926563138DF6EBCC17CC64F3770EAB74FDAD31794D990`.

The source wrapper builds successfully. The source image controls every
reading; its OCR/text layer is only a locator or drafting witness. Printed
defects are preserved and recorded rather than silently normalized.

## Authority and exclusions

The controlling local authority copy is the 43-page NUMDAM scan, 4,134,102
bytes, SHA-256
`9898F985DD6932496E26450BFE0BECA8655A937032F545B97CEBD88D1BC8EB98`.
The scan, source pixels, extracted OCR, caches, scripts, and raw build files are
not included here.

No blanket license grant is asserted for the underlying paper, the
transcription, or this package. Rights remain with their respective holders.

## Reader defect held open

The first working build was 24 pages / 355,145 bytes, SHA-256
`A8E4684376D3977020CB95B5C18E75753344B1DB4BB54AC9245CED7E9B133839`.
It is deliberately excluded because 32 literal page-join sentinel tokens
(`CONT>>` and `<<CONT`), forming 16 joins, remain in the TeX and are visibly
typeset in that PDF. A later
no-overwrite successor must remove those workflow delimiters and inspect the
affected joins before a reader is fronted.

This snapshot preserves the underlying mathematical transcription while that
reader repair remains open.
