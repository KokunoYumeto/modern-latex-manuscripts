# Render check

Both accepted PDFs were rendered with MiKTeX Poppler `pdftoppm -png -r 180 -singlefile`.

| Render | Dimensions | Inspection result |
|---|---:|---|
| `visual_inspection/Noether_Paper27_German_control.png` | 1489 × 2105 | pass |
| `visual_inspection/Noether_Paper27_Korean_v001.png` | 1489 × 2105 | pass |

The German control and Korean page were inspected at original render resolution. The check covered title, centered citation, leading dash and author, body text, Fraktur identifiers and exponents, page number, margins, final line, and page boundary.

No clipping, overlap, missing glyph, black box, margin overflow, accidental blank page, or unreadable formula was observed. The large lower-page whitespace reflects the source notice's short one-page extent and is not a truncation.

Visual gate: **pass**.
