# P29 Korean U01 rendered QA

Both PDFs were rendered with Poppler `pdftoppm -png -r 180 -singlefile` to 1489 × 2105 PNGs and inspected at original resolution.

| Visual ID | Render | SHA-256 | Result |
|---|---|---|---|
| `VE-NOE-P29-KO-U01-003` | `visual_inspection/Noether_Paper29_German_U01_control.png` | `310D979F8FB54027FBAC2DD3CB971F2C9658E311797E53E56328CE83628BFF10` | pass |
| `VE-NOE-P29-KO-U01-004` | `visual_inspection/Noether_Paper29_Korean_U01_v001.png` | `1EF5FE9157DDC2CD1E54A1217142DA2EE8F8E03185C07703F0DA0BDC0E5679DD` | pass |

The inspection covered title hierarchy, citation, author block, all body paragraphs, Fraktur symbols, inline `p`, four footnotes, margins, final line, and page number. The corrected target was rerendered and reinspected at original resolution after changing the criterion to explicit finite-generation wording and `Modulbasis` to a module-generating-system rendering. No clipping, overlap, missing glyph, black box, margin overflow, blank output, footnote collision, or unreadable symbol was found. The two underfull-box warnings have no visible defect.

Printed-source pp. 28–29 were separately inspected at native 400 PPI for the title, author/presenter apparatus, footnote markers/text, criterion label, paragraph continuation, quoted invariant labels, and §1 boundary. No external human visual review is claimed.
