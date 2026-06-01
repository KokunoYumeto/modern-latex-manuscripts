# BATCH_REPORT — zuazua_wave_2402.17894

**Source**: arXiv:2402.17894 — Enrique Zuazua, *Exact Controllability and Stabilization of the Wave Equation* (Springer, 2024 monograph; arXiv version 2024-02).
**Translator**: auxiliary local run (Anthropic), lane lead: local project.
**Date**: 2026-06-01.
**Status**: **Chapters 1, 2, 3 complete** — the full linear-theory core (problem statement, boundary controllability via HUM, interior controllability via HUM). The reader has the complete linear controllability machinery: HUM construction, hidden regularity (direct inequality), observability (inverse inequality), main controllability theorems, weak solutions via transposition, geometric considerations (GCC), variable coefficients in 1D, and substantial comments.

Chapters 4 (semilinear wave equation), 5 (volumetric stabilization), 6 (boundary stabilization), and appendix pending.

## Output files
- `chapter01_uk.tex` — Presentation and Formulation (352 lines, full translation; the problem statement)
- `chapter02_uk.tex` — Boundary Controllability via HUM (~1000 lines, full translation; the HUM keystone with hidden regularity, observability, main theorem, transposition method, geometric considerations, 1D variable coefficients, comments on plates/Schrödinger/numerics)
- `chapter03_uk.tex` — Interior Controllability (~600 lines, full translation; HUM adaptation, 4-step inverse inequality proof with compactness-uniqueness, 1D variable coefficients, comments including whispering gallery phenomenon, singular limit to boundary control)

## Status mapping
| Source chapter | Source lines | UK lines | Status |
|---|---|---|---|
| chapter01.tex | 360 | 352 | DONE |
| chapter02.tex | 1117 | ~1000 | DONE |
| chapter03.tex | 805 | ~600 | DONE |
| chapter04.tex | 1368 | — | pending (semilinear) |
| chapter05.tex | 979 | — | pending (volumetric stabilization) |
| chapter06.tex | 1241 | — | pending (boundary stabilization) |
| appendix.tex | 78 | — | pending |

## Translation policy applied throughout
- All math notation preserved verbatim (operators, function spaces, norms, equation labels eqI01–eqI25, eqII01–eqII80, eqIII01–eqIII75).
- All cross-references to chapters (e.g., `\ref{chapter04}`, `\ref{theorem:II.2.1}`) preserved.
- All `\cite{}` keys preserved (brezis1973operateurs, hormander1976analysis, lions1988controlabilite, bardos1992sharp, komornik1987controlabilite, etc. — ~50 distinct references).
- All theorem/lemma/proof/remark environment labels preserved.
- Author block, dedication, biblio kept original.

## Cumulative terminology (chapters 1-3)
**Core**:
- exact controllability → точна керованість
- stabilization → стабілізація
- wave equation → хвильове рівняння
- Dirichlet/Neumann boundary condition → гранична умова Діріхле/Неймана
- boundary / interior / localized control → граничне / внутрішнє / локалізоване керування
- feedback / closed-loop → зворотний зв'язок / замкнений контур
- open-loop → відкритий контур
- energy space → енергетичний простір
- finite speed of propagation → скінченна швидкість поширення

**Function spaces** (kept Latin notation): $L^2(\Omega)$, $H_0^1(\Omega)$, $H^{-1}(\Omega)$, $L^\infty(0,T;X)$, $W^{1,\infty}$, $BV$, $\mathcal{D}(\Omega)$, $C^k(\overline{\Omega})$.

**Method-specific**:
- Hilbert Uniqueness Method (HUM) → Метод Гільбертової Єдиності (HUM)
- multiplier method / technique → метод множників
- hidden regularity → прихована регулярність
- direct inequality / inverse inequality → пряма нерівність / обернена нерівність
- observability inequality → нерівність спостережуваності
- equipartition of energy → рівнорозподіл енергії
- unique continuation → єдине продовження
- compactness-uniqueness argument → аргумент компактність–єдиність
- transposition method → метод транспозиції
- weak solution → слабкий розв'язок
- Holmgren's theorem → теорема Гольмгрена
- Geometric Control Condition (GCC) → геометрична умова керування (GCC)
- microlocal analysis → мікролокальний аналіз
- bicharacteristic ray → біхарактеристичний промінь
- geometric optics → геометрична оптика
- Carleman inequality → нерівність Карлемана
- whispering gallery → ``шепочучі галереї''
- admissible controls → допустимі керування
- minimal-norm control → керування мінімальної норми
- semilinear → напівлінійний
- globally Lipschitz → глобально ліпшицев
- damping / dissipation → демпфування / дисипація
- non-diffractive point → недифракційна точка
- ray of geometric optics → промінь геометричної оптики
- self-adjoint elliptic operator → самоспряжений еліптичний оператор

## Glossary additions to roll into UKRAINIAN_TERMINOLOGY_GUIDE.md
All terms in the table above. Highest-value additions to the seed glossary (which currently lacks PDE/control vocabulary):
- exact controllability, stabilization, observability inequality, HUM, multiplier method, geometric control condition, microlocal analysis, Carleman inequality, hidden regularity, transposition method, weak solution.

## TODOs / [[CHECK: ...]] flags
- `[[CHECK: term-stability]]` "оборотність у часі" vs "інверсія часу" for time-reversibility — picked оборотність throughout.
- `[[CHECK: term-stability]]` "метод множників" — alternative "метод мультиплікаторів". Seed glossary silent; picked the morphologically transparent form.
- `[[CHECK: term-stability]]` "недифракційна точка" for non-diffractive point — checked against Bardos-Lebeau-Rauch's framework; no Ukrainian canonical translation found in my training corpus; this is a faithful calque.
- `[[CHECK: term-stability]]` "шепочучі галереї" for whispering gallery — quoted on first use; physics literature in Ukrainian also uses this.
- `[[CHECK: math]]` All 25+80+75 = ~180 numbered equations preserved with original labels; spot-check a few against the source LaTeX before publishing.

## Coverage delta vs web model session
web model GPT-5.5 Pro session 02 lists Zuazua arXiv:2402.17894 as **not in its pipeline**. The chapters 1-3 here provide a complete linear-theory Ukrainian module on exact controllability of the wave equation. This is wholly additive to the multi-AI translation lane.

## Build
```bash
cd zuazua_wave_2402.17894
# Combine with the original book.tex skeleton (or write a minimal driver):
# \documentclass{svmono}
# \usepackage{fontspec}\setmainfont{DejaVu Serif}
# \usepackage{polyglossia}\setmainlanguage{ukrainian}\setotherlanguage{english}
# \usepackage{amsmath,amssymb,...}
# \begin{document}
#   \include{chapter01_uk}
#   \include{chapter02_uk}
#   \include{chapter03_uk}
# \end{document}
xelatex driver_uk.tex
```
The source `book.tex`, biblio (`biblio.bib`, `book.bbl`), and figures (`fig01-chap02-sec2_3.eps`, `fig02-chap03-sec3_2.eps`) come from the arXiv source bundle.

