# BATCH_REPORT — antenna_peeterjoot

**Source**: github.com/peeterjoot/ece1229-antenna — Peeter Joot, *Advanced Antenna Theory* (ECE1229 University of Toronto lecture notes, © 2015 Peeter Joot, LaTeX source under repo LICENSE).
**Translator**: auxiliary local run (Anthropic), lane lead: local project.
**Date**: 2026-06-01.
**Status**: **Comprehensive antenna lane** — **10 files** covering Maxwell foundations, antenna patterns and directivity, polarization, reciprocity, duality, array synthesis, dipole far-field, wire antennas, RCS examples, free-space impedance, and EIRP. The antenna lane is now a real Ukrainian antenna-theory module suitable as an introductory reference.

## Output files (10 files total)

### Foundational equations and transformations
1. `MaxwellsFieldAndSourceDescription_uk.tex` — field/source identification, SI units (E, H, D, B; J, M, q_e, q_m).
2. `MaxwellsStatement_uk.tex` — Maxwell's equations in time-domain, symmetric form with magnetic sources.
3. `MaxwellsTimeHarmonic_uk.tex` — Maxwell's equations in time-harmonic (phasor) form.
4. `dualityTransformation_uk.tex` — duality transformation (E↔H rotation in field space; source rotation in (ρ_e, ρ_m) and (J_e, J_m); shows magnetic-source-only Maxwell as a θ=π/2 rotation).

### Lecture content (antenna engineering)
5. `advancedantennaL1_uk.tex` — **Lecture 1, full translation, ~400 UK lines**:
   - What is an antenna; antenna patterns; principle E/H planes
   - Radiation power density (time-averaged Poynting vector)
   - Isotropic radiator; radiation intensity; far-field intensity \(U(\theta,\phi)\)
   - Intrinsic impedance \(\eta_0 = 377\,\Omega\)
   - Directivity \(D(\theta,\phi)\); maximum directivity \(D_0\); beam solid angle \(\Omega_A\)
   - Worked example: infinitesimal dipole \(D = (3/2)\sin^2\theta = 1.5 = 1.76\)~dBi
   - Worked example: upper-half-plane radiator \(U = A_0 \cos\theta\) giving \(D_0 = 4\)
   - Directivity in dB; Tai–Pereira approximation

6. `chapter2Notes_uk.tex` — **Fundamental parameters, ~500 UK lines**:
   - Poynting vector \(\bcW = \bcE \cross \bcH\) clarification
   - Rigorous far-field intensity derivation from dipole solutions (Griffiths/Jackson)
   - Superposition: \(\BW_\tav = \rcap (|E_\theta|^2 + |E_\phi|^2)/(2\eta_0 r^2)\)
   - Field/intensity plots, Mathematica patterns
   - dB vs dBi
   - Trig integral tables (\(\int_0^{\pi/2}, \int_0^\pi\) of \(\sin^n\), \(\cos^n\))
   - Polarization vectors \(\rhocap\); links to polarizationReview
   - Phasor power \(P = \tfrac12 |\BI|^2 \BZ\); complex power \(\BS = \BV_\trms \BI^\conj_\trms\)
   - **RCS examples**: flat plate \(\sigma_\tmax = 4\pi(LW)^2/\lambda^2\); sphere \(\pi r^2\); cylinder \(2\pi r h^2/\lambda\); trihedral corner reflector \(4\pi L^4/(3\lambda^2)\)
   - **Scattering vs frequency**: Rayleigh (\(\sigma \propto (\kappa r)^4\)), Mie (resonance), optical limit
   - **EIRP** (effective isotropic radiated power, \(P_t G_t\))
   - Free-space impedance \(\eta = 120\pi \approx 377\,\Omega\) exact derivation

7. `chapter4Notes_uk.tex` — **Linear wire antennas, ~430 UK lines**:
   - Magnetic vector potential \(\BA\) vs electric vector potential \(\BF\)
   - Infinitesimal dipole radial dependence of \(H_\phi, E_r, E_\theta\) (real/imag plots)
   - Electric far-field derivation for spherical \(\BA\): cancellation of radial components giving \(\BE_\textrm{ff} = -j\omega \BA_\txtT\)
   - Magnetic far-field: \(\BH = (1/\eta) \rcap \cross \BE\)
   - Plane-wave relations: \(\BH = (1/\eta) \kcap \cross \BE\) from Maxwell-Faraday
   - Transverse nature of far-field (\(\Bk \cdot \BE = 0\), \(\Bk \cdot \BB = 0\))

