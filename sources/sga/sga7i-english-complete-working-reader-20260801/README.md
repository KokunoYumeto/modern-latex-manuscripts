# SGA 7 I complete English working reader

Open `reader/SGA7I_English_Complete_Working_Reader_20260801.pdf` to read the
current cumulative English translation. The `source/` directory is its complete
buildable TeX closure.

## Coverage

This reader covers all written exposes in SGA 7 I: I, II, VI, VII, VIII, and
IX, including their bibliographies and the terminal publisher matter. It ends
at the end of the available SGA 7 I source; there is no continuation cursor.

The reader is a complete working translation of the volume, not a critical
edition, peer review, mathematical certification, or accessibility-remediated
edition. Its internal-reference layer has not received an exhaustive
reference-v2 audit.

## Build

Run three passes from `source/`:

```text
pdflatex SGA7_I_English_source_first_workpass.tex
pdflatex SGA7_I_English_source_first_workpass.tex
pdflatex SGA7_I_English_source_first_workpass.tex
```

See `RIGHTS_AND_PROVENANCE.md` for the source and attribution boundary.
