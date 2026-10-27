# Elements of Algebraic Geometry — English edition

This folder holds the English edition as published in [ega-en](https://github.com/KokunoYumeto/ega-en) on 25 October 2026 (commit ac48183). The French editions are in [ega-fr](https://github.com/KokunoYumeto/ega-fr).

Alexandre Grothendieck, with the collaboration of Jean Dieudonné, *Éléments de géométrie algébrique*, Chapters 0–IV,
in English. The original appeared in the *Publications mathématiques de l'IHÉS* 4, 8, 11, 17, 20, 24, 28 and 32
(1960–1967).

## Read

[pdf/EGA_EN.pdf](pdf/EGA_EN.pdf), 1,768 pages: the Introduction; Chapter 0, §§1–23; Chapters I–IV; and the
bibliographies, indexes, errata and addenda of the original volumes, each after the chapter it belongs to.

- Every numbered paragraph keeps its original number, and cross-references such as (IV, 17.5.1) are links.
- The page numbers of the original printing are in the margin: [IV-2 | 19] is page 19 of the second part of
  Chapter IV.

## Translation

The text is AI-translated from the French transcription in [ega-fr](https://github.com/KokunoYumeto/ega-fr):

- by Claude Opus 5.5 (Anthropic): the Introduction; Chapter 0, §§1–11 and 14; Chapter I; Chapter II with its
  errata; Chapter III, §§1 and 3; Chapter IV: its introduction, §§1, 16, 17 and 20, and the bibliography and
  indexes that close its first part;
- by OpenAI Codex models (GPT-6 Astra, GPT-5.6 Sol): the other sections.

The mathematics, the numbering and the cross-references follow the French transcription.

## Sources

[tex/](tex) holds the LaTeX sources of the PDF. To build it, run `pdflatex EGA_EN.tex` in `tex/` until LaTeX no
longer asks for a rerun (five passes).

[Rights](LICENSE) · [Purpose](PURPOSE.md)

---

[Sponsor this work](https://github.com/sponsors/KokunoYumeto)
