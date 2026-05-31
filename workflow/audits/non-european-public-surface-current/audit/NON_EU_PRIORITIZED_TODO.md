# Non-European Mathematics Web-Session TODO Packet

Goal: repair the current public-facing Non-European mathematics readers only where the replacement is visibly better.

Rules for the web session:
- Keep human-readable work titles and author names.
- Do not include process notes, source-session notes, model names, local paths, or TODO commentary in reader PDFs.
- Preserve older work in artifacts if a new replacement is not clearly better.
- Prefer work-level PDFs, not language-only mega-combines.
- Fix obvious blank pages, tofu squares, visible raw TeX, overfull/overlapping text, unreadably tiny text, and first-page title junk.
- When uncertain, produce a corrected PDF plus a short note explaining what was actually fixed.

Audited 59 current front-facing reader PDFs.
Mechanical classification: 2 critical, 11 review, 46 OK.

## Priority Files

### CRITICAL: 40-01 Chinese Original - Nine Chapters, vols. 1-9.pdf
- Pages: 77; flagged pages: 1, 2, 33, 77.
- Reasons: process notes or source-session wording visible; several blankish or very low-text pages.
- Action: Open the PDF and compare against the TeX/source material. Rebuild only if the replacement is visibly better; keep the same human title pattern; remove process notes, visible raw TeX, tofu squares, empty pages, and obvious overflow.

### CRITICAL: 60-08 Islamic and Arabic Work - al-Battani - Opus Astronomicum, Segments 1-42.pdf
- Pages: 125; flagged pages: 2, 3, 5, 6, 7, 8, 10, 11, 12, 13.
- Reasons: process notes or source-session wording visible; text block bounding boxes exceed page on multiple pages.
- Action: Open the PDF and compare against the TeX/source material. Rebuild only if the replacement is visibly better; keep the same human title pattern; remove process notes, visible raw TeX, tofu squares, empty pages, and obvious overflow.

### REVIEW: 10-08 English Translation - Bhaskara II - Bijaganita, parts 1-3.pdf
- Pages: 59; flagged pages: see PDF.
- Reasons: very large font span; check title/page scaling.
- Action: Open the PDF and compare against the TeX/source material. Rebuild only if the replacement is visibly better; keep the same human title pattern; remove process notes, visible raw TeX, tofu squares, empty pages, and obvious overflow.

### REVIEW: 10-14 English Translation - Robert of Chester and Karpinski.pdf
- Pages: 28; flagged pages: 13.
- Reasons: very large font span; check title/page scaling.
- Action: Open the PDF and compare against the TeX/source material. Rebuild only if the replacement is visibly better; keep the same human title pattern; remove process notes, visible raw TeX, tofu squares, empty pages, and obvious overflow.

### REVIEW: 10-16 English Translation - Rosen - Algebra of Mohammed Ben Musa.pdf
- Pages: 42; flagged pages: see PDF.
- Reasons: very large font span; check title/page scaling.
- Action: Open the PDF and compare against the TeX/source material. Rebuild only if the replacement is visibly better; keep the same human title pattern; remove process notes, visible raw TeX, tofu squares, empty pages, and obvious overflow.

### REVIEW: 20-03 Modern Chinese - Li Ye - Ceyuan Haijing Fenlei Shishu.pdf
- Pages: 104; flagged pages: 69.
- Reasons: possible page-edge overflow.
- Action: Open the PDF and compare against the TeX/source material. Rebuild only if the replacement is visibly better; keep the same human title pattern; remove process notes, visible raw TeX, tofu squares, empty pages, and obvious overflow.

### REVIEW: 20-04 Modern Chinese - Qin - Shuxue Jiuzhang, fasc. 1-9.pdf
- Pages: 132; flagged pages: 2, 35, 36, 37, 39, 51, 54, 68, 88, 117.
- Reasons: several blankish or very low-text pages.
- Action: Open the PDF and compare against the TeX/source material. Rebuild only if the replacement is visibly better; keep the same human title pattern; remove process notes, visible raw TeX, tofu squares, empty pages, and obvious overflow.

### REVIEW: 50-02 Indian Original - Bhaskara II - Bijaganita, parts 1-3.pdf
- Pages: 59; flagged pages: see PDF.
- Reasons: very large font span; check title/page scaling.
- Action: Open the PDF and compare against the TeX/source material. Rebuild only if the replacement is visibly better; keep the same human title pattern; remove process notes, visible raw TeX, tofu squares, empty pages, and obvious overflow.

### REVIEW: 50-04 Indian Original - Brahmagupta - Brahmasphutasiddhanta.pdf
- Pages: 279; flagged pages: 52, 71, 72, 90, 91, 92, 93, 94, 95, 119.
- Reasons: several blankish or very low-text pages; possible page-edge overflow.
- Action: Open the PDF and compare against the TeX/source material. Rebuild only if the replacement is visibly better; keep the same human title pattern; remove process notes, visible raw TeX, tofu squares, empty pages, and obvious overflow.

### REVIEW: 60-01 Islamic Original - al-Kashi - Miftah al-Hisab.pdf
- Pages: 27; flagged pages: see PDF.
- Reasons: very large font span; check title/page scaling.
- Action: Open the PDF and compare against the TeX/source material. Rebuild only if the replacement is visibly better; keep the same human title pattern; remove process notes, visible raw TeX, tofu squares, empty pages, and obvious overflow.

### REVIEW: 60-02 Islamic Original - al-Khwarizmi - Algebra.pdf
- Pages: 31; flagged pages: see PDF.
- Reasons: very large font span; check title/page scaling.
- Action: Open the PDF and compare against the TeX/source material. Rebuild only if the replacement is visibly better; keep the same human title pattern; remove process notes, visible raw TeX, tofu squares, empty pages, and obvious overflow.

### REVIEW: 60-06 Islamic Original - Rosen - Algebra of Mohammed Ben Musa.pdf
- Pages: 42; flagged pages: see PDF.
- Reasons: very large font span; check title/page scaling.
- Action: Open the PDF and compare against the TeX/source material. Rebuild only if the replacement is visibly better; keep the same human title pattern; remove process notes, visible raw TeX, tofu squares, empty pages, and obvious overflow.

### REVIEW: 60-07 Islamic Original - Robert of Chester and Karpinski.pdf
- Pages: 28; flagged pages: 13.
- Reasons: very large font span; check title/page scaling.
- Action: Open the PDF and compare against the TeX/source material. Rebuild only if the replacement is visibly better; keep the same human title pattern; remove process notes, visible raw TeX, tofu squares, empty pages, and obvious overflow.

## Included Files

- `current-reader-pdfs/`: all current front-facing Non-European PDFs from the public record.
- `source-reference/`: compact TeX/source/OCR artifacts useful for repair; deliberately excludes the giant page-image archive.
- `audit/NON_EU_PUBLIC_READER_AUDIT.csv` and `.json`: mechanical audit data.
- `audit/NON_EU_FLAGGED_PAGE_CONTACT_SHEET.pdf`: thumbnails of sampled/flagged pages for quick triage.
