# Hand transcription and rendering workflow

## Source handling

Use a clean per-paper source PDF where possible. Render the relevant source page range to images before transcribing.

Recommended loop:

```bash
python scripts/render_pdf_pages.py source.pdf renders --from-page 75 --to-page 84 --dpi 220
```

Use the rendered images for visual reading. Text extraction may be used as a rough locator, but it is not authoritative for formulas, primes, Greek letters, subscripts, or diagrams.

## Installments

For hard papers, use 5--10 source pages per installment. Each installment ZIP should contain one top-level folder with:

```text
Installment_pXXX_YYY/
  TEX/
  PDF/
  SCAN/
Cumulative_pSTART_YYY/
  TEX/
  PDF/
  SCAN/
```

The cumulative TeX must be a continuous paper, not separated by artificial page-chunk breaks. Do not insert visible batch labels, source-check labels, internal comments, screenshots, or notes in the clean paper output.

## TeX build

Compile twice:

```bash
python scripts/compile_latex_twice.py paper_EN.tex
python scripts/compile_latex_twice.py paper_FR.tex
```

Then audit:

```bash
python scripts/audit_tex_pdf_package.py CleanPaperPackageRoot
```

The audit script checks for forbidden process labels, logs/reports inside a clean package, missing scan sidecars, and basic PDF page counts.

## Review pass

For every installment, check:

- first page, middle page, and last page render of EN;
- first page, middle page, and last page render of FR;
- scan sidecar page count matches source range;
- no obvious equation overflow or diagram collision;
- no old OCR artifacts such as `chi(x)` for `\kappa(x)`, `J` for `\mathcal J`, or broken prime notation;
- cumulative file flows as a single paper.

## Delivery convention

Clean paper ZIP: reader-facing files only.

Methodology ZIP: workflow, conventions, scripts, failure modes, and reusable local tooling.
