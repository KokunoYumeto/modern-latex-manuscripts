# Build and visual-QA record: Noether Paper 3

Date: 2026-07-18

- two consecutive `pdflatex` passes completed with exit code 0 in the canonical `output/pdf` directory;
- final output is two A4 pages, PDF 1.5;
- the final-log scan found zero overfull/underfull boxes, LaTeX/package warnings, undefined controls, emergency stops, or fatal errors; the sole case-insensitive word `warning` occurs in the package description `infwarerr`, not in a diagnostic;
- the log records one benign `microtype` Info notice: character `029` has no protrusion setting in `T1/lmr/m/sc/10.95`, so that protrusion setting is ignored. This is not a missing body glyph; complete render inspection found the small-caps byline and all other text present and legible;
- `pdfinfo` confirms nonblank title, author, subject, and keywords;
- `pdftotext -layout` preserves the editorial prefix disclosure, all prose, six source-note labels, formulae (1) and (2), corrected total-rho index, less-than-or-equal relation, and article end;
- final PDF rendered at 180 dpi to `render_check/paper03-1.png` and `render_check/paper03-2.png`;
- both complete pages were visually inspected: no clipping, overlap, blank region caused by missing content, missing glyph, margin failure, or illegible formula was found;
- formula (1) remains fully contained on one line; formula (2) retains its two-line source grouping and all indices are visually legible;
- page 1 footnotes and page 2 footnotes are fully contained above the page numbers;
- `SOURCE_STRUCTURE_CHECK.csv` closes twelve source/layout checks, including all four emphasis boundaries and both formulas;
- `CORRECTION_LEDGER.csv` closes 26 correction/apparatus/metadata dispositions;
- `TERMINOLOGY_AND_ADVERSE_LEDGER.csv` retains external-review status honestly rather than treating internal agreement as independent evidence.

The operationally independent review separately rebuilt twice, rerendered both pages at 180 dpi, reproduced both stored render hashes, confirmed all fonts embedded, and returned PASS for this bounded unit.

Promoted artifact hashes:

- TeX: `E0FE64204D325B44F427570D311EC781C1119CF28420A4CD92138A51FC6F5CE5`;
- PDF: `51F4C7B884CF4A20F3DB031D0EA31C76575E03F903A89722CF6DF899A9477F4C`;
- final log: `A8840F61CEF98ABCFFEC0A5028732E1D165DC990B12931D58324D2C44C467954`;
- render page 1: `45A541D2C7CCDBA224C647C0E5CCA4318CFBA76DF12D02FBBA4668BBB21F94C9`;
- render page 2: `C309D99052616F7AA0223FA5BCA508F062044495D83F1A6C3CF1CF7D00241643`.

These object hashes were independently reverified. The final public checkpoint manifest and SHA index control the distributed package identity.
