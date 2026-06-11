# Sylvester Vol. I batch 26 status

Cumulative range: book pp. 1--493.

New work: book pp. 476--493, continuing Paper 57 through the beginning of Art. 42. The range continues the syzygetic-relation memoir: conjunctive factors, reciprocity of continued fractions, specialization to Sturm functions, rhizoristic series, and the beginning of the general construction of tau. The page 493 endpoint is a source-page boundary and stops mid-argument; next work resumes with the continuation of Art. 42 on book p. 494.

No graphical figures or standalone tables occur in the new range. The bracket products, syzygetic equations, continued fractions, zeta expressions, and tau formulas are encoded in TeX. No screenshots are used as edition content; PNG witnesses are present only under `new/img` for checking.

Audit/corrections while continuing:
- Corrected prior cumulative p.475 sign exponent in `\Syz_{m-i,0}` to `(-)^{(i-1)i/2}`, confirmed by the continuation on p.476.
- Corrected an old unclosed `\scriptsize` group in the cumulative TeX around an early combinatorial table; cumulative compilation no longer reports the end-inside-group warning.
- Ran a compactness-marker check: no missing source-page markers through p.493, no `includegraphics`, no screenshots/placeholders/TODO/not-transcribed markers. Hits for “omitted”/“summary” are Sylvester’s own wording, not editorial omissions.

Folder layout remains short: `cum`, `new`, `old`, `qa`, `aid`, `verify`.

The Vol. I future-aid package remains directly applicable through the rest of Volume I and is used as scan/page-map/witness support, not as OCR authority.

Compilation/rendering:
- `new/tex/Vol1_pp476_493.tex`: pdflatex passed.
- `cum/tex/Vol1_pp001_493.tex`: pdflatex passed after audit corrections.
- New-work PDF rendered to PNG; cumulative first/last pages rendered.

Next range starts at book p. 494, continuing Art. 42.
