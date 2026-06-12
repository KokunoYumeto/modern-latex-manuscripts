# Workflow Addendum 2026-06-12: OCR Locators, Page Maps, and Source Copies

This addendum records a reusable lesson from the SGA repair lane. It is a workflow note, not a mathematical certification of any SGA text.

## OCR Is A Locator

OCR and math-OCR output should be used to locate likely omissions, formula regions, diagram regions, and prose blocks for review. It should not be pasted into an edition or translation as authority unless a page-specific source comparison promotes it.

The productive pattern is:

1. Generate OCR or math-OCR witnesses from a known source file.
2. Preserve the source checksum, page range, rasterization settings, tool name, model/version when known, and raw output.
3. Compare OCR-derived anchors against current TeX to locate likely gaps.
4. Inspect the source scan or high-resolution crop before accepting or rejecting any candidate.
5. Record the candidate as accepted, rejected, uncertain, context-only, or already-present.

## SGA Tooling Lesson

In French mathematical typescript tests, Surya-style GPU OCR was materially more useful than ordinary CPU OCR as a locator. It preserved more math-bearing prose and often emitted formulas or arrows in LaTeX-like form. RapidOCR-style output remained useful for anchors and formula numbers, but was weaker on mathematical prose and should be treated as a lower-resolution locator.

This is an engine-selection lesson only. Even strong OCR is still witness material. Source images remain the authority.

## Page-Map Caveat

OCR from a different source copy can be useful for broad string search, but it is dangerous for page-specific claims. If an OCR layer was generated from a PDF whose pagination differs from the repair authority, chunk names and page numbers can drift.

Therefore every OCR witness intended for source checking should carry:

- source filename and checksum;
- source page count;
- page-map or scan-page map;
- rasterization DPI and settings;
- OCR engine and model/environment;
- raw output and normalized comparison output;
- reviewer disposition.

Without that metadata, use the OCR only for "this phrase occurs somewhere" questions, not for "this phrase occurs on source page N" claims.

## Aid-Packet Rule

The best aid packet for a web or local review session is compact and labelled. Send page maps, current TeX anchors, source slices, high-resolution crops for hard objects, OCR prose witnesses, and candidate ledgers. Do not send unlabelled image bricks or unscoped OCR dumps and expect the recipient to reconstruct the task.

The reviewer should return a ledger that says exactly which candidates were promoted, rejected, or left uncertain, with source-page references.
