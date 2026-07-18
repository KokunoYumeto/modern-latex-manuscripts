# Controlled-Romance PDF visual QA v7

Date: 2026-07-17. The current T002 and T003 PDFs were freshly rendered with the pinned Poppler runtime at 150 dpi, inspected at the original 1241 × 1754 pixel resolution, and compared byte-for-byte with their stored QA renders. `PDF_RENDER_REPRODUCIBILITY_v7.json` records the executable reproduction.

- **T002 page 2:** the corrected page begins with a deliberate top margin. The first nonwhite pixel row is 299 of 1754, the heading cap height is fully visible, and no glyph touches or crosses the top boundary. Text, formulas, page number, and the large intentional lower whitespace are clean. Fresh-render SHA-256 `81E74EB9D99D573173BF5E9034B5FDDBF57F98343A9133FF5A88386C335949CA` exactly matches the pinned render.
- **T003 pages 1–2:** title/status/source boundary, direct and reciprocal module definitions, all action-order and annihilator formulas, editorial sense notes, and continuation boundary are legible. There is no clipping, overlap, missing glyph, or margin escape. Fresh renders exactly match the pinned page hashes `15B7DD9471FEB10819EE47D9C8A33AAD5E838A158F13AF44BF30D0E42B1F5053` and `0D3BEEEC4340AE63FC633ABEE90F23426E978EB8AF2B160E955601E8D1C004AA`.

Result: **PASS** for render reproducibility and visual layout. This does not constitute linguistic review, human comprehension evidence, or a pilot result.
