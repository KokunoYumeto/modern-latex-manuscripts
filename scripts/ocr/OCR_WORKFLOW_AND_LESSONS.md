# OCR Workflow and Lessons

This note records practical lessons from the al-Battani table reconstruction and the broader math-OCR experiments. It is meant to be reused by future local agents and by other projects trying to turn scanned mathematical sources into editable TeX/data.

## Resolution First

Many "OCR failed" cases were really source-resolution failures. Clean public PDFs often downsample or crop away the evidence needed for table cells, dots, primes, and diacritics. For table work, use the highest-resolution original scan and render tight crops from the source PDF. Full pages are expensive and noisy; cell/row crops are faster and more accurate.

## Preserve Source Authority

For numerical historical tables, first look for a scholarly printed edition of the table. In al-Battani, Nallino's printed Latin table with Western numerals was more authoritative and easier to check than trying to decode every abjad numeral from a lower-resolution Arabic witness. Manuscript witnesses still matter, but the critical printed table may be the correct source for public numeric data.

## Use a Dispatcher

No single OCR tool is best for all content. The reusable pattern is:

- `math` -> Pix2Text for page/region math into Markdown/LaTeX.
- `math_equation` -> pix2tex for single cropped equations.
- `multilingual` -> Surya or another multilingual text OCR engine.
- `historical` -> Kraken or another trainable OCR engine, trained on real labeled lines/cells from the target print.
- `layout` -> docling or a layout-aware detector.

See `ocr_dispatch.py` for a thin routing layer. Set `MLM_OCR_PYTHON` to an isolated OCR environment so OCR dependencies do not clobber the main project environment.

## GPU/VLM Findings

Local vision-language models can help with prose columns and page/region triage, but they were not reliable for tiny abjad numeric cells. The tested pattern was fast enough on a 16 GB consumer GPU when using row/cell crops, but full-page inputs wasted memory and context. VLM output remains draft evidence, never insertion-grade TeX/data.

## Trainable OCR Is Label-Hungry

Synthetic-only abjad-number classifiers did not transfer cleanly to real 1899 print. The reliable route is to hand-read enough cells/lines to form a real labeled training set, then fine-tune a trainable OCR model on the actual typeface. Manual transcription is not wasted: it becomes training data.

## Math OCR Is Useful Now

Pix2Text produced useful LaTeX from real mathematical pages, including aligned equations, fractions, subscripts/superscripts, and tags. It should be used as a formula witness generator for formula-heavy authors, especially when the prose OCR is already acceptable. Its output still needs scan comparison and render-checking before promotion.

## Operational Rules

- Keep OCR/ML tools in isolated environments.
- Use scans and crops as witnesses, not replacements for TeX.
- Prefer page/region manifests with source page numbers and crop coordinates.
- Promote source-checked TeX/PDF, not screenshots.
- Keep source scans, crop witnesses, accepted/rejected OCR candidates, and render checks in the source packet.
- Do not re-run expensive OCR blindly over ranges already known to fail; change the source quality, crop strategy, or tool.

