# Noether R7 Myanmar LearnBig Math Textbook PDF Capture - 2026-07-05

Scope: source-canon/provenance only. This packet adds Myanmar/Burmese mathematics textbook witnesses from LearnBig routes that attribute the books to Myanmar basic-education / Ministry of Education sources. It does not translate, approve terms, claim native review, claim canonical approval, clear licenses, promote gates, claim completion, or push Git.

Rows:

- CSV: `NOETHER_R7_MYANMAR_LEARNBIG_MATH_TEXTBOOK_PDF_CAPTURE_ROWS_20260705.csv`
- Row count: 8
- Payload policy: no raw PDF, HTML, text, or source bodies are stored in `outputs`; PDFs were downloaded to temporary files, hashed, byte-counted, and deleted immediately.

## Captured Routes

- Kindergarten Basic Mathematics item page and S3 PDF bitstream.
- Grade 5 Mathematics item page and S3 PDF bitstream.
- Grade 6 Mathematics item page and S3 PDF bitstream.
- Grade 10 Mathematics item page and S3 PDF bitstream.

## Findings

- All four LearnBig item pages returned HTTP 200 as HTML and exposed hidden PDF download URLs.
- All four PDF bitstreams returned HTTP 200 as `application/pdf`.
- PDF byte counts and SHA-256 values were captured from temp files, then the temp files were deleted.
- The Grade 10 PDF is the strongest source witness in this packet for secondary mathematics, but it remains PDF fallback rather than TeX/LaTeX/e-print/source archive material.
- LearnBig item pages carry Ministry/committee attribution and educational-use conditions; no license clearance is claimed.

## PDF Hashes

- Kindergarten PDF: 37,801,801 bytes; SHA-256 `7F45D46F6F422F3254F74D23A710015749B80D4A2DC53B9699B02FAB295B300E`
- Grade 5 PDF: 18,969,929 bytes; SHA-256 `F655832BD2593956743A5441E08150D2B3C1C1717F945605BBE4B7AFEB55EA16`
- Grade 6 PDF: 48,894,022 bytes; SHA-256 `EC97D32D848EEEA06DB62E10A364AD7B39D2B33638BD2BD4F04957DDC9D93B3A`
- Grade 10 PDF: 341,363,922 bytes; SHA-256 `FA98C15B61AB365A609967CC4836A23B4A6EC2885931BB15F8F2A0F983B9D419`

## Disposition

This packet strengthens the SEA/Pacific source-canon shelf with exact Myanmar/Burmese mathematics PDF provenance, especially for Grade 10. It does not close the source-level archive gap: no TeX, LaTeX, arXiv, e-print, or editable source package was found or stored.

Next source actions:

- Search for official Myanmar MOE source/archive routes matching these PDFs.
- Search for university or journal-level Burmese/Myanmar algebra, ring/module/group, or proof-prose material.
- Keep LearnBig/S3 rows as exact PDF fallback witnesses with educational-use/no-clearance boundary.

## Validation Snapshot

- Row CSV count: 8
- HTML item-page rows: 4
- Temp-hashed PDF bitstream rows: 4
- HTTP 200 rows: 8
- Rows missing SHA-256/hash field: 0
- Rows missing required no-claim boundary: 0
- Duplicate row IDs: 0
- Raw PDF/HTML/text/source payload files stored in `outputs`: 0
- Coverage map row: `R7COV022`
