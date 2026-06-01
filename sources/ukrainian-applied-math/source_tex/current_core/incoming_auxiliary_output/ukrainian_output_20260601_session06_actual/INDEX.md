# Ukrainian applied-math translation lane — output index

Date: 2026-06-01.
Translator: auxiliary local run (Anthropic). lane lead: local project.

This output is **complementary to** web model GPT-5.5 Pro's session 01/02 native-Ukrainian authoring at `ukrainian_applied_math_core_tex_session{01,02}_20260601/`. web model is **synthesizing** a unified Ukrainian textbook covering state estimation, signal processing, Lie groups, PDE, optimization, and Kalman filters. The output here covers **lanes web model's session pipeline does NOT include**: wave-equation controllability, RF/antenna theory, and sensor fusion / SLAM-adjacent surveys.

## Three lanes delivered

### 1. Wave equation controllability (PDE / control theory)
**Folder**: `zuazua_wave_2402.17894/`
**Source**: arXiv:2402.17894 — Enrique Zuazua, *Exact Controllability and Stabilization of the Wave Equation* (Springer monograph).
**Delivered**: Chapter 1 (Presentation and Formulation) — full translation.
**Pending**: Chapters 2-6 + appendix.
**Lane status vs web model**: Not in web model's queue.

### 2. RF / Antenna theory
**Folder**: `antenna_peeterjoot/` and `sdr_survey_1804.06564/`

#### 2a. Antenna theory foundations
**Source**: github.com/peeterjoot/ece1229-antenna — Peeter Joot, *Advanced Antenna Theory* (CC-licensed LaTeX lecture notes).
**Delivered**: 3 Maxwell-equation foundational modules (`MaxwellsFieldAndSourceDescription`, `MaxwellsStatement` time-domain, `MaxwellsTimeHarmonic` phasor form) — full translation.
**Pending**: Plane waves, radiation integrals, antenna types, arrays. 68 source files remain.
**Lane status vs web model**: Zero RF/antenna coverage in web model pipeline.

#### 2b. SDR architecture survey
**Source**: arXiv:1804.06564 — Akeela & Dezfouli, *Software-defined Radios: Architecture, State-of-the-art, and Challenges* (2018).
**Delivered**: Title, abstract, introduction (incl. abbreviations table), Concepts and Architecture (full), Design Approaches framing (criteria + concept-level summary of GPP/GPU/DSP/FPGA/co-design), Conclusion.
**Deferred**: Sections 4 (Development Tools) and 5 (Platforms) — 2018-specific commercial enumerations, low utility per token in 2026.
**Lane status vs web model**: web model has 1 small PySDR-derived module; the architectural survey is not in queue.

### 3. Sensor fusion (CV / SLAM / robotics)
**Folder**: `sensor_fusion_2506.19769/`
**Source**: arXiv:2506.19769 — Ruan et al., *A Survey of Multi-sensor Fusion Perception for Embodied AI* (2025).
**Delivered**: **Full end-to-end translation** of all 9 sections (Abstract, Introduction, Background incl. datasets and tasks, Multi-modal Fusion methods, Multi-agent Fusion, Time-Series Fusion, MM-LLM Fusion, Open Challenges and Future Opportunities, Conclusion).
**Pending**: arXiv:2410.15480 (event-based sensor fusion for odometry) — separate paper in same lane, not yet started.
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

