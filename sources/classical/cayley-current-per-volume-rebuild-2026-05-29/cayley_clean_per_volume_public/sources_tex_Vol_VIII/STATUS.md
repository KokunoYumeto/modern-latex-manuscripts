# Cayley Vol VIII — Direct-Typeset Status

## What's here

**Merged partial PDF:** `../Cayley_Collected_Mathematical_Papers_Vol_VIII_partial.pdf`
419 pages: 416 typeset book content + 3 gap placeholders + 0-page-overhead front matter.

**Per-chunk source TeX + PDF** in this directory:

| Book pp | PDF pages | Status |
|---|---|---|
| 1–16 | 15 | clean |
| 17–66 | 6 | **partial** (agent blocked at ~p23; needs redo for pp 24-66) |
| 67–116 | 41 | clean |
| 117–166 | 50 | clean (one `% TODO` for table on p122) |
| 167–216 | 49 | clean (some tables abbreviated, structure preserved) |
| 217–241 | gap | not completed, **needs typesetting** |
| 242–266 | 25 | clean |
| 267–291 | 25 | clean |
| 292–316 | gap | not completed, **needs typesetting** |
| 317–366 | 49 | clean (some `% TODO` on dense pp 339-340, 344, 348, 365) |
| 367–416 | 50 | clean (cube-line tables on pp 368-9, 374-5, 378, 393 marked `[table omitted]`) |
| 417–441 | 26 | clean |
| 442–466 | 25 | clean |
| 467–516 | 51 | clean |
| 517–566 | gap | not completed, **needs typesetting** |
| 567–570 | 4 | clean (END OF VOL. VIII) |

**Total typeset: ~416 of 570 book pages (~73%).**

Source scan PNGs (640 files, 452 MB) at `_scan_pages/`.
Source scan PDF (45 MB) at `../Cayley_Collected_Mathematical_Papers_Vol_VIII_source_scan.pdf` as fallback for the gaps.

## Filter-blocked chunks — recommendation

Four chunks (pp 17–66 partial, 217–241, 292–316, 517–566) were blocked by
content filters during agent runs. The pattern: long final response
messages with summary prose trigger filters; short final messages
("Done. Exit 0.") don't.

Three options to close the gaps:
1. **Foreground local repair pass session** — typeset the ~150 gap pages directly,
   one mini-chunk at a time with minimal-output prompts. Probably
   ~4-5 hours sequential.
2. **source system pipeline** queued for Vol VIII specifically — produces TeX
   from same scans, output integrates with existing chunks. Days of
   wall-clock.
3. **Ship as-is with gap markers** — the placeholder pages already note
   "Modern LaTeX typesetting pending; refer to source scan for these
   pages." Honest labeling, no false claims.

## Quality bar

Direct-typeset chunks preserve `\Delta`, `\partial`, subscripts,
superscripts, brace nesting, `\Sigma`, `\int`, primes, accents — the
exact symbols source system was found to drop in the broader audit. Spot-checked
clean.

Some dense numerical tables are marked `% TODO` or `[table omitted]`
where the OCR was ambiguous; the surrounding structure (sections,
papers, displayed equations) is intact.

This serves as the **proof of concept** that direct scan-based is a
viable typesetting workflow when source system has failed — exactly the
recommendation in the Phase 2 synthesis for the 15-20 corrupted chunks
across other authors.
