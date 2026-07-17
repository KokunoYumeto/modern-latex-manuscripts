# Render check

All five one-page PDFs were rasterized at 150 dpi with Poppler `pdftoppm` and inspected at original resolution, individually and in a contact sheet.

Contact sheet:

`visual_inspection/Noether_Paper26_CJK_tranche_002_contact.png`

## Result

- German: pass; complete page, clean title wrapping, no clipping or margin walk-off.
- Simplified Chinese: pass; title weight is distinct, mixed CJK/Latin controls are readable, and all lines remain inside the text block.
- Traditional Chinese: pass as a generic `zh-Hant` adaptation; traditional forms and Latin controls render without missing glyphs or clipping.
- Japanese: pass; `代数体`, the controlled historical terms, kana/kanji, and punctuation render correctly.
- Korean: pass; Hangul word spaces are preserved, German controls remain legible, and no black boxes or missing glyphs occur.
- All pages retain the title, centered citation, numbered author/location line, complete body, closing publication sentence, and page number.

Visual inspection establishes layout legibility only. It does not replace target-language domain review or establish Taiwan/Hong-Kong localization for the generic `zh-Hant` output.