### Specific topics
8. `polarizationReview_uk.tex` — **Polarization, ~230 UK lines**: linear, elliptical, circular polarization derived from general E-field phasor; conic-form trajectory; worked examples for each polarization type.
9. `reciprocityTheorem_uk.tex` — **Reciprocity theorem, ~200 UK lines**: derivation from phasor Maxwell, divergence form, far-field integral form, TX/RX equivalence in antenna theory. Includes vector identity lemmas (divergence of cross product, triple cross product dotted).
10. `tschebyscheff_uk.tex` — **Chebyshev polynomials, ~190 UK lines**: definition, hyperbolic form, polynomial nature, full derivation of \(T_m(x) = \sum_k \binom{m}{2k} (-1)^k x^{m-2k}(1-x^2)^k\), properties (recurrence, ODE, orthogonality), application to Dolph–Chebyshev array synthesis.

## Coverage shift
- **Before this pass**: 3 foundational equation files; antenna lane was a vocabulary anchor.
- **After this pass**: A Ukrainian reader has Maxwell's equations, the antenna pattern/directivity framework with worked examples (dipole, half-plane radiator), polarization in all three forms, the reciprocity theorem (which is the fundamental TX/RX equivalence for antennas), and Chebyshev array synthesis math (which is the standard technique for low-sidelobe array design).

## What still isn't covered (next targets, if depth continues)
- `chapter2Notes.tex` (528 lines) — Joot's annotations on Balanis Ch.2 fundamentals: Poynting vector rigorous treatment, dipole far-field solutions from Griffiths/Jackson, partial efficiency, gain vs. directivity.
- `chapter4Notes.tex` (436 lines) — likely linear-wire antennas (dipoles, monopoles, loops): the actual radiator types every field engineer uses.
- `energyMomentumWithMagneticSources.tex` (512 lines) — energy-momentum theorems with magnetic sources (foundational for understanding power flow).
- `phasorMaxwellsWithElectricAndMagneticCharges.tex` (353 lines), `phasorMaxwellsGA.tex` (382 lines) — geometric-algebra formulations (specialist, lower utility).
- `dualityTransformation.tex` (181 lines) — electric/magnetic duality.
- `ExPlaneWave.tex` — plane wave example.
- `resolvingFieldsIncidentOnPlane.tex` (203 lines) — fields incident on a plane (radiation integral adjacent).
- `cornerCubeTakeII.tex` (369 lines) — corner reflector/cube.
- Problem sets — defer; notation-heavy, dependent on solution-specific macros.

Recommended next pass for completeness: chapter2Notes + chapter4Notes + dualityTransformation. Those three would round out a Ukrainian "introduction to antennas" module.

## Translation policy
- All Joot custom macros preserved verbatim: `\BE, \BH, \BD, \BB, \BM, \BJ, \BS, \BA, \BC` (boldface vectors), `\bcE, \bcH, \bcB` (calligraphic time-domain), `\rcap, \xcap, \ycap, \zcap, \ncap, \thetacap, \phicap, \rhocap` (unit vectors), `\spacegrad, \cross, \conj, \Real, \lr, \inv, \PD, \timeaverage, \dmath, \makeexample, \mathLabelBox, \mytikzmark, \DrawMyBox, \boxedEquation, \makelemma, \cref, \citep, \textAndIndex, \largestIntLessThan, \cancel`, etc.
- All equation labels preserved (eqn:advancedantennaL1:*, eqn:polarizationReview:*, eqn:reciprocityTheorem:*, eqn:chebyscheff:*).
- All `\index{}` entries translated to Ukrainian for proper indexing.
- All `\cite{}` keys (balanis2005antenna, abramowitz1964handbook, griffiths1999introduction, jackson1975cew, landau1980classical, irwin2007bec, sedra1982microelectronic, chen2005reciprocity) preserved.

