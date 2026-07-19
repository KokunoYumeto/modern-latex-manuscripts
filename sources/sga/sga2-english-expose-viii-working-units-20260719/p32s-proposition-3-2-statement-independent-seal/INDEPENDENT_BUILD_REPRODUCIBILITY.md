# Independent build reproducibility

The independent reviewer rebuilt the unchanged 2,215-byte target TeX twice in
an isolated temporary directory with `pdflatex -interaction=nonstopmode
-halt-on-error`. Both passes exited zero. No target or source-evidence file in
this unit was changed by that rebuild.

- Frozen target PDF: 252,594 bytes, SHA-256
  `2F2C1049289DC9400DEAAA7F29B9D2AF2A9376859B5D6F269A17B66A3C4C8E85`.
- Independent rebuild PDF: 252,594 bytes, SHA-256
  `E4A205A9EEEE9DD7175CC1B8FC1F631C0CCAC4CAABF32BC3AC24E9CF120D1AEE`.
- The byte difference is the expected PDF timestamp variation. Extracted
  layout from frozen and rebuilt PDFs is byte-identical, SHA-256
  `827C69AD6B761954F05A9FF90B48BE7AF0FBF8B535DAECD812C66D28247A5ACC`.
- Independent 150-dpi renders are byte-identical, SHA-256
  `619279DEDB2152C145028BBF447B7DBB0C200456014B5C0477BFF0A20867FE8F`.
- Rebuilt output is one A4 page. All 17 listed fonts are embedded, subset, and
  Unicode-mapped. The second-pass diagnostic scan found zero LaTeX errors,
  undefined controls/references, rerun requests, or overfull/underfull boxes.

Temporary raw rebuild logs and the timestamp-variant PDF are not retained or
proposed for release because they contain local dependency paths or duplicate
the frozen target semantically. This file records the reproducibility result;
the public-safe producer logs remain the proposed build transcripts.
