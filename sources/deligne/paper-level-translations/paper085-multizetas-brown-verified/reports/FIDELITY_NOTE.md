# Fidelity note - Deligne Paper 085

Paper: Pierre Deligne, **Multizêtas, d'après Francis Brown** / **Multizetas, after Francis Brown**.

Status of this package: Paper 085 source-grounded repair package.

## What is included

- English translation TeX and compiled PDF.
- French/source verified PDF built from the source/reference pages, plus a TeX wrapper that compiles those pages without screenshots.
- Source/reference PDF and extracted source text used for checking.
- Combined user/Codex workflow document.

## Coverage represented in the English layer

The English TeX/PDF covers the complete mathematical article: title block, Introduction, Sections 1 through 8, acknowledgements, and references. It includes the numbered theorem/proposition/corollary/lemma structure and the displayed equations/formula labels from the working source layer, including the Brown basis theorem, the iterated-integral formula, the pro-unipotent fundamental group formalism, motivic multizeta construction, mixed Tate motives, the space H(2,3), the motivic Galois action, and the proof sketches in Section 8.

## French/source layer decision

The earlier retyped French layer for Paper 085 was rejected from this package because its rendered output collapses source text and equations into an OCR-style block. To avoid shipping another bad French PDF, the French/source layer here is the verified source-reference PDF compiled through a LaTeX `pdfpages` wrapper. This preserves the full original-language mathematical content without screenshot substitution or OCR reflow.

## Compilation and render verification

- English translation PDF compiled with pdfLaTeX: 20 pages.
- French/source verified PDF compiled with XeLaTeX through `pdfpages`: 26 pages.
- Both PDFs were rendered successfully for visual smoke checking.

## Known limitation

The French/source layer is exact source-page inclusion rather than a clean retyped French TeX transcription. It is suitable for source grounding and cumulative bilingual reference, but a later typographic French TeX transcription could still be built if the project requires reflowable French source text. The rejected OCR/retyped layer is intentionally not shipped.
