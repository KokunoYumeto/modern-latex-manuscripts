# Cayley review system Progress and Cost Inventory — 2026-05-31

## Headline

- **older full assembled rendered pages**: 7216
- **validated pickup pdf count**: 127
- **validated pickup rendered pages**: 3307
- **validated unique book pages from filename ranges**: 3917
- **source book pages in chunk map**: 8394
- **validated percent of chunk mapped book pages**: 46.7
- **v2 fix pdf count**: 117
- **v2 fix tex count**: 122

## Interpretation

- There are older cumulative per-volume PDFs/TeX covering essentially the whole Cayley corpus, but they include OCR junk, summaries, hallucinated or missing math in places, so they should be treated as a baseline corpus rather than faithful public reader.
- The pickup directory is the safer measure of review system-paid progress: 127 PDFs marked as scan-validated slices by review system, totaling 3307 rendered pages and about the listed book-page coverage below.
- Most validated slices are useful and close to source-faithful, but still need layout QA for oversized or split equations; deep audit shows some non-validated full-volume chunks remain seriously wrong.

## Volume coverage by validated pickup slices

| Volume | Source book pages mapped | Validated book pages | Percent | Main gaps against chunk map |
|---|---:|---:|---:|---|
| Front matter | 160 | 0 | 0.0% | 1-160 |
| Vol I | 620 | 150 | 24.2% | 1-125, 226-300, 351-620 |
| Vol II | 628 | 225 | 35.8% | 1-25, 251-628 |
| Vol III | 594 | 212 | 35.7% | 101-150, 176-250, 276-325, 388-594 |
| Vol IV | 648 | 350 | 54.0% | 1-25, 376-648 |
| Vol V | 650 | 350 | 53.8% | 351-650 |
| Vol VI | 636 | 636 | 100.0% |  |
| Vol VII | 652 | 275 | 42.2% | 226-275, 326-652 |
| Vol VIII | 570 | 570 | 100.0% |  |
| Vol IX | 650 | 199 | 30.6% | 1-25, 38-400, 563-575, 601-650 |
| Vol X | 640 | 300 | 46.9% | 301-640 |
| Vol XI | 672 | 225 | 33.5% | 26-50, 101-200, 226-250, 276-350, 401-450, 501-672 |
| Vol XII | 680 | 225 | 33.1% | 226-680 |
| Vol XIII | 594 | 200 | 33.7% | 151-200, 251-594 |

## Quality caveats

- The 7,216-page full assembled Cayley set exists, but it is not the same as source-faithful completion. Some old volume-level PDFs still contain summaries, OCR garbage, hallucinated math, missing pages, or layout failures.
- The 127-file `cayley_codex_pickup` set is the safer “paid review system work” measure: it is specifically described as OCR-skeleton + PNG-verified or direct scan-typeset.
- The pickup PDFs still need visual layout QA. Many equations are present in TeX but may overflow or split badly on the page.
- Deep audit of Vol X remains a warning: broad non-validated Vol X material is not production quality until replaced by validated slices.

## Cost heuristic

- Treating this as roughly **about 30-50 USD of review system subscription usage, while also doing EGA, Gauss, downloads and triage**, review system produced about **3307 rendered pages** / **3917 unique book pages** of validated pickup material.
- That is roughly **66.1 rendered pages per $50** or **78.3 book pages per $50** for this run.
- Naive rate: **$0.0151 per rendered page** or **$0.0128 per book page**, before proofing/layout polish and before harder-page penalty.
- Grant-planning conservative multiplier: expect real production completion to cost several times the naive page rate once you include dense tables, diagrams, hard math, final visual QA, and second-pass source comparison.

## Public location notes

- **validated pickup**: mirrored in this repository under `reader-pdfs/classical/` and in the classical shelf source artifacts.
- **latest source fixes**: preserved in the current classical shelf source ZIPs and extracted source folders.
- **older full assembled per-volume set**: treated as a baseline scaffold rather than the source-faithful public reader.
- **deep audit**: summarized here; the detailed audit remains a local working artifact until sanitized for publication.
