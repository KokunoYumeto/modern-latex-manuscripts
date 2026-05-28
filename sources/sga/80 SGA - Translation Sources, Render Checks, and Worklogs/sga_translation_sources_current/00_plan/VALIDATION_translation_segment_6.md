# Validation - Batch 007

## Build checks

- `pdflatex` pass 1: success.
- `pdflatex` pass 2: success.
- Fresh PDF exists and is readable by `pypdf`.
- Fresh PDF page count: 16.
- Cumulative PDF exists and is readable by `pypdf`.
- Cumulative SGA 4 Exposé I page count: 103.

## Render checks

Fresh PDF sample-rendered pages:

- page 1: `04_render_checks/batch_007/SGA4_Expose_I_sections_9_13_2_to_9_26_en_render/page-01.png`
- page 8: `04_render_checks/batch_007/SGA4_Expose_I_sections_9_13_2_to_9_26_en_render/page-08.png`
- page 16: `04_render_checks/batch_007/SGA4_Expose_I_sections_9_13_2_to_9_26_en_render/page-16.png`

Cumulative PDF sample-rendered pages:

- page 87: `04_render_checks/batch_007/SGA4_Expose_I_sections_0_to_9_26_cumulative_sample_render/page-087.png`
- page 88: `04_render_checks/batch_007/SGA4_Expose_I_sections_0_to_9_26_cumulative_sample_render/page-088.png`
- page 103: `04_render_checks/batch_007/SGA4_Expose_I_sections_0_to_9_26_cumulative_sample_render/page-103.png`

## Notes

The fresh PDF compiled with non-fatal hyperref duplicate-destination warnings due to repeated manually tagged equation labels in a standalone translation file. The PDF is readable and renders. These warnings do not indicate missing pages or a failed build.

No OCR was used.
