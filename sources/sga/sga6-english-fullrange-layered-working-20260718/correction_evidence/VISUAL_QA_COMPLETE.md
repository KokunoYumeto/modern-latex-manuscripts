# SGA 6 Complete English Working Edition — Visual QA Complete

QA date: 18 July 2026  
Result: **PASS for PDF assembly, rendering, and visual integrity**  
Publication status: **working/review artifact only; not a publication payload**

## Frozen artifact checked

- PDF: `SGA6_English_Complete_Layered_WorkingEdition.pdf`
- SHA-256: `F8B1E15754BEB5C83CF2A47B261D6F9F907DE5B7E8A6ED4DF311C624E38C7B8E`
- Size: 2,565,870 bytes
- Extent: 381 PDF pages
- Geometry: all 381 pages are A4, 595.276 × 841.89 points, rotation 0

The production TeX and PDF were not edited during this QA pass. The PDF hash above was reconfirmed after all rendering and inspection work.

## Complete-page inspection

The frozen PDF was freshly rendered one page per process at 96 dpi to avoid the memory spike seen on the workstation. The result is 381 non-empty PNG files, each 794 × 1123 pixels, totalling 65,858,289 bytes.

Twenty contact sheets were generated in batches of no more than 20 pages and every sheet was opened and inspected: pages 1–20, 21–40, 41–60, 61–80, 81–100, 101–120, 121–140, 141–160, 161–180, 181–200, 201–220, 221–240, 241–260, 261–280, 281–300, 301–320, 321–340, 341–360, 361–380, and 381.

No clipping, overflow, overlap, missing or blank leaf, broken diagram, black missing-glyph box, corrupt raster, or unexplained discontinuity was found. Page 325's relatively large lower whitespace is a natural page break, not lost content.

The 381 fresh page PNGs and 20 contact sheets were also SHA-256-identical to the corresponding rasters made from the immediately preceding metadata-only PDF build. This corroborates that the final clean-auxiliary rebuild did not alter visible page content.

## Targeted 200-dpi inspection

Thirty-one gate pages were freshly rendered at 200 dpi, one page per process. All are 1654 × 2339 pixels. Each was opened at original resolution and inspected:

`1, 2, 8, 9, 80, 81, 82, 83, 84, 85, 152, 157, 191, 192, 205, 206, 207, 224, 225, 226, 272, 273, 349, 350, 375, 376, 377, 378, 379, 380, 381`.

Specific gate results:

- Pages 1–2: working-edition cover, authority warning, source title, and preface are clean and legible.
- Pages 8–9: the source-PDF 014 repair locus and its diagram/formulas render cleanly.
- Pages 80–85: the source-PDF 141–150 repaired block, diagrams, and footnotes render cleanly.
- Page 81: formula marker 14 is present after the arrow to `G`; footnote 14 is complete, unobscured, and reads: “We write S for the final object of the topos S, and Z_S for the constant sheaf with value Z.”
- Page 152: the source-PDF 277 repair locus is clean.
- Page 157: the source-PDF 286 footnote repair is present and unobstructed.
- Pages 191–192: the source-PDF 347 derivation and source-PDF 350 gamma/proof repairs are complete and aligned.
- Pages 205–207: the source-PDF 377 restored numbering/proof/lemma block is continuous.
- Pages 224–226: the retained source-PDF 431 / Proposition 1.8 repair block is continuous, including its large formulas.
- Pages 272–273: Exposé IX closes on page 272 and Exposé X begins on page 273. There is no missing or duplicated page at the seam.
- Pages 349–350: the idx662/idx663 boundary is continuous. The sentence crosses correctly from “classes τ-equivalent to zero have only one” to “Hilbert polynomial. Thus (iii) follows from 2.11.”
- Pages 375–376: idx702, the end of Exposé XIV, bibliography, and terminal notes are complete.
- Pages 377–379: the terminological index is complete and clean. The large lower whitespace on page 379 is the natural end of that index.
- Pages 380–381: the index of notations is complete and clean; terminal `Z(x)` is present on page 381.

## Structural checks

- `complete_pdfinfo.txt` records 381 A4 pages and 381 zero-rotation entries.
- `complete_pdftotext_layout.txt` contains 381 form-feed delimiters, i.e. 382 split segments including the normal trailing empty segment.
- The page-81 extraction contains marker 14 and the full footnote-14 text.
- Layout extraction places the Exposé IX/X seam on PDF pages 272/273, the idx662/663 sentence boundary on PDF page 350, and terminal `Z(x)` on PDF page 381.

## Scope and authority caveat

This PASS establishes that the frozen working PDF is visually whole and correctly assembled. It does not convert draft translation layers into source-certified text. The cover's authority warning remains controlling: the early inherited layer is only partially source-synchronized; the certified control runs through idx662; idx663–702 and the terminal unindexed back matter remain a scan-checked English draft pending incorporation of the open French-workpass corrections by Claude.

No new Claude-facing ambiguity was discovered during visual QA. Any unresolved translation or source-choice flags already recorded in the package remain publication blockers until the relevant locus is corrected or explicitly accepted. Such flags should continue to identify the current-rescribe index, printed volume page, source-PDF page, issue, proposed action, and status.

## Evidence

- `pages/`: all 381 fresh 96-dpi page renders
- `contacts/`: all 20 inspected contact sheets
- `key_pages_200dpi/`: all 31 full-resolution gate renders
- `complete_pdfinfo.txt`: per-page geometry/rotation receipt
- `complete_pdftotext_layout.txt`: final layout-preserving text extraction
- `VISUAL_QA_EVIDENCE_SHA256.csv`: per-file SHA-256 evidence manifest, including the frozen PDF and this report

