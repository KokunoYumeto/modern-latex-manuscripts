# Non-European Corpus Current Repair Queue

Generated: 2026-05-28 19:50 Europe/Berlin

This is a continuation queue for the current public non-European/multilingual working release. The release remains usable and is better than the previous public surface, but the files below deserve targeted repair or visual comparison before the next polish pass.

## Summary

- Public PDFs in current staged record: 66
- Files needing targeted review under the stricter local sweep: 13
- Public-process-note audit across Zenodo still reports 0 process-note flags; the items below are mostly glyph/layout/sparse-text quality work.

## Queue

### P1 - 01 Combined English Translations.pdf

- Issue: square/missing glyphs in extracted text
- Audit reason: `missing_or_corrupt_glyph_chars=727`
- Pages: 1213; near-blank text pages: 24
- Square/missing-glyph count in extracted text: 727
- Sample blank/sparse pages: 16, 751, 907, 910, 911, 921, 938, 941, 979, 990, 991, 995, 1007, 1012, 1013, 1016, 1017, 1037, 1151, 1153, 1157, 1158, 1163, 1164
- Archive assessment: quality/layout issue only
- Next action: recompile from TeX with verified CJK/Sanskrit fonts or replace damaged glyph runs from source TeX

### P1 - 02 Combined Modern Chinese Renderings.pdf

- Issue: square/missing glyphs in extracted text
- Audit reason: `missing_or_corrupt_glyph_chars=371`
- Pages: 460; near-blank text pages: 13
- Square/missing-glyph count in extracted text: 371
- Sample blank/sparse pages: 17, 35, 90, 135, 175, 247, 276, 303, 321, 323, 360, 362, 446
- Archive assessment: quality/layout issue only
- Next action: recompile from TeX with verified CJK/Sanskrit fonts or replace damaged glyph runs from source TeX

### P1 - 04 Chinese Originals - Modern LaTeX.pdf

- Issue: square/missing glyphs in extracted text; process-pattern or placeholder text hit
- Audit reason: `missing_or_corrupt_glyph_chars=498; process_hits=1`
- Pages: 587; near-blank text pages: 14
- Square/missing-glyph count in extracted text: 498
- Sample blank/sparse pages: 2, 28, 87, 109, 130, 155, 183, 218, 261, 376, 397, 413, 446, 507
- Archive assessment: possible placeholder wording; verify and replace if it is editorial scaffolding
- Next action: recompile from TeX with verified CJK/Sanskrit fonts or replace damaged glyph runs from source TeX; review text context: in the history of math- ematics: • Symbolic algebra: The use of “元” (yuan) as a placeholder for the unknown predates Eur

### P2 - 06 Islamic and Arabic Originals - Modern LaTeX.pdf

- Issue: process-pattern or placeholder text hit
- Audit reason: `process_hits=1`
- Pages: 228; near-blank text pages: 36
- Sample blank/sparse pages: 2, 40, 62, 167, 168, 170, 185, 187, 188, 189, 190, 191, 192, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206
- Archive assessment: likely manuscript-codex false positive; verify visually/textually before changing
- Next action: review text context: d (MS Hunt. 214, fols. 1–123), copied in 743 AH / 1342 CE. It forms part of the codex designated CMXXVIII, which also co

### P1 - 10-02 English Translation - Li Ye - Ceyuan Haijing, vols. 1-12.pdf

- Issue: square/missing glyphs in extracted text
- Audit reason: `missing_or_corrupt_glyph_chars=727`
- Pages: 144; near-blank text pages: 0
- Square/missing-glyph count in extracted text: 727
- Archive assessment: quality/layout issue only
- Next action: recompile from TeX with verified CJK/Sanskrit fonts or replace damaged glyph runs from source TeX

### P2 - 10-18 English Translation - al-Muqaddasi - Ahsan al-Taqasim.pdf

- Issue: sparse/near-blank text extraction on several pages
- Audit reason: `many_blank_text_pages=6`
- Pages: 15; near-blank text pages: 6
- Sample blank/sparse pages: 1, 3, 7, 8, 13, 14
- Archive assessment: quality/layout issue only
- Next action: visually compare sampled pages to source scan; keep if these are intentional scan/plate pages, otherwise rebuild

