# BATCH_REPORT — sensor_fusion_2410.15480

**Source**: arXiv:2410.15480 — Zhang et al., *Event-based Sensor Fusion and Application on Odometry: A Survey* (2024). TIERS Lab, University of Turku, Finland.
**Translator**: auxiliary local run (Anthropic), lane lead: local project.
**Date**: 2026-06-01.
**Status**: **Full translation** of all included sections (Abstract, Introduction, Event Camera Technology, Sensor Fusion for Odometry, Event-based Fusion for Odometry incl. all subsections, Datasets, Conclusion). Section 04-Experiment was commented out in source `main.tex` and is omitted; this matches the published version.

## Why this paper is mission-relevant
Event cameras combined with IMU / LiDAR / RGB are directly applicable to:
- **UAV navigation in GPS-denied/jammed environments** — high temporal resolution + low latency + high dynamic range gives robust odometry where GPS/inertial-only systems drift or visual systems get jammed by motion blur.
- **Indoor / urban / corridor reconnaissance** — overcomes the LiDAR "long corridor" drift problem by adding photometric information.
- **Low-light / harsh-lighting operations** — 140 dB dynamic range (vs 60–70 dB for traditional cameras) keeps the sensor useful at night, in smoke, in extreme contrast.
- **High-speed pose estimation** — Chamorro et al.'s 10 kHz event-based + 1 kHz IMU fusion = 100× state-of-the-art throughput.

## Output files
- `main.tex` — XeLaTeX + polyglossia + IEEEtran conference class.
- `Sections/00-Abstract.tex` through `Sections/06-Conclusion.tex` (skipping omitted 04-Experiment per source).
- `IEEEtran.cls`, `main.bbl`, `bibliography.bib`, `Figs/` copied from source.

## Build
```bash
cd sensor_fusion_2410.15480
xelatex -interaction=nonstopmode main.tex
xelatex -interaction=nonstopmode main.tex
```

## Translation policy
- All math notation preserved verbatim: \(\Delta L(x,y,t) = \log I(...) - \log I(t_\text{last}) = p \cdot C\), polarity \(p \in \{+1,-1\}\), contrast threshold \(C\).
- All bibliography keys preserved (lichtsteiner200564x64, gallego2020event, shariff2024event, weikersdorfer2012event, etc.; ~50 cites).
- Author block with ORCID IDs preserved in Latin.
- Author affiliation (TIERS Lab, University of Turku) kept in original.
- Vendor names (Prophesee, IniVation, Lucid, Sony) kept in original Latin.
- Dataset names (CoSEC, ECMD, UNIZG-FER LAMOR, Evimo2, DSEC, MVSEC, DAVIS) kept in original Latin.
- System/algorithm names (Fast-LIO, COIN-LIO, VINS-Mono, Kimera-VIO, EVO, ESVO2, etc.) kept in original Latin.

## Terminology additions
| EN | UK |
|---|---|
| event camera | подієва камера |
| event-based sensor fusion | сенсорне злиття на основі подій |
| asynchronous sensor | асинхронний сенсор |
| visual odometry (VO) | візуальна одометрія (VO) |
| visual-inertial odometry (VIO) | візуально-інерціальна одометрія (VIO) |
| LiDAR-inertial odometry | LiDAR-інерціальна одометрія |
| motion blur | розмиття руху |
| drift | дрейф |
| dynamic range | динамічний діапазон |
| temporal resolution | часова роздільна здатність |
| latency | затримка |
| contrast threshold | контрастний поріг |
| polarity (event) | полярність (події) |
| stereo event camera | стерео-подієва камера |
| disparity | диспаратність |
| feature track | трек ознак |
| direct sparse odometry (DSO) | пряма розріджена одометрія (DSO) |
| event-aided DSO | подія-підтримана DSO |
| 6-DoF (degrees of freedom) | 6 ступенів свободи (6-DoF) |
| extrinsic calibration | зовнішнє калібрування |
| inertial measurement unit (IMU) | інерціальний вимірювальний модуль (IMU) |
| pose estimation | оцінювання пози |
| Kalman filter (iterative) | (ітеративний) фільтр Калмана |
| photometric information | фотометрична інформація |
| dense / sparse depth map | щільна / розріджена карта глибини |
| scene flow | потік сцени |

## TODOs / [[CHECK: ...]] flags
- All cites preserved as in source; bibliography.bib is in Latin and ready for build.
- `[[CHECK: term-stability]]` "подієва камера" for event camera — chosen as the morphologically transparent Ukrainian calque. Alternative: "ивент-камера" (transliteration) which is used in some Ukrainian RF tech informal contexts. The calque is preferred for technical writing.
- `[[CHECK: term-stability]]` "розмиття руху" for motion blur — also "змаз руху", but "розмиття" is the standard.
- `[[CHECK: term-stability]]` "трек ознак" for feature track — could also be "слід ознак". "Трек" is the standard in robotics literature.

## Coverage delta vs web model session
web model GPT-5.5 Pro session 02 lists arXiv:2410.15480 as **not in its pipeline**. The companion paper arXiv:2506.19769 (multi-sensor fusion for embodied AI) is also not in its pipeline; together these two surveys give Ukrainian researchers a complete modern picture of sensor fusion for state estimation: 2506.19769 for the multi-modal/multi-agent/MM-LLM landscape, and 2410.15480 for the specific event-camera-based odometry application.

