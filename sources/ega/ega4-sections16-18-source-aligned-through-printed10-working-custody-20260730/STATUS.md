# EGA IV §§16–18 source-aligned English successor

- State: ACTIVE — source alignment in progress.
- Exclusive scope: §16 printed p. 5 through the end of §18; hard stop before §19 printed p. 185.
- Controlling authority: `EGA_IV-4_PMIHES_tome32_1967.pdf`, 360 physical pages, SHA-256 `B4277FB99C6EDF8FEEC5B01F54368E4B8521BCD52871316C0EDF6FF4AE69389E`.
- Exact opening cursor: authority physical PDF page 4 / printed page 5 / §16 opening.
- Current cursor: authority physical PDF page 10 / printed page 11 / Proposition 16.2.2 proof continuation, active `ega4-16.tex` line 278.
- Inherited English inputs are frozen under `source/inherited_input`; all corrections occur copy-on-write under `source/source_aligned`.
- Excluded: §§11–15, §§19–21, EGA I–III, SGA3, and SGA7.
- OCR/text extraction may locate passages but does not decide readings; the direct PDF image controls.
- Controlling no-overlap allocation: `00_lane_control/EGA_IV_SECTIONS11_21_THREE_SESSION_SPLIT_20260730.md`, 2,390 B, SHA-256 `D3BD7DAD97DC09973A624EC24772A19F4691BF7ED9BCF796AB5953C1D9C0283F`.

## Current checkpoint

The inherited source closure is frozen and independently rehashed. Printed pages 5–10 (authority physical pages 4–9) have been aligned directly from 1800-dpi page bands, with targeted magnification for formula/index ambiguity. The authority's reversed transition-map indices at 16.1.9(b) were corrected transparently in a TeX comment to agree with the displayed map and the convention in 16.1.2. Printed page 10 supplied two substantive inherited corrections: the lower symmetric algebra is over `O_{Y'}` and the base-change homomorphism is `gr(u)\otimes 1`, not `gr(u)\otimes I`. A rendered seam check rejected checkpoint r4 for the duplicated phrase “taking into Taking into account”; r5 corrects that seam and preserves r4 as adverse history. The active `ega4-16.tex` is 176,540 B, SHA-256 `A2E0227D52CBA9B108F1B6D3AF96E10B6DF1EE38A40703057A1B3E61A67C510C`. The three-section harness builds in three XeLaTeX passes to 121 pages; fatal errors 0 and missing glyphs 0. Current checkpoint PDF: 826,688 B, SHA-256 `EE8147A87CC2AF28B45BF9720D77AA1922E95CDD8CC38DB40E71E7C758AFBABC`.