### P1 - 20-02 Modern Chinese - Li Ye - Ceyuan Haijing, vols. 1-12.pdf

- Issue: square/missing glyphs in extracted text
- Audit reason: `missing_or_corrupt_glyph_chars=371`
- Pages: 89; near-blank text pages: 1
- Square/missing-glyph count in extracted text: 371
- Sample blank/sparse pages: 47
- Archive assessment: quality/layout issue only
- Next action: recompile from TeX with verified CJK/Sanskrit fonts or replace damaged glyph runs from source TeX

### P2 - 30-04 Arabic Translation - al-Kashi - Miftah al-Hisab.pdf

- Issue: sparse/near-blank text extraction on several pages
- Audit reason: `many_blank_text_pages=10`
- Pages: 38; near-blank text pages: 10
- Sample blank/sparse pages: 2, 3, 4, 6, 10, 14, 18, 26, 30, 32
- Archive assessment: quality/layout issue only
- Next action: visually compare sampled pages to source scan; keep if these are intentional scan/plate pages, otherwise rebuild

### P1 - 40-02 Chinese Original - Li Ye - Ceyuan Haijing, vols. 1-12.pdf

- Issue: square/missing glyphs in extracted text
- Audit reason: `missing_or_corrupt_glyph_chars=498`
- Pages: 95; near-blank text pages: 4
- Square/missing-glyph count in extracted text: 498
- Sample blank/sparse pages: 2, 24, 45, 70
- Archive assessment: quality/layout issue only
- Next action: recompile from TeX with verified CJK/Sanskrit fonts or replace damaged glyph runs from source TeX

### P1 - 40-08 Chinese Original - Zhu Shijie - Suanxue Qimeng, parts 1-2.pdf

- Issue: process-pattern or placeholder text hit
- Audit reason: `process_hits=1`
- Pages: 52; near-blank text pages: 0
- Archive assessment: possible placeholder wording; verify and replace if it is editorial scaffolding
- Next action: review text context: in the history of math- ematics: • Symbolic algebra: The use of “元” (yuan) as a placeholder for the unknown predates Eur

### P2 - 60-02 Islamic Original - al-Khwarizmi - Algebra.pdf

- Issue: process-pattern or placeholder text hit
- Audit reason: `process_hits=1`
- Pages: 47; near-blank text pages: 2
- Sample blank/sparse pages: 14, 36
- Archive assessment: likely manuscript-codex false positive; verify visually/textually before changing
- Next action: review text context: d (MS Hunt. 214, fols. 1–123), copied in 743 AH / 1342 CE. It forms part of the codex designated CMXXVIII, which also co

### P2 - 60-07 Islamic Original - Robert of Chester and Karpinski.pdf

- Issue: process-pattern or placeholder text hit
- Audit reason: `process_hits=10`
- Pages: 204; near-blank text pages: 29
- Sample blank/sparse pages: 1, 3, 4, 5, 6, 7, 11, 16, 18, 59, 60, 61, 62, 71, 72, 73, 74, 90, 91, 92, 94, 119, 188, 199, 200
- Archive assessment: likely manuscript-codex false positive; verify visually/textually before changing
- Next action: review text context: TA MELBOURNE THE MACMILLAN CO. OF CANADA, Ltd. TORONTO Plate I. no lillli 4^^ Codex Vindobonensfs 4770, Fol. 1'''. ROBER | Fakhri, p. 29. ' The Algebra of Abu Kaviil, loc. cit. ^Scritti, Vol. I, p. i. 5 Codex Palat. 567, Biblioteca Nazionale,  | also in Zeitschrift f. Math, uiid Physik, Hist.-Ut. Abtheil., Vol. 45, 1900. ^ Codex Dresden C. 80. 3 Woepcke, Atti delV

### P2 - 70-02 Reference Text - al-Muqaddasi - Ahsan al-Taqasim.pdf

- Issue: sparse/near-blank text extraction on several pages
- Audit reason: `many_blank_text_pages=6`
- Pages: 15; near-blank text pages: 6
- Sample blank/sparse pages: 1, 3, 7, 8, 13, 14
- Archive assessment: quality/layout issue only
- Next action: visually compare sampled pages to source scan; keep if these are intentional scan/plate pages, otherwise rebuild
