# Final rendered visual QA

QA date: 2026-07-17, Europe/Berlin.

PDF under review: `SGA5_English_sync_workpass.pdf`, SHA-256
`176759209CD284F1DD6D3E26D0C7600EC146AB01FAA637BF6F6BB97BFAA396A4`.

## Complete-page render

All 309 PDF pages were rendered at 100 dpi to
`visual_qa/pages/page-001.png` through `page-309.png`. Sixteen ordered contact
sheets under `visual_qa/contact_sheets/` cover pages 1–20 through 301–309. Every
contact sheet was inspected for:

- page presence and order;
- unintended blank pages;
- missing or duplicated exposé starts/ends;
- clipped text, formulas, diagrams, and page numbers;
- collisions, overlaps, corrupt glyphs, or broken page renders;
- gross shifts in margins or text-block geometry.

Result: 309/309 pages render. There is no unintended blank page, missing page,
gross crop, overlap, or broken render. A pixel-content audit found zero exactly
blank page images. The lowest-density pages are intentional sparse content,
including bibliography continuation on page 88 and the final index tail on page
308–309; all three were inspected directly.

For portable evidence viewing, all sixteen contact sheets were re-encoded after
inspection as 8-bit sRGB PNGs; page order and pixels were retained.

## High-risk inspection

Twenty-nine pages were rerendered at 180 dpi to `visual_qa/high_risk/` and
inspected at original image resolution:

| PDF pages | Risk covered | Result |
|---|---|---|
| 4 | breakable bold underline after final layout repair | full sentence wraps; no right-edge loss |
| 23–24 | Exposé-I cartesian-square topology and adjacent formulas | nodes, vertical arrows, labels, and text legible |
| 28–29 | Exposé-I printed-p.48 paired distinguished triangles and the proposition restatement with `+1` labels | both source pairs and all cycles are visible and uncropped |
| 41 | Exposé-I p.71 desingularization diagram | `i'` runs from `U` to `Y'`; all arrows visible |
| 63, 67 | Exposé-III font-warning diagram pages (§§4.4.2 and 4.4.6) | script-size labels are complete, legible, and uncropped |
| 93–94, 97 | Exposé-III-B general-position and restored labelled-square tranche | formulas and labels (1)–(4) legible |
| 111, 115, 118–119, 121, 123–124, 128–129, 135 | restored III-B §§5.0–5.8/semantic repairs, tensor diagrams, module sides, trace formulas, and p.199–202 tranche | no crop or collision; font-warning page 118 and its compact §5.12.3 diagram are fully inside the text block |
| 217 | Exposé-VII restored Lemma 8.2(c) cohomology map | display present and legible |
| 229 | Exposé-VII §9.8.5 intermediate equality and adjacent diagram | omitted step restored; full lower diagram visible |
| 254 | Exposé-X Proposition 4.4 and three restored leading equalities | all cases, primes, and braces legible |
| 264–265 | X/XII boundary and formula-dense XII opening | no page-boundary loss or title collision |
| 282–283 | XII/XV boundary and relative-Frobenius diagrams | headings and full diagrams visible |
| 299 | Exposé-XV noetherian-reduction formulas | long products, indices, and page edges legible |

The nine final overfull-box loci were also located through the build log and
their rendered pages reviewed. Each affected line remains readable on the
physical page; none loses a mathematical symbol or prose continuation.

The three final LaTeX font-warning pages (63, 67, and 118) were likewise
reviewed at 180 dpi. Their warnings concern a script-size declaration in math
mode; no label, glyph, arrow, or formula is missing or displaced.

## Specific before/after layout defects

Two defects found in an earlier render were repaired before the frozen build:

1. PDF page 4 previously clipped the end of a long bold underlined sentence.
   The final breakable underline wraps normally.
2. PDF page 118 previously pushed the §5.12.3 diagram past the right edge. The
   final source-authority compact layout preserves all nodes/arrows/labels and
   fits the text block.

The full 309-page render and the high-risk images were generated from the
hash-pinned final PDF, not from the superseded intermediate builds.

Verdict: **visual-QA pass** for the frozen PDF. This verifies rendering and
layout only; the independent source/formula and topology ledgers remain the
content authority.
