# Build report

Build date: 2026-07-18 (Europe/Berlin).

## Toolchain

- Engine: XeTeX 3.141592653-2.6-0.999998, MiKTeX 26.5.
- Acceptance command: `xelatex -interaction=nonstopmode -halt-on-error -file-line-error <file.tex>`.
- Both documents received two final XeLaTeX passes.

An initial draft preflight exposed an undefined `\mathfrak`; `amssymb` was added before acceptance testing. The final two-pass builds below are clean.

## Acceptance results

| Artifact | Pages | Page size | Bytes | Final PDF SHA-256 |
|---|---:|---|---:|---|
| German standalone control | 1 | A4 | 26,555 | `23B322080568761507B7BAE3BD705192D243D2D5179007B643F02F39530E201C` |
| Korean translation | 1 | A4 | 54,626 | `ED36B34C58666926E34EAE7849908EB4A3B7F6151E1F4F48E33D559DF4845E32` |

Final log scans returned zero matches for fatal errors, undefined control sequences, missing characters, overfull boxes, underfull boxes, and LaTeX font warnings in both documents.

UTF-8 extraction with `pdftotext -enc UTF-8` returned 1,555 characters for the German control and 807 for the Korean PDF. Both extractions contain zero U+FFFD replacement characters and zero U+25A1 box characters. The corrected Korean final-equivalence clause is present in the extracted text.

Build gate: **pass**.
