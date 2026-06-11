# Source and translation status

The project is source-first: use arXiv/GitHub/TeX/RST/Markdown whenever possible; use OCR/transcription only for gaps.

The original source-fetch stage contains exact arXiv/GitHub source manifests, a gap matrix, local translation batches, and task notes for preserving TeX/math. It was built so local local organizer can fetch native source tarballs and repository archives rather than OCR modern PDFs.

## Strong current modules

- Wave equation controllability: Zuazua chapters 1--3 are translated/staged and compiled as a standalone module.
- Sensor fusion: multi-sensor fusion survey and event-based fusion/odometry are staged as standalone modules.
- SDR/DSP: PySDR Ukrainian source lane is converted into a larger TeX module; SDR architecture survey is present.
- RF/antenna: Peeter Joot antenna/RF module is staged and format-checked.
- Robotics: Correll autonomous robots perception/navigation chapters are staged.
- Robust filtering: Roth Student-t robust filtering module is staged.
- Estimation spine: Solà ESKF and micro-Lie are present as partial/core modules, but need full expansion.

## Highest-value gaps

1. Full Solà ESKF source-preserved translation.
2. Full micro-Lie source-preserved translation.
3. Labbe Kalman notebooks converted into clean TeX chapters.
4. Event-based odometry and GNSS-denied VIO/SLAM current preprints integrated as mathematical modules.
5. FDM/FEM and optimization modules expanded for breadth.
