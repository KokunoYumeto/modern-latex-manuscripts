# Lead layout and reference QA — EGA IV complete reader R11

Date: 2026-08-01

## Controlling reader

- PDF: `build_r11_stable_reference_runtime_moving_safe_20260801/ega4.pdf`
- Pages: 651 A4 pages
- Bytes: 4,252,287
- SHA-256: `6087FD9475DBDE908EA2025326BC7A49AF33583C7047A7D9332648D2B6387C7A`
- Five XeLaTeX passes completed successfully; passes 3–5 have byte-identical console output, SHA-256 `3ACBC2C6D4E39109E6F2E137067187B11719E89E14069B4494C3CF53DF0BC48A`.

## Reference closure

- Final detector replay: 9,748 candidates = 7,062 live applications + 2,686 positively classified residuals.
- Proposed local links after application: 0.
- Delivered PDF: 5,911 named destinations and 7,374 internal GoTo actions; broken or missing stable targets: 0.
- Delivered target ledger: 2,983 rows; 2,911 AUX-bound labels, 9 bibliography targets, and 63 generated/footnote targets; coordinate mismatches: 0.
- The seven remaining `unresolved_locator_like` detector rows were individually read in context. Five are visibly corrected printed-source slips and two are honest references to `(0_IV, ...)`; none is a pending EGA-IV internal link.

## Personal rendered-page review

The top-level lead performed the review directly. No agent or delegated reviewer supplied mathematical or visual judgment.

- Pages 630–651 were rendered at 600 dpi for page-flow/layout inspection. All index, contents, errata, addenda, and terminal pages are present and show no clipping, overlap, blank-page defect, or broken glyph.
- Page 100 and page 441 were rendered at 600 dpi and inspected at original resolution.
- A small-text reference band on page 100 was additionally rendered at 1,800 dpi: 499,622 B, SHA-256 `B208B0DA8D02F1EA53709E4B7A3E63D254F9CDE19D36895D90973FA7606C2F64`.
- The printed-source-slip note on page 441 was additionally rendered at 1,800 dpi: 1,304,674 B, SHA-256 `F26E1DB41DB09080633B8E1600F9ADDF2C1342A507982E9D649068779274F296`.
- The page-441 pair of similar footnotes was checked against the NUMDAM authority. It is faithful: the printed French page has separate notes `(1)` and `(2)`, both referring to 17.7.11. The English reader therefore preserves both.
- Authority: `EGA_IV-4_PMIHES_1967_32.pdf`, 49,852,990 B, SHA-256 `B4277FB99C6EDF8FEEC5B01F54368E4B8521BCD52871316C0EDF6FF4AE69389E` (not redistributed).

## Result

PASS. The 651-page reader is visually coherent on the reviewed pages and its complete delivered internal-reference surface has no unresolved local link, missing destination, broken GoTo action, raster image, or unembedded font.
