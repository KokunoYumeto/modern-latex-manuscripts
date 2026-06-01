# BATCH_REPORT — antenna_peeterjoot

**Source**: github.com/peeterjoot/ece1229-antenna — Peeter Joot, *Advanced Antenna Theory* (ECE1229 University of Toronto lecture notes, © 2015 Peeter Joot, LaTeX source under repo LICENSE).
**Translator**: auxiliary local run (Anthropic), lane lead: local project.
**Date**: 2026-06-01.
**Status**: **Pilot batch — 3 Maxwell-equations modules translated** as the foundational vocabulary anchor for the antenna/RF lane.

## Output
- `MaxwellsFieldAndSourceDescription_uk.tex` — field/source identification and SI units
- `MaxwellsStatement_uk.tex` — Maxwell's equations in time-domain (with magnetic sources)
- `MaxwellsTimeHarmonic_uk.tex` — Maxwell's equations in time-harmonic (phasor) form

## Why these three first
The repo has 71 .tex files (lecture notes + problem sets). Most are problem-set solutions which are highly notation-dependent. The three Maxwell files at the head of the corpus establish:
1. The Ukrainian vocabulary for E/H/D/B fields, currents, and charge densities.
2. The time-domain symmetric (with magnetic sources) Maxwell form used throughout antenna theory.
3. The time-harmonic / phasor form ($\partial_t \to j\omega$) needed for impedance, radiation, and aperture calculations.

This locks in the terminology that every later chapter (radiation integrals, antenna types, arrays, propagation) inherits.

## Translation policy
- All math notation preserved verbatim: `\spacegrad`, `\cross`, `\bcE`, `\BE`, `\PD{t}{\bcB}`, `\bcM`, `\bcJ`, `\bcD`, `q_\txte`, `q_\txtm`, `\rho`, `\rho_\txtm`.
- SI unit notation (`\si{V/m}` etc.) preserved.
- `\index{...}` entries translated to Ukrainian for proper indexing.
- Comments translated/added to explain the formulation.

## Terminology decisions
| EN | UK |
|---|---|
| electric field intensity | напруженість електричного поля |
| magnetic field intensity | напруженість магнітного поля |
| electric flux density (displacement vector) | електрична індукція (вектор зміщення) |
| magnetic flux density | магнітна індукція |
| electric current density | густина електричного струму |
| magnetic current density | густина магнітного струму |
| electric charge density | об'ємна густина електричного заряду |
| magnetic charge density | об'ємна густина магнітного заряду |
| primary fields / induced fields | первинні поля / індуковані поля |
| Maxwell's equations | рівняння Максвелла |
| time-harmonic | часо-гармонічний |
| phasor | фазор |

## Glossary additions proposed
- `electric field intensity → напруженість електричного поля`
- `magnetic field intensity → напруженість магнітного поля`
- `electric flux density / displacement vector → електрична індукція / вектор зміщення`
- `magnetic flux density → магнітна індукція`
- `current density → густина струму`
- `Maxwell's equations → рівняння Максвелла`
- `time-harmonic / phasor → часо-гармонічний / фазор`

## Next priorities (recommended)
After these foundational equations, the highest-leverage targets in the repo are:
1. **`ExPlaneWave.tex`** — plane wave example, establishes plane-wave vocabulary
2. **`advancedantennaL1.tex`** — Lecture 1, conceptual overview
3. **`chapter3Notes.tex`** (referenced by labels in MaxwellsStatement) — covers boundary conditions, radiation integrals
4. Problem set solutions can be left untranslated initially (notation-heavy, lower utility per token).

## Build note
Peeter Joot's repo uses custom macros (`\spacegrad`, `\cross`, `\bcE`, `\bcM`, `\PD`, `\txte`, `\txtm`, etc.) defined in style files (peeter_*.sty). To build the Ukrainian version, copy those .sty files alongside or set up a small preamble that mimics them.

## Coverage delta vs web model session
web model GPT-5.5 Pro session 02 has **zero RF/antenna coverage**. This is wholly additive — the antenna lane is structurally outside web model's pipeline.

