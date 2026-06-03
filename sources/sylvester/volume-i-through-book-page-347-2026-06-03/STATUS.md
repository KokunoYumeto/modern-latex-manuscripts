# Sylvester Vol. I batch 18 status

Cumulative endpoint: book pp. 1--347.

New work this round: Paper 43, book pp. 328--347 / source PDF pp. 346--365. This covers Part I, Section IV and the opening of Section V of “On the Principles of the Calculus of Forms.”

Short-path layout retained for Windows path-length safety:
- cum/
- new/
- old/
- qa/
- aid/
- verify/

Key files:
- cum/tex/Vol1_pp001_347.tex
- cum/pdf/Vol1_pp001_347.pdf
- cum/txt/Vol1_pp001_347.txt
- cum/scan_pdf/src_019_365_book001_347.pdf
- new/tex/Vol1_p43_pp328_347.tex
- new/pdf/Vol1_p43_pp328_347.pdf
- new/txt/Vol1_p43_pp328_347.txt
- new/scan_pdf/src_346_365_book328_347.pdf
- new/img/src346_book328.png through src365_book347.png
- qa/audit_001_347.json

Coverage notes:
- No graphical figures occur in the new range.
- The condition list/table and determinant/operator arrays are encoded in TeX.
- No screenshots are used as substitutes for mathematical displays.
- The aid package was useful for witness pages and source mapping; OCR was not treated as authoritative.

Build checks:
- new-work pdflatex: passed
- cumulative pdflatex: passed
- new-work PDF rendered to PNG for spot verification
- cumulative first/last pages rendered for spot verification

No current intake/backfill gap found for the active Sylvester path. Next range starts at book p. 348, continuing Paper 43.
