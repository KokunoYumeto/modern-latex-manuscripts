# SGA 7 II English working reader through Expose XXI Section 4

Open `reader/SGA7II_English_Through_Expose_XXI_4_20260802.pdf`
to read the current cumulative English translation. The `source/` directory
contains its complete buildable TeX closure.

## Coverage

The reader contains complete English Exposes X through XX and Expose XXI
through Section 4 and its bibliography. It has 226 A4 pages. The Expose XXI
Section 5 appendix and Expose XXII are excluded; the exact next cursor is
Expose XXI Section 5.

This is a current-progress working reader, not complete SGA 7 II, a critical
edition, peer review, mathematical certification, or an
accessibility-remediated edition. Its internal references have not yet received
an exhaustive cross-expose reference audit.

## Build

Run three XeLaTeX passes from `source/`:

```text
xelatex SGA7II_English_Through_Expose_XXI_4_20260802.tex
xelatex SGA7II_English_Through_Expose_XXI_4_20260802.tex
xelatex SGA7II_English_Through_Expose_XXI_4_20260802.tex
```

The reader starts directly with the mathematics and contains no project-status
preface. `SGA7II_English_Through_Expose_XXI_4_Reader_and_TeX_20260802.zip`
groups the PDF and buildable TeX for one-click use.
