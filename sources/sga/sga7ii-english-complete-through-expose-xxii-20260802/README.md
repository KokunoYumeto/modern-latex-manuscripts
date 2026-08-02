# SGA 7 II complete English working reader

Open `reader/SGA7II_English_Complete_Through_Expose_XXII_20260802.pdf`
to read the complete current English working translation. The `source/`
directory contains its complete buildable TeX closure.

## Coverage

The reader contains all SGA 7 II Exposes X through XXII and ends at the
volume bibliography. It has 264 A4 pages and no continuation cursor.

This is a complete working translation of SGA 7 II, not a critical edition,
peer review, mathematical certification, accessibility-remediated edition,
or complete SGA 1-7.2 reader. Its internal references have not yet received
an exhaustive cross-expose reference audit.

## Build

Run three pdfLaTeX passes from `source/`:

```text
pdflatex SGA7II_English_Complete_Through_Expose_XXII_20260802.tex
pdflatex SGA7II_English_Complete_Through_Expose_XXII_20260802.tex
pdflatex SGA7II_English_Complete_Through_Expose_XXII_20260802.tex
```

The reader starts directly with the mathematics and contains no workflow or
project-status preface. The reader/buildable-TeX ZIP groups the PDF and full
editable closure for one-click use.
