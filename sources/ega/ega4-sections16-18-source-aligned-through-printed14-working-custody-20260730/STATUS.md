# EGA IV §§16–18 source-aligned English successor

- State: ACTIVE — source alignment in progress.
- Exclusive scope: §16 printed p. 5 through the end of §18; hard stop before §19 printed p. 185.
- Controlling authority: `EGA_IV-4_PMIHES_tome32_1967.pdf`, 360 physical pages, SHA-256 `B4277FB99C6EDF8FEEC5B01F54368E4B8521BCD52871316C0EDF6FF4AE69389E`.
- Exact opening cursor: authority physical PDF page 4 / printed page 5 / §16 opening.
- Current cursor: authority physical PDF page 14 / printed page 15 / Proposition 16.3.4 continuation, active `ega4-16.tex` line 500.
- Inherited English inputs are frozen under `source/inherited_input`; all corrections occur copy-on-write under `source/source_aligned`.
- Excluded: §§11–15, §§19–21, EGA I–III, SGA3, and SGA7.
- OCR/text extraction may locate passages but does not decide readings; the direct PDF image controls.
- Controlling no-overlap allocation: `00_lane_control/EGA_IV_SECTIONS11_21_THREE_SESSION_SPLIT_20260730.md`, 2,390 B, SHA-256 `D3BD7DAD97DC09973A624EC24772A19F4691BF7ED9BCF796AB5953C1D9C0283F`.

## Current checkpoint

The inherited source closure is frozen and independently rehashed. Printed pages 5–14 (authority physical pages 4–13) have been aligned directly from overlapping 1800-dpi page bands, with targeted magnification for formula/index ambiguity. The authority's reversed transition-map indices at 16.1.9(b) were corrected transparently in a TeX comment to agree with the displayed map and the convention in 16.1.2. Printed page 10 supplied two substantive inherited corrections: the lower symmetric algebra is over `O_{Y'}` and the base-change homomorphism is `gr(u)\otimes 1`, not `gr(u)\otimes I`. Printed page 11 restored a missing affine-module equality, corrected the placement of a module-tilde, and corrected a prime-locus error from `Gamma(Y,...)` to `Gamma(Y',...)`. Printed page 14 corrected the inherited `Gr_n(P^n_{X/S})` to the source's `Gr_n(P_{X/S})`, restored the Erratum III locator, and preserved rather than pointwise fixed the relevant subobjects under the canonical symmetry. A rendered seam check rejected checkpoint r4 for the duplicated phrase “taking into Taking into account”; r5 corrects that seam and preserves r4 as adverse history. The active `ega4-16.tex` is 176,699 B, SHA-256 `0709ABA3B463E86C5CCB0CE8778BC684F4DBB55D27CBAF21713F4BB141214B35`. The three-section harness builds in three XeLaTeX passes to 121 pages; fatal errors 0 and missing glyphs 0. Current checkpoint PDF: 827,040 B, SHA-256 `5774244064F3BFCF27AAE772C7195A9C4CABBE1EFD6D12004F40FA50556ED314`.
