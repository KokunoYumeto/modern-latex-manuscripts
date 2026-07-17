# Render check

All five one-page PDFs were rasterized at 150 dpi with Poppler `pdftoppm` and visually inspected together at original contact-sheet resolution.

Contact sheet:

`visual_inspection/Noether_Paper36_CJK_tranche_001_contact.png`

## Result

- German: pass; complete page, no clipping or margin walk-off.
- Simplified Chinese: pass after font replacement; glyphs are clear, lines remain inside the text block, and the page is nonblank.
- Traditional Chinese: pass; traditional forms render correctly and remain inside the text block.
- Japanese: pass; kana/kanji and punctuation render correctly with no clipping.
- Korean: pass after spacing repair; Hangul word spaces are visible, no black boxes or missing glyphs occur, and the closing line remains inside the text block.
- All pages retain the title, centered citation, numbered author line, complete body, closing publication sentence, and page number.

Visual inspection establishes layout legibility only. It does not replace target-language domain review.
