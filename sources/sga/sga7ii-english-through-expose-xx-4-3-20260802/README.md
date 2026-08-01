# SGA 7 II English working reader through Expose XX Section 4.3

Open `reader/SGA7II_English_Through_Expose_XX_4_3_20260802.pdf`
to read the current cumulative English translation. The `source/` directory
contains its complete buildable TeX closure.

## Coverage

The reader contains complete English Exposes X through XIX and Expose XX
through Section 4.3. It has 212 A4 pages. The remainder of Expose XX and
Exposes XXI-XXII are excluded; the exact next cursor is Expose XX Section 4.4.

This is a current-progress working reader, not complete SGA 7 II, a critical
edition, peer review, mathematical certification, or an
accessibility-remediated edition. Its internal references have not yet received
an exhaustive cross-expose reference audit.

## Build

Run three XeLaTeX passes from `source/`:

```text
xelatex SGA7II_English_Through_Expose_XX_4_3_20260802.tex
xelatex SGA7II_English_Through_Expose_XX_4_3_20260802.tex
xelatex SGA7II_English_Through_Expose_XX_4_3_20260802.tex
```

The reader starts directly with the mathematics and contains no project-status
preface. `SGA7II_English_Through_Expose_XX_4_3_Reader_and_TeX_20260802.zip`
groups the PDF and buildable TeX for one-click use.
