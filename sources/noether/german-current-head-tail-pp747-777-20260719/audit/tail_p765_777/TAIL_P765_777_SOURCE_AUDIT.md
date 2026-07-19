# Tail pp. 765-777 source audit

## Scope and method

LocalCodex independently opened every collected-volume source page from p. 765 through p. 777 and compared it with the corresponding live cumulative TeX. The audit covered prose, displayed and inline mathematics, symbol families, accents, emphasis, footnotes, bibliography labels, page continuity, and final backmatter entries.

The source authority was the included IA-derived collected-volume scan packet. Package-local pages 55-67 were rendered at 650 dpi. Dense or ambiguous fields on pp. 767, 768, and 771 were enlarged again from those renders before adjudication. OCR and inherited ledgers were not used as authority.

## Confirmed repairs

### TAIL-20260719-F001: collected p. 768

Four occurrences in Zusatz II and the Bertini paragraph visibly use the `varrho` symbol family. The inherited TeX used `rho`. All four were changed to `\varrho` as one coordinated source-backed repair.

### TAIL-20260719-F002: collected p. 775

Bibliography item 34 visibly ends its label with a period. The inherited TeX had a colon. The label was restored from `34:` to `34.`.

## Diplomatic no-patch rulings

### Collected p. 767, equation (3)

The source unambiguously prints `xK_1` and `xK_2` at the ends of the first two recurrence rows, while its general row ends in `xK_{r+1}` and the prose implies the shifted `K_2`, `K_3` progression. This is logged as probable original-print mathematical inconsistency `SE-20260719-TAIL-KAPFERER-001`. The German body remains source-literal.

### Collected p. 771, proof of (5)

The source unambiguously prints `f(0,y)` without subscript `i` in the second identity, while the surrounding recurrence strongly suggests `f_i(0,y)`. This is logged as probable original-print subscript omission `SE-20260719-TAIL-KAPFERER-002`. The German body remains source-literal.

### Negative controls

- p. 772 deliberately distinguishes `y^{(K)}` in the opening statement from `y^\lambda` in the proof. The distinction is retained.
- p. 777 visibly prints `Öystein Orne` and `Brauschweig` in the bibliographic entry. The diplomatic spellings are retained.

## Build and render QA

XeLaTeX passed twice. The cumulative remains 466 pages. Pass 2 has zero fatal errors, undefined controls, emergency stops, rerun requests, overfull boxes, underfull boxes, and missing-character flags.

Output pages 455-466 were rendered before and after at 220 dpi and compared pixelwise. Only output p. 459 changed for the four `varrho` glyphs (424 differing pixels), and output p. 463 changed for the bibliography punctuation (38 differing pixels). All other pages in the comparison band were pixel-identical. Final p. 459 and p. 463 renders were reopened visually; symbols are complete and no clipping, overlap, or incoherent reflow is present.

## Provenance and closure

Both body fixes and both source-error candidates were found by LocalCodex in this independent pass. The user set the source-critical completion requirement but supplied no symbol reading for these loci. Web Pro was kept on the non-overlapping Paper 2 lane.

Closure is limited to collected pp. 765-777 on this exact head and witness. The remaining tail bands pp. 711-746 and pp. 747-764 still need equivalent full-page closure.
