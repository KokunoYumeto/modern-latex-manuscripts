# Ukrainian applied-math translation lane — output index

Date: 2026-06-01.
Translator: auxiliary local run (Anthropic). lane lead: local project.

This output is **complementary to** web model GPT-5.5 Pro's session 01/02 native-Ukrainian authoring at `ukrainian_applied_math_core_tex_session{01,02}_20260601/`. web model is **synthesizing** a unified Ukrainian textbook covering state estimation, signal processing, Lie groups, PDE, optimization, and Kalman filters. The output here covers **lanes web model's session pipeline does NOT include**: wave-equation controllability, RF/antenna theory, and sensor fusion / SLAM-adjacent surveys.

## Three lanes delivered

### 1. Wave equation controllability (PDE / control theory)
**Folder**: `zuazua_wave_2402.17894/`
**Source**: arXiv:2402.17894 — Enrique Zuazua, *Exact Controllability and Stabilization of the Wave Equation* (Springer monograph).
**Delivered**: **Chapters 1, 2, 3 — full translations** (~2,000 lines). The complete linear-theory core: problem statement, boundary controllability via HUM, interior controllability via HUM, including hidden regularity, observability inequalities, weak solutions via transposition, geometric considerations (GCC, whispering gallery), 1D variable coefficients.
**Pending**: Chapter 4 (semilinear wave equation), Chapter 5 (volumetric stabilization), Chapter 6 (boundary stabilization), appendix.
**Lane status vs web model**: Not in web model's queue.

### 2. RF / Antenna theory
**Folder**: `antenna_peeterjoot/` and `sdr_survey_1804.06564/`

#### 2a. Antenna theory foundations and core engineering
**Source**: github.com/peeterjoot/ece1229-antenna — Peeter Joot, *Advanced Antenna Theory* (CC-licensed LaTeX lecture notes).
**Delivered**: **10 substantive files** (~3,000+ lines of Ukrainian, covering an introductory antenna-theory course):
- 4 Maxwell foundation modules (field/source description, time-domain with magnetic sources, time-harmonic/phasor, duality transformation)
- Lecture 1 full: antenna patterns, Poynting vector, isotropic radiator, radiation intensity, directivity, maximum directivity, beam solid angle, half-power beamwidth, Tai–Pereira approximation, worked examples (dipole, half-plane radiator)
- Chapter 2 notes full: rigorous Poynting derivation, dipole far-field solutions, intensity plots, phasor power, **RCS examples (flat plate, sphere, cylinder, trihedral corner reflector)**, Rayleigh/Mie/optical scattering, EIRP, free-space impedance derivation
- Chapter 4 notes full: linear wire antennas — magnetic vector potential, infinitesimal dipole radial dependence, far-field derivation with radial-component cancellation, plane-wave relations, transverse nature
- Polarization review: linear, elliptical, circular polarization with conic-form derivation
- Reciprocity theorem: derivation from phasor Maxwell, far-field integral form, TX/RX equivalence with vector identity proofs
- Chebyshev polynomials: full derivation, properties, application to Dolph–Chebyshev array synthesis
**Pending**: phasor Maxwell with electric+magnetic charges, energy-momentum with magnetic sources, plane wave example, fields incident on plane, corner reflector specifics, problem set solutions.
**Lane status vs web model**: Zero RF/antenna coverage in web model pipeline.

#### 2b. SDR architecture survey
**Source**: arXiv:1804.06564 — Akeela & Dezfouli, *Software-defined Radios: Architecture, State-of-the-art, and Challenges* (2018).
**Delivered**: Title, abstract, introduction (incl. abbreviations table), Concepts and Architecture (full), Design Approaches framing (criteria + concept-level summary of GPP/GPU/DSP/FPGA/co-design), Conclusion.
**Deferred**: Sections 4 (Development Tools) and 5 (Platforms) — 2018-specific commercial enumerations, low utility per token in 2026.
**Lane status vs web model**: web model has 1 small PySDR-derived module; the architectural survey is not in queue.

### 3. Sensor fusion (CV / SLAM / robotics)

#### 3a. Multi-sensor fusion for embodied AI
**Folder**: `sensor_fusion_2506.19769/`
**Source**: arXiv:2506.19769 — Ruan et al., *A Survey of Multi-sensor Fusion Perception for Embodied AI* (2025).
**Delivered**: **Full end-to-end translation** of all 9 sections (Abstract, Introduction, Background incl. datasets and tasks, Multi-modal Fusion methods, Multi-agent Fusion, Time-Series Fusion, MM-LLM Fusion, Open Challenges and Future Opportunities, Conclusion).
**Lane status vs web model**: Not in web model's queue.

#### 3b. Event-based sensor fusion for odometry
**Folder**: `sensor_fusion_2410.15480/`
**Source**: arXiv:2410.15480 — Zhang et al., *Event-based Sensor Fusion and Application on Odometry: A Survey* (2024, TIERS Lab Turku).
**Delivered**: **Full translation** of all included sections (Abstract, Intro, Event Camera Technology, Sensor Fusion for Odometry, Event-based Fusion subsections — event-only / +frame / +IMU / stereo VO / +LiDAR, Datasets table, Discussion, Conclusion).
**Mission relevance**: directly applicable to UAV navigation in GPS-denied/jammed environments, low-light operations, corridor/indoor reconnaissance, high-speed pose estimation.
**Lane status vs web model**: Not in web model's queue.

