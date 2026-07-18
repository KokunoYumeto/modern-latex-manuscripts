# RTL and bidi invariants

Validated against 180-dpi PNG renders produced from the final PDFs on
2026-07-17.

| Invariant | Test | Arabic | `fa_IR` |
| --- | --- | --- | --- |
| Prose direction | Main paragraph begins at the right margin and flows RTL. | pass | pass |
| Glyph shaping | Arabic-script letters join correctly; no tofu or missing glyph boxes. | pass | pass |
| Language-specific code points | No Persian yeh/keheh leaked into Arabic; Persian uses U+06CC/U+06A9 and preserves 34 ZWNJ joins. | pass | pass |
| Embedded citation | `Math. Ann. 76 (1915), pp. 161--196` remains an isolated LTR run. | pass | pass |
| Segment identifiers | `P06-S0002, P06-S0004, P06-S0005` retain LTR internal order. | pass | pass |
| Date | `2026-07-16` retains LTR internal order. | pass | pass |
| Footnote direction | Footnote marker and text route to an RTL footnote at page bottom. | pass | pass |
| Punctuation | Parentheses, commas, semicolons, quotation marks, and em-dash substitutes are legible in context. | pass | pass |
| Line breaks | No clipping, overlap, overfull line, or isolated orphan line is visible. | pass | pass |
| Formula direction | No formula occurs in this source unit. | not applicable | not applicable |
| Page geometry | A4 portrait, one page, no rotation. | pass | pass |

The PDFs use XeLaTeX, Polyglossia, bidi, and the Windows Arial Arabic-script
coverage. Formula-direction tests become mandatory in the first tranche that
contains mathematics.
