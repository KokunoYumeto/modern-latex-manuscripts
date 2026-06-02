# Audit note - Noether Paper 05 and Paper 06 through §6

Scope completed in this package:

- Paper 05, `Rationale Funktionenkörper`, complete.
- Paper 06, `Körper und Systeme rationaler Funktionen`, title/front matter, introduction, and §§1--6 complete.
- Stopping point: immediately before Paper 06 §7 (`Beliebiges System ... Existenz der Rationalbasis.`).

Translation basis:

- German source excerpt is treated as authority.
- English control excerpt is included as a checking witness.
- Source scans for Paper 05 and Paper 06 are included for visual checking.
- Formula numbering, displayed equations, footnotes, and historical terminology are preserved in editable TeX.

Translation status:

- Spanish standalone: 12 pages.
- Japanese standalone: 14 pages.
- Spanish cumulative through Paper 06 §6: 75 pages.
- Japanese cumulative through Paper 06 §6: 86 pages.
- Declared gaps in completed range: none.

Terminology decisions:

- `Rationalbasis` -> Spanish `base racional`; Japanese `有理基底`.
- `Minimalbasis` -> Spanish `base mínima`; Japanese `最小基底`.
- `Integritätsbasis` -> Spanish `base de integralidad`; Japanese `整性基底`.
- `Funktionenkörper` -> Spanish `cuerpo de funciones`; Japanese `関数体`.
- `Involutionsform` / `Involutionsbasis` -> Spanish `forma de involución` / `base de involución`; Japanese `インヴォリューション形式` / `インヴォリューション基底`.
- `Übertragungsprinzip` -> Spanish `principio de transferencia`; Japanese `転移原理`.
- Lagrange's `Gattungsbereich/Gattungsbereiche` is retained in German italics where it is historically marked.
- `affektlos` is handled conservatively rather than silently modernized.

Build/assembly note:

- Standalone Spanish, Japanese, German source, and English control PDFs were compiled successfully before packaging.
- Spanish cumulative PDF was generated from the cumulative TeX by `pdflatex`.
- Japanese cumulative PDF was assembled with `pdfunite` from the verified previous cumulative PDF and the verified current Japanese standalone chunk; the full cumulative TeX is included for local Codex builds.
- Selected render checks are included for first/middle/last or new-tail pages.

Next recommended continuation: Paper 06 §§7--15.