### 4. Autonomous robotics (UAV/UGV navigation)
**Folder**: `autonomous_robots_correll/`
**Source**: github.com/Correll-Lab/Introduction-to-Autonomous-Robots — Correll et al., open-source robotics textbook (CC BY-NC-SA).
**Delivered**: **Path Planning + Localization + Sensors + SLAM + Mapping + Vision chapters** — six full translations covering the entire autonomous perception+navigation+planning stack: Sensors (IMU, encoders, LiDAR, GPS, F/T) → Vision (image processing, convolution, Sobel/Canny/DoG/LoG, morphological, stereo + epipolar geometry, structured light) → Localization (Markov/Bayes/Particle/EKF) → Mapping (ICP, Octomap, RGB-D/TSDF) → SLAM (EKF + graph-based, loop closure) → Path Planning (Dijkstra/A*/RRT). A complete drone/UGV reference module in Ukrainian.
**Mission relevance**: every UAV/UGV navigation system uses these algorithms. Coverage planning is directly applicable to survey/reconnaissance/de-mining operations.
**Pending in this lane**: 25 more chapters in the book — most useful next: localization, SLAM, sensors, mapping, kinematics, vision, statistics, error propagation.
**Lane status vs web model**: web model lists `Autonomous Robots TeX` as pending; this chapter is the first delivery, complementary to whatever web model picks up next.

### 5. Robust Bayesian filtering (state estimation under outliers)
**Folder**: `roth_robust_filter_1703.02428/`
**Source**: arXiv:1703.02428 — Roth, Ardeshiri, Özkan, Gustafsson, *Robust Bayesian Filtering and Smoothing Using Student's $t$ Distribution* (2017, Linköping/Cambridge/METU).
**Delivered**: Focused translation — Abstract, Introduction, key $t$-distribution results (§2), filtering problem setup (§3), **full $t$-filter algorithm with all equations (§4.1)**, **drone tracking simulation example (§7.2)**, Concluding remarks. Deferred: deeper KLD-approximation diagrams, $t$-smoother derivation, appendices.
**Mission relevance**: drop-in robustness upgrade for any Kalman/EKF system. Filter equations are structurally identical to KF with one extra scalar covariance multiplier — retrofittable in ~10 lines of code. Validated on drone tracking with outliers + maneuvers. Directly useful for: GPS multipath/jamming, anti-drone camera tracking, INS with intermittent sensors, target maneuver handling.
**Lane status vs web model**: Not in web model's queue.

## Build targets ready (XeLaTeX + polyglossia)

- `sensor_fusion_2506.19769/` — full multi-file project; build `0_main.tex`. Figures and IEEEtran.cls included.
- `sdr_survey_1804.06564/` — single-file `paper_uk_core.tex`. Needs original `paper.bbl` renamed.
- `zuazua_wave_2402.17894/` — single chapter file `chapter01_uk.tex`; combine with original `book.tex` skeleton (after translating front-matter macros).
- `antenna_peeterjoot/` — three module files; need Peeter Joot's `peeter_*.sty` macros from source.

## Per-batch reports
Each folder has its own `BATCH_REPORT.md` with full terminology decisions, [[CHECK: ...]] flags, glossary additions proposed, and TODOs.

## Aggregate glossary additions to roll into `00_COMPLETE_CONTROL/terminology/UKRAINIAN_TERMINOLOGY_GUIDE.md`
(Consolidated from all 4 BATCH_REPORTs.)

**PDE / control theory**
- exact controllability → точна керованість
- stabilization → стабілізація
- wave equation → хвильове рівняння
- Hilbert Uniqueness Method (HUM) → Метод Гільбертової Єдиності
- observability inequality → нерівність спостережуваності
- damping → демпфування
- dissipation → дисипація
- semilinear → напівлінійний
- support (function) → носій
- finite speed of propagation → скінченна швидкість поширення

**Computer vision / sensor fusion / robotics**
- multi-sensor fusion perception (MSFP) → багатосенсорне сприйняття на основі злиття даних
- embodied AI → втілений ШІ
- point cloud → хмара точок
- voxel → воксель
- bird's-eye view (BEV) → вид з висоти пташиного польоту
- occupancy prediction → передбачення зайнятості
- bounding box → обмежувальна рамка
- self-attention → самоувага
- cross-attention → перехресна увага
- ego-motion → его-рух
- 3D object detection → 3D-детектування об'єктів

**SDR / RF / antenna**
- Software-defined Radio (SDR) → програмно-визначене радіо
- transceiver → трансивер
- baseband → базова смуга
- RF front end → РЧ-передній край
- digital front end → цифровий передній край
- Low Noise Amplifier (LNA) → малошумний підсилювач
- FPGA → програмована логічна матриця
- ASIC → інтегральна схема спеціального призначення
- co-design → спільне проектування
- Maxwell's equations → рівняння Максвелла
- electric/magnetic field intensity → напруженість електричного/магнітного поля
- electric/magnetic flux density → електрична/магнітна індукція
- current density → густина струму
- time-harmonic / phasor → часо-гармонічний / фазор

## Notes on workflow
- All translations preserve `\cite{}` keys, `\label{}`/`\ref{}`, `\eqref{}`, math notation, figure includes, and class-file structure for clean side-by-side EN/UK comparison.
- The `IEEEtran.cls` and `.bbl` files were copied from sources where present for buildability.
- `xelatex + polyglossia[ukrainian]` is the consistent build target, matching web model session preamble.