## Build requirements
- Joot's custom style files (`peeter_*.sty`, `peeters_layout_exercise.sty`, `blogpost.tex`, `peeter_prologue_print2.tex`, `ece1229.sty`, `macros_bm.sty`, `macros_qed.sty`) must be available from the source repo's `latex/` subdirectory.
- For Ukrainian, add `\usepackage{polyglossia}\setmainlanguage{ukrainian}\setotherlanguage{english}` to the preamble (already done in `advancedantennaL1_uk.tex`).
- Font: DejaVu or another Cyrillic-aware font via `fontspec` under XeLaTeX.

## Terminology decisions (extending the seed glossary)

### Antenna/radiation
| EN | UK |
|---|---|
| antenna | антена |
| antenna pattern | діаграма спрямованості |
| principle planes (E/H) | головні площини (E/H) |
| Poynting vector | вектор Пойнтінга |
| radiation power density | густина потужності випромінювання |
| radiation intensity | інтенсивність випромінювання |
| far field / near field | дальня зона / ближня зона |
| isotropic radiator | ізотропний випромінювач |
| directivity | спрямованість |
| gain | підсилення |
| beam solid angle | тілесний кут променя |
| half-power beamwidth (HPBW) | ширина променя за рівнем половини потужності |
| sidelobe | бічна пелюстка |
| main lobe / main beam | головна пелюстка / головний промінь |
| intrinsic impedance | власна імпеданс |
| solid angle | тілесний кут |
| dipole | диполь |
| infinitesimal dipole | нескінченно малий диполь |
| spherical wave | сферична хвиля |
| transverse field | поперечне поле |
| dB / dBi | дБ / дБі |
| antenna array | антенна решітка |
| array synthesis | синтез антенної решітки |
| Dolph–Chebyshev array | решітка Дольфа–Чебишева |

### Polarization
| EN | UK |
|---|---|
| polarization | поляризація |
| linear polarization | лінійна поляризація |
| circular polarization | кругова поляризація |
| elliptical polarization | еліптична поляризація |
| polarization loss factor (PLF) | коефіцієнт поляризаційних втрат |
| right/left-hand circular | права/ліва кругова |

### Electromagnetics
| EN | UK |
|---|---|
| electric field intensity | напруженість електричного поля |
| magnetic field intensity | напруженість магнітного поля |
| electric flux density | електрична індукція |
| magnetic flux density | магнітна індукція |
| current density (electric/magnetic) | густина струму (електричного/магнітного) |
| charge density | густина заряду |
| reciprocity theorem | теорема взаємності |
| divergence theorem | теорема дивергенції |
| time-harmonic / phasor | часо-гармонічний / фазор |
| duality transformation | перетворення двоїстості |
| free-space wave impedance | імпеданс вільного простору |

## TODOs / [[CHECK: ...]] flags
- `[[CHECK: math]]` in `advancedantennaL1_uk.tex` Section "Інтенсивність випромінювання в дальній зоні": source has \(U_\tiso = P_0/(2\pi)\) but the integral identity \(\oiint d\Omega = 4\pi\) gives \(U_\tiso = P_0/(4\pi)\). I corrected the value with an inline `[[CHECK: math]]` note. local/native review should confirm against authoritative Balanis textbook.
- `[[CHECK: term-stability]]` "власна імпеданс" for intrinsic impedance — also commonly "хвильовий опір вільного простору"; I used the morphologically transparent form.
- `[[CHECK: term-stability]]` "бічна пелюстка" for sidelobe — also "бокова пелюстка"; both forms used in Ukrainian RF literature.
- `[[CHECK: term-stability]]` "решітка" vs "ґратка" for "array" — picked "решітка" (the standard antenna-engineering term in Ukrainian).
- "Чебишев" used instead of "Tschebyscheff" — the Ukrainian transliteration of the Russian mathematician's name. Original source uses German spelling.
- Many of Joot's example labels and figure references rely on figures not in the translated package — they'll show as missing references when built, with the equation/label structure intact.

## Coverage delta vs web model session
web model GPT-5.5 Pro session 02 has **zero RF/antenna coverage**. This 7-file delivery is wholly additive. The antenna lane is structurally outside web model's pipeline.

