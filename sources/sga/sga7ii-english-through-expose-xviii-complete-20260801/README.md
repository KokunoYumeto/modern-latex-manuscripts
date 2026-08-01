# SGA 7 II English working reader through complete Expose XVIII

Open `reader/SGA7II_English_Through_Expose_XVIII_Complete_20260801.pdf`
to read the current cumulative English translation. The `source/` directory
contains its complete buildable TeX closure.

## Coverage

The reader contains complete English Exposes X through XVIII, including the
terminal Corollary 6.7 and bibliography. It has 194 A4 pages. Exposes XIX
through XXII are excluded; the exact next cursor is the opening of Expose XIX.

This is a current-progress working reader, not complete SGA 7 II, a critical
edition, peer review, mathematical certification, or an
accessibility-remediated edition. Its internal references have not yet received
an exhaustive cross-expose reference audit.

## Build

Run three XeLaTeX passes from `source/`:

```text
xelatex SGA7II_English_Through_Expose_XVIII_Complete_20260801.tex
xelatex SGA7II_English_Through_Expose_XVIII_Complete_20260801.tex
xelatex SGA7II_English_Through_Expose_XVIII_Complete_20260801.tex
```

The reader starts directly with the mathematics and contains no project-status
preface. `SGA7II_English_Through_Expose_XVIII_Complete_Reader_and_TeX_20260801.zip`
groups the PDF and buildable TeX for one-click use.
