# BATCH_REPORT — zuazua_wave_2402.17894

**Source**: arXiv:2402.17894 — Enrique Zuazua, *Exact Controllability and Stabilization of the Wave Equation* (Springer, 2024 monograph; arXiv version 2024-02).
**Translator**: auxiliary local run (Anthropic), lane lead: local project.
**Date**: 2026-06-01.
**Status**: **Chapter 1 complete** (Presentation and Formulation of Controllability and Stabilization Problems; ~360 source lines, full translation).

The monograph has 6 chapters + appendix. This batch delivers the keystone chapter, which:
- Defines the wave equation with Dirichlet BC
- States the exact controllability problem (interior, localized, boundary)
- States the stabilization problem (volumetric, localized, boundary dissipation)
- Sketches the energy method for proving exponential decay under bounded damping
- Outlines the rest-of-book plan

Chapters 2 through 6 + appendix pending.

## Output
- `chapter01_uk.tex` — full Ukrainian translation, all equations, labels, refs, citations preserved.

## Translation policy
- All math notation (Δ, ∇, $H^1_0$, $L^2$, ξ, ω, $\chi_\omega$, $\Gamma$, $\Omega$, etc.) preserved verbatim.
- All equation labels (`eqI01` through `eqI25`) preserved.
- All cross-references to other chapters (chapter02 — chapter06) and cite keys (brezis1973operateurs, haraux1987semi, lions1988controlabilite, etc.) preserved.
- Prose translated; "in" / "on" qualifiers around equation systems translated to "в" / "на" (Ukrainian preposition use for "in the domain"/"on the boundary" is asymmetric like English).
- Mathematical English idioms ("if and only if", "of class $C^2$", "energy space", "Hilbert Uniqueness Method") translated to standard Ukrainian mathematical Ukrainian.

## Terminology decisions
| EN | UK |
|---|---|
| exact controllability | точна керованість |
| stabilization | стабілізація |
| wave equation | хвильове рівняння |
| Dirichlet boundary condition | гранична умова Діріхле |
| Neumann boundary condition | гранична умова Неймана |
| boundary control | граничне керування |
| internal (interior) control | внутрішнє керування |
| localized | локалізований |
| feedback / closed-loop | зворотний зв'язок / замкнений контур [seed glossary] |
| open-loop | відкритий контур |
| energy space | енергетичний простір |
| energy conservation law | закон збереження енергії |
| time-reversibility | оборотність у часі |
| trajectory | траєкторія [seed glossary] |
| equilibrium state | рівноважний стан |
| exponential decay | експоненційне затухання |
| damping (term) | демпфування |
| dissipation / dissipative | дисипація / дисипативний |
| Hilbert Uniqueness Method (HUM) | Метод Гільбертової Єдиності (HUM) |
| observability inequality | нерівність спостережуваності |
| unique continuation principle | принцип єдиного продовження |
| multiplier technique | техніка множників |
| semilinear (wave equation) | напівлінійне (хвильове рівняння) |
| globally Lipschitz | глобально ліпшицев(а) |
| eigenvalue | власне значення |
| characteristic function | характеристична функція |
| support (of a function) | носій |
| finite speed of propagation | скінченна швидкість поширення |

## Glossary additions proposed
- `exact controllability → точна керованість`
- `stabilization → стабілізація`
- `feedback (control) → зворотний зв'язок` (already in seed)
- `observability inequality → нерівність спостережуваності`
- `damping → демпфування` (alternative: затухання)
- `dissipation → дисипація`
- `wave equation → хвильове рівняння` (already in seed)

## Pending chapters (high-value, source-backed)
| Chapter | Estimated source lines | Focus |
|---|---|---|
| chapter02 | TBD | Boundary controllability via HUM |
| chapter03 | TBD | Internal localized controllability |
| chapter04 | TBD | Semilinear wave equation + fixed-point argument |
| chapter05 | TBD | Stabilization: volumetric nonlinear dissipation |
| chapter06 | TBD | Boundary dissipation |
| appendix | TBD | Auxiliary lemmas/PDE estimates |

## TODOs / [[CHECK: ...]] flags
- `[[CHECK: math]]` — Eq.~(\ref{eqI19}): The Young-style estimate splits the integral with weights $\lambda_1/(2a_1)$ and $a_1/(2\lambda_1)$; check the canonical Ukrainian-textbook presentation of this estimate against the rendering.
- `[[CHECK: term-stability]]` — "оборотність у часі" for time-reversibility: alternative "інверсія часу" is also used in physics. I chose оборотність because it carries the reversibility (not pure inversion) connotation.
- `[[CHECK: term-stability]]` — "метод множників" (multiplier method): also rendered as "метод мультиплікаторів" in some Ukrainian PDE texts. The seed glossary does not specify.

## Coverage delta vs web model session
web model GPT-5.5 Pro session 02 lists Zuazua arXiv:2402.17894 as **not in its pipeline**. This translation is wholly additive and fills the PDE/control lane.

