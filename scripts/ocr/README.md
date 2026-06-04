# OCR and Formula Extraction Workflow

This folder contains reusable OCR helpers for the manuscript pipeline.

The central idea is routing each page region to the tool that is actually good at that content type:

- math/formulas -> Pix2Text or pix2tex
- modern multilingual print -> Surya or a comparable multilingual OCR engine
- historical print and abjad numerals -> a trainable OCR engine such as Kraken, with real labeled cells/lines
- layout and table structure -> docling or layout-aware OCR
- local VLMs -> useful for prose/description columns, not trusted for numeric abjad cells without verification

Use an isolated OCR Python environment and point the dispatcher at it:

```powershell
$env:MLM_OCR_PYTHON = "C:\path\to\ocr_env\Scripts\python.exe"
python scripts\ocr\ocr_dispatch.py page_or_crop.png math
```

Do not paste OCR output directly into public TeX. Treat it as a witness layer: crop, transcribe, compare against the scan, compile, render-check, and only then promote.

