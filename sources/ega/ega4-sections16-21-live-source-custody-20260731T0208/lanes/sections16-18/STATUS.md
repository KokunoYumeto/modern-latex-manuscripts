# EGA IV §§16–18 source-aligned English successor

- State: ACTIVE — source alignment in progress.
- Exclusive scope: §16 printed p. 5 through the end of §18; hard stop before §19 printed p. 185.
- Controlling authority: `EGA_IV-4_PMIHES_tome32_1967.pdf`, 360 physical pages, SHA-256 `B4277FB99C6EDF8FEEC5B01F54368E4B8521BCD52871316C0EDF6FF4AE69389E`.
- Exact opening cursor: authority physical PDF page 4 / printed page 5 / §16 opening.
- Current cursor: authority physical PDF page 46 / printed page 47 / proof of Proposition 16.9.3, active `ega4-16.tex` line 2282.
- Inherited English inputs are frozen under `source/inherited_input`; all corrections occur copy-on-write under `source/source_aligned`.
- Excluded: §§11–15, §§19–21, EGA I–III, SGA3, and SGA7.
- OCR/text extraction may locate passages but does not decide readings; the direct PDF image controls.
- Controlling no-overlap allocation: `00_lane_control/EGA_IV_SECTIONS11_21_THREE_SESSION_SPLIT_20260730.md`, 2,390 B, SHA-256 `D3BD7DAD97DC09973A624EC24772A19F4691BF7ED9BCF796AB5953C1D9C0283F`.

## Current checkpoint

The inherited source closure is frozen and independently rehashed. Printed pages 5–46 (authority physical pages 4–45) have been aligned directly from 600-dpi full pages and overlapping 1800-dpi page bands, with targeted magnification for formula/index ambiguity. The detailed correction history is append-only in `LOGBOOK.md`; substantive recent repairs include the order-$n'$ representation of the second differential operator, the $I_n$ induction sum, the discrete target `Gamma(U,G)` in the continuous-homomorphism description, a wrong equation tag and internal reference, principal-parts module sides, and the functor variable in the arbitrary-direct-sum argument. Obvious printed cross-reference/ring typos are corrected transparently where the surrounding mathematics fixes the intended reading. Active `ega4-16.tex`: 176,755 B, SHA-256 `CE9A3A21F0D8BE10065D24B9BACBBCD5A82E958A55FF31E9D9BDA445BC8D8A6A`. Checkpoint r15 builds in three XeLaTeX passes to 121 letter pages; fatal errors 0, undefined control sequences 0, missing glyphs 0, duplicate destinations 0. The expected partial-harness undefined-reference summary and one pre-existing later-section overfull box remain. Current PDF: 827,826 B, SHA-256 `83137ED5636D9F18D4992B73FDB1AE7FDE7AB5E1B930F4DEDD8EE451FD176DB9`; build log SHA-256 `6835B1BC17EB88461B0922FA9530A502C6175C05BBAA373FB09BEFEED7F9FCF6`. English reader pages 29–34 were rendered at 600 dpi and personally checked; formulas, diagrams, section transition 16.8→16.9, proof boxes, and page seams are intact.
