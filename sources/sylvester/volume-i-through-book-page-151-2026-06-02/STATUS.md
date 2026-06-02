# Sylvester Volume I Batch 09 Status

Date: 2026-06-02

## Coverage

Current cumulative edition:
- Volume I book pp. 1-151
- Source PDF pp. 19-169
- Completed cumulative sequence now includes Papers 1-25.

New work this round:
- Book pp. 119-151 / source PDF pp. 137-169
- Paper 22: "On the intersections, contacts, and other correlations of two conics expressed by indeterminate coordinates" (book pp. 119-137)
- Paper 23: "An instantaneous demonstration of Pascal's theorem by the method of indeterminate coordinates" (book p. 138)
- Paper 24: "On a new class of theorems in elimination between quadratic functions" (book pp. 139-144)
- Paper 25: "Additions to the articles 'On a new class of theorems,' and 'On Pascal's theorem'" (book pp. 145-151)

## Deliverables

- `cumulative_current/original_language/tex/Sylvester_Collected_Papers_Volume_I_original_language_bookpp001_151.tex`
- `cumulative_current/original_language/pdf/Sylvester_Collected_Papers_Volume_I_original_language_bookpp001_151.pdf`
- `cumulative_current/original_language/txt/Sylvester_Collected_Papers_Volume_I_original_language_bookpp001_151.txt`
- `new_work_this_round/original_language/tex/sylvester_vol01_papers22_25_bookpp119_151.tex`
- `new_work_this_round/original_language/pdf/sylvester_vol01_papers22_25_bookpp119_151.pdf`
- `new_work_this_round/original_language/txt/sylvester_vol01_papers22_25_bookpp119_151.txt`

## Source scans

The package includes:
- a cumulative source PDF slice for book pp. 1-151;
- a new-work source PDF slice for book pp. 119-151;
- one cumulative PNG source scan per book page, book pp. 1-151;
- one new-work PNG source scan per book page, book pp. 119-151;
- source page manifests mapping book pages to source PDF pages.

The page offset remains:
`source_pdf_page = book_page + 18`.

## Verification

- The new-work standalone TeX compiles with `pdflatex`.
- The cumulative TeX compiles with `pdflatex`.
- Rendered PDF sample pages and source scan montages are included under `work_verification/renders_sample/`.

## Notes

The front-facing TeX/PDF/TXT contain only the reconstructed original-language mathematical text. They do not contain workflow commentary, translator notes, or chat/process remarks.

The densest proofing risk in this batch is Paper 22, especially the long determinant and syzygy formula chain on book pp. 129-134. It is source-checked against the scan, but it should still be prioritized in any later independent audit pass.
