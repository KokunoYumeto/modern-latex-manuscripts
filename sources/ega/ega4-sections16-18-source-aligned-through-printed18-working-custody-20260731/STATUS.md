# EGA IV §§16–18 source-aligned English successor

- State: ACTIVE — source alignment in progress.
- Exclusive scope: §16 printed p. 5 through the end of §18; hard stop before §19 printed p. 185.
- Controlling authority: `EGA_IV-4_PMIHES_tome32_1967.pdf`, 360 physical pages, SHA-256 `B4277FB99C6EDF8FEEC5B01F54368E4B8521BCD52871316C0EDF6FF4AE69389E`.
- Exact opening cursor: authority physical PDF page 4 / printed page 5 / §16 opening.
- Current cursor: authority physical PDF page 18 / printed page 19 / Proposition 16.4.5, active `ega4-16.tex` line 737.
- Inherited English inputs are frozen under `source/inherited_input`; all corrections occur copy-on-write under `source/source_aligned`.
- Excluded: §§11–15, §§19–21, EGA I–III, SGA3, and SGA7.
- OCR/text extraction may locate passages but does not decide readings; the direct PDF image controls.
- Controlling no-overlap allocation: `00_lane_control/EGA_IV_SECTIONS11_21_THREE_SESSION_SPLIT_20260730.md`, 2,390 B, SHA-256 `D3BD7DAD97DC09973A624EC24772A19F4691BF7ED9BCF796AB5953C1D9C0283F`.

## Current checkpoint

The inherited source closure is frozen and independently rehashed. Printed pages 5–18 (authority physical pages 4–17) have been aligned directly from overlapping 1800-dpi page bands, with targeted magnification for formula/index ambiguity. The authority's reversed transition-map indices at 16.1.9(b) were corrected transparently in a TeX comment to agree with the displayed map and the convention in 16.1.2. Printed page 10 supplied two substantive inherited corrections: the lower symmetric algebra is over `O_{Y'}` and the base-change homomorphism is `gr(u)\otimes 1`, not `gr(u)\otimes I`. Printed page 11 restored a missing affine-module equality, corrected the placement of a module-tilde, and corrected a prime-locus error from `Gamma(Y,...)` to `Gamma(Y',...)`. Printed page 14 corrected the inherited `Gr_n(P^n_{X/S})` to the source's `Gr_n(P_{X/S})`, restored the Erratum III locator, and preserved rather than pointwise fixed the relevant subobjects under the canonical symmetry. Printed page 16 corrected the limit map's category from graded rings to augmented sheaves of rings. Printed page 17 corrected the inherited transitivity data from `u'',v'',f,f''` to the source's `u'',w'',f,f''`, and pages 17–18 were checked diagram-by-diagram. A rendered seam check rejected checkpoint r4 for the duplicated phrase “taking into Taking into account”; r5 corrects that seam and preserves r4 as adverse history. The active `ega4-16.tex` is 176,685 B, SHA-256 `88D983C556603FB3552BFCC2091EF5D4F270055A1B21A8D64EE39515E2F53E6C`. The three-section harness builds in three XeLaTeX passes to 121 pages; fatal errors 0 and missing glyphs 0. Current checkpoint PDF: 827,157 B, SHA-256 `3C90B846762303B16A98447EE9B543970764175DE8D7B3D21335BECF8782CAE6`.
