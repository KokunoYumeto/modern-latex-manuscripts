# R9 Amharic OCR / Unicode / Font-Map Triage

Generated: 2026-07-04

Lane: R9 Africa/Horn/West Africa source-return continuation.

Purpose: advance the Amharic blocker beyond a general "OCR needed" note by sampling rendered pages and text-layer extraction behavior from the current pass2 shelf.

## Boundary

- This is OCR/source triage only.
- No Amharic terms are accepted.
- No Noether prose is drafted.
- No native/community review or license approval is claimed.
- `promotion_allowed=false` for every row.

## Source Shelf

Canonical source artifact: `logs/R9_AMHARIC_FULL_SHELF_SOURCE_RETURN_PASS2_20260703T164546Z.csv`

Overall pass2 state:

- 48 Amharic math candidate PDFs downloaded.
- 588 pages total.
- CSV text status: 3 `extractable_ethiopic_text`, 1 `empty_extraction`, 44 `font_garbled_or_non_unicode_extraction`.

## Tooling Note

The bundled `pdfinfo.cmd` / `pdftoppm.cmd` wrappers failed with `The system cannot find the path specified`. Direct Poppler executables under:

`C:\Users\memo_\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin`

worked for rendering. Poppler reported missing display fonts for `Symbol` and `ArialUnicode` on the sample batch, which supports keeping font-map/OCR triage open.

Rendered first-page PNGs were written under:

`C:\Users\memo_\Documents\Codex\2026-07-04\noether-r9-africa-horn-west\work\tmp\pdfs\amharic_triage`

## Sample Decisions

| PDF row | Initial CSV status | Visual page-1 result | Text-layer result | Decision |
| --- | --- | --- | --- | --- |
| 001 Grade 1 Chapter 10 | `font_garbled_or_non_unicode_extraction` | visible Ethiopic/Amharic glyphs and math table render | pypdf all pages: 46 chars, 0 Ethiopic | image/OCR or font-map required; no text extraction use |
| 014 Grade 2 Chapter 10 | `extractable_ethiopic_text` | visible Ethiopic/Amharic glyphs render | pypdf all pages: 1911 chars, 522 Ethiopic, Ethiopic on pages 3-4 | page-level text usable for triage only; engine divergence requires verification |
| 025 Grade 3 Chapter 1 | `empty_extraction` | visible cover text renders | pypdf all pages: 0 chars | image/OCR required; no text extraction use |
| 045 Grade 6 Chapter 4 | `extractable_ethiopic_text` | visible rendered page | pypdf all pages: 31092 chars, 4804 Ethiopic | candidate for reviewer-facing OCR-clean text audit, not term promotion |
| 048 Grade 6 Chapter 7 | `extractable_ethiopic_text` | visible rendered page | pypdf all pages: 44565 chars, 15930 Ethiopic | candidate for reviewer-facing OCR-clean text audit, not term promotion |

## Closure Decision

Amharic remains blocked for corpus translation. The shelf is visually real and source-rich, but the text layer is mixed:

- rows 045 and 048 are the best next text-audit candidates;
- row 014 needs page-level extraction reconciliation because the CSV and pypdf counts differ;
- row 001 and row 025 prove that visible Ethiopic pages can still have unusable text layers;
- the 44 garbled/font rows cannot feed term or prose support until OCR/font-map repair or human transcription exists.

## Next Artifact

Create:

`R9_AMHARIC_OCR_CLEAN_TEXT_AUDIT_<timestamp>.md/json/csv`

Minimum columns:

- `pdf_index`
- `pdf_sha256`
- `page`
- `visual_text_present`
- `pypdf_ethiopic_count`
- `poppler_text_count`
- `ocr_text_count`
- `font_map_needed`
- `human_transcription_needed`
- `reviewer_question`
- `source_permission_note`
- `promotion_allowed`

